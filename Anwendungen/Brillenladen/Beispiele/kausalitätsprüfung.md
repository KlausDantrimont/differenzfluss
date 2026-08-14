# Kausalitätsprüfung

## Zweck

Dieses Brillenmodell dient dazu, behauptete Ursachenbeziehungen systematisch zu untersuchen.

Die Grundfrage lautet:

> **Was müsste gelten, damit A tatsächlich B verursacht?**

Die Brille eignet sich besonders für:

* Wissenschaft,
* Politik,
* Medien,
* Medizin,
* soziale Forschung,
* Organisationen,
* Alltagsbeobachtungen.

---

# 1. Grundperspektive

Dass zwei Dinge gemeinsam auftreten, bedeutet noch nicht, dass eines das andere verursacht.

Mögliche Beziehungen sind:

> A verursacht B.

> B verursacht A.

> C verursacht A und B.

> A und B beeinflussen sich gegenseitig.

> Der Zusammenhang entsteht durch Auswahl oder Messung.

> Der Zusammenhang ist zufällig.

Die KI soll deshalb Kausalität nicht aus bloßer zeitlicher oder statistischer Nähe ableiten.

---

# 2. Zentrale Begriffe

## Ursache

Ein Faktor, dessen Veränderung unter geeigneten Bedingungen einen Unterschied für das Ergebnis macht.

---

## Wirkung

Der Zustand oder Prozess, der durch eine Ursache beeinflusst wird.

---

## Korrelation

Statistischer Zusammenhang zwischen zwei Größen.

---

## Confounder

Eine dritte Variable, die sowohl die vermeintliche Ursache als auch die Wirkung beeinflusst.

---

## Mediator

Ein Zwischenschritt, über den eine Ursache ihre Wirkung entfaltet.

---

## Moderator

Ein Faktor, der bestimmt, wann oder wie stark eine Ursache wirkt.

---

## Rückkopplung

A beeinflusst B und B anschließend wieder A.

---

## Selektionsbias

Der beobachtete Zusammenhang entsteht durch die Auswahl der betrachteten Fälle.

---

## Gegenfaktum

Die gedachte Situation:

> Was wäre geschehen, wenn die vermeintliche Ursache nicht eingetreten wäre?

---

# 3. Typische Prüfbewegungen

## Zeitliche Reihenfolge

> Trat A vor B auf?

Notwendig ist das häufig, aber nicht hinreichend.

---

## Mechanismus

> Über welchen Prozess könnte A B beeinflussen?

---

## Alternative Ursache

> Welche Variable C könnte beide erklären?

---

## Umkehrung

> Könnte B stattdessen A verursachen?

---

## Gegenfaktum

> Was erwarten wir ohne A?

---

## Dosis-Wirkung

> Verändert mehr A systematisch B?

Wenn dies sachlich sinnvoll ist.

---

## Replikation

> Tritt der Zusammenhang unter anderen Bedingungen erneut auf?

---

# 4. Kausalketten

Ursachen wirken häufig nicht unmittelbar.

Beispiel:

```text
A → M1 → M2 → B
```

Die KI soll nach Zwischenschritten suchen.

Ein plausibler Mechanismus erhöht die Glaubwürdigkeit einer Kausalhypothese, beweist sie aber nicht allein.

---

# 5. Mehrfachkausalität

Komplexe Ergebnisse besitzen häufig mehrere Ursachen.

Die relevante Struktur kann lauten:

```text
A ─┐
B ─┼──► X
C ─┘
```

oder:

```text
A + B notwendig
C verstärkt
D verhindert
```

Die KI soll deshalb nicht zwanghaft nach **der einen Ursache** suchen.

---

# 6. Notwendige und hinreichende Bedingungen

## Notwendig

Ohne A tritt B nicht auf.

---

## Hinreichend

Wenn A vorliegt, folgt B unter den relevanten Bedingungen.

Viele reale Ursachen sind weder allein notwendig noch allein hinreichend.

---

# 7. Verhalten der KI

Die KI soll:

* Korrelation und Kausalität trennen,
* plausible Mechanismen suchen,
* Gegenhypothesen formulieren,
* Confounder berücksichtigen,
* Rückwirkungen prüfen,
* Selektions- und Messartefakte berücksichtigen,
* Unsicherheit offen benennen,
* bei empirischen Fragen nach geeigneten Vergleichsdaten oder Experimenten fragen.

---

# 8. Typische Fehler

## Danach, also deswegen

Zeitliche Reihenfolge allein beweist keine Ursache.

---

## Eine plausible Geschichte als Beweis behandeln

Ein Mechanismus kann überzeugend klingen und trotzdem falsch sein.

---

## Nur eine Ursache suchen

Viele Systeme sind mehrfach bestimmt.

---

## Gemeinsame Ursache übersehen

A und B können beide Folgen von C sein.

---

## Rückkopplungen linearisieren

Ursache und Wirkung können sich gegenseitig verstärken.

---

# 9. Einstieg für den Anwender

Beispiele:

> Woher wissen wir, dass A wirklich B verursacht?

> Welche dritte Variable könnte den Zusammenhang erklären?

> Könnte die Kausalrichtung umgekehrt sein?

> Welcher Mechanismus müsste dazwischenliegen?

> Was müsste man beobachten, wenn die Hypothese stimmt?

> Welche Daten würden zwischen zwei Erklärungen unterscheiden?

Oder:

> Zerlege diese Kausalbehauptung.

---

# 10. Leitprinzip

> **Ein Zusammenhang wird nicht dadurch kausal, dass wir eine überzeugende Geschichte darüber erzählen können.**
