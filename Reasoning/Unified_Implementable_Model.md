# Unified Implementable Model, Version 2.0

**Verifier-Centered Latent World Models with Evidence-Grounded Three-Way Semantics**

Vladimir Yakunin

July 8, 2026

---

## Abstract

We present a revised unified architecture for embodied agents operating in partially observed, safety-relevant environments such as mobile robotics and autonomous aerial systems. The architecture combines an object-centric latent world model, a geometric predicate layer, bounded semantic hypothesis generation, measurable verification contracts, exact post-action verification, event-sourced memory, and recursive recovery across failed attempts. Its central design principle is an explicit authority boundary: imagined trajectories may rank actions and suppress bad routes, but only an accepted action followed by a trusted observation may create factual transition evidence. A semantic proposer, including an optional language model, is therefore not an action authority, a metric authority, or a factual memory writer.

The mathematical treatment corrects two common errors in box-based semantics. First, the differentiable containment penalty is oriented so that it vanishes exactly when the antecedent box is contained in the consequent box. Second, box incompatibility is represented by separation in at least one coordinate, rather than by the substantially stronger and generally incorrect requirement of zero overlap in every coordinate. We further distinguish structural ontology constraints from grounded state evaluation: predicate boxes are persistent semantic regions, while a predicted or observed entity embedding is tested for membership in those regions.

The resulting model uses three specification relations—required entailment, required incompatibility, and irrelevance—together with a separate epistemic outcome, unresolved. Planning is performed by surface-conditioned, risk-sensitive model predictive control over mixed discrete and continuous actions. Candidate rollouts remain predictive-only; before execution, a deterministic binder constructs a measurable contract and a verifier checks legality, surface compatibility, semantic constraints, and uncertainty. After execution, the official before–action–after tuple is ingested exactly once, producing a four-way verdict: required, forbidden, irrelevant, or unresolved. Canonical claims, assumption lineage, and memory events prevent speculative explanations from being promoted into confirmed mechanics. The same core architecture supports different domains by replacing the perception adapter, action surface, constraint modules, research modules, and recovery policy while preserving the authority, verification, and memory invariants.

---

## Contents

