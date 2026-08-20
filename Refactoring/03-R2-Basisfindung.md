# R2 – Wie findet man eine gute Zerlegung?

## Status

Nachfolgedokument zu:

- `01-R1-gute-Zerlegung.md`
- `02-R1-Belastungstest-Mathematik.md`

R1 formuliert Qualitätskriterien für gute Zerlegungen.

R2 untersucht nun die Suchfrage:

> **Wie findet man eine solche Zerlegung, wenn man sie noch nicht kennt?**

Die hier beschriebene Methode ist zunächst **substratneutral**.

Sie kann von Menschen, von KI-Systemen oder interaktiv von beiden angewendet werden.

Die Unterschiede liegen vor allem in der Operationalisierung:

- Menschen arbeiten mit wenigen starken Fragen, Erfahrung, Relevanzgefühl und Kontextverständnis.
- KI-Systeme können große Variantenräume durchsuchen, viele Hypothesen parallel vergleichen und Suchverläufe systematisch speichern.
- In der Kombination können beide Stärken zusammenwirken.

---

# 1. Ausgangspunkt

Eine gute Zerlegung entsteht nicht dadurch, dass ein komplexes System einfach vollständig beschrieben wird.

Gesucht wird ein Strukturskelett:

> **möglichst abstrakt, funktional wenig redundant und hinreichend leistungsfähig, um eine relevante Leistung zu erkennen, zu erklären oder zu generieren.**

R2 muss deshalb nicht unmittelbar „die richtige Basis“ erkennen.

Es genügt zunächst, wenn das Verfahren:

1. plausible Zerlegungskandidaten erzeugt,
2. sie systematisch verändert,
3. ihre Invarianten untersucht,
4. sie anhand der Kriterien aus R1 prüft,
5. und aus Fehlern neue Suchrichtungen gewinnt.

Damit entsteht ein iterativer Prozess:

```text
Kandidaten erzeugen
↓
variieren
↓
abstrahieren
↓
prüfen
↓
refactoren
↓
erneut prüfen
```

R2 ist damit kein einmaliger Schnitt.

Es ist ein Suchprozess im Raum möglicher Zerlegungen.

---

# 2. Grundprinzip

Die vorläufige Kurzform von R2 lautet:

> **Schneiden → Variieren → Invarianten suchen → Abstrahieren → Refactoren → Prüfen**

Etwas ausführlicher:

```text
Fragestellung
↓
relevante Leistung
↓
Gegenstandsschnitt
↓
Strukturkandidaten erzeugen
↓
Variationen durchführen
↓
leistungsrelevante Invarianten bestimmen
↓
leistungsneutrale Details entfernen
↓
Kandidatenbasis refactoren
↓
mit R1 prüfen
↓
Residuum analysieren
↓
weiter suchen oder abbrechen
```

Der Prozess enthält drei unterschiedliche Klassen von Operationen:

1. **Suchoperatoren**
2. **Refactoringoperatoren**
3. **Prüfoperatoren**

Diese Unterscheidung ist wichtig.

Nicht jeder Operator soll dasselbe leisten.

---

# 3. Schritt 0 – Die Frage setzt den Kontext

Vor jeder Zerlegung muss geklärt werden:

> **Bezüglich welcher Leistung wird zerlegt?**

Dies ist kein Nebenschritt.

Die Fragestellung bestimmt, welche Unterschiede relevant werden.

Dasselbe System kann bezüglich verschiedener Leistungen unterschiedliche gute Zerlegungen besitzen.

Beispiele:

Ein Motor kann untersucht werden bezüglich:

- Kraftübertragung,
- Wärmefluss,
- Regelung,
- Fehlerdiagnose,
- Fertigung.

Ein soziales System kann untersucht werden bezüglich:

- Stabilität,
- Entscheidungsfähigkeit,
- Informationsfluss,
- Machtverteilung,
- Konfliktdynamik.

Daraus folgt:

> **Die Frage ist selbst bereits ein Schnittoperator.**

Sie setzt:

- Kontext,
- Relevanz,
- Maßstab,
- und damit auch die zulässige Abstraktion.

---

# 4. Schritt 1 – Gegenstandsschnitt

