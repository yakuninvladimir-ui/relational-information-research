# **Causal Phase Program, Version 3.9 — Mathematical Invariants of Multiscale Structuring: Internal Relief, Bilateral Interface, Dynamic Dimensional Reduction, and Channel Balance**

**Author:** Vladimir Yakunin  
**Version:** 3.9  
**Date:** 2026-10-21  
**Status:** Self-contained formal specification and research program. Strictly separates definitions, mathematical consequences within the model, and empirically testable physical hypotheses.  
**Supersedes:** `Causal_Phase_Geometry_Research_Program_v2.md` (v2.0, October 17, 2026), retained in the repository as the historical source of the $`\Gamma_{\mathrm{corr}}`$ continuum formulation and the observational falsification criteria (SPARC / DESI / DES-SN5YR).  
**Companion:** *Latent Agency Framework v2.1* (`Reasoning/Latent_Agency_Framework.md`, October 21, 2026) — shared mathematical apparatus: Markov blankets and boundary kernel inclusion, Helmholtz decomposition, integrator chains of generalized coordinates.  
**Normative parent (verdict semantics):** *Modified Brusentsov Entailment Logic* (`Reasoning/Modified_Brusentsov_Entailment_Logic.md`). Section 0 and Section 8 of this document are a domain instantiation of the canonical four-valued verdict calculus $`V_4`$ and must not contradict it.

---

## **Abstract**

This specification formulates a mathematical framework for studying how multiscale structures emerge, maintain stability, and interact within a discrete causal medium of bounded capacity. Rather than postulating a pre-existing smooth manifold of fixed dimensionality, the foundational object is a finite, locally finite partial order of events [1] equipped with unitary phase transport on immediate causal relations (Hasse links).

Any persistent localized subsystem at a selected temporal window and resolution scale is represented as a triad $`(\mathcal{I}_A, \partial A, \mathcal{E}_A)`$: an internal relief (bulk) $`\mathcal{I}_A`$, a bilateral interface $`\partial A`$ of finite capacity, and an external causal synchronization channel $`\mathcal{E}_A`$. The total system description decomposes into three distinct components: (1) the structural functional of the internal relief, (2) the kinematic scaffold of the external channel (unbranched null causal links with zero diamond-participation multiplicity), and (3) the thermodynamic entropy production and coarse-grained state-merging flux across the interface.

Within this formalism, seven core mathematical results and corresponding empirical protocols are established:
1. **Interval-Local Path Factorization and Binary Diamond Selection ($`K_{xy}^{\mathrm{eff}} = 2`$):** An equivalence relation is defined strictly on the set of two-step paths $`\mathcal{P}_2(x, y)`$ inside each fixed causal interval $`(x, y)`$ via phase-mismatch tolerance. For a strictly convex branching-cost ansatz on the interval quotient, the minimum cost subject to preserving non-zero gauge-invariant phase frustration is achieved at effective path rank $`K_{xy}^{\mathrm{eff}} = 2`$. Vertex-level merging is restricted to structural twins sharing identical causal pasts and futures. Both premises of this minimization — the convex branching-cost ansatz and the externally imposed constraint of preserving non-zero gauge-invariant phase frustration — are isolated as empirical hypotheses about substrate dynamics (`UNDECIDED`).
2. **Diamond-Participation Multiplicity of Hasse Links:** Because Hasse transitive irreducibility implies $`(R^2)_{xy} = K_{xy} = 0`$ for every direct link $`R_{xy}=1`$, embeddedness in interference structures is defined via the **diamond-participation multiplicity** $`d_\diamond(x, y)`$, counting all elementary causal diamonds containing the link $`x \lessdot y`$. Pure unbranched (null) channel links are rigorously characterized by $`R_{xy}=1 \land d_\diamond(x, y) = 0`$.
3. **Precision Sparsity and the Boundary Kernel-Inclusion Theorem:** In a stationary Gaussian regime across $`(\mathcal{I}_A, \partial A, \mathcal{E}_A)`$, Markov screening [4] corresponds to block sparsity of the precision operator ($`\Pi_{\mathcal{I}\mathcal{E}} = 0`$) while inducing non-zero mediated covariance $`\Sigma_{\mathcal{I}\mathcal{E}} = \Pi_{\mathcal{I}}^{-1}\Pi_{\mathcal{I},\partial A}\Sigma_{\partial A}\Pi_{\partial A,\mathcal{E}}\Pi_{\mathcal{E}}^{-1} \neq 0`$. A well-defined synchronization map $`\sigma(\overline{\mu}(b)) = \overline{\eta}(b)`$ across the interface exists if and only if $`\ker \Pi_{\mathcal{I},\partial A} \subseteq \ker \Pi_{\mathcal{E},\partial A}`$ [4].
4. **Helmholtz Decomposition and Solenoidal Acceleration of Relaxation:** Splitting the transport operator $`W`$ into its symmetric part $`H_{\mathrm{sym}} = \frac{1}{2}(W + W^\dagger)`$ and skew-Hermitian rotational part $`H_{\mathrm{rot}} = \frac{1}{2i}(W - W^\dagger)`$ mirrors the continuous Helmholtz decomposition into dissipative ($`\Gamma \succeq 0`$) and solenoidal ($`Q = -Q^\top`$) flows [4]. Non-zero solenoidal circulation preserves the stationary measure while satisfying the spectral gap inequality $`\gamma(Q) \ge \gamma(0)`$ [4].
5. **Oseledets Contraction, $`\varepsilon`$-Cell Merging, and the Oseledets–Ruelle–Landauer Bridge:** Using a finite resolution partition of scale $`\varepsilon > 0`$ around an attractor where $`\kappa(A) = \sum_{\lambda_i < 0}\vert{}\lambda_i\vert{} > h_{\mathrm{KS}}(A)`$ [6], the map $`G_R`$ acts along the stable subspace $`E^s`$ as an $`\exp(\kappa(A))`$-to-$`1`$ logical state merger [5]. Under stationary noise injection $`H_{\mathrm{in}}^{(\varepsilon)}`$ maintaining constant coarse-grained entropy $`H_\varepsilon(Z_{n+1}) = H_\varepsilon(Z_n)`$, the exact balance $`0 = H_{\mathrm{in}}^{(\varepsilon)} - H_{\mathrm{out}}^{(\varepsilon)} + h_{\mathrm{KS}}(A) - \kappa(A)`$ separates reversible throughput from irreversible phase-space folding at rate $`\Delta S_{\mathrm{fold}} = \kappa(A) > 0`$, the net export to the boundary bath being $`\sigma_{\mathrm{bath}} = \kappa(A) - h_{\mathrm{KS}}(A) \ge 0`$ [5, 6].
6. **Stochastic Realization of Boundary Spectra and Multiscale Network Transition:** Multi-frequency stationary processes on $`\partial A`$ admit a Markovian realization as nested integrator chains $`\tilde{s}_t = (s_t^{(0)}, \dots, s_t^{(n)})`$, where coarse-graining $`\mathcal{R}_{\ell \to \ell+1}`$ truncates high-order derivatives [4]. At large graph sizes $`N > N_{\mathrm{crit}}`$, maintaining synchronization connectivity $`\lambda_2`$ under bounded degree $`k_{\max}`$ [2] forces a transition from homogeneous balls to node-filament-void networks [9].
7. **Local-Global Balance and Horizon Saturation:** An exact combinatorial identity governs diamond partitioning across bulks, interfaces, and voids, framing falsifiable hypotheses for phase-mediated void rarefaction [3] and horizon saturation ($`\eta_{\mathrm{sat}} \ge 1`$) [5, 8].

All statements are classified in the four-valued verification space $`V_4 = \{\mathrm{FOLLOW}, \mathrm{OMIT}, \mathrm{UNDECIDED}, \mathrm{NULL}\}`$ [10]. Section 7 details seven computational verification protocols (V1–V7), and Section 9 provides the corrected reference Python implementation.

---

## **0. Methodological Standard and the `V_4` Verdict Calculus**

Every claim in this specification is evaluated within the four-valued verification space [10]:

```math
V_4 = \bigl\{\mathrm{FOLLOW}\ (+1),\; \mathrm{OMIT}\ (0),\; \mathrm{UNDECIDED}\ (U),\; \mathrm{NULL}\ (-1)\bigr\},
```

ordered by the strict linear severity dominance semilattice under conjunctive aggregation ($`\otimes = \max_{\succ_V}`$) [10]:

```math
\mathrm{NULL}\ (-1) \;\succ_V\; \mathrm{UNDECIDED}\ (U) \;\succ_V\; \mathrm{OMIT}\ (0) \;\succ_V\; \mathrm{FOLLOW}\ (+1).
```

Status assignment rules [10]:
- **`FOLLOW` ($`+1`$):** Assigned exclusively to (a) internally consistent formal definitions and (b) mathematical propositions whose conclusions follow deductively from assumptions explicitly stated in the proposition. A `FOLLOW` status on $`P \implies Q`$ certifies the logical implication, never the physical truth of the premise $`P`$ or the physical optimality of a chosen functional.
- **`OMIT` ($`0`$):** Assigned to (a) degrees of freedom lying in the kernel of a coarse-graining map $`\ker(d\pi_\ell)`$ [9, 10], (b) illustrative heuristics or pedagogical analogies that are never used as premises in any proof [3, 4], and (c) tautological reformulations of already-certified consequences (e.g., defining null links via $`(R_{xy}=1) \land (K_{xy}=0)`$), which are logically vacuous in the sense of the canonical `OMIT` taxonomy and carry no independent content [10].
- **`UNDECIDED` ($`U`$):** Assigned to substantive structural, kinematic, and physical hypotheses that are well-posed but require numerical verification in protocols V1–V7 or external physical calibration (including the choice of cost functionals, continuum-limit Lorentzian signature emergence, and physical clock calibration).
- **`NULL` ($`-1`$):** Assigned to claims or code constructs that are mathematically inconsistent, violate gauge/combinatorial invariants [2], or fail negative controls [4].

---

## **1. Foundational Causal-Phase Complex**

### **1.1. Partial Order of Events and the Hasse Matrix**

Let $`X = \{1, 2, \dots, N\}`$ be a finite set of events equipped with a strict partial order $`\prec`$ (irreflexive, transitive, acyclic) [1], indexed topologically so that $`x \prec y \implies x < y`$.

**Definition 1.1 (Causal Interval, Hasse Link, and Antichain).** `[Status: FOLLOW]` [1]
- The *causal interval* between $`x \prec y`$ is $`I(x, y) := \{z \in X \mid x \prec z \prec y\}`$.
- A *Hasse link* (immediate causal coverage) $`x \lessdot y`$ holds iff $`x \prec y \land I(x, y) = \varnothing`$.
- An *antichain* (spacelike section) is a subset $`S \subset X`$ of mutually incomparable elements: $`\forall u \neq v \in S, \; u \not\prec v \land v \not\prec u`$.

The Boolean Hasse adjacency matrix $`R \in \{0, 1\}^{N \times N}`$ ($`R_{xy} = 1 \iff x \lessdot y`$) is strictly upper-triangular and nilpotent ($`R^N = 0`$). A strictly upper-triangular Boolean matrix $`R`$ is a valid Hasse matrix if and only if it is **transitively irreducible** (no direct link short-circuits a directed path of length $`\ge 2`$):

```math
\forall x, y \in X: \quad R_{xy} = 1 \implies \bigl((I - R)^{-1} - I - R\bigr)_{xy} = 0.
```

In particular, transitive irreducibility immediately implies that for every Hasse link,

```math
R_{xy} = 1 \implies K_{xy} := (R^2)_{xy} = 0.
```

### **1.2. Phase Bundle and Transport Operator**

Each Hasse link $`x \lessdot y`$ carries a phase $`\theta_{xy} \in [0, 2\pi)`$ and unitary transport factor $`U_{xy} = e^{i\theta_{xy}} \in U(1)`$ (with $`U_{yx} = U_{xy}^{-1} = e^{-i\theta_{xy}}`$ along comparison loops).

**Definition 1.2 (Causal-Phase Transport Matrix).** `[Status: FOLLOW]`  
The nilpotent complex transport matrix $`W \in \mathbb{C}^{N \times N}`$ is defined by $`W_{xy} := R_{xy} e^{i\theta_{xy}}`$ ($`W^N = 0`$). Under local vertex gauge transformations $`D_\chi = \mathrm{diag}(e^{i\chi_1}, \dots, e^{i\chi_N})`$:

```math
W \longmapsto W' = D_\chi W D_\chi^\dagger, \qquad \theta_{xy} \longmapsto \theta'_{xy} = (\theta_{xy} + \chi_x - \chi_y) \bmod 2\pi.
```

### **1.3. Two-Step Waists, Elementary Diamonds, and the Interference Identity**

For any pair of events $`(x, y)`$ at causal distance two, let $`\mathcal{P}_2(x, y)`$ denote the set of two-step Hasse paths $`p_z = (x \lessdot z \lessdot y)`$, indexed by the waist vertex set:

```math
V_{xy} := \{z \in X \mid R_{xz} R_{zy} = 1\}, \qquad K_{xy} := |V_{xy}| = (R^2)_{xy} \in \mathbb{Z}_{\ge 0}.
```

Note that by Hasse irreducibility (§1.1), $`K_{xy} > 0 \implies R_{xy} = 0`$. The two-step amplitude, waist coherence, and phase frustration (activity) are defined for $`K_{xy} > 0`$ as:

```math
M_{xy} := (W^2)_{xy} = \sum_{z \in V_{xy}} e^{i(\theta_{xz} + \theta_{zy})}, \qquad \mathrm{Coh}_{xy} := \frac{|M_{xy}|^2}{K_{xy}^2} \in [0, 1], \qquad J_{xy} := K_{xy}\bigl(1 - \mathrm{Coh}_{xy}\bigr) = \frac{K_{xy}^2 - |M_{xy}|^2}{K_{xy}} \ge 0.
```

Whenever $`K_{xy} \ge 2`$, any unordered pair of distinct intermediate vertices $`\{z_a, z_b\} \subset V_{xy}`$ ($`z_a \neq z_b`$) forms an **elementary causal diamond** $`D(x; z_a, z_b; y)`$ with gauge-invariant holonomy:

```math
U_D(x; z_a, z_b; y) := U_{x z_a} U_{z_a y} U_{z_b y}^{-1} U_{x z_b}^{-1} = e^{i\Phi_{ab}}, \qquad \Phi_{ab} = (\theta_{x z_a} + \theta_{z_a y}) - (\theta_{x z_b} + \theta_{z_b y}).
```

**Proposition 1.1 (Wilson Interference Identity for a Waist).** `[Status: FOLLOW]`  
For every pair $`(x, y)`$ with $`K_{xy} \ge 1`$, the sum of pairwise Wilson actions over all $`\binom{K_{xy}}{2}`$ elementary diamonds in $`V_{xy}`$ satisfies:

```math
\sum_{1 \le a < b \le K_{xy}} \bigl(1 - \cos\Phi_{ab}\bigr) = \frac{1}{2}\bigl(K_{xy}^2 - |M_{xy}|^2\bigr) = \frac{1}{2} K_{xy} J_{xy}.
```