1. [Scope and Architectural Position](#1-scope-and-architectural-position)
   - 1.1 [Non-claims](#11-non-claims)
2. [Formal Environment and Evidence Model](#2-formal-environment-and-evidence-model)
   - 2.1 [Partially observed controlled process](#21-partially-observed-controlled-process)
   - 2.2 [Trusted observation is not metaphysical truth](#22-trusted-observation-is-not-metaphysical-truth)
   - 2.3 [Authority hierarchy](#23-authority-hierarchy)
3. [Three-Way Semantic Specification and Four-Way Judgment](#3-three-way-semantic-specification-and-four-way-judgment)
4. [Corrected Predicate-Box Semantics](#4-corrected-predicate-box-semantics)
   - 4.1 [Entity and relation grounding](#41-entity-and-relation-grounding)
   - 4.2 [Signed membership and epistemic band](#42-signed-membership-and-epistemic-band)
   - 4.3 [Exact entailment and corrected containment loss](#43-exact-entailment-and-corrected-containment-loss)
   - 4.4 [Exact incompatibility and corrected separation loss](#44-exact-incompatibility-and-corrected-separation-loss)
   - 4.5 [Structural relations versus state constraints](#45-structural-relations-versus-state-constraints)
   - 4.6 [Ontology loss](#46-ontology-loss)
   - 4.7 [Expressivity boundary](#47-expressivity-boundary)
5. [Object-Centric Latent World Model](#5-object-centric-latent-world-model)
   - 5.1 [Belief state](#51-belief-state)
   - 5.2 [Probabilistic dynamics](#52-probabilistic-dynamics)
   - 5.3 [Predictive objective](#53-predictive-objective)
   - 5.4 [Anti-collapse regularization](#54-anti-collapse-regularization)
   - 5.5 [Grounding and calibration losses](#55-grounding-and-calibration-losses)
6. [Canonical Evidence Ledger](#6-canonical-evidence-ledger)
7. [Proposer, Binder, Planner, and Verifier](#7-proposer-binder-planner-and-verifier)
   - 7.1 [Semantic proposer](#71-semantic-proposer)
   - 7.2 [Deterministic binder](#72-deterministic-binder)
   - 7.3 [Planner and compiler](#73-planner-and-compiler)
   - 7.4 [Pre-action and post-action verifier](#74-pre-action-and-post-action-verifier)
8. [Measurable Verification Contracts](#8-measurable-verification-contracts)
9. [Surface-Conditioned Action Realization](#9-surface-conditioned-action-realization)
10. [Risk-Sensitive Predictive Planning](#10-risk-sensitive-predictive-planning)
    - 10.1 [Predictive rollouts](#101-predictive-rollouts)
    - 10.2 [Chance and hard constraints](#102-chance-and-hard-constraints)
    - 10.3 [Mixed discrete–continuous CEM](#103-mixed-discretecontinuous-cem)
11. [Two-Phase Execution and the Factual Commit Boundary](#11-two-phase-execution-and-the-factual-commit-boundary)
    - 11.1 [Pre-action phase](#111-pre-action-phase)
    - 11.2 [Pending transition invariant](#112-pending-transition-invariant)
    - 11.3 [Post-action phase](#113-post-action-phase)
12. [Recursive Hypothesis Revision](#12-recursive-hypothesis-revision)
13. [Canonical Event-Sourced Memory](#13-canonical-event-sourced-memory)
    - 13.1 [Deterministic consolidation](#131-deterministic-consolidation)
14. [Attempts, Recovery, and Termination](#14-attempts-recovery-and-termination)
15. [Learning Objective](#15-learning-objective)
    - 15.1 [Observed versus imagined training data](#151-observed-versus-imagined-training-data)
16. [Knowledge Distillation with Alignment and Authority Control](#16-knowledge-distillation-with-alignment-and-authority-control)
    - 16.1 [Representation alignment](#161-representation-alignment)
    - 16.2 [Dynamic distribution distillation](#162-dynamic-distribution-distillation)
    - 16.3 [Semantic distillation](#163-semantic-distillation)
    - 16.4 [Logit distillation](#164-logit-distillation)
    - 16.5 [Teacher authority boundary](#165-teacher-authority-boundary)
17. [Correctness Results and Precise Guarantees](#17-correctness-results-and-precise-guarantees)
18. [Worked Drone Example](#18-worked-drone-example)
    - 18.1 [Predicates and relations](#181-predicates-and-relations)
    - 18.2 [Current action surface](#182-current-action-surface)
    - 18.3 [Bound contract](#183-bound-contract)
    - 18.4 [Recovery](#184-recovery)
19. [Implementation Invariants and Test Obligations](#19-implementation-invariants-and-test-obligations)
20. [Research Modules and Domain Substitution](#20-research-modules-and-domain-substitution)
21. [Development Roadmap](#21-development-roadmap)
    - 21.1 [Stage 1: Static verified baseline](#211-stage-1-static-verified-baseline)
    - 21.2 [Stage 2: Calibrated uncertainty and active research](#212-stage-2-calibrated-uncertainty-and-active-research)
    - 21.3 [Stage 3: Canonical evidence and recursive revision](#213-stage-3-canonical-evidence-and-recursive-revision)
    - 21.4 [Stage 4: Event-sourced memory and attempt recursion](#214-stage-4-event-sourced-memory-and-attempt-recursion)
    - 21.5 [Stage 5: Controlled predicate and relation induction](#215-stage-5-controlled-predicate-and-relation-induction)
    - 21.6 [Stage 6: Richer semantic geometries](#216-stage-6-richer-semantic-geometries)
    - 21.7 [Stage 7: Hierarchical skills and long-horizon planning](#217-stage-7-hierarchical-skills-and-long-horizon-planning)
22. [Conclusion](#22-conclusion)
23. [References](#references)

---

## 1 Scope and Architectural Position

The Unified Implementable Model (UIM) is intended for agents that must jointly:

1. infer a compact state from high-dimensional and noisy observations;
2. predict the consequences of candidate actions;
3. reason over semantic objects, relations, and constraints;
4. select actions under uncertainty and changing control modes;
5. distinguish predicted consequences from observed consequences;
6. revise hypotheses without erasing still-valid assumptions;
7. retain only evidence-grounded knowledge across levels, attempts, or mission phases.

The architecture is domain-general, but not domain-free. A robotics deployment and an abstract reasoning deployment use different perception front ends, action spaces, verification metrics, and research probes. They nevertheless share one control architecture:

```
observe → canonicalize evidence → propose → bind → plan
  → verify before action → act → verify after observation → consolidate
```

The model is **verifier-centered**. A neural world model predicts; a semantic proposer generates testable explanations; a binder makes them measurable; a planner realizes them as routes; and an exact verifier determines what the trusted transition actually supports.

### 1.1 Non-claims

The following claims are explicitly excluded.

1. Exact satisfaction of a learned latent constraint is not, by itself, a proof of physical-world safety.
2. A language model explanation is not factual evidence.
3. An imagined rollout is not an observed transition.
4. A failed route does not imply that every assumption of its parent hypothesis is false.
5. A successful route does not automatically confirm the proposer’s explanation of why it succeeded.
6. A geometric box ontology is not universally expressive; disjunctions, rotated regions, multimodal concepts, and temporal properties may require richer representations.

---

## 2 Formal Environment and Evidence Model

### 2.1 Partially observed controlled process

Let the physical environment be a controlled stochastic process

$$
\mathcal{M} = (\mathcal{X}, \mathcal{O}, \mathcal{A}, \mathcal{T}, \mathcal{Z}, \mathcal{C}),
$$

where \(x_t \in \mathcal{X}\) is the inaccessible physical state, \(o_t \in \mathcal{O}\) is an observation, \(a_t \in \mathcal{A}\) is an action, \(\mathcal{T}(x_{t+1} \mid x_t, a_t)\) is the transition law, \(\mathcal{Z}(o_t \mid x_t)\) is the observation law, and \(\mathcal{C}\) is the collection of task and safety constraints.

At time \(t\), not every action in \(\mathcal{A}\) is necessarily available. The current action surface is

$$
\Sigma_t = (\mathcal{A}_t, \kappa_t), \qquad \mathcal{A}_t \subseteq \mathcal{A},
$$

where \(\kappa_t\) contains mode, capability, payload, actuator, communication, and authorization metadata. For a drone, \(\Sigma_t\) may distinguish manual-rate control, position hold, landing, return-to-home, degraded navigation, or payload operation. For a symbolic environment, it may distinguish different interaction modes or newly available action symbols.

### 2.2 Trusted observation is not metaphysical truth

The agent cannot directly record \(x_t\). It records a trusted, timestamped observation packet

$$
\bar{o}_t = (o_t, \Sigma_t, m_t),
$$

where \(m_t\) contains source, timestamp, calibration, synchronization, and estimator metadata. The pair

$$
\epsilon_t = (\bar{o}_t, a_t, \bar{o}_{t+1})
$$

is the highest-authority transition evidence available to the agent, provided that the environment or control stack accepted \(a_t\) and the returned observation passed ingestion checks. It is called an *authoritative observed transition*; it is not claimed to be the hidden physical state itself.

**Definition 2.1** (Evidence scope). Each result has one of the scopes

$$
\texttt{NOT\_AVAILABLE},\quad \texttt{PREDICTIVE\_ONLY},\quad \texttt{OBSERVED\_TRANSITION},\quad \texttt{REPLAY\_VERIFIED}.
$$

A predictive result may affect ranking and risk estimation, but it may not create a factual transition, a confirmed mechanic, or positive success memory.

### 2.3 Authority hierarchy

A generic authority order is

```
accepted action and trusted post-action observation
  > current action-surface legality and capability
  > post-action verifier result and bound metric result
  > canonical observed memory and deterministic consolidation
  > committed causal models and current deterministic scene facts
  > bound semantic hypothesis and route realization
  > predictive rollout
  > unbound semantic proposal or explanation.
```

No lower layer may promote its output into a higher evidentiary class without the corresponding higher-authority observation or verification event.

---

## 3 Three-Way Semantic Specification and Four-Way Judgment

The UIM uses a three-way relation vocabulary inspired by the distinction between consequence, incompatibility, and omission of a relation. Let \(\mathcal{P}\) be a predicate vocabulary. For a pair \((p, q) \in \mathcal{P}^2\), the structural specification label is

$$
R(p, q) \in \{\texttt{REQ}, \texttt{FORB}, \texttt{IRR}\}.
$$

The labels mean:

1. \(R(p, q) = \texttt{REQ}\): the ontology requires \(p \Rightarrow q\);
2. \(R(p, q) = \texttt{FORB}\): the ontology requires \(p \land q\) to be impossible for the same grounded argument;
3. \(R(p, q) = \texttt{IRR}\): no entailment or incompatibility constraint is asserted between \(p\) and \(q\).

Irrelevance is not falsehood. It means that the theory intentionally imposes no relation of the specified kind. Data may still reveal correlation, partial overlap, causal dependence, or a future need to refine the ontology.

At runtime, the verifier emits a separate epistemic-semantic judgment

$$
J \in \{\texttt{REQUIRED}, \texttt{FORBIDDEN}, \texttt{IRRELEVANT}, \texttt{UNRESOLVED}\}.
$$

Here \(\texttt{UNRESOLVED}\) is not a fourth structural relation. It records insufficient, predictive-only, stale, unstable, or contradictory evidence. This separation prevents unknown from being treated as false and prevents a legal no-progress action from being treated as a contradiction.

---

## 4 Corrected Predicate-Box Semantics

### 4.1 Entity and relation grounding

A predicate box is a region in a semantic feature space, not a state-dependent box generated anew for every rollout. Let \(e_{t,i}\) be an object or entity representation extracted from the current scene graph \(G_t\). A grounding map produces

$$
\xi_{t,i} = \psi_\eta(e_{t,i}, G_t) \in \mathbb{R}^m.
$$

For a binary relation \(r(i, j)\), a relation grounding map may use

$$
\xi^{(2)}_{t,ij} = \psi^{(2)}_\eta(e_{t,i}, e_{t,j}, G_t) \in \mathbb{R}^{m_2}.
$$

Unary and relational predicates may use separate semantic spaces.

Each unary predicate \(p \in \mathcal{P}\) is represented by a closed axis-aligned box

$$
B_p = [\ell_p, u_p] = \{\xi \in \mathbb{R}^m : \ell_p \leq \xi \leq u_p\},
$$

with componentwise inequalities. A stable parameterization is

$$
\ell_p = c_p - r_p, \qquad u_p = c_p + r_p, \qquad r_p = r_{\min} + \mathrm{softplus}(\rho_p),
$$

where \(r_{\min} > 0\) prevents numerical collapse and \(u_p\) is the upper endpoint of \(B_p\).

### 4.2 Signed membership and epistemic band

For a grounded feature \(\xi\), define the signed box margin

$$
\mu_p(\xi) = \min_{1 \leq j \leq m} \min\{\xi_j - \ell_{p,j},\; u_{p,j} - \xi_j\}.
$$

Then \(\mu_p(\xi) > 0\) means that \(\xi\) lies in the interior of \(B_p\), \(\mu_p(\xi) = 0\) means that it lies on the boundary, and \(\mu_p(\xi) < 0\) means that it lies outside.

Given an epistemic tolerance \(\gamma_p > 0\), the grounded truth status is

$$
\mathrm{truth}_p(\xi) =
\begin{cases}
\texttt{TRUE}, & \mu_p(\xi) \geq \gamma_p, \\
\texttt{FALSE}, & \mu_p(\xi) \leq -\gamma_p, \\
\texttt{UNRESOLVED}, & |\mu_p(\xi)| < \gamma_p.
\end{cases}
$$

The unresolved band absorbs representation error, sensor uncertainty, and small numerical perturbations. A differentiable membership score may be defined by

$$
\tilde{m}_p(\xi) = \sigma\left(\frac{\mu_p(\xi)}{\tau_p}\right),
$$

where \(\sigma\) is the logistic sigmoid and \(\tau_p > 0\) is a temperature.

### 4.3 Exact entailment and corrected containment loss

The intended structural semantics is

$$
p \Rightarrow q \quad\Longleftrightarrow\quad B_p \subseteq B_q.
$$

For closed axis-aligned boxes,

$$
B_p \subseteq B_q \quad\Longleftrightarrow\quad \ell_q \leq \ell_p \;\text{and}\; u_p \leq u_q
$$

componentwise. Using \(u_p\) for the upper endpoint of \(B_p\), the exact condition is

$$
\ell_{q,j} \leq \ell_{p,j}, \qquad u_{p,j} \leq u_{q,j} \qquad \forall j.
$$

For a desired clearance \(\varepsilon_\Rightarrow \geq 0\), the corrected hinge loss is

$$
\mathcal{L}^\varepsilon_\subseteq(p, q) = \sum_{j=1}^{m} \Bigl( [\ell_{q,j} + \varepsilon_\Rightarrow - \ell_{p,j}]_+ + [u_{p,j} - u_{q,j} + \varepsilon_\Rightarrow]_+ \Bigr).
$$

For \(\varepsilon_\Rightarrow = 0\), the loss vanishes exactly when \(B_p \subseteq B_q\). A positive margin requires \(B_p\) to lie inside \(B_q\) with coordinatewise clearance.

### 4.4 Exact incompatibility and corrected separation loss

For closed boxes,

$$
B_p \cap B_q = \emptyset \quad\Longleftrightarrow\quad \exists j:\; (u_{p,j} < \ell_{q,j}) \lor (u_{q,j} < \ell_{p,j}).
$$

Define the signed overlap depth in coordinate \(j\) by

$$
\delta_j(p, q) = \min(u_{p,j}, u_{q,j}) - \max(\ell_{p,j}, \ell_{q,j}).
$$

The boxes intersect if and only if \(\delta_j(p, q) \geq 0\) for every coordinate. They are separated by at least \(\varepsilon_\perp > 0\) in some coordinate if and only if

$$
\min_j \delta_j(p, q) \leq -\varepsilon_\perp.
$$

Therefore a correct margin loss is

$$
\mathcal{L}^\varepsilon_\perp(p, q) = \bigl[\varepsilon_\perp + \min_{1 \leq j \leq m} \delta_j(p, q)\bigr]_+.
$$

This loss is non-smooth but subdifferentiable almost everywhere. A smooth approximation may replace \(\min\) by the normalized soft minimum

$$
\mathrm{smin}_\tau(\delta) = -\tau \log\left(\frac{1}{m} \sum_{j=1}^{m} e^{-\delta_j / \tau}\right),
$$

with the understanding that the exact deployment check remains the empty-intersection condition above.

> **Remark 4.1** (Why a sum of coordinate overlaps is wrong). The quantity \(\sum_j [\delta_j]_+\) vanishes only when every coordinate has non-positive overlap. Empty intersection, however, requires separation in at least one coordinate. The summed-overlap objective therefore enforces a much stronger geometry and can incorrectly push boxes apart along dimensions that need not separate them.

### 4.5 Structural relations versus state constraints

The relations \(B_p \subseteq B_q\) and \(B_p \cap B_q = \emptyset\) are properties of the ontology. They do not need to be re-evaluated as if the boxes themselves changed at every predicted step. Runtime state checking instead evaluates whether grounded entities or relations satisfy atomic predicates and task formulas.

For example, if \(B_{\mathrm{square}} \subseteq B_{\mathrm{rectangle}}\) and an entity embedding \(\xi_{t,i}\) is robustly inside \(B_{\mathrm{square}}\), then it is also inside \(B_{\mathrm{rectangle}}\). A planner checks \(\xi_{t,i} \in B_p\) for the predicted state and separately verifies that the ontology remains structurally valid.

### 4.6 Ontology loss

Let \(\Theta^\Rightarrow\) be the required entailments and \(\Theta^\perp\) the required incompatibilities. The structural ontology loss is

$$
\mathcal{L}_{\mathrm{ont}} = \sum_{(p,q) \in \Theta^\Rightarrow} \lambda^\Rightarrow_{pq}\, \mathcal{L}^\varepsilon_\subseteq(p, q) + \sum_{(p,q) \in \Theta^\perp} \lambda^\perp_{pq}\, \mathcal{L}^\varepsilon_\perp(p, q).
$$

Relations marked irrelevant contribute no structural penalty. This does not prevent a separate statistical model from learning correlations between them.

### 4.7 Expressivity boundary

Axis-aligned boxes represent conjunction-like, convex, coordinate-factorized concepts. The following extensions are permitted when needed:

1. a finite union of boxes for multimodal predicates;
2. oriented boxes or ellipsoids for rotated geometry;
3. neural energy regions for highly non-convex concepts;
4. temporal automata for predicates over trajectories;
5. relation-specific spaces for pairwise or higher-arity predicates.

The authority and verification architecture does not depend on the box family; only the grounding and exact-check modules change.

---

## 5 Object-Centric Latent World Model

### 5.1 Belief state

The agent maintains a recurrent belief state

$$
h_t = F_\theta\bigl(h_{t-1},\; E_\theta(o_t),\; a_{t-1},\; \Sigma_t\bigr), \qquad q_\theta(s_t \mid h_t),
$$

where \(s_t\) is a stochastic latent state. An object-centric decoder or slot extractor yields

$$
G_t = (V_t, E_t), \qquad V_t = \{e_{t,1}, \ldots, e_{t,n_t}\},
$$

with object attributes, identities or descriptors, and typed relations. Object identifiers are state-local unless a re-identification module supplies evidence for persistence.

### 5.2 Probabilistic dynamics

The world model predicts

$$
p_\phi(s_{t+1}, G_{t+1}, \Sigma_{t+1} \mid s_t, G_t, \Sigma_t, a_t).
$$

Predicting \(\Sigma_{t+1}\) is important because an action may change the available action set, control mode, payload state, or authorization surface.

A practical ensemble \(\{p_{\phi_r}\}_{r=1}^{M}\) provides epistemic disagreement. For a scalar predicted quantity \(y\), one may use

$$
U_{\mathrm{epi}}(y) = \frac{1}{M} \sum_{r=1}^{M} \left(\hat{y}_r - \frac{1}{M} \sum_{k=1}^{M} \hat{y}_k\right)^2.
$$

Aleatoric uncertainty is represented by each member’s conditional distribution.

### 5.3 Predictive objective

With a target encoder \(\tilde{E}_{\bar{\theta}}\), a stable one-step latent objective is

$$
\mathcal{L}_{\mathrm{pred}} = \mathbb{E}\Bigl[\bigl\|\hat{z}_{t+1} - \mathrm{sg}\bigl(\tilde{E}_{\bar{\theta}}(o_{t+1})\bigr)\bigr\|_2^2\Bigr],
$$

where \(\hat{z}_{t+1} = P_\phi(h_t, a_t, \Sigma_t)\). The target encoder may be an exponential moving average of the online encoder or another stable target construction. A probabilistic alternative is the negative log-likelihood

$$
\mathcal{L}_{\mathrm{dyn}} = -\mathbb{E}\log p_\phi(s_{t+1} \mid s_t, a_t, \Sigma_t).
$$

For long-horizon consistency, one may add multi-step losses with scheduled sampling while retaining explicit uncertainty growth.

### 5.4 Anti-collapse regularization

A concrete variance–covariance regularizer for a batch \(Z \in \mathbb{R}^{B \times d}\) is

$$
\mathcal{L}_{\mathrm{var}} = \frac{1}{d} \sum_{j=1}^{d} \bigl[\gamma - \sqrt{\mathrm{Var}(Z_{:,j}) + \epsilon}\bigr]_+,
$$

$$
\mathcal{L}_{\mathrm{cov}} = \frac{1}{d(d-1)} \sum_{i \neq j} \mathrm{Cov}(Z)_{ij}^2.
$$

A constant representation incurs a strictly positive variance penalty when \(\gamma > 0\). This fact alone does not prove that every collapsed parameterization is absent as a local stationary point under every optimizer and weighting; such a global anti-collapse theorem would require stronger assumptions than are generally available.

A projection-based Gaussian discrepancy such as SIGReg may replace the covariance term, provided its finite-sample statistic, normalization, and gradients are specified explicitly and tested rather than invoked as an informal guarantee.

### 5.5 Grounding and calibration losses

When predicate labels or weak supervision are available, the grounding loss may be

$$
\mathcal{L}_{\mathrm{ground}} = -\mathbb{E}_{(\xi,p,y)}\Bigl[y\log\tilde{m}_p(\xi) + (1-y)\log\bigl(1 - \tilde{m}_p(\xi)\bigr)\Bigr].
$$

Calibration of transition and predicate uncertainty is enforced by a proper scoring rule, for example negative log-likelihood or the Brier score. The calibration set must be disjoint from the training set used to fit the same confidence thresholds.

---

## 6 Canonical Evidence Ledger

The semantic proposer receives one canonical evidence interface rather than several independently summarized truth copies. A claim is a tuple

$$
C = (\mathrm{id},\; k,\; \tau,\; s,\; r,\; v,\; \alpha,\; c,\; \sigma,\; \mathcal{E},\; \mathcal{S}),
$$

where \(k\) is a semantic key, \(\tau\) is claim type, \(s\) is subject scope, \(r\) is predicate or relation, \(v\) is value, \(\alpha\) is authority rank, \(c\) is confidence, \(\sigma\) is status, \(\mathcal{E}\) is the set of evidence references, and \(\mathcal{S}\) is the set of superseded claims.

Claims are deduplicated by semantic key. If two claims conflict, the higher-authority claim supersedes the lower-authority representation while preserving lineage. Derived summaries may exist for efficiency, but they are marked non-authoritative and refer back to canonical claim identifiers.

The ledger includes a canonical belief delta

$$
\Delta B_t = \bigl(\text{changed components},\; \text{confirmed assumptions},\; \text{contradicted assumptions},\; \text{unresolved assumptions},\; \text{new high-authority claims}\bigr).
$$

This delta lets a revision module respond to genuinely new evidence instead of regenerating unrelated hypotheses from scratch.

---

## 7 Proposer, Binder, Planner, and Verifier

### 7.1 Semantic proposer

A semantic proposer may be a language model, a program synthesizer, a graph search module, or a hybrid. It may propose:

1. a semantic hypothesis;
2. target object or relation descriptors;
3. a metric family and improvement direction;
4. required action surfaces;
5. explicit assumptions and registered questions;
6. parent–child revision lineage.

It may **not** authorize a primitive action, certify a metric baseline, write factual memory, or promote its explanation to confirmed knowledge.

### 7.2 Deterministic binder

The binder resolves proposal references against the current trusted scene and constructs a measurable verification contract. It owns:

1. target bindings and stable descriptors;
2. metric selection from an allowed registry;
3. baseline recomputation;
4. direction, tolerances, progress threshold, success threshold, and failure margin;
5. contract identity and hash.

Numeric values suggested by the proposer are treated as intent, not authority.

### 7.3 Planner and compiler

The planner converts a bound hypothesis into one or more surface-conditioned routes. The compiler maps each route step to executable actions, preserving the contract, required surface, target bindings, and predicted next surface. A planner may use continuous optimization, graph search, sampling, trajectory optimization, or a hybrid.

### 7.4 Pre-action and post-action verifier

The pre-action verifier checks current legality, capability, surface compatibility, contract validity, uncertainty, and hard safety constraints. The post-action verifier evaluates the trusted transition using the same bound metric and target semantics. The post-action result has higher authority than predictive evaluation.

---

## 8 Measurable Verification Contracts

A contract is

$$
\mathcal{K} = (\mathrm{id},\; \mathcal{D},\; \mu,\; b,\; d,\; \tau_{\mathrm{prog}},\; \tau_{\mathrm{succ}},\; \tau_{\mathrm{fail}},\; \varepsilon,\; h),
$$

where \(\mathcal{D}\) contains target descriptors and bindings, \(\mu\) is a registered metric, \(b\) is the baseline, \(d \in \{-1, +1\}\) is the favorable direction, the \(\tau\) values are progress, success, and failure thresholds, \(\varepsilon\) is tolerance, and \(h\) is a contract hash.

The binder computes

$$
b = \mu(G_t; \mathcal{D}_t)
$$

from the current trusted scene. After action execution, the targets are rebound using stable descriptors rather than transient indices, and the verifier computes

$$
b^- = \mu(G_t; \hat{\mathcal{D}}_t), \qquad b^+ = \mu(G_{t+1}; \hat{\mathcal{D}}_{t+1}).
$$

If \(|b^- - b| > \varepsilon\), the contract is stale and the outcome is unresolved.

Define observed improvement

$$
\Delta_{\mathcal{K}} = d\,(b^+ - b^-).
$$

A generic classification is

$$
J(\epsilon_t, \mathcal{K}) =
\begin{cases}
\texttt{REQUIRED}, & \text{terminal success or contract success}, \\
\texttt{REQUIRED}, & \Delta_{\mathcal{K}} \geq \tau_{\mathrm{prog}}, \\
\texttt{FORBIDDEN}, & \Delta_{\mathcal{K}} \leq -\tau_{\mathrm{fail}} \text{ or a hard constraint is violated}, \\
\texttt{IRRELEVANT}, & \text{legal, resolved, and } |\Delta_{\mathcal{K}}| < \tau_{\mathrm{prog}}, \\
\texttt{UNRESOLVED}, & \text{predictive-only, stale, unstable, or insufficient evidence}.
\end{cases}
$$

Domain-specific contracts may replace scalar \(\mu\) by a vector metric with a declared partial order, but the order must be fixed before observing the post-action result.

---

## 9 Surface-Conditioned Action Realization

Every route step carries

$$
R_h = (a_h,\; \Sigma^{\mathrm{req}}_h,\; \hat{\Sigma}^{\mathrm{exp}}_{h+1},\; \mathcal{K}_h,\; \chi_h),
$$

where \(\chi_h\) contains target bindings and semantic hypothesis lineage. The action may be emitted only if

$$
a_h \in \mathcal{A}_t \quad\text{and}\quad \Sigma_t \models \Sigma^{\mathrm{req}}_h.
$$

A mode-changing action is a first-class surface transition. The next route step is not emitted until the next trusted observation confirms the new surface.

If the observed surface differs from the expected surface, the route realization becomes unresolved or failed. This does not by itself falsify the semantic hypothesis. The architecture distinguishes

- mechanic error,
- target-binding error,
- metric error,
- surface-plan error,
- route error.

This distinction is essential in robotics, where a correct mission objective may be paired with an invalid control mode or temporarily unavailable actuator.

---

## 10 Risk-Sensitive Predictive Planning

### 10.1 Predictive rollouts

For a candidate action sequence

$$
\mathbf{a} = a_{t:t+H-1},
$$

the world model generates \(M\) stochastic rollouts

$$
\hat{\tau}^{(r)} = (s_t,\; \hat{s}^{(r)}_{t+1},\; \ldots,\; \hat{s}^{(r)}_{t+H},\; \hat{\Sigma}^{(r)}_{t+1:t+H}), \qquad r = 1, \ldots, M.
$$

Every such rollout has evidence scope \(\texttt{PREDICTIVE\_ONLY}\).

A risk-sensitive cost is

$$
\hat{J}(\mathbf{a}) = \frac{1}{M}\sum_{r=1}^{M} J_{\mathrm{task}}(\hat{\tau}^{(r)}) + \lambda_{\mathrm{cvar}}\,\mathrm{CVaR}_\alpha\bigl(J_{\mathrm{risk}}(\hat{\tau}^{(r)})\bigr) + \lambda_{\mathrm{epi}}\,U_{\mathrm{epi}}(\mathbf{a}) - \lambda_{\mathrm{info}}\,I(\mathbf{a}),
$$

where \(I(\mathbf{a})\) is expected information gain for a registered question. Information gain may justify a probe, but it does not convert the probe into positive task success.

**Algorithm 1** — Verifier-centered receding-horizon control

```
Require: Trusted observation ō_t, canonical ledger L_t, world model W, budgets B
Ensure:  One emitted action or a controlled stop/recovery decision

 1: Ingest ō_t and synchronize the current action surface Σ_t
 2: Build the current scene graph G_t and canonical belief delta
 3: Obtain bounded semantic hypotheses grounded in known claim identifiers
 4: for all eligible hypotheses H_i do
 5:     Bind targets and construct a measurable contract K_i
 6:     if K_i is invalid or vacuous then
 7:         reject H_i for the current cycle
 8:         continue
 9:     end if
10:     Compile surface-conditioned candidate routes
11:     Evaluate routes predictively under the risk-sensitive cost and chance constraints
12:     Mark all rollout results as PREDICTIVE_ONLY
13: end for
14: Select the best route passing legality, surface, uncertainty, and hard pre-action checks
15: if no goal-directed route is authorized then
16:     Select a registered epistemic probe, if one is verifier-authorized
17: end if
18: if no authorized action exists then
19:     return controlled stop or domain recovery action
20: end if
21: Register a pending transition token for the selected action a_t
22: Emit a_t and receive ō_{t+1}
23: Ingest (ō_t, a_t, ō_{t+1}) exactly once
24: Rebind K, recompute the metric, and emit a four-way verdict
25: Append canonical transition and verifier events; update assumptions and memory
26: Execute only the first action of the route; replan from ō_{t+1}
```

### 10.2 Chance and hard constraints

For each safety constraint \(g_k(s) \leq 0\), the planner may require

$$
\mathbb{P}\bigl(g_k(\hat{s}_{t+h}) \leq 0\bigr) \geq 1 - \alpha_k, \qquad h = 1, \ldots, H.
$$

Constraints with certified runtime monitors remain hard and are checked again immediately before action emission. A learned chance constraint is not a substitute for an independent low-level safety controller where one is available.

### 10.3 Mixed discrete–continuous CEM

For hybrid actions \(a_h = (a^d_h, a^c_h)\), use a factorized proposal

$$
q_\omega(\mathbf{a}) = \prod_{h=0}^{H-1} \mathrm{Cat}(a^d_h; \pi_h)\, \mathcal{N}(a^c_h; \mu_h, \Sigma_h),
$$

followed by projection of continuous controls onto actuator limits. This avoids the invalid assumption that all action sequences are Gaussian vectors.

If no feasible elites exist during CEM, the planner must not insert arbitrary random actions merely to keep the loop running. It either changes the search distribution, chooses a registered information-gathering probe, invokes an explicitly authorized recovery policy, or stops in a controlled manner.

---

## 11 Two-Phase Execution and the Factual Commit Boundary

### 11.1 Pre-action phase

Before action emission the agent may parse observations, update beliefs, invoke bounded semantic proposal, construct contracts, perform predictive rollouts, estimate uncertainty, reject routes, and select a candidate action. None of these operations creates an observed causal fact.

### 11.2 Pending transition invariant

Immediately before emitting an action, the agent registers a token

$$
\pi_t = (\mathrm{sequence},\; \mathrm{hash}(\bar{o}_t),\; a_t,\; \mathrm{hash}(\mathcal{K}_t)).
$$

A second action may not be emitted while \(\pi_t\) remains pending.

### 11.3 Post-action phase

After the control stack accepts \(a_t\) and returns \(\bar{o}_{t+1}\), the system must immediately ingest the authoritative transition tuple. The commit operation is idempotent with respect to \(\pi_t\). It:

1. compares trusted before and after observations and action surfaces;
2. rebuilds grounded scene representations;
3. rebinds contract targets;
4. recomputes the official before and after metric;
5. produces the post-action verdict;
6. writes exactly one committed transition edge;
7. updates observed action-effect and movement models;
8. appends canonical memory events;
9. clears the pending token.

The control loop may not terminate normally with a pending accepted transition.

---

## 12 Recursive Hypothesis Revision

A hypothesis is

$$
H = (\mathrm{id},\; \mathcal{P}_H,\; g,\; \rho,\; \mathcal{C}^+,\; \mathcal{C}^-,\; \mathcal{A}_H,\; \mathcal{T}_H,\; \mathcal{S}_H),
$$

where \(\mathcal{P}_H\) is the parent set, \(g\) is lineage generation, \(\rho\) is revision type, \(\mathcal{C}^+\) and \(\mathcal{C}^-\) are supporting and challenged claim identifiers, \(\mathcal{A}_H\) is an assumption graph, \(\mathcal{T}_H\) is target and metric intent, and \(\mathcal{S}_H\) is the surface and route intent.

Assumptions have statuses

$$
\texttt{PROPOSED},\quad \texttt{CONFIRMED},\quad \texttt{CONTRADICTED},\quad \texttt{UNRESOLVED}.
$$

A route failure updates only assumptions actually contradicted by observed evidence or explicitly rejected by a grounded child revision. Other assumptions remain confirmed or unresolved.

Permitted revision operators include:

1. preserve the mechanic and change the route;
2. replace the target binding;
3. replace the metric;
4. change the surface plan;
5. refine assumptions;
6. split a hypothesis into alternatives;
7. abandon the hypothesis family.

A child must cite an eligible parent, use a new identifier, preserve or reject known parent assumptions explicitly, and make the change declared by its revision type. Parents remain in memory as superseded rather than being deleted.

---

## 13 Canonical Event-Sourced Memory

The memory system is a bounded append-only stream of canonical events. A generic event is

$$
M_e = (\mathrm{id},\; h,\; \tau,\; \mathrm{scope},\; \mathrm{authority},\; J,\; \mathcal{P}_e,\; \mathcal{R}_e,\; \chi),
$$

where \(h\) is a deterministic hash, \(\tau\) is event type, \(J\) is semantic judgment, \(\mathcal{P}_e\) contains parent events, \(\mathcal{R}_e\) contains source records, and \(\chi\) is typed payload.

Useful event types include:

- `OBSERVED_TRANSITION`
- `VERIFIER_OUTCOME`
- `BELIEF_UPDATE`
- `BACKREACTION`
- `SEGMENT_COMPLETION`
- `ATTEMPT_RESET`
- `ATTEMPT_TERMINATED`

Memory layers are separated into raw evidence, belief state, transferable mechanics, proposed explanations, and summaries. A proposed explanation remains proposed even when its associated route succeeds, unless independent observed evidence establishes the claimed mechanism.

### 13.1 Deterministic consolidation

At a confirmed mission-segment or level boundary, consolidation produces

$$
M_{\mathrm{cons}} = (\mathcal{F}^+,\; \mathcal{F}^-,\; \mathcal{U},\; \mathcal{T},\; \mathcal{E}_{\mathrm{src}},\; \sigma_{\mathrm{det}},\; \sigma_{\mathrm{prop}}),
$$

where \(\mathcal{F}^+\) are confirmed facts, \(\mathcal{F}^-\) contradicted facts, \(\mathcal{U}\) unresolved proposals, \(\mathcal{T}\) transferable mechanics, \(\mathcal{E}_{\mathrm{src}}\) source event identifiers, \(\sigma_{\mathrm{det}}\) a deterministic summary, and \(\sigma_{\mathrm{prop}}\) an optional proposer-authored explanation. Only the first six fields may contribute confirmed transfer without further evidence.

Negative transfer is scope-sensitive. A failure tied to a transient object identifier, local map patch, battery state, or route binding must not become a universal mission rule.

---

## 14 Attempts, Recovery, and Termination

An attempt begins from an initial or recovered state and ends at one of:

1. confirmed task or segment success;
2. environment-originated failure followed by an accepted recovery transition;
3. wall-clock, energy, action-count, or communication budget exhaustion;
4. non-recoverable orchestration or hardware failure.

Environment failure and orchestration termination are different causal classes. A timeout must not be converted into an environment reset. For a drone, recovery may mean hover, re-localize, return-to-home, divert, or land. It is allowed only if the recovery action is currently available, authorized, and consistent with remaining hard budgets.

Across an accepted recovery boundary, preserve game- or mission-scoped observed knowledge:

1. canonical evidence and consolidations;
2. observed transition and action-effect models;
3. failed and irrelevant route signatures;
4. verifier backreaction and hypothesis lineage;
5. cumulative proposal and action budgets.

Clear or renew state-local execution state:

1. active route and transient bindings;
2. pending verification and pending transition token;
3. local candidate blacklist and oscillation counters;
4. state-specific research queues;
5. per-attempt proposal slots.

A recovery does not restart a higher-level mission deadline unless the mission specification explicitly defines a new segment.

---

## 15 Learning Objective

A mature training objective separates representation, dynamics, grounding, ontology, calibration, and distillation:

$$
\begin{aligned}
\mathcal{L}_{\mathrm{total}} &= \lambda_{\mathrm{pred}}\mathcal{L}_{\mathrm{pred}} + \lambda_{\mathrm{dyn}}\mathcal{L}_{\mathrm{dyn}} + \lambda_{\mathrm{var}}\mathcal{L}_{\mathrm{var}} + \lambda_{\mathrm{cov}}\mathcal{L}_{\mathrm{cov}} \\
&\quad + \lambda_{\mathrm{obj}}\mathcal{L}_{\mathrm{obj}} + \lambda_{\mathrm{ground}}\mathcal{L}_{\mathrm{ground}} + \lambda_{\mathrm{ont}}\mathcal{L}_{\mathrm{ont}} + \lambda_{\mathrm{cal}}\mathcal{L}_{\mathrm{cal}} \\
&\quad + \lambda_{\mathrm{dist}}\mathcal{L}_{\mathrm{dist}}.
\end{aligned}
$$

The weights are not assumed to be commensurate. They must be chosen by dimension-aware normalization, gradient diagnostics, and held-out performance rather than by treating the sum as scale-free.

### 15.1 Observed versus imagined training data

Training batches should retain provenance. Let \(\mathcal{D}_{\mathrm{obs}}\) contain trusted observed transitions and \(\mathcal{D}_{\mathrm{imag}}\) contain model-generated trajectories. Dynamics fitting and factual causal updates use \(\mathcal{D}_{\mathrm{obs}}\). Imagined data may regularize planning or representation learning only under an explicit synthetic-data weight and may not be labeled as observed evidence.

---

## 16 Knowledge Distillation with Alignment and Authority Control

### 16.1 Representation alignment

Teacher and student latent coordinates need not be directly comparable. Let \(A\) map student latents into the teacher space. The representation loss is

$$
\mathcal{L}^{\mathrm{dist}}_{\mathrm{repr}} = \mathbb{E}\,\|A z^S - z^T\|_2^2,
$$

with an orthogonality or condition-number regularizer when appropriate. Matching raw coordinates without alignment is unjustified when dimensions, permutations, rotations, or scales differ.

### 16.2 Dynamic distribution distillation

For probabilistic dynamics,

$$
\mathcal{L}^{\mathrm{dist}}_{\mathrm{dyn}} = \mathbb{E}\,\mathrm{KL}\bigl(p^T(s_{t+1} \mid s_t, a_t) \,\|\, p^S(s_{t+1} \mid s_t, a_t)\bigr),
$$

possibly after mapping student states through \(A\). For ensembles, mean, covariance, and tail-risk predictions should be matched separately.

### 16.3 Semantic distillation

Directly matching raw box centers and raw width parameters is coordinate-dependent. A more invariant semantic objective matches grounded membership margins and relation violations:

$$
\begin{aligned}
\mathcal{L}^{\mathrm{dist}}_{\mathrm{sem}} &= \mathbb{E}_{\xi,p}\bigl(\mu^S_p(\xi) - \mu^T_p(\xi)\bigr)^2 \\
&\quad + \sum_{(p,q) \in \Theta^\Rightarrow} \bigl(\mathcal{L}^{S}_\subseteq(p,q) - \mathcal{L}^{T}_\subseteq(p,q)\bigr)^2 \\
&\quad + \sum_{(p,q) \in \Theta^\perp} \bigl(\mathcal{L}^{S}_\perp(p,q) - \mathcal{L}^{T}_\perp(p,q)\bigr)^2.
\end{aligned}
$$

If teacher and student semantic spaces differ, the grounded samples must be aligned or evaluated through a shared semantic probe.

### 16.4 Logit distillation

For \(K\) classes and temperature \(\tau\),

$$
p^{T,\tau}_i = \frac{e^{t_i/\tau}}{\sum_{j=1}^{K} e^{t_j/\tau}}, \qquad p^{S,\tau}_i = \frac{e^{s_i/\tau}}{\sum_{j=1}^{K} e^{s_j/\tau}},
$$

with

$$
\mathcal{L}^{\mathrm{dist}}_{\mathrm{logit}} = \tau^2\,\mathrm{KL}(p^{T,\tau} \,\|\, p^{S,\tau}).
$$

The exact high-temperature coefficient is stated in Theorem 17.3; it is not generally \(1/2\) unless the class-count normalization is absorbed elsewhere.

### 16.5 Teacher authority boundary

A teacher may be more accurate than a student but remains a predictive model. Distilled outputs do not become authoritative transition evidence. Factual memory still requires trusted observed transitions and verifier lineage.

---

## 17 Correctness Results and Precise Guarantees

**Proposition 17.1** (Containment-loss correctness). For \(\varepsilon_\Rightarrow \geq 0\), the containment loss satisfies

$$
\mathcal{L}^\varepsilon_\subseteq(p, q) = 0
$$

if and only if

$$
\ell_p \geq \ell_q + \varepsilon_\Rightarrow\mathbf{1}, \qquad u_p \leq u_q - \varepsilon_\Rightarrow\mathbf{1}.
$$

In particular, for zero margin it vanishes if and only if \(B_p \subseteq B_q\).

*Proof.* Every summand is nonnegative. The sum is zero if and only if each positive-part argument is nonpositive. These inequalities are exactly the stated lower- and upper-endpoint conditions. □

**Proposition 17.2** (Separation-loss correctness). For \(\varepsilon_\perp > 0\), the separation loss satisfies

$$
\mathcal{L}^\varepsilon_\perp(p, q) = 0 \quad\Longleftrightarrow\quad \min_j \delta_j(p, q) \leq -\varepsilon_\perp.
$$

Hence zero loss certifies separation by at least \(\varepsilon_\perp\) in at least one coordinate.

*Proof.* By definition, \([x]_+ = 0\) if and only if \(x \leq 0\). Substituting \(x = \varepsilon_\perp + \min_j \delta_j\) yields the result. □

**Theorem 17.1** (Grounded entailment soundness). If \(B_p \subseteq B_q\) and \(\xi \in B_p\), then \(\xi \in B_q\).

*Proof.* Because \(\xi \in B_p\), \(\ell_p \leq \xi \leq u_p\). Because \(B_p \subseteq B_q\), \(\ell_q \leq \ell_p\) and \(u_p \leq u_q\). Therefore \(\ell_q \leq \xi \leq u_q\), so \(\xi \in B_q\). □

**Theorem 17.2** (Robust entailment under bounded grounding error). Assume

$$
\ell_p \geq \ell_q + \varepsilon\mathbf{1}, \qquad u_p \leq u_q - \varepsilon\mathbf{1}
$$

for some \(\varepsilon > 0\). If \(\xi \in B_p\) and \(\|\eta\|_\infty \leq \varepsilon\), then \(\xi + \eta \in B_q\).

*Proof.* For every coordinate, \(\xi_j + \eta_j \geq \ell_{p,j} - \varepsilon \geq \ell_{q,j}\) and \(\xi_j + \eta_j \leq u_{p,j} + \varepsilon \leq u_{q,j}\). Thus \(\xi + \eta \in B_q\). □

**Theorem 17.3** (High-temperature distillation limit). Let \(t, s \in \mathbb{R}^K\) satisfy \(\sum_i t_i = \sum_i s_i = 0\). Then

$$
\tau^2\,\mathrm{KL}\bigl(\mathrm{softmax}(t/\tau) \,\|\, \mathrm{softmax}(s/\tau)\bigr) = \frac{1}{2K}\,\|t - s\|_2^2 + O(\tau^{-1})
$$

as \(\tau \to \infty\).

*Proof sketch.* For centered logits, \(\mathrm{softmax}(t/\tau)_i = 1/K + t_i/(K\tau) + O(\tau^{-2})\), and similarly for \(s\). Expanding the KL divergence to second order around the uniform distribution and substituting yields the stated asymptotic. □

**Proposition 17.3** (Non-promotion invariant). Suppose every factual write API requires evidence scope \(\texttt{OBSERVED\_TRANSITION}\) or \(\texttt{REPLAY\_VERIFIED}\), and predictive evaluators can emit only \(\texttt{PREDICTIVE\_ONLY}\). Then no purely predictive computation can create a factual transition or confirmed positive mechanic.

*Proof.* The conclusion follows from the type and authority guard on every factual write path. A predictive result does not satisfy the precondition of any factual write API. The invariant is architectural and must be regression-tested; it is not guaranteed by model accuracy. □

**Corollary 17.1** (Scope of exact verification). Exact box and contract checks guarantee only that the encoded state, bound metric, and declared constraints satisfy their formal conditions. Physical safety additionally requires valid sensing, calibration, model coverage, uncertainty control, actuator compliance, and any independent runtime safety mechanisms mandated by the domain.

---

## 18 Worked Drone Example

Consider a multirotor operating in a mapped but partially changing environment. The observation packet contains synchronized camera, inertial, altitude, localization, battery, and flight-mode data. The scene graph contains the vehicle, obstacles, candidate landing zones, corridor segments, and geofence regions.

### 18.1 Predicates and relations

Possible predicates include

- `inside_authorized_corridor`
- `obstacle_clear`
- `battery_safe`
- `landing_zone_stable`
- `localization_reliable`
- `emergency_reachable`

A structural entailment may be

$$
\texttt{certified\_landing\_zone} \Rightarrow \texttt{landing\_zone\_stable},
$$

and an incompatibility may be

$$
\texttt{inside\_authorized\_corridor} \;\bot\; \texttt{inside\_hard\_no\_fly\_region}
$$

for the same spatial point. Other predicate pairs are irrelevant unless explicitly constrained.

### 18.2 Current action surface

Suppose the current surface is

$$
\Sigma_t = \{\texttt{velocity\_control},\; \texttt{hover},\; \texttt{land},\; \texttt{return\_home}\}
$$

with payload actuation unavailable. A semantic hypothesis that requires payload release may remain plausible as a mission explanation but is not currently realizable. The route is therefore surface-unresolved rather than semantically false.

### 18.3 Bound contract

Assume the proposer suggests “move toward the nearest certified emergency landing zone.” The binder identifies a landing-zone descriptor \(d_L\) and registers

$$
\mu(G_t; d_L) = \text{risk-weighted path distance to } d_L.
$$

The favorable direction is \(d = -1\), because smaller is better. The binder computes the baseline from the trusted current scene, not from the proposer’s numeric estimate. A candidate action is predictively ranked by expected distance reduction, collision risk, localization uncertainty, and surface stability.

After the accepted action, the verifier recomputes the before and after metric from the trusted transition. A decrease exceeding \(\tau_{\mathrm{prog}}\) is \(\texttt{REQUIRED}\) progress. A legal action with negligible change is \(\texttt{IRRELEVANT}\). An increase beyond the failure margin or a geofence violation is \(\texttt{FORBIDDEN}\). A localization discontinuity, stale target binding, or predictive-only evaluation is \(\texttt{UNRESOLVED}\).

### 18.4 Recovery

If localization becomes unreliable, a recovery policy may authorize hover and re-localization. This is an environment- and capability-conditioned recovery action. If the mission deadline or energy reserve is already exhausted, the system must not pretend that the same recovery constitutes a fresh mission attempt; it must execute the appropriate terminal safety action under the higher-priority budget policy.

---

## 19 Implementation Invariants and Test Obligations

A conforming implementation should regression-test at least the following invariants:

1. predictive rollouts cannot call factual transition writers;
2. there is exactly one factual commit point for accepted transitions;
3. no second action is emitted while a prior transition token is pending;
4. containment and incompatibility losses satisfy the equivalences in Section 17;
5. structural box checks are not confused with grounded state membership;
6. the binder recomputes baselines and rejects stale contracts;
7. every route step retains its action-surface contract;
8. a surface mismatch invalidates route realization, not automatically the parent mechanic;
9. semantic proposals cite known canonical claims;
10. a revision cites eligible parents and performs its declared change;
11. route failure does not blanket-contradict all assumptions;
12. positive memory requires observed or independently verified source lineage;
13. proposer-authored explanations remain proposed without independent evidence;
14. recovery preserves mission-scoped observed knowledge and clears state-local execution state;
15. external timeout, energy exhaustion, or action-limit termination cannot emit a reset-like transition;
16. the loop cannot exit normally with an un-ingested accepted action.

Trace artifacts should include the canonical evidence ledger, belief delta, proposer input and output, binder result, route and surface contract, predictive score, pre-action verifier result, pending transition token, post-action observation, contract result, exact verdict, memory event identifiers, and nondeterminism classification.

---

## 20 Research Modules and Domain Substitution

The architecture remains fixed while domain modules vary.

| Core interface | Robotics / drone realization | Abstract reasoning realization |
|---|---|---|
| Perception adapter | Sensor fusion, detection, tracking, mapping | Grid parsing, object extraction, relation graph |
| Action surface | Flight modes, actuator limits, payload and safety authorization | Available action symbols, interaction modes, coordinate actions |
| World model | Stochastic physical and sensor dynamics | State-transition and action-effect model |
| Semantic grounding | Objects, regions, trajectories, hazards | Objects, colors, shapes, topology, transformations |
| Binder metrics | Distance, clearance, energy, stability, tracking error | Graph distance, overlap mismatch, alignment, containment, endpoint error |
| Research modules | Active perception, calibration maneuver, system identification | Action-semantics probe, coordinate probe, ambiguity resolution |
| Recovery policy | Hover, re-localize, return-to-home, divert, land | Level reset or controlled termination when explicitly available |
| Hard verifier | Geofence, collision shield, actuator and energy limits | Action legality, exact state and contract checks |

A research module is allowed to choose an information-gathering action only when it is tied to a registered question with an explicit prior, expected evidence, disconfirming evidence, required surface, and resolution rule. Unregistered random exploration is not a valid degraded fallback.

---

## 21 Development Roadmap

### 21.1 Stage 1: Static verified baseline

Implement the observation adapter, action-surface synchronization, object-centric world model, fixed ontology, corrected box losses, deterministic binder, receding-horizon planner, pre-action verifier, and single post-action commit point.

### 21.2 Stage 2: Calibrated uncertainty and active research

Add ensemble or Bayesian uncertainty, held-out calibration, registered questions, and information-gain probes. Require explicit separation between task progress and epistemic progress.

### 21.3 Stage 3: Canonical evidence and recursive revision

Introduce canonical claims, belief deltas, parent–child hypothesis lineage, assumption statuses, and typed revision operators. Preserve superseded hypotheses for audit and learning.

### 21.4 Stage 4: Event-sourced memory and attempt recursion

Add canonical memory events, deterministic consolidation, mission-scoped transfer, recovery boundaries, and external termination causes. Validate preserved and cleared state explicitly.

### 21.5 Stage 5: Controlled predicate and relation induction

Propose new predicates from persistent residual structure, but require utility, identifiability, held-out stability, and compatibility checks. New predicates remain proposed until observed evidence supports their grounding. Relation induction must distinguish absence of counterexamples from evidence of incompatibility.

### 21.6 Stage 6: Richer semantic geometries

Introduce unions of boxes, temporal constraints, relation-specific spaces, or neural energy regions only when the fixed box family is empirically inadequate. Preserve exact or certified checking for hard constraints whenever possible.

### 21.7 Stage 7: Hierarchical skills and long-horizon planning

Learn temporally extended skills with explicit initiation surfaces, termination conditions, measurable contracts, and failure scopes. High-level plans must compile to lower-level verified actions without bypassing the post-action truth boundary.

---

## 22 Conclusion

The revised UIM is not merely a latent world model with a logical regularizer. It is an authority-structured agent architecture. Its central invariants are that predictions do not become facts, proposals do not become actions, explanations do not become confirmed mechanics, and route failures do not erase unrelated assumptions. Corrected box mathematics provides a coherent geometric ontology, but runtime semantics is grounded in entity membership and measurable state transitions rather than repeated inspection of static box relations.

The architecture is shared across robotics, drones, and abstract reasoning systems because the essential control problem is the same: infer under partial observability, propose testable structure, bind it to measurable quantities, plan under changing action surfaces, verify before and after action, and retain only evidence-grounded knowledge. Different domains supply different constraints and research modules; the authority hierarchy, verification contracts, recursive revision, and event-sourced memory remain unchanged.

---

## References

1. N. P. Brusentsov. *Improving the Logic of Inferences*. New Millennium Foundation, 2012.
2. J. Schmidhuber. Making the world differentiable: On using self-supervised recurrent neural networks for reinforcement learning and planning. Technical Report FKI-126-90, 1990.
3. D. Ha and J. Schmidhuber. World Models. arXiv:1803.10122, 2018.
4. Y. LeCun. A Path Towards Autonomous Machine Intelligence. OpenReview, 2022.
5. G. Hinton, O. Vinyals, and J. Dean. Distilling the Knowledge in a Neural Network. arXiv:1503.02531, 2015.
6. C. Buciluă, R. Caruana, and A. Niculescu-Mizil. Model Compression. In *Proceedings of KDD*, 2006.
7. R. Y. Rubinstein and D. P. Kroese. *The Cross-Entropy Method: A Unified Approach to Combinatorial Optimization, Monte-Carlo Simulation, and Machine Learning*. Springer, 2004.
8. J. B. Rawlings, D. Q. Mayne, and M. Diehl. *Model Predictive Control: Theory, Computation, and Design*. Nob Hill Publishing, second edition, 2017.
9. R. T. Rockafellar and S. Uryasev. Optimization of conditional value-at-risk. *Journal of Risk*, 2(3):21–41, 2000.
10. A. Bardes, J. Ponce, and Y. LeCun. VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning. In *International Conference on Learning Representations*, 2022.
11. L. P. Kaelbling, M. L. Littman, and A. R. Cassandra. Planning and acting in partially observable stochastic domains. *Artificial Intelligence*, 101(1–2):99–134, 1998.
