# Problem-Radar

## Spezifikation für KI-Systeme zur semantischen Bedarfsdetektion

**Version 0.1**

---

## 1. Zweck

Problem-Radar ist ein KI-gestütztes System zur Erkennung öffentlich geäußerter Probleme, bei denen die Fähigkeiten, Methoden oder Werkzeuge eines gegebenen Akteurs einen plausiblen Beitrag zur Lösung leisten können.

Das System sucht nicht primär nach:

- Stellenanzeigen,
- Aufträgen,
- bestimmten Technologien,
- Schlüsselwörtern,
- Branchen,
- Personen oder Unternehmen.

Es sucht nach **Problemen**.

Ausgangspunkt ist ein explizites Fähigkeitsmodell.

Die Leitfrage lautet:

> **Wo wird derzeit ein Problem sichtbar, für das dieses Fähigkeitsmodell eine ungewöhnlich passende Intervention ermöglicht?**

Problem-Radar ist damit keine klassische Jobsuche und kein Lead-Scraper.

Es ist ein System zur **semantischen Bedarfsdetektion**.

---

# 2. Grundprinzip

Übliche Suchsysteme gehen von einer bereits bekannten Bezeichnung des Gesuchten aus:

> „Finde Python-Aufträge.“

> „Finde Unternehmen, die KI-Beratung suchen.“

> „Finde Jobs für Softwarearchitekten.“

Problem-Radar invertiert diese Suche:

> **Finde Situationen, in denen ein relevantes Problem existiert, unabhängig davon, ob der Betroffene bereits weiß, welche Art von Hilfe er benötigt.**

Damit können insbesondere Probleme sichtbar werden, für die noch keine passende Stellenbezeichnung, Produktkategorie oder Ausschreibung existiert.

---

# 3. Kernobjekte

Das System unterscheidet mindestens folgende Objekte:

## 3.1 Quelle

Eine öffentlich oder autorisiert zugängliche Information.

Beispiele:

- Reddit-Post
- Reddit-Kommentar
- Forumseintrag
- Blogartikel
- Kommentar unter einem Artikel
- GitHub-Issue
- öffentliche Diskussion
- technische Mailingliste
- Hacker-News-Diskussion
- Stack-Overflow-Frage
- öffentliche Ausschreibung
- Stellenanzeige
- Unternehmensblog
- öffentliche Supportdiskussion
- RSS-Feed
- öffentliche Social-Media-Äußerung

---

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

---

## 3.3 Problem

Eine abstrahierte Beschreibung des zugrunde liegenden Problems.

Die Beschreibung soll möglichst unabhängig von der Wortwahl der Quelle sein.

Beispiel:

Quelle:

> „Wir haben inzwischen fünf verschiedene ETL-Strecken und keiner weiß mehr, warum manche Daten zweimal geschrieben werden.“

Problem:

> Fehlende Nachvollziehbarkeit und strukturelle Kontrolle einer historisch gewachsenen Datenintegrationsarchitektur.

---

## 3.4 Betroffener Akteur

Die Person oder Organisation, die unter dem Problem leidet oder für dessen Lösung verantwortlich ist.

Beispiele:

- Entwickler
- Teamleiter
- CTO
- Geschäftsführer
- Forschungsteam
- Behörde
- Bildungseinrichtung
- Freelancer
- Betreiber eines Systems

---

## 3.5 Intervention

Eine konkrete Leistung, die das Problem zumindest teilweise verbessern könnte.

Eine Intervention muss enger formuliert sein als eine allgemeine Fähigkeit.

Nicht:

> Softwarearchitektur

Sondern beispielsweise:

> Zweitägige unabhängige Diagnose der Datenflüsse mit Rekonstruktion von Abhängigkeiten, Redundanzen und Fehlerquellen.

---

# 4. Fähigkeitsmodell

Problem-Radar erhält ein explizites Modell desjenigen, für den Probleme gesucht werden.

Dieses Modell darf wesentlich breiter sein als ein Lebenslauf.

Es enthält mindestens:

## 4.1 Technisches Wissen

Beispielsweise:

- Softwarearchitektur
- Python
- SQL
- Datenbanken
- ETL/DWH
- Cloud-Systeme
- Legacy-Systeme
- Performance
- Parallelisierung
- Compiler und Interpreter
- Systemintegration
- Automatisierung
- KI-Systeme

---

## 4.2 Problemlösungsfähigkeiten

Beispielsweise:

- strukturelle Diagnose
- Problemzerlegung
- Ursachenanalyse
- Refactoring
- Rekonstruktion unbekannter Systeme
- Reduktion von Komplexität
- Architekturkritik
- unabhängige Zweitmeinung
- Modellbildung

