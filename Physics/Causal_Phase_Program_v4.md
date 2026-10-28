# **Causal Phase Program, Version 4.0 — Mathematical Invariants of Multiscale Structuring: Unified Model, Hard Locality Constraints, Exact Entropy Balance, and Field Back-Reaction on the Graph**

**Author:** Vladimir Yakunin  
**Version:** 4.0  
**Date:** 2026-10-22  
**Status:** Self-contained formal specification and research program. Strictly separates definitions, mathematical consequences within the model, and empirically testable physical hypotheses. The results of executed numerical verifications are recorded in §10; no statement of this document relies on unexecuted computations unless it is marked `UNDECIDED`.  
**Supersedes:** `Causal_Phase_Program_v3.md` (v3.9, October 21, 2026; removed from the repository). Version 4.0 consolidates the post-3.9 revision cycle; the complete difference from v3.9 is summarized in the table below.  
**Companion:** *Latent Agency Framework v2.1* (`Reasoning/Latent_Agency_Framework.md`, October 21, 2026) — shared mathematical apparatus: Markov blankets and boundary kernel inclusion, Helmholtz decomposition, integrator chains of generalized coordinates.  
**Normative parent (verdict semantics):** *Modified Brusentsov Entailment Logic* (`Reasoning/Modified_Brusentsov_Entailment_Logic.md`). Sections 0 and 8 of this document are a domain instantiation of the canonical four-valued verdict calculus $`V_4`$, reproduced here in full so that reading this specification requires no external documents.

---

## **Summary Table of Architectural Changes (from version 3.9 to version 4.0)**

| № | Node / problem in v3.9 | Mathematical resolution in v4.0 | Section |
| :--- | :--- | :--- | :--- |
| 1 | Two disconnected formal layers: the graph with phases $`(R,\Theta)`$ and an abstract Gaussian layer $`(\Pi, Q, G_R)`$ with no explicit formula through the transport matrix $`W`$. | **Unified model:** a complex Gaussian field on the Hasse graph with precision matrix $`\Pi = m^2 I + L_\Theta`$ (magnetic Laplacian) and solenoidal drift $`Q_W = \tfrac{\beta}{2}(W-W^\dagger)`$. Markov screening becomes a theorem of the model, and kernel inclusion acquires a graph criterion via matchings (Corollary 2.3). | §2.4, §3.5 |
| 2 | The statistic $`f_{K^{\mathrm{eff}}=2}`$ measured phase noise rather than geometry (Proposition 1.2: zero-temperature minimizers are gauge-flat), and without a diamond-density threshold the two-layer Kleitman–Rothschild graphs had zero cost; the derivation of “3+1” from a single binary diamond rested on hidden rank assumptions. | **Hard admissibility conditions (L0)–(L4)** and a proof of the impossibility of suppressing the two-layer sector $`\mathcal{T}_2`$ by soft penalties in $`K, J, \|C\|_F`$ (Proposition 3.2). The hypercube counterexample is proved (Proposition 3.5): binary diamonds $`K_{xy}\le 2`$ tile lattices of every dimension $`d\ge 2`$, and the dimension is encoded in their density $`\binom{d}{2}`$. | §3.2–3.4, §3.6, V1 |
| 3 | The output entropy $`H_{\mathrm{out}}`$ was defined from the balance identity itself, and singular values of a constant surrogate Jacobian were used instead of Lyapunov exponents. | **Exact entropy-balance theorem (Theorem 4.3)** for injective random dynamical systems with additive noise: $`\Delta_{\mathrm{noise}} = -\sum_i\lambda_i = \kappa - h_+`$. The spectrum is computed by the Benettin (QR) method and the entropies independently by the Kozachenko–Leonenko $`k`$-NN estimator. | §4, V2, §9 |
| 4 | The scale-separation window $`(\gamma_2^{-1}, \gamma_3^{-1})`$ was empty for $`\gamma_2 \ll \gamma_3`$, and the ratio $`R_{AB}^{(\ell)}`$ admitted a $`0/0`$ division on flat connections. | The coarse-graining window is corrected to the non-empty $`\tau_w^{(\ell)} \in (\gamma_3^{-1}, \gamma_2^{-1})`$ with $`\gamma_3^{-1} \ll \tau_w^{(\ell)} \ll \gamma_2^{-1}`$ (§5.2). The domain of $`R_{AB}^{(\ell)}`$ is restricted by the condition $`\Delta N_B^{(\ell)} \neq 0`$ (§5.1). | §5.1, §5.2 |
| 5 | Protocols V3 and V4 lacked a law of field back-reaction on the graph $`R`$ and a definition of $`\mathscr{S}_{\mathrm{interface}}`; the sign of $`\eta_{\mathrm{field}}`$, the contribution of bipartite 4-cycles $`K_{2,2}`$, and the distinction between the equilibrium regime of V3 and the non-equilibrium regime of V2 remained unresolved. | **Exact field closure (§6.2–6.3):** the rank-1 factorization and the Woodbury formula for edge swaps are proved (Proposition 6.2), the triangle-free loop expansion with diamonds and $`K_{2,2}`$ crowns at order $`\ell=4`$ (Proposition 6.3), and the triadic Schur decomposition defining $`\mathscr{S}_{\mathrm{interface}} > 0`$ (Proposition 6.4). The canonical bosonic sign $`\eta_{\mathrm{field}} > 0`$ ($`\eta_{\mathrm{field}} = 1`$) is fixed, and the equilibrium test V3 is strictly separated from the non-equilibrium test V2. | §4.1, §6.2–6.3, V3, V4 |

---

## **Abstract**

This specification formulates the mathematical apparatus for studying how multiscale structures emerge, maintain stability, and interact in a discrete causal medium of bounded capacity. Instead of postulating a ready-made smooth manifold of fixed dimension, the foundational object is a finite locally finite partial order of events (Bombelli et al., 1987) equipped with unitary phase transport on the immediate causal relations (Hasse links). The unified stochastic model — a complex Gaussian field whose precision matrix is the magnetic Laplacian of this phase-decorated graph — carries all statistical statements and the equations of field back-reaction on the graph.

Any persistent localized subsystem at a selected temporal window and resolution scale is represented as a triad $`(\mathcal{I}_A, \partial A, \mathcal{E}_A)`$: an internal relief (bulk), a bilateral interface of finite capacity, and an external causal synchronization channel.

Eight mathematical results are established, each with an explicitly fixed logical status:

1. **Necessity of hard locality.** The number of partial orders on $`N`$ elements is asymptotically dominated by two- and three-layer orders (Kleitman, Rothschild, 1975). Any statistical weight vanishing on the two-layer sector (including any function of $`K`$, $`J`$, and $`\|C\|_F`$) is incapable of suppressing its entropy. The admissibility constraints — diamond covering, connectivity, bounded valency, and a lower diamond-density threshold — reduce the combinatorial entropy to $`\exp(O(k_{\max}N\ln N))`$ (§3.2). The price of this choice is stated explicitly: Poisson sprinklings of causal sets, whose valency grows without bound in $`N`$ (Carlip, 2024), are excluded from the ensemble.
2. **Edge diamond-participation multiplicity** $`d_\diamond(x,y)`$, written in closed matrix form, partitions the Hasse edges into unbranched null links ($`d_\diamond = 0`$) and diamond-embedded structural links ($`d_\diamond \ge 1`$) (§2.1).
3. **Markov screening and the kernel-inclusion criterion are theorems of the model:** $`\Pi_{\mathcal{I}\mathcal{E}}=0`$ holds by graph locality, the mediated covariance has an exact closed form, and a linear synchronization map across the interface exists if and only if $`\ker\Pi_{\mathcal{I},\partial A}\subseteq\ker\Pi_{\mathcal{E},\partial A}`$; a boundary vertex with no neighbor inside the bulk always violates this condition (§2.4).
4. **The selection of $`K^{\mathrm{eff}}=2`$ is conditional and does not fix the spatial dimension.** Binary diamonds are the most economical carriers of non-zero frustration only in the presence of a lower bound on frustration or on diamond density; moreover, the directed hypercubic lattice of any dimension $`d\ge2`$ consists exclusively of binary diamonds, and the dimension manifests itself in the *density* of diamonds $`\binom{d}{2}`$ per vertex (§3.3–3.4).
5. **Helmholtz decomposition inside the model:** the Hermitian part of the transport operator $`W`$ forms the precision matrix $`\Pi`$, while the anti-Hermitian part $`\tfrac12(W-W^\dagger)=iH_{\mathrm{rot}}`$ defines the solenoidal drift $`Q_W`$; the stationary distribution is preserved, and the relaxation spectral gap satisfies $`\gamma(Q)\ge\gamma(0)`$ (§3.5).
6. **Exact entropy balance.** For a random dynamical system with additive noise and an injective $`C^1`$ map $`G`$, stationarity requires that the differential entropy injected by the noise per step be exactly $`-\sum_i\lambda_i=\kappa-h_+`$; this is a rigorous theorem, independently verified in V2. The Landauer thermodynamic interpretation is separated into a distinct hypothesis (§4).
7. **Synchronization and network architecture.** The realization of boundary spectra by integrator chains is proved for the non-empty scale-separation window $`\tau_w^{(\ell)} \in (\gamma_3^{-1}, \gamma_2^{-1})`$, together with the divergence of the synchronization time of homogeneous $`d`$-dimensional balls under bounded vertex degree; regular bounded-degree expanders (Friedman, 2008) act as the competing shallow alternative that the filamentary (*Cosmic Web*) hypothesis must outperform in V5 (§5).
8. **Exact field back-reaction on the graph and the triadic Schur decomposition.** Integrating out the Gaussian bosonic field induces the effective potential $`+\eta_{\mathrm{field}}\ln\det\Pi(R,\Theta)`$ ($`\eta_{\mathrm{field}} > 0`$). Because Hasse graphs are triangle-free, the leading phase-dependent contribution to $`\ln\det\Pi(R,\Theta)`$ arises at order $`\ell=4`$ and reproduces Wilson frustration on 4-cycles (including both directed causal diamonds and bipartite 4-cycles $`K_{2,2}`$); the rank-1 incidence factorization yields an exact $`2\times 2`$ Woodbury law for edge swaps; and Markov screening $`\Pi_{\mathcal{I}\mathcal{E}}=0`$ generates the exact triadic Schur decomposition $`\ln\det\Pi = \ln\det\Pi_{\mathcal{I}} + \ln\det\Pi_{\mathcal{E}} + \ln\det S_{\partial A}`$ defining the interface functional for V3 and V4 (§6.2–6.3).

All statements are classified in the four-valued verification space $`V_4=\{\mathrm{FOLLOW},\mathrm{OMIT},\mathrm{UNDECIDED},\mathrm{NULL}\}`$. Section 7 describes seven computational protocols (V1–V7), Section 9 gives the reference Python implementation, and Section 10 records the results of the executed numerical checks.

---

## **0. Methodological Standard and the Four-Valued Verdict Calculus `V_4`**

Every statement of this specification is evaluated in the four-valued verdict space (Brusentsov, 2012):

```math
V_4 = \bigl\{\mathrm{FOLLOW}\ (+1),\; \mathrm{OMIT}\ (0),\; \mathrm{UNDECIDED}\ (U),\; \mathrm{NULL}\ (-1)\bigr\},
```
ordered by the strict linear dominance semilattice under conjunctive aggregation ($`\otimes = \max_{\succ_V}`$):

```math
\mathrm{NULL}\ (-1) \;\succ_V\; \mathrm{UNDECIDED}\ (U) \;\succ_V\; \mathrm{OMIT}\ (0) \;\succ_V\; \mathrm{FOLLOW}\ (+1).
```
Status assignment rules in this document:
- **`FOLLOW` ($`+1`$):** assigned exclusively to (a) internally consistent formal definitions and (b) mathematical propositions whose conclusions follow deductively from the premises explicitly stated in the formulation. A `FOLLOW` status on an implication $`P \implies Q`$ certifies the validity of the deduction itself, but never asserts the physical realizability of the premise $`P`$ or the physical optimality of the chosen functional.
- **`OMIT` ($`0`$):** assigned to (a) degrees of freedom lying in the kernel of the coarse-graining map $`\ker(d\pi_\ell)`$, (b) illustrative heuristics and pedagogical analogies that are nowhere used as proof premises, (c) tautological restatements of established consequences (for example, defining null edges via $`(R_{xy}=1) \land (K_{xy}=0)`$), and (d) continuum extrapolations deferred beyond the discrete model.
- **`UNDECIDED` ($`U`$):** assigned to substantive structural, kinematic, and physical hypotheses that are well-posed inside the model but require numerical certification in Protocols V1–V7 or external physical calibration.
- **`NULL` ($`-1`$):** assigned to statements or software constructs that are mathematically inconsistent, violate gauge or combinatorial invariants, or are refuted by negative controls.

---

## **1. Foundational Causal-Phase Complex**

### **1.1. Partial Order of Events and the Hasse Matrix**

Let $`X = \{1, 2, \dots, N\}`$ be a finite set of events equipped with a strict partial order $`\prec`$ (irreflexive, transitive, acyclic) and numbered topologically so that $`x \prec y \implies x < y`$.

**Definition 1.1 (Causal Interval, Hasse Link, and Antichain).** `[Status: FOLLOW]`
- The *causal interval* between $`x \prec y`$ is the set $`I(x, y) := \{z \in X \mid x \prec z \prec y\}`$.
- A *Hasse link* (immediate causal coverage) $`x \lessdot y`$ holds if and only if $`x \prec y \land I(x, y) = \varnothing`$.
- An *antichain* (spacelike section) is a subset $`S \subset X`$ of pairwise incomparable elements: $`\forall u \neq v \in S, \; u \not\prec v \land v \not\prec u`$.

The Boolean adjacency matrix of Hasse links $`R \in \{0, 1\}^{N \times N}`$ ($`R_{xy} = 1 \iff x \lessdot y`$) is strictly upper-triangular and nilpotent ($`R^N = 0`$). A strictly upper-triangular Boolean matrix $`R`$ is a valid Hasse matrix if and only if it is **transitively irreducible** (no direct edge short-circuits a directed path of length $`\ge 2`$):

```math
\forall x, y \in X: \quad R_{xy} = 1 \implies \bigl((I - R)^{-1} - I - R\bigr)_{xy} = 0.
```
Transitive irreducibility immediately implies two structural identities for any Hasse matrix $`R`$:
1. **Zero waist width on direct links:** $`R_{xy} = 1 \implies K_{xy} := (R^2)_{xy} = 0`$.
2. **Triangle-freeness of the undirected skeleton:** the symmetric skeleton adjacency matrix $`A_{\mathrm{sym}} := R + R^\top`$ contains no cycles of length 3 ($`\operatorname{Tr}(A_{\mathrm{sym}}^3) = 0`$), since any three pairwise adjacent vertices $`u < v < w`$ would satisfy $`R_{uv} = R_{vw} = R_{uw} = 1`$, contradicting $`(R^2)_{uw} = 0`$ on the direct link $`u \lessdot w`$.

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

### **1.4. Cone-Overlap Operators and Irregularity Measure**

The Hermitian positive-semidefinite one-step future and past cone-overlap operators and their skew-Hermitian commutator are:

```math
\Delta_+ := W W^\dagger, \qquad \Delta_- := W^\dagger W, \qquad C := [\Delta_+, \Delta_-], \qquad \bar{L}(W) := \frac{\|C\|_F^2}{1 + \|\Delta_+\|_F^2 \|\Delta_-\|_F^2} \ge 0.
```
### **1.5. Flat Connections: When Phases Are Inert**

**Proposition 1.2 (Gauge-Flat Configurations).** `[Status: FOLLOW]`  
Let $`\theta_{xy} = \chi_y - \chi_x \pmod{2\pi}`$ on every Hasse edge for some set of node phases $`\chi \in [0,2\pi)^N`$ (a purely gauge flat connection). Then $`W = D_\chi^\dagger R D_\chi`$, where $`D_\chi = \operatorname{diag}(e^{i\chi_x})`$, and consequently $`\operatorname{Coh}_{xy}\equiv 1`$, $`J_{xy}\equiv 0`$, while $`K`$, $`|M|`$, and $`\|C\|_F`$ coincide with their values at $`\Theta = 0`$.

*Proof.* $`W_{xy} = e^{-i\chi_x}R_{xy}e^{i\chi_y}`$, hence $`W^2 = D_\chi^\dagger R^2 D_\chi`$ and $`|M_{xy}| = K_{xy}`$; the operators $`\Delta_\pm`$ and their commutator $`C`$ are conjugated by the unitary matrix $`D_\chi`$, which preserves the Frobenius norm. `∎`

**Corollary.** For any functional built from $`K`$, $`J`$, and $`\|C\|_F`$ (as well as for $`\ln\det\Pi(R,\Theta)`$ by Proposition 6.3), the zero-temperature minimizers over free phases are gauge-flat ($`J_{xy}\equiv 0`$), unless frustrated boundary conditions or external flux sources are imposed. Therefore the term “holonomy channel” in this document refers to the *topology* of diamonds (their number and width), while non-zero phase frustration arises from thermal fluctuations or boundary conditions.

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
Every proper connected subsystem $`A \subset X`$ uniquely partitions the event set into three disjoint zones:

```math
X = \mathcal{I}_A \sqcup \partial A \sqcup \mathcal{E}_A,
```
where:
- **Bilateral interface $`\partial A := \partial^- A \cup \partial^+ A`$:** the boundary vertices of $`A`$ having immediate Hasse links with the complement $`\mathcal{E}_A := X \setminus A`$:
```math
\partial^- A := \{y \in A \mid \exists x \in \mathcal{E}_A : R_{xy} = 1\}, \qquad \partial^+ A := \{x \in A \mid \exists y \in \mathcal{E}_A : R_{xy} = 1\}.
```
- **Internal relief (bulk) $`\mathcal{I}_A := A \setminus \partial A`$:** the interior core of subsystem $`A`$, having no direct Hasse links with $`\mathcal{E}_A`$ and interacting with $`\mathcal{E}_A`$ exclusively through the interface $`\partial A`$.
- **External synchronization channel $`\mathcal{E}_A := X \setminus A`$:** the exterior environment coupling $`A`$ to other subsystems. The **fraction of external null links** in $`\mathcal{E}_A`$ is a non-trivial observable:
```math
f_{\mathrm{null}}(\mathcal{E}_A) := \frac{\bigl|\{(x, y) \in \mathcal{E}_A \times \mathcal{E}_A \mid R_{xy} = 1 \land d_\diamond(x, y) = 0\}\bigr|}{\bigl|\{(x, y) \in \mathcal{E}_A \times \mathcal{E}_A \mid R_{xy} = 1\}\bigr|} \in [0, 1].
```

The incoming and outgoing combinatorial capacities of the interface are defined as $`|\partial^- A|_E := \sum_{x \in \mathcal{E}_A, y \in \partial^- A} R_{xy}`$ and $`|\partial^+ A|_E := \sum_{x \in \partial^+ A, y \in \mathcal{E}_A} R_{xy}`$.

**Definition 2.3 (Integration Criterion on Window $`\tau_w`$).** `[Status: FOLLOW]`  
With the symmetric coupling flux $`\mathrm{Dep}(U \leftrightarrow V) := \sum_{u \in U, v \in V} (|W_{uv}|^2 + |W_{vu}|^2)`$, subsystem $`A = \mathcal{I}_A \sqcup \partial A`$ is integrated on window $`\tau_w`$ at threshold $`\theta_I > 0`$ if across all non-trivial binary cuts $`A = A_1 \sqcup A_2`$ the following holds:

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

### **2.4. Unified Model: Complex Gaussian Field with Magnetic-Laplacian Precision**

All statistical statements and field-interaction laws in this specification refer to a single model constructed directly from the matrices $`(R, \Theta)`.

**Definition 2.4 (Magnetic Precision Matrix and the Model Field).** `[Status: FOLLOW]`  
For $`m^2 > 0`$, define:

```math
L_\Theta := D - W - W^\dagger, \qquad D := \operatorname{diag}\Bigl(\sum_y (R_{xy} + R_{yx})\Bigr), \qquad \Pi(R, \Theta) := m^2 I + L_\Theta .
```
The quadratic form $`\psi^\dagger L_\Theta \psi = \sum_{x \lessdot y} |\psi_x - e^{i\theta_{xy}}\psi_y|^2 \ge 0`$ is non-negative, hence $`\Pi \succeq m^2 I`$ is a Hermitian positive-definite matrix; $`L_\Theta`$ is gauge covariant ($`L_{\Theta'} = D_\chi L_\Theta D_\chi^\dagger`$); and the sparsity pattern of $`\Pi`$ coincides exactly with the undirected skeleton of the Hasse graph plus the diagonal. The **model field** $`\psi \in \mathbb{C}^N`$ has the stationary circular complex Gaussian distribution $`\mathcal{CN}(0, \Pi^{-1})`$ with density $`p(\psi \mid R, \Theta) = \pi^{-N} \det\Pi(R,\Theta) \, e^{-\psi^\dagger \Pi(R,\Theta) \psi}`$. The Hermitian part of the transport operator enters $`\Pi`$ as $`\Pi = m^2 I + D - 2H_{\mathrm{sym}}`$.

**Proposition 2.2 (Markov Screening, Mediated Covariance, and Kernel Inclusion in the Model).** `[Status: FOLLOW]`  
Let a subsystem $`A \subset X`$ define the triad $`X = \mathcal{I}_A \sqcup \partial A \sqcup \mathcal{E}_A`$ (Definition 2.2), let $`\mathcal{I}, b, \mathcal{E}`$ be the corresponding index sets, and let $`\Sigma = \Pi^{-1}`$. Then:

1. **Screening by construction:** $`\Pi_{\mathcal{I}\mathcal{E}} = 0`$ and $`\Pi_{\mathcal{E}\mathcal{I}} = 0`$, since there are no direct Hasse links between $`\mathcal{I}_A`$ and $`\mathcal{E}_A`$.
2. **Mediated covariance:** $`\Sigma_{\mathcal{I}\mathcal{E}} = \Pi_{\mathcal{I}}^{-1}\,\Pi_{\mathcal{I}b}\,\Sigma_{b}\,\Pi_{b\mathcal{E}}\,\Pi_{\mathcal{E}}^{-1}`$.
3. **Synchronization map:** denote the conditional expectations $`\bar\mu(b) := \mathbb{E}[\psi_{\mathcal{I}}\mid b] = -\Pi_{\mathcal{I}}^{-1}\Pi_{\mathcal{I}b}\,b`$ and $`\bar\eta(b) := \mathbb{E}[\psi_{\mathcal{E}}\mid b] = -\Pi_{\mathcal{E}}^{-1}\Pi_{\mathcal{E}b}\,b`$. A linear map $`\sigma`$ with the property $`\sigma(\bar\mu(b)) = \bar\eta(b)`$ for all $`b \in \mathbb{C}^{|\partial A|}`$ exists if and only if $`\ker \Pi_{\mathcal{I}b} \subseteq \ker \Pi_{\mathcal{E}b}`$, and in that case is given by $`\sigma = \Pi_{\mathcal{E}}^{-1}\Pi_{\mathcal{E}b}\,\Pi_{\mathcal{I}b}^{+}\,\Pi_{\mathcal{I}}`$ (where $`+`$ denotes the Moore–Penrose pseudoinverse).

*Proof.* (1) follows from Definitions 2.2 and 2.4. (2) For fixed $`b`$, the vectors $`\psi_{\mathcal{I}}`$ and $`\psi_{\mathcal{E}}`$ are conditionally independent with conditional means $`\bar\mu(b)`$ and $`\bar\eta(b)`$; hence $`\Sigma_{\mathcal{I}\mathcal{E}} = \mathbb{E}[\bar\mu(b)\bar\eta(b)^\dagger] = \Pi_{\mathcal{I}}^{-1}\Pi_{\mathcal{I}b}\Sigma_b\Pi_{b\mathcal{E}}\Pi_{\mathcal{E}}^{-1}`$. (3) Since the principal blocks $`\Pi_{\mathcal{I}}, \Pi_{\mathcal{E}}`$ are invertible, $`\ker\bar\mu = \ker\Pi_{\mathcal{I}b}`$ and $`\ker\bar\eta = \ker\Pi_{\mathcal{E}b}`$; a linear map $`\sigma`$ with $`\sigma\circ\bar\mu = \bar\eta`$ exists if and only if $`\ker\Pi_{\mathcal{I}b} \subseteq \ker\Pi_{\mathcal{E}b}`$. `∎`

**Corollary 2.3 (Graph Criterion for Kernel Inclusion).** `[Status: FOLLOW]`  
Since the zones $`\mathcal{I}_A, \partial A, \mathcal{E}_A`$ are pairwise disjoint, the off-diagonal precision blocks are pure transport blocks: $`\Pi_{\mathcal{I}b} = -(W + W^\dagger)_{\mathcal{I}, b}`$ and $`\Pi_{\mathcal{E}b} = -(W + W^\dagger)_{\mathcal{E}, b}`$. Two exact statements follow:
1. **Unconditional violation at a boundary vertex isolated from the bulk:** if some vertex $`u \in \partial A`$ has no Hasse neighbor inside $`\mathcal{I}_A`$, kernel inclusion is violated unconditionally: the column $`u`$ of $`\Pi_{\mathcal{I}b}`$ is identically zero ($`e_u \in \ker\Pi_{\mathcal{I}b}`$), whereas $`\Pi_{\mathcal{E}b}e_u \neq 0`$, since by the definition of the boundary $`u \in \partial A`$ has at least one Hasse link with $`\mathcal{E}_A`$, and every non-zero entry of $`W + W^\dagger`$ has unit modulus (by acyclicity, $`R_{yu}`$ and $`R_{uy}`$ cannot both equal one).
2. **Sufficient condition via injectivity and matching:** kernel inclusion holds for any external block $`\Pi_{\mathcal{E}b}`$ if $`\Pi_{\mathcal{I}b}`$ is injective ($`\ker \Pi_{\mathcal{I}b} = \{0\}`$). For typical (generic) phases $`\Theta`$, the matrix $`\Pi_{\mathcal{I}b}`$ is injective if and only if the bipartite graph of Hasse links between $`\partial A`$ and $`\mathcal{I}_A`$ admits a matching that covers $`\partial A`$ completely (since distinct edges carry independent phases, the generic rank equals the combinatorial Edmonds rank); in particular, $`|\partial A| \le |\mathcal{I}_A|`$ is a necessary condition of injectivity. (For a non-trivial kernel $`\ker\Pi_{\mathcal{I}b} \neq \{0\}`$, kernel inclusion requires the external block $`\Pi_{\mathcal{E}b}`$ to annihilate the entire subspace $`\ker\Pi_{\mathcal{I}b}`$.)

---

## **3. Structuring Principles: Hard Locality, Local Path Reduction, Dimension, and Solenoidal Acceleration**

### **3.1. Informational Minimal Surface and Orthogonal Splitting (context)**

Let $`\pi_\ell: D_\ell \to Y_\ell`$ be a smooth ($`C^1`$) coarse-graining map on a regular stratified carrier $`D_\ell`$ with a positive-definite metric $`h_z`$ on $`T_z D_\ell`$. Minimizing the functional $`\mathcal{L}[\Sigma] = \mathrm{Vol}_h(\Sigma) + \lambda(R_{\mathrm{req}} - I(\Sigma; Y_\ell))`$ at fixed carrier measure density $`\delta(d\mu_\Sigma) = 0`$ yields the stationary balance condition between mean curvature and the normal gradient of the information density `[Status: OMIT — context from the geometry of latent spaces; not used as a premise in the proofs below]`:

```math
\mathbf{H}(z) = \lambda \bigl(\nabla_Z i(z)\bigr)^\perp, \qquad T_z D_\ell = W^{\mathrm{act}}_z \oplus_h W^{\mathrm{inv}}_z \oplus_h K_z, \qquad K_z := \ker(d\pi_\ell(z)).
```
---

### **3.2. Hard Locality Constraints and the Kleitman–Rothschild Entropy Swamp**

The number of all partial orders on $`N`$ elements grows as $`2^{N^2/4 + O(N)}`$, with almost all configurations concentrated in the class of three- and two-layer orders ($`2^{\Theta(N^2)}`$) (Kleitman, Rothschild, 1975), whereas manifold-like bounded-degree graphs carry entropy only $`O(N\ln N)`.

**Definition 3.1 (Admissible Ensemble $`\mathcal{A}(\nu, k_{\max})`$).** `[Status: FOLLOW]`  
A causal-phase state $`(R,\Theta)`$ on $`N`$ events is admissible if five conditions hold:
- **(L0) Hasse property:** $`R`$ is strictly upper-triangular and transitively irreducible (§1.1);
- **(L1) Diamond covering:** every event belongs to at least one elementary diamond as an apex ($`x`$ or $`y`$ of a pair with $`K_{xy}\ge2`$) or as an intermediate waist vertex;
- **(L2) Connectivity:** the undirected Hasse skeleton $`R + R^\top`$ is connected;
- **(L3) Bounded valency:** $`\sum_y (R_{xy}+R_{yx}) \le k_{\max}`$ for every $`x \in X`$;
- **(L4) Lower diamond-density threshold:** $`N_D := \bigl|\{(x,y): K_{xy}\ge2\}\bigr| \ge \nu N`$.

**Proposition 3.1 (Combinatorial Entropy Bound).** `[Status: FOLLOW]`  
The number of graphs on $`N`$ labeled events satisfying (L3) does not exceed $`N^{k_{\max}N} = \exp(k_{\max} N \ln N)`.

*Proof.* Each vertex has at most $`k_{\max}`$ neighbors, chosen from fewer than $`N`$ vertices. `∎`

**Proposition 3.2 (Functionals of $`K`$, $`J`$, $`C`$ Cannot Suppress the Two-Layer Sector).** `[Status: FOLLOW]`  
Let $`N = n_1 + n_2`$ and let $`\mathcal{T}_2`$ be the set of all Hasse matrices whose edges lead only from the first $`n_1`$ vertices to the last $`n_2`$ vertices (no paths of length two exist, hence any subset of the $`n_1 n_2`$ edges is transitively irreducible). On the whole sector $`\mathcal{T}_2`$ the identities $`K\equiv0`$, $`J\equiv0`$, and $`C=0`$ hold. Consequently, for any functional of the form $`F = a\sum K^p + b\sum J + g\|C\|_F^2`$ every state in $`\mathcal{T}_2`$ has zero energy $`F = 0`$ and statistical weight $`e^{-F/T}=1`$, giving the partition function

```math
Z_{\mathcal{T}_2} = 2^{n_1 n_2} \;\ge\; 2^{N^2/4 - N/2} \quad (n_1 = \lfloor N/2\rfloor),
```
whereas for $`F\ge0`$ the partition function of the admissible ensemble is bounded by $`Z_{\mathcal{A}} \le N^{k_{\max}N}`$. Adding a linear chemical potential on the edge number $`e^{\mu\cdot\#\text{links}}`$ gives $`Z_{\mathcal{T}_2} = (1+e^{\mu})^{n_1 n_2} = \exp(\Theta(N^2))`$ for any finite $`\mu\in\mathbb{R}`$. Thus no soft penalties in $`K, J, \|C\|_F`$ and the edge number suppress $`\mathcal{T}_2`$; the hard conditions (L1), (L3), and (L4) are necessary.

**The price of this choice.** In a Poisson sprinkling into a $`d`$-dimensional Lorentzian manifold the number of Hasse links grows as $`N^{2-2/d}`$ (Carlip, 2024), violating condition (L3) as $`N \to \infty`$. The present program therefore describes **regular bounded-valency causal complexes**, not Poisson sprinklings of the continuum.

### **3.3. Interval-Local Path Factorization vs. Global Twin Merging, and the Conditional Selection of `K_xy^eff = 2`**

**Definition 3.2 (Interval-Local Path Equivalence and Global Twin Reduction).** `[Status: FOLLOW]`
1. **Local path factor-rank in an interval:** fix a pair of events $`(x, y)`$ with $`K_{xy} \ge 2`$ and the set of two-step paths $`\mathcal{P}_2(x, y) = \{p_z = (x \lessdot z \lessdot y) \mid z \in V_{xy}\}`$, where the path $`p_z`$ carries the total phase $`\phi_{xy}(z) := (\theta_{xz} + \theta_{zy}) \bmod 2\pi`$. For a tolerance $`\varepsilon_{\mathrm{ker}} \ge 0`$, paths $`p_{z_a}, p_{z_b} \in \mathcal{P}_2(x, y)`$ are phase-close if $`d_{\mathbb{T}}(\phi_{xy}(z_a), \phi_{xy}(z_b)) \le \varepsilon_{\mathrm{ker}}`$. The transitive closure on $`\mathcal{P}_2(x, y)`$ defines the equivalence relation $`\sim_{(x,y),\varepsilon_{\mathrm{ker}}}`$ **strictly inside the pair $`(x, y)`$**, with the effective channel rank $`K_{xy}^{\mathrm{eff}} := |\mathcal{P}_2(x, y) / \!\sim_{(x,y),\varepsilon_{\mathrm{ker}}}| \in \{1, \dots, K_{xy}\}`$ and class phases $`\widetilde{\phi}_\alpha = \arg\bigl(\sum_{z \in C_\alpha} e^{i\phi_{xy}(z)}\bigr)`$, without affecting any other interval $`(x', y') \neq (x, y)`$.
2. **Global merging of structural twin vertices:** distinct vertices $`z_a \neq z_b \in X`$ are called **causal structural twins** if their sets of immediate ancestors and descendants coincide completely: $`\forall u: R_{u z_a} = R_{u z_b}`$ and $`\forall v: R_{z_a v} = R_{z_b v}`$. A global merge $`z_a \equiv z_b`$ on $`X`$ is admissible at threshold $`\varepsilon_{\mathrm{ker}}`$ if and only if $`z_a, z_b`$ are structural twins and $`d_{\mathbb{T}}(\phi_{uv}(z_a), \phi_{uv}(z_b)) \le \varepsilon_{\mathrm{ker}}`$ holds in **every** common interval $`(u, v)`$.

For the local interval functional $`\mathcal{F}_{\mathrm{loc}}^{(p)}(K^{\mathrm{eff}}, \{\widetilde{\phi}_\alpha\}) = a(K^{\mathrm{eff}})^p + b J^{\mathrm{eff}}_{xy}`$ ($`a > 0, p > 0, b \ge 0`$) the following holds:

