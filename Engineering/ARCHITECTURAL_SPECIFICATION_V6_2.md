# ARC-AGI-3 LCLD Agent
# Architectural Specification
# Version 6.2

## 0. Purpose

This document defines the Version 6 target architecture for an ARC-AGI-3 interactive reasoning agent operating under:

- hidden environment rules;
- dynamic action spaces;
- interactive exploration;
- causal uncertainty;
- strict offline execution constraints;
- deterministic object-centric perception;
- ARGA-style semantic graph abstraction;
- local LLM semantic hypothesis generation;
- verifier-centered execution;
- rollback-safe verification;
- explicit three-valued semantic judgment including `IRRELEVANT`;
- external episodic memory and recursive verifier-backreaction loops.

Version 6.2 preserves the safety and replay guarantees of V5.1 but changes the intelligence hierarchy. V5.1 treated the LLM as an optional advisory layer. V6 makes the LLM the **Primary Semantic Proposer** whenever a local offline backend is configured. The verifier remains the **Primary Truth and Execution Judge**. Memory and backreaction form an explicit layer between them.

The architecture is **not**:

- an unrestricted LLM agent;
- an LLM-authorized action executor;
- a pure symbolic GOFAI solver;
- a raw-pixel policy;
- a generic RL learner;
- an unconstrained transformer planner;
- a hidden-state LLM controller;
- a heuristic-only action mapper.

The architecture **is**:

- a neuro-symbolic proposer/judge system;
- an LLM-as-Proposer, Verifier-as-Judge architecture;
- a deterministic ARGA-state-to-LLM context assembler;
- a strict capability-conditioned DSL compiler;
- a rollback-verified trajectory executor;
- an external-memory recursive reasoning loop;
- an offline, replayable, auditable ARC-AGI-3 solver.

### 0.1 V6 Authority Hierarchy

The normative authority hierarchy is:

1. **ExactVerifier and Three-Valued Semantic Judgment**
2. **Capability Manifest and Action Boundary**
3. **Stabilization, Rollback, Replay, and Snapshot Contracts**
4. **Verifier Backreaction and Task-Local Memory**
5. **ARGA State Assembler and Semantic Serializer**
6. **LLM Primary Semantic Proposer**
7. **SemanticHypothesisBinder**
8. **CapabilityConditionedDSLCompiler**
9. **HypothesisRouter Verification Queue**
10. **PureSymbolicRanker as Verifier Helper / Fallback / Tie-breaker**
11. **Program and Trajectory Search**

The LLM may propose semantic hypotheses, epistemic tests, capability questions, and graph-DSL intents. It may not emit final actions. It may not authorize execution. It may not revise manifest facts directly. It may not assign final semantic truth.

The verifier may accept, reject, or mark a proposal as irrelevant. `IRRELEVANT` is a first-class outcome, not a synonym for false and not a failure of reasoning.

### 0.2 V6 Core Loop

```text
Stable observation + action metadata
-> ARGAStateAssembler
-> deterministic object/action/graph JSON
-> memory and backreaction injection
-> LLM Semantic Proposer
-> strict schema validation
-> SemanticHypothesisBinder
-> CapabilityConditionedDSLCompiler
-> HypothesisRouter verification queue
-> rollback execution
-> ExactVerifier three-valued judgment
-> emit first verifier-authorized action if applicable
-> observe real transition
-> update transition graph, action effects, backreaction memory, failed-memory, capability constraints
-> next LLM prompt includes structured feedback from prior attempts
```

This loop is recursive, but the recursion state is external and replayable. The LLM is stateless across calls. All episodic memory lives in deterministic agent memory.


### 0.3 V6.1/V6.2 Amendment: Local Baseline, Persistent Structured Memory, and Context Discipline

V6.2 keeps three practical constraints to the V6 architecture:

1. **Model-neutral local baseline.** The reference local model profile is a modest offline GGUF model such as `qwen2.5-7b-instruct-q4_k_m.gguf`. The architecture must not depend on any specific model family, MoE behavior, cloud API, or reasoning-specialized model. Larger models may be used later through `LLMModelProfile` with minimal config changes.
2. **Persistent structured semantic notes.** The agent may keep persistent game-scoped, cross-level structured notes through `SemanticMemoryBuffer`. This is not hidden LLM memory. It is deterministic, replayable, bounded, importance-scored, and injected into prompts only through compact retrieved summaries.
3. **Strict LLM context budget management.** The LLM context is treated as a bounded resource. The prompt assembly pipeline must compact old transitions, old notes, low-salience graph details, and verbose feedback when context pressure rises. It must never drop valid ids, action surface, coordinate contract, current verifier feedback, active trajectory summary, or allowed output schema.

The baseline LLM is expected to provide useful semantic pattern recognition, not deep chain-of-thought reasoning. The prompt must therefore emphasize compact scene semantics, relation mappings, verifier feedback, and required JSON output rather than long reasoning instructions.



### 0.4 V6.2 Amendment: Verifier-Side Information Gain, Prompt-Tail Priority, and Sparse Terminal Progress

V6.2 adds three architectural rules:

1. **Observed information gain is semantic uncertainty reduction.** The verifier measures `information_gain_observed` as posterior entropy reduction over registered semantic variables. Raw grid change is evidence only when it updates a tracked semantic question.
2. **Prompt-tail priority is mandatory for local 7B models.** The most action-guiding sections must be placed at the end of the LLM prompt: previous feedback, candidate menu, current question set, allowed schema, and strict JSON instruction.
3. **Terminal progress is sparse-evidence aware.** Terminal progress may be estimated from metadata when present, but must also support bounded proxy evidence and abstain when the environment provides only binary final feedback and no valid proxy signal.


