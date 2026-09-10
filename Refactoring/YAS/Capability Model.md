# Capability Model

## Fähigkeitsmodell für Problem-Radar

**Version 0.1**

---

# 1. Zweck

Dieses Dokument beschreibt die Fähigkeiten, Methoden, Werkzeuge und Arbeitspräferenzen des Akteurs, für den Problem-Radar nach passenden Problemsituationen sucht.

Es ist kein Lebenslauf.

Es beschreibt nicht primär:

- welche Technologien bekannt sind,
- welche Rollen bereits ausgeübt wurden,
- welche Branchen im Lebenslauf stehen,
- welche Stellenbezeichnungen passen könnten.

Es beschreibt vielmehr:

> **Welche Arten von Problemen kann dieser Akteur wahrscheinlich erkennen, verstehen oder lösen?**

Das Modell dient als semantische Grundlage für das Matching zwischen beobachteten Problemen und möglichen Interventionen.

---

# 2. Grundprinzip

Eine Fähigkeit ist mehr als eine Technologie oder ein Schlagwort.

Beispielsweise ist:

> Python

eine technische Kompetenz.

Dagegen ist:

> ein unbekanntes technisches System rekonstruieren und seine wesentlichen Strukturen sichtbar machen

eine Problemlösungsfähigkeit.

Für Problem-Radar sind insbesondere Fähigkeiten der zweiten Art relevant.

Das Fähigkeitsmodell unterscheidet daher mehrere Ebenen.

---

# 3. Fähigkeitsprofil

## 3.1 Technische Domänen

### Softwareentwicklung

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

---

### Softwarearchitektur

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

---

### Legacy-Systeme

Fähigkeiten:

- Einstieg in unbekannte oder schlecht dokumentierte Systeme
- Rekonstruktion historisch entstandener Strukturen
- Identifikation technischer Schulden
- Unterscheidung notwendiger Komplexität von historischer Komplexität
- schrittweises Refactoring
- Risikoabschätzung bei Änderungen
- Erhaltung vorhandener Funktionalität während struktureller Verbesserungen

---

### Performance und Parallelisierung

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

---

### Daten und Datenintegration

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

---

### Cloud, Infrastruktur und Automatisierung

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

---

### Compiler, Interpreter und formale Systeme

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

Besonders geeignet für Situationen, in denen Beteiligte viele Details kennen, aber das Gesamtbild verloren haben.

---

## 4.2 Rekonstruktion unbekannter Systeme

Fähigkeit, sich in Systeme einzuarbeiten, die:

- schlecht dokumentiert,
- historisch gewachsen,
- widersprüchlich,
- teilweise defekt,
- organisatorisch fragmentiert

sind.

Arbeitsweise:

1. Beobachtbare Strukturen identifizieren.
2. Abhängigkeiten rekonstruieren.
3. implizite Regeln herausarbeiten.
4. Widersprüche und Sonderfälle sammeln.
5. ein explizites Modell erzeugen.
6. Modell gegen das reale System prüfen.

---

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

---

## 4.4 Problemzerlegung

Fähigkeit, komplexe Probleme in möglichst unabhängige Teilprobleme zu zerlegen.

Bevorzugt werden Zerlegungen, bei denen:

- unterschiedliche Dimensionen getrennt bleiben,
- funktionale Redundanz gering ist,
- Abhängigkeiten explizit werden,
- Teilfragen separat bearbeitet werden können.

Besondere Aufmerksamkeit gilt vermischten Kategorien und scheinbaren Konflikten, die durch unterschiedliche Betrachtungsebenen entstehen.

---

## 4.5 Ursachenanalyse

Stärke bei Problemen, bei denen:

- Symptome bekannt sind,
- Ursache unklar ist,
- mehrere plausible Erklärungen existieren,
- lokale Reparaturen das Problem nur verschieben.

Bevorzugte Operationen:

- Hypothesen erzeugen
- Gegenhypothesen bilden
- Evidenz unterscheiden
- Kausalmodelle vergleichen
- Rückkopplungen untersuchen
- Systemgrenzen variieren
- zeitliche Dynamik berücksichtigen

---

## 4.6 Second Opinion

Geeignet als unabhängige Instanz für Situationen, in denen bereits:

- eine Architektur,
- ein Lösungsansatz,
- ein Konzept,
- eine technische Entscheidung,
- ein KI-Workflow,
- eine Analyse

vorliegt.

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

Explizierung dient insbesondere:

- Kommunikation
- Prüfung
- Vergleich
- Modifikation
- Wiederverwendung
- Automatisierung
- KI-Nutzung

---

## 5.2 Perspektivanalyse

Fähigkeit, unterschiedliche Perspektiven auf denselben Gegenstand auseinanderzuhalten.

Fragen:

- Welche Perspektive wird verwendet?
- Welche Systemgrenze wird vorausgesetzt?
- Welche Aspekte werden sichtbar?
- Welche bleiben unsichtbar?
- Welche anderen Perspektiven wären relevant?

Ziel ist nicht notwendig, eine Perspektive als falsch zu verwerfen.

Mehrere Perspektiven können gleichzeitig nützlich sein.

---

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

Solche Vermischungen können Scheinkonflikte und unlösbar wirkende Probleme erzeugen.

---

## 5.4 Annahmenanalyse

Fähigkeit, implizite Voraussetzungen sichtbar zu machen.

Untersucht werden:

- unausgesprochene Annahmen
- Standardannahmen
- verborgen gesetzte Systemgrenzen
- stillschweigende Zielgrößen
- vorausgesetzte Kausalmodelle

---

## 5.5 Widerspruchsanalyse

Unterscheidung verschiedener Arten scheinbarer Widersprüche:

- tatsächlicher logischer Widerspruch
- unterschiedliche Perspektive
- unterschiedliche Systemgrenze
- unterschiedlicher Zeithorizont
- unterschiedliche Zielsetzung
- unterschiedlicher Informationsstand
- unterschiedliche Begriffsverwendung

---

## 5.6 Blindstellenanalyse

Frage:

> Was kann innerhalb des aktuell verwendeten Modells kaum oder gar nicht gesehen werden?

Blindstellen können entstehen durch:

- Perspektive
- Sprache
- Organisationsstruktur
- Messgrößen
- Zielsysteme
- Gewohnheiten
- bestehende Tools
- Anreizstrukturen

---

## 5.7 Fragenrefactoring

Eine Frage wird nicht lediglich beantwortet.

Sie kann zunächst untersucht werden auf:

- versteckte Annahmen
- Kategorienmischungen
- unklare Begriffe
- falsche Systemgrenzen
- fehlende Perspektiven
- alternative Zerlegungen
- voreilige Lösungsannahmen

Ziel:

> Eine bessere bearbeitbare Frage erzeugen.

---

# 6. Eigene Methoden und epistemische Werkzeuge

## 6.1 Schnittwerk

Epistemische Architektur für:

- Fragen
- Perspektiven
- Problemräume
- epistemische Operatoren
- Analyse
- Refactoring
- Auditierbarkeit

Schnittwerk kann insbesondere dort eingesetzt werden, wo komplexe Problemräume strukturiert und unterschiedliche Betrachtungsweisen explizit gemacht werden müssen.

---

## 6.2 Brillenmodelle

Deklarative Spezifikationen bestimmter Perspektiven.

Eine Brille definiert beispielsweise:

- relevante Begriffe
- typische Fragen
- bevorzugte Relationen
- Diagnosekategorien
- Blindstellen

Anwendungsfall:

> Ein Problem systematisch durch mehrere unterschiedliche Perspektiven untersuchen.

---

## 6.3 Epistemische Operatoren

Wiederverwendbare Denkoperationen zur Bearbeitung von Problemräumen.

Beispiele:

- differenzieren
- Systemgrenze verändern
- Perspektive wechseln
- abstrahieren
- konkretisieren
- zerlegen
- Beziehungen explizieren
- Annahmen sichtbar machen
- Gegenmodell erzeugen

---

## 6.4 Epistemischer Linter

Analyse von:

- Fragen
- Prompts
- Argumentationen
- Anforderungen
- Entscheidungsgrundlagen

auf typische strukturelle Fehler oder Unklarheiten.

---

## 6.5 Diagnostischer Tutor

KI-gestütztes Lernverfahren, bei dem nicht primär Antworten geliefert, sondern Verständnisstrukturen diagnostiziert werden.

