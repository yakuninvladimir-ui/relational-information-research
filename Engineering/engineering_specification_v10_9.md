# ARC-AGI-3 LCLD Agent
# Engineering Specification
# Version 10.9

## 0. Engineering Objective

Build an ARC-AGI-3 agent that:

- normalizes heterogeneous interactive observations into a dual-space, HUD-isolated canonical form;
- extracts deterministic object-centric representations (ARGA-Lite) with persistent multi-frame identity tracking;
- resolves entity correspondence by optimal bipartite matching (Jonker–Volgenant) into strictly typed semantic deltas;
- detects ephemeral multi-frame dynamics via the Transient Cells Engine;
- maintains a per-level empirical world model (`TransitionTable`: Trace + Quotient) feeding guards, deduplication, and fallback;
- partitions cognition into three LLM call families (Explorer, Coder, Solver) with strictly isolated memory contours;
- certifies all synthesized DSL code through AST validation, sandbox execution, and dry-run before use;
- grounds all declarative plan steps against the immutable PlanningSet before execution;
- verifies every transition through the non-invertible 8-tier Brusentsov cascade (`FOLLOW / OMIT / NULL / UNDECIDED`);
- severs contradicted candidates early, with structured diagnostics and exactly one clean `RESET`;
- triangulates defeat evidence (`F_alive` → `F_fatal` → `F_reset`) and grounds exemplars and invariants from it;
- interdicts known no-op and known-fatal emissions via ActionGuards before they reach the environment;
- arbitrates action sources deterministically via PriorityScheduler under hard budgets and deadline reserve;
- degrades to a single bounded, reset-free, state-aware Tabu A* fallback when proposers are exhausted;
- records every action, judgment, and LLM call so that any session is replayable without re-querying a model;
- remains model-neutral: all LLM specifics resolve through the backend abstraction and `LLMModelProfile`.

Core ownership:

```text
Explorer/Coder/Solver = primary proposers (facts / code / plans)
Perception + Tracker + FrameDiff + Transient Engine = deterministic state serializer
TransitionTable = empirical world model
VerificationBinder = grounding authority
ActionGuards = emission interdiction
LayeredVerifier = final transition judge (Brusentsov 4-valued)
SymbolicTrajectoryExecutor = sole emission path for planned steps
GameSession + PriorityScheduler = orchestration and arbitration
Memory contours = external recursive state between verdicts and next proposals
SymbolicFallbackEngine = bounded deterministic last resort
```

Canonical logic foundation: `Reasoning/Modified_Brusentsov_Entailment_Logic.md` (October 2026) — verdict space V4, dominance order, decision cascade, typed certificates. The 8-tier cascade is its ARC-AGI-3 instantiation; the tier-to-canonical-step mapping is fixed in Architectural Specification §4.1.

Target constraints:

- Python 3.12 or newer;
- offline-only competition execution; no internet dependency at runtime;
- no hidden nondeterminism in the deterministic layer; all nondeterminism confined to recorded LLM calls;
- pytest must pass entirely under the `fake` backend: no real model, no network, no model files;
- full auditability of every action boundary;
- the LayeredVerifier is the only transition-truth authority; the guarded executor path is the only emission authority.

### 0.1 Normativity and Exclusions

This document specifies modules, contracts, schemas, configuration semantics, and tests. It does **not** specify, and code must not depend on: concrete model artifacts or families; serving engine flags or launch command lines; accelerator topology, clusters, tunnels, or ports; dataset mount paths; notebook packaging. These live in the Deployment Manifest (Architectural Specification §0.3). Any pull request that writes such content into these specifications or into agent-core code is rejected by review and by the AST Code Guardian.

---

## 1. Repository Structure

### 1.1 Agent Core (normative)

```text
v10_agent/
  types.py                    core value types: Grid2D, BoundingBox, Centroid, propositions
  action_semantics.py         SINGLE SOURCE OF TRUTH: action vectors, legal/forbidden ids, tokenizers
  action_adapter.py           gateway action normalization and boundary validation
  config.py                   V10Config, deadline tracker, env resolution, alias handling
  observe.py                  observation normalization, 1px crop, grid hashing
  arga_lite.py                deterministic perception: components, cavities, relations, roles
  tracker.py                  PersistentObjectTracker: bipartite association, kinematics, confidence
  frame_diff.py               Jonker-Volgenant frame differencing, typed semantic deltas
  animation_analysis.py       Transient Cells Engine: micro-frame analysis and geometry classes
  planning_set.py             immutable PlanningSet assembly (objects, aliases, relations, candidates)
  frame_media.py              DualView rendering: raw and annotated frames
  transition_table.py         Trace + Quotient (ObservedEdgeOverlay) world model
  brusentsov_logic.py         Ternary/Verdict enums, implies_brusentsov, contradicts, judgments
  verification.py             VerificationBinder, GroundedStep
  verifier_packet.py          offline symbolic verifier packet (v10.verifier_packet.1)
  judge.py                    LayeredVerifier: 8-tier cascade, proposition extraction, matching
  action_guards.py            NoopRepeatGuard, DeathActionGuard, interior_grid_hash, budget guard
  priority_scheduler.py       deterministic arbitration over action sources
  memory_contours.py          5 memory blocks + agent contours + MemoryContourManager
  universal_invariants.py     domain-general topological invariants and discovery
  explorer_agent.py           Explorer (call family 1) + PrimitiveProbeManager
  dsl_coder.py                Coder (call family 2): synthesis, extraction, auto-augmentation
  sandbox.py                  SafeASTVisitor, SandboxExecutor, SandboxAPI
  solver_agent.py             Solver (call family 3): package generation, EXPECT grammar, reflection
  trajectory.py               CandidateTrajectory, TrajectoryPool
  symbolic_executor.py        SymbolicTrajectoryExecutor: unrolling, severance, diagnostics
  virtual_sandbox.py          forward kinematic simulation, A*, ObservedEdgeOverlay, repair
  fallback_symbolic.py        SymbolicFallbackEngine: bounded state-aware Tabu A*
  cycle_detector.py           VisibleCycle orbit detection and recovery triggers
  session.py                  GameSession orchestrator: phase machine, transitions, defeat protocol
  policy.py                   emission arbitration policy helpers
  llm_advisor.py              backend abstraction: advisor interface, factory, sanitization
  logging.py                  structured JSON audit and session logger
  game_adapter.py             gateway/game interface adapters

  prompt_builders/
    explorer_prompt.py        probing and coordinate-hypothesis prompt assembly
    coder_prompt.py           incremental DSL synthesis prompt assembly
    solver_prompt.py          declarative planning and reflection prompt assembly

  tests/                      full suite; runs under the fake backend only
```

### 1.2 Deployment Layer (non-normative, out of architectural scope)

```text
kaggle_agent.py               competition gateway adapter
submission.py                 competition entrypoint and enum mappers
lcld_competition_child.py     isolated child-process runner
lcld_preflight.py             structural preflight validation (endpoint, profile, artifact agreement)
build_notebook_v10.py         notebook packaging
serving_*.py, watchdog        serving lifecycle, health monitoring, teardown (Deployment Manifest territory)
tools/ast_code_guardian.py    purity auditor (normative as a gate, deployment-agnostic)
```

Rules: deployment scripts must contain no agent cognition; agent core must contain no deployment paths, model names, engine flags, or cluster references; the only coupling is `V10Config` + `LLMModelProfile` resolved at startup.

### 1.3 Active-Path Rule

Do not create duplicate inactive modules. Every new module must be: imported by the active pipeline; covered by tests; or explicitly marked experimental and disabled by configuration. Legacy modules are replaced, wrapped, or routed cleanly — never left as dead parallel paths.

---

## 2. Configuration Contract

### 2.1 Canonical `V10Config`

One canonical field per knob. Vendor-prefixed duplicates (`qwen_*`) are **compatibility aliases**, resolved once at ingestion (§2.2); no module may read an alias directly.

