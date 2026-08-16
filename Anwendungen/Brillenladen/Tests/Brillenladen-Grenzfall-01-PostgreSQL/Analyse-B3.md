
Die Beobachtungen passen auffallend gut zu einem **sessiongebundenen Prepared-Statement-/Plan-Cache-Effekt bei stark schiefer Datenverteilung**. Das ist zunächst eine Hypothese, kein bereits nachgewiesener Befund. Die Aufgabenstellung selbst sichert nur das Fünf-/Sechs-Muster, die Wertabhängigkeit, den Reset durch eine neue Connection und die schnelle Literal-Abfrage.  

### 1. Führende Hypothese

**PostgreSQL wechselt für das parametrisierte Prepared Statement von wertabhängigen Custom Plans zu einem wertunabhängigen Generic Plan; dieser Generic Plan ist wegen der stark ungleichen Werteverteilung für die seltenen Werte schlecht.**

Der Mechanismus erklärt nahezu alle charakteristischen Beobachtungen gemeinsam:

* Bei `plan_cache_mode=auto` führt PostgreSQL ein parametrisiertes Prepared Statement zunächst fünfmal mit Custom Plans aus. Danach wird ein Generic Plan betrachtet und gegebenenfalls für weitere Ausführungen verwendet. Ein Custom Plan kennt den konkreten Parameterwert, ein Generic Plan nicht. ([PostgreSQL][1])
* Bei stark schiefer Verteilung kann genau diese fehlende Kenntnis entscheidend sein. Denkbares Beispiel, **nicht festgestellter Befund**: Der Generic Plan verwendet einen Plan, der für häufige Werte vernünftig ist, für einen seltenen Wert aber erheblich mehr Arbeit macht als ein speziell dafür geplanter Indexzugriff.
* Die Literal-Abfrage kann dagegen beim Planen den konkreten Wert berücksichtigen und daher einen anderen, schnellen Plan bekommen. ([PostgreSQL][2])
* Prepared Statements und ihre Planhistorie sind sessiongebunden. Eine neue Verbindung beseitigt diesen Zustand, was zum beobachteten Neustart des Musters passt. ([PostgreSQL][3])

**Wichtige Einschränkung:** Bei Java/pgJDBC gibt es noch eine zweite relevante Fünfer-Schwelle. pgJDBC hat standardmäßig `prepareThreshold=5` und wechselt ungefähr an dieser Stelle auf ein benanntes serverseitiges Prepared Statement. ([jdbc.postgresql.org][4]) Daher beweist „fünf schnell, ab sechs langsam“ für sich allein noch nicht, dass bereits PostgreSQLs Generic-Plan-Heuristik die konkrete Ursache ist. Es macht die ganze Prepared-Statement-/Plan-Cache-Richtung aber besonders verdächtig.

### 2. Alternativen

1. **pgJDBC-Schwelleneffekt ohne problematischen Generic Plan.** Der Breakpoint könnte primär durch `prepareThreshold=5` und den Wechsel auf serverseitiges Prepare entstehen. Der exakte Schwellenwert würde dazu passen. ([jdbc.postgresql.org][4])

2. **Ein anderer sessionlokaler Zustand ändert sich reproduzierbar nach einigen Ausführungen.** Beispielsweise könnte die Anwendung selbst Session-Einstellungen oder Statement-Zustand verändern. Dafür enthält der Fall aber bislang keinen positiven Befund.

3. **Parameter-Typisierung bzw. ein planungsrelevanter Unterschied zwischen parametrisierter und Literal-Abfrage.** Das könnte unterschiedliche Pläne erklären. Allein erklärt es den exakt reproduzierbaren Fünf-/Sechs-Übergang jedoch schlechter als die Prepared-Statement-Hypothese.

