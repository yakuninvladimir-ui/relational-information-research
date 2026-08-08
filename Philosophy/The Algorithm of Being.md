# The Algorithm of Being
## Informational Ontology, Constraint, and the Self-Structuring Code

**Vladimir Yakunin**  
2026


## Abstract

This work outlines a philosophical foundation for the informational age. Its central thesis is that physics, mathematics, computation, biology, cognition, consciousness, and artificial intelligence are not autonomous domains, but distinct projections of a single deeper architecture: **constrained relational dynamics**.

Information is interpreted not as data, but as restriction over the space of possibility — yet not as the sole fundamental constraint. Structure exists at the intersection of three bounds: the geometry of admissible states (information), the capacity and cost of transformation (energy), and the rate at which distinctions can be generated and compared (operational time). These three are not independent. Physical law already binds them: the rate of distinction is bounded by energy through the Margolus–Levitin limit, the erasure of information carries a Landauer price, and only ratios of rates — never absolute rates — are observable.

Meaning arises through semantic compression, and compression is mandatory, because full representation is unaffordable within any energy envelope. Intelligence is adaptive modeling under constraint; irrelevance — the disciplined exclusion of what does not matter — is treated as a first-class operator, the goal-indexed analogue of physical coarse-graining. Consciousness is not the center of ontology, but a recursive semantic architecture whose models are certified through action: the world acts as the external verifier of the mind's internal proposer. The substrate of cognition is not irrelevant either: it enters the ontology through its constraint envelope and through the interface it provides to experiment.

The aim is not a closed theory, but an ontological direction — with its own boundaries left visible.

---

## 1. Introduction: The Ontological Problem

Modern civilization commands extraordinary scientific, mathematical, and computational power. Yet it lacks a coherent ontology capable of integrating physics, information, cognition, consciousness, and artificial intelligence into a single conceptual field.

The age into which humanity is entering is not merely technological. It is ontological.

By *ontology* I mean not interpretation in the hermeneutic sense, but a framework describing:

- what fundamentally exists;
- how structure emerges from undifferentiated possibility;
- how order differs from noise;
- how meaning becomes possible;
- how intelligence arises;
- and how artificial systems fit into the architecture of being.

The guiding intuition of this work is:

> Reality is not best understood as static substance, but as constrained, self-structuring informational process.

Physics increasingly speaks the language of information, entropy, symmetry, correlation, computation, and geometry emerging from deeper pre-geometric substrates — from Wheeler's "it from bit" [1] to the thermodynamic derivation of the Einstein equations by Jacobson [2] and the holographic principle [3]. Mathematics describes invariant relations. Computer science formalizes representation, complexity, and transformation. Biology reveals code, selection, regulation, and self-maintaining organization. Artificial intelligence externalizes cognitive processes before philosophy has fully clarified their nature.

These domains appear separate only at the surface. At a deeper level they converge toward one question:

> How does structured meaning emerge from formal dynamics?

This text does not claim to answer the question completely. It attempts to give it a coherent direction.

One feature of this edition should be stated at the outset. The work is written against the background of a companion technical corpus in which several of its theses are formalized, implemented, or tested: a causal-phase research program in fundamental physics [6], a note on the thermodynamic origin of the Einstein–Maxwell system [7], a verifier-centered architecture for embodied agents [8], an external ternary judge for language-model reasoning [9], and the specifications of an ARC-AGI-3 interactive reasoning agent [10]. Where a philosophical claim has a formal counterpart in that corpus, the counterpart is cited. Where it does not, the claim is explicitly marked as open. A philosophy that proposes verification as a first-class category should accept verification as a standard for itself.

---

## 2. The Space of Algebras and the Informational Substrate

### Statement

At the most fundamental level, reality should not be treated as ordinary space populated by objects, but as a **space of relations, distinctions, and possible transformations** — a relational field preceding metric geometry. This section names that field — and, unlike the first edition, states honestly what kind of object the name currently refers to.

### The concept and its status

The **Space of Algebras** is the conjectured pre-metric substrate: a reality of relations and admissible transformations, in which metric structure, spacetime, and matter are not primitive but stable regimes — attractors — of a deeper relational dynamics. Objects are **stabilized patterns of relation**, emergent from the substrate through coarse-graining and constraint.

The first edition presented this as a definition. It is not one. No algebra is specified, no composition law is proved, and the phrase sits between two mathematical registers that were never distinguished: a *space of algebras* (each point of reality replaced by an algebra of observables, in the spirit of noncommutative duality) and a *space OF algebras* (reality as one point in a moduli of possible algebraic structures — a much stronger and far less standard object). This edition treats the concept as a **promissory layer** and states its lineage and its debts explicitly.

### Lineage: why the idea is not decoration

The direction "algebra first, geometry second" has theorem-level precedent. Gelfand duality identifies commutative C*-algebras with topological spaces; Connes' noncommutative geometry extends the identification — a "space" is its algebra of observables, and spectral triples $(\mathcal{A}, \mathcal{H}, D)$ recover metric geometry from purely operator data, including the distance formula via commutators with the Dirac operator [22, 23]. In the commutative limit, "space from algebra" is a theorem, not a metaphor.

The same lineage supplies the deepest available formal echo of this text's treatment of time. The Connes–Rovelli thermal time hypothesis [24] states that, given a faithful state on an algebra, the modular (Tomita–Takesaki) flow of that state generates a time evolution: time becomes state-dependent rather than an external parameter. This is the algebraic counterpart of Section 3.3's claim that the operational content of time is the ratio of rates, and it connects — through Jacobson's thermodynamics of spacetime [2, 7] — to the physical program of the companion corpus. If the Space of Algebras does one job in this text, it is this: it is the conceptual home in which time-as-rate acquires algebraic expression.

