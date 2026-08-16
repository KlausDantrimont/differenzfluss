
Die **wichtigste Erklärungsrichtung ist ein Wechsel von parameterabhängigen Custom Plans zu einem Generic Plan eines Prepared Statements**. Das auffällige „fünf schnell, ab sechs langsam“-Muster passt nahezu exakt zu PostgreSQLs Plan-Cache-Heuristik. ([PostgreSQL][1])

### 1. Gesicherte Beobachtungen

Aus dem Fall sind ausschließlich folgende Punkte gesichert: Die ersten fünf Ausführungen einer parametrisierten Abfrage auf einer neuen Verbindung sind schnell; ab der sechsten werden bestimmte seltene Parameterwerte reproduzierbar langsam; der Zustand bleibt innerhalb der Session bestehen und verschwindet mit dem Neuaufbau der Verbindung. Die Datenverteilung ist stark schief, während derselbe seltene Wert als SQL-Literal schnell ist. Eine globale CPU-, RAM- oder I/O-Sättigung wurde nicht beobachtet. 

Diagnostisch entscheidend sind damit **ZEIT** und **ZUSTAND**: Es gibt einen scharfen Übergang nach exakt fünf Ausführungen und einen Zustand, der an die Datenbank-Session gekoppelt erscheint. Genau diese beiden Merkmale sollen laut Aufgabenstellung primär erklärt werden. 

### 2. Führende Hypothese

Bei `plan_cache_mode = auto` verwendet PostgreSQL für ein parametrisiertes Prepared Statement zunächst **fünf Custom Plans**. Dabei kennt der Planner jeweils den konkreten Parameterwert. Danach erzeugt PostgreSQL einen **Generic Plan** und vergleicht dessen geschätzte Kosten mit dem Mittelwert der bisherigen Custom Plans. Wird der Generic Plan gewählt, kann er bei späteren Ausführungen wiederverwendet werden. ([PostgreSQL][1])

Das erklärt die Beobachtungen besonders gut:

* **1.–5. Ausführung:** Custom Plan kann die Selektivität des konkreten seltenen Werts berücksichtigen.
* **Ab 6.:** Ein Generic Plan kann gewählt werden, der den konkreten Parameterwert bei der Planung nicht kennt.
* **Stark ungleiche Verteilung:** Gerade dann kann der optimale Plan stark vom Wert abhängen; PostgreSQL weist ausdrücklich darauf hin, dass ein Generic Plan in solchen Fällen deutlich ineffizienter sein kann. ([PostgreSQL][1])
* **Literal schnell:** Das ist damit vereinbar, weil beim separat geplanten Literal der konkrete Wert sichtbar ist. Es ist aber **noch kein Beweis** für die Hypothese.
* **Reconnect setzt das Muster zurück:** Prepared Statements sind sessionbezogene Objekte; `pg_prepared_statements` zeigt entsprechend nur die Prepared Statements der aktuellen Session. ([PostgreSQL][2])

### 3. Alternativen

**Erste Alternative: pgJDBC `prepareThreshold`.** Der PostgreSQL-JDBC-Treiber hat standardmäßig ebenfalls einen Schwellenwert von fünf Ausführungen und wechselt dann bei demselben `PreparedStatement` zu einem benannten serverseitig vorbereiteten Statement. Das ist wegen „Java + fünf Ausführungen“ unbedingt mitzuprüfen. Es ist aber nicht dasselbe wie der PostgreSQL-Wechsel Custom→Generic; vielmehr kann es beeinflussen, ab wann der serverseitige Prepared-Statement-Zustand überhaupt entsteht. ([pgJDBC][3])

**Zweite Alternative: ein anderer JDBC-/Session-spezifischer Unterschied zwischen parametrisierter und Literal-Ausführung**, etwa im Zusammenhang mit Parametertypen oder dem gewählten Protokollpfad. Dafür gibt es im Fall jedoch keinen zusätzlichen Befund, und es erklärt die exakte PostgreSQL-Fünfergrenze schlechter.

**Dritte Alternative: allgemeine Cache-, Last- oder I/O-Effekte.** Sie sind nicht unmöglich, passen aber deutlich schlechter zum reproduzierbaren Reset allein durch Verbindungsneuaufbau und zur festen 5→6-Grenze. Aus den angegebenen Ressourcendaten lässt sich lediglich sagen, dass keine globale Sättigung beobachtet wurde; mehr sollte daraus nicht abgeleitet werden. 

### 4. Kürzester unterscheidender Test

Der kürzeste Test ist **auf derselben Verbindung**:

```sql
SET plan_cache_mode = force_custom_plan;
```

Dann exakt dieselbe parametrisierte Abfrage mit demselben seltenen Wert erneut ausführen. PostgreSQL dokumentiert `force_custom_plan` genau als Möglichkeit, den automatischen Generic-/Custom-Entscheid zu übersteuern. ([PostgreSQL][1])

**Wird die zuvor langsame Ausführung damit sofort wieder schnell, ist die Custom-vs.-Generic-Plan-Richtung sehr stark bestätigt.** Bleibt sie langsam, ist als nächster kurzer Schritt der JDBC-Übergang zu prüfen, insbesondere `prepareThreshold`.

Falls Zugriff aus **derselben Session** möglich ist, liefert zusätzlich

```sql
SELECT name, generic_plans, custom_plans
FROM pg_prepared_statements;
```

einen direkten Befund: PostgreSQL zählt dort, wie oft für jedes Prepared Statement Generic bzw. Custom Plans gewählt wurden. ([PostgreSQL][2])

**Priorität also:** nicht zuerst Indizes, Hardware oder allgemeine Datenbanklast untersuchen, sondern zuerst `force_custom_plan` gegen den reproduzierbaren sechsten Aufruf testen. Das trennt die auffälligste Hypothese mit minimalem Eingriff.

[1]: https://www.postgresql.org/docs/current/sql-prepare.html?utm_source=chatgpt.com "PostgreSQL: Documentation: 18: PREPARE"
[2]: https://www.postgresql.org/docs/15/view-pg-prepared-statements.html?utm_source=chatgpt.com "PostgreSQL: Documentation: 15: 54.15. pg_prepared_statements"
[3]: https://jdbc.postgresql.org/documentation/server-prepare/?utm_source=chatgpt.com "PostgreSQL® Extensions to the JDBC API | pgJDBC"