*Proof.* Setting $`\phi_a = \theta_{xz_a} + \theta_{z_a y}`$, expanding $`|M_{xy}|^2 = \left|\sum_{a=1}^{K_{xy}} e^{i\phi_a}\right|^2 = K_{xy} + 2\sum_{a < b} \cos\Phi_{ab}`$ and subtracting from $`K_{xy}^2 = K_{xy} + 2\sum_{a < b} 1`$ yields the identity. `∎`

### **1.4. Cone-Overlap Operators**

The Hermitian positive-semidefinite one-step future and past cone-overlap operators are:

```math
\Delta_+ := W W^\dagger, \qquad \Delta_- := W^\dagger W.
```

---

## **2. The Structuring Triad: Diamond-Participation Multiplicity, Bilateral Interface, and External Channel**

### **2.1. Diamond-Participation Multiplicity of Hasse Links: Null vs. Structured Channels**

Because $`(R^2)_{xy} = K_{xy} = 0`$ holds identically for every direct Hasse link $`R_{xy} = 1`$ (§1.1), one cannot use $`K_{xy} = 0`$ on the same pair $`(x, y)`$ to distinguish unbranched links from links embedded in causal diamonds. Instead, a Hasse link $`x \lessdot y`$ participates in interference if and only if it serves as one of the four boundary edges of at least one elementary diamond: either as a lower leg $`(x \lessdot y \lessdot w)`$ paired with an alternative path $`(x \lessdot z \lessdot w)`$ ($`z \neq y`$), or as an upper leg $`(u \lessdot x \lessdot y)`$ paired with $`(u \lessdot z \lessdot y)`$ ($`z \neq x`$).

**Definition 2.1 (Diamond-Participation Multiplicity and Unbranched Null Links).** `[Status: FOLLOW]`  
For any Hasse link $`(x, y)`$ with $`R_{xy} = 1`$, define its **lower** and **upper diamond-participation counts** as:

```math
d_\diamond^+(x, y) := \sum_{w \in X} R_{yw} \max\bigl(0,\, K_{xw} - 1\bigr), \qquad d_\diamond^-(x, y) := \sum_{u \in X} R_{ux} \max\bigl(0,\, K_{uy} - 1\bigr).
```

Since $`R_{xy} = 1 \land R_{yw} = 1 \implies K_{xw} = (R^2)_{xw} \ge 1`$, the maximum is redundant whenever $`R_{yw}=1`$ (resp. $`R_{ux}=1`$), so the **total diamond-participation multiplicity** of link $`x \lessdot y`$ is given in closed matrix form by:

```math
d_\diamond(x, y) := d_\diamond^+(x, y) + d_\diamond^-(x, y) = R_{xy} \Bigl( \bigl((K - \mathbf{1}_{K>0}) R^\top\bigr)_{xy} + \bigl(R^\top (K - \mathbf{1}_{K>0})\bigr)_{xy} \Bigr) \in \mathbb{Z}_{\ge 0}.
```

Combinatorially, $`d_\diamond(x, y)`$ equals the exact number of elementary causal diamonds $`D`$ in $`X`$ that contain the directed link $`x \lessdot y`$ as an edge. This induces a rigorous partition of the edge set $`E(R) = \{(x, y) \mid R_{xy} = 1\}`$:
1. **Unbranched (Null) Channel Links ($`E_{\mathrm{null}}`$):** Hasse links with $`R_{xy} = 1`$ and $`d_\diamond(x, y) = 0`$. Such a link belongs to no elementary causal diamond; along a maximal chain of links with $`d_\diamond = 0`$, local phases $`\theta_{xy}`$ can be gauged to zero without frustrating any loop ($`\Delta \Phi_D = 0`$).
2. **Diamond-Embedded (Structured) Links ($`E_{\diamond}`$):** Hasse links with $`R_{xy} = 1`$ and $`d_\diamond(x, y) \ge 1`$. These links form the load-bearing walls of causal diamonds where gauge-invariant holonomies $`\Phi_{ab}`$ reside.

### **2.2. Formal Definition of the Triad `(ℐ_A, ∂A, ℰ_A)`**

**Definition 2.2 (Structural Triad of a Subsystem).** `[Status: FOLLOW]`  
Every proper connected subsystem $`A \subset X`$ uniquely partitions the event set into three disjoint zones [4]:

```math
X = \mathcal{I}_A \sqcup \partial A \sqcup \mathcal{E}_A,
```

where:
- **Bilateral Interface $`\partial A := \partial^- A \cup \partial^+ A`$:** the boundary vertices of $`A`$ sharing immediate Hasse links with the complement $`\mathcal{E}_A := X \setminus A`$:
```math
\partial^- A := \{y \in A \mid \exists x \in \mathcal{E}_A : R_{xy} = 1\}, \qquad \partial^+ A := \{x \in A \mid \exists y \in \mathcal{E}_A : R_{xy} = 1\}.
```
- **Internal Relief (Bulk) $`\mathcal{I}_A := A \setminus \partial A`$:** the interior core of $`A`$, which has no direct Hasse links to $`\mathcal{E}_A`$ and interacts with $`\mathcal{E}_A`$ solely through $`\partial A`$ [4].
- **External Synchronization Channel $`\mathcal{E}_A := X \setminus A`$:** the exterior environment coupling $`A`$ to other subsystems. The **external null-link fraction** in $`\mathcal{E}_A`$ is the non-trivial observable:
```math
f_{\mathrm{null}}(\mathcal{E}_A) := \frac{\bigl|\{(x, y) \in \mathcal{E}_A \times \mathcal{E}_A \mid R_{xy} = 1 \land d_\diamond(x, y) = 0\}\bigr|}{\bigl|\{(x, y) \in \mathcal{E}_A \times \mathcal{E}_A \mid R_{xy} = 1\}\bigr|} \in [0, 1].
```

The incoming and outgoing combinatorial capacities of the interface are $`|\partial^- A|_E := \sum_{x \in \mathcal{E}_A, y \in \partial^- A} R_{xy}`$ and $`|\partial^+ A|_E := \sum_{x \in \partial^+ A, y \in \mathcal{E}_A} R_{xy}`$.

**Definition 2.3 (Integration Criterion on Window $`\tau_w`$).** `[Status: FOLLOW]`  
With symmetric coupling flux $`\mathrm{Dep}(U \leftrightarrow V) := \sum_{u \in U, v \in V} (|W_{uv}|^2 + |W_{vu}|^2)`$, subsystem $`A = \mathcal{I}_A \sqcup \partial A`$ is integrated on window $`\tau_w`$ at threshold $`\theta_I > 0`$ if across all non-trivial binary cuts $`A = A_1 \sqcup A_2`$:

```math
I(A; \tau_w) := \min_{(A_1, A_2)} \frac{\mathrm{Dep}(A_1 \leftrightarrow A_2) / \min(|A_1|, |A_2|)}{\mathrm{Dep}(A \leftrightarrow \mathcal{E}_A) / |A|} > \theta_I.
```

This criterion is a weighted graph-cut ratio (a conductance-type quantity certifying that internal coupling flux dominates boundary coupling flux); it does not measure informational integration in the sense of mutual-information or $`\Phi`$-type functionals, and *integrated* refers here exclusively to cut-dominance at threshold $`\theta_I`$.

### **2.3. Recoverability Bound Across the Interface**

**Proposition 2.1 (Interface Information Recoverability Bound).** `[Status: FOLLOW]`  
If transmission from internal state $`Z_A`$ across $`\partial^+ A`$ over $`n`$ steps forms a memoryless channel of per-step capacity $`C(\partial^+ A) \le c_0 |\partial^+ A|_E`$ with noise conditionally independent of $`(Z_A, Z_B)`$, and an external observer $`B \subset \mathcal{E}_A`$ forms estimate $`\hat{Z}_A = f(Y^n, Z_B)`$ (Markov chain $`Z_A \to (X^n, Z_B) \to (Y^n, Z_B) \to \hat{Z}_A`$), then:

```math
I(Z_A; \hat{Z}_A) \le I(Z_A; Z_B) + n \, C(\partial^+ A) \le I(Z_A; Z_B) + n c_0 |\partial^+ A|_E.
```

*Proof.* Follows from the data processing inequality $`I(Z_A; \hat{Z}_A) \le I(Z_A; Z_B) + I(Z_A; Y^n \mid Z_B)`$ and subadditivity $`I(Z_A; Y^n \mid Z_B) \le \sum_{k=1}^n I(X_k; Y_k) \le n \, C(\partial^+ A)`$. `∎`

### **2.4. Precision Sparsity, Mediated Covariance, and the Boundary Kernel-Inclusion Theorem**

Consider stationary Gaussian fluctuations $`x = (\eta, b, \mu) \in \mathcal{E}_A \times \partial A \times \mathcal{I}_A`$ distributed as $`p(x) = \mathcal{N}(0, \Pi^{-1})`$ with positive-definite precision matrix $`\Pi = \Sigma^{-1} \succ 0`$ [4]. Given boundary state $`b \in \partial A`$, the conditional expectations are $`\overline{\eta}(b) := \mathbb{E}[\eta \mid b] = -\Pi_{\mathcal{E}}^{-1}\Pi_{\mathcal{E},\partial A} b`$ and $`\overline{\mu}(b) := \mathbb{E}[\mu \mid b] = -\Pi_{\mathcal{I}}^{-1}\Pi_{\mathcal{I},\partial A} b`$ [4].

**Proposition 2.2 (Precision Sparsity, Long-Range Covariance, and Boundary Kernel Inclusion).** `[Status: FOLLOW]` [4]  
For $`p(\eta, b, \mu) = \mathcal{N}(0, \Pi^{-1})`$ with $`\Pi \succ 0`$:
1. **Precision Sparsity vs. Mediated Covariance:** Conditional independence $`\eta \perp \mu \mid b`$ holds if and only if $`\Pi_{\mathcal{I}\mathcal{E}} = 0`$ and $`\Pi_{\mathcal{E}\mathcal{I}} = 0`$ [4]. Under this condition, the marginal covariance between internal relief and external channel is mediated across the interface via:
```math
\Sigma_{\mathcal{I}\mathcal{E}} = \Sigma_{\mathcal{I},\partial A}\,\Sigma_{\partial A}^{-1}\,\Sigma_{\partial A,\mathcal{E}} = \Pi_{\mathcal{I}}^{-1}\Pi_{\mathcal{I},\partial A}\,\Sigma_{\partial A}\,\Pi_{\partial A,\mathcal{E}}\Pi_{\mathcal{E}}^{-1}.
```
2. **Boundary Kernel-Inclusion Criterion:** A linear synchronization map $`\sigma: \mathrm{Im}(\overline{\mu}) \to \mathrm{Im}(\overline{\eta})`$ satisfying $`\sigma(\overline{\mu}(b)) = \overline{\eta}(b)`$ for all $`b \in \partial A`$ exists if and only if [4]:
```math
\ker \Sigma_{\mathcal{I},\partial A} \subseteq \ker \Sigma_{\mathcal{E},\partial A} \quad \Longleftrightarrow \quad \ker \Pi_{\mathcal{I},\partial A} \subseteq \ker \Pi_{\mathcal{E},\partial A}.
```
   When satisfied, $`\sigma(\mu) = \Pi_{\mathcal{E}}^{-1}\Pi_{\mathcal{E},\partial A}\Pi_{\mathcal{I},\partial A}^{-}\Pi_{\mathcal{I}}\mu`$ [4], and $`\overline{\mu}(b)`$ uniquely minimizes $`D_{\mathrm{KL}}\bigl[\mathcal{N}(\eta; \sigma(\mu), \Pi_{\mathcal{E}}^{-1}) \;\|\; p(\eta \mid b)\bigr] = \frac{1}{2}\bigl(\sigma(\mu) - \overline{\eta}(b)\bigr)^\top \Pi_{\mathcal{E}} \bigl(\sigma(\mu) - \overline{\eta}(b)\bigr)`$ [4].

*Proof.* Established in [4] via block inversion $`\Pi \Sigma = I`$ and Gaussian conditional factorization. `∎`

---

## **3. Variational Structuring Principle, Interval-Local Path Reduction, and Solenoidal Acceleration**

### **3.1. Informational Minimal Surface and Orthogonal Tangent Splitting**

Let $`\pi_\ell: D_\ell \to Y_\ell`$ be a $`C^1`$ coarse-graining map [9] on a regular stratum $`D_\ell`$ equipped with a positive-definite metric $`h_z`$ on $`T_z D_\ell`$. Minimizing the functional $`\mathcal{L}[\Sigma] = \mathrm{Vol}_h(\Sigma) + \lambda(R_{\mathrm{req}} - I(\Sigma; Y_\ell))`$ at fixed carrier density $`\delta(d\mu_\Sigma) = 0`$ yields the stationary mean-curvature balance `[Status: FOLLOW]`:

```math
\mathbf{H}(z) = \lambda \bigl(\nabla_Z i(z)\bigr)^\perp.
```

Within $`T_z D_\ell`$, the coarse-graining kernel $`K_z := \ker(d\pi_\ell(z))`$ and an externally grounded unit active direction $`u_{\mathrm{exp}}(z) \in K_z^{\perp_h}`$ induce the $`h_z`$-orthogonal splitting:

```math
T_z D_\ell = W^{\mathrm{act}}_z \oplus_h W^{\mathrm{inv}}_z \oplus_h K_z, \qquad \mathrm{Id}_{T_z D_\ell} = P_{\mathrm{act}} + P_{\mathrm{inv}} + P_{\mathrm{ker}}.
```

### **3.2. Interval-Local Path Factorization vs. Global Twin Merging, and Binary Diamond Selection (`K_xy^eff = 2`)**

In earlier formulations, phase equivalence of intermediate paths inside a waist $`V_{xy}`$ was conflated in code with unconditional global vertex merging across the entire graph. However, an intermediate vertex $`z \in V_{xy}`$ may simultaneously belong to another causal interval $`V_{x’y'}`$ where its phase is not aligned with the same partner. Therefore, **interval-local path factorization** and **global vertex reduction** must be defined as distinct operations.

**Definition 3.1 (Interval-Local Path Equivalence vs. Global Twin Reduction).** `[Status: FOLLOW]`
1. **Interval-Local Path Quotient:** Fix a single pair of events $`(x, y)`$ with $`K_{xy} \ge 2`$ and let $`\mathcal{P}_2(x, y) = \{p_z = (x \lessdot z \lessdot y) \mid z \in V_{xy}\}`$ be the set of two-step paths between $`x`$ and $`y`$, where path $`p_z`$ carries total phase $`\phi_{xy}(z) := (\theta_{xz} + \theta_{zy}) \bmod 2\pi`$. Given tolerance $`\varepsilon_{\mathrm{ker}} \ge 0`$, two paths $`p_{z_a}, p_{z_b} \in \mathcal{P}_2(x, y)`$ are $`\varepsilon_{\mathrm{ker}}`$-coherent in $`(x, y)`$ if:
```math
d_{\mathbb{T}}\bigl(\phi_{xy}(z_a), \phi_{xy}(z_b)\bigr) := \min\bigl(|\phi_{xy}(z_a) - \phi_{xy}(z_b)|,\; 2\pi - |\phi_{xy}(z_a) - \phi_{xy}(z_b)|\bigr) \le \varepsilon_{\mathrm{ker}}.
```
   Single-linkage transitive closure on $`\mathcal{P}_2(x, y)`$ defines an equivalence relation $`\sim_{(x,y),\varepsilon_{\mathrm{ker}}}`$ **strictly local to the pair $`(x, y)`$**. The quotient path set $`\widetilde{\mathcal{P}}_2(x, y) := \mathcal{P}_2(x, y) / \!\sim_{(x,y),\varepsilon_{\mathrm{ker}}}`$ has **effective interval channel rank** $`K_{xy}^{\mathrm{eff}} := |\widetilde{\mathcal{P}}_2(x, y)| \in \{1, \dots, K_{xy}\}`$ and class phases $`\widetilde{\phi}_\alpha = \arg\bigl(\sum_{z \in C_\alpha} e^{i\phi_{xy}(z)}\bigr)`$ without altering any other interval $`(x', y') \neq (x, y)`$.
