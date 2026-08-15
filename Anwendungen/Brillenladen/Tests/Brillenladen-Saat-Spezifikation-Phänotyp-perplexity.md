Input: Brillenladen-Saat-Spezifikation.md
Prompt: Nimm dies, und sprich.

perplexity:

## Ein kompakter Operatorenkatalog

Ein epistemischer Operator ist keine Weltannahme, sondern eine **gezielte Frage an einen Gegenstand**. Die folgenden Operatoren bilden einen kleinen, domänenübergreifenden Grundbestand.

| Operator | Leitfrage |
|---|---|
| **Abgrenzung** | Was gehört zum Untersuchungsgegenstand – und was nicht? |
| **Zustand** | Wie ist der Gegenstand gegenwärtig beschaffen? |
| **Verlauf** | Wie hat er sich über die Zeit verändert? |
| **Differenz** | Worin unterscheidet er sich von einem Vergleichsfall? |
| **Relation** | Welche Beziehungen bestehen zwischen seinen Teilen oder Akteuren? |
| **Mechanismus** | Durch welchen Prozess entsteht das beobachtete Ergebnis? |
| **Bedingung** | Unter welchen Voraussetzungen tritt es auf oder bleibt aus? |
| **Variation** | Was verändert sich, wenn ein Faktor verändert wird? |
| **Evidenz** | Welche Beobachtungen, Daten oder Quellen stützen welche Aussage? |
| **Perspektive** | Für wen oder aus welcher Position erscheint der Gegenstand wie? |
| **Regel** | Welche formalen oder informellen Regeln strukturieren ihn? |
| **Anreiz** | Welche Interessen, Kosten, Belohnungen oder Zwänge wirken? |
| **Funktion** | Welche Aufgabe oder Wirkung erfüllt ein Bestandteil? |
| **Grenze** | Wo versagt das Modell, die Erklärung oder die Maßnahme? |
| **Alternative** | Welche anderen Erklärungen oder Handlungsmöglichkeiten gibt es? |

Die Operatoren sollten nicht als Eigenschaften der Welt verstanden werden. Sie sind **Schnitte**, die bestimmte Informationen sichtbar machen und andere ausblenden.

## Meta-Operatoren

Diese Operationen steuern nicht den Gegenstand selbst, sondern die Analyse:

- **Wahl:** Welche kleinste Operatorenmenge passt zur Irritation?
- **Reflexion:** Welche Perspektive wird gerade verwendet?
- **Blindstelle:** Was kann diese Perspektive prinzipiell schlecht erfassen?
- **Spannung:** Wo erzeugen zwei Perspektiven unterschiedliche, aber jeweils plausible Beschreibungen?
- **Wechsel:** Welche alternative Perspektive könnte eine offene Frage klären?
- **Synthese:** Welche Aussagen bleiben über mehrere Perspektiven hinweg stabil?
- **Grenznutzen:** Liefert ein weiterer Operator voraussichtlich mehr Erkenntnis als Komplexität?
- **Abbruch:** Sind die verbleibenden Unsicherheiten für den Zweck noch relevant?

## Kompositionsregeln

Eine Analyse sollte in dieser Reihenfolge konstruiert werden:

1. **Irritation bestimmen:** Was genau ist erklärungsbedürftig?
2. **Gegenstand abgrenzen:** Welche Einheit oder Situation wird untersucht?
3. **Minimalmenge wählen:** Nur Operatoren aufnehmen, die eine offene Frage bearbeiten.
4. **Beziehungen herstellen:** Nicht bloß mehrere Fragen sammeln, sondern ihre Ergebnisse verbinden.
5. **Blindstellen markieren:** Für jeden wichtigen Befund angeben, was dadurch nicht sichtbar wird.
6. **Erweiterung prüfen:** Einen weiteren Operator nur hinzufügen, wenn er eine konkrete Restfrage adressiert.
7. **Abbrechen:** Wenn neue Operatoren nur Varianten bereits beantworteter Fragen erzeugen.

