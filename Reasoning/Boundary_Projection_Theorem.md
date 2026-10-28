# **The Boundary Projection Theorem, the Kernel of Insignificance, and the Four-Valued Verdict (Geometric Core of `V_4`)**

**Author:** Vladimir Yakunin  
**Version:** 1.0 (revised from the conceptual-core draft)  
**Date:** 2026-10-22  
**Status:** Derived geometric semantics of the verdict layer at the point/ball level. A domain instantiation of the canonical calculus; **not** a replacement of the normative cascade (see §0).  
**Normative parent:** *Modified Brusentsov Entailment Logic* (`Reasoning/Modified_Brusentsov_Entailment_Logic.md`), especially §§3–5. Where this document and the canonical specification differ, the canonical specification governs.  
**Siblings:** *Spectral and Matrix Realization of `V_4` in Latent Spaces* (feature-space realization, estimators, and aggregation theorems — this document reuses its Thm 5.1–5.2 verbatim); *Latent Agency Framework v2.1* §8 and *Causal Phase Program v4.0* §2.4 (boundary kernel-inclusion conditions, imported here as the cross-layer preservation form).  
**Purpose:** A single geometric theorem — the projection of the observation confidence ball through the boundary (contract) with a kernel — that carries the point-level verdict semantics, replacing scattered case tables at this layer only.

---

## **Abstract**

The verification and agency architecture of the archive admits a compact geometric core at the level of point verdicts. It reduces to three mathematical constructions:

1. **A single object (the projection triad):** the micro-dynamics mapped through a boundary operator (contract / scale) $`\pi_K`$ with the insignificance kernel $`\ker \pi_K`$ and the target cone $`C_K^+`$, at finite observation resolution given by a confidence ball $`\mathcal{B}_t`$.
2. **The four-verdict theorem (`V_4`):** a total, deterministic, single-valued classification of the position of the ball image $`\pi_K(\mathcal{B}_t)`$ relative to the kernel zero $`\{0\}`$ and the cone $`C_K^+`$. Brusentsov's three-valued ontology $`\{+, 0, -\}`$ partitions the *points* of the space, while the fourth status `UNDECIDED` ($`U`$) arises as a purely topological consequence of passing from points to finite-radius *sets* $`\mathcal{B}_t`$ (intersection with region boundaries).
3. **The composition-and-scale law:** aggregation of multiple contracts on the linear dominance semilattice via the cumulative operator $`\mathrm{sLSE}_T`$, and the structure-preservation condition for transmission across a boundary ($`\ker \pi_{\mathrm{int}} \subseteq \ker \pi_{\mathrm{ext}}`$ at an unsaturated channel $`\eta_{\mathrm{sat}} < 1`$ — the physical reading of the threshold is `UNDECIDED`, §3.2).

This document is a **derived semantics** of the canonical calculus: typed certificates, ensemble law quantifiers, and the two-phase commit protocol remain governed by MBEL; feature-space estimators and confidence-ball construction remain governed by the Spectral realization. The correspondence is fixed row-by-row in §6; the coverage boundary is declared in §0.

---

## **0. Scope and Authority**

### **0.1. What this document covers**

- The **point/ball verdict layer**: a single contract $`K`$, a single observation window $`\tau_w`$, one confidence set $`\mathcal{B}_t`$, and the resulting verdict (Theorem 2.1).
- **Refinement dynamics** of the ball under certified evidence and the stability of decided verdicts (Proposition 2.2, Corollary 2.3).
- **Aggregation** of point verdicts across contracts, imported without change from the Spectral realization (§3.1).
- The **boundary preservation condition** in its three corpus instantiations (§3.2), with explicit statuses.

### **0.2. What this document does not cover (authority remains with the normative parent)**

- Typed verification certificates and evidence scopes beyond their ball-size reading (MBEL §5.3; Spectral §3.4–§4.1).
- Ensemble law quantifiers and the Hempel–Nicod immunity (MBEL §3.4, Thm 3.1).
- Two-phase commit, pending tokens, and rollback (MBEL §5.4).
- The variational minimal-surface layer (VIM / latent information structuring) — geometrically adjacent but logically independent of the verdict core; it is **not** part of this reduction.
- Feature-space diagnostics ($`\alpha_k, \beta_k, \nu_k`$, Mahalanobis SNR) — these construct $`\mathcal{B}_t`$ and belong to the Spectral realization.

