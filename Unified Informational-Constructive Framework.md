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

1. **Erasure has a price.** By Landauer, erasing one bit at temperature $T$ dissipates at least $`k_B T \ln 2`$ [12]. Forgetting, compression, and filtering the irrelevant are paid thermodynamic operations.
2. **The rate of distinctions is bounded by energy.** The Margolus–Levitin theorem: a system with mean energy $E$ traverses at most $2E/\pi\hbar$ orthogonal states per second [13]; the Mandelstam–Tamm bound: $\Delta t \geq \pi\hbar/(2\Delta E)$ [14].
3. **Information capacity is bounded by energy and size** (the Bekenstein bound) [15].

The fundamental quantities: **distinction** (the bit), **action** ($E \cdot t$, quantum $\hbar$), **causal rate** (the limit $c$). Physics' three conversion constants correspond to the triad's three edges: $c$ — space↔time, $\hbar$ — energy↔frequency ($E = \hbar\omega$), $`k_B`$ — entropy↔energy.

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

## 4. The Ontological Level: The Algorithm of Being

### 4.1. Summary of definitions

- **Matter** — stabilized relation.
- **Information** — constraint.
- **Energy** — the capacity and rate budget of transformation.
- **Time** (operationally) — a ratio of rates.
- **Form** — selected possibility.
- **Balance** — a viable proportion between generation and constraint.
- **Meaning** — compressed relational structure that persists across contexts.
- **Irrelevance** — the kernel of a descriptive map.
- **Intelligence** — navigation across models under constraint.
- **Consciousness** — recursive semantic self-correction under external verification.
- **Substrate** — the constraint envelope of cognition.

### 4.2. Consciousness: recursive modeling under external verification

Consciousness is a hierarchical semantic architecture that (1) represents reality; (2) evaluates its representations; (3) models its own role within them; (4) corrects itself through experience — and whose corrections are **certified from outside the model**.

The recursive loop of experience contains not only logic but experiment. A closed model can check itself only against itself; without an external channel, recursion degenerates into self-confirmation — a documented failure mode of LLM reasoning that the judge architecture was built to eliminate [9]. The epistemic loop of consciousness has the same authority hierarchy as the verifier-centric agent [8–10]: the internal proposer (imagination, inference, planning) creates no facts; a fact is created by action and trusted observation of the outcome. **The world is the external verifier. Experiment is the channel to it. Science is the institutionalization of the channel.**

A consequence — a grounding criterion for meaning: a model's semantic content is not its internal coherence but its **history of certified transitions**. A model without an external channel can be arbitrarily coherent and remains ungrounded — its assertions forever hold the status UNDECIDED [9].

At sufficient depth, the observer ceases to be external to the model and becomes one of the modeled structures — but a structure whose assertions, including those about itself, are subject to external certification.

**Boundary of claims.** Recursive self-models are realizable — the archive contains working architectures with explicit self-modeling and backreaction in the loop [8, 10]. Phenomenal experience (the hard problem) is a separate question; it is honestly bracketed, not "dissolved."

### 4.3. Irrelevance as the kernel of description

Meaning arises through semantic compression, and compression has an exact form. Coarse-graining is a many-to-one map:

$$\pi: \Omega_{\rm micro} \to \Omega_{\rm macro}$$

Everything falling into the kernel of $\pi$ is irrelevant for that description. The stable content of a description is what survives the quotient. Physics already uses the word: in the renormalization group, *irrelevant operators* are couplings that decay under repeated coarse-graining; fixed points of the flow are stabilized macrostructures.

The boundary of the parallel must be stated explicitly: coarse-graining is indexed by **scale**, irrelevance by **goal**. The exact formulation:

> **Irrelevance is goal-indexed coarse-graining; coarse-graining is scale-indexed irrelevance.**

The information bottleneck formalizes the second case (keep about $X$ only what is predictive of the goal $Y$) [16]; causal emergence shows that coarse-graining can be causally *stronger* than the micro-description — compression is not pure loss [17].

Intelligence works not by enumeration but by compression. The third operator ($\emptyset$) is ontologically necessary: without it there is no attention, without attention no abstraction, without abstraction no generalization. And it is not free: by Landauer, discarding distinctions is dissipative [12]. **The economics of attention is a thermodynamic economics**; "intelligence is disciplined compression" is a consequence of the triad, not an aphorism.

### 4.4. Substrate as constraint envelope