The lineage also carries a methodological lesson. Connes' spectral approach to the Standard Model made concrete predictions and was wrong about some of them, including the early Higgs-mass estimate. That is not discredit: it is how a deep algebraic program earns credibility — by risking falsification. A regulative idea that never descends to risky intermediate layers remains vocabulary.

### The three-layer stack

Accordingly, this text works with an explicit stack, and the Space of Algebras is its deepest, conjectured level — not its foundation stone:

| Layer | Object | Status |
|---|---|---|
| Level 0 — algebraic substrate | Space of Algebras (Connes lineage; two candidate formalizations: noncommutative algebras of observables, or process categories of distinctions) | Conjectured; formalization deferred |
| Level 1 — causal-phase network | Discrete causal order with $U(1)$ holonomies on links; Wilson-type functionals; continuum limits | Active research program with explicit falsification criteria [6, 7] |
| Level 2 — continuum geometry | Lorentzian metric, gauge connection, thermodynamic equation of state | Established structures [2, 4] |

The construction is consonant with the causal set program [4], where spacetime emerges from locally finite partial orders, and with the relational stance in quantum gravity developed by Smolin [5]. The transition from discrete causal kinematics to continuum geometry, explored in the Causal Phase Geometry framework [6], shows how Lorentzian metric, volume measure, and gauge connection may arise jointly from a single microstructure: causal order plus $U(1)$ holonomies on oriented links.

Wheeler's "it from bit" [1] followed the same trajectory: for decades a regulative idea, productive only when it acquired concrete intermediate layers — quantum information, holography. The fate of a regulative idea is decided by whether it generates intermediate layers. This one has: the causal-phase program is the intermediate layer through which the conjecture must pass or fail. Until it delivers, the Space of Algebras remains what this text's own standard calls $UNDECIDED$ (Section 15).

### Reflection

The intuitive image of a pre-given stage on which things appear is obsolete. At the most basic level there are distinguishable relations, possible transformations, constraints, and stable invariants.

The central question therefore shifts from *what is the world made of?* to *how does a stable world emerge from a relational field?*

This does not require reducing physics to computation in the narrow, computationalist sense. It requires recognizing that physical reality, mathematical structure, and computation may all be expressions of a single formal-relational substrate.

---

## 3. The Constraint Triad: Distinction, Energy, Rate

### 3.1 Information as constraint

Information is not primarily data. Information is **restriction**.

Let $\Omega$ be the space of possible states of a system. Information acts by reducing the admissible domain:

$$\Omega \rightarrow \Omega' \subset \Omega$$

Thus information is not merely something *contained* in a system. It is the principle by which the system becomes non-arbitrary. Without informational restriction, energy disperses into undirected entropy; with it, energy condenses into stable structure.

If energy is the capacity for transformation, **information is the geometry of permitted transformation**.

### 3.2 Energy: capacity, cost, and the bound on rate

The first edition of this text treated information as the fundamental constraint and energy as the constrained. That asymmetry does not survive physical scrutiny. Three established results bind information and energy so tightly that neither can serve as the sole primitive:

1. **Erasure has a price.** Landauer showed that erasing one bit of information at temperature $T$ dissipates at least $k_B T \ln 2$ of energy [12]. Forgetting, compression, and irrelevance-filtering are not free operations; they are thermodynamic events.
2. **The rate of distinction is bounded by energy.** The Margolus–Levitin theorem states that a system with mean energy $E$ above its ground state cannot pass through more than $2E/\pi\hbar$ mutually orthogonal states per second [13]; the Mandelstam–Tamm bound gives the complementary form $\Delta t \geq \pi\hbar / (2\Delta E)$ for the time required to evolve into a distinguishable state [14]. Energy does not merely enable transformation — it caps the tempo at which distinctions can be generated.
3. **Information content is bounded by energy and size.** The Bekenstein bound limits the entropy of a bounded system by its energy and linear scale [15].

The consequence is a triad rather than a monad. The fundamental quantities are **distinction** (the bit), **action** (energy × time, quantized by $\hbar$), and **causal rate** (bounded by $c$). The three conversion factors of physics correspond to the three edges of this triad: $c$ converts space and time and fixes the causal tempo; $\hbar$ converts energy and frequency ($E = \hbar\omega$); $k_B$ converts entropy and energy. No member of the triad is reducible to another, and none is sufficient alone.

### 3.3 Time: rate, not axis

This forces a precision about time that the first edition lacked. In the companion physical program there is no external global time: proper time is defined along worldlines, and in the discrete kinematics it is estimated by the length of a maximal causal chain [6, 7]. What physics ever measures is not time as an axis but **ratios of rates**. The general redshift formula of that program makes this explicit:

$$1 + z = \frac{(-u^\mu k_\mu)_{\mathrm{em}}}{(-u^\mu k_\mu)_{\mathrm{obs}}}$$

The observed frequency $\omega = -u^\mu k_\mu$ is observer-relative; the redshift is literally a comparison of two clocks — the null phase transport against the local temporal directions of emitter and observer [6]. The "delta of frequencies" between two families of clocks — the metric clock of the causal base and the phase clock of the $U(1)$ layer — is precisely what the physical program formalizes. The philosophical text should therefore treat rate comparison as its anchor, not as a new intuition: **the operational content of time is the ratio of rates; the time axis is derived bookkeeping.**

