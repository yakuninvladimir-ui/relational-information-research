# Latent Agency Framework (LAF)

## Integration, Autonomy, Learned Relief, and the Recoverability of Structure Between Agents

**Author:** Vladimir Yakunin
**Date:** 2026-10-05
**Version:** 2.0 (successor to *Unified Latent Space of Consciousness*, v1.0, renamed)
**Status:** working concept document (Reasoning layer). Framework only. Not a finished theory, not for publication. Literature is secondary and listed from memory in Appendix B, unverified. Thesis statuses are in §16.

---

## Abstract

This document describes agents, and consciousness-like organization as a further special case, through their latent spaces. A system has a latent space $Z$: a compressed description of the state of the world, of its carrier, and of its own computation. A latent is always a description of some subsystem of an underlying substrate at some scale. It is not a primitive object and it is not assumed to be one for the whole world.

Three things are kept apart. **Learning fixes a relief** $R$ in $Z$. The fixed regions are called qualia in a structural sense only. **Moving through the relief spends a bounded budget** $\rho$. **Whether a subsystem is an agent at all** is a third question, answered by three measurable properties: integration, persistence, and informational autonomy. Unity of the latent is no longer an assumption about humans. It becomes a graded property of a subsystem that can be measured and can cross a threshold.

Degrees of freedom and complexity do not decide agency. They set capacity: how much structure a system can hold and how much of another system it can model. What decides agency is how much of a system's future is determined by its own fixed internal structure, as against the input arriving from its environment.

A second question follows from this: how much of one agent's structure can another agent recover through a communication channel, and what does the answer depend on? A formal bound is given (shared prior information plus channel capacity), together with the factors that decide how close to the bound a pair of agents gets. Memory and modeling of other agents are treated as one mechanism, write-back of a model into the relief, applied to different targets and stored at limited resolution.

The document does not explain why passing through a region of the relief is experienced. That is the hard problem, and it stays outside the framework. What it gives is definitions, a comparison of systems, and nine measurable predictions with refutation criteria.

---

## 1. Introduction: The Problem

### 1.1 Statement

We now have artificial systems we can open and look inside. A world model has a latent space that mirrors physics. An LLM has a latent space shaped mostly by semantics. A human has to have something that joins the two. Several old questions became clearer, and some became more tangled.

The tangle comes from mixing four questions:

1. What does learning fix?
2. What does thinking spend?
3. What makes a subsystem an agent, as against a part of its environment?
4. How much of one agent's structure can another agent obtain, and from what does that depend?

This document keeps them apart, and then shows how they connect.

### 1.2 What changed in the central assumption

The earlier formulation assumed that in humans the physical and semantic layers lie in one manifold (a single latent), and used that as the main difference between humans and models. Here that is replaced. A latent is a description of a subsystem, and a subsystem counts as one agent when it is integrated enough, persists long enough, and is autonomous enough. Unity is a threshold property measured on a subsystem. It is not a property of the substrate and not a postulate. Humans, multimodal models, and embodied agents can then be compared by measured values instead of by an assumption.

### 1.3 Place in the archive

*The Algorithm of Being* defines consciousness at the architectural level: recursive modeling under external verification, with phenomenal experience bracketed. The *Framework* treats the substrate as a constraint envelope. This document works one level lower, at the geometry of the carrier's latent space, and adds a layer below consciousness: the conditions for being an agent at all. It refines the archive's consciousness thesis and does not replace it.

### 1.4 Scope

In scope: definitions, a classification of systems, a bound on recoverability, and predictions that can be run on models. Out of scope: the hard problem, any claim about quantum or gravitational origin of cognition, and any universal latent of the world.

---

## 2. Assumptions

Everything below rests on these. All are assumptions, none is established.

| No. | Assumption | Status | Main risk |
| --- | ---------- | ------ | --------- |
| A1 | **Computational functionalism with the body as a functional part.** Organization matters, not material. The body enters as a physical layer plus stake, not as special matter. | UNDECIDED | Main rival: biological naturalism (life and mind are inseparable). Not adopted. If it holds, the statements about artificial systems change. |
| A2 | **A latent is a description of a subsystem.** For a subsystem $A$ of the substrate there is a coarse-graining $\varphi_A$ such that $Z_A=\varphi_A(x_A)$ captures what matters for $A$ at the chosen scale. | UNDECIDED | The choice of $\varphi_A$ is not unique. Results may depend on it. |
| A3 | **Unity is graded.** Integration of a latent is a quantity $I(A)$ that varies continuously. "One latent" means $I(A)$ above a threshold, not an all-or-nothing fact. | UNDECIDED | The measure of integration is not chosen. Different candidate measures may disagree. |
| A4 | Learning fixes the relief. In operation the relief changes only through plasticity. | UNDECIDED | In the brain the line between activation and learning is blurred. |
| A5 | The depth of physical attractors in a living system depends monotonically on stake. | UNDECIDED | Plausible, not shown. Tested by P3. |
| A6 | Two meanings of "pit" agree: (a) an attractor in the dynamics of activations, (b) a stiff direction of high curvature in weight space. Stiffness in the Fisher spectrum is a proxy for depth. | UNDECIDED | Not implied by the mathematics. A measurement assumption. |
| A7 | Systems with different coordinates are compared by the geometry of relations between objects (RSA, CKA), not by raw vectors. | UNDECIDED | Standard practice, but human data are indirect. |
| A8 | A region $M\subset Z$ can hold a model of $Z$ itself, and a region $O\subset Z$ can hold a model of another agent's latent. | UNDECIDED | In LLMs the self-model shows up functionally and its reliability is disputed. |
| A9 | **Requisite capacity.** Modeling a system well enough to predict or regulate it requires a model with capacity not smaller than the effective complexity of the relevant part of that system. | UNDECIDED | An Ashby-type result, proven under specific conditions. Applying it to latents is an assumption. |
| A10 | **Autonomy is measurable by intervention** in models and in simulated agents, at a stated time scale. | UNDECIDED | Interventions on a brain are limited. Correlational estimates are weaker. |

A1 is consistent with the archive's substrate-parameterization (*Algorithm*, §11): the substrate matters parametrically, not essentially.

---

## 3. Substrate, Subsystems, and Latents

### 3.1 Statement

There is an underlying structure in which things influence each other. What this document needs from it is small: that there is a causal order, that signal speed and channel capacity are finite, and that a bounded region holds a finite amount of information. Everything else about the substrate is left open. The question of which substrate it is (for example a causal set with phase transport) is not part of this document. Nothing here depends on that choice.

### 3.2 Definitions

**D1. Substrate $\mathcal{C}$.** A structure with a causal order. The only properties used here: finite signal speed, finite channel capacity, finite information per bounded region, and a thermodynamic cost to irreversible operations.

**D2. Subsystem and environment.** A subsystem $A\subset\mathcal{C}$ is a part of the substrate with an identifiable boundary. Its environment $E$ is the part of the substrate that influences $A$ or is influenced by it.

