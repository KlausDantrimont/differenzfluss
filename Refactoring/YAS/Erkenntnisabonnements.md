# Erkenntnisabonnements

## Vom Informationsabonnement zur konfigurierbaren Erkenntnisleistung

Ein klassisches Abonnement liefert Inhalte.

Ein Newsletter liefert neue Ausgaben.
Ein RSS-Feed liefert neue Einträge.
Ein Datenfeed liefert neue Datenpunkte.
Eine Suchabfrage liefert neue Treffer.

Der Empfänger entscheidet anschließend selbst, was davon relevant ist und wie es zu bewerten ist.

Mit KI entsteht eine zusätzliche Möglichkeit:

> **Nicht nur Inhalte abonnieren, sondern deren Auswertung.**

Der Nutzer beschreibt nicht nur, **welche Quelle** ihn interessiert.

Er beschreibt auch:

* welche Frage gestellt werden soll,
* unter welcher Perspektive die Quelle betrachtet werden soll,
* welche Veränderungen relevant sind,
* welche Bedingungen eine Meldung auslösen,
* und welche Aktion anschließend erfolgen soll.

Aus dem Informationsabonnement wird ein:

> **Erkenntnisabonnement**

---

## Grundform

Ein Erkenntnisabonnement kann als Kombination mehrerer Komponenten verstanden werden:

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

Beispiel:

```text
Quelle:
    Newsletter X

Fragestellungen:
    Was hat sich seit der letzten Ausgabe verändert?
    Welche neuen Behauptungen werden aufgestellt?
    Welche Evidenz wird dafür genannt?

Perspektiven:
    Evidenz
    Anreize
    langfristige Folgen

Bedingung:
    Nur melden, wenn eine wesentliche neue Behauptung auftaucht
    oder eine bisher tragende Annahme fraglich wird.

Aktion:
    Kurzbericht erzeugen
    und auf die Originalquelle verweisen.
```

Das Abonnement gilt damit nicht dem Newsletter selbst.

Es gilt einer **definierten Erkenntnisleistung auf diesem Newsletter**.

---

## Was wird eigentlich abonniert?

Der Unterschied lässt sich einfach formulieren.

Ein Informationsabonnement fragt:

> **Was ist neu?**

Ein Erkenntnisabonnement kann zusätzlich fragen:

> **Was daran ist für meine Fragestellung relevant?**

Oder:

> **Was hat sich epistemisch verändert?**

Oder:

> **Welche meiner bisherigen Annahmen werden dadurch berührt?**

Oder:

> **Welche neue Perspektive wird notwendig?**

Das Abonnement bezieht sich damit nicht nur auf Inhalte.

Es bezieht sich auf eine **Transformation von Information in eine für den Nutzer relevante epistemische Form**.

---

## Beispiele

### Gesetzgebung

```text
Quelle:
    Veröffentlichungen zu einem Gesetzgebungsverfahren

Fragen:
    Welche Änderungen wurden vorgenommen?
    Welche Gruppen sind davon betroffen?
    Welche neuen Nebenwirkungen könnten entstehen?

Brillen:
    Anreize
    Verteilungswirkungen
    Systemgrenzen

Trigger:
    Melden, wenn sich die Belastung einer betroffenen Gruppe
    wesentlich verändert.
```

---

### Wissenschaft

```text
Quelle:
    Veröffentlichungen zu Forschungsgebiet X

Fragen:
    Welche Ergebnisse sind neu?
    Welche bisherigen Annahmen werden gestützt oder geschwächt?
    Gibt es methodische Einwände?

Brillen:
    Evidenz
    Gegenhypothesen
    Reproduzierbarkeit

Trigger:
    Melden, wenn eine zentrale Annahme des bisherigen Modells
    substanziell in Frage gestellt wird.
```

---

### Unternehmen

```text
Quelle:
    Geschäftsberichte, Pressemitteilungen, Branchenmeldungen

Fragen:
    Welche strategischen Veränderungen zeichnen sich ab?
    Welche Risiken werden neu erwähnt?
    Welche früheren Aussagen werden verändert oder aufgegeben?

Brillen:
    Anreize
    zeitliche Dynamik
    Widersprüche

Trigger:
    Melden bei substantieller Änderung der strategischen Lage.
```

---

### Öffentlicher Diskurs

```text
Quelle:
    Aussagen mehrerer Akteure zu einem Thema

Fragen:
    Welche Behauptungen widersprechen sich?
    Welche Begriffe werden unterschiedlich verwendet?
    Welche Annahmen bleiben unausgesprochen?

Brillen:
    Framing
    Evidenz
    Perspektivenvergleich

Trigger:
    Melden, wenn ein neuer struktureller Konflikt sichtbar wird.
```