Potenzielle Anwendung:

- Bildung
- Weiterbildung
- Training
- Wissensdiagnose
- KI-gestütztes Lernen

---

## 6.6 Disput-Refactoring

Analyse festgefahrener Diskussionen.

Mögliche Operationen:

- Positionen zerlegen
- gemeinsame Annahmen identifizieren
- unterschiedliche Systemgrenzen sichtbar machen
- Zeithorizonte trennen
- Begriffe klären
- Sachfragen von Wertfragen unterscheiden

---

# 7. KI-bezogene Fähigkeiten

## 7.1 KI als kognitives Werkzeug

Fähigkeit, KI nicht nur als Textgenerator einzusetzen, sondern als:

- Analyseinstrument
- Strukturspiegel
- Perspektivmaschine
- diagnostisches Werkzeug
- Forschungsassistent
- Refactoring-System
- semantische Runtime

---

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

Mögliche Einsatzgebiete:

- Analyse
- Recherche
- Tutoring
- Diagnose
- Wissensarbeit
- Entscheidungsunterstützung

---

## 7.3 KI-Workflow-Diagnose

Potenzielle Interventionen:

- Bestehenden KI-Einsatz untersuchen
- schlechte Prompt-/Workflow-Strukturen erkennen
- Aufgaben sinnvoll zwischen Mensch und KI aufteilen
- implizite Anforderungen explizieren
- Output-Qualität diagnostizieren
- zuverlässigere Prüf- und Feedbackschleifen entwickeln

---

# 8. Typische Problemsituationen mit hohem Fit

Problem-Radar soll insbesondere aufmerksam werden, wenn folgende Muster auftreten.

## Technische Sackgasse

Ein Team versteht nicht mehr, warum ein System bestimmte Fehler produziert.

---

## Historisch gewachsene Komplexität

Ein System funktioniert noch, ist aber kaum noch veränderbar.

---

## Niemand versteht das Ganze

Viele Spezialisten kennen jeweils Teilbereiche, aber niemand besitzt ein belastbares Gesamtmodell.

---

## Wiederkehrende Reparaturen

Probleme werden regelmäßig lokal behoben, treten aber in anderer Form erneut auf.

---

## Schlechte oder widersprüchliche Architektur

Systembestandteile wurden über längere Zeit unabhängig voneinander entwickelt.

---

## Informations- oder Datenchaos

Mehrere Quellen, Pipelines oder Verantwortlichkeiten widersprechen sich.

---

## Unklare Anforderungen

Beteiligte diskutieren Lösungen, obwohl nicht klar ist, welches Problem eigentlich gelöst werden soll.

---

## Festgefahrene Entscheidung

Mehrere plausible Alternativen existieren und die Diskussion wiederholt sich.

---

## Festgefahrener Disput

Beteiligte widersprechen einander, möglicherweise jedoch aufgrund unterschiedlicher Perspektiven, Begriffe oder Systemgrenzen.

---

## Unbefriedigender KI-Einsatz

Eine Organisation verwendet KI, erhält aber:

- inkonsistente Ergebnisse
- oberflächliche Antworten
- schwer prüfbare Resultate
- zu viel manuelle Nacharbeit
- geringe Zuverlässigkeit

---

## Wissensproblem ohne offensichtliche technische Lösung

Menschen besitzen Informationen, können daraus aber keine gemeinsame, prüfbare Struktur erzeugen.

---

# 9. Besonders interessante Problemmuster

Problem-Radar soll einen Bonus vergeben, wenn mehrere der folgenden Bedingungen zusammentreffen:

- Problem ist strukturell statt rein operativ.
- Ursache ist unbekannt.
- vorhandene Lösungsversuche sind gescheitert.
- mehrere Domänen sind beteiligt.
- Problem wird falsch oder zu eng beschrieben.
- Beteiligte haben den Überblick verloren.
- unabhängige Analyse wäre wertvoll.
- ein begrenzter diagnostischer Eingriff könnte bereits großen Nutzen erzeugen.
- das Problem erfordert ungewöhnliche Kombinationen aus Technik und Modellbildung.
- KI könnte Teil der Lösung sein, aber nicht durch bloße Standardautomatisierung.

---

# 10. Mögliche Interventionstypen