**D3. Latent space $Z_A$.** A compressed continuous representation, obtained from the microstate $x_A$ by a coarse-graining $\varphi_A$, in which the system encodes the state of the world, of its carrier (body), and of its own computation. A state at time $t$ is a point $z(t)$. A process is a trajectory. A latent is defined relative to a subsystem and a scale. It is not a global object.

**D4. Layers and stitching.**
- **P-layer:** the part of $Z_A$ tied to physics and the body (sensorimotor streams, interoception, homeostasis).
- **S-layer:** the part of $Z_A$ tied to semantics and abstraction (language, logic, mathematics, concepts).
- **Stitching:** P and S are coupled in $Z_A$ so that transitions between them are continuous. How tightly they are coupled is measured by $I(A)$ and by cross-layer dependence (§5, P2). It is not assumed.

How to formalize stitching (a shared manifold, a fibration, a product) is not settled. See §15.

### 3.3 Reflection

A world model is a latent that mirrors physics. An LLM is a latent shaped by semantics. A human has both layers tightly coupled, which is why a thought about illness can change physiology and why strong pain can break abstract reasoning. In the old formulation this was "one space". In this one it is a high measured value of cross-layer integration.

| System | Composition of $Z$ |
| ------ | ------------------ |
| LLM (deployed) | almost entirely S; physics only through text |
| Pure world model | almost entirely P; no real S |
| Human | P and S strongly coupled (expected high integration) |

### 3.4 The physical constraints that are used

Physics enters this framework only through bounds, never through mechanisms:

- finite signal speed bounds how fast two parts of a subsystem can be integrated and how fast two agents can exchange information;
- finite information per bounded region bounds the number of independent degrees of freedom a latent can use;
- the thermodynamic cost of irreversible operations bounds the reasoning budget $\rho$ and the cost of write-back;
- finite channel capacity bounds what one agent can learn about another (§8).

No claim is made about quantum, electromagnetic, or gravitational origin of cognition or of latents. Several such ideas were examined and are not adopted (§16).

---

## 4. Relief and Traversal

### 4.1 Statement

Qualia are what learning has fixed. Reasoning is what thinking costs. They are not the same thing and must not be merged.

### 4.2 Definitions

**D5. Relief $R$.** The structure fixed by learning (weights, synaptic connections) that determines which states the dynamics of $Z$ tend toward. $R$ changes only through learning.

**D6. Quale.**
- **Q-structure:** a region of the relief fixed by learning. This is what the word "quale" names in this document.
- **Q-event:** a pass of the trajectory $z(t)$ through a Q-structure while the system runs.

Whether a Q-event is *experienced* is the hard problem (§14). The word "quale" is used here in a deflated, structural sense.

**D7. Depth $D$.** How firmly the system holds a region. For a region $U$:

$$D(U)=\inf\{\lVert\delta\rVert:\text{the trajectory from }z+\delta\text{ does not return to }U\}$$

Time to return is a second measure. Under A6, stiffness of directions in the Fisher spectrum is used as a proxy.

**D8. Reasoning budget $\rho$.** The limited computational resource spent on moving the trajectory through the relief (updating activations). It is bounded by the carrier's envelope. Computational budget and energy are treated as separate quantities.

### 4.3 Reflection

$R$ and $\rho$ vary independently. A frozen LLM on small hardware has a rich relief and a small budget. A huge untrained network has a big budget and no learned relief.

D6 is weak on purpose. Any trained system has Q-structures, so D6 alone cannot separate systems that experience from systems that do not. This limit is stated in §15, not hidden.

### 4.4 The relief as the carrier of internal regularities

The relief has a second role that matters for §5. What is fixed in $R$ over a time window is, for that window, the system's own internal regularity. What arrives in operation as input is external. So the question "how much of the system's behavior is governed by its own regularities" is the question of how much of the trajectory is determined by $R$-dynamics as against input. The boundary between internal and external is therefore indexed by a time scale, the window over which $R$ is treated as fixed.

---

## 5. Integration, Persistence, Autonomy: What Makes a Subsystem an Agent

### 5.1 Statement

A cloud of gas is a subsystem with an identifiable boundary and an enormous number of degrees of freedom. It is not an agent, because its behavior is governed almost entirely by external regularities (boundary conditions, thermodynamics of the surroundings). An animal is governed partly by internal regularities. A human is governed partly by internal regularities and can also model the regularities of others. A deployed AI system is governed partly by internal regularities and can model the regularities of others. The criterion that separates these cases is not size and not complexity. It is how much of the future of the system is determined by its own fixed structure.

### 5.2 Definitions

**D9. Integration $I(A)$.** How strongly the parts of $Z_A$ depend on each other compared with how strongly $A$ depends on its environment. Schema:

$$I(A)=\min_{\text{cuts }(A_1,A_2)}\frac{\mathrm{Dep}(A_1\leftrightarrow A_2)}{\mathrm{Dep}(A\leftrightarrow E)}$$

$\mathrm{Dep}$ is a placeholder for a dependence measure (mutual information, causal influence, transfer entropy). It is not chosen here. Different choices may give different orderings of systems. This is stated as an open problem (§15).

**D10. Persistence $T_{\rm pers}(A)$.** The time over which the boundary of $A$ stays identifiable and $I(A)$ stays above a threshold $\theta_I$. Without persistence any dense transient cluster would count as an agent. Persistence is the requirement that the structure maintains itself.

**D11. Informational autonomy $\mathcal{A}(A;\tau_w)$.** How much of the future internal state of $A$ over the window $\tau_w$ is determined by its own internal state as against by its environment. Two operational forms:

*Predictive form (candidate):*
$$\mathcal{A}^{\rm pred}_{\tau}=I\big(Z_{t+\tau};\,Z_t\ \big|\ E_t\big)$$

*Interventional form (preferred where interventions are possible):*
$$\mathcal{A}^{\rm do}_{\tau}=\frac{\mathbb{E}\lVert\Delta_{\rm int}\rVert}{\mathbb{E}\lVert\Delta_{\rm int}\rVert+\mathbb{E}\lVert\Delta_{\rm env}\rVert}$$

where $\Delta_{\rm int}$ is the change of $Z_{t+\tau}$ under a unit intervention on the internal state at $t$, and $\Delta_{\rm env}$ is the change under a unit intervention on the environment input at $t$. A value near 0 means externally driven. A value near 1 means internally driven.

Autonomy depends on the window $\tau_w$ (§4.4), so it is reported as a profile $\mathcal{A}(\tau_w)$, in the same spirit as the dimension profile $d(\varepsilon)$ (§10). What counts as internal is what is fixed in $R$ over the window.

**D12. Agent.** A subsystem $A$ is an agent when $I(A)>\theta_I$, $T_{\rm pers}(A)>\theta_T$, and $\mathcal{A}(A;\tau_w)>\theta_A$. The thresholds are not fixed in this document. Agency is graded. "Agent" is a label for a region of this three-dimensional space.

