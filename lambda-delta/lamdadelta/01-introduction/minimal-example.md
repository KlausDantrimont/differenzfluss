# Minimal Example  
### A Tiny Δ–λ–C System in Action

To make the λΔ-calculus intuitive,  
here is the smallest possible example of a system that uses:

- **Δ₍C₎** — contextual differentiation  
- **λ₍C₎** — contextual stabilization  
- **~₍C₎** — contextual similarity  
- **C** — the context that shapes both operators  

We choose a very simple context:

```

C:

* Similarity: x ~₍C₎ y  iff |x - y| ≤ 1
* Allowed variation (Δ): ±1
* Stability target (λ): values near 0

```

This context says:

- “Small differences don't matter”  
- “Variations must stay within ±1”  
- “Stable structures are those close to 0”

---

# 1. Starting Point

Let the initial expression be:

```

E = 0

```

---

# 2. Apply Δ₍C₎ (Differentiation)

Δ₍C₎ generates context-valid variations:

```

Δ₍C₎(0) → (-1, +1)

```

Both -1 and +1 are:

- similar to 0 in context C  
- allowed by the variation rule  
- different from each other  

Δ creates **two possibilities**.

---

# 3. Apply λ₍C₎ (Stabilization)

Now λ₍C₎ tries to find a more coherent,  
more stable successor of -1 and +1.

Given the context's stability preference (toward 0):

```

λ₍C₎(-1, +1) → 0

```

0 is similar to both -1 and +1  
and minimizes the contextual variance.

λ restores **coherence**.

---

# 4. The Minimal Δ–λ Cycle

Putting it together:

```

0
→Δ→ (-1, +1)
→λ→ 0
→Δ→ (-1, +1)
→λ→ 0
...

```

This is a **1-cycle fixpoint**:

- Δ keeps generating two possibilities,  
- λ keeps stabilizing them back to 0.

Even in this toy system, we already see:

- variation  
- stabilization  
- identity under change  
- context-dependence  
- emergent stability

---

# 5. Changing the Context Changes the Dynamics

If we modify the context to prefer values near **1** instead of 0:

```

C':

* Stability target ~1
* Same variation and similarity rules

```

Then:

```

Δ₍C'₎(1) → (0, 2)
λ₍C'₎(0, 2) → 1

```

Again a 1-cycle,  
but now the **stable point has shifted**.

Changing C changes the system  
without touching Δ or λ themselves.

---

# 6. A True Oscillator (2-cycle)

With a context that prefers:

- “values near 0 unless both signals are far positive”

we get:

```

1
→Δ₍C₎→ (-1, 3)
→λ₍C₎→ 2
→Δ₍C₎→ (0, 4)
→λ₍C₎→ 1
→ ...

```

This yields a **2-cycle fixpoint**:

```

1 ↔ 2

```

The system does not settle;  
it **oscillates** in a stable pattern.

---

# 7. Why This Matters

Even this microscopic example illustrates:

- Δ explores structured possibilities.  
- λ stabilizes what is coherent.  
- C shapes both exploration and stabilization.  
- The dynamics are emergent.  
- Changing the context changes the behavior.  
- Fixpoints and cycles appear naturally.  

This is the essence of the λΔ-calculus:

> Through Δ and λ acting inside a context,  
> emergence becomes a natural, minimal consequence  
> rather than a special-case phenomenon.

