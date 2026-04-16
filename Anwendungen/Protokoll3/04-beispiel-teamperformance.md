# Beispiel: Teamperformance, Altsystem und Änderungsunsicherheit

## Von der schlechten Frage zur prüfbaren Strukturhypothese

Dieses Beispiel zeigt, wie eine moralisch oder personalisierend gestellte Frage durch das DFT-Dialogprotokoll in einen analysierbaren Gegenstand und schließlich in eine prüfbare Strukturhypothese überführt wird.

Die Ausgangsfrage lautet:

**„Warum performt mein Team so schlecht?“**

Das Problem dieser Frage ist nicht nur ihre Unschärfe, sondern auch ihr impliziter Fokus auf Personen.  
Sie legt nahe, dass das Defizit primär im Team selbst liegt.  
Die Aufgabe der KI besteht hier darin, diese Frage nicht einfach zu beantworten, sondern sie zunächst in eine bessere Szene zu überführen.

---

# Phase 0 — Simulierter Dialog zur Szenenerhebung

## Mensch

Warum performt mein Team so schlecht?

## KI

Das ist noch zu grob und stark personenzentriert.  
Ich würde zuerst nicht nach „schlecht“, sondern nach **sichtbaren Reibungen** fragen.

Woran genau machst du die schlechte Performance fest?

---

## Mensch

Alles dauert zu lange. Features kommen zu spät. Die Leute wirken beschäftigt, aber es kommt wenig raus.

## KI

Gut. Dann haben wir schon erste Symptome:

- Verzögerung
- hoher Beschäftigungseindruck
- geringer Output

Jetzt der nächste Schnitt:  
Wo genau entsteht die Verzögerung am stärksten?

- bei Entscheidungen?
- bei Abstimmung?
- bei Implementierung?
- bei Tests?
- bei Abnahmen?
- bei unklaren Anforderungen?

---

## Mensch

Schwer zu sagen. Vermutlich überall ein bisschen. Aber vor allem reden sie wahnsinnig viel. Viele Meetings, viel Abstimmung. Und dann tauchen beim Umsetzen dauernd neue Probleme im Altsystem auf.

## KI

Jetzt wird es brauchbar.  
Ich sehe mindestens zwei mögliche Richtungen:

1. **Koordinationslast / Meeting-Inflation**
2. **technische Änderungshemmung im gewachsenen System**

Bevor wir das vermischen:  
Welcher Effekt scheint stärker?

- zu viel Abstimmung?
- oder jede Änderung ist technisch unverhältnismäßig teuer?

---

## Mensch

Wahrscheinlich das zweite. Die Meetings sind auch deshalb so häufig, weil keiner genau sagen kann, was bei Änderungen alles kaputtgeht.

## KI

Sehr gut. Das ist bereits eine viel bessere Szene.

Dann wäre die Standarddeutung „Das Team performt schlecht“ vermutlich unzureichend.  
Es könnte eher sein, dass das Team in einem System arbeitet, in dem Änderungen hohe Unsicherheit erzeugen.

Noch zwei Fragen:

1. Woran merkt ihr die technische Unsicherheit konkret?
2. Wer trägt die Kosten davon zuerst?

---

## Mensch

Kleine Änderungen dauern ewig, weil man erstmal verstehen muss, welche Stellen betroffen sind. Neue Leute sind fast nutzlos am Anfang. Und Fehler tauchen oft an ganz anderen Stellen auf.

## KI

Das riecht stark nach einem Strukturproblem im System, nicht primär nach einem Motivationsproblem im Team.

Die Standarddeutung wäre also:

> „Das Team ist langsam oder performt schlecht.“

Und die unbefriedigende Seite daran:

> Sie verwechselt wahrscheinlich Teamleistung mit Änderbarkeit des Systems.

Ich würde den Gegenstand jetzt vorläufig so schneiden:

**Nicht „schwache Teamperformance“, sondern „ein Team, dessen Lieferfähigkeit durch hohe Änderungsunsicherheit in einem gewachsenen Softwaresystem gebremst wird“.**

