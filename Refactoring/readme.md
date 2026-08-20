# Refactoring

## Worum es hier geht

Dieses Verzeichnis untersucht eine einfache Frage:

> **Wie findet man eine gute Zerlegung eines komplexen Systems?**

Mit „Zerlegung“ ist dabei nicht gemeint, einen Gegenstand möglichst fein in Einzelteile zu zerlegen.

Gesucht wird eine **möglichst abstrakte, tragende und generative Basis**:

* wenige Elemente,
* möglichst wenig Redundanz,
* klare Beziehungen,
* hohe Wiederverwendbarkeit,
* und genügend Struktur, um das relevante Verhalten des ursprünglichen Systems zu erhalten oder zu rekonstruieren.

Das Ergebnis soll einem **Skelett** ähneln:

stark reduziert, aber nicht verstümmelt.

Die konkrete Ausprägung verschwindet weitgehend.
Die tragende Struktur bleibt.

---

## Warum „Refactoring“?

Der Begriff stammt aus der Softwareentwicklung.

Beim Refactoring wird die innere Struktur eines Systems verändert, während sein relevantes äußeres Verhalten erhalten bleibt.

Etwas Ähnliches geschieht hier mit Problemräumen, Modellen und Begriffssystemen.

Ein komplexer Gegenstand wird:

* zerlegt,
* neu geschnitten,
* auf Redundanz geprüft,
* abstrahiert,
* auf tragende Beziehungen reduziert,
* und gegebenenfalls aus einer kleineren Basis neu konstruiert.

Das Ziel ist nicht bloße Vereinfachung.

Das Ziel ist:

> **Maximale Abstraktion bei Erhalt relevanter Struktur.**

---

# Ausgangspunkt

Viele komplexe Systeme erscheinen zunächst als große Ansammlung von:

* Dingen,
* Eigenschaften,
* Sonderfällen,
* Begriffen,
* Ereignissen,
* Regeln,
* Wechselwirkungen.

Eine gute Analyse versucht nicht, diese Komplexität einfach vollständig abzubilden.

Sie fragt:

> Welche Unterschiede tragen tatsächlich?

> Welche Beziehungen bestimmen relevante Folgen?

> Welche Variablen sind unabhängig?

> Welche Elemente sind nur Varianten derselben tieferen Struktur?

> Was kann entfernt werden, ohne dass relevante Erklärungskraft verloren geht?

> Welche wenigen Strukturen reichen aus, um viele konkrete Fälle wieder zu erzeugen?

Eine gute Zerlegung ist damit zugleich eine Form von **Kompression**.

Aber nicht jede Kompression ist gut.

Wenn tragende Struktur verloren geht, wurde nicht abstrahiert, sondern verstümmelt.

---

# Szene, Folge, Skelett

Ein möglicher Ausgangspunkt ist die Betrachtung von **Szenen**.

Eine Szene enthält Elemente und Beziehungen, aus denen eine bestimmte Folge oder Konsequenz zu erwarten ist.

Für die Analyse wird gefragt:

> Welche Veränderungen an der Szene verändern die relevante Folge?

Was verändert werden kann, ohne die relevante Folge wesentlich zu verändern, ist bezüglich dieser Fragestellung wahrscheinlich **Detail**.

Was nicht entfernt oder verändert werden kann, ohne dass sich die Folge ändert, gehört wahrscheinlich zur **tragenden Struktur**.

Daraus ergibt sich ein einfaches Grundschema:

```text
Szene
↓
interessierende Folge bestimmen
↓
Elemente und Beziehungen variieren
↓
folgenneutrale Details entfernen
↓
tragende Relationen erhalten
↓
Strukturskelett
```

Die Abstraktion ist dabei immer bezogen auf eine Fragestellung.

Dieselbe Szene kann für unterschiedliche Folgen unterschiedliche Skelette besitzen.

---

# Begriffe als komprimierte Strukturen

Ein Begriff wird hier nicht primär als Wort verstanden.

Ein Begriff kann als **komprimiertes Relationsmuster** betrachtet werden.

Wenn dieselbe tragende Struktur in unterschiedlichen konkreten Szenen wiederkehrt, kann sie als eigene Einheit behandelt werden.

Irgendwann lohnt es sich, ihr einen Namen zu geben.

Dann wird aus:

```text
vielen konkreten Fällen
↓
gemeinsame tragende Beziehungen
↓
wiederkehrendes Strukturmuster
↓
Begriff
```

Ein guter Begriff senkt kognitive Last.

Er macht eine komplexe Struktur als Einheit verfügbar.

