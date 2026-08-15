# Problem-Landkarte des Brillenladens

## Leitfrage

> **Wer hat bereits ein Problem, das eine explizite epistemische Zwischenschicht möglicherweise löst?**

Der Brillenladen ist dort interessant, wo ein KI-System grundsätzlich leistungsfähig genug ist, aber die **Wahl der Analyseperspektive** zu implizit, zu grob, zu redundant oder zu teuer bleibt.

Der gemeinsame Problemkern lautet:

> **Reasoning capability is available; perspective selection is underspecified.**

Oder einfacher:

> **Das Modell kann genug. Aber es schaut nicht zuverlässig an der richtigen Stelle hin.**

---

# 1. Agenten- und Reasoning-Systeme

## Problem

Agenten werden häufig über Rollen beschrieben:

- „Sei ein Kritiker.“
- „Sei ein Finanzexperte.“
- „Sei ein Skeptiker.“
- „Suche Gegenargumente.“

Solche Rollen sind anschaulich, aber epistemisch unscharf.

Mehrere Agenten produzieren dadurch oft:

- Redundanz,
- ähnliche Analysen in anderer Sprache,
- unnötige Rechenkosten,
- schwer nachvollziehbare Arbeitsteilung,
- unklare Abbruchbedingungen.

## Typische Notlösung

- immer mehr Rollen,
- längere Systemprompts,
- zusätzliche Agenten,
- nachträgliche Synthese,
- mehr Reasoning-Tokens.

## Brillenladen-Mechanismus

Agenten oder Reasoning-Schritte werden nicht primär durch Persönlichkeit, sondern durch **unterschiedliche Analyseoperationen** definiert.

Beispiel:

```text
Agent A:
ZEIT + RÜCKKOPPLUNG + SKALA

Agent B:
ANREIZ + MACHT + ROLLE

Agent C:
EVIDENZ + GEGENHYPOTHESE + KAUSALITÄT
```

Eine Metaebene prüft:

- Welche Perspektive fehlt?
- Welche Agenten sind redundant?
- Welche Ergebnisse widersprechen sich wirklich?
- Lohnt ein weiterer Agent?
- Wann ist genug analysiert?

## 5-Minuten-Demo

Gib drei Agenten denselben Organisationsfall.

### Variante A
Rollen:
- Optimist
- Skeptiker
- Experte

### Variante B
Operatoren:
- ANREIZ + MACHT
- INFORMATION + ROLLE
- ZEIT + RÜCKKOPPLUNG

Vergleiche:

- Redundanz,
- Unterschiedlichkeit der Befunde,
- Begründbarkeit der Perspektivwahl,
- Kosten,
- Qualität der Synthese.

## Ansprechpartner

- AI System Architects
- Agentic AI Engineers
- Reasoning Researchers
- Multi-Agent Framework Developers
- Applied AI Teams

---

# 2. Debugging, SRE und technische Diagnose

## Problem

Bei komplexen technischen Störungen ist oft nicht Wissen das Problem.

Das Problem ist der **Suchraum**.

Ein LLM kann viele plausible Ursachen nennen und trotzdem auf der falschen Ebene suchen.

Typische Situationen:

- intermittierende Fehler,
- Neustart hilft nur vorübergehend,
- Einzelkomponenten erscheinen gesund,
- Standardmetriken zeigen nichts Auffälliges,
- mehrere Optimierungen bleiben wirkungslos.

## Typische Notlösung

- längere Log-Analyse,
- mehr Metriken,
- mehr Hypothesen,
- „denk Schritt für Schritt“,
- breit gestreute Root-Cause-Listen.

## Brillenladen-Mechanismus

Vor der Ursachenhypothese wird explizit gefragt:

> Welche Schnitte sind für dieses Fehlerbild wahrscheinlich ergiebig?

Beispiel:

```text
ZEIT
+ ZUSTAND
+ RELATION
+ INFORMATION
```

Erst danach:

- Hypothesen,
- Messplan,
- Evidenz,
- Reproduktion.

## 5-Minuten-Demo

Szene:

> Ein System läuft meist stabil. Gelegentlich steigt die Latenz stark. Neustarts helfen zuverlässig, aber nur vorübergehend. Optimierungen einzelner Komponenten ändern nichts. Standardmetriken zeigen kein klares Muster.

Vergleich:

### Normale Analyse
„Nenne mögliche Ursachen.“

### Brillenladen
„Wähle zunächst maximal vier möglichst unterschiedliche Operatoren. Begründe die Wahl. Formuliere daraus einen Mess- und Prüfplan. Erfinde keine Befunde.“

Vergleiche die Qualität des Suchraums.

## Ansprechpartner

- SRE Teams
- Observability-Plattformen
- Incident-Response-Tools
- DevOps Copilot Teams
- AI-assisted Debugging Research

---

# 3. Research Assistants und Wissenssysteme

## Problem

LLMs können Texte hervorragend:

- zusammenfassen,
- clustern,
- vergleichen,
- zitieren.

Dabei geht jedoch leicht verloren, **wie unterschiedlich die Quellen denselben Gegenstand schneiden**.

Zwei Arbeiten können scheinbar widersprechen, obwohl sie:

- unterschiedliche Skalen betrachten,
- andere Kausalbegriffe verwenden,
- andere Evidenzformen akzeptieren,
- Zustände statt Prozesse untersuchen,
- individuelle statt institutionelle Ebenen wählen.

## Typische Notlösung

- thematische Cluster,
- Embeddings,
- Keyword-Vergleiche,
- klassische Literature Reviews,
- abstrakte „Pros/Cons“-Listen.

## Brillenladen-Mechanismus

**Epistemische Faktorisierung**:

> Welche minimale Operatorenkombination erklärt den charakteristischen Blick dieses Textes?

Danach:

- Quellen nach epistemischer Signatur gruppieren,
- Blindstellen vergleichen,
- echte Widersprüche von verschiedenen Schnitten unterscheiden,
- unterrepräsentierte Perspektiven erkennen.

## 5-Minuten-Demo

Nimm drei Texte zum selben Thema.

Für jeden Text:

```text
dominante Operatoren
unterrepräsentierte Operatoren
Evidenzform
Skala
charakteristische Blindstelle
```

Dann frage:

> Welche Texte widersprechen sich wirklich, und welche stellen nur verschiedene Fragen?

## Ansprechpartner

- Research Assistant Developers
- Knowledge Management Teams
- Literature Review Tools
- Scientific AI
- Enterprise Search / RAG Teams

---

# 4. KI-Tutoren und Bildung

## Problem

Ein leistungsfähiger Tutor kann zum Problem werden, wenn er zu schnell antwortet.

Der Schüler lernt dann:

> Frage stellen → Antwort erhalten

statt:

> Situation → Struktur → Frage → Untersuchung

## Typische Notlösung

- sokratische Prompts,
- „gib nicht sofort die Lösung“,
- feste Tutor-Personas,
- Schwierigkeitsstufen,
- Quiz-Modi.

## Brillenladen-Mechanismus

Der Tutor kann statt einer Antwort zunächst **epistemische Bewegungen** anbieten.

Zum Beispiel:

```text
ZEIT:
Was hat sich verändert?

PERSPEKTIVE:
Aus wessen Sicht sieht die Sache anders aus?

EVIDENZ:
Woher wissen wir das?

GEGENHYPOTHESE:
Welche andere Erklärung wäre möglich?

SKALA:
Was ändert sich, wenn wir hinein- oder herauszoomen?
```

Der Schüler muss den Operatornamen nicht kennen.

Er erlebt nur bessere Fragen.

## 5-Minuten-Demo

Gleiche Schülerfrage an zwei Tutoren.

### Tutor A
Erklärt sofort.

### Tutor B
Wählt zunächst zwei passende Perspektivfragen und lässt den Schüler entscheiden, welcher Spur er folgen möchte.

