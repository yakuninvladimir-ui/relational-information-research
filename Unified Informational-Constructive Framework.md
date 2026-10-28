# **Unified Informational-Constructive Framework**

**Author:** Vladimir Yakunin  
**Version:** 2.1  
**Date:** 2026-10-22 (v2.1 revision; v2.0: 2026-10-22; v1.9: 2026-10-22; v1.8: 2026-10-21; v1.7: 2026-10-17; v1.6: 2026-10-17; v1.5: 2026-10-14; v1.4: 2026-10-13; v1.3: 2026-10-05; v1.2: 2026-09-23)  
**Status:** archive synthesis document; aligned with the revised edition of “The Algorithm of Being” (2026), the Causal Phase Program v4.0 (October 22, 2026; unified Gaussian model, hard locality constraints, exact entropy balance, exact field back-reaction on the graph, protocols V1–V7 with executed identity-level checks), Technical Specification v0.4 (October 22, 2026; the active executable specification of protocols V1–V7), the geometric theory of latent representations (September 2026), the ARC-AGI-3 LCLD Agent specifications V10.9 (October 2026), the Latent Agency Framework v2.1 (October 21, 2026), the Self-Developing Runtime Research Program v0.2 (September 2026), the canonical Modified Brusentsov Entailment Logic specification (October 2026), the Spectral and Matrix Realization of V₄ in Latent Spaces v2.2 (October 17, 2026), the Boundary Projection Theorem (October 22, 2026; geometric core of the verdict layer at the point/ball level), and the preliminary ternary-judge MVP results (August 2026)

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

The archive’s physics program admits no external global time: proper time is defined along worldlines; in discrete kinematics it is estimated by an internal combinatorial clock — accumulated phase cycles in CPP v4.0 (§5.1) [6], maximal-chain length in the earlier continuum-oriented formulations (removed from the repository). Only **ratios of rates** are observable. The general redshift formula of the continuum limit (standard relativistic kinematics; its discrete counterpart is the phase-cycle ratio $`R^{(\ell)}_{AB}`$ of [6], defined only at $`\Delta N_B^{(\ell)}\ne0`$) is literally a comparison of two clocks (null-transported phase against the local time directions of emitter and observer):

```math
1+z = \frac{(-u^\mu k_\mu)_{\mathrm{em}}}{(-u^\mu k_\mu)_{\mathrm{obs}}}
```

In the Causal Phase Program v4.0 (§5.1) this becomes fully combinatorial: relative operational time between subsystems is the ratio of accumulated gauge-invariant holonomy cycles along worldtubes, $`R^{(\ell)}_{AB}=\Delta N^{(\ell)}_A/\Delta N^{(\ell)}_B`$, and the Lorentzian signature $`(-,+,+,+)`$ is derived — as an explicitly kinematic step-allocation ansatz (UNDECIDED; CPP v4.0 Registry row 14) — from quadratic budget competition between spatial propagation and internal diamond synchronization. An algebraic echo of the same thesis is the Connes–Rovelli thermal time hypothesis [24]: a state on an algebra generates its own time evolution through the modular flow. **The operational content of time is a ratio of rates; the time axis is a derived bookkeeping tool.**

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
| Level 1 — causal-phase complex | Discrete causal order with U(1) holonomies on Hasse links, encoded as a nilpotent transfer matrix $`W_{xy}=R_{xy}e^{i\theta_{xy}}`$; unified Gaussian model $`\Pi=m^2I+L_\Theta`$; admissible ensembles $`\mathcal{A}(\nu,k_{\max})`$; structuring triad $`(\mathcal{I}_A,\partial A,\mathcal{E}_A)`$ | Active program (CPP v4.0): protocols V1–V7; executable specification v0.4 (active); identity-level checks executed (§10) |
| Level 2 — continuum geometry | Lorentzian metric, gauge connection, effective field equations | **OMIT** in CPP v4.0 (Registry row 17): deferred beyond the discrete specification |

The “Space of Algebras” is not a claimed foundation but a deep conjectural layer whose fate is tied to the intermediate one: failure of the causal-phase program by its own criteria demotes the conjecture to a historical footnote.

### **3.2. Fundamental kinematics and the admissible ensemble**

