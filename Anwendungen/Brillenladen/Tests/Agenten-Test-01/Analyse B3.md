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