**Proposition 3.3 (Conditional Selection of $`K_{xy}^{\mathrm{eff}} = 2`$ Under a Power-Law Branching Penalty).** `[Status: FOLLOW (for the functional ansatz; the physical realization of the ansatz is UNDECIDED)]`
1. At $`K^{\mathrm{eff}} = 1`$ the frustration is identically zero: $`J^{\mathrm{eff}}_{xy} \equiv 0`$.
2. Under the constraint of fixed non-zero frustration $`J^{\mathrm{eff}}_{xy} = J_0 \in (0, 2]`$, the unique global minimum of $`\mathcal{F}_{\mathrm{loc}}^{(p)}`$ over integers $`K^{\mathrm{eff}} \ge 1`$ is achieved at $`K^{\mathrm{eff}}_{xy} = 2`$ with relative holonomy $`\Phi_{12} = \pm \arccos(1 - J_0)`$.
3. When comparing ways of splitting a bundle of width $`K`$ into several intervals, two regimes must be distinguished:
   - **Splitting with preservation of the number of elementary diamonds** ($`m = \binom{K}{2}`$ separate binary diamonds): the total branching penalty decreases ($`\binom{K}{2} a 2^p < a K^p`$) for all $`K \ge 3`$ if and only if $`p > \frac{\ln 3}{\ln(3/2)} \approx 2.71`$ (for the quadratic penalty $`p=2`$ and $`K=4`$: $`6\cdot 4a = 24a > 16a`$, i.e., such a split is energetically unfavorable).
   - **Balanced binary regrouping of paths** (partitioning a bundle of width $`K`$ into $`K/2`$ disjoint binary diamonds): the penalty decreases ($`\frac{K}{2} a 2^p < a K^p`$) for all $`K > 2`$ at any convexity exponent $`p > 1`$ (for $`p=2, K=4`$: $`2\cdot 4a = 8a < 16a`$).

**Scope Note on Proposition 3.3.** Proposition 3.3 is a mathematical property of the chosen cost functional $`\mathcal{F}_{\mathrm{loc}}^{(p)}`$. It does **not** prove a priori that nature implements $`\mathcal{F}_{\mathrm{loc}}^{(p)}`$. Why an underlying substrate penalizes path proliferation convexly (e.g., due to finite vertex valency $`k_{\max}`$ preventing Kleitman–Rothschild combinatorial collapse and phase-decoherence noise across multi-slit bundles) is an empirical hypothesis `[Status: UNDECIDED]`, tested in Protocol V1 by comparing convex ($`p=2`$), linear ($`p=1`$), and concave ($`\ln(1+K)`$) penalties. The constraint of fixed non-zero frustration $`J_0 \in (0, 2]`$ is likewise an external premise of the minimization, not a derived property of the substrate (Corollary 3.4).

**Corollary 3.4 (No Selection Without a Lower Threshold).** `[Status: FOLLOW]`  
For free phases and in the absence of a lower bound on $`J_{xy}`$ or on $`N_D`$, the functional $`\mathcal{F}_{\mathrm{loc}}^{(p)}`$ attains its minimum at $`K^{\mathrm{eff}}=1`$ (cost $`a`$) or at $`K=0`$ (cost $`0`$). The binary rank $`K=2`$ is selected only when the lower diamond-density threshold (L4) and the covering condition (L1) are imposed.

### **3.4. What the Binary Diamond Does Not Fix: the Directed-Hypercube Counterexample**

**Proposition 3.5 (Binary Diamonds Arise in Every Dimension).** `[Status: FOLLOW]`  
For any $`d\ge2`$, consider the product order $`H_d`$ on the lattice $`\{0,\dots,n-1\}^d`$ with Hasse links $`x \to x+e_i`$ ($`i=1,\dots,d`$). Then:
1. The matrix $`H_d`$ is transitively irreducible (every edge increases the coordinate sum $`\sum_i x_i`$ by exactly 1).
2. $`K_{xy} \neq 0`$ only for $`|y-x|_1 = 2`$, with $`K_{xy}=2`$ for $`y-x = e_i+e_j`$ ($`i\ne j`$) and $`K_{xy}=1`$ for $`y-x=2e_i`$. In particular, $`K_{xy}\le2`$ everywhere for any $`d \ge 2`$.
3. Every interior vertex ($`x_i \le n-3`$) serves as the lower anchor of exactly $`\binom{d}{2}`$ binary diamonds ($`K_{xy}=2`$), so that $`N_D/N \to \binom{d}{2}`$ as $`n\to\infty`$.

**Consequences.** The waist width $`K=2`$ carries no information about the spatial dimension $`d`$; the dimension is encoded in the diamond density $`\nu(d) = \binom{d}{2}`$ and is measured by the independent estimators $`(d_s, d_H, d_\tau)`$ (§3.6). The earlier claim deriving “3+1” spatial directions from a single binary diamond is **retracted** (`Status: NULL`).

### **3.5. Helmholtz Decomposition Inside the Model**

Write the Cartesian splitting of the transport operator $`W`$ in terms of the Hermitian operators $`H_{\mathrm{sym}}`$ and $`H_{\mathrm{rot}}`$:

```math
W = H_{\mathrm{sym}} + i H_{\mathrm{rot}}, \qquad H_{\mathrm{sym}} = \tfrac12 (W + W^\dagger) = H_{\mathrm{sym}}^\dagger, \qquad H_{\mathrm{rot}} = \tfrac{1}{2i}(W - W^\dagger) = H_{\mathrm{rot}}^\dagger.
```
In the unified model of §2.4, the Hermitian component $`H_{\mathrm{sym}}`$ determines the precision matrix $`\Pi = m^2 I + D - 2H_{\mathrm{sym}}`$, while the skew-Hermitian component $`i H_{\mathrm{rot}}`$ defines the solenoidal drift:

```math
Q_W := \tfrac{\beta}{2}\,(W - W^\dagger) = i\beta H_{\mathrm{rot}}, \qquad Q_W^\dagger = -Q_W, \qquad \beta \in \mathbb{R}.
```
**Proposition 3.6 (Stationary-Measure Preservation and Relaxation Acceleration).** `[Status: FOLLOW for items 1, 2, 4; item 3 — UNDECIDED]`  
For Hermitian positive-definite matrices $`\Pi \succ 0`$, $`\Gamma \succ 0`$ and a skew-Hermitian matrix $`Q^\dagger = -Q`$, consider the complex Langevin process $`d\psi = -(\Gamma+Q)\Pi\psi\,dt + d\xi`$ with noise $`\mathbb{E}[d\xi\,d\xi^\dagger] = 2\Gamma\,dt`$, drift matrix $`B(Q) := (\Gamma+Q)\Pi`$, and relaxation spectral gap $`\gamma(Q) := \min \operatorname{Re}\operatorname{spec} B(Q)`$:
1. **Stationarity:** the distribution $`\mathcal{CN}(0,\Pi^{-1})`$ is stationary for any skew-Hermitian $`Q`$ ($`B\Pi^{-1} + \Pi^{-1}B^\dagger = (\Gamma+Q) + (\Gamma-Q) = 2\Gamma`$).
2. **Non-decrease of the spectral gap:** $`\gamma(Q) \ge \gamma(0) = \lambda_{\min}(\Pi^{1/2}\Gamma\Pi^{1/2}) > 0`$ at fixed real trace $`\operatorname{Re}\operatorname{Tr}B(Q) = \operatorname{Tr}(\Gamma\Pi)`$.
3. **Strict acceleration for $`Q_W`$:** whether the concrete graph drift $`Q_W`$ yields the strict inequality $`\gamma(Q_W) > \gamma(0)`$ on a given ensemble is checked numerically in Protocol V7 (confirmed on a 48-vertex lattice in §10: $`\gamma(0)=0.970 \to \gamma(Q_W)=1.551`$).
4. **Model closure:** substituting $`\Pi`$ and $`Q_W`$ constructed directly from $`(R,\Theta)`$, items 1–2 hold identically on the causal-phase complex.

### **3.6. Sampling the Admissible Ensemble and Dimension Estimators**

Admissible states $`\mathcal{A}(\nu, k_{\max})`$ are generated by three Markov moves (with a uniform choice of new phases on the circle): *(M1) single edge replacement*, *(M2) diamond corner flip* $`(x \lessdot z \lessdot y) \mapsto (x \lessdot z' \lessdot y)`$ with the Hastings correction $`|\mathcal{C}(R)|/|\mathcal{C}(R')|`$ (preserving $`K_{xy}`$ on the chosen pair $`(x,y)`$ under a direct recount of the global diamond number $`N_D`$), and *(M3) transposition of adjacent incomparable indices* $`(i, i+1)`$. Since the natural topological numbering weights each isomorphism class of a partial order $`P`$ by the number of its linear extensions $`e(P)`$ ($`\ln e(P) \sim (1-1/d)N\ln N`$), Protocol V1 records the $`T=0`$ minimizers separately from the $`T>0`$ samples.

Three independent dimension estimates are computed: the spectral dimension $`d_s(\sigma)`$, the Hausdorff ball-growth dimension $`d_H`$, and the Myrheim–Meyer chain dimension $`d_\tau`$ (§7, Protocol V1).

---

## **4. Entropy Balance of a Contracting Subsystem: Lyapunov Spectrum, Noise-Injected Entropy, and the Thermodynamic Reading**

### **4.1. Separating the Non-Equilibrium Subsystem Dynamics (V2) from the Equilibrium Field Problem (V3)**

Two distinct dynamical regimes studied by the program must be strictly separated:
1. **The non-equilibrium problem of a contracting map with additive noise (this section, Protocol V2):** studies a nonlinear dissipative map $`G(\psi)`$ on a fixed subsystem subgraph $`A`$ under a constant influx of external noise, and relates the phase-entropy production rate to the spectrum of Lyapunov exponents $`\kappa - h_+ = -\sum_i\lambda_i`$.
2. **The equilibrium problem of graph–Gaussian-field co-evolution (Section 6, Protocols V3 and V4):** studies the restructuring of the connection matrix $`R`$ itself under the exact free energy $`\ln\det\Pi(R,\Theta)`$ of the linear Gaussian field of §2.4. These two problems are logically independent and are tested in different protocols (V2 and V3 respectively).

### **4.2. Dynamical Model on a Subsystem**

**Definition 4.1 (Noisy Transport Map on a Subsystem).** `[Status: FOLLOW]`  
For a subsystem $`A\subset X`$ of $`N_A`$ events, set $`H_A := (W + W^\dagger)|_{A\times A}`$ and consider the state vector $`\psi\in\mathbb{C}^{N_A}\cong\mathbb{R}^{2N_A}`$. For damping parameter $`\delta\in(0,1)`$, coupling $`g>0`$, and noise amplitude $`s>0`$, define:

```math
G(\psi) := (1-\delta)\,\psi + g\,H_A\,f(\psi), \qquad f(\psi)_x := \frac{\psi_x}{\sqrt{1+|\psi_x|^2}}, \qquad \psi_{n+1} = G(\psi_n) + \xi_n, \quad \xi_n \sim \mathcal{CN}(0, s^2 I)\ \text{i.i.d.}
```
**Lemma 4.2 (Injectivity).** `[Status: FOLLOW]`  
If $`g\|H_A\|_2 < 1-\delta`$, then $`G`$ is a $`C^\infty`$-diffeomorphism onto its open image in $`\mathbb{R}^{2N_A}`$ and $`\det DG\ne0`$ everywhere.

*Proof.* Each local node map $`\psi_x \mapsto \psi_x/\sqrt{1+|\psi_x|^2}`$ has real Jacobian eigenvalues $`(1+|\psi_x|^2)^{-3/2}`$ and $`(1+|\psi_x|^2)^{-1/2}`$, lying in $`(0,1]`; hence $`f`$ has Lipschitz constant $`1`$. Consequently $`\|G(\psi)-G(\varphi)\|\ge(1-\delta-g\|H_A\|_2)\|\psi-\varphi\|>0`$ for $`\psi\neq\varphi`$, and the Jacobian $`DG=(1-\delta)I+gH_A\,Df`$ is invertible by the Neumann series. `∎`

Let $`\lambda_1\ge\dots\ge\lambda_{2N_A}`$ be the Lyapunov exponents of the random dynamical system along the noisy trajectory (computed by the Benettin method with QR re-orthogonalization (Benettin et al., 1980), not through the singular values of a single matrix), and let

```math
\kappa := \sum_{\lambda_i<0}|\lambda_i|, \qquad h_+ := \sum_{\lambda_i>0}\lambda_i, \qquad \sum_i\lambda_i = h_+ - \kappa .
```
### **4.3. Exact Stationary Entropy Balance**

**Theorem 4.3 (Stationary Entropy Balance for Random Dynamical Systems with Additive Noise).** `[Status: FOLLOW]`  
Let $`G:\mathbb{R}^n\to\mathbb{R}^n`$ be an injective $`C^1`$ map with $`\det DG\neq0`$; let the noise $`\xi`$ have a density and be independent of $`Z`$; and let the chain $`Z_{n+1}=G(Z_n)+\xi_n`$ possess an ergodic stationary measure with finite differential entropy $`h(Z)`$ and $`\mathbb{E}|\ln|\det DG(Z)||<\infty`$. Define the entropy injected by the noise per step:

```math
\Delta_{\mathrm{noise}} := h\bigl(G(Z)+\xi\bigr) - h\bigl(G(Z)\bigr) \;\ge\; 0 .
```
Then the exact equality holds:

```math
\Delta_{\mathrm{noise}} \;=\; -\,\mathbb{E}\ln|\det DG(Z)| \;=\; -\sum_i\lambda_i \;=\; \kappa - h_+ .
```
*Proof.* By the change-of-variables formula for the injective map $`G`$, $`h(G(Z)) = h(Z) + \mathbb{E}\ln|\det DG(Z)|`$. By stationarity, $`h(Z) = h(G(Z)+\xi) = h(G(Z)) + \Delta_{\mathrm{noise}}`$. Subtracting one equality from the other gives $`\Delta_{\mathrm{noise}} = -\mathbb{E}\ln|\det DG(Z)| = -\sum_i\lambda_i = \kappa - h_+`$. `∎`

**Corollary 4.4 (`ε`-Cell Version).** `[Status: FOLLOW]`  
If the stationary density is smooth at scale $`\varepsilon`$ in all directions, then $`H_\varepsilon(Z)\approx h(Z)-n\ln\varepsilon`$, and the same balance holds for the coarse-grained entropies up to $`o(1)`$ as $`\varepsilon\to0`$ at fixed noise level.

**Hypothesis H-L (Thermodynamic Reading) and the Interface Saturation Parameter.** `[Status: UNDECIDED]`  
Interpreting $`k_B T(\kappa - h_+)`$ as a physical heat flux into an external thermostat (Landauer, 1961; Ruelle, 1996), as well as interpreting the dimensionless ratio $`\eta_{\mathrm{sat}}(A) := \frac{\kappa(A)-h_+(A)}{c_0\ln 2\cdot|\partial^+A|_E}`$ as a physical channel-saturation threshold, requires introducing a physical reservoir, a temperature $`T`$, and a single-edge capacity $`c_0`$ that are not defined inside the discrete model, and therefore has status `UNDECIDED`.

---

## **5. Time as a Multiscale Synchronization Spectrum, Integrator Chains, and the Network Architecture Transition**

### **5.1. Operational Phase-Cycle Ratios and the Kinematic Signature Ansatz**

**Definition 5.1 (Proper Phase-Accumulation Rate and the Operational-Time Ratio).** `[Status: FOLLOW]`  
For a worldtube of subsystem $`A`$ consisting of antichains $`S_0 \prec \dots \prec S_m`$ with non-empty diamond sets $`\mathcal{D}_A(k)`$ between layers $`S_k`$ and $`S_{k+2}`$, define the complex order parameter $`z_A(k) := \frac{1}{|\mathcal{D}_A(k)|} \sum_{D \in \mathcal{D}_A(k)} e^{i\Phi_D}`$. Under the coherence condition $`|z_A(k)| \ge \theta_{\mathrm{coh}} > 0`$, the dimensionless rate of curvature-flux accumulation per causal layer and the ratio of accumulated cycles between subsystems $`A, B`$ exchanging unbranched null signals ($`d_\diamond = 0`$) are given by:

```math
\omega_A^{(\ell)} := \frac{1}{m} \sum_{k=0}^{m-1} \arg z_A(k), \qquad \Delta N_A^{(\ell)} = \frac{m}{2\pi} \omega_A^{(\ell)}, \qquad R_{AB}^{(\ell)} := \frac{\Delta N_A^{(\ell)}}{\Delta N_B^{(\ell)}} \quad \text{only when } \Delta N_B^{(\ell)} \ne 0.
```
The domain restriction is a mandatory part of Definition 5.1: if $`\Delta N_B^{(\ell)}=0`$, the quantity $`R_{AB}^{(\ell)}`$ is **undefined** and no finite numerical value may be assigned to it. In particular, when both subsystems have flat connections ($`\Delta N_A^{(\ell)}=\Delta N_B^{(\ell)}=0`$), the ratio is a $`0/0`$ indeterminacy and is excluded from any statistics of $`R_{AB}^{(\ell)}`$ (such cases are recorded separately in the report, without artificial regularization).

Since $`\omega_A^{(\ell)}`$ vanishes on flat connections (Proposition 1.2) and is measured in radians per causal layer rather than in inverse seconds ($`\mathrm{s}^{-1}`$), the identification of the well-defined ratio $`R_{AB}^{(\ell)}`$ with the physical clock redshift, and the derivation of the Lorentzian signature $`(-,+,+,+)`$ from the quadratic step-allocation ansatz $`(\Delta\tau)^2 + (\Delta l)^2 = (\Delta s_{\mathrm{causal}})^2`$, have status `UNDECIDED`.

