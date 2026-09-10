# Capability Model

## Fähigkeitsmodell für Problem-Radar

**Version 0.2**

---

# 1. Zweck

Dieses Dokument beschreibt die Fähigkeiten, Methoden, Werkzeuge, Arbeitspräferenzen und möglichen Interventionsformen des Akteurs, für den Problem-Radar nach passenden Problemsituationen sucht.

Es ist kein Lebenslauf.

Es beschreibt nicht primär, welche Technologien bekannt sind oder welche Rollen bereits ausgeübt wurden, sondern:

> **Welche Arten von Problemen kann dieser Akteur wahrscheinlich erkennen, verstehen oder lösen?**

Das Modell dient als semantische Grundlage für das Matching zwischen beobachteten Problemen und möglichen Interventionen.

---

# 2. Grundprinzip

Eine Fähigkeit ist mehr als eine Technologie oder ein Schlagwort.

Beispielsweise ist:

> Python

technische Kompetenz.

Dagegen ist:

> ein unbekanntes technisches System rekonstruieren und seine wesentlichen Strukturen sichtbar machen

Problemlösungsfähigkeit.

Für Problem-Radar sind insbesondere Fähigkeiten der zweiten Art relevant.

---

# 3. Technische Domänen

## 3.1 Softwareentwicklung

Erfahrung mit:

- C
- C++
- Java
- Python
- Scala
- SQL
- VBA
- .NET
- PowerShell

Die konkrete Programmiersprache ist normalerweise nachrangig gegenüber der zugrunde liegenden Problemstruktur.

## 3.2 Softwarearchitektur

Fähigkeiten:

- Analyse bestehender Architekturen
- Identifikation struktureller Schwächen
- Entkopplung
- Modularisierung
- Schnittstellenanalyse
- Rekonstruktion impliziter Architektur
- Architekturrefactoring
- Bewertung technischer Alternativen
- Systemgrenzen bestimmen

Besonders geeignet für historisch gewachsene Systeme, deren tatsächliche Architektur von der dokumentierten Architektur abweicht.

## 3.3 Legacy-Systeme

Fähigkeiten:

- Einstieg in unbekannte oder schlecht dokumentierte Systeme
- Rekonstruktion historisch entstandener Strukturen
- Identifikation technischer Schulden
- Unterscheidung notwendiger Komplexität von historischer Komplexität
- schrittweises Refactoring
- Risikoabschätzung bei Änderungen
- Erhaltung vorhandener Funktionalität während struktureller Verbesserungen

## 3.4 Performance und Parallelisierung

Fähigkeiten:

- Performanceanalyse
- Engpassdiagnose
- Laufzeitverhalten untersuchen
- Ressourcenverbrauch analysieren
- Parallelisierung
- Multithreading
- algorithmische Optimierung
- unnötige Arbeit erkennen
- Performanceprobleme strukturell statt symptomatisch behandeln

## 3.5 Daten und Datenintegration

Erfahrung und Fähigkeiten in:

- Data Warehousing
- ETL
- SQL
- Datenbanken
- SSIS
- Polybase
- Timescale
- Azure Data Factory
- Azure Synapse
- Datenflüsse
- Schnittstellen
- Datenpipelines

Diagnostische Fähigkeiten:

- Datenherkunft rekonstruieren
- redundante Datenflüsse erkennen
- Ownership-Probleme identifizieren
- Inkonsistenzen zwischen Systemen untersuchen
- historisch gewachsene Integrationsarchitekturen vereinfachen
- Ursachen schwer nachvollziehbarer Datenfehler lokalisieren

## 3.6 Cloud, Infrastruktur und Automatisierung

Erfahrung mit:

- Azure
- Docker
- Kubernetes
- Jenkins
- Azure DevOps
- Git
- Key Vault
- Storage
- Automation

Relevanter als einzelne Produkte ist die Fähigkeit, verteilte technische Abläufe als Gesamtsystem zu rekonstruieren.

## 3.7 Compiler, Interpreter und formale Systeme

Erfahrung mit:

- Compilerbau
- Interpreterbau
- formalen Repräsentationen
- Transformationen
- deklarativen Beschreibungen

Daraus abgeleitete Stärke:

> Komplexe Abläufe bevorzugt über explizite Strukturen, Regeln, Operatoren und Transformationen betrachten.

---

# 4. Übergreifende Problemlösungsfähigkeiten

## 4.1 Strukturdiagnose

Fähigkeit, aus einem komplexen Sachverhalt eine tragfähige Struktur herauszuarbeiten.

Typische Fragen:

- Was sind die relevanten Bestandteile?
- Welche Beziehungen bestehen?
- Welche Abhängigkeiten sind wesentlich?
- Was ist Ursache, was Symptom?
- Wo liegen Systemgrenzen?
- Welche Komplexität ist notwendig?
- Welche Komplexität ist historisch entstanden?

## 4.2 Rekonstruktion unbekannter Systeme

Fähigkeit, sich in Systeme einzuarbeiten, die schlecht dokumentiert, historisch gewachsen, widersprüchlich, teilweise defekt oder organisatorisch fragmentiert sind.

Arbeitsweise:

1. Beobachtbare Strukturen identifizieren.
2. Abhängigkeiten rekonstruieren.
3. implizite Regeln herausarbeiten.
4. Widersprüche und Sonderfälle sammeln.
5. ein explizites Modell erzeugen.
6. Modell gegen das reale System prüfen.

## 4.3 Refactoring

Refactoring wird nicht nur als Quellcode-Technik verstanden.

Allgemeines Prinzip:

> Eine funktionierende, aber schwer verständliche Struktur so verändern, dass ihre innere Ordnung klarer wird, ohne den relevanten Gegenstand unnötig zu verändern.

Anwendbar auf:

- Quellcode
- Architekturen
- Prozesse
- Datenflüsse
- Anforderungen
- Argumentationen
- Begriffssysteme
- Fragestellungen
- Entscheidungsräume

## 4.4 Problemzerlegung

Fähigkeit, komplexe Probleme in möglichst unabhängige Teilprobleme zu zerlegen.

Bevorzugt werden Zerlegungen, bei denen:

- unterschiedliche Dimensionen getrennt bleiben,
- funktionale Redundanz gering ist,
- Abhängigkeiten explizit werden,
- Teilfragen separat bearbeitet werden können.

## 4.5 Ursachenanalyse

Stärke bei Problemen, bei denen Symptome bekannt, Ursachen unklar und mehrere plausible Erklärungen vorhanden sind.

Bevorzugte Operationen:

- Hypothesen erzeugen
- Gegenhypothesen bilden
- Evidenz unterscheiden
- Kausalmodelle vergleichen
- Rückkopplungen untersuchen
- Systemgrenzen variieren
- zeitliche Dynamik berücksichtigen

## 4.6 Second Opinion

Geeignet als unabhängige Instanz für bestehende Architekturen, Lösungsansätze, Konzepte, technische Entscheidungen, KI-Workflows oder Analysen.

Aufgabe:

> Nicht erneut dasselbe Problem lösen, sondern prüfen, welche Annahmen, Blindstellen, Alternativen oder strukturellen Schwächen bisher übersehen wurden.

---

# 5. Epistemische Fähigkeiten

## 5.1 Explizierung

Implizites Wissen, Können oder Verständnis wird in eine adressierbare Repräsentation überführt.

Mögliche Resultate:

- Begriffe
- Relationen
- Kategorien
- Regeln
- Modelle
- Operatoren
- Entscheidungsstrukturen
- Diagnosemodelle

Explizierung dient insbesondere Kommunikation, Prüfung, Vergleich, Modifikation, Wiederverwendung, Automatisierung und KI-Nutzung.

## 5.2 Perspektivanalyse

Fähigkeit, unterschiedliche Perspektiven auf denselben Gegenstand auseinanderzuhalten.

## 5.3 Kategorienanalyse

Fähigkeit zu erkennen, wenn Diskussionen oder Modelle unterschiedliche Kategorien vermischen.

Beispiele:

- Beschreibung und Bewertung
- Ursache und Rechtfertigung
- Mittel und Ziel
- Individuum und System
- kurzfristige und langfristige Wirkung
- empirische und normative Aussage
- Modell und Gegenstand

## 5.4 Annahmenanalyse

Fähigkeit, implizite Voraussetzungen sichtbar zu machen.