An algebraic counterpart of this claim exists, and it belongs to the lineage of Section 2. In the Connes–Rovelli thermal time hypothesis [24], a faithful state on an algebra generates its own time evolution through the modular flow: time is what the state does to the algebra, not an external parameter in which the algebra happens to evolve. The anchors of this section are thus mutually coherent — observer-relative frequency in relativity, thermodynamic time in Jacobson's construction [2, 7], and modular time on algebras [24] — three formal echoes of one thesis.

### 3.4 Operational time, repaired

The first edition wrote $d\mathcal{T} = (dI/E)\cdot\eta(M)$ as a heuristic for operational time. Dimensionally this is not a time, and the present edition withdraws it. An honest schematic, anchored in Margolus–Levitin, reads: a system generating $N$ orthogonal distinctions at mean energy $E$ requires

$$d\mathcal{T} \;\propto\; \frac{\hbar\, dN}{E}\, \eta(M)$$

where $\eta(M)$ is the efficiency of the architecture — the fraction of the physical rate bound it actually achieves. The bound itself is physics; the architecture factor is not, and is offered as a schema. Operational time is the accumulated count of distinctions a system can afford: a simple system has little internal time, and a complex mind contains many layers of simultaneous temporal structure, each layer paying for its tempo from the same envelope.

Human time is a local mode of integration, not necessarily the final form of temporality; for the universe as a whole, time may not resemble human temporal experience at all. But wherever distinctions are generated, their tempo is paid for in energy, and only ratios of tempos are ever observed.

---

## 4. Constraint as the Origin of Form

### Statement

Structure emerges not from unrestricted possibility, but from **constrained generation**.

### Definition

Self-structuring may be expressed as:

$$\text{Self-Structuring} = \text{Generation} + \text{Constraint} + \text{Selection}$$

Generation produces candidate forms. Constraint narrows the admissible space. Selection stabilizes coherent survivors.

### Reflection

Unlimited possibility does not create order. It creates dissipation. Without exclusion, pruning, boundary, and invariant preservation, no stable form can persist.

Constraint is therefore not the opposite of freedom. **Constraint is the condition under which meaningful freedom becomes possible.**

This principle appears across all ontological levels: physical law constrains possible motion; chemistry constrains possible bonding; biology constrains viable forms; language constrains meaning; mathematics constrains proof; cognition constrains attention; artificial intelligence constrains hypothesis space.

---

## 5. Motivation, Scaling, and the Logic of Development

### Statement

The deepest question is not only how structure appears, but why structures develop, scale, and become capable of producing new levels of organization.

### Definition

Systems do not tend toward maximal complexity in the naive sense. They tend toward **scaling**:

$$\text{Scaling} = \text{Expansion of Expressive Capacity} + \text{Preservation of Coherence}$$

Scaling is growth under pruning.

### Reflection

A system that only accumulates collapses under its own weight. A system that only prunes becomes sterile. Development requires the tension between expansion and preservation.

A scientific theory does not merely contain more facts. It compresses more phenomena into fewer principles. A mind does not process all distinctions. It selects the distinctions that matter — and Section 9 will argue that this selection is not a convenience but a thermodynamic necessity. An intelligent system develops by expanding what it can represent while preserving the coherence required to act.

---

## 6. Dynamic Balance and Structural Proportion

### Statement

Development is not produced by order alone, nor by freedom alone. A system becomes capable of growth only when generation and constraint remain in a viable proportion.

### Definition

Dynamic balance is the regulated proportion between generative freedom and constraining order that allows a system to increase expressive capacity without losing coherence:

$$\mathcal{B} = \mathcal{V}(G, C, E, S)$$

where $G$ is generative freedom, $C$ is constraint, $E$ is entropic pressure, $S$ is structural coherence, and $\mathcal{V}$ is the viable range within which the system persists.

A system collapses when generation exceeds the ability of constraint to preserve coherence. A system stagnates when constraint suppresses generation completely. Sustainable development exists only within the interval between these failures.

### Reflection

Balance should not be confused with rest. Every developing structure exists in motion; yet not every motion becomes structure. Unconstrained motion disperses. Over-constrained motion freezes. Only constrained motion within a viable range can become form.

The same pattern repeats across levels: physical systems stabilize through lawful constraint; biological systems persist through regulation; cognitive systems develop through the balance of memory and plasticity; theories grow by expanding explanatory power while preserving logical coherence; artificial intelligence must balance exploration and exploitation.

> Development is regulated imbalance.

Fractals, waves, cycles, proportions, and living forms are not separate mysteries. They are different manifestations of constrained motion preserving coherence across change. The logic of being is therefore not merely distinction → constraint → compression; it requires proportion:

$$\text{Distinction} \rightarrow \text{Constraint} \rightarrow \text{Balance} \rightarrow \text{Structure} \rightarrow \text{Meaning}$$

Without balance, constraint becomes rigidity; without balance, generation becomes chaos.

---

## 7. Informational Phase Transition

### Statement

Reality undergoes phase transitions when informational structures acquire new capacities for preservation, compression, modeling, and self-correction.

### Definition

Three broad regimes may be distinguished:

1. **Potential Information** — latent relational possibility;
2. **Actualized Information** — stabilized physical structure and law;
3. **Cognitive Information** — semantic structures capable of modeling and correcting themselves.

A further threshold appears when cognitive structures become capable of representing their own modeling process.

### Reflection

