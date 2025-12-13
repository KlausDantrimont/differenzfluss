# Turing Patterns in λΔ

**Directory:** `08-examples/`  
**Status:** Example specification – 2D reaction–diffusion in λΔ

This example shows how **Turing patterns** (spots, stripes, labyrinths) can emerge in the λΔ framework via a **reaction–diffusion system** implemented with δ-rules on a 2D lattice.

It combines:

- δ as **local reaction + diffusion operator**,  
- the **spatial model** (2D grid, neighbourhood),  
- and the **discrete evolution engine** (synchronous timesteps).

---

## 1. Conceptual Setup

We simulate a classic two-species reaction–diffusion system on a 2D grid:

- `U(x, y, t)` – activator
- `V(x, y, t)` – inhibitor

Each cell `(x, y)` carries a λΔ-term encoding the local concentrations of `U` and `V`.

The δ-operator applies:

- **diffusion** via discrete Laplacian over neighbours,  
- **reaction** via nonlinear local terms.

Over time, stable spatial patterns emerge.

---

## 2. λΔ Term Structure

For each lattice site `(i, j)` we store a term of the form:

```text
Cell(i, j) := δ_{C(i,j)} [ Chem(U_ij, V_ij) ]
````

where:

* `U_ij` – activator concentration at `(i, j)`
* `V_ij` – inhibitor concentration at `(i, j)`
* `C(i,j)` – context containing:

  * coordinates `(i, j)`
  * neighbour references
  * global parameters: `Du, Dv, F, k`
  * current time step `t`

Globally, the world is a 2D array:

```text
World := [ [ Cell(i, j) ]_{j=0..Ny-1} ]_{i=0..Nx-1}
```

---

## 3. δ-Rule: Gray–Scott Style Reaction–Diffusion

We use a Gray–Scott-like model (one of the standard Turing systems):

Let:

* `∆U_ij` = discrete Laplacian of `U` at `(i, j)`
* `∆V_ij` = discrete Laplacian of `V` at `(i, j)`
* `Du, Dv` – diffusion coefficients
* `F` – feed rate
* `k` – kill rate
* `dt` – time step

The continuous equations (for orientation) are:

```text
∂U/∂t = Du ∆U - U V² + F (1 - U)
∂V/∂t = Dv ∆V + U V² - (F + k) V
```

We discretise as:

```text
U' = U + dt * ( Du * ∆U - U*V² + F*(1 - U) )
V' = V + dt * ( Dv * ∆V + U*V² - (F + k)*V )
```

### 3.1 δ-Rule Form

In λΔ rule notation:

```text
(C, Chem(U, V)) ↦ (C, Chem(U', V'))
```

where `U'` and `V'` are computed from the context `C`:

* `C.U` = U
* `C.V` = V
* `C.∆U` = discrete Laplacian of U from neighbors
* `C.∆V` = discrete Laplacian of V from neighbors
* `C.params = {Du, Dv, F, k, dt}`

---

## 4. Discrete Laplacian via Context

The **spatial model** provides a neighbourhood `N(i, j)` of indices for each cell.
For a regular 2D grid with 4-neighbour connectivity:

```text
N(i, j) = {
    (i-1, j), (i+1, j),
    (i, j-1), (i, j+1)
}
```

The Laplacian for a scalar field `U` is approximated as:

```text
∆U_ij = ∑_{(p,q) ∈ N(i,j)} U_pq - |N(i,j)| * U_ij
```

This is computed by the **spatial update phase** and injected into the δ-context of each cell:

```text
C(i,j).∆U = Laplace_U(i, j)
C(i,j).∆V = Laplace_V(i, j)
```

The δ-rule then only sees `U`, `V`, `∆U`, `∆V`, `Du`, `Dv`, `F`, `k`, `dt` as scalar values.

---

## 5. Example Parameter Sets

Typical Gray–Scott parameter sets that produce interesting patterns:

1. **Spots**

   ```text
   Du = 0.16
   Dv = 0.08
   F  = 0.060
   k  = 0.062
   dt = 1.0  (or smaller if needed)
   ```

2. **Labyrinths / Stripes**

   ```text
   Du = 0.16
   Dv = 0.08
   F  = 0.035
   k  = 0.065
   dt = 1.0
   ```

3. **Moving/chaotic patterns**

   ```text
   Du = 0.20
   Dv = 0.10
   F  = 0.030
   k  = 0.055
   dt = 1.0
   ```

These numbers are meant as **starting points** for λΔ-simulations.

---

## 6. Initial Conditions

A typical initialisation strategy:

1. Start with almost uniform `U ≈ 1`, `V ≈ 0` everywhere.
2. Add a small perturbation region (e.g. a square in the middle):

```text
for (i, j) in center_region:
    U_ij := 0.50
    V_ij := 0.25
