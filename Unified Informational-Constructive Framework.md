# Unified Informational-Constructive Framework
## Version 1.0

**Author:** Vladimir Yakunin  
**Date:** 2026-08-08  
**Status:** archive synthesis document; aligned with the revised edition of "The Algorithm of Being" (2026)

## 1. Central Thesis

Reality, consciousness, and artificial intelligence are not separate domains but different scales of one and the same process: **self-structuring under constraint**. At every level the same architecture recurs — but not on an abstract "substrate-indifferent" carrier; it runs on a material substrate with its own **constraint envelope** (power, distinction rate, noise, persistence) that parameterizes viable architectures.

| Level | Substrate | What happens |
|---|---|---|
| Physical | Causal network + $U(1)$ holonomies | Spacetime and field emerge as stable regimes of constrained dynamics |
| Ontological | Recursive semantic structures on a biological envelope | Consciousness is a self-model certified by the world through action |
| Engineering | Neuro-symbolic agent on an artificial envelope | A rational agent separates hypothesis generation, selection, and fact fixation |

---

## 2. Basic Definitions

### 2.1. Information as constraint

**Information** is not data but a narrowing of the space of admissible states:

$$\Omega \rightarrow \Omega' \subset \Omega$$

Without constraint, energy dissipates into entropy. With constraint, it forms stable structure. If energy is the capacity for transformation, information is the geometry of admissible transformation.

### 2.2. The constraint triad: distinction, action, rate

Information is not the only fundamental constraint. Three physical results bind information and energy so tightly that neither can serve as the sole primitive:

1. **Erasure has a price.** By Landauer, erasing one bit at temperature $T$ dissipates at least $k_B T \ln 2$ [12]. Forgetting, compression, and filtering the irrelevant are paid thermodynamic operations.
2. **The rate of distinctions is bounded by energy.** The Margolus–Levitin theorem: a system with mean energy $E$ traverses at most $2E/\pi\hbar$ orthogonal states per second [13]; the Mandelstam–Tamm bound: $\Delta t \geq \pi\hbar/(2\Delta E)$ [14].
3. **Information capacity is bounded by energy and size** (the Bekenstein bound) [15].

The fundamental quantities: **distinction** (the bit), **action** ($E \cdot t$, quantum $\hbar$), **causal rate** (the limit $c$). Physics' three conversion constants correspond to the triad's three edges: $c$ — space↔time, $\hbar$ — energy↔frequency ($E = \hbar\omega$), $k_B$ — entropy↔energy.

### 2.3. Time: rate, not axis

The archive's physics program admits no external global time: proper time is defined along worldlines, and in discrete kinematics is estimated by maximal-chain length [6, 7]. Only **ratios of rates** are observable. The general redshift formula is literally a comparison of two clocks (null-transported phase against the local time directions of emitter and observer):

$$1 + z = \frac{(-u^\mu k_\mu)_{\mathrm{em}}}{(-u^\mu k_\mu)_{\mathrm{obs}}}$$

An algebraic echo of the same thesis is the Connes–Rovelli thermal time hypothesis [24]: a state on an algebra generates its own time evolution through the modular flow. **The operational content of time is a ratio of rates; the time axis is a derived bookkeeping tool.**

### 2.4. Operational time

The density of distinctions a system can generate and integrate is paid out of its energy envelope. An honest schema, anchored in Margolus–Levitin:

$$d\mathcal{T} \;\propto\; \frac{\hbar\, dN}{E}\, \eta(M)$$

where $dN$ is the number of orthogonal distinctions generated, $E$ the mean energy, and $\eta(M)$ the architecture's efficiency (the fraction of the physical rate limit actually achieved). The bound is physics; the architectural factor is a schema.

### 2.5. Ternary semantics

Any judgment about a system state takes one of three values:

- **REQUIRED** — the state is necessary for the current task (progress, success).
- **FORBIDDEN** — the state is excluded by constraints (contradiction, impossibility).
- **IRRELEVANT** — the state is admissible but semantically invariant (no-op, noise).

To these is added the epistemic category **UNRESOLVED** — insufficient data for classification. In the judge for LLM reasoning [9], the same discipline takes the form of verdicts FOLLOW / OMIT / NULL / UNDECIDED, where OMIT certifies the semantic invariance of a move.

