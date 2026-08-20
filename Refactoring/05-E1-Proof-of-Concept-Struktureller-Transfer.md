# E1 – Proof of Concept: Struktureller Transfer über verschiedene Biotope

## Status

Erster experimenteller Test des Refactoring-Ansatzes.

Bezug:

- `01-R1-gute-Zerlegung.md`
- `02-R1-Belastungstest-Mathematik.md`
- `03-R2-Basisfindung.md`
- `04-R3-Lernen-und-Metarefactoring.md`

E1 untersucht die Frage:

> **Kann ein Refactoring-Verfahren in verschieden dargestellten Situationen wiederkehrende tragende Strukturen erkennen, abstrahieren und auf neue Situationen übertragen?**

Der Test ist ausdrücklich als **Proof of Concept** gedacht.

Er soll nicht zeigen, dass eine bestimmte Ontologie richtig ist.

Er soll zeigen, ob die Grundidee praktisch trägt.

---

# 1. Grundidee

Unterschiedliche Systeme können sehr verschiedene Oberflächen besitzen und dennoch funktional ähnliche Strukturen enthalten.

Beispiele für mögliche „Biotope“:

- Psyche,
- Gemeinschaft,
- Team,
- Verein,
- Organisation,
- technisches System.

Die konkrete Sprache und die konkreten Elemente unterscheiden sich.

Gesucht wird:

> **eine übertragbare tragende Struktur unterhalb der Oberfläche.**

Beispiel:

```text
Psyche:
Überforderung
→ Rückzug
→ kurzfristige Entlastung
→ weniger Korrekturerfahrung
→ stärkere Unsicherheit

Team:
Fehler
→ Schuldzuweisung
→ Informationszurückhaltung
→ weniger Korrektur
→ mehr Fehler

Verein:
Konflikt
→ Zentralisierung
→ weniger Beteiligung
→ weniger Rückmeldung
→ schlechtere Entscheidungen
```

Eine mögliche gemeinsame Struktur wäre:

```text
Störung
→ defensive Stabilisierung
→ Rückkopplung wird reduziert
→ kurzfristige Stabilität
→ langfristig sinkende Anpassungsfähigkeit
```

Diese gemeinsame Struktur darf nicht einfach vorausgesetzt werden.

Sie dient hier nur als Beispiel dafür, wie ein E1-Test konstruiert werden kann.

---

# 2. Relevante Leistung

Die relevante Leistung von E1 ist zunächst bewusst bescheiden:

> **Proof of Concept für strukturellen Transfer.**

Konkret:

> Kann das Verfahren in unterschiedlich dargestellten Situationen wiederkehrende tragende Strukturen erkennen und zu einer kleineren, übertragbaren Basis abstrahieren?

E1 soll zunächst nicht beweisen:

- dass die gefundene Struktur ontologisch fundamental ist,
- dass der Operatorenraum optimal ist,
- dass autonomes Lernen funktioniert,
- oder dass eine universelle Strukturtheorie vorliegt.

Der erste Test lautet nur:

> **Funktioniert die Grundidee sichtbar und reproduzierbar?**

---

# 3. Konstruktion der Testfälle

E1 verwendet mehrere Szenen aus unterschiedlichen Biotopen.

Die Testfälle können bewusst parallel konstruiert werden.

Dabei werden:

- verschiedene konkrete Begriffe,
- verschiedene Akteure,
- verschiedene Oberflächenmechanismen,
- verschiedene sprachliche Formen

verwendet.

Unterhalb dieser Unterschiede werden jedoch bestimmte funktionale Beziehungen absichtlich ähnlich gehalten.

Dadurch entsteht ein kontrollierter Test:

> Erkennt das Verfahren die gemeinsame Struktur trotz unterschiedlicher Oberfläche?

Später können weniger künstliche und stärker offene Fälle hinzukommen.

---

# 4. Darstellung der Szenen

Die primäre Repräsentation bleibt **natürlichsprachlich**.

Gründe:

- hohe semantische Ausdruckskraft,
- gute Lesbarkeit,
- leichte Analyse,
- nachvollziehbares Debugging,
- geringe Bindung an ein bestimmtes Formalismusformat.

Zusätzlich darf **Python-Code** verwendet werden.

Python eignet sich besonders für:

- kompakte Zustandsregeln,
- Übergänge,
- kleine Simulationen,
- Variationen,
- Testfälle.

Beispiel:

```text
Wenn Belastung steigt und Rückkopplungsfähigkeit sinkt,
wird eine kurzfristig stabilisierende Reaktion wahrscheinlicher,
die langfristig weitere Rückkopplung reduziert.
```

Optional präzisiert durch:

```python
if load > capacity and feedback < threshold:
    defensive_stabilization += 1
    feedback -= suppression
```

Python dient hier nicht als Ontologie.

Es ist eine mögliche **ausführbare Präzisierung einer Strukturhypothese**.