"Substrate independence" is the wrong slogan. Two questions must be separated:

- **Logical realizability:** architecture is not bound to material — multiple realizability stands.
- **Physical realizability:** any actual realization must fit the envelope: available power, achievable distinction rate, noise floor, thermal stability, memory persistence, a sensorimotor channel to the external verifier.

The correct position is **substrate-parameterization**: substrate matters parametrically, not essentially. The brain is remarkable not as tissue but as an extreme solution of the triad: ~20 W at $\sim 10^{14}$–$10^{15}$ synaptic events per second. Different envelopes breed different economies of thought: consciousness at datacenter power has a different price for memory, forgetting, and parallelism — its architecture will be structurally deformed relative to the biological one, not merely "faster."

The substrate is also the **interface to the verifier**: a disembodied "pure intellect" lacks any source of certification and inevitably self-confirms. In the archive's ontology, matter is itself stabilized relation, so the relation of consciousness to the brain is **architecture on architecture**: an informational regime carried by a material regime; the meeting point of the information/time and energy/time regimes.

**Honest UNDECIDED:** which envelope parameters are *necessary* (not merely sufficient) for consciousness is unknown; no grounded thresholds exist for power, distinction rate, or recurrence depth.

---

## 5. The Engineering Level

The engineering level is not an illustration of the philosophy but its operational form: the same constraints, written as an executable architecture. Three archive documents cover it at different depths: the **Unified Implementable Model (UIM v2.0)** defines the statics (requirement semantics, authority hierarchy, verification contracts), the **External Ternary Judge Adapter** defines the external-verification interface, and the **ARC-AGI-3 LCLD Agent architectural and engineering specifications (V10.9)** define a concrete instantiation for a task. Beneath all three lies their common formal-logical foundation: **Modified Brusentsov Entailment Logic** [26] fixes the canonical notation, the verdict space $`V_4`$ with its dominance semilattice, the normative six-step decision cascade, evidence scopes, typed certificates, and the two-tier separation of pointwise verdicts from ensemble law statuses. A further layer, **Spectral and Matrix Realization of $V_4$ in Latent Spaces** [27], supplies the continuous geometric realization of the same verdict calculus: kernel-path quotients of coarse-graining maps, tangent-space diagnostics as evidence (not substitutes) for the normative verifier, and exact plus smooth cumulative-coordinate realizations of the $V_4$ semilattice.

### 5.1. Requirements as ternary constraints

A requirement is not a wish but a constraint on the space of admissible state transitions. UIM fixes three modalities:

- **REQUIRED** — the transition must contain the constraint's consequence;
- **FORBIDDEN** — the transition must not contain the constraint's consequence;
- **IRRELEVANT** — the constraint neither narrows nor widens this class of transitions.

To these is added the honest state **UNRESOLVED** — a constraint whose modality for a given transition has not been established. The fourth state is fundamental: a system that cannot say "I don't know" is forced to fabricate verdicts — the engineering analogue of the philosophical error of passing UNDECIDED off as FOLLOW.

IRRELEVANT here is a first-class outcome, not a missing answer. It is a direct projection of §4.3: a constraint lying in the kernel of the state-update map must neither force nor forbid a transition.

### 5.2. The authority hierarchy

UIM fixes a separation of roles that excludes self-certification:

- **Proposer** — generates transition candidates; has no right to declare a transition actual;
- **Binder** — binds requirements to the concrete execution context; has no right to verify;
- **Planner (with Compiler)** — converts bound hypotheses into executable routes; has no right to certify (UIM §7.3);
- **Verifier** — the only role with the right to certify a transition; external to the Proposer;
- **Memory** — stores only certified transitions (event-sourced journal); has no right to propose.

This is the same structure as in §4.2: the model (Proposer) is separated from the verifier (Verifier), and grounding is a history of certified transitions, not of generated ones. The authority hierarchy is the institutionalization of external verification inside the machine.

### 5.3. Two-phase execution and the pending-transition invariant

Every transition executes in two phases:

1. **Proposal phase.** The Proposer forms a candidate; the Binder binds it to active requirements; a *pending transition* is created — a request that does not yet have ontological status.
2. **Certification phase.** The Verifier issues a verdict on each bound requirement. Only after the full verdict is the transition either recorded in Memory or rejected.

