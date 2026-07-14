# ARC-AGI-3 LCLD Agent
# Engineering Specification



### 0.1 V6.2 Engineering Amendment

V6.2 adds three mandatory engineering changes:

1. `information_gain_observed` is a verifier-side posterior uncertainty reduction metric over registered semantic variables. It is not raw grid-difference magnitude.
2. The LLM prompt builder must use prompt-tail priority for local 7B models: `previous_attempts_feedback`, `semantic_candidate_menu`, `current_question_set`, `allowed_output_schema`, and the strict JSON instruction must appear at the end of the prompt.
3. Terminal progress must support sparse/binary-feedback environments. `TerminalProgressModel` may use metadata deltas when present, but must also support bounded proxy evidence and must abstain when no valid evidence exists.


## 0. Engineering Objective

Build an ARC-AGI-3 agent that:

- parses heterogeneous interactive environments;
- extracts deterministic object-centric representations;
- constructs ARGA-style semantic graphs;
- serializes environment/action state into compact deterministic JSON;
- uses a local offline LLM as the primary semantic hypothesis proposer when configured;
- validates all LLM proposals through strict schema and binder grounding;
- compiles bound hypotheses into capability-conditioned DSL programs;
- routes candidate programs through a verification queue;
- evaluates programs under rollback;
- uses ExactVerifier as the final judge;
- supports three-valued semantic outcomes: `REQUIRED`, `FORBIDDEN`, `IRRELEVANT`;
- stores verifier backreaction in external task-local memory;
- feeds structured failures/irrelevance/no-op outcomes back into the next LLM prompt;
- remains fully offline, reproducible, bounded, and replayable.

V6 changes the implementation target from symbolic-first search to **LLM-priority neuro-symbolic search**.

Core ownership:

```text
LLM = primary semantic proposer
ARGA/Object/Manifest = canonical state serializer
Binder = grounding and error computation
CapabilityConditionedDSLCompiler = hypothesis-to-program bridge
HypothesisRouter = verification queue planner
PureSymbolicRanker = helper/fallback/tie-breaker
ExactVerifier = final judge
Memory = external recursive state between verifier and next LLM prompt
```

Target constraints:

- Python 3.12 or newer;
- offline-only execution;
- no external APIs;
- no hidden nondeterminism;
- no internet dependency;
- optional local LLM backend with a modest default profile such as `qwen2.5-7b-instruct-q4_k_m.gguf`;
- pytest must not require a real model;
- full auditability of every action boundary;
- ExactVerifier remains the only legality and execution authority.

---

## 1. Repository Structure

Recommended active structure:

```text
src/
  core/
  capability/
    manifest.py
    action_schema.py
    affordance_registry.py
    capability_constraints.py

  parser/
    grid_extraction.py
    playfield.py
    connected_components.py
    object_slot.py
    pattern_detector.py
    semantic_serializer.py

  scene_graph/
    scene_graph.py
    semantic_graph.py
    arga_adapter.py
    arga_state_assembler.py
    relation_model.py
    graph_hashing.py

  semantics/
    three_valued.py
    semantic_judgment.py
    semantic_hypotheses.py
    error_functions.py
    information_gain.py

  llm_advisor/
    llm_semantic_proposer.py
    prompts.py
    schemas.py
    qwen_local.py
    fake_qwen.py
    replay_records.py
    prompt_feedback_formatter.py
    prompt_builder.py

  memory/
    verifier_backreaction_memory.py
    trajectory_memory.py
    capability_constraint_memory.py
    game_experience_memory.py
    advisory_memory.py
    semantic_memory_buffer.py

  dsl/
    primitives.py
    graph_dsl.py
    capability_conditioned_compiler.py
    trajectory_programs.py
    binding.py
    serialization.py

  search/
    hypothesis_router.py
    symbolic_ranker.py
    trajectory_planner.py
    transition_graph.py
    action_effect_model.py
    program_generator.py
    candidate_evaluator.py
    terminal_progress_model.py

  verifier/
    exact_verifier.py
    capability_verifier.py
    stabilization_verifier.py
    transition_verifier.py
    topology_verifier.py
    reachability_verifier.py
    action_semantics_verifier.py
    affordance_verifier.py
    terminal_verifier.py
    replay_verifier.py
    semantic_relevance_verifier.py

  environment/
    wrapper.py
    observation_adapter.py
    action_adapter.py
    rollback_manager.py
    stabilization.py
    coordinate_transform.py

  replay/
  eval/
  visualization/
  debug/
```

### 1.1 Active-Path Rule

Do not create duplicate inactive modules. Every new module must be:

- imported by active pipeline;
- covered by tests; or
- explicitly marked experimental and disabled.

V6 modules must replace, wrap, or route existing V5.1 modules cleanly.

---

## 2. Configuration Contract

### 2.1 Default Behavior

Without local model/backend:

```python
hypothesis_mode = "symbolic_only"
enable_llm_semantic_advisor = False
llm_default_fell_back_to_symbolic = True
```

With configured local model/backend:

```python
hypothesis_mode = "hybrid"
enable_llm_semantic_advisor = True
llm_advisor_backend = "qwen_local"
llm_priority_hybrid = True
```

Explicit user config/env always wins.

### 2.2 Required Config Keys

```text
enable_llm_semantic_advisor: bool
hypothesis_mode: symbolic_only | hybrid | llm_semantic
llm_priority_hybrid: bool
llm_advisor_backend: disabled | qwen_local | llama_cli | llama_server | ollama | fake
qwen_model_path: str | None
qwen_llama_cli_path: str | None
qwen_llama_device: str | None
qwen_gpu_layers: int | None
qwen_context_tokens: int
qwen_max_output_tokens: int
qwen_temperature: float
qwen_seed: int
qwen_strict_required: bool
llm_timeout_seconds: int
llm_empty_output_retry_enabled: bool
llm_nonempty_graph_requires_proposal: bool
llm_model_profile: str
llm_context_strategy: normal | aggressive | minimal
llm_max_input_tokens: int
llm_compression_trigger_ratio: float
llm_fallback_to_structured_only: bool
llm_note_summarization_enabled: bool
semantic_memory_enabled: bool
semantic_memory_max_notes: int
semantic_memory_top_k: int
prompt_tail_priority_enabled: bool
information_gain_min_threshold: float
terminal_progress_sparse_mode: bool
```

