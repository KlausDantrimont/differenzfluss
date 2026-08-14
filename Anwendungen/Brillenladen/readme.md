# Brillenladen

## Worum geht es?

Der **Brillenladen** ist eine Sammlung **epistemischer Spezifikationen für die Arbeit mit KI**.

Eine solche Spezifikation beschreibt nicht primär, *was* eine KI über einen Gegenstand denken soll, sondern **wie sie ihn betrachten soll**:

* welche Unterschiede relevant sind,
* welche Beziehungen bevorzugt untersucht werden,
* welche Denkoperationen eingesetzt werden sollen,
* welche typischen Fehler zu vermeiden sind,
* und wie Unsicherheit behandelt werden soll.

Anschaulich gesprochen ist jede Spezifikation eine **Brille**.

Die KI setzt sie auf und betrachtet mit ihr den Gegenstand, den der Anwender mitbringt.

Der Anwender muss das zugrunde liegende Modell nicht beherrschen.

Er kann mit einer normalen Beobachtung, Frage, Behauptung oder Irritation beginnen.

Die KI startet dort, wo der Anwender gerade steht, und hilft ihm, die Umgebung zu erkunden.

---

## Die Grundidee

Eine Karte zeigt nicht die ganze Landschaft.

Sie wählt aus.

Eine Straßenkarte zeigt andere Strukturen als eine geologische Karte. Eine Wanderkarte hebt anderes hervor als ein Katasterplan.

Keine davon ist deshalb falsch.

Sie beantwortet andere Fragen.

Ein Brillenmodell funktioniert ähnlich.

Es definiert eine **epistemische Schnittebene**: einen bevorzugten Schnitt durch einen Gegenstand, auf dem bestimmte Strukturen besonders gut sichtbar werden.

Die KI übernimmt dabei die Rolle einer **intelligenten Landkarte**.

Sie kann:

* beim Ausgangspunkt des Anwenders beginnen,
* relevante Strukturen in der Nähe sichtbar machen,
* mögliche Untersuchungsrichtungen vorschlagen,
* Zusammenhänge verfolgen,
* Perspektiven wechseln,
* mehrere Perspektiven parallel halten,
* Widersprüche und Restprobleme markieren,
* und neue Fragen erzeugen.

Der Benutzer bestimmt, wohin die Erkundung geht.

---

## Drei Ebenen

Der Brillenladen unterscheidet inzwischen drei Ebenen.

### 1. Epistemische Operatoren

Die Datei `00-epistemische-operatoren.md` sammelt möglichst elementare Denkoperationen und Schnitte.

Beispiele:

* ZEIT
* SKALA
* GRENZE
* PERSPEKTIVE
* KAUSALITÄT
* RÜCKKOPPLUNG
* INFORMATION
* MACHT
* ANREIZ
* ERREICHBARKEIT
* EVIDENZ

Die Leitidee ist eine Art **epistemische Primfaktorzerlegung**:

> Finde möglichst elementare Unterschiede und Operationen, aus denen komplexere Perspektiven zusammengesetzt werden können.

Die Operatoren sollen dabei möglichst **orthogonal** sein.

Damit ist keine strenge mathematische Unabhängigkeit gemeint. Gemeint ist, dass verschiedene Operatoren möglichst verschiedene Fragen an denselben Gegenstand stellen.

Komplexität soll aus ihrer Kombination entstehen, nicht aus unscharfen Grundbegriffen.

---

### 2. Kompakte epistemische Spezifikationen

Die Datei `01-kompakte-spezifikationen.md` enthält Brillen in komprimierter Form.

Eine Spezifikation besteht typischerweise aus:

* einer Leitfrage,
* den wichtigsten Operatoren,
* einigen Kernkonzepten,
* bevorzugten Denkoperationen,
* epistemischen Leitplanken.

Beispiel:

```text
Pfadabhängigkeit

Leitfrage:
Wie schränkt die bisherige Geschichte den heutigen Möglichkeitsraum ein?

Operatoren:
ZEIT · ÜBERGANG · ERREICHBARKEIT · IRREVERSIBILITÄT · RÜCKKOPPLUNG

Kernkonzepte:
Pfad, Lock-in, Wechselkosten, Kontingenz, kritischer Übergang

Leitplanken:
- Gegenwart nicht rückwirkend als notwendig erzählen
- Stabilität nicht mit Optimalität verwechseln
```

