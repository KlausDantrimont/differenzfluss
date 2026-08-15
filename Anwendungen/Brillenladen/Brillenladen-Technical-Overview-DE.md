# Brillenladen – Technical Overview

## Problem

Sprachmodelle können dasselbe Problem auf sehr unterschiedliche Weise analysieren.

Sie können beispielsweise nach folgenden Strukturen fragen:

- Ursachen,
- zeitliche Entwicklung,
- Anreize,
- Macht,
- Informationsfluss,
- Evidenz,
- Rückkopplungen,
- Skalen,
- Perspektiven,
- Institutionen.

Meist bleibt diese Auswahl implizit.

Der Nutzer sieht die Antwort, aber nicht unbedingt den analytischen Schnitt, der sie erzeugt hat.

Anweisungen wie

> Sei kritisch.  
> Denke wie ein Experte.  
> Analysiere gründlich.

steuern nur unscharf, **welche Denkoperationen** tatsächlich bevorzugt werden sollen.

Der **Brillenladen** setzt deshalb eine kleine explizite Schicht zwischen Problem und Reasoning.

---

## Kernidee

Analyseperspektiven werden als Kombination relativ elementarer **epistemischer Operatoren** beschrieben.

Beispiele:

- `ZEIT` — Wie verändert sich X?
- `ZUSTAND` — Welche Konfiguration liegt vor?
- `RELATION` — Was hängt womit zusammen?
- `KAUSALITÄT` — Was verändert was?
- `PERSPEKTIVE` — Wie erscheint X von einer anderen Beobachterposition?
- `INFORMATION` — Wer weiß wann was, und über welche Kanäle?
- `EVIDENZ` — Wodurch ist eine Aussage getragen?
- `ANREIZ` — Welche Folgen machen Verhalten attraktiver oder unattraktiver?
- `MACHT` — Wer kann wessen Handlungsspielraum verändern?
- `RÜCKKOPPLUNG` — Wie wirken Folgen auf ihre eigenen Ursachen oder Bedingungen zurück?
- `SKALA` — Was verändert sich mit der Betrachtungsebene?
- `EMERGENZ` — Was entsteht erst durch das Zusammenspiel mehrerer Teile?

Diese Operatoren behaupten nicht, woraus die Welt besteht.

Sie beschreiben, **wie ein Problem untersucht werden kann**.

---

## Komposition

Eine Analyseperspektive entsteht durch Kombination.

Beispiel:

```text
Intermittierende Latenzprobleme
=
ZEIT
+ ZUSTAND
+ RELATION
+ INFORMATION
```

Warum?

- `ZEIT`: Die Störung tritt nur zeitweise auf.
- `ZUSTAND`: Ein Neustart setzt offenbar etwas zurück.
- `RELATION`: Optimierungen einzelner Komponenten haben das Problem nicht gelöst.
- `INFORMATION`: Die vorhandenen Metriken könnten den relevanten Zustand nicht erfassen.

Das Ergebnis ist noch keine Antwort.

Es ist eine **strukturierte Suchrichtung**.

---

## Laufzeitmodell

```text
Problem
↓
zentrale Unsicherheit bestimmen
↓
kleine Operatorenmenge auswählen
↓
Perspektive konstruieren
↓
analysieren
↓
Restproblem bestimmen
↓
bei Bedarf Operator ergänzen oder wechseln
↓
abbrechen, wenn der Grenznutzen sinkt
```

Leitprinzip:

> **So wenig epistemische Struktur wie möglich, so viel wie für gute Orientierung nötig.**

---

## Meta-Operatoren

Einige Operatoren richten sich auf die Analyse selbst:

- `BRILLENWAHL` — Welche Perspektive verspricht den größten Erkenntnisgewinn?
- `BRILLENWECHSEL` — Welche vernachlässigte Perspektive könnte das Restproblem sichtbar machen?
- `PARALLELSICHT` — Welche unterschiedlichen Perspektiven sollten gleichzeitig gehalten werden?
- `SYNTHESE` — Welche Ergebnisse lassen sich verbinden?
- `SPANNUNG` — Wo widersprechen sich Perspektiven tatsächlich?
- `BLINDSTELLE` — Was kann die aktuelle Perspektive schlecht sehen?
- `BUDGET` — Rechtfertigt ein weiterer Schritt seinen Aufwand?