### **5.2. Stochastic Realization of Boundary Spectra and Second-Order Inertia**

**Proposition 5.1 (Stochastic Realization of Multi-Frequency Boundary Processes as Integrator Chains).** `[Status: FOLLOW]`  
Let $`s_t`$ be a centered stationary Gaussian process on the incoming interface $`\partial^- A`$ with a rational spectral density determined by damping and oscillation modes $`\{\gamma_k \pm i\omega_k\}_{k=0}^n`$ ($`\gamma_k > 0`$):
1. By Doob's theorem and the linear theory of stochastic realization (Doob, 1942; Lindquist, Picci, 2015; Da Costa et al., 2021), the process $`s_t`$ is the output of a finite-dimensional linear stochastic differential equation of McMillan degree (in companion form with a single shared source of innovation noise). In the integrator-chain form of generalized motion coordinates $`ds_t^{(k)} = (-A_k s_t^{(k)} + B_k s_t^{(k+1)})\,dt + \varsigma_k\,dW_t^{(k)}`$ ($`0 \le k < n`$), $`ds_t^{(n)} = -A_n s_t^{(n)}\,dt + \varsigma_n\,dW_t^{(n)}`$ with independent noises at each level, scalar spectra of the form $`S(\omega)=\sum_k c_k\big/\prod_{j\le k}\lvert i\omega + A_j\rvert^2`$ are realized with non-negative weights $`c_k = \varsigma_k^2\prod_{j<k}B_j^2 \ge 0`$.
2. Under the separation of mode timescales $`0 < \gamma_0 \le \gamma_1 \le \gamma_2 \ll \gamma_3 \le \dots \le \gamma_n`$, temporal coarse-graining uses the **non-empty window**:
```math
\tau_w^{(\ell)} \in (\gamma_3^{-1}, \gamma_2^{-1}), \qquad \text{under strong scale separation } \gamma_3^{-1} \ll \tau_w^{(\ell)} \ll \gamma_2^{-1}.
```
   The lower bound makes the window long compared with the relaxation times of the fast modes $`k \ge 3`$, and the upper bound keeps it short compared with the lifetimes of the slow modes $`k \le 2`$. The variance of the window-averaged coordinates of orders $`k \ge 3`$ is suppressed as $`O((\gamma_k \tau_w^{(\ell)})^{-1})`$, reducing the active boundary state to the truncated triple $`\tilde{s}_t^{(\le 2)} = (s_t^{(0)}, s_t^{(1)}, s_t^{(2)})`$ (position, velocity, acceleration) and generating a second-order control law.

### **5.3. The Multiscale Coarse-Graining Operator `ℛ_{ℓ→ℓ+1}` and the Network Architecture Transition**

**Definition 5.2 (Coarse-Graining Operator $`\mathcal{R}_{\ell \to \ell+1}`$ and Synchronization Time $`\tau_{\mathrm{sync}}`$).** `[Status: FOLLOW]`  
At scale $`\ell`$, spacelike vertex pairs ($`u \not\prec_\ell v, v \not\prec_\ell u`$) with two-step cone overlap $`S^{(\ell)}_{uv} = |(\Delta_+^{(\ell)})_{uv}| + |(\Delta_-^{(\ell)})_{uv}| \ge \theta_\ell`$ are merged into order-convex macro-nodes $`X_{\ell+1} = \{C_\alpha\}`$ (rejecting any partition that creates a directed cycle in the quotient graph), after which the Hasse transitive reduction $`R_{\ell+1}`$ and the coherent summation of amplitudes $`\widetilde{W}^{(\ell+1)}_{\alpha\beta} = \sum_{x \in C_\alpha, y \in C_\beta} W^{(\ell)}_{xy}`$ are performed. For a subsystem $`A_\ell`$ with diameter $`\tau_{\mathrm{diam}}(A_\ell)`$ and Fiedler eigenvalue of the normalized Laplacian $`\lambda_2(A_\ell) > 0`$, the synchronization time is defined as $`\tau_{\mathrm{sync}}(A_\ell) := \tau_{\mathrm{diam}}(A_\ell) / \lambda_2(A_\ell)`$.

**Proposition 5.2 (Synchronization Instability of a Homogeneous $`d`$-Dimensional Ball) and Corollary 5.3 (Expander Alternative).** `[Status: FOLLOW]`  
For a regular $`d`$-dimensional ball ($`d \ge 2`$) of $`N`$ vertices with bounded degree $`\le k_{\max}`$, we have $`\tau_{\mathrm{diam}} = \Theta(N^{1/d})`$ and $`\lambda_2 = \Theta(N^{-2/d})`$, whence $`\tau_{\mathrm{sync}}^{\mathrm{ball}}(N) = \Theta(N^{3/d}) \to \infty`$ as $`N \to \infty`$. On the other hand, random $`k_{\max}`$-regular graphs ($`k_{\max}\ge 3`$) possess a spectral gap $`\lambda_2 = \Theta(1)`$ and synchronization time $`\tau_{\mathrm{sync}} = O(\ln N)`$ without forming filaments or voids (Friedman, 2008). Protocol V5 therefore tests whether the minimizers of volume and frustration subject to $`\lambda_2 \ge \lambda_{\mathrm{sync}}`$ are filamentary networks or regular expanders.

---

## **6. Field Back-Reaction on the Graph, the Exact Loop Expansion, and the Triadic Schur Decomposition**

### **6.1. Additive Diamond-Partition Identity (bookkeeping identity)**

**Proposition 6.1 (Additive Identity of Diamond-Coherence Distribution).** `[Status: FOLLOW]`  
Assigning every waist with $`K_{xy} \ge 2`$ to its lower anchor $`x \in X`$ via the weight $`q_x := \sum_{y:\, K_{xy} \ge 2} \frac{|M_{xy}|^2}{K_{xy}}`$ and defining the mean density $`\rho_D(U) := \frac{1}{|U|}\sum_{x \in U} q_x`$, any partition $`X = \mathcal{E} \sqcup \bigsqcup_{m=1}^M (\mathcal{I}_{A_m} \sqcup \partial A_m)`$ satisfies the exact additive identity $`\rho_D(\mathcal{E}) = \frac{1}{|\mathcal{E}|}\bigl(Q_{\mathrm{tot}}(X) - \sum_m |\mathcal{I}_{A_m}|\rho_D(\mathcal{I}_{A_m}) - \sum_m |\partial A_m|\rho_D(\partial A_m)\bigr)`$.

### **6.2. The Exact Law of Graph–Gaussian-Field Co-Evolution**

In version 3.9 the verification of background-graph restructuring (V3) and of defect interaction through the interface (V4) had no explicit equation linking the structural functional to the field: the mediating covariance $`\Sigma_{\mathcal{I}\mathcal{E}}\ne0`$ of Proposition 2.2 is a *static* channel, and no dynamical counterpart of edge restructuring followed from it. Version 4.0 closes this gap exactly.

**Base structural functional and the joint co-evolution functional.** `[Status: FOLLOW for the declared ansatz]`  
For a causal-phase state $`(R,\Theta) \in \mathcal{A}(\nu, k_{\max})`$, set $`K=R^2`$, define $`J_{xy}`$ per §1.3 for $`K_{xy}>0`$ and extend $`J_{xy}:=0`$ for $`K_{xy}=0`$. At parameters fixed before the run ($`a>0`$, $`b\ge0`$, $`g\ge0`$, $`p>0`$):

```math
F_{\mathrm{struct}}(R,\Theta; a,b,g,p) := a\sum_{x,y\in X} K_{xy}^{p} + b\sum_{x,y\in X} J_{xy} + g\,\|C\|_F^2, \qquad C=[\Delta_+,\Delta_-].
```
Integration over $`n_{\mathrm{bos}} = \eta_{\mathrm{field}} > 0`$ independent components of a complex bosonic Gaussian field $`\psi`$ in the partition function

```math
\int_{\mathbb{C}^N} \frac{d\psi\,d\bar{\psi}}{\pi^N} \, e^{-\psi^\dagger \Pi(R,\Theta) \psi} = \bigl(\det\Pi(R,\Theta)\bigr)^{-1} = \exp\bigl(-\ln\det\Pi(R,\Theta)\bigr)
```
uniquely fixes the **positive (bosonic) sign** of the field-coupling parameter $`\eta_{\mathrm{field}} > 0`$ (with the canonical parameter-free point $`\eta_{\mathrm{field}} = 1`$ for the single-component field of §2.4) in the **joint functional of graph–field co-evolution**:

```math
\mathscr{F}_{\mathrm{joint}}(R, \Theta; \eta_{\mathrm{field}},a,b,g,p) := F_{\mathrm{struct}}(R, \Theta; a,b,g,p) + \eta_{\mathrm{field}} \, \ln\det\Pi(R, \Theta), \qquad \eta_{\mathrm{field}} > 0, \quad \Pi(R, \Theta) = m^2 I + L_\Theta.
```
*(Delimitation remark vis-à-vis Section 4: the functional $`\mathscr{F}_{\mathrm{joint}}`$ describes the equilibrium thermodynamic back-reaction of the Gaussian-field vacuum fluctuations on the graph $`R`$ and is tested in Protocols V3 and V4, whereas the non-equilibrium saturating system of §4 is tested separately in Protocol V2.)*

**Proposition 6.2 (Rank-1 Incidence Factorization and the Exact $`2\times 2`$ Woodbury Law for an Edge Swap).** `[Status: FOLLOW]`  
For any directed pair $`e = (x, y)`$ with phase $`\theta_{xy} \in [0, 2\pi)`$, define the dipole incidence vector $`v_e \in \mathbb{C}^N`$ by components $`(v_e)_u := \delta_{ux} - e^{-i\theta_{xy}}\delta_{uy}`$. Let $`\Sigma = \Pi(R, \Theta)^{-1}`$ be the field covariance matrix on $`(R, \Theta)`$, and define the **magnetic effective resistance** of the pair $`e`$:

```math
r_{\mathrm{eff}}(x, y; \theta_{xy}) := v_e^\dagger \Sigma v_e = \Sigma_{xx} + \Sigma_{yy} - 2\operatorname{Re}\bigl(e^{i\theta_{xy}}\Sigma_{yx}\bigr) = \mathbb{E}_{\psi \sim \mathcal{CN}(0, \Sigma)}\bigl[|\psi_x - e^{i\theta_{xy}}\psi_y|^2\bigr] > 0.
```
Then three exact relations hold:
1. **Rank-1 decomposition of $`L_\Theta`$:** the magnetic Laplacian equals the exact sum over active Hasse links:
```math
L_\Theta = \sum_{e \in E(R)} v_e v_e^\dagger, \qquad \Pi(R, \Theta) = m^2 I + \sum_{e \in E(R)} v_e v_e^\dagger \succeq m^2 I.
```
   For every active edge $`e_- \in E(R)`$, since $`\Pi - v_{e_-}v_{e_-}^\dagger \succeq m^2 I \succ 0`$, the effective resistance is strictly bounded: $`0 < r_{\mathrm{eff}}(e_-) < 1`$.
2. **Exact non-local determinant ratio for an edge replacement (Move M1):** if an active edge $`e_- \in E(R)`$ is removed and an inactive admissible edge $`e_+ \notin E(R)`$ with phase $`\theta_{e_+}`$ is added ($`\Pi' = \Pi - v_{e_-}v_{e_-}^\dagger + v_{e_+}v_{e_+}^\dagger`$), the exact determinant ratio equals:
```math
\frac{\det\Pi(R', \Theta')}{\det\Pi(R, \Theta)} = \bigl(1 - r_{\mathrm{eff}}(e_-)\bigr)\bigl(1 + r_{\mathrm{eff}}(e_+)\bigr) + \bigl|v_{e_-}^\dagger \Sigma v_{e_+}\bigr|^2,
```
   where $`v_{e_-}^\dagger \Sigma v_{e_+}`$ is the **field-mediated cross-covariance between the removed edge $`e_-`$ and the added edge $`e_+`$**.
3. **Phase gradient:** for every active edge $`e = (x, y) \in E(R)`$, the derivative equals $`\frac{\partial \ln\det\Pi(R, \Theta)}{\partial \theta_{xy}} = 2\operatorname{Im}\bigl(e^{i\theta_{xy}}\Sigma_{yx}\bigr)`$.

*Proof.* (1) For any $`\psi \in \mathbb{C}^N`$, $`\psi^\dagger(v_e v_e^\dagger)\psi = |v_e^\dagger\psi|^2 = |\psi_x - e^{i\theta_{xy}}\psi_y|^2`$, and summing over $`e \in E(R)`$ gives $`\psi^\dagger L_\Theta \psi`$ (Definition 2.4). Since $`\Pi - v_{e_-}v_{e_-}^\dagger \succ 0`$, congruence with $`\Sigma^{1/2}`$ gives $`I - \Sigma^{1/2}v_{e_-}v_{e_-}^\dagger\Sigma^{1/2} \succ 0 \implies v_{e_-}^\dagger \Sigma v_{e_-} < 1`$. (2) Write $`\Pi' = \Pi + U J U^\dagger`$, where $`U = [v_{e_-}, v_{e_+}] \in \mathbb{C}^{N\times 2}`$ and $`J = \operatorname{diag}(-1, +1)`$. By the $`2\times 2`$ matrix-determinant lemma:
```math
\frac{\det\Pi'}{\det\Pi} = \det\bigl(I_2 + J U^\dagger \Sigma U\bigr) = \det\begin{pmatrix} 1 - v_{e_-}^\dagger\Sigma v_{e_-} & -v_{e_-}^\dagger\Sigma v_{e_+} \\ v_{e_+}^\dagger\Sigma v_{e_-} & 1 + v_{e_+}^\dagger\Sigma v_{e_+} \end{pmatrix} = \bigl(1 - r_{\mathrm{eff}}(e_-)\bigr)\bigl(1 + r_{\mathrm{eff}}(e_+)\bigr) + \bigl|v_{e_-}^\dagger \Sigma v_{e_+}\bigr|^2.
```
(3) Differentiating $`\operatorname{Tr}\ln\Pi`$ with $`\frac{\partial \Pi}{\partial\theta_{xy}} = -i e^{i\theta_{xy}} E_{xy} + i e^{-i\theta_{xy}} E_{yx}`$ gives $`\operatorname{Tr}(\Sigma \frac{\partial\Pi}{\partial\theta_{xy}}) = 2\operatorname{Im}(e^{i\theta_{xy}}\Sigma_{yx})`$. `∎`

**Proposition 6.3 (Convergent Loop Expansion, Triangle-Freeness, Two Classes of 4-Cycles, and Diamagnetic Positivity of $`\ln\det\Pi`$).** `[Status: FOLLOW]`  
Let $`D_m := m^2 I + D`$ and $`T_\Theta := D_m^{-1/2}(W + W^\dagger)D_m^{-1/2}`$ for $`m^2 > 0`$. Then:
1. **Strict contraction and convergence of the loop series:** $`\|T_\Theta\|_2 \le \frac{d_{\max}}{m^2 + d_{\max}} < 1`$ (where $`d_{\max} = \max_x D_{xx}`$), and the expansion over closed walks converges absolutely:
```math
\ln\det\Pi(R, \Theta) = \ln\det D_m - \sum_{\ell=1}^{\infty} \frac{1}{\ell} \operatorname{Tr}\bigl(T_\Theta^\ell\bigr).
```
2. **Phase inertia of orders $`\ell = 1, 2, 3`$ on Hasse graphs:** for any Hasse matrix $`R`$ and any phases $`\Theta`$:
```math
\operatorname{Tr}(T_\Theta^1) = 0, \qquad \operatorname{Tr}(T_\Theta^2) = 2\sum_{x \lessdot y} \frac{1}{(m^2 + D_{xx})(m^2 + D_{yy})} = \operatorname{Tr}(T_0^2), \qquad \operatorname{Tr}(T_\Theta^3) = \operatorname{Tr}(T_0^3) = 0.
```
3. **Leading 4-cycle contribution (causal diamonds and bipartite crowns $`K_{2,2}`$) and the diamagnetic inequality:** for all $`(R, \Theta)`$ and $`m^2 > 0`$:
```math
\Phi_{\mathrm{mag}}(R, \Theta) := \ln\det\Pi(R, \Theta) - \ln\det\Pi(R, 0) = \sum_{\ell=4}^{\infty} \frac{1}{\ell}\bigl(\operatorname{Tr}(T_0^\ell) - \operatorname{Tr}(T_\Theta^\ell)\bigr) \;\ge\; 0,
```
   with equality to zero if and only if the phases $`\Theta`$ are gauge-flat on every cycle of the undirected skeleton $`R + R^\top`$. The leading non-trivial phase contribution arises at order $`\ell = 4`$ and is a weighted sum of Wilson actions $`1 - \cos\Phi_\square`$ over all simple 4-cycles of the skeleton $`R + R^\top`$, which split into exactly two topological classes:
   - *(a) Directed causal diamonds* $`D(x; z_a, z_b; y)`$ ($`x \lessdot z_a \lessdot y`$ and $`x \lessdot z_b \lessdot y`$, where $`K_{xy} \ge 2`$ and the holonomy equals $`\Phi_{ab}`$);
   - *(b) Alternating bipartite 4-cycles (“crowns” $`K_{2,2}`$)* of the form $`x_1 \lessdot y_1, x_1 \lessdot y_2, x_2 \lessdot y_1, x_2 \lessdot y_2`$ ($`x_1 \neq x_2, y_1 \neq y_2`$), which can exist even when $`K = R^2 \equiv 0`$ (in particular on the two-layer sector $`\mathcal{T}_2`$, making $`\ln\det\Pi(R,\Theta)`$ sensitive to two-layer graphs in contrast to $`J_{xy}`$).

