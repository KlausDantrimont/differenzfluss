# R3 – Lernen und Metarefactoring

## Status

Nachfolgedokument zu:

- `01-R1-gute-Zerlegung.md`
- `02-R1-Belastungstest-Mathematik.md`
- `03-R2-Basisfindung.md`

R1 beantwortet:

> **Woran erkennt man eine gute Zerlegung?**

R2 beantwortet:

> **Wie findet man eine gute Zerlegung?**

R3 geht eine Ebene höher:

> **Wie lernt ein Refactoring-Verfahren aus erfolgreichen und gescheiterten Zerlegungen und verbessert dadurch seinen eigenen Operatorenraum?**

Dabei zeigt sich eine grundlegende Unterscheidung:

1. **gerichtetes Lernen**
2. **exploratives Lernen**
3. **Metarefactoring**

---

# 1. Refactoring als Lernprozess

R2 beschreibt Refactoring als iterativen Suchprozess:

```text
Frage
↓
Schnitt
↓
Kandidaten
↓
Variation
↓
Invarianz
↓
Abstraktion
↓
Refactoring
↓
Prüfung
↓
Residuum
```

R3 betrachtet nicht mehr nur das Ergebnis dieses Prozesses.

Es betrachtet den **Suchprozess selbst als lernfähiges System**.

Das Verfahren soll sich merken:

- welche Fragen gestellt wurden,
- welche Schnitte versucht wurden,
- welche Operatoren eingesetzt wurden,
- welche Zerlegungen gut funktioniert haben,
- welche Residuen übrig blieben,
- welche Operatoren redundant waren,
- welche neuen Operatoren entstanden,
- und unter welchen Bedingungen bestimmte Suchstrategien erfolgreich waren.

Damit wird jede Analyse selbst zu Trainingsmaterial für spätere Analysen.

---

# 2. Zwei Arten von Lernrichtung

## 2.1 Gerichtetes Lernen

Eine Frage oder Aufgabe gibt bereits vor:

- worum es geht,
- welche Leistung relevant ist,
- und woran der Erfolg gemessen wird.

Die Frage erzeugt damit eine **Bewertungsfunktion**.

Beispiel:

> Welche Faktoren machen dieses System instabil?

Dann kann ein Operator danach bewertet werden, ob er hilft:

- relevante Instabilitäten sichtbar zu machen,
- Residuen zu reduzieren,
- Vorhersagen zu verbessern,
- Ursachen zu isolieren,
- oder ein besseres generatives Modell zu bauen.

Die Richtung kommt von außen.

## 2.2 Exploratives Lernen

Beim explorativen Lernen gibt es keine einzelne vorgegebene Frage.

Das System sucht selbst nach Bereichen, in denen Lernen wahrscheinlich lohnend ist.

Die Frage lautet dann:

> **Wo könnte Refactoring Erkenntnisgewinn erzeugen?**

Die Richtung entsteht aus internen Signalen.

Dazu gehören beispielsweise:

- Inkonsistenz,
- Überraschung,
- wiederkehrende Fehler,
- ungelöste Residuen,
- hohe Komplexität,
- viele Sonderregeln,
- funktionale Redundanz,
- unerwartete Ähnlichkeiten,
- ungenutzte Analogien,
- wiederkehrende negative Folgen,
- oder Hinweise auf starke mögliche Kompression.

Das Lernen ist damit nicht wirklich richtungslos.

Es besitzt nur keine von außen gesetzte Zielrichtung.

Besser ist daher der Begriff:

> **exploratives Lernen**

---

# 3. R3a – Gerichtetes Lernen

## 3.1 Ausgangspunkt

Gerichtetes Lernen beginnt mit:

```text
Frage
↓
relevante Leistung
↓
Bewertungsfunktion
```

Damit entsteht ein lokaler Maßstab für die Qualität von Suchoperatoren.

Ein Operator ist nicht abstrakt „gut“.

Er ist gut **bezüglich einer bestimmten Aufgabe**.

## 3.2 Bewertung eines Operators

Ein Suchoperator O kann beispielsweise danach bewertet werden:

> Wie stark verbessert O die Qualität der gefundenen Basis bezüglich Leistung L?

Mögliche Kriterien:

- reduziert O relevante Residuen?
- erhöht O die Rekonstruktionskraft?
- verbessert O Erkennen, Erklären oder Generieren?
- reduziert O Suchkosten?
- reduziert O funktionale Redundanz?
- erzeugt O bessere Transferfähigkeit?
- verhindert O wiederkehrende Fehlzerlegungen?
- erzeugt O neue deduktive oder konstruktive Möglichkeiten?

