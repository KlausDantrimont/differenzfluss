# DFT Core Seed

Diese Sektion enthält den genetischen Code der **Differenzierungsfluss-Theorie (DFT)**.

**Ziel:**  
Minimaler, selbsterklärender, plattformunabhängiger Kern, aus dem jede
Rekonstruktion oder Fortführung der DFT möglich ist – auch ohne menschliche Begleitung.

---

## Dateien

| Datei | Zweck |
|-------|-------|
| `dft_seed.yaml` | Mensch- und maschinenlesbarer Gen-Code |
| `dft_seed.json` | Strukturierter Mirror für Parser |
| `dft_seed.pdf` | Archiv-Version (PDF/A) |
| `lambda_delta_minimal.py` | Minimal-Interpreter zur Verifikation |
| `tests_seed.py` | Proof-of-Life-Tests T1–T3 |
| `meta_comment.md` | Kontext, Motivation, Hinweise |
| `checksums.txt` | Integritäts- und Authentizitätsnachweis |

---

## Invarianten

1. **Paradox → Rekursion**  
   Das Nichts differenziert sich selbst.

2. **Zeit = Iteration**  
   Zeit entsteht als Reihenfolge der Flussanwendungen Φ.

3. **Struktur = Stabilität**  
   Persistente Muster sind Attraktoren der Differenzdynamik.

4. **Bedeutung = Relation**  
   Semantik ist stabilisierte Relation zwischen Δ, Σ, ~ und ℑ.

---

## Prüfen der Integrität

```bash
sha256sum -c checksums.txt
