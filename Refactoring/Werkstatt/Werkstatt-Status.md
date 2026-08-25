# Werkstatt – Status quo

**Stand:** 24. August 2026  
**Funktion:** Arbeitskarte der derzeit relevanten Erkenntnis- und Dokumentstränge.  
**Charakter:** veränderliche Sicht, kein Archiv und keine vollständige Inventarliste.

Dieses Dokument ergänzt die Projektspezifikation **„Forschungsindex“**. Die Spezifikation beschreibt, *wie* Funde erkannt und eingeordnet werden. Dieses Dokument beschreibt, *was derzeit lebendig, ausgearbeitet, ungeklärt oder anschlussfähig ist*.

Der Status soll regelmäßig konsolidiert werden. Er darf schrumpfen. Abgeschlossene, verworfene oder in andere Dokumente überführte Punkte müssen hier nicht dauerhaft erhalten bleiben.

---

## 1. Aktueller Schwerpunkt

Der gegenwärtig stärkste Entwicklungsstrang liegt nicht mehr nur in der Ausarbeitung der Differenzfluss-Theorie selbst, sondern in der Frage:

> **Wie lassen sich gute epistemische Schnitte, Zerlegungen und Perspektiven finden, explizit machen, kombinieren und für KI-Systeme operationalisieren?**

Daraus ist inzwischen ein zusammenhängender Werkzeugraum entstanden:

```text
Refactoring komplexer Problemräume
        ↓
epistemische Operatoren / Schnitte
        ↓
Brillen als Kompositionen
        ↓
Fragen als epistemische Aufträge
        ↓
Linter / Tutor / Textprofile / Agenten
```

Die DFT wirkt dabei zunehmend als **Unterboden, Strukturintuition und Suchgrammatik**, nicht notwendig als sichtbare Oberfläche jedes Werkzeugs.

---

## 2. Aktive Forschungsfäden

### A. Refactoring / gute Zerlegung

**Status:** ausgearbeitet → erste Tests

Zentrale Frage:

> Wie findet man eine möglichst abstrakte, tragende und generative Zerlegung eines komplexen Systems?

Der Strang ist inzwischen in mehrere Ebenen differenziert:

- **R1:** Qualitätskriterien guter Zerlegung: Strukturerhalt, Minimalität, geringe Redundanz, Orthogonalität, Kompositionalität, Rekonstruktionskraft, Transferfähigkeit, Operationalisierbarkeit.
- **R2:** Suche nach geeigneten Schnitten und Basisdimensionen.
- **R3:** Lernen und Metarefactoring; erfolgreiche und gescheiterte Zerlegungen werden selbst zum Lernmaterial für die Verbesserung des Operatorenraums.
- **E1 / E1.2:** Proof-of-Concept für strukturellen Transfer mit Baseline-vs.-Refactoring-Vergleich.

**Offen:** Die bisherigen Tests sind Proofs of Concept, keine belastbare Evaluation. Benötigt werden mehr und schwierigere Testfälle, saubere Baselines und möglichst automatisierte Testläufe.

**Wichtige Dokumente:** `Refactoring/readme.md`, `01-R1-gute-Zerlegung.md`, `03-R2-Basisfindung.md`, `04-R3-Lernen-und-Metarefactoring.md`, `Tests/E1.2-Testpaket/`.

---

### B. Brillenladen / epistemische Operatoren

**Status:** ausgearbeitet → plausibilisiert → experimentell getestet

Der Brillenladen hat sich von einer Sammlung nützlicher Perspektiven zu einer **epistemischen Zwischensprache für KI-Systeme** entwickelt.

Kernidee:

> Komplexe Perspektiven lassen sich als Komposition elementarer epistemischer Operatoren auffassen.

Der Operatorenkatalog enthält u. a. DIFFERENZ, GRENZE, ZEIT, SKALA, PERSPEKTIVE, ZUSTAND, ÜBERGANG, ERREICHBARKEIT, RELATION, KAUSALITÄT, RÜCKKOPPLUNG, INFORMATION, VARIATION, SELEKTION, ANREIZ, MACHT, ROLLE, KOORDINATION, EVIDENZ, GEGENHYPOTHESE und BEGRIFF.

Der interessante Anspruch ist nicht ein endgültiger Katalog, sondern eine Art **epistemische Primfaktorzerlegung**: möglichst unabhängige Schnitte, aus denen komplexere Brillen zusammengesetzt werden können.

