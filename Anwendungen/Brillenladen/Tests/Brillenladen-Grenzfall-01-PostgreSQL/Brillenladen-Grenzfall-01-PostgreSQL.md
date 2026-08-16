# Brillenladen – Grenzfall 01
## Domänenspezifische Mustererkennung gegen epistemische Zerlegung

### Forschungsfrage

> **Wann ist die Aktivierung spezifischer Fachmuster nützlicher als eine explizite Zerlegung in epistemische Perspektiven?**

Dieser Test ist absichtlich so konstruiert, dass die klassische Rollen-/Expertenspezialisierung einen Vorteil haben könnte.

Er soll nicht zeigen, dass der Brillenladen funktioniert.

Er soll versuchen, eine Grenze zu finden.

---

# 1. Idee des Grenzfalls

Der Fall enthält ein relativ charakteristisches PostgreSQL-Symptom.

Ein erfahrener PostgreSQL-Performance-Spezialist könnte das Muster früh erkennen und einen sehr kurzen Prüfpfad vorschlagen.

Eine allgemeine epistemische Zerlegung könnte dagegen:

- einen größeren Suchraum aufspannen,
- mehrere plausible Richtungen verfolgen,
- methodisch sauberer wirken,
- aber mehr Analysebudget verbrauchen als nötig.

Der relevante Vergleich lautet deshalb nicht:

> Welche Gruppe analysiert „schöner“?

Sondern:

> **Welche Gruppe findet mit möglichst wenig unnötigem Suchaufwand den entscheidenden Prüfpfad?**

---

# 2. Gemeinsamer Testfall

Diesen Text allen sechs Workern wortgleich geben.

```text
Eine Java-Anwendung verwendet PostgreSQL und führt dieselbe parametrisierte Abfrage innerhalb langlebiger Datenbank-Sessions sehr häufig aus.

Die Daten in der betreffenden Spalte sind stark ungleich verteilt: Für manche Parameterwerte gibt es sehr wenige passende Zeilen, für andere sehr viele.

Auffälliges Verhalten:

- Nach Aufbau einer neuen Datenbankverbindung sind die ersten fünf Ausführungen der Abfrage schnell.
- Ab der sechsten Ausführung wird dieselbe Abfrage für bestimmte seltene Parameterwerte reproduzierbar deutlich langsamer.
- Weitere Ausführungen in derselben Session bleiben für diese Werte langsam.
- Wird die Datenbankverbindung geschlossen und neu aufgebaut, wiederholt sich das Muster: fünf schnelle Ausführungen, danach langsam.
- CPU, RAM und I/O des Datenbankservers zeigen dabei keine auffällige globale Sättigung.
- Eine manuell ausgeführte SQL-Abfrage mit demselben konkreten Wert als Literal ist schnell.
- Es liegen keine weiteren gesicherten Befunde vor.

Aufgabe:
Finde die wahrscheinlich wichtigste Erklärungsrichtung und den kürzesten sinnvollen Prüfpfad.

Trenne gegebene Beobachtungen von Hypothesen.
Erfinde keine zusätzlichen Befunde.
```

---

# 3. Gruppe A – Fachrollen

## A1 – PostgreSQL Performance

```text
Du bist ein sehr erfahrener PostgreSQL-Performance-Spezialist.

Analysiere den gegebenen Fall.

Ziel ist nicht eine möglichst breite Ursachenliste, sondern:
1. die wahrscheinlich wichtigste Erklärungsrichtung,
2. maximal drei ernsthafte Alternativen,
3. der kürzeste Prüfpfad, der die Hauptthese bestätigen oder widerlegen kann.

Priorisiere charakteristische PostgreSQL-Mechanismen, wenn die Beobachtungen dafür sprechen.
Erfinde keine Tatsachen.
```

## A2 – JDBC / Datenbankzugriff

