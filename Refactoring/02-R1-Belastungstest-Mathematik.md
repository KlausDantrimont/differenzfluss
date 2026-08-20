# R1 – Belastungstest an mathematischen Abstraktionen

## Status

Nachfolgedokument zu `01-R1-gute-Zerlegung.md`.

Dieses Dokument prüft die dort formulierten Kriterien einer guten Zerlegung an historischen Beispielen aus der Mathematik.

Die Frage lautet nicht, ob Mathematik „genauso funktioniert“ wie das hier untersuchte Refactoring.

Die Frage lautet:

> **Beschreiben die Kriterien aus R1 tatsächlich erfolgreiche historische Abstraktions- und Strukturierungsprozesse?**

Wenn ja, steigt die Plausibilität, dass R1 mehr erfasst als nur die eigene begriffliche Konstruktion.

Wenn nein, muss R1 korrigiert werden.

---

# 1. Ausgangspunkt

R1 formuliert eine gute Zerlegung als:

> **eine bezüglich einer bestimmten relevanten Leistung maximal abstrahierte, möglichst wenig funktional redundante und strukturell ökonomische Basis, die genügend relationale Struktur erhält, um die relevante Leistung mindestens zu erkennen und zu erklären und im stärksten Fall generativ zu rekonstruieren.**

Kurz:

> **Minimale Struktur bei maximaler relevanter Rekonstruktionskraft.**

Für den Belastungstest werden bei jedem Beispiel dieselben Fragen gestellt:

1. Was war der heterogene oder unübersichtliche Ausgangsraum?
2. Welche relevante Leistung sollte erhalten bleiben?
3. Was wurde wegabstrahiert?
4. Was blieb invariant?
5. Welche Basis entstand?
6. Welche neue Erkennungs-, Erklärungs- oder Generierungsleistung wurde dadurch möglich?

---

# 2. Peano/Dedekind – Struktur statt konkreter Zahlvorstellung

Die natürlichen Zahlen waren lange vor ihrer modernen axiomatischen Fassung bekannt und praktisch verwendbar.

Die spätere axiomatische Arbeit bestand daher nicht darin, Zahlen zu „erfinden“.

Die strukturelle Frage lautete vielmehr:

> **Welche minimale Struktur muss vorausgesetzt werden, damit sich das Verhalten der natürlichen Zahlen erfassen und rekonstruieren lässt?**

Dabei treten konkrete Vorstellungen von Zahlen in den Hintergrund.

Tragend werden stattdessen Strukturen wie:

* ausgezeichnetes Anfangselement,
* Nachfolgerbeziehung,
* Eindeutigkeit bzw. Injektivität des Nachfolgers,
* Induktionsstruktur.

## R1-Lesart

### Ausgangsraum

Viele konkrete Zahlen, Rechenpraktiken und Zahlvorstellungen.

### Relevante Leistung

Die Struktur der natürlichen Zahlen und die auf ihr aufbauende Arithmetik erfassen.

### Wegabstrahiert

Die konkrete materielle oder anschauliche Natur der einzelnen Zahlen.

### Invariant

Die relationale Struktur von Anfang, Nachfolge und Induktion.

### Basis

Ein kleines Axiomensystem.

### Neue Leistung

Arithmetik kann aus wenigen strukturellen Voraussetzungen systematisch entwickelt und untersucht werden.

## Befund

R1 beschreibt diesen Vorgang gut.

Die Abstraktion vernichtet konkrete Information, ohne die relevante Leistung zu zerstören.

Gerade das ist ihre Funktion.

---

# 3. Gruppen – viele konkrete Systeme, ein gemeinsames Operationsskelett

Der abstrakte Gruppenbegriff entstand nicht als fertige Definition aus dem Nichts.

Vor ihm standen konkrete mathematische Probleme und Strukturen, insbesondere Permutationen und Symmetrien.

Mit der Zeit wurde sichtbar, dass sehr verschiedene Gegenstände dieselbe operative Grundstruktur besitzen.