```text
LLM runtime (resolved into LLMModelProfile, §2.4):
  llm_advisor_backend: vllm | openai_chat | openai_responses | fake        (default: vllm)
  endpoint_base_url: str                       local OpenAI-compatible endpoint
  endpoint_api_key: str                        opaque; never logged
  context_tokens / max_input_tokens / max_output_tokens: int
  temperature / top_p / top_k / min_p / presence_penalty / repeat_penalty
  seed: int
  timeout_seconds: int
  multimodal_enabled: bool
  enable_thinking: bool
  reasoning_strength: low | medium | high | xhigh
  reasoning_budget_tokens: int
Role-scoped overrides:
  solver_temperature (0.7)  coder_temperature (0.5)  explorer_temperature (0.9)
  solver_max_output_tokens (8192)  coder_max_output_tokens (8192)  explorer_max_output_tokens (2048)
  solver_reasoning_budget_tokens (24576)  coder_/explorer_reasoning_budget_tokens (8192)
  solver_/explorer_/coder_multimodal_enabled: bool

Trajectory and packages:
  max_candidates_per_solver_package: 4
  max_steps_per_candidate: 30
  execute_one_step_at_a_time: True

Perception:
  crop_border_pixels: 1
  min_substantive_area: 4         axis_merge_min_area: 6      axis_merge_max_gap: 15
  object_match_area_tolerance: 0.15
  movement_detection_threshold: 1.0
  max_probe_distance: 24.0

Tracker and 4-valued knobs:
  enable_persistent_tracker: True
  track_match_threshold: 0.45     track_max_age: 5            track_min_area: 1
  matching_ambiguity_threshold: 0.15
  min_reliable_delta: 0.8
  track_confidence_threshold: 0.6
  occlusion_radius: 3             cumulative_window: 3
  enable_undecided_verdict: True
  max_undecided_streak: 2        # k_max of canonical §5.4; on exhaustion the verdict stays
                                 # UNDECIDED forever (ABORT_ON_UNDECIDED), never NULL
  max_evidence_probes_per_level: 3
  min_remaining_actions_for_probe: 25
  declared_neutral_regions: {}   # Ω_sub registry (canonical §3.1); empty by default; any change
                                 # is a contract change (contract-hash update); consumed by rule 4 only

Transient engine:
  enable_transient_engine: True
  transient_min_mutations: 2
  transient_hud_exclusion: True

Sandbox:
  sandbox_enabled: True
  sandbox_allowed_modules: [math, typing, dataclasses, enum, collections]
  sandbox_max_cpu_seconds: 10.0
  sandbox_max_memory_mb: 512

Memory:
  game_memory_reset_on_game_change: True
  game_memory_reset_on_level_change: False
  epistemic_memory_max_entries: 50
  syntax_error_memory_max_entries: 5

Probing and fallback:
  enable_primitive_probing: True
  max_primitive_probes_per_level: 16
  probe_reset_after_discrete: False
  enable_symbolic_fallback: True
  coder_exhaustion_forces_fallback: True
  solver_exhaustion_forces_fallback: True
  abort_on_dsl_exhaustion: False

Cycle detection:
  enable_cycle_detector: True
  cycle_detector_min_actions: 8   cycle_detector_max_period: 8
  cycle_detector_min_cycles: 2    cycle_detector_per_level_limit: 2

Competition ceilings and deadline:
  max_actions_per_game: 500
  max_actions_per_level: 80
  max_game_over_resets_per_level: 5
  max_chain_attempts_per_level: 5
  max_coder_retries_per_level: 5
  max_solver_retries_per_level: 5
  max_explorer_attempts_per_level: 2
  max_explorer_probe_steps: 2
  max_explorer_probe_actions_per_level: 30
  max_invariant_verification_probes: 3
  max_invariant_probe_steps: 2
  reset_on_game_over: True
  deadline_reserve_seconds: 15.0
  game_wall_clock_limit_seconds: 5000.0
  competition_wall_clock_limit_seconds: 30600.0
  concurrency: int
```

Defaults in parentheses are shipped defaults; they are configuration, not architecture. Serving-engine parameters (speculative decoding, caching, scheduler flags, startup timeouts, max sequences) are **removed from `V10Config`** and belong to the Deployment Manifest; the agent core must not read them.

### 2.2 Alias and Environment Resolution

- one alias table maps harness/vendor vocabulary onto canonical fields (e.g. `qwen_backend -> llm_advisor_backend`, `game_concurrency -> concurrency`, `max_coder_retries -> max_coder_retries_per_level`, `qwen_vllm_model -> model_ref`);
- environment resolution uses the canonical `ARC_*` namespace (`ARC_LLM_ADVISOR_BACKEND`, `ARC_MODEL_REF`, `ARC_ENDPOINT_BASE_URL`, `ARC_CONTEXT_TOKENS`, `ARC_MAX_INPUT_TOKENS`, `ARC_MAX_OUTPUT_TOKENS`, `ARC_TEMPERATURE`, `ARC_SEED`, `ARC_TIMEOUT_SECONDS`, `ARC_ENABLE_THINKING`, `ARC_REASONING_STRENGTH`, `ARC_REASONING_BUDGET_TOKENS`, `ARC_MULTIMODAL_ENABLED`, role-scoped `ARC_SOLVER_*` / `ARC_CODER_*` / `ARC_EXPLORER_*`, and budget/deadline vars mirroring §2.1);
- legacy vendor-prefixed env names are accepted as deprecated fallbacks inside the resolver only, with a logged warning; they must never appear in agent-core reads;
- explicit user config wins over env; env wins over shipped defaults;
- unknown keys are logged and ignored, never applied.

### 2.3 Runtime Update and Deadline Contracts

```python
def to_dict(self) -> dict:
    # fields with leading underscore never leave the process via harness merge

def update_runtime(self, updates: Mapping) -> None:
    # resolve aliases; skip underscore-prefixed keys; never overwrite a live field with None;
    # log and ignore unknown keys

def set_deadline(self, wall_clock_seconds: float) -> None:
    # arm absolute monotonic instant; re-arming with a smaller value is legal;
    # non-positive values ignored (never arm an expired deadline)

def resolve(self, key, default=None):
    # single accessor for call sites: alias-resolved, dataclass-backed;
    # call sites must not embed their own fallback literals
```

`_deadline_time` is private: it is excluded from `to_dict()` and immune to harness config merges.

### 2.4 `LLMModelProfile`

```text
LLMModelProfile:
  profile_id: str                     stable profile name (not a model artifact name)
  backend: vllm | openai_chat | openai_responses | fake
  model_ref: str                      opaque Deployment Manifest reference
  multimodal: bool
  context_tokens: int
  max_input_tokens: int
  max_output_tokens: int
  temperature / top_p / top_k / seed: sampling policy
  reasoning: {enable_thinking, reasoning_strength, reasoning_budget_tokens}
  role_overrides: {solver, coder, explorer} -> {temperature, max_output_tokens,
                                                reasoning_budget_tokens, multimodal}
  timeout_seconds: int
```

Reference baseline profile (illustrative defaults; the architecture must not depend on them):

```text
profile_id: local_multimodal_instruct_baseline
backend: vllm (local offline OpenAI-compatible endpoint)
multimodal: true
context_tokens: 131072     max_input_tokens: 65536     max_output_tokens: 32000
temperature: role-scoped (solver 0.7, coder 0.5, explorer 0.9)
seed: fixed per profile
```

Model swaps are profile + Deployment Manifest changes only. No `if model_family == ...` branch may exist anywhere.

### 2.5 Config Tests

Required:

- default construction satisfies every bound in §2.1 (invariant test);
- alias resolution maps every documented alias to its canonical field; unknown keys are ignored with a warning;
- `update_runtime` never applies underscore keys and never wipes a live field with `None`;
- `to_dict` excludes private fields; `set_deadline` ignores non-positive values;
- `resolve` returns dataclass defaults for unset keys and never resurrects call-site literals;
- backend `fake` requires no network and no model files; the full suite passes under it;
- no config field name contains a model, vendor, engine, or cluster identifier (guardian-checked);
- `enable_primitive_probing` default is identical in the dataclass and in env resolution (single agent surface).

---

## 3. Core Data Types (`types.py`)

```text
Grid2D = list[list[int]]                        palette ids 0..15

BoundingBox:  min_row, min_col, max_row, max_col          (frozen; to_dict)
Centroid:     row: float, col: float                      (frozen)

CoordinateCandidate:
  candidate_id: str
  x: int, y: int                              local space
  source_type: str                            centroid | mask_pixel | relation | region
  object_id: str | None
  crop_offset: int                            dual-space metadata (ISO-12)

ActionDeclaration:
  action_id: str
  params: dict
  declared_effect: str

EffectDeclaration:
  action_id: str
  effect_summary: str
  displacement: tuple[int, int] | None
  confidence: float

AtomicProposition:                (frozen)
  family: str                     object_identity | attribute_delta | metric_sign |
                                  relation_existence | terminal_metadata |
                                  spatial_position | area_conservation | kinematic
  subject_id: str | None
  secondary_id: str | None
  predicate: str                  preserved | destroyed | vanished | missing | moved |
                                  step_moved | unchanged | stationary | row_delta |
                                  col_delta | win | game_over | ...
  value: Any | None

PropositionSet:                   (frozen, sized, iterable; empty() constructor; to_list())

SolverInput / CoderInput:         (frozen role-input bundles)
```

