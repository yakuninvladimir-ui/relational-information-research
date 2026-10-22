# **Unified Informational-Constructive Framework**

**Author:** Vladimir Yakunin  
**Version:** 1.8  
**Date:** 2026-10-21 (v1.8 revision; v1.7: 2026-10-17; v1.6: 2026-10-17; v1.5: 2026-10-14; v1.4: 2026-10-13; v1.3: 2026-10-05; v1.2: 2026-09-23)  
**Status:** archive synthesis document; aligned with the revised edition of “The Algorithm of Being” (2026), the Causal Phase Program v3.9 (October 21, 2026; structuring triad, binary-diamond selection, Oseledets–Landauer bridge, protocols V1–V7), the Causal-Phase Geometry Research Program v2.0 (October 17, 2026; historical — the $`\Gamma_{\mathrm{corr}}`$ continuum formulation), Technical Specification v0.2 (frozen historical pilot; v0.3 pending), the geometric theory of latent representations (September 2026), the ARC-AGI-3 LCLD Agent specifications V10.9 (October 2026), the Latent Agency Framework v2.1 (October 21, 2026), the Self-Developing Runtime Research Program v0.2 (September 2026), the canonical Modified Brusentsov Entailment Logic specification (October 2026), the Spectral and Matrix Realization of V₄ in Latent Spaces v2.2 (October 17, 2026), and the preliminary ternary-judge MVP results (August 2026)

## **1. Central Thesis**

Reality, consciousness, and artificial intelligence are not separate domains but different scales of one and the same process: **self-structuring under constraint**. At every level the same architecture recurs — but not on an abstract “substrate-indifferent” carrier; it runs on a material substrate with its own **constraint envelope** (power, distinction rate, noise, persistence) that parameterizes viable architectures.

| Level | Substrate | What happens |
| :--- | :--- | :--- |
| Physical | Causal network + U(1) holonomies | Spacetime and field emerge as stable regimes of constrained dynamics |
| Ontological | Recursive semantic structures on a biological envelope | Consciousness is a self-model certified by the world through action |
| Engineering | Neuro-symbolic agent on an artificial envelope | A rational agent separates hypothesis generation, selection, and fact fixation |

---

## **2. Basic Definitions**

### **2.1. Information as constraint**

**Information** is not data but a narrowing of the space of admissible states:

```math
\Omega \to \Omega' \subset \Omega
```

Without constraint, energy dissipates into entropy. With constraint, it forms stable structure. If energy is the capacity for transformation, information is the geometry of admissible transformation.

### **2.2. The constraint triad: distinction, action, rate**

Information is not the only fundamental constraint. Three physical results bind information and energy so tightly that neither can serve as the sole primitive:

1. **Erasure has a price.** By Landauer, erasing one bit at temperature $`T`$ dissipates at least $`k_B T \ln 2`$ [12]. Forgetting, compression, and filtering the irrelevant are paid thermodynamic operations.
2. **The rate of distinctions is bounded by energy.** The Margolus–Levitin theorem: a system with mean energy $`E`$ traverses at most $`2E/\pi\hbar`$ orthogonal states per second [13]; the Mandelstam–Tamm bound: $`\Delta t \geq \pi\hbar/(2\Delta E)`$ [14].
3. **Information capacity is bounded by energy and size** (the Bekenstein bound) [15].

The fundamental quantities: **distinction** (the bit), **action** ($`E \cdot t`$, quantum $`\hbar`$), **causal rate** (the limit $`c`$). Physics' three conversion constants correspond to the triad’s three edges: $`c`$ — space↔time, $`\hbar`$ — energy↔frequency ($`E = \hbar\omega`$), $`k_B`$ — entropy↔energy.

### **2.3. Time: rate, not axis**

The archive’s physics program admits no external global time: proper time is defined along worldlines, and in discrete kinematics is estimated by maximal-chain length [6, 7]. Only **ratios of rates** are observable. The general redshift formula is literally a comparison of two clocks (null-transported phase against the local time directions of emitter and observer):

```math
1+z = \frac{(-u^\mu k_\mu)_{\mathrm{em}}}{(-u^\mu k_\mu)_{\mathrm{obs}}}
```

In the Causal Phase Program v3.9 (§5.1) this becomes fully combinatorial: relative operational time between subsystems is the ratio of accumulated gauge-invariant holonomy cycles along worldtubes, $`R^{(\ell)}_{AB}=\Delta N^{(\ell)}_A/\Delta N^{(\ell)}_B`$, and the Lorentzian signature $`(-,+,+,+)`$ itself arises from budget competition between spatial propagation and internal diamond synchronization. An algebraic echo of the same thesis is the Connes–Rovelli thermal time hypothesis [24]: a state on an algebra generates its own time evolution through the modular flow. **The operational content of time is a ratio of rates; the time axis is a derived bookkeeping tool.**

### **2.4. Operational time**

The density of distinctions a system can generate and integrate is paid out of its energy envelope. An honest schema, anchored in Margolus–Levitin:

```math
d\mathcal{T} \propto \frac{\hbar \, dN}{E} \cdot \eta(M)
```

where $`dN`$ is the number of orthogonal distinctions generated, $`E`$ the mean energy, and $`\eta(M)`$ the architecture’s efficiency (the fraction of the physical rate limit actually achieved). The bound is physics; the architectural factor is a schema.

### **2.5. Ternary semantics**

Any judgment about a system state takes one of three values:

- **REQUIRED** — the state is necessary for the current task (progress, success).
- **FORBIDDEN** — the state is excluded by constraints (contradiction, impossibility).
- **IRRELEVANT** — the state is admissible but semantically invariant (no-op, noise).

To these is added the epistemic category **UNRESOLVED** — insufficient data for classification. In the judge for LLM reasoning [9], the same discipline takes the form of verdicts FOLLOW / OMIT / NULL / UNDECIDED. The canonical formalization is fixed by the Modified Brusentsov Entailment Logic specification [26]: the ontological triad FOLLOW (+1) / OMIT (0) / NULL (−1) — operational aliases REQUIRED / IRRELEVANT / FORBIDDEN — is ordered by the strict dominance chain NULL ≻ UNDECIDED ≻ OMIT ≻ FOLLOW, while epistemic insufficiency is isolated as the control signal UNDECIDED (alias UNRESOLVED), never as a fourth truth value. OMIT certifies admissible inessentiality of a move in one of three disjoint forms: blocked applicability (OMIT_BLOCKED), semantic invariance (OMIT_REDUNDANT), or a resolved incidental / sub-threshold change (OMIT_INCIDENTAL).

**Important:** `IRRELEVANT` is neither “false” nor “unknown.” It is an explicitly recorded absence of relevance, allowing the system to compress its attention space.

### **2.6. The Algorithm of Being (short form)**

Distinction → Constraint → Balance → Compression → Meaning → Modeling → Certification → Self-Correction

Or shorter still:

Relation → Constraint → Structure → Semantics → Intelligence

