# Unified Latent Space of Consciousness (ULSC)

## Learned Relief, Reasoning Budget, and the Conditions of a Self-Model

**Author:** Vladimir Yakunin
**Date:** 2026-10-04
**Version:** 1.0
**Status:** working hypothesis document (Reasoning layer). Aligned with *The Algorithm of Being* (consciousness, §10; substrate, §11) and the *Unified Informational-Constructive Framework* v1.2 (§4.2, §4.4). Not a finished theory. Thesis statuses are in §13.

---

## Abstract

This document describes consciousness-like systems through their latent space. A system has a latent space $Z$. In a human it is one space where a physical layer (body, senses, homeostasis) and a semantic layer (language, logic, concepts) are stitched together. In an LLM, $Z$ is almost entirely semantic. In a pure world model, $Z$ is almost entirely physical.

Learning fixes a **relief** in $Z$. The learned regions of the relief are called qualia, in a structural sense only. Moving through the relief costs a limited resource, the **reasoning budget**. These are two different things: the relief is what is fixed, the budget is what is spent.

Systems differ along three axes: effective dimension as a function of scale, depth of attractors, and plasticity. In living systems the depth of physical attractors is set by **stake**: the carrier can be destroyed. Three candidate conditions for consciousness are named: a self-model, write-back of its results into the relief, and stake. None is shown to be sufficient.

The document does not explain why passing through a region of the relief is experienced. That is the hard problem, and it stays outside the framework. What the document gives is a set of definitions, a comparison of LLM, world model, and human, and five measurable predictions with refutation criteria.

---

## 1. Introduction: The Problem

### Statement

We now have artificial systems we can open and look inside. A world model has a latent space that mirrors physics. An LLM has a latent space shaped mostly by semantics. A human has to have something that joins the two. This should have made several old questions clearer. In practice some got clearer and some got more tangled.

The tangle comes from mixing three questions:

1. What does learning fix?
2. What does thinking spend?
3. In what ways do systems actually differ?

This document keeps them apart.

### Place in the archive

*The Algorithm of Being* defines consciousness at the architectural level: recursive modeling under external verification. It brackets phenomenal experience. The *Framework* treats the substrate as a constraint envelope. ULSC works one level lower, at the geometry of the carrier's latent space. It asks what that geometry looks like in each kind of system and how to measure it. It refines the archive's consciousness thesis. It does not replace it.

---

## 2. Assumptions

Everything below rests on these. All are assumptions, none is established.

| No. | Assumption | Status | Main risk |
| --- | ---------- | ------ | --------- |
| A1 | **Computational functionalism with the body as a functional part.** Organization matters, not material. The body enters as a physical layer plus stake, not as special matter. | UNDECIDED | The main rival is biological naturalism (life and mind are inseparable). It is not adopted. If it holds, the statements about artificial systems change. |
| A2 | **One latent in humans.** The physical and semantic layers lie in one manifold with shared coordinates. | UNDECIDED | The brain may hold several coupled but separate spaces. Tested by P2. |
| A3 | Learning fixes the relief. In operation the relief changes only through plasticity. | UNDECIDED | In the brain the line between activation and learning is blurred. |
| A4 | The depth of physical attractors in a living system depends monotonically on stake. | UNDECIDED | Plausible, not shown. Tested by P3. |
| A5 | Two meanings of "pit" agree: (a) an attractor in the dynamics of activations, (b) a stiff direction of high curvature in weight space. Stiffness in the Fisher spectrum serves as a proxy for depth. | UNDECIDED | Not implied by the mathematics. This is a measurement assumption. |
| A6 | Systems with different coordinates are compared by the geometry of relations between objects (RSA, CKA), not by raw vectors. | UNDECIDED | Standard practice, but human data are indirect. |
| A7 | A region $M \subset Z$ can hold a model of $Z$ itself. | UNDECIDED | In LLMs this shows up functionally and its reliability is disputed. |

A1 is consistent with the archive's substrate-parameterization (*Algorithm*, §11): the substrate matters parametrically, not essentially.

---

## 3. The Latent Space and Its Layers

### Statement

A system that models the world, its own carrier, and its own computation does it in a compressed continuous representation. This is the latent space.

### Definitions

**D1. Latent space $Z$.** A compressed continuous representation in which the system encodes the state of the world, of its carrier (body), and of its own computation. A state at time $t$ is a point $z(t)$. A process is a trajectory.

