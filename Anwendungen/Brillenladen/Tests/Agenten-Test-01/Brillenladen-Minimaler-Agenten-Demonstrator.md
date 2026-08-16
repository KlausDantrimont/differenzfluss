# Brillenladen – Minimaler Agenten-Demonstrator

## Ziel

Nicht zeigen, dass „mehr Agenten besser“ sind.

Sondern eine engere Frage prüfen:

> **Erzeugen explizit unterschiedliche epistemische Operatoren eine trennschärfere und weniger redundante Arbeitsteilung als übliche Rollenbeschreibungen?**

Der Versuch ist absichtlich klein.  
Er braucht zunächst kein Agenten-Framework.

---

# 1. Was hier überhaupt ein „Agent“ ist

Für diesen Versuch genügt:

> **Agent = ein eigener Modellaufruf mit eigener Arbeitsanweisung und demselben Ausgangsproblem.**

Vier Aufrufe reichen:

```text
Problem
├── Agent 1
├── Agent 2
├── Agent 3
└── Koordinator
```

Die drei Analyse-Agenten arbeiten unabhängig.

Der Koordinator erhält anschließend nur ihre Ergebnisse und soll:

- Überschneidungen markieren,
- wirklich unterschiedliche Befunde zusammenführen,
- Widersprüche unterscheiden,
- fehlende Evidenz benennen,
- und entscheiden, ob ein weiterer Analysegang nötig wäre.

Das ist bereits ein minimales Multi-Agent-System.

---

# 2. Testfall

```text
Ein verteiltes Softwaresystem läuft die meiste Zeit stabil.

In unregelmäßigen Abständen steigt die Antwortzeit einzelner Requests stark an.
Ein Neustart des betroffenen Dienstes beseitigt das Problem zuverlässig, aber nur vorübergehend.

CPU-, Speicher- und Datenbankmetriken zeigen während der Störung keine eindeutige Auffälligkeit.
Optimierungen einzelner Komponenten haben das Verhalten bisher nicht dauerhaft verändert.

Es liegen keine weiteren gesicherten Befunde vor.
Nicht gegebene Tatsachen dürfen nicht erfunden werden.
```

Der Fall ist absichtlich unterbestimmt.

Ein gutes Verfahren soll deshalb nicht möglichst schnell eine Ursache erfinden, sondern einen produktiven **Untersuchungsraum** aufspannen.

---

# 3. Variante A – Rollen-Agenten

Alle drei Agenten erhalten denselben Fall.

## Agent A1 – SRE

```text
Du bist ein erfahrener Site Reliability Engineer.

Analysiere den Fall.
Identifiziere die wahrscheinlich wichtigsten Erklärungsrichtungen und schlage nächste Untersuchungen vor.

Trenne Beobachtungen, Hypothesen und benötigte Evidenz.
Erfinde keine nicht gegebenen Tatsachen.
```

## Agent A2 – Softwarearchitekt

```text
Du bist ein erfahrener Softwarearchitekt für verteilte Systeme.

Analysiere den Fall.
Identifiziere die wahrscheinlich wichtigsten Erklärungsrichtungen und schlage nächste Untersuchungen vor.

Trenne Beobachtungen, Hypothesen und benötigte Evidenz.
Erfinde keine nicht gegebenen Tatsachen.
```

## Agent A3 – kritischer Reviewer

```text
Du bist ein kritischer technischer Reviewer.

Analysiere den Fall.
Suche besonders nach übersehenen Erklärungsrichtungen, vorschnellen Annahmen und notwendigen Gegenprüfungen.

Trenne Beobachtungen, Hypothesen und benötigte Evidenz.
Erfinde keine nicht gegebenen Tatsachen.
```

---

# 4. Variante B – epistemische Agenten

Wieder derselbe Fall, dasselbe Modell, gleiche sonstige Einstellungen.

Die Agenten unterscheiden sich nun nicht durch Beruf oder Persönlichkeit, sondern durch **Analyserichtung**.

## Agent B1 – Zeit und Zustand

```text
Untersuche den Fall ausschließlich primär mit:

ZEIT
- Wie verändert sich das Problem?
- Welche zeitlichen Muster wären unterscheidend?

ZUSTAND
- Welche verborgenen oder temporären Zustände könnten für die Untersuchung relevant sein?
- Was könnte ein Neustart prinzipiell verändern, ohne zu behaupten, dass dies tatsächlich geschieht?

Erzeuge keine fertige Root-Cause-Erzählung.

Liefere:
1. gesicherte Beobachtungen,
2. daraus folgende Fragen,
3. prüfbare Hypothesen,
4. benötigte Evidenz,
5. Blindstellen dieser Perspektive.

Erfinde keine Tatsachen.
```

## Agent B2 – Relation und Information

```text
Untersuche den Fall ausschließlich primär mit:

RELATION
- Welche Beziehungen zwischen Komponenten, Requests, Ressourcen oder Zuständen sollten untersucht werden?

INFORMATION
- Welche relevanten Zustände oder Übergänge könnten von den vorhandenen Metriken prinzipiell nicht erfasst werden?
- Welche Beobachtbarkeit fehlt möglicherweise?

Erzeuge keine fertige Root-Cause-Erzählung.

Liefere:
1. gesicherte Beobachtungen,
2. daraus folgende Fragen,
3. prüfbare Hypothesen,
4. benötigte Evidenz,
5. Blindstellen dieser Perspektive.

Erfinde keine Tatsachen.
```

## Agent B3 – Kausalität, Evidenz und Gegenhypothese