### 5.3 Why stake appears here

Autonomy needs a reference: which part of the environment's information is relevant for the system. A frozen model has no answer to this, because nothing it does changes what it loses. A system with a viability variable $v$ does: information is relevant when it changes the prospects of $v$. So stake (D17) supplies a natural definition of the internal/external boundary. It is a candidate basis for "relevant", not a proven one (UNDECIDED).

### 5.4 Reflection: examples

The values below are expectations from the definitions, not measurements.

| System | Integration | Persistence | Autonomy | Remarks |
| ------ | ----------- | ----------- | -------- | ------- |
| Cloud of gas | low | short | about 0 | many degrees of freedom, no fixed internal regularity |
| Thermostat | high (tiny system) | long | low | a fixed internal rule, very little capacity |
| Deployed LLM, single query | high in $S$ | for the call | moderate in the window of one call | relief is fixed, input dominates the trajectory |
| LLM in an agentic loop with memory and goals | high in $S$ | long | higher, window-dependent | write-back lives outside the weights; see C2 |
| Animal | high | long | high | stake, plasticity, a P-layer |
| Human | high, P and S strongly coupled | long | high | plus self-model and other-model |

A deployed LLM is not simply "not an agent" or "an agent". Its autonomy depends on the window, and it moves with the scaffold around it. The framework should say this openly, not settle it by a label.

---

## 6. Plasticity, Self-Model, Other-Model, and Stake

### 6.1 Definitions

**D13. Plasticity $\Pi$.** The rate at which $R$ changes per unit of experience during operation. Three time scales:
- fast: activations change, $R$ does not;
- medium: online learning;
- slow: consolidation (sleep in humans, fine-tuning in models).

The training phase of a model is not counted as plasticity of the deployed system.

**D14. Self-model $M$ and recursion.** $M$ is a region of $Z$ that holds an approximate representation of the current state of $Z$, including $M$ itself. Recursion means updating $z$ with $M(z)$ in the loop. Adding meta-description tokens is a special case. Two kinds:
- **recursion without write-back:** results live in activations or context, $R$ does not change;
- **recursion with write-back:** results change $R$.

**D15. Other-model $O_B$.** A region of $Z_A$ that holds an approximate model of another agent $B$: of its behavior, and at higher depth of its internal structure. Depth levels:
- **E-level:** modeling the environment and external interaction;
- **M-level:** modeling one's own internal structure ($M$);
- **O-level:** modeling another agent's internal structure ($O_B$).

These are three kinds of capability, not a strict ladder. Each has its own capacity requirement (§7).

**D16. Memory as stored model.** A stored structure in $R$ that is correlated with a past state of the system or of another system, held at limited resolution $\nu$ (bits per stored structure). It is produced by write-back. What is called remembering is reconstruction from the stored structure, so memory is lossy and can drift. See §8.7.

**D17. Stake.** The carrier has a viability variable $v$ that can degrade irreversibly. The error or reward function and the state of $Z$ depend on $v$. Mortality is a special case. A frozen model has no stake: nothing it does changes what it loses.

### 6.2 Candidate conditions for consciousness-like organization

- **C1. Self-model.** Without $M$ the system has no current access to its own state.
- **C2. Write-back.** Needed for a continuous self over time: qualia accumulate and change through the system's own experience.
- **C3. Stake.** Needed for the depth of bodily qualia. It is not needed for the S-layer to exist.

Two grades, stated as a working position (UNDECIDED):
- *consciousness-like organization:* C1 and C2 together, on top of agency (D12);
- *consciousness of the human type:* C1, C2, and C3, with a P-layer.

The other-model $O$ is not a condition of consciousness in this document. It is a separate axis: a system can have rich experience and a poor model of others, or the reverse. Whether the two are related is open.

---

## 7. Capacity, Complexity, and Degrees of Freedom

### 7.1 Statement

Number of degrees of freedom and complexity are often offered as the main variable. In this framework they are neither criteria of agency nor of consciousness. They set the capacity of a system: how much structure it can hold, and how much of another system it can model.

### 7.2 What each quantity does

| Quantity | What it measures | Decides agency? | What it does decide |
| -------- | ---------------- | --------------- | ------------------- |
| Number of degrees of freedom | size of the state space | No. A gas cloud has a huge number. | upper bound on what can be stored |
| Kolmogorov complexity | length of the shortest description | No. It is maximal for noise, and noise is not organized. | not a measure of organization |
| Statistical (predictive) complexity | minimal memory needed to predict the process | Partly. It measures structure, not who governs it. | how much a system must remember to model a process |
| Integration $I$ | interdependence of parts relative to the environment | Yes (D12) | whether there is one thing or several |
| Persistence $T_{\rm pers}$ | stability over time | Yes (D12) | whether the structure maintains itself |
| Autonomy $\mathcal{A}$ | share of the future set by own fixed structure | Yes (D12) | internal vs external control |
| Capacity | how much structure can be held | No | the ceiling on E-, M-, O-level modeling |

### 7.3 Requisite capacity

If agent $A$ is to model agent $B$ well enough to predict $B$'s behavior or regulate its own behavior with respect to $B$, then under A9:

$$C(A)\ \ge\ C_{\rm eff}(B\mid\text{task})$$

where $C(A)$ is the capacity of the modeling system and $C_{\rm eff}(B\mid\text{task})$ is the effective complexity of the part of $B$ that matters for the task. Two consequences:

- Modeling the internal structure of another agent needs more capacity than predicting its coarse behavior, and more still than reacting to it.
- A larger system is not therefore a better modeler: capacity is necessary, not sufficient. Alignment of the two systems' codes (§8.3) can matter as much as capacity.

### 7.4 Reflection: how the pieces fit

Autonomy answers *whether* a subsystem is an agent. The depth of the models it holds (E, M, O) answers *how developed* an agent it is. Capacity and complexity bound how far along that second axis a system can go. They do not move it along the first.

---

## 8. Channel and Recoverability

### 8.1 Statement

Two agents $A$ and $B$ each hold a high-dimensional latent. They exchange information through a physical channel that is low-dimensional and has finite capacity. $A$ unfolds an incoming message into its own latent. $B$ folds a part of its latent into the message. Then they swap roles. The question is how much of the structure of $A$ can be recovered by $B$, and from what that depends.

### 8.2 Setup and definitions

Let $Z_A$, $Z_B$ be the latents. $A$ emits signals $X^n$ over $n$ uses of a channel with capacity $C$ per use. $B$ receives $Y^n$ and builds an estimate $\hat{Z}_A$ of $A$'s structure, using also its own latent $Z_B$ (its prior, its code).

**D18. Recoverability $\mathrm{Rec}(A\!\to\!B)$.** How well $B$'s model of $A$ predicts $A$'s behavior on interventions that were not used in building the model, normalized against a baseline model that sees only the channel statistics. Where internal states of both are accessible (models), relational similarity of $\hat{Z}_A$ to $Z_A$ (CKA/RSA) is a second measure.