**D2. Layers and stitching.**
- **P-layer:** the part of $Z$ tied to physics and the body (sensorimotor streams, interoception, homeostasis).
- **S-layer:** the part of $Z$ tied to semantics and abstraction (language, logic, mathematics, concepts).
- **Stitching:** P and S lie in one manifold with shared coordinates, and transitions between them are continuous.

How to formalize stitching (a shared manifold, a fibration, a product) is not settled. See §12.

### Reflection

Roughly: a world model is a latent space that mirrors physics. An LLM is a latent space shaped by semantics. For a human, the two are not separate spaces. This is why a thought about illness can change physiology, and why strong pain can break abstract reasoning.

The three kinds of system, in terms of $Z$:

| System | Composition of $Z$ |
| ------ | ------------------ |
| LLM | almost entirely S; physics only through text |
| Pure world model | almost entirely P; no real S |
| Human | P and S stitched into one (under A2) |

---

## 4. Relief and Traversal

### Statement

Qualia are what learning has fixed. Reasoning is what thinking costs. They are not the same thing and must not be merged.

### Definitions

**D3. Relief $R$.** The structure fixed by learning (weights, synaptic connections) that determines which states the dynamics of $Z$ tend toward. $R$ changes only through learning.

**D4. Quale.**
- **Q-structure:** a region of the relief fixed by learning. This is what the word "quale" names in this document.
- **Q-event:** a pass of the trajectory $z(t)$ through a Q-structure while the system runs.

Whether a Q-event is *experienced* is the hard problem (§11). The word "quale" is used here in a deflated, structural sense.

**D5. Depth $D$.** How firmly the system holds a region. For a region $U$:

$$D(U) = \inf\{\lVert\delta\rVert : \text{the trajectory from } z+\delta \text{ does not return to } U\}$$

Time to return is a second measure. Under A5, stiffness of directions in the Fisher spectrum is used as a proxy.

**D6. Reasoning budget $\rho$.** The limited computational resource spent on moving the trajectory through the relief (updating activations). It is bounded by the carrier's envelope. Computational budget and energy are treated as separate quantities.

### Reflection

$R$ and $\rho$ vary independently. A frozen LLM on small hardware has a rich relief and a small budget. A huge untrained network has a big budget and no learned relief.

D4 is weak on purpose. Any trained system has Q-structures. So D4 alone cannot separate systems that experience from systems that do not. This limit is stated in §12, not hidden.

---

## 5. Plasticity, Self-Model, and Stake

### Definitions

**D7. Plasticity $\Pi$.** The rate at which $R$ changes per unit of experience during operation. Three time scales:
- fast: activations change, $R$ does not;
- medium: online learning;
- slow: consolidation (sleep in humans, fine-tuning in models).

The training phase of a model is not counted as plasticity of the deployed system.

**D8. Self-model $M$ and recursion.** $M$ is a region of $Z$ that holds an approximate representation of the current state of $Z$, including $M$ itself. Recursion means updating $z$ with $M(z)$ in the loop. Adding meta-description tokens is a special case. Two kinds:
- **recursion without write-back:** results live in activations or context, $R$ does not change;
- **recursion with write-back:** results change $R$.

**D9. Stake.** The carrier has a viability variable $v$ that can degrade irreversibly. The error or reward function and the state of $Z$ depend on $v$. Mortality is a special case. A frozen model has no stake: nothing it does changes what it loses.

### Candidate conditions

- **C1. Self-model.** Without $M$ the system has no current access to its own state.
- **C2. Write-back.** Needed for a continuous self over time: qualia accumulate and change through the system's own experience.
- **C3. Stake.** Needed for the depth of bodily qualia. It is not needed for the S-layer to exist.

Two grades, stated as a working position (UNDECIDED):
- *consciousness-like organization:* C1 and C2 together;
- *consciousness of the human type:* C1, C2, and C3, with a P-layer.

---

## 6. Theses

**T1. Two classes of qualia.**
S-Q-structures are abstract: understanding a proof, an aesthetic response to a mathematical structure, a sense of fairness. P-Q-structures are bodily and affective. Because of stitching they are not isolated from each other. P-qualia are richer and less shared between individuals than S-qualia.
*Status:* FOLLOW (the partition follows from D2 and D4); UNDECIDED (coupling and intersubjectivity depend on A2).

