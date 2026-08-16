
Die vorgegebenen Beobachtungen sprechen am stärksten für ein **session-lokales Prepared-Statement-/Plan-Cache-Problem, insbesondere den Wechsel von parameterabhängigen Custom Plans zu einem Generic Plan**. Das ist eine Hypothese, kein bereits gesicherter Befund. Der Fall und die gewünschte RELATION/INFORMATION-Perspektive stammen aus den beiden Vorgaben.  

### 1. Gesicherte Beobachtungen

* Die Laufzeit hängt von der **Ausführungsnummer innerhalb derselben Session** ab: 1–5 schnell, ab 6 für bestimmte seltene Werte langsam.
* Ein Verbindungsneuaufbau setzt dieses Verhalten zurück.
* Die Laufzeit hängt außerdem vom **Parameterwert** ab; die Datenverteilung der Spalte ist stark ungleich.
* Dieselbe logische Bedingung mit dem konkreten Wert als **SQL-Literal** ist schnell.
* Eine globale CPU-, RAM- oder I/O-Sättigung wurde nicht beobachtet.

Mehr ist nicht gesichert; insbesondere wurde noch **kein Planwechsel beobachtet**.

### 2. Führende Hypothese

PostgreSQL verwendet für Prepared Statements entweder einen **Custom Plan**, der den konkreten Parameterwert bei der Planung berücksichtigen kann, oder einen **Generic Plan**, der unabhängig vom jeweiligen Parameterwert wiederverwendet wird. Bei `plan_cache_mode=auto` werden für ein serverseitig vorbereitetes Statement zunächst fünf Custom Plans verwendet; danach wird geprüft, ob sich ein Generic Plan lohnt. ([PostgreSQL][1])

Damit ergibt sich als plausible Beziehung:

**seltenes Datum → Custom Plan mit Kenntnis dieses Werts → geeigneter Plan → schnell**

gegenüber möglicherweise

**seltenes Datum → Generic Plan ohne Kenntnis dieses Werts → für die schiefe Verteilung ungeeigneter Kompromissplan → langsam**.

Gerade bei ungleich verteilten Werten ist die fehlende Information über den konkreten Wert relevant. Beim `EXPLAIN EXECUTE` erkennt man einen Generic Plan typischerweise daran, dass `$1` im Plan stehen bleibt; beim Custom Plan erscheint der konkrete Wert. ([PostgreSQL][1])

Das erklärt auch, warum die Literal-Abfrage anders behandelt werden **könnte**: Bei `WHERE x = 123` kennt der Planner `123` unmittelbar. Bei einem wiederverwendbaren Generic Plan für `WHERE x = $1` darf der Plan nicht von einem bestimmten `$1` abhängen. ([PostgreSQL][1])

**Wichtige Einschränkung:** Aus der Zahl „6“ allein darf man noch nicht schließen, dass exakt PostgreSQLs Fünf-Ausführungen-Heuristik der Trigger ist. Falls die Anwendung pgJDBC verwendet, existiert zusätzlich `prepareThreshold`; dessen Default ist ebenfalls 5, und der Treiber wechselt damit zur Verwendung eines benannten serverseitigen Prepared Statements. Die konkrete Zählung hängt deshalb davon ab, wie Treiber und Anwendung die Statements vorbereiten und wiederverwenden. ([pgJDBC][2])

### 3. Maximal drei Alternativen

1. **Treiberseitiger Prepare-Übergang statt bzw. vor dem eigentlichen Generic-Plan-Wechsel.** Bei pgJDBC wäre `prepareThreshold` die naheliegende Stelle. Das gehört zur selben allgemeinen Erklärungsrichtung „Darstellungs-/Prepare-Zustand der Query“, aber der konkrete Trigger wäre ein anderer. ([pgJDBC][3])

2. **Planner-Statistiken bilden die schiefe Verteilung nicht ausreichend ab.** Das könnte dazu führen, dass PostgreSQL die Kosten eines Generic Plans falsch einschätzt und ihn auswählt, obwohl er für den seltenen Wert real teuer ist. Das ist derzeit lediglich eine mögliche Ursache dafür, *warum* ein Generic Plan schlecht wäre, nicht ein gesicherter Befund. ([PostgreSQL][1])

3. **Parameterdatentyp bzw. Cast unterscheidet sich von der Literalvariante.** Bei Prepared Statements gehören konkrete `parameter_types` zum serverseitigen Statement; eine Typ-/Cast-Differenz könnte ebenfalls Planung oder Indexnutzung verändern. Ob das hier der Fall ist, ist völlig offen. `pg_prepared_statements` zeigt die Parametertypen an. ([PostgreSQL][4])

### 4. Kürzester unterscheidender Test

Auf **derselben betroffenen Verbindung**, nachdem der langsame Zustand erreicht ist:

```sql
SHOW plan_cache_mode;

SELECT name, parameter_types, generic_plans, custom_plans
FROM pg_prepared_statements;
```

Die View ist session-lokal und zählt für jedes serverseitig vorbereitete Statement, wie oft Generic bzw. Custom Plans gewählt wurden. ([PostgreSQL][4])

Dann als entscheidenden A/B-Test auf derselben Verbindung:

```sql
SET plan_cache_mode = force_custom_plan;
```

und **denselben seltenen Parameterwert nochmals ausführen**.

Wenn die Abfrage dadurch unmittelbar wieder schnell wird und/oder der Plan gegenüber `auto` wechselt, ist die führende Erklärung sehr stark bestätigt. `force_custom_plan` ist genau dafür vorgesehen, die automatische Generic-/Custom-Entscheidung zu übersteuern. ([PostgreSQL][1])

**Priorität daher:** nicht zuerst Hardware, Locks oder allgemeines SQL-Tuning untersuchen, sondern zunächst feststellen: **Wird ab dem fraglichen Punkt ein serverseitiges Prepared Statement bzw. ein Generic Plan verwendet, und verschwindet der Effekt mit `force_custom_plan`?** Das trennt die führende Hypothese mit sehr wenig Aufwand von den meisten anderen Erklärungen.

[1]: https://www.postgresql.org/docs/current/sql-prepare.html?utm_source=chatgpt.com "PostgreSQL: Documentation: 18: PREPARE"
[2]: https://jdbc.postgresql.org/documentation/use/?utm_source=chatgpt.com "Initializing the Driver | pgJDBC"
[3]: https://jdbc.postgresql.org/documentation/server-prepare/?utm_source=chatgpt.com "PostgreSQL® Extensions to the JDBC API | pgJDBC"
[4]: https://www.postgresql.org/docs/15/view-pg-prepared-statements.html?utm_source=chatgpt.com "PostgreSQL: Documentation: 15: 54.15. pg_prepared_statements"
