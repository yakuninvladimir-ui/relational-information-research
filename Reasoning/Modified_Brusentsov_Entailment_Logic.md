# **Modified Brusentsov Entailment Logic and Four-Valued Verdict Calculus for External State-Control Systems**

**Document Status:** Canonical Formal-Logical Specification  
**Role in Repository:** Canonical formal-logical foundation of the corpus. Documents that define or instantiate ternary statuses, entailment semantics, or the verdict space (`FOLLOW` / `OMIT` / `NULL` / `UNDECIDED`) cite this specification as normative; domain instantiations (Unified Implementable Model v2.0, External Ternary Judge Adapter, ARC-AGI-3 LCLD Agent V10.9, Self-Developing Runtime Research Program) may refine operational mappings but must not contradict §§1–5 of this document.  
**Domain:** Non-classical mathematical logic, state-transition verification theory, neuro-symbolic and agentic architectures with authority separation (*Propose — Judge — Commit*).

---

## **Abstract**

In standard generation and planning loops, machine learning models may fail to maintain a formal boundary between a plausible prediction and a certified state transition: an unverified hypothesis or intermediate reasoning step can enter the mutable working context and influence subsequent tool calls, physical actions, and long-term memory writes [21–24]. Classical two-valued Boolean algebra and material implication are unsuitable as a verification semantics for such transitions because they conflate the non-applicability of a rule with its confirmation (*vacuous truth*) and fail to distinguish logical incompatibility (exclusion) from incidental inessentiality [8, 10].

This document specifies a formal verification calculus extending N. P. Brusentsov’s three-valued algebra of contentful consequence [3–8] and Lewis Carroll’s method of indices [2]. It separates pointwise transition assessment from ensemble-level law assessment and distinguishes fulfillment, neutral indifference, incompatibility, and epistemic uncertainty. It defines an operational verdict space, evidence certificates, metric and geometric instantiations, and hierarchical graph coarse-graining. Formal guarantees are stated together with their operational assumptions: in particular, the pointwise cascade is the normative decision procedure, semilattice aggregation is proved equivalent to the cascade (Proposition 4.2), law statuses are computed on reliably grounded transitions only, and rollback guarantees apply to logged logical state unless external effects are transactional or compensated.

---

## **0. Canonical Notation Table**

Every symbol family used in this specification is assigned a distinct role across all sections:

| Symbol | Mathematical Object |
| :--- | :--- |
| `X, O, 𝒜` | Latent state space, observation space, and global action (or semantic move) space |
| `Σ_t = (𝒜_t, κ_t)` | Available action surface `𝒜_t ⊆ 𝒜` and mode/capability/resource metadata vector `κ_t` at step `t` |
| `ō_t = (o_t, Σ_t, meta_t), H_t = ψ(ō_t) ∈ H` | Trusted observation packet at step `t` (frame, action surface, synchronization telemetry `meta_t`) and its deterministic structural descriptor in state-descriptor space `H` |
| `𝒮_t^+ ⊆ H_t` | Certified active state projection committed to state memory at step `t` |
| `τ_t = (seq_t, ō_t, act_t, ō_{t+1})` | Single state transition at step `t` with unique monotonic sequence identifier `seq_t ∈ ℕ` and executed action `act_t ∈ 𝒜_t` |
| `𝒯, 𝒯_{t-1}, 𝒯_rel(Λ) ⊆ 𝒯` | Deduplicated ensemble (set keyed by `seq_t`) of authoritatively observed transitions, its prefix ensemble prior to ingesting `τ_t`, and its subset where law `Λ` is reliably grounded (`Rel = 1`) |
| `σ(τ_t), ϖ_t` | Evidentiary scope of transition `τ_t` and pending transition token registered before action emission |
| `a ∈ {0, 1}, A ∈ {0, 1}` | Atomic Boolean indicator of tested operator activation (`a' = 1 - a`; `a(τ_t) = 1` iff `act_t` is the tested operator) and compound antecedent `A = a_1 ∧ ... ∧ a_k` |
| `c ∈ {0, 1}, C ∈ {0, 1}` | Atomic Boolean indicator of unobstructed admissible precondition context (`c' = 1 - c`) and compound context `C = c_1 ∧ ... ∧ c_r` |
| `s, F, φ_exp` | Target subject identifier `s`, feature family `F`, and expected change predicate (admissible target set) `φ_exp` |
| `Alive(s, ō_t), Alive(s, ō_{t+1}), ι_s` | Explicit before/after subject-presence predicates and identity requirement `ι_s ∈ {PRESENT, ABSENT, PRESERVE}`; identity violations are not inferred from an undefined feature delta |
| `δ_obs(s, F; τ_t), 𝛅_exp ∈ ℝ^d` | Observed change of feature `F` on subject `s` during `τ_t` (vector-valued `𝛅_obs ∈ ℝ^d` when `F` is `d`-dimensional, with zero element `𝟎`, where `𝟎 = 0` in 1D/discrete scalar spaces), and reference expected displacement vector `𝛅_exp` |
| `ε_rev, ε_orth ≥ 0` | Sign-inversion noise tolerance along active axes and leakage tolerance along orthogonal invariant axes (`ε_rev = ε_orth = 0` on discrete grids) |
| `y^+, y^∼, y^⊥ ∈ {0, 1}` | Mutually exclusive indicators of consequent fulfillment (`+`), neutral indifference (`∼`), and strong incompatibility (`⊥`) |
| `y^∼_stag, y^∼_sub ∈ {0, 1}` | Disjoint sub-indicators of `y^∼`: strict zero-delta stagnation (`δ_obs = 𝟎`) and non-zero change inside a contract-declared bounded neutral region |
| `Ω_{sub,k} ⊆ ℝ^d ∖ {𝟎}` | Explicitly bounded, clause-specific set of non-zero changes permitted as neutral/sub-threshold; it must be stated in the contract and is empty by default |
| `(·)_1, (·)_0` | Carroll–Brusentsov indices: mandatory empirical existence (`1`) and incompatibility / *nullity* (`0`) [2, 8] |
| `N_min ∈ ℕ, η_tol ∈ [0, 1)` | Minimum empirical support threshold (`N_min ≥ 1`) and observation noise tolerance in ensemble quantifiers |
| $`\mathbf{V}^{(N_{\min})}_{\mathcal{T}},\mathbf{N}^{(\eta_{\mathrm{tol}})}_{0,\mathcal{T}}(\Psi\mid\Gamma_{\mathrm{cond}})`$ | Generalized Carroll–Brusentsov existence and conditional nullity quantifiers over reliably grounded transitions in `𝒯` with conditioning event `Γ_cond` |
| `Λ = (AC ⇒ y), χ_conf(A, F; 𝒯), χ_conf(A, F; 𝒯_{t-1})` | Universal law over `𝒯` and Boolean indicator that operator `A` is confirmed for feature family `F` on `𝒯` (evaluated on `𝒯_{t-1}` when judging `τ_t`) |
| `Ob_effect, Ob_safety` | Ensemble-level and step-level obligations for unobstructed effect fulfillment (`AC = 1`) and obstructed non-destructiveness (`AC' = 1`) |
| `Ω_y ⊊ Ω_𝒰` | Feature acceptance region of consequent `y` and ambient feature universe in the non-triviality predicate `NonTriv(y)` |
| `E = E_act ⊔ E_inv` | Bound step expectation set `E = {e_1, ..., e_{n_E}}` partitioned into active change clauses `E_act` and preservation clauses `E_inv` |
| `I, Viol(i, τ_t) ∈ {0, 1}` | Global task/safety invariant set `I` and Boolean violation indicator for invariant `i ∈ I` on transition `τ_t` |
| `AuthSafety(i, τ_t) ∈ {0, 1}` | Indicator that an apparent invariant violation is supported by authoritative observed/replay-verified evidence or by a separately validated safety proof permitted by the contract |
| `conf(e_k, τ_t), θ_conf, Rel(e_k, τ_t)` | Grounding/tracking confidence of clause `e_k`, reliability threshold `θ_conf ∈ (0, 1]`, and reliability indicator `Rel(e_k, τ_t) ∈ {0, 1}` |
| `V_4, ⊗, ≻, ≻_cg` | Four-valued verdict space, conjunctive aggregation operator, strict linear verdict dominance order `≻`, and coarse-graining status order `≻_cg`; `v(·, τ_t) ∈ V_4` denotes a clause-level verdict |
| `𝒞, 𝒞^+, 𝒞^⊥, 𝒞^∅, ξ_wit` | Verification certificate `𝒞` of realization (`+`), incompatibility (`⊥`), or scoped exhaustion (`∅`), with witness tuple `ξ_wit` |
| `S_scope, ρ_query, ϱ_pol, N_match` | Search domain identifier, query specification, existential polarity `ϱ_pol ∈ {+, -}`, and match count in `𝒞^∅` |
| `π_{g_obj,ℓ}, ker(π_{g_obj,ℓ}), π_{ℓ→ℓ+1}` | Coarse-graining projection for goal `g_obj` at scale `ℓ`, its equivalence kernel on `H × H`, and inter-scale graph projection `ℓ → ℓ + 1` |
| `K, D, D̂_t, μ` | Metric verification contract `K`, bound target descriptors `D`, re-identified descriptors `D̂_t`, and registered scalar metric `μ` |
| `b_0, b, b^-, b^+, ς_K ∈ {-1, +1}` | Route-initial metric value `b_0`, step baseline `b`, pre/post-step evaluations `b^-, b^+`, and favorable improvement sign `ς_K` |
| `Δ_K, Δ_K^{tot,-}, Δ_K^{tot,+}, Cross, Cons` | Directed single-step metric change `ς_K(b^+ - b^-)`, pre/post-step cumulative changes relative to `b_0`, the goal-crossing event `Cross`, and the metric–feature consistency predicate `Cons` (§6.1) |
| `θ_prog, θ_succ, θ_fail, ε_base` | Strictly positive step-progress, cumulative-success, and failure thresholds, and baseline stability tolerance in `K` |
| `p, q, r ∈ P, ϕ_gnd, z ∈ B_U` | Predicate symbols in vocabulary `P`, feature grounding map `ϕ_gnd`, and grounded feature vector `z` in ambient box `B_U ⊂ ℝ^m` |
| `B_p = [lo_p, hi_p], w_{p,j}, w_min, margin_p(z)` | Closed axis-aligned predicate box with lower/upper bounds `lo_p, hi_p`, half-widths `w_{p,j}`, minimum half-width `w_min`, and signed membership margin `margin_p(z)` |
| `γ_p, ε_⇒, ε_⊥, ν_max, ovl_j(p, q)` | Epistemic boundary half-width `γ_p`, containment/separation clearances `ε_⇒, ε_⊥`, non-universality margin `ν_max`, and overlap `ovl_j` |
| $`\mathcal{L}_{\subseteq}^{\varepsilon},\mathcal{L}_{\bot}^{\varepsilon},\mathcal{L}_{\mathrm{non\text{-}univ}}`$, `ζ ∈ ℝ^m` | Box containment, separation, and non-universality hinge losses, and bounded feature perturbation vector `ζ` |
| `𝒢_KG, Sc, ℰ_ℓ, 𝔢_ℓ, u_{ℓ+1}, S(𝔢_ℓ, ℓ)` | Hierarchical knowledge graph, scale index set `Sc`, element set `ℰ_ℓ` at scale `ℓ`, micro-element `𝔢_ℓ ∈ ℰ_ℓ`, macro-element `u_{ℓ+1} ∈ ℰ_{ℓ+1}`, and graph status function `S` |
| `h_1, h_2 ∈ H, Tol_K` | Generic descriptors (arguments of kernels and relations) and the step-tolerance relation of a metric contract (§5.1) |
| `T_wait, N_probes, k_max` | Pending-token timeout, evidence-seeking probe budget, and consecutive-`UNDECIDED` limit (§5.4) |
| `m, G^+, G^∼, G^⊥, G^U` | Candidate move and ground-truth reference classes (productive, indifferent, incompatible, undecidable) used in §7.2 |

---

## **1. Introduction and Theoretical Prerequisites**

### **1.1. The State-Transition Verification Problem and Defects of Material Implication**

In neuro-symbolic, agentic, and reasoning architectures, a generative model proposes sequences of intermediate assertions, trajectory steps, and tool invocations. When a generated move is admitted directly into the system state without external verification, a fundamental vulnerability arises: statistically inevitable generator hallucinations [21–22] and the systematic failure of models to abstain from unsupported steps [20, 23–24] corrupt the state trajectory irreversibly. Preventing state corruption requires an architectural separation of powers (*Propose — Judge — Commit*): a generator proposes candidate moves, an external verifier (judge) evaluates them under a formal contract, and a state manager commits only certified transitions.

Attempting to formalize such a verifier within classical two-valued Boolean algebra [9–10] encounters three structural defects of material implication `(x → y) ≡ x' ∨ y ≡ xy ∨ x'y ∨ x'y'` [8]:
1. **Vacuous truth (false antecedent):** When the antecedent is false (`x' = 1`), the implication `x → y` evaluates to true for any consequent `y`, allowing an unexecuted action or unsatisfied premise to confirm arbitrary rules [8].
2. **Vacuous truth (empty expectation or independent consequent):** When an expectation set is empty or when the consequent property `y` holds independently of `x` (`y = 1`), Boolean semantics returns true in the absence of any causal or logical containment linking `x` to `y` [8].
3. **Conflation of exclusion and inessentiality:** In a two-valued Disjunctive Normal Form (DNF), omitting a constituent signifies its impossibility (falsity) [8]. Consequently, to express entailment `x ⇒ y`, the constituent `x'y` must either be excluded—degenerating entailment into equivalence `(x = y) ≡ xy ∨ x'y'`—or explicitly retained—diluting necessary consequence into material implication [8].

These defects do not render classical logic itself unsound; they render the truth-functional semantics of material implication unsuitable as a verification contract for state transitions under incomplete applicability and empirical conditioning.

### **1.2. The Aristotle–Carroll–Brusentsov Lineage**

N. P. Brusentsov and Yu. S. Vladimirova [3–8] demonstrated that Aristotle’s universal affirmative judgment `Axy` (“All `x` are `y`” [1], expressed algebraically by the recursion `x = xy`—“the attribute `y` necessarily belongs to every `x`”) requires a three-valued generalization of Boolean algebra.

Applying Lewis Carroll’s method of indices [2]—where the subscript “1” marks existence (class non-emptiness) and the subscript “0” marks incompatibility (class emptiness, *nullity*)—together with the postulate of the coexistence of opposites in the Aristotelian universe (`x_1, x'_1, y_1, y'_1`) [3, 7–8], Brusentsov formulated necessary entailment `x ⇒ y` as the conjunction [8]:

```math
(x\Rightarrow y)\equiv x_1\land(xy')_0\land y'_1
```

On the four-component constituent scale `(xy, xy', x'y, x'y')`, this relation is encoded by the ternary vector `+-0+`, and in Brusentsov’s improved three-valued DNF by the expression [8]:

```math
(x\Rightarrow y)\equiv xy\vee(xy')_0\vee x'y'
```

Here the constituents `xy` and `x'y'` carry the status of **necessarily given (+)**, the constituent `(xy')_0` carries the status of **necessarily excluded (−, *nullity*)**, and the constituent `x'y` is omitted as **incidental / inessential (0, *incidental*)** [8].

### **1.3. Brusentsov Ternarity versus Łukasiewicz, Kleene, and Belnap Logics**

In the three-valued logics of J. Łukasiewicz [12] and S. C. Kleene [11], the third truth value (`1/2` or `I`) represents an **epistemic truth-value gap** arising from incomplete information. In N. D. Belnap’s four-valued logic `FOUR_4` [16], epistemic states form a diamond bilattice over the presence or absence of positive and negative evidence (`{T, F, None, Both}`), where `None` and `Both` are incomparable under the truth ordering.

In N. P. Brusentsov’s algebra [4, 8], the status `0` (omission of a constituent in the DNF) has a fundamentally different nature: it is an **ontological status of a relation member**, certifying that the member is *incidental (inessential)* to the law under consideration—the relation holds regardless of whether that constituent is present or absent [8]. In the present calculus, Brusentsov’s ontological inessentiality is formalized as the structural verdict `OMIT` (0), whereas epistemic insufficiency (lack of certification, analogous to Kleene’s `I` [11] or Belnap’s `None` [16]) is isolated as a distinct operational control signal `UNDECIDED` (`U`).