Es ist dabei durchaus möglich, dass relevante Strukturtypen existieren, für die menschliche Sprache noch keinen guten Begriff besitzt.

---

# Generative Basis

Besonders interessant sind Zerlegungen, deren Elemente nicht nur beschreiben, sondern **erzeugen** können.

Gesucht wird daher nicht einfach eine Liste wichtiger Eigenschaften, sondern möglichst eine Menge von Strukturen oder Operatoren, aus deren Kombination komplexere Strukturen hervorgehen können.

Eine solche Basis sollte:

* möglichst klein,
* möglichst unabhängig,
* kombinierbar,
* wiederverwendbar,
* und generativ leistungsfähig sein.

Komplexität soll möglichst aus der **Komposition einfacher Teile** entstehen und nicht bereits in unscharfen Grundbegriffen versteckt sein.

---

# Forschungsfragen

## R1 – Qualitätsproblem

> **Was kennzeichnet eine gute Zerlegung eines komplexen Systems?**

Vorläufige Kriterien sind:

### Abstraktion

Die Darstellung enthält möglichst wenig konkrete Ausprägung.

### Strukturerhalt

Für die interessierende Fragestellung relevante Beziehungen und Folgen bleiben erhalten.

### Minimalität

Kein Bestandteil kann entfernt werden, ohne relevante Ausdrucks- oder Erklärungskraft zu verlieren.

### geringe Redundanz

Verschiedene Elemente der Basis leisten tatsächlich Verschiedenes.

### Orthogonalität

Die gewählten Schnitte erfassen möglichst unabhängige Dimensionen.

### Kompositionalität

Aus den Basiselementen lassen sich komplexere Strukturen erzeugen.

### Rekonstruktionskraft

Wesentliche Eigenschaften oder Fälle des ursprünglichen Systems können aus der Basis wiedergewonnen werden.

### Transferfähigkeit

Dieselben Strukturen funktionieren in unterschiedlichen konkreten Szenen oder Domänen.

### Operationalisierbarkeit

Mit den gefundenen Elementen kann tatsächlich gearbeitet werden:

analysieren, unterscheiden, konstruieren, prüfen, simulieren oder entscheiden.

---

## R2 – Suchproblem

> **Wie findet man eine solche Zerlegung?**

Eine Vermutung lautet:

Bestimmte allgemeine Strukturachsen können die Suche beschleunigen.

Beispiele:

* Relation
* Übergang
* Zustand
* Perspektive
* Skala
* Zeit
* Rückkopplung
* Invarianz
* Variation
* Grenze
* Kontext
* Abhängigkeit
* Komposition
* Gegenfaktum

Diese Achsen sollen keine Ontologie darstellen.

Sie sind zunächst **Suchwerkzeuge**.

Ihre Aufgabe ist nicht, jedem Gegenstand dieselbe Struktur aufzuzwingen.

Sie sollen helfen, relevante Schnitte zu finden.

Eine gute Suchmethode muss deshalb auch erkennen können:

> Diese Achse bringt hier keinen zusätzlichen Erkenntnisgewinn.

Oder:

> Hier fehlt offenbar eine bisher nicht vorhandene Achse.

---

## R3 – Lernproblem

> **Kann ein Verfahren seine eigene Menge von Analyseoperatoren verbessern?**

Dazu müsste es nicht nur Ergebnisse speichern, sondern auch seine Suchgeschichte:

* Welche Zerlegung wurde versucht?
* Welche Operatoren wurden verwendet?
* Was wurde dadurch sichtbar?
* Was blieb unerklärt?
* Welche Operatoren erwiesen sich als redundant?
* Welche neuen Unterscheidungen waren nötig?
* Welche Zerlegungen funktionierten über mehrere Domänen hinweg?

Daraus könnte ein rekursiver Prozess entstehen:

```text
Analyse
↓
Basis finden
↓
Basis testen
↓
Fehler und Redundanz erkennen
↓
Operatoren verändern
↓
erneut testen
↓
Refactoring des Refactoring-Verfahrens
```

Das Verfahren würde damit seinen eigenen epistemischen Werkzeugkasten **refactoren**.

---

# Mögliche Tests

Eine Zerlegung kann unter anderem durch folgende Operationen geprüft werden:

## Entfernungstest

Was geht verloren, wenn ein Element entfernt wird?

Wenn nichts Relevantes verloren geht, war es vermutlich nicht fundamental.

## Ersetzungstest

Kann ein Element vollständig durch andere Elemente ersetzt werden?

Dann ist es möglicherweise abgeleitet oder redundant.

