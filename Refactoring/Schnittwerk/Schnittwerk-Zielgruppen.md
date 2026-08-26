# Schnittwerk – Zielgruppen

## Wer welchen Teil der Architektur wofür braucht

**Status:** Arbeitsfassung 0.1  
**Funktion:** Metadokument zu Zielgruppen, Nutzungskontexten und Einstiegspunkten

---

## 1. Zweck

Schnittwerk ist keine Anwendung für eine einzige Nutzergruppe.

Es ist eine epistemische Architektur, deren verschiedene Teile in unterschiedlichen Kontexten nützlich werden können.

Deshalb ist die zentrale Frage nicht:

> **Wer ist die Zielgruppe des Schnittwerks?**

Sondern:

> **Wer braucht welchen Teil des Schnittwerks für welche Aufgabe?**

Nicht jeder Nutzer muss den gesamten epistemischen Maschinenraum verstehen oder bedienen.

Im Gegenteil:

> **Eine gute Architektur darf im Inneren komplex sein und nach außen kleine, passende Interfaces anbieten.**

Dieses Dokument ordnet Zielgruppen deshalb funktional nach:

- typischem Problem,
- gewünschtem Nutzen,
- sinnvollem Einstiegspunkt,
- relevanten Schnittwerk-Komponenten,
- notwendigem Vorwissen,
- möglichen Hürden.

---

## 2. Vier grundlegende Rollen

Berufsgruppen allein reichen zur Einordnung nicht aus.

Dieselbe Person kann Schnittwerk in unterschiedlichen Rollen verwenden.

### 2.1 Nutzer

Der Nutzer will mit Hilfe des Schnittwerks **besser erkennen, fragen, prüfen oder entscheiden**.

Er braucht meist keinen vollständigen Zugriff auf die Architektur.

Typische Interfaces:

- Kunst der Frage,
- Linter,
- ausgewählte Brillen,
- einfache Audit-Ausgaben.

### 2.2 Entwickler

Der Entwickler baut auf Schnittwerk auf.

Er interessiert sich für:

- Schnittwerk-Spezifikationen,
- Operatoren und Dimensionen,
- lokale Basen,
- ModelOfMind,
- Refactoring,
- Betriebsmodi,
- Agenten- und Tutorarchitekturen,
- Auditierbarkeit.

### 2.3 Prüfer

Der Prüfer möchte nachvollziehen:

- wie ein Problemraum konstruiert wurde,
- welche Annahmen tragend waren,
- welche Alternativen ausgeschlossen wurden,
- welche Perspektiven oder Systemgrenzen gewählt wurden,
- welches Residuum verbleibt.

Für ihn ist vor allem das Audit- und Rekonstruktions-Interface relevant.

### 2.4 Forscher

Der Forscher untersucht das Schnittwerk selbst.

Er fragt beispielsweise:

- Welche Komponenten erzeugen messbaren Mehrwert?
- Welche Begriffe sind redundant?
- Welche lokalen Operatorenbasen funktionieren?
- Wie stabil sind epistemische Signaturen?
- Welche Teile besitzen bekannte Vorläufer?
- Welche Audit- oder Tutorhypothesen lassen sich empirisch testen?

Diese Rolle benötigt den tiefsten Zugriff auf Architektur, Einordnung und Testdesign.

---

## 3. Zielgruppe: normale KI-Anwender

### Typisches Problem

Eine KI beantwortet eine schlecht geschnittene Frage sehr überzeugend.

Oder:

- der Nutzer weiß nicht, wie er eine komplexe Frage formulieren soll,
- wichtige Perspektiven fehlen,
- die Antwort wirkt plausibel, aber ihre Voraussetzungen sind unklar,
- das Gespräch läuft in einem schlechten Frame weiter.

### Nutzen

Schnittwerk kann helfen:

- bessere Fragen zu formulieren,
- relevante Alternativschnitte sichtbar zu machen,
- Blindstellen zu erkennen,
- die aktuelle Fragestellung zu refactorieren,
- Anschlussfragen zu finden.

