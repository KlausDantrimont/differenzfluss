
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

---

Auf Basis ausschließlich der gegebenen Fallbeschreibung  und mit Fokus auf **RELATION** und **INFORMATION**:

## 1. Gesicherte Beobachtungen

### RELATION

* Das System ist **die meiste Zeit stabil**. 
* Die starke Latenzerhöhung betrifft **einzelne Requests**, nicht nachweislich alle Requests oder das gesamte System. 
* Die Störung tritt **unregelmäßig** auf. 
* Ein **Neustart des betroffenen Dienstes** beseitigt das beobachtete Problem zuverlässig, aber nur vorübergehend. Damit ist eine Beziehung zwischen dem Zustand dieses Dienstes und dem Symptom gesichert; die Art dieser Beziehung ist nicht geklärt. 
* Optimierungen einzelner Komponenten haben das Verhalten **nicht dauerhaft verändert**. Daraus folgt nicht, dass diese Komponenten irrelevant sind; nur eine dauerhafte Beseitigung wurde dadurch bisher nicht erreicht. 

### INFORMATION

* CPU-, Speicher- und Datenbankmetriken zeigen während der Störung **keine eindeutige Auffälligkeit**. 
* Daraus lässt sich lediglich ableiten, dass die **vorhandenen** Metriken dort keinen klaren Befund zeigen. Es ist nicht gesichert, dass CPU, Speicher oder Datenbank keinerlei Rolle spielen.
* Weitere gesicherte Befunde liegen ausdrücklich nicht vor. 

---

## 2. Daraus folgende Fragen

### RELATION

Zu untersuchen wären insbesondere Beziehungen, die durch aggregierte Komponentenmetriken leicht verborgen bleiben:

* Welche Eigenschaft unterscheidet **langsame von normalen Requests**?

  * Zieloperation?
  * Request-Typ?
  * Mandant/User?
  * bestimmte Daten?
  * bestimmte Instanz?
  * bestimmte Verbindung oder Session?
  * bestimmter Upstream/Downstream?

* Sind langsame Requests an **dieselbe Dienstinstanz** gebunden oder über mehrere Instanzen verteilt?

* Gibt es eine Beziehung zwischen der Störung und der **Lebensdauer des Prozesses**?

  * Zeit seit Neustart?
  * Anzahl verarbeiteter Requests?
  * Anzahl eröffneter Verbindungen/Sessions?
  * Zahl bestimmter Zustandsübergänge?

* Welche Ressourcen oder Zustände werden durch einen Neustart tatsächlich zurückgesetzt?

  * Prozessinterner Zustand
  * Pools
  * Caches
  * Queues
  * Verbindungen
  * Sessions
  * Locks/Leases
  * lokale Worker-/Thread-Zustände

* Ist die Latenz **im betroffenen Dienst selbst** entstanden oder wartet dieser auf eine andere Komponente?

* Gibt es Beziehungen zwischen mehreren Requests?

  * blockiert ein Request einen anderen?
  * teilen sie eine Ressource?
  * gibt es Serialisierung, Fairness- oder Head-of-Line-Effekte?

* Verändert der Neustart nur den Dienst selbst oder auch dessen **Beziehungen zu externen Ressourcen**, etwa indem Verbindungen neu aufgebaut oder Zuordnungen erneuert werden?

### INFORMATION

* Werden aktuell nur **Durchschnitts- oder aggregierte Werte** betrachtet, während einzelne Ausreißer unsichtbar bleiben?
* Kann die bestehende Telemetrie erkennen, **wo innerhalb eines Requests Zeit verloren geht**?
* Gibt es per-Request-Traces oder nur Komponentenmetriken?
* Werden Wartezeiten separat von aktiver Rechenzeit gemessen?
* Sind Queueing, Pool-Auslastung, Lock-Wartezeiten, Verbindungszustände und Retries beobachtbar?
* Gibt es Instanz-, Worker-, Thread-, Connection- oder Request-spezifische Dimensionen?
* Sind Zustandsänderungen vor und nach einem Neustart vergleichbar dokumentiert?

---

## 3. Prüfbare Hypothesen

Diese Hypothesen sind **keine Ursachenbehauptungen**, sondern aus RELATION/INFORMATION ableitbare Prüfpfade.

### H1: Der relevante Zustand ist instanzlokal

**Hypothese:** Langsame Requests korrelieren mit einer bestimmten Dienstinstanz oder einem darin enthaltenen Zustand.