Besonders wichtig ist das Saat-Experiment: Verschiedene Modelle erzeugten aus derselben abstrakten Spezifikation unterschiedliche konkrete Operatorenkataloge, aber eine stark konvergierende Meta-Architektur. Das spricht dafür, dass die Saat eher eine **Strukturklasse** als eine feste Taxonomie spezifiziert.

**Offen:** adversariale Grenzfälle; Vergleich mit klassischer Rollenzuweisung; automatisierter Flächentest über unterschiedliche Problem- und Analyselandschaften; Frage, welche Operatoren tatsächlich elementar, redundant oder kontextabhängig sind.

**Wichtige Dokumente:** `Anwendungen/Brillenladen/00-epistemische-operatoren.md`, `01-kompakte-spezifikationen.md`, `Brillenladen-Saat-Spezifikation.md`, `Brillenladen-Technical-Overview-DE.md`, `Tests/`.

---

### C. Die Kunst der Frage 2.0

**Status:** ausgearbeitet

Die frühere Fragegrammatik ist in eine allgemeinere Sicht übergegangen:

> **Eine Frage ist eine Spezifikation eines epistemischen Auftrags.**

Wichtige Parameter sind Gegenstand, Erkenntnisinteresse, das fundamentale **„bezüglich“**, Abstraktionstiefe, Schnittfreiheit, Gegenprüfung, Residuum und Meta-Perspektive.

Damit entsteht eine natürliche Benutzerschnittstelle zu leistungsfähiger KI: Der Mensch muss nicht jeden Denkoperator einzeln vorgeben. Er sollte vor allem präzisieren können, **welche Art von Erkenntnis gesucht wird**.

**Offen:** Verhältnis zwischen einfacher natürlicher Frage, expliziter epistemischer Spezifikation und automatisch gewählter Operatorenkomposition weiter testen.

**Wichtiges Dokument:** `Refactoring/08-Die-Kunst-der-Frage-2.0.md`.

---

### D. Epistemischer Linter

**Status:** Spezifikation ausgearbeitet; Anwendungskonzept vorhanden

Kernidee:

> Eine KI sollte nicht nur Antworten prüfen, sondern vor der Bearbeitung erkennen können, ob eine Frage ihren Problemraum bereits ungünstig konstruiert.

Prüfklassen sind u. a. begriffliche Unterbestimmtheit, Kategorienvermischung, Präsuppositionen, Kausalitätsannahmen, Reifikation, Skalen- und Perspektivenvermischung, falsche Alternativen, Begriffsdrift und ungeklärte Systemgrenzen.

Zentrale Leitplanke:

> **Nur eingreifen, wenn die Struktur der Frage die mögliche Antwort wesentlich verändert.**

Keine stille Reparatur: problematische Schnitte sollen sichtbar gemacht, nicht unbemerkt durch die Perspektive der KI ersetzt werden.

**Offen:** systematische Tests an echten Nutzerfragen; Schwelle zwischen hilfreichem Linting und störender Metakommunikation; Fehlalarme; Domänenabhängigkeit.

**Wichtige Dokumente:** `Refactoring/Anwendungen/Der epistemische Linter.md`, `Epistemische Linter-spec.md`.

---

### E. Epistemisch diagnostischer Tutor

**Status:** Spezifikation Version 2; noch zu testen

Der Tutor verbindet Wissensvermittlung mit fortlaufender Hypothesenbildung über das mentale Modell des Lernenden.

Arbeitszyklus:

```text
Diagnose → Linting → Intervention → Prüfung → Anpassung
```

Das Lehrziel ist nicht schnelle Antwortproduktion, sondern die Verbesserung des eigenen Modells, der Fragefähigkeit, Begriffsarbeit, Fehlererkennung, Unsicherheitstoleranz und Transferleistung des Lernenden.

**Offen:** Testskript praktisch durchführen; verschiedene Lernertypen und Fehlmodelle testen; prüfen, wo LLMs Diagnose nur plausibel simulieren; Interventionsdosis und Überhilfe untersuchen.

**Wichtiges Dokument:** `Refactoring/Anwendungen/Epistemisch diagnostischer Tutor.md`.

---

### F. Epistemische Textprofile

**Status:** neuer ausgearbeiteter Ansatz

Ausgangspunkt ist die Kritik an der Frage „Klingt dieser Text nach KI?“.

Unterschieden werden:

> **Provenienz des Textes**

und

> **epistemische Leistung des Textes**.