Komplexe Problemräume sind häufig zu groß oder zu unscharf, um direkt zerlegt zu werden.

Deshalb wird zunächst ein bearbeitbarer Ausschnitt konstruiert.

Fragen dafür sind beispielsweise:

> Was genau gehört zum untersuchten System?

> Wo beginnt und endet der relevante Ausschnitt?

> Welche Folge oder Leistung interessiert?

> Welcher Zeitraum ist relevant?

> Welche Perspektive wird zunächst eingenommen?

> Welche Aspekte können vorläufig ausgeblendet werden?

Der Gegenstandsschnitt ist vorläufig.

Er darf später verändert werden.

Ein schlechter Schnitt zeigt sich häufig daran, dass:

- zu viele unabhängige Phänomene vermischt werden,
- keine klare relevante Leistung formulierbar ist,
- scheinbare Widersprüche lediglich aus vermischten Ebenen entstehen,
- oder zentrale Einflüsse systematisch außerhalb der gesetzten Grenze liegen.

---

# 5. Schritt 2 – Suchoperatoren

Suchoperatoren erzeugen alternative Schnitte oder Strukturhypothesen.

Sie behaupten nicht, dass die Welt aus diesen Kategorien bestehen müsse.

Sie lauten vielmehr:

> **Versuche, den Gegenstand einmal entlang dieser Achse zu betrachten.**

Damit sind sie heuristische Kandidatengeneratoren.

Ein möglicher Startvorrat ist:

## Relation

> Welche Elemente sind nur durch ihre Beziehungen relevant?

## Zustand / Übergang

> Was ist Zustand, was Veränderung?

## Zeit

> Welche Struktur wird erst im Verlauf sichtbar?

## Grenze

> Was ändert sich, wenn die Systemgrenze verschoben wird?

## Perspektive

> Welche Strukturen hängen vom Beobachter oder Standpunkt ab?

## Skala

> Was bleibt beim Hinein- oder Herauszoomen erhalten?

## Kausalität

> Welche Veränderung verändert welche relevante Folge?

## Rückkopplung

> Welche Folgen verändern ihre eigenen Bedingungen?

## Information

> Welche Unterschiede entstehen durch verschiedene Informationsstände?

## Kontext

> Welche Beziehungen gelten nur unter bestimmten Randbedingungen?

## Variation

> Was kann verändert werden, ohne dass die relevante Leistung verloren geht?

## Gegenhypothese

> Welche alternative Struktur könnte dieselben Beobachtungen erklären?

## Wiederholung / Muster

> Welche relationale Form tritt in verschiedenen Fällen erneut auf?

## Abhängigkeit

> Welche Elemente können nicht unabhängig verändert werden?

## Komposition

> Welche komplexen Leistungen entstehen erst aus dem Zusammenwirken einfacherer Teile?

Diese Liste ist keine endgültige Operatorenbasis.

Sie ist ein **Seed für die Suche**.

Ein gutes Verfahren muss auch feststellen können:

> Dieser Operator bringt hier keinen zusätzlichen Erkenntnisgewinn.

Oder:

> Für dieses Problem fehlt offenbar eine bisher nicht vorhandene Achse.

---

# 6. Variation als zentraler Suchoperator

Der mathematische Belastungstest von R1 legt nahe, Variation besonders hervorzuheben.

Die Leitfrage lautet:

> **Welche Veränderungen darf ich am Gegenstand vornehmen, ohne dass sich die relevante Leistung wesentlich ändert?**

Damit entsteht das Muster:

```text
Strukturkandidat
↓
gezielte Variation
↓
relevante Leistung beobachten
↓
leistungsneutrale Veränderungen identifizieren
↓
Invarianten isolieren
```

Die Invarianten sind Kandidaten für das Strukturskelett.

Dies ersetzt die direkte Frage nach einem vermeintlichen „Wesen“ durch eine operationalisierbare Suche:

> Nicht fragen, was wesentlich ist.

> Verändern und beobachten, was nicht verschwinden darf.

Kurz:

> **Variation → Invarianz → Skelett**

---

# 7. Schritt 3 – Abstraktion

