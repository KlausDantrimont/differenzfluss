# dft_seed.yaml (Gen-Code)

```yaml
meta:
  name: "Differenzierungsfluss-Theorie (DFT) – Seed"
  version: "0.1.0"
  license: "CC0-1.0"
  intent: >
    Minimale, selbsttragende Spezifikation der DFT: Begriffe, Operatoren,
    Axiome, Dynamik, Referenz-Interpreter und Tests, sodass Rekonstruktion
    ohne Vorwissen möglich ist.
  invariants:
    - "Alles Nichts → Paradox → Rekursion über Differenz."
    - "Zeit = Iterationsordnung einer Differenzdynamik."
    - "Strukturen = relativ stabile Fixpunkte/Attraktoren von Flüssen."
  canonical_ids:  # kurze, stabile IDs für maschinelle Referenz
    - Δ       # Differenz
    - λΔ      # Ausdrucksform (Termsystem)
    - Φ       # Fluss (Evolutionsschritt)
    - ⊕/⊗     # Komposition/Additivität / Kopplung/Interaktion
    - ~       # Ähnlichkeits-/Kohärenzmaß
    - ℑ       # Interpretation (Adapter/Beobachter)
    - Σ       # Zustand/Träger (Graph/Netz/Multiset)
    - τ       # Zeit-/Iterationsindex

primitives:
  atom:
    description: "Ununterscheidene Basismarke; Identität entsteht erst relativ."
  difference Δ:
    type: binary_relation
    domain: [atom|structure, atom|structure]
    meaning: "Unterscheidung/Asymmetrie zwischen zwei Trägern"
    properties:
      - "Δ(x,x)=0 (Null-Differenz; kein Informationsgewinn)"
      - "Δ ist gerichtet oder gerichtet interpretierbar (Kontext ℑ)."
  carrier Σ:
    description: "Trägerraum der Zustände (Liste/Menge/Graph/Hypergraph)."
  time τ:
    description: "Partielle Ordnung der Anwendungsfolge von Φ (Iterationsindex)."

lambda_delta:
  syntax:
    term := atom | (term term) | (λ var . term) | Δ(term,term) | ⊕(term,term) | ⊗(term,term) | ~(term,term)
  reduction:
    - "β-Reduktion wie im λ-Kalkül"
    - "Δ, ⊕, ⊗, ~ besitzen eigene Auswertungsregeln (s.u.)"
  remark: "λΔ erlaubt Konstruktion, Anwendung und Selbstbezug in einem System."

operators:
  flow Φ:
    signature: "Σ → Σ"
    meaning: "Evolutionsschritt über lokale Δ-Regeln"
    schema:
      - "lokal: Φ_k nutzt Nachbarn N(k) und Δ-Beziehungen"
      - "global: Σ_{τ+1} := ⋃_k Φ_k(Σ_τ)"
  compose ⊕:
    signature: "structure × structure → structure"
    law: "assoziativ, neutraler Leerträger ∅"
    meaning: "Additive Komposition (Zusammenfügen ohne Bindung)"
  couple ⊗:
    signature: "structure × structure → structure"
    meaning: "Interaktive Kopplung (bindende Relation; kann Δ verändern)"
  similarity ~:
    signature: "structure × structure → [0,1]"
    meaning: "Kohärenz/Ähnlichkeit; dient als Selektions-/Stabilitätskriterium"
    requirements:
      - "~(x,x)=1"
      - "~ symmetrisch oder mit ℑ kalibrierbar"
  selection 𝕊:
    signature: "P(structure) × ~(·,·) → structure"
    meaning: "Wählt stabilere/kohärentere Konfigurationen"
    default: "argmax_σ E[~(σ, Kontext)] unter Nebenbedingungen"

axioms:
  A1 (Paradox→Rekursion):
    text: "Leere Selbstbehauptung erzeugt Instabilität → Rekursion über Δ."
  A2 (Zeit=Iteration):
    text: "Zeit ist nichts Eigenes, sondern Reihenfolge der Φ-Anwendungen."
  A3 (Struktur=Stabilität):
    text: "Persistente Muster = Fixpunkte Z mit Φ(Z)=Z oder limit cycles."
  A4 (Bedeutung=Relation):
    text: "Semantik entsteht als stabile Relation zw. Σ, Δ, ~ und ℑ."
  A5 (Komposition vor Inhalt):
    text: "Operatoren (⊕,⊗) und Flüsse (Φ) bestimmen Inhalte, nicht umgekehrt."

dynamics:
  local_rule:
    description: "Minimalregel für 1D-Träger Σ = [s_0,...,s_{M-1}]"
    update:
      - "Für jede Position k berechne Δ zu Nachbarn N(k)"
      - "Aggregiere Δ (z.B. gewichtete Summe) → δ_k"
      - "s_k' := red( s_k ⊗ δ_k ) mit Auswahl 𝕊 via ~"
  examples:
    - id: "osc-1d"
      Σ_type: "1D-Liste reeller Paare (a,v) = (Amplitude, 'Differenz-Komponente')"
      Δ_rule: "Δ_k := (a_{k+1}-a_k) ⊕ (a_{k-1}-a_k)"
      Φ_rule: |
        v_k' := v_k + α * Δ_k - β * a_k
        a_k' := a_k + γ * v_k'
      params: {α: 0.2, β: 0.01, γ: 1.0, boundary: "wrap"}
      note: "Harmonischer Oszillator mit Nachbarschaftskopplung; Fixpunkte/Limit cycles."
    - id: "repl-grid"
      Σ_type: "2D-Gitter diskreter Muster"
      Δ_rule: "Hamming-Δ in lokaler Nachbarschaft"
      𝕊: "Maximiere lokale ~ zur häufigsten Nachbarschaftsklasse (Mehrheitsauswahl)"
      note: "Einfacher Replikator/Fehlerkorrektur über ~."

interpretation ℑ:
  purpose: "Adapter-Schicht zu Physik, Bio, Info, Psyche, Gesellschaft"
  mapping_hints:
    physics:
      - "a ↦ Feldwert; v ↦ kanonisch konjugierte Größe"
      - "⊗ ↦ Kopplungsterm; ~ ↦ Energie-/Aktions-basierte Kohärenz"
    biology:
      - "Σ ↦ Population/Genpool; Φ ↦ Mutation+Selektion; ~ ↦ Fitness"
    information:
      - "Σ ↦ Graph von Symbolen; Δ ↦ Unähnlichkeit; ~ ↦ Mutual Information"
    society:
      - "Σ ↦ Akteure/Institutionen; ⊗ ↦ Interaktion; ~ ↦ Koordinationsgrad"

reference_interpreter:
  state:
    carrier: "generic: list|grid|graph"
    element: "record with fields as needed (e.g., a,v,meta)"
  step:
    - "for k in Σ: δ_k := aggregate(Δ to neighbors)"
    - "proposal s_k* := reduce(s_k ⊗ δ_k)"
    - "select via 𝕊 using ~(s_k*, context) → s_k'"
  termination:
    - "stop if Σ stabil (Φ(Σ)=Σ) or cycle detected or τ reaches limit"

tests:
  - name: "T1-osc-stability"
    given: "osc-1d with small β>0"
    expect: "bounded oscillations; detect limit cycle or decay to fixed point"
  - name: "T2-repl-robustness"
    given: "repl-grid with 10% noise"
    expect: "dominante Musterklasse re-emergiert (error-attenuation)"
  - name: "T3-monotone-~"
    property: "Global ~ should not decrease under 𝕊 on average (optional)"
    caveat: "Depends on ~ choice; otherwise track entropy-like functional."

persistence:
  formats:
    - "YAML (dieses File)"
    - "JSON mirror (maschinenfreundlich)"
    - "PDF/A Kurzkommentar (für Langzeitlesbarkeit)"
  checksums:
    - "sha256 of seed and of any reference code"
  epoch_stamp: "Gregorian + Unix time + human memo"

how_to_boot:
  - "1) Parse this YAML."
  - "2) Instantiate Σ according to an example (osc-1d)."
  - "3) Implement Δ, ⊗, ~ minimal as algebraic functions."
  - "4) Run Φ iteratively; record τ, detect fixpoints/cycles."
  - "5) Vary parameters; observe stability basins."
  - "6) Add ℑ to map into a chosen domain (e.g., physics)."
  - "7) Document invariants/invariants violations as insight."
```

