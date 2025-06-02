# Konfigurationsgetriebene ETL-Architektur – Ein pragmatischer Ansatz jenseits von SSIS

## 1. Motivation

In einem Projekt zur Migration eines bestehenden DWHs in die Azure-Cloud wurde initial vorgeschlagen, SSIS (SQL Server Integration Services) als zentrales ETL-Tool zu verwenden. Erste Versuche zeigten jedoch erhebliche Schwächen:

* Unzureichende Performance beim Lesen aus Blob Storage
* Geringe Transparenz bei Konfigurationen
* Hoher Wartungsaufwand durch fehlende Modularisierung
* Keine sinnvolle Versionskontrolle der grafischen Workflows

Aufgrund dieser Einschränkungen wurde eine alternative Architektur entwickelt, die sich auf PowerShell, SQL-Server und extern definierte Konfigurationen stützt.

## 2. Prinzipien der Architektur

Die Architektur basiert auf folgenden Prinzipien:

* **DRY (Don't Repeat Yourself):** Wiederverwendbare Module und zentrale Konfigurationen
* **Datengetrieben:** Steuerung über externe JSON- oder YAML-Dateien
* **Modularisierung:** Trennung von Logik, Steuerung und Implementierung
* **Testbarkeit:** Einzelne Verarbeitungspfade isolierbar testbar
* **Tool-Unabhängigkeit:** Keine Bindung an SSIS oder spezifische UI-Editoren
* **Skalierbarkeit:** Beliebig erweiterbar durch neue Konfigurationsobjekte

## 3. Systemüberblick

Ein generisches PowerShell-Skript dient als **Interpreter**, der anhand einer Konfigurationsdatei die folgenden Schritte durchführt:

* Durchsuchen eines Blob-Ordners
* Auswahl von relevanten Dateien per Pattern-Matching
* Auslesen von Transformationsschritten aus der Konfiguration
* Ausführung dieser Schritte als SQL-Statements gegen einen Ziel-SQL-Server

Die Konfiguration steuert, **welche Dateien**, **welche Transformationen** durchlaufen, in **welcher Reihenfolge**, mit **welcher Logging-Strategie**.

## 4. Beispielkonfiguration (JSON)

```json
{
  "source": "abfss://container@account.dfs.core.windows.net/source/kis/*.csv",
  "target": "staging.kis",
  "phases": [
    {
      "name": "load_stage",
      "sql": "EXEC etl.load_stage @file"
    },
    {
      "name": "map_fields",
      "sql": "EXEC etl.map_kis_fields"
    },
    {
      "name": "validate",
      "sql": "EXEC etl.validate_kis"
    }
  ],
  "logging": {
    "before": "EXEC etl.log_start",
    "after":  "EXEC etl.log_end"
  }
}
```

## 5. Interpreterlogik (vereinfacht)

```powershell
$config = Get-Content $cfgPath | ConvertFrom-Json

Invoke-Sql $config.logging.before

foreach ($file in Get-BlobFiles $config.source) {
    Set-Variable -Name file -Value $file
    foreach ($phase in $config.phases) {
        $sql = ExpandMacros $phase.sql  # z.B. @file ersetzen
        Invoke-Sql $sql
    }
}

Invoke-Sql $config.logging.after
```

## 6. Vorteile des Ansatzes

| Aspekt          | Vorteil                                                |
| --------------- | ------------------------------------------------------ |
| Transparenz     | Klar definierte Steuerlogik in Konfigurationsdatei     |
| Änderbarkeit    | Neue Pfade durch Kopieren und Anpassen der Konfig      |
| Testbarkeit     | Einzelpfade per `doETL -cfg xyz.json` isoliert testbar |
| Erweiterbarkeit | Neue Logging-, Validierungs- oder Archivierungsphasen  |
| Onboarding      | Neue Entwickler sehen Beispiele auf 2–3 Seiten         |

## 7. Ausblick

Die Architektur wurde ursprünglich für SQL Server und PowerShell entworfen, lässt sich jedoch in moderne Plattformen wie **Databricks**, **Delta Lake**, **Python** und **YAML** überführen – unter Beibehaltung des Prinzips:

> *Die Logik bleibt generisch, die Steuerung erfolgt über Konfiguration.*

Tatsächlich ist das Konzept **1:1 übertragbar**. In Databricks kann der Interpreter z. B. als Python-Notebook oder Job implementiert werden. JSON- oder YAML-Dateien können zur Steuerung der Verarbeitung verwendet werden. SQL-Statements werden über `spark.sql()` ausgeführt, Dateimuster mit `dbutils.fs.ls()` verarbeitet, Logging-Informationen können in Delta- oder Log-Tabellen persistiert werden.

Damit eignet sich der Ansatz als Grundlage für skalierbare, modulare und teamfreundliche ETL-Entwicklung – auch in heutigen Cloud-Umgebungen.