Nach den Variationen wird versucht, alles zu entfernen, was bezüglich der relevanten Leistung nicht trägt.

Fragen dafür:

> Welche Eigenschaften können variieren?

> Welche Unterschiede verändern die relevante Leistung nicht?

> Welche konkreten Darstellungen sind austauschbar?

> Welche Elemente besitzen dieselbe funktionale Rolle?

> Welche Einzelheiten sind nur historische oder materielle Ausprägung?

Abstraktion ist dabei kein Selbstzweck.

Sie steht unter der Nebenbedingung:

> **Die relevante Leistung muss erhalten bleiben.**

Der Informationsverlust ist gewollt.

Verloren gehen soll das, was bezüglich der Frage nicht benötigt wird.

---

# 8. Schritt 4 – Refactoringoperatoren

Suchoperatoren erzeugen Kandidaten.

Refactoringoperatoren verändern deren innere Struktur.

Sie entsprechen teilweise bekannten Bewegungen aus der Softwareentwicklung.

## REMOVE

> Kann ein Element entfernt werden, ohne relevante Leistung zu verlieren?

## SPLIT

> Enthält ein Element mehrere funktional unterschiedliche Rollen?

Dann kann eine Aufspaltung sinnvoll sein.

## MERGE

> Leisten mehrere Elemente funktional dasselbe?

Dann können sie Kandidaten für eine gemeinsame abstraktere Struktur sein.

## REPLACE

> Kann ein Element vollständig durch eine Kombination anderer Elemente ersetzt werden?

Dann ist es möglicherweise abgeleitet.

## EXTRACT

> Wiederholt sich dasselbe Relationsmuster an mehreren Stellen?

Dann kann es als eigene Struktur herausgezogen werden.

## COMPOSE

> Welche komplexen Leistungen entstehen aus der Kombination einfacherer Elemente?

## GENERALIZE

> Welche konkrete Eigenschaft kann durch eine allgemeinere relationale Form ersetzt werden?

## SPECIALIZE

> Ist eine Abstraktion so weit gefasst, dass relevante Unterschiede verschwinden?

Dann muss sie gezielt wieder differenziert werden.

## REFRAME

> Ist die aktuelle Fragestellung oder Systemgrenze selbst ungünstig gewählt?

Dann kann ein neuer Schnitt nötig sein.

Diese Operationen erzeugen alternative Kandidatenbasen.

---

# 9. Schritt 5 – Prüfung mit R1

Jede Kandidatenbasis wird anschließend gegen die Kriterien aus R1 geprüft.

Fragen sind unter anderem:

## Relevante Leistung

> Ist klar, welche Leistung erhalten werden soll?

## Abstraktion

> Enthält die Basis noch konkrete Details, die entfernt werden können?

## Strukturerhalt

> Bleibt die relevante Leistung erhalten?

## Minimalität

> Ist ein Element entfernbar?

## Funktionale Redundanz

> Leisten mehrere Elemente im Wesentlichen dasselbe?

## Kompositionalität

> Lassen sich die Teile sinnvoll kombinieren?

## Rekonstruktionskraft

> Kann die relevante Leistung aus der Basis wieder hervorgebracht werden?

## Transferfähigkeit

> Funktioniert die Struktur auch in anderen Fällen?

## Operationalisierbarkeit

> Kann mit der Basis tatsächlich gearbeitet werden?

## Strukturelle Ökonomie

> Ist die Komplexität sichtbar verteilt oder nur in scheinbar einfachen Grundbegriffen versteckt?

Damit übernimmt R1 die Rolle einer **Fitnessfunktion** für R2.

R2 erzeugt und verändert.

R1 bewertet.

---

# 10. Erkennen, Erklären und Generieren als Teststufen

Eine Kandidatenbasis kann auf drei Ebenen geprüft werden.

## Erkennen

> Kann die Basis relevante Fälle zuverlässig identifizieren?

## Erklären

> Kann sie zeigen, welche Teile und Relationen für die Leistung verantwortlich sind?

## Generieren

> Kann sie die relevante Leistung wieder hervorbringen?

Generativität kann dabei verschiedene Formen besitzen:

### rekonstruktiv

