
## 1. FÜHRENDE HYPOTHESE

Die Gruppe trägt am stärksten folgende Erklärung:

**Das parametrisierte Statement gerät innerhalb derselben PostgreSQL-Session in einen Prepared-Statement-/Plan-Cache-Zustand, in dem ein wertunabhängiger Generic Plan verwendet wird; dieser Plan ist für bestimmte seltene Parameterwerte bei stark schiefer Datenverteilung ungeeignet.**

Alle drei Analysen konvergieren auf diese Richtung. Gleichzeitig weisen sie darauf hin, dass die exakt beobachtete 5→6-Grenze auch durch den pgJDBC-`prepareThreshold` mitverursacht oder ausgelöst werden kann.   

## 2. BEGRÜNDUNG

Besonders charakteristisch für diese Erklärung ist die **Kombination** der Beobachtungen:

* **Ausführungen 1–5 schnell, ab 6 langsam:** passt auffällig zu einem zustandsabhängigen Prepare-/Planwechsel.
* **Nur bestimmte seltene Parameterwerte werden langsam:** spricht dafür, dass der konkrete Wert für die optimale Planung relevant ist.
* **Stark schiefe Datenverteilung:** macht einen wertunabhängigen Kompromissplan plausibel problematisch.
* **Derselbe Wert als SQL-Literal ist schnell:** dabei steht der konkrete Wert bereits bei der Planung fest; das passt zu einem Unterschied zwischen wertabhängiger und wertunabhängiger Planung.
* **Reconnect setzt das Verhalten zurück:** spricht stark für sessiongebundenen Zustand.
* **Keine beobachtete globale CPU-, RAM- oder I/O-Sättigung:** schwächt eine allgemeine Ressourcenüberlastung als Haupterklärung.

Entscheidend ist nicht eine einzelne Beobachtung, sondern dass **Schwellenwert, Parameterabhängigkeit und Session-Reset gemeinsam** erklärt werden.    

## 3. ALTERNATIVEN

Höchstens diese drei sollten ernsthaft offenbleiben:

1. **pgJDBC-`prepareThreshold` / Wechsel auf serverseitiges Prepare.**
   Die Fünfergrenze könnte primär vom Treiber stammen und muss deshalb vom eigentlichen Custom→Generic-Plan-Wechsel getrennt werden.

2. **Parameter-Typisierung oder Cast-Unterschied zwischen Prepared Statement und Literal.**
   Das könnte unterschiedliche Pläne bzw. Indexnutzung verursachen, erklärt den scharfen 5→6-Übergang aber schlechter.

3. **Anderer sessionlokaler Statement- oder Anwendungzustand.**
   Möglich, aber bislang ohne positiven Befund und daher deutlich schwächer als die führende Erklärung.   

## 4. KÜRZESTER PRÜFPFAD

Der minimale diagnostische Pfad ist:

**1. Auf derselben bereits betroffenen Connection `plan_cache_mode = force_custom_plan` setzen.**
Dann denselben seltenen Parameterwert erneut ausführen.

* **Wird die Query sofort wieder schnell:** führende Generic-Plan-Hypothese stark bestätigt.
* **Bleibt sie langsam:** Generic-vs.-Custom allein reicht als Erklärung nicht.

**2. Falls nötig unmittelbar danach `prepareThreshold` variieren bzw. serverseitiges Prepare testweise deaktivieren.**

* Verschwindet oder verschiebt sich damit der Breakpoint, liegt der relevante Übergang eher auf der JDBC-/Server-Prepare-Grenze.

**Optional parallel, wenn ohne Zusatzaufwand möglich:** in derselben Session `pg_prepared_statements` auf `generic_plans`, `custom_plans` und Parametertypen prüfen. Das liefert direkte Evidenz, ist aber für den ersten A/B-Test nicht zwingend erforderlich.   

## 5. UNNÖTIGE SUCHBREITE

Vor diesem Prüfpfad zunächst verzichtbar sind:

**breite Hardware-, CPU-, RAM- oder I/O-Analyse; allgemeine Indexoptimierung; umfassende Lock-/Lastanalyse; pauschales SQL-Tuning; allgemeine Cache-Untersuchungen.**

Diese Untersuchungen können später relevant werden, erklären aber die ungewöhnlich präzise Kombination aus **5→6-Schwelle, Parameterabhängigkeit und Reset per Reconnect** weniger direkt als der kurze Plan-/Prepare-Test.  

## 6. ENTSCHEIDUNG

**NEIN.**

Vor dem ersten entscheidenden Test ist keine weitere Analyse nötig. Die drei unabhängigen Analysen konvergieren bereits ausreichend stark auf dieselbe, mit einem kleinen reversiblen Eingriff prüfbare Hypothese. Zusätzliche theoretische Analyse würde den nächsten Schritt kaum verändern; der größte Informationsgewinn kommt jetzt aus dem **`force_custom_plan`-A/B-Test auf derselben betroffenen Connection**.    