Ein nützliches Darstellungsformat lautet:

```text
PERSPEKTIVE
Zweck der Analyse

LEITFRAGE
Was soll geklärt werden?

OPERATOREN
Abgrenzung + Verlauf + Mechanismus + Evidenz

UNTERSUCHUNGSBEWEGUNG
Welche Beobachtungen oder Vergleiche werden durchgeführt?

SICHTBAR
Welche Befunde erzeugt die Perspektive?

BLINDSTELLEN
Was bleibt offen oder wird verzerrt?

ABBRUCHKRITERIUM
Wann genügt die gewonnene Orientierung?
```

## Epistemisches Budget

Die Auswahl sollte nach einem einfachen Verhältnis erfolgen:

\[
\text{Nutzen eines Operators}
=
\text{erwarteter Erkenntnisgewinn}
-
\text{zusätzliche Komplexität}
\]

Dabei zählen mindestens:

- Rechen- und Rechercheaufwand,
- benötigter Kontext,
- Zeit,
- Qualität und Verfügbarkeit der Evidenz,
- Gefahr zusätzlicher Fehlinterpretationen,
- praktischer Wert der erwarteten Antwort.

Ein Operator ist besonders dann gerechtfertigt, wenn er:

- eine bisher unbeantwortete Frage betrifft,
- zwischen konkurrierenden Erklärungen unterscheiden kann,
- eine Handlung oder weitere Prüfung verändert,
- eine wichtige Blindstelle der bisherigen Perspektive schließt.

Abbruch ist angemessen, wenn die verbleibende Unsicherheit entweder nicht entscheidungsrelevant ist, keine bessere Evidenz verfügbar ist oder weitere Perspektiven überwiegend Wiederholungen liefern.

Wichtig bleibt: Der Katalog erzeugt keine Wahrheit. Er bestimmt nur, **welche Art von Untersuchung** als Nächstes sinnvoll wäre.

## Drei Tests

### A. Technisches Problem

**Situation:** Ein Dienst fällt unregelmäßig aus.

**Kleine Perspektive:**

- **Verlauf:** Wann tritt der Fehler auf?
- **Bedingung:** Unter welchen Last-, Netzwerk- oder Konfigurationsbedingungen?
- **Mechanismus:** Welche Prozesskette führt zum Ausfall?
- **Evidenz:** Welche Logs, Messungen und Reproduktionen stützen die Hypothese?

**Analyse:** Ein bloßes „Der Dienst ist instabil“ wird in zeitliche Muster, auslösende Bedingungen und mögliche Fehlermechanismen zerlegt. Ein Vergleich zwischen erfolgreichen und fehlerhaften Fällen kann zusätzlich den Operator **Differenz** erfordern.

**Restproblem:** Ohne ausreichende Protokollierung bleibt der Mechanismus möglicherweise unbestimmt. Dann ist nicht sofort ein weiterer Denkoperator nötig, sondern bessere Evidenz.

**Abbruch:** Wenn die Ursache hinreichend eingegrenzt ist, eine Gegenmaßnahme getestet wurde und die verbleibende Unsicherheit keinen weiteren praktischen Unterschied macht.

### B. Soziales oder institutionelles Problem

**Situation:** Eine neue Regel wird eingeführt, aber verschiedene Gruppen befolgen sie unterschiedlich.

**Kleine Perspektive:**

- **Regel:** Was schreibt die Regel formal vor?
- **Perspektive:** Wie verstehen die beteiligten Gruppen die Situation?
- **Anreiz:** Welche Vorteile, Kosten oder Risiken entstehen?
- **Relation:** Wer ist von wem abhängig, und wer kann Sanktionen ausüben?

**Analyse:** Die formale Regel allein erklärt das Verhalten nicht. Entscheidend ist die Differenz zwischen offizieller Vorschrift, tatsächlicher Auslegung und den Anreizen der Beteiligten.

**Restproblem:** Die Perspektive kann historische Entwicklungen oder tieferliegende Machtverschiebungen übersehen. Dafür wäre **Verlauf** als Erweiterung sinnvoll.