Invariant: **no uncertified transition may affect the system state** — a pending transition is visible neither to subsequent proposals nor to memory. This is the executable form of the ontological principle: to become real (for the system) is to pass certification, not to be generated.

### 5.4. Runtime verdicts

The Verifier (including an external one, via the Ternary Judge Adapter) issues one of four verdicts:

| Verdict | Meaning | Ontological analogue |
|---|---|---|
| **FOLLOW** | The transition satisfies the constraint | Certified following |
| **OMIT** | The constraint does not apply to the transition | Membership in the kernel of the state-update map |
| **NULL** | The transition violates the constraint | Uncertified transition, rejected |
| **UNDECIDED** | The verifier cannot issue a verdict | Honest ignorance; the transition is blocked or escalated |

OMIT is neither an "error" nor a "skip": it is a deliberate decision of non-applicability, logged on equal footing with the rest. The canonical calculus [26] refines OMIT into three disjoint subtypes with fixed controller commands (§5.2 of [26]): OMIT_BLOCKED → preserve the law and repair the route; OMIT_REDUNDANT → drop and suppress the repeat; OMIT_INCIDENTAL → retain silently and advance. The verdict→controller-action bijection is domain-specific: pre-commit judges (the Adapter; the Propose–Judge–Commit loop) map OMIT to silence/no-commit — the move is not admitted into state; post-action verifiers (the ARC-AGI-3 agent V10.9) map OMIT to advance-without-confirmation — the transition has already occurred and the branch is preserved. The invariant common to every domain: **OMIT never certifies and never severs.** Two further canonical invariants bind every domain [26]: a single certified NULL annihilates all other clause statuses, including UNDECIDED (dominance chain NULL ≻ UNDECIDED ≻ OMIT ≻ FOLLOW; Theorem 4.1), and an UNDECIDED record is never overwritten into NULL on evidence-budget exhaustion — the attempt terminates operationally while the audit record permanently retains UNDECIDED (§5.4). The adapter fixes the rule interpreter as an immutable component: the interpreter may not be updated by the agent whose transitions it judges.

### 5.5. Nested levels of specification

| Document | Level of abstraction | What it fixes |
|---|---|---|
| **UIM v2.0** | Architectural ontology | Ternary requirement semantics, the Proposer/Binder/Planner/Verifier/Memory hierarchy, verification contracts, evidence scopes (the four canonical scopes NOT_AVAILABLE / PREDICTIVE_ONLY / OBSERVED_TRANSITION / REPLAY_VERIFIED) |
| **External Ternary Judge Adapter** | Verification protocol | The external-verifier interface, the fixed rule interpreter, the FalseFollowRate metric |
| **ARC-AGI-3 LCLD Agent (V10.9)** | Instantiation | Tri-Agent hierarchy (Explorer / Coder / Solver), isolated memory contours, Brusentsov 4-valued verdicts (FOLLOW / OMIT / NULL / UNDECIDED), sandboxed dynamic DSL |

The three documents are three nesting levels of one principle: **an agent that is not separated from its verifier has no grounds for trusting its own transitions.** The distinction of evidence scopes (canonical Definition 2.1 of [26]: NOT_AVAILABLE / PREDICTIVE_ONLY / OBSERVED_TRANSITION / REPLAY_VERIFIED) is the engineering record of a philosophical boundary: a model's prediction is not an observed transition, and conflating these statuses is the source of hallucinations in the most precise sense of the word.

A fourth document sits beneath the three as their formal-logical foundation: **Modified Brusentsov Entailment Logic** [26] — the canonical specification of the verdict space $`V_4`$ and its dominance semilattice, the modified Brusentsov DNF of conditional entailment $(ac\Rightarrow y)$, the six-step decision cascade, evidence scopes, typed certificates ($\mathcal{C}^{+}$, $\mathcal{C}^{\bot}$, $\mathcal{C}^{\emptyset}$), and the two-tier separation of pointwise verdicts from ensemble law statuses (CONFIRMED / CONTRADICTED / CONDITIONAL_CANDIDATE / UNRESOLVED). Where any of the three documents above and the canonical specification diverge in verdict semantics, the canonical specification governs.

### 5.6. Geometric substrate of the agent

The agent V10.9 runs on a neural substrate whose internal representations are themselves subject to constraint. The geometric theory of latent representations (*Latent Information Structuring*) describes this substrate: how informational constraints organize the internal geometry of the neural carrier on which the agent operates. This is the engineering instantiation of the constraint-envelope principle (§4.4) applied to the representation layer.

