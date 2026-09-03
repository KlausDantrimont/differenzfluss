# Der epistemische Compiler-Compiler

## Von deklarativen Erkenntnisverfahren zu ausführbaren Working-Set-Strategien

**Status:** Konzept / Architekturhypothese 0.1  
**Kontext:** Schnittwerk, epistemisches Refactoring, Brillenladen, Working-Set Compiler

---

## 1. Ausgangspunkt

Schnittwerk beschreibt epistemische Arbeit bereits auf der Ebene von:

- Fragen,
- relevanten Leistungen,
- Schnitten,
- Operatoren,
- Dimensionen,
- Perspektiven,
- Brillen,
- epistemischen Signaturen,
- Prüfungen,
- Residuen.

Diese Elemente können nicht nur zur Beschreibung oder Analyse epistemischer Verfahren verwendet werden.

Sie können möglicherweise auch als **deklarative Spezifikation ausführbarer Erkenntnisverfahren** dienen.

Daraus entsteht die Idee eines:

> **epistemischen Compiler-Compilers**

Seine Aufgabe lautet:

> **Aus einer Beschreibung eines epistemischen Verfahrens eine ausführbare Strategie zu erzeugen, die für konkrete Aufgaben die jeweils benötigten Working Sets konstruiert.**

---

## 2. Drei Ebenen

```text
epistemische Spezifikation
          ↓
   Compiler-Compiler
          ↓
Working-Set Compiler
          ↓
    konkrete Aufgabe
          ↓
      Working Set
          ↓
    semantische Runtime
```

Die Ebenen dürfen nicht vermischt werden.

---

## 3. Epistemische Spezifikation

Die oberste Ebene beschreibt ein Erkenntnisverfahren unabhängig von einer konkreten Ausführung.

Beispiel:

```yaml
operator: contradiction_check

relevant_performance:
  detect:
    - genuine_contradictions
    - apparent_contradictions
  distinguish:
    - perspective_difference
    - scope_difference
    - temporal_difference
    - definition_difference

dimensions:
  - claim
  - definition
  - perspective
  - system_boundary
  - time
  - provenance

requires:
  - target_claim
  - relevant_counterclaims
  - definitions

prefer:
  - provenance
  - temporal_context
  - alternative_interpretations

preserve:
  - claim_identity
  - validity
  - source_relationships

minimize:
  - unrelated_history
  - redundant_evidence

tests:
  - contradiction_test
  - scope_test
  - perspective_test
```

Dies ist noch kein Prompt und noch kein Programm für ein bestimmtes LLM.

Es ist eine **epistemische Methodenspezifikation**.

---

## 4. Rolle des Compiler-Compilers

Der Compiler-Compiler übersetzt die Methodenspezifikation in eine ausführbare Working-Set-Strategie.

Formal:

\[
C_O = G(O,R,B)
\]

mit:

- \(O\): epistemische Spezifikation,
- \(R\): allgemeine Refactoring- und Qualitätsregeln,
- \(B\): Eigenschaften der Zielruntime,
- \(G\): Compiler-Generator,
- \(C_O\): erzeugter Working-Set Compiler.

Der Generator beantwortet die Frage:

> **Wenn diese epistemische Methode ausgeführt werden soll: Nach welchen Regeln muss der benötigte Kontext konstruiert werden?**

---

## 5. Der Working-Set Compiler

Der erzeugte Compiler arbeitet anschließend auf konkreten Aufgaben:

\[
W = C_O(S,T,Budget)
\]

mit:

- \(S\): aktueller epistemischer Zustand,
- \(T\): konkrete Aufgabe,
- \(Budget\): verfügbares Kontext-/Kostenbudget,
- \(W\): Working Set.

Damit ergeben sich zwei verschiedene Compilationsvorgänge:

```text
METHODE
epistemische Spezifikation
↓
Compiler-Compiler
↓
Working-Set Compiler


AUSFÜHRUNG
epistemischer Zustand + Task
↓
Working-Set Compiler
↓
Working Set
```

Der erste Vorgang findet vergleichsweise selten statt.

Der zweite möglicherweise vor jedem relevanten LLM-Aufruf.

---

## 6. Warum ein Compiler-Compiler?

Ohne Generator müsste für jeden epistemischen Operator, jede Brille und jede Domäne eine eigene Context-Management-Logik programmiert werden.

```text
Widerspruchsanalyse
→ eigener Retrieval-Code

Kausalanalyse
→ eigener Retrieval-Code

Systembrille
→ eigener Retrieval-Code

Disput-Refactoring
→ eigener Retrieval-Code
```

Das skaliert schlecht.

Schnittwerk besitzt jedoch bereits einen expliziten Beschreibungsraum aus:

- relevanter Leistung,
- Operatoren,
- Dimensionen,
- Perspektiven,
- Signaturen,
- Budgets,
- Blindstellen,
- Prüfverfahren.

Die Hypothese lautet daher:

> **Wenn epistemische Verfahren hinreichend explizit spezifiziert werden können, kann ihre Laufzeitlogik zumindest teilweise automatisch erzeugt werden.**

---

## 7. R1 als generische Qualitätssemantik

R1 liefert einen allgemeinen Maßstab:

> **So wenig Struktur wie möglich, so viel wie nötig, damit die relevante Leistung erhalten bleibt.**

Auf Working Sets übertragen:

> **So wenig Kontext wie möglich, so viel wie nötig, damit die spezifizierte epistemische Operation zuverlässig ausgeführt werden kann.**

Die jeweilige Methode spezifiziert die **relevante Leistung**.

R1 liefert den allgemeinen Optimierungsrahmen.

Zu minimieren sind beispielsweise:

- irrelevante Information,
- Redundanz,
- unnötige Tokenmenge,
- widersprüchliche Altstände,
- strukturelle Überladung.

Zu erhalten oder zu maximieren sind:

- relevante Information,
- notwendige Beziehungen,
- Rekonstruktionskraft,
- Prüfbarkeit,
- Operationsfähigkeit.

R1 wird damit zu einer **generischen Semantik guter Working Sets**.

---

## 8. R2 als Compilationslogik

R2 beschreibt, wie aus einem großen Problemraum eine tragfähige lokale Struktur gefunden werden kann.

Für den Working-Set Compiler bedeutet dies:

```text
Task bestimmen
↓
relevante epistemische Leistung bestimmen
↓
Kontextschnitt erzeugen
↓
Kandidaten auswählen
↓
Relationen und Abhängigkeiten prüfen
↓
irrelevante Struktur entfernen
↓
fehlende Struktur erkennen
↓
Working Set prüfen
```

Die R2-Operationen lassen sich direkt verwenden:

- REMOVE
- SPLIT
- MERGE
- REPLACE
- EXTRACT
- COMPOSE
- GENERALIZE
- SPECIALIZE
- REFRAME

R2 kann damit zur **generischen Transformations- und Suchlogik des Compilers** werden.

---

## 9. R3 ist optional

Für einen funktionsfähigen Compiler-Compiler werden R1 und R2 benötigt.

R3 nicht.

Ein statisches System kann bereits:

1. eine epistemische Methode erhalten,
2. daraus eine Working-Set-Strategie erzeugen,
3. diese auf konkrete Aufgaben anwenden,
4. Working Sets konstruieren,
5. Ergebnisse prüfen.

R3 kann später lernen:

- welche Context Contracts zu großzügig sind,
- welche Informationen häufig fehlen,
- welche Operatoren welche Objektklassen benötigen,
- welche Compilerstrategien in bestimmten Domänen funktionieren,
- welche Spezifikationen wiederholt schlechte Working Sets erzeugen.

R3 ist daher:

> **adaptive Optimierung eines bereits funktionierenden Compilersystems.**

---

## 10. Brillen als compilierbare Spezifikationen

Eine Brille ist im Schnittwerk bereits eine wiederverwendbare epistemische Konfiguration.

Beispiel:

```yaml
lens: system_dynamics

attend_to:
  - states
  - transitions
  - feedback
  - delay
  - boundary

prefer:
  - temporal_observations
  - causal_relations
  - interventions

challenge:
  - static_explanations
  - linear_models

blind_spots:
  - normative_evaluation
```

Der Compiler-Compiler kann daraus ableiten:

- welche Objektarten bevorzugt werden,
- welche Relationen relevant sind,
- welche Perspektiven zurückgestellt werden,
- welche Gegenprüfungen nötig sind,
- welche Teile des epistemischen Zustands in den Working Set gehören.

Damit erhält der Satz

> **„Setze diese Brille auf.“**

technische Bedeutung:

> **Compile diese epistemische Perspektivenspezifikation zu einer Working-Set-Strategie und wende sie auf den aktuellen Zustand an.**

---

## 11. Epistemische Signaturen als Zwischendarstellung

Die epistemische Signatur eignet sich möglicherweise als Intermediate Representation des Compilersystems.

```text
natürliche Frage / Brille / Methode
             ↓
      epistemische Signatur
             ↓
       Compiler-Compiler
             ↓
    Working-Set-Strategie
```

Eine Signatur könnte enthalten:

```text
relevante Leistung
Operatoren
Dimensionen
Gewichtungen
Systemgrenzen
Perspektiven
Prüfanforderungen
Budget
Blindstellen
```

