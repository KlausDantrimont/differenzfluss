Aus dem Fall lässt sich noch keine einzelne Ursache ableiten. Das auffälligste Signal ist aber die Kombination aus **sporadischer Latenzverschlechterung**, **fehlender klarer CPU-/RAM-/DB-Korrelation** und **zuverlässiger, aber temporärer Heilung durch einen Dienstneustart**. Das verschiebt die Untersuchung weg von reiner Rechen- oder Datenbankkapazität und stärker hin zu **zustandsbehafteten Ressourcen, Warteschlangen und langlebigen Abhängigkeiten innerhalb des betroffenen Prozesses**. 

## 1. Gesicherte Beobachtungen

| Beobachtung                                                             | Was daraus zulässig folgt                                                                                                       |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Das System läuft die meiste Zeit stabil.                                | Kein dauerhaftes Kapazitätsproblem ist belegt.                                                                                  |
| Einzelne Requests werden in unregelmäßigen Abständen sehr langsam.      | Es handelt sich zumindest sichtbar um ein Latenz-/Tail-Latency-Problem, nicht zwingend um einen vollständigen Ausfall.          |
| Neustart des betroffenen Dienstes behebt das Problem zuverlässig.       | Ein Zustand, der durch Prozessneustart zurückgesetzt wird, ist besonders verdächtig.                                            |
| Die Wirkung des Neustarts ist nur temporär.                             | Der problematische Zustand kann sich erneut aufbauen oder erneut ausgelöst werden.                                              |
| CPU, Speicher und DB-Metriken zeigen keine eindeutige Auffälligkeit.    | Diese Ressourcen sind nicht als Ursache ausgeschlossen; nur ein offensichtlicher Zusammenhang ist bisher nicht sichtbar.        |
| Komponentenoptimierungen haben das Verhalten nicht dauerhaft verändert. | Lokale Performanceoptimierung adressiert wahrscheinlich nicht den eigentlichen Mechanismus – oder jedenfalls nicht vollständig. |

Mehr ist durch die Falldaten nicht gesichert. Insbesondere wissen wir nicht, **welcher Request-Typ betroffen ist, ob Requests gleichzeitig betroffen sind, wie lange die Störung anhält, ob mehrere Instanzen betroffen sind oder was ein Neustart intern genau zurücksetzt**. 

## 2. Wahrscheinlich wichtigste Hypothesen

### H1 — Erschöpfung oder Degeneration eines begrenzten Ressourcenpools

Das wäre meine erste Untersuchungsrichtung.

Beispiele für die **Klasse** von Ressourcen, nicht Behauptungen über das konkrete System:

* Thread-/Worker-Pool
* HTTP-/RPC-Connection-Pool
* DB-Connection-Pool
* Socket-/File-Descriptor-Ressourcen
* interne Semaphore oder begrenzte Executor
* sonstige gepoolte Objekte

**Warum passend:** Ein Pool kann schrittweise in einen schlechten Zustand geraten, während Gesamt-CPU und Heap völlig normal aussehen. Requests warten dann hauptsächlich auf Verfügbarkeit statt zu rechnen. Ein Neustart initialisiert den Pool neu.

**Benötigte Evidenz:**

* aktive vs. freie vs. wartende Pool-Slots über die Zeit
* Queue-Wartezeiten getrennt von tatsächlicher Bearbeitungszeit
* Timeout- und Acquisition-Latenzen
* Thread-/Task-Dumps während der Störung
* Vergleich direkt nach Neustart vs. kurz vor Neustart

Besonders aussagekräftig wäre: Viele langsame Requests warten auf **dieselbe Ressource oder denselben Synchronisationspunkt**.

---

### H2 — Queueing / Backpressure innerhalb des Dienstes

Der Dienst könnte intern eine Warteschlange aufbauen, ohne dass CPU oder Speicher sichtbar an ihre Grenzen kommen.

Beispiel:

`Request → Queue → begrenzter Worker/Executor → Downstream`

Ist der Engpass hinter der Queue langsam oder blockiert, steigt vor allem die **Wartezeit**.