The same substrate is given an explicit bridge to the normative verdict calculus by *Spectral and Matrix Realization of $V_4$ in Latent Spaces* [27]. That specification defines (i) a goal- and scale-dependent kernel-path equivalence generated by admissible paths tangent to $\ker d\pi_\ell$, (ii) the induced quotient transition graph, (iii) local tangent-space diagnostics ($\alpha_k$, $\beta_k$, $\nu_k$, Mahalanobis SNR) used strictly as evidence for the MBEL verifier, and (iv) an exact tropical/cumulative realization of the $V_4$ semilattice together with a normalized LogMeanExp relaxation that preserves the simplex and converges uniformly to the crisp join. Soft scores remain training surrogates; final commitment is governed exclusively by the crisp cascade of [26]. Existence and learnability of the required kernel geometry remain empirical hypotheses.

---

## 6. Isomorphism of Levels

The three levels — physical, ontological, engineering — are structurally aligned. The table below fixes the correspondences. The caveat is mandatory: this is a **homology, not an identity** — a structural similarity of forms of constraint on different carriers, not a claim that physics "contains" logic or that an agent "is" a universe.

| Concept | Physical level | Ontological level | Engineering level |
|---|---|---|---|
| Distinction | Bit, Bekenstein bound [15] | Information as constraint $\Omega \to \Omega' \subset \Omega$ | Requirement (REQUIRED/FORBIDDEN) |
| Action | $\hbar$, Margolus–Levitin bound [13] | The price of a transition | A certified transition as the unit of progress |
| Rate / time | Ratio of frequencies; $`\omega = -u^\mu k_\mu`$; redshift | Time as a ratio of rates, not an axis | Operational time $d\mathcal{T} \propto (\hbar \, dN/E) \cdot \eta(M)$ |
| Irrelevance | Kernel of coarse-graining; RG-irrelevant operators | Irrelevance as the kernel of description $\pi$ | IRRELEVANT; verdict OMIT |
| Uncertainty | Quantum uncertainty; Mandelstam–Tamm bound [14] | Honest UNDECIDED | UNRESOLVED; verdict UNDECIDED |
| Verification | Experiment, observed transition; relative-entropy diagnostics | The world as external verifier | Verifier; OBSERVED_TRANSITION; FalseFollowRate |
| Memory | Recorded trace (Landauer price [12]) | Grounding = history of certified transitions | Event-sourced Memory |
| Substrate | Material carrier within the constraint triad | Constraint envelope | The agent's hardware and compute budget |
| **Latent geometric structure** | — | — | Informational minimal surface: $\Sigma$ as minimal-volume embedding in $`g_{\mathrm{approx}}`$ under informational constraint $`I(Z;Y) \geq R_{\mathrm{task}}`$ |

**Irrelevance.** The physical analogue of irrelevance is not "degrees of freedom outside the light cone" (that is a different, kinematic phenomenon) but the kernel of coarse-graining: microstates erased by the map $`\pi: \Omega_{\rm micro} \to \Omega_{\rm macro}`$, and RG-irrelevant operators whose contribution decays with scale. This correspondence is consistent with §4.3 and with the definition of OMIT as membership in the kernel of the state-update map.

**Verification.** In physics the external verifier is the experiment; in the ontology it is the world; in the engineering layer it is the Verifier role. The same authority hierarchy recurs: the internal model does not certify itself.

---

## 7. Thesis Statuses

Statuses are attached to theses, not to documents. A document may be complete as a specification while the thesis it records remains open.