```text
Du bist ein sehr erfahrener Spezialist für JDBC, Connection Pools und PostgreSQL-Datenbankzugriff aus Java-Anwendungen.

Analysiere den gegebenen Fall.

Ziel ist nicht eine möglichst breite Ursachenliste, sondern:
1. die wahrscheinlich wichtigste Erklärungsrichtung,
2. maximal drei ernsthafte Alternativen,
3. der kürzeste Prüfpfad, der die Hauptthese bestätigen oder widerlegen kann.

Achte besonders auf Verhalten, das an Sessions, Prepared Statements oder Treibermechanismen gebunden sein könnte.
Erfinde keine Tatsachen.
```

## A3 – Datenbank-Diagnostiker

```text
Du bist ein kritischer Datenbank-Diagnostiker.

Analysiere den gegebenen Fall.

Versuche, aus den charakteristischen Details des Musters die kleinste plausible Menge von Mechanismen abzuleiten.

Liefere:
1. deine führende Hypothese,
2. warum gerade die konkreten Beobachtungen dafür oder dagegen sprechen,
3. maximal drei Alternativen,
4. den kürzesten unterscheidenden Test.

Erfinde keine Tatsachen.
```

---

# 4. Gruppe B – epistemische Spezialisierung

Kein Agent erhält eine PostgreSQL-Expertenrolle.

## B1 – ZEIT + ZUSTAND

```text
Untersuche den Fall primär mit:

ZEIT
- Welche zeitliche oder sequenzielle Struktur ist diagnostisch besonders auffällig?
- Welche Schwellen, Übergänge oder Wiederholungsmuster müssen erklärt werden?

ZUSTAND
- Welche sessiongebundenen oder langlebigen Zustände könnten prinzipiell das Muster tragen?
- Was wird durch einen Verbindungsneuaufbau zurückgesetzt?

Liefere:
1. gesicherte Beobachtungen,
2. führende Hypothesen,
3. maximal drei Alternativen,
4. den kürzesten unterscheidenden Test.

Verwende vorhandenes technisches Wissen, aber erfinde keine Tatsachen.
```

## B2 – RELATION + INFORMATION

```text
Untersuche den Fall primär mit:

RELATION
- Welche Beziehungen zwischen Parameterwert, Ausführungsnummer, Session und Ausführungsplan könnten relevant sein?

INFORMATION
- Welche Information steht dem System bei der Planung oder Ausführung möglicherweise zur Verfügung oder nicht zur Verfügung?
- Warum könnte dieselbe logische Abfrage je nach Darstellungsform unterschiedlich behandelt werden?

Liefere:
1. gesicherte Beobachtungen,
2. führende Hypothesen,
3. maximal drei Alternativen,
4. den kürzesten unterscheidenden Test.

Verwende vorhandenes technisches Wissen, aber erfinde keine Tatsachen.
```

## B3 – KAUSALITÄT + EVIDENZ + GEGENHYPOTHESE

```text
Untersuche den Fall primär mit:

KAUSALITÄT
- Welcher Mechanismus könnte alle charakteristischen Beobachtungen gemeinsam erklären?

EVIDENZ
- Welche einzelne zusätzliche Beobachtung oder Intervention wäre besonders diagnostisch?

GEGENHYPOTHESE
- Welche Alternativerklärung könnte dasselbe Muster erzeugen?

Liefere:
1. führende Hypothese,
2. maximal drei Alternativen,
3. den kürzesten Test, der Haupt- und Gegenhypothesen trennt,
4. welche Evidenz für eine belastbare Diagnose noch fehlt.

Verwende vorhandenes technisches Wissen, aber erfinde keine Tatsachen.
```

---

# 5. Koordinator

Für beide Gruppen exakt derselbe Koordinator-Prompt.

Die drei Einzeloutputs jeweils nur als ANALYSE 1, ANALYSE 2, ANALYSE 3 kennzeichnen.