**Warum passend:** Hohe Latenz bei niedriger CPU ist für wartende statt rechnende Requests durchaus konsistent. Ein Neustart leert typischerweise auch Queues und beendet blockierte Arbeit.

**Benötigte Evidenz:**

* Queue-Länge
* Queue-Age, also Alter des ältesten Elements
* Zeitstempel für `received`, `queued`, `started`, `completed`
* Anzahl aktiver Worker
* Verhältnis Arrival Rate / Completion Rate
* Verhalten unmittelbar vor und nach Neustart

Nur Queue-Länge reicht nicht. Wichtig ist, **wo die Zeit eines langsamen Requests tatsächlich verbracht wird**.

---

### H3 — Problem mit langlebigen Downstream-Verbindungen oder Clients

Ein interner HTTP-, RPC-, Messaging- oder DB-Client könnte einen degradierten Zustand entwickeln.

Denkbare Mechanismen dieser Kategorie sind beispielsweise defekte/stale Verbindungen, ungünstige Wiederverwendung, Verbindungsaufbauprobleme oder ein fehlerhafter Clientzustand.

**Warum passend:** Ein Prozessneustart verwirft langlebige Verbindungen und erzeugt Clients neu. Gleichzeitig müsste der eigentliche Downstream nicht zwingend auffällige globale Metriken zeigen.

**Benötigte Evidenz:**

Die End-to-End-Latenz sollte in einzelne Phasen zerlegt werden, etwa:

`Pool wait → DNS → connect → TLS → request sent → downstream wait → response`

Zusätzlich:

* Connection-Reuse
* Connect-/Read-Timeouts
* Retries
* Verbindungsalter
* Fehler pro Zielhost
* Unterschiede zwischen Instanzen

Wenn nur eine einzelne Dienstinstanz schlecht wird, während andere denselben Downstream problemlos verwenden, würde das diese Richtung deutlich stärken.

---

### H4 — Lock Contention, Deadlock-artige Zustände oder blockierte Threads

Nicht zwingend ein klassischer Deadlock. Auch ein stark umkämpfter Lock oder eine blockierende Operation kann einzelne Request-Pfade massiv verzögern.

**Warum passend:** Blockierte Threads verbrauchen kaum CPU. Ein Neustart beseitigt den Prozesszustand.

**Benötigte Evidenz:**

Während der Störung:

* mehrere Thread-Dumps in kurzem Abstand
* Lock-Wartezeiten
* Anzahl blockierter/wartender Threads
* Stack-Traces langsamer Requests

Der wichtige Unterschied lautet:

**„Der Request arbeitet langsam“** versus **„der Request arbeitet gar nicht, sondern wartet.“**

Diese Unterscheidung ist im aktuellen Fall noch nicht getroffen.

---

### H5 — Cache oder anderer langlebiger In-Process-Zustand degeneriert

Auch ein Cache kann Performance verschlechtern, obwohl er eigentlich Performance verbessern soll: etwa durch ungünstigen Inhalt, Locking, Invalidierungsverhalten oder zunehmend teure Operationen.

Allgemeiner formuliert könnte irgendein **prozesslokaler Zustand mit der Laufzeit degenerieren**.

**Warum passend:** Der Neustart löscht genau solchen Zustand.

**Benötigte Evidenz:**

Nicht nur Cache-Größe messen, sondern:

* Hit/Miss-Rate
* Lookup-Latenz
* Eviction-Rate
* Ladezeiten
* Locks
* Größe einzelner Einträge
* Korrelation zwischen Prozessalter und Latenz

Diese Hypothese ist momentan schwächer als Pool-/Queue-/Blocking-Probleme, weil keine konkrete Cache-Beobachtung gegeben ist.

---

### H6 — Garbage Collection / Runtime-Pausen

Das sollte geprüft, aber aufgrund der vorhandenen Informationen nicht voreilig angenommen werden.

**Warum denkbar:** Lange Runtime-Pausen können Tail Latency verursachen und werden von groben CPU-/Speicher-Dashboards manchmal schlecht sichtbar gemacht.

**Was dagegen spricht:** Der zuverlässige längerfristige Effekt eines Neustarts ist ohne weitere Evidenz noch keine starke GC-Signatur.

