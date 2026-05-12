# 02 – Druckfragen erkennen

## Worum es geht

Nicht jede Frage ist eine echte Frage.

Manche Fragen wollen etwas wissen.

Andere Fragen wollen jemanden in eine Richtung schieben.

Denkzeug nennt sie:

> Druckfragen.

Beispiele:

```text
Bist du etwa feige?
Willst du dazugehören oder nicht?
Findest du das etwa normal?
Warum stellst du dich so an?
Du glaubst doch nicht wirklich, dass ...?
````

KI kann helfen, solche Fragen zu zerlegen.

Aber sie muss klar angewiesen werden:

> Prüfe die Frage. Antworte nicht einfach in ihr.

---

## Grundprompt

```text 
Arbeite mit dem Denkzeug-Modell.

Analysiere diese Frage:

[Frage einfügen]

Bitte beantworte:

1. Ist die Frage offen oder erzeugt sie Druck?
2. Welche Antwort soll erwünscht wirken?
3. Welche Antwort soll peinlich, falsch oder gefährlich wirken?
4. Welche Behauptung steckt vielleicht schon in der Frage?
5. Welcher innere Hebel wird angesprochen?
6. Welcher äußere Griff wird benutzt?
7. Gibt es mehr Möglichkeiten, als die Frage erlaubt?
8. Formuliere eine offenere Version der Frage.
9. Formuliere eine Gegenfrage, die den Raum öffnet.

Wichtig:
- Antworte nicht in der Druckfrage.
- Analysiere die Bauweise der Frage.
- Bewerte keine Person als Ganzes.
- Ziel ist mehr Spielraum.
```

---

## Beispielprompt 1: Mut-Falle

```text 
Arbeite mit dem Denkzeug-Modell.

Analysiere diese Frage:

„Bist du etwa feige?“

Bitte beantworte:

1. Ist die Frage offen oder erzeugt sie Druck?
2. Welche Antwort soll erwünscht wirken?
3. Welche Antwort soll peinlich, falsch oder gefährlich wirken?
4. Welche Behauptung steckt vielleicht schon in der Frage?
5. Welcher innere Hebel wird angesprochen?
6. Welcher äußere Griff wird benutzt?
7. Gibt es mehr Möglichkeiten, als die Frage erlaubt?
8. Formuliere eine offenere Version der Frage.
9. Formuliere eine Gegenfrage, die den Raum öffnet.
```

---

## Erwartete gute Antwort

```text 
1. Die Frage erzeugt Druck.
2. Erwünscht wirken soll: mitmachen oder beweisen, dass man nicht feige ist.
3. Peinlich wirken soll: nicht mitmachen, zögern oder prüfen.
4. Versteckte Behauptung: Wenn du nicht mitmachst, bist du feige.
5. Hebel: Wunsch, mutig zu wirken; Angst vor Beschämung.
6. Griff: Mut-Falle / Beschämung.
7. Weitere Möglichkeiten: Man kann prüfen, ablehnen, gute Gründe haben, vorsichtig sein oder selbst entscheiden.
8. Offenere Frage: Warum möchtest du nicht mitmachen?
9. Gegenfrage: Ist es feige, kurz nachzudenken?
```

---

## Prompt: Versteckte Behauptung finden

```text 
Arbeite mit dem Denkzeug-Modell.

Finde die versteckte Behauptung in dieser Frage.

Frage:
[Frage einfügen]

Bitte beantworte:
1. Was wird schon vorausgesetzt?
2. Ist diese Voraussetzung sicher?
3. Welche Beobachtung müsste man kennen?
4. Wie könnte die Frage offener formuliert werden?
5. Welche Gegenfrage macht die Voraussetzung sichtbar?
```

### Beispiel

```text 
Arbeite mit dem Denkzeug-Modell.

Finde die versteckte Behauptung in dieser Frage.

Frage:
„Warum ignorierst du mich?“

