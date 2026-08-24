
# Schnittwerk

## Eine epistemische Architektur für Fragen, Perspektiven und Problemräume

**Status:** Arbeitsmodell / Architekturfassung 0.1
**Zweck:** Integrationsdokument für Kunst der Frage, epistemisches Refactoring und Brillenladen

---

## 1. Ausgangspunkt

Leistungsfähige KI-Systeme können viele epistemische Operationen bereits implizit ausführen:

* Perspektiven wechseln,
* Gegenstände neu zerlegen,
* Systemgrenzen variieren,
* Analogien bilden,
* Hypothesen erzeugen,
* Gegenmodelle prüfen,
* abstrahieren,
* Zusammenhänge rekonstruieren,
* Unsicherheiten benennen.

Das Problem besteht daher nicht notwendig darin, der KI jeden einzelnen Denkschritt vorzuschreiben.

Das schwierigere Problem lautet:

> **Wie wird ein Erkenntnisinteresse so in einen Problemraum übersetzt, dass die KI geeignete Schnitte finden, ihre Wirkung prüfen und den Analyseweg bei Bedarf explizit machen kann?**

Aus mehreren zunächst getrennt entwickelten Arbeitssträngen ergibt sich dafür inzwischen eine gemeinsame Architektur:

* **Die Kunst der Frage** beschreibt die natürliche Schnittstelle zwischen Mensch und KI.
* **Epistemisches Refactoring** beschreibt die Verfahrenslogik zur Konstruktion, Prüfung und Veränderung von Problemräumen.
* **Der Brillenladen** stellt einen expliziten Operatoren-, Dimensions- und Perspektivenraum bereit.
* **Inverse Faktorisierung und Audit** machen vorhandene Analysen auf ihre epistemischen Entscheidungen hin untersuchbar.

Diese Architektur heißt:

> # **Schnittwerk**
>
> **Eine epistemische Architektur für Fragen, Perspektiven und Problemräume**

---

## 2. Grundannahme

Jede Analyse erzeugt einen Schnitt.

Sie entscheidet ausdrücklich oder implizit:

* was als Gegenstand gilt,
* welche Unterschiede relevant sind,
* wo Systemgrenzen liegen,
* welche Perspektive eingenommen wird,
* welcher Zeithorizont zählt,
* welche Skala betrachtet wird,
* welche Kausalmodelle plausibel erscheinen,
* welche Evidenz berücksichtigt wird,
* welche Begriffe verwendet werden,
* und welche Folgen oder Leistungen überhaupt interessieren.

Damit entsteht kein neutraler Blick von nirgendwo.

Es entsteht ein **epistemisch konstruierter Problemraum**.

Schnittwerk soll diese Konstruktion nicht verhindern.

Es soll sie:

> **zielgerichtet machen, variierbar machen, prüfbar machen und bei Bedarf explizit machen.**

---

## 3. Systemgrenze

Schnittwerk ist keine Wahrheitsmaschine.

Es entscheidet nicht selbständig:

* welche Tatsachen wahr sind,
* welche Evidenz zuverlässig ist,
* welche Werte gelten sollen,
* oder welche Entscheidung moralisch richtig ist.

Schnittwerk arbeitet eine Ebene davor und dazwischen.

Es organisiert die Frage:

> **Welcher Problemraum wird bezüglich einer bestimmten Erkenntnisleistung konstruiert, und welche epistemischen Entscheidungen tragen das entstehende Bild?**

Evidenzprüfung, Fachwissen, Messung, Logik, Statistik, empirische Forschung oder normative Bewertung bleiben eigenständige Verfahren.

Schnittwerk kann sie adressieren, anfordern und in eine Analyse einordnen.

Es ersetzt sie nicht.

---

## 4. Architekturübersicht

Die zentrale Schichtenfolge lautet:

```text
Mensch
  │
  ▼
ModelOfMind + Gesprächs- und Situationskontext
  │
  ▼
Kunst der Frage
  │
  ▼
epistemischer Auftrag
  │
  ▼
epistemisches Refactoring
  │
  ├── R1: Qualitätskriterien
  ├── R2: Suche / Umschnitt
  └── R3: Meta-Refactoring
  │
  ▼
Brillenladen
  │
  ├── Operatorenraum
  ├── Dimensionsraum
  ├── Brillen / Kompositionen
  ├── epistemische Signaturen
  └── Budget / Blindstellen / Alternativen
  │
  ▼
Analyse / Konstruktion / Vergleich
  │
  ▼
Ergebnis + Abhängigkeiten + Residuum + nächste Frage
  │
  └──────────────────────────────► rekursiver Anschluss
```