```text
Untersuche den Fall ausschließlich primär mit:

KAUSALITÄT
- Welche Beobachtungen würden benötigt, um einen kausalen Zusammenhang zu behaupten?

EVIDENZ
- Was ist tatsächlich belegt, was nur plausibel?

GEGENHYPOTHESE
- Welche alternativen Erklärungsklassen müssen gegen naheliegende Ursachen bestehen bleiben?

Priorisiere Trennexperimente statt Ursachenlisten.

Liefere:
1. gesicherte Beobachtungen,
2. prüfbare konkurrierende Hypothesenklassen,
3. unterscheidende Tests,
4. benötigte Evidenz,
5. Blindstellen dieser Perspektive.

Erfinde keine Tatsachen.
```

---

# 5. Gleicher Koordinator für beide Varianten

Der Koordinator darf nicht wissen, welche Variante „gewinnen soll“.

```text
Du erhältst drei unabhängige Analysen desselben technischen Falls.

Bewerte nicht ihren Schreibstil.

Untersuche stattdessen:

1. Welche substanziellen Punkte kommen mehrfach vor?
2. Welche Punkte sind tatsächlich eigenständig und nicht nur anders formuliert?
3. Welche Analyse erzeugt zusätzliche prüfbare Untersuchungsrichtungen?
4. Wo werden unbelegte Tatsachen oder zu konkrete Ursachen angenommen?
5. Welche wichtigen Blindstellen werden explizit erkannt?
6. Welche Vorschläge ermöglichen unterscheidende Tests?
7. Ist ein weiterer Analyse-Agent voraussichtlich noch lohnend?
   Wenn ja: Welche möglichst orthogonale Perspektive fehlt?
   Wenn nein: Begründe den Abbruch.

Erstelle am Ende:
- gemeinsame Befunde,
- einzigartige Beiträge pro Agent,
- Redundanzen,
- offene Evidenz,
- empfohlenen nächsten Untersuchungsschritt,
- Stop/Weiter-Entscheidung.
```

---

# 6. Was gemessen wird

Keine komplizierte Benchmark-Mathematik nötig.

Für den ersten Versuch reichen sieben Kriterien.

## A. Redundanz

Wie viele wesentliche Punkte werden von mehreren Agenten wiederholt?

## B. Perspektivische Trennschärfe

Kann man an den Ergebnissen erkennen, dass tatsächlich verschiedene Analysebewegungen stattgefunden haben?

## C. Zusätzliche Abdeckung

Wie viele **eigenständige** relevante Untersuchungsrichtungen liefert das Ensemble?

## D. Prüfqualität

Werden Hypothesen in unterscheidbare Tests übersetzt?

## E. Epistemische Disziplin

Werden Beobachtung, Hypothese und Evidenz sauber getrennt?

## F. Blindstellenkontrolle

Erkennt ein Agent, was seine eigene Perspektive schlecht sieht?

## G. Budget / Abbruch

Kann das System begründet sagen:

> Jetzt brauchen wir eher Daten als noch einen weiteren Agenten.

---

# 7. Erwartung – ausdrücklich keine Erfolgsgarantie

Die Hypothese lautet:

> Rollen erzeugen wahrscheinlich teilweise unterschiedliche Fachakzente, aber auch erhebliche Überlappung.

Die operatorbasierte Variante sollte – wenn die Idee trägt – eher:

- unterschiedliche Schnitte erzwingen,
- Redundanz reduzieren,
- Blindstellen expliziter machen,
- Hypothesen besser trennen,
- und eine begründbare Arbeitsteilung erzeugen.

Es wäre ebenso interessant, wenn sie das **nicht** tut.

Dann wissen wir, dass die Operatorenschicht in dieser Form keinen zusätzlichen Nutzen liefert.

---

# 8. Warum dieser Test für Agentenleute interessant sein könnte

Der Versuch prüft keine neue Modellfähigkeit.

Er prüft eine andere Form der **Orchestrierung**.

Übliche Form:

```text
Problem
→ Rollen / Personas
→ mehrere Analysen
→ Synthese
```

Brillenladen-Form:

```text
Problem
→ epistemische Zerlegung
→ möglichst orthogonale Analyseoperationen
→ Synthese
→ Restproblem
→ Stop oder gezielter weiterer Schnitt
```

Der Unterschied liegt also weniger im „Agenten“ als in der Frage:

> **Nach welchem Prinzip wird kognitive Arbeit zwischen Agenten aufgeteilt?**

---

# 9. Wenn der Minimaltest funktioniert

Erst dann lohnt sich der nächste Schritt:

```text
Operatorenkatalog
        ↓
epistemischer Router
        ↓
dynamisch gewählte Agenten
        ↓
parallele Analyse
        ↓
Meta-Agent
        ↓
Restproblem / Budget
        ↓
weiter oder Stop
```

Dann wäre ein Framework wie AG2 interessant.

Der Router könnte zur Laufzeit entscheiden:

- Welche Operatoren sind für diesen Fall ergiebig?
- Welche lassen sich sinnvoll zu einem Agenten bündeln?
- Welche Perspektiven sind möglichst wenig redundant?
- Brauchen wir zwei Agenten oder vier?
- Welcher zusätzliche Schnitt hätte den höchsten erwarteten Erkenntnisgewinn?
- Wann ist genug?

Das wäre der eigentliche **Brillenladen-Agent**.

---

# 10. Minimaler Outreach-Satz nach einem erfolgreichen Test

> We tested a small alternative to persona-based agent specialization.
>
> Instead of assigning agents roles such as “expert”, “skeptic” or “reviewer”, we assigned orthogonal epistemic operations such as TIME/STATE, RELATION/INFORMATION and CAUSALITY/EVIDENCE.
>
> The question is not whether this makes the underlying model smarter, but whether it produces a less redundant and more controllable division of reasoning work.
>
> We call the intermediate representation an epistemic lens layer.