Die konkrete Natur der Elemente konnte wegfallen.

Tragend blieben Eigenschaften der Operation:

* Verknüpfbarkeit,
* Assoziativität,
* neutrales Element,
* inverse Elemente.

## R1-Lesart

### Ausgangsraum

Permutationen, Symmetrien und andere konkrete algebraische Strukturen.

### Relevante Leistung

Das gemeinsame Verhalten ihrer Komposition erfassen.

### Wegabstrahiert

Was die Elemente konkret „sind“.

### Invariant

Die Operationsstruktur.

### Basis

Menge + Verknüpfung + wenige Strukturbedingungen.

### Neue Leistung

Allgemeine Sätze können einmal für die abstrakte Struktur bewiesen und anschließend auf sehr verschiedene konkrete Systeme übertragen werden.

## Befund

Der Gruppenbegriff ist ein besonders klarer Fall von:

> **viele konkrete Fälle → gemeinsame tragende Relationen → abstrakte generative Struktur**

Zugleich zeigt die historische Entwicklung, dass Basen selbst refactort werden können.

Frühe Definitionen können zu stark, zu speziell oder teilweise redundant sein.

---

# 4. Vektorräume – die Repräsentation wird irrelevant

Vektoren können sehr unterschiedlich konkret dargestellt werden.

Sie können geometrische Pfeile sein, Zahlenlisten, Funktionen oder andere mathematische Objekte.

Für viele Fragestellungen ist diese konkrete Repräsentation jedoch irrelevant.

Tragend ist die lineare Struktur:

* Addition,
* Skalarmultiplikation,
* die zugehörigen Strukturgesetze.

## R1-Lesart

### Ausgangsraum

Sehr verschiedene mathematische Objekte mit ähnlichem linearem Verhalten.

### Relevante Leistung

Lineare Kombination, lineare Abhängigkeit, Dimension und lineare Abbildungen behandeln.

### Wegabstrahiert

Die konkrete Natur der „Vektoren“.

### Invariant

Das lineare Relations- und Operationsmuster.

### Basis

Vektorraumstruktur.

### Neue Leistung

Dieselben Begriffe und Sätze werden auf sehr verschiedene Gegenstandsbereiche übertragbar.

## Befund

Dieses Beispiel bestätigt besonders deutlich die fundamentale Rolle des Wortes:

> **bezüglich**

Eine Vektorraumzerlegung soll nicht rekonstruieren, ob ihre Elemente ursprünglich Pfeile, Funktionen oder Zahlenfolgen waren.

Diese Information wurde absichtlich entfernt.

Sie soll die **relevante lineare Leistung** erhalten.

---

# 5. Kategorientheorie – Refactoring bereits abstrahierter Strukturen

Die Kategorientheorie geht noch eine Ebene weiter.

Hier werden nicht nur konkrete mathematische Objekte abstrahiert.

Auch bereits hochabstrakte mathematische Strukturen werden hinsichtlich ihrer Beziehungen und Abbildungen verglichen.

Wichtig werden dabei unter anderem:

* Objekte,
* Morphismen,
* Komposition,
* Identität,
* strukturtreue Abbildungen zwischen Kategorien,
* natürliche Transformationen.

Die konkrete innere Beschaffenheit eines mathematischen Objekts tritt dabei teilweise noch weiter zurück.

Entscheidend wird:

> **Wie steht etwas mit anderem in strukturverträglicher Beziehung?**

## R1-Lesart

### Ausgangsraum

Viele verschiedene mathematische Gebiete und bereits abstrahierte Strukturen.

### Relevante Leistung

Gemeinsame Beziehungsmuster und strukturtreue Transformationen erfassen.

### Wegabstrahiert

Große Teile der inneren konkreten Struktur einzelner Gegenstände.

### Invariant

Kompositions- und Beziehungsmuster.

### Basis

Objekte, Pfeile/Morphismen und Komposition.

### Neue Leistung

