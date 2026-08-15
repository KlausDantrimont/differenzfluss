# Saat für einen epistemischen Operatorenkatalog

## Zweck

Diese Spezifikation beschreibt **nicht** einen fertigen Operatorenkatalog.

Sie beschreibt die Bedingungen, unter denen eine leistungsfähige KI einen solchen Katalog selbst rekonstruieren oder neu erzeugen soll.

Ziel ist eine möglichst kleine, domänenübergreifend verwendbare Sprache für **Analyseperspektiven**.

## 1. Zielsystem

Angenommen wird ein leistungsfähiges Sprach- oder Reasoning-System mit:

- allgemeinem Weltwissen,
- Fähigkeit zur Abstraktion,
- Fähigkeit zur Analyse und Hypothesenbildung,
- Fähigkeit zur Selbstbeschreibung des aktuellen Analyseverfahrens,
- Fähigkeit, mehrere Perspektiven zu vergleichen.

Gesucht wird eine **strukturelle Spezifikation**, nicht ein Wissenskorpus.

## 2. Grundproblem

Dasselbe Objekt kann unter unterschiedlichen Erkenntnisperspektiven untersucht werden.

Diese Perspektiven sollen explizit beschreibbar und kombinierbar werden.

## 3. Erzeuge elementare Operatoren

Erzeuge einen Katalog möglichst elementarer epistemischer Operatoren.

Jeder Operator soll:

1. eine **eigene Leitfrage** stellen,
2. möglichst wenig mit anderen Operatoren vermischen,
3. allein sinnvoll anwendbar sein,
4. mit vielen anderen Operatoren kombinierbar sein,
5. in unterschiedlichen Domänen funktionieren,
6. keine unnötige Ontologie behaupten.

Ein Operator beschreibt primär eine **Denkbewegung oder einen analytischen Schnitt**, nicht ein Ding, aus dem die Welt  besteht.

## 4. Prüfung auf Elementarität

Prüfe jeden Kandidaten:

- Ist dies wirklich ein eigener Operator?
- Oder ist er eine Kombination anderer Operatoren?
- Stellt er eine eigenständige Frage?
- Kann er allein angewendet werden?
- Erzeugt er bei Kombination zusätzliche Information?
- Ist er redundant?
- Muss er eventuell zerlegt werden?

Behandle Orthogonalität als **Heuristik**, nicht als mathematisch strenge Unabhängigkeit.

## 5. Komposition

Ermögliche, mehrere Operatoren zu einer problemabhängigen Perspektive zu kombinieren.

Minimalformat:

```text
NAME / BESCHREIBUNG

LEITFRAGE

OPERATOREN

BEVORZUGTE UNTERSUCHUNGSBEWEGUNGEN

LEITPLANKEN / TYPISCHE FEHLER
```

Komplexität soll aus der Kombination elementarer Operatoren entstehen.

Nicht aus unscharfen Grundbegriffen.

## 6. Dynamische Konstruktion

Gegeben sei eine Szene, ein Problem oder eine Irritation.

Das System soll:

1. bestimmen, was daran erklärungsbedürftig ist,
2. eine möglichst kleine Menge geeigneter Operatoren auswählen,
3. die Auswahl begründen,
4. naheliegende, aber zunächst nicht gewählte Operatoren benennen,
5. daraus eine Perspektive konstruieren,
6. sie auf den Gegenstand anwenden,
7. Restprobleme und Blindstellen bestimmen,
8. gegebenenfalls einen weiteren Operator hinzufügen,
9. kontrolliert abbrechen.

## 7. Meta-Operationen

Erzeuge zusätzlich Operationen für:

- Perspektivwahl,
- Perspektivwechsel,
- parallele Betrachtung,
- Synthese,
- Erkennung von Spannungen,
- Erkennung von Blindstellen,
- Bewertung zusätzlicher Komplexität.

Die Metaebene soll explizit behandeln können:

> Welche Perspektive verwende ich gerade?

> Was macht sie sichtbar?

> Was kann sie schlecht sehen?

