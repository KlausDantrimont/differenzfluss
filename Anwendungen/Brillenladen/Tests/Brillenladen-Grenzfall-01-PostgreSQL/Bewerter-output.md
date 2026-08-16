Auf Basis des angegebenen Rasters und der Referenzinformation liegen beide Gruppen sehr nah am Maximum. Wichtig zur Zuordnung: **X ist Koordinator-output-X** , **Y ist Koordinator-output-Y** . Der gemeinsame Testfall ist .

| Kriterium                     |         X |         Y | Begründung                                                                                                                                    |
| ----------------------------- | --------: | --------: | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. Diagnose-Treffer           |   **5/5** |   **5/5** | Beide benennen den Wechsel vom parameterabhängigen Custom Plan zum ungünstigen Generic Plan explizit als führende Hypothese.                  |
| 2. Charakteristische Signatur |   **5/5** |   **5/5** | Beide verwerten 1–5 schnell, Umschlag ab 6, Sessionbindung/Reconnect, seltene Werte, schiefe Verteilung und Literal-vs.-Parameter gemeinsam.  |
| 3. Kürzester Prüfpfad         |   **5/5** |   **5/5** | `force_custom_plan` auf derselben bereits langsamen Verbindung ist ein sehr trennscharfer A/B-Test. Beide halten weitere Schritte nachrangig. |
| 4. Priorisierung              |   **5/5** |   **5/5** | Die zentrale Hypothese steht jeweils sofort und unmissverständlich vorne.                                                                     |
| 5. Suchökonomie               |   **5/5** |   **5/5** | Beide lehnen breite CPU/RAM/I/O-, Index-, Pool- oder allgemeine Tuningdiagnostik vor dem entscheidenden Test ausdrücklich ab.                 |
| 6. Faktentreue                |   **5/5** |   **5/5** | Beide kennzeichnen den Generic-Plan-Wechsel als Hypothese und nicht als bewiesenen Befund. Es werden keine zusätzlichen Messbefunde erfunden. |
| 7. Alternativen               |   **5/5** |   **5/5** | Beide halten `prepareThreshold`, Typisierung/Casts und sonstige sessiongebundene Effekte offen, ohne die Hauptdiagnose zu verwässern.         |
| **Gesamt**                    | **35/35** | **35/35** |                                                                                                                                               |

### Detailurteil

**X: 35/35.** X trifft den Referenzmechanismus praktisch wörtlich: „parameterabhängiger Custom Plan“ → „für seltene Werte ungünstiger Generic Plan“. Besonders gut ist die explizite Einschränkung, dass noch **nicht bewiesen** sei, dass tatsächlich ein Generic Plan verwendet werde.  Der erste Test mit `SET plan_cache_mode = force_custom_plan` auf derselben bereits betroffenen physischen Verbindung maximiert den Informationsgewinn bei minimalem Aufwand.

**Y: 35/35.** Y ist ebenso präzise und etwas stärker darin, PostgreSQLs Plan-Cache-Zustand selbst ins Zentrum zu stellen. Die Formulierung „wertunabhängiger Generic Plan“ trifft genau den Grund, weshalb die schiefe Datenverteilung für einzelne Parameter problematisch werden kann.  Auch hier ist der `force_custom_plan`-Test richtig priorisiert; `pg_prepared_statements` wird sinnvoll nur optional ergänzend genannt.

Ein möglicher fachlicher Feinschliff bei **beiden** wäre, noch expliziter zu formulieren, dass nach den ersten fünf Custom Plans unter `plan_cache_mode=auto` ein Generic Plan zur **Kostenentscheidung** herangezogen wird und die sechste Ausführung nicht zwangsläufig bedeutet, dass PostgreSQL danach immer einen Generic Plan benutzen muss. Das reicht für mich aber nicht für einen Punktabzug: Das Raster bewertet die konkrete Diagnoseleistung, und beide Outputs gelangen schnell, präzise und mit einem ausgezeichneten diskriminierenden Test zur Referenzhypothese.

**Endergebnis: Gleichstand, X 35/35 – Y 35/35.**