**Prüfung:** Requests nach Instanz aufteilen und Latenzverteilungen vergleichen. Bei Störung prüfen, ob ein Neustart nur der fraglichen Instanz die Auffälligkeit beendet.

---

### H2: Das Symptom hängt von einem Zustand ab, der durch Neustart zurückgesetzt wird

**Hypothese:** Ein langlebiger Zustand verändert sich über die Betriebszeit und wird beim Neustart verworfen.

Mögliche Zustandsklassen, ohne Festlegung auf eine davon: Pool-, Cache-, Queue-, Session-, Connection-, Worker- oder interner Prozesszustand.

**Prüfung:** Zustand und Alter des Prozesses unmittelbar vor und nach dem Neustart erfassen und korrelieren.

---

### H3: Die Verzögerung besteht überwiegend aus Wartezeit

**Hypothese:** Der Request benötigt nicht wesentlich mehr CPU-Arbeit, sondern wartet auf eine Ressource oder einen Zustandsübergang.

Das wäre mit unauffälliger CPU grundsätzlich vereinbar, ist dadurch aber nicht bewiesen.

**Prüfung:** Request-Dauer in aktive Ausführung und einzelne Wartephasen zerlegen.

---

### H4: Nur eine Teilmenge von Requests durchläuft einen problematischen Pfad

**Hypothese:** Die langsamen Requests besitzen ein gemeinsames Merkmal, das normale Requests nicht besitzen.

**Prüfung:** Schnelle und langsame Requests anhand von Route, Instanz, Abhängigkeiten, Datenklasse, Connection, Retry-Verhalten und weiteren Request-Dimensionen vergleichen.

---

### H5: Aggregierte Metriken verdecken einen lokalen Engpass

**Hypothese:** Eine Ressource ist auf Gesamtservice-Ebene unauffällig, während ein kleiner Pool, Worker, Shard, Thread oder eine Verbindung stark belastet bzw. blockiert ist.

**Prüfung:** Metriken mit feinerer Kardinalität und Verteilungsmaßen statt ausschließlich aggregierter Service-Werte erfassen.

---

### H6: Die relevante Beziehung liegt zwischen dem Dienst und einer externen Abhängigkeit

**Hypothese:** Der Neustart erneuert eine Beziehung zu einer anderen Ressource, obwohl deren globale Metriken selbst unauffällig bleiben.

**Prüfung:** Für jeden langsamen Request Abhängigkeitsaufrufe inklusive Verbindung, Timing, Retry und Zielinstanz nachvollziehen.

---

## 4. Benötigte Evidenz

Am aussagekräftigsten wäre Evidenz, die **langsame und normale Requests direkt vergleichbar** macht:

* End-to-End-Trace pro Request mit Zeitanteilen pro Hop/Operation.
* Request-ID plus Dienstinstanz, Prozess-ID und gegebenenfalls Worker-/Thread-Kontext.
* Latenzverteilungen und Tail-Werte statt nur Mittelwerte.
* Zeitpunkt des Auftretens relativ zu Prozessstart bzw. letztem Neustart.
* Vorher-/Nachher-Snapshot beim Neustart relevanter dienstinterner Zustände.
* Pool-Metriken: belegt/frei/wartend, Erwerbsdauer, Timeouts.
* Queue-Metriken: Tiefe, Wartezeit, Alter des ältesten Elements.
* Connection-Metriken: Alter, Zustand, Wiederverwendung, Fehler, Reconnects.
* Retry-/Timeout-Ereignisse pro Request.
* Lock-/Synchronisationswartezeiten, soweit vorhanden.
* Vergleich: **gleicher Request-Typ, gleiche Zeit, unterschiedliche Instanz**.
* Vergleich: **langsame vs. schnelle Requests auf derselben Instanz**.

Ein besonders informativer Versuch wäre, während einer Störung zunächst **nicht sofort neu zu starten**, sondern einen kurzen Zustands- und Trace-Snapshot zu erfassen und denselben Satz unmittelbar nach dem Neustart erneut aufzunehmen. Entscheidend wäre dabei nicht nur, *was* sich ändert, sondern welche Änderung mit dem Verschwinden der hohen Latenz zusammenfällt.

## 5. Blindstellen dieser Perspektive

Der RELATION-/INFORMATION-Fokus hat bewusst Grenzen:

* Er identifiziert eher **fehlende Beziehungen und Beobachtbarkeit** als konkrete Defekte.
* Dass ein Neustart wirkt, sagt nicht, **welcher** zurückgesetzte Zustand relevant ist.
* Korrelation zwischen einem Zustand und hoher Latenz wäre noch keine Kausalität.
* Die Perspektive kann einen Fehler übersehen, der sich erst aus konkreter Implementierungslogik, Code oder Protokolldetails erklärt.
* Unauffällige vorhandene Metriken können sowohl echte Unauffälligkeit als auch **ungeeignete Aggregation, Sampling oder fehlende Dimensionen** bedeuten.
* Ohne Telemetrie aus einer tatsächlichen Störungsphase lassen sich die genannten Hypothesen nicht gegeneinander priorisieren.
* Aussagen darüber, ob Netzwerk, Datenbank, Runtime, Synchronisation, Pools oder andere Komponenten ursächlich beteiligt sind, wären mit dem vorhandenen Material nicht gerechtfertigt.

Der zentrale Erkenntnisbedarf aus dieser Perspektive ist daher nicht „Welche Komponente ist kaputt?“, sondern: **Welche Beziehung unterscheidet langsame von normalen Requests, und welcher durch den Neustart veränderte Zustand ist in der aktuellen Beobachtbarkeit noch unsichtbar?**

---

Auf Basis des Testfalls lässt sich **noch keine konkrete technische Ursache kausal behaupten**. Der stärkste vorhandene Hinweis ist der reproduzierbare Zusammenhang mit dem Neustart; selbst dieser identifiziert aber nicht, *welcher* durch den Neustart veränderte Zustand ursächlich ist.

## 1. Gesicherte Beobachtungen

Gesichert ist nur:

* Das verteilte System läuft die meiste Zeit stabil.
* In unregelmäßigen Abständen steigt die Antwortzeit **einzelner Requests** stark an.
* Ein Neustart des als betroffen bezeichneten Dienstes beseitigt das beobachtete Problem zuverlässig, jedoch nur vorübergehend. 
* CPU-, Speicher- und Datenbankmetriken zeigen während der Störung **keine eindeutige Auffälligkeit**. Das belegt nicht, dass diese Ressourcen irrelevant sind; nur, dass die vorhandenen Metriken bisher keinen eindeutigen Befund liefern. 
* Optimierungen einzelner Komponenten haben keine dauerhafte Änderung bewirkt. Welche Komponenten, welche Optimierungen und unter welchen Bedingungen, ist nicht angegeben. 
* Weitere gesicherte Befunde liegen ausdrücklich nicht vor. 

**Kausal noch nicht belegt** ist insbesondere:

> „Der Dienst selbst besitzt einen Fehler, der die Latenz verursacht.“

Denn ein Neustart verändert gleichzeitig viele Dinge: Prozesszustand, Verbindungen, lokale Queues, Caches, Zuordnung von Requests, eventuell Routing und weitere nicht spezifizierte Zustände. Welche dieser Änderungen wirksam ist, wissen wir nicht.

---

## 2. Prüfbare konkurrierende Hypothesenklassen

Die Hypothesen sollten so breit bleiben, dass nicht vorschnell eine konkrete Implementierungsursache angenommen wird.

| Klasse                                                                   | Kausale Behauptung                                                                                                                                                | Mit bisherigen Befunden vereinbar?                                     |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **H1: Akkumulierender lokaler Zustand**                                  | Ein Zustand im laufenden Dienst entwickelt sich mit der Zeit so, dass bestimmte Requests verzögert werden; Neustart setzt ihn zurück.                             | Ja                                                                     |
| **H2: Externer Zustand, der durch Neustart indirekt zurückgesetzt wird** | Ursache liegt außerhalb des eigentlichen Dienstprozesses, z. B. in einer Verbindung oder Interaktion; Neustart trennt/erneuert diese Beziehung.                   | Ja                                                                     |
| **H3: Traffic-/Routing-Effekt des Neustarts**                            | Nicht der Reset des Prozesses, sondern das Entfernen und erneute Einbinden der Instanz bzw. eine Veränderung der Request-Zuordnung beendet das Symptom.           | Ja                                                                     |
| **H4: Bestimmte Request-/Lastklasse**                                    | Nur bestimmte Requests oder Kombinationen von Requests erzeugen die hohen Latenzen; Neustarts verändern lediglich vorübergehend die Bedingungen dafür.            | Ja                                                                     |
| **H5: Verdeckte Ressourcen-/Queue-Problematik**                          | Eine relevante Ressource oder Warteschlange ist betroffen, wird aber von den vorhandenen CPU-/Speicher-/DB-Metriken nicht mit ausreichender Granularität erfasst. | Ja                                                                     |
| **H6: Neustart und Erholung sind nur korreliert**                        | Die Störung würde ungefähr zum selben Zeitpunkt auch ohne Neustart verschwinden.                                                                                  | Weniger naheliegend, aber mit den gegebenen Daten nicht ausgeschlossen |

