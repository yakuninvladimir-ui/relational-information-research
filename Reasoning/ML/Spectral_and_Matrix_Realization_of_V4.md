# **Spectral and Matrix Realization of V\_4 in Latent Spaces**

**Subtitle:** Tangent-Space Geometry, Kernel-Path Quotients, Four-Channel Verdicts, and Semilattice Aggregation for Neuro-Symbolic State Control  
**Author:** Vladimir Yakunin  
**Version:** 2.2 — Unified Specification (ML Engineering Edition — full structural and mathematical fidelity)  
Date: 2026-10-17  
Status: Formal results are conditional on the assumptions stated below; the existence and learnability of the required geometry remain empirical hypotheses.  
Normative parent: Modified Brusentsov Entailment Logic and Four-Valued Verdict Calculus for External State-Control Systems (MBEL), especially §§3–6.  
**Related foundations:** *The Law of Useful Information Structuring in Model Latent Spaces* (VIM); *Latent Agency Framework* (LAF); *Boundary Projection Theorem* (point/ball-level geometric core of the verdict layer; sibling document — this specification provides the feature-space realization and the aggregation theorems it imports).

# **Abstract & ML Engineering Overview**

**Why this document exists (for ML Engineers):**  
*Modified Brusentsov Entailment Logic* (MBEL) defines how an external Judge evaluates agent transitions using discrete four-valued verdicts:

V\_4 \= { FOLLOW (+1), OMIT (0), UNDECIDED (U), NULL (−1) },   with severity order   FOLLOW ≺\_V OMIT ≺\_V UNDECIDED ≺\_V NULL.

However, deep learning models (world models, encoders, multimodal agents) represent states as continuous vectors z\_t in a high-dimensional latent space Z. How do we bridge continuous latent vectors and Jacobian matrices to discrete symbolic verdicts and knowledge graphs—both at **inference time** (strict verification) and during **gradient-based training** (differentiable loss surrogates)?

This specification builds that bridge across **four distinct architectural layers**, separated into an **Inference Verification Path (§§1–4)** and a **Differentiable Training Path (§§5–6)**:

1. **Layer 1 — Kernel-Path Equivalence (§1):** Given a coarse-graining projection π\_ℓ(z) (which extracts macro-features relevant to a goal at scale ℓ), directions in the tangent kernel K\_z \= ker(dπ\_ℓ(z)) leave the macro-state unchanged to first order. Two latent states z\_0, z\_1 belong to the same equivalence class \[z\]\_ℓ if they can be connected by a continuous path whose tangent vector stays inside K\_z everywhere.  
2. **Layer 2 — Quotient Transition Graph (§2):** The vertices of the symbolic state graph at scale ℓ are these equivalence classes Vert\_ℓ \= D\_ℓ / \~\_{K,ℓ}, and observed transitions τ\_t induce directed edges labelled by crisp MBEL verdicts.  
3. **Layer 3 — Orthogonal Tangent Projectors & Confidence-Ball Diagnostics (§§3–4):** Using a positive-definite tangent metric h\_z, we split each tangent space into three mutually orthogonal subspaces: active progress (W\_act), invariant preservation (W\_inv), and irrelevant kernel motion (K\_z). Rather than trusting raw point estimates or global SNR, we bound the epistemic uncertainty ellipsoid B\_k along each subspace to issue certified geometric predicates (ProgCert\_k, PresCert\_k, LeakCert\_k, RevCert\_k, NeutCert\_k) that feed into the normative MBEL cascade.  
4. **Layer 4 — Cumulative Semilattice & Padding-Invariant Smooth Aggregation (§§5–6):** On the 4-simplex Δ³, mapping verdict weights to cumulative severity coordinates q \= (p^(-), p^(-) \+ p^(U), p^(-) \+ p^(U) \+ p^(0)) turns conjunctive aggregation (⊗) into a coordinatewise maximum. For training, we introduce the **padding-invariant shifted LogSumExp operator (sLSE\_T)**, which leaves satisfied `FOLLOW` clauses completely inert (zero padding bias), absorbs a single crisp `NULL` exactly at any temperature T \> 0, and never under-reports severity.

# **0\. Scope, Conventions, and Notation**

## **0.1. Scope and Authority**

This document specifies a **mathematical realization** of V\_4 in continuous latent spaces, not an empirically guaranteed property of arbitrary neural networks. Normative verdict semantics, evidence certificates, and commit rules remain governed by *Modified Brusentsov Entailment Logic* (MBEL). Every statement in this specification belongs to one of three categories:

* **Formal consequence:** Proven mathematically from the stated definitions and assumptions.  
* **Contract-dependent conclusion:** Holds once a verification contract fixes thresholds, metrics, feature maps, and certificate rules.  
* **Empirical hypothesis:** Requires experimental validation on trained checkpoints (§8.2).

## **0.2. Core Notation Reference (ML Engineer's Cheat Sheet)**

| Symbol | Mathematical Object & ML Engineering Meaning |
| :---- | :---- |
| X\_obs, Enc\_θ, Z | Raw observation space X\_obs, grounding encoder Enc\_θ, and ambient latent space Z |
| M ⊂ Z, D\_ℓ ⊆ M | Encoder image manifold/stratum M and active domain D\_ℓ at scale ℓ |
| g\_obj, ℓ, π\_ℓ | Goal identifier g\_obj, resolution scale ℓ, and C¹ coarse-graining map π\_{g\_obj,ℓ}: D\_ℓ → Y\_ℓ |
| K\_z | Tangent kernel subspace ker(dπ\_ℓ(z): T\_z D\_ℓ → T\_{π\_ℓ(z)} Y\_ℓ) — directions of zero macro-change |
| \~\_{K,ℓ}, \[z\]\_ℓ, cl\_ℓ | Kernel-path equivalence relation, equivalence class of z, and quotient map z ↦ \[z\]\_ℓ |
| G\_ℓ \= (Vert\_ℓ, Ed\_ℓ) | Quotient transition multigraph at scale ℓ |
| g\_I \= g\_approx | Operational information bilinear form from VIM (may be positive semidefinite / rank-deficient) |
| h\_z | Explicit positive-definite Riemannian inner product on T\_z D\_ℓ used to build orthogonal projectors |
| P\_{ker,k}, P\_{act,k}, P\_{inv,k} | Mutually h\_z-orthogonal projectors onto kernel K\_z, active subspace W^{act}*{k,z}, and invariant subspace W^{inv}*{k,z} |
| P\_s, E^s\_z, E^u\_z | Non-orthogonal (oblique) dynamical dichotomy projector and stable/unstable Oseledets subspaces from LAF |
| ξ\_t ∈ T\_{z\_t} D\_ℓ | Local tangent displacement vector of transition τ\_t |
| α\_k, β\_k, ν\_k | Point estimates of directed active progress (α\_k), invariant leakage norm (β\_k), and kernel motion norm (ν\_k) |
| Cov\_{epi,k}, γ\_snr, B\_k | Epistemic covariance on the essential subspace, confidence radius γ\_snr \> 0, and Mahalanobis confidence ball B\_k |
| s\_{act,k}, s\_{inv,k}, α\_k^±, β\_k^± | Projected noise scales and worst/best-case confidence bounds across the ball B\_k (§3.4) |
| G\_{k,z\_t}, δ\_hat^{geom}*k, Ω*{sub,k} | Versioned tangent-to-feature map, mapped feature delta, and contract-declared neutral region (∅ by default) |
| LeakCert\_k, PresCert\_k, RevCert\_k, ProgCert\_k, NeutCert\_k, OutCert\_k | Certified geometric predicates evaluated over the entire confidence ball B\_k (Definition 3.1, §4.2) |
| Δ³, p, Φ\_cum, Q | Four-channel probability/score simplex Δ³, soft verdict vector p, cumulative bijection Φ\_cum, and cumulative cone Q |
| T, T\_g, sLSE\_T, sig | Aggregation temperature T, gate temperature T\_g, padding-invariant shifted LogSumExp, and logistic sigmoid sig(x) |
| ⊗, ≻\_V, ≻\_cg | Step-level conjunctive verdict operator (⊗) under severity order ≻\_V, and spatial coarse-graining order ≻\_cg |

