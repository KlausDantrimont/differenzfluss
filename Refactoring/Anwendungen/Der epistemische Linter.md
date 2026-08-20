# Der epistemische Linter

## Warum KI nicht nur Antworten, sondern auch Fragen prüfen sollte

Mit leistungsfähigen KI-Systemen verändert sich die Art, wie Menschen Wissen erschließen.

Eine Suchmaschine verlangt vor allem, dass man weiß, wonach man sucht.
Eine KI kann wesentlich mehr: Sie kann Begriffe ordnen, Zusammenhänge herstellen, Perspektiven wechseln, Hypothesen entwickeln und große kognitive Räume in kurzer Zeit durchqueren.

Damit verschiebt sich jedoch das Problem.

Nicht nur die Qualität der Antwort wird wichtig.

Auch die Qualität der Frage.

Denn eine Frage ist kein neutraler Eingang in einen Wissensraum. Sie enthält bereits Entscheidungen darüber, was als Gegenstand gilt, welche Kategorien verwendet werden, welche Unterschiede relevant sind und welche Zusammenhänge überhaupt sichtbar werden.

Eine schlechte Frage erzeugt deshalb nicht unbedingt eine schlechte Antwort.

Sie kann etwas Gefährlicheres erzeugen:

**eine sehr gute Antwort auf ein schlecht konstruiertes Problem.**

---

## Fragen enthalten Modelle

Betrachten wir eine einfache Frage:

> Warum macht soziale Medien die Menschen dümmer?

Sie klingt verständlich. Doch in ihr stecken bereits mehrere Annahmen.

Dass „soziale Medien“ eine hinreichend einheitliche Ursache seien.

Dass „die Menschen“ sinnvoll als eine Gruppe behandelt werden können.

Dass „dümmer“ eine ausreichend klare Eigenschaft bezeichnet.

Dass eine Veränderung tatsächlich stattfindet.

Und dass diese Veränderung kausal auf soziale Medien zurückzuführen ist.

Noch bevor die erste Antwort gegeben wurde, ist also bereits ein erheblicher Teil des Problemraums konstruiert worden.

Eine KI kann nun beginnen, Studien, Mechanismen und Beispiele zu liefern.

Sie kann dabei sachlich korrekt sein und dennoch innerhalb eines problematischen Framings arbeiten.

Das eigentliche Problem liegt dann nicht in der Antwort.

Es liegt im Eingang.

---

## Der Prompt als Quelltext

Aus der Softwareentwicklung ist ein ähnliches Problem bekannt.

Ein Programm wird nicht einfach ausgeführt, nur weil jemand Zeichen in eine Datei geschrieben hat.

Ein Compiler untersucht zunächst seine Struktur.

Ist die Syntax gültig?

Passen die Typen?

Sind verwendete Namen definiert?

Gibt es Mehrdeutigkeiten oder Konstruktionen, die wahrscheinlich zu Fehlern führen?

Für Fragen an KI fehlt eine vergleichbare Schicht bislang weitgehend.

Die Eingabe wird gewöhnlich unmittelbar als Arbeitsauftrag behandelt.

Man könnte jedoch eine zusätzliche Funktion einführen:

**einen epistemischen Linter.**

Seine Aufgabe wäre nicht, die Frage zu beantworten.

Seine erste Aufgabe wäre zu prüfen, ob die Frage als Erkenntnisinstrument sauber genug konstruiert ist.

---

## Was ein epistemischer Linter prüfen könnte

Ein epistemischer Linter müsste keine philosophische Vollprüfung jeder Äußerung durchführen.

Er müsste lediglich nach Strukturen suchen, die das Ergebnis wesentlich beeinflussen können.

Dazu gehören beispielsweise:

**Unklare Begriffe**

Was bedeutet „Intelligenz“, „Gerechtigkeit“, „Gesellschaft“, „Erfolg“ oder „Bewusstsein“ in der konkreten Frage?

**Verdeckte Voraussetzungen**

Wird bereits vorausgesetzt, dass das behauptete Phänomen überhaupt existiert?

**Kausalitätsannahmen**

Wird nach dem Grund für etwas gefragt, dessen Ursache noch gar nicht geklärt ist?

**Reifikation**

Wird ein Prozess, ein Aggregat oder eine statistische Beschreibung behandelt, als wäre es ein handelndes Ding?

**Kategorienvermischung**

Werden Tatsachen, Bewertungen, Absichten und Erklärungen miteinander vermengt?

**Skalenvermischung**

Wird unbemerkt zwischen Individuen, Gruppen, Institutionen und Gesellschaften gewechselt?

**Falsche Alternativen**

Unterstellt die Frage, dass nur zwei Möglichkeiten existieren?

**Begriffsdrift**

Verändert ein zentraler Begriff während der Argumentation seine Bedeutung?

**Mehrfachfragen**

Werden mehrere voneinander unabhängige Probleme in eine einzige Frage gepackt?

**Framing**

Welche möglichen Erklärungen werden durch die Formulierung bereits bevorzugt oder ausgeschlossen?

---

