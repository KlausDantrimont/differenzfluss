# Working-Set Compiler

## Eine epistemische Laufzeitschicht für LLM-Systeme

**Status:** Konzept / Architekturhypothese 0.1  
**Kontext:** Schnittwerk, epistemisches Refactoring, Context & Working-Set Management

---

## 1. Ausgangspunkt

Ein Sprachmodell arbeitet immer nur auf einem begrenzten aktuellen Kontext.

Dieser Kontext ist nicht identisch mit dem gesamten Wissen, der vollständigen Historie oder dem persistenten Zustand eines Agenten. Er ist vielmehr der **aktuelle Working Set** der semantischen Verarbeitung.

Daraus ergibt sich die Leitfrage:

> **Welche Information muss einem LLM für einen bestimmten epistemischen Arbeitsschritt gerade jetzt vorliegen?**

Die Arbeitshypothese lautet:

> **Nicht maximale Kontextmenge, sondern die richtige reduzierte Struktur erzeugt zuverlässige semantische Arbeit.**

Der Working-Set Compiler konstruiert diese reduzierte Struktur.

---

## 2. Definition

Ein **Working-Set Compiler** ist eine epistemische Laufzeitkomponente, die aus

- einem persistenten epistemischen Zustand,
- einer aktuellen Aufgabe,
- einer gewünschten epistemischen Operation,
- den verfügbaren Informationsquellen,
- und einem Ressourcenbudget

 einen für den nächsten Verarbeitungsschritt geeigneten Working Set konstruiert.

Formal:

\[
W = C(S,T,O,B)
\]

mit:

- \(S\): epistemischer Zustand,
- \(T\): aktuelle Aufgabe,
- \(O\): epistemische Operation oder Methode,
- \(B\): Ressourcen- bzw. Kontextbudget,
- \(W\): Working Set.

Der Working Set ist zunächst eine **strukturierte Auswahl epistemischer Objekte** und noch nicht notwendig der endgültige Prompt.

---

## 3. Warum „Compiler“?

Ein klassischer Compiler nimmt eine strukturierte Repräsentation, berücksichtigt Regeln und Zielbedingungen und erzeugt daraus eine für eine Zielmaschine geeignete ausführbare Darstellung.

Analog:

```text
epistemischer Zustand
+
Aufgabe
+
Operator
+
Budget
        ↓
Working-Set Compiler
        ↓
strukturierter Working Set
        ↓
modellabhängiges Rendering
        ↓
LLM
```

Die Zielmaschine ist hier ein Sprachmodell als **semantischer Prozessor**.

Der Compiler entscheidet nicht primär, wie die Sachfrage beantwortet wird. Er entscheidet:

> **Welche Unterlagen braucht die semantische CPU, damit sie diese Aufgabe bearbeiten kann?**

---

## 4. Epistemischer Zustand

Der persistente Zustand besteht nicht nur aus Textfragmenten. Er enthält typisierte epistemische Objekte, beispielsweise:

- Beobachtung
- Behauptung
- Hypothese
- Gegenhypothese
- Entscheidung
- Regel
- Constraint
- offene Frage
- Quelle
- Evidenz
- Modell
- Annahme
- Gegenbeispiel
- Perspektive
- Definition
- Artefakt
- verworfene Erklärung
- Residuum

Mögliche Metadaten:

- Identität
- Typ
- Status
- Scope
- Version
- Gültigkeit
- Provenienz
- Priorität
- Confidence
- Abhängigkeiten
- Beziehungen
- Aktualität
- Komprimierbarkeit

Damit wird Information nicht nur danach unterschieden, **wo** sie gespeichert ist, sondern **welche epistemische Funktion** sie besitzt.

---

## 5. Context Management und Working-Set Management

**Context Management** verwaltet den gesamten prinzipiell verfügbaren epistemischen Zustand.

Es behandelt beispielsweise:

- Persistenz
- Versionierung
- Gültigkeit
- Provenienz
- Abhängigkeiten
- Rechte und Scope
- Aktualität
- Kompression
- Retrieval

**Working-Set Management** beantwortet die engere Frage:

> **Welche Teilmenge dieses Zustands benötigt der nächste Verarbeitungsschritt?**

```text
gesamter epistemischer Zustand
             ↓
       Context Management
             ↓
      verfügbarer Kontext
             ↓
     Working-Set Compiler
             ↓
       aktueller Working Set
             ↓
             LLM
```

Ein Agent muss nicht alles erinnern.

> **Er muss zum richtigen Zeitpunkt das Richtige im Working Set haben.**

---

## 6. Der Compiler als LLM-gestützte Komponente

Die Konstruktion eines Working Sets ist teilweise selbst eine semantische Aufgabe.

Relevanz lässt sich nicht vollständig durch Keywords, Embeddings oder feste Regeln bestimmen. Deshalb kann der Working-Set Compiler selbst einen LLM-Aufruf verwenden.

Dieser Call besitzt jedoch eine eng begrenzte Aufgabe:

> **Bestimme, welche epistemischen Objekte für den nächsten Arbeitsschritt benötigt werden.**

Er beantwortet die Sachfrage noch nicht.

Beispiel:

```yaml
working_set:
  pinned:
    - rule_12
    - decision_7

  target:
    - hypothesis_4

  retrieve:
    - source_23
    - source_31
    - definition_9

  supporting:
    - observation_18
    - counterexample_3

  exclude:
    - obsolete_hypothesis_2
    - unrelated_history_41

missing:
  - current_status_component_x
```

---

## 7. LLM für Urteil, Runtime für Invarianten

Eine sinnvolle Arbeitsteilung lautet:

### Semantisches Urteil durch das LLM

- Relevanz
- mögliche Gegenpositionen
- benötigte Perspektiven
- anschlussfähige frühere Entscheidungen
- wahrscheinlich erforderliche Evidenz
- ähnliche Fälle
- mögliche Blindstellen

### Deterministische Kontrolle durch die Runtime

- `pinned = true`
- Rechte
- Gültigkeitsregeln
- Versionierung
- harte Constraints
- Scope
- exakte Objektidentitäten
- Abhängigkeiten
- Budgetgrenzen
- Dublettenbehandlung

Grundsatz:

> **LLM für semantisches Urteil. Runtime für Invarianten.**

---

## 8. Epistemische Operatoren als Kontextverträge

Ein epistemischer Operator beschreibt nicht nur, **was getan werden soll**, sondern auch:

> **Welche Art von Information er dafür benötigt.**

Beispiel:

```yaml
operator: contradiction_check

requires:
  - target_claim
  - relevant_counterclaims
  - definitions
  - provenance
  - validity
  - temporal_scope

prefer:
  - alternative_interpretations
  - competing_models

exclude:
  - unrelated_history
```

Ein anderer Operator kann einen völlig anderen Context Contract besitzen.

Damit lautet die Auswahl nicht bloß:

> Was ähnelt der Frage?

Sondern:

> **Was benötigt diese epistemische Operation, um ihre relevante Leistung zu erbringen?**

---

## 9. R1 – Qualität eines Working Sets

R1 beschreibt eine gute Zerlegung als bezüglich einer relevanten Leistung möglichst abstrakte, wenig redundante und dennoch tragfähige Struktur.

Auf Working Sets übertragen lautet die relevante Leistung:

> **Dem nächsten epistemischen Verarbeitungsschritt genügend Struktur bereitzustellen, damit er seine Aufgabe zuverlässig erfüllen kann.**

Daraus folgt:

> **So wenig Kontext wie möglich, so viel wie nötig, damit die epistemische Operation trägt.**

Oder:

> **Minimale Kontextstruktur bei maximaler relevanter Operationskraft.**

Nicht die Zahl der Tokens ist das primäre Qualitätsmaß, sondern die Frage:

> **Welche relevante Leistung bleibt nach der Kontextreduktion erhalten?**

---

## 10. Context Overload und Context Loss

Zwei symmetrische Fehlerklassen begrenzen die Suche.

### Context Overload

Zu viel Material wird geladen.

Mögliche Folgen:

- Attention Degradation
- Redundanz
- widersprüchliche Information
- unnötiger Tokenverbrauch
- schlechte Prioritätserkennung
- schlechtere Instruktionsbefolgung

### Context Loss

Zu viel relevante Struktur wurde entfernt.

Mögliche Folgen:

- fehlende Entscheidungen
- fehlende Regeln
- Verlust wichtiger Annahmen
- falsche Schlussfolgerungen
- Wiederholung erledigter Arbeit
- scheinbares „Vergessen“

Gesucht wird die Grenze:

```text
Context Overload
       ↓
tragender Working Set
       ↓
Context Loss
```

---

## 11. R2 – Konstruktion des Working Sets

R2 fragt allgemein, wie eine gute Zerlegung gefunden wird.

Für den Compiler lautet die entsprechende Frage:

> **Wie findet man die Auswahl epistemischer Objekte, die bezüglich der aktuellen Operation einen guten Working Set bildet?**

Eine Runtime-Variante des R2-Prozesses lautet:

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

R2-Operationen können direkt auf Kontext angewandt werden:

- REMOVE
- SPLIT
- MERGE
- REPLACE
- EXTRACT
- COMPOSE
- GENERALIZE
- SPECIALIZE
- REFRAME

Beispielsweise:

**REMOVE** – Kann dieses Objekt entfernt werden, ohne die relevante Leistung zu beeinträchtigen?

**SPLIT** – Enthält ein Dokument mehrere epistemisch verschiedene Informationsarten, von denen nur eine benötigt wird?

**MERGE** – Sind mehrere Objekte funktional redundant?

**EXTRACT** – Kann aus langer Historie eine kleine tragende Struktur herausgezogen werden?

**REFRAME** – Ist nicht der Kontext zu schlecht, sondern bereits der epistemische Auftrag falsch geschnitten?

---

## 12. Epistemischer Page Fault

Der Compiler darf feststellen:

> **Die benötigte Information ist nicht vorhanden.**

Beispiel:

```yaml
status: incomplete

missing:
  - current_definition_component_x
  - evidence_for_hypothesis_7

required_action:
  - retrieve_internal
  - search_external
```

Der Task-Aufruf wird dann nicht mit unzureichendem Kontext gestartet.

```text
Task
 ↓
Working-Set Compiler
 ↓
Information ausreichend?
 ↓                 ↓
ja                nein
 ↓                 ↓
Task-LLM       Retrieval
                  ↓
               Compile erneut
```

Nichtwissen wird damit zu einem expliziten Laufzeitzustand.

---

## 13. R3 – optionale Lernschicht

R1 und R2 genügen für einen funktionsfähigen Working-Set Compiler.

R3 ist eine optionale Erweiterung.

Jeder Compilerlauf kann Erfahrungen liefern:

- Aufgabe
- Operator
- ausgewählter Kontext
- ausgelassener Kontext
- Tokenkosten
- Ergebnisqualität
- Fehler
- nachträglich benötigte Information
- ungenutzte Information
- Residuen

Daraus könnte später gelernt werden:

> **Welche Working-Set-Strategien funktionieren unter welchen Bedingungen?**

R3 ist damit adaptive Optimierung eines bereits funktionierenden Systems, nicht Voraussetzung seiner Existenz.

---

## 14. Verbindung zu Supervision und Verification Cost

Schlechtes Working-Set Management kann downstream erhebliche Kosten erzeugen:

```text
schlechte Working-Set-Konstruktion
↓
fehlende oder widersprüchliche Information
↓
schlechte Agentenentscheidung
↓
menschliche Prüfung
↓
Korrektur / Wiederholung
↓
Supervision Cost
```

Working-Set Management ist damit nicht nur eine technische Optimierung, sondern kann eine Ursache wirtschaftlich relevanter Agentenprobleme sein.

---

## 15. Forschungsdesign

Verschiedene Strategien lassen sich experimentell vergleichen:

### A – vollständiger Kontext

Alles verfügbare Material wird geladen.

### B – Sliding Window

Nur die letzten Interaktionen.

### C – Similarity Retrieval

Embeddings oder Keyword-Suche bestimmen den Kontext.