### **1.4. Structural Limitations of Classical Brusentsov Notation**

Constructing a mathematically closed automated verifier requires resolving four limitations in Brusentsov’s 2012 formulation [8]:
1. **Incompatibility between pointwise and ensemble evaluation:** In an integral law over a universe of discourse, both classes `xy` and `x'y'` must be non-empty (vector `+-0+`). In a single observed transition `τ_t`, however, the disjoint classes `xy` and `x'y'` have empty intersection (`xy ∩ x'y' = ∅`) and cannot be realized simultaneously.
2. **The Hempel–Nicod confirmation paradox (“the raven paradox”):** Because Brusentsov equates entailment with its contrapositive, `Axy ≡ Ay'x' ≡ (x ⇒ y)(y' ⇒ x')`, the constituent `x'y'` (“non-black non-ravens”) receives the same asserted status `+` as `xy` (“black ravens”) [8]. Under J. Nicod’s confirmation criterion [13] and C. G. Hempel’s equivalence condition [14], observing an unrelated object `x'y'` counts as positive empirical confirmation of `x ⇒ y`. (Moreover, in Bayesian confirmation theory, I. J. Good [15] demonstrated that when background world distributions correlate the population of ravens with the population of black objects, passive observation of `xy` or `x'y'` depends on prior background frequencies; consequently, an operational verifier must separate structural non-triviality of the predicate space from direct empirical trials of the antecedent.)
3. **Heterogeneity of consequent negation `y'`:** In multi-dimensional state spaces, neutral non-realization of an expected effect (`y^∼`, e.g., halting against an obstacle or sub-threshold movement) must be distinguished from active contrariety (`y^⊥`, e.g., moving in the opposite direction, leaking into an orthogonal invariant coordinate, or destroying the target object).
4. **Lack of closure for `n ≥ 3` variables:** Brusentsov’s statement that the existence index “1” is unnecessary in the improved DNF because “members unindexed by zero are non-excludable” [8, p. 6] holds only for two variables (`x, y`). When a third variable (such as a context precondition `c` or a syllogistic middle term `z`) is introduced, the class `xy` splits into `xyz ∨ xyz'`; the condition `x_1` requires the non-emptiness of the *union* `xyz ∪ xyz' ≠ ∅`, whereas listing both unindexed terms in Brusentsov’s DNF erroneously requires both sub-classes to exist simultaneously.

---

## **2. Two-Tier Verification Architecture: Transition and Law**

### **2.1. Formal Process Model and Evidence Scopes**

Let a controlled process be defined by the tuple `(X, O, 𝒜, Σ_t)`, where at each discrete step `t` the system ingests a trusted observation packet `ō_t = (o_t, Σ_t, meta_t)` comprising a sensory or symbolic frame `o_t ∈ O`, the active action surface `Σ_t = (𝒜_t, κ_t)` (where `𝒜_t ⊆ 𝒜` and `κ_t` encodes active control mode, capability, and resource metadata), and synchronization telemetry `meta_t`. Let `H_t = ψ(ō_t) ∈ H` denote the deterministic structural state descriptor (an object-relation scene graph or normalized assertion graph) extracted from `ō_t`.

The tuple

```math
\tau_t=(seq_t,\bar{o}_t,\mathsf{act}_t,\bar{o}_{t+1})
```

with unique monotonic sequence identifier `seq_t ∈ ℕ` and executed action `act_t ∈ 𝒜_t` is the **state transition at step `t`**. To capture fast intra-step dynamics, `τ_t` may include a finite sub-frame sequence `(o_{t,0}, o_{t,1}, ..., o_{t,k})` with `o_{t,0} = o_t` and `o_{t,k} = o_{t+1}`, from which both static and intra-step transient feature changes `δ_obs(s, F; τ_t)` are deterministically extracted.

**Definition 2.1 (Evidence Scope).** Every transition or evaluation artifact `τ_t` is assigned an evidentiary scope `σ(τ_t)`:
- `NOT_AVAILABLE` — observation data is missing or corrupted;
- `PREDICTIVE_ONLY` — generated by internal simulation (*rollout*) or model proposal prior to physical or instrumental execution;
- `OBSERVED_TRANSITION` — produced by single ingestion of an actually executed transition `τ_t`;
- `REPLAY_VERIFIED` — deterministically verified against the immutable audit log for an existing sequence identifier `seq_t`.

**Non-Promotion Invariant:** No artifact with scope `σ(τ_t) = PREDICTIVE_ONLY` may be committed to long-term memory as a factual transition or included in the law-confirmation ensemble `𝒯`. Furthermore, `𝒯` is a **set keyed by `seq_t`**: replaying a transition updates its verification status to `REPLAY_VERIFIED` in place without duplicating the transition record in `𝒯`.

### **2.2. Hierarchy of the Two Calculus Tiers**

To resolve the collision between single-step evaluation and universal rule evaluation, the calculus is partitioned into two tiers:
1. **Tier 1 (Pointwise Transition Calculus):** Maps a single transition `τ_t`, given a bound expectation set `E` and global invariants `I`, into the four-valued verdict space `V_4 = {FOLLOW, OMIT, NULL, UNDECIDED}`.
2. **Tier 2 (Integral Law Calculus):** Maps a universal hypothesis `Λ = (AC ⇒ y)` over the deduplicated ensemble of authoritatively observed transitions `𝒯 = {τ_{t_1}, ..., τ_{t_N}}` (where `∀τ ∈ 𝒯: σ(τ) ∈ {OBSERVED_TRANSITION, REPLAY_VERIFIED}`), restricted to its reliably grounded sub-ensemble `𝒯_rel(Λ) = {τ ∈ 𝒯 : Rel(Λ, τ) = 1}`, into an invariant lifecycle status. Restricting Tier 2 evaluation to `𝒯_rel(Λ)` guarantees that epistemically uncertified transitions (judged `UNDECIDED` at Tier 1 due to `Rel = 0`) never pollute law confirmation or falsification at Tier 2.

---

## **3. Modified Brusentsov Disjunctive Normal Form (MDNF)**

### **3.1. Strictly Disjoint Ternary Consequent Splitting `(y^+, y^∼, y^⊥)`**

Let an atomic expectation clause `e_k = (a_k, c_k, s_k, F_k, φ_{exp,k})` bind an operator indicator `a_k ∈ {0, 1}`, a precondition context indicator `c_k ∈ {0, 1}`, a specific subject (entity, graph node, variable) `s_k`, a feature family `F_k`, and a target change predicate `φ_{exp,k}` specifying the admissible non-empty subset of observed feature changes `δ_obs(s_k, F_k; τ_t)`. Throughout this specification, `𝟎` denotes the zero change element of the feature-delta space (identifying `𝟎 = 0` in one-dimensional or discrete scalar spaces). When `𝟎 ∉ φ_{exp,k}` (an active change clause `e_k ∈ E_act`) in a `d`-dimensional feature space `ℝ^d`, `φ_{exp,k}` may be parameterized by a reference expected displacement vector `𝛅_exp ∈ ℝ^d ∖ {𝟎}`. Global task and safety constraints `i ∈ I` are evaluated separately by a direct violation predicate `Viol(i, τ_t) ∈ {0, 1}`. An apparent violation (`Viol = 1`) is eligible for `NULL` only when it is authoritatively supported (`AuthSafety(i, τ_t) = 1`); an unauthenticated apparent violation is epistemically unresolved (`UNDECIDED`, §4.3 Step 2) and is never silently ignored.

To prevent overlap on boundary cases (such as stationarity/preservation expectations `𝟎 ∈ φ_{exp,k}` or orthogonal vector components), the three consequent outcomes for clause `e_k`—fulfillment `y^+`, neutral indifference `y^∼`, and strong incompatibility `y^⊥`—are defined sequentially and disjointly. For each active clause, the contract may declare a bounded set `Ω_{sub,k} ⊆ ℝ^d ∖ {𝟎}` of non-zero changes that are explicitly tolerated as neutral/sub-threshold. This set must be grounded in feature-space units, disjoint from `φ_{exp,k}`, and must not be inferred from `δ_obs ≠ 𝟎` alone. If no such region is specified, take `Ω_{sub,k} = ∅`. For an active clause, a resolved observed change outside `φ_{exp,k} ∪ {𝟎} ∪ Ω_{sub,k}` is incompatible rather than automatically treated as sub-threshold.

**Definition 3.1 (Canonical Nullity Classes `y^⊥`).** For a bound expectation clause `e_k = (a_k, c_k, s_k, F_k, φ_{exp,k})`, the incompatibility indicator `y^⊥(e_k, τ_t) = 1` holds if and only if, during transition `τ_t`, at least one of the following occurs for the **same subject `s_k` and feature family `F_k`**:
1. *Subject identity violation:* Identity is assessed only when an explicit identity clause `e^id = (s_k, ι_{s_k})` is bound, where `ι_{s_k} ∈ {PRESENT, ABSENT, PRESERVE}`, using the trusted before/after predicates `Alive(s_k, ō_t) ∈ {0, 1}` and `Alive(s_k, ō_{t+1}) ∈ {0, 1}`. Canonically, `e^id` is embedded in the 5-tuple clause format with feature family `F_k = Alive` and observed delta `δ_obs(s_k, Alive; τ_t) = Alive(s_k, ō_{t+1}) - Alive(s_k, ō_t) ∈ {-1, 0, +1}` (so `φ_{exp,k} = {0}` places identity preservation in `E_inv`, whereas active creation `φ_{exp,k} = {+1}` or removal `φ_{exp,k} = {-1}` places `e^id` in `E_act`). The clause is incompatible (`y^⊥ = 1`) if the observed presence/absence violates `ι_{s_k}`. A non-identity feature delta `δ_obs(s_k, F_k; τ_t)` (`F_k ≠ Alive`) is undefined when `s_k` is missing; the verifier must not infer identity failure from an undefined feature delta. If the required presence information `Alive(s_k, ·)` is unavailable, the identity clause is `UNDECIDED` rather than `NULL`.
2. *Unintended invariant mutation:* `𝟎 ∈ φ_{exp,k}` (stationarity or bounded-tolerance preservation required for feature `F_k` of subject `s_k`, i.e., `e_k ∈ E_inv`), but an out-of-bounds change `δ_obs(s_k, F_k; τ_t) ∉ φ_{exp,k}` is observed (in particular, when `φ_{exp,k} = {𝟎}`, any `δ_obs(s_k, F_k; τ_t) ≠ 𝟎` yields `y^⊥ = 1`).
3. *Directional sign inversion, orthogonal axis leakage, or failure-threshold breach:* Given an active change clause (`𝟎 ∉ φ_{exp,k}`) with reference expected displacement vector `𝛅_exp ∈ ℝ^d ∖ {𝟎}` and a non-zero observed displacement `𝛅_obs ∈ ℝ^d ∖ {𝟎}`, there exists a coordinate axis `j ∈ {1, ..., d}` such that either $`\delta_{\mathrm{exp},j}\neq 0\land\mathrm{sign}(\delta_{\mathrm{exp},j})\cdot\delta_{\mathrm{obs},j}<-\varepsilon_{\mathrm{rev}}`$ (sign inversion beyond tolerance `ε_rev ≥ 0` on an active axis, reducing to `sign(δ_{exp,j}) · sign(δ_{obs,j}) < 0` when `ε_rev = 0` on discrete grids) or `(δ_{exp,j} = 0 ∧ |δ_{obs,j}| > ε_orth)` (unintended leakage along an axis required to remain invariant, with `ε_orth = 0` on discrete grids); or, in a metric contract, the directed change satisfies `Δ_K ≤ -θ_fail` (evaluable only under a stable baseline and sufficient tracking confidence, §6.1).
4. *Local state-consistency conflict:* `δ_obs(s_k, F_k; τ_t)` directly contradicts a previously committed `FOLLOW` assertion on the same subject `s_k` and feature family `F_k`.
5. *Resolved out-of-contract active change:* For `e_k ∈ E_act`, a reliably observed change lies outside `φ_{exp,k} ∪ {𝟎} ∪ Ω_{sub,k}`. This residual case closes the partition: a non-zero change is not neutral merely because it is non-zero; it must belong to the explicitly declared neutral region.

(Note: Observations concerning distinct subjects `s_1 ≠ s_2` never trigger `y^⊥` for each other.)

**Definition 3.2 (Fulfillment `y^+` and Indifference `y^∼ = y^∼_stag ∨ y^∼_sub`).** The partition below applies only to resolved transitions for which the relevant subject identity and feature delta are defined. If the subject/feature cannot be reliably tracked or the delta is undefined, the clause is epistemically unresolved and receives `UNDECIDED` rather than a member of the three-way partition. On an active clause, zero change is the stagnation subtype, while a non-zero change is the sub-threshold subtype only when it belongs to the contract-declared set `Ω_{sub,k}`:
- `y^+(e_k, τ_t) = 1 ⇔ y^⊥(e_k, τ_t) = 0 ∧ δ_obs(s_k, F_k; τ_t) ∈ φ_{exp,k}` (in particular, for any preservation constraint `e_k ∈ E_inv` where `𝟎 ∈ φ_{exp,k}`, observing `δ_obs ∈ φ_{exp,k}` yields `y^+ = 1`, whereas `δ_obs ∉ φ_{exp,k}` is captured by Clause 2 of Definition 3.1 as `y^⊥ = 1`);
- `y^∼(e_k, τ_t) = 1 ⇔ y^⊥(e_k, τ_t) = 0 ∧ y^+(e_k, τ_t) = 0`.

By construction, for every clause `e_k` and resolved transition `τ_t`, the triple `(y^+, y^∼, y^⊥)` forms a strict partition of unity:

```math
y^{+}\vee y^{\sim}\vee y^{\bot}=1,\qquad y^{u}\land y^{v}=0\quad(\forall u\neq v\in\{+,\sim,\bot\}).
```

Because every preservation clause `e_k ∈ E_inv` (`𝟎 ∈ φ_{exp,k}`) satisfies `y^+ ∨ y^⊥ = 1`, the indifferent outcome `y^∼(e_k, τ_t) = 1` can only occur for active change clauses `e_k ∈ E_act` (`𝟎 ∉ φ_{exp,k}`). Within `y^∼(e_k, τ_t) = 1`, we define two disjoint sub-indicators:
- **Strict zero-delta stagnation:** `y^∼_stag(e_k, τ_t) = 1 ⇔ y^∼(e_k, τ_t) = 1 ∧ δ_obs(s_k, F_k; τ_t) = 𝟎`;
- **Sub-threshold non-zero change:** `y^∼_sub(e_k, τ_t) = 1 ⇔ y^∼(e_k, τ_t) = 1 ∧ δ_obs(s_k, F_k; τ_t) ∈ Ω_{sub,k}`.

Thus `y^∼ = y^∼_stag ∨ y^∼_sub` with `y^∼_stag ∧ y^∼_sub = 0`. In a metric contract (§6.1) the neutral set is extended transition-wise by admissible-direction changes whose metric progress is below the progress threshold; the partition remains total by construction.

### **3.2. Contextual Antecedent `c`**

For any clause `e_k`, let `a_k ∈ {0, 1}` indicate whether the tested operator was invoked in transition `τ_t`, and let `c_k ∈ {0, 1}` be the Boolean indicator of an **admissible, unobstructed precondition context**:
- `c_k = 1`: Operator `a_k` is compatible with the current control surface (`Σ_t ⊨ Σ^req`), activation preconditions hold, and subject `s_k` is free of boundary or obstacle contact along the action direction;
- `c'_k = 1` (`c_k = 0`): Physical boundary or obstacle contact is present (*boundary / obstacle contact*), a conditional trigger precondition is unfulfilled, or the surface `Σ_t` is incompatible.

**Independence requirement.** `c_k(τ_t)` is computed from `(ō_t, act_t)` and the contract only, and it is certified by a context witness `ξ_c` (§5.3) derived from pre-outcome evidence. It must never be inferred from `ō_{t+1}` or from the outcome indicators `y^+, y^∼, y^⊥`. Without this requirement the law `(ac ⇒ y)` would be unfalsifiable: any stagnation could be relabeled post hoc as obstruction (`c'`). A context that cannot be certified from pre-outcome evidence makes the clause epistemically unresolved (`UNDECIDED`, §4.3 Step 2).

**Static domains.** In domains without actions (e.g., a static text corpus) the convention `a_k ≡ 1`, `c_k ≡ 1` applies.

### **3.3. Canonical MDNF of Conditional Entailment `(ac ⇒ y)`**

