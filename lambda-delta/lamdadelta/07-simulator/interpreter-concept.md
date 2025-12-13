# λΔ Interpreter Concept
**Directory:** `07-simulator/`  
**Status:** Core specification

The λΔ interpreter is the minimal executable engine that realises:
1. the reduction rules from `03-semantics/`,  
2. the δ–evolution under discrete time,  
3. optional spatial embedding (1D, 2D, 3D),  
4. and the emergence of patterns, fields, or computation.

This document defines the architecture, execution model, and internal data structures of the interpreter.

---

# 1. Goals and constraints

The λΔ interpreter must:

### **(1) Execute λΔ expressions step-by-step**
Reduction should follow the operational semantics (β, δ-step, fixpoint, congruence).

### **(2) Support discrete time evolution**
A global tick `t → t+1` updates all active δ-terms in the world.

### **(3) Represent space optionally**
The calculus itself is spatially agnostic, but the simulator may assign:
- positions,
- neighborhoods,
- adjacency graphs,
- metrics,
for physical-style simulations.

### **(4) Allow local rules**
δ-rules may depend on:
- local context (C),
- neighborhood values,
- spatial gradients,
- similarity relations.

### **(5) Remain modular**
Physics modules, computation modules, and experiment modules should build *on top* of this interpreter without modifying the core engine.

---

# 2. High-level architecture

```

User Input (λΔ expressions)
|
v
Parser / Loader
|
v
┌───────────────────────────┐
│    λΔ Core Interpreter    │
│                           │
│ - β-reduction             │
│ - δ-context injection     │
│ - δ-rule execution        │
│ - Fix/unfolding           │
│ - Congruence rules        │
└───────────────────────────┘
|
v
Discrete Timestepping
|
v
Spatial Embedding (optional)
|
v
Rendering / Output

```

The interpreter core is **syntax-directed** and **context-driven**:
- The λ-structure reduces exactly as in the λ-calculus.
- δ is the only operator that interacts with *time*, *space*, and *physical rules*.

---

# 3. Internal representation of terms

All λΔ terms are stored as nodes of a tree-like structure:

### **Term kinds**
- `Var(name)`
- `Lambda(var, body)`
- `App(func, arg)`
- `Delta(context, inner)`
- `Compose(left, right)`
- `Fix(func)`

### **Optional metadata**
Each term may carry:
- `position` (for spatial models)
- `id` (unique instance ID)
- `cache` (memoization for fixpoints)
- `similarity_profile`
- `history` (optional debugging)

---

# 4. Execution cycle

The interpreter runs in cycles consisting of:

## **(1) Syntactic reduction phase**
Repeatedly apply:
- β-reduction  
- fixpoint unfolding  
- congruence rules  
until no pure λ-reduction steps remain *outside* δ.

This yields a “δ-ready normal form”:
```

M →* M'
where M' contains only δ-wrapped reducible subterms.

```

## **(2) δ-evolution phase (the physics engine)**
For each δ-term `δ_C[M]`:

1. Inject the current **context**  
   (neighborhood, external parameters, previous states, gradients, …)

2. Apply the δ-rule set `R_δ`:
```

(C, M) ↦ (C', M')

```

3. Replace:
```

δ_C[M] → δ_C'[M']

```

4. If `Stable(C', M')` holds, unbox:
```

δ_C'[M'] → M'

```

## **(3) Spatial update (optional)**
Used to:
- compute gradients,
- gather neighbor values,
- propagate signals,
- update metric fields.

Space is represented by:
- graph of nodes, or
- 1D/2D/3D lattice.

## **(4) Rendering/export**
The engine outputs:
- numeric fields,
- symbolic states,
- heatmaps,
- oscillation frequencies,
- graph embeddings,
depending on the experiment.

---

# 5. Context injection

Contexts are updated via a **Context Manager**.

A context `C` may include:
- `t` (global time)
- `x,y,z` (spatial coordinates)
- neighbor values / similarity scores
- global constants
- local metric tensors
- energy levels (for physics modules)
- arbitrary meta-information

The interpreter guarantees:

> Every δ-term receives the correct context before rule application.

---

# 6. The δ-rule engine

A δ-rule has the form:

```

(C, P) ↦ (C', M')

```

or approximate:
```

(C, P) ↦_τ (C', M')   with similarity threshold τ

```

### **Matching algorithm**
- exact match first,
- then approximate match using similarity operator `~`,
- then fallback rules.

### **Conflict resolution**
In case multiple rules match:
- Prioritise most specific pattern,
- or highest similarity,
- or use weighted random selection (stochastic physics).

The interpreter stores rules in a **pattern trie** for fast retrieval.

---

# 7. Time model

Time is discrete:
```

t = 0, 1, 2, ...

```

Each tick triggers:
- one syntactic reduction wave,
- one δ-evolution wave.

This makes λΔ simulations:
- deterministic or stochastic depending on rules,
- parallel,
- emergent.

---

# 8. Spatial model (optional)

Possible spatial embeddings:

### **1. 1D chain**
Useful for:
- wave equation,
- oscillator chains,
- simple automata.

### **2. 2D lattice**
Useful for:
- Turing patterns,
- reaction–diffusion,
- cellular automata,
- fluid-like behaviours.

### **3. 3D lattice**
Useful for:
- field visualisation,
- emergent metric experiments,
- toy cosmology.

### **4. Arbitrary graph**
Useful for:
- neural λΔ-networks,
- irregular physics,
- adaptive topology.

The **Neighborhood Operator** computes:
```

N(x) = { y | edge(x, y) }

```
and passes neighbor states into the δ-context.

---

# 9. Memory & Fixpoints

Fixpoints introduce persistent patterns.

Interpreter behaviour:
- `Fix F` is unfolded only as needed,
- Memoisation ensures efficient repeated self-application,
- δ may stabilise fixpoints into stationary patterns.

This is the foundation for:
- oscillators,
- attractors,
- stable system states,
- memory as equilibrium (see `05-computation/memory-as-fixpoint.md`).

---

# 10. Example execution (sketch)

Let
```

M = δ_{C0} [ Osc(a, v) ]

```

Tick steps:

### **t = 0**
Parser loads term.  
No β-steps.

### **t = 1**
δ-rule:
```

(C, Osc(a, v)) ↦ (C, Osc(a+v, v-a))

```
→ new oscillator state emerges.

### **t = 10**
Stable?  
If oscillation amplitude no longer changes beyond threshold → unbox.

Thus a stabilised limit cycle or fixed point appears.

---

# 11. Separation of concerns

To avoid a monolithic design:

### **Interpreter core**
- pure λ-reduction,
- pure δ-mechanics,
- rule engine,
- fixpoints.

### **Physics modules**
- δ-rule sets for waves, fields, oscillators, metrics.

### **Simulator backend**
- discrete time loop,
- grid/graph updates,
- rendering.

### **Experiment DSL**
Eventually allow something like:
```

world {
space 2D, size 256;
rule-set wave-equation;
initial oscillator at (30,40) with a=0.1, v=0.3;
}

```

This DSL is optional; the core remains minimal.

---

# 12. Summary

The λΔ interpreter:

- operationalises λΔ semantics,
- provides a consistent time & context model,
- supports optional spatial embedding,
- executes δ-rules deterministically or stochastically,
- enables physical and computational experiments,
- remains modular enough for future extensions.

The next files in this folder should naturally be:

1. `vm-design.md` → data structures + bytecode model  
2. `discrete-evolution-engine.md` → timesteps, parallel updates  
3. `examples.md` → oscillator chain, reaction–diffusion, emergent metric  

