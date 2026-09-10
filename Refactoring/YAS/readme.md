# YAS

## Yet Another Sense

**YAS** ist ein Entwurf für eine verteilte epistemische Infrastruktur.

Die Ausgangsidee war einfach:

> KI kann öffentliche und private Informationsquellen beobachten und auf relevante Veränderungen untersuchen.

Daraus entstand die Vorstellung eines zusätzlichen „Sinnes“:

Ein System, das nicht nur Daten sammelt, sondern Fragen an die Welt richtet.

Inzwischen ist daraus mehr geworden.

YAS kann als Netzwerk gedacht werden, in dem:

* Quellen beobachtet werden,
* Fragestellungen als ausführbare Skripte vorliegen,
* Perspektiven und epistemische Modelle auf Quellen angewandt werden,
* Bedingungen Ereignisse auslösen,
* Nutzer bestimmte Erkenntnisleistungen abonnieren,
* Auswertungen wiederverwendet werden, solange ihre Grundlagen unverändert bleiben,
* und strukturell verwandte Gedanken oder Untersuchungen miteinander verbunden werden können.

Kurz:

> **YAS ist kein Feedreader.
> Es ist ein Netz für abonnierbare Erkenntnisprozesse.**

---

## Grundidee

Klassische Informationssysteme liefern Inhalte.

Ein Newsletter liefert einen Newsletter.
Ein RSS-Feed liefert neue Einträge.
Eine Suchmaschine liefert Treffer.

YAS setzt eine zusätzliche Verarbeitungsschicht dazwischen.

Nicht nur:

```text
Quelle
→ Nutzer
```

sondern:

```text
Quelle
→ Frage
→ Perspektive
→ Prüfung
→ Bedingung
→ Ausgabe oder Aktion
```

Dadurch wird aus einem Informationsabonnement ein:

> **Erkenntnisabonnement**

---

## Beispiel

Ein Nutzer könnte konfigurieren:

```text
Quelle:
    Newsletter X

Fragen:
    Was hat sich verändert?
    Welche neuen Behauptungen werden aufgestellt?
    Welche Evidenz wird genannt?

Brillen:
    Anreize
    Systemgrenzen
    Langfristige Folgen

Bedingung:
    Nur melden, wenn etwas wesentlich Neues auftaucht
    oder eine frühere Annahme fraglich wird.

Aktion:
    Kurzbericht erzeugen
    und auf die Originalquelle verweisen.
```

Der Nutzer abonniert damit nicht einfach den Newsletter.

Er abonniert eine **bestimmte Erkenntnisleistung auf diesem Newsletter**.

---

## Epistemische Skripte

Eine zentrale Einheit in YAS ist das **epistemische Skript**.

Ein epistemisches Skript beschreibt, was eine KI mit einem Gegenstand tun soll.

Beispiele:

* Welche wesentlichen Veränderungen gab es?
* Welche Behauptungen sind neu?
* Welche Annahmen tragen diese Argumentation?
* Welche Gruppen wären betroffen?
* Welche Gegenhypothesen sind plausibel?
* Wo widersprechen sich zwei Quellen?
* Welche Risiken entwickeln sich?
* Welche bekannten Blindstellen werden relevant?

Solche Skripte können:

* einmalig verwendet,
* gespeichert,
* geteilt,
* kombiniert,
* auf verschiedene Quellen angewandt,
* und automatisch ausgelöst werden.

Sie sind damit keine bloßen Prompts.

Sie können zu **wiederverwendbaren epistemischen Objekten** werden.

---

## Brillenmodelle

YAS kann auf die Perspektiven und Operatoren des **Schnittwerks** zurückgreifen.

Eine Brille beschreibt eine bestimmte Art des Betrachtens.

Beispiele:

* Evidenz
* Anreize
* Macht
* Systemgrenzen
* zeitliche Dynamik
* Verteilungswirkungen
* Risiko
* Framing
* Gegenmodelle
* Blindstellen

Brillenmodelle könnten als eigenständige Module gespeichert und referenziert werden.

