# ARC-AGI-3 LCLD Agent
# Architectural Specification — Version 10.0
# (Tri-Agent Hierarchy, Isolated Memory Contours & Brusentsov Ternary Logic)

## 0. Purpose

This document defines the Version 10.0 architecture of an ARC-AGI-3 interactive reasoning agent operating under:

- hidden environment rules and dynamic action spaces;
- deterministic object-centric perception (ARGALite + PlanningSet);
- strict offline / competition execution constraints;
- multimodal local LLM (Qwen FP8 / vLLM) used only through three isolated roles;
- **tri-agent authority separation** (Explorer, Coder, Solver);
- **strictly isolated memory contours** that prevent cross-contamination between factual discovery, syntax generation, and epistemic reasoning;
- **Brusentsov ternary logic** for empiric transition judgment (FOLLOW / NULL / OMIT);
- Double-Loop Learning with domain-specific error routing;
- dual-view observation (annotated visual frame for multimodal input, structured verifier packet for offline verification);
- offline, replayable, auditable competition agent.

The architecture is **not**:

- a single monolithic LLM prompt loop;
- a system that allows an LLM to emit or authorize final environment actions;
- a system that hallucinates unrestricted DSL execution;
- a raw-pixel policy network or generic RL learner;
- an unconstrained transformer planner;
- a hidden-state LLM controller.

The architecture **is**:

- a neuro-symbolic multi-agent system with clear separation of powers;
- an environment in which a level-specific DSL is *dynamically generated* by a dedicated Coder but *deterministically validated, sandboxed and executed*;
- a verifier-centered system that distinguishes strict physical contradictions (NULL) from insignificant / passive outcomes (OMIT) using Brusentsov’s necessary-implication semantics;
- a system that retains the PlanningSet identity contract and dual-view media of later V9 work while restoring the high-assurance isolation philosophy of V6.

### 0.1 Authority Hierarchy

Normative authority order (highest first):

1. **Environment transition and competition gateway contracts** (accepted `env.step` frames, official RESET semantics).
2. **LayeredVerifier using Brusentsov ternary logic** — absolute authority on step relevance and branch viability (FOLLOW / NULL / OMIT).
3. **GameSession** — sole mutable-state owner and orchestrator of agent calls, memory mutations, budgets and fallbacks.
4. **ActionBoundary** — only component allowed to call the real environment.
5. **SandboxExecutor** — restricted interpreter for generated DSL.
6. **VerificationBinder** — grounds DSL calls against the current PlanningSet.
7. **PlanningSet** — canonical id vocabulary for one snapshot cycle.
8. **ExplorerAgent / DSLCoder / SolverAgent** — proposers only; none may emit environment actions.

No LLM role may authorize execution. No generated Python may leave the sandbox. All identifiers must come from the PlanningSet.

### 0.2 Dual-view design intent (retained)

Each stable observation cycle produces:

- an **annotated visual frame** (PNG) for multimodal LLM input;
- a **structured verifier packet** for offline, deterministic verification and audit.

Both views share one PlanningSet identity contract for the same snapshot cycle.

---

## 1. Tri-Agent Separation of Powers & Memory Contours

### 1.1 Explorer Agent (Call 1 family)

- **Role:** factual discovery of the environment.
- **Writes only:** `EnvironmentSpecMemory`.
- **Must not receive:** level goals, epistemic judgments, syntax diagnostics, or Coder/Solver outputs.
- **Output:** `EnvironmentSpecification` (objects, relations, affordance hypotheses, action-surface facts grounded on PlanningSet ids).

### 1.2 Coder Agent (Call 2 family)

- **Role:** generate a level-specific Python DSL and function manifest.
- **Writes only:** `SyntaxErrorMemory`.
- **Must not receive:** level goals, epistemic judgments, or Solver outputs.
- **Output:** validated DSL source + function manifest; published only after static checks and sandbox publication rule.

### 1.3 Solver Agent (Call 3 family)

- **Role:** epistemic reasoning and trajectory packages over the published manifest.
- **Writes only:** `EpistemicMemory`.
- **Must not receive:** syntax / traceback diagnostics or Coder-only failure details.
- **Output:** trajectory packages that reference only published DSL functions and PlanningSet ids.

### 1.4 Isolation Invariants (normative)

- **ISO-1** Explorer never sees goals or Solver judgments.
- **ISO-2** Coder never sees goals or Solver judgments.
- **ISO-3** Solver never sees syntax tracebacks or raw Coder failures.
- **ISO-4** Memory contours are write-isolated by agent role.
- **ISO-5** Cross-contour reads are mediated only by GameSession summaries that respect the same isolation rules.

Violation of any isolation invariant is a critical architectural defect.

---

## 2. Double-Loop Learning & Feedback Routing

- Syntax / execution failures route **only** to the Coder (and SyntaxErrorMemory).
- Logical / semantic outcomes (FOLLOW / NULL / OMIT) route **only** to the Solver (and EpistemicMemory).
- Factual environment discoveries route **only** to the Explorer contour.
- Exhaustion of Coder or Solver retries forces a documented pure-symbolic / fixed-primitive fallback under GameSession control.

This Double-Loop design prevents the contamination failures observed when a single prompt loop mixed syntax repair with epistemic search.

