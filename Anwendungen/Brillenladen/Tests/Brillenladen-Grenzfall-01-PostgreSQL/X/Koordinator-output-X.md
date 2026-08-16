Die drei Analysen konvergieren sehr deutlich auf dieselbe Diagnose und denselben ersten Test. Entsprechend priorisiere ich Trennschärfe vor weiterer Ursachenbreite. 

### 1. FÜHRENDE HYPOTHESE

**Sessiongebundener Wechsel eines JDBC-Prepared-Statements von einem parameterabhängigen Custom Plan auf einen für seltene Werte ungünstigen Generic Plan.**

Das ist die von allen drei Analysen am stärksten getragene Erklärung. Dabei ist noch **nicht bewiesen**, dass tatsächlich ein Generic Plan verwendet wird; genau das soll der erste Test klären.   

### 2. BEGRÜNDUNG

Besonders charakteristisch ist die Kombination aus:

* **genau fünf schnellen Ausführungen, dann Einbruch ab der sechsten**,
* **Verlangsamung nur für bestimmte seltene Parameterwerte** bei stark schiefer Datenverteilung,
* **Bindung an dieselbe Session** und Reset nach Reconnect,
* **schneller Ausführung desselben Werts als Literal**.

Gemeinsam spricht das wesentlich stärker für eine parameter- und sessionabhängige Planänderung als für eine allgemeine Ressourcenursache. Insbesondere das Fünf→Sechs-Muster wird in allen Analysen als stärkstes Indiz bewertet.   

### 3. ALTERNATIVEN

Höchstens diese drei sollten vorerst offenbleiben:

1. **pgJDBC-`prepareThreshold` / Wechsel auf serverseitiges Prepare** als eigentlicher oder zusätzlicher Auslöser des Übergangs.
2. **Abweichende JDBC-Parametertypisierung bzw. implizite Casts** gegenüber der Literal-Abfrage.
3. **Anderer sessiongebundener Treiber-, Pool-, Framework- oder Statement-Cache-Effekt**, der nach wiederholter Nutzung die Ausführungsart verändert.

Unzureichende Planner-Statistiken wären eher eine mögliche Erklärung dafür, **warum** ein Generic Plan schlecht gewählt wird, nicht die stärkste unabhängige Erklärung für das gesamte Fünf→Sechs-Muster.   

### 4. KÜRZESTER PRÜFPFAD

Auf **derselben physischen Verbindung, nachdem der langsame Zustand bereits erreicht wurde**:

```sql
SET plan_cache_mode = force_custom_plan;
```

Dann exakt dieselbe parametrisierte Abfrage mit einem betroffenen seltenen Wert erneut ausführen.

**Wird sie sofort wieder schnell:** Die Custom-vs.-Generic-Plan-Hypothese ist sehr stark bestätigt.

**Bleibt sie langsam:** Die Generic-Plan-Erklärung ist klar geschwächt. Dann als nächsten kurzen A/B-Test `prepareThreshold=0` auf JDBC-Seite prüfen.

Optional unmittelbar zur Bestätigung in derselben Session:

```sql
SELECT name, generic_plans, custom_plans, statement
FROM pg_prepared_statements;
```

Ein detaillierter `EXPLAIN (ANALYZE, BUFFERS)`-Vergleich gehört erst **nach** diesem diskriminierenden Test zur Ursachenklärung.   

### 5. UNNÖTIGE SUCHBREITE

Vor diesem Prüfpfad zunächst verzichtbar sind eine breite CPU-/RAM-/I/O-Analyse, Hardwarediagnostik, vorschnelle Indexänderungen, umfangreiche Pool-Zerlegung sowie detaillierte Plan-, Statistik- oder Scan-/Join-Analysen.

Diese Untersuchungen können später relevant werden, liefern aber vor dem `force_custom_plan`-Test weniger diagnostische Trennschärfe.  

### 6. ENTSCHEIDUNG

**NEIN.**

Vor dem ersten entscheidenden Test ist keine weitere Analyse nötig. Das beobachtete Muster ist spezifisch genug, und `force_custom_plan` auf der bereits langsamen Session ist ein minimaler, unmittelbar unterscheidender Eingriff: Er kann die führende Hypothese direkt stark bestätigen oder deutlich schwächen. 
