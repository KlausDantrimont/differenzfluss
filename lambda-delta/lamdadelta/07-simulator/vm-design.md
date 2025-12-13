# λΔ Virtual Machine (VM) Design
**Directory:** `07-simulator/`  
**Status:** Technical specification

The λΔ Virtual Machine provides a low-level execution substrate for running λΔ-programs efficiently.  
It translates high-level λΔ terms into a small instruction set, manages memory, stack frames, δ-contexts, and discrete-time updates.

It is *not* mandatory for all λΔ simulations, but it enables:
- optimisation,
- incremental evaluation,
- interactive experiments,
- large-scale field simulations,
- embedding λΔ into external engines (e.g. Python or C++).

---

# 1. VM Overview

The VM is a **graph-based reduction machine** with:

- a **heap** storing λΔ term nodes,
- a **stack** for application and lambda evaluation,
- a **δ-context table** for evolution rules,
- a **scheduler** (driven by the Discrete Evolution Engine),
- an **instruction pipeline** for both λ and δ steps.

The VM is designed to follow the structure of a classical SECD / CEK machine —  
but extended for δ-evolution, fixpoints, and similarity operations.

---

# 2. Core Components

The VM maintains the following structures:

```

VM {
Heap           // all λΔ nodes
EnvStack       // variable bindings
ControlStack   // pending computations
DeltaTable     // δ-context → rule mappings
FixMemo        // memoisation for Fix
ContextStore   // world-level and local contexts
SpaceModel     // optional spatial embedding
Scheduler      // orchestrates time steps
}

```

Each component is described below.

---

# 3. Heap: Graph of λΔ Nodes

All terms are represented as **nodes with tagged constructors**:

```

NodeKind = VAR | LAMBDA | APP | DELTA | COMPOSE | FIX

```

Example:

```

Node {
kind: LAMBDA
var: x
body: pointer_to_node
}

```

Nodes may also store optional metadata:
- unique ID,
- position (x,y,z),
- similarity profile,
- cached reductions,
- history/logging data.

The heap allows *graph sharing* for common subterms → efficient recursive structures.

---

# 4. Execution Model

The VM uses a **dual-cycle model**:

### **(1) λ-Cycle**  
Handles β-reduction, fix/unfold, composition, congruence.

### **(2) δ-Cycle**  
Handles context evolution, δ-rules, stabilisation, spatial embedding.

This mirrors the two-phase model of the Discrete Evolution Engine.

Each instruction is classified as either:

- **L-instruction** (λ-structural)
- **D-instruction** (δ-evolutional)

---

# 5. Instruction Set

The VM instruction set is intentionally small.

---

## **5.1 Structural Instructions (λ-part)**

| Instruction | Meaning |
|-------------|---------|
| `LAMBDA x, body` | Push a lambda node |
| `APPLY` | Evaluate function application |
| `BETA` | Perform (λx.M) N reduction |
| `LOOKUP x` | Read variable from EnvStack |
| `PUSH_ENV x := v` | Extend environment |
| `POP_ENV` | Restore environment |
| `FIX_UNFOLD` | Replace `Fix F` → `F(Fix F)` |
| `COMPOSE` | Evaluate left ∘ right |

These are executed during the "λ-wave" of each timestep.

---

## **5.2 δ-Instructions (contextual / physical)**

| Instruction | Meaning |
|-------------|---------|
| `DELTA_ENTER C` | Begin δ-context evaluation |
| `DELTA_MATCH` | Determine applicable δ-rule |
| `DELTA_APPLY` | Apply δ-rule → update term & context |
| `DELTA_STABLE?` | Check stabilisation predicate |
| `DELTA_UNBOX` | Convert δ_C[M] → M |
| `CTX_INJECT` | Inject global + local context |
| `CTX_UPDATE` | Store updated context |
| `SIM_MATCH` | Similarity-based approximate pattern match |

These execute once per tick on all δ-wrapped terms.

---

# 6. Environment & Control Stacks

