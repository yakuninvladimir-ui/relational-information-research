# ARC-AGI-3 LCLD Agent
# Architectural Specification
# Version 10.8

## 0. Purpose

This document defines Version 10.8 of the LCLD (Locally Constrained Learning and Discovery) architecture for an ARC-AGI-3 interactive reasoning agent. The agent operates under strict constraints to solve unseen interactive grid tasks via deterministic physical grounding and a neuro-symbolic tri-agent system.

Version 10.8 introduces the following architectural foundations:

- **Brusentsov Entailment Logic**: 4-valued epistemic engine distinguishing necessary incompatibility (`NULL`) from inessentiality (`OMIT`).
- **Transient Cells Engine**: Multi-frame micro-step animation analysis for ephemeral dynamics.
- **Triangulated Defeat Architecture**: Decoupling the fatal collision frame from the post-death level reset.
- **Tri-Agent Separation**: Segregation of cognition into Explorer (probing), Coder (DSL synthesis), and Solver (declarative planning).
- **Stratified Memory**: 5-block cross-level memory with a trace/quotient `TransitionTable` world model.
- **Dual-Space Perception**: 1px boundary crop handling with strict local-to-engine coordinate synchronization.
- **State-Aware TabuFallback**: Empirically grounded actor selection for fallback A* pathfinding.

### 0.1 What the Architecture Is NOT

The architecture is not:
- an LLM queried sequentially per-frame for action decisions;
- a system that executes arbitrary un-sandboxed code;
- a reinforcement learning policy requiring offline weight updates;
- a heuristic engine hardcoded to specific benchmark puzzles;
- a system that relies on `ACTION7` (Undo).

### 0.2 Architectural Constraints

The system is governed by the following structural invariants:
1. Benchmark puzzle IDs must not exist in any logic, prompt, or branch condition.
2. Grid dimensions and object boundaries must not be hardcoded (algorithms must be invariant from 2x2 to 64x64).
3. The standard 16-color palette (0..15) must not be destructively erased; it must be semantically mapped via `PaletteRoleMap`.
4. Regular expressions must not be used to parse spatial coordinates or action semantics.
5. The 8-tier verification cascade (`LayeredVerifier`) is strictly non-invertible and must not be bypassed.

### 0.3 Normative Authority Hierarchy

Operational authority resolves strictly in this order:
1. **Environment action boundary** (Step/Reset, GAME_OVER, action budget).
2. **LayeredVerifier & FrameDiff** (8-Tier Cascade, transient overrides).
3. **ActionGuards** (NoopRepeatGuard, DeathActionGuard, interior_grid_hash).
4. **GameSession Orchestrator** (State machine, Triangulated Defeat, DSL invalidation).
5. **SymbolicTrajectoryExecutor** (Pre-execution idle guard, early null severance).
6. **VirtualKinematicSandbox** (ObservedEdgeOverlay, trajectory repair).
7. **Solver Agent** (Declarative package planning, invariant distillation).
8. **Coder Agent** (Sandboxed DSL synthesis, auto-augmentation).
9. **Explorer Agent** (Two-tier empirical probing).
10. **Perception Engine** (ARGA-Lite, PersistentObjectTracker).
11. **External Memory Stores** (PaletteRoleMap, CoreInvariantRegistry).

---

## 1. Theoretical Foundation: Brusentsov's Logic of Entailment

To overcome the material implication paradoxes of classical Boolean logic (where a false premise erroneously validates an implication), the verifier is grounded in N.P. Brusentsov's 3-valued logic of entailment, extended to a 4-valued decision space for partial observability.

### 1.1 Decision Semantics

Transitions are evaluated into one of four states:

- **`FOLLOW (+1)` (Entailment Confirmed, $xy$)**: The action produced the explicit state change predicted by the grounded step's `EXPECT` proposition. The trajectory advances.
- **`OMIT (0)` (Inessentiality, $x'y$ or $x'y'$)**: The action produced no physical contradiction but did not fulfill a specific expected delta (e.g., a passive transition). The trajectory is **not severed**. Vacuous truth is prohibited: empty expectation sets evaluate strictly to `OMIT`.
- **`NULL (-1)` (Incompatibility / Falsification, $xy'_0$)**: The action contradicted an established physical invariant (e.g., expected motion but observed stagnation, or expected identity preservation but observed destruction). The candidate trajectory is **immediately severed**, and the state is reset.
- **`UNDECIDED` (Epistemic Ambivalence)**: Triggered by partial observability, low tracking confidence, or sub-pixel ambiguity. Pauses execution and schedules an evidence-seeking probe.

### 1.2 Carrollian Nullity Completeness

Incompatibility (`NULL`) is triggered by exhaustive physical invariants:
- **Object Identity**: Expected `preserved`, observed `destroyed/missing`.
- **Physical Stagnation**: Expected $\Delta \neq 0$, observed $\Delta = 0$.
- **Unintended Mutation**: Expected stationary, observed $\Delta \neq 0$.
- **Direction Inversion**: Expected vector and observed vector have opposite signs.

---

## 2. Tri-Agent Separation of Powers

### 2.1 Explorer Agent (Call Family 1)
- **Role**: Empirically probes actions (`ACTION1..6`) on the pristine initial frame ($S_0$).
- **Output**: Populates the `TransitionTable` with deterministic kinematics, transient animation facts, and affordances.
- **Constraints**: Strictly prohibited from formulating goals or multi-step plans.
- **Coordinate Probing**: Uses `_select_on_mask_pixel` to target physical pixels rather than hollow bounding-box centroids.

### 2.2 Coder Agent (Call Family 2)
- **Role**: Translates verified `EnvironmentSpecMemory` facts into a Python Domain-Specific Language (DSL).
- **Environment**: Code is AST-validated and runs in a strictly constrained `SandboxExecutor`.
- **Reactive Invalidation**: If new kinematics are discovered during execution that are missing from the current DSL, the module is invalidated, triggering a Coder replan and auto-augmentation of the DSL manifest.

### 2.3 Solver Agent (Call Family 3)
- **Role**: Proposes packages of up to 4 multi-step candidate trajectories expressed via the DSL manifest.
- **Constraints**: Plans declaratively. Has no access to execution environments or raw Python execution traces.
- **DualView Grounding**: Receives synchronized raw pixel frames and annotated frames (with bounding boxes) to overcome parser over-segmentation of multi-color objects.

---

## 3. Stratified Memory Architecture

Cross-level memory is divided into five strictly partitioned stores:

1. **`PaletteRoleMap`**: Maps colors (0..15) to semantic roles (e.g., `ACTOR`, `HAZARD`, `TARGET`) rather than destructively erasing color indices.
2. **`CoreInvariantRegistry`**: Stores `NEGATIVE_BARRIER` and `POSITIVE_CANON` invariants. A single empirical contradiction on $S_0$ falsifies and retires an invariant.
3. **`EpisodicExemplarBuffer`**:
   - `DefeatExemplar`: Grounded from `GAME_OVER`. Contains `fatal_step_diff` (isolating the lethal action) and `valid_prefix_actions`.
   - `VictoryExemplar`: Grounded from level completion.
4. **`CurriculumProgressionBuffer`**: Cross-level pattern tracking.
5. **`WorkingRolloutMemory`**: Active step propositions and state diffs.

### 3.1 TransitionTable WorldModel
An empirical environment graph maintained per-level:
- **Trace**: Append-only log of `TransitionRecord` structs.
- **Quotient (ObservedEdgeOverlay)**: State-action edge index `(grid_hash, action_key) -> TransitionRecord`. Distinguishes `IDLE_SELF_LOOP` (verified zero-delta edge) from `IDLE_UNLINKED` (untried edge).

---

## 4. Execution Engine and Dynamics

### 4.1 Triangulated Defeat Architecture
Directly comparing a pre-death frame to a post-death reset frame corrupts state diffs. On `GAME_OVER`:
1. **$F_{alive}$**: The state immediately before the fatal action.
2. **$F_{fatal}$**: The intermediate collision/death frame.
3. **$F_{reset}$**: The pristine level reset.
The system calculates the isolated `fatal_step_diff` between $F_{alive}$ and $F_{fatal}$ and captures this in a `DefeatExemplar`.

### 4.2 Multi-Frame Transient Cells Engine
Action effects (e.g., lasers, projectiles) are evaluated across intermediate micro-frames:
- Cells that mutate $\ge 2$ times across a single transition are marked as `transient_cells`.
- Transient geometry is classified (`beam`, `sweep`, `pulse`).
- The presence of transient cells overrides a static `zero_delta` evaluation, properly classifying the action as effective rather than an `IDLE_SELF_LOOP`.

### 4.3 1px Boundary Crop and Dual-Space Coordinates
- Perception is cropped by 1 pixel on all boundaries (`crop_offset = 1`).
- All spatial reasoning, ARGA-Lite object extraction, and deduplication operate in local coordinates.
- Actions dispatched to the engine are strictly mapped: `engine_x = local_x + crop_offset`.

### 4.4 Hungarian Jonker-Volgenant FrameDifferencing
Entity tracking between frames $S_t$ and $S_{t+1}$ is resolved via bipartite matching.
- **Cost Function**: Normalized sum of spatial distance, area similarity, and color congruence.
- **Outputs**: Strict semantic deltas (`moved`, `rotated`, `resized`, `color_changed`, `appeared`, `disappeared`).

---

## 5. Execution Orchestration and Safety Guards

### 5.1 SymbolicTrajectoryExecutor
Executes Solver-proposed packages step-by-step:
- **Pre-Execution Idle Guard**: Before emitting a step, it queries `TransitionTable`. If the action is a known `IDLE_SELF_LOOP` in the current `grid_hash`, the step is blocked and the candidate is severed.
- **Macro-Step Unrolling**: Multi-step functions (`count=N`) are decomposed. Invariants are evaluated at every sub-step.
- **Early Severance**: Any `NULL` verdict immediately halts the candidate and forces an environmental `RESET` to $S_0$.

### 5.2 Action Guards and Perimeter Isolation
- **NoopRepeatGuard**: Blocks consecutive identical actions if the first yielded zero delta.
- **DeathActionGuard**: Caches and blocks known `GAME_OVER` edges.
- **Peripheral HUD Isolation**: Identifies peripheral timers/progress bars based on border thickness and bounding boxes. Computes `interior_grid_hash` to ensure state signatures remain stable despite peripheral HUD ticks.

### 5.3 Fallback Execution Contract
The lifecycle is strictly bounded:
1. Max 5 Solver attempts per level.
2. Exactly 1 continuous `SymbolicFallbackEngine` run using state-aware Tabu A* search.
3. In fallback mode, `RESET` is strictly prohibited. If a cycle or `GAME_OVER` occurs during fallback, the level is cleanly abandoned.