Passt das eher?

---

## Mensch

Ja, das trifft es ziemlich gut.

## KI

Dann noch ein letzter Schritt für Phase 0:

Was wäre ein erster sichtbarer Indikator, an dem wir das festmachen könnten?

Zum Beispiel:

- Dauer kleiner Änderungen
- Zahl betroffener Module pro Änderung
- Zahl unerwarteter Nebenwirkungen
- Onboarding-Zeit neuer Entwickler
- Anteil der Zeit für Verstehen statt Umsetzen

Was davon passt am besten?

---

## Mensch

Dauer kleiner Änderungen und die Zahl der unerwarteten Nebenwirkungen.

## KI

Gut. Dann ist die Szene für Phase 1 reif.

---

# Output von Phase 0

## Rohszene

Ein Chef erlebt sein Team als langsam und wenig lieferfähig, obwohl alle beschäftigt wirken.

## Standarddeutung

Das Team performt schlecht.

## Warum sie nicht reicht

Die Deutung personifiziert das Problem und blendet aus, dass die eigentliche Bremswirkung aus technischer Unsicherheit und schwer kalkulierbarer Änderbarkeit stammen könnte.

## Gegenstandsschnitt

**Nicht „schwache Teamperformance“, sondern „ein Team, dessen Lieferfähigkeit durch hohe Änderungsunsicherheit in einem gewachsenen Softwaresystem gebremst wird“.**

## Sichtbares Hauptsymptom

Kleine Änderungen dauern unverhältnismäßig lang und erzeugen unerwartete Nebenwirkungen.

## Möglicher Messhaken

- Durchlaufzeit kleiner Änderungen
- Zahl betroffener Module pro Änderung
- Häufigkeit regressiver Seiteneffekte

---

# Phase 1 — DFT-Zerlegung

## Ausgangspunkt

**Gegenstandsschnitt**  
Nicht „schwache Teamperformance“, sondern **ein Team, dessen Lieferfähigkeit durch hohe Änderungsunsicherheit in einem gewachsenen Softwaresystem gebremst wird**.

**Hauptsymptom**  
Kleine Änderungen dauern unverhältnismäßig lang und erzeugen unerwartete Nebenwirkungen.

---

## 1. Primärflüsse

Wovon lebt dieses System operativ?

- **Datenfluss**
- **Entwickleraufmerksamkeit**
- **Änderungszeit**
- **Fehlerrückmeldung**
- **Betriebsstabilität**

Das sind hier die eigentlichen Träger.  
Nicht Motivation als erstes, sondern die operative Änderbarkeit.

---

## 2. Sekundärflüsse

Was stabilisiert das Muster zusätzlich?

- **Lieferdruck**
- **Sicherheitsgefühl durch Bekanntes**
- **Sichtbarkeit von Aktivität**
- **Teamgrenzen und Zuständigkeitsgrenzen**
- **die Erzählung „das Team ist zu langsam“**

Gerade der letzte Punkt ist heikel:  
Die Deutung „schwaches Team“ kann selbst zum Stabilisator werden, weil sie die Aufmerksamkeit von der Struktur weg auf Personen lenkt.

---

## 3. Stabilisatoren

Warum verschwindet das Muster nicht einfach?

- Deadlines belohnen lokale Fixes statt struktureller Bereinigung
- Angst vor Regression schützt alte Kopplungen
- Wissen über Nebeneffekte sitzt in Köpfen einzelner Leute
- kleine Änderungen werden begonnen, ohne dass die globale Folgelast sichtbar ist
- Meetings und Abstimmung steigen als Reaktion auf Unsicherheit
- Führung sieht vor allem Outputmangel, nicht die interne Verstehenslast

Das System hält sich also nicht trotz, sondern teilweise **wegen** dieser Mechanismen.

---

## 4. Zentrale Entkopplung

**Liefererwartung vs. strukturelle Änderbarkeit**

Der Chef bewertet das Team am Output.  
Das System zwingt das Team aber zuerst in Verstehen, Absichern und Schadensvermeidung.