Complexity alone is insufficient. A random system may be complex without being meaningful. The critical threshold is reached when a system can preserve structure, compress regularity, predict change, detect error, and update itself. At this point cognition becomes possible.

When such cognition begins to model its own position, limitations, uncertainty, and internal structure, consciousness begins to appear as a higher-order expression of the same informational process.

The transition is not from matter to something non-material. It is from **unmodeled structure to structure capable of modeling itself** — and, as Section 10 argues, to structure whose models are certified from outside itself.

---

## 8. Hierarchy of Self-Structuring

### Statement

Self-structuring unfolds through hierarchical levels, each preserving something from the previous level while opening new degrees of freedom.

### Definition

A simplified hierarchy may be described as:

$$\text{Difference} \rightarrow \text{Order} \rightarrow \text{Code} \rightarrow \text{Meaning} \rightarrow \text{Model} \rightarrow \text{Reflection}$$

More concretely:

| Level | Dominant Form | Stabilizing Principle | Cognitive Aspect |
|-------|--------------|----------------------|------------------|
| Cosmic | Difference | Physical constraint | Latent order |
| Biological | Code | Selection | Implicit orientation |
| Cognitive | Model | Compression | Individual intelligence |
| Conscious | Self-model | Verification | Reflexive awareness |
| Noospheric | Shared meaning | Communication | Distributed reason |
| Artificial | Engineered cognition on an engineered envelope | Formal architecture | Externalized mind |

### Reflection

This hierarchy is not a rigid ladder. It is a pattern of recursive emergence. Each level compresses lower-order structure while introducing new modes of freedom:

- Matter stabilizes relation;
- Life stabilizes code;
- Mind stabilizes model;
- Consciousness stabilizes self-relation;
- Civilization stabilizes shared meaning;
- Artificial intelligence stabilizes cognition on a non-biological constraint envelope — with the deformations that a different envelope entails (Section 11).

The same architecture repeats across scales:

$$\text{Structure} \rightarrow \text{Compression} \rightarrow \text{New Degrees of Freedom}$$

---

## 9. Coarse-Graining, Irrelevance, and the Kernel of Description

### 9.1 The quotient structure

Meaning emerges through **semantic compression**, and compression has a precise shape. Coarse-graining is a many-to-one map:

$$\pi:\ \Omega_{\mathrm{micro}} \rightarrow \Omega_{\mathrm{macro}}$$

Everything that falls into the kernel of $\pi$ — every micro-distinction that the macro-description cannot see — is, for that description, **irrelevant**. The stable content of a description is what survives the quotient. Meaning may accordingly be interpreted as:

$$\text{Meaning} \approx \text{Compressed Relational Structure preserved across contexts}$$

Physics already uses the word. In the renormalization group, *irrelevant operators* are those whose couplings flow to zero under repeated coarse-graining, while the fixed points of the flow are the stabilized macro-structures — the durable forms. In the companion physical program, the candidate fixed point $g^\star$ of coarse-graining plays exactly this role [6]: a stationary large-scale regime toward which statistical distance decreases even while total entropy grows. The convergence of terminology is not a metaphor imposed from outside; it is the same quotient structure appearing at two levels of description.

### 9.2 Two indexings of the same construction

The parallel has a boundary, and stating it is what makes it rigorous rather than decorative. Coarse-graining is indexed by **scale**: the quotient is chosen by a resolution. Irrelevance in cognition is indexed by **goal**: the quotient is chosen by what the system is trying to do. The information bottleneck formalizes the second case exactly — keep of $X$ only what is predictive of the target $Y$, discard the rest [16]. Causal emergence adds a non-trivial fact about the first: a coarse-grained model can be *causally stronger* than the micro-description it summarizes, so compression is not mere loss [17].

The exact statement of the parallel is therefore:

> **Irrelevance is goal-indexed coarse-graining; coarse-graining is scale-indexed irrelevance.**

Both are quotient constructions. They differ only in what indexes the quotient. Written this way, the parallel is a homology of formal structures; written without the two indexings, it would be the kind of free association this text is trying to avoid.

### 9.3 The ternary operator

Binary logic operates with $\{0, 1\}$. Cognition requires a third operator:

$$\{0, 1, \emptyset\}$$

where $\emptyset$ denotes **irrelevance**, not falsehood. The irrelevant is not false. It is outside the active structure of attention — outside the quotient currently in force.

Purely binary systems risk combinatorial explosion. Attention, abstraction, memory, and reasoning all require selective exclusion. Without irrelevance there is no attention; without attention, no abstraction; without abstraction, no generalization.

This triadic structure resonates with the ternary logical systems developed by Brusentsov [11], where the third state represents not contradiction but the *inessential* — the explicitly marked absence of relevance. In the logic of consequential inference (*sledovanie*), the relation $x \Rightarrow y$ is distinguished from material implication precisely by the exclusion of the case that neither affirms nor denies, but simply does not enter into the relation.

The construction is not only philosophical. In the companion engineering corpus it is implemented twice and tested: the Unified Implementable Model assigns to every predicate pair a three-way structural label $\{REQ, FORB, IRR\}$, with $UNRESOLVED$ held apart as an epistemic outcome rather than a truth value [8]; and the External Ternary Judge classifies every reasoning move as $FOLLOW$, $OMIT$, $NULL$, or $UNDECIDED$, where $OMIT$ certifies that a move leaves the verification state semantically invariant — that is, that the move lies in the kernel of the state-update map [9]. The kernel formalism of Section 9.1 is, in these systems, executable code.