The base structure is a finite (or locally finite) causal set $`(X,\prec)`$ equipped with U(1) holonomies on oriented Hasse links, encoded as a single nilpotent complex **causal-phase transfer matrix**:

```math
W_{xy}=R_{xy}\,e^{i\theta_{xy}},\qquad R_{xy}\in\{0,1\},\quad\theta_{xy}\in[0,2\pi),\quad W^N=0,
```

where $`R`$ is the Boolean Hasse matrix — strictly upper-triangular and transitively irreducible. Irreducibility implies two structural identities: zero waist width on direct links ($`R_{xy}=1 \Rightarrow K_{xy}=(R^2)_{xy}=0`$) and triangle-freeness of the undirected skeleton ($`\operatorname{Tr}((R+R^\top)^3)=0`$). Since $`K_{xy}`$ vanishes on the links themselves, their embeddedness in interference structures is measured by the **diamond-participation multiplicity** $`d_\diamond(x,y)`$ (closed matrix form, CPP v4.0 Def 2.1), which partitions the edges into unbranched null links ($`d_\diamond=0`$) and diamond-embedded structural links ($`d_\diamond\ge1`$); along maximal null chains the phases can be gauged to zero, and at zero temperature any functional of $`(K, J, \|C\|_F, \ln\det\Pi)`$ is minimized by gauge-flat configurations (Prop 1.2). The Wilson interference identity $`\sum_{a<b}(1-\cos\Phi_{ab})=\tfrac12K_{xy}J_{xy}`$ (Prop 1.1) ties diamond holonomies to waist coherence and frustration.

**Admissible ensemble.** The Kleitman–Rothschild asymptotics ($`2^{N^2/4}`$ partial orders, dominated by two- and three-layer configurations) make soft penalties ineffective: on the two-layer sector $`K\equiv0`$, $`J\equiv0`$, $`C=0`$, so any functional $`a\sum K^p + b\sum J + g\|C\|_F^2`$ (and any edge chemical potential) assigns zero cost to the whole swamp (Prop 3.2). The program therefore imposes **hard locality constraints** (L0)–(L4): the Hasse property, diamond covering, connectivity, bounded valency $`k_{\max}`$, and the diamond-density threshold $`N_D \ge \nu N`$ — reducing the entropy to $`\exp(O(k_{\max}N\ln N))`$ (Prop 3.1). The price is stated explicitly: Poisson sprinklings (link count $`N^{2-2/d}`$, Carlip) violate (L3) and are excluded; the program describes regular bounded-valency causal complexes.

The phase layer is treated strictly as an **internal** fibre:

```math
U(1)\hookrightarrow P\xrightarrow{\pi}M_4,\quad\delta\ell_*=0.
```

No free radion, no physical fifth dimension, no KK tower. The competing physical-radion branch (H_R) has been frozen (August 2026) and is catalogued as NULL in §7. Spatial dimensionality is not postulated — and is no longer derived from a single binary diamond either: the directed hypercubic lattice of every $`d\ge2`$ consists entirely of binary diamonds $`K_{xy}\le2`$ (Prop 3.5), so the dimension is encoded in the diamond density $`\binom{d}{2}`$ per vertex and measured empirically by the estimators $`(d_s, d_H, d_\tau)`$. The former “3+1” derivation from the transverse algebra of the binary diamond is **retracted** (CPP v4.0 Registry row 9, NULL). The full formal specification is given in **Causal Phase Program v4.0**.

### **3.3. Unified Gaussian model, exact entropy balance, and the constraint triad**

The historical v2.0 program (removed from the repository) derived gravity through the relative-entropy route (Dorau–Much [25]; Araki–Uhlmann; Casini) with the local bound $`D_{\mathrm{KL}}\le c\,N_\partial`$; its pilot (Tech Spec v0.2, removed) was executed and returned UNDECIDED (glassy freezing; finite-size ambiguity). In CPP v4.0 the continuum route is deferred (OMIT, Registry row 17); the operative content is discrete and exact.