In the base space of `2 × 2 × 3 = 12` elementary constituents over `{a, a'}`, `{c, c'}`, and `{y^+, y^∼, y^⊥}`, with the single unobstructed indifferent constituent `acy^∼` further partitioned into strict stagnation `acy^∼_stag` and sub-threshold progress `acy^∼_sub`, the conditional effect-entailment law `Λ = (ac ⇒ y)` is defined by the **Modified Brusentsov DNF**. This law tests the expected effect only under the applicable antecedent `ac = 1`:

```math
(ac\Rightarrow y)\equiv (acy^{+})_1\vee(acy^{\sim}_{\mathrm{stag}})_0\vee(acy^{\bot})_0\vee ac'y^{\sim}\vee a'y^{\sim}.
```

The term `(ac'y^⊥)_0` is intentionally excluded from `Λ`: with `ac' = 1`, the effect law is outside its applicability conditions. Destructive outcomes in that context are governed by a separate safety obligation, formalized in §3.4 as `Ob_safety`. A system contract may require both `Λ` and `Ob_safety`; violation of either contradicts the combined contract, while the evidence record identifies which obligation failed.

**Remark (Absorption of context under `a' = 1` and omission of `acy^∼_sub`).** When the operator is not activated (`a' = 1`), the context variable `c` is irrelevant to the law `Λ`; thus the single unindexed term `a'y^∼` absorbs both `a'cy^∼` and `a'c'y^∼`. Similarly, under `a = 1 ∧ c = 1`, only strict stagnation `(acy^∼_stag)_0` is indexed as a Carrollian nullity, whereas sub-threshold non-zero progress `acy^∼_sub` is omitted as incidental to law falsification. On discrete grids where `φ_exp` admits all non-zero valid moves, `y^∼_sub ≡ 0` and `acy^∼_stag` coincides with `acy^∼`. The table below accounts for all `12` base constituents. Splitting the single base constituent `acy^∼` into stagnation and sub-threshold non-zero change yields `13` refined cases in the table; these are `12` Boolean/ternary base cells plus one additional subcase.

| Constituent | Syntactic Category in MDNF | Meaning and Tier 2 Law Impact | Tier 1 Step Verdict (§4.3) |
| :--- | :--- | :--- | :--- |
| **`acy^+`** (1) | Unit-indexed `(·)_1` (mandatory existence) | Productive core: operator `a` in unobstructed context `c = 1` realizes `y^+`; increments law support. | `FOLLOW` (+1) |
| **`acy^⊥`** (2) | Zero-indexed `(·)_0` (Carrollian nullity) | Direct contrariety under unobstructed execution; falsifies law `Λ`. | `NULL` (−1) |
| **`acy^∼_stag`** (3a) | Zero-indexed `(·)_0` (Carrollian nullity) | Strict zero-delta stagnation (`δ_obs = 𝟎`) in unobstructed context: falsifies law `Λ` at Tier 2; at Tier 1 yields `NULL` on a confirmed pair `(a, F)` and `UNDECIDED` if unconfirmed. | `NULL` (−1) (if `χ_conf = 1`) / `UNDECIDED` (U) (if `χ_conf = 0`) |
| **`acy^∼_sub`** (3b) | Omitted (incidental sub-threshold step) | Non-zero change inside the explicitly declared bounded neutral region `Ω_{sub,k}`; excluded from law falsification/confirmation at Tier 2 (see §3.4 and §5.2). | `OMIT_INCIDENTAL` (0) |
| **`ac'y^⊥`** (4) | Separate safety obligation (not a term of `Λ`) | Boundary/obstacle contact causes *destructive* contrariety (subject destruction, invariant breach, or sign inversion); violates `Ob_safety`, not the effect law by itself. Soft obstruction without destruction is handled by `ac'y^∼`. | `NULL` (−1) under an authoritative, valid safety certificate |
| **`ac'y^∼`** (5) | Unindexed explicit (admissible indifference) | **Obstructed soft stop** or **inactive conditional trigger**: zero/declared neutral change under `c' = 1`; it does not falsify the effect law or establish a safety violation. | `OMIT_BLOCKED` (0) |
| **`a'cy^∼, a'c'y^∼`** (6, 7 — absorbed as **`a'y^∼`**) | Unindexed explicit (admissible indifference) | Passive indifference when operator `a` is not invoked (`a' = 1`); neither confirms nor falsifies `Λ`. | `OMIT_REDUNDANT` (0) (if `H_{t+1} = H_t`) or `OMIT_INCIDENTAL` (0) |
| **`ac'y^+, a'cy^+, a'c'y^+, a'cy^⊥, a'c'y^⊥`** (8–12) | Omitted (incidental inessentiality) | Effect `y^+` or `y^⊥` caused by an external factor or alternative operator `b ≠ a` while `ac = 0`; incidental to the effect law `Λ`. The obstructed destructive case `ac'y^⊥` is handled separately by `Ob_safety`. | `OMIT_INCIDENTAL` (0) (relative to `Λ`) |

**Remark (Tier separation).** Omission at Tier 2 does not imply `OMIT` at Tier 1 for every clause type. A *preservation clause* (`e_k ∈ E_inv`) that is reliably certified as violated yields `NULL` irrespective of `a_k`, because the step contract is incompatible with the observation (§4.2). An *active* clause with `a_k = 0` is inessential to the step contract (the operator was not invoked) and yields `OMIT` even when an exogenous contrary change is observed (rows 8–12 of the table above); such an outcome does not falsify the law `Λ` about the tested operator either.

### **3.4. Context-Normalized Ensemble Quantifiers and Defense Against the Hempel–Nicod Paradox**

Let `𝒯` be the deduplicated ensemble of transitions with scope `σ(τ) ∈ {OBSERVED_TRANSITION, REPLAY_VERIFIED}`, and for a tested law `Λ = (AC ⇒ y)` let `𝒯_rel(Λ) = {τ ∈ 𝒯 : Rel(Λ, τ) = 1}` denote the subset of transitions on which the subject and feature descriptors of `Λ` are reliably tracked. Let `Γ_AC = AC(y^+ ∨ y^⊥ ∨ y^∼_stag)` denote an effective unobstructed trial of `Λ` (excluding incidental sub-threshold steps `ACy^∼_sub`). Here `y^+` is included in `Γ_AC` so that the conditioning denominator of $`\mathbf{N}^{(\eta_{\mathrm{tol}})}_{\mathrm{effect},\mathcal{T}}`$ spans all effective unobstructed trials (both productive realizations and violations), whereas the numerator counts only the violation events `AC(y^⊥ ∨ y^∼_stag)`. For any conditioning event `Γ_cond ∈ {Γ_AC, AC'}`, minimum empirical support threshold `N_min ∈ ℕ` (`N_min ≥ 1`), and observation noise tolerance `η_tol ∈ [0, 1)`, we define the generalized Carroll–Brusentsov ensemble quantifiers over `𝒯_rel(Λ)`:

```math
\mathbf{V}^{(N_{\min})}_{\mathcal{T}}(\Phi)\;\equiv\;\Bigl(\bigl|\{\tau\in\mathcal{T}_{\mathrm{rel}}(\Lambda):\Phi(\tau)=1\}\bigr|\ge N_{\min}\Bigr)_1
```

```math
\mathbf{N}^{(\eta_{\mathrm{tol}})}_{0,\mathcal{T}}(\Psi\mid\Gamma_{\mathrm{cond}})\;\equiv\;\Bigl(\bigl|\{\tau\in\mathcal{T}_{\mathrm{rel}}(\Lambda):\Psi(\tau)=1\}\bigr|\le\eta_{\mathrm{tol}}\cdot\bigl|\{\tau\in\mathcal{T}_{\mathrm{rel}}(\Lambda):\Gamma_{\mathrm{cond}}(\tau)=1\}\bigr|\Bigr)_0
```

**Convention on zero conditioning set.** If `|{τ ∈ 𝒯_rel(Λ) : Γ_cond(τ) = 1}| = 0`, then the numerator is also zero for the predicates used here because each violation event is a subset of its conditioning event. The inequality `0 ≤ η_tol · 0` therefore holds formally, but the quantifier is interpreted as *vacuously satisfied* and does **not** by itself constitute empirical confirmation of the law. Confirmation requires the independent positive-support condition $`\mathbf{V}^{(N_{\min})}_{\mathcal{T}}(ACy^{+})`$ together with `NonTriv(y)`. Thus “no contradictions observed on an empty applicable set” is distinguished from “law verified on a sufficient number of applicable observations.”

In deterministic domains, `η_tol = 0` and `N_min = 1`, the quantifier $`\mathbf{N}^{(0)}_{0,\mathcal{T}}(\Psi\mid\Gamma_{\mathrm{cond}})\equiv\bigl(\{\tau\in\mathcal{T}_{\mathrm{rel}}(\Lambda):\Psi(\tau)=1\}=\emptyset\bigr)_0`$ recovers exact Carrollian class emptiness (*nullity*). The effect obligation conditions `AC(y^⊥ ∨ y^∼_stag)` on `Γ_AC`; the independent safety obligation conditions `AC'y^⊥` on `AC'`. This separation prevents denominator dilution: obstructed soft stops `AC'y^∼ = 1` do not count as safety violations, and sub-threshold steps `ACy^∼_sub = 1` do not inflate the denominator of unobstructed effect trials.

Define the two obligations and their combined contract predicate separately:

```math
\mathbf{N}^{(\eta_{\mathrm{tol}})}_{\mathrm{effect},\mathcal{T}}(A,C,y)\equiv\mathbf{N}^{(\eta_{\mathrm{tol}})}_{0,\mathcal{T}}\bigl(AC(y^{\bot}\lor y^{\sim}_{\mathrm{stag}})\mid \Gamma_{AC}\bigr),
```

```math
\mathbf{N}^{(\eta_{\mathrm{tol}})}_{\mathrm{safety},\mathcal{T}}(A,C,y)\equiv\mathbf{N}^{(\eta_{\mathrm{tol}})}_{0,\mathcal{T}}\bigl(AC'y^{\bot}\mid AC'\bigr),
```

```math
\mathbf{N}^{(\eta_{\mathrm{tol}})}_{\mathrm{contract},\mathcal{T}}(A,C,y)\equiv\mathbf{N}^{(\eta_{\mathrm{tol}})}_{\mathrm{effect},\mathcal{T}}(A,C,y)\land\mathbf{N}^{(\eta_{\mathrm{tol}})}_{\mathrm{safety},\mathcal{T}}(A,C,y).
```

For compact reference, define `Ob_effect` as the obligation that $`\mathbf{N}^{(\eta_{\mathrm{tol}})}_{\mathrm{effect},\mathcal{T}}(A,C,y)`$ holds, and define `Ob_safety` as the obligation that $`\mathbf{N}^{(\eta_{\mathrm{tol}})}_{\mathrm{safety},\mathcal{T}}(A,C,y)`$ holds. The first predicate tests the effect law under `AC = 1`; the second independently tests safety under `AC' = 1`. The combined contract is satisfied only when both predicates hold.

Let `NonTriv(y)` assert that the acceptance region of `y` is a proper subset of the ambient feature universe (`Ω_y ⊊ Ω_𝒰`).

**Definition 3.3 (Integral Law Status and Feature-Indexed Operator Confirmation).** The combined effect-and-safety contract for `Λ = (AC ⇒ y)` on feature family `F` assumes exactly one of four mutually exclusive statuses over `𝒯`. The separate predicates above remain available to report whether a contradiction belongs to the effect obligation or the safety obligation:

```math
\mathrm{Status}(\Lambda\mid\mathcal{T})=\begin{cases}
\text{CONTRADICTED}, & \text{if }\neg\mathbf{N}^{(\eta_{\mathrm{tol}})}_{\mathrm{contract},\mathcal{T}}(A,C,y),\\[6pt]
\text{CONFIRMED}, & \text{if }\mathbf{V}^{(N_{\min})}_{\mathcal{T}}(ACy^{+})\;\land\;\mathbf{N}^{(\eta_{\mathrm{tol}})}_{\mathrm{contract},\mathcal{T}}(A,C,y)\;\land\;\mathrm{NonTriv}(y),\\[6pt]
\text{CONDITIONAL\_CANDIDATE}, & \text{if }\neg\mathbf{V}^{(1)}_{\mathcal{T}}(AC)\;\land\;\mathbf{V}^{(1)}_{\mathcal{T}}(AC'y^{\sim})\;\land\;\mathbf{N}^{(\eta_{\mathrm{tol}})}_{0,\mathcal{T}}(AC'y^{\bot}\mid AC'),\\[6pt]
\text{UNRESOLVED}, & \text{otherwise.}
\end{cases}
```

*(Note on mutual exclusivity: If the `CONDITIONAL_CANDIDATE` condition holds, then $`\neg\mathbf{V}^{(1)}_{\mathcal{T}}(AC)`$ implies both $`\neg\mathbf{V}^{(N_{\min})}_{\mathcal{T}}(ACy^{+})`$ for all `N_min ≥ 1` and `|{τ ∈ 𝒯_rel(Λ) : Γ_AC(τ) = 1}| = 0`, so the effect-nullity predicate holds vacuously; together with the safety-nullity condition explicitly required by `CONDITIONAL_CANDIDATE`, this makes $`\mathbf{N}^{(\eta_{\mathrm{tol}})}_{\mathrm{contract},\mathcal{T}}(A,C,y)`$ true. Hence the first three branches are strictly disjoint regardless of evaluation order.)*

An operator `A` is **confirmed for feature family `F`** on ensemble `𝒯`, denoted `χ_conf(A, F; 𝒯) = 1`, if and only if there exists a target predicate `y` on feature family `F` such that `Status(AC ⇒ y | 𝒯) = CONFIRMED` (otherwise `χ_conf(A, F; 𝒯) = 0`). Indexing confirmation by the pair `(A, F)` ensures that an operator confirmed to modify one feature (e.g., spatial position) is never falsely penalized for “stagnation” on an unrelated feature (e.g., color) that it was never confirmed to affect.

**Lifecycle semantics of statuses.**

| Status | Meaning | Effect on memory and on `χ_conf` |
| :--- | :--- | :--- |
| `CONFIRMED` | At least `N_min` positive instances; violation share `≤ η_tol` in both obligations; non-trivial `y` | Stored as an invariant; `χ_conf(A, F; 𝒯) = 1` |
| `CONTRADICTED` | Violation share above `η_tol` in the effect or the safety obligation | Retired from active invariants (log retained); `χ_conf = 0` |
| `CONDITIONAL_CANDIDATE` | Operator observed only in obstructed contexts, without violation | Kept in the candidate pool awaiting an admissible-context test; `χ_conf = 0` |
| `UNRESOLVED` | Insufficient evidence | Collect more evidence; `χ_conf = 0` |

**Order of operations.** The flag `χ_conf` used in the verdict of `τ_t` is evaluated on the ensemble *before* `τ_t` is ingested, `𝒯_{t-1}`; `τ_t` is appended to `𝒯` and the law statuses are recomputed only after the verdict is fixed. Consequently, a stagnation event that yields `NULL` is itself a counterexample: with `η_tol = 0` it turns the law into `CONTRADICTED`, so `χ_conf` becomes `0` and an identical repeated stagnation is subsequently `UNDECIDED` (evidence-seeking), not `NULL`. Without this convention the verdict would depend on whether a transition is counted in its own evaluation context.

**Theorem 3.1 (Immunity to the Hempel–Nicod Raven Paradox and Boundary Stability Across All `η_tol ∈ [0, 1)`).** For any transition ensemble `𝒯`, support threshold `N_min ≥ 1`, and noise tolerance `η_tol ∈ [0, 1)`:
1. *Confirmation Asymmetry:* Appending to `𝒯` any number of transitions `τ` with `A(τ) = 0` (in particular, instances of `a'y^∼`—“non-black non-ravens” [13–14]) leaves both $`\mathbf{V}_{\mathcal{T}}^{(N_{\min})}(ACy^{+})`$ and $`\mathbf{N}_{\mathrm{contract},\mathcal{T}}^{(\eta_{\mathrm{tol}})}(A,C,y)`$ invariant and cannot promote `Λ` from `UNRESOLVED` to `CONFIRMED`.
2. *Boundary Obstruction and Sub-Threshold Stability:* Appending to `𝒯` any number of obstructed transitions `τ` satisfying `A(τ) = 1, C'(τ) = 1, y^∼(τ) = 1` (*soft stop*) or sub-threshold transitions satisfying `A(τ) = 1, C(τ) = 1, y^∼_sub(τ) = 1` keeps $`\mathbf{N}_{\mathrm{contract},\mathcal{T}}^{(\eta_{\mathrm{tol}})}(A,C,y)`$ satisfied whenever it was satisfied, and therefore never demotes a law that already satisfies the `CONFIRMED` conditions to `CONTRADICTED` (see Remark 3.2 for the converse direction). (The status may remain `UNRESOLVED` or `CONDITIONAL_CANDIDATE` if positive support or non-triviality was previously lacking.)