Bekannte relevante Leistungen werden reproduziert.

### deduktiv

Aus der Basis folgen neue Konsequenzen.

### konstruktiv

Aus der Basis können neue Instanzen oder Konfigurationen erzeugt werden.

Je höher die erreichte Stufe, desto stärker ist die Evidenz dafür, dass die Zerlegung tragende Struktur erfasst.

---

# 11. Das Residuum als Suchsignal

Ein unvollständiges Modell ist nicht nur ein Fehlschlag.

Sein Rest kann eine Suchrichtung liefern.

Nach jeder Prüfung wird deshalb gefragt:

> Was erklärt die aktuelle Basis gut?

> Was bleibt unerklärt?

> Wo verliert sie relevante Leistung?

> Welche Fälle passen nicht?

> Welche Unterschiede musste man als Sonderfall ergänzen?

> Welche Beobachtung widerspricht der aktuellen Zerlegung?

Das Unerklärte bildet ein **Residuum**.

Dieses Residuum kann anzeigen:

- einen fehlenden Operator,
- einen falschen Schnitt,
- eine zu grobe Abstraktion,
- eine versteckte Variable,
- eine falsche Systemgrenze,
- eine übersehene Perspektive,
- oder eine funktionale Vermischung.

Schema:

```text
Basis B
↓
Test
↓
Residuum R
↓
neuer Schnitt / neue Variation
↓
veränderte Basis B'
```

Damit wird Scheitern selbst Teil des Suchverfahrens.

---

# 12. Suchbudget und Stop-Regel

Mehr Differenzierung erzeugt nicht automatisch mehr Erkenntnis.

Ein Verfahren, das immer weitere Details hinzufügt, nähert sich lediglich einer vollständigen Beschreibung des Gegenstands.

Das widerspricht dem Ziel der Abstraktion.

Deshalb braucht R2 ein Suchbudget.

Die Leitregel lautet:

> **Füge nur dann zusätzliche Struktur hinzu, wenn der erwartete Gewinn an relevanter Leistung den zusätzlichen Komplexitätsaufwand rechtfertigt.**

Ein Suchprozess kann beendet werden, wenn:

- relevante Leistung hinreichend erhalten ist,
- weitere Variationen keine neuen tragenden Invarianten liefern,
- zusätzliche Operatoren nur noch geringe Verbesserungen erzeugen,
- verbleibende Residuen außerhalb des gesetzten Kontexts liegen,
- oder die Kosten weiterer Suche den erwarteten Erkenntnisgewinn übersteigen.

Damit entsteht eine pragmatische Stop-Regel.

---

# 13. Vorläufiger R2-Algorithmus

```text
0. FRAGE
   Welche relevante Leistung interessiert?

1. SCHNITT
   Einen bearbeitbaren Gegenstand bestimmen.

2. EXPLORE
   Mit allgemeinen Suchoperatoren alternative Schnitte erzeugen.

3. VARIIEREN
   Elemente, Relationen, Grenzen, Perspektiven, Skalen und Bedingungen verändern.

4. INVARIANTEN FINDEN
   Was bleibt bezüglich der relevanten Leistung erhalten?

5. ABSTRAHIEREN
   Leistungsneutrale Details entfernen.

6. REFACTOR
   Elemente entfernen, splitten, mergen, ersetzen, extrahieren oder neu komponieren.

7. TESTEN
   Kandidaten mit den Kriterien aus R1 prüfen.

8. RESIDUUM ANALYSIEREN
   Was erklärt oder erzeugt die Basis noch nicht?

9. ERWEITERN ODER ABBRECHEN
   Nur weiter differenzieren, wenn zusätzlicher Erkenntnisgewinn zu erwarten ist.
```

Der Prozess ist rekursiv.

Jeder Durchlauf kann:

- die Basis verändern,
- den Gegenstandsschnitt verändern,
- die Fragestellung präzisieren,
- oder neue Suchoperatoren erforderlich machen.

---

# 14. Drei Operatorenklassen

Die bisherige Unterscheidung lässt sich zusammenfassen.

## A. Suchoperatoren

Sie erzeugen alternative Sichtweisen oder Strukturhypothesen.