The VM uses a dual-stack model:

---

### **EnvStack**
Holds variable bindings:

```

(x := node_pointer)

```

Upon calling a lambda, the VM performs:

```

PUSH_ENV x := argument
...
POP_ENV

```

---

### **ControlStack**
Stores pending computations:

- return addresses,
- suspended applications,
- evaluation continuations.

Typical items:

```

APPLY(node_left)
EVAL(node_right)
RETURN(node_result)

```

This mirrors CEK/SECD style control flow.

---

# 7. δ-Rule Execution Model

δ-rules are stored in a **pattern table**:

```

DeltaTable: map<Pattern, RuleHandler>

```

A δ-step performs:

1. **Context injection**  
   (global time, space, neighbor states, parameters)

2. **Exact match attempt**  
   `DELTA_MATCH`

3. **Approximate match (if needed)**  
   using the Similarity Operator `~`.

4. **Apply rule handler**  
   → produces new `(C', M')`.

5. **Stability check**  
   → if stable, unbox.

The VM guarantees δ-operations are:

- atomic per term,
- logically parallel across terms,
- deterministic unless rule set declares randomness.

---

# 8. Fixpoint Handling

Fixpoints are handled with a memoisation table:

```

FixMemo : map<Node, Node>

```

Whenever the VM encounters `Fix F`, it:

1. Checks if F is already memoised.
2. If not, unfolds:
```

Fix F → F(Fix F)

```
3. Stores resulting node in memo table.

This ensures stable attractors, recursive definitions, and oscillators remain efficient.

---

# 9. Spatial Model Integration

If the simulator uses space, the VM includes:

```

SpaceModel {
positions: map<NodeID → (x,y,z)>
neighbors: map<NodeID → list<NodeID>>
metric: optional tensor field
}

```

Spatial functions:

- `NEIGHBORS(id)` → adjacency list
- `GRADIENT(id)` → approximate gradient from neighbor values
- `DISTANCE(id1, id2)` → used for similarity or metric experiments

The VM does *not* enforce geometry—  
it simply provides the substrate.

---

# 10. Scheduler Interface

The VM receives scheduling commands from the Discrete Evolution Engine:

```

SCHEDULE_LAMBDA_WAVE
SCHEDULE_DELTA_WAVE
SCHEDULE_SPATIAL_UPDATE
SCHEDULE_RENDER

```

The VM must obey:

- λ-wave executes until no progress possible,
- δ-wave executes one δ-step per active δ-term,
- spatial update executes once per cycle.

The scheduler allows:

- synchronous simulations,
- asynchronous/randomised updates,
- block/grid-partitioned updates,
- multi-timescale evolution.

---

# 11. Bytecode Option (optional extension)

Although λΔ is not inherently designed for bytecode, the VM can implement one:

### Example bytecode instructions:

```

LOAD_VAR x
LOAD_LAMBDA x, addr
APPLY
REDUCE_BETA
ENTER_DELTA C_addr
DELTA_RULE rule_id
END_DELTA
FIX_UNFOLD
END

```

This is optional but enables:

- JIT compilation,
- embedding λΔ into game engines,
- efficient field simulations (NumPy/GPU backend).

---

# 12. VM as a Meta-Interpreter

The VM is deliberately transparent:  
it exposes internal states (heap, stacks, contexts), enabling:

- tracing,
- debugging,
- emergent behaviour extraction,
- comparison to other rewriting systems,
- meta-simulation (λΔ running inside λΔ).

---

# 13. Summary

The λΔ Virtual Machine:

- provides a concrete execution model for the abstract semantics,  
- separates λ-structure from δ-evolution,  
- manages environments, control flow, and contexts,  
- integrates optional space and similarity mechanics,  
- supports fixpoints through memoisation,  
- is compatible with synchronous and asynchronous simulation modes.

Together with:

- `interpreter-concept.md`, and  
- `discrete-evolution-engine.md`

the VM forms the **computational substrate** of λΔ.