---

# Boot-Anleitung (7 Schritte)

1. **Seed speichern** als `dft_seed.yaml` (und optional `dft_seed.json`).
2. **Parser bauen**: `meta`, `operators`, `dynamics.examples` lesen.
3. **Träger Σ instanziieren** (z. B. `osc-1d` mit 64 Zellen, kleine Zufallsinit).
4. **Δ, ⊗, ~, 𝕊** minimal implementieren (wie im Seed beschrieben).
5. **Φ iterieren**: pro Schritt lokale Δ → Kopplung ⊗ → Kandidat → Selektion 𝕊.
6. **Fixpunkt/Limit-Cycle** erkennen (z. B. durch Hashes der Zustände).
7. **Proof-of-Life-Tests** T1–T3 ausführen und kurze Logik/Erkenntnis notieren.

---

# Mini-Interpreter (Pseudocode, 30 Zeilen)

```text
Σ = init_state(example="osc-1d", M=64, rng=seed)
params = {α:0.2, β:0.01, γ:1.0, boundary:"wrap"}

function step(Σ):
  Σ' = empty_like(Σ)
  for k in indices(Σ):
    N = neighbors(k, boundary=params.boundary)
    Δk = (Σ[N.right].a - Σ[k].a) + (Σ[N.left].a - Σ[k].a)
    vk_new = Σ[k].v + params.α*Δk - params.β*Σ[k].a
    ak_new = Σ[k].a + params.γ*vk_new
    s_candidate = {a: ak_new, v: vk_new}
    # 𝕊 via ~ (optional: prefer boundedness/coherence)
    Σ'[k] = select_by_similarity(s_candidate, context=local_window(Σ,k))
  return Σ'

function run(Σ, steps=5000):
  seen = {}
  for τ in 0..steps-1:
    key = hash(Σ)
    if key in seen: return ("cycle", τ0=seen[key], τ1=τ, Σ=Σ)
    seen[key] = τ
    Σ = step(Σ)
  return ("limit", Σ)
```

