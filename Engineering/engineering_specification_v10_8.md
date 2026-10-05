# ARC-AGI-3 LCLD Agent
# Engineering Specification
# Version 10.8

## 0. Engineering Objective

Build an ARC-AGI-3 agent that:
- Implements Brusentsov's 4-valued logic of entailment for transition verification.
- Enforces strict tri-agent authority (Explorer, Coder, Solver) over distinct memory contours.
- Maintains dual-space coordinate tracking with a 1px boundary crop.
- Detects ephemeral multi-frame dynamics via a Transient Cells Engine.
- Resolves entity identity across frames using Jonker-Volgenant bipartite matching.
- Isolates fatal step deltas via Triangulated Defeat Architecture on `GAME_OVER`.
- Maintains a 5-block stratified memory and a `TransitionTable` world model.
- Operates under a hard per-level action budget and a dynamic priority scheduler.
- Includes a pure symbolic, state-aware Tabu fallback algorithm operating without environmental resets.

## 1. Repository Structure

Active module structure:

```text
src/
  kaggle_agent.py
  lcld_competition_child.py
  submission.py
  vllm_server_watchdog.py
  
  v10_agent/
    action_adapter.py
    action_guards.py
    action_semantics.py
    animation_analysis.py
    arga_lite.py
    brusentsov_logic.py
    config.py
    cycle_detector.py
    dsl_coder.py
    explorer_agent.py
    fallback_symbolic.py
    frame_diff.py
    frame_media.py
    judge.py
    llm_advisor.py
    memory_contours.py
    observe.py
    planning_set.py
    policy.py
    priority_scheduler.py
    sandbox.py
    session.py
    solver_agent.py
    symbolic_executor.py
    tracker.py
    trajectory.py
    types.py
    universal_invariants.py
    virtual_sandbox.py
    
    prompt_builders/
      coder_prompt.py
      explorer_prompt.py
      solver_prompt.py
```

## 2. Configuration Contract

The system configuration is defined by `V10Config`. Runtime settings must not exceed the defined bounds.

```python
@dataclass
class V10Config:
    llm_advisor_backend: str = "vllm"
    model_path: str = "Qwen/Qwen3.8-27B"
    context_tokens: int = 262144
    max_input_tokens: int = 131072
    max_output_tokens: int = 131072
    temperature: float = 1.0
    timeout_seconds: int = 700

    max_candidates_per_solver_package: int = 4
    max_steps_per_candidate: int = 30
    execute_one_step_at_a_time: bool = True

    enable_persistent_tracker: bool = True
    track_match_threshold: float = 0.45
    min_reliable_delta: float = 0.8
    enable_undecided_verdict: bool = True

    deadline_reserve_seconds: float = 15.0
    crop_border_pixels: int = 1

    max_actions_per_game: int = 500
    max_actions_per_level: int = 80
    max_chain_attempts_per_level: int = 5
    concurrency: int = 8
```

## 3. Core Data Types

### 3.1 Brusentsov Judgment

```python
@dataclass(frozen=True)
class BrusentsovJudgment:
    trajectory_id: str
    step_id: str
    verdict: Verdict | Ternary
    expected_propositions: PropositionSet
    observed_propositions: PropositionSet
    explanation: str = ""
    is_effective: bool = False
```

### 3.2 Transition Record

```python
@dataclass
class TransitionRecord:
    pre_grid_hash: str
    action_id: str
    coords: tuple[int, int] | None = None
    post_grid_hash: str = ""
    delta_cells: int = 0
    moved_object_ids: list[str] = field(default_factory=list)
    outcome_class: str = "EFFECTIVE"  # EFFECTIVE | IDLE_SELF_LOOP | LOSS | WIN
    observed_effect: str = ""
```

### 3.3 Defeat Exemplar

```python
@dataclass
class DefeatExemplar:
    level_index: int
    fatal_step: int
    fatal_action_id: int
    fatal_coords: tuple[int, int] | None = None
    actor_position_before: tuple[int, int] = (0, 0)
    hazard_color: int = -1
    fatal_step_diff: dict[str, Any] = field(default_factory=dict)
    fatal_transient_trajectory: str = ""
    valid_prefix_actions: list[str] = field(default_factory=list)
    environment_signal: str = "GAME_OVER"
```

## 4. Mathematical Logic Engine (`brusentsov_logic.py`)

### 4.1 Entailment Logic