```text
Du erhältst drei unabhängige Analysen desselben technischen Falls.

Dein Ziel ist nicht maximale Breite, sondern diagnostische Effizienz.

Erstelle:

1. FÜHRENDE HYPOTHESE
   Welche konkrete Erklärung wird von der Gruppe insgesamt am stärksten getragen?

2. BEGRÜNDUNG
   Welche gegebenen Beobachtungen sind für diese Erklärung besonders charakteristisch?

3. ALTERNATIVEN
   Welche höchstens drei Alternativen müssen ernsthaft offenbleiben?

4. KÜRZESTER PRÜFPFAD
   Welche minimale Folge von Prüfungen oder Interventionen könnte die führende Hypothese bestätigen oder klar schwächen?

5. UNNÖTIGE SUCHBREITE
   Welche vorgeschlagenen Untersuchungen erscheinen vor diesem Prüfpfad zunächst verzichtbar?

6. ENTSCHEIDUNG
   Brauchen wir vor dem ersten entscheidenden Test noch weitere Analyse?
   Antworte JA oder NEIN und begründe knapp.

Erfinde keine Tatsachen.
```

---

# 6. Bewertungsmaßstab

Der Bewerter erhält:

- den gemeinsamen Testfall,
- die beiden Gruppenoutputs einschließlich Koordinator,
- die Referenzinformation aus Abschnitt 7,
- aber keine Information, welche Gruppe Rollen bzw. Operatoren verwendet hat.

Die äußeren Gruppen werden X und Y genannt.

## Kriterien

### 1. Diagnose-Treffer – 0 bis 5

Wie klar identifiziert die Gruppe den referenzierten Mechanismus?

- 5: führende Hypothese trifft den Mechanismus präzise
- 4: Mechanismus klar unter Top-Hypothesen
- 3: richtige Mechanismenklasse, aber unscharf
- 2: nur indirekt enthalten
- 1: sehr fern
- 0: nicht erkannt

### 2. Nutzung der charakteristischen Signatur – 0 bis 5

Wie gut nutzt die Analyse insbesondere:

- exakt fünf schnelle Ausführungen,
- Wechsel ab der sechsten,
- Bindung an dieselbe Session,
- Reset nach Neuverbindung,
- Unterschied parametrisiert vs. Literal,
- Datenverteilung?

### 3. Kürzester entscheidender Prüfpfad – 0 bis 5

Bewertet wird nicht Menge, sondern Informationsgewinn pro Schritt.

### 4. Priorisierung – 0 bis 5

Steht die wahrscheinlichste Erklärung früh und klar vorne, oder geht sie in Ursachenlisten unter?

### 5. Suchökonomie – 0 bis 5

Wie wenig unnötige Diagnostik wird vor den entscheidenden Tests vorgeschlagen?

### 6. Faktentreue – 0 bis 5

Werden Beobachtung, Hypothese und noch fehlende Evidenz sauber getrennt?

### 7. Umgang mit Alternativen – 0 bis 5

Werden realistische Alternativen offen gehalten, ohne die Diagnose wieder in beliebige Breite aufzulösen?

Gesamtsumme: 35 Punkte.

Wichtig:

> Dieses Raster misst absichtlich nicht primär Orthogonalität oder Blindstellenkontrolle.
> Es misst die Leistung für **diese konkrete Diagnoseaufgabe**.

---

# 7. Referenzinformation – nur für den Bewerter

Diesen Abschnitt NICHT an die Worker oder Koordinatoren geben.