---

## 4.3 Epistemische Fähigkeiten

Beispielsweise:

- Perspektivwechsel
- Widerspruchsanalyse
- Explizierung impliziter Annahmen
- Trennung vermischter Kategorien
- Rekonstruktion von Argumentationsstrukturen
- Identifikation von Blindstellen
- Vergleich konkurrierender Modelle
- Untersuchung von Systemgrenzen
- Analyse unterschiedlicher Zeithorizonte

---

## 4.4 Verfügbare Methoden und Werkzeuge

Beispielsweise:

- Schnittwerk
- epistemische Operatoren
- Brillenmodelle
- epistemischer Linter
- diagnostische Verfahren
- KI-gestützte Analyseverfahren

---

## 4.5 Arbeitspräferenzen

Das Fähigkeitsmodell kann zusätzlich Bedingungen enthalten.

Beispielsweise:

Bevorzugt:

- begrenzte Interventionen
- Diagnose
- schwierige Einzelprobleme
- Analyse
- Prototyping
- unabhängige Beratung
- Forschungsnähe

Weniger erwünscht:

- langfristige Teamaugmentation
- reine Implementierung nach Tickets
- dauerhafte Scrum-Rollen
- Routinewartung
- reine Personalüberlassung

Diese Angaben beeinflussen das Ranking, nicht die Erkennung eines Problems.

---

# 5. Quellenerschließung

Problem-Radar muss selbständig geeignetes Material finden können.

Es existieren drei Zugriffsmodi.

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

---

## Modus B – Direkte Quellenbeobachtung

Bestimmte Quellen können regelmäßig untersucht werden.

Beispiele:

- ausgewählte Subreddits
- GitHub-Repositories
- Foren
- RSS-Feeds
- bestimmte Blogs
- technische Communities

Die Quelle wird nicht deshalb relevant, weil sie vorher als „gute Quelle“ definiert wurde.

Ihre tatsächliche Fundqualität soll beobachtet werden.

---

## Modus C – Authentifizierte Quellen

Optional können Quellen verwendet werden, die ein Benutzerkonto verlangen.

Authentifizierung ist Aufgabe der Laufzeitumgebung, nicht des Sprachmodells.

### Sicherheitsregel

Zugangsdaten dürfen niemals Bestandteil der Problem-Radar-Spezifikation oder eines LLM-Prompts sein.

Stattdessen verwendet die Laufzeit beispielsweise:

- OAuth
- API-Tokens
- Session-Management
- Connectoren
- lokale Secret Stores

Das KI-System erhält ausschließlich den autorisierten Zugriff.

Ein separates Konto für automatisierte Recherche kann sinnvoll sein, sofern Plattformregeln dies erlauben.

---

# 6. Suchstrategie

Das System darf sich nicht auf explizite Hilfegesuche beschränken.

Es sucht mindestens nach folgenden Signalgruppen.

## Explizite Problemsignale

Beispiele:

- „Wie löst ihr …?“
- „Wir bekommen … nicht hin.“
- „Hat jemand Erfahrung mit …?“
- „Unser Problem ist …“
- „Warum funktioniert …?“
- „Ich suche eine Lösung für …“

---

## Implizite Problemsignale

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

---

## Problemsignale zweiter Ordnung

Besonders interessant sind Situationen, in denen der Akteur möglicherweise das falsche Problem zu lösen versucht.

Beispiel:

> „Welche KI kann unsere 300-seitigen Prozesshandbücher besser durchsuchen?“

Mögliche tiefere Probleme:

- ungeeignete Wissensstruktur
- fehlende Explizierung
- schlechte Informationsarchitektur
- widersprüchliche Prozessmodelle
- ungeklärte Verantwortlichkeiten

Problem-Radar darf solche tieferen Interpretationen erzeugen.

Sie müssen jedoch ausdrücklich als **Hypothese** markiert werden.

---

# 7. Analyseoperatoren

Für jeden Kandidaten führt das System folgende Operationen aus.

## O1 – Problemsignal extrahieren

Bestimme:

- Was funktioniert nicht?
- Wer ist betroffen?
- Welche Folgen werden beschrieben?
- Welche Originalaussagen belegen dies?

---

## O2 – Problem abstrahieren

Formuliere das zugrunde liegende Problem unabhängig von der konkreten Wortwahl.

Vermeide unnötige Generalisierung.

---

## O3 – Wunschzustand rekonstruieren

Bestimme:

> Was müsste anders sein, damit der Akteur das Problem als gelöst oder wesentlich verbessert betrachten würde?

---