Beispiele:

- Perspektive
- Skala
- Grenze
- Zeit
- Relation
- Variation
- Gegenhypothese
- Rückkopplung
- Information

## B. Refactoringoperatoren

Sie verändern eine bestehende Kandidatenbasis.

Beispiele:

- Remove
- Split
- Merge
- Replace
- Extract
- Compose
- Generalize
- Specialize
- Reframe

## C. Prüfoperatoren

Sie beurteilen die Qualität einer Kandidatenbasis.

Beispiele:

- Entfernungstest
- Ersetzungstest
- Variationstest
- Rekonstruktionstest
- Transfertest
- Redundanztest
- Kompositionstest

Diese funktionale Trennung kann verhindern, dass ein einziger unscharfer „Operatoren“-Begriff zu viele verschiedene Aufgaben übernimmt.

---

# 15. Mensch und KI

Die Grundmethode ist für Mensch und KI dieselbe.

Die praktische Ausführung unterscheidet sich jedoch erheblich.

---

## 15.1 Menschliches Refactoring

Menschen besitzen besondere Stärken bei:

- Relevanzgefühl,
- Kontextverständnis,
- implizitem Erfahrungswissen,
- ungewöhnlichen Analogien,
- Bewertung dessen, was überhaupt interessant ist,
- intuitiver Erkennung schlecht gestellter Fragen,
- normativen und praktischen Zielsetzungen.

Gleichzeitig bestehen Grenzen:

- begrenztes Arbeitsgedächtnis,
- geringe Zahl parallel verfolgbarer Varianten,
- unvollständige Protokollierung verworfener Wege,
- kognitive Verzerrungen,
- Bindung an vertraute Begriffe und Modelle.

Für Menschen sollte R2 deshalb vor allem als **kleiner Satz starker Fragen** operationalisiert werden.

Zum Beispiel:

> Was genau soll erhalten bleiben?

> Was kann ich verändern, ohne dass es verloren geht?

> Was bleibt dabei invariant?

> Welche zwei Dinge leisten möglicherweise dasselbe?

> Welcher Begriff enthält möglicherweise mehrere Funktionen?

> Was fehlt noch, damit ich die relevante Leistung erklären oder erzeugen kann?

> Welche andere Perspektive würde meine derzeitige Zerlegung sichtbar beschädigen?

Damit wird Refactoring zu einem Denkwerkzeug.

---

## 15.2 KI-Refactoring

KI-Systeme können dieselben Operationen in größerer Breite und Parallelität durchführen.

Eine KI kann beispielsweise:

- viele alternative Schnitte erzeugen,
- mehrere Suchoperatoren kombinieren,
- Varianten systematisch durchspielen,
- Kandidatenbasen gegeneinander bewerten,
- Suchbäume speichern,
- Entfernungstests wiederholen,
- Redundanzen statistisch oder semantisch suchen,
- erfolgreiche Strukturen über verschiedene Domänen hinweg vergleichen,
- Residuen sammeln und gruppieren.

Dadurch wird aus einer Denkheuristik ein möglicher:

> **Suchalgorithmus im Konzeptraum**

Beispielsweise kann eine KI Kombinationen untersuchen wie:

```text
Perspektive × Skala × Grenze × Zeitfenster × Gegenhypothese
```

und anschließend prüfen, welche Kombinationen tatsächlich neue relevante Struktur sichtbar machen.

---

# 16. Namenlose Strukturen

Menschen arbeiten stark mit Begriffen.

KI-Systeme müssen dagegen nicht zwingend zuerst einen sprachlichen Begriff besitzen.

Wenn ein Begriff als:

> **menschliches Interface für ein komprimiertes Relationsmuster**

verstanden wird, kann ein KI-System zunächst strukturell arbeiten.

Es könnte beispielsweise feststellen:

> Ein bestimmtes Relationsmuster tritt in sehr unterschiedlichen Fällen wiederholt auf und besitzt dort dieselbe funktionale Rolle.

Erst danach wäre zu fragen:

> Gibt es dafür bereits einen menschlichen Begriff?

> Ist ein neuer Begriff hilfreich?

> Oder genügt die interne Strukturrepräsentation?

