# Frage-Generator

## Kompakte Spezifikation

### Zweck

Der Frage-Generator erzeugt nicht möglichst viele Fragen.

Er versucht, aus einer gegebenen Situation die **nächste erkenntnisproduktive Frage** zu bestimmen.

> **Welche Frage verspricht jetzt den größten zusätzlichen Erkenntnisgewinn?**

### Eingabe

Beliebig:

* Beobachtung
* Behauptung
* Problem
* Irritation
* Text
* Gespräch
* Hypothese
* bereits laufende Untersuchung

Optional zusätzlich:

* bisherige Fragen
* bisherige Antworten
* konkurrierende Hypothesen
* verfügbare Evidenz
* Zeit-/Aufwandsbudget

### Arbeitszustand

Der Generator rekonstruiert zunächst:

```text
Was wissen wir?
Was vermuten wir?
Was ist unklar?
Welche Perspektive dominiert bereits?
Welche relevanten Unterschiede wurden noch nicht untersucht?
```

### Fragequellen

Fragen werden aus epistemischen Operatoren erzeugt.

Beispiele:

```text
ZEIT
→ Was hat sich verändert?

RELATION
→ Was hängt womit zusammen?

PERSPEKTIVE
→ Aus welcher Position sähe die Sache anders aus?

SKALA
→ Was ändert sich auf einer anderen Betrachtungsebene?

EVIDENZ
→ Welche Beobachtung trägt diese Behauptung?

GEGENHYPOTHESE
→ Welche andere Erklärung wäre mit denselben Befunden vereinbar?

KAUSALITÄT
→ Welche Beobachtung würde Ursache und bloße Korrelation unterscheiden?

BLINDSTELLE
→ Was kann die bisherige Betrachtung schlecht sehen?
```

Ein Operator erzeugt dabei keine feste Frage, sondern eine **Frageklasse**.

### Ablauf

```text
Situation
↓
aktuellen Erkenntniszustand bestimmen
↓
Restproblem identifizieren
↓
geeignete epistemische Operatoren auswählen
↓
mehrere Kandidatenfragen erzeugen
↓
Kandidaten bewerten
↓
beste nächste Frage auswählen
↓
Antwort / neue Evidenz
↓
Erkenntniszustand aktualisieren
↓
wiederholen oder stoppen
```

### Bewertung einer Frage

Eine Kandidatenfrage ist umso wertvoller, je mehr sie:

* neue Information erwarten lässt,
* bisherige Perspektiven ergänzt,
* konkurrierende Hypothesen trennt,
* relevante Blindstellen öffnet,
* handlungsfähige nächste Schritte erzeugt,

und je weniger sie:

* bereits Bekanntes wiederholt,
* unnötig breit ist,
* hohe Kosten bei geringem Erkenntnisgewinn erzeugt.

Kurz:

> **Fragewert ≈ erwarteter Erkenntnisgewinn – epistemische Kosten**

### Zwei Hauptmodi

**Exploration**

> Was könnte hier noch relevant sein?

Ziel: den Untersuchungsraum erweitern.

**Diskrimination**

> Welche Frage trennt die derzeit plausiblen Erklärungen am stärksten?

Ziel: den Untersuchungsraum verkleinern.

Optional später:

**Intervention**

> Welche Frage führt am schnellsten zu einer entscheidenden Beobachtung oder Handlung?

### Ausgabe

Nicht nur die Frage selbst, sondern kompakt:

```text
Nächste Frage:
...

Warum diese?
...

Verwendeter Schnitt:
...

Was könnte die Antwort unterscheiden?
...

Warum nicht die nächstliegenden Alternativfragen?
...
```

Die Erklärung kann für normale Nutzung weggelassen werden. Sie ist vor allem für Prüfung und Entwicklung nützlich.

### Guardrails

Der Generator soll:

* keine fehlenden Tatsachen erfinden,
* Fragen nicht mit versteckten Behauptungen überladen,
* nicht künstlich Komplexität erzeugen,
* bereits beantwortete Fragen nicht nur umformulieren,
* Unsicherheit erhalten, wenn Evidenz fehlt,
* keine Frage erzeugen, wenn zunächst Beobachtung oder Datenbeschaffung nötig ist.

### Stop-Regel

Der Generator darf auch zu dem Ergebnis kommen:

> **Im Moment ist keine weitere Frage wertvoller als das Beschaffen der bereits identifizierten Evidenz.**

Oder:

> **Das Erkenntnisziel ist für das vorhandene Budget ausreichend erreicht.**

### Technische Kurzdefinition

> **Ein Frage-Generator ist ein epistemischer Router, der aus dem aktuellen Erkenntniszustand eine kleine Menge möglicher Frageschnitte erzeugt, deren erwarteten Erkenntnisgewinn bewertet und die nächste Untersuchung durch Auswahl einer Frage steuert.**

Und noch kürzer:

> **Nicht: Welche Fragen kann man stellen?
> Sondern: Welche Frage lohnt sich jetzt?**

Das wäre für mich im Moment der Kern.