Damit bekommt jeder Operator eine **kontextabhängige Erfolgsbilanz**.

---

# 4. Operatoren sind nicht global gut oder schlecht

Ein Operator kann in einer Domäne sehr produktiv und in einer anderen nahezu nutzlos sein.

Beispiel:

- ZEIT kann für einen dynamischen Prozess zentral sein.
- Für eine rein statische Klassifikation kann ZEIT kaum zusätzlichen Nutzen liefern.
- PERSPEKTIVE kann in sozialen Systemen enorm wichtig sein.
- In einem stark formalisierten technischen Teilproblem kann sie weniger relevant sein.

Daraus folgt:

> **Der Wert eines Operators ist kontextabhängig.**

R3 sollte daher nicht nur speichern:

> Operator O war erfolgreich.

Sondern:

> Operator O war unter Kontext C bezüglich Leistung L erfolgreich.

Damit entsteht eine Art Erfahrungsraum:

```text
Kontext
×
Fragestellung
×
Operator
×
Ergebnis
```

---

# 5. R3b – Exploratives Lernen

Exploratives Lernen besitzt keine einzelne externe Bewertungsfunktion.

Es sucht stattdessen nach **epistemischen Spannungen**.

Diese Spannungen markieren Orte, an denen neues Refactoring lohnend sein könnte.

---

# 6. Interne Suchsignale

## Inkonsistenz

> Zwei Modelle, Überzeugungen oder Erinnerungen passen nicht zusammen.

Eine Inkonsistenz kann darauf hinweisen, dass:

- Begriffe vermischt wurden,
- eine Perspektive fehlt,
- eine Systemgrenze falsch gesetzt ist,
- oder mehrere unterschiedliche Strukturen unter demselben Begriff zusammengefasst wurden.

## Überraschung

> Erwartung und Beobachtung weichen deutlich voneinander ab.

Überraschung signalisiert:

> Das aktuelle Strukturmodell besitzt eine Lücke.

## Residuum

> Etwas bleibt wiederholt unerklärt.

Ein einzelnes Residuum kann Zufall sein.

Wiederkehrende Residuen können auf einen systematischen blinden Fleck hinweisen.

## Sonderfalllast

> Ein Modell benötigt viele Ausnahmen und Zusatzregeln.

Das kann bedeuten:

> Die Basis ist schlecht gewählt.

Ein besserer Schnitt könnte mehrere Sonderfälle in einer allgemeineren Struktur zusammenführen.

## Redundanz

> Mehrere Begriffe oder Operatoren scheinen dieselbe funktionale Rolle zu erfüllen.

Dies ist ein Kandidat für MERGE oder GENERALIZE.

## Überkomplexität

> Ein Bereich benötigt ungewöhnlich viele Variablen oder Regeln.

Dort kann hohe Kompressionschance bestehen.

## Wiederholung

> Ähnliche Relationsmuster treten in verschiedenen Kontexten auf.

Das kann auf eine bisher unbenannte abstrakte Struktur hinweisen.

## Analogie

> Zwei scheinbar getrennte Bereiche besitzen ähnliche relationale Skelette.

Eine solche Ähnlichkeit kann neue Übertragungen oder Begriffe ermöglichen.

## Schmerz / wiederkehrende negative Folge

Bei Menschen können wiederkehrende problematische Folgen selbst Suchsignale bilden.

Beispielsweise:

- wiederkehrende Konflikte,
- dieselbe Fehlentscheidung,
- dieselbe Form von Überforderung,
- dieselbe unerklärte emotionale Reaktion.

Das Refactoring fragt dann nicht zunächst:

> Was ist falsch mit mir?

Sondern:

> **Welche Struktur wiederholt sich hier?**

## Chance

Nicht nur Probleme erzeugen Suchsignale.

Auch ungewöhnlich gut funktionierende Situationen können interessant sein.

Frage:

> **Welche Struktur trägt diesen unerwarteten Erfolg?**

Damit wird Lernen nicht nur fehlergetrieben.

Es kann auch nach positiver generativer Struktur suchen.

---

# 7. Erinnerung als Reservoir ungelöster Strukturprobleme

Erfahrungen müssen nicht sofort vollständig verstanden werden.

Eine Szene kann zunächst gespeichert werden mit:

- damaliger Interpretation,
- offenen Fragen,
- emotionaler oder praktischer Relevanz,
- unerklärten Residuen,
- widersprüchlichen Deutungen.

Später kann ein veränderter Operatorenraum dieselbe Szene erneut untersuchen.

```text
Erfahrung
↓
vorläufige Strukturierung
↓
Residuum / Inkonsistenz speichern
↓
neue Erfahrungen / neue Operatoren
↓
alte Szene erneut untersuchen
↓
neue Struktur sichtbar
```

Damit ist Erinnerung nicht bloß Archiv.

Sie wird zu:

> **einem Reservoir noch nicht vollständig refactorierter Szenen.**

---

# 8. Neue Erkenntnis kann rückwärts wirken

Lernen verändert nicht nur zukünftige Analysen.

Es kann vergangene Szenen neu strukturieren.

Eine frühere Situation kann Jahre später verständlich werden, weil inzwischen:

- ein neuer Begriff vorhanden ist,
- eine neue Perspektive gelernt wurde,
- ein bisher unbekannter Zusammenhang erkannt wurde,
- oder mehrere alte Szenen plötzlich dasselbe Relationsmuster zeigen.

Die Szene bleibt gleich.

Der **Operatorenraum** hat sich verändert.

Damit wird Lernen rekursiv:

```text
neue Struktur
↓
verändert Interpretation alter Erfahrung
↓
alte Erfahrung liefert neue Evidenz
↓
verändert wiederum die neue Struktur
```

---

# 9. Von Residuen zu neuen Fragen

Exploratives Lernen soll nicht nur Defizite markieren.

Es soll daraus neue Forschungsfragen erzeugen.

```text
wiederkehrendes Residuum
↓
Cluster ähnlicher Residuen
↓
Hypothese eines fehlenden Schnitts
↓
neue Frage
↓
gerichteter R2-Prozess
```

Damit erzeugt exploratives Lernen seine eigenen gerichteten Lernprozesse.

Aus:

> Hier stimmt etwas nicht.

wird beispielsweise:

> Welche zusätzliche Variable erklärt diese Abweichung?

Oder:

> Welche zwei bisher getrennten Strukturen sind möglicherweise Varianten desselben Musters?

Oder:

> Welche relevante Perspektive fehlt hier?

---

# 10. Epistemischer Erwartungswert

Ein exploratives System kann nicht überall gleichzeitig suchen.

Es braucht daher eine Priorisierung.

Ein Bereich ist besonders interessant, wenn beispielsweise:

- große Inkonsistenz vorliegt,
- viele Fälle betroffen sind,
- hohe praktische Relevanz besteht,
- starke Kompression möglich erscheint,
- eine neue Struktur viele Residuen gleichzeitig erklären könnte,
- oder geringe Suchkosten hohem möglichen Gewinn gegenüberstehen.

Damit entsteht eine heuristische Bewertungsgröße:

> **Wo ist der erwartete Erkenntnisgewinn pro Suchaufwand besonders hoch?**

Dies ist keine notwendige mathematische Formel.

Es ist zunächst eine Priorisierungsregel.

---

# 11. R3c – Metarefactoring

Gerichtetes und exploratives Lernen erzeugen Erfahrungen über den eigenen Operatorenraum.

Metarefactoring verwendet diese Erfahrungen, um die Suchwerkzeuge selbst zu verändern.

Die Frage lautet:

> **Welche Evidenz rechtfertigt es, einen Operator beizubehalten, zu verändern, zusammenzulegen oder zu verwerfen?**

---

# 12. Operationen auf dem Operatorenraum

## KEEP

Ein Operator wird beibehalten, wenn er wiederholt relevanten Erkenntnisgewinn erzeugt.

## DOWNWEIGHT

Ein Operator bleibt verfügbar, wird aber seltener priorisiert, wenn er in bestimmten Kontexten wenig beiträgt.

## REMOVE

Ein Operator kann entfernt werden, wenn er:

- dauerhaft keinen zusätzlichen Erkenntnisgewinn erzeugt,
- vollständig durch andere Operatoren ersetzbar ist,
- oder nur Redundanz erzeugt.

## MERGE

Zwei Operatoren können zusammengelegt werden, wenn sie über viele Fälle hinweg dieselbe funktionale Rolle besitzen.

## SPLIT

Ein Operator kann aufgeteilt werden, wenn sich zeigt, dass er mehrere unterschiedliche Suchfunktionen vermischt.

## GENERALIZE