Vergleiche:

- Eigenaktivität,
- Qualität der Folgefragen,
- Transfer,
- Abhängigkeit von der KI.

## Ansprechpartner

- AI Tutor Teams
- EdTech
- Didaktik-Forschung
- Hochschuldidaktik
- Lehrkräfte mit KI-Schwerpunkt

---

# 5. Strategie, Risiko und Red Teams

## Problem

Entscheidungsunterlagen erscheinen oft sachlich vollständig, obwohl sie bereits stark gerahmt sind.

Gefahren:

- Groupthink,
- implizite Annahmen,
- gleiche Perspektive bei allen Beteiligten,
- falsche Sicherheit durch sprachliche Kohärenz,
- blinde Flecken in Szenarien.

## Typische Notlösung

- Devil’s Advocate,
- Red Team,
- SWOT,
- Szenarioanalyse,
- „Was haben wir übersehen?“

## Brillenladen-Mechanismus

Zwei Richtungen:

### Vorwärts
Welche Perspektiven sollten wir ergänzen?

### Rückwärts
Welche Perspektive trägt die Vorlage bereits?

Beispiel:

```text
Beschlussvorlage
≈
KAUSALITÄT
+ ANREIZ
+ ZUSTAND
```

Mögliche Gegenprobe:

```text
ZEIT
+ RÜCKKOPPLUNG
+ MACHT
```

Nicht mit dem Ziel, die erste Sicht zu widerlegen.

Sondern um zu prüfen, **was sie strukturell schlecht sehen kann**.

## 5-Minuten-Demo

Nimm eine kurze Strategievorlage.

1. Faktorisiere die dominante Perspektive.
2. Benenne genau einen möglichst orthogonalen Gegen-Schnitt.
3. Prüfe, ob dieser die Entscheidung verändert.
4. Stoppe, wenn kein relevanter Erkenntnisgewinn entsteht.

## Ansprechpartner

- Strategy Teams
- Risk Management
- Red Teams
- Policy Analysis
- Corporate Intelligence

---

# 6. Journalismus, Medien- und Diskursanalyse

## Problem

Öffentliche Darstellungen desselben Geschehens unterscheiden sich nicht nur in Fakten oder Meinung.

Sie unterscheiden sich häufig schon darin:

- welche Akteure sichtbar werden,
- welche Zeitskala gewählt wird,
- ob Ursachen oder Normen dominieren,
- ob Institutionen berücksichtigt werden,
- welche Evidenzformen zählen.

## Typische Notlösung

- Bias-Klassifikation,
- Sentiment,
- Framing-Labels,
- politische Links/Rechts-Zuordnung,
- Fact Checking.

## Brillenladen-Mechanismus

Nicht zuerst:

> Wer hat recht?

Sondern:

> Welche Art von Welt erzeugt diese Darstellung?

Ausgabe:

```text
dominante Operatoren
sichtbar gemachte Strukturen
unterrepräsentierte Schnitte
mögliche Gegenperspektive
offene Evidenzfragen
```

Das vermeidet vorschnelle Psychologisierung oder Parteinahme.

## 5-Minuten-Demo

Zwei Berichte über dasselbe Ereignis.

Frage:

> Faktorisiere beide Darstellungen. Wo widersprechen sich Tatsachenbehauptungen? Wo unterscheiden sich lediglich die epistemischen Schnitte?

## Ansprechpartner

- Investigative Journalism
- Media Analysis
- Fact-Checking Organizations
- Newsroom AI Teams
- Political Communication Research

---

# 7. Reasoning-Effizienz und epistemisches Routing

## Problem

Ein leistungsfähiges Modell kann viele Analysebewegungen ausführen.

Aber wenn es jedes Mal neu bestimmen muss,

- welche Perspektive relevant ist,
- welche Kombination sinnvoll ist,
- welche redundant ist,
- wann gewechselt werden sollte,

entsteht zusätzlicher Aufwand.