### Einstiegspunkt

**Kunst der Frage**

Optional:

**Epistemischer Linter**

### Relevante Komponenten

- Kontext / ModelOfMind
- Kunst der Frage
- epistemischer Auftrag
- einfache Refactoring-Operationen
- Selektion / Exklusion / Residuum

### Vorwissen

Keines notwendig.

### Hürde

Metaanalyse darf nicht mehr Aufwand erzeugen als die eigentliche Aufgabe.

Für diese Zielgruppe muss Schnittwerk daher weitgehend **unsichtbar funktionieren**.

---

## 4. Zielgruppe: Wissensarbeiter und Analysten

Dazu gehören beispielsweise:

- Berater,
- Analysten,
- Journalisten,
- Strategen,
- Forscher,
- Juristen,
- Produkt- und Organisationsentwickler.

### Typisches Problem

Komplexe Sachverhalte werden unter Zeitdruck analysiert.

Dabei besteht das Risiko:

- falscher Systemgrenzen,
- vermischter Kategorien,
- unklarer Kausalmodelle,
- übersehener Gegenperspektiven,
- vorschneller Abstraktion,
- impliziter Gewichtungen.

### Nutzen

Schnittwerk kann Analyseprozesse strukturieren und prüfbarer machen.

Besonders relevant sind:

- Perspektivwechsel,
- Systemgrenzen,
- Zeit- und Skalenwechsel,
- Alternativmodelle,
- Residuen,
- Audit.

### Einstiegspunkt

**Epistemisches Refactoring**

### Relevante Komponenten

- R1 / R2 / R3
- Brillenladen
- Audit
- epistemische Signaturen
- Budgetsteuerung

### Vorwissen

Grundverständnis analytischer Arbeit.

### Hürde

Schnittwerk muss zeigen, dass es nicht nur zusätzliche Terminologie erzeugt, sondern tatsächlich bessere oder schneller prüfbare Analysen ermöglicht.

---

## 5. Zielgruppe: Philosophen und Erkenntnistheoretiker

### Typisches Interesse

Nicht primär Anwendung, sondern Begriffs- und Architekturfragen:

- Wie werden Problemräume konstruiert?
- Was ist ein epistemischer Schnitt?
- Wie hängen Perspektive, Abstraktion und Relevanz zusammen?
- Was bedeutet es, Erkenntnisprozesse zu refactorieren?
- Wie verhalten sich Schnittwerk-Begriffe zu bestehenden erkenntnistheoretischen Ansätzen?

### Nutzen

Schnittwerk bietet einen konstruktiven, operationalisierbaren Zugriff auf Fragen, die sonst häufig getrennt behandelt werden.

### Einstiegspunkt

**Architekturdokument**

Danach:

**Einordnung und Abgrenzung**

### Relevante Komponenten

- Problemraumkonstruktion
- relevante Leistung
- Perspektivität
- Operator / Dimension
- lokale Basen
- epistemische Signaturen
- Audit
- Rekursion

### Vorwissen

Philosophisches oder erkenntnistheoretisches Grundverständnis hilfreich, aber nicht zwingend.

### Hürde

Die Sprache darf nicht so technisch werden, dass philosophische Anschlussfähigkeit verloren geht.

Zugleich müssen Begriffe präzise genug sein, um mehr als Metaphern zu bleiben.

---

## 6. Zielgruppe: KI-Forscher und AI-Alignment / Safety

### Typisches Problem

KI-Systeme erzeugen leistungsfähige Antworten, deren epistemische Struktur oft implizit bleibt.

Relevant sind Fragen wie:

- Wie lässt sich Problem Framing explizieren?
- Wie können Analysewege geprüft werden?
- Welche Nutzerkontexte beeinflussen die Interpretation einer Anfrage?
- Wie lassen sich Alternativschnitte oder Gegenmodelle systematisch erzeugen?
- Welche Rolle kann Auditierbarkeit spielen?

### Nutzen