Rules: propositions are the only vocabulary exchanged between planner, binder, and verifier; new families require a version increment of this document; `AtomicProposition` is hashable and comparable by value.

---

## 4. Brusentsov Logic Engine (`brusentsov_logic.py`)

### 4.1 Enums and Bridge

```python
class Ternary(Enum):
    TRUE = 1          # FOLLOW: necessary containment held (xy)
    FALSE = -1        # NULL: hard physical contradiction (xy'_0)
    IRRELEVANT = 0    # OMIT: inessential / passive outcome (x'y or x'y')

class EpistemicSignal(Enum):
    SEEK_EVIDENCE = 1  # controller signal, not a truth value

class Verdict(Enum):
    FOLLOW, NULL, OMIT, UNDECIDED
    # .ternary property: FOLLOW->TRUE, NULL->FALSE, OMIT->IRRELEVANT, UNDECIDED->None
    # Verdict.from_ternary is total on Ternary and raises on anything else
    # cross-type equality is defined only along the bridge above; hashing preserved
```

Canonical aliases and aggregation (`Modified_Brusentsov_Entailment_Logic.md` §4): `FOLLOW` ≡ REQUIRED (+1), `NULL` ≡ FORBIDDEN (−1), `OMIT` ≡ IRRELEVANT (0), `UNDECIDED` ≡ UNRESOLVED (U) with `.ternary → None` — the code-level form of the canonical separation of the ontological triad from the epistemic control signal (canonical §1.3). Clause aggregation follows the dominance chain NULL ≻ UNDECIDED ≻ OMIT ≻ FOLLOW (canonical §4.2, Theorem 4.1). `OMIT` subtypes (canonical §5.2): BLOCKED (Tier 3 soft stop), REDUNDANT (`NoopRepeatGuard`), INCIDENTAL (Tier 8 retention).

### 4.2 `BrusentsovJudgment` (schema `v10.judgment.1`)

```text
trajectory_id: str
step_id: str
verdict: Verdict | Ternary
expected_propositions: PropositionSet
observed_propositions: PropositionSet
explanation: str                      deterministic, reason-coded
is_effective: bool
timestamp: float
ambiguity_score: float | None
evidence_hint: str | None
matching_candidates: list[str]
track_confidence_min: float | None
action_dict: dict                     dual-space action metadata
```

Frozen, serializable (`to_dict`), append-only in storage. Judgments are the sole truth record of transitions; nothing downstream may re-derive verdicts from raw frames.

### 4.3 `implies_brusentsov` Contract

```python
def implies_brusentsov(expected: PropositionSet, observed: PropositionSet,
                        neutral: NeutralRegionRegistry = EMPTY_REGISTRY) -> Ternary
```

Evaluation order is normative:

1. `len(expected) == 0` → `IRRELEVANT` (vacuous truth elimination, unconditional);
2. incompatibility scan: any `contradicts(e, o)` pair → `FALSE`; object-identity destruction check included;
3. necessary containment: all expected propositions contained in observed → `TRUE`;
4. otherwise, for a **resolved** discrepancy: → `FALSE` when the observed change lies outside the expected set, is non-zero, and is not inside a contract-declared bounded neutral region `Ω_sub` (canonical Definition 3.1, clause 5: a resolved out-of-contract active change is certified incompatibility, not inessentiality; `Ω_sub = ∅` by default and must be declared per contract); → `IRRELEVANT` when the change lies inside a declared `Ω_sub` (sub-threshold neutrality, canonical §3.1). **Unresolved** observations (below the tracking resolution floor, ambiguous matching) are never decided here: the cascade maps them to `UNDECIDED` (Tiers 4/7). Expectation-free and passive cases remain inessential by rule 1 (empty expectations → `IRRELEVANT`, canonical Axiom 4.1); distinct subjects never contradict (§4.4 item 0).

**Neutral-region registry (`Ω_sub`).** Rule 4 consumes an explicit registry of contract-declared neutral regions: mappings from (subject family, predicate family) to bounded sets/bands of resolved non-zero deviations admitted as sub-threshold-neutral. Sources: the `declared_neutral_regions` config field and per-`EXPECT` tolerance declarations bound by the VerificationBinder into the contract hash. The registry is **empty by default**; adding or changing a region is a contract change (contract-hash update) and is never inferred at runtime from observed deltas. Only rule 4 consumes the registry; `contradicts()` (§4.4) is unaffected — a declared neutral region never legalizes a §4.4 contradiction class.

### 4.4 `contradicts` Completeness Requirements

```python
def contradicts(expected: AtomicProposition, observed: AtomicProposition) -> bool
```

Must implement, exhaustively and in this order:

0. subject matching — distinct explicit subjects can never contradict;
1. object identity — `preserved` vs `destroyed/vanished/missing` (both directions);
2. attribute delta — same subject+predicate, normalized values differ;
3. kinematics — tuple forms (`moved`, `step_moved`): stagnation, unintended mutation, direction inversion per axis;
4. invariant violation — expected `unchanged/stationary` vs observed motion (tuple or scalar forms);
5. metric-sign contradictions — `row_delta/dy` and `col_delta/dx` families: expected≠0/observed=0, expected=0/observed≠0, sign inversion;
6. cross-format checks — tuple-expected vs scalar-observed and scalar-expected vs tuple-observed, symmetric normalization;
7. relation existence — same subject+secondary+predicate, boolean values differ;
8. terminal metadata — expected `win` vs observed `game_over/lost`;
9. spatial position and area conservation — same subject, values differ.

Regular expressions are forbidden in this module; value normalization is tokenizer-based.

### 4.5 Vacuity Guards

- `evaluate_invariant_across_levels` returns `IRRELEVANT` for kinematic rules evaluated without an executed action (`act_id` empty) on $`S_0`$;
- no code path may convert `IRRELEVANT` into `TRUE`.

### 4.6 Tests

- PBT (`test_pbt_brusentsov_axioms.py`): empty expectations never yield TRUE; preserved-vs-destroyed always contradicts; exact containment always yields TRUE; unasserted changes never yield TRUE; cross-type equality/hash bridge laws; resolved out-of-contract change (non-zero, outside any declared neutral region) yields FALSE; declared `Ω_sub` member yields IRRELEVANT;
- PBT (`test_pbt_brusentsov_severance.py`): stagnation, unintended mutation, direction inversion, containment consistency, macro-step decomposition, early severance;
- PBT (`test_pbt_undecided_exhaustion.py`, new in 10.9): probe-queue exhaustion and `max_undecided_streak` exhaustion retain the judgment verdict permanently as `UNDECIDED`; `ABORT_ON_UNDECIDED` is logged with the exhaustion reason code; no `NEGATIVE_BARRIER` invariant or branch signature is grounded from the retained record; exactly one clean `RESET` is scheduled;
- unit: every contradiction class of §4.4 has positive and negative cases in every supported kinematic format; subject mismatch never contradicts; vacuity guard on $`S_0`$.

---

## 5. Judge Cascade (`judge.py`, `LayeredVerifier`)

### 5.1 Interface

```python
class LayeredVerifier:
    def __init__(self, config: V10Config): ...
    def reset(self) -> None: ...
    def match_objects_between_snapshots(self, prev, cur) -> dict: ...
    def extract_observed_propositions(self, step, prev, cur, diff, transient) -> PropositionSet: ...
    def evaluate_transition(self, step, prev_snapshot, cur_snapshot, *,
                            frame_diff=None, transient_evidence=None,
                            game_memory=None, transition_table=None,
                            action_dict=None) -> BrusentsovJudgment: ...
```

`evaluate_transition` implements the 8-tier cascade of Architectural Specification §4.1 in exactly that order. Tier order is frozen; adding evidence channels (FrameDiff, transient, TransitionTable) may enrich tier inputs but must never reorder or bypass tiers.

### 5.2 Required Tier Behaviors

