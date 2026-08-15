# Brillenladen

## Eine epistemische Zwischensprache für KI-Systeme

## Warum dieser Brillenladen existiert

Ich arbeite viel mit KI-Systemen.  
Dabei ist mir wiederholt dasselbe Problem begegnet:  
Eine KI kann eine Frage hervorragend beantworten – und trotzdem am eigentlichen Problem vorbeidenken.  
Nicht unbedingt, weil ihr Wissen fehlt.  
Sondern weil sie einen bestimmten **Blick auf das Problem** gewählt hat.

Bei einem organisatorischen Problem sucht sie vielleicht nach individuellen Fehlern, obwohl Anreize entscheidend sind.  
Bei einem technischen Problem sucht sie nach Komponenten, obwohl ein zeitlicher Zustand relevant wäre.  
Bei einem Konflikt sucht sie nach Schuld, obwohl unterschiedliche Informationsstände das Geschehen besser erklären.

Die Antwort kann innerhalb dieser Perspektive vollkommen plausibel sein.  
Nur die Perspektive selbst bleibt meistens unsichtbar.  
Das hat mich gestört.

---

## Was daraus entstanden ist

Ich weiß nicht, ob es den einen „richtigen“ Katalog von Analyseperspektiven gibt.  
Wahrscheinlich nicht.  
Der hier vorgestellte ist experimentell, unvollständig und veränderbar.  
Aber ein Format hat sich als brauchbar erwiesen:  
Man beschreibt nicht nur, **was** eine KI untersuchen soll, sondern expliziter, **wie sie hinschauen soll**.

Zum Beispiel:

- **ZEIT** – Wie verändert sich etwas?
- **INFORMATION** – Wer weiß wann was?
- **ANREIZ** – Welche Folgen machen Verhalten attraktiv?
- **EVIDENZ** – Was trägt eine Behauptung?
- **PERSPEKTIVE** – Was ändert sich mit dem Beobachter?

Solche einfachen Schnitte lassen sich kombinieren.  
Daraus entstehen problemabhängige **Brillen**.

Ich weiß nicht, ob die aktuelle Zerlegung optimal ist.
Darum geht es auch nicht.    
Aber ich kann zeigen,  
- warum sie gebaut wurde,
- wie sie funktioniert,
- wo verschiedene KI-Systeme unterschiedlich wählen,
- wo die Konstruktion scheitert,
- und wie sie aufgrund solcher Fehler verändert wird.

---

## Das Angebot

Wer mit KI arbeitet und gelegentlich den Eindruck hat,

> *Die Antwort ist plausibel, aber irgendetwas fehlt*,

kann den Brillenladen ausprobieren.  
Man muss weder den gesamten Operatorenkatalog lernen noch die theoretischen Überlegungen dahinter teilen.  
Man kann mit einem konkreten Problem beginnen und eine KI beispielsweise fragen:

> Welche wenigen unterschiedlichen Schnitte wären hier vermutlich besonders aufschlussreich?  
> Begründe die Auswahl.  
> Prüfe anschließend, was diese Perspektive schlecht sehen kann.

Wenn das keinen Mehrwert bringt, war es die falsche Brille – oder das Werkzeug wird für diesen Fall schlicht nicht gebraucht.

Wer nur eine schnelle technische Beschreibung möchte, kann mit dem **Technical Overview** beginnen.  
Wer die Idee lieber über eine Geschichte versteht, findet **„Der kleine Karl im Brillenladen“**.  
Wer wissen möchte, wie wenig Struktur nötig ist, damit eine KI selbst einen solchen Brillenladen rekonstruiert, kann mit der **Saat-Spezifikation** und ihren Testläufen beginnen.

---

## Technisch gesprochen

Der **Brillenladen** ist ein experimenteller Baukasten für **epistemische Spezifikationen**.

Eine solche Spezifikation beschreibt nicht primär, *was* eine KI über einen Gegenstand denken soll, sondern **wie sie ihn betrachten soll**:

- welche Unterschiede relevant sind,
- welche Beziehungen bevorzugt untersucht werden,
- welche Denkoperationen eingesetzt werden,
- welche Perspektiven getrennt gehalten werden,
- welche typischen Fehler zu vermeiden sind,
- wie Unsicherheit behandelt wird,
- und wann zusätzliche Analyse ihren Aufwand nicht mehr rechtfertigt.

Anschaulich gesprochen ist eine solche Spezifikation eine **Brille**.  
Die Brille ist nicht die Wirklichkeit.  
Sie ist eine für KI ausführbar gemachte Art des Hinschauens.

---

## Die Grundidee

Eine Karte zeigt nicht die ganze Landschaft.

*Sie wählt aus.*

Eine Straßenkarte zeigt andere Strukturen als eine geologische Karte.  
Eine Wanderkarte hebt anderes hervor als ein Katasterplan.  
Keine davon ist deshalb falsch.  
Sie beantwortet andere Fragen.  
Eine epistemische Brille funktioniert ähnlich.

Sie definiert einen bevorzugten **Schnitt durch einen Gegenstand**.  
Mit einer anderen Brille werden andere Strukturen sichtbar.

Die KI kann dabei die Rolle einer **intelligenten Landkarte** übernehmen:

- beim Ausgangspunkt des Anwenders beginnen,
- relevante Strukturen sichtbar machen,
- mögliche Untersuchungsrichtungen vorschlagen,
- Zusammenhänge verfolgen,
- Perspektiven wechseln,
- mehrere Perspektiven parallel halten,
- Widersprüche und Restprobleme markieren,
- neue Fragen erzeugen,
- und die Untersuchung beenden, wenn weitere Komplexität kaum noch Erkenntnisgewinn verspricht.

Der Anwender **muss** die zugrunde liegenden Operatoren **nicht** beherrschen.  
Er kann mit einer normalen Beobachtung, Frage, Behauptung, Irritation oder einem Text beginnen.

---

# 1. Epistemische Operatoren

Die Datei `00-epistemische-operatoren.md` enthält einen offenen Katalog möglichst elementarer epistemischer Operationen.

Beispiele:

- DIFFERENZ
- GRENZE
- ZEIT
- SKALA
- PERSPEKTIVE
- ZUSTAND
- ÜBERGANG
- ERREICHBARKEIT
- RELATION
- KAUSALITÄT
- RÜCKKOPPLUNG
- INFORMATION
- TRÄGER
- VARIATION
- SELEKTION
- ANREIZ
- MACHT
- ROLLE
- KOORDINATION
- INSTITUTION
- IRREVERSIBILITÄT
- RESILIENZ
- EMERGENZ
- EVIDENZ
- GEGENHYPOTHESE
- NEBENFOLGE
- NORM
- BEGRIFF

Die Leitidee ist eine Art **epistemische Primfaktorzerlegung**:

> Finde möglichst elementare Unterschiede und Operationen, aus denen komplexere Perspektiven zusammengesetzt werden können.

Die Operatoren sollen möglichst **orthogonal** sein.  
Damit ist keine mathematisch strenge Unabhängigkeit gemeint.  
Gemeint ist:

> Zwei Operatoren sollten möglichst unterschiedliche Fragen an denselben Gegenstand stellen.

Komplexität soll aus ihrer Kombination entstehen – nicht aus unscharfen Grundbegriffen.

---

# 2. Brillen als Kompositionen

Ein einzelner Operator ist noch keine vollständige Perspektive.  
Interessant wird der Brillenladen durch Kombination.

Zum Beispiel:

```text
Pfadabhängigkeit
=
ZEIT
+ ZUSTAND
+ ÜBERGANG
+ ERREICHBARKEIT
+ IRREVERSIBILITÄT
+ RÜCKKOPPLUNG
```

Oder:

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

Dadurch werden Brillen nicht nur sammelbar.  Sie werden **konstruierbar**.

Eine hinreichend leistungsfähige KI kann aus dem Operatorenkatalog problemabhängig selbst eine kleine Perspektive zusammenstellen.  
Damit entsteht schrittweise eine **Algebra epistemischer Perspektiven**.  
Nicht als fertiger mathematischer Formalismus, sondern zunächst als kompositionelle Grammatik:

> elementare Operatoren → Kombination → Perspektive → Analyse

---

# 3. Epistemische Spezifikationen

Die Datei `01-kompakte-spezifikationen.md` enthält bereits zusammengesetzte Brillen in kompakter Form.

Eine Spezifikation besteht typischerweise aus:

- einer Leitfrage,
- den wichtigsten Operatoren,
- einigen Kernkonzepten,
- bevorzugten Denkoperationen,
- epistemischen Leitplanken.

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
Das Kompressionsprinzip lautet:

> **So wenig Vorgabe wie möglich. So viel Struktur wie nötig.**

---

# 4. Dynamische Brillenkonstruktion

Der Brillenladen ist nicht auf vorgefertigte Spezifikationen beschränkt.  
Eine KI kann auch nur den Operatorenkatalog erhalten und daraus selbst eine passende Perspektive konstruieren.  
Ein möglicher Ablauf:

1. zentrale Irritation oder Erkenntnisfrage bestimmen,
2. Operatoren mit hohem erwarteten Erkenntnisgewinn auswählen,
3. möglichst redundante Schnitte vermeiden,
4. aus den Operatoren eine kleine epistemische Spezifikation bilden,
5. den Gegenstand damit untersuchen,
6. Restprobleme und Blindstellen bestimmen,
7. gegebenenfalls einen weiteren Schnitt hinzufügen,
8. abbrechen, wenn der zusätzliche Erkenntnisgewinn zu gering wird.

Der entscheidende Punkt ist:

> Die KI verwendet nicht einfach möglichst viele Perspektiven.

Sie baut eine **problemabhängige Arbeitsbrille**.

---

# 5. Meta-Operatoren

Einige Operatoren richten sich nicht primär auf den Gegenstand, sondern auf die aktuelle Untersuchung selbst.

Dazu gehören unter anderem:

- **BRILLENWAHL** – Welche Perspektive verspricht hier den größten Erkenntnisgewinn?
- **BRILLENWECHSEL** – Welche bisher vernachlässigte Perspektive könnte das Restproblem sichtbar machen?
- **PARALLELSICHT** – Wie sieht derselbe Gegenstand gleichzeitig unter mehreren möglichst unterschiedlichen Perspektiven aus?
- **SYNTHESE** – Welche Ergebnisse lassen sich kompatibel verbinden?
- **SPANNUNG** – Wo erzeugen Perspektiven tatsächlich unterschiedliche oder widersprüchliche Modelle?
- **BLINDSTELLE** – Was kann die aktuelle Perspektive strukturell schlecht sehen?
- **BUDGET** – Welcher nächste epistemische Schritt rechtfertigt seinen Aufwand?

Damit kann die KI nicht nur den Gegenstand analysieren.

Sie kann auch ihre **aktuelle Analysearchitektur**  *explizit!* behandeln.

---

# 6. Epistemisches Budget

Perspektiven lassen sich theoretisch beinahe beliebig kombinieren.  
Praktisch sind jedoch begrenzt:

- Zeit,
- Rechenleistung,
- Aufmerksamkeit,
- Kontext,
- verfügbare Evidenz.

Darum gehört zur Metaebene ein **epistemisches Budget**.

Die relevante Frage lautet nicht nur:

> Was könnte noch untersucht werden?

Sondern:

> **Welcher nächste epistemische Schritt verspricht den größten Erkenntnisgewinn im Verhältnis zu seinen Kosten?**

Eine Analyse kann deshalb iterativ verlaufen:

```text
Problem
↓
erste Operatorenauswahl
↓
Analyse
↓
Restproblem
↓
nächster sinnvoller Schnitt?
↓
ja → erweitern
nein → abbrechen
```

Auch das Beenden einer Analyse ist damit eine epistemische Operation.  
Orthogonalität ist in diesem Zusammenhang nicht nur erkenntnistheoretisch interessant.  
Sie kann auch eine **Kompressions- und Rechenstrategie** sein.

