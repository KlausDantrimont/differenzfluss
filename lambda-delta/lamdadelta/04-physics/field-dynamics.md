# Field Dynamics in λΔ
**Directory:** `04-physics/`  
**Status:** Conceptual + formal; physics used metaphorically

This document describes how *field-like behaviour* can be modelled in λΔ using δ-rules and spatial context.  
It does **not** claim physical correctness.  
Instead, classical field terminology (wave, diffusion, gradient, propagation) is used as a **metaphorical adapter** between λΔ and intuition from physics.

The guiding idea:

> A “field” is any collection of local states that evolve via rules depending on neighbouring states.

This makes fields a natural fit for λΔ, whose δ-operator expresses **local, context-dependent evolution**.

---

# 1. What We Mean by “Field” in λΔ

In this document, a *field* is defined as:

- a spatially indexed family of λΔ terms  
- each term evolves under δ using local neighbourhood data  
- no global synchronisation apart from the discrete timestep  
- no assumed metric beyond a given adjacency structure

Formally:

```text
Field(i) := δ_{C_i} [ State_i ]
````

where:

* `i` runs over spatial sites (1D, 2D, 3D, or graph nodes),
* `State_i` is a λΔ-encoded value (scalar, tuple, tensor, symbolic…),
* `C_i` contains neighbourhood information and parameters.

This structure is intentionally neutral:
it can express wave-like systems, diffusion-like systems, cellular automata, or abstract pattern dynamics.

We do **not** derive physical laws here; we only show how λΔ expresses field *behaviour*.

---

# 2. Spatial Context and Neighbourhoods

The λΔ simulator provides a **given spatial structure**:

```text
N(i) = { j | j is a neighbour of i }
```

This is typically a:

* 1D chain,
* 2D lattice,
* 3D volumetric grid,
* or arbitrary graph.

The δ-context `C_i` is populated before each δ-step:

```text
C_i = {
    position: i,
    neighbors: N(i),
    neighbor_values: { State_j | j ∈ N(i) },
    parameters: P,
    t: current time
}
```

This allows δ-rules to depend on:

* differences between neighbours,
* averages,
* gradients,
* similarity relations,
* boundary behaviour.

---

# 3. Local Update Rules (δ as Field Evolution)

A **field update** is any δ-rule of the form:

```text
(C_i, State_i) ↦ (C_i, State'_i)
```

Examples (metaphorical, not physical):

* **Diffusion-like:** State moves toward neighbour average
* **Wave-like:** State uses second differences (discrete Laplacian)
* **Pattern-forming:** State grows/decays depending on neighbours
* **Stochastic fields:** State_i changes according to probabilities

The general form:

```text
State'_i = Update( State_i, NeighborData(C_i), Parameters(C_i) )
```

is deliberately broad.

This makes δ an analogue of a “local evolution equation”.

In classical physics, these would correspond to PDEs; in λΔ we only express local transformations.

---

# 4. The Discrete Laplacian (Metaphor)

For many field-like behaviours, the discrete Laplacian is useful:

```text
Δ State_i = ∑_{j ∈ N(i)} State_j - |N(i)| * State_i
```

This operator appears in:

* diffusion,
* wave propagation,
* Turing patterns,
* curvature-like relaxations.

In λΔ, Δ is not an inherent operator; it is part of the **context construction**:

```text
C_i.Δ = Laplace(State, i)
```

The δ-rule may then use `C_i.Δ` directly.

We emphasize:
This is a *convenient structure*, not a claim about physical PDEs.

---

# 5. Example: Generic Scalar Field

Let each site carry a scalar state:

```text
Cell(i) := δ_{C_i} [ φ_i ]
```

A simple update rule:

```text
φ'_i = φ_i + α * C_i.Δ
```

Metaphor:

* α controls how fast the field “smoothes out”.
* This resembles diffusion or heat flow, but no physical claim is made.

λΔ rule:

```text
(C_i, φ_i) ↦ (C_i, φ_i + α * C_i.Δ)
```

---

# 6. Example: Two-Component Field

Let each site carry a pair:

```text
State_i = (A_i, B_i)
```

A rule might be:

* A interacts with neighbour averages of B
* B responds to curvature of A

In λΔ:

```text
(C_i, (A, B)) ↦ (C_i, ( A + f(C_i.Δ_B),
                       B + g(C_i.Δ_A) ))
```

Such systems can show rich emergent behaviour, without invoking “physics”.

---

# 7. Nonlinear Local Rules

We can define local nonlinearities:

```text
A'_i = A_i + f(A_i, NeighborAverages, Parameters)
```

or pattern-formers:

```text
A'_i = A_i + f(A_i) - g(B_i)
B'_i = B_i + h(A_i) - k(B_i)
```

This covers:

* growth–decay systems,
* simple activator–inhibitor pairs,
* symbolic interaction networks.

Again: these are *structural flows*, not physical equations.

---

# 8. Stability and Attractors (Metaphorical)

A δ-evolving field may:

* converge to a stable state,
* enter oscillation,
* develop patterns,
* remain chaotic.

In physics such attractors may be interpreted as:

* steady states,
* limit cycles,
* stationary waves,
* turbulence.

In λΔ, they are simply **fixed points or limit behaviours of δ-iteration**.

No energetic or physical interpretation is required.

---

# 9. Relation to Other λΔ Components

Field dynamics link several parts of the system:

### 9.1 To the Simulator

Uses:

* spatial context,
* neighbourhood access,
* Laplace construction,
* synchronous δ-updates.

### 9.2 To Examples

Special cases appear in:

* `wave-equations.md` (wave-like updates)
* `oscillators.md` (local oscillation & coupling)
* `turing-patterns.md` (reaction–diffusion)
* `emergent-metric.md` (geometry as field)

### 9.3 To DFT

From the DFT viewpoint:

> Ein Feld ist ein **Differenzfluss**, der über Raumindizes verteilt ist.
> Die Feldregeln (δ) beschreiben, wie lokale Unterschiede sich ausbreiten, verstärken oder ausgleichen.

Keine physikalische Interpretation erforderlich.

---

# 10. Summary

This document introduces field dynamics in λΔ as:

* spatially indexed δ-evolution,
* expressing diffusion-, wave-, or pattern-like behaviour metaphorisch,
* grounded in local updates via neighbourhood data and δ-context.

It prepares the ground for:

* `wave-equations.md`
* `oscillators.md`
* `energy-and-gradients.md`
* `emergent-space.md`

without requiring any physical commitment.