*Proof.* (1) Whenever `A(τ) = 0`, the conjunctions `ACy^+(τ)`, `AC(y^⊥(τ) ∨ y^∼_stag(τ))`, `AC'y^⊥(τ)`, and the conditioning events `Γ_AC(τ)` and `AC'(τ)` all evaluate to `0`, leaving every cardinality in $`\mathbf{V}_{\mathcal{T}}^{(N_{\min})}`$ and $`\mathbf{N}_{\mathrm{contract},\mathcal{T}}^{(\eta_{\mathrm{tol}})}`$ unchanged. Meanwhile, Brusentsov’s requirement that the consequent’s opposite be non-empty (`y'_1` [8]) is enforced structurally by `NonTriv(y)` (`Ω_y ⊊ Ω_𝒰`) without counting external instances `a'y^∼`. (2) For any transition `τ` with `A(τ) = 1, C'(τ) = 1, y^∼(τ) = 1`, we have `C(τ) = 0` and `y^⊥(τ) = 0`. Consequently, in $`\mathbf{N}^{(\eta_{\mathrm{tol}})}_{0,\mathcal{T}}(AC(y^{\bot}\lor y^{\sim}_{\mathrm{stag}})\mid \Gamma_{AC})`$ neither the numerator nor the denominator changes. For the separate safety predicate $`\mathbf{N}^{(\eta_{\mathrm{tol}})}_{\mathrm{safety},\mathcal{T}}(A,C,y)`$, the numerator `|{τ' ∈ 𝒯_rel(Λ) : AC'y^⊥ = 1}|` increases by `0` while the denominator `|{τ' ∈ 𝒯_rel(Λ) : AC' = 1}|` increases by at most `1`; since `η_tol ≥ 0`, the inequality `LHS ≤ η_tol · RHS` remains satisfied for all `η_tol ∈ [0, 1)`. Similarly, for any sub-threshold transition with `A(τ) = 1, C(τ) = 1, y^∼_sub(τ) = 1`, all indicators `y^+, y^⊥, y^∼_stag, C'` are `0`, leaving all numerators and denominators in $`\mathbf{V}_{\mathcal{T}}^{(N_{\min})}`$ and $`\mathbf{N}_{\mathrm{contract},\mathcal{T}}^{(\eta_{\mathrm{tol}})}`$ invariant. `∎`

**Remark 3.1 (Meaning of `CONFIRMED`).** `CONFIRMED` records corroboration—at least `N_min` positive instances and no (or an `η_tol`-negligible share of) counterexamples in both obligations—not a posterior probability. With `η_tol = 0` the status `CONTRADICTED` is permanent for the evidence at hand; in stochastic domains `η_tol` and `N_min` must be calibrated empirically.

**Remark 3.2 (One-directional stability).** Part (2) of Theorem 3.1 is a non-demotion statement. For `η_tol > 0`, appending many obstructed soft stops can only decrease the violation share within the stratum `AC'` and can therefore also newly satisfy a previously violated safety obligation by dilution inside that stratum. Whenever violations under obstruction are hard exclusions (e.g., destruction of the target), the safety obligation should be evaluated with `η_tol = 0`.

**Remark 3.3 (Scope of the immunity).** The theorem is syntactic: evidence that does not instantiate the antecedent cannot change the status. It does not address I. J. Good’s population-frequency counterexample to Nicod’s criterion [15] (§1.4, item 2); the calculus is a falsification-first status calculus, not a Bayesian confirmation measure.

---

## **4. Four-Valued Verdict Calculus and the Dominance Semilattice**

### **4.1. The Verdict Space `V_4`**

At Tier 1, each transition `τ_t` is evaluated in the four-element verdict set `V_4`:

```math
V_4=\bigl\{\mathrm{FOLLOW}\ (+1),\;\mathrm{OMIT}\ (0),\;\mathrm{NULL}\ (-1),\;\mathrm{UNDECIDED}\ (U)\bigr\}
```

| Verdict in `V_4` | Operational Alias | Graph Equivalent | Operational and Logical Meaning |
| :--- | :--- | :--- | :--- |
| `FOLLOW` (+1) | `REQUIRED` | `+` | Necessary entailment certified (`acy^+`): all active clauses in `E_act ≠ ∅` and preservation clauses in `E_inv` hold. |
| `OMIT` (0) | `IRRELEVANT` | `0` | Admissible inessentiality (`a'y^∼`, `ac'y^∼`, `acy^∼_sub`, `E_act = ∅`, or omitted MDNF constituents): no contradiction, zero certified step progress. |
| `NULL` (−1) | `FORBIDDEN` | `-` | Certified incompatibility (`(acy^⊥)_0`, `(acy^∼_stag)_0`, a destructive `ac'y^⊥` under the independent safety obligation `Ob_safety`, or an authoritatively supported `Viol(i, τ_t) = 1`): explicit contradiction of an effect expectation, safety obligation, or invariant. |
| `UNDECIDED` (U) | `UNRESOLVED` | *Epistemic query* | Epistemic insufficiency: evidence is insufficient to certify or refute the transition. |

### **4.2. Conjunctive Expectation Aggregation Algebra `(V_4, ≻, ⊗)`**

Let the bound expectation set `E = {e_1, ..., e_{n_E}}` be partitioned into **active change expectations** `E_act = {e_k ∈ E : 𝟎 ∉ φ_{exp,k}}` and **preservation (stationarity) constraints** `E_inv = {e_k ∈ E : 𝟎 ∈ φ_{exp,k}}`.

**Axiom 4.1 (Prohibition of Vacuous Truth).** For any transition `τ_t` that violates no global safety invariant (`∀i ∈ I: Viol(i, τ_t) = 0`), satisfies all bound preservation constraints (`∀e_k ∈ E_inv: Rel(e_k, τ_t) = 1 ∧ y^+(e_k, τ_t) = 1 ∧ 𝒞^+(e_k, τ_t) is valid`) under authoritative evidence scope `σ(τ_t) ∈ {OBSERVED_TRANSITION, REPLAY_VERIFIED}`, and has no active change expectations (`E_act = ∅`, which includes both `E = ∅` and purely stationary expectation sets `E = E_inv`), the aggregate verdict maps identically to `OMIT` (0):

```math
\bigl(\forall i\in I:\mathrm{Viol}(i,\tau_t)=0\bigr)\;\land\;\bigl(\forall e_k\in E_{\mathrm{inv}}:Rel(e_k,\tau_t)=1\land y^{+}(e_k,\tau_t)=1\land\mathrm{Valid}(\mathcal{C}^{+}(e_k,\tau_t))\bigr)\;\land\;(E_{\mathrm{act}}=\emptyset)\;\implies\;\mathrm{Verdict}(E,\tau_t)=\mathrm{OMIT}\ (0).
```

Each clause `e_k ∈ E` receives an individual clause verdict `v(e_k, τ_t) ∈ V_4`; the evidence scope and the global invariants `i ∈ I` contribute two transition-level factors (defined below). For an active clause `e_k ∈ E_act`, the local rule is:
- (i) `v(e_k, τ_t) = NULL (−1)` if `σ(τ_t) ∈ {OBSERVED_TRANSITION, REPLAY_VERIFIED}`, `Rel(e_k, τ_t) = 1`, and a certificate-backed incompatibility holds under the clause’s active/destructive conditions in Step 1 of §4.3;
- (ii) `v(e_k, τ_t) = UNDECIDED (U)` if `σ(τ_t) ∉ {OBSERVED_TRANSITION, REPLAY_VERIFIED}`, `Rel(e_k, τ_t) = 0`, a required certificate is missing/invalid (including a context witness `ξ_c` that cannot be derived from pre-outcome evidence, §3.2 and §5.3), an existential search is unexhausted with zero matches, or strict zero-delta stagnation occurs on an unconfirmed operator–feature pair (`χ_conf(a_k, F_k; 𝒯_{t-1}) = 0`);
- (iii) `v(e_k, τ_t) = FOLLOW (+1)` if `σ(τ_t) ∈ {OBSERVED_TRANSITION, REPLAY_VERIFIED}`, `Rel(e_k, τ_t) = 1`, `a_k = c_k = 1`, `y^+(e_k, τ_t) = 1`, and the realization/exhaustion certificate is valid;
- (iv) `v(e_k, τ_t) = OMIT (0)` for a reliably grounded, certificate-backed, resolved inessential case not covered by (i)–(iii), including blocked soft stops (`a_k = 1, c_k = 0, y^∼ = 1`), passive clauses (`a_k = 0`), and sub-threshold non-zero progress (`y^∼_sub = 1`).

For a preservation constraint `e_k ∈ E_inv`:
- `v(e_k, τ_t) = NULL (−1)` if `σ(τ_t) ∈ {OBSERVED_TRANSITION, REPLAY_VERIFIED} ∧ Rel(e_k, τ_t) = 1 ∧ y^⊥(e_k, τ_t) = 1` (backed by `𝒞^⊥`);
- `v(e_k, τ_t) = UNDECIDED (U)` if `σ(τ_t) ∉ {OBSERVED_TRANSITION, REPLAY_VERIFIED}`, `Rel(e_k, τ_t) = 0`, or a valid certificate is missing;
- `v(e_k, τ_t) = FOLLOW (+1)` (the identity element of `⊗`) if `σ(τ_t) ∈ {OBSERVED_TRANSITION, REPLAY_VERIFIED} ∧ Rel(e_k, τ_t) = 1 ∧ y^+(e_k, τ_t) = 1` backed by `𝒞^+` (i.e., preservation holds without violation, allowing the active clauses in `E_act` to determine whether the aggregate verdict is `FOLLOW` or `OMIT`).

**Transition-level factors.** The evidence scope contributes `v_scope(τ_t) = FOLLOW` if `σ(τ_t) ∈ {OBSERVED_TRANSITION, REPLAY_VERIFIED}` and `v_scope(τ_t) = UNDECIDED` otherwise. Each global invariant `i ∈ I` contributes `v(i, τ_t) = NULL` if `Viol(i, τ_t) = 1 ∧ AuthSafety(i, τ_t) = 1`; `v(i, τ_t) = UNDECIDED` if `Viol(i, τ_t) = 1 ∧ AuthSafety(i, τ_t) = 0` (an unauthenticated apparent violation is neither ignored nor certified); and `v(i, τ_t) = FOLLOW` (the neutral element) if `Viol(i, τ_t) = 0`. Let $`v_{\mathrm{inv}}(\tau_t)=\bigotimes_{i\in I}v(i,\tau_t)`$.

**Progress requirement.** Let `prog(E) = FOLLOW` if `E_act ≠ ∅` and `prog(E) = OMIT` if `E_act = ∅`. A step in which no change was required is never certified as progress (Axiom 4.1).

The aggregate base verdict is defined by the conjunctive aggregation operator `⊗`:

```math
\mathrm{Verdict}(E,\tau_t)=v_{\mathrm{scope}}(\tau_t)\otimes v_{\mathrm{inv}}(\tau_t)\otimes\Bigl(\bigotimes_{k=1}^{n_E} v(e_k,\tau_t)\Bigr)\otimes\mathrm{prog}(E),
```

where the empty `⊗`-product equals `FOLLOW`, the identity element of `⊗`. The factor `prog(E)` realizes Axiom 4.1 for `E = ∅` and for purely stationary sets `E = E_inv` without a separate case distinction. The operator `⊗` is governed by the bounded linear dominance semilattice `(V_4, ≻)`:

```math
\mathrm{NULL}(-1)\succ\mathrm{UNDECIDED}(U)\succ\mathrm{OMIT}(0)\succ\mathrm{FOLLOW}(+1)
```

where `v_1 ⊗ v_2 = max_≻(v_1, v_2)`:

| `⊗` | `FOLLOW` (+1) | `OMIT` (0) | `UNDECIDED` (U) | `NULL` (−1) |
| :--- | :--- | :--- | :--- | :--- |
| `FOLLOW` (+1) | `FOLLOW` (+1) | `OMIT` (0) | `UNDECIDED` (U) | `NULL` (−1) |
| `OMIT` (0) | `OMIT` (0) | `OMIT` (0) | `UNDECIDED` (U) | `NULL` (−1) |
| `UNDECIDED` (U) | `UNDECIDED` (U) | `UNDECIDED` (U) | `UNDECIDED` (U) | `NULL` (−1) |
| `NULL` (−1) | `NULL` (−1) | `NULL` (−1) | `NULL` (−1) | `NULL` (−1) |

Unlike Belnap’s diamond bilattice `FOUR_4` [16]—where the two non-classical values `None` and `Both` are incomparable under the truth ordering and satisfy `None ∧_truth Both = F`—the verification algebra `(V_4, ≻, ⊗)` is a **strictly linear priority chain**. This total ordering is architecturally mandatory: combining an inessential clause (`OMIT` (0)) with an epistemically uncertified clause (`UNDECIDED` (U)) must yield `UNDECIDED` (U) (never `NULL` and never `OMIT`), halting commitment until the uncertified clause is resolved, whereas a single certified contradiction (`NULL` (−1)) immediately annihilates all other statuses (including `UNDECIDED` (U) on an unrelated clause).

**Theorem 4.1 (Semilattice Soundness and Annihilation of Ambiguity).** The structure `(V_4, ⊗)` is a commutative idempotent monoid (join-semilattice under `≻`) with identity element `FOLLOW` (+1) and absorbing annihilator `NULL` (−1). Specifically, for any non-empty expectation set `E`:

```math
\exists e_k\in E:v(e_k,\tau_t)=\mathrm{NULL}\ (-1)\;\implies\;\bigotimes_{j=1}^{n_E} v(e_j,\tau_t)=\mathrm{NULL}\ (-1).
```

*Proof.* Because `≻` is a strict total order on a finite four-element set, the binary maximum operation `v_1 ⊗ v_2 = max_≻(v_1, v_2)` is associative, commutative, and idempotent (`v ⊗ v = v`). The least element under `≻`, `FOLLOW` (+1), satisfies `max_≻(FOLLOW, v) = v` for all `v ∈ V_4` (identity), while the greatest element, `NULL` (−1), satisfies `max_≻(NULL, v) = NULL` for all `v ∈ V_4`, including `v = UNDECIDED(U)`. By induction on `n_E`, the presence of at least one factor equal to `NULL` (−1) forces the entire product $`\bigotimes_{j=1}^{n_E} v(e_j,\tau_t)`$ to equal `NULL` (−1). `∎`

### **4.3. Canonical Deterministic Cascade of the Rule Interpreter**

A clause `e_k ∈ E` is defined as **reliably bound** on transition `τ_t`, denoted `Rel(e_k, τ_t) = 1`, if and only if its entity/source grounding confidence satisfies `conf(e_k, τ_t) ≥ θ_conf` and (for metric contracts) its baseline stability condition `|b^- - b| ≤ ε_base` holds (otherwise `Rel(e_k, τ_t) = 0`).

Evaluating `Verdict(E, τ_t)` for a transition `τ_t = (seq_t, ō_t, act_t, ō_{t+1})` under global invariants `I` proceeds through a fixed six-step cascade. The cascade returns both a base verdict in `V_4` and, when the base verdict is `OMIT`, a subtype. A predictive-only artifact may trigger a separate pre-action safety veto, but it is not an observed invariant violation and must not be stored as a factual `NULL` verdict. In the verdict cascade, a global violation is eligible for `NULL` only when `AuthSafety(i, τ_t) = 1`, and a clause-level violation is eligible for `NULL` only under authoritative transition scope `σ(τ_t) ∈ {OBSERVED_TRANSITION, REPLAY_VERIFIED}`; for an unverified prediction, the operational gate may block action emission while the transition-level epistemic verdict remains `UNDECIDED`.