## **0.3. Two Distinct Polarity Orders: Step Conjunction (≼\_V) vs. Spatial Coarse-Graining (≻\_cg)**

ML engineers implementing both step verification and hierarchical graph pooling must keep two orderings distinct:

1. **Single-step conjunctive clause aggregation (≼\_V):** When checking multiple expectations on a single transition τ\_t, all active expectations must succeed for the step to be `FOLLOW`, whereas a single `NULL` breaks the step. Thus `FOLLOW` is the identity element and severity increases as:  
   FOLLOW ≼\_V OMIT ≼\_V UNDECIDED ≼\_V NULL,   with   u ⊗ v := max\_{≼\_V}(u, v).  
2. **Spatial/structural graph coarse-graining (≻\_cg):** When pooling committed micro-nodes/edges `{-, +, 0}` into a macro-node across scales ℓ → ℓ' (MBEL §6.3, Definition 6.1), a macro-element represents a certified state refinement (`+`) if *at least one* essential micro-element achieved `+` while *none* were contradicted (`-`). Thus `FOLLOW` (`+`) dominates `OMIT` (`0`):  
   − (NULL) ≻\_cg \+ (FOLLOW) ≻\_cg 0 (OMIT).

# **1\. State Space and Kernel-Path Equivalence (Inference Layer 1\)**

## **1.1. Geometric Domain and Smoothness Assumptions**

Fix a goal g\_obj, a resolution scale ℓ, and a state domain D\_ℓ ⊆ M (assumed to be a smooth manifold or a smooth stratum of a stratified latent support). Let the coarse-graining map

π\_ℓ := π\_{g\_obj,ℓ}: D\_ℓ → Y\_ℓ

be of class C¹ on each regular stratum, mapping latent states into a smooth macro-descriptor space Y\_ℓ. *(Note: Local Lipschitz continuity alone is insufficient for the chain-rule proofs below, because an absolutely continuous path could spend positive measure on non-differentiable kinks.)*

At each regular point z ∈ D\_ℓ, the **tangent kernel distribution** is the null space of the Jacobian differential:

K\_z := ker( dπ\_ℓ(z): T\_z D\_ℓ → T\_{π\_ℓ(z)} Y\_ℓ ).

A tangent vector v ∈ K\_z is a first-order direction along which the macro-descriptor π\_ℓ(z) has zero derivative. On any regular stratum where rank(dπ\_ℓ) is locally constant, K\_z forms a continuous (and smooth if π\_ℓ ∈ C²) vector subbundle of T D\_ℓ.

## **1.2. Definition of Admissible Kernel Paths and Equivalence**

**Definition 1.1 (Admissible Kernel Path).** Two latent states z\_0, z\_1 ∈ D\_ℓ are joined by an admissible kernel path (written z\_0 ⇝\_{K,ℓ} z\_1) if there exists a piecewise C¹ (or absolutely continuous) curve γ: \[0, 1\] → D\_ℓ such that:

γ(0) \= z\_0,   γ(1) \= z\_1,   and   γ̇(s) ∈ K\_{γ(s)}   for almost every s ∈ \[0, 1\].

**Definition 1.2 (Kernel-Path Equivalence).** We define the relation:

z\_0 \~*{K,ℓ} z\_1   ⟺   z\_0 ⇝*{K,ℓ} z\_1.

The equivalence class of z is denoted \[z\]\_ℓ.

**Proposition 1.1 (Equivalence Relation).** Under Definition 1.1, \~\_{K,ℓ} is reflexive, symmetric, and transitive on D\_ℓ.

*Proof.* Reflexivity holds via the constant path γ(s) ≡ z (γ̇ \= 0 ∈ K\_z). Symmetry holds because for any path γ from z\_0 to z\_1, the time-reversed path γ\_rev(s) \= γ(1 − s) has tangent −γ̇(1 − s) ∈ K\_{γ\_rev(s)} since K\_z is a linear subspace. Transitivity holds by concatenating γ\_1 (from z\_0 to z\_1) and γ\_2 (from z\_1 to z\_2) under a piecewise-linear reparameterization of \[0, 1\]. ∎

## **1.3. Relation Between Kernel-Path Classes and Coarse-Graining Fibers**

**Proposition 1.2 (Kernel Paths Stay Inside a Single Fiber).** If z\_0 \~\_{K,ℓ} z\_1, then π\_ℓ(z\_0) \= π\_ℓ(z\_1).

*Proof.* Because π\_ℓ ∈ C¹ and γ is absolutely continuous, the composite curve π\_ℓ ∘ γ is absolutely continuous and satisfies the chain rule almost everywhere:  
(d/ds)(π\_ℓ ∘ γ)(s) \= dπ\_ℓ(γ(s))\[γ̇(s)\] \= 0   for a.e. s ∈ \[0, 1\].  
An absolutely continuous function with zero derivative almost everywhere is constant, so π\_ℓ(z\_0) \= π\_ℓ(z\_1). ∎

**Crucial topological caveat (Disconnected Fibers):** The converse of Proposition 1.2 does **not** hold in general\! Two points z\_0, z\_1 may have the exact same macro-descriptor π\_ℓ(z\_0) \= π\_ℓ(z\_1) (lying in the same preimage fiber π\_ℓ⁻¹(y)) yet lie in disconnected components of that fiber inside D\_ℓ, making it impossible to move from z\_0 to z\_1 without temporarily changing π\_ℓ. Thus, kernel-path equivalence \~\_{K,ℓ} is generally a **finer partition** than equality of π\_ℓ-values.

**Proposition 1.3 (Kernel-Path Classes Are Path-Connected Fiber Components).** Let U ⊆ D\_ℓ be an open region on which π\_ℓ is C¹ with constant rank, and restrict admissible paths to U. Then the equivalence classes of \~\_{K,ℓ} in U are precisely the path-connected components of the fibers π\_ℓ⁻¹(y) ∩ U.

*Proof.* By the Constant Rank Theorem, each fiber π\_ℓ⁻¹(y) ∩ U is a C¹ embedded submanifold of U with tangent space T\_z(π\_ℓ⁻¹(y)) \= K\_z. By Proposition 1.2, any kernel path remains inside one fiber and, by continuity, inside a single path-connected component. Conversely, any two points in the same path-connected component of a C¹ embedded submanifold can be joined by a piecewise C¹ curve lying inside that submanifold, whose velocity vector necessarily lies in T\_z(π\_ℓ⁻¹(y)) \= K\_z. ∎

**Four Objects Not to Confuse:**  
In code and theory, four subspaces must never be conflated without explicit proof:

1. The differential kernel K\_z \= ker dπ\_ℓ(z) (defined by the task coarse-graining map);  
2. The radical (null space) of the operational information matrix g\_I(z);  
3. The stable contracting Oseledets subspace E^s\_z of the recurrent state-transition Jacobian (from LAF);  
4. The span of small-eigenvalue eigenvectors of an empirical covariance or Fisher matrix.

# **2\. Quotient Transition Graph and Multi-Scale Compatibility (Inference Layer 2\)**

## **2.1. Quotient Graph Vertices**

**Definition 2.1 (Kernel-Path Quotient Vertices).** At goal and scale (g\_obj, ℓ), the symbolic graph vertex set is the quotient set:

Vert\_ℓ := D\_ℓ / \~\_{K,ℓ} \= { \[z\]\_ℓ : z ∈ D\_ℓ },   with quotient map   cl\_ℓ(z) := \[z\]\_ℓ.

By Proposition 1.2, the macro-descriptor descends uniquely to vertices via π\_bar\_ℓ(\[z\]\_ℓ) := π\_ℓ(z). Note that a vertex \[z\]\_ℓ is a kernel-path equivalence class—not a single representative point, not an eigenvector, and not automatically an entire dynamical attractor basin unless that basin is proven to be a single kernel-path component.