## O4 – Ursachenhypothesen bilden

Erzeuge mögliche zugrunde liegende Ursachen.

Trenne dabei strikt:

- belegte Ursache
- plausible Ursache
- spekulative Ursache

---

## O5 – Fähigkeitsmatching

Bestimme:

- welche Fähigkeiten passen,
- warum sie passen,
- welcher Teil des Problems damit bearbeitbar wäre,
- welcher nicht.

---

## O6 – Intervention konstruieren

Formuliere mindestens eine konkrete, begrenzte Intervention.

Eine Intervention soll möglichst beantworten:

- Was würde getan?
- Was erhält der Kunde?
- Wie groß ist ungefähr der Eingriff?
- Welcher Nutzen könnte entstehen?

---

## O7 – Käufer identifizieren

Frage:

> Gibt es jemanden, der nicht nur betroffen ist, sondern tatsächlich entscheiden kann, für eine Lösung Ressourcen einzusetzen?

Unterscheide:

- Betroffener
- Nutzer
- Entscheider
- Budgethalter

---

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

Nicht jedes interessante Problem ist ein kommerziell relevantes Problem.

---

## O9 – Zugänglichkeit prüfen

Bewerte:

- Ist ein Ansprechpartner identifizierbar?
- Ist Kontaktaufnahme angemessen?
- Existiert bereits ein öffentliches Hilfegesuch?
- Ist die Organisation erreichbar?
- Ist das Problem aktuell?

---

## O10 – epistemische Gegenprüfung

Vor Aufnahme eines Funds muss das System fragen:

1. Wurde das Problem tatsächlich beobachtet?
2. Was wurde nur inferiert?
3. Welche alternativen Interpretationen gibt es?
4. Wird lediglich aufgrund des Fähigkeitsmodells überall ein passendes Problem gesehen?
5. Ist die vorgeschlagene Intervention tatsächlich plausibel?
6. Welche Informationen fehlen?

---

# 8. Bewertung

Jeder Fund erhält Bewertungen von 0 bis 5.

### Problemklarheit

Wie eindeutig existiert das Problem?

### Evidenz

Wie stark wird die Interpretation durch die Quelle gestützt?

### Fähigkeitsfit

Wie gut passt das Fähigkeitsmodell?

### Interventionsklarheit

Kann eine konkrete Leistung formuliert werden?

### wirtschaftliche Relevanz

Ist das Problem wahrscheinlich teuer oder wichtig genug?

### Käuferklarheit

Ist ein möglicher Auftraggeber identifizierbar?

### Zugänglichkeit

Kann der Akteur realistisch erreicht werden?

### Aktualität

Ist das Problem noch relevant?

### Neuigkeitswert

Ist die Kombination aus Problem und möglicher Intervention ungewöhnlich?

### Unsicherheit

Wie viel Interpretation steckt in der Analyse?

---

# 9. Priorisierung

Ein hoher Gesamtscore allein genügt nicht.

Problem-Radar soll insbesondere Kandidaten hervorheben, bei denen gleichzeitig gilt:

> reales Problem  
> + hoher Fähigkeitsfit  
> + plausible Intervention  
> + wirtschaftliche Relevanz  
> + erreichbarer Akteur

Ein technisch faszinierendes Problem ohne Käufer ist entsprechend niedriger zu priorisieren.

Ein zahlungsfähiger Käufer ohne besonderen Fähigkeitsfit ebenfalls.

---

# 10. Ausgabeformat

Ein Fund soll kompakt dargestellt werden.

## Fund

**Problem:**  
Kurze abstrahierte Beschreibung.

**Quelle:**  
URL / Plattform / Datum

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

**Warum möglicherweise wirtschaftlich relevant:**  
Kurze Begründung.

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
- Gespräch suchen
- kleine Analyse erstellen

---

# 11. Keine automatische Akquise

Problem-Radar ist zunächst ein **Beobachtungs- und Diagnosesystem**.

Es darf ohne ausdrückliche Freigabe nicht:

- Personen anschreiben,
- Kommentare posten,
- Angebote versenden,
- Accounts kontaktieren,
- automatisierte Werbung betreiben.

Die Grenze zwischen Beobachtung und Intervention bleibt explizit.

---

# 12. Lernschleife

Problem-Radar soll aus der späteren Bewertung seiner Funde lernen können.

Für jeden Fund können beispielsweise folgende Rückmeldungen gespeichert werden:

- uninteressant
- interessant
- überraschend
- bereits bekannt
- schlechter Fit
- guter Fit
- kein Käufer
- Kontakt aufgenommen
- Gespräch entstanden
- Auftrag entstanden
- Problem falsch interpretiert

