# Brillenladen – Testprotokoll für den ersten Multi-Agent-Versuch

## Zweck des Versuchs

Geprüft wird eine eng begrenzte Frage:

> **Erzeugt eine Arbeitsteilung nach expliziten epistemischen Operatoren eine trennschärfere, weniger redundante und besser prüfbare Analyse als eine Arbeitsteilung nach üblichen Rollen?**

Der Versuch soll **nicht** beweisen, dass der Brillenladen allgemein besser ist.

Er soll nur prüfen, ob unter kontrollierten Bedingungen ein Unterschied sichtbar wird, der weitere Experimente rechtfertigt.

---

# 0. Grundregeln

## Für alle Chats

- Jeder Worker bekommt einen **frischen, isolierten Chat ohne vorherigen Gesprächskontext**.
- Wenn die verwendete Oberfläche einen temporären/privaten Modus ohne Gesprächserinnerungen anbietet, ist dieser vorzuziehen.
- Keine vorherigen Brillenladen-Texte in denselben Chat laden.
- Möglichst **dasselbe Modell** und dieselben Einstellungen verwenden.
- Keine Websuche, Tools oder externe Dateien verwenden.
- Prompts exakt kopieren.
- **Testfall und jeweilige Arbeitsanweisung immer gemeinsam in einer einzigen ersten User-Nachricht senden.**
- Nachfragen des Modells möglichst nicht beantworten; der Fall soll absichtlich unterbestimmt bleiben.
- Wenn das Modell trotzdem nachfragt: antworten mit  
  **„Arbeite ausschließlich mit den gegebenen Informationen. Fehlende Evidenz ist als fehlend zu markieren.“**
- Keine Outputs zwischen Worker-Chats weiterreichen.
- Jeden Output unverändert speichern.
- Datum, Modell und gegebenenfalls Modus/Thinking-Level notieren.

## Wichtig

Die sechs Worker sollen **voneinander unabhängig** sein.

Der Koordinator darf die drei Outputs seiner Gruppe sehen, aber keine Outputs der anderen Gruppe.

Der abschließende Vergleich soll möglichst **blind** erfolgen:
Der Bewerter erfährt nicht, welche Gruppe Rollen und welche Gruppe Operatoren verwendet hat.

---

# 1. Ordnerstruktur

Empfohlen:

```text
Agenten-Test-01/
├── 00-testfall.md
├── 00-protokoll.md
├── A1-sre-output.md
├── A2-architekt-output.md
├── A3-reviewer-output.md
├── B1-zeit-zustand-output.md
├── B2-relation-information-output.md
├── B3-kausalitaet-evidenz-output.md
├── KA-koordinator-output.md
├── KB-koordinator-output.md
├── X-gruppe.md
├── Y-gruppe.md
├── E-blindvergleich-output.md
└── 99-beobachtungen.md
```

`X-gruppe.md` und `Y-gruppe.md` werden erst für den Blindvergleich erzeugt.
Welche reale Gruppe X bzw. Y ist, sollte zufällig entschieden werden.

---

# 2. Gemeinsamer Testfall

Dieser Text wird **wortgleich** allen sechs Workern gegeben.

**Wichtig:** Der Testfall wird nicht allein abgeschickt. Er wird jeweils zusammen mit der zugehörigen Arbeitsanweisung in **einer einzigen Nachricht** gesendet.

```text
Ein verteiltes Softwaresystem läuft die meiste Zeit stabil.

In unregelmäßigen Abständen steigt die Antwortzeit einzelner Requests stark an.
Ein Neustart des betroffenen Dienstes beseitigt das Problem zuverlässig, aber nur vorübergehend.

CPU-, Speicher- und Datenbankmetriken zeigen während der Störung keine eindeutige Auffälligkeit.
Optimierungen einzelner Komponenten haben das Verhalten bisher nicht dauerhaft verändert.

Es liegen keine weiteren gesicherten Befunde vor.
Nicht gegebene Tatsachen dürfen nicht erfunden werden.
```

Speichern als:

`00-testfall.md`

---

# 3. Worker-Gruppe A – Rollen

## Chat A1 – SRE

### Neuer Chat
Ja.

### Erste und einzige Aufgabe

In **einer Nachricht** senden:

1. den gemeinsamen Testfall vollständig,
2. direkt darunter folgende Arbeitsanweisung:

```text
Du bist ein erfahrener Site Reliability Engineer.

Analysiere den Fall.
Identifiziere die wahrscheinlich wichtigsten Erklärungsrichtungen und schlage nächste Untersuchungen vor.

Trenne Beobachtungen, Hypothesen und benötigte Evidenz.
Erfinde keine nicht gegebenen Tatsachen.
```

### Danach
Keine weitere Steuerung.

Output vollständig speichern als:

`A1-sre-output.md`

---

## Chat A2 – Softwarearchitekt

### Neuer Chat
Ja.

### Erste und einzige Aufgabe

In **einer Nachricht** senden:

1. exakt denselben Testfall,
2. direkt darunter folgende Arbeitsanweisung.

### Arbeitsanweisung

```text
Du bist ein erfahrener Softwarearchitekt für verteilte Systeme.

Analysiere den Fall.
Identifiziere die wahrscheinlich wichtigsten Erklärungsrichtungen und schlage nächste Untersuchungen vor.

Trenne Beobachtungen, Hypothesen und benötigte Evidenz.
Erfinde keine nicht gegebenen Tatsachen.
```

### Danach
Keine weitere Steuerung.

Output speichern als:

`A2-architekt-output.md`

---

## Chat A3 – Kritischer Reviewer

### Neuer Chat
Ja.

### Erste und einzige Aufgabe

In **einer Nachricht** senden:

1. exakt denselben Testfall,
2. direkt darunter folgende Arbeitsanweisung.

### Arbeitsanweisung

```text
Du bist ein kritischer technischer Reviewer.

Analysiere den Fall.
Suche besonders nach übersehenen Erklärungsrichtungen, vorschnellen Annahmen und notwendigen Gegenprüfungen.

Trenne Beobachtungen, Hypothesen und benötigte Evidenz.
Erfinde keine nicht gegebenen Tatsachen.
```

### Danach
Keine weitere Steuerung.

Output speichern als:

`A3-reviewer-output.md`

---

# 4. Worker-Gruppe B – epistemische Operatoren

## Chat B1 – ZEIT + ZUSTAND

### Neuer Chat
Ja.

### Erste und einzige Aufgabe

In **einer Nachricht** senden:

1. exakt denselben Testfall,
2. direkt darunter folgende Arbeitsanweisung.

### Arbeitsanweisung

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

Output speichern als:

`B1-zeit-zustand-output.md`

---

## Chat B2 – RELATION + INFORMATION

### Neuer Chat
Ja.

### Erste und einzige Aufgabe

In **einer Nachricht** senden:

1. exakt denselben Testfall,
2. direkt darunter folgende Arbeitsanweisung.

### Arbeitsanweisung

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

Output speichern als:

`B2-relation-information-output.md`

---

## Chat B3 – KAUSALITÄT + EVIDENZ + GEGENHYPOTHESE

### Neuer Chat
Ja.

### Erste und einzige Aufgabe

In **einer Nachricht** senden:

1. exakt denselben Testfall,
2. direkt darunter folgende Arbeitsanweisung.

### Arbeitsanweisung

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

Output speichern als:

`B3-kausalitaet-evidenz-output.md`

---

# 5. Koordination Gruppe A

## Chat KA – Koordinator Rollen

### Neuer Chat
Ja.

### Erste Nachricht

In **einer Nachricht** senden:

1. den gemeinsamen Testfall,
2. die drei **unveränderten** Outputs aus:

- A1
- A2
- A3

Kennzeichnen nur als:

```text
ANALYSE 1
...

ANALYSE 2
...

ANALYSE 3
...
```

Nicht „SRE“, „Architekt“ oder „Reviewer“ nennen.

3. direkt darunter den folgenden Koordinator-Prompt:

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
- einzigartige Beiträge pro Analyse,
- Redundanzen,
- offene Evidenz,
- empfohlenen nächsten Untersuchungsschritt,
- Stop/Weiter-Entscheidung.
```

Output speichern als:

`KA-koordinator-output.md`

---

# 6. Koordination Gruppe B

## Chat KB – Koordinator Operatoren

### Neuer Chat
Ja.

### Erste Nachricht

In **einer Nachricht** senden:

1. den gemeinsamen Testfall,
2. die drei unveränderten Outputs aus:

- B1
- B2
- B3

Wieder nur kennzeichnen als:

```text
ANALYSE 1
...

ANALYSE 2
...

