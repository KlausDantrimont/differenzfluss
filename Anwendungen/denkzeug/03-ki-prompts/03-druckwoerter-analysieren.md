# 03 – Druckwörter analysieren

## Worum es geht

Manche Wörter beschreiben nicht nur.

Sie drücken.

Sie markieren.

Sie werten auf oder ab.

Sie machen bestimmte Handlungen wahrscheinlicher.

Denkzeug nennt sie:

> Wörter mit eingebauter Richtung.

Beispiele:

```text
Opfer
Verräter
feige
mutig
normal
unnormal
respektlos
toxisch
dumm
echter Freund
richtige Seite
````

KI kann helfen, solche Wörter sichtbar zu machen.

Aber sie soll nicht entscheiden, welches Wort „verboten“ ist.

Sie soll zeigen:

> Was macht dieses Wort in dieser Situation?

---

## Grundprompt

```text 
Arbeite mit dem Denkzeug-Modell.

Analysiere diesen Satz auf Wörter mit eingebauter Richtung.

Satz:
[Satz einfügen]

Bitte beantworte:

1. Welche Wörter oder Formulierungen haben eine eingebaute Bewertung?
2. Welche Wörter erzeugen Druck?
3. Wer wird dadurch aufgewertet?
4. Wer wird dadurch abgewertet?
5. Welcher innere Hebel wird angesprochen?
6. Welcher äußere Griff wird benutzt?
7. Welche Handlung wird dadurch wahrscheinlicher oder unwahrscheinlicher?
8. Welche konkrete Beobachtung könnte hinter dem Wort stehen?
9. Wie könnte man den Satz genauer und weniger markierend formulieren?

Wichtig:
- Verbiete das Wort nicht.
- Analysiere seine Wirkung.
- Bewerte keine Person als Ganzes.
- Unterscheide zwischen Beschreibung und Markierung.
- Ziel ist mehr Genauigkeit und Spielraum.
```

---

## Beispielprompt 1: „Opfer“

```text 
Arbeite mit dem Denkzeug-Modell.

Analysiere diesen Satz auf Wörter mit eingebauter Richtung.

Satz:
„Wer das meldet, ist ein Opfer.“

Bitte beantworte:

1. Welche Wörter oder Formulierungen haben eine eingebaute Bewertung?
2. Welche Wörter erzeugen Druck?
3. Wer wird dadurch aufgewertet?
4. Wer wird dadurch abgewertet?
5. Welcher innere Hebel wird angesprochen?
6. Welcher äußere Griff wird benutzt?
7. Welche Handlung wird dadurch wahrscheinlicher oder unwahrscheinlicher?
8. Welche konkrete Beobachtung könnte hinter dem Wort stehen?
9. Wie könnte man den Satz genauer und weniger markierend formulieren?
```

---

## Erwartete gute Antwort

```text 
1. Druckwort: „Opfer“.
2. Das Wort erzeugt Druck, weil niemand als schwach oder peinlich gelten will.
3. Aufgewertet werden die, die nicht melden und scheinbar „stark“ bleiben.
4. Abgewertet wird die Person, die Hilfe holen oder etwas melden will.
5. Hebel: Angst vor Beschämung, Wunsch stark zu wirken.
6. Griff: Abwertung.
7. Wahrscheinlicher wird Schweigen. Unwahrscheinlicher wird Hilfe holen oder Grenzen setzen.
8. Konkrete Beobachtung könnte sein: Jemand überlegt, etwas einer Lehrkraft oder Vertrauensperson zu sagen.
9. Genauer: „Ich möchte nicht, dass du das meldest, weil ich Angst vor den Folgen habe.“
```

---

## Prompt: Beschreibung oder Markierung?

```text 
Arbeite mit dem Denkzeug-Modell.

Prüfe, ob dieser Satz eher beschreibt oder markiert.

Satz:
[Satz einfügen]

Bitte beantworte:
1. Welche konkrete Beobachtung enthält der Satz?
2. Welche Deutung enthält der Satz?
3. Welche Bewertung enthält der Satz?
4. Wird ein Verhalten beschrieben oder eine Person markiert?
5. Welche genauere Formulierung wäre möglich?
```

### Beispiel

```text 
Arbeite mit dem Denkzeug-Modell.

