# Brillenladen – Technical Overview

## Problem

Large Language Models can analyze the same problem in very different ways.

They may focus on causes, time, incentives, power, information, evidence, feedback, scale, perspective, institutions, or other structures.

Usually this choice remains implicit.

The user sees the answer, but not necessarily the analytical cut that produced it.

Common instructions such as:

> Be critical.  
> Think like an expert.  
> Analyze this deeply.

provide only weak control over the actual reasoning perspective.

The **Brillenladen** proposes a small explicit layer between problem and reasoning.

## Core idea

Represent analysis perspectives as compositions of relatively elementary **epistemic operators**.

Examples:

- `TIME` — How does X change?
- `STATE` — What configuration currently exists?
- `RELATION` — What is connected to what?
- `CAUSALITY` — What changes what?
- `PERSPECTIVE` — How does X appear from another observer position?
- `INFORMATION` — Who knows what, when, and through which channels?
- `EVIDENCE` — What supports this claim?
- `INCENTIVE` — What consequences make behavior attractive or unattractive?
- `POWER` — Who can change whose action space?
- `FEEDBACK` — How do effects return to their own causes or conditions?
- `SCALE` — What changes when the level of observation changes?
- `EMERGENCE` — What appears only through interaction between parts?

These operators are not claims about what reality consists of.

They are instructions for **how to inspect a problem**.

## Composition

A useful perspective can be built by combining operators.

```text
Intermittent software latency
=
TIME
+ STATE
+ RELATION
+ INFORMATION
```

Why?

- `TIME`: the problem is intermittent.
- `STATE`: a restart apparently resets something.
- `RELATION`: isolated component optimization has failed.
- `INFORMATION`: current metrics may not observe the relevant internal state.

The result is not a complete answer.

It is a **structured search direction**.

## Runtime model

```text
Problem
↓
Identify central uncertainty
↓
Select small operator set
↓
Construct perspective
↓
Analyze
↓
Inspect residual problem
↓
Add / switch operator if useful
↓
Stop when marginal value falls
```

The objective is:

> **As little epistemic structure as possible, as much as needed for useful orientation.**

## Meta-operators

- `LENS_SELECTION`
- `LENS_SWITCH`
- `PARALLEL_VIEW`
- `SYNTHESIS`
- `TENSION`
- `BLIND_SPOT`
- `BUDGET`

These make perspective selection inspectable instead of purely implicit.

## Epistemic budget

Additional perspectives consume context, computation, attention, time, and interpretive complexity.

The system should ask:

> Which next epistemic operation promises the largest additional orientation per unit of cost?

Sometimes the best next step is another operator.

Sometimes it is more evidence.

Sometimes it is to stop.

## Inverse operation: epistemic factorization

The same vocabulary can be used in reverse.

Input:

- report,
- strategy paper,
- political speech,
- scientific text,
- conflict narrative,
- AI answer.

Question:

> Which epistemic operators structure this representation?

Example:

```text
Narrative
≈
CAUSALITY
+ INCENTIVE
+ ROLE
```

or:

```text
Narrative
≈
TIME
+ INSTITUTION
+ FEEDBACK
```

The goal is to find a **small set that explains the characteristic analytical viewpoint**.

## Why this may matter for AI systems

```text
User / Application
↓
Problem / Question / Text
↓
Epistemic layer
- operators
- lens construction
- factorization
- blind-spot analysis
- budget
↓
Reasoning system
- analysis
- search
- hypotheses
- simulation
- synthesis
```

The layer does not determine the answer.

It structures the **space of preferred reasoning moves**.

## Minimal usage example

Input:

> Customer complaints about failures are increasing. Internal telemetry shows no increase in error rate.

Possible operator selection:

```text
INFORMATION
CONCEPT
PERSPECTIVE
SCALE
EVIDENCE
```

Questions:

- Are customers and telemetry observing the same event?
- What counts internally as an “error”?
- Which failures are visible to customers but invisible to instrumentation?
- Is aggregation hiding a local problem?
- What observation would distinguish “customers are mistaken” from “measurement is blind”?

Same model. Same world knowledge. Different cuts.

## Status

The Brillenladen is an experimental design.

The operator set is not claimed to be complete or mathematically independent.

The intended test is practical:

> Do small explicit operator sets help AI systems construct, compare, inspect and revise analysis perspectives?

Early experiments with several current models suggest that they can.

That is not proof of a general theory.

It is enough for a prototype.

## One-line definition

> **The Brillenladen is a compositional catalog of epistemic operators for constructing and reconstructing AI analysis perspectives.**