---

## 1. ARC-AGI-3 Environment Reality Model

ARC-AGI-3 environments remain heterogeneous:

- keyboard-only games;
- click-only games;
- keyboard+click hybrid games;
- coordinate-centric interaction games;
- sparse-action environments;
- partially observable interaction semantics;
- delayed passive transitions;
- camera offsets and viewport-relative interaction;
- level-local or game-local changes in action meaning;
- UI/counter/padding artifacts outside the logical playfield;
- multi-color, patterned, hollow, sparse, or sprite-like objects.

The architecture therefore assumes:

P1. Action semantics are environment-local.  
P2. Action availability is dynamic.  
P3. Interaction affordances must be inferred.  
P4. Control channels cannot be hardcoded globally.  
P5. Selection/reset/undo are optional capabilities.  
P6. Coordinate actions are first-class but semantically unassigned.  
P7. Sprite identity matters independently of raw geometry.  
P8. Stable-state evaluation is mandatory before final verification.  
P9. Raw observations are not directly equivalent to semantically stable state.  
P10. Connected components by color are insufficient for semantic object recognition.  
P11. Human-like visual abstractions must be proposed by LLM or deterministic semantic heuristics, then grounded.  
P12. Interactive world dynamics are represented by task-local transition evidence.  
P13. LLM reasoning must operate over deterministic semantic summaries, not uncontrolled raw state.  
P14. Verifier outcomes include REQUIRED/FORBIDDEN/IRRELEVANT semantic judgments.

### 1.1 Grid and Palette Contract

Normative logical-state constraints:

- logical grids are rectangular with `1 <= height <= 64` and `1 <= width <= 64`;
- logical grid cells use integer palette IDs in `0..15`;
- coordinate payloads use `x = col`, `y = row`, with payload bounds `0 <= x <= 63`, `0 <= y <= 63`;
- internal geometry uses row/column order;
- rendered RGB colors are not authoritative for solver logic;
- color names are debug-only;
- transparency/collision sentinels must be represented as layer/material metadata, not palette colors.

ARGA semantic graph construction, LLM serialization, DSL compilation, and verifier replay must preserve:

- `grid_shape`;
- `grid_source`;
- `palette_domain`;
- `palette_ids_seen`;
- `coordinate_order`;
- `grid_hash`;
- `semantic_graph_hash`.

### 1.2 Failure Modes to Prevent

V6 explicitly guards against:

- assuming ACTION1..ACTION5 correspond to movement or interaction semantics;
- assuming ACTION6 means click/select/place/shoot;
- evaluating unstable frames as final state;
- using coordinate actions without manifest validation;
- letting LLM infer or emit concrete actions;
- retrying a failed semantic proposal without new evidence;
- collapsing `IRRELEVANT` into `FORBIDDEN`;
- treating verifier acceptance as a utility function;
- treating LLM confidence as truth;
- overfitting one game's affordances into global priors;
- using PureSymbolicRanker as the primary intelligence engine;
- treating raw grid churn as information gain;
- treating unrelated visual changes as terminal progress;
- placing critical feedback/candidate-menu sections too early in a long prompt for local 7B models.

---

## 2. Version 6 Architectural Layers

```text
Raw Observation
-> Stabilization
-> Grid / Playfield Extraction
-> Deterministic Object-Centric Perception
-> Sprite and Pattern-Aware Object Canonicalization
-> ARGA-style Semantic Graph
-> Task-Local Transition Graph
-> Action-Effect Model
-> VerifierBackreactionMemory / TaskLocalTrajectoryMemory / CapabilityConstraintMemory
-> ARGAStateAssembler / Semantic Serializer
-> LLM Primary Semantic Proposer
-> SemanticHypothesisBinder
-> CapabilityConditionedDSLCompiler
-> HypothesisRouter
     uses: PureSymbolicRanker as helper/fallback/tie-breaker
-> Rollback Evaluation / DSL Execution
-> ExactVerifier Stack with three-valued judgment
-> Emit first verifier-authorized action
-> Observe real transition
-> Update memory and backreaction
```

### 2.1 ARGA Graph Is the LLM Substrate, Not the World Authority

The ARGA-style semantic graph represents:

- objects;
- attributes;
- internal patterns;
- graph nodes;
- graph edges;
- relation constraints;
- possible semantic roles;
- interaction affordance evidence.

It does not represent final semantic truth. It is the deterministic substrate that lets the LLM reason over a compact, canonical description of the scene and action surface.

Correct separation:

```text
ARGA graph = what is visible and structurally related.
Transition graph = how the world changed after actions.
LLM = what semantic hypotheses are worth trying.
Binder = which hypotheses are grounded in known ids and measurable errors.
DSL compiler = how abstract hypotheses become manifest-legal programs.
Verifier = what is legal, stable, replayable, required, forbidden, or irrelevant.
Memory = what failed, what was irrelevant, and what changed the manifest/affordance picture.
```

### 2.2 Advisory Layers Are Reclassified

V5.1 had advisory ranking layers. V6 splits them:

- **LLMSemanticProposer**: primary semantic hypothesis generator.
- **PureSymbolicRanker**: deterministic helper, verifier aide, fallback, and tie-breaker.
- **HypothesisRouter**: verification queue planner.

PureSymbolicRanker no longer owns primary policy selection. It remains useful for:

- measured-error ordering;
- repeated-state penalty;
- failed-memory penalty;
- information-gain scoring;
- cost/depth estimation;
- deterministic ablation;
- sanity checks for verifier queue ordering.