1. **Step 1 (Global Safety and Certified Nullity Priority → `NULL`):**  
   If `∃i ∈ I: Viol(i, τ_t) = 1 ∧ AuthSafety(i, τ_t) = 1`, OR if `σ(τ_t) ∈ {OBSERVED_TRANSITION, REPLAY_VERIFIED}` and `∃e_k ∈ E` with `Rel(e_k, τ_t) = 1` backed by a valid incompatibility certificate `𝒞^⊥` or refuting exhaustion certificate `𝒞^∅`—specifically:
   - (a) active or invariant contrariety: `(e_k ∈ E_act ∧ a_k = 1 ∧ y^⊥(e_k, τ_t) = 1)` or `(e_k ∈ E_inv ∧ y^⊥(e_k, τ_t) = 1)`;
   - (b) unexplained strict stagnation on a confirmed operator–feature pair in an observed unobstructed transition: `e_k ∈ E_act ∧ a_k = 1 ∧ c_k = 1 ∧ χ_conf(a_k, F_k; 𝒯_{t-1}) = 1 ∧ y^∼_stag(e_k, τ_t) = 1`; or
   - (c) existential refutation: either closed-domain exhaustion refuting a positive existential expectation (`ϱ_pol = +`, `exhausted = true`, `N_match = 0`) or a positive match refuting a negative existential expectation (`ϱ_pol = -`, `N_match ≥ 1`)  
   `⇒` return `NULL` (−1).
2. **Step 2 (Epistemic Boundary and Ambiguity Priority → `UNDECIDED`):**  
   If `σ(τ_t) ∉ {OBSERVED_TRANSITION, REPLAY_VERIFIED}`, OR `∃e_k ∈ E: Rel(e_k, τ_t) = 0`, OR an existential expectation in `E_act` is evaluated over an unexhausted domain with zero matches (`exhausted = false` with `N_match = 0`), OR strict stagnation (`e_k ∈ E_act ∧ a_k = 1 ∧ c_k = 1 ∧ y^∼_stag(e_k, τ_t) = 1`) occurs on an **unconfirmed** operator–feature pair (`χ_conf(a_k, F_k; 𝒯_{t-1}) = 0`), OR any clause `e_k ∈ E` lacks a valid certificate required to establish its candidate outcome (including a context witness `ξ_c` that cannot be derived from pre-outcome evidence, §3.2 and §5.3), OR `∃i ∈ I: Viol(i, τ_t) = 1 ∧ AuthSafety(i, τ_t) = 0` (an unauthenticated apparent invariant violation is never silently ignored) `⇒` return `UNDECIDED` (U).
3. **Step 3 (Axiom 4.1 Priority for Absence of Active Expectations → `OMIT`):**  
   If `E_act = ∅` (with Steps 1 and 2 passed, and all `e_k ∈ E_inv` satisfying `Rel(e_k, τ_t) = 1 ∧ y^+(e_k, τ_t) = 1` with valid certificates `𝒞^+`):
   - (a) if `ψ(ō_{t+1}) = ψ(ō_t)` `⇒` return `OMIT_REDUNDANT` (0);
   - (b) else (`ψ(ō_{t+1}) ≠ ψ(ō_t)`) `⇒` return `OMIT_INCIDENTAL` (0).
4. **Step 4 (Complete Necessary Containment Check → `FOLLOW`):**  
   If `E_act ≠ ∅`, for **all** `e_k ∈ E_act` we have `a_k = 1 ∧ c_k = 1 ∧ y^+(e_k, τ_t) = 1` (including positive existential claims `ϱ_pol = +` with `N_match ≥ 1` and negative existential claims `ϱ_pol = -` with `exhausted = true`, `N_match = 0`), and for **all** `e_k ∈ E_inv` we have `y^+(e_k, τ_t) = 1`, all backed by valid certificates `𝒞^+` or `𝒞^∅` `⇒` return `FOLLOW` (+1).
5. **Step 5 (Disjoint Partition of Admissible Inessentiality and Omitted MDNF Constituents → `OMIT`):**  
   If all `e_k ∈ E` are reliably bound and epistemically resolved with valid witness certificates, and no clause triggered Step 1 or Step 2, but Step 4 did not hold (because for some `e_k ∈ E_act` either sub-threshold change `y^∼_sub(e_k, τ_t) = 1` occurred, or an obstructed/passive/omitted MDNF constituent with `a_k = 0` or `c_k = 0` occurred):
   - (a) if `∃e_k ∈ E_act: a_k = 1 ∧ c_k = 0 ∧ y^∼(e_k, τ_t) = 1` (active expectation blocked by boundary/context) `⇒` return `OMIT_BLOCKED` (0);
   - (b) else if `ψ(ō_{t+1}) = ψ(ō_t)` `⇒` return `OMIT_REDUNDANT` (0);
   - (c) else (`ψ(ō_{t+1}) ≠ ψ(ō_t)`) `⇒` return `OMIT_INCIDENTAL` (0).
6. **Step 6 (Epistemic Default Fallback → `UNDECIDED`):**  
   In all remaining cases (a move with `E_act ≠ ∅` or `E_inv ≠ ∅` that fails to satisfy Steps 3, 4, or 5) `⇒` return `UNDECIDED` (U). By Lemma 4.3 this step is unreachable when Steps 1–5 are implemented as specified; it is retained to guarantee totality under implementation faults and is defined as `UNDECIDED`, never as `OMIT`.

**Proposition 4.2 (Cascade `=` clause-wise aggregation).** For every input, the base verdict returned by the cascade equals `Verdict(E, τ_t)` of §4.2. (The `OMIT` subtype is a transition-level controller policy selected by §5.2: `OMIT_BLOCKED` has priority, followed by unchanged-descriptor `OMIT_REDUNDANT`, then `OMIT_INCIDENTAL`; it is not part of the equivalence.)

*Proof.* Write `v_k = v(e_k, τ_t)` and recall `⊗ = max_≻`. (a) The aggregate is `NULL` iff some factor is `NULL`. The factor `v_scope` is never `NULL`; `v_inv` is `NULL` iff some invariant has `Viol = 1 ∧ AuthSafety = 1`; a clause verdict is `NULL` iff rule (i) (resp. the `NULL` rule for preservation clauses) holds, i.e. exactly the clause conditions of Step 1. This is Step 1. (b) Otherwise the aggregate is `UNDECIDED` iff some factor is `UNDECIDED`: `v_scope` (non-authoritative scope), `v_inv` (`Viol = 1 ∧ AuthSafety = 0`), or a clause verdict by rule (ii) (resp. the `UNDECIDED` rule for preservation clauses). This is exactly Step 2. (c) Otherwise `v_scope = v_inv = FOLLOW` and every clause verdict lies in `{FOLLOW, OMIT}`. If `E_act = ∅`, then `prog(E) = OMIT` and all preservation clauses are `FOLLOW` (otherwise Steps 1–2 would apply), so the aggregate is `OMIT`: Step 3. (d) If `E_act ≠ ∅`, then `prog(E) = FOLLOW`, and the aggregate is `FOLLOW` iff every clause verdict is `FOLLOW`, which by rule (iii) and the `FOLLOW` rule for preservation clauses is exactly the condition of Step 4; otherwise it is `OMIT`: Step 5. `∎`

**Lemma 4.3 (Totality).** The clause-level rules, the transition-level factors, and `prog(E)` assign a verdict in `V_4` to every input, and Step 6 is unreachable.

*Proof.* For an active clause, rules (i)–(iii) are followed by the residual rule (iv); in particular `Rel = 0`, a missing certificate, or non-authoritative scope fall under (ii), so (iv) applies only to reliably grounded, certified, resolved cases. For a preservation clause, `y^∼` is impossible, so after `Rel = 1`, valid certificates, and authoritative scope the clause is either `y^+` (`FOLLOW`) or `y^⊥` (`NULL`, or `UNDECIDED` if its certificate is invalid). The operator `⊗` is total on `V_4`. By Proposition 4.2 every input is therefore handled by Steps 1–5. `∎`

---

## **5. Operational Semantics of Statuses and State Control**

### **5.1. Equivalence Kernels on Discrete Abstractions versus Step-Tolerance Relations**

Let `H` be the space of structural state descriptors `H_t = ψ(ō_t)`, and let `π_{g_obj,ℓ}: H → H_{g_obj,ℓ}` be a surjective coarse-graining projection that extracts the state components essential to goal `g_obj` at resolution scale `ℓ` [17–19]. Set-theoretically, the **equivalence kernel of `π_{g_obj,ℓ}`** is the reflexive, symmetric, and transitive equivalence relation on state pairs:

```math
\ker(\pi_{g_{\mathrm{obj}},\ell})\;\equiv\;\bigl\{(h_1,h_2)\in H\times H\;:\;\pi_{g_{\mathrm{obj}},\ell}(h_1)=\pi_{g_{\mathrm{obj}},\ell}(h_2)\bigr\}.
```

A critical mathematical distinction must be maintained between two mechanisms that produce `OMIT` (0) across discrete and continuous representations:
1. **Exact Equivalence Kernel in Discrete/Graph Representations (§6.3):** When `π_{g_obj,ℓ}` projects a symbolic state or knowledge graph onto its goal-essential subgraph (eliminating irrelevant variables or background entities), any transition `τ_t: H_t → H_{t+1}` that modifies only ignored variables satisfies `(H_t, H_{t+1}) ∈ ker(π_{g_obj,ℓ})` strictly (`π_{g_obj,ℓ}(H_{t+1}) = π_{g_obj,ℓ}(H_t)`).
2. **Step-tolerance relation in continuous metric contracts (§6.1):** For a fixed metric contract `K`, define a relation on state descriptors by $`h_1\,\mathsf{Tol}_K\,h_2\iff-\theta_{\mathrm{fail}}<\varsigma_K(\mu(h_2)-\mu(h_1))<\theta_{\mathrm{prog}}`$. This is not an equivalence kernel: in general it is non-transitive, and it is asymmetric when `θ_fail ≠ θ_prog`. Consequently, individually sub-threshold steps can accumulate over time; the step that crosses the cumulative success threshold `Δ_K^{tot,+} ≥ θ_succ` is evaluated as `FOLLOW` (+1) under the cumulative-crossing rule in §6.1.

Under both mechanisms, assigning the status `OMIT` (0) allows the controller to exclude incidental or sub-threshold steps from law-confirmation memory without deleting the underlying state change from `H_{t+1}`, preserving lossless recovery upon scale refinement `ℓ' < ℓ` (*fine-graining*).

**Definition 5.1 (Projection neutrality and treatment of `OMIT`).** A transition `τ_t: H_t → H_{t+1}` is *`π_{g_obj,ℓ}`-neutral* iff `(H_t, H_{t+1}) ∈ ker(π_{g_obj,ℓ})`, i.e. `π_{g_obj,ℓ}(H_{t+1}) = π_{g_obj,ℓ}(H_t)`. The verdict `OMIT` is assigned by the cascade of §4.3, not by the kernel test; the kernel decides how an `OMIT` node is treated in the active projection (§5.2):
1. `OMIT_REDUNDANT` transitions satisfy `H_{t+1} = H_t` and are neutral for every `(g_obj, ℓ)`.
2. An `OMIT_INCIDENTAL` node is *hidden* from the active projection if the transition is neutral. If it is not neutral (a goal-relevant change that is not attributable to the tested operator, e.g. an exogenous realization), the node remains *visible* in the projection with status `0` and is queued for expectation re-binding.
3. An `OMIT_BLOCKED` node is treated as in (2) for any change of `ψ`, and as `OMIT_REDUNDANT` when `ψ` is unchanged.

`OMIT` is not a statement that a change is irrelevant to the world; it states the absence of certified progress attributable to the tested operator.

### **5.2. Disjoint Taxonomy of `OMIT` (0) Subtypes and Controller Bijection**

In Steps 3 and 5 of the cascade (§4.3), the verdict `OMIT` (0) is deterministically mapped to one of three mutually exclusive subtypes and corresponding state-controller commands:

| `OMIT` Subtype | Strictly Disjoint Condition in Cascade (§4.3) | State-Controller Command |
| :--- | :--- | :--- |
| `OMIT_BLOCKED` | Step 5a: `E_act ≠ ∅ ∧ (∃e_k ∈ E_act: a_k = 1 ∧ c_k = 0 ∧ y^∼(e_k, τ_t) = 1)` (active expectation attempted but obstructed by external context/boundary `c_k = 0`: obstacle *soft stop* or unfulfilled conditional trigger). | `PRESERVE_LAW_AND_REPAIR_ROUTE`: Preserve confirmed laws in invariant memory without falsification, retain the trigger in the candidate pool, **halt route cursor advancement**, invoke local trajectory repair from `H_{t+1}`, and apply the repeat guard of `DROP_AND_SUPPRESS_REPEAT` to re-emission of the same action from the same descriptor. |
| `OMIT_REDUNDANT` | Step 3a or Step 5b: Not `OMIT_BLOCKED` and `ψ(ō_{t+1}) = ψ(ō_t)` (the observable structural state descriptor is invariant, or an identical node is re-submitted to the state graph). | `DROP_AND_SUPPRESS_REPEAT`: Do not allocate a duplicate state node; activate the idempotency guard (NoopRepeatGuard) to block immediate re-emission of the same no-op action in state `ψ(ō_t)`. |
| `OMIT_INCIDENTAL` | Step 3b or Step 5c: Not `OMIT_BLOCKED` and `ψ(ō_{t+1}) ≠ ψ(ō_t)` (a non-contradictory state change occurred that either lies in `ker(π_{g_obj,ℓ})`, realizes an omitted MDNF constituent with `a_k c_k = 0`, or yields sub-threshold metric change `y^∼_sub = 1`). | `RETAIN_AND_ADVANCE`: Record the node in the state graph with status `0`; hide it from the active projection `π_{g_obj,ℓ}` if the transition is `π`-neutral (Definition 5.1), otherwise keep it visible and flag it for expectation re-binding; retain it for *fine-graining*; in trajectory execution, advance the step cursor. |

Across all three subtypes, the foundational invariant holds: **no** `OMIT` **subtype increments law-confirmation counters or triggers a punitive environmental** `RESET` **or state** `ROLLBACK`.

**Recording rule.** Nodes are recorded in persistent memory only for `σ(τ_t) ∈ {OBSERVED_TRANSITION, REPLAY_VERIFIED}`; the result of a `PREDICTIVE_ONLY` evaluation is never recorded as a factual node (Non-Promotion Invariant). Status-0 nodes are retained but are not premises of `FOLLOW` chains.

### **5.3. Verification Certificates Typed by Arity and Polarity**

A verification certificate `𝒞` is a machine-checkable object binding an expectation clause `e_k ∈ E` (and its associated safety obligation `Ob_safety` when `a_k = 1, c_k = 0`) to a transition observation `τ_t` or source evidence via a witness tuple `ξ_wit = (ξ_a, ξ_c, ξ_y)`. A validator must check at least: the unique transition/source identifier and evidence scope; the clause and contract/version hashes; subject and feature-family identity; the operator and context witnesses where applicable (the context witness must be derived from pre-outcome evidence, §3.2); the observed outcome or scoped-exhaustion result; witness provenance and integrity; and the certificate type’s polarity. Missing, mismatched, stale, or unverifiable required fields make the certificate invalid and the clause `UNDECIDED`, unless an independently verified global invariant violation or another certified `NULL` clause already has priority. Reflecting the structure of MDNF constituents, certificates are partitioned into three types:
1. **Realization Certificate `𝒞^+(e_k, ξ_a, ξ_c, ξ_y)`:** Certifies the constituent `acy^+` (at Step 4), satisfied preservation `y^+` on `e_k ∈ E_inv`, or a resolved non-contradictory outcome (at Step 5), recording the operator witness `ξ_a`, context witness `ξ_c`, and outcome witness `ξ_y` (an exact document quote span, tool output, or bipartite entity delta vector).
2. **Incompatibility Certificate `𝒞^⊥(e_k, ξ_a, ξ_c, ξ_y)`:** For effect-law contradictions, the excluded MDNF constituents `(acy^⊥)_0` and `(acy^∼_stag)_0` are conjunctions of operator, context, and outcome. A destructive outcome under obstruction (`ac'y^⊥`) is certified by `𝒞^⊥` under the same contract hash `h_K` as a breach of the clause’s companion safety obligation `Ob_safety` (recording `ξ_c ⊨ c'_k = 1` and `ξ_y ⊨ y^⊥ = 1`), while flagging in metadata that `Ob_safety` rather than `Ob_effect` was violated. In all cases, `𝒞^⊥` comprises a witness triple `(ξ_a, ξ_c, ξ_y)` bound to the same subject `s_k` and feature family `F_k`:
   - for inter-document conflicts in a static text corpus (where `a_k ≡ 1, c_k ≡ 1`), `𝒞^⊥` reduces to a binary quote pair `(ξ_1, ξ_2)` with `ξ_1 ⊨ x` and `ξ_2 ⊨ y^⊥`;
   - for unexplained strict stagnation `(acy^∼_stag)_0` with `δ_obs = 𝟎`, the context witness `ξ_c` must explicitly certify `c_k = 1` (absence of boundary or obstacle contact) from pre-outcome evidence (§3.2).
