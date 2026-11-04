# **The Boundary Projection Theorem, the Kernel of Insignificance, and the Four-Valued Verdict (Geometric Core of V\_4)**

**Author:** Vladimir Yakunin  
**Version:** 1.0 (ML Engineering Edition — full structural and mathematical fidelity)  
**Date:** 2026-10-22  
**Status:** Derived geometric semantics of the verdict layer at the point/ball level. A domain instantiation of the canonical calculus; not a replacement of the normative cascade (see §0).  
Normative parent: Modified Brusentsov Entailment Logic (Reasoning/Modified\_Brusentsov\_Entailment\_Logic.md), especially §§3–5. Where this document and the canonical specification differ, the canonical specification governs.  
**Siblings:** Spectral and Matrix Realization of V\_4 in Latent Spaces (feature-space realization, estimators, and aggregation theorems — this document reuses its Theorems 5.1–5.2 verbatim); Latent Agency Framework v2.1 §8 and Causal Phase Program v4.0 §2.4 (boundary kernel-inclusion conditions, imported here as the cross-layer preservation form).  
**Purpose:** A single geometric theorem — the projection of the observation confidence ball through a boundary (contract) with a kernel — that carries the point-level verdict semantics, replacing scattered case tables at this layer only.

# **Abstract & ML Engineering Intuition**

**Why this document exists (for ML Engineers):**  
When an agent executes an action or state transition, how do we verify whether that step succeeded, failed, was irrelevant, or was too noisy to judge? In Modified Brusentsov Entailment Logic (MBEL), this requires a multi-step logical case table. Here, we show that at the single-step level, the entire four-valued verdict space V\_4 \= {FOLLOW, OMIT, NULL, UNDECIDED} reduces to a single geometric operation: projecting a confidence ellipsoid (representing observation/tracking uncertainty) through a task projection operator.

Specifically, the point-verdict architecture reduces to three mathematical constructions:

* **A single object (the projection triad):** Micro-dynamics in state-transition space 𝒳 are mapped through a boundary operator (verification contract or coarse-graining scale) π\_K into an essential feature space 𝒴\_K. This operator has an insignificance kernel ker(π\_K) (transitions that do not affect the contract) and a target cone C\_K^+ (valid productive shifts). Because sensors and encoders have finite resolution, an observed transition is represented not as a point, but as a compact confidence ball/ellipsoid 𝔹\_t ⊆ 𝒳.  
* **The four-verdict theorem (V\_4):** A total, deterministic, single-valued classification of where the projected ball π\_K(𝔹\_t) lands relative to the kernel origin {0} and the target cone C\_K^+. Brusentsov's three-valued ontology {+, 0, −} partitions the points of the space, while the fourth status UNDECIDED (U) arises purely from topology when passing from points to finite-radius sets 𝔹\_t: whenever the uncertainty ball straddles the boundary between regions, the verdict is UNDECIDED.  
* **The composition-and-scale law:** Multiple verification contracts are aggregated on a linear dominance semilattice via a padding-invariant shifted LogSumExp operator (sLSE\_T). When transmitting information across a subsystem boundary, preserving structure requires the kernel-inclusion condition ker(π\_int) ⊆ ker(π\_ext) at an unsaturated channel η\_sat \< 1 (where the physical reading of the saturation threshold carries status UNDECIDED, see §3.2).

This document is a derived geometric semantics of the canonical calculus: typed certificates, ensemble law quantifiers, and the two-phase commit protocol remain governed by MBEL; feature-space estimators and confidence-ball construction remain governed by the Spectral realization. Row-by-row correspondence is fixed in §6; coverage boundaries are declared in §0.

# **0\. Scope and Authority**

## **0.1. What this document covers**

* **The point/ball verdict layer:** A single verification contract K, a single observation window τ\_w, one confidence set 𝔹\_t, and the resulting verdict (Theorem 2.1).  
* **Refinement dynamics:** How narrowing the confidence ball under certified evidence stabilizes decided verdicts (Proposition 2.2, Corollary 2.3).  
* **Multi-contract aggregation:** Combining point verdicts across contracts, imported verbatim from the Spectral realization (§3.1).  
* **Boundary preservation condition:** The kernel-inclusion condition across its three corpus instantiations (§3.2), with explicit verification statuses.

## **0.2. What this document does not cover (authority remains with the normative parent)**