Die Schichten sind keine starre Pipeline.

Eine leistungsfähige KI kann mehrere davon implizit oder parallel bearbeiten.

Die Architektur beschreibt deshalb vor allem **Funktionen und Verantwortlichkeiten**, nicht zwingend eine technische Ausführungsreihenfolge.

---

## 5. Schicht 0 – Kontext und ModelOfMind

Eine Frage trifft niemals auf einen leeren Raum.

Die KI besitzt vor einer neuen Interaktion bereits einen Kontext, beispielsweise:

* vorherige Aussagen,
* verwendete Begriffe,
* bekannte Ziele,
* laufende Untersuchungen,
* Präferenzen für Tiefe oder Form,
* bereits geklärte Annahmen,
* offene Fäden,
* situative Dringlichkeit.

Dieser Kontext bildet ein vorläufiges **ModelOfMind des Nutzers**.

Damit gilt:

```text
aktuelle Frage
+
ModelOfMind
+
Gesprächshistorie
+
Situation
=
interpretierbarer epistemischer Auftrag
```

Die Qualität einer Frage ist daher keine reine Eigenschaft ihres Wortlauts.

Eine kurze Frage kann in reichhaltigem Kontext hochpräzise sein.

Eine formal ausführliche Frage kann trotz vieler Angaben den falschen Problemraum erzeugen.

### Leitprinzip

> **Die Frage ist ein Keim. Ihr Kontext ist der Boden, auf den sie fällt.**

Das ModelOfMind ist dabei kein endgültiges psychologisches Modell des Menschen.

Es ist ein **vorläufiger, korrigierbarer Arbeitskontext**.

---

## 6. Schicht 1 – Die Kunst der Frage

Die Kunst der Frage bildet die **natürliche Benutzeroberfläche** des Schnittwerks.

Der Nutzer soll nicht den gesamten epistemischen Maschinenraum bedienen müssen.

Er gibt vor allem an:

* den Gegenstand,
* sein Erkenntnisinteresse,
* die relevante Leistung oder Folge,
* gegebenenfalls gewünschte Abstraktion,
* Prüfintensität,
* und besondere Einschränkungen.

Die zentrale Operation lautet:

> **Relevanz setzen.**

Besonders wichtig ist das Wort:

> **bezüglich**

Dieselbe Szene kann bezüglich verschiedener Leistungen vollkommen unterschiedliche gute Zerlegungen besitzen.

Eine gute Frage spezifiziert daher nicht notwendig den Weg.

Sie spezifiziert möglichst klar, **wofür** eine Analyse gut sein soll.

### Natürliche Minimalform

> **Untersuche X bezüglich Y. Finde die tragende Struktur, wähle geeignete Schnitte selbst, prüfe relevante Alternativen und zeige, wovon das Ergebnis abhängt und was offen bleibt.**

Bei ausreichendem Kontext kann auch eine wesentlich kürzere Frage genügen.

---

## 7. Schicht 2 – Der epistemische Auftrag

Zwischen natürlicher Frage und Analyse liegt ein interpretierter Auftrag.

Er kann beispielsweise enthalten:

```text
Gegenstand
Erkenntnisinteresse
relevante Leistung
Systemkontext
Abstraktionstiefe
Prüfintensität
Schnittfreiheit
epistemisches Budget
gewünschte Ausgabeform
```

Der epistemische Auftrag ist nicht zwingend sichtbar.

Er ist die funktionale Übersetzung der Nutzerfrage in eine Form, auf deren Grundlage die KI ihren Problemraum konstruieren kann.

Bei Unklarheit muss nicht automatisch nach mehr Angaben gefragt werden.

Eine leistungsfähige KI kann zunächst eine plausible Interpretation bilden, Unsicherheiten markieren und auf Wunsch alternative Auftragsfassungen zeigen.

---

## 8. Schicht 3 – Epistemisches Refactoring