**Unified model (Def 2.4).** A complex Gaussian field on the Hasse graph with magnetic-Laplacian precision $`\Pi(R,\Theta)=m^2I+L_\Theta`$, $`L_\Theta = D-W-W^\dagger \succeq 0`$, and field $`\psi\sim\mathcal{CN}(0,\Pi^{-1})`$; the solenoidal drift $`Q_W=\tfrac\beta2(W-W^\dagger)=i\beta H_{\mathrm{rot}}`$ is the skew-Hermitian part of $`W`$. Markov screening $`\Pi_{\mathcal{I}\mathcal{E}}=0`$ is a theorem of the model (triad locality), the mediated covariance is exact, and the kernel-inclusion criterion $`\ker\Pi_{\mathcal{I},\partial A}\subseteq\ker\Pi_{\mathcal{E},\partial A}`$ acquires a **graph criterion** (Cor 2.3): a boundary vertex without an interior neighbor violates inclusion unconditionally (defect of magnitude $`\sqrt2`$, verified numerically), while injectivity of $`\Pi_{\mathcal{I}b}`$ at generic phases is equivalent to a matching saturating $`\partial A`$ (Edmonds rank).

**Exact entropy balance (Thm 4.3).** For the injective noisy map $`Z_{n+1}=G(Z_n)+\xi_n`$ (Def 4.1; the injectivity condition $`g\|H_A\|_2<1-\delta`$ is Lemma 4.2), stationarity yields the exact identity

```math
\Delta_{\mathrm{noise}} \;=\; -\,\mathbb{E}\ln|\det DG(Z)| \;=\; -\sum_i\lambda_i \;=\; \kappa - h_+,
```

with no SRB or Pesin assumption. It is verified through three independent channels (Benettin QR spectrum; Jacobian average; Kozachenko–Leonenko $`k`$-NN entropies): $`1.602 / 1.603 / 1.600`$ at the reference point (§10). The Landauer reading $`k_BT(\kappa-h_+)`$ and the saturation ratio $`\eta_{\mathrm{sat}}`$ are separated as **Hypothesis H-L** (UNDECIDED, Registry row 12): they require a physical reservoir, temperature, and edge capacity $`c_0`$ external to the discrete model. The triad-level counterpart of the constraint triad remains: distinction, action, and rate are paid across the boundary of every localized structure (recoverability bound Prop 2.1 with capacity $`C(\partial^+A)\le c_0|\partial^+A|_E`$).

### **3.4. Field back-reaction on the graph: exact closure**

Integrating out the Gaussian field fixes the bosonic sign and the joint co-evolution functional:

```math
\mathscr{F}_{\mathrm{joint}}(R,\Theta) = F_{\mathrm{struct}}(R,\Theta) + \eta_{\mathrm{field}}\ln\det\Pi(R,\Theta), \qquad \eta_{\mathrm{field}} > 0 \;(\text{canonical point } 1).
```

Three exact results close the graph↔field dynamics (CPP v4.0 §6.2–6.3; all verified to machine precision in §10):
1. **Rank-1 factorization and the Woodbury law (Prop 6.2):** $`L_\Theta=\sum_e v_ev_e^\dagger`$; for an M1 edge swap, $`\det\Pi'/\det\Pi = (1-r_{\mathrm{eff}}(e_-))(1+r_{\mathrm{eff}}(e_+)) + |v_{e_-}^\dagger\Sigma v_{e_+}|^2`$ exactly, with $`0<r_{\mathrm{eff}}(e_-)<1`$ — a non-local, field-mediated interaction between the removed and added edges; the phase gradient is $`\partial\ln\det\Pi/\partial\theta_{xy}=2\operatorname{Im}(e^{i\theta_{xy}}\Sigma_{yx})`$.
2. **Loop expansion (Prop 6.3):** an absolutely convergent series ($`\|T_\Theta\|_2\le d_{\max}/(m^2+d_{\max})<1`$); orders $`\ell=1,2,3`$ are phase-inert (Hasse graphs are triangle-free); the leading phase physics lives at $`\ell=4`$ in two classes of 4-cycles — causal diamonds and bipartite crowns $`K_{2,2}`$ (visible even where $`K\equiv0`$); the diamagnetic bound $`\ln\det\Pi(R,\Theta)\ge\ln\det\Pi(R,0)`$ holds with equality only for flat connections.
3. **Triadic Schur decomposition (Prop 6.4):** $`\ln\det\Pi = \ln\det\Pi_{\mathcal{I}}+\ln\det\Pi_{\mathcal{E}}+\ln\det S_{\partial A}`$ with the strictly positive interface functional $`\mathscr{S}_{\mathrm{interface}}>0`$ — the exact object measured by V3/V4.

