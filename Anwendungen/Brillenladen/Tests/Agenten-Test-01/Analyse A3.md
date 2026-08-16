Die bisherige Evidenz ist zu dünn, um auf eine einzelne Ursache wie „Memory Leak“, „Datenbankproblem“ oder „ineffizienten Code“ zu schließen. Besonders wichtig: **Ein erfolgreicher Neustart ist diagnostisch unspezifisch**. Er setzt gleichzeitig sehr viele Zustände zurück. 

### 1. Gesicherte Beobachtungen

Aus dem Fall sind nur folgende Punkte belastbar:

* Das verteilte System ist überwiegend stabil.
* Unregelmäßig haben **einzelne Requests** stark erhöhte Antwortzeiten.
* Ein Neustart des „betroffenen Dienstes“ beseitigt das Phänomen zuverlässig, jedoch nur vorübergehend.
* CPU-, Speicher- und Datenbankmetriken zeigen während der Störung **keine eindeutige Auffälligkeit**.
* Bisherige Optimierungen einzelner Komponenten haben das Verhalten nicht dauerhaft beseitigt.
* Es gibt keine weiteren gesicherten Befunde. 

Wichtig ist die Formulierung „keine eindeutige Auffälligkeit“: Daraus folgt **nicht**, dass CPU, Speicher oder Datenbank als Ursache ausgeschlossen sind. Es folgt nur, dass die bisher betrachteten Metriken keinen klaren Zusammenhang gezeigt haben.

### 2. Vorschnelle Schlussfolgerungen, die vermieden werden sollten

**„Der Dienst selbst ist kaputt, weil ein Neustart hilft.“**
Nicht zwingend. Ein Neustart verändert unter anderem Prozesszustand, Connections, Pools, Caches, Netzwerkverbindungen, eventuell Service-Discovery-Zustände und möglicherweise auch die Instanz, auf die Traffic anschließend gelangt. Die Ursache kann deshalb außerhalb der eigentlichen Geschäftslogik liegen.

**„Es ist kein Ressourcenproblem, weil CPU und RAM normal sind.“**
Zu eng. Knapp werden können beispielsweise Threads, Connection-Pools, File Descriptors, Sockets, interne Queues oder andere begrenzte Ressourcen, ohne dass CPU oder Gesamtspeicher auffällig werden.

**„Die Datenbank ist es nicht, weil die DB-Metriken normal sind.“**
Auch das ist nicht bewiesen. Einzelne blockierende oder langsame Operationen, Connection-Probleme oder bestimmte Abfragemuster können in aggregierten DB-Metriken verschwinden.

**„Die optimierten Komponenten waren nicht die Ursache.“**
Nur bedingt zulässig. Eine wirkungslose Optimierung widerlegt eine Ursache nur dann, wenn klar ist, dass genau der relevante Mechanismus verändert wurde. Eine allgemeine Performanceverbesserung muss einen intermittierenden Blockierungsmechanismus nicht beeinflussen.

### 3. Plausible Hypothesen – ausdrücklich keine Befunde