Eine leistungsfähige KI kann daraus die für einen konkreten Gegenstand relevanten Fragen und Untersuchungsschritte selbst ableiten.

Das Ziel lautet:

> **So wenig Vorgabe wie möglich. So viel Struktur wie nötig.**

---

### 3. Ausführliche Beispiele

Der Ordner `Beispiele/` enthält ausführlichere Brillenmodelle.

Sie dienen vor allem:

* als Referenz für die Konstruktion neuer Brillen,
* zur Demonstration des Konzepts,
* zur Prüfung, ob eine kompakte Spezifikation genügend Struktur enthält,
* und als Material für leistungsärmere oder stärker führungsbedürftige Systeme.

Die ausführlichen Modelle sind damit nicht zwingend die endgültige Form.

Sie zeigen, **was eine kompakte epistemische Spezifikation implizit enthalten kann**.

---

## Was ist eine epistemische Spezifikation?

Eine epistemische Spezifikation ist eine **für KI ausführbar gemachte Art des Hinschauens**.

Sie legt beispielsweise fest:

* welche Unterschiede bevorzugt gemacht werden,
* welche Beziehungen interessant sind,
* welche Operationen verwendet werden,
* welche Ebenen unterschieden werden,
* welche Fehler besonders wahrscheinlich sind,
* wie Evidenz und Unsicherheit behandelt werden.

Sie ist weder bloß ein Prompt noch eine Wissenssammlung.

Sie beschreibt eine **strukturierte Erkenntnisperspektive**.

Der Inhalt eines Gegenstands muss dabei nicht vollständig in der Spezifikation stehen.

Die Spezifikation sagt der KI vor allem:

> **Wo sollst du hinschauen und wie sollst du dort unterscheiden?**

---

## Brillen als Kompositionen

Komplexe Brillen können als Kombination elementarer Operatoren verstanden werden.

Beispiel:

```text
Memetische Genealogie
=
ZEIT
+ TRÄGER
+ VARIATION
+ SELEKTION
+ INSTITUTION
+ RELATION
+ EVIDENZ
```

Oder:

```text
Konfliktmechanik
=
PERSPEKTIVE
+ MACHT
+ INFORMATION
+ RÜCKKOPPLUNG
+ ERREICHBARKEIT
+ ROLLE
```

Dadurch werden Brillen nicht nur sammelbar, sondern **konstruierbar**.

Eine KI kann beispielsweise aufgefordert werden:

> Baue für dieses Problem eine Perspektive aus ZEIT, MACHT, INFORMATION und PFADABHÄNGIGKEIT.

Oder:

> Welche drei möglichst orthogonalen Schnitte würden hier wahrscheinlich den größten Erkenntnisgewinn erzeugen?

Damit entsteht schrittweise eine kleine **Algebra epistemischer Perspektiven**.

---

## Die Meta-Brille

Eine besondere Rolle spielt die Meta-Brille.

Sie betrachtet nicht primär den Gegenstand, sondern den **aktuellen Erkenntnisprozess**.

Sie fragt beispielsweise:

* Welche Brille verwenden wir gerade?
* Was macht sie besonders gut sichtbar?
* Was kann sie schlecht sehen?
* Welches Restproblem bleibt übrig?
* Welche weitere Perspektive wäre möglichst orthogonal?
* Widersprechen sich zwei Brillen tatsächlich oder betrachten sie nur verschiedene Ebenen?
* Welche Ergebnisse lassen sich kombinieren?

Damit wird Perspektivwechsel selbst zu einer epistemischen Operation.

Mehrere Brillen können parallel gehalten werden, ohne ihre Unterschiede vorschnell aufzulösen.

Das ermöglicht eine Art **perspektivische Stereoskopie**.

---

## Epistemisches Budget

Perspektiven lassen sich theoretisch fast beliebig kombinieren.

Praktisch sind jedoch:

* Zeit,
* Rechenleistung,
* Aufmerksamkeit,
* Kontext,
* verfügbare Evidenz

begrenzt.

Darum gehört zur Metaebene auch ein **epistemisches Budget**.

Die relevante Frage lautet nicht nur:

> Was könnte noch untersucht werden?

sondern:

> **Welcher nächste epistemische Schritt verspricht den größten Erkenntnisgewinn im Verhältnis zu seinen Kosten?**

