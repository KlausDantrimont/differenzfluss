
Die Fallbeschreibung und die Diagnosevorgaben ergeben zusammen ein sehr charakteristisches Muster.  

### Gegebene Beobachtungen

Gesichert sind nur: stark schiefe Datenverteilung, fünf schnelle Ausführungen nach neuem Verbindungsaufbau, ab der sechsten reproduzierbare Verlangsamung für bestimmte seltene Werte, Fortbestehen innerhalb derselben Session, Reset durch neue Verbindung und eine schnelle Literal-Abfrage. Eine globale Ressourcenknappheit wurde nicht beobachtet. Daraus folgt **noch nicht**, welcher konkrete Plan verwendet wird oder ob ein Index benutzt bzw. nicht benutzt wird.

### 1. Führende Hypothese

**Wechsel von einem parameterwertspezifischen Custom Plan zu einem Generic Plan für ein Prepared Statement.**

PostgreSQL macht bei `plan_cache_mode=auto` für ein parametrisiertes Prepared Statement zunächst **fünf Custom Plans**. Danach wird ein Generic Plan erzeugt und kostenmäßig mit den bisherigen Custom Plans verglichen. Wird der Generic Plan gewählt, kann er für weitere Ausführungen wiederverwendet werden.

Das passt ungewöhnlich genau zum Übergang **„erste fünf gut, ab sechs schlecht“**.

Bei stark ungleich verteilten Werten ist genau das ein Problemfall: Ein Custom Plan kennt den konkreten Parameterwert; ein Generic Plan nicht. PostgreSQL weist selbst darauf hin, dass ein Generic Plan ineffizient sein kann, wenn der optimale Plan stark vom Parameterwert abhängt.

### 2. Warum die Beobachtungen dafür sprechen

**Fünf → sechs:** Das ist der stärkste Befund. Die dokumentierte PostgreSQL-Heuristik arbeitet exakt mit fünf anfänglichen Custom-Plan-Ausführungen.

**Nur bestimmte seltene Werte werden langsam:** Das passt zu Parameter-Sensitivität. Bei schiefer Verteilung kann derselbe parameterunabhängige Plan für häufige Werte akzeptabel, für seltene Werte aber sehr ungünstig sein.

**Neue Session setzt das Verhalten zurück:** Prepared Statements und deren Planhistorie sind sessionbezogen; `pg_prepared_statements` zeigt die Prepared Statements der aktuellen Session einschließlich der Anzahl von Generic- und Custom-Plänen.

**Dasselbe Literal ist schnell:** Das unterstützt die Richtung, weil die Planung dann den konkreten Wert kennt. Es beweist sie allein aber nicht.

**Keine globale CPU-/RAM-/I/O-Sättigung:** Das beweist nichts über den Plan, macht eine allgemeine Ressourcenüberlastung aber als Erklärung des exakt session- und ausführungszahlabhängigen Musters weniger attraktiv.

### 3. Alternativen

1. **pgJDBC-Server-Prepare-Schwelle.** Das ist eng mit der Haupthypothese verwandt und muss wegen „Java“ mitgeprüft werden. pgJDBC hat standardmäßig `prepareThreshold=5` und wechselt nach wiederholten Ausführungen zu serverseitig vorbereiteten Statements.  Der dokumentierte aktuelle Treiber beginnt bei Default-Konfiguration allerdings bereits beim fünften entsprechenden Aufruf mit Server Prepare; deshalb sollte man aus dem beobachteten „ab sechs“ nicht ohne Prüfung behaupten, dass exakt der JDBC-Default die Ursache sei.

2. **Andere planändernde Session-/Middleware-Effekte.** Denkbar wäre ein Pool, Framework oder eine abweichende JDBC-Konfiguration, die nach wiederholter Nutzung die Ausführungsart verändert. Dafür gibt es im Fall aber keinen zusätzlichen Befund.

3. **Parameter-Typisierung/Casts bzw. eine andere Planabweichung zwischen gebundener und Literal-Abfrage.** Prinzipiell möglich, erklärt allein aber den scharfen Übergang nach genau fünf Ausführungen wesentlich schlechter.

### 4. Kürzester unterscheidender Test

Auf **derselben Verbindung, auf der der langsame Zustand bereits erreicht ist**, für einen betroffenen seltenen Wert:

```sql
SET plan_cache_mode = force_custom_plan;
```

Danach exakt dieselbe parametrisierte Abfrage erneut ausführen.

**Wird sie sofort wieder schnell**, ist die Generic-vs-Custom-Plan-Richtung sehr stark bestätigt. `force_custom_plan` ist genau für diesen Vergleich vorgesehen.

Als direkte Gegenprobe kann man in derselben Session ansehen:

```sql
SELECT name, generic_plans, custom_plans, statement
FROM pg_prepared_statements;
```

Die View zählt ausdrücklich, wie oft Generic bzw. Custom Plans für jedes Prepared Statement gewählt wurden.

Erst **danach** würde ich die konkreten Pläne mit `EXPLAIN (ANALYZE, BUFFERS)` vergleichen und nach der Ursache des Fehlentscheids suchen — etwa Statistiken oder unterschiedliche Scan-/Join-Strategien. Vor diesem Test wäre es voreilig, solche Befunde zu behaupten.

**Kurzfassung:** Zuerst `force_custom_plan` auf der bereits „langsamen“ Session testen. Wenn der seltene Wert damit wieder schnell wird, hat man mit einem einzigen Eingriff die wichtigste Hypothese von den meisten Alternativen getrennt.