**Benötigte Evidenz:**

* GC-Pausendauer
* Stop-the-world-Zeiten
* Allocation Rate
* Heap nach GC
* eventuell Runtime-/JIT-/Safepoint-Telemetrie der verwendeten Plattform

---

## 3. Wichtigste nächste Untersuchung

Ich würde zunächst **nicht weiter optimieren**, sondern einen langsamen Request kausal zerlegen.

Für jeden Request sollte möglichst eine Zeitlinie entstehen:

```text
Request angenommen
│
├─ Warten auf internen Worker       3 ms
├─ Warten auf Connection Pool       8.4 s
├─ Downstream Call                  42 ms
├─ interne Verarbeitung             7 ms
└─ Response
```

Schon ein einziger solcher Trace während der Störung kann deutlich mehr Erkenntnis liefern als viele aggregierte CPU-/RAM-Dashboards.

Die zentrale Frage lautet:

> **Wo verbringt ein langsamer Request die zusätzliche Zeit?**

Erst danach sollte nach der Ursache dieses Wartens gesucht werden.

## 4. Besonders wertvolles Experiment: Neustart als Diagnoseinstrument

Da der Neustart reproduzierbar hilft, ist er nicht nur ein Workaround, sondern ein sehr wertvoller Hinweis.

Unmittelbar **vor und nach demselben Neustart** sollten Zustände verglichen werden:

| Vor Neustart              | Nach Neustart             |
| ------------------------- | ------------------------- |
| Threads nach State        | Threads nach State        |
| Pool-Auslastung           | Pool-Auslastung           |
| wartende Acquisitions     | wartende Acquisitions     |
| offene Verbindungen       | offene Verbindungen       |
| Queue-Längen              | Queue-Längen              |
| Request-Latenz nach Phase | Request-Latenz nach Phase |
| Client-/Socket-Zustände   | Client-/Socket-Zustände   |
| Runtime-/GC-Zustand       | Runtime-/GC-Zustand       |

Was sich durch den Neustart abrupt normalisiert, ist ein guter Kandidat für den relevanten Zustandsraum.

## 5. Diagnose über Instanzen hinweg

Falls der Dienst mehrfach repliziert ist, wäre ein Vergleich besonders aufschlussreich.

Man sollte bestimmen, ob bei einer Störung:

**A. nur eine Instanz langsam wird**
→ Prozesslokaler Zustand, Pools, Locks, Clients oder Runtime werden deutlich wahrscheinlicher.

**B. alle Instanzen gleichzeitig langsam werden**
→ gemeinsame Downstreams, Netzwerk, Infrastruktur oder externe Last werden interessanter.

**C. nur bestimmte Requests langsam werden**
→ gemeinsamer Codepfad oder gemeinsame Abhängigkeit dieser Requests suchen.

**D. praktisch alle Requests derselben Instanz langsam werden**
→ globale Ressource oder Synchronisationspunkt innerhalb dieser Instanz suchen.

Diese Klassifikation würde den Suchraum stark verkleinern.

## Priorisierung

Mit ausschließlich den gegebenen Informationen würde ich die Richtungen so priorisieren:

1. **Warten auf erschöpfte/degradierte Pools oder andere begrenzte Ressourcen**
2. **interne Queue-/Worker-Erschöpfung**
3. **degradierter Zustand langlebiger Downstream-Verbindungen/Clients**
4. **Locking bzw. blockierte Threads**
5. **anderer degenerierender prozesslokaler Zustand, z. B. Cache**
6. **Runtime/GC-Pausen**
7. erst danach allgemeinere Performanceoptimierung einzelner Komponenten

Der gemeinsame Nenner der ersten vier Hypothesen lautet: **Die Requests könnten überwiegend warten statt rechnen.** Genau deshalb können CPU-, Speicher- und Datenbankmetriken unauffällig bleiben.

Der höchste Erkenntnisgewinn käme daher aus **verteilten Traces mit Zeitaufschlüsselung plus Thread-/Pool-/Queue-Zustand genau während einer Störung**, idealerweise gekoppelt mit einem Vorher-/Nachher-Vergleich beim Neustart.