* **Typed verification certificates and evidence scopes** beyond their ball-radius reading (MBEL §5.3; Spectral §3.4–§4.1).  
* **Ensemble law quantifiers** and Hempel–Nicod raven-paradox immunity across historical transition logs (MBEL §3.4, Theorem 3.1).  
* **Two-phase commit, pending tokens, and rollback protocols** (MBEL §5.4).  
* **The variational minimal-surface layer (VIM / Latent Information Structuring):** Geometrically adjacent but logically independent of the verdict core; it is not part of this reduction.  
* **Feature-space diagnostics** (α\_k, β\_k, ν\_k, Mahalanobis SNR): These construct 𝔹\_t and belong to the Spectral realization.

## **0.3. Priority rule**

Every mapping in §6 is a geometric representation of the canonical constructs, not a redefinition. In any conflict of verdict semantics, MBEL §§1–5 govern.

# **1\. The Single Object: Projection Triad, Kernel, and Confidence Ball**

**Engineering Intuition:**  
Think of 𝒳 as the space of all possible state deltas Δx during a time step τ\_w. A contract K cares only about a specific projection π\_K(Δx) in a lower-dimensional task feature space 𝒴\_K.

* If π\_K(Δx) \= 0, the transition happened in a direction the contract ignores (the nullspace/kernel ker(π\_K) → OMIT).  
* If π\_K(Δx) lands inside the desired target cone C\_K^+, the step made valid progress (FOLLOW).  
* If π\_K(Δx) lands anywhere else outside the kernel and outside the target cone, it violated the contract (NULL).

Let 𝒳 be the space of elementary transitions (or tangent state shifts) of the system on a time window τ\_w and resolution scale ℓ.

## **Definition 1.1 (Boundary Contract and the Three-Valued Ontological Partition)**

A verification contract (a law, or a scale description) K is defined by a projection operator

π\_K : 𝒳 ⟶ 𝒴\_K

into the factor space of essential features 𝒴\_K (with a distinguished zero element 0 ∈ 𝒴\_K). This projection partitions 𝒳 into three disjoint ontological regions in the sense of Brusentsov's three-valued logic:

𝒳 \= ℛ\_K^0 ⊔ ℛ\_K^+ ⊔ ℛ\_K^⊥

* **Insignificance kernel (OMIT region, status 0):**  
  ℛ\_K^0 := ker(π\_K) \= { x ∈ 𝒳 \| π\_K(x) \= 0 }.  
  ker(π\_K) contains all transitions that are invariant or inapplicable with respect to the law K: non-activated operators (a\_k \= 0), contexts blocked by an external obstacle (c\_k \= 0), changes in subsystems orthogonal to the law, and sub-threshold neutral fluctuations Ω\_{sub,K} explicitly declared in the contract.  