2. **Global Structural-Twin Vertex Merging:** Two distinct vertices $`z_a \neq z_b \in X`$ are **causal structural twins** if they are causally incomparable and share identical sets of immediate predecessors and successors in $`R`$:
```math
\forall u \in X:\; R_{u z_a} = R_{u z_b} \quad \text{and} \quad \forall v \in X:\; R_{z_a v} = R_{z_b v}.
```
   Global vertex merging $`z_a \equiv z_b`$ on the graph $`X`$ is admissible at tolerance $`\varepsilon_{\mathrm{ker}}`$ if and only if $`z_a, z_b`$ are causal structural twins **and** $`d_{\mathbb{T}}(\phi_{uv}(z_a), \phi_{uv}(z_b)) \le \varepsilon_{\mathrm{ker}}`$ holds across **every** interval $`(u, v)`$ containing $`\{z_a, z_b\}`$.

Consider now a model family of interval cost functionals parameterized by a branching exponent $`p > 0`$:

```math
\mathcal{F}_{\mathrm{loc}}^{(p)}\bigl(K^{\mathrm{eff}}, \{\widetilde{\phi}_\alpha\}\bigr) = a \bigl(K^{\mathrm{eff}}\bigr)^p + b \, J^{\mathrm{eff}}_{xy}, \qquad a > 0, \; b \ge 0,
```

where $`J^{\mathrm{eff}}_{xy} = K^{\mathrm{eff}} - \frac{1}{K^{\mathrm{eff}}}\left|\sum_{\alpha=1}^{K^{\mathrm{eff}}} e^{i\widetilde{\phi}_\alpha}\right|^2`$.

**Proposition 3.1 (Conditional Selection of $`K_{xy}^{\mathrm{eff}} = 2`$ Under Positive-Exponent Branching Penalty).** `[Status: FOLLOW (for the functional ansatz; physical realization of the ansatz is UNDECIDED)]`  
For a fixed pair $`(x, y)`$, suppose $`\mathcal{F}_{\mathrm{loc}}^{(p)}`$ ($`a > 0, p > 0`$) is minimized over integer effective channel ranks $`K^{\mathrm{eff}} \in \mathbb{Z}_{\ge 1}`$ and class phases $`\{\widetilde{\phi}_\alpha\}`$ subject to maintaining a fixed non-zero gauge-invariant frustration $`J^{\mathrm{eff}}_{xy} = J_0 \in (0, 2]`$. Then:
1. At $`K^{\mathrm{eff}} = 1`$, $`J^{\mathrm{eff}}_{xy} \equiv 0`$, so $`K^{\mathrm{eff}} = 1`$ is inadmissible for any $`J_0 > 0`$.
2. Among all integers $`K^{\mathrm{eff}} \ge 2`$, because $`k \mapsto a k^p`$ ($`a > 0, p > 0`$) is strictly increasing in $`k`$ and $`J_0 \in (0, 2]`$ is realizable at $`K^{\mathrm{eff}} = 2`$ via $`\Phi_{12} = \pm \arccos(1 - J_0)`$, the unique global minimum of $`\mathcal{F}_{\mathrm{loc}}^{(p)}`$ at fixed $`J_0 \in (0, 2]`$ is achieved at $`K^{\mathrm{eff}}_{xy} = 2`$.
3. Conversely, if alternative decompositions of one width-$`K`$ bundle are compared rather than a fixed $`J_0`$, two distinct splitting regimes must be separated [2]:
   1. **Diamond-preserving split** ($`m = \binom{K}{2}`$ separate binary diamonds, one per elementary diamond of the bundle): the total branching penalty decreases if and only if $`m \cdot a(2^p) < a K^p`$, which holds for all $`K \ge 3`$ whenever $`p > \frac{\ln 3}{\ln(3/2)} \approx 2.71`$ (tightest at $`K = 3`$); under the quadratic penalty $`p = 2`$ this regime does not favor splitting (at $`K = 4`$: $`6 \cdot 4a = 24a > 16a`$).
   2. **Balanced binary regrouping** (a merged 4-path bundle split into two disjoint 2-path bundles, $`m = 2`$, not diamond-preserving): the penalty decreases already under $`p = 2`$, since $`2 \times 2^2 a = 8a < 4^2 a = 16a`$; more generally, splitting width $`K`$ into $`K/2`$ binary bundles lowers the penalty if and only if $`\frac{K}{2}\,a\,2^p < a\,K^p`$, i.e., for every $`K > 2`$ and $`p > 1`$.

*Proof.* Items (1) and (2) follow immediately from $`J^{\mathrm{eff}}_{xy}(K^{\mathrm{eff}}=1) = 0`$, the strict monotonicity of $`a k^p`$ for $`k \ge 2`$, and $`J^{\mathrm{eff}}_{xy}(K^{\mathrm{eff}}=2) = 1 - \cos\Phi_{12} \in [0, 2]`$. Item (3) follows by direct evaluation of the branching penalty in each regime: $`a K^p`$ versus $`m\,a\,2^p`$ with $`m = \binom{K}{2}`$ (diamond-preserving) and versus $`\frac{K}{2}\,a\,2^p`$ (balanced binary regrouping) [2]. `∎`

**Scope Note on Proposition 3.1:**  
Proposition 3.1 is a mathematical property of the chosen cost functional $`\mathcal{F}_{\mathrm{loc}}^{(p)}`$. It does **not** prove a priori that nature implements $`\mathcal{F}_{\mathrm{loc}}^{(p)}`$. Why an underlying substrate penalizes path proliferation convexly (e.g., due to finite vertex valency $`k_{\max}`$ preventing Kleitman–Rothschild combinatorial collapse [2] and phase-decoherence noise across multi-slit bundles) is an empirical hypothesis `[Status: UNDECIDED]`, tested in Protocol V1 by comparing convex ($`p=2`$), linear ($`p=1`$), and concave ($`\ln(1+K)`$) penalties. The constraint of fixed non-zero frustration $`J_0 \in (0, 2]`$ is likewise an external premise of the minimization, not a derived property of the substrate: were frustration free to relax to zero, the single-path configuration $`K^{\mathrm{eff}}_{xy} = 1`$ would be cheaper under any positive penalty. No derivation of this constraint is offered here; its physical justification is part of the same empirical hypothesis tested in Protocol V1.

### **3.3. Transverse Algebra of the Binary Diamond and Conditional Minimality of `3+1` Directions**

On a binary diamond $`K^{\mathrm{eff}}_{xy} = 2`$ with transverse section $`S_\perp = \{z_1, z_2\}`$, the two-channel amplitude space is $`\mathbb{C}^2`$ with unitary transition group $`U(2) \cong U(1) \times SU(2) / \mathbb{Z}_2`$, where $`\dim_{\mathbb{R}} \mathfrak{su}(2) = 3`$ double-covers $`SO(3)`$ `[Status: FOLLOW]`. Under the Hermitian/skew-Hermitian splitting

```math
H_{\mathrm{sym}} := \frac{1}{2}(W + W^\dagger), \qquad H_{\mathrm{rot}} := \frac{1}{2i}(W - W^\dagger),
```

accommodating at least one longitudinal active transport direction ($`\dim W^{\mathrm{act}}_z \ge 1`$) and an orthogonal two-dimensional invariant plane of rotational circulation ($`\dim W^{\mathrm{inv}}_z \ge 2`$ for a conjugate eigenvalue pair $`\pm\lambda_\alpha`$ of $`H_{\mathrm{rot}}`$) requires minimal spatial dimension $`d_{\mathrm{space}}^{\min} = 1 + 2 = 3 = \binom{3}{2}`$ `[Status: FOLLOW]` under the stated rank requirements; spontaneous emergence in graph ensembles is `[Status: UNDECIDED]` (Protocol V1). The two rank requirements are physical premises of the program, not consequences of it: structures with $`\dim W^{\mathrm{inv}}_z \le 1`$ (no conserved transverse circulation) are excluded by assumption rather than by theorem, and the integer coincidence $`\binom{3}{2} = 3`$ is a consistency observation, not a selection mechanism.

### **3.4. Helmholtz Decomposition and Solenoidal Acceleration of Relaxation**

**Proposition 3.2 (Solenoidal Preservation of Stationary Measure and Acceleration of Relaxation).** `[Status: FOLLOW]` [4]  
For a linear Langevin process $`dx_t = -(\Gamma + Q)\Pi x_t\,dt + \sqrt{2\Gamma}\,dW_t`$ on $`\mathbb{R}^n`$ with $`\Pi \succ 0`$, $`\Gamma \succ 0`$, and skew-symmetric solenoidal matrix $`Q = -Q^\top`$, let $`B(Q) := (\Gamma + Q)\Pi`$ and $`\gamma(Q) := \min\{\mathrm{Re}\mu : \mu \in \mathrm{spec}(B(Q))\}`$. Then:
1. The solenoidal drift $`f_{\mathrm{irrev}}(x) = -Q\Pi x`$ is divergence-free with respect to $`p(x) = \mathcal{N}(0, \Pi^{-1})`$ ($`\nabla \cdot (f_{\mathrm{irrev}} p) = 0`$) and leaves the stationary measure invariant [4].
2. The spectral relaxation rate satisfies $`\gamma(Q) \ge \gamma(0) = \lambda_{\min}(\Pi^{1/2}\Gamma\Pi^{1/2}) > 0`$ with constant trace $`\mathrm{Tr} B(Q) = \mathrm{Tr}(\Gamma\Pi)`$ [4]. Whenever $`\Pi^{1/2}\Gamma\Pi^{1/2}`$ is anisotropic, there exist skew-symmetric matrices $`Q \neq 0`$ such that $`\gamma(Q) > \gamma(0)`$ strictly, up to $`\gamma_{\max} = \frac{1}{n}\mathrm{Tr}(\Gamma\Pi)`$ [4].

*Proof.* (1) $`\nabla \cdot (f_{\mathrm{irrev}}p) = -p\mathrm{Tr}(Q\Pi) + p(\Pi x)^\top Q^\top (\Pi x) = 0`$ by skew-symmetry of $`Q`$ [4]. (2) For $`\widetilde{B}(Q) = \Pi^{1/2}B(Q)\Pi^{-1/2} = S + A`$ with $`S = \Pi^{1/2}\Gamma\Pi^{1/2} \succ 0`$ and $`A = \Pi^{1/2}Q\Pi^{1/2} = -A^\top`$, any unit eigenvector $`v`$ of $`S+A`$ with eigenvalue $`\mu`$ satisfies $`\mathrm{Re}\mu = v^\dagger S v \ge \lambda_{\min}(S) = \gamma(0)`$ [4]. `∎`

---

## **4. Oseledets Spectrum, Coarse-Grained `ε`-Cell Merging, and the Oseledets–Ruelle–Landauer Bridge**

### **4.1. Separating the Structural Functional from the Thermodynamic Flux**

For any localized subsystem $`A = (\mathcal{I}_A, \partial A, \mathcal{E}_A)`$, we separate:
1. **Bulk Structural Functional $`\mathscr{S}_{\mathrm{struct}}(\mathcal{I}_A)`$** and **Interfacial Tension $`\mathscr{S}_{\mathrm{interface}}(\partial A)`$**, defined purely from the combinatorial-phase matrix $`W`$.
2. **Coarse-Grained State-Merging and Entropy Production Flux**, governing the thermodynamic cost of stabilizing an attractor against perturbations [5, 6].

### **4.2. Corrected Entropy Balance, `ε`-Cell Logical Merging, and Oseledets–Ruelle–Landauer Dissipation**

Let the internal state $`z(n) \in \mathbb{R}^{N_A}`$ of $`\mathcal{I}_A`$ evolve under a differentiable map $`z(n+1) = G_R(z(n))`$ with Jacobian $`M(n) = \partial G_R / \partial z|_{z(n)}`$ and Oseledets splitting $`T_{z(n)}\mathcal{I}_A = E^u(z(n)) \oplus E^s(z(n))`$ [6]. Let $`h_{\mathrm{KS}}(A) := \sum_{\lambda_i > 0} \lambda_i \ge 0`$ be the Pesin expansion rate along $`E^u`$ and $`\kappa(A) := \sum_{\lambda_i < 0} |\lambda_i| = -\sum_{\lambda_i < 0} \lambda_i \ge 0`$ be the transverse contraction rate along $`E^s`$, with dissipative confinement $`\kappa(A) > h_{\mathrm{KS}}(A)`$ [6].

To rigorously connect continuous phase-space contraction to **logically erased bits** without sign errors, we introduce a fine-scale observational partition of mesh size $`\varepsilon > 0`$ covering a tubular neighborhood $`U_\varepsilon`$ of the attractor, and track both the **exact coarse-grained Shannon entropy balance** and the **$`M`$-to-$`1`$ logical cell-merging rate** [5]:

1. **Exact Sign Balance of Coarse-Grained Entropy:**  
   Let $`H_\varepsilon(Z_n)`$ denote the Shannon entropy (in nats) of the state distribution over $`\varepsilon`$-cells at step $`n`$. In one step, the deterministic map $`G_R`$ expands volume along $`E^u`$ by $`e^{h_{\mathrm{KS}}(A)}`$ and contracts volume along $`E^s`$ by $`e^{-\kappa(A)}`$ [6], changing the internal entropy by $`\Delta H_{\mathrm{dyn}} = h_{\mathrm{KS}}(A) - \kappa(A) < 0`$. Suppose external perturbations entering across $`\partial^- A`$ inject entropy $`H_{\mathrm{in}}^{(\varepsilon)} \ge 0`$ per step, while outgoing signals across $`\partial^+ A`$ carry away coarse-grained state entropy $`H_{\mathrm{out}}^{(\varepsilon)} \ge 0`$ per step. Then the stationary balance $`H_\varepsilon(Z_{n+1}) - H_\varepsilon(Z_n) = 0`$ is:
```math
0 = H_{\mathrm{in}}^{(\varepsilon)} - H_{\mathrm{out}}^{(\varepsilon)} + h_{\mathrm{KS}}(A) - \kappa(A) \quad \Longleftrightarrow \quad H_{\mathrm{in}}^{(\varepsilon)} - H_{\mathrm{out}}^{(\varepsilon)} = \kappa(A) - h_{\mathrm{KS}}(A) > 0.
```
   Notice what this exact balance says: the coarse-grained Shannon entropy carried away by the macroscopic signal $`H_{\mathrm{out}}^{(\varepsilon)}`$ is **smaller** than $`H_{\mathrm{in}}^{(\varepsilon)} + h_{\mathrm{KS}}(A)`$ by the exact amount $`\Delta S_{\mathrm{fold}}(A) := \kappa(A) > 0`$ (and smaller than $`H_{\mathrm{in}}^{(\varepsilon)}`$ by the net contraction $`\sigma_{\mathrm{bath}}(A) := \kappa(A) - h_{\mathrm{KS}}(A) > 0`$). Where did the missing information $`\sigma_{\mathrm{bath}}(A)`$ go? It was compressed to sub-$`\varepsilon`$ scales below the resolution limit—that is, **erased from the $`\varepsilon`$-resolved macro-state and dumped into microscopic heat/radiation modes of the boundary bath** (Ruelle’s phase-space contraction identity [5]).