---

## **3. The Physical Level: Causal Phase Program**

### **3.1. The three-layer stack of the program**

The archive’s physics works with an explicit stack, not a single “foundation”:

| Layer | Object | Status |
| :--- | :--- | :--- |
| Level 0 — algebraic substrate | “Space of Algebras” (the Connes lineage: Gelfand duality, spectral triples, thermal time [22–24]) | Conjecture; regulative idea; formalization deferred |
| Level 1 — causal-phase complex | Discrete causal order with U(1) holonomies on Hasse links, encoded as a nilpotent causal-phase transfer matrix $`W_{xy}=R_{xy}e^{i\theta_{xy}}`$; structuring triad $`(\mathcal{I}_A,\partial A,\mathcal{E}_A)`$; continuum limits | Active program (CPP v3.9) with verification protocols V1–V7; executable specification v0.3 pending (v0.2 frozen) |
| Level 2 — continuum geometry | Lorentzian metric, gauge connection, three-component effective Einstein–Maxwell decomposition ($`T^{\mathrm{bulk}}`$, $`T^{\mathrm{interface}}`$, $`\Lambda_{\mathrm{eff}}[I_{\mathrm{erase}}]`$) | Established structures + open continuum limit (Protocol V4); historical $`\Gamma_{\mathrm{corr}}`$ formulation in CPG v2.0 |

The “Space of Algebras” is not a claimed foundation but a deep conjectural layer whose fate is tied to the intermediate one: failure of the causal-phase program by its own criteria demotes the conjecture to a historical footnote.

### **3.2. Fundamental kinematics**

The base structure is a finite (or locally finite) causal set $`(X,\prec)`$ equipped with U(1) holonomies on oriented Hasse links, encoded as a single nilpotent complex **causal-phase transfer matrix**:

```math
W_{xy}=R_{xy}\,e^{i\theta_{xy}},\qquad R_{xy}\in\{0,1\},\quad\theta_{xy}\in[0,2\pi),\quad W^N=0,
```

where $`R`$ is the Boolean Hasse matrix — strictly upper-triangular and transitively irreducible (no edges short-circuiting directed paths of length $`\ge2`$). Unbranched null chains (two-step waist width $`K_{xy}=0`$) form the lightlike radiative scaffold and transmit phase without accumulating gauge-invariant holonomy; massive matter corresponds to structured complexes with waists $`K_{xy}\ge2`$, whose elementary causal diamonds carry irreducible phase dynamics tied together by the exact Wilson interference identity $`\sum_{a<b}(1-\cos\Phi_{ab})=\tfrac12K_{xy}J_{xy}`$ (CPP v3.9, Prop 1.1). Coarse-graining yields continuum geometry:

```math
(X,R,\Theta)\xrightarrow{\pi_\ell}(\mathcal{M}_4,g_{\mu\nu},A_\mu).
```

- The causal order fixes the light cones and the conformal class of the metric.
- The volume measure (element count in an interval) fixes the proper-time scale.
- Discrete U(1) transports generate the electromagnetic connection; gauge curvature arises from path non-commutativity on minimal diamonds.

The phase layer is treated strictly as an **internal** fibre:

```math
U(1)\hookrightarrow P\xrightarrow{\pi}M_4,\quad\delta\ell_*=0.
```

No free radion, no physical fifth dimension, no KK tower; postulating fixed microscopic dimensions prior to kernel factorization is rejected (CPP v3.9 Registry item 20, NULL). The competing physical-radion branch (H_R) has been frozen (August 2026). The full formal specification — Hasse criteria, the structuring triad $`(\mathcal{I}_A,\partial A,\mathcal{E}_A)`$, the variational selection of binary causal diamonds ($`K^{\mathrm{eff}}_{xy}=2`$, Thm 3.1), and the $`3+1`$ minimality argument (§3.3 of v3.9) — is given in **Causal Phase Program v3.9**.

### **3.3. Thermodynamic bridge at the interface and the constraint triad**

The historical v2.0 program derived gravity through the relative-entropy route (Dorau–Much [25]; Araki–Uhlmann; the Casini link between the Bekenstein bound and the non-negativity of relative entropy), with the local bound $`D_{\mathrm{KL}}(\sigma_D\|\rho_{\mathrm{dyn,D}})\le c\cdot N_\partial`$ on causal diamonds and a classical Kullback–Leibler proxy in the pilot stage. That route is retained in CPG v2.0 as historical; it was never executed numerically, and the full modular relative entropy was never claimed.

In **CPP v3.9** the thermodynamic bridge is the **Oseledets–Landauer erasure-flux theorem** (Thm 4.1): a stationary dissipative attractor under boundary noise must expel information across its outgoing interface at the rate

```math
\dot I_{\mathrm{erase}}(\mathcal{I}_A\to\partial^+A)\ \ge\ \frac{\kappa(A)-h_{\mathrm{KS}}(A)}{\ln 2},\qquad \dot Q_{\mathrm{ext}}\ \ge\ k_B T_{\partial A}\bigl(\kappa(A)-h_{\mathrm{KS}}(A)\bigr),
```

where $`\kappa(A)`$ is the transverse Oseledets contraction and $`h_{\mathrm{KS}}(A)`$ the internal entropy production (Landauer price per bit). The interface capacity is combinatorially bounded, $`C(\partial^+A)\le c_0|\partial^+A|_E`$, which together with the data-processing inequality yields the recoverability bound (Prop 2.1) — the physical-level counterpart of the constraint triad: distinction, action, and rate are paid across the boundary of every localized structure. Synchronization across the interface is governed by the boundary kernel-inclusion criterion $`\ker\Pi_{\mathcal{I},\partial A}\subseteq\ker\Pi_{\mathcal{E},\partial A}`$ (Prop 2.2): precision sparsity (Markov screening) coexists with exactly mediated long-range covariance $`\Sigma_{\mathcal{I}\mathcal{E}}\ne0`$.

Globally, an exact combinatorial identity (Prop 6.1) partitions coherent diamonds across internal bulks, interfaces, and the external channel. The dynamical hypothesis H-LG (UNDECIDED; Protocols V2–V3) states that local condensation drives phase-mediated rarefaction of voids beyond combinatorial edge subtraction — the seed of effective metric expansion.

### **3.4. Effective field equations: three-component decomposition and the dual origin of dark-sector effects**

In the macroscopic regime where null paths ($`K_{xy}=0`$) reconstruct the conformal structure of $`g_{\mu\nu}`$ and link phases $`\theta_{xy}=\int_x^y A_\mu dx^\mu`$ induce the Maxwell field strength, the Landauer interface balance $`\delta Q_{\mathrm{ext}}=T_{\partial A}\,\delta S_{\mathrm{interface}}`$ (Thm 4.1) together with the Raychaudhuri equation on local causal screens yields the target Einstein–Maxwell equation of state (CPP v3.9 §6.2; UNDECIDED — Protocol V4):