* **Target cone of following (FOLLOW region, status \+1):**  
  ℛ\_K^+ := { x ∈ 𝒳 \\ ker(π\_K) \| π\_K(x) ∈ C\_K^+ },  
  where ∅ ≠ C\_K^+ ⊊ 𝒴\_K \\ {0} is a non-empty, non-universal target cone (the admissible set of productive shifts) satisfying the Carroll–Brusentsov non-triviality axioms (x\_1 and y'\_1: the target cone is neither empty nor covers the whole space).  
* **Incompatibility / nullification region (NULL region, status −1):**  
  ℛ\_K^⊥ := 𝒳 \\ (ℛ\_K^0 ∪ ℛ\_K^+) \= { x ∈ 𝒳 \\ ker(π\_K) \| π\_K(x) ∉ C\_K^+ }.  
  This region collects all out-of-kernel transitions that violate the contract: sign inversion along active axes, leakage into invariant subspaces, destruction of the target object, exit beyond the contract, and unexplained stagnation on a confirmed law.

**Special case (pure conservation invariant e ∈ E\_inv):** For a safety or preservation condition that only requires keeping the state inside an admissible tube with no active shift, the kernel is empty (ℛ\_K^0 \= ∅), and the space splits into the admissible conservation tube ℛ\_K^+ and the invariant-breakdown region ℛ\_K^⊥.

## **Definition 1.2 (Observation Confidence Ball 𝔹\_t)**

In a real control loop or physical measurement, the transition on the window τ\_w is observed with finite resolution and is represented not by a single point, but by a non-empty compact confidence set (ellipsoid/ball) 𝔹\_t ⊆ 𝒳:

* **Exact deterministic observation:** 𝔹\_t \= {x\_t} collapses to a single point.  
* **Finite sensor or tracking noise:** Given epistemic covariance Σ\_epi and SNR threshold γ\_snr \> 0, the set is the Mahalanobis ellipsoid  
  𝔹\_t \= { x : ‖x − x̂\_t‖\_{Σ\_epi^{-1}} ≤ γ\_snr }  
  (whose certified construction is specified in Spectral §3.4).  
* **Unverified prediction or tracking loss:** In the absence of an authoritative observation (scopes PREDICTIVE\_ONLY or NOT\_AVAILABLE), on tracking loss (Rel \= 0), or without a valid certificate, the uncertainty ball inflates to the entire space: 𝔹\_t \= 𝒳.

# **2\. The Four-Verdict Theorem (V\_4)**

**Engineering Intuition:**  
Why do we need four verdicts in V\_4 if the world only has three regions (ℛ\_K^0, ℛ\_K^+, ℛ\_K^⊥)? Because our measurement is a ball 𝔹\_t, not a point\!

* Ball entirely inside ℛ\_K^0 → OMIT  
* Ball entirely inside ℛ\_K^+ → FOLLOW  
* Ball entirely inside ℛ\_K^⊥ → NULL  
* Ball straddles a boundary between two or more regions → UNDECIDED.

## **Theorem 2.1 (Topological Generation of V\_4 from the Three-Valued Ontology) \[Status: FOLLOW\]**

Let 𝒳 \= ℛ\_K^0 ⊔ ℛ\_K^+ ⊔ ℛ\_K^⊥ be the three-valued ontological partition of a contract K, and let 𝔹\_t ⊆ 𝒳 be a non-empty observation confidence set. Then the following four conditions are pairwise incompatible, exhaust all possible configurations of 𝔹\_t, and define the verdict in V\_4 \= {FOLLOW, OMIT, NULL, UNDECIDED} by a total, deterministic, single-valued map:

* **OMIT (0):** if 𝔹\_t ⊆ ℛ\_K^0  ⟺  π\_K(𝔹\_t) \= {0}  
* **FOLLOW (+1):** if 𝔹\_t ⊆ ℛ\_K^+  ⟺  π\_K(𝔹\_t) ⊆ C\_K^+  
* **NULL (−1):** if 𝔹\_t ⊆ ℛ\_K^⊥  ⟺  π\_K(𝔹\_t) ∩ (C\_K^+ ∪ {0}) \= ∅  
* **UNDECIDED (U):** otherwise (∃ u ≠ v ∈ {0, \+, ⊥} : 𝔹\_t ∩ ℛ\_K^u ≠ ∅ and 𝔹\_t ∩ ℛ\_K^v ≠ ∅).

**Proof.** Since ℛ\_K^0, ℛ\_K^+, ℛ\_K^⊥ are pairwise disjoint and cover 𝒳, any non-empty subset 𝔹\_t ⊆ 𝒳 is either entirely contained in exactly one of the three regions (the first three branches, which are pairwise incompatible because 𝔹\_t ≠ ∅), or has a non-empty intersection with at least two distinct regions (the fourth branch). Hence the map is total, deterministic, and single-valued. ∎

**Remark.** The classification is a surjection onto V\_4 (many ball configurations map to one verdict), not a bijection; uniqueness holds per configuration, not per verdict.

```py
# Reference Python Intuition for Theorem 2.1
def evaluate_ball_verdict(ball_B_t, region_omit, region_follow, region_null):
    in_omit   = ball_B_t.is_subset_of(region_omit)     # pi_K(B_t) == {0}
    in_follow = ball_B_t.is_subset_of(region_follow)   # pi_K(B_t) subset of C_K^+
    in_null   = ball_B_t.is_subset_of(region_null)     # disjoint from C_K^+ and {0}

    if in_omit:
        return "OMIT"       # 0
    elif in_follow:
        return "FOLLOW"     # +1
    elif in_null:
        return "NULL"       # -1
    else:
        return "UNDECIDED"  # U: ball straddles a boundary between regions
```

## **Corollary 2.1 (The Nature of UNDECIDED)**

UNDECIDED (U) is not a fourth ontological truth value. It is the geometric indicator that the confidence ball intersects the boundary between ontological regions — equivalently, that the distance from the ball center to the region boundary does not exceed the ball radius. Resolving UNDECIDED is possible by exactly two routes:

* **Shrinking the ball 𝔹\_t:** Additional measurement, active probing, improved tracking precision, or a certified narrowing event (Proposition 2.2).  
* **Changing the coarse-graining scale ℓ → ℓ':** Expanding the kernel ker(π\_K) so that it absorbs the boundary fluctuations. This is admissible only under the scale-compatibility condition ker(π\_K) ⊆ ker(π\_{K'}) (Spectral Proposition 2.1) and the re-verification protocol of MBEL §5.4.