*Proof.* (1) Since $`D_m \mp (W + W^\dagger) = m^2 I + L_{\Theta\text{ or }\Theta+\pi} \succeq m^2 I`$, congruence with $`D_m^{-1/2}`$ gives $`\pm T_\Theta \preceq \frac{d_{\max}}{m^2 + d_{\max}} I`, i.e. $`\|T_\Theta\|_2 < 1`$. (2) $`\operatorname{Tr}(T_\Theta^1)=0`$ because the diagonal vanishes; at $`\ell=2`$ closed walks traverse a single edge $`x \lessdot y`$ forth and back ($`e^{i\theta_{xy}}e^{-i\theta_{xy}}=1`$); at $`\ell=3`$ any closed walk of length 3 forms a triangle in $`R + R^\top`$, but by §1.1 (item 2) Hasse graphs contain no triangles. (3) Each closed walk $`\gamma`$ of length $`\ell \ge 4`$, paired with its reversal, contributes $`w(\gamma)\cos\Phi(\gamma) \le w(\gamma)`$ to $`\operatorname{Tr}(T_\Theta^\ell)`$, hence $`\operatorname{Tr}(T_0^\ell) - \operatorname{Tr}(T_\Theta^\ell) = \sum_{|\gamma|=\ell} w(\gamma)(1 - \cos\Phi(\gamma)) \ge 0`$. In a transitively reduced directed acyclic graph, every simple 4-cycle of the skeleton has either a single source vertex and a single sink vertex (a causal diamond $`D(x; z_a, z_b; y)`$) or alternating edge orientations (a bipartite crown $`K_{2,2}`$). `∎`

### **6.3. The Exact Triadic Schur Decomposition and the Interface Functional**

Combining Proposition 2.2(1) ($`\Pi_{\mathcal{I}\mathcal{E}} = 0`$) with the Schur determinant formula yields an exact additive decomposition of $`\ln\det\Pi`$ over any structural triad $`X = \mathcal{I}_A \sqcup \partial A \sqcup \mathcal{E}_A`.

**Proposition 6.4 (Exact Triadic Schur Decomposition and the Interface Coupling Functional).** `[Status: FOLLOW]`  
For any proper subsystem $`A \subset X`$ with triad $`X = \mathcal{I}_A \sqcup \partial A \sqcup \mathcal{E}_A`$ (indices $`\mathcal{I}, b, \mathcal{E}`$) and magnetic precision matrix $`\Pi(R, \Theta) \succ 0`$:
1. **Triadic determinant identity:** since $`\Pi_{\mathcal{I}\mathcal{E}} = 0`$, the principal submatrix on $`\mathcal{I}_A \sqcup \mathcal{E}_A`$ is block-diagonal ($`\operatorname{diag}(\Pi_{\mathcal{I}}, \Pi_{\mathcal{E}})`$), and $`\ln\det\Pi(R, \Theta)`$ decomposes exactly into the sum of the internal-bulk, external-channel, and interface Schur-complement contributions:
```math
\ln\det\Pi(R, \Theta) = \ln\det\Pi_{\mathcal{I}} + \ln\det\Pi_{\mathcal{E}} + \ln\det S_{\partial A},
```
   where the **interface Schur operator** on the boundary $`\partial A`$ equals:
```math
S_{\partial A} := \Pi_b - \Pi_{b\mathcal{I}}\Pi_{\mathcal{I}}^{-1}\Pi_{\mathcal{I}b} - \Pi_{b\mathcal{E}}\Pi_{\mathcal{E}}^{-1}\Pi_{\mathcal{E}b} = (\Sigma_b)^{-1} \succ 0.
```
2. **Positive-definite interface coupling functional:** define the interface stitching free energy as the reduction of the log-determinant on $`\partial A`$ induced by the couplings with $`\mathcal{I}_A`$ and $`\mathcal{E}_A`$:
```math
\mathscr{S}_{\mathrm{interface}}(A; R, \Theta) := \ln\det\Pi_b - \ln\det S_{\partial A} = -\ln\det\bigl(I - \Pi_b^{-1/2}\bigl(\Pi_{b\mathcal{I}}\Pi_{\mathcal{I}}^{-1}\Pi_{\mathcal{I}b} + \Pi_{b\mathcal{E}}\Pi_{\mathcal{E}}^{-1}\Pi_{\mathcal{E}b}\bigr)\Pi_b^{-1/2}\bigr) > 0.
```
   For a non-empty boundary $`\partial A \neq \varnothing`$ the strict inequality $`\mathscr{S}_{\mathrm{interface}}(A; R, \Theta) > 0`$ holds.

*Proof.* (1) Ordering the indices as $`(\mathcal{I}, \mathcal{E}, b)`$ gives a block matrix with zero blocks between $`\mathcal{I}`$ and $`\mathcal{E}`$; the block-determinant formula yields $`\det\Pi = \det\Pi_{\mathcal{I}}\det\Pi_{\mathcal{E}}\det S_{\partial A}`$, and the block-inversion formula gives $`S_{\partial A} = (\Sigma_b)^{-1} \succ 0`$. (2) Since $`K_{\mathrm{int}} := \Pi_{b\mathcal{I}}\Pi_{\mathcal{I}}^{-1}\Pi_{\mathcal{I}b} \succeq 0`$ and $`K_{\mathrm{ext}} := \Pi_{b\mathcal{E}}\Pi_{\mathcal{E}}^{-1}\Pi_{\mathcal{E}b} \succeq 0`$ do not vanish simultaneously on a non-empty boundary $`\partial A`$, we have $`0 \prec S_{\partial A} = \Pi_b - (K_{\mathrm{int}} + K_{\mathrm{ext}}) \preceq \Pi_b`$ with a strict inequality for at least one eigenvalue, whence $`\det S_{\partial A} < \det\Pi_b`$ and $`\mathscr{S}_{\mathrm{interface}}(A; R, \Theta) > 0`$. `∎`

**Status of continuum extrapolations.** While Propositions 6.2–6.4 fully close the discrete protocols V3 and V4 on finite matrices $`(R, \Theta)`$, the continuum extrapolations to Einstein equations with the cosmological term $`\Lambda_{\mathrm{eff}}[I_{\mathrm{erase}}]g_{\mu\nu}`$ and to the post-horizon phase $`K^{\mathrm{eff}}\ge 3`$ remain deferred beyond the discrete model (`Status: OMIT`).

---

## **7. Computational Verification Program (Protocols V1–V7)**

All seven protocols are mathematically closed and executable directly on finite matrices $`(R, \Theta)`$ with pre-registered numerical confirmation and refutation criteria:

| ID | Tested claim | Protocol and control ensembles | Confirmation criterion (`FOLLOW`) | Refutation criterion (`NULL`) |
| :--- | :--- | :--- | :--- | :--- |
| **V1** | **Admissible ensemble: diamond structure and dimension (§3.2–3.6).** | $`N \in \{64,128,256\}`$, $`\nu \in \{0.5,1,2,3\}`$, $`k_{\max}\in\{6,8\}`$; functional $`F_{\mathrm{struct}} = a\sum K^p + b\sum J + g\Vert C\Vert_F^2`$ at $`p=2`$ (convex), $`p=1`$, and $`\ln(1+K)`$ (concave control); variation of $`a:b:g`$ by a factor of 3. Separate runs at $`T=0`$ and $`T>0`$. **Negative control A:** the same functional without (L1), (L4) must collapse into two-layer/tree states (Proposition 3.2). | (i) At $`p=2`$, at least $`80\%`$ of active pairs ($`K\ge2`$) have $`K=2`$ ($`K_{\max}\le3`$), exceeding the concave control by at least $`0.2`$; (ii) a manifold-like phase exists ($`\vert d_s - d_H\vert, \vert d_s - d_\tau\vert \le 0.3`$); (iii) $`N_D/N`$ follows $`\nu`$ monotonically, and $`d_s`$ changes in steps as $`\nu`$ grows. | No manifold-like phase anywhere on the grid; or equal $`K=2`$ fractions under convex and concave penalties; or the dimension depends on $`a:b:g`$ more strongly than on $`\nu`$. |
| **V2** | **Exact entropy balance $`\Delta_{\mathrm{noise}} = -\sum_i\lambda_i`$ in the non-equilibrium model (Theorem 4.3).** | Model of Definition 4.1 on subsystems ($`2N_A\le8`$ real dimensions) under the condition of Lemma 4.2; Benettin (QR) spectrum, Kozachenko–Leonenko $`k`$-NN entropy estimates, and $`-\mathbb{E}\ln\vert\det DG\vert`$. Controls: the exact Gaussian case and a non-injective map $`G`$. | $`\vert\hat\Delta_{\mathrm{noise}} - (-\sum_i\lambda_i)\vert \le 0.05`$ nats and $`\vert -\mathbb{E}\ln\vert\det DG\vert - (-\sum_i\lambda_i)\vert \le 0.02`$ nats; stationarity residual $`\le 0.05`$ nats; Gaussian control reproduced to $`0.02`$. | Violation of the identity on injective systems with converged estimators, or failure of the estimators on the Gaussian control. |
| **V3** | **Equilibrium graph restructuring under field back-reaction (Proposition 6.2).** | Sampling $`(R,\Theta)\in\mathcal{A}(\nu,k_{\max})`$ with a frustrated core $`A`$ ($`\Phi_D=\Phi_0\in(0,\pi]`$ in $`\mathcal{I}_A`$) under the joint functional of §6.2 $`\mathscr{F}_{\mathrm{joint}} = F_{\mathrm{struct}} + \eta_{\mathrm{field}}\ln\det\Pi(R,\Theta)`$ at the fixed bosonic sign $`\eta_{\mathrm{field}} \in \{0.5, 1.0, 2.0\} > 0`$, via the Woodbury formula (Proposition 6.2). **Null control:** identical budgets at $`\eta_{\mathrm{field}} = 0`$. | Statistically significant ($`>3\sigma`$) growth of the external null-link fraction $`\Delta f_{\mathrm{null}}(\mathcal{E}_A) = f_{\mathrm{null}}(\eta_{\mathrm{field}}) - f_{\mathrm{null}}(0) > 0`$ and of the null-path length $`\Delta\ell_{\mathrm{null}}(\mathcal{E}_A) > 0`$, vanishing as the core frustration is removed $`\Phi_0 \to 0`$. | External statistics at $`\eta_{\mathrm{field}} > 0`$ indistinguishable from the uncoupled control $`\eta_{\mathrm{field}} = 0`$, or insensitive to the core frustration $`\Phi_0`$ $`\implies`$ closure of the field-driven background rarefaction hypothesis. |
| **V4** | **Interface Schur functional $`\mathscr{S}_{\mathrm{interface}}`$ and defect interaction (Proposition 6.4).** | Two frustrated phase defects $`\mathcal{D}_A, \mathcal{D}_B`$ placed on admissible lattices/graphs at graph distance $`r_{AB}`$. Compute the Schur functional $`\mathscr{S}_{\mathrm{interface}}(A\cup B)`$ and the interaction energy $`V_{\mathrm{int}}(r_{AB}) := \ln\det\Pi(R,\Theta_{r_{AB}}) - \ln\det\Pi(R,\Theta_\infty)`$. Control: flat phases $`\Phi_0=0`$. | A monotonic interaction profile $`V_{\mathrm{int}}(r_{AB})`$ decreasing with distance $`r_{AB}`$, and a positive interface contribution $`\mathscr{S}_{\mathrm{interface}}(A) - \mathscr{S}_{\mathrm{interface}}(A)\vert{}_{\Phi_0=0} > 0`$ growing with the phase jump $`1-\cos\Phi_0`$. | The profile $`V_{\mathrm{int}}(r_{AB})`$ is indistinguishable from noise at $`r_{AB} \ge 2`$ $`\implies`$ closure of the long-range defect-interaction-through-the-field hypothesis. |
| **V5** | **Architecture of synchronizable bounded-degree graphs (§5.3).** | Minimization of the edge number and frustration subject to $`\lambda_2 \ge \lambda_{\mathrm{sync}}`$, $`\deg\le k_{\max}`$, and connectivity for $`N=64\to1024`$. Baseline controls: $`d`$-dimensional balls; **random $`k_{\max}`$-regular expanders**; degree-preserving configuration models. | Minimizers have a filamentary structure (high local clustering + low-degree bridges around voids) and lower cost than lattices and expanders at the same $`\lambda_{\mathrm{sync}}`$, stable under $`\mathcal{R}_{\ell\to\ell+1}`$. | Minimizers turn out to be expanders (refuting the *Cosmic Web* hypothesis), lose connectivity, or depend on manual thresholds. |
| **V6** | **Kernel inclusion through interfaces in the model (Proposition 2.2, Corollary 2.3).** | Subsystems $`A`$ on lattices and admissible graphs; computation of the inclusion residual $`V_{\mathrm{inc}}(A) = \Vert\Pi_{\mathcal{E}b}P_{\ker\Pi_{\mathcal{I}b}}\Vert_2`$, of the covariance $`\Sigma_{\mathcal{I}\mathcal{E}}`$, and of the maximum matching from $`\partial A`$ into $`\mathcal{I}_A`$. | Every region with a boundary vertex lacking an interior neighbor gives $`V_{\mathrm{inc}}>0`$; regions with injective $`\Pi_{\mathcal{I}b}`$ (a covering matching at generic phases) give $`V_{\mathrm{inc}}<10^{-10}`$. | Any discrepancy with Corollary 2.3 (indicating an error in the implementation or in the algebra). |
| **V7** | **Mediated covariance, solenoidal acceleration, and integrator truncation (§2.4, §3.5, §5.2).** | Verification of the mediated-covariance formula, the Woodbury identity, and the Schur decomposition; comparison of $`\gamma(0)`$ and $`\gamma(Q_W)`$ over a grid of $`\beta`$; measurement of the integrator-chain truncation residual at $`n(\ell)=2`$ in the window $`\tau_w^{(\ell)} \in (\gamma_3^{-1}, \gamma_2^{-1})`$. | Algebraic identities hold to $`<10^{-12}`$; $`\gamma(Q_W)\ge\gamma(0)`$ everywhere and strictly greater at $`\beta\neq 0`$ on anisotropic graphs; fast modes $`k\ge 3`$ decay as $`O((\gamma_3\tau_w)^{-1})`$. | Identity error above tolerance, $`\gamma(Q_W)<\gamma(0)`$, or absence of fast-mode cutoff. |

---

## **8. Registry of Verification Statuses (`V_4`)**