```math
R_{\mu\nu}-\tfrac12Rg_{\mu\nu}+\Lambda_{\mathrm{eff}}[I_{\mathrm{erase}}]\,g_{\mu\nu}=\frac{8\pi G_{\mathrm{eff}}}{c^4}\Bigl(T^{\mathrm{bulk}}_{\mu\nu}(\mathcal{I}_A)+T^{\mathrm{interface}}_{\mu\nu}(\partial A)+T^{\mathrm{em}}_{\mu\nu}(F_{\alpha\beta})\Bigr).
```

1. **$`T^{\mathrm{bulk}}_{\mu\nu}(\mathcal{I}_A)`$ — localized massive matter:** the contribution of high-synchronization diamond and vortical complexes ($`\lambda_2>\lambda_{\mathrm{crit}}`$, $`H_{\mathrm{rot}}\ne0`$).
2. **$`T^{\mathrm{interface}}_{\mu\nu}(\partial A)`$ — synchronization-shell tension (“dark matter” regime):** the boundary transition zone where the frequency mismatch between the internal clock $`\omega_A`$ and the external channel is balanced by embedding curvature $`\mathbf H=\lambda(\nabla i)^\perp`$ (Prop 3.1) and precision-weighted prediction error (Prop 2.2). At galactic scales this extended interface produces an effective gravitational potential without new particle species in the halo.
3. **$`\Lambda_{\mathrm{eff}}[I_{\mathrm{erase}}]\,g_{\mu\nu}`$ — global channel response (“dark energy” regime):** cumulative null-mode injection across all outgoing interfaces rarefies the external channel (H-LG), coupled to bulk and interface stress-energy via the Bianchi identity.

Dense cores that reach interface saturation $`\eta_{\mathrm{sat}}\ge1`$ enter the post-horizon phase (§6.3 of v3.9; UNDECIDED — Protocol V6): the outgoing interface screens deeper bulk layers, radiates thermally with area-law entropy $`\propto|\partial^+A|_E`$, and the interior transitions to a high-rank matrix phase $`K^{\mathrm{eff}}_{xy}\ge3`$.

The explicit correlation functional $`\Gamma_{\mathrm{corr}}`$ of the v2.0 program — the KKT form $`\lambda(x)[i(x)-\mathcal B_{\max}(x)]_+`$ plus the budget term — is retained in **CPG v2.0 (historical)**; in v3.9 the same physics is carried by the triad decomposition above. Whether any of these signals is quantitatively real is the object of protocols V1–V7, whose executable specification (Tech Spec v0.3) is pending.

### **3.5. Computational verification program**

The frontal program is **protocols V1–V7** (CPP v3.9 §7): graph-level tests with pre-registered numerical pass/fail thresholds and control ensembles — V1 binary-diamond collapse and dimension selection; V2 Oseledets contraction vs. interface flux; V3 phase-mediated void rarefaction; V4 interfacial synchronization shell; V5 compact-to-filamentary architecture transition; V6 horizon saturation; V7 kernel inclusion, solenoidal spectral gap, integrator truncation. A self-contained reference implementation (Python / NumPy / SciPy) is given in CPP v3.9 §9.

**Technical Specification v0.2 is frozen and was never executed.** Its Mode A (frozen topology; residual $`\Delta F`$) and Mode B (budget-conserving rewiring; observables $`\Delta N_\partial`$, $`\delta\rho_{\mathrm{void}}`$, $`z^{\mathrm{eff}}_{\mathrm{void}}`$; null tests D1–D8) targeted the same condensation–rarefaction mechanism that Protocol V3 now covers, but under the v2.0 mechanics of $`D_{\mathrm{KL}}\le c\,N_\partial`$. **Technical Specification v0.3**, implementing V1–V7 on the v3.9 reference implementation, is planned and not yet created. Until a closed report exists, no empirical claim of the physics program is certified.

---

## **4. The Ontological Level: The Algorithm of Being**

### **4.1. Summary of definitions**

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

### **4.2. Consciousness: recursive modeling under external verification**

Consciousness is a hierarchical semantic architecture that (1) represents reality; (2) evaluates its representations; (3) models its own role within them; (4) corrects itself through experience — and whose corrections are **certified from outside the model**.

The recursive loop of experience contains not only logic but experiment. A closed model can check itself only against itself; without an external channel, recursion degenerates into self-confirmation — a documented failure mode of LLM reasoning that the judge architecture was built to eliminate [9]. The epistemic loop of consciousness has the same authority hierarchy as the verifier-centric agent [8–10]: the internal proposer (imagination, inference, planning) creates no facts; a fact is created by action and trusted observation of the outcome. **The world is the external verifier. Experiment is the channel to it. Science is the institutionalization of the channel.**

A consequence — a grounding criterion for meaning: a model’s semantic content is not its internal coherence but its **history of certified transitions**. A model without an external channel can be arbitrarily coherent and remains ungrounded — its assertions forever hold the status UNDECIDED [9].

At sufficient depth, the observer ceases to be external to the model and becomes one of the modeled structures — but a structure whose assertions, including those about itself, are subject to external certification.

**Boundary of claims.** Recursive self-models are realizable — the archive contains working architectures with explicit self-modeling and backreaction in the loop [8, 10]. Phenomenal experience (the hard problem) is a separate question; it is honestly bracketed, not “dissolved.”

### **4.3. Irrelevance as the kernel of description**

Meaning arises through semantic compression, and compression has an exact form. Coarse-graining is a many-to-one map:

```math
\pi: \Omega_{\mathrm{micro}} \to \Omega_{\mathrm{macro}}
```

Everything falling into the kernel of $`\pi`$ is irrelevant for that description. The stable content of a description is what survives the quotient. Physics already uses the word: in the renormalization group, *irrelevant operators* are couplings that decay under repeated coarse-graining; fixed points of the flow are stabilized macrostructures.

The boundary of the parallel must be stated explicitly: coarse-graining is indexed by **scale**, irrelevance by **goal**. The exact formulation:

> **Irrelevance is goal-indexed coarse-graining; coarse-graining is scale-indexed irrelevance.**

The information bottleneck formalizes the second case (keep about $`X`$ only what is predictive of the goal $`Y`$) [16]; causal emergence shows that coarse-graining can be causally *stronger* than the micro-description — compression is not pure loss [17].

Intelligence works not by enumeration but by compression. The third operator ($`\emptyset`$) is ontologically necessary: without it there is no attention, without attention no abstraction, without abstraction no generalization. And it is not free: by Landauer, discarding distinctions is dissipative [12]. **The economics of attention is a thermodynamic economics**; “intelligence is disciplined compression” is a consequence of the triad, not an aphorism.

### **4.4. Substrate as constraint envelope**

“Substrate independence” is the wrong slogan. Two questions must be separated:

- **Logical realizability:** architecture is not bound to material — multiple realizability stands.
- **Physical realizability:** any actual realization must fit the envelope: available power, achievable distinction rate, noise floor, thermal stability, memory persistence, a sensorimotor channel to the external verifier.