**Important:** `IRRELEVANT` is neither "false" nor "unknown." It is an explicitly recorded absence of relevance, allowing the system to compress its attention space.

### 2.6. The Algorithm of Being (short form)

$$\text{Distinction} \rightarrow \text{Constraint} \rightarrow \text{Balance} \rightarrow \text{Compression} \rightarrow \text{Meaning} \rightarrow \text{Modeling} \rightarrow \text{Certification} \rightarrow \text{Self-Correction}$$

Or shorter still:

$$\text{Relation} \rightarrow \text{Constraint} \rightarrow \text{Structure} \rightarrow \text{Semantics} \rightarrow \text{Intelligence}$$

---

## 3. The Physical Level: Causal Phase Geometry

### 3.1. The three-layer stack of the program

The archive's physics works with an explicit stack, not a single "foundation":

| Layer | Object | Status |
|---|---|---|
| Level 0 — algebraic substrate | "Space of Algebras" (the Connes lineage: Gelfand duality, spectral triples, thermal time [22–24]) | Conjecture; regulative idea; formalization deferred |
| Level 1 — causal-phase network | Discrete causal order with $U(1)$ holonomies; Wilson functionals; continuum limits | Active program with falsification criteria [6, 7] |
| Level 2 — continuum geometry | Lorentzian metric, gauge connection, thermodynamic equation of state | Established structures [2, 4] |

The "Space of Algebras" is not a claimed foundation but a deep conjectural layer whose fate is tied to the intermediate one: failure of the causal-phase program by its own criteria demotes the conjecture to a historical footnote. The trajectory is the same as Wheeler's "it from bit": a regulative idea becomes productive only by generating intermediate layers.

### 3.2. Fundamental kinematics

The base structure is a locally finite causal set $(\mathcal{C}, \prec)$ with $U(1)$ holonomies on oriented links:

$$ (\mathcal{C}, \prec, U_{xy}) \xrightarrow{\text{coarse-graining}} (\mathcal{M}_4, g_{\mu\nu}, A_\mu) $$

- The causal order fixes the light cones and the conformal class of the metric.
- The volume measure (element count in an interval) fixes the proper-time scale.
- Discrete $U(1)$ transports generate the electromagnetic connection.

### 3.3. Thermodynamic origin

Applying Jacobson's local thermodynamics to five-dimensional KK geometry yields the Einstein–Maxwell equations after reduction. The central condition is **commutativity**: reduction after thermodynamics must give the same result as thermodynamics after reduction [7].

### 3.4. The fixed point

A coarse-graining fixed-point hypothesis is investigated:

$$a_\star(t) \propto t, \quad H_\star = 1/t$$

The observed metric is treated as a non-equilibrium deformation of this point; "synchronization" as the decay of relative entropy toward a stationary state while total entropy keeps growing. This is not a postulate but a diagnostic decomposition requiring independent derivation.

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

$$\pi:\ \Omega_{\mathrm{micro}} \rightarrow \Omega_{\mathrm{macro}}$$

Everything falling into the kernel of $\pi$ is irrelevant for that description. The stable content of a description is what survives the quotient. Physics already uses the word: in the renormalization group, *irrelevant operators* are couplings that decay under repeated coarse-graining; fixed points of the flow are stabilized macrostructures (cf. $a_\star$ in §3.4).

The boundary of the parallel must be stated explicitly: coarse-graining is indexed by **scale**, irrelevance by **goal**. The exact formulation:

> **Irrelevance is goal-indexed coarse-graining; coarse-graining is scale-indexed irrelevance.**

The information bottleneck formalizes the second case (keep about $X$ only what is predictive of the goal $Y$) [16]; causal emergence shows that coarse-graining can be causally *stronger* than the micro-description — compression is not pure loss [17].

Intelligence works not by enumeration but by compression. The third operator $\emptyset$ is ontologically necessary: without it there is no attention, without attention no abstraction, without abstraction no generalization. And it is not free: by Landauer, discarding distinctions is dissipative [12]. **The economics of attention is a thermodynamic economics**; "intelligence is disciplined compression" is a consequence of the triad, not an aphorism.