- Tier 1/2: terminal signals dominate all other evidence;
- Tier 3: zero delta on confirmed motion → boundary/obstacle contact check (`is_blocked_by_boundary`, memory wall rules) → soft-stop `OMIT`; transient evidence present → effective-action override; else → `NULL`;
- Tier 4: grounded-step `confidence == "low"` or `matching_status == "ambiguous"`; JV match gap < `matching_ambiguity_threshold`; min participating track confidence < `track_confidence_threshold` → `UNDECIDED`;
- Tier 5/6: `implies_brusentsov` FALSE → `NULL`; TRUE → `FOLLOW`;
- Tier 7: zero delta on unconfirmed action with non-empty EXPECT; sub-`min_reliable_delta` displacement with non-empty EXPECT and no terminal → `UNDECIDED` (sub-`min_reliable_delta` means $`\delta_{obs}`$ is below the tracking resolution floor — undefined, hence epistemically unresolved per canonical §3.1/§6.1, not sub-threshold-neutral; a contract-declared neutral region `Ω_sub` would instead map resolved members to `OMIT`);
- Tier 8: certified effect + verified non-empty EXPECT → `FOLLOW`; certified effect + empty/unverified EXPECT → `OMIT`; default → `OMIT` (ISO-10; resolved cases only — unresolved cases are intercepted by Tiers 4/7 as `UNDECIDED`, canonical §4.3 Step 6).

With `enable_undecided_verdict = False`, Tiers 4 and 7 map to `OMIT` (ablation mode).

### 5.3 Observed Proposition Extraction

Extraction consumes FrameDiff typed deltas and transient evidence — never raw pixel diffs:

- `moved/rotated/resized/color_changed/appeared/disappeared` map to kinematic, attribute, and identity propositions with tracked subject IDs;
- transient geometry maps to effectiveness propositions with `evidence_hint = transient:<class>`;
- extraction is deterministic and unit-tested per delta type.

### 5.4 Tests

- cascade order: constructed transitions that would yield different verdicts under permuted tier order must fail the frozen-order test;
- each tier has isolated positive/negative fixtures;
- soft stop vs stagnation discrimination (boundary contact present/absent);
- transient override: zero static delta + transient cells ⇒ effective, never `IDLE_SELF_LOOP` in the TransitionTable write;
- vacuous FOLLOW elimination: non-zero delta + empty EXPECT ⇒ `OMIT`;
- UNDECIDED ablation mapping;
- HUD tick transitions produce no delta propositions and stable `interior_grid_hash` verdicts.

---

## 6. Perception Contracts

### 6.1 Observation Normalization (`observe.py`)

```python
def collapse_frame_axes(grid) -> Grid2D
def crop_grid_border(grid, border=1) -> tuple[Grid2D, int]      # (cropped, crop_offset)
def normalize_observation(raw, crop_border) -> dict              # grid, hashes, state, metadata
def compute_grid_hash(grid) -> str                               # deterministic row-encoded
def grid_to_hex_rows(grid) -> list[str]
def normalize_state_name(state) -> str
def normalize_action_name(action) -> str
```

Both `grid_hash` (full) and `interior_grid_hash` (HUD-isolated) must be produced; consumers declare which they use.

### 6.2 ARGA-Lite (`arga_lite.py`)

```text
PlanningObject:
  id, alias, color, pixels, bounding_box, centroid, area,
  shape_signature, shape_signature_stable, is_single_color,
  functional_role (evidence-tagged hypothesis), enclosed_by, uncertainty

SpatialRelation:
  relation_id, relation_type, subject_id, object_id, metrics, confidence

ARGALiteSnapshot:
  snapshot_id, grid_dims, background_color, objects, relations, cavities, grid_hash
```

Pipeline: background detection → component segmentation → shape properties → cavity detection → collinear axis merging → substantive filtering (`area >= min_substantive_area`, ISO-6) → relation extraction → enclosure detection → functional role annotation. All stages dimension-invariant ($2\times2..64\times64$) and palette-permutation-invariant (PBT-enforced).

### 6.3 PersistentObjectTracker (`tracker.py`)

Cost and acceptance per Architectural Specification §5.3. Contract:

- matches accepted iff `cost < track_match_threshold`; deterministic tie-break by lexicographic `persistent_id`;
- track state: confidence, velocity EMA, shape-stability decay, cumulative window, occlusion flag, age; tracks retire after `track_max_age` unmatched frames;
- ambiguity signal emitted when best-vs-second gap < `matching_ambiguity_threshold`;
- tracker output is the identity authority for FrameDiff and the judge; object IDs in propositions are persistent track IDs.

### 6.4 FrameDiff (`frame_diff.py`)

```python
def match_frames(prev_objects, cur_objects, grid_dims, config) -> FrameDiffResult

FrameDiffResult:
  matches: list[(track_id, object_id, cost)]
  deltas:  list[SemanticDelta]        # subject_id, delta_type, evidence
  appeared / disappeared: list[object_id]
  ambiguity: float | None             # best-vs-second gap of the assignment
```

Assignment is solved optimally (Jonker–Volgenant) over the normalized cost (spatial distance, area similarity, color congruence). `delta_type` vocabulary is closed: `moved | rotated | resized | color_changed | appeared | disappeared`. Unmatched residue must surface as `appeared`/`disappeared`, never be dropped.

### 6.5 Transient Cells Engine (`animation_analysis.py`)

```python
def extract_transient_cells(chain: Sequence[Grid2D], *,
                            ignore_peripheral_hud: bool = True) -> TransientEvidence

TransientEvidence:
  transient_cells: list[tuple[int, int]]     # mutation count >= transient_min_mutations
  geometry: beam | sweep | pulse | none
  direction: tuple[int, int] | None
  micro_frame_count: int
  hud_excluded_cells: list[tuple[int, int]]
```

Consumed by judge Tier 3 override and by TransitionTable annotation. When no micro-frame chain is available, the engine returns `geometry = none, micro_frame_count <= 1` and the static path proceeds.

### 6.6 PlanningSet (`planning_set.py`)

```text
PlanningSet:
  snapshot_id, grid_hash, full_grid_hex_rows, grid_dims, crop_offset
  object_ids, objects, object_real_to_alias, object_alias_to_real
  relation_ids, relations
  allowed_action_ids, allowed_coordinate_candidate_ids, coordinate_candidates
```

Immutable after assembly (ISO-4). `build_planning_set(snapshot, available_actions, crop_offset)` filters forbidden IDs (`ACTION7`), assigns deterministic aliases, and derives coordinate candidates with dual-space metadata.

### 6.7 DualView Rendering (`frame_media.py`)

```python
def render_grid_png(grid) -> bytes
def render_annotated_frame_png(grid, planning_set) -> bytes
```

Synchronized pairs; annotation vocabulary fixed (boxes, alias labels, centroids). Prompts must carry the over-segmentation caveat and the raw-pixels-first authority order.

### 6.8 Tests

- normalization: crop invariance, hash determinism, interior vs full hash divergence under simulated HUD ticks;
- ARGA-Lite: PBT scale invariance, PBT color permutation, cavity and collinear-merge fixtures, substantive filtering;
- tracker: cost monotonicity, tie-break determinism, ambiguity emission, occlusion and aging;
- frame_diff: optimality against brute-force assignment on small fixtures; closed delta vocabulary; residue handling;
- transient engine: beam/sweep/pulse classification fixtures; HUD exclusion; mutation-count threshold; zero static delta + transient ⇒ effective;
- planning set: immutability, alias determinism, forbidden-ID filtering, coordinate dual-space metadata;
- dual view: raw/annotated synchronization, coordinate notation consistency (PBT orthogonal-modality suite).

---

## 7. TransitionTable (`transition_table.py`)

### 7.1 `TransitionRecord` (schema `v10.transition_record.1`)

```text
step_index: int
level_id: str
pre_grid_hash: str            interior_pre_hash: str
action_id: str
coords: tuple[int, int] | None          # local space
coords_engine: tuple[int, int] | None   # engine space (ISO-12)
action_source: probe | executor | evidence | fallback | reset
post_grid_hash: str           interior_post_hash: str
delta_cells: int
moved_object_ids: list[str]
transient_cells_present: bool
transient_geometry: beam | sweep | pulse | none
micro_frame_count: int
outcome_class: EFFECTIVE | IDLE_SELF_LOOP | LOSS | WIN | UNKNOWN_PENDING
verdict: Verdict | None
observed_effect: str
```

### 7.2 Interface

```python
class TransitionTable:
    def record(self, rec: TransitionRecord) -> None            # trace append; quotient upsert
    def is_known_idle_self_loop(self, interior_hash, action_id, coords=None) -> bool
    def is_known_death_edge(self, interior_hash, action_id, coords=None) -> bool
    def get_edge(self, interior_hash, action_key) -> TransitionRecord | None
    def edges_for_state(self, interior_hash) -> list[TransitionRecord]
    def tested_action_keys(self) -> set[tuple]                 # both coordinate spaces decoded
    def export_trace(self) -> list[dict]                       # replay backbone
    def clear_quotient_for_new_level(self, level_id) -> None   # trace archived, quotient reset
```

