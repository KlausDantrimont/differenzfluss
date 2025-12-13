# 📄 **`02-operators/similarity-operator.md`**


# The Similarity Operator `~`
### Context-Dependent Structural Resemblance in the λΔ-Calculus

Similarity is a foundational concept in the λΔ-calculus.  
It ensures that Δ produces *recognizable variations* and λ produces *coherent stabilizations*.  
Unlike equality, similarity is **context-dependent, structural, graded, and dynamic**.

This document defines similarity in its general, formal, and domain-independent form.

---

# 1. Core Idea

Similarity is not a single absolute relation.  
Instead, it is a **family** of relations parameterized by a *context*:

```

E ~_C F

```

Meaning:

> “E and F are structurally similar within context C.”

Contexts may represent:
- perceptual frames
- coordinate systems
- resolutions or scales
- conceptual or categorical schemes
- physical gauges or boundary conditions
- cognitive or social narratives
- internal λΔ states (e.g., memories, constraints)

Similarity is therefore **relational** and **perspectival**, not global.

---

# 2. Formal Definition

Similarity is a context-indexed relation:

```

~_C  ⊆ Expr × Expr

```

with the following axioms.

---

## 2.1 Reflexivity (Contextual)

```

E ~_C E

```

Every expression is similar to itself in any context.

---

## 2.2 Symmetry

```

E ~_C F  →  F ~_C E

```

Similarity does not depend on ordering.

---

## 2.3 Weak Transitivity (Context-Limited)

Similarity chains propagate *unless* the distance becomes too large:

```

E ~_C F   and   F ~_C G
→ E ~_C G    unless Δ_C(E, G) is maximal

```

This prevents trivialization (i.e., everything becoming similar to everything else).

---

## 2.4 Structural Compatibility (Operator-Level Similarity)

If E and F share the same operator structure:

```

E = op(E1, E2, ..., En)
F = op(F1, F2, ..., Fn)

```

then:

```

E ~_C F    iff    Ei ~_C Fi for all i

```

This makes `~` a **morphological relation**.

---

# 3. Context C as a λΔ Expression

The context C may encode:

- what counts as a relevant feature  
- what kinds of variations are allowed  
- a particular scale or resolution  
- constraints or boundary conditions  
- a conceptual interpretation  
- a physical gauge/frame  
- an observer’s perspective  
- a temporal or historical state  

Contexts themselves evolve under Δ and λ:

```

C →Δ C1       (context expansion)
C →λ C2       (context consolidation)

```

Thus similarity is **dynamic**.

---

# 4. Δ-Compatibility (Variation Must Preserve Identity)

Δ generates variation:

```

Δ(E) → (E1, E2)

```

Similarity constrains this:

```

E1 ~_C E
E2 ~_C E

```

Interpretation:

> Δ may vary structure, but must not break identity within context C.

This ensures Δ does not explode into unrelated configurations.

---

# 5. λ-Compatibility (Stabilization Must Preserve Coherence)

λ produces coherent unifications:

```

λ(E, F) → G

```

Similarity ensures:

```

G ~_C E
G ~_C F

```

Interpretation:

> λ finds a structurally coherent successor within context C.

This prevents λ from collapsing structure into triviality.

---

# 6. Fixpoint Preservation

If X is a stable expression under λ:

```

λ(X, X) = X

```

then similarity must consider X identical to itself over time:

```

X ~_C X

```

This models:

- identity  
- memory  
- persistent features  
- stable particles  
- roles and norms  
- cognitive attractors  

---

# 7. Canonical Construction (If Needed)

A canonical definition of similarity that satisfies all axioms:

```

E ~_C F
iff
there exists a finite Δ/λ-sequence from E to F
that does not leave context C.

```

Symbolically:

```

E = X0 → X1 → ... → Xk = F
with each Xi+1 obtained by Δ or λ under context C.

```

This captures the idea that similarity = **reachable via structural transformations**.

---

# 8. Optional: Graded Similarity

For physics, cognition, or machine-learning integrations:

```

sim_C(E, F) ∈ [0, 1]

```

Then:

```

E ~_C F   iff   sim_C(E, F) ≥ τ_C

```

where τ_C is a context-defined threshold.

λ then becomes:

```

λ(E, F) → G such that sim_C(G, E) and sim_C(G, F) are maximized.

```

Δ becomes:

```

Δ(E) → (E1, E2) such that sim_C(E1, E) and sim_C(E2, E) remain above τ_C.

```

---

# 9. Context-Free Similarity (Special Case)

If C = ∅ (the empty context), we get the *weakest possible* similarity relation.

This is useful for minimal or universal λΔ interpretations.

---

# 10. Summary

Similarity in the λΔ calculus is defined as:

```

~_C : Expr × Expr → {true, false}

```

with properties:

- reflexive  
- symmetric  
- weakly transitive  
- structurally recursive  
- Δ-compatible  
- λ-compatible  
- fixpoint-preserving  
- context-dependent  
- dynamic  
- domain-independent  

**Without similarity, Δ would explode and λ would collapse.  
With similarity, the λΔ-calculus becomes a coherent engine for emergence.**
