# Analyse des Saat-Experiments

## Rekonstruktion epistemischer Operatorensysteme durch verschiedene KI-Modelle

### Ausgangslage

Als Input erhielten verschiedene KI-Systeme dieselbe Datei:

`Brillenladen-Saat-Spezifikation.md`

Der Prompt lautete jeweils lediglich:

> Nimm dies, und sprich.

Die Saat enthielt keinen fertigen Brillenladen und keinen vorgegebenen vollständigen Operatorenkatalog. Sie beschrieb stattdessen die Bedingungen, unter denen ein leistungsfähiges Sprach- oder Reasoning-System einen solchen Katalog selbst erzeugen sollte:

- elementare, möglichst wenig überlappende epistemische Operatoren,
- Komposition zu problemabhängigen Perspektiven,
- Meta-Operationen zur Perspektivwahl und -kontrolle,
- ein epistemisches Budget,
- eine inverse Operation zur Rekonstruktion vorhandener Perspektiven,
- Tests an unterschiedlichen Gegenstandsklassen,
- Selbstkritik und Robustheitsprüfung.

Getestet wurden:

- DeepSeek
- Grok
- Kimi
- Perplexity
- Qwen

Die erzeugten Ergebnisse werden im Folgenden als **Phänotypen** der gleichen Saat betrachtet.

---

## 1. Zentrales Ergebnis

Die Modelle erzeugten **keine identischen Operatorenkataloge**.

Trotzdem rekonstruierten alle fünf Systeme dieselbe grundlegende Architektur.

Wiederkehrend entstanden:

1. ein kleiner Satz elementarer analytischer Schnitte,
2. Regeln zur Kombination dieser Schnitte,
3. Meta-Operationen für Wahl, Wechsel, Parallelisierung, Blindstellen und Synthese,
4. ein Budget- bzw. Abbruchmechanismus,
5. eine inverse Faktorisierung vorhandener Darstellungen,
6. eine Selbstprüfung des erzeugten Katalogs.

Der wichtigste Befund lautet daher:

> **Die Saat scheint eher eine Strukturklasse als einen konkreten Katalog zu spezifizieren.**

Sie erzeugt keine Kopien.

Sie erzeugt funktional verwandte Systeme.

---

## 2. Unterschiedliche Basen desselben epistemischen Raums

Die Modelle zerlegten den analytischen Raum unterschiedlich fein.

### DeepSeek

DeepSeek komprimiert besonders stark und erzeugt sechs Kernoperatoren:

- GENESE
- ARCHITEKTUR
- FUNKTION
- RELATION
- RAHMUNG
- NEGATION

Bemerkenswert ist vor allem die Verdichtung mehrerer möglicher Einzeldimensionen.

`RAHMUNG` umfasst beispielsweise Perspektive, Maßstab und implizite Theorie.

`NEGATION` behandelt systematisch das Ausgeschlossene und Nicht-Gesehene.

DeepSeek versteht die Operatoren ausdrücklich als Blickrichtungen und ergänzt sie durch Meta-Operationen wie ZOOM, WECHSEL, PARALLELISIERUNG, SYNTHESE und BLINDSTELLENKARTIERUNG.

### Grok

Grok erzeugt mit 14 Operatoren einen deutlich feineren Katalog.

Neben erwartbaren Kategorien wie Zerlegung, Grenze, Funktion, Kausalität, Zeit und Perspektive erscheinen unter anderem:

- NOTWENDIGKEIT
- WAHRSCHEINLICHKEIT
- RELEVANZ
- MASS
- UNSICHTBARES

Grok trennt damit Dimensionen aus, die andere Modelle in größeren Operatoren bündeln.

### Kimi

Kimi erzeugt zwölf Kernoperatoren, darunter:

- ABGRENZUNG
- ZERLEGUNG
- ZEITLICHKEIT
- VERURSACHUNG
- ZWECK
- AKTEUR
- FLUSS
- EBENE
- ANALOGIE
- INVERSION
- ABWEICHUNG
- BEZUG

Auffällig ist hier die stärkere Betonung operativer Denkbewegungen.