## **Corollary 2.2 (Geometric Nature of the Three OMIT Subtypes: Stratified Kernel)**

When π\_K(𝔹\_t) \= {0} (OMIT), the operational controller subtype is determined by where 𝔹\_t lies within the clause-stratified kernel — the stratification inherited from the contract's MDNF coordinates (active clause flag a\_k, precondition context flag c\_k, and identity of the zero shift), which is part of the contract data. Position inside an unstratified kernel does not by itself separate the subtypes:

* **OMIT\_REDUNDANT:** 𝔹\_t \= {0\_𝒳} — the zero shift in the entire state space (the identity transition H\_{t+1} \= H\_t).  
* **OMIT\_BLOCKED:** 𝔹\_t lies in the stratum of ker(π\_K) cut out by a\_k \= 1, c\_k \= 0 — the active operator was invoked but met the boundary of the admissible region (a soft stop against an obstacle without breaching invariants).  
* **OMIT\_INCIDENTAL:** 𝔹\_t ⊆ ker(π\_K) \\ {0\_𝒳} within the stratum a\_k \= 0 or the declared sub-threshold zone Ω\_{sub,K} — real motion occurred in the system, but orthogonal to the given law K (internal circulation within the kernel, or the work of another operator).

This reading reproduces the disjoint taxonomy and controller priority of MBEL §5.2 (OMIT\_BLOCKED first, then unchanged-descriptor OMIT\_REDUNDANT, then OMIT\_INCIDENTAL); the priority is a property of the stratification labels, not of metric position.

## **Proposition 2.2 (Refinement Monotonicity; Stability of Decided Verdicts) \[Status: FOLLOW\]**

Let ∅ ≠ 𝔹' ⊆ 𝔹 be two confidence sets of the same contract K (representing a refinement or certified narrowing of uncertainty). Then:

* If Verdict\_K(𝔹) ∈ {FOLLOW, OMIT, NULL}, then Verdict\_K(𝔹') \= Verdict\_K(𝔹): a decided verdict is preserved under any narrowing.  
* If Verdict\_K(𝔹) \= UNDECIDED, then Verdict\_K(𝔹') may become any of the four verdicts. Conversely, a decided verdict can revert to UNDECIDED only by ball inflation or by changing the regions (contract/scale revision) — never by narrowing.

**Proof.** (1) 𝔹 ⊆ ℛ implies 𝔹' ⊆ ℛ for each region ℛ ∈ {ℛ\_K^0, ℛ\_K^+, ℛ\_K^⊥}. (2) A straddling ball narrows either into a single region (reaching a decision) or remains straddling. ∎

## **Corollary 2.3 (Geometric Form of Certified Resolution and Non-Promotion)**

In MBEL, evidence arrives as typed certificates (§5.3) and resolution is governed by the two-phase commit protocol (§5.4). Their geometric reading is:

* **Certified narrowing:** An authoritative certificate for a scope-OBSERVED transition replaces 𝔹\_t with the intersection 𝔹\_t ∩ Z\_𝒞, where Z\_𝒞 is the certificate's admissible set. A NULL certificate with 𝔹\_t ∩ Z\_𝒞 ⊆ ℛ\_K^⊥ decides the verdict even when the prior ball straddled — this captures the fundamental asymmetry of authoritative refutation: NULL is decidable from partial refuting evidence, whereas FOLLOW is not (it requires the entire ball to lie inside the target cone).  
* **Non-promotion / non-demotion (MBEL §5.4):** Once a verdict is decided on a certified narrowing, Proposition 2.2 guarantees its stability under all further narrowings; re-deciding requires new authoritative evidence or an explicit contract/scale revision with re-verification. In particular, an UNDECIDED verdict recorded when the probing budget is exhausted is never overwritten to NULL afterwards: budget exhaustion simply stops the narrowing, and a straddling ball remains straddling.

# **3\. Composition, Scale, and Inter-Agent Stitching**

## **3.1. Linear Dominance Semilattice and Cumulative Aggregation**

**Engineering Intuition:**  
When checking M requirements (clauses) in parallel, the worst status must win: a single failure (NULL) overrides everything; if nothing failed, any unresolved check (UNDECIDED) blocks commitment; if everything is resolved, an irrelevant step (OMIT) prevents claiming progress (FOLLOW). To make this max-severity operation differentiable for training without diluting a single NULL across M clauses, we map the 4-simplex into cumulative severity coordinates q \= \[p^{(-)}, p^{(-)}+p^{(U)}, p^{(-)}+p^{(U)}+p^{(0)}\] and apply a shifted LogSumExp (sLSE\_T) where satisfied clauses (q\_m \= 0\) contribute e^0 − 1 \= 0 (zero padding distortion).

Under simultaneous verification of an ensemble of contracts {K\_1, ..., K\_M}, the base verdicts are ordered by the strict linear dominance chain:

NULL (−1) ≻\_V UNDECIDED (U) ≻\_V OMIT (0) ≻\_V FOLLOW (+1),   with   u ⊗ v := max\_{≻\_V}(u, v).

On the four-dimensional simplex of soft weights p \= (p^{(+)}, p^{(0)}, p^{(U)}, p^{(-)})^⊤ ∈ Δ³, the affine bijection to cumulative severity coordinates

Φ\_cum(p) \= q := \[ p^{(-)},  p^{(-)} \+ p^{(U)},  p^{(-)} \+ p^{(U)} \+ p^{(0)} \]^⊤ ∈ ℚ \= { 0 ≤ q\_1 ≤ q\_2 ≤ q\_3 ≤ 1 }

turns the discrete conjunction ⊗ into the coordinatewise maximum (⋁\_m q\_m)*j \= max\_m q*{m,j}, and turns its smooth relaxation at temperature T \> 0 into the padding-invariant shifted operator:

sLSE\_T(q\_{1,j}, ..., q\_{M,j}) := min{ 1,  T · ln( 1 \+ ∑\_{m=1}^M (exp(q\_{m,j} / T) − 1\) ) }.

**Key properties of sLSE\_T** (proved in Spectral and Matrix Realization of V\_4, Theorems 5.1–5.2; imported here verbatim):

* **Inertia of FOLLOW:** Any satisfied contract (q\_m \= (0, 0, 0)^⊤) contributes exp(0) − 1 \= 0 and does not distort the sum for any number of clauses M.  
* **Absorption of NULL:** A single reliable NULL (q\_m \= (1, 1, 1)^⊤) yields the exact output e\_{(-)} at any temperature T \> 0\.  
* **Vacuous-truth guard (MBEL Axiom 4.1):** Multiplying by the activity guard p\_prog(E) (which equals e\_{(0)} when E\_act \= ∅ and e\_{(+)} when E\_act ≠ ∅) guarantees that a step with no active goals never receives FOLLOW.

## **3.2. Kernel Inclusion and the Interface Saturation Threshold**

**Engineering Intuition:**  
Suppose Agent A (external environment/sender) interacts with Agent B (internal model/receiver) across an interface ∂A. For Agent B to synchronize with Agent A without blind spots, B's boundary projection must not throw away into its nullspace (ker(π\_int), i.e., OMIT) signals that represent real state changes for A (outside ker(π\_ext)). Mathematically: ker(π\_int) ⊆ ker(π\_ext).

Let two subsystems (or two description scales) be coupled through an interface ∂A with internal projector π\_int and external projector π\_ext. Let the internal dynamics contract phase volume transversely to the attractor at rate κ(A) \= ∑\_{λ\_i \< 0} \|λ\_i\| while generating expansion rate h\_+(A) \= ∑\_{λ\_i \> 0} λ\_i (the Pesin expansion rate, which equals the Kolmogorov–Sinai entropy rate under SRB-type measures and is an upper bound in general by Ruelle's inequality; notation follows CPP v4.0 §4.2).  
\|---\|

### **1\. Kernel-inclusion condition (structural completeness of the boundary) \[Status: FOLLOW for per-layer definitions; UNDECIDED as a cross-layer unification thesis\]**

ker(π\_int) ⊆ ker(π\_ext).

The internal projection must not discard into OMIT (ker(π\_int)) those boundary distinctions that for the external environment lie in FOLLOW or NULL (𝒳 \\ ker(π\_ext)). Violating this inclusion produces irreducible model blindness regardless of observation duration. This same inclusion form appears across three layers of the repository with three distinct mathematical species of kernel:

| Layer | Kernel Species | Inclusion Statement | Normative Source |
| :---- | :---- | :---- | :---- |
| **Coarse-graining of descriptions** | Tangent distribution ker(dπ\_ℓ) | K\_z^{(ℓ)} ⊆ K\_z^{(ℓ')} for π\_{ℓ'} \= f ∘ π\_ℓ | Spectral Prop 2.1; CPP v4.0 §3.1-context |
| **Gaussian boundary coupling** | Precision matrix block ker(Π\_{ℐb}) | ker(Π\_{ℐb}) ⊆ ker(Π\_{ℰb}) ⟺ existence of linear synchronization map σ | CPP v4.0 Prop 2.2, Cor 2.3; LAF §8.3a |
| **Verdict contracts** | Logical insignificance ker(π\_K) | ker(π\_int) ⊆ ker(π\_ext) (this section) | MBEL §5.1 (equivalence kernels) |

These three are analogous in form, not identical in kind: their unification is a programmatic homology (the corpus-wide caveat "homology, not identity"), and no transport functor between the species is constructed. Status of the unification thesis: UNDECIDED (see §5, row 8).

### **2\. Channel non-saturation criterion (boundary throughput) \[Status: UNDECIDED — physical reading; CPP v4.0 Registry row 12 (Hypothesis H-L)\]**

η\_sat(A) := İ\_erase^{net}(ℐ\_A → ∂^+ A) / C\_max(∂^+ A) \= (κ(A) − h\_+(A)) / (ln 2 · C\_max(∂^+ A)).

* **What is FOLLOW here:** Regardless of any threshold reading, the recoverability bound of CPP v4.0 Proposition 2.1 limits whatever an external observer can reconstruct through ∂^+ A to the shared prior plus n · C(∂^+ A) bits — an exact data-processing inequality under its stated assumptions.  
* **What is UNDECIDED:** The physical reading of η\_sat (an erasure flux into a thermal reservoir at temperature T and a per-edge capacity c\_0) requires entities external to the discrete model — this is Hypothesis H-L of CPP v4.0 (Registry row 12). The claim that at η\_sat ≥ 1 the inclusion condition breaks and deep bulk modes are permanently screened (an information horizon) belongs to the continuum narrative that CPP v4.0 moved to OMIT (Registry row 17); at the discrete layer it remains an untested hypothesis, not an operative criterion.  
* **What is not proved at all (recorded honestly):** The synthesis claiming that "internal OMIT-states unfold across the boundary into a temporal chain of generalized coordinates s̃\_t \= (s\_t^{(0)}, ..., s\_t^{(n)}) and admit synchronization in finite time under η\_sat \< 1 plus kernel inclusion" composes CPP v4.0 Proposition 5.1 (rational-spectrum realization) with Propositions 2.1–2.2 (bounds and inclusion). The composition itself has no formal proof; its status is UNDECIDED, tested indirectly by Protocols V2/V7 of CPP v4.0.

# **4\. Explicit Non-Claims**

* **Calibration is still required:** The theorem fixes the formal geometry of verification and coarse-graining; it does not replace empirical calibration of the epistemic covariance Σ\_epi and target cone thresholds C\_K^+ in a concrete domain.  
* **Soft aggregation is for training only:** The smooth operator sLSE\_T is a surrogate for gradient optimization and route ranking; factual writes to memory occur strictly on crisp verdicts (Verdict\_K(𝔹\_t) at T → 0^+).  
* **No replacement of MBEL:** This document does not replace the MBEL decision cascade, certificate typing, or ensemble law quantifiers; §0.2 fixes the authority boundary and §6 fixes the correspondence.  
* **Homology, not identity:** The cross-layer kernel-inclusion unification (§3.2) is a homology of mathematical forms, not an identity of objects.  
* **Saturation semantics are unestablished:** The saturation-threshold semantics (η\_sat) and everything downstream of it (information horizons, finite-time synchronization) carry status UNDECIDED and must not be cited as established results.

# **5\. Self-Assessment Under the Ternary Standard**

| № | Claim of this document | V\_4 Status | Basis |
| :---- | :---- | :---- | :---- |
| 1 | Contract partition 𝒳 \= ℛ\_K^0 ⊔ ℛ\_K^+ ⊔ ℛ\_K^⊥ (Def 1.1) and confidence-ball states (Def 1.2) | **FOLLOW** | Definitions; consistent with MBEL §5.1–§5.2 via §6 |
| 2 | Four-verdict theorem: totality, determinism, single-valuedness, pairwise incompatibility (Theorem 2.1) | **FOLLOW** | Set-theoretic trichotomy of a partition (two-line proof) |
| 3 | UNDECIDED as boundary intersection; resolution only by ball shrinking or kernel expansion (Corollary 2.1) | **FOLLOW** | Restatement of Theorem 2.1's fourth branch |
| 4 | OMIT subtypes as strata of the clause-stratified kernel (Corollary 2.2) | **FOLLOW** | Definition reading; faithful to MBEL §5.2 priority via stratification labels (unstratified position alone is insufficient) |
| 5 | Refinement monotonicity; decided verdicts are stable under narrowing (Proposition 2.2) | **FOLLOW** | Subset transitivity |
| 6 | Certified narrowing and the geometric non-promotion rule (Corollary 2.3) | **FOLLOW** | Geometric reading; underlying protocol is MBEL §5.3–§5.4 (§0.3) |
| 7 | Semilattice and sLSE\_T properties (§3.1) | **FOLLOW** | Imported verbatim from Spectral Theorems 5.1–5.2 |
| 8 | Kernel inclusion across layers (§3.2.1); unification of tangent, precision-block, and logical kernels | **FOLLOW (per layer) / UNDECIDED (unification)** | Per-layer proven in Spectral Prop 2.1, CPP v4.0 Prop 2.2/Cor 2.3, MBEL §5.1; cross-layer unification is a homology without a transport functor |
| 9 | Saturation criterion η\_sat, horizon screening, finite-time boundary synchronization of unfolded OMIT-states (§3.2.2) | **UNDECIDED** | CPP v4.0 Registry rows 12 (H-L) and 17 (OMIT continuum); composition is unproved |
| 10 | Claim that this geometry replaces the full MBEL cascade (certificates, ensemble laws, two-phase commit) | **OMIT** | Outside declared scope (§0.2); applies to the point/ball layer only |

# **6\. Correspondence: MBEL Constructs ↔ Geometric Core**

| MBEL / Corpus Construct | Geometric Counterpart in This Document |
| :---- | :---- |
| MDNF constituent acy^+ (productive shift under active clause and context) | π\_K(x) ∈ C\_K^+ (interior of the target cone) |
| MDNF constituent ac'y^\~ (indifference / inactive or obstructed context) | x ∈ ker(π\_K) (corresponding kernel stratum) |
| MDNF constituent acy^⊥ (incompatibility), authoritative | x ∈ ℛ\_K^⊥ (outside both kernel and target cone) |
| Axiom 4.1 (prohibition of vacuous truth) | Activity guard p\_prog(E) in the aggregate (§3.1, property 3\) |
| Evidence scope OBSERVED\_TRANSITION | Narrowed ball: certified 𝔹\_t of small radius |
| Evidence scopes PREDICTIVE\_ONLY / NOT\_AVAILABLE; Rel \= 0 | 𝔹\_t \= 𝒳 (full-space inflation → maximal UNDECIDED) |
| Typed certificate (§5.3) | Certified narrowing event 𝔹\_t ↦ 𝔹\_t ∩ Z\_𝒞 (Corollary 2.3) |
| Epistemic UNDECIDED | Ball straddling two or more ontological regions |
| Decision cascade (§4.3) | Any evaluation order of region-membership for the narrowed ball; equivalent by Theorem 2.1 \+ Proposition 2.2 |
| Non-promotion rule (§5.4) | Stability of decided verdicts under narrowing (Corollary 2.3, item 2\) |
| OMIT subtype taxonomy (§5.2) | Kernel strata with controller priority (Corollary 2.2) |
| Scale change / re-verification | Kernel expansion ker(π\_K) ⊆ ker(π\_{K'}) under factorization (Spectral Proposition 2.1) |
| Ensemble law quantifiers (§3.4, Theorem 3.1) | Out of scope (§0.2); point-layer aggregation only via Φ\_cum / sLSE\_T |

*End of document. Version 1.0 (ML Engineering Edition).*