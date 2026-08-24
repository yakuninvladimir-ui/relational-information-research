# ARC-AGI-3 LCLD Agent
# Engineering Specification — Version 10.0
# (Tri-Agent Hierarchy, Isolated Memory Contours & Brusentsov Ternary Logic)

## 0. Engineering Objective

Implement the V10.0 architecture so that the agent:

- uses three isolated LLM roles (Explorer, Coder, Solver) behind a single GameSession;
- maintains three strictly isolated memory contours;
- generates a level-specific Python DSL that is statically validated and executed only inside a restricted sandbox;
- routes syntax / execution failures exclusively to the Coder and logical / semantic outcomes exclusively to the Solver (Double-Loop);
- judges real transitions with Brusentsov ternary logic (FOLLOW / NULL / OMIT);
- falls back to a pure-symbolic / fixed-primitive path when Coder or Solver retries are exhausted;
- runs under Kaggle offline constraints with a fixed Qwen FP8 / vLLM stack;
- remains fully replayable and auditable.

### 0.1 Ownership

```text
GameSession              = sole orchestration + mutable state owner
ExplorerAgent            = Call-1 family, writes EnvironmentSpecMemory
DSLCoder                 = Call-2 family, writes SyntaxErrorMemory
SolverAgent              = Call-3 family, writes EpistemicMemory
PlanningSet              = canonical id vocabulary for one snapshot cycle
LayeredVerifier          = Brusentsov ternary authority
VerificationBinder       = grounds DSL calls against PlanningSet
ActionBoundary           = only component allowed to call the real environment
SandboxExecutor          = restricted interpreter for generated DSL
MemoryContours           = EnvironmentSpecMemory | SyntaxErrorMemory | EpistemicMemory
```

All other modules are pure or close-to-pure functions over explicit arguments.

---

## 1. Repository Layout

Active package: `v10_agent/`

```text
v10_agent/
  __init__.py
  config.py
  types.py
  observe.py
  game_adapter.py
  action_adapter.py
  arga_lite.py
  planning_set.py
  frame_media.py              # PNG + annotated_frame_png
  verifier_packet.py

  # Tri-Agent
  explorer_agent.py           # Call 1 – factual EnvironmentSpecification
  dsl_coder.py                # Call 2 – dynamic Python DSL + manifest
  solver_agent.py             # Call 3 – trajectory packages over manifest
  prompt_builders/
    explorer_prompt.py
    coder_prompt.py
    solver_prompt.py

  # Logic & Memory
  brusentsov_logic.py         # Ternary enum + implies_brusentsov
  memory_contours.py          # three isolated stores + GameMemory summary
  verification.py             # VerificationBinder
  judge.py                    # LayeredVerifier integrating Brusentsov
  sandbox.py                  # restricted executor + static checks

  # Core execution
  trajectory.py
  session.py                  # GameSession
  policy.py
  logging.py
  fallback_symbolic.py

  IDENTITY_CONTRACT.md
  tests/
    test_isolation*.py
    test_brusentsov*.py
    test_sandbox*.py
    test_lifecycle*.py
    test_v10_end_to_end.py
```

---

## 2. Configuration Contract

### 2.1 Required keys (V10Config)

```text
# LLM backend
llm_backend: qwen_vllm | qwen_fp8 | fake
model_path / endpoint settings for fixed competition stack

# Tri-agent budgets (normative ceilings)
max_explorer_calls_per_level: int
max_coder_calls_per_level: int
max_solver_calls_per_level: int
max_total_llm_calls_per_level: int

# Trajectory / package limits
max_trajectory_steps: int
max_package_functions: int

# Sandbox
sandbox_timeout_s: float
sandbox_allowed_modules: tuple[str, ...]

# Memory
contour_max_records: int
game_memory_enabled: bool

# Fallback
symbolic_fallback_enabled: bool
```

### 2.2 Competition defaults

Offline-only, fixed Qwen FP8 / vLLM stack, no external APIs, deterministic seeds where applicable, ActionBoundary as sole environment caller.

---

## 3. Core Data Types

### 3.1 Brusentsov Ternary (`brusentsov_logic.py`)

```python
class BrusentsovJudgment(str, Enum):
    FOLLOW = "FOLLOW"
    NULL = "NULL"
    OMIT = "OMIT"
```

`implies_brusentsov(antecedent, consequent, evidence) -> BrusentsovJudgment` implements necessary-implication classification used by LayeredVerifier.

### 3.2 EnvironmentSpecification (Explorer output)

Factual description grounded on PlanningSet ids: objects, relations, action-surface facts, affordance hypotheses (not final truth).

### 3.3 DSL Function Manifest (Coder output, visible to Solver)

Published only after static checks and sandbox publication rule. Lists function names, signatures, and PlanningSet-grounded preconditions.

### 3.4 Trajectory Package (Solver output)

Ordered steps referencing only published DSL functions and PlanningSet ids; expected semantic claims for verifier.

### 3.5 Memory Contours

```text
EnvironmentSpecMemory   # Explorer only
SyntaxErrorMemory       # Coder only
EpistemicMemory         # Solver only
GameMemory              # cross-level summary mediated by GameSession rules
```

