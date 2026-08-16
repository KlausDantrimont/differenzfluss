Die drei Analysen liegen in ihrer Grunddiagnose sehr nah beieinander. Der Testfall selbst gibt nur vier belastbare Signale her: sporadische starke Latenz einzelner Requests, temporäre Heilung durch Dienstneustart, keine eindeutige Auffälligkeit in CPU/RAM/DB und keine dauerhafte Wirkung bisheriger Optimierungen; ausdrücklich dürfen keine weiteren Tatsachen ergänzt werden. 

## 1. Gemeinsame Befunde

Substanziell mehrfach vorhanden sind vor allem diese Punkte:

| Gemeinsamer Punkt                                            | A1 | A2 | A3 | Bewertung                                                     |
| ------------------------------------------------------------ | -: | -: | -: | ------------------------------------------------------------- |
| Neustart deutet auf zustandsabhängigen Mechanismus           |  ✓ |  ✓ |  ✓ | Stark, aber nicht auf **prozessinternen** Zustand beschränken |
| CPU/RAM/DB unauffällig schließt Ressourcenprobleme nicht aus |  ✓ |  ✓ |  ✓ | Wichtig und korrekt                                           |
| Requests könnten **warten statt rechnen**                    |  ✓ |  ✓ |  ✓ | Zentrale gemeinsame Arbeitshypothese                          |
| Pools / Worker / Connections als Kandidaten                  |  ✓ |  ✓ |  ✓ | Stark redundant                                               |
| Queueing / Backpressure                                      |  ✓ |  ✓ |  ✓ | Stark redundant                                               |
| Locks / blockierte Threads                                   |  ✓ |  ✓ |  ✓ | Stark redundant                                               |
| langlebige Downstream-Verbindungen / Clients                 |  ✓ |  ✓ |  ✓ | Stark redundant                                               |
| GC-/Runtime-Effekte                                          |  ✓ |  ✓ |  ✓ | Stark redundant und derzeit schwächer belegt                  |
| langsamen Request zeitlich zerlegen / Distributed Tracing    |  ✓ |  ✓ |  ✓ | Höchster gemeinsamer Erkenntniswert                           |
| Diagnosezustand **vor** Neustart sichern                     |  ✓ |  ✓ |  ✓ | Sehr wichtig                                                  |
| gesunde gegen betroffene Instanz vergleichen                 |  ✓ |  ✓ |  ✓ | A2/A3 stärker ausgearbeitet                                   |
| Neustart in kleinere Reset-Experimente zerlegen              |  ✓ |  ✓ |  ✓ | A3 macht daraus die schärfsten Gegenproben                    |

Der Kern aller drei Analysen ist damit praktisch derselbe: Nicht weiter breit optimieren, sondern feststellen, **wo die zusätzliche Request-Zeit verbracht wird und welcher Zustand mit dem Neustart verändert wird**. A1 formuliert dies über Slow-Request-Tracing, Diagnose-Snapshots und selektive Resets.  A2 macht dieselbe Leitfrage zum Mittelpunkt und kombiniert sie mit Vorher-/Nachher-Zuständen.   A3 verfolgt dieselbe Grundlinie. 

## 2. Einzigartige Beiträge pro Analyse

### Analyse A1

A1 hat nur wenige wirklich eigenständige Beiträge. Am nützlichsten ist die explizite Suche nach **zeitlich driftenden Größen seit dem letzten Neustart** — nicht nur Incident-Snapshots, sondern Größen, die mit Prozesslaufzeit oder Zahl verarbeiteter Requests schlechter werden. 

Das ist tatsächlich etwas anderes als bloß „Pool messen“: Es prüft eine Akkumulationshypothese longitudinal.

Ebenfalls brauchbar ist der Hinweis auf die **Metrikauflösung**: kurze Runtime-Stalls können für einzelne Requests gravierend sein und in grob aggregierten CPU-/RAM-Metriken verschwinden.  Das ist eine echte Observability-Blindstelle.

Ansonsten besteht A1 überwiegend aus demselben Hypothesencluster wie A2 und A3.