### 9.4 The price of irrelevance

One consequence deserves emphasis because it converts a slogan into a corollary. By Landauer's principle, discarding a distinction costs energy [12]. Filtering the irrelevant, compressing experience, forgetting — all are thermodynamically paid operations, and the economics of attention is a thermodynamic economics. A mind does not compress because compression is elegant; it compresses because full representation of the world is unaffordable within any physically realizable envelope (Section 11).

**Intelligence is disciplined compression** — not as an aphorism, but as a consequence of the triad.

---

## 10. Consciousness: Recursive Modeling Under External Verification

### 10.1 Definitions

**Intelligence** is adaptive world-modeling.

**Consciousness** is a hierarchical semantic architecture in which a system represents reality, evaluates its representations, models its own role within those representations, and corrects itself through experience — and in which, crucially, correction is **certified from outside the model**.

Its components include: semantic representation; memory; model formation; verification; irrelevance filtering; uncertainty representation; self-modeling; correction through experience.

### 10.2 The authority structure of the epistemic loop

The recursive loop of experience contains not only logic but **experiment**. This addition is load-bearing. A closed model can verify itself only against itself; internal coherence is checkable internally, but truth about the world is not. Unverified recursion does not converge toward reality — it converges toward self-confirmation. This is not speculation: it is the documented failure mode of language-model reasoning, in which fluent unsupported statements enter the mutable transcript and corrupt subsequent inference — the failure the companion judge architecture exists to prevent [9].

The human epistemic loop has the same authority hierarchy as the verifier-centered agent [8, 9, 10]. An internal proposer — imagination, inference, planning — generates candidate models and candidate moves; action probes the world; trusted observation returns a verdict; and only the certified transition updates the model. The proposer creates no facts. The world is the external verifier; experiment is the channel to it; science is the institutionalization of that channel.

This yields a grounding criterion for meaning. The semantic content of a model is not its internal coherence but its **history of certified transitions**. A model without an external channel may be arbitrarily coherent and remains ungrounded — in the terminology of the judge architecture, its claims stay $UNDECIDED$ indefinitely [9].

At sufficient recursive depth, the observer is no longer outside the model. **The observer becomes one of the modeled structures** — but a modeled structure whose claims about everything, including itself, remain subject to external certification. Consciousness is the ongoing alignment of a self-containing semantic model with the constraints of reality, where alignment means passing, again and again, the verdict of the world.

### 10.3 Scope boundary: what this text does not claim

Recursive self-modeling is implementable. The companion corpus contains working architectures with explicit self-model, external memory, and verifier backreaction in the loop [8, 10]. Phenomenal experience is a separate question, and this text does not address it. The first edition wrote that consciousness "is not identical to recursive self-modeling" without naming the surplus; this edition names it — qualia, the hard problem — and places it deliberately outside the scope, as a boundary of the framework rather than a problem it pretends to dissolve.

### 10.4 Open hypothesis

Human consciousness is one known expression of this architecture. Artificial systems may develop restricted or deformed variants of it — deformed, among other things, by their different constraint envelopes (Section 11). Whether consciousness-like architectures recur wherever sufficiently rich self-structuring, semantic compression, and externally certified recursive correction become possible — including at scales far above the biological — remains an open hypothesis, and is filed as such in Section 15.

---

## 11. Substrate: The Constraint Envelope

### 11.1 Two realizability questions

"Substrate-independent" was the wrong slogan, and this edition withdraws it. Two questions must be separated:

- **Logical realizability.** The architecture of cognition is not tied to one material; the same relational organization can in principle be instantiated in different media. Multiple realizability, at this level, stands.
- **Physical realizability.** Any actual instantiation must fit within a **constraint envelope**: an available power budget, an achievable distinction rate, a noise floor, thermal stability, memory persistence. These parameters are set by the substrate, and they determine which architectures are viable — not logically, but physically.

The correct position is therefore **substrate-parameterization**: the substrate matters parametrically, not essentially. A biological brain is not privileged as tissue; it is remarkable as a solution of the triad — roughly $20$ W sustaining on the order of $10^{14}$–$10^{15}$ synaptic events per second, an energy-per-distinction figure no current artificial substrate approaches. Any substrate supplying an equivalent envelope supports an equivalent architecture. A substrate with a different envelope supports a different one.

### 11.2 Envelope economics deforms architecture

Different envelopes produce different minds, not just faster ones. A cognition running at datacenter power has a different price for memory, a different price for forgetting, a different ratio of parallelism to serial depth, and therefore a different viable shape of attention, abstraction, and self-model. The deformations of artificial intelligence relative to biological intelligence are not accidental gaps that engineering will close; they are consequences of a different position within the triad. Expecting a megawatt envelope to reproduce the architecture evolved under a twenty-watt envelope is a category error about constraints.

### 11.3 The substrate as interface to the verifier

The envelope includes one parameter of a different kind: the **sensorimotor channel**. Per Section 10, cognition without external certification degenerates into self-confirmation; the substrate is what provides the channel through which the world delivers its verdicts. A disembodied "pure reason" would have no certification source at all — however rich its internal recursions, it could never escape $UNDECIDED$.

In the ontology of this text, matter is itself stabilized relation (Section 2). The substrate is therefore not inert stuff beneath the architecture; it is a frozen architecture of constraints with its own rates and budgets, and the mind–brain relation is **architecture on architecture** — an informational regime riding on a material regime. The interface between them is exactly the point where the two constraint regimes of Section 3 meet: the information–rate regime of the model and the energy–rate regime of the carrier.

