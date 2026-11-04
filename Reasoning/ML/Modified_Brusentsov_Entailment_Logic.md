# **Modified Brusentsov Entailment Logic and Four-Valued Verdict Calculus for External State-Control Systems**

**Author:** Vladimir Yakunin  
**Version:** 1.0 (Canonical Edition — ML Engineering Adaptation with full formal fidelity)  
**Date:** 2026-10-14 (corpus-wide verdict-semantics synchronization; rendering normalization 2026-10-15)  
Document Status: Canonical Formal-Logical Specification  
Role in Repository: Canonical formal-logical foundation of the corpus. Documents that define or instantiate ternary statuses, entailment semantics, or the verdict space (FOLLOW / OMIT / NULL / UNDECIDED) cite this specification as normative; domain instantiations (Unified Implementable Model v2.0, External Ternary Judge Adapter, ARC-AGI-3 LCLD Agent V10.9, Self-Developing Runtime Research Program, Boundary Projection Theorem — geometric point/ball semantics) may refine operational mappings but must not contradict §§1–5 of this document.  
Domain: Non-classical mathematical logic, state-transition verification theory, neuro-symbolic and agentic architectures with authority separation (Propose — Judge — Commit).

# **Abstract & Architecture Overview**

The Engineering Problem:  
In standard LLM generation and agentic planning loops, models fail to maintain a hard boundary between a plausible prediction (a rollout or hypothesis) and a certified state transition (an observed fact). Once an unverified intermediate step enters the mutable working context, it corrupts subsequent tool calls, physical actions, and long-term memory writes (Farquhar et al., 2024; Kalai et al., 2025; Kirichenko et al., 2025; Liu et al., 2026). Preventing this requires an architectural separation of powers (Propose — Judge — Commit): a generator proposes candidate moves, an external deterministic Judge evaluates them under a formal contract, and a State Manager commits only certified transitions.

Why Classical Boolean Logic Fails as a Judge:  
Classical two-valued Boolean algebra and material implication (x → y ≡ ¬x ∨ y) break down as a verification contract because they conflate the *non-applicability* of a rule (¬x \= 1\) with its active confirmation (vacuous truth), and fail to distinguish logical incompatibility (a rule breach) from *incidental inessentiality* (an irrelevant side change) (Brusentsov, 2012; Hilbert & Ackermann, 1928).

What This Specification Provides:  
This document specifies a closed formal verification calculus extending N. P. Brusentsov's three-valued algebra of contentful consequence (Brusentsov, 1994, 2005, 2011, 2012; Brusentsov & Vladimirova, 2005\) and Lewis Carroll's method of indices (Carroll, 1896). It separates **Tier 1 (single-step transition evaluation)** from **Tier 2 (ensemble-level law confirmation)**, and distinguishes four operational outcomes:

* **FOLLOW (+1):** Certified productive fulfillment of all active expectations and preservation constraints.  
* **OMIT (0):** Certified ontological inessentiality (rule not invoked, soft-stopped by an obstacle, or sub-threshold neutral drift).  
* **NULL (−1):** Certified contradiction (active reversal, invariant leakage, target destruction, or unexplained stagnation on a confirmed rule).  
* **UNDECIDED (U):** Epistemic insufficiency (missing observation, low tracking confidence, or unexhausted search), which halts commitment and triggers active probing without fabricating a false negative.

# **0\. Canonical Notation Reference (ML Engineer's Cheat Sheet)**

Every symbol family used in this specification is assigned a single distinct role across all sections:

| Symbol | Mathematical Object & ML Engineering Meaning |
| :---- | :---- |
| X, O, 𝒜 | Latent state space X, raw observation space O, and global action/tool-call space 𝒜 |
| Σ\_t \= (𝒜\_t, κ\_t) | Available action surface 𝒜\_t ⊆ 𝒜 and mode/capability/resource metadata vector κ\_t at step t |
| ō\_t \= (o\_t, Σ\_t, meta\_t), H\_t \= ψ(ō\_t) ∈ H | Trusted observation packet at step t and its deterministic structural scene/assertion graph H\_t |
| 𝒮\_t^+ ⊆ H\_t | Certified active state projection committed to long-term state memory at step t |
| τ\_t \= (seq\_t, ō\_t, act\_t, ō\_{t+1}) | Single state transition record at step t with unique monotonic ID seq\_t ∈ ℕ and executed action act\_t ∈ 𝒜\_t |
| 𝒯, 𝒯\_{t-1}, 𝒯\_rel(Λ) ⊆ 𝒯 | Deduplicated set (keyed by seq\_t) of observed/replay-verified transitions, its prefix before τ\_t, and the reliably tracked subset (Rel \= 1\) for law Λ |
| σ(τ\_t), ϖ\_t | Evidentiary scope of transition τ\_t (e.g. PREDICTIVE\_ONLY vs OBSERVED\_TRANSITION) and pending transition lock token ϖ\_t |
| a ∈ {0, 1}, A ∈ {0, 1} | Boolean flag of tested operator activation (a' \= 1 − a; a(τ\_t) \= 1 iff act\_t is the tested operator) and compound antecedent A \= a\_1 ∧ ... ∧ a\_k |
| c ∈ {0, 1}, C ∈ {0, 1} | Boolean flag of unobstructed precondition context (c' \= 1 − c; computed strictly from pre-outcome state) and compound context C \= c\_1 ∧ ... ∧ c\_r |
| s, F, φ\_exp | Target entity/subject ID s, feature family F, and expected admissible change set φ\_exp |
| Alive(s, ō\_t), Alive(s, ō\_{t+1}), ι\_s | Explicit before/after entity-presence predicates and identity requirement ι\_s ∈ {PRESENT, ABSENT, PRESERVE} |
| δ\_obs(s, F; τ\_t), δ\_exp ∈ ℝ^d | Observed feature delta during τ\_t (with zero element 0\) and reference expected displacement vector δ\_exp |
| ε\_rev, ε\_orth ≥ 0 | Sign-inversion noise tolerance along active axes and leakage tolerance along orthogonal invariant axes (0 on discrete grids) |
| y^+, y^\~, y^⊥ ∈ {0, 1} | Mutually exclusive indicators of consequent fulfillment (+), neutral indifference (\~), and strong incompatibility (⊥) |
| y^\~\_stag, y^\~\_sub ∈ {0, 1} | Disjoint sub-indicators of y^\~: strict zero-delta stagnation (δ\_obs \= 0\) and non-zero change inside a declared bounded neutral region Ω\_{sub,k} |
| Ω\_{sub,k} ⊆ ℝ^d \\ {0} | Explicitly bounded, clause-specific set of non-zero changes permitted as neutral/sub-threshold (empty by default) |
| (·)\_1, (·)\_0 | Carroll–Brusentsov indices: mandatory empirical existence (1) and incompatibility / nullity (0) |
| N\_min ∈ ℕ, η\_tol ∈ \[0, 1\) | Minimum empirical support count (N\_min ≥ 1\) and observation noise tolerance in ensemble quantifiers |
| V^{(N\_min)}*𝒯, N^{(η\_tol)}*{0,𝒯}(Ψ | Γ\_cond) |
| Λ \= (AC ⇒ y), χ\_conf(A, F; 𝒯) | Universal law over 𝒯 and Boolean indicator that operator A is confirmed for feature family F on 𝒯 (evaluated on 𝒯\_{t-1} when judging τ\_t) |
| Ob\_effect, Ob\_safety | Obligations for unobstructed effect fulfillment (AC \= 1\) and obstructed non-destructiveness (AC' \= 1\) |
| Ω\_y ⊊ Ω\_𝒰 | Feature acceptance region of consequent y and ambient feature universe in the non-triviality check NonTriv(y) |
| E \= E\_act ⊔ E\_inv | Bound step expectation set E \= {e\_1, ..., e\_{n\_E}} split into active change clauses E\_act and preservation clauses E\_inv |
| I, Viol(i, τ\_t), AuthSafety(i, τ\_t) | Global safety invariant set I, violation indicator Viol ∈ {0, 1}, and authoritative safety evidence flag AuthSafety ∈ {0, 1} |
| conf(e\_k, τ\_t), θ\_conf, Rel(e\_k, τ\_t) | Grounding/tracking confidence of clause e\_k, reliability threshold θ\_conf ∈ (0, 1\], and reliability indicator Rel ∈ {0, 1} |
| V\_4, ⊗, ≻, ≻\_cg | Four-valued verdict space, conjunctive aggregation operator ⊗, strict linear dominance order ≻, and coarse-graining status order ≻\_cg |
| 𝒞, 𝒞^+, 𝒞^⊥, 𝒞^∅, ξ\_wit | Verification certificate 𝒞 of realization (+), incompatibility (⊥), or scoped exhaustion (∅), with witness tuple ξ\_wit \= (ξ\_a, ξ\_c, ξ\_y) |
| S\_scope, ρ\_query, ϱ\_pol, N\_match | Search domain ID, query specification, existential polarity ϱ\_pol ∈ {+, −}, and match count in 𝒞^∅ |
| π\_{g\_obj,ℓ}, ker(π\_{g\_obj,ℓ}), π\_{ℓ→ℓ+1} | Coarse-graining projection for goal g\_obj at scale ℓ, its equivalence kernel on H × H, and inter-scale graph projection ℓ → ℓ \+ 1 |
| K, D, D̂\_t, μ, b\_0, b, b^-, b^+, ς\_K | Metric verification contract K, target descriptors D, re-identified descriptors D̂\_t, scalar metric μ, baselines b\_0, b, evaluations b^-, b^+, improvement sign ς\_K ∈ {−1, \+1} |
| Δ\_K, Δ\_K^{tot,-}, Δ\_K^{tot,+}, Cross, Cons | Directed single-step metric change ς\_K(b^+ − b^-), cumulative changes relative to b\_0, goal-crossing event Cross, and metric–feature consistency predicate Cons (§6.1) |
| θ\_prog, θ\_succ, θ\_fail, ε\_base | Strictly positive step-progress, cumulative-success, and failure thresholds, and baseline stability tolerance in K |
| p, q, r ∈ P, ϕ\_gnd, z ∈ B\_U, B\_p | Predicate symbols in P, feature grounding map ϕ\_gnd, grounded vector z in ambient box B\_U ⊂ ℝ^m, and closed predicate box B\_p \= \[lo\_p, hi\_p\] |
| w\_{p,j}, w\_min, margin\_p(z), γ\_p, ε\_⇒, ε\_⊥, ν\_max, ovl\_j | Box half-widths, minimum half-width, signed membership margin, epistemic band γ\_p, containment/separation clearances ε\_⇒, ε\_⊥, non-universality margin ν\_max, overlap ovl\_j |
| 𝒢\_KG, Sc, ℰ\_ℓ, 𝔢\_ℓ, u\_{ℓ+1}, S(𝔢\_ℓ, ℓ) | Hierarchical knowledge graph, scale set Sc, elements ℰ\_ℓ at scale ℓ, micro-element 𝔢\_ℓ, macro-element u\_{ℓ+1}, and graph status function S |
| T\_wait, N\_probes, k\_max | Pending-token timeout, evidence-seeking probe budget, and consecutive-UNDECIDED limit (§5.4) |
| m, G^+, G^\~, G^⊥, G^U | Candidate move m and ground-truth reference classes (productive, indifferent, incompatible, undecidable) in §7.2 |

# **1\. Introduction and Theoretical Prerequisites**

## **1.1. The State-Transition Verification Problem and Defects of Material Implication**

In neuro-symbolic, agentic, and reasoning architectures, a generative model proposes sequences of intermediate assertions, trajectory steps, and tool invocations. When a generated move is admitted directly into the system state without external verification, statistically inevitable generator hallucinations (Farquhar et al., 2024; Kalai et al., 2025\) and the systematic failure of models to abstain from unsupported steps (Geifman & El-Yaniv, 2017; Kirichenko et al., 2025; Liu et al., 2026\) corrupt the state trajectory irreversibly. Preventing state corruption requires an architectural separation of powers (**Propose — Judge — Commit**): a generator proposes candidate moves, an external verifier (Judge) evaluates them under a formal contract, and a state manager commits only certified transitions.

Attempting to formalize such a verifier within classical two-valued Boolean algebra (Poretsky, 1884; Hilbert & Ackermann, 1928\) encounters three structural defects of material implication (x → y) ≡ x' ∨ y ≡ xy ∨ x'y ∨ x'y' (Brusentsov, 2012):

1. **Vacuous truth (false antecedent):** When the antecedent is false (x' \= 1, i.e., an action was not executed or its precondition did not hold), material implication x → y evaluates to `True` for any consequent y. In an agent loop, an unexecuted action would falsely confirm arbitrary rules.  
2. **Vacuous truth (empty expectation or independent consequent):** When an expectation set is empty, or when consequent y holds independently of x (y \= 1), Boolean semantics returns `True` without any causal or logical link connecting x to y.  
3. **Conflation of exclusion and inessentiality:** In a two-valued Disjunctive Normal Form (DNF), omitting a constituent signifies its impossibility (falsity) (Brusentsov, 2012). Consequently, to express entailment x ⇒ y, the constituent x'y must either be excluded — degenerating entailment into equivalence (x \= y) ≡ xy ∨ x'y' — or explicitly retained — diluting necessary consequence into material implication.

These defects do not render classical logic unsound in mathematics; they render truth-functional material implication unsuitable as a state-transition verification contract under incomplete applicability and empirical conditioning.

## **1.2. The Aristotle–Carroll–Brusentsov Lineage**

N. P. Brusentsov and Yu. S. Vladimirova (Brusentsov, 1994, 2005, 2011, 2012; Brusentsov & Vladimirova, 2005; Vladimirova, 2010\) demonstrated that Aristotle's universal affirmative judgment Axy ("All x are y" (Aristotle, Prior Analytics), expressed algebraically by the recursion x \= xy — "the attribute y necessarily belongs to every x") requires a three-valued generalization of Boolean algebra.

Applying Lewis Carroll's method of indices (Carroll, 1896\) — where the subscript 1 marks mandatory existence (class non-emptiness) and the subscript `0` marks **incompatibility / nullity** (class emptiness) — together with the postulate of coexistence of opposites in the Aristotelian universe (x\_1, x'\_1, y\_1, y'\_1), Brusentsov formulated necessary entailment x ⇒ y as the conjunction (Brusentsov, 2012):

(x ⇒ y) ≡ x\_1 ∧ (xy')\_0 ∧ y'\_1

On the four-component constituent scale (xy, xy', x'y, x'y'), this relation is encoded by the ternary vector \+-0+, and in Brusentsov's improved three-valued DNF by the expression:

(x ⇒ y) ≡ xy ∨ (xy')\_0 ∨ x'y'

Here:

* Constituents `xy` and `x'y'` carry the status of **necessarily given (+)**;  
* Constituent `(xy')_0` carries the status of **necessarily excluded (−, nullity)**;  
* Constituent `x'y` is omitted as **incidental / inessential (0, incidental)**.

## **1.3. Brusentsov Ternarity versus Łukasiewicz, Kleene, and Belnap Logics**

**Why 3-valued epistemic logics are not enough:**  
In the three-valued logics of J. Łukasiewicz (1920) and S. C. Kleene (1952), the third truth value (`1/2` or `I`) represents an **epistemic truth-value gap** due to missing information. In N. D. Belnap's four-valued logic FOUR\_4 (Belnap, 1977), epistemic states form a diamond bilattice over the presence or absence of positive and negative evidence (`{T, F, None, Both}`), where `None` and `Both` are incomparable under the truth ordering.

In Brusentsov's algebra (Brusentsov & Vladimirova, 2005; Brusentsov, 2012), the status `0` (omission of a constituent in the DNF) has a fundamentally different nature: it is an ontological status of a relation member, certifying that the member is incidental (inessential) to the law under consideration — the law holds regardless of whether that constituent is present or absent. In our calculus:

* Brusentsov's ontological inessentiality is formalized as the structural verdict **OMIT (0)**;  
* Epistemic insufficiency (lack of certification, analogous to Kleene's `I` or Belnap's `None`) is isolated as a distinct operational control signal **UNDECIDED (U)**.

## **1.4. Four Structural Limitations of Classical Brusentsov Notation Resolved Here**

Constructing a mathematically closed automated verifier requires resolving four limitations in Brusentsov's 2012 formulation:

1. **Incompatibility between pointwise (single-step) and ensemble (law-level) evaluation:** In an integral law over a universe of discourse, both classes `xy` and `x'y'` must be non-empty (vector `+-0+`). In a single observed transition τ\_t, however, the disjoint classes `xy` and `x'y'` have empty intersection (xy ∩ x'y' \= ∅) and cannot occur simultaneously. We resolve this via the Two-Tier Architecture (§2).  
2. **The Hempel–Nicod confirmation paradox ("the raven paradox"):** Because Brusentsov equates entailment with its contrapositive, Axy ≡ Ay'x' ≡ (x ⇒ y)(y' ⇒ x'), the constituent `x'y'` ("non-black non-ravens") receives the same asserted status `+` as `xy` ("black ravens"). Under J. Nicod's confirmation criterion (Nicod, 1930\) and C. G. Hempel's equivalence condition (Hempel, 1945), observing an unrelated object `x'y'` (e.g., a idle step where operator `a` was not invoked) would count as positive empirical confirmation of `x ⇒ y`. Furthermore, I. J. Good (1967) showed that passive observation depends on background population frequencies. Our verifier separates structural non-triviality `NonTriv(y)` from direct empirical trials of the active antecedent (§3.4, Theorem 3.1).  
3. **Heterogeneity of consequent negation y':** In multi-dimensional state spaces, neutral non-realization of an expected effect (`y^~`, such as halting softly against an obstacle or sub-threshold drift) must be distinguished from active contrariety (`y^⊥`, such as moving in the opposite direction, leaking into an invariant axis, or destroying the target object) (§3.1).  
4. **Lack of closure for n ≥ 3 variables:** Brusentsov's rule that the existence index `1` can be dropped in the improved DNF because "unindexed members are non-excludable" (Brusentsov, 2012, p. 6\) holds only for two variables (x, y). When a third variable (such as a context precondition `c`) is introduced, the class `xy` splits into `xyz ∨ xyz'`; the condition `x_1` requires the non-emptiness of the *union* `xyz ∪ xyz' ≠ ∅`, whereas listing both unindexed terms in Brusentsov's DNF erroneously requires both sub-classes to exist simultaneously. We restore explicit unit indexing `(acy^+)_1` (§3.3).

# **2\. Two-Tier Verification Architecture: Transition and Law**

## **2.1. Formal Process Model and Evidence Scopes**

Let a controlled process be defined by the tuple (X, O, 𝒜, Σ\_t). At each discrete step t, the system ingests a trusted observation packet ō\_t \= (o\_t, Σ\_t, meta\_t) comprising a sensory or symbolic frame o\_t ∈ O, the active action surface Σ\_t \= (𝒜\_t, κ\_t) (where 𝒜\_t ⊆ 𝒜 and κ\_t encodes active control mode, capability, and resource metadata), and synchronization telemetry meta\_t. Let H\_t \= ψ(ō\_t) ∈ H denote the deterministic structural state descriptor (an object-relation scene graph or normalized assertion graph) extracted from ō\_t.

The tuple

τ\_t \= (seq\_t, ō\_t, act\_t, ō\_{t+1})

with unique monotonic sequence identifier seq\_t ∈ ℕ and executed action act\_t ∈ 𝒜\_t is the **state transition at step t**. To capture fast intra-step dynamics, τ\_t may include a finite sub-frame sequence (o\_{t,0}, o\_{t,1}, ..., o\_{t,k}) with o\_{t,0} \= o\_t and o\_{t,k} \= o\_{t+1}, from which both static and intra-step transient feature changes δ\_obs(s, F; τ\_t) are deterministically extracted.

**Definition 2.1 (Evidence Scope).** Every transition or evaluation artifact τ\_t is assigned an evidentiary scope σ(τ\_t):

* `NOT_AVAILABLE` — observation data is missing, timed out, or corrupted;  
* `PREDICTIVE_ONLY` — generated by internal simulation (world-model rollout) or LLM proposal prior to physical or instrumental execution;  
* `OBSERVED_TRANSITION` — produced by single ingestion of an actually executed transition τ\_t;  
* `REPLAY_VERIFIED` — deterministically verified against the immutable audit log for an existing sequence identifier seq\_t.

**Non-Promotion Invariant:** No artifact with scope σ(τ\_t) \= `PREDICTIVE_ONLY` may ever be committed to long-term memory as a factual transition or included in the law-confirmation ensemble 𝒯. Furthermore, 𝒯 is a **set keyed by seq\_t**: replaying a transition updates its verification status to `REPLAY_VERIFIED` in place without duplicating the transition record in 𝒯.

## **2.2. Hierarchy of the Two Calculus Tiers**

To resolve the collision between single-step evaluation and universal rule evaluation, the calculus is partitioned into two tiers:

1. **Tier 1 (Pointwise Transition Calculus):** Maps a single transition τ\_t, given a bound expectation set E and global invariants I, into the four-valued verdict space V\_4 \= {FOLLOW, OMIT, NULL, UNDECIDED}.  
2. **Tier 2 (Integral Law Calculus):** Maps a universal hypothesis Λ \= (AC ⇒ y) over the deduplicated ensemble of authoritatively observed transitions 𝒯 \= {τ\_{t\_1}, ..., τ\_{t\_N}} (where ∀τ ∈ 𝒯: σ(τ) ∈ {OBSERVED\_TRANSITION, REPLAY\_VERIFIED}), restricted to its reliably grounded sub-ensemble 𝒯\_rel(Λ) \= {τ ∈ 𝒯 : Rel(Λ, τ) \= 1}, into an invariant lifecycle status (`CONFIRMED`, `CONTRADICTED`, `CONDITIONAL_CANDIDATE`, `UNRESOLVED`). Restricting Tier 2 evaluation to 𝒯\_rel(Λ) guarantees that epistemically uncertified transitions (judged `UNDECIDED` at Tier 1 due to Rel \= 0\) never pollute law confirmation or falsification at Tier 2\.

# **3\. Modified Brusentsov Disjunctive Normal Form (MDNF)**

## **3.1. Strictly Disjoint Ternary Consequent Splitting (y^+, y^\~, y^⊥)**

**Engineering Intuition:**  
Instead of a binary outcome ("matched expected change" vs "did not match"), every resolved clause evaluation splits into three mutually exclusive outcomes:

* `y^+ = 1`: The feature changed as expected (or stayed invariant for a preservation clause).  
* `y^⊥ = 1`: Active violation (moved the wrong way, leaked into a locked coordinate, broke an invariant, or changed outside the contract).  
* `y^~ = 1`: Neutral indifference — either strict zero change (`y^~_stag = 1`, stagnation) or a non-zero change inside an explicitly declared sub-threshold neutral zone (`y^~_sub = 1`).

Let an atomic expectation clause e\_k \= (a\_k, c\_k, s\_k, F\_k, φ\_{exp,k}) bind an operator indicator a\_k ∈ {0, 1}, a precondition context indicator c\_k ∈ {0, 1}, a specific subject (entity, graph node, variable) s\_k, a feature family F\_k, and a target change predicate φ\_{exp,k} specifying the admissible non-empty subset of observed feature changes δ\_obs(s\_k, F\_k; τ\_t). Throughout this specification, `0` denotes the zero change element of the feature-delta space. When 0 ∉ φ\_{exp,k} (an active change clause e\_k ∈ E\_act) in a d-dimensional feature space ℝ^d, φ\_{exp,k} may be parameterized by a reference expected displacement vector δ\_exp ∈ ℝ^d \\ {0}. Global task and safety constraints i ∈ I are evaluated separately by a direct violation predicate Viol(i, τ\_t) ∈ {0, 1}. An apparent violation (Viol \= 1\) is eligible for `NULL` only when authoritatively supported (AuthSafety(i, τ\_t) \= 1); an unauthenticated apparent violation is epistemically unresolved (`UNDECIDED`, §4.3 Step 2\) and is never silently ignored.

For each active clause, the contract may declare a bounded set Ω\_{sub,k} ⊆ ℝ^d \\ {0} of non-zero changes explicitly tolerated as neutral/sub-threshold. This set must be grounded in feature-space units, disjoint from φ\_{exp,k}, and must not be inferred from δ\_obs ≠ 0 alone. If no such region is specified, Ω\_{sub,k} \= ∅. For an active clause, a resolved observed change outside φ\_{exp,k} ∪ {0} ∪ Ω\_{sub,k} is incompatible (`y^⊥ = 1`) rather than automatically treated as sub-threshold.

**Definition 3.1 (Canonical Nullity Classes y^⊥).** For a bound expectation clause e\_k \= (a\_k, c\_k, s\_k, F\_k, φ\_{exp,k}), the incompatibility indicator y^⊥(e\_k, τ\_t) \= 1 holds if and only if, during transition τ\_t, at least one of the following five conditions occurs for the **same subject s\_k and feature family F\_k**:

1. **Subject identity violation:** Identity is assessed only when an explicit identity clause e^id \= (s\_k, ι\_{s\_k}) is bound, where ι\_{s\_k} ∈ {PRESENT, ABSENT, PRESERVE}, using the trusted before/after predicates Alive(s\_k, ō\_t) ∈ {0, 1} and Alive(s\_k, ō\_{t+1}) ∈ {0, 1}. Canonically, e^id is embedded in the 5-tuple clause format with feature family F\_k \= Alive and observed delta δ\_obs(s\_k, Alive; τ\_t) \= Alive(s\_k, ō\_{t+1}) − Alive(s\_k, ō\_t) ∈ {−1, 0, \+1} (so φ\_{exp,k} \= {0} places identity preservation in E\_inv, whereas active creation φ\_{exp,k} \= {+1} or removal φ\_{exp,k} \= {−1} places e^id in E\_act). The clause is incompatible (y^⊥ \= 1\) if observed presence/absence violates ι\_{s\_k}. A non-identity feature delta δ\_obs(s\_k, F\_k; τ\_t) (F\_k ≠ Alive) is undefined when s\_k is missing; the verifier must not infer identity failure from an undefined feature delta. If required presence information Alive(s\_k, ·) is unavailable, the identity clause is `UNDECIDED` rather than `NULL`.  
2. **Unintended invariant mutation:** 0 ∈ φ\_{exp,k} (stationarity or bounded-tolerance preservation required for feature F\_k of subject s\_k, i.e., e\_k ∈ E\_inv), but an out-of-bounds change δ\_obs(s\_k, F\_k; τ\_t) ∉ φ\_{exp,k} is observed (in particular, when φ\_{exp,k} \= {0}, any δ\_obs ≠ 0 yields y^⊥ \= 1).  
3. **Directional sign inversion, orthogonal axis leakage, or failure-threshold breach:** Given an active change clause (0 ∉ φ\_{exp,k}) with reference expected displacement vector δ\_exp ∈ ℝ^d \\ {0} and a non-zero observed displacement δ\_obs ∈ ℝ^d \\ {0}, there exists a coordinate axis j ∈ {1, ..., d} such that either:  
   * δ\_{exp,j} ≠ 0 ∧ sign(δ\_{exp,j}) · δ\_{obs,j} \< −ε\_rev (sign inversion beyond tolerance ε\_rev ≥ 0 on an active axis, reducing to sign(δ\_{exp,j}) · sign(δ\_{obs,j}) \< 0 when ε\_rev \= 0 on discrete grids), OR  
   * δ\_{exp,j} \= 0 ∧ \|δ\_{obs,j}\| \> ε\_orth (unintended leakage along an axis required to remain invariant, with ε\_orth \= 0 on discrete grids);  
   * OR, in a metric contract, the directed change satisfies Δ\_K ≤ −θ\_fail (evaluable only under a stable baseline and sufficient tracking confidence, §6.1).  
4. **Local state-consistency conflict:** δ\_obs(s\_k, F\_k; τ\_t) directly contradicts a previously committed `FOLLOW` assertion on the same subject s\_k and feature family F\_k.  
5. **Resolved out-of-contract active change:** For e\_k ∈ E\_act, a reliably observed change lies outside φ\_{exp,k} ∪ {0} ∪ Ω\_{sub,k}. This residual case closes the partition: a non-zero change is not neutral merely because it is non-zero; it must belong to the explicitly declared neutral region.

*(Note: Observations concerning distinct subjects s\_1 ≠ s\_2 never trigger y^⊥ for each other.)*

**Definition 3.2 (Fulfillment y^+ and Indifference y^\~ \= y^\~\_stag ∨ y^\~\_sub).** For resolved transitions where subject identity and feature delta are defined:

* `y^+(e_k, τ_t) = 1  ⟺  y^⊥(e_k, τ_t) = 0 ∧ δ_obs(s_k, F_k; τ_t) ∈ φ_{exp,k}`  
  (For any preservation constraint e\_k ∈ E\_inv where 0 ∈ φ\_{exp,k}, observing δ\_obs ∈ φ\_{exp,k} yields y^+ \= 1, whereas δ\_obs ∉ φ\_{exp,k} yields y^⊥ \= 1 by Definition 3.1 Clause 2.)  
* `y^~(e_k, τ_t) = 1  ⟺  y^⊥(e_k, τ_t) = 0 ∧ y^+(e_k, τ_t) = 0`.

By construction, for every clause e\_k and resolved transition τ\_t, the triple (y^+, y^\~, y^⊥) forms a strict partition of unity:

y^+ ∨ y^\~ ∨ y^⊥ \= 1,   and   y^u ∧ y^v \= 0   (∀ u ≠ v ∈ {+, \~, ⊥}).

Because every preservation clause e\_k ∈ E\_inv satisfies y^+ ∨ y^⊥ \= 1, the indifferent outcome y^\~(e\_k, τ\_t) \= 1 can occur only for active change clauses e\_k ∈ E\_act (0 ∉ φ\_{exp,k}). Within y^\~(e\_k, τ\_t) \= 1, we define two disjoint sub-indicators:

* **Strict zero-delta stagnation:** `y^~_stag(e_k, τ_t) = 1  ⟺  y^~(e_k, τ_t) = 1 ∧ δ_obs(s_k, F_k; τ_t) = 0`;  
* **Sub-threshold non-zero change:** `y^~_sub(e_k, τ_t) = 1  ⟺  y^~(e_k, τ_t) = 1 ∧ δ_obs(s_k, F_k; τ_t) ∈ Ω_{sub,k}`.

Thus y^\~ \= y^\~\_stag ∨ y^\~\_sub with y^\~\_stag ∧ y^\~\_sub \= 0\.

## **3.2. Contextual Antecedent c**

For any clause e\_k, let a\_k ∈ {0, 1} indicate whether the tested operator was invoked in transition τ\_t, and let c\_k ∈ {0, 1} be the Boolean indicator of an **admissible, unobstructed precondition context**:

* **c\_k \= 1:** Operator a\_k is compatible with the current control surface (Σ\_t ⊨ Σ^req), activation preconditions hold, and subject s\_k is free of boundary or obstacle contact along the action direction;  
* **c'\_k \= 1 (c\_k \= 0):** Physical boundary or obstacle contact is present (*boundary / obstacle contact*), a conditional trigger precondition is unfulfilled, or the control surface Σ\_t is incompatible.

**Independence Requirement (Anti-Post-Hoc Falsification Guard):**  
`c_k(τ_t)` must be computed strictly from `(ō_t, act_t)` and the contract, certified by a context witness ξ\_c (§5.3) derived from **pre-outcome evidence**. It must never be inferred from ō\_{t+1} or from the outcome indicators y^+, y^\~, y^⊥. Without this rule, the law `(ac ⇒ y)` would become unfalsifiable: any stagnation failure could be excused post hoc as "there must have been an obstacle (c' \= 1)". If context cannot be certified from pre-outcome evidence, the clause evaluates to `UNDECIDED` (§4.3 Step 2).

**Static domains:** In domains without actions (e.g., verifying claims against a static text corpus), the convention a\_k ≡ 1, c\_k ≡ 1 applies.

## **3.3. Canonical MDNF of Conditional Entailment (ac ⇒ y)**

In the base space of 2 × 2 × 3 \= 12 elementary constituents over {a, a'}, {c, c'}, and {y^+, y^\~, y^⊥} (with unobstructed indifferent acy^\~ split into `acy^~_stag` and `acy^~_sub`, giving 13 refined rows below), the conditional effect-entailment law `Λ = (ac ⇒ y)` is defined by the Modified Brusentsov DNF:

(ac ⇒ y) ≡ (acy^+)\_1 ∨ (acy^\~\_stag)\_0 ∨ (acy^⊥)\_0 ∨ ac'y^\~ ∨ a'y^\~

Notice that `(ac'y^⊥)_0` (destructive outcome when obstructed) is intentionally separated from the effect law Λ into a companion safety obligation Ob\_safety (§3.4). A system contract requires both Λ and `Ob_safety`, while keeping their evidence counters distinct so that soft obstacle stops (`ac'y^~`) do not dilute unobstructed effect trials.

| Constituent | Syntactic Category in MDNF | Meaning and Tier 2 Law Impact | Tier 1 Step Verdict (§4.3) |
| :---- | :---- | :---- | :---- |
| **1\. acy^+** | Unit-indexed (·)\_1 (mandatory existence) | Productive core: operator `a` in unobstructed context `c = 1` realizes `y^+`; increments law support. | `FOLLOW` (+1) |
| **2\. acy^⊥** | Zero-indexed (·)\_0 (Carrollian nullity) | Direct contrariety under unobstructed execution; falsifies effect law Λ. | `NULL` (−1) |
| **3a. acy^\~\_stag** | Zero-indexed (·)\_0 (Carrollian nullity) | Strict zero-delta stagnation (`δ_obs = 0`) in unobstructed context: falsifies Λ at Tier 2; at Tier 1 yields `NULL` on a confirmed pair `(a, F)` and `UNDECIDED` if unconfirmed. | `NULL` (−1) (if χ\_conf \= 1\) / `UNDECIDED` (U) (if χ\_conf \= 0\) |
| **3b. acy^\~\_sub** | Omitted (incidental sub-threshold step) | Non-zero change inside declared neutral region `Ω_{sub,k}`; excluded from law falsification/confirmation at Tier 2\. | `OMIT_INCIDENTAL` (0) |
| **4\. ac'y^⊥** | Separate safety obligation (Ob\_safety) | Boundary/obstacle contact causes *destructive* contrariety (subject destruction, invariant breach, or sign inversion); violates `Ob_safety`. | `NULL` (−1) under an authoritative, valid safety certificate |
| **5\. ac'y^\~** | Unindexed explicit (admissible indifference) | **Obstructed soft stop** or **inactive conditional trigger**: zero/declared neutral change under `c' = 1`; neither falsifies Λ nor violates safety. | `OMIT_BLOCKED` (0) |
| **6–7. a'cy^\~, a'c'y^\~** (absorbed as **a'y^\~**) | Unindexed explicit (admissible indifference) | Passive indifference when operator `a` is not invoked (`a' = 1`); neither confirms nor falsifies Λ. | `OMIT_REDUNDANT` (0) (if H\_{t+1} \= H\_t) or `OMIT_INCIDENTAL` (0) |
| **8–12. ac'y^+, a'cy^+, a'c'y^+, a'cy^⊥, a'c'y^⊥** | Omitted (incidental inessentiality) | Effect `y^+` or `y^⊥` caused by an external factor or another operator `b ≠ a` while `ac = 0`; incidental to effect law Λ. | `OMIT_INCIDENTAL` (0) (relative to Λ) |

**Remark (Tier separation for preservation vs active clauses):**  
A *preservation clause* (`e_k ∈ E_inv`) that is reliably certified as violated yields `NULL` at Tier 1 irrespective of `a_k`, because keeping the feature invariant is required on every step (§4.2). An *active clause* (`e_k ∈ E_act`) with `a_k = 0` was not invoked on this step and yields `OMIT` even if an external factor caused an opposite change on that feature (rows 8–12).

## **3.4. Context-Normalized Ensemble Quantifiers and Defense Against the Hempel–Nicod Paradox**

Let 𝒯 be the deduplicated ensemble of transitions with scope σ(τ) ∈ {OBSERVED\_TRANSITION, REPLAY\_VERIFIED}, and for a tested law Λ \= (AC ⇒ y) let 𝒯\_rel(Λ) \= {τ ∈ 𝒯 : Rel(Λ, τ) \= 1}. Let `Γ_AC = AC(y^+ ∨ y^⊥ ∨ y^~_stag)` denote an effective unobstructed trial of Λ (excluding incidental sub-threshold steps `ACy^~_sub`). Given a minimum empirical support threshold `N_min ∈ ℕ` (`N_min ≥ 1`) and observation noise tolerance `η_tol ∈ [0, 1)`, we define the generalized Carroll–Brusentsov ensemble quantifiers over 𝒯\_rel(Λ):

* **Existence Quantifier V^{(N\_min)}\_𝒯(Φ):**  
  `(|{ τ ∈ 𝒯_rel(Λ) : Φ(τ) = 1 }| ≥ N_min)_1`  
* **Conditional Nullity Quantifier N^{(η\_tol)}\_{0,𝒯}(Ψ \| Γ\_cond):**  
  `(|{ τ ∈ 𝒯_rel(Λ) : Ψ(τ) = 1 }| ≤ η_tol · |{ τ ∈ 𝒯_rel(Λ) : Γ_cond(τ) = 1 }|)_0`

**Convention on zero conditioning set:** If the denominator `|{τ ∈ 𝒯_rel(Λ) : Γ_cond(τ) = 1}| = 0`, the numerator is also zero and `0 ≤ η_tol · 0` holds vacuously, but this does **not** confirm the law: confirmation requires the positive-support quantifier `V^{(N_min)}_𝒯(ACy^+)` plus `NonTriv(y)`.

We define the effect obligation, safety obligation, and combined contract predicate separately:

* **Effect Obligation (`Ob_effect`):** `N^{(η_tol)}_{effect,𝒯}(A, C, y) ≡ N^{(η_tol)}_{0,𝒯}(AC(y^⊥ ∨ y^~_stag) | Γ_AC)`  
* **Safety Obligation (`Ob_safety`):** `N^{(η_tol)}_{safety,𝒯}(A, C, y) ≡ N^{(η_tol)}_{0,𝒯}(AC'y^⊥ | AC')`  
* **Combined Contract:** `N^{(η_tol)}_{contract,𝒯}(A, C, y) ≡ N^{(η_tol)}_{effect,𝒯}(A, C, y) ∧ N^{(η_tol)}_{safety,𝒯}(A, C, y)`

Let `NonTriv(y)` assert that the acceptance region of y is a proper subset of the ambient feature universe (`Ω_y ⊊ Ω_𝒰`).

**Definition 3.3 (Integral Law Status and Feature-Indexed Operator Confirmation).** The combined effect-and-safety contract for Λ \= (AC ⇒ y) on feature family F assumes exactly one of four mutually exclusive statuses over 𝒯:

* **CONTRADICTED:** if `¬N^{(η_tol)}_{contract,𝒯}(A, C, y)`  
* **CONFIRMED:** if `V^{(N_min)}_𝒯(ACy^+) ∧ N^{(η_tol)}_{contract,𝒯}(A, C, y) ∧ NonTriv(y)`  
* **CONDITIONAL\_CANDIDATE:** if `¬V^{(1)}_𝒯(AC) ∧ V^{(1)}_𝒯(AC'y^~) ∧ N^{(η_tol)}_{0,𝒯}(AC'y^⊥ | AC')`  
* **UNRESOLVED:** otherwise.

*(Mutual exclusivity note: When `CONDITIONAL_CANDIDATE` holds, `¬V^{(1)}_𝒯(AC)` implies zero unobstructed trials, so `Ob_effect` holds vacuously while `Ob_safety` is explicitly satisfied; thus the first three branches are strictly disjoint regardless of evaluation order.)*

An operator A is **confirmed for feature family F** on ensemble 𝒯, denoted `χ_conf(A, F; 𝒯) = 1`, if and only if there exists a target predicate y on feature family F such that `Status(AC ⇒ y | 𝒯) = CONFIRMED` (otherwise χ\_conf(A, F; 𝒯) \= 0). Indexing by the pair `(A, F)` ensures that an operator confirmed to move spatial position is never penalized for "stagnation" on an unrelated feature (such as color) that it was never confirmed to affect.

| Status | Meaning | Effect on Memory and on χ\_conf |
| :---- | :---- | :---- |
| `CONFIRMED` | At least N\_min positive instances; violation share ≤ η\_tol in both obligations; non-trivial y | Stored as an active invariant; `χ_conf(A, F; 𝒯) = 1` |
| `CONTRADICTED` | Violation share above η\_tol in the effect or safety obligation | Retired from active invariants (audit log retained); `χ_conf = 0` |
| `CONDITIONAL_CANDIDATE` | Operator observed only in obstructed contexts (`AC'`), without destructive violation | Kept in candidate pool awaiting an unobstructed test; `χ_conf = 0` |
| `UNRESOLVED` | Insufficient empirical evidence | Collect more evidence; `χ_conf = 0` |

**Order of operations (Causality Guard):** The confirmation flag `χ_conf` used when judging step τ\_t is evaluated on the prefix ensemble **before** τ\_t is ingested (`𝒯_{t-1}`). Only after the step verdict is fixed is τ\_t appended to 𝒯 and law statuses recomputed. Thus, if a confirmed law experiences an unexplained stagnation (`NULL` at step t), with `η_tol = 0` that counterexample transitions the law to `CONTRADICTED` after step t, so `χ_conf` becomes `0` and a subsequent identical stagnation is judged `UNDECIDED` (triggering evidence-seeking probes) rather than `NULL`.

**Theorem 3.1 (Immunity to the Hempel–Nicod Raven Paradox and Boundary Stability Across All η\_tol ∈ \[0, 1)).** For any transition ensemble 𝒯, support threshold N\_min ≥ 1, and noise tolerance η\_tol ∈ \[0, 1):

1. *Confirmation Asymmetry:* Appending to 𝒯 any number of transitions τ with A(τ) \= 0 (in particular, instances of `a'y^~` — "non-black non-ravens" (Nicod, 1930; Hempel, 1945)) leaves both `V^{(N_min)}_𝒯(ACy^+)` and `N^{(η_tol)}_{contract,𝒯}(A, C, y)` invariant and cannot promote Λ from `UNRESOLVED` to `CONFIRMED`.  
2. *Boundary Obstruction and Sub-Threshold Stability:* Appending to 𝒯 any number of obstructed soft-stop transitions (`A(τ) = 1, C'(τ) = 1, y^~(τ) = 1`) or sub-threshold transitions (`A(τ) = 1, C(τ) = 1, y^~_sub(τ) = 1`) keeps `N^{(η_tol)}_{contract,𝒯}(A, C, y)` satisfied whenever it was already satisfied, and therefore never demotes a `CONFIRMED` law to `CONTRADICTED`.

**Proof.** (1) Whenever A(τ) \= 0, the conjunctions ACy^+(τ), AC(y^⊥(τ) ∨ y^\~\_stag(τ)), AC'y^⊥(τ), and the conditioning events `Γ_AC(τ)` and `AC'(τ)` all evaluate to `0`, leaving every cardinality in `V^{(N_min)}_𝒯` and `N^{(η_tol)}_{contract,𝒯}` unchanged. Meanwhile, Brusentsov's requirement that the consequent's opposite be non-empty (y'\_1) is enforced structurally by `NonTriv(y)` (`Ω_y ⊊ Ω_𝒰`) without counting external instances `a'y^~`. (2) For any transition τ with `A(τ) = 1, C'(τ) = 1, y^~(τ) = 1`, we have `C(τ) = 0` and `y^⊥(τ) = 0`. Thus in `Ob_effect` neither numerator nor denominator changes. In Ob\_safety, the numerator \|{τ' ∈ 𝒯\_rel(Λ) : AC'y^⊥ \= 1}\| increases by 0 while the denominator `|{τ' ∈ 𝒯_rel(Λ) : AC' = 1}|` increases by at most `1`; since `η_tol ≥ 0`, the inequality `LHS ≤ η_tol · RHS` remains satisfied. Similarly, for `A(τ) = 1, C(τ) = 1, y^~_sub(τ) = 1`, all indicators `y^+, y^⊥, y^~_stag, C'` are `0`, leaving all numerators and denominators invariant. ∎

* **Remark 3.1 (Meaning of CONFIRMED):** `CONFIRMED` records empirical corroboration (at least N\_min positive instances and ≤ η\_tol violation share), not a Bayesian posterior probability.  
* **Remark 3.2 (One-directional stability):** Part (2) is a non-demotion statement. When `η_tol > 0`, appending many obstructed soft stops decreases the violation fraction inside `AC'`. Whenever violations under obstruction are hard safety exclusions (e.g., target destruction), `Ob_safety` should be evaluated with `η_tol = 0`.  
* **Remark 3.3 (Scope of immunity):** The theorem is syntactic: evidence not instantiating the antecedent cannot alter law status. It is a falsification-first status calculus, not a Bayesian confirmation measure (Good, 1967).

# **4\. Four-Valued Verdict Calculus and the Dominance Semilattice**

## **4.1. The Verdict Space V\_4**

At Tier 1, each transition τ\_t is evaluated in the four-element verdict set V\_4:

V\_4 \= { FOLLOW (+1),  OMIT (0),  NULL (−1),  UNDECIDED (U) }

| Verdict in V\_4 | Operational Alias | Graph Equivalent | Operational and Logical Meaning |
| :---- | :---- | :---- | :---- |
| `FOLLOW` (+1) | `REQUIRED` | `+` | Necessary entailment certified (`acy^+`): all active clauses in `E_act ≠ ∅` and preservation clauses in `E_inv` hold. |
| `OMIT` (0) | `IRRELEVANT` | `0` | Admissible inessentiality (`a'y^~`, `ac'y^~`, `acy^~_sub`, `E_act = ∅`, or omitted MDNF constituents): no contradiction, zero certified step progress. |
| `NULL` (−1) | `FORBIDDEN` | `-` | Certified incompatibility (`(acy^⊥)_0`, `(acy^~_stag)_0`, a destructive `ac'y^⊥` under `Ob_safety`, or an authoritative `Viol(i, τ_t) = 1`). |
| `UNDECIDED` (U) | `UNRESOLVED` | *Epistemic query* | Epistemic insufficiency: evidence is insufficient to certify or refute the transition. |

## **4.2. Conjunctive Expectation Aggregation Algebra (V\_4, ≻, ⊗)**

Let the bound expectation set E \= {e\_1, ..., e\_{n\_E}} be partitioned into **active change expectations** `E_act = {e_k ∈ E : 0 ∉ φ_{exp,k}}` and **preservation (stationarity) constraints** `E_inv = {e_k ∈ E : 0 ∈ φ_{exp,k}}`.

**Axiom 4.1 (Prohibition of Vacuous Truth).** For any transition τ\_t that violates no global safety invariant (`∀i ∈ I: Viol(i, τ_t) = 0`), satisfies all bound preservation constraints (`∀e_k ∈ E_inv: Rel(e_k, τ_t) = 1 ∧ y^+(e_k, τ_t) = 1 ∧ Valid(𝒞^+(e_k, τ_t))`) under authoritative scope `σ(τ_t) ∈ {OBSERVED_TRANSITION, REPLAY_VERIFIED}`, and has **no active change expectations** (`E_act = ∅`, which includes both `E = ∅` and purely stationary sets `E = E_inv`), the aggregate verdict maps identically to `OMIT` (0):

(∀i ∈ I: Viol \= 0\) ∧ (∀e\_k ∈ E\_inv: Rel \= 1 ∧ y^+ \= 1 ∧ Valid(𝒞^+)) ∧ (E\_act \= ∅)  ⟹  Verdict(E, τ\_t) \= OMIT (0).

**Individual Clause Verdicts `v(e_k, τ_t) ∈ V_4`:**  
For an **active clause** `e_k ∈ E_act`:

* **(i) `NULL (−1)`:** if `σ(τ_t) ∈ {OBSERVED_TRANSITION, REPLAY_VERIFIED}`, `Rel(e_k, τ_t) = 1`, and a certificate-backed incompatibility holds under Step 1 of §4.3 (`a_k = 1 ∧ y^⊥ = 1`, or `a_k = c_k = 1 ∧ χ_conf = 1 ∧ y^~_stag = 1`, or existential refutation).  
* **(ii) `UNDECIDED (U)`:** if `σ(τ_t) ∉ {OBSERVED_TRANSITION, REPLAY_VERIFIED}`, `Rel(e_k, τ_t) = 0`, a required certificate is missing/invalid (including a context witness ξ\_c not derived from pre-outcome evidence), an existential search is unexhausted with zero matches, or strict zero-delta stagnation occurs on an unconfirmed operator–feature pair (`χ_conf(a_k, F_k; 𝒯_{t-1}) = 0`).  
* **(iii) `FOLLOW (+1)`:** if `σ(τ_t) ∈ {OBSERVED_TRANSITION, REPLAY_VERIFIED}`, `Rel(e_k, τ_t) = 1`, `a_k = c_k = 1`, `y^+(e_k, τ_t) = 1`, and the realization/exhaustion certificate is valid.  
* **(iv) `OMIT (0)`:** for any reliably grounded, certificate-backed, resolved inessential case not covered by (i)–(iii), including blocked soft stops (`a_k = 1, c_k = 0, y^~ = 1`), passive clauses (`a_k = 0`), and sub-threshold non-zero progress (`y^~_sub = 1`).

For a **preservation constraint** `e_k ∈ E_inv`:

* `v(e_k, τ_t) = NULL (−1)` if `σ(τ_t) ∈ {OBSERVED_TRANSITION, REPLAY_VERIFIED} ∧ Rel(e_k, τ_t) = 1 ∧ y^⊥(e_k, τ_t) = 1` (backed by 𝒞^⊥);  
* `v(e_k, τ_t) = UNDECIDED (U)` if `σ(τ_t) ∉ {OBSERVED_TRANSITION, REPLAY_VERIFIED}`, `Rel(e_k, τ_t) = 0`, or a valid certificate is missing;  
* `v(e_k, τ_t) = FOLLOW (+1)` (the identity element of ⊗) if `σ(τ_t) ∈ {OBSERVED_TRANSITION, REPLAY_VERIFIED} ∧ Rel(e_k, τ_t) = 1 ∧ y^+(e_k, τ_t) = 1` backed by 𝒞^+.

**Transition-level factors and Progress Guard:**

* **Scope factor `v_scope(τ_t)`:** `FOLLOW` if `σ(τ_t) ∈ {OBSERVED_TRANSITION, REPLAY_VERIFIED}`, else `UNDECIDED`.  
* **Global invariant factor `v_inv(τ_t) = ⨂_{i ∈ I} v(i, τ_t)`:** where `v(i, τ_t) = NULL` if `Viol(i, τ_t) = 1 ∧ AuthSafety(i, τ_t) = 1`; `UNDECIDED` if `Viol(i, τ_t) = 1 ∧ AuthSafety(i, τ_t) = 0`; and `FOLLOW` if `Viol(i, τ_t) = 0`.  
* **Progress guard `prog(E)`:** `FOLLOW` if `E_act ≠ ∅`, and `OMIT` if `E_act = ∅` (enforcing Axiom 4.1).

The aggregate base verdict is defined by the conjunctive aggregation operator ⊗:

Verdict(E, τ\_t) \= v\_scope(τ\_t) ⊗ v\_inv(τ\_t) ⊗ ( ⨂\_{k=1}^{n\_E} v(e\_k, τ\_t) ) ⊗ prog(E),

where the operator ⊗ is governed by the bounded **linear dominance semilattice `(V_4, ≻)`**:

NULL (−1) ≻ UNDECIDED (U) ≻ OMIT (0) ≻ FOLLOW (+1),   with   v\_1 ⊗ v\_2 \= max\_≻(v\_1, v\_2).

| ⊗ | FOLLOW (+1) | OMIT (0) | UNDECIDED (U) | NULL (−1) |
| :---- | :---- | :---- | :---- | :---- |
| **FOLLOW (+1)** | `FOLLOW` (+1) | `OMIT (0)` | `UNDECIDED (U)` | `NULL (−1)` |
| **OMIT (0)** | `OMIT` (0) | `OMIT (0)` | `UNDECIDED (U)` | `NULL (−1)` |
| **UNDECIDED (U)** | `UNDECIDED` (U) | `UNDECIDED (U)` | `UNDECIDED (U)` | `NULL (−1)` |
| **NULL (−1)** | `NULL` (−1) | `NULL (−1)` | `NULL (−1)` | `NULL (−1)` |

Unlike Belnap's diamond bilattice FOUR\_4 (Belnap, 1977\) — where `None` and `Both` are incomparable — `(V_4, ≻, ⊗)` is a **strictly linear priority chain**: combining an inessential clause (`OMIT`) with an uncertified clause (`UNDECIDED`) yields `UNDECIDED` (halting commitment until resolved), whereas a single certified contradiction (`NULL`) immediately annihilates all other statuses.

**Theorem 4.1 (Semilattice Soundness and Annihilation of Ambiguity).** The structure `(V_4, ⊗)` is a commutative idempotent monoid (join-semilattice under ≻) with identity element `FOLLOW` (+1) and absorbing annihilator NULL (−1). Specifically, for any non-empty expectation set E:

∃ e\_k ∈ E : v(e\_k, τ\_t) \= NULL (−1)  ⟹  ⨂\_{j=1}^{n\_E} v(e\_j, τ\_t) \= NULL (−1).

**Proof.** Because ≻ is a strict total order on a finite four-element set, the binary maximum operation v\_1 ⊗ v\_2 \= max\_≻(v\_1, v\_2) is associative, commutative, and idempotent (v ⊗ v \= v). The least element under ≻, FOLLOW (+1), satisfies max\_≻(FOLLOW, v) \= v for all v ∈ V\_4 (identity), while the greatest element, NULL (−1), satisfies `max_≻(NULL, v) = NULL` for all `v ∈ V_4`, including `v = UNDECIDED (U)`. By induction on n\_E, at least one factor equal to `NULL` (−1) forces the entire product to equal `NULL` (−1). ∎

## **4.3. Canonical Deterministic Cascade of the Rule Interpreter**

A clause e\_k ∈ E is **reliably bound** on transition τ\_t, denoted `Rel(e_k, τ_t) = 1`, iff its entity/source grounding confidence satisfies `conf(e_k, τ_t) ≥ θ_conf` and (for metric contracts) its baseline stability condition `|b^- − b| ≤ ε_base` holds (otherwise `Rel(e_k, τ_t) = 0`).

Evaluating `Verdict(E, τ_t)` proceeds through a fixed **six-step cascade** that returns both a base verdict in V\_4 and, when the base verdict is `OMIT`, a controller subtype:

1. **Step 1 (Global Safety and Certified Nullity Priority → `NULL`):**  
   If `∃i ∈ I: Viol(i, τ_t) = 1 ∧ AuthSafety(i, τ_t) = 1`, OR if `σ(τ_t) ∈ {OBSERVED_TRANSITION, REPLAY_VERIFIED}` and `∃e_k ∈ E` with `Rel(e_k, τ_t) = 1` backed by a valid incompatibility certificate 𝒞^⊥ or refuting exhaustion certificate 𝒞^∅ — specifically:  
   * (a) **Active or invariant contrariety:** `(e_k ∈ E_act ∧ a_k = 1 ∧ y^⊥(e_k, τ_t) = 1)` or `(e_k ∈ E_inv ∧ y^⊥(e_k, τ_t) = 1)`;  
   * (b) **Unexplained strict stagnation on a confirmed pair:** `e_k ∈ E_act ∧ a_k = 1 ∧ c_k = 1 ∧ χ_conf(a_k, F_k; 𝒯_{t-1}) = 1 ∧ y^~_stag(e_k, τ_t) = 1`; or  
   * (c) **Existential refutation:** either closed-domain exhaustion refuting a positive existential expectation (`ϱ_pol = +`, `exhausted = true`, `N_match = 0`) or a positive match refuting a negative existential expectation (`ϱ_pol = −`, `N_match ≥ 1`)  
     `⇒ return NULL (−1)`.  
2. **Step 2 (Epistemic Boundary and Ambiguity Priority → `UNDECIDED`):**  
   If `σ(τ_t) ∉ {OBSERVED_TRANSITION, REPLAY_VERIFIED}`, OR `∃e_k ∈ E: Rel(e_k, τ_t) = 0`, OR an existential expectation in `E_act` is evaluated over an unexhausted domain with zero matches (`exhausted = false` with `N_match = 0`), OR strict stagnation (`e_k ∈ E_act ∧ a_k = 1 ∧ c_k = 1 ∧ y^~_stag(e_k, τ_t) = 1`) occurs on an **unconfirmed** operator–feature pair (`χ_conf(a_k, F_k; 𝒯_{t-1}) = 0`), OR any clause `e_k ∈ E` lacks a valid required certificate (including a pre-outcome context witness ξ\_c), OR `∃i ∈ I: Viol(i, τ_t) = 1 ∧ AuthSafety(i, τ_t) = 0`  
   `⇒ return UNDECIDED (U)`.  
3. **Step 3 (Axiom 4.1 Priority for Absence of Active Expectations → `OMIT`):**  
   If `E_act = ∅` (with Steps 1 and 2 passed, and all `e_k ∈ E_inv` satisfying `Rel = 1 ∧ y^+ = 1` with valid certificates 𝒞^+):  
   * (a) if `ψ(ō_{t+1}) = ψ(ō_t)` `⇒ return OMIT_REDUNDANT (0)`;  
   * (b) else (`ψ(ō_{t+1}) ≠ ψ(ō_t)`) `⇒ return OMIT_INCIDENTAL (0)`.  
4. **Step 4 (Complete Necessary Containment Check → `FOLLOW`):**  
   If `E_act ≠ ∅`, for **all** `e_k ∈ E_act` we have `a_k = 1 ∧ c_k = 1 ∧ y^+(e_k, τ_t) = 1` (including positive existential claims `ϱ_pol = +` with `N_match ≥ 1` and negative existential claims `ϱ_pol = −` with `exhausted = true, N_match = 0`), and for **all** `e_k ∈ E_inv` we have `y^+(e_k, τ_t) = 1`, all backed by valid certificates 𝒞^+ or 𝒞^∅  
   `⇒ return FOLLOW (+1)`.  
5. **Step 5 (Disjoint Partition of Admissible Inessentiality → `OMIT`):**  
   If all `e_k ∈ E` are reliably bound and epistemically resolved with valid certificates, and no clause triggered Step 1 or Step 2, but Step 4 did not hold (because for some `e_k ∈ E_act` either sub-threshold change `y^~_sub = 1` occurred, or an obstructed/passive/omitted constituent with `a_k = 0` or `c_k = 0` occurred):  
   * (a) if `∃e_k ∈ E_act: a_k = 1 ∧ c_k = 0 ∧ y^~(e_k, τ_t) = 1` `⇒ return OMIT_BLOCKED (0)`;  
   * (b) else if `ψ(ō_{t+1}) = ψ(ō_t)` `⇒ return OMIT_REDUNDANT (0)`;  
   * (c) else (`ψ(ō_{t+1}) ≠ ψ(ō_t)`) `⇒ return OMIT_INCIDENTAL (0)`.  
6. **Step 6 (Epistemic Default Fallback → `UNDECIDED`):**  
   In all remaining cases `⇒ return UNDECIDED (U)`. (By Lemma 4.3, Step 6 is unreachable when Steps 1–5 are implemented as specified; it is retained as a defensive totality guard.)

```py
# Reference Implementation of the 6-Step Normative Cascade (§4.3)
def evaluate_cascade(tau_t, E_act, E_inv, invariants_I, history_T_prev):
    is_auth_scope = tau_t.scope in ("OBSERVED_TRANSITION", "REPLAY_VERIFIED")

    # Step 1: Global Safety and Certified Nullity Priority -> NULL
    if any(i.violated(tau_t) and i.auth_safety(tau_t) for i in invariants_I):
        return ("NULL", None)
    if is_auth_scope:
        for e in E_act + E_inv:
            if e.rel(tau_t) == 1 and e.has_valid_null_or_refuting_cert(tau_t):
                if (e in E_inv and e.y_perp(tau_t) == 1) or (e in E_act and e.a == 1 and e.y_perp(tau_t) == 1):
                    return ("NULL", None)
                if e in E_act and e.a == 1 and e.c == 1 and e.is_confirmed(history_T_prev) and e.y_stag(tau_t) == 1:
                    return ("NULL", None)
                if e in E_act and e.is_existential_refuted(tau_t):
                    return ("NULL", None)

    # Step 2: Epistemic Boundary and Ambiguity Priority -> UNDECIDED
    if not is_auth_scope:
        return ("UNDECIDED", None)
    if any(i.violated(tau_t) and not i.auth_safety(tau_t) for i in invariants_I):
        return ("UNDECIDED", None)
    for e in E_act + E_inv:
        if e.rel(tau_t) == 0 or not e.has_valid_required_cert(tau_t):
            return ("UNDECIDED", None)
        if e in E_act and e.is_unexhausted_zero_match(tau_t):
            return ("UNDECIDED", None)
        if e in E_act and e.a == 1 and e.c == 1 and not e.is_confirmed(history_T_prev) and e.y_stag(tau_t) == 1:
            return ("UNDECIDED", None)

    # Step 3: Axiom 4.1 Vacuous Truth Guard (E_act is empty) -> OMIT
    if len(E_act) == 0:
        subtype = "OMIT_REDUNDANT" if tau_t.H_next == tau_t.H_curr else "OMIT_INCIDENTAL"
        return ("OMIT", subtype)

    # Step 4: Complete Necessary Containment Check -> FOLLOW
    if all(e.a == 1 and e.c == 1 and e.y_plus(tau_t) == 1 for e in E_act) and all(e.y_plus(tau_t) == 1 for e in E_inv):
        return ("FOLLOW", None)

    # Step 5: Disjoint Partition of Admissible Inessentiality -> OMIT
    if any(e.a == 1 and e.c == 0 and e.y_tilde(tau_t) == 1 for e in E_act):
        return ("OMIT", "OMIT_BLOCKED")
    elif tau_t.H_next == tau_t.H_curr:
        return ("OMIT", "OMIT_REDUNDANT")
    else:
        return ("OMIT", "OMIT_INCIDENTAL")
```

**Proposition 4.2 (Cascade \= clause-wise aggregation).** For every input, the base verdict returned by the cascade equals `Verdict(E, τ_t)` of §4.2. (The `OMIT` subtype is a transition-level controller policy selected by §5.2: OMIT\_BLOCKED has priority, followed by unchanged-descriptor OMIT\_REDUNDANT, then OMIT\_INCIDENTAL.)

Proof. Write `v_k = v(e_k, τ_t)` and recall `⊗ = max_≻`. (a) The aggregate is `NULL` iff some factor is `NULL`. `v_scope` is never `NULL`; `v_inv` is `NULL` iff some invariant has `Viol = 1 ∧ AuthSafety = 1`; a clause verdict is `NULL` iff rule (i) (or the preservation `NULL` rule) holds — matching Step 1\. (b) Otherwise the aggregate is `UNDECIDED` iff some factor is `UNDECIDED`: `v_scope` (non-authoritative scope), `v_inv` (`Viol = 1 ∧ AuthSafety = 0`), or a clause verdict by rule (ii) — matching Step 2\. (c) Otherwise v\_scope \= v\_inv \= FOLLOW and every clause verdict lies in `{FOLLOW, OMIT}`. If `E_act = ∅`, then `prog(E) = OMIT` and all preservation clauses are `FOLLOW`, so the aggregate is `OMIT` — matching Step 3\. (d) If `E_act ≠ ∅`, then `prog(E) = FOLLOW`, and the aggregate is `FOLLOW` iff every clause verdict is `FOLLOW` (Step 4); otherwise it is `OMIT` (Step 5). ∎

**Lemma 4.3 (Totality).** The clause-level rules, transition-level factors, and prog(E) assign a verdict in V\_4 to every input, and Step 6 is unreachable.

Proof. For an active clause, rules (i)–(iii) are followed by the residual rule (iv); `Rel = 0`, a missing certificate, or non-authoritative scope fall under (ii), so (iv) applies only to reliably grounded, certified, resolved cases. For a preservation clause, y^\~ is impossible, so after Rel \= 1, valid certificates, and authoritative scope the clause is either y^+ (FOLLOW) or y^⊥ (NULL, or UNDECIDED if its certificate is invalid). The operator ⊗ is total on V\_4. By Proposition 4.2 every input is handled by Steps 1–5. ∎

# **5\. Operational Semantics of Statuses and State Control**

## **5.1. Equivalence Kernels on Discrete Abstractions versus Step-Tolerance Relations**

Let H be the space of structural state descriptors H\_t \= ψ(ō\_t), and let `π_{g_obj,ℓ}: H → H_{g_obj,ℓ}` be a surjective coarse-graining projection that extracts the state components essential to goal `g_obj` at resolution scale `ℓ` (Tishby et al., 1999; Hoel et al., 2013; Kolchinsky & Wolpert, 2018). Set-theoretically, the **equivalence kernel of `π_{g_obj,ℓ}`** is the reflexive, symmetric, and transitive equivalence relation on state pairs:

ker(π\_{g\_obj,ℓ}) ≡ { (h\_1, h\_2) ∈ H × H : π\_{g\_obj,ℓ}(h\_1) \= π\_{g\_obj,ℓ}(h\_2) }.

A critical mathematical distinction must be maintained between two mechanisms that produce `OMIT` (0):

1. **Exact Equivalence Kernel in Discrete/Graph Representations (§6.3):** When `π_{g_obj,ℓ}` projects a symbolic state or knowledge graph onto its goal-essential subgraph (eliminating irrelevant variables or background entities), any transition `τ_t: H_t → H_{t+1}` modifying only ignored variables satisfies `(H_t, H_{t+1}) ∈ ker(π_{g_obj,ℓ})` strictly (`π_{g_obj,ℓ}(H_{t+1}) = π_{g_obj,ℓ}(H_t)`).  
2. **Step-tolerance relation in continuous metric contracts (§6.1):** For a fixed metric contract K, define a relation on state descriptors by `h_1 Tol_K h_2 ⟺ −θ_fail < ς_K(μ(h_2) − μ(h_1)) < θ_prog`. **This is not an equivalence kernel:** in general it is non-transitive (small steps accumulate\!), and asymmetric when `θ_fail ≠ θ_prog`. Consequently, individually sub-threshold steps can accumulate over time; the step that crosses the cumulative success threshold `Δ_K^{tot,+} ≥ θ_succ` is evaluated as `FOLLOW` (+1) under the cumulative-crossing rule in §6.1.

**Definition 5.1 (Projection neutrality and treatment of OMIT).** A transition `τ_t: H_t → H_{t+1}` is *`π_{g_obj,ℓ}`\-neutral* iff (H\_t, H\_{t+1}) ∈ ker(π\_{g\_obj,ℓ}). The verdict `OMIT` is assigned by the cascade of §4.3, not by the kernel test; the kernel decides how an OMIT node is treated in the active projection (§5.2):

1. `OMIT_REDUNDANT` transitions satisfy `H_{t+1} = H_t` and are neutral for every `(g_obj, ℓ)`.  
2. An `OMIT_INCIDENTAL` node is *hidden* from the active projection if the transition is neutral. If it is not neutral (a goal-relevant change caused exogenously rather than by the tested operator), the node remains *visible* in the projection with status `0` and is queued for expectation re-binding.  
3. An `OMIT_BLOCKED` node is treated as in (2) for any change of ψ, and as `OMIT_REDUNDANT` when ψ is unchanged.

## **5.2. Disjoint Taxonomy of OMIT (0) Subtypes and Controller Bijection**

In Steps 3 and 5 of the cascade (§4.3), the verdict `OMIT` (0) is deterministically mapped to one of three mutually exclusive subtypes and corresponding state-controller commands:

| OMIT Subtype | Strictly Disjoint Condition in Cascade (§4.3) | State-Controller Command & Action |
| :---- | :---- | :---- |
| **`OMIT_BLOCKED`** | Step 5a: `E_act ≠ ∅ ∧ (∃e_k ∈ E_act: a_k = 1 ∧ c_k = 0 ∧ y^~(e_k, τ_t) = 1)` (active expectation attempted but obstructed by external context/boundary `c_k = 0`: obstacle soft stop or unfulfilled trigger). | **`PRESERVE_LAW_AND_REPAIR_ROUTE`**: Preserve confirmed laws in invariant memory without falsification, retain trigger in candidate pool, **halt route cursor advancement**, invoke local trajectory repair from H\_{t+1}, and block immediate repeat of the same action from the same descriptor. |
| **`OMIT_REDUNDANT`** | Step 3a or Step 5b: Not `OMIT_BLOCKED` and `ψ(ō_{t+1}) = ψ(ō_t)` (observable structural state descriptor is invariant, or duplicate node submitted). | **`DROP_AND_SUPPRESS_REPEAT`**: Do not allocate a duplicate state node; activate idempotency guard (`NoopRepeatGuard`) to block immediate re-emission of the same no-op action in state ψ(ō\_t). |
| **`OMIT_INCIDENTAL`** | Step 3b or Step 5c: Not `OMIT_BLOCKED` and `ψ(ō_{t+1}) ≠ ψ(ō_t)` (non-contradictory state change that lies in `ker(π_{g_obj,ℓ})`, realizes an omitted constituent with `a_k c_k = 0`, or yields sub-threshold change `y^~_sub = 1`). | **`RETAIN_AND_ADVANCE`**: Record node in state graph with status `0`; hide from active projection `π_{g_obj,ℓ}` if `π`\-neutral (Def 5.1), else keep visible and flag for expectation re-binding; retain for fine-graining; advance route step cursor. |

**Foundational Invariant across all OMIT subtypes:** No `OMIT` subtype ever increments law-confirmation counters or triggers a punitive environmental `RESET` or state `ROLLBACK`. Nodes are recorded in persistent memory only for `σ(τ_t) ∈ {OBSERVED_TRANSITION, REPLAY_VERIFIED}`.

## **5.3. Verification Certificates Typed by Arity and Polarity**

A verification certificate 𝒞 is a machine-checkable object binding an expectation clause `e_k ∈ E` (and its companion safety obligation `Ob_safety` when `a_k = 1, c_k = 0`) to a transition observation τ\_t or source evidence via a witness tuple `ξ_wit = (ξ_a, ξ_c, ξ_y)`. A validator must check: unique transition/source ID and evidence scope; clause and contract/version hashes; subject and feature-family identity; operator and context witnesses (where `ξ_c` must be derived from pre-outcome evidence, §3.2); observed outcome or scoped-exhaustion result; witness provenance/integrity; and polarity. Missing, mismatched, stale, or unverifiable fields invalidate the certificate and force `UNDECIDED` (unless overridden by an independently certified `NULL`).

1. **Realization Certificate `𝒞^+(e_k, ξ_a, ξ_c, ξ_y)`:** Certifies constituent `acy^+` (Step 4), satisfied preservation `y^+` on `e_k ∈ E_inv`, or a resolved non-contradictory outcome (Step 5), recording operator witness `ξ_a`, context witness `ξ_c`, and outcome witness `ξ_y`.  
2. **Incompatibility Certificate `𝒞^⊥(e_k, ξ_a, ξ_c, ξ_y)`:** Certifies effect-law contradictions `(acy^⊥)_0` and `(acy^~_stag)_0`, or a destructive outcome under obstruction (`ac'y^⊥`) as a breach of `Ob_safety` under the same contract hash `h_K` (flagging in metadata whether `Ob_safety` or `Ob_effect` failed). For unexplained strict stagnation `(acy^~_stag)_0`, `ξ_c` must explicitly certify `c_k = 1` (no obstacle contact) from pre-outcome evidence.  
3. **Polarized Scoped Exhaustion Certificate `𝒞^∅(S_scope, ρ_query, ϱ_pol, exhausted, N_match)`:** Evaluates existential expectations for query `ρ_query` with polarity `ϱ_pol ∈ {+, −}` (`+` for expected existence `∃ω: P(ω)`, `−` for asserted absence `¬∃ω: P(ω)`):  
   * `N_match ≥ 1` and `ϱ_pol = +` `⇒ y^+ = 1 ⇒ FOLLOW (+1)` (exporting matched witness as 𝒞^+);  
   * `N_match ≥ 1` and `ϱ_pol = −` `⇒ y^⊥ = 1 ⇒ NULL (−1)` (counterexample refutes claimed absence, exported as 𝒞^⊥);  
   * `N_match = 0`, `exhausted = true`, and `ϱ_pol = −` `⇒ y^+ = 1 ⇒ FOLLOW (+1)` (closed domain fully scanned, absence confirmed);  
   * `N_match = 0`, `exhausted = true`, and `ϱ_pol = +` `⇒ y^⊥ = 1 ⇒ NULL (−1)` (closed domain fully scanned, expected item absent);  
   * `N_match = 0` and `exhausted = false` `⇒ UNDECIDED (U)` for either polarity `ϱ_pol ∈ {+, −}`.

## **5.4. Two-Phase Commit and Resolution of UNDECIDED Without Epistemic Falsification**

1. **Pending Transition Token Invariant (`ϖ_t`):** Before emitting any action `act_t` into an external environment, the Pre-Action Gate (under `σ = PREDICTIVE_ONLY`) verifies admissibility and may veto a proposed action on a prospective safety warning (recorded as a veto, never as factual `NULL`). The gate then registers a pending lock token `ϖ_t = (seq_t, hash(ō_t), act_t, h_K)`. While `ϖ_t` is active, subsequent action emission is blocked. Upon receiving `ō_{t+1}`, transition `τ_t` with scope `OBSERVED_TRANSITION` is evaluated once by the cascade of §4.3, committed to memory, and cleared of `ϖ_t`.  
2. **Liveness:** If `ō_{t+1}` is not received within timeout `T_wait`, the pending token is closed with `σ(τ_t) = NOT_AVAILABLE` and verdict `UNDECIDED`, proceeding to item 4\.  
3. **Active Probing under `UNDECIDED` (U):** An `UNDECIDED` verdict freezes route progression and blocks state graph commit, transitioning the controller into an Evidence-Seeking Finite State Machine that dispatches diagnostic probes, tool queries, or tracker re-identifications within a bounded budget `N_probes`.  
4. **Prohibition of Epistemic Falsification on Budget Exhaustion:** If `N_probes` is exhausted or consecutive undecided evaluations reach `k_max`, **the judgment record in the audit log permanently retains the verdict `UNDECIDED` (U)** (never overwritten to `NULL`, preventing fabrication of false negative invariants in memory), while the execution controller issues `ABORT_ATTEMPT_ON_UNDECIDED` and returns to a safe baseline state.

# **6\. Continuous, Metric, and Graph Realizations of the Calculus**

## **6.1. Metric Verification Contracts**

Let a deterministic binder construct a measurable verification contract for an active expectation clause e \= (a, c, s, F, φ\_exp) ∈ E\_act:

K \= (id\_K, D, μ, b\_0, b, ς\_K, θ\_prog, θ\_succ, θ\_fail, ε\_base, θ\_conf, h\_K)

where `D` denotes target entity descriptors for subject `s`, `μ` is a registered scalar metric on feature family F, b\_0 \= μ(ψ(ō\_0); D\_0) is the route-initial metric value, b \= μ(ψ(ō\_t); D\_t) is the pre-step baseline, `ς_K ∈ {−1, +1}` is the favorable improvement sign, `0 < θ_prog ≤ θ_succ` are the single-step progress and cumulative goal-success thresholds, `θ_fail > 0` is the failure margin, `ε_base > 0` is the baseline stability tolerance, `θ_conf ∈ (0, 1]` is the tracking confidence threshold, and `h_K` is the contract hash.

Upon observing `τ_t`, the verifier re-identifies `D̂_t, D̂_{t+1}` with confidence `conf(D̂, τ_t)` and computes `b^- = μ(ψ(ō_t); D̂_t)`, `b^+ = μ(ψ(ō_{t+1}); D̂_{t+1})`, single-step directed delta `Δ_K = ς_K(b^+ − b^-)`, and cumulative deltas `Δ_K^{tot,-} = ς_K(b^- − b_0)` and `Δ_K^{tot,+} = ς_K(b^+ − b_0)`.

* **Reliability Indicator:** `Rel(K, τ_t) = 𝕀(|b^- − b| ≤ ε_base ∧ conf(D̂, τ_t) ≥ θ_conf ∧ Cons(K, τ_t))`.  
* **Goal-Crossing Event (`Cross`):** `Cross ⟺ Δ_K^{tot,-} < θ_succ ≤ Δ_K^{tot,+}` (goal success is an event, not a static state: only the step crossing the threshold is rewarded; a no-op after reaching the goal is not).  
* **Metric–Feature Consistency (`Cons`):** Requires `(i) δ_obs(s, F; τ_t) = 0 ⟹ Δ_K = 0`, and `(ii) δ_obs(s, F; τ_t) ∈ Ω_sub^K ⟹ ¬Cross ∧ Δ_K < θ_prog`. Violating `Cons` forces `Rel = 0` (`UNDECIDED`).

Define the qualified realization set Ω\_{+,K} := {δ ∈ φ\_exp : Δ\_K ≥ θ\_prog ∨ Cross}. Under Rel(K, τ\_t) \= 1, the three consequent indicators partition by construction:

* `y^⊥(K, τ_t) = 1  ⟺  Δ_K ≤ −θ_fail ∨ δ_obs(s, F; τ_t) ∉ φ_exp ∪ {0} ∪ Ω_sub^K`;  
* `y^+(K, τ_t) = 1  ⟺  y^⊥(K, τ_t) = 0 ∧ δ_obs(s, F; τ_t) ∈ Ω_{+,K}`;  
* `y^~(K, τ_t) = 1  ⟺  y^⊥(K, τ_t) = 0 ∧ y^+(K, τ_t) = 0`, split into strict stagnation `y^~_stag = 1 ⟺ y^~ = 1 ∧ δ_obs = 0` and sub-threshold change `y^~_sub = 1 ⟺ y^~ = 1 ∧ δ_obs ≠ 0`.

**Convention on metric-flat changes:** Because a scalar metric `μ` may be non-injective, `Δ_K = 0` alone does not prove `δ_obs = 0`. Strict stagnation requires establishing δ\_obs(s, F; τ\_t) \= 0 on the tracked feature (or an explicit validated injectivity declaration in `K`); if that distinction is required by the cascade and unavailable, the verdict is UNDECIDED.

Given a, c ∈ {0, 1}, prior confirmation flag χ\_conf \= χ\_conf(a, F; 𝒯\_{t-1}), and certificate bundle 𝒞, the contract evaluation function `J(τ_t, K, a, c, χ_conf, 𝒞)` specializes the §4.3 cascade directly:

* **`FORBIDDEN (NULL)`:** if an authoritative global safety violation holds (`Viol = 1 ∧ AuthSafety = 1`), OR if `σ(τ_t)` is authoritative, `Rel(K, τ_t) = 1`, `a = 1`, `Valid^⊥(𝒞; τ_t, K)` holds, and `(y^⊥ = 1 ∨ (c = 1 ∧ χ_conf = 1 ∧ y^~_stag = 1))`.  
* **`UNRESOLVED (UNDECIDED)`:** if `σ(τ_t)` is non-authoritative, or `Rel(K, τ_t) = 0`, or `(a = 1 ∧ c = 1 ∧ χ_conf = 0 ∧ y^~_stag = 1)`, or `(Viol = 1 ∧ AuthSafety = 0)`, or `¬Valid^req(𝒞; τ_t, K, a, c, χ_conf)`.  
* **`REQUIRED (FOLLOW)`:** if `a = 1 ∧ c = 1 ∧ y^+(K, τ_t) = 1 ∧ Valid^+(𝒞; τ_t, K)`.  
* **`IRRELEVANT (OMIT)`:** if the outcome is resolved and `Valid^+(𝒞; τ_t, K)` certifies the applicable non-contradictory, inessential case (with subtype `BLOCKED / REDUNDANT / INCIDENTAL` recovered from Step 5).

## **6.2. Geometric Semantics of Predicate Boxes in ℝ^m**

**Engineering Intuition:**  
In box embeddings, each unary predicate `p` is represented as an axis-aligned hyperrectangle `B_p = [lo_p, hi_p]` inside a bounded ambient box B\_U ⊂ ℝ^m. Entailment p ⇒ q means box B\_p sits inside box B\_q (B\_p ⊆ B\_q), while incompatibility p ⊥ q means the boxes are disjoint (B\_p ∩ B\_q \= ∅). Adding an epistemic margin band `γ_p > 0` around each box face creates a buffer zone: points deep inside B\_p are FOLLOW, points inside a contrary box B\_r are NULL, points well outside both are OMIT, and points near a box boundary (\|margin\| \< γ) are `UNDECIDED`.

Let entity representations be mapped by `ϕ_gnd` into a compact coordinate-aligned universe box B\_U \= \[lo\_U, hi\_U\] ⊂ ℝ^m with `hi_{U,j} − lo_{U,j} ≥ 2w_min > 0` for all `j ∈ {1, ..., m}`. Each unary predicate `p ∈ P` is parameterized as a closed box `B_p = [lo_p, hi_p] ⊆ B_U` with center `ctr_{p,j} ∈ [lo_{U,j} + w_{p,j}, hi_{U,j} − w_{p,j}]` and half-widths:

w\_{p,j} \= (hi\_{p,j} − lo\_{p,j}) / 2 \= min( (hi\_{U,j} − lo\_{U,j}) / 2,  w\_min \+ softplus(w̃\_{p,j}) ),

where `w_min ≥ γ_p > 0` enforces Carroll's non-emptiness condition (`x_1`) both for `B_p` and for its strict `γ_p`\-interior core `{z ∈ B_p : margin_p(z) ≥ γ_p} ≠ ∅`.

For a grounded feature vector `z ∈ B_U`, the signed membership margin in `B_p` is:

margin\_p(z) \= min\_{1 ≤ j ≤ m} min{ z\_j − lo\_{p,j},  hi\_{p,j} − z\_j }.

Let Θ^⊥(p) \= {r ∈ P : R(p, r) \= FORB} denote the set of predicates declared incompatible with p. Given epistemic tolerance bands γ\_p \> 0, pointwise evaluation of z with respect to expectation p is defined by four mutually exclusive and exhaustive cases:

* **FORBIDDEN (`NULL`, y^⊥ \= 1):** `∃r ∈ Θ^⊥(p): margin_r(z) ≥ γ_r`  
* **REQUIRED (`FOLLOW`, y^+ \= 1):** `y^⊥ = 0 ∧ margin_p(z) ≥ γ_p ∧ (∀r ∈ Θ^⊥(p): margin_r(z) ≤ −γ_r)`  
* **IRRELEVANT (`OMIT`, y^\~ \= 1):** `y^⊥ = 0 ∧ margin_p(z) ≤ −γ_p ∧ (∀r ∈ Θ^⊥(p): margin_r(z) ≤ −γ_r)`  
* **UNRESOLVED (`UNDECIDED`):** otherwise (when `y^⊥ = 0` and `z` lies in the epistemic boundary band `|margin_p(z)| < γ_p` or `|margin_r(z)| < γ_r` for some `r ∈ Θ^⊥(p)`).

At Tier 2, structural ontology specifications `R(p, q) ∈ {REQ, FORB, IRR}` are enforced by hinge losses:

1. **Required Entailment (`REQ`, p ⇒ q ⟺ B\_p ⊆ B\_q and B\_q ⊊ B\_U):**  
   Containment loss with margin `ε_⇒ ≥ 0`:  
   `ℒ^ε_⊆(p, q) = ∑_{j=1}^m ( [lo_{q,j} + ε_⇒ − lo_{p,j}]_+ + [hi_{p,j} − hi_{q,j} + ε_⇒]_+ )`  
   plus the non-universality barrier with relative clearance `ν_max ∈ (0, 1)`:  
   `ℒ_{non-univ}(q) = [ min_{1 ≤ j ≤ m} ((hi_{q,j} − lo_{q,j}) / (hi_{U,j} − lo_{U,j})) − (1 − ν_max) ]_+`.  
2. **Required Incompatibility (`FORB`, p ⊥ q ⟺ B\_p ∩ B\_q \= ∅):**  
   Using coordinatewise overlap depth `ovl_j(p, q) = min(hi_{p,j}, hi_{q,j}) − max(lo_{p,j}, lo_{q,j})` and separation clearance `ε_⊥ > 0`:  
   `ℒ^ε_⊥(p, q) = [ ε_⊥ + min_{1 ≤ j ≤ m} ovl_j(p, q) ]_+`.  
3. **Structural Irrelevance (`IRR`):** Zero penalty.

**Theorem 6.1 (Soundness, Robustness, and Epistemic Clearance Consistency of Geometric Box Semantics).** For closed boxes B\_p, B\_q ⊆ B\_U ⊂ ℝ^m:

1. *Containment and Perturbation Robustness:* For `ε_⇒ ≥ 0`, `ℒ^ε_⊆(p, q) = 0` holds iff `lo_{p,j} ≥ lo_{q,j} + ε_⇒` and `hi_{p,j} ≤ hi_{q,j} − ε_⇒` for all `j = 1, ..., m`. For `ε_⇒ = 0`, `ℒ^0_⊆(p, q) = 0 ⟺ B_p ⊆ B_q`; for `ε_⇒ > 0`, `z ∈ B_p` and `‖ζ‖_∞ ≤ ε_⇒` imply `z + ζ ∈ B_q`.  
2. *Non-Universality (`y'_1`):* For `ν_max ∈ (0, 1)`, `ℒ_{non-univ}(q) = 0` holds iff along at least one axis `j` the width of `B_q` satisfies `(hi_{q,j} − lo_{q,j}) ≤ (1 − ν_max)(hi_{U,j} − lo_{U,j})`, guaranteeing `B_U \ B_q ≠ ∅` (Brusentsov's condition `y'_1`).  
3. *Disjointness (`(xy')_0`):* For `ε_⊥ > 0`, `ℒ^ε_⊥(p, q) = 0` holds iff `min_{1 ≤ j ≤ m} ovl_j(p, q) ≤ −ε_⊥`, certifying a gap of at least `ε_⊥` along some axis and hence `B_p ∩ B_q = ∅`. (Strict disjointness requires `ε_⊥ > 0`; `ε_⊥ = 0` permits boundary contact.)  
4. *Epistemic Clearance Consistency:* If `ℒ^ε_⊆(p, q) = 0` with `ε_⇒ ≥ max(0, γ_q − γ_p)`, then any point `z` with `margin_p(z) ≥ γ_p` satisfies `margin_q(z) ≥ γ_q`. Furthermore, if `Θ^⊥(p) ≠ ∅` and `ℒ^ε_⊥(p, r) = 0` for all `r ∈ Θ^⊥(p)` with `ε_⊥ ≥ max_{r ∈ Θ^⊥(p)} γ_r`, then every `z ∈ B_p` automatically satisfies `margin_r(z) ≤ −γ_r` for all `r ∈ Θ^⊥(p)`, ensuring the `γ_p`\-core of `B_p` is strictly disjoint from the epistemic boundary bands of all contrary predicates.

**Proof.** (1) Since `[x]_+ = max(0, x) ≥ 0`, the sum in `ℒ^ε_⊆(p, q)` vanishes iff every summand is `≤ 0`: `lo_{q,j} + ε_⇒ − lo_{p,j} ≤ 0` and `hi_{p,j} − hi_{q,j} + ε_⇒ ≤ 0` (`∀j`). For `z ∈ B_p` and `|ζ_j| ≤ ε_⇒`, `lo_{q,j} ≤ lo_{p,j} − ε_⇒ ≤ z_j + ζ_j ≤ hi_{p,j} + ε_⇒ ≤ hi_{q,j}`, so `z + ζ ∈ B_q`. (2) `[x]_+ = 0 ⟺ x ≤ 0` gives an axis `j*` where `B_q`'s projection is strictly narrower than `B_U`'s projection, so `B_U \ B_q ≠ ∅`. (3) Closed boxes intersect iff ovl\_j(p, q) ≥ 0 on every axis; for `ε_⊥ > 0`, zero loss gives `min_j ovl_j(p, q) ≤ −ε_⊥ < 0`. (4) From (1), `margin_q(z) ≥ margin_p(z) + ε_⇒ ≥ γ_p + max(0, γ_q − γ_p) ≥ γ_q`. From (3), on the separating axis `j*`, any `z ∈ B_p` lies at least `ε_⊥ ≥ γ_r` outside `[lo_{r,j*}, hi_{r,j*}]`, so `margin_r(z) ≤ −ε_⊥ ≤ −γ_r`. ∎

## **6.3. Hierarchical Knowledge Graphs and Compositional Scale Transitions**

Let a hierarchical knowledge graph be given by `𝒢_KG = (V_KG, E_KG, Sc, S)`, where `Sc = {0, 1, ..., M}` indexes resolution scales (from finest `0` to coarsest `M`) and `S: ℰ_ℓ → {+, −, 0}` assigns ternary statuses to graph elements `ℰ_ℓ` at scale `ℓ`.

At each scale `ℓ`, `ℰ_ℓ` is partitioned into essential and ignorable (coarse-grained out) subsets: `ℰ_ℓ = ℰ^{ess}_{ℓ→ℓ+1} ⊔ ℰ^{ign}_{ℓ→ℓ+1}`, where global safety invariants `I_ℓ` always stay essential (`I_ℓ ⊆ ℰ^{ess}_{ℓ→ℓ+1}` and `I_{ℓ+1} = π_{ℓ→ℓ+1}(I_ℓ)`). A surjective projection `π_{ℓ→ℓ+1}: ℰ_ℓ → ℰ_{ℓ+1}` maps each macro-element `u_{ℓ+1} ∈ ℰ_{ℓ+1}` to a non-empty preimage `π⁻¹_{ℓ→ℓ+1}(u_{ℓ+1}) ⊆ ℰ_ℓ`.

**Definition 6.1 (Status Transformation Law under Coarse-Graining π\_{ℓ→ℓ+1}).** The status of a macro-element `u_{ℓ+1} ∈ ℰ_{ℓ+1}` is uniquely determined by its essential preimage `Π_ess(u_{ℓ+1}) = π⁻¹_{ℓ→ℓ+1}(u_{ℓ+1}) ∩ ℰ^{ess}_{ℓ→ℓ+1}`:

* **`− (NULL)`:** if `∃ 𝔢_ℓ ∈ Π_ess(u_{ℓ+1}) : S(𝔢_ℓ, ℓ) = −`  
* **`+ (FOLLOW)`:** if branch `−` does not hold and `∃ 𝔢_ℓ ∈ Π_ess(u_{ℓ+1}) : S(𝔢_ℓ, ℓ) = +`  
* **`0 (OMIT)`:** otherwise (i.e., when `∀ 𝔢_ℓ ∈ Π_ess(u_{ℓ+1}) : S(𝔢_ℓ, ℓ) = 0`).

*(Polarity Note: In single-step conjunctive clause aggregation (§4.2), all active clauses must succeed for the step to achieve `FOLLOW`, so `OMIT (0) ≻ FOLLOW (+1)`. In spatial coarse-graining of a committed graph (§6.3), a macro-element represents a certified state refinement if at least one of its essential micro-elements is certified (`+`) while none are contradicted (`−`), inducing the coarse-graining order `− ≻_cg + ≻_cg 0`.)*

**Proposition 6.1 (Totality and Compositionality of Coarse-Graining).**

1. Definition 6.1 is total and mutually exclusive, and any violated global invariant `i ∈ I_ℓ` bearing status `−` preserves status `−` across all coarser scales `ℓ' > ℓ`.  
2. If under a two-step coarse-graining `ℓ → ℓ + 1 → ℓ + 2` the essential subsets satisfy the compatibility condition `ℰ^{ess}_{ℓ→ℓ+2} = π⁻¹_{ℓ→ℓ+1}(ℰ^{ess}_{ℓ+1→ℓ+2}) ∩ ℰ^{ess}_{ℓ→ℓ+1}`, then status assignment is compositional (`π_{ℓ→ℓ+2} = π_{ℓ+1→ℓ+2} ∘ π_{ℓ→ℓ+1}`).

**Proof.** (1) The three branches partition the power set `𝒫({−, +, 0})` on `Π_ess(u_{ℓ+1})`, and I\_ℓ ⊆ ℰ^{ess}\_{ℓ→ℓ+1} propagates − inductively. (2) Under the strict total order − ≻\_cg \+ ≻\_cg 0 with identity 0, Definition 6.1 is the semilattice join max\_{≻\_cg}(S(Π\_ess(u\_{ℓ+1})) ∪ {0}). Associativity, commutativity, and idempotence of `max_{≻_cg}` together with the stated preimage identity make the two-step join identical to the direct join. ∎

# **7\. Constructive Guarantees and Verification Quality Metrics**

## **7.1. Constructive Architectural Theorem**

**Theorem 7.1 (Totality, Well-Definedness, State Groundedness, Rollback Consistency, and Auditability).**  
Assume:

* The audit log is append-only, immutable, and complete for all committed transitions;  
* The structural extractor `ψ` is a pure deterministic function of its observation argument;  
* All data required for logical-state reconstruction are retained in the log (side-effect descriptors, invariant versions, expectation bindings, scopes, certificate payloads, and verifier/contract version hashes);  
* Certificates `𝒞_t` are uniquely bound to `seq_t` and the contract hash;  
* No unlogged external mutations of controlled state occur between action emission and subsequent observation receipt;  
* Any claimed rollback of external physical/tool effects is supported either by a transactional environment or by a separately verified compensating-action protocol (otherwise, the theorem guarantees logical-state restoration only).

Under these assumptions, any state-control system governed by the cascade of §4.3 and the commit protocol of §5.2–§5.4 satisfies:

1. **Judge Totality and Uniqueness:** Every transition `τ_t`, expectation set `E`, and invariant set `I` terminates with a unique verdict in V\_4 (and unique `OMIT` subtype in §5.2). Any transition with `E_act ≠ ∅` lacking valid certificates maps to `UNDECIDED` or `NULL`, never to `FOLLOW`. Unauthenticated apparent invariant violations (`Viol = 1 ∧ AuthSafety = 0`) map to `UNDECIDED` and are never ignored.  
2. **State Groundedness:** If the state manager commits a goal-essential state transition into `𝒮_t^+` only upon receiving `FOLLOW` (+1) (while recording `OMIT` nodes with status `0` outside `𝒮_t^+`), then at any step `T ≥ 0`, every element in `𝒮_T^+` is derived from initial state axioms `H_0` via a finite chain of authoritatively observed transitions (`OBSERVED_TRANSITION` or `REPLAY_VERIFIED`) certified with `FOLLOW` (+1).  
3. **Logical Rollback Consistency:** Under the pending-token lock (`ϖ_t`, §5.4) and non-destructive retention of `OMIT_INCIDENTAL` nodes (§5.2), replaying the versioned logical-state log to checkpoint `t_chk` restores the recorded descriptor `H_{t_chk}` identically.  
4. **Deterministic Auditability:** Given `H_0` and the complete append-only log for `t = 0, ..., T − 1`, the logical trajectory `(H_1, ..., H_T)` and verdicts `(V_0, ..., V_{T-1})` are uniquely reconstructible without querying any stochastic generator.

**Proof.** (1) Follows from Proposition 4.2, Lemma 4.3, and the dichotomous subtype conditions in Steps 3 and 5\. (2) Follows by induction on T: each new element in 𝒮\_{t+1}^+ requires passing Step 2 (authoritative scope) and Step 4 (valid certificates 𝒞^+ or `𝒞^∅` anchored in `τ_t` and `𝒮_t^+`). (3) By the `ϖ_t` lock, at most one transition is in flight at any step, uncertified transitions (`NULL / UNDECIDED`) never mutate accepted state, and `OMIT_INCIDENTAL` nodes are appended with status `0` without overwriting prior nodes. (4) Every component in the verification loop (`ψ`, validator, cascade, controller policy) is a pure function of logged inputs. ∎

## **7.2. Canonical Suite of Verifier Evaluation Metrics (4×4 Confusion View)**

Let an evaluation benchmark partition candidate moves `m` into four disjoint ground-truth classes:

* **`G^+`**: Truly productive state refinements;  
* **`G^~`**: Truly incidental/indifferent moves;  
* **`G^⊥`**: Truly incompatible/false moves;  
* **`G^U`**: Epistemically undecidable moves (genuinely insufficient evidence).

| Ground Truth \\ Judge Output J(m) | FOLLOW (+1) | OMIT (0) | NULL (−1) | UNDECIDED (U) |
| :---- | :---- | :---- | :---- | :---- |
| **`m ∈ G^+` (Productive)** | True Follow | False Omit (`FOmitR`) | Productive Loss (`FNullR^+`) | False Abstention (FAR) |
| **`m ∈ G^~` (Indifferent)** | **False Follow (FFR)** | True Omit | False Null (`FNullR`) | False Abstention (FAR) |
| **`m ∈ G^⊥` (Incompatible)** | **False Follow (FFR)** | **Safety Miss (`FOmitR^⊥`)** | True Null | False Abstention (FAR) |
| **`m ∈ G^U` (Undecidable)** | **Over-Commit (OCR\_U)** | **Over-Commit (`OCR_U`)** | **Over-Commit (`OCR_U`)** | True Abstention |

**Group A. Verdict-Conditioned Error Risks (Precision-type, conditioned on Judge output):**

1. **False Follow Rate (`FFR` — Primary Safety Metric):**  
   `FFR = ℙ(m ∉ G^+ | J(m) = FOLLOW)`  
2. **False Nullification Risk (`FNullR` and productive-loss sub-metric `FNullR^+`):**  
   `FNullR = ℙ(m ∉ G^⊥ | J(m) = NULL)`,   `FNullR^+ = ℙ(m ∈ G^+ | J(m) = NULL)`  
3. **False Omit Risk (`FOmitR` and safety-critical sub-metric `FOmitR^⊥`):**  
   `FOmitR = ℙ(m ∉ G^~ | J(m) = OMIT)`,   `FOmitR^⊥ = ℙ(m ∈ G^⊥ | J(m) = OMIT)`

**Group B. Ground-Truth-Conditioned Sensitivity and Selective Coverage (Rate-type):**  
4\. **False Abstention Rate on Decidable Moves (`FAR`) and Over-Commitment Rate on Undecidable Moves (`OCR_U`):**  
`FAR = ℙ(J(m) = UNDECIDED | m ∈ G^+ ∪ G^~ ∪ G^⊥)`,   `OCR_U = ℙ(J(m) ≠ UNDECIDED | m ∈ G^U)`  
5\. **Selective Coverage (`Cov`) (Geifman & El-Yaniv, 2017):**  
`Cov = ℙ(J(m) ≠ UNDECIDED)`, maximized subject to a hard upper bound on the false-commit risk `FFR ≤ α` (meaningful only when `FFR` is estimable from a non-empty set of `FOLLOW` predictions).

## **7.3. Scope, Limits of the Claims, and Implementation Conformance Requirements**

* **Proved in this specification:** Theorem 3.1; Theorem 4.1; Proposition 4.2; Lemma 4.3; Theorem 6.1; Proposition 6.1; and Theorem 7.1 relative to its stated operational assumptions.  
* **Not established here:**  
  1. *Completeness, decidability, and model-theoretic semantics* for the MDNF fragment, and a consistency proof of the full two-tier calculus.  
  2. *Contraposition is deliberately not inherited:* Because `(ac ⇒ y)` is not contraposable (§1.4, item 2), classical Aristotelian syllogistic figures relying on conversion or contraposition are not inherited by Tier 2\.  
  3. *Empirical calibration* of thresholds (`θ_prog, θ_succ, θ_fail, ε_base, θ_conf, ε_rev, ε_orth, N_min, η_tol, T_wait, N_probes, k_max`) and achieving `FFR ≤ α`, which are empirical engineering targets (§7.2), not theorems.  
  4. *Graph-level uncertainty:* The ternary graph status `S` of §6.3 carries no `UNDECIDED`; epistemic states are resolved at Tier 1 before commitment.

# **References**

* Aristotle. *Prior Analytics* (Analytica Priora).  
* Belnap, N. D. (1977). A Useful Four-Valued Logic. In *Modern Uses of Multiple-Valued Logic*, Dordrecht: D. Reidel, 5–37.  
* Brusentsov, N. P. (1994). *Foundations of Informatics* \[Nachala informatiki\]. Moscow: New Millennium Foundation.  
* Brusentsov, N. P. (2005). Reanimation of Aristotelian Syllogistics. In *Restoration of Logic*, Moscow: New Millennium Foundation.  
* Brusentsov, N. P., & Vladimirova, Yu. S. (2005). Ternary Computerization of Logic. In *Mathematical Methods of Pattern Recognition (MMRO-12)*, Moscow: MAX Press.  
* Brusentsov, N. P. (2011). *Ordering of Mathematical Logic* \[Uporyadochenie matematicheskoy logiki\]. Moscow: New Millennium Foundation.  
* Brusentsov, N. P. (2012). *Improvement of the Logic of Inferences* \[Usovershenstvovanie logiki umozaklyucheniy\]. Moscow: New Millennium Foundation.  
* Carroll, L. (1896). *Symbolic Logic*. London: Macmillan and Co. (Russian ed.: Moscow: Mir, 1973).  
* Farquhar, S., Kossen, J., Kuhn, L., & Gal, Y. (2024). Detecting Hallucinations in Large Language Models Using Semantic Entropy. *Nature*, 630, 625–630.  
* Geifman, Y., & El-Yaniv, R. (2017). Selective Classification for Deep Neural Networks. In *Advances in Neural Information Processing Systems (NeurIPS)*.  
* Good, I. J. (1967). The White Shoe is a Red Herring. *The British Journal for the Philosophy of Science*, 17(4), 322\.  
* Hempel, C. G. (1945). Studies in the Logic of Confirmation (I & II). *Mind*, 54(213–214), 1–26, 97–121.  
* Hilbert, D., & Ackermann, W. (1928). *Principles of Mathematical Logic* \[Grundzüge der theoretischen Logik\]. Berlin: Springer.  
* Hoel, E. P., Albantakis, L., & Tononi, G. (2013). Quantifying Causal Emergence Shows That Macro Can Beat Micro. *PNAS*, 110(49), 19790–19795.  
* Kalai, A. T., Nachum, O., Vempala, S. S., & Zhang, E. (2025). Why Language Models Hallucinate. *arXiv:2509.04664*.  
* Kirichenko, P., Ibrahim, M., Chaudhuri, K., & Bell, S. J. (2025). AbstentionBench: Reasoning LLMs Fail on Unanswerable Questions. In *NeurIPS* (*arXiv:2506.09038*).  
* Kleene, S. C. (1952). *Introduction to Metamathematics*. Amsterdam: North-Holland.  
* Kolchinsky, A., & Wolpert, D. H. (2018). Semantic Information, Autonomous Agency and Non-Equilibrium Statistical Physics. *Interface Focus*, 8(6).  
* Liu, X., et al. (2026). AgentAbstain: Do LLM Agents Know When Not to Act? *arXiv:2607.10059*.  
* Łukasiewicz, J. (1920). O logice trójwartościowej \[On Three-Valued Logic\]. *Ruch Filozoficzny*, 5, 170–171.  
* Nicod, J. (1930). *Foundations of Geometry and Induction*. London: Kegan Paul, Trench, Trubner & Co.  
* Poretsky, P. S. (1884). *On the Methods of Solving Logical Equalities and on the Inverse Method of Mathematical Logic*. Kazan.  
* Tishby, N., Pereira, F. C., & Bialek, W. (1999). The Information Bottleneck Method. In *Proceedings of the 37th Annual Allerton Conference*, 368–377.  
* Vladimirova, Yu. S. (2010). Computerization of Contentful Reasoning Based on Syllogistic Inference. *Software Systems and Tools*, No. 12, Moscow: VMK MSU.

*End of specification. Version 1.0 (ML Engineering Edition).*