---

# 7. Die inverse Operation: epistemische Faktorisierung

Wenn sich aus Operatoren eine Perspektive konstruieren lässt, kann man die Bewegung auch **umkehren**.

Gegeben sei nun kein Problem, sondern beispielsweise:

- ein Bericht,
- eine Erzählung,
- eine politische Rede,
- ein wissenschaftlicher Text,
- ein Strategiepapier,
- eine persönliche Konfliktdarstellung.

Dann lautet die Frage:

> **Welche Brille wird hier bereits verwendet?**

Die KI versucht, die charakteristische Perspektive auf eine möglichst kleine Menge tragender Operatoren zurückzuführen.

Zum Beispiel:

```text
Darstellung
≈
KAUSALITÄT
+ ANREIZ
+ ROLLE
```

oder:

```text
Darstellung
≈
ZEIT
+ INSTITUTION
+ RÜCKKOPPLUNG
```

Das Ziel ist nicht, möglichst viele irgendwie passende Operatoren im Text zu finden.  
Gesucht wird vielmehr:

> **Welche minimale Kombination erklärt den charakteristischen Blick dieser Darstellung?**

Diese Rückwärtsbewegung wird hier **epistemische Faktorisierung** genannt.  
Sie erlaubt anschließend weitere Fragen:

- Welche Schnitte dominieren?
- Welche fehlen?
- Welche Blindstellen entstehen daraus?
- Sind zwei Darstellungen tatsächlich widersprüchlich?
- Oder schneiden sie denselben Gegenstand nur auf verschiedenen Ebenen?

Das Ergebnis ist kein psychologisches Profil eines Autors.  
Es sagt nicht:  
> So denkt dieser Mensch.  
Sondern:  

> **So wird in diesem Text gedacht.**

---

# 8. Vorwärts und rückwärts

Damit entsteht eine einfache Symmetrie.

## Vorwärts

```text
Szene
→ Irritation
→ Operatorenauswahl
→ Brille
→ Analyse
```

## Rückwärts

```text
Darstellung
→ charakteristischer Blick
→ Faktorisierung
→ Operatoren
→ epistemisches Profil
```

Die erste Bewegung erzeugt einen Blick.  
Die zweite rekonstruiert einen vorhandenen.  
Zusammen bilden sie eine kleine Sprache für Perspektiven.  
Nicht für die Welt selbst.  
Sondern für die Art, wie wir sie schneiden.

---

# 9. Keine Wahrheitsmaschine

Der Brillenladen entscheidet nicht, was wahr ist.  
Ein sauber konstruierter kausaler Blick kann auf falschen Daten beruhen.  
Eine präzise faktorisierte Erzählung kann unwahre Behauptungen enthalten.  
Eine multiperspektivische Analyse kann sich trotzdem irren.  
Epistemische Struktur und Wahrheit sind nicht dasselbe.  
Der Brillenladen arbeitet eine Ebene davor.  
Er macht **sichtbar**:

- welche Fragen gestellt werden,
- welche Schnitte verwendet werden,
- welche Arten von Erklärung entstehen,
- welche Alternativen zunächst unsichtbar bleiben.

Danach können Evidenzprüfung, Recherche, Experiment, Statistik oder Argumentation einsetzen.  
Der Brillenladen ersetzt diese Verfahren nicht.  
Er kann helfen zu entscheiden, **welche davon überhaupt gebraucht werden**.

---

# 10. Was der Brillenladen nicht ist

Der Brillenladen ist:

- kein Prompt-Katalog,
- keine Sammlung von Expertenrollen,
- kein Multi-Agent-System,
- keine Ontologie,
- keine vollständige Erkenntnistheorie,
- keine Wahrheitsmaschine.

Er ist eher eine:

> **epistemische Zwischensprache für KI-Systeme.**  
Sein Vokabular besteht aus elementaren epistemischen Operatoren.  
Seine Grammatik besteht aus deren Kombination.  
Seine Optimierungsregel ist das epistemische Budget.  
Seine Vorwärtsoperation ist die Konstruktion einer Perspektive.  
Seine inverse Operation ist deren Faktorisierung.  
Sein Zweck ist Orientierung.