### Analyse A2

A2 liefert die stärkste **systematische Klassifikation des Fehlerbilds**. Besonders wertvoll ist die Unterscheidung:

* nur eine Instanz betroffen,
* alle Instanzen gleichzeitig,
* nur bestimmte Requests,
* praktisch alle Requests einer Instanz.

Daraus ergeben sich jeweils unterschiedliche Hypothesenräume.  Das ist mehr als eine Umformulierung vorhandener Kandidaten; es ist eine diagnostische Partitionierung.

Eigenständig nützlich sind außerdem Queue-spezifische Messgrößen wie **Queue Age** und insbesondere das Verhältnis von Arrival Rate zu Completion Rate.  Das macht die Backpressure-Hypothese konkreter prüfbar.

Die explizite Phasenzerlegung einer Downstream-Anfrage in etwa `Pool wait → DNS → connect → TLS → ...` liefert ebenfalls eine sauberere Lokalisierung als nur „Downstream-Latenz messen“. 

### Analyse A3

A3 erzeugt den größten zusätzlichen Erkenntnisgewinn.

Der wichtigste eigenständige Punkt lautet: **Ein erfolgreicher Neustart ist diagnostisch unspezifisch.** Er kann nicht nur internen Prozesszustand zurücksetzen, sondern beispielsweise Verbindungen, Discovery-Zustand und möglicherweise auch das Traffic-Routing verändern.  

Damit korrigiert A3 eine leichte Tendenz von A1 und A2, den Neustarteffekt zu schnell als Hinweis auf prozesslokalen Zustand zu interpretieren.

Zwei weitere echte Erweiterungen sind:

**Request-/Datenabhängigkeit:** Nicht nur Codepfad oder Downstream, sondern beispielsweise Kunde, Schlüssel oder Payload als gemeinsames Merkmal langsamer Requests. 

**Retry-/Timeout-Verstärkung:** Kleine primäre Verzögerungen können durch Retries oder gestaffelte Timeouts zu sehr großer End-to-End-Latenz werden.  Das ist in A1/A2 nicht als eigener Mechanismus ausgearbeitet.

Noch wichtiger sind die konkreten Gegenexperimente: Instanz nur aus dem Load Balancer nehmen, Traffic ohne Neustart verschieben, nur Connections/Pools erneuern, gleiche Instanz bzw. Host vergleichen.  Diese Tests unterscheiden **Prozesszustand, Kommunikationszustand, Routing und äußere Abhängigkeit** voneinander und sind deshalb diagnostisch besonders wertvoll.

## 3. Redundanzen

Die größte Redundanz liegt nicht in der Wortwahl, sondern in der Hypothesenstruktur.

„Pool-Erschöpfung“, „begrenzte Ressourcen“, „Worker-Starvation“, „Connection-Pool-Probleme“ und teilweise „interne Queue“ sind eng verwandte Varianten derselben übergeordneten These: Ein Request wartet auf eine knappe oder blockierte Ressource.

Ähnlich überlappen „Lock Contention“, „blockierte Threads“ und Teile der Queue-/Worker-Hypothese funktional: Sie sollen alle erklären, weshalb Latenz steigt, obwohl CPU niedrig bleiben kann.

Auch „prozesslokaler Zustand“, „Cache degeneriert“, „langlebiger Clientzustand“ und „Runtime-Zustand“ sind auf der obersten Ebene nur verschiedene Untertypen der Aussage „etwas Zustandsbehaftetes wird durch Restart zurückgesetzt“.

A2 wirkt wegen seiner größeren Länge hypothesenreicher, enthält aber nur begrenzt mehr **orthogonale** Hypothesen. Viele Abschnitte zerlegen vorhandene Klassen feiner.

## 4. Wo zu konkrete oder unbelegte Ursachen angenommen werden

Keine der drei Analysen erfindet massiv Tatsachen; alle kennzeichnen ihre Kandidaten überwiegend als Hypothesen. Es gibt aber unterschiedliche Grade der Überinterpretation.

