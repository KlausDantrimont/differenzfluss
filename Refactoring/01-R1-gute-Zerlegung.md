# R1 – Was kennzeichnet eine gute Zerlegung eines komplexen Systems?

## Status

Vorläufig beantwortete Forschungsfrage.

Diese Notiz formuliert die derzeitige Arbeitsantwort auf **R1**. Sie ist kein endgültiges Axiom, sondern eine belastbare Definition, auf der die weiteren Fragen zur **Suche nach guten Zerlegungen (R2)** und zum **Lernen bzw. Refactoring des eigenen Operatorenraums (R3)** aufbauen können.

---

## 1. Ausgangsfrage

> **Was kennzeichnet eine gute Zerlegung eines komplexen Systems?**

Eine Zerlegung ist hier nicht einfach die Aufteilung eines Systems in möglichst viele Bestandteile.

Gesucht wird eine möglichst kleine, abstrakte und tragende Struktur, in der das für eine bestimmte Fragestellung Wesentliche erhalten bleibt.

Das Bild dafür ist ein **Skelett**:

* stark reduziert,
* frei von möglichst vielen zufälligen Details,
* aber noch tragfähig,
* und im Idealfall geeignet, die relevante Leistung des ursprünglichen Systems wieder hervorzubringen.

---

## 2. Vorläufige Definition

> **Eine gute Zerlegung eines komplexen Systems ist bezüglich einer bestimmten relevanten Leistung eine möglichst abstrakte Darstellung mit möglichst wenig funktionaler Redundanz, die genügend Struktur erhält, um diese Leistung zu erkennen, zu erklären oder – im stärksten Fall – zu generieren.**

Kurzform:

> **Minimale Struktur bei maximaler relevanter Rekonstruktionskraft.**

Oder noch anschaulicher:

> **So wenig Struktur wie möglich, so viel wie nötig, um das Wesentliche wieder hervorzubringen.**

---

## 3. Das „bezüglich“ ist fundamental

Es gibt nicht notwendig **die eine richtige Zerlegung** eines Systems.

Eine Zerlegung ist immer auf eine Fragestellung, eine Perspektive oder eine relevante Leistung bezogen.

Dasselbe System kann deshalb verschiedene tragfähige Skelette besitzen.

Ein Motor kann beispielsweise zerlegt werden bezüglich:

* Kraftübertragung,
* Wärmefluss,
* Regelung,
* Fehlerdiagnose,
* Fertigung,
* Wartung.

Jede dieser Fragen setzt andere Relevanzen.

Damit gilt:

> **Die Frage setzt den Kontext des Schnitts.**

Ohne Angabe dessen, was erhalten, erklärt oder erzeugt werden soll, ist „gute Zerlegung“ unterbestimmt.

---

## 4. Relevante Leistung

Der Ausdruck **relevante Leistung** ist allgemeiner als „Folge“ oder „Konsequenz“.

Eine Leistung kann beispielsweise sein:

* ein bestimmtes Verhalten zu erzeugen,
* eine Folge vorherzusagen,
* einen Zustand zu stabilisieren,
* Fälle zu unterscheiden,
* einen Sachverhalt zu erklären,
* eine Entscheidung zu ermöglichen,
* eine Klasse von Szenen zu erkennen,
* ein System zu rekonstruieren.

Die relevante Leistung bildet die **Nebenbedingung der Abstraktion**.

Man darf entfernen, vereinfachen und zusammenfassen – aber nur so lange, wie die für die Fragestellung relevante Leistung erhalten bleibt.

---

## 5. Drei Stufen des Verständnisses

Eine Zerlegung kann unterschiedlich viel leisten.

### 5.1 Erkennen

Die schwächste, aber bereits nützliche Stufe lautet:

> **Ich kann erkennen, wann eine bestimmte Struktur vorliegt.**

Eine diagnostische Basis erlaubt es, Fälle zu klassifizieren, Muster wiederzuerkennen oder relevante Strukturen sichtbar zu machen.

Das ist bereits wertvoll, auch wenn das System noch nicht vollständig verstanden oder reproduziert werden kann.

### 5.2 Erklären

Die stärkere Stufe lautet:

> **Ich kann angeben, welche Teile und Relationen für die relevante Leistung verantwortlich sind.**

Damit wird aus bloßer Wiedererkennung ein Strukturmodell.

Die Zerlegung zeigt nicht nur, **dass** eine Struktur vorliegt, sondern **wodurch** sie ihre relevante Leistung erbringt.

### 5.3 Generieren

Die stärkste Stufe lautet:

> **Ich kann aus den gefundenen Teilen und Relationen die relevante Leistung prinzipiell wieder hervorbringen.**

Generativität ermöglicht systematische Tests:

* Teile entfernen,
* Relationen verändern,
* Elemente ersetzen,
* Bedingungen variieren,
* neue Kombinationen erzeugen,
* Folgen beobachten.

Damit wird die Zerlegung experimentierbar.

Generieren ist deshalb eine besonders starke Form von Verständnis.

Die drei Stufen bilden eine vorläufige Leistungsleiter:

```text
Erkennen
   ↓
Erklären
   ↓
Generieren
```

Eine diagnostische Basis kann bereits gut sein.
Eine generative Basis liefert jedoch stärkere Evidenz dafür, dass die tragende Struktur tatsächlich getroffen wurde.

---

## 6. Kernkriterien einer guten Zerlegung

### 6.1 Bezug auf eine relevante Leistung

Die Zerlegung muss angeben, **bezüglich welcher Leistung** sie optimiert wird.

Ohne diesen Bezug ist nicht entscheidbar, was relevant und was Detail ist.

### 6.2 Abstraktion

Alles, was variiert werden kann, ohne die relevante Leistung zu verändern, darf grundsätzlich wegabstrahiert werden.

Eine gute Zerlegung enthält möglichst wenig konkrete Oberfläche und möglichst viel tragende Struktur.

### 6.3 Strukturerhalt

Abstraktion darf die relevante Leistung nicht zerstören.

Die reduzierte Struktur muss mindestens noch ermöglichen, die betreffende Leistung zu erkennen oder zu erklären; im stärkeren Fall muss sie sie rekonstruieren können.

### 6.4 Minimalität

Kein Bestandteil der Basis sollte entfernbar sein, ohne dass relevante Leistung verloren geht.

Ein Bestandteil, dessen Entfernung nichts Wesentliches verändert, ist wahrscheinlich kein tragendes Element dieser Zerlegung.

### 6.5 Möglichst geringe funktionale Redundanz

Verschiedene Basiselemente sollten möglichst unterschiedliche strukturelle Beiträge leisten.

Das Kriterium lautet bewusst **nicht** vollständige Orthogonalität.

Reale Systeme können gekoppelte Funktionen besitzen. Eine zu strenge Forderung nach Orthogonalität würde möglicherweise eine mathematische Sauberkeit erzwingen, die der Gegenstand selbst nicht besitzt.

Gesucht wird daher:

> **möglichst wenig funktionale Redundanz, nicht maximale formale Unabhängigkeit.**

### 6.6 Kompositionalität

Die Teile einer guten Basis sollten sich sinnvoll kombinieren lassen.

Die Komplexität des Systems soll möglichst aus den Beziehungen und Kombinationen einfacher Elemente entstehen und nicht bereits in unscharfen Grundelementen verborgen sein.

### 6.7 Rekonstruktionskraft

Je stärker sich die relevante Leistung des ursprünglichen Systems aus der reduzierten Basis wiedergewinnen lässt, desto stärker ist die Zerlegung.

Rekonstruktionskraft ist damit ein zentrales Gegenkriterium gegen übermäßige Vereinfachung.

---

## 7. Sekundäre Qualitätsmerkmale

Neben den Kernkriterien sind weitere Eigenschaften nützlich.

### Transferfähigkeit

Eine tragende Struktur sollte möglichst nicht nur einen einzigen konkreten Fall beschreiben.

Wenn dieselbe Basis in unterschiedlichen Szenen oder Domänen relevante Leistung erklären kann, steigt ihr Abstraktionswert.

### Robustheit

Kleine Variationen eines Falls sollten nicht sofort eine völlig neue Basis erzwingen.

Eine gute Zerlegung erfasst Invarianten und ist deshalb gegenüber irrelevanten Änderungen relativ stabil.

### Operationalisierbarkeit

Mit den gefundenen Elementen muss sich etwas tun lassen:

* unterscheiden,
* analysieren,
* prüfen,
* variieren,
* konstruieren,
* simulieren,
* entscheiden.

### Strukturelle Ökonomie

Eine Basis darf ihre scheinbare Einfachheit nicht dadurch erkaufen, dass ihre einzelnen Elemente selbst beliebig komplex werden.

Ein einzelner Operator `ALLES()` wäre formal minimal, aber epistemisch wertlos.

Die Komplexität soll sichtbar in der **Komposition einfacher Teile** liegen, nicht versteckt in undurchsichtigen Grundbegriffen.

---

## 8. Prüfverfahren

Aus den Kriterien ergeben sich einfache Tests.

### Entfernungstest

> Was geht verloren, wenn ein Element entfernt wird?

Geht keine relevante Leistung verloren, ist das Element wahrscheinlich nicht fundamental für diese Zerlegung.

### Ersetzungstest

> Kann ein Element vollständig durch andere Elemente ersetzt werden?

