# ARC-AGI-3 LCLD Agent
# Architectural Specification
# Version 10.9

## 0. Purpose

This document defines the Version 10.9 target architecture of the LCLD (Locally Constrained Learning and Discovery) agent for ARC-AGI-3 interactive reasoning under:

- completely unseen interactive grid environments;
- hidden mechanics and environment-local action semantics;
- dynamic, partially observable action surfaces;
- interactive online exploration with no offline training phase;
- strict offline execution and hard action/time budgets;
- deterministic object-centric perception;
- multi-frame transient dynamics and death/reset coupling;
- neuro-symbolic tri-agent cognition (Explorer, Coder, Solver);
- verifier-centered execution under Brusentsov entailment logic;
- four-valued semantic judgment including `OMIT` (inessentiality) and `UNDECIDED` (epistemic ambivalence);
- clean-reset recovery with forward-only epistemic consistency;
- stratified cross-level memory grounded in physical exemplars.

Version 10.9 preserves the tri-agent separation of powers, the Brusentsov verifier core, the isolation invariants of V10.5, and the V10.8 empirical world model and hardened execution layer. V10.9 is a semantics-alignment release: the verdict logic is synchronized with the canonical specification `Reasoning/Modified_Brusentsov_Entailment_Logic.md` (§0.5); the cascade order, tier structure, and judgment schemas are unchanged. The intelligence hierarchy is unchanged: the LLM tri-agent is the **Primary Proposer of facts, code, and plans**; the `LayeredVerifier` is the **Primary Truth and Execution Judge**. Memory, guards, and the `TransitionTable` form an explicit evidence layer between them.

The architecture is **not**:

- a monolithic LLM game player queried per-frame for the next action;
- an LLM-authorized action executor of any kind;
- an unconstrained code executor;
- a reinforcement learning policy requiring weight updates;
- a heuristic engine hardcoded to benchmark puzzles;
- a raw-pixel policy;
- a system dependent on `ACTION7` (Undo);
- a system that treats raw grid change as progress without verdict grounding.

The architecture **is**:

- a neuro-symbolic proposer/judge system with tri-agent separation of powers;
- an LLM-as-Proposer, Verifier-as-Judge architecture grounded in Brusentsov entailment logic;
- a deterministic ARGA-Lite perception and object-tracking substrate;
- a sandboxed, manifest-certified DSL synthesis pipeline;
- a symbolic trajectory executor with early null severance and clean-reset recovery;
- an empirical `TransitionTable` world model (trace/quotient) feeding pre-execution guards;
- a stratified, exemplar-grounded, cross-level memory architecture;
- an offline, budgeted, auditable, replayable ARC-AGI-3 solver.

### 0.1 V10.9 Authority Hierarchy

The normative authority hierarchy is:

1. **Environment Action Boundary** (gateway step/reset interface, `GAME_OVER` protocol, action and time budgets)
2. **LayeredVerifier and FrameDiff** (8-tier verdict cascade, transient-evidence overrides)
3. **ActionGuards** (NoopRepeatGuard, DeathActionGuard, interior-grid-hash stability)
4. **GameSession Orchestrator** (phase state machine, arbitration order, triangulated defeat, reactive DSL invalidation)
5. **SymbolicTrajectoryExecutor** (grounded step execution, pre-execution idle guard, macro-step unrolling, early null severance)
6. **VirtualKinematicSandbox** (forward simulation, ObservedEdgeOverlay, trajectory repair)
7. **Solver Agent** (declarative trajectory packages, invariant distillation)
8. **Coder Agent** (sandboxed DSL synthesis, auto-augmentation)
9. **Explorer Agent** (two-tier empirical probing, environment spec synthesis)
10. **Perception Engine** (ARGA-Lite, PersistentObjectTracker, FrameDiff, Transient Cells Engine)
11. **External Memory Stores** (PaletteRoleMap, CoreInvariantRegistry, EpisodicExemplarBuffer, CurriculumProgressionBuffer, WorkingRolloutMemory, TransitionTable)

The LLM tri-agent may propose empirical facts, DSL code, and declarative trajectory packages. It may not emit final actions. It may not authorize execution. It may not sever or preserve candidate branches. It may not revise grounded invariants directly. It may not assign final transition truth.

The verifier may confirm, contradict, mark inessential, or suspend a transition. `OMIT` is a first-class verdict, not a synonym for `NULL` and not a failure of reasoning. `UNDECIDED` is an epistemic controller signal, not a truth value.

### 0.2 V10.9 Core Loop

```text
raw observation (frame, metadata, state)
-> observation normalization (1px boundary crop, dual-space coordinates)
-> ARGA-Lite perception + PersistentObjectTracker + FrameDiff (+ Transient Cells from micro-frames)
-> immutable PlanningSet assembly
-> action guards and budget checks
-> GameSession arbitration (phase machine, priority order)
     PROBING:    Explorer probes -> TransitionTable + EnvironmentSpecMemory
     CODING:     Coder DSL synthesis -> AST validation -> sandbox dry-run -> certified manifest
     SOLVING:    Solver package -> VerificationBinder grounding -> TrajectoryPool
     EXECUTING:  executor emits one grounded step -> LayeredVerifier verdict
                 -> FOLLOW advance | OMIT advance | NULL sever + clean RESET | UNDECIDED evidence probe
     REFLECTING: exemplar capture, invariant distillation, curriculum update
     FALLBACK:   bounded state-aware Tabu A* run (no RESET)
-> exactly one action emitted per act() call
-> observe_action_result: TransitionTable trace/quotient update, memory writes, diagnostics
-> next arbitration with updated evidence
```

The loop is recursive, but the recursion state is external, budgeted, and auditable. LLM agents are stateless across calls; all episodic state lives in deterministic memory stores. Every emitted action passes through the guard/verifier path; no action reaches the environment from any other source.

### 0.3 Normativity and Exclusions

This document and the companion Engineering Specification are the **sole normative definition** of the agent architecture. The following are explicitly out of scope for both specifications and must never be recorded in them:

- concrete model artifacts, checkpoints, quantizations, or model-family names as hard dependencies;
- serving engine command lines, engine flags, speculative-decoding settings;
- accelerator topology, cluster identity, tunnels, ports, or network protocols;
- dataset mount paths, notebook packaging, or submission mechanics;
- local development or test-cluster configurations.

These belong to a **Deployment Manifest** maintained separately per runtime environment. The architectural contract is: the agent core resolves its LLM exclusively through the backend abstraction and `LLMModelProfile` of §11, and must run unchanged under any deployment manifest that satisfies that contract, including the `fake` backend used by tests.

Normative language: "must", "must not", "required", "forbidden", and "never" denote hard invariants enforced by tests or by the AST Code Guardian. "Should" denotes a strong default that may be varied only by configuration, never by code branches keyed to environments, models, or benchmarks.

Version discipline: any change to a contract, schema, cascade order, budget semantics, or isolation invariant requires a version increment of these documents. Operational tuning (model choice, engine flags, cluster) requires no specification change and must not produce one.

### 0.4 V10.8 Amendments over V10.5

V10.8 adds the following architectural elements to the V10.5 baseline:

1. **TransitionTable world model.** A per-level empirical transition graph with an append-only Trace and a state-action Quotient (`ObservedEdgeOverlay`), distinguishing verified idle edges (`IDLE_SELF_LOOP`) from untried edges (`IDLE_UNLINKED`).
2. **Transient Cells Engine.** Multi-frame micro-step analysis detecting cells that mutate two or more times within one logical transition, classifying transient geometry (`beam`, `sweep`, `pulse`), and overriding static zero-delta evaluation.
3. **Triangulated Defeat Architecture.** Decoupling of the fatal collision frame ($F_{fatal}$) from the post-death reset frame ($F_{reset}$), isolating `fatal_step_diff` for exemplar grounding.
4. **Jonker–Volgenant FrameDifferencing.** Optimal bipartite entity matching between consecutive frames producing strictly typed semantic deltas.
5. **ActionGuards.** Pre-emission guards (NoopRepeatGuard, DeathActionGuard) and peripheral-HUD isolation via `interior_grid_hash`.
6. **PriorityScheduler.** Explicit deterministic arbitration over competing action sources under budget pressure.
7. **State-aware Tabu fallback.** Empirically grounded actor/target selection for the fallback A* search, with tabu suppression of observed non-progressing edges.
8. **Model-neutral LLM runtime contract.** Canonical backend abstraction and `LLMModelProfile`; all model and serving specifics moved to the Deployment Manifest (§0.3, §11).

### 0.5 V10.9 Amendments over V10.8

V10.9 is a semantics-alignment release synchronizing the verifier logic with the canonical specification `Reasoning/Modified_Brusentsov_Entailment_Logic.md` (October 2026). It changes verdict **semantics and records**, not the cascade order, tier structure, or schemas:

1. **Normative source (§1).** The verifier logic is an instantiation of the canonical specification; the full mathematical treatment is no longer claimed by this section alone.
2. **Complete entailment form (§1.1).** $(x \Rightarrow y) \equiv x_1 \land (xy')_0 \land y'_1$ replaces the truncated $xy'_0$; the two-tier reading of $x'y'$ is fixed (§1.2).
3. **Canonical aliases, dominance chain, and `OMIT` subtypes (§1.3).** NULL ≻ UNDECIDED ≻ OMIT ≻ FOLLOW; OMIT_BLOCKED / OMIT_REDUNDANT / OMIT_INCIDENTAL mapped onto Tier 3, `NoopRepeatGuard`, and Tier 8.
4. **Completed nullity taxonomy (§1.4).** Two classes added: local state-consistency conflict and resolved out-of-contract active change ($\Omega_{\mathrm{sub}}$ empty by default).
5. **Prohibition of epistemic falsification (§4.3).** On probe/streak exhaustion the judgment permanently retains `UNDECIDED` (`ABORT_ON_UNDECIDED`); the previous rewrite into `NULL` is abolished; retained records never ground `NEGATIVE_BARRIER`.
6. **ISO-10 restated (§7.6) and the fail-safe default scoped to resolved cases (§4.6).** Epistemically unresolved transitions default to `UNDECIDED` (Tiers 4/7).
7. **`implies_brusentsov` rule 4 split (Engineering Specification §4.3).** Resolved out-of-contract change → `FALSE` unless inside a declared neutral region; neutral-region registry introduced (empty by default, contract-hashed).
8. **Test obligations extended** (Engineering Specification §4.6, §17.4): rule-4 conformance PBT, neutral-registry behavior, `UNDECIDED`-retention on exhaustion.

---

## 1. Theoretical Foundation: The Brusentsov Verifier (Brief Introduction)

This section is the concise normative introduction to the logic of the verifier for the ARC-AGI-3 domain. The full mathematical treatment is fixed by the canonical specification `Reasoning/Modified_Brusentsov_Entailment_Logic.md` (*Modified Brusentsov Entailment Logic and Four-Valued Verdict Calculus for External State-Control Systems*, October 2026; cited below as *canonical specification*): this section instantiates it for grid transitions and must not contradict it. No other document may extend the verifier logic without alignment to the canonical specification and a version increment of this document.

### 1.1 Why Material Implication Fails as a Verifier

Classical two-valued material implication $(x \to y) \equiv x' \lor y$ is unsound as an empirical verification semantics:

1. **Ex falso quodlibet.** A false premise validates any implication. An agent whose expectation did not occur would "confirm" arbitrary rules.
2. **Vacuous truth.** An action whose expected effect did not happen counts as confirming the rule "if this action, then that effect". The observation carried zero evidence, yet Boolean semantics returns TRUE.
3. **Loss of necessity.** Material implication expresses non-exclusion, not necessary consequence. Verification requires necessity: the effect must be contained in the action.

N.P. Brusentsov ("Усовершенствование логики умозаключений", 2012, MSU) showed that Aristotle's syllogistic entailment $Axy$ — "$y$ belongs to every $x$", i.e. $x = xy$ — was distorted by the forced two-valued reduction, and recovered the genuine entailment relation through Lewis Carroll's biliteral indexical method, in which the subscript «1» denotes **mandatory empirical existence** and the subscript «0» denotes **nullity (incompatibility)**. In the canonical conjunctive form (canonical specification §1.2):

$$(x \Rightarrow y) \equiv x_1 \land (xy')_0 \land y'_1$$

— the class $x$ is non-empty; it is impossible for $x$ to coexist with the absence of $y$ (the nullity component $(xy')_0$ alone is the Carrollian truth-condition of the consequence); and the complement $y'$ is non-empty (non-universality of $y$). The existence indices $x_1$ and $y'_1$ are what distinguish contentful entailment from material implication: operationally, non-universality is enforced structurally ($\mathrm{NonTriv}(y)$), and passive observations of $x'y'$ never confirm the law (immunity to the Hempel–Nicod paradox, canonical specification §3.4, Theorem 3.1).

### 1.2 Entailment as a Three-Valued DNF

The necessary entailment relation is the three-valued DNF:

$$x \Rightarrow y \equiv xy \;\lor\; xy'_0 \;\lor\; x'y'$$

where the term $x'y$ is **omitted as inessential**. The omission is not falsity: in Brusentsov's algebra, exclusion must be explicitly indexed («0»), affirmation is unindexed, and omission signifies inessentiality (несущественность) — the relation holds regardless of the omitted term.

| Term | Status | Verifier semantics |
| :--- | :--- | :--- |
| $xy$ | affirmed | **`FOLLOW (+1)`** — expected effect necessarily observed; trajectory advances |
| $xy'_0$ | excluded (nullity) | **`NULL (−1)`** — physical contradiction; candidate branch severed |
| $x'y$ | omitted | **`OMIT (0)`** — inessential outcome; branch preserved |
| $x'y'$ | affirmed | **`OMIT (0)`** — nothing expected, nothing relevant observed; branch preserved |

**Two-tier reading (canonical specification §1.4, §2.2).** The statuses in the right column are step-level (Tier 1) verdicts for a single observed transition. At the law level (Tier 2), both $xy$ and $x'y'$ carry the asserted status $+$ in the integral law (ternary vector $+{-}0+$); in a single transition the disjoint classes $xy$ and $x'y'$ cannot co-occur, so an $x'y'$ step evaluates as `OMIT` — incidental to the law — and an ensemble of such steps never confirms the law by itself (immunity to the Hempel–Nicod paradox, canonical specification Theorem 3.1). Law confirmation requires positive support ($ACy^{+}$ above the support threshold $N_{\min}$) plus non-triviality $\mathrm{NonTriv}(y)$, and yields the Tier-2 statuses `CONFIRMED` / `CONTRADICTED` / `CONDITIONAL_CANDIDATE` / `UNRESOLVED` (canonical specification §3.4). In this agent the law statuses are recorded as confirmed action laws, `NEGATIVE_BARRIER` invariants, and `CONDITIONAL_TRIGGER` preservation, respectively.

### 1.3 Four-Valued Decision Semantics

Because ARC-AGI-3 observation is partial (occlusion, hidden layers, tracking ambiguity), the ternary logic is extended with a fourth, non-truth value:

- **`FOLLOW (+1)`** — entailment confirmed ($xy$). The transition realized the grounded step's `EXPECT` propositions. Cursor advances.
- **`OMIT (0)`** — inessentiality ($x'y$ or $x'y'$). No physical contradiction, but the specific expected delta was not fulfilled (passive transition, selection change, empty expectation set). The candidate is **never severed** on `OMIT` (ISO-10).
- **`NULL (−1)`** — incompatibility ($xy'_0$). The transition contradicted an established invariant or expectation. The candidate is **immediately severed**; a clean `RESET` to $S_0$ is scheduled.
- **`UNDECIDED`** — epistemic ambivalence. Evidence is insufficient to decide between entailment and contradiction. Execution suspends and an evidence-seeking probe is scheduled (§4.3). `UNDECIDED` is a controller signal, not a truth value, and is stored separately from confirmed judgments (ISO-9).

Canonical aliases and aggregation (canonical specification §4.1–§4.2): `FOLLOW` ≡ REQUIRED (+1), `OMIT` ≡ IRRELEVANT (0), `NULL` ≡ FORBIDDEN (−1), `UNDECIDED` ≡ UNRESOLVED (U). Multi-clause aggregation is governed by the strict dominance chain

$$\mathrm{NULL}\ (-1) \succ \mathrm{UNDECIDED}\ (U) \succ \mathrm{OMIT}\ (0) \succ \mathrm{FOLLOW}\ (+1)$$

— a single certified `NULL` annihilates all other clause statuses (including `UNDECIDED`), and `FOLLOW` is the identity element (canonical specification Theorem 4.1). `OMIT` refines into three disjoint subtypes with fixed controller commands (canonical specification §5.2): `OMIT_BLOCKED` (soft stop / unfulfilled trigger — law preserved, trajectory repair; realized by Tier 3 boundary contact and ISO-11), `OMIT_REDUNDANT` (state descriptor unchanged — repeat suppression; realized by `NoopRepeatGuard`), and `OMIT_INCIDENTAL` (resolved inessential or sub-threshold change — retained with status 0, cursor advances; realized by Tier 8 retention).

### 1.4 Carrollian Nullity Completeness

`NULL` is triggered only by explicit incompatibility evidence. The verifier must detect at least the following contradiction classes (grid instantiation of the canonical nullity taxonomy, canonical specification Definition 3.1):

1. **Object identity violation** — expected `preserved`, observed `destroyed` / `vanished` / `missing` (or the inverse expectation). Identity is assessed only via explicit before/after presence predicates; a feature delta on a missing subject is undefined and must not be reinterpreted as an identity failure (canonical specification Definition 3.1, clause 1).
2. **Physical stagnation** — expected motion ($\Delta_{exp} \neq 0$), observed strict zero delta ($\Delta_{obs} = 0$) without boundary or obstacle contact, on an action whose effect is confirmed ($\chi_{\mathrm{conf}}=1$); on an unconfirmed action the same observation is `UNDECIDED` (Tier 7), never `NULL` (canonical specification §4.3, Steps 1–2).
3. **Unintended mutation** — expected stationary/invariant, observed motion ($\Delta_{obs} \neq 0$).
4. **Direction inversion / orthogonal leakage** — expected and observed displacement signs opposite on any axis ($\mathrm{sign}(\Delta_{exp}) \cdot \mathrm{sign}(\Delta_{obs}) < 0$; the discrete $\varepsilon_{\mathrm{inv}}=0$ case of canonical Definition 3.1, clause 3), or observed displacement along an axis expected to remain invariant.
5. **Local state-consistency conflict** — a resolved delta directly contradicts a previously committed `FOLLOW` assertion on the same subject and feature family (canonical specification Definition 3.1, clause 4).
6. **Resolved out-of-contract active change** — a reliably observed change lies outside the expected change set, is non-zero, and is not inside a contract-declared bounded neutral region $\Omega_{\mathrm{sub}}$ (canonical specification Definition 3.1, clause 5). A non-zero change is not neutral merely because it is non-zero: $\Omega_{\mathrm{sub}}=\emptyset$ by default, and any tolerance must be explicitly declared in the contract.

Attribute-value, relation-existence, spatial-position, area-conservation, and terminal-metadata contradictions are likewise nullity grounds when the expected and observed propositions share a subject and family. Propositions about distinct subjects can never contradict each other.

### 1.5 Prohibition of Vacuous Truth

- An empty expectation set evaluates strictly to `OMIT`. Absence of expectation is never confirmation.
- `FOLLOW` is granted **if and only if** the grounded step carries at least one expected proposition and every expected proposition is necessarily contained in the observed transition.
- A non-zero grid delta with empty or unverified expectations is `OMIT`, never `FOLLOW`.
- Kinematic invariants evaluated on the pristine frame $S_0$ without an executed action are `OMIT` (they can be neither confirmed nor falsified without a transition).

### 1.6 Verifier-Centered Consequence

The verifier, not any LLM, owns: legality of emission, truth of transitions, severance and preservation of candidate branches, reset scheduling, invariant falsification, and exemplar grounding. The LLM tri-agent owns: empirical fact proposals (Explorer), DSL code proposals (Coder), declarative plan proposals (Solver). Every proposal becomes an action only through the grounded, guarded, verifier-supervised execution path. This division is the operational form of the propose–judge–commit principle of the research program and is enforced by the isolation invariants of §7.6.

---

## 2. ARC-AGI-3 Environment Reality Model

ARC-AGI-3 environments are heterogeneous interactive games. The architecture assumes:

P1. Mechanics, goals, and physics are unknown a priori and are environment-local; nothing may be pre-programmed per benchmark.
P2. The action surface is partitioned: discrete actions `ACTION1..ACTION5` and the coordinate action `ACTION6(x, y)`; `ACTION7` (Undo) exists in some manifests and is architecturally forbidden; `RESET` is a meta-action, not a game action.
P3. Canonical direction vectors for `ACTION1..ACTION4` are simulation priors only; per-environment confirmed effects from empirical probing are authoritative and override priors on conflict.
P4. Actions yielding zero delta on the pristine frame $S_0$ may be conditional triggers whose preconditions arise later; they must never be discarded.
P5. Raw frames may carry a 1-pixel decorative border; the logical playfield is the cropped interior.
P6. The palette is the 16-color domain `0..15`; color indices carry functional roles that are empirical, level- and game-scoped, and must be mapped non-destructively.
P7. One logical step may span multiple rendered micro-frames; ephemeral effects (beams, sweeps, pulses) may leave no static trace.
P8. Peripherals (timers, counters, progress bars) may tick independently of game state; state signatures must be interior-stable.
P9. Death semantics are coupled: `GAME_OVER` may arrive together with, or shortly before, an automatic level reset; the fatal frame and the reset frame must never be diffed against each other.
P10. Observation is partial: entities may be occluded, ambiguous, or sub-threshold; judgment must support suspension and evidence seeking.
P11. Feedback is sparse: win/loss signals may be the only terminal information; progress claims require verdict-grounded evidence.
P12. Action and time budgets are hard: per-level, per-game, and wall-clock; loop burn is a first-class failure mode.
P13. Levels within one game share mechanics but may re-gate actions and roles; probing must reactivate on level transitions.
P14. Grid dimensions vary from $2 \times 2$ to $64 \times 64$; every algorithm must be scale-invariant across this range and across all permutations of the 16-color palette.

### 2.1 Grid and Palette Contract

Normative logical-state constraints:

- logical grids are rectangular with $2 \le H, W \le 64$ after normalization, and algorithms must remain correct for any dimension in this range;
- cells use integer palette IDs in `0..15`; the palette domain must never be destructively erased or requantized;
- semantic color roles are maintained by `PaletteRoleMap` as evidence-backed assignments (`EntityRole`), never as hardcoded mappings;
- state signatures exist in two forms: `grid_hash` (full logical grid) and `interior_grid_hash` (HUD-isolated interior, §5.8); guard and cycle logic must declare which signature it consumes;
- rendered RGB is debug/visualization-only and is never authoritative for verification;
- coordinate notation is strictly Cartesian: $x$ = column, $y$ = row; tuples are always explicitly labeled `(Row, Col)` or `(x, y)`.

### 2.2 Dual-Space Coordinate Contract

- normalization crops `crop_border_pixels = 1` on all four sides, producing the local perception grid $(H-2) \times (W-2)$ with `crop_offset = 1`;
- all perception, relation extraction, planning, probing, and deduplication operate exclusively in **local coordinates**;
- all engine dispatches translate to **engine coordinates**: `engine_x = local_x + crop_offset`, `engine_y = local_y + crop_offset`;
- action metadata must record both spaces plus the offset: `{x, y, local_x, local_y, crop_offset}`;
- tested-coordinate deduplication must symmetrically decode engine coordinates back to local space before comparison; a coordinate already probed in either encoding must never be re-probed;
- coordinate probes must target physical mask pixels of objects (`_select_on_mask_pixel`), never hollow bounding-box centroids that may fall outside the object.

### 2.3 Action Space Contract

- the action vocabulary has exactly one source of truth: `action_semantics.py` (canonical vectors, legal/forbidden IDs, meta-action classification, displacement tokenizers). No module may maintain a local or inverted copy;
- `FORBIDDEN_ACTION_IDS = {ACTION7}` is absolute: no agent may propose it, no adapter may emit it, manifest occurrences are filtered at ingestion;
- epistemic recovery is forward-only: erroneous paths are abandoned via environmental `RESET` to $S_0$, never via undo;
- actions are classified into the two-tier lifecycle:
  - `confirmed_effective_actions` — demonstrated observable delta or transient effect in some state;
  - `conditional_candidate_actions` — zero delta on $S_0$, preserved with affordance class `CONDITIONAL_TRIGGER` and status `unconfirmed_on_s0`;
- promotion from conditional to confirmed happens immediately upon first observed effect in any state; demotion of confirmed actions is forbidden except through invariant falsification with recorded evidence;
- `RESET` emission is restricted: exactly one `RESET` per `GAME_OVER` event; `RESET` is prohibited during fallback (§12.1).

### 2.4 Frame Dynamics Contract

- a logical transition is the pair $(S_{t-1}, a_t) \to S_t$ plus the micro-frame chain between them when available;
- cells mutating $\ge 2$ times within one logical transition are `transient_cells`; transient geometry is classified (`beam`, `sweep`, `pulse`) and recorded with the transition;
- the presence of transient cells overrides a static zero-delta reading: an action with transient evidence is effective, not an idle self-loop;
- entity correspondence across frames is established by optimal bipartite matching (Jonker–Volgenant) over a normalized cost of spatial distance, area similarity, and color congruence, producing strictly typed semantic deltas: `moved`, `rotated`, `resized`, `color_changed`, `appeared`, `disappeared`;
- on `GAME_OVER`, the frame triple $(F_{alive}, F_{fatal}, F_{reset})$ must be triangulated (§8.7): the fatal diff is computed strictly between $F_{alive}$ and $F_{fatal}$.

### 2.5 Failure Modes to Prevent

V10.9 explicitly guards against:

- querying an LLM per frame for the next action;
- executing any LLM output without AST validation, sandboxing, grounding, and verifier supervision;
- granting `FOLLOW` on empty expectations (material implication paradox);
- severing candidates on `OMIT` (collapsing inessentiality into contradiction);
- overwriting `UNDECIDED` with `NULL` on evidence-probe exhaustion (epistemic falsification; canonical specification §5.4);
- treating a resolved out-of-contract change as inessential without a contract-declared neutral region (canonical specification Definition 3.1, clause 5);
- classifying zero-delta transitions with transient animation as idle;
- classifying boundary or obstacle stops as falsification of confirmed action laws;
- re-probing coordinates already tested in the other coordinate space;
- discarding zero-delta actions probed on $S_0$ (losing conditional triggers);
- diffing pre-death frames against post-reset frames (corrupted fatal evidence);
- counting peripheral HUD ticks as game-state change;
- burning level budget in closed state-action orbits;
- double `RESET` on a single `GAME_OVER`;
- `RESET` emission during fallback;
- leaking Python tracebacks into Solver context or goal information into Coder context;
- hardcoding benchmark IDs, grid dimensions, or puzzle-specific constants anywhere in logic, prompts, or branch conditions;
- parsing spatial coordinates or action semantics with regular expressions;
- bypassing, reordering, or truncating the 8-tier verification cascade;
- branching agent logic on model family, model name, serving engine, or deployment specifics;
- treating raw grid churn as progress without a verdict-grounded evidence chain.

---

## 3. Architectural Layers

```text
Raw Observation
-> Observation Normalization (1px crop, dual-space, state normalization)
-> ARGA-Lite Deterministic Perception (components, cavities, relations, roles)
-> PersistentObjectTracker (multi-frame identity, kinematics, confidence)
-> FrameDiff (JV bipartite matching, typed semantic deltas)
-> Transient Cells Engine (micro-frame analysis, geometry classification)
-> PlanningSet (immutable grounding surface) + DualView frames
-> TransitionTable update (trace + quotient)
-> ActionGuards + Budget Checks
-> GameSession arbitration (PriorityScheduler)
     |-> Explorer Agent  -> EnvironmentSpecMemory
     |-> Coder Agent     -> sandboxed DSL module + certified manifest
     |-> Solver Agent    -> declarative trajectory package
-> VerificationBinder (grounding against PlanningSet)
-> SymbolicTrajectoryExecutor (macro-step unrolling, one action per step)
-> LayeredVerifier (8-tier cascade, four-valued verdict)
-> Verdict routing: advance | preserve | sever+RESET | evidence probe
-> Memory writes (exemplars, invariants, epistemic feedback, diagnostics)
-> Reflection and curriculum update
```

### 3.1 Correct Separation of Concerns

```text
Perception      = what is visible, tracked, and structurally related (deterministic).
TransitionTable = how the world actually responded to actions (empirical, append-only).
Explorer        = which empirical facts about actions and affordances hold (proposals).
Coder           = how verified facts become typed, sandboxed manipulation primitives.
Solver          = which multi-step trajectories are worth attempting, with what expectations.
Binder          = which proposed steps are grounded in the current PlanningSet.
Executor        = when and how one grounded step is emitted, unrolled, severed, reset.
Verifier        = what is confirmed, contradicted, inessential, or undecided.
Guards          = what must not be emitted at all (known no-ops, known death edges).
Memory          = what failed, what won, what is invariant, what is level-transient.
Fallback        = what to do when proposers are exhausted, strictly bounded and reset-free.
```

### 3.2 The Cognitive Triad

Cognition is partitioned into three LLM call families with disjoint memory ownership:

```text
                 ┌────────────────────────────────┐
                 │            GameSession         │
                 │   (state machine, arbitration) │
                 └───────┬────────┬────────┬──────┘
             Empirical   │ Syntax │Declarative
             probing     │ synth. │ planning
                 ▼       │        ▼        ▼
            ┌─────────┐  │  ┌─────────┐ ┌─────────┐
            │Explorer │  │  │  Coder  │ │ Solver  │
            └────┬────┘  │  └────┬────┘ └────┬────┘
        writes   ▼       │ writes▼      reads/writes ▼
        EnvironmentSpec  SyntaxError      Epistemic + Game
           Memory           Memory            Memory
```

#### 3.2.1 Explorer Agent (Call Family 1 — Empirical Fact Discovery)

- **Mission**: probe discrete actions and coordinate affordances on the pristine frame $S_0$; extract deterministic kinematics, transient animation facts, selection mechanics, and affordances into schema `v10.env_spec.1`.
- **Memory ownership**: writes exclusively to `EnvironmentSpecMemory`.
- **Prohibitions**: must not formulate goals, hypothesize win conditions, or plan multi-step paths.
- **Probing discipline**: two-tier lifecycle (§2.3); dual-space deduplication (§2.2); mask-pixel coordinate targeting; probe budgets from configuration.

#### 3.2.2 Coder Agent (Call Family 2 — Sandboxed DSL Synthesis)

- **Mission**: translate verified environment facts into a typed Python DSL module with manifest `v10.dsl_manifest.1`; develop the DSL incrementally across levels, preserving previously confirmed primitives.
- **Memory ownership**: writes exclusively to `SyntaxErrorMemory` on compilation/runtime failure.
- **Prohibitions (ISO-2)**: strictly quarantined from goals, scores, and win conditions; synthesizes manipulation mechanics only.
- **Certification**: every module passes AST whitelist validation, resource-bounded sandbox execution, and dry-run against the current `PlanningSet` before certification.
- **Auto-augmentation**: confirmed actions omitted from the synthesized module are automatically wrapped with canonical sandboxed primitives and manifest descriptors; augmentation output passes the same certification path.

#### 3.2.3 Solver Agent (Call Family 3 — Declarative Planning and Reflection)

- **Mission (planning turn)**: propose a package of up to `max_candidates_per_solver_package` (default 4) multi-step candidate trajectories over the certified DSL manifest, every step carrying explicit `EXPECT:` propositions, in schema `v10.trajectory_package.1`.
- **Mission (reflection turn)**: after victory or attempt exhaustion, distill domain-general invariants into the categories `[PALETTE & ROLES]`, `[GOAL]`, `[ENTITIES]`, `[CONTROL]`, `[PHYSICS]`.
- **Memory ownership**: reads/writes `EpistemicMemory` and `GameMemory`.
- **Prohibitions**: never executes code; never emits raw actions; never receives Python tracebacks (ISO-1); never proposes `ACTION7`.
- **Grounding inputs**: DualView frames with the source-authority order — raw pixels > empirical evidence log > annotated frame > symbolic object index; failed-attempt differential scratchpad with exact grid diffs and structured diagnostics (§4.7).

### 3.3 Double-Loop Feedback Routing

Feedback is routed by kind, never mixed:

- syntax/compilation/sandbox errors → `SyntaxErrorMemory` → Coder repair loop only;
- physical/logical transition outcomes, severances, diagnostics → `EpistemicMemory` → Solver adaptation loop only.

Cross-routing is an isolation violation and must be test-enforced.

### 3.4 Determinism Boundary

Deterministic and replayable by construction: normalization, ARGA-Lite, tracking, FrameDiff, transient analysis, PlanningSet assembly, TransitionTable, guards, binder, executor, verifier cascade, fallback search, memory updates.

Nondeterministic by nature and therefore record-bound: the three LLM call families. Every LLM call must be recorded (§14.3) and must be replayed from records, never re-queried. Given identical records, a full session run is deterministic.

---

## 4. LayeredVerifier: The 8-Tier Verdict Cascade

Every transition $(S_{t-1}, a_t, S_t)$ is evaluated by `judge.py` through a strict, non-invertible cascade. The cascade order must not be bypassed, reordered, or truncated.

### 4.1 Cascade

```text
Tier 1  Terminal win (WIN / levels_completed increase)                    -> FOLLOW
Tier 2  Terminal loss (GAME_OVER / LOST)                                  -> NULL
Tier 3  Zero delta on confirmed motion action:
          known obstacle/wall/boundary contact                            -> OMIT (soft stop)
          transient cells detected during the transition                  -> effective-action override (re-enter as non-zero-delta evidence)
          unexplained stagnation                                          -> NULL (contradiction)
Tier 4  Epistemic ambiguity:
          grounded-step confidence low / matching status ambiguous        -> UNDECIDED
          best-vs-second match cost gap < matching_ambiguity_threshold    -> UNDECIDED
          participating track confidence < track_confidence_threshold     -> UNDECIDED
Tier 5  Explicit EXPECT contradiction (implies_brusentsov == FALSE)       -> NULL
Tier 6  Explicit EXPECT necessary containment (implies == TRUE)           -> FOLLOW
Tier 7  Unconfirmed zero delta / sub-reliable delta:
          zero delta on unconfirmed action with non-empty EXPECT          -> UNDECIDED
          0 < max displacement < min_reliable_delta                       -> UNDECIDED
Tier 8  Certified action effect:
          non-zero delta + verified non-empty EXPECT                      -> FOLLOW
          non-zero delta + empty/unverified EXPECT                        -> OMIT (no vacuous FOLLOW)
          default fail-safe (ISO-10; resolved cases only)                 -> OMIT
```

**Mapping to the canonical cascade (canonical specification §4.3).** Tier 1/2 instantiate metric-contract terminal success and failure (cumulative crossing of $\theta_{\mathrm{succ}}$; breach of $-\theta_{\mathrm{fail}}$). Tier 3 boundary contact = `OMIT_BLOCKED` (canonical Step 5a); unexplained stagnation on a confirmed action = canonical Step 1(b) `NULL`. Tier 4 = canonical Step 2 (epistemic boundary: tracking confidence and match ambiguity make $\delta_{obs}$ unreliable, $Rel=0$). Tier 5 = canonical Step 1(a) (certified incompatibility, $\mathcal{C}^{\bot}$). Tier 6 = canonical Step 4 (complete necessary containment, $\mathcal{C}^{+}$). Tier 7 = canonical Step 2 (stagnation on an unconfirmed action, $\chi_{\mathrm{conf}}=0$; displacement below `min_reliable_delta` means $\delta_{obs}$ is *undefined* at the tracking resolution floor — epistemically unresolved, not sub-threshold-neutral; a contract-declared neutral region $\Omega_{\mathrm{sub}}$ would instead map resolved members to `OMIT_INCIDENTAL`, canonical specification §3.1, §6.1). Tier 8 = canonical Steps 3/5 (`OMIT` on empty/unverified expectations per canonical Axiom 4.1; the ISO-10 fail-safe default covers only epistemically resolved cases — all unresolved cases are intercepted by Tiers 4/7, matching the canonical epistemic default of Step 6).

### 4.2 Verdict Routing Effects

| Verdict | Executor effect | Session effect | Memory effect |
| :--- | :--- | :--- | :--- |
| `FOLLOW` | advance cursor | continue package traversal | confirm expectations; may ground positive canon |
| `OMIT` | advance cursor, branch preserved | continue; guards may suppress exact repeat | record as inessential; never a physics fact |
| `NULL` | `sever()`, drop remaining steps | schedule exactly one clean `RESET`; next candidate or replan | sever branch signatures; record diagnostic; may ground negative barrier |
| `UNDECIDED` | freeze cursor | enter evidence-seeking FSM (§4.3) | store in transient `epistemic_signals`, separate from judgments (ISO-9) |

### 4.3 Evidence-Seeking Finite State Machine

On `UNDECIDED`:

1. snapshot the pending step; freeze the execution cursor (no advance, no severance);
2. block trajectory progression and Solver calls while `evidence_seeking_active`;
3. if `evidence_probes_remaining > 0`, emit a targeted diagnostic probe authorized by the remaining-budget rule (`min_remaining_actions_for_probe`);
4. on the post-probe observation, re-evaluate the pending step: resolved → clear the flag and resume; unresolved → increment `undecided_streak`;
5. if the probe queue is exhausted or the streak reaches `max_undecided_streak`, terminate the attempt (`ABORT_ON_UNDECIDED`): the judgment record **permanently retains `UNDECIDED`** — it is never overwritten into `NULL`, and the retained record must never ground `NEGATIVE_BARRIER` invariants or branch signatures (prohibition of epistemic falsification, canonical specification §5.4); operationally: sever the current candidate, schedule exactly one clean `RESET` to $S_0$, and record the exhaustion reason code.

Evidence probes are speculative moves and must be affordable: they are authorized only while the level budget reserve is intact.

With `enable_undecided_verdict = False` (ablation), all ambiguity conditions map conservatively to `OMIT`, yielding classic three-valued operation.

### 4.4 Kinematic Boundary Protection and Soft Stop

Before treating a zero delta as falsification, the verifier must check physical obstruction:

- **boundary contact** — the active component touches the perimeter in the action direction;
- **obstacle contact** — memory-established wall/barrier rules or observed edge evidence explain the stop.

Obstructed stops are `OMIT` (soft stop), never `NULL`. Confirmed kinematics in `GameMemory` must never be deleted because of an obstructed stop (ISO-11). Severance of the current candidate may still follow from trajectory-level rules, but the action law itself remains confirmed.

### 4.5 Transient Evidence Override

Static frame comparison is insufficient under P7. The verifier must consume the micro-frame chain when available:

- transient cells present with zero static delta → the action is effective; the transition is evaluated on transient evidence (geometry class, trajectory direction) instead of the zero-delta branch;
- transient classification feeds `TransitionTable` outcome (`EFFECTIVE` with transient annotation) and prevents false `IDLE_SELF_LOOP` records;
- when no micro-frames are available, zero-delta evaluation proceeds under Tiers 3/7 with the ambiguity rules intact.

### 4.6 Fail-Safe Default

Among epistemically resolved transitions that trigger no nullity class (§1.4), the default verdict is `OMIT` and the candidate branch survives (ISO-10); epistemically unresolved transitions default to `UNDECIDED` (Tiers 4/7; canonical specification §4.3, Steps 2 and 6), never to `OMIT` or `NULL`. Severance requires positive contradiction evidence, terminal loss, cycle detection, guard interdiction, or operational attempt termination under retained `UNDECIDED` (evidence-probe exhaustion, §4.3) — each recorded with a reason code; only the first four are recorded as factual `NULL`.

### 4.7 Structured Contradiction Diagnostics

Every severance must synthesize a structured diagnostic:

```text
[FAILED ATTEMPT N DIAGNOSTIC]
Failed at step sK (function_name): mismatch class (stagnation | inversion | identity | mutation | ...).
EXPECTED: <expected proposition set>
OBSERVED: <observed proposition set>
DIAGNOSIS: <one deterministic sentence, e.g. "function_name mutates alias B, not alias A">
INSTRUCTION: do-not-repeat condition for the same operator/target absent new evidence.
```

Diagnostics plus the physical grid diff are written to `EpistemicMemory` and rendered into the Solver's failed-attempts scratchpad on the next planning turn. Diagnostics are deterministic functions of the judgment record; they must not contain raw model text.

---

## 5. Perception Engine

### 5.1 Observation Normalization

`observe.py` converts raw gateway observations into the canonical internal form:

- grid extraction and axis collapsing to a 2D integer grid;
- 1px boundary crop with `crop_offset` recorded (§2.2);
- state and action name normalization;
- deterministic `grid_hash` (row-encoded) and hex-row serialization.

Only normalized observations may enter perception, verification, memory, or prompts.

### 5.2 ARGA-Lite Object-Centric Perception

`arga_lite.py` produces the deterministic scene graph:

- background detection; monochrome connected-component segmentation (4/8-connectivity);
- per-component properties: color, pixel set, bounding box, centroid, area, shape signature;
- cavity detection (background regions enclosed by components);
- collinear axis-component merging for elongated structures (scale-free, gap-bounded);
- substantive filtering: components with area below `min_substantive_area` are excluded from the relation graph as decorative/noise (ISO-6);
- spatial relation extraction between substantive entities;
- functional role annotation of objects (candidate actor/target/hazard hypotheses, evidence-tagged, never final truth);
- spatial enclosure detection.

All ARGA-Lite outputs must be invariant across $2\times2..64\times64$ grids and 16-color permutations (PBT-enforced).

### 5.3 PersistentObjectTracker

`tracker.py` stabilizes identity across frames:

- normalized 4-part bipartite association cost:

$$\mathrm{Cost}(T, C) = 0.30\,\mathrm{color} + 0.40\,\frac{\mathrm{manhattan}}{\max(H, W)} + 0.20\,(1 - \mathrm{Jaccard}) + 0.10\,\mathrm{area\ rel.\ diff}$$

- match acceptance below `track_match_threshold`; deterministic tie-breaking by lexicographic `persistent_id`;
- per-track confidence $= 1 - \mathrm{cost}$; velocity EMA; shape-stability decay; cumulative motion over a sliding window; occlusion flagging within `occlusion_radius`; track aging with `track_max_age`;
- ambiguity (best-vs-second gap below `matching_ambiguity_threshold`) and low confidence feed Tier 4 `UNDECIDED`.

### 5.4 Frame Differencing (Jonker–Volgenant)

`frame_diff.py` resolves entity correspondence between $S_{t-1}$ and $S_t$ by optimal bipartite assignment (Jonker–Volgenant) under the normalized cost of spatial distance, area similarity, and color congruence, and emits strictly typed semantic deltas:

```text
moved | rotated | resized | color_changed | appeared | disappeared
```

FrameDiff output is the typed delta channel consumed by the verifier's observed-proposition extraction and by `TransitionRecord.moved_object_ids`. It must never invent deltas outside this vocabulary, and unmatched residue must be reported as `appeared`/`disappeared`, not silently dropped.

### 5.5 Transient Cells Engine

`animation_analysis.py` analyzes the micro-frame chain $f_0 \dots f_k$ of one logical transition:

- cells with mutation count $\ge 2$ across the chain are `transient_cells`;
- transient geometry is classified: `beam` (linear, axis-aligned), `sweep` (progressive front), `pulse` (localized, retracting);
- peripheral HUD regions are excluded from transient analysis (§5.8);
- outputs: transient cell list, geometry class, direction/trajectory summary, micro-frame count — all recorded with the transition and consumed by Tier 3 override (§4.5).

### 5.6 PlanningSet: The Sole Grounding Surface

`planning_set.py` assembles the immutable per-frame grounding surface:

```text
snapshot_id, grid_hash, full_grid_hex_rows, grid_dims, crop_offset
object_ids, objects (PlanningObject), object_real_to_alias / object_alias_to_real
relation_ids, relations (SpatialRelation)
allowed_action_ids, allowed_coordinate_candidate_ids, coordinate_candidates
```

- the PlanningSet extracted at frame $t$ is immutable (ISO-4): agents may reference objects and aliases but can never mutate the perceptual graph;
- every binder grounding, sandbox query, solver reference, and fallback target resolves against the active PlanningSet;
- coordinate candidates carry dual-space metadata (§2.2).

### 5.7 DualView Multimodal Rendering

`frame_media.py` renders synchronized frame pairs for every agent call that uses vision:

- `raw_frame` — unannotated pixels (absolute ground truth of screen content);
- `annotated_frame` — bounding boxes, alias labels, centroids overlaid.

Prompts must state the over-segmentation caveat: monochrome component parsing fragments multi-color compound objects; the raw view is authoritative for composite structure. Coordinate conventions in all rendered text follow §2.1.

### 5.8 Peripheral HUD Isolation

Border-adjacent timers, counters, and progress bars are identified by border thickness and bounding-box adjacency, and excluded from:

- `interior_grid_hash` — the state signature used by guards, cycle detection, and idle classification;
- transient-cell analysis;
- FrameDiff entity matching residue.

The full `grid_hash` remains available for exact replay identity. Any component consuming a state signature must declare which of the two hashes it uses; mixing them within one comparison is forbidden.

---

## 6. TransitionTable: Empirical World Model

The `TransitionTable` is the per-level empirical record of how the environment actually responded. It is append-only in its Trace and idempotent in its Quotient. It is the sole source of "known edge" facts for guards and fallback.

### 6.1 Trace

An append-only log of `TransitionRecord` entries, one per emitted action:

```text
step_index, level_id
pre_grid_hash, interior_pre_hash
action_id, coords (dual-space), action_source (probe | executor | evidence | fallback | reset)
post_grid_hash, interior_post_hash
delta_cells, moved_object_ids
transient_cells_present, transient_geometry, micro_frame_count
outcome_class: EFFECTIVE | IDLE_SELF_LOOP | LOSS | WIN
verdict (when judged), observed_effect summary
```

The Trace is the replay backbone: a session is replayable iff its Trace plus LLM call records reproduce every emitted action (§14.3).

### 6.2 Quotient (ObservedEdgeOverlay)

A state-action edge index:

```text
(interior_grid_hash, action_key) -> TransitionRecord
```

where `action_key` canonicalizes the action ID and, for `ACTION6`, the local-space coordinate. The Quotient must distinguish:

- `IDLE_SELF_LOOP` — a **verified** zero-delta edge (probed or executed with full observation);
- `IDLE_UNLINKED` — an **untried** edge (no record); absence of a record is never evidence of idleness.

### 6.3 Normative Uses

1. **Pre-execution idle guard** — the executor queries the Quotient before emitting step 0 of any candidate; a known `IDLE_SELF_LOOP` blocks the step and severs the candidate (§8.4).
2. **Probe deduplication** — the Explorer never re-probes an edge present in the Quotient, in either coordinate space.
3. **Death-edge cache** — `DeathActionGuard` reads LOSS-classified edges from the Quotient (§8.5).
4. **Boundary/obstacle evidence** — soft-stop classification consumes repeated zero-delta edges with contact evidence (§4.4).
5. **Reactive DSL invalidation trigger** — a confirmed effective action absent from the certified manifest invalidates the module (§9.3).
6. **Fallback grounding** — Tabu suppression and actor/target selection read the Quotient (§12.2).

### 6.4 Integrity Rules

- the Table is level-scoped; level transitions clear the Quotient but archive the Trace into the level record;
- records are written once, at `observe_action_result` time, from normalized observations only;
- records with incomplete observation (missing post-state) are written with `outcome_class = UNKNOWN_PENDING` and must never populate the Quotient;
- the Table must never be edited by any LLM output; all writes come from the deterministic observation path.

---

## 7. Stratified Memory Architecture

### 7.1 Five Cross-Level Memory Blocks

```text
1. PaletteRoleMap             — 16 colors -> evidence-backed EntityRole assignments + confidence
2. CoreInvariantRegistry      — GroundedInvariant records (NEGATIVE_BARRIER | POSITIVE_CANON)
3. EpisodicExemplarBuffer     — DefeatExemplar (on GAME_OVER), VictoryExemplar (on level win)
4. CurriculumProgressionBuffer— cross-level trajectory history and distilled patterns
5. WorkingRolloutMemory       — active candidate steps, propositions, transition deltas
```

Blocks are strictly partitioned: no block may write into another; cross-block flow happens only through the orchestrator and the reflection turn.

### 7.2 Agent Memory Contours

In addition to the five blocks, each call family owns a contour:

- `EnvironmentSpecMemory` — Explorer-owned empirical specs (`v10.env_spec.1`), affordances, displacements, probe records;
- `SyntaxErrorMemory` — Coder-owned syntax/sandbox failure records (bounded, most-recent-first);
- `EpistemicMemory` — Solver-owned attempt feedback: severed branch signatures, failed completed trajectories, diagnostics, differential scratchpad;
- `GameMemory` — consolidated game-scoped summary: confirmed action effects, selection mechanics, reusable primitives, invariant rules (tiered), solution patterns, confirmed actor IDs, plus handles to the five blocks.

Contour access is mediated by `MemoryContourManager`, which enforces the isolation invariants and raises on violation.

### 7.3 Exemplars and Grounded Invariants

- **`DefeatExemplar`** — captured on `GAME_OVER` via triangulated defeat (§8.7): fatal step, fatal action, dual-space fatal coordinates, actor position before, hazard color, isolated `fatal_step_diff`, `fatal_transient_trajectory`, `valid_prefix_actions`, environment signal. Grounds `NEGATIVE_BARRIER` invariants ($xy'_0 \to$ `NULL`).
- **`VictoryExemplar`** — captured on level completion: total steps, action sequence, key transitions, final action, target color, winning invariants used. Grounds `POSITIVE_CANON` invariants ($xy \to$ `FOLLOW`).
- Exemplars are injected into Solver prompts in a compact deterministic format; they are demonstrations, never executable macros. Winning sequences must not leak into Coder context (ISO-2).

### 7.4 Invariant Lifecycle and Falsification

`GroundedInvariant`: antecedent, consequent, Brusentsov type (`NEGATIVE_BARRIER` | `POSITIVE_CANON`), scope (`CORE_GAME_LAW` | `LEVEL_SPECIFIC`), grounding exemplar, confirmation/falsification counters, confidence, creation level.

- an invariant is active iff `times_falsified == 0`;
- a single empirical contradiction on the pristine frame $S_0$ permanently retires the invariant (falsification is recorded, never silent);
- cross-level re-evaluation of invariants occurs only on the pristine frame of the new level, never on the victory frame of the previous one;
- kinematic invariants evaluated without an executed action are `OMIT` (§1.5) and never count as confirmations.

### 7.5 PaletteRoleMap

- roles: `BACKGROUND, ACTOR, OBSTACLE, HAZARD, TARGET, COLLECTIBLE, PORTAL, UNKNOWN`;
- role assignment is evidence-backed (probe results, exemplars, invariant grounding) with confidence; a higher-confidence assignment supersedes a lower one; `UNKNOWN` is superseded by any evidence;
- generalization is non-destructive: color references render as `Color N (ROLE)`; the index is always preserved (ISO-8);
- role assignments are game-scoped by default and must be re-validated on level transitions when contradicted.

### 7.6 Isolation Invariants (ISO-1 .. ISO-12)

The integrity of the architecture is guarded by twelve non-negotiable invariants, each test-enforced:

- **ISO-1 Zero syntax tracebacks in Solver context.** Python errors are confined to `SyntaxErrorMemory`.
- **ISO-2 Curriculum goal quarantine for Coder.** Coder context and `EnvironmentSpecMemory` are purged of goals, scores, win conditions, and winning macros.
- **ISO-3 Sandbox containment.** All DSL code executes in the restricted sandbox with CPU/memory ceilings.
- **ISO-4 Immutable perception grounding.** The PlanningSet is read-only for all consumers.
- **ISO-5 Declarative planning purity.** The Solver produces declarative text only; no invocation capability, no runtime introspection.
- **ISO-6 Substantive relation filtering.** Relations are restricted to substantive entities (area threshold), preventing combinatorial explosion from background cavities.
- **ISO-7 Forward-only clean-reset execution.** `ACTION7` prohibited; recovery only via `RESET` to $S_0$.
- **ISO-8 Non-destructive palette mapping.** Color indices are preserved alongside roles.
- **ISO-9 Epistemic signal segregation.** `UNDECIDED` signals live in transient `epistemic_signals`, separate from confirmed judgments.
- **ISO-10 Non-severance on inessentiality.** Expectation mismatches carrying no certified nullity class (§1.4) yield `OMIT` and preserve the branch; unexplained strict stagnation on a confirmed action and resolved out-of-contract changes remain `NULL` grounds (canonical specification Definition 3.1).
- **ISO-11 Kinematic boundary protection.** Obstructed zero-delta stops do not falsify confirmed action laws.
- **ISO-12 Dual-space coordinate consistency.** Engine-space conversions are symmetrically inverted in recording and deduplication.

### 7.7 Memory Hygiene

- level-transient content (level-specific obstacle layouts, per-level object IDs and coordinates) is sanitized out of cross-level stores on level transition;
- game-scoped state is reset on game transition (counters, streaks, probe budgets, completed-level observations);
- all bounded stores declare their capacity and eviction order; eviction is deterministic (oldest/least-important first) and logged;
- memory writes are deterministic functions of judgment and observation records; no store may be written from raw model text without schema validation.

---

## 8. Symbolic Execution Engine

### 8.1 Grounding (VerificationBinder)

Every Solver-proposed step is grounded before execution:

- function names must exist in the certified manifest;
- object references must resolve to PlanningSet object IDs or aliases;
- coordinate arguments must resolve to allowed coordinate candidates or in-bounds local coordinates;
- unresolvable arguments raise `GroundingError`; the step is rejected with a reason, never executed with invented values;
- grounded steps carry `expected_propositions` parsed from the typed `EXPECT` grammar, plus optional `confidence` / `matching_status` feeding Tier 4.

Grounding output is `GroundedStep`: the only executable step representation.

### 8.2 Macro-Step Decomposition

- macro commands (`count=N`) are unrolled into $N$ atomic sub-steps;
- state invariants (`unchanged`, `preserved`) are distributed to **every** sub-step;
- incremental motion signs (`step_moved`) are verified at each transition; the cumulative vector (`moved`) is verified on the final sub-step;
- legacy silent-skip mechanisms (`break_on_null` and equivalents) are forbidden: contradictions surface as severance with diagnostics, never as skipped steps.

### 8.3 Early Null Severance and Clean-RESET Protocol

On `NULL`:

1. `active_candidate.sever()` — remaining steps are dropped;
2. the severed prefix and full signatures are written to `EpistemicMemory` (branch severance + failed-trajectory records);
3. a structured diagnostic is synthesized (§4.7);
4. exactly one clean `RESET` restores $S_0$ before the next candidate or replan;
5. on `GAME_OVER`: exactly one `RESET`; only the defeated candidate is severed; the pool resumes from $S_0$ with the next candidate; the orchestrator tracks the last engine action source to prevent double-reset traps.

### 8.4 Pre-Execution Idle Guard

Before emitting step 0 of a candidate, the executor queries the `TransitionTable` Quotient for the current state and action key:

- known `IDLE_SELF_LOOP` → the step is blocked and the candidate is severed with reason `known_idle_edge` (no environment action is wasted);
- `IDLE_UNLINKED` or effective edge → execution proceeds.

The guard consumes `interior_grid_hash` and must never fire on untried edges.

### 8.5 ActionGuards

Pre-emission interdiction layer, evaluated after arbitration and before dispatch:

- **NoopRepeatGuard** — blocks an action identical to the immediately preceding one when that action yielded zero delta with no transient evidence; the block is recorded and the candidate is re-arbitrated;
- **DeathActionGuard** — caches LOSS-classified edges from the Quotient and blocks re-emission of known fatal state-action pairs (same interior hash, same action key);
- **Budget guard** — no emission when the level/game action budget or deadline reserve is breached; exhaustion raises the bounded-exhaustion path (§8.8).

A guard block is never a physics falsification: confirmed action laws are untouched; only the emission is suppressed, with a reason code.

### 8.6 Multi-Candidate Package Traversal

For a package $\langle T_1, \dots, T_k \rangle$, $k \le$ `max_candidates_per_solver_package`:

1. execute $T_i$ step-by-step from $S_0$;
2. on severance, if unsevered candidates remain: one clean `RESET`, resume with $T_{i+1}$;
3. on package exhaustion: reflection turn, then replan;
4. hard ceiling: `max_chain_attempts_per_level` (default 5) chain attempts per level before the fallback contract engages (§12.1);
5. pool inspection uses non-mutating peek; progression is explicit; severance is a candidate-level operation only (Engineering Specification §10.4).

### 8.7 Triangulated Defeat Architecture

Direct comparison of a pre-death frame with a post-death reset frame corrupts fatal evidence. On `GAME_OVER` the orchestrator must:

1. retain $F_{alive}$ — the normalized state immediately before the fatal action;
2. capture $F_{fatal}$ — the intermediate collision/death frame when the gateway exposes it (micro-frame chain or pre-reset observation);
3. compute `fatal_step_diff` strictly between $F_{alive}$ and $F_{fatal}$; classify the fatal transient trajectory when transient evidence exists;
4. emit exactly one `RESET`; observe $F_{reset}$; verify level identity restoration;
5. construct the `DefeatExemplar` with `valid_prefix_actions` (the confirmed-safe prefix of the defeated candidate);
6. replan preserving the safe prefix; ground or reinforce a `NEGATIVE_BARRIER` invariant.

When $F_{fatal}$ is not observable, the exemplar is recorded with `fatal_frame_observed = false` and the diff degrades to action-level evidence only; it must never be synthesized from $F_{reset}$.

### 8.8 Budgets and Exhaustion

- per-level action budget (`max_actions_per_level`, default 80) and per-game budget (`max_actions_per_game`, default 500) are hard;
- exhausting the level attempt budget raises `LevelAttemptsExhaustedError`: the level is cleanly abandoned **without** emitting `RESET`;
- all probe classes (primitive, coordinate, evidence) draw from declared budgets; probes are authorized only above the reserve floor (`min_remaining_actions_for_probe`);
- every budget decrement is logged with the remaining value.

---

## 9. Sandboxed DSL Synthesis

### 9.1 Coder Contract

- input: `EnvironmentSpecMemory` facts, confirmed physics from `GameMemory`, DualView frames; never goals (ISO-2);
- output: one Python module of typed primitives (`def actionX(api, ...)`) plus manifest `v10.dsl_manifest.1`;
- the DSL is developed incrementally: previously certified primitives persist across levels and are augmented, not rewritten, when new actions are confirmed;
- synthesis temperature, output ceiling, and reasoning budget are role-scoped configuration (§11.3).

### 9.2 Certification Path

Every candidate module passes, in order:

1. response sanitization and code/manifest extraction;
2. AST whitelist validation (`SafeASTVisitor`): allowed modules only, no imports outside the whitelist, no I/O, no introspection, no dunder access;
3. sandbox load and dry-run against the current PlanningSet under CPU/memory ceilings;
4. manifest consistency check: every declared function exists, every confirmed action is represented — missing confirmed actions trigger auto-augmentation with canonical wrappers, which re-enter steps 2–4.

Only a fully certified module + manifest pair becomes `active_module` / `active_manifest`. Certification failure routes to `SyntaxErrorMemory` and the Coder repair loop, bounded by `max_coder_retries_per_level`.

### 9.3 Reactive DSL Invalidation

If execution or probing observes a confirmed effective action absent from the active manifest:

1. `active_module` and `active_manifest` are invalidated;
2. the Coder retry ceiling is unblocked for the level;
3. `replan_requested` is set, forcing a fresh Solver package after re-certification;
4. `EnvironmentSpecMemory` synchronizes its action surface with the new confirmed effect.

Invalidation is evidence-triggered only; no time-based or speculative invalidation exists.

### 9.4 Sandbox Boundary

The sandbox is the only execution environment for synthesized code. It exposes a narrow API surface (object queries, metric distances, action declarations, click declarations) over the immutable PlanningSet. Resource ceilings are configuration, not code. Any escape, timeout, or memory breach is a certification failure, recorded and routed to the repair loop. The sandbox never touches the environment gateway: DSL functions declare effects; the executor emits actions.

---

## 10. Session Orchestration

### 10.1 Phase State Machine

```text
SessionPhase: PROBING | CODING | SOLVING | EXECUTING | REFLECTING | FALLBACK
```

Legal transitions (all phases may self-loop):

```text
PROBING    -> CODING | FALLBACK | REFLECTING
CODING     -> SOLVING | PROBING | FALLBACK | REFLECTING
SOLVING    -> EXECUTING | PROBING | FALLBACK | REFLECTING
EXECUTING  -> REFLECTING | SOLVING | PROBING | FALLBACK
REFLECTING -> PROBING | SOLVING | EXECUTING | FALLBACK
FALLBACK   -> EXECUTING | PROBING | SOLVING | REFLECTING | FALLBACK
```

Illegal transitions must raise. Phase entry/exit is logged with a reason string.

### 10.2 Normative Arbitration Order

Within one `act()` call, after normalization and PlanningSet assembly, action sources are arbitrated in exactly this order:

1. game/level transition handling (non-emitting);
2. pending reset obligation (single-RESET protocol) → emit `RESET`;
3. evidence-seeking FSM (probe queue or exhaustion path) → emit probe or sever+reset;
4. persistent fallback mode → emit fallback step;
5. probing phase → emit next probe, or conclude probing and reset to pristine;
6. Coder phase trigger (no active module, retries remain) → synthesize (non-emitting);
7. Solver phase trigger (no runnable candidate) → generate package (non-emitting);
8. executing phase → emit next grounded step of the active candidate;
9. otherwise → bounded fallback emission.

Exactly one environment action is emitted per `act()` call. Non-emitting work (synthesis, planning, reflection) never consumes action budget.

### 10.3 PriorityScheduler

`priority_scheduler.py` owns the arbitration of §10.2 as an explicit, testable component:

- inputs: phase, guard interdictions, budget state, deadline state, pending obligations (reset, probes, evidence), pool status;
- output: the single winning action source with a reason code;
- the scheduler is deterministic: identical inputs produce identical decisions;
- under budget pressure the scheduler degrades in fixed order: disable speculative probes → disable non-strict LLM calls → prefer low-cost verifier-authorized actions → abandon level. Degradation steps are logged; none may bypass guards or the verifier.

### 10.4 Budgets

| Budget | Default | Scope |
| :--- | :--- | :--- |
| `max_actions_per_game` | 500 | game |
| `max_actions_per_level` | 80 | level |
| `max_chain_attempts_per_level` | 5 | level |
| `max_game_over_resets_per_level` | 5 | level |
| `max_coder_retries_per_level` / `max_solver_retries_per_level` | 5 / 5 | level |
| `max_primitive_probes_per_level` | 16 | level |
| `max_explorer_probe_actions_per_level` | 30 | level |
| `max_evidence_probes_per_level` | 3 | level |
| `min_remaining_actions_for_probe` | 25 | level |
| `deadline_reserve_seconds` | 15.0 | run |
| `game_wall_clock_limit_seconds` | 5000.0 | game |

Budgets are configuration; their **semantics** (hardness, exhaustion behavior, ordering) are normative and test-enforced.

### 10.5 Cycle Detection and Recovery

- transitions are recorded as $(\mathrm{hash}(S_{t-1}), a_t, \mathrm{hash}(S_t))$ over the interior hash;
- closed orbits of period $1..8$ repeating at least `cycle_detector_min_cycles` times over at least `cycle_detector_min_actions` actions trigger recovery;
- recovery: sever the active candidate, record the failure, one clean `RESET`, replan with cycle-avoidance constraints;
- recovery is limited to `cycle_detector_per_level_limit` (default 2) per level; further detection abandons the level path to fallback.

### 10.6 Level and Game Transition Protocol

- level transition: archive level-scoped stores (TransitionTable Quotient, probe records, working memory), sanitize level-transient content from cross-level stores, reactivate the probing phase, defer cross-level invariant re-evaluation to the pristine frame of the new level;
- game transition: reset game-scoped state (observed completed-level counters, evidence-probe budgets, undecided streaks) so the next game's first level transition is observed; game memory is rebuilt per game when configured;
- the invariant registry is resolved live from the current game memory on every access (no cached aliases).

### 10.7 Deadline Management

- the deadline is an absolute monotonic instant armed by the harness; re-arming with a smaller remaining value is legal, non-positive values are ignored;
- the deadline instant is a private runtime field: it never serializes into harness-facing config and is never overwritten by config merges (Engineering Specification §2.3, §11.6);
- on reserve breach: LLM requests abort immediately with an empty structured response; socket timeouts clamp to remaining time minus reserve; the run exits gracefully with reason `deadline_reserve`.

---

## 11. LLM Runtime Contract (Model-Neutral)

### 11.1 Backend Abstraction

All LLM access flows through one advisor interface (`generate` / `generate_chat` with role, messages, optional images). Backends:

```text
vllm               local offline OpenAI-compatible server (normative competition runtime)
openai_chat        generic OpenAI-compatible chat-completions endpoint (development only)
openai_responses   generic OpenAI-compatible responses-protocol endpoint (development only)
fake               deterministic in-process mock (tests; no network; no model files)
```

Vendor-specific adapters are instances of the generic contracts selected by adapter label or endpoint; they add no architecture. Competition runs must resolve to a local offline endpoint; cloud endpoints are development-only and must be disabled in the competition profile. The `fake` backend must satisfy every agent contract, so the full test suite runs without any model.

### 11.2 LLMModelProfile

Model identity and sizing live exclusively in a profile:

```text
profile_id                  (stable name of the profile, not of a model artifact)
backend                     (from §11.1)
model_ref                   (opaque deployment-manifest reference)
multimodal                  (bool)
context_tokens              max_input_tokens              max_output_tokens
temperature / top_p / top_k / seed
reasoning: enable_thinking, reasoning_strength, reasoning_budget_tokens
timeout_seconds
```

The architecture must not branch on model family, artifact name, quantization, or engine. Swapping models is a profile + deployment-manifest change only. Role-scoped overrides (per-agent temperature, output ceiling, reasoning budget) are part of the profile contract.

### 11.3 Call Families and Role Policy

- three call families only: Explorer (facts), Coder (code), Solver (plans/reflection);
- each family has role-scoped decoding policy and output ceiling; exploratory roles run hotter, synthesis roles cooler — exact values are configuration;
- per-frame action queries are forbidden: no call family may be invoked with "choose the next action" semantics;
- call volume is bounded by phase triggers and retry ceilings, never by frame count.

### 11.4 Output Discipline

- every family output conforms to its schema (`v10.env_spec.1`, `v10.dsl_manifest.1`, `v10.trajectory_package.1`) after sanitization and extraction;
- schema-invalid output is a bounded retry with a focused repair prompt, then a recorded no-op; it never reaches execution;
- no family may emit environment actions, coordinates-as-actions, or manifest revisions as facts;
- reasoning traces, when the profile enables thinking, stay inside the producing contour and are never routed across contours (ISO-1, ISO-2).

### 11.5 Serving Runtime Requirements

The deployment layer (out of specification scope, §0.3) must provide:

- a local OpenAI-compatible endpoint satisfying the profile's context and multimodal contract;
- deterministic decoding under the profile's temperature/seed policy;
- health monitoring with bounded automatic restarts (watchdog), non-blocking with respect to the agent loop;
- fast, graceful teardown that cannot leave orphaned servers or hang the run;
- startup validation (preflight) proving the endpoint, profile, and artifact agree before any game starts.

The agent core interacts with serving only through the advisor interface and the deadline/timeout clamps of §10.7.

### 11.6 Context and Budget Discipline

- prompts are assembled deterministically from memory stores and PlanningSet; assembly order and section inventory are fixed per call family (Engineering Specification §9.4);
- decision-critical sections (failed-attempt diagnostics, do-not-repeat instructions, allowed manifest surface, output schema, strict-format instruction) occupy the prompt tail and survive any compaction;
- under context pressure, compaction removes in fixed order: older curriculum history → older probe records → low-salience relation detail → older diagnostics (summarized, never dropped wholesale while the relevant branch is active);
- compaction must never remove: allowed action surface, valid object/alias IDs, coordinate contract, active diagnostics for the current planning turn, output schema.

---

## 12. Deterministic Fallback

### 12.1 Fallback Contract

The fallback engages only when proposer paths are exhausted (Coder ceiling, Solver ceiling, or `max_chain_attempts_per_level` reached) and is strictly bounded:

1. exactly one continuous `SymbolicFallbackEngine` run per level engagement;
2. `RESET` is prohibited during fallback;
3. a detected cycle or `GAME_OVER` during fallback abandons the level cleanly (no reset, no replan);
4. fallback emissions pass the same guards and the same verifier cascade as all other actions; the verifier is not relaxed in fallback;
5. fallback state (tabu set, visited signatures, step counter) is level-scoped and logged.

### 12.2 State-Aware Tabu A* Search

- actor selection is empirically grounded: confirmed actor IDs from `GameMemory` first; absent confirmation, deterministic candidate scoring over tracked objects (mobility evidence from the TransitionTable, area/role priors) — never a fixed heuristic pick;
- target selection prefers objects referenced in goal/invariant relations, then shape/mirror-compatible objects, with deterministic tie-breaking;
- search is A* over the grid with the normalized feature-differential heuristic:

$$h(S) = 0.4\,\Delta_{centroid} + 0.2\,\Delta_{bbox} + 0.2\,(1 - \mathrm{color\ match}) + 0.2\,\Delta_{count}$$

- perimeter clamping keeps simulated coordinates in-bounds;
- the tabu set suppresses state-action edges observed as `IDLE_SELF_LOOP` or as non-progressing in the current engagement; tabu entries expire on state-signature change;
- every emitted fallback step is recorded in the TransitionTable with `action_source = fallback`.

### 12.3 VirtualKinematicSandbox

`virtual_sandbox.py` provides forward simulation for planning support:

- kinematics extraction from confirmed action effects (single source: `action_semantics` + `GameMemory`);
- simulated invariant trajectories with collision/bounds checking;
- `ObservedEdgeOverlay`: simulation edges overridden by observed `TransitionTable` facts — observation always beats simulation;
- trajectory evaluation and repair: candidate packages may be pre-checked and repaired against simulation before execution; repair output re-enters grounding and verification, never execution directly.

Simulation is advisory: it may reorder, repair, or veto-before-emission, but it never authorizes an action by itself and never overrides a verifier verdict.

---

## 13. Execution Loop (Normative Pseudocode)

```text
initialize session (config resolve, deadline arm, preflight, memory build)
while not terminated:
    obs = gateway.step_result_or_initial()
    if game_changed: handle_game_transition()
    if level_changed: handle_level_transition()

    norm = normalize_observation(obs, crop_border)
    snapshot = arga_lite.extract(norm.grid)
    tracked = tracker.update(snapshot)
    diff = frame_diff.match(previous_snapshot, snapshot)          # JV bipartite
    transient = animation_analysis.extract(micro_frames)          # when available
    planning_set = build_planning_set(snapshot, allowed_actions, crop_offset)
    transition_table.record_trace(norm, last_action, diff, transient, verdict)

    if deadline_reserve_breached: exit_gracefully("deadline_reserve")
    if budgets_exhausted: abandon_level_or_game()

    source = priority_scheduler.arbitrate(phase, guards, budgets, obligations, pool)
    action = None
    match source:
        RESET_OBLIGATION:  action = single_reset()
        EVIDENCE_PROBE:    action = evidence_fsm.next_probe_or_exhaust()
        FALLBACK:          action = fallback_engine.step(planning_set)
        PROBE:             action = probe_queue.pop_or_conclude_probing()
        CODER:             certify_dsl_module(); continue            # non-emitting
        SOLVER:            pool = ground(solver.package()); continue  # non-emitting
        EXECUTE:           step = executor.next_grounded_step(pool, planning_set)
                           if transition_table.known_idle(state, step): sever; continue
                           action = step.emit_one()
    action = action_guards.filter(action, state)                    # noop/death/budget
    gateway.emit(action)

    result = gateway.observe()
    judgment = layered_verifier.evaluate(transition(result))        # 8-tier cascade
    route_verdict(judgment):
        FOLLOW:    executor.advance(); memory.confirm()
        OMIT:      executor.advance(); memory.record_inessential()
        NULL:      executor.sever(); defeat_or_contradiction_path(); schedule_reset()
        UNDECIDED: evidence_fsm.suspend_and_probe()
    memory.write(judgment, diagnostics, exemplars, invariants)
    if level_won: reflection_turn(); handle_level_transition()
```

---

## 14. Audit, Telemetry, and Replay

### 14.1 Action Audit Trail

Every emitted environment action is logged with: step index, phase, action source (probe | executor | evidence | fallback | reset), action ID, dual-space coordinates, guard decisions, budget state before/after, deadline remaining.

### 14.2 Judgment Records

Every judged transition persists a `BrusentsovJudgment`: verdict, expected/observed proposition sets, explanation, effectiveness flag, ambiguity evidence (score, matching candidates, minimum track confidence), action dictionary. Judgment records are append-only and keyed to the Trace.

### 14.3 LLM Call Recording and Replay Rule

Every LLM call records: call family, prompt hash, full prompt payload after compaction, profile ID, backend, response hash, parsed output, schema-validation result, retry count, token usage, latency.

Replay must not re-query any model. A replayed session loads recorded calls and recomputes the deterministic pipeline; a run that requires repeating nondeterministic LLM calls during replay is not a deterministic replay. The TransitionTable Trace plus LLM call records plus judgment records form the complete replay basis.

### 14.4 Required Telemetry (summary)

Per step: phase, source, verdict, severance, guard blocks, budget deltas. Per level: probes issued/deduplicated, chain attempts, invalidations, cycle events, fallback engagement, exhaustion reasons. Per game: wins, losses, abandoned levels, LLM call counts by family, schema-failure counts, memory write counts by store. Full key inventory: Engineering Specification §15.

---

## 15. Anti-Specification Gaming Contract

The codebase is governed by a purity contract enforced continuously by the AST Code Guardian:

1. **Categorically forbidden** in any logic, prompt, comment, or branch condition:
   - benchmark puzzle/game IDs;
   - hardcoded grid or object dimensions (except reading dynamic parameters from perception or PlanningSet);
   - regular expressions parsing spatial coordinates or action semantics (the tokenizer in `action_semantics.py` is the only sanctioned parser);
   - bypassing, reordering, or truncating the 8-tier cascade;
   - destructive color erasure replacing palette indices;
   - emission or proposal of `ACTION7`;
   - model-family or deployment-specific branching in agent code (§0.3, §11).
2. **Invariance principles**:
   - all algorithms operate invariantly from $2 \times 2$ to $64 \times 64$ and over the full 16-color palette;
   - color roles are grounded exclusively in exemplars and probe evidence;
   - aspect-ratio and scale-free geometric criteria replace absolute-size constants.

The Guardian runs over the whole package in CI and locally; any finding blocks acceptance.

---

## 16. Risk Model

| # | Risk | Mitigation (normative) |
| :-- | :--- | :--- |
| R1 | LLM hallucination reaches the environment | Binding + AST certification + sandbox + guards + verifier cascade; no emission path bypasses them (§0.1, §8, §9) |
| R2 | Vacuous confirmation inflates false progress | Brusentsov semantics; Tier 8 OMIT default; PBT axioms (§1.5, §4) |
| R3 | Irrelevance collapsed into contradiction (over-severance) | ISO-10; OMIT never severs; fail-safe cascade default (§4.6) |
| R4 | Transient dynamics misread as idleness | Transient Cells Engine override; interior-hash HUD isolation (§4.5, §5.5, §5.8) |
| R5 | Fatal evidence corrupted by reset coupling | Triangulated defeat; `fatal_frame_observed` honesty flag (§8.7) |
| R6 | Budget burn in loops | Cycle detector; NoopRepeatGuard; pre-execution idle guard; budget reserve floors (§8.4, §8.5, §10.5) |
| R7 | Probe thrash and re-probing | Quotient deduplication in both coordinate spaces; probe ceilings (§2.2, §6.3) |
| R8 | Conditional mechanics lost by premature pruning | Two-tier action lifecycle; CONDITIONAL_TRIGGER preservation (§2.3) |
| R9 | Cross-contamination of agent contours | ISO-1..ISO-12; MemoryContourManager enforcement; isolation tests (§7.6) |
| R10 | Specification drift via operational detail | Normativity and exclusions rule; Deployment Manifest; version discipline (§0.3) |
| R11 | Model lock-in | Backend abstraction + LLMModelProfile; fake-backend full-suite rule (§11) |
| R12 | Stale DSL suppressing newly confirmed actions | Reactive invalidation + auto-augmentation (§9.3) |
| R13 | Ambiguity thrash under partial observability | UNDECIDED segregation (ISO-9); bounded evidence FSM with `UNDECIDED`-retaining attempt termination (§4.3; canonical specification §5.4) |
| R14 | Fallback overreach | Single bounded run; RESET prohibition; same guards/verifier; clean abandonment (§12.1) |

---

## 17. Acceptance Criteria

Version 10.9 architecture is acceptable only if:

- the Brusentsov four-valued cascade is the sole transition judge, non-invertible and non-bypassable, with `OMIT` never severing, empty expectations never confirming, and `UNDECIDED` never epistemically falsified (§4.3);
- no LLM output reaches the environment except through grounding, certification, guards, and the verifier path; no call family is queried per-frame for actions;
- the tri-agent contours are isolated and test-proven (ISO-1..ISO-12), with double-loop routing by failure kind;
- the dual-space coordinate contract holds end-to-end, with symmetric deduplication and mask-pixel targeting;
- the two-tier action lifecycle preserves conditional triggers and promotes them on first evidence;
- the TransitionTable records every emitted action, distinguishes `IDLE_SELF_LOOP` from `IDLE_UNLINKED`, and feeds the pre-execution idle guard, probe deduplication, death-edge cache, and fallback grounding;
- transient evidence overrides static zero-delta classification, and HUD ticks never enter interior state signatures;
- defeat handling is triangulated: fatal diffs never mix $F_{alive}$ with $F_{reset}$, exactly one `RESET` per `GAME_OVER`, safe prefixes preserved;
- macro-steps are unrolled atomically with per-substep invariant checks; severance is immediate, diagnosed, and reset-clean;
- the fallback is a single bounded tabu A* run with empirically grounded actor selection, no `RESET`, and full verifier supervision;
- budgets, deadlines, and the priority scheduler degrade in the fixed normative order, with every decrement and degradation logged;
- the LLM runtime is model-neutral: backend abstraction + profile; the full test suite passes under the `fake` backend; no model, engine, cluster, or deployment identifier appears in agent logic or in these specifications;
- every action, judgment, and LLM call is recorded such that a session is replayable without re-querying any model;
- the AST Code Guardian reports zero findings; PBT suites prove scale, palette, and coordinate invariance and the Brusentsov axioms;
- the harness demonstrates improved wins or produces exact blocker diagnostics with verdict-level evidence.

---

## 18. Migration from V10.5 to V10.8

Mandatory migration changes:

1. Introduce `TransitionTable` (Trace + `ObservedEdgeOverlay` Quotient) as the per-level world model; wire all six normative uses (§6.3).
2. Introduce the Transient Cells Engine; Tier 3 must consume transient evidence before any zero-delta classification.
3. Introduce Jonker–Volgenant FrameDiff as the typed semantic-delta channel feeding observed-proposition extraction and transition records.
4. Introduce the Triangulated Defeat protocol; extend `DefeatExemplar` with `fatal_step_diff`, `fatal_transient_trajectory`, `valid_prefix_actions`, and the `fatal_frame_observed` honesty flag.
5. Extract `ActionGuards` (NoopRepeatGuard, DeathActionGuard, budget guard) and `interior_grid_hash` HUD isolation into a dedicated module consumed by the scheduler and executor.
6. Formalize the §10.2 arbitration order as `PriorityScheduler` with deterministic degradation semantics.
7. Replace heuristic fallback actor selection with state-aware, evidence-grounded selection plus tabu suppression over observed non-progressing edges.
8. Canonicalize configuration: one canonical field set per knob with an explicit alias table; introduce `LLMModelProfile`; remove all model artifacts, engine flags, cluster and tunnel specifics from specifications and agent code into the Deployment Manifest.
9. Canonicalize the backend enum (`vllm | openai_chat | openai_responses | fake`) with vendor labels as aliases; make the `fake` backend sufficient for the entire test suite.
10. Extend the test suite: transient-cell unit tests, triangulated-defeat differential tests, guard interdiction tests, scheduler degradation tests, tabu-fallback grounding tests, budget-exhaustion integration test (`LevelAttemptsExhaustedError` without `RESET`), and replay-basis completeness tests.

---

## 19. Migration from V10.8 to V10.9

Mandatory migration changes:

1. Rename the specification files and corpus references: `architectural_specification_v10_8.md` → `architectural_specification_v10_9.md`, `engineering_specification_v10_8.md` → `engineering_specification_v10_9.md`; engineering-cycle reports move to the `v10_9_*` namespace (historical V10.8-cycle artifacts keep their `v10_8_*` names).
2. `brusentsov_logic.implies_brusentsov`: split rule 4 into resolved/unresolved branches and add the neutral-region parameter (Engineering Specification §4.3); introduce the `NeutralRegionRegistry` consumed from `declared_neutral_regions` (empty by default; any change is a contract change and updates the contract hash).
3. Evidence-seeking FSM: replace the exhaustion fallback to `NULL` with attempt termination under permanently retained `UNDECIDED` (`ABORT_ON_UNDECIDED` reason code); suppress `NEGATIVE_BARRIER` grounding and branch-signature writes from retained records.
4. Extend the test suite: rule-4 conformance PBT (resolved out-of-contract change → `FALSE`; declared $\Omega_{\mathrm{sub}}$ member → `IRRELEVANT`; unresolved → `UNDECIDED` via Tiers 4/7), neutral-registry default-empty and contract-hash coupling, exhaustion-retention integration test (`test_pbt_undecided_exhaustion.py`).
5. No changes to: cascade order and tier count, `v10.judgment.1` / `v10.env_spec.1` schemas, verdict routing effects (§4.2), isolation invariants ISO-1..ISO-12 (ISO-10 restated, not renumbered), budget and arbitration semantics.