## **2.2. Directed Edges from Authoritatively Observed Transitions**

Let T\_auth be the deduplicated set of transitions τ\_t \= (seq\_t, o\_bar\_t, act\_t, o\_bar\_{t+1}) with authoritative scope σ(τ\_t) ∈ {OBSERVED\_TRANSITION, REPLAY\_VERIFIED}. Using the frozen, versioned verifier encoder Enc\_ver to map observations to z\_t, z\_{t+1} ∈ D\_ℓ, each transition induces a directed edge in the **quotient transition multigraph** G\_ℓ \= (Vert\_ℓ, Ed\_ℓ):

edge\_t := ( cl\_ℓ(z\_t), cl\_ℓ(z\_{t+1}); seq\_t, act\_t ),   labelled by the crisp MBEL verdict v\_t ∈ V\_4.

**Why Quotient Geometry Does Not Bypass the MBEL Verifier:**

* Staying inside the same vertex (cl\_ℓ(z\_t) \= cl\_ℓ(z\_{t+1}), a self-loop) indicates that the macro-descriptor at scale ℓ did not change, but does **not** automatically force `OMIT`: if an active confirmed operator was supposed to move the state, staying in place triggers strict stagnation (`NULL` or `UNDECIDED`), or if a global safety invariant was breached intra-step, it triggers `NULL`.  
* Crossing into a new vertex (cl\_ℓ(z\_t) ≠ cl\_ℓ(z\_{t+1})) does **not** automatically force `FOLLOW`: the transition might have moved in the wrong direction (`NULL`) or leaked into an invariant subspace (`NULL`).

**Rules for Merging Parallel Edges:**

1. *Simultaneous conjunctive clauses on one step:* Merge using `⊗` (`NULL ≻_V UNDECIDED ≻_V OMIT ≻_V FOLLOW`).  
2. *Spatial/hierarchical coarse-graining of committed graph elements across scales ℓ → ℓ':* Merge on essential elements using `≻_cg` (`- ≻_cg + ≻_cg 0`, MBEL §6.3).  
3. *Historical ensemble logs across different steps t:* Evaluate via Tier 2 ensemble quantifiers (MBEL §3.4), never by naive `⊗`\-folding.

## **2.3. Cross-Scale Quotient Compatibility (ℓ → ℓ')**

When moving from a fine scale ℓ to a coarser scale ℓ', the inter-scale vertex map cl\_{ℓ→ℓ'}(\[z\]*ℓ) := \[z\]*{ℓ'} is well-defined if and only if \~*{K,ℓ} ⊆ \~*{K,ℓ'}.

**Proposition 2.1 (Factorization Condition for Scale Compatibility).** Suppose D\_ℓ ⊆ D\_{ℓ'} and the coarser projection factors through the finer one via a C¹ map f: π\_{ℓ'} \= f ∘ π\_ℓ. Then at every regular point z ∈ D\_ℓ,

K^(ℓ)*z ⊆ K^(ℓ')z,   which implies   \~{K,ℓ} ⊆ \~*{K,ℓ'},

so the quotient coarsening map cl\_{ℓ→ℓ'}: Vert\_ℓ → Vert\_{ℓ'} is well-defined.