---

## Nicht alles muss ständig neu ausgewertet werden

Erkenntnisabonnements sind nicht als dauerhafte KI-Beschäftigung gedacht.

Eine Auswertung ist ein abgeleitetes Objekt.

Wenn sich ihre Abhängigkeiten nicht verändert haben, bleibt sie gültig.

```text
Quelle v12
+
Skript v4
+
Brille v2
=
Auswertung A
```

Solange Quelle, Skript und Brille gleich bleiben:

```text
Auswertung A bleibt gültig.
```

Erst wenn sich eine relevante Abhängigkeit verändert:

```text
Quelle v13
→ Auswertung A potenziell veraltet
```

muss erneut geprüft werden.

Das Prinzip lautet:

> **Auswerten bei Bedarf, nicht aus Gewohnheit.**

---

## Trigger statt Dauerbeobachtung

Ein Erkenntnisabonnement kann Bedingungen enthalten.

Zum Beispiel:

* wenn eine neue Behauptung auftaucht,
* wenn zwei Quellen sich erstmals widersprechen,
* wenn ein Risiko einen Schwellenwert überschreitet,
* wenn sich die Bewertung einer Entwicklung wesentlich verändert,
* wenn eine bekannte Annahme nicht mehr trägt,
* wenn eine neue strukturelle Verwandtschaft gefunden wird.

Der Trigger bestimmt, wann eine erneute Auswertung sinnvoll ist.

Damit kann YAS zwischen zwei Ebenen unterscheiden:

### leichte Prüfung

Hat sich überhaupt etwas verändert?

### tiefe Auswertung

Ist die Veränderung für die deklarierte Fragestellung relevant?

Das spart Rechenaufwand und reduziert unnötige Meldungen.

---

## Brillen als Teil des Abonnements

Die gleiche Quelle kann unter verschiedenen Perspektiven völlig unterschiedliche Erkenntnisleistungen erzeugen.

Ein Wirtschaftsnewsletter könnte beispielsweise betrachtet werden unter:

* Evidenz,
* makroökonomischer Dynamik,
* Verteilungswirkungen,
* politischen Anreizen,
* Langfristfolgen,
* Risiko,
* Framing.

Die Quelle bleibt gleich.

Die **epistemische Verarbeitung** verändert sich.

Brillenmodelle können deshalb Bestandteil eines Erkenntnisabonnements sein.

Sie sollten möglichst als referenzierbare und versionierte Objekte vorliegen:

```text
Quelle X
+
Fragestellung Y
+
Brille Z v3
```

Ändert sich die Brille wesentlich, kann auch eine neue Auswertung notwendig werden.

---

## Epistemische Skripte

Komplexere Erkenntnisabonnements können ihre Analyse in einem epistemischen Skript beschreiben.

Beispiel:

```text
1. Ermittle alle neuen Aussagen.
2. Trenne Tatsachenbehauptungen von Bewertungen.
3. Suche die angegebene Evidenz.
4. Vergleiche mit früheren Aussagen derselben Quelle.
5. Prüfe auf Widersprüche.
6. Betrachte relevante Folgen unter der Risiko-Brille.
7. Melde nur substanzielle Änderungen.
```

Damit wird die Auswertung:

* reproduzierbarer,
* teilbarer,
* vergleichbarer,
* versionierbar,
* und auditierbarer.

Ein Erkenntnisabonnement ist damit nicht bloß ein gespeicherter Prompt.

Es kann ein **persistenter epistemischer Prozess** sein.

---

## Persönliche und öffentliche Erkenntnisabonnements

Nicht jedes Erkenntnisabonnement muss privat bleiben.

Menschen könnten gute epistemische Skripte oder Brillenkombinationen teilen.

Beispielsweise:

> „Neue medizinische Studien – Evidenzprüfung“

> „Neue Gesetze – Nebenwirkungsanalyse“

> „Politische Reden – Framing und Widersprüche“

> „Unternehmensberichte – strategische Veränderungen“

Andere Nutzer könnten solche Konfigurationen übernehmen, verändern oder mit anderen Quellen verbinden.

Damit würden nicht nur Inhalte geteilt.

Geteilt würde:

> **wie Inhalte untersucht werden.**

---

## Erkenntnisabonnements als soziale Objekte

Ein öffentliches Erkenntnisabonnement kann selbst Teil des Netzes werden.

Dann könnte YAS beispielsweise erkennen:

> Mehrere Nutzer wenden strukturell ähnliche Fragen auf verschiedene Domänen an.

