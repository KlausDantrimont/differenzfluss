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