Globale CPU-, RAM- oder I/O-Sättigung ist nach den gegebenen Beobachtungen keine besonders starke Haupthypothese: Sie erklärt weder die exakte Session-Schwelle noch den Reset durch eine neue Verbindung gut. Das ist aber kein Beweis, dass lokale I/O- oder Warteeffekte ausgeschlossen wären.

### 3. Kürzester trennender Test

Die diagnostisch stärkste kleine Intervention ist, **auf derselben JDBC-Connection für den Test `plan_cache_mode = force_custom_plan` zu setzen und denselben seltenen Parameterwert mehr als sechs Mal auszuführen**.

Wenn der Sprung ab der sechsten Ausführung verschwindet und die Ausführungen schnell bleiben, ist die Generic-Plan-Erklärung sehr stark gestützt. PostgreSQL dokumentiert `force_custom_plan` ausdrücklich als Möglichkeit, die automatische Generic-/Custom-Wahl zu überschreiben. ([PostgreSQL][1])

Bleibt der Sprung trotzdem bestehen, würde ich als **unmittelbar nächsten** Test den pgJDBC-`prepareThreshold` verändern, etwa serverseitiges Prepare mit `prepareThreshold=0` testweise deaktivieren. Wandert oder verschwindet damit der Breakpoint, liegt der relevante Übergang auf der Treiber-/Server-Prepare-Grenze statt beim späteren Generic-Plan-Entscheid. ([jdbc.postgresql.org][5])

Zusätzlich lässt sich, sofern die PostgreSQL-Version die Spalten anbietet, innerhalb derselben Session in `pg_prepared_statements` unmittelbar nachsehen, ob `custom_plans` bzw. `generic_plans` hochgezählt werden. Diese View erfasst auch über das Frontend/Backend-Protokoll angelegte Prepared Statements. ([PostgreSQL][3])

### 4. Was für eine belastbare Diagnose noch fehlt

Es fehlt vor allem die **tatsächliche Plan-Evidenz**. Noch ist nicht gezeigt, dass die schnelle und die langsame Ausführung verschiedene Pläne besitzen oder dass bei der langsamen Ausführung wirklich ein Generic Plan verwendet wird.

Belastbar wäre die Diagnose, wenn man für denselben seltenen Wert etwa folgende Kette belegt: vor dem Umschlag Custom Plan + schnell; danach Generic Plan + langsam; unter `force_custom_plan` weiterhin Custom Plan + wieder schnell. PostgreSQL weist darauf hin, dass sich bei `EXPLAIN EXECUTE` ein Generic Plan typischerweise dadurch erkennen lässt, dass `$1` im Plan stehen bleibt, während beim Custom Plan der konkrete Parameterwert erscheint. ([PostgreSQL][2])

**Kurzfassung:** Zuerst nicht Cache, Hardware oder Indexe allgemein untersuchen. Zuerst den **Custom-vs.-Generic-Plan-Verdacht** mit `force_custom_plan` testen. Falls das den Effekt nicht beseitigt, als Nächstes den **pgJDBC-`prepareThreshold`** variieren. Diese zwei kleinen Experimente trennen die naheliegendsten Ursachen deutlich schneller als eine breite Performanceanalyse.

[1]: https://www.postgresql.org/docs/current/runtime-config-query.html?utm_source=chatgpt.com "PostgreSQL: Documentation: 18: 19.7. Query Planning"
[2]: https://www.postgresql.org/docs/current/sql-prepare.html?utm_source=chatgpt.com "PostgreSQL: Documentation: 18: PREPARE"
[3]: https://www.postgresql.org/docs/15/view-pg-prepared-statements.html?utm_source=chatgpt.com "PostgreSQL: Documentation: 15: 54.15. pg_prepared_statements"
[4]: https://jdbc.postgresql.org/documentation/use/?utm_source=chatgpt.com "Initializing the Driver | pgJDBC"
[5]: https://jdbc.postgresql.org/documentation/server-prepare/?utm_source=chatgpt.com "PostgreSQL® Extensions to the JDBC API | pgJDBC"