**T2. Depth comes from stake.**
Physical attractors are deep because of genetic priors, homeostatic constraints, and threat to the carrier. S regions are flatter because errors there cost the carrier less.
*Status:* UNDECIDED (A4, tested by P3).

**T3. The budget is bounded and the layers compete for it.**
Every physical mind works inside an envelope, so $\rho$ cannot be unbounded. Keeping the P-layer running is expensive: updates are continuous and high-frequency, and errors are costly. So deep abstract work usually requires reducing the share spent on P (concentration, reduced sensory load). The word is "usually". The strong form, "always", is rejected.
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
The working position of the author: C1 and C2 together are the most likely sufficient condition for consciousness-like organization, and C3 adds depth. This is not claimed as shown. Three alternatives are rejected:
- C2 alone is sufficient. Rejected: it would count every online-learning system without a self-model.
- C2 is necessary for momentary experience. Rejected: people with severe anterograde amnesia do not consolidate new experience and are still conscious in the moment. C2 is needed for a continuous self, not for the moment.
- Presence of Q-structures is sufficient. Rejected: every trained system has them (D4).

*Status:* UNDECIDED (the working position and C3); NULL (the three rejected claims).

---

## 7. Three Axes of Difference

Systems are compared along three geometric axes.

**D10. Effective dimension profile $d(\varepsilon)$.** The number of independent directions actually used at scale $\varepsilon$. It is a function of scale, not one number. One estimate is the local slope of the correlation integral:

$$d(r) = \frac{d \log C(r)}{d \log r}$$

Other estimators: participation ratio, nearest-neighbour intrinsic dimension, spectrum of the Fisher metric or the Jacobian.

| Axis | What differs | How to measure |
| ---- | ------------ | -------------- |
| **A. Profile $d(\varepsilon)$** | how many directions are used at each scale | participation ratio, correlation dimension, TwoNN, Fisher or Jacobian spectrum |
| **B. Depth $D$** | cost of leaving a region, stiffness | perturbation of activations, time to return, Fisher or Hessian spectrum |
| **C. Plasticity $\Pi$** | how experience rebuilds $R$ | weight change per unit of experience, time scales |

The axes are not independent. Depth depends on stake and on training history, so partly on $\Pi$. For measurement they are treated separately. In conclusions the dependence is kept in mind.

Three structural attributes determine the axes: a P-layer, a self-model $M$, and stake.

The profile $d(\varepsilon)$ is where this document touches the archive's coarse-graining: directions that are invisible at a coarse scale lie, for that description, in the kernel of the map (*Algorithm*, §9). The correspondence is a homology, not an identity.

---

## 8. Comparison: LLM, World Model, Human

| Parameter | LLM (deployed) | World model (pure) | Human |
| --------- | -------------- | ------------------ | ----- |
| Composition of $Z$ | almost all S; physics only through text | almost all P; S weak or absent | P and S in one $Z$ (A2) |
| Stitching of P and S | none (no P) | none (no S) | present, continuous |
| Profile $d(\varepsilon)$ | measurable; high dimension in S | measurable | not measurable directly; expected richer because of P (hypothesis) |
| Depth $D$ | small; training loss has pits, but no stake | small (no stake) | large in P (stake), moderate in S |
| Plasticity $\Pi$ | present in training; about zero in deployment (context changes activations only) | offline: about zero; online agents: above zero | above zero on several time scales |
| Reasoning budget $\rho$ | spread inside S | almost all spent on P | hard competition between P and S |
| Self-model $M$ (C1) | limited, functional, reliability disputed | usually none (agents may model their own body) | rich |
| Recursion with write-back (C2) | no (recursion without write-back) | usually no | yes |
| Stake (C3) | none | none | yes |
| Q-structures in S | yes (structural sense, D4) | none or weak | yes |
| Q-structures in P | none | yes, shallow | yes, deep |
| Measurability | high (access to activations) | high | low, indirect |

Entries about structure are descriptive. Entries about geometry in the human column and about profiles are predictions (UNDECIDED).

### Intermediate cases