| Thesis | Primary source | Status |
|---|---|---|
| Information as constraint; the constraint triad (distinction / action / rate) | The Algorithm of Being; this document (§2) | FOLLOW as a schema |
| Time as a ratio of rates; operational time $d\mathcal{T} \propto (\hbar \, dN/E)\eta(M)$ | The Algorithm of Being (§3.3–3.4); this document (§2.3–2.4) | FOLLOW as a schema; UNDECIDED as physical theory |
| Irrelevance = kernel of description; two indexings (goal / scale) | The Algorithm of Being (§9); this document (§4.3) | FOLLOW as formalism |
| Consciousness: recursive modeling under external verification | The Algorithm of Being (§10); this document (§4.2) | FOLLOW as an architectural frame; the hard problem is UNDECIDED |
| Substrate as constraint envelope | The Algorithm of Being (§11); this document (§4.4) | FOLLOW as a frame; numerical envelope bounds are UNDECIDED |
| Causal-phase network $(\mathcal{C},\prec)+U(1)\to(\mathcal{M}_4,g_{\mu\nu},A_\mu)$ under (H_P) only; matrix kinematics $W_{xy}=r_{xy}e^{i\theta_{xy}}$ | Causal-Phase Geometry Research Program v2.0 | UNDECIDED: active program with falsification criteria and pilot numerics v0.2 |
| Physical-radion branch (H_R) / 5D KK | KK–Jacobson Commutativity Note | NULL (frozen August 2026) |
| $\Gamma_{\rm corr}$ as residual of informational truncation; dual regimes (local surface-tension condensation = effective DM; global budget-driven void decompression = effective DE) | Causal-Phase Geometry Research Program v2.0; Technical Specification v0.2 | UNDECIDED: formal identification of $\Gamma_{\rm corr}$ is FOLLOW under the stated variational principle; quantitative residual and dual-regime signals are the object of pilot v0.2 |
| Relative-entropy (Dorau–Much [25] / Araki–Uhlmann / Casini) route to gravity | Causal-Phase Geometry Research Program v2.0 | UNDECIDED: theoretical frame; classical KL proxy used in pilot |
| Budget conservation $\Rightarrow$ local condensation forces complementary void rarefaction (formal graph statement) | Causal-Phase Geometry Research Program v2.0; Technical Specification v0.2 | FOLLOW as elementary conservation on finite graphs; dynamical magnitude and continuum limit are UNDECIDED (tested in Mode B of v0.2) |
| Space of Algebras (Level 0) | The Algorithm of Being (§2); this document (§3.1) | UNDECIDED: a conjecture, not a foundation |
| Modified Brusentsov entailment logic; four-valued verdict calculus $`V_4`$ (FOLLOW / OMIT / NULL / UNDECIDED) with dominance semilattice; MDNF of conditional entailment; typed certificates; ensemble law quantifiers; metric, box, and graph realizations | Modified_Brusentsov_Entailment_Logic.md (October 2026) | FOLLOW: formal specification — the canonical reference for verdict semantics corpus-wide (theorems proven internally); implementation conformance and empirical validation per its §7.3 are UNDECIDED |
| Ternary requirement semantics; authority hierarchy | Unified Implementable Model v2.0 | FOLLOW: specified |
| External verifier; FOLLOW/OMIT/NULL/UNDECIDED; FalseFollowRate | External Ternary Judge Adapter; Draft: ternary_judge.md; canonical verdict semantics: [26] | FOLLOW: protocol; preliminary controlled-corpus MVP empirics exist (Reasoning/Draft/ternary_judge.md, run of 2026-08-09: FFR 0.362 → 0.035 at coverage 0.81; effect depends primarily on judge competence); open-domain transfer is UNDECIDED and remains in the §8 program |
| Agent V10.9 (Tri-Agent, Brusentsov 4-valued verdicts) | ARCHITECTURAL / ENGINEERING SPECIFICATION (Version 10.9) | FOLLOW: specification; the ARC-AGI-3 benchmark is in the §8 program |
| Controlled self-development of a language model under an external verifier (capability growth at bounded structural continuity) | Self-Developing Runtime Research Program v0.2 (2026-09-11) | UNDECIDED: pre-implementation specification; success/failure criteria and control groups fixed |
| Latent Agency Framework: graded agency (integration, persistence, informational autonomy); relief vs reasoning budget; recoverability bound; nine measurable predictions | Latent_Agency_Framework.md (v2.0, 2026-10-09; successor to Unified Latent Space of Consciousness v1.0) | UNDECIDED: working hypothesis; predictions untested; the hard problem is bracketed |
| Informational minimal surfaces: $\mathbf{H} = \lambda(\nabla i)^\perp$ as stationary condition; VIM surrogates bound the variational functional | Latent Information Structuring | UNDECIDED: active experimental program (E1–E5); mathematical framework is FOLLOW |
| Kernel-path quotient realization of $V_4$; tangent-space diagnostics as geometric evidence; exact and smooth cumulative-coordinate semilattice aggregation | Spectral and Matrix Realization of $V_4$ in Latent Spaces (v1.0, 2026-10-17) | FOLLOW as formal construction under stated assumptions; existence/learnability of the required kernel geometry and empirical certification of projectors remain UNDECIDED |

