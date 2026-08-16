## Gesamturteil

Die drei Analysen konvergieren stark auf dieselbe Kernlage: **Es gibt noch keine belastbare Root Cause; der Neustart ist der stärkste Hinweis, aber diagnostisch unspezifisch.** Der Testfall erlaubt ausdrücklich keine weiteren Tatsachenannahmen. 

Der größte zusätzliche Erkenntnisgewinn kommt von **B3**. B1 strukturiert den Problemraum entlang **Zeit/Zustand**, B2 entlang **Relation/Beobachtbarkeit**, und B3 macht daraus **kausal unterscheidende Interventionen**. Das ist ein qualitativer Fortschritt, nicht nur eine weitere Hypothesenliste.

## 1. Substanzielle Punkte, die mehrfach vorkommen

**Verdeckter, durch Neustart beeinflusster Zustand.** Alle drei Analysen halten eine Zustandsklasse für plausibel, die durch einen Neustart verändert oder zurückgesetzt wird, warnen aber davor, daraus vorschnell Cache, Pool, Leak, Lock o. Ä. als Ursache abzuleiten. B1 formuliert das explizit als prozesslokalen Zustand, B2 als langlebigen Neustart-beeinflussten Zustand und B3 als eine von mehreren konkurrierenden Klassen.   

**Uptime versus akkumulierte Nutzung.** B1 trennt besonders sauber „Zeit seit Neustart“ von kumulierter Request-/Operationszahl. B2 fragt fast dasselbe über Prozesslebensdauer, Requests, Sessions und Zustandsübergänge; B3 nimmt Prozessalter erneut als Trennvariable auf.   

**Langsame gegen normale Requests vergleichen.** Das ist in allen drei Analysen zentral: per Trace, Pfad, Instanz oder request-spezifischen Merkmalen herausfinden, wo sich die langsamen Requests unterscheiden.   

**Aggregierte Metriken können den relevanten Zustand verdecken.** Keine der Analysen interpretiert unauffällige CPU-/Speicher-/DB-Metriken als Ausschluss dieser Bereiche. B2 arbeitet diesen Punkt am stärksten über Granularität, Sampling und fehlende Dimensionen aus.   

**Externe Abhängigkeit bzw. durch Neustart erneuerte Beziehung.** B1s „extern ausgelöster, intern persistierender Zustand“, B2s externe Abhängigkeit und B3s externer Zustand sind Varianten derselben größeren Klasse.   

## 2. Tatsächlich eigenständige Beiträge

| Analyse | Eigenständiger Beitrag                                                                                                                                                                                              | Wert        |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **B1**  | Trennt **graduelle Akkumulation** von einem **episodischen Zustandsübergang**. Eine Störung kann also abrupt in einen persistenten schlechten Zustand wechseln, ohne dass vorher kontinuierlich etwas „vollläuft“.  | Hoch        |
| **B1**  | Unterscheidet **Zeit** von **Nutzung** als Akkumulationsachse und fordert mehrere Neustartzyklen auf gemeinsamer Zeitachse.                                                                                         | Hoch        |
| **B2**  | Macht **Request-Dimensionen und Instanzlokalität** zu primären Vergleichsachsen: gleiche Zeit/gleicher Request-Typ, aber andere Instanz; oder schnelle und langsame Requests auf derselben Instanz.                 | Hoch        |
| **B2**  | Trennt **aktive Ausführung von Wartezeit**. Das ist stärker als bloß „mehr Metriken sammeln“, weil es lokalisiert, welche Art von Zeit überhaupt zusätzlich entsteht.                                               | Hoch        |
| **B2**  | Expliziert Beobachtbarkeitsfehler: Aggregation, Sampling, fehlende Kardinalität und lokale Engpässe trotz unauffälliger Service-Metriken.                                                                           | Mittel–hoch |
| **B3**  | Führt erstmals ein echtes **Gegenfaktual** ein: Restart vs. No Restart. Damit wird geprüft, ob der Neustart überhaupt kausal für die Erholung ist.                                                                  | Sehr hoch   |
| **B3**  | Zerlegt den Neustart in **Traffic-Reset versus Prozess-Reset** und anschließend in **Teil-Resets einzelner Zustände**.                                                                                              | Sehr hoch   |
| **B3**  | Formuliert explizite Anforderungen an einen Kausalschluss: zeitliche Ordnung, Kovariation, Intervention, Gegenfaktual, Trennung gekoppelter Interventionen und Replikation.                                         | Sehr hoch   |

Damit erzeugt **B3 die meisten zusätzlichen prüfbaren Untersuchungsrichtungen**. B1 und B2 erweitern hauptsächlich den Suchraum; B3 verändert das **Versuchsdesign**.

