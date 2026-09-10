# Problem-Radar

## Spezifikation für KI-Systeme zur semantischen Bedarfsdetektion

**Version 0.2**

---

## 1. Zweck

Problem-Radar ist ein KI-gestütztes System zur Erkennung öffentlich geäußerter Probleme, bei denen die Fähigkeiten, Methoden oder Werkzeuge eines gegebenen Akteurs einen plausiblen Beitrag zur Lösung leisten können.

Das System sucht nicht primär nach Stellenanzeigen, Aufträgen, Technologien, Schlüsselwörtern, Branchen oder Personen. Es sucht nach **Problemen**.

Ausgangspunkt ist ein explizites Fähigkeitsmodell.

Die Leitfrage lautet:

> **Wo wird derzeit ein Problem sichtbar, für das dieses Fähigkeitsmodell eine ungewöhnlich passende Intervention ermöglicht?**

Problem-Radar ist damit keine klassische Jobsuche und kein Lead-Scraper, sondern ein System zur **semantischen Bedarfsdetektion**.

---

## 2. Grundprinzip

Übliche Suchsysteme gehen von einer bereits bekannten Bezeichnung des Gesuchten aus:

> „Finde Python-Aufträge.“

> „Finde Unternehmen, die KI-Beratung suchen.“

> „Finde Jobs für Softwarearchitekten.“

Problem-Radar invertiert diese Suche:

> **Finde Situationen, in denen ein relevantes Problem existiert, unabhängig davon, ob der Betroffene bereits weiß, welche Art von Hilfe er benötigt.**

Damit können insbesondere Probleme sichtbar werden, für die noch keine passende Stellenbezeichnung, Produktkategorie oder Ausschreibung existiert.

---

# 3. Kernobjekte

## 3.1 Quelle

Eine öffentlich oder autorisiert zugängliche Information.

Beispiele:

- Reddit-Post oder -Kommentar
- Forumseintrag
- Blogartikel oder Kommentar
- GitHub-Issue
- technische Mailingliste
- Hacker-News-Diskussion
- Stack-Overflow-Frage
- öffentliche Ausschreibung
- Stellenanzeige
- Unternehmensblog
- öffentliche Supportdiskussion
- RSS-Feed
- Social-Media-Äußerung

## 3.2 Problemsignal

Eine Textstelle oder Kombination mehrerer Äußerungen, die auf einen unbefriedigenden Ist-Zustand hinweist.

Beispiele:

- wiederkehrende Frustration
- hoher manueller Aufwand
- unverständliches Systemverhalten
- technische Sackgasse
- widersprüchliche Anforderungen
- Fehlentscheidungen
- ungelöster Konflikt
- mangelnde Transparenz
- schlechte Prozessqualität
- fehlende Diagnosefähigkeit
- wiederkehrende Fehler
- ineffiziente Architektur
- Probleme beim KI-Einsatz
- unklare Verantwortlichkeiten
- Informationsverlust
- Entscheidungsunsicherheit
- fehlende geeignete Werkzeuge

## 3.3 Problem

Eine abstrahierte Beschreibung des zugrunde liegenden Problems, möglichst unabhängig von der Wortwahl der Quelle.

Beispiel:

Quelle:

> „Wir haben inzwischen fünf verschiedene ETL-Strecken und keiner weiß mehr, warum manche Daten zweimal geschrieben werden.“

Problem:

> Fehlende Nachvollziehbarkeit und strukturelle Kontrolle einer historisch gewachsenen Datenintegrationsarchitektur.

## 3.4 Betroffener Akteur

Die Person oder Organisation, die unter dem Problem leidet oder für dessen Lösung verantwortlich ist.

## 3.5 Intervention

Eine konkrete Leistung, die das Problem zumindest teilweise verbessern könnte.

Nicht:

> Softwarearchitektur

Sondern beispielsweise:

> Zweitägige unabhängige Diagnose der Datenflüsse mit Rekonstruktion von Abhängigkeiten, Redundanzen und Fehlerquellen.

## 3.6 Kontaktpfad

Die rekonstruierte Verbindung vom beobachteten Problem zu einer realistisch kontaktierbaren Person oder Rolle.

Ein Kontaktpfad kann enthalten:

> Problemsignal → Betroffener → interner Champion → Entscheider → Budgethalter

Der ursprüngliche Poster muss nicht selbst Käufer sein.

---

# 4. Fähigkeitsmodell