Ein epistemisches Skript müsste dann nicht alle Regeln selbst enthalten.

Es könnte beispielsweise sagen:

```text
Wende auf diese Quelle an:

- Evidenz-Brille
- Anreiz-Brille
- Langfrist-Brille
```

Damit entsteht eine Bibliothek wiederverwendbarer Erkenntnisoperationen.

---

## Epistemisches Pub/Sub

Technisch ähnelt YAS einem Publish/Subscribe-System.

Aber abonniert werden nicht nur Topics oder Inhalte.

Abonniert werden Kombinationen aus:

```text
Quelle
+
Fragestellung
+
Perspektive
+
Bedingung
+
Aktion
```

Man könnte das als **epistemisches Pub/Sub** verstehen.

Beispiele:

> Beobachte Gesetzgebung zum Thema X und melde mir Änderungen, die aus Sicht kleiner Unternehmen neue Belastungen erzeugen könnten.

> Prüfe Veröffentlichungen zu Thema Y auf Evidenzqualität und benachrichtige mich, wenn eine bisher tragende Annahme angegriffen wird.

> Vergleiche die Aussagen dieser drei Akteure und melde nur substanzielle Widersprüche.

Die eigentliche Einheit des Abonnements ist damit nicht Information.

Sie ist eine **gewünschte Erkenntnisoperation**.

---

## Grundprinzipien

### Ereignisgetriebene Auswertung

YAS wertet nicht permanent alles neu aus.

Eine Auswertung erfolgt:

* auf Anfrage,
* wenn eine Bedingung geprüft werden muss,
* oder wenn sich eine relevante Abhängigkeit verändert hat.

Bleiben Quelle, Skript und verwendete Brillen unverändert, bleibt auch eine bestehende Auswertung gültig.

```text
Quelle v17
+ Skript v3
+ Brille v5
→ Auswertung A

keine Änderung
→ A bleibt gültig

Quelle v18
→ A ist potenziell veraltet
→ bei Bedarf neu auswerten
```

YAS behandelt Erkenntnisleistungen damit ähnlich wie andere abgeleitete Artefakte:

> **berechnen, speichern, Abhängigkeiten beobachten, bei Änderung invalidieren.**

---

### Human in the Loop

Semantische oder strukturelle Verwandtschaft ist kein endgültiges Urteil.

Wenn eine KI zwei Gedanken, Modelle oder Untersuchungen für verwandt hält, kann sie diese Beziehung als Hypothese anbieten.

Bei Unsicherheit entscheidet der Mensch, der die Suche oder Kopplung initiiert hat.

Zum Beispiel:

> „Ich sehe hier möglicherweise dieselbe Problemstruktur unter anderem Vokabular. Ist diese Verbindung für deine Suche relevant?“

Damit muss Unsicherheit nicht vollständig automatisiert aufgelöst werden.

Sie kann an den zuständigen Menschen zurückgegeben werden.

---

### Explizite Sichtbarkeit

Nicht jedes epistemische Objekt muss öffentlich sein.

Objekte können beispielsweise sein:

* lokal,
* privat,
* mit ausgewählten Teilnehmern geteilt,
* oder öffentlich.

Eine unveröffentlichte Idee wird nicht dadurch geschützt, dass ein öffentliches Netz besondere Magie betreibt.

Sie wird geschützt, indem sie **nicht veröffentlicht wird**.

YAS sollte daher Sichtbarkeit explizit modellieren und nicht mit Persistenz oder Replikation verwechseln.

---

### Provenienz und Historie

Persistierte epistemische Objekte können eine nachvollziehbare Geschichte besitzen.

Dazu gehören beispielsweise:

```text
Objekt
Autor oder Schlüssel
Zeitstempel
Version
Vorgänger
Hash
Signatur
```

Damit könnte bei Bedarf rekonstruiert werden:

* wann eine Idee erstmals persistiert wurde,
* wie sie sich verändert hat,
* welche Version auf welche zurückgeht,
* welche Vorläufer existierten,
* und welche Autoren beteiligt waren.