The correct position is **substrate-parameterization**: substrate matters parametrically, not essentially. The brain is remarkable not as tissue but as an extreme solution of the triad: ~20 W at $`\sim 10^{14}`$–$`10^{15}`$ synaptic events per second. Different envelopes breed different economies of thought: consciousness at datacenter power has a different price for memory, forgetting, and parallelism — its architecture will be structurally deformed relative to the biological one, not merely “faster.”

The substrate is also the **interface to the verifier**: a disembodied “pure intellect” lacks any source of certification and inevitably self-confirms. In the archive’s ontology, matter is itself stabilized relation, so the relation of consciousness to the brain is **architecture on architecture**: an informational regime carried by a material regime; the meeting point of the information/time and energy/time regimes.

**Honest UNDECIDED:** which envelope parameters are *necessary* (not merely sufficient) for consciousness is unknown; no grounded thresholds exist for power, distinction rate, or recurrence depth.

---

## **5. The Engineering Level**

The engineering level is not an illustration of the philosophy but its operational form: the same constraints, written as an executable architecture. Three archive documents cover it at different depths: the **Unified Implementable Model (UIM v2.0)** defines the statics (requirement semantics, authority hierarchy, verification contracts), the **External Ternary Judge Adapter** defines the external-verification interface, and the **ARC-AGI-3 LCLD Agent architectural and engineering specifications (V10.9)** define a concrete instantiation for a task. Beneath all three lies their common formal-logical foundation: **Modified Brusentsov Entailment Logic** [26] fixes the canonical notation, the verdict space $`V_4`$ with its dominance semilattice, the normative six-step decision cascade, evidence scopes, typed certificates, and the two-tier separation of pointwise verdicts from ensemble law statuses. A further layer, **Spectral and Matrix Realization of $`V_4`$ in Latent Spaces** [27], supplies the continuous geometric realization of the same verdict calculus: kernel-path quotients of coarse-graining maps, tangent-space diagnostics as evidence (not substitutes) for the normative verifier, and exact plus smooth cumulative-coordinate realizations of the $`V_4`$ semilattice.

### **5.1. Requirements as ternary constraints**

A requirement is not a wish but a constraint on the space of admissible state transitions. UIM fixes three modalities:

- **REQUIRED** — the transition must contain the constraint’s consequence;
- **FORBIDDEN** — the transition must not contain the constraint’s consequence;
- **IRRELEVANT** — the constraint neither narrows nor widens this class of transitions.

To these is added the honest state **UNRESOLVED** — a constraint whose modality for a given transition has not been established. The fourth state is fundamental: a system that cannot say “I don’t know” is forced to fabricate verdicts — the engineering analogue of the philosophical error of passing UNDECIDED off as FOLLOW.

IRRELEVANT here is a first-class outcome, not a missing answer. It is a direct projection of §4.3: a constraint lying in the kernel of the state-update map must neither force nor forbid a transition.

### **5.2. The authority hierarchy**

UIM fixes a separation of roles that excludes self-certification:

- **Proposer** — generates transition candidates; has no right to declare a transition actual;
- **Binder** — binds requirements to the concrete execution context; has no right to verify;
- **Planner (with Compiler)** — converts bound hypotheses into executable routes; has no right to certify (UIM §7.3);
- **Verifier** — the only role with the right to certify a transition; external to the Proposer;
- **Memory** — stores only certified transitions (event-sourced journal); has no right to propose.

This is the same structure as in §4.2: the model (Proposer) is separated from the verifier (Verifier), and grounding is a history of certified transitions, not of generated ones. The authority hierarchy is the institutionalization of external verification inside the machine.

### **5.3. Two-phase execution and the pending-transition invariant**

Every transition executes in two phases:

1. **Proposal phase.** The Proposer forms a candidate; the Binder binds it to active requirements; a *pending transition* is created — a request that does not yet have ontological status.
2. **Certification phase.** The Verifier issues a verdict on each bound requirement. Only after the full verdict is the transition either recorded in Memory or rejected.

Invariant: **no uncertified transition may affect the system state** — a pending transition is visible neither to subsequent proposals nor to memory. This is the executable form of the ontological principle: to become real (for the system) is to pass certification, not to be generated.

### **5.4. Runtime verdicts**

The Verifier (including an external one, via the Ternary Judge Adapter) issues one of four verdicts:

| Verdict | Meaning | Ontological analogue |
| :--- | :--- | :--- |
| **FOLLOW** | The transition satisfies the constraint | Certified following |
| **OMIT** | The constraint does not apply to the transition | Membership in the kernel of the state-update map |
| **NULL** | The transition violates the constraint | Uncertified transition, rejected |
| **UNDECIDED** | The verifier cannot issue a verdict | Honest ignorance; the transition is blocked or escalated |

OMIT is neither an “error” nor a “skip”: it is a deliberate decision of non-applicability, logged on equal footing with the rest. The canonical calculus [26] refines OMIT into three disjoint subtypes with fixed controller commands (§5.2 of [26]): OMIT_BLOCKED → preserve the law and repair the route; OMIT_REDUNDANT → drop and suppress the repeat; OMIT_INCIDENTAL → retain silently and advance. The verdict→controller-action bijection is domain-specific: pre-commit judges (the Adapter; the Propose–Judge–Commit loop) map OMIT to silence/no-commit — the move is not admitted into state; post-action verifiers (the ARC-AGI-3 agent V10.9) map OMIT to advance-without-confirmation — the transition has already occurred and the branch is preserved. The invariant common to every domain: **OMIT never certifies and never severs.** Two further canonical invariants bind every domain [26]: a single certified NULL annihilates all other clause statuses, including UNDECIDED (dominance chain NULL ≻ UNDECIDED ≻ OMIT ≻ FOLLOW; Theorem 4.1), and an UNDECIDED record is never overwritten into NULL on evidence-budget exhaustion — the attempt terminates operationally while the audit record permanently retains UNDECIDED (§5.4). The adapter fixes the rule interpreter as an immutable component: the interpreter may not be updated by the agent whose transitions it judges.

### **5.5. Nested levels of specification**

| Document | Level of abstraction | What it fixes |
| :--- | :--- | :--- |
| **UIM v2.0** | Architectural ontology | Ternary requirement semantics, the Proposer/Binder/Planner/Verifier/Memory hierarchy, verification contracts, evidence scopes (the four canonical scopes NOT_AVAILABLE / PREDICTIVE_ONLY / OBSERVED_TRANSITION / REPLAY_VERIFIED) |
| **External Ternary Judge Adapter** | Verification protocol | The external-verifier interface, the fixed rule interpreter, the FalseFollowRate metric |
| **ARC-AGI-3 LCLD Agent (V10.9)** | Instantiation | Tri-Agent hierarchy (Explorer / Coder / Solver), isolated memory contours, Brusentsov 4-valued verdicts (FOLLOW / OMIT / NULL / UNDECIDED), sandboxed dynamic DSL |