### 2.3 Required Env Vars

```text
ARC_HYPOTHESIS_MODE
ARC_ENABLE_LLM_SEMANTIC_ADVISOR
ARC_LLM_ADVISOR_BACKEND
ARC_LLM_PRIORITY_HYBRID
ARC_QWEN_MODEL_PATH
ARC_QWEN_LLAMA_CLI_PATH
ARC_QWEN_LLAMA_DEVICE
ARC_QWEN_GPU_LAYERS
ARC_QWEN_CONTEXT_TOKENS
ARC_QWEN_MAX_OUTPUT_TOKENS
ARC_QWEN_TEMPERATURE
ARC_QWEN_SEED
ARC_QWEN_STRICT_REQUIRED
ARC_LLM_MODEL_PROFILE
ARC_LLM_CONTEXT_STRATEGY
ARC_LLM_MAX_INPUT_TOKENS
ARC_SEMANTIC_MEMORY_ENABLED
```

### 2.4 Config Tests

Required tests:

- no model/backend defaults to symbolic-only;
- explicit symbolic_only disables LLM;
- model path + backend enables hybrid LLM-priority;
- explicit llm_semantic disables deterministic induction only as ablation;
- fake backend works without real model;
- config does not permit direct LLM action emission.


### 2.5 Baseline Local Model Profile

V6.2 is model-neutral, but the reference local profile is deliberately modest:

```text
llm_model_profile: qwen2_5_7b_instruct_gguf_baseline
reference_model_filename: qwen2.5-7b-instruct-q4_k_m.gguf
backend: qwen_local | llama_cli | llama_server | ollama | fake
qwen_context_tokens: 8192
llm_max_input_tokens: 6000
qwen_max_output_tokens: 512
qwen_temperature: 0.0
llm_timeout_seconds: 120
llm_context_strategy: normal
llm_compression_trigger_ratio: 0.80
llm_fallback_to_structured_only: true
```

The implementation must not hard-depend on this model name. It is the baseline profile for local development and should be replaceable by changing `LLMModelProfile` config only. The baseline model is expected to provide semantic pattern recognition over compact ARGA JSON; deep reasoning output is not required and must not be requested as chain-of-thought.

### 2.6 LLM Context Management Contract

Required config object:

```text
LLMContextManagement:
  max_input_tokens: int = 6000
  max_output_tokens: int = 512
  context_tokens: int = 8192
  compression_trigger_ratio: float = 0.80
  context_strategy: normal | aggressive | minimal = normal
  fallback_to_structured_only: bool = true
  note_summarization_enabled: bool = true
  preserve_valid_ids: bool = true
  preserve_action_surface: bool = true
```

When estimated prompt size exceeds `compression_trigger_ratio * max_input_tokens`, the prompt builder must compact previous feedback, old transitions, old notes, and low-salience ARGA edges. It must never drop valid ids, action surface, coordinate schema, current verifier feedback, active trajectory summary, or allowed output schema.

---



### 2.7 Prompt Tail Priority for Local 7B Models

The prompt builder must order prompt sections for attention density:

1. stable high-level task/system constraints;
2. compact scene/ARGA/object/action surface context;
3. persistent notes and older transition summaries;
4. current active trajectory and current unresolved questions;
5. **tail-priority section**:
   - `previous_attempts_feedback`;
   - `semantic_candidate_menu`;
   - `current_question_set`;
   - `allowed_output_schema`;
   - strict `return JSON only` instruction.

Under context pressure, the builder must preserve the tail-priority section before low-salience object/edge detail. This is mandatory for the local 7B baseline because late prompt tokens are more likely to dominate JSON generation behavior.

Tests:

- serialized prompt places `previous_attempts_feedback` after broad ARGA context;
- serialized prompt places `semantic_candidate_menu` after feedback or immediately before schema;
- `allowed_output_schema` and strict JSON instruction are final;
- `minimal` compaction still preserves tail-priority sections.


## 3. Capability Manifest Contract

`EnvironmentCapabilityManifest` remains mandatory and must include fields for:

- game/level identity;
- action surface;
- coordinate action ids;
- payload schema;
- reset/undo/selection availability;
- logical grid contract;
- palette contract;
- stabilization schema;
- semantic graph schema;
- transition graph schema;
- LLM advisory schema;
- verifier backreaction schema;
- three-valued verifier schema.

### 3.1 Grid and Palette Record

```text
GridPaletteRecord:
  grid_shape: tuple[int, int]
  palette_domain: tuple[int, int] = (0, 15)
  palette_ids_seen: tuple[int, ...]
  grid_source: logical_grid | engine_layer | rgb_quantized_fallback
  coordinate_order: x=col,y=row
  confidence: float
```

### 3.2 Capability Constraint Records

```text
CapabilityConstraintRecord:
  constraint_id: str
  game_id: str
  level_id: str
  action_id: str | None
  target_signature: str | None
  region_signature: str | None
  constraint_type: coordinate_no_effect | blocked | no_op | invalid_target | action_surface_changed | unknown
  verifier_judgment: REQUIRED | FORBIDDEN | IRRELEVANT | UNRESOLVED
  evidence_count: int
  counterexample_count: int
  scope: current_step | current_level | current_game
  confidence: float
```

Manifest revisions require repeated verifier-backed evidence and must be replayable.

---

## 4. Three-Valued Semantics Engineering

### 4.1 Enums

Implement in `semantics/three_valued.py`:

```python
class Applicability(str, Enum):
    APPLICABLE = "APPLICABLE"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    UNDECIDED = "UNDECIDED"

class EpistemicResolution(str, Enum):
    RESOLVED = "RESOLVED"
    UNRESOLVED = "UNRESOLVED"

class SemanticJudgment(str, Enum):
    REQUIRED = "REQUIRED"
    FORBIDDEN = "FORBIDDEN"
    IRRELEVANT = "IRRELEVANT"
    UNRESOLVED = "UNRESOLVED"
```

### 4.2 Verifier Verdict Schema

```text
ExactVerdict:
  accept: bool
  verdict_status: ACCEPT | REJECT | UNRESOLVED
  semantic_judgment: REQUIRED | FORBIDDEN | IRRELEVANT | UNRESOLVED
  reason_code: str
  reason: str
  relevance_score: float
  observed_information_gain: float
  observed_error_delta: float | None
  replay_status: str
  stabilization_status: str
  verifier_module: str
  rollout_hash: str
```

### 4.3 Required Tests

- legal useful transition -> `ACCEPT`, `REQUIRED`;
- legal no-op -> `ACCEPT`, `IRRELEVANT`;
- illegal action -> `REJECT`, `FORBIDDEN`;
- unstable rollout -> `REJECT`, `UNRESOLVED` or dedicated unstable reason;
- irrelevant result is fed to memory and suppresses equivalent retry;
- irrelevant is not treated as forbidden.



## 4A. Observed Information Gain Engineering

### 4A.1 Definition

`information_gain_observed` measures how much a stable verifier-evaluated action/program reduces uncertainty over explicitly registered semantic variables.

It must not be computed from raw cell-change count, raw image difference, or untyped object churn.

Before candidate evaluation, the router/compiler must register:

```text
SemanticQuestion:
  variable_id: str
  variable_type: affordance | controllability | action_effect | relation_relevance | hypothesis_viability | capability_constraint | terminal_progress | action_surface_change
  target_object_ids: tuple[str, ...]
  target_relation_ids: tuple[str, ...]
  action_ids: tuple[str, ...]
  domain: tuple[str, ...]
  prior_distribution: dict[str, float]
  relevance_weight: float
  expected_evidence_predicates: tuple[str, ...]
```

### 4A.2 Entropy Formula

For each question `q_i`:

```text
H_norm(P_i) = - Σ_k P_i(k) log(P_i(k)) / log(|D_i|)
IG_i = max(0, H_norm(P_i_before) - H_norm(P_i_after))
```

Aggregate score:

```text
information_gain_observed =
  clip(
    reliability *
    Σ_i relevance_i * evidence_link_i * IG_i / max(epsilon, Σ_i relevance_i)
    + structural_novelty_gain
    - noise_penalty
    - repeat_penalty
    - instability_penalty,
    0,
    1
  )
```

Where:

- `reliability = 0` unless rollout is stable, replayable, manifest-legal, and verifier-consistent;
- `evidence_link_i = 0` for unrelated grid/UI/noise changes;
- `repeat_penalty` suppresses repeated equivalent probes from equivalent semantic states;
- `instability_penalty` suppresses transitional or non-replayable outcomes.

### 4A.3 Posterior Update

Implementation may use simple Dirichlet/categorical counts:

```text
P_i(k) = (count_i[k] + alpha) / Σ_j(count_i[j] + alpha)
```

After evidence, update only the outcome supported by verifier-stable typed evidence. Do not update posterior from raw unlinked visual changes.

### 4A.4 Judgment Rules

- Goal trajectory eligibility requires rollback-observed error reduction.
- Epistemic trajectory eligibility requires `information_gain_observed >= theta_info_min`.
- Legal no-op can be epistemically useful only if it resolves a registered question.
- Legal no-op without registered uncertainty reduction is `ACCEPT_IRRELEVANT`.
- Repeated equivalent no-op should produce near-zero gain after prior evidence exists.

Recommended thresholds:

```text
theta_info_min = 0.03
theta_info_good = 0.10
theta_info_strong = 0.20
```

### 4A.5 Required Telemetry

```text
information_gain_observed
information_gain_components
registered_question_count
entropy_before
entropy_after
entropy_drop
evidence_link
relevance_weight
noise_penalty
repeat_penalty
stability_reliability
epistemic_result
```

### 4A.6 Tests

- unrelated raw grid delta gives zero information gain;
- registered affordance no-op gives positive first-time epistemic gain;
- repeated equivalent no-op is penalized to near zero;
- unstable rollout gives zero gain;
- action-surface change linked to registered question gives positive gain;
- accepted no-op without registered question becomes `ACCEPT_IRRELEVANT`.


---

## 5. Object-Centric Parser Contract

`ObjectSlot` required fields:

```text
object_id: str
sprite_id: str | None
bbox_rc: tuple[int, int, int, int]
centroid_rc: tuple[float, float]
area: int
colors: dict[int, int]
topology: str
internal_pattern: PatternDescriptor | None
symmetry: tuple[str, ...]
holes: int
border_touching: tuple[str, ...]
semantic_tags: tuple[str, ...]
relations: tuple[str, ...]
controllability_score: float
affordance_scores: dict[str, float]
stable_identity_hash: str
uncertainty: dict[str, float]
```

Parser tests from V5.1 remain required, including 64x64 grid and palette 0..15 handling.

---

## 6. ARGA State Assembler

### 6.1 Module

`scene_graph/arga_state_assembler.py` exposes:

```python
build_arga_state_snapshot(
    stable_observation,
    manifest,
    object_slots,
    semantic_graph,
    transition_graph,
    action_effect_model,
    active_trajectory,
    verifier_backreaction_memory,
    failed_trajectory_memory,
    capability_constraint_memory,
    game_experience_memory,
    current_bound_goals,
    current_epistemic_hypotheses,
    unresolved_relations,
    config,
) -> ARGAStateSnapshot
```

### 6.2 Snapshot Schema