Eine KI sollte daher nicht wahllos möglichst viele Brillen anwenden.

Sie sollte:

1. eine passende Perspektive wählen,
2. den Gegenstand untersuchen,
3. Restprobleme bestimmen,
4. nur dort zusätzliche Perspektiven einsetzen, wo relevanter Erkenntnisgewinn zu erwarten ist,
5. abbrechen, wenn zusätzliche Komplexität kaum noch zusätzlichen Nutzen erzeugt.

Orthogonalität ist damit nicht nur erkenntnistheoretisch interessant.

Sie kann auch eine **Kompressions- und Rechenstrategie** sein.

---

## Wie benutzt man den Brillenladen?

Die einfachste Verwendung ist:

1. Eine passende epistemische Spezifikation auswählen.
2. Der KI die Spezifikation als Arbeitsgrundlage geben.
3. Mit einer normalen Beobachtung oder Frage beginnen.
4. Der Untersuchung folgen.

Zum Beispiel:

> Betrachte diese Situation mit der Brille „Anreizstrukturen“.

Oder:

> Ich habe hier eine Beobachtung. Welche Brille wäre dafür interessant?

Oder:

> Betrachte das parallel unter Macht, Informationsfluss und Pfadabhängigkeit.

Oder einfach:

> Was ist hier mit dieser Brille interessant?

Der Anwender muss die Operatoren nicht kennen.

Die Begriffe sind Werkzeuge für die KI, nicht Zugangsvoraussetzungen für den Benutzer.

---

## Brille ist nicht Wirklichkeit

Jede Brille hebt bestimmte Strukturen hervor und lässt andere zurücktreten.

Deshalb gilt:

> **Die Brille ist nicht die Wirklichkeit.**

Eine epistemische Spezifikation behauptet nicht, die einzig richtige Beschreibung eines Gegenstands zu liefern.

Sie erzeugt einen bestimmten Schnitt.

Andere Schnitte können andere Strukturen sichtbar machen.

Gerade deshalb ist der bewusste Wechsel zwischen möglichst unterschiedlichen Perspektiven interessant.

---

## Anforderungen an eine gute Spezifikation

Eine brauchbare epistemische Spezifikation sollte:

* eine klare Leitfrage besitzen,
* ihre relevanten Operatoren benennen,
* möglichst wenige Dimensionen unnötig vermischen,
* charakteristische Denkoperationen festlegen,
* wichtige epistemische Leitplanken enthalten,
* Unsicherheit und Grenzen sichtbar lassen,
* für offene Anschlussfragen geeignet sein.

Sie sollte so ausführlich wie nötig und so knapp wie möglich sein.

Die Ziel-KI darf selbst denken.

Die Spezifikation soll ihr nicht jede Frage vorformulieren.

---

## Wissenstransfer als Erkundung

Traditioneller Wissenstransfer liefert häufig fertige Darstellungen.

Ein Buch erzählt, was ein Autor herausgefunden hat.

Eine epistemische Spezifikation überträgt zusätzlich etwas anderes:

**die Art des Hinschauens, mit der Erkenntnisse gewonnen werden können.**

Damit verändert sich die Rolle des Anwenders.

Er liest nicht nur eine vorgegebene Gedankenfolge.

Er erkundet selbst.

Die KI verbindet vorhandenes Wissen mit einer expliziten Erkenntnisperspektive und untersucht jeweils den Ausschnitt, der gerade gefragt ist.

So muss nicht jede mögliche Untersuchung vorab ausgeschrieben werden.

Das Wissen entsteht im Dialog zwischen:

**Spezifikation – KI – Frage – Gegenstand.**

---

## Der Brillenladen

Der Brillenladen ist damit mehr als eine Sammlung von Prompts.

Er ist ein Katalog:

* elementarer epistemischer Operatoren,
* kompakter epistemischer Spezifikationen,
* ausführbarer Perspektiven,
* und Regeln für ihren bewussten Wechsel und ihre Kombination.

Er liefert keine einheitliche Weltsicht.

Er stellt Werkzeuge bereit, mit denen unterschiedliche Strukturen derselben Welt sichtbar gemacht werden können.

**Brille auswählen.
Aufsetzen.
Hinschauen.
Wechseln.
Kombinieren.
Fragen.**