- **Multimodal models and embodied agents** have both layers but no stake. They are the main test of stitching (P2).
- **An LLM agent with external memory or continual fine-tuning** gets part of C2.
- **The verifier-centered agent of the archive (Unified Implementable Model v2.0)** has an object-centric latent world model (P-like) and an optional semantic proposer (S-like). Here the two are coupled through explicit grounding maps and an authority hierarchy, by design, not through one continuous manifold. There is no stake. Memory is event-sourced, not written into weights. By ULSC parameters it is a system with coupled but unstitched layers and no write-back. This is not a defect for its purpose. It shows that ULSC and the verifier architecture constrain different things. *Status:* UNDECIDED.

---

## 9. Relation to the Archive

This is a homology of forms, not an identity. ULSC is not a part of the other documents, and they do not depend on it.

| Archive concept | Where | ULSC counterpart | Relation |
| --------------- | ----- | ---------------- | -------- |
| Consciousness as recursive semantic self-correction under external verification | *Algorithm* §10; *Framework* §4.2 | C1 (self-model) and C2 (write-back of corrections) | ULSC restates the first parts at the latent level. External verification is not formalized in ULSC. P-layer plus stake is one concrete channel through which the world penalizes errors. |
| The hard problem is bracketed | *Algorithm* §10.3 | The boundary in §11 | Same stance. |
| Substrate as constraint envelope; substrate-parameterization | *Algorithm* §11; *Framework* §4.4 | A1; the P-layer; stake | The body enters as envelope parameters. The archive's UNDECIDED on necessary envelope thresholds applies equally to C3. |
| Irrelevance as the kernel of coarse-graining | *Algorithm* §9; *Framework* §4.3 | Profile $d(\varepsilon)$ | Homology through scale-indexing. |
| Compression is thermodynamically mandatory | *Algorithm* §9.4 | Bounded reasoning budget (T3) | T3 inherits the bound. |
| Grounding is a history of certified transitions; a prediction is not a fact | *Algorithm* §10.2; *UIM* §2.3, §17 | Write-back (C2) | ULSC does not say what may be written back. The archive supplies a candidate rule: only externally certified corrections, otherwise recursion degenerates into self-confirmation. Not adopted. Open problem. *Status:* UNDECIDED. |
| Geometric theory of latent representations; experimental track E1–E5 | *Framework* §5.6, §8.2 | Effective-dimension and Fisher-spectrum measurements (§10) | May share models and tooling. Compatibility of the two geometric descriptions is not examined. *Status:* UNDECIDED. |
| Ternary standard FOLLOW / OMIT / NULL / UNDECIDED | *Algorithm* §15; *Framework* §5.4, §7 | Statuses in §13 | Used as is. |

---

## 10. Experimental Program

### Statement

The program measures geometry. It does not measure experience. All predictions below are untested at the date of this document.

### Method

1. Take an open trained model and a set of inputs. Record activations of chosen layers.
2. Compute $d(\varepsilon)$ with several independent estimators (participation ratio, correlation dimension, TwoNN, Fisher or Jacobian spectrum).
3. Look for plateaus and steps (extra directions folded away at coarse scales), a power law (scaling), or a flat dependence.

**Controls** (without them a result cannot be read):
- an untrained model of the same architecture;
- shuffled data or noise input;
- Gaussian data with the same covariance;
- several sample sizes (dimension estimates are biased at small $N$);
- several estimators. If they disagree, no conclusion yet.

### Predictions

| ID | Prediction | Refuted if |
| -- | ---------- | ---------- |
| P1 | Similarity between LLM representations and human brain responses (RSA on neural data) is higher for abstract concepts and lower for bodily and interoceptive ones. | No difference, or the reverse, after controlling for word frequency and concreteness. |
| P2 | In multimodal and embodied models the P and S subspaces are more strongly linked (CKA, linear predictability) than in separately trained models. | The link is the same. Note: convergence of representations across models and modalities would also give this result. The distinguishing version is P3. |
| P3 | An RL agent in simulation with a viability variable (stake) has deeper pits in the linked regions than the same agent without it: more effort to leave, longer time to return, stiffer spectrum. | No difference. |
| P4 | The profile $d(\varepsilon)$ differs between an LLM, a world model, and an embodied model. A flat profile everywhere means axis A is uninformative. | The profiles cannot be told apart. |
| P5 | Across training checkpoints of one model (for example, a public checkpoint family) coarse-scale structure forms before fine-scale structure. | The order is reversed or random. The link to ULSC is indirect (axis C). |

