# Unified Informational-Constructive Framework

## Version 1.7

**Author:** Vladimir Yakunin

**Date:** 2026-10-17 (v1.7 revision; v1.6: 2026-10-17; v1.5: 2026-10-14; v1.4: 2026-10-13; v1.3: 2026-10-05; v1.2: 2026-09-23)

**Status:** archive synthesis document; aligned with the revised edition of "The Algorithm of Being" (2026), Causal-Phase Geometry Research Program v2.0 (October 2026; matrix kinematics, budget-constrained dual origin of dark-sector effects), Technical Specification v0.2 (consolidated pilot: frozen + dynamic-budget graph), the geometric theory of latent representations (September 2026), the ARC-AGI-3 LCLD Agent specifications V10.9 (October 2026), the Latent Agency Framework v2.0 (October 2026), the Self-Developing Runtime Research Program v0.2 (September 2026), the canonical Modified Brusentsov Entailment Logic specification (October 2026), the Spectral and Matrix Realization of V₄ in Latent Spaces (October 2026), and the preliminary ternary-judge MVP results (August 2026)

## 1. Central Thesis

Reality, consciousness, and artificial intelligence are not separate domains but different scales of one and the same process: **self-structuring under constraint**. At every level the same architecture recurs — but not on an abstract "substrate-indifferent" carrier; it runs on a material substrate with its own **constraint envelope** (power, distinction rate, noise, persistence) that parameterizes viable architectures.

| Level | Substrate | What happens |
|---|---|---|
| Physical | Causal network + U(1) holonomies | Spacetime and field emerge as stable regimes of constrained dynamics |
| Ontological | Recursive semantic structures on a biological envelope | Consciousness is a self-model certified by the world through action |
| Engineering | Neuro-symbolic agent on an artificial envelope | A rational agent separates hypothesis generation, selection, and fact fixation |

---

## 2. Basic Definitions

### 2.1. Information as constraint

**Information** is not data but a narrowing of the space of admissible states:

$$\Omega \to \Omega' \subset \Omega$$

Without constraint, energy dissipates into entropy. With constraint, it forms stable structure. If energy is the capacity for transformation, information is the geometry of admissible transformation.

### 2.2. The constraint triad: distinction, action, rate

Information is not the only fundamental constraint. Three physical results bind information and energy so tightly that neither can serve as the sole primitive:

1. **Erasure has a price.** By Landauer, erasing one bit at temperature $T$ dissipates at least $k_B T \ln 2$ [12]. Forgetting, compression, and filtering the irrelevant are paid thermodynamic operations.
2. **The rate of distinctions is bounded by energy.** The Margolus–Levitin theorem: a system with mean energy $E$ traverses at most $2E/\pi\hbar$ orthogonal states per second [13]; the Mandelstam–Tamm bound: $\Delta t \geq \pi\hbar/(2\Delta E)$ [14].
3. **Information capacity is bounded by energy and size** (the Bekenstein bound) [15].

The fundamental quantities: **distinction** (the bit), **action** ($E \cdot t$, quantum $\hbar$), **causal rate** (the limit $c$). Physics' three conversion constants correspond to the triad's three edges: $c$ — space↔time, $\hbar$ — energy↔frequency ($E = \hbar\omega$), $k_B$ — entropy↔energy.

### 2.3. Time: rate, not axis

The archive's physics program admits no external global time: proper time is defined along worldlines, and in discrete kinematics is estimated by maximal-chain length [6, 7]. Only **ratios of rates** are observable. The general redshift formula is literally a comparison of two clocks (null-transported phase against the local time directions of emitter and observer):

$$1+z = \frac{(-u^\mu k_\mu)_{\rm em}}{(-u^\mu k_\mu)_{\rm obs}}$$

An algebraic echo of the same thesis is the Connes–Rovelli thermal time hypothesis [24]: a state on an algebra generates its own time evolution through the modular flow. **The operational content of time is a ratio of rates; the time axis is a derived bookkeeping tool.**

### 2.4. Operational time

The density of distinctions a system can generate and integrate is paid out of its energy envelope. An honest schema, anchored in Margolus–Levitin:

$$d\mathcal{T} \propto \frac{\hbar \, dN}{E} \cdot \eta(M)$$

where $dN$ is the number of orthogonal distinctions generated, $E$ the mean energy, and $\eta(M)$ the architecture's efficiency (the fraction of the physical rate limit actually achieved). The bound is physics; the architectural factor is a schema.

### 2.5. Ternary semantics

Any judgment about a system state takes one of three values:

- **REQUIRED** — the state is necessary for the current task (progress, success).
- **FORBIDDEN** — the state is excluded by constraints (contradiction, impossibility).
- **IRRELEVANT** — the state is admissible but semantically invariant (no-op, noise).

To these is added the epistemic category **UNRESOLVED** — insufficient data for classification. In the judge for LLM reasoning [9], the same discipline takes the form of verdicts FOLLOW / OMIT / NULL / UNDECIDED. The canonical formalization is fixed by the Modified Brusentsov Entailment Logic specification [26]: the ontological triad FOLLOW (+1) / OMIT (0) / NULL (−1) — operational aliases REQUIRED / IRRELEVANT / FORBIDDEN — is ordered by the strict dominance chain NULL ≻ UNDECIDED ≻ OMIT ≻ FOLLOW, while epistemic insufficiency is isolated as the control signal UNDECIDED (alias UNRESOLVED), never as a fourth truth value. OMIT certifies admissible inessentiality of a move in one of three disjoint forms: blocked applicability (OMIT_BLOCKED), semantic invariance (OMIT_REDUNDANT), or a resolved incidental / sub-threshold change (OMIT_INCIDENTAL).

**Important:** `IRRELEVANT` is neither "false" nor "unknown." It is an explicitly recorded absence of relevance, allowing the system to compress its attention space.

### 2.6. The Algorithm of Being (short form)

Distinction → Constraint → Balance → Compression → Meaning → Modeling → Certification → Self-Correction

Or shorter still:

Relation → Constraint → Structure → Semantics → Intelligence

---

## 3. The Physical Level: Causal Phase Geometry (Hypothesis (H_P))

### 3.1. The three-layer stack of the program

The archive's physics works with an explicit stack, not a single "foundation":

| Layer | Object | Status |
|---|---|---|
| Level 0 — algebraic substrate | "Space of Algebras" (the Connes lineage: Gelfand duality, spectral triples, thermal time [22–24]) | Conjecture; regulative idea; formalization deferred |
| Level 1 — causal-phase network | Discrete causal order with U(1) holonomies, represented as a strictly upper-triangular causal-phase transfer matrix $W_{xy}=r_{xy}e^{i\theta_{xy}}$; continuum limits under hypothesis (H_P) | Active program with falsification criteria; pilot numerics v0.2 |
| Level 2 — continuum geometry | Lorentzian metric, gauge connection, effective equations from relative entropy; explicit $\Gamma_{\rm corr}$ with dual regimes | Established structures + open quantitative extraction of residual $H_{\mu\nu}^{\rm corr}$ |

The "Space of Algebras" is not a claimed foundation but a deep conjectural layer whose fate is tied to the intermediate one: failure of the causal-phase program by its own criteria demotes the conjecture to a historical footnote.

### 3.2. Fundamental kinematics (hypothesis (H_P))

The base structure is a locally finite causal set $(\mathcal{C},\prec)$ equipped with U(1) holonomies on oriented links, encoded as a single nilpotent complex **causal-phase transfer matrix**:

$$W_{xy}=r_{xy}\,e^{i\theta_{xy}},\qquad r_{xy}\in\{0,1\},\quad\theta_{xy}\in[0,2\pi).$$

Irreducible links ($I(x,y)=\emptyset$) form the null (lightlike) radiative scaffold; massive matter corresponds to dense clusters of multi-step causal chains ($|I(x,y)|\gg 1$) that accumulate proper time and discrete volume. Coarse-graining yields continuum geometry:

$$(\mathcal{C},\prec,W)\xrightarrow{\pi_\ell}(\mathcal{M}_4,g_{\mu\nu},A_\mu).$$

- The causal order fixes the light cones and the conformal class of the metric.
- The volume measure (element count in an interval) fixes the proper-time scale.
- Discrete U(1) transports generate the electromagnetic connection; gauge curvature arises from path non-commutativity on minimal diamonds.

The phase layer is treated strictly as an **internal** fibre:

$$U(1)\hookrightarrow P\xrightarrow{\pi}M_4,\quad\delta\ell_*=0.$$

No free radion, no physical fifth dimension, no KK tower. The competing physical-radion branch (H_R) has been frozen (August 2026). Full matrix kinematics, radiative-scaffold vs. timelike-condensation distinction, and kernel-path quotient alignment are given in **Causal-Phase Geometry Research Program v2.0**.

### 3.3. Relative-entropy origin of gravity and the constraint triad