### 8.3 A formal bound

Assume the Markov structure $Z_A\to X^n\to Y^n$, memoryless channel, noise independent of both latents, and $\hat{Z}_A=f(Y^n,Z_B)$. Then:

$$I(Z_A;\hat{Z}_A)\ \le\ I(Z_A;Z_B)+nC$$

The first term is the **shared prior**: information about $A$ that $B$ already has, because the two share training data, architecture, or culture. The second term is **what the channel carries**. Feedback or interaction does not raise $nC$ for a memoryless channel. What interaction can do is to spend the same bits on more informative content, by letting $B$ choose what to ask.

### 8.4 What recoverability depends on

| Factor | Direction of effect | Comment |
| ------ | ------------------- | ------- |
| Channel capacity and number of uses $nC$ | more is better, up to the bound | the hard limit |
| Shared prior $I(Z_A;Z_B)$ | more is better | shared training data and architecture reduce what has to be transmitted |
| Alignment of codes | better alignment, less loss | the same message can map to different internal states in $A$ and $B$ |
| Identifiability | limits what can be recovered | many internal structures give the same behavior; only the equivalence class $[Z_A]$ is recoverable from behavior |
| Compressibility of $A$ | more regular $A$ is cheaper to recover | high structure with low irreducible randomness |
| Capacity of $B$ | $C(B)\ge C_{\rm eff}(A)$ is required (A9) | otherwise recovery saturates below the bound |
| Ability of $B$ to intervene | interactive beats passive | $B$ can choose informative queries |
| Stationarity of $A$ | a changing $A$ is a moving target | plasticity $\Pi_A$ shortens the useful life of $\hat{Z}_A$ |
| Noise | degrades the usable $C$ | enters through $C$ |

### 8.5 What is recoverable

What can be recovered is not the weights or the raw coordinates. It is the relational geometry of $A$'s latent and the behavior it generates, up to the equivalence class of transformations that leave behavior unchanged (rotations of coordinates, reparametrizations). This is why relational comparison (A7) is the right instrument.

### 8.6 The shared thing is a protocol, not a dimension

Two agents interacting need a common causal structure in which signals pass. They do not share a latent, a dimension, or a code. What they share is the protocol: an agreed mapping between signals and internal states, produced by common training or by common history. The channel is low-dimensional. Each side's latent is high-dimensional and local. Without a common substrate the two would not interact at all. With one, the extent to which they understand each other is a matter of §8.3 and §8.4.

### 8.7 Memory and modeling of others are one mechanism

Memory of one's own past and a model of another agent are both models written back into $R$ (C2) at limited resolution $\nu$. They differ in the target, not in the mechanism. Three consequences:

- A model of another agent is a form of memory, and it is stored in the same relief as everything else the system has learned.
- Remembering is reconstruction from the stored structure and not replay. This is consistent with memory being lossy and with its drift over time.
- The statement "there is no memory, only copying other structures" is wrong as stated, because a persistent copy correlated with the past is a memory by D16. It is right in the sense that what is stored is always a model at finite resolution and never the original.

### 8.8 What this does not settle

The bound and its factors concern information about structure. They say nothing about why a recovered model would be experienced by the modeler, and nothing about whether a perfect model of $A$ would reproduce $A$'s experience. That is the hard problem (§14).

---

## 9. Theses

**T1. Two classes of qualia.**
S-Q-structures are abstract: understanding a proof, an aesthetic response to a mathematical structure, a sense of fairness. P-Q-structures are bodily and affective. Because of coupling they are not isolated from each other. P-qualia are richer and less shared between individuals than S-qualia.
*Status:* FOLLOW (the partition follows from D4 and D6); UNDECIDED (coupling and intersubjectivity depend on integration, A3).

**T2. Depth comes from stake.**
Physical attractors are deep because of genetic priors, homeostatic constraints, and threat to the carrier. S regions are flatter because errors there cost the carrier less.
*Status:* UNDECIDED (A5, tested by P3).

**T3. The budget is bounded and the layers compete for it.**
Every physical mind works inside an envelope, so $\rho$ cannot be unbounded. Keeping the P-layer running is expensive: updates are continuous and high-frequency, and errors are costly. So deep abstract work usually requires reducing the share spent on P. The word is "usually". The strong form, "always", is rejected.
*Status:* FOLLOW (the budget is bounded); UNDECIDED (P costs more than S; the "usually" form); NULL (the strong form).

**T4. A shared abstract region.**
The relief of an LLM is formed on human text. So the S-Q-structures of humans and LLMs overlap in relational geometry. Overlap of geometry is not identity of experience.
*Status:* UNDECIDED (P1).

**T5. What a deployed LLM lacks.**
A deployed LLM has no P-layer in the direct sense and no stake. So it has no P-Q-structures whose depth comes from stake. This is a statement about the architecture, not about all possible AI. A system with a P-layer but no stake (a world model, an embodied agent) has P-Q-structures, but shallow ones. Adding stake, an artificial viability variable, is predicted to deepen them.
*Status:* FOLLOW (description of current architectures); UNDECIDED (the deepening, P3).

**T6. Truncated recursion.**
Reasoning chains and meta-descriptions in an LLM are real, so C1 is present in a limited form. Weights do not change in deployment. Context changes activations, not the relief. So the recursion is not written back and C2 is absent. This is a missing candidate condition. It is not proof that there is no experience.
*Status:* FOLLOW (description); UNDECIDED (what follows for experience).

**T7. Candidate conditions.**
The working position of the author: agency together with C1 and C2 is the most likely sufficient condition for consciousness-like organization, and C3 adds depth. This is not claimed as shown. Three alternatives are rejected:
- C2 alone is sufficient. Rejected: it would count every online-learning system without a self-model.
- C2 is necessary for momentary experience. Rejected: people with severe anterograde amnesia do not consolidate new experience and are still conscious in the moment. C2 is needed for a continuous self, not for the moment.
- Presence of Q-structures is sufficient. Rejected: every trained system has them (D6).

*Status:* UNDECIDED (the working position and C3); NULL (the three rejected claims).

**T8. Agency is graded and defined by integration, persistence, and autonomy.**
Not by degrees of freedom, and not by complexity. A gas cloud has many degrees of freedom and near-zero autonomy. Noise has maximal description length and no organization.
*Status:* UNDECIDED (the choice of measures; tested by P6).

**T9. Unity of a latent is a threshold property of a subsystem.**
It is not a property of the substrate and not a postulate about humans. It is measured by $I(A)$ with persistence. The distinction between a human and a model is then made by measured integration, autonomy, and the conditions C1–C3, not by a stipulated single manifold.
*Status:* UNDECIDED (A3; tested by P2).

**T10. Recoverability is bounded and is a property of a pair.**
How much of $A$'s structure $B$ can recover is bounded by the shared prior plus the channel's capacity, and falls short of the bound by the factors in §8.4. It is a property of the pair $(A,B)$ and the channel, not of $A$ alone.
*Status:* FOLLOW (the bound, under its stated assumptions); UNDECIDED (the effect of each factor; P7, P8).