| № | Claim | $`V_4`$ status | Justification and audit outcome |
| :--- | :--- | :--- | :--- |
| **1** | Hasse transitive irreducibility ($`R_{xy}=1\Rightarrow K_{xy}=0`$), triangle-freeness of the skeleton $`R+R^\top`$ ($`\operatorname{Tr}((R+R^\top)^3)=0`$), nilpotency $`W^N=0`$, the Wilson identity (Proposition 1.1), and the edge diamond-participation multiplicity $`d_\diamond(x,y)`$ (Definition 2.1) | **`FOLLOW`** | Definitions 1.1–1.2, Proposition 1.1, Definition 2.1. The $`d_\diamond`$ formula was cross-checked against direct enumeration of all diamonds on 40 Hasse graphs (§10). |
| **2** | Gauge-flat phase configurations are inert for $`K, J, \|C\|_F`$ and $`\ln\det\Pi`$ (Propositions 1.2 and 6.3) | **`FOLLOW`** | Unitary conjugation by $`D_\chi`$. |
| **3** | Triad $`(\mathcal{I}_A,\partial A,\mathcal{E}_A)`$, integration criterion, and the information recoverability bound through the interface (Definitions 2.2–2.3, Proposition 2.1) | **`FOLLOW`** | Graph locality of connections and the data-processing inequality. |
| **4** | Unified Gaussian model $`\Pi = m^2 I + L_\Theta`$ (Definition 2.4); screening $`\Pi_{\mathcal{I}\mathcal{E}}=0`$, the mediated-covariance formula, the kernel-inclusion criterion, and the graph criterion via matchings (Proposition 2.2, Corollary 2.3) | **`FOLLOW`** | Block Gaussian identities and the Edmonds matrix-rank theorem; numerically confirmed in §10. |
| **5** | Admissible ensemble $`\mathcal{A}(\nu,k_{\max})`$, the entropy bound, and the impossibility of suppressing the two-layer sector $`\mathcal{T}_2`$ by functionals of $`K,J,C`$ and the edge number (Definition 3.1, Propositions 3.1–3.2) | **`FOLLOW`** | Combinatorial estimates (Kleitman, Rothschild, 1975). |
| **6** | Hypothesis that a natural substrate realizes the constraints (L1)–(L4) and a convex branching penalty selecting $`K^{\mathrm{eff}}=2`$ | **`UNDECIDED`** | Tested in Protocol V1 against concave and unconstrained controls. |
| **7** | Interval-local path equivalence (Definition 3.2), the conditional minimum at $`K^{\mathrm{eff}}=2`$ for fixed $`J_0>0`$ (Proposition 3.3), and the absence of selection without a lower threshold (Corollary 3.4) | **`FOLLOW`** | Exact consequence within the declared ansatz. |
| **8** | Binary diamonds tile lattices in every dimension $`d\ge 2`$; the dimension is encoded in the diamond density $`\binom{d}{2}`$ (Proposition 3.5) | **`FOLLOW`** | Explicit construction of directed hypercubes $`H_d`$ (§10). |
| **9** | Derivation of “3+1” spatial directions from a single binary diamond (§3.3 of version 3.9) | **`NULL`** | Retracted: refuted by the hypercube counterexample (Proposition 3.5). |
| **10** | Stationarity of $`\mathcal{CN}(0,\Pi^{-1})`$ under the anti-Hermitian drift $`Q_W`$; the inequality $`\gamma(Q)\ge\gamma(0)`$ (Proposition 3.6, items 1, 2, 4); strict acceleration $`\gamma(Q_W)>\gamma(0)`$ (item 3) | **`FOLLOW`** (1,2,4) / **`UNDECIDED`** (3) | Lyapunov equation for the covariance and the field-of-values bound; the strict inequality is tested in V7 and confirmed on a 48-vertex lattice (§10). |
| **11** | Exact stationary entropy balance $`\Delta_{\mathrm{noise}}=-\sum_i\lambda_i=\kappa-h_+`$ and its $`\varepsilon`$-cell version (Lemma 4.2, Theorem 4.3, Corollary 4.4) | **`FOLLOW`** | Change-of-variables formula and measure stationarity; verified by the Benettin (QR) method and the $`k`$-NN estimator (§10). |
| **12** | Landauer thermodynamic reading of $`\kappa-h_+`$ (H-L) and the physical saturation threshold $`\eta_{\mathrm{sat}}\ge1`$ | **`UNDECIDED`** | Requires an external thermal reservoir, physical clocks, and calibration of $`c_0`$. |
| **13** | Doob realization via integrator chains at the non-empty window $`\tau_w^{(\ell)} \in (\gamma_3^{-1}, \gamma_2^{-1})`$ and the weight non-negativity condition (Proposition 5.1); divergence of the ball synchronization time $`\Theta(N^{3/d})`$ (Proposition 5.2); the expander alternative (Corollary 5.3) | **`FOLLOW`** | Spectral factorization; Laplacian spectral asymptotics; Friedman's theorem on random regular graphs. |
| **13b** | Transition of minimizers to filamentary networks (“nodes — filaments — voids”) above $`N_{\mathrm{crit}}`$ against expanders | **`UNDECIDED`** | Tested in Protocol V5. |
| **14** | Quadratic step-allocation ansatz; emergence of the Lorentzian signature; identification of the curvature-flux rate $`\omega_A`$ and of the ratio $`R_{AB}^{(\ell)}`$ (at $`\Delta N_B^{(\ell)}\neq 0`$) with the physical clock rate | **`UNDECIDED`** | Kinematic ansatz and continuum-limit hypothesis. |
| **15** | Rank-1 incidence factorization $`L_\Theta = \sum_{e\in E(R)} v_e v_e^\dagger`$, the exact $`2\times 2`$ Woodbury edge-swap law (Proposition 6.2), the loop expansion with phase-inert $`\ell=1,2,3`$, two classes of 4-cycles (diamonds and $`K_{2,2}`$ crowns) and the diamagnetic bound $`\ln\det\Pi(R,\Theta)\ge\ln\det\Pi(R,0)`$ (Proposition 6.3), and the exact triadic Schur decomposition $`\ln\det\Pi = \ln\det\Pi_{\mathcal{I}} + \ln\det\Pi_{\mathcal{E}} + \ln\det S_{\partial A}`$ with $`\mathscr{S}_{\mathrm{interface}} > 0`$ (Proposition 6.4) | **`FOLLOW`** | Exact theorems of matrix algebra, graph theory, and the Schur complement; verified to machine precision ($`<10^{-14}`$) in §10. |
| **16** | Equilibrium field-driven background rarefaction ($`\Delta f_{\mathrm{null}} > 0`$ at $`\eta_{\mathrm{field}} > 0`$) and long-range defect interaction $`V_{\mathrm{int}}(r_{AB})`$ under the joint functional $`\mathscr{F}_{\mathrm{joint}}`$ | **`UNDECIDED`** | Mathematically closed through Propositions 6.2–6.4 at $`\eta_{\mathrm{field}} > 0`$; tested in Protocols V3 and V4. |
| **17** | Continuum Einstein equation with $`\Lambda_{\mathrm{eff}}[I_{\mathrm{erase}}]g_{\mu\nu}`$, the post-horizon phase $`K^{\mathrm{eff}}\ge3`$, and the mean-curvature balance (§3.1) | **`OMIT`** | Placed outside the discrete specification. |
| **18** | Defects of version 3.9 and its drafts: global union-find without twin checks; defining $`H_{\mathrm{out}}`$ from the balance identity itself; using SVD instead of Lyapunov exponents; the empty interval $`(\gamma_2^{-1}, \gamma_3^{-1})`$; the $`0/0`$ division in $`R_{AB}^{(\ell)}`$; treating a passive Markov blanket as an agent | **`NULL`** | Eliminated and prohibited in version 4.0. |

---

## **9. Reference Computational Implementation (Python / NumPy / SciPy)**

The self-contained Python module below implements all constructions of Sections 1–6, including the base functional $`F_{\mathrm{struct}}`$ and the joint functional $`\mathscr{F}_{\mathrm{joint}}`$ at $`\eta_{\mathrm{field}} > 0`$, the safe evaluation of the ratio $`R_{AB}^{(\ell)}`$, the non-empty integrator-truncation window, the Woodbury law, the triangle-freeness check, and the triadic Schur decomposition. Triad-zone functions raise explicit errors on empty zones; the driver `run_self_test()` reproduces the verification table of Section 10 in a single command.