Technischer formuliert:

> **Ein kompositioneller Operatorenkatalog zur Konstruktion und Rekonstruktion von Analyseperspektiven.**

---

# 11. Wie benutzt man den Brillenladen?

Es gibt inzwischen drei grundlegende Nutzungsarten.

## A. Eine vorhandene Brille anwenden

> Betrachte diese Situation mit der Brille „Anreizstrukturen“.

Oder:

> Analysiere das parallel unter Macht, Informationsfluss und Pfadabhängigkeit.

---

## B. Eine Brille dynamisch konstruieren lassen

Dazu genügt grundsätzlich der Operatorenkatalog.

Zum Beispiel:

> Bestimme zunächst, was an dieser Situation erklärungsbedürftig ist.  
> Wähle dann eine möglichst kleine Menge geeigneter epistemischer Operatoren.  
> Begründe die Auswahl anhand von Erkenntnisgewinn, Orthogonalität und epistemischem Budget.  
> Konstruiere daraus eine Perspektive, führe sie aus und prüfe anschließend Restprobleme und Blindstellen.

---

## C. Eine vorhandene Darstellung faktorisieren

> Rekonstruiere die dominante epistemische Perspektive dieses Textes.  
> Führe sie auf eine möglichst kleine Menge tragender Operatoren zurück.  
> Benenne anschließend naheliegende, aber unterrepräsentierte Schnitte.

---

Der Anwender muss die Operatoren nicht selbst kennen.  
Die Begriffe sind **Werkzeuge für die KI, nicht Zugangsvoraussetzungen für den Benutzer**.

---

# 12. Weitere Zugänge zum Brillenladen

Nicht jeder Zugang muss über die ausführliche konzeptionelle Beschreibung führen.  
Deshalb existieren inzwischen mehrere Darstellungsformen für unterschiedliche Einstiegspunkte.

## Technical Overview

`Brillenladen-Technical-Overview-DE.md`

Die kompakte technische Fassung beginnt beim praktischen Problem:

- Perspektivwahl in Sprachmodellen bleibt oft implizit,
- epistemische Operatoren machen Analysebewegungen expliziter,
- Operatoren lassen sich problemabhängig kombinieren,
- eine Metaebene steuert Auswahl, Wechsel, Blindstellen und Budget,
- vorhandene Darstellungen lassen sich invers faktorisieren.

Diese Fassung richtet sich vor allem an technisch orientierte Leser, die zuerst wissen möchten:

> **Was ist das, wie funktioniert es, und wozu könnte ich es benutzen?**

## Der kleine Karl im Brillenladen

`Der-kleine-Karl-im-Brillenladen.md`

Die kurze Geschichte erklärt das Grundprinzip ohne Fachsprache.  
Karl probiert unterschiedliche Brillen aus und entdeckt, dass jede andere Dinge sichtbar macht.  
Als er immer mehr Brillen gleichzeitig aufsetzt, sieht er irgendwann vor allem noch die Brillen.  
Am Ende bekommt er vom Brillenmacher eine besonders unscheinbare Brille geschenkt:

**NEUGIER**

Sie ist dort scharf, wo Du noch nicht hingesehen hast, obwohl es vielleicht etwas zu finden gäbe.  
Die Geschichte ist keine technische Spezifikation.  
Sie ist ein intuitiver Zugang zu Perspektivwahl, Perspektivwechsel, epistemischem Budget und der Bereitschaft, noch einmal anders hinzusehen.

## Die Saat-Spezifikation

`Brillenladen-Saat-Spezifikation.md`

Die Saat geht in die entgegengesetzte Richtung.  
Sie enthält **keinen fertigen Operatorenkatalog**.  
Stattdessen beschreibt sie die Bedingungen, unter denen eine leistungsfähige KI selbst einen solchen Katalog erzeugen soll:

- möglichst elementare Operatoren,
- geringe Redundanz,
- domänenübergreifende Verwendbarkeit,
- Komposition,
- Meta-Steuerung,
- epistemisches Budget,
- inverse Faktorisierung,
- Tests,
- Selbstkritik und Revision.

Sie ist damit eine Art **generative Spezifikation** des Brillenladens.  
Oder kürzer:

> Nicht der Bauplan eines fertigen Hauses, sondern eine Saat plus Beschreibung des Biotops, in dem etwas dieser Art wachsen soll.

## Phänotypen der Saat

Die gleiche Saat wurde mehreren KI-Systemen mit demselben sehr knappen Prompt gegeben:

> Nimm dies, und sprich.

Unter anderem entstanden Phänotypen von:

- DeepSeek,
- Grok,
- Kimi,
- Perplexity,
- Qwen.

Die erzeugten Operatorenkataloge sind nicht identisch.

Trotzdem rekonstruieren sie auffällig ähnliche Grundstrukturen:

- elementare analytische Schnitte,
- Kombination zu Perspektiven,
- Meta-Operationen,
- Blindstellenkontrolle,
- Budget und Abbruch,
- inverse Faktorisierung,
- Selbstprüfung des eigenen Katalogs.

Der Vergleich liegt in:

`Tests/Brillenladen-Saat-Testvergleich.md`

Ein vorläufiger Befund lautet:

> **Die Saat scheint eher eine Strukturklasse als einen konkreten Katalog zu spezifizieren.**

Die Modelle erzeugen keine Klone.

Sie erzeugen verschiedene mögliche **Basen eines ähnlichen epistemischen Raums**.

## Transparenz statt Autoritätsbehauptung

Ein erheblicher Teil des Brillenladens ist in dialogischer Arbeit mit KI-Systemen entstanden.

KI war dabei gleichzeitig:

- Werkzeug,
- Sparringspartner,
- Generator alternativer Zerlegungen,
- Testgegenstand,
- und gelegentlich Fehlerquelle.

Deshalb sind gerade die Unterschiede und Fehlversuche wichtig.  
Wo ein Modell Operatoren anders zerlegt, wird verglichen.  
Wo ein Test unerlaubt Tatsachen ergänzt, wird die Spezifikation nachgeschärft.  
So wurde die Saat beispielsweise um einen Guardrail ergänzt, nachdem mehrere Modelle in Testfällen fehlende Befunde durch erfundene Details ersetzt hatten.  
Die relevante Frage soll deshalb nicht lauten:

> Hat ein Mensch oder eine KI diesen Satz formuliert?

Sondern:

> **Ist der Gedankengang nachvollziehbar, prüfbar, reproduzierbar und nützlich?**

Der Brillenladen bittet nicht um Vertrauen in eine Autorität.  
Er stellt seine Konstruktion zur Prüfung.

---

# 13. Ausführliche Beispiele

Der Ordner `Beispiele/` enthält ausführlichere Brillenmodelle.

Sie dienen vor allem:

- als Referenz für die Konstruktion neuer Brillen,
- zur Demonstration des Konzepts,
- zur Prüfung der Kompression,
- und als Material für Systeme, die mehr Führung benötigen.

Die ausführlichen Modelle sind nicht zwingend die endgültige Form.

Sie zeigen, **was eine kompakte epistemische Spezifikation implizit enthalten kann**.

---

# 14. Tests

Der Ordner `Tests/` dient dazu, den Brillenladen nicht nur konzeptionell, sondern praktisch zu prüfen.

Bisher wurden mehrere Arten von Versuchen durchgeführt.

## Test 1: Ein Gegenstand, mehrere fertige Brillen

Derselbe abstrakte Organisationsfall wurde mit mehreren vorgegebenen Brillen untersucht.

Geprüft wurden insbesondere:

- perspektivische Trennschärfe,
- Redundanz,
- Orthogonalität,
- Komponierbarkeit,
- Restprobleme,
- Meta-Synthese,
- Budget-Sensitivität.