The rule for reading the archive: **status is attached to the thesis, not to the document.** A document may be technically complete (FOLLOW as a specification) while recording open questions (UNDECIDED as empirics). Conflating these statuses is the same error as passing a prediction off as an observation.

---

## 8. Experimental Program

### 8.1. Physics

- **Pilot stage v0.2 (consolidated).** Single software complex with Mode A (frozen topology = former v0.1 baseline: residual $\Delta F$ under classical KL truncation) and Mode B (dynamic budget-conserving rewiring: core condensation $\Delta N_\partial$, void depletion $\delta\rho_{\rm void}$, effective void expansion $z_{\rm void}^{\rm eff}$). Eight mandatory null tests D1–D8; decision criteria under $V_4$ (FOLLOW / NULL / UNDECIDED). See Technical Specification v0.2. Closed report `REPORT_v0.2.md` required before any further step.
- **Post-v0.2.** If Mode B yields a confirmed pilot signal (FOLLOW): extract empirical radial profile $\Delta\rho(r)$ and compare analytically with the VIM surface-tension kernel $\mathbf{H}=\lambda(\nabla i)^\perp$; thereafter cautious continuum-limit contact with SPARC and cosmological observables under a single parameter set. If the residual / dual-regime signals vanish (NULL): documented negative result or revision of the constraint definition. UNDECIDED (numerical insufficiency) triggers parallel tempering or larger $L$ before any physical claim.

### 8.2. Engineering

- **FalseFollowRate.** Primary metric of the verifier-centric architecture: the fraction of transitions certified as FOLLOW that fail the constraint under independent checking. A preliminary live MVP on a controlled corpus (Reasoning/Draft/ternary_judge.md, run of 2026-08-09) reports an order-of-magnitude reduction relative to binary baselines (0.362 → 0.035 at coverage 0.81), with an ablation showing that the primary factor is judge competence and the certificate contract is its multiplier. Remaining goal: reproduce the effect on open domains and in the full adapter deployment, via first-class OMIT/UNDECIDED.
- **ARC-AGI-3.** Agent V10.9 is run on the benchmark; the criteria are not only task success but calibration (the match between declared confidence and observed accuracy), isolation integrity, and the share of honest UNDECIDED / OMIT versus fabricated FOLLOW.
- **Ternary Judge track.** The controlled-corpus MVP is complete (see above). Remaining: independent evaluation of the adapter on open domains — rule-interpreter stability across a change of proposer, absence of semantic drift in verdicts, graph persistence (OMIT-node retention, re-verification with rollback), and binary certificates for contradictions. The canonical certificate algebra of [26] (§5.3) supplies the target forms for the two missing certificate types: polarized scoped-exhaustion certificates $\mathcal{C}^{\emptyset}$ for absence claims and binary quote-pair certificates $\mathcal{C}^{\bot}$ for contradictions; conformance testing of the six-step cascade and of the exhaustion invariant (an UNDECIDED record is never rewritten into NULL, §5.4 of [26]) is added to this track.
- **Latent geometry track.** Experimental program E1–E5 from *Latent Information Structuring*: projection of curvature onto information gradient ($`r > r_0`$), curvature dynamics during training, stratification at metric degeneracies, NTK-filtered dynamics correlation, comparison of standard CE training versus explicit VIM surrogate optimization. This track tests whether the neural substrate of the agent self-organizes according to the informational minimal surface principle. Complementary checks required by *Spectral and Matrix Realization of $V_4$* [27]: validation of estimated kernel distributions against $\ker d\pi_\ell$, numerical projector idempotence/orthogonality under the declared positive-definite metric $h$, preservation of $\pi_\ell$ along admissible kernel paths, cross-scale equivalence compatibility, and crisp-limit recovery of the MBEL cascade (including inactive-clause immunity and Axiom 4.1 empty-active-clause guard).

### 8.3. Ontology

The philosophical level has no direct experiment but has an indirect one: **consistency**. If the physics program is falsified, the ontology must revise the corresponding sections; if the engineering metrics show that ternary semantics does not reduce FalseFollowRate, the linked theses lose their operational support and revert to hypothesis status. This document records these dependencies explicitly, so that falsification at one level automatically demotes the linked theses at the others.

---

## 9. What This Document Does Not Claim

