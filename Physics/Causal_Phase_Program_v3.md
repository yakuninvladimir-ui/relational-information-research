# Causal Phase Program, Version 3.9
## Mathematical Invariants of Multiscale Structuring: Internal Relief, Bilateral Interface, Dynamic Dimensional Reduction, and Channel Balance

**Author:** Vladimir Yakunin  
**Version:** 3.9  
**Date:** October 21, 2026  
**Status:** Self-contained formal specification and research program[cite: 35]. Strictly separates definitions, mathematical consequences within the model, and empirically testable physical hypotheses[cite: 35].

---

## Abstract

This specification formulates a mathematical framework describing how multiscale structures emerge, maintain stability, and interact within a discrete causal medium of bounded capacity[cite: 35]. Rather than postulating a pre-existing smooth manifold of fixed dimensionality, the foundational object is a finite, locally finite partial order of events equipped with unitary phase transport on immediate causal relations (Hasse links)[cite: 35].

Any persistent localized subsystem at a selected temporal window and resolution scale is represented as a triad $(\mathcal{I}_A, \partial A, \mathcal{E}_A)$: an internal relief (bulk) $\mathcal{I}_A$, a bilateral interface $\partial A$ of finite capacity, and an external causal synchronization channel $\mathcal{E}_A$[cite: 35]. The total system description decomposes into three distinct components: (1) the structural functional of the internal relief, (2) the kinematic scaffold of the external channel (unbranched null causal chains), and (3) the thermodynamic erasure flux across the interface[cite: 35].

Within this formalism, seven core mathematical results are established:
1. **Kernel-Path Factorization and Binary Causal Diamond Selection ($K_{xy}^{\mathrm{eff}} = 2$):** An equivalence relation on intermediate paths is defined via phase-mismatch tolerance (the kernel of the coarse-graining differential)[cite: 7, 35]. For any strictly convex branching-volume penalty on the quotient graph, the minimum cost subject to preserving non-zero gauge-invariant phase frustration is achieved uniquely on the binary causal diamond ($K_{xy}^{\mathrm{eff}} = 2$)[cite: 35].
2. **Precision Sparsity and the Boundary Kernel-Inclusion Theorem:** In the stationary Gaussian regime across the triad $(\mathcal{I}_A, \partial A, \mathcal{E}_A)$, conditional independence (Markov screening) corresponds to block sparsity of the precision operator ($\Pi_{\mathcal{I}\mathcal{E}} = 0$) while inducing non-zero long-range covariance $\Sigma_{\mathcal{I}\mathcal{E}} = -\Pi_{\mathcal{I}}^{-1}\Pi_{\mathcal{I},\partial A}\Sigma_{\partial A}\Pi_{\partial A,\mathcal{E}}\Pi_{\mathcal{E}}^{-1} \neq 0$[cite: 11, 26]. A well-defined synchronization map $\sigma(\overline{\mu}(b)) = \overline{\eta}(b)$ across the interface exists if and only if the boundary kernel-inclusion condition $\ker \Pi_{\mathcal{I},\partial A} \subseteq \ker \Pi_{\mathcal{E},\partial A}$ holds[cite: 12].
3. **Helmholtz Decomposition and Solenoidal Acceleration of Structural Relaxation:** Splitting the causal transport operator $W$ into its symmetric potential part $H_{\mathrm{sym}} = \frac{1}{2}(W + W^\dagger)$ and skew-Hermitian rotational (vortical) part $H_{\mathrm{rot}} = \frac{1}{2i}(W - W^\dagger)$[cite: 2, 35] provides the discrete counterpart of the continuous Helmholtz decomposition into time-reversible dissipative flow ($\Gamma \succeq 0$) and time-irreversible solenoidal flow ($Q = -Q^\top$)[cite: 15, 26]. Non-zero solenoidal circulation ($Q \neq 0$, $H_{\mathrm{rot}} \neq 0$) preserves the stationary distribution while strictly increasing or maintaining the spectral relaxation gap $\gamma(Q) \ge \gamma(0)$, accelerating convergence toward the structural attractor[cite: 19, 20, 32].
4. **Transverse Attractor Stiffness and Boundary Flux (the Oseledets–Landauer Bridge):** Applying Oseledets' multiplicative ergodic decomposition to the internal dynamics splits the tangent space into active directions along the attractor ($E^u$) and contracting transverse directions ($E^s$)[cite: 4, 35]. Under stationary measure preservation in the presence of boundary noise, the transverse phase-space contraction rate $\kappa(A) = \sum_{\lambda_i < 0} |\lambda_i|$ sets the lower bound on the information erasure flux that must be continuously expelled through the outgoing interface $\partial^+ A$ into the external channel[cite: 35].
5. **Stochastic Realization of Boundary Spectra and Second-Order Inertial Dynamics:** By Doob's theorem and stochastic realization theory, a multi-frequency stationary process on the interface $\partial A$ is isomorphic to a nested integrator chain of generalized coordinates of motion $\tilde{s}_t = (s_t^{(0)}, s_t^{(1)}, \dots, s_t^{(n)})$[cite: 22]. The coarse-graining operator $\mathcal{R}_{\ell \to \ell+1}$ acts as a spectral truncation filter cutting off orders $k > n(\ell)$[cite: 23, 35]; truncation at $n(\ell)=2$ (position, velocity, acceleration) yields effective second-order equations of motion (inertia and restoring force)[cite: 22, 23].
6. **Multiscale Synchronization and Network Architecture Transition:** Relative operational time between subsystems is defined by the ratio of accumulated gauge-invariant holonomy cycles along worldtubes[cite: 2, 35]. Maintaining algebraic connectivity $\lambda_2$ under bounded vertex valency $k_{\max}$ forces a structural transition from compact rotational modes at small scales to sparse node-filament-void networks at large scales[cite: 2, 35].
7. **Local-Global Balance and Horizon Saturation:** An exact combinatorial identity governs the partitioning of coherent diamonds across internal bulks, interfaces, and the external channel[cite: 35]. Falsifiable hypotheses are formulated for interfacial halo tension, phase-mediated void rarefaction, and horizon saturation ($\eta_{\mathrm{sat}} \ge 1$) leading to a high-rank matrix phase ($K_{xy}^{\mathrm{eff}} \ge 3$)[cite: 35].

All statements in this document are classified under the four-valued verification calculus $V_4 = \{\mathrm{FOLLOW}, \mathrm{OMIT}, \mathrm{UNDECIDED}, \mathrm{NULL}\}$[cite: 6, 35]. Section 7 specifies seven computational verification protocols (V1–V7), and Section 9 provides a self-contained reference implementation in Python[cite: 35].

---

## 0. Methodological Standard and the $V_4$ Verdict Calculus

To prevent conflation between mathematical theorems, operational definitions, and unverified physical interpretations, every claim in this specification is evaluated within the four-valued verification space[cite: 6, 35]:

$$
V_4 = \bigl\{\mathrm{FOLLOW}\ (+1),\; \mathrm{OMIT}\ (0),\; \mathrm{UNDECIDED}\ (U),\; \mathrm{NULL}\ (-1)\bigr\},
$$

governed by the strict linear severity dominance semilattice under conjunctive aggregation ($\otimes = \max_{\succ_V}$)[cite: 6, 35]:

$$
\mathrm{NULL}\ (-1) \;\succ_V\; \mathrm{UNDECIDED}\ (U) \;\succ_V\; \mathrm{OMIT}\ (0) \;\succ_V\; \mathrm{FOLLOW}\ (+1).
$$

Status assignment rules in this document[cite: 35]:
- **`FOLLOW` ($+1$):** Assigned exclusively to (a) internally consistent formal definitions and (b) mathematical propositions that follow deductively from assumptions explicitly stated within the proposition[cite: 4, 35]. A `FOLLOW` status on a conditional statement $P \implies Q$ certifies the validity of the implication, not the physical realization of premise $P$ in nature[cite: 35].
- **`OMIT` ($0$):** Assigned to (a) degrees of freedom lying in the kernel of the coarse-graining map $\ker(d\pi_\ell)$ (inessential at the chosen scale)[cite: 3, 6, 35], and (b) illustrative heuristics or metaphors included for geometric orientation that never enter as premises in any proof[cite: 3, 4, 35].
- **`UNDECIDED` ($U$):** Assigned to substantive structural and physical hypotheses that are mathematically well-posed but require numerical certification in protocols V1–V7 or external experimental calibration[cite: 35]. No `UNDECIDED` statement may be used as an established fact in subsequent derivations[cite: 6, 35].
- **`NULL` ($-1$):** Assigned to claims and model variants that are logically inconsistent, violate combinatorial or gauge invariants, or fail negative-control tests[cite: 4, 35].

---

## 1. Foundational Causal-Phase Complex

### 1.1. Partial Order of Events and the Hasse Matrix

Let $X = \{1, 2, \dots, N\}$ be a finite set of elementary events equipped with a strict partial order $\prec$[cite: 2, 35]:
1. **Irreflexivity:** $\forall x \in X, \; x \not\prec x$[cite: 2, 35].
2. **Transitivity:** $(x \prec z) \land (z \prec y) \implies x \prec y$[cite: 2, 35].
3. **Acyclicity:** $x \prec y \implies y \not\prec x$[cite: 2, 35].

Indices on $X$ are chosen topologically consistent with $\prec$: $x \prec y \implies x < y$[cite: 2, 35]. All structural observables must remain invariant under admissible relabelings (linear extensions of the partial order)[cite: 1, 35].

**Definition 1.1 (Causal Interval, Hasse Link, and Antichain).** `[Status: FOLLOW]`[cite: 35]
- The *causal interval* between $x \prec y$ is the set[cite: 1, 2, 35]
  $$
  I(x, y) := \{z \in X \mid x \prec z \prec y\}.
  $$
- A *Hasse link* (immediate causal coverage) $x \lessdot y$ holds if and only if $x \prec y$ and no intermediate event exists between them[cite: 1, 2, 35]:
  $$
  x \lessdot y \quad \Longleftrightarrow \quad x \prec y \;\land\; I(x, y) = \varnothing.
  $$
- An *antichain* (spacelike section) is a subset $S \subset X$ in which no two distinct elements are causally comparable: $\forall u \neq v \in S, \; u \not\prec v \land v \not\prec u$[cite: 2, 35].

The Boolean adjacency matrix of Hasse links $R \in \{0, 1\}^{N \times N}$ ($R_{xy} = 1 \iff x \lessdot y$) is strictly upper-triangular ($R_{xy} = 0$ for $x \ge y$) and nilpotent ($R^N = 0$)[cite: 1, 2, 35]. An arbitrary strictly upper-triangular Boolean matrix $R$ is the Hasse matrix of a partial order if and only if it is **transitively irreducible** (contains no edges short-circuiting directed paths of length $\ge 2$)[cite: 2, 35]:

$$
\forall x, y \in X: \quad R_{xy} = 1 \implies \bigl((I - R)^{-1} - I - R\bigr)_{xy} = 0.
$$

### 1.2. Phase Bundle and Transport Operator

Each directed Hasse link $x \lessdot y$ carries a phase variable $\theta_{xy} \in [0, 2\pi)$ and a unitary transport factor $U_{xy} = e^{i\theta_{xy}} \in U(1)$[cite: 1, 2, 35] (traversing a link backwards along a closed comparison loop uses $U_{yx} = U_{xy}^{-1} = e^{-i\theta_{xy}}$, which does not introduce a reverse causal edge into $R$[cite: 1, 35]).

**Definition 1.2 (Causal-Phase Transport Matrix).** `[Status: FOLLOW]`[cite: 35]  
The complex transport matrix $W \in \mathbb{C}^{N \times N}$ is defined by the Hadamard product[cite: 2, 35]:

$$
W_{xy} := R_{xy} e^{i\theta_{xy}}, \qquad W^N = 0.
$$