### D – regelbasierter Working Set

Feste Kontextregeln.

### E – LLM-basierter Compiler

Ein Modell entscheidet semantisch über die Auswahl.

### F – hybrider Compiler

LLM-Auswahl plus deterministische Invarianten.

Mögliche Messgrößen:

- Taskqualität
- Fehlerquote
- Instruktionsverlust
- Widerspruchserkennung
- Halluzinationsrate
- Tokenverbrauch
- Laufzeit
- Supervisionbedarf
- Zahl epistemischer Page Faults

---

## 16. Modellgröße als Variable

Der Compiler eröffnet die Forschungsfrage:

> **Wie viel Modellleistung lässt sich durch bessere epistemische Infrastruktur ersetzen?**

Beispielsweise:

```text
kleines Modell + einfacher Kontext
vs.
kleines Modell + Working-Set Compiler
vs.
großes Modell + einfacher Kontext
vs.
großes Modell + Working-Set Compiler
```

Damit wird präziser untersuchbar:

> **Wie viel Modell braucht man, wenn Zustand, Kontextselektion und epistemische Verfahren außerhalb des Modells explizit organisiert sind?**

---

## 17. Stellung im epistemischen Betriebssystem

```text
Anwendungen
────────────────────────────────
Problem-Radar | Tutor | Audit | Forschung | YAS

Epistemische Methoden
────────────────────────────────
Schnittwerk | Brillen | Operatoren | Refactoring

Working-Set Compiler
────────────────────────────────
Task + Operator + Zustand + Budget → Working Set

Epistemischer Kernel
────────────────────────────────
Objektidentität | Status | Scope | Provenienz
Versionierung | Gültigkeit | Abhängigkeiten | Rechte

Runtime
────────────────────────────────
LLM | Tools | Retrieval | Speicher | Web | Datenbanken
```

Der Working-Set Compiler bildet die Übergangsschicht zwischen **persistenter epistemischer Struktur** und **momentaner semantischer Verarbeitung**.

---

## 18. Rolle von Schnittwerk

Schnittwerks Operatoren können in dieser Architektur zugleich festlegen:

- welche epistemischen Objekte benötigt werden,
- welche Relationen relevant sind,
- welche Blindstellen geprüft werden,
- welche Alternativen geladen werden sollen,
- welche Qualitätskriterien gelten.

Ein Operator wird damit potenziell zu:

```text
Operation
+
Kontextvertrag
+
Prüfverfahren
```

Eine Brille kann dieselbe Funktion für eine zusammengesetzte Perspektive übernehmen.

---

## 19. R1–R3 als Compilerlogik

### R1

> **Was ist ein guter Working Set?**

Qualitätsmaßstab.

### R2

> **Wie findet der Compiler diesen Working Set?**

Compilationsverfahren.

### R3

> **Wie verbessert sich der Compiler aus Erfahrung?**

Optionale adaptive Erweiterung.

Kurz:

```text
R1  Qualität des Working Sets
R2  Compilation
R3  optionale adaptive Compilation
```

---

## 20. Kernhypothese

> **Die Zuverlässigkeit eines LLM-Agenten hängt wesentlich davon ab, ob für jeden Verarbeitungsschritt ein bezüglich der aktuellen epistemischen Operation geeigneter Working Set konstruiert wird.**

Daraus folgt:

> **Context Engineering kann als Compilerproblem aufgefasst werden.**

Die Aufgabe besteht nicht darin, möglichst viele Tokens bereitzustellen, sondern den persistenten epistemischen Zustand in eine für die aktuelle Erkenntnisoperation tragfähige semantische Arbeitsrepräsentation zu übersetzen.

---

## 21. Kurzform

> **Der Working-Set Compiler übersetzt epistemischen Zustand in ausführbaren Kontext.**

Er beantwortet vor jedem semantischen Verarbeitungsschritt:

> **Was muss diese Maschine jetzt wissen?**

R1 definiert, wann diese Auswahl gut ist.

R2 beschreibt, wie sie gefunden werden kann.

R3 kann später beschreiben, wie das Verfahren aus Erfahrung besser wird.
