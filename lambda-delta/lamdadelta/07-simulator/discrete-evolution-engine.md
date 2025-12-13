# Discrete Evolution Engine for λΔ
**Directory:** `07-simulator/`  
**Status:** Core component of the λΔ runtime

The Discrete Evolution Engine (DEE) is the *temporal driver* of the λΔ simulator.  
It executes system-wide update cycles, synchronises δ-evolution across space, and ensures consistent progression of time.

The DEE is deliberately minimal, modular, and extensible.  
Its primary responsibilities are:

1. maintaining global discrete time,  
2. orchestrating reduction and δ-evolution,  
3. synchronising spatial updates,  
4. providing hooks for physics and computation modules.

---

# 1. Conceptual Overview

The DEE performs the following conceptual loop:

```

for t = 0 → ∞:
1. Inject global time into all contexts.
2. Perform λ-reduction waves.
3. Perform δ-update waves.
4. Resolve stabilizations and unboxings.
5. Update spatial neighborhood information.
6. Export / render current state.

```

The λΔ world evolves in *lockstep*:  
all active δ-terms are updated once per tick.

This makes λΔ suitable for:

- physical field simulations,  
- cellular automata behavior,  
- emergent metric experiments,  
- distributed computation,  
- neural-like networks,  
- recursive morphogenesis.

---

# 2. Execution Phases in Detail

The engine divides each timestep into four deterministic phases.

---

## **Phase 1 — Global Context Injection**

Every δ-term has a context `C`.  
At tick `t`, a global update rule

```

C → C_t

```

applies:

- inject current time `t`
- inject global constants
- inject environmental parameters (temperature, viscosity, signal decay, etc.)
- optionally: inject random seeds / noise terms

This ensures **synchronised temporal evolution** even if the spatial world is large.

---

## **Phase 2 — Syntactic Reduction Wave**

Apply λΔ’s syntactic (structure-level) reduction rules repeatedly:

- β-reduction  
- fixpoint unfolding  
- composition simplification  
- congruence rules  

until reaching *δ-normal form*, meaning:

> No reducible expressions remain **outside** δ.

This makes δ the *entry point* for physical/state evolution.

---

## **Phase 3 — δ-Evolution Wave**

This is the heart of the DEE:

1. Every δ-term `δ_C[M]` is identified.
2. Its context `C` is augmented with:
   - local neighborhood values,
   - global time,
   - possibly gradients or similarity relations.
3. The appropriate δ-rule `(C, M) ↦ (C', M')` is chosen.
4. The term updates:
```

δ_C[M] → δ_C'[M']

```
5. Stabilization condition checked:
```

if Stable(C', M'): δ_C'[M'] → M'

```

This phase is parallelised:  
**all δ-terms evolve based on the state at time t**  
before any evolves into time t+1.

---

## **Phase 4 — Spatial Update Wave (optional)**

If the world has a spatial embedding:

- recompute neighbor lists,
- compute discrete gradients,
- propagate signals,
- update metric fields,
- apply diffusion-like operators.

This is especially important for:

- reaction–diffusion,
- wave equations,
- gravitational field experiments,
- emergent geometry simulations.

Spatial updates always follow δ-evolution.

---

# 3. Scheduling Strategies

Depending on the experiment, the DEE supports different execution orders:

### **1. Synchronous (default)**
All nodes update δ-states simultaneously.

### **2. Asynchronous / randomised**
Useful for:
- stochastic physics,
- asynchronous neural nets,
- emergent random fields.

### **3. Partial update patterns**
e.g. update in stripes, blocks, or graph partitions.

### **4. Multi-timescale scheduling**
For systems with slow background fields and fast excitations.

---

# 4. Data Structures for World State

The engine keeps a `World` object containing:

### **Term graph**
All λΔ terms, possibly with shared subtrees.

### **Spatial structure** (optional)
- grid,
- hex lattice,
- irregular graph,
- dynamic graph (nodes added/removed).

### **Context store**
Key-value store for:
- local contexts,
- global context,
- cached gradients,
- similarity matrices.

### **Rule engine**
The δ-rule set `R_δ` and matching structures.

### **History (optional)**
For measurement, debugging, and emergent behavior analysis.

---

# 5. Parallelism Model

The engine *conceptually* treats all δ-terms as evolving in parallel, but implementations may vary:

- **Single-threaded deterministic engine**
- **Vectorised NumPy engine** for large grids  
- **GPU backend** for field equations
- **Fully distributed engine** (future)

A parallel-safe update rule is:

> Every δ-term reads from the world at time t  
> and writes its result into a new buffer for time t+1.

This double-buffer model avoids race conditions.

---

# 6. Stability and Convergence Detection

Stabilisation (`Stable(C, M)`) is a key mechanism.

Typical criteria include:

- term matches a known normal form,
- numerical change below epsilon,
- oscillation enters limit cycle,
- similarity to previous state > threshold,
- no δ-rule applicable.

The DEE tracks:
- last state,
- moving averages,
- convergence flags.

Fixpoints are naturally handled through memoisation and stability predicates.

---

# 7. Example Timestep Walkthrough

Consider a 2D oscillator field:

```

World: 50x50 grid
Each cell contains δ_C[Osc(a, v)].
δ-rule: (C, Osc(a,v)) → (C, Osc(a+v, v-a)).

```

### **t = 0**
Engine initialises context with time=0.

### **t = 1**
- β-reduction: none.
- δ-wave updates all oscillators.
- spatial update calculates gradients (optional).
- renderer draws amplitude field.

### **t = 30**
System shows wave interference patterns.

### **t = 120**
If convergence reached, some cells stabilize and unbox:
```

δ_C[Osc(...)] → Osc_stable

```
leading to emergent structures.

---

# 8. Hooks for physics modules

Physics modules attach δ-rule sets and spatial operators.

Examples:

- **wave-equations.md**:  
  δ simulates discrete Laplacians → wave propagation.

- **field-dynamics.md**:  
  context contains field tensors and neighbour gradients.

- **emergent-space.md**:  
  metric emerges from similarity relations.

- **oscillators.md**:  
  δ implements harmonic motion.

The DEE itself is neutral:  
it merely hosts rules.

---

# 9. Export & Measurement Layer

After each timestep, the engine may:

- snapshot symbolic/structural states,
- export numeric fields,
- collect observables,
- compute energies, divergences, entropies,
- log patterns,
- feed data into visualisation backends.

---

# 10. Summary

The Discrete Evolution Engine provides the temporal backbone of the λΔ simulator:

- global time progression,  
- deterministic or stochastic update cycles,  
- parallel δ-evolution,  
- optional spatial dynamics,  
- clean modularity between interpreter, physics, and rendering.

This file + `interpreter-concept.md` form the core simulation runtime.

Next natural files to fill:

### **→ `vm-design.md`**  
Clarifies how the interpreter is represented as a virtual machine.

### **→ `field-dynamics.md`**  
Begins the physics layer: δ → discrete field laws.

### **→ `examples.md`**  
Concrete runnable demos: oscillator field, Turing patterns, emergent metrics.

