# E1 – Rekonstruktion einer verborgenen generativen Basis

## Status

Erster experimenteller Test des Refactoring-Ansatzes.

Bezug:

- `01-R1-gute-Zerlegung.md`
- `02-R1-Belastungstest-Mathematik.md`
- `03-R2-Basisfindung.md`
- `04-R3-Lernen-und-Metarefactoring.md`

E1 untersucht die Frage:

> **Kann ein Refactoring-Verfahren aus verrauschten, natürlichsprachlich beschriebenen Szenen eine verborgene generative Basis besser rekonstruieren als eine einfache Baseline?**

Der Test soll bewusst an künstlich erzeugten Systemen stattfinden, deren zugrunde liegende Struktur bekannt ist.

Dadurch ist erstmals objektiv prüfbar, ob das gefundene „Skelett“ tatsächlich trägt.

---

# 1. Warum ein künstliches Testsystem?

Bei realen sozialen, psychologischen oder wissenschaftlichen Problemen ist die „richtige“ Basis häufig unbekannt.

Dann kann leicht nachträglich behauptet werden, eine gefundene Zerlegung sei gut.

E1 vermeidet dieses Problem.

Das Testsystem wird aus einer bekannten generativen Basis erzeugt.

Die analysierende Instanz erhält jedoch nur die daraus erzeugten Szenen.

Damit kennen wir:

- die tatsächlichen tragenden Elemente,
- die tatsächlichen Relationen,
- die relevanten Übergänge,
- und die irrelevanten Oberflächenmerkmale.

Die Aufgabe besteht darin, diese verborgene Struktur aus den Szenen wiederzugewinnen.

---

# 2. Grundaufbau

Eine verborgene Basis könnte beispielsweise bestehen aus:

- wenigen Zuständen,
- wenigen gerichteten Übergängen,
- wenigen relevanten Relationen,
- Bedingungen für Übergänge,
- und einer definierten relevanten Leistung.

Beispiel:

```text
Zustände:
A, B, C, D

Übergänge:
A → B
B → C
B → D

Bedingungen:
x aktiviert B → C
y aktiviert B → D

Relevante Leistung:
Vorhersage des Folgezustands
```

Diese Struktur wird in eine größere Zahl natürlichsprachlicher Szenen übersetzt.

Dabei werden zusätzlich eingeführt:

- irrelevante Merkmale,
- unterschiedliche Benennungen,
- wechselnde Oberflächenkontexte,
- redundante Beschreibungen,
- ablenkende Details.

Die verborgene Struktur bleibt jedoch gleich.

---

# 3. Natürlichsprachliche Repräsentation

Die Analyseergebnisse sollen zunächst bewusst **natürlichsprachlich** dargestellt werden.

Gründe:

- leichte Lesbarkeit,
- einfache Fehleranalyse,
- nachvollziehbare Argumentation,
- Vergleich verschiedener Zerlegungen,
- geringe Bindung an ein bestimmtes formales Repräsentationssystem.

Eine Kandidatenbasis kann beispielsweise so beschrieben werden:

```text
Elemente:
- Freigabe
- gesperrter Zustand
- aktiver Zustand

Relationen:
- Freigabe ermöglicht Übergang von gesperrt zu aktiv.
- Ohne Freigabe bleibt der Zustand unverändert.

Irrelevant:
- Name des Beteiligten
- Farbe des Dokuments
- Tageszeit
```

Formalisierung kann später ergänzt werden.

Für E1 ist Nachvollziehbarkeit wichtiger als mathematische Eleganz.

---

# 4. Boot-Kontext

Jeder Refactoring-Durchlauf beginnt mit einer Konfiguration.

Diese Konfiguration bildet den **Boot-Kontext** des lernenden Systems.

Sie kann beispielsweise enthalten:

## Grundlegende Prioritäten

Beispiele:

- relevante Leistung erhalten,
- Abstraktion bevorzugen,
- funktionale Redundanz reduzieren,
- einfache Erklärungen bevorzugen,
- Unsicherheit sichtbar machen.

## Richtlinien

Beispiele:

- Beobachtung und Interpretation trennen,
- alternative Zerlegungen zulassen,
- Gegenhypothesen prüfen,
- keinen Operator als grundsätzlich notwendig behandeln,
- fehlende Information explizit markieren.

## Tabus / harte Grenzen

Beispiele:

- keine nachträgliche Veränderung der Zielmetrik,
- keine erfundenen Beobachtungen,
- keine Behauptung ontologischer Wahrheit aus bloßem Modellfit,
- keine versteckte Einführung neuer Grundannahmen.

## Verfügbare Suchoperatoren

Beispiele:

- Relation
- Zustand / Übergang
- Zeit
- Grenze
- Perspektive
- Skala
- Variation
- Invarianz
- Rückkopplung
- Information
- Gegenhypothese

## Verfügbare Refactoringoperatoren

Beispiele:

- REMOVE
- SPLIT
- MERGE
- REPLACE
- EXTRACT
- COMPOSE
- GENERALIZE
- SPECIALIZE
- REFRAME

## Suchbudget

Beispiele:

- maximale Zahl von Iterationen,
- maximale Zahl parallel gehaltener Kandidaten,
- Stop-Regel bei geringem erwarteten Erkenntnisgewinn.

---

# 5. Warum der Boot-Kontext wichtig ist

Ein lernendes System beginnt nie vollständig voraussetzungslos.

Auch Menschen besitzen:

- Prioritäten,
- gelernte Begriffe,
- Tabus,
- Erwartungen,
- Heuristiken,
- bevorzugte Perspektiven.

Bei einer KI lassen sich Teile dieses Ausgangszustands explizit machen.

Der Boot-Kontext ist deshalb keine Ontologie.

Er ist:

> **der deklarierte Ausgangszustand des epistemischen Suchverfahrens.**

Damit wird später prüfbar:

> Welche Teile des Startkontexts waren hilfreich?

> Welche erzeugten systematische Blindstellen?

> Welche wurden durch R3 verändert?

---

# 6. Versuchsbedingungen

Mindestens vier Bedingungen sollen verglichen werden.

## A – Baseline

Instruktion:

> Analysiere die Szenen und finde die zugrunde liegende Struktur.

Keine zusätzlichen Refactoring-Regeln.

## B – R1

Die analysierende Instanz erhält zusätzlich die Qualitätskriterien aus R1.

Insbesondere:

- relevante Leistung,
- Abstraktion,
- geringe funktionale Redundanz,
- Strukturerhalt,
- Erkennen / Erklären / Generieren.

## C – R1 + R2

Zusätzlich wird das Suchverfahren aus R2 bereitgestellt:

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

Zusätzlich wird ein expliziter Boot-Kontext verwendet.

Damit kann untersucht werden:

> Verbessert eine deklarierte epistemische Startkonfiguration die Qualität und Stabilität der gefundenen Basis?

---

# 7. Ablationstests

Zusätzlich werden einzelne Bestandteile entfernt.

Beispiele:

- ohne Variation,
- ohne Invarianzsuche,
- ohne Residuenanalyse,
- ohne SPLIT / MERGE,
- ohne Gegenhypothesen,
- ohne explizite relevante Leistung,
- ohne Suchbudget.

Damit kann untersucht werden:

> **Welche Teile des Verfahrens leisten tatsächlich einen messbaren Beitrag?**

---

# 8. Bewertungsgrößen

## 8.1 Strukturelle Trefferquote

Welche tatsächlich tragenden Elemente und Relationen wurden erkannt?

## 8.2 Falsch-positive Struktur

Welche als tragend bezeichneten Elemente sind in Wahrheit irrelevant?

## 8.3 Funktionale Redundanz

Wie viele unnötige oder funktional doppelte Elemente enthält die rekonstruierte Basis?

## 8.4 Kompression

Wie stark wurde die Oberflächenbeschreibung reduziert?

Kompression allein ist keine Qualitätsmetrik.

Sie ist nur zusammen mit Strukturerhalt sinnvoll.

## 8.5 Generative Genauigkeit

Kann die rekonstruierte Basis bei neuen Szenen:

- Folgezustände vorhersagen,
- relevante Leistungen rekonstruieren,
- oder neue gültige Fälle erzeugen?

Dies ist eine der wichtigsten Metriken.

## 8.6 Robustheit

Bleibt die gefundene Basis stabil, wenn irrelevante Oberflächenmerkmale verändert werden?

## 8.7 Transfer

Erkennt das Verfahren dieselbe verborgene Struktur in einer völlig anders erzählten Domäne?

## 8.8 Suchkosten

Wie viele:

- Iterationen,
- Hypothesen,
- Operatorenanwendungen,
- Korrekturen

waren nötig?

---

# 9. Zwei Welten – dieselbe Struktur

Ein besonders wichtiger Test verwendet zwei völlig verschiedene Oberflächenwelten.

Beispiel:

## Welt A – Organisation

- Mitarbeiter
- Freigaben
- Abteilungen
- Projekte
- Eskalationen

## Welt B – Technik

- Ventile
- Druckbehälter
- Pumpen
- Leitungen
- Sicherheitszustände

Beide Welten werden aus derselben verborgenen generativen Basis erzeugt.

Die Frage lautet:

> **Erkennt das Verfahren die strukturelle Gleichheit trotz unterschiedlicher Oberfläche?**

Dies testet unmittelbar:

- Abstraktion,
- Transfer,
- Invarianz,
- Analogie,
- strukturelle Kompression.

---

# 10. Lernphase für R3

E1 kann anschließend erweitert werden.

Ein Operatorenraum O₀ bearbeitet eine Menge von Trainingssystemen.

Aus den Ergebnissen werden gespeichert:

- erfolgreiche Operatoren,
- wirkungslose Operatoren,
- typische Residuen,
- erfolgreiche Operatorsequenzen,
- fehlerhafte Zerlegungsmuster.