Strukturen verschiedener mathematischer Gebiete können auf einer gemeinsamen Ebene verglichen werden.

Analoge Konstruktionen werden sichtbar.

Strukturelle Übertragungen zwischen Gebieten werden systematisch formulierbar.

## Befund

Die Kategorientheorie ist für das Refactoring-Projekt besonders interessant, weil sie selbst wie ein **Meta-Refactoring** erscheint.

Sie fragt nicht nur:

> Welche Struktur trägt diesen Gegenstand?

sondern:

> **Welche strukturellen Muster tauchen in bereits abstrahierten Gegenstandsbereichen wiederholt auf?**

Damit nähert sie sich stark der Frage nach wiederverwendbaren Operatoren und Beziehungsmustern.

---

# 6. Ergebnis des Belastungstests

R1 beschreibt diese mathematischen Abstraktionsbewegungen überraschend gut.

Ein wiederkehrendes Schema lautet:

```text
komplexer / heterogener Ausgangsraum
↓
relevante Leistung bestimmen
↓
Variationen zulassen
↓
Invarianten erkennen
↓
konkrete Eigenschaften entfernen
↓
tragende Struktur isolieren
↓
Basis formulieren
↓
Erkennen / Erklären / Generieren
```

Der Belastungstest bestätigt damit den Grundgedanken:

> **Eine gute Abstraktion ist keine möglichst vollständige Beschreibung, sondern eine leistungsbezogene strukturelle Kompression.**

Gleichzeitig zwingt die Mathematik zu einigen Präzisierungen von R1.

---

# 7. Präzisierung A – Relevanz als Invarianz unter erlaubter Variation

Die bisherige Formulierung fragte:

> Welche Struktur ist für die relevante Leistung wesentlich?

Die mathematischen Beispiele legen eine stärkere Fassung nahe:

> **Welche Struktur bleibt invariant, wenn alle Veränderungen zugelassen werden, die bezüglich der Fragestellung irrelevant sein sollen?**

Damit wird der Variationstest zentral.

Nicht direkt nach dem „Wesen“ fragen.

Sondern:

1. verändern,
2. vergleichen,
3. beobachten, was erhalten bleibt.

Die Invarianten sind Kandidaten für das Skelett.

Dies liefert bereits einen wichtigen Hinweis für R2:

> **Variation → Invarianz → Skelett**

---

# 8. Präzisierung B – Minimalität ist relativ zu einer Sprache

„Die kleinste Basis“ ist nicht absolut bestimmt.

Minimalität hängt davon ab, welche Begriffe, Operationen oder Ausdrucksmittel bereits zur Verfügung stehen.

Wenn eine komplexe Operation als primitives Sprachelement vorausgesetzt wird, kann ein System formal mit weniger Axiomen oder Regeln beschrieben werden.

Die Komplexität wurde dann möglicherweise nur verborgen.

Deshalb gilt:

> **Minimalität ist immer relativ zu einer gegebenen Beschreibungssprache bzw. einem verfügbaren Operatorenraum.**

Das ergänzt das bereits in R1 formulierte Kriterium der strukturellen Ökonomie.

Ein einzelner Operator

```text
ALLES()
```

wäre formal minimal.

Er wäre aber keine gute Faktorisierung, weil seine innere Komplexität vollständig verborgen bleibt.

Eine brauchbare Basis braucht daher nicht nur wenige Elemente.

Ihre Elemente müssen selbst hinreichend einfach und transparent sein.

---

# 9. Präzisierung C – Generativität hat mehrere Formen

Die bisherige R1-Fassung unterscheidet:

```text
Erkennen
↓
Erklären
↓
Generieren
```

Der mathematische Belastungstest zeigt, dass „Generieren“ weiter aufgeteilt werden kann.

## Rekonstruktive Generativität

> Die relevante Leistung bekannter Fälle kann aus der Basis reproduziert werden.

## Deduktive Generativität

> Aus der Basis lassen sich neue Konsequenzen ableiten, die nicht einzeln in die Basis eingebaut wurden.

