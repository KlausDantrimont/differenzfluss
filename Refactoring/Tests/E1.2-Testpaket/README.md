# E1.2 – Testpaket: struktureller Transfer

## Zweck

Dieser Test prüft, ob ein explizites Refactoring-Verfahren gegenüber einer normalen Analyse einen Mehrwert liefert.

Wichtig: **Baseline und Refactoring müssen in getrennten, frischen Kontexten laufen.**
Ein Modell, das R1/R2 bereits kennt, ist keine faire Baseline.

## Ablauf

1. Öffne einen frischen Chat mit Modell X.
2. Gib `01-Szenen.md` + `02-Prompt-Baseline.md`.
3. Speichere die Antwort.
4. Öffne einen zweiten frischen Chat mit demselben Modell X.
5. Gib `01-Szenen.md` + `03-Prompt-Refactoring.md`.
6. Speichere die Antwort.
7. Erst danach `99-Loesungsschluessel.md` öffnen.
8. Beide Antworten mit `04-Auswertung.md` vergleichen.

Optional kann derselbe Test mit mehreren Modellen wiederholt werden.

## Methodischer Hinweis

Der Test ist ein Proof of Concept, kein statistisch belastbares Experiment.
Die Szenen wurden zufällig aus einer kleinen Familie verborgener Strukturmuster erzeugt.