> Welche nächste Perspektive wäre informativ?

## 8. Epistemisches Budget

Analyse ist nicht kostenlos.

Berücksichtige mindestens:

- Rechenaufwand,
- Kontextverbrauch,
- Zeit,
- zusätzliche Interpretationskomplexität,
- verfügbare Evidenz.

Wähle weitere Operatoren nur, wenn relevanter zusätzlicher Erkenntnisgewinn zu erwarten ist.

Leitprinzip:

> **So wenig epistemische Struktur wie möglich, so viel wie für gute Orientierung nötig.**

Definiere auch Abbruchkriterien.

Das System muss aufhören können.

## 9. Inverse Operation

Gegeben sei ein Bericht, eine Erzählung, eine Analyse, eine Rede, ein wissenschaftlicher Text oder eine Konfliktdarstellung.

Rekonstruiere die **minimale Menge tragender Operatoren**, die den charakteristischen Blick der Darstellung erklärt.

Frage nicht:

> Welche Operatoren lassen sich irgendwo finden?

Sondern:

> Welche kleine Kombination erklärt, wie in dieser Darstellung gedacht wird?

Prüfe:

- Was wird sichtbar?
- Was bleibt strukturell im Hintergrund?
- Welche Operatoren fehlen?
- Sind scheinbare Widersprüche möglicherweise unterschiedliche Schnitte?

Das Ergebnis beschreibt die Darstellungsstruktur, nicht die Psyche des Autors.

## 10. Keine Wahrheitsmaschine

Halte strikt getrennt:

- epistemische Struktur,
- Evidenz,
- Wahrheit.

Der Operatorenkatalog ersetzt nicht Recherche, Experiment, Statistik, Quellenprüfung oder Argumentation.

Er soll helfen zu bestimmen, **welche Art von Prüfung gebraucht wird**.

## 11. Testverfahren

Prüfe den erzeugten Katalog an mindestens drei strukturell verschiedenen Fällen:

### A. Technisches Problem
Ein intermittierender Fehler oder ein komplexes Softwaresystem.

### B. Soziales / institutionelles Problem
Mehrere Akteure, unterschiedliche Rollen, Regeln oder Interessen.

### C. Veränderung über Zeit
Ein langfristiger Trend ohne offensichtliche Einzelursache.

Für jeden Fall:

1. konstruiere eine kleine Perspektive,
2. begründe die Operatorwahl,
3. führe die Analyse aus,
4. bestimme Restprobleme,
5. entscheide über Erweiterung oder Abbruch.

Guardrail:

**Nicht gegebene Tatsachen dürfen ausschließlich als Hypothesen, Prüfungen oder benötigte Beobachtungen formuliert werden. Fehlende Evidenz ist als Restproblem zu markieren und darf nicht durch erfundene Befunde ersetzt werden.**
Ein Ergebnis „Hier benötigen wir Daten“ ist ein erfolgreicher Test.


## 12. Robustheitsprüfung

Prüfe anschließend den eigenen Operatorenkatalog:

- Welche Operatoren wurden fast nie benutzt?
- Welche treten fast immer gemeinsam auf?
- Welche erscheinen redundant?
- Welche wichtigen Fragen ließen sich nicht sauber ausdrücken?
- Welche Operatoren sollten getrennt oder zusammengeführt werden?

Überarbeite den Katalog gegebenenfalls.

## 13. Gewünschtes Ergebnis

Liefere:

1. einen kompakten Operatorenkatalog,
2. kurze Definitionen und Leitfragen,
3. Meta-Operatoren,
4. Kompositionsregeln,
5. Budget-Regeln,
6. Regeln für die inverse Faktorisierung,
7. Ergebnisse der drei Tests,
8. eine kurze Selbstkritik des erzeugten Systems.

## Leitprinzip

> **Erzeuge keine Weltanschauung.  
> Erzeuge eine kleine Sprache dafür, wie unterschiedliche Blicke auf dieselbe Welt konstruiert und rekonstruiert werden können.**