## Typische Notlösung

- mehr Test-Time Compute,
- längere Reasoning-Prozesse,
- mehr Agenten,
- heuristische Router,
- domänenspezifische Prompts.

## Brillenladen-Mechanismus

Häufig erfolgreiche epistemische Bewegungsfiguren könnten gelernt oder vorkompiliert werden.

Dann entsteht ein **epistemischer Router**:

```text
Problemstruktur
→ wahrscheinliche Operatorenregion
→ kleine Arbeitsbrille
→ Reasoning
→ Restproblem
→ Erweiterung oder Stopp
```

Das fügt nicht notwendig neue Grundfähigkeiten hinzu.

Es könnte aber Rechen- und Kontextressourcen freisetzen.

Dadurch steigt möglicherweise die **effektive kognitive Bandbreite**.

## 5-Minuten-Demo

Noch kein belastbarer Benchmark.

Ein erster Test könnte zwei Verfahren vergleichen:

### A
freie Operatorensuche über den gesamten Katalog

### B
vorgegebene kleine Kandidatenmenge aus einem Router

Messgrößen:

- Tokenverbrauch,
- Laufzeit,
- Anzahl unnötiger Operatoren,
- Qualität des Endergebnisses,
- Zahl sinnvoll erkannter Blindstellen.

## Ansprechpartner

- Reasoning Efficiency Research
- Model Routing Research
- Test-Time Compute Research
- LLM Architecture Teams
- Sparse / Modular AI Research

---

# Priorisierung

## Stufe 1 – sofort demonstrierbar

1. Agenten- und Reasoning-Systeme
2. Debugging / technische Diagnose
3. KI-Tutoren
4. Strategie / Red Teaming

Hier lässt sich der Nutzen mit kleinen kontrollierten Demos zeigen.

## Stufe 2 – sehr interessant, aber evaluierungsintensiver

5. Research Assistants
6. Journalismus / Diskursanalyse

Hier braucht es stabilere Vergleichs- und Faktorisierungstests.

## Stufe 3 – Forschungsrichtung

7. Epistemisches Routing / Training

Hier ist die Idee konzeptionell stark, aber noch kaum experimentell geprüft.

---

# Outreach-Regel

Nicht beginnen mit:

> Ich habe eine epistemische Zwischensprache entwickelt.

Sondern mit dem Problem des Empfängers.

Beispiele:

### Agenten

> Ihre Agenten liefern unterschiedliche Texte, aber nicht unbedingt unterschiedliche Analysen?

### Debugging

> Ihr LLM kann hundert Ursachen nennen, aber nicht entscheiden, in welchem Fehlerraum es zuerst suchen sollte?

### Forschung

> Ihr Research Assistant fasst Quellen zusammen, verliert dabei aber die unterschiedlichen Denkperspektiven der Quellen?

### Bildung

> Ihr KI-Tutor beantwortet Fragen besser, als er Denken auslöst?

### Strategie

> Ihr Red Team produziert Gegenargumente, aber keine wirklich andere Perspektive?

Erst danach:

> Dafür experimentiere ich mit einer kleinen Zwischenschicht aus expliziten Analyseoperatoren.

---

# Minimaler Pitch

> **Der Brillenladen macht nicht das Modell klüger.**
>
> Er versucht expliziter zu machen, **wie das vorhandene Können auf ein Problem gerichtet wird**.
>
> Statt nur nach Antworten zu fragen, behandelt er Perspektivwahl, Perspektivwechsel, Blindstellen und Abbruch als eigene Operationen.

---

# Der eigentliche Test

Für jede Zielgruppe gilt letztlich dieselbe Frage:

> **Verbessert eine kleine explizite epistemische Zwischenschicht die Analyse gegenüber dem bisherigen Verfahren – bei vertretbaren zusätzlichen Kosten?**

Wenn nein, braucht diese Zielgruppe den Brillenladen nicht.

Wenn ja, haben wir einen Anwendungsfall.
