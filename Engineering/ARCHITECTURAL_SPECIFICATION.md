# ARC-AGI-3 LCLD Agent
# Architectural Specification — Version 10.8
# (Neuro-Symbolic Tri-Agent Architecture, Brusentsov Entailment Logic, WorldModel TransitionTable [Trace + Quotient], Hungarian Jonker-Volgenant FrameDiff, Multi-Frame Animation & Transient Cells Engine, Triangulated Defeat Architecture, Peripheral HUD Filtering, ActionGuards, PriorityScheduler, ObservedEdgeOverlay, Null Severance & Epistemic Recovery, Two-Tier Action Lifecycle, Reactive DSL Invalidation, Universal Multimodal Dual-View, 5-Block Stratified Memory, State-Aware TabuFallback & Resilient Remote TPU/vLLM HTTP/2 Serving)

---

## 0. Purpose and Architectural Vision

This document defines the authoritative architecture of the **ARC-AGI-3 LCLD (Locally Constrained Learning and Discovery) Agent (Version 10.8)**. The agent is engineered to autonomously solve diverse, completely unseen ARC-AGI-3 interactive grid tasks under official Kaggle competition runtime constraints:

1. **Unknown Mechanics & Hidden Rules**: No pre-programmed rules, object identities, goal definitions, or physics models are provided. Every environment must be empirically identified, modeled, and solved entirely online.
2. **Standard 16-Color Palette ($0..15$) & Semantic Role Mapping**: ARC-AGI-3 operates over a 16-color palette (integers $0..15$). The agent maintains a persistent `PaletteRoleMap` tracking functional roles (`EntityRole`) for each color index, completely replacing destructive `[COLOR]` erasure with role-aware semantic labeling (`Color N (ROLE)`).
3. **Partitioned Action Space & Hardware Constraints**: Environments feature discrete directional/toggle actions (`ACTION1..5`) and spatial coordinate clicks (`ACTION6(x, y)`). Step-reversal (`ACTION7` / `Undo`) is **hardware-blocked** by architectural contract. Epistemic consistency is maintained strictly through forward deterministic planning and clean state resets ($S_0$).
4. **Dual-Space Coordinate Synchronization & 1px Boundary Crop**: Raw environment frames are cropped by 1 border pixel on all 4 sides ($[1:-1, 1:-1]$), yielding a local perception grid $(H-2) \times (W-2)$. Coordinates are strictly maintained in a dual-space representation (local ARGA-Lite coordinates vs. engine coordinates via `crop_offset = 1`), guaranteeing boundary precision and tested-coordinate deduplication.
5. **Brusentsov 4-Valued Logic of Entailment & Carrollian Nullity Completeness**: Foundational epistemic engine based on N.P. Brusentsov’s non-paradoxical logic of entailment ($xy \lor xy'_0 \lor x'y'$), distinguishing necessary incompatibility (Carroll's nullity $xy'_0 \to \text{NULL}$) from benign inessentiality (omission/silence $\to \text{OMIT}$), with strict elimination of material implication paradoxes ($len(expected)=0 \to \text{IRRELEVANT}$, vacuous `FOLLOW` prevention). Incompatibility ($xy'_0$) covers physical stagnation (expected motion, observed stationary), unintended mutation (expected invariant, observed motion), direction inversion (opposite kinematic signs), and object identity violation (expected preserved, observed destroyed/missing).
6. **Multi-Frame Animation & Transient Cells Engine (`animation_analysis.py`)**: ARC-AGI-3 environments often feature ephemeral projectile, laser beam, scanner sweep, or interaction flash mechanics animated across a sequence of intermediate micro-frames ($f_0 \dots f_k$) returned by `env.step`. Cells that mutate two or more times across the transition chain ($\Delta(r, c) \ge 2$) revert before or at the final static frame. The engine extracts these micro-frames, computes the collapsed animation chain, isolates transient cells, classifies trajectory geometry (`horizontal_beam`, `vertical_beam`, `vertical_sweep`, `horizontal_sweep`, `localized_pulse`, `spatial_sweep`), and renders a `transient_composite` grid in active non-reverted colors. In `LayeredVerifier`, transient cell detection overrides zero-delta judgments, ensuring ephemeral mechanics are recognized as effective actions rather than passive self-loops.
7. **Triangulated Defeat Architecture ($F_{\text{alive}} \to F_{\text{fatal}} \to F_{\text{reset}}$)**: When `GAME_OVER` occurs, the environment emits a fatal collision/death frame before resetting to the level initial state. Comparing $F_{\text{alive}}$ directly to $F_{\text{reset}}$ causes catastrophic misattribution of the entire board reset (teleporting, door closing) to the fatal action. The agent explicitly decouples $F_{\text{alive}}$ (state before fatal action), $F_{\text{fatal}}$ (death collision frame), and $F_{\text{reset}}$ (restarted level frame). `DefeatExemplar` captures an isolated `fatal_step_diff`, `fatal_transient_trajectory`, and the sequence of verified safe prefix actions (`valid_prefix_actions`). The Solver prompt instructs the LLM to retain the verified safe prefix and branch only at the fatal step.
8. **Peripheral HUD & Dynamic Margin Filtering**: Peripheral progress bars, level timers, and border counters mutate cyclically without altering the interior gameplay state. The agent employs dynamic border thickness filtering (up to 2-3px) via `is_peripheral_hud_strip` and `is_only_peripheral_hud_delta` in `arga_lite.py` and `session.py`, preventing peripheral timer ticks from masquerading as effective actions or corrupting interior state hashes.
9. **Deterministic Empirical WorldModel (`TransitionTable`: Trace + Quotient)**: `EnvironmentSpecMemory` maintains a dual-representation `TransitionTable` combining an append-only monotone time Trace (`transitions`) with a Quotient state-action edge overlay (`edges`: `(before_grid_hash, action_key) -> TransitionRecord`). It distinguishes verified self-loops (`IDLE_SELF_LOOP`) from unlinked zero-delta steps (`IDLE_UNLINKED`), tracks non-determinism (`hidden_state_suspected`), and provides pre-execution guards against known no-op and fatal (`GAME_OVER`) edges across `SymbolicTrajectoryExecutor`, `VirtualKinematicSandbox`, and `SymbolicFallbackEngine`.
10. **5 Stratified Memory Blocks**: Cross-level game memory is partitioned into five specialized, non-interfering stores: `PaletteRoleMap`, `CoreInvariantRegistry` (`GroundedInvariant` & `InvariantHypothesis`), `EpisodicExemplarBuffer` (`DefeatExemplar` & `VictoryExemplar`), `CurriculumProgressionBuffer` (`curriculum_history`), and `WorkingRolloutMemory`.
11. **Empirically Grounded Exemplars**:
    - `DefeatExemplar`: Generated upon `GAME_OVER` / lethal failure; grounds negative barrier invariants ($xy'_0 \to \text{NULL}$) to prevent recurring mistakes, enriched with isolated fatal diffs and safe prefix retention.
    - `VictoryExemplar`: Generated upon level victory; grounds positive canonical exemplars ($xy \to \text{FOLLOW}$) for cross-level transfer.
12. **Symbolic Trajectory Execution with Pre-Execution Idle Guard, Early Null Severance & Epistemic Recovery**: Before emitting step 0, `SymbolicTrajectoryExecutor` consults `TransitionTable` to circuit-break trajectories whose leading action is an empirically confirmed `IDLE_SELF_LOOP` on the current `grid_hash`. Macro-step commands (`count=N`) are unrolled into $N$ atomic steps by `_decompose_expected_propositions_for_substep`. State invariants (`unchanged`, `preserved`) are distributed across all intermediate steps, single-step motion signs (`step_moved`) are verified at each transition, and cumulative vectors are checked on the terminal step. Any physical contradiction ($xy'_0 \to \text{NULL}$) causes immediate candidate branch severance (`sever()`), early execution termination, structured diagnostic synthesis (`[FAILED ATTEMPT N DIAGNOSTIC]`), and a clean environmental reset ($S_0$) without dirty-state cascading.
13. **Two-Tier Action Lifecycle, On-Mask Coordinate Probing & Action Affordance Completeness**: Primitive probe management distinguishes immediately effective actions from conditional trigger actions. Actions yielding $\Delta = 0$ on the pristine initial frame $S_0$ are strictly preserved in `available_actions` and typed as `CONDITIONAL_TRIGGER` affordances (`status: unconfirmed_on_s0`) rather than being discarded. Spatial `ACTION6` probes strictly select actual on-mask pixels (`obj.pixels`) closest to object centroids rather than raw bounding-box centers, avoiding background cavities on non-convex (`L`/`U`/`O`/ring) shapes.
14. **Reactive DSL Invalidation & Auto-Augmentation**: When any newly confirmed action (not in the active manifest) is observed during execution, `GameSession` reactively invalidates `active_module` and `active_manifest`, unblocks Coder retry ceilings, and requests a clean replan. The Coder auto-augments output with canonical sandboxed wrappers for any omitted confirmed actions.
15. **Universal Multimodal Dual-View & Coordinate Disambiguation**: Perception provides synchronized DualView imagery (raw pixel frame + annotated frame with object bounding boxes and aliases) across all three agents, mitigating parser over-segmentation of multi-color composite structures. Grid coordinates follow strict Cartesian $(Row, Col) \leftrightarrow (Y, X)$ disambiguation.
16. **Tri-Agent Authority Segregation**: Cognition is strictly divided among three distinct agent roles (**Explorer**, **Coder**, and **Solver**) operating through dedicated, non-overlapping memory contours guarded by ISO-1 through ISO-18 invariants.
17. **Multi-Candidate Package Synthesis, ObservedEdgeOverlay & Coordinate Invariant Synthesis**: The Solver plans complete multi-step trajectory packages (up to 4 candidate paths per package) upfront, under a hard ceiling of 5 chain attempts per level. `VirtualKinematicSandbox` validates and repairs candidates using `TransitionTable` (`ObservedEdgeOverlay`) to strip leading `IDLE_SELF_LOOP` steps and reject known `GAME_OVER` edges, and synthesizes fallback invariant trajectories for both directional (`ACTION1..4`) and pure coordinate (`ACTION6`) games.
18. **State-Aware `TabuFallback` Engine with Empirical Actor Grounding**: When symbolic fallback is engaged, `SymbolicFallbackEngine` synchronizes with `TransitionTable` to maintain state-action tabu counters (`tabu_counts`), dead-end edge sets (`dead_end_edges` for `IDLE_SELF_LOOP` and `GAME_OVER`), and state-visitation penalties (`visited_state_counts`). Actor selection for 2D BFS pathfinding is grounded in empirical displacements (`TransitionTable.transitions`), `GameMemory.confirmed_actors` (`persistent_id`), and `PaletteRoleMap` (`EntityRole.ACTOR`).
19. **Clean Physics Simulator & Topological Invariants**: Aspect ratio heuristics ($\ge 3.0$) replace puzzle-specific constants. Domain-general topological invariants (`ConnectedComponentConservation`, `GravitySettling`, `ContactTrigger`, `AreaConservation`) model world physics without geometric hardcoding.
20. **Persistent Multi-Frame Object Tracking**: Object permanence across frames is maintained by `PersistentObjectTracker` via 4-part bipartite matching (color, centroid distance, shape Jaccard, relative area), velocity EMA, and confidence tracking.
21. **Safe Evidence-Seeking Loop (E-FSM)**: Epistemic uncertainty (`Verdict.UNDECIDED`) schedules targeted empirical probes without premature candidate branch severing.
22. **Coordinate-Aware `VisibleCycle` Loop Recovery**: Orbit detection for periods 1..8 detects repeating state-action cycles (incorporating `(x, y)` coordinates for `ACTION6` so distinct coordinate clicks are not conflated) before burning the level action budget, severs the loop, and triggers clean replanning.
23. **Production Remote TPU v5e-8 & vLLM Serving Architecture**: Resilient remote inference powered by Qwen3.8-27B running on Google Cloud TPU v5e-8 with Cloudflare HTTP/2 tunneling (`--protocol http2`), overcoming Kaggle UDP drops, real-time tunnel logging, and a 60-second auto-reconnection watchdog daemon. Absolute deadline tracking with 15-second reserves prevents timeouts.
24. **Jonker-Volgenant Optimal Bipartite Hungarian Matching & Entity Frame Differencing (`frame_diff.py`)**: Inter-frame displacement tracking classifies connected components using the Jonker-Volgenant linear sum assignment algorithm. Emits semantic deltas: Translation (`moved`, `step_moved`), Rotation (`rotated`), Scaling (`resized`), Color Change (`color_changed`), Spawning/Destruction (`appeared`, `disappeared`). Isolates peripheral HUD progress bars and timers by bounding box and border analysis, shielding gameplay deltas from spurious ticks.
25. **Action Guards & Resilient Interior Grid Hashing (`action_guards.py`)**: `NoopRepeatGuard` monitors consecutive actions and blocks repetitions that yield zero gameplay delta. `DeathActionGuard` records fatal state-action transitions `(interior_hash, action_sig)`. Invariant interior grid hashing strips outer margins to ensure state signatures remain stable despite peripheral HUD variations.
26. **Dynamic Priority Compute Allocation (`priority_scheduler.py`)**: Dynamic scheduling formula $P = (A + B) \cdot C$, where $A$ is level completion ratio, $B$ is attempt progress bonus, and $C$ is stall decay factor. Dynamically reallocates concurrency and execution priority to tasks showing measurable progress, throttling dead-end levels.
27. **Strict Single-Run Fallback Execution Contract Without Reset**: The agent is bounded by a strict structural lifecycle: up to 5 attempts with LLM solver $\to$ exactly ONE continuous symbolic fallback run $\to$ clean abandonment without reset on `GAME_OVER`, cycle, or action budget exhaustion. In fallback mode, `RESET` is strictly prohibited under all circumstances.
28. **Per-Level Action Budget Hard Ceiling (`max_actions_per_level = 80`)**: Protects the 9-hour competition window by enforcing an 80-action ceiling per level in `lcld_competition_child.py`, preventing runaway loops from monopolizing resources.

---

### 0.1 What the Architecture Is NOT

- **NOT a monolithic LLM game player**: The LLM is never prompted with "What action do you want to take next?" on every frame. Such approaches suffer catastrophic hallucination, high latency, context explosion, and rapid budget depletion.
- **NOT a step-by-step solver**: The Solver plans complete multi-step trajectories upfront. The deterministic symbolic executor carries out execution step-by-step, verifying world laws at every transition.
- **NOT an unconstrained code executor**: The Coder synthesizes Python DSL implementations that are verified by an AST whitelist parser and executed inside a restricted memory/CPU sandbox. Arbitrary Python execution is blocked.
- **NOT a reinforcement learning policy**: The agent requires zero training frames, weight updates, or offline learning loops.
- **NOT hardcoded for specific games**: No heuristics tailored to specific benchmark puzzles exist. All invariant rules are deduced online from empirical observations.
- **NOT dependent on `ACTION7`**: By competition rules, `ACTION7` is a step-reversal (`Undo`). The agent hardware-blocks `ACTION7`, maintaining epistemic consistency strictly through forward deterministic planning and clean state resets ($S_0$).

---

### 0.2 Anti-Specification Gaming Contract

The codebase is governed by a non-negotiable contract of abstract purity enforced by continuous AST validation:

1. **Categorically Forbidden**:
   - Creating conditions, variables, comments, or branches containing benchmark puzzle IDs (`ar25`, `ft09`, `ls20`, `re86`, `rs01`, etc.).
   - Hardcoding grid dimensions or object dimensions (e.g. `width <= 4`, `height >= 10`, `grid_size == 62`, `10x4`), except for reading dynamic parameters from the perception grid or `PlanningSet`.
   - Using regular expressions (`re`, `regex`) to parse coordinate trajectories or action semantics (`axis_steps`, `piece_steps`, `internal dots`).
   - Bypassing, reordering, or truncating the 8-tier verification cascade of `LayeredVerifier`.
   - Replacing color indices with destructive `[COLOR]` tokens that erase semantic roles.
2. **Invariance Principles**:
   - All algorithms must operate invariantly across grid dimensions ($2 \times 2$ up to $64 \times 64$) and the full 16-color palette ($0..15$).
   - Color role classification (`EntityRole`) must be empirically grounded in victory exemplars (`VictoryExemplar`) and defeat exemplars (`DefeatExemplar`).

---

### 0.3 Normative Authority Hierarchy

Operational authority in the agent is strictly ordered from highest to lowest:

```
1. Gateway & Competition Contracts (Arcade step/reset interface, GAME_OVER protocol, max_actions_per_level=80, PriorityScheduler)
                                 │
2. Brusentsov LayeredVerifier & Hungarian FrameDiff (Strict 8-Tier Decision Cascade: FOLLOW / NULL / OMIT / UNDECIDED, Animation/Transient override)
                                 │
3. ActionGuards & Invariant Hash (NoopRepeatGuard, DeathActionGuard, compute_interior_grid_hash)
                                 │
4. GameSession Orchestrator (State machine, 5-LLM + 1-Fallback lifecycle, Triangulated Defeat, no-reset fallback, reactive DSL invalidation)
                                 │
5. SymbolicTrajectoryExecutor & TransitionTable WorldModel (Pre-execution idle guard, early null severance, atomic substep unrolling)
                                 │
6. VerificationBinder Contracts & VirtualKinematicSandbox (Grounds declarative steps & repairs against ObservedEdgeOverlay)
                                 │
7. Solver Agent (Declarative planning: packages multi-step trajectories, retains safe prefixes, and distills invariants)
                                 │
8. Coder Agent (Synthesizes sandboxed Python DSL implementations with auto-augmentation from factual specs)
                                 │
9. Explorer Agent (Two-tier discrete & on-mask coordinate probing; populates TransitionTable & transient animation facts)
                                 │
10. ARGA-Lite, PersistentObjectTracker & PlanningSet (Deterministic perception, grid_hash, tracking, HUD isolation & DualView)
                                 │
11. Isolated Memory Stores & State-Aware TabuFallback (PaletteRoleMap, CoreInvariantRegistry, TransitionTable, TabuFallback)
```

No raw text or candidate action generated by an LLM is ever sent directly to the environment. Every action must be verified against world laws, bound through formal contracts, and emitted one transition at a time.

---

## 1. Theoretical Foundation: Brusentsov's Logic of Entailment

### 1.1 Historical Context & Epistemic Flaw of Classical Material Implication

Standard two-valued mathematical logic, founded on Boolean algebra and the truth-functional definition of material implication:
$$(x \to y) \equiv \neg x \lor y \equiv x' \lor y$$
introduces fatal paradoxes when applied to autonomous empirical reasoning and invariant deduction:

1. **Ex Falso Quodlibet (Truth from Falsehood)**: Under material implication, if premise $x$ is false ($x = 0$), the formula $(x \to y)$ evaluates to `TRUE` regardless of whether conclusion $y$ is true, false, or physically impossible.
2. **Vacuous Truth in Verification**: If an agent formulates an invariant rule "If object $A$ moves right, its color changes to red", and the agent performs an action where object $A$ does not move, classical logic treats the rule as completely verified and confirmed ($1$). In reality, the observation provided **zero evidence** regarding the validity of the rule.
3. **Loss of Necessary Consequence**: Material implication denotes mere non-exclusion (possibility) rather than necessary consequence.

In his seminal paper *"Усовершенствование логики умозаключений"* (2012, МГУ им. М.В. Ломоносова), **Nikolay Petrovich Brusentsov** demonstrated that Aristotle's original syllogistic entailment $Axy$ ("All $x$ are $y$", "y belongs to every x", $x = xy$ — *из $x$ необходимо следует $y$*) was distorted by modern logicians who forced a two-valued reduction upon an inherently three-valued relation.

---

### 1.2 Aristotle's Syllogistic Entailment ($Axy$)

Aristotle established that entailment is the containment of essences: to state that $y$ follows from $x$ means that the characteristic $y$ is necessarily inherent in every instance of $x$:
$$x = xy$$
Taking the contrapositive:
$$y' = x'y'$$
which expresses that if characteristic $y$ is absent ($y'$), characteristic $x$ must also be absent ($x'$), i.e. $A(y', x')$.

Aristotle's universe of discourse ($\text{УА}$) is populated by non-empty terms:
$$x \neq 0, \quad x' \neq 0, \quad y \neq 0, \quad y' \neq 0$$
Neither a characteristic nor its opposite is universally empty or universally exhaustive.

---

### 1.3 Lewis Carroll's Biliteral Diagrams & The Nullity Index ($xy'_0$)

Brusentsov recovered the genuine relation of entailment using the biliteral and indexical methods of Lewis Carroll (Charles Lutwidge Dodgson):

1. **Elementary Characteristics and Coexistence of Opposites**:
   Every primary characteristic $x$ necessarily coexists with its opposite $x'$. Their coexistence is subject to mutual incompatibility:
   $$xx'_0, \quad yy'_0, \quad zz'_0$$
   where the prime symbol ($'$) denotes opposition (negation), and the subscript index **«0»** denotes the **nullity (incompatibility / non-existence)** of the conjunction.

2. **The Entailment Relation as Incompatibility**:
   To state that $y$ necessarily follows from $x$ ($x \Rightarrow y$) means that it is physically and logically impossible for $x$ to exist without $y$ (i.e. for $x$ to coexist with $y'$):
   $$(x \Rightarrow y) \equiv xy'_0$$
   Taking into account contraposition ($(x \Rightarrow y) \equiv (y' \Rightarrow x')$), Carroll's complete formula for entailment is:
   $$(x \Rightarrow y)(y' \Rightarrow x') \equiv x_1 y'_0 \land y'_1 x_0 \equiv xy'_0$$
   In Aristotelian discourse, affirming entailment is mathematically identical to asserting the nullity of $xy'$.

3. **Material Implication vs. Entailment**:
   Material implication $(x \to y)$ can be expanded algebraically:
   $$(x \to y) \equiv (x \Rightarrow y) \lor x'y \equiv xy \lor xy'_0 \lor x'y \lor x'y'$$
   Material implication erroneously includes the term $x'y$ (where $x$ is absent and $y$ is present) as an explicitly affirmed truth condition. In necessary entailment, $x'y$ does not constitute part of the entailment relationship.

---

### 1.4 Overcoming DNF Incompleteness: Inessentiality (Omission) vs Exclusion

A central insight of Brusentsov’s theory is the **fundamental distinction between inessentiality (omission) and exclusion (incompatibility)**:

* **In Classical Boolean Algebra**: Omission of a conjunction term from a DNF formula implicitly signifies its **exclusion (falsity / non-existence)**:
  $$\text{omitted} \implies 0 \ (\text{false})$$
* **In Brusentsov’s Three-Valued Algebra**:
  * **Exclusion (Incompatibility)** must be explicitly designated by Carroll's nullity index **«0»** ($xy'_0$).
  * **Affirmation (Coexistence)** is designated by unindexed terms ($xy$).
  * **Omission (Silence / Умалчивание)** signifies **inessentiality (несущественность / irrelevance)**: the relationship holds regardless of whether the omitted term occurs or does not occur.

---

### 1.5 The 3-Valued DNF of Necessary Entailment

Thus, the relation of necessary entailment ($x \Rightarrow y$) is represented by the **three-valued DNF**:
$$x \Rightarrow y \equiv xy \lor xy'_0 \lor x'y'$$
where the term $x'y$ is **omitted as inessential**.

| Term | Algebraic Status | Semantics in Logic of Entailment | Semantics in LCLD Agent Verifier |
| :--- | :--- | :--- | :--- |
| **$xy$** | Unindexed | Necessary coexistence: premise and conclusion both occur. | **`FOLLOW (+1)`**: Positive confirmation of physical expectation. |
| **$xy'_0$** | Indexed with «0» | Strict incompatibility: premise occurs, conclusion fails. | **`NULL (-1)`**: Invariant contradiction. Candidate branch severed. |
| **$x'y$** | Omitted | Inessential: premise does not occur; conclusion occurs. | **`OMIT (0)`**: Neutral transition. Candidate branch preserved. |
| **$x'y'$** | Unindexed | Coexistence of opposites: neither premise nor conclusion occurs. | **`OMIT (0)`**: Neutral transition. World state unaffected. |

---

### 1.6 The 4-Valued Decision Semantics of `LayeredVerifier`

In real ARC-AGI-3 environments, observations are subject to **partial observability** (hidden layers, occluded entities, ambiguous affordances). To handle partial observability without violating Brusentsov’s axioms, the agent extends ternary logic into a **4-valued epistemic decision system**:

```
                                  Transition Result Evaluated
                                               │
                     ┌─────────────────────────┴─────────────────────────┐
                     │                                                   │
              Contradiction                                        No Contradiction
                     │                                                   │
              ┌──────┴──────┐                                     ┌──────┴──────┐
              │  VERDICT:   │                                     │             │
              │    NULL     │                           Expectation Met?        Ambiguity
              │    (-1)     │                                     │             Detected?
              └─────────────┘                        ┌────────────┴───────────┐         │
                Incompatibility                      │                        │         │
                  $xy'_0$                           YES                       NO        ▼
                                                     │                        │   ┌───────────┐
                                               ┌─────┴─────┐            ┌─────┴───┤ VERDICT:  │
                                               │ VERDICT:  │            │VERDICT: │ UNDECIDED │
                                               │  FOLLOW   │            │  OMIT   │   (SEEK)  │
                                               │   (+1)    │            │  (0)    └───────────┘
                                               └───────────┘            └─────────┘ Epistemic
                                                Entailment              Omission    Ambivalence
                                                    $xy$                   $x'y$
```

1. **`Verdict.FOLLOW (+1)` (Entailment Confirmed, $xy$)**:
   - The executed action caused the explicit state change predicted by the grounded step's `EXPECT:` proposition (all expected propositions necessarily contained in observed transitions).
   - Physical progression is affirmed. The candidate trajectory advances its execution cursor (`cursor += 1`).

2. **`Verdict.OMIT (0)` (Inessentiality / Neutral Omission, $x'y$)**:
   - The action produced no contradiction with known physical world laws, but did not trigger the specific expected delta (e.g. passive interaction, non-essential background shift, or empty expectation set).
   - **Crucial Invariant (ISO-10)**: In accordance with Brusentsov's principle, inessentiality does **not** signify falsehood. The active candidate trajectory is **NEVER severed** on an `OMIT` verdict, and execution advances safely.
   - **Elimination of Vacuous Truth**: If a step declares zero expected propositions (`len(expected) == 0`), Brusentsov evaluation strictly returns `Ternary.IRRELEVANT` (neutral $x'y'$), mapping to `Verdict.OMIT`. It is fundamentally forbidden to treat absence of expectation as logical confirmation (`TRUE`).

3. **`Verdict.NULL (-1)` (Incompatibility / Falsification, $xy'_0$)**:
   - The action directly contradicted an established physical invariant or expected proposition.
   - Forms of contradiction detected by `contradicts()` include:
     - **Object identity destruction**: Expected `preserved`, observed `destroyed`, `vanished`, or `missing`.
     - **Physical stagnation**: Expected motion along an axis ($\text{exp} \neq 0$), but observed stationary ($\text{obs} == 0$).
     - **Unintended mutation**: Expected stationary/invariant state ($\text{exp} == 0$ or `unchanged`), but observed movement ($\text{obs} \neq 0$).
     - **Direction inversion**: Expected motion vector opposite to observed motion vector ($\text{exp} \times \text{obs} < 0$).
     - **Attribute/Area mismatch**: Value differences in color, bounding box, or pixel count.
   - The active candidate trajectory is **immediately severed (`sever()`)**. Execution of the current candidate terminates cleanly without executing trailing steps. The orchestrator schedules an environmental reset (`RESET` $\to S_0$) to restore a clean state before executing the next candidate or replanning.

4. **`Verdict.UNDECIDED` (Epistemic Ambivalence / Partial Observability)**:
   - Emitted when empirical evidence is insufficient to distinguish between entailment and contradiction:
     a) Bipartite track matching cost difference between best and second-best candidate is $< \text{matching\_ambiguity\_threshold}$ (0.15).
     b) Any participating `TrackedObject` exhibits confidence $< \text{track\_confidence\_threshold}$ (0.60).
     c) Zero grid delta observed on an unconfirmed action carrying a non-empty `EXPECT` set away from boundaries.
     d) Detected change metrics have magnitudes $< \text{min\_reliable\_delta}$ (0.8 px) with non-empty `EXPECT` and without terminal completion.
     e) Upstream `GroundedStep` or binder sets `confidence == "low"` or `matching_status == "ambiguous"`.
   - **Ablation Invariant**: When `enable_undecided_verdict = False`, all conditions above map conservatively to `Verdict.OMIT`, maintaining classic 3-valued operation.