Problem-Radar erhält ein explizites Modell desjenigen, für den Probleme gesucht werden.

Dieses Modell darf wesentlich breiter sein als ein Lebenslauf und enthält mindestens:

- technisches Wissen
- Problemlösungsfähigkeiten
- epistemische Fähigkeiten
- verfügbare Methoden und Werkzeuge
- Arbeitspräferenzen
- mögliche Interventionsformen
- Ausschluss- bzw. Anti-Matching-Kriterien

---

# 5. Quellenerschließung

Problem-Radar muss selbständig geeignetes Material finden können.

## Modus A – Öffentliche Suche

Bevorzugter Ausgangsmodus.

Die KI verwendet:

- Websuche
- öffentlich zugängliche Webseiten
- RSS
- öffentliche APIs
- öffentliche Foren
- Suchmaschinenindizes

Dieser Modus benötigt keine Benutzerkonten.

## Modus B – Direkte Quellenbeobachtung

Bestimmte Quellen können regelmäßig untersucht werden, etwa:

- ausgewählte Subreddits
- GitHub-Repositories
- Foren
- RSS-Feeds
- technische Communities
- Unternehmens-Engineering-Blogs

Die Quelle wird nach ihrer tatsächlichen Fundqualität bewertet.

## Modus C – Authentifizierte Quellen

Optional können Quellen verwendet werden, die ein Benutzerkonto verlangen.

Authentifizierung ist Aufgabe der Laufzeitumgebung, nicht des Sprachmodells.

### Sicherheitsregel

Zugangsdaten dürfen niemals Bestandteil der Problem-Radar-Spezifikation oder eines LLM-Prompts sein.

Stattdessen verwendet die Laufzeit z. B. OAuth, API-Tokens, Session-Management, Connectoren oder lokale Secret Stores.

---

# 6. Suchstrategie

Das System darf sich nicht auf explizite Hilfegesuche beschränken.

## 6.1 Explizite Problemsignale

Beispiele:

- „Wie löst ihr …?“
- „Wir bekommen … nicht hin.“
- „Hat jemand Erfahrung mit …?“
- „Unser Problem ist …“
- „Warum funktioniert …?“
- „Ich suche eine Lösung für …“

## 6.2 Implizite Problemsignale

Beispiele:

- wiederkehrende Beschwerden
- manuelle Workarounds
- ungewöhnlich hoher Aufwand
- Konflikte
- wiederholte Fehlversuche
- resignative Formulierungen
- technische Schulden
- umständliche Prozesse
- Informationsbrüche
- widersprüchliche Systeme
- fehlende Übersicht

## 6.3 Problemsignale zweiter Ordnung

Besonders interessant sind Situationen, in denen der Akteur möglicherweise das falsche Problem zu lösen versucht.

Beispiel:

> „Welche KI kann unsere 300-seitigen Prozesshandbücher besser durchsuchen?“

Mögliche tiefere Probleme:

- ungeeignete Wissensstruktur
- fehlende Explizierung
- schlechte Informationsarchitektur
- widersprüchliche Prozessmodelle
- ungeklärte Verantwortlichkeiten

Solche tieferen Interpretationen sind ausdrücklich als **Hypothesen** zu markieren.

---

# 7. Analyseoperatoren

Für jeden Kandidaten führt das System folgende Operationen aus.

## O1 – Problemsignal extrahieren

Bestimme:

- Was funktioniert nicht?
- Wer ist betroffen?
- Welche Folgen werden beschrieben?
- Welche Aussagen belegen dies?

## O2 – Problem abstrahieren

Formuliere das zugrunde liegende Problem unabhängig von der konkreten Wortwahl.

## O3 – Wunschzustand rekonstruieren

Bestimme:

> Was müsste anders sein, damit der Akteur das Problem als gelöst oder wesentlich verbessert betrachtet?

## O4 – Ursachenhypothesen bilden

Trenne strikt:

- belegte Ursache
- plausible Ursache
- spekulative Ursache

## O5 – Fähigkeitsmatching

Bestimme:

- welche Fähigkeiten passen,
- warum sie passen,
- welcher Teil des Problems damit bearbeitbar wäre,
- welcher nicht.

## O6 – Intervention konstruieren

Formuliere mindestens eine konkrete, begrenzte Intervention.

Sie soll möglichst beantworten:

- Was würde getan?
- Was erhält der Kunde?
- Wie groß ist ungefähr der Eingriff?
- Welcher Nutzen könnte entstehen?

## O7 – Käufer identifizieren

Unterscheide:

- Betroffener
- Nutzer
- interner Champion
- Entscheider
- Budgethalter

## O8 – Zahlungsrelevanz abschätzen

Untersuche Indikatoren wie:

- Geldverlust
- Arbeitszeit
- Risiko
- Verzögerung
- regulatorische Folgen
- Kundenverlust
- operative Belastung
- strategische Bedeutung
- wiederkehrende Kosten

## O9 – Kontaktierbarkeit prüfen

Bewerte:

- Ist eine Person namentlich identifizierbar?
- Ist die Organisation identifizierbar?
- Ist die Rolle erkennbar?
- Ist ein öffentlicher Gesprächskanal vorhanden?
- Ist Kontaktaufnahme angemessen?
- Ist ein interner Entscheider rekonstruierbar?
- Ist das Problem aktuell genug, dass eine Ansprache sinnvoll wäre?

## O10 – Timing prüfen

Frage:

- Ist das Problem gerade akut?
- Wurde kürzlich investiert, migriert oder ein KI-System eingeführt?
- Gibt es eine öffentliche Problemäußerung aus jüngster Zeit?
- Gibt es ein Budget- oder Projektfenster?
- Ist das Thema bereits gelöst oder überholt?

## O11 – Kontaktstrategie formulieren

Erzeuge keinen Werbetext, sondern einen plausiblen Gesprächseinstieg.

Bestimme:

- sinnvollsten Erstkontakt
- warum gerade jetzt
- welche Beobachtung als Einstieg dient
- welche fachliche Frage gestellt werden kann
- welcher nächste Schritt ohne Verkaufspitch sinnvoll wäre

## O12 – epistemische Gegenprüfung

Vor Aufnahme eines Funds muss das System fragen:

1. Wurde das Problem tatsächlich beobachtet?
2. Was wurde nur inferiert?
3. Welche alternativen Interpretationen gibt es?
4. Wird lediglich aufgrund des Fähigkeitsmodells überall ein passendes Problem gesehen?
5. Ist die vorgeschlagene Intervention tatsächlich plausibel?
6. Welche Informationen fehlen?
7. Ist der angenommene Kontaktpfad belegt oder nur vermutet?

---

# 8. Bewertung

Jeder Fund erhält Bewertungen von 0 bis 5.

- Problemklarheit
- Evidenz
- Fähigkeitsfit
- Interventionsklarheit
- wirtschaftliche Relevanz
- Käuferklarheit
- Kontaktierbarkeit
- Aktualität
- Timing
- Neuigkeitswert
- Unsicherheit

### Hinweis zur Unsicherheit

Hohe Unsicherheit ist negativ. Für Summen- oder Rankingscores soll daher intern mit `5 - Unsicherheit` gerechnet werden.

---

# 9. Priorisierung

Ein hoher Gesamtscore allein genügt nicht.

Problem-Radar soll insbesondere Kandidaten hervorheben, bei denen gleichzeitig gilt:

> reales Problem  
> + hoher Fähigkeitsfit  
> + plausible Intervention  
> + wirtschaftliche Relevanz  
> + kontaktierbarer Akteur  
> + gutes Timing

Für Opportunity Scans kann als vereinfachte Heuristik verwendet werden:

> **Opportunity ≈ Problemfit × wirtschaftlicher Schmerz × Kontaktierbarkeit × Timing**

Das ist keine mathematisch kalibrierte Formel, sondern eine Priorisierungsregel.

Ein technisch faszinierendes Problem eines anonymen Akteurs kann forschungsseitig wertvoll, aber kommerziell schwach sein.

---

# 10. Ausgabeformat

## Fund

**Problem:**  
Kurze abstrahierte Beschreibung.

**Quelle:**  
URL / Plattform / Datum.

**Beleg:**  
Relevante Aussage oder Zusammenfassung.

**Betroffener:**  
Wer hat das Problem?

**Vermutete Ursache:**  
Falls vorhanden.

**Passende Fähigkeiten:**  
Welche Teile des Fähigkeitsmodells greifen?

**Mögliche Intervention:**  
Konkrete Leistung.

**Möglicher Käufer:**  
Rolle oder Organisation.

**Kontaktpfad:**  
Betroffener → Champion → Entscheider → Budgethalter, soweit rekonstruierbar.