```text
ARGAStateSnapshot:
  schema_version: v6.arga_state_snapshot.1
  session_id: str
  game_id: str
  level_id: str
  manifest_hash: str
  observation_hash: str
  stable_state_hash: str
  grid_shape: tuple[int, int]
  grid_contract: dict
  palette_ids_seen: tuple[int, ...]
  grid_source: str
  coordinate_order: str
  action_surface_summary: dict
  available_actions: tuple[str, ...]
  coordinate_action_ids: tuple[str, ...]
  coordinate_payload_schema: dict
  coordinate_slots_or_targets: tuple
  reset_available: bool
  undo_available: bool
  selection_available: bool
  object_slots: tuple[dict, ...]
  arga_nodes: tuple[dict, ...]
  arga_edges: tuple[dict, ...]
  relation_errors: tuple[dict, ...]
  current_bound_goals: tuple[dict, ...]
  current_epistemic_hypotheses: tuple[dict, ...]
  active_trajectory: dict | None
  last_transition_edges: tuple[dict, ...]
  last_action_effects: tuple[dict, ...]
  recent_verifier_rejections: tuple[dict, ...]
  previous_attempts_feedback: tuple[dict, ...]
  failed_trajectory_summary: tuple[dict, ...]
  failed_hypotheses_summary: tuple[dict, ...]
  irrelevant_attempts_summary: tuple[dict, ...]
  unresolved_relations: tuple[dict, ...]
  game_scoped_experience_hints: tuple[dict, ...]
  persistent_notes_summary: tuple[dict, ...]
  semantic_state_signature: str
  recent_irrelevant_attempts_summary: tuple[dict, ...]
  capability_constraint_summary: tuple[dict, ...]
  active_trajectory_prediction_vs_observed: dict | None
  llm_context_budget_state: dict
  current_question_set: tuple[dict, ...]
  prompt_tail_priority_sections: tuple[str, ...]
  information_gain_budget_state: dict
  terminal_progress_summary: dict | None
  capability_constraints: tuple[dict, ...]
  allowed_output_schema: dict
  valid_object_ids: tuple[str, ...]
  valid_relation_ids: tuple[str, ...]
  valid_graph_operator_names: tuple[str, ...]
  valid_error_function_names: tuple[str, ...]
```

### 6.3 Compaction Rules

Compaction may reduce object/edge/history counts but may never drop:

- valid id lists;
- action surface;
- coordinate availability;
- previous feedback summaries;
- capability constraints;
- allowed output schema.

### 6.4 Tests

- snapshot contains action surface;
- snapshot contains coordinate action ids;
- snapshot contains previous verifier feedback;
- snapshot contains failed and irrelevant attempts;
- snapshot contains active trajectory;
- snapshot compaction preserves valid ids and action surface;
- snapshot hash is deterministic.


### 6.5 Snapshot Compaction and Context Budget Tests

`ARGAStateSnapshot` must implement or expose deterministic compaction:

```python
snapshot.compact(strategy: Literal["normal", "aggressive", "minimal"], max_items: dict | None = None) -> ARGAStateSnapshot
```

Compaction may reduce low-salience object details, old transitions, old notes, and low-priority edges. It must preserve:

- `valid_object_ids`;
- `valid_relation_ids`;
- `available_actions`;
- `coordinate_action_ids`;
- `coordinate_payload_schema`;
- `previous_attempts_feedback` relevant to current state;
- `persistent_notes_summary` relevant to current game/state;
- `active_trajectory_prediction_vs_observed` when active;
- allowed output schema.

Tests:

- compact normal/aggressive/minimal modes are deterministic;
- compaction preserves all valid ids;
- compaction preserves action surface;
- compaction preserves current feedback and active trajectory summary;
- oversized prompt switches to aggressive or minimal strategy.

---

## 7. LLM Semantic Proposer

### 7.1 Interface

`llm_advisor/llm_semantic_proposer.py`:

```python
class LLMSemanticProposer:
    def is_available(self, config) -> bool: ...
    def propose(self, snapshot: ARGAStateSnapshot, config) -> SemanticProposalResult: ...
```

### 7.2 Output Schema

```text
SemanticProposalResult:
  schema_version: str
  backend: str
  model_id: str | None
  prompt_hash: str
  response_hash: str
  valid_json: bool
  parse_policy_status: str
  semantic_hypotheses: tuple[SemanticHypothesisProposal, ...]
  suggested_epistemic_tests: tuple[EpistemicTestProposal, ...]
  capability_questions: tuple[CapabilityQuestion, ...]
  risk_flags: tuple[dict, ...]
  empty_output_on_nonempty_graph: bool
  retry_used: bool
  raw_response_excerpt_hash: str
```

### 7.3 SemanticHypothesisProposal

```text
proposal_id: str
family: str
target_object_ids: tuple[str, ...]
target_relation_ids: tuple[str, ...]
semantic_role: str
expected_relation: str
requires_error_function: str
suggested_graph_operator: str
expected_semantic_judgment: REQUIRED | IRRELEVANT | UNRESOLVED
confidence: float
reason_code: str
```

### 7.4 Prompt Requirements

Prompt must state:

- propose hypotheses over existing ids;
- return strict JSON;
- never emit actions;
- never emit coordinates;
- never invent ids;
- return non-empty hypotheses/tests on non-empty graph;
- include previous feedback as do-not-repeat/try-different evidence;
- distinguish forbidden vs irrelevant results.

Priority mappings:

```text
unique_symbol_pair        -> SymbolPairAlignment / AlignNodeToNode / centroid_distance
button_like_structure     -> ButtonLikeAffordance / ProbeNodeAffordance / affordance_unknown
scaled_layout_similarity  -> MapProjection / InterpretMapProjection / scaled_layout_mismatch
separated_by_gap          -> BridgeGap / BridgeGap / gap_distance
line_continuation         -> ConnectionGoal or PatternCompletion / ExtendLineToTarget / line_endpoint_distance
frame_contains or contains -> ContainmentGoal / MoveNodeIntoContainer / containment_outside_distance
same_shape                -> SameShapeAlignment / AlignNodeToNode / centroid_distance or mask_overlap_mismatch
same_color                -> SameColorConnection / ConnectNodes / gap_distance or centroid_distance
```

### 7.5 Retry Policy