```python
class Ternary(Enum):
    TRUE = 1          # FOLLOW: Necessary containment held
    FALSE = -1        # NULL: Hard physical contradiction
    IRRELEVANT = 0    # OMIT: Inessential / passive outcome

class Verdict(Enum):
    FOLLOW = "FOLLOW"
    NULL = "NULL"
    OMIT = "OMIT"
    UNDECIDED = "UNDECIDED"
```

### 4.2 Nullity Completeness
The `contradicts()` evaluation strictly enforces:
- Object identity failure (expected preservation, observed destruction).
- Physical stagnation (expected motion, observed stationary).
- Unintended mutation (expected invariant, observed motion).
- Directional inversion (expected and observed motion signs differ).

## 5. Perception and Animation Interfaces

### 5.1 Transient Cells Engine
Extracts intermediate micro-frames $f_0 \dots f_k$ during a step transition.
```python
def extract_transient_cells(
    chain: Sequence[Grid2D],
    ignore_peripheral_hud: bool = True,
) -> list[tuple[int, int]]:
    # Returns coordinates where Delta(r,c) >= 2
    ...
```

### 5.2 Coordinate Grounding
Forces `ACTION6` probes to strike literal pixels.
```python
def _select_on_mask_pixel(obj: Any) -> tuple[int, int]:
    # Selects physical obj.pixels closest to centroid.
    ...
```

## 6. Execution and Verification

### 6.1 8-Tier Judge Cascade
Every transition is evaluated in `judge.py` using a strict order:
1. **WIN**: Yields `FOLLOW`.
2. **GAME_OVER**: Yields `NULL`.
3. **Zero Delta on Motion**: If boundary collision $\to$ `OMIT`; if transient cells detected $\to$ effective action override; otherwise $\to$ `NULL`.
4. **Epistemic Ambiguity**: Yields `UNDECIDED`.
5. **EXPECT Contradiction**: Yields `NULL`.
6. **EXPECT Containment**: Yields `FOLLOW`.
7. **Unconfirmed Zero Delta**: Yields `UNDECIDED`.
8. **Action Effect Check**: If non-zero delta but empty/unverified expectations $\to$ `OMIT` (prevents vacuous `FOLLOW`).

### 6.2 Pre-Execution Edge Overlay
`SymbolicTrajectoryExecutor` checks the graph before emitting action step 0:
```python
if transition_table.is_known_idle_self_loop(current_grid_hash, action_id, coords):
    candidate.sever()
```

## 7. Session Orchestration

### 7.1 Triangulated Defeat Sequence
When `state == "GAME_OVER"`:
1. Capture $F_{alive}$ (pre-action frame) and $F_{fatal}$ (collision frame).
2. Compute `fatal_step_diff` isolated from level reset.
3. Emit single `RESET` command to engine.
4. Construct `DefeatExemplar` with `valid_prefix_actions`.
5. Replan trajectory preserving safe prefix.

### 7.2 Two-Tier Action Lifecycle
- `confirmed_effective_actions`: Demonstrated $\Delta > 0$ or transient animation.
- `conditional_candidate_actions`: $\Delta = 0$ on pristine frame $S_0$. Maintained as `CONDITIONAL_TRIGGER` affordances.
- Reactive Invalidation: Execution of any effective action missing from the Coder DSL manifest immediately invalidates the module and triggers a forced replan.

## 8. Remote Serving Infrastructure

Remote TPU v5e-8 serving runs the following canonical vLLM configuration to ensure deterministic 262K context handling and Speculative Decoding:

```bash
vllm serve Qwen/Qwen3.8-27B \
  --max-num-seqs 8 \
  --tensor-parallel-size 1 \
  --max-model-len 262144 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_xml \
  --mm-encoder-tp-mode data \
  --reasoning-parser qwen3 \
  --speculative-config '{"method":"mtp","num_speculative_tokens":5}'
```

Tunnels must enforce `--protocol http2` for environment stability.

## 9. Testing Strategy

Codebase validation requires passing the following core tests without side effects:
- **PBT Brusentsov Axioms**: Verify Ex Falso Quodlibet elimination and Carroll nullity logic across random proposition sets.
- **PBT Scale Invariance**: Validate invariant ARGA graph construction from $2 \times 2$ up to $64 \times 64$.
- **Transient Animation Unit Tests**: Validate micro-frame collapsing and geometric trajectory classification (beam, sweep).
- **Triangulated Defeat**: Verify decoupling of $F_{fatal}$ and $F_{reset}$ state differentials.
- **Action Budget Integration**: Verify system correctly triggers `LevelAttemptsExhaustedError` upon reaching `max_actions_per_level` (80) without generating a `RESET`.