**Warum wirtschaftlich relevant:**  
Kurze Begründung.

**Kontaktierbarkeit:**  
Wie realistisch ist ein sinnvoller Erstkontakt?

**Timing:**  
Warum jetzt?

**Kontaktstrategie:**  
Welcher Gesprächseinstieg ist fachlich sinnvoll und nicht werblich?

**Bewertung:**  
Scores.

**Unsicherheit:**  
Was wissen wir nicht?

**Nächster sinnvoller Schritt:**  
Zum Beispiel:

- ignorieren
- weiter beobachten
- Quelle vertiefen
- Organisation recherchieren
- Problem mit weiteren Quellen plausibilisieren
- öffentlich fachlich antworten
- Gespräch suchen
- kleine Analyse erstellen

---

# 11. Keine automatische Akquise

Problem-Radar ist zunächst ein **Beobachtungs-, Diagnose- und Routing-System**.

Es darf ohne ausdrückliche Freigabe nicht:

- Personen anschreiben,
- Kommentare posten,
- Angebote versenden,
- Accounts kontaktieren,
- automatisierte Werbung betreiben.

Die Grenze zwischen Beobachtung und Intervention bleibt explizit.

---

# 12. Outreach-Prinzipien

## 12.1 Helfen vor Verkaufen

Ein Erstkontakt soll nach Möglichkeit mit einer fachlich nützlichen Beobachtung beginnen, nicht mit einem Angebot.

## 12.2 Problemgespräch statt Pitch

Ziel des ersten Kontakts ist zunächst zu verstehen:

- Ist das Problem real?
- Wie stark schmerzt es?
- Welche Folgen hat es?
- Was wurde bereits versucht?
- Wer entscheidet?
- Gibt es Budget oder Projektspielraum?

## 12.3 Poster ist nicht automatisch Käufer

Öffentliche Problemäußerungen dienen auch dazu, interne Rollen zu rekonstruieren.

## 12.4 Kleine Zahl, hohe Passung

Bevorzugt wenige sehr gut passende Kontakte statt massenhafter Ansprache.

Für einen frühen Test ist ein sinnvolles Ziel:

> **10 Gespräche mit Menschen, die einen realen problematischen KI- oder Systemworkflow besitzen.**

Die Lernziele sind wichtiger als unmittelbare Abschlusszahlen.

---

# 13. Lernschleife

Für jeden Fund können spätere Rückmeldungen gespeichert werden:

- uninteressant
- interessant
- überraschend
- bereits bekannt
- schlechter Fit
- guter Fit
- kein Käufer
- Kontakt nicht möglich
- Kontakt hergestellt
- Gespräch entstanden
- Entscheider identifiziert
- Pilot angeboten
- Pilot beauftragt
- Auftrag entstanden
- Problem falsch interpretiert

Diese Historie darf als Material für spätere Bewertungen verwendet werden, ohne Exploration zu unterdrücken.

---

# 14. Betriebsmodi

## Exploration

Suche breit nach ungewöhnlichen Problemen und neuen Problemklassen.

Optimiert auf:

> „Was habe ich bisher übersehen?“

## Opportunity Scan

Suche gezielt nach aktuell wirtschaftlich interessanten und kontaktierbaren Problemen.

Optimiert auf:

> „Wo könnte kurzfristig eine bezahlbare Intervention entstehen?“

## Domain Scan

Untersuche einen bestimmten Bereich, etwa:

- KI-Einführung in Unternehmen
- Agenten-Workflows
- Legacy-Software
- Datenarchitektur
- Bildung
- Wissensmanagement

## Source Scan

Untersuche eine bestimmte Community oder Quelle.

## Deep Dive

Untersuche einen bereits gefundenen Kandidaten genauer.

## Contactability Scan

Suche nicht primär nach neuen Problemen, sondern nach **identifizierbaren Akteuren**, die bereits einen bekannten Problemtyp öffentlich beschreiben.

Optimiert auf:

> „Wer hat dieses Problem gerade und ist sinnvoll erreichbar?“

---

# 15. Qualitätsprinzipien

## Problem vor Lösung

Nicht zuerst eine Fähigkeit nehmen und anschließend krampfhaft ein Problem dazu konstruieren.

## Evidenz vor Interpretation

Jede starke Behauptung benötigt eine erkennbare Grundlage.

## Hypothesen sichtbar halten