## Nicht korrigieren, sondern sichtbar machen

Dabei entsteht sofort ein neues Problem.

Wenn die KI eine schlecht gebaute Frage einfach stillschweigend verbessert, ersetzt sie möglicherweise das Modell des Nutzers durch ihr eigenes.

Das wäre epistemisch bequem, aber gefährlich.

Die KI sollte daher nicht heimlich normalisieren.

Sie sollte sichtbar machen, was sie erkennt.

Zum Beispiel:

> Deine Frage setzt voraus, dass der beobachtete Effekt existiert und kausal durch X verursacht wird.
> Wenn diese Annahmen selbst untersucht werden sollen, wäre eine offenere Frage: …

Damit bleibt die Entscheidung beim Menschen.

Der Linter zeigt mögliche Schnitte.

Er bestimmt sie nicht.

---

## Eingreifen nur dann, wenn es zählt

Ein epistemischer Linter darf allerdings nicht zum philosophischen Türsteher werden.

Wer fragt:

> Wie lange muss ein Ei kochen?

braucht keine Abhandlung über die ontologische Bedeutung des Begriffs „Ei“.

Die Prüfung muss deshalb eine Eingriffsschwelle besitzen.

Ein sinnvoller Grundsatz wäre:

**Kommentiere die Frage nur dann, wenn ihre Struktur die mögliche Antwort wesentlich verändert.**

Daraus könnten drei Stufen entstehen:

**Hinweis**

Ein anderer Schnitt könnte zusätzliche Erkenntnisse liefern.

**Warnung**

Eine Annahme oder Mehrdeutigkeit beeinflusst die Antwort deutlich.

**Fehler**

Die Frage vermischt Kategorien oder Voraussetzungen so stark, dass eine belastbare Antwort ohne Klärung kaum möglich ist.

---

## Vom Prompt Engineering zur gemeinsamen Problemformulierung

Damit verändert sich auch die Rolle des Nutzers.

Heute lautet die implizite Forderung häufig:

> Lerne, gute Prompts zu schreiben.

Das ist nur begrenzt befriedigend.

Je leistungsfähiger KI-Systeme werden, desto weniger sinnvoll erscheint es, dem Menschen allein die Verantwortung für die vollständige Konstruktion des Erkenntnisraums aufzubürden.

Eine bessere Arbeitsteilung wäre:

Der Mensch bringt sein Problem, seine Vermutung oder seine Verwirrung mit.

Die KI hilft ihm, darin Strukturen zu erkennen.

Beide formen daraus eine tragfähige Frage.

Erst dann beginnt die eigentliche Exploration.

Der Ablauf wäre:

**Anliegen → Frage → Prüfung → Refactoring → Exploration**

Damit wird die KI nicht nur Antwortmaschine.

Sie wird zum Werkzeug der Problemformulierung.

---

## Fragen refaktorieren

Der Begriff des Refactorings passt erstaunlich gut.

In der Softwareentwicklung verändert Refactoring die Struktur eines Programms, ohne seine gewünschte Funktion zu verlieren.

Etwas Ähnliches lässt sich mit Fragen tun.

Aus:

> Warum zerstört Kapitalismus die Gesellschaft?

könnte der Linter zunächst extrahieren:

* „zerstört“ enthält bereits eine Bewertung und Kausalannahme,
* „Kapitalismus“ bezeichnet ein komplexes Institutionengefüge,
* „Gesellschaft“ ist ein Aggregat,
* der relevante Vergleichsmaßstab fehlt.

Danach könnten mehrere tragfähigere Schnitte entstehen:

> Welche gesellschaftlichen Strukturen verändern sich unter unterschiedlichen kapitalistischen Institutionen?

oder:

> Welche Gruppen profitieren oder verlieren unter bestimmten wirtschaftlichen Mechanismen?

oder:

> Welche empirischen Effekte werden kapitalistischen Institutionen zugeschrieben, und wie gut sind die jeweiligen Kausalmodelle belegt?

Keine dieser Fragen ist automatisch die richtige.

Aber nun ist sichtbar, **welche Frage eigentlich untersucht wird**.

---

## Eine neue Benutzerschnittstelle zur KI

Vielleicht liegt hier eine allgemeinere Konsequenz.

Menschen werden nicht sämtliche kognitiven Räume kennen können, die leistungsfähige KI-Systeme erschließen.

Sie werden auch nicht alle erkenntnistheoretischen Fehlerklassen beherrschen.

Sie müssen es möglicherweise auch nicht.

Die KI selbst kann lernen, den Zugang zu diesen Räumen zu prüfen.

Damit entsteht eine neue Form der Mensch-Maschine-Kopplung:

Der Mensch liefert Neugier, Erfahrung, Ziele und Urteil.

Die KI liefert Struktur, Variation, Vergleich und Analyse.

Und zwischen beiden liegt die Frage.

Der epistemische Linter bewacht nicht die Wahrheit.

Er bewacht den **Einstieg in die Suche nach ihr**.

Vielleicht ist das eine der sinnvolleren Aufgaben, die man einer intelligenten Maschine geben kann.