---

## 4. Sandbox & Validation Pipeline (Coder output)

### 4.1 Static checks (must pass before manifest publication)

- no forbidden imports / I/O / network / `exec` / `eval`;
- declared functions match source;
- identifiers reference only PlanningSet vocabulary where required;
- deterministic API surface only.

### 4.2 Restricted executor

Minimal pure API: PlanningSet queries, typed accessors, metric evaluators, declare-intended-action. No real environment side effects inside sandbox.

### 4.3 Publication rule

Manifest and DSL become visible to Solver only after static + sandbox success. Failures write SyntaxErrorMemory and re-enter Coder under budget.

---

## 5. implies_brusentsov — Engineering Realisation

Map verifier atomic evidence to FOLLOW / NULL / OMIT:

- hard contract / physics contradiction → NULL;
- expected semantic change observed and consistent → FOLLOW;
- legal no-op / passive / unlinked noise → OMIT.

OMIT must not be stored as NULL. NULL must not be softened to OMIT.

---

## 6. GameSession Lifecycle (detailed)

```text
initialize session
while not terminated:
  dual_view, planning_set = observe_and_build()
  if need facts: Explorer → EnvironmentSpecMemory
  if need DSL: Coder → static/sandbox → SyntaxErrorMemory or publish manifest
  if need trajectories: Solver → EpistemicMemory packages
  for package in packages under budget:
    bind = VerificationBinder(package, planning_set)
    judgment = LayeredVerifier(bind, dual_view)  # FOLLOW/NULL/OMIT
    route Double-Loop feedback
    if FOLLOW and authorized: ActionBoundary.step(...)
  if retries exhausted: fallback_symbolic()
```

---

## 7. Isolation Enforcement & Tests

Mandatory tests:

- Explorer prompt never contains goals / Solver judgments / Coder tracebacks;
- Coder prompt never contains goals / Solver judgments;
- Solver prompt never contains syntax tracebacks;
- writes to wrong contour raise or are rejected;
- ISO-1…ISO-5 hold under adversarial prompt-injection fixtures.

---

## 8. Prompt Construction Rules

- Three separate prompt builders; no shared mutable template that mixes contours.
- Compact, schema-constrained JSON outputs only.
- No chain-of-thought requirement for competition path.
- PlanningSet ids are the only allowed identity vocabulary in agent outputs.

---

## 9. Fallback Path

When Coder or Solver budgets are exhausted, `fallback_symbolic.py` must provide a pure-symbolic / fixed-primitive path that still passes ActionBoundary and LayeredVerifier. Fallback is mandatory, documented, and logged.

---

## 10. Logging & Audit

Every environment action must be reconstructible from:

PlanningSet → agent outputs → Binding → Brusentsov judgment → ActionBoundary.

Replay must not re-query nondeterministic LLM calls; load recorded prompts/responses and contour writes.

---

## 11. Acceptance Criteria (Engineering)

1. Isolation invariants enforced by tests and runtime checks.
2. Brusentsov judgments correctly separate OMIT from NULL.
3. Sandbox blocks unsafe DSL and publishes only validated manifests.
4. Double-Loop routes syntax errors only to Coder and logical outcomes only to Solver.
5. GameSession is the only mutable-state owner and environment-action orchestrator.
6. Exhaustion triggers symbolic fallback.
7. Offline Qwen FP8 / vLLM competition path remains viable.
8. End-to-end test covers observe → tri-agent → verify → action → memory routing.
9. Structural Phase-A preflight can pass without starting vLLM where specified.
10. Zero accepted actions must not silently finalize an empty successful scorecard without explicit policy.
11. All emitted actions are auditable.
12. Package layout matches §1 and contains isolation, brusentsov, sandbox, and lifecycle tests.
13. Zero accepted actions refuse successful finalization of an empty scorecard.
14. Structural Phase-A preflight passes without starting vLLM.
15. The whole pipeline remains offline-compatible with the fixed Qwen FP8 / vLLM stack.

---

## 12. Validation Commands

```bash
python -m compileall -q v10_agent
python -m pytest -q v10_agent/tests/test_isolation*.py
python -m pytest -q v10_agent/tests/test_brusentsov*.py
python -m pytest -q v10_agent/tests/test_sandbox*.py
python -m pytest -q v10_agent/tests/test_lifecycle*.py
python -m pytest -q v10_agent/tests/test_v10_end_to_end.py
```

After packaging, assert that the notebook payload contains the three agent modules, sandbox, brusentsov_logic, memory_contours and that no competing hard-coded sampling limits remain in the child process.

---

## 13. Final Engineering Invariant

```text
Three agents, three memory contours, zero contamination.

Explorer writes facts.
Coder writes syntax.
Solver writes epistemic judgments.

Syntax failures travel only to the Coder.
Logical outcomes travel only to the Solver.

Dynamic Python exists only inside the sandbox.
All identifiers come from the PlanningSet.
Brusentsov decides FOLLOW / NULL / OMIT.

When retries are exhausted the symbolic fallback is mandatory.
GameSession is the only owner of mutable state and of the routing decisions.
```