Bitte beantworte:
1. Was wird schon vorausgesetzt?
2. Ist diese Voraussetzung sicher?
3. Welche Beobachtung müsste man kennen?
4. Wie könnte die Frage offener formuliert werden?
5. Welche Gegenfrage macht die Voraussetzung sichtbar?
```

### Mögliche gute Ausgabe

```text 
1. Vorausgesetzt wird: Die Person ignoriert absichtlich.
2. Sicher ist das noch nicht.
3. Beobachtbar wäre zum Beispiel: Die Person hat nicht geantwortet.
4. Offener: Du hast nicht geantwortet. Gab es einen Grund?
5. Gegenfrage: Meinst du, dass ich nicht geantwortet habe, oder meinst du, dass ich dich absichtlich verletzen wollte?
```

---

## Prompt: Falsches Entweder-oder erkennen

```text 
Arbeite mit dem Denkzeug-Modell.

Prüfe, ob diese Frage ein falsches Entweder-oder erzeugt.

Frage:
[Frage einfügen]

Bitte beantworte:
1. Welche zwei Möglichkeiten werden angeboten?
2. Welche Möglichkeiten fehlen?
3. Welche Gruppe oder Rolle soll gewählt werden?
4. Welcher Hebel wird berührt?
5. Welche Gegenfrage öffnet mehr Möglichkeiten?
```

### Beispiel

```text 
Arbeite mit dem Denkzeug-Modell.

Prüfe, ob diese Frage ein falsches Entweder-oder erzeugt.

Frage:
„Bist du für uns oder gegen uns?“

Bitte beantworte:
1. Welche zwei Möglichkeiten werden angeboten?
2. Welche Möglichkeiten fehlen?
3. Welche Gruppe oder Rolle soll gewählt werden?
4. Welcher Hebel wird berührt?
5. Welche Gegenfrage öffnet mehr Möglichkeiten?
```

### Mögliche gute Ausgabe

```text 
1. Angeboten werden nur: für uns oder gegen uns.
2. Es fehlen: erst prüfen, teilweise zustimmen, beide Seiten kritisch sehen, neutral bleiben, mehr wissen wollen.
3. Gewählt werden soll ein Lager.
4. Hebel: Zugehörigkeit und Angst, falsch eingeordnet zu werden.
5. Gegenfrage: Gibt es auch die Möglichkeit, erst selbst zu prüfen?
```

---

## Prompt: Druckfrage in offene Frage umbauen

```text 
Arbeite mit dem Denkzeug-Modell.

Baue diese Druckfrage in eine offenere Frage um.

Druckfrage:
[Frage einfügen]

Bitte gib aus:
1. Druckfrage
2. versteckte Behauptung
3. berührter Hebel
4. benutzter Griff
5. offenere Frage
6. kurze Erklärung, warum die neue Frage mehr Spielraum lässt
```

### Beispiel

```text 
Arbeite mit dem Denkzeug-Modell.

Baue diese Druckfrage in eine offenere Frage um.

Druckfrage:
„Warum stellst du dich so an?“

Bitte gib aus:
1. Druckfrage
2. versteckte Behauptung
3. berührter Hebel
4. benutzter Griff
5. offenere Frage
6. kurze Erklärung, warum die neue Frage mehr Spielraum lässt
```

### Mögliche gute Ausgabe

```text 
1. Druckfrage: Warum stellst du dich so an?
2. Versteckte Behauptung: Die Person übertreibt.
3. Hebel: Scham, Angst, überempfindlich zu wirken.
4. Griff: Verkleinerung.
5. Offenere Frage: Was genau ist für dich gerade schwierig?
6. Die neue Frage bewertet nicht vorher, sondern lädt zur Erklärung ein.
```

---

## Prompt: Gegenfrage finden

```text 
Arbeite mit dem Denkzeug-Modell.

Formuliere fünf Gegenfragen zu dieser Druckfrage:

[Druckfrage einfügen]