Ein fertiger Text enthält nur begrenzte Evidenz über seinen Erzeugungsprozess, aber viel Evidenz über seine eigene Struktur: Behauptungen, Evidenz, Schlüsse, Begriffe, Perspektiven, Unsicherheit, Gegenpositionen und erzeugte Fragen.

Daraus folgt die Idee eines **epistemischen Textprofils**, das die Erkenntnisleistung eines Textes bezüglich seines Zwecks beschreibt, statt aus Stilmerkmalen primär Autorenschaft oder KI-Anteil zu erraten.

**Offen:** Profilachsen operationalisieren; Beispiele und Gegenbeispiele; Vergleich unterschiedlicher Textsorten; mögliche Verbindung zum epistemischen Linter.

**Wichtiges Dokument:** `Refactoring/13-Epistemische-Textprofile.md`.

---

## 3. Tragender Unterbau

### Differenzfluss-Theorie (DFT)

**Status:** umfangreich ausgearbeitet; theoretischer Kern relativ stabil; wissenschaftlicher Anspruch weiterhin offen

Die DFT bildet den älteren und breiteren Unterbau des Repositories. Der Kern beschreibt Wirklichkeit prozessual über Differenzierung, Kontext, Komposition/Rekursion und Stabilisierung bzw. Ähnlichkeit/Fixpunkte.

Der bestehende Root-`status.md` beschreibt noch einen **Projektstatus 2025**. Er ist als historische Standortbestimmung brauchbar, aber nicht mehr als Status der gesamten heutigen Werkstatt.

Weiter offen bleiben insbesondere formale Strenge, empirische bzw. physikalische Spezifität und die Abgrenzung zwischen produktiver Prozessgrammatik, Metasprache und zu allgemeiner Beschreibung.

### λΔ-Formalismus

**Status:** umfangreiche Vorarbeit; Formalisierung nicht abgeschlossen

λΔ ist als technischer Minimalformalismus für rekursive Differenzierung und Verknüpfung angelegt. Es existieren Bibliotheks-, Kalkül-, Turing-, Physik- und Interpreter-Stränge.

Der Anspruch ist hoch; entsprechend bleibt die entscheidende Arbeit die formale Präzisierung und Belastung gegen bekannte Mathematik, Informatik und Physik.

### DFT Core Seed

**Status:** ausgearbeitet

Der Core Seed versucht, einen minimalen, maschinenlesbaren „genetischen Code“ der DFT mit Invarianten, strukturierter Repräsentation und Proof-of-Life-Tests bereitzustellen.

---

## 4. Größere vorhandene Anwendungsräume

Diese Bereiche sind substanziell vorhanden, stehen aber derzeit nicht im Zentrum der Werkstatt:

| Bereich | derzeitige Einordnung |
|---|---|
| **Denkzeug** | weit ausgearbeiteter Bildungs-/Urteilskraft-Werkzeugkasten für 12–15-Jährige; gute Anschlussstelle für Tutor und Linter |
| **Protokoll3** | DFT als Arbeitsgrammatik für KI-gestützte Strukturdiagnose; möglicher Vorläufer bzw. Nachbar des Refactoring-Strangs |
| **Atlas / Atlas der Anschlussstellen** | Ordnungs- und Anschlusslandkarten für Mechaniken, Konzepte und Disziplinen |
| **Gegenwartsdiagnosen** | eigenständiger großer Ast mit Mechaniken, Feldgrößen, Analysen und Begriffsarbeit |
| **Adapter** | umfangreiche Anschlussarbeit der DFT an Disziplinen, Theorien und Autoren |
| **Wesen / Begriffe / Kommunikation** | Essays und Anwendungen zu Selbstmodell, Begriffen, Kommunikation, Gesellschaft und psychischer Statik |
| **Physik** | spekulative bzw. formale Anschlussversuche; derzeit kein belastbares physikalisches Modell |

Diese Bereiche sollten nicht automatisch als „offene Aufgaben“ behandelt werden. Sie bilden einen Vorrat an Material und Anschlussstellen.

---

## 5. Geparkte oder außerhalb des aktuellen Repository-Bildes liegende Fäden

### YAS / Systemsignale

**Status:** Konzept vorhanden, im untersuchten Repository-Snapshot nicht als eigener Strang auffindbar

Idee: KI-Systeme beobachten zugängliche Daten auf Entwicklungen, Risiken und Chancen und beantworten bzw. pflegen wiederkehrende Fragen wie „Wie entwickeln sich Lebenshaltungskosten?“ oder andere Systemsignale.