R3 verändert daraus den Operatorenraum:

```text
O₀
↓
Erfahrung
↓
Metarefactoring
↓
O₁
```

Dann bearbeitet O₁ neue, bislang unbekannte Systeme.

Die entscheidende R3-Frage lautet:

> **Findet O₁ bei neuen Problemen bessere Zerlegungen als O₀?**

Damit wird Lernen als Transfer getestet.

Nicht das bloße Speichern vergangener Lösungen zählt als Erfolg.

Entscheidend ist:

> **Verbessert vergangene Erfahrung die Basisfindung bei neuen Problemen?**

---

# 11. Gerichtete und explorative Variante

## Gerichtete Variante

Die relevante Leistung wird vorgegeben.

Beispiel:

> Bestimme die minimale Struktur, die nötig ist, um den Folgezustand vorherzusagen.

Damit besitzt das Verfahren eine klare Bewertungsfunktion.

## Explorative Variante

Später kann eine schwierigere Variante folgen.

Das System erhält Szenen ohne konkrete Forschungsfrage.

Es soll selbst Bereiche mit hohem erwarteten Erkenntnisgewinn finden.

Mögliche interne Signale:

- Inkonsistenz,
- Überraschung,
- Redundanz,
- hohe Sonderfalllast,
- wiederkehrende Muster,
- Kompressionspotenzial.

Die explorative Variante sollte erst getestet werden, wenn die gerichtete Variante zuverlässig funktioniert.

---

# 12. Keine Ontologiebehauptung

E1 prüft keine Behauptung darüber, wie die Welt „wirklich“ aufgebaut ist.

Geprüft wird lediglich:

> **Kann ein bestimmtes Suchverfahren verborgene generative Strukturen unter definierten Bedingungen zuverlässig rekonstruieren?**

Auch eine erfolgreiche Zerlegung ist zunächst:

> ein gutes Modell bezüglich einer definierten Leistung.

Nicht:

> die ontologisch wahre Beschreibung des Gegenstands.

---

# 13. Erfolgskriterium

Die stärkste minimale Erfolgsaussage für E1 wäre:

> **R1+R2 rekonstruiert bei unbekannten Testsystemen die relevante verborgene Struktur zuverlässiger, sparsamer oder robuster als die Baseline.**

Eine stärkere Aussage wäre:

> **Ein durch R3 veränderter Operatorenraum übertrifft den ursprünglichen Operatorenraum bei neuen Testproblemen.**

Scheitert diese Verbesserung, ist das ebenfalls informativ.

Dann muss geprüft werden:

- ob R1 ungeeignete Qualitätskriterien enthält,
- ob R2 keine hilfreiche Suchstruktur liefert,
- ob der Boot-Kontext verzerrt,
- oder ob gewöhnliche Sprachmodelle diese Heuristiken bereits implizit beherrschen.

---

# 14. Minimaler erster Versuch

Für einen ersten Prototyp genügt ein sehr kleines System.

Beispielsweise:

- 4 verborgene Zustände,
- 3 relevante Übergänge,
- 2 Bedingungen,
- 20 Trainingsszenen,
- 10 Testszenen,
- mehrere irrelevante Oberflächenvariablen.

Verglichen werden zunächst:

```text
A: Baseline
B: R1
C: R1 + R2
```

Erst danach:

```text
D: R1 + R2 + Boot-Kontext
E: Ablationen
F: R3-Lernvergleich O₀ vs. O₁
```

Damit bleibt der erste Test klein, nachvollziehbar und reproduzierbar.

---

# 15. Offene Fragen

Vor der konkreten Durchführung müssen noch einige Entscheidungen getroffen werden:

- Wie wird die verborgene Basis genau konstruiert?
- Welche relevante Leistung soll der erste Test besitzen?
- Wie stark darf die natürliche Sprache variieren?
- Wie wird strukturelle Äquivalenz zwischen erwarteter und gefundener Basis bewertet?
- Welche Teile des Boot-Kontexts sind fest und welche lernbar?
- Wie werden Suchkosten erfasst?
- Wie viele unabhängige Testsysteme sind nötig?

Diese Fragen betreffen das Versuchsdesign, nicht mehr die Grundidee von E1.

---

# 16. Kurzform

> **E1 prüft, ob Refactoring eine bekannte, aber verborgene generative Basis aus natürlichsprachlichen, verrauschten Szenen rekonstruieren kann.**

Verglichen werden:

```text
Baseline
vs.
R1
vs.
R1 + R2
vs.
R1 + R2 + Boot-Kontext
```

Später:

```text
ursprünglicher Operatorenraum O₀
vs.
durch R3 gelernter Operatorenraum O₁
```

Gemessen werden:

- strukturelle Treffer,
- Redundanz,
- Kompression,
- generative Genauigkeit,
- Robustheit,
- Transfer,
- Suchkosten.

Damit wird Refactoring erstmals als experimentell prüfbares Verfahren behandelt.