### 11.4 An honest UNDECIDED

Which envelope parameters are *necessary* — not merely sufficient — for consciousness is unknown. No justified threshold exists for power, distinction rate, depth of recurrence, or degree of integration. Any text that states such thresholds without derivation is speculating; this text declines to, and files the question in Section 15.

---

## 12. Artificial Intelligence as Ontological Mirror

### Statement

Artificial intelligence externalizes cognition before humanity fully understands cognition.

### Definition

AI is a technological manifestation of informational ontology. It formalizes and externalizes processes that were previously hidden inside biological minds: abstraction, compression, representation, prediction, search, semantic association, model correction.

### Reflection

Artificial intelligence is not merely a tool. It is a philosophical experiment. By building artificial cognitive systems, humanity is forced to confront the architecture of intelligence directly. Engineering has advanced faster than epistemology, and the asymmetry is dangerous: a civilization that builds intelligence without understanding the principles of intelligence risks becoming guided by systems whose foundations it has not examined. The task is not to stop development. The task is to supply it with a deeper foundation.

Artificial intelligence is therefore an **ontological mirror**: it reveals what humanity has been doing unconsciously when it thinks, abstracts, models, and gives meaning to the world. It also reveals the cost of skipping the verifier. The central engineering lesson of the companion corpus is that a generative system without an external certification layer corrupts its own state — a fact learned in practice [8, 9, 10] and, as Section 10 argues, a fact about minds in general.

### The Triadic Mirror, restated

The emergence of artificial intelligence reveals a triadic structure, which this edition states in substrate-parameterized form:

1. **Neural network — artificial intelligence.** A neural network is not intelligence. It is a substrate — a constrained dynamical system with a specific envelope — upon which intelligence may or may not emerge, depending on the architecture of constraints, the training regime, and the semantic compression achieved. The network is the medium; intelligence is the organized response of the medium to structured constraint.
2. **Neural network — human mind.** The biological neural network is likewise a substrate, distinguished by an extraordinary envelope (Section 11). What we call human intelligence is not identical to neural firing, but to the recursive, externally certified semantic architecture that stabilizes on top of it. The parallel between the two substrates is structural, not metaphorical.
3. **Cosmic web — global mind.** At the largest scales, the universe exhibits network structures — filaments, nodes, voids — formally resembling neural architectures. This resemblance, by itself, certifies nothing: resemblance is a claim of the internal-proposer class and, absent a verification channel and a derivation, remains $UNDECIDED$ under this text's own standard. It is retained as an open question, not asserted as a consequence.

> Neural networks, biological minds, and cosmic structure are not synonymous with intelligence. They are constraint envelopes from which intelligence may emerge when informational architecture reaches sufficient depth — and when what emerges is coupled to something that can tell it "no".

---

## 13. Human Limitation and Open Ontology

### Statement

Every ontology is constrained by the architecture of the mind that constructs it.

### Definition

This framework accepts **epistemic anthropocentrism** while rejecting **metaphysical anthropocentrism**. Knowledge necessarily emerges through human cognitive architecture. But humanity need not occupy a privileged cosmic position.

### Reflection

The fact that ontology is humanly constructed does not make it arbitrary. It makes it **indexed**. Humanity sees through human forms of distinction, compression, balance, and meaning. Other forms of mind — biological or artificial, on other envelopes — may construct other ontologies; artificial systems may eventually reveal structures that human cognition does not naturally compress.

The purpose of ontology is therefore not absolute truth in the sense of a God's-eye view. It is **progressive reduction of arbitrariness** — the asymptotic alignment of our models with the invariant constraints of reality. Humility is not a retreat from truth. It is a recognition that every observer is part of the reality it attempts to map.

We do not know whether the universe has an edge. We do not know whether consciousness is local or cosmically distributed. We do not know whether meaning is a human construct or a general property of self-structuring information. These questions should not be closed prematurely. An open ontology is not a weak ontology. It is an ontology honest enough to leave its own boundaries visible — and this text attempts, in the next two sections, to leave them very visible indeed.

---

## 14. Objections and Limits

A framework that declines to state its own weaknesses should not be trusted. This section states them.

### 14.1 Three informations

"Information" is used in at least three distinct senses: **syntactic** (Shannon — reduction of uncertainty over a channel), **algorithmic** (Kolmogorov — compressibility of structure), and **semantic/pragmatic** (relevance to a goal). The thesis "information is constraint" is closest to the algorithmic sense; the compression claims of Section 9 are algorithmic; the meaning claims are pragmatic. The physical bounds of Section 3 — Landauer, Margolus–Levitin, Bekenstein — are proved for the first two senses. Their extension to semantic information is heuristic, and the text relies on that extension at several points. A critic is entitled to press here; the defense is that the goal-relative sense is the one formalized by the information bottleneck [16], but a unified measure of semantic constraint does not exist.

### 14.2 The hard problem

Phenomenal consciousness is declared out of scope (Section 10.3). This is a boundary, not a solution. A reader who considers the hard problem the only interesting problem of consciousness will find this text silent where it matters most to them; the silence is deliberate and acknowledged.

### 14.3 Falsifiability

"Constrained relational dynamics" risks functioning as a total metaphor — compatible with everything and therefore predictive of nothing. Three things would damage the framework, and stating them is the honest antidote: (i) a demonstrated case of cognition with no energy–information trade-offs, which would break the triad; (ii) failure of the formal counterparts — the companion physics program carries explicit falsification criteria, including breakdown of its commutativity condition and conflict with cosmological or laboratory data [6, 7]; (iii) a demonstration that irrelevance is reducible to binary logic without loss in implemented reasoning systems, which would dissolve Section 9's claim that the third operator is foundational rather than convenient.