---

# 5. Der Boot-Kontext

Jeder Durchlauf beginnt mit einem deklarierbaren Ausgangskontext.

Der Boot-Kontext ist:

> **keine Ontologie, sondern der deklarierte Ausgangszustand des epistemischen Suchverfahrens.**

Er besteht mindestens aus zwei Bereichen.

## 5.1 Prämissen

Dieser Bereich ist zunächst relativ stabil.

Beispiele:

- Die Frage setzt Relevanz.
- Modelle sind perspektivisch.
- Gute Modelle dürfen Information verlieren.
- Ontologische Wahrheit folgt nicht aus Modellfit.
- Unsicherheit soll sichtbar bleiben.
- Widerspruch darf ein Modell beschädigen.
- Suchkosten sind endlich.
- Kein Operator gilt allein aufgrund seiner Herkunft als notwendig.

## 5.2 Adaptiver Bereich

Dieser Bereich darf durch Erfahrung verändert werden.

Beispiele:

- bevorzugte Suchoperatoren,
- Operatorengewichte,
- erfolgreiche Operatorsequenzen,
- bekannte Strukturmuster,
- domänenspezifische Heuristiken,
- wiederkehrende Residuen,
- vergangene Fehlzerlegungen.

Schema:

```text
BOOT-KONTEXT

[PRÄMISSEN]
relativ stabil

[ADAPTIVER BEREICH]
lernbar
```

---

# 6. Rekursion im Boot-Kontext

Ob der adaptive Bereich die Prämissen verändern darf, ist selbst eine Prämisse.

Damit kann später eine dritte Ebene sinnvoll werden:

```text
P0  Meta-Prämissen
    Was darf überhaupt verändert werden?

P1  Arbeitsprämissen
    Epistemische Grundregeln

A   Adaptiver Operatorenraum
    Lernbarer Werkzeugkasten
```

Für E1 genügt zunächst die Zwei-Ebenen-Struktur.

Die Meta-Ebene wird erst relevant, wenn das Verfahren selbst seine Grundregeln refactoren soll.

---

# 7. Versuchsbedingungen

E1 vergleicht zunächst einfache Varianten.

## A – Baseline

Instruktion:

> Analysiere diese Szenen und finde wiederkehrende oder tragende Strukturen.

Keine expliziten R1/R2-Regeln.

## B – R1

Zusätzlich werden Qualitätskriterien bereitgestellt:

- relevante Leistung,
- Abstraktion,
- Strukturerhalt,
- geringe funktionale Redundanz,
- Erkennen,
- Erklären,
- Generieren.

## C – R1 + R2

Zusätzlich wird das Suchverfahren verwendet:

```text
Frage
→ Schnitt
→ Variation
→ Invarianz
→ Abstraktion
→ Refactoring
→ Prüfung
→ Residuum
```

## D – R1 + R2 + Boot-Kontext

Zusätzlich wird eine explizite Startkonfiguration verwendet.

Später können Ablationen folgen.

---

# 8. Was wird verglichen?

Strukturelle Äquivalenz wird zunächst nicht primär formal über Graphisomorphie gemessen.

Stattdessen wird die **behaviorale Äquivalenz der Analyse** betrachtet.

Fragen:

> Welche Beziehungen werden als tragend identifiziert?

> Welche Details werden wegabstrahiert?

> Welche Folgen werden erwartet?

> Welche Hebel werden gesehen?

> Welche Gegenhypothesen entstehen?

> Welche Variationen gelten als relevant?

> Welche nächsten Fragen werden erzeugt?

Wenn zwei sehr unterschiedlich erzählte Szenen zu strukturell analogen Analysen führen, ist das Evidenz für erfolgreichen Transfer.

Nicht notwendig für ontologische Gleichheit.

---

# 9. Bewertungsgrößen

Für E1 werden zunächst qualitative und halbquantitative Kriterien verwendet.

## Strukturelle Übereinstimmung

Erkennen verschiedene Durchläufe ähnliche tragende Beziehungen?

## Oberflächenunabhängigkeit

Bleibt die Analyse stabil, wenn Namen, Rollen oder nebensächliche Details verändert werden?

## Transfer

Wird ein in einem Biotop erkanntes Muster in einem anderen Biotop wiedergefunden?

## Redundanz

Wie viele unnötige oder doppelte Kategorien werden erzeugt?

## Abstraktion

Wird die Beschreibung tatsächlich kleiner und allgemeiner?

## Erklärungsleistung

Hilft die gefundene Struktur, die Szenen verständlicher zu machen?

## Generative Leistung

Erzeugt die Basis plausible Erwartungen, neue Fälle, Hypothesen oder Simulationen?

---

# 10. Suchkosten

Suchkosten werden im Proof of Concept zunächst bewusst grob erfasst.

Ein fein kalibriertes Sensorium dafür existiert noch nicht.

