# Simple Oscillator in λΔ

**Directory:** `08-examples/`  
**Status:** Minimal dynamical example – pure recursion, no stabilisation

This example presents the **simplest non-trivial λΔ-dynamics**:

- a 2D oscillator in the state space `(a, v)`,
- driven by a linear δ-update,
- running either without space (single point) or as a 1D chain of coupled oscillators.

It is the canonical “hello world” of λΔ as a **differential process**:
recursion + δ-evolution, but still fully understandable by hand.

---

## 1. Conceptual Overview

We consider a state with two components:

- `a` – “position-like” component  
- `v` – “velocity-like” component  

and evolve it under the δ-rule:

```text
(a, v) ↦ (a + v, v - a)
````

Interpretations:

* As a **discrete-time linear oscillator** in a 2D state space.
* As a **rotation-like map** (up to scaling) in the `(a, v)` plane.
* As a minimal example of λΔ’s ability to express **iterative dynamics**.

No stabilisation or unboxing is used here; the oscillator runs **indefinitely**.

---

## 2. λΔ Term Structure

We encode the oscillator as a δ-wrapped term. For a single oscillator:

```text
Osc := δ_C [ Osc(a, v) ]
```

where

* `Osc(a, v)` is a constructor holding the state,
* `C` is a context that can (optionally) store:

  * current timestep `t`,
  * oscillator ID,
  * external parameters (e.g. coupling strength in multi-oscillator setups).

For a 1D chain of oscillators (optional extension):

```text
Osc_i := δ_{C_i} [ Osc(a_i, v_i) ]
```

with `i` an index along a discrete line.

---

## 3. δ-Rule Definition

We define a **single δ-rule** for the uncoupled oscillator:

```text
(C, Osc(a, v)) ↦ (C, Osc(a', v'))
```

with

```text
a' = a + v
v' = v - a
```

In λΔ rule notation:

```text
δ_C [ Osc(a, v) ]
    → δ_C [ Osc(a + v, v - a) ]
```

Notes:

* `C` remains unchanged – the rule is **purely internal** to the oscillator.
* No similarity operator is needed here.
* No stabilisation predicate is defined; evolution continues forever.

---

## 4. Behaviour in State Space

The update

```text
(a, v) → (a + v, v - a)
```

is linear and can be written as a matrix map:

```text
[ a' ]   [ 1  1 ] [ a ]
[ v' ] = [ -1 1 ] [ v ]
```

Key qualitative properties:

* The origin `(0, 0)` is a fixed point.
* Generic initial states orbit around the origin in a **rotation-like trajectory**.
* The map can be interpreted as a discrete analogue of a **harmonic oscillator** (up to rescaling and coordinate transforms).

For the purposes of λΔ, we mostly care that:

* the system **does not converge**,
* it exhibits **ongoing, structured change**,
* the pattern is simple enough to be reasoned about analytically.

---

## 5. Initial Conditions

Typical initial states for demonstrations:

1. **Single oscillator**

   ```text
   a₀ = 1.0
   v₀ = 0.0
   ```

2. **Slightly perturbed**

   ```text
   a₀ = 1.0
   v₀ = 0.1
   ```

3. **Randomised ensemble** (for chains)

   ```text
   a_i(0) = random small value
   v_i(0) = random small value
   ```

Even with very simple initial conditions, running the δ-rule over many timesteps produces interesting structure in the `(a, v)` trajectory.

---

## 6. Simulation in the λΔ Engine

Within the discrete evolution engine (DEE), a typical timestep for the **single oscillator**:

1. **λ-phase**

   * No β-reduction or fixpoints involved in this minimal example.
   * `Osc(a, v)` is already a constructor in δ-normal form.

2. **δ-phase**

   * Engine finds the δ-term: `δ_C[Osc(a, v)]`.
   * Applies the oscillator rule:

     ```text
     (C, Osc(a, v)) ↦ (C, Osc(a + v, v - a))
     ```
   * Updates the world state at this location.

3. **Spatial phase**

   * Not used for the single oscillator (no space, just one point).

4. **Rendering / logging**

   * Store `(a, v)` for time series / phase portrait.

The oscillator is thus an ideal **sanity check** for:

* δ-rule application,
* context handling,
* basic performance.

---

## 7. Optional: 1D Oscillator Chain

To test spatial embedding and neighbourhood handling, we can extend the oscillator to a **coupled chain**:

### 7.1 Term

For each site `i`:

```text
Osc_i := δ_{C_i} [ Osc(a_i, v_i) ]
```

The context `C_i` contains:

* neighbour indices `i-1`, `i+1` (if they exist),
* coupling parameter `κ`,
* global time `t`.

### 7.2 δ-Rule with coupling (optional extension)

We can add a simple coupling via neighbour average:

```text
ā_neighbors = (a_{i-1} + a_{i+1}) / 2   (with appropriate boundary handling)

a_i' = a_i + v_i + κ * (ā_neighbors - a_i)
v_i' = v_i - a_i
```

Rule:

```text
(C_i, Osc(a_i, v_i)) ↦ (C_i, Osc(a_i', v_i'))
```

Qualitative behaviour:

* For small `κ`: oscillators stay mostly independent.
* For larger `κ`: tendency towards phase alignment and collective modes.
* This connects directly to synchronisation examples (e.g. Kuramoto-like models).

---

## 8. Visualisation Ideas

For diagnostic and didactic purposes, the simulator can display:

1. **Time series**

   * `a(t)` and `v(t)` over time steps,
   * see recurring patterns, phase shift.

2. **Phase portrait**

   * plot `(a(t), v(t))` in the plane,
   * observe orbital / rotational structure.

3. **Spatial field (for chains)**

   * show `a_i(t)` as a 2D image (i vs. t),
   * or animate `a_i` along a 1D line over time.

These views make the otherwise abstract δ-evolution **intuitively graspable**.

---

## 9. Relation to Other λΔ Examples

* This is the **simplest** non-trivial δ-dynamics in the examples folder.
* It provides a **building block** for:

  * field dynamics (`04-physics/oscillators.md`),
  * synchronisation models (multi-oscillator examples),
  * more complex emergent structures (e.g. metric fields driven by oscillatory modes).

In DFT terms:

> The simple oscillator is a minimal **self-maintaining Differenzfluss**:
> Eine Struktur, die nicht „zu sich kommt“, indem sie zur Ruhe kommt,
> sondern indem sie sich **stabil verändert**.

---

## 10. Summary

This file defines:

* a minimal λΔ oscillator as `δ_C[Osc(a, v)]`,
* a single, linear δ-update rule `(a, v) → (a + v, v - a)`,
* optional extensions to 1D chains with coupling,
* and suggestions for simulation and visualisation.

It serves as:

* a basic test case for the interpreter and δ-engine,
* an intuitive illustration of recursive dynamics in λΔ,
* and a starting point for more elaborate physical models.