### 4.4. Substrate as constraint envelope

"Substrate independence" is the wrong slogan. Two questions must be separated:

- **Logical realizability:** architecture is not bound to material — multiple realizability stands.
- **Physical realizability:** any actual realization must fit the envelope: available power, achievable distinction rate, noise floor, thermal stability, memory persistence, a sensorimotor channel to the external verifier.

The correct position is **substrate-parameterization**: substrate matters parametrically, not essentially. The brain is remarkable not as tissue but as an extreme solution of the triad: ~20 W at ~$10^{14}$–$10^{15}$ synaptic events per second. Different envelopes breed different economies of thought: consciousness at datacenter power has a different price for memory, forgetting, and parallelism — its architecture will be structurally deformed relative to the biological one, not merely "faster."

The substrate is also the **interface to the verifier**: a disembodied "pure intellect" lacks any source of certification and inevitably self-confirms. In the archive's ontology, matter is itself stabilized relation, so the relation of consciousness to the brain is **architecture on architecture**: an informational regime carried by a material regime; the meeting point of the information/time and energy/time regimes.

**Honest UNDECIDED:** which envelope parameters are *necessary* (not merely sufficient) for consciousness is unknown; no grounded thresholds exist for power, distinction rate, or recurrence depth.

---

## 5. The Engineering Level

The engineering level is not an illustration of the philosophy but its operational form: the same constraints, written as an executable architecture. Three archive documents cover it at different depths: the **Unified Implementable Model (UIM v2.0)** defines the statics (requirement semantics, authority hierarchy, verification contracts), the **External Ternary Judge Adapter** defines the external-verification interface, and the **ARC-AGI-3 LCLD Agent architectural and engineering specifications (V6.2)** define a concrete instantiation for a task.

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

OMIT is neither an "error" nor a "skip": it is a deliberate decision of non-applicability, logged on equal footing with the rest. The adapter fixes the rule interpreter as an immutable layer: verdict semantics is not subject to further training and does not drift with the model.

### 5.5. Three documents, one hierarchy

| Document | Level of abstraction | What it fixes |
|---|---|---|
| **UIM v2.0** | Architectural ontology | Ternary requirement semantics, the Proposer/Binder/Verifier/Memory hierarchy, verification contracts, evidence scopes (PREDICTIVE_ONLY vs OBSERVED_TRANSITION) |
| **External Ternary Judge Adapter** | Verification protocol | The external-verifier interface, the fixed rule interpreter, the FalseFollowRate metric |
| **ARC-AGI-3 LCLD Agent (V6.2)** | Instantiation | A concrete agent: the epistemic loop, IRRELEVANT as a first-class policy outcome, information_gain_observed as posterior entropy reduction |

The three documents are three nesting levels of one principle: **an agent that is not separated from its verifier has no grounds for trusting its own transitions.** The distinction of evidence scopes (PREDICTIVE_ONLY / OBSERVED_TRANSITION) is the engineering record of a philosophical boundary: a model's prediction is not an observed transition, and conflating these statuses is the source of hallucinations in the most precise sense of the word.

---

## 6. Isomorphism of Levels

The three levels — physical, ontological, engineering — are structurally aligned. The table below fixes the correspondences. The caveat is mandatory: this is a **homology, not an identity** — a structural similarity of forms of constraint on different carriers, not a claim that physics "contains" logic or that an agent "is" a universe.

| Concept | Physical level | Ontological level | Engineering level |
|---|---|---|---|
| Distinction | Bit, Bekenstein bound [15] | Information as constraint Ω→Ω′⊂Ω | Requirement (REQUIRED/FORBIDDEN) |
| Action | ħ, Margolus–Levitin bound [13] | The price of a transition | A certified transition as the unit of progress |
| Rate / time | Ratio of frequencies; ω = −u^μk_μ; redshift | Time as a ratio of rates, not an axis | Operational time d𝒯 ∝ (ħ dN/E)·η(M) |
| Irrelevance | Kernel of coarse-graining; RG-irrelevant operators | Irrelevance as the kernel of description π | IRRELEVANT; verdict OMIT |
| Uncertainty | Quantum uncertainty; Mandelstam–Tamm bound [14] | Honest UNDECIDED | UNRESOLVED; verdict UNDECIDED |
| Verification | Experiment, observed transition | The world as external verifier | Verifier; OBSERVED_TRANSITION; FalseFollowRate |
| Memory | Recorded trace (Landauer price [12]) | Grounding = history of certified transitions | Event-sourced Memory |
| Substrate | Material carrier within the constraint triad | Constraint envelope | The agent's hardware and compute budget |