---

## 3. Three-Valued Semantics

V6 makes three-valued semantics central.

Every predicate, relation, affordance, hypothesis, DSL operator, trajectory, and verifier result passes through:

1. applicability evaluation;
2. epistemic resolution;
3. semantic judgment.

Final semantic judgment may be:

- `REQUIRED`;
- `FORBIDDEN`;
- `IRRELEVANT`.

`IRRELEVANT` means the hypothesis or predicate does not matter for the current state, goal, verification path, or interaction surface. It does not mean false. It is not the same as forbidden.

### 3.1 Applicability

Applicability states:

- `APPLICABLE`;
- `NOT_APPLICABLE`;
- `UNDECIDED`.

`NOT_APPLICABLE` usually maps to semantic `IRRELEVANT`, not `FORBIDDEN`.

### 3.2 Epistemic Resolution

Epistemic states:

- `RESOLVED`;
- `UNRESOLVED`.

`UNRESOLVED` is not a truth value. It means more evidence is needed.

### 3.3 Verifier Three-Valued Outcome

Verifier-level outcomes include:

```text
ACCEPT_REQUIRED       action/program/trajectory is legal and relevantly advances or tests the hypothesis
ACCEPT_IRRELEVANT     action/program/trajectory is legal but irrelevant/no-op/no useful semantic effect
REJECT_FORBIDDEN      action/program/trajectory violates capability, topology, reachability, replay, or manifest constraints
REJECT_UNSTABLE       evaluation was not stable/replayable
UNRESOLVED            insufficient evidence or budget to decide
```

For routing:

- `REJECT_FORBIDDEN` blocks the candidate and records a hard negative.
- `ACCEPT_IRRELEVANT` records a no-progress/irrelevance counterexample and usually suppresses equivalent retries.
- `ACCEPT_REQUIRED` or equivalent positive observed utility may produce an emitted action.
- `UNRESOLVED` may become an epistemic test if budget allows.

### 3.4 LLM and Three-Valued Semantics

The LLM may propose that a relation is likely relevant or likely irrelevant, but final tri-valued judgment belongs to verifier-backed ontology update logic.

LLM output may include an optional field:

```json
{
  "expected_semantic_judgment": "REQUIRED | IRRELEVANT | UNRESOLVED"
}
```

It must not output `FORBIDDEN` as a final fact. It may flag a risk that a proposal might be forbidden, which the verifier must check.



### 3.5 Observed Information Gain

`information_gain_observed` is part of semantic judgment. It is not raw state difference.

The architecture defines a set of registered semantic variables before evaluating an epistemic action or candidate program:

```text
Affordance(object, action)
Controllability(object, action)
ActionEffect(action, object_class)
RelationRelevance(edge)
HypothesisViability(hypothesis)
CapabilityConstraint(action, target_region)
TerminalProgress(candidate_family)
ActionSurfaceChange(action_surface)
```

Each variable has a finite domain and a prior distribution. After rollback/verifier evaluation, typed evidence updates the posterior. The observed information gain is normalized entropy reduction:

```text
IG_i = max(0, H_norm(P_before) - H_norm(P_after))
```

Aggregated information gain is weighted by semantic relevance and evidence linkage, then penalized for instability, repetition, and unrelated noise.

Architectural implications:

- legal no-op can be useful information only when it resolves a registered epistemic question;
- unrelated grid change is noise, not information;
- repeated equivalent no-op converges toward irrelevance;
- accepted action with no goal progress and no information gain is `IRRELEVANT`;
- information gain records must be replayable and auditable.


---

## 4. Capability Manifest and Action Ontology

The `EnvironmentCapabilityManifest` remains the central runtime contract.

Required fields include:

- `game_id`;
- `level_id`;
- `action_mode`;
- `available_actions`;
- `coordinate_actions`;
- `reset_available`;
- `undo_available`;
- `selection_available`;
- `action_payload_schema`;
- `dynamic_action_updates`;
- `observation_metadata`;
- `logical_grid_schema`;
- `palette_schema`;
- `playfield_schema`;
- `semantic_graph_schema`;
- `transition_graph_schema`;
- `llm_advisory_schema`;
- `backreaction_schema`;
- `trivalent_verifier_schema`.

### 4.1 Action Semantics

Actions are initially `UNINFERRED` unless proven otherwise. Action meanings are local to game/level/manifest scope.

State values:

- `UNINFERRED`;
- `PARTIALLY_INFERRED`;
- `RESOLVED`;
- `CONTRADICTED`.

ACTION1..ACTION5 may not be hardcoded as directions or verbs. ACTION6 is only the coordinate carrier `(x, y)` unless local evidence grounds a semantic effect.

### 4.2 Capability Constraints from Backreaction

Verifier failures and irrelevant/no-op outcomes create `CapabilityConstraintHypothesis` records, not immediate global manifest facts.

Example:

```json
{
  "constraint_type": "coordinate_no_effect_or_irrelevant",
  "action_id": "ACTION6",
  "target_signature": "button_like:shape_hash:...",
  "region_signature": "bbox_or_cell_region_hash",
  "verifier_judgment": "ACCEPT_IRRELEVANT",
  "evidence_count": 1,
  "scope": "current_level"
}
```

Only repeated, verifier-backed evidence may revise manifest/affordance constraints.

---

## 5. Stabilized Observation Model

Only `StableObservation` may enter:

- ontology updates;
- verifier evaluation;
- affordance induction;
- action semantics inference;
- semantic graph commits;
- trajectory continuation;
- irreversible planning commitments;
- replay judgment;
- LLM prompt context.