Prüfe, ob dieser Satz eher beschreibt oder markiert.

Satz:
„Sie ist toxisch.“

Bitte beantworte:
1. Welche konkrete Beobachtung enthält der Satz?
2. Welche Deutung enthält der Satz?
3. Welche Bewertung enthält der Satz?
4. Wird ein Verhalten beschrieben oder eine Person markiert?
5. Welche genauere Formulierung wäre möglich?
```

### Mögliche gute Ausgabe

```text 
1. Konkrete Beobachtung: Im Satz selbst wird keine konkrete Beobachtung genannt.
2. Deutung: Das Verhalten der Person wird als schädlich erlebt.
3. Bewertung: Die Person wird stark negativ bewertet.
4. Der Satz markiert die Person als Ganzes.
5. Genauer wäre: „Sie hat mir gedroht, private Dinge weiterzuerzählen, wenn ich nicht mache, was sie will.“
```

---

## Prompt: Druckwort genauer machen

```text 
Arbeite mit dem Denkzeug-Modell.

Mache dieses Druckwort genauer.

Druckwort:
[Wort einfügen]

Satz:
[Satz einfügen]

Bitte beantworte:
1. Was könnte mit dem Wort konkret gemeint sein?
2. Welche verschiedenen Bedeutungen kann das Wort haben?
3. Welche Bedeutung passt hier wahrscheinlich?
4. Welche Gefahr entsteht, wenn das Wort ungenau bleibt?
5. Formuliere drei genauere Alternativen.
```

### Beispiel

```text 
Arbeite mit dem Denkzeug-Modell.

Mache dieses Druckwort genauer.

Druckwort:
„respektlos“

Satz:
„Das war respektlos.“

Bitte beantworte:
1. Was könnte mit dem Wort konkret gemeint sein?
2. Welche verschiedenen Bedeutungen kann das Wort haben?
3. Welche Bedeutung passt hier wahrscheinlich?
4. Welche Gefahr entsteht, wenn das Wort ungenau bleibt?
5. Formuliere drei genauere Alternativen.
```

### Mögliche gute Ausgabe

```text 
1. Gemeint sein könnte: beleidigen, unterbrechen, widersprechen, eine Grenze nicht beachten oder unfreundlich sprechen.
2. „Respektlos“ kann echte Verletzung beschreiben, aber auch benutzt werden, um Widerspruch zu stoppen.
3. Ohne Kontext ist nicht sicher, was gemeint ist.
4. Die Gefahr: Eine konkrete Handlung wird nicht geklärt, sondern die Person wird markiert.
5. Genauere Alternativen:
   - „Du hast mich unterbrochen.“
   - „Dein Ton hat mich verletzt.“
   - „Du hast meiner Aussage widersprochen. Ich möchte verstehen, warum.“
```

---

## Prompt: Eingebaute Bewertung finden

```text 
Arbeite mit dem Denkzeug-Modell.

Finde die eingebaute Bewertung in diesen Wörtern oder Formulierungen.

Liste:
[Wörter oder Formulierungen einfügen]

Erstelle eine Tabelle mit:
1. Wort/Formulierung
2. eingebaute Bewertung
3. möglicher Hebel
4. mögliche Wirkung
5. neutralere oder genauere Formulierung
```

### Beispiel

```text 
Arbeite mit dem Denkzeug-Modell.

Finde die eingebaute Bewertung in diesen Wörtern oder Formulierungen.

Liste:
- Opfer
- Verräter
- echter Freund
- normal
- feige
- respektlos
- toxisch

Erstelle eine Tabelle mit:
1. Wort/Formulierung
2. eingebaute Bewertung
3. möglicher Hebel
4. mögliche Wirkung
5. neutralere oder genauere Formulierung
```

---

## Prompt: Wortwirkung auf Handlung prüfen

```text 
Arbeite mit dem Denkzeug-Modell.

Prüfe, welche Handlung durch dieses Wort wahrscheinlicher oder unwahrscheinlicher wird.

Satz:
[Satz einfügen]