The matrix power $(W^k)_{xy}$ sums the complex amplitudes over all directed Hasse paths of length $k$ from $x$ to $y$[cite: 2, 35]. For a coupling parameter $\zeta \in (0, 1)$, the finite series $\mathcal{G}(\zeta) := (I - \zeta W)^{-1} = \sum_{k=0}^{N-1} \zeta^k W^k$ defines the full causal resolvent (Green's function)[cite: 2]. Local gauge transformations at vertices are generated by diagonal unitary matrices $D_\chi = \operatorname{diag}(e^{i\chi_1}, \dots, e^{i\chi_N})$, $\chi_x \in [0, 2\pi)$[cite: 1, 2, 35]:

$$
W \longmapsto W' = D_\chi W D_\chi^\dagger, \qquad \theta_{xy} \longmapsto \theta'_{xy} = (\theta_{xy} + \chi_x - \chi_y) \bmod 2\pi.
$$

### 1.3. Two-Step Waists, Elementary Diamonds, and the Interference Identity

For any pair of events $(x, y)$, consider the set of intermediate vertices of two-step paths (the interval waist)[cite: 1, 2, 35]:

$$
V_{xy} := \{z \in X \mid R_{xz} R_{zy} = 1\}.
$$

Four fundamental observables characterize two-step transport[cite: 2, 35]:
1. **Waist width:** $K_{xy} := |V_{xy}| = (R^2)_{xy} \in \mathbb{Z}_{\ge 0}$[cite: 1, 2, 35].
2. **Two-step amplitude:** $M_{xy} := (W^2)_{xy} = \sum_{z \in V_{xy}} e^{i(\theta_{xz} + \theta_{zy})} \in \mathbb{C}$[cite: 1, 2, 35].
3. **Waist coherence** (for $K_{xy} > 0$)[cite: 1, 2, 35]:
   $$
   \operatorname{Coh}_{xy} := \frac{|M_{xy}|^2}{K_{xy}^2} \in [0, 1].
   $$
4. **Phase frustration (activity)**[cite: 1, 2, 35]:
   $$
   J_{xy} := K_{xy}\bigl(1 - \operatorname{Coh}_{xy}\bigr) = \frac{K_{xy}^2 - |M_{xy}|^2}{K_{xy}} \ge 0.
   $$

Whenever $K_{xy} \ge 2$, any unordered pair of distinct intermediate vertices $\{z_a, z_b\} \subset V_{xy}$ ($z_a \neq z_b$) forms an **elementary causal diamond** $D(x; z_a, z_b; y)$ with gauge-invariant holonomy[cite: 1, 2, 35]:

$$
U_D(x; z_a, z_b; y) := U_{x z_a} U_{z_a y} U_{z_b y}^{-1} U_{x z_b}^{-1} = e^{i\Phi_{ab}}, \qquad \Phi_{ab} = (\theta_{x z_a} + \theta_{z_a y}) - (\theta_{x z_b} + \theta_{z_b y}).
$$

**Proposition 1.1 (Wilson Interference Identity for a Waist).** `[Status: FOLLOW]`[cite: 35]  
*For every pair of events $(x, y)$ with $K_{xy} \ge 1$, the sum of pairwise Wilson actions over all $\binom{K_{xy}}{2}$ elementary diamonds inside the waist satisfies the exact algebraic identity[cite: 1, 2, 35]:*

$$
\sum_{1 \le a < b \le K_{xy}} \bigl(1 - \cos\Phi_{ab}\bigr) = \frac{1}{2}\bigl(K_{xy}^2 - |M_{xy}|^2\bigr) = \frac{1}{2} K_{xy} J_{xy}.
$$

*Proof.* Setting $\phi_a = \theta_{xz_a} + \theta_{z_a y}$, expanding the squared modulus of $M_{xy} = \sum_{a=1}^{K_{xy}} e^{i\phi_a}$ gives $|M_{xy}|^2 = K_{xy} + 2\sum_{a < b} \cos(\phi_a - \phi_b) = K_{xy} + 2\sum_{a < b} \cos\Phi_{ab}$[cite: 1, 2, 35]. Subtracting this from $K_{xy}^2 = K_{xy} + 2\sum_{a < b} 1$ yields the stated identity[cite: 2, 35]. $\blacksquare$

### 1.4. Cone-Overlap Operators and Irregularity Measure

Define the Hermitian positive-semidefinite one-step future and past cone-overlap operators[cite: 1, 2, 35]:

$$
\Delta_+ := W W^\dagger, \qquad \Delta_- := W^\dagger W, \qquad C := [\Delta_+, \Delta_-] = \Delta_+ \Delta_- - \Delta_- \Delta_+.
$$

The diagonal entries $(\Delta_+)_{xx} = \mathrm{deg}^+(x)$ and $(\Delta_-)_{yy} = \mathrm{deg}^-(y)$ give outgoing and incoming vertex degrees, while off-diagonal entries measure phase-weighted shared futures and pasts[cite: 2, 35]. The commutator $C$ is skew-Hermitian ($C^\dagger = -C$)[cite: 1, 2, 35]. The scalar quantities

$$
L(W) := \|C\|_F^2 = \operatorname{Tr}(C^\dagger C) \ge 0, \qquad \bar{L}(W) := \frac{\|[\Delta_+, \Delta_-]\|_F^2}{1 + \|\Delta_+\|_F^2 \|\Delta_-\|_F^2}
$$

are gauge-invariant and vanish in the interior of translationally invariant regular lattices with flat connection ($\Phi_{ab} = 0$)[cite: 1, 2, 35].

---

## 2. The Structuring Triad: Internal Relief, Bilateral Interface, and External Channel

### 2.1. Separation of Null Channels and Massive Complexes

A foundational structural distinction within $(X, R, \Theta)$ separates unbranched transport chains from regions containing closed phase-comparison diamonds[cite: 2, 35]:

1. **Null (lightlike) transport links:** Hasse links $x \lessdot y$ along which, and in whose immediate neighborhood, no alternative two-step paths exist ($K_{xy} = 0$)[cite: 2, 35]. On a single unbranched link $x \lessdot y$, the local phase $\theta_{xy}$ can be gauged to zero via $\chi_y = \chi_x + \theta_{xy}$[cite: 35]. Consequently, an unbranched chain of such links transmits phase from emitter to receiver without accumulating internal gauge-invariant holonomy ($\Delta \Phi_D = 0$)[cite: 2, 35].
2. **Timelike (structured) complexes:** Connected subgraphs with high waist density $K_{xy} \ge 2$[cite: 2, 35]. Within these regions, phases cannot be gauged away whenever diamond holonomies satisfy $\Phi_{ab} \not\equiv 0 \pmod{2\pi}$, generating irreducible internal phase dynamics[cite: 35].

### 2.2. Formal Definition of the Triad $(\mathcal{I}_A, \partial A, \mathcal{E}_A)$

Let a connected subset of vertices $A \subset X$ be selected at resolution scale $\ell$ and observation window $\tau_w$[cite: 35].

**Definition 2.1 (Structural Triad of a Subsystem).** `[Status: FOLLOW]`[cite: 35]  
Every proper subsystem $A \subset X$ uniquely partitions the event set into three disjoint functional zones and two directed boundary streams[cite: 35]:

$$
X = \mathcal{I}_A \sqcup \partial A \sqcup \mathcal{E}_A,
$$

where[cite: 35]:
- **Bilateral Interface $\partial A := \partial^- A \cup \partial^+ A$:** the boundary vertices of $A$ sharing immediate Hasse links with the complement $X \setminus A$[cite: 35]:
  $$
  \partial^- A := \{y \in A \mid \exists x \in X \setminus A : R_{xy} = 1\}, \qquad \partial^+ A := \{x \in A \mid \exists y \in X \setminus A : R_{xy} = 1\}.
  $$
- **Internal Relief (Bulk) $\mathcal{I}_A := A \setminus \partial A$:** the interior core of subsystem $A$, which interacts with the rest of the complex exclusively through the mediation of the interface $\partial A$ (graph Markov blanket property)[cite: 10, 11, 35].
- **External Synchronization Channel $\mathcal{E}_A := X \setminus A$:** the exterior environment coupling subsystem $A$ to other subsystems $B, C, \dots \subset \mathcal{E}_A$[cite: 35].

The incoming and outgoing combinatorial capacities (discrete surface areas) of the interface are defined by the number of active Hasse links crossing the boundary[cite: 35]:

$$
|\partial^- A|_E := \sum_{x \in \mathcal{E}_A,\, y \in \partial^- A} R_{xy}, \qquad |\partial^+ A|_E := \sum_{x \in \partial^+ A,\, y \in \mathcal{E}_A} R_{xy}.
$$

**Definition 2.2 (Integration and Indivisibility Criterion on Window $\tau_w$).** `[Status: FOLLOW]`[cite: 35]  
Let $\mathrm{Dep}(U \leftrightarrow V) := \sum_{u \in U, v \in V} (|W_{uv}|^2 + |W_{vu}|^2)$ denote the symmetric coupling flux between disjoint vertex subsets[cite: 35]. Subsystem $A = \mathcal{I}_A \sqcup \partial A$ forms an **integrated (indivisible) object** on window $\tau_w$ at threshold $\theta_I > 0$ if for every non-trivial binary cut $(A_1, A_2)$ of $A$ ($A = A_1 \sqcup A_2$, $A_1, A_2 \neq \varnothing$), the ratio of internal coupling to external interface flux satisfies[cite: 4, 35]:

$$
I(A; \tau_w) := \min_{(A_1, A_2)} \frac{\mathrm{Dep}(A_1 \leftrightarrow A_2) / \min(|A_1|, |A_2|)}{\mathrm{Dep}(A \leftrightarrow \mathcal{E}_A) / |A|} > \theta_I.
$$

### 2.3. Recoverability Bound Across the Interface

Consider observing subsystem $A$ from the external channel $\mathcal{E}_A$[cite: 35]. Let the internal relief state $\mathcal{I}_A$ be represented by a random variable $Z_A$ that acts across the outgoing interface $\partial^+ A$ over $n$ steps, generating a boundary signal sequence $X^n \to Y^n$ received by an external observer $B \subset \mathcal{E}_A$ holding prior state $Z_B$[cite: 4, 35]. Let each transmission step across $\partial^+ A$ have channel capacity $C(\partial^+ A) \le c_0 |\partial^+ A|_E$ bits per step[cite: 35].

**Proposition 2.1 (Interface Information Recoverability Bound).** `[Status: FOLLOW]`[cite: 4, 35]  
*If transmission across $\partial^+ A$ is a memoryless channel with noise conditionally independent of $(Z_A, Z_B)$, and the reconstruction $\hat{Z}_A = f(Y^n, Z_B)$ is formed by observer $B$ from received signals $Y^n$ and prior state $Z_B$ (Markov structure $Z_A \to (X^n, Z_B) \to (Y^n, Z_B) \to \hat{Z}_A$), then the mutual information between the true internal structure $Z_A$ and its external reconstruction $\hat{Z}_A$ is bounded above by[cite: 4, 35]:*

$$
I(Z_A; \hat{Z}_A) \le I(Z_A; Z_B) + n \, C(\partial^+ A) \le I(Z_A; Z_B) + n c_0 |\partial^+ A|_E.
$$

*Proof.* By the data processing inequality, $I(Z_A; \hat{Z}_A) \le I(Z_A; Y^n, Z_B) = I(Z_A; Z_B) + I(Z_A; Y^n \mid Z_B)$[cite: 4, 35]. For a memoryless channel with conditionally independent noise, $I(Z_A; Y^n \mid Z_B) \le I(X^n; Y^n) \le \sum_{k=1}^n I(X_k; Y_k) \le n \, C(\partial^+ A)$[cite: 35]. $\blacksquare$

### 2.4. Precision Sparsity, Long-Range Covariance, and the Boundary Kernel-Inclusion Theorem

While Proposition 2.1 bounds the total information rate through $\partial A$, we can also characterize the exact linear-algebraic conditions under which the internal relief $\mathcal{I}_A$ synchronizes with and encodes expected states of the external channel $\mathcal{E}_A$ across the interface $\partial A$[cite: 11, 12].

Consider a stationary fluctuation regime around a stable configuration of the triad $x = (\eta, b, \mu) \in \mathcal{E}_A \times \partial A \times \mathcal{I}_A$, governed by a non-degenerate stationary Gaussian measure $p(x) = \mathcal{N}(0, \Pi^{-1})$ with symmetric positive-definite precision matrix $\Pi = \Sigma^{-1} \succ 0$ partitioned conformally with $(\mathcal{E}_A, \partial A, \mathcal{I}_A)$[cite: 10, 11]:

$$
\Pi = \begin{pmatrix} \Pi_{\mathcal{E}} & \Pi_{\mathcal{E},\partial A} & \Pi_{\mathcal{I}\mathcal{E}}^\top \\ \Pi_{\partial A,\mathcal{E}} & \Pi_{\partial A} & \Pi_{\partial A,\mathcal{I}} \\ \Pi_{\mathcal{I}\mathcal{E}} & \Pi_{\mathcal{I},\partial A} & \Pi_{\mathcal{I}} \end{pmatrix}, \qquad
\Sigma = \Pi^{-1} = \begin{pmatrix} \Sigma_{\mathcal{E}} & \Sigma_{\mathcal{E},\partial A} & \Sigma_{\mathcal{E}\mathcal{I}} \\ \Sigma_{\partial A,\mathcal{E}} & \Sigma_{\partial A} & \Sigma_{\partial A,\mathcal{I}} \\ \Sigma_{\mathcal{I}\mathcal{E}} & \Sigma_{\mathcal{I},\partial A} & \Sigma_{\mathcal{I}} \end{pmatrix}.
$$

Given any boundary state $b \in \partial A$, the conditional expectations of the external channel and internal relief are linear maps $\overline{\eta}(b) := \mathbb{E}[\eta \mid b] = \Sigma_{\mathcal{E},\partial A}\Sigma_{\partial A}^{-1} b = -\Pi_{\mathcal{E}}^{-1}\Pi_{\mathcal{E},\partial A} b$ and $\overline{\mu}(b) := \mathbb{E}[\mu \mid b] = \Sigma_{\mathcal{I},\partial A}\Sigma_{\partial A}^{-1} b = -\Pi_{\mathcal{I}}^{-1}\Pi_{\mathcal{I},\partial A} b$[cite: 11, 12, 26].

**Proposition 2.2 (Precision Sparsity, Long-Range Correlation, and Boundary Kernel Inclusion).** `[Status: FOLLOW]`[cite: 11, 12, 26]  
*Let $p(\eta, b, \mu) = \mathcal{N}(0, \Pi^{-1})$ with $\Pi \succ 0$. Then:*
1. **Precision Sparsity vs. Long-Range Covariance:** *Conditional independence between the internal relief and the external channel given the interface ($\eta \perp \mu \mid b$, the Markov blanket property) holds if and only if the direct off-diagonal precision block vanishes[cite: 11]:*
   $$
   \Pi_{\mathcal{I}\mathcal{E}} = 0 \quad \text{and} \quad \Pi_{\mathcal{E}\mathcal{I}} = 0.
   $$
   *Despite this strict locality of $\Pi$, the marginal covariance between the internal relief and the external channel is generally non-zero and is mediated across the interface by the exact identity:*
   $$
   \Sigma_{\mathcal{I}\mathcal{E}} = \Sigma_{\mathcal{I},\partial A}\,\Sigma_{\partial A}^{-1}\,\Sigma_{\partial A,\mathcal{E}} = \Pi_{\mathcal{I}}^{-1}\Pi_{\mathcal{I},\partial A}\,\Sigma_{\partial A}\,\Pi_{\partial A,\mathcal{E}}\Pi_{\mathcal{E}}^{-1}.
   $$
2. **Boundary Kernel-Inclusion Criterion for Synchronization:** *There exists a well-defined linear synchronization map $\sigma: \operatorname{Im}(\overline{\mu}) \to \operatorname{Im}(\overline{\eta})$ satisfying $\sigma(\overline{\mu}(b)) = \overline{\eta}(b)$ for all interface states $b \in \partial A$ if and only if the kernel of the internal-interface coupling is contained within the kernel of the external-interface coupling[cite: 12]:*
   $$
   \ker \Sigma_{\mathcal{I},\partial A} \subseteq \ker \Sigma_{\mathcal{E},\partial A} \quad \Longleftrightarrow \quad \ker \Pi_{\mathcal{I},\partial A} \subseteq \ker \Pi_{\mathcal{E},\partial A}.
   $$
   *When this condition holds, the canonical synchronization map is given explicitly in terms of the Moore–Penrose pseudoinverse by $\sigma(\mu) = \Pi_{\mathcal{E}}^{-1}\Pi_{\mathcal{E},\partial A}\Pi_{\mathcal{I},\partial A}^{-}\Pi_{\mathcal{I}}\mu$[cite: 13], and the expected internal state $\overline{\mu}(b)$ uniquely minimizes the quadratic prediction-error functional $D_{\mathrm{KL}}\bigl[\mathcal{N}(\eta; \sigma(\mu), \Pi_{\mathcal{E}}^{-1}) \;\|\; p(\eta \mid b)\bigr] = \frac{1}{2}\bigl(\sigma(\mu) - \overline{\eta}(b)\bigr)^\top \Pi_{\mathcal{E}} \bigl(\sigma(\mu) - \overline{\eta}(b)\bigr)$[cite: 17, 28].*

*Proof.* (1) Expanding the quadratic form $x^\top \Pi x$ shows that $p(\eta, \mu \mid b)$ factorizes as $p(\eta \mid b)p(\mu \mid b)$ if and only if the cross-term $\eta^\top \Pi_{\mathcal{E}\mathcal{I}}\mu$ vanishes identically, i.e., $\Pi_{\mathcal{I}\mathcal{E}} = 0$[cite: 11]. From the block inversion identity $\Pi \Sigma = I$ with $\Pi_{\mathcal{I}\mathcal{E}} = 0$, the $(\mathcal{I}, \partial A)$ block of $\Pi \Sigma = I$ gives $\Pi_{\mathcal{I},\partial A}\Sigma_{\partial A} + \Pi_{\mathcal{I}}\Sigma_{\mathcal{I},\partial A} = 0 \implies \Sigma_{\mathcal{I},\partial A} = -\Pi_{\mathcal{I}}^{-1}\Pi_{\mathcal{I},\partial A}\Sigma_{\partial A}$[cite: 26], and similarly $\Sigma_{\mathcal{E},\partial A} = -\Pi_{\mathcal{E}}^{-1}\Pi_{\mathcal{E},\partial A}\Sigma_{\partial A}$[cite: 26]. For a Gaussian Markov chain $\mu - b - \eta$, conditional independence $\mathbb{E}[(\mu - \overline{\mu}(b))(\eta - \overline{\eta}(b))^\top \mid b] = 0$ yields $\Sigma_{\mathcal{I}\mathcal{E}} = \Sigma_{\mathcal{I},\partial A}\Sigma_{\partial A}^{-1}\Sigma_{\partial A,\mathcal{E}}$. Substituting the expressions for $\Sigma_{\mathcal{I},\partial A}$ and $\Sigma_{\partial A,\mathcal{E}} = \Sigma_{\mathcal{E},\partial A}^\top$ gives the stated formula. (2) A map $\sigma$ with $\sigma(\overline{\mu}(b)) = \overline{\eta}(b)$ exists if and only if $\overline{\mu}(b_1) = \overline{\mu}(b_2) \implies \overline{\eta}(b_1) = \overline{\eta}(b_2)$, which by linearity is equivalent to $\ker(\Sigma_{\mathcal{I},\partial A}\Sigma_{\partial A}^{-1}) \subseteq \ker(\Sigma_{\mathcal{E},\partial A}\Sigma_{\partial A}^{-1})$[cite: 12, 25]. Since $\Sigma_{\partial A}^{-1}$, $\Pi_{\mathcal{I}}$, and $\Pi_{\mathcal{E}}$ are invertible principal/marginal blocks of positive-definite matrices, right-multiplying by $\Sigma_{\partial A}$ and using $\Pi_{\mathcal{I}}\Sigma_{\mathcal{I},\partial A} = -\Pi_{\mathcal{I},\partial A}\Sigma_{\partial A}$ yields $\ker \Sigma_{\mathcal{I},\partial A} \subseteq \ker \Sigma_{\mathcal{E},\partial A} \iff \ker \Pi_{\mathcal{I},\partial A} \subseteq \ker \Pi_{\mathcal{E},\partial A}$[cite: 25, 26]. The explicit formula for $\sigma$ and the KL-divergence minimization follow by direct substitution of the Gaussian conditionals[cite: 13, 28]. $\blacksquare$

**Structural Significance of Proposition 2.2:**  
First, item (1) demonstrates how **strictly local Hasse couplings** ($\Pi_{\mathcal{I}\mathcal{E}} = 0$: no direct links bypass the interface $\partial A$) automatically generate **non-zero long-range correlations** ($\Sigma_{\mathcal{I}\mathcal{E}} \neq 0$) between the internal relief and the distant external channel through the inverse operator $\Sigma = \Pi^{-1}$. Second, item (2) shows that the boundary synchronization condition $\ker \Pi_{\mathcal{I},\partial A} \subseteq \ker \Pi_{\mathcal{E},\partial A}$[cite: 12] is the exact linear-Gaussian specialization of the general differential kernel-inclusion condition $\ker d\pi_\ell \subseteq \ker d\pi_{\ell'}$ governing cross-scale quotient compatibility (§3.1)[cite: 7].

---

## 3. Variational Structuring Principle, Dynamic Dimensional Reduction, and Solenoidal Acceleration

### 3.1. Law of the Informational Minimal Surface and Orthogonal Splitting

Let a coarse-graining (descriptive) map $\pi_\ell: D_\ell \to Y_\ell$ be defined at resolution scale $\ell$ on a smooth manifold (or regular stratum) $D_\ell$ equipped with a positive-definite metric $h_z$ on $T_z D_\ell$[cite: 7, 35].

We formulate the variational principle of useful information structuring: a stable embedding $\Sigma \subset D_\ell$ minimizes its geometric volume subject to preserving a required level of mutual information (or coherent phase transport) $I(\Sigma; Y_\ell) \ge R_{\mathrm{req}}$[cite: 5, 35]:

$$
\mathcal{L}[\Sigma] = \mathrm{Vol}_{h}(\Sigma) + \lambda \bigl(R_{\mathrm{req}} - I(\Sigma; Y_\ell)\bigr).
$$

**Proposition 3.1 (Stationary Equation Balancing Mean Curvature and Information Gradient).** `[Status: FOLLOW]`[cite: 5, 35]  
*If $\Sigma$ is a smooth submanifold in an ambient Riemannian space $(Z, h)$, and the local information density is given by a smooth function $i(z) = D_{\mathrm{KL}}(P(Y|z) \| P(Y))$ under the fixed carrier density approximation ($\delta(d\mu_\Sigma) = 0$), then the stationarity condition $\delta \mathcal{L} / \delta \Sigma = 0$ with respect to normal variations of $\Sigma$ takes the form[cite: 5, 35]:*

$$
\mathbf{H}(z) = \lambda \bigl(\nabla_Z i(z)\bigr)^\perp,
$$

*where $\mathbf{H}(z)$ is the mean curvature vector of $\Sigma \subset Z$, and $(\nabla_Z i(z))^\perp$ is the projection of the information-density gradient onto the normal bundle $N_z \Sigma = (T_z \Sigma)^\perp$[cite: 5, 7, 35].*

*Proof.* The first variation of the Riemannian volume of a submanifold under a normal deformation $\delta z = \eta^\perp$ is $-\int_\Sigma \langle \mathbf{H}(z), \eta^\perp \rangle_h d\mathrm{Vol}_h$, while the variation of the information integral at fixed measure density is $\int_\Sigma \langle (\nabla_Z i(z))^\perp, \eta^\perp \rangle_h d\mathrm{Vol}_h$. Since $\eta^\perp$ is arbitrary, $\mathbf{H}(z) = \lambda(\nabla_Z i(z))^\perp$[cite: 35]. $\blacksquare$

To analyze state transitions within the support $D_\ell$, consider the differential $d\pi_\ell(z): T_z D_\ell \to T_{\pi_\ell(z)} Y_\ell$[cite: 7, 35]. Its kernel

$$
K_z := \ker\bigl(d\pi_\ell(z)\bigr) \subset T_z D_\ell
$$

forms the subspace of directions along which the macro-descriptor $\pi_\ell(z)$ is invariant to first order[cite: 7, 35]. Given a unit reference direction of expected active progress $u_{\mathrm{exp}}(z) \in K_z^{\perp_h}$, the tangent space $T_z D_\ell$ splits into an $h_z$-orthogonal direct sum of three subspaces[cite: 7, 35]:

$$
T_z D_\ell = W^{\mathrm{act}}_z \oplus_h W^{\mathrm{inv}}_z \oplus_h K_z, \qquad \mathrm{Id}_{T_z D_\ell} = P_{\mathrm{act}} + P_{\mathrm{inv}} + P_{\mathrm{ker}},
$$

where $W^{\mathrm{act}}_z = \operatorname{span}\{u_{\mathrm{exp}}(z)\}$ is the one-dimensional active transport subspace, $W^{\mathrm{inv}}_z = K_z^{\perp_h} \cap (W^{\mathrm{act}}_z)^{\perp_h}$ is the subspace of preserved transverse invariants at scale $\ell$, and $K_z$ is the kernel of inessential micro-variations (`OMIT`)[cite: 7, 35]. If a coarser map $\pi_{\ell'}$ factors smoothly through $\pi_\ell$ ($\pi_{\ell'} = f \circ \pi_\ell$), then $K_z^{(\ell)} \subseteq K_z^{(\ell')}$, guaranteeing well-defined cross-scale quotient projection[cite: 7].

### 3.2. Kernel-Path Factorization and Collapse of Multi-Vertex Bundles into Binary Diamonds ($K_{xy}^{\mathrm{eff}} = 2$)

We now translate kernel-path factorization directly onto the discrete causal-phase complex $(X, R, \Theta)$[cite: 35].

Consider a pair of events $x \prec y$ with waist $V_{xy} = \{z_1, \dots, z_m\}$ of arbitrary microscopic width $K_{xy} = m \ge 2$[cite: 35]. Each intermediate vertex $z_a \in V_{xy}$ defines a two-step path $p_a = (x \lessdot z_a \lessdot y)$ carrying total phase $\phi_a = (\theta_{xz_a} + \theta_{z_a y}) \bmod 2\pi$[cite: 2, 35].

**Definition 3.1 (Waist Factorization by the Phase Kernel).** `[Status: FOLLOW]`[cite: 35]  
Given a phase-distinction resolution $\varepsilon_{\mathrm{ker}} \ge 0$, two intermediate vertices $z_a, z_b \in V_{xy}$ are $\varepsilon_{\mathrm{ker}}$-coherent if they are causally incomparable and the relative holonomy between their paths does not exceed $\varepsilon_{\mathrm{ker}}$[cite: 35]:

$$
d_{\mathbb{T}}(\phi_a, \phi_b) := \min\bigl(|\phi_a - \phi_b|,\; 2\pi - |\phi_a - \phi_b|\bigr) \le \varepsilon_{\mathrm{ker}}.
$$

Path connectivity by chains of such pairs generates an equivalence relation $\sim_{K,\varepsilon_{\mathrm{ker}}}$ on $V_{xy}$ (at $\varepsilon_{\mathrm{ker}} = 0$, this reduces to exact phase equality $\phi_a = \phi_b$)[cite: 35]. The quotient waist $\widetilde{V}_{xy} := V_{xy} / \!\sim_{K,\varepsilon_{\mathrm{ker}}}$ comprises $K_{xy}^{\mathrm{eff}} := |\widetilde{V}_{xy}| \le K_{xy}$ macro-vertices (equivalence classes $C_1, \dots, C_{K^{\mathrm{eff}}}$) with effective phases $\widetilde{\phi}_\alpha = \arg\bigl(\sum_{z_a \in C_\alpha} e^{i\phi_a}\bigr)$[cite: 2, 35].

Consider on the quotient waist the local cost functional combining a strictly convex branching-volume penalty (the discrete counterpart of $\mathrm{Vol}_h(\Sigma)$) and phase frustration[cite: 2, 35]:

$$
\mathcal{F}_{\mathrm{loc}}(K^{\mathrm{eff}}, \{\widetilde{\phi}_\alpha\}) = a \bigl(K^{\mathrm{eff}}\bigr)^2 + b \, J^{\mathrm{eff}}_{xy}, \qquad a > 0, \; b \ge 0,
$$

where $J^{\mathrm{eff}}_{xy} = K^{\mathrm{eff}} - \frac{1}{K^{\mathrm{eff}}}\left|\sum_{\alpha=1}^{K^{\mathrm{eff}}} e^{i\widetilde{\phi}_\alpha}\right|^2$[cite: 35].

**Theorem 3.1 (Variational Selection of the Binary Causal Diamond $K_{xy}^{\mathrm{eff}} = 2$).** `[Status: FOLLOW]`[cite: 35]  
*Suppose $\mathcal{F}_{\mathrm{loc}}$ is minimized over waist configurations $(K_{xy}, \{\phi_a\})$ under exact coherent factorization ($\varepsilon_{\mathrm{ker}} = 0$) subject to maintaining a fixed non-zero gauge-invariant phase frustration $J^{\mathrm{eff}}_{xy} = J_0 \in (0, 2]$. Then[cite: 35]:*
1. *Every single-path configuration ($K^{\mathrm{eff}} = 1$) has identically zero gauge-invariant frustration $J^{\mathrm{eff}}_{xy} \equiv 0$ and cannot satisfy the boundary condition $J_0 > 0$[cite: 35].*
2. *For every $J_0 \in (0, 2]$, the global minimum of $\mathcal{F}_{\mathrm{loc}}$ is achieved on the **binary causal diamond** $K^{\mathrm{eff}}_{xy} = 2$ with relative holonomy $\Phi_{12} = \pm \arccos(1 - J_0)$, yielding minimum cost $\mathcal{F}_{\min} = 4a + b J_0$[cite: 35].*
3. *Any multi-vertex bundle with $K_{xy} = m > 2$, upon phase synchronization of $(m - 2)$ redundant paths with either of the two primary channels ($\phi_a \to \widetilde{\phi}_1$ or $\widetilde{\phi}_2$), collapses under kernel factorization to $K^{\mathrm{eff}}_{xy} = 2$, strictly lowering the cost by $\Delta \mathcal{F} = a(m^2 - 4) > 0$[cite: 35].*

*Proof.* (1) For $K^{\mathrm{eff}} = 1$, $|M^{\mathrm{eff}}_{xy}|^2 = |e^{i\widetilde{\phi}_1}|^2 = 1 = (K^{\mathrm{eff}})^2$, so $J^{\mathrm{eff}}_{xy} = 0 < J_0$[cite: 35]. (2) For integer $K^{\mathrm{eff}} \ge 2$ at fixed $J^{\mathrm{eff}}_{xy} = J_0$, $\mathcal{F}_{\mathrm{loc}} = a(K^{\mathrm{eff}})^2 + b J_0$[cite: 35]. Since $f(k) = a k^2$ ($a > 0$) is strictly increasing for $k \ge 2$, its unique integer minimum on $k \ge 2$ occurs at $k = 2$[cite: 35]. By Proposition 1.1, at $K^{\mathrm{eff}} = 2$ we have $J^{\mathrm{eff}}_{xy} = 1 - \cos(\widetilde{\phi}_1 - \widetilde{\phi}_2)$, which surjectively covers $(0, 2]$ for $\Phi_{12} \in (0, \pi]$[cite: 2, 35]. (3) At $\varepsilon_{\mathrm{ker}} = 0$, aligning the phases of $(m-2)$ vertices with $\widetilde{\phi}_1$ or $\widetilde{\phi}_2$ places them into equivalence classes $C_1, C_2$, reducing $K^{\mathrm{eff}}$ from $m$ to $2$ and decreasing the volume penalty from $a m^2$ to $4a$[cite: 35]. $\blacksquare$

### 3.3. Transverse Algebra of the Binary Diamond and Selection of $3+1$ Directions

Consider the internal structure of a binary causal diamond $K^{\mathrm{eff}}_{xy} = 2$ with intermediate vertices $\{z_1, z_2\}$ forming a minimal spacelike antichain $S_\perp = \{z_1, z_2\}$[cite: 2, 35]:

1. **Transverse State Space and $SU(2) \to SO(3)$:** `[Status: FOLLOW (algebraic structure)]`[cite: 35]  
   The space of complex amplitudes on the two-channel transverse section $S_\perp = \{z_1, z_2\}$ is isomorphic to $\mathbb{C}^2$[cite: 2, 35]. The group of norm-preserving unitary transitions across the two channels is $U(2) \cong U(1) \times SU(2) / \mathbb{Z}_2$[cite: 2, 35]. The abelian factor $U(1)$ represents overall phase shift, while $SU(2)$ has real dimension $\dim_{\mathbb{R}} \mathfrak{su}(2) = 3$ (generated by Pauli matrices $\sigma_1, \sigma_2, \sigma_3$, where $\sigma_3$ measures the relative phase $\Phi_{12}$ and $\sigma_1, \sigma_2$ govern coherent channel mixing)[cite: 35]. The adjoint representation of $SU(2)$ on traceless Hermitian $2\times 2$ matrices realizes the universal double cover of the 3D rotation group $SO(3)$[cite: 35].
2. **Minimal Dimension of Orthogonal Splitting with a Vortical Invariant:** `[Status: FOLLOW (under stated rank conditions)]`[cite: 35]  
   Decompose the transport operator $W$ into its Hermitian symmetric (potential) and skew-Hermitian (vortical/rotational) components[cite: 2, 35]:
   $$
   H_{\mathrm{sym}} := \frac{1}{2}(W + W^\dagger), \qquad H_{\mathrm{rot}} := \frac{1}{2i}(W - W^\dagger).
   $$
   In a real representation, non-zero eigenvalues of the skew-symmetric circulation generator $i H_{\mathrm{rot}} = \frac{1}{2}(W - W^\dagger)$ occur in conjugate pairs $\pm i\lambda_\alpha$, each spanning a two-dimensional invariant rotation plane[cite: 2, 35]. For the essential spatial subspace $T^{\mathrm{ess}}_z = W^{\mathrm{act}}_z \oplus_h W^{\mathrm{inv}}_z$ (§3.1) to simultaneously support a longitudinal propagation direction ($\dim W^{\mathrm{act}}_z \ge 1$) and an orthogonal plane of conserved transverse phase circulation (discrete angular momentum $\mathcal{L}_z \neq 0$, requiring $\dim W^{\mathrm{inv}}_z \ge 2$), the minimal spatial dimension must satisfy[cite: 35]:
   $$
   d_{\mathrm{space}}^{\min} = \dim W^{\mathrm{act}}_z + \dim W^{\mathrm{inv}}_z = 1 + 2 = 3.
   $$
   At $d_{\mathrm{space}} = 3$, the number of binary coordinate holonomy planes $\nu(d) = \binom{d}{2}$ satisfies the unique non-trivial integer duality $\binom{3}{2} = 3 = d_{\mathrm{space}}$[cite: 2, 35]. Combined with the directed causal order of phase accumulation, this singles out $3+1$ as the minimal closed architecture[cite: 35]. Whether $3+1$ emerges spontaneously as the global attractor of random causal ensembles is an empirical computational hypothesis (`Status: UNDECIDED`, Protocol V1)[cite: 35].

### 3.4. Helmholtz Decomposition and Solenoidal Acceleration of Structural Relaxation

Why do persistent structures in the causal-phase complex require a non-zero rotational component $H_{\mathrm{rot}} \neq 0$ rather than relaxing solely through purely symmetric gradient flow $H_{\mathrm{sym}}$? Non-equilibrium stochastic mechanics provides an exact analytical answer via the **Helmholtz decomposition**[cite: 15, 26].

In the continuous-time diffusion limit around a stationary density $p(x) \propto \exp(-\mathcal{F}(x)/T)$ with precision matrix $\Pi \succ 0$ of the linearized potential $\mathcal{F}(x) = \frac{1}{2} x^\top \Pi x$, any stationary Itô stochastic differential equation $dx_t = f(x_t)\,dt + \varsigma(x_t)\,dW_t$ maintaining $p(x)$ as its invariant measure uniquely decomposes its drift field $f(x)$ into two components[cite: 15, 26]:

$$
f(x) = f_{\mathrm{rev}}(x) + f_{\mathrm{irrev}}(x), \qquad f_{\mathrm{rev}}(x) = \Gamma(x)\nabla \ln p(x) + \nabla \cdot \Gamma(x), \qquad f_{\mathrm{irrev}}(x) = Q(x)\nabla \ln p(x) + \nabla \cdot Q(x),
$$

where $\Gamma(x) = \frac{1}{2}\varsigma(x)\varsigma(x)^\top \succeq 0$ is the symmetric dissipative diffusion tensor (driving gradient descent down $\mathcal{F}(x)$) and $Q(x) = -Q(x)^\top$ is a skew-symmetric matrix field generating divergence-free, conservative (solenoidal) circulation along the level sets of $\mathcal{F}(x)$ ($\nabla \cdot (f_{\mathrm{irrev}} p) = 0$)[cite: 15, 26, 27, 28].

On the discrete causal-phase complex, the operator splitting

$$
W = H_{\mathrm{sym}} + i H_{\mathrm{rot}}, \qquad H_{\mathrm{sym}}^\dagger = H_{\mathrm{sym}}, \quad (i H_{\mathrm{rot}})^\dagger = -(i H_{\mathrm{rot}})
$$

is the direct algebraic counterpart of the Helmholtz decomposition $(\Gamma + Q)$[cite: 2, 15, 35]: $H_{\mathrm{sym}}$ generates dissipative relaxation across potential gradients, while the skew-Hermitian component $i H_{\mathrm{rot}}$ generates solenoidal phase circulation along constant-cost contours[cite: 2, 27, 35].

**Proposition 3.2 (Solenoidal Preservation of Stationary Measure and Acceleration of Relaxation).** `[Status: FOLLOW]`[cite: 19, 20, 28, 32]  
*Consider a linear Langevin relaxation process $dx_t = -(\Gamma + Q)\Pi x_t\,dt + \sqrt{2\Gamma}\,dW_t$ on $\mathbb{R}^n$ with symmetric positive-definite precision $\Pi \succ 0$, constant symmetric positive-definite dissipative tensor $\Gamma \succ 0$, and skew-symmetric solenoidal matrix $Q = -Q^\top$. Let $B(Q) := (\Gamma + Q)\Pi$ be the drift matrix and $\gamma(Q) := \min\{\operatorname{Re}\mu : \mu \in \operatorname{spec}(B(Q))\}$ be the spectral relaxation rate toward the stationary Gaussian state $p(x) = \mathcal{N}(0, \Pi^{-1})$. Then:*
1. **Invariance of the Stationary Relief:** *For every skew-symmetric matrix $Q = -Q^\top$, the solenoidal drift $f_{\mathrm{irrev}}(x) = -Q\Pi x$ is divergence-free with respect to $p(x)$ ($\nabla \cdot (f_{\mathrm{irrev}} p) = 0$) and leaves the stationary distribution $p(x) = \mathcal{N}(0, \Pi^{-1})$ strictly unchanged[cite: 26, 28].*
2. **Non-Decrease and Strict Acceleration of the Spectral Gap:** *For every skew-symmetric $Q = -Q^\top$, the spectral relaxation rate satisfies the inequality[cite: 20, 32]:*
   $$
   \gamma(Q) \;\ge\; \gamma(0) = \lambda_{\min}\bigl(\Pi^{1/2}\Gamma\Pi^{1/2}\bigr) > 0, \qquad \operatorname{Tr} B(Q) = \operatorname{Tr}(\Gamma \Pi) = \mathrm{const}.
   $$
   *Moreover, whenever $\Pi^{1/2}\Gamma\Pi^{1/2}$ is not a scalar multiple of the identity (anisotropic relief stiffness), there exist skew-symmetric matrices $Q \neq 0$ that couple the slow and fast eigendirections of $\Pi^{1/2}\Gamma\Pi^{1/2}$ such that $\gamma(Q) > \gamma(0)$ strictly, achieving the theoretical maximum $\gamma_{\max} = \frac{1}{n}\operatorname{Tr}(\Gamma\Pi)$ when all eigenvalues of $B(Q)$ coalesce in real part[cite: 32].*

*Proof.* (1) Since $\nabla p(x) = -p(x)\Pi x$ and $\nabla \cdot (Q\Pi x) = \operatorname{Tr}(Q\Pi) = 0$ (as the trace of the product of a skew-symmetric and a symmetric matrix), we have $\nabla \cdot (f_{\mathrm{irrev}} p) = -p\operatorname{Tr}(Q\Pi) + (\Pi x)^\top Q^\top p \Pi x = 0$ because $v^\top Q^\top v = 0$ for all $v$[cite: 28]. Thus the stationary Fokker–Planck equation $\nabla \cdot (-f p + \Gamma \nabla p) = 0$ holds identically for all $Q = -Q^\top$[cite: 28]. (2) Perform the similarity transformation $\widetilde{B}(Q) := \Pi^{1/2} B(Q) \Pi^{-1/2} = S + A$, where $S := \Pi^{1/2}\Gamma\Pi^{1/2} \succ 0$ is symmetric positive-definite and $A := \Pi^{1/2} Q \Pi^{1/2} = -A^\top$ is skew-symmetric. Let $\mu \in \operatorname{spec}(\widetilde{B}(Q))$ with unit eigenvector $v \in \mathbb{C}^n$ ($\|v\|_2 = 1$, $(S + A)v = \mu v$). Taking the Hermitian inner product with $v$ gives $\mu = v^\dagger S v + v^\dagger A v$. Since $S^\dagger = S$ and $A^\dagger = -A$, $v^\dagger S v$ is real and $v^\dagger A v$ is purely imaginary, so $\operatorname{Re}\mu = v^\dagger S v \ge \lambda_{\min}(S) = \gamma(0)$. Taking the minimum over all eigenvalues gives $\gamma(Q) \ge \gamma(0)$. Furthermore, $\operatorname{Tr}\widetilde{B}(Q) = \operatorname{Tr} S = \sum_{i=1}^n \operatorname{Re}\mu_i$, so the average real part of the eigenvalues is fixed at $\bar{\gamma} = \frac{1}{n}\operatorname{Tr}(\Gamma\Pi)$. If $S$ has distinct eigenvalues $\lambda_{\min}(S) < \lambda_{\max}(S)$, choosing $A = -A^\top$ to mix the eigenvectors of $S$ lifts the smallest real part toward the mean $\bar{\gamma}$, yielding $\gamma(Q) > \gamma(0)$ with complex-conjugate eigenvalues (damped spiral trajectories)[cite: 20, 32]. $\blacksquare$

**Physical Consequence:**  
Proposition 3.2 provides a rigorous dynamical reason for the ubiquity of spin and vortical phase modes ($H_{\mathrm{rot}} \neq 0$, $\mathcal{L}_z \neq 0$) in stable structures: on an anisotropic relief, purely gradient relaxation ($Q=0$) is bottlenecked by the slowest eigendirection $\lambda_{\min}(S)$, whereas adding solenoidal circulation $H_{\mathrm{rot}} \neq 0$ couples slow and fast modes, exponentially accelerating relaxation back to the attractor after perturbations at the signature cost of damped oscillatory (spiral) trajectories[cite: 19, 20, 32].

---

## 4. Oseledets Spectrum and the Landauer Thermodynamic Bridge at the Interface

### 4.1. Separating the Structural Functional from the Thermodynamic Flux

For any localized structure $A = (\mathcal{I}_A, \partial A, \mathcal{E}_A)$, its internal combinatorial-phase organization must be strictly separated from the thermodynamic cost of maintaining it within the external channel[cite: 35]. We distinguish three components[cite: 35]:
1. **Bulk Structural Functional $\mathscr{S}_{\mathrm{struct}}(\mathcal{I}_A)$:** determined by the restriction $W_{\mathcal{I}}$ inside $\mathcal{I}_A$[cite: 35]:
   $$
   \mathscr{S}_{\mathrm{struct}}(\mathcal{I}_A) = a \sum_{x,y \in \mathcal{I}_A,\, K_{xy}>0} K_{xy}^2 + b \sum_{x,y \in \mathcal{I}_A,\, K_{xy}>0} J_{xy} + g \, \|[\Delta_+^{\mathcal{I}}, \Delta_-^{\mathcal{I}}]\|_F^2.
   $$
2. **Interfacial Structural Tension $\mathscr{S}_{\mathrm{interface}}(\partial A)$:** the contribution of waists and cone commutators on the boundary layer $\partial A$ stitching $\mathcal{I}_A$ to $\mathcal{E}_A$[cite: 35].
3. **Thermodynamic Erasure Flux $\dot{Q}_{\mathrm{Landauer}}(\mathcal{I}_A \to \partial^+ A)$:** the flux of irreversibly discarded microscopic distinctions expelled from $\mathcal{I}_A$ through the outgoing interface $\partial^+ A$ into the external channel[cite: 35].

### 4.2. Internal Oseledets–Lyapunov Spectrum and the Erasure Flux Theorem

By Landauer's principle, erasing one bit of information at temperature $T$ dissipates at least $k_B T \ln 2$ of energy[cite: 3, 35]. While this minimum price per bit is a universal constant independent of internal dimensionality, **the number of bits a subsystem must erase per step of its internal dynamics to remain localized on its attractor** is governed directly by the tangent-space geometry of its internal relief[cite: 35].

Let the internal state of $\mathcal{I}_A$ across consecutive causal layers $n = 0, 1, 2, \dots$ be described by a continuous state vector $z(n) \in \mathbb{R}^{N_A}$ evolving under a differentiable map $z(n+1) = G_R(z(n))$ with Jacobian $M(n) = \left.\frac{\partial G_R(z)}{\partial z}\right|_{z(n)}$[cite: 4, 35].

By Oseledets' multiplicative ergodic theorem, on an ergodic invariant measure of the attractor there exist Lyapunov exponents $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_{N_A}$, and the tangent space splits into a direct (generally oblique) sum[cite: 4, 7, 35]:

$$
T_{z(n)} \mathcal{I}_A = E^u(z(n)) \oplus E^s(z(n)),
$$

where[cite: 4, 35]:
- $E^u(z)$ is the unstable/neutral subspace ($\lambda_i \ge 0$) tangent to the attractor; the sum of positive exponents defines the internal information generation rate (Kolmogorov–Sinai entropy rate via Pesin's formula)[cite: 4, 35]:
  $$
  h_{\mathrm{KS}}(A) = \sum_{i:\, \lambda_i > 0} \lambda_i \ge 0,
  $$
  and the intrinsic attractor dimension is given by the Kaplan–Yorke formula[cite: 4, 35]:
  $$
  D_{\mathrm{KY}}(A) = j + \frac{\sum_{i=1}^j \lambda_i}{|\lambda_{j+1}|}, \qquad \sum_{i=1}^j \lambda_i \ge 0 > \sum_{i=1}^{j+1} \lambda_i.
  $$
- $E^s(z)$ is the stable (contracting) subspace ($\lambda_i < 0$) transverse to the attractor, responsible for relaxing perturbations back onto the attractor with total logarithmic volume contraction rate[cite: 4, 35]:
  $$
  \kappa(A) := \sum_{i:\, \lambda_i < 0} |\lambda_i| = -\sum_{i:\, \lambda_i < 0} \lambda_i \ge 0.
  $$

At finite $N_A$, the cumulative Lyapunov distribution $F_A(s) = \frac{1}{N_A}|\{i : \lambda_i < s\}|$ equals the normalized trace of the minimum-norm one-step tangent response matrix $R^{vv}_\eta(n+1, n)$ for the shifted Jacobian $M_s(n) = e^{-s} M(n)$ (the dichotomy projector onto $E^s_s$)[cite: 4, 35]:

$$
F_A(s) = \lim_{\eta \to 0^+} \frac{1}{N_A}\operatorname{Tr} R^{vv}_\eta(n+1, n), \qquad \kappa(A) = -N_A \int_{-\infty}^{0} s \, F'_A(s) \, ds.
$$

**Theorem 4.1 (Boundary Erasure Flux Bound for a Stationary Attractor Under Noise).** `[Status: FOLLOW (under stated stationarity assumptions)]`[cite: 35]  
*Suppose subsystem $\mathcal{I}_A$ evolves according to $z(n+1) = G_R(z(n)) + \xi_{\mathrm{in}}(n)$, where a stationary flux of small perturbations $\xi_{\mathrm{in}}(n)$ enters through the incoming interface $\partial^- A$, maintaining a finite stationary differential entropy $H(Z_n) = \mathrm{const} \in (-\infty, +\infty)$ in a neighborhood of the attractor[cite: 35]. Suppose to first order in perturbation amplitude the local tangent volume scales per step by the Jacobian $|\det M(n)| = \exp\bigl(\sum_{i=1}^{N_A} \lambda_i\bigr)$ with $\kappa(A) > h_{\mathrm{KS}}(A)$ (dissipative attractor confinement)[cite: 35]. Then:*
1. *To maintain stationary differential entropy $H(Z_{n+1}) = H(Z_n)$, the irreversible phase-volume contraction along the stable subspace $E^s$, net of internal expansion along $E^u$, must be compensated by an outward information erasure flux (discarding perturbation microstates) across the outgoing interface $\partial^+ A$ into the external channel $\mathcal{E}_A$ at a rate (in bits per update step)[cite: 35]:*
   $$
   \dot{I}_{\mathrm{erase}}(\mathcal{I}_A \to \partial^+ A) \;\ge\; \frac{\kappa(A) - h_{\mathrm{KS}}(A)}{\ln 2} = \frac{1}{\ln 2} \sum_{i=1}^{N_A} (-\lambda_i).
   $$
2. *If the outgoing interface $\partial^+ A$ couples to the external channel at effective temperature $T_{\partial A} > 0$ and Landauer's bound applies to each erased bit, the minimum dissipation power (action/heat flux per internal step) across $\partial^+ A$ satisfies[cite: 35]:*
   $$
   \dot{Q}_{\mathrm{ext}}(\partial^+ A) \;\ge\; k_B T_{\partial A} \ln 2 \cdot \dot{I}_{\mathrm{erase}}(\mathcal{I}_A \to \partial^+ A) \;\ge\; k_B T_{\partial A} \bigl(\kappa(A) - h_{\mathrm{KS}}(A)\bigr).
   $$

*Proof.* Under a linear tangent-volume map with matrix $M(n)$, differential entropy (in nats) transforms as $H_{\mathrm{map}}(Z_{n+1}) = H(Z_n) + \mathbb{E}[\ln |\det M(n)|] = H(Z_n) + h_{\mathrm{KS}}(A) - \kappa(A)$[cite: 35]. Incoming boundary noise across $\partial^- A$ injects $\Delta H_{\mathrm{in}} \ge 0$[cite: 35]. For the distribution to remain stationary ($H(Z_{n+1}) = H(Z_n)$) without escaping the attractor, excess entropy $\Delta H_{\mathrm{erase}} = \Delta H_{\mathrm{in}} \ge \kappa(A) - h_{\mathrm{KS}}(A)$ nats per step must be expelled from the internal state description across $\partial^+ A$ into the external reservoir $\mathcal{E}_A$[cite: 35]. Dividing by $\ln 2$ converts nats to bits (item 1), and multiplying by the Landauer minimum $k_B T_{\partial A} \ln 2$ per bit yields item 2[cite: 35]. $\blacksquare$

---

## 5. Time as a Multiscale Synchronization Spectrum, Integrator Chains, and Network Architecture Transition

### 5.1. Operational Time and the Origin of the Lorentzian Metric Signature

The foundational complex $(X, \prec)$ possesses no external global time axis; only the partial order of causal admissibility exists[cite: 1, 3, 35].

Let subsystem $A$ at scale $\ell$ be a worldtube composed of consecutive spacelike antichains $S_0 \prec S_1 \prec \dots \prec S_m$ linked by internal causal diamonds ($K_{xy} \ge 2$)[cite: 2, 35].

**Definition 5.1 (Proper Frequency and Relative Operational Time).** `[Status: FOLLOW]`[cite: 35]
1. For a localized region $A$ with a non-empty set of elementary diamonds $\mathcal{D}_A(k)$ between layers $S_k$ and $S_{k+2}$, the complex phase-synchronization order parameter is[cite: 1, 35]
   $$
   z_A(k) := \frac{1}{|\mathcal{D}_A(k)|} \sum_{D \in \mathcal{D}_A(k)} e^{i\Phi_D}, \qquad \Phi_D \in (-\pi, \pi].
   $$
   Whenever $|z_A(k)| \ge \theta_{\mathrm{coh}} > 0$, the mean gauge-invariant phase increment per two-step layer defines the **internal proper frequency of subsystem $A$ at scale $\ell$**[cite: 1, 2, 35]:
   $$
   \omega_A^{(\ell)} := \frac{1}{m} \sum_{k=0}^{m-1} \arg z_A(k),
   $$
   and the accumulated count of internal phase cycles is $\Delta N_A^{(\ell)} = \frac{m}{2\pi} \omega_A^{(\ell)}$[cite: 2, 35].
2. For two subsystems $A$ and $B$ exchanging signals along unbranched null chains of the external channel $\mathcal{E}_{\mathrm{null}}$ ($K_{xy} = 0$, along which the internal diamond counter vanishes, $\Delta N_{\mathrm{null}} = 0$), **relative operational time** between successive exchange events is the dimensionless ratio of accumulated phase cycles[cite: 2, 3, 35]:
   $$
   R_{AB}^{(\ell)} := \frac{\Delta N_A^{(\ell)}}{\Delta N_B^{(\ell)}} = \frac{\omega_A^{(\ell)} \Delta m_A}{\omega_B^{(\ell)} \Delta m_B}.
   $$

**Combinatorial Origin of the Lorentzian Signature $(-,+,+,+)$:** `[Status: FOLLOW (within combinatorial step allocation)]`[cite: 35]  
Let the total budget of elementary Hasse steps between two events along a worldtube be $\Delta s_{\mathrm{causal}}$[cite: 35]. Each Hasse step is allocated either to transverse spatial displacement along an antichain ($\Delta l$) or to closing internal synchronization diamonds ($\Delta \tau \propto \Delta N_A$)[cite: 35]. In the quadratic allocation regime,

$$
(\Delta \tau)^2 + (\Delta l)^2 = (\Delta s_{\mathrm{causal}})^2 \quad \Longleftrightarrow \quad \Delta s_{\mathrm{Lorentz}}^2 := -(\Delta \tau)^2 + (\Delta l)^2 = 2(\Delta l)^2 - (\Delta s_{\mathrm{causal}})^2.
$$

For a pure external null channel ($\mathcal{E}_{\mathrm{null}}$, $K_{xy}=0$), all steps propagate longitudinally without internal diamond closure ($\Delta l = \Delta \tau$ in external coordinates, yielding $\Delta s_{\mathrm{Lorentz}}^2 = 0$), whereas for a stationary massive complex ($\Delta l = 0$) the entire step budget is spent on internal diamond resynchronization ($\Delta s_{\mathrm{Lorentz}}^2 = -(\Delta \tau)^2 < 0$)[cite: 35]. Thus the opposite sign of the $+1$ temporal component reflects budget competition between spatial propagation and internal phase synchronization[cite: 35].

### 5.2. Stochastic Realization of Boundary Spectra and the Emergence of Second-Order Inertia

How does a discrete spectrum of synchronization frequencies on the interface $\partial A$ translate into differential equations of motion (position, velocity, acceleration/inertia) in the continuum limit? Stochastic realization theory and Doob's theorem provide the exact bridge[cite: 21, 22].

Consider a boundary observable $s_t \in \mathbb{R}^d$ on the incoming interface $\partial^- A$ evolving as a mean-zero stationary Gaussian process with autocovariance $C(\tau) = \mathbb{E}[s_{t+\tau} s_t^\top]$ determined by a finite set of relaxation and oscillation modes $\{\gamma_k \pm i\omega_k\}_{k=0}^n$ ($\gamma_k > 0$)[cite: 22].

**Proposition 5.1 (Stochastic Realization of Multi-Frequency Boundary Processes as Integrator Chains and Scale Truncation).** `[Status: FOLLOW]`[cite: 22, 23]  
*Let $s_t$ be a mean-zero stationary Gaussian boundary process on $\partial^- A$ whose spectral density is rational (equivalently, whose autocovariance $C(\tau)$ is a finite linear combination of damped exponentials and sinusoids $e^{-\gamma_k |\tau|}\cos(\omega_k \tau + \phi_k)$). Then:*
1. **Integrator-Chain Realization:** *By Doob's theorem and linear stochastic realization theory, there exists a Markov process $\tilde{s}_t = \bigl(s_t^{(0)}, s_t^{(1)}, \dots, s_t^{(n)}\bigr)$ (the hierarchy of generalized coordinates of motion: position, velocity, acceleration, jerk, etc.) governed by a triangular chain of coupled Ornstein–Uhlenbeck stochastic differential equations[cite: 22, 23]:*
   $$
   \begin{aligned}
   s_t &= F_0 s_t^{(0)}, \\
   ds_t^{(k)} &= \bigl(-A_k s_t^{(k)} + B_k s_t^{(k+1)}\bigr)\,dt + \varsigma_k\,dW_t^{(k)} \quad (0 \le k \le n-1), \\
   ds_t^{(n)} &= -A_n s_t^{(n)}\,dt + \varsigma_n\,dW_t^{(n)},
   \end{aligned}
   $$
   *such that the marginal law of $F_0 s_t^{(0)}$ reproduces $s_t$ identically for all $t$[cite: 22].*
2. **Coarse-Graining as High-Order Truncation and Emergence of Second-Order Dynamics ($n=2$):** *If the decay rates are ordered by timescale separation $0 < \gamma_0 \le \gamma_1 \le \gamma_2 \ll \gamma_3 \le \dots \le \gamma_n$, then coarse-graining over a temporal window $\tau_w^{(\ell)} \in (\gamma_2^{-1}, \gamma_3^{-1})$ averages out all high-frequency orders $k \ge 3$ ($\gamma_k \tau_w^{(\ell)} \gg 1$), reducing the active boundary state to the three-level truncation $\tilde{s}_t^{(\le 2)} = \bigl(s_t^{(0)}, s_t^{(1)}, s_t^{(2)}\bigr)$ (integral/position, velocity, and acceleration)[cite: 22, 23]. Minimizing the quadratic interfacial free energy $F(\tilde{s}_t^{(\le 2)}, a_t, \mu_t) = \frac{1}{2}\bigl[\tilde{s}_t^{(\le 2)}, a_t, \mu_t\bigr] K_{\partial A} \bigl[\tilde{s}_t^{(\le 2)}, a_t, \mu_t\bigr]^\top$ with respect to autonomous states $(a_t, \mu_t)$ yields a second-order dynamical control law with effective inertia (proportional to the precision weight on $s_t^{(2)}$), damping (weight on $s_t^{(1)}$), and restoring force (weight on $s_t^{(0)}$)[cite: 20, 21, 22, 23].*

*Proof.* (1) A stationary Gaussian process has a rational spectral density $S(\omega) = \int_{-\infty}^\infty e^{-i\omega\tau}C(\tau)\,d\tau$ if and only if $S(\omega)$ admits a stable minimum-phase spectral factorization $S(\omega) = H(i\omega)H(-i\omega)^\top$ with rational transfer matrix $H(s) = F_0(sI - \mathcal{A})^{-1}\mathcal{B}$[cite: 22, 32]. Transforming $(\mathcal{A}, \mathcal{B}, F_0)$ to block-companion/Hessenberg integrator-chain form yields the nested Itô system for $\tilde{s}_t = (s_t^{(0)}, \dots, s_t^{(n)})$[cite: 22]. (2) For modes $k \ge 3$ with $\gamma_k \tau_w^{(\ell)} \gg 1$, the variance of the window-averaged coordinate $\frac{1}{\tau_w^{(\ell)}}\int_t^{t+\tau_w^{(\ell)}} s_u^{(k)}\,du$ decays as $O\bigl((\gamma_k \tau_w^{(\ell)})^{-1}\bigr)$, placing $s_t^{(k)}$ ($k \ge 3$) inside the coarse-graining kernel (`OMIT`) at scale $\ell$[cite: 7, 23]. Retaining $k \in \{0, 1, 2\}$ and taking the linear-quadratic stationary minimum of $\frac{1}{2}[\tilde{s}^{(\le 2)}, a, \mu] K_{\partial A} [\tilde{s}^{(\le 2)}, a, \mu]^\top$ produces linear feedback gains over $(s_t^{(0)}, s_t^{(1)}, s_t^{(2)})$, which is the canonical second-order (PID/inertial) equation of motion[cite: 21, 22, 23]. $\blacksquare$

### 5.3. Multiscale Coarse-Graining Operator $\mathcal{R}_{\ell \to \ell+1}$ and Synchronization Criterion

Different levels of organization (quantum, atomic, molecular, planetary, stellar, galactic, cosmological) correspond to successive coarse-graining scales $\ell = 0, 1, \dots, M$[cite: 35].

**Definition 5.2 (Multiscale Coarse-Graining Operator $\mathcal{R}_{\ell \to \ell+1}$).** `[Status: FOLLOW]`[cite: 2, 35]  
Given $(X_\ell, R_\ell, \Theta_\ell)$ with transport matrix $W_\ell$:
1. On spacelike vertex pairs ($u \not\prec_\ell v$ and $v \not\prec_\ell u$), compute the two-step cone-overlap coherence matrix[cite: 2, 35]:
   $$
   S^{(\ell)}_{uv} := \bigl|(\Delta_+^{(\ell)})_{uv}\bigr| + \bigl|(\Delta_-^{(\ell)})_{uv}\bigr|.
   $$
2. At threshold $\theta_\ell > 0$, partition $X_\ell$ into connected spacelike clusters (macro-nodes) $X_{\ell+1} = \{C_1, \dots, C_{N_{\ell+1}}\}$ subject to causal order convexity (acyclicity of the quotient graph)[cite: 1, 2, 35].
3. Set $\alpha \prec_{\ell+1} \beta$ whenever at least one Hasse link $x \lessdot_\ell y$ connects $x \in C_\alpha$ to $y \in C_\beta$, and apply Hasse transitive reduction to obtain $R_{\ell+1}$[cite: 2, 35].
4. Compute effective macro-amplitudes and phases by coherent summation[cite: 1, 2, 35]:
   $$
   \widetilde{W}^{(\ell+1)}_{\alpha\beta} = \sum_{x \in C_\alpha,\, y \in C_\beta} W^{(\ell)}_{xy}, \qquad r^{(\ell+1)}_{\alpha\beta} = \bigl|\widetilde{W}^{(\ell+1)}_{\alpha\beta}\bigr|, \qquad \Theta^{(\ell+1)}_{\alpha\beta} = \arg\bigl(\widetilde{W}^{(\ell+1)}_{\alpha\beta}\bigr) \quad (r^{(\ell+1)}_{\alpha\beta} > \epsilon).
   $$
5. Store the internal frequency $\omega_\alpha^{(\ell)}$, transverse contraction rate $\kappa_\alpha^{(\ell)}$, and topological circulation index $\mathcal{L}_\alpha^{(\ell)}$ of cluster $C_\alpha$ as internal attributes of macro-node $\alpha$ at scale $\ell+1$[cite: 2, 35].

**Definition 5.3 (Synchronization Stability Criterion at Scale $\ell$).** `[Status: FOLLOW]`[cite: 35]  
Let $L_{\mathrm{norm}}^{(\ell)}(A)$ be the normalized symmetric skeleton Laplacian of subsystem $A_\ell \subset X_\ell$ with algebraic connectivity (Fiedler eigenvalue) $\lambda_2(A_\ell) > 0$, graph diameter $\tau_{\mathrm{diam}}(A_\ell)$, and internal frequency dispersion $\sigma_\omega(A_\ell) = \sqrt{\operatorname{Var}_{x \in A_\ell}(\omega_x^{(\ell)})}$[cite: 2, 35]. Subsystem $A_\ell$ is **phase-synchronizable on window $\tau_w^{(\ell)}$** if the diffusive relaxation time across the subgraph does not exceed the dephasing time or the window length[cite: 35]:

$$
\tau_{\mathrm{sync}}(A_\ell) := \frac{\tau_{\mathrm{diam}}(A_\ell)}{\lambda_2(A_\ell)} \;\le\; \min\left(\frac{2\pi}{\sigma_\omega(A_\ell)},\; \tau_w^{(\ell)}\right).
$$

### 5.4. Architectural Phase Transition Across Scales: From Compact Modes to Filamentary Networks

**Proposition 5.2 (Synchronization Instability of a Homogeneous $d$-Dimensional Ball as $N \to \infty$ Under Bounded Degree).** `[Status: FOLLOW]`[cite: 35]  
*Suppose subsystem $A$ of $N$ vertices has the topology of a regular $d$-dimensional ball ($d \ge 2$) with bounded vertex degree $\mathrm{deg}(x) \le k_{\max}$[cite: 35]. As $N \to \infty$, the graph diameter grows as $\tau_{\mathrm{diam}}(A) = \Theta(N^{1/d})$, the algebraic connectivity of the normalized Laplacian decays as $\lambda_2(A) = \Theta(N^{-2/d})$, and the global synchronization time diverges as a power law[cite: 35]:*

$$
\tau_{\mathrm{sync}}^{\mathrm{ball}}(N) = \frac{\tau_{\mathrm{diam}}(A)}{\lambda_2(A)} = \Theta\bigl(N^{3/d}\bigr) \;\xrightarrow{\;N \to \infty\;}\; \infty.
$$

*Consequently, for any fixed $k_{\max} < \infty$ and $\sigma_\omega > 0$, there exists a critical size $N_{\mathrm{crit}}(d, k_{\max}, \sigma_\omega)$ above which a homogeneously filled $d$-dimensional ball cannot satisfy the global synchronization criterion of Definition 5.3[cite: 35].*

*Proof.* A ball of volume $N$ in a regular $d$-dimensional lattice has linear radius $R \sim N^{1/d}$[cite: 35]. The smallest non-zero eigenvalue of the discrete Laplacian on a ball of radius $R$ scales as $\lambda_2 \sim R^{-2} \sim N^{-2/d}$, so $\tau_{\mathrm{diam}}/\lambda_2 \sim R / R^{-2} = R^3 \sim N^{3/d}$[cite: 35]. For $N > N_{\mathrm{crit}} \propto (\sigma_\omega)^{-d/3}$, the inequality $\tau_{\mathrm{sync}} \le 2\pi/\sigma_\omega$ fails[cite: 35]. $\blacksquare$

**Structural Consequence (Hypothesis of Universal Filamentary Architecture):** `[Status: UNDECIDED — tested in Protocol V5]`[cite: 35]  
Above $N > N_{\mathrm{crit}}$ under a bounded edge budget $\sum_{x \in A} \mathrm{deg}(x) \le k_{\max} N$, simultaneously minimizing embedding volume $\mathrm{Vol}_h(\Sigma)$ (§3.1) and maintaining short synchronization time $\tau_{\mathrm{sync}}(A) \le \tau_w^{(\ell)}$ forces the network out of homogeneous 3D ball filling into a **sparse node-filament-void percolation architecture** (dense high-clustering nodes linked by quasi-1D coherent filaments bounding empty voids)[cite: 2, 35]. This provides a shared variational mechanism for the structural similarity between the cosmological *Cosmic Web* and biological or artificial neural networks[cite: 1, 3, 35].

---

## 6. Local-Global Channel Balance, Effective Gravity, and Horizon Saturation

### 6.1. Combinatorial Identity of Diamond Partitioning and Void Rarefaction

To prevent double-counting, assign each elementary diamond to its lower causal anchor $x \in X$[cite: 1, 35]:

$$
q_x := \sum_{y \in X:\, K_{xy} \ge 2} K_{xy} \operatorname{Coh}_{xy} = \sum_{y \in X:\, K_{xy} \ge 2} \frac{|M_{xy}|^2}{K_{xy}} \ge 0.
$$

For any subset $U \subseteq X$, define the mean coherent structure density $\rho_D(U) := \frac{1}{|U|} \sum_{x \in U} q_x$ and total coherent resource $Q_{\mathrm{tot}}(X) := \sum_{x \in X} q_x$[cite: 1, 35].

**Proposition 6.1 (Exact Balance Identity Across Local Bulks, Interfaces, and External Channel).** `[Status: FOLLOW]`[cite: 35]  
*If the complex $X$ is partitioned into $M$ disjoint localized subsystems $A_m = \mathcal{I}_{A_m} \sqcup \partial A_m$ ($m = 1, \dots, M$) and the shared external channel $\mathcal{E} = X \setminus \bigcup_{m=1}^M A_m$, then the mean density of coherent diamonds in the external channel $\rho_D(\mathcal{E})$ satisfies the exact identity[cite: 35]:*

$$
\rho_D(\mathcal{E}) = \frac{1}{|\mathcal{E}|} \left( Q_{\mathrm{tot}}(X) - \sum_{m=1}^{M} |\mathcal{I}_{A_m}| \, \rho_D(\mathcal{I}_{A_m}) - \sum_{m=1}^{M} |\partial A_m| \, \rho_D(\partial A_m) \right).
$$

*Proof.* Follows immediately from the additivity of $\sum_{x \in X} q_x$ over the disjoint partition $X = \mathcal{E} \sqcup \bigsqcup_{m=1}^M (\mathcal{I}_{A_m} \sqcup \partial A_m)$[cite: 35]. $\blacksquare$

**Dynamic Mechanism of Local-Global Compensation (Hypothesis H-LG):** `[Status: UNDECIDED — tested in Protocols V2 and V3]`[cite: 35]  
Beyond simple combinatorial edge conservation, in a dynamical ensemble with fixed total edges $E_{\mathrm{tot}}$ and bounded valency $k_{\max}$, local condensation of internal reliefs $\mathcal{I}_{A_m}$ (increasing $\rho_D(\mathcal{I}_{A_m})$ and transverse contraction $\kappa(A_m)$) drives **phase-mediated rarefaction of the external channel $\mathcal{E}$ exceeding combinatorial edge subtraction**[cite: 1, 2, 35]:
1. By Theorem 4.1, increasing $\kappa(A_m)$ increases the outward phase-entropy erasure flux $\dot{I}_{\mathrm{erase}}(A_m) \ge (\kappa(A_m) - h_{\mathrm{KS}}(A_m))/\ln 2$ across $\partial^+ A_m$[cite: 35].
2. By Proposition 2.2(1), this boundary flux propagates into $\mathcal{E}$ via long-range covariance $\Sigma_{\mathcal{I}\mathcal{E}} = \Pi_{\mathcal{I}}^{-1}\Pi_{\mathcal{I},\partial A}\Sigma_{\partial A}\Pi_{\partial A,\mathcal{E}}\Pi_{\mathcal{E}}^{-1} \neq 0$, reconfiguring links in distant void regions $\mathcal{E}_{\mathrm{void}}$ from transverse diamonds ($K_{xy} \ge 2$) into longitudinal unbranched null chains ($K_{xy} = 0$)[cite: 35].
3. Consequently, in $\mathcal{E}_{\mathrm{void}}$ the diamond density $\rho_D(\mathcal{E}_{\mathrm{void}})$ drops, the pure null-link fraction $f_{K=0}(\mathcal{E}_{\mathrm{void}})$ rises, and **the effective null geodesic distance $\ell_{\mathrm{null}}(\mathcal{E}_{\mathrm{void}})$ between distant clusters expands**[cite: 2, 35].

### 6.2. Three-Component Structure of Effective Field Equations in the Continuum Limit

In a macroscopic regime where null paths $\mathcal{E}_{\mathrm{null}}$ ($K_{xy}=0$) reconstruct the conformal structure of a Lorentzian metric $g_{\mu\nu}(x)$ and edge phases $\theta_{xy} = \int_x^y A_\mu dx^\mu$ induce the Maxwell field strength $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$, applying the Landauer interface balance $\delta Q_{\mathrm{ext}} = T_{\partial A} \delta S_{\mathrm{interface}}$ (Theorem 4.1) and the Raychaudhuri equation to local causal screens $\partial A$ yields the target Einstein–Maxwell equation of state[cite: 1, 3, 35]:

$$
R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu} + \Lambda_{\mathrm{eff}}[I_{\mathrm{erase}}] \, g_{\mu\nu} = \frac{8\pi G_{\mathrm{eff}}}{c^4} \Bigl( T_{\mu\nu}^{\mathrm{bulk}}(\mathcal{I}_A) + T_{\mu\nu}^{\mathrm{interface}}(\partial A) + T_{\mu\nu}^{\mathrm{em}}(F_{\alpha\beta}) \Bigr).
$$

**Decomposition by the Triad $(\mathcal{I}_A, \partial A, \mathcal{E}_A)$:** `[Status: UNDECIDED — continuum limit hypothesis]`[cite: 35]
1. **$T_{\mu\nu}^{\mathrm{bulk}}(\mathcal{I}_A)$ — Localized Baryonic/Massive Matter:** contribution of high-synchronization diamond and vortical complexes ($\lambda_2 > \lambda_{\mathrm{crit}}$, $H_{\mathrm{rot}} \neq 0$)[cite: 35].
2. **$T_{\mu\nu}^{\mathrm{interface}}(\partial A)$ — Interfacial Synchronization-Shell Tension:** contribution of the boundary transition zone $\partial A$ where the frequency mismatch between internal clock rate $\omega_A$ and external channel rate $\omega_{\mathrm{ext}}$ is balanced by embedding curvature $\mathbf{H} = \lambda(\nabla i)^\perp$ (Proposition 3.1) and precision-weighted prediction error $\frac{1}{2}(\sigma(\mu) - \overline{\eta}(b))^\top \Pi_{\mathcal{E}}(\sigma(\mu) - \overline{\eta}(b))$ (Proposition 2.2)[cite: 17, 35]. At galactic scales, this extended synchronization interface produces an effective gravitational potential without requiring new particle species in the halo ("dark matter" regime)[cite: 35].
3. **$\Lambda_{\mathrm{eff}}[I_{\mathrm{erase}}] \, g_{\mu\nu}$ — Global Channel Response to Erasure Flux:** cumulative null-mode injection across all outgoing interfaces $\partial^+ A_m$ rarefying the external channel $\mathcal{E}$ ("dark energy" regime), coupled to bulk and interfacial stress-energy via the Bianchi identity[cite: 1, 35]:
   $$
   \frac{8\pi G_{\mathrm{eff}}}{c^4} \nabla^\mu \Bigl( T_{\mu\nu}^{\mathrm{bulk}} + T_{\mu\nu}^{\mathrm{interface}} + T_{\mu\nu}^{\mathrm{em}} \Bigr) = \nabla_\nu \Lambda_{\mathrm{eff}}[I_{\mathrm{erase}}].
   $$

### 6.3. Interface Information Saturation and the Post-Horizon Phase Transition

Combining Theorem 4.1 with Proposition 2.1 defines the dimensionless **interface saturation ratio**[cite: 35]:

$$
\eta_{\mathrm{sat}}(A) := \frac{\dot{I}_{\mathrm{erase}}(\mathcal{I}_A)}{C_{\max}(\partial^+ A)} = \frac{\kappa(A) - h_{\mathrm{KS}}(A)}{c_0 \ln 2 \cdot |\partial^+ A|_E}.
$$

Normal spacetime persistence ($K_{xy}^{\mathrm{eff}} = 2$, $d_{\mathrm{eff}} \approx 4$) requires $\eta_{\mathrm{sat}}(A) < 1$[cite: 35]. Because bulk volume and total contraction $\kappa(A) \propto |\mathcal{I}_A|$ grow faster than boundary area $|\partial^+ A|_E$, sufficiently dense cores reach the saturation threshold $\eta_{\mathrm{sat}}(A) \ge 1$ (`Status: UNDECIDED`, Protocol V6)[cite: 35]:
1. **Exterior Regime (Event Horizon):** The outgoing interface $\partial^+ A$ saturates at capacity $C_{\max}(\partial^+ A)$, screening external observers from deeper bulk layers ($\ker \Pi_{\mathcal{I},\partial A} \not\subseteq \ker \Pi_{\mathcal{E},\partial A}$ in Proposition 2.2, so the synchronization map $\sigma$ becomes degenerate on interior modes) and radiating thermally at temperature $T_{\partial A}$ with area-law entropy $\propto |\partial^+ A|_E$[cite: 12, 13, 35].
2. **Interior Regime (High-Rank Matrix Phase $K_{xy}^{\mathrm{eff}} \ge 3$):** Because excess internal phase fluctuations can no longer be expelled across $\partial^+ A$, the sparsity condition supporting binary diamond collapse fails inside $\mathcal{I}_A$, driving the interior into a dense multi-vertex matrix phase ($K_{xy}^{\mathrm{eff}} \ge 3$) bounded by the horizon screen $\partial A$[cite: 35].

---

## 7. Computational Verification Program (Protocols V1–V7)

All seven protocols operate directly on finite matrices $(R, \Theta)$ without external physical constants, using pre-registered numerical pass/fail thresholds[cite: 2, 35].

| ID | Tested Claim | Protocol & Control Ensembles | Confirmation Criterion (`FOLLOW`) | Refutation Criterion (`NULL`) |
| :--- | :--- | :--- | :--- | :--- |
| **V1** | **Dynamic collapse of multi-vertex bundles into binary diamonds $K_{xy}=2$ and dimension selection (§3.2–3.3)**[cite: 35] | Initialize graphs $N \in \{128, 256\}$ with wide waists $K_{xy} \in \{3, \dots, 8\}$; anneal $\mathcal{F} = a\sum K^2 + b\sum J + g\Vert{}[\Delta_+,\Delta_-]\Vert{}_F^2$ under kernel factorization $\sim_{K,\varepsilon_{\mathrm{ker}}}$ with $\sum J_{xy} \ge J_{\min}$. Control: random DAGs of matched density[cite: 35]. | Quotient binary waist fraction converges to $f_{K=2} \ge 0.80$, and three dimension estimators ($d_s, d_H, d_\tau$) agree within $\le 0.3$ across a decade of scale[cite: 2, 35]. | Graph degenerates into trees ($K_{xy}\le 1$), hubs ($K_{xy} \gg 2$), or dimensions fail to converge $\implies$ closes spontaneous geometry selection[cite: 2, 35]. |
| **V2** | **Oseledets contraction $\kappa(A)$ vs. outgoing interface flux $\partial^+ A$ (§4.2)**[cite: 35] | Extract subsystem $A = (\mathcal{I}_A, \partial A)$ across stiffness parameters $(a, b, g)$. Compute Lyapunov spectrum $\{\lambda_i\}$, $\kappa(A)$, and boundary phase-entropy flux $\dot{I}_{\mathrm{out}}(\partial^+ A)$ under stationary input noise on $\partial^- A$. Control: covariance-matched random matrix[cite: 4, 35]. | Monotonic linear Pearson correlation $r \ge 0.85$ between $(\kappa(A) - h_{\mathrm{KS}}(A))$ and $\dot{I}_{\mathrm{out}}(\partial^+ A)$; invariance to padding with zero-contraction nodes[cite: 35]. | Outgoing flux is independent of $\kappa(A)$ or scales solely with node count $N_A$ $\implies$ closes Oseledets–Landauer bridge on graphs[cite: 35]. |
| **V3** | **Phase-mediated void rarefaction under local bulk condensation (§6.1)**[cite: 35] | On $N \in \{256, 512\}$ at fixed $E_{\mathrm{tot}}$ and $k_{\max}$, condense cores $\mathcal{I}_{A_m}$. Measure far-void residual $\Delta \rho_{D,*}^{\mathrm{far}}(r)$, null fraction $f_{K=0}$, and null path length $\ell_{\mathrm{null}}$. Controls: (1) degree-preserving edge swaps; (2) phase randomization on $\partial^+ A_m$[cite: 1, 35]. | Statistically significant ($> 3\sigma$ beyond combinatorial control) drop $\Delta \rho_{D,*}^{\mathrm{far}} < 0$ and expansion $\Delta \ell_{\mathrm{null}}(\mathcal{E}_{\mathrm{void}}) > 0$; excess vanishes when phases on $\partial^+ A_m$ are randomized[cite: 1, 2, 35]. | Far-void response reduces to trivial edge subtraction $\Delta E / N$ or is insensitive to boundary phase scrambling $\implies$ closes Hypothesis H-LG[cite: 1, 2, 35]. |
| **V4** | **Interfacial synchronization-shell potential on $\partial A$ (§6.2)**[cite: 35] | Measure radial frequency shift $\delta\omega(r)/\omega_\infty$ and interaction free energy $V_{\mathrm{int}}(r)$ around a synchronized cluster ($\omega_A \neq \omega_{\mathrm{ext}}$), separating bulk $\mathscr{S}_{\mathrm{struct}}(\mathcal{I}_A)$ and interface $\mathscr{S}_{\mathrm{interface}}(\partial A)$. Control: frequency-matched cluster $\omega_A = \omega_{\mathrm{ext}}$[cite: 2, 35]. | Presence of an extended interfacial shell $r \in [r_{\mathrm{bulk}}, r_{\mathrm{halo}}]$ where $\partial_r V_{\mathrm{int}}(r) > 0$ scales with frequency jump $\vert{}\omega_A - \omega_{\mathrm{ext}}\vert{}$ and precision error[cite: 17, 35]. | Potential and frequency shift truncate sharply at the core boundary without interfacial extension $\implies$ closes interfacial halo model[cite: 35]. |
| **V5** | **Scale transition from compact modes to filamentary networks (§5.4)**[cite: 35] | Minimize volume and frustration subject to $\lambda_2(A) \ge \lambda_{\mathrm{sync}}$ and $\mathrm{deg}(x) \le k_{\max}$ across $N = 64 \to 256 \to 1024$ and iterative coarse-graining $\mathcal{R}_{\ell \to \ell+1}$. Control: Erdős–Rényi and degree-matched configuration models[cite: 1, 2, 35]. | Compact rotational clusters ($\mathcal{L}_z \neq 0$) dominate for $N < N_{\mathrm{crit}}$; node-filament-void percolation networks emerge for $N > N_{\mathrm{crit}}$ with scale-invariant Laplacian spectrum[cite: 2, 35]. | Above $N_{\mathrm{crit}}$, graphs disconnect, collapse into acyclic trees, or depend on manual thresholds $\theta_\ell$ $\implies$ closes architectural scaling hypothesis[cite: 1, 2, 35]. |
| **V6** | **Interface saturation $\eta_{\mathrm{sat}} \ge 1$ and transition to $K_{xy} \ge 3$ (§6.3)**[cite: 35] | Pump bulk contraction $\kappa(U_c)$ inside core $U_c$ at fixed boundary capacity $\vert{}\partial^+ U_c\vert{}_E$. Track trans-boundary mutual information, kernel inclusion, and interior $(f_{K=2}, \langle K_{xy}\rangle, d_s, d_H, d_\tau)$ across $\eta_{\mathrm{sat}}(U_c) = 1$[cite: 12, 35]. | For $\eta_{\mathrm{sat}} \ge 1$, outward information saturates at $\vert{}\partial^+ U_c\vert{}_E$, $\sigma$ becomes degenerate on deep modes, and the interior transitions to a stable plateau with $K^{\mathrm{eff}}_{xy} \ge 3$[cite: 13, 35]. | For $\eta_{\mathrm{sat}} \ge 1$, the interior degenerates into an unstructured Kleitman–Rothschild 3-layer graph ($d_\tau \to 1, d_H \to \infty$) $\implies$ closes structured post-horizon phase[cite: 2, 35]. |
| **V7** | **Precision kernel inclusion, solenoidal acceleration, and integrator truncation (§2.4, §3.4, §5.2)** | (a) Test $\Sigma_{\mathcal{I}\mathcal{E}} \neq 0$ and recovery accuracy of $\sigma(\overline{\mu}(b)) = \overline{\eta}(b)$ when $\ker \Pi_{\mathcal{I},\partial A} \subseteq \ker \Pi_{\mathcal{E},\partial A}$ vs. violated inclusion[cite: 12, 14]; (b) compare spectral gap $\gamma(Q)$ with $H_{\mathrm{rot}} \neq 0$ vs. $H_{\mathrm{rot}} = 0$[cite: 20, 32]; (c) measure state reconstruction error under integrator-chain truncation at order $n(\ell)=2$[cite: 22, 23]. | (a) Pearson correlation $> 0.98$ for $\sigma(\overline{\mu}(b))$ vs. $\overline{\eta}(b)$ under kernel inclusion and collapse when violated[cite: 14, 15]; (b) strict increase $\gamma(Q) > \gamma(0)$ on anisotropic reliefs[cite: 32]; (c) bounded $O((\gamma_3 \tau_w)^{-1})$ truncation residual for $k \ge 3$[cite: 23]. | Synchronization persists when $\ker \Pi_{\mathcal{I},\partial A} \not\subseteq \ker \Pi_{\mathcal{E},\partial A}$, solenoidal flow slows convergence ($\gamma(Q) < \gamma(0)$), or high-order modes dominate macro-dynamics[cite: 12, 23, 32]. |

---

## 8. Registry of Verification Statuses ($V_4$)

In accordance with Section 0, `FOLLOW` is restricted to definitions and mathematical propositions whose conclusions follow deductively from explicitly stated premises[cite: 4, 35].

| No. | Claim | $V_4$ Status | Basis and Scope of Validity |
| :--- | :--- | :--- | :--- |
| **1** | Hasse transitive irreducibility of $R$, nilpotency $W^N = 0$, and gauge invariance of diamond holonomies $\Phi_{ab}$, frustration $J_{xy}$, and cone commutator norm $\Vert{}[\Delta_+,\Delta_-]\Vert{}_F^2$ | **`FOLLOW`** | Definitions 1.1–1.2; direct algebraic verification under $W \mapsto D_\chi W D_\chi^\dagger$[cite: 2, 35]. |
| **2** | Wilson interference identity for a two-step waist: $\sum_{a<b}(1-\cos\Phi_{ab}) = \frac{1}{2}K_{xy}J_{xy}$ (Proposition 1.1) | **`FOLLOW`** | Exact algebraic identity for all $K_{xy} \ge 1$ and arbitrary edge phases $\theta_{xy}$[cite: 1, 2, 35]. |
| **3** | Disjoint partitioning of $X$ by any proper subsystem $A$ into $(\mathcal{I}_A, \partial A, \mathcal{E}_A)$, indivisibility criterion $I(A;\tau_w) > \theta_I$, and interface recoverability bound $I(Z_A; \hat{Z}_A) \le I(Z_A; Z_B) + n C(\partial^+ A)$ (Definitions 2.1–2.2, Proposition 2.1) | **`FOLLOW`** | Graph locality of $R_{xy}$ and the data processing inequality under the stated memoryless Markov channel assumptions[cite: 4, 35]. |
| **4** | Equivalence of Markov blanket screening to precision sparsity $\Pi_{\mathcal{I}\mathcal{E}} = 0$, exact mediated covariance formula $\Sigma_{\mathcal{I}\mathcal{E}} = \Pi_{\mathcal{I}}^{-1}\Pi_{\mathcal{I},\partial A}\Sigma_{\partial A}\Pi_{\partial A,\mathcal{E}}\Pi_{\mathcal{E}}^{-1}$, and the boundary kernel-inclusion theorem $\ker \Pi_{\mathcal{I},\partial A} \subseteq \ker \Pi_{\mathcal{E},\partial A}$ for synchronization $\sigma(\overline{\mu}(b)) = \overline{\eta}(b)$ (Proposition 2.2) | **`FOLLOW`** | Exact linear-algebraic and Gaussian conditional-independence identities for $\Pi \succ 0$[cite: 11, 12, 25, 26]. |
| **5** | Stationary informational minimal surface equation $\mathbf{H}(z) = \lambda(\nabla_Z i(z))^\perp$ (Proposition 3.1) and orthogonal tangent splitting $T_z D_\ell = W^{\mathrm{act}}_z \oplus_h W^{\mathrm{inv}}_z \oplus_h K_z$ | **`FOLLOW`** | Calculus of variations at fixed carrier measure density $\delta(d\mu_\Sigma)=0$[cite: 5, 35] and linear projection under a positive-definite metric $h_z$[cite: 7, 35]. |
| **6** | Global minimum of the convex waist functional $\mathcal{F}_{\mathrm{loc}} = a(K^{\mathrm{eff}})^2 + b J^{\mathrm{eff}}_{xy}$ subject to $J^{\mathrm{eff}}_{xy} = J_0 \in (0, 2]$ under exact phase factorization ($\varepsilon_{\mathrm{ker}}=0$) occurs uniquely at the binary causal diamond $K^{\mathrm{eff}}_{xy} = 2$ (Theorem 3.1) | **`FOLLOW`** | Exact integer optimization: $K^{\mathrm{eff}}=1 \implies J^{\mathrm{eff}}=0$, and $a k^2$ is strictly increasing for $k \ge 2$[cite: 35]. |
| **7** | Unitary transition group $U(2) \cong U(1) \times SU(2)/\mathbb{Z}_2$ on the two-channel section of a binary diamond, and minimal spatial dimension $d_{\mathrm{space}}^{\min} = 1 + 2 = 3 = \binom{3}{2}$ for $W^{\mathrm{act}} \oplus_h W^{\mathrm{inv}}$ supporting a 2D circulation plane (§3.3) | **`FOLLOW`** | Linear algebra on $\mathbb{C}^2$ and rank arithmetic under $\dim W^{\mathrm{act}} \ge 1$ and $\dim W^{\mathrm{inv}} \ge 2$[cite: 2, 35]. |
| **8** | Helmholtz drift decomposition $f = f_{\mathrm{rev}} + f_{\mathrm{irrev}}$, invariance of the stationary Gaussian density under skew-symmetric solenoidal flow $Q = -Q^\top$, and spectral gap acceleration $\gamma(Q) \ge \gamma(0)$ (Proposition 3.2) | **`FOLLOW`** | Stationary Fokker–Planck equation and Bendixson–field-of-values bound $\operatorname{Re}(v^\dagger(S+A)v) = v^\dagger S v \ge \lambda_{\min}(S)$[cite: 26, 28, 32]. |
| **9** | Lower bound on outgoing interface erasure flux $\dot{I}_{\mathrm{erase}}(\mathcal{I}_A \to \partial^+ A) \ge (\kappa(A) - h_{\mathrm{KS}}(A))/\ln 2$ and heat dissipation $\dot{Q}_{\mathrm{ext}} \ge k_B T_{\partial A}(\kappa(A) - h_{\mathrm{KS}}(A))$ (Theorem 4.1) | **`FOLLOW`** | Conditional theorem: follows from linear tangent-volume entropy transformation under stationary $H(Z_{n+1})=H(Z_n)$ and Landauer's bound[cite: 35]. |
| **10** | Stochastic realization of rational-spectrum boundary processes as nested Ornstein–Uhlenbeck integrator chains $\tilde{s}_t = (s_t^{(0)}, \dots, s_t^{(n)})$ and emergence of second-order inertial dynamics upon truncation at $n(\ell)=2$ (Proposition 5.1) | **`FOLLOW`** | Doob's theorem, spectral factorization of rational spectral densities, and linear-quadratic optimization at $n=2$[cite: 21, 22, 23]. |
| **11** | Relative operational time $R_{AB}^{(\ell)}$, coarse-graining operator $\mathcal{R}_{\ell \to \ell+1}$, and divergence of synchronization time on a homogeneous $d$-dimensional ball $\tau_{\mathrm{sync}}^{\mathrm{ball}}(N) = \Theta(N^{3/d}) \to \infty$ as $N \to \infty$ at bounded degree $k_{\max}$ (Proposition 5.2) | **`FOLLOW`** | Definitions 5.1–5.3 and asymptotic spectral scaling of the discrete Laplacian on a ball of radius $R \sim N^{1/d}$[cite: 35]. |
| **12** | Exact additive conservation identity partitioning coherent diamonds across bulk interiors $\mathcal{I}_{A_m}$, interfaces $\partial A_m$, and external channel $\mathcal{E}$ (Proposition 6.1) | **`FOLLOW`** | Exact combinatorial identity on a finite set $X$[cite: 35]. |
| **13** | Spontaneous emergence of a macroscopic $3+1$ Lorentzian manifold phase in annealed ensembles of random causal graphs | **`UNDECIDED`** | Computational hypothesis; tested in **Protocol V1**[cite: 2, 35]. |
| **14** | Physical correspondence between discrete Oseledets contraction $\kappa(A)$ on a causal graph and physical radiation flux in the external channel | **`UNDECIDED`** | Tested numerically in **Protocol V2**; requires continuum calibration[cite: 1, 35]. |
| **15** | Phase-mediated void rarefaction ($\Delta\rho_{D,*}^{\mathrm{far}} < 0$, null path stretching $\Delta\ell_{\mathrm{null}} > 0$) beyond combinatorial edge subtraction and its identification with effective dark energy $\Lambda_{\mathrm{eff}}$ | **`UNDECIDED`** | Tested in **Protocol V3**[cite: 1, 2, 35]. |
| **16** | Derivation of continuum Einstein–Maxwell equations from interfacial balance (§6.2) and attribution of galactic rotation-curve anomalies to interfacial synchronization tension $T_{\mu\nu}^{\mathrm{interface}}(\partial A)$ | **`UNDECIDED`** | Tested in **Protocol V4**; requires continuum limit proof[cite: 1, 35]. |
| **17** | Percolation transition to "node–filament–void" networks above $N_{\mathrm{crit}}$ as a shared variational origin of the *Cosmic Web* and neural architectures | **`UNDECIDED`** | Tested in **Protocol V5** against degree-preserving configuration null models[cite: 1, 35]. |
| **18** | Formation of an informational horizon at $\eta_{\mathrm{sat}}(A) \ge 1$ and transition of the interior bulk to a stable high-rank matrix phase $K_{xy}^{\mathrm{eff}} \ge 3$ | **`UNDECIDED`** | Tested in **Protocol V6**[cite: 35]. |
| **19** | Heuristic analogies ("soap film", "hydraulic fluid", "cognitive agent") | **`OMIT`** | Pedagogical orientation only; never used as proof premises[cite: 3, 5, 35]. |
| **20** | Soft linear degree penalties without hard valency bound $k_{\max}$; postulating fixed microscopic dimensions ($5, 9, 11$) prior to kernel factorization; treating $+1$ time as a scale-invariant spatial axis; claiming a passive Gaussian Markov blanket without action loop or stake is an intrinsic agent | **`NULL`** | Refuted by the Kleitman–Rothschild $O(N^2)$ entropy theorem[cite: 2, 35], Theorem 3.1, Proposition 5.2, and negative controls on passive Ornstein–Uhlenbeck systems[cite: 4]. |

---

## 9. Reference Computational Implementation (Python / NumPy / SciPy)

The self-contained Python module below implements the mathematical structures of Sections 1–6 and provides executable routines for Verification Protocols V1–V7[cite: 35].

```python
import numpy as np
from scipy.sparse.csgraph import connected_components, shortest_path
from scipy.linalg import eigh, eigvals, svdvals, pinv, sqrtm

# =====================================================================
# 1. FOUNDATIONAL CAUSAL-PHASE ALGEBRA (SECTION 1)
# =====================================================================

def is_hasse_transitive_free(R):
    """
    Verify Hasse transitive irreducibility for a strictly upper-triangular
    Boolean matrix R: no edge short-circuits a directed path of length >= 2.
    """
    N = len(R)
    if not np.all(np.tril(R) == 0):
        return False
    reach_all = np.linalg.inv(np.eye(N) - R) - np.eye(N)
    reach_2plus = reach_all - R
    return not np.any((R > 0) & (reach_2plus > 0.5))


def compute_causal_phase_invariants(R, Theta):
    """
    Compute the waist matrix K_xy, two-step amplitude M_xy, phase frustration J_xy,
    and gauge-invariant cone-commutator norm L(W) = ||[Delta_+, Delta_-]||_F^2
    (Proposition 1.1 and Section 1.4).
    """
    W = R * np.exp(1j * Theta)
    K = R @ R
    M = W @ W
    mask = K > 0
    J = np.zeros(K.shape, dtype=float)
    J[mask] = (K[mask] ** 2 - np.abs(M[mask]) ** 2) / K[mask]

    Dp = W @ W.conj().T
    Dm = W.conj().T @ W
    C = Dp @ Dm - Dm @ Dp
    L_raw = float(np.real(np.trace(C.conj().T @ C)))
    norm_factor = 1.0 + float(np.linalg.norm(Dp, "fro") ** 2 * np.linalg.norm(Dm, "fro") ** 2)
    L_norm = L_raw / norm_factor
    return K, M, J, L_raw, L_norm


def verify_wilson_identity(R, Theta):
    """
    Numerical verification of Proposition 1.1:
    Sum_{a < b} (1 - cos(Phi_ab)) == 0.5 * K_xy * J_xy.
    """
    N = len(R)
    K, _, J, _, _ = compute_causal_phase_invariants(R, Theta)
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
# 2. TRIAD PARTITIONING (I_A, dA, E_A) AND INTEGRATION (SECTION 2)
# =====================================================================

def partition_triad(R, subsystem_nodes):
    """
    Partition complex X into the structural triad (Definition 2.1):
    - I_A: internal relief (Bulk);
    - dA_in, dA_out, dA: incoming, outgoing, and bilateral interface;
    - E_A: external synchronization channel;
    - E_null_edges: unbranched null links in the external channel (K_xy = 0).
    """
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

    K = R @ R
    E_null_edges = (R == 1) & (K == 0) & E_mask[:, None] & E_mask[None, :]

    return {
        "I_A": I_A,
        "dA_in": dA_in,
        "dA_out": dA_out,
        "dA": dA,
        "E_A": E_A,
        "capacity_in": int(np.sum(edges_in)),
        "capacity_out": int(np.sum(edges_out)),
        "E_null_edges": E_null_edges,
    }


def compute_integration_spectral_proxy(R, Theta, subsystem_nodes, eps=1e-12):
    """
    Spectral proxy for subsystem integration I(A; tau_w) (Definition 2.2)
    using internal Fiedler connectivity lambda_2 relative to boundary flux.
    """
    idx = np.array(sorted(subsystem_nodes), dtype=int)
    if len(idx) < 2:
        return 0.0
    W = R * np.exp(1j * Theta)
    W_int = W[np.ix_(idx, idx)]
    A_sym = (np.abs(W_int) ** 2) + (np.abs(W_int.T) ** 2)

    if connected_components(A_sym > 0, directed=False)[0] > 1:
        return 0.0

    deg = np.maximum(A_sym.sum(axis=1), eps)
    D_inv_sqrt = np.diag(1.0 / np.sqrt(deg))
    L_norm = np.eye(len(idx)) - D_inv_sqrt @ A_sym @ D_inv_sqrt
    evals = np.sort(eigh(L_norm, eigvals_only=True))
    lambda_2 = float(max(0.0, evals[1]))

    int_flow = float(np.sum(A_sym) / 2.0) / len(idx)
    ext_idx = np.setdiff1d(np.arange(len(R)), idx)
    bnd_flow = float(
        np.sum(np.abs(W[np.ix_(idx, ext_idx)]) ** 2)
        + np.sum(np.abs(W[np.ix_(ext_idx, idx)]) ** 2)
    ) / len(idx)
    return float(lambda_2 * int_flow / (bnd_flow + eps))


# =====================================================================
# 3. KERNEL-PATH COLLAPSE INTO BINARY DIAMONDS K_xy = 2 (THEOREM 3.1, V1)
# =====================================================================

def kernel_path_diamond_collapse(R, Theta, eps_ker=0.30):
    """
    Factorize waists with K_xy > 2 by the phase kernel ~_{K, eps_ker}
    (Definition 3.1 and Theorem 3.1), merging coherent intermediate nodes
    z_a, z_b in V_xy when d_T(phi_a, phi_b) <= eps_ker while preserving Hasse irreducibility.
    """
    N = len(R)
    K = R @ R
    reach = (np.linalg.inv(np.eye(N) - R) - np.eye(N)) > 0.5
    parent = np.arange(N, dtype=int)

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    for x in range(N - 2):
        for y in range(x + 2, N):
            if K[x, y] > 2:
                zs = np.where((R[x, :] == 1) & (R[:, y] == 1))[0]
                phases = (Theta[x, zs] + Theta[zs, y]) % (2.0 * np.pi)
                for a in range(len(zs)):
                    for b in range(a + 1, len(zs)):
                        za, zb = zs[a], zs[b]
                        if not (reach[za, zb] or reach[zb, za]):
                            dphi = abs(phases[a] - phases[b])
                            dphi = min(dphi, 2.0 * np.pi - dphi)
                            if dphi <= eps_ker:
                                ra, rb = find(za), find(zb)
                                if ra != rb:
                                    parent[max(ra, rb)] = min(ra, rb)

    clusters = {}
    for u in range(N):
        clusters.setdefault(find(u), []).append(u)
    sorted_clusters = sorted(clusters.values(), key=lambda c: np.mean(c))
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
                W_red[a, b] = np.sum(sub_W)

    reach_all = np.linalg.inv(np.eye(M) - R_red) - np.eye(M)
    reach_2plus = reach_all - R_red
    R_red[(R_red > 0) & (reach_2plus > 0.5)] = 0
    Theta_red = np.mod(np.angle(W_red), 2.0 * np.pi) * R_red

    K_red = R_red @ R_red
    n_ge2 = int(np.sum(K_red >= 2))
    f_K2 = float(np.sum(K_red == 2) / max(1, n_ge2))
    return R_red, Theta_red, f_K2


# =====================================================================
# 4. OSELEDETS SPECTRUM AND LANDAUER ERASURE FLUX (THEOREM 4.1, V2)
# =====================================================================

def compute_oseledets_landauer_profile(R, Theta, subsystem_nodes, dissipation=0.45, eps=1e-12):
    """
    Compute the local Lyapunov spectrum {lambda_i} on subgraph A,
    transverse contraction rate kappa(A) = Sum_{lambda_i < 0} |lambda_i|,
    Pesin entropy rate h_KS(A), Kaplan-Yorke dimension D_KY(A), and
    lower bound on outward erasure flux I_erase_bits (Theorem 4.1).
    """
    idx = np.array(sorted(subsystem_nodes), dtype=int)
    n_sub = len(idx)
    if n_sub == 0:
        return {"kappa": 0.0, "h_KS": 0.0, "D_KY": 0.0, "I_erase_bits": 0.0}

    W_sub = (R * np.exp(1j * Theta))[np.ix_(idx, idx)]
    H_sym = 0.5 * (W_sub + W_sub.conj().T)
    H_rot = (W_sub - W_sub.conj().T) / (2j)

    M_jac = (1.0 - dissipation) * np.eye(n_sub) + 0.5 * (H_sym + 1j * H_rot)
    s_vals = np.maximum(svdvals(M_jac), eps)
    lyap = np.sort(np.log(s_vals))[::-1]

    kappa = float(np.sum(np.abs(lyap[lyap < 0.0])))
    h_KS = float(np.sum(lyap[lyap > 0.0]))

    csum = np.cumsum(lyap)
    pos_idx = np.where(csum >= 0.0)[0]
    if len(pos_idx) == 0:
        D_KY = 0.0
    elif pos_idx[-1] == n_sub - 1:
        D_KY = float(n_sub)
    else:
        j = int(pos_idx[-1])
        D_KY = float((j + 1) + csum[j] / max(abs(lyap[j + 1]), eps))

    I_erase_bits = float(max(0.0, (kappa - h_KS) / np.log(2.0)))
    return {
        "lyapunov_spectrum": lyap,
        "kappa": kappa,
        "h_KS": h_KS,
        "D_KY": D_KY,
        "I_erase_bits": I_erase_bits,
    }


# =====================================================================
# 5. MULTISCALE SYNCHRONIZATION AND CHANNEL BALANCE (SECTIONS 5-6, V3-V6)
# =====================================================================

def evaluate_synchronization_and_balance(R, Theta, core_nodes, eps=1e-12):
    """
    Diagnostic suite for Protocols V3, V5, and V6:
    - synchronization time tau_sync = tau_diam / lambda_2 (Definition 5.3);
    - exact diamond balance across bulk, interface, and external channel (Proposition 6.1);
    - pure null link fraction f_{K=0} and mean null distance l_null in the external channel;
    - interface saturation ratio eta_sat (Section 6.3).
    """
    N = len(R)
    triad = partition_triad(R, core_nodes)
    K, M_amp, _, _, _ = compute_causal_phase_invariants(R, Theta)

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
    if len(A_nodes) >= 2:
        R_A = R[np.ix_(A_nodes, A_nodes)]
        A_sym = R_A + R_A.T
        dist_A = shortest_path(A_sym, directed=False, unweighted=True)
        fin_A = dist_A[np.isfinite(dist_A) & (dist_A > 0)]
        tau_diam = float(np.max(fin_A)) if len(fin_A) > 0 else 1.0

        deg = np.maximum(A_sym.sum(axis=1), eps)
        D_inv_sqrt = np.diag(1.0 / np.sqrt(deg))
        L_norm = np.eye(len(A_nodes)) - D_inv_sqrt @ A_sym @ D_inv_sqrt
        evals = np.sort(eigh(L_norm, eigvals_only=True))
        lambda_2 = float(max(eps, evals[1]))
        tau_sync = float(tau_diam / lambda_2)
    else:
        tau_sync = 0.0

    ext_mask = np.isin(np.arange(N)[:, None], E_A) & np.isin(np.arange(N)[None, :], E_A)
    n_ext_edges = int(np.sum((R == 1) & ext_mask))
    n_null_edges = int(np.sum(triad["E_null_edges"]))
    f_null_void = float(n_null_edges / max(1, n_ext_edges))

    if len(E_A) >= 2:
        R_E = R[np.ix_(E_A, E_A)]
        dist_E = shortest_path(R_E + R_E.T, directed=False, unweighted=True)
        fin_E = dist_E[np.isfinite(dist_E) & (dist_E > 0)]
        l_null_void = float(np.mean(fin_E)) if len(fin_E) > 0 else np.nan
    else:
        l_null_void = np.nan

    oseledets = compute_oseledets_landauer_profile(R, Theta, A_nodes)
    eta_sat = float(oseledets["I_erase_bits"] / max(1, triad["capacity_out"]))

    return {
        "Q_tot": Q_tot,
        "rho_bulk": rho_I,
        "rho_interface": rho_dA,
        "rho_void": rho_E,
        "balance_identity_error": float(balance_residual),
        "tau_sync": tau_sync,
        "f_null_void": f_null_void,
        "l_null_void": l_null_void,
        "I_erase_bits": oseledets["I_erase_bits"],
        "capacity_out": triad["capacity_out"],
        "eta_saturation": eta_sat,
    }


# =====================================================================
# 6. PRECISION KERNEL INCLUSION, SOLENOIDAL GAP & INTEGRATORS (PROTOCOL V7)
# =====================================================================

def verify_precision_helmholtz_and_integrator_chain(
    Pi_E, Pi_Eb, Pi_b, Pi_Ib, Pi_I, Gamma, Q_sol, gamma_modes=(0.1, 0.5, 1.2, 8.0, 15.0), tau_w=0.8
):
    """
    Executable verification suite for Protocol V7 (Propositions 2.2, 3.2, and 5.1):
    1. Constructs the block-sparse Markov blanket precision matrix Pi (Pi_{IE} = 0),
       verifies non-zero mediated covariance Sigma_{IE}, and tests the synchronization
       map sigma(mu_bar(b)) == eta_bar(b) under kernel inclusion.
    2. Compares the spectral relaxation rate gamma(Q) of the Helmholtz drift
       B(Q) = (Gamma + Q) * Pi_I against pure gradient relaxation gamma(0).
    3. Evaluates the relative variance residual of modes k >= 3 under coarse-graining
       window tau_w in an Ornstein-Uhlenbeck integrator chain.
    """
    d_E, d_b, d_I = len(Pi_E), len(Pi_b), len(Pi_I)
    Z_EI = np.zeros((d_E, d_I))

    Pi = np.block([
        [Pi_E, Pi_Eb, Z_EI],
        [Pi_Eb.T, Pi_b, Pi_Ib.T],
        [Z_EI.T, Pi_Ib, Pi_I]
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

    # Synchronization map sigma: Im(mu_bar) -> Im(eta_bar) (Proposition 2.2)
    sigma_map = np.linalg.inv(Pi_E) @ Pi_Eb @ pinv(Pi_Ib) @ Pi_I
    B_samples = np.random.default_rng(42).normal(size=(d_b, 200))
    eta_expected = -np.linalg.inv(Pi_E) @ Pi_Eb @ B_samples
    mu_expected = -np.linalg.inv(Pi_I) @ Pi_Ib @ B_samples
    eta_predicted = sigma_map @ mu_expected
    sync_err = float(np.max(np.abs(eta_expected - eta_predicted)))

    # Helmholtz relaxation spectral gap gamma(Q) vs gamma(0) (Proposition 3.2)
    B_0 = Gamma @ Pi_I
    B_Q = (Gamma + Q_sol) @ Pi_I
    gamma_0 = float(np.min(np.real(eigvals(B_0))))
    gamma_Q = float(np.min(np.real(eigvals(B_Q))))

    # Integrator-chain window truncation residual for modes k >= 3 (Proposition 5.1)
    gammas = np.array(gamma_modes, dtype=float)
    # Exact window-averaged variance factor for OU mode: 2*(g*T - 1 + exp(-g*T))/(g*T)^2
    gT = gammas * tau_w
    win_factors = 2.0 * (gT - 1.0 + np.exp(-gT)) / np.maximum(gT ** 2, 1e-12)
    fast_truncation_ratio = float(np.sum(win_factors[3:]) / max(np.sum(win_factors[:3]), 1e-12))

    return {
        "Sigma_IE_frobenius_norm": float(np.linalg.norm(Sigma_IE, "fro")),
        "mediated_covariance_identity_error": cov_formula_err,
        "synchronization_map_max_error": sync_err,
        "spectral_gap_gradient_only": gamma_0,
        "spectral_gap_with_solenoidal_Q": gamma_Q,
        "solenoidal_acceleration_gain": float(gamma_Q - gamma_0),
        "integrator_fast_mode_residual_ratio": fast_truncation_ratio,
    }
```

---

## 10. References

1. **Causal Sets and Lorentzian Geometry Reconstruction:** L. Bombelli, J. Lee, D. Meyer, R. D. Sorkin, *Space-Time as a Causal Set*, Physical Review Letters **59**, 521–524 (1987)[cite: 1, 3, 35]; S. Surya, *The Causal Set Approach to Quantum Gravity*, Living Reviews in Relativity **22**, 5 (2019)[cite: 1, 35].
2. **Combinatorial Asymptotics of Partial Orders:** D. J. Kleitman, B. L. Rothschild, *Asymptotic Enumeration of Partial Orders on a Finite Set*, Transactions of the American Mathematical Society **205**, 205–220 (1975)[cite: 35].
3. **Thermodynamic Derivation of Field Equations and Relative Entropy:** T. Jacobson, *Thermodynamics of Spacetime: The Einstein Equation of State*, Physical Review Letters **75**, 1260–1263 (1995)[cite: 1, 3, 35]; H. Araki, *Relative Entropy of States of von Neumann Algebras*, Publications of the RIMS **11**, 809–833 (1976)[cite: 35]; A. Uhlmann, *Relative Entropy and the Wigner–Yanase–Dyson–Lieb Concavity in an Interpolation Theory*, Communications in Mathematical Physics **54**, 21–32 (1977)[cite: 35]; P. Dorau, R. Verch, M. Much, works on deriving gravitational field equations from Araki–Uhlmann relative entropy on causal diamonds[cite: 35].
4. **Markov Blankets, Helmholtz Decomposition, and Non-Equilibrium Stationary Processes:** L. Da Costa, K. Friston, C. Heins, G. A. Pavliotis, *Bayesian Mechanics for Stationary Processes*, Proceedings of the Royal Society A **477**, 20210518 (2021)[cite: 8]; G. A. Pavliotis, *Stochastic Processes and Applications: Diffusion Processes, the Fokker–Planck and Langevin Equations*, Springer (2014)[cite: 30]; T. Lelièvre, F. Nier, G. A. Pavliotis, *Optimal Non-Reversible Linear Drift for the Convergence to Equilibrium of a Diffusion*, Journal of Statistical Physics **152**, 237–274 (2013)[cite: 32]; J. L. Doob, *The Brownian Movement and Stochastic Equations*, Annals of Mathematics **43**, 351–369 (1942)[cite: 32]; A. Lindquist, G. Picci, *Linear Stochastic Systems: A Geometric Approach to Modeling, Estimation and Identification*, Springer (2015)[cite: 32]; M. Biehl, F. A. Pollock, R. Kanai, *A Technical Critique of Some Parts of the Free Energy Principle*, Entropy **23**, 293 (2021)[cite: 30]; M. Aguilera, B. Millidge, A. Tschantz, C. L. Buckley, *How Particular Is the Physics of the Free Energy Principle?*, Physics of Life Reviews (2021/2022)[cite: 30].
5. **Thermodynamics of Computation and Quantum Rate Bounds:** R. Landauer, *Irreversibility and Heat Generation in the Computing Process*, IBM Journal of Research and Development **5**, 183–191 (1961)[cite: 3, 35]; N. Margolus, L. B. Levitin, *The Maximum Speed of Dynamical Evolution*, Physica D **120**, 188–195 (1998)[cite: 3, 35]; J. D. Bekenstein, *Universal Upper Bound on the Entropy-to-Energy Ratio for Bounded Systems*, Physical Review D **23**, 287–298 (1981)[cite: 3, 35].
6. **Multiplicative Ergodic Theory, Attractor Dimension, and Dichotomy Projectors:** V. I. Oseledets, *A Multiplicative Ergodic Theorem: Characteristic Ljapunov Exponents of Dynamical Systems*, Transactions of the Moscow Mathematical Society **19**, 197–231 (1968)[cite: 4, 35]; Ya. B. Pesin, *Characteristic Lyapunov Exponents and Smooth Ergodic Theory*, Russian Mathematical Surveys **32**(4), 55–114 (1977)[cite: 4, 35]; J. L. Kaplan, J. A. Yorke, *Chaotic Behavior of Multidimensional Difference Equations*, Lecture Notes in Mathematics **730**, 204–227 (1979)[cite: 4, 35]; D. G. Clark, *Lyapunov Spectrum and Minimum-Norm Tangent Response in High-Dimensional Networks* (2026)[cite: 4, 35]; R. Engelken, F. Wolf, L. F. Abbott, *Lyapunov Spectra of Chaotic Recurrent Neural Networks*, Physical Review Research **5**, 043044 (2023)[cite: 4, 35].
7. **Noncommutative Geometry and Thermal Time:** A. Connes, *Noncommutative Geometry*, Academic Press (1994)[cite: 3, 35]; A. Connes, C. Rovelli, *Von Neumann Algebra Automorphisms and Time-Thermodynamics Relation in Generally Covariant Quantum Theories*, Classical and Quantum Gravity **11**, 2899–2917 (1994)[cite: 1, 3, 35].
8. **Matrix Models and Holographic Complexity:** T. Banks, W. Fischler, S. H. Shenker, L. Susskind, *M Theory as a Matrix Model: A Conjecture*, Physical Review D **55**, 5112–5128 (1997)[cite: 1, 35]; A. R. Brown, D. A. Roberts, L. Susskind, B. Swingle, Y. Zhao, *Complexity, Action, and Black Holes*, Physical Review D **93**, 086006 (2016)[cite: 1, 35].
9. **Information Bottleneck, Causal Emergence, and Network Null Models:** N. Tishby, F. C. Pereira, W. Bialek, *The Information Bottleneck Method*, Allerton Conference (1999)[cite: 3, 6, 35]; E. P. Hoel, L. Albantakis, G. Tononi, *Quantifying Causal Emergence Shows That Macro Can Beat Micro*, PNAS **110**, 19790–19795 (2013)[cite: 3, 6, 35]; F. Vazza, A. Feletti, *The Quantitative Comparison Between the Neuronal Network and the Cosmic Web*, Frontiers in Physics **8**, 525731 (2020)[cite: 1, 35]; F. Váša, B. Mišić, *Null Models in Network Neuroscience*, Nature Reviews Neuroscience **23**, 493–504 (2022)[cite: 1, 35].
10. **Three-Valued Entailment Logic and Verification Semilattices:** N. P. Brusentsov, *The Improvement of Inference Logic* [Usovershenstvovanie logiki umozaklyucheniy], Moscow: New Millennium Foundation (2012)[cite: 3, 6, 35]; L. Carroll, *Symbolic Logic*, Macmillan (1896)[cite: 6, 35].