If real LLM returns empty arrays on a non-empty graph in LLM-priority mode:

1. log `llm_empty_output_on_nonempty_graph=True`;
2. issue one smaller relation-focused retry;
3. if still empty, continue with deterministic fallback but mark advisor no-op.

### 7.6 Tests

- FakeQwen returns non-empty on non-empty graph;
- unique_symbol_pair fixture yields SymbolPairAlignment;
- button_like_structure fixture yields ButtonLikeAffordance or AffordanceProbe;
- scaled_layout_similarity fixture yields MapProjection;
- direct actions are rejected;
- invented ids are rejected;
- empty real output triggers retry;
- pytest uses fake backend only.


### 7.7 Model-Neutral Local Backend Contract

The default local implementation target is:

```text
qwen2.5-7b-instruct-q4_k_m.gguf
```

This is a reference profile only. The code must use `LLMModelProfile` and backend abstraction so that another local GGUF/instruct model can replace it with minimal config changes.

The prompt must not request hidden chain-of-thought. It should request concise strict JSON proposals. The baseline model is used for semantic recognition of ARGA relations, affordance cues, map-like layouts, symbol pairs, and relevance/irrelevance hypotheses.

Supported backend labels:

```text
disabled | qwen_local | llama_cli | llama_server | ollama | fake
```

Required model profile fields:

```text
profile_id
backend
model_path
context_tokens
max_input_tokens
max_output_tokens
temperature
seed
timeout_seconds
context_strategy
supports_json_mode | false
may_emit_thinking | false
```

---

## 8. Semantic Hypothesis Binder

### 8.1 Raw Hypothesis Source Fields

```text
source: qwen | fake | deterministic | experience
source_priority: int
llm_confidence: float | None
advisor_reason_code: str | None
expected_semantic_judgment: SemanticJudgment
```

Suggested priorities:

```text
qwen/fake high-confidence valid proposal: 100
same-game experience hint: 80
deterministic measurable relation: 60
deterministic epistemic relation: 40
```

### 8.2 Binding Behavior

Binder may infer missing ids only from existing deterministic graph evidence:

- valid object pair without relation id -> attach best compatible existing relation edge;
- valid relation id without object ids -> infer endpoints;
- missing error function -> try family defaults;
- unsupported/hallucinated proposal -> reject.

### 8.3 Bound Output

```text
BoundGoalHypothesis:
  hypothesis_id
  family
  source
  source_priority
  target_object_ids
  target_relation_ids
  target_node_ids
  target_edge_ids
  error_name
  current_error
  llm_confidence
  advisor_reason_code
  semantic_judgment_hint
  evidence

BoundEpistemicHypothesis:
  hypothesis_id
  family
  source
  source_priority
  target_object_ids
  target_relation_ids
  information_gain_target
  llm_confidence
  advisor_reason_code
  semantic_judgment_hint
  evidence
```

### 8.4 Tests

- Qwen valid object pair without relation id binds through existing ARGA edge;
- Qwen relation id without object ids binds through endpoints;
- Qwen high-confidence proposal with `none` error tries family default;
- hallucinated ids rejected;
- unsupported operator rejected;
- binder inference never creates actions.

---

## 9. CapabilityConditionedDSLCompiler

### 9.1 Interface

```python
compile_bound_hypothesis(
    bound_hypothesis,
    manifest,
    arga_graph,
    action_effect_model,
    capability_constraints,
    failed_memory,
) -> tuple[CandidateProgram, ...]
```

### 9.2 Operator Support

Required operators:

- `ProbeNodeAffordance`;
- `ProbeRelation`;
- `BridgeGap`;
- `ConnectNodes`;
- `MoveNodeIntoContainer`;
- `ExtendLineToTarget`;
- `InterpretMapProjection`;
- `CompletePattern`;
- `AlignNodeToNode`;
- `MoveNodeToward`.

### 9.3 Coordinate Probe Rules

For coordinate actions, candidate targets are object/affordance-centered:

- centroid;
- bbox center;
- contour midpoint;
- button-like hotspot;
- relation hotspot;
- guide-line intersection;
- region center.

Full-grid enumeration is forbidden unless explicitly enabled for diagnostics and tightly bounded.

### 9.4 Tests

- ButtonLikeAffordance compiles to coordinate probe when coordinate action exists;
- invalid coordinate target rejected before verification;
- BridgeGap compiles only with measurable gap target;
- MapProjection remains epistemic if ambiguous;
- compiler never emits action without verifier path.

---

## 10. HypothesisRouter

### 10.1 Interface

```python
class HypothesisRouter:
    def plan_queue(
        self,
        bound_goals,
        epistemic_hypotheses,
        candidate_programs,
        memory,
        pure_symbolic_ranker,
        config,
    ) -> tuple[HypothesisRouteItem, ...]: ...
```

### 10.2 Route Item

```text
HypothesisRouteItem:
  route_id: str
  hypothesis_id: str
  source: str
  source_priority: int
  candidate_program_id: str
  graph_operator: str
  expected_judgment: REQUIRED | IRRELEVANT | UNRESOLVED
  expected_error_delta: float | None
  expected_information_gain: float
  llm_confidence: float | None
  pure_symbolic_score: dict
  failed_memory_status: none | penalized | suppressed
  route_reason: str
```

### 10.3 Routing Algorithm

Order by:

1. hard validity and manifest compatibility;
2. failed/irrelevant memory suppression;
3. valid LLM proposal with measurable error, high confidence, and no memory block;
4. valid deterministic or experience proposal with measurable error and rollback-observed progress evidence;
5. high-confidence LLM epistemic test with explicit information-gain target;
6. PureSymbolic measurable fallback;
7. generic exploration probes;
8. relation salience;
9. PureSymbolicRanker helper score;
10. cost/depth/budget.

Rules:

- Qwen proposals are processed before deterministic fallback in LLM-priority hybrid mode;
- measured rollback-observed progress dominates LLM confidence;
- verifier rejection dominates everything;
- irrelevance suppresses exact repeats but does not mark physics as impossible;
- PureSymbolicRanker cannot authorize actions.