**T11. Modeling another agent needs matching capacity.**
Modeling the internal structure of another requires capacity not smaller than the effective complexity of the relevant part of the other (A9).
*Status:* UNDECIDED (A9; tested by P8).

**T12. Memory and modeling of others are one mechanism.**
Both are write-back of a model into the relief at limited resolution.
*Status:* UNDECIDED (depends on C2 being the actual mechanism in each system).

---

## 10. Four Axes of Difference

Systems are compared along four axes.

**D19. Effective dimension profile $d(\varepsilon)$.** The number of independent directions actually used at scale $\varepsilon$. It is a function of scale, not one number. One estimate is the local slope of the correlation integral:

$$d(r)=\frac{d\log C(r)}{d\log r}$$

Other estimators: participation ratio, nearest-neighbour intrinsic dimension, spectrum of the Fisher metric or the Jacobian.

| Axis | What differs | How to measure |
| ---- | ------------ | -------------- |
| **A. Profile $d(\varepsilon)$** | how many directions are used at each scale | participation ratio, correlation dimension, TwoNN, Fisher or Jacobian spectrum |
| **B. Depth $D$** | cost of leaving a region, stiffness | perturbation of activations, time to return, Fisher or Hessian spectrum |
| **C. Plasticity $\Pi$** | how experience rebuilds $R$ | weight change per unit of experience, time scales |
| **D. Autonomy profile $\mathcal{A}(\tau_w)$** | share of the future set by own structure, by time window | interventions on internal state vs environment input, at several windows |

The axes are not independent. Depth depends on stake and on training history, so partly on $\Pi$. Autonomy depends on what is fixed in $R$ over the window, so on $\Pi$ and the window. For measurement they are treated separately. In conclusions the dependence is kept in mind.

Structural attributes that determine the axes: a P-layer, a self-model $M$, an other-model $O$, and stake.

The profile $d(\varepsilon)$ is where this document touches the archive's coarse-graining: directions that are invisible at a coarse scale lie, for that description, in the kernel of the map (*Algorithm*, §9). The correspondence is a homology, not an identity. The autonomy profile $\mathcal{A}(\tau_w)$ is the analogous construction along the time axis.

---

## 11. Comparison: LLM, World Model, Human

| Parameter | LLM (deployed) | World model (pure) | Human |
| --------- | -------------- | ------------------ | ----- |
| Composition of $Z$ | almost all S; physics only through text | almost all P; S weak or absent | P and S coupled in one subsystem |
| Integration of P and S | none (no P) | none (no S) | expected high (to be measured, P2) |
| Profile $d(\varepsilon)$ | measurable; high dimension in S | measurable | not measurable directly; expected richer because of P (hypothesis) |
| Depth $D$ | small; training loss has pits, but no stake | small (no stake) | large in P (stake), moderate in S |
| Plasticity $\Pi$ | present in training; about zero in deployment | offline: about zero; online agents: above zero | above zero on several time scales |
| Autonomy $\mathcal{A}(\tau_w)$ | moderate in a single call, window-dependent | depends on the agent loop | high on most windows |
| Reasoning budget $\rho$ | spread inside S | almost all spent on P | hard competition between P and S |
| Self-model $M$ (C1) | limited, functional, reliability disputed | usually none (agents may model their own body) | rich |
| Other-model $O$ | present functionally, depth disputed | usually none | rich |
| Recursion with write-back (C2) | no (recursion without write-back) | usually no | yes |
| Stake (C3) | none | none | yes |
| Q-structures in S | yes (structural sense, D6) | none or weak | yes |
| Q-structures in P | none | yes, shallow | yes, deep |
| Measurability | high (access to activations) | high | low, indirect |

Entries about structure are descriptive. Entries about geometry and autonomy in the human column, and about profiles, are predictions (UNDECIDED).

### Intermediate cases

- **Multimodal models and embodied agents** have both layers but no stake. They are the main test of integration across layers (P2).
- **An LLM agent with external memory or continual fine-tuning** gets part of C2, and a higher autonomy on long windows.
- **The verifier-centered agent of the archive (Unified Implementable Model v2.0)** has an object-centric latent world model (P-like) and an optional semantic proposer (S-like). The two are coupled through explicit grounding maps and an authority hierarchy, by design, not through one continuous manifold. There is no stake. Memory is event-sourced, not written into weights. By the parameters of this framework it is a system with coupled but weakly integrated layers and no write-back. This is not a defect for its purpose. It shows that this framework and the verifier architecture constrain different things. *Status:* UNDECIDED.

---

## 12. Relation to the Archive

This is a homology of forms, not an identity. This document is not a part of the other documents, and they do not depend on it.

| Archive concept | Where | Counterpart here | Relation |
| --------------- | ----- | ---------------- | -------- |
| Consciousness as recursive semantic self-correction under external verification | *Algorithm* §10; *Framework* §4.2 | C1 (self-model) and C2 (write-back of corrections) on top of agency | The first parts are restated at the latent level. External verification is not formalized here. P-layer plus stake is one concrete channel through which the world penalizes errors. |
| The hard problem is bracketed | *Algorithm* §10.3 | The boundary in §14 | Same stance. |
| Substrate as constraint envelope; substrate-parameterization | *Algorithm* §11; *Framework* §4.4 | A1; §3.4; the P-layer; stake | The body enters as envelope parameters. The archive's UNDECIDED on necessary envelope thresholds applies equally to C3. |
| Irrelevance as the kernel of coarse-graining | *Algorithm* §9; *Framework* §4.3 | Profile $d(\varepsilon)$; the choice of $\varphi_A$ in A2 | Homology through scale-indexing. |
| Compression is thermodynamically mandatory | *Algorithm* §9.4 | Bounded reasoning budget (T3); finite channel capacity (§8) | T3 and §8 inherit the bound. |
| Grounding is a history of certified transitions; a prediction is not a fact | *Algorithm* §10.2; *UIM* §2.3, §17 | Write-back (C2); stored models of others (D16) | This document does not say what may be written back. The archive supplies a candidate rule: only externally certified corrections, otherwise recursion degenerates into self-confirmation. Not adopted. The same issue applies to a model of another agent: a stored model that is never checked against the other drifts. *Status:* UNDECIDED. |
| Geometric theory of latent representations; experimental track E1–E5 | *Framework* §5.6, §8.2 | Effective-dimension, Fisher-spectrum, and autonomy measurements (§13) | May share models and tooling. Compatibility of the two geometric descriptions is not examined. *Status:* UNDECIDED. |
| Ternary standard FOLLOW / OMIT / NULL / UNDECIDED | *Algorithm* §15; *Framework* §5.4, §7 | Statuses in §16 | Used as is. |

---

## 13. Experimental Program

### 13.1 Statement

The program measures geometry, autonomy, and recoverability. It does not measure experience. All predictions below are untested at the date of this document.