**Physical hypotheses (UNDECIDED, Registry row 16; Protocols V3–V4):** equilibrium field-driven void rarefaction ($`\Delta f_{\mathrm{null}}>0`$ at $`\eta_{\mathrm{field}}>0`$) and long-range defect interaction $`V_{\mathrm{int}}(r_{AB})`$. These replace both the historical $`\Gamma_{\mathrm{corr}}`$ machinery of v2.0 and the three-component Einstein–Maxwell decomposition with $`\Lambda_{\mathrm{eff}}[I_{\mathrm{erase}}]`$ and the post-horizon phase of v3.9: the entire continuum layer — including the mean-curvature balance — is now **OMIT** (Registry row 17), outside the discrete specification. The dark-sector narrative is no longer part of the program.

### **3.5. Computational verification program**

The frontal program is **protocols V1–V7** (CPP v4.0 §7) under the active **Technical Specification v0.4**: V1 admissible ensembles (hard constraints, three penalty families, dimension estimators); V2 the exact entropy balance via three independent channels; V3 equilibrium graph restructuring under exact Woodbury ratios; V4 the Schur interface functional and defect interaction; V5 the architecture of synchronizable graphs against expanders (pre-registered topology classifier); V6 kernel inclusion via the graph criterion; V7 mediated covariance, solenoidal gap, integrator truncation.

**Executed checks (CPP v4.0 §10).** The identity-level verifications are already performed and ship with the document — 15 self-test checks of the reference implementation (`run_self_test()`): $`d_\diamond`$ against brute-force enumeration (0 mismatches on 40 graphs), Wilson $`9\cdot10^{-16}`$, hypercube densities $`1,3,6,10 = \binom{d}{2}`$, exact screening, the $`\sqrt2`$ inclusion defect, the entropy balance $`1.602/1.603/1.600`$, Woodbury and Schur to machine precision, the loop expansion, and the gauge-flat diagnostics of $`f_{K^{\mathrm{eff}}=2}`$ ($`0.000/0.167/0.958`$). These certify the mathematics and the implementation — not the physical hypotheses.

**Predecessors.** Tech Spec v0.2 was executed and returned UNDECIDED (glassy freezing of stochastic rewiring; finite-size ambiguity) — v0.4 removes the freezing mechanism by construction (equilibrium Metropolis with exact determinant ratios instead of stochastic rewiring); Tech Spec v0.3 (written for v3.9) was superseded before execution. Both are removed from the repository. The closed automated report `REPORT_v0.4.md` remains the gate: until it exists, no empirical claim of the physics program is certified.

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