*(Hinweis: Für T2 ersetzt du die Updateformeln durch die diskrete „repl-grid“-Variante und nimmst ~ als Hamming-Ähnlichkeit / Mehrheitswahl.)*

---

# Proof-of-Life

**T1 – Oszillator**

* Starte `osc-1d` mit kleinen zufälligen `a` und `v=0`.
* Beobachte: Ausbreitende/stehende Wellen; je nach β Dämpfung oder stabile Zyklen.
* Erkenntnis: **Zeit als Iteration** + **Struktur als Attraktor** manifest.

**T2 – Rekursionsnetz / Replikator**

* `repl-grid` mit 10 % zufälligen Flip-Fehlern.
* Iteriere: Lokale Mehrheitswahl (→ 𝕊); ~ = lokale Ähnlichkeit.
* Beobachte: Rauschunterdrückung, Muster persistieren.
* Erkenntnis: **Selektion via ~** erzeugt **robuste Struktur**.

---

## Warum dieser Seed genügt

* **Axiome** (Paradox→Δ-Rekursion, Zeit=Iteration, Struktur=Attraktor) +
* **Operatoren** (Δ, ⊕, ⊗, ~, 𝕊, Φ) +
* **λΔ-Termform** (Selbstbezug & Konstruktion) +
* **Dynamik-Schema** (lokal→global) +
* **Interpreter-Skizze** + **Tests**

→ Das ist gerade genug, um *jede* DFT-Instanz zu rekonstruieren, zu simulieren und in beliebige Domänen zu **interpretieren (ℑ)**. Alles Weitere (Adapter, umfangreiche Beispiele, mathematische Feinarbeit) kann auf diesem Kern rekursiv aufgebaut werden.