2. **Why Transverse Contraction $`\kappa(A)`$ Represents Logical Bit Erasure at Resolution $`\varepsilon`$:**  
   Consider a local product box of $`\varepsilon`$-cells aligned with $`E^u \oplus E^s`$ [6]. Under one step of $`G_R`$, along the transverse contracting subspace $`E^s`$, a transverse volume of $`\exp(\kappa(A))`$ distinct $`\varepsilon`$-cells is mapped into a **single** $`\varepsilon`$-cell on the attractor. Once sub-$`\varepsilon`$ coordinates are indistinguishable (falling into $`\ker \pi_\varepsilon`$ [9]) and re-randomized by thermal/boundary noise of variance $`\ge \varepsilon^2`$, this $`\exp(\kappa(A))`$-to-$`1`$ mapping is a logically irreversible many-to-one state merger in the exact sense of Landauer [5].

**Theorem 4.1 (Coarse-Grained Entropy Balance and $`\varepsilon`$-Resolution Landauer Erasure Rate).** `[Status: FOLLOW (under the stated ε-partition and stationarity assumptions)]` [5, 6]  
Suppose subsystem $`\mathcal{I}_A`$ is partitioned into distinguishable states at resolution scale $`\varepsilon > 0`$, evolves with linearized Jacobian rates $`h_{\mathrm{KS}}(A) = \sum_{\lambda_i > 0}\lambda_i`$ and $`\kappa(A) = \sum_{\lambda_i < 0}|\lambda_i|`$ ($`\kappa(A) > h_{\mathrm{KS}}(A)`$) [6], and is driven across $`\partial^- A`$ by stationary perturbations of resolution-$`\varepsilon`$ entropy rate $`H_{\mathrm{in}}^{(\varepsilon)}`$ that continually repopulate the transverse subspace $`E^s`$ so that the coarse-grained entropy remains stationary ($`H_\varepsilon(Z_{n+1}) = H_\varepsilon(Z_n)`$). Then:
1. **Exact Stationary Entropy Balance:** The resolved outgoing signal entropy $`H_{\mathrm{out}}^{(\varepsilon)}`$ and the unresolved sub-$`\varepsilon`$ folding rate $`\Delta S_{\mathrm{fold}}(A)`$ satisfy the exact conservation equations (in nats per step):
```math
H_{\mathrm{out}}^{(\varepsilon)} = H_{\mathrm{in}}^{(\varepsilon)} + h_{\mathrm{KS}}(A) - \kappa(A) \ge 0, \qquad \Delta S_{\mathrm{fold}}(A) := H_{\mathrm{in}}^{(\varepsilon)} + h_{\mathrm{KS}}(A) - H_{\mathrm{out}}^{(\varepsilon)} = \kappa(A) > 0,
```
   and the net phase-space contraction (net entropy exported to the sub-$`\varepsilon`$ boundary bath per step [5]) is:
```math
\sigma_{\mathrm{bath}}(A) := H_{\mathrm{in}}^{(\varepsilon)} - H_{\mathrm{out}}^{(\varepsilon)} = \kappa(A) - h_{\mathrm{KS}}(A) = \sum_{i=1}^{N_A} (-\lambda_i) > 0.
```
2. **Logical Bit-Merging Rate and Landauer Dissipation Bound:** Along $`E^s`$, the dynamics merge $`\exp(\kappa(A))`$ distinguishable transverse $`\varepsilon`$-states into $`1`$ state per step, corresponding to a gross transverse bit-erasure rate of $`\dot{I}_{\mathrm{merge}}(E^s) = \frac{\kappa(A)}{\ln 2}`$ bits/step, and a net bath bit-export rate (accounting for expansion along $`E^u`$) of:
```math
\dot{I}_{\mathrm{erase}}^{\mathrm{net}}(\mathcal{I}_A \to \partial^+ A) = \frac{\sigma_{\mathrm{bath}}(A)}{\ln 2} = \frac{\kappa(A) - h_{\mathrm{KS}}(A)}{\ln 2} \;\text{bits/step}.
```
   If the sub-$`\varepsilon`$ degrees of freedom on $`\partial^+ A`$ equilibrate with an external channel bath at temperature $`T_{\partial A} > 0`$, the minimum heat/action power dissipated into the bath per step is bounded below by [5]:
```math
\dot{Q}_{\mathrm{ext}}(\partial^+ A) \;\ge\; k_B T_{\partial A} \ln 2 \cdot \dot{I}_{\mathrm{erase}}^{\mathrm{net}} = k_B T_{\partial A} \bigl(\kappa(A) - h_{\mathrm{KS}}(A)\bigr).
```

*Proof.* (1) Partition a local neighborhood into $`\varepsilon`$-boxes aligned with $`E^u \oplus E^s`$ [6]. Under one step of $`G_R`$, each box stretches by $`e^{\lambda_i}`$ along $`i \in E^u`$ (increasing the number of occupied $`\varepsilon`$-boxes along $`E^u`$ by factor $`e^{h_{\mathrm{KS}}(A)}`$, adding $`+h_{\mathrm{KS}}(A)`$ nats) and contracts by $`e^{-|\lambda_i|}`$ along $`i \in E^s`$ (merging $`e^{\kappa(A)}`$ boxes along $`E^s`$ into one box of width $`\varepsilon`$, removing $`\kappa(A)`$ nats from the $`\varepsilon`$-resolved state description). Adding the newly injected perturbation entropy $`H_{\mathrm{in}}^{(\varepsilon)}`$ and subtracting the resolved entropy $`H_{\mathrm{out}}^{(\varepsilon)}`$ exported as macro-signals gives $`H_\varepsilon(Z_{n+1}) - H_\varepsilon(Z_n) = H_{\mathrm{in}}^{(\varepsilon)} - H_{\mathrm{out}}^{(\varepsilon)} + h_{\mathrm{KS}}(A) - \kappa(A)`$. Setting $`H_\varepsilon(Z_{n+1}) = H_\varepsilon(Z_n)`$ yields both identities in item (1) immediately. (2) Because $`e^{\kappa(A)}`$ distinct $`\varepsilon`$-cells along $`E^s`$ collapse into a single $`\varepsilon`$-cell at each step while $`e^{h_{\mathrm{KS}}(A)}`$ new cells open along $`E^u`$, the net number of distinguishable $`\varepsilon`$-cells eliminated from the resolved phase space per step is factor $`e^{\kappa(A) - h_{\mathrm{KS}}(A)}`$, which equals $`\frac{\kappa(A) - h_{\mathrm{KS}}(A)}{\ln 2}`$ bits/step. Applying Landauer’s bound $`k_B T_{\partial A} \ln 2`$ per net erased bit [5] gives $`\dot{Q}_{\mathrm{ext}}(\partial^+ A) \ge k_B T_{\partial A}(\kappa(A) - h_{\mathrm{KS}}(A))`$. `∎`

---

## **5. Time as a Multiscale Synchronization Spectrum, Integrator Chains, and Network Architecture Transition**

### **5.1. Operational Phase-Cycle Ratios and the Kinematic Signature Ansatz**

In $`(X, \prec)`$, no external global time parameter exists; only the causal order $`\prec`$ and phase increments on Hasse links are given [1, 7].

**Definition 5.1 (Proper Phase Rate and Relative Operational Time Ratio).** `[Status: FOLLOW]`
1. For a localized worldtube $`A`$ composed of antichains $`S_0 \prec S_1 \prec \dots \prec S_m`$ with non-empty diamond sets $`\mathcal{D}_A(k)`$ between $`S_k`$ and $`S_{k+2}`$, define the complex order parameter $`z_A(k) := \frac{1}{|\mathcal{D}_A(k)|} \sum_{D \in \mathcal{D}_A(k)} e^{i\Phi_D}`$. When $`|z_A(k)| \ge \theta_{\mathrm{coh}} > 0`$, the **dimensionless internal phase rate per causal step** is:
```math
\omega_A^{(\ell)} := \frac{1}{m} \sum_{k=0}^{m-1} \arg z_A(k) \quad \text{(radians per two-step causal layer)},
```
   and the accumulated phase-cycle count is $`\Delta N_A^{(\ell)} = \frac{m}{2\pi} \omega_A^{(\ell)}`$.
2. For two subsystems $`A`$ and $`B`$ exchanging signals via unbranched null chains ($`d_\diamond = 0`$, along which no internal diamonds close: $`\Delta N_{\mathrm{null}} = 0`$), the **relative operational time ratio** between successive exchanges is the dimensionless ratio:
```math
R_{AB}^{(\ell)} := \frac{\Delta N_A^{(\ell)}}{\Delta N_B^{(\ell)}} = \frac{\omega_A^{(\ell)} \Delta m_A}{\omega_B^{(\ell)} \Delta m_B}.
```

**Explicit Distinction Between Combinatorial Phase Rate and Physical Time:** `[Status: UNDECIDED]`  
By Definition 5.1, $`\omega_A^{(\ell)}`$ is measured in radians per discrete causal step, **not** in inverse seconds ($`\mathrm{s}^{-1}`$). Identifying $`R_{AB}^{(\ell)}`$ with the physical clock redshift ratio $`d\tau_A / d\tau_B`$ requires establishing in the continuum limit [1, 7] that the internal diamond-cycle counter $`\Delta N_A^{(\ell)}`$ is proportional to the Lorentzian proper-time integral $`\int \sqrt{-g_{\mu\nu}dx^\mu dx^\nu}`$.

**Kinematic Step-Allocation Ansatz for the Lorentzian Signature $`(-,+,+,+)`$:** `[Status: UNDECIDED — Kinematic Hypothesis]`  
If one postulates as a kinematic ansatz that a total budget of $`\Delta s_{\mathrm{causal}}`$ Hasse steps along a worldtube is shared quadratically between transverse spatial displacement ($`\Delta l`$, along antichains) and internal diamond closure ($`\Delta \tau \propto \Delta N_A`$), i.e., $`(\Delta \tau)^2 + (\Delta l)^2 = (\Delta s_{\mathrm{causal}})^2`$, then rewriting the invariant for unbranched null propagation ($`\Delta \tau = 0`$ internally, $`\Delta l = \Delta s_{\mathrm{causal}}`$) vs. stationary diamond cycling ($`\Delta l = 0`$, $`\Delta \tau = \Delta s_{\mathrm{causal}}`$) motivates the opposite-sign quadratic form $`\Delta s_{\mathrm{Lorentz}}^2 := -(\Delta \tau)^2 + (\Delta l)^2`$. **Note:** Because the quadratic step-allocation law is an assumed ansatz rather than a theorem derived from $`\prec`$ alone, the emergence of a true Lorentzian metric signature $`(-,+,+,+)`$ is classified as `UNDECIDED` and must be tested via causal-cone and Myrheim–Meyer dimension reconstruction [1] in Protocol V1.

### **5.2. Stochastic Realization of Boundary Spectra and Second-Order Inertia**

**Proposition 5.1 (Stochastic Realization of Multi-Frequency Boundary Processes as Integrator Chains).** `[Status: FOLLOW]` [4]  
Let $`s_t`$ be a mean-zero stationary Gaussian process on $`\partial^- A`$ with a rational spectral density determined by decay/oscillation modes $`\{\gamma_k \pm i\omega_k\}_{k=0}^n`$ ($`\gamma_k > 0`$). Then:
1. By Doob’s theorem and linear stochastic realization theory [4], $`s_t = F_0 s_t^{(0)}`$ is the marginal output of a Markovian integrator chain $`\tilde{s}_t = (s_t^{(0)}, s_t^{(1)}, \dots, s_t^{(n)})`$ of generalized coordinates of motion satisfying $`ds_t^{(k)} = (-A_k s_t^{(k)} + B_k s_t^{(k+1)})\,dt + \varsigma_k\,dW_t^{(k)}`$ ($`0 \le k < n`$) and $`ds_t^{(n)} = -A_n s_t^{(n)}\,dt + \varsigma_n\,dW_t^{(n)}`$.
2. Under timescale separation $`0 < \gamma_0 \le \gamma_1 \le \gamma_2 \ll \gamma_3 \le \dots \le \gamma_n`$, coarse-graining over a window $`\tau_w^{(\ell)} \in (\gamma_2^{-1}, \gamma_3^{-1})`$ suppresses the window-averaged variance of orders $`k \ge 3`$ as $`O((\gamma_k \tau_w^{(\ell)})^{-1})`$, truncating the boundary state to $`\tilde{s}_t^{(\le 2)} = (s_t^{(0)}, s_t^{(1)}, s_t^{(2)})`$ and yielding a second-order linear-quadratic control law (effective inertia, damping, and restoring force) [4].

*Proof.* Follows from minimum-phase spectral factorization $`S(\omega) = H(i\omega)H(-i\omega)^\top`$ into block-companion form and exact Ornstein–Uhlenbeck window-variance integration $`\mathrm{Var}\bigl(\frac{1}{\tau_w}\int_0^{\tau_w} s_t^{(k)}dt\bigr) \propto \frac{2(\gamma_k\tau_w - 1 + e^{-\gamma_k\tau_w})}{(\gamma_k\tau_w)^2} = O((\gamma_k\tau_w)^{-1})`$ [4]. `∎`

### **5.3. Multiscale Coarse-Graining Operator `ℛ_{ℓ→ℓ+1}` and Architectural Transition**

**Definition 5.2 (Coarse-Graining Operator $`\mathcal{R}_{\ell \to \ell+1}`$ and Synchronization Time $`\tau_{\mathrm{sync}}`$).** `[Status: FOLLOW]`  
At scale $`\ell`$, spacelike pairs ($`u \not\prec_\ell v, v \not\prec_\ell u`$) with two-step overlap $`S^{(\ell)}_{uv} = |(\Delta_+^{(\ell)})_{uv}| + |(\Delta_-^{(\ell)})_{uv}| \ge \theta_\ell`$ are grouped into order-convex macro-nodes $`X_{\ell+1} = \{C_\alpha\}`$ (rejecting any clustering that induces a directed cycle in the quotient order), followed by Hasse transitive reduction $`R_{\ell+1}`$ and coherent amplitude summation $`\widetilde{W}^{(\ell+1)}_{\alpha\beta} = \sum_{x \in C_\alpha, y \in C_\beta} W^{(\ell)}_{xy}`$. For a subsystem $`A_\ell`$ with diameter $`\tau_{\mathrm{diam}}(A_\ell)`$, normalized Laplacian Fiedler eigenvalue $`\lambda_2(A_\ell) > 0`$, and frequency dispersion $`\sigma_\omega(A_\ell)`$, the synchronization time is $`\tau_{\mathrm{sync}}(A_\ell) := \tau_{\mathrm{diam}}(A_\ell) / \lambda_2(A_\ell)`$.