The three documents are three nesting levels of one principle: **an agent that is not separated from its verifier has no grounds for trusting its own transitions.** The distinction of evidence scopes (canonical Definition 2.1 of [26]: NOT_AVAILABLE / PREDICTIVE_ONLY / OBSERVED_TRANSITION / REPLAY_VERIFIED) is the engineering record of a philosophical boundary: a model’s prediction is not an observed transition, and conflating these statuses is the source of hallucinations in the most precise sense of the word.

A fourth document sits beneath the three as their formal-logical foundation: **Modified Brusentsov Entailment Logic** [26] — the canonical specification of the verdict space $`V_4`$ and its dominance semilattice, the modified Brusentsov DNF of conditional entailment $`(ac\Rightarrow y)`$, the six-step decision cascade, evidence scopes, typed certificates ($`\mathcal{C}^{+}`$, $`\mathcal{C}^{\bot}`$, $`\mathcal{C}^{\emptyset}`$), and the two-tier separation of pointwise verdicts from ensemble law statuses (CONFIRMED / CONTRADICTED / CONDITIONAL_CANDIDATE / UNRESOLVED). Where any of the three documents above and the canonical specification diverge in verdict semantics, the canonical specification governs.

### **5.6. Geometric substrate of the agent**

The agent V10.9 runs on a neural substrate whose internal representations are themselves subject to constraint. The geometric theory of latent representations (*Latent Information Structuring*) describes this substrate: how informational constraints organize the internal geometry of the neural carrier on which the agent operates. This is the engineering instantiation of the constraint-envelope principle (§4.4) applied to the representation layer.

The same substrate is given an explicit bridge to the normative verdict calculus by *Spectral and Matrix Realization of $`V_4`$ in Latent Spaces* [27]. That specification defines (i) a goal- and scale-dependent kernel-path equivalence generated by admissible paths tangent to $`\ker d\pi_\ell`$, (ii) the induced quotient transition graph, (iii) local tangent-space diagnostics ($`\alpha_k`$, $`\beta_k`$, $`\nu_k`$, Mahalanobis SNR) used strictly as evidence for the MBEL verifier, and (iv) an exact tropical/cumulative realization of the $`V_4`$ semilattice together with a normalized LogMeanExp relaxation that preserves the simplex and converges uniformly to the crisp join. Soft scores remain training surrogates; final commitment is governed exclusively by the crisp cascade of [26]. Existence and learnability of the required kernel geometry remain empirical hypotheses.

---

## **6. Isomorphism of Levels**

The three levels — physical, ontological, engineering — are structurally aligned. The table below fixes the correspondences. The caveat is mandatory: this is a **homology, not an identity** — a structural similarity of forms of constraint on different carriers, not a claim that physics “contains” logic or that an agent “is” a universe.

| Concept | Physical level | Ontological level | Engineering level |
| :--- | :--- | :--- | :--- |
| Distinction | Bit, Bekenstein bound [15] | Information as constraint $`\Omega \to \Omega' \subset \Omega`$ | Requirement (REQUIRED/FORBIDDEN) |
| Action | $`\hbar`$, Margolus–Levitin bound [13] | The price of a transition | A certified transition as the unit of progress |
| Rate / time | Ratio of frequencies; $`\omega = -u^\mu k_\mu`$; redshift | Time as a ratio of rates, not an axis | Operational time $`d\mathcal{T} \propto (\hbar \, dN/E) \cdot \eta(M)`$ |
| Irrelevance | Kernel of coarse-graining; RG-irrelevant operators | Irrelevance as the kernel of description $`\pi`$ | IRRELEVANT; verdict OMIT |
| Uncertainty | Quantum uncertainty; Mandelstam–Tamm bound [14] | Honest UNDECIDED | UNRESOLVED; verdict UNDECIDED |
| Verification | Experiment, observed transition; relative-entropy diagnostics | The world as external verifier | Verifier; OBSERVED_TRANSITION; FalseFollowRate |
| Memory | Recorded trace (Landauer price [12]) | Grounding = history of certified transitions | Event-sourced Memory |
| Substrate | Material carrier within the constraint triad | Constraint envelope | The agent’s hardware and compute budget |
| **Structuring triad** | Internal relief $`\mathcal{I}_A`$ / bilateral interface $`\partial A`$ / external channel $`\mathcal{E}_A`$; kernel-inclusion synchronization (CPP v3.9 §2) | Markov blanket: internal / boundary / external states; recoverability bound (LAF v2.1 §8) | Isolated memory contours and the authority boundary: committed state / verification interface / untrusted proposals (V10.9) |
| **Latent geometric structure** | — | — | Informational minimal surface: $`\Sigma`$ as minimal-volume embedding in $`g_{\mathrm{approx}}`$ under informational constraint $`I(Z;Y) \geq R_{\mathrm{task}}`$ |

**Irrelevance.** The physical analogue of irrelevance is not “degrees of freedom outside the light cone” (that is a different, kinematic phenomenon) but the kernel of coarse-graining: microstates erased by the map $`\pi: \Omega_{\mathrm{micro}} \to \Omega_{\mathrm{macro}}`$, and RG-irrelevant operators whose contribution decays with scale. This correspondence is consistent with §4.3 and with the definition of OMIT as membership in the kernel of the state-update map.

**Verification.** In physics the external verifier is the experiment; in the ontology it is the world; in the engineering layer it is the Verifier role. The same authority hierarchy recurs: the internal model does not certify itself.

---

## **7. Thesis Statuses**

Statuses are attached to theses, not to documents. A document may be complete as a specification while the thesis it records remains open.