| Hypothese                                                           | Warum mit den Beobachtungen vereinbar                                                                          | Was noch fehlt                                                                      |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Erschöpfung eines begrenzten Pools** – Threads, Connections o. Ä. | Kann einzelne Requests warten lassen; Neustart leert/resetet den Zustand; CPU kann niedrig bleiben             | Poolauslastung, Wait-Zeiten und Queue-Längen zum Störungszeitpunkt                  |
| **Lock-/Synchronisationsproblem**                                   | Wartende Threads verursachen Latenz ohne notwendige hohe CPU                                                   | Thread Dumps / Lock-Wait-Daten während der Störung                                  |
| **Interne Queue / Backpressure**                                    | Lange Wartezeit kann entstehen, obwohl die eigentliche Verarbeitung schnell ist                                | Aufteilung der Request-Latenz in Queue- und Processing-Zeit                         |
| **Problem mit langlebigen Netzwerk-/Downstream-Verbindungen**       | Neustart baut Connections neu auf und kann damit temporär heilen                                               | Connection-Alter, Fehler, Retries, TCP-/TLS-/DNS-bezogene Daten                     |
| **Problem eines bestimmten Downstreams**                            | Der lokale Dienst kann nur der Ort sein, an dem gewartet wird                                                  | Distributed Traces mit Zeitanteilen je Hop                                          |
| **GC-/Runtime-Effekt**                                              | Aggregierte Speicher-/CPU-Metriken können kurze oder spezielle Runtime-Probleme übersehen                      | GC-Pausen, Allocation-Verhalten, Runtime-/Heap-Daten                                |
| **Ressourcenleck außerhalb des klassischen Heap-Speichers**         | Passt zur vorübergehenden Heilung durch Neustart                                                               | Entwicklung von FDs, Threads, Connections, Sockets usw. über die Prozesslebensdauer |
| **Instanzspezifischer Zustand**                                     | „Betroffener Dienst“ könnte faktisch eine einzelne Instanz betreffen                                           | Vergleich langsamer und gesunder Instanzen                                          |
| **Request-/Datenabhängigkeit**                                      | Dass nur einzelne Requests betroffen sind, kann auf bestimmte Pfade, Kunden, Schlüssel oder Payloads hindeuten | Vergleich langsamer und normaler Requests nach Eigenschaften                        |
| **Retry-/Timeout-Verstärkung**                                      | Einzelne kleine Störungen können durch Retries zu großen End-to-End-Latenzen werden                            | Retry-Zahlen, Timeout-Stufen und Timeline eines betroffenen Requests                |
| **Cache- oder zustandsabhängiges Verhalten**                        | Neustart verändert lokalen Zustand                                                                             | Cache-Zustand und Latenz vor/nach Neustart                                          |
| **Routing-/Load-Balancing-Effekt**                                  | Neustart kann Traffic umverteilen; die Heilung muss nicht aus dem Prozessreset selbst stammen                  | Instanzgenaues Routing vor und nach dem Neustart                                    |

### 4. Die wichtigste fehlende Evidenz

Der entscheidende nächste Schritt wäre **nicht eine weitere Optimierung**, sondern die Lokalisierung der verlorenen Zeit eines tatsächlich langsamen Requests.

Für mindestens einen betroffenen Request müsste rekonstruiert werden:

**Eingang → Queue/Warten → lokale Verarbeitung → Downstream-Aufrufe → Retries/Timeouts → Antwort.**

Distributed Tracing wäre dafür besonders aussagekräftig. Falls es nicht existiert, wären korrelierbare Zeitstempel und Request-IDs die nächstbeste Variante.

Parallel sollte während einer Störung ein **Vergleich zwischen betroffener und gesunder Instanz** erfolgen. Besonders relevant wären Thread-Zustände, interne Queues, Connection-Pools, offene Deskriptoren/Sockets, Runtime-/GC-Daten und Downstream-Latenzen. Entscheidend ist der Snapshot **vor dem Neustart**; danach ist gerade der interessante Zustand vernichtet.

### 5. Gegenprüfungen mit hohem diagnostischem Wert

Eine sehr wertvolle Gegenprobe wäre, die Wirkung des Neustarts genauer zu zerlegen. Momentan wird aus „Restart → Problem weg“ möglicherweise zu viel geschlossen.

Zu unterscheiden wäre beispielsweise:

1. Verschwindet das Problem schon, wenn die Instanz nur aus dem Load Balancer genommen und wieder aufgenommen wird?
2. Muss tatsächlich der Prozess beendet werden?
3. Reicht es, bestimmte Connections oder Pools neu aufzubauen?
4. Tritt die Störung nach dem Neustart derselben Instanz wieder auf oder ist sie host-/instanzabhängig?
5. Verschwindet das Problem auch, wenn Traffic ohne Neustart auf eine andere Instanz verschoben wird?

Diese Tests würden stark dabei helfen zu unterscheiden zwischen **Prozesszustand**, **Kommunikationszustand**, **Routing** und **äußerer Abhängigkeit**.

### 6. Arbeitshypothese mit der geringsten Überinterpretation

Die stärkste derzeit zulässige Aussage wäre:

> Es scheint einen mit der Laufzeit oder dem Zustand des betroffenen Dienstkontexts verbundenen Mechanismus zu geben, der die Latenz einzelner Requests erhöht und durch einen Neustart zurückgesetzt oder umgangen wird.

Selbst diese Aussage lässt bewusst offen, **welcher Zustand** betroffen ist und ob er tatsächlich innerhalb des Prozesses liegt.

Der größte diagnostische Fehler wäre daher momentan, noch mehr Komponenten „auf Verdacht“ zu optimieren. Die fehlende Information ist nicht primär *wie schnell die Komponenten sind*, sondern **wo ein langsamer Request seine Zeit verbringt und welcher Zustand sich durch den Neustart verändert**.