Schnittwerk kann als Versuch einer expliziten epistemischen Steuerungs- und Auditschicht interessant sein.

### Einstiegspunkt

**Architektur + Audit**

### Relevante Komponenten

- ModelOfMind
- epistemischer Auftrag
- Operatoren- und Dimensionsraum
- Signaturrekonstruktion
- Process / Audit Layer
- ex-ante Disziplinierungshypothese

### Vorwissen

KI-/LLM-Grundverständnis.

### Hürde

Schnittwerk darf Auditierbarkeit nicht mit vollständiger innerer Transparenz oder kausaler Faithfulness verwechseln.

Der Mehrwert gegenüber starkem implizitem LLM-Reasoning muss empirisch gezeigt werden.

---

## 7. Zielgruppe: Entwickler von KI-Anwendungen

### Typisches Problem

Eine Anwendung benötigt mehr als generische Prompt-Templates.

Beispiele:

- Tutor,
- Rechercheagent,
- Analyseagent,
- Linter,
- Disput-Refactoring,
- Entscheidungsunterstützung,
- Multi-Agenten-System.

### Nutzen

Schnittwerk kann eine gemeinsame epistemische Infrastruktur liefern.

Statt jede Anwendung isoliert zu prompten, können wiederverwendbare Schichten definiert werden:

- Kontextmodell,
- Erkenntnisauftrag,
- Refactoring,
- Perspektiven,
- Audit,
- Modi und Budgets.

### Einstiegspunkt

**Minimaler Betriebsmodus**

### Relevante Komponenten

- Schnittwerk-Spezifikation
- ModelOfMind
- lokale Basen
- Agentenrollen
- Brillen
- Audit
- Budgetsteuerung

### Vorwissen

Software- oder KI-Entwicklung.

### Hürde

Die Architektur muss praktisch genug sein, um implementierbar zu bleiben.

Ein zu großer Metarahmen würde denselben Fehler erzeugen, den Schnittwerk eigentlich vermeiden will.

---

## 8. Zielgruppe: Pädagogen und Lernsystem-Entwickler

### Typisches Problem

Ein KI-Tutor kann überzeugend erklären, ohne zu wissen, was der Lernende tatsächlich verstanden hat.

Außerdem kann zu viel Hilfe den Lernprozess schwächen.

### Nutzen

Schnittwerk kann helfen:

- Lernermodelle zu prüfen,
- Fragen diagnostisch einzusetzen,
- Fehlkonzepte zu unterscheiden,
- Schwierigkeits- und Hilfsgrade anzupassen,
- unterschiedliche Linter- oder Tutor-Modi zu definieren.

### Einstiegspunkt

**Epistemisch diagnostischer Tutor**

### Relevante Komponenten

- ModelOfMind / Lernermodell
- Kunst der Frage
- diagnostische Fragen
- Linter-Modi
- epistemisches Budget
- Audit des Lernprozesses

### Vorwissen

Pädagogisches oder didaktisches Verständnis hilfreich.

### Hürde

Ein gutes Lernermodell darf nicht nur plausibel klingen.

Es muss empirisch zeigen, dass es Lernfortschritt tatsächlich besser diagnostiziert oder unterstützt.

---

## 9. Zielgruppe: Moderatoren, Mediatoren und Konfliktbearbeitung

### Typisches Problem

Konflikte erscheinen als Sachwiderspruch, beruhen aber teilweise auf unterschiedlichen:

- Begriffen,
- Perspektiven,
- Systemgrenzen,
- Zeithorizonten,
- Skalen,
- Evidenzannahmen,
- Zielgrößen.

### Nutzen

**Disput-Refactoring** kann helfen, solche Differenzen auseinanderzulegen.

### Einstiegspunkt

**Disput-Refactoring**

### Relevante Komponenten

- relevante Leistung
- Perspektive
- Systemgrenze
- Begriffe
- Zeit / Skala
- Kausalmodell
- Selektion / Exklusion
- Audit

### Vorwissen

Keines zwingend.

### Hürde

Das Verfahren darf nicht suggerieren, jeder Konflikt sei bloß ein Missverständnis.

