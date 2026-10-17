# Causal-Phase Geometry Research Program (v2.0)

**Matrix Kinematics, Budget-Constrained Coarse-Graining, and the Dual Origin of Dark Sector Effects**

**Author:** Vladimir Yakunin  
**Version:** 2.0  
**Date:** October 17, 2026  
**Status:** Active research program under hypothesis $H_P$ (incorporating formal mathematical structures from VIM v1.0, LAF v2.0, and Spectral Realization of $V_4$ v2.2)  
**Supersedes:** `Causal_Phase_Geometry_Research_Program.md` (August 2026 draft)

---

## Abstract

We formulate an extended structural hypothesis for the Causal-Phase Geometry program ($H_P$) that mathematically connects local gravitational condensation, electromagnetic radiation, and global cosmological expansion without introducing new fundamental fields, extra spatial dimensions, or ad-hoc fluid equations of state. 

At the microscopic level, spacetime kinematics is represented by a locally finite causal set $\mathcal{C} = (X, \prec)$ equipped with $U(1)$ phase holonomies on oriented links, encoded as a strictly upper-triangular complex transfer matrix $W_{xy} = r_{xy} e^{i\theta_{xy}}$. Direct causal links ($I(x,y) = \emptyset$) form the null (lightlike) radiative scaffold, whereas massive matter corresponds to dense clusters of multi-step causal chains ($I(x,y) \neq \emptyset$) that accumulate proper time and discrete volume.

By importing three proven mathematical results from the companion AI/latent-geometry corpus—(i) the variational mean-curvature balance of informational minimal surfaces (VIM), (ii) the kernel-path quotient construction ($\sim_{K,\ell}$), and (iii) the tangent-space Lyapunov dichotomy under a bounded distinction budget (LAF)—we show that the correlation functional $\Gamma_{\rm corr}[g, A]$ splits naturally into two coupled regimes. When local baryonic and electromagnetic configurations saturate the Bekenstein–Casini relative-entropy bound $D_{\rm KL}(\sigma \| \rho_{\rm dyn}) \le c \cdot N_\partial$, the graph must allocate finite causal capacity to sustain transverse contraction ($\lambda_i < 0$ in the stable subspace $E^s$). On the boundary of saturated regions ($\nabla D_{\rm KL} \neq 0$), the Lagrange multiplier enforcing the capacity bound induces a normal surface-tension response $\mathbf{H} = \lambda (\nabla i)^\perp$, reproducing flat galactic rotation curves and black-hole/halo scaling (effective dark matter). Globally, under a conserved causal-distinction rate (Margolus–Levitin bound), condensing vertices into local attractors depletes intermediate timelike events along long-range null links in cosmic voids. Because observers measure distance and redshift via null phase transport ($1+z = \omega_{\rm em}/\omega_{\rm obs}$), this vertex deficit manifests macroscopically as positive metric volume expansion ($h_{\rm KS} > 0$ in $E^u$, effective dark energy). Quantum gravity is thus identified not as a quantization of attractive spin-2 gravitons, but as the global entropic decompression of the causal scaffold driven by local informational condensation.

---

## 0. Canonical Notation and Cross-Corpus Alignment

