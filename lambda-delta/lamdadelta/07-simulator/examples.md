# λΔ Examples
**Directory:** `08-examples/`  
**Status:** Overview + runnable conceptual prototypes

This document collects illustrative examples demonstrating how λΔ behaves in simulation.  
Each example is self-contained and highlights one conceptual feature:

- oscillation (self-sustaining recursion),
- spatial propagation (waves),
- reaction–diffusion (Turing patterns),
- emergent metric fields,
- recursive split/merge processes,
- computational structures.

Every example includes:

1. **The λΔ expression**,  
2. **The δ-rule set**,  
3. **Expected behaviour**,  
4. **Notes for implementation in the simulator**.

---

# 1. Simple Oscillator (1D)
A canonical example showing recursive evolution and δ-updates.

## 1.1 Term
```

Osc := δ_C [ Osc(a, v) ]

```

## 1.2 δ-rule
A harmonic oscillator update:
```

(C, Osc(a, v)) ↦ (C, Osc(a + v, v - a))

```

## 1.3 Expected behaviour
- Oscillation in phase space `(a, v)`.
- Limit cycles appear depending on numerical ranges.
- Stabilisation criterion:  
  amplitude change < ε for N steps → freeze into `Osc_stable`.

## 1.4 Notes
- Ideal to test the VM’s δ-pipeline.
- Reveals performance bottlenecks in the interpreter.

---

# 2. 1D Wave Propagation
Minimal discrete wave equation.

## 2.1 Initial field
For grid positions `x ∈ ℤ`:
```

Field(x) := δ_C [ A(x), V(x) ]

```

Where `A` = amplitude, `V` = velocity.

## 2.2 δ-rule
```

V'(x) = V(x) + k * ( A(x+1) - 2*A(x) + A(x-1) )
A'(x) = A(x) + V'(x)

```

Represented as:
```

(C, Field(A, V)) ↦ (C, Field(A', V'))

```

## 2.3 Expected behaviour
- Propagating waves,
- Interference patterns,
- Boundary reflections for fixed edges.

## 2.4 Notes
- Shows how δ uses neighbourhood contexts.
- Good test for spatial context injection.

---

# 3. 2D Reaction–Diffusion (Turing Patterns)
A more elaborate emergent structure.

## 3.1 Term
Each cell contains two chemical species:
```

Cell := δ_C [ Chem(U, V) ]

```

## 3.2 δ-rule (Gray–Scott style)
```

U' = U + D_u ∆U - U*V² + F*(1 - U)
V' = V + D_v ∆V + U*V² - (F + k)*V

```

Written in λΔ-dispatch form:
```

(C, Chem(U, V)) ↦ (C, Chem(U', V'))

```

## 3.3 Expected behaviour
- Spots, stripes, labyrinths,
- Parameter-sensitive morphologies,
- Pattern bifurcations.

## 3.4 Notes
- Tests heavy δ-load and neighbour access.
- Good benchmark for the VM and evolution engine.

---

# 4. Emergent Metric Field (DFT-inspired)
Emergence of distance from similarity.

## 4.1 Term
Each node carries a local “shape descriptor” `S`:
```

Node := δ_C [ MetricNode(S, M) ]

```

Where `M` is the current estimate of metric values.

## 4.2 δ-rule
Let similarity determine curvature-like adjustments:
```

M' = Relax( M, ∑_neighbors f( Sim(S, S_neighbor) ) )

```

In λΔ form:
```

(C, MetricNode(S, M)) ↦ (C, MetricNode(S, M'))

```

## 4.3 Expected behaviour
- metric tensor emerges gradually,
- clusters → low distance,  
- discontinuities → high curvature,
- non-linear topology if non-Euclidean relaxations used.

## 4.4 Notes
- Demonstrates λΔ → geometric emergence.
- Bridges to physics chapter.

---

# 5. Recursive Split/Merge Automaton
Structural recursion in pure λΔ.

## 5.1 Term
```

Tree := Fix( λ self . δ_C [ Node(value, self(left), self(right)) ] )

```

## 5.2 δ-rule
Probabilistic branching:
```

(C, Node(v, L, R)) ↦
with p:  Node(v+1, L,    R )
with q:  Node(v-1, L,    R )
with r:  Node(v,   self, R )
with s:  Node(v,   L,   self)

```

## 5.3 Expected behaviour
- random walk of tree shape,
- fractal-like fluctuations,
- stabilisation once height variation < ε.

## 5.4 Notes
- Exercises fixpoint unfolding + δ-stochasticity.
- Very sensitive to scheduling choices.

---

# 6. Turing-Complete Embedding (λΔ → TM)
See also: `05-computation/turing-machines.md`.

## 6.1 Term (sketch)
```

Tape := δ_C [ TapeCell(symbol, left, right) ]
Controller := δ_C [ State(q, headpos) ]

```

## 6.2 δ-rule
Implements TM transition:
```

(q, symbol) → (q', symbol', move)

```

## 6.3 Expected behaviour
- formal demonstration of computability,  
- useful for regression tests of the interpreter.

## 6.4 Notes
- λΔ’s mix of λ-structure + δ-evolution expresses TMs concisely.
- Stability detection corresponds to halting.

---

# 7. Multi-Oscillator Synchronisation (Kuramoto-like)
Collective behaviour from coupled oscillators.

## 7.1 Term
```

Osc_i := δ_C [ Osc(θ_i, ω_i) ]

```

## 7.2 δ-rule
Phase-coupling:
```

θ_i' = θ_i + ω_i + K * ∑_j sin(θ_j - θ_i)

```

## 7.3 Expected behaviour
- transition from incoherence → synchrony,
- cluster synchronisation for heterogeneous ω_i.

## 7.4 Notes
- Tests similarity operator for phase comparison.
- Good candidate for GPU acceleration.

---

# 8. Energy Minimisation (Gradient Flow)
δ as a descent operator.

## 8.1 Term
```

Node := δ_C [ State(x) ]

```

## 8.2 δ-rule
```

x' = x - η * ∂E/∂x

```

## 8.3 Expected behaviour
- convergence to minima,  
- possibility of oscillations, saddle escape.

## 8.4 Notes
- δ plays role analogous to time evolution in physics.

---

# 9. Example Index Summary

| Example | Key Concept | Tests Which Subsystems |
|---------|-------------|------------------------|
| Simple Oscillator | recursion + δ | VM core, fixpoints |
| 1D Wave | neighbour context | spatial model |
| Reaction–Diffusion | PDE approximation | heavy δ-load, diffusion |
| Emergent Metric | similarity + geometry | similarity operator, relaxations |
| Split/Merge Tree | stochastic recursion | fixpoint unfolding, δ-stochasticity |
| Turing Machine | computation | correctness of interpreter |
| Kuramoto Model | synchronisation | neighbourhood coupling, similarity |
| Gradient Flow | optimisation | δ as physical law |

---

# 10. How to Add New Examples

Create a new `.md` or `.ld` (lambda-delta) file with sections:

```

# Name

## Term

## δ-rules

## Expected behaviour

## Implementation notes

```

Then link it from this index.

---

# 11. Summary

This document provides a catalogue of λΔ examples that:

- exercise fundamental subsystems of the interpreter,  
- illustrate emergent behaviours,  
- show physical and computational expressiveness,  
- serve as regression tests and inspiration.

These examples will grow as λΔ evolves further.