### 13.2 Method for the geometry predictions

1. Take an open trained model and a set of inputs. Record activations of chosen layers.
2. Compute $d(\varepsilon)$ with several independent estimators (participation ratio, correlation dimension, TwoNN, Fisher or Jacobian spectrum).
3. Look for plateaus and steps (extra directions folded away at coarse scales), a power law (scaling), or a flat dependence.

**Controls** (without them a result cannot be read):
- an untrained model of the same architecture;
- shuffled data or noise input;
- Gaussian data with the same covariance;
- several sample sizes (dimension estimates are biased at small $N$);
- several estimators. If they disagree, no conclusion yet.

### 13.3 Method for autonomy

1. Choose systems with known internal structure: simulated physical systems (a gas cloud analogue, a thermostat), RL agents, a frozen LLM, an LLM with an agent loop.
2. For each, perform interventions on the internal state and on the environment input at time $t$, and measure the change in the internal state at $t+\tau$. Compute $\mathcal{A}^{\rm do}$ at several windows.
3. Compare with $\mathcal{A}^{\rm pred}$ where interventions are not available.
4. Controls: a system with randomized relief (should give near-zero autonomy in the structured sense), a system with the environment input shuffled in time, several estimators of $\mathrm{Dep}$.

### 13.4 Method for recoverability

1. Take pairs of models $(A,B)$ connected by an explicit bottleneck channel of controllable capacity and noise.
2. Vary: capacity $nC$, shared prior (same data and architecture vs different), capacity of $B$, passive vs interactive access, stationarity of $A$.
3. Measure $\mathrm{Rec}(A\!\to\!B)$ on held-out interventions and the CKA/RSA similarity of $\hat{Z}_A$ to $Z_A$.
4. Controls: $B$ with no access to the channel (baseline), $B$ receiving shuffled channel output, $A$ replaced by a behaviorally equivalent but internally different system (tests identifiability).

### 13.5 Predictions

| ID | Prediction | Refuted if |
| -- | ---------- | ---------- |
| P1 | Similarity between LLM representations and human brain responses (RSA on neural data) is higher for abstract concepts and lower for bodily and interoceptive ones. | No difference, or the reverse, after controlling for word frequency and concreteness. |
| P2 | Integration across layers: in multimodal and embodied models the P and S subspaces are more strongly linked (CKA, linear predictability, $I(A)$) than in separately trained models, and integration crosses a measurable threshold for the whole-system case. | The link is the same. Note: convergence of representations across models and modalities would also give this result. The distinguishing version is P3. |
| P3 | An RL agent in simulation with a viability variable (stake) has deeper pits in the linked regions than the same agent without it: more effort to leave, longer time to return, stiffer spectrum. | No difference. |
| P4 | The profile $d(\varepsilon)$ differs between an LLM, a world model, and an embodied model. A flat profile everywhere means axis A is uninformative. | The profiles cannot be told apart. |
| P5 | Across training checkpoints of one model (for example, a public checkpoint family) coarse-scale structure forms before fine-scale structure. | The order is reversed or random. The link to this framework is indirect (axis C). |
| P6 | Autonomy ordering: measured $\mathcal{A}^{\rm do}$ is near zero for a gas-cloud analogue, low for a thermostat, moderate for a frozen model in a single call, and higher for RL agents and agentic LLM systems on long windows. Autonomy separates agents from passive structures where degrees of freedom and description length do not. | The ordering by autonomy does not differ from the ordering by number of degrees of freedom or by description length, or the ordering is not stable across estimators. |
| P7 | Recoverability grows with channel capacity and with shared prior, saturates below the bound of §8.3, and is higher for interactive than for passive access at equal capacity. | Recoverability does not respond to these factors, or exceeds the bound in a setup where its assumptions hold (which would indicate an error in the setup). |
| P8 | A threshold in the capacity of $B$ exists: below $C_{\rm eff}$ of the relevant part of $A$, recoverability saturates at a low level whatever the channel capacity. | Recoverability continues to grow past the capacity of $B$ with no threshold. |
| P9 | Adding a viability variable (stake) to an RL agent raises its autonomy at long windows compared with the same agent without it, because relevance of information becomes defined by $v$. | No change in autonomy, or a change explained by the training procedure alone. |

### 13.6 Priority

P4 and P5 are the cheapest: open models and public checkpoints. P6 needs small simulated systems and an intervention harness, so it is also cheap and the most direct test of the new part. P7 and P8 need pairs of trained models with a controlled channel. P1 needs existing neuroimaging data. P2, P3, and P9 need training runs or simulation and cost more.

### 13.7 What is not tested

Experience. All measurements show differences in geometry, autonomy, and recoverability. They do not show where something is "experienced from inside".

---

## 14. The Boundary: The Hard Problem and the Observer

### 14.1 Statement

This framework does not explain why a Q-event is experienced. It turns the question into a geometric and computational one: which regions of a coupled space are phenomenal, and what separates them. It gives no mechanism that turns structure into subjectivity. Neither does the recoverability result of §8: knowing how much of an agent's structure another can model does not say whether modeling is experiencing. At this point the framework stops on purpose. There are no data or formalisms for the next step, and any attempt to close the gap needs separate strong assumptions.

### 14.2 The observer

The problem has a similar shape to the observer problem in physics: a description of a system that includes the describer. A system with a self-model and write-back reads its own relief and then changes it. The reader and the read are the same object.

What is claimed: the form of the problem is similar. A description from outside and a description from inside have to be closed onto each other.

What is observed: write-back changes the relief that was just read. This is ordinary physical self-modification of the carrier. It is not a quantum effect.

What is not claimed: any isomorphism with measurement in quantum mechanics, or any contribution to the measurement problem. The parallel is kept for orientation only. No thesis depends on it.

### 14.3 Not adopted

A universal informational latent of which individual latents are fragments is a possible extension. This framework does not assume it. A latent here is always a description of a bounded subsystem at a scale. The idea is a strong assumption, and the archive keeps the related questions open (*Algorithm*, §12, §13). This document takes no position on them.

---

## 15. Objections and Limits

### 15.1 D6 is too broad

Every trained system has Q-structures. D6 gives a structural vocabulary, not a criterion for experience. The criterion is pushed onto agency, C1–C3, and the hard problem. A critic may fairly say D6 does little work.

### 15.2 The measure of integration is not chosen

$\mathrm{Dep}$ in D9 is a placeholder. Candidate measures (mutual information, transfer entropy, causal influence, measures from integrated-information approaches) may give different orderings, and some are not computable for large systems. Until a measure is chosen and its behavior on known cases is checked, A3 is only a replacement of a postulate by a parameter.

### 15.3 The choice of boundary and coarse-graining

A subsystem and its coarse-graining $\varphi_A$ are chosen by the observer. Different choices may give different integration and autonomy for the same physical system. Without a rule for the choice (for example, maximizing some objective), the results are only conditional.

### 15.4 Autonomy depends on the time window