The system distinguishes:

- `RawObservation`;
- `RenderedObservation`;
- `LogicalGridObservation`;
- `TransitionalObservation`;
- `StableObservation`;
- `SemanticObservation`;
- `ARGAStateSnapshot`.

LLM prompt context must be derived from stable/canonical state, not transitional frames.

---

## 6. Object-Centric Perception Pipeline

Pipeline:

```text
stable observation
-> canonical grid/playfield extraction
-> palette normalization
-> sprite decomposition
-> pattern-aware connected components
-> ObjectSlot creation
-> sprite registry matching
-> object canonicalization
-> relation extraction
-> affordance estimation
-> ARGA semantic graph assembly
-> ARGAStateSnapshot serialization
```

### 6.1 ObjectSlot

Required fields:

- `object_id`;
- `sprite_id`;
- `bbox_rc`;
- `centroid_rc`;
- `area`;
- `colors`;
- `topology`;
- `internal_pattern`;
- `symmetry`;
- `holes`;
- `border_touching`;
- `semantic_tags`;
- `relations`;
- `controllability_score`;
- `affordance_scores`;
- `stable_identity_hash`;
- `uncertainty`.

`semantic_tags` are evidence hints for LLM and binder. They are not final truth.

### 6.2 PatternDescriptor

Required pattern classes:

- `solid`;
- `sparse`;
- `frame`;
- `hollow`;
- `checkerboard`;
- `horizontal_stripes`;
- `vertical_stripes`;
- `diagonal_hatch`;
- `custom_periodic`;
- `unknown_patterned`.

---

## 7. ARGA-style Semantic Graph

The graph contains:

- object nodes;
- region nodes;
- UI nodes when relevant;
- relation edges;
- affordance edges;
- transition-derived evidence edges;
- uncertainty annotations;
- canonical graph hash.

### 7.1 Required Edge Types

V6 edge types include:

- `same_color`;
- `same_shape`;
- `same_pattern`;
- `translated_shape`;
- `scaled_layout_similarity`;
- `aligned_row`;
- `aligned_col`;
- `near`;
- `touching`;
- `separated_by_gap`;
- `line_continuation`;
- `inside`;
- `contains`;
- `overlaps`;
- `frame_contains`;
- `mirror_candidate`;
- `rotation_candidate`;
- `repeated_pattern`;
- `guide_line_relation`;
- `button_like_structure`;
- `button_object_relation`;
- `unique_symbol_pair`;
- `affordance_relation`;
- `controllability_relation`.

### 7.2 Measurable Relation Errors

Any relation used to drive a goal trajectory must expose measurable error or be converted into epistemic testing.

Examples:

- centroid distance;
- bbox offset;
- mask overlap mismatch;
- reflected mask mismatch;
- rotated mask mismatch;
- endpoint gap;
- component disconnectedness;
- containment violation;
- hole count;
- unfilled region count;
- line continuation mismatch;
- scaled layout mismatch;
- affordance unknown;
- controllability unknown.

### 7.3 ARGA as LLM Context

The ARGA graph must be serialized as deterministic JSON for the LLM. The LLM receives:

- node ids;
- object ids;
- relation ids;
- relation types;
- measurable errors;
- semantic tags;
- action surface;
- unresolved relations;
- previous attempt feedback;
- memory hints.

The LLM must not receive uncontrolled, unbounded histories or mutable internal objects.

---

## 8. Semantic Serializer and ARGAStateSnapshot

### 8.1 Required Snapshot Fields

`ARGAStateSnapshot` includes:

```text
schema_version
session_id
game_id
level_id
manifest_hash
observation_hash
stable_state_hash
grid_shape
grid_contract
palette_ids_seen
grid_source
coordinate_order
action_surface_summary
available_actions
coordinate_action_ids
coordinate_payload_schema
coordinate_slots_or_targets
reset_available
undo_available
selection_available
object_slots
arga_nodes
arga_edges
relation_errors
current_bound_goals
current_epistemic_hypotheses
active_trajectory
last_3_to_5_transition_edges
last_3_to_5_action_effects
recent_verifier_rejections
previous_attempts_feedback
failed_trajectory_summary
failed_hypotheses_summary
unresolved_relations
game_scoped_experience_hints
persistent_notes_summary
semantic_state_signature
recent_irrelevant_attempts_summary
capability_constraint_summary
active_trajectory_prediction_vs_observed
llm_context_budget_state
allowed_output_schema
valid_object_ids
valid_relation_ids
valid_graph_operator_names
valid_error_function_names
```

### 8.2 Previous Attempts Feedback

Verifier and memory feedback must be formatted for the LLM as structured records:

```json
{
  "previous_attempts_feedback": [
    {
      "attempt_id": "attempt_001",
      "your_hypothesis": "ButtonLikeAffordance(node_7)",
      "compiled_program": "ACTION6 at node_7 centroid",
      "verifier_judgment": "ACCEPT_IRRELEVANT",
      "reason_code": "coordinate_no_semantic_effect",
      "observed_effect": "no semantic graph change",
      "semantic_error_before": null,
      "semantic_error_after": null,
      "instruction_to_llm": "Do not repeat this exact probe unless target/action/evidence changes."
    }
  ]
}
```

The feedback should be concise, deterministic, schema-versioned, and replayable.


### 8.3 Snapshot Compaction and Context Budget

`ARGAStateSnapshot` must expose a deterministic `compact(strategy)` operation.

Supported strategies:

- `normal`: preserve all high-salience objects/edges, recent transitions, recent backreaction, and top retrieved notes;
- `aggressive`: reduce low-salience objects/edges, summarize older feedback and notes, and keep only top-N relevant memory records;
- `minimal`: preserve only the current action surface, valid ids, top relations, unresolved questions, active trajectory, latest verifier feedback, and allowed output schema.

Compaction may remove detail, but must never remove:

- `valid_object_ids`;
- `valid_relation_ids`;
- `available_actions`;
- `coordinate_action_ids`;
- coordinate payload/schema information;
- current verifier/backreaction feedback;
- active trajectory summary;
- `persistent_notes_summary` when retrieved notes are relevant to current game/state;
- allowed output schema.

The LLM prompt builder must track estimated input tokens and switch to a stronger compaction strategy when context usage exceeds the configured threshold.

### 8.4 Prompt-Tail Priority

For local 7B models, broad context must not bury the most decision-critical records. The prompt order must put broad ARGA context first and the following sections last:

```text
previous_attempts_feedback
semantic_candidate_menu
current_question_set
allowed_output_schema
return_json_only_instruction
```

Compaction must preserve these tail sections before preserving low-salience graph detail.

---

## 9. LLM Primary Semantic Proposer

### 9.1 Role

The LLM proposes:

- `SemanticHypothesisProposal` records;
- `EpistemicTestProposal` records;
- `CapabilityQuestion` records;
- risk flags;
- possible graph-DSL operator intents.

The LLM does not propose final actions. It may reference existing action ids only inside capability questions or abstract action-surface analysis, never as final action commands.

### 9.2 Required Input

The input is `ARGAStateSnapshot` plus compact deterministic summaries. It includes scene structure, action surface, transition history, verifier feedback, failed memory, active trajectory, and unresolved questions.

### 9.3 Required Output Schema

```json
{
  "schema_version": "v6.semantic_proposals.1",
  "semantic_hypotheses": [
    {
      "proposal_id": "string",
      "family": "string",
      "target_object_ids": ["object_id"],
      "target_relation_ids": ["relation_id"],
      "semantic_role": "string",
      "expected_relation": "string",
      "requires_error_function": "string",
      "suggested_graph_operator": "string",
      "expected_semantic_judgment": "REQUIRED | IRRELEVANT | UNRESOLVED",
      "confidence": 0.0,
      "reason_code": "string"
    }
  ],
  "suggested_epistemic_tests": [
    {
      "proposal_id": "string",
      "test_family": "string",
      "target_object_ids": ["object_id"],
      "target_relation_ids": ["relation_id"],
      "information_gain_target": "string",
      "suggested_graph_operator": "string",
      "confidence": 0.0,
      "reason_code": "string"
    }
  ],
  "capability_questions": [
    {
      "question_id": "string",
      "action_id": "optional existing action id",
      "target_object_ids": ["object_id"],
      "question_type": "affordance | controllability | no_op | toggle | terminal | unknown",
      "confidence": 0.0
    }
  ],
  "risk_flags": []
}
```

### 9.4 Non-Empty Proposal Rule

If valid object ids and relation ids exist, the LLM must return at least one semantic hypothesis or epistemic test. Empty output on a non-empty graph is an advisor failure signal and may trigger one relation-focused retry.

Empty arrays are valid only when:

- no valid object ids exist;
- no valid relation ids exist;
- all candidate relations are invalid;
- the schema cannot be satisfied.

### 9.5 Prompt Priority Mappings

The prompt must tell the LLM to prioritize:

```text
unique_symbol_pair        -> SymbolPairAlignment / AlignNodeToNode / centroid_distance
button_like_structure     -> ButtonLikeAffordance / ProbeNodeAffordance / affordance_unknown
scaled_layout_similarity  -> MapProjection / InterpretMapProjection / scaled_layout_mismatch
separated_by_gap          -> BridgeGap / BridgeGap / gap_distance
line_continuation         -> ConnectionGoal or PatternCompletion / ExtendLineToTarget / line_endpoint_distance
frame_contains/contains   -> ContainmentGoal / MoveNodeIntoContainer / containment_outside_distance
same_shape                -> SameShapeAlignment / AlignNodeToNode / centroid_distance or mask mismatch
same_color                -> SameColorConnection / ConnectNodes / gap_distance or centroid_distance
```

### 9.6 Safety

LLM output is rejected if it:

- emits final actions;
- emits coordinates;
- invents object ids;
- invents relation ids;
- uses unsupported operators;
- uses unsupported error functions;
- includes chain-of-thought text;
- attempts manifest revision as fact.


### 9.7 Local Baseline Model Profile

V6.1 is model-neutral, but the reference local baseline is a modest offline instruction model profile:

```text
profile_id: qwen2_5_7b_instruct_gguf_baseline
backend: qwen_local | llama_cli | llama_server | ollama | fake
reference_model_file: qwen2.5-7b-instruct-q4_k_m.gguf
context_tokens_default: 8192
max_input_tokens_default: 6000
max_output_tokens_default: 512
temperature_default: 0.0
context_strategy_default: normal
```

The model is used for semantic proposal, not final action choice and not authoritative reasoning. It should receive compact deterministic state plus verifier feedback, and return strict structured hypotheses. Larger or different local models must fit behind the same `LLMModelProfile` interface without changing the architecture.

---

## 10. SemanticHypothesisBinder

The binder converts raw proposals into:

- `BoundGoalHypothesis`;
- `BoundEpistemicHypothesis`;
- `RejectedSemanticHypothesis`.

### 10.1 Binder Rules

A proposal may bind only if:

- target ids exist or are safely inferable from existing ARGA edges;
- operator is supported;
- error function is supported or safely defaulted;
- graph evidence exists;
- three-valued applicability is not `NOT_APPLICABLE`.

### 10.2 Aggressive but Safe LLM Binding

For high-confidence LLM proposals:

- if object pair is valid but relation id omitted, binder may attach best compatible ARGA edge;
- if relation id valid but object ids omitted, binder may infer endpoints;
- if error function omitted/`none`, binder may try family-default error functions;
- if grounding fails, reject with explicit reason.

Default fallback error functions:

```text
SymbolPairAlignment: centroid_distance, bbox_offset, mask_overlap_mismatch
SameShapeAlignment: centroid_distance, mask_overlap_mismatch, bbox_offset
SameColorConnection: gap_distance, centroid_distance
BridgeGap: gap_distance, line_endpoint_distance
ContainmentGoal: containment_outside_distance
MapProjection: scaled_layout_mismatch
ButtonLikeAffordance: affordance_unknown
ControllabilityProbe: controllability_unknown
```

### 10.3 Source Priority

Bound hypotheses carry:

- `source` = `qwen | fake | deterministic | experience`;
- `source_priority`;
- `llm_confidence`;
- `advisor_reason_code`;
- `semantic_judgment_hint`.

Priority does not override verifier or rollback-observed utility.

---

## 11. CapabilityConditionedDSLCompiler

The compiler turns bound hypotheses into manifest-legal candidate programs.

It is responsible for:

- mapping abstract graph operators to possible action programs;
- selecting coordinate targets from object-centric/affordance evidence;
- respecting manifest payload schemas;
- using task-local action-effect evidence;
- avoiding full-grid coordinate enumeration;
- producing rollback-evaluable programs;
- preserving hypothesis linkage.

### 11.1 Required Graph Operators

V6 compiler supports at least:

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

### 11.2 Coordinate Affordance Probes

If manifest exposes a coordinate action, `ProbeNodeAffordance` may generate coordinate candidates at:

- object centroid;
- bbox center;
- contour midpoint;
- button-like hotspot;
- relation target hotspot;
- guide-line intersection;
- region center.

All coordinate candidates must pass manifest validation and rollback + verifier evaluation.

---

## 12. HypothesisRouter

`HypothesisRouter` replaces PureSymbolicRanker as the primary verification queue planner.

### 12.1 Role

The router orders candidate hypotheses/programs for verification based on:

1. valid ids and manifest compatibility;
2. source priority;
3. measurable error or information gain;
4. memory suppression state;
5. LLM confidence;
6. ARGA relation salience;
7. expected verifier cost;
8. PureSymbolicRanker helper score;
9. exploration/diversity constraints.


### 12.1.1 Explicit LLM-Priority Hybrid Route Order

In `llm_priority_hybrid` mode, `HypothesisRouter` plans the verification queue in this order, after hard validity and manifest compatibility checks:

1. valid LLM proposal with measurable error, high confidence, and no failed/irrelevant-memory suppression;
2. valid deterministic or experience proposal with measurable error and strong rollback-observed progress evidence;
3. high-confidence LLM epistemic test with explicit information-gain target;
4. PureSymbolic measurable fallback with verifier-compatible utility;
5. generic exploration probes.

LLM confidence affects verification order only. It never overrides rollback-observed progress, verifier verdicts, tri-valued semantic judgment, failed-memory suppression, or manifest constraints.

### 12.2 Routing Rules

- Valid LLM proposals are processed before deterministic fallback in LLM-priority mode.
- Deterministic measurable errors may improve or repair LLM proposals.
- PureSymbolicRanker may reorder within a bucket but does not become the primary semantic source.
- Failed-memory suppression dominates LLM confidence.
- Negative rollback-observed progress dominates all priors.
- `IRRELEVANT` outcomes are recorded and suppress semantically equivalent retries.

### 12.3 PureSymbolicRanker Role

PureSymbolicRanker is retained as:

- verifier helper;
- deterministic fallback;
- tie-breaker;
- measured-error prioritizer;
- loop and failed-memory penalty provider;
- ablation mode baseline.

It must not be treated as the main semantic intelligence module.

---

## 13. ExactVerifier Stack

Verifier remains final authority.

Verifier modules include:

- `CapabilityVerifier`;
- `StabilizationVerifier`;
- `TransitionVerifier`;
- `TopologyVerifier`;
- `ReachabilityVerifier`;
- `ActionSemanticsVerifier`;
- `AffordanceVerifier`;
- `TerminalVerifier`;
- `ReplayVerifier`;
- `SemanticRelevanceVerifier`.

### 13.1 Three-Valued Verdict

Verifier returns structured verdicts:

```text
verdict_status: ACCEPT | REJECT | UNRESOLVED
semantic_judgment: REQUIRED | FORBIDDEN | IRRELEVANT | UNRESOLVED
reason_code
relevance_score
observed_information_gain
observed_error_delta
replay_status
stabilization_status
```

### 13.2 Verifier Backreaction

Every non-positive result creates a backreaction record:

- rejection records for forbidden/impossible actions;
- irrelevance records for legal but no-progress/no-op actions;
- unresolved records for insufficient evidence/budget;
- contradiction records for broken predictions.

---

## 14. Memory and Recursive Backreaction Layer

V6 explicitly places memory between verifier and next LLM prompt.

### 14.1 VerifierBackreactionMemory

Stores:

- hypothesis attempted;
- compiled program;
- verifier verdict;
- semantic judgment;
- reason code;
- observed effect;
- error before/after;
- information gain;
- next prompt summary.

