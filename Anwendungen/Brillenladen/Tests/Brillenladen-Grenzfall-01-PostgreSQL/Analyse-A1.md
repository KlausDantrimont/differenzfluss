
Die **wahrscheinlich wichtigste Erklärungsrichtung ist ein Wechsel von parameterabhängigen Custom Plans auf einen Generic Plan bei einem Prepared Statement**. Das passt ungewöhnlich präzise zum beobachteten Muster: fünf schnelle Ausführungen, ab der sechsten reproduzierbar langsam für bestimmte seltene Werte, und Reset nach Aufbau einer neuen Session. 

### Gegebene Beobachtungen

Die Spalte ist stark ungleich verteilt; manche Parameterwerte treffen wenige, andere viele Zeilen.  Nach einer neuen Verbindung sind genau die ersten fünf Ausführungen schnell, ab der sechsten werden bestimmte seltene Werte langsam, und ein Reconnect setzt das Verhalten zurück. Eine SQL-Ausführung mit demselben Wert als Literal ist dagegen schnell. 

### Hauptthese

PostgreSQL kann für parametrisierte Prepared Statements zwischen **Custom Plan** und **Generic Plan** wählen. Bei `plan_cache_mode=auto` werden laut PostgreSQL-Dokumentation zunächst **fünf Custom Plans** erzeugt. Danach wird ein Generic Plan berechnet und dessen geschätzte Kosten mit dem Durchschnitt der Custom Plans verglichen; wird er für ausreichend günstig gehalten, können die folgenden Ausführungen den Generic Plan verwenden. ([PostgreSQL][1])

Genau bei stark schiefer Datenverteilung kann das problematisch sein: Ein Custom Plan kennt den konkreten Parameterwert und kann für einen seltenen Wert beispielsweise einen sehr selektiven Zugriffsweg wählen. Ein Generic Plan kennt diesen konkreten Wert bei der Planung nicht und muss einen parameterunabhängigen Kompromiss wählen. PostgreSQL weist ausdrücklich darauf hin, dass ein Generic Plan wesentlich ineffizienter sein kann, wenn der optimale Plan stark vom Parameterwert abhängt. ([PostgreSQL][1])

Dass die Literal-Abfrage schnell ist, stützt diese Richtung zusätzlich: Dort sieht der Planner den tatsächlichen Wert beim Planen. Das ist **noch kein Beweis**, aber es ist genau das erwartbare Indiz für parameterabhängige Planqualität.

Auch der Session-Reset passt: Prepared Statements bestehen nur für die Dauer einer Datenbanksession und verschwinden beim Verbindungsende. ([PostgreSQL][1])

### Kürzester sinnvoller Prüfpfad

Der stärkste Einzeltest ist auf **derselben problematischen Verbindung**:

```sql
SET plan_cache_mode = force_custom_plan;
```

Danach dieselbe parametrisierte Abfrage mit dem problematischen seltenen Wert erneut mehrfach ausführen.

**Wenn der Einbruch ab der sechsten Ausführung verschwindet**, ist die Hauptthese praktisch bestätigt. PostgreSQL dokumentiert `force_custom_plan` ausdrücklich als Möglichkeit, die automatische Generic-vs.-Custom-Entscheidung zu übersteuern. ([PostgreSQL][1])

Danach, erst zur Erklärung des *Warum*, die beiden Planvarianten vergleichen, idealerweise mit:

```sql
EXPLAIN (ANALYZE, BUFFERS)
...
```

einmal unter `force_custom_plan` und einmal unter `force_generic_plan`. Gesucht wird kein beliebiger Unterschied, sondern der konkrete Punkt, an dem der Generic Plan für den seltenen Wert viel mehr Arbeit verrichtet.

### Ernsthafte Alternativen

1. **pgJDBC-`prepareThreshold` als Auslöser bzw. zusätzliche Schicht.** pgJDBC hat standardmäßig einen `prepareThreshold` von 5 und wechselt nach Erreichen des Thresholds auf ein benanntes serverseitiges Prepared Statement. Das ist wegen derselben auffälligen Zahl unbedingt zu prüfen. ([pgJDBC][2]) Es kann die PostgreSQL-Plan-Cache-Problematik erst sichtbar machen, ist also eher ein möglicher Auslöser der Hauptthese als eine völlig unabhängige Ursache. Ein ergänzender A/B-Test mit `prepareThreshold=0` kann das eingrenzen; dadurch deaktiviert pgJDBC serverseitige Prepared Statements. ([pgJDBC][2])

2. **Unzureichende Planner-Statistiken für die schiefe Verteilung.** Das könnte erklären, warum PostgreSQL die Kosten eines Generic Plans falsch genug einschätzt, um ihn auszuwählen. Das wäre eher die Ursache der falschen Generic-Plan-Entscheidung als eine Erklärung für das Fünfer-Muster selbst.

3. **Abweichender JDBC-Parametertyp gegenüber der Literal-Abfrage.** pgJDBC weist darauf hin, dass Parametertypen den Plan beeinflussen und beispielsweise implizite Casts einen Indexzugriff verhindern können. ([pgJDBC][2]) Das passt aber deutlich schlechter zum exakten „ab der sechsten Ausführung“-Verhalten.

**Priorität:** Nicht zuerst CPU, I/O, Indexe oder eine breite Ursachenliste untersuchen. Der kürzeste Weg ist `force_custom_plan` → reproduzieren → danach Custom/Generic-Pläne vergleichen. Das folgt auch dem vorgegebenen Ziel, eine charakteristische PostgreSQL-Erklärung und einen möglichst kurzen Bestätigungs-/Widerlegungstest zu priorisieren. 

[1]: https://www.postgresql.org/docs/current/sql-prepare.html "PostgreSQL: Documentation: 18: PREPARE"
[2]: https://jdbc.postgresql.org/documentation/server-prepare/ "PostgreSQL® Extensions to the JDBC API | pgJDBC"