`UNKNOWN_PENDING` records never populate the Quotient. The Quotient key canonicalizes `ACTION6` coordinates into local space before indexing.

### 7.3 Tests

- trace append-only; quotient idempotence on duplicate observation;
- `IDLE_SELF_LOOP` vs `IDLE_UNLINKED` discrimination (absence of record is never idle evidence);
- dual-space key canonicalization: the same physical coordinate probed via engine encoding deduplicates;
- transient-annotated zero-delta records classify as `EFFECTIVE`;
- level transition archives trace and clears quotient; game transition rebuilds;
- no LLM-derived write path exists (guardian + unit).

---

## 8. Memory Contours (`memory_contours.py`)

### 8.1 PaletteRoleMap

```text
EntityRole: background | actor | obstacle | hazard | target | collectible | portal | unknown

ColorAffordance:
  color_id: 0..15
  role: EntityRole
  is_dynamic: bool
  pixel_count: int
  interaction_count: int
  confidence: float
  evidence: list[str]

PaletteRoleMap:
  colors: list[ColorAffordance]           # exactly 16, always present
  assign_role(color_id, role, confidence, evidence)   # higher confidence supersedes; UNKNOWN always superseded
  get_role_label(color_id) -> "Color N (ROLE)"
  generalize_color_reference(text) -> str             # non-destructive (ISO-8)
```

### 8.2 Agent Contours

```text
EnvironmentSpecMemory:
  specs: list[dict]                       # v10.env_spec.1 records
  probe_records: list[ProbeRecord]
  affordances / displacements / invariants indices
  record_spec(spec); synchronize_action_surface(confirmed_effect)

ProbeRecord:
  action_id, action_data (dual-space), pre/post hash, delta summary,
  effect_class: EffectClass, status, transient annotation

SyntaxErrorRecord / SyntaxErrorMemory:
  bounded (syntax_error_memory_max_entries), most-recent-first;
  error class, message, offending fragment (sanitized), repair hint;
  never readable from Solver-facing code paths (ISO-1, test-enforced)

EpistemicMemory:
  attempt_feedback: list                  # bounded (epistemic_memory_max_entries)
  severed_branch_signatures: set
  failed_completed_trajectories: set
  epistemic_signals: list                 # UNDECIDED storage, segregated (ISO-9)
  record_attempt_feedback(...); sever_branch(sig); record_failed_completed_trajectory(sig)
  failed_attempts_scratchpad() -> str     # deterministic render for Solver prompts

GameMemory:
  game_id
  confirmed_action_effects: dict[str, str]
  unconfirmed_actions: dict[str, str]
  selection_mechanics / reusable_primitives / invariant_rules (tiered 1-3)
  level_solution_patterns / completed_levels
  structured_invariants: list[StructuredInvariant]
  confirmed_actor_ids: set[str]
  palette: PaletteRoleMap
  last_defeat_exemplar / last_victory_exemplar_v2
  grounded_invariants: list[GroundedInvariant]
  curriculum_history: list                # CurriculumProgressionBuffer
  working_hypotheses: list                # WorkingRolloutMemory handle
```

### 8.3 Exemplars and Invariants

```text
DefeatExemplar (schema v10.defeat_exemplar.2):
  level_index, fatal_step, fatal_action_id, fatal_coords (dual-space)
  actor_position_before, hazard_color
  fatal_step_diff: dict                   # strictly F_alive vs F_fatal
  fatal_transient_trajectory: str
  fatal_frame_observed: bool              # honesty flag (§Arch 8.7)
  valid_prefix_actions: list[str]
  environment_signal: str                 # GAME_OVER
  explanation, timestamp
  format_for_prompt() -> str              # compact deterministic lesson block

VictoryExemplar:
  level_index, total_steps, action_sequence, key_transitions,
  final_action_id, target_color, final_subgrid, winning_invariants_used,
  explanation, timestamp
  format_for_prompt() -> str

GroundedInvariant:
  invariant_id, antecedent, consequent
  brusentsov_type: NEGATIVE_BARRIER | POSITIVE_CANON
  scope: CORE_GAME_LAW | LEVEL_SPECIFIC
  grounded_in_defeat / grounded_in_victory
  times_confirmed, times_falsified, confidence, created_on_level
  is_active() == (times_falsified == 0)

CoreInvariantRegistry:
  register / confirm / falsify / active_set(scope)
  falsification is recorded with the contradicting observation, never silent
```

### 8.4 `MemoryContourManager`

Mediates all contour access; enforces ISO-1..ISO-12 at the API boundary (`IsolationViolationError` on violation); performs level-transition sanitization of level-transient content and game-transition reset of game-scoped state; guarantees deterministic eviction on bounded stores.

### 8.5 Tests

- isolation: traceback strings never render into Solver-facing prompts; goal/score/win-condition strings never render into Coder-facing prompts or env specs (ISO-1/ISO-2, `test_prompt_isolation.py`, `test_isolation_invariants.py`);
- role assignment: confidence supersession, UNKNOWN override, permutation invariance (PBT color suite);
- exemplars: field capture from simulated GAME_OVER/victory; prompt-format determinism; safe-prefix correctness;
- invariant lifecycle: single $`S_0`$ contradiction retires permanently; kinematic vacuity on pristine frames;
- bounded stores: eviction order determinism; budget caps respected;
- level-transition sanitization and game-transition reset (`test_stage2_*`, `test_stage3_*` suites);
- double-loop routing: syntax failures reach only Coder repair; physical failures reach only Solver scratchpad (`test_double_loop.py`).

---

## 9. Agent Contracts

### 9.1 Explorer (`explorer_agent.py`)

```python
class ExplorerAgent:
    def generate_environment_spec(...) -> dict          # schema v10.env_spec.1
    def synthesize_level_spec(...) -> dict
    def research_unconfirmed_primitives(...) -> list
    def propose_coordinate_probes(planning_set, memory, crop_offset) -> list

class PrimitiveProbeManager:
    def plan_discrete_probes(planning_set, memory, max_probes, known_actions) -> list
    def handle_level_transition(confirmed_action_effects=None) -> None
    def get_dynamic_reprobes(...) -> list
    def is_action_effective(effect_summary) -> bool
```

`v10.env_spec.1` required fields:

```text
schema_version, snapshot_hash, planning_set_id
available_actions: list[str]
researched_actions: [{action_id, effect_class, status, displacement, contradicted}]
action_affordances / coordinate_affordances (dual-space, source-typed)
action_displacements
object_class_notes / action_surface_notes / invariants
```

Contract: two-tier lifecycle classification (`EffectClass`: confirmed effective vs `CONDITIONAL_TRIGGER` with `status: unconfirmed_on_s0`); coordinate probes target mask pixels; tested coordinates are deduplicated through the TransitionTable in both spaces; probe emissions carry `action_source = probe`.

### 9.2 Coder (`dsl_coder.py`)

```python
def parse_dsl_manifest(source) -> dict                  # schema v10.dsl_manifest.1
def extract_code_and_manifest(text) -> tuple[str|None, dict|None]

class DSLCoder:
    def generate_dsl(env_spec, game_memory, planning_set, images=None) -> tuple[module, manifest]
```

`v10.dsl_manifest.1`:

```text
schema_version
functions: [{name, parameters: [{name, type, default}], returns,
             docstring, purity: pure_declaration, expected_effect_template,
             action_id (when the wrapper declares an environment action)}]
```

Contract: response sanitization → extraction → AST validation → sandbox dry-run → manifest consistency → auto-augmentation of missing confirmed actions (canonical `api.declare_environment_action` wrappers) → re-certification of augmented output. Failure routes to `SyntaxErrorMemory` and bounded repair retries (`max_coder_retries_per_level`).

### 9.3 Solver (`solver_agent.py`)

```python
def parse_expect_grammar_str(exp_str, planning_set=None) -> list[dict]
def parse_text_trajectory(text, ...) -> dict | None      # schema v10.trajectory_package.1

class SolverAgent:
    def generate_trajectory_package(manifest, planning_set, epistemic_memory=None,
                                    budget=50, image_png=None, game_memory=None,
                                    attempts_remaining=None, max_attempts=None,
                                    probes_remaining=None, max_probes=None,
                                    env_spec=None) -> dict | None
    def reflect(...) -> dict                             # invariant distillation turn
```

`v10.trajectory_package.1`:

```text
schema_version, proposal_id, hypothesis
candidates: [{trajectory_id, steps: [{step_id, dsl_function, arguments,
              expect (grammar string), abort_if}], success_condition, confidence}]
invariant_evolution / analysis (reflection turn)
```