Falls ja, ist es möglicherweise abgeleitet oder redundant.

### Variationstest

> Welche Veränderungen eines Elements oder einer Relation verändern die relevante Leistung?

Leistungsneutrale Veränderungen weisen auf Details hin.
Leistungswirksame Veränderungen markieren Kandidaten für tragende Struktur.

### Kompositionstest

> Lassen sich aus den Basiselementen komplexere relevante Fälle bilden?

Eine bloße Liste wichtiger Merkmale ist noch keine generative Basis.

### Rekonstruktionstest

> Wie viel der relevanten Leistung des ursprünglichen Systems lässt sich aus der reduzierten Struktur wieder hervorbringen?

### Transfertest

> Funktioniert dieselbe Basis auch bei anderen konkreten Fällen derselben Leistungsklasse?

---

## 9. Stop-Regel

Abstraktion besitzt einen natürlichen Grenzpunkt.

> **Abstrahiere weiter, solange keine relevante Leistung verloren geht.**

Oder ausführlicher:

> Entferne, vereinige oder vereinfache Struktur so lange, wie die relevante Leistung weiterhin erkannt, erklärt oder – je nach Anspruch – generiert werden kann. Stoppe dort, wo weiteres Weglassen diese Fähigkeit wesentlich verschlechtert.

Damit liegt die optimale Zerlegung nicht bei maximaler Einfachheit allein.

Sie liegt an der Grenze zwischen:

```text
unnötiger Komplexität
        ↓
tragendem Skelett
        ↓
Verstümmelung
```

Gesucht wird das **minimal Tragende**.

---

## 10. Das Skelett

Der Begriff **Skelett** ist mehr als eine Metapher für „wenig“.

Ein Skelett ist:

* stark reduziert,
* relational organisiert,
* tragend,
* funktional,
* und geeignet, bestimmte Bewegungen oder Formen zu ermöglichen.

Übertragen auf komplexe Systeme bedeutet das:

> **Ein Strukturskelett ist die maximal abstrahierte relationale Struktur, die bezüglich einer relevanten Leistung noch trägt.**

Das Skelett ist daher nicht einfach das, was nach Weglassen übrigbleibt.

Es ist das, was nach Weglassen **noch etwas kann**.

---

## 11. R1 als Optimierungsproblem

Die Suche nach einer guten Zerlegung lässt sich vorläufig als mehrdimensionales Optimierungsproblem auffassen.

### Zu maximieren

* Abstraktion,
* Invarianz,
* Rekonstruktionskraft,
* Transferfähigkeit,
* Operationalisierbarkeit.

### Zu minimieren

* Anzahl der benötigten Basiselemente,
* Komplexität der Basiselemente,
* funktionale Redundanz,
* Sonderfälle,
* irrelevante Details.

### Unter der Nebenbedingung

> **Die für die Fragestellung relevante Leistung muss erhalten bleiben.**

Es ist nicht zu erwarten, dass alle Kriterien gleichzeitig ein eindeutiges mathematisches Optimum besitzen.

Sie bilden zunächst einen Qualitätsrahmen für den Vergleich verschiedener Zerlegungen.

---

## 12. Vorläufige Antwort auf R1

> **Eine gute Zerlegung eines komplexen Systems ist eine bezüglich einer bestimmten relevanten Leistung maximal abstrahierte, möglichst wenig funktional redundante und strukturell ökonomische Basis, die genügend relationale Struktur erhält, um die relevante Leistung mindestens zu erkennen und zu erklären und im stärksten Fall generativ zu rekonstruieren.**

Ihre Qualität wächst mit:

* Abstraktion,
* Strukturerhalt,
* Minimalität,
* geringer funktionaler Redundanz,
* Kompositionalität,
* Rekonstruktionskraft,
* Transferfähigkeit,
* Operationalisierbarkeit.

Die stärkste Prüfung einer solchen Basis besteht darin, aus ihr die relevante Leistung wieder erzeugen und durch gezielte Variation systematisch untersuchen zu können.

---

## 13. Kurzform

> **R1: Was ist eine gute Zerlegung?**
>
> Ein bezüglich einer relevanten Leistung möglichst abstraktes Strukturskelett mit möglichst wenig funktionaler Redundanz, das genügend Struktur erhält, um die Leistung zu erkennen, zu erklären oder – im stärksten Fall – zu generieren.

Oder:

> **So wenig Struktur wie möglich. So viel wie nötig. Und genug, um das Wesentliche wieder hervorzubringen.**

---

## Nächster Schritt

Mit R1 liegt ein vorläufiger Qualitätsmaßstab vor.

Damit kann R2 präziser gestellt werden:

> **Wie findet man systematisch eine Zerlegung, die diese Kriterien möglichst gut erfüllt?**