### 10.4 Tests

- Qwen measurable goal outranks equal deterministic goal;
- deterministic candidate with better rollback-observed progress outranks Qwen;
- Qwen epistemic affordance test outranks generic discovery;
- failed-memory suppressed candidate is not routed;
- irrelevant candidate is demoted/suppressed, not forbidden;
- router cannot emit final actions.

---

## 11. PureSymbolicRanker

PureSymbolicRanker remains active but is no longer the primary policy engine.

Responsibilities:

- score measured error reduction;
- score information gain;
- penalize repeated states;
- penalize failed or irrelevant repeats;
- provide deterministic fallback;
- provide tie-breaking;
- provide ablation comparison.

Required score record:

```text
total
lexicographic_key
ranking_mode
semantic_goal_alignment
rollback_observed_progress
information_gain
repeated_state_penalty
failed_trajectory_penalty
irrelevant_attempt_penalty
llm_priority_bonus_if_any
explanation
canonical_hash
```

---

## 12. Candidate Evaluation and Verifier Integration

### 12.1 Evaluation Record

```text
CandidateEvaluation:
  candidate_id
  hypothesis_id
  route_id
  rollback_snapshot_id
  verifier_verdicts
  final_verdict_status
  final_semantic_judgment
  error_before
  predicted_error_after
  rollback_observed_error_after
  rollback_observed_error_delta
  observed_information_gain
  transition_novelty
  accepted_required: bool
  accepted_irrelevant: bool
  rejected_forbidden: bool
  unresolved: bool
  reason_code
```

### 12.2 Eligibility

Goal trajectory selectable if:

- all steps manifest-legal;
- verifier accepts;
- semantic judgment not forbidden;
- rollback-observed error decreases;
- not irrelevant/no-op;
- not failed-memory suppressed.

Epistemic candidate selectable if:

- verifier accepts;
- observed information gain or transition novelty positive;
- not irrelevant/no-op repeat;
- not failed-memory suppressed.

### 12.3 Tests

- predicted-only progress rejected;
- verifier-accepted no-op becomes `ACCEPT_IRRELEVANT`;
- irrelevant candidate is recorded and suppresses exact retry;
- forbidden candidate is rejected and blocks route;
- useful candidate can be emitted only through verifier path.

---

## 13. Memory Engineering

### 13.1 VerifierBackreactionRecord

```text
attempt_id: str
step_index: int
hypothesis_id: str
hypothesis_family: str
hypothesis_source: str
target_object_ids: tuple[str, ...]
target_relation_ids: tuple[str, ...]
graph_operator: str
compiled_program_signature: str
action_sequence: tuple[dict, ...]
verdict_status: ACCEPT | REJECT | UNRESOLVED
semantic_judgment: REQUIRED | FORBIDDEN | IRRELEVANT | UNRESOLVED
verifier_reason_code: str
verifier_reason: str
semantic_error_before: float | None
semantic_error_after: float | None
semantic_error_delta: float | None
observed_information_gain: float
environment_effect: no_op | blocked | moved_expected | moved_wrong_object | changed_unrelated_state | terminal | unknown
next_prompt_summary: str
state_signature: str
```

### 13.2 Prompt Feedback Formatter

Formats backreaction as:

```json
{
  "previous_attempts_feedback": [
    {
      "your_hypothesis": "SymbolPairAlignment(node_a,node_b)",
      "compiled_program": "ACTION3 repeated 2 steps",
      "verifier_result": "ACCEPT_IRRELEVANT",
      "semantic_judgment": "IRRELEVANT",
      "reason": "legal movement but target relation error unchanged",
      "instruction_to_llm": "Do not repeat this operator/target unless new evidence changes."
    }
  ]
}
```

### 13.3 Failed and Irrelevant Memory

Write memory records for:

- `semantic_error_not_decreased`;
- `semantic_error_unavailable`;
- `prediction_mismatch`;
- `verifier_rejected_next_step`;
- `rollback_observed_error_not_decreased`;
- `accept_irrelevant_no_information_gain`;
- `trajectory_timeout`;
- `manifest_changed_invalidates_trajectory`.

### 13.4 Tests

- forbidden attempt blocks equivalent retry;
- irrelevant attempt suppresses/demotes equivalent retry;
- same idea allowed after new evidence;
- prompt includes previous feedback;
- memory resets per task;
- game-scoped experience remains exact-game scoped.


### 13.5 SemanticMemoryBuffer

`memory/semantic_memory_buffer.py` implements persistent structured notes.

Interface:

```python
class SemanticMemoryBuffer:
    def add_note(self, note: SemanticMemoryNote) -> str: ...
    def retrieve(self, query: SemanticMemoryQuery, *, top_k: int, budget_tokens: int) -> tuple[SemanticMemoryNote, ...]: ...
    def summarize_old_notes(self, *, budget_tokens: int) -> tuple[SemanticMemoryNote, ...]: ...
    def to_prompt_summary(self, notes: tuple[SemanticMemoryNote, ...]) -> tuple[dict, ...]: ...
    def export_replay(self) -> dict: ...
```

`SemanticMemoryNote` schema:

```text
note_id: str
game_id: str
level_id: str | None
semantic_state_signature: str | None
note_type: success | failure | irrelevance | affordance | action_effect | capability_constraint | strategy | summary
summary: str
importance_score: float
confidence: float
evidence_refs: tuple[str, ...]
related_object_signatures: tuple[str, ...]
related_relation_types: tuple[str, ...]
related_action_ids: tuple[str, ...]
hypothesis_family: str | None
verifier_outcome: str | None
semantic_judgment: REQUIRED | FORBIDDEN | IRRELEVANT | UNRESOLVED
created_at_step: int
last_used_step: int | None
ttl_policy: current_level | current_game | abstract_global
replay_hash: str
```

Retrieval rules:

- filter by exact `game_id` before semantic similarity;
- require action-surface compatibility;
- prefer symbolic filters before optional vector retrieval;
- optional FAISS/in-memory vector retrieval is allowed only after exact filters;
- retrieved notes are advisory prompt context, never action authority;
- LLM-generated summaries must be replay-recorded.

### 13.6 Relevance and Irrelevance Memory

Keep `FailedTrajectoryMemory` and `IrrelevantAttemptMemory` separate.

- Failed memory blocks or strongly penalizes forbidden/impossible trajectories.
- Irrelevant memory suppresses exact no-progress/no-information-gain repeats from equivalent semantic states.
- Irrelevance does not create global forbidden facts.
- Prompt feedback must state whether a prior attempt was `FORBIDDEN`, `IRRELEVANT`, or `UNRESOLVED`.

Tests:

- persistent note retrieval is game-scoped;
- cross-game note retrieval is rejected;
- irrelevant note appears in prompt feedback but does not block unrelated hypotheses;
- old notes are summarized when over budget;
- note replay uses logged records and does not re-run LLM summarization.

---

## 14. LLM Semantic Loop Prevention

Implement:

```python
def semantic_state_signature(...):
    return stable_hash({
        "semantic_graph_hash": ..., 
        "action_surface_hash": ..., 
        "active_hypothesis_family": ..., 
        "recent_goal_families": ..., 
        "recent_epistemic_families": ..., 
        "palette_ids_seen": ..., 
        "grid_shape": ..., 
        "failed_or_irrelevant_attempts": ...,
    })
```

Rules:

- same Qwen family/targets/operator from same signature after failure -> suppress;
- after irrelevance -> demote/suppress exact repeat;
- after new transition evidence -> allow retry;
- after action surface change -> allow retry;
- after relation error change -> allow retry.

Tests required.

---

## 15. Game-Scoped Experience Memory

Records are exact-game scoped.

Requirements:

- retrieval requires same `game_id`;
- action-surface compatibility required;
- cross-game retrieval rejected;
- retrieved hint enters binder as raw hypothesis;
- invalid hint rejected;
- hint may affect router priority but cannot bypass verifier.

Telemetry:

```text
game_experience_query_count
game_experience_candidate_count
game_experience_hints_retrieved
game_experience_hints_bound
game_experience_hints_rejected
game_experience_prior_applied
cross_game_retrieval_rejected
```

---

## 16. First-Action Timeout Guard

Add per-stage timers:

```text
observation normalization
scene/object extraction
ARGA graph build
semantic serializer
LLM proposer
deterministic induction
binder
DSL compilation
route planning
candidate evaluation
rollback verification
debug serialization
```

Config:

```text
first_action_timeout_guard_s
first_action_max_candidate_programs
first_action_max_route_items
first_action_disable_llm_if_budget_low
first_action_disable_debug_heavy_serialization
```

If budget is nearly exhausted, route a verifier-authorized low-cost epistemic probe. This is not fallback action; it must pass manifest and verifier.

Tests:

- bp35-like expensive first observation returns under 30s;
- low-budget path skips LLM if not strict-required;
- no fallback action source appears.


### 16.1 LLM Context Budget Guard

In addition to first-action timers, LLM prompt construction must obey:

```text
llm_context_management:
  context_tokens: 8192
  max_input_tokens: 6000
  max_output_tokens: 512
  compression_strategy: normal | aggressive | minimal
  compression_trigger_ratio: 0.80
  fallback_to_structured_only: true
  note_summarization_enabled: true
```

When prompt size exceeds 80% of the configured input budget:

- summarize older previous feedback;
- summarize older persistent notes;
- reduce low-salience ARGA edges;
- reduce old transitions/action effects;
- keep top-N unresolved relations and relevant notes;
- preserve valid ids and action surface.

If budget remains too high, use `minimal` context strategy and log `llm_context_minimal_mode_used=True`.

---

## 17. Logging and Telemetry

Every step logs:

```text
hypothesis_mode
llm_priority_hybrid
llm_backend
llm_prompt_hash
llm_response_hash
llm_empty_output_on_nonempty_graph
llm_retry_used
qwen_useful_hypothesis_count
qwen_epistemic_test_count
bound_goal_counts_by_source
epistemic_counts_by_source
selected_hypothesis_source
selected_hypothesis_llm_confidence
selected_route_id
selected_graph_operator
selected_candidate_program_id
pure_symbolic_helper_score
verifier_status
semantic_judgment
rollback_observed_error_delta
observed_information_gain
failed_memory_match
irrelevant_memory_match
previous_feedback_count
first_action_stage_timings
```

---

## 18. Replay Requirements


Replay must include:

- LLM model profile and backend;
- LLM prompt hash and full prompt JSON after compaction;
- LLM context strategy and token budget state;
- retrieved semantic memory note ids and prompt summaries;
- LLM response hash and parsed output;
- fixed advisory replay record;
- binder result;
- DSL compilation result;
- router queue;
- rollback evaluation records;
- verifier verdicts;
- backreaction memory writes;
- semantic memory writes/summaries;
- emitted actions.

During replay, LLM calls and LLM-based summarization calls must not be repeated. Replay must load recorded advisory and summary records. A run that re-queries a nondeterministic model during replay is not a deterministic replay.


---

## 19. Testing Strategy

### 19.1 LLM and Prompt Tests

- fake model non-empty output on non-empty graph;
- invalid JSON rejected;
- direct actions rejected;
- unknown ids rejected;
- relation-focused retry triggered;
- prompt includes action surface and previous feedback.

### 19.2 Binder Tests

- valid Qwen proposals bind;
- missing relation inferred from object pair;
- missing object ids inferred from relation edge;
- fallback error functions attempted;
- hallucinations rejected.

### 19.3 DSL Compiler Tests

- affordance probe from coordinate action;
- bridge gap candidate generation;
- containment candidate generation;
- map projection epistemic fallback;
- no full-grid enumeration.

### 19.4 Router Tests

- LLM priority works;
- PureSymbolicRanker tie-break works;
- failed/irrelevant memory suppresses repeats;
- negative observed progress dominates confidence;
- router cannot emit actions.