Vorläufig genügen:

- Zahl deutlich unterschiedlicher Anläufe,
- Zahl notwendiger Korrekturen,
- sichtbare Komplexität der Analyse,
- Zahl zusätzlicher Sonderannahmen,
- Zahl menschlicher Eingriffe,
- subjektiv wahrgenommene kognitive Belastung.

Prinzip:

> **Daumen mal Pi, aber protokolliert.**

Erst wenn Suchkosten selbst experimentell wichtig werden, lohnt sich eine feinere Instrumentierung.

---

# 11. Anzahl der Testsysteme

E1 legt keine feste Zahl unabhängiger Testsysteme vorab fest.

Der Prozess ist iterativ.

Vorgehen:

```text
wenige einfache Fälle
↓
Fehler sichtbar machen
↓
Verfahren anpassen
↓
schwierigere Fälle
↓
erneut testen
```

Wenn zusätzliche Fälle keine neue Information mehr liefern, wird nicht einfach die Fallzahl erhöht.

Dann wird das Testdesign verändert.

---

# 12. Ein möglicher erster Mini-Test

Drei Biotope:

```text
A – Psyche
B – Team
C – Verein
```

Alle drei Szenen werden so konstruiert, dass ein ähnliches funktionales Rückkopplungsmuster unter verschiedenen Oberflächen verborgen liegt.

Dann werden verglichen:

```text
Baseline
vs.
R1
vs.
R1 + R2
```

Erst danach:

```text
R1 + R2 + Boot-Kontext
```

Die Kernfrage lautet:

> **Findet Refactoring in den drei Welten stabiler dasselbe oder ein strukturell ähnliches Skelett als eine unspezifische Analyse?**

---

# 13. Späterer R3-Test

Nach mehreren Durchläufen kann ein ursprünglicher Operatorenraum O₀ anhand der Erfahrungen verändert werden.

```text
O₀
↓
Erfahrung
↓
Metarefactoring
↓
O₁
```

Dann werden neue Testfälle verwendet.

Die entscheidende Frage lautet:

> **Findet O₁ bei neuen Problemen bessere Zerlegungen als O₀?**

Damit wird Lernen als Transfer geprüft.

Bloßes Erinnern an vergangene Lösungen genügt nicht.

---

# 14. Keine Ontologiebehauptung

E1 prüft nicht:

> Wie ist die Welt wirklich aufgebaut?

Geprüft wird:

> **Kann ein explizites Refactoring-Verfahren funktionale Strukturen über unterschiedliche Darstellungen hinweg zuverlässig erkennen und übertragen?**

Ein erfolgreiches Ergebnis ist daher zunächst:

> ein gutes Modell bezüglich einer definierten Leistung.

Nicht:

> eine ontologisch wahre Beschreibung.

---

# 15. Erfolgskriterium

Die minimale Erfolgsaussage für E1 lautet:

> **R1+R2 erzeugt über verschiedenartige Szenen hinweg konsistentere, abstraktere oder besser übertragbare Strukturbeschreibungen als eine unspezifische Baseline.**

Eine stärkere Aussage wäre:

> **Ein durch R3 veränderter Operatorenraum O₁ übertrifft O₀ bei neuen Testfällen.**

Scheitert dies, ist das ebenfalls ein verwertbares Ergebnis.

Dann kann geprüft werden:

- ob R1 ungeeignete Qualitätskriterien enthält,
- ob R2 keinen zusätzlichen Suchwert liefert,
- ob der Boot-Kontext verzerrt,
- ob das Testdesign zu einfach oder zu künstlich ist,
- oder ob leistungsfähige Sprachmodelle die beschriebenen Heuristiken ohnehin implizit anwenden.

---

# 16. Kurzform

> **E1 ist ein Proof of Concept für strukturellen Transfer.**

Mehrere verschiedenartige Biotope enthalten bewusst ähnliche funktionale Strukturen.

Das Refactoring-Verfahren soll:

```text
Oberfläche
↓
tragende Relationen
↓
Abstraktion
↓
übertragbares Skelett
```

leisten.

Verglichen werden zunächst:

```text
Baseline
vs.
R1
vs.
R1 + R2
```

Später:

```text
+ Boot-Kontext
+ Ablationen
+ O₀ vs. O₁
```

Die Ergebnisse bleiben primär natürlichsprachlich und dürfen durch Python präzisiert oder ausführbar gemacht werden.

Damit prüft E1 die Grundidee des Refactorings, ohne eine Ontologie vorauszusetzen.

---
Ergänzung:

Der Nutzen expliziter Operatoren bemisst sich nicht ausschließlich an höherer Analyseleistung. Explizierung kann auch dadurch wertvoll sein, dass sie Suchprozesse beobachtbar, vergleichbar, steuerbar und selbst zum Gegenstand von Lernen und Refactoring macht.