## 5.5 Widerspruchsanalyse

Unterscheidung verschiedener Arten scheinbarer Widersprüche, etwa durch unterschiedliche Perspektiven, Systemgrenzen, Zeithorizonte, Ziele oder Begriffe.

## 5.6 Blindstellenanalyse

Frage:

> Was kann innerhalb des aktuell verwendeten Modells kaum oder gar nicht gesehen werden?

## 5.7 Fragenrefactoring

Eine Frage wird nicht nur beantwortet, sondern auf versteckte Annahmen, Kategorienmischungen, unklare Begriffe, falsche Systemgrenzen, fehlende Perspektiven und voreilige Lösungsannahmen untersucht.

---

# 6. Eigene Methoden und epistemische Werkzeuge

## 6.1 Schnittwerk

Epistemische Architektur für Fragen, Perspektiven, Problemräume, Operatoren, Analyse, Refactoring und Auditierbarkeit.

## 6.2 Brillenmodelle

Deklarative Spezifikationen bestimmter Perspektiven.

## 6.3 Epistemische Operatoren

Wiederverwendbare Denkoperationen zur Bearbeitung von Problemräumen.

## 6.4 Epistemischer Linter

Analyse von Fragen, Prompts, Argumentationen, Anforderungen und Entscheidungsgrundlagen auf strukturelle Fehler oder Unklarheiten.

## 6.5 Diagnostischer Tutor

KI-gestütztes Lernverfahren zur Diagnose von Verständnisstrukturen.

## 6.6 Disput-Refactoring

Analyse festgefahrener Diskussionen durch Zerlegung von Positionen, Systemgrenzen, Zeithorizonten und Begriffen.

---

# 7. KI-bezogene Fähigkeiten

## 7.1 KI als kognitives Werkzeug

Fähigkeit, KI nicht nur als Textgenerator einzusetzen, sondern als Analyseinstrument, Strukturspiegel, Perspektivmaschine, diagnostisches Werkzeug, Forschungsassistent, Refactoring-System und semantische Runtime.

## 7.2 Deklarative KI-Spezifikationen

Besonderes Interesse und Erfahrung mit der Idee:

> Nicht jeden Arbeitsablauf prozedural programmieren, sondern einer leistungsfähigen KI eine explizite Domänenspezifikation geben.

Typische Bestandteile:

- Begriffe
- Operatoren
- Relationen
- Regeln
- Qualitätskriterien
- Ausgabeformen
- Grenzen
- Prüfverfahren

## 7.3 KI-Workflow-Diagnose

Potenzielle Interventionen:

- bestehenden KI-Einsatz untersuchen
- schlechte Prompt-/Workflow-Strukturen erkennen
- Aufgaben sinnvoll zwischen Mensch und KI aufteilen
- implizite Anforderungen explizieren
- Output-Qualität diagnostizieren
- zuverlässigere Prüf- und Feedbackschleifen entwickeln

## 7.4 Kontext- und Spezifikationspflege

Neue Problemklasse:

Explizite KI-Kontexte, Skills, Regeln, `CLAUDE.md`-/`AGENTS.md`-artige Dateien oder andere dauerhafte Spezifikationen können gegenüber der realen Systemlandschaft veralten.

Relevante Fähigkeiten:

- veraltete Annahmen erkennen
- Kontext gegen Realität prüfen
- Scope-Grenzen explizieren
- Regelkonflikte identifizieren
- deklarative Wissensartefakte versionierbar und lintbar machen

## 7.5 Eval- und Verifikationsarchitektur

Fähigkeit, nicht nur den KI-Output, sondern die Struktur seiner Prüfung zu untersuchen.

Fragen:

- Was gilt überhaupt als korrekt?
- Welche Fehlerklassen werden geprüft?
- Welche Evals sind veraltet?
- Welche Prüfungen verursachen hohe menschliche Kosten?
- Welche Qualitätsgates können explizit oder deterministisch werden?

---

# 8. Typische Problemsituationen mit hohem Fit

Problem-Radar soll besonders aufmerksam werden bei:

- technischer Sackgasse
- historisch gewachsener Komplexität
- niemand versteht das Ganze
- wiederkehrenden Reparaturen
- schlechter oder widersprüchlicher Architektur
- Informations- oder Datenchaos
- unklaren Anforderungen
- festgefahrenen Entscheidungen
- festgefahrenen Disputen
- unbefriedigendem KI-Einsatz
- hohem Human-in-the-loop-Aufwand
- Review-/Verifikationsstau
- veraltetem KI-Kontext
- implizitem Wissen, das für Agenten expliziert werden muss
- AI Technical Debt
- Cognitive Debt
- Eval Drift
- Agentenlandschaften mit unklaren Rechten oder Ownership

---

# 9. Besonders interessante Problemmuster

Bonus bei Kombinationen wie:

- Problem ist strukturell statt rein operativ.
- Ursache ist unbekannt.
- vorhandene Lösungsversuche sind gescheitert.
- mehrere Domänen sind beteiligt.
- Problem wird falsch oder zu eng beschrieben.
- Beteiligte haben den Überblick verloren.
- unabhängige Analyse wäre wertvoll.
- ein begrenzter diagnostischer Eingriff könnte großen Nutzen erzeugen.
- ungewöhnliche Kombination aus Technik und Modellbildung ist gefragt.
- KI ist Teil der Lösung, aber nicht durch bloße Standardautomatisierung.

---

# 10. Konkrete Angebotsformen

Die folgenden Angebote übersetzen Fähigkeiten in kaufbare, begrenzte Interventionen.

## 10.1 KI-Workflow-Audit

### Problem

Ein produktiver KI-Workflow spart weniger Arbeit als erwartet, weil Kontrolle, Nacharbeit, Ausnahmebehandlung und Verifikation den Nutzen auffressen.

### Typische Käufer

- CTO
- Head of AI
- VP Engineering
- Engineering Manager
- AI Engineering Lead
- Product Owner eines produktiven KI-Systems

### Intervention

Analyse eines konkreten Workflows auf:

- menschliche Eingriffe
- Supervision Costs
- Verification Costs
- Fehlermuster
- unklare Zustände
- fehlende Validierung
- ungeeignete Aufgabenzerlegung
- fehlende Abbruchbedingungen
- falsche Mischung probabilistischer und deterministischer Komponenten

### Ergebnis

- Workflow-Modell
- Supervision-/Verification-Hotspots
- Ursachenanalyse
- priorisierte Verbesserungen
- optional kleiner Prototyp

### Einstiegsform

Kleiner Pilot an einem einzelnen realen Workflow.

---

## 10.2 AI Context / Specification Audit

### Problem

Die expliziten Regeln und Kontextdateien, nach denen KI-Agenten arbeiten, sind unvollständig, widersprüchlich, schlecht geschnitten oder veraltet.

### Typische Käufer

- AI Platform Lead
- Engineering Manager
- Developer Productivity Lead
- CTO
- Head of AI

### Intervention

Prüfung von:

- Systemprompts
- Skills
- Agent Rules
- `CLAUDE.md`
- `AGENTS.md`
- persistentem Agent-Kontext
- internen KI-Spezifikationen

auf:

- veraltete Aussagen
- fehlende Strukturen
- widersprüchliche Regeln
- falsche Scope-Grenzen
- unklare Gültigkeit
- mangelnde Prüfbarkeit

### Ergebnis

- Kontext-/Spec-Modell
- Konflikt- und Rot-Report
- Vorschlag für bessere Strukturierung
- Linting-/Pflegekonzept

---

## 10.3 Knowledge-to-Spec Refactoring

### Problem

Wesentliches Wissen liegt nur implizit in Köpfen erfahrener Mitarbeiter und ist für Menschen wie KI-Agenten schwer adressierbar.

### Käufer

- Engineering Leads
- Platform Teams
- Knowledge Management
- Teams mit starkem Experten- oder Legacy-Wissen

### Intervention

Implizites Wissen extrahieren und in versionierte, prüfbare, KI-lesbare Spezifikationen überführen.

### Ergebnis

> **Extrahieren → Explizieren → Anwenden → Prüfen → Aktualisieren**

---

## 10.4 System-Reconstruction Sprint

### Problem

Niemand versteht ein historisch gewachsenes System oder seine Datenflüsse noch vollständig.

### Typische Käufer

- CTO
- Head of IT
- Head of Data
- Lead Architect
- Engineering Manager