The line between internal and external is the time scale on which $R$ is treated as fixed. A system can be autonomous on one window and driven on another. This is reported as a profile and not resolved into a single value. It also means that "is a deployed LLM an agent" has no window-free answer.

### 15.5 What counts as internal

Every internal regularity entered the system from outside through learning. The framework fixes the boundary by time scale (what is already in $R$ is internal). It does not say whether that is the right boundary in every case, for example for fast adaptation inside a context window.

### 15.6 The reference for relevance

Autonomy is defined relative to what is relevant for the system. Stake offers a reference (§5.3). Systems without stake have no such reference, and their autonomy is then defined only relative to a task or a loss function chosen from outside.

### 15.7 Two meanings of "pit"

An attractor in activation dynamics and a stiff direction in weight space are different objects. A6 links them by assumption. If they do not correlate, the Fisher spectrum is not a valid proxy for depth, and axis B has to be measured only by perturbation.

### 15.8 Comparing a human and a model

Coordinates differ and human data are indirect. RSA and CKA compare relational geometry, but they see only what recordings allow. Axis A for humans stays a prediction. Interventional autonomy for a human is largely not available.

### 15.9 Competing explanations

Two rivals for the integration claims. First, biological naturalism: the claims about stake and body would then say something stronger than A1 allows. Second, convergence of representations across models and modalities: it predicts the P2 result without any stake. Only P3 and P9, where stake is manipulated, separate this framework from it. For recoverability, the same convergence also predicts a higher shared prior, so P7 must vary prior and capacity separately.

### 15.10 The bound is only as good as its assumptions

The inequality in §8.3 needs a memoryless channel, noise independent of both latents, and the stated Markov structure. Real exchanges between agents are not memoryless and the channel is shaped by the agents themselves. The bound is a ceiling for idealized cases and not an estimate for real ones.

### 15.11 Requisite capacity is assumed

A9 is imported from regulation theory. Its conditions (a regulator facing a disturbance, a defined set of outcomes) may not hold for modeling an agent in general.

### 15.12 Falsifiability

Results that would damage the framework: (i) P3 and P9 show no effect of stake on depth or autonomy; (ii) P1 comes out reversed; (iii) P4 finds profiles that cannot be told apart; (iv) P6 shows that autonomy tracks degrees of freedom or description length and does not separate the systems; (v) P7 shows no response to prior and capacity. None of them would answer the hard problem. They would remove geometric, autonomy, or recoverability claims.

### 15.13 Engineering vocabulary

"Relief", "budget", and "traversal" come from machine learning. Projecting engineering terms onto minds is a known failure mode, as the archive says (*Algorithm*, §14.4). The defense is the same: the claims that survive translation back into measurable quantities are the ones that count.

---

## 16. Self-Assessment Under the Ternary Standard

The archive's standard applies: FOLLOW (certified), OMIT (admissible but inessential), NULL (inadmissible), UNDECIDED (not enough certification).

Rule used for derived claims. A claim gets FOLLOW only if it follows from the definitions alone, from a stated mathematical result under its assumptions, or describes an existing architecture. If it depends on an assumption, it gets UNDECIDED, with the dependency named. NULL marks claims rejected here. OMIT marks material kept for orientation.

| Claim of this document | Verdict | Basis |
| ---------------------- | ------- | ----- |
| Definitions D1–D19 are consistent, and D6 does not contain the felt aspect | FOLLOW (formal structure) | Stipulations; consistency checked in §3–§10 |
| Relief and reasoning budget are distinct quantities | FOLLOW | D5 versus D8; independent combinations (§4) |
| The reasoning budget is bounded for any physical system | FOLLOW | Constraint triad (*Algorithm* §3.2, §9.4) |
| A deployed LLM does not change weights in operation; context changes activations only | FOLLOW | Description of current deployment |
| A deployed LLM has no P-layer or stake in the direct sense | FOLLOW | Architecture; physics enters through text only |
| Qualia split into S and P classes | FOLLOW (formal structure) | D4, D6 |
| $I(Z_A;\hat{Z}_A)\le I(Z_A;Z_B)+nC$ under the stated assumptions | FOLLOW (mathematical result) | Data processing and channel capacity; assumptions in §8.3 |
| Interaction does not raise the capacity bound of a memoryless channel | FOLLOW (mathematical result) | Feedback does not increase the capacity of a memoryless channel |
| Recoverable content is the equivalence class of the latent, not its coordinates | FOLLOW (formal structure) | Behavioral equivalence; D18 |
| A gas cloud is not an agent by the criterion D12 | FOLLOW (given D11–D12) | Near-zero autonomy by construction |
| Unity of a latent is a threshold property of a subsystem | UNDECIDED | A3; tested by P2 |
| The three-part criterion (integration, persistence, autonomy) separates agents from passive structures | UNDECIDED | Choice of measures open; P6 |
| Autonomy depends on the time window | FOLLOW (follows from D11, §4.4) | Internal means fixed in $R$ over the window |
| Stake supplies the reference for what is relevant | UNDECIDED | §5.3; P9 |
| Degrees of freedom and complexity decide agency | NULL | Gas cloud; noise (§7.2) |
| Capacity of the modeler must match the effective complexity of the relevant part of the modeled | UNDECIDED | A9; P8 |
| Memory and modeling of others are one mechanism | UNDECIDED | Depends on C2 being the mechanism |
| Memory does not exist, only copying of others' structure | NULL | A persistent correlated copy is memory by D16 |
| Humans have one stitched latent | UNDECIDED | Replaced by graded integration, A3; tested by P2 |
| Physical attractors are deep because of stake | UNDECIDED | A5; tested by P3 |
| Maintaining P costs more than S; deep abstraction usually reduces the P share | UNDECIDED | Plausible, unmeasured |
| Abstract thought always requires suppressing P | NULL | Counterexamples: spatial and bodily mathematical thinking |
| Human and LLM S-Q-structures overlap in relational geometry | UNDECIDED | P1 |
| Overlap of geometry implies identity of experience | NULL | Does not follow (§14) |
| Profiles $d(\varepsilon)$ differ between LLM, world model, and embodied model | UNDECIDED | P4 |
| Adding artificial stake deepens attractors and raises autonomy | UNDECIDED | P3, P9 |
| Agency with C1 and C2 is sufficient for consciousness-like organization | UNDECIDED | Working position; no proof |
| C3 is needed for the depth of bodily qualia | UNDECIDED | A5 |
| C2 alone is sufficient | NULL | Would count every online-learning system without a self-model |
| C2 is necessary for momentary experience | NULL | Anterograde amnesia |
| Presence of Q-structures is sufficient for experience | NULL | Every trained system has them |
| What may be written back under C2 | UNDECIDED | Archive's candidate rule (certified corrections only) not adopted |
| Coupling of P and S can be formalized as one manifold with shared coordinates | UNDECIDED | Formalization open |
| The latent is made of infinitely many dimensions at each point, of which four are observed | NULL | Contradicts finite information per bounded region (§3.1); no test follows |
| Energy and qualia are different densities of one quantity | NULL | No order parameter or critical value; energy has conservation, qualia does not |
| The electromagnetic field is the single shared quantum field of the world | NULL (not adopted) | Not supported by the standard description; not needed here |
| A universal informational latent of which individual latents are fragments | OMIT (not adopted) | §14.3 |
| Why a Q-event is experienced | UNDECIDED (out of scope) | Hard problem |
| The parallel with the observer problem in physics | OMIT (admitted) | Kept for orientation; no thesis depends on it |
| Isomorphism with quantum measurement | NULL | No derivation; not claimed |