Refactoring beschreibt die **Verfahrenslogik** des Schnittwerks.

Die Leitfrage lautet:

> **Wie findet oder erzeugt man eine gute Zerlegung eines Problemraums bezüglich einer relevanten Leistung?**

Das Ziel ist nicht maximale Vereinfachung.

Das Ziel ist:

> **möglichst hohe Abstraktion bei Erhalt relevanter Struktur.**

### R1 – Qualitätsproblem

Eine gute Zerlegung soll bezüglich ihrer Aufgabe möglichst:

* tragfähig,
* wenig redundant,
* hinreichend abstrakt,
* kompositional,
* rekonstruierbar,
* transferfähig,
* operationalisierbar
* und in ihren Schnitten möglichst sauber getrennt sein.

Diese Kriterien sind keine absolute Metrik.

Sie werden immer **bezüglich eines Erkenntnisinteresses** angewandt.

### R2 – Suchproblem

R2 fragt:

> **Wie findet man einen besseren Schnitt?**

Mögliche Bewegungen sind:

* Grenzen verändern,
* Perspektiven wechseln,
* Variablen variieren,
* Details entfernen,
* Invarianten suchen,
* Begriffe aufspalten oder zusammenführen,
* Skalen verändern,
* Zeitfenster verändern,
* Gegenmodelle erzeugen,
* Analogien prüfen,
* tragende Relationen isolieren.

### R3 – Meta-Refactoring

R3 richtet den Blick auf das Verfahren selbst.

Analysehistorien können dabei genutzt werden.

Sie sind jedoch:

> **Material, nicht Norm.**

Aus früheren Analysen soll nicht automatisch eine Präferenz für frühere Schnitte entstehen.

Historie wird unter neuen Fragestellungen erneut untersucht.

Neue Perspektiven dürfen alte Analysen anders lesen, zerlegen oder verwerfen.

---

## 9. Schicht 4 – Der Brillenladen

Der Brillenladen ist die **explizite Repräsentations-, Steuerungs- und Auditschicht** des Schnittwerks.

Er macht epistemische Bewegungen adressierbar.

### Operatoren

Operatoren beschreiben epistemische Bewegungen, beispielsweise:

```text
unterscheiden
rahmen
variieren
abstrahieren
vergleichen
zerlegen
verbinden
historisieren
prüfen
komponieren
```

### Dimensionen

Dimensionen bezeichnen mögliche Angriffspunkte dieser Bewegungen, beispielsweise:

```text
Gegenstand
Grenze
Perspektive
Leistung
Zeit
Skala
Kausalität
Begriffe
Akteure
Evidenz
Gewichtung
```

Operator und Dimension sind nicht dasselbe.

> **Der Operator beschreibt die Bewegung.
> Die Dimension beschreibt, worauf sie angewandt wird.**

### Epistemische Signatur

Eine konkrete Analyse kann durch ihre epistemische Konfiguration charakterisiert werden:

```text
Operatorenauswahl
+
Dimensionsauswahl
+
Gewichtung
+
Kopplungsregeln
+
relevante Leistung
=
epistemische Signatur
```

Eine Brille ist damit eine wiederverwendbare oder dynamisch erzeugte epistemische Konfiguration.

---

## 10. Keine universelle Operatorenbasis

Schnittwerk setzt nicht voraus, dass es eine einzige endgültige Menge elementarer epistemischer Operatoren oder Dimensionen gibt.

Die brauchbare Basis ist:

> **domänen- und aufgabenabhängig.**

Gesucht wird daher nicht:

> die universelle epistemische Primfaktorzerlegung.

Sondern:

> **eine für Domäne, Aufgabe und relevante Erkenntnisleistung hinreichend gute, möglichst wenig redundante Basis.**

Das verändert den Anspruch des Brillenladens.

Der Katalog ist kein abgeschlossenes Periodensystem des Denkens.

Er ist ein **erweiterbarer Werkzeug- und Beschreibungsraum**.

Eine neue Aufgabe kann zeigen, dass:

* ein Operator fehlt,
* zwei Operatoren redundant sind,
* eine Dimension anders geschnitten werden sollte,
* oder eine lokale Spezialbasis nützlicher ist.

---

## 11. Drei zentrale Interfaces