### 19.5 Verifier Tests

- required/forbidden/irrelevant judgments;
- legal no-op classified as irrelevant;
- irrelevant not treated as forbidden;
- exact verifier remains final authority.

### 19.6 Integration Tests

At least one synthetic test demonstrates:

```text
ARGA graph -> LLM proposal -> binder -> DSL compiler -> router -> rollback -> verifier -> action -> backreaction memory
```

At least one test demonstrates irrelevant/no-op feedback entering next LLM prompt.

---

## 20. Validation Commands

Always run:

```bash
python -m compileall -q .
python -m pytest -q
```

Focused tests:

```bash
python -m pytest -q Code/tests/test_llm_semantic_advisor.py Code/tests/test_semantic_hypothesis_binder.py Code/tests/test_symbolic_ranker_v5_1.py Code/tests/test_semantic_trajectory_planner.py
```

Symbolic comparison:

```bash
python harness.py --environment-root environment_files --agent-module kaggle_agent --limit 3 --max-steps 64 --agent-timeout 30 --step-timeout 30 --stuck-threshold 0 --output harness_report_v6_symbolic_limit3_64.json --debug-bundle-dir debug_v6_symbolic_limit3_64
```

LLM-priority hybrid:

```bash
python harness.py --environment-root environment_files --agent-module kaggle_agent --limit 3 --max-steps 64 --agent-timeout 180 --step-timeout 180 --stuck-threshold 0 --output harness_report_v6_llm_priority_limit3_64.json --debug-bundle-dir debug_v6_llm_priority_limit3_64
```

Suggested local Qwen env:

```bash
ARC_HYPOTHESIS_MODE=hybrid
ARC_ENABLE_LLM_SEMANTIC_ADVISOR=1
ARC_LLM_PRIORITY_HYBRID=1
ARC_LLM_ADVISOR_BACKEND=qwen_local
ARC_QWEN_MODEL_PATH=Code/qwen/qwen2.5-7b-instruct-q4_k_m.gguf
ARC_QWEN_LLAMA_CLI_PATH=C:\arxiv\llama.cpp\build\bin\Release\llama-cli.exe
ARC_QWEN_LLAMA_DEVICE=Vulkan0
ARC_QWEN_GPU_LAYERS=99
ARC_QWEN_CONTEXT_TOKENS=2048
ARC_QWEN_MAX_OUTPUT_TOKENS=256
ARC_QWEN_TEMPERATURE=0
ARC_QWEN_STRICT_REQUIRED=0
```

---



## 20A. Sparse Terminal Progress Engineering

`TerminalProgressModel` must not rely only on dense metadata deltas. Many ARC/Kaggle-like environments expose no useful intermediate score; terminal feedback may be binary.

### 20A.1 Allowed Signals

The model may use:

```text
terminal_or_win_signal
score_or_counter_delta when present
action_surface_delta
exact_target_similarity_delta when a target/output proxy exists
relation_error_delta for terminal-linked hypotheses
object_graph_delta linked to selected candidate target
same_game_terminal_hint
near_terminal_signature_recurrence
```

### 20A.2 Abstention Rule

If no terminal signal or valid proxy exists:

```text
terminal_progress_evidence = "none"
terminal_progress_confidence = 0.0
```

The model must not infer terminal progress from arbitrary grid change.

### 20A.3 Proxy Evidence Weights

Recommended bounded weights:

```text
terminal_or_win_signal: 1.00
score_or_counter_delta: 0.90
action_surface_delta linked to progress: 0.45
target similarity delta: 0.40
terminal-linked relation error delta: 0.35
same-game terminal hint: 0.30
unrelated grid/object churn: 0.00
```

### 20A.4 Tests

- metadata terminal delta creates strong terminal-progress evidence;
- action-surface delta creates bounded evidence only when linked to a candidate;
- terminal-linked relation error reduction creates bounded proxy evidence;
- unrelated grid noise creates zero terminal progress;
- binary-only environment with no proxy evidence abstains.


## 21. Reports

Create/update:

```text
v6_llm_primary_semantic_proposer.md
v6_arga_state_assembler.md
v6_hypothesis_router.md
v6_trivalent_verifier.md
v6_verifier_backreaction_memory.md
v6_capability_conditioned_dsl.md
v6_integration_results.md
v6_findings.json
```

Reports must include:

- files changed;
- tests added;
- exact commands run;
- compile result;
- pytest result;
- symbolic comparison result;
- LLM-priority hybrid result;
- wins/errors/verifier_exhausted/max_steps;
- first 16 actions per game;
- LLM useful hypothesis counts;
- empty-output counts;
- bound goal counts by source;
- epistemic counts by source;
- route source distribution;
- verifier semantic judgment counts;
- `IRRELEVANT` counts;
- memory writes/hits/suppressions;
- prior failed/irrelevant feedback included in prompts;
- information-gain component summaries;
- prompt-tail ordering validation;
- sparse terminal-progress evidence/abstention counts;
- remaining blockers.

---

## 22. Acceptance Criteria

V6 implementation is acceptable only if:

- LLM is primary semantic proposer when backend is configured;
- ARGAStateSnapshot includes environment/action/failure context;
- LLM proposals are schema-validated;
- binder grounds proposals safely;
- DSL compiler converts hypotheses into manifest-legal programs;
- HypothesisRouter plans verification queue;
- PureSymbolicRanker is helper/fallback/tie-breaker;
- ExactVerifier produces three-valued judgments;
- `IRRELEVANT` is recorded, fed back, and not collapsed into `FORBIDDEN`;
- verifier backreaction memory is included in next prompt;
- no direct LLM action emission exists;
- no fallback action source exists;
- live failed/irrelevant memory affects routing;
- integration harness improves wins or produces exact blocker diagnosis;
- information gain is not based on raw grid delta;
- terminal-progress pressure abstains when only unrelated grid noise is available;
- prompt-tail priority is preserved under compaction.