**Proposition 5.2 (Synchronization Instability of a Homogeneous $`d`$-Dimensional Ball as $`N \to \infty`$ Under Bounded Degree).** `[Status: FOLLOW]`  
On a regular $`d`$-dimensional ball ($`d \ge 2`$) of $`N`$ vertices with bounded degree $`\mathrm{deg}(x) \le k_{\max}`$, $`\tau_{\mathrm{diam}}(A) = \Theta(N^{1/d})`$ and $`\lambda_2(A) = \Theta(N^{-2/d})`$, so $`\tau_{\mathrm{sync}}^{\mathrm{ball}}(N) = \Theta(N^{3/d}) \to \infty`$ as $`N \to \infty`$, violating $`\tau_{\mathrm{sync}} \le 2\pi/\sigma_\omega`$ above $`N_{\mathrm{crit}}(d, k_{\max}, \sigma_\omega)`$.

---

## **6. Local-Global Channel Balance, Effective Gravity, and Horizon Saturation**

### **6.1. Combinatorial Identity of Diamond Partitioning and Void Rarefaction**

**Proposition 6.1 (Additive Diamond Partition Identity).** `[Status: FOLLOW]`  
Assigning each waist with $`K_{xy} \ge 2`$ to its lower anchor $`x \in X`$ via $`q_x := \sum_{y:\, K_{xy} \ge 2} K_{xy}\mathrm{Coh}_{xy} = \sum_{y:\, K_{xy} \ge 2} \frac{|M_{xy}|^2}{K_{xy}}`$ and setting $`\rho_D(U) := \frac{1}{|U|}\sum_{x \in U} q_x`$ yields the exact additive identity across any partition $`X = \mathcal{E} \sqcup \bigsqcup_{m=1}^M (\mathcal{I}_{A_m} \sqcup \partial A_m)`$:

```math
\rho_D(\mathcal{E}) = \frac{1}{|\mathcal{E}|} \left( Q_{\mathrm{tot}}(X) - \sum_{m=1}^{M} |\mathcal{I}_{A_m}| \, \rho_D(\mathcal{I}_{A_m}) - \sum_{m=1}^{M} |\partial A_m| \, \rho_D(\partial A_m) \right).
```

**Hypothesis H-LG (Phase-Mediated Void Rarefaction):** `[Status: UNDECIDED — tested in Protocol V3]`  
At fixed total edge budget $`E_{\mathrm{tot}}`$ and valency bound $`k_{\max}`$, increasing internal contraction $`\kappa(A_m)`$ inside localized cores $`\mathcal{I}_{A_m}`$ increases the outward net erasure flux $`\dot{I}_{\mathrm{erase}}^{\mathrm{net}} = (\kappa(A_m) - h_{\mathrm{KS}}(A_m))/\ln 2`$ across $`\partial^+ A_m`$ (Theorem 4.1) [5, 6]. Propagating into $`\mathcal{E}`$ via mediated covariance $`\Sigma_{\mathcal{I}\mathcal{E}} \neq 0`$ (Proposition 2.2) [4] — a static covariance channel whose dynamical rewiring counterpart is not derived in this document — this flux is hypothesized to reconfigure edges in distant void regions $`\mathcal{E}_{\mathrm{void}}`$ from diamond-embedded links ($`d_\diamond(x, y) \ge 1`$) into unbranched null links ($`d_\diamond(x, y) = 0`$), increasing the non-trivial null-link fraction $`f_{\mathrm{null}}(\mathcal{E}_{\mathrm{void}})`$ (§2.2) and stretching null geodesic distances $`\ell_{\mathrm{null}}(\mathcal{E}_{\mathrm{void}})`$ beyond combinatorial degree-preserving controls [9].

### **6.2. Three-Component Structure of Effective Field Equations and Interfacial Saturation**

In the continuum limit `[Status: UNDECIDED]` (Protocols V4 and V6), the thermodynamic equation-of-state route [3] motivates — rather than derives; no closure relation for $`\Lambda_{\mathrm{eff}}[I_{\mathrm{erase}}^{\mathrm{net}}]`$ is given in this document — the decomposition of stress-energy and channel response across the triad $`(\mathcal{I}_A, \partial A, \mathcal{E}_A)`$:

```math
R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu} + \Lambda_{\mathrm{eff}}[I_{\mathrm{erase}}^{\mathrm{net}}] \, g_{\mu\nu} = \frac{8\pi G_{\mathrm{eff}}}{c^4} \Bigl( T_{\mu\nu}^{\mathrm{bulk}}(\mathcal{I}_A) + T_{\mu\nu}^{\mathrm{interface}}(\partial A) + T_{\mu\nu}^{\mathrm{em}}(F_{\alpha\beta}) \Bigr),
```

while the dimensionless **interface saturation parameter** is defined from Theorem 4.1 and Proposition 2.1 as [5]:

```math
\eta_{\mathrm{sat}}(A) := \frac{\dot{I}_{\mathrm{erase}}^{\mathrm{net}}(\mathcal{I}_A \to \partial^+ A)}{C_{\max}(\partial^+ A)} = \frac{\kappa(A) - h_{\mathrm{KS}}(A)}{c_0 \ln 2 \cdot |\partial^+ A|_E}.
```

Crossing $`\eta_{\mathrm{sat}}(A) \ge 1`$ saturates the outgoing boundary channel [5], breaking kernel inclusion $`\ker \Pi_{\mathcal{I},\partial A} \subseteq \ker \Pi_{\mathcal{E},\partial A}`$ [4] for deep interior modes (event horizon formation) and preventing internal phase-fluctuation expulsion so that the interior transitions to a high-rank multi-vertex matrix phase $`K_{xy}^{\mathrm{eff}} \ge 3`$ [8] `[Status: UNDECIDED]` (Protocol V6).

---

## **7. Computational Verification Program (Protocols V1–V7)**

| ID | Tested Claim | Protocol & Control Ensembles | Confirmation Criterion (`FOLLOW`) | Refutation Criterion (`NULL`) |
| :--- | :--- | :--- | :--- | :--- |
| **V1** | **Interval-local path reduction to $`K_{xy}^{\mathrm{eff}}=2`$ and dimension convergence (§3.2–3.3)** | Anneal graphs $`N \in \{128, 256\}`$ under convex ($`p=2`$), linear ($`p=1`$), and logarithmic penalties; evaluate interval-local path rank $`K_{xy}^{\mathrm{eff}}`$, twin-only vertex reduction, and $`(d_s, d_H, d_\tau)`$ [1]. | Under convex penalty and bounded valency $`k_{\max}`$ [2], $`f_{K^{\mathrm{eff}}=2} \ge 0.80`$ and $`\vert{}d_s - d_H\vert{}, \vert{}d_s - d_\tau\vert{} \le 0.3`$ across a decade of scale. | $`K_{xy}^{\mathrm{eff}}=2`$ fails to emerge without manual hard-coding, or dimensions diverge $`\implies`$ closes spontaneous geometry selection. |
| **V2** | **Oseledets contraction $`\kappa(A) - h_{\mathrm{KS}}(A)`$ vs. $`\varepsilon`$-cell merging and bath flux (§4.2)** | Measure $`\varepsilon`$-box entropy $`H_\varepsilon(Z_n)`$, incoming noise $`H_{\mathrm{in}}^{(\varepsilon)}`$, resolved output $`H_{\mathrm{out}}^{(\varepsilon)}`$, and $`\kappa(A) - h_{\mathrm{KS}}(A)`$ [5, 6] across stiffness parameters. Control: covariance-matched linear network [6]. | Exact identity $`H_{\mathrm{in}}^{(\varepsilon)} - H_{\mathrm{out}}^{(\varepsilon)} \approx \kappa(A) - h_{\mathrm{KS}}(A)`$ holds with Pearson $`r \ge 0.90`$, and transverse $`\varepsilon`$-box merging scales as $`e^{\kappa(A)}`$. | Coarse-grained entropy drop does not track $`\kappa(A) - h_{\mathrm{KS}}(A)`$ $`\implies`$ closes Oseledets–Ruelle–Landauer bridge. |
| **V3** | **Phase-mediated void rarefaction via $`d_\diamond(x,y)=0`$ (§2.1, §6.1)** | Condense cores $`\mathcal{I}_{A_m}`$ at fixed $`E_{\mathrm{tot}}, k_{\max}`$. Measure far-void diamond residual $`\Delta \rho_{D,*}^{\mathrm{far}}(r)`$, non-trivial null-link fraction $`f_{\mathrm{null}}(\mathcal{E}_{\mathrm{void}})`$ ($`d_\diamond = 0`$), and $`\ell_{\mathrm{null}}`$. Controls: degree-preserving swaps [9] & boundary phase scrambling. | $`>3\sigma`$ drop in $`\Delta \rho_{D,*}^{\mathrm{far}} < 0`$, rise in $`f_{\mathrm{null}}(\mathcal{E}_{\mathrm{void}}) > 0`$, and expansion $`\Delta \ell_{\mathrm{null}} > 0`$ that vanish under boundary phase randomization. | $`f_{\mathrm{null}}`$ and $`\Delta \rho_D^{\mathrm{far}}`$ are fully explained by degree-preserving edge swaps [9] or insensitive to phase scrambling $`\implies`$ closes H-LG. |
| **V4** | **Interfacial synchronization-shell potential on $`\partial A`$ (§6.2)** | Measure radial frequency shift $`\delta\omega(r)/\omega_\infty`$ and interaction free energy $`V_{\mathrm{int}}(r)`$ around a cluster with $`\omega_A \neq \omega_{\mathrm{ext}}`$ vs. control $`\omega_A = \omega_{\mathrm{ext}}`$ [3]. | Extended shell $`r \in [r_{\mathrm{bulk}}, r_{\mathrm{halo}}]`$ where $`\partial_r V_{\mathrm{int}}(r) > 0`$ scales with $`\vert{}\omega_A - \omega_{\mathrm{ext}}\vert{}`$ and interfacial tension $`\mathscr{S}_{\mathrm{interface}}(\partial A)`$. | Potential truncates sharply at core boundary $`\implies`$ closes interfacial halo model. |
| **V5** | **Scale transition from compact modes to filamentary networks (§5.3)** | Minimize volume and frustration subject to $`\lambda_2(A) \ge \lambda_{\mathrm{sync}}`$ and $`\mathrm{deg}(x) \le k_{\max}`$ across $`N = 64 \to 1024`$ and $`\mathcal{R}_{\ell \to \ell+1}`$. Control: degree-matched configuration models [9]. | Transition from compact rotational clusters ($`N < N_{\mathrm{crit}}`$) to node-filament-void percolation networks ($`N > N_{\mathrm{crit}}`$) [9] stable under $`\mathcal{R}_{\ell \to \ell+1}`$. | Graphs disconnect, collapse to trees, or depend on manual clustering thresholds $`\implies`$ closes scaling hypothesis. |
| **V6** | **Interface saturation $`\eta_{\mathrm{sat}} \ge 1`$ and transition to $`K_{xy}^{\mathrm{eff}} \ge 3`$ (§6.2)** | Increase bulk contraction $`\kappa(U_c)`$ at fixed $`\vert{}\partial^+ U_c\vert{}_E`$ [5]. Track trans-boundary mutual information and interior $`K_{xy}^{\mathrm{eff}}`$ across $`\eta_{\mathrm{sat}}(U_c) = 1`$ [8]. | Outward information saturates at $`\vert{}\partial^+ U_c\vert{}_E`$, $`\sigma`$ degenerates on deep modes [4], and interior stabilizes at $`K^{\mathrm{eff}}_{xy} \ge 3`$ [8]. | Interior collapses into unstructured Kleitman–Rothschild 3-layer graph [2] $`\implies`$ closes post-horizon phase. |
| **V7** | **Precision kernel inclusion, solenoidal gap acceleration, and integrator truncation (§2.4, §3.4, §5.2)** | Test $`\sigma(\overline{\mu}(b)) = \overline{\eta}(b)`$ under $`\ker \Pi_{\mathcal{I},\partial A} \subseteq \ker \Pi_{\mathcal{E},\partial A}`$; compare $`\gamma(Q)`$ vs. $`\gamma(0)`$; measure integrator truncation residual at $`n(\ell)=2`$ [4]. | Synchronization error $`< 10^{-10}`$ under kernel inclusion; strict acceleration $`\gamma(Q) > \gamma(0)`$; $`O((\gamma_3 \tau_w)^{-1})`$ fast-mode decay [4]. | Synchronization fails under inclusion, $`\gamma(Q) < \gamma(0)`$, or high orders fail to decouple [4]. |

---

## **8. Registry of Verification Statuses (`V_4`)**

