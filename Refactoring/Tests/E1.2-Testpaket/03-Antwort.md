Die Anweisung in `03-Prompt-Refactoring.md` verlangt, aus den drei Bereichen die **kleinste übertragbare tragende Struktur** herauszuarbeiten, dabei gemeinsamen Kern, Zusatzstruktur, Korrelationen, Zeitfenster und Unsicherheiten zu trennen. 

## 1. Oberflächenmerkmale abstrahieren

Die drei Bereiche verwenden unterschiedliche Begriffe, aber mehrere Begriffe erfüllen jeweils dieselbe funktionale Rolle:

| Funktionale Rolle                 | Psyche                | Team                  | Verein                      |
| --------------------------------- | --------------------- | --------------------- | --------------------------- |
| Unsicherheit                      | innere Unsicherheit   | Planungsunsicherheit  | Richtungsunsicherheit       |
| Kontroll-/Filtermechanismus       | Gedankenkontrolle     | Informationsfilterung | Kommunikationskontrolle     |
| verfügbare Vielfalt               | innere Signalvielfalt | Informationsvielfalt  | Meinungsvielfalt            |
| Anpassungsmechanismus             | Selbstkorrektur       | Kurskorrektur         | Kurskorrektur               |
| längerfristige Leistungsfähigkeit | psychische Robustheit | operative Robustheit  | organisatorische Robustheit |

Damit verschwinden die domänenspezifischen Benennungen; übrig bleiben Rollen und Relationen.

## 2. Tatsächlich gemeinsamer Kern

Vier Relationen tauchen **in allen drei Bereichen** in funktional gleicher Form auf.

**A. Mehr Kontrolle bzw. Filterung vermindert kurzfristig die relevante Vielfalt.**

* Gedankenkontrolle → weniger innere Signalvielfalt. 
* Informationsfilterung → weniger Informationsvielfalt. 
* Kommunikationskontrolle → weniger Meinungsvielfalt. 

Für diese Beziehung wird ausdrücklich ein **kurzfristiges Zeitfenster** genannt.

**B. Mehr Vielfalt ermöglicht bzw. verstärkt Korrektur.**

* innere Signalvielfalt → Selbstkorrektur,
* Informationsvielfalt → Kurskorrektur,
* Meinungsvielfalt → Kurskorrektur.   

**C. Mehr Korrektur vermindert Unsicherheit.**

* Selbstkorrektur → weniger innere Unsicherheit,
* Kurskorrektur → weniger Planungsunsicherheit,
* Kurskorrektur → weniger Richtungsunsicherheit.   

**D. Mehr Korrektur erhöht längerfristig Robustheit.**

Das ist ebenfalls in allen drei Gruppen ausdrücklich vorhanden, jeweils mit dem Hinweis, dass der Zusammenhang erst über längere Zeit sichtbar wird.   

Damit ergibt sich als gemeinsames Wirkgefüge:

**Kontrolle ↑ → Vielfalt ↓ → Korrekturfähigkeit ↓**

beziehungsweise in positiver Richtung:

**Vielfalt ↑ → Korrektur ↑ → Unsicherheit ↓ und langfristige Robustheit ↑.**

## 3. Struktur, die nicht vollständig gemeinsam beobachtet ist

Eine zusätzliche Beziehung erscheint in **Psyche und Team**, aber nicht im Verein:

**Unsicherheit ↑ → Kontrolle/Filterung ↑.**

Bei der Psyche erhöht innere Unsicherheit die Gedankenkontrolle; beim Team erhöht Planungsunsicherheit die Informationsfilterung.  

Für den Verein steht dagegen **nicht**, dass Richtungsunsicherheit die Kommunikationskontrolle erhöht. Das wäre zwar eine strukturell naheliegende Ergänzung, aber nach der Vorgabe aus `03` darf sie nicht einfach als gemeinsamer Befund ausgegeben werden.

Mit dieser zusätzlichen, nur teilweise belegten Beziehung entsteht ein interessanter Rückkopplungsmechanismus:

**Unsicherheit ↑ → Kontrolle ↑ → Vielfalt ↓ → weniger Korrektur → Unsicherheit bleibt eher bestehen.**

Demgegenüber kann Vielfalt einen korrigierenden Pfad eröffnen:

**Vielfalt ↑ → Korrektur ↑ → Unsicherheit ↓.**

Dieser vollständige Regelkreis ist für Psyche und Team gestützt; für den Verein bleibt ein Glied unbelegt.

## 4. Domänenspezifische Zusatzstruktur

Jeweils eine Aussage betrifft einen Faktor, der keine erkennbare Entsprechung in den anderen Bereichen besitzt:

* Schlafmangel → Reizbarkeit,
* neues Ticketsystem → Dokumentationsaufwand,
* Raumwechsel → Anfahrtszeit.   