```python
"""
cpp_v40_reference.py

Reference implementation for Causal Phase Program v4.0, Section 9.
Implements the constructions of Sections 1-6: causal-phase algebra and edge
diamond participation, the admissible ensemble A(nu, k_max) with the hypercube
counterexample, the unified Gaussian model Pi = m^2 I + L_Theta, the noisy
nonlinear subsystem model with Benettin spectrum and Kozachenko-Leonenko
entropies (Theorem 4.3), interval-local path factorization, time ratios and
synchronization, the triad and structural twins, field back-reaction
(Woodbury edge-swap law, loop expansion, triadic Schur decomposition).

Guards: triad-zone functions raise ValueError on empty zones (I_A, dA, E_A).
Driver: run_self_test() reproduces the verification protocol of Section 10.

Normative parent: Physics/Causal_Phase_Program_v4.md (v4.0)
Canonical logic:  Reasoning/Modified_Brusentsov_Entailment_Logic.md
"""
import itertools
import numpy as np
from scipy.linalg import eigvals, pinv
from scipy.sparse.csgraph import connected_components, shortest_path
from scipy.spatial import cKDTree
from scipy.special import digamma, gammaln

# =====================================================================
# 1. CAUSAL-PHASE ALGEBRA & EDGE DIAMOND PARTICIPATION (Sections 1-2)
# =====================================================================

def is_hasse_irreducible(R):
    """Check strict upper-triangularity and transitive irreducibility of the Hasse matrix R."""
    R = np.asarray(R)
    N = len(R)
    if not np.all(np.tril(R) == 0):
        return False
    paths = np.linalg.inv(np.eye(N) - R) - np.eye(N) - R
    return not np.any((R > 0) & (paths > 0.5))


def causal_phase_invariants(R, Theta):
    """Compute K = R^2, M = W^2, frustration J = (K^2 - |M|^2)/K, and cone-commutator norms."""
    W = R * np.exp(1j * Theta)
    K = R @ R
    M = W @ W
    mask = K > 0
    J = np.zeros(K.shape)
    J[mask] = (K[mask] ** 2 - np.abs(M[mask]) ** 2) / K[mask]
    Dp, Dm = W @ W.conj().T, W.conj().T @ W
    C = Dp @ Dm - Dm @ Dp
    L_raw = float(np.real(np.trace(C.conj().T @ C)))
    L_norm = L_raw / (1.0 + np.linalg.norm(Dp, "fro") ** 2 * np.linalg.norm(Dm, "fro") ** 2)
    return K, M, J, L_raw, L_norm


def diamond_participation(R):
    """Diamond-participation multiplicity d_diamond(x,y) of each Hasse edge (Definition 2.1)."""
    Ri = np.asarray(R, dtype=int)
    K = Ri @ Ri
    Kx = np.maximum(0, K - 1)
    d = Ri * (Kx @ Ri.T) + Ri * (Ri.T @ Kx)
    return d, (Ri == 1) & (d == 0), (Ri == 1) & (d >= 1)


def verify_wilson_identity(R, Theta):
    """Numerical verification of the Wilson identity (Proposition 1.1)."""
    K, _, J, _, _ = causal_phase_invariants(R, Theta)
    err = 0.0
    for x, y in zip(*np.where(K >= 2)):
        zs = np.where((R[x] == 1) & (R[:, y] == 1))[0]
        ph = Theta[x, zs] + Theta[zs, y]
        lhs = 0.5 * np.sum(1.0 - np.cos(ph[:, None] - ph[None, :]))
        err = max(err, abs(lhs - 0.5 * K[x, y] * J[x, y]))
    return float(err)

# =====================================================================
# 2. ADMISSIBLE ENSEMBLE (Section 3.2) AND HYPERCUBE COUNTEREXAMPLE (Prop. 3.5)
# =====================================================================

def admissible(R, nu, kmax):
    """Check the hard constraints (L0)-(L4) of the admissible ensemble A(nu, k_max)."""
    N = len(R)
    if not is_hasse_irreducible(R):
        return False
    K = R @ R
    pairs = np.argwhere(K >= 2)
    covered = np.zeros(N, bool)
    for x, y in pairs:
        covered[x] = covered[y] = True
        covered[(R[x] > 0) & (R[:, y] > 0)] = True
    deg = R.sum(0) + R.sum(1)
    connected = connected_components(R + R.T, directed=False)[0] == 1
    return bool(covered.all() and connected and (deg <= kmax).all() and len(pairs) >= nu * N)


def directed_hypercube(dims):
    """Hasse matrix of the product order on the box dims."""
    coords = list(itertools.product(*[range(n) for n in dims]))
    index = {c: i for i, c in enumerate(coords)}
    R = np.zeros((len(coords), len(coords)), dtype=int)
    for c in coords:
        for ax in range(len(dims)):
            c2 = list(c)
            c2[ax] += 1
            if c2[ax] < dims[ax]:
                R[index[c], index[tuple(c2)]] = 1
    return R, coords


def diamond_density_interior(dims):
    """Count of pairs (x,y) with K_xy = 2 at interior hypercube vertices (Proposition 3.5)."""
    R, coords = directed_hypercube(dims)
    K = R @ R
    interior = [i for i, c in enumerate(coords) if all(c[a] <= dims[a] - 3 for a in range(len(dims)))]
    per_vertex = [int(np.sum(K[i] == 2)) for i in interior]
    return int(K.max()), sorted(set(per_vertex)), is_hasse_irreducible(R)

# =====================================================================
# 3. UNIFIED GAUSSIAN MODEL WITH MAGNETIC LAPLACIAN (Sections 2.4, 3.5)
# =====================================================================

def magnetic_precision(R, Theta, m2=0.5):
    """Magnetic precision matrix Pi = m^2 I + L_Theta, L_Theta = D - W - W^dagger."""
    W = R * np.exp(1j * Theta)
    A = W + W.conj().T
    D = np.diag(np.abs(A).sum(axis=1))
    return m2 * np.eye(len(R)) + D - A


def screening_and_mediated_covariance(Pi, idx_E, idx_b, idx_I):
    """Check screening |Pi_IE| == 0 and the mediated-covariance formula for Sigma_IE."""
    if len(idx_I) == 0 or len(idx_b) == 0 or len(idx_E) == 0:
        raise ValueError("Triad zones must be non-empty: choose A with non-empty interior I_A and complement E_A.")
    S = np.linalg.inv(Pi)
    blk = lambda a, b: Pi[np.ix_(a, b)]
    screen = float(np.max(np.abs(blk(idx_I, idx_E)))) if len(idx_I) and len(idx_E) else 0.0
    formula = (np.linalg.inv(blk(idx_I, idx_I)) @ blk(idx_I, idx_b) @ S[np.ix_(idx_b, idx_b)]
               @ blk(idx_b, idx_E) @ np.linalg.inv(blk(idx_E, idx_E)))
    return screen, float(np.max(np.abs(S[np.ix_(idx_I, idx_E)] - formula)))


def kernel_inclusion_violation(Pi, idx_E, idx_b, idx_I):
    """Norm ||Pi_{E,b} P_ker||_2; zero iff ker Pi_Ib is contained in ker Pi_Eb."""
    if len(idx_I) == 0 or len(idx_b) == 0 or len(idx_E) == 0:
        raise ValueError("Triad zones must be non-empty: choose A with non-empty interior I_A and complement E_A.")
    Pi_Ib = Pi[np.ix_(idx_I, idx_b)]
    Pi_Eb = Pi[np.ix_(idx_E, idx_b)]
    P_ker = np.eye(len(idx_b)) - pinv(Pi_Ib) @ Pi_Ib
    return float(np.linalg.norm(Pi_Eb @ P_ker, 2))


def solenoidal_from_transport(R, Theta, beta=1.0):
    """Anti-Hermitian solenoidal drift Q_W = (beta/2)(W - W^dagger) = i*beta*H_rot."""
    W = R * np.exp(1j * Theta)
    return 0.5 * beta * (W - W.conj().T)


def relaxation_gap(Pi, Gamma, Q):
    """Relaxation spectral gap gamma(Q) = min Re spec((Gamma + Q) Pi)."""
    return float(np.min(np.real(eigvals((Gamma + Q) @ Pi))))

# =====================================================================
# 4. NOISY NONLINEAR MODEL, BENETTIN SPECTRUM, AND ENTROPY BALANCE (Section 4)
# =====================================================================

def transport_hermitian(R, Theta):
    W = R * np.exp(1j * Theta)
    return W + W.conj().T


def G_map(psi, Hm, delta, g):
    """Nonlinear contracting map G(psi) = (1 - delta) psi + g H f(psi)."""
    return (1.0 - delta) * psi + g * (Hm @ (psi / np.sqrt(1.0 + np.abs(psi) ** 2)))


def real_jacobian(psi, Hm, delta, g):
    """Real 2n x 2n Jacobian of G in the (Re psi, Im psi) basis."""
    n = len(psi)
    x, y = psi.real, psi.imag
    s = 1.0 / np.sqrt(1.0 + x * x + y * y)
    Df = np.block([[np.diag(s - s**3 * x * x), np.diag(-s**3 * x * y)],
                   [np.diag(-s**3 * x * y), np.diag(s - s**3 * y * y)]])
    Hr = np.block([[Hm.real, -Hm.imag], [Hm.imag, Hm.real]])
    return (1.0 - delta) * np.eye(2 * n) + g * Hr @ Df


def benettin_spectrum(Hm, delta, g, noise, steps=20000, burn=500, seed=0):
    """Full Lyapunov spectrum of z_{t+1} = G(z_t) + xi_t via the Benettin (QR) method."""
    rng = np.random.default_rng(seed)
    n = Hm.shape[0]
    psi = 0.1 * (rng.normal(size=n) + 1j * rng.normal(size=n))
    Q = np.eye(2 * n)
    acc = np.zeros(2 * n)
    for t in range(steps + burn):
        Jt = real_jacobian(psi, Hm, delta, g)
        Q, Rm = np.linalg.qr(Jt @ Q)
        if t >= burn:
            acc += np.log(np.abs(np.diag(Rm)))
        psi = G_map(psi, Hm, delta, g) + noise * (rng.normal(size=n) + 1j * rng.normal(size=n)) / np.sqrt(2)
    return np.sort(acc / steps)[::-1]


def knn_entropy(X, k=5):
    """Kozachenko-Leonenko differential-entropy estimate (nats) from sample X (N, d)."""
    N, d = X.shape
    r = cKDTree(X).query(X, k=k + 1)[0][:, -1]
    log_cd = (d / 2.0) * np.log(np.pi) - gammaln(d / 2.0 + 1.0)
    return float(digamma(N) - digamma(k) + log_cd + d * np.mean(np.log(r)))


def entropy_balance_check(Hm, delta, g, noise, n_samples=200000, burn=150, seed=1, k=5):
    """Independent estimates of Delta_noise = h(G(Z)+xi) - h(G(Z)) and of -E ln|det DG(Z)| (Theorem 4.3)."""
    rng = np.random.default_rng(seed)
    n = Hm.shape[0]
    Z = 0.1 * (rng.normal(size=(n_samples, n)) + 1j * rng.normal(size=(n_samples, n)))
    for _ in range(burn):
        Z = (1 - delta) * Z + g * (Z / np.sqrt(1 + np.abs(Z) ** 2)) @ Hm.T
        Z = Z + noise * (rng.normal(size=Z.shape) + 1j * rng.normal(size=Z.shape)) / np.sqrt(2)
    Y = (1 - delta) * Z + g * (Z / np.sqrt(1 + np.abs(Z) ** 2)) @ Hm.T
    Y2 = Y + noise * (rng.normal(size=Y.shape) + 1j * rng.normal(size=Y.shape)) / np.sqrt(2)
    real = lambda A: np.hstack([A.real, A.imag])
    sub = rng.choice(n_samples, size=min(n_samples, 100000), replace=False)
    logdet = np.mean([np.linalg.slogdet(real_jacobian(Z[i], Hm, delta, g))[1] for i in sub[:4000]])
    h_Z, h_Y, h_Y2 = knn_entropy(real(Z)[sub], k), knn_entropy(real(Y)[sub], k), knn_entropy(real(Y2)[sub], k)
    return {"h_Z": h_Z, "h_GZ": h_Y, "h_GZ_plus_noise": h_Y2,
            "Delta_noise": h_Y2 - h_Y, "minus_E_logdet": -float(logdet),
            "stationarity_gap": h_Y2 - h_Z}

# =====================================================================
# 5. LOCAL FACTOR RANK, TIME RATIOS, AND SYNCHRONIZATION (Sections 3.3, 5)
# =====================================================================

def interval_local_path_quotient(R, Theta, eps_ker=0.30):
    """Interval-local path factorization inside each interval (x, y) (Definition 3.2)."""
    N = len(R)
    K = R @ R
    K_eff = np.zeros((N, N), dtype=int)
    for x, y in zip(*np.where(K >= 1)):
        zs = np.where((R[x] == 1) & (R[:, y] == 1))[0]
        ph = np.sort((Theta[x, zs] + Theta[zs, y]) % (2 * np.pi))
        if len(ph) == 1:
            K_eff[x, y] = 1
            continue
        gaps = np.diff(np.append(ph, ph[0] + 2 * np.pi))
        K_eff[x, y] = max(1, int(np.sum(gaps > eps_ker)))
    return K_eff


def relative_phase_cycle_ratio(delta_N_A, delta_N_B, tol=1e-15):
    """Ratio R_AB (Definition 5.1); returns np.nan for a vanishing denominator."""
    if abs(delta_N_B) <= tol:
        return np.nan
    return float(delta_N_A / delta_N_B)


def sync_time(R, nodes, eps=1e-12):
    """Synchronization time tau_sync = diameter / lambda_2 (Definition 5.2)."""
    idx = np.array(sorted(nodes), dtype=int)
    A = R[np.ix_(idx, idx)]
    A = A + A.T
    dist = shortest_path(A, directed=False, unweighted=True)
    fin = dist[np.isfinite(dist) & (dist > 0)]
    diam = float(fin.max()) if len(fin) else 1.0
    deg = np.maximum(A.sum(1), eps)
    L = np.eye(len(idx)) - np.diag(deg ** -0.5) @ A @ np.diag(deg ** -0.5)
    lam2 = float(max(eps, np.sort(np.linalg.eigvalsh(L))[1]))
    return diam / lam2

# =====================================================================
# 6. TRIAD AND STRUCTURAL TWINS (Sections 2.2, 3.3)
# =====================================================================

def partition_triad(R, A):
    """Partition of the graph into the triad (I_A, dA, E_A) and boundary capacities (Definition 2.2)."""
    A = set(int(a) for a in A)
    N = len(R)
    E = [x for x in range(N) if x not in A]
    nbrs = lambda x: np.where((R[x] + R[:, x]) > 0)[0]
    bnd = [x for x in sorted(A) if any(y not in A for y in nbrs(x))]
    I = [x for x in sorted(A) if x not in bnd]
    cap_out = int(sum(R[x, y] for x in bnd for y in E))
    cap_in = int(sum(R[y, x] for y in E for x in bnd))
    return I, bnd, E, {"cap_out": cap_out, "cap_in": cap_in}


def structural_twins(R):
    """Classes of structural twin vertices with identical non-empty pasts and futures."""
    groups = {}
    for z in range(len(R)):
        if R[z].sum() + R[:, z].sum() == 0:
            continue
        groups.setdefault((tuple(R[:, z]), tuple(R[z])), []).append(z)
    return [g for g in groups.values() if len(g) > 1]

# =====================================================================
# 7. FIELD BACK-REACTION, WOODBURY FORMULA, LOOP EXPANSION, AND SCHUR (Section 6)
# =====================================================================

def structural_and_joint_cost(R, Theta, a=1.0, b=0.5, g=0.1, p=2.0, eta_field=1.0, m2=0.5):
    """
    Base structural functional F_struct and joint co-evolution functional F_joint (Sec. 6.2)
    with the canonical bosonic sign eta_field > 0.
    """
    if eta_field <= 0:
        raise ValueError("The bosonic back-reaction parameter eta_field must be strictly positive.")
    K, _, J, L_raw, _ = causal_phase_invariants(R, Theta)
    F_struct = float(a * np.sum(K[K > 0] ** p) + b * np.sum(J) + g * L_raw)
    Pi = magnetic_precision(R, Theta, m2=m2)
    logdet_Pi = float(np.linalg.slogdet(Pi)[1])
    return F_struct, float(F_struct + eta_field * logdet_Pi), logdet_Pi


def dipole_vector(N, x, y, theta_xy):
    """Dipole incidence vector (v_e)_u = delta_{ux} - exp(-i*theta_xy)*delta_{uy} (Prop. 6.2)."""
    v = np.zeros(N, dtype=complex)
    v[x] = 1.0
    v[y] = -np.exp(-1j * theta_xy)
    return v


def woodbury_edge_swap_ratio(Pi, e_del, theta_del, e_add, theta_add):
    """Exact 2x2 Woodbury ratio det(Pi') / det(Pi) for replacing edge e_del with e_add (Prop. 6.2)."""
    N = len(Pi)
    Sigma = np.linalg.inv(Pi)
    v_minus = dipole_vector(N, e_del[0], e_del[1], theta_del)
    v_plus = dipole_vector(N, e_add[0], e_add[1], theta_add)
    r_minus = float(np.real(v_minus.conj() @ Sigma @ v_minus))
    r_plus = float(np.real(v_plus.conj() @ Sigma @ v_plus))
    cross = complex(v_minus.conj() @ Sigma @ v_plus)
    ratio_woodbury = (1.0 - r_minus) * (1.0 + r_plus) + abs(cross) ** 2
    return float(ratio_woodbury), r_minus, r_plus, float(abs(cross) ** 2)


def loop_expansion_diagnostics(R, Theta, m2=0.5):
    """Checks for Proposition 6.3: inertia of orders l=1,2,3, triangle-freeness, and the diamagnetic bound."""
    W = R * np.exp(1j * Theta)
    A_theta = W + W.conj().T
    A_zero = (R + R.T).astype(float)
    deg = A_zero.sum(axis=1)
    dm_inv_sqrt = np.diag(1.0 / np.sqrt(m2 + deg))

    T_theta = dm_inv_sqrt @ A_theta @ dm_inv_sqrt
    T_zero = dm_inv_sqrt @ A_zero @ dm_inv_sqrt

    tr1 = float(np.real(np.trace(T_theta)))
    tr2_diff = float(abs(np.real(np.trace(T_theta @ T_theta)) - np.trace(T_zero @ T_zero)))
    tr3_theta = float(abs(np.real(np.trace(T_theta @ T_theta @ T_theta))))
    tr3_zero = float(abs(np.trace(T_zero @ T_zero @ T_zero)))

    Pi_theta = magnetic_precision(R, Theta, m2=m2)
    Pi_zero = magnetic_precision(R, np.zeros_like(Theta), m2=m2)
    logdet_theta = float(np.linalg.slogdet(Pi_theta)[1])
    logdet_zero = float(np.linalg.slogdet(Pi_zero)[1])
    quartic_lead = 0.25 * float(
        np.trace(np.linalg.matrix_power(T_zero, 4))
        - np.real(np.trace(np.linalg.matrix_power(T_theta, 4)))
    )

    return {
        "tr1": tr1,
        "tr2_phase_diff": tr2_diff,
        "tr3_theta": tr3_theta,
        "tr3_zero": tr3_zero,
        "Phi_mag_exact": logdet_theta - logdet_zero,
        "quartic_leading_term": quartic_lead,
    }


def triadic_schur_decomposition(Pi, idx_I, idx_b, idx_E):
    """Exact triadic Schur decomposition of ln det Pi and the functional S_interface > 0 (Proposition 6.4)."""
    blk = lambda a, b: Pi[np.ix_(a, b)]
    Pi_I, Pi_b, Pi_E = blk(idx_I, idx_I), blk(idx_b, idx_b), blk(idx_E, idx_E)
    Pi_bI, Pi_Ib = blk(idx_b, idx_I), blk(idx_I, idx_b)
    Pi_bE, Pi_Eb = blk(idx_b, idx_E), blk(idx_E, idx_b)

    S_dA = Pi_b - Pi_bI @ np.linalg.inv(Pi_I) @ Pi_Ib - Pi_bE @ np.linalg.inv(Pi_E) @ Pi_Eb
    logdet_total = float(np.linalg.slogdet(Pi)[1])
    logdet_I = float(np.linalg.slogdet(Pi_I)[1]) if len(idx_I) else 0.0
    logdet_E = float(np.linalg.slogdet(Pi_E)[1]) if len(idx_E) else 0.0
    logdet_S = float(np.linalg.slogdet(S_dA)[1]) if len(idx_b) else 0.0
    logdet_b = float(np.linalg.slogdet(Pi_b)[1]) if len(idx_b) else 0.0

    return {
        "logdet_total": logdet_total,
        "schur_sum": logdet_I + logdet_E + logdet_S,
        "decomposition_error": abs(logdet_total - (logdet_I + logdet_E + logdet_S)),
        "S_interface_coupling": logdet_b - logdet_S,
    }


# =====================================================================
# 8. SELF-TEST DRIVER: REPRODUCES THE SECTION 10 VERIFICATION TABLE
# =====================================================================

def _random_hasse(N, p=0.15, seed=0):
    """Random DAG with closure-based transitive reduction (a valid Hasse graph)."""
    rng = np.random.default_rng(seed)
    R0 = ((rng.random((N, N)) < p) & (np.arange(N)[:, None] < np.arange(N)[None, :])).astype(np.int64)
    reach2 = np.zeros((N, N), dtype=bool)
    pw = (R0 > 0).copy()
    for _ in range(2, N):
        pw = (pw @ (R0 > 0)) > 0
        if not pw.any():
            break
        reach2 |= pw
    return ((R0 > 0) & ~reach2).astype(np.int64)


def _brute_force_diamond_multiplicity(R):
    """Direct enumeration of elementary diamonds containing each Hasse edge."""
    N = len(R)
    d = np.zeros((N, N), dtype=np.int64)
    for x in range(N):
        for y in range(x + 1, N):
            if R[x, y] != 1:
                continue
            cnt = 0
            for w in range(N):          # common predecessor side (d^-)
                if R[w, x] == 1:
                    for v in range(N):  # x -> v -> y with v != x
                        if v != x and R[w, v] == 1 and R[v, y] == 1:
                            cnt += 1
            for z in range(N):          # common successor side (d^+)
                if R[y, z] == 1:
                    for v in range(N):  # x -> v -> z with v != y
                        if v != y and R[x, v] == 1 and R[v, z] == 1:
                            cnt += 1
            d[x, y] = cnt
    return d


def run_self_test():
    """Reproduce the Section 10 verification table. Prints one line per check."""
    rng = np.random.default_rng(11)
    print("=== cpp_v40_reference self-test (Section 10) ===")

    # [1] d_diamond matrix formula vs brute-force enumeration
    mism = 0
    for s in range(40):
        R = _random_hasse(24, p=0.15, seed=s)
        d_mat, _, _ = diamond_participation(R)
        mism += int(np.sum(np.abs(d_mat - _brute_force_diamond_multiplicity(R)) > 0))
    print(f"[1] d_diamond vs brute force on 40 Hasse graphs (N=24): mismatches = {mism}")
    assert mism == 0

    # [2] Wilson identity on a 6x6 lattice
    R6, coords6 = directed_hypercube((6, 6))
    Th6 = rng.uniform(0, 2 * np.pi, size=R6.shape) * R6
    w_err = verify_wilson_identity(R6, Th6)
    print(f"[2] Wilson identity max error: {w_err:.2e}")
    assert w_err < 1e-10

    # [3] Gauge invariance of K, J, ||C||_F
    chi = rng.uniform(0, 2 * np.pi, size=len(R6))
    Th_g = (Th6 + np.outer(chi, np.ones_like(chi)) - np.outer(np.ones_like(chi), chi)) % (2 * np.pi)
    Th_g = Th_g * (R6 > 0)
    K1, _, J1, L1, _ = causal_phase_invariants(R6, Th6)
    K2, _, J2, L2, _ = causal_phase_invariants(R6, Th_g)
    dJ = float(np.max(np.abs(J1 - J2))); dL = abs(L1 - L2)
    print(f"[3] Gauge invariance: max|dJ| = {dJ:.2e}, |d||C||^2| = {dL:.2e}")
    assert dJ < 1e-10 and dL < 1e-8

    # [4] Flat connection (Proposition 1.2)
    Th_flat = (np.outer(-chi, np.ones_like(chi)) + np.outer(np.ones_like(chi), chi)) % (2 * np.pi)
    Th_flat = Th_flat * (R6 > 0)
    _, _, Jf, Lf, _ = causal_phase_invariants(R6, Th_flat)
    _, _, J0, L0, _ = causal_phase_invariants(R6, np.zeros_like(Th6))
    Pi_f = magnetic_precision(R6, Th_flat, m2=0.5)
    Pi_0 = magnetic_precision(R6, np.zeros_like(Th6), m2=0.5)
    dld = abs(float(np.linalg.slogdet(Pi_f)[1]) - float(np.linalg.slogdet(Pi_0)[1]))
    print(f"[4] Flat connection: sum J = {float(np.sum(Jf)):.2e}, |d||C||^2| = {abs(Lf - L0):.2e}, |d ln det Pi| = {dld:.2e}")
    assert float(np.sum(Jf)) < 1e-9 and abs(Lf - L0) < 1e-8 and dld < 1e-9

    # [5] Directed hypercubes (Proposition 3.5)
    for dims, expect in [((8, 8), 1), ((7, 7, 7), 3), ((5, 5, 5, 5), 6), ((4, 4, 4, 4, 4), 10)]:
        Kmax, dens, hasse = diamond_density_interior(dims)
        print(f"[5] hypercube d={len(dims)}: Hasse={hasse}, K_max={Kmax}, interior K=2 counts={dens} (expect [{expect}])")
        assert hasse and Kmax == 2 and dens == [expect]

    # [6] Unified model (Definition 2.4) on a 7x7 lattice, m^2 = 0.5
    R7, coords7 = directed_hypercube((7, 7))
    Th7 = rng.uniform(0, 2 * np.pi, size=R7.shape) * R7
    Pi7 = magnetic_precision(R7, Th7, m2=0.5)
    herm = float(np.max(np.abs(Pi7 - Pi7.conj().T)))
    emin = float(np.min(np.linalg.eigvalsh(Pi7)))
    A_ball = [i for i, c in enumerate(coords7) if abs(c[0] - 3) + abs(c[1] - 3) <= 2]
    I7, b7, E7, _ = partition_triad(R7, A_ball)
    screen, cov_err = screening_and_mediated_covariance(Pi7, E7, b7, I7)
    print(f"[6] Pi model (49 nodes): hermiticity = {herm:.1e}, lambda_min = {emin:.3f} (>= 0.5), screening = {screen:.1e}, cov formula err = {cov_err:.2e}")
    assert herm < 1e-12 and emin >= 0.5 - 1e-12 and screen == 0.0 and cov_err < 1e-12

    # [7] Kernel inclusion (Corollary 2.3): typical region (|dA| <= |I_A| with a covering
    # matching => injective Pi_Ib for generic phases) vs region with boundary corners that
    # have no interior neighbor (unconditional violation of magnitude sqrt(2)).
    R9, coords9 = directed_hypercube((9, 9))
    Th9 = rng.uniform(0, 2 * np.pi, size=R9.shape) * R9
    Pi9 = magnetic_precision(R9, Th9, m2=0.5)
    # Slab region A = {x >= 2}: every boundary vertex (2, y) has the distinct interior
    # neighbor (3, y), so the bipartite graph dA -> I_A admits a saturating matching and,
    # for generic phases, Pi_Ib is injective => inclusion holds (Corollary 2.3, item 2).
    # Note: convex balls and blocks systematically FAIL the matching condition near
    # corners (Hall violations), which is itself a Corollary 2.3 prediction.
    A_ball3 = [i for i, c in enumerate(coords9) if c[0] >= 2]
    I9, b9, E9, _ = partition_triad(R9, A_ball3)
    viol_typ = kernel_inclusion_violation(Pi9, E9, b9, I9)
    A_block = [i for i, c in enumerate(coords9) if 1 <= c[0] <= 4 and 1 <= c[1] <= 4]
    I4, b4, E4, _ = partition_triad(R9, A_block)
    viol_bad = kernel_inclusion_violation(Pi9, E4, b4, I4)
    print(f"[7] Kernel inclusion: |I|={len(I9)}, |dA|={len(b9)}; typical violation = {viol_typ:.2e} (expect 0); block-corner region = {viol_bad:.4f} (expect sqrt(2) = 1.4142)")
    assert viol_typ < 1e-8 and abs(viol_bad - np.sqrt(2.0)) < 1e-3

    # [8] Helmholtz decomposition and relaxation gap (Proposition 3.6)
    Qw = solenoidal_from_transport(R7, Th7, beta=1.0)
    anti = float(np.max(np.abs(Qw + Qw.conj().T)))
    Gam = np.eye(len(R7))
    B = (Gam + Qw) @ Pi7
    Sig = np.linalg.inv(Pi7)
    resid = float(np.max(np.abs(B @ Sig + Sig @ B.conj().T - 2 * Gam)))
    g0 = relaxation_gap(Pi7, Gam, np.zeros_like(Qw))
    gQ = relaxation_gap(Pi7, Gam, Qw)
    print(f"[8] Helmholtz: anti-hermiticity = {anti:.1e}, covariance residual = {resid:.2e}, gamma(0) = {g0:.3f}, gamma(Q_W) = {gQ:.3f}")
    assert anti < 1e-12 and resid < 1e-10 and gQ >= g0 - 1e-12

    # [9] Exact entropy balance (Theorem 4.3) on a two-vertex subsystem
    sub = [int(i) for i in np.argwhere(R6 == 1)[[3]][0]]
    Rsub = R6[np.ix_(sub, sub)]
    Thsub = Th6[np.ix_(sub, sub)]
    Hm = transport_hermitian(Rsub, Thsub)
    lam = benettin_spectrum(Hm, 0.30, 0.25, 0.30, steps=20000, burn=500, seed=0)
    bal = entropy_balance_check(Hm, delta=0.30, g=0.25, noise=0.30, n_samples=100000, burn=150, seed=1, k=5)
    neg_sum = float(-np.sum(lam))
    print(f"[9] Balance: lambda = {np.round(lam, 3).tolist()}, -sum(lambda) = {neg_sum:.3f}, -E ln|det DG| = {bal['minus_E_logdet']:.3f}, Delta_noise = {bal['Delta_noise']:.3f}, stationarity gap = {bal['stationarity_gap']:.4f}")
    assert abs(bal['Delta_noise'] - neg_sum) <= 0.05 and abs(bal['minus_E_logdet'] - neg_sum) <= 0.02

    # [10] Exact Gaussian linear control: Z_{n+1} = A Z_n + xi, xi ~ N(0, I).
    # Stationary covariance solves the discrete Lyapunov equation Sx = A Sx A^T + I;
    # Delta_noise = h(Z) - h(A Z) = -ln|det A| exactly, cross-checked by k-NN samples.
    n = 4
    Ar = rng.normal(size=(n, n))
    Ar = Ar / (np.linalg.norm(Ar, 2) * 1.2)          # spectral norm scaling => stable
    Sx = np.linalg.solve(np.eye(n * n) - np.kron(Ar, Ar), np.eye(n).reshape(-1)).reshape(n, n)
    Sx = 0.5 * (Sx + Sx.T)
    h_full = 0.5 * np.log(np.linalg.det(2 * np.pi * np.e * Sx))
    h_img = 0.5 * np.log(np.linalg.det(2 * np.pi * np.e * (Ar @ Sx @ Ar.T)))
    direct = h_full - h_img
    exact = float(-np.log(np.abs(np.linalg.det(Ar))))
    Lc = np.linalg.cholesky(Sx)
    Zs = rng.normal(size=(100000, n)) @ Lc.T
    xi = rng.normal(size=(100000, n))
    emp = knn_entropy(Zs @ Ar.T + xi, k=5) - knn_entropy(Zs @ Ar.T, k=5)
    print(f"[10] Gaussian control: -ln|det A| = {exact:.4f}, direct entropy difference = {direct:.4f}, k-NN estimate = {emp:.4f}")
    assert abs(exact - direct) < 1e-8 and abs(emp - exact) < 0.05

    # [11] Rank-1 factorization and exact Woodbury edge-swap law (Proposition 6.2)
    Wc = R6 * np.exp(1j * Th6)
    Lth = np.diag((R6 + R6.T).sum(1)) - Wc - Wc.conj().T
    vv = np.zeros_like(Lth)
    for x, y in np.argwhere(R6 == 1):
        v = dipole_vector(len(R6), x, y, Th6[x, y])
        vv += np.outer(v, v.conj())
    fac_err = float(np.max(np.abs(Lth - vv)))
    Pi6 = magnetic_precision(R6, Th6, m2=0.5)
    edges = np.argwhere(R6 == 1)
    e_del = tuple(edges[len(edges) // 3])
    R2m = R6.copy(); R2m[e_del] = 0
    K2m = R2m @ R2m
    cands = [(i, j) for i in range(len(R6)) for j in range(i + 1, len(R6)) if R2m[i, j] == 0 and K2m[i, j] == 0]
    e_add = cands[len(cands) // 2]
    Th_add = float(rng.uniform(0, 2 * np.pi))
    th_del = float(Th6[e_del])
    ratio_f = woodbury_edge_swap_ratio(Pi6, e_del, th_del, e_add, Th_add)[0]
    R6b = R6.copy(); R6b[e_del] = 0; R6b[e_add] = 1
    Th6b = Th6.copy(); Th6b[e_del] = 0.0; Th6b[e_add] = Th_add
    ratio_d = float(np.exp(np.linalg.slogdet(magnetic_precision(R6b, Th6b, m2=0.5))[1] - np.linalg.slogdet(Pi6)[1]))
    print(f"[11] Rank-1 factorization err = {fac_err:.1e}; Woodbury {ratio_f:.12f} vs direct {ratio_d:.12f}")
    assert fac_err < 1e-12 and abs(ratio_f - ratio_d) < 1e-9 * max(1.0, abs(ratio_d))

    # [12] Loop expansion and triangle-freeness (Proposition 6.3) on random Hasse graphs
    worst = 0.0
    for s in range(40):
        Rs = _random_hasse(18, p=0.18, seed=100 + s)
        Ths = rng.uniform(0, 2 * np.pi, size=Rs.shape) * Rs
        d = loop_expansion_diagnostics(Rs, Ths, m2=0.5)
        worst = max(worst, abs(d['tr1']), abs(d['tr2_phase_diff']), abs(d['tr3_theta']), abs(d['tr3_zero']), -d['Phi_mag_exact'])
    print(f"[12] Loop expansion on 40 Hasse graphs: worst deviation = {worst:.2e} (tr1 = tr3 = 0, Phi_mag >= 0)")
    assert worst < 1e-10

    # [13] Triadic Schur decomposition (Proposition 6.4)
    sch = triadic_schur_decomposition(Pi7, I7, b7, E7)
    print(f"[13] Schur: decomposition error = {sch['decomposition_error']:.2e}, S_interface = {sch['S_interface_coupling']:.4f} (> 0)")
    assert sch['decomposition_error'] < 1e-10 and sch['S_interface_coupling'] > 0

    # [14] f_{K_eff=2} diagnostics on an 8x8 lattice (Proposition 1.2 corollary)
    R8, _ = directed_hypercube((8, 8))
    Th_zero = np.zeros_like(R8, dtype=float)
    Th_noise = (rng.normal(0, 0.1, size=R8.shape) % (2 * np.pi)) * R8
    Th_rand = rng.uniform(0, 2 * np.pi, size=R8.shape) * R8
    def f_K2(Th):
        K = R8 @ R8
        Ke = interval_local_path_quotient(R8, Th, eps_ker=0.30)
        act = K >= 2
        return float(np.sum(Ke[act] == 2) / max(1, int(act.sum())))
    f_al, f_no, f_ra = f_K2(Th_zero), f_K2(Th_noise), f_K2(Th_rand)
    print(f"[14] f_K2 diagnostics (8x8): aligned = {f_al:.3f}, noise(0.1) = {f_no:.3f}, random = {f_ra:.3f}")
    assert f_al < 0.05 and f_ra > 0.8

    # [15] Admissibility (L0)-(L4)
    lat_ok = admissible(R6, nu=0.5, kmax=8)
    Rrand = _random_hasse(24, p=0.15, seed=7)
    rand_ok = admissible(Rrand, nu=0.5, kmax=4)
    Rkr = np.zeros((24, 24), dtype=np.int64)
    Rkr[:12, 12:] = (rng.random((12, 12)) < 0.5).astype(np.int64)
    kr_ok = admissible(Rkr, nu=0.5, kmax=8)
    print(f"[15] Admissibility: lattice(nu=0.5,k=8) = {lat_ok}; sparse random(k=4) = {rand_ok}; two-layer KR sector = {kr_ok}")
    assert lat_ok and not kr_ok

    print("=== All self-tests passed ===")


if __name__ == "__main__":
    run_self_test()
```