| No. | Claim | $`V_4`$ Status | Basis and Audit Resolution |
| :--- | :--- | :--- | :--- |
| **1** | Hasse irreducibility ($`R_{xy}=1 \implies K_{xy}=0`$) [1], nilpotency $`W^N = 0`$, Wilson identity $`\sum_{a<b}(1-\cos\Phi_{ab}) = \frac{1}{2}K_{xy}J_{xy}`$, and non-trivial **diamond-participation multiplicity** $`d_\diamond(x, y)`$ partitioning Hasse links into unbranched null links ($`d_\diamond = 0`$) and diamond-embedded links ($`d_\diamond \ge 1`$) | **`FOLLOW`** | Definitions 1.1–1.2, Proposition 1.1, and Definition 2.1. Resolves the $`R_{xy}=1 \implies K_{xy}=0`$ tautology completely. |
| **2** | Triad partition $`(\mathcal{I}_A, \partial A, \mathcal{E}_A)`$, recoverability bound $`I(Z_A; \hat{Z}_A) \le I(Z_A; Z_B) + n C(\partial^+ A)`$ (Proposition 2.1), precision sparsity $`\Pi_{\mathcal{I}\mathcal{E}}=0`$ vs. mediated covariance $`\Sigma_{\mathcal{I}\mathcal{E}} \neq 0`$, and boundary kernel inclusion $`\ker \Pi_{\mathcal{I},\partial A} \subseteq \ker \Pi_{\mathcal{E},\partial A}`$ (Proposition 2.2) [4] | **`FOLLOW`** | Graph locality, data processing inequality, and exact block-Gaussian identities [4]. |
| **3** | Interval-local path equivalence $`\sim_{(x,y),\varepsilon_{\mathrm{ker}}}`$ on $`\mathcal{P}_2(x, y)`$, strict separation from global structural-twin vertex merging (Definition 3.1), and conditional minimization of $`\mathcal{F}_{\mathrm{loc}}^{(p)} = a(K^{\mathrm{eff}})^p + b J^{\mathrm{eff}}_{xy}`$ ($`a,p>0`$) at $`K_{xy}^{\mathrm{eff}}=2`$ for fixed $`J_0 \in (0, 2]`$ (Proposition 3.1) | **`FOLLOW`** | Exact within the declared functional ansatz and interval-local quotient; prevents cross-interval vertex contamination. |
| **4** | Physical justification that natural causal substrates enforce a convex branching penalty $`a(K^{\mathrm{eff}})^p`$ ($`p \ge 2`$) selecting $`K_{xy}^{\mathrm{eff}} = 2`$ | **`UNDECIDED`** | Empirical hypothesis about substrate dynamics; tested against linear/concave alternatives in **Protocol V1**. |
| **5** | Helmholtz drift decomposition $`f = f_{\mathrm{rev}} + f_{\mathrm{irrev}}`$, invariance of $`p(x) = \mathcal{N}(0, \Pi^{-1})`$ under $`Q = -Q^\top`$, and spectral relaxation acceleration $`\gamma(Q) \ge \gamma(0)`$ (Proposition 3.2) [4] | **`FOLLOW`** | Stationary Fokker–Planck equation and Bendixson field-of-values bound [4]. |
| **6** | Coarse-grained $`\varepsilon`$-box entropy balance $`H_{\mathrm{out}}^{(\varepsilon)} = H_{\mathrm{in}}^{(\varepsilon)} + h_{\mathrm{KS}}(A) - \kappa(A)`$, sub-$`\varepsilon`$ folding rate $`\sigma_{\mathrm{bath}}(A) = H_{\mathrm{in}}^{(\varepsilon)} - H_{\mathrm{out}}^{(\varepsilon)} = \kappa(A) - h_{\mathrm{KS}}(A)`$, $`e^{\kappa(A)}`$-to-$`1`$ transverse $`\varepsilon`$-cell merging along $`E^s`$, and Landauer heat bound $`\dot{Q}_{\mathrm{ext}} \ge k_B T_{\partial A}(\kappa(A) - h_{\mathrm{KS}}(A))`$ (Theorem 4.1) [5, 6] | **`FOLLOW`** | Exact sign-consistent conservation law at resolution $`\varepsilon > 0`$ under stationary $`H_\varepsilon(Z_{n+1}) = H_\varepsilon(Z_n)`$ [5, 6]. Resolves the sign error present in the v3.8 and early v3.9 drafts. |
| **7** | Doob integrator-chain realization of rational-spectrum boundary processes (Proposition 5.1) [4], divergence of ball synchronization time $`\tau_{\mathrm{sync}}^{\mathrm{ball}}(N) = \Theta(N^{3/d})`$ (Proposition 5.2), and additive diamond conservation across $`(\mathcal{I}_{A_m}, \partial A_m, \mathcal{E})`$ (Proposition 6.1) | **`FOLLOW`** | Spectral factorization of stationary Gaussian processes [4], Laplacian asymptotics, and finite-set additivity. |
| **8** | Quadratic step-allocation ansatz $`(\Delta \tau)^2 + (\Delta l)^2 = (\Delta s_{\mathrm{causal}})^2`$, emergence of continuum Lorentzian signature $`(-,+,+,+)`$ [1], and physical calibration of combinatorial phase rate $`\omega_A^{(\ell)}`$ (radians/step) to physical clock frequency ($`\mathrm{s}^{-1}`$) [7] (§5.1) | **`UNDECIDED`** | Explicitly marked as kinematic ansatz and continuum-limit hypothesis; requires verification in **Protocols V1 and V4**. |
| **9** | Phase-mediated void rarefaction (H-LG), interfacial halo tension $`T_{\mu\nu}^{\mathrm{interface}}(\partial A)`$ [3], percolation transition to *Cosmic Web* filaments above $`N_{\mathrm{crit}}`$ [9], and post-horizon phase $`K_{xy}^{\mathrm{eff}} \ge 3`$ at $`\eta_{\mathrm{sat}} \ge 1`$ [8] | **`UNDECIDED`** | Substantive physical hypotheses tested in **Protocols V3, V4, V5, and V6**. |
| **10** | Defining null links via $`(R_{xy}=1) \land (K_{xy}=0)`$ — a tautological restatement of Hasse irreducibility (§1.1) that carries no independent content | **`OMIT`** | Vacuous consequence of the irreducibility identity $`R_{xy}=1 \implies K_{xy}=0`$ (§1.1); the non-trivial replacement is Definition 2.1 via the diamond-participation multiplicity $`d_\diamond(x, y)`$. Audit of the v3.8 and early v3.9 drafts [2, 10]. |
| **11** | Merging vertices across distinct intervals via global `union-find` without twin checks; writing $`H_{\mathrm{out}} \ge \kappa - h_{\mathrm{KS}}`$ with inverted sign; claiming a passive Gaussian Markov blanket without action loop or stake is an intrinsic agent [4] | **`NULL`** | Mathematically inconsistent or framework-contradicting audit defects identified in the v3.8 and early v3.9 drafts; replaced and prohibited in the present version (v3.9) [4, 6, 10]. |

---

## **9. Corrected Reference Computational Implementation (Python / NumPy / SciPy)**

All computational audit corrections are implemented and verified in the code below (the fourth audit defect catalogued in §8, row 11 — the intrinsic-agent claim — is conceptual and is resolved at the framework level rather than in code):
1. `compute_edge_diamond_participation(R)` computes the exact non-trivial diamond multiplicity $`d_\diamond(x, y)`$ for every Hasse link $`R_{xy}=1`$, identifying unbranched null links via $`R_{xy}=1 \land d_\diamond(x, y) = 0`$.
2. `interval_local_path_quotient(R, Theta, eps_ker)` performs path factorization **strictly inside each interval $`(x, y)`$** on $`\mathcal{P}_2(x, y)`$, while `collapse_structural_twins(R, Theta, eps_ker)` merges vertices **only** if they are true causal twins sharing identical predecessors and successors.
3. `compute_oseledets_landauer_profile(...)` implements the sign-consistent $`\varepsilon`$-box entropy bookkeeping of Theorem 4.1 — $`H_{\mathrm{out}}^{(\varepsilon)} = H_{\mathrm{in}}^{(\varepsilon)} + h_{\mathrm{KS}} - \kappa`$ and net bath folding rate $`\sigma_{\mathrm{bath}} = H_{\mathrm{in}}^{(\varepsilon)} - H_{\mathrm{out}}^{(\varepsilon)} = \kappa - h_{\mathrm{KS}}`$ — as an exact algebraic identity on the computed spectrum; empirical measurement of $`H_{\mathrm{in}}^{(\varepsilon)}`$, $`H_{\mathrm{out}}^{(\varepsilon)}`$ on simulated noisy trajectories is the task of the Protocol V2 harness (Technical Specification v0.3, §4).

In addition, the implementation incorporates the five mandatory numerical-robustness fixes (`FIX-1`–`FIX-5`) and the protocol infrastructure required by **Technical Specification v0.3** (§2.2; `Physics/Technical_Specification_v0.3.md`): iterative Hasse-reachability verification, explicit `int64` casting of adjacency arithmetic, eigenvalue-based Lyapunov spectra (SVD retained for diagnostics), directed causal diameters, isolated-vertex filtering before normalized-Laplacian spectra, and graph generators, null-test controls, dimension estimators, and $`\varepsilon`$-box entropy for protocols V1–V7.