| Symbol | Mathematical / Physical Object | Origin in Repository |
| :--- | :--- | :--- |
| $\mathcal{C} = (X, \prec)$ | Locally finite causal set (strict partial order: $x \prec y$ implies $x \neq y$ and no cycles) | `KK_Jacobson` §2.1, `CPG` v1 §2 |
| $I(x, y)$ | Causal diamond $\{z \in X \mid x \prec z \prec y\}$; discrete volume measure $V(x,y) = v_* \vert{}I(x,y)\vert{}$ | `KK_Jacobson` §2.1 |
| $\mathrm{Link}(\mathcal{C})$ | Set of irreducible causal relations (links / Hasse edges): $x \prec_* y \iff x \prec y \land I(x,y) = \emptyset$ | Introduced in v2.0 |
| $W_{xy} = r_{xy} e^{i\theta_{xy}}$ | Causal-phase transfer matrix: $r_{xy} \in \{0,1\}$ (or $[0,1]$ under relaxation), $\theta_{xy} \in [0, 2\pi)$ | Introduced in v2.0 |
| $W_D = W(\gamma_1, \gamma_2)$ | Relative $U(1)$ holonomy $U(\gamma_1)U(\gamma_2)^{-1}$ across two chains bounding a minimal diamond $D$ | `KK_Jacobson` §2.2, `CPG` v1 §2 |
| $\pi_\ell : (\mathcal{C}, W) \to (M_4, g_{\mu\nu})$ | Scale-indexed coarse-graining projection onto the continuum Lorentzian base | `Algorithm` §9, `Spectral_V4` §1.1 |
| $K_z = \ker(d\pi_\ell)$ | Kernel distribution of the metric projection (contains local $U(1)$ gauge shifts and null generators) | `Spectral_V4` §1.1–1.3 |
| $\rho_{\rm dyn}, \sigma$ | Dynamical vacuum state ($\langle \mathrm{Re} W_D \rangle \to 1$) and excited phase-matter state on a causal diamond | `CPG` v1 §4.1 |
| $N_\partial = \vert{}\partial D\vert{}$ | Cardinality of the spatial antichain / boundary cut of a causal diamond (discrete horizon area) | `CPG` v1 §4.2, `Tech_Spec` v0.1 §2 |
| $i(x) := D_{\rm KL}(\sigma_x \Vert{} \rho_{\rm dyn})$ | Local relative-entropy density evaluated on gauge-invariant diamond descriptors | `CPG` v1 §4.2, `VIM` §3.1 |
| $\lambda(x) \ge 0$ | Karush–Kuhn–Tucker (KKT) / Lagrange multiplier field enforcing $i(x) \le c \cdot \mathcal{A}_\partial(x)$ | `VIM` §3.1–3.2 (dualized) |
| $E^s_x \oplus E^u_x$, $\kappa(U)$, $h_{\rm KS}$ | Stable ($\lambda_i < 0$) and unstable ($\lambda_i \ge 0$) tangent subspaces; transverse contraction and KS entropy rate | `LAF` §4.2 D7, §5.2 D11, §10 D19 |
| $\mathrm{sLSE}_T$ | Padding-invariant shifted LogSumExp operator for non-diluting ensemble aggregation | `Spectral_V4` §5.4 (Theorem 5.2) |

---

## 1. Microscopic Kinematics: The Causal-Phase Matrix and the Radiative Scaffold

### 1.1. Matrix Representation of Causal Sets with $U(1)$ Transport

Let $X = \{x_1, x_2, \dots, x_N\}$ be a finite subset of a locally finite causal set $\mathcal{C} = (X, \prec)$ in a topological ordering ($x_i \prec x_j \implies i < j$). The combined causal and electromagnetic microstructure is completely specified by a single nilpotent $N \times N$ complex **causal-phase transfer matrix** $W$:

$$
W_{xy} = r_{xy} \, U_{xy} = r_{xy} \, e^{i q a_{xy}}, \qquad r_{xy} = \begin{cases} 1, & \text{if } x \prec_* y \;\; (I(x,y) = \emptyset), \\ 0, & \text{otherwise.} \end{cases}
$$

Here $x \prec_* y$ denotes an irreducible causal link (an edge in the Hasse diagram of $\mathcal{C}$). Because $\prec$ is acyclic, $W$ is strictly upper-triangular ($W^N = 0$).

1. **Multi-step causal paths:** The matrix power $(W^k)_{xy}$ sums the parallel-transported $U(1)$ phases over all directed causal chains $\gamma = (x = z_0 \prec_* z_1 \prec_* \dots \prec_* z_k = y)$ of combinatorial length $k$:
   $$
   (W^k)_{xy} = \sum_{\gamma \in \Gamma_k(x,y)} \prod_{m=0}^{k-1} U_{z_m z_{m+1}}.
   $$