Das ist kein automatischer Urheberrechtsentscheid.

Es schafft aber eine technische Grundlage für **Provenienz und Prioritätsrekonstruktion**, sofern Autorenzuordnung und Zeitstempel hinreichend manipulationssicher sind.

---

### Dezentrale Replikation

YAS ist nicht zwingend als zentrale Plattform gedacht.

Ein möglicher Grundaufbau ist ein Netzwerk von Knoten, die Objekte replizieren und synchronisieren.

Wer Ressourcen beitragen möchte, kann einen weiteren Rechner bereitstellen.

Dieser kann sich im Netz bekannt machen und ausgewählte Daten oder Dienste übernehmen.

Ein Knoten muss dabei nicht das gesamte Netz speichern.

Er kann beispielsweise nur halten:

* eigene lokale Objekte,
* abonnierte Objekte,
* öffentliche Daten bestimmter Bereiche,
* gecachte Auswertungen,
* oder replizierte Objekte, die er für andere bereitstellt.

```text
YAS-Knoten
│
├── lokale/private Objekte
├── abonnierte replizierte Objekte
├── eigene Skripte und Brillen
├── gecachte Auswertungen
└── öffentliche/geteilte Objekte
          │
          ↕ Sync
     andere Knoten
```

Damit entsteht eher ein **repliziertes epistemisches Netz** als ein einzelner zentraler KI-Dienst.

---

## Soziale Ebene

YAS könnte außerdem Erkenntnisprozesse verschiedener Menschen miteinander verbinden.

Heute finden Menschen einander meistens über:

* gemeinsame Themen,
* Institutionen,
* soziale Netzwerke,
* Suchbegriffe,
* Bekanntheit,
* Zufall.

Zwei Personen können jedoch an strukturell ähnlichen Problemen arbeiten und völlig unterschiedliche Begriffe verwenden.

KI kann solche Verwandtschaften möglicherweise erkennen.

Ein System könnte beispielsweise feststellen:

> Zwei unabhängige Untersuchungen verwenden verschiedene Begriffe, bearbeiten aber eine sehr ähnliche Problemstruktur.

Oder:

> Eine veröffentlichte Brille adressiert genau eine Blindstelle eines anderen Modells.

Oder:

> Mehrere Menschen stellen unabhängig dieselbe strukturelle Frage in verschiedenen Domänen.

Mit Zustimmung der Beteiligten könnte YAS daraus einen gemeinsamen Resonanzraum eröffnen.

Die KI wäre dabei nicht primär Autor.

Sie wäre:

> **epistemischer Router**

---

## Knoten im Netz

Ein YAS-Netz könnte verschiedene Knotentypen enthalten:

### Quellen

* Websites
* Newsletter
* RSS-Feeds
* Datenbanken
* Dokumente
* öffentliche Datensätze
* Repositories
* Foren
* persönliche Informationsquellen

### Fragen

Explizite Untersuchungsinteressen.

### Epistemische Skripte

Ausführbare Analyseverfahren.

### Brillen

Wiederverwendbare Perspektiven und Operatoren.

### Auswertungen

Persistierte Ergebnisse epistemischer Operationen einschließlich ihrer Abhängigkeiten.

### Signale

Erkannte Veränderungen, Widersprüche oder andere relevante Ereignisse.

### Bedingungen

Regeln dafür, wann etwas relevant wird.

### Aktionen

Zum Beispiel:

* melden,
* zusammenfassen,
* vergleichen,
* archivieren,
* eine weitere Analyse starten,
* einen Menschen oder Agenten einbeziehen.

### Menschen

Teilnehmer, Autoren, Beobachter, Prüfer und Empfänger.

### Rechner

Knoten, die Daten replizieren, Auswertungen durchführen oder Dienste im Netz bereitstellen.

---

## Verhältnis zu Schnittwerk

**Schnittwerk** und **YAS** sind Schwesterprojekte.

Schnittwerk beschäftigt sich mit:

* epistemischen Schnitten,
* Perspektiven,
* Operatoren,
* Refactoring,
* Problemräumen,
* Audit.

YAS beschäftigt sich mit:

* Quellen,
* Ereignissen,
* Netzwerken,
* Abonnements,
* Automatisierung,
* Persistenz,
* Replikation,
* Verteilung,
* sozialer Vermittlung.

Kurz:

> **Schnittwerk ist die epistemische Maschine.
> YAS ist das Netz, in dem sie laufen kann.**

YAS muss Schnittwerk dabei nicht zwingend voraussetzen.

Aber Schnittwerk kann YAS eine explizite Sprache für epistemische Operationen liefern.

---

## Technischer Status

Die meisten notwendigen technischen Bausteine existieren bereits:

* Sprachmodelle,
* Embeddings,
* semantische Suche,
* RSS und APIs,
* Agentensysteme,
* Ereignisverarbeitung,
* Publish/Subscribe,
* Trigger,
* Content-Addressing,
* digitale Signaturen,
* verteilte Speicherung,
* Replikation,
* Knowledge Graphs,
* Workflow-Systeme.

YAS behauptet deshalb nicht, neue technische Primitive zu erfinden.

Die offene Frage ist vielmehr:

> **Was entsteht, wenn diese vorhandenen Bausteine als epistemische Infrastruktur zusammengesetzt werden?**

Der mögliche eigene Beitrag liegt in der Architektur:

* Erkenntnisleistungen als abonnierbare Einheiten,
* epistemische Skripte als wiederverwendbare Objekte,
* Brillen als portable Perspektivmodelle,
* ereignisgetriebene und wiederverwendbare Auswertungen,
* nachvollziehbare Provenienz epistemischer Objekte,
* dezentrale Replikation,
* KI-vermitteltes Routing zwischen verwandten Erkenntnisprozessen.

---

## Offene Fragen

YAS ist weiterhin ein Forschungs- und Entwurfsraum.

Offen ist unter anderem:

* Wie werden epistemische Skripte formal oder halbformal beschrieben?
* Welche Teile sollten standardisiert sein?
* Wie werden Brillen referenziert, versioniert und kombiniert?
* Wie fein müssen Abhängigkeiten einer Auswertung erfasst werden?
* Wann genau gilt eine Auswertung als invalidiert?
* Wie werden Relevanz und Dringlichkeit gewichtet?
* Wie funktionieren epistemische Budgets?
* Welche Vertrauensmodelle braucht ein dezentrales Netz?
* Welche Objekte sollten repliziert werden und nach welchen Regeln?
* Wie werden widersprüchliche Versionen zusammengeführt?
* Wie verhindert man Filterblasen trotz personalisierter epistemischer Abonnements?
* Wie werden Zustimmung und Privatsphäre bei sozialer Vermittlung behandelt?
* Welche Provenienzdaten müssen öffentlich sein, welche können privat bleiben?
* Wann ist menschliche Prüfung zwingend erforderlich?
* Welche Sicherheitsgrenzen gelten für automatisch ausgelöste Aktionen?

---

## Forschungsrichtung

YAS begann als zusätzliche Sensorik.

Inzwischen zeichnet sich eine allgemeinere Möglichkeit ab:

> Ein Netz, in dem nicht nur Informationen zirkulieren, sondern auch Fragen, Perspektiven, Auswertungen und Erkenntnisoperationen.

Vielleicht entsteht daraus einmal eine Infrastruktur, in der Menschen nicht nur Inhalte teilen.

Sondern auch:

* **wie sie etwas untersuchen,**
* **was sie beobachten wollen,**
* **welche Perspektive sie darauf anwenden,**
* **welche Ergebnisse bereits vorliegen,**
* **wann diese Ergebnisse neu geprüft werden müssen,**
* **und welche Erkenntnisprozesse miteinander verbunden werden sollten.**

Derzeit ist YAS eine Hypothese darüber, wie eine solche Infrastruktur aussehen könnte.

Und ein Ort, um herauszufinden, was damit möglich wird.
