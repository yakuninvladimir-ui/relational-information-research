# **The Continuous Python-Symbolic Agent (CPSA), Version 2.3: The Emergent Symbolic Layer at the Agent–Environment Interface**

**Author:** Vladimir Yakunin  
**Version:** 1.0 (specifies the CPSA 2.3 codebase)  
**Date:** 2026-11-02  
**Status:** Implemented, acceptance-tested architecture for ARC-AGI-3 (ARC Prize 2026). Implementation and acceptance evidence exist; certified benchmark results do not yet exist (§8).  
**Normative parent:** *Modified Brusentsov Entailment Logic and Four-Valued Verdict Calculus for External State-Control Systems* (`Reasoning/Modified_Brusentsov_Entailment_Logic.md`, cited below as *MBEL*). Where this document and the canonical specification differ in verdict semantics, the canonical specification governs.  
**Theoretical foundations:** *Boundary Projection Theorem* (`Reasoning/Boundary_Projection_Theorem.md`, cited as *BPT*); *Latent Agency Framework v2.1* (`Reasoning/Latent_Agency_Framework.md`, cited as *LAF*); *Unified Implementable Model v2.0* (`Reasoning/Unified_Implementable_Model.md`, cited as *UIM*); *Spectral and Matrix Realization of V₄* (`Reasoning/Spectral_and_Matrix_Realization_of_V4.md`, cited as *Spectral*).  
**Predecessor and contrast:** ARC-AGI-3 LCLD Agent specifications V10.9 (`Engineering/architectural_specification_v10_9.md`, `Engineering/engineering_specification_v10_9.md`).  
**Implementation:** [https://github.com/yakuninvladimir-ui/arc3-cpsa-agent](https://github.com/yakuninvladimir-ui/arc3-cpsa-agent) (MIT; builds on Tufa Labs *duck-harness*/TAAF and `da-fr/arc-agi-3-solution`).

---

## **Abstract**

This document specifies the architecture of the **Continuous Python-Symbolic Agent (CPSA)**, the second ARC-AGI-3 instantiation in this corpus, and records the paradigm shift it embodies.

The classical neuro-symbolic recipe **constructs** the symbolic layer: a designer fixes an ontology, a typed DSL, schemas, and a verification cascade, and the neural component must speak through them. CPSA inverts the recipe. Its central thesis is:

> **The symbolic layer for verification and control need not be artificial. It can arise naturally at the interface between the agent and its environment — here, as the Python sandbox through which the agent acts on the game.**

And its central method is:

> **Do not create new constraints. Formalize the constraints that are already available — and they almost always lie at the interface boundary.**

The interface between an LLM agent and an ARC-AGI-3 game already carries everything a verification layer needs: a single action channel, a deterministic environment, authoritative terminal signals, a quadratic action economy, animation micro-frames, and — on the agent side — Python itself, the symbolic system in which the model is natively fluent. CPSA adds no imposed ontology. Instead, the agent **writes its own world model as executable Python** (`simulate`, `project`, `is_goal`), and a deterministic Judge (**the V₄ Judge**, an instantiation of MBEL) certifies or falsifies that model by retrodiction against an append-only journal of actually observed transitions. The symbolic layer is therefore not a prerequisite structure but a **sediment of certified hypotheses**, produced by the agent, verified by the boundary, and retained across levels and deaths.

The architecture realizes, at the interface, the corpus theory: the four-valued verdict calculus and the Non-Promotion Invariant (MBEL); the boundary projection $`\pi_K`$, the kernel of insignificance, and the kernel-inclusion condition $`\ker\pi_K \subseteq \ker\pi_{\mathrm{env}}`$ (BPT); the authority separation and the factual commit boundary (UIM); loop closure, recoverability, and the write-back guard C2 (LAF). What changes relative to the constructed-layer design (LCLD V10.9) is not the logic of verification — it is the **locus and the production mechanism of the symbolic layer**.

---

## **0. Purpose and Scope**

### **0.1 What this document specifies**

This document is the architectural specification and paradigm record of CPSA 2.3 for ARC-AGI-3 interactive reasoning under:

- completely unseen interactive grid environments with hidden, environment-local mechanics;
- one scored run per game; a quadratic action economy with hidden human baselines;
- a local, frozen-weight LLM analyzer with no offline training phase and no weight updates;
- strict offline execution, hard action/time/token budgets, and a single tool — a sandboxed Python REPL;
- multi-frame transient dynamics, HUD timers, death/reset coupling, and level progression;
- four-valued verdict semantics (FOLLOW / OMIT / NULL / UNDECIDED) under the canonical specification.

It defines: the paradigm (§1); the interface contract that the architecture formalizes (§2); the system architecture — evidence layer, agent-authored world models, the deterministic V₄ Judge, the three-mode execution engine, guards, retention, consolidation, fleet scheduling (§3); the precise sense in which the symbolic layer is emergent rather than artificial (§4); invariants and test obligations (§5). Deployment specifics are excluded (§0.3, §6).

### **0.2 Relation to the LCLD V10.9 specifications**

The V10.9 Architectural and Engineering Specifications define the **constructed-layer** design: a deterministic ARGA-Lite perception engine, a typed DSL with manifest certification, three separated LLM call families (Explorer/Coder/Solver) with enforced isolation invariants, and an 8-tier verdict cascade designed in advance. Those documents remain the normative definition of the LCLD agent and are not superseded by this one; they are the necessary contrast class.

CPSA retains what V10.9 established as canonical — the authority separation (proposer ≠ judge), the four-valued verdict semantics, evidence scopes, non-promotion, guards-before-emission, clean handling of defeat — and changes **where the symbolic content comes from**: not from a designed perception/DSL stack, but from the agent's own Python code, certified against observed history at the interface. §4.4 fixes the comparison row by row. Both designs instantiate the same normative parent (MBEL); the paradigm shift is about the production of the symbolic layer, not about the logic of verification.

### **0.3 Normativity and exclusions**

Normative language: "must", "must not", "never" denote hard invariants enforced by the acceptance suite or by the sandbox/guard machinery. "Should" denotes a strong default varied only by configuration.

Excluded from this specification, as in V10.9 §0.3: concrete model artifacts, quantizations, serving engines and flags, accelerator topology, notebook packaging, and submission mechanics. These live in the deployment layer of the implementation repository (§6). The agent core is model-neutral: it resolves its LLM exclusively through an OpenAI-compatible endpoint contract and must run unchanged under any deployment satisfying it, including fake backends used by tests. The master flag `ARC3_CPSA` gates all CPSA behavior; with it off, the harness behaves as the unmodified base solution.

---

## **1. The Paradigm: Do Not Construct the Symbolic Layer — Formalize the Interface**

### **1.1 Two provenances of the symbolic layer**

A neuro-symbolic agent needs a symbolic layer: typed objects on which verification and control can operate deterministically. There are exactly two provenances for it.

**Provenance A — constructed (imposed from above).** The designer fixes the symbolic vocabulary in advance: a perception schema (objects, relations, roles), a plan/DSL language with a certification pipeline, message schemas for each cognitive role, and a verification cascade over the designer's predicates. The neural component proposes *inside* this vocabulary; the symbolic machinery checks proposals *against* it. This is the V10.9 design and the design of most neuro-symbolic systems in the literature.

**Provenance B — emergent (formalized at the boundary).** The designer fixes no domain vocabulary. The agent produces symbolic artifacts itself, in its own native symbolic medium (code), as hypotheses about the environment; the system supplies only (i) an honest record of what actually happened at the boundary and (ii) a deterministic judge that evaluates the agent's artifacts against that record under canonical verdict semantics. The symbolic layer is the growing set of certified artifacts. This is CPSA.

### **1.2 The costs of the constructed layer**

Provenance A pays four structural costs, none of them accidental:

1. **The translation tax.** Every observation and every plan must cross a representation boundary: pixels → typed objects → schema-conformant proposals → grounded steps. Each crossing is engineered, lossy, and a source of failure modes that have nothing to do with the task (schema violations, grounding failures, tracking ambiguity). V10.9 needs an immutable PlanningSet, a VerificationBinder, and twelve isolation invariants largely to police its own translation layers.
2. **Ontology lock-in.** The designer's kernel of insignificance is fixed before the environment is seen. But irrelevance is goal-indexed and environment-local (BPT §1; *Framework* §4.3): what is decoration in one game is load-bearing state in the next (a ticking HUD bar is a real budget in some games and noise in others). A pre-designed ontology is a pre-designed $`\ker\pi`$ — and there is no reason it should match the environment's.
3. **The brittleness of schemas at the frontier.** When the environment does something the ontology did not anticipate (transient beams, hidden counters, conditional triggers), the constructed layer can only mark it unrepresentable; the machinery of typed deltas degrades to "something changed".
4. **Role separation must be enforced, not lived.** With cognition partitioned into call families (Explorer/Coder/Solver), isolation is a discipline imposed by prompt walls and test-enforced invariants. The separation of powers exists because the designer built three boxes, not because the task has three joints.

### **1.3 The paradigm shift: constraints are discovered at the boundary, then formalized**

The CPSA thesis is that a verification layer does not need Provenance A, because **the interface already carries the constraints**. The design question changes from *"what symbolic structure should we impose?"* to *"what does the boundary already guarantee, and what is the minimal machinery that formalizes it?"*

At the agent–game boundary the following are already given, before any design decision:

| # | Available constraint (a fact of the boundary) | Formalization in CPSA |
| :-- | :--- | :--- |
| C1 | **Determinism.** The same action from the same state produces the same transition. | The transition journal is evidence, not sample: one observation per (state, action) is authoritative. Cycle guards treat repetition as zero-information (§3.8). The Judge's retrodiction is sound because history does not drift (§3.5). |
| C2 | **A single action channel.** Every effect the agent has on the world passes through one call (`action(...)` over one IPC path). | One chokepoint hosts guards, journaling, budget accounting, and refusals (§3.2). There is no second door to the environment; verification is total by construction, not by discipline. |
| C3 | **Authoritative terminal signals.** `game_over`, `level_completed`, `run_complete` are facts emitted by the environment, not inferences. | Terminal transitions carry model-free verdicts — `level_completed` ⇒ FOLLOW, `game_over` ⇒ NULL (terminal-metadata grounds, MBEL Definition 3.1; cf. Tiers 1–2 of the V10.9 cascade), as instantiated in `act_expect`/`act_checked`; `game_over` arms the death ledger and auto-falsification; `level_completed` triggers the consolidation turn (§3.10). |
| C4 | **A quadratic action economy (RHAE, §2.2).** Environment actions are scored $`\propto (b/n)^2`$ against hidden human baselines; thinking costs nothing. | The verification stack is organized by *environment cost*: inspection, `check_sim`, `search` cost zero actions; only committed steps spend. Guards refuse at zero action cost with the counterexample included (§3.8). "Think long, act little" is not advice; it is the price system of the interface. |
| C5 | **Observation includes intra-step dynamics.** One logical step may render multiple frames; transient effects leave no static trace. | The journal stores full animation chains; `act_expect` halts on hidden animation as UNDECIDED (a static zero-delta is not evidence of idleness) (§3.3, §3.6). |
| C6 | **Python is the model's native symbolic medium.** The LLM was trained on code; writing a transition function is not a translation for it — it is fluency. | The world model *is* Python source: `simulate`, `project`, `is_goal` as plain top-level defs, retained for the whole game (§3.4). No DSL to learn, no schema to satisfy, no grounding layer to police. |
| C7 | **Python is checkable.** Source code has an AST, an exception discipline, and executable semantics. | The sandbox whitelist is an AST-level contract; vacuous goals are detected by AST/bytecode inspection; certification is *execution against the journal*, not parsing against a schema (§2.4, §3.5). |
| C8 | **A finite context window and a shared compute budget.** The agent forgets; the fleet competes for one GPU. | Memory that must survive forgetting lives outside the context: journal on disk, invariant store, retained functions (§3.9). Compute budget is explicit, schedulable state: the priority gate rotates streams on measured progress (§3.11). |

None of the right column **adds a constraint on the agent's hypothesis space**. Each entry converts a boundary fact into machinery that keeps the agent's own claims honest. This is the operational meaning of "formalize what is available": the design work is a *reading* of the interface, not an *imposition* on it.

### **1.4 Why the interface is the canonical seat of verification**

The corpus theory says the same thing from three directions, which is why the paradigm is a shift *within* the framework rather than away from it:

- **BPT.** A verdict is the position of the observation confidence ball relative to a contract's kernel and target cone, and the contract is a *boundary operator* $`\pi_K`$ between the dynamics and the observer. Verification is not located in the agent's head or in the environment; it is generated **at the projection through the boundary** (BPT Theorem 2.1). A sandbox that sees every action and every resulting frame *is* that boundary; putting the Judge there is putting it where the theorem says verdicts are born.
- **LAF §8.** Two systems exchange structure through a low-dimensional channel; what is recoverable across the channel is governed by the kernel-inclusion condition $`\ker\Pi_{\mu b}\subset\ker\Pi_{\eta b}`$ — the receiver's boundary projection must not collapse distinctions the environment makes. CPSA's `project(frame)` is exactly a receiver-side boundary projection, and the Judge enforces kernel inclusion empirically (§3.5): the agent's abstraction is *certified admissible* precisely when it does not collapse real transitions. The recoverability bound says no amount of interaction rescues a violating kernel; the Judge therefore refuses to certify it instead of letting the agent plan on it.
- **UIM §§2.3, 11.** The authority hierarchy (Proposer / Verifier / Memory with no self-certification) and the factual commit boundary (predictions are PREDICTIVE_ONLY; only an accepted action followed by a trusted observation creates factual evidence) are boundary properties: the commit boundary *is* the interface crossing. CPSA keeps the hierarchy but stops building a symbolic apparatus around it — the boundary enforces it: nothing enters the journal except through the chokepoint (C2), and nothing enters the store as `[checked]` except through the Judge (§3.9).

The philosophical reading (*Framework* §4.3–§4.4, §6): the interface is the bilateral boundary $`\partial A`$ of the structuring triad, the substrate is the constraint envelope, and verification is the world's answer to the agent's claims. A constructed symbolic layer interposes a *designed* boundary between the agent and the world's answers; an interface-native layer lets the world answer directly, at the one place where its answers are already recorded.

---

## **2. The Interface: What the Agent–Game Boundary Already Provides**

### **2.1 Environment contract**

ARC-AGI-3 games (TAAF/`arcengine` runtime) are heterogeneous interactive grid games:

- **Observation:** frames of a logical grid up to 64×64 over the 16-color domain `0..15` (canonical characters `WwgGcBMPRbSYOrNp`); per-step results carry flags `level_completed`, `game_over`, `run_complete`, optional animation micro-frame chains, and the action surface (`available_actions`).
- **Action surface:** discrete `UP/DOWN/LEFT/RIGHT/SPACE` (engine `ACTION1..ACTION5`), coordinate action `MOUSE(row, col)` (`ACTION6`), optional `UNDO` (`ACTION7`, exposure-mode-dependent), and meta-action `RESET`. Actions are issued as strings/dicts through the sandbox's `action()` and normalized by the harness.
- **Structure:** a game is a sequence of levels; the run ends on victory or budget exhaustion; death resets the current attempt; level completion swaps the board (with a possible terminal animation frame, `pre_level_swap_grid`).
- **Epistemics:** mechanics, goals, and physics are unknown a priori and environment-local; nothing may be hardcoded per benchmark; human baseline action counts are hidden.

### **2.2 The scoring economy (RHAE)**

The scorecard (mirroring `arc_agi.scorecard`) is:

```math
\mathrm{score}(\ell)=\begin{cases}\min\!\Big(115,\ \big(\dfrac{b_\ell}{n_\ell}\big)^{2}\cdot 100\Big), & \text{level } \ell \text{ completed},\ n_\ell \ge 1\\[4pt] 0, & \text{otherwise,}\end{cases}
\qquad
\mathrm{final}=\min\!\Big(\frac{\sum_{i} w_i\,\mathrm{score}(i)}{\sum_i w_i},\ \mathrm{cap}(\text{completed})\Big),\quad w_i=i+1,
```

where $`b_\ell`$ is the hidden human baseline and $`n_\ell`$ the agent's spent actions. Consequences formalized by the architecture: every environment action is quadratically expensive, so **verification and planning must be relocated to zero-cost media** (sandbox compute); later levels weigh more, so **the world model is an investment good** (consolidation, §3.10); an incomplete level caps the whole game, so **cheap completion beats perfect exploration** (escalation ladder, §3.8); baselines are hidden, so **all thresholds must be par-free** (guards trigger on repetition and budget absorption, never on comparison to a baseline).

### **2.3 The single tool: a sandboxed Python REPL**

The agent (ToolAgent analyzer loop) has exactly one tool: `python`. Each tool call runs a model-written snippet in a **fresh isolated subprocess** (`sys.executable -I -S`, whitelisted builtins and modules, resource limits, timeout, JSON-lines IPC to the harness). Inside the snippet the model sees:

- `current_frame` (a `FrameView`: `.grid`, `.ascii`, `.segmentation`), `previous_frame`, `history`, `transitions`, `last_transition`, `valid_actions`, `death_ledger`;
- `action(...)`, the sole channel to the environment (C2), returning a structured result and refreshing all views;
- object-level `frame_diff()` and segmentation utilities;
- the CPSA API bound by the bridge (§3.1): `wmlib`, `SimFrame`, `act_expect`, `check_sim`, `search`, `act_checked`, `explore_frontier`, `save_invariants`, inspection/physics helpers;
- its own **retained functions**: top-level `def`s from previous snippets, re-executed source-first into every later snippet — the persistent body of the agent's growing world model (§3.4).

The sandbox is thus simultaneously: an execution environment (C6), a static-analysis surface (C7), a process-isolation boundary, and the recording station of the evidence layer (C1–C3). This dual nature — medium and boundary in one object — is the technical core of the paradigm: *the symbolic layer and the verification layer occupy the same place because the interface is where the agent's symbols meet the world's answers.*

### **2.4 Refusals as typed, unswallowable verdicts**

The action channel does not merely execute; it *answers*. Known-bad emissions are refused **before** the engine step (zero actions spent, C4) with typed exceptions:

- `KnownNoOpActionError`, `KnownDeathActionError`, `RepeatedActionInStateError`, `TerminalStateActionError`, `CpsaGuardRefusal` — derived from `BaseException`, so a defensive `except Exception:` (which models write routinely) cannot swallow a verdict; the refusal means the action *did not run*, so any code resting on it is already invalid. Each carries the counterexample and a way out, and (for guards) an armed override slot (§3.8).
- `StaleStateActionError` — deliberately a plain `Exception`: it reports a *belief* that may be stale (an epistemic warning, UNDECIDED-flavored), not a verdict on the action.

The exception taxonomy is the MBEL cascade expressed in the type system of the interface: certified incompatibility (NULL) is uncatchable-by-accident; epistemic ambiguity (UNDECIDED) is catchable and arguable. The distinction between the two exception bases is the distinction between verdict and controller signal (MBEL §4.1) made structural.

---

## **3. Architecture**

### **3.1 System map**

```text
┌────────────────────────────── ORCHESTRATOR (harness process; lives for the whole game) ─────────────────────────────┐
│                                                                                                                       │
│  ToolAgent (LLM analyzer loop; single `python` tool; context drainage; history)                                       │
│   ├─ CpsaHost (cpsa_host.py)                                                                                          │
│   │   ├─ CpsaJournalWriter      → cpsa_*/journal.jsonl + grids/*.npy     (SOLE WRITER of the evidence layer)          │
│   │   ├─ GameInvariantStore     → invariants.json    ([checked]/[assumed]; write-back guard)                         │
│   │   ├─ FalsifiedGoalLedger    → ledger.json        (goal black-list; runtime latch)                                 │
│   │   ├─ CpsaGuards             (cycle / click / sweep refusal + escalation ladder T1/T2/FLOOR)                      │
│   │   ├─ ReasoningLifecycleManager (keep-last-K pruning; amputation on falsification)                                 │
│   │   └─ consolidation control  (zero-cost turn on level completion; in-process Judge re-check)                       │
│   ├─ wiring: solver.action_guard_hook → host.guard_check     (refuse BEFORE the engine step)                          │
│   ├─ wiring: solver.cpsa_transition_hook → host.on_transition (journal EVERY executed step, incl. automatic resets)   │
│   └─ _PriorityGate (fleet level: N concurrent game streams, progress-ranked GPU/token allocation)                    │
│                                                                                                                       │
│  HarnessSolver (framework/solver.py) — owns the Game session; normalizes actions; terminal payloads; auto-RESET       │
└───────────────▲───────────────────────────────────────────────────────────────────────────────┬──────────────────────┘
                │ JSON-lines IPC: {"type":"action", ...} → guards → engine → journal → state     │
┌───────────────┴──────────────── SANDBOX SUBPROCESS (fresh per snippet; -I -S; whitelists) ────▼──────────────────────┐
│  model-written Python snippet  +  cpsa.sandbox_bridge.build(env):                                                     │
│   • loads wmlib / ledger / store from disk (journal_dir; disk is the source of truth — no megabytes over IPC)         │
│   • binds the world-model API to the live stepper: act_expect, check_sim, search, act_checked, explore_frontier       │
│   • mirrors every executed step into the in-snippet journal copy                                                     │
│   • wraps raw action() so all environment effects pass the same guarded, journaled path                              │
│   • returns final fields: hypothesis_falsified, falsification_reason, invariant_store_state,                          │
│     falsified_ledger_state, wmlib_summary  → CpsaHost.sync_from_sandbox                                              │
└───────────────▲───────────────────────────────────────────────────────────────────────────────┬──────────────────────┘
                │ frames, animation chains, terminal flags, action surface                      │ actions (sole channel)
┌───────────────┴──────────────────────────── ARC-AGI-3 GAME (arcengine) ───────────────────────▼──────────────────────┐
│  deterministic hidden mechanics; levels; HUD; death/reset; RHAE scorecard                                             │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

Ownership rules: the orchestrator is the sole journal writer (the sandbox mirrors locally for read-fast verification and reports deltas back); the sandbox is the only place agent-authored code runs; the game is reached only through the guarded chokepoint. State is not shuttled as JSON per snippet — **disk is the source of truth**; the IPC payload carries only `journal_dir` plus the current observation.

### **3.2 The single chokepoint: a guarded action channel**

Every environment action — from a raw `action("RIGHT")`, from `act_expect`, or from `act_checked` — traverses the same path:

```text
snippet call → IPC {"type":"action"} → orchestrator._handle_action
  → per-position guard checks (recomputed against the CURRENT board, so batch position N
    is judged on the state its predecessors actually produced)
  → engine step → terminal/animation capture → cpsa_transition_hook (journal write)
  → structured result back into the snippet → view refresh
```

Properties enforced here, each a formalization of a boundary fact (§1.3): refusals cost zero actions (C4); every executed step is journaled exactly once, including automatic post-death resets (C1–C3); guard checks are per-position and state-hash-based with a HUD-aware hash, so a ticking timer bar cannot blind repetition detection (C5, §3.3); terminal results latch the snippet (`TerminalStateActionError` on any later action) because the board a plan was computed against no longer exists (C3).

### **3.3 Evidence layer: the append-only transition journal**

`WorldModelLibrary` (`cpsa/wmlib.py`) plus the on-disk journal (`journal.jsonl` + `grids/*.npy`, orchestrator-written) record every transition as a `TransitionRecord`: unique monotonic `seq_id`, level, attempt, step-in-attempt, canonical action string, before/after grids (64×64 int), animation frames (lazy-loaded), `level_completed`, `game_over`, `automatic` flag, derived properties `is_noop`, `has_hidden_animation`, `pre_level_swap_grid`.

In MBEL terms: the journal is the ensemble $`\mathcal{T}`$ of transitions with scope `OBSERVED_TRANSITION`; nothing else is ever admitted (the Non-Promotion Invariant is structural — there is no API by which a simulated step could enter the journal). The journal is append-only; attempts and levels segment it; `win_transition(level)` isolates the single most valuable record in the game — the transition where the environment itself certified a goal.

**HUD isolation.** `compute_hud_mask` detects peripheral timer bars from the evidence itself: edge lines (rows/cols 0–1, 62–63) that tick by 1–4 px on ≥70% of active transitions with no bursts are classified as HUD and masked from change statistics. This is the paradigm in miniature: the HUD/gameplay distinction is not designed in — it is *measured* from the boundary's own regularities, per level, with cross-level inheritance on thin evidence. The HUD is then treated as what it is — real state (a budget bar), not decoration: `hud_report()` estimates remaining actions for search-depth bounding.

### **3.4 Agent-authored world models: SimFrame and boundary projection**

The agent formalizes a level's physics by writing plain top-level Python functions. Two representation options are offered, and the choice is the agent's, per level:

**Option A — full-grid Moore machine (`SimFrame`).** State = 64×64 grid + hidden `state` dict + `dead` flag. `simulate(frame, action)` returns the next `SimFrame`; hidden variables (counters, phases, keys) live in `frame.state`; `f.dead = True` marks a hazard; assigning `None` to a cell yields `UNKNOWN_CELL` — a **local abstention**: the model may declare "I do not predict this cell", which the Judge scores as UNDECIDED within a 15% budget (`MAX_UNKNOWN_RATIO`), never as FOLLOW. This is the four-valued semantics inside the representation itself: unknown is a first-class cell value, not an exception.

**Option B — boundary projection (quotient state, BPT).** The agent writes three functions:

```python
def project(frame):      # π_K: frame → hashable essential state (objects, counters)
def simulate(state, action):   # pure transition in the quotient; '_'-prefixed keys carry
                               # hidden Moore state across steps; state['_dead'] marks hazards
def is_goal(state):      # terminal condition in the quotient
```

The Judge verifies the **commutativity** of the diagram and the **kernel-inclusion** condition (BPT §3.2; LAF §8.3a):

```math
\pi_K\big(\mathrm{env}(s,a)\big) \;=\; \mathrm{simulate}\big(\pi_K(s),a\big),
\qquad
\ker\pi_K \subseteq \ker\pi_{\mathrm{env}}
\ \Longleftrightarrow\
\frac{\#\{\tau\in\mathcal{T}_{\mathrm{active}}:\ \pi_K(\tau.\mathrm{before})\neq\pi_K(\tau.\mathrm{after})\}}{\#\mathcal{T}_{\mathrm{active}}} \;\ge\; \theta_{\mathrm{cov}}=0.75 .
```

The second condition is the empirical form of "your abstraction must not collapse real transitions": a projector that maps genuinely changing boards to one state is rejected with `KERNEL INCLUSION VIOLATION`, regardless of how well it predicts. The `_`-prefixed hidden keys are the Moore-machine pull-through of Tycho §3.1 (Proposition 1): the observation need not contain the full memory (keys collected, switch phases, move parity), so latent state is threaded through `simulate` along the attempt and re-synchronized against the live board by `get_current_projected_state` before every search/execution.

**Retention.** Top-level defs (with explicit imports and immutable literal constants) are retained source-first for the whole game (`ARC3_PERSISTENT_FUNCTIONS_SCOPE=game`): the world model is a persistent, versioned-by-overwrite artifact — the agent's *relief* in LAF terms, written back at the boundary under certification (§3.9), not a per-turn message that context trimming can erase.

### **3.5 The deterministic V₄ Judge (`check_sim` / `evaluate_model`)**

The Judge is a pure function: journal + candidate model → verdict report. Zero environment actions, zero LLM calls, fully deterministic. For every recorded transition of the level it replays the model from the attempt's start state and scores each step in the canonical verdict space:

| Observed situation | V₄ count |
| :--- | :--- |
| predicted grid/state matches observation; real non-HUD change occurred | **FOLLOW** (+1) |
| prediction matches; no real change (idle/blocked step) | **OMIT** (0) |
| `simulate` returned `None` / abstained cells cover a real change / too many UNKNOWN cells | **UNDECIDED** (U) |
| mismatch on claimed cells, exception, unexplained real change | **NULL** (−1) |

Per-operator statistics yield the confirmation indicator of MBEL §3.4,

```math
\chi_{\mathrm{conf}}(a)=1 \iff \mathrm{FOLLOW}(a)\ge 1 \ \land\ \mathrm{NULL}(a)=0 \ \land\ \mathrm{UNDECIDED}(a)=0,
```

and its negative counterpart `unconfirmed_noop_operators` (OMIT>0, FOLLOW=0) — operators observed only as no-ops, which `search(strict_operator_confirmation=True)` prunes so that plans are not built on actions the evidence has never seen do anything (an ensemble-level guard against planning through hallucinated affordances).

**Prohibitions of vacuous truth** (MBEL Axiom 4.1 / `NonTriv(y)`; BPT §2):

- `FOLLOW = 0` on a level with active transitions ⇒ `VACUOUS MODEL VIOLATION` — an identity simulator that "predicts" no-ops everywhere cannot pass;
- `is_goal` that is a constant-False stub is detected **by AST and bytecode inspection** (`_is_trivial_false_goal`) ⇒ `GOAL CONTRADICTED` before any replay;
- **goal invariant:** `is_goal` must be False on every non-completing historical frame and True on the winning transition (`win_rec`), else `GOAL VIOLATION` / `WINNING TRANSITION VIOLATION`;
- `FalsifiedGoalLedger.validate_goal_candidate` rejects any goal hypothesis previously falsified at runtime (§3.6).

**Verdict tiers** gate Mode 3:

```text
PASS        : passed == total ∧ has_follow ∧ kernel_ok ∧ no goal violations ∧ no ledger rejection
ADVISORY-OK : not PASS ∧ has_follow ∧ kernel_ok ∧ no goal/ledger violations
              ∧ simulation_accuracy ≥ 0.85 ∧ active_acc ≥ 0.85 ∧ prediction_coverage ≥ 0.75
FAIL        : otherwise — search() raises RuntimeError("REJECTED BY JUDGE") unless
              allow_unchecked_goal (UNCHECKED tier, for frontier exploration only)
```

where `active_acc` = FOLLOW / (FOLLOW + UNDECIDED + NULL) — accuracy computed on the active ensemble only, so that padding the history with wall-bumps (OMIT) cannot inflate it (Tycho §4.3). The ADVISORY tier is the graded, non-perfectionist regime the RHAE economy demands: an ≥85%-accurate model may plan, because execution is guarded step-by-step (§3.6) and the guard converts residual model error into a zero-tail-loss counterexample instead of a wasted budget. **Cross-level transfer** is certified, not assumed: on Turn 0 of level L+1 the Judge may transfer physics certification from the most recent level where the same `simulate` passed — but `is_goal` is always re-validated against the new level's start grid (a goal that already holds at start is contradictory), preventing stale-goal certification.

### **3.6 The three-mode execution engine**

```text
 [frame + journal + store]
        │ verified model (simulate, is_goal[, project])?
   NO ──┴── YES
    │         │
    ▼         ▼
 MODE 1     MODE 3
 act_expect(actions, expect=Φ)          plan = search(frame, simulate, is_goal, project=…)
 every step checked against reality;    act_checked(plan, simulate, is_goal, project=…)
 first divergence HALTS, tail dropped   every step predicted before execution; first
 (0 wasted actions); typed counter-     divergence VOIDs the remaining plan; false goals
 example returned (diff_text)           are black-listed at zero cost
    │         │
    └────┬────┘
         ▼
 MODE 2 — check_sim(simulate, is_goal, project=…) : the V₄ Judge, 0 environment actions
```

**Mode 1 — guarded exploration (`act_expect`).** While the model is unverified, movement itself is an experiment: each action carries an expectation predicate (`expect_moved`, `expect_region_changed`, `expect_diff_count`, `expect_cells`, or any `(prev_f, curr_f, act, diff) → (ok, reason)` callable). After each executed step reality is compared to the expectation; on divergence the remaining tail is aborted **immediately** — the counterfactual tail costs zero actions — and the compact `diff_text` counterexample is returned. The halt taxonomy is the pointwise cascade in interface terms: `LEVEL_COMPLETED` ⇒ FOLLOW; `GAME_OVER` ⇒ NULL (+ auto-falsification into the store); unexpected no-op with a remaining tail ⇒ OMIT-halt (a no-op on the batch's final step is merely reported — there is nothing left to abort); hidden animation with zero static delta ⇒ UNDECIDED-halt ("a transient effect carries information your model is missing"); expectation violation ⇒ NULL-halt with counterexample.

**Mode 2 — formalize the physics (`check_sim`).** §3.5. The pivotal economic fact: hypothesis certification is **free**. The agent is pushed by the price system (C4) and pulled by the escalation ladder (§3.8) from acting-on-guesses to acting-on-certified-models.

**Mode 3 — search and guarded commit (`search` + `act_checked`).** `search` runs BFS (or A* with an agent-supplied heuristic) over `SimFrame`s or projected states, on the certified model: dead states are pruned (hazard pruning — the model's `f.dead`/`_dead` markings let the search see fatal branches without paying for them, Kepler §3.4); operator-confirmed action sets can be enforced; model tier is re-checked at entry (VERIFIED plans freely, ADVISORY plans under guard, uncertified models are rejected). `act_checked` then executes the plan under **predict-then-commit semantics**: before each step the simulator predicts the outcome; the step is executed; prediction and observation are compared; the **first divergence voids the remaining plan** (0 wasted actions) and returns the exact masked diff as counterexample, with the divergent transition already in the journal — the failure is instantly re-verifiable evidence. A goal hypothesis that fires on a non-completing board is recorded in the `FalsifiedGoalLedger` (`GOAL_FALSIFIED`): the transition is black-listed, subsequent `search`/`check_sim` calls reject the same goal at zero cost, and the agent is instructed to re-derive the objective from what actually changes at real level ends. The ledger is the runtime latch against goal hallucination: a falsified goal cannot be re-proposed by forgetting, because the refutation lives outside the context window.

This is UIM's two-phase execution and factual commit boundary (UIM §11), realized without a schema layer: the *pre-action phase* is simulation (PREDICTIVE_ONLY, never journaled as fact), the *commit* is the guarded step, and the *post-action verdict* is divergence checking against the trusted observation.

### **3.7 Zero-cost frontier exploration (`explore_frontier`)**

When the goal is unknown or `search` returns `None`, the architecture does not fall back to random probing. `explore_frontier` expands the certified model breadth-first (bounded by `max_depth`/`max_states`) and returns shortest action sequences that **trigger novel events**: modification of a previously untouched object color, adjacency to a static object, a change of a projected state key. These are zero-environment-cost subgoals — the LAF §5.2 loop-closure move: the agent uses its own model to choose the *informative* interactions it has not yet had, converting "search failed" into a menu of discriminating experiments (the same logic as Tycho §2.2's minimal discriminating probe: one action on which rival hypotheses diverge is worth ten confirmations).

### **3.8 Guards and the escalation ladder: formalized interface economics**

Orchestrator-side `CpsaGuards` refuse emissions **before** the engine step (zero actions spent), each guard a direct formalization of a boundary fact:

| Guard | Trigger (defaults) | Boundary fact formalized |
| :--- | :--- | :--- |
| Cycle guard | same (level, interior-state-hash, action) ≥ 3× | Determinism (C1): repetition cannot produce new information |
| Click guard | same `MOUSE(row,col)` ≥ 25× per level | C1 + C4: re-clicking a pixel is not an experiment |
| Sweep guard | ≥ 200 clicks inside one 4×4 block | C4: coordinate sweeps are quadratically punished |
| Reset-thrash | ≥ 6 self-resets with ≤ 40 distinct actions | C4: RESET restarts the attempt but spent actions still count |
| Terminal latch | action after `game_over`/`level_completed` | C3: the planned-against board no longer exists |
| No-op / death ledgers | action proven inert or fatal in a bit-identical state | C1: the journal already contains the answer |

Two design invariants make the guards epistemically safe rather than merely restrictive:

1. **Refusals carry counterexamples and ways out.** Every refusal message names the observed regularity, states that 0 actions were spent, and lists exits: update `simulate`/`is_goal`/`project` and run `check_sim` ("the mismatch you keep hitting IS the counterexample"); `search` a different route; inspect the journal's animation frames of unexplained transitions. The guard is a *teacher of the paradigm*, converting a grind into a modeling turn.
2. **Blocks are never self-sealing.** A refusal arms a single override slot: immediately re-issuing the exact same action executes it (costing one action). Rationale: a hidden-state mechanic (counter, cooldown, off-screen timer) would otherwise be foreclosed forever — once an action is on a hard block list, no contradicting evidence could ever arrive. The override preserves falsifiability of the guard itself; each insistence costs exactly one scored action, so the price system arbitrates.

**Escalation ladder.** Budget absorption itself is evidence (C4). At ≥120 actions on a level without completion, directive **T1** binds the agent to the paradigm: inventory unexplained journal entries *and* unvisited reachable states; if pixel-level simulation is hard, define a `project` quotient and certify it; plan via `search` + `act_checked`; spend single actions only as discriminating probes. At ≥250 actions (or reset-thrash), **T2** orders frontier enumeration under the model, re-derivation of any rule claiming unreachability, and inspection of animation frames of unreproduced transitions. At ≥400 actions, the **score-floor** directive states the RHAE arithmetic honestly (the level's points are largely gone) and re-allocates: finish with the cheapest verified plan, then invest the remaining budget into the world model that makes later, higher-weighted levels cheap.

### **3.9 Knowledge retention and the write-back discipline**

**`GameInvariantStore`** persists across deaths and levels: confirmed mechanics (each tagged `[checked]` or `[assumed]`), the win condition, falsified hypotheses & known hazards (capped list), per-level deltas ("what changed when this level started"). It is injected into the prompt every turn and survives any context drainage (guaranteed persistent-store injection) — the store is the part of memory that does not depend on the context window (C8).

**The write-back guard (Non-Promotion, hard-enforced).** A claim may be *tagged* `[checked]` by the agent, but the bridge downgrades the tag to `[assumed]` unless certification actually happened in this snippet's authoritative state: for mechanics — `check_sim` certified the model (PASS or ADVISORY-OK), or, absent a `check_sim` call, an observed FOLLOW exists (`act_expect` verdict or a non-no-op transition); for the win condition — an actually observed level win plus a goal the Judge did not contradict. This is MBEL §2.1's Non-Promotion Invariant and LAF §12's C2 write-back rule ("only externally certified corrections may be written back, otherwise recursion degenerates into self-confirmation") implemented as a property of the store's API — the agent *cannot* promote its own hypotheses, no matter what it writes. The prompt completes the discipline: never build multi-step plans on `[assumed]`.

**Auto-falsification.** `GAME_OVER`, expectation mismatches, simulator divergences, and falsified goals are recorded into `falsified_hypotheses_and_hazards` automatically (`record_auto_falsification`), independent of whether the agent remembers to save them: the negative evidence layer writes itself from the boundary (C3).

**`ReasoningLifecycleManager`.** Chain-of-thought is retained only on the last K=6 assistant messages, and **all** prior reasoning is amputated (rate-limited) when a falsification class fires (`EXPECTATION_MISMATCH`, `HIDDEN_ANIMATION`, `SIM_DIVERGENCE`, `GOAL_FALSIFIED`, `GAME_OVER`, `SIM_ERROR`). Justification: a counterexample invalidates the reasoning chain that produced it; keeping falsified chains in context re-infects subsequent proposals. The epistemic counterpart lives outside the context — journal, store, ledger — so amputation destroys no evidence, only discredited narrative. (KV-cache economics: destructive history mutation is flag-gated, `ARC3_CPSA_MUTATE_HISTORY_REASONING`, because prefix-cache hits are themselves a budget resource.)

### **3.10 The zero-cost consolidation turn**

Level completion is a natural boundary event (C3) and is institutionalized as a **reflection turn at zero action cost**: on `level_completed`, the orchestrator opens a consolidation window (`ARC3_CONSOLIDATION_TURN=1`, bounded turns) in which environment actions are *disabled* — any `action`/`act_expect`/`act_checked` raises `CONSOLIDATION_READONLY` — and the agent is instructed to crystallize the just-beaten level while its history is still hot in the journal: inspect `win_transition`, define/update `simulate`/`project`/`is_goal` until `check_sim` returns PASS, and `save_invariants(...)` with certified tags. The orchestrator independently re-verifies consolidation in-process (`check_level_consolidated` re-execs the retained sources against the same deterministic Judge — the certification does not trust the sandbox's word).

The consolidation turn is the architecture's answer to the "one scored run" regime: knowledge must transfer *during* the run, at the moments the boundary provides for free. A PASS-certified model on level L is, by the cross-level transfer rule (§3.5), immediately usable on level L+1 Turn 0 — planning before acting, at zero exploration cost, which is exactly where the RHAE economy wants the agent to be.

### **3.11 Fleet level: the priority gate (budget as explicit state)**

Competition runs execute a fleet of games (≈110 per submission) against one served model; a `_PriorityGate` admits at most `ARC3_MAX_ACTIVE_STREAMS` (16) analyzer streams and ranks waiting games by a par-free priority value built from boundary-observable quantities only: current level, action efficiency, empirically calibrated continuation-value tails (`TAIL_LOOKUP` from historical level-cost data), win-chance estimate, and token pace, with a monotonic **progress bonus** (proven depth is never demoted below shallower games by tail arithmetic — the CPSA 2.3 scheduler fix) and a final-level floor (a game one level from victory is never starved). Streams yield on token budget or context trim (`handover`), so GPU prefill/generation bandwidth flows to the games with the highest marginal expected score. This is the Self-Developing Runtime's principle — *computational resource as explicit, schedulable state* — applied at fleet scale: compute is part of the constraint envelope (C8), and the envelope is managed by the same doctrine: formalize the available signals (levels, actions, tokens), invent nothing.

---

## **4. The Emergence Claim: Why This Symbolic Layer Is Natural, Not Artificial**

### **4.1 Where the symbolic layer lives**

In CPSA the symbolic layer is the set of artifacts the agent itself has written and the boundary has certified:

```text
symbolic layer  =  { retained defs: simulate, project, is_goal, helpers }        (physics & abstraction)
                 ∪ { invariant store entries tagged [checked] }                    (certified facts)
                 ∪ { FalsifiedGoalLedger, hazard list }                            (certified refutations)
                 ∪ { the journal itself }                                          (grounding: certified transitions)
```

Every element is (i) authored by the neural component in its native medium, (ii) about *this* environment, discovered interactively, (iii) admissible only through the deterministic Judge or the boundary's own signals, and (iv) stored outside the context window. Nothing in this set was designed by the architect; the architect designed only the *admission rules* — and those rules are transcriptions of facts the interface already had (§1.3). In that precise sense the symbolic layer **arises naturally at the interface**: it is the residue of verified interaction, in the agent's own language, held in the boundary's own memory.

### **4.2 The Judge verifies claims, not representations**

The constructed-layer tradition verifies *conformance* (does the proposal match the schema?); CPSA verifies *claims* (does the model retrodict the observed history?). MBEL's verdict semantics is representation-agnostic — it scores transitions against expectations, whatever medium carries them — which is exactly what makes Provenance B possible: the canonical logic constrains the **verdicts**, leaving the **vocabulary** free. The only representation requirements the interface imposes are Python's own (plain top-level defs; hashable quotient states; no type annotations in retained signatures so source-retention stays conservative). The kernel of insignificance is not declared by a designer; each candidate `project` *proposes* one, and the kernel-inclusion coverage check certifies or rejects it per level (BPT's scale-compatibility condition, executed).

### **4.3 The growth loop**

The emergent layer grows by a fixed cycle, all arrows boundary-mediated:

```text
probe (act_expect, discriminating single actions)
  → record (journal; scope OBSERVED; animation chains; HUD-masked)
  → hypothesize (write/revise simulate, project, is_goal — plain Python)
  → certify (check_sim: V₄ retrodiction; PASS / ADVISORY-OK / FAIL)
  → plan (search: BFS/A* with hazard pruning on the certified model)
  → commit (act_checked: predict-then-execute; first divergence voids the tail)
  → falsify or confirm (counterexample → journal + store + ledger, automatically)
  → retain (retained defs; [checked] entries under the write-back guard)
  → consolidate (zero-cost turn at level end; certified model transfers to the next level)
```

Each iteration converts environment actions (expensive) into model structure (free to hold, cheap to plan with) — the agent's epistemic capital compounds, and the compounding is guarded at every write by the verdict calculus.

### **4.4 Constructed vs interface-native symbolic layer (comparison with V10.9)**

| Aspect | V10.9 LCLD (constructed) | CPSA 2.3 (interface-native) |
| :--- | :--- | :--- |
| Perception | Designed engine: ARGA-Lite components, JV-matched typed deltas, transient-cells classifier | Environment-native frames + agent-chosen abstractions (`objects_of`, `project`); HUD classified from measured regularities |
| World-model authorship | Coder agent emits modules in a typed DSL; certified by AST whitelist + manifest schema | The agent writes plain Python `simulate`/`project`/`is_goal`; certified by retrodiction against observed history |
| Kernel of insignificance | Fixed by the designer's ontology and schema versions | Proposed per level by the agent (`project`), certified by kernel-inclusion coverage |
| Plan representation | Declarative trajectory packages with `EXPECT:` propositions, grounded against an immutable PlanningSet by a Binder | Executable search over the certified model; plans are action lists committed under predict-then-check execution |
| Verification object | Schema-conformant proposals and typed transitions through an 8-tier cascade | The agent's own claims (code) against the journal, through the deterministic V₄ Judge |
| Role separation | Three LLM call families with enforced isolation invariants (ISO-1..12) | One analyzer; separation of powers is *structural*: proposer (LLM code) ≠ judge (deterministic) ≠ memory (append-only, boundary-written) |
| Memory | Stratified contours with schema'd exemplars and registries | Journal on disk + invariant store + retained source + ledgers; write-back guard enforces non-promotion |
| Failure handling | Severance, clean-RESET protocol, triangulated defeat, fallback A* engine | Zero-tail-loss aborts, auto-falsification, goal ledger latch, guards-with-override, escalation ladder into modeling |
| Cost of representation change | Re-specification: schemas, prompts, binder, tests (version increment) | None for the system: the agent changes its own representation; the Judge's contract is unchanged |

The rows are not a scorecard — V10.9 remains a coherent, fully specified design, and several of its mechanisms (guard-before-emission, defeat triangulation, HUD isolation) reappear in CPSA as boundary formalizations. The structural difference is the provenance column pair: **designed vocabulary vs certified claims**.

### **4.5 Economics: think long, act little**

The paradigm has a measurable economic signature. Under RHAE, environment actions cost quadratically and sandbox compute costs nothing; therefore the rational agent migrates its epistemic work — hypothesis testing, model revision, planning — into the free medium and spends the expensive medium only on (i) discriminating probes that the model cannot answer and (ii) long guarded commits that a certified model has already justified. Every architectural device points the same way: zero-cost Judge, zero-cost search, zero-tail-loss aborts, zero-action refusals, zero-cost consolidation, zero-cost frontier. The constructed layer, by contrast, spends its budget on maintaining its own translation machinery. **The interface-native layer is not merely more natural; under an action economy it is the cheaper place to think.**

### **4.6 What remains constructed (honest boundary of the claim)**

The claim is *not* "nothing is engineered". CPSA constructs: the Judge and its thresholds, the journal and store machinery, the guard taxonomy, the exception hierarchy, the consolidation protocol, the scheduler. The precise thesis is narrower and checkable:

1. The **semantic content** of the symbolic layer (objects, physics, goals, abstractions, plans) is not designed — it is agent-authored and evidence-certified. What the system contributes is admission rules, not vocabulary.
2. The admission rules are **transcriptions of boundary facts** (determinism, single channel, terminal signals, price system, animation, Python's checkability, finite context/budget) — each traceable to a constraint the interface already imposes (§1.3 table), not new restrictions on the hypothesis space.
3. The verdict **semantics** is inherited from the canonical specification (MBEL), representation-agnostically — so the emergent layer is judged by the same logic that judges the constructed one.

A symbolic layer satisfying (1)–(3) is *natural* in the sense the corpus requires: it is the world's answers, recorded at the boundary, in the agent's own symbols.

---

## **5. Invariants and Test Obligations**

### **5.1 Hard invariants**

- **ISO-C1 Single chokepoint.** No environment action except through the guarded `action()` IPC path; raw and guarded modes share it (`act_expect`/`act_checked` call the same stepper).
- **ISO-C2 Sole journal writer.** The orchestrator writes the authoritative journal exactly once per executed step (including automatic resets); the sandbox mirrors locally and reports state back; journaling never breaks a step (all hooks exception-isolated).
- **ISO-C3 Non-promotion.** Only `OBSERVED_TRANSITION` records enter the journal; simulated rollouts are never recorded as facts; `[checked]` tags require in-snippet certification evidence (write-back guard); PREDICTIVE_ONLY content never reaches persistent memory as factual.
- **ISO-C4 Vacuity prohibition.** FOLLOW=0 on active history ⇒ no PASS; constant-False `is_goal` ⇒ goal CONTRADICTED (AST/bytecode inspection); empty expectations never certify.
- **ISO-C5 Kernel inclusion.** Projected models are certified only with active-transition coverage ≥ θ_cov; commutativity is checked per transition, not assumed.
- **ISO-C6 Goal latch.** A goal falsified at runtime is black-listed in the ledger; Judge and search reject it at zero cost thereafter; the ledger persists on disk.
- **ISO-C7 Zero-cost refusal with override.** Guards refuse before the engine step; every refusal carries a counterexample, exits, and a single armed override slot; no block is self-sealing.
- **ISO-C8 Consolidation read-only.** During a consolidation turn, environment actions raise; the orchestrator re-verifies consolidation with the same Judge in-process.
- **ISO-C9 Determinism of the Judge.** `evaluate_model` is pure (journal + model → verdict); no I/O, no LLM, no environment; identical inputs yield identical reports; replayable.
- **ISO-C10 Model and deployment neutrality.** No benchmark IDs, no game-specific constants, no model-family branches in logic or prompts; the analyzer resolves through the endpoint contract; `ARC3_CPSA=0` restores baseline behavior exactly.
- **ISO-C11 Terminal authority.** Terminal flags are environment facts: post-terminal actions in the same snippet are refused; death arms auto-falsification and the death ledger; level completion arms consolidation.
- **ISO-C12 Par-free thresholds.** No guard, tier, or escalation may reference hidden baselines; all thresholds are repetition-, coverage-, accuracy-, or budget-based.

### **5.2 Acceptance suite**

`tests/test_cpsa_acceptance.py` (8 core acceptance tests + 17 regression tests) enforces, at minimum: `diff_text`/helper contracts; expectation predicates (`expect_cells`); journal round-trip (write → reload → identical library); guard behavior (corridor no-ops, cycle/click/sweep refusal, escalation text, zero-action-cost refusals, override arming); the ADVISORY tier arithmetic; bridge + consolidation lifecycle (read-only enforcement, in-process re-check); HUD detection and `hud_report`; redundant-RESET safety; FrameView/`_grid` compatibility and ARC color characters on non-zero backgrounds; **boundary-projection quotient mode with the kernel-inclusion check**; **vacuous-truth and UNDECIDED semantics (MBEL Axiom 4.1)**; `pre_level_swap_grid` correctness on 2-frame collapses; reasoning-key handling; the CPSA 2.1 regression set (11 groups); and the three MBEL/LAF-derived upgrades (per-operator χ_conf with strict-operator-confirmed search; write-back downgrade of uncertified `[checked]` claims; zero-cost reachable-interaction frontier). The suite runs on a synthetic deterministic 64×64 game — no model, no network.

**Divergence discovered during spec work — FIXED in place.** Re-executing the suite at the time of writing exposed one regression at HEAD `bb7728b`: `test_redundant_reset_no_typeerror` failed because the CPSA 2.3 re-activation of the unexpected-no-op halt in `act_expect` (audit defect №8) (a) did not exempt guard-skipped fake records (`_FakeRecord`, `action="SKIPPED"`, `seq_id=-1`, 0 spent actions, emitted by the redundant-RESET skip in `sandbox_bridge._step_and_mirror`) and (b) also fired on the *final* step of a batch, where no tail remains to abort — relabeling a fully consumed batch as `EXPECTATION_MISMATCH` and writing a bogus auto-falsification into the hypothesis store. Fixed in commit [`3516663`](https://github.com/yakuninvladimir-ui/arc3-cpsa-agent/commit/3516663ac3138adad5a8e2d15d193230c17a6d05): skipped records are now reported `SKIPPED by guard (0 actions spent)` and the batch continues; the no-op halt requires a remaining tail (`remaining_after > 0`), so mid-batch no-ops still abort exactly as defect №8 intended, while a final-step no-op is merely reported (CPSA 2.2 semantics). `act_checked` needs no patch — it has no changed-coords no-op halt; its predict-then-commit divergence check already covers no-ops. Suite status after the fix: **all 8 core acceptance tests + all 17 regression tests pass** (exit 0, re-executed 2026-11-02). Status of the mechanism: FOLLOW.

---

## **6. Deployment Instantiation (non-normative)**

The reference deployment (excluded from the normative contract per §0.3; see the implementation repository) runs the agent offline on Kaggle against the ARC Prize 2026 gateway: a local frozen-weight LLM analyzer served through an OpenAI-compatible endpoint (SGLang/vLLM class servers; the CPSA 2.2 lineage used a Qwen3.8-Flash-Next class model with FP4/MXFP8 mixed-precision weights on a single workstation GPU), ≈110 games under one scorecard within an ≈8 h 40 m envelope, 16 concurrent analyzer streams under the priority gate, context windows ≈128K with drainage, and the full guard/consolidation stack enabled by environment flags (`.env.example` documents every knob). The notebook lineage (`df-wm`), server bring-up, and submission mechanics are deployment-manifest material and deliberately not specified here.

---

## **7. Explicit Non-Claims**

1. **No certified benchmark result is claimed.** The architecture is implemented and acceptance-tested on synthetic environments; competition performance under the ARC Prize 2026 gateway is, at the date of this document, UNDECIDED (no certified scorecard run is recorded in the corpus).
2. **No claim that the interface-native paradigm dominates the constructed paradigm in general.** §4.4 is a structural comparison; superiority in score, sample efficiency, or robustness across domains requires paired evidence that does not yet exist (§8).
3. **No claim that the symbolic layer converges to a minimal sufficient representation.** The Judge certifies consistency with observed history, not optimality or minimality of the agent's abstraction; relating certified `project`s to informational minimal surfaces (*Latent Information Structuring*) is an open question.
4. **No general intelligence claim; no claim of learning.** Weights are frozen; all adaptation is external (journal, store, retained code) — the system is a bounded, auditable epistemic loop, not a training procedure.
5. **Guards and thresholds are formalized heuristics, not theorems.** Cycle/click/sweep counts, tier accuracies (0.85/0.75/0.15), and escalation budgets are calibrated defaults; their values are UNDECIDED in the absence of an optimization study, though their *existence* follows from the boundary facts they transcribe.
6. **The Judge's soundness is conditional on journal completeness.** Transitions the boundary does not report (e.g., effects hidden in unreported intermediate frames) are outside the evidence ensemble; the hidden-animation halt mitigates but does not eliminate this.
7. **No claim that Python is the unique natural medium.** The paradigm requires *a* medium that is simultaneously native to the proposer, checkable by the boundary, and executable against the evidence; Python is the instantiation available for LLM agents today.

---

## **8. Self-Assessment Under the Ternary Standard**

Statuses are attached to theses, not to the document (verdict semantics per MBEL §4).

| # | Thesis | Status |
| :-- | :--- | :--- |
| 1 | An interface-native symbolic layer is constructible and operational: agent-authored Python world models, certified by a deterministic V₄ Judge against an append-only journal, with guarded three-mode execution | **FOLLOW** — implemented; acceptance suite re-executed 2026-11-02: 8 core tests + all 17 regression tests pass on synthetic environments (the single divergence found during spec work was fixed in place — §5.2, commit `3516663`) (`arc3-cpsa-agent`, CPSA 2.3) |
| 2 | The constraints needed for verification and control are available at the agent–environment boundary and can be formalized without inventing new ones (§1.3 inventory C1–C8) | **FOLLOW** as a design doctrine demonstrated on ARC-AGI-3; each formalization is traceable to a boundary fact |
| 3 | The Judge instantiates MBEL verdict semantics (V₄ counts, non-promotion, vacuity prohibition, per-operator χ_conf, epistemic-vs-ontic refusal split) within its declared scope | **FOLLOW** as implementation conformance on the tested surface; full cascade equivalence beyond the tested surface is UNDECIDED |
| 4 | Boundary projection mode instantiates BPT: `project` = π_K, commutativity check, kernel-inclusion coverage ≥ θ_cov, OMIT-as-kernel semantics of idle steps | **FOLLOW** as implementation; the quantitative thresholds (0.75/0.85/0.15) are calibrated constants, not derived optima — UNDECIDED |
| 5 | The write-back guard enforces LAF §12 C2 / MBEL §2.1 non-promotion as an API property (self-certification is impossible, not merely discouraged) | **FOLLOW** — enforced in `save_invariants` and covered by acceptance tests |
| 6 | Zero-cost consolidation at boundary events (level completion) produces transferable certified models usable on Turn 0 of the next level | **FOLLOW** as mechanism (transfer certification is implemented and tested); its score contribution is UNDECIDED pending certified runs |
| 7 | The interface-native paradigm outperforms constructed-layer designs (e.g., LCLD V10.9) on ARC-AGI-3 under matched budgets | **UNDECIDED** — requires paired benchmark evidence; no certified head-to-head exists |
| 8 | Competition performance of CPSA 2.3 under the ARC Prize 2026 gateway | **UNDECIDED** — audits of the 2.2 lineage identified and fixed scheduler/consolidation/retention defects (2.2.1→2.3); no certified scorecard recorded in the corpus |
| 9 | The paradigm transfers beyond grid games (robotics, tool-use agents, self-developing runtimes) wherever a single guarded action channel and a native checkable medium exist | **UNDECIDED** — plausible by construction (§1.4), untested |
| 10 | Certified agent-authored projections relate to informational minimal surfaces (the emergent kernel approaches the goal-indexed optimal coarse-graining) | **UNDECIDED** — open theoretical question connecting CPSA to *Latent Information Structuring* |
| 11 | Claims that frozen-weight LLMs cannot maintain cross-level symbolic knowledge without imposed schemas | **NULL** — refuted by the retained-function + store + consolidation mechanism operating under frozen weights |

---

## **9. Relation to the Corpus**

- **MBEL** (normative parent): verdict space V₄ and dominance chain, two-tier verification (pointwise steps here; law-level confirmation via χ_conf and the store's `[checked]` lifecycle), evidence scopes, Non-Promotion Invariant, prohibition of vacuous truth (Axiom 4.1/`NonTriv(y)`), prohibition of epistemic falsification (UNDECIDED halts are retained as UNDECIDED, never rewritten into NULL).
- **BPT**: `project` as boundary operator π_K; the kernel of insignificance proposed by the agent and certified by kernel inclusion; the four-verdict theorem instantiated per transition; certified narrowing in the ADVISORY→PASS progression as the journal grows.
- **LAF**: loop closure and use (§5.2 → `explore_frontier`); recoverability and kernel-inclusion synchronization at the channel (§8 → Judge's coverage condition); write-back guard C2 (§12 → store downgrade); relief vs budget (§3.11 → priority gate); reasoning amputation as relief maintenance under falsification.
- **UIM**: authority hierarchy without schema layers; two-phase execution and the factual commit boundary (§3.6); recursive hypothesis revision driven by counterexamples; event-sourced memory (the journal).
- **Spectral**: the quotient transition graph and kernel-path equivalence are the discrete ancestors of `project`-mode search; tangent-space diagnostics remain out of scope here (the Judge is exact, not spectral).
- **LCLD V10.9 specifications**: the constructed-layer contrast class (§4.4); shared canonical logic; several mechanisms re-derived as boundary formalizations.
- **Self-Developing Runtime Research Program**: computational resource as explicit state (§3.11); controlled external verification of self-modifying artifacts — CPSA's retained-function growth under the Judge is a bounded, non-weight instance of the same principle.
- **Unified Informational-Constructive Framework**: §5 (engineering level), §4.3 (irrelevance as goal-indexed kernel — the agent proposes the kernel, the boundary certifies it), §6 (structuring triad: store/retained code = internal relief; sandbox IPC = bilateral interface ∂A; game = external channel).

## **References**

- [R1] V. Yakunin, *Modified Brusentsov Entailment Logic and Four-Valued Verdict Calculus for External State-Control Systems* (2026); this repository, `Reasoning/Modified_Brusentsov_Entailment_Logic.md` — canonical verdict semantics.
- [R2] V. Yakunin, *The Boundary Projection Theorem, the Kernel of Insignificance, and the Four-Valued Verdict* (2026); this repository, `Reasoning/Boundary_Projection_Theorem.md`.
- [R3] V. Yakunin, *Latent Agency Framework v2.1* (2026); this repository, `Reasoning/Latent_Agency_Framework.md`.
- [R4] V. Yakunin, *Unified Implementable Model v2.0* (2026); this repository, `Reasoning/Unified_Implementable_Model.md`.
- [R5] V. Yakunin, *Spectral and Matrix Realization of V₄ in Latent Spaces v2.2* (2026); this repository, `Reasoning/Spectral_and_Matrix_Realization_of_V4.md`.
- [R6] V. Yakunin, *ARC-AGI-3 LCLD Agent: Architectural / Engineering Specification V10.9* (2026); this repository, `Engineering/architectural_specification_v10_9.md`, `Engineering/engineering_specification_v10_9.md`.
- [R7] V. Yakunin, *Unified Informational-Constructive Framework* (2026); this repository.
- [R8] V. Yakunin, *Self-Developing Runtime Research Program v0.2* (2026); this repository, `Reasoning/Self_Developing_Runtime_Research_Program.md`.
- [R9] CPSA implementation repository: [https://github.com/yakuninvladimir-ui/arc3-cpsa-agent](https://github.com/yakuninvladimir-ui/arc3-cpsa-agent) — `inference/agent/cpsa/*` (wmlib, world_model, invariant_store, guards, journal, consolidation, helpers, prompts, sandbox_bridge), `inference/agent/cpsa_host.py`, `inference/agent/python_tool_sandbox.py`, `inference/agent/tool_agent.py`, `inference/framework/solver.py`, `tests/test_cpsa_acceptance.py`.
- [R10] *Tycho* (2026), arXiv:2607.28287 — Moore-machine world models for grid games; hidden-state pull-through in factor spaces (§3.1, Prop. 1); active-transition accuracy (§4.3); discriminating probes (§2.2).
- [R11] *Kepler* (2026), arXiv:2610.00834 — simulator-based lookahead with hazard pruning (§3.4); predict-then-commit execution semantics.
- [R12] Tufa Labs, *duck-harness* / TAAF (Tufa ARC-AGI Framework): [https://github.com/Tufalabs/duck-harness](https://github.com/Tufalabs/duck-harness) — evaluation stack and tool-harness base.
- [R13] D. Franzen, *arc-agi-3-solution*: [https://github.com/da-fr/arc-agi-3-solution](https://github.com/da-fr/arc-agi-3-solution) — base harness (Milestone-2 methodology) extended by CPSA.

---

## **Appendix A. Interface Primitives (quick reference)**

| Primitive | Mode | Environment cost | Contract |
| :--- | :--- | :--- | :--- |
| `action(a)` / `action([a…])` | raw | 1 action per step | sole channel; guarded; journaled; typed refusals |
| `act_expect(actions, expect=Φ)` | 1 | until first divergence | per-step reality check; typed halts; V₄-tagged result; tail void at 0 cost |
| `check_sim(simulate, is_goal, project=…)` | 2 | **0** | deterministic V₄ Judge; PASS / ADVISORY-OK / FAIL; goal & kernel checks |
| `search(frame, simulate, is_goal, …)` | 3 | **0** | BFS/A* on certified model; hazard pruning; tier-gated; frontier on failure |
| `act_checked(plan, simulate, is_goal, project=…)` | 3 | until first divergence | predict-then-commit; first divergence voids tail; goal falsification latches |
| `explore_frontier(frame, simulate, …)` | 3 | **0** | shortest sequences producing novel events (subgoal menu) |
| `get_current_sim_frame(simulate)` / `get_current_projected_state(project, simulate)` | — | **0** | re-synchronize hidden Moore state against the live board |
| `save_invariants(mechanics=…, win_condition=…, hazard_or_falsified=…, level_delta=…)` | — | **0** | persistent store; `[checked]` downgraded without certification evidence |
| `wmlib.transitions/win_transition/summary/hud_report/…` | — | **0** | read-only evidence queries |
| helpers: `objects_of`, `find_color`, `first_of`, `bg_color`, `move_object`, `move_by_action`, `tick_budget`, `phase_step`, `paint`, `manhattan`, `candidate_clicks`, `cells`, `bbox`, `colors`, `show_window`, `diff_text`, `expect_moved/region_changed/diff_count/cells` | — | **0** | composable physics/inspection primitives (dual color ontology: IDs 0..15 and ARC characters) |
| exceptions: `KnownNoOpActionError`, `KnownDeathActionError`, `RepeatedActionInStateError`, `TerminalStateActionError`, `CpsaGuardRefusal` (BaseException); `StaleStateActionError` (Exception) | — | **0** (refused) | verdicts vs epistemic warnings, made structural (§2.4) |

## **Appendix B. Repository Map**

```text
arc3-cpsa-agent/
├── inference/agent/
│   ├── cpsa/                    # the interface-native symbolic layer machinery
│   │   ├── wmlib.py             # transition journal, HUD detector, compact diffs
│   │   ├── world_model.py       # SimFrame, V4 Judge (evaluate_model), bound API
│   │   │                        #   (act_expect/check_sim/search/act_checked/explore_frontier),
│   │   │                        #   FalsifiedGoalLedger, expectation predicates
│   │   ├── invariant_store.py   # GameInvariantStore ([checked]/[assumed], write-back guard),
│   │   │                        #   ReasoningLifecycleManager (prune/amputate)
│   │   ├── guards.py            # cycle/click/sweep guards, escalation ladder T1/T2/FLOOR
│   │   ├── journal.py           # thread/process-safe on-disk journal (.jsonl + .npy)
│   │   ├── consolidation.py     # in-process re-verification of zero-cost consolidation
│   │   ├── helpers.py           # composable physics/object primitives; SIM_SKELETON
│   │   ├── prompts.py           # CPSA_SYSTEM_ADDENDUM; falsification & consolidation templates
│   │   └── sandbox_bridge.py    # glue executed INSIDE the sandbox; certification state
│   ├── cpsa_host.py             # orchestrator-side coordinator (sole journal writer)
│   ├── python_tool_sandbox.py   # isolated subprocess runner; whitelists; typed refusals
│   ├── tool_agent.py            # analyzer loop; single `python` tool; _PriorityGate
│   ├── priority_scheduler.py    # par-free priority value; tail lookups; progress bonus
│   └── noop_repeat_guard.py     # base no-op ledger with override semantics
├── inference/framework/solver.py# HarnessSolver: game session, guard hooks, journal hook
├── inference/utils/retained_functions.py  # source-only retention of top-level defs
├── taaf/                        # TAAF arcade/benchmark framework (base harness)
├── tests/test_cpsa_acceptance.py# acceptance suite: 8 core + 17 regression tests (synthetic game)
└── configs/, viewer/, run.py    # runner, replay viewer, evaluation configs
```

---

*End of document. Version 1.0 (CPSA 2.3). Feedback and objections — via repository issues.*