2. **Causal resolvent (Green's function):** For a coupling parameter $\zeta \in (0, 1)$, the resolvent
   $$
   \mathcal{G}(\zeta) = (I - \zeta W)^{-1} = \sum_{k=0}^{N-1} \zeta^k W^k
   $$
   propagates phase information across the entire causal future.
3. **Gauge curvature from path non-commutativity:** For any minimal 2-step causal diamond $D(x,y)$ formed by two distinct intermediate vertices $z_1, z_2 \in I(x,y)$ (so that $\gamma_1 = (x \prec_* z_1 \prec_* y)$ and $\gamma_2 = (x \prec_* z_2 \prec_* y)$), the gauge-invariant plaquette observable is the normalized interference term:
   $$
   \mathrm{Re}\, W_D(z_1, z_2) = \mathrm{Re}\bigl(W_{x z_1} W_{z_1 y} \, W_{z_2 y}^* W_{x z_2}^*\bigr) = \cos(\Phi_D),
   $$
   which reduces in the continuum limit to $1 - \frac{1}{2}\Phi_D^2 \propto F_{\mu\nu}F^{\mu\nu}$.

### 1.2. Structural Distinction Between Radiation and Massive Matter

A central question of the research program is how massless radiation differs structurally from massive matter while serving as the scaffold for spacetime geometry. Within the matrix causal-phase kinematics, this distinction is exact and requires no fifth dimension:

**Definition 1.1 (Radiative Scaffold vs. Timelike Condensation).**
1. **Null (Lightlike) Channels:** An irreducible link $x \prec_* y$ satisfies $I(x,y) = \emptyset$. Its discrete volume is zero ($V(x,y) = 0$) and its combinatorial length is minimal ($\vert{}\gamma\vert{} = 1$). In the continuum limit, irreducible links generate null geodesics ($ds^2 = g_{\mu\nu}dx^\mu dx^\nu = 0$). Light is a coherent excitation of the link phases $U_{xy}$ propagating directly along $\mathrm{Link}(\mathcal{C})$. Because $I(x,y) = \emptyset$, the emitter $x$ and absorber $y$ are directly connected in the Hasse graph without intermediate causal scattering, explaining why radiation is locally isotropic in ensemble distribution yet maintains direct emitter–observer phase identifiability.
2. **Timelike (Massive) Worldlines:** A pair of events $x \prec y$ with a dense causal diamond $|I(x,y)| \gg 1$ and maximal chain length $L_{\max}(x,y) = \max_{\gamma} |\gamma| \gg 1$ generates positive proper time $\tau(x,y) = \tau_* L_{\max}(x,y) > 0$ and positive four-volume $V(x,y) = v_* |I(x,y)| > 0$. Massive matter is a **localized cluster of high-in-degree / high-out-degree causal vertices** where phase excitations undergo repeated zig-zag scattering across dense sub-graphs of links.

### 1.3. Kernel-Path Quotient Interpretation (`Spectral_V4` Alignment)

Let $\pi_\ell : (\mathcal{C}, W) \to (M_4, g_{\mu\nu})$ be the coarse-graining map that forgets microscopic phase configurations and outputs the macroscopic Lorentzian metric $g_{\mu\nu}$ at scale $\ell$. By Proposition 1.2 of *Spectral and Matrix Realization of $V_4$*, paths tangent to the kernel distribution $K = \ker(d\pi_\ell)$ preserve the coarse metric descriptor.

- Pure $U(1)$ gauge transformations $U_{xy} \to e^{i\chi_x} U_{xy} e^{-i\chi_y}$ lie strictly inside $\ker(d\pi_\ell)$ (`OMIT_REDUNDANT`).
- Displacement along a single unobstructed null link $x \prec_* y$ contributes $ds^2 = 0$ to the Lorentzian interval; metric clock ticks are accumulated only when null links intersect timelike vertex clusters ($u^\mu k_\mu \neq 0$). Thus, the radiative network $\mathrm{Link}(\mathcal{C})$ forms the **inter-class transport edges** of the quotient graph $\mathcal{G}_\ell = D_\ell / \sim_{K,\ell}$, while massive states correspond to persistent equivalence classes (attractor basins) of dense causal diamonds.

---

## 2. The Constraint Triad on the Graph and the Conservation of Distinction Budget

### 2.1. The Local Bekenstein–Casini Bound

Consider a causal diamond $D(p,q)$ with waist (maximal spatial antichain) $\Sigma_\partial \subset D(p,q)$ crossed by $N_\partial$ causal links. Let $\rho_{\rm dyn}$ be the reference thermal/vacuum Gibbs measure of the microscopic Wilson action $S_{U(1)}[W] = \beta \sum_D (1 - \mathrm{Re}\, W_D)$, and let $\sigma$ be the actual local probability measure over gauge-invariant phase configurations in $D(p,q)$.

Following the Dorau–Much and Casini framework adopted in $H_P$, the relative entropy (Kullback–Leibler divergence on gauge-invariant observables) across the diamond waist is bounded by the discrete boundary capacity:

$$
D_{\rm KL}\bigl(\sigma_D \,\|\, \rho_{\rm dyn, D}\bigr) \le c \cdot N_\partial.
$$

In the linear semi-classical regime ($D_{\rm KL} \ll c \cdot N_\partial$), variation of $D_{\rm KL}$ with respect to the state reproduces the modular Hamiltonian flux $\Delta \langle K \rangle = \delta Q / T$, which via the Raychaudhuri equation yields the standard Einstein–Maxwell system $\Gamma_0[g, A]$.

### 2.2. Global Rate Bound and the Tangent-Space Dichotomy (`LAF` Alignment)

Why does local gravitational condensation induce global cosmological expansion? The missing link in earlier versions of $H_P$ was that $N_\partial$ was treated on a fixed lattice where vertex density could not redistribute.

In *The Algorithm of Being* (§3.2), physical dynamics is governed by the **Constraint Triad**: every distinction requires action ($\hbar$), erasing/Maintaining a constraint costs energy ($k_B T \ln 2$), and the rate of generating orthogonal distinctions in a finite region of mean energy $E$ is strictly capped by the Margolus–Levitin bound:

$$
\nu_{\rm dist} = \frac{dN_{\rm vert}}{dt} \le \frac{2E}{\pi \hbar}.
$$

In *Latent Agency Framework* (LAF §4.2 D7, §10 D19), the evolution of a bounded dynamical system on a state space of dimension $N$ splits by Oseledets' multiplicative ergodic theorem into a contracting (stable) subspace $E^s$ ($\lambda_i < 0$) and an expanding/neutral subspace $E^u$ ($\lambda_i \ge 0$), with cumulative Lyapunov distribution $F(s)$:

$$
\underbrace{\kappa(U) = -\int_{-\infty}^{0} s\, F'(s)\, ds}_{\text{Local transverse contraction (Attractor stiffness)}} \quad \text{vs.} \quad \underbrace{\frac{h_{\rm KS}}{N} = \int_{0}^{\infty} s\, F'(s)\, ds}_{\text{Global trajectory divergence (Volume expansion)}}.
$$

For a causal-phase graph evolving under a **fixed global rate of vertex/link generation** (fixed total distinction budget per operational step, $\sum_{i=1}^N \lambda_i = \mathrm{const}$ or $\sum_{x \in X} \mathrm{deg}(x) = N_{\rm links}$):

1. **Local Condensation ($E^s$):** Forming a bound massive structure or a coherent high-flux field configuration ($F_{\mu\nu}F^{\mu\nu} \gg 0$) requires concentrating causal vertices $|I(x,y)|$ and links into a localized region $U$ so that $N_{\partial}(U)$ is large enough to satisfy $D_{\rm KL}(U) \le c \cdot N_\partial(U)$. Dynamically, this corresponds to strong transverse contraction $\kappa(U) > 0$ ($\lambda_i < 0$ in $E^s$), pulling causal paths inward.
2. **Global Decompression ($E^u$):** Because the total rate of causal event generation $\sum_x v_*$ per unit null phase advance is bounded by the global distinction budget, **sequestering vertices into high-density local attractors ($E^s$) necessarily depletes the density of intermediate timelike vertices $|I(x,y)|$ along the long-range null links spanning the complementary cosmic voids ($E^u$)**.

### 2.3. How Vertex Depletion Produces Apparent Metric Expansion (Dark Energy)

Consider an emitter $x$ and a cosmological observer $y$ separated by a void region $V_{\rm void}$.
- The observer measures frequency and time intervals by comparing the null phase clock of the $U(1)$ connection against their local baryonic (timelike) clock (`Algorithm` §3.3):
  $$1 + z = \frac{(-u^\mu k_\mu)_{\rm em}}{(-u^\mu k_\mu)_{\rm obs}}.$$
- Along the null rays crossing the void, phase transport $U(\gamma)$ occurs over long chains of sparse links where intermediate scattering vertices $\vert{}I(x,y)\vert{}$ have been depleted to feed the growing local condensations (galaxies, filaments, black holes).
- In the continuum reconstruction $(\mathcal{C}, W) \to (M_4, g_{\mu\nu})$, the metric volume element is proportional to the local vertex density: $\sqrt{-g_{\rm micro}} \propto \rho_{\rm vert}(x)$. However, in standard general relativity, the observer normalizes local rulers to fixed baryon Compton wavelengths ($m_p = \mathrm{const}$ inside the condensed attractors). Relative to these fixed local rulers, a decrease in background vertex density $\rho_{\rm vert}^{\rm void}(t)$ along the radiative scaffold is conformally equivalent to an **increase in the macroscopic scale factor $a(t) \propto (\rho_{\rm vert}^{\rm void})^{-1/3}$**, i.e., a positive Kolmogorov–Sinai expansion rate $h_{\rm KS} > 0$ in the void sector.

**Core Structural Thesis:**
> *Quantum gravity is not an attractive short-range force mediated by independent spin-2 particles on a fixed background. Short-range attraction is ordinary entropic focus along $\nabla D_{\rm KL}$. The specifically quantum-gravitational effect is the global conservation of the causal distinction budget: local informational condensation ($\kappa(U) > 0$ in $E^s$) directly drives the global metric decompression of the radiative scaffold ($h_{\rm KS} > 0$ in $E^u$), which macroscopic cosmology parameterizes as Dark Energy.*

---

## 3. Variational Derivation of the Correlation Functional $\Gamma_{\rm corr}$

We now translate the mechanism of Section 2 into a continuum variational principle by directly adapting the mathematics of *The Law of Useful Information Structuring in Model Latent Spaces* (`VIM` §2–3).

### 3.1. Constrained Action Functional

Let $M_4$ be covered by a locally finite family of causal diamonds $\{D_x\}_{x \in M_4}$ of characteristic coarse-graining scale $\ell$. At each point $x$, let:
- $i(x) := \ell^{-4} D_{\rm KL}\bigl(\sigma_{D_x}[g, A, \Psi] \,\Vert{}\, \rho_{\rm dyn}\bigr)$ be the coarse-grained relative-entropy density of the phase/matter fields above the dynamical vacuum;
- $\mathcal{B}_{\max}(x) := c \, \ell^{-4} N_\partial(D_x) = \frac{c}{\ell^2 \ell_{\rm Pl}^2} \mathcal{A}_\partial(x)$ be the local Bekenstein–Casini capacity density determined by the transverse horizon area $\mathcal{A}_\partial(x)$ of the causal diamond;
- $\rho_{\rm vert}(x) = n(x) \sqrt{-g}$ be the dimensionless causal vertex density relative to the continuum reference volume, subject to the global (horizon-scale) budget conservation constraint:
  $$\int_{\Omega_H} d^4x \sqrt{-g} \, \bigl(\rho_{\rm vert}(x) - \bar{\rho}_0\bigr) = 0.$$

The total effective action under hypothesis $H_P$ is the constrained variational functional:

$$\Gamma_P[g, A, \Psi, \lambda, \Lambda_0] = \Gamma_0[g, A, \Psi] - \int d^4x \sqrt{-g} \, \lambda(x) \Bigl[ i(x) - \mathcal{B}_{\max}(x; \rho_{\rm vert}) \Bigr]_+ - \Lambda_0 \int d^4x \sqrt{-g} \, \bigl(\rho_{\rm vert}(x) - \bar{\rho}_0\bigr),$$

where $\Gamma_0$ is the standard Einstein–Maxwell–matter action, $\lambda(x) \ge 0$ is the local Karush–Kuhn–Tucker (KKT) multiplier field that activates wherever the informational bound approaches saturation, and $\Lambda_0$ is the global budget multiplier.

Therefore, the correlation functional $\Gamma_{\rm corr}$ sought in `Causal_Phase_Geometry` v1 (§5) is explicitly identified as:

$$\boxed{ \Gamma_{\rm corr}[g, A, \Psi] = -\int d^4x \sqrt{-g} \left\{ \lambda(x) \Bigl[ i(x) - \mathcal{B}_{\max}(x) \Bigr]_+ + \Lambda_{\rm budget}(x) \right\} }$$

### 3.2. Stationary Equations and the Two Regimes of $H_{\mu\nu}^{\rm corr}$

Varying $\Gamma_P$ with respect to the inverse metric $g^{\mu\nu}$ yields the modified Einstein equations:

$$G_{\mu\nu} = \frac{8\pi G}{c^4} \Bigl( T_{\mu\nu}^{\rm matter} + T_{\mu\nu}^{\rm EM} + H_{\mu\nu}^{\rm corr} \Bigr), \qquad H_{\mu\nu}^{\rm corr} := -\frac{2}{\sqrt{-g}} \frac{\delta \Gamma_{\rm corr}}{\delta g^{\mu\nu}}.$$

Evaluating the variation of $\Gamma_{\rm corr}$ produces two distinct geometric terms corresponding to the boundary and the bulk of saturated regions:

#### Regime I: Galactic Halos and Black-Hole Scaling (The VIM Minimal-Surface Term)
Consider the boundary zone $\Sigma_{\rm sat}$ surrounding a baryonic condensation (e.g., a galactic disk or a black hole) where $i(x)$ transitions from the saturated core ($i \approx \mathcal{B}_{\max}$) to the unsaturated exterior ($i \ll \mathcal{B}_{\max}$). 

Exactly as in `VIM` §3.2 (where minimizing embedded surface volume $\mathrm{Vol}(\Sigma)$ under an information constraint yields $\mathbf{H}(z) = \lambda (\nabla i)^\perp$), varying the diamond boundary area $\mathcal{A}_\partial(x)$ with respect to the ambient metric $g^{\mu\nu}$ across the iso-information hypersurfaces $\Sigma_i = \{x : i(x) = \mathrm{const}\}$ yields the **mean-curvature vector** $\mathbf{H}^\alpha = K \, n^\alpha$ (where $n^\alpha = \nabla^\alpha i / \vert{}\nabla i\vert{}$ is the unit normal to the iso-information surface and $K = \nabla_\alpha n^\alpha$ is its extrinsic trace curvature):

$$\bigl(H_{\mu\nu}^{\rm corr}\bigr)_{\rm local} = \lambda(x) \, c_{\rm area} \left( K_{\mu\nu} - K \, h_{\mu\nu} \right) + \bigl(n_\mu \nabla_\nu + n_\nu \nabla_\mu\bigr)\bigl(\lambda(x)\, i(x)\bigr),$$

where $h_{\mu\nu} = g_{\mu\nu} - n_\mu n_\nu$ is the induced metric on the constant-$D_{\rm KL}$ shell.

**Physical consequences of Regime I:**
1. **Flat Rotation Curves ($1/r$ radial force):** For a quasi-spherical or axisymmetric baryonic distribution of mass $M_B$ at radius $r$ where the radiative/phase flux decays as $i(r) \propto M_B / r^2$, the extrinsic mean curvature of the nested causal shells is $K(r) = 2/r$. In the saturation transition zone where $\lambda(r)$ is locked to the critical slope, the trace of the surface-tension stress tensor generates an effective radial acceleration:
   $$a_{\rm corr}(r) \sim c^2 \lambda_{\rm crit} K(r) = \frac{v_\infty^2}{r}, \qquad v_\infty^4 \propto G M_B c^2 \Lambda_{\rm budget}^{1/2} \equiv G M_B a_0.$$
   This reproduces the Baryonic Tully–Fisher Relation (BTFR) and the Radial Acceleration Relation (RAR) in SPARC galaxies **as an informational surface-tension effect of the causal graph**, without dark-matter particles.
2. **Black Hole – Halo Coupling (The Triad Closure):** A supermassive black hole (SMBH) is a region where the causal diamond bound is maximally saturated ($i(x) = \mathcal{B}_{\max}$ on the event horizon, $N_\partial = A_H / (4\ell_{\rm Pl}^2)$). Because the KKT field $\lambda(x)$ is anchored at its maximum boundary value on the horizon $\partial B_{\rm BH}$ and relaxes outward across the host galaxy's causal waist, the integrated halo surface tension $\int H_{00}^{\rm corr} d^3x$ is topologically tied to the horizon boundary condition $N_{\partial, {\rm BH}}$, providing a direct structural mechanism for $M_{\rm BH}$–$M_{\rm halo}$ co-scaling.

#### Regime II: Cosmic Voids and Late-Time Acceleration (The Budget Depletion Term)
In cosmic voids ($V_{\rm void}$) far from baryonic condensations, $i(x) \to 0$ and the local KKT multiplier vanishes ($\lambda(x) = 0$). However, the global budget conservation term in $\Gamma_{\rm corr}$ remains active. Let $f_{\rm cond}(z)$ be the fraction of the cosmic causal-vertex budget sequestered into saturated local structures ($i \approx \mathcal{B}_{\max}$, $\lambda_i < 0$ in $E^s$) at redshift $z$. By budget conservation, the background vertex density in voids is reduced by $\Delta \rho_{\rm vert}^{\rm void}(z) \propto -f_{\rm cond}(z)$, inducing a pure metric-trace term:

$$\bigl(H_{\mu\nu}^{\rm corr}\bigr)_{\rm global} = -\rho_{\rm DE}^{\rm eff}(z) \, g_{\mu\nu}, \qquad \rho_{\rm DE}^{\rm eff}(z) = \Lambda_0 \, \bar{\rho}_0 + \gamma_{\rm cpl} \int_{\Omega_H} \frac{d^3x'}{V_H} \, \lambda(x', z) \, i(x', z).$$

**Physical consequences of Regime II:**
1. **Direct Coupling of Local Structure Growth and Global Expansion:** Unlike a static cosmological constant $\Lambda$, $\rho_{\rm DE}^{\rm eff}(z)$ is directly driven by the volume integral of saturated local structures $\langle \lambda \cdot i \rangle_{\Omega_H}$. As structure formation accelerates at late cosmic times ($z \lesssim 2$), more causal links are pulled into high-contraction local attractors ($\kappa(U) > 0$), increasing the void vertex deficit and driving the effective equation of state toward $w_{\rm eff}(z) \to -1$ (or weak dynamical dark energy $w_0, w_a$ testable by DESI/DES-SN5YR).
2. **Irreducibility Criterion Satisfied:** Both Regime I (galactic surface tension) and Regime II (cosmological void expansion) depend on the **same underlying coupling $c$ (the threshold $B = c \cdot N_\partial$) and the same KKT functional $\lambda[i]$**. No independent dark-matter and dark-energy fields or separate free parameters exist.

---

## 4. Non-Diluting Aggregation of Graph Constraints via $\mathrm{sLSE}_T$

In numerical lattice or graph implementations (such as Stage v0.1 and the new dynamic Stage v0.2), computing the global effective action penalty from local diamond violations $v_m = [i(D_m) - c N_\partial(D_m)]_+$ across $M \gg 1$ causal diamonds encounters the exact mathematical pathology identified and solved in *Spectral and Matrix Realization of $V_4$* (§5.4, Theorem 5.2):

- **Defect of linear summation or plain LogSumExp:** Summing soft penalties over $M$ vacuum diamonds ($v_m \approx 0$ up to thermal noise) accumulates a spurious volume divergence $O(T \log M)$ that masks localized topological signals.
- **Defect of LogMeanExp:** Averaging $\frac{1}{M}\sum_m v_m$ dilutes a genuine localized Bekenstein saturation ($v_{m_*} > 0$) by $1/M$ as the total graph size grows.

To eliminate both defects, the normalized saturation degree $q_m = \tanh\bigl([i(D_m) - c N_\partial(D_m)]_+ / B_0\bigr) \in [0, 1]$ across a collection of $M$ causal sub-diamonds is aggregated using the **padding-invariant shifted LogSumExp operator** ($\mathrm{sLSE}_T$):

$$\mathcal{Q}_T\bigl(q_1, \dots, q_M\bigr) := \min\left\{ 1, \; T \log\left( 1 + \sum_{m=1}^{M} \bigl(e^{q_m / T} - 1\bigr) \right) \right\}.$$

By Theorem 5.2 of `Spectral_V4`:
1. **Vacuum Inertness (Padding Invariance):** Any unsaturated diamond in the void with $q_m = 0$ contributes $e^0 - 1 = 0$ to the sum. Expanding the ambient void volume ($M \to \infty$ by adding vacuum diamonds) produces **zero** parasitic shift in $\mathcal{Q}_T$.
2. **Non-Dilution of Saturation:** A single black-hole or galactic core diamond reaching $q_{m_*} = 1$ forces $\mathcal{Q}_T = 1$ at every temperature $T > 0$, independent of $M$.

---

## 5. Falsification Criteria and Status Assessment ($V_4$ Standard)

### 5.1. Explicit Falsification Conditions

The extended hypothesis $H_P$ (v2.0) must be rejected (assigned status `NULL`) if any of the following holds:

1. **Failure of Dynamic Graph Redistribution (Stage v0.2):** On a causal-phase graph with fixed total vertex/link budget, introducing a localized gauge-invariant $U(1)$ flux source $\kappa$ under the truncation penalty $D_{\rm KL} \le c N_\partial$ fails to produce a statistically significant drop in background vertex density $\rho_{\rm vert}^{\rm void}$ (or increase in effective shortest-path distance) in the surrounding unsaturated region.
2. **Irreducible Galactic vs. Cosmological Parameters:** Fitting SPARC rotation curves via the surface-tension term $(\mathbf{H} = \lambda \nabla^\perp i)$ and fitting $H(z)$ / DESI BAO via the budget-depletion term require incompatible values of the fundamental capacity threshold $c$.
3. **Breakdown of Null Redshift Scaling:** The graph's radiative scaffold fails to reproduce the exact cosmological time-dilation relation $\Delta t_{\rm obs} = (1+z)\Delta t_{\rm em}$ in supernova light curves (DES-SN5YR).
4. **Local Equivalence Violations:** Because the 5D radion ($H_R$) remains strictly abandoned ($\delta \ell_* = 0$), any detection of scalar fifth-force effects inside saturated high-density solar-system environments where $\nabla i \to 0$ would falsify the screening mechanism of the KKT multiplier $\lambda(x)$.

### 5.2. Self-Assessment Table (`FOLLOW` / `OMIT` / `NULL` / `UNDECIDED`)

| Claim / Component | Verdict | Justification |
| :--- | :--- | :--- |
| 5D Kaluza–Klein radion branch ($H_R$) and heuristic fluid equations of state ($w \in \{1, 1/3, -1/3, -1\}$) | **NULL** | Frozen in August 2026; conflicts with MICROSCOPE and lacks microscopic derivation |
| AdS/CFT as a foundational derivation of 4D FLRW dark energy | **OMIT** | Inessential / inapplicable to positive-expansion causal graphs without an AdS boundary |
| Isomorphism between a finite causal set with $U(1)$ link phases and a nilpotent transfer matrix $W_{xy} = r_{xy}e^{i\theta_{xy}}$ | **FOLLOW** (formal) | Exact algebraic identity for finite acyclic directed graphs (§1.1) |
| Irreducible causal links ($I(x,y)=\emptyset$) have zero discrete 4-volume and minimal path length, whereas dense diamonds ($\vert{}I(x,y)\vert{}\gg 1$) generate proper time and volume | **FOLLOW** (formal) | Standard causal-set kinematics (`KK_Jacobson` §2.1) |
| Variation of an area-bounded information functional $\mathrm{Area}(\partial D) - \lambda D_{\rm KL}$ yields the mean-curvature balance $\mathbf{H} = \lambda (\nabla i)^\perp$ | **FOLLOW** (formal) | Proven in `VIM` §3.2 (Calculus of Variations) |
| Padding-invariant $\mathrm{sLSE}_T$ eliminates vacuum volume noise while preserving localized saturation signals | **FOLLOW** (formal) | Proven in `Spectral_V4` §5.4 (Theorem 5.2) |
| Under a conserved total causal vertex/link budget, increasing local subgraph density to satisfy $D_{\rm KL} \le c N_\partial$ reduces vertex density in the complementary subgraph | **FOLLOW** (formal) | Elementary conservation law on finite graphs; dynamical magnitude is tested in v0.2 |
| The surface-tension term $\lambda K_{\mu\nu}$ quantitatively reproduces the SPARC Radial Acceleration Relation ($a_0 \sim c H_0$) without free halo parameters | **UNDECIDED** | Empirical hypothesis; requires extracting $\lambda(r)$ from Stage v0.2 and testing on SPARC |
| Void vertex depletion quantitatively reproduces late-time cosmological acceleration $H(z)$ (DESI / DES-SN5YR) | **UNDECIDED** | Empirical hypothesis; requires continuum limit of the v0.2 budget-depletion curve |

---

## References

1. V. Yakunin, *The Algorithm of Being: Informational Ontology, Constraint, and the Self-Structuring Code* (2026).
2. V. Yakunin, *Causal-Phase Geometry Research Program (v1.0)* and *Technical Specification v0.1.1* (August 2026).
3. V. Yakunin, *The Law of Useful Information Structuring in Model Latent Spaces (Theory of Informational Minimal Surfaces, VIM v1.0)* (September 2026).
4. V. Yakunin, *Modified Brusentsov Entailment Logic and Four-Valued Verdict Calculus for External State-Control Systems* (2026).
5. V. Yakunin, *Latent Agency Framework (LAF v2.0)* (October 15, 2026).
6. V. Yakunin, *Spectral and Matrix Realization of $V_4$ in Latent Spaces (v2.2)* (October 17, 2026).
7. P. Dorau, A. Much, "From Quantum Relative Entropy to the Semiclassical Einstein Equations," *Physical Review Letters* (2026); arXiv:2510.24491.
8. H. Casini, "Relative Entropy and the Bekenstein Bound," *Classical and Quantum Gravity* 25, 205021 (2008).
9. L. Bombelli, J. Lee, D. Meyer, R. D. Sorkin, "Space-Time as a Causal Set," *Physical Review Letters* 59, 521–524 (1987).
10. N. Margolus, L. B. Levitin, "The Maximum Speed of Dynamical Evolution," *Physica D* 120, 188–195 (1998).