---

### 1.7 Elimination of Material Implication Paradox in Verification

In earlier neuro-symbolic systems, when an action produced a non-zero grid delta and matched a confirmed action effect from memory, the verifier would grant a positive confirmation (`FOLLOW`) even if the step's expected proposition set was empty or unverified.

This was a direct manifestation of the **material implication paradox** ($x'y \to \text{FOLLOW}$). Under Brusentsov's logic:
- If expected propositions are empty (`len(expected) == 0`), the premise $x$ was not asserted. Any observed change $y$ is an unasserted side effect ($x'y$).
- The transition must evaluate to **`Verdict.OMIT`**, never `FOLLOW`.
- `Verdict.FOLLOW` is granted **if and only if** `len(step.expected_propositions) > 0` and `prop_verdict == Ternary.TRUE` ($xy$).

---

### 1.8 Carroll Nullity Completeness in Invariant Verification

In `brusentsov_logic.py`, the `contradicts()` operator exhaustively implements Carroll nullity ($xy'_0 \to \text{NULL}$) across all kinematic and topological dimensions:

1. **Object Identity Preservation**: When antecedent expectation asserts `predicate == "preserved"` and observation confirms `predicate in ("destroyed", "vanished", "missing")`, $x$ (preservation expected) and $y'$ (destruction observed) co-occur. Under Carroll's nullity rule, $xy'_0 \to \text{NULL}$.
2. **Physical Stagnation**: When expected motion is non-zero ($\Delta_{\text{exp}} \neq 0$) along row, column, or tuple vector, and observed displacement is zero ($\Delta_{\text{obs}} == 0$), the physical claim is refutable. The transition evaluates to incompatibility ($xy'_0$).
3. **Unintended Mutation**: When a step asserts that an entity remains stationary or invariant (`unchanged`, `stationary`, or $\Delta_{\text{exp}} == 0$), but observed displacement is non-zero ($\Delta_{\text{obs}} \neq 0$), an unexpected mutation occurred. This evaluates to incompatibility ($xy'_0$).
4. **Direction Inversion**: When expected and observed displacements move in opposite directions along an axis ($\text{sign}(\Delta_{\text{exp}}) \times \text{sign}(\Delta_{\text{obs}}) < 0$), the action's intended kinematic effect failed. This evaluates to incompatibility ($xy'_0$).
5. **Multi-Format Kinematics Support**: The operator handles tuple representations `(dy, dx)`, `moved`, `step_moved`, scalar signs `row_delta`, `col_delta`, and cross-comparisons with symmetric normalization.

---

### 1.9 Kinematic Boundary Protection & Obstacle Collision Soft Stop

To prevent spurious disqualification of confirmed directional actions when an actor collides with grid boundaries or impassable obstacles:

1. **Boundary Collision Detection (`is_blocked_by_boundary`)**:
   - Before evaluating a zero delta as action falsification, the executor checks whether the active component is in physical contact with the perimeter corresponding to the action direction ($y_{\min} == 0$ for UP, $y_{\max} == H-1$ for DOWN, $x_{\min} == 0$ for LEFT, $x_{\max} == W-1$ for RIGHT).
   - If in contact, the zero delta is recognized as physical obstruction rather than action failure. The candidate branch is severed without globally disqualifying the action from `GameMemory`.

2. **Obstacle Collision Soft Stop (`Tier 3`)**:
   - When motion produces zero grid delta against an established obstacle or wall rule in memory, the transition is classified as a **soft stop (`Verdict.OMIT`)** rather than a hard contradiction (`Verdict.NULL`).
   - The actor simply cannot pass through solid matter; no physical world law was broken. Confirmed kinematics in `GameMemory` remain protected from spurious deletion.

3. **Macro-Step Decomposition (Excising `break_on_null`)**:
   - Macro-commands (`count=N`) are unrolled into atomic steps where state invariants are enforced at every step. If an unexpected contradiction occurs, the candidate is cleanly severed, a diagnostic is recorded, and execution resets to $S_0$.

---

### 1.10 Evidence-Seeking Finite State Machine (E-FSM)

When `Verdict.UNDECIDED` is emitted, candidate trajectory execution is suspended, entering an active evidence-seeking loop:

1. **State Snapshotting & Execution Freezing**:
   - Immutable snapshot captured: `pending_step_snapshot = active_step`.
   - `evidence_seeking_active = True` engaged; execution cursor frozen (`candidate_advanced = False`, `candidate_severed = False`).

2. **Blocking `act()` Action Arbitration**:
   - Trajectory advancement and Solver calls are blocked.
   - If `evidence_probes_remaining > 0`, a targeted diagnostic probe action is emitted.
   - If `probe_queue` is exhausted, falls back to `Verdict.NULL`, severs the candidate, and resets cleanly to $S_0$.

3. **Post-Probe Re-evaluation**:
   - Upon observing the post-probe state, the verifier checks whether the epistemic ambiguity condition on `pending_step_snapshot` has resolved.
   - Resolved: `evidence_seeking_active` cleared; trajectory execution resumes cleanly.
   - Persisting: `undecided_streak` increments. If streak reaches `max_undecided_streak = 2`, falls back to `Verdict.NULL` and resets.

---

### 1.11 The 8-Tier Verification Cascade (`LayeredVerifier`) with Transient Cells Awareness

Every transition $(S_{t-1}, a_t, S_t)$ is evaluated through a strict, non-invertible 8-tier hierarchy, augmented in Version 10.8 with multi-frame transient cell awareness:

```
[Incoming Step Transition]
           │
  Tier 1:  ▼ Terminal Win Condition (WIN / levels_completed increase) ────────► FOLLOW
  Tier 2:  ▼ Terminal Loss Condition (GAME_OVER / LOST) ──────────────────────► NULL
  Tier 3:  ▼ Zero Grid Delta on Confirmed Motion:
           │   - Transient cells detected in animation? ──────────────────────► OVERRIDE (Effective Action)
           │   - Known obstacle / wall collision? ────────────────────────────► OMIT (Soft Stop)
           │   - Unexpected motion failure? ──────────────────────────────────► NULL (Contradiction)
  Tier 4:  ▼ Epistemic Uncertainty & Multi-Frame Tracking Ambiguity:
           │   - GroundedStep confidence == 'low' / ambiguous status ─────────► UNDECIDED
           │   - Ambiguity diff < matching_ambiguity_threshold (0.15) ────────► UNDECIDED
           │   - Participating TrackedObject confidence < 0.60 ───────────────► UNDECIDED
  Tier 5:  ▼ Explicit EXPECT Contradiction (implies_brusentsov == FALSE) ─────► NULL
  Tier 6:  ▼ Explicit EXPECT Necessary Containment (implies == TRUE) ─────────► FOLLOW
  Tier 7:  ▼ Unconfirmed Zero Delta or Low Metric Delta:
           │   - Transient cells present in animation? ───────────────────────► Effective Action Check
           │   - Zero Delta on Unconfirmed Action with non-empty EXPECT ──────► UNDECIDED
           │   - Sub-pixel displacement (0 < Delta < min_reliable_delta 0.8) ─► UNDECIDED
  Tier 8:  ▼ Certified Action Effect with Verified Propositions:
           │   - Non-zero delta (or transient cells) + verified non-empty EXPECT? ──► FOLLOW
           │   - Non-zero delta + empty / unverified EXPECT? ─────────────────► OMIT (No Vacuous Follow)
           │   - Default Fallback (Fail-Safe Preservation, ISO-10) ───────────► OMIT
```

- **Fail-Safe Default Guarantee (ISO-10)**: Tiers 7 and 8 strictly return `Verdict.OMIT`. Unless affirmative physical incompatibility ($xy'_0$) is proved, the candidate trajectory is never severed.
- **Transient Cells Integration**: When `raw_obs` carries intermediate animation frames where cells mutated and reverted ($\Delta(r, c) \ge 2$), `zero_delta` is overridden. Ephemeral lasers, projectiles, or scanning beams are marked as effective (`is_effective = True`), preventing false classification as `IDLE_SELF_LOOP`.

---

### 1.12 Structured Contradiction Diagnostics & Epistemic Recovery

When a candidate trajectory is severed at step $k$, `SymbolicTrajectoryExecutor` invokes `_build_step_contradiction_diagnostic()` to synthesize an informative diagnostic block:

```text
[FAILED ATTEMPT N DIAGNOSTIC]
Failed at step sK (function_name): Mismatch detected.
EXPECTED: moved(A, 0, 1) & unchanged(B)
OBSERVED: stationary(A, 0, 0) & moved(B, 0, 1)
DIAGNOSIS: function_name mutates alias B, not alias A. Do NOT repeat function_name for moving A!
```

This diagnostic, along with the physical grid diff (`summarize_grid_diff`), is recorded into `EpistemicMemory.record_attempt_feedback` and rendered directly into the Solver's `failed_attempts_scratchpad`. This differential feedback prevents the Solver from repeating contradictory hypotheses and enables rapid epistemic recovery.

---

## 2. Tri-Agent Separation of Powers

To guarantee zero cross-contamination, cognitive responsibilities are strictly partitioned among three specialized LLM call families:

```
                      ┌─────────────────────────────────────────┐
                      │               GameSession               │
                      │      (State Machine & Orchestrator)     │
                      └───────┬────────────┬────────────┬───────┘
                              │            │            │
                  Empirical   │     Syntax │ Declarative│ Multi-Candidate
                  Probing     │  Synthesis │   Planning │ Packages
                              ▼            ▼            ▼
                       ┌────────────┐┌────────────┐┌────────────┐
                       │  Explorer  ││   Coder    ││   Solver   │
                       │   Agent    ││   Agent    ││   Agent    │
                       └──────┬─────┘└─────┬──────┘└─────┬──────┘
                              │ Writes     │ Writes      │ Writes
                              ▼ Only       ▼ Only        ▼ Only
                       ┌────────────┐┌────────────┐┌────────────┐
                       │  EnvSpec   ││SyntaxError ││ Epistemic  │
                       │  Memory &  ││   Memory   ││   Memory   │
                       │Trans.Table ││            ││            │
                       └────────────┘└────────────┘└────────────┘
                              ▲            ▲             ▲
                              └────────────┴─────────────┘
                                  Strictly Quarantined
```

### 2.1 Explorer Agent (Call Family 1: Empirical Fact Discovery)
* **Mission**: Probe available actions (`ACTION1..5`) and spatial coordinates (`ACTION6`) on the pristine board ($S_0$) to extract deterministic action kinematics, coordinate affordances, entity switching mechanics, animation dynamics, and populate the `TransitionTable` WorldModel.
* **Memory Ownership**: Writes exclusively to `EnvironmentSpecMemory` (including `EnvironmentSpecMemory.transition_table`).
* **Prohibitions**: **Must not** formulate puzzle goals, hypothesize winning conditions, or plan multi-step paths.
* **Output Contract**: Valid JSON payload adhering to schema `v10.env_spec.1`, enriched with deterministic `empirical_transitions`, `action_affordances`, `confirmed_effective_actions`, and `conditional_candidate_actions`. If the LLM advisor fails or returns empty JSON, the deterministic baseline specification is preserved without blind overwrite.
* **Multi-Frame Animation & Transient Dynamics**:
  - Ingests animation analysis metadata (`transient_cells`, `trajectory_type`, `transient_colors`).
  - Classifies actions triggering ephemeral beams, projectiles, or scans into functional affordances (`BEAM_FIRE`, `PROJECTILE_LAUNCH`, `SCANNER_SWEEP`).
* **Two-Tier Action Lifecycle & Affordance Completeness**:
  - Discrete actions probed on the pristine initial frame $S_0$ are partitioned into `confirmed_effective_actions` (producing observable grid delta $\Delta > 0$ or transient animation cells) and `conditional_candidate_actions` (zero grid delta $\Delta = 0$ on $S_0$).
  - Zero-delta actions are **not discarded**. They are preserved in `available_actions` and typed as `EffectClass.CONDITIONAL_TRIGGER` affordances (`status: unconfirmed_on_s0`) in `EnvironmentSpecMemory`.
  - Per-object displacements are extracted by matching objects across frames first by `persistent_id` and then by color/shape/proximity, recording structured `TransitionRecord` entries into `TransitionTable`.
* **Action Space Partitioning, On-Mask Coordinate Probing & Dual-Space Synchronization**:
  - Probes are strictly partitioned: `ACTION1..5` are evaluated as discrete actions by `PrimitiveProbeManager.plan_discrete_probes()`.
  - `ACTION6` spatial coordinate probes are handled via `propose_coordinate_probes()`. To prevent clicking hollow background cavities on non-convex objects (`L`/`U`/`O`/ring shapes), `_select_on_mask_pixel(obj)` selects an actual pixel `(r, c) in obj.pixels` closest to the object centroid rather than a raw bounding-box midpoint.
  - All coordinate hypotheses and affordances operate strictly in local cropped grid coordinates `(0 <= x < width, 0 <= y < height)` matching the ARGA-Lite `PlanningSet`.
  - Coordinates are shifted by `crop_offset` when dispatched to the game engine (`engine_x = local_x + crop_offset`, `engine_y = local_y + crop_offset`).
  - Recorded probe actions preserve dual-space metadata. Tested coordinate sets decode engine coordinates back to local coordinates, guaranteeing that previously probed coordinates are **never re-probed**.
* **Universal Multimodal Dual-View**:
  - Explorer receives both `raw_frame.png` and `annotated_frame.png`, providing perceptual grounding for compound structures that the single-color connected-component parser fragments.

---

### 2.2 Coder Agent (Call Family 2: Sandboxed DSL Synthesis)
* **Mission**: Translate verified empirical facts from `EnvironmentSpecMemory` (including `empirical_transitions` from `TransitionTable`) and confirmed physics from `GameMemory` into a clean, typed Python Domain-Specific Language (DSL) module implementing high-level primitive operations.
* **Memory Ownership**: Writes exclusively to `SyntaxErrorMemory` upon compilation or runtime failure.
* **Prohibitions (ISO-2)**: **Strictly quarantined from goal definitions**. Does not know how to solve the puzzle, only how to manipulate objects according to the physics of the environment.
* **Execution Environment**: Compiled code is validated by `SafeASTVisitor` and executed inside `SandboxExecutor` under strict resource ceilings (10s CPU, 512MB RAM).
* **Incremental DSL Synthesis & Automatic Code Augmentation**:
  - The Coder develops the DSL incrementally across levels: previously confirmed actions (`action1..action4`) must be preserved and augmented with newly discovered level primitives (e.g. `action5` entity cycling or `action6` coordinate clicking).
  - **Automatic Augmentation Guard**: In `dsl_coder.py`, `generate_dsl` inspects both function names and `action_id` tags. If the LLM omitted any confirmed action from `GameMemory.confirmed_action_effects` or `env_spec["available_actions"]`, canonical implementation wrappers and manifest descriptors are automatically synthesized and injected:
    ```python
    def action5(api):
        """Canonical auto-augmented wrapper for confirmed action ACTION5."""
        return api.declare_environment_action(action_id='ACTION5')
    ```
  - **Sandbox Verification**: All augmented code undergoes restricted AST validation and dry-run execution against the current `PlanningSet`.
* **Universal Multimodal Dual-View**:
  - Coder receives both `raw_frame.png` and `annotated_frame.png` to cross-reference symbolic action semantics with macroscopic visual objects.

---

### 2.3 Solver Agent (Call Family 3: Declarative Planning, ObservedEdgeOverlay & Reflection)
* **Mission (Turn-1 Planning)**: Propose a structured package of up to 4 distinct multi-step candidate trajectories expressed in terms of the Coder's DSL manifest, with explicit `EXPECT:` propositions for every step.
* **Mission (Turn-2 Reflection)**: Following level completion or attempt exhaustion, analyze outcomes and distill domain-general invariants categorized into `[PALETTE & ROLES]`, `[GOAL]`, `[ENTITIES]`, `[CONTROL]`, and `[PHYSICS]`.
* **Memory Ownership**: Reads from and writes to `EpistemicMemory` and `GameMemory`. Receives sanitized `empirical_transitions` from `EnvironmentSpecMemory.transition_table`.
* **Prohibitions**: Never executes code, never emits raw actions directly to the environment, and never receives Python syntax error tracebacks. `ACTION7` does not exist for the Solver and is never proposed.
* **Triangulated Defeat Grounding**:
  - When planning following a `GAME_OVER`, the Solver prompt presents the decoupled defeat record:
    1. The sequence of verified safe prefix actions (`RETAIN PREFIX: Steps 1..K were SAFE: [a1 -> a2 ...]`).
    2. The isolated fatal step delta (distinguishing the lethal action from the subsequent level reset).
    3. Transient animation data (e.g. laser beam trajectory that caused death).
  - Explicit prompt instructions command the Solver to retain the safe prefix and explore branch variations strictly at or right before the fatal step.
* **Virtual Kinematic Sandbox & ObservedEdgeOverlay**:
  - Candidate trajectories proposed by the Solver are routed through `VirtualKinematicSandbox(planning_set, game_memory, transition_table=transition_table)`.
  - At step 0, `VirtualKinematicSandbox` consults `transition_table.get_known_edge(grid_hash, action_id, args)`: known `GAME_OVER` edges immediately reject the candidate, and known `IDLE_SELF_LOOP` leading steps are stripped (`REPAIRED`).
  - If no LLM candidates pass sandbox validation, `synthesize_invariant_trajectory` synthesizes fallback trajectories from discovered topological invariants for both directional (`ACTION1..4`) and coordinate-only (`ACTION6`) games (filtering out known `IDLE_SELF_LOOP` coordinates).
* **Source Authority Hierarchy (Prompt Grounding)**:
  1. **Raw frame pixels**: Absolute ground truth of screen content.
  2. **Empirical evidence log & `TransitionTable`**: Factual records of state-action transitions.
  3. **Annotated frame**: Parser segmentation used strictly to map alias labels to pixel regions.
  4. **Symbolic object index**: Lossy metadata representation. Where index and pixels conflict, pixels win.
* **DualView Grounding & Parser Over-Segmentation Compensation**:
  - Informs the model that the perception engine decomposes multi-color objects into monochromatic components. The model must consult raw pixels to identify compound patterns and multi-color composite shapes.
* **Differential Analysis & Severed Attempt Diagnostics**:
  - Section 7 of the Solver prompt provides `failed_attempts_scratchpad` containing exact physical grid diffs and `[FAILED ATTEMPT N DIAGNOSTIC]` analysis, enabling differential reasoning and preventing repetition of contradicted steps.

---

## 3. Stratified Memory Architecture & TransitionTable WorldModel

To facilitate lifelong cross-level learning and deterministic transition grounding without context pollution, memory combines five cross-level stores in `GameMemory` with the level-scoped `TransitionTable` WorldModel in `EnvironmentSpecMemory`:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 0. TransitionTable WorldModel (Trace + Quotient ObservedEdgeOverlay)        │
│    - Append-only monotone Trace (transitions) & Quotient edges              │
│    - IDLE_SELF_LOOP vs IDLE_UNLINKED, hidden_state_suspected, kinematics    │
│    - Multi-frame transient cell awareness & ephemeral trajectory metadata   │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. PaletteRoleMap: 16-color palette (0..15) affordances, roles & confidence │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. CoreInvariantRegistry: Invariants grounded in exemplars via Brusentsov   │
│    logic (NEGATIVE_BARRIER from Defeat, POSITIVE_CANON from Victory)        │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3. EpisodicExemplarBuffer: Concrete physical exemplars of terminal states   │
│    - DefeatExemplar: fatal_step_diff, fatal_transient_trajectory,           │
│      and valid_prefix_actions (Triangulated Defeat Architecture)            │
│    - VictoryExemplar: verified winning sequence on Level Win                │
├─────────────────────────────────────────────────────────────────────────────┤
│ 4. CurriculumProgressionBuffer: Cross-level trajectory history & patterns    │
├─────────────────────────────────────────────────────────────────────────────┤
│ 5. WorkingRolloutMemory: Active candidate steps, propositions & deltas       │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.1 16-Color Palette & Role-Aware Semantic Labeling

ARC-AGI-3 environments operate across a fixed 16-color palette ($0..15$). The agent models this palette through `PaletteRoleMap` and `ColorAffordance`:

```python
class EntityRole(str, Enum):
    BACKGROUND = "background"     # Empty / filler cells (typically most frequent color)
    ACTOR = "actor"               # Controllable object (moves with ACTION1..5 or clicks)
    OBSTACLE = "obstacle"         # Impassable walls (zero delta on collision)
    HAZARD = "hazard"             # Lethal color (contact triggers RESET / defeat)
    TARGET = "target"             # Goal zone / exit (contact triggers VICTORY)
    COLLECTIBLE = "collectible"   # Items that vanish on contact (keys, coins)
    PORTAL = "portal"             # Teleports or state-change triggers
    UNKNOWN = "unknown"           # Not yet classified
```

- **Non-Destructive Generalization**: Instead of erasing colors with destructive `[COLOR]` tokens, `PaletteRoleMap.generalize_color_reference` transforms color references into semantic labels: `Color N (ROLE)` (e.g., `Color 1 (ACTOR)`, `Color 2 (HAZARD)`, `Color 8 (TARGET)`).
- This preserves the exact color identifier while conveying its discovered functional role to the LLM.

---

### 3.2 Triangulated Negative Barrier Exemplars (`DefeatExemplar`)

Upon encountering `GAME_OVER` or a fatal state transition, the orchestrator constructs an immutable `DefeatExemplar` using Triangulated Defeat Grounding:

- **Fields**:
  - `level_index`, `fatal_step`, `fatal_action_id`, `fatal_coords`, `actor_position_before`, `hazard_color`, `environment_signal`, `explanation`.
  - `fatal_step_diff`: Exact physical delta between the pre-fatal state ($F_{\text{alive}}$) and the fatal collision state ($F_{\text{fatal}}$), isolating the lethal interaction from the subsequent board reset ($F_{\text{reset}}$).
  - `fatal_transient_trajectory`: Ephemeral trajectory of any projectile or laser active on the fatal step.
  - `valid_prefix_actions`: Sequence of verified safe actions executed from level start up to the step preceding death.
- **Brusentsov Grounding**: Grounds `NEGATIVE_BARRIER` invariants ($xy'_0 \to \text{NULL}$).
- **Prompt Injection**:
  ```text
  LAST DEFEAT (Level 0, Step 8):
    Fatal Action: ACTION3
    Actor was at: row=12, col=15
    Hazard color: 2
    Signal: GAME_OVER
    Fatal Step Outcome: 2 cells changed, moved dy=0, dx=-1
    RETAIN PREFIX: Steps 1..7 were SAFE: [ACTION4 -> ACTION4 -> ACTION1 -> ACTION1 -> ACTION4 -> ACTION2 -> ACTION2]. KEEP this prefix and branch to an alternate safe action at step 8!
    Lesson: Moving left (ACTION3) into Color 2 causes immediate destruction.
    DETERMINISM ENFORCEMENT: Environment is deterministic. Replaying the exact same actions to this point will cause death again. Plan an alternate path before the fatal step!
  ```
  This prevents the Solver from discarding verified progress and instructs it to explore branch points at the exact fatal frontier.

---

### 3.3 Positive Canon Exemplars (`VictoryExemplar`)

Upon level completion, the orchestrator captures a `VictoryExemplar` (and `LevelVictoryExample`):

- **Fields**: `level_index`, `total_steps`, `action_sequence`, `key_transitions`, `final_action_id`, `target_color`, `winning_invariants_used`, `explanation`.
- **Brusentsov Grounding**: Grounds `POSITIVE_CANON` invariants ($xy \to \text{FOLLOW}$).
- **Prompt Injection**: Injected as an objective physical demonstration of successful problem-solving, guiding subsequent levels with verified behavioral canons.

---

### 3.4 Grounded Invariant Lifecycle, Falsification & Empirical TransitionTable

1. **Grounded Invariants & Hypothesis Lifecycle (`CoreInvariantRegistry`)**:
   - Invariants in `CoreInvariantRegistry` are structured as `GroundedInvariant` and `InvariantHypothesis`:
     - `antecedent`: Condition (e.g. `Contact(ACTOR, Color_2)`).
     - `consequent`: Outcome (e.g. `DefeatReset()`).
     - `brusentsov_type`: `NEGATIVE_BARRIER` or `POSITIVE_CANON`.
     - `scope`: `CORE_GAME_LAW` (persists across all levels) or `LEVEL_SPECIFIC`.
     - Grounded directly in `DefeatExemplar` or `VictoryExemplar`.
   - **Falsification Rule**: An invariant is active iff `times_falsified == 0`. The first empirical contradiction on pristine $S_0$ permanently inactivates the invariant (`falsify_invariant`).

2. **Deterministic Empirical WorldModel (`TransitionTable`: Trace + Quotient)**:
   - Maintained inside `EnvironmentSpecMemory.transition_table` (`v10_agent/memory_contours.py`):
     - **Trace (`transitions`)**: Append-only monotone time log (`step_time = clock`) of `TransitionRecord` objects capturing `transition_id`, `level_id`, `action_id`, `action_data`, `before_grid_hash`, `after_grid_hash`, `zero_delta`, `idle_kind` (`IDLE_SELF_LOOP` vs `IDLE_UNLINKED`), `delta_cells`, `outcome_class` (`STATE_MUTATION`, `IDLE_SELF_LOOP`, `GAME_OVER`), `observed_effect`, `affordance`, `displacements` (`moved_object_ids`), `terminal` (`WIN` | `GAME_OVER` | `None`), and `kind` (`step` | `probe` | `reset` | `undo`).
     - **Quotient (`edges`: `(before_grid_hash, action_key) -> TransitionRecord`)**: `ObservedEdgeOverlay` indexing state-action outcomes via `build_transition_action_key(action_id, action_data)`.
     - **Animation and Transient Telemetry**: Ingests transient cells, trajectory geometry, and frame counts into `observed_effect`.
     - **Hidden-State Detector (`hidden_state_suspected`)**: Automatically flags non-Markovian / hidden-state transitions when the same `(before_grid_hash, action_key)` within the same level transitions to two distinct `after_grid_hash` states.
     - **Universal Ingestion**: Updated on every probe transition (`PrimitiveProbeManager.record_probe_result`) and every non-probe Solver/Fallback transition (`GameSession.observe_action_result`).

---

### 3.5 Architectural Isolation Invariants (ISO-1..ISO-18)

The integrity of the architecture is guarded by non-negotiable isolation invariants:

* **ISO-1 (Zero Syntax Tracebacks in Solver)**: Raw Python tracebacks, compiler errors, and AST violations are strictly confined to `SyntaxErrorMemory` and never leak into `EpistemicMemory` or Solver prompts.
* **ISO-2 (Curriculum Goal Quarantine for Coder)**: The Coder prompt and `EnvironmentSpecMemory` are strictly purged of all `[GOAL]` tags, target scores, and win conditions. Coder synthesizes mechanical manipulation primitives only.
* **ISO-3 (Sandbox Containment)**: All DSL code executes in an isolated subprocess with strict CPU, memory, and syscall restrictions.
* **ISO-4 (Immutable Perception Grounding)**: The `PlanningSet` extracted at frame $t$ is immutable. LLMs can refer to objects (`obj_0`, `obj_1`) but cannot mutate the underlying perceptual graph.
* **ISO-5 (Declarative Planning Purity)**: The Solver produces pure declarative text trajectories; it possesses no ability to invoke functions, mutate environment state, or inspect Python runtime state.
* **ISO-6 (Substantive Relation Filtering)**: Spatial relations in the `PlanningSet` are restricted to substantive entities ($area \ge 4$), eliminating combinatorial explosions from background cavities.
* **ISO-7 (Forward-Only Clean Reset Execution)**: Step reversal via `ACTION7` is prohibited. Erroneous paths are abandoned via environmental `RESET`, returning the system to pristine initial state $S_0$.
* **ISO-8 (Non-Destructive Palette Mapping)**: Concrete palette indices are converted into role-aware labels (`Color N (ROLE)`), preserving both color identity and semantic function across levels.
* **ISO-9 (Epistemic Signal Segregation)**: `Verdict.UNDECIDED` signals are stored in transient `epistemic_signals`, completely separated from confirmed historical `judgments`.
* **ISO-10 (Non-Severance on Expectation Mismatch)**: An unfulfilled step expectation that does not violate any established physical invariant yields `Verdict.OMIT`, strictly preserving the surviving candidate trajectory.
* **ISO-11 (Kinematic Boundary Protection)**: Zero grid delta on a motion action caused by contact with grid boundaries or selection-state requirements is classified as obstruction rather than physical falsification, preserving confirmed directional rules in `GameMemory`.
* **ISO-12 (Dual-Space Coordinate Consistency)**: Spatial coordinate reasoning and tested-coordinate deduction operate strictly in the local perception frame. Engine coordinate conversions ($+ crop\_offset$) must be symmetrically inverted when recording and evaluating tested coordinate history.
* **ISO-18 (WorldModel Sanitization of Control Actions)**: `TransitionTable.to_summary_list()` strictly excludes `RESET` and `ACTION7` (`kind in ("reset", "undo")`) when exporting `empirical_transitions` to LLM prompts and the virtual sandbox.

---

### 3.6 Persistent Object Tracking (`PersistentObjectTracker`)

To overcome object ID flicker across consecutive frames, perception is stabilized by `PersistentObjectTracker` (`v10_agent/tracker.py`):

1. **Normalized 4-Part Bipartite Matching Cost**:
   $$\text{Cost}(T, C) = 0.30 \cdot \text{color\_diff} + 0.40 \cdot \frac{\text{manhattan}(T, C)}{\max(H, W)} + 0.20 \cdot (1.0 - \text{Jaccard}(T, C)) + 0.10 \cdot \frac{|T_{\text{area}} - C_{\text{area}}|}{\max(T_{\text{area}}, C_{\text{area}}, 1)}$$
   Matches are accepted if $\text{Cost}(T, C) < 0.45$. Ties are resolved deterministically by lexicographic priority on `persistent_id`.

2. **Track Kinematics & Identity Permanence**:
   - Confidence: $\text{confidence} = 1.0 - \text{cost}$ (initialized to 1.0 upon spawn).
   - Velocity EMA: $\mathbf{v}_t = 0.3 \cdot (\mathbf{c}_t - \mathbf{c}_{t-1}) + 0.7 \cdot \mathbf{v}_{t-1}$.
   - Shape Stability: Decays by $\times 0.9$ if shape Jaccard $< 0.85$.
   - Cumulative Motion: Evaluated across a 3-frame window ($\Delta_{\text{cum}} = \mathbf{c}_{\text{newest}} - \mathbf{c}_{\text{oldest}}$).
   - Occlusion Detection: Unmatched track flagged `occluded = True` if overlapping an adjacent larger component within 3 px.

---

## 4. Action Space, Coordinates & Hardware Constraints

### 4.1 Partitioned Action Space

The action space partitions strictly into:
1. **Discrete Actions (`ACTION1..5`)**: Directional controls (`ACTION1` UP, `ACTION2` DOWN, `ACTION3` LEFT, `ACTION4` RIGHT) and entity toggle/mode switches (`ACTION5`). Canonical displacement vectors live in a single module `v10_agent/action_semantics.py` (`ACTION_VECTORS`); all consumers (session, judge, fallback, virtual_sandbox) import from there and must not maintain local inverted tables.
2. **Spatial Coordinate Actions (`ACTION6(x, y)`)**: Spatial clicks targeting specific grid cells. Probed via deterministic on-mask pixel selection (`_select_on_mask_pixel`) and Qwen coordinate proposals.

---

### 4.2 Hardware Constraint: Prohibition of `ACTION7`

`ACTION7` represents step reversal (`Undo`). The agent fundamentally excludes `ACTION7`:
- It is never generated by the Explorer, Coder, or Solver.
- If present in environment action manifests, it is filtered out by `allowed_action_ids`.
- Epistemic recovery is achieved exclusively through forward planning from clean initial states ($S_0$) via `RESET`.

---

### 4.3 1px Boundary Crop & Dual-Space Coordinate Mapping

ARC-AGI-3 environments frequently include a 1-pixel border perimeter around the active grid.
- **Normalization**: `normalize_observation` crops 1 border pixel on all 4 sides ($[1:-1, 1:-1]$), producing local dimensions $H_{\text{local}} = H - 2$, $W_{\text{local}} = W - 2$ with `crop_offset = 1`.
- **Local Reasoning**: All perception, object extraction, spatial relations, and planning operate exclusively in local coordinates $[0, W_{\text{local}}) \times [0, H_{\text{local}})$. Both `ARGALiteSnapshot` and `PlanningSet` compute deterministic SHA-256 `grid_hash` digests over the hex-encoded local grid rows.
- **Dispatch Translation**: When dispatching `ACTION6(x, y)` to the competition arcade gateway, coordinates are mapped to engine space:
  $$\text{engine\_x} = \text{local\_x} + \text{crop\_offset}, \quad \text{engine\_y} = \text{local\_y} + \text{crop\_offset}$$
  Action metadata records `{"x": engine_x, "y": engine_y, "local_x": local_x, "local_y": local_y, "crop_offset": crop_offset}`.

---

### 4.4 Tested Coordinate Deduplication Across Spaces

When reconstructing `tested_coords` from probe history, engine coordinates are decoded back into local space:
$$\text{local\_x} = \text{engine\_x} - \text{crop\_offset}, \quad \text{local\_y} = \text{engine\_y} - \text{crop\_offset}$$
This symmetric decoding prevents duplicate probing of identical physical locations.

---

## 5. Symbolic Execution, ObservedEdgeOverlay & Domain-General Invariants

### 5.1 Symbolic Trajectory Execution with Pre-Execution Idle Guard, Macro-Step Unrolling & Early Null Severance

Candidate trajectories are executed step-by-step by `SymbolicTrajectoryExecutor`:
- **Pre-Execution Idle Self-Loop Guard**: Before emitting step 0 of an active candidate, `prepare_and_execute_step` checks `transition_table.is_known_idle_self_loop(planning_set.grid_hash, action_id, action_data)`. If the leading action is a verified `IDLE_SELF_LOOP` on the current `grid_hash` (and `not transition_table.hidden_state_suspected`), the candidate is immediately circuit-broken (`known_idle_self_loop:...`) and severed without wasting an environment step.
- **Atomic Substep Decomposition**: Macro-step instructions like `action1(count=N)` are decomposed into $N$ atomic steps via `_decompose_expected_propositions_for_substep`.
- **Invariant Distribution**: State invariants (`unchanged`, `preserved`) are distributed to every intermediate substep. Incremental motion expectations (`step_moved: (sgn(dy), sgn(dx))`) are assigned to each step, while the full cumulative vector (`moved: (dy, dx)`) is evaluated on the final step.
- **Early Severance on Contradiction**: If any step receives `Verdict.NULL` (falsification, boundary collision, stagnation, or unintended mutation), execution of the candidate halts immediately:
  - `active_cand.sever()` is executed.
  - Remaining unexecuted steps are cleanly dropped.
  - `SymbolicTrajectoryExecutor` compiles a structured contradiction diagnostic block.
  - `GameSession` triggers a clean `RESET` to $S_0$, restoring the environment before testing the next candidate.

---

### 5.2 Multi-Frame Animation & Transient Cells Engine (`animation_analysis.py`)

ARC-AGI-3 environments often feature ephemeral animation effects such as projectile motion, laser beams, scanner sweeps, or interaction flashes that mutate across multiple intermediate frames and revert or terminate before the final static frame.

1. **Micro-Step Frame Sequence Extraction**:
   - Ingests raw `raw_obs.frame` from `arcengine`. Handles 3D arrays $(T, H, W)$, lists of 2D grids, and single static frames.
   - Slices and crops intermediate frames identically to the static observation ($[1:-1, 1:-1]$).
2. **Collapsed Chain & Transient Cell Detection**:
   - Prepend $S_{t-1}$ to the frame sequence and collapse consecutive identical frames.
   - Counts color changes per coordinate $(r, c)$ across consecutive frames:
     $$\text{changes}(r, c) = \sum_{k=1}^K \mathbf{1}_{f_{k-1}(r, c) \neq f_k(r, c)}$$
   - Coordinates with $\text{changes}(r, c) \ge 2$ are classified as **transient cells** ($\mathcal{C}_{\text{transient}}$). A cell changing once remains visible in the final frame; a cell mutating $\ge 2$ times represents dynamic pass-through or ephemeral effects.
3. **Geometric Trajectory Classification**:
   - Computes bounding box $[r_{\min}, c_{\min}, r_{\max}, c_{\max}]$ and spans $h_{\text{span}} = r_{\max} - r_{\min} + 1$, $w_{\text{span}} = c_{\max} - c_{\min} + 1$.
   - Evaluates trajectory geometry invariantly without regex:
     - $h_{\text{span}} = 1, w_{\text{span}} \ge 2 \implies \text{horizontal\_beam}$
     - $w_{\text{span}} = 1, h_{\text{span}} \ge 2 \implies \text{vertical\_beam}$
     - $h_{\text{span}} \ge 3, h_{\text{span}} > 2 w_{\text{span}} \implies \text{vertical\_sweep}$
     - $w_{\text{span}} \ge 3, w_{\text{span}} > 2 h_{\text{span}} \implies \text{horizontal\_sweep}$
     - $|\mathcal{C}_{\text{transient}}| \le 4, h_{\text{span}} \le 2, w_{\text{span}} \le 2 \implies \text{localized\_pulse}$
     - Otherwise $\implies \text{spatial\_sweep}$
4. **Transient Composite Construction**:
   - Renders a 2D composite grid `transient_composite` where transient coordinates are painted with their active non-reverted colors, making invisible raycasts directly perceptible to downstream visual reasoning and object tracking.
5. **Verifier & WorldModel Integration**:
   - When transient cells are present, `LayeredVerifier` classifies the action as effective (`is_effective = True`, `zero_delta = False`), preventing false `IDLE_SELF_LOOP` classification.
   - Recorded into `TransitionRecord.observed_effect` for WorldModel and Solver grounding.

---

### 5.3 Virtual Kinematic Sandbox, ObservedEdgeOverlay & Coordinate Invariant Synthesis

In `virtual_sandbox.py` and `universal_invariants.py`:
- Geometric aspect ratio $\ge 3.0$ is used generically to identify elongated or axis-like components regardless of absolute scale, operating invariantly on boards from $2 \times 2$ to $64 \times 64$.
- **ObservedEdgeOverlay Integration**: `VirtualKinematicSandbox` ingests `transition_table` to normalize confirmed kinematic vectors `{"dy": dy, "dx": dx}` into `(dr, dc)` tuples. During `evaluate_and_repair_trajectory`, step 0 is checked against `transition_table.get_known_edge`: known `GAME_OVER` edges are rejected (`REJECTED`), and known `IDLE_SELF_LOOP` leading steps are stripped (`REPAIRED`).
- **Coordinate-Only (`ACTION6`) Invariant Trajectory Synthesis**: When `has_directional_primitives` is `False`, `synthesize_invariant_trajectory` synthesizes a grounded click trajectory targeting on-mask pixels of the invariant's `subject` and `target` objects while skipping coordinates already recorded in `transition_table` as `IDLE_SELF_LOOP`.

---

### 5.4 Domain-General Topological Invariants

World physics is modeled using four domain-general invariants:
1. `ConnectedComponentConservation`: Verifies that an object retains its 4/8-connectivity and pixel area under spatial transformations.
2. `GravitySettling`: Models dynamic entities that settle along a directional gradient $(\Delta y, \Delta x)$ until contacting a support surface.
3. `ContactTrigger`: Models spatial adjacency between subject and trigger entities that induces a state change (barrier opening, teleportation, color transformation).
4. `AreaConservation`: Verifies that object pixel count is conserved across translations and rotations.

---

### 5.5 Multi-Candidate Package Traversal via Clean RESET

When the Solver produces a trajectory package containing candidates $\langle T_1, T_2, T_3, T_4 \rangle$:
1. $T_1$ executes step-by-step.
2. If $T_1$ encounters a hard `Verdict.NULL` or pre-execution circuit break, it is severed (`T1.sever()`).
3. If unsevered candidates remain ($T_2, T_3, \dots$), the orchestrator dispatches `RESET` (if the board was mutated) to restore clean state $S_0$, and execution immediately resumes with $T_2$.
4. If all candidates are severed, replanning is requested. The agent allows up to 5 chain attempts per level before falling back to the state-aware `SymbolicFallbackEngine`.

---

### 5.6 Triangulated Defeat Architecture and Single-RESET `GAME_OVER` Protocol

When the environment emits `state == "GAME_OVER"`:
1. **Frame Decoupling ($F_{\text{alive}} \to F_{\text{fatal}} \to F_{\text{reset}}$)**:
   - $F_{\text{alive}}$: The perception grid immediately prior to dispatching the fatal action.
   - $F_{\text{fatal}}$: The intermediate fatal frame returned upon death (capturing the fatal collision, laser impact, or hazard contact).
   - $F_{\text{reset}}$: The initial level grid after environmental reset.
2. **Defeat Triangulation**:
   - The orchestrator calculates `fatal_step_diff` by diffing $F_{\text{alive}}$ against $F_{\text{fatal}}$, preventing the level reset from contaminating the fatal interaction.
   - Captures any active projectile or laser in `fatal_transient_trajectory`.
   - Records the verified sequence of safe actions executed up to $F_{\text{alive}}$ in `valid_prefix_actions`.
3. Exactly **one** `RESET` action is emitted to restart the level.
4. Receiving `GAME_OVER` severs **only** the active candidate trajectory that caused the defeat. It captures a `DefeatExemplar` and resumes from $S_0$ with the next candidate in the pool.
5. The orchestrator tracks `last_engine_action_source` to prevent double-reset traps.

---

### 5.7 Cross-Level Invariant Discovery & Context-Driven Probing Protocol

* **Pristine Frame Invariant Evaluation ($S_0$)**: Cross-level invariant re-evaluation occurs strictly during the first `act()` call on the pristine observation of the new level ($S_0$, `level_initial_grid is None`), never on the victory frame of the prior level.
* **Reactivation of Probing Phase**: `handle_level_transition` sets `probing_phase = True` and clears level-local probe records and `TransitionTable`, discovering actions that become functional only on subsequent levels.
* **Selection Indicator Trigger**: When a probe reveals a selection indicator or entity toggle, targeted directional probes (`ACTION1..4`) are immediately enqueued to probe the kinematics of the newly activated entity before resetting to $S_0$.

---

### 5.8 Two-Tier Action Lifecycle & Reactive DSL Invalidation Pipeline

* **Two-Tier Preservation**: Actions evaluated during primitive probing that exhibit zero delta ($\Delta = 0$) on $S_0$ are tracked in `conditional_candidate_actions` and preserved in `available_actions` with `effect_class = CONDITIONAL_TRIGGER`. They are not discarded as ineffective.
* **Reactive Invalidation**: In `observe_action_result`, if any confirmed action is executed that is absent from `active_manifest`:
  1. `active_module` and `active_manifest` are invalidated (`None`).
  2. `coder_failed_for_level` is reset to `False`, allowing fresh Coder synthesis attempts.
  3. `replan_requested` is flagged `True` to trigger complete trajectory package replanning.
  4. `EnvironmentSpecMemory` dynamically synchronizes its action surface with the new confirmed effect.

---

### 5.9 Orchestration Contracts (Post-Audit Invariants)

These contracts are mandatory and match the production `session.py` / `config.py` / `trajectory.py` implementation:

1. **Deadline integrity**: `V10Config.to_dict()` omits all `_`-prefixed fields. `update_runtime()` never applies keys starting with `_` and never overwrites a live field with `None`. Harness merges therefore cannot wipe `_deadline_time`.
2. **Game-scoped reset**: `handle_game_transition` calls `_reset_game_scoped_state()`, which zeroes `levels_completed_observed`, evidence-probe counters, and undecided streaks so the next game's first level transition is observed.
3. **Live invariant registry**: `GameSession.invariant_registry` is a **property** resolving to the current `GameMemory.invariant_registry` on every access (no cached alias after memory rebuild).
4. **Trajectory pool API**: Inspection uses `TrajectoryPool.peek_active_candidate()` (no side effects). Progression uses `advance_to_next_candidate()`. `CandidateTrajectory.sever()` takes no arguments. Call sites must never invoke a non-existent `TrajectoryPool.sever(...)`.
5. **Harness config aliases**: `FIELD_ALIASES` maps competition harness names (`max_coder_retries`, `game_concurrency`, …) onto canonical `V10Config` fields; unknown keys are logged and ignored.
6. **Action vocabulary SoT**: Direction vectors, legal/forbidden ids, and displacement parsing live only in `action_semantics.py` (tokenizer-based, no regex for `dy=`/`dx=` semantics).

---

### 5.10 Entity Frame Differencing & Hungarian Jonker-Volgenant Matching (`v10_agent/frame_diff.py`)

Inter-frame state diffing operates over connected components matched across successive frames $t$ and $t+1$ via the Jonker-Volgenant linear sum assignment algorithm:
1. **Jonker-Volgenant Optimal Bipartite Matching**: Matches objects between $S_t$ and $S_{t+1}$ using a normalized cost matrix based on spatial centroid distance, area similarity, and color congruence.
2. **Deterministic Change Classification**:
   - `moved` / `step_moved`: Spatial translation along row and column dimensions $(\Delta r, \Delta c)$.
   - `rotated`: Pixel footprint transformation consistent with $90^\circ, 180^\circ,$ or $270^\circ$ rotation without centroid translation.
   - `resized`: Significant area scaling ($|\Delta \text{area}| > 0$) preserving aspect ratio.
   - `color_changed`: Pixel color transformation preserving geometry.
   - `appeared` / `disappeared`: Spawning or deletion of entities.
3. **Physical HUD & Timer Progress Bar Isolation**: Peripheral status lines, border timers, and progress meters are dynamically identified by aspect ratio ($\ge 4.0$) and monochrome boundary alignment (thickness up to 2-3px). Their localized pixel deltas are decoupled from the gameplay region, preventing artificial state hash corruption from peripheral clock ticks.
4. **Hungarian Proposition Grounding in LayeredVerifier**: Emitted frame difference propositions (`delta_r`, `delta_c`, `row_delta`, `col_delta`, `moved`, `step_moved`, `rotated`) directly feed into the 8-tier verification cascade of `LayeredVerifier`, verifying kinematics with mathematical precision.

---

### 5.11 Action Guards & Resilient Interior Grid Hashing (`v10_agent/action_guards.py`)

State-action transitions are protected by deterministic action guards that prevent destructive exploration loops:
1. **`NoopRepeatGuard`**:
   - Caches the last executed action and monitors whether it produced zero gameplay delta in the current interior grid state.
   - Prevents immediate consecutive re-execution of ineffective actions that collide with walls or stationary obstacles.
2. **`DeathActionGuard`**:
   - Records fatal state-action pairs `(interior_hash, action_sig)` upon encountering `GAME_OVER`.
   - In subsequent attempts, any candidate proposing a known fatal action in that state signature is immediately severed and blocked.
3. **Interior Grid Hashing (`compute_interior_grid_hash`)**:
   - Computes MD5 signatures over the inner $(H-2) \times (W-2)$ gameplay area, discarding outer margins where peripheral HUD bars tick.
   - Guarantees that state signatures remain invariant under peripheral timer changes, restoring Tabu memory stability.

---

### 5.12 Strict Single-Run Fallback Execution Contract Without Reset (`v10_agent/session.py`, `v10_agent/fallback_symbolic.py`, `kaggle_agent.py`)

The agent is governed by an absolute structural execution contract:
$$\text{Up to 5 LLM Solver Attempts} \longrightarrow \text{Exactly 1 Continuous Symbolic Fallback Run} \longrightarrow \text{Clean Abandonment Without Reset}$$

1. **Strict 5-Attempt LLM Budget**:
   - The Solver Agent plans and tests complete trajectory packages for up to 5 attempts per level.
   - Selective clean `RESET` actions are permitted between failed candidate trajectories or between attempts to restore pristine state $S_0$.
2. **Transition to Persistent Fallback**:
   - Upon exhausting 5 solver attempts, the agent permanently transitions to `in_persistent_fallback = True`.
3. **Zero-Reset Fallback Invariant**:
   - **`RESET` IS CATEGORICALLY FORBIDDEN IN FALLBACK MODE**.
   - If `GAME_OVER` occurs during fallback: the agent **NEVER** emits `RESET`. It immediately sets `session_aborted = True` and raises `LevelAttemptsExhaustedError`, transitioning cleanly to the next game in the queue.
   - If a cycle or dead end is detected during fallback: execution halts immediately without reset.
   - `SymbolicFallbackEngine.select_fallback_action` filters out `RESET` from allowed action IDs. If only `RESET` is available, the game is abandoned.
   - `kaggle_agent.reset_after_game_over` rejects reset requests if fallback is active.
4. **Clean Abandonment**:
   - The competition child runner catches `LevelAttemptsExhaustedError`, logs `agent_level_limit`, leaves the failed game without issuing a gateway reset, and proceeds to the next puzzle.

---

## 6. Competition Reliability & Serving Infrastructure

### 6.1 Coordinate-Aware `VisibleCycle` Loop Recovery (`cycle_detector.py` & `session.py`)

To prevent burning the per-level action budget (`max_actions_per_level`, default 80) in closed loops:
- Records transitions as tuples: $(\text{hash}(S_{t-1}), \text{ACTION\_KEY}, \text{hash}(S_t))$ using fast row-level MD5 hashing. For `ACTION6`, the action key includes the local click coordinates (`ACTION6:x,y`) so clicking distinct objects in sequence is never conflated with repeating a single action.
- Detects closed orbits of period $P \in [1..8]$ repeating $\ge 2$ times and spanning $\ge 8$ actions (config: `cycle_detector_min_cycles=2`, `cycle_detector_min_actions=8`).
- Automatically severs the active candidate via `CandidateTrajectory.sever()`, captures a failure record, resets the environment to $S_0$, and triggers replanning with cycle-avoidance constraints.

---

### 6.2 Deadline Management & Dynamic Time Budgeting

To safeguard the 5000-second per-game and 30600-second competition budgets:
- Monotonic deadline tracking with a 15-second reserve (`deadline_reserve_seconds = 15.0`).
- If remaining time is $\le 15.0$ seconds, LLM generation requests abort immediately, returning `"{}"`.
- Socket timeouts are dynamically clamped: $\min(\text{base\_timeout}, \max(2.0, \text{remaining\_time} - 15.0))$.
- Competition child process exits gracefully with `stop_reason = "deadline_reserve"`.

---

### 6.3 Resilient Production Remote TPU v5e-8 & Local vLLM Serving

The agent supports both local GPU serving and remote Google Cloud TPU v5e-8 server instances (`notebooks/tpu_api_server/build_tpu_api_notebook.py`):
1. **Remote TPU v5e-8 Architecture (Qwen3.8-27B)**:
   - Downloads fresh, official `cloudflared` binary via `curl -fsSL` from GitHub directly on startup (eliminating stale package dependencies).
   - Enforces `--protocol http2` flag on the Cloudflare quick tunnel, completely bypassing Kaggle outbound UDP/QUIC drops and maintaining a stable 9-hour HTTP/2 tunnel.
   - Dedicated tunnel background logger streaming progress to `/tmp/cloudflared.log` and notebook cell stdout.
   - Dedicated 60-second auto-reconnection watchdog script automatically probing tunnel health and re-establishing lost connections without interrupting the TPU XLA runtime.
   - Restores precompiled XLA cache from both tarball archives and loose JIT files, ensuring rapid startup under 3 minutes.
2. **Local GPU vLLM Configuration**:
   - Production server flags conforming to official vLLM Qwen3.8 recipes: `--max-model-len 262144`, `--max-num-seqs 8`, `--enable-auto-tool-choice`, `--tool-call-parser qwen3_xml`, `--mm-encoder-tp-mode data`, `--reasoning-parser qwen3`, `--enable-prefix-caching`, `--enable-chunked-prefill`, `--async-scheduling`, `--no-enable-log-requests`, `--disable-uvicorn-access-log`, `--gpu-memory-utilization 0.95`.
   - Native multimodal support with default item limit = 999.
   - Built-in MTP=5 speculative decoding: `--speculative-config '{"method": "mtp", "num_speculative_tokens": 5}'`.
   - Background Watchdog: Non-blocking daemon probing `/health` every 15s using `threading.RLock`. Automatically restarts stalled servers (up to 2 attempts).
   - Sub-millisecond Teardown: Probes socket in $< 0.05$s; if port is closed, exits in $< 1$ ms without invoking expensive shell processes.

---

### 6.4 State-Aware `TabuFallback` Engine & Generalized A* Search (`fallback_symbolic.py` & `virtual_sandbox.py`)

1. **State-Aware `TabuFallback` (`SymbolicFallbackEngine`)**:
   - Synchronizes continuously with `TransitionTable` (`_sync_from_transition_table` and `record_transition_outcome`) to maintain state-action tabu counts (`tabu_counts`), dead-end edges (`dead_end_edges` for `IDLE_SELF_LOOP` and `GAME_OVER`), and state-visitation penalties (`visited_state_counts`).
   - **Empirically Grounded Actor Selection (`_select_actor_object`)**: Selects the controllable actor for 2D BFS pathfinding by checking (1) objects with confirmed non-zero displacements in `TransitionTable.transitions` (`moved_object_ids`), (2) `GameMemory.confirmed_actors` (`id` and `persistent_id`), (3) `PaletteRoleMap` (`EntityRole.ACTOR`, excluding `OBSTACLE`/`HAZARD`/`BACKGROUND`), (4) perception role metadata, and (5) smallest non-obstacle object.
   - **Coordinate Candidate Ranking**: Filters out dead-end `(grid_hash, ACTION6:x,y)` edges and ranks remaining candidates by `(tabu_score, clicked_pen, is_center, role_prio)` using `transition_table.get_effective_coordinates()` and `PaletteRoleMap`.

2. **Generalized A* Search over Feature Differentials**:
   - Operates over a 4-feature differential vector:
     $$h(S) = 0.4 \cdot \Delta_{\text{centroid}} + 0.2 \cdot \Delta_{\text{bbox}} + 0.2 \cdot (1.0 - \text{color\_match}) + 0.2 \cdot \Delta_{\text{count}}$$
   - Perimeter coordinate clamping prevents spurious boundary exceptions during simulation:
      $$y \leftarrow \max(0, \min(H-1, y)), \quad x \leftarrow \max(0, \min(W-1, x))$$

---

### 6.5 Dynamic Priority Scheduling & Per-Level Action Caps (`priority_scheduler.py` & `lcld_competition_child.py`)

1. **Dynamic Priority Formula ($P = (A + B) \cdot C$)**:
   To maximize competition score under strict 9-hour runtime limits, compute allocation is dynamically scheduled across games using Daniel Franzen's formula:
   $$P = (A + B) \cdot C$$
   - **$A$ (Progress Ratio)**: $A = \frac{\text{levels\_completed}}{\max(1, \text{total\_levels})}$, prioritizing games where multiple levels have already been successfully solved.
   - **$B$ (Level Attempt Bonus)**: $B = \frac{1}{1 + \text{attempts}}$, granting high compute priority to freshly encountered levels and rewarding early breakthroughs.
   - **$C$ (Stall Decay Penalty)**: $C = \text{decay}^{\text{stagnant\_actions}}$, exponentially penalizing games where actions fail to progress the score, freeing execution slots for promising tasks.

2. **Per-Level Action Budget Hard Ceiling (`max_actions_per_level = 80`)**:
   - In `lcld_competition_child.py`, `actions_on_current_level` is capped at 80 actions.
   - If an agent fails to solve a level within 80 actions, the runner records `max_actions_per_level_exhausted`, terminates the game cleanly without reset, and transitions immediately to the next task in the priority queue.

---

## 7. Verification & Code Quality Assurance Stack

### 7.1 AST Code Guardian (`tools/ast_code_guardian.py`)

Static and semantic AST auditor enforcing the Anti-Specification Gaming Contract:
- Scans all Python source files in the codebase (137 files audited).
- Checks for forbidden game ID patterns (`ar\d{2}`, `ft\d{2}`, etc.).
- Checks for forbidden heuristic tokens (`piece_steps`, `axis_steps`, `internal dots`).
- Checks for hardcoded dimension comparisons (`width <= 4`, `height >= 10`).
- Verifies that `ACTION7` is never emitted as an executable action.
- Validates that `getattr(config, key, default)` calls do not drift from canonical `V10Config` field defaults.
- Verifies 0 violations across the entire codebase.

---

### 7.2 Property-Based Testing with Hypothesis (`v10_agent/tests/test_pbt_*.py`)

Exhaustive property-based verification of mathematical and geometric invariants:
- `test_pbt_brusentsov_axioms.py`: Verifies ex falso quodlibet elimination, Carroll nullity, identity consequence, and non-vacuous truth across randomized proposition sets.
- `test_pbt_brusentsov_severance.py`: Verifies Carrollian nullity completeness, physical stagnation, unintended mutation, direction inversion, consistent containment, macro-step decomposition, and early candidate severance.
- `test_pbt_scale_invariance.py`: Verifies grid parsing and topological invariants across arbitrary grid dimensions ($2 \times 2$ to $64 \times 64$).
- `test_pbt_color_permutation.py`: Verifies semantic role stability and prompt generalization under arbitrary permutations of the 16-color palette.
- `test_pbt_coordinate_isomorphism.py`: Verifies dual-space coordinate translations and tested-coordinate deduplication under arbitrary cropping offsets.
- `test_reactive_dsl_invalidation.py`: Verifies two-tier action lifecycle, preservation of unconfirmed candidates as `CONDITIONAL_TRIGGER`, reactive DSL module invalidation on newly confirmed effects, and Coder wrapper auto-augmentation.
- `test_universal_multimodal_dual_view.py`: Verifies DualView frame generation, perception grounding, and coordinate format consistency.

---

### 7.3 Multi-Frame Animation & Triangulated Defeat Verification

Dedicated test suites verify the v10.8 capabilities:
- `test_transient_cells_and_animation.py`: Verifies extraction of micro-step frame sequences, transient cell detection ($\Delta \ge 2$), geometric trajectory classification (beams, sweeps, pulses), transient composite generation, and override of zero-delta self-loops in `LayeredVerifier`.
- `test_fatal_frame_and_reset_decoupling.py`: Verifies that `GAME_OVER` decouples $F_{\text{alive}}$, $F_{\text{fatal}}$, and $F_{\text{reset}}$, builds isolated `fatal_step_diff` without board reset contamination, and preserves `valid_prefix_actions` in `DefeatExemplar`.

---

### 7.4 Comprehensive Full-Suite Test Coverage

The entire architecture is verified by **522 unit, integration, property-based, and lifecycle regression tests** (`pytest v10_agent/tests/ -q`), guaranteeing 100% specification compliance with zero regressions across all subsystems.