Macroscopic gravity is obtained from quantum-information principles (Dorau–Much approach [25]): the role of heat flux is played by the quantum relative entropy (Araki–Uhlmann) evaluated on a horizon. The Casini link between the Bekenstein bound and the non-negativity of relative entropy supplies the informational constraint that, after coarse-graining, yields the semi-classical Einstein equation.

A classical Kullback–Leibler proxy on gauge-invariant boundary descriptors is used in the pilot numerical stage; it is **not** claimed to be the full modular relative entropy.

The local Bekenstein–Casini bound on a causal diamond reads

$$D_{\rm KL}(\sigma_D\|\rho_{\rm dyn,D})\le c\cdot N_\partial.$$

Globally, under a conserved causal-distinction rate (Margolus–Levitin), the tangent-space Lyapunov dichotomy of the Latent Agency Framework (stable subspace $E^s$ vs. unstable $E^u$) implies that local condensation necessarily depletes intermediate vertices along long-range null links in complementary voids.

### 3.4. The correlation functional $\Gamma_{\rm corr}$ and the dual origin of dark-sector effects

Under hypothesis (H_P) the effective action is the constrained variational functional

$$\Gamma_P[g,A,\Psi,\lambda,\Lambda_0]=\Gamma_0[g,A,\Psi]-\int d^4x\sqrt{-g}\,\lambda(x)\bigl[i(x)-\mathcal{B}_{\max}(x)\bigr]_+-\Lambda_0\int d^4x\sqrt{-g}\,(\rho_{\rm vert}-\bar\rho_0),$$

so that the residual is identified explicitly as

$$\boxed{\Gamma_{\rm corr}[g,A,\Psi]=-\int d^4x\sqrt{-g}\Bigl\{\lambda(x)\bigl[i(x)-\mathcal{B}_{\max}(x)\bigr]_++\Lambda_{\rm budget}(x)\Bigr\}}.$$

Its geometric response $H_{\mu\nu}^{\rm corr}=-2/\sqrt{-g}\,\delta\Gamma_{\rm corr}/\delta g^{\mu\nu}$ splits into two coupled regimes (Causal-Phase Geometry v2.0):

1. **Regime I (local condensation — effective dark matter).** On the boundary of saturated regions ($\nabla D_{\rm KL}\neq 0$) the Lagrange multiplier induces a normal surface-tension response $\mathbf{H}=\lambda(\nabla i)^\perp$ (VIM minimal-surface balance), reproducing flat galactic rotation curves and black-hole/halo scaling without independent halo fields.
2. **Regime II (global decompression — effective dark energy).** Because the total rate of causal-event generation is bounded, sequestering vertices into high-density local attractors depletes intermediate timelike events along long-range null links spanning cosmic voids. Relative to fixed local (baryonic) rulers this manifests as positive metric volume expansion ($h_{\rm KS}>0$ in $E^u$).

Thus quantum gravity is identified not as a quantization of attractive spin-2 gravitons, but as the global entropic decompression of the causal scaffold driven by local informational condensation. Whether the quantitative residual is measurable and stable is the concrete question of the pilot stage.

### 3.5. Pilot numerical programme (v0.2)

Because Stage v0.1 was not executed prior to the theoretical synthesis of October 2026, the static lattice of v0.1 is retained as the exact $\mathrm{Mobility}=0$ control branch inside a single consolidated software complex. **Technical Specification v0.2** defines:

- **Mode A (`topology_mode="frozen"` — v0.1 baseline):** fixed 3D layered causal lattice; only U(1) phases update. Answers: does informational truncation produce a non-zero residual $\Delta F$ on a fixed background?
- **Mode B (`topology_mode="dynamic_budget"` — v0.2 core test):** both phases and causal links evolve under Metropolis–Hastings rewiring that **strictly conserves** total vertex and link counts $N_V,N_E$ and causal acyclicity. Directly tests whether local $D_{\rm KL}$ saturation forces topological condensation in the core ($\Delta N_\partial>0$) and topological rarefaction / effective metric expansion in the void ($\delta\rho_{\rm void}<0$, $z_{\rm void}^{\rm eff}>0$).

Primary observables, eight mandatory null tests (D1–D8), resource budget, and decision criteria under the $V_4$ verdict standard (FOLLOW / NULL / UNDECIDED) are fixed in the specification. Full continuum 4D reconstruction, SPARC fitting and DESI $H(z)$ contact remain explicitly excluded from v0.2.

Only after a closed report `REPORT_v0.2.md` may the programme proceed to analytical comparison with the VIM surface-tension kernel or to continuum-limit cosmological tests.

---