## Orthogonalitätstest

Erzeugen zwei Elemente tatsächlich verschiedene Schnitte?

Oder unterscheiden sie sich hauptsächlich sprachlich?

## Variationstest

Welche Veränderung eines Elements verändert die relevante Folge?

## Rekonstruktionstest

Lässt sich das relevante Verhalten des ursprünglichen Systems aus der reduzierten Basis wieder erzeugen?

## Transfertest

Taugt dieselbe Basis auch für andere konkrete Szenen?

---

# Verhältnis zur DFT

Dieser Forschungsstrang ist aus Arbeiten an der **Differenzfluss-Theorie (DFT)** hervorgegangen.

Die DFT lieferte unter anderem:

* allgemeine Strukturachsen,
* den Blick auf Unterschiede und Beziehungen,
* Rekursion und Rückkopplung,
* Perspektivität,
* Stabilität und Dynamik,
* Abstraktion über Skalen,
* sowie verschiedene Versuche, komplexe Gegenstände auf kleine operative Basen zurückzuführen.

Die hier untersuchte Methode setzt jedoch die starken metaphysischen Behauptungen der DFT **nicht voraus**.

Es genügt die schwächere Arbeitshypothese:

> **Es gibt wiederkehrende strukturelle Achsen und Konstruktionsprinzipien, deren Kenntnis die Zerlegung komplexer Problemräume erleichtern kann.**

Ob diese Ähnlichkeiten darauf beruhen, dass Wirklichkeit tatsächlich aus denselben fundamentalen Prinzipien konstruiert ist, bleibt eine weitergehende und hier nicht notwendige Frage.

Die DFT kann deshalb zugleich:

* Herkunft dieses Forschungsstrangs,
* Quelle möglicher Operatoren,
* und selbst Untersuchungsgegenstand des Refactorings sein.

---

# Die DFT als erster Testfall

Ein naheliegender erster Gegenstand ist die DFT selbst.

Die Frage lautet:

> **Sind die gegenwärtigen DFT-Begriffe primitive Operatoren, emergente Strukturen oder lediglich menschlich gut lesbare Projektionen einer tieferen relationalen Basis?**

Erste Versuche deuten darauf hin, dass Begriffe wie:

* Differenz,
* Beziehung,
* Prozess,
* Zeit,
* Rekursion,
* Stabilität,
* Struktur,
* Selbstbezug,
* Evolution,
* Erinnerung,
* Kognition

nicht notwendig auf derselben Ebene liegen.

Ein möglicher tieferer Kandidat ist derzeit:

> **gerichtete Relation + Komposition**

innerhalb eines operativ geschlossenen Raumes, in dem auch erzeugte Strukturen wieder als Operanden auftreten können.

Ob diese Basis trägt, ist offen.

Sie ist ein Forschungsgegenstand, kein Axiom.

---

# Arbeitshaltung

Dieses Projekt versucht nicht, vorhandene Modelle zu bestätigen.

Eine gute Faktorisierung darf frühere Begriffe zerstören.

Ein erfolgreicher Test kann ergeben:

* Ein angenommener Grundbegriff ist redundant.
* Zwei scheinbar verschiedene Operatoren sind dieselbe Struktur.
* Eine bisher fundamentale Kategorie ist emergent.
* Eine wichtige Dimension fehlt.
* Eine schöne Zerlegung funktioniert außerhalb ihres Ursprungsbereichs nicht.
* Ein bislang namenloses Strukturmuster erweist sich als tragend.

Auch Widerlegung ist Erkenntnisgewinn.

Das Ziel ist nicht, Recht zu behalten.

Das Ziel ist, bessere Schnitte zu finden.

---

# Kurzform

**R1**

> Was ist eine gute Zerlegung?

**Antwortkandidat:**

> Eine möglichst abstrakte, minimale und generative Struktur, die das für die Fragestellung Wesentliche erhält.

**R2**

> Wie findet man sie?

**Antwortkandidat:**

> Durch systematisches Schneiden, Variieren, Vergleichen, Abstrahieren und Prüfen entlang allgemeiner Strukturachsen.

**R3**

> Kann das Verfahren selbst lernen?

**Antwortkandidat:**

> Indem erfolgreiche und gescheiterte Zerlegungen zur Veränderung des eigenen Operatorenraums verwendet werden.

---

# Leitfrage

> **Wie refactort man einen komplexen Problemraum auf eine möglichst abstrakte generative Basis, ohne relevante Struktur zu verlieren?**

Das ist der Gegenstand dieses Verzeichnisses.