### **0.3. Priority rule**

Every mapping in §6 is a *representation* of the canonical constructs, not a redefinition. In any conflict of verdict semantics, MBEL §§1–5 govern.

---

## **1. The Single Object: Projection Triad, Kernel, and Confidence Ball**

Let $`\mathcal{X}`$ be the space of elementary transitions (or tangent state shifts) of the system under consideration, on a time window $`\tau_w`$ and resolution scale $`\ell`$.

### **Definition 1.1 (Boundary Contract and the Three-Valued Ontological Partition)**

A verification contract (a law, or a scale description) $`K`$ is given by a projection operator

```math
\pi_K: \mathcal{X} \longrightarrow \mathcal{Y}_K
```

into the factor space of essential features $`\mathcal{Y}_K`$ (with a distinguished zero element $`0 \in \mathcal{Y}_K`$), which partitions $`\mathcal{X}`$ into **three disjoint ontological regions** in the sense of Brusentsov's three-valued logic:

```math
\mathcal{X} = \mathcal{R}_K^0 \;\sqcup\; \mathcal{R}_K^+ \;\sqcup\; \mathcal{R}_K^\perp
```

1. **Insignificance kernel (`OMIT` region, status $`0`$):**
   ```math
   \mathcal{R}_K^0 := \ker \pi_K = \{x \in \mathcal{X} \mid \pi_K(x) = 0\}.
   ```
   $`\ker \pi_K`$ contains all transitions invariant or inapplicable with respect to the law $`K`$: non-activated operators ($`a_k = 0`$), contexts blocked by an external obstacle ($`c_k = 0`$), changes of subsystems orthogonal to the law, and the sub-threshold neutral fluctuations $`\Omega_{\mathrm{sub},K}`$ explicitly declared in the contract.
2. **Target cone of following (`FOLLOW` region, status $`+1`$):**
   ```math
   \mathcal{R}_K^+ := \{x \in \mathcal{X} \setminus \ker \pi_K \mid \pi_K(x) \in C_K^+\},
   ```
   where $`\emptyset \neq C_K^+ \subsetneq \mathcal{Y}_K \setminus \{0\}`$ is a non-empty, non-universal target cone (the admissible set of productive shift) satisfying the Carroll–Brusentsov non-triviality axioms ($`x_1`$ and $`y'_1`$).
3. **Incompatibility / nullification region (`NULL` region, status $`-1`$):**
   ```math
   \mathcal{R}_K^\perp := \mathcal{X} \setminus (\mathcal{R}_K^0 \cup \mathcal{R}_K^+) = \{x \in \mathcal{X} \setminus \ker \pi_K \mid \pi_K(x) \notin C_K^+\}.
   ```
   This region collects all out-of-kernel transitions that violate the contract: sign inversion along active axes, leakage into invariant subspaces, destruction of the target object, exit beyond the contract, and unexplained stagnation on a confirmed law.

*Special case (a pure conservation invariant $`e \in E_{\mathrm{inv}}`$):* for a condition that only requires keeping the state inside an admissible tube, with no active shift, the kernel is empty ($`\mathcal{R}_K^0 = \emptyset`$), and the space splits into the admissible conservation tube $`\mathcal{R}_K^+`$ and the invariant-breakdown region $`\mathcal{R}_K^\perp`$.

### **Definition 1.2 (Observation Confidence Ball $`\mathcal{B}_t`$)**

In a real control loop or physical measurement, the transition on the window $`\tau_w`$ is observed with finite resolution and is represented not by a point but by a **non-empty compact confidence set (ellipsoid/ball) $`\mathcal{B}_t \subseteq \mathcal{X}`$**:

- Under exact deterministic observation, $`\mathcal{B}_t = \{x_t\}`$ collapses to a point.
- Under finite sensor or tracking noise with covariance $`\Sigma_{\mathrm{epi}}`$ and threshold $`\gamma_{\mathrm{snr}} > 0`$, the set is the Mahalanobis ellipsoid $`\mathcal{B}_t = \{x : \Vert{}x - \hat{x}_t\Vert{}_{\Sigma_{\mathrm{epi}}^{-1}} \le \gamma_{\mathrm{snr}}\}`$ (its certified construction is Spectral §3.4).
- In the absence of an authoritative observation (`PREDICTIVE_ONLY`, `NOT_AVAILABLE`), on tracking loss (`Rel = 0`), or without a valid certificate, the ball inflates to the whole space: $`\mathcal{B}_t = \mathcal{X}`$.