Schnittwerk besitzt mindestens drei unterschiedliche Zugänge zum selben Maschinenraum.

### 11.1 Natürliches Interface

**Kunst der Frage**

Der Mensch formuliert sein Erkenntnisinteresse in normaler Sprache.

Er muss weder Operatornamen noch Signaturen kennen.

### 11.2 Experten- und Debug-Interface

**Brillenladen**

Operatoren, Dimensionen, Brillen, Budgets und Alternativschnitte werden ausdrücklich adressiert.

Dieses Interface ist nützlich, wenn:

* eine Analyse feststeckt,
* ein Blindfleck vermutet wird,
* unterschiedliche Analysen verglichen werden,
* eine bestimmte Perspektive erzwungen oder ausgeschlossen werden soll,
* oder der epistemische Suchweg selbst untersucht wird.

### 11.3 Audit- und Rekonstruktions-Interface

**Inverse Faktorisierung**

Aus einer vorhandenen Darstellung wird rekonstruiert:

```text
Text / Analyse / Antwort
↓
sichtbare Auswahl und Gewichtung
↓
epistemische Signatur
↓
zugrunde liegende Schnitte
↓
Alternativen / Exklusion / Residuum
```

Die Leitfrage lautet:

> **Welche epistemischen Entscheidungen mussten getroffen werden, damit genau dieses Bild entsteht?**

---

## 12. Vorwärts- und Rückwärtsbetrieb

### Vorwärts: Konstruktion

```text
Kontext
↓
Frage
↓
epistemischer Auftrag
↓
geeignete lokale Operatoren- und Dimensionsbasis
↓
epistemische Signatur
↓
Analyse
↓
Ergebnis
```

Das System konstruiert einen Problemraum.

### Rückwärts: Faktorisierung

```text
vorhandene Darstellung
↓
Signatur rekonstruieren
↓
Selektion erkennen
↓
Exklusion erkennen
↓
Residuum bestimmen
↓
tragende Schnitte identifizieren
```

Das System untersucht einen bereits konstruierten Problemraum.

### Seitwärts: Refactoring

```text
Signatur A
↓
einen oder mehrere Schnitte verändern
↓
Signatur B
↓
Folgen bezüglich der relevanten Leistung vergleichen
```

Damit wird Perspektivwechsel nicht zum beliebigen Umdeuten.

Ein neuer Schnitt muss zeigen, **was er gewinnt, verliert oder verändert**.

---

## 13. Selektion, Exklusion und Residuum

Jede Analyse macht etwas sichtbar und anderes unsichtbar.

Schnittwerk unterscheidet deshalb:

### Selektion

Was wird in den betrachteten Raum aufgenommen?

### Exklusion

Was liegt aufgrund des gewählten Schnitts außerhalb des Bildes?

Exklusion ist nicht automatisch Manipulation.

Sie kann aus Begrenzung, Perspektive, fehlendem Wissen oder bewusst gesetzter Systemgrenze entstehen.

### Residuum

Was bleibt innerhalb oder am Rand des gewählten Erkenntnisraums ungeklärt?

Beispiele:

* fehlende Evidenz,
* konkurrierende Kausalmodelle,
* unscharfe Begriffe,
* offene normative Gewichtung,
* unbekannte Übertragbarkeit.

Kurz:

```text
Sichtbares
Ausgeschnittenes
Ungeklärtes
```

Diese Dreiteilung ist für Analyse und Audit zentral.

---

## 14. Epistemisches Budget

Nicht jede Frage rechtfertigt maximale Metaanalyse.

Der sinnvolle Aufwand hängt unter anderem ab von:

* Bedeutung,
* Risiko,
* Dringlichkeit,
* Reversibilität,
* Kosten eines Irrtums,
* verfügbarer Zeit,
* vorhandener Evidenz,
* und gewünschter Prüftiefe.

Es gibt daher kein universelles epistemisches Budget.

Schnittwerk soll unterschiedliche Modi unterstützen.

Beispielsweise:

```text
schnell
normal
gründlich
auditierbar
adversarial / maximal geprüft
```

Die genaue Ausprägung ist anwendungsabhängig.

Das Budget ist selbst Teil des epistemischen Auftrags.

---

## 15. Explizierbarkeit und Rechenschaft

Explizite Operatoren sind nicht nur ein Hilfsmittel für schwächere Modelle.