## 3. Redundanzen

Die größte Redundanz liegt zwischen **B1 und B2**. Beide behandeln verborgenen Zustand, Uptime/Nutzung, Pool-/Queue-/Connection-artige Zustandsklassen, Traces langsamer Requests und den Vorher-/Nachher-Vergleich um einen Restart.  

Auch B3 wiederholt mehrere Hypothesenklassen aus B1/B2 – lokaler Zustand, externe Abhängigkeit, Request-Klasse und verdeckter Ressourcenengpass. Sein Mehrwert liegt daher **nicht** primär in H1–H5, sondern in den Trennexperimenten A–F. 

Besonders redundant sind somit:

* „Restart setzt irgendeinen relevanten Zustand zurück.“
* „Prozessalter oder kumulierte Nutzung könnten relevant sein.“
* „Slow vs. fast Requests sollten verglichen werden.“
* „Aggregierte Service-Metriken könnten lokale Probleme verbergen.“
* „Die eigentliche Verzögerung könnte in einer externen Abhängigkeit liegen.“

Diese Wiederholung erhöht die Konfidenz, erweitert aber den Hypothesenraum kaum.

## 4. Unbelegte Tatsachen oder zu konkrete Ursachen

Hier sind alle drei insgesamt diszipliniert. Die Fallbeschreibung sagt ausdrücklich, dass keine zusätzlichen Befunde existieren und nichts erfunden werden darf. 

**B1** hält die Grenze am saubersten: selbst bei Cache, Pool, Verbindung, Queue usw. wird ausdrücklich gesagt, dass keiner dieser Zustände als relevant belegt ist. 

Bei **B2** ist eine Formulierung etwas zu stark: Aus dem wirksamen Restart sei „eine Beziehung zwischen dem Zustand dieses Dienstes und dem Symptom gesichert“.  Das ist enger formuliert, als die Evidenz erlaubt. Der Restart könnte beispielsweise eine **Beziehung des Dienstes zu externen Ressourcen oder seine Traffic-Zuordnung** verändern; genau diese Möglichkeit erkennt B2 später selbst.  Präziser wäre: *Eine durch den Neustart veränderte Bedingung steht reproduzierbar mit der Erholung in Beziehung.*

Bei **B3** ist die Aussage, ein Neustart verändere gleichzeitig „Prozesszustand, Verbindungen, lokale Queues, Caches, Zuordnung von Requests …“, etwas zu konkret.  Nicht jedes nicht beschriebene System muss lokale Queues oder Caches besitzen. Als **mögliche** gekoppelte Effekte sind diese Beispiele legitim; als Tatsachen sollten sie konditional formuliert werden.

B3s Bewertung von H6 als „weniger naheliegend“ ist ebenfalls ein Prior, kein Ergebnis eines Gegenfaktualtests.  Dass der Restart zuverlässig gefolgt von Erholung ist, macht H6 intuitiv schwächer, schließt es aber gerade nicht aus.

## 5. Explizit erkannte Blindstellen

**B1** erkennt die breiteste inhaltliche Blindstellenliste: Request-Typen, konkrete Daten/Eingaben, Topologie/Routing, Instanzunterschiede, Netzwerk, externe Dienste und fehlerhafte Instrumentierung. Besonders wichtig ist die Einsicht, dass ein Restart geringe diagnostische Spezifität besitzt. 

**B2** erkennt vor allem Erkenntnis- und Messblindstellen: Korrelation ist keine Kausalität, Implementierungs- oder Protokolldetails könnten fehlen, Aggregation/Sampling kann Probleme unsichtbar machen, und ohne Telemetrie einer echten Störung lassen sich die Hypothesen nicht priorisieren. 

**B3** erkennt Blindstellen des eigenen experimentellen Ansatzes: Mehrfachursachen, unbeobachtbare Variablen, Nebeneffekte der Intervention selbst, Seltenheit der Ereignisse und unvollkommene Gegenfaktuale in verteilten Systemen. 

Diese Blindstellen sind überwiegend **komplementär**, nicht redundant.

## 6. Welche Vorschläge ermöglichen wirklich unterscheidende Tests?

Die stärksten sind:

**1. Restart vs. No Restart — B3.**
Trennt „Restart ist tatsächlich kausal für die Erholung“ von „die Episode wäre ohnehin beendet worden“. Das ist die wichtigste bisher fehlende Kontrollbedingung. 

**2. Traffic-Drain vs. Prozess-Restart — B3.**
Trennt Routing/Traffic-/Request-Zuordnung von einem echten Prozessreset. 

**3. Gezielte Teil-Resets — B3.**
Der Restart wird in kleinere Interventionen zerlegt. Nur so kann aus „Restart hilft“ schrittweise „Reset von X hilft, Reset von Y nicht“ werden. 