### Priority

P4 and P5 are the cheapest: open models and public checkpoints. P1 needs existing neuroimaging data. P2 and P3 need training runs or simulation and cost more.

### What is not tested

Experience. All measurements show differences in geometry. They do not show where something is "experienced from inside".

---

## 11. The Boundary: The Hard Problem and the Observer

### Statement

ULSC does not explain why a Q-event is experienced. It turns the question into a geometric and computational one: which regions of a stitched space are phenomenal, and what separates them. It gives no mechanism that turns structure into subjectivity. At this point the framework stops on purpose. There are no data or formalisms for the next step, and any attempt to close the gap needs separate strong assumptions.

### The observer

The problem has a similar shape to the observer problem in physics: a description of a system that includes the describer. A system with a self-model and write-back reads its own relief and then changes it. The reader and the read are the same object.

What is claimed: the form of the problem is similar. A description from outside and a description from inside have to be closed onto each other.

What is observed: write-back changes the relief that was just read. This is ordinary physical self-modification of the carrier. It is not a quantum effect.

What is not claimed: any isomorphism with measurement in quantum mechanics, or any contribution to the measurement problem. The parallel is kept for orientation only. No thesis depends on it.

### Not adopted

A universal informational latent of which individual latents are fragments is a possible extension. ULSC does not assume it. It is a strong assumption, and the archive keeps the related questions open (*Algorithm*, §12, §13). ULSC takes no position on them.

---

## 12. Objections and Limits

### 12.1 D4 is too broad

Every trained system has Q-structures. D4 gives a structural vocabulary, not a criterion for experience. The criterion is pushed onto C1–C3 and onto the hard problem. A critic may fairly say D4 does little work.

### 12.2 The single latent may not exist

A2 is an assumption. The brain may have several coupled spaces that only look like one at the behavioral level. If so, "stitching" has to be redefined as coupling, and part of T1 weakens.

### 12.3 Two meanings of "pit"

An attractor in activation dynamics and a stiff direction in weight space are different objects. A5 links them by assumption. If they do not correlate, the Fisher spectrum is not a valid proxy for depth, and axis B has to be measured only by perturbation.

### 12.4 Comparing a human and a model

Coordinates differ and human data are indirect. RSA and CKA compare relational geometry, but they see only what recordings allow. Axis A for humans stays a prediction.

### 12.5 Competing explanations

Two rivals. First, biological naturalism: the claims about stake and body would then say something stronger than A1 allows. Second, convergence of representations across models and modalities: it predicts the P2 result without any stake. Only P3, where stake is manipulated, separates ULSC from it.

### 12.6 Falsifiability

Three results would damage the framework: (i) P3 shows no change in depth when stake is added; (ii) P1 comes out reversed; (iii) P4 finds profiles that cannot be told apart. None of them would answer the hard problem. They would remove the geometric claims.

### 12.7 Engineering vocabulary

"Relief", "budget", and "traversal" come from machine learning. Projecting engineering terms onto minds is a known failure mode, as the archive says (*Algorithm*, §14.4). The defense is the same: the claims that survive translation back into measurable quantities are the ones that count.

---

## 13. Self-Assessment Under the Ternary Standard

The archive's standard applies: FOLLOW (certified), OMIT (admissible but inessential), NULL (inadmissible), UNDECIDED (not enough certification).

Rule used for derived claims. A claim gets FOLLOW only if it follows from the definitions alone or describes an existing architecture. If it depends on an assumption, it gets UNDECIDED, with the dependency named. NULL marks claims rejected here. OMIT marks material kept for orientation.