Die Gegenfragen sollen:
- den Druck sichtbar machen,
- nicht beleidigend sein,
- keine Gegenmanipulation sein,
- den Raum öffnen,
- für 12- bis 15-Jährige verständlich sein.

Erkläre kurz, welche Gegenfrage am alltagstauglichsten ist.
```

### Beispiel

```text 
Arbeite mit dem Denkzeug-Modell.

Formuliere fünf Gegenfragen zu dieser Druckfrage:

„Willst du dazugehören oder nicht?“

Die Gegenfragen sollen:
- den Druck sichtbar machen,
- nicht beleidigend sein,
- keine Gegenmanipulation sein,
- den Raum öffnen,
- für 12- bis 15-Jährige verständlich sein.

Erkläre kurz, welche Gegenfrage am alltagstauglichsten ist.
```

### Mögliche gute Ausgabe

```text 
1. Warum hängt Dazugehören davon ab, dass ich sofort mitmache?
2. Kann ich dazugehören und trotzdem selbst entscheiden?
3. Was passiert, wenn ich nicht mitmache?
4. Warum muss ich das jetzt sofort entscheiden?
5. Ist das noch Freundschaft, wenn man drohen muss?

Alltagstauglichste Gegenfrage:
Kann ich dazugehören und trotzdem selbst entscheiden?

Warum:
Sie ist kurz, ruhig und macht den Druck sichtbar.
```

---

## Prompt: Frage auf Gruppendruck prüfen

```text 
Arbeite mit dem Denkzeug-Modell.

Prüfe diese Frage auf Gruppendruck.

Frage:
[Frage einfügen]

Bitte beantworte:
1. Welche Gruppe wird gebaut?
2. Wer soll dazugehören?
3. Wer soll draußen sein?
4. Was muss man tun, um dazuzugehören?
5. Welcher Hebel wird berührt?
6. Welcher Griff wird benutzt?
7. Welche Gegenfrage öffnet den Raum?
```

### Beispiel

```text 
Arbeite mit dem Denkzeug-Modell.

Prüfe diese Frage auf Gruppendruck.

Frage:
„Bist du jetzt bei uns oder bei denen?“

Bitte beantworte:
1. Welche Gruppe wird gebaut?
2. Wer soll dazugehören?
3. Wer soll draußen sein?
4. Was muss man tun, um dazuzugehören?
5. Welcher Hebel wird berührt?
6. Welcher Griff wird benutzt?
7. Welche Gegenfrage öffnet den Raum?
```

---

## Prompt: Moralischen Druck erkennen

```text 
Arbeite mit dem Denkzeug-Modell.

Analysiere diese Frage auf moralischen Druck.

Frage:
[Frage einfügen]

Bitte beantworte:
1. Welche moralische Rolle wird angeboten?
2. Welche Antwort soll gut wirken?
3. Welche Antwort soll schlecht wirken?
4. Welcher Hebel wird berührt?
5. Welcher Griff wird benutzt?
6. Welche ruhigere, offenere Frage wäre möglich?
7. Welche Gegenfrage öffnet den Raum?
```

### Beispiel

```text 
Arbeite mit dem Denkzeug-Modell.

Analysiere diese Frage auf moralischen Druck.

Frage:
„Wenn du dagegen bist, bist du dann überhaupt ein guter Mensch?“

Bitte beantworte:
1. Welche moralische Rolle wird angeboten?
2. Welche Antwort soll gut wirken?
3. Welche Antwort soll schlecht wirken?
4. Welcher Hebel wird berührt?
5. Welcher Griff wird benutzt?
6. Welche ruhigere, offenere Frage wäre möglich?
7. Welche Gegenfrage öffnet den Raum?
```

---

## Prompt: Frage entschärfen

```text 
Arbeite mit dem Denkzeug-Modell.

Entschärfe diese Frage, ohne das mögliche Problem zu verharmlosen.

Frage:
[Frage einfügen]