| Thesis | Primary source | Status |
| :--- | :--- | :--- |
| Information as constraint; the constraint triad (distinction / action / rate) | The Algorithm of Being; this document (§2) | FOLLOW as a schema |
| Time as a ratio of rates; operational time $`d\mathcal{T} \propto (\hbar \, dN/E)\eta(M)`$ | The Algorithm of Being (§3.3–3.4); this document (§2.3–2.4) | FOLLOW as a schema; UNDECIDED as physical theory |
| Irrelevance = kernel of description; two indexings (goal / scale) | The Algorithm of Being (§9); this document (§4.3) | FOLLOW as formalism |
| Consciousness: recursive modeling under external verification | The Algorithm of Being (§10); this document (§4.2) | FOLLOW as an architectural frame; the hard problem is UNDECIDED |
| Substrate as constraint envelope | The Algorithm of Being (§11); this document (§4.4) | FOLLOW as a frame; numerical envelope bounds are UNDECIDED |
| Causal-phase complex $`(X,R,\Theta)`$: causal order + U(1) transport as a nilpotent matrix $`W=Re^{i\Theta}`$; Hasse criteria, Wilson interference identity, gauge invariants; null radiative scaffold vs. timelike condensation | Causal Phase Program v3.9 (§§1–2; Registry items 1–2) | FOLLOW as formal algebra within the model; physical realization of the continuum limit is UNDECIDED (Protocol V1) |
| Physical-radion branch (H_R) / 5D KK; fixed microscopic dimensions postulated prior to kernel factorization | KK–Jacobson Commutativity Note (historical); CPP v3.9 Registry item 20 | NULL (frozen August 2026) |
| Structuring triad $`(\mathcal{I}_A,\partial A,\mathcal{E}_A)`$; indivisibility criterion; interface recoverability bound; precision sparsity and boundary kernel-inclusion synchronization | CPP v3.9 (§2; Registry items 3–4) | FOLLOW as definitions and exact Gaussian identities; numerical certification in Protocol V7 |
| Binary-diamond selection $`K^{\mathrm{eff}}_{xy}=2`$; transverse $`SU(2)\to SO(3)`$ algebra; minimal $`3+1`$ architecture | CPP v3.9 (Thm 3.1, §3.3; Registry items 6–7, 13) | FOLLOW as theorems under stated assumptions; spontaneous emergence of $`3+1`$ is UNDECIDED (Protocol V1) |
| Helmholtz decomposition; solenoidal acceleration of relaxation $`\gamma(Q)\ge\gamma(0)`$ | CPP v3.9 (Prop 3.2; Registry item 8) | FOLLOW as theorem; numerical certification in Protocol V7(b) |
| Oseledets–Landauer bridge: erasure flux $`\dot I_{\mathrm{erase}}\ge(\kappa-h_{\mathrm{KS}})/\ln 2`$ across $`\partial^+A`$ | CPP v3.9 (Thm 4.1; Registry items 9, 14) | FOLLOW under stated stationarity assumptions; physical correspondence to radiation flux is UNDECIDED (Protocol V2) |
| Operational time as ratio of holonomy cycles; combinatorial Lorentzian signature; integrator chains $`\to`$ second-order inertia; synchronization criterion and ball instability $`\tau_{\mathrm{sync}}=\Theta(N^{3/d})`$ | CPP v3.9 (§5; Registry items 10–11, 17) | FOLLOW as mathematical results; universal filamentary architecture (cosmic web $`\leftrightarrow`$ neural networks) is UNDECIDED (Protocol V5) |
| Exact balance identity of coherent diamonds; phase-mediated void rarefaction (H-LG, effective dark energy); interface synchronization-shell tension (effective dark matter); three-component Einstein–Maxwell decomposition | CPP v3.9 (§6; Registry items 12, 15–16); historical $`\Gamma_{\mathrm{corr}}`$ formulation: CPG v2.0 | Balance identity FOLLOW; dynamical mechanism and continuum decomposition UNDECIDED (Protocols V3–V4); observational contact (SPARC, DESI/DES-SN5YR) deferred to the post-v0.3 stage per CPG v2.0 §5.1 |
| Interface saturation $`\eta_{\mathrm{sat}}\ge1`$: horizon screening and interior high-rank phase $`K^{\mathrm{eff}}_{xy}\ge3`$ | CPP v3.9 (§6.3; Registry item 18) | UNDECIDED (Protocol V6) |
| Relative-entropy (Dorau–Much [25] / Araki–Uhlmann / Casini) route to gravity | CPG v2.0 (historical); CPP v3.9 References item 3 | Historical frame; superseded as the primary thermodynamic bridge by the Oseledets–Landauer theorem (Thm 4.1); the classical KL proxy of the frozen pilot v0.2 was never executed |
| Space of Algebras (Level 0) | The Algorithm of Being (§2); this document (§3.1) | UNDECIDED: a conjecture, not a foundation |
| Modified Brusentsov entailment logic; four-valued verdict calculus $`V_4`$ (FOLLOW / OMIT / NULL / UNDECIDED) with dominance semilattice; MDNF of conditional entailment; typed certificates; ensemble law quantifiers; metric, box, and graph realizations | Modified_Brusentsov_Entailment_Logic.md (October 2026) | FOLLOW: formal specification — the canonical reference for verdict semantics corpus-wide (theorems proven internally); implementation conformance and empirical validation per its §7.3 are UNDECIDED |
| Ternary requirement semantics; authority hierarchy | Unified Implementable Model v2.0 | FOLLOW: specified |
| External verifier; FOLLOW/OMIT/NULL/UNDECIDED; FalseFollowRate | External Ternary Judge Adapter; Draft: ternary_judge.md; canonical verdict semantics: [26] | FOLLOW: protocol; preliminary controlled-corpus MVP empirics exist (Reasoning/Draft/ternary_judge.md, run of 2026-08-09: FFR 0.362 → 0.035 at coverage 0.81; effect depends primarily on judge competence); open-domain transfer is UNDECIDED and remains in the §8 program |
| Agent V10.9 (Tri-Agent, Brusentsov 4-valued verdicts) | ARCHITECTURAL / ENGINEERING SPECIFICATION (Version 10.9) | FOLLOW: specification; the ARC-AGI-3 benchmark is in the §8 program |
| Controlled self-development of a language model under an external verifier (capability growth at bounded structural continuity) | Self-Developing Runtime Research Program v0.2 (2026-09-11) | UNDECIDED: pre-implementation specification; success/failure criteria and control groups fixed |
| Latent Agency Framework: graded agency (integration, persistence, informational autonomy); relief vs reasoning budget; recoverability bound and kernel-inclusion synchronization; Helmholtz decomposition and integrator-chain truncation of boundary dynamics; ten measurable predictions | Latent_Agency_Framework.md (v2.1, 2026-10-21; successor to LAF v2.0 and Unified Latent Space of Consciousness v1.0) | UNDECIDED: working hypothesis; predictions untested; stationary Markov-blanket mechanics is a necessary boundary kinematics, not a sufficient agency criterion; the hard problem is bracketed |
| Informational minimal surfaces: $`\mathbf{H} = \lambda(\nabla i)^\perp`$ as stationary condition; VIM surrogates bound the variational functional | Latent Information Structuring | UNDECIDED: active experimental program (E1–E5); mathematical framework is FOLLOW |
| Kernel-path quotient realization of $`V_4`$; tangent-space diagnostics as geometric evidence; exact and smooth cumulative-coordinate semilattice aggregation | Spectral and Matrix Realization of $`V_4`$ in Latent Spaces (v2.2, 2026-10-17) | FOLLOW as formal construction under stated assumptions; existence/learnability of the required kernel geometry and empirical certification of projectors remain UNDECIDED |

The rule for reading the archive: **status is attached to the thesis, not to the document.** A document may be technically complete (FOLLOW as a specification) while recording open questions (UNDECIDED as empirics). Conflating these statuses is the same error as passing a prediction off as an observation.

---

## **8. Experimental Program**

### **8.1. Physics**