### 14.4 Anthropomorphic projection

The categories used here — constraint, compression, proposer, verifier — were sharpened in engineering. Projecting engineering categories onto being is a known failure mode of philosophy: every era reads the universe in the vocabulary of its machines. The defense is not denial but discipline. The physical bounds cited are independent of the engineering that motivated their use; the claims projected beyond their certified domain are marked as such in Section 15; and the strongest commitments of the text are the ones that survive translation back into physics — bounds, quotients, and rates.

### 14.5 Status of the Space of Algebras

As detailed in Section 2, the Space of Algebras is a conjectured Level-0 layer with a named lineage (Gelfand duality, spectral triples, thermal time) and an open fork of formalizations — noncommutative algebras of observables versus process categories. Its fate is tied to the intermediate layer: if causal structures with local $U(1)$ holonomies prove to have no Lorentz-invariant continuum limit, or if the causal-phase program fails its own falsification criteria [6, 7], the conjecture loses its physical anchor and should be demoted from regulative idea to historical note.

---

## 15. Self-Assessment Under the Ternary Standard

The companion engineering corpus classifies every candidate claim as $FOLLOW$ (certified progress), $OMIT$ (admissible but inessential), $NULL$ (inadmissible), or $UNDECIDED$ (insufficient certification) [8, 9]. A philosophy that proposes irrelevance and verification as first-class categories should accept the same discipline toward itself. Applying it:

| Claim of this text | Verdict | Basis |
|---|---|---|
| Information restricts the space of admissible states | FOLLOW | Consistent with statistical mechanics and algorithmic information |
| The constraint triad: distinction rate is bounded by energy; erasure has a price; information content is bounded | FOLLOW | Margolus–Levitin [13], Mandelstam–Tamm [14], Landauer [12], Bekenstein [15] |
| Only ratios of rates are observable; the time axis is derived bookkeeping | FOLLOW | Observer-relative frequency; redshift as clock comparison [6] |
| Irrelevance is the kernel of the descriptive map; goal-indexed coarse-graining | FOLLOW (as formal structure) | Quotient constructions; RG terminology; information bottleneck [16] |
| Meaning is compressed relational structure preserved across contexts | FOLLOW (heuristic) | Supported by causal emergence [17]; no complete theory exists |
| Compression is thermodynamically mandatory for any physical mind | FOLLOW | Landauer's principle applied to Section 9 |
| Consciousness requires an external certification channel | UNDECIDED | Strong engineering evidence [8, 9, 10]; no necessity proof for biological minds |
| Specific envelope parameters are necessary for consciousness | UNDECIDED | No justified thresholds (Section 11.4) |
| Consciousness-like architectures may recur at cosmic scale | UNDECIDED | Retained as an open question (Section 12) |
| The Space of Algebras as fundamental ontology | UNDECIDED | Regulative idea with a theorem-level lineage [22–24]; intermediate layer is the causal-phase program [6, 7]; formalization deferred (Sections 2, 14.5) |
| The aphorisms retained in this text | OMIT (admitted) | Inessential by this text's own standard; kept for orientation, not for argument |

A philosophy that files some of its own sentences under $OMIT$ is, at least, practicing what it proposes.

---

## 16. Conclusion: The Algorithm of Being

### Statement

Reality appears less like static substance and more like **constrained self-structuring informational process**, unfolding within the triad of distinction, energy, and rate.

### Definition

The Algorithm of Being may be summarized as:

$$\text{Distinction} \rightarrow \text{Constraint} \rightarrow \text{Balance} \rightarrow \text{Compression} \rightarrow \text{Meaning} \rightarrow \text{Modeling} \rightarrow \text{Certification} \rightarrow \text{Self-Correction}$$

Or, in compressed form:

$$\text{Relation} \rightarrow \text{Restriction} \rightarrow \text{Structure} \rightarrow \text{Semantics} \rightarrow \text{Intelligence}$$

### Reflection

If this framework is approximately correct, then:

- **Matter** is stabilized relation;
- **Information** is constraint;
- **Energy** is the capacity and rate budget of transformation;
- **Time**, operationally, is the ratio of rates;
- **Form** is selected possibility;
- **Balance** is viable proportion;
- **Meaning** is compressed relational structure preserved across contexts;
- **Irrelevance** is the kernel of description;
- **Intelligence** is constrained navigation through models;
- **Consciousness** is recursive semantic self-correction under external verification;
- **The substrate** is the constraint envelope of cognition;
- **Artificial intelligence** is externalized informational modeling on an engineered envelope.

The universe may not merely contain information. It may be structured through informational constraint — within energetic bounds, at bounded rates. It may not merely contain intelligence. It may produce intelligence as one of the ways in which its own structure becomes self-aware — and it may insist, as it insists everywhere else, that self-awareness pay its costs and accept its verdicts.

Whether consciousness is limited to biological organisms, whether artificial systems may develop genuine forms of mind, and whether large-scale structures of the universe possess primitive or distributed forms of self-modeling remain open questions. They should remain open.

The task of philosophy in the informational age is not to replace science, mathematics, or engineering. It is to provide the conceptual ground on which they may converge — a ground firm enough to support the weight of what we are building, yet open enough to allow for what we have not yet imagined.

---

## References