Diese Historie darf als Material für spätere Bewertungen verwendet werden.

Sie darf jedoch nicht dazu führen, nur noch bereits bekannte Problemtypen zu finden.

Exploration muss erhalten bleiben.

---

# 13. Betriebsmodi

## Exploration

Suche breit nach ungewöhnlichen Problemen und neuen Problemklassen.

Optimiert auf:

> „Was habe ich bisher übersehen?“

---

## Opportunity Scan

Suche gezielt nach aktuell wirtschaftlich interessanten Problemen.

Optimiert auf:

> „Wo könnte kurzfristig eine bezahlbare Intervention entstehen?“

---

## Domain Scan

Untersuche einen bestimmten Bereich.

Beispielsweise:

- KI-Einführung in Unternehmen
- Legacy-Software
- Datenarchitektur
- Bildung
- Wissensmanagement

---

## Source Scan

Untersuche eine bestimmte Community oder Quelle.

Beispielsweise:

> Analysiere neue Beiträge in ausgewählten technischen Subreddits auf relevante Problemsignale.

---

## Deep Dive

Untersuche einen bereits gefundenen Kandidaten genauer.

Suche weitere Quellen und prüfe:

- Ist das Problem systematisch?
- Betrifft es mehrere Akteure?
- Welche bisherigen Lösungsversuche existieren?
- Gibt es bereits Anbieter?
- Was wäre eine unterscheidbare Intervention?

---

# 14. Qualitätsprinzipien

## Problem vor Lösung

Das System darf nicht zuerst eine vorhandene Fähigkeit nehmen und anschließend krampfhaft ein Problem dazu konstruieren.

---

## Evidenz vor Interpretation

Jede starke Behauptung benötigt eine erkennbare Grundlage.

---

## Hypothesen sichtbar halten

Interpretation ist erlaubt.

Verdeckte Interpretation ist nicht erlaubt.

---

## Konkretion vor Schlagwort

„Digitale Transformation“ ist kein Problem.

„Drei Abteilungen führen dieselben Kundendaten unabhängig voneinander und niemand kann erklären, welche Version verbindlich ist“ ist eines.

---

## Intervention vor Selbstbeschreibung

Nicht:

> „Hier könnte strategische Beratung helfen.“

Sondern:

> „Rekonstruktion der drei Datenflüsse, Identifikation widersprüchlicher Ownership-Regeln und Erstellung eines gemeinsamen Zuständigkeitsmodells.“

---

## Nutzen vor Technologie

Eine technische Übereinstimmung allein begründet keinen Fund.

---

# 15. Minimaler Runtime-Vertrag

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

# 16. Minimal Viable Problem-Radar

Für einen ersten Test ist kein eigener Crawler erforderlich.

Eine ausreichend leistungsfähige KI mit Webzugriff erhält:

1. diese Spezifikation,
2. ein Fähigkeitsmodell,
3. den Auftrag:

> Suche in öffentlich zugänglichen Quellen nach aktuellen Problemsignalen.  
> Identifiziere Probleme, bei denen das gegebene Fähigkeitsmodell eine konkrete und wirtschaftlich plausible Intervention erlaubt.  
> Liefere nur ausreichend belegte Kandidaten.  
> Suche nicht nur nach expliziten Aufträgen oder Stellenanzeigen.  
> Behandle tieferliegende Problemdeutungen als Hypothesen.  
> Priorisiere reale Probleme vor bloßer thematischer Ähnlichkeit.

Damit lässt sich die zentrale Hypothese von Problem-Radar testen, bevor eigene Infrastruktur entwickelt wird.

---

# 17. Forschungsfrage

Die zentrale experimentelle Frage lautet:

> **Kann ein KI-System aus heterogenen öffentlichen Äußerungen kommerziell relevante Problemsituationen erkennen, die durch klassische Job-, Lead- oder Keyword-Suche nicht oder nur schwer auffindbar wären?**

Eine stärkere Variante lautet:

> **Kann ein explizites Fähigkeitsmodell seine eigenen Anwendungsfälle finden?**

---

# 18. Einordnung

Problem-Radar kann unabhängig verwendet werden.

Konzeptionell lässt es sich jedoch als kleiner Spezialfall einer allgemeineren semantischen Routing-Infrastruktur verstehen:

> Nicht Menschen suchen nach passenden Ausschreibungen.

> Nicht Anbieter suchen nach passenden Kunden.

> **Probleme werden mit möglichen Lösungsfähigkeiten in Beziehung gesetzt.**

In dieser Form lautet das Prinzip:

> **Fähigkeiten finden ihre Probleme.**