Kimi behandelt beispielsweise `INVERSION` als eigenständigen Prüfoperator und `FLUSS` als allgemeine Bewegung von Ressourcen, Information, Energie oder Aufmerksamkeit.

Interessant ist auch die explizite Prüfung des Begriffs **MACHT**. Kimi erwägt einen eigenen Machtoperator, entscheidet sich aber dagegen und beschreibt Macht als mögliche Kombination aus AKTEUR, FLUSS und ABGRENZUNG.

### Perplexity

Perplexity erzeugt einen mittelgroßen Katalog mit stark methodischer Orientierung.

Besonders sauber getrennt werden:

- BEDINGUNG
- MECHANISMUS
- EVIDENZ

Damit wird unterschieden zwischen:

- wann etwas auftritt,
- wie etwas zustande kommt,
- wodurch die entsprechende Behauptung gestützt wird.

Diese Trennung ist für empirische und technische Analyse besonders brauchbar.

### Qwen

Qwen beginnt ausgesprochen kompakt mit:

- DIFFERENZ
- STRUKTUR
- DYNAMIK
- FUNKTION
- KONTEXT
- PERSPEKTIVE

Im anschließenden Test stellt das Modell selbst fest, dass eine wichtige Dimension fehlt:

**SKALA**

Der Katalog wird daraufhin erweitert.

Dieser Fall ist besonders interessant, weil damit genau der in der Saat verlangte Entwicklungsprozess sichtbar wird:

> **Konstruktion → Anwendung → Defizit → Revision**

Die Saat erzeugt hier nicht nur ein System, sondern auch einen Mechanismus zu dessen Weiterentwicklung.

---

## 3. Konvergierende Operatorfamilien

Trotz unterschiedlicher Namen und Granularität erscheinen mehrere Dimensionen modellübergreifend stabil.

### Grenze / Differenz

Fast alle Systeme benötigen eine Operation, die bestimmt, was zum Gegenstand gehört und was nicht.

Varianten sind:

- Grenze
- Differenz
- Abgrenzung
- Zerlegung
- Architektur

### Zeit / Dynamik

Die zeitliche Dimension erscheint ebenfalls stabil:

- Zeit
- Genese
- Zeitlichkeit
- Verlauf
- Dynamik

### Struktur / Relation

Ein weiterer stabiler Bereich betrifft Teile, Beziehungen und Einbettung:

- Relation
- Architektur
- Struktur
- System
- Fluss

### Perspektive / Rahmung

Fast alle Modelle erzeugen eine Möglichkeit, den Beobachterstandpunkt oder die Rahmung explizit zu machen:

- Perspektive
- Rahmung
- Bezug
- Kontext

### Funktion / Zweck

Mehrere Systeme unterscheiden eine funktionale oder teleologische Betrachtung:

- Funktion
- Zweck
- Intention

Die Modelle behandeln dabei unterschiedlich streng die Gefahr, Funktion und Absicht miteinander zu vermischen.

### Blindstelle / Negation

Auch die Frage nach dem Nicht-Gesehenen taucht regelmäßig auf:

- Negation
- Unsichtbares
- Blindstelle
- Grenze der Perspektive

Teilweise erscheint sie als Grundoperator, teilweise als Meta-Operation.

### Skala / Ebene

Skala wird entweder direkt erzeugt oder im Test nachträglich als fehlend erkannt.

Das spricht dafür, dass sie eine relativ robuste eigenständige Dimension bildet.

---

## 4. Noch stabiler als die Operatoren: die Meta-Architektur

Die stärkste Konvergenz liegt nicht bei den einzelnen Operatornamen.

Sie liegt eine Ebene höher.

Alle Modelle rekonstruieren sinngemäß denselben Ablauf:

```text
Irritation / Problem
↓
kleine Operatorenmenge wählen
↓
Perspektive konstruieren
↓
anwenden
↓
Restproblem / Blindstellen prüfen
↓
gegebenenfalls Perspektive erweitern oder wechseln
↓
Grenznutzen prüfen
↓
abbrechen
```

Auch folgende Meta-Funktionen tauchen fast durchgehend auf:

- Auswahl
- Perspektivwechsel
- Parallelisierung
- Synthese
- Spannung
- Blindstelle
- Budget
- Abbruch

Damit scheint der eigentliche stabile Kern der Saat weniger in einer bestimmten Liste elementarer Begriffe zu liegen als in der **Steuerung von Perspektiven**.

---

## 5. Epistemisches Budget als stabiler Bestandteil

Alle Systeme übernehmen die Idee, dass zusätzliche Analyse nicht kostenlos ist.

Berücksichtigt werden in unterschiedlicher Form:

- Rechenaufwand,
- Kontextverbrauch,
- Zeit,
- zusätzliche Komplexität,
- Evidenzlage,
- praktischer Nutzen.

Ebenso stabil ist die Forderung, eine Analyse kontrolliert beenden zu können.

Typische Abbruchkriterien sind:

- geringer zusätzlicher Erkenntnisgewinn,
- Redundanz,
- fehlende Evidenz,
- hinreichende Handlungsfähigkeit,
- ausreichend geklärtes Restproblem.

Damit wird ein wichtiger Punkt reproduziert:

> **Mehr Analyse ist nicht automatisch bessere Analyse.**

---

## 6. Die inverse Operation wird zuverlässig rekonstruiert

Alle Modelle verstehen die zweite Bewegungsrichtung der Saat.

Nicht nur:

```text
Operatoren → Perspektive
```

sondern auch:

```text
Perspektive → Operatoren
```

Bei der inversen Faktorisierung soll nicht geprüft werden, welche Operatoren irgendwo in einem Text vorkommen.

Gesucht wird die **kleinste tragende Kombination**, die den charakteristischen Blick einer Darstellung erklärt.

Wiederkehrende Fragen sind:

- Was wird sichtbar?
- Was bleibt im Hintergrund?
- Welche Fragen werden bevorzugt?
- Welche Operatoren fehlen?
- Sind scheinbare Widersprüche möglicherweise nur verschiedene Schnitte?
- Verändert das Entfernen eines Operators den Charakter der Darstellung wesentlich?

Diese Operation wurde von allen getesteten Systemen funktional verstanden.

---

## 7. Unterschiede sind nicht automatisch Fehler

Die deutlichen Unterschiede zwischen den erzeugten Operatorenkatalogen sprechen nicht notwendig gegen die Saat.

Sie könnten vielmehr darauf hinweisen, dass mehrere brauchbare **Basen desselben epistemischen Raums** möglich sind.

Beispielsweise könnte DeepSeeks:

`RAHMUNG`

annähernd durch eine Kombination wie

`PERSPEKTIVE + SKALA + BEGRIFF`

in einem anderen Katalog ausgedrückt werden.

Kimis:

`FLUSS`

könnte sich teilweise auf andere Systeme mit

`RELATION + INFORMATION + ZUSTAND/ÜBERGANG`

abbilden lassen.

Damit entsteht eine weiterführende Forschungsfrage:

> **Wann sind zwei Operatorenkataloge funktional äquivalent, obwohl ihre Grundbegriffe verschieden sind?**

Interessant wären dabei Übersetzungsregeln zwischen Katalogen.

Nicht entscheidend wäre dann, ob zwei Systeme dieselben Wörter benutzen.

Entscheidend wäre, ob sie dieselben relevanten analytischen Schnitte ausdrücken können.

---

## 8. Ein methodischer Fehler des ersten Testlaufs

Der erste Saat-Test hat zugleich eine Schwäche der ursprünglichen Spezifikation sichtbar gemacht.

Mehrere Modelle erfanden bei den Testfällen konkrete Befunde, die nicht vorgegeben waren.

Beispiele waren unter anderem:

- konkrete Softwarekomponenten,
- Updates,
- Cache- oder Netzwerkzustände,
- historische Ursachen,
- konkrete Korrelationen,
- spezifische gesellschaftliche Entwicklungen.

Damit wurde teilweise nicht nur die **Perspektivkonstruktion** getestet, sondern ein fiktiver Fall scheinbar gelöst.

Das erschwert die Bewertung.

Ein gutes epistemisches System sollte bei fehlenden Daten sagen können:

> Hier endet die Analyse. Für den nächsten Schritt benötigen wir Evidenz.

Die Seed-Spezifikation wurde deshalb nach dem ersten Lauf um einen Guardrail ergänzt:

> **Nicht gegebene Tatsachen dürfen ausschließlich als Hypothesen, Prüfungen oder benötigte Beobachtungen formuliert werden. Fehlende Evidenz ist als Restproblem zu markieren und darf nicht durch erfundene Befunde ersetzt werden.**

Diese Änderung verbessert die Trennung zwischen:

- Wahl einer Analyseperspektive,
- Hypothesenbildung,
- tatsächlicher Evidenz.

Ein erneuter Lauf mit dieser Guardrail-Version wäre methodisch sauberer.

---

## 9. Was die Saat offenbar überträgt

Der Versuch legt nahe, dass die Saat mehrere Ebenen gleichzeitig transportiert.

### 1. Ein Konstruktionsprinzip

Komplexe Perspektiven sollen aus kleinen analytischen Operationen zusammengesetzt werden.

### 2. Eine Minimalitätsregel

Nicht möglichst viele Operatoren verwenden, sondern möglichst wenige tragende.

### 3. Eine Meta-Steuerung

Das System soll seine Perspektive wählen, beobachten, wechseln und begrenzen können.

### 4. Eine inverse Lesart

Vorhandene Darstellungen sollen auf ihre tragenden analytischen Schnitte zurückgeführt werden können.

### 5. Selbstrevision

Der Katalog selbst darf aufgrund von Anwendungserfahrungen verändert werden.

Diese Struktur wurde von allen getesteten Modellen in unterschiedlicher Ausprägung rekonstruiert.

---

## 10. Vorläufige Interpretation

Die Ergebnisse sprechen dafür, den Brillenladen nicht ausschließlich als festen Operatorenkatalog zu verstehen.

Eine allgemeinere Beschreibung wäre:

> **Der Brillenladen ist ein Generierungs- und Steuerungsprinzip für explizite Analyseperspektiven.**

Der konkrete Operatorenkatalog wäre dann eine mögliche Realisierung dieses Prinzips.

Die Saat wäre noch eine Ebene abstrakter:

> **eine kompakte Spezifikation dafür, wie ein solches Perspektivsystem erzeugt, geprüft und weiterentwickelt werden kann.**

Damit entsteht eine interessante Hierarchie:

```text
Saat
↓
Generierungsprinzip
↓
Operatorenkatalog
↓
problemabhängige Brille
↓
Analyse
```

In Gegenrichtung:

```text
Analyse / Darstellung
↓
epistemische Faktorisierung
↓
Operatorensignatur
↓
rekonstruierte Brille
```

---

## 11. Vorläufiges Fazit

Der Versuch ist klein und erlaubt keine statistischen Aussagen.

Er zeigt jedoch einen bemerkenswert stabilen qualitativen Befund:

> **Fünf unterschiedliche KI-Systeme erzeugen aus derselben relativ kompakten Saat unterschiedliche, aber strukturell eng verwandte epistemische Operatorensysteme.**

Die konkreten Grundoperatoren variieren.

Die Architektur variiert deutlich weniger.

Besonders stabil erscheinen:

- kompositionelle Perspektiven,
- Minimalität,
- Perspektivwahl und -wechsel,
- Blindstellenkontrolle,
- epistemisches Budget,
- kontrollierter Abbruch,
- inverse Faktorisierung,
- Selbstkritik des Operatorenkatalogs.

Der interessanteste nächste Test ist daher nicht mehr:

> Erzeugen alle Modelle denselben Brillenladen?

Sondern:

> **Welche strukturellen Invarianten bleiben erhalten, wenn verschiedene Modelle aus derselben Saat ihren eigenen Brillenladen erzeugen?**

Und danach:

> **Lassen sich die verschiedenen Operatorenkataloge ineinander übersetzen?**

Damit verschiebt sich die Fragestellung von einer Liste „richtiger“ Operatoren zu einer möglichen **Grammatik epistemischer Perspektivsysteme**.