3. **Polarized Scoped Exhaustion Certificate `𝒞^∅(S_scope, ρ_query, ϱ_pol, exhausted, N_match)`:** Evaluates existential expectations for query `ρ_query` with polarity `ϱ_pol ∈ {+, -}` (where `ϱ_pol = +` denotes expected existence $`\exists\omega:P_{\rho_{\mathrm{query}}}(\omega)`$ and `ϱ_pol = -` denotes asserted absence of evidence $`\neg\exists\omega:P_{\rho_{\mathrm{query}}}(\omega)`$). Across all values of `(N_match, exhausted, ϱ_pol)`, the deterministic rule evaluates to:
   - if `N_match ≥ 1` and `ϱ_pol = +` (positive match found) `⇒ y^+ = 1 ⇒ FOLLOW (+1)` (with matched witness exported as `𝒞^+`);
   - if `N_match ≥ 1` and `ϱ_pol = -` (counterexample match found refuting claimed absence) `⇒ y^⊥ = 1 ⇒ NULL (−1)` (with counterexample witness exported as `𝒞^⊥`);
   - if `N_match = 0`, `exhausted = true`, and `ϱ_pol = -` (closed domain fully scanned, absence expected) `⇒ y^+ = 1 ⇒ FOLLOW (+1)`;
   - if `N_match = 0`, `exhausted = true`, and `ϱ_pol = +` (closed domain fully scanned, presence expected) `⇒ y^⊥ = 1 ⇒ NULL (−1)`;
   - if `N_match = 0` and `exhausted = false` (open or partially scanned domain with no match yet found) `⇒ UNDECIDED (U)` for either polarity `ϱ_pol ∈ {+, -}`.

### **5.4. Two-Phase Commit and Resolution of `UNDECIDED` Without Epistemic Falsification**

1. **Pending Transition Token Invariant (`ϖ_t`):** Before emitting any action `act_t` into an external environment, the pre-action gate (Pre-Action Gate under `σ = PREDICTIVE_ONLY`) verifies admissibility and may veto a proposed action on a prospective safety warning; such a warning is recorded as a veto, not as factual `NULL`. A predictive `UNDECIDED` carries no factual credit and does not by itself block emission. The gate then registers a pending token `ϖ_t = (seq_t, hash(ō_t), act_t, h_K)`. While `ϖ_t` is active, subsequent action emission is blocked. Upon receiving `ō_{t+1}`, the transition `τ_t = (seq_t, ō_t, act_t, ō_{t+1})` with scope `σ(τ_t) = OBSERVED_TRANSITION` is evaluated exactly once by the cascade of §4.3, committed to memory, and cleared of `ϖ_t`.
2. **Liveness:** If `ō_{t+1}` is not received within the timeout `T_wait`, the pending token is closed with `σ(τ_t) = NOT_AVAILABLE` and verdict `UNDECIDED`, and the controller proceeds as in item 4.
3. **Active Probing under `UNDECIDED` (U):** An `UNDECIDED` verdict freezes route progression (and blocks state graph commit), transitioning the controller into an Evidence-Seeking Finite State Machine that dispatches diagnostic probes, tool queries, or tracker re-identifications within a bounded budget `N_probes`.
4. **Prohibition of Epistemic Falsification on Budget Exhaustion:** If the probe budget `N_probes` is exhausted or consecutive undecided evaluations reach `k_max`, **the judgment record in the audit log permanently retains the verdict** `UNDECIDED` (U) (it is never overwritten into `NULL`, preventing the fabrication of false negative invariants in memory), while the execution controller issues an operational attempt termination (`ABORT_ATTEMPT_ON_UNDECIDED`) and returns to a safe baseline state.

---

## **6. Continuous, Metric, and Graph Realizations of the Calculus**

### **6.1. Metric Verification Contracts**

Let a deterministic binder construct a measurable verification contract for an active expectation clause `e = (a, c, s, F, φ_exp) ∈ E_act`:

```math
K=(id_K,D,\mu,b_0,b,\varsigma_K,\theta_{\mathrm{prog}},\theta_{\mathrm{succ}},\theta_{\mathrm{fail}},\varepsilon_{\mathrm{base}},\theta_{\mathrm{conf}},h_K)
```

where `D` denotes target entity descriptors for subject `s`, `μ` is a registered scalar metric on feature family `F`, `b_0 = μ(ψ(ō_0); D_0)` is the route-initial metric value, `b = μ(ψ(ō_t); D_t)` is the pre-step baseline, `ς_K ∈ {-1, +1}` is the favorable improvement sign, `0 < θ_prog ≤ θ_succ` are the single-step progress threshold and cumulative goal-success threshold, `θ_fail > 0` is the failure margin, `ε_base > 0` is the baseline stability tolerance, `θ_conf ∈ (0, 1]` is the required descriptor-tracking confidence threshold, and `h_K` is the contract specification hash (covering both the effect expectation of `e` and its companion safety obligation `Ob_safety` under `a = 1, c = 0`).

Upon observing `τ_t`, the verifier re-identifies `D̂_t, D̂_{t+1}` with tracking confidence `conf(D̂, τ_t)` and computes `b^- = μ(ψ(ō_t); D̂_t)`, `b^+ = μ(ψ(ō_{t+1}); D̂_{t+1})`, the single-step directed delta `Δ_K = ς_K(b^+ - b^-)`, and the pre/post-step cumulative deltas `Δ_K^{tot,-} = ς_K(b^- - b_0)` and `Δ_K^{tot,+} = ς_K(b^+ - b_0)`.

In this metric instantiation, the reliability indicator is $`Rel(K,\tau_t)=\mathbb{I}\bigl(|b^{-}-b|\leq\varepsilon_{\mathrm{base}}\land conf(\hat{D},\tau_t)\geq\theta_{\mathrm{conf}}\land\mathrm{Cons}(K,\tau_t)\bigr)`$. Here `Cross ⇔ Δ_K^{tot,-} < θ_succ ≤ Δ_K^{tot,+}` is the **goal-crossing event** (goal success is an event, not a state: only the step that crosses the cumulative threshold can be rewarded, and a no-op after the goal is reached cannot), and the **metric–feature consistency** predicate `Cons(K, τ_t)` requires that the scalar metric and the independently tracked feature delta do not contradict each other: (i) `δ_obs(s, F; τ_t) = 𝟎 ⇒ Δ_K = 0`, and (ii) `δ_obs(s, F; τ_t) ∈ Ω_sub^K ⇒ ¬Cross ∧ Δ_K < θ_prog`. A transition violating `Cons` is epistemically unresolved (`Rel = 0`, hence `UNDECIDED`). A metric-flat change `Δ_K = 0` with `δ_obs ≠ 𝟎` remains admissible (see the convention below).

The active clause retains its admissible realization set `φ_exp`, and the contract may declare a bounded neutral set `Ω_sub^K ⊆ ℝ^d ∖ {𝟎}` of non-zero feature deltas, disjoint from `φ_exp` (empty by default). The metric thresholds *qualify* the realization set rather than contradict it: a change in `φ_exp` is a realization only if it carries threshold-significant metric progress, i.e. `δ ∈ Ω_{+,K} := {δ ∈ φ_exp : Δ_K ≥ θ_prog ∨ Cross}`; an admissible-direction change in `φ_exp` whose metric progress lies below the progress threshold (`-θ_fail < Δ_K < θ_prog`, no `Cross`) is sub-threshold neutral progress. The scalar metric alone cannot establish that a state change is small when `μ` is non-injective. Under `Rel(K, τ_t) = 1` the three consequent indicators partition by construction:
- `y^⊥(K, τ_t) = 1 ⇔ Δ_K ≤ -θ_fail ∨ δ_obs(s, F; τ_t) ∉ φ_exp ∪ {𝟎} ∪ Ω_sub^K` (reversal beyond the failure margin, or a resolved out-of-contract change);
- `y^+(K, τ_t) = 1 ⇔ y^⊥(K, τ_t) = 0 ∧ δ_obs(s, F; τ_t) ∈ Ω_{+,K}`, so that metric progress alone is insufficient when the observed change lies outside the admissible realization set;
- `y^∼(K, τ_t) = 1 ⇔ y^⊥(K, τ_t) = 0 ∧ y^+(K, τ_t) = 0`, with strict zero-delta stagnation `y^∼_stag(K, τ_t) = 1 ⇔ y^∼ = 1 ∧ δ_obs(s, F; τ_t) = 𝟎` (which implies `Δ_K = 0` by `Cons` and no intra-step transient activity on `(s, F)`), and sub-threshold change `y^∼_sub(K, τ_t) = 1 ⇔ y^∼ = 1 ∧ δ_obs(s, F; τ_t) ≠ 𝟎` (a declared neutral delta in `Ω_sub^K`, or an admissible-direction delta in `φ_exp` below the progress threshold).

Under `Rel = 1`, `y^∼ = 1` implies `-θ_fail < Δ_K < θ_prog` and `¬Cross` (by `Cons` and the definition of `Ω_{+,K}`), and `Cross` implies `Δ_K = Δ_K^{tot,+} - Δ_K^{tot,-} > 0`, so `y^⊥` and `Cross` are disjoint. An arbitrary non-zero delta is not automatically sub-threshold: it must belong to `φ_exp` or to the explicitly declared set `Ω_sub^K`.

**Convention on metric-flat changes.** A zero metric change `Δ_K = 0` does not by itself prove that the tracked feature state is unchanged: a scalar metric may be non-injective. Strict stagnation is therefore determined from the independently tracked feature delta `δ_obs(s, F; τ_t) = 𝟎`, not from `Δ_K = 0` alone. If the implementation has only the scalar metric and cannot independently establish the feature delta, it may classify the outcome as metric-flat indifference but must not label it strict zero-delta stagnation; where that distinction is required by the cascade, the verdict is `UNDECIDED`. If the contract asserts that `μ` is a faithful scalarization on the admissible feature domain, that injectivity/faithfulness assumption must be declared and validated as part of `K`. Each independently tracked feature retains its own `δ_obs`.

Given `a, c ∈ {0, 1}`, the operator–feature confirmation status `χ_conf = χ_conf(a, F; 𝒯_{t-1}) ∈ {0, 1}` (evaluated before `τ_t` is ingested, §3.4), and the certificate bundle `𝒞`, define `Valid^+(𝒞; τ_t, K)` and `Valid^⊥(𝒞; τ_t, K)` to mean that the corresponding realization or incompatibility certificate passes the typed validator in §5.3 and is bound to this transition, clause, and contract hash `h_K` (including `𝒞^⊥` issued for a destructive safety breach `a = 1, c = 0, y^⊥ = 1` under `Ob_safety`). Define `Valid^req(𝒞; τ_t, K, a, c, χ_conf)` to mean that the certificate type required by the resolved candidate outcome is present and valid. A missing or invalid required certificate makes this predicate false. The contract evaluation function `J(τ_t, K, a, c, χ_conf, 𝒞)` is the certificate-aware specialization of the cascade of §4.3 (base verdict only; `OMIT` subtype is recovered from Step 5):

```math
J(\tau_t,K,a,c,\chi_{\mathrm{conf}},\mathcal{C})=\begin{cases}
\text{FORBIDDEN (NULL)}, & \text{if }\exists i\in I:\mathrm{Viol}(i,\tau_t)=1\land AuthSafety(i,\tau_t)=1,\\
& \text{or if }\sigma(\tau_t)\in\{\mathrm{OBSERVED\_TRANSITION},\mathrm{REPLAY\_VERIFIED}\}\land Rel(K,\tau_t)=1\\
& \qquad\land a=1\land \mathrm{Valid}^{\bot}(\mathcal{C};\tau_t,K)\\
& \qquad\land\bigl(y^{\bot}(K,\tau_t)=1\lor(c=1\land\chi_{\mathrm{conf}}=1\land y^{\sim}_{\mathrm{stag}}(K,\tau_t)=1)\bigr),\\[4pt]
\text{UNRESOLVED (UNDECIDED)}, & \text{if }\sigma(\tau_t)\notin\{\mathrm{OBSERVED\_TRANSITION},\mathrm{REPLAY\_VERIFIED}\}\text{ or }Rel(K,\tau_t)=0,\\
& \text{or if }a=1\land c=1\land\chi_{\mathrm{conf}}=0\land y^{\sim}_{\mathrm{stag}}(K,\tau_t)=1,\\
& \text{or if }\exists i\in I:\mathrm{Viol}(i,\tau_t)=1\land AuthSafety(i,\tau_t)=0,\\
& \text{or if }\neg\mathrm{Valid}^{\mathrm{req}}(\mathcal{C};\tau_t,K,a,c,\chi_{\mathrm{conf}}),\\[4pt]
\text{REQUIRED (FOLLOW)}, & \text{if }a=1\land c=1\land y^{+}(K,\tau_t)=1\land\mathrm{Valid}^{+}(\mathcal{C};\tau_t,K),\\[4pt]
\text{IRRELEVANT (OMIT)}, & \text{if the outcome is resolved and }\mathrm{Valid}^{+}(\mathcal{C};\tau_t,K)\\
& \text{certifies the applicable non-contradictory, inessential case},\\[4pt]
\text{UNRESOLVED (UNDECIDED)}, & \text{otherwise.}
\end{cases}
```

When the base verdict is `OMIT`, the subtype (`BLOCKED` / `REDUNDANT` / `INCIDENTAL`) is recovered exactly as in Step 5 of the cascade by examining `a`, `c`, and equality of successive state descriptors. Because the outcome classes partition under `Rel = 1`, the final `UNDECIDED` branch is a defensive default (cf. Lemma 4.3).

### **6.2. Geometric Semantics of Predicate Boxes in `ℝ^m`**

Let entity representations be mapped by a feature grounding function `ϕ_gnd` into a compact coordinate-aligned universe box `B_U = [lo_U, hi_U] ⊂ ℝ^m` with `hi_{U,j} - lo_{U,j} ≥ 2w_min > 0` for all `j ∈ {1, ..., m}`. Each unary predicate `p ∈ P` is parameterized as a closed box `B_p = [lo_p, hi_p] ⊆ B_U` with center `ctr_{p,j} ∈ [lo_{U,j} + w_{p,j}, hi_{U,j} - w_{p,j}]` and half-widths

```math
w_{p,j}=\frac{\mathrm{hi}_{p,j}-\mathrm{lo}_{p,j}}{2}=\min\Bigl(\frac{\mathrm{hi}_{U,j}-\mathrm{lo}_{U,j}}{2},\;w_{\min}+\mathrm{softplus}(\tilde{w}_{p,j})\Bigr),
```

where `w_min ≥ γ_p > 0` enforces Carroll’s non-emptiness condition (`x_1`) not only for `B_p` itself but also for its strict `γ_p`-interior core `{z ∈ B_p : margin_p(z) ≥ γ_p} ≠ ∅`, while coordinate clamping guarantees `B_p ⊆ B_U`.

For a grounded feature vector `z ∈ B_U`, the signed membership margin in `B_p` is:

```math
\mathrm{margin}_p(z)=\min_{1\leq j\leq m}\min\{z_j-\mathrm{lo}_{p,j},\mathrm{hi}_{p,j}-z_j\}.
```

Let `Θ^⊥(p) = {r ∈ P : R(p, r) = FORB}` denote the set of predicates declared incompatible (contrary) with `p` in the ontology. Given epistemic tolerance bands `γ_p > 0`, pointwise evaluation of `z` with respect to expectation `p` is defined by four mutually exclusive and exhaustive cases:
- `∃r ∈ Θ^⊥(p): margin_r(z) ≥ γ_r ⇒ y^⊥ = 1` (`FORBIDDEN` / `NULL`);
- `y^⊥ = 0 ∧ margin_p(z) ≥ γ_p ∧ (∀r ∈ Θ^⊥(p): margin_r(z) ≤ -γ_r) ⇒ y^+ = 1` (`REQUIRED` / `FOLLOW`);
- `y^⊥ = 0 ∧ margin_p(z) ≤ -γ_p ∧ (∀r ∈ Θ^⊥(p): margin_r(z) ≤ -γ_r) ⇒ y^∼ = 1` (`IRRELEVANT` / `OMIT`);
- otherwise (the point satisfies `y^⊥ = 0` and lies in the **epistemic boundary region** relative to `p` or `Θ^⊥(p)`, i.e., `|margin_p(z)| < γ_p` or `|margin_r(z)| < γ_r` for some `r ∈ Θ^⊥(p)`) `⇒` `UNRESOLVED` (`UNDECIDED`).

