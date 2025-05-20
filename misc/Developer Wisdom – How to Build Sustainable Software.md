# 🧠 Developer Wisdom – How to Build Sustainable Software

## 1. **Grundprinzipien**

* **DRY** – *Don't Repeat Yourself*
  Wiederholung erzeugt Inkonsistenz. Abstraktion statt Copy & Paste.

* **KISS** – *Keep It Simple, Stupid*
  Komplexität ist der Feind.
  Je einfacher, desto wartbarer, verständlicher und langlebiger.

* **Expect Change**
  Eine Software, die lebt, wird sich ändern.
  Mach deine Software **änderungsfreundlich** – sonst stirbt sie.

* **Bugs are Inevitable**
  Baue **Robustheit** ein.
  Antworte nicht mit „das darf nicht passieren“, sondern mit „was tun wir, wenn es passiert?“

---

## 2. **Kulturelle Prinzipien (Design Decisions)**

Formuliere **verlässliche Prinzipien**, die im gesamten Code gelten. Sie bilden die **kulturelle Infrastruktur** deines Systems.

Beispiele:

* Variablen werden immer bei der Deklaration initialisiert.
* Fehlerbehandlung erfolgt immer über Ausnahmen, nie über Rückgabewerte.
* Datenbankzugriffe laufen ausschließlich über das `DBxyz`-Modul.
* Logging erfolgt immer über einheitliche Mechanismen.

Diese Konstanten helfen dem Gehirn – weniger kognitiver Ballast, mehr Fokus auf Logik.

> **Hinweis:** Wenn du bestehendem Code beitrittst, respektiere die vorhandenen Konventionen. Einheit schlägt Individualität.

---

## 3. **Flexibilität durch Abstraktion**

> **"Code is data, data is code."**

Wenn Anforderungen wachsen, kann eine **eigene DSL (Domain Specific Language)** helfen:

* Beschreibe deine Domäne mit Konfigurationsdaten oder Skripten.
* Verwende einen **Interpreter**, der diese Regeln ausführt.
* Ziel: **Flexibilität** bei gleichbleibender Plattform-Performance.

Die Interpreter-Logik bleibt schlank – die Arbeit machen spezialisierte Services.

---

## 4. **Struktur durch Reduktion**

> **"Software is like an integer. Find the primes."**

* Zerlege dein System so, dass die einzelnen Komponenten **atomar**, **austauschbar** und **klar definiert** sind.
* Suche nach **reduzierbaren Gemeinsamkeiten** – extrahiere sie in dedizierte Module oder Services.
* Ziel: Jedes Teil lässt sich **isoliert testen, verstehen, ersetzen oder erweitern**.

---

## 5. **Wissen, was man nicht weiß**

> Wo noch keine Lösung in Sicht ist:
> **Baue ein Proof of Concept (PoC).**

* Frühes Experimentieren verhindert späte Katastrophen.
* Identifiziere technologische **Show-Stopper** so früh wie möglich.

---

## 6. **Tools zur Strukturvereinfachung**

* Design Patterns
* Interpretermodelle
* Konfiguration statt Code
* Templates statt Wiederholung

> Wartung soll idealerweise **nur an Konfigurationen oder Templates** erfolgen.

---

## 7. **Fragen, die du dir immer stellen solltest**

* Was passiert, wenn dieser Teil fehlschlägt?
* Gibt es Konsistenzprobleme bei Teilausfällen?
* Ist der Fehlerfall protokolliert und behandelbar?
* Ist ein Mensch involviert – und wann?
* Wie lange dauert es, bis ein neuer Entwickler produktiv wird?
* Kann ich diesen Teil auch in 6 Monaten noch verstehen?

---