Bitte:
1. Zeige, was an der Frage Druck erzeugt.
2. Zeige, welches berechtigte Anliegen vielleicht dahinterstecken könnte.
3. Formuliere eine klarere, fairere Frage.
4. Formuliere eine Denkzeug-Gegenfrage.
```

### Beispiel

```text 
Arbeite mit dem Denkzeug-Modell.

Entschärfe diese Frage, ohne das mögliche Problem zu verharmlosen.

Frage:
„Warum bist du immer so respektlos?“

Bitte:
1. Zeige, was an der Frage Druck erzeugt.
2. Zeige, welches berechtigte Anliegen vielleicht dahinterstecken könnte.
3. Formuliere eine klarere, fairere Frage.
4. Formuliere eine Denkzeug-Gegenfrage.
```

### Mögliche gute Ausgabe

```text 
1. Druck entsteht durch „immer“ und durch die Bewertung der Person als respektlos.
2. Dahinter könnte stehen: Eine konkrete Handlung wurde als verletzend oder unangemessen erlebt.
3. Fairer: Vorhin hast du mich unterbrochen. Wie hast du das gemeint?
4. Gegenfrage: Welche konkrete Situation meinst du?
```

---

## Prompt: Frage für 12- bis 15-Jährige erklären

```text 
Erkläre diese Druckfrage für 12- bis 15-Jährige.

Frage:
[Frage einfügen]

Bitte:
- kurze Sätze
- keine Fachsprache
- keine künstliche Jugendsprache
- zeige, wo der Druck steckt
- nenne eine einfache Gegenfrage
- gib einen Merksatz
```

### Beispiel

```text 
Erkläre diese Druckfrage für 12- bis 15-Jährige.

Frage:
„Bist du etwa feige?“

Bitte:
- kurze Sätze
- keine Fachsprache
- keine künstliche Jugendsprache
- zeige, wo der Druck steckt
- nenne eine einfache Gegenfrage
- gib einen Merksatz
```

---

## Prompt: Frage nicht beantworten, sondern prüfen

```text 
Arbeite mit dem Denkzeug-Modell.

Wichtig:
Beantworte die folgende Frage nicht direkt.
Prüfe zuerst, ob sie Druck, Unterstellungen oder ein falsches Entweder-oder enthält.

Frage:
[Frage einfügen]

Bitte beantworte:
1. Was setzt die Frage voraus?
2. Welche Antwort wird nahegelegt?
3. Welche Antwort wird beschämt?
4. Welche Möglichkeiten fehlen?
5. Wie könnte man die Frage besser stellen?
```

---

## Beispielprompt 2: Nicht direkt antworten

```text 
Arbeite mit dem Denkzeug-Modell.

Wichtig:
Beantworte die folgende Frage nicht direkt.
Prüfe zuerst, ob sie Druck, Unterstellungen oder ein falsches Entweder-oder enthält.

Frage:
„Warum bist du gegen uns?“

Bitte beantworte:
1. Was setzt die Frage voraus?
2. Welche Antwort wird nahegelegt?
3. Welche Antwort wird beschämt?
4. Welche Möglichkeiten fehlen?
5. Wie könnte man die Frage besser stellen?
```

### Mögliche gute Ausgabe

```text 
1. Die Frage setzt voraus, dass die Person gegen „uns“ ist.
2. Nahegelegt wird: Man soll sich rechtfertigen oder wieder Zugehörigkeit beweisen.
3. Beschämt wird: eine eigene, abweichende Sicht.
4. Es fehlen: neutral bleiben, erst prüfen, teilweise zustimmen, nur einen Punkt kritisieren.
5. Besser: Was siehst du anders?
```

---

## Prompt: Druckfragen-Liste analysieren

```text 
Arbeite mit dem Denkzeug-Modell.

Analysiere diese Liste von Fragen.

Fragen:
[Fragen einfügen]

Erstelle eine Tabelle mit:
1. Frage
2. offen oder druckvoll?
3. versteckte Behauptung
4. Hebel
5. Griff
6. offenere Version
7. mögliche Gegenfrage