Mehrere KI-Systeme konnten die verschiedenen Perspektiven erkennbar getrennt anwenden und anschließend Gemeinsamkeiten, Spannungen und Blindstellen beschreiben.

---

## Test 2: Brillenkonstruktion nur aus Operatoren

In einem härteren Versuch erhielten KI-Systeme keine fertigen Brillen, sondern nur den Operatorenkatalog samt Meta-Operatoren und BUDGET.

Die Aufgabe bestand darin:

- selbst relevante Operatoren auszuwählen,
- daraus eine problemabhängige Perspektive zu konstruieren,
- sie auszuführen,
- Restprobleme festzustellen,
- gegebenenfalls zu erweitern,
- und kontrolliert abzubrechen.

Die ersten Versuche zeigen, dass aktuelle KI-Systeme mit diesem Verfahren zumindest grundsätzlich umgehen können.  
Sie wählen nicht identisch.  
Das ist auch nicht erforderlich.

Interessanter ist:

- Können sie ihre Auswahl begründen?
- Erkennen sie Redundanz?
- Finden sie Blindstellen?
- Wechseln sie bei einem Restproblem sinnvoll die Perspektive?
- Können sie zusätzliche Komplexität auch ablehnen?
- Können sie aufhören?

Diese Tests sind noch kein Nachweis einer allgemeinen Gültigkeit.

Sie sind ein erster **Proof of Concept**.

---

## Test 3: Rekonstruktion aus einer Saat

In einem weiteren Versuch erhielten mehrere KI-Systeme keinen fertigen Brillenladen.

Sie erhielten lediglich eine **Saat-Spezifikation**, die beschreibt, welche Eigenschaften ein epistemischer Operatorenkatalog besitzen und wie er sich selbst prüfen soll.

Der Prompt war jeweils möglichst klein:

> Nimm dies, und sprich.

Getestet wurden unter anderem DeepSeek, Grok, Kimi, Perplexity und Qwen.

Die Modelle erzeugten unterschiedliche Kataloge.

Die Zahl und Benennung der Grundoperatoren variierte deutlich.

Trotzdem blieben mehrere strukturelle Eigenschaften erstaunlich stabil:

- Komposition elementarer Schnitte,
- explizite Meta-Operationen,
- Minimalität,
- Blindstellenanalyse,
- epistemisches Budget,
- kontrollierter Abbruch,
- inverse Faktorisierung,
- Selbstkritik und Revision.

Ein besonders interessanter Fall war Qwen:

Das Modell erzeugte zunächst einen sehr kompakten Katalog, stellte während der eigenen Tests fest, dass **SKALA** nicht ausreichend ausdrückbar war, und ergänzte den Operator nachträglich.

Damit wurde genau der vorgesehene Zyklus sichtbar:

```text
Konstruktion
→ Anwendung
→ Defizit
→ Revision
```

### Methodische Korrektur

Der erste Saat-Test zeigte zugleich eine Schwäche der ursprünglichen Spezifikation.

Mehrere Modelle erfanden in den Testfällen konkrete Befunde, die nicht gegeben waren.

Daraufhin wurde ein Guardrail ergänzt:

> Nicht gegebene Tatsachen dürfen ausschließlich als Hypothesen, Prüfungen oder benötigte Beobachtungen formuliert werden. Fehlende Evidenz ist als Restproblem zu markieren und darf nicht durch erfundene Befunde ersetzt werden.

Der ausführliche Vergleich liegt in:

`Tests/Brillenladen-Saat-Testvergleich.md`

Die weiterführende Frage lautet inzwischen nicht mehr:

> Erzeugen alle Modelle denselben Operatorenkatalog?

Sondern:

> **Welche strukturellen Invarianten bleiben erhalten, wenn unterschiedliche Modelle aus derselben Saat ihre eigene epistemische Grammatik erzeugen?**


# 15. Projektstruktur

Eine mögliche Struktur des Brillenladens:

```text
Brillenladen/
├── README.md
├── 00-epistemische-operatoren.md
├── 01-kompakte-spezifikationen.md
├── Brillenladen-Technical-Overview-DE.md
├── Der-kleine-Karl-im-Brillenladen.md
├── Brillenladen-Saat-Spezifikation.md
├── Beispiele/
│   ├── ...
│   └── meta-brille.md
└── Tests/
    ├── 01-ein-gegenstand-mehrere-brillen.md
    ├── Brillenladen-Saat-Spezifikation-Phänotyp-deepseek.md
    ├── Brillenladen-Saat-Spezifikation-Phänotyp-Grok.md
    ├── Brillenladen-Saat-Spezifikation-Phänotyp-Kimi.md
    ├── Brillenladen-Saat-Spezifikation-Phänotyp-perplexity.md
    ├── Brillenladen-Saat-Spezifikation-Phänotyp-Qwen.md
    └── Brillenladen-Saat-Testvergleich.md
```

Die Struktur ist nicht endgültig.

Der Brillenladen ist selbst Gegenstand seiner eigenen Untersuchung.

Neue Anwendungen können zeigen, dass:

- Operatoren fehlen,
- bestehende Operatoren redundant sind,
- einzelne Operatoren aufgeteilt werden sollten,
- neue Kompositionsregeln sinnvoll sind,
- das epistemische Budget präziser gefasst werden muss,
- oder sich weitere Meta-Operationen ergeben.

---

# 16. Status

Der Brillenladen ist ein **experimenteller Entwurf**.

Inzwischen ist nicht nur der konkrete Operatorenkatalog Gegenstand der Tests.

Auch die Frage, **wie stabil sich die zugrunde liegende Architektur aus einer kompakten Saat über verschiedene KI-Systeme hinweg rekonstruieren lässt**, wird experimentell untersucht.

Der Operatorenkatalog beansprucht weder Vollständigkeit noch mathematisch strenge Unabhängigkeit.  
Die bisherigen Spezifikationen und Kompositionen sind Arbeitsmodelle.  
Gerade die Anwendung auf sehr unterschiedliche Gegenstände soll zeigen:

- welche Operatoren tragen,
- welche überlappen,
- welche fehlen,
- welche Kombinationen besonders produktiv sind,
- und wie stabil das Konzept über verschiedene KI-Systeme hinweg ist.

Die Grammatik soll sich durch Gebrauch weiterentwickeln.

---

# 17. Wissenstransfer als Erkundung

Traditioneller Wissenstransfer liefert häufig fertige Darstellungen.  
Ein Buch erzählt, was ein Autor herausgefunden hat.  
Eine epistemische Spezifikation überträgt zusätzlich etwas anderes:

> **die Art des Hinschauens, mit der Erkenntnisse gewonnen werden können.**

Damit verändert sich die Rolle des Anwenders.

Er liest nicht nur eine vorgegebene Gedankenfolge.

Er erkundet selbst.

Die KI verbindet vorhandenes Wissen mit einer expliziten Erkenntnisperspektive und untersucht jeweils den Ausschnitt, der gerade gefragt ist.

So muss nicht jede mögliche Untersuchung vorab ausgeschrieben werden.

Das Wissen entsteht im Dialog zwischen:

**Operatoren – Spezifikation – KI – Frage – Gegenstand.**

---

# Der Brillenladen

Der Brillenladen ist damit ein Katalog:

- elementarer epistemischer Operatoren,
- kompakter epistemischer Spezifikationen,
- ausführbarer Perspektiven,
- Regeln für ihre Konstruktion und Kombination,
- Verfahren zu ihrer Rekonstruktion,
- Meta-Operatoren für Perspektivwechsel und Blindstellen,
- und eines epistemischen Budgets zur Begrenzung der Komplexität.

Er liefert keine einheitliche Weltsicht.

Er stellt Werkzeuge bereit, mit denen unterschiedliche Strukturen derselben Welt sichtbar gemacht werden können.

**Brille auswählen.  
Oder bauen.  
Aufsetzen.  
Hinschauen.  
Wechseln.  
Faktorisieren.  
Absetzen.  
Fragen.**

Klaus Dantrimont 2026