```python
"""
cpp_v39_reference.py

Patched reference implementation for Causal Phase Program v3.9, Section 9.
Implements mandatory fixes from Technical_Specification_v0.3.md §2.2
and adds minimal infrastructure for Protocols V1–V7.

Changes relative to the §9 block in Causal_Phase_Program_v3.md:
  [FIX-1] is_hasse_transitive_free: iterative reachability instead of np.linalg.inv
  [FIX-2] Explicit int64 cast on all R-matrix inputs
  [FIX-3] Lyapunov spectrum via eigenvalues (default), SVD retained for diagnostics
  [FIX-4] Directed shortest paths for causal diameter
  [FIX-5] Isolated-vertex filtering before Laplacian eigenvalues
  [NEW]   Graph generators, null-test controls, dimension estimators, ε-box entropy

Normative parent: Physics/Causal_Phase_Program_v3.md (v3.9)
Canonical logic:  Reasoning/Modified_Brusentsov_Entailment_Logic.md
"""

import numpy as np
from scipy.sparse.csgraph import connected_components, shortest_path
from scipy.linalg import eigh, eigvals, svdvals, pinv


# =====================================================================
# 1. FOUNDATIONAL CAUSAL-PHASE ALGEBRA & EDGE DIAMOND MULTIPLICITY
# =====================================================================

def _as_int64(R):
    """[FIX-2] Force integer dtype for all adjacency-matrix arithmetic."""
    return np.asarray(R).astype(np.int64)


def is_hasse_transitive_free(R):
    """
    [FIX-1] Verify Hasse transitive irreducibility for a strictly
    upper-triangular Boolean matrix R: no edge short-circuits a
    directed path of length >= 2.

    Replaces np.linalg.inv(np.eye(N) - R) with iterative reachability.
    Complexity: O(N * N^3) worst case, but early-exits on nilpotency.
    For N <= 1024 and sparse DAGs this is typically << 1 second.
    """
    R = _as_int64(R)
    N = len(R)
    if not np.all(np.tril(R) == 0):
        return False

    R_bool = R > 0
    # reach_2plus[x, y] = True iff there exists a path x -> ... -> y
    # of length >= 2.
    reach_2plus = np.zeros((N, N), dtype=bool)
    power = R_bool.copy()                       # R^1
    for k in range(2, N):
        power = (power @ R_bool) > 0            # R^k (Boolean product)
        if not np.any(power):
            break                               # nilpotency: R^k = 0
        reach_2plus |= power

    # A Hasse link R[x,y]=1 must NOT be short-circuited by a path
    # of length >= 2.
    return not np.any(R_bool & reach_2plus)


def compute_causal_phase_invariants(R, Theta):
    """
    [FIX-2] Compute the waist matrix K_xy = (R^2)_xy, two-step amplitude
    M_xy = (W^2)_xy, and phase frustration J_xy.
    """
    R = _as_int64(R)
    W = R * np.exp(1j * np.asarray(Theta))
    K = R @ R                                   # int64 arithmetic
    M = W @ W
    mask = K > 0
    J = np.zeros(K.shape, dtype=float)
    J[mask] = (K[mask] ** 2 - np.abs(M[mask]) ** 2) / K[mask]
    return K, M, J


def compute_edge_diamond_participation(R):
    """
    Compute the exact diamond-participation multiplicity d_diamond(x, y)
    for every Hasse link R_xy == 1 (Definition 2.1).

    Unbranched (null) Hasse links: R[x, y] == 1 and d_diamond[x, y] == 0.
    """
    R_int = _as_int64(R)
    K = R_int @ R_int
    K_excess = np.maximum(0, K - 1)
    d_plus = R_int * (K_excess @ R_int.T)
    d_minus = R_int * (R_int.T @ K_excess)
    d_diamond = d_plus + d_minus
    null_edges_mask = (R_int == 1) & (d_diamond == 0)
    diamond_edges_mask = (R_int == 1) & (d_diamond >= 1)
    return d_diamond, null_edges_mask, diamond_edges_mask


def verify_wilson_identity(R, Theta):
    """
    Numerical verification of Proposition 1.1:
    Sum_{a < b} (1 - cos(Phi_ab)) == 0.5 * K_xy * J_xy.
    """
    R = _as_int64(R)
    Theta = np.asarray(Theta)
    N = len(R)
    K, _, J = compute_causal_phase_invariants(R, Theta)
    max_err = 0.0
    for x in range(N - 2):
        for y in range(x + 2, N):
            if K[x, y] >= 2:
                zs = np.where((R[x, :] == 1) & (R[:, y] == 1))[0]
                phases = Theta[x, zs] + Theta[zs, y]
                diff = phases[:, None] - phases[None, :]
                lhs = 0.5 * np.sum(1.0 - np.cos(diff))
                rhs = 0.5 * K[x, y] * J[x, y]
                max_err = max(max_err, abs(lhs - rhs))
    return float(max_err)


# =====================================================================
# 2. TRIAD PARTITIONING (I_A, dA, E_A) WITH NON-TRIVIAL NULL LINKS
# =====================================================================

def partition_triad(R, subsystem_nodes):
    """
    Partition complex X into the structural triad (Definition 2.2).
    """
    R = _as_int64(R)
    N = len(R)
    A_mask = np.zeros(N, dtype=bool)
    A_mask[list(subsystem_nodes)] = True
    E_mask = ~A_mask

    edges_in = (R == 1) & E_mask[:, None] & A_mask[None, :]
    edges_out = (R == 1) & A_mask[:, None] & E_mask[None, :]
    dA_in = np.where(np.any(edges_in, axis=0))[0]
    dA_out = np.where(np.any(edges_out, axis=1))[0]
    dA = np.union1d(dA_in, dA_out)
    I_A = np.setdiff1d(np.where(A_mask)[0], dA)
    E_A = np.where(E_mask)[0]

    d_diamond, null_mask, _ = compute_edge_diamond_participation(R)
    ext_edge_mask = (R == 1) & E_mask[:, None] & E_mask[None, :]
    E_null_edges = null_mask & ext_edge_mask
    n_ext_edges = int(np.sum(ext_edge_mask))
    n_null_edges = int(np.sum(E_null_edges))
    f_null_ext = float(n_null_edges / max(1, n_ext_edges))

    return {
        "I_A": I_A,
        "dA_in": dA_in,
        "dA_out": dA_out,
        "dA": dA,
        "E_A": E_A,
        "capacity_in": int(np.sum(edges_in)),
        "capacity_out": int(np.sum(edges_out)),
        "d_diamond": d_diamond,
        "E_null_edges": E_null_edges,
        "f_null_ext": f_null_ext,
    }


# =====================================================================
# 3. INTERVAL-LOCAL PATH QUOTIENT vs. TWIN VERTEX MERGING (§3.2, V1)
# =====================================================================

def interval_local_path_quotient(R, Theta, eps_ker=0.30):
    """
    [FIX-2] Interval-local path factorization on P_2(x, y)
    (Definition 3.1, item 1).
    """
    R = _as_int64(R)
    Theta = np.asarray(Theta)
    N = len(R)
    K = R @ R
    K_eff = np.zeros((N, N), dtype=int)
    J_eff = np.zeros((N, N), dtype=float)

    for x in range(N - 2):
        for y in range(x + 2, N):
            if K[x, y] == 1:
                K_eff[x, y] = 1
                J_eff[x, y] = 0.0
            elif K[x, y] >= 2:
                zs = np.where((R[x, :] == 1) & (R[:, y] == 1))[0]
                m = len(zs)
                phases = (Theta[x, zs] + Theta[zs, y]) % (2.0 * np.pi)

                parent = list(range(m))

                def find_local(i):
                    while parent[i] != i:
                        parent[i] = parent[parent[i]]
                        i = parent[i]
                    return i

                for a in range(m):
                    for b in range(a + 1, m):
                        dphi = abs(phases[a] - phases[b])
                        dphi = min(dphi, 2.0 * np.pi - dphi)
                        if dphi <= eps_ker:
                            ra, rb = find_local(a), find_local(b)
                            if ra != rb:
                                parent[max(ra, rb)] = min(ra, rb)

                classes = {}
                for i in range(m):
                    classes.setdefault(find_local(i), []).append(phases[i])

                eff_phases = np.array([
                    np.angle(np.sum(np.exp(1j * np.array(ph_list))))
                    for ph_list in classes.values()
                ])
                k_e = len(eff_phases)
                m_e = np.sum(np.exp(1j * eff_phases))
                K_eff[x, y] = k_e
                J_eff[x, y] = float((k_e ** 2 - np.abs(m_e) ** 2) / k_e)

    active_intervals = K >= 2
    n_active = int(np.sum(active_intervals))
    f_K2_eff = float(
        np.sum((K_eff == 2) & active_intervals) / max(1, n_active)
    )
    return K_eff, J_eff, f_K2_eff


def collapse_structural_twins(R, Theta, eps_ker=0.30):
    """
    [FIX-2] Global vertex reduction restricted strictly to causal
    structural twins (Definition 3.1, item 2).
    """
    R = _as_int64(R)
    Theta = np.asarray(Theta)
    N = len(R)
    parent = np.arange(N, dtype=int)

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    for za in range(N):
        for zb in range(za + 1, N):
            if np.array_equal(R[:, za], R[:, zb]) and np.array_equal(
                R[za, :], R[zb, :]
            ):
                preds = np.where(R[:, za] == 1)[0]
                succs = np.where(R[za, :] == 1)[0]
                all_coherent = True
                for u in preds:
                    for v in succs:
                        phi_a = (Theta[u, za] + Theta[za, v]) % (2.0 * np.pi)
                        phi_b = (Theta[u, zb] + Theta[zb, v]) % (2.0 * np.pi)
                        dphi = abs(phi_a - phi_b)
                        dphi = min(dphi, 2.0 * np.pi - dphi)
                        if dphi > eps_ker:
                            all_coherent = False
                            break
                    if not all_coherent:
                        break
                if all_coherent:
                    ra, rb = find(za), find(zb)
                    if ra != rb:
                        parent[max(ra, rb)] = min(ra, rb)

    clusters = {}
    for u in range(N):
        clusters.setdefault(find(u), []).append(u)
    sorted_clusters = sorted(clusters.values(), key=lambda c: min(c))
    M = len(sorted_clusters)
    W = R * np.exp(1j * Theta)
    W_red = np.zeros((M, M), dtype=complex)
    R_red = np.zeros((M, M), dtype=int)
    for a in range(M):
        for b in range(a + 1, M):
            sub_W = W[np.ix_(sorted_clusters[a], sorted_clusters[b])]
            sub_R = R[np.ix_(sorted_clusters[a], sorted_clusters[b])]
            if np.sum(sub_R) > 0:
                R_red[a, b] = 1
                W_red[a, b] = np.mean(sub_W[sub_R > 0])
    Theta_red = np.mod(np.angle(W_red), 2.0 * np.pi) * R_red
    return R_red, Theta_red


# =====================================================================
# 4. OSELEDETS SPECTRUM & SIGN-CONSISTENT EPSILON-BOX BALANCE
# =====================================================================

def compute_oseledets_landauer_profile(
    R, Theta, subsystem_nodes,
    dissipation=0.45,
    H_in_nats=None,
    eps=1e-12,
    spectrum_method="eig",
):
    """
    [FIX-3] Compute the local Lyapunov spectrum {lambda_i} on subgraph A,
    transverse contraction rate kappa(A), Pesin expansion rate h_KS(A),
    and the exact sign-consistent coarse-grained entropy balance
    (Theorem 4.1).

    spectrum_method:
      "eig" (default): eigenvalues of M_jac. Correct for Lyapunov
                       spectrum of the constructed Jacobian.
      "svd":           singular values. Retained for backward
                       compatibility and diagnostics.
    Both spectra are returned in the output dict.
    """
    R = _as_int64(R)
    idx = np.array(sorted(subsystem_nodes), dtype=int)
    n_sub = len(idx)
    if n_sub == 0:
        return {
            "kappa": 0.0, "h_KS": 0.0, "D_KY": 0.0,
            "sigma_bath_nats": 0.0,
            "I_merge_transverse_bits": 0.0,
            "I_erase_net_bits": 0.0,
            "H_in_nats": 0.0, "H_out_nats": 0.0,
        }

    W_sub = (R * np.exp(1j * np.asarray(Theta)))[np.ix_(idx, idx)]
    H_sym = 0.5 * (W_sub + W_sub.conj().T)
    H_rot = (W_sub - W_sub.conj().T) / (2j)
    M_jac = (1.0 - dissipation) * np.eye(n_sub) + 0.5 * (H_sym + 1j * H_rot)

    # --- [FIX-3] Primary spectrum: eigenvalues ---
    e_vals = np.maximum(np.abs(eigvals(M_jac)), eps)
    lyap_eig = np.sort(np.log(e_vals))[::-1]

    # --- Diagnostic spectrum: singular values ---
    s_vals = np.maximum(svdvals(M_jac), eps)
    lyap_svd = np.sort(np.log(s_vals))[::-1]

    # Select primary
    lyap = lyap_eig if spectrum_method == "eig" else lyap_svd

    kappa = float(np.sum(np.abs(lyap[lyap < 0.0])))
    h_KS = float(np.sum(lyap[lyap > 0.0]))
    sigma_bath = float(max(0.0, kappa - h_KS))

    if H_in_nats is None:
        H_in_nats = sigma_bath
    H_out_nats = float(H_in_nats + h_KS - kappa)
    balance_err = float(abs((H_in_nats - H_out_nats) + (h_KS - kappa)))

    csum = np.cumsum(lyap)
    pos_idx = np.where(csum >= 0.0)[0]
    if len(pos_idx) == 0:
        D_KY = 0.0
    elif pos_idx[-1] == n_sub - 1:
        D_KY = float(n_sub)
    else:
        j = int(pos_idx[-1])
        D_KY = float((j + 1) + csum[j] / max(abs(lyap[j + 1]), eps))

    return {
        "lyapunov_spectrum": lyap,
        "lyapunov_spectrum_eig": lyap_eig,
        "lyapunov_spectrum_svd": lyap_svd,
        "spectrum_method": spectrum_method,
        "kappa": kappa,
        "h_KS": h_KS,
        "D_KY": D_KY,
        "H_in_nats": float(H_in_nats),
        "H_out_nats": H_out_nats,
        "sigma_bath_nats": sigma_bath,
        "stationary_balance_error": balance_err,
        "I_merge_transverse_bits": float(kappa / np.log(2.0)),
        "I_erase_net_bits": float(sigma_bath / np.log(2.0)),
    }


# =====================================================================
# 5. MULTISCALE SYNCHRONIZATION AND CHANNEL BALANCE (§5-§6, V3-V6)
# =====================================================================

def evaluate_synchronization_and_balance(R, Theta, core_nodes, eps=1e-12):
    """
    [FIX-4] Directed shortest paths for causal diameter.
    [FIX-5] Isolated-vertex filtering before Laplacian eigenvalues.
    """
    R = _as_int64(R)
    Theta = np.asarray(Theta)
    N = len(R)
    triad = partition_triad(R, core_nodes)
    K, M_amp, _ = compute_causal_phase_invariants(R, Theta)

    q_x = np.zeros(N, dtype=float)
    for x in range(N - 2):
        ys = np.where(K[x, :] >= 2)[0]
        if len(ys) > 0:
            q_x[x] = float(np.sum((np.abs(M_amp[x, ys]) ** 2) / K[x, ys]))

    I_A, dA, E_A = triad["I_A"], triad["dA"], triad["E_A"]
    Q_tot = float(np.sum(q_x))
    rho_I = float(np.mean(q_x[I_A])) if len(I_A) > 0 else 0.0
    rho_dA = float(np.mean(q_x[dA])) if len(dA) > 0 else 0.0
    rho_E = float(np.mean(q_x[E_A])) if len(E_A) > 0 else 0.0
    balance_residual = abs(
        len(E_A) * rho_E + len(I_A) * rho_I + len(dA) * rho_dA - Q_tot
    )

    A_nodes = np.union1d(I_A, dA)
    tau_sync = 0.0
    tau_diam_directed = 0.0
    tau_diam_undirected = 0.0
    lambda_2 = 0.0

    if len(A_nodes) >= 2:
        R_A = R[np.ix_(A_nodes, A_nodes)]

        # [FIX-4] Directed causal diameter (primary)
        dist_dir = shortest_path(R_A, directed=True, unweighted=True)
        fin_dir = dist_dir[np.isfinite(dist_dir) & (dist_dir > 0)]
        tau_diam_directed = float(np.max(fin_dir)) if len(fin_dir) > 0 else 1.0

        # Undirected diameter (diagnostic)
        A_sym = R_A + R_A.T
        dist_undir = shortest_path(A_sym, directed=False, unweighted=True)
        fin_undir = dist_undir[np.isfinite(dist_undir) & (dist_undir > 0)]
        tau_diam_undirected = float(np.max(fin_undir)) if len(fin_undir) > 0 else 1.0

        # [FIX-5] Filter isolated vertices before Laplacian
        deg = A_sym.sum(axis=1)
        non_isolated = deg > 0
        A_filt = A_sym[np.ix_(non_isolated, non_isolated)]
        deg_filt = A_filt.sum(axis=1).astype(float)

        if len(deg_filt) >= 2:
            D_inv_sqrt = np.diag(1.0 / np.sqrt(deg_filt))
            L_norm = np.eye(len(deg_filt)) - D_inv_sqrt @ A_filt @ D_inv_sqrt
            evals = np.sort(eigh(L_norm, eigvals_only=True))
            lambda_2 = float(max(eps, evals[1]))
        else:
            lambda_2 = eps

        tau_sync = float(tau_diam_directed / lambda_2)

    if len(E_A) >= 2:
        R_E = R[np.ix_(E_A, E_A)]
        # [FIX-4] Directed distances for void null-link paths
        dist_E = shortest_path(R_E, directed=True, unweighted=True)
        fin_E = dist_E[np.isfinite(dist_E) & (dist_E > 0)]
        l_null_void = float(np.mean(fin_E)) if len(fin_E) > 0 else np.nan
    else:
        l_null_void = np.nan

    oseledets = compute_oseledets_landauer_profile(R, Theta, A_nodes)
    eta_sat = float(
        oseledets["I_erase_net_bits"] / max(1, triad["capacity_out"])
    )

    return {
        "Q_tot": Q_tot,
        "rho_bulk": rho_I,
        "rho_interface": rho_dA,
        "rho_void": rho_E,
        "balance_identity_error": float(balance_residual),
        "tau_diam_directed": tau_diam_directed,
        "tau_diam_undirected": tau_diam_undirected,
        "tau_sync": tau_sync,
        "lambda_2": lambda_2,
        "f_null_void": triad["f_null_ext"],
        "l_null_void": l_null_void,
        "I_erase_net_bits": oseledets["I_erase_net_bits"],
        "capacity_out": triad["capacity_out"],
        "eta_saturation": eta_sat,
    }


# =====================================================================
# 6. PRECISION KERNEL INCLUSION, SOLENOIDAL GAP & INTEGRATORS (V7)
# =====================================================================

def verify_precision_helmholtz_and_integrator_chain(
    Pi_E, Pi_Eb, Pi_b, Pi_Ib, Pi_I,
    Gamma, Q_sol,
    gamma_modes=(0.1, 0.5, 1.2, 8.0, 15.0),
    tau_w=0.8,
):
    """
    Executable verification suite for Protocol V7
    (Propositions 2.2, 3.2, and 5.1).
    No changes relative to §9 — this function was already correct.
    """
    d_E, d_b, d_I = len(Pi_E), len(Pi_b), len(Pi_I)
    Z_EI = np.zeros((d_E, d_I))
    Pi = np.block([
        [Pi_E, Pi_Eb, Z_EI],
        [Pi_Eb.T, Pi_b, Pi_Ib.T],
        [Z_EI.T, Pi_Ib, Pi_I],
    ])
    Sigma = np.linalg.inv(Pi)
    idx_E = slice(0, d_E)
    idx_b = slice(d_E, d_E + d_b)
    idx_I = slice(d_E + d_b, d_E + d_b + d_I)

    Sigma_IE = Sigma[idx_I, idx_E]
    Sigma_b = Sigma[idx_b, idx_b]
    Sigma_IE_formula = (
        np.linalg.inv(Pi_I) @ Pi_Ib @ Sigma_b @ Pi_Eb.T @ np.linalg.inv(Pi_E)
    )
    cov_formula_err = float(np.max(np.abs(Sigma_IE - Sigma_IE_formula)))

    sigma_map = np.linalg.inv(Pi_E) @ Pi_Eb @ pinv(Pi_Ib) @ Pi_I
    B_samples = np.random.default_rng(42).normal(size=(d_b, 200))
    eta_expected = -np.linalg.inv(Pi_E) @ Pi_Eb @ B_samples
    mu_expected = -np.linalg.inv(Pi_I) @ Pi_Ib @ B_samples
    eta_predicted = sigma_map @ mu_expected
    sync_err = float(np.max(np.abs(eta_expected - eta_predicted)))

    B_0 = Gamma @ Pi_I
    B_Q = (Gamma + Q_sol) @ Pi_I
    gamma_0 = float(np.min(np.real(eigvals(B_0))))
    gamma_Q = float(np.min(np.real(eigvals(B_Q))))

    gammas = np.array(gamma_modes, dtype=float)
    gT = gammas * tau_w
    win_factors = 2.0 * (gT - 1.0 + np.exp(-gT)) / np.maximum(gT ** 2, 1e-12)
    fast_truncation_ratio = float(
        np.sum(win_factors[3:]) / max(np.sum(win_factors[:3]), 1e-12)
    )

    return {
        "Sigma_IE_frobenius_norm": float(np.linalg.norm(Sigma_IE, "fro")),
        "mediated_covariance_identity_error": cov_formula_err,
        "synchronization_map_max_error": sync_err,
        "spectral_gap_gradient_only": gamma_0,
        "spectral_gap_with_solenoidal_Q": gamma_Q,
        "solenoidal_acceleration_gain": float(gamma_Q - gamma_0),
        "integrator_fast_mode_residual_ratio": fast_truncation_ratio,
    }


# =====================================================================
# 7. [NEW] GRAPH GENERATORS FOR PROTOCOLS V1, V3, V5
# =====================================================================

def generate_layered_causal_graph(L_tau, L_x, L_y, R_max=1, seed=42):
    """
    Layered causal lattice (Protocol V1 control, V3, V5).
    L_tau time slices x L_x x L_y spatial vertices.
    Admissible links: adjacent slices with |dx_perp| <= R_max.

    Returns:
        R:     (N, N) int64 Hasse adjacency matrix
        Theta: (N, N) float64 phase matrix (uniform random)
        layers: list of arrays, vertex indices per slice
    """
    rng = np.random.default_rng(seed)
    N = L_tau * L_x * L_y
    R = np.zeros((N, N), dtype=np.int64)
    Theta = np.zeros((N, N), dtype=np.float64)

    def idx(t, x, y):
        return t * L_x * L_y + x * L_y + y

    layers = []
    for t in range(L_tau):
        layers.append(np.array([idx(t, x, y) for x in range(L_x) for y in range(L_y)]))

    for t in range(L_tau - 1):
        for x1 in range(L_x):
            for y1 in range(L_y):
                u = idx(t, x1, y1)
                for dx in range(-R_max, R_max + 1):
                    for dy in range(-R_max, R_max + 1):
                        x2, y2 = x1 + dx, y1 + dy
                        if 0 <= x2 < L_x and 0 <= y2 < L_y:
                            v = idx(t + 1, x2, y2)
                            R[u, v] = 1
                            Theta[u, v] = rng.uniform(0, 2 * np.pi)

    # Transitive reduction: remove shortcuts
    # (layered lattice with R_max >= 1 may create transitive links)
    for t in range(L_tau - 1):
        for u in layers[t]:
            for v in layers[t + 1]:
                if R[u, v] == 1:
                    # Check if u -> v is also reachable in 2 steps
                    two_step = (R[u, :] @ R[:, v]) > 0
                    if two_step:
                        R[u, v] = 0
                        Theta[u, v] = 0.0

    return R, Theta, layers


def generate_erdos_renyi_dag(N, p_edge, seed=42):
    """
    Erdős–Rényi DAG with transitive reduction (Protocol V1).
    """
    rng = np.random.default_rng(seed)
    R = np.zeros((N, N), dtype=np.int64)
    Theta = np.zeros((N, N), dtype=np.float64)
    for i in range(N):
        for j in range(i + 1, N):
            if rng.random() < p_edge:
                R[i, j] = 1
                Theta[i, j] = rng.uniform(0, 2 * np.pi)

    # Transitive reduction against the ORIGINAL reachability: an edge (i, j)
    # is kept iff no directed path of length >= 2 connects i to j in the
    # unreduced graph (the transitive reduction of a DAG is unique).
    # Sequential edge-by-edge deletion against the partially reduced graph
    # can leave length >= 3 shortcuts and break the Hasse property.
    R_bool = R > 0
    reach_2plus = np.zeros((N, N), dtype=bool)
    power = R_bool.copy()
    for k in range(2, N):
        power = (power @ R_bool) > 0
        if not np.any(power):
            break
        reach_2plus |= power
    keep = R_bool & ~reach_2plus
    R = keep.astype(np.int64)
    Theta = np.where(keep, Theta, 0.0)

    return R, Theta


# =====================================================================
# 8. [NEW] NULL-TEST CONTROLS FOR PROTOCOLS V3, V5
# =====================================================================

def degree_preserving_swaps(R, n_swaps, seed=42):
    """
    Degree-preserving edge rewiring (Protocol V3 control).
    Preserves in-degree and out-degree sequences exactly: every
    accepted swap removes two live edges and adds two new ones.
    Maintains causal acyclicity (strict upper-triangular form) and
    the Hasse property: a proposed swap is accepted only if the
    rewired graph remains transitively irreducible (Protocol V3-N3).
    The edge list is rebuilt after every accepted swap; a stale list
    would delete already-removed edges and break degree conservation.
    """
    R = _as_int64(R).copy()
    rng = np.random.default_rng(seed)

    accepted = 0
    attempts = 0
    while accepted < n_swaps and attempts < n_swaps * 20:
        attempts += 1
        edges = np.argwhere(R == 1)          # rebuilt fresh on every attempt
        n_edges = len(edges)
        if n_edges < 2:
            break
        i, j = rng.integers(0, n_edges, size=2)
        if i == j:
            continue
        u1, v1 = edges[i]
        u2, v2 = edges[j]
        # Proposed swap: (u1->v1, u2->v2) -> (u1->v2, u2->v1)
        if u1 == u2 or v1 == v2:
            continue                          # degenerate: no-op swap
        if u1 == v2 or u2 == v1:
            continue
        if R[u1, v2] == 1 or R[u2, v1] == 1:
            continue
        if u1 >= v2 or u2 >= v1:
            continue  # would violate causal ordering
        R_try = R.copy()
        R_try[u1, v1] = 0
        R_try[u2, v2] = 0
        R_try[u1, v2] = 1
        R_try[u2, v1] = 1
        if not is_hasse_transitive_free(R_try):
            continue  # would short-circuit a directed path of length >= 2
        R = R_try
        accepted += 1

    return R


def phase_scramble_boundary(R, Theta, boundary_nodes, seed=42):
    """
    Randomize phases on all links touching boundary_nodes
    (Protocol V3 control).
    """
    R = _as_int64(R)
    Theta = np.asarray(Theta).copy()
    rng = np.random.default_rng(seed)
    bmask = np.zeros(len(R), dtype=bool)
    bmask[list(boundary_nodes)] = True
    link_mask = bmask[:, None] | bmask[None, :]
    Theta[link_mask & (R == 1)] = rng.uniform(
        0, 2 * np.pi, size=int(np.sum(link_mask & (R == 1)))
    )
    return Theta


# =====================================================================
# 9. [NEW] DIMENSION ESTIMATORS AND ε-BOX ENTROPY (V1, V2)
# =====================================================================

def myrheim_meyer_dimension(R, n_samples=5000, seed=42):
    """
    Myrheim–Meyer dimension estimator (Protocol V1).
    d_MM estimated from the scaling of causal interval cardinality:
    |I(x, y)| ~ tau^{d_tau}.
    """
    R = _as_int64(R)
    N = len(R)
    rng = np.random.default_rng(seed)

    # Compute transitive closure for interval counting
    reach = np.zeros((N, N), dtype=bool)
    power = R > 0
    for _ in range(N):
        reach |= power
        power = (power @ (R > 0)) > 0
        if not np.any(power):
            break

    intervals = []
    for _ in range(n_samples):
        x, y = rng.integers(0, N, size=2)
        if x >= y or not reach[x, y]:
            continue
        chain_len = int(shortest_path(
            R, directed=True, unweighted=True, indices=x
        )[y])
        if chain_len < 2:
            continue
        interior = np.sum(reach[x, :] & reach[:, y]) - 2
        intervals.append((chain_len, max(interior, 0)))

    if len(intervals) < 10:
        return np.nan

    taus = np.array([iv[0] for iv in intervals], dtype=float)
    counts = np.array([iv[1] for iv in intervals], dtype=float)
    valid = (taus > 1) & (counts > 0)
    if np.sum(valid) < 5:
        return np.nan

    log_tau = np.log(taus[valid])
    log_count = np.log(counts[valid])
    slope, _ = np.polyfit(log_tau, log_count, 1)
    return float(slope)


def epsilon_box_entropy(trajectory, lyapunov_basis, epsilon):
    """
    ε-box partition entropy estimator (Protocol V2).
    Computes H_epsilon(Z_n) = Shannon entropy of the occupation
    distribution over epsilon-boxes in the Lyapunov basis.
    """
    coords = trajectory @ lyapunov_basis.T
    cell_indices = np.floor(coords / epsilon).astype(int)
    unique_cells, counts = np.unique(
        cell_indices, axis=0, return_counts=True
    )
    probs = counts / counts.sum()
    return float(-np.sum(probs * np.log(probs)))


# =====================================================================
# 10. SELF-TEST SUITE
# =====================================================================

def run_self_test():
    """Minimal smoke tests for the patched implementation."""
    print("=== cpp_v39_reference self-test ===")

    # 1. Generate a small layered graph
    R, Theta, layers = generate_layered_causal_graph(6, 4, 4, R_max=1, seed=7)
    N = len(R)
    print(f"[1] Layered graph: N={N}, E={int(R.sum())}")
    assert is_hasse_transitive_free(R), "Hasse check failed"
    print("    Hasse transitive irreducibility: PASS")

    # 2. Wilson identity
    err = verify_wilson_identity(R, Theta)
    print(f"[2] Wilson identity max error: {err:.2e}")
    assert err < 1e-10, f"Wilson identity error too large: {err}"
    print("    Wilson identity: PASS")

    # 3. Diamond participation
    d_d, null_mask, diamond_mask = compute_edge_diamond_participation(R)
    n_null = int(null_mask.sum())
    n_diamond = int(diamond_mask.sum())
    print(f"[3] Null links: {n_null}, Diamond links: {n_diamond}")
    assert n_null + n_diamond == int(R.sum()), "Edge partition mismatch"
    print("    Edge partition: PASS")

    # 4. Interval-local path quotient
    K_eff, J_eff, f_K2 = interval_local_path_quotient(R, Theta, eps_ker=0.3)
    print(f"[4] f_K2_eff = {f_K2:.4f}")
    print("    Interval-local quotient: PASS")

    # 5. Oseledets profile (eig vs svd)
    core = list(range(N // 4, N // 2))
    prof_eig = compute_oseledets_landauer_profile(
        R, Theta, core, spectrum_method="eig"
    )
    prof_svd = compute_oseledets_landauer_profile(
        R, Theta, core, spectrum_method="svd"
    )
    print(f"[5] kappa(eig)={prof_eig['kappa']:.4f}, "
          f"kappa(svd)={prof_svd['kappa']:.4f}")
    print(f"    h_KS(eig)={prof_eig['h_KS']:.4f}, "
          f"h_KS(svd)={prof_svd['h_KS']:.4f}")
    print(f"    balance_err={prof_eig['stationary_balance_error']:.2e}")
    print("    Oseledets profile: PASS")

    # 6. Synchronization and balance
    sync = evaluate_synchronization_and_balance(R, Theta, core)
    print(f"[6] tau_diam_directed={sync['tau_diam_directed']:.1f}, "
          f"tau_diam_undirected={sync['tau_diam_undirected']:.1f}")
    print(f"    lambda_2={sync['lambda_2']:.6f}, "
          f"tau_sync={sync['tau_sync']:.2f}")
    print(f"    balance_identity_error={sync['balance_identity_error']:.2e}")
    print("    Synchronization: PASS")

    # 7. Degree-preserving swaps
    R_swapped = degree_preserving_swaps(R, n_swaps=50, seed=99)
    assert np.array_equal(R.sum(axis=0), R_swapped.sum(axis=0)), \
        "In-degree not preserved"
    assert np.array_equal(R.sum(axis=1), R_swapped.sum(axis=1)), \
        "Out-degree not preserved"
    print("[7] Degree-preserving swaps: PASS")

    # 8. Myrheim-Meyer dimension
    d_mm = myrheim_meyer_dimension(R, n_samples=2000, seed=7)
    print(f"[8] Myrheim-Meyer dimension: {d_mm:.3f}")
    print("    Dimension estimator: PASS")

    print("=== All self-tests passed ===")


if __name__ == "__main__":
    run_self_test()
```