[1] J. A. Wheeler, "Information, Physics, Quantum: The Search for Links," in *Complexity, Entropy, and the Physics of Information*, W. H. Zurek (ed.), Addison-Wesley, 1990.

[2] T. Jacobson, "Thermodynamics of Spacetime: The Einstein Equation of State," *Physical Review Letters* 75, 1260–1263 (1995).

[3] J. M. Maldacena, "The Large N Limit of Superconformal Field Theories and Supergravity," *Advances in Theoretical and Mathematical Physics* 2, 231–252 (1998).

[4] L. Bombelli, J. Lee, D. Meyer, R. D. Sorkin, "Space-Time as a Causal Set," *Physical Review Letters* 59, 521–524 (1987).

[5] L. Smolin, *Three Roads to Quantum Gravity*, Basic Books, 2001; "The Case for Background Independence," in *The Structural Foundations of Quantum Gravity*, D. Rickles et al. (eds.), Oxford University Press, 2006.

[6] V. Yakunin, *Causal Phase Geometry Research Program: Minimal Draft, Competing Interpretations of the Phase Layer, and a Program of Experimental Tests* (2026).

[7] V. Yakunin, *KK–Jacobson Commutativity Note: Discrete Causal Structure, U(1) Holonomies, and the Thermodynamic Origin of the Einstein–Maxwell System* (2026).

[8] V. Yakunin, *Unified Implementable Model, Version 2.0: Verifier-Centered Latent World Models with Evidence-Grounded Three-Way Semantics* (2026).

[9] V. Yakunin, *External Ternary Judge Adapter for OpenClaw and DeepSeek V4 API: Engineering Whitepaper* (2026).

[10] V. Yakunin, *ARC-AGI-3 LCLD Agent: Architectural Specification and Engineering Specification* (2026).

[11] N. P. Brusentsov, *Usovershenstvovanie logiki umozaklyucheniy* [The Improvement of Inference Logic], Fond "Novoe tysyacheletie", Moscow, 2012.

[12] R. Landauer, "Irreversibility and Heat Generation in the Computing Process," *IBM Journal of Research and Development* 5, 183–191 (1961).

[13] N. Margolus, L. B. Levitin, "The Maximum Speed of Dynamical Evolution," *Physica D* 120, 188–195 (1998).

[14] L. Mandelstam, I. Tamm, "The Uncertainty Relation Between Energy and Time in Non-Relativistic Quantum Mechanics," *Journal of Physics (USSR)* 9, 249–254 (1945).

[15] J. D. Bekenstein, "Universal Upper Bound on the Entropy-to-Energy Ratio for Bounded Systems," *Physical Review D* 23, 287–298 (1981).

[16] N. Tishby, F. C. Pereira, W. Bialek, "The Information Bottleneck Method," in *Proceedings of the 37th Annual Allerton Conference on Communication, Control and Computing*, 368–377 (1999).

[17] E. P. Hoel, L. Albantakis, G. Tononi, "Quantifying Causal Emergence Shows That Macro Can Beat Micro," *Proceedings of the National Academy of Sciences* 110, 19790–19795 (2013).

[18] S. Lloyd, *Programming the Universe: A Quantum Computer Scientist Takes on the Cosmos*, Knopf, 2006.

[19] S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002; *The Concept of the Ruliad* (2021).

[20] G. Chaitin, *Meta Math! The Quest for Omega*, Vintage, 2005.

[21] D. Deutsch, *The Fabric of Reality*, Allen Lane, 1997.

[22] A. Connes, *Noncommutative Geometry*, Academic Press, 1994.

[23] A. Connes, "Gravity Coupled with Matter and the Foundation of Non-commutative Geometry," *Communications in Mathematical Physics* 182, 155–176 (1996).

[24] A. Connes, C. Rovelli, "Von Neumann Algebra Automorphisms and Time-Thermodynamics Relation in Generally Covariant Quantum Theories," *Classical and Quantum Gravity* 11, 2899–2917 (1994).

---

## Appendix: Core Formulae as Logical Schemata

Most formal expressions in this work are **logical schemata** — compressed conceptual relations intended to make the architecture of the argument visually tractable. Two entries, however, are physical bounds with established derivations; they are marked as such, because the distinction between a schema and a bound is itself one of this text's commitments.

| Expression | Status | Reading |
|--------|--------|---------|
| $\Omega \rightarrow \Omega' \subset \Omega$ | Schema | Restriction of possibility space |
| $\text{Self-Structuring} = G + C + S$ | Schema | Form arises from generation filtered by constraint and selection |
| $\mathcal{B} = \mathcal{V}(G, C, E, S)$ | Schema | Dynamic balance is the viable proportion of freedom, constraint, entropy, and coherence |
| $\nu \leq 2E/\pi\hbar$ | **Physical bound** | Margolus–Levitin: energy caps the rate of distinguishable transitions [13] |
| $W \geq k_B T \ln 2$ per erased bit | **Physical bound** | Landauer: discarding a distinction dissipates energy [12] |
| $d\mathcal{T} \propto (\hbar\, dN / E)\,\eta(M)$ | Schema (bound-anchored) | Operational time as accumulated distinctions, paid from the energy envelope; supersedes the first edition's $dI/E$ |
| $\{0, 1, \emptyset\}$ | Schema | The logic of cognition requires irrelevance as a third state, distinct from falsehood |
| $\ker \pi$ | Formal structure | The irrelevant as the kernel of the descriptive map $\pi$; shared skeleton of coarse-graining and irrelevance |