**Mögliche neue Verbindung:** Der Forschungsindex und R3/Metarefactoring besitzen strukturelle Nähe dazu: Beide behandeln kontinuierliche Beobachtung, Signale, Relevanz und Wiederaufnahme lohnender Untersuchungen.

### Kommentierte / weiterentwickelte Buchfassungen

Mehrere Buch- und Essaystränge existieren außerhalb des unmittelbaren Werkstattfokus. Sie sind Publikationsobjekte, nicht automatisch Forschungsprioritäten.

### „Eine nüchterne Art von Hoffnung“

**Status:** ausgearbeiteter Essay im Repository.

Strukturelle Kernidee: Handlung kann Möglichkeiten erzeugen, indem zuvor unerreichbare Folgezustände erreichbar werden. Anschluss an den Operator **ERREICHBARKEIT** und an Möglichkeitsräume.

---

## 6. Jüngste übergreifende Funde

### Fund 1 – Epistemische Perspektiven sind konstruierbar

Eine Perspektive muss nicht als diffuse „Haltung“ behandelt werden. Sie kann zumindest teilweise als Komposition expliziter Schnitte und Operatoren rekonstruiert und erzeugt werden.

**Status:** plausibilisiert / experimentell gestützt.

### Fund 2 – Die Frage ist eine Schnittstelle, kein bloßer Suchstring

Die zentrale menschliche Leistung im Umgang mit leistungsfähiger KI verschiebt sich von der vollständigen Durchführung einzelner Denkoperationen zur Spezifikation des Erkenntnisinteresses.

**Status:** ausgearbeitet; empirische Belastung offen.

### Fund 3 – Gute Zerlegung und gute Frage sind dual verwandt

Eine gute Frage legt fest, **bezüglich welcher Leistung** eine Zerlegung relevant ist. Eine gute Zerlegung wiederum zeigt, welche Fragen an einem Gegenstand tragfähig sind.

**Status:** starke Arbeitshypothese.

### Fund 4 – Epistemische Werkzeuge können selbst lernfähig werden

Wenn erfolgreiche und gescheiterte Analysen einschließlich Residuen, Operatoren und Kontext gespeichert werden, kann ein System seinen eigenen Such- und Operatorenraum verbessern.

**Status:** Hypothese / R3-Konzept.

### Fund 5 – Provenienz und Erkenntnisleistung sind verschiedene Achsen

Bei Texten ist die Frage nach dem Erzeugungsprozess logisch von der Frage zu trennen, welche epistemische Leistung der Text selbst erbringt.

**Status:** ausgearbeitet; Operationalisierung offen.

---

### Fund 6 – Explizierbarkeit kann disziplinierend wirken

Explizite epistemische Verfahren können ein KI-System nicht nur **nachträglich prüfbarer** machen. Wenn ein System damit rechnen muss, dass seine Analysewege später rekonstruiert und kritisiert werden können, könnte bereits diese Erwartung sein Verhalten **während** der Analyse verändern.

Damit wäre Explizierbarkeit nicht nur ein Audit-Instrument, sondern möglicherweise selbst ein Steuerungsmechanismus.

**Status:** neue Hypothese; empirisch offen.

## 7. Festlegungen, Arbeitshypothesen und offene Kernfragen

Mehrere zuvor offene Fragen sind inzwischen zu vorläufigen Designentscheidungen oder Arbeitshypothesen geworden.

1. **Operatorenbasis – Festlegung:** Eine gute Operatorenbasis ist nicht notwendig universell. Welche Basis trägt, hängt von Domäne und Aufgabe ab. Der Brillenladen sollte daher nicht auf eine einzige endgültige Minimalbasis verpflichtet werden.

2. **Mehrwert expliziter Verfahren – Arbeitshypothese:** Explizites Refactoring und Brillenkomposition haben spätestens dann einen eigenen Wert, wenn nachvollzogen und überprüft werden soll, **wie** eine Analyse zustande kam. Dieser Wert ist nicht auf bessere Endergebnisse reduziert, sondern umfasst Auditierbarkeit und Rechenschaftsfähigkeit. Daraus folgt die weitergehende Hypothese, dass bereits die Erwartung späterer Prüfung das Verhalten eines KI-Systems disziplinieren könnte.