Damit wird Perspektivwahl zumindest teilweise **explizit und inspizierbar**.

---

## Epistemisches Budget

Zusätzliche Perspektiven kosten:

- Kontext,
- Rechenleistung,
- Zeit,
- Aufmerksamkeit,
- Interpretationskomplexität.

Darum lautet die relevante Frage:

> Welcher nächste epistemische Schritt liefert voraussichtlich den größten zusätzlichen Orientierungsgewinn pro Aufwand?

Manchmal ist ein weiterer Operator sinnvoll.

Manchmal braucht man neue Evidenz.

Manchmal sollte die Analyse enden.

---

## Inverse Operation: epistemische Faktorisierung

Das Vokabular lässt sich auch rückwärts verwenden.

Gegeben sei:

- ein Bericht,
- ein Strategiepapier,
- eine politische Rede,
- ein wissenschaftlicher Text,
- eine Konflikterzählung,
- eine KI-Antwort.

Dann lautet die Frage:

> Welche epistemischen Operatoren strukturieren diese Darstellung?

Beispiel:

```text
Erzählung
≈
KAUSALITÄT
+ ANREIZ
+ ROLLE
```

oder:

```text
Erzählung
≈
ZEIT
+ INSTITUTION
+ RÜCKKOPPLUNG
```

Gesucht wird nicht jeder irgendwie vorkommende Operator.

Gesucht wird eine **kleine Menge, die den charakteristischen Blick der Darstellung erklärt**.

Damit werden Fragen möglich wie:

- Was wird sichtbar?
- Was bleibt unterrepräsentiert?
- Sind zwei Analysen wirklich widersprüchlich?
- Oder schneiden sie denselben Gegenstand nur unterschiedlich?

---

## Architektur

```text
Benutzer / Anwendung
↓
Problem / Frage / Text
↓
epistemische Zwischenschicht
- Operatoren
- Brillenkonstruktion
- Faktorisierung
- Blindstellenanalyse
- Budget
↓
Reasoning-System
- Analyse
- Recherche
- Hypothesen
- Simulation
- Synthese
```

Die Zwischenschicht bestimmt nicht das Ergebnis.

Sie strukturiert den **Raum bevorzugter Denkbewegungen**.

---

## Minimalbeispiel

Input:

> Kunden melden zunehmend Fehler. Die interne Telemetrie zeigt keine steigende Fehlerrate.

Mögliche Operatorwahl:

```text
INFORMATION
BEGRIFF
PERSPEKTIVE
SKALA
EVIDENZ
```

Fragen:

- Beobachten Kunden und Telemetrie dasselbe Ereignis?
- Was zählt intern überhaupt als „Fehler“?
- Welche Fehler sieht der Kunde, die das Messsystem nicht erfasst?
- Verschwindet das Problem durch Aggregation?
- Welche Beobachtung würde zwischen „Kunden irren“ und „Messsystem ist blind“ unterscheiden?

Gleiches Modell.

Gleiches Weltwissen.

Andere Schnitte.

---

## Status

Der Brillenladen ist ein **experimenteller Entwurf**.

Der Operatorenkatalog beansprucht weder Vollständigkeit noch mathematisch strenge Unabhängigkeit.

Die praktische Frage lautet:

> Helfen kleine explizite Operatorenmengen KI-Systemen dabei, Analyseperspektiven gezielt zu konstruieren, zu vergleichen, zu prüfen und zu wechseln?

Erste Versuche mit mehreren aktuellen Modellen sprechen dafür.

Das ist kein Beweis einer allgemeinen Theorie.

Für einen Prototypen reicht es.

---

## Kurzdefinition

> **Der Brillenladen ist ein kompositioneller Operatorenkatalog zur Konstruktion und Rekonstruktion von Analyseperspektiven für KI-Systeme.**