*Proof.* By the chain rule, dπ\_{ℓ'}(z) \= df(π\_ℓ(z)) ∘ dπ\_ℓ(z), which vanishes on K^(ℓ)\_z \= ker dπ\_ℓ(z). Thus every admissible ℓ-kernel path is automatically an admissible ℓ'-kernel path. ∎

# **3\. Tangent-Space Orthogonal Splitting and Confidence-Ball Bounds (Inference Layer 3\)**

## **3.1. Metric Discipline: Regularizing Positive-Semidefinite Information Forms**

In VIM (*Latent Information Structuring*), the operational metric g\_I(z) \= g\_approx(z) (such as a probe Fisher matrix) is often positive semidefinite (rank-deficient). A degenerate matrix cannot define unique orthogonal complements or norms. Therefore, to construct orthogonal projectors on T\_z D\_ℓ, we explicitly fix a \*\* strictly positive-definite inner product h\_z\*\*:

h\_z \= g\_I(z) \+ λ\_reg h^0\_z,   with   λ\_reg \> 0,

where h^0\_z is a declared positive-definite reference metric (e.g., Euclidean I\_d or regularized activation Mahalanobis covariance).

## **3.2. Three-Way Orthogonal Tangent Splitting**

Fix a verification clause e\_k and the positive-definite metric h\_z on T\_z D\_ℓ:

* **For an active change clause (e\_k ∈ E\_act):** Let u\_{exp,k}(z) ∈ K\_z^(⊥\_h) be the externally grounded unit reference vector of expected progress, normalized so that h\_z(u\_{exp,k}, u\_{exp,k}) \= 1\. We define the active and invariant subspaces:  
  W^{act}*{k,z} := span{ u*{exp,k}(z) },   W^{inv}*{k,z} := K\_z^(⊥\_h) ∩ (W^{act}*{k,z})^(⊥\_h).  
* **For a preservation clause (e\_k ∈ E\_inv):** Set W^{act}*{k,z} := {0} and W^{inv}*{k,z} := K\_z^(⊥\_h).

In both cases, the tangent space decomposes into an **h\_z-orthogonal direct sum**:

T\_z D\_ℓ \= K\_z  ⊕\_h  W^{act}*{k,z}  ⊕\_h  W^{inv}*{k,z}.

The corresponding h\_z-orthogonal projectors P\_{ker,k}, P\_{act,k}, P\_{inv,k} satisfy:

Id\_{T\_z D\_ℓ} \= P\_{act,k} \+ P\_{inv,k} \+ P\_{ker,k},   P\_{u,k}² \= P\_{u,k},   P\_{u,k} P\_{v,k} \= 0 (u ≠ v),   P\_{u,k}^(\*h) \= P\_{u,k}.

We also denote the essential (non-kernel) projector by P\_{ess,k} := P\_{act,k} \+ P\_{inv,k} \= Id − P\_{ker,k}.**Geometric Warning (Normal Curvature vs. Tangential Progress):**  
In VIM (§3.2), the minimal-surface balance H(z) \= λ(∇\_Z i(z))⊥ lives in the **normal bundle N\_z M \= (T\_z M)⊥** and describes how training bends the manifold M inside ambient space Z. Its projection onto T\_z D\_ℓ ⊆ T\_z M is identically zero\! By contrast, an agent's runtime state transition moves *along* the manifold inside the **tangent bundle T\_z D\_ℓ**, so u\_{exp,k}(z) lives in T\_z D\_ℓ (related at most to the intrinsic tangential gradient ∇\_M i(z) \= (∇\_Z i(z))⊤, grounded by the external contract).

## **3.3. Representing a State Transition as a Tangent Vector**

Given consecutive grounded latent states z\_t, z\_{t+1} ∈ D\_ℓ within a Riemannian normal neighborhood under h, the transition displacement is the logarithmic map:

ξ\_t := Log^h\_{z\_t}(z\_{t+1}) ∈ T\_{z\_t} D\_ℓ

(or a projected chord in local coordinates when explicitly declared as an approximation). Decomposing ξ\_t via the projectors at z\_t yields:

ξ\_{act,k} := P\_{act,k} ξ\_t,   ξ\_{inv,k} := P\_{inv,k} ξ\_t,   ξ\_{ker,k} := P\_{ker,k} ξ\_t,   ξ\_{ess,k} := P\_{ess,k} ξ\_t.

## **3.4. Point Diagnostics, Epistemic Confidence Balls, and Worst-Case Bounds**

From the decomposed tangent vector, we extract three scalar point estimates:

1. **Directed active progress:** α\_k := h\_{z\_t}(u\_{exp,k}, ξ\_{act,k}) ∈ ℝ;  
2. **Invariant leakage norm:** β\_k := ‖ξ\_{inv,k}‖\_h ≥ 0;  
3. **Local kernel motion norm:** ν\_k := ‖ξ\_{ker,k}‖\_h ≥ 0 (a local diagnostic only).

**Why global SNR fails and why we use Confidence-Ball Bounds:**  
Suppose a preservation clause (e\_k ∈ E\_inv) requires a feature to stay still (ξ\_{ess,k} ≈ 0). Its global Mahalanobis SNR is near zero\! If a verifier required "high SNR" to issue a verdict, it could never certify a satisfied preservation clause. Conversely, a huge displacement along an active axis creates a high global SNR even if the orthogonal invariant axis is completely buried in noise.

Instead, let Cov\_{epi,k} be the positive-definite epistemic covariance matrix on the essential subspace T^{ess}*{k,z} \= Im(P*{ess,k}) (regularized via Cov\_{epi,k} \+ λ\_cov Id if estimated from an ensemble), and let γ\_snr \> 0 be the contract's confidence radius. This defines the **Mahalanobis confidence ball (ellipsoid)**:

B\_k := { ξ ∈ T^{ess}*{k,z} : (ξ − ξ*{ess,k})ᵀ Cov\_{epi,k}⁻¹ (ξ − ξ\_{ess,k}) ≤ γ\_snr² }.

In an h-orthonormal basis, the projected directional noise scales on W^{act}*{k,z} and W^{inv}*{k,z} are:

s\_{act,k} := ‖ Cov\_{epi,k}^(1/2) u\_{exp,k} ‖ \= √( u\_{exp,k}ᵀ Cov\_{epi,k} u\_{exp,k} ),  
s\_{inv,k} := ‖ P\_{inv,k} Cov\_{epi,k}^(1/2) ‖*op \= √( λ\_max( P*{inv,k} Cov\_{epi,k} P\_{inv,k} ) ),

(with s\_{act,k} := 0 for e\_k ∈ E\_inv). This gives the exact worst-case and best-case bounds across all ξ ∈ B\_k:

α\_k^− := α\_k − γ\_snr s\_{act,k},   α\_k^+ := α\_k \+ γ\_snr s\_{act,k},  
β\_k^− := max(0, β\_k − γ\_snr s\_{inv,k}),   β\_k^+ := β\_k \+ γ\_snr s\_{inv,k}.

**Lemma 3.1 (Confidence-Ball Interval Bounds).** For every vector ξ ∈ B\_k, let α(ξ) := h(u\_{exp,k}, P\_{act,k} ξ) and β(ξ) := ‖P\_{inv,k} ξ‖\_h. Then:

α\_k^− ≤ α(ξ) ≤ α\_k^+   and   β\_k^− ≤ β(ξ) ≤ β\_k^+.

*Proof.* Any ξ ∈ B\_k can be written as ξ \= ξ\_{ess,k} \+ Cov\_{epi,k}^(1/2) w with ‖w‖*2 ≤ γ\_snr. By Cauchy–Schwarz, \|α(ξ) − α\_k\| \= \|(Cov*{epi,k}^(1/2) u\_{exp,k})ᵀ w\| ≤ s\_{act,k} γ\_snr. Similarly, by the triangle inequality and operator norm definition, \|β(ξ) − β\_k\| ≤ ‖P\_{inv,k} Cov\_{epi,k}^(1/2) w‖ ≤ s\_{inv,k} γ\_snr, and β(ξ) ≥ 0 gives β\_k^−. ∎

**Definition 3.1 (Certified Directional and Invariant Predicates).** Given contract thresholds θ\_prog \> 0, ε\_rev ≥ 0, and ε\_orth ≥ 0, we define five certified boolean predicates that hold if and only if the **entire confidence ball B\_k** lies inside the corresponding region:

* **Certified Invariant Leakage:** LeakCert\_k  :⟺  β\_k^− \> ε\_orth  (worst-case lower bound breaches tolerance);  
* **Certified Invariant Preservation:** PresCert\_k  :⟺  β\_k^+ ≤ ε\_orth  (worst-case upper bound stays within tolerance);  
* **Certified Sign Reversal:** RevCert\_k  :⟺  α\_k^+ \< −ε\_rev  (entire ball moves backward beyond tolerance);  
* **Certified Active Progress:** ProgCert\_k  :⟺  α\_k^− ≥ θ\_prog  (entire ball achieves required progress);  
* **Certified Sub-Threshold Neutral Band:** NeutCert\_k  :⟺  (α\_k^+ \< θ\_prog) ∧ (α\_k^− ≥ −ε\_rev).

**Proposition 3.2 (Mutual Exclusivity of Certified Predicates).** For any clause e\_k, LeakCert\_k and PresCert\_k are mutually exclusive. For any active clause, RevCert\_k, ProgCert\_k, and NeutCert\_k are pairwise mutually exclusive.

*Proof.* Immediate from β\_k^− ≤ β\_k^+ and α\_k^− ≤ α\_k^+ combined with −ε\_rev ≤ 0 \< θ\_prog. ∎

# **4\. Spectral Evidence and the Normative Verdict Cascade (Inference Layer 4\)**

## **4.1. Feature-Space Calibration Map G\_{k,z\_t}**

Because MBEL contracts specify target sets φ\_{exp,k} and optional bounded neutral regions Ω\_{sub,k} (empty by default, Ω\_{sub,k} ∩ φ\_{exp,k} \= ∅) in the observed feature-delta space F\_k, the verifier contract supplies a versioned, calibrated tangent-to-feature map:

G\_{k,z\_t}: T\_{z\_t} D\_ℓ → F\_k,   δ\_hat^{geom}*k := G*{k,z\_t}(ξ\_t).

Let Cons^{geom}*k \= 1 indicate that G*{k,z\_t} passes its version and consistency check against observed feature deltas δ\_obs(s\_k, F\_k; τ\_t). Under Cons^{geom}*k \= 1, the image of the confidence ball G*{k,z\_t}(B\_k) ⊆ F\_k defines three pairwise disjoint feature-set predicates:

* Cone^{in}*k  :⟺  G*{k,z\_t}(B\_k) ⊆ φ\_{exp,k};  
* SubSetCert\_k  :⟺  G\_{k,z\_t}(B\_k) ⊆ Ω\_{sub,k}  (identically false when Ω\_{sub,k} \= ∅);  
* OutCert\_k  :⟺  G\_{k,z\_t}(B\_k) ⊆ F\_k \\ (φ\_{exp,k} ∪ {0} ∪ Ω\_{sub,k})  (certified out-of-contract active change).

## **4.2. Certified Geometric Classes and Normative MBEL Alignment**

For an active clause (e\_k ∈ E\_act), we group the confidence-ball predicates into three mutually exclusive certified geometric outcomes:

G^{breach}\_k := LeakCert\_k ∨ RevCert\_k ∨ (Cons^{geom}\_k ∧ OutCert\_k),  
G^{real}\_k := Cons^{geom}\_k ∧ ProgCert\_k ∧ PresCert\_k ∧ Cone^{in}\_k,  
G^{neut}\_k := Cons^{geom}\_k ∧ PresCert\_k ∧ ( (NeutCert\_k ∧ Cone^{in}\_k) ∨ SubSetCert\_k ).

For a preservation clause (e\_k ∈ E\_inv), G^{breach}\_k := LeakCert\_k and G^{pres}\_k := PresCert\_k.

**Three Normative MBEL Rules Enforced Here:**

1. **Inactive operator immunity (a\_k \= 0):** If an active clause's operator was not invoked (a\_k \= 0), an exogenous change never triggers `NULL` for e\_k (`OMIT_INCIDENTAL`).  
2. **Obstructed safety separation (a\_k \= 1, c\_k \= 0):** Under an external obstacle (c\_k \= 0), `NULL` is triggered only if a destructive breach of Ob\_safety is certified by an explicit safety certificate Cert^⊥\_k \= 1, never by latent geometry B\_geom alone.  
3. **Feature-level stagnation and redundancy:** Exact state redundancy Eq(τ\_t) (H\_{t+1} \= H\_t) and feature stagnation Zero\_k (δ\_obs(s\_k, F\_k; τ\_t) \= 0\) are read from authoritative structural descriptors, not inferred from small latent steps.

Thus, the combined geometric breach, stagnation, and resolution flags are:

Breach\_k := (e\_k ∈ E\_inv ∧ LeakCert\_k) ∨ (e\_k ∈ E\_act ∧ a\_k \= 1 ∧ c\_k \= 1 ∧ G^{breach}\_k),  
Stag\_k := (e\_k ∈ E\_act) ∧ a\_k \= 1 ∧ c\_k \= 1 ∧ χ\_{conf,k} \= 1 ∧ Auth(τ\_t) \= 1 ∧ Rel(e\_k, τ\_t) \= 1 ∧ Zero\_k,  
Need\_k := ¬Eq(τ\_t) (if e\_k ∈ E\_inv)   else   a\_k \= 1 ∧ ¬Eq(τ\_t) ∧ ¬Zero\_k,  
Res\_k := (B\_geom ∧ LeakCert\_k) ∨ PresCert\_k (if e\_k ∈ E\_inv)   else   (c\_k \= 1 ∧ B\_geom ∧ G^{breach}\_k) ∨ G^{real}\_k ∨ G^{neut}\_k,  
GeoUnres\_k := Need\_k ∧ ¬Res\_k.

## **4.3. Priority Table for Spectral Clause & Transition Evaluation**

| Priority / Verdict | Spectral & MBEL Realization Conditions | Operational Interpretation |
| :---- | :---- | :---- |
| **1\. NULL** (clause level) | Auth \= 1 ∧ Rel \= 1, and: (a) valid Cert^⊥\_k (requires a\_k \= 1 for E\_act; validates Ob\_safety if c\_k \= 0), OR (b) B\_geom ∧ Breach\_k, OR (c) Stag\_k. | Certified contrariety, confidence-ball breach, or unexplained stagnation on a confirmed operator. |
| **2\. UNDECIDED** (clause level) | Not NULL, and: Auth \= 0 ∨ Rel \= 0 ∨ missing/invalid required certificate (including Cert^c\_k) ∨ GeoUnres\_k ∨ (a\_k \= c\_k \= 1 ∧ Zero\_k ∧ χ\_{conf,k} \= 0). | Confidence ball straddles a boundary, tracking is unreliable, or stagnation occurred on an unconfirmed operator. |
| **3\. FOLLOW** (preservation e\_k ∈ E\_inv) | Auth \= 1 ∧ Rel \= 1 ∧ valid Cert^+\_k ∧ (PresCert\_k ∨ Eq(τ\_t)). | Invariant preserved across the entire confidence ball (β\_k^+ ≤ ε\_orth); no positive SNR required. |
| **4\. FOLLOW** (active e\_k ∈ E\_act) | a\_k \= c\_k \= 1 ∧ Auth \= 1 ∧ Rel \= 1 ∧ valid Cert^+\_k ∧ G^{real}\_k. | Certified progress inside target cone (α\_k^− ≥ θ\_prog) with zero invariant leakage (β\_k^+ ≤ ε\_orth). |
| **5\. OMIT\_BLOCKED** (transition subtype) | Aggregate base verdict is OMIT; E\_act ≠ ∅ and ∃e\_k ∈ E\_act with a\_k \= 1, c\_k \= 0 (certified by pre-outcome Cert^c\_k) and (Zero\_k ∨ Eq(τ\_t) ∨ G^{neut}\_k). | Non-destructive soft stop against a boundary/obstacle. Halts route cursor and triggers local repair. |
| **6\. OMIT\_REDUNDANT** (transition subtype) | Aggregate base verdict is OMIT; not OMIT\_BLOCKED; and Eq(τ\_t) (H\_{t+1} \= H\_t). | Exact descriptor equality. Triggers NoopRepeatGuard. |
| **7\. OMIT\_INCIDENTAL** (transition subtype) | Aggregate base verdict is OMIT; neither BLOCKED nor REDUNDANT; all evidence resolved; covers a\_k \= c\_k \= 1 ∧ G^{neut}\_k, or a\_k \= 1, c\_k \= 0 ∧ G^{real}\_k, or a\_k \= 0\. | Admissible sub-threshold drift or orthogonal activity of another operator. |
| **8\. UNDECIDED** (fallback) | Defensive catch-all if none of 1–7 hold. | Guarantees totality without fabricating OMIT. |

## **4.4. Normative Semilattice Aggregation Across Clauses**

With transition-level scope factor v\_scope ∈ {FOLLOW, UNDECIDED}, global safety factor v\_inv ∈ {FOLLOW, UNDECIDED, NULL}, and the vacuous-truth guard prog(E) \= OMIT (if E\_act \= ∅) else FOLLOW (MBEL Axiom 4.1), the crisp step verdict is:

Verdict(E, τ\_t) \= v\_scope ⊗ v\_inv ⊗ ( ⨂\_{e\_k ∈ E} v\_k ) ⊗ prog(E).

# **5\. Four-Channel Simplex and Cumulative Semilattice Aggregation (Training Layer 1\)**

## **5.1. The Four-Channel Verdict Simplex Δ³**

To train models or rank candidate trajectories via gradients, we embed the four verdicts as the standard basis vertices of the 3-simplex Δ³ \= { p \= (p^(+), p^(0), p^(U), p^(−))ᵀ ∈ \[0, 1\]⁴ : ∑ p^(s) \= 1 }:

e\_(+) \= (1, 0, 0, 0)ᵀ (FOLLOW),   e\_(0) \= (0, 1, 0, 0)ᵀ (OMIT),   e\_(U) \= (0, 0, 1, 0)ᵀ (UNDECIDED),   e\_(−) \= (0, 0, 0, 1)ᵀ (NULL).

## **5.2. Cumulative Severity Coordinates Φ\_cum**

Define the affine bijection Φ\_cum: Δ³ → Q := { q ∈ \[0, 1\]³ : 0 ≤ q\_1 ≤ q\_2 ≤ q\_3 ≤ 1 } and its explicit inverse:

q \= Φ\_cum(p) := \[ p^(−),  p^(−) \+ p^(U),  p^(−) \+ p^(U) \+ p^(0) \]ᵀ,  
Φ\_cum⁻¹(q) \= \[ 1 − q\_3,  q\_3 − q\_2,  q\_2 − q\_1,  q\_1 \]ᵀ.

Under Φ\_cum, the four crisp verdicts become a monotone chain of binary vectors in Q:

Φ\_cum(e\_(+)) \= (0, 0, 0)ᵀ,   Φ\_cum(e\_(0)) \= (0, 0, 1)ᵀ,   Φ\_cum(e\_(U)) \= (0, 1, 1)ᵀ,   Φ\_cum(e\_(−)) \= (1, 1, 1)ᵀ.

## **5.3. Exact Semilattice Join on Δ³ and Axiom 4.1 Guard**

Because the crisp cumulative images are ordered coordinatewise, the exact semilattice conjunction `⊗` on Δ³ is simply the coordinatewise maximum in cumulative coordinates:

⨂\_{m=1}^M p\_m := Φ\_cum⁻¹( max\_{m=1..M} Φ\_cum(p\_m) ),   where   (⋁\_m q\_m)*j \= max\_m q*{m,j}.

Including the Axiom 4.1 progress guard vector p\_prog(E) \= e\_(0) (if E\_act \= ∅) else e\_(+) in the factor list P(E, τ\_t) \= (p\_1, ..., p\_{n\_E}, e\_(v\_scope), e\_(v\_inv), p\_prog(E)) guarantees that an empty active expectation set never evaluates to `FOLLOW`.

**Theorem 5.1 (Exact Cumulative Semilattice Realization).** The operation `⊗` on Δ³ is associative, commutative, and idempotent, with identity element e\_(+) (`FOLLOW`) and absorbing annihilator e\_(−) (`NULL`). On crisp basis vectors, ⨂\_{m=1}^M e\_(v\_m) \= e\_(max\_{≼\_V} {v\_1, ..., v\_M}), reproducing Verdict(E, τ\_t) identically.

*Proof.* Transport of the coordinatewise maximum lattice properties on Q \= {0 ≤ q\_1 ≤ q\_2 ≤ q\_3 ≤ 1} via the affine bijection Φ\_cum. ∎

## **5.4. Padding-Invariant Shifted LogSumExp (sLSE\_T)**

**Why standard LogSumExp and LogMeanExp fail in verification:**

* *Standard LogSumExp* T log(∑\_m exp(q\_{m,j}/T)) suffers from **padding inflation**: each satisfied `FOLLOW` factor (q\_{m,j} \= 0\) contributes exp(0) \= 1 to the sum, so adding 5 satisfied clauses to 1 `OMIT` clause fabricates a spurious `NULL` mass of \~0.18 at T \= 0.1.  
* *Normalized LogMeanExp* T log((1/M) ∑\_m exp(q\_{m,j}/T)) suffers from **veto dilution**: a single certified `NULL` (q \= 1\) among 5 `FOLLOW` clauses is diluted to \~0.36 at T \= 0.5.

We solve both problems simultaneously with the **padding-invariant shifted LogSumExp operator**:

sLSE\_T(x\_1, ..., x\_M) := min{ 1,  T log( 1 \+ ∑\_{m=1}^M ( exp(x\_m / T) − 1 ) ) },   for x ∈ \[0, 1\]^M, T \> 0\.

The smooth cumulative join on Δ³ is then:

q\_j^(T) := sLSE\_T(Q\_{1,j}, ..., Q\_{M,j}),   ⨂\_{T, m=1}^M p\_m := Φ\_cum⁻¹(q^(T)).

**Theorem 5.2 (Five Exact Guarantees of sLSE\_T).** Let T \> 0, M ≥ 1, p\_m ∈ Δ³, Q\_m \= Φ\_cum(p\_m), q\_j^(0) \= max\_m Q\_{m,j}, and K\_j \= \#{m : Q\_{m,j} \> 0}. Then:

1. **Simplex Closure:** 0 ≤ q\_1^(T) ≤ q\_2^(T) ≤ q\_3^(T) ≤ 1, so ⨂\_T p\_m ∈ Δ³.  
2. **Conservative One-Sided Bound (Never Under-Reports Severity):** q\_j^(0) ≤ q\_j^(T) ≤ min{ 1, q\_j^(0) \+ T log K\_j } (with q\_j^(T) \= 0 if K\_j \= 0).  
3. **Exact Padding Invariance (`FOLLOW` Inertia):** Appending any number of `FOLLOW` factors e\_(+) (where Q\_m \= (0, 0, 0)ᵀ) contributes exp(0) − 1 \= 0 and leaves q^(T) completely unchanged for any M and T \> 0\.  
4. **Exactness on All Crisp Inputs at Any Temperature:** If every p\_m is a crisp vertex of Δ³, then ⨂\_T p\_m \= ⨂ p\_m for every T \> 0\. In particular, a single crisp `NULL` factor forces the exact output e\_(−) at every T \> 0\.  
5. **Uniform Convergence:** ‖ ⨂\_T p\_m − ⨂ p\_m ‖\_∞ ≤ T log M → 0 as T → 0⁺.

*Proof.* Retaining only the maximum term gives 1 \+ ∑\_m (e^(x\_m/T) − 1\) ≥ e^(max x\_m / T), proving q\_j^(0) ≤ q\_j^(T). Bounding each of the K\_j positive terms by e^(q\_j^(0)/T) − 1 gives 1 \+ K\_j(e^(q\_j^(0)/T) − 1\) ≤ K\_j e^(q\_j^(0)/T) since K\_j ≥ 1, proving the upper bound. Monotonicity of sLSE\_T in each coordinate preserves q\_1^(T) ≤ q\_2^(T) ≤ q\_3^(T). Zero inputs contribute e⁰ − 1 \= 0, giving padding invariance. If any crisp input has Q\_{m,j} \= 1, then 1 \+ ∑ (e^(Q\_{m,j}/T) − 1\) ≥ e^(1/T), so T log(·) ≥ 1 and the cap at 1 returns exactly 1\. ∎

# **6\. Differentiable Spectral Gates for Optimization (Training Layer 2\)**

## **6.1. Smooth Clause Gate Construction (PyTorch-Ready)**

During training or trajectory ranking (never as a substitute for crisp post-transition commit verification), each clause e\_k is mapped to a soft score vector p\_k ∈ Δ³ using logistic sigmoids sig(x) \= 1 / (1 \+ e^(−x)) at gate temperature T\_g \> 0:

```py
import torch

def smooth_clause_verdict_gate(
    alpha_minus, alpha_plus, beta_minus, beta_plus,
    theta_prog: float, eps_rev: float, eps_orth: float, T_g: float,
    Au: float, Re: float, iota_k: float, a_k: float, c_k: float,
    chi_conf: float, Zero_k: float, Eq: float, B_geom: float,
    C_perp: float, u_cert: float, Cons_geom: float,
    m_cone: float = 1.0, m_sub: float = 0.0, m_out: float = 0.0
):
    """
    Computes the differentiable 4-channel soft verdict p_k = [p^(+), p^(0), p^(U), p^(-)] in Δ³
    for a single clause e_k, matching §6.1 of Spectral Realization v2.2.
    """
    sig = torch.sigmoid
    u_map = (1.0 - iota_k) * a_k * (1.0 - Cons_geom)

    # 1. Smooth confidence-ball predicates
    b_br = sig((beta_minus - eps_orth) / T_g)
    b_ok = sig((eps_orth - beta_plus) / T_g)
    r_br = sig((-eps_rev - alpha_plus) / T_g)
    r_pr = sig((alpha_minus - theta_prog) / T_g)
    r_ne = sig((theta_prog - alpha_plus) / T_g) * sig((alpha_minus + eps_rev) / T_g)

    # 2. Active & invariant geometric composite scores
    g_br_act = 1.0 - (1.0 - b_br) * (1.0 - r_br) * (1.0 - (1.0 - u_map) * m_out)
    g_real_act = (1.0 - u_map) * r_pr * b_ok * m_cone
    g_neut_act = (1.0 - u_map) * b_ok * (1.0 - (1.0 - r_ne * m_cone) * (1.0 - m_sub))
    h_br = iota_k * b_br + (1.0 - iota_k) * a_k * c_k * g_br_act

    # 3. Contradiction score d_- (NULL channel)
    kappa_perp = iota_k + (1.0 - iota_k) * a_k
    S_k = (1.0 - iota_k) * a_k * c_k * chi_conf * Zero_k
    d_minus = Au * Re * kappa_perp * (
        C_perp + (1.0 - C_perp) * (S_k + (1.0 - S_k) * B_geom * h_br)
    )

    # 4. Uncertainty score d_U (UNDECIDED channel)
    need_k = iota_k * (1.0 - Eq) + (1.0 - iota_k) * a_k * (1.0 - Eq) * (1.0 - Zero_k)
    res_k = iota_k * (1.0 - (1.0 - B_geom * b_br) * (1.0 - b_ok)) + (1.0 - iota_k) * (
        1.0 - (1.0 - c_k * B_geom * g_br_act) * (1.0 - g_real_act) * (1.0 - g_neut_act)
    )
    u_scope, u_rel = 1.0 - Au, 1.0 - Re
    u_stag = (1.0 - iota_k) * a_k * c_k * (1.0 - chi_conf) * Zero_k
    u_geo = need_k * (1.0 - res_k)
    d_U = 1.0 - (1.0 - u_scope) * (1.0 - u_rel) * (1.0 - u_cert) * (1.0 - u_map) * (1.0 - u_stag) * (1.0 - u_geo)

    # 5. Realization score g_+ and priority partition into Δ³
    g_plus = iota_k + (1.0 - iota_k) * a_k * c_k * (1.0 - Zero_k) * (1.0 - Eq) * g_real_act
    p_minus = d_minus
    p_U = (1.0 - d_minus) * d_U
    rem = (1.0 - d_minus) * (1.0 - d_U)
    p_plus = rem * g_plus
    p_zero = rem * (1.0 - g_plus)
    return torch.stack([p_plus, p_zero, p_U, p_minus], dim=-1)


def slse_aggregate(p_list: torch.Tensor, T: float = 0.05) -> torch.Tensor:
    """
    Aggregates a stack of M soft verdict vectors p_list [..., M, 4] in Δ³
    using the padding-invariant shifted LogSumExp operator sLSE_T (§5.4).
    """
    # Φ_cum: [p^(-), p^(-) + p^(U), p^(-) + p^(U) + p^(0)]
    q1 = p_list[..., 3]
    q2 = q1 + p_list[..., 2]
    q3 = q2 + p_list[..., 1]
    Q = torch.stack([q1, q2, q3], dim=-1)  # [..., M, 3]

    # sLSE_T(Q) = min(1, T * log(1 + sum(exp(Q / T) - 1)))
    sum_expm1 = torch.sum(torch.expm1(Q / T), dim=-2)
    q_agg = torch.clamp(T * torch.log1p(sum_expm1), min=0.0, max=1.0)

    # Φ_cum^(-1)
    p_plus = 1.0 - q_agg[..., 2]
    p_zero = q_agg[..., 2] - q_agg[..., 1]
    p_U = q_agg[..., 1] - q_agg[..., 0]
    p_minus = q_agg[..., 0]
    return torch.stack([p_plus, p_zero, p_U, p_minus], dim=-1)
```

## **6.2. Exact Zero-Temperature Convergence Properties (T\_g → 0⁺)**

Away from threshold boundaries, as T\_g → 0⁺, the soft gate converges pointwise to the exact crisp clause verdicts of §4.3:

1. **Inactive active clauses (a\_k \= 0):** κ\_{⊥,k} \= 0 forces d\_− \= 0, need\_k \= 0, and g\_+ \= 0, converging to e\_(0) (`OMIT`) even if another operator caused orthogonal changes.  
2. **Satisfied preservation clauses (e\_k ∈ E\_inv, β\_k^+ \< ε\_orth):** Converges to e\_(+) (`FOLLOW`) with zero SNR penalty when β\_k \= 0\.  
3. **Sub-threshold vs. out-of-contract active moves:** Expected-set sub-threshold moves converge to e\_(0) (`OMIT`) even when Ω\_{sub,k} \= ∅; out-of-contract moves (`OutCert_k`) converge to e\_(−) (`NULL`) when B\_geom \= 1\.  
4. **Obstructed active moves (a\_k \= 1, c\_k \= 0):** Trigger d\_− → 1 (`NULL`) only when C^⊥ \= 1 validates a breach of Ob\_safety; soft stops converge to e\_(0) (`OMIT`).

# **7\. Projector Authority and Anti-Wireheading Boundary**

## **7.1. The Wireheading / Self-Confirmation Failure Mode**

If a policy or proposer network is allowed to backpropagate its reward/verdict loss into the verifier's encoder Enc\_ver, metric h\_z, active direction u\_{exp,k}, or kernel projector P\_{ker,k}, it will "wirehead" the Judge: instead of solving the task in the environment, it will rotate u\_{exp,k} toward whatever random motion it generates, or expand K\_z so that safety breaches fall into the kernel (`OMIT`).

## **7.2. Invariant 7.1 (Strict Separation of Verifier Authority & Stop-Gradient Rules)**

1. **Verifier Ownership:** The coarse-graining map π\_ℓ, metric h\_z, projectors P\_{act,k}, P\_{inv,k}, P\_{ker,k}, reference vector u\_{exp,k}, feature calibration map G\_{k,z\_t}, covariance Cov\_{epi,k}, thresholds, and **the verifier encoder checkpoint Enc\_ver** are owned exclusively by the external Verifier/Binder and must be version-logged.  
2. **Stop-Gradient (`detach()`) Boundary During Policy Planning:** When a policy optimizes a planned displacement ξ\_hat\_t against the differentiable gate, all verifier-owned tensors must be wrapped in a stop-gradient operator (`sg` / `.detach()`):  
   α\_hat^{plan}*k \= sg( h(u*{exp,k}, P\_{act,k} ·) )\[ξ\_hat\_t\],   β\_hat^{plan}*k \= ‖ sg(P*{inv,k}) ξ\_hat\_t ‖\_h.  
3. **Frozen Verifier Encoder Checkpoint:** Even if the policy and verifier share a backbone architecture, factual and surrogate verdicts must be evaluated through a frozen checkpoint `Enc_ver` (`with torch.no_grad():` on `θ_ver`). Updating `Enc_ver` is a versioned migration that requires re-calibrating all projectors, covariances, and thresholds.  
4. **Non-Promotion of Rollout Scores:** Differentiable gate outputs on `PREDICTIVE_ONLY` rollouts are used solely for planning/ranking or pre-action safety vetoes; only post-action `OBSERVED_TRANSITION` / `REPLAY_VERIFIED` records evaluated by the crisp MBEL cascade may update state memory or law counters.

# **8\. Alignment with VIM and the Latent Agency Framework (LAF)**

## **8.1. Three Mathematical Distinctions Across the Corpus**

1. **VIM Metric Spectrum vs. Coarse-Graining Kernel K\_z:** Minimizing the VIM volume surrogate Vol\_hat\_θ encourages compression of redundant directions, but does *not* mathematically prove that the zero-eigenvalue radical of g\_I equals K\_z \= ker dπ\_ℓ(z). Treating low-eigenvalue directions as K\_z requires an explicit numerical validation protocol.  
2. **VIM Normal Curvature vs. Spectral Tangential Directions:** In VIM, H(z) \= λ(∇\_Z i(z))⊥ lies in the normal bundle N\_z M (perpendicular to M), whereas the active progress vector u\_{exp,k}(z) in this specification lies in the tangent bundle T\_z D\_ℓ ⊆ T\_z M.  
3. **Static h\_z-Orthogonal Projectors vs. LAF Oblique Oseledets Projectors:** In *Latent Agency Framework* (LAF §4.2 D7, §5.2 D11), tangent dynamics v(n+1) \= M(n)v(n) split T\_z M \= E^s\_z ⊕ E^u\_z via the dynamical dichotomy projector P\_s \= R^{vv}. Keep three differences in mind:  
   * *Oblique vs. Orthogonal:* In recurrent networks, E^s\_z and E^u\_z intersect at oblique angles (P\_s is non-self-adjoint), whereas P\_{ker,k}, P\_{act,k}, P\_{inv,k} are strictly h\_z-orthogonal.  
   * *Dual role of contracting directions E^s\_z:* Depending on the time window τ\_w and contract clause, transverse contraction in E^s\_z (rate κ(U)) may correspond either to irrelevant micro-perturbations relaxing back to the same macro-state (K\_z) or to actively maintained homeostatic/viability invariants (W^{inv}\_{k,z}), while inter-basin transitions move along E^u\_z.  
   * *Invariance:* LAF's Lyapunov spectrum is a diffeomorphism invariant of autonomous dynamics, whereas clause projectors are anchored to externally grounded verifier contracts.

## **8.2. Testable Empirical Hypotheses**

* VIM regularization induces a sharper spectral gap between task-essential directions (W^{act} ⊕ W^{inv}) and task-insensitive kernel directions (K\_z).  
* Empirically estimated kernel-path quotient vertices align with discrete symbolic states and macroscopic attractor basins on benchmark control tasks.  
* On stationary phases within a basin, the oblique LAF dichotomy projector P\_s onto E^s\_z statistically aligns with P\_{ker,k} ⊕ P\_{inv,k}.

# **9\. Verification Status Table of Claims**

| Claim in This Specification | Status | Mathematical / Operational Basis |
| :---- | :---- | :---- |
| Kernel-path reachability \~\_{K,ℓ} is an equivalence relation | **FOLLOW (formal)** | Proposition 1.1 |
| Kernel-path equivalence implies equal macro-descriptors π\_ℓ(z\_0) \= π\_ℓ(z\_1) | **FOLLOW (formal, C¹ π\_ℓ)** | Proposition 1.2 (chain rule) |
| Kernel-path classes coincide with path-connected fiber components on constant-rank C¹ regions | **FOLLOW (formal)** | Proposition 1.3 (Constant Rank Theorem) |
| Quotient graph vertices are equivalence classes D\_ℓ / \~\_{K,ℓ} | **FOLLOW (definition)** | Definition 2.1 |
| Cross-scale quotient coarsening and status compositionality hold | **CONDITIONAL** | Requires \~*{K,ℓ} ⊆ \~*{K,ℓ'} (Prop 2.1) and essential-subset compatibility under ≻\_cg (MBEL Prop 6.1) |
| Three-way orthogonal tangent projector splitting exists | **CONDITIONAL** | Requires positive-definite h\_z and grounded u\_{exp,k} ∈ K\_z^(⊥\_h) (§3.1–3.2) |
| Interval bounds \[α\_k^−, α\_k^+\] and \[β\_k^−, β\_k^+\] hold across confidence ball B\_k | **FOLLOW (formal)** | Lemma 3.1 (Cauchy–Schwarz & operator norm) |
| Certified geometric predicates are pairwise mutually exclusive | **FOLLOW (formal)** | Proposition 3.2 and disjointness of feature target sets (§4.1–4.2) |
| Spectral cascade and soft gate enforce inactive-operator immunity (a\_k \= 0), obstructed safety separation (c\_k \= 0), and preservation resolution | **CONDITIONAL** | Requires calibrated G\_{k,z\_t}, valid safety certificates Cert^⊥\_k under c\_k \= 0, and gating rules of §§4.1–4.3, §6.1 |
| Cumulative map Φ\_cum is an affine bijection between Δ³ and Q | **FOLLOW (formal)** | Explicit inverse in §5.2 |
| Exact cumulative join (with p\_prog(E)) reproduces the MBEL semilattice and Axiom 4.1 | **FOLLOW (formal)** | Theorem 5.1 |
| Shifted operator sLSE\_T preserves Δ³, leaves FOLLOW inert, is exact on crisp inputs at all T \> 0, never under-reports severity, and converges at O(T log M) | **FOLLOW (formal)** | Theorem 5.2 |
| Soft gate (§6.1) converges to crisp clause verdicts as T\_g → 0⁺ away from thresholds | **CONDITIONAL** | Verified analytically and numerically away from boundary ties (§6.2) |
| Uncalibrated spectral margins alone certify NULL | **NOT CLAIMED** | Requires verifier authority, Rel \= 1, B\_geom \= 1, or Cert^⊥\_k |
| VIM training automatically makes ker(g\_I) \= K\_z | **UNDECIDED** | Empirical hypothesis (§8.1–8.2) |
| LAF oblique dichotomy projector P\_s equals P\_{ker,k} | **UNDECIDED** | Distinct mathematical objects; statistical alignment is empirical (§8.1) |

# **10\. Explicit Non-Claims and Implementation Checklist**

## **Explicit Non-Claims**

1. **Eigenvalue cutoff ≠ Kernel equivalence:** The quotient is defined by path connectivity under K\_z \= ker dπ\_ℓ(z), not by an unvalidated eigenvalue threshold.  
2. **Quotient vertex ≠ Dynamical basin by default:** A basin forms a single vertex only if all its states are mutually kernel-path connected inside D\_ℓ.  
3. **Kernel equivalence ≠ Continuous step tolerance Tol\_K:** Step tolerance in metric contracts is non-transitive and asymmetric; kernel equivalence \~\_{K,ℓ} is a strict equivalence relation.  
4. **Staying in \[z\]\_ℓ ≠ automatic OMIT:** The full MBEL cascade (including stagnation checks and global invariants) governs the verdict.  
5. **Inactive (a\_k \= 0\) and obstructed (c\_k \= 0\) safeguards:** Exogenous changes under a\_k \= 0 never trigger clause `NULL`; obstructed moves under c\_k \= 0 trigger `NULL` only via an explicit safety certificate Cert^⊥\_k for Ob\_safety.  
6. **Confidence balls replace global SNR gating:** Preservation clauses (e\_k ∈ E\_inv) are certified via β\_k^+ ≤ ε\_orth without needing positive signal norm.  
7. **Soft gate scores ≠ Factual commits:** Soft vectors p ∈ Δ³ are strictly for training/ranking; state commits require the crisp post-transition MBEL cascade.

## **Nine Mandatory Conformance Checks for Engineering Implementations**

An implementation of this specification must pass nine automated unit tests:

5. **Versioned Maps and C¹ Rank Check:** Version-log the coarse-graining map π\_ℓ, kernel-path rule, tangent-to-feature map G\_{k,z\_t}, its consistency check Cons^{geom}\_k, and the declared feature-space neutral sets Ω\_{sub,k} (empty by default), and verify that π\_ℓ is C¹ with locally constant rank on the active regions (§1.1).  
6. **Projector Algebra Validation:** Numerically verify idempotence (P² \= P), mutual h\_z-orthogonality (P\_u P\_v \= 0 for u ≠ v), self-adjointness (P^{\*h} \= P), and completeness (P\_{act,k} \+ P\_{inv,k} \+ P\_{ker,k} \= Id) under the regularized positive-definite metric h\_z (§3.1–3.2).  
7. **Kernel-Path Fiber Preservation:** Verify that every declared admissible kernel path preserves π\_ℓ within numerical tolerance (§1.2–1.3).  
8. **Cross-Scale Compatibility:** Verify kernel inclusion \~\_{K,ℓ} ⊆ \~\_{K,ℓ'} (Proposition 2.1) and essential-subset preimage compatibility under ≻\_cg (MBEL Proposition 6.1) before constructing multi-scale graph links (§2.3).  
9. **Exhaustive Crisp Cascade Unit Tests:** Test the crisp verdict cascade against all MBEL edge cases, including inactive-operator immunity (a\_k \= 0 never triggers clause NULL), obstructed safety breaches (a\_k \= 1, c\_k \= 0 requires a valid safety certificate Cert^⊥\_k for Ob\_safety), expected-set sub-threshold progress remaining neutral (OMIT\_INCIDENTAL) even when Ω\_{sub,k} \= ∅, out-of-contract changes being rejected via OutCert\_k, and Axiom 4.1 vacuous-truth prevention when E\_act \= ∅ (§4.2–4.4).  
10. **Semilattice and sLSE\_T Guarantees:** Numerically verify the 4×4 semilattice table, the p\_prog(E) guard, FOLLOW inertia (zero padding bias), exactness on crisp inputs at all temperatures T \> 0, and the O(T log M) uniform convergence bound of Theorem 5.2 (§5.3–5.4).  
11. **Non-Promotion Guard:** Enforce in code that PREDICTIVE\_ONLY rollout scores and soft gate vectors p ∈ Δ³ can never enter factual state-commit or law-counter update paths (§7.2).  
12. **Certified Predicate Exclusivity & Zero-Temperature Gate Agreement:** Test mutual exclusivity of the certified confidence-ball classes (Proposition 3.2 and §4.2) and verify that smooth\_clause\_verdict\_gate (§6.1) converges to the exact crisp clause outcomes of §4.3 as T\_g → 0⁺ on randomized test inputs bounded away from thresholds (§6.2).  
13. **Frozen Verifier Encoder Authority:** Freeze and version-lock the verifier encoder checkpoint Enc\_ver and verify that stop-gradient (detach) blocks all policy/proposer gradients from flowing into Enc\_ver, h\_z, and the projectors (§7.2, Invariant 7.1).

---

*End of specification. Normative verdict semantics: Modified Brusentsov Entailment Logic, §§3–6.*