The verdict layer itself has a compact geometric core: the *Boundary Projection Theorem* (`Reasoning/Boundary_Projection_Theorem.md`) derives the four verdicts from the position of the observation confidence ball relative to the contract kernel and target cone (Theorem 2.1), gives the certified-narrowing dynamics and the geometric form of the non-promotion rule, and imports the aggregation laws of [27] unchanged. It is a derived semantics of [26] at the declared point/ball scope, not a replacement of the cascade; the cross-layer kernel-inclusion unification it sketches is a homology claim (UNDECIDED).

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
| **Structuring triad** | Internal relief $`\mathcal{I}_A`$ / bilateral interface $`\partial A`$ / external channel $`\mathcal{E}_A`$; kernel-inclusion synchronization (CPP v4.0 §2) | Markov blanket: internal / boundary / external states; recoverability bound (LAF v2.1 §8) | Isolated memory contours and the authority boundary: committed state / verification interface / untrusted proposals (V10.9) |
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
| Causal-phase complex $`(X,R,\Theta)`$: Hasse identities ($`K_{xy}=0`$ on links; triangle-free skeleton), Wilson identity, diamond-participation multiplicity $`d_\diamond(x,y)`$; null radiative scaffold vs diamond-embedded links | Causal Phase Program v4.0 (§§1–2; Registry row 1) | FOLLOW as formal algebra; cross-checked against brute-force diamond enumeration (§10) |
| Gauge-flat configurations are inert for $`K, J, \|C\|_F, \ln\det\Pi`$ (Prop 1.2) | CPP v4.0 (§1.5; Registry row 2) | FOLLOW; consequence: zero-temperature minimizers are flat absent frustration sources |
| Physical-radion branch (H_R) / 5D KK | KK–Jacobson Commutativity Note (historical) | NULL (frozen August 2026); in v4.0 dimensionality is measured, not postulated |
| Structuring triad $`(\mathcal{I}_A,\partial A,\mathcal{E}_A)`$; integration criterion (graph-cut nature); interface recoverability bound | CPP v4.0 (§§2.2–2.3; Registry row 3) | FOLLOW as definitions and the data-processing inequality |
| Unified Gaussian model $`\Pi = m^2I + L_\Theta`$; Markov screening; mediated covariance; kernel inclusion with the graph matching criterion (Cor 2.3) | CPP v4.0 (§2.4; Registry row 4) | FOLLOW (Edmonds rank; the $`\sqrt2`$ defect at an isolated boundary vertex verified numerically) |
| Admissible ensemble $`\mathcal{A}(\nu,k_{\max})`$; entropy bound; impossibility of suppressing the two-layer sector by soft penalties (Props 3.1–3.2) | CPP v4.0 (§3.2; Registry row 5) | FOLLOW; that a physical substrate realizes (L1)–(L4) and the convex penalty is UNDECIDED (row 6, Protocol V1) |
| Interval-local path equivalence; conditional $`K^{\mathrm{eff}}=2`$ at fixed $`J_0>0`$ (Prop 3.3); no selection without a lower threshold (Cor 3.4) | CPP v4.0 (§3.3; Registry row 7) | FOLLOW (ansatz-conditional) |
| Binary diamonds tile lattices in every dimension $`d\ge2`$; dimension encoded in the density $`\binom{d}{2}`$ (hypercube, Prop 3.5) | CPP v4.0 (§3.4; Registry row 8) | FOLLOW (explicit construction; densities $`1,3,6,10`$ verified) |
| Derivation of “3+1” spatial directions from a single binary diamond (v3.9 §3.3) | CPP v4.0 Registry row 9 | NULL — retracted by the hypercube counterexample |
| Stationarity of $`\mathcal{CN}(0,\Pi^{-1})`$ under $`Q_W`$; $`\gamma(Q)\ge\gamma(0)`$; strict acceleration for $`Q_W`$ | CPP v4.0 (Prop 3.6; Registry row 10) | FOLLOW (items 1,2,4); strict acceleration UNDECIDED, numerically confirmed on a 48-node lattice (Protocol V7) |
| Exact stationary entropy balance $`\Delta_{\mathrm{noise}}=-\sum_i\lambda_i=\kappa-h_+`$ (Benettin spectrum; Kozachenko–Leonenko entropies) | CPP v4.0 (Thm 4.3; Registry row 11) | FOLLOW; verified via three independent channels (§10) |
| Landauer thermodynamic reading (H-L) and the physical saturation threshold $`\eta_{\mathrm{sat}}\ge1`$ | CPP v4.0 (Registry row 12) | UNDECIDED: requires an external reservoir, temperature, and edge capacity $`c_0`$ |
| Integrator chains in the non-empty window $`(\gamma_3^{-1},\gamma_2^{-1})`$; ball synchronization divergence $`\Theta(N^{3/d})`$; the expander alternative | CPP v4.0 (§5; Registry row 13) | FOLLOW; filamentary-vs-expander architecture is UNDECIDED (row 13b, Protocol V5) |
| Quadratic step-allocation ansatz; Lorentzian signature; identification of $`\omega_A`$ and $`R_{AB}^{(\ell)}`$ (at $`\Delta N_B\ne0`$) with physical clock rates | CPP v4.0 (§5.1; Registry row 14) | UNDECIDED: kinematic ansatz and continuum-limit hypothesis |
| Rank-1 factorization; exact Woodbury edge-swap law; loop expansion with diamonds and $`K_{2,2}`$ crowns; diamagnetic bound; triadic Schur decomposition with $`\mathscr{S}_{\mathrm{interface}}>0`$ | CPP v4.0 (§6; Registry row 15) | FOLLOW; verified to machine precision ($`<10^{-14}`$) |
| Equilibrium field-driven void rarefaction $`\Delta f_{\mathrm{null}}>0`$ and long-range defect interaction $`V_{\mathrm{int}}(r_{AB})`$ | CPP v4.0 (Registry row 16) | UNDECIDED (Protocols V3–V4) |
| Continuum Einstein equation with $`\Lambda_{\mathrm{eff}}`$, post-horizon phase $`K^{\mathrm{eff}}\ge3`$, mean-curvature balance | CPP v4.0 (Registry row 17) | OMIT — outside the discrete specification |
| Defects of v3.9 and its drafts ($`H_{\mathrm{out}}`$ from the identity; SVD instead of Lyapunov; empty scale window; $`0/0`$ in $`R_{AB}`$; union-find without twins; passive-blanket agency) | CPP v4.0 (Registry row 18) | NULL — eliminated and prohibited |
| Relative-entropy route to gravity (Jacobson / Dorau–Much [25]) | Historical (CPG v2.0, removed); CPP v4.0 References item 3 | Historical frame; outside the current discrete program |
| Space of Algebras (Level 0) | The Algorithm of Being (§2); this document (§3.1) | UNDECIDED: a conjecture, not a foundation |
| Modified Brusentsov entailment logic; four-valued verdict calculus $`V_4`$ (FOLLOW / OMIT / NULL / UNDECIDED) with dominance semilattice; MDNF of conditional entailment; typed certificates; ensemble law quantifiers; metric, box, and graph realizations | Modified_Brusentsov_Entailment_Logic.md (October 2026) | FOLLOW: formal specification — the canonical reference for verdict semantics corpus-wide (theorems proven internally); implementation conformance and empirical validation per its §7.3 are UNDECIDED |
| Ternary requirement semantics; authority hierarchy | Unified Implementable Model v2.0 | FOLLOW: specified |
| External verifier; FOLLOW/OMIT/NULL/UNDECIDED; FalseFollowRate | External Ternary Judge Adapter; Draft: ternary_judge.md; canonical verdict semantics: [26] | FOLLOW: protocol; preliminary controlled-corpus MVP empirics exist (Reasoning/Draft/ternary_judge.md, run of 2026-08-09: FFR 0.362 → 0.035 at coverage 0.81; effect depends primarily on judge competence); open-domain transfer is UNDECIDED and remains in the §8 program |
| Agent V10.9 (Tri-Agent, Brusentsov 4-valued verdicts) | ARCHITECTURAL / ENGINEERING SPECIFICATION (Version 10.9) | FOLLOW: specification; the ARC-AGI-3 benchmark is in the §8 program |
| Controlled self-development of a language model under an external verifier (capability growth at bounded structural continuity) | Self-Developing Runtime Research Program v0.2 (2026-09-11) | UNDECIDED: pre-implementation specification; success/failure criteria and control groups fixed |
| Latent Agency Framework: graded agency (integration, persistence, informational autonomy); relief vs reasoning budget; recoverability bound and kernel-inclusion synchronization; Helmholtz decomposition and integrator-chain truncation of boundary dynamics; ten measurable predictions | Latent_Agency_Framework.md (v2.1, 2026-10-21; successor to LAF v2.0 and Unified Latent Space of Consciousness v1.0) | UNDECIDED: working hypothesis; predictions untested; stationary Markov-blanket mechanics is a necessary boundary kinematics, not a sufficient agency criterion; the hard problem is bracketed |
| Informational minimal surfaces: $`\mathbf{H} = \lambda(\nabla i)^\perp`$ as stationary condition; VIM surrogates bound the variational functional | Latent Information Structuring | UNDECIDED: active experimental program (E1–E5); mathematical framework is FOLLOW |
| Kernel-path quotient realization of $`V_4`$; tangent-space diagnostics as geometric evidence; exact and smooth cumulative-coordinate semilattice aggregation | Spectral and Matrix Realization of $`V_4`$ in Latent Spaces (v2.2, 2026-10-17) | FOLLOW as formal construction under stated assumptions; existence/learnability of the required kernel geometry and empirical certification of projectors remain UNDECIDED |
| Geometric core of the verdict layer: four-verdict theorem from the ball–region trichotomy; refinement monotonicity and geometric non-promotion; stratified `OMIT` kernel; kernel inclusion as the cross-layer preservation form | Boundary_Projection_Theorem.md (v1.0, 2026-10-22) | FOLLOW as derived point/ball semantics of [26] (its §5 rows 1–7); the cross-layer unification and the saturation reading are UNDECIDED (rows 8–9); replacement of the full cascade is out of scope (OMIT, row 10) |