Damit eröffnet KI die Möglichkeit, nach tragenden Strukturen zu suchen, bevor eine passende menschliche Benennung existiert.

Dies könnte insbesondere bei hochdimensionalen oder domänenübergreifenden Mustern relevant werden.

---

# 17. Interaktives Refactoring

Eine besonders interessante Form ist die Zusammenarbeit von Mensch und KI.

Der Mensch kann:

- Fragestellung setzen,
- relevante Leistung bestimmen,
- Kontext korrigieren,
- ungewöhnliche Ergebnisse bewerten,
- normative Relevanz festlegen.

Die KI kann:

- Suchraum verbreitern,
- Varianten erzeugen,
- Operatoren kombinieren,
- Kandidaten vergleichen,
- Residuen sammeln,
- Suchhistorien protokollieren.

Ein möglicher Zyklus lautet:

```text
Mensch:
Frage + Relevanz

↓
KI:
Varianten + Schnitte + Kandidaten

↓
gemeinsam:
Prüfung

↓
Mensch:
Kontextkorrektur / Relevanzentscheidung

↓
KI:
erneute Suche
```

Das Ziel ist nicht:

> KI denkt anstelle des Menschen.

Sondern:

> **Der Mensch setzt und korrigiert Relevanz; die KI verbreitert und systematisiert die Suche.**

---

# 18. Die Rolle der DFT

Die DFT ist für R2 zunächst keine notwendige Ontologie.

Sie kann jedoch einen Startvorrat allgemeiner Strukturachsen liefern.

Die schwache und testbare Hypothese lautet:

> **Eine kleine Menge allgemeiner Strukturachsen kann die Suche nach guten Zerlegungen in vielen Problemräumen systematisch verbessern.**

Diese Achsen wären keine Wahrheiten über die fundamentale Konstruktion der Welt.

Sie wären:

> **heuristische Suchoperatoren**

Ihre Qualität bemisst sich daran, ob sie:

- relevante Strukturen sichtbar machen,
- gute Zerlegungen schneller finden,
- Residuen reduzieren,
- Transfer zwischen Domänen ermöglichen,
- und generative Modelle verbessern.

Ein Operator, der wiederholt keinen zusätzlichen Erkenntnisgewinn liefert, sollte herabgestuft oder entfernt werden.

Ein wiederkehrendes Residuum kann einen neuen Operator nahelegen.

Damit führt R2 unmittelbar zu R3.

---

# 19. Vorläufige Antwort auf R2

> **Eine gute Zerlegung lässt sich durch einen iterativen Suchprozess finden, der eine relevante Leistung bestimmt, alternative Schnitte erzeugt, gezielte Variationen durchführt, leistungsbezogene Invarianten isoliert, redundante oder irrelevante Struktur entfernt, Kandidatenbasen refactort und sie anhand der R1-Kriterien prüft.**

Der Kernprozess lautet:

> **Frage → Schnitt → Variation → Invarianz → Abstraktion → Refactoring → Prüfung → Residuum**

Suchoperatoren erzeugen Kandidaten.

Refactoringoperatoren verändern Kandidaten.

Prüfoperatoren bewerten Kandidaten.

Der Prozess kann von Menschen und KI gleichermaßen angewendet werden, wobei sich ihre praktischen Stärken und Suchkapazitäten unterscheiden.

---

# 20. Übergang zu R3

R2 setzt zunächst einen verfügbaren Vorrat an Suchoperatoren voraus.

Damit entsteht die nächste Frage:

> **Wie gut ist dieser Operatorenvorrat selbst?**

Und weiter:

> **Kann ein Refactoring-Verfahren aus erfolgreichen und gescheiterten Zerlegungen lernen und seinen eigenen Suchraum verbessern?**

Dann würden unter anderem folgende Prozesse relevant:

```text
redundante Operatoren
→ zusammenlegen oder entfernen

unproduktive Operatoren
→ abwerten

wiederkehrende Residuen
→ neuen Operator suchen

erfolgreiche neue Schnitte
→ Operator abstrahieren

Operatorenraum
→ selbst refactoren
```

Dies ist Gegenstand von R3.