| Claim of this document | Verdict | Basis |
| ---------------------- | ------- | ----- |
| Definitions D1–D10 are consistent, and D4 does not contain the felt aspect | FOLLOW (formal structure) | Stipulations; consistency checked in §3–§5 |
| Relief and reasoning budget are distinct quantities | FOLLOW | D3 versus D6; independent combinations (§4) |
| The reasoning budget is bounded for any physical system | FOLLOW | Constraint triad (*Algorithm* §3.2, §9.4) |
| A deployed LLM does not change weights in operation; context changes activations only | FOLLOW | Description of current deployment |
| A deployed LLM has no P-layer or stake in the direct sense | FOLLOW | Architecture; physics enters through text only |
| Qualia split into S and P classes | FOLLOW (formal structure) | D2, D4 |
| Humans have one stitched latent | UNDECIDED | A2; tested by P2 |
| Physical attractors are deep because of stake | UNDECIDED | A4; tested by P3 |
| Maintaining P costs more than S; deep abstraction usually reduces the P share | UNDECIDED | Plausible, unmeasured |
| Abstract thought always requires suppressing P | NULL | Counterexamples: spatial and bodily mathematical thinking |
| Human and LLM S-Q-structures overlap in relational geometry | UNDECIDED | P1 |
| Overlap of geometry implies identity of experience | NULL | Does not follow (§11) |
| Profiles $d(\varepsilon)$ differ between LLM, world model, and embodied model | UNDECIDED | P4 |
| Adding artificial stake deepens attractors | UNDECIDED | P3 |
| C1 and C2 together are sufficient for consciousness-like organization | UNDECIDED | Working position; no proof |
| C3 is needed for the depth of bodily qualia | UNDECIDED | A4 |
| C2 alone is sufficient | NULL | Would count every online-learning system without a self-model |
| C2 is necessary for momentary experience | NULL | Anterograde amnesia |
| Presence of Q-structures is sufficient for experience | NULL | Every trained system has them |
| What may be written back under C2 | UNDECIDED | Archive's candidate rule (certified corrections only) not adopted |
| Stitching can be formalized as one manifold with shared coordinates | UNDECIDED | Formalization open |
| Why a Q-event is experienced | UNDECIDED (out of scope) | Hard problem |
| The parallel with the observer problem in physics | OMIT (admitted) | Kept for orientation; no thesis depends on it |
| Isomorphism with quantum measurement | NULL | No derivation; not claimed |

---

## 14. What This Document Does Not Claim

1. **It does not explain why a Q-event is experienced.** It names the gap and stops.
2. **It does not say that LLMs are or are not conscious.** It lists which candidate conditions are present or absent.
3. **It does not claim that a biological body is required.** Stake can in principle be implemented in an artificial system. P3 tests one version.
4. **It does not claim that a single manifold exists.** That is A2.
5. **It does not claim that the measurements separate conscious from non-conscious systems.** They show geometry.
6. **It does not claim measured values.** The entries in the comparison table are structural statements or predictions.
7. **It does not claim novelty.** Several components resemble existing work on homeostatic accounts of feeling, self-model theories, and embodied cognition. A systematic comparison has not been done.
8. **It does not claim completeness.** The statuses in §13 can move in both directions after the experiments in §10.

---

## 15. Conclusion

Learning fixes a relief in the latent space. Thinking spends a limited budget to move through it. In a human the physical and semantic layers sit in one space, and the physical part is deep because the body can be lost. In an LLM the space is almost entirely semantic, frozen in operation, with no stake. A world model has the physical layer without the semantic one and without stake.

$$\text{Stitched latent} \rightarrow \text{Learned relief} \rightarrow \text{Bounded traversal} \rightarrow \text{Self-model} \rightarrow \text{Write-back}$$

Stake modifies the depth of the relief along this chain. The step from the chain to experience is not made here. What can be done is to measure the geometry and see whether the predictions hold.

---

## Appendix: Core Formulae as Schemata

Most expressions are schemata: compressed relations that make the argument easier to follow. Some are formal definitions. Some are measurement proxies.

| Expression | Status | Reading |
| ---------- | ------ | ------- |
| $Z \supseteq P \cup S$, with continuous transitions | Schema | Stitched latent |
| $R = R(\theta)$ | Schema | Relief determined by weights |
| $D(U) = \inf\{\lVert\delta\rVert : z+\delta \text{ does not return to } U\}$ | Formal structure | Depth of a region |
| $F(\theta) = \mathbb{E}[\nabla \log p \, \nabla \log p^{\top}]$, spectrum of $F$ | Measurement proxy | Stiff directions as a proxy for depth (A5) |
| $d(r) = d\log C(r) / d\log r$ | Measurement proxy | Effective dimension at scale $r$ |
| $c_P + c_S \le \rho_{\max}$ | Schema | The cost of traversal per unit time is bounded by the envelope |
| $\Pi = \lVert\Delta R\rVert / \text{unit of experience}$ | Schema | Plasticity |
| $M(z) \subset Z$, with $M \subset z$ | Schema | Self-model inside the space it models |