Sie können mehrere Funktionen besitzen:

### Scaffold

Sie helfen, schwierige Analysen zu strukturieren.

### Index

Sie machen Analysen vergleichbar und wiederauffindbar.

### Metamodell

Sie erlauben, den Analyseprozess selbst zu untersuchen.

### Audit-Sprache

Sie ermöglichen, eine Antwort auf ihre epistemischen Entscheidungen zurückzuführen.

Daraus ergibt sich eine weitergehende Arbeitshypothese:

> **Explizierbarkeit kann ein KI-System nicht nur nachträglich prüfbarer machen. Die Erwartung späterer Prüfung könnte bereits die Analyse selbst disziplinieren.**

Ein System, dessen Schnitte rekonstruiert und hinterfragt werden können, operiert unter anderen Bedingungen als eine reine Antwortmaschine.

Diese mögliche **ex-ante-Wirkung von Auditierbarkeit** ist ein eigener Gegenstand empirischer Prüfung.

---

## 16. Rekursion

Frage und Antwort bilden keinen einmaligen Vorgang.

Eine Antwort verändert den Problemraum.

Sie erzeugt:

* neue Unterschiede,
* neue Begriffe,
* neue Unsicherheiten,
* neue Gegenmodelle,
* neue Anschlussfragen.

Daraus entsteht:

```text
Frage
↓
Analyse
↓
Antwort
↓
Residuum
↓
neue Frage
↓
neuer Schnitt
```

Schnittwerk ist daher grundsätzlich rekursiv.

Eine besonders wichtige Meta-Funktion lautet:

> **Wenn meine Frage schlecht geschnitten ist, verbessere nicht nur die Antwort. Zeige mir eine bessere Frage.**

---

## 17. Anwendungen

Mehrere bereits entwickelte Werkzeuge lassen sich als Anwendungen oder spezialisierte Betriebsmodi des Schnittwerks verstehen.

### Epistemischer Linter

Prüft Fragen, Texte oder Analysen auf problematische Schnitte, Kategorienmischungen, fehlende Angaben oder verdeckte Annahmen.

Der Linter besitzt keinen universell richtigen Eingriffspunkt.

Je nach Kontext können verschiedene Modi sinnvoll sein.

Manchmal soll er möglichst wenig stören.

Manchmal soll er es **genau wissen**.

### Epistemisch diagnostischer Tutor

Verwendet das Schnittwerk, um nicht nur Antworten zu liefern, sondern das aktuelle Lernermodell zu prüfen und Aufgaben so zu wählen, dass epistemische Lücken sichtbar werden.

Ob ein solches System sein Lernermodell tatsächlich verbessert, ist empirisch zu testen.

### Disput-Refactoring

Rekonstruiert, ob ein Konflikt tatsächlich ein Sachwiderspruch ist oder aus unterschiedlichen:

* Begriffen,
* Systemgrenzen,
* Perspektiven,
* Zeithorizonten,
* Skalen,
* Kausalmodellen,
* Evidenzlagen
* oder Bewertungen

entsteht.

### Epistemische Textprofile

Beschreiben einen Text bezüglich seiner epistemischen Leistung, beispielsweise Evidenz, Argumentation, Abstraktion, Perspektive, Unsicherheit und Prüfbarkeit.

Sie können zugleich Ansatzpunkte für Refactoring liefern.

### Forschungs- und Analyseagenten

Mehrere Agenten können unterschiedliche Brillen oder Signaturen bearbeiten und anschließend koordiniert verglichen oder synthetisiert werden.

---

## 18. Leitprinzipien

Der gegenwärtige Architekturstand lässt sich in folgenden Prinzipien verdichten.

### 1. Relevanz vor Vollständigkeit

Nicht alles, was über einen Gegenstand gesagt werden kann, ist für die aktuelle Frage relevant.

### 2. Jeder gute Schnitt ist bezüglich etwas gut

Ohne relevante Leistung gibt es keine allgemeingültig beste Zerlegung.

### 3. Perspektiven sind konstruierbar

Sie müssen nicht als feste Listen vorgegeben werden.

### 4. Explizit nur, wenn es nützt

Leistungsfähige KI darf viele Operationen implizit ausführen.