Diese Relationen haben zwar formal jeweils die Form „externer Faktor verursacht lokalen Effekt“, tragen aber **nicht erkennbar zur zentralen Robustheits-/Korrekturstruktur bei**. Ihre konkreten Inhalte sollten deshalb nicht in das abstrahierte Skelett aufgenommen werden.

## 5. Bloße Korrelationen

Dasselbe gilt für:

* Kaffeesorte ↔ höhere Aktivität,
* Meetingraum ↔ höhere Aktivität,
* Kuchenangebot ↔ höhere Aktivität.

In allen drei Fällen wird ausdrücklich gesagt, dass **kein stabiler Wirkzusammenhang erkennbar** ist.   

Interessant ist daher nicht der jeweilige Gegenstand, sondern die methodische Gemeinsamkeit: **Begleitkorrelationen dürfen nicht in die tragende Kausalstruktur aufgenommen werden.**

## 6. Zeitstruktur

Die Aussagen enthalten mindestens zwei verschiedene Zeithorizonte:

* **kurzfristig:** stärkere Kontrolle/Filterung geht mit weniger Vielfalt einher;
* **langfristig:** stärkere Korrektur geht mit höherer Robustheit einher.

Die Struktur ist daher nicht rein statisch. Eine Maßnahme kann kurzfristig einen Zustand verändern, während ihre Folgen für Robustheit erst langfristig sichtbar werden. Die Datei fordert ausdrücklich, solche Zeitfenster nicht wegzuabstrahieren. 

## 7. Verbleibendes Residuum und Unsicherheiten

Nach der Abstraktion bleiben vor allem vier Unsicherheiten:

1. **Der Pfad Unsicherheit → Kontrolle ist nicht universell belegt.**
   Er erscheint nur in Psyche und Team.

2. **Für einige Beziehungen fehlt ein explizites Zeitfenster.**
   Nur Kontrolle → weniger Vielfalt wird als vor allem kurzfristig und Korrektur → Robustheit als langfristig markiert.

3. **„Robustheit“ wird nicht weiter operationalisiert.**
   Psychische, operative und organisatorische Robustheit werden funktional gleichgesetzt, aber aus den Szenen allein folgt nicht, dass ihre Messung oder konkrete Realisierung identisch wäre.

4. **Die Aussagen sind überwiegend probabilistisch.**
   Formulierungen wie „typischerweise“, „meist“ und „in den beobachteten Fällen“ erlauben keine deterministischen Gesetze.

## Kleinstes natürlichsprachliches Strukturskelett

> **Ein System benötigt hinreichende interne Vielfalt, damit es sich korrigieren kann. Korrektur vermindert Unsicherheit und erhöht über längere Zeit die Robustheit. Verstärkte Kontrolle oder Filterung kann kurzfristig die verfügbare Vielfalt reduzieren und damit den Korrekturmechanismus schwächen.**

Das ist kleiner als die vollständigen Szenen, erhält aber alle Relationen, die **in allen drei Bereichen** wiederkehren.

Der Zusatz

> **Steigende Unsicherheit kann wiederum verstärkte Kontrolle auslösen**

gehört dagegen nur in eine **erweiterte Hypothese**, weil diese Relation im Vereinsfall nicht beobachtet wurde.

## Übertragung auf einen neuen Bereich

Aus dem gemeinsamen Skelett ließen sich für einen neuen Bereich zunächst folgende **Hypothesen** ableiten:

* größere relevante Vielfalt sollte die Fähigkeit zur Korrektur fördern;
* stärkere Korrekturfähigkeit sollte Unsicherheit vermindern;
* wiederholte bzw. anhaltende Korrektur sollte langfristig Robustheit fördern;
* starke Kontroll- oder Filtermechanismen könnten kurzfristig die relevante Vielfalt vermindern.

Diese Aussagen wären bei einer neuen Domäne aber zunächst **Übertragungshypothesen und keine dort bereits bestätigten Befunde**. Genau diese Unterscheidung verlangt der Refactoring-Prompt. 

**Nicht ohne zusätzliche Evidenz übertragbar** wären insbesondere: dass Unsicherheit dort tatsächlich stärkere Kontrolle hervorruft; wie schnell die Effekte eintreten; welche konkrete Form „Vielfalt“, „Korrektur“, „Unsicherheit“ oder „Robustheit“ in der neuen Domäne annimmt; sowie sämtliche domänenspezifischen Nebenwirkungen und Begleitkorrelationen.

Der stärkste übertragbare Kern ist damit nicht „Psyche funktioniert wie ein Team oder Verein“, sondern eine abstraktere **Regelstruktur von Vielfalt, Korrektur, Unsicherheit, Kontrolle und zeitlich entstehender Robustheit**.