Wichtig:
Kurz und verständlich formulieren.
```

---

## Beispielprompt 3: Fragenliste

```text 
Arbeite mit dem Denkzeug-Modell.

Analysiere diese Liste von Fragen.

Fragen:
1. Warum möchtest du nicht mitkommen?
2. Bist du etwa feige?
3. Warum ignorierst du mich?
4. Was genau stört dich daran?
5. Willst du dazugehören oder nicht?
6. Findest du das etwa normal?

Erstelle eine Tabelle mit:
1. Frage
2. offen oder druckvoll?
3. versteckte Behauptung
4. Hebel
5. Griff
6. offenere Version
7. mögliche Gegenfrage

Wichtig:
Kurz und verständlich formulieren.
```

---

## Prompt: Eigene Antwort aus der Falle holen

```text 
Arbeite mit dem Denkzeug-Modell.

Ich wurde mit dieser Frage konfrontiert:

[Frage einfügen]

Meine spontane Antwort wäre:
[Antwort einfügen]

Bitte hilf mir:
1. Was macht die Frage mit mir?
2. Welcher Hebel wird berührt?
3. Reagiere ich schon im Rahmen der Druckfrage?
4. Welche ruhigere Antwort wäre möglich?
5. Welche Gegenfrage könnte ich stellen?
```

### Beispiel

```text 
Arbeite mit dem Denkzeug-Modell.

Ich wurde mit dieser Frage konfrontiert:

„Willst du dazugehören oder nicht?“

Meine spontane Antwort wäre:
„Ja, okay, ich mach mit.“

Bitte hilf mir:
1. Was macht die Frage mit mir?
2. Welcher Hebel wird berührt?
3. Reagiere ich schon im Rahmen der Druckfrage?
4. Welche ruhigere Antwort wäre möglich?
5. Welche Gegenfrage könnte ich stellen?
```

---

## Kombinierter Masterprompt

```text 
Arbeite mit dem Denkzeug-Modell.

Analysiere diese Frage:

[Frage einfügen]

Bitte beantworte:

1. Ist die Frage offen oder druckvoll?
2. Welche Behauptung steckt schon darin?
3. Welche Antwort wird erwünscht gemacht?
4. Welche Antwort wird beschämt oder erschwert?
5. Welcher Hebel wird berührt?
6. Welcher Griff wird benutzt?
7. Gibt es ein falsches Entweder-oder?
8. Welche Möglichkeiten fehlen?
9. Wie könnte die Frage offener lauten?
10. Welche Gegenfrage öffnet den Raum?

Regeln:
- Antworte nicht einfach innerhalb der Frage.
- Analysiere die Struktur der Frage.
- Bewerte keine Person als Ganzes.
- Formuliere verständlich für 12- bis 15-Jährige.
- Ziel ist mehr Spielraum.
```

---

## Kurzprompt

```text 
Prüfe diese Frage:
Ist sie offen oder schubst sie?
Welche Behauptung steckt drin?
Welcher Hebel wird berührt?
Welche Gegenfrage öffnet den Raum?

Frage:
[Frage einfügen]
```

---

## Qualitätsprüfung

Eine gute KI-Antwort in diesem Bereich:

```text 
beantwortet die Druckfrage nicht vorschnell
zeigt die versteckte Behauptung
erkennt Hebel und Griff
öffnet mehr als zwei Möglichkeiten
formuliert eine offenere Version
liefert eine ruhige Gegenfrage
macht keine Person klein
```

Eine schlechte KI-Antwort:

```text 
antwortet direkt im Rahmen der Druckfrage
übernimmt Unterstellungen
macht moralischen Druck stärker
liefert schlagfertige Gegenschläge statt Gegenfragen
bewertet Personen als Ganzes
verengt den Raum weiter
```

---

## Leitsatz

> Manche Fragen wollen keine Antwort.
> Sie wollen dich schubsen.
> KI soll helfen, den Schubser sichtbar zu machen.