Manche Konflikte beruhen auf echten Interessen-, Wert- oder Machtgegensätzen.

---

## 10. Zielgruppe: Organisationen und Systemberatung

### Typisches Problem

Organisationen arbeiten häufig mit impliziten Problemdefinitionen und historisch gewachsenen Kategorien.

Dadurch können:

- lokale Optimierungen,
- falsche Systemgrenzen,
- Zielkonflikte,
- blinde Flecken,
- strukturelle Fehlanreize

unsichtbar bleiben.

### Nutzen

Schnittwerk kann als strukturierte Methode für Problemraum- und Boundary-Refactoring dienen.

### Einstiegspunkt

**Refactoring + Brillenladen**

### Relevante Komponenten

- Systemgrenzen
- Akteure
- Leistungen
- Zeithorizonte
- Rückkopplungen
- Perspektiven
- Audit

### Vorwissen

Systemisches oder organisatorisches Denken hilfreich.

### Hürde

Die Analyse darf nicht zu einem abstrakten Meta-Workshop ohne operative Konsequenz werden.

---

## 11. Zielgruppe: Autoren, Leser und Medienanalyse

### Typisches Problem

Texte werden häufig pauschal nach:

- Stil,
- politischer Zuordnung,
- vermeintlicher KI-Herkunft,
- rhetorischem Eindruck

bewertet.

Dabei bleibt unklar, welche epistemische Leistung ein Text tatsächlich erbringt.

### Nutzen

**Epistemische Textprofile** können Texte differenzierter beschreiben.

Mögliche Dimensionen:

- Evidenz,
- Argumentation,
- Perspektive,
- Abstraktion,
- Unsicherheit,
- Prüfbarkeit,
- Blindstellen.

### Einstiegspunkt

**Epistemisches Textprofil**

### Relevante Komponenten

- inverse Faktorisierung
- Signaturrekonstruktion
- Selektion / Exklusion / Residuum
- Linter

### Vorwissen

Keines zwingend.

### Hürde

Das Profil darf nicht selbst zu einem scheinobjektiven Bewertungsscore werden.

Es beschreibt eine epistemische Struktur, nicht automatisch die Qualität oder Wahrheit des Textes.

---

## 12. Zielgruppe: Forscher, die Schnittwerk selbst untersuchen

### Typisches Problem

Schnittwerk ist bislang ein Arbeitsmodell.

Mehrere zentrale Claims sind plausibel, aber noch nicht ausreichend empirisch geprüft.

### Forschungsfragen

- Wann verbessert explizites Refactoring die Analyse?
- Wann erzeugt es nur Overhead?
- Wie zuverlässig sind Signaturrekonstruktionen?
- Welche lokalen Basen entstehen in verschiedenen Domänen?
- Wie stark hängt die Analyse vom ModelOfMind ab?
- Verbessert Auditierbarkeit die ex-ante Analysequalität?
- Welche Anwendungen profitieren am stärksten?

### Einstiegspunkt

**Architektur + Einordnung + Testfälle**

### Relevante Komponenten

Alle.

### Hürde

Interne Plausibilität ist kein Ersatz für externe Validierung.

---

## 13. Zielgruppen nach benötigter Tiefe

Nicht jede Zielgruppe braucht dieselbe Darstellungstiefe.

### Ebene A – Unsichtbar

Der Nutzer formuliert normale Fragen.

Schnittwerk wirkt intern.

Geeignet für:

- normale KI-Anwender,
- Lernende,
- gelegentliche Nutzer.

### Ebene B – Sichtbare Hilfen

Das System zeigt:

- bessere Fragen,
- Blindstellen,
- Alternativperspektiven,
- offene Residuen.

Geeignet für:

- Wissensarbeiter,
- Pädagogen,
- Moderatoren,
- Autoren.

### Ebene C – Explizites Experteninterface

Operatoren, Dimensionen, Brillen und Budgets werden gezielt gewählt.

Geeignet für:

- Analysten,
- Entwickler,
- Forscher,
- Systemberater.

### Ebene D – Audit und Forschung

Epistemische Signaturen, Analysewege und Varianten werden rekonstruiert und verglichen.

Geeignet für:

- Prüfer,
- KI-Forscher,
- Safety-/Alignment-Forschung,
- wissenschaftliche Evaluation.

---

## 14. Was keine Zielgruppe braucht

Schnittwerk sollte nicht voraussetzen, dass Nutzer:

- neue Terminologie lernen,
- philosophische Literatur kennen,
- Operatorenlisten auswendig beherrschen,
- jeden Analyseweg explizit sehen,
- oder ständig Metareflexion betreiben.

Wenn ein Nutzer eine einfache Frage stellt und eine einfache Antwort genügt, sollte Schnittwerk keinen epistemischen Maschinenraum aufklappen.

Ein zentrales Designprinzip lautet daher:

> **So viel Explizierung wie nötig, so wenig wie möglich.**

---

## 15. Prioritäre Zielgruppen für frühe Tests

Für erste praktische Tests erscheinen besonders geeignet:

### 1. KI-Anwender mit komplexen Fragen

Test:

Verbessert Schnittwerk die Formulierung und Qualität des Problemraums?

### 2. Wissensarbeiter / Analysten

Test:

Werden Blindstellen, Alternativschnitte und Abhängigkeiten besser sichtbar?

### 3. Pädagogische Anwendungen

Test:

Verbessert ein diagnostischer Tutor tatsächlich sein Lernermodell?

### 4. KI-Audit und Forschung

Test:

Lassen sich epistemische Signaturen reproduzierbar rekonstruieren?

### 5. Disput-Refactoring

Test:

Kann Schnittwerk echte Sachkonflikte von Perspektiv-, Begriffs- oder Grenzkonflikten unterscheiden?

Diese Gruppen eignen sich nicht deshalb, weil sie die größten Märkte wären.

Sie eignen sich, weil sie unterschiedliche Teile der Architektur unter Belastung setzen.

---

## 16. Kurzmatrix

| Zielgruppe | Problem | Einstieg | Tiefe |
|---|---|---|---|
| KI-Anwender | schlechte oder zu enge Fragen | Kunst der Frage | niedrig |
| Wissensarbeiter | komplexe Problemräume | Refactoring | mittel |
| Philosophen | Architektur und Begriffe | Architektur / Einordnung | hoch |
| KI-Forscher | Framing, Audit, ModelOfMind | Architektur / Audit | hoch |
| KI-Entwickler | wiederverwendbare epistemische Logik | Betriebsmodus | hoch |
| Pädagogen | Lernermodell und Diagnose | Tutor | mittel |
| Moderation / Konflikt | unterschiedliche Schnitte | Disput-Refactoring | mittel |
| Organisationen | Grenzen, Ziele, Blindstellen | Refactoring / Brillenladen | mittel bis hoch |
| Autoren / Medienanalyse | epistemische Textstruktur | Textprofile | mittel |
| Schnittwerk-Forschung | Validierung der Architektur | gesamtes System | sehr hoch |

---

## 17. Fazit

Schnittwerk besitzt nicht eine Zielgruppe.

Es besitzt einen **gemeinsamen epistemischen Maschinenraum mit mehreren Interfaces**.

Für den normalen Nutzer kann davon fast alles unsichtbar bleiben.

Für den Entwickler wird die Architektur selbst zum Werkzeug.

Für den Prüfer wird sie zur Audit-Sprache.

Für den Forscher wird sie zum Untersuchungsgegenstand.

Die wichtigste Zielgruppenfrage lautet deshalb:

> **Welche epistemische Leistung wird in diesem Kontext gebraucht – und wie wenig Schnittwerk muss dafür sichtbar werden?**

Das ist zugleich eine Designregel:

> **Nicht jeder braucht das ganze Schnittwerk.  
> Jeder sollte nur den Teil sehen, der seine Erkenntnisarbeit tatsächlich verbessert.**