1. **It does not claim identity of levels.** The §6 isomorphism is a homology of forms of constraint, not an ontological identification. An agent is not a universe; logic is not physics.
2. **It does not claim that the Space of Algebras is a foundation.** Level 0 is a conjecture with the status UNDECIDED, a promissory note whose fate is tied to the falsifiable causal-phase program (Level 1). Until Level 1 is closed, the Level 0 construction is an abstraction for notational convenience.
3. **It does not claim novelty for the triad as such.** The "information–energy–time" pairs are old (Landauer, Margolus–Levitin, Mandelstam–Tamm). The novelty — if any — lies in binding the triad to a concrete physics program and to an executable engineering semantics.
4. **It does not claim a solution to the hard problem of consciousness.** The "recursive modeling under external verification" frame is architectural, not phenomenological. Qualia lie outside this framework's competence.
5. **It does not claim substrate independence for consciousness.** It claims substrate-parameterization: the architecture of consciousness is realized only within the constraint envelope of a material carrier, and that carrier is the interface to the external verifier.
6. **It does not claim that $\Gamma_{\rm corr}$ has already been computed or fitted to data.** The formal identification of $\Gamma_{\rm corr}$ and of the dual regimes is given in Causal-Phase Geometry v2.0; the pilot stage v0.2 is precisely the first quantitative test of whether a measurable residual and the condensation–decompression signals appear under informational truncation on a budget-conserving graph.
7. **It does not claim completeness.** The document is a snapshot as of the version date. The §7 statuses are subject to revision per the §8 results, in both directions: UNDECIDED may become FOLLOW, and FOLLOW may become NULL.

---

## Appendix. Archive Document Correspondence

| File | Level | Language | Role in the framework |
|---|---|---|---|
| The Algorithm of Being (Revised) | Ontology | EN | The philosophical frame: triad, kernel, consciousness under verification, substrate envelope |
| Causal-Phase Geometry Research Program v2.0 (Oct 2026) | Physics | EN | Level 1 under (H_P): matrix kinematics $W$, dual origin of dark-sector effects (local surface-tension condensation / global budget-driven decompression), explicit $\Gamma_{\rm corr}$; supersedes Aug 2026 draft |
| Causal Phase Geometry Research Program (Aug 2026) | Physics | EN | Historical predecessor of v2.0 (kept for continuity) |
| Technical Specification v0.2 (consolidated) | Physics | EN | Executable pilot: Mode A (frozen = former v0.1) + Mode B (dynamic budget-conserving graph); primary observables $\Delta F$, $\Delta N_\partial$, $\delta\rho_{\rm void}$, $z_{\rm void}^{\rm eff}$; null tests D1–D8 |
| Technical Specification v0.1.1 — $\Gamma_{\rm corr}$ Extraction | Physics | EN | Historical static-lattice pilot (now the Mode A control branch of v0.2) |
| KK–Jacobson Commutativity Note | Physics | EN | Historical (5D route frozen) |
| Modified Brusentsov Entailment Logic and Four-Valued Verdict Calculus (`Reasoning/Modified_Brusentsov_Entailment_Logic.md`) | Reasoning (formal logic) | EN | Canonical formal foundation of verdict semantics corpus-wide: MDNF, $`V_4`$ and dominance semilattice, decision cascade, evidence scopes, typed certificates, ensemble law quantifiers, metric/box/graph realizations |
| Unified Implementable Model v2.0 | Engineering | EN | The agent's architectural ontology |
| External Ternary Judge Adapter | Engineering | EN | The external-verification protocol |
| ARC-AGI-3 LCLD Agent: Architectural + Engineering Specifications (Version 10.9) | Engineering | EN | The V10.9 instantiation (Tri-Agent, isolated memory contours, Brusentsov 4-valued verdict logic; aligned to the canonical specification [26]) |
| The Law of Useful Information Structuring in Model Latent Spaces (`Reasoning/latent_information_structuring.md`) | Reasoning (substrate geometry) | EN | Geometric theory of latent representations: variational principle, VIM surrogates, NTK-filtered dynamics, experimental program (E1–E5) |
| Spectral and Matrix Realization of $V_4$ in Latent Spaces (`Reasoning/Spectral_and_Matrix_Realization_of_V4.md`) | Reasoning (geometry ↔ logic) | EN | Continuous geometric realization of the $V_4$ verdict calculus: kernel-path quotients, tangent-space diagnostics as evidence for MBEL, exact and smooth semilattice aggregation; normative parent = [26] §§3–6 |
| Latent Agency Framework (v2.0) | Reasoning | EN | Working hypothesis: latent-space agency (integration, persistence, autonomy); relief vs budget; recoverability bound; nine measurable predictions; hard problem bracketed. Successor to Unified Latent Space of Consciousness v1.0 |
| Self-Developing Runtime Research Program v0.2 | Reasoning | EN | Pre-implementation specification: controlled self-development of an LLM under an external verifier, with control groups and success/failure criteria |
| Draft: Propose, Judge, Commit (ternary_judge.md); Hierarchical Ternary KG as RAG Alternative | Reasoning (drafts) | EN | Working drafts, not catalogued as formal deliverables: the judge architecture with preliminary MVP results; ternary hierarchical knowledge graph as a RAG alternative |
| Unified Informational-Constructive Framework (this document) | Synthesis | EN | The map of theses, statuses, and cross-level dependencies |