Damit kann die Signatur eine ähnliche Rolle übernehmen wie eine IR in klassischen Compilersystemen: verschiedene Eingabesprachen werden auf eine gemeinsame Zwischenrepräsentation abgebildet.

---

## 12. Mehrere Quellsprachen

Der Compiler-Compiler muss nicht nur explizite Operatorenspezifikationen verstehen.

Mögliche Quellsprachen sind:

### Natürliche Frage

```text
Welche strukturellen Ursachen machen diesen Agenten unzuverlässig?
```

### Brille

```text
systemische Brille
```

### Expliziter Operator

```text
causal_analysis
```

### Epistemische Signatur

Eine vollständig spezifizierte Konfiguration.

### Komposition

```text
system_dynamics
+
contradiction_check
+
adversarial_test
```

Alle können in eine gemeinsame ausführbare Repräsentation übersetzt werden.

---

## 13. Mehrere Zielsysteme

Auch die Zielruntime muss nicht immer dasselbe LLM sein.

```text
                  epistemische Spezifikation
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
         großes LLM    lokales LLM     Mensch
              │            │            │
          Context       Context       Fragen /
          + Tools       + Retrieval   Checkliste
```

Damit bleibt der Grundgedanke erhalten:

> **Das epistemische Verfahren ist zunächst substratneutral.**

Der Compiler-Compiler erzeugt eine für das jeweilige Substrat geeignete Operationalisierung.

---

## 14. Ein Compiler muss nicht aus Programmcode bestehen

Ein erzeugter Working-Set Compiler könnte sein:

- Python-Code,
- eine deklarative Policy,
- ein Prompt,
- ein LLM-basierter Auswahlagent,
- eine Kombination aus Regeln und LLM-Aufrufen,
- ein Workflow-Graph.

Beispiel:

```yaml
working_set_compiler:

  pin:
    - hard_constraints
    - current_goal

  semantic_select:
    model: local_llm
    task:
      choose objects required for causal analysis

  enforce:
    - validity
    - scope
    - permissions

  on_missing:
    - retrieve
    - recompile

  budget:
    max_tokens: 12000
```

Entscheidend ist nicht die Implementationssprache.

> **Der Compiler transformiert epistemischen Zustand nach einer expliziten Methode in einen ausführbaren Working Set.**

---

## 15. Determinismus und KI

Eine sinnvolle Aufteilung lautet:

### Deterministisch

- Typregeln
- Gültigkeit
- Versionierung
- Scope
- Rechte
- harte Constraints
- Budgets
- Objektidentitäten
- Abhängigkeiten

### Semantisch / LLM-basiert

- Relevanz
- Ähnlichkeit
- benötigte Gegenpositionen
- Perspektivwahl
- mögliche Blindstellen
- Relevanz von Evidenz
- notwendige Kontextausweitung

Grundsatz:

> **Explizite Regeln dort, wo Regeln möglich sind. Semantisches Urteil dort, wo Bedeutung beurteilt werden muss.**

---

## 16. Epistemische Page Faults

Ein erzeugter Compiler darf feststellen:

> Die für diese Operation notwendige Information ist nicht vorhanden.

```yaml
compile_status: incomplete

missing:
  - current_definition
  - evidence_for_claim_17

required_actions:
  - retrieve_internal
  - search_external

resume_after:
  - missing_information_resolved
```

Damit wird fehlender Kontext zu einem expliziten Laufzeitzustand.

---

## 17. Schnittwerk als epistemische Programmiersprache?

Damit ergibt sich eine stärkere Interpretation.

Schnittwerk wäre nicht nur eine Architektur zur Beschreibung epistemischer Problemräume.

Es könnte zugleich die Grundlage einer **deklarativen Sprache für epistemische Programme** bilden.

Ein epistemisches Programm spezifiziert nicht jeden Gedankenschritt. Es spezifiziert vielmehr:

- welche Erkenntnisleistung gesucht wird,
- welche epistemischen Operationen zulässig oder erwünscht sind,
- auf welchen Dimensionen sie arbeiten,
- was erhalten werden muss,
- welche Alternativen geprüft werden sollen,
- welche Blindstellen relevant sind,
- und wann eine Ausführung als hinreichend gilt.

Der Compiler-Compiler übersetzt diese deklarative Beschreibung in eine konkrete Ausführungsstrategie.

---

## 18. Verschiebung der Rolle des LLM

In dieser Architektur ist das LLM nicht mehr das vollständige kognitive System.

Es wird zu einer austauschbaren semantischen Runtime.

```text
Schnittwerk
epistemisches Programm
       ↓
Compiler-Compiler
       ↓
Working-Set Compiler
       ↓
Working Set
       ↓
LLM
```