Bitte beantworte:
1. Welches Wort macht Druck?
2. Welche Handlung soll wahrscheinlicher werden?
3. Welche Handlung soll unwahrscheinlicher werden?
4. Wer gewinnt dadurch Einfluss?
5. Welche Gegenfrage könnte die Wirkung sichtbar machen?
```

### Beispiel

```text 
Arbeite mit dem Denkzeug-Modell.

Prüfe, welche Handlung durch dieses Wort wahrscheinlicher oder unwahrscheinlicher wird.

Satz:
„Nur echte Freunde halten dicht.“

Bitte beantworte:
1. Welches Wort macht Druck?
2. Welche Handlung soll wahrscheinlicher werden?
3. Welche Handlung soll unwahrscheinlicher werden?
4. Wer gewinnt dadurch Einfluss?
5. Welche Gegenfrage könnte die Wirkung sichtbar machen?
```

### Mögliche gute Ausgabe

```text 
1. Druckformulierung: „echte Freunde“.
2. Wahrscheinlicher wird Schweigen.
3. Unwahrscheinlicher wird Reden, Hilfe holen oder Grenzen setzen.
4. Einfluss gewinnt die Person oder Gruppe, die Schweigen verlangt.
5. Gegenfrage: Heißt Freundschaft, dass ich auch bei etwas Falschem schweigen muss?
```

---

## Prompt: Wort als Gruppensignal prüfen

```text 
Arbeite mit dem Denkzeug-Modell.

Prüfe, ob dieses Wort als Gruppensignal wirkt.

Wort oder Satz:
[Wort oder Satz einfügen]

Bitte beantworte:
1. Welche Gruppe benutzt oder versteht dieses Wort wahrscheinlich?
2. Wer gehört dadurch dazu?
3. Wer steht draußen?
4. Welche Bewertung wird mittransportiert?
5. Wird das Wort eher zur Verständigung oder zur Abgrenzung benutzt?
6. Welche genauere Frage könnte helfen?
```

### Beispiel

```text 
Arbeite mit dem Denkzeug-Modell.

Prüfe, ob dieses Wort als Gruppensignal wirkt.

Wort oder Satz:
„Das ist cringe.“

Bitte beantworte:
1. Welche Gruppe benutzt oder versteht dieses Wort wahrscheinlich?
2. Wer gehört dadurch dazu?
3. Wer steht draußen?
4. Welche Bewertung wird mittransportiert?
5. Wird das Wort eher zur Verständigung oder zur Abgrenzung benutzt?
6. Welche genauere Frage könnte helfen?
```

---

## Prompt: Normalitätsdruck prüfen

```text 
Arbeite mit dem Denkzeug-Modell.

Analysiere diesen Satz auf Normalitätsdruck.

Satz:
[Satz einfügen]

Bitte beantworte:
1. Wo kommt das Wort „normal“ oder eine ähnliche Idee vor?
2. Was gilt als normal?
3. Was wird als unnormal markiert?
4. Bedeutet „nicht normal“ hier selten, ungewohnt, falsch oder unerwünscht?
5. Welcher Hebel wird berührt?
6. Welche Gegenfrage öffnet den Raum?
```

### Beispiel

```text 
Arbeite mit dem Denkzeug-Modell.

Analysiere diesen Satz auf Normalitätsdruck.

Satz:
„Das ist doch nicht normal.“

Bitte beantworte:
1. Wo kommt das Wort „normal“ oder eine ähnliche Idee vor?
2. Was gilt als normal?
3. Was wird als unnormal markiert?
4. Bedeutet „nicht normal“ hier selten, ungewohnt, falsch oder unerwünscht?
5. Welcher Hebel wird berührt?
6. Welche Gegenfrage öffnet den Raum?
```

### Mögliche gute Ausgabe

```text 
1. Das Wort „normal“ ist der zentrale Druckbegriff.
2. Als normal gilt offenbar das, was die sprechende Person erwartet oder akzeptiert.
3. Markiert wird etwas als abweichend.
4. Unklar ist, ob „nicht normal“ selten, ungewohnt oder moralisch falsch bedeutet.
5. Hebel: Wunsch, dazuzugehören und nicht komisch zu wirken.
6. Gegenfrage: Was meinst du mit normal genau?
```

---

## Prompt: Moralische Markierung prüfen

```text 
Arbeite mit dem Denkzeug-Modell.

