# Recursive Split–Merge Automaton in λΔ

**Directory:** `08-examples/`  
**Status:** Structural, stochastic example – fixpoints + δ-evolution

This example demonstrates how λΔ can express **recursive, branching structures** whose evolution is defined by δ-rules.  
It highlights the interplay between:

- **Fixpoints** (self-application as structural recursion),
- **Stochastic δ-rules** (non-deterministic evolution),
- **Tree-like emergent morphologies** (fractal or fluctuating).

Unlike the oscillator or reaction–diffusion systems, this example is **not numeric**, but **structural**:  
it evolves a *shape* rather than a field.

---

## 1. Conceptual Overview

We construct a recursively defined tree-like structure.  
Each node carries:

- a value `v` (e.g. height, mass, size),
- two substructures `L` (left) and `R` (right).

Under δ-evolution, each node may:

1. **stay the same**,  
2. **increase its value**,  
3. **decrease its value**,  
4. **grow** (replace one branch with a recursive call),  
5. **shrink** (replace one branch with a terminal element).

This allows patterns such as:

- random exploration of tree shapes,
- alternating growth / shrinkage cycles,
- fluctuating fractals,
- emergence of balanced vs. skewed shapes,
- slow drift toward certain morphologies governed by δ-statistics.

---

## 2. λΔ Term Structure

We define a recursive tree as a fixpoint:

```text
Tree :=
  Fix ( λ self .
          δ_C [
            Node(v, self(left), self(right))
          ]
      )
````

Interpretation:

* `Fix` provides a self-referential generator of structure.
* `self(left)` and `self(right)` produce recursive subtrees.
* `Node(v, L, R)` is the structural container.
* The outer `δ_C[...]` determines *how* the tree evolves over time.

The context `C` may include:

* branch identifiers,
* depth,
* randomness seeds,
* parameters controlling probabilities.

---

## 3. δ-Rule Specification

We define a **stochastic** set of δ-rules for a node:

```text
(C, Node(v, L, R)) ↦ (C, NewNode)
```

with several alternatives, chosen according to probabilities stored in `C`:

### 3.1 Value fluctuations

Increase or decrease the value:

```text
v' = v + 1      with probability p
v' = v - 1      with probability q
```

### 3.2 Structural modification

Modify one branch using the recursive generator:

```text
L' = self(left)   with probability r
R' = self(right)  with probability s
```

Or shrink:

```text
L' = Leaf         with probability t
R' = Leaf         with probability u
```

### 3.3 No change

With probability (1 − p − q − r − s − t − u):

```text
Node(v, L, R) stays unchanged
```

### 3.4 Combined rule (λΔ notation)

We write the δ-rule schematically as:

```text
(C, Node(v, L, R)) ↦ (C, Node(v*, L*, R*))
```

where `(v*, L*, R*)` are sampled according to the probabilities in `C`.

The interpreter will typically implement this via a rule handler that:

* reads parameters from `C`,
* samples a random branch,
* constructs the appropriate new node.

---

## 4. Behaviour & Dynamics

### 4.1 Fluctuating size

The scalar `v` performs a random walk:

* drifting up or down depending on (p − q),
* possibly stabilising if bounded by external constraints in `C`.

### 4.2 Fluctuating topology

Probabilities (r, s, t, u) shape the overall morphology:

* high `r` → more growth on the left,
* high `s` → more growth on the right,
* high `t` or `u` → decay and compactification,
* symmetric parameters → balanced stochastic trees,
* asymmetric parameters → skewed morphologies.

### 4.3 Fractal-like states

Under prolonged evolution, the tree exhibits:

* recursive self-similarity,
* shape “breathing” (expansion–contraction cycles),
* possibly intermittent bursts of growth or collapse depending on parameters.

---

## 5. Simulation Notes

### 5.1 Evaluation strategy

* The fixpoint expansion must be **lazy**: expand only as needed.
* The VM memoisation prevents exponential blow-up.
* δ-rules apply once per timestep to *each expanded node*.

### 5.2 Pruning / depth control

Optionally, the context may enforce:

* maximum depth,
* maximum total nodes,
* targeted pruning rules,
* or decay probability increasing with depth.

This avoids infinite tree explosion during simulations.

### 5.3 Visualisation

Tree visualisation strategies:

* simple ASCII dendrograms,
* graphical trees,
* rendering nodes as circles with size ∝ `v`,
* colour-coding subtrees by depth or age.

Time-lapse visualisations reveal the evolving morphology clearly.

---

## 6. Variants and Extensions

### 6.1 Deterministic split/merge patterns

Replace probabilities with deterministic conditions (e.g. alternate steps, parity of depth, or similarity-based conditions).

### 6.2 Spatial trees

Assign each node a spatial position and grow embedded structures:

* L grows left,
* R grows right,
* position inherited from parent ± offsets.

### 6.3 Mutating generators

Let `self` carry parameters:

```text
self(left, α), self(right, β)
```

and evolve α, β over time for adaptive behaviour.

### 6.4 Interaction between subtrees

Node values may depend on sums or differences of subtrees:

```text
v' = v + (L.value − R.value)
```

introducing feedback loops across branches.

---

## 7. Summary

This example demonstrates how λΔ can represent:

* recursive structures via `Fix`,
* stochastic δ-driven evolution,
* structural (non-numeric) emergence,
* fluctuating trees with self-similar behaviour.

It is a test of:

* the VM’s fixpoint handling,
* δ-rule dispatch,
* structural rewriting speed,
* lazy evaluation and memoisation.