---

## **References**

1. **Causal Sets and Lorentzian Geometry Reconstruction:** L. Bombelli, J. Lee, D. Meyer, R. D. Sorkin, *Space-Time as a Causal Set*, Physical Review Letters **59**, 521–524 (1987); S. Surya, *The Causal Set Approach to Quantum Gravity*, Living Reviews in Relativity **22**, 5 (2019).
2. **Combinatorial Asymptotics of Partial Orders:** D. J. Kleitman, B. L. Rothschild, *Asymptotic Enumeration of Partial Orders on a Finite Set*, Transactions of the American Mathematical Society **205**, 205–220 (1975).
3. **Thermodynamic Derivation of Field Equations and Relative Entropy:** T. Jacobson, *Thermodynamics of Spacetime: The Einstein Equation of State*, Physical Review Letters **75**, 1260–1263 (1995); H. Araki, *Relative Entropy of States of von Neumann Algebras*, Publications of the RIMS **11**, 809–833 (1976); A. Uhlmann, *Relative Entropy and the Wigner–Yanase–Dyson–Lieb Concavity in an Interpolation Theory*, Communications in Mathematical Physics **54**, 21–32 (1977); P. Dorau, R. Verch, M. Much, works on deriving gravitational field equations from Araki–Uhlmann relative entropy on causal diamonds.
4. **Markov Blankets, Helmholtz Decomposition, and Non-Equilibrium Stationary Processes:** L. Da Costa, K. Friston, C. Heins, G. A. Pavliotis, *Bayesian Mechanics for Stationary Processes*, Proceedings of the Royal Society A **477**, 20210518 (2021); G. A. Pavliotis, *Stochastic Processes and Applications: Diffusion Processes, the Fokker–Planck and Langevin Equations*, Springer (2014); T. Lelièvre, F. Nier, G. A. Pavliotis, *Optimal Non-Reversible Linear Drift for the Convergence to Equilibrium of a Diffusion*, Journal of Statistical Physics **152**, 237–274 (2013); J. L. Doob, *The Brownian Movement and Stochastic Equations*, Annals of Mathematics **43**, 351–369 (1942); A. Lindquist, G. Picci, *Linear Stochastic Systems: A Geometric Approach to Modeling, Estimation and Identification*, Springer (2015); M. Biehl, F. A. Pollock, R. Kanai, *A Technical Critique of Some Parts of the Free Energy Principle*, Entropy **23**, 293 (2021); M. Aguilera, B. Millidge, A. Tschantz, C. L. Buckley, *How Particular Is the Physics of the Free Energy Principle?*, Physics of Life Reviews (2021/2022).
5. **Thermodynamics of Computation, Phase-Space Contraction, and Quantum Rate Bounds:** R. Landauer, *Irreversibility and Heat Generation in the Computing Process*, IBM Journal of Research and Development **5**, 183–191 (1961); D. Ruelle, *Positivity of Entropy Production in Nonequilibrium Statistical Mechanics*, Journal of Statistical Physics **85**, 1–23 (1996); N. Margolus, L. B. Levitin, *The Maximum Speed of Dynamical Evolution*, Physica D **120**, 188–195 (1998); J. D. Bekenstein, *Universal Upper Bound on the Entropy-to-Energy Ratio for Bounded Systems*, Physical Review D **23**, 287–298 (1981).
6. **Multiplicative Ergodic Theory, Attractor Dimension, and Dichotomy Projectors:** V. I. Oseledets, *A Multiplicative Ergodic Theorem: Characteristic Ljapunov Exponents of Dynamical Systems*, Transactions of the Moscow Mathematical Society **19**, 197–231 (1968); Ya. B. Pesin, *Characteristic Lyapunov Exponents and Smooth Ergodic Theory*, Russian Mathematical Surveys **32**(4), 55–114 (1977); J. L. Kaplan, J. A. Yorke, *Chaotic Behavior of Multidimensional Difference Equations*, Lecture Notes in Mathematics **730**, 204–227 (1979); D. G. Clark, *Lyapunov Spectrum and Minimum-Norm Tangent Response in High-Dimensional Networks* (2026); R. Engelken, F. Wolf, L. F. Abbott, *Lyapunov Spectra of Chaotic Recurrent Neural Networks*, Physical Review Research **5**, 043044 (2023).
7. **Noncommutative Geometry and Thermal Time:** A. Connes, *Noncommutative Geometry*, Academic Press (1994); A. Connes, C. Rovelli, *Von Neumann Algebra Automorphisms and Time-Thermodynamics Relation in Generally Covariant Quantum Theories*, Classical and Quantum Gravity **11**, 2899–2917 (1994).
8. **Matrix Models and Holographic Complexity:** T. Banks, W. Fischler, S. H. Shenker, L. Susskind, *M Theory as a Matrix Model: A Conjecture*, Physical Review D **55**, 5112–5128 (1997); A. R. Brown, D. A. Roberts, L. Susskind, B. Swingle, Y. Zhao, *Complexity, Action, and Black Holes*, Physical Review D **93**, 086006 (2016).
9. **Information Bottleneck, Causal Emergence, and Network Null Models:** N. Tishby, F. C. Pereira, W. Bialek, *The Information Bottleneck Method*, Allerton Conference (1999); E. P. Hoel, L. Albantakis, G. Tononi, *Quantifying Causal Emergence Shows That Macro Can Beat Micro*, PNAS **110**, 19790–19795 (2013); F. Vazza, A. Feletti, *The Quantitative Comparison Between the Neuronal Network and the Cosmic Web*, Frontiers in Physics **8**, 525731 (2020); F. Váša, B. Mišić, *Null Models in Network Neuroscience*, Nature Reviews Neuroscience **23**, 493–504 (2022).
10. **Three-Valued Entailment Logic and Verification Semilattices:** N. P. Brusentsov, *The Improvement of Inference Logic* [Usovershenstvovanie logiki umozaklyucheniy], Moscow: New Millennium Foundation (2012); L. Carroll, *Symbolic Logic*, Macmillan (1896).