---

## References

- [6] V. Yakunin, *Causal Phase Geometry Research Program* (2026).
- [7] V. Yakunin, *Causal Structure, U(1) Holonomies, and the Thermodynamic Origin of the Einstein–Maxwell System* (2026).
- [8] V. Yakunin, *Unified Implementable Model, Version 2.0: Verifier-Centered Latent World Models with Evidence-Grounded Three-Way Semantics* (2026).
- [9] V. Yakunin, *External Ternary Judge Adapter for OpenClaw and DeepSeek V4 API: Engineering Whitepaper* (2026).
- [10] V. Yakunin, *ARC-AGI-3 LCLD Agent: Architectural Specification and Engineering Specification* (2026).
- [11] N. P. Brusentsov, *Usovershenstvovanie logiki umozaklyucheniy* [The Improvement of Inference Logic], Fond "Novoe tysyacheletie", Moscow, 2012.
- [12] R. Landauer, "Irreversibility and Heat Generation in the Computing Process," *IBM Journal of Research and Development* 5, 183–191 (1961).
- [13] N. Margolus, L. B. Levitin, "The Maximum Speed of Dynamical Evolution," *Physica D* 120, 188–195 (1998).
- [14] L. Mandelstam, I. Tamm, "The Uncertainty Relation Between Energy and Time in Non-Relativistic Quantum Mechanics," *Journal of Physics (USSR)* 9, 249–254 (1945).
- [15] J. D. Bekenstein, "Universal Upper Bound on the Entropy-to-Energy Ratio for Bounded Systems," *Physical Review D* 23, 287–298 (1981).
- [16] N. Tishby, F. C. Pereira, W. Bialek, "The Information Bottleneck Method," in *Proceedings of the 37th Annual Allerton Conference on Communication, Control and Computing*, 368–377 (1999).
- [17] E. P. Hoel, L. Albantakis, G. Tononi, "Quantifying Causal Emergence Shows That Macro Can Beat Micro," *Proceedings of the National Academy of Sciences* 110, 19790–19795 (2013).
- [22] A. Connes, *Noncommutative Geometry*, Academic Press, 1994.
- [23] A. Connes, "Gravity Coupled with Matter and the Foundation of Non-commutative Geometry," *Communications in Mathematical Physics* 182, 155–176 (1996).
- [24] A. Connes, C. Rovelli, "Von Neumann Algebra Automorphisms and Time-Thermodynamics Relation in Generally Covariant Quantum Theories," *Classical and Quantum Gravity* 11, 2899–2917 (1994).
- [25] P. Dorau, A. Much, "From Quantum Relative Entropy to the Semiclassical Einstein Equations," *Physical Review Letters* (2026); arXiv:2510.24491.
- [26] V. Yakunin, *Modified Brusentsov Entailment Logic and Four-Valued Verdict Calculus for External State-Control Systems* (2026); this repository, `Reasoning/Modified_Brusentsov_Entailment_Logic.md` — the canonical reference for verdict semantics across the corpus.
- [27] V. Yakunin, *Spectral and Matrix Realization of $V_4$ in Latent Spaces* (2026); this repository, `Reasoning/Spectral_and_Matrix_Realization_of_V4.md` — geometric/matrix realization of the four-valued verdict calculus on latent state spaces (kernel-path quotients, tangent diagnostics, cumulative semilattice).

---

*End of document. Version 1.7. Feedback and objections — via repository issues.*