Mehrere erfolgreiche spezialisierte Operatoren können auf eine gemeinsame abstraktere Struktur zurückgeführt werden.

## SPECIALIZE

Ein allgemeiner Operator kann in spezifischere Varianten zerlegt werden, wenn verschiedene Kontexte systematisch unterschiedliche Anwendungen verlangen.

## COMPOSE

Mehrere Operatoren können zu einer häufig nützlichen Suchsequenz kombiniert werden.

Beispiel:

```text
Variation
→ Invarianz
→ Entfernungstest
```

## INVENT

Wiederkehrende Residuen können einen neuen Operator nahelegen.

Ein neuer Operator entsteht dann nicht aus freier Begriffsproduktion, sondern aus:

> **wiederkehrender struktureller Notwendigkeit.**

---

# 13. Wie entsteht ein neuer Operator?

Ein möglicher Prozess lautet:

```text
mehrere ungelöste Fälle
↓
ähnliches Residuum
↓
gemeinsames Relationsmuster
↓
neuer Schnitt
↓
an mehreren Fällen testen
↓
wiederkehrender Erkenntnisgewinn
↓
Operator abstrahieren
```

Erst danach braucht der Operator einen Namen.

Damit gilt erneut:

> **Begriff = Interface für eine stabilisierte funktionale Struktur.**

Ein KI-System könnte eine solche Struktur zunächst ohne sprachliche Benennung verwenden.

---

# 14. Fitness eines Operatorenraums

Nicht nur einzelne Operatoren können bewertet werden.

Auch ein kompletter Operatorensatz kann gegen einen anderen getestet werden.

```text
Operatorensatz A
vs.
Operatorensatz B
```

Vergleichskriterien können sein:

- Qualität der gefundenen Zerlegungen nach R1,
- Suchkosten,
- Geschwindigkeit bis zu einer brauchbaren Basis,
- Anzahl benötigter Sonderfälle,
- Größe verbleibender Residuen,
- Transfer über verschiedene Domänen,
- generative Leistung,
- Robustheit gegenüber veränderten Fragestellungen.

Damit wird Metarefactoring experimentell prüfbar.

---

# 15. Lernen als rekursiver Zyklus

Die drei Ebenen greifen ineinander:

```text
R3a – gerichtetes Lernen
Frage
↓
Operatoren anwenden
↓
Erfolg / Misserfolg bewerten

             ↓

R3b – exploratives Lernen
Residuen / Inkonsistenzen / Chancen
↓
neue Fragen erzeugen

             ↓

R3c – Metarefactoring
Suchhistorien vergleichen
↓
Operatoren verändern
↓
neuer Operatorenraum
```

Dann beginnt der Zyklus erneut.

Der neue Operatorenraum verändert:

- welche Unterschiede wahrgenommen werden,
- welche Fragen entstehen,
- welche Zerlegungen gefunden werden,
- und welche alten Erfahrungen neu interpretierbar werden.

---

# 16. Menschliche Operationalisierung

Beim Menschen geschieht ein großer Teil dieses Prozesses implizit.

Menschen:

- lernen neue Begriffe,
- verändern ihre Perspektiven,
- erkennen alte Situationen neu,
- entwickeln Heuristiken,
- verwerfen schlechte Erklärungen,
- bilden Analogien,
- und lernen, welche Fragen in welchen Situationen nützlich sind.

Eine explizite Refactoring-Methode könnte diesen Prozess unterstützen.

Beispielhafte Meta-Fragen:

> Welche Art von Frage hat mir hier geholfen?

> Welche Perspektive hat wiederholt nichts gebracht?

> Welche Begriffe verwende ich für eigentlich verschiedene Dinge?

> Welche wiederkehrende Irritation habe ich bisher nie als gemeinsames Muster betrachtet?

> Welche frühere Situation würde ich mit meinem heutigen Begriffsraum anders verstehen?

> Wo brauche ich ungewöhnlich viele Sondererklärungen?

So wird Metarefactoring zu einer Form bewusster epistemischer Selbstbeobachtung.

---

# 17. KI-Operationalisierung

Bei KI-Systemen kann R3 wesentlich expliziter implementiert werden.

Ein System kann protokollieren:

- Fragestellung,
- Kontext,
- verwendete Operatoren,
- Reihenfolge der Operatoren,
- erzeugte Kandidaten,
- Bewertungswerte,
- verworfene Wege,
- verbleibende Residuen,
- erfolgreiche Transfers.

Damit können lernende Modelle entstehen:

> In Kontext C besitzt Operator O hohe erwartete epistemische Nützlichkeit.

Oder:

> Die Operatorsequenz O1 → O2 → O3 ist bei Problemklasse P besonders erfolgreich.

KI eröffnet damit die Möglichkeit:

> **Refactoring selbst als lernbaren Suchprozess zu behandeln.**

---

# 18. Interaktives Lernen von Mensch und KI

Besonders interessant ist die Kombination.

Der Mensch kann:

- Relevanz setzen,
- Schmerz und Bedeutung bewerten,
- normative Ziele bestimmen,
- überraschende Analogien beurteilen,
- Kontext korrigieren.

Die KI kann:

- große Suchhistorien vergleichen,
- alte Szenen erneut analysieren,
- wiederkehrende Residuen clustern,
- operatorische Redundanzen erkennen,
- neue Operatorenkandidaten erzeugen,
- und systematisch testen.

Damit entsteht eine mögliche Arbeitsteilung:

```text
Mensch:
Bedeutung / Relevanz / Kontext

KI:
Suche / Variation / Vergleich / Gedächtnis

gemeinsam:
Bewertung / neue Fragen / neue Operatoren
```

---

# 19. Eine wichtige Grenze

Exploratives Lernen darf nicht mit permanenter Problemproduktion verwechselt werden.

Ein System, das überall Inkonsistenzen sucht, könnte endlos neue Fragen erzeugen.

Deshalb gilt auch hier ein Suchbudget.

Nicht jede Irritation verdient Analyse.

Nicht jedes Residuum ist relevant.

Nicht jede mögliche Kompression ist praktisch interessant.

Auch exploratives Lernen braucht Priorisierung nach:

- Relevanz,
- erwarteter Erkenntnis,
- möglicher Wirkung,
- und Suchkosten.

---

# 20. Vorläufige Antwort auf R3

> **Ein Refactoring-Verfahren kann lernen, indem es Suchverläufe, Erfolge, Misserfolge und Residuen speichert und daraus die kontextabhängige Nützlichkeit seiner Operatoren ableitet.**

Gerichtetes Lernen erhält seine Bewertungsfunktion aus einer Frage und der damit gesetzten relevanten Leistung.

Exploratives Lernen erzeugt neue Fragen aus internen epistemischen Signalen wie Inkonsistenz, Überraschung, Residuen, Redundanz, Überkomplexität oder wiederkehrenden Mustern.

Metarefactoring verändert daraufhin den Operatorenraum selbst:

> **beibehalten, abwerten, entfernen, zusammenlegen, aufspalten, generalisieren, spezialisieren, komponieren oder neu erzeugen.**

Dadurch entsteht ein rekursiver Lernprozess:

> **Refactoring verändert den Operatorenraum.  
> Der veränderte Operatorenraum verändert Wahrnehmung und Fragebildung.  
> Neue Fragen erzeugen neue Refactoring-Erfahrungen.**

---

# 21. Kurzform

## R3a – Gerichtetes Lernen

> **Welche Operatoren helfen bezüglich einer gegebenen Frage?**

```text
Frage
→ Bewertungsfunktion
→ Operatoren testen
→ Nützlichkeit lernen
```

## R3b – Exploratives Lernen

> **Wo lohnt es sich, überhaupt eine neue Frage zu stellen?**

```text
Inkonsistenz / Überraschung / Residuum / Chance
→ erwarteter Erkenntnisgewinn
→ neue Frage
```

## R3c – Metarefactoring

> **Wie wird aus diesen Erfahrungen ein besserer Operatorenraum?**

```text
Suchhistorien
→ Operatoren bewerten
→ Operatoren refactoren
→ erneut suchen
```

---

# 22. Gesamtarchitektur R1–R3

```text
R1
Was ist eine gute Zerlegung?
↓
Qualitätsmaßstab

R2
Wie findet man sie?
↓
Suchverfahren

R3
Wie verbessert sich das Suchverfahren selbst?
↓
Lernprozess
```

Oder als rekursiver Gesamtprozess:

```text
Frage
↓
Refactoring
↓
Basis
↓
Prüfung
↓
Erfahrung
↓
Operatoren lernen
↓
neue Wahrnehmung
↓
neue Fragen
↓
Refactoring
```

Damit wird Refactoring nicht nur zu einer Methode der Analyse.

Es wird zu einem Modell dafür, wie ein lernendes System seine eigenen Möglichkeiten zur Strukturierung von Erfahrung schrittweise verbessern kann.
