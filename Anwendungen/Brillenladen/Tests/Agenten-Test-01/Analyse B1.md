## 1. Gesicherte Beobachtungen

**ZEIT**

* Das System ist **die meiste Zeit stabil**. Die Störung ist also kein permanenter Zustand. 
* In **unregelmäßigen Abständen** steigt die Antwortzeit einzelner Requests stark an. Damit ist bislang weder eine feste Periodizität noch ein deterministischer Zeitpunkt belegt. 
* Ein Neustart des betroffenen Dienstes beseitigt das beobachtete Problem **zuverlässig, aber nur vorübergehend**. Gesichert ist damit eine zeitliche Beziehung zwischen Neustart und Verschwinden des Symptoms, nicht deren Ursache. 
* Änderungen beziehungsweise Optimierungen einzelner Komponenten haben das Verhalten bisher **nicht dauerhaft** verändert. 

**ZUSTAND**

* Während der Störung zeigen CPU-, Speicher- und Datenbankmetriken **keine eindeutige Auffälligkeit**. Das schließt andere, nicht gemessene oder zu grob aggregierte Zustände nicht aus. 
* Weitere gesicherte Befunde liegen nicht vor. Insbesondere ist kein konkreter interner Zustand als Ursache belegt. 

## 2. Daraus folgende Fragen

**ZEIT**

* Wie lange läuft der Dienst typischerweise, bevor die erste Latenzspitze auftritt?
* Ist die relevante Zeitgröße tatsächlich **Zeit seit Neustart**, oder korreliert das Auftreten stärker mit etwas anderem, etwa:

  * Anzahl verarbeiteter Requests,
  * Zahl bestimmter Operationen,
  * Zeit seit einer bestimmten Interaktion,
  * Tageszeit,
  * periodischen Hintergrundprozessen?
* Entsteht die Störung abrupt oder entwickelt sie sich graduell?
* Werden Latenzspitzen mit zunehmender Laufzeit häufiger, stärker oder länger?
* Gibt es nach einem Neustart eine reproduzierbare störungsfreie Phase?
* Betrifft ein Ereignis nur einzelne Requests isoliert, oder treten sie zeitlich gehäuft auf?
* Gibt es einen zeitlichen Zusammenhang mit Deployments, Konfigurationsänderungen, Verbindungsabbrüchen oder externen Ereignissen?

**ZUSTAND**

* Welche Zustände existieren im Dienst, die durch die vorhandenen CPU-, Speicher- und Datenbankmetriken nicht sichtbar werden?
* Welche davon sind:

  * langlebig,
  * pro Prozess,
  * pro Thread,
  * pro Verbindung,
  * pro Client,
  * pro Request,
  * cache- oder poolbezogen?
* Gibt es Zustände, die sich über Zeit oder Nutzung akkumulieren und bei Neustart zurückgesetzt werden könnten?
* Gibt es temporäre Zustände, die nur für die langsamen Requests gelten?
* Unterscheidet sich der interne Zustand unmittelbar **vor**, **während** und **nach** einer Latenzspitze?
* Welche Zustände überleben einen Dienstneustart und welche nicht?

## 3. Prüfbare Hypothesen

Diese Hypothesen sind ausdrücklich **keine Root-Cause-Aussagen**.

### H1: Laufzeitabhängigkeit

Die Wahrscheinlichkeit oder Stärke der Latenzspitzen hängt von der Zeit seit dem letzten Neustart ab.

**Prüfbar durch:** Auftragen der Ereignisrate und Latenz gegen „uptime since restart“.

**Unterscheidendes Muster:** Eine systematische Verschlechterung mit zunehmender Laufzeit würde H1 stützen; ein fehlender Zusammenhang würde dagegen sprechen.

---

### H2: Nutzungsabhängige statt zeitabhängige Akkumulation

Nicht die verstrichene Zeit, sondern eine kumulierte Nutzung verändert einen verborgenen Zustand.

**Prüfbar durch:** Vergleich von Zeit seit Neustart mit kumulativen Größen wie Request-Anzahl oder Anzahl relevanter Operationen.

**Unterscheidendes Muster:** Das Problem tritt bei ähnlichem Nutzungsstand, aber unterschiedlicher Laufzeit auf.

---

### H3: Temporärer interner Zustand einzelner Ausführungspfade

Langsame Requests geraten zeitweise in einen anderen internen Zustand als normale Requests.

**Prüfbar durch:** Vergleich von Traces beziehungsweise zustandsnaher Telemetrie schneller und langsamer Requests.

**Unterscheidendes Muster:** Bestimmte Warte-, Queue-, Pool-, Lock- oder Retry-Zustände treten nur oder gehäuft bei langsamen Requests auf.