- **Frontal program: protocols V1–V7 (CPP v3.9 §7).** Graph-level computational tests with pre-registered pass/fail thresholds and control ensembles: V1 binary-diamond collapse and dimension selection; V2 Oseledets contraction vs. interface flux; V3 phase-mediated void rarefaction; V4 interfacial synchronization shell; V5 compact→filamentary transition; V6 horizon saturation; V7 kernel inclusion, solenoidal gap, integrator truncation. Reference implementation: CPP v3.9 §9 (Python / NumPy / SciPy). The $`V_4`$ Registry (§8 of v3.9) is updated according to protocol outcomes.
- **Executable specification: pending.** Technical Specification v0.2 (Mode A/B budget-conserving pilot; null tests D1–D8) is frozen and was never executed; its Mode B targeted the same condensation–rarefaction mechanism now tested by Protocol V3. Technical Specification **v0.3**, implementing V1–V7, is planned and not yet created. A closed report remains the gate: until it exists, no empirical claim of the physics program is certified.
- **Deferred observational stage.** Protocols V1–V7 are purely graph-level. The observational falsification criteria formulated in the historical CPG v2.0 §5.1 (a single capacity parameter spanning both SPARC rotation curves and $`H(z)`$; the supernova time-dilation scaling $`\Delta t_{\mathrm{obs}}=(1+z)\Delta t_{\mathrm{em}}`$) remain program commitments for the post-v0.3 continuum-contact stage. If a protocol reaches its refutation criterion, the corresponding Registry items 13–18 of v3.9 close as NULL and the observational stage is void.

### **8.2. Engineering**

- **FalseFollowRate.** Primary metric of the verifier-centric architecture: the fraction of transitions certified as FOLLOW that fail the constraint under independent checking. A preliminary live MVP on a controlled corpus (Reasoning/Draft/ternary_judge.md, run of 2026-08-09) reports an order-of-magnitude reduction relative to binary baselines (0.362 → 0.035 at coverage 0.81), with an ablation showing that the primary factor is judge competence and the certificate contract is its multiplier. Remaining goal: reproduce the effect on open domains and in the full adapter deployment, via first-class OMIT/UNDECIDED.
- **ARC-AGI-3.** Agent V10.9 is run on the benchmark; the criteria are not only task success but calibration (the match between declared confidence and observed accuracy), isolation integrity, and the share of honest UNDECIDED / OMIT versus fabricated FOLLOW.
- **Ternary Judge track.** The controlled-corpus MVP is complete (see above). Remaining: independent evaluation of the adapter on open domains — rule-interpreter stability across a change of proposer, absence of semantic drift in verdicts, graph persistence (OMIT-node retention, re-verification with rollback), and binary certificates for contradictions. The canonical certificate algebra of [26] (§5.3) supplies the target forms for the two missing certificate types: polarized scoped-exhaustion certificates $`\mathcal{C}^{\emptyset}`$ for absence claims and binary quote-pair certificates $`\mathcal{C}^{\bot}`$ for contradictions; conformance testing of the six-step cascade and of the exhaustion invariant (an UNDECIDED record is never rewritten into NULL, §5.4 of [26]) is added to this track.
- **Latent geometry track.** Experimental program E1–E5 from *Latent Information Structuring*: projection of curvature onto information gradient ($`r > r_0`$), curvature dynamics during training, stratification at metric degeneracies, NTK-filtered dynamics correlation, comparison of standard CE training versus explicit VIM surrogate optimization. This track tests whether the neural substrate of the agent self-organizes according to the informational minimal surface principle. Complementary checks required by *Spectral and Matrix Realization of $`V_4`$* [27]: validation of estimated kernel distributions against $`\ker d\pi_\ell`$, numerical projector idempotence/orthogonality under the declared positive-definite metric $`h`$, preservation of $`\pi_\ell`$ along admissible kernel paths, cross-scale equivalence compatibility, and crisp-limit recovery of the MBEL cascade (including inactive-clause immunity and Axiom 4.1 empty-active-clause guard).

### **8.3. Ontology**

The philosophical level has no direct experiment but has an indirect one: **consistency**. If the physics program is falsified, the ontology must revise the corresponding sections; if the engineering metrics show that ternary semantics does not reduce FalseFollowRate, the linked theses lose their operational support and revert to hypothesis status. This document records these dependencies explicitly, so that falsification at one level automatically demotes the linked theses at the others.

---

## **9. What This Document Does Not Claim**

1. **It does not claim identity of levels.** The §6 isomorphism is a homology of forms of constraint, not an ontological identification. An agent is not a universe; logic is not physics.
2. **It does not claim that the Space of Algebras is a foundation.** Level 0 is a conjecture with the status UNDECIDED, a promissory note whose fate is tied to the falsifiable causal-phase program (Level 1). Until Level 1 is closed, the Level 0 construction is an abstraction for notational convenience.
3. **It does not claim novelty for the triad as such.** The “information–energy–time” pairs are old (Landauer, Margolus–Levitin, Mandelstam–Tamm). The novelty — if any — lies in binding the triad to a concrete physics program and to an executable engineering semantics.
4. **It does not claim a solution to the hard problem of consciousness.** The “recursive modeling under external verification” frame is architectural, not phenomenological. Qualia lie outside this framework’s competence.
5. **It does not claim substrate independence for consciousness.** It claims substrate-parameterization: the architecture of consciousness is realized only within the constraint envelope of a material carrier, and that carrier is the interface to the external verifier.
6. **It does not claim that any physical hypothesis of the program has been tested.** The exact mathematical results of Causal Phase Program v3.9 are FOLLOW within the model; all its physical hypotheses (Registry items 13–18) are UNDECIDED pending protocols V1–V7, for which no executable specification exists yet (Technical Specification v0.3 is pending; v0.2 is frozen and was never executed). The historical $`\Gamma_{\mathrm{corr}}`$ functional of CPG v2.0 has never been computed or fitted to data.
7. **It does not claim completeness.** The document is a snapshot as of the version date. The §7 statuses are subject to revision per the §8 results, in both directions: UNDECIDED may become FOLLOW, and FOLLOW may become NULL.

---

## **Appendix. Archive Document Correspondence**

| File | Level | Language | Role in the framework |
| :--- | :--- | :--- | :--- |
| The Algorithm of Being (Revised) | Ontology | EN | The philosophical frame: triad, kernel, consciousness under verification, substrate envelope |
| Causal Phase Program v3.9 (Oct 21, 2026; `Physics/Causal_Phase_Program_v3.md`) | Physics | EN | Active formal specification and research program: structuring triad $`(\mathcal{I}_A,\partial A,\mathcal{E}_A)`$, binary-diamond selection $`K^{\mathrm{eff}}=2`$, Oseledets–Landauer bridge, three-component Einstein–Maxwell decomposition, horizon saturation, protocols V1–V7, $`V_4`$ registry, reference implementation; supersedes CPG v2.0 |
| Causal-Phase Geometry Research Program v2.0 (Oct 17, 2026) | Physics | EN | Historical predecessor of v3.9; source of the $`\Gamma_{\mathrm{corr}}`$ continuum formulation, the $`\mathrm{sLSE}_T`$ aggregation bridge, and the observational falsification criteria (SPARC / DESI / DES-SN5YR) |
| Technical Specification v0.2 (consolidated) | Physics | EN | Frozen historical pilot design: Mode A (frozen topology) + Mode B (budget-conserving rewiring); observables $`\Delta F`$, $`\Delta N_\partial`$, $`\delta\rho_{\mathrm{void}}`$, $`z_{\mathrm{void}}^{m eff}`$; null tests D1–D8; never executed; to be replaced by v0.3 (pending) |
| KK–Jacobson Commutativity Note | Physics | EN | Historical (5D route frozen August 2026; NULL per CPP v3.9 Registry item 20) |
| Modified Brusentsov Entailment Logic and Four-Valued Verdict Calculus (`Reasoning/Modified_Brusentsov_Entailment_Logic.md`) | Reasoning (formal logic) | EN | Canonical formal foundation of verdict semantics corpus-wide: MDNF, $`V_4`$ and dominance semilattice, decision cascade, evidence scopes, typed certificates, ensemble law quantifiers, metric/box/graph realizations |
| Unified Implementable Model v2.0 | Engineering | EN | The agent’s architectural ontology |
| External Ternary Judge Adapter | Engineering | EN | The external-verification protocol |
| ARC-AGI-3 LCLD Agent: Architectural + Engineering Specifications (Version 10.9) | Engineering | EN | The V10.9 instantiation (Tri-Agent, isolated memory contours, Brusentsov 4-valued verdict logic; aligned to the canonical specification [26]) |
| The Law of Useful Information Structuring in Model Latent Spaces (`Reasoning/Latent_Information_Structuring.md`) | Reasoning (substrate geometry) | EN | Geometric theory of latent representations: variational principle, VIM surrogates, NTK-filtered dynamics, experimental program (E1–E5) |
| Spectral and Matrix Realization of $`V_4`$ in Latent Spaces (`Reasoning/Spectral_and_Matrix_Realization_of_V4.md`) | Reasoning (geometry ↔ logic) | EN | Continuous geometric realization of the $`V_4`$ verdict calculus: kernel-path quotients, tangent-space diagnostics as evidence for MBEL, exact and smooth semilattice aggregation; normative parent = [26] §§3–6 |
| Latent Agency Framework (v2.1, Oct 21, 2026) | Reasoning | EN | Working hypothesis: latent-space agency (integration, persistence, autonomy); relief vs budget; recoverability bound and kernel-inclusion synchronization; Helmholtz decomposition and integrator-chain truncation; ten measurable predictions; hard problem bracketed. Successor to LAF v2.0 and Unified Latent Space of Consciousness v1.0 |
| Self-Developing Runtime Research Program v0.2 | Reasoning | EN | Pre-implementation specification: controlled self-development of an LLM under an external verifier, with control groups and success/failure criteria |
| Draft: Propose, Judge, Commit (ternary_judge.md); Hierarchical Ternary KG as RAG Alternative | Reasoning (drafts) | EN | Working drafts, not catalogued as formal deliverables: the judge architecture with preliminary MVP results; ternary hierarchical knowledge graph as a RAG alternative |
| Unified Informational-Constructive Framework (this document) | Synthesis | EN | The map of theses, statuses, and cross-level dependencies |

---

## **References**

- [6] V. Yakunin, *Causal Phase Program, Version 3.9* (October 21, 2026); this repository, `Physics/Causal_Phase_Program_v3.md` — the active physics specification (supersedes the Causal-Phase Geometry Research Program drafts of August–October 2026; v2.0 is retained in the repository as historical).
- [7] V. Yakunin, *Causal Structure, U(1) Holonomies, and the Thermodynamic Origin of the Einstein–Maxwell System* (2026).
- [8] V. Yakunin, *Unified Implementable Model, Version 2.0: Verifier-Centered Latent World Models with Evidence-Grounded Three-Way Semantics* (2026).
- [9] V. Yakunin, *External Ternary Judge Adapter for OpenClaw and DeepSeek V4 API: Engineering Whitepaper* (2026).
- [10] V. Yakunin, *ARC-AGI-3 LCLD Agent: Architectural Specification and Engineering Specification* (2026).
- [11] N. P. Brusentsov, *Usovershenstvovanie logiki umozaklyucheniy* [The Improvement of Inference Logic], Fond “Novoe tysyacheletie”, Moscow, 2012.
- [12] R. Landauer, “Irreversibility and Heat Generation in the Computing Process,” *IBM Journal of Research and Development* 5, 183–191 (1961).
- [13] N. Margolus, L. B. Levitin, “The Maximum Speed of Dynamical Evolution,” *Physica D* 120, 188–195 (1998).
- [14] L. Mandelstam, I. Tamm, “The Uncertainty Relation Between Energy and Time in Non-Relativistic Quantum Mechanics,” *Journal of Physics (USSR)* 9, 249–254 (1945).
- [15] J. D. Bekenstein, “Universal Upper Bound on the Entropy-to-Energy Ratio for Bounded Systems,” *Physical Review D* 23, 287–298 (1981).
- [16] N. Tishby, F. C. Pereira, W. Bialek, “The Information Bottleneck Method,” in *Proceedings of the 37th Annual Allerton Conference on Communication, Control and Computing*, 368–377 (1999).
- [17] E. P. Hoel, L. Albantakis, G. Tononi, “Quantifying Causal Emergence Shows That Macro Can Beat Micro,” *Proceedings of the National Academy of Sciences* 110, 19790–19795 (2013).
- [22] A. Connes, *Noncommutative Geometry*, Academic Press, 1994.
- [23] A. Connes, “Gravity Coupled with Matter and the Foundation of Non-commutative Geometry,” *Communications in Mathematical Physics* 182, 155–176 (1996).
- [24] A. Connes, C. Rovelli, “Von Neumann Algebra Automorphisms and Time-Thermodynamics Relation in Generally Covariant Quantum Theories,” *Classical and Quantum Gravity* 11, 2899–2917 (1994).
- [25] P. Dorau, A. Much, “From Quantum Relative Entropy to the Semiclassical Einstein Equations,” *Physical Review Letters* (2026); arXiv:2510.24491.
- [26] V. Yakunin, *Modified Brusentsov Entailment Logic and Four-Valued Verdict Calculus for External State-Control Systems* (2026); this repository, `Reasoning/Modified_Brusentsov_Entailment_Logic.md` — the canonical reference for verdict semantics across the corpus.
- [27] V. Yakunin, *Spectral and Matrix Realization of $`V_4`$ in Latent Spaces* (2026); this repository, `Reasoning/Spectral_and_Matrix_Realization_of_V4.md` — geometric/matrix realization of the four-valued verdict calculus on latent state spaces (kernel-path quotients, tangent diagnostics, cumulative semilattice).

---

*End of document. Version 1.8. Feedback and objections — via repository issues.*