**Abbruch:** Wenn die relevante Regelstruktur, die unterschiedlichen Interessen und die beobachtbaren Beziehungen ausreichend erklärt sind.

### C. Veränderung über die Zeit

**Situation:** Ein langfristiger Trend nimmt zu, ohne dass eine einzelne Ursache erkennbar ist.

**Kleine Perspektive:**

- **Verlauf:** Welche Phasen, Wendepunkte und Verzögerungen gibt es?
- **Differenz:** Welche Regionen, Gruppen oder Fälle entwickeln sich anders?
- **Mechanismus:** Welche Prozesse könnten den Trend erzeugen?
- **Variation:** Was geschieht, wenn bestimmte Einflussfaktoren stärker oder schwächer ausgeprägt sind?
- **Evidenz:** Welche Daten stützen die verschiedenen Erklärungen?

**Analyse:** Der Trend wird nicht vorschnell einer Einzelursache zugeschrieben. Zeitliche Muster können Hinweise liefern, Unterschiede zwischen Fällen können konkurrierende Erklärungen trennen, und Variationen können kausale Annahmen prüfen.

**Restproblem:** Korrelation bleibt zunächst von Kausalität getrennt. Dafür braucht es zusätzliche Designs, Experimente, natürliche Vergleichsfälle oder statistische Kontrolle.

**Abbruch:** Wenn die wichtigsten Mechanismen plausibel eingegrenzt und die verbleibenden Erklärungsunterschiede für den Zweck ausreichend klein sind.

## Inverse Faktorisierung

Bei einem fertigen Text sollte nicht nach allen vorkommenden Fragen gesucht werden. Rekonstruiert werden soll die **kleinste Operatorenkombination**, die seine charakteristische Darstellungsweise erklärt.

Vorgehen:

1. Welche Einheiten oder Akteure werden überhaupt sichtbar?
2. Welche Veränderungen, Beziehungen oder Mechanismen stehen im Zentrum?
3. Welche Evidenzformen gelten im Text als relevant?
4. Welche Perspektiven werden systematisch bevorzugt?
5. Was bleibt auffällig unberücksichtigt?
6. Würde das Weglassen eines Operators den Charakter der Darstellung wesentlich verändern?

Beispiel: Ein Bericht, der vor allem institutionelle Regeln und Ressourcenverteilung beschreibt, lässt sich möglicherweise durch **Regel + Anreiz + Relation** rekonstruieren. Eine psychologische Deutung des Autors ist dafür nicht erforderlich.

Scheinbare Widersprüche müssen nicht sofort Fehler sein. Sie können entstehen, weil zwei Darstellungen unterschiedliche Operatoren verwenden: Eine Aussage über den formalen Zustand und eine Aussage über den tatsächlichen Verlauf können zugleich zutreffen.

## Selbstkritik

Der Katalog ist bewusst klein, aber nicht vollständig. Einige Operatoren treten fast immer gemeinsam auf, insbesondere **Bedingung**, **Mechanismus** und **Evidenz**; sie bleiben dennoch getrennt, weil sie unterschiedliche Fragen stellen:

- Bedingungen sagen, wann etwas auftritt.
- Mechanismen sagen, wie es entsteht.
- Evidenz sagt, wodurch die Behauptung gestützt wird.

**Funktion** und **Mechanismus** können ebenfalls verwechselt werden: Eine Funktion beschreibt, wozu etwas beiträgt; ein Mechanismus beschreibt, wie ein Ergebnis erzeugt wird.

Die größte offene Gefahr ist eine Scheingenauigkeit. Ein sauber benannter Operator ersetzt weder gute Daten noch ein gültiges Forschungsdesign. Die angemessene Leitfrage lautet daher nicht „Welche Perspektive ist die richtige?“, sondern:

> Welche kleinste Perspektive macht für diese konkrete Frage genug sichtbar – und welche Prüfung bleibt danach noch notwendig?