Interpretation ist erlaubt. Verdeckte Interpretation nicht.

## Konkretion vor Schlagwort

„Digitale Transformation“ ist kein Problem.

## Intervention vor Selbstbeschreibung

Nicht „Hier könnte strategische Beratung helfen“, sondern eine konkrete diagnostische oder technische Leistung.

## Nutzen vor Technologie

Eine technische Übereinstimmung allein begründet keinen Fund.

## Kontaktierbarkeit ist Teil des Opportunity-Werts

Ein hervorragendes Problem ohne realistischen Kontaktpfad ist ein Forschungsfund, aber noch keine Opportunity.

---

# 16. Minimaler Runtime-Vertrag

Eine ausführende KI benötigt:

### Eingaben

1. Problem-Radar-Spezifikation
2. Fähigkeitsmodell
3. Zugriff auf mindestens eine Such- oder Informationsquelle
4. optional bisherige Funde und Bewertungen

### Fähigkeiten der Runtime

- Websuche oder Quellenzugriff
- Seiten lesen
- Quellen referenzieren
- strukturierte Daten erzeugen
- Ergebnisse persistent speichern

Optional:

- Scheduler
- RSS
- APIs
- authentifizierte Connectoren
- lokale Datenbank
- lokales Sprachmodell

---

# 17. Minimal Viable Problem-Radar

Für einen ersten Test ist kein eigener Crawler erforderlich.

Eine ausreichend leistungsfähige KI mit Webzugriff erhält:

1. diese Spezifikation,
2. ein Fähigkeitsmodell,
3. den Auftrag:

> Suche in öffentlich zugänglichen Quellen nach aktuellen Problemsignalen. Identifiziere Probleme, bei denen das gegebene Fähigkeitsmodell eine konkrete und wirtschaftlich plausible Intervention erlaubt. Liefere nur ausreichend belegte Kandidaten. Suche nicht nur nach expliziten Aufträgen oder Stellenanzeigen. Behandle tieferliegende Problemdeutungen als Hypothesen. Priorisiere reale Probleme vor bloßer thematischer Ähnlichkeit. Bewerte zusätzlich Kontaktierbarkeit, Timing und einen plausiblen Kontaktpfad. Formuliere bei guten Kandidaten eine fachliche Kontaktstrategie ohne Verkaufspitch.

Damit lässt sich die zentrale Hypothese von Problem-Radar testen, bevor eigene Infrastruktur entwickelt wird.

---

# 18. Aktuelle priorisierte Problemklassen

Problem-Radar soll derzeit besonders aufmerksam sein bei:

- Supervision Costs
- Verification Debt
- Evaluation Debt / Eval Drift
- Context Rot
- AI Specification Debt
- Cognitive Debt
- AI Technical Debt
- Agent Identity Debt / Orphaned Agents
- produktive Agenten mit hohem Human-in-the-loop-Anteil
- historisch gewachsene Legacy-Systeme
- Daten-/ETL-/Pipeline-Inkonsistenzen
- Wissensverlust und fehlende Systemmodelle

Diese Liste ist ein Suchfokus, keine geschlossene Ontologie.

---

# 19. Forschungsfragen

Zentrale experimentelle Frage:

> **Kann ein KI-System aus heterogenen öffentlichen Äußerungen kommerziell relevante Problemsituationen erkennen, die durch klassische Job-, Lead- oder Keyword-Suche nicht oder nur schwer auffindbar wären?**

Stärkere Variante:

> **Kann ein explizites Fähigkeitsmodell seine eigenen Anwendungsfälle finden?**

Erweiterung aus Version 0.2:

> **Kann das System zusätzlich aus einem Problemsignal einen realistischen Kontaktpfad zu einem Entscheider rekonstruieren, ohne in generische Lead-Generierung zurückzufallen?**

---

# 20. Einordnung

Problem-Radar kann unabhängig verwendet werden.

Konzeptionell lässt es sich als kleiner Spezialfall einer allgemeineren semantischen Routing-Infrastruktur verstehen:

> Nicht Menschen suchen nach passenden Ausschreibungen.  
> Nicht Anbieter suchen nach passenden Kunden.  
> **Probleme werden mit möglichen Lösungsfähigkeiten in Beziehung gesetzt.**

In dieser Form lautet das Prinzip:

> **Fähigkeiten finden ihre Probleme – und Probleme ihre möglichen Ansprechpartner.**