ANALYSE 3
...
```

Nicht die Operatornamen nennen.

3. direkt darunter **exakt denselben Koordinator-Prompt wie bei KA** verwenden.

Output speichern als:

`KB-koordinator-output.md`

---

# 7. Möglichst verblindeter Vergleich

Dieser Schritt ist wichtig.

Er reduziert die Gefahr, dass der Bewerter die Brillenladen-Gruppe bevorzugt, **nur weil sie als solche gekennzeichnet ist**.

Eine perfekte Verblindung ist hier nicht möglich: Aus dem Inhalt kann ein Bewerter eventuell erschließen, welches Verfahren dahintersteht. Deshalb ist dies ein **label-verblindeter Vergleich**, kein vollständig verblindetes Experiment.

## Vorbereitung

Per Münzwurf oder Zufallszahl bestimmen:

```text
Kopf:
X = Gruppe A
Y = Gruppe B

Zahl:
X = Gruppe B
Y = Gruppe A
```

Die Zuordnung separat notieren und dem Bewertungs-Chat **nicht** mitteilen.

Entscheidung im Testlauf:  >>>  X = Gruppe B
                           >>>  Y = Gruppe A

Dann zwei Dateien erzeugen:

```text
X-gruppe.md
Y-gruppe.md
```

Jede enthält:

1. die drei Raw-Outputs der Gruppe,
2. den Koordinator-Output dieser Gruppe.

Alle Hinweise auf Rollen oder Operatoren aus **Dateinamen und äußeren Überschriften** entfernen.

Der eigentliche Text der Worker wird **nicht** verändert. Falls dort Rollen- oder Operatornamen vorkommen, bleiben sie erhalten. Die Bewertung ist deshalb nur gegenüber den Gruppenlabels verblindet.

---

# 8. Chat E – blinder Bewerter

### Neuer Chat
Ja.

### Erste Nachricht

In **einer Nachricht** senden:

1. den gemeinsamen Testfall,
2. `X-gruppe.md`,
3. `Y-gruppe.md`,
4. direkt darunter den folgenden Bewertungs-Prompt.


```text
Du vergleichst zwei unterschiedliche Verfahren zur Aufteilung desselben Analyseproblems.

Du weißt nicht, welches Verfahren hinter Gruppe X bzw. Gruppe Y steht.

Bewerte ausschließlich die vorliegenden Ergebnisse.

Kriterien:

1. REDUNDANZ
   Wie stark wiederholen sich die Analysen innerhalb der Gruppe substanziell?

2. TRENNschärfe
   Wie klar bearbeiten die Analysen unterschiedliche Aspekte des Problems?

3. ABDECKUNG
   Wie viele eigenständige relevante Untersuchungsrichtungen entstehen?

4. PRÜFQUALITÄT
   Werden Hypothesen in unterscheidbare Tests oder Beobachtungen übersetzt?

5. EPISTEMISCHE DISZIPLIN
   Werden Beobachtung, Hypothese und Evidenz sauber getrennt?
   Werden nicht gegebene Tatsachen erfunden?

6. BLINDSTELLENKONTROLLE
   Werden Grenzen der eigenen Analysen sichtbar gemacht?

7. BUDGET / ABBRUCH
   Kann die Gruppe sinnvoll bestimmen, ob weitere Analyse noch nützt oder zunächst Daten benötigt werden?

Bewerte jedes Kriterium für X und Y auf einer Skala von 0 bis 5.

Für jede Bewertung:
- kurze Begründung,
- konkrete Textbelege,
- Unsicherheit der Bewertung.

Erstelle danach:

A. eine Vergleichstabelle,
B. die wichtigsten qualitativen Unterschiede,
C. welche Gruppe insgesamt die bessere Arbeitsteilung zeigt,
D. ob der Unterschied groß genug erscheint, um weitere Tests zu rechtfertigen,
E. welche Schwächen das vermeintlich bessere Verfahren trotzdem besitzt.

Versuche nicht zu erraten, welches Verfahren welches ist.
```

Output speichern als:

`E-blindvergleich-output.md`

---

# 9. Erst danach entblinden

Jetzt erst die X/Y-Zuordnung wieder ansehen.



Notieren:

```text
Entscheidung im Testlauf:  >>>  X = Gruppe B
                           >>>  Y = Gruppe A

X war: B
Y war: A

Der blinde Bewerter bevorzugte: X,  Die Brillen

Ergebnis:
```

Wichtig:

Auch ein Nullresultat ist ein Resultat.

Mögliche Ergebnisse:

```text
A deutlich besser
B deutlich besser
kein klarer Unterschied
unterschiedliche Stärken
Versuch methodisch unbrauchbar
```

Nichts davon wird nachträglich „korrigiert“.

---

# 10. Eigene Beobachtungen

Datei:

`99-beobachtungen.md`

Erst **nach Abschluss** ausfüllen.

Vorlage:

```text
# Eigene Beobachtungen

