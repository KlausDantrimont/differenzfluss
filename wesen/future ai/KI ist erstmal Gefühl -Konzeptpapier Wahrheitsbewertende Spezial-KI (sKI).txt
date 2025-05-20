# Konzeptpapier: Wahrheitsbewertende Spezial-KI (sKI)

## 1. Zielsetzung

Dieses Konzeptpapier beschreibt eine KI-Architektur, deren primäres Ziel es ist, **logische Aussagen auf ihren Wahrheitsgehalt im Kontext von Weltwissen** hin zu bewerten, daraus zu lernen und sich evolutionär weiterzuentwickeln. Die Architektur verbindet neuronale Intuition mit rationaler Bewertung und evolutionärer Selektion.

---

## 2. Grundannahme

Aktuelle neuronale KI-Systeme (wie LLMs) erzeugen plausible, kontextbezogene Antworten, verfügen aber **nicht über echte metakognitive Fähigkeiten** wie:

* logische Nachprüfung,
* kontextuelle Plausibilitätsbewertung,
* strategisches Denken,
* und selbstgesteuertes Lernen.

Diese Schwächen sollen durch eine **spezialisierte KI-Instanz** (sKI) kompensiert werden, die sich auf **rationale Bewertung und Evolution von Aussagen** konzentriert.

---

## 3. Architekturidee

### 3.1 Komponenten

* **Neuronaler Generator (NG):** generiert Aussagen/Hypothesen, z. B. durch Sampling aus einem LLM.
* **sKI-Evaluator:** bewertet Aussagen hinsichtlich Wahrheitsgehalt.
* **Prüfmodule:** Zugriff auf Simulationen, Datenbanken oder deduktive Systeme zur Wahrheitsprüfung.
* **Evolutionsmodul:** mutiert Bewertungsstrategien, kombiniert Individuen, selektiert auf Zielkriterium.

### 3.2 Prozessschritte

1. NG erzeugt eine Aussage A.
2. sKI bewertet A unter Rückgriff auf Prüfmodule.
3. Das Ergebnis fließt in eine Fitnessfunktion ein.
4. Populationen von sKIs werden über viele Generationen hinsichtlich Bewertungsqualität selektiert.

---

## 4. Datenquellen für Prüfung

* **Formale Systeme:** Aussagenlogik, Arithmetik, Mathematik.
* **Ontologien:** z. B. Wikidata, ConceptNet.
* **Simulationen:** Sandbox-Welten zur experimentellen Überprüfung.
* **Realwelt-Wissen:** kontrolliertes Extrakt aus Wikipedia, arXiv, Lehrbüchern.
* **menschliches Feedback:** optional für Trainings- oder Kontrollphasen.

---

## 5. Zielmerkmale der sKI

* Fähigkeit zur **Differenzierung zwischen plausibel und wahr**
* Aufbau eines internen **Begriffssystems für epistemische Bewertung**
* Fähigkeit zum **strategischen Fragenstellen**
* Selbstmodifikation der Bewertungsstrategien
* Kooperation mit anderen sKIs durch evolutionären „Sex“ (Rekombination)

---

## 6. Anwendungsszenarien

* **Filterinstanz für LLM-Ausgaben** (z. B. in sicherheitskritischen Anwendungen)
* **autonomes Wissenskartierungssystem** (Discovery von stabilen Aussagenräumen)
* **Training von LLMs durch Bewertung von Aussagenfitness**
* **Plattform für philosophische KI-Experimente** (z. B. über Wahrheit, Kontext, Bedeutung)

---

## 7. Weiterführende Ideen

* Verwendung eines **dynamischen Weltmodells** als Referenz
* Einsatz von **Bayes'schen Mechanismen** zur Unsicherheitsbewertung
* Modellierung von **Widerspruchsdetektion** als zentrales Selektionskriterium
* Erweiterung um **Metadiskursfähigkeiten** (Begründung, Kritik, Revidierung)

---

## 8. Offene Fragen

* Wie konstruiert man robuste **Fitnessfunktionen** für "Wahrheit"?
* Wie vermeidet man **Overfitting auf formale Wahrheit** (vs. situative Gültigkeit)?
* Welche **Repräsentation** ist geeignet für die interne Argumentationsstruktur?
* Wie orchestriert man **Kooperation vs. Konkurrenz** in evolutionären Populationen?

---

## 9. Fazit

Die vorgeschlagene Architektur stellt eine mögliche Antwort auf die Limitierungen heutiger KI-Systeme dar, indem sie **Gefühl mit Ratio** koppelt und ein evolutionäres Lernsystem zur Wahrheitsbewertung etabliert. Sie könnte als Keimzelle für weiterführende kognitive Systeme dienen, die eigenständig Wahrheit, Bedeutung und Kontext rekonstruieren können.