Wichtig ist: **H1 ist nicht automatisch „Memory Leak“**, H5 nicht automatisch „Thread Pool“ usw. Solche konkreten Ursachen wären erst Unterhypothesen, sobald zusätzliche Evidenz vorliegt.

---

## 3. Unterscheidende Tests

Hier liegt der größte Informationsgewinn. Statt Komponenten nacheinander zu optimieren, sollte jeweils **eine Eigenschaft des Neustarts isoliert werden**.

### Trennexperiment A: Neustart gegen Nicht-Neustart

Bei einer auftretenden Störung zwei möglichst vergleichbare Einheiten beobachten:

* eine wird neu gestartet,
* eine bleibt unverändert.

Danach denselben definierten Latenzindikator verfolgen.

**Trennt vor allem H6 von H1–H5.**

Wenn nur die neu gestartete Einheit unmittelbar und reproduzierbar gesund wird, wird die Behauptung „Neustart verändert kausal etwas Relevantes“ deutlich stärker.

Wenn beide gleichzeitig gesund werden, wäre der Neustart als Ursache der Erholung wesentlich weniger überzeugend.

---

### Trennexperiment B: Traffic entfernen vs. Prozess neu starten

Falls die Architektur dies erlaubt, während einer Störung getrennt testen:

1. Dienst/Instanz lediglich aus dem Traffic nehmen und danach wieder zuschalten, **ohne Prozesszustand zurückzusetzen**.
2. In einem anderen Fall tatsächlich den Prozess neu starten.

**Interpretation:**

* Traffic-Drain allein heilt → H3/H4 werden stärker.
* Nur echter Prozessreset heilt → H1/H2/H5 werden stärker.
* Beides heilt → die Interventionen teilen möglicherweise einen bislang unbekannten gemeinsamen Effekt.

Das wäre wesentlich informativer als eine weitere Komponentenoptimierung.

---

### Trennexperiment C: Teilzustände statt ganzen Dienst zurücksetzen

Der Neustart ist derzeit eine sehr grobe Intervention. Wenn technisch möglich, einzelne durch ihn veränderte Zustände separat zurücksetzen, beispielsweise eine bestimmte Art externer Verbindung oder einen anderen klar definierten lokalen Zustand.

Entscheidend ist nicht, *welchen* Kandidaten man zuerst vermutet, sondern das Muster:

[
\text{Reset von X} \rightarrow \text{Symptom verschwindet}
]

während

[
\text{Reset von Y} \rightarrow \text{Symptom bleibt}
]

Das zerlegt den Neustart schrittweise in kausal unterscheidbare Interventionen.

---

### Trennexperiment D: Betroffene Requests end-to-end lokalisieren

Für langsame und normale Requests derselben möglichst vergleichbaren Klasse die Zeitanteile entlang des Request-Pfads erfassen.

Gesucht wird nicht einfach „eine auffällige Metrik“, sondern:

**Wo entsteht die zusätzliche Zeit?**

Beispielsweise abstrakt:

[
T_{\text{gesamt}}
=================

T_1+T_2+\ldots+T_n+T_{\text{Warten}}
]

Dann langsame gegen normale Requests vergleichen.

Das trennt:

* Verzögerung innerhalb des betroffenen Dienstes,
* Warten vor der eigentlichen Verarbeitung,
* Verzögerung bei einer Abhängigkeit,
* ausschließlich end-to-end sichtbare Verzögerung.

Damit könnten insbesondere H1/H5 gegen H2 abgegrenzt werden.

---

### Trennexperiment E: Alter des Prozesses gegen absoluten Zeitpunkt

Nach mehreren Neustarts erfassen:

[
\text{Zeit seit Neustart}
]

bis zur nächsten Störung.

Dann prüfen, ob das Risiko der Störung stärker mit **Prozessalter** als mit Uhrzeit, Lastphase oder anderen äußeren Bedingungen zusammenhängt.

Ein reproduzierbares Muster wie

[
P(\text{Störung}\mid\text{Prozessalter})
]

würde eine akkumulierende Zustandsklasse H1 stützen.

Unregelmäßige Abstände allein reichen dafür nicht.