`EXPECT` grammar (typed, tokenizer-parsed; regex parsing of coordinates/semantics forbidden):

```text
moved(ALIAS, dy, dx) | moved(ALIAS, dy<0, dx>0)        # relational signs allowed
step_moved(ALIAS, sgn_dy, sgn_dx)
unchanged(ALIAS) | preserved(ALIAS) | stationary(ALIAS)
destroyed(ALIAS) | color_changed(ALIAS, c)
contact(ALIAS_A, ALIAS_B) | win() | ...
```

Macro form: `dsl_function(count=N)` with cumulative `moved(...)` and per-step `step_moved(...)` semantics per Architectural Specification §8.2.

Contract: packages are capped by `max_candidates_per_solver_package`; every step carries EXPECT or is explicitly expectation-free (which yields OMIT, never FOLLOW); the failed-attempts scratchpad (grid diffs + diagnostics) is mandatory input on replans; reflection output categories are fixed (`[PALETTE & ROLES] [GOAL] [ENTITIES] [CONTROL] [PHYSICS]`).

### 9.4 Prompt Builders (`prompt_builders/`)

Per call family, the section inventory and order are fixed:

```text
system role constraints (family-specific prohibitions)
environment evidence (env spec facts / confirmed physics)     [Explorer, Coder]
DualView frames + over-segmentation caveat + coordinate conventions
memory context (role-appropriate stores only)
active planning surface (manifest for Solver; PlanningSet digest)
failed-attempt diagnostics + do-not-repeat instructions       [Solver]
output schema + strict-format instruction                     (tail, always last)
```

Tail-priority rule: schema and format instructions are the final prompt sections and survive every compaction step (Architectural Specification §11.6). Isolation: builders read only their family's contours; the manager raises on cross-contour access.

### 9.5 LLM Advisor (`llm_advisor.py`)

```python
class BaseLLMAdvisor:
    def generate_chat(self, messages, *, role, config, images=None) -> str
    def generate(self, prompt, *, role, config) -> str

def build_llm_advisor(config) -> BaseLLMAdvisor     # factory over §2.4 backends
def sanitize_model_response(raw_text) -> str        # fence stripping, control-char removal
def format_multimodal_message(...)                  # canonical image payload format
def is_role_vision_enabled(config, role) -> bool
```

Contract:

- backends: `vllm` (local offline, normative), `openai_chat`, `openai_responses` (development only), `fake` (tests). Vendor labels resolve to generic backends via the alias table; selection logic lives in the factory alone;
- every call: deadline check (abort with `"{}"` on reserve breach), timeout clamping `min(base_timeout, max(2.0, remaining - reserve))`, role-scoped decoding parameters from the profile;
- every call is recorded per Architectural Specification §14.3 (prompt hash, payload, response hash, parsed result, validation status, usage);
- `MockLLMAdvisor` (`fake`) supports scripted per-role responses and must satisfy all three family schemas so the full suite runs offline;
- no backend may retry silently: retries are explicit, bounded, and recorded.

### 9.6 Tests

- Explorer: env-spec schema conformance; two-tier classification; mask-pixel targeting; dedup across coordinate spaces; probe budget enforcement (`test_explorer_agent.py`, `test_primitive_probing_and_detection.py`, `test_coordinate_and_probe_partitioning.py`, `test_two_tier_memory_and_probes.py`);
- Coder: extraction from messy responses; AST rejection cases; auto-augmentation completeness; dry-run failure routing to SyntaxErrorMemory (`test_dsl_coder.py`, `test_sandbox.py`);
- Solver: package parsing (XML and markdown forms); EXPECT grammar matrix including relational signs; macro decomposition; scratchpad rendering determinism; reflection category conformance (`test_solver_agent.py`, `test_failed_attempts_differential_scratchpad.py`, `test_solver_two_turn_reflection.py`);
- isolation: ISO-1/ISO-2 prompt-content tests (`test_prompt_isolation.py`);
- advisor: fake-backend schema sufficiency; timeout clamping; deadline abort; recording completeness (`test_qwen_thinking_and_smoke.py` renamed to backend-neutral `test_llm_advisor_contract.py`).

---

## 10. Verification and Execution

### 10.1 VerificationBinder (`verification.py`)

```python
class VerificationBinder:
    def ground_step(self, step_dict, planning_set) -> GroundedStep   # raises GroundingError

GroundedStep:
  step_id, dsl_function, arguments (grounded), expected_propositions,
  abort_if, confidence, matching_status
```

Grounding rules: function ∈ certified manifest; object refs ∈ PlanningSet IDs/aliases; coordinates ∈ allowed candidates or in-bounds local; invented references raise, never coerce.

### 10.2 Verifier Packet (`verifier_packet.py`)

`build_verifier_packet(planning_set, metadata)` → schema `v10.verifier_packet.1`: snapshot identity, grid hashes, hex rows, object catalog (with aliases), relations, coordinate affordances, action surface. Deterministic serialization; used for offline verification exchange and replay.

### 10.3 SymbolicTrajectoryExecutor (`symbolic_executor.py`)

```python
class SymbolicTrajectoryExecutor:
    def next_grounded_step(self, pool, planning_set, transition_table) -> EmissionStep | None
    def on_judgment(self, judgment, pool, memory) -> RouteDecision
```

Contract:

- pre-execution idle guard: `transition_table.is_known_idle_self_loop(...)` blocks step 0 and severs with reason `known_idle_edge`;
- macro unrolling via substep decomposition: invariants distributed to every substep; `step_moved` per transition; cumulative `moved` on the final substep; `break_on_null`-style silent skips are forbidden;
- verdict routing: `FOLLOW/OMIT` → advance (OMIT recorded as inessential); `NULL` → `sever()`, branch signatures to EpistemicMemory, structured diagnostic via `_build_step_contradiction_diagnostic()`, single clean `RESET` scheduled; `UNDECIDED` → hand off to the evidence FSM; on probe exhaustion the FSM terminates the attempt with the verdict permanently retained as `UNDECIDED` (`ABORT_ON_UNDECIDED`; Arch. Spec §4.3, canonical §5.4) — never rewritten to `NULL`;
- exactly one environment action per emitted step (`execute_one_step_at_a_time`);
- diagnostics are deterministic renders of judgment records (no raw model text).

### 10.4 Trajectory Pool API (`trajectory.py`)

```python
class CandidateTrajectory:
    def current_step(self) -> dict | None
    def advance(self) -> None
    def sever(self) -> None                 # no arguments; idempotent
    def is_severed(self) / is_finished(self) -> bool

class TrajectoryPool:
    @classmethod from_package(cls, package) -> TrajectoryPool
    def peek_active_candidate(self) -> CandidateTrajectory | None    # NO mutation
    def advance_to_next_candidate(self) -> CandidateTrajectory | None
```

`TrajectoryPool` has no `sever` method; call sites must not invent one. Inspection uses `peek_*`; progression is explicit.

### 10.5 ActionGuards (`action_guards.py`)

```python
class NoopRepeatGuard:
    def check(self, action, prev_action, prev_record) -> GuardDecision
class DeathActionGuard:
    def observe_loss(self, record) -> None
    def check(self, action, interior_hash, table) -> GuardDecision
def compute_interior_grid_hash(grid, hud_mask) -> str
class BudgetGuard:
    def check(self, budgets, deadline_state) -> GuardDecision

GuardDecision: allow | block(reason_code)
```

Guards run after arbitration, before dispatch; a block re-arbitrates (never fabricates an alternative action); every decision is logged with reason codes. Guards never falsify action laws (ISO-11 boundary).

### 10.6 Tests

- binder: grounding matrix (valid/alias/coordinate/invented); GroundingError routing (`test_symbolic_spec_and_action_gating.py`);
- executor: unrolling correctness (invariant distribution, per-step signs, cumulative final); severance side effects (signatures, diagnostic, single reset); idle-guard interdiction without environment action (`test_symbolic_executor.py`);
- pool API: peek non-mutation; advance semantics; sever idempotence;
- guards: noop-repeat block after zero-delta; transient-annotated zero-delta does NOT arm the noop guard; death-edge cache blocks re-emission; budget guard at boundaries; interior hash stability under HUD ticks (`test_action_guards.py`, `test_audit_fixes.py`);
- end-to-end: grounded package → emission → verdict → memory write chain (`test_v10_end_to_end.py`).

---

## 11. Session Orchestrator (`session.py`)

### 11.1 Interface