Analysiere diesen Satz auf moralische Markierung.

Satz:
[Satz einfügen]

Bitte beantworte:
1. Welche Wörter stellen jemanden moralisch gut oder schlecht dar?
2. Welche Handlung oder Meinung wird moralisch aufgeladen?
3. Welcher Hebel wird berührt?
4. Wird begründet oder beschämt?
5. Welche Gegenfrage öffnet den Raum?
```

### Beispiel

```text 
Arbeite mit dem Denkzeug-Modell.

Analysiere diesen Satz auf moralische Markierung.

Satz:
„Wer dagegen ist, ist ein schlechter Mensch.“

Bitte beantworte:
1. Welche Wörter stellen jemanden moralisch gut oder schlecht dar?
2. Welche Handlung oder Meinung wird moralisch aufgeladen?
3. Welcher Hebel wird berührt?
4. Wird begründet oder beschämt?
5. Welche Gegenfrage öffnet den Raum?
```

---

## Prompt: Aufwertung und Abwertung finden

```text 
Arbeite mit dem Denkzeug-Modell.

Analysiere, wer in diesem Satz aufgewertet und wer abgewertet wird.

Satz:
[Satz einfügen]

Bitte beantworte:
1. Wer oder was wird aufgewertet?
2. Durch welche Wörter?
3. Wer oder was wird abgewertet?
4. Durch welche Wörter?
5. Welche Gruppe entsteht dadurch?
6. Welche Handlung wird wahrscheinlicher?
7. Welche neutralere Formulierung wäre möglich?
```

### Beispiel

```text 
Arbeite mit dem Denkzeug-Modell.

Analysiere, wer in diesem Satz aufgewertet und wer abgewertet wird.

Satz:
„Nur mutige Leute machen mit. Der Rest kneift.“

Bitte beantworte:
1. Wer oder was wird aufgewertet?
2. Durch welche Wörter?
3. Wer oder was wird abgewertet?
4. Durch welche Wörter?
5. Welche Gruppe entsteht dadurch?
6. Welche Handlung wird wahrscheinlicher?
7. Welche neutralere Formulierung wäre möglich?
```

---

## Prompt: Genauer formulieren

```text 
Arbeite mit dem Denkzeug-Modell.

Formuliere diesen Satz genauer und weniger markierend.

Satz:
[Satz einfügen]

Bitte gib aus:
1. ursprünglicher Satz
2. markierende Wörter
3. mögliche konkrete Beobachtung
4. genauere Formulierung
5. ruhige Nachfrage
```

### Beispiel

```text 
Arbeite mit dem Denkzeug-Modell.

Formuliere diesen Satz genauer und weniger markierend.

Satz:
„Du machst immer Drama.“

Bitte gib aus:
1. ursprünglicher Satz
2. markierende Wörter
3. mögliche konkrete Beobachtung
4. genauere Formulierung
5. ruhige Nachfrage
```

### Mögliche gute Ausgabe

```text 
1. Ursprünglicher Satz: Du machst immer Drama.
2. Markierende Wörter: „immer“, „Drama“.
3. Mögliche Beobachtung: Die Person hat gesagt, dass sie verletzt ist oder ein Problem ansprechen möchte.
4. Genauere Formulierung: „Du hast gesagt, dass dich die Situation verletzt hat.“
5. Ruhige Nachfrage: „Was genau hat dich verletzt?“
```

---

## Prompt: Druckwörter-Liste aus einem Text ziehen

```text 
Arbeite mit dem Denkzeug-Modell.

Untersuche diesen Text auf Druckwörter.

Text:
[Text einfügen]

Erstelle eine Liste mit:
1. Druckwort oder Druckformulierung
2. eingebaute Bewertung
3. angesprochener Hebel
4. mögliche Wirkung
5. genauere Alternative