Oder:

> Zwei Erkenntnisabonnements verwenden unterschiedliche Begriffe, prüfen aber dieselbe epistemische Struktur.

Oder:

> Eine neu veröffentlichte Brille ergänzt eine bestehende Auswertung sinnvoll.

Damit können Erkenntnisabonnements nicht nur Information filtern.

Sie können auch **Menschen, Methoden und Fragestellungen miteinander verbinden**.

---

## Der Unterschied zu personalisierten Feeds

Personalisierte Feeds versuchen meist vorherzusagen:

> **Was wird diesen Nutzer vermutlich interessieren?**

Ein Erkenntnisabonnement funktioniert anders.

Der Nutzer deklariert sein Erkenntnisinteresse selbst:

> **Was möchte ich beobachten, unter welcher Fragestellung und mit welchen Kriterien?**

Das ist ein wesentlicher Unterschied.

Das System optimiert nicht primär Aufmerksamkeit.

Es führt eine explizit gewünschte epistemische Aufgabe aus.

---

## Der Unterschied zu einem KI-Agenten

Ein KI-Agent ist zunächst ein technischer Ausführungsmechanismus.

Ein Erkenntnisabonnement beschreibt dagegen die **epistemische Absicht**.

Ein Agent kann ein Erkenntnisabonnement ausführen.

Aber das Abonnement selbst sollte unabhängig vom konkreten Agenten beschreibbar sein.

Damit können verschiedene Systeme dieselbe Erkenntnisleistung ausführen und ihre Ergebnisse verglichen werden.

```text
Erkenntnisabonnement
       │
       ├── KI-System A
       ├── KI-System B
       └── Mensch
```

Das eröffnet prinzipiell auch Audit und Qualitätsvergleich.

---

## Anforderungen

Damit Erkenntnisabonnements zuverlässig funktionieren, sollten mindestens folgende Eigenschaften explizit sein:

* Quelle,
* Fragestellung,
* verwendete Brillen oder Operatoren,
* Versionen der verwendeten Objekte,
* Bedingungen und Trigger,
* Zeitpunkt und Grundlage einer Auswertung,
* Provenienz des Ergebnisses,
* gewünschte Ausgabe oder Aktion.

Je nach Anwendung kommen hinzu:

* Vertrauensniveau der Quellen,
* epistemisches Budget,
* Relevanzschwellen,
* Dringlichkeit,
* Sichtbarkeit,
* Datenschutz,
* notwendige menschliche Freigaben.

---

## Offene Fragen

Zu untersuchen bleibt insbesondere:

* Wie formal müssen Erkenntnisabonnements beschrieben werden?
* Welche Teile können natürlichsprachlich bleiben?
* Wann ist ein Ergebnis hinreichend ähnlich, um wiederverwendet zu werden?
* Welche Änderungen invalidieren eine bestehende Auswertung?
* Wie werden Unsicherheit und unterschiedliche KI-Ergebnisse dargestellt?
* Welche Trigger können billig geprüft werden?
* Wann ist eine erneute vollständige Auswertung notwendig?
* Wie werden Fehlalarme vermieden?
* Wie verhindert man epistemische Filterblasen?
* Wie können konkurrierende Brillen oder Skripte verglichen werden?
* Wie werden Abonnements versioniert und geteilt?
* Welche Teile sollten lokal ausgeführt werden?

---

## Verhältnis zu YAS

Erkenntnisabonnements sind eine mögliche zentrale Nutzungsform von YAS.

YAS stellt dafür die Infrastruktur bereit:

```text
Quellen
↓
Änderungserkennung
↓
epistemische Skripte
↓
Brillen
↓
Auswertungen
↓
Trigger
↓
Signale und Aktionen
```

Das Erkenntnisabonnement beschreibt, **welche Kombination davon ein Nutzer tatsächlich möchte**.

Damit wird YAS von einem Netz beobachteter Quellen zu einem Netz konfigurierbarer Erkenntnisprozesse.

---

## Kurzfassung

> **Ein Informationsabonnement liefert Neues.**
>
> **Ein Erkenntnisabonnement prüft, was davon unter einer bestimmten Fragestellung relevant ist.**

Mit KI wird diese zweite Form technisch billig genug, um sie breit einzusetzen.

Dadurch könnte sich die Art verändern, wie Menschen Informationen abonnieren.

Nicht mehr nur:

> „Zeig mir, was veröffentlicht wurde.“

Sondern:

> **„Beobachte das für mich – und sag mir Bescheid, wenn sich etwas ändert, das ich wissen sollte.“**