The rule for reading the archive: **status is attached to the thesis, not to the document.** A document may be technically complete (FOLLOW as a specification) while recording open questions (UNDECIDED as empirics). Conflating these statuses is the same error as passing a prediction off as an observation.

---

## **8. Experimental Program**

### **8.1. Physics**

- **Frontal program: protocols V1–V7 (CPP v4.0 §7).** V1 admissible ensembles and dimension; V2 the exact entropy balance (Theorem 4.3) via three independent channels; V3 equilibrium graph restructuring under the exact Woodbury law; V4 the Schur interface functional and defect interaction; V5 synchronizable-graph architecture against expanders; V6 kernel inclusion via the graph criterion; V7 mediated covariance, solenoidal gap, integrator truncation. Reference implementation: CPP v4.0 §9 (`cpp_v40_reference.py` with the `run_self_test()` driver reproducing §10). The $`V_4`$ Registry (v4.0 §8) is updated according to protocol outcomes.
- **Executable specification: Technical Specification v0.4 (October 22, 2026; active).** Phase 0 hard gate: the baseline self-test must pass. Then V6 → V7 (algebra), V2 (dynamics), V3 → V4 (equilibrium co-evolution), V1 (ensembles), V5 (architecture); ≈20–32 h on the target hardware; $`V_4`$ decision rules per MBEL (including `OMIT` for unmet preconditions and the non-promotion rule for `UNDECIDED`); the closed automated report `REPORT_v0.4.md` is the gate for any empirical claim. Predecessors: Tech Spec v0.2 was executed and returned `UNDECIDED` (glassy freezing of stochastic rewiring; finite-size ambiguity); Tech Spec v0.3 was superseded before execution; both removed from the repository.
- **Observational stage: outside the current program.** The continuum layer is `OMIT` (Registry row 17): SPARC/DESI-type contact and the historical $`\Gamma_{\mathrm{corr}}`$ falsification criteria of the removed v2.0 are no longer program commitments; they may return only through a future revision re-entering the continuum.

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
6. **It does not claim that any physical hypothesis of the program has been tested.** The exact mathematical results of Causal Phase Program v4.0 are FOLLOW within the model, and the identity-level checks have been executed (§10; self-test driver). All physical hypotheses (Registry rows 6, 12, 13b, 14, 16) are UNDECIDED pending protocols V1–V7 under the active executable specification v0.4, which has not yet been run. The continuum-level claims (Einstein equations with $`\Lambda_{\mathrm{eff}}`$, dark-sector decompositions, post-horizon phases, mean-curvature balance) are OMIT from the program (Registry row 17); the historical $`\Gamma_{\mathrm{corr}}`$ and three-component formulations belong to removed documents (CPG v2.0, CPP v3.9) and were never fitted to data.
7. **It does not claim completeness.** The document is a snapshot as of the version date. The §7 statuses are subject to revision per the §8 results, in both directions: UNDECIDED may become FOLLOW, and FOLLOW may become NULL.