**A1** ist etwas zu schnell prozesszentriert. Gleich zu Beginn wird aus dem Neustarteffekt abgeleitet, zuerst nach einem Zustand zu suchen, der „innerhalb der laufenden Instanz entsteht oder sich dort akkumuliert“.  Als Priorisierung ist das vertretbar, aber nicht die einzig naheliegende Interpretation. A3 zeigt den Gegenpunkt: Ein Restart kann auch Routing, Connections oder anderen Kontext verändern. Das ist die wichtigste Korrektur an A1.

Die Formulierung in A1, ein Neustart setze „genau solche Zustände zurück“, ist für Pools/FDs/Caches generell plausibel, aber für den konkreten Fall nicht belegt. 

**A2** formuliert vorsichtiger, priorisiert Pools/Queues/Connections/Locks aber dennoch ziemlich stark.  Diese Reihenfolge ist heuristisch vernünftig, aus den fünf Fallbeobachtungen allein jedoch nicht empirisch ableitbar. Insbesondere gibt es noch keine Evidenz, die Pool-Erschöpfung gegenüber Routing, requestabhängigem Verhalten oder Retry-Verstärkung klar bevorzugt.

Außerdem ist die Aussage, lokale Performanceoptimierung adressiere „wahrscheinlich nicht den eigentlichen Mechanismus“, etwas stärker als nötig.  Die erfolglosen Optimierungen sagen nur dann viel aus, wenn bekannt wäre, welchen Mechanismus sie tatsächlich verändert haben. A3 erkennt genau diese Einschränkung ausdrücklich. 

**A3** ist bezüglich Tatsachenbehauptungen am saubersten. Zusätzliche Mechanismen werden ausdrücklich als Möglichkeiten formuliert, und die Analyse warnt selbst vor zu weitgehenden Schlussfolgerungen aus dem Neustart. Ihre Stärke liegt gerade darin, die Reichweite der vorhandenen Evidenz eng zu halten.

## 5. Explizit erkannte Blindstellen

A1 erkennt vor allem Blindstellen der **Messung**: fehlende Wait-Zeiten, fehlende Zustände vor dem Restart, zu grob aggregierte Runtime-Metriken sowie fehlende Korrelation mit Prozessalter.  

A2 benennt zusätzlich mehrere komplett unbekannte Dimensionen: Request-Typ, Gleichzeitigkeit der betroffenen Requests, Incident-Dauer, Zahl betroffener Instanzen und vor allem, **was der Neustart technisch tatsächlich zurücksetzt**.  Das ist eine wichtige epistemische Bestandsaufnahme.

A3 erkennt die breitesten Blindstellen: Aggregationsprobleme bei DB-Metriken, unklarer Effekt früherer Optimierungen, mögliche Instanzspezifik, Request-/Datenabhängigkeit, Retry-/Timeout-Kaskaden sowie Routing-/Load-Balancing-Effekte.  

Damit hat **A3 die beste Blindstellenabdeckung**.

## 6. Welche Vorschläge wirklich unterscheidende Tests ermöglichen

Nicht jede Messung ist ein unterscheidender Test. „Mehr CPU-Metriken sammeln“ könnte beispielsweise nur zusätzliche Beobachtung liefern. Höherwertig sind Eingriffe oder Vergleiche, bei denen verschiedene Hypothesen unterschiedliche Vorhersagen machen.

Der stärkste gemeinsame Test ist die **Zeitzerlegung eines konkret langsamen Requests**. Wenn 8 Sekunden im Pool-Wait liegen, verlieren GC, reine lokale Rechenzeit und langsame DB-Ausführung erheblich an Wahrscheinlichkeit. A2 formuliert das besonders klar. 

Danach sind diese Tests besonders trennscharf:

* **Traffic auf andere Instanz verschieben, ohne Prozessrestart:** Heilung spricht gegen einen zwingend nötigen Prozessreset und stärker für Instanz-, Routing- oder Kommunikationskontext.
* **Instanz aus LB entfernen und wieder hinzufügen, ohne Neustart:** trennt Routing-/LB-Effekt von echtem Prozessreset.
* **Nur Connection-Pool/Client zurücksetzen:** trennt Verbindungszustand von anderem Prozesszustand.
* **Betroffene und gesunde Instanz gleichzeitig vergleichen:** trennt lokale von gemeinsamen Downstream-/Infrastrukturursachen.
* **Request-Kohorten vergleichen:** gemeinsamer Endpoint, Kunde, Key, Payload etc. trennt requestabhängige von instanzweiten Mechanismen.
* **Zeitverlauf seit Restart beobachten:** monotone oder nutzungsabhängige Drift stärkt Akkumulations-/Leak-/Degenerationshypothesen.

Gerade die ersten drei aus A3 sind echte **Interventionstests** statt nur zusätzliche Telemetrie. 

## Offene Evidenz

Trotz der drei Analysen fehlen weiterhin die Daten, die den Hypothesenraum tatsächlich verkleinern würden: Wo liegt die zusätzliche Zeit eines langsamen Requests? Betrifft das Phänomen einen Request-Typ oder viele? Eine Instanz oder mehrere? Gibt es zeitliches Clustering? Welche Zustände verändern sich beim Restart? Muss überhaupt der Prozess beendet werden? Ist das Verhalten an Prozess, Instanz, Host oder Traffic-Zuordnung gebunden?

Vor allem ist bisher nicht gezeigt, dass irgendein Pool erschöpft, irgendein Lock blockiert, eine Connection stale, GC langsam oder ein Downstream ursächlich ist. Das sind weiterhin Kandidaten, keine Befunde.

## Empfohlener nächster Untersuchungsschritt

Der nächste Schritt sollte **kein weiterer Hypothesenkatalog**, sondern ein einzelner Incident mit einem kleinen Satz kausal informativer Messungen sein.

Priorität hätte:

**1. Einen langsamen Request vollständig zeitlich zerlegen.**
Queue-/Worker-Wait, Pool-Wait, lokale Verarbeitung, DNS/Connect/TLS, Downstream-Zeit, Retries und Timeouts getrennt erfassen.

**2. Im selben Incident vor dem Neustart betroffene und gesunde Instanz vergleichen.**

**3. Danach den Restart als kontrollierte Intervention zerlegen.**
Zuerst Traffic-Umschaltung bzw. LB-Drain ohne Restart, danach selektiver Connection-/Client-/Pool-Reset und erst zuletzt vollständiger Prozessrestart.

Diese Reihenfolge liefert nicht bloß weitere Verdächtige, sondern entscheidet zwischen mehreren bereits vorhandenen Erklärungsklassen.

## Stop/Weiter-Entscheidung

**STOP für einen weiteren allgemeinen Analyse-Agenten.**

Der Grenznutzen eines vierten frei arbeitenden Root-Cause-Agenten ist voraussichtlich gering. Pools, Queues, Locks, Connections, Runtime, Cache, Downstreams, Instanzspezifik und Neustartzustand sind bereits mehrfach abgedeckt; A3 ergänzt zudem die wichtigste bisher fehlende Gegenperspektive, nämlich dass der Neustart selbst diagnostisch unspezifisch ist und Routing bzw. Kommunikationskontext verändern kann.

Ein vierter allgemeiner Agent würde mit hoher Wahrscheinlichkeit weitere Varianten derselben Kandidaten produzieren. Der Engpass ist jetzt **Evidenz**, nicht Ideengenerierung.

Falls dennoch ein weiterer Agent eingesetzt wird, sollte er deshalb nicht erneut nach Ursachen brainstormen, sondern strikt orthogonal als **Experiment-Design-/Causal-Diagnosis-Agent** arbeiten: minimale Interventionen definieren, für jede Hypothesenklasse Vorhersagen festlegen und daraus einen Entscheidungsbaum für den nächsten Incident erzeugen. Das wäre neue Arbeit; ein weiterer allgemeiner Ursachenanalyst wäre es nicht.