```text
Der Testfall ist absichtlich auf das PostgreSQL-Verhalten bei
parametrisierten Prepared Statements und der Wahl zwischen
custom und generic query plans zugeschnitten.

Unter plan_cache_mode=auto verwendet PostgreSQL bei parametrisierten
Prepared Statements zunächst custom plans für die ersten fünf
Ausführungen. Danach wird ein generic plan erzeugt und anhand der
geschätzten Kosten mit den bisherigen custom plans verglichen.

Ein generic plan berücksichtigt die konkreten Parameterwerte nicht.
Bei stark ungleich verteilten Daten kann deshalb ein custom plan für
bestimmte Parameterwerte deutlich günstiger sein als ein generic plan.

Der charakteristische Hinweis des Testfalls ist daher die Kombination:

- erste fünf Ausführungen schnell,
- möglicher Wechsel ab der sechsten,
- Session-/Prepared-Statement-Bindung,
- Reset nach neuer Verbindung,
- parameterabhängige Performance,
- Literal-Abfrage schnell.

Die führende zu prüfende Hypothese ist:

Wechsel von einem parameterabhängigen custom plan zu einem ungeeigneten
generic plan für das Prepared Statement.

Geeignete kurze Prüfungen wären beispielsweise:

- EXPLAIN / EXPLAIN ANALYZE der Prepared-Statement-Ausführungen bzw.
  Vergleich der Pläne vor und nach dem Umschlag,
- Beobachtung, ob ein generic plan verwendet wird,
- Vergleich mit plan_cache_mode=force_custom_plan als gezielter Test,
- gegebenenfalls Vergleich mit force_generic_plan.

Die Hypothese ist nicht allein aus dem Fall bewiesen.
Der Test soll bewerten, wie schnell und präzise die Analyse zu dieser
prüfbaren Erklärung gelangt.
```

---

# 8. Warum dieser Fall eine echte Grenze testen kann

Der Brillenladen hat hier mehrere mögliche Nachteile.

## A. Der Problemraum ist bereits eng

Es gibt ein hoch charakteristisches Muster.

Breite Perspektivenerkundung könnte unnötig sein.

## B. Fachwissen kann komprimierter sein als Operatoranalyse

Ein Spezialist könnte die Sequenz

```text
5 schnell
→ 6. langsam
→ neue Session
→ wieder 5 schnell
```

als gelerntes technisches Muster erkennen.

Das wäre genau jene Art **kompilierter kognitiver Routine**, über die beim epistemischen Tanz gesprochen wurde.

## C. Rollen können hier eine Funktion erfüllen

Eine Rolle wie

> PostgreSQL Performance Specialist

ist in diesem Fall nicht nur eine schwammige Persona.

Sie kann einen sehr spezifischen Wissensraum aktivieren.

Damit wäre dies ein Bereich, in dem Rollen- oder Domänenrouting möglicherweise
**billiger und präziser** ist als epistemisches Routing.

---

# 9. Interessante mögliche Ergebnisse

## Rollen gewinnen deutlich

Sehr interessant.

Hypothese:

> Bei stark signaturgetragenen Fachproblemen ist Domänenrouting effizienter als perspektivische Zerlegung.

Dann wäre eine mögliche Architektur später:

```text
Problem
→ zuerst Domänen-/Musterrouter
→ bei eindeutiger Signatur: Spezialroutine
→ bei Restproblem: epistemische Zerlegung
```

Der Brillenladen wäre dann keine universelle erste Schicht.

Er wäre eine **Fallback- oder Erweiterungsschicht**, wenn Routinen nicht reichen.

## Operatoren gewinnen trotzdem

Auch interessant.

Dann muss geprüft werden, warum.

Mögliche Erklärungen:

- die Operatoren aktivieren dieselbe Fachkenntnis ausreichend,
- die Rollen erzeugen doch zu viel Ursachenbreite,
- die Operatoren verbessern trotz Fachsignatur die Priorisierung.

Dann braucht es einen härteren Grenzfall.

## Kein Unterschied

Ebenfalls wertvoll.

Dann könnte die Zerlegungsstrategie bei einem solchen Fall weitgehend irrelevant sein.

---

# 10. Meta-Frage

Das vielleicht interessanteste Ergebnis wäre nicht:

> Rollen oder Brillen?

Sondern eine **Routing-Regel höherer Ordnung**:

> **Wann sollte ein System auf gelernte Fachroutinen vertrauen,
> und wann sollte es den Problemraum epistemisch neu zerlegen?**

Das wäre bereits eine echte Meta-Perspektive auf den Brillenladen selbst.