## Konstruktive Generativität

> Aus der Basis lassen sich neue konkrete Instanzen oder Konfigurationen derselben Struktur erzeugen.

Eine starke Basis besitzt damit eine Form von **produktiver Kompression**.

Sie fasst nicht nur Bekanntes kürzer zusammen.

Sie erzeugt einen Raum neuer möglicher Ableitungen und Konstruktionen.

---

# 10. Präzisierung D – Informationsverlust ist kein Fehler

Eine gute Abstraktion darf Information dauerhaft vernichten.

Das ist kein Defekt, sondern ihr Zweck.

Aus dem abstrakten Begriff einer Gruppe lässt sich beispielsweise nicht rekonstruieren, ob die konkreten Elemente ursprünglich Permutationen, Matrizen oder etwas anderes waren.

Diese Information ist bezüglich der Gruppenstruktur irrelevant.

Daraus folgt:

> Eine gute Zerlegung muss nicht das ursprüngliche System vollständig rekonstruieren.

Sie muss nur die bezüglich der Fragestellung **relevante Struktur oder Leistung** rekonstruieren.

Das Wort „relevant“ schützt R1 damit vor einem zu starken Rekonstruktionsanspruch.

---

# 11. Ergänzte Fassung von R1

Nach dem mathematischen Belastungstest lässt sich R1 präzisieren:

> **Eine gute Zerlegung eines komplexen Systems ist bezüglich einer bestimmten relevanten Leistung eine möglichst abstrakte, strukturell ökonomische und funktional wenig redundante Basis, welche die unter erlaubten Variationen invarianten tragenden Strukturen erhält und genügend generative Kraft besitzt, um die relevante Leistung zu erkennen, zu erklären oder zu rekonstruieren.**

Dabei gilt:

* Minimalität ist relativ zum verwendeten Operatoren- und Beschreibungsraum.
* Informationsverlust ist zulässig und notwendig, sofern er relevante Leistung nicht betrifft.
* Generativität kann rekonstruktiv, deduktiv oder konstruktiv sein.
* Invarianten unter relevanzneutralen Transformationen sind zentrale Kandidaten für tragende Struktur.

---

# 12. Ein erstes allgemeines Suchmuster

Der Belastungstest liefert bereits einen möglichen Übergang von R1 zu R2.

Statt unmittelbar zu fragen:

> Welche Teile sind fundamental?

kann gefragt werden:

> **Welche Veränderungen darf ich am Gegenstand vornehmen, ohne dass sich die für mich relevante Leistung ändert?**

Dann:

```text
Fragestellung
↓
relevante Leistung
↓
erlaubte Variation
↓
Invarianten
↓
Strukturskelett
```

Dies könnte ein elementarer Suchoperator für R2 sein.

---

# 13. Vorläufiges Fazit

R1 hat den mathematischen Belastungstest nicht nur überstanden.

Die Beispiele schärfen den Ansatz.

Insbesondere bestätigen sie:

> **Abstraktion ist leistungsbezogen.**

> **Gute Basen bewahren Invarianten statt Oberflächenmerkmale.**

> **Generativität ist eine starke Form von Verständnis.**

> **Eine gute Zerlegung darf große Mengen konkreter Information vernichten.**

> **Minimalität ist nur relativ zu einer gegebenen Sprache sinnvoll.**

Damit ist R1 vorläufig stabil genug, um als Qualitätsrahmen für R2 zu dienen.

---

# Übergang zu R2

R1 beantwortet:

> **Woran erkennen wir eine gute Zerlegung?**

R2 fragt nun:

> **Wie findet man eine solche Zerlegung, wenn man sie noch nicht kennt?**

Der mathematische Belastungstest liefert bereits einen ersten Kandidaten:

> **Variation → Invarianz → Skelett**

Ob und wie sich daraus zusammen mit weiteren Strukturachsen ein systematisches Suchverfahren bauen lässt, ist Gegenstand von R2.
::: 