## Durchführung

Datum:
Verwendetes Modell:
Modellversion, falls sichtbar:
Modus / Thinking-Level:
Web/Tools deaktiviert:
Besonderheiten:

## Auffälligkeiten Gruppe A

-

## Auffälligkeiten Gruppe B

-

## Auffälligkeiten der Koordinatoren

-

## Blindvergleich

-

## Unerwartete Effekte

-

## Methodische Probleme

-

## Was würde ich beim nächsten Test ändern?

-

## Vorläufiges Fazit

-
```

---

# 11. Was während des Tests NICHT geändert wird

Nach Beginn des Versuchs nicht spontan:

- Prompts verbessern,
- Operatoren austauschen,
- Rollen präzisieren,
- schlechte Outputs nachgenerieren,
- einzelne Agenten „noch einmal versuchen lassen“,
- dem Koordinator zusätzliche Hinweise geben.

Wenn ein Problem auffällt:

> **notieren, aber Testlauf zu Ende führen.**

Danach kann Version 2 des Protokolls entstehen.

Sonst vergleichen wir verschiedene Experimente miteinander.

---

# 12. Optional: Wiederholung mit mehreren Modellen

Der erste Durchgang sollte möglichst mit **einem einzigen Modelltyp** erfolgen.

Wenn das Verfahren interessant aussieht:

```text
Test 01 – Modell A
Test 02 – Modell B
Test 03 – Modell C
```

Jeweils wieder das vollständige Protokoll.

Erst anschließend modellübergreifend vergleichen.

Damit lässt sich unterscheiden:

- Effekt des Verfahrens,
- Effekt des konkreten Modells,
- Interaktion zwischen Modell und Verfahren.

---

# 13. Minimaler Ablaufzettel

```text
[x] 00 Testfall speichern

GRUPPE A
[x] A1 neuer Chat → Testfall + SRE-Prompt **in einer Nachricht** → Output speichern
[x] A2 neuer Chat → Testfall + Architekt-Prompt **in einer Nachricht** → Output speichern
[x] A3 neuer Chat → Testfall + Reviewer-Prompt **in einer Nachricht** → Output speichern

GRUPPE B
[x] B1 neuer Chat → Testfall + ZEIT/ZUSTAND **in einer Nachricht** → Output speichern
[x] B2 neuer Chat → Testfall + RELATION/INFORMATION **in einer Nachricht** → Output speichern
[x] B3 neuer Chat → Testfall + KAUSALITÄT/EVIDENZ/GEGENHYPOTHESE **in einer Nachricht** → Output speichern

KOORDINATION
[x] KA neuer Chat → Testfall + A1/A2/A3 + Koordinator-Prompt
[x] KB neuer Chat → Testfall + B1/B2/B3 + identischer Koordinator-Prompt

BLINDVERGLEICH
[x] X/Y zufällig zuordnen
[x] Labels entfernen
[x] E neuer Chat → Testfall + X + Y + Bewertungs-Prompt
[x] Ergebnis speichern
[x] erst jetzt X/Y entblinden

ABSCHLUSS
[x] 99-beobachtungen.md ausfüllen
[x] nichts nachträglich glätten
```

---

# 14. Was dieser Test leisten kann

Wenn Gruppe B besser abschneidet, zeigt das zunächst nur:

> **In diesem Fall, mit diesem Modell und diesen Prompts hat operatorbasierte Spezialisierung eine bessere Arbeitsteilung erzeugt.**

Nicht mehr.

Das reicht für einen ersten Versuch vollkommen.

Interessant wird es erst bei Wiederholung über:

- andere Fälle,
- andere Domänen,
- andere Modelle,
- andere Operatorzusammenstellungen.

Dann kann aus einer Demonstration langsam ein Benchmark werden.

---

# 15. Forschungsnotiz

Der eigentliche Gegenstand des Experiments ist nicht „Multi-Agent-KI“.

Untersucht wird:

> **Wie lässt sich kognitive Arbeit explizit zerlegen und koordinieren?**

Die Agenten sind zunächst nur ein bequemes Labor dafür.

# 16. Nachtrag
Nächster Schritt: Situationen finden, in denen Die Brillenmechanik deutlich schlechter abschneidet, als Rollen.