---

## **2. The Four-Verdict Theorem (`V_4`)**

### **Theorem 2.1 (Topological Generation of `V_4` from the Three-Valued Ontology)** `[Status: FOLLOW]`

Let $`\mathcal{X} = \mathcal{R}_K^0 \sqcup \mathcal{R}_K^+ \sqcup \mathcal{R}_K^\perp`$ be the three-valued ontological partition of a contract $`K`$, and let $`\mathcal{B}_t \subseteq \mathcal{X}`$ be a non-empty observation confidence set. Then the following four conditions are pairwise incompatible, exhaust all possible configurations of $`\mathcal{B}_t`$, and define the verdict in $`V_4 = \{\mathrm{FOLLOW}, \mathrm{OMIT}, \mathrm{NULL}, \mathrm{UNDECIDED}\}`$ by a total, deterministic, single-valued map:

```math
\mathrm{Verdict}_K(\mathcal{B}_t) = \begin{cases}
\mathbf{OMIT}\ (0), & \text{if } \mathcal{B}_t \subseteq \mathcal{R}_K^0 \quad \Longleftrightarrow \quad \pi_K(\mathcal{B}_t) = \{0\}, \\[6pt]
\mathbf{FOLLOW}\ (+1), & \text{if } \mathcal{B}_t \subseteq \mathcal{R}_K^+ \quad \Longleftrightarrow \quad \pi_K(\mathcal{B}_t) \subseteq C_K^+, \\[6pt]
\mathbf{NULL}\ (-1), & \text{if } \mathcal{B}_t \subseteq \mathcal{R}_K^\perp \quad \Longleftrightarrow \quad \pi_K(\mathcal{B}_t) \cap (C_K^+ \cup \{0\}) = \emptyset, \\[6pt]
\mathbf{UNDECIDED}\ (U), & \text{otherwise } \bigl(\exists u \neq v \in \{0, +, \perp\}: \; \mathcal{B}_t \cap \mathcal{R}_K^u \neq \emptyset \;\land\; \mathcal{B}_t \cap \mathcal{R}_K^v \neq \emptyset\bigr).
\end{cases}
```

*Proof.* Since $`\mathcal{R}_K^0, \mathcal{R}_K^+, \mathcal{R}_K^\perp`$ are pairwise disjoint and cover $`\mathcal{X}`$, any non-empty subset $`\mathcal{B}_t \subseteq \mathcal{X}`$ is either entirely contained in exactly one of the three regions (the first three branches, pairwise incompatible because $`\mathcal{B}_t \neq \emptyset`$), or has a non-empty intersection with at least two distinct regions (the fourth branch). Hence the map is total, deterministic, and single-valued. `∎`

*Remark.* The classification is a surjection onto $`V_4`$ (many configurations map to one verdict), not a bijection; uniqueness is per configuration, not per verdict.

### **Corollary 2.1 (The Nature of `UNDECIDED`)**

`UNDECIDED` ($`U`$) is not a fourth ontological truth value. It is the geometric indicator that **the confidence ball intersects the boundary between ontological regions** — equivalently, that the distance from the ball center to the region boundary does not exceed the ball radius. Resolution of `UNDECIDED` is possible by exactly two routes:
1. **Shrinking the ball $`\mathcal{B}_t`$** (additional measurement / probing / improved tracking precision / a certified narrowing event, Proposition 2.2).
2. **Changing the coarse-graining scale $`\ell \to \ell'`$** (expanding the kernel $`\ker \pi_K`$ so that it absorbs the boundary fluctuations — admissible only under the scale-compatibility condition $`\ker \pi_K \subseteq \ker \pi_{K'}`$, Spectral Prop 2.1, and the re-verification protocol of MBEL §5.4).

### **Corollary 2.2 (Geometric Nature of the Three `OMIT` Subtypes: stratified kernel)**

When $`\pi_K(\mathcal{B}_t) = \{0\}`$ (`OMIT`), the operational subtype is determined by the position of $`\mathcal{B}_t`$ within the **clause-stratified** kernel — the stratification inherited from the contract's MDNF coordinates (active clause $`a_k`$, context $`c_k`$, identity of the zero shift), which is part of the contract data. Position inside an unstratified kernel does **not** by itself separate the subtypes:

- **`OMIT_REDUNDANT`:** $`\mathcal{B}_t = \{0_{\mathcal{X}}\}`$ — the zero shift in the whole state space (the identity transition $`H_{t+1} = H_t`$).
- **`OMIT_BLOCKED`:** $`\mathcal{B}_t`$ lies in the stratum of $`\ker \pi_K`$ cut out by $`a_k = 1, c_k = 0`$ — the active operator was invoked but met the boundary of the admissible region (soft stop without invariant breach).
- **`OMIT_INCIDENTAL`:** $`\mathcal{B}_t \subseteq \ker \pi_K \setminus \{0_{\mathcal{X}}\}`$ within the stratum $`a_k = 0`$ or the declared sub-threshold zone $`\Omega_{\mathrm{sub},K}`$ — real motion occurred in the system, orthogonal to the given law $`K`$ (internal circulation within the kernel, or the work of another operator).

The reading reproduces the disjoint taxonomy and the controller priority of MBEL §5.2 (`OMIT_BLOCKED` first, then unchanged-descriptor `OMIT_REDUNDANT`, then `OMIT_INCIDENTAL`); the priority is a property of the stratification labels, not of the metric position.

### **Proposition 2.2 (Refinement Monotonicity; Stability of Decided Verdicts)** `[Status: FOLLOW]`

Let $`\varnothing \neq \mathcal{B}' \subseteq \mathcal{B}`$ be two confidence sets of the same contract $`K`$ (a refinement / certified narrowing). Then:
1. If $`\mathrm{Verdict}_K(\mathcal{B}) \in \{\mathrm{FOLLOW}, \mathrm{OMIT}, \mathrm{NULL}\}`$, then $`\mathrm{Verdict}_K(\mathcal{B}') = \mathrm{Verdict}_K(\mathcal{B})`$: a decided verdict is preserved under any narrowing.
2. If $`\mathrm{Verdict}_K(\mathcal{B}) = \mathrm{UNDECIDED}`$, then $`\mathrm{Verdict}_K(\mathcal{B}')`$ may be any of the four verdicts. Conversely, a decided verdict can return to `UNDECIDED` only by ball inflation or by a change of the regions (contract/scale revision) — never by narrowing.

*Proof.* (1) $`\mathcal{B} \subseteq \mathcal{R}`$ implies $`\mathcal{B}' \subseteq \mathcal{R}`$ for each region $`\mathcal{R} \in \{\mathcal{R}_K^0, \mathcal{R}_K^+, \mathcal{R}_K^\perp\}`$. (2) A straddling ball narrows either into one region (decision) or remains straddling. `∎`

### **Corollary 2.3 (Geometric Form of Certified Resolution and Non-Promotion)**

In MBEL, evidence arrives as typed certificates (§5.3) and resolution is governed by the two-phase protocol (§5.4). Their geometric reading:

1. **Certified narrowing:** an authoritative certificate for a scope-`OBSERVED` transition replaces $`\mathcal{B}_t`$ by $`\mathcal{B}_t \cap Z_{\mathcal{C}}`$, where $`Z_{\mathcal{C}}`$ is the certificate's admissible set. A `NULL` certificate with $`\mathcal{B}_t \cap Z_{\mathcal{C}} \subseteq \mathcal{R}_K^\perp`$ decides the verdict even when the prior ball straddled — this is the asymmetry of authoritative refutation: `NULL` is decidable from partial evidence, `FOLLOW` is not (it requires the whole ball inside the cone).
2. **Non-promotion / non-demotion (MBEL §5.4):** once a verdict is decided on a certified narrowing, Proposition 2.2 makes it stable under all further narrowings; re-deciding requires new authoritative evidence or an explicit contract/scale revision with re-verification. In particular, an `UNDECIDED` recorded at budget exhaustion is **never** overwritten to `NULL` afterwards: exhaustion stops the narrowing, and a straddling ball remains straddling.

---

## **3. Composition, Scale, and Inter-Agent Stitching**

### **3.1. Linear Dominance Semilattice and Cumulative Aggregation**

Under the simultaneous verification of an ensemble of contracts $`\{K_1, \dots, K_M\}`$, the base verdicts are ordered by the strict linear dominance chain:

```math
\mathrm{NULL}\ (-1) \;\succ_V\; \mathrm{UNDECIDED}\ (U) \;\succ_V\; \mathrm{OMIT}\ (0) \;\succ_V\; \mathrm{FOLLOW}\ (+1), \qquad u \otimes v := \max_{\succ_V}(u, v).
```

On the four-dimensional simplex of soft weights $`\mathbf{p} = (p^{(+)}, p^{(0)}, p^{(U)}, p^{(-)})^\top \in \Delta^3`$, the bijection to cumulative severity coordinates

```math
\Phi_{\mathrm{cum}}(\mathbf{p}) = \mathbf{q} := \begin{bmatrix} p^{(-)} \\ p^{(-)} + p^{(U)} \\ p^{(-)} + p^{(U)} + p^{(0)} \end{bmatrix} \in \mathcal{Q} = \{0 \le q_1 \le q_2 \le q_3 \le 1\}
```

turns the operation $`\otimes`$ into the coordinatewise maximum $`\bigl(\bigvee_m \mathbf{q}_m\bigr)_j = \max_m q_{m,j}`$, and its smooth relaxation at temperature $`T > 0`$ into the **padding-invariant shifted operator**:

```math
\mathrm{sLSE}_T(q_{1,j}, \dots, q_{M,j}) := \min\Bigl\{1, \; T \ln\Bigl(1 + \sum_{m=1}^M \bigl(e^{q_{m,j}/T} - 1\bigr)\Bigr)\Bigl\}.
```

Properties of the operator (proved in *Spectral and Matrix Realization of `V_4`*, Thm 5.1–5.2; imported here without change):
1. **Inertia of `FOLLOW`:** any satisfied contract ($`\mathbf{q}_m = (0,0,0)^\top`$) contributes $`e^0 - 1 = 0`$ and does not distort the sum for any $`M`$.
2. **Absorption of `NULL`:** a single reliable `NULL` ($`\mathbf{q}_m = (1,1,1)^\top`$) yields the exact output $`\mathbf{e}_{(-)}`$ at any temperature $`T > 0`$.
3. **Vacuous-truth guard (MBEL Axiom 4.1):** multiplying by the activity guard $`\mathbf{p}_{\mathrm{prog}}(E)`$ ($`\mathbf{e}_{(0)}`$ when $`E_{\mathrm{act}} = \emptyset`$ and $`\mathbf{e}_{(+)}`$ when $`E_{\mathrm{act}} \neq \emptyset`$) guarantees that a step with no active goals never receives `FOLLOW`.

### **3.2. Kernel Inclusion and the Interface Saturation Threshold**