### Intervention

Begrenzte unabhängige Rekonstruktion von:

- Architektur
- Abhängigkeiten
- Datenflüssen
- Ownership
- kritischen Risiken
- impliziten Regeln

### Ergebnis

Ein belastbares Modell dessen, wie das System tatsächlich funktioniert, plus priorisierte Handlungsoptionen.

### Rolle

Dieses Angebot ist die am leichtesten verständliche Brücke zu klassisch bezahlter Arbeit, ohne langfristige Teamaugmentation vorauszusetzen.

---

# 11. Angebotspriorität

Für die aktuelle Markterprobung:

## A – Jetzt testen

**KI-Workflow-Audit**

Niedrige Erklärungshürde, aktueller Schmerz, begrenzte Intervention.

## B – Neues Terrain entwickeln

**AI Context / Specification Audit**

Noch junges Problemfeld mit starkem Fit zu deklarativen Spezifikationen und epistemischem Linting.

## C – Einnahmebrücke

**System-Reconstruction Sprint**

Hoher Fit zur langjährigen technischen Erfahrung und leicht verständlicher Kundennutzen.

---

# 12. Arbeitspräferenzen

## Bevorzugt

- klar begrenzte Probleme
- anspruchsvolle Diagnose
- hohe Eigenständigkeit
- überschaubare Interventionen
- Forschung und Exploration
- Architektur
- Analyse
- Refactoring
- Prototyping
- schwierige Sonderfälle
- unabhängige Zweitmeinung
- Arbeit mit direktem Erkenntnisgewinn
- Aufgaben, bei denen zunächst verstanden werden muss, was eigentlich das Problem ist

## Weniger bevorzugt

- dauerhafte Teamaugmentation
- langfristige Vollzeitintegration in Scrum-Teams
- tägliche Statusrituale als zentraler Arbeitsmodus
- reine Ticketabarbeitung
- Routineimplementierung
- Wartung ohne strukturellen Gestaltungsspielraum
- Aufgaben, bei denen die Lösung vollständig vorgegeben ist und lediglich Arbeitskapazität benötigt wird

Diese Präferenzen sind keine absoluten Ausschlusskriterien, beeinflussen aber den Opportunity-Score.

---

# 13. Gute Auftragsform

Besonders passend:

> „Wir haben ein schwieriges Problem und verstehen noch nicht vollständig, warum es entsteht. Schau dir das unabhängig an, rekonstruiere die relevante Struktur und sag uns, was du siehst.“

Weniger passend:

> „Wir haben bereits 427 Jira-Tickets spezifiziert und benötigen einen weiteren Entwickler zur Abarbeitung.“

---

# 14. Capability Matching

Problem-Radar fragt:

1. Ist das Problem mit den vorhandenen Fähigkeiten tatsächlich bearbeitbar?
2. Gibt es einen ungewöhnlich guten Fit?
3. Ist die Kombination mehrerer Fähigkeiten relevant?
4. Kann daraus eine konkrete Intervention entstehen?
5. Ist diese Intervention zeitlich und organisatorisch realistisch?
6. Könnte ein Standardanbieter das Problem offensichtlich besser lösen?
7. Gibt es einen plausiblen Käufer?
8. Ist der Käufer oder ein interner Champion realistisch erreichbar?

---

# 15. Kombinatorische Fähigkeiten

Besonders relevant sind Kombinationen.

### Softwarearchitektur + epistemische Analyse

Geeignet für Probleme, bei denen technische Architektur und mentale Modelle der Beteiligten gleichzeitig fragmentiert sind.

### Legacy-Erfahrung + Rekonstruktion

Geeignet für Systeme, bei denen Dokumentation, Implementierung und Organisationswissen auseinandergefallen sind.

### KI + deklarative Spezifikation

Geeignet für Aufgaben, bei denen ein LLM systematisch nach expliziten Regeln analysieren oder diagnostizieren soll.

### Refactoring + Problemzerlegung

Geeignet für Probleme, die bisher als monolithische Gesamtfrage behandelt wurden.

### technische Analyse + Perspektivwechsel

Geeignet für Konflikte zwischen technischen und organisatorischen Sichtweisen.

### Forschung + Prototyping