---

## 3. Brusentsov Ternary Logic in Transition Judgment

### 3.1 Core mapping

| Outcome | Meaning |
|---|---|
| **FOLLOW** | Transition is relevant and consistent with the current branch hypothesis; continue. |
| **NULL** | Strict contradiction / physical or contractual impossibility; sever the branch. |
| **OMIT** | Legal but insignificant / passive / no useful semantic effect; do not sever, do not treat as success. |

`OMIT` is not false and is not failure. It is the architectural analogue of “irrelevant but legal” without collapsing into contradiction.

### 3.2 Necessary implication (architectural definition)

Brusentsov necessary implication is used to decide branch viability: a step supports continuation only when the observed transition *necessarily implies* the expected semantic claim under the current PlanningSet and environment contracts. Passive no-ops and unlinked noise map to OMIT; hard contract violations map to NULL.

### 3.3 Atomic proposition families (normative)

Verifier atomic propositions include (non-exhaustive):

- action accepted by environment gateway;
- PlanningSet id grounding succeeded;
- expected object/relation change observed;
- no unexpected contract violation;
- stabilization and replay consistency.

### 3.4 Branch lifetime

- FOLLOW keeps the branch alive.
- OMIT records an irrelevance/no-progress counterexample and typically suppresses exact equivalent retries without declaring impossibility.
- NULL severs the branch and records a hard negative.

---

## 4. PlanningSet Identity Contract (retained & strengthened)

For one snapshot cycle the PlanningSet is the sole canonical vocabulary of object, relation, and action-surface identifiers. Dual-view media (annotated frame + verifier packet) must share the same PlanningSet. Invented identifiers are rejected by VerificationBinder.

---

## 5. Lifecycle of the Tri-Agent Pipeline

```text
GameSession owns the loop:
  observe → dual-view + PlanningSet
  → Explorer (facts → EnvironmentSpecMemory)
  → Coder (DSL + manifest → SyntaxErrorMemory; publish only if sandbox/static OK)
  → Solver (trajectory packages → EpistemicMemory)
  → VerificationBinder + LayeredVerifier (FOLLOW / NULL / OMIT)
  → ActionBoundary emits only verifier-authorized environment actions
  → Double-Loop routing of failures
  → budgets / fallback symbolic path when retries exhausted
```

---

## 6. Budgets & Hard Limits (architectural)

LLM call counts are secondary to environment-action counts for RHAE scoring, yet wall-clock and Kaggle quota remain real constraints; therefore the architecture forbids unbounded retry loops. Hard ceilings on Explorer / Coder / Solver calls, trajectory package size, and sandbox runtime are normative and enforced by GameSession.

---

## 7. Sandbox & Deterministic Execution (architectural requirements)

Any Python generated by the Coder:

- must be executed only inside a restricted sandbox that exposes a minimal, pure API (PlanningSet queries, typed object/relation accessors, metric evaluators, and the ability to *declare* an intended environment action);
- may not perform I/O, network, arbitrary `exec`/`eval`, or import of unsafe modules;
- must be statically checked for the declared function manifest before any trajectory may reference it;
- must be deterministic given the same PlanningSet snapshot.

The sandbox is an architectural necessity, not an optional engineering detail. Failure to enforce it is a critical security and reproducibility defect.

---

## 8. Acceptance Criteria (Architecture)

1. The three agents (Explorer, Coder, Solver) are strictly separated by role and by memory contour; isolation invariants ISO-1 … ISO-5 hold.
2. Tracebacks and syntax diagnostics never appear in Solver prompts or EpistemicMemory.
3. Level goals and epistemic judgments never appear in Coder prompts or SyntaxErrorMemory.
4. Empiric evaluation uses Brusentsov ternary logic and correctly classifies passive / insignificant outcomes as OMIT while severing only true contradictions as NULL.
5. All DSL functions and trajectory steps are grounded on the current PlanningSet; no invented identifiers are accepted.
6. Dual-view media share one PlanningSet per snapshot cycle.
7. GameSession is the sole orchestrator of agent calls, memory mutations, budgets and fallbacks.
8. Dynamic Python is always sandboxed and validated before use.
9. Exhaustion of Coder or Solver retries forces a documented pure-symbolic / fixed-primitive fallback.
10. Every emitted environment action is auditable through the chain: PlanningSet → agent outputs → Binding → Verifier judgment → ActionBoundary.
11. The design remains offline-compatible with a fixed local Qwen / vLLM stack and competition gateway contracts.

---

## 9. Relation to Prior Versions

- **From V6**: high-assurance isolation, three-valued judgment, verifier as final authority, strict budgets, GameMemory across levels.
- **From V9**: PlanningSet identity, dual-view media, empiric post-step authority, repair-friendly treatment of incomplete knowledge (now expressed via OMIT).
- **New in V10**: explicit Tri-Agent hierarchy, Double-Loop routing, Brusentsov formalization of ternary logic, dynamic yet sandboxed DSL generation, and hard memory-contour isolation that prevents the contamination failures observed in intermediate versions.

Version 10.0 is therefore a synthesis that restores the safety posture of V6 while solving the “DSL for unknown environment” problem that originally forced the move toward V9-style trajectory proposal.