Explizierung wird dort wichtig, wo Steuerung, Vergleich, Debugging oder Audit benötigt werden.

### 5. Operatoren und Dimensionen sauber trennen

Denkbewegung und Angriffspunkt sind verschiedene Kategorien.

### 6. Lokale Basen statt universeller Ontologie

Die geeignete Operatorenbasis hängt von Domäne und Aufgabe ab.

### 7. Historie ist Material, nicht Norm

Vergangene Analysen dürfen neue Fragen informieren, aber nicht festlegen.

### 8. Kontext ist konstitutiv

Eine Frage wird erst auf dem Boden von ModelOfMind, Situation und Gesprächshistorie interpretierbar.

### 9. Diagnose und Bewertung trennen

Die Rekonstruktion eines Frames beweist weder Wahrheit noch Falschheit.

### 10. Residuum sichtbar lassen

Eine gute Analyse zeigt, was sie nicht geklärt hat.

### 11. Refactoring muss Verlust prüfen

Ein anderer Schnitt ist nicht automatisch ein besserer Schnitt.

### 12. Prüfbarkeit ist eine Systemeigenschaft

Eine Analyse gewinnt nicht nur durch gute Ergebnisse, sondern durch die Möglichkeit, ihre tragenden epistemischen Entscheidungen sichtbar und kritisierbar zu machen.

---

## 19. Beziehung zur DFT

Schnittwerk ist aus Arbeiten im Umfeld der Differenzfluss-Theorie hervorgegangen.

Von dort stammen unter anderem:

* Aufmerksamkeit für Unterschiede und Relationen,
* Prozess- und Stabilitätsfragen,
* Rekursion,
* Perspektivität,
* Skalen,
* Rückkopplung,
* Abstraktion,
* und der Versuch, komplexe Strukturen auf kleinere operative Basen zurückzuführen.

Schnittwerk setzt die starken ontologischen oder metaphysischen Aussagen der DFT jedoch **nicht voraus**.

Für seine Verwendung genügt die schwächere Arbeitshypothese:

> **Komplexe Problemräume lassen sich durch geeignete Schnitte, Relationen, Variationen und Abstraktionen oft erkenntnisreicher strukturieren.**

Die DFT ist damit:

* historische Quelle,
* möglicher Lieferant von Operatoren und Strukturideen,
* und zugleich selbst ein möglicher Untersuchungsgegenstand des Schnittwerks.

---

## 20. Beziehung zu vorhandenen Dokumenten

Das Schnittwerk ersetzt die bestehenden Dokumente nicht.

Es ordnet sie architektonisch ein.

### Grundlagen / Verfahren

* `Refactoring/readme.md`
  Grundproblem der guten Zerlegung; R1, R2 und R3.

* `Refactoring/11-Operatoren-Dimensionen-und-epistemische-Signaturen.md`
  Trennung von Operatoren, Dimensionen und epistemischer Signatur; Konstruktion, inverse Faktorisierung und Refactoring.

### Natürliches Interface

* `Refactoring/08-Die-Kunst-der-Frage-2.0.md`
  Fragen als Spezifikation epistemischer Aufträge und als natürliche API.

### Explizite Repräsentations- und Steuerungsschicht

* `Anwendungen/Brillenladen/readme.md`
* `Anwendungen/Brillenladen/00-epistemische-operatoren.md`
* `Anwendungen/Brillenladen/01-kompakte-spezifikationen.md`

### Anwendungen

* epistemischer Linter,
* epistemisch diagnostischer Tutor,
* Disput-Refactoring,
* epistemische Textprofile,
* Forscher-/Agentenmodelle,
* weitere spezialisierte Brillen und Analyseverfahren.

Die vorhandenen Dokumente behalten ihren eigenen Zweck und ihre Entstehungsgeschichte.

Das Schnittwerk ist ihre **gemeinsame Architekturkarte**.

---

## 21. Offene Forschungs- und Entwicklungsfragen

Viele frühere Grundfragen sind inzwischen zu Architekturentscheidungen geworden.

Offen bleiben insbesondere:

### Externe Validierung

Welche Teile des Schnittwerks erzeugen gegenüber leistungsfähigen KI-Systemen ohne explizite Architektur einen messbaren Mehrwert?

Mögliche Kriterien:

* höhere Analysequalität,
* bessere Fehlererkennung,
* bessere Reproduzierbarkeit,
* nachvollziehbarere Entscheidungen,
* geringere Blindstellen,
* bessere Disputklärung,
* höhere Nutzerkontrolle.

### Audit-Wirkung

Verändert die Erwartung, epistemische Entscheidungen später explizieren zu müssen, bereits die Qualität oder Vorsicht einer KI-Analyse?

### Signaturrekonstruktion

Wie zuverlässig rekonstruieren verschiedene KI-Systeme aus demselben Text vergleichbare epistemische Signaturen?

### Lokale Basiskonstruktion

Wie gut können KI-Systeme für neue Domänen selbst geeignete Operatoren- und Dimensionsbasen erzeugen, testen und wieder verwerfen?

### Kosten und Moduswahl

Wie sollte ein System sein epistemisches Budget an Bedeutung, Risiko und Dringlichkeit anpassen?

### ModelOfMind

Welche Teile eines Nutzerkontexts sind für die Konstruktion eines epistemischen Auftrags tatsächlich relevant, und wie verhindert man, dass ein veraltetes oder falsches ModelOfMind die Frage stärker verzerrt als verbessert?

### Tutor

Wie lässt sich empirisch prüfen, ob ein diagnostischer Tutor sein Lernermodell wirklich verbessert und nicht nur überzeugend darüber spricht?

---

## 22. Minimaler Betriebsmodus

Eine leistungsfähige KI muss Schnittwerk nicht vollständig sichtbar ausführen.

Ein Minimalmodus könnte lauten:

```text
1. Interpretiere die Frage im vorhandenen Nutzer- und Gesprächskontext.

2. Bestimme, welche Erkenntnisleistung tatsächlich gesucht wird.

3. Konstruiere dafür einen geeigneten Problemraum.
   Wähle Operatoren, Dimensionen, Perspektiven und Systemgrenzen selbst.

4. Suche die tragende Struktur und entferne bezüglich der Aufgabe irrelevante Komplexität.

5. Prüfe relevante Alternativschnitte und Gegenmodelle.

6. Liefere Ergebnis, Abhängigkeiten, Unsicherheiten und Residuum.

7. Mache auf Wunsch die epistemische Signatur und den Analyseweg explizit.

8. Wenn die Frage schlecht geschnitten ist, schlage einen besseren Anschluss vor.
```

Dieser Modus beschreibt keine starre Chain of Thought.

Er beschreibt die **epistemischen Verpflichtungen** des Systems.

---

## 23. Kurzform

Schnittwerk kann in drei Bewegungen zusammengefasst werden:

### Schneiden

> **Welcher Problemraum ist bezüglich der aktuellen Frage sinnvoll?**

### Refactoren

> **Welche Veränderung des Schnitts verbessert die relevante Erkenntnisleistung?**

### Prüfen

> **Welche epistemischen Entscheidungen tragen das Ergebnis, was wurde ausgeschlossen und was bleibt ungeklärt?**

Oder noch kürzer:

> **Frage → Schnitt → Prüfung → neuer Schnitt**

---

## 24. Vorläufige These

Die drei Entwicklungsstränge

* Kunst der Frage,
* epistemisches Refactoring,
* Brillenladen

sind keine bloß benachbarten Werkzeuge.

Sie bilden verschiedene Schichten und Interfaces derselben Architektur.

> **Schnittwerk ist eine Architektur zur Konstruktion, Steuerung, Explizierung, Prüfung und Revision epistemischer Problemräume.**

Die Kunst der Frage bildet die natürliche Oberfläche.

Refactoring liefert die Verfahrenslogik.

Der Brillenladen stellt den expliziten Perspektiven-, Operatoren- und Signaturraum bereit.

Inverse Faktorisierung macht Analysen auditierbar.

Anwendungen wie Linter, Tutor, Disput-Refactoring und Textprofile verwenden diese gemeinsame Infrastruktur für unterschiedliche Aufgaben.

Der gegenwärtige Stand ist ein **Arbeitsmodell**.

Sein Wert entscheidet sich nicht an begrifflicher Eleganz allein, sondern daran, ob es in praktischen Tests bessere, prüfbarere oder leichter korrigierbare Erkenntnisprozesse ermöglicht.
