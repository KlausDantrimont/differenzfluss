
# Composition in the λΔ-Calculus
### How Expressions, Operators, and Contexts Combine to Produce Emergent Structure

Composition is the connective tissue of the λΔ-calculus.  
Δ generates variation, λ stabilizes coherence, C shapes both —  
but **composition** determines how these transformations propagate  
through compound expressions, contexts, operators, and meta-operators.

This document defines:

- expression composition  
- operator composition  
- context composition  
- Δ–λ mixed flows  
- meta-composition  
- invariants and reduction interactions  

---

# 1. Expression Composition

Expressions may be combined structurally:

```

op(E1, E2, ..., En)

```

Reduction distributes over the structure unless prohibited by context.

### Δ-Distribution
```

Δ_C(op(E1,...,En))
→ (op(E1',...,En), op(E1'',...,En))

```

Where:

```

(E1', E1'') = Δ_C(E1)

```

and similarly for Ei if variation is allowed by context C.

### λ-Distribution
λ acts componentwise when coherence is structurally meaningful:

```

λ_C(op(E1,...,En), op(F1,...,Fn))
→ op(G1,...,Gn)

```

where each:

```

Gi = λ_C(Ei, Fi)

```

if the operator `op` preserves structure in context C.

### Similarity Propagation
```

op(E1,...,En) ~_C op(F1,...,Fn)
iff
Ei ~_C Fi  for all i

```

A context may override or extend this rule.

---

# 2. Sequential Composition

Standard rewriting closure:

```

E → F
F → G
-----

E → G

```

This applies to Δ, λ, fix, context evolution, and meta-operators.

---

# 3. Mixed Operator Composition (Δ–λ Loop)

The fundamental dynamical pattern:

```

E
→Δ_C→ (E1, E2)
→λ_C→ G
→Δ_C→ ...

```

Combined rule:

```

E →Δ_C (E1, E2)
(E1, E2) →λ_C G
---------------

E → G

```

Interpretation:

> Δ explores; λ selects; C constrains.  
> Composition yields emergence.

---

# 4. Operator Composition (Higher-Order)

Operators themselves may be composed:

```

(λ_C ∘ Δ_C)(E)   =   λ_C( Δ_C(E) )

```

or:

```

O₁ ∘ O₂ : Expr → Expr

```

Composition follows standard functional composition:

```

(O₁ ∘ O₂)(E) = O₁( O₂(E) )

```

Meta-operators naturally act here (see meta-operators.md).

---

# 5. Context Composition

Contexts combine to form joint frames:

```

C₁ ⊗ C₂

```

Requirements for C₁ ⊗ C₂:

1. It is a valid context  
2. It defines combined similarity:
```

E ~_(C₁⊗C₂) F   iff   (E ~₍C₁₎ F) and (E ~₍C₂₎ F)

```
or a weighted merger depending on domain.

3. It defines combined variation space:
```

V_(C₁⊗C₂) = V_C₁ ∩ V_C₂   (restrictive)
or
V_C₁ × V_C₂ (expansive)

```

4. Combined variance metric:
```

Var_(C₁⊗C₂) = f(Var_C₁, Var_C₂)

```

Interpretation:

> C₁ ⊗ C₂ fuses perspectives, constraints, or frames.

Examples:

- physical ⊗ semantic  
- local ⊗ global  
- micro ⊗ macro  
- agent ⊗ environment  

---

# 6. Fixpoint Composition

Fixpoints can be composed when contexts and transformations align:

```

fix_C(E) = X
fix_C(F) = Y
------------

fix_C( λ_C(E, F) ) = fix_C( λ_C(X, Y) )

```

Fixpoint stability interacts with expression composition:

```

fix_C( op(E1,...,En) )
= op( fix_C(E1), ..., fix_C(En) )

```

if the operator respects context.

Cyclic fixpoints compose by phase synchronization:

```

k-cycle and m-cycle → lcm(k, m)-cycle

```

---

# 7. Meta-Composition

Meta-operators also compose:

```

M₁ ∘ M₂ : Operator → Operator

```

Example:

```

(M₁ ∘ M₂)(Δ_C) = M₁( M₂(Δ_C) )

```

Meta-operators can participate in Δ and λ flows:

```

Δ_C(M) → (M1, M2)
λ_C(M1, M2) → M*

```

Thus the entire system is self-modifying at multiple levels.

---

# 8. Commutativity and Non-Commutativity

### Δ and λ generally **do not commute**:

```

λ_C( Δ_C(E) )  ≠  Δ_C( λ_C(E) )

```

This asymmetry is the source of:

- emergent complexity  
- oscillators  
- chaotic attractors  
- stabilization-driven novelty  

### Context shifts may reorder reductions:

```

C → C'
Δ_C(E) may differ from Δ_C'(E)
λ_C(E,F) may differ from λ_C'(E,F)

```

Thus composition is **context-sensitive**.

---

# 9. Normalization and Canonical Flows

A canonical reduction step is:

```

E →Δ_C→ (E1, E2) →λ_C→ E*

```

or compactly:

```

E ⇒_C E*

```

A full system evolves by iterating this composed transformation.

Fixed points satisfy:

```

E* ⇒_C E*

```

Cycles satisfy:

```

E ⇒_C E1 ⇒_C E2 ⇒_C ... ⇒_C E

```

---

# 10. Summary

Composition in the λΔ-calculus determines:

- how structure propagates  
- how Δ and λ interact  
- how similarity spreads across expressions  
- how contexts combine  
- how fixpoints emerge  
- how operators modify other operators  
- how meta-dynamics unfold  

It is the backbone of λΔ as a **process calculus**.

In short:

> **Without composition, the operators are static.  
> With composition, they become a universe.**