### 14.2 TaskLocalTrajectoryMemory

Stores:

- failed trajectory signatures;
- irrelevant trajectory signatures;
- no-op probes;
- semantic state signatures;
- action sequence abstractions;
- failure/irrelevance reasons;
- retry conditions.

### 14.3 CapabilityConstraintMemory

Stores tentative constraints derived from repeated verifier/backreaction evidence:

- coordinate no-effect regions;
- blocked object signatures;
- action no-op under preconditions;
- action-surface changes;
- affordance confirmations;
- invalid target classes.

### 14.4 Memory to Prompt

The next LLM prompt includes compact memory summaries:

- previous attempts feedback;
- do-not-repeat hints;
- failed semantic ideas;
- irrelevant semantic ideas;
- newly confirmed action effects;
- newly contradicted action effects;
- unresolved capability questions.

Memory is task-local unless explicitly abstracted into non-task-specific priors.


### 14.5 SemanticMemoryBuffer

`SemanticMemoryBuffer` stores persistent structured notes. It provides OpenClaw-style persistent notes without depending on OpenClaw or hidden LLM state.

Scope rules:

- default scope is `game_id` scoped;
- notes may be reused across levels only inside the same game;
- cross-game retrieval is forbidden unless a note has been explicitly abstracted into a global non-task-specific prior;
- all retrieval must pass action-surface and manifest compatibility filters before semantic similarity is considered.

A semantic note contains:

```text
note_id
game_id
level_id | None
semantic_state_signature
note_type
summary
importance_score
confidence
evidence_refs
related_object_signatures
related_relation_types
related_action_ids
hypothesis_family
verifier_outcome
semantic_judgment
created_at_step
last_used_step
ttl_policy
replay_hash
```

Retrieval is deterministic by default using symbolic filters, tags, signatures, and relation/action family overlap. Optional in-memory FAISS/vector retrieval may be added as a secondary backend, but it must never bypass exact game/action-surface filters and must remain replayable through logged retrieval results.

### 14.6 Relevance Memory vs Failure Memory

`FORBIDDEN` and `IRRELEVANT` outcomes must be stored separately.

- `FailedTrajectoryMemory` stores verifier rejection, impossible transition, manifest violation, topology contradiction, and prediction mismatch.
- `IrrelevantAttemptMemory` stores legal but useless/no-op/no-information-gain attempts.
- `SemanticMemoryBuffer` stores compact persistent lessons and retrieved notes for the next LLM prompt.

An irrelevant attempt may suppress an exact repeated semantic idea from an equivalent semantic state. It must not globally ban an action id, coordinate region, object class, or hypothesis family.

### 14.7 Memory Context Injection

The next LLM prompt may include `persistent_notes_summary` and `previous_attempts_feedback`. Both must be compact, deterministic, and ranked by relevance and importance. Old notes are automatically summarized when the memory budget is exceeded. Summarization output must be replay-recorded if produced by an LLM.

---

## 15. Trajectory Planning and Rollback Evaluation

A trajectory includes:

- bound hypothesis;
- graph operator;
- candidate program;
- expected effect;
- predicted error curve;
- predicted information gain;
- rollback-observed error curve;
- verifier verdicts;
- three-valued semantic judgments.

### 15.1 Eligibility

Goal trajectory eligibility requires:

- manifest-legal steps;
- verifier acceptance;
- rollback-observed error decrease;
- no failed-memory suppression;
- no semantic irrelevance verdict.

Epistemic trajectory eligibility requires:

- manifest-legal steps;
- verifier acceptance;
- positive observed information gain or transition novelty;
- no failed/irrelevant equivalent retry.

Verifier acceptance alone is insufficient. Legal but irrelevant actions must be classified and remembered as such.

### 15.2 Active Trajectory Continuation

On the next observation, continuation requires:

- prediction match;
- observed error decrease or information gain;
- manifest compatibility;
- no new irrelevance evidence;
- verifier acceptance for next step.

If continuation fails, record exact backreaction reason and pass it to the next LLM context.

---

## 16. LLM Semantic Loop Prevention

Semantic loop prevention uses:

```text
semantic_graph_hash
action_surface_hash
active_hypothesis_family
recent_goal_families
recent_epistemic_families
palette_ids_seen
grid_shape
failed_or_irrelevant_attempt_signatures
```

Repeated LLM proposals from the same semantic state are:

- suppressed if previously forbidden;
- demoted if previously irrelevant;
- allowed if new transition evidence, changed action surface, or changed relation error exists.

---

## 17. Execution Loop

```text
initialize session
while not terminated:
    stable_obs = wait_for_stabilization()
    playfield = extract_playfield(stable_obs)
    objects = object_parser.parse(playfield)
    arga_graph = arga_builder.build(objects, manifest)
    transition_graph.update_from_last_real_transition(arga_graph)
    action_effect_model.update(transition_graph)
    memory_context = backreaction_memory.summarize_for_prompt()

    if active_trajectory exists:
        continuation = evaluate_active_trajectory(...)
        if continuation.accept_required:
            emit verifier-authorized next action
            continue
        else:
            memory.record_backreaction(continuation)

    snapshot = ARGAStateAssembler.build(
        arga_graph,
        manifest,
        action_effect_model,
        transition_graph,
        memory_context,
        unresolved_questions
    )

    llm_proposals = LLMSemanticProposer.propose(snapshot)
    deterministic_evidence = SemanticGoalInducer.annotate(snapshot)
    bound = SemanticHypothesisBinder.bind(llm_proposals, deterministic_evidence, memory)
    programs = CapabilityConditionedDSLCompiler.compile(bound, manifest, action_effect_model)
    queue = HypothesisRouter.plan_queue(programs, bound, memory, PureSymbolicRanker)

    for item in queue within budget:
        result = rollback_and_verify(item)
        memory.record(result)
        if result.accept_required_or_useful_epistemic:
            active_trajectory = maybe_start(item)
            emit first verifier-authorized action
            break

    if no item accepted:
        emit bounded verifier-authorized epistemic probe if available
        otherwise report verifier_exhausted with full evidence
```