Das LLM erhält nicht alles, was das System weiß.

Es erhält:

> **das, was es für die gegenwärtige epistemische Operation wissen soll.**

Damit verschiebt sich ein Teil der Intelligenz vom Modell in die Architektur.

---

## 19. Ein epistemisches Betriebssystem

```text
Anwendungen
─────────────────────────────
Problem-Radar | Tutor | Audits | Forschungsagenten | YAS

Epistemische Programme
─────────────────────────────
Schnittwerk | Brillen | Operatoren | Kompositionen

Compiler-Compiler
─────────────────────────────
epistemische Spec → ausführbare Methode

Working-Set Compiler
─────────────────────────────
Zustand + Task → Working Set

Epistemischer Kernel
─────────────────────────────
Objekte | Identität | Version | Gültigkeit | Provenienz
Scope | Budget | Rechte

Runtime
─────────────────────────────
LLMs | Tools | Retrieval | Speicher
```

Der Compiler-Compiler verbindet die **Methodenschicht** mit der **Laufzeitschicht**.

---

## 20. Minimal Viable Compiler-Compiler

Für einen ersten Proof of Concept genügen:

1. einige epistemische Objekttypen,
2. zwei oder drei Operatorenspezifikationen,
3. eine kleine Menge gespeicherter epistemischer Objekte,
4. ein Compiler-Generator,
5. ein Working-Set Compiler,
6. ein Task-LLM.

Beispielsweise:

```text
Operator A: contradiction_check
Operator B: causal_analysis
Operator C: perspective_shift
```

Für jeden Operator wird automatisch eine Working-Set-Strategie erzeugt.

Erste Testfrage:

> **Erzeugt der generierte Compiler bei unterschiedlichen Aufgaben plausibel unterschiedliche Working Sets?**

Erst danach folgt:

> **Verbessern diese Working Sets tatsächlich die Leistung des Task-LLMs?**

---

## 21. Vergleichsexperiment

```text
A  gesamter verfügbarer Kontext
B  Similarity Retrieval
C  manuell entworfener Working-Set Compiler
D  automatisch generierter Working-Set Compiler
```

Mögliche Messgrößen:

- Taskqualität
- Instruktionsbefolgung
- Fehler
- Widerspruchserkennung
- Tokenverbrauch
- unnötiger Kontext
- fehlender Kontext
- Zahl notwendiger Nach-Retrievals

Damit lässt sich der Wert des Compiler-Compiler-Ansatzes empirisch prüfen.

---

## 22. Kernhypothese

> **Epistemische Methoden können hinreichend explizit beschrieben werden, um daraus automatisch ausführbare Context- und Working-Set-Strategien zu erzeugen.**

Die stärkere Hypothese lautet:

> **Ein erheblicher Teil zuverlässiger KI-gestützter Erkenntnisarbeit kann aus deklarativen epistemischen Spezifikationen und einer generischen Runtime erzeugt werden, statt für jede Anwendung separat programmiert zu werden.**

---

## 23. Bedeutung für Schnittwerk

Die Compiler-Compiler-Idee verändert die Interpretation des Schnittwerks.

Bisher:

> Schnittwerk beschreibt und strukturiert epistemische Verfahren.

Neu:

> **Schnittwerk könnte epistemische Verfahren spezifizieren, die durch einen Compiler-Compiler ausführbar gemacht werden.**

Damit werden:

- Kunst der Frage zur natürlichen Quellsprache,
- epistemische Signaturen zu möglichen Zwischenrepräsentationen,
- R1 zur Qualitätssemantik,
- R2 zur generischen Transformations- und Suchlogik,
- Brillen und Operatoren zu compilierbaren Methodenbausteinen,
- der Working-Set Compiler zur Laufzeitschicht,
- das LLM zur semantischen Zielmaschine.

R3 kann später als optionale adaptive Optimierung hinzukommen.

---

## 24. Kurzform

> **Schnittwerk beschreibt epistemische Programme.**

> **Der Compiler-Compiler übersetzt diese Programme in ausführbare Erkenntnisverfahren.**

> **Der Working-Set Compiler erzeugt während ihrer Ausführung den jeweils benötigten semantischen Arbeitskontext.**

> **Das LLM führt die konkrete semantische Operation aus.**

```text
Frage
↓
epistemischer Auftrag
↓
epistemische Spezifikation
↓
Compiler-Compiler
↓
Working-Set Compiler
↓
Working Set
↓
LLM
↓
Ergebnis + Residuum
```

Damit entsteht aus einer Architektur für Fragen, Perspektiven und Problemräume der Entwurf einer möglichen:

> **deklarativen epistemischen Runtime.**