**4. Gleicher bzw. äquivalenter Request auf frischer und betroffener Instanz — B3/B2.**
Trennt Request-Eigenschaft von Instanz-/Zustandseigenschaft. B2 nähert sich diesem Design bereits über gematchte Vergleiche; B3 formuliert es als stärker kontrolliertes Experiment. 

**5. Prozessalter gegen kumulierte Nutzung — B1.**
Das ist ein guter discriminating test zwischen zeitgetriebener und nutzungsgetriebener Akkumulation. 

**6. Episodischer Zustandswechsel gegen graduelle Verschlechterung — B1.**
Hochauflösende Zeitreihen können zwei fundamental andere Mechanismen auseinanderhalten. 

Dagegen sind Forderungen wie „mehr Metriken“, „Pools beobachten“ oder „Traces sammeln“ **für sich allein noch keine Trennexperimente**. Sie werden erst stark, wenn vorher definiert ist, welche zwei Hypothesen ein bestimmtes Ergebnis gegeneinander verschiebt.

## 7. Ist ein weiterer Analyse-Agent noch lohnend?

**Nein, derzeit nicht als weiterer allgemeiner Analyse-Agent.**

Der Engpass ist inzwischen nicht mehr ein Mangel an plausiblen Hypothesen. Die drei Analysen decken bereits drei weitgehend komplementäre Ebenen ab:

**Zeit/Zustand → Relation/Beobachtbarkeit → Kausale Intervention.**

Ein vierter breit angelegter Agent würde mit hoher Wahrscheinlichkeit weitere Varianten von Pool, Cache, Netzwerk, Routing, Lock, Queue, Retry, Request-Klasse oder Telemetrie erzeugen. Das erhöht die Zahl denkbarer Ursachen, aber kaum die Fähigkeit, sie zu unterscheiden.

Der nächste marginal wertvolle Input ist deshalb **Evidenz aus einem gezielten Störungsversuch**, nicht noch eine Hypothesenliste.

Falls später doch ein weiterer Agent eingesetzt wird, sollte das erst **nach** neuen Messdaten geschehen und eng auf eine dann offene Dimension beschränkt sein, etwa Messvalidität oder konkrete Protokoll-/Topologieanalyse. Vorher ist der erwartete Informationsgewinn gering.

---

# Verdichtetes Endergebnis

### Gemeinsame Befunde

Es gibt keine belegte technische Root Cause. Der Restart ist reproduzierbar mit Erholung verbunden, aber unspezifisch. Ein verborgener Zustand, Request-spezifische Unterschiede, lokale statt globale Effekte und fehlende Observability bleiben mit den Daten vereinbar.

### Einzigartige Beiträge pro Analyse

**B1:** Zeit vs. Nutzung, graduelle vs. episodische Zustandsänderung, zeitliche Episodenstruktur.
**B2:** Request-/Instanzrelationen, aktive Zeit vs. Wartezeit, Kardinalität/Aggregationsprobleme.
**B3:** Gegenfaktuale, gekoppelte Interventionen zerlegen, Restart/No-Restart, Traffic-/Prozessreset und Teil-Resets.

### Redundanzen

Hidden state nach Restart, Uptime/Nutzung, Slow-vs.-Fast-Tracing, externe Abhängigkeiten und feinere Pool-/Queue-/Connection-Telemetrie erscheinen mehrfach. B1 und B2 überlappen dabei am stärksten.

### Offene Evidenz

Es fehlen vor allem Incident-nahe per-Request-Daten, Instanz-/Prozesszuordnung, genaue Zeitanteile des langsamen Pfads, Zustand unmittelbar vor einer Intervention und eine Kontrollbedingung, die zeigt, was **ohne** Restart geschieht.

### Empfohlener nächster Untersuchungsschritt

Bei der nächsten sicher beobachtbaren Störung zunächst **vor dem Restart einen kurzen Trace-/Zustandssnapshot sichern** und – sofern die Architektur und Betriebsrisiken es erlauben – einen **Restart-vs.-No-Restart-Vergleich** zwischen möglichst vergleichbaren Einheiten durchführen. Erst danach sollte als nächster Split **Traffic-Drain vs. echter Prozessreset** folgen. Das kombiniert die benötigte Evidenz aus B1/B2 mit dem stärksten Trennexperiment aus B3.  

### Stop/Weiter-Entscheidung

**STOP für weitere allgemeine Analyse-Agenten; WEITER mit empirischer Untersuchung.** Neue Analyse ohne neue Evidenz hat inzwischen deutlich geringeren erwarteten Informationsgewinn als ein sauberer unterscheidender Test.
