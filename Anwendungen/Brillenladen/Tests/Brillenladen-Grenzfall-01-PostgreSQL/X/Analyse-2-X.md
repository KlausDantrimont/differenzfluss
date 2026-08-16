
Die **wichtigste Erklärungsrichtung ist ein sessiongebundener Wechsel im Prepared-Statement-/Plan-Caching**, insbesondere von einem parameterabhängigen **Custom Plan** zu einem parameterunabhängigen **Generic Plan**. Das passt deutlich besser zu den vorgegebenen Beobachtungen als eine allgemeine Ressourcenursache. Der Testfall nennt ausdrücklich die starke Daten-Schieflage, den reproduzierbaren Umschlag nach fünf Ausführungen, das Zurücksetzen nach Verbindungsneuaufbau und die schnelle Literal-Abfrage.  Das Analyseziel legt zudem zu Recht den Fokus auf Sessions, Prepared Statements und Treibermechanismen. 

### Gegebene Beobachtungen

Gesichert ist nur: Die ersten fünf Ausführungen sind schnell, ab der sechsten sind bestimmte seltene Werte langsam; das Verhalten hängt an der Session; ein Verbindungsneustart setzt es zurück; die Werteverteilung ist stark ungleich; dieselbe Bedingung mit einem Literal ist schnell; globale CPU-/RAM-/I/O-Sättigung wurde nicht beobachtet. Daraus folgt **noch nicht**, dass tatsächlich ein Generic Plan verwendet wird.

### Hauptthese

PostgreSQL kann ein parametrisiertes Prepared Statement entweder mit einem wertabhängigen Custom Plan oder einem Generic Plan ausführen. Bei `plan_cache_mode=auto` werden für ein vorbereitetes Statement zunächst fünf Custom Plans verwendet; danach wird geprüft, ob sich ein Generic Plan lohnt. Ein Generic Plan kennt den konkreten Parameterwert nicht. Bei stark schiefer Datenverteilung kann deshalb ein Plan, der für den „durchschnittlichen“ Wert vernünftig erscheint, für einen seltenen Wert erheblich schlechter sein. Eine Literal-Abfrage kann dagegen beim Planen genau diesen konkreten Wert berücksichtigen. ([PostgreSQL][1])

Auch die Session-Grenze passt: Prepared Statements existieren nur innerhalb der jeweiligen Datenbank-Session und verschwinden mit deren Ende. ([PostgreSQL][1])

**Aber:** Die Zahl fünf darf hier nicht vorschnell PostgreSQL allein zugeschrieben werden. pgJDBC besitzt ebenfalls einen `prepareThreshold`, standardmäßig `5`, ab dem auf ein benanntes serverseitiges Prepared Statement gewechselt wird. Außerdem ist der Statement-Cache verbindungsbezogen. ([pgJDBC][2]) Deshalb lautet die Hauptthese präzise: **Beim wiederholten JDBC-Prepared-Statement findet ein sessiongebundener Prepare-/Plan-Übergang statt; erster Verdächtiger ist dabei ein für die seltenen Werte schlechter Generic Plan.**

### Kürzester sinnvoller Prüfpfad

Der stärkste einzelne A/B-Test ist auf **derselben physischen JDBC-Verbindung**:

```sql
SET plan_cache_mode = force_custom_plan;
```

Danach die gleiche Abfrage mit demselben seltenen Parameter deutlich mehr als sechs Mal ausführen. `plan_cache_mode` wird bei der Ausführung eines gecachten Plans berücksichtigt; `force_custom_plan` verhindert also gerade den verdächtigen Generic-Plan-Wechsel. ([PostgreSQL][3])

**Interpretation:** Verschwindet der Umschlag und bleiben auch spätere Ausführungen schnell, ist die Hauptthese praktisch bestätigt. Bleibt die sechste Ausführung langsam, ist ein PostgreSQL-Generic-Plan als Erklärung stark geschwächt.

Parallel bzw. unmittelbar danach lohnt in **genau derselben Session**:

```sql
SELECT name, statement, parameter_types,
       generic_plans, custom_plans
FROM pg_prepared_statements;
```

PostgreSQL weist dort pro vorbereitetem Statement aus, wie oft Generic bzw. Custom Plans gewählt wurden. Die Sicht ist sessionbezogen. ([PostgreSQL][4]) Bei einem explizit reproduzierten `PREPARE` lässt sich zusätzlich mit `EXPLAIN EXECUTE` prüfen: Ein Generic Plan enthält typischerweise `$1`, während beim Custom Plan der konkrete Parameterwert im Plan erscheint. ([PostgreSQL][1])

Wenn `force_custom_plan` **nicht** hilft, wäre mein nächster und ebenfalls sehr kurzer Test `prepareThreshold=0` in pgJDBC. Damit werden serverseitige Prepared Statements deaktiviert. Verschwindet erst damit der Effekt, liegt die Ursache weiterhin sehr wahrscheinlich im JDBC/serverseitigen-Prepare-Pfad, aber nicht primär in PostgreSQLs Generic-vs.-Custom-Auswahl. ([pgJDBC][2])

### Maximal drei ernsthafte Alternativen

1. **pgJDBC-`prepareThreshold` selbst:** Beim Erreichen des Schwellenwerts wechselt pgJDBC in den serverseitig vorbereiteten Modus; auch binäre Übertragung hängt daran. Das zeitliche Muster macht diesen Mechanismus unabhängig von der Generic-Plan-Hypothese prüfenswert. ([pgJDBC][2])
2. **Unterschiedliche Parametertypisierung JDBC vs. Literal:** Bind-Typ, implizite Casts oder Typinferenz könnten zu einem anderen Plan führen. Das wäre anhand von `parameter_types` und der tatsächlich verwendeten JDBC-Setter zu prüfen. Ohne weitere Befunde ist es aber schwächer, weil es den exakten Session-/Ausführungszähler schlechter erklärt.
3. **Sonstiger sessiongebundener Zustand** wie Einstellungen oder ein Pool-/Statement-Cache-Effekt. Das bleibt möglich, wäre wegen des sehr charakteristischen Fünf-/Sechs-Musters aber erst nach den beiden Tests oben zu untersuchen.

**Priorität daher:** nicht zuerst Indizes umbauen, Hardware untersuchen oder den Pool zerlegen. Zuerst `force_custom_plan` auf derselben physischen Verbindung testen und `pg_prepared_statements` ansehen. Damit lässt sich die wahrscheinlichste Ursache mit minimalem Eingriff sehr schnell bestätigen oder verwerfen.

[1]: https://www.postgresql.org/docs/current/sql-prepare.html?utm_source=chatgpt.com "PostgreSQL: Documentation: 18: PREPARE"
[2]: https://jdbc.postgresql.org/documentation/server-prepare/?utm_source=chatgpt.com "PostgreSQL® Extensions to the JDBC API | pgJDBC"
[3]: https://www.postgresql.org/docs/16/runtime-config-query.html?utm_source=chatgpt.com "PostgreSQL: Documentation: 16: 20.7. Query Planning"
[4]: https://www.postgresql.org/docs/15/view-pg-prepared-statements.html?utm_source=chatgpt.com "PostgreSQL: Documentation: 15: 54.15. pg_prepared_statements"