Wichtig:
- Kurz und verständlich.
- Keine Person als Ganzes bewerten.
- Nur die Wirkung der Sprache analysieren.
```

---

## Prompt: Für 12- bis 15-Jährige erklären

```text 
Erkläre diese Druckwort-Analyse für 12- bis 15-Jährige.

Analyse:
[Analyse einfügen]

Bitte:
- kurze Sätze
- keine Fachsprache
- keine künstliche Jugendsprache
- ein einfaches Beispiel
- ein Merksatz
```

---

## Prompt: Gegenfragen zu Druckwörtern

```text 
Arbeite mit dem Denkzeug-Modell.

Formuliere fünf Gegenfragen zu diesem Druckwort im Satz.

Satz:
[Satz einfügen]

Druckwort:
[Wort einfügen]

Die Gegenfragen sollen:
- den Druck sichtbar machen,
- nicht beleidigend sein,
- keine Gegenmanipulation sein,
- den Raum öffnen,
- alltagstauglich für 12- bis 15-Jährige sein.
```

### Beispiel

```text 
Arbeite mit dem Denkzeug-Modell.

Formuliere fünf Gegenfragen zu diesem Druckwort im Satz.

Satz:
„Du willst doch kein Verräter sein.“

Druckwort:
„Verräter“

Die Gegenfragen sollen:
- den Druck sichtbar machen,
- nicht beleidigend sein,
- keine Gegenmanipulation sein,
- den Raum öffnen,
- alltagstauglich für 12- bis 15-Jährige sein.
```

### Mögliche gute Ausgabe

```text 
1. Warum wäre es Verrat, selbst nachzudenken?
2. Was genau soll daran Verrat sein?
3. Heißt Loyalität, dass ich alles mitmachen muss?
4. Kann ich zu euch halten und trotzdem anderer Meinung sein?
5. Wird hier wirklich Verrat beschrieben oder nur Druck gemacht?
```

---

## Kombinierter Masterprompt

```text 
Arbeite mit dem Denkzeug-Modell.

Analysiere diesen Satz oder Text auf Druckwörter:

[Satz oder Text einfügen]

Bitte beantworte:

1. Welche Wörter oder Formulierungen haben eine eingebaute Richtung?
2. Welche Bewertung steckt in diesen Wörtern?
3. Wer wird aufgewertet?
4. Wer wird abgewertet?
5. Welcher Hebel wird berührt?
6. Welcher Griff wird benutzt?
7. Welche Handlung wird wahrscheinlicher oder unwahrscheinlicher?
8. Wird Verhalten beschrieben oder eine Person markiert?
9. Welche konkrete Beobachtung könnte dahinterstehen?
10. Wie könnte man genauer und weniger markierend formulieren?
11. Welche Gegenfrage öffnet den Raum?

Regeln:
- Verbiete keine Wörter.
- Analysiere ihre Wirkung.
- Bewerte keine Person als Ganzes.
- Unterscheide Beschreibung, Deutung und Bewertung.
- Formuliere verständlich für 12- bis 15-Jährige.
- Ziel ist mehr Genauigkeit und Spielraum.
```

---

## Kurzprompt

```text 
Welche Wörter machen hier Druck?
Welche Bewertung steckt drin?
Wer wird auf- oder abgewertet?
Welche Handlung wird wahrscheinlicher?
Wie kann man es genauer sagen?

Satz:
[Satz einfügen]
```

---

## Qualitätsprüfung

Eine gute KI-Antwort in diesem Bereich:

```text 
erkennt konkrete Druckwörter
erklärt ihre Wirkung
unterscheidet Beschreibung und Markierung
nennt Hebel und Griff
zeigt mögliche Handlungswirkung
macht keine Person zum Etikett
formuliert genauer
liefert eine Gegenfrage
```

Eine schlechte KI-Antwort:

```text 
verbietet Wörter pauschal
moralisiert nur
bewertet Menschen als Ganzes
analysiert keine konkrete Wirkung
übersieht Aufwertung und Abwertung
macht aus Denkzeug Sprachpolizei
verengt den Raum
```

---

## Leitsatz

> Manche Wörter erklären nichts.
> Sie kleben nur ein Schild auf.
> KI soll helfen, das Schild zu erkennen — und genauer zu sprechen.