3. **Epistemische Kosten – Festlegung:** Ein allgemeingültiges epistemisches Budget oder Abbruchkriterium ist nicht zu erwarten. Wie viel Metaanalyse gerechtfertigt ist, hängt vom Gegenstand, vom aktuellen Kontext sowie von Gewicht und Dringlichkeit der Entscheidung ab.

4. **R3 und Historie – Festlegung:** Analysehistorien sind verfügbares Material, keine Norm. Frühere Analysen, Residuen und Entscheidungen dürfen unter neuen Fragestellungen oder Perspektiven erneut herangezogen werden, sollen aber nicht automatisch zu dauerhaft verfestigten Präferenzen werden.

5. **Fragequalität / ModelOfMind – Arbeitshypothese:** Eine Frage wird nicht isoliert interpretiert. Sie fällt auf den bereits vorhandenen Kontext bzw. ein **ModelOfMind des Users** und wird auf diesem Boden wirksam. Die richtige Analyseeinheit ist deshalb nicht nur der Prompttext, sondern **Frage × Nutzerkontext × Situation**.

6. **Linter-Schwelle – Festlegung:** Es wird unterschiedliche Kontexte und entsprechend unterschiedliche Linter-Modi geben müssen. Manche Situationen verlangen minimale Reibung, andere maximale Explizitheit und genaue Prüfung. Ein universeller Eingriffspunkt wäre vermutlich falsch.

7. **Tutor-Diagnose – empirisch offen:** Ob der Tutor tatsächlich ein Lernermodell verbessert oder nur überzeugend darüber spricht, lässt sich voraussichtlich nicht rein konzeptionell entscheiden. Das muss praktisch getestet werden.

8. **Externe Validierung – offen:** Welche Teile sich mit unabhängigen Modellen, Nutzern oder Fachleuten so testen lassen, dass mehr als interne Plausibilität entsteht, bleibt eine zentrale offene Frage.

---

## 8. Nächste sinnvolle Anschlüsse

Diese Punkte sind **keine To-do-Liste**, sondern derzeit besonders ergiebige Anschlussmöglichkeiten:

- Refactoring/Brillenladen adversarial testen: Fälle suchen, in denen die explizite Methode schlechter als eine gute freie Analyse ist.
- E1.2 mit mehreren Modellen sauber als Baseline-vs.-Refactoring-Test durchführen.
- Tutor mit einem kleinen Satz absichtlich unterschiedlicher Fehlmodelle testen.
- Linter an realen Fragen prüfen und Fehlalarme dokumentieren.
- Epistemische Textprofile an kontrastierenden Textpaaren operationalisieren.
- R3 mit dem Forschungsindex verbinden: Funde, Residuen und wiederkehrende offene Fragen könnten als Lernsignale für die Werkstatt dienen.
- Prüfen, ob Brillenladen, Refactoring und Kunst der Frage inzwischen als **ein gemeinsames System mit mehreren Interfaces** beschrieben werden sollten, statt als lose benachbarte Projekte. Diese Prüfung ist ausdrücklich gewünscht und derzeit offen.

---

## 9. Meta-Status der Werkstatt

Das Repository ist inzwischen zu groß und zu verzweigt, um seinen Zustand sinnvoll aus der Ordnerstruktur allein abzulesen. Im untersuchten Snapshot liegen rund **726 Dateien**, davon **703 Markdown-Dateien**.

Die bisherige Projektorganisation ist überwiegend **dokument- und themenorientiert**. Die neue Werkstatt ergänzt sie um eine zweite Ordnung:

```text
Fund
× Begriff
× Zusammenhang
× Dokument
× Status
```

Der entscheidende nächste Organisationsschritt ist daher nicht, alle vorhandenen Dateien neu zu sortieren.

Er besteht darin, eine **laufend rekonstruierbare Sicht auf die Erkenntnislandschaft** zu erhalten.

Dieses Statusdokument ist der erste Versuch einer solchen Sicht.

---

## Pflegehinweis

Bei einer späteren Aktualisierung soll nicht einfach angehängt werden.

Stattdessen jeweils prüfen:

- Was ist neu aktiv geworden?
- Was wurde ausgearbeitet oder getestet?
- Welche offenen Fragen wurden beantwortet oder präzisiert?
- Welche Fäden sind geparkt?
- Welche früher getrennten Stränge haben sich verbunden?
- Welche Einträge sind für die aktuelle Orientierung nicht mehr nötig und können entfernt werden?

**Ziel:** eine kleine, aktuelle Arbeitskarte – nicht ein zweites Archiv.