Two rows of the table deserve separate warnings.

**Irrelevance.** The physical analogue of irrelevance is not "degrees of freedom outside the light cone" (that is a different, kinematic phenomenon) but the kernel of coarse-graining: microstates erased by the map π: Ω_micro → Ω_macro, and RG-irrelevant operators whose contribution decays with scale. This correspondence is consistent with §4.3 and with the definition of OMIT as membership in the kernel of the state-update map.

**Rate.** Time in this framework is not a fourth dimension alongside information and energy but their ratio: the rate of transitions. Therefore, in all three columns the "Rate / time" row is a derived construction (ratio of frequencies, ratio of rates, d𝒯), not a primitive. This is consistent with the physics program, where no global time is introduced and the emergent dynamics a∝t arises from the commutativity condition.

---

## 7. Archive Map and Verification Statuses

The archive is not a list of files but a distribution of theses across documents with explicit statuses. The table below is the repository's main navigation tool.

| Thesis | Document(s) | Status |
|---|---|---|
| The constraint triad: distinction / action / rate | The Algorithm of Being (§3); this document (§2.2) | FOLLOW (anchored to physical bounds) |
| Information as constraint, not substance | The Algorithm of Being (§3.1); this document (§2.1) | FOLLOW |
| Time as a ratio of rates; operational time d𝒯 ∝ (ħ dN/E)η(M) | The Algorithm of Being (§3.3–3.4); this document (§2.3–2.4) | FOLLOW as a schema; UNDECIDED as physical theory |
| Irrelevance = kernel of description; two indexings (goal / scale) | The Algorithm of Being (§9); this document (§4.3) | FOLLOW as formalism |
| Consciousness: recursive modeling under external verification | The Algorithm of Being (§10); this document (§4.2) | FOLLOW as an architectural frame; the hard problem is UNDECIDED |
| Substrate as constraint envelope | The Algorithm of Being (§11); this document (§4.4) | FOLLOW as a frame; numerical envelope bounds are UNDECIDED |
| Causal-phase network (C,≺)+U(1) → (M₄, g_μν, A_μ) | Causal Phase Geometry Research Program | UNDECIDED: a program with falsification criteria |
| Commutativity R_KK∘T₅ ≡ T₄∘R_KK; fixed point a∝t | KK–Jacobson Commutativity Note | UNDECIDED: the mathematical condition is formulated; physical realization is open (the radion stabilization problem) |
| Γ_corr and relic correlations of joint coarse-graining | Causal Phase Geometry Research Program | UNDECIDED: a prediction awaiting data |
| Space of Algebras (Level 0) | The Algorithm of Being (§2); this document (§3.1) | UNDECIDED: a conjecture, not a foundation |
| Ternary requirement semantics; authority hierarchy | Unified Implementable Model v2.0 | FOLLOW: specified |
| External verifier; FOLLOW/OMIT/NULL/UNDECIDED; FalseFollowRate | External Ternary Judge Adapter | FOLLOW: protocol; the empirics are in the §8 program |
| Agent V6.2 with the epistemic loop | ARCHITECTURAL / ENGINEERING SPECIFICATION | FOLLOW: specification; the ARC-AGI-3 benchmark is in the §8 program |

The rule for reading the archive: **status is attached to the thesis, not to the document.** A document may be technically complete (FOLLOW as a specification) while recording open questions (UNDECIDED as empirics). Conflating these statuses is the same error as passing a prediction off as an observation.

---

## 8. Experimental Program

### 8.1. Physics