Let two subsystems (or two description scales) be coupled through an interface $`\partial A`$ with internal projector $`\pi_{\mathrm{int}}`$ and external projector $`\pi_{\mathrm{ext}}`$, and let the internal dynamics contract phase volume transversely to the attractor at rate $`\kappa(A) = \sum_{\lambda_i < 0}\vert{}\lambda_i\vert{}`$ while generating the expansion rate $`h_+(A) = \sum_{\lambda_i > 0}\lambda_i`$ (the Pesin expansion rate; it equals the Kolmogorov–Sinai entropy rate under SRB-type measures and is only an upper bound in general — Ruelle's inequality; notation follows CPP v4.0 §4.2).

**1. Kernel-inclusion condition (structural completeness of the boundary).** `[Status: FOLLOW as the per-layer definitions; the cross-layer unification is a homology claim, UNDECIDED]`

```math
\ker \pi_{\mathrm{int}} \subseteq \ker \pi_{\mathrm{ext}}.
```

The internal projection must not discard into `OMIT` ($`\ker \pi_{\mathrm{int}}`$) those boundary distinctions that for the external environment lie in `FOLLOW` or `NULL` ($`\mathcal{X} \setminus \ker \pi_{\mathrm{ext}}`$). Violation of the inclusion produces irreducible model blindness at any observation time. The same inclusion form appears in three corpus layers with **three different mathematical species of kernel**:

| Layer | Kernel species | Inclusion statement | Source |
|---|---|---|---|
| Coarse-graining of descriptions | tangent distribution $`\ker d\pi_\ell`$ | $`K_z^{(\ell)} \subseteq K_z^{(\ell')}`$ for $`\pi_{\ell'} = f \circ \pi_\ell`$ | Spectral Prop 2.1; CPP v4.0 §3.1-context |
| Gaussian boundary coupling | precision block $`\ker \Pi_{\mathcal{I}b}`$ | $`\ker \Pi_{\mathcal{I}b} \subseteq \ker \Pi_{\mathcal{E}b}`$ ⟺ existence of the synchronization map $`\sigma`$ | CPP v4.0 Prop 2.2, Cor 2.3; LAF §8.3a |
| Verdict contracts | logical insignificance $`\ker \pi_K`$ | this section | MBEL §5.1 (equivalence kernels) |

The three are **analogous in form, not identical in kind**: the unification is a programmatic homology (the corpus-wide caveat "homology, not identity"), and no transport functor between the species is constructed. Status of the unification thesis: `UNDECIDED` (Registry row 7 below).

**2. Channel non-saturation criterion (boundary throughput).** `[Status: UNDECIDED — physical reading; CPP v4.0 Registry row 12 (Hypothesis H-L)]`

```math
\eta_{\mathrm{sat}}(A) := \frac{\dot{I}_{\mathrm{erase}}^{\mathrm{net}}(\mathcal{I}_A \to \partial^+ A)}{C_{\max}(\partial^+ A)} = \frac{\kappa(A) - h_+(A)}{\ln 2 \cdot C_{\max}(\partial^+ A)}.
```

- **What is FOLLOW here:** regardless of any threshold reading, the recoverability bound of CPP v4.0 Prop 2.1 limits whatever an external observer can reconstruct through $`\partial^+ A`$ by the prior plus $`n\,C(\partial^+ A)`$ bits — a data-processing inequality, exact under its stated assumptions.
- **What is UNDECIDED:** the *physical* reading of $`\eta_{\mathrm{sat}}`$ (an erasure flux into a thermal reservoir at temperature $`T`$, a per-edge capacity $`c_0`$) requires entities external to the discrete model — this is Hypothesis H-L of CPP v4.0 (Registry row 12). The claim that at $`\eta_{\mathrm{sat}} \ge 1`$ the inclusion condition "breaks" and deep bulk modes are permanently screened (an information horizon) belongs to the continuum narrative that CPP v4.0 moved to `OMIT` (Registry row 17); at the discrete layer it remains an untested hypothesis, not an operative criterion.
- **What is not proved at all (recorded honestly):** the synthesis "internal `OMIT`-states unfold across the boundary into a temporal chain of generalized coordinates $`\tilde{s}_t = (s_t^{(0)}, \dots, s_t^{(n)})`$ and admit synchronization in finite time under $`\eta_{\mathrm{sat}} < 1`$ plus inclusion" composes CPP v4.0 Prop 5.1 (rational-spectrum realization) with Props 2.1–2.2 (bounds and inclusion). The composition itself has no proof; status `UNDECIDED`, tested indirectly by Protocols V2/V7 of CPP v4.0.

---

## **4. Explicit Non-Claims**

1. The theorem fixes the formal geometry of verification and coarse-graining; it does **not** replace the empirical calibration of the metric $`\Sigma_{\mathrm{epi}}`$ and of the cone thresholds $`C_K^+`$ in a concrete domain.
2. The smooth aggregation $`\mathrm{sLSE}_T`$ is a surrogate for training and ranking; fact writes to memory occur only on the crisp verdict ($`\mathrm{Verdict}_K(\mathcal{B}_t)`$ at $`T \to 0^+`$).
3. This document does **not** replace the MBEL decision cascade, its certificate typing, or its ensemble law quantifiers; §0.2 fixes the authority boundary, §6 fixes the correspondence.
4. The cross-layer kernel-inclusion unification (§3.2) is a homology of forms, not an identity of mathematical objects.
5. The saturation-threshold semantics and everything downstream of it (horizons, finite-time synchronization) carry `UNDECIDED` status and must not be cited as established.

---

## **5. Self-Assessment Under the Ternary Standard**

| № | Claim of this document | $`V_4`$ status | Basis |
| :--- | :--- | :--- | :--- |
| 1 | The contract partition $`\mathcal{X} = \mathcal{R}_K^0 \sqcup \mathcal{R}_K^+ \sqcup \mathcal{R}_K^\perp`$ (Definition 1.1) and the confidence-ball states (Definition 1.2) | **`FOLLOW`** | Definitions; consistency with MBEL §5.1–§5.2 via §6 |
| 2 | Four-verdict theorem: totality, determinism, single-valuedness, pairwise incompatibility (Theorem 2.1) | **`FOLLOW`** | Set-theoretic trichotomy of a partition (two-line proof) |
| 3 | `UNDECIDED` as boundary intersection; resolution only by shrinking or kernel expansion (Corollary 2.1) | **`FOLLOW`** | Restatement of Theorem 2.1's fourth branch |
| 4 | `OMIT` subtypes as strata of the clause-stratified kernel (Corollary 2.2) | **`FOLLOW`** as a definition reading; faithful to MBEL §5.2 priority via the stratification labels | Position in an unstratified kernel is insufficient — stated explicitly |
| 5 | Refinement monotonicity; decided verdicts are stable under narrowing (Proposition 2.2) | **`FOLLOW`** | Subset transitivity |
| 6 | Certified narrowing and the geometric non-promotion rule (Corollary 2.3) | **`FOLLOW`** as the reading; the underlying protocol is MBEL §5.3–§5.4 | Mapping, not redefinition (§0.3) |
| 7 | Semilattice and $`\mathrm{sLSE}_T`$ properties (§3.1) | **`FOLLOW`** | Imported verbatim: Spectral Thm 5.1–5.2 |
| 8 | Kernel inclusion as the cross-layer preservation form (§3.2.1); unification of the three kernel species (tangent, precision-block, logical) | **`FOLLOW`** per layer (Spectral Prop 2.1; CPP v4.0 Prop 2.2/Cor 2.3; MBEL §5.1); **`UNDECIDED`** as a unification thesis | Homology of forms; no transport functor constructed |
| 9 | Saturation criterion $`\eta_{\mathrm{sat}}`$, horizon screening, finite-time boundary synchronization of unfolded `OMIT`-states (§3.2.2) | **`UNDECIDED`** | CPP v4.0 Registry rows 12 (H-L) and 17 (`OMIT` continuum); the composition is unproved |
| 10 | Claim that this geometry *replaces* the full MBEL cascade (certificates, ensemble laws, two-phase commit) | **`OMIT`** | Outside the declared scope (§0.2); the point/ball layer only |

---

## **6. Correspondence: MBEL Constructs ↔ Geometric Core**

| MBEL / corpus construct | Geometric counterpart in this document |
|---|---|
| MDNF constituent $`acy^+`$ (productive shift under active clause and context) | $`\pi_K(x) \in C_K^+`$ (interior of the target cone) |
| MDNF constituent $`ac'y^{\sim}`$ (indifference / inactive context) | $`x \in \ker \pi_K`$ (corresponding kernel stratum) |
| MDNF constituent $`ac'y^{\perp}`$ (incompatibility), authoritative | $`x \in \mathcal{R}_K^\perp`$ |
| Axiom 4.1 (prohibition of vacuous truth) | activity guard $`\mathbf{p}_{\mathrm{prog}}(E)`$ in the aggregate (§3.1, property 3) |
| Evidence scope `OBSERVED_TRANSITION` | narrowed ball: certified $`\mathcal{B}_t`$ of small radius |
| Evidence scopes `PREDICTIVE_ONLY` / `NOT_AVAILABLE`; `Rel = 0` | $`\mathcal{B}_t = \mathcal{X}`$ (maximal `UNDECIDED`) |
| Typed certificate (§5.3) | certified narrowing event $`\mathcal{B}_t \mapsto \mathcal{B}_t \cap Z_{\mathcal{C}}`$ (Corollary 2.3) |
| Epistemic `UNDECIDED` | ball straddling two or more regions |
| Decision cascade (§4.3) | any evaluation order of region-membership for the narrowed ball; equivalent by Theorem 2.1 + Proposition 2.2 |
| Non-promotion rule (§5.4) | stability of decided verdicts under narrowing (Corollary 2.3, item 2) |
| `OMIT` subtype taxonomy (§5.2) | kernel strata with controller priority (Corollary 2.2) |
| Scale change / re-verification | kernel expansion $`\ker \pi_K \subseteq \ker \pi_{K'}`$ under factorization (Spectral Prop 2.1) |
| Ensemble law quantifiers (§3.4, Thm 3.1) | **out of scope** (§0.2); point-layer aggregation only via $`\Phi_{\mathrm{cum}}`$/$`\mathrm{sLSE}_T`$ |

---

*End of document. Version 1.0. Feedback and objections — via repository issues.*
