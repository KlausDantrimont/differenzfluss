Die stärkste Spur ist der **zuverlässige, aber nur temporäre Effekt eines Dienst-Neustarts**. Das spricht dafür, zuerst nach einem Zustand zu suchen, der **innerhalb der laufenden Instanz entsteht oder sich dort akkumuliert**, statt breit einzelne Komponenten weiter zu optimieren. Das ist eine Hypothese, kein gesicherter Befund. 

### Beobachtungen

Gesichert ist nur:

* Das verteilte System ist überwiegend stabil.
* In unregelmäßigen Abständen haben **einzelne Requests stark erhöhte Antwortzeiten**. 
* Ein Neustart des betroffenen Dienstes beseitigt das Problem **zuverlässig**, jedoch nur vorübergehend. 
* CPU-, Speicher- und Datenbankmetriken zeigen währenddessen **keine eindeutige Auffälligkeit**. Das heißt nicht, dass diese Ressourcen als Ursache ausgeschlossen sind; lediglich die vorhandenen Metriken zeigen nichts Eindeutiges. 
* Bisherige Optimierungen einzelner Komponenten haben das Verhalten nicht dauerhaft verändert. 
* Weitere gesicherte Befunde liegen nicht vor. 

### Wahrscheinlich wichtigste Hypothesen

**1. Prozesslokaler Zustand bzw. schleichende Ressourcenerschöpfung**

Das wäre meine erste Untersuchungsrichtung. Kandidaten sind etwa Connection-/Thread-/Worker-Pools, File Descriptors, Sockets, interne Queues, Caches oder andere langlebige Objekte. Entscheidend ist nicht, dass einer dieser Mechanismen nachgewiesen wäre, sondern dass ein Neustart genau solche Zustände zurücksetzt.

Benötigte Evidenz: Werte **pro Dienstinstanz** unmittelbar vor, während und nach der Störung, insbesondere aktive/idle/wartende Pool-Einträge, Queue-Längen und Wait-Zeiten, Threads/Worker, offene FDs/Sockets und gegebenenfalls interne Cache-Größen. Besonders aussagekräftig wäre eine Größe, die zwischen Neustarts wächst oder sich verschlechtert und beim Neustart auf Normalniveau zurückspringt.

**2. Contention, Blockierung oder Queueing innerhalb des Dienstes**

Normale CPU-Auslastung widerspricht diesem Szenario nicht. Requests können langsam sein, weil sie auf Locks, Semaphore, Worker, Connections oder andere Requests warten, während die CPU weitgehend untätig bleibt.

Benötigte Evidenz: Aufteilung der Request-Zeit in **Ausführung vs. Warten**. Sinnvoll wären Thread-/Goroutine-/Task-Dumps während einer Störung, Lock-/Mutex-Contention, Event-Loop-Lag beziehungsweise Worker-Auslastung sowie Queue-Wartezeiten. Wichtig ist, einen Dump **vor dem Neustart** zu bekommen; danach ist der interessante Zustand verloren.

**3. Problem mit langlebigen Verbindungen oder Pools zu Abhängigkeiten**

Ein Neustart baut typischerweise ausgehende Verbindungen neu auf. Deshalb gehören HTTP-/RPC-/DB-Connection-Pools, DNS-Verhalten, Keep-Alive-Verbindungen und andere langlebige Netzwerkzustände zu den wichtigen Kandidaten. Normale Datenbankmetriken allein schließen beispielsweise nicht aus, dass der Dienst lokal auf eine Pool-Connection wartet.

Benötigte Evidenz: Verbindungserstellung, Pool-Wartezeit, Connect-/TLS-/DNS-Zeit, Retries, Timeouts und Connection-Alter. Ein sehr nützlicher Test wäre, wenn technisch vertretbar, **nur den verdächtigen Connection-Pool neu aufzubauen**, ohne den Prozess neu zu starten. Verschwindet die Störung ebenfalls, wird die Ursache deutlich eingegrenzt.

**4. Laufzeit-/GC-/Allocator-Effekt**

Abhängig von der verwendeten Runtime könnten lange Pausen, Heap-Verhalten oder andere Runtime-Zustände einzelne Requests verzögern, ohne dass eine grobe Speicher- oder CPU-Kurve auffällig aussieht.

Benötigte Evidenz: Runtime-spezifische Daten wie GC-Pausen, Heap-/Allocation-Raten, Thread-Pool-Starvation oder Event-Loop-Lag. Dabei sollten nicht nur Minutenmittel betrachtet werden: Ein kurzer 500-ms- oder 2-s-Stall kann für einen Request katastrophal sein und in aggregierten Infrastrukturmetriken praktisch verschwinden.

**5. Externe Abhängigkeit oder spezifischer Request-Pfad**

Dass nur einzelne Requests betroffen sind, könnte auch bedeuten, dass ein bestimmter Codepfad oder eine bestimmte Downstream-Abhängigkeit langsam wird. Der Neustarteffekt macht diese Erklärung allein etwas weniger überzeugend, schließt sie aber nicht aus – beispielsweise wenn der Dienst problematischen Downstream-Zustand cached oder persistente Verbindungen verwendet.

Benötigte Evidenz: Distributed Traces für **langsame und normale Requests desselben Typs**. Für jeden Span sollte sichtbar werden, wo die zusätzliche Zeit entsteht: im eigenen Dienst, beim Queueing oder in welchem Downstream.

### Nächste Untersuchungen

Ich würde nicht mit weiterer Komponentenoptimierung beginnen, sondern zunächst die Störung **beobachtbar und differenzierbar** machen:

1. **Slow-Request-Tracing aktivieren bzw. gezielt erfassen.** Für einen langsamen Request muss anschließend beantwortbar sein: *Wo wurden die zusätzlichen Millisekunden/Sekunden verbracht?*
2. **Bei der nächsten Störung vor dem Restart einen Diagnose-Snapshot ziehen:** Prozess-/Runtime-Dump, Poolzustände, Queues, Connections, FDs und hochauflösende Latenz-/Wait-Metriken.
3. **Betroffene gegen gesunde Instanzen vergleichen.** Falls gleichzeitig mehrere Instanzen existieren, ist dieser Vergleich besonders wertvoll: Was unterscheidet die langsame Instanz von einer gesunden?
4. **Restart als Experiment zerlegen.** Statt nur den ganzen Dienst neu zu starten, soweit gefahrlos möglich einzelne Zustände zurücksetzen: Connection-Pool erneuern, Cache leeren, Worker/Client neu initialisieren. Damit lässt sich feststellen, *welcher Teil des Neustarts* eigentlich heilt.
5. **Zeitliche Entwicklung seit dem letzten Neustart korrelieren.** Interessant sind nicht nur Werte während des Incidents, sondern Größen, die mit der Prozesslaufzeit oder der Anzahl verarbeiteter Requests driften.

Der entscheidende diagnostische Sprung wäre damit von **„der Request ist langsam“** zu **„der Request verbringt 4,2 s wartend auf X“**. Erst danach lässt sich sinnvoll entscheiden, ob die Ursache beispielsweise ein Pool, ein Lock, die Runtime, das Netzwerk oder ein Downstream ist.