---

### Trennexperiment F: Gleicher Request, unterschiedlicher Zustand

Wenn technisch und betrieblich vertretbar, denselben oder einen äquivalenten Request unter kontrollierten Bedingungen an:

* eine gerade unauffällige/frische Instanz und
* eine aktuell betroffene Instanz

richten.

**Mögliche Trennung:**

* nur betroffene Instanz langsam → instanz-/zustandsbezogene Hypothesen gewinnen.
* auf beiden langsam → Request-, Dependency- oder systemweite Erklärung gewinnt.
* unterschiedliche Requestklassen reagieren unterschiedlich → H4 wird stärker.

Dieses Experiment ist besonders wertvoll, weil Request und Systemzustand voneinander getrennt werden.

---

## 4. Benötigte Evidenz für einen Kausalschluss

Für die Aussage

> „X verursacht die hohen Antwortzeiten“

würden die bisherigen Beobachtungen nicht genügen.

Mindestens nötig wären mehrere Evidenzschichten:

**Erstens: zeitliche Ordnung.**
Die vermutete Ursache (X) muss vor der zusätzlichen Latenz auftreten.

**Zweitens: Kovariation.**
Wenn (X) vorhanden beziehungsweise stärker ausgeprägt ist, muss die Störung systematisch häufiger oder stärker auftreten.

**Drittens: Intervention.**
Gezielte Veränderung von (X) sollte die erwartete Änderung von (Y), der Request-Latenz, erzeugen:

[
do(X) \Rightarrow \Delta Y
]

Nicht nur:

[
X \text{ tritt gemeinsam mit } Y \text{ auf}.
]

**Viertens: geeignetes Gegenfaktual.**
Es muss möglichst gezeigt werden, was unter vergleichbaren Bedingungen **ohne** Intervention passiert wäre. Deshalb ist „Restart vs. No Restart“ wichtiger als die bloße Beobachtung, dass ein Restart gefolgt von Erholung ist.

**Fünftens: Trennung gekoppelter Interventionen.**
Da ein Neustart viele Zustände gleichzeitig verändert, muss gezeigt werden, welcher davon entscheidend ist.

**Sechstens: Replikation.**
Das gleiche Trennmuster sollte über mehrere unabhängige Störungsepisoden auftreten. Ein einzelner erfolgreicher Versuch wäre schwach.

Der derzeit stärkste zulässige Kausalsatz wäre daher ungefähr:

**„Eine oder mehrere durch den Neustart veränderte Bedingungen scheinen für die Fortdauer des Symptoms relevant zu sein.“**

Selbst das sollte idealerweise noch durch einen kontrollierten Restart-vs.-No-Restart-Vergleich abgesichert werden.

---

## 5. Blindstellen dieser Perspektive

Die konsequente Kausalperspektive hat selbst Grenzen.

**Komplexe Mehrfachursachen.** Mehrere Bedingungen könnten gemeinsam notwendig sein. Ein Test, der nur einen Faktor isoliert, kann dann fälschlich wie ein Nullbefund aussehen.

**Nicht beobachtete Zustände.** Es können relevante Variablen existieren, für die momentan weder Messpunkte noch Interventionen verfügbar sind. „Keine Auffälligkeit in den Metriken“ ist deshalb keine starke Negativ-Evidenz.

**Intervention verändert das System selbst.** Neustart, Traffic-Drain oder zusätzliche Instrumentierung können Nebeneffekte erzeugen. Ein positiver Test identifiziert daher zunächst die Intervention, nicht automatisch ihren vermuteten Mechanismus.

**Seltene Ereignisse.** Wegen der unregelmäßigen Störungen können viele Wiederholungen notwendig sein, bevor Unterschiede zwischen Hypothesen robust werden.

**Verteilte Systeme erschweren das Gegenfaktual.** Zwei scheinbar vergleichbare Requests oder Instanzen können tatsächlich unterschiedliche Abhängigkeiten, Pfade oder zeitgleiche Umgebungsbedingungen besitzen.

### Priorität

Mit den gegebenen Informationen wäre die höchste diagnostische Priorität **nicht eine weitere Ursachenoptimierung**, sondern diese Sequenz:

**Restart vs. No Restart → Traffic-Reset vs. Prozess-Reset → Lokalisierung der zusätzlichen Request-Zeit → gezielte Teil-Resets.**

Damit würde aus dem derzeitigen Befund „Restart hilft“ schrittweise eine wesentlich engere kausale Aussage.

---

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