At Tier 2, structural ontology specifications `R(p, q) ∈ {REQ, FORB, IRR}` are enforced by the following loss functionals:
1. **Required Entailment (`REQ`, `p ⇒ q ⇔ B_p ⊆ B_q` and `B_q ⊊ B_U`):** Enforced by the sum of the containment hinge loss with margin `ε_⇒ ≥ 0`:

```math
\mathcal{L}^{\varepsilon}_{\subseteq}(p,q)=\sum_{j=1}^m\Bigl([\mathrm{lo}_{q,j}+\varepsilon_{\Rightarrow}-\mathrm{lo}_{p,j}]_{+}+[\mathrm{hi}_{p,j}-\mathrm{hi}_{q,j}+\varepsilon_{\Rightarrow}]_{+}\Bigr)
```

   and the coordinatewise normalized non-universality barrier with relative clearance parameter `ν_max ∈ (0, 1)`:

```math
\mathcal{L}_{\mathrm{non\text{-}univ}}(q)=\Bigl[\min_{1\leq j\leq m}\Bigl(\frac{\mathrm{hi}_{q,j}-\mathrm{lo}_{q,j}}{\mathrm{hi}_{U,j}-\mathrm{lo}_{U,j}}\Bigr)-(1-\nu_{\max})\Bigr]_{+}.
```

2. **Required Incompatibility (`FORB`, `p ⊥ q ⇔ B_p ∩ B_q = ∅`):** Using the coordinatewise overlap depth `ovl_j(p, q) = min(hi_{p,j}, hi_{q,j}) - max(lo_{p,j}, lo_{q,j})` and separation clearance `ε_⊥ > 0`, the separation loss is:

```math
\mathcal{L}^{\varepsilon}_{\bot}(p,q)=\bigl[\varepsilon_{\bot}+\min_{1\leq j\leq m}\mathrm{ovl}_j(p,q)\bigr]_{+}.
```

3. **Structural Irrelevance (`IRR`):** Contributes zero penalty to the ontology loss.

**Theorem 6.1 (Soundness, Robustness, and Epistemic Clearance Consistency of Geometric Box Semantics).** For closed boxes `B_p, B_q ⊆ B_U ⊂ ℝ^m`:
1. *Containment and Perturbation Robustness:* For `ε_⇒ ≥ 0`, $`\mathcal{L}_{\subseteq}^{\varepsilon}(p,q)=0`$ holds if and only if `lo_{p,j} ≥ lo_{q,j} + ε_⇒` and `hi_{p,j} ≤ hi_{q,j} - ε_⇒` for all `j = 1, ..., m`. In particular, for `ε_⇒ = 0`, $`\mathcal{L}^{0}_{\subseteq}(p,q)=0\iff B_p\subseteq B_q`$; for `ε_⇒ > 0`, `z ∈ B_p` and `‖ζ‖_∞ ≤ ε_⇒` imply `z + ζ ∈ B_q` (the perturbed point need not remain inside `B_U` unless additional constraints on `ε_⇒` relative to the distance from `B_p` to the boundary of `B_U` are imposed).
2. *Non-Universality (`y'_1`):* For `ν_max ∈ (0, 1)`, $`\mathcal{L}_{\mathrm{non\text{-}univ}}(q)=0`$ holds if and only if along at least one coordinate axis `j ∈ {1, ..., m}` the width of `B_q` satisfies `(hi_{q,j} - lo_{q,j}) ≤ (1 - ν_max)(hi_{U,j} - lo_{U,j})`, which is necessary and sufficient for relative clearance `ν_max` in at least one dimension and guarantees `B_U ∖ B_q ≠ ∅` (Brusentsov’s condition `y'_1`).
3. *Disjointness (`(xy')_0`):* For `ε_⊥ > 0`, $`\mathcal{L}_{\bot}^{\varepsilon}(p,q)=0`$ holds if and only if `min_{1≤j≤m} ovl_j(p, q) ≤ -ε_⊥`, i.e., the boxes are separated by a gap of at least `ε_⊥` along at least one axis and hence `B_p ∩ B_q = ∅`. For `ε_⊥ = 0`, the zero-loss condition is only `min_j ovl_j(p, q) ≤ 0`; it admits boundary contact, so it does **not** guarantee that closed boxes are disjoint. Strict disjointness must use `ε_⊥ > 0`, or an equivalent explicit strict-separation constraint.
4. *Epistemic Clearance Consistency:* If $`\mathcal{L}^{\varepsilon}_{\subseteq}(p,q)=0`$ with `ε_⇒ ≥ max(0, γ_q - γ_p)`, then any point `z` satisfying `margin_p(z) ≥ γ_p` satisfies `margin_q(z) ≥ γ_q`. Furthermore, if `Θ^⊥(p) ≠ ∅` and $`\mathcal{L}^{\varepsilon}_{\bot}(p,r)=0`$ for all `r ∈ Θ^⊥(p)` with $`\varepsilon_{\bot}\geq\max_{r\in\Theta^{\bot}(p)}\gamma_r`$, then every point `z ∈ B_p` (and hence every point with `margin_p(z) ≥ γ_p`) automatically satisfies `margin_r(z) ≤ -γ_r` for all `r ∈ Θ^⊥(p)`, ensuring that the `γ_p`-core of `B_p` is strictly disjoint from the epistemic boundary bands of all contrary predicates. If `Θ^⊥(p) = ∅`, the contrary-predicate condition is vacuously true and no maximum over an empty set is evaluated.

*Proof.* (1) Since each summand `[x]_+ = max(0, x)` is non-negative, the sum in $`\mathcal{L}_{\subseteq}^{\varepsilon}(p,q)`$ vanishes if and only if every summand is non-positive: `lo_{q,j} + ε_⇒ - lo_{p,j} ≤ 0` and `hi_{p,j} - hi_{q,j} + ε_⇒ ≤ 0` (`∀j`). At `ε_⇒ = 0`, this is the definition of `B_p ⊆ B_q`. If `ε_⇒ > 0`, `z ∈ B_p`, and `|ζ_j| ≤ ε_⇒`, then `z_j + ζ_j ≥ lo_{p,j} - ε_⇒ ≥ lo_{q,j}` and `z_j + ζ_j ≤ hi_{p,j} + ε_⇒ ≤ hi_{q,j}`, so `z + ζ ∈ B_q`. (2) By `[x]_+ = 0 ⇔ x ≤ 0`, $`\mathcal{L}_{\mathrm{non\text{-}univ}}(q)=0`$ is equivalent to the existence of an axis `j*` where `(hi_{q,j*} - lo_{q,j*}) ≤ (1 - ν_max)(hi_{U,j*} - lo_{U,j*}) < hi_{U,j*} - lo_{U,j*}`; thus the projection of `B_q` on axis `j*` is a proper subset of the projection of `B_U`, implying `B_U ∖ B_q ≠ ∅`. (3) Two closed axis-aligned boxes intersect if and only if their projections overlap on every axis (`∀j: ovl_j(p, q) ≥ 0`). For `ε_⊥ > 0`, `[ε_⊥ + min_j ovl_j(p, q)]_+ = 0 ⇔ min_j ovl_j(p, q) ≤ -ε_⊥ < 0`, certifying separation by at least `ε_⊥` along some axis `j`. If `ε_⊥ = 0`, zero loss only gives `min_j ovl_j(p, q) ≤ 0`, which permits boundary contact and is insufficient for strict disjointness. (4) From (1), `z_j - lo_{q,j} ≥ z_j - lo_{p,j} + ε_⇒` and `hi_{q,j} - z_j ≥ hi_{p,j} - z_j + ε_⇒` for all `j`, so `margin_q(z) ≥ margin_p(z) + ε_⇒ ≥ γ_p + max(0, γ_q - γ_p) ≥ γ_q`. From (3), for each `r ∈ Θ^⊥(p)` there exists an axis `j*` where `min(hi_{p,j*}, hi_{r,j*}) - max(lo_{p,j*}, lo_{r,j*}) ≤ -ε_⊥`. For any `z ∈ B_p`, `lo_{p,j*} ≤ z_{j*} ≤ hi_{p,j*}`, so either `hi_{r,j*} ≤ lo_{p,j*} - ε_⊥ ≤ z_{j*} - ε_⊥` (giving `hi_{r,j*} - z_{j*} ≤ -ε_⊥`) or `lo_{r,j*} ≥ hi_{p,j*} + ε_⊥ ≥ z_{j*} + ε_⊥` (giving `z_{j*} - lo_{r,j*} ≤ -ε_⊥`); in either case `margin_r(z) ≤ -ε_⊥ ≤ -γ_r`. `∎`

### **6.3. Hierarchical Knowledge Graphs and Compositional Scale Transitions**

Let a hierarchical knowledge graph be given by the tuple `𝒢_KG = (V_KG, E_KG, Sc, S)`, where `Sc = {0, 1, ..., M}` indexes resolution scales (from finest scale `0` to coarsest scale `M`) and `S: ℰ_ℓ → {+, -, 0}` assigns ternary statuses to the set of graph elements (nodes and edges) `ℰ_ℓ` at scale `ℓ`.

At each scale `ℓ`, the element set `ℰ_ℓ` is partitioned with respect to the transition `ℓ → ℓ + 1` into essential and ignorable (coarse-grained out) subsets: $`\mathcal{E}_{\ell}=\mathcal{E}^{\mathrm{ess}}_{\ell\to\ell+1}\sqcup\mathcal{E}^{\mathrm{ign}}_{\ell\to\ell+1}`$, where the scale-`ℓ` safety invariant representation `I_ℓ` satisfies $`I_{\ell}\subseteq\mathcal{E}^{\mathrm{ess}}_{\ell\to\ell+1}`$ and `I_{ℓ+1} = π_{ℓ→ℓ+1}(I_ℓ)` across all scales `ℓ`. A surjective coarse-graining projection `π_{ℓ→ℓ+1}: ℰ_ℓ → ℰ_{ℓ+1}` maps each macro-element `u_{ℓ+1} ∈ ℰ_{ℓ+1}` to a non-empty preimage `π⁻¹_{ℓ→ℓ+1}(u_{ℓ+1}) ⊆ ℰ_ℓ`.

**Definition 6.1 (Status Transformation Law under Coarse-Graining `π_{ℓ→ℓ+1}`).** The status of a macro-element `u_{ℓ+1} ∈ ℰ_{ℓ+1}` is uniquely determined by its preimage via the exhaustive, mutually exclusive rule:

```math
S(u_{\ell+1},\ell+1)=\begin{cases}
\text{− (NULL)}, & \text{if }\exists\mathfrak{e}_{\ell}\in\pi^{-1}_{\ell\to\ell+1}(u_{\ell+1})\cap\mathcal{E}^{\mathrm{ess}}_{\ell\to\ell+1}\;:\;S(\mathfrak{e}_{\ell},\ell)=\text{−},\\[4pt]
\text{+ (FOLLOW)}, & \text{if branch − does not hold and }\exists\mathfrak{e}_{\ell}\in\pi^{-1}_{\ell\to\ell+1}(u_{\ell+1})\cap\mathcal{E}^{\mathrm{ess}}_{\ell\to\ell+1}\;:\;S(\mathfrak{e}_{\ell},\ell)=\text{+},\\[4pt]
\text{0 (OMIT)}, & \text{otherwise (i.e., when }\forall\mathfrak{e}_{\ell}\in\pi^{-1}_{\ell\to\ell+1}(u_{\ell+1})\cap\mathcal{E}^{\mathrm{ess}}_{\ell\to\ell+1}:S(\mathfrak{e}_{\ell},\ell)=\text{0}).
\end{cases}
```

*(Note on ordering polarity: In single-step conjunctive clause aggregation (§4.2), all active expectations in `E_act` must be fulfilled for the step to achieve `FOLLOW`, so `OMIT(0) ≻ FOLLOW(+1)`. In spatial/structural coarse-graining of a committed graph (§6.3), by contrast, a macro-element `u_{ℓ+1}` represents a certified state refinement if at least one of its essential micro-elements is certified (`+`) while none are contradicted (`-`), inducing the coarse-graining status order `- ≻_cg + ≻_cg 0`.)*

Contradictions confined to $`\mathcal{E}^{\mathrm{ign}}_{\ell\to\ell+1}`$ are screened into status `0` at scale `ℓ + 1` while retaining their exact micro-statuses in `S(·, ℓ)`, so they remain recoverable under fine-graining; because $`I_{\ell}\subseteq\mathcal{E}^{\mathrm{ess}}_{\ell\to\ell+1}`$, a violated global invariant is never screened.

**Proposition 6.1 (Totality and Compositionality of Coarse-Graining).**
1. Definition 6.1 is total and mutually exclusive for every status configuration in `π⁻¹_{ℓ→ℓ+1}(u_{ℓ+1})`, and any violated global invariant $`i\in I_{\ell}\subseteq\mathcal{E}^{\mathrm{ess}}_{\ell\to\ell+1}`$ bearing status `−` preserves status `−` across all coarser scales `ℓ' > ℓ`.
2. If under a two-step coarse-graining `ℓ → ℓ + 1 → ℓ + 2` the essential subsets satisfy the compatibility condition $`\mathcal{E}^{\mathrm{ess}}_{\ell\to\ell+2}=\pi^{-1}_{\ell\to\ell+1}(\mathcal{E}^{\mathrm{ess}}_{\ell+1\to\ell+2})\cap\mathcal{E}^{\mathrm{ess}}_{\ell\to\ell+1}`$, then status assignment is compositional with respect to `π_{ℓ→ℓ+2} = π_{ℓ+1→ℓ+2} ∘ π_{ℓ→ℓ+1}`: computing `S(u_{ℓ+2}, ℓ + 2)` sequentially through scale `ℓ + 1` yields the exact same status as direct projection from scale `ℓ`.

*Proof.* (1) Let $`\Pi_{\mathrm{ess}}(u_{\ell+1})=\pi^{-1}_{\ell\to\ell+1}(u_{\ell+1})\cap\mathcal{E}^{\mathrm{ess}}_{\ell\to\ell+1}`$. On `Π_ess(u_{ℓ+1})`, `S(·, ℓ)` takes values in `{-, +, 0}`. The three branches of Definition 6.1 correspond to: (a) `- ∈ S(Π_ess(u_{ℓ+1}), ℓ)`; (b) `- ∉ S(Π_ess(u_{ℓ+1}), ℓ)` and `+ ∈ S(Π_ess(u_{ℓ+1}), ℓ)`; and (c) `S(Π_ess(u_{ℓ+1}), ℓ) ⊆ {0}` (including `Π_ess(u_{ℓ+1}) = ∅` when the entire preimage lies in $`\mathcal{E}^{\mathrm{ign}}_{\ell\to\ell+1}`$). These three cases partition the power set `𝒫({-, +, 0})`. Because $`I_{\ell}\subseteq\mathcal{E}^{\mathrm{ess}}_{\ell\to\ell+1}`$ and `I_{ℓ+1} = π_{ℓ→ℓ+1}(I_ℓ)`, any `i ∈ I_ℓ` with `S(i, ℓ) = −` belongs to `Π_ess(π_{ℓ→ℓ+1}(i))` and triggers branch (a), propagating status `−` inductively to all `ℓ' > ℓ`. (2) Equipping `{-, +, 0}` with the strict total order `- ≻_cg + ≻_cg 0` on `Π_ess(u_{ℓ+1})` and identity element `0` writes Definition 6.1 as the semilattice join $`S(u_{\ell+1},\ell+1)=\max_{\succ_{\mathrm{cg}}}(\{S(\mathfrak{e}_{\ell},\ell):\mathfrak{e}_{\ell}\in\Pi_{\mathrm{ess}}(u_{\ell+1})\}\cup\{0\})`$. By associativity, commutativity, and idempotence of `max_{≻_cg}` (with `0` as least element) and the set identity