- **Γ_corr.** Joint coarse-graining of the causal order and the phase degrees of freedom predicts specific correlations in relic data. The program's falsification criterion is the absence of the predicted correlations at sufficient data sensitivity (the SPARC analysis and beyond).
- **KK–Jacobson commutativity.** An open problem: radion stabilization and consistency with the scale hierarchy. The condition R_KK∘T₅ ≡ T₄∘R_KK is an exact mathematical filter: any realization violating it is discarded before comparison with data.
- **FAIR-MAST and adjacent campaigns** — potential channels for testing the predictions of causal-phase kinematics.

### 8.2. Artificial intelligence

- **FalseFollowRate** — the key metric: the fraction of transitions certified as FOLLOW that fail the constraint under independent checking. The goal is a measurable reduction relative to binary baselines, via first-class OMIT/UNDECIDED.
- **ARC-AGI-3.** Agent V6.2 is run on the benchmark; the criteria are not only task success but calibration (the match between declared confidence and observed accuracy) and the share of honest UNDECIDED versus fabricated FOLLOW.
- **Ternary Judge track.** Independent evaluation of the adapter: rule-interpreter stability across a change of proposer (OpenClaw/DeepSeek V4 and others), absence of semantic drift in verdicts.

### 8.3. Ontology

The philosophical level has no direct experiment but has an indirect one: **consistency**. If the physics program is falsified, the ontology must revise §2.3–2.4; if the engineering metrics show that ternary semantics does not reduce FalseFollowRate, §4.2–4.3 lose their operational support and revert to hypothesis status. This document records these dependencies explicitly, so that falsification at one level automatically demotes the linked theses at the others.

---

## 9. What This Document Does Not Claim

1. **It does not claim identity of levels.** The §6 isomorphism is a homology of forms of constraint, not an ontological identification. An agent is not a universe; logic is not physics.
2. **It does not claim that the Space of Algebras is a foundation.** Level 0 is a conjecture with the status UNDECIDED, a promissory note whose fate is tied to the falsifiable causal-phase program (Level 1). Until Level 1 is closed, the Level 0 construction is an abstraction for notational convenience, like Wheeler's bit.
3. **It does not claim novelty for the triad as such.** The "information–energy–time" pairs are old (Landauer, Margolus–Levitin, Mandelstam–Tamm). The novelty — if any — lies in binding the triad to a concrete physics program (the delta of rates as the object of formalization) and to an executable engineering semantics.
4. **It does not claim a solution to the hard problem of consciousness.** The "recursive modeling under external verification" frame is architectural, not phenomenological. Qualia lie outside this framework's competence.
5. **It does not claim substrate independence for consciousness.** It claims substrate-parameterization: the architecture of consciousness is realized only within the constraint envelope of a material carrier, and that carrier is the interface to the external verifier. No dualism is introduced; architectures are separated, not substances.
6. **It does not claim that the old schemata retain force.** The formula d𝒯 = (dI/E)·η(M) from earlier versions is withdrawn as dimensionally invalid; it is replaced by d𝒯 ∝ (ħ dN/E)·η(M). The archive records the withdrawal rather than concealing it.
7. **It does not claim completeness.** The document is a snapshot as of the version date. The §7 statuses are subject to revision per the §8 results, in both directions: UNDECIDED may become FOLLOW, and FOLLOW may become NULL.

---

## Appendix. Archive Document Correspondence

| File | Level | Language | Role in the framework |
|---|---|---|---|
| The Algorithm of Being (Revised) | Ontology | EN | The philosophical frame: triad, kernel, consciousness under verification, substrate envelope |
| Causal Phase Geometry Research Program | Physics | EN | Level 1: the causal-phase network, falsifiable predictions |
| KK–Jacobson Commutativity Note | Physics | EN | Level 1: the 5D→4D thermodynamic bridge, the commutativity condition |
| Unified Implementable Model v2.0 | Engineering | EN | The agent's architectural ontology |
| External Ternary Judge Adapter | Engineering | EN | The external-verification protocol |
| ARC-AGI-3 LCLD Agent: Architectural + Engineering Specifications | Engineering | EN | The V6.2 instantiation |
| Unified Informational-Constructive Framework (this document) | Synthesis | EN (RU version available) | The map of theses, statuses, and cross-level dependencies |

---

*End of document. Version 1.0. Feedback and objections — via repository issues.*