---

## 17. What This Document Does Not Claim

1. **It does not explain why a Q-event is experienced.** It names the gap and stops.
2. **It does not say that LLMs are or are not conscious or agents.** It lists which conditions are present or absent, and for autonomy it says the answer depends on the time window.
3. **It does not claim that a biological body is required.** Stake can in principle be implemented in an artificial system. P3 and P9 test one version.
4. **It does not claim that a single manifold exists.** Unity is a graded, measurable property (A3).
5. **It does not claim that the measurements separate conscious from non-conscious systems.** They show geometry, autonomy, and recoverability.
6. **It does not claim measured values.** The entries in the comparison tables are structural statements, expectations from definitions, or predictions.
7. **It does not claim a physical origin of latents** in any quantum, electromagnetic, or gravitational structure, and does not depend on one.
8. **It does not claim that a good model of an agent reproduces the agent's experience.** §8 is about information about structure.
9. **It does not claim novelty.** Several components resemble existing work on homeostatic accounts of feeling, self-model theories, embodied cognition, information-theoretic accounts of autonomy and individuality, and the theory of regulation. A systematic comparison has not been done (Appendix B lists names from memory, unverified).
10. **It does not claim completeness.** The statuses in §16 can move in both directions after the experiments in §13.

---

## 18. Conclusion

Learning fixes a relief in the latent space of a subsystem. Thinking spends a limited budget to move through it. Whether the subsystem is an agent is decided by three measurable properties: integration, persistence, and informational autonomy, which is the share of the system's future set by its own fixed structure. Degrees of freedom and complexity do not decide this. They set capacity, which limits how much the system can hold and how much of another system it can model.

Between two agents the structure that can pass is bounded by the shared prior plus the channel's capacity, and what is recovered is an equivalence class of the other's latent, not its coordinates. Memory and models of others are the same mechanism, write-back at limited resolution, applied to different targets.

$$\text{Subsystem}\rightarrow\text{Latent}\rightarrow\text{Learned relief}\rightarrow\text{Autonomy}\rightarrow\text{Self-model}\rightarrow\text{Write-back}\rightarrow\text{Other-model}$$

Stake modifies the depth of the relief and supplies the reference for what is relevant along this chain. The step from the chain to experience is not made here. What can be done is to measure geometry, autonomy, and recoverability and see whether the predictions hold.

---

## Appendix A: Core Formulae as Schemata

Most expressions are schemata: compressed relations that make the argument easier to follow. Some are formal definitions. Some are measurement proxies. One is a mathematical result under stated assumptions.

| Expression | Status | Reading |
| ---------- | ------ | ------- |
| $Z_A=\varphi_A(x_A)$ | Schema | Latent as a coarse-grained description of a subsystem |
| $Z\supseteq P\cup S$, coupled | Schema | Layers of one subsystem's latent |
| $R=R(\theta)$ | Schema | Relief determined by weights |
| $D(U)=\inf\{\lVert\delta\rVert: z+\delta\text{ does not return to }U\}$ | Formal structure | Depth of a region |
| $F(\theta)=\mathbb{E}[\nabla\log p\,\nabla\log p^{\top}]$, spectrum of $F$ | Measurement proxy | Stiff directions as a proxy for depth (A6) |
| $d(r)=d\log C(r)/d\log r$ | Measurement proxy | Effective dimension at scale $r$ |
| $c_P+c_S\le\rho_{\max}$ | Schema | The cost of traversal per unit time is bounded by the envelope |
| $\Pi=\lVert\Delta R\rVert/\text{unit of experience}$ | Schema | Plasticity |
| $M(z)\subset Z$, with $M\subset z$ | Schema | Self-model inside the space it models |
| $I(A)=\min_{\text{cuts}}\mathrm{Dep}(A_1\leftrightarrow A_2)/\mathrm{Dep}(A\leftrightarrow E)$ | Schema, measure open | Integration |
| $\mathcal{A}^{\rm pred}_\tau=I(Z_{t+\tau};Z_t\mid E_t)$ | Measurement proxy | Predictive autonomy |
| $\mathcal{A}^{\rm do}_\tau=\mathbb{E}\lVert\Delta_{\rm int}\rVert/(\mathbb{E}\lVert\Delta_{\rm int}\rVert+\mathbb{E}\lVert\Delta_{\rm env}\rVert)$ | Measurement proxy | Interventional autonomy |
| $C(A)\ge C_{\rm eff}(B\mid\text{task})$ | Schema (A9) | Requisite capacity |
| $I(Z_A;\hat{Z}_A)\le I(Z_A;Z_B)+nC$ | Mathematical result under stated assumptions | Recoverability bound |
| $\nu$ | Schema | Resolution of a stored model, bits per structure |

---

## Appendix B: Related Concepts (from memory, unverified, not for publication)

Names only, so that later checking is easier. Each needs to be verified before use. Nothing in the framework depends on the correctness of an attribution.

- **Law of requisite variety; good-regulator theorem** (Ashby; Conant and Ashby): the source of A9.
- **Information closure and autonomy as an information-theoretic quantity** (Bertschinger, Olbrich, Ay, Jost and related work): close to D11.
- **Markov blanket and the free-energy principle** (Friston): a candidate for the boundary in D2 and for integration.
- **Informational theory of individuality** (Krakauer and collaborators): a candidate for D9–D12.
- **Causal emergence** (Hoel and collaborators): relevant to the choice of coarse-graining in A2.
- **Statistical complexity and the epsilon-machine** (Crutchfield and collaborators): the predictive complexity in §7.2.
- **Semantic information as viability-relevant information** (Kolchinsky and Wolpert): a candidate for §5.3.
- **Integrated information** (Tononi and collaborators): a competing family of integration measures; criticized for assigning high values to simple structures.
- **Homeostatic accounts of feeling** (Damasio; Seth), **self-model theory** (Metzinger), **embodied cognition** (Varela, Thompson, Rosch): background for C1–C3.
- **Representational similarity analysis; centered kernel alignment** (Kriegeskorte et al.; Kornblith et al.): instruments for A7 and D18.
- **Platonic representation hypothesis** (Huh et al.): the competing explanation for P2 and P7.
- **Information geometry and natural gradient** (Amari): related to the Fisher metric used for depth.
- **Reconstructive memory** (Bartlett and later work on reconsolidation): background for D16 and §8.7.