```

3. Optionally add random noise:

   * slight random variation in U and/or V,
   * or random seeds scattered across the grid.

The **emergent pattern** strongly depends on both parameters and initial conditions.

---

## 7. λΔ Pseudocode Sketch

This is **illustrative**, not a strict syntax spec:

```text
-- Term template for a single cell
Cell(i, j) :=
  δ_{C(i,j)} [
    Chem(U_ij, V_ij)
  ]

-- δ-rule (pseudo-code)
rule TuringStep(C, Chem(U, V)) =

  let Du  = C.params.Du
      Dv  = C.params.Dv
      F   = C.params.F
      k   = C.params.k
      dt  = C.params.dt
      dU  = C.∆U    -- Laplacian of U
      dV  = C.∆V    -- Laplacian of V
  in
      let U' = U + dt * ( Du * dU - U*V*V + F*(1 - U) )
          V' = V + dt * ( Dv * dV + U*V*V - (F + k)*V )
      in
          Chem(U', V')
```

As δ-rule:

```text
(C, Chem(U, V)) ↦ (C, Chem(U', V'))
```

Stabilisation (`Stable(C, Chem(U,V))`) is usually **not** applied here, because Turing patterns are ongoing dynamic equilibria rather than fully frozen states. But you *can* define:

* local convergence criteria,
* or a “frozen phase” where diffusion is turned off after a while.

---

## 8. Integration with the Simulator

### 8.1 Discrete Evolution Engine

Each timestep `t`:

1. **Spatial phase**

   * compute Laplacians `∆U`, `∆V` for all cells,
   * inject into `C(i,j)`.

2. **δ-evolution phase**

   * apply `TuringStep` rule once to each `Cell(i, j)`.

3. **Rendering**

   * derive a color from `(U_ij, V_ij)` for each cell,
   * e.g. grayscale or colormap of `V`.

### 8.2 VM and Context

* The VM’s `SpaceModel` keeps neighbour lists and field values.
* `ContextStore` provides per-cell contexts `C(i,j)` populated before δ-rules fire.
* δ-terms are naturally **parallel** across cells.

---

## 9. Observables and Diagnostics

During the simulation you can track:

* spatial variance of `U`, `V`,
* histogram of concentrations,
* number and size of spot/stripe clusters,
* symmetry breaking vs. homogeneous state,
* sensitivity to parameter changes (bifurcations).

For DFT-Betrachtung interessant:

* Muster sind **stabile Differenzflüsse** in Raum und Zeit,
* δ kodiert die **lokale Prozessregel**,
* das emergente Muster ist eine **fixierte Struktur im globalen Fluss**.

---

## 10. Extensions and Variants

Once the basic Gray–Scott Turing patterns run, you can extend:

1. **Noise injection**

   * Add δ-rules that occasionally perturb U/V with small random noise → robustnessanalyse.

2. **Spatially varying parameters**

   * Let `F` oder `k` von Position oder Zeit abhängen → Gradienten, Domänenwände.

3. **Metric feedback**

   * Couple diffusion to an emergent metric field from `emergent-metric.md`.

4. **Coupling to oscillators**

   * Use local oscillators whose frequency depends on U/V → pattern-based rhythms.

5. **Boundary conditions**

   * periodic, reflective, absorbing – all beeinflussen die entstehenden Strukturen.

---

## 11. Summary

This example shows:

* how a classical reaction–diffusion system can be expressed in λΔ,
* how δ + spatial context encode local physical laws,
* how **global patterns** emerge from **local rules** in discrete time,
* and how this ties into the λΔ simulator architecture.

It is a canonical testbed for:

* 2D spatial embedding,
* neighbour-based δ-rules,
* heavy parallel evolution,
* and emergent structure analysis.