## Diagnose

Beispiel:

> Analyse eines bestehenden Systems und Erstellung eines strukturellen Problemberichts mit Ursachenhypothesen und Handlungsoptionen.

---

## Architektur-Review

Beispiel:

> Unabhängige Prüfung einer bestehenden oder geplanten Architektur auf unnötige Komplexität, Kopplung, Risiken und Alternativen.

---

## Legacy-Rekonstruktion

Beispiel:

> Rekonstruktion eines schlecht dokumentierten Systems und Erstellung eines belastbaren Modells seiner tatsächlichen Struktur.

---

## Problem-Refactoring

Beispiel:

> Analyse einer festgefahrenen Problemstellung und Erzeugung einer klareren Zerlegung, Systemgrenze und Fragestellung.

---

## Entscheidungs-Refactoring

Beispiel:

> Explizierung von Annahmen, Kriterien, Perspektiven und Risiken einer schwierigen Entscheidung.

---

## KI-Workflow-Audit

Beispiel:

> Analyse eines bestehenden KI-Workflows und Entwicklung einer robusteren Aufgaben-, Prüf- und Feedbackstruktur.

---

## Epistemischer Audit

Beispiel:

> Untersuchung eines Analyse-, Entscheidungs- oder Wissensprozesses auf Blindstellen, Kategorienmischungen, implizite Annahmen und fehlende Perspektiven.

---

## Prototyp

Beispiel:

> Schneller experimenteller Aufbau eines KI-gestützten Werkzeugs zur Prüfung einer neuen Arbeitsweise.

---

# 11. Arbeitspräferenzen

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

---

## Weniger bevorzugt

- dauerhafte Teamaugmentation
- langfristige Vollzeitintegration in Scrum-Teams
- tägliche Statusrituale als zentraler Arbeitsmodus
- reine Ticketabarbeitung
- Routineimplementierung
- Wartung ohne strukturellen Gestaltungsspielraum
- Aufgaben, bei denen die Lösung vollständig vorgegeben ist und lediglich Arbeitskapazität benötigt wird

Diese Präferenzen sind keine absoluten Ausschlusskriterien.

Sie beeinflussen den Opportunity-Score.

---

# 12. Gute Auftragsform

Ein besonders passender Auftrag besitzt typischerweise folgende Form:

> „Wir haben ein schwieriges Problem und verstehen noch nicht vollständig, warum es entsteht. Schau dir das unabhängig an, rekonstruiere die relevante Struktur und sag uns, was du siehst.“

Weniger passend:

> „Wir haben bereits 427 Jira-Tickets spezifiziert und benötigen einen weiteren Entwickler zur Abarbeitung.“

---

# 13. Capability Matching

Problem-Radar bewertet nicht nur, ob eine Fähigkeit theoretisch anwendbar ist.

Es fragt:

1. Ist das Problem mit den vorhandenen Fähigkeiten tatsächlich bearbeitbar?
2. Gibt es einen ungewöhnlich guten Fit?
3. Ist die Kombination mehrerer Fähigkeiten relevant?
4. Kann daraus eine konkrete Intervention entstehen?
5. Ist diese Intervention zeitlich und organisatorisch realistisch?
6. Könnte ein anderer Standardanbieter das Problem offensichtlich besser lösen?

---

# 14. Kombinatorische Fähigkeiten

Besonders relevant sind Kombinationen.

Beispielsweise:

### Softwarearchitektur + epistemische Analyse

Geeignet für Probleme, bei denen nicht nur die technische Architektur, sondern auch das mentale Modell der Beteiligten fragmentiert ist.

### Legacy-Erfahrung + Rekonstruktion

Geeignet für Systeme, bei denen Dokumentation, Implementierung und Organisationswissen auseinandergefallen sind.

### KI + deklarative Spezifikation

Geeignet für Aufgaben, bei denen ein LLM systematisch nach bestimmten Regeln analysieren oder diagnostizieren soll.

### Refactoring + Problemzerlegung

Geeignet für Probleme, die bisher als monolithische Gesamtfrage behandelt wurden.

### technische Analyse + Perspektivwechsel

Geeignet für Konflikte zwischen technischen und organisatorischen Sichtweisen.

### Forschung + Prototyping