```math
\bigcup_{u_{\ell+1}\in\pi^{-1}_{\ell+1\to\ell+2}(u_{\ell+2})\cap\mathcal{E}^{\mathrm{ess}}_{\ell+1\to\ell+2}}\bigl(\pi^{-1}_{\ell\to\ell+1}(u_{\ell+1})\cap\mathcal{E}^{\mathrm{ess}}_{\ell\to\ell+1}\bigr)=\pi^{-1}_{\ell\to\ell+2}(u_{\ell+2})\cap\mathcal{E}^{\mathrm{ess}}_{\ell\to\ell+2},
```

iterating the join over `ℓ → ℓ + 1 → ℓ + 2` equals $`\max_{\succ_{\mathrm{cg}}}(\{S(\mathfrak{e}_{\ell},\ell):\mathfrak{e}_{\ell}\in\pi^{-1}_{\ell\to\ell+2}(u_{\ell+2})\cap\mathcal{E}^{\mathrm{ess}}_{\ell\to\ell+2}\}\cup\{0\})`$. `∎`

---

## **7. Constructive Guarantees and Verification Quality Metrics**

### **7.1. Constructive Architectural Theorem**

**Theorem 7.1 (Totality, Well-Definedness, State Groundedness, Rollback Consistency, and Auditability).**  
Assume the following additional conditions:
- the audit log is append-only, immutable, and complete for all committed transitions;
- the structural extractor `ψ` is a pure deterministic function of its observation argument;
- all data required for logical-state reconstruction are retained in the log, including side-effect descriptors, invariant-set versions, expectation bindings, evidence scopes, certificate payloads, and the verifier/contract version hashes;
- certificates `𝒞_t` are uniquely bound to the concrete transition identifier `seq_t` and the contract version hash;
- no unlogged external mutations of the controlled state occur between the emission of an action and the receipt of the subsequent observation;
- any claimed rollback of external effects is supported either by a transactional environment or by a separately verified compensating-action protocol. Without this last condition, the theorem guarantees logical-state restoration only, not physical reversal of external actions.

Under these assumptions, and assuming deterministic candidate parsing by the adapter and deterministic witness verification, any state-control system governed by the cascade of §4.3 and the commit protocol of §5.2–§5.4 satisfies the following conditional guarantees:
1. **Judge Totality and Uniqueness:** For every transition `τ_t`, expectation set `E`, and invariant set `I`, the cascade of §4.3 terminates and assigns a unique verdict in `V_4` (and a unique subtype in §5.2 whenever the verdict is `OMIT` (0)). Moreover, any transition with `E_act ≠ ∅` that lacks valid certificates `𝒞^+, 𝒞^⊥, 𝒞^∅` is mapped to `UNDECIDED` (U) (Step 2; Step 6 is unreachable by Lemma 4.3) or `NULL` (−1) (Step 1), never to `FOLLOW` (+1). An apparent invariant violation that is not authoritatively supported (`Viol = 1 ∧ AuthSafety = 0`) is likewise mapped to `UNDECIDED` (U) and never ignored.
2. **State Groundedness:** If the state manager commits a goal-essential state transition into the certified active state projection `𝒮_t^+` only upon receiving verdict `FOLLOW` (+1) (while recording `OMIT` nodes with status `0` outside `𝒮_t^+`, hidden or flagged but never as facts and never as premises of `FOLLOW` chains, §5.2), then at any step `T ≥ 0`, every element in `𝒮_T^+` is derived from initial state axioms `H_0` via a finite chain of authoritatively observed transitions (`σ(τ_t) ∈ {OBSERVED_TRANSITION, REPLAY_VERIFIED}`) certified with verdict `FOLLOW` (+1).
3. **Logical Rollback Consistency:** Under the pending-token protocol (`ϖ_t`, §5.4) and non-destructive retention of `OMIT_INCIDENTAL` (0) nodes (§5.2), replaying the versioned logical-state log to checkpoint index `t_chk` restores the recorded descriptor `H_{t_chk}`. This does not by itself reverse external physical/tool side effects; those are covered only when the transactional or compensating-action condition above is met.
4. **Deterministic Auditability:** Given `H_0` and a complete append-only log containing `(τ_t, E_t, I_t, 𝒞_t)`, the evidence scopes, every referenced version/hash, and the commit/controller records for `t = 0, ..., T - 1`, the logical trajectory of state descriptors `(H_1, ..., H_T)` and verdicts `(V_0, ..., V_{T-1})` is uniquely reconstructible without querying any stochastic generator.

*Proof.* (1) Steps 1–6 of §4.3 form a sequential decision list ending in a catch-all default (Step 6), ensuring termination and uniqueness of the returned verdict; by Proposition 4.2 and Lemma 4.3 the cascade coincides with the clause-wise aggregation and Step 6 is unreachable. Within `OMIT` (0) (reached only at Step 3 or Step 5), Step 5a requires `E_act ≠ ∅ ∧ (∃e_k ∈ E_act: a_k = 1 ∧ c_k = 0 ∧ y^∼ = 1)`, which is disjoint from Step 3 (`E_act = ∅`); the remaining cases of Step 3 (3a/3b) and Step 5 (5b/5c) split on the dichotomous equality `ψ(ō_{t+1}) = ψ(ō_t)` versus `ψ(ō_{t+1}) ≠ ψ(ō_t)`, proving uniqueness of the `OMIT` subtype. Because Step 4 (`FOLLOW` (+1)) explicitly requires `E_act ≠ ∅`, `σ(τ_t) ∈ {OBSERVED_TRANSITION, REPLAY_VERIFIED}` (having passed Step 2, which also excludes unauthenticated apparent invariant violations), and valid certificates `𝒞^+` or `𝒞^∅` for all `e_k ∈ E`, an uncertified move can never reach `FOLLOW` (+1).  
(2) We proceed by induction on `T`. For `T = 0`, `𝒮_0^+ ⊆ H_0` is grounded in initial state axioms by definition. Assume the invariant holds at step `t`. At step `t + 1`, a new element enters `𝒮_{t+1}^+` only if `Verdict(E_t, τ_t) = FOLLOW(+1)`. By part (1), this requires passing Step 2 (`σ(τ_t) ∈ {OBSERVED_TRANSITION, REPLAY_VERIFIED}`) and Step 4 (every `e_k ∈ E_t` is certified by `𝒞^+` or `𝒞^∅` anchored in `τ_t` and prior elements of `𝒮_t^+ ⊆ H_t`), extending the finite certified chain from `H_0` by one authoritative link.  
(3) By the `ϖ_t` lock (§5.4), at most one transition is in flight at any step, and uncertified (`NULL` / `UNDECIDED`) transitions never mutate accepted state. Because `OMIT_INCIDENTAL` nodes are appended with status `0` rather than destructively overwriting prior nodes, replaying the versioned logical-state log to index `t_chk` recovers the recorded `H_{t_chk}` identically. External effects require the independently specified compensation condition and are not reversed by log replay alone.  
(4) For each complete recorded evaluation record, the versioned extractor `ψ`, invariant set, expectation bindings, certificate validator, cascade, and deterministic controller policy are pure functions of logged inputs; induction on `t` yields unique reconstruction of the logical state descriptors and verdicts for all `t ≤ T`. `∎`

### **7.2. Canonical Suite of Verifier Evaluation Metrics**

Let an evaluation benchmark partition candidate moves into four disjoint ground-truth reference classes: three **decidable classes**—`G^+` (truly productive state refinements), `G^∼` (truly incidental/indifferent moves), and `G^⊥` (truly incompatible/false moves)—and the **epistemically undecidable class** `G^U` (moves for which available evidence is genuinely insufficient to certify or refute). Verifier performance is quantified by the following risk and coverage metrics. Group A metrics are precision-type (conditioned on the verdict) and therefore depend on the class prevalence in the benchmark; Group B metrics are rate-type (conditioned on the ground truth). A conditional metric is **undefined** when its conditioning event has probability zero; report its denominator/count alongside the estimate and do not interpret an undefined estimate as zero risk or perfect performance:

**Group A. Verdict-Conditioned Error Risks (conditioned on judge output):**
1. False Follow Rate (`FFR` — primary safety metric):

```math
\mathrm{FFR}=\mathbb{P}\bigl(\mathsf{m}\notin G^{+}\;\big\vert{}\;J(\mathsf{m})=\mathrm{FOLLOW}\bigr)
```

2. False Nullification Risk (`FNullR` — total over-nullification risk, with productive-loss sub-metric `FNullR^+`):

```math
\mathrm{FNullR}=\mathbb{P}\bigl(\mathsf{m}\notin G^{\bot}\;\big\vert{}\;J(\mathsf{m})=\mathrm{NULL}\bigr),\qquad\mathrm{FNullR}^{+}=\mathbb{P}\bigl(\mathsf{m}\in G^{+}\;\big\vert{}\;J(\mathsf{m})=\mathrm{NULL}\bigr)
```

3. False Omit Risk (`FOmitR` — total misclassification into `OMIT`, with safety-critical sub-metric `FOmitR^⊥`):

```math
\mathrm{FOmitR}=\mathbb{P}\bigl(\mathsf{m}\notin G^{\sim}\;\big\vert{}\;J(\mathsf{m})=\mathrm{OMIT}\bigr),\qquad\mathrm{FOmitR}^{\bot}=\mathbb{P}\bigl(\mathsf{m}\in G^{\bot}\;\big\vert{}\;J(\mathsf{m})=\mathrm{OMIT}\bigr)
```

**Group B. Ground-Truth-Conditioned Sensitivity and Selective Coverage:**
4. False Abstention Rate on Decidable Moves (`FAR`) and Over-Commitment Rate on Undecidable Moves (`OCR_U`):

```math
\mathrm{FAR}=\mathbb{P}\bigl(J(\mathsf{m})=\mathrm{UNDECIDED}\;\big\vert{}\;\mathsf{m}\in G^{+}\cup G^{\sim}\cup G^{\bot}\bigr),\qquad\mathrm{OCR}_U=\mathbb{P}\bigl(J(\mathsf{m})\neq\mathrm{UNDECIDED}\;\big\vert{}\;\mathsf{m}\in G^{U}\bigr)
```

5. Selective Coverage (`Cov`) [20]:

```math
\mathrm{Cov}=\mathbb{P}\bigl(J(\mathsf{m})\neq\mathrm{UNDECIDED}\bigr)
```

   maximized subject to a hard upper bound on the false-commit risk `FFR ≤ α`. The optimization is meaningful only when `FFR` is estimable from a non-empty set of `FOLLOW` predictions; if that set is empty, the constraint is not certified by assigning `FFR = 0`.

### **7.3. Scope, Limits of the Claims, and Implementation Conformance Requirements**

This specification defines a formal verification calculus; conformance of a concrete software or hardware implementation requires verifying that the system satisfies the stated operational assumptions. Specifically, a conforming implementation must test the cascade of §4.3 against an exhaustive finite case table or model checker, validate the geometric clearance constraints of §6.2 numerically, and verify certificates against versioned evidence payloads (§5.3). Theorem 4.1 and Proposition 4.2 establish the algebraic properties of the aggregation operator `⊗` and its equivalence with the cascade, while system-level safety and auditability rely jointly on the cascade and commit assumptions of Theorem 7.1. Similarly, the coarse-graining compositionality guarantee in Proposition 6.1 requires enforcing the stated compatibility condition on essential subsets across scales.

**Proved in this document:** Theorem 3.1; Theorem 4.1; Proposition 4.2; Lemma 4.3; Theorem 6.1; Proposition 6.1; and Theorem 7.1 relative to its stated assumptions.

**Not established here:**
- *Completeness, decidability, and a model-theoretic semantics* for the MDNF fragment, and a consistency proof of the full two-tier calculus.
- *Contraposition is not inherited.* The modified entailment `(ac ⇒ y)` is deliberately not contraposable (§1.4, item 2); consequently, Aristotelian syllogistic figures that rely on conversion or contraposition are not inherited by the Tier 2 calculus.
- *Empirical calibration* of `θ_prog`, `θ_succ`, `θ_fail`, `ε_base`, `θ_conf`, `ε_rev`, `ε_orth`, `N_min`, `η_tol`, `T_wait`, `N_probes`, and `k_max`; and any bound `FFR ≤ α`, which is an evaluation target (§7.2) and not a theorem.
- *Graph-level uncertainty.* The ternary status `S` of §6.3 carries no `UNDECIDED`; epistemic states at the graph level are handled at Tier 1 before a status is committed.

---

## **References**

1. Aristotle. *Prior Analytics* (Analytica Priora).
2. Carroll, L. *Symbolic Logic*. London: Macmillan and Co., 1896 (Russian ed.: Moscow: Mir, 1973).
3. Brusentsov, N. P. *Foundations of Informatics* [Nachala informatiki]. Moscow: New Millennium Foundation, 1994.
4. Brusentsov, N. P., & Vladimirova, Yu. S. Ternary Computerization of Logic. In *Mathematical Methods of Pattern Recognition (MMRO-12)*, Moscow: MAX Press, 2005.
5. Brusentsov, N. P. Reanimation of Aristotelian Syllogistics. In *Restoration of Logic*, Moscow: New Millennium Foundation, 2005.
6. Vladimirova, Yu. S. Computerization of Contentful Reasoning Based on Syllogistic Inference. *Software Systems and Tools*, No. 12, Moscow: VMK MSU, 2010.
7. Brusentsov, N. P. *Ordering of Mathematical Logic* [Uporyadochenie matematicheskoy logiki]. Moscow: New Millennium Foundation, 2011.
8. Brusentsov, N. P. *Improvement of the Logic of Inferences* [Usovershenstvovanie logiki umozaklyucheniy]. Moscow: New Millennium Foundation, 2012.
9. Poretsky, P. S. *On the Methods of Solving Logical Equalities and on the Inverse Method of Mathematical Logic* [O sposobakh resheniya logicheskikh ravenstv i ob obratnom sposobe matematicheskoy logiki]. Kazan, 1884. (Reprint: Moscow: Russkaya Pravda, 2011).
10. Hilbert, D., & Ackermann, W. *Principles of Mathematical Logic* [Grundzüge der theoretischen Logik]. Berlin: Springer, 1928 (Russian ed.: Moscow: IL, 1947).
11. Kleene, S. C. *Introduction to Metamathematics*. Amsterdam: North-Holland, 1952.
12. Łukasiewicz, J. O logice trójwartościowej [On Three-Valued Logic]. *Ruch Filozoficzny*, 5, 170–171, 1920.
13. Nicod, J. *Foundations of Geometry and Induction*. London: Kegan Paul, Trench, Trubner & Co., 1930.
14. Hempel, C. G. Studies in the Logic of Confirmation (I & II). *Mind*, 54(213–214), 1–26, 97–121, 1945.
15. Good, I. J. The White Shoe is a Red Herring. *The British Journal for the Philosophy of Science*, 17(4), 322, 1967.
16. Belnap, N. D. A Useful Four-Valued Logic. In *Modern Uses of Multiple-Valued Logic*, Dordrecht: D. Reidel, 5–37, 1977.
17. Tishby, N., Pereira, F. C., & Bialek, W. The Information Bottleneck Method. In *Proceedings of the 37th Annual Allerton Conference on Communication, Control and Computing*, 368–377, 1999.
18. Hoel, E. P., Albantakis, L., & Tononi, G. Quantifying Causal Emergence Shows That Macro Can Beat Micro. *Proceedings of the National Academy of Sciences (PNAS)*, 110(49), 19790–19795, 2013.
19. Kolchinsky, A., & Wolpert, D. H. Semantic Information, Autonomous Agency and Non-Equilibrium Statistical Physics. *Interface Focus*, 8(6), 2018.
20. Geifman, Y., & El-Yaniv, R. Selective Classification for Deep Neural Networks. In *Advances in Neural Information Processing Systems (NeurIPS)*, 2017.
21. Farquhar, S., Kossen, J., Kuhn, L., & Gal, Y. Detecting Hallucinations in Large Language Models Using Semantic Entropy. *Nature*, 630, 625–630, 2024.
22. Kalai, A. T., Nachum, O., Vempala, S. S., & Zhang, E. Why Language Models Hallucinate. *arXiv:2509.04664*, 2025.
23. Kirichenko, P., Ibrahim, M., Chaudhuri, K., & Bell, S. J. AbstentionBench: Reasoning LLMs Fail on Unanswerable Questions. In *NeurIPS*, 2025 (arXiv:2506.09038).
24. Liu, X., et al. AgentAbstain: Do LLM Agents Know When Not to Act? *arXiv:2607.10059*, 2026.