---

## **Appendix. Archive Document Correspondence**

| File | Level | Language | Role in the framework |
| :--- | :--- | :--- | :--- |
| The Algorithm of Being (Revised) | Ontology | EN | The philosophical frame: triad, kernel, consciousness under verification, substrate envelope |
| Causal Phase Program v4.0 (Oct 22, 2026; `Physics/Causal_Phase_Program_v4.md`) | Physics | EN | Active formal specification and research program: unified Gaussian model $`\Pi=m^2I+L_\Theta`$, hard locality (L0)–(L4) with the Kleitman–Rothschild impossibility theorem, the hypercube counterexample (“3+1” retracted), exact entropy balance (Thm 4.3) with the Landauer reading separated as Hypothesis H-L, exact field back-reaction (Woodbury, loop expansion, Schur), protocols V1–V7, $`V_4`$ registry (18 rows), reference implementation with the executed §10 checks; supersedes v3.9 (removed) |
| Technical Specification v0.4 (Oct 22, 2026) | Physics | EN | Active executable specification of protocols V1–V7: Phase 0 self-test gate, ensemble movers M1/M2/M3, exact-Woodbury equilibrium sampler, pre-registered V5 topology classifier, three inclusion region classes for V6, execution plan ≈20–32 h, $`V_4`$ decision rules, automated `REPORT_v0.4.md`; supersedes v0.3 (removed; superseded before execution) and v0.2 (removed; executed → UNDECIDED) |
| KK–Jacobson Commutativity Note | Physics | EN | Historical (5D route frozen August 2026; NULL per §7); the single retained frozen artifact of the physics corpus |
| Modified Brusentsov Entailment Logic and Four-Valued Verdict Calculus (`Reasoning/Modified_Brusentsov_Entailment_Logic.md`) | Reasoning (formal logic) | EN | Canonical formal foundation of verdict semantics corpus-wide: MDNF, $`V_4`$ and dominance semilattice, decision cascade, evidence scopes, typed certificates, ensemble law quantifiers, metric/box/graph realizations |
| Unified Implementable Model v2.0 | Engineering | EN | The agent’s architectural ontology |
| External Ternary Judge Adapter | Engineering | EN | The external-verification protocol |
| ARC-AGI-3 LCLD Agent: Architectural + Engineering Specifications (Version 10.9) | Engineering | EN | The V10.9 instantiation (Tri-Agent, isolated memory contours, Brusentsov 4-valued verdict logic; aligned to the canonical specification [26]) |
| The Law of Useful Information Structuring in Model Latent Spaces (`Reasoning/Latent_Information_Structuring.md`) | Reasoning (substrate geometry) | EN | Geometric theory of latent representations: variational principle, VIM surrogates, NTK-filtered dynamics, experimental program (E1–E5) |
| Spectral and Matrix Realization of $`V_4`$ in Latent Spaces (`Reasoning/Spectral_and_Matrix_Realization_of_V4.md`) | Reasoning (geometry ↔ logic) | EN | Continuous geometric realization of the $`V_4`$ verdict calculus: kernel-path quotients, tangent-space diagnostics as evidence for MBEL, exact and smooth semilattice aggregation; normative parent = [26] §§3–6 |
| Boundary Projection Theorem (`Reasoning/Boundary_Projection_Theorem.md`) | Reasoning (geometry ↔ logic) | EN | Derived geometric semantics of the verdict layer at the point/ball level: four-verdict theorem, certified narrowing and non-promotion, stratified `OMIT` kernel, aggregation imported from [27], kernel inclusion as the cross-layer preservation form (homology, UNDECIDED); normative parent = [26] |
| Latent Agency Framework (v2.1, Oct 21, 2026) | Reasoning | EN | Working hypothesis: latent-space agency (integration, persistence, autonomy); relief vs budget; recoverability bound and kernel-inclusion synchronization; Helmholtz decomposition and integrator-chain truncation; ten measurable predictions; hard problem bracketed. Successor to LAF v2.0 and Unified Latent Space of Consciousness v1.0 |
| Self-Developing Runtime Research Program v0.2 | Reasoning | EN | Pre-implementation specification: controlled self-development of an LLM under an external verifier, with control groups and success/failure criteria |
| Draft: Propose, Judge, Commit (ternary_judge.md); Hierarchical Ternary KG as RAG Alternative | Reasoning (drafts) | EN | Working drafts, not catalogued as formal deliverables: the judge architecture with preliminary MVP results; ternary hierarchical knowledge graph as a RAG alternative |
| Unified Informational-Constructive Framework (this document) | Synthesis | EN | The map of theses, statuses, and cross-level dependencies |

---

## **References**

- [6] V. Yakunin, *Causal Phase Program, Version 4.0* (October 22, 2026); this repository, `Physics/Causal_Phase_Program_v4.md` — the active physics specification (supersedes v3.9 and the Causal-Phase Geometry Research Program lineage of 2026; historical versions are removed from the repository).
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
- [28] V. Yakunin, *The Boundary Projection Theorem, the Kernel of Insignificance, and the Four-Valued Verdict (Geometric Core of $`V_4`$)* (2026); this repository, `Reasoning/Boundary_Projection_Theorem.md` — derived point/ball-level geometric semantics of the verdict calculus [26]; sibling of [27].

---

*End of document. Version 2.1. Feedback and objections — via repository issues.*