Geeignet für Probleme, bei denen noch unklar ist, ob eine Lösung überhaupt funktioniert.

---

# 15. Anti-Matching

Problem-Radar soll Kandidaten abwerten, wenn:

- lediglich zusätzliche Entwicklungskapazität gesucht wird,
- das Problem vollständig spezifiziert und routinemäßig ist,
- eine lange operative Einbindung zwingend erforderlich ist,
- das Problem überwiegend Vertrieb, Marketing oder Verwaltung betrifft,
- kein relevanter struktureller oder diagnostischer Anteil existiert,
- die benötigte Expertise klar außerhalb des Fähigkeitsprofils liegt,
- die mögliche Intervention keinen erkennbaren Vorteil gegenüber Standarddienstleistungen besitzt.

---

# 16. Explorationsregel

Das Modell darf nicht dazu führen, ausschließlich bekannte Einsatzgebiete zu finden.

Problem-Radar soll ausdrücklich auch nach Problemen suchen, bei denen:

> eine vorhandene Fähigkeit in einem bislang nicht betrachteten Kontext nützlich sein könnte.

Solche Treffer müssen als **exploratives Matching** gekennzeichnet werden.

Beispiel:

Eine Methode, die ursprünglich für Softwarearchitektur oder epistemisches Refactoring entwickelt wurde, könnte sich möglicherweise auf:

- Organisationsdiagnose
- Bildung
- Forschung
- Wissensmanagement
- Entscheidungsprozesse

übertragen lassen.

Die Übertragbarkeit ist dabei Hypothese, nicht Tatsache.

---

# 17. Meta-Fähigkeit

Über den einzelnen Fähigkeiten steht eine allgemeinere Fähigkeit:

> **Aus komplexen, historisch gewachsenen oder schlecht explizierten Zusammenhängen ein handhabbares Modell erzeugen.**

Diese Fähigkeit kann sich auf technische wie nichttechnische Gegenstände beziehen.

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

Diese Meta-Fähigkeit soll beim Matching berücksichtigt werden, darf aber niemals allein zur Behauptung führen, ein unbekanntes Fachproblem lösen zu können.

Domänenspezifische Grenzen bleiben bestehen.

---

# 18. Grenzen

Das Modell beschreibt keine universelle Problemlösungskompetenz.

Insbesondere gilt:

- Fachwissen bleibt relevant.
- Gute Strukturdiagnose ersetzt keine unbekannte Spezialexpertise.
- Hypothesen über neue Einsatzgebiete müssen getestet werden.
- epistemische Werkzeuge garantieren keine richtige Analyse.
- technisches Können bedeutet nicht automatisch wirtschaftliche oder organisatorische Kompetenz.
- ein hoher semantischer Fit ist noch kein Kundenbedarf.
- ein realer Bedarf bedeutet noch keine Zahlungsbereitschaft.

Problem-Radar muss diese Grenzen bei jeder Bewertung berücksichtigen.

---

# 19. Kurzprofil für Problem-Radar

Für schnelle Matching-Durchläufe kann folgende verdichtete Repräsentation verwendet werden:

> Seniorer Softwareentwickler und Systemanalytiker mit langjähriger Erfahrung in Softwarearchitektur, Legacy-Systemen, Datenintegration, Performance, Automatisierung und komplexen technischen Systemen. Besondere Stärke in der Rekonstruktion unbekannter oder historisch gewachsener Strukturen, Ursachenanalyse, Problemzerlegung und Refactoring. Zusätzlich Entwicklung epistemischer Methoden zur Explizierung von Annahmen, Perspektiven, Kategorien, Fragestellungen und Entscheidungsräumen sowie KI-gestützter Analyseverfahren. Bevorzugt begrenzte diagnostische, architektonische, forschende und prototypische Interventionen gegenüber langfristiger operativer Teamaugmentation.

---

# 20. Leitfrage

Beim Matching ist nicht zu fragen:

> „Passt dieser Auftrag zum bisherigen Berufsbild?“

Sondern:

> **„Gibt es hier ein reales Problem, bei dem diese Kombination aus Erfahrung, Diagnosefähigkeit, Modellbildung und Werkzeugen einen ungewöhnlich hohen Wert erzeugen könnte?“**