---

## 5. Strukturtyp der Dysfunktion

**Haupttyp:** Wartungsverlust  
**Optionaler Nebentyp:** Verantwortungsverdünnung

Wartungsverlust, weil das System immer mehr Aufwand braucht, um kleine Änderungen sicher zu bewegen.  
Verantwortungsverdünnung, weil niemand direkt für die globale Änderbarkeit zuständig ist: alle liefern lokal, niemand pflegt systemisch.

---

## 6. Messhaken

Woran könnte man die Diagnose prüfen?

- Durchlaufzeit kleiner Änderungen
- Zahl der betroffenen Module pro kleiner Änderung
- Zahl unerwarteter Seiteneffekte nach Änderungen
- Anteil der Zeit für Verstehen oder Impact-Analyse statt Implementierung
- Onboarding-Zeit neuer Entwickler
- Zahl der Personen, die für eine kleine Änderung konsultiert werden müssen

Damit wird aus „fühlt sich zäh an“ etwas Beobachtbares.

---

## 7. Eingriffspunkt

Nicht:  
**„Das Team muss sich mehr anstrengen.“**

Sondern:

- kleine Änderungen systematisch auf betroffene Stellen und Seiteneffekte mappen
- wiederkehrende Unsicherheitscluster identifizieren
- privilegierte Zeit für strukturelle Vereinfachung schaffen
- Architektur- und Wartungslast explizit verantwortlich machen
- Meetings trennen in Problemklärung und Lieferabstimmung
- das Urteil über Teamleistung teilweise von der Änderbarkeit des Systems entkoppeln

Der erste Hebel ist meist:

**Unsichtbare Änderungsfolgen sichtbar machen.**

---

## 8. Gegenprobe

Was erklärt die DFT hier schlecht?

- Es könnte tatsächlich ein Personal- oder Kompetenzproblem geben.
- Schlechte Anforderungen oder häufige Prioritätswechsel könnten die Hauptursache sein, nicht das System selbst.
- Manche Domänen sind objektiv stark gekoppelt; nicht jede Seiteneffektlast ist Fehlstruktur.
- Fehlende Tests könnten der primäre Hebel sein, nicht Refactoring.

Das muss offen bleiben.

---

## 9. Kernsatz

**Der eigentliche Strukturkern ist nicht ein schlecht performendes Team, sondern eine Situation, in der Liefererwartung und reale Änderbarkeit strukturell entkoppelt sind, weil ein gewachsenes System kleine Änderungen in globale Unsicherheit übersetzt.**

---

## Vier-Satz-Format

**Vorher war unklar:** Warum wirkt das Team langsam, obwohl alle beschäftigt sind?  
**Durch die DFT-Brille sichtbar wurde:** Ein großer Teil der Leistung geht in Verstehen, Absichern und Nebenwirkungsmanagement eines schwer änderbaren Systems.  
**Der Strukturkern scheint zu sein:** Nicht primär schwache Teamperformance, sondern Wartungsverlust durch entkoppelte Liefererwartung und technische Änderbarkeit.  
**Daraus folgt als Prüf- oder Handlungsfrage:** Wie machen wir Änderungsfolgen, Kopplungslast und Wartungsverlust sichtbar, bevor wir die Leistung des Teams bewerten?

---

# Warum dieses Beispiel wichtig ist

Dieses Beispiel zeigt den methodischen Kern des Protokolls besonders klar:

- Eine schlechte Frage wird nicht direkt beantwortet.
- Eine personalisierende Deutung wird in eine Strukturszene überführt.
- Die DFT-Zerlegung trennt operative Flüsse von narrativer Fehlzuschreibung.
- Am Ende steht keine bloße Meinung, sondern eine prüfbare Strukturhypothese.

Gerade darin zeigt sich der Nutzen der Kombination aus DFT und KI:  
Die KI beantwortet nicht einfach eine Klage, sondern hilft, sie in eine bessere Frage zu transformieren.