### 17.3 LLM Replay Rule

If an LLM is used during live execution, every call must be replayable. Replay must not re-query the model. It must load the recorded prompt hash, prompt JSON, model profile, raw response hash, parsed response, schema validation result, binder result, and route usage from replay records.

A run that requires repeating nondeterministic LLM calls during replay is not considered deterministic replay.



## 17A. Sparse Terminal Progress Model

Terminal progress is not assumed to be densely observable.

In some environments the only terminal signal is binary success/failure at episode end. Therefore V6.2 terminal-pressure is advisory and evidence-bounded.

Allowed terminal-progress evidence:

```text
explicit terminal/win signal
score/counter delta when metadata exists
action-surface change linked to candidate
exact-target similarity delta if a target/output proxy exists
relation-error reduction for terminal-linked hypotheses
object/graph delta linked to selected candidate target
same-game terminal hints
near-terminal signature recurrence
```

Forbidden terminal-progress evidence:

```text
arbitrary unrelated grid delta
UI/debug-only noise
unlinked object churn
LLM-declared terminal progress without verifier evidence
```

If no valid signal or proxy exists, the model must abstain with zero confidence. Abstention is preferable to hallucinated progress.


---

## 18. Risk Model

### 18.1 LLM Proposal Risk

Mitigation:

- strict JSON schema;
- id grounding;
- binder validation;
- no action emission;
- relation-focused retry;
- memory feedback;
- verifier dominance.

### 18.2 Symbolic Overcontrol Risk

Mitigation:

- LLM-priority hybrid mode;
- PureSymbolicRanker downgraded to helper;
- HypothesisRouter owns verification queue;
- deterministic symbolic layer cannot suppress valid LLM proposal unless measured evidence justifies it.

### 18.3 Irrelevance Collapse Risk

Mitigation:

- explicit `IRRELEVANT` judgment;
- no-op and no-progress memory;
- prompt feedback distinguishes forbidden vs irrelevant;
- irrelevant paths are suppressed without claiming they violate physics.

### 18.4 Information-Gain Noise Risk

Mitigation:

- register semantic questions before evaluation;
- compute posterior entropy reduction;
- require evidence linkage;
- penalize unrelated grid/UI noise;
- suppress repeated equivalent no-op probes.

### 18.5 Terminal-Progress Hallucination Risk

Mitigation:

- use terminal metadata only when available;
- use bounded proxy evidence only when linked to candidate targets;
- abstain in binary-only/no-proxy states;
- never accept LLM-declared terminal progress without verifier-backed evidence.

### 18.6 Prompt Context Dilution Risk

Mitigation:

- prompt-tail priority;
- preserve candidate menu and previous feedback under compaction;
- place strict JSON schema at the generation edge;
- avoid long low-salience graph dumps before decision-critical records.

### 18.7 Verifier Backreaction Misuse

Mitigation:

- one failure does not globally revise manifest;
- constraints are scoped and evidence-counted;
- manifest updates require repeated verifier-backed evidence.

---

## 19. Acceptance Criteria

V6 architecture is acceptable only if:

- LLM is primary semantic proposer when local backend is configured;
- all LLM proposals pass schema validation and binder grounding;
- no LLM output can emit final actions;
- ExactVerifier remains final action authority;
- verifier supports forbidden/required/irrelevant semantics;
- irrelevant legal no-op actions are recorded and fed back to LLM;
- memory/backreaction is included in the next LLM prompt;
- HypothesisRouter plans verification queue;
- PureSymbolicRanker is retained only as helper/fallback/tie-breaker;
- GraphDSL operators compile to manifest-legal programs;
- coordinate probes are object/affordance-centered, not full-grid brute force;
- failed and irrelevant trajectory memory is active in the live path;
- all decisions are replayable;
- local harness demonstrates improved wins or produces exact blocker reports;
- `information_gain_observed` is verifier-stable entropy reduction over registered semantic variables;
- prompt-tail priority keeps feedback, candidate menu, questions, and schema at the end of LLM prompts;
- sparse terminal progress abstains when no valid proxy evidence exists.

---

## 20. Migration from V5.1 to V6

Mandatory migration changes:

1. Reclassify LLM Advisor as `LLMSemanticProposer`.
2. Introduce `ARGAStateAssembler` as the canonical prompt context builder.
3. Add `VerifierBackreactionMemory`, `CapabilityConstraintMemory`, and prompt feedback formatting.
4. Replace primary scalar ranking with `HypothesisRouter`.
5. Retain PureSymbolicRanker as helper/fallback/tie-breaker.
6. Add three-valued verifier outcomes and `SemanticRelevanceVerifier`.
7. Make `IRRELEVANT` a first-class outcome in memory, telemetry, and LLM feedback.
8. Implement CapabilityConditionedDSLCompiler as the bridge from bound hypotheses to programs.
9. Strengthen LLM prompt and schema so non-empty ARGA graphs produce useful hypotheses or epistemic tests.
10. Ensure all candidate programs are still rollback-evaluated and verifier-authorized.