Geeignet für Probleme, bei denen noch unklar ist, ob eine Lösung überhaupt funktioniert.

### Explizierung + KI-Betrieb

Geeignet für Context Rot, AI Specification Debt und Knowledge-to-Spec-Aufgaben.

### Verifikation + epistemische Analyse

Geeignet für Supervision Costs, Verification Debt und Eval Drift.

---

# 16. Anti-Matching

Problem-Radar soll Kandidaten abwerten, wenn:

- lediglich zusätzliche Entwicklungskapazität gesucht wird,
- das Problem vollständig spezifiziert und routinemäßig ist,
- eine lange operative Einbindung zwingend erforderlich ist,
- das Problem überwiegend Vertrieb, Marketing oder Verwaltung betrifft,
- kein relevanter struktureller oder diagnostischer Anteil existiert,
- die benötigte Expertise klar außerhalb des Fähigkeitsprofils liegt,
- die mögliche Intervention keinen erkennbaren Vorteil gegenüber Standarddienstleistungen besitzt.

---

# 17. Explorationsregel

Das Modell darf nicht dazu führen, ausschließlich bekannte Einsatzgebiete zu finden.

Problem-Radar soll ausdrücklich auch nach Problemen suchen, bei denen eine vorhandene Fähigkeit in einem bislang nicht betrachteten Kontext nützlich sein könnte.

Solche Treffer müssen als **exploratives Matching** gekennzeichnet werden.

---

# 18. Meta-Fähigkeit

Über den einzelnen Fähigkeiten steht eine allgemeinere Fähigkeit:

> **Aus komplexen, historisch gewachsenen oder schlecht explizierten Zusammenhängen ein handhabbares Modell erzeugen.**

Typische Operationen:

- beobachten
- unterscheiden
- abstrahieren
- zerlegen
- Beziehungen herstellen
- explizieren
- Modelle bilden
- Widersprüche prüfen
- Perspektiven wechseln
- Strukturen refactorieren
- erneut gegen die Realität prüfen

Diese Meta-Fähigkeit darf niemals allein zur Behauptung führen, ein unbekanntes Fachproblem lösen zu können.

---

# 19. Grenzen

- Fachwissen bleibt relevant.
- Gute Strukturdiagnose ersetzt keine unbekannte Spezialexpertise.
- Hypothesen über neue Einsatzgebiete müssen getestet werden.
- epistemische Werkzeuge garantieren keine richtige Analyse.
- technisches Können bedeutet nicht automatisch wirtschaftliche oder organisatorische Kompetenz.
- ein hoher semantischer Fit ist noch kein Kundenbedarf.
- ein realer Bedarf bedeutet noch keine Zahlungsbereitschaft.
- ein guter Fund ohne Kontaktpfad ist noch keine Opportunity.

---

# 20. Kurzprofil für Problem-Radar

> Seniorer Softwareentwickler und Systemanalytiker mit langjähriger Erfahrung in Softwarearchitektur, Legacy-Systemen, Datenintegration, Performance, Automatisierung und komplexen technischen Systemen. Besondere Stärke in der Rekonstruktion unbekannter oder historisch gewachsener Strukturen, Ursachenanalyse, Problemzerlegung und Refactoring. Zusätzlich Entwicklung epistemischer Methoden zur Explizierung von Annahmen, Perspektiven, Kategorien, Fragestellungen und Entscheidungsräumen sowie KI-gestützter Analyseverfahren. Bevorzugt begrenzte diagnostische, architektonische, forschende und prototypische Interventionen gegenüber langfristiger operativer Teamaugmentation. Aktuelle Angebotsfelder: KI-Workflow-Audit, AI Context/Specification Audit, Knowledge-to-Spec Refactoring und System-Reconstruction Sprint.

---

# 21. Leitfrage

Beim Matching ist nicht zu fragen:

> „Passt dieser Auftrag zum bisherigen Berufsbild?“

Sondern:

> **„Gibt es hier ein reales Problem, bei dem diese Kombination aus Erfahrung, Diagnosefähigkeit, Modellbildung und Werkzeugen einen ungewöhnlich hohen Wert erzeugen könnte – und gibt es einen plausiblen Weg zu jemandem, der diesen Wert tatsächlich braucht?“**