---

### H4: Prozesslokaler Zustand

Ein relevanter Zustand gehört zum laufenden Dienstprozess und könnte durch dessen Neustart verworfen beziehungsweise neu initialisiert werden.

Ein Neustart **könnte prinzipiell** beispielsweise Prozessspeicher, lokale Caches, Pools, Verbindungen, Threads, Queues, Timer oder andere prozesslokale Verwaltungszustände neu erzeugen. Dass einer davon hier tatsächlich relevant ist, ist nicht belegt.

**Prüfbar durch:** gezielte Beobachtung dieser Zustände vor und nach Neustarts.

**Unterscheidendes Muster:** Ein Kandidatenzustand unterscheidet sich konsistent unmittelbar vor und nach dem Neustart und entwickelt sich vor späteren Störungen erneut.

---

### H5: Episodischer Zustand statt gradueller Akkumulation

Der Dienst wechselt gelegentlich in einen problematischen Zustand und verbleibt dort zumindest zeitweise.

**Prüfbar durch:** hochauflösende Zeitreihen um Beginn und Ende von Störungsepisoden.

**Unterscheidendes Muster:** Klar erkennbare Zustandsübergänge statt kontinuierlicher Verschlechterung.

---

### H6: Extern ausgelöster, intern persistierender Zustand

Ein externes Ereignis könnte einen temporären internen Zustand auslösen, der bis zu einem späteren Zustandswechsel oder Neustart bestehen bleibt.

**Prüfbar durch:** zeitliche Korrelation externer Ereignisse mit dem **Beginn** einer Störung, nicht nur mit einzelnen langsamen Requests.

**Unterscheidendes Muster:** Wiederkehrende externe Ereignisse liegen unmittelbar vor dem Übergang von „normal“ zu „gestört“.

## 4. Benötigte Evidenz

Am wertvollsten wäre eine **gemeinsame Zeitachse**, die Neustarts, normale Requests, langsame Requests und zustandsnahe Messwerte zusammenführt.

Benötigt würden insbesondere:

* exakte Zeitpunkte jedes Neustarts;
* Zeit seit letztem Neustart für jeden Request;
* Beginn, Dauer und Ende jeder beobachteten Störungsepisode;
* vollständige Latenzverteilung statt nur aggregierter Mittelwerte;
* Request- oder Trace-IDs zur Gegenüberstellung schneller und langsamer Requests;
* kumulative Nutzung seit Neustart;
* gegebenenfalls Queue-, Pool-, Verbindungs-, Thread-, Lock-, Retry-, Timeout- oder Cache-Zustände, sofern solche Mechanismen im System existieren;
* Momentaufnahmen relevanter Zustände unmittelbar vor und nach einem Neustart;
* zeitlich korrelierte externe Ereignisse;
* mehrere Neustartzyklen, damit sich prüfen lässt, ob Muster reproduzierbar sind.

Besonders aussagekräftig wäre ein Verlauf der Form:

**Neustart → stabile Phase → möglicher Zustandsübergang → Latenzstörung → Neustart**

Dabei sollte zunächst nur geprüft werden, **ob** dieses Muster reproduzierbar existiert und welche messbaren Zustände sich entlang dieser Zeitachse verändern.

## 5. Blindstellen dieser Perspektive

Die Beschränkung auf **ZEIT** und **ZUSTAND** ist nützlich, aber absichtlich unvollständig.

Sie kann insbesondere Folgendes übersehen:

* strukturelle Unterschiede zwischen bestimmten Request-Typen;
* Abhängigkeiten von konkreten Daten oder Eingaben;
* Topologie- oder Routingeffekte im verteilten System;
* Unterschiede zwischen Instanzen;
* Netzwerkverhalten;
* externe Dienste;
* Fehler in Messung oder Instrumentierung;
* Kausalmechanismen, die weder durch Laufzeit noch durch einen langlebigen internen Zustand charakterisiert sind.

Außerdem besitzt der Neustart geringe diagnostische Spezifität: **Viele unterschiedliche Zustände können durch einen Neustart gleichzeitig verändert werden.** Aus der zuverlässigen vorübergehenden Besserung allein lässt sich deshalb nicht ableiten, *welcher* Zustand relevant ist oder ob der entscheidende Effekt überhaupt im betroffenen Dienst selbst liegt. 

Die stärkste nächste Untersuchung innerhalb dieser Perspektive wäre daher nicht „Was verursacht es?“, sondern: **Welche zeitlich reproduzierbare Zustandsänderung unterscheidet stabile von gestörten Phasen?**