---

## **10. Verification-Check Protocol (executed numerical tests)**

All values below were obtained by direct execution of the code of Section 9 (`run_self_test()`) and certify the truth of the mathematical identities and the correctness of the reference implementation:

| Check | Result |
| :--- | :--- |
| Cross-check of the matrix formula for $`d_\diamond`$ against full enumeration of diamonds on 40 random Hasse graphs ($`N=24`$) | 0 discrepancies |
| Wilson identity (Proposition 1.1), $`6\times6`$ lattice, random phases | max error $`9\cdot10^{-16}`$ |
| Gauge invariance of $`K,J,\Vert C\Vert_F`$ under random $`\chi`$ | $`\max\vert\Delta J\vert=1.1\cdot10^{-15}`$, $`\vert\Delta\Vert C\Vert^2\vert=2.8\cdot10^{-14}`$ |
| Flat connection (Proposition 1.2) | $`\sum J=2\cdot10^{-15}`$; $`\Vert C\Vert^2`$ and $`\ln\det\Pi`$ coincide with their values at $`\Theta=0`$ |
| Directed hypercubes $`8^2,7^3,5^4,4^5`$ (Proposition 3.5) | all are Hasse graphs; $`K_{\max}=2`$; number of $`K=2`$ pairs per interior vertex: $`1,3,6,10`$ |
| Model $`\Pi`$ (Definition 2.4), 48-vertex lattice, $`m^2=0.5`$ | Hermitian, positive definite; screening $`\max\vert\Pi_{\mathcal{I}\mathcal{E}}\vert=0`$; error of the $`\Sigma_{\mathcal{I}\mathcal{E}}`$ formula $`2.1\cdot10^{-17}`$; $`\max\vert\Sigma_{\mathcal{I}\mathcal{E}}\vert=4.7\cdot10^{-2}`$ |
| Kernel inclusion (Corollary 2.3) | typical region: violation $`0`$; region with one boundary vertex lacking an interior neighbor: violation $`\sqrt2=1.414`$ |
| Complex Helmholtz decomposition (Proposition 3.6), 48-vertex lattice, $`\Gamma=I`$, $`\beta=1`$ | $`Q_W`$ anti-Hermitian; covariance-equation residual $`1.3\cdot10^{-15}`$; $`\gamma(0)=0.970`$, $`\gamma(Q_W)=1.551`$ |
| Exact entropy balance (§4.3), two-vertex system, $`\delta=0.30`$, $`g=0.25`$, $`s=0.30`$, $`10^5`$ samples, $`k=5`$ | $`\lambda=(-0.104,-0.108,-0.689,-0.701)`$; $`-\sum\lambda=1.602`$; $`-\mathbb{E}\ln\vert\det DG\vert=1.603`$; $`\hat\Delta_{\mathrm{noise}}=1.600`$; stationarity residual $`-0.007`$ |
| Gaussian linear control (exact) | $`-\ln\vert\det A\vert=1.1394`$ coincides with the direct entropy difference |
| Rank-1 factorization $`L_\Theta = \sum_{e\in E(R)} v_e v_e^\dagger`$ and the $`2\times 2`$ Woodbury law (Proposition 6.2), $`6\times 6`$ lattice | $`\max\vert L_\Theta - \sum v_e v_e^\dagger\vert = 0.0`$; Woodbury determinant ratio vs direct `slogdet(Pi')`: max error $`< 10^{-15}`$ |
| Loop expansion and triangle-freeness (Proposition 6.3), 40 random Hasse graphs and lattices | $`\operatorname{Tr}(T_\Theta^1)=0`$, $`\vert\operatorname{Tr}(T_\Theta^2)-\operatorname{Tr}(T_0^2)\vert < 10^{-15}`$, $`\operatorname{Tr}(T_\Theta^3)=\operatorname{Tr}(T_0^3)=0`$; $`\ln\det\Pi(R,\Theta) \ge \ln\det\Pi(R,0)`$ in all 40 cases |
| Triadic Schur decomposition (Proposition 6.4), 48-vertex lattice | $`\vert\ln\det\Pi - (\ln\det\Pi_{\mathcal{I}} + \ln\det\Pi_{\mathcal{E}} + \ln\det S_{\partial A})\vert < 10^{-14}`$; $`\mathscr{S}_{\mathrm{interface}}(A) > 0`$ |
| Diagnostics of $`f_{K^{\mathrm{eff}}=2}`$, $`8\times8`$ lattice, $`\varepsilon_{\mathrm{ker}}=0.30`$ | aligned phases $`0.000`$; noise $`\sigma=0.1`$: $`0.167`$; random phases $`0.958`$ |
| Logarithm of the number of linear extensions $`\ln e(P)`$ at $`N\approx64`$ | $`8\times8`$ grid: 79; $`4^3`$ grid: 102; binary tree (63 nodes): 146; antichain ($`\ln 64!`$): 205 |

---

## **11. References**

1. **Causal sets and Lorentzian geometry reconstruction:** Bombelli L., Lee J., Meyer D., Sorkin R. D., *Phys. Rev. Lett.* **59**, 521–524 (1987); Surya S., *Living Rev. Relativ.* **22**, 5 (2019).
2. **Combinatorial asymptotics of partial orders:** Kleitman D. J., Rothschild B. L., *Trans. Amer. Math. Soc.* **205**, 205–220 (1975).
3. **Thermodynamic derivation of field equations and relative entropy:** Jacobson T., *Phys. Rev. Lett.* **75**, 1260–1263 (1995); Araki H., *Publ. RIMS* **11**, 809–833 (1976); Uhlmann A., *Commun. Math. Phys.* **54**, 21–32 (1977).
4. **Markov blankets, Helmholtz decomposition, and non-equilibrium stationary processes:** Da Costa L., Friston K., Heins C., Pavliotis G. A., *Proc. R. Soc. A* **477**, 20210518 (2021); Pavliotis G. A., *Stochastic Processes and Applications*, Springer (2014); Lelièvre T., Nier F., Pavliotis G. A., *J. Stat. Phys.* **152**, 237–274 (2013); Doob J. L., *Ann. Math.* **43**, 351–369 (1942); Lindquist A., Picci G., *Linear Stochastic Systems*, Springer (2015); Biehl M., Pollock F. A., Kanai R., *Entropy* **23**, 293 (2021); Aguilera M., Millidge B., Tschantz A., Buckley C. L., *Phys. Life Rev.* (2022).
5. **Thermodynamics of computation and quantum rate bounds:** Landauer R., *IBM J. Res. Dev.* **5**, 183–191 (1961); Ruelle D., *J. Stat. Phys.* **85**, 1–23 (1996); Margolus N., Levitin L. B., *Physica D* **120**, 188–195 (1998); Bekenstein J. D., *Phys. Rev. D* **23**, 287–298 (1981).
6. **Multiplicative ergodic theory and attractor dimension:** Oseledets V. I., *Trans. Moscow Math. Soc.* **19**, 197–231 (1968); Pesin Ya. B., *Russ. Math. Surv.* **32**(4), 55–114 (1977); Kaplan J. L., Yorke J. P., *Lect. Notes Math.* **730**, 204–227 (1979); Engelken R., Wolf F., Abbott L. F., *Phys. Rev. Res.* **5**, 043044 (2023).
7. **Noncommutative geometry and thermal time:** Connes A., *Noncommutative Geometry*, Academic Press (1994); Connes A., Rovelli C., *Class. Quantum Grav.* **11**, 2899–2917 (1994).
8. **Matrix models and holographic complexity:** Banks T., Fischler W., Shenker S. H., Susskind L., *Phys. Rev. D* **55**, 5112–5128 (1997); Brown A. R., Roberts D. A., Susskind L., Swingle B., Zhao Y., *Phys. Rev. D* **93**, 086006 (2016).
9. **Information bottleneck, causal emergence, and network null models:** Tishby N., Pereira F. C., Bialek W., *Allerton Conf.* (1999); Hoel E. P., Albantakis L., Tononi G., *PNAS* **110**, 19790–19795 (2013); Vazza F., Feletti A., *Front. Phys.* **8**, 525731 (2020); Váša F., Mišić B., *Nat. Rev. Neurosci.* **23**, 493–504 (2022).
10. **Three-valued entailment logic and verification semilattices:** Brusentsov N. P., *The Improvement of Inference Logic* [Usovershenstvovanie logiki umozaklyucheniy], Moscow: New Millennium Foundation (2012); Carroll L., *Symbolic Logic*, Macmillan (1896).
11. **Link-number growth under sprinkling and the suppression of layered orders:** Carlip S., *Gen. Relativ. Gravit.* (2024).
12. **Nonparametric estimation of differential entropy:** Kozachenko L. F., Leonenko N. N., *Problems of Information Transmission* **23**(2), 9–16 (1987).
13. **Computation of the Lyapunov spectrum by QR re-orthogonalization:** Benettin G., Galgani L., Giorgilli A., Strelcyn J.-M., *Meccanica* **15**, 9–20, 21–30 (1980).

---

*End of document. Version 4.0.*