```python
class GameSession:
    def act(self, raw_observation) -> dict          # exactly one action per call
    def observe_action_result(self, after_observation=None) -> bool
    def handle_level_transition(self, new_level_id) -> None
    def handle_game_transition(self, new_game_id) -> None
    def update_runtime_config(self, updates) -> None
    def harness_telemetry(self) -> dict
    invariant_registry: property                    # live resolution, never cached
```

`SessionPhase` and `PhaseTransition` per Architectural Specification §10.1; illegal transitions raise; every transition logs `(from, to, reason)`.

### 11.2 Arbitration and Scheduler

`act()` implements the normative arbitration order (Architectural Specification §10.2) through `PriorityScheduler.arbitrate(...)`; the session must not contain ad-hoc source selection outside the scheduler. Degradation under budget/deadline pressure follows the fixed order and is logged per step.

### 11.3 Triangulated Defeat Sequence

On `state == "GAME_OVER"`:

1. retrieve $`F_{alive}`$ (normalized pre-action state) and, when exposed, $`F_{fatal}`$ (collision frame from the micro-frame chain or pre-reset observation);
2. compute `fatal_step_diff` strictly between $`F_{alive}`$ and $`F_{fatal}`$; set `fatal_frame_observed` honestly;
3. sever only the defeated candidate; capture `valid_prefix_actions`;
4. emit exactly one `RESET` (`last_engine_action_source` tracked to prevent double-reset);
5. construct `DefeatExemplar`; ground/reinforce `NEGATIVE_BARRIER`;
6. resume pool traversal from $`S_0`$ or replan with the preserved safe prefix.

### 11.4 Transition Handlers

- `handle_level_transition`: archive TransitionTable quotient; clear level-local probe records; sanitize level-transient memory; `probing_phase = True`; defer cross-level invariant re-evaluation to the pristine frame (`level_initial_grid is None`);
- `handle_game_transition`: `_reset_game_scoped_state()` (observed completed-level counters, evidence-probe budgets, undecided streaks); rebuild game memory when configured;
- selection-indicator discovery during probes enqueues targeted directional probes before resetting to $`S_0`$.

### 11.5 Reactive Invalidation

`_check_and_invalidate_dsl_for_new_action(action_id, effect_desc)`: for observable moves absent from the active manifest → invalidate module/manifest, unblock Coder retries, set `replan_requested`, synchronize env-spec action surface. Meta actions (`RESET`, forbidden IDs) are excluded via `action_semantics`.

### 11.6 Orchestration Invariants (post-audit, test-enforced)

1. deadline integrity: private fields never serialize; merges never wipe an armed deadline;
2. game-scoped reset completeness (§11.4);
3. live invariant-registry property (no stale aliases after memory rebuild);
4. trajectory pool API discipline (§10.4);
5. alias-resolved config access only (`resolve`, `update_runtime`);
6. action vocabulary SoT: all vector/legal/forbidden/displacement logic imported from `action_semantics.py` — local tables are a guardian finding.

### 11.7 Tests

- phase machine: legal/illegal transition matrix;
- arbitration: source-priority fixtures for each §10.2 slot; single-emission invariant; non-emitting synthesis does not consume budget;
- defeat: triangulation with and without $`F_{fatal}`$ (honesty flag); single-RESET; safe-prefix preservation; exemplar field capture (`test_triangulated_defeat.py`);
- budget exhaustion: `LevelAttemptsExhaustedError` at `max_actions_per_level` with no `RESET` emitted (integration);
- harness lifecycle: config merge after `set_deadline`, game_id transition, levels_completed observation, GAME_OVER with live pool (`test_harness_lifecycle.py`, `test_session_lifecycle.py`);
- invalidation: newly confirmed action → module drop → replan flag → env-spec sync (`test_reactive_dsl_invalidation.py`).

---

## 12. Fallback Engine

### 12.1 `SymbolicFallbackEngine` (`fallback_symbolic.py`)

```python
class SymbolicFallbackEngine:
    def select_fallback_action(self, planning_set, game_memory, transition_table) -> dict | None
    def clear_cycle_memory(self) -> None
```

Contract: engages only on proposer exhaustion; one continuous run per level engagement; `RESET` emission forbidden; cycle or GAME_OVER during fallback abandons the level cleanly; emissions pass guards and the full verifier cascade; tabu state is level-scoped and logged.

### 12.2 State-Aware Actor/Target Selection

- actor: `GameMemory.confirmed_actor_ids` first; else deterministic scoring over tracked objects using TransitionTable mobility evidence (edges with `moved_object_ids` containing the track), area/role priors; ties broken lexicographically;
- target: goal/invariant-referenced objects first; then shape/mirror-compatible objects (`identical_shape`, chiral-mirror relation types); deterministic tie-break;
- BFS/A* path over the grid using confirmed action vectors (`effect_vectors(allowed, confirmed_action_effects)`), perimeter-clamped.

### 12.3 `VirtualKinematicSandbox` (`virtual_sandbox.py`)

```python
class VirtualKinematicSandbox:
    def evaluate_and_repair_trajectory(self, trajectory, ...) -> SandboxEvaluationResult
    def synthesize_invariant_trajectory(self, invariant, ...) -> trajectory | None
```

- kinematics extraction solely from `action_semantics` + confirmed effects;
- generalized aspect-ratio criteria ($\ge 3.0$) instead of absolute-size constants;
- `ObservedEdgeOverlay`: observed TransitionTable facts override simulated edges — observation always beats simulation;
- A* heuristic: $`h(S) = 0.4\,\Delta_{centroid} + 0.2\,\Delta_{bbox} + 0.2\,(1-\mathrm{color\ match}) + 0.2\,\Delta_{count}`$ with perimeter clamping;
- repair output re-enters grounding and verification, never direct emission.

### 12.4 Tests

- fallback lifecycle: engagement conditions, single-run bound, no-RESET invariant, clean abandonment on cycle/death (`test_fallback_symbolic.py`, `test_divided_fallback_and_judge.py`, `test_solver_fallback_exhaustion.py`);
- actor selection: grounded vs prior-driven fixtures; determinism;
- overlay precedence: observed idle edge vetoes simulated step;
- A*: clamping at perimeters; heuristic monotonicity fixtures (`test_virtual_sandbox_and_curriculum.py`).

---

## 13. Cycle Detection (`cycle_detector.py`)

- transition tuples over `interior_grid_hash`: $`(\mathrm{hash}(S_{t-1}), a_t, \mathrm{hash}(S_t))`$;
- orbit detection: periods $1..$ `cycle_detector_max_period`, at least `cycle_detector_min_cycles` repetitions over at least `cycle_detector_min_actions` actions;
- recovery: sever active candidate, record failure, single clean `RESET`, replan with cycle-avoidance constraints; limited to `cycle_detector_per_level_limit` per level, then fallback path;
- hash function: deterministic row-encoded MD5 (16-hex truncation) — stable across processes (no `hash()`).

Tests: period matrix detection, min-cycle/min-action thresholds, per-level limit, interior-hash stability under HUD ticks, recovery side effects (`test_cycle_detector_and_deadline.py`, `test_collinear_axis_and_clean_reset.py`).

---

## 14. Sandbox Engineering (`sandbox.py`)

```python
def validate_dsl_source(source, allowed_modules) -> ValidationResult    # SafeASTVisitor

class SandboxAPI:           # narrow surface over the immutable PlanningSet
    query_objects(predicate); get_object(key); metric_distance(a, b, metric)
    declare_environment_action(action_id, ...); click_object(...)

class SandboxExecutor:
    def load_module(source, manifest) -> SandboxedModule
    def dry_run_manifest(module, manifest, planning_set) -> DryRunResult
    def execute(fn, args, ...) -> Any        # CPU + memory ceilings, timeout error typed
```

AST whitelist: allowed modules only (`sandbox_allowed_modules`); forbidden: imports outside the whitelist, I/O, network, subprocess, eval/exec, dunder attribute access, global mutation. Ceilings: `sandbox_max_cpu_seconds`, `sandbox_max_memory_mb`. Timeout raises `SandboxTimeoutError` → certification failure → repair loop. The sandbox has no gateway reference: DSL functions declare effects; the executor emits.

Tests: whitelist rejection matrix; ceiling enforcement; dry-run against fixtures; API surface closure (no attribute escape); `SandboxedModule` getattr restrictions (`test_sandbox.py`, `test_stage4_logical_and_sandbox.py`).

---

## 15. Logging and Telemetry (`logging.py`)

Structured JSON audit; every step logs at minimum:

```text
step_index, phase, arbitration_source, arbitration_reason
action_id, action_source, coords_local, coords_engine, crop_offset
guard_decisions: [{guard, allow|block, reason_code}]
budget_state: {level_actions_remaining, game_actions_remaining,
               chain_attempts_remaining, probes_remaining, evidence_probes_remaining}
deadline_remaining_seconds
verdict, semantic_effect (is_effective), explanation_code
severed (bool), sever_reason
transition_record_id, interior_pre/post_hash, delta_cells
transient: {present, geometry, micro_frame_count}
undecided: {streak, probes_issued}
memory_writes: {store: count}
llm_calls: [{family, profile_id, backend, prompt_hash, response_hash,
             schema_valid, retry_count, tokens, latency_ms}]
invalidations: {dsl_invalidated, replan_requested}
cycle_events, fallback_state
```

Per level: probes issued/deduplicated, chain attempts, exhaustion reasons. Per game: wins/losses/abandoned, call counts by family, schema-failure counts, judgment distribution (`FOLLOW/OMIT/NULL/UNDECIDED` counts), `OMIT`-vs-`NULL` ratio (calibration metric of the research program).

Logs must contain no endpoint keys, no raw prompts (hash + recorded payload reference instead), and no deployment identifiers.

---

## 16. Replay Requirements

A replay bundle contains: config snapshot (alias-resolved, private fields excluded), `LLMModelProfile`, per-call LLM records (prompt hash, compacted prompt payload, response hash, parsed output, validation result), TransitionTable trace export, judgment records, memory write log, telemetry stream.

Replay rules:

- replay recomputes the deterministic pipeline from recorded observations; LLM calls are loaded from records, never re-queried;
- a run requiring nondeterministic model re-queries is not a deterministic replay and fails acceptance;
- replay must reproduce: emitted action sequence, verdict sequence, severance points, memory store finals, telemetry aggregates;
- replay identity keys: `grid_hash` chain + judgment IDs + call record IDs.

---

## 17. Testing Strategy

### 17.1 Suite Composition

- **Unit contracts**: every module of §1 has a named test module; schemas (`v10.env_spec.1`, `v10.dsl_manifest.1`, `v10.trajectory_package.1`, `v10.verifier_packet.1`, `v10.judgment.1`, `v10.transition_record.1`, `v10.defeat_exemplar.2`) have conformance fixtures;
- **Property-based (Hypothesis)**: `test_pbt_brusentsov_axioms.py`, `test_pbt_brusentsov_severance.py`, `test_pbt_scale_invariance.py`, `test_pbt_color_permutation.py`, `test_pbt_coordinate_isomorphism.py`, `test_pbt_action_affordances.py`, `test_pbt_orthogonal_modality.py`;
- **Synthetic calibration micro-worlds** (`test_synthetic_calibration_worlds.py`): Maze Navigation (obstacle soft-stop, no false severance), Gravity Settling (soft boundary), Contact Trigger (state-change gating); micro-worlds are generated, never recorded benchmark content;
- **Integration**: end-to-end grounded package → verdict → memory; double-loop routing; harness lifecycle; reactive invalidation; budget exhaustion (`LevelAttemptsExhaustedError`, no RESET);
- **Purity**: AST Code Guardian over the whole package, zero findings required.

### 17.2 Offline Rule

The entire suite runs under the `fake` backend with no network and no model files. Any test requiring a real model is a deployment-manifest smoke test, lives outside `v10_agent/tests/`, and never gates acceptance.

### 17.3 New-in-10.8 Coverage (mandatory)

Transient-cell classification and Tier 3 override; JV FrameDiff optimality and vocabulary closure; triangulated defeat (with/without $`F_{fatal}`$); guard interdiction matrix; scheduler arbitration and degradation order; tabu-fallback grounding and overlay precedence; TransitionTable dual-space deduplication and `IDLE_UNLINKED` semantics; replay-basis completeness.

### 17.4 New-in-10.9 Coverage (mandatory)

Canonical-alignment conformance: `implies_brusentsov` rule-4 split (resolved out-of-contract change → `FALSE`; declared `Ω_sub` member → `IRRELEVANT`; unresolved observations intercepted by Tiers 4/7 as `UNDECIDED`); neutral-region registry (empty by default; contract-hash coupling; no legalization of §4.4 classes); `UNDECIDED`-retention on probe/streak exhaustion (no `NULL` rewrite, no `NEGATIVE_BARRIER` grounding, exactly one clean `RESET`); Tier 8 default restricted to resolved cases.

---

## 18. Validation Commands

Always run:

```bash
python -m compileall -q .
python -m pytest -q v10_agent/tests
python tools/ast_code_guardian.py v10_agent
python lcld_preflight.py
```

Focused suites:

```bash
python -m pytest -q v10_agent/tests/test_pbt_brusentsov_axioms.py \
                    v10_agent/tests/test_pbt_brusentsov_severance.py \
                    v10_agent/tests/test_judge_brusentsov_world_laws.py \
                    v10_agent/tests/test_pbt_undecided_exhaustion.py
python -m pytest -q v10_agent/tests/test_reactive_dsl_invalidation.py \
                    v10_agent/tests/test_isolation_invariants.py \
                    v10_agent/tests/test_prompt_isolation.py
python -m pytest -q v10_agent/tests/test_synthetic_calibration_worlds.py
```

All commands are environment-agnostic: no model paths, no cluster identifiers, no vendor env vars. Deployment smoke commands belong to the Deployment Manifest.

---

## 19. Reports

Create/update per engineering cycle:

```text
v10_9_transition_table.md
v10_9_transient_cells.md
v10_9_triangulated_defeat.md
v10_9_frame_diff.md
v10_9_action_guards.md
v10_9_priority_scheduler.md
v10_9_tabu_fallback.md
v10_9_model_neutral_runtime.md
v10_9_canonical_alignment.md
v10_9_integration_results.md
v10_9_findings.json
```

Historical V10.8-cycle artifacts keep their `v10_8_*` names; the V10.9 cycle adds `v10_9_canonical_alignment.md` (rule-4 split, neutral-region registry, exhaustion retention, test deltas).

Each report must include: files changed; tests added; exact commands run; compile/pytest/guardian results; judgment distribution (`FOLLOW/OMIT/NULL/UNDECIDED` counts); severance and reset counts; probe deduplication rate; guard block counts by reason; fallback engagements and outcomes; wins/errors/exhausted/max-steps per game; replay-basis completeness check; remaining blockers with verdict-level evidence. Reports must not contain deployment identifiers.

---

## 20. Acceptance Criteria

V10.9 implementation is acceptable only if:

- the 8-tier cascade is the sole transition judge, order-frozen, with `OMIT` never severing, empty expectations never confirming, `UNDECIDED` segregated and evidence-routed, and `UNDECIDED` never epistemically falsified (probe exhaustion retains the verdict and terminates the attempt; canonical §5.4);
- `implies_brusentsov` rule 4 conforms to canonical Definition 3.1 clause 5: a resolved out-of-contract change is `FALSE` unless inside a declared `Ω_sub` region; the neutral-region registry is empty by default and contract-hashed;
- every contradiction class of §4.4 is implemented and PBT-proven; the vacuity guards hold on $`S_0`$;
- no emission path bypasses grounding → guards → verifier; exactly one action per `act()`; `ACTION7` is unrepresentable in emissions;
- the dual-space contract holds end-to-end with symmetric deduplication (PBT coordinate isomorphism) and mask-pixel targeting;
- the two-tier action lifecycle preserves `CONDITIONAL_TRIGGER` actions and promotes them on first evidence;
- the TransitionTable records every action, distinguishes `IDLE_SELF_LOOP` from `IDLE_UNLINKED`, and feeds all six normative uses;
- transient evidence overrides static zero-delta classification; HUD ticks never perturb `interior_grid_hash`-based logic;
- defeat is triangulated with the honesty flag; exactly one `RESET` per `GAME_OVER`; safe prefixes preserved into replans;
- ISO-1..ISO-12 are test-enforced at the contour-manager boundary;
- the fallback is a single bounded tabu A* run, reset-free, verifier-supervised, with empirically grounded actor selection;
- budgets, deadline reserve, and scheduler degradation follow the normative order with complete logging;
- the runtime is model-neutral: backend abstraction + profile; the full suite passes under `fake`; no model/vendor/engine/cluster identifier appears in agent-core code, config field names, or these specifications;
- every session is replayable from records without re-querying any model;
- `compileall`, the full pytest suite, and the AST Code Guardian all pass with zero failures/findings;
- the harness demonstrates improved wins or produces exact blocker diagnostics with verdict-level evidence.
