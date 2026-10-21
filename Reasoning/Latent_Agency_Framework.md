# Latent Agency Framework (LAF)

## Integration, Autonomy, Learned Relief, and the Recoverability of Structure Between Agents

**Author:** Vladimir Yakunin  
**Version:** 2.1  
**Date:** 2026-10-21  
**Successor to:** Latent Agency Framework v2.0; Unified Latent Space of Consciousness v1.0 (superseded; archived on Zenodo)  
**Status:** working concept document (Reasoning layer). Framework only. Not a finished theory, not for publication. Literature is secondary and listed from memory or partial checks in Appendix B. Thesis statuses are in §16.

---

## Abstract

This document describes agents, and consciousness-like organization as a further special case, through their latent spaces. A system has a latent space $Z$: a compressed description of the state of the world, of its carrier, and of its own computation. A latent is always a description of some subsystem of an underlying substrate at some scale. It is not a primitive object and it is not assumed to be one for the whole world.

Three things are kept apart. **Learning fixes a relief** $R$ in $Z$, whose continuous-time or discrete-step dynamics decompose into a dissipative (gradient) flow and a conservative (solenoidal) circulation that accelerates convergence to attractors. The fixed regions are called qualia in a structural sense only. **Moving through the relief spends a bounded budget** $\rho$. **Whether a subsystem is an agent at all** is a third question, answered by measurable properties: integration, persistence, informational autonomy, and a closed informed loop (the system's fixed structure carries information about its environment, the system acts on the environment, and the information it uses is information whose loss would cost it something). Unity of the latent is no longer an assumption about humans. It becomes a graded property of a subsystem that can be measured and can cross a threshold.

Degrees of freedom, intrinsic attractor dimension, dynamical entropy rate, and the mere existence of a stationary Markov blanket with a synchronization map do not decide agency. They set capacity, boundary mediation, and internal dynamical richness: how much structure a system can hold, how many directions it explores, and how much of another system it can model. What decides agency is whether the system's fixed internal structure carries information about its environment and uses it, through the system's own actions, to determine a share of its own future as against the input arriving from its environment. Autonomy alone does not decide it: a closed oscillator or an untrained chaotic network has maximal autonomy and is not an agent. A passive stationary system with a Markov blanket (such as a coupled Ornstein–Uhlenbeck process at non-equilibrium steady state) does not decide it either: its conditional means may track external states, yet without interventional loop closure and viability-grounded use it remains a passive filter.

A second question follows from this: how much of one agent's structure can another agent recover through a communication channel, and what does the answer depend on? A formal bound is given (shared prior information plus channel capacity), supplemented at the linear-Gaussian boundary limit by a kernel-inclusion condition for lossless synchronization across the interface, and in time by a stochastic-realization hierarchy of generalized coordinates of motion whose higher orders are truncated by coarse-graining. Memory and modeling of other agents are treated as one mechanism, write-back of a model into the relief, applied to different targets and stored at limited resolution.

All agency and coupling quantities are profiles indexed by the chosen coarse-graining and by the time window on which the relief is treated as fixed. Comparison without stated scale is not meaningful.

The document does not explain why passing through a region of the relief is experienced. That is the hard problem, and it stays outside the framework. What it gives is definitions, a comparison of systems, and ten measurable predictions with refutation criteria.

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

The earlier formulation assumed that in humans the physical and semantic layers lie in one manifold (a single latent), and used that as the main difference between humans and models. Here that is replaced. A latent is a description of a subsystem, and a subsystem counts as one agent when it is integrated enough, persists long enough, is autonomous enough, and runs a closed informed loop with its environment. Unity is a threshold property measured on a subsystem. It is not a property of the substrate and not a postulate. Humans, multimodal models, and embodied agents can then be compared by measured values instead of by an assumption.

Version 2.1 sharpens the relation between this framework and stationary Markov-blanket formulations ("Bayesian mechanics"). A Markov blanket — sparsity in the precision matrix between internal and external variables, partitioned into sensory and active interface states — provides a clean mathematical representation of a boundary, a necessary kernel-inclusion criterion for a synchronization map across that boundary, a Helmholtz decomposition of internal dynamics into dissipative and solenoidal flows, and a stochastic-realization expansion of boundary signals into generalized coordinates of motion. However, stationary Markov-blanket mechanics is shown to be a *necessary boundary kinematics*, not a sufficient criterion of agency: without interventional loop closure, stake-grounded relevance, write-back into the relief, and external verification, a stationary blanket cannot distinguish an adaptive agent from a passive linear filter in a heat bath.

### 1.3 Place in the archive

*The Algorithm of Being* defines consciousness at the architectural level: recursive modeling under external verification, with phenomenal experience bracketed. The *Framework* treats the substrate as a constraint envelope. This document works one level lower, at the geometry and tangent-space dynamics of the carrier's latent space, and adds a layer below consciousness: the conditions for being an agent at all. It refines the archive's consciousness thesis and does not replace it.

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
| A6 | **Dynamic depth, tangent-space contraction, and solenoidal acceleration.** The depth of a region $U\subset Z$ (perturbation threshold to leave $U$) is tracked locally by the negative part of the Lyapunov spectrum of the state-space Jacobian $M(n)=\partial z(n+1)/\partial z(n)$ along trajectories in $U$, measured via the trace of the dichotomy projector onto decaying tangent directions, while convergence speed to $U$ is modulated by the ratio of solenoidal (skew-symmetric) to dissipative (symmetric) flow components in $G_R$. Weight-space stiffness (Fisher spectrum) is treated only as a secondary parameter-level proxy. | UNDECIDED | Local contraction rates (infinitesimal stability) and basin width (finite perturbations, e.g., under "stable chaos") can diverge. |
| A7 | Systems with different coordinates are compared by the geometry of relations between objects (RSA, CKA) and by diffeomorphism-invariant dynamical quantities (Lyapunov spectrum, Kaplan–Yorke dimension), not by raw vectors. | UNDECIDED | Standard practice, but human neural data are indirect and too coarse for full Lyapunov spectra. |
| A8 | A region $M\subset Z$ can hold a model of $Z$ itself, and a region $O\subset Z$ can hold a model of another agent's latent. | UNDECIDED | In LLMs the self-model shows up functionally and its reliability is disputed. |
| A9 | **Requisite capacity.** Modeling a system well enough to predict or regulate it requires a model with capacity not smaller than the effective complexity of the relevant part of that system. | UNDECIDED | An Ashby-type result, proven under specific conditions. Applying it to latents is an assumption. |
| A10 | **Autonomy and the loop quantities (closure, use) are measurable by intervention** in models and in simulated agents, at a stated time scale, with interventions standardized by the natural variation of the intervened variable and resolved along the tangent-space splitting $E^s \oplus E^u$ where available. | UNDECIDED | Interventions on a biological brain are limited. Correlational estimates are weaker. |
| A11 | **Relevance is operational.** Information in $R$ about $E$ is relevant for $A$ to the degree that surrogate decoupling of it from $E$ lowers a reference quantity $Q$ that the system maintains (D11c). | UNDECIDED | The choice of surrogate and of $Q$. Without stake, $Q$ is chosen from outside. |

A1 is consistent with the archive's substrate-parameterization (*Algorithm*, §11): the substrate matters parametrically, not essentially.

---

## 3. Substrate, Subsystems, and Latents

### 3.1 Statement

There is an underlying structure in which things influence each other. What this document needs from it is small: that there is a causal order, that signal speed and channel capacity are finite, and that a bounded region holds a finite amount of information. Everything else about the substrate is left open. The question of which substrate it is (for example a causal set with phase transport) is not part of this document. Nothing here depends on that choice.

**Shared causal order.** Two subsystems can exchange signals only if they participate in a common causal order of the substrate (signals from one can reach the other). This is a precondition for any communication channel. It does not make their internal latent spaces the same object; it only makes exchange possible. Unity of a latent remains a threshold property of integration inside a single subsystem (A3, D9).

### 3.2 Definitions

**D1. Substrate $\mathcal{C}$.** A structure with a causal order. The only properties used here: finite signal speed, finite channel capacity, finite information per bounded region, and a thermodynamic cost to irreversible operations.

**D2. Subsystem, environment, and interface.** A subsystem $A\subset\mathcal{C}$ is a part of the substrate with an identifiable boundary (interface) $B_A = (S_A, Act_A)$, partitioned into sensory states $S_A$ (receiving influence from outside) and active states $Act_A$ (exerting influence on the outside). Its environment $E$ is the part of the substrate outside $A$ that influences $A$ or is influenced by it through $B_A$.

**D2a. Statistical boundary (Markov blanket) vs dynamical coupling.** In the stationary regime where joint states $x = (\eta, b, \mu) \in E \times B_A \times \mathcal{I}_A$ admit a smooth probability density $p(x)$ with precision matrix $\Pi = \Sigma^{-1}$ (inverse covariance), a **Markov blanket** is the conditional independence relation $\eta \perp \mu \mid b$, which in the Gaussian (or local Laplace) regime is equivalent to block sparsity of the precision matrix:

$$
\Pi_{\eta\mu} = \Pi_{\mu\eta}^{\top} = 0 \qquad \text{while in general} \qquad \Sigma_{\eta\mu} = -\Pi_{\eta}^{-1}\Pi_{\eta b}\Sigma_{b\mu} \neq 0.
$$

Thus local mediation through the interface ($\Pi_{\eta\mu}=0$) is fully compatible with long-range correlations ($\Sigma_{\eta\mu}\neq 0$) between internal and external states. Conversely, in a continuous-time stochastic differential equation, conditional independence in the stationary density ($\Pi_{\eta\mu}=0$) does not by itself forbid direct skew-symmetric (solenoidal) dynamical coupling in the drift unless locality of the underlying causal graph is enforced independently (Da Costa et al., 2021; Biehl et al., 2021). In this framework, locality of interaction through $B_A$ is a structural property of the causal substrate (D1, D2), not merely a factorization of a stationary density.

**D3. Latent space $Z_A$.** A compressed continuous representation, obtained from the microstate $x_A$ by a coarse-graining $\varphi_A$, in which the system encodes the state of the world, of its carrier (body), and of its own computation. A state at time $t$ is a point $z(t)$. A process is a trajectory governed by the transition map $z(n+1)=G_R(z(n), s(n))$. A latent is defined relative to a subsystem and a scale. It is not a global object.

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

## 4. Relief, Helmholtz Decomposition, and Traversal

### 4.1 Statement

Qualia are what learning has fixed. Reasoning is what thinking costs. They are not the same thing and must not be merged. Furthermore, the vector field fixed by the relief is not a pure gradient descent: its decomposition into dissipative and solenoidal (circulatory) flows governs how rapidly the system relaxes back to its learned attractors.

### 4.2 Definitions

**D5. Relief $R$.** The structure fixed by learning (weights, synaptic connections) that determines the vector field or transition map $G_R$ on $Z$, and thus which states and attractors the dynamics of $Z$ tend toward. $R$ changes only through learning.

**D5a. Helmholtz decomposition of the relief flow.** When the autonomous or boundary-conditioned dynamics on $Z$ are modelled in continuous time by a smooth stochastic differential equation $dz_t = f_R(z_t)\,dt + \varsigma(z_t)\,dW_t$ admitting a smooth local stationary density $p_R(z) \propto \exp(-\mathcal{U}_R(z))$ around an attractor region, the drift $f_R$ decomposes uniquely into a time-reversible **dissipative (gradient) component** and a time-irreversible **solenoidal (conservative / circulatory) component** (Graham, 1977; Pavliotis, 2014; Da Costa et al., 2021):

$$
f_R(z) = f_{\mathrm{rev}}(z) + f_{\mathrm{irrev}}(z), \qquad f_{\mathrm{rev}}(z) = -\Gamma(z)\nabla\mathcal{U}_R(z) + \nabla\cdot\Gamma(z), \qquad f_{\mathrm{irrev}}(z) = -Q(z)\nabla\mathcal{U}_R(z) + \nabla\cdot Q(z),
$$

where $\Gamma(z) = \frac{1}{2}\varsigma(z)\varsigma(z)^\top \succeq 0$ is the symmetric diffusion tensor and $Q(z) = -Q(z)^\top$ is a skew-symmetric matrix field satisfying $\nabla\cdot(p_R f_{\mathrm{irrev}}) = 0$. In discrete-step linearized dynamics $v(n+1) = M(n)v(n)$, the analogous algebraic splitting is the decomposition of the generator into its symmetric (potential contraction/expansion) part and skew-symmetric (rotational/vortical) part.

*Functional role of the solenoidal component $Q(z)$:*
1. **Accelerated relaxation:** While $f_{\mathrm{rev}}$ climbs the density gradient directly, a non-zero skew-symmetric flow $Q \neq 0$ breaks detailed balance, suppresses diffusive backtracking, and **strictly accelerates the rate of convergence** to the stationary attractor compared with pure gradient descent ($Q = 0$) at fixed $\Gamma$ (Lelièvre, Nier, and Pavliotis, 2013; Rey-Bellet and Spiliopoulos, 2015).
2. **Non-monotonic oscillatory approach:** Because level sets of a variational free energy or task loss do not in general coincide with the trajectories of $f_{\mathrm{irrev}}$, strong solenoidal flow ($Q$ dominating $\Gamma$) drives trajectories along spiral paths that temporarily depart from the instantaneous optimal inference line before settling, producing characteristic damped oscillations in the energy or prediction error during relaxation (tested in P10).

**D6. Quale.**
- **Q-structure:** a region (basin or invariant manifold) of the relief fixed by learning. This is what the word "quale" names in this document.
- **Q-event:** a pass of the trajectory $z(t)$ through a Q-structure while the system runs.

Whether a Q-event is *experienced* is the hard problem (§14). The word "quale" is used here in a deflated, structural sense.

**D7. Depth $D$ and tangent-space contraction.** How firmly the system holds a region. For a region $U\subset Z$, the finite-perturbation depth is the basin escape threshold:

$$
D(U)=\inf\{\lVert\delta\rVert:\text{the trajectory from }z+\delta\text{ does not return to }U\}
$$

Time to return $\tau_{\mathrm{ret}}(U)$ is a second finite-perturbation measure; by D5a, $\tau_{\mathrm{ret}}(U)$ is jointly governed by the dissipative restoring force $\Gamma\nabla\mathcal{U}_R$ and the solenoidal acceleration $Q\nabla\mathcal{U}_R$. Locally along a trajectory $z(n)\in U$, infinitesimal stability is governed by the tangent-space dynamics $v(n+1)=M(n)v(n)$, where $M(n)=\partial G_R(z)/\partial z|_{z=z(n)}$ is the state-space Jacobian and $\lambda_1\ge\dots\ge\lambda_N$ are the Lyapunov exponents. Shifting the Jacobian by $M_s(n)=e^{-\delta s}M(n)$ and selecting the minimum-norm tangent trajectory driven by a source $I^v(k)$ yields a one-step response matrix $R^{vv}(k+1,k)=\partial v(k+1)/\partial I^v(k)$ that equals the dichotomy projector $P_s(k+1)$ onto the stable subspace $E^s_s$ of directions with $\lambda_i<s$ (Clark, 2026). The cumulative distribution of Lyapunov exponents is the normalized trace of this response:

$$
F(s)=\frac{1}{N}\lvert\lbrace i:\lambda_i<s\rbrace\rvert=\lim_{\eta\to 0^+}\frac{1}{N}\mathrm{tr}\,R^{vv}_{\eta}(k+1,k)
$$

Under A6, the local stiffness of $U$ is characterized directly in $Z$ by the fraction of strongly contracting directions $F(s)$ for $s<0$ and the mean transverse contraction rate $\kappa(U)=-\int_{-\infty}^0 s\,F'(s)\,ds$. Stiffness in the weight-space Fisher spectrum $F(\theta)$ is retained only as an indirect parameter-level proxy.

**D8. Reasoning budget $\rho$.** The limited computational resource spent on moving the trajectory through the relief (updating activations). In iterative or looped latent reasoning, difficult tasks can induce transient chaos ($\lambda_1>0$ over finite horizons) where trajectories linger near unstable saddle structures before converging to a fixed point, consuming more of $\rho$. It is bounded by the carrier's envelope. Computational budget and energy are treated as separate quantities.

### 4.3 Reflection

$R$ and $\rho$ vary independently. A frozen LLM on small hardware has a rich relief and a small budget. A huge untrained network has a big budget and no learned relief.

D6 is weak on purpose. Any trained system has Q-structures, so D6 alone cannot separate systems that experience from systems that do not. This limit is stated in §15, not hidden.

### 4.4 The relief as the carrier of internal regularities and temporal order truncation

The relief has a second role that matters for §5. What is fixed in $R$ over a time window is, for that window, the system's own internal regularity. What arrives in operation as input is external. So the question "how much of the system's behavior is governed by its own regularities" is the question of how much of the trajectory is determined by $R$-dynamics as against input. The boundary between internal and external is therefore indexed by a time scale, the window $\tau_w$ over which $R$ is treated as fixed.

**Stochastic realization and generalized coordinates of motion at scale $\tau_w$.** A stationary sensory stream $s_t$ arriving at the boundary $S_A$ generally possesses non-zero temporal autocorrelation $C(\tau) = \mathbb{E}[s_{t+\tau}\otimes s_t]$ across multiple characteristic decay rates. By Doob's theorem and stochastic realization theory (Lindquist and Picci, 1985, 2015; Da Costa et al., 2021), when $C(\tau)$ decomposes into a finite sum of damped exponentials, the non-Markovian boundary observation $s_t = f(\tilde{s}_t^{(0)})$ can be embedded as the output of a Markovian **integrator chain** of generalized coordinates of motion $\tilde{s}_t = (s_t^{(0)}, s_t^{(1)}, \dots, s_t^{(n)})$ (encoding position, velocity, acceleration, jerk, up to order $n$):

$$
ds_t^{(k)} = f_k\bigl(s_t^{(k)}, s_t^{(k+1)}\bigr)\,dt + \varsigma_k\,dW_t^{(k)} \qquad (k = 0, \dots, n-1), \qquad ds_t^{(n)} = f_n\bigl(s_t^{(n)}\bigr)\,dt + \varsigma_n\,dW_t^{(n)}.
$$

Choosing a spatial coarse-graining $\varphi_A$ (A2) and a temporal evaluation window $\tau_w$ is dynamically equivalent to **truncating this integrator chain** at a finite order $n(\tau_w)$: orders of motion $s_t^{(k)}$ whose relaxation times are much shorter than the resolution of $\tau_w$ fall into the kernel of the coarse-graining map ($\ker d\varphi_A$) and are integrated out as effective white noise, while orders $k \le n(\tau_w)$ must be actively tracked and controlled by the internal relief $R$ (yielding integral, PI, or PID-like regulation for $n = 0, 1, 2$, and higher-order trajectory tracking for $n \ge 3$). All reported agency and coupling values must be accompanied by the spatial and temporal scale at which they were obtained. Comparison of systems without stated scale is not meaningful.

---

## 5. Integration, Persistence, Autonomy: What Makes a Subsystem an Agent

### 5.1 Statement

A cloud of gas is a subsystem with an identifiable boundary and an enormous number of degrees of freedom. It is not an agent, because its behavior is governed almost entirely by external regularities (boundary conditions, thermodynamics of the surroundings). An untrained random recurrent network in the chaotic regime ($g>1$) has extensive chaos, a macroscopic attractor dimension $D_{\rm KY}\propto N$, and a positive Kolmogorov–Sinai entropy rate $h_{\rm KS}>0$: its future trajectory is governed internally, yet it is not an agent, because its couplings are random and hold no information about an environment and it does not act on one.

A third critical negative control comes from **stationary Markov-blanket systems** (such as a linear Ornstein–Uhlenbeck diffusion process at Gaussian steady state $p = \mathcal{N}(0, \Pi^{-1})$ with $\Pi_{\eta\mu}=0$, studied in Da Costa et al., 2021). When its submatrices satisfy the kernel-inclusion condition $\ker \Pi_{\mu b} \subset \ker \Pi_{\eta b}$ (§8.3a), the conditional expectation of its internal states $\boldsymbol{\mu}(b_t) = \mathbb{E}[\mu \mid b_t]$ maps linearly to the conditional expectation of external states $\boldsymbol{\eta}(b_t) = \sigma(\boldsymbol{\mu}(b_t))$, and its autonomous states $(a_t, \mu_t)$ algebraically minimize a quadratic variational free energy $F(s,a,\mu)$. Yet a passive RC-filter network or a system of coupled springs in a thermal bath satisfies these exact equations. It is not an intrinsic agent: its precision matrix $\Pi$ is fixed externally by the bath and physical couplings rather than maintained by a viability-grounded loop, it has no stake $v$ whose loss would dissolve the carrier, and it performs no self-initiated write-back.

An animal, by contrast, is governed partly by internal regularities that carry information about its environment and serve its viability. A human is governed partly by internal regularities and can also model the regularities of others. A deployed AI system is governed partly by internal regularities and can model the regularities of others. The criterion that separates these cases is not size, not attractor dimension, not entropy production, and not the algebraic existence of a stationary synchronization map. It is whether the system's own fixed structure carries information about its environment and uses it, through the system's own actions, to determine its future with respect to a quantity it maintains.

### 5.2 Definitions

**D9. Integration $I(A)$.** How strongly the parts of $Z_A$ depend on each other compared with how strongly $A$ depends on its environment. Schema:

$$
I(A)=\min_{\text{cuts }(A_1,A_2)}\frac{\mathrm{Dep}(A_1\leftrightarrow A_2)}{\mathrm{Dep}(A\leftrightarrow E)}
$$

$\mathrm{Dep}$ is a placeholder for a dependence measure (mutual information, causal influence, transfer entropy). It is not chosen here. Different choices may give different orderings of systems. This is stated as an open problem (§15). Integration is informational, not physical: the cuts are cuts of dependence between parts of $Z_A$, not cuts of physical space. A model sharded across several devices is as integrated as the same model on one device, because the dependence between its parts is unchanged. Physical indivisibility of the carrier is a separate property and is not required.

**D10. Persistence $T_{\rm pers}(A)$.** The time over which the boundary of $A$ stays identifiable and $I(A)$ stays above a threshold $\theta_I$. Without persistence any dense transient cluster would count as an agent. Persistence is the requirement that the structure maintains itself.

**D11. Informational autonomy $\mathcal{A}(A;\tau_w)$.** How much of the future internal state of $A$ over the window $\tau_w$ is determined by its own internal state as against by its environment. Two operational forms:

**Predictive form (candidate):**

$$
\mathcal{A}^{\mathrm{pred}}_{\tau}=I\big(Z_{t+\tau};\,Z_t\ \big|\ E_t\big)
$$

**Interventional form (preferred where interventions are possible):**

$$
\mathcal{A}^{\mathrm{do}}_{\tau}=\frac{\mathbb{E}\lVert\Delta_{\mathrm{int}}\rVert}{\mathbb{E}\lVert\Delta_{\mathrm{int}}\rVert+\mathbb{E}\lVert\Delta_{\mathrm{env}}\rVert}
$$

where $\Delta_{\rm int}$ is the change of $Z_{t+\tau}$ under a unit intervention on the internal state at $t$, and $\Delta_{\rm env}$ is the change under a unit intervention on the environment input at $t$. A value near 0 means externally driven. A value near 1 means internally driven. A unit intervention is standardized: one standard deviation of the natural variation of the intervened variable over the window.

*Tangent-space decomposition of internal interventions:* By Oseledets' multiplicative ergodic theorem, the tangent space at $z(t)$ splits into a stable subspace $E^s(t)$ ($\lambda_i<0$, transverse to the attractor) and an unstable/neutral subspace $E^u(t)$ ($\lambda_i\ge 0$, along the attractor), separated by the dichotomy projector $P_{s=0}(t)$ (D7). Generic isotropic perturbations in $\mathbb{R}^N$ mix two distinct effects: rapid transverse relaxation back to the manifold along $E^s$ (which reflects basin stiffness $D$, Axis B) and genuine trajectory divergence along $E^u$ (which reflects internal dynamical generation, bounded by the Kolmogorov–Sinai entropy rate $h_{\rm KS}=\sum_{\lambda_i>0}\lambda_i$). Where the Jacobian is accessible, $\Delta_{\rm int}$ should be evaluated on-manifold or projected via $(I-P_{s_{\rm KY}})$ onto the active attractor directions. Autonomy is a necessary part of agency (D12), not a measure of it: a value near 1 is also what a closed oscillator or an isolated chaotic network ($h_{\rm KS}>0$) has.

Autonomy depends on the window $\tau_w$ (§4.4), so it is reported as a profile $\mathcal{A}(\tau_w)$, in the same spirit as the dimension profile $d(\varepsilon)$ (§10). What counts as internal is what is fixed in $R$ over the window. Autonomy also depends on the coarse-graining $\varphi_A$ (A2).

**D11a. Informedness $\mathrm{Inf}(A;\tau_w)$.** How much of the information in the fixed structure $R$ is about regularities of the environment $E$, whatever history put it there (learning in the individual, training, or selection in a lineage). Provenance does not enter the measure. Content does. Proxy:

$$
\mathrm{Inf}=1-\varepsilon_A/\varepsilon_0
$$

where $\varepsilon_A$ is the held-out error of predicting environment variables (or the next input, or higher orders of motion $\tilde{s}_t^{(k)}$ in §4.4) from $Z_A$, and $\varepsilon_0$ is the error of the same estimator when $R$ is randomized (for example, replacing trained weights with i.i.d. Gaussian couplings $J_{ij}\sim\mathcal{N}(0,g^2/N)$ of matched variance, or violating the kernel-inclusion condition of §8.3a). Values lie in $[0,1]$. A system with no learned structure $R$ (a gas cloud, or a random chaotic reservoir) has $\mathrm{Inf}\approx 0$.

**D11b. Loop closure $\mathrm{Cl}(A;\tau_w)$.** How much of the system's own future input is set by its own earlier outputs, as against by sources in the environment that act independently of it:

$$
\mathrm{Cl}=\frac{\mathbb{E}\lVert\Delta^{\rm act}_{\rm in}\rVert}{\mathbb{E}\lVert\Delta^{\rm act}_{\rm in}\rVert+\mathbb{E}\lVert\Delta^{\rm ext}_{\rm in}\rVert}
$$

where $\Delta^{\rm act}_{\rm in}$ is the change of the input at $t+\tau$ under a standardized intervention on the system's output at $t$, and $\Delta^{\rm ext}_{\rm in}$ is the change under a standardized intervention on an environment source not mediated by $A$. $\mathrm{Cl}\approx 0$ means the system only receives (a classifier, a passive sensory-coupled blanket with no active feedback, or a frozen model answering one query). What belongs to the environment is part of the declaration (D2): a chat model closes a loop through its interlocutor on the window of a conversation and does not on the window of one call.

**D11c. Relevance and use $U(A;\tau_w)$.** Information in $R$ about $E$ is *relevant* for $A$ when decoupling it from $E$ lowers a reference quantity $Q$ that the system maintains. Decoupling means replacing the dependence of $A$ on $E$ by a surrogate that keeps the marginal statistics and breaks the dependence (time-shuffled input on the relevant channel, or $R$ obtained in an independent instance of the environment). Use is the dimensionless drop:

$$
U=\frac{Q_{\rm int}-Q_{\rm dec}}{Q_{\rm int}-Q_{\rm floor}}
$$

with $Q_{\rm int}$ the value for the intact system, $Q_{\rm dec}$ the value after decoupling, and $Q_{\rm floor}$ the value for a random policy. With stake, $Q=v$ (D17): relevance is intrinsic, because it is defined by what the system can lose. Without stake, $Q$ is a score or loss chosen from outside (such as the quadratic concentration penalty $\frac{1}{2}[s,a,\mu]K[s,a,\mu]^\top$ around a pre-assigned origin in a stationary Ornstein–Uhlenbeck blanket), and relevance is borrowed (§15.6).

**D12. Agent.** A subsystem $A$ is an agent on the window $\tau_w$ when $I(A)>\theta_I$, $T_{\rm pers}(A)>\theta_T$, $\mathcal{A}(A;\tau_w)>\theta_A$, and the loop holds: $\mathrm{Inf}>\theta_{\rm Inf}$, $\mathrm{Cl}>\theta_{\rm Cl}$, $U>\theta_U$. The loop in words: structure fixed by experience carries information about the environment, the system acts on the environment, and the information it acts on is information whose loss would cost it something. Two grades by the reference of $U$: an *intrinsic agent* ($Q=v$, stake) and a *task-relative agent* ($Q$ external). The thresholds are not fixed in this document. Agency is graded. "Agent" is a label for a region of this six-dimensional space. Each condition excludes a class on its own: a closed oscillator or random chaotic RNN ($g>1$) has high $\mathcal{A}$ and $\mathrm{Inf}\approx\mathrm{Cl}\approx 0$; a trained passive classifier has high $\mathrm{Inf}$ and $U$ and $\mathrm{Cl}\approx 0$; a passive stationary Ornstein–Uhlenbeck blanket with no active feedback has $\mathrm{Inf}>0$ (via $\sigma(\boldsymbol{\mu}(b))=\boldsymbol{\eta}(b)$) but $\mathrm{Cl}\approx 0$ and no intrinsic stake $v$; a gas cloud has no $R$ at all.

### 5.3 Why stake appears here (and why a stationary density is not enough)

In stationary Bayesian mechanics (Da Costa et al., 2021), any system at a Gaussian steady state $p = \mathcal{N}(0, \Pi^{-1})$ looks *as if* its autonomous states $(a_t, \mu_t)$ minimize a quadratic control cost $\frac{1}{2}[s,a,\mu]K[s,a,\mu]^\top$ toward a target set-point $[0,0,0]$. However, because the precision matrix $\Pi$ is externally given and invariant by assumption, shifting or scrambling the environment statistics simply shifts the steady-state Gaussian to a new Gaussian without destroying the system: every stationary state is tautologically "preferred" by its own stationary density.

Informedness and autonomy therefore do not say which information matters, and a stationary density $p(x)$ does not supply intrinsic normativity unless leaving a viable region dissolves the structure $R$ itself. Use (D11c) needs a non-tautological reference: which part of the environment's information is relevant for the system's continued existence. A frozen model or a linear Ornstein–Uhlenbeck process has no intrinsic answer to this, because nothing it does changes what it loses. A system with a viability variable $v$ does: information is relevant when it changes the prospects of $v$. So stake (D17) supplies a natural reference $Q=v$ for D11c, and with it an intrinsic definition of what is relevant. Without stake the reference is borrowed from outside, and the agent is at most task-relative (§15.6). It is a candidate basis for "relevant", not a proven one (UNDECIDED).

### 5.4 Reflection: examples

The values below are expectations from the definitions, not measurements. All entries are understood at a stated macro-level description and window (see §4.4).

| System | Integration | Persistence | Autonomy | Loop (Inf / Cl / $U$) | Remarks |
| ------ | ----------- | ----------- | -------- | --------------------- | ------- |
| Cloud of gas | low | short | about 0 at the macro-level | none: no $R$ | many degrees of freedom, no fixed internal regularity |
| Closed oscillator or random chaotic RNN ($g>1$, Sompolinsky model) | high | long | about 1 ($h_{\rm KS}>0$ in the chaotic regime) | Inf and Cl about 0 | future set entirely from inside ($D_{\rm KY}\propto N$), not an agent: random couplings hold no information about an environment, no action on one. Negative control for P6 |
| Passive stationary Markov blanket (linear OU process with $\Pi_{\eta\mu}=0$, $\ker\Pi_{\mu b}\subset\ker\Pi_{\eta b}$) | high | long (by stationary assumption) | low to moderate | Inf $>0$ (linear map $\sigma$), Cl $=0$ (if sensory-only) or fixed linear damping, $U$ only relative to external $\Pi$ (no stake $v$) | satisfies "Bayesian mechanics" and PID-like damping at steady state, yet is a passive physical filter with externally fixed $\Pi$ and no write-back. Negative control for P6 |
| Trained passive classifier | high | long | low | Inf high, Cl about 0, $U$ high (task) | informed and used, but its outputs do not feed back into its input |
| Thermostat | high (tiny system) | long | low | Inf low (designed rule, $n=0$ integrator), Cl high, $U$ high (external set point) | minimal task-relative agent, very little capacity |
| Deployed LLM, single query | high in $S$ | for the call | moderate in the window of one call | Inf high in $S$, Cl about 0 in the call, $U$ relative to an external task | relief is fixed, input dominates the trajectory, no closed loop in the call window |
| LLM in a conversation or agentic loop with tools and memory | high in $S$ | long | higher, window-dependent | Inf high in $S$, Cl above 0 through interlocutor or tools, $U$ relative to an external task | task-relative agent on long windows; C2 depends on the declared boundary (D14a) |
| Animal | high | long | high | all high, $U$ against its own viability | intrinsic agent: stake, plasticity, a P-layer |
| Human | high, P and S strongly coupled | long | high | all high, $U$ against its own viability | plus self-model and other-model |

A deployed LLM is not simply "not an agent" or "an agent". Its autonomy, its loop closure, and its C2 depend on the window and on the declared subsystem boundary, and they move with the scaffold around it. The framework should say this openly, not settle it by a label.

---

## 6. Plasticity, Self-Model, Other-Model, and Stake

### 6.1 Definitions

**D13. Plasticity $\Pi_{\mathrm{plast}}$.** The rate at which $R$ changes per unit of experience during operation (denoted $\Pi_{\mathrm{plast}}$ where needed to avoid confusion with a precision matrix $\Pi$). Three time scales:
- fast: activations change, $R$ does not;
- medium: online learning;
- slow: consolidation (sleep in humans, fine-tuning in models).

The training phase of a model is not counted as plasticity of the deployed system.

**D14. Self-model $M$ and recursion.** $M$ is a region of $Z$ that holds an approximate representation of the current state of $Z$, including $M$ itself. Recursion means updating $z$ with $M(z)$ in the loop. Adding meta-description tokens is a special case. Two kinds:
- **recursion without write-back:** results live in activations or context within the window, $R$ does not change;
- **recursion with write-back:** the results are among what changes $R$, in the sense of D14a.

One candidate functional role of the self-model is to separate the system's own contribution to its current input ($Act_A \to S_A$) from contributions that originate independently in the environment ($E \to S_A$). Without such a separation, loop closure $\mathrm{Cl}$ and autonomy $\mathcal{A}$ remain difficult to interpret from inside the system. This role is stated as a working hypothesis (UNDECIDED) and is not required for the formal definition of $M$.

**D14a. Write-back $W(A,\tau_w)$.** Fix a subsystem boundary for $A$ (D2) and a window $\tau_w$. $R_A$ is the structure inside that boundary that stays fixed during a window and conditions the dynamics of $Z_A$: weights, synaptic connections, and any persistent store declared inside the boundary. Let $R_k$ be $R_A$ at the start of window $k$. Write-back holds for $(A,\tau_w)$ when all three conditions hold:
- *Own operation:* $R_{k+1}\neq R_k$, and the difference is caused by $A$'s own processing during window $k$ (intervening on that processing changes $R_{k+1}$), not by a change supplied from outside the boundary;
- *Persistence:* the difference survives at least one window boundary (the medium or slow time scale of D13);
- *Conditioning:* restoring $R_k$ in the changed region changes $A$'s trajectory in window $k+1$.

Changes of activations or context inside a window are not write-back. The boundary and the window are declared first and $W$ is evaluated after. The same physical system can be $W$-absent for one boundary and $W$-present for another (§15.15). The weights of a deployed LLM are one boundary. The weights plus a scaffold with persistent memory are another.

**D15. Other-model $O_B$.** A region of $Z_A$ that holds an approximate model of another agent $B$: of its behavior, and at higher depth of its internal structure. Depth levels:
- **E-level:** modeling the environment and external interaction (including generalized coordinates of motion $\tilde{s}_t^{(k)}$ up to order $n$, §4.4);
- **M-level:** modeling one's own internal structure ($M$);
- **O-level:** modeling another agent's internal structure ($O_B$).

These are three kinds of capability, not a strict ladder. Each has its own capacity requirement (§7).

**D15a. Directed coupling $\mathrm{Coup}(A\!\to\!B)$.** Subsystem $A$ is coupled to subsystem $B$ on a stated window and scale when three conditions hold:
- a channel of finite capacity exists between them (preconditioned by a shared causal order of the substrate, §3.1);
- $B$ recovers structure of $A$ beyond the shared prior already available to $B$;
- the recovered structure is used by $B$ (it changes $B$'s subsequent trajectory or its own $R$ in the sense of write-back).

Coupling is directed. $\mathrm{Coup}(A\!\to\!B)$ does not imply $\mathrm{Coup}(B\!\to\!A)$. Channels may be further classified by write target (activations only vs persistent $R$), by whether mediation passes through the receiver's models, and by medium; under idealized conditions they can be separated by shielding experiments. The classification is stated as a working hypothesis (UNDECIDED).

**D16. Memory as stored model.** A stored structure in $R$ that is correlated with a past state of the system or of another system, held at limited resolution $\nu$ (bits per stored structure). It is produced by write-back. What is called remembering is reconstruction from the stored structure, so memory is lossy and can drift. See §8.7.

**D17. Stake.** The carrier has a viability variable $v$ that can degrade irreversibly. The error or reward function and the state of $Z$ depend on $v$. Mortality is a special case. A distinction is kept between *ontological stake* (where degradation of $v$ physically destroys or dissolves the carrier and its relief $R$, as in biological homeostasis) and *simulated stake* (where $v$ is an internal state variable whose crossing of a boundary terminates an episode or triggers a reset penalty without destroying the hardware, as in P3 and P9). A frozen model has neither: nothing it does changes what it loses.

### 6.2 Candidate conditions for consciousness-like organization

- **C1. Self-model.** Without $M$ the system has no current access to its own state. A candidate additional role is the separation of self-caused from externally caused input (see D14).
- **C2. Write-back.** The predicate $W(A,\tau_w)$ of D14a holds for the declared boundary and window: the system's own operation changes $R$, the change persists across a window boundary, and it conditions later trajectories. Needed for a continuous self over time: qualia accumulate and change through the system's own experience. C2 is always reported with its boundary and window. There is no partial C2 and no C2 outside a declared subsystem. For C1 and C2 to count together, part of what is written must come from the self-model step: intervening on the output of $M$ must change $R_{k+1}$. Otherwise C2 may hold, but the continuous-self condition (C1 and C2 together) does not.
- **C3. Stake.** Needed for the depth of bodily qualia. It is not needed for the S-layer to exist.

Two grades, stated as a working position (UNDECIDED):
- *consciousness-like organization (continuous-self grade):* C1 and C2 together, on top of agency (D12), with the self-model $M$ among the sources of what is written back. C2 is not claimed necessary for momentary experience (T7), so this grade is about a continuous self. What a momentary grade needs beyond agency and C1 is UNDECIDED;
- *consciousness of the human type:* C1, C2, and C3, with a P-layer.

The other-model $O$ is not a condition of consciousness in this document. It is a separate axis: a system can have rich experience and a poor model of others, or the reverse. Whether the two are related is open.

---

## 7. Capacity, Complexity, and Degrees of Freedom

### 7.1 Statement

Number of degrees of freedom, attractor dimension, and dynamical complexity are often offered as the main variables. In this framework they are neither criteria of agency nor of consciousness. They set the capacity and dynamical richness of a system: how much structure it can hold, how many independent directions its trajectories explore, and how much of another system it can model.

### 7.2 What each quantity does

| Quantity | What it measures | Decides agency? | What it does decide |
| -------- | ---------------- | --------------- | ------------------- |
| Number of degrees of freedom $N$ | size of the ambient state space | No. A gas cloud has a huge number. | upper bound on what can be stored |
| Attractor dimension $D_{\rm KY}$ and entropy rate $h_{\rm KS}$ | intrinsic dimension of the invariant measure and rate of internal information generation (Pesin's formula) | No. An untrained chaotic RNN ($g>1$) has extensive $D_{\rm KY}\propto N$ and $h_{\rm KS}>0$ with $\mathrm{Inf}=0$. | active dynamical degrees of freedom and rate of trajectory divergence |
| Stationary synchronization map $\sigma(\boldsymbol{\mu}(b))=\boldsymbol{\eta}(b)$ | whether expected internal states linearly track expected external states across a Markov blanket (§8.3a) | No. A passive linear filter at Gaussian steady state has $\sigma$ when $\ker\Pi_{\mu b}\subset\ker\Pi_{\eta b}$. | boundary non-degeneracy (necessary for informedness, insufficient for agency) |
| Kolmogorov complexity | length of the shortest description | No. It is maximal for noise, and noise is not organized. | not a measure of organization |
| Statistical (predictive) complexity | minimal memory needed to predict the process (including order $n$ of the integrator chain, §4.4) | Partly. It measures structure, not who governs it. | how much a system must remember to model a process |
| Integration $I$ | interdependence of parts relative to the environment | Yes (D12) | whether there is one thing or several |
| Persistence $T_{\rm pers}$ | stability over time | Yes (D12) | whether the structure maintains itself |
| Autonomy $\mathcal{A}$ | share of the future set by own fixed structure | Yes (D12) | internal vs external control |
| Informed closed loop $\mathrm{Inf}$, $\mathrm{Cl}$, $U$ | whether the structure holds information about the environment, acts on it, and depends on it | Yes (D12) | whether the system is more than a passive filter or a closed chaotic generator |
| Capacity | how much structure can be held | No | the ceiling on E-, M-, O-level modeling |

### 7.3 Requisite capacity

If agent $A$ is to model agent $B$ well enough to predict $B$'s behavior or regulate its own behavior with respect to $B$, then under A9:

$$
C(A)\ \ge\ C_{\rm eff}(B\mid\text{task})
$$

where $C(A)$ is the capacity of the modeling system and $C_{\rm eff}(B\mid\text{task})$ is the effective complexity of the part of $B$ that matters for the task. Two consequences:

- Modeling the internal structure of another agent needs more capacity than predicting its coarse behavior, and more still than reacting to it.
- A larger system is not therefore a better modeler: capacity is necessary, not sufficient. Alignment of the two systems' codes (§8.3–8.3a) can matter as much as capacity.

### 7.4 Reflection: how the pieces fit

Integration, persistence, autonomy, and the closed informed loop (D12) answer *whether* a subsystem is an agent. The depth of the models it holds (E, M, O) answers *how developed* an agent it is. Capacity, attractor dimension, and complexity bound how far along that second axis a system can go. They do not move it along the first.

### 7.5 Invariance under reparameterization

The idealized measures of integration, autonomy, informedness, loop closure, use, and recoverability are intended to be invariant under the classes of transformations that leave the relevant relational or dynamical structure unchanged (smooth invertible reparameterizations / diffeomorphisms of the state space, and, for recoverability, transformations that leave behavioral equivalence classes intact).

For Axis A and Axis B (§10), concrete estimators differ sharply in their invariance properties:
- **Linear covariance estimators**, such as the participation-ratio dimension $PR = (\mathrm{tr}\,C)^2/\mathrm{tr}(C^2)$ of preactivations or firing rates, measure the dimension of the linear subspace spanned by the activity (PCA) and **depend on the choice of coordinates**. Moreover, by *linear equivalence* (Clark, 2026; Shen and Hu, 2025), the stationary covariance spectrum of a nonlinear chaotic network can coincide exactly with that of a stable linear network driven by noise ($\lambda_1<0$), making $PR$ blind to whether the underlying relief is chaotic or stable.
- **Tangent-space Lyapunov estimators** — the Lyapunov spectrum $\{\lambda_i\}$, the cumulative distribution $F(s)$, the Kaplan–Yorke attractor dimension $D_{\rm KY}$, and the Kolmogorov–Sinai entropy rate $h_{\rm KS}$ — are **strictly invariant under smooth coordinate transformations (diffeomorphisms)** of the phase space. They capture intrinsic properties of the dynamics on the relief $R$. Comparing $PR$ (linear embedding dimension) against $D_{\rm KY}$ (intrinsic attractor dimension) measures how nonlinearly the attractor is folded inside the ambient space.

---

## 8. Channel, Synchronization Kernel Inclusion, and Recoverability

### 8.1 Statement

Two agents $A$ and $B$ each hold a high-dimensional latent. They exchange information through a physical channel (or boundary $B_{AB}$) that is low-dimensional and has finite capacity. $A$ unfolds an incoming message into its own latent. $B$ folds a part of its latent into the message. Then they swap roles. The question is how much of the structure of $A$ can be recovered by $B$, and from what that depends.

### 8.2 Setup and definitions

Let $Z_A$, $Z_B$ be the latents. $A$ emits signals $X^n$ over $n$ uses of a channel with capacity $C$ per use. $B$ receives $Y^n$ and builds an estimate $\hat{Z}_A$ of $A$'s structure, using also its own latent $Z_B$ (its prior, its code).

**D18. Recoverability $\mathrm{Rec}(A\!\to\!B)$.** How well $B$'s model of $A$ predicts $A$'s behavior on interventions that were not used in building the model, normalized against a baseline model that sees only the channel statistics. Where internal states of both are accessible (models), relational similarity of $\hat{Z}_A$ to $Z_A$ (CKA/RSA) and dynamical similarity (alignment of Lyapunov spectra or Dynamical Similarity Analysis) are secondary measures.

### 8.3 A formal information-theoretic bound

Assume the Markov structure $Z_A\to X^n\to Y^n$, memoryless channel, noise independent of both latents, and $\hat{Z}_A=f(Y^n,Z_B)$. Then:

$$
I(Z_A;\hat{Z}_A)\ \le\ I(Z_A;Z_B)+nC
$$

The first term is the **shared prior**: information about $A$ that $B$ already has, because the two share training data, architecture, or culture. The second term is **what the channel carries**. Feedback or interaction does not raise $nC$ for a memoryless channel. What interaction can do is to spend the same bits on more informative content, by letting $B$ choose what to ask.

### 8.3a Linear-Gaussian boundary limit: the synchronization map and kernel inclusion

In the local stationary Gaussian regime (or Laplace approximation around an attractor mode, D2a) where external states $\eta$ (for example, the relevant subspace of $Z_A$), interface states $b$, and internal states $\mu$ (of $Z_B$) have joint covariance $\Sigma = \Pi^{-1}$ with Markov blanket $\Pi_{\eta\mu}=0$, the conditional expectations given a boundary state $b\in B$ are $\boldsymbol{\eta}(b) = \mathbb{E}[\eta\mid b] = \Sigma_{\eta b}\Sigma_b^{-1}b$ and $\boldsymbol{\mu}(b) = \mathbb{E}[\mu\mid b] = \Sigma_{\mu b}\Sigma_b^{-1}b$.

A well-defined **synchronization map** $\sigma: \mathrm{Im}(\boldsymbol{\mu}) \to \mathrm{Im}(\boldsymbol{\eta})$ satisfying $\sigma(\boldsymbol{\mu}(b)) = \boldsymbol{\eta}(b)$ for all $b\in B$ exists if and only if every boundary distinction that is compressed into the kernel of the internal projection also lies in the kernel of the external projection (Da Costa et al., 2021, Lemma 2.3):

$$
\exists\,\sigma:\ \sigma(\boldsymbol{\mu}(b))=\boldsymbol{\eta}(b)\quad\Longleftrightarrow\quad \ker\Sigma_{\mu b}\subset\ker\Sigma_{\eta b}\quad\Longleftrightarrow\quad \ker\Pi_{\mu b}\subset\ker\Pi_{\eta b}.
$$

When this holds, the map is given explicitly via the Moore–Penrose pseudoinverse by $\sigma(\mu) = \Sigma_{\eta b}\Sigma_{\mu b}^{-}\mu = \Pi_\eta^{-1}\Pi_{\eta b}\Pi_{\mu b}^{-}\Pi_\mu\mu$, and the expected internal state minimizes the precision-weighted prediction error:

$$
\boldsymbol{\mu}(b_t) = \arg\min_{\mu}\, D_{\mathrm{KL}}\bigl[q_\mu(\eta)\,\big\|\,p(\eta\mid b_t)\bigr] = \arg\min_{\mu}\,\frac{1}{2}\bigl(\sigma(\mu)-\boldsymbol{\eta}(b_t)\bigr)^{\top}\Pi_\eta\bigl(\sigma(\mu)-\boldsymbol{\eta}(b_t)\bigr).
$$

**Connection to the archive's kernel-path quotient:** This equivalence is the exact linear-Gaussian boundary counterpart of the cross-scale kernel-inclusion condition $\ker d\pi_{\mathrm{int}} \subseteq \ker d\pi_{\mathrm{ext}}$ (*Algorithm*, §9; *Spectral Realization of V4*, Proposition 2.1). If $\ker \Pi_{\mu b} \not\subset \ker \Pi_{\eta b}$, boundary variations that distinguish external states are collapsed into the kernel of the receiver's interface projection ($\mathrm{OMIT}$ from the receiver's perspective), making the representation degenerate regardless of how long the channel is observed ($nC \to \infty$).

### 8.4 What recoverability depends on

| Factor | Direction of effect | Comment |
| ------ | ------------------- | ------- |
| Channel capacity and number of uses $nC$ | more is better, up to the bound | the hard information-theoretic limit (§8.3) |
| Shared prior $I(Z_A;Z_B)$ | more is better | shared training data and architecture reduce what has to be transmitted |
| Kernel inclusion at the interface ($\ker\Pi_{\mu b}\subset\ker\Pi_{\eta b}$) and alignment of codes | violation causes permanent degeneracy | if the receiver's boundary projection collapses directions that vary in the sender, recovery saturates strictly below the capacity bound (§8.3a) |
| Identifiability | limits what can be recovered | many internal structures give the same behavior; only the equivalence class $[Z_A]$ is recoverable from behavior |
| Compressibility, attractor dimension, and generalized motion order of $A$ | lower $D_{\rm KY}$, $h_{\rm KS}$, and truncation order $n(\tau_w)$ are cheaper to recover | extensive chaos ($D_{\rm KY}\propto N$), high entropy rate, or high-order nonlinear integrator chains (§4.4) increase $C_{\rm eff}(A)$ |
| Capacity of $B$ | $C(B)\ge C_{\rm eff}(A)$ is required (A9) | otherwise recovery saturates below the bound |
| Ability of $B$ to intervene | interactive beats passive | $B$ can choose informative queries |
| Stationarity of $A$ | a changing $A$ is a moving target | plasticity $\Pi_{\mathrm{plast},A}$ shortens the useful life of $\hat{Z}_A$ |
| Noise | degrades the usable $C$ | enters through $C$ |

### 8.4a Channel classification (working)

Channels may be classified by three independent axes:

- write target (activations / context only versus persistent store inside the receiver's declared boundary);
- mediation (whether the signal is interpreted through the receiver's existing models $M$ or $O$);
- medium (the physical or symbolic carrier).

Under idealized conditions these axes can be separated by shielding or ablation. The classification is a working hypothesis (UNDECIDED) and is not required for the recoverability bound.

### 8.5 What is recoverable

What can be recovered is not the weights or the raw coordinates. It is the relational geometry and diffeomorphism-invariant dynamical structure of $A$'s latent and the behavior it generates, up to the equivalence class of transformations that leave behavior unchanged (rotations of coordinates, smooth reparameterizations). This is why relational comparison and invariant spectra (A7, §7.5) are the right instruments.

### 8.6 The shared thing is a protocol, not a dimension

Two agents interacting need a common causal structure in which signals pass. They do not share a latent, a dimension, or a code. What they share is the protocol: an agreed mapping between signals and internal states, produced by common training or by common history. The channel is low-dimensional. Each side's latent is high-dimensional and local. Without a common substrate the two would not interact at all. With one, the extent to which they understand each other is a matter of §8.3–8.4. (The precondition of a shared causal order is stated once in §3.1.)

### 8.7 Memory and modeling of others are one mechanism

Memory of one's own past and a model of another agent are both models written back into $R$ (C2, evaluated for the declared boundary, D14a) at limited resolution $\nu$. They differ in the target, not in the mechanism. Three consequences:

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

**T2. Depth comes from stake, and return is accelerated by solenoidal circulation.**  
Physical attractors are deep (strong transverse contraction in $E^s$, high escape threshold $D(U)$) because of genetic priors, homeostatic constraints, and threat to the carrier, while the skew-symmetric solenoidal component $Q(z)$ of the relief flow accelerates relaxation back to the homeostatic set-point at the cost of damped oscillatory transients (D5a). S regions are flatter because errors there cost the carrier less.  
*Status:* FOLLOW (mathematical acceleration property of $Q\neq 0$ for stationary diffusions, D5a); UNDECIDED (A5 and the empirical dependence on stake, tested by P3 and P10).

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
Reasoning chains and meta-descriptions in an LLM are real, so C1 is present in a limited form. Weights do not change in deployment. Context changes activations, not the relief. So for the boundary "the model weights" the recursion is not written back and C2 is absent. For a declared boundary that includes a scaffold with persistent memory, C2 is evaluated by D14a and can hold (§11). This is a missing candidate condition for the weights-only system. It is not proof that there is no experience.  
*Status:* FOLLOW (description); UNDECIDED (what follows for experience).

**T7. Candidate conditions.**  
The working position of the author: agency together with C1 and C2 is the most likely sufficient condition for consciousness-like organization (continuous-self grade, §6.2), and C3 adds depth. This is not claimed as shown. Three alternatives are rejected:
- C2 alone is sufficient. Rejected: it would count every online-learning system without a self-model.
- C2 is necessary for momentary experience. Rejected: people with severe anterograde amnesia do not consolidate new experience and are still conscious in the moment. C2 is needed for a continuous self, not for the moment.
- Presence of Q-structures is sufficient. Rejected: every trained system has them (D6).

*Status:* UNDECIDED (the working position and C3); NULL (the three rejected claims).

**T8. Agency is graded and defined by integration, persistence, autonomy, and a closed informed loop — not by degrees of freedom, chaos, or a passive Markov blanket.**  
Not by degrees of freedom, not by complexity, not by extensive chaos ($D_{\rm KY}, h_{\rm KS}$), not by autonomy alone, and not by the mere existence of a stationary Markov blanket with a synchronization map $\sigma(\boldsymbol{\mu}(b))=\boldsymbol{\eta}(b)$. A gas cloud has many degrees of freedom and holds no information about an environment. Noise has maximal description length and no organization. A closed oscillator or an untrained chaotic network ($g>1$) has maximal autonomy and positive entropy production, and no informed loop. A passive linear Ornstein–Uhlenbeck system with $\Pi_{\eta\mu}=0$ and $\ker\Pi_{\mu b}\subset\ker\Pi_{\eta b}$ satisfies stationary "Bayesian mechanics" (Da Costa et al., 2021), yet without interventional loop closure $\mathrm{Cl}>\theta_{\mathrm{Cl}}$ and stake-grounded relevance $U>\theta_U$ it is a passive filter, not an intrinsic agent.  
*Status:* FOLLOW (exclusion of the gas cloud, random chaotic RNN, and passive sensory-only OU blanket under D12); UNDECIDED (the choice of empirical measures and thresholds; tested by P6).

**T9. Unity of a latent is a threshold property of a subsystem.**  
It is not a property of the substrate and not a postulate about humans. It is measured by $I(A)$ with persistence. The distinction between a human and a model is then made by measured integration, autonomy, and the conditions C1–C3, not by a stipulated single manifold.  
*Status:* UNDECIDED (A3; tested by P2).

**T10. Recoverability is bounded by prior plus capacity and gated by boundary kernel inclusion.**  
How much of $A$'s structure $B$ can recover is bounded by the shared prior plus the channel's capacity (§8.3), requires $\ker\Pi_{\mu b}\subset\ker\Pi_{\eta b}$ in the linear-Gaussian boundary limit to avoid representational degeneracy (§8.3a), and falls short of the bound by the factors in §8.4. It is a property of the pair $(A,B)$ and the channel, not of $A$ alone.  
*Status:* FOLLOW (both mathematical results under their stated assumptions); UNDECIDED (the empirical effect of each factor; P7, P8).

**T11. Modeling another agent needs matching capacity across active orders of motion.**  
Modeling the internal structure of another requires capacity not smaller than the effective complexity of the relevant part of the other, including the untruncated orders of generalized motion $\tilde{s}_t^{(0,\dots,n)}$ active at the window $\tau_w$ (A9, §4.4).  
*Status:* UNDECIDED (A9; tested by P8).

**T12. Memory and modeling of others are one mechanism.**  
Both are write-back of a model into the relief at limited resolution.  
*Status:* UNDECIDED (depends on C2 being the actual mechanism in each system).

**T13. Coupling is directed and requires recovery beyond the prior plus use.**  
$\mathrm{Coup}(A\!\to\!B)$ is not symmetric and is not implied by the mere existence of a channel.  
*Status:* FOLLOW (definition D15a); UNDECIDED (empirical separability of channel classes).

---

## 10. Four Axes of Difference

Systems are compared along four axes.

**D19. Effective dimension profile $d(\varepsilon)$ and invariant attractor dimension $D_{\rm KY}$.** The number of independent directions actually used at spatial scale $\varepsilon$ is a function of scale, not one number.
- *Scale-dependent geometric estimators:* local slope of the correlation integral $d(r)=d\log C(r)/d\log r$, nearest-neighbour intrinsic dimension (TwoNN), and participation ratio $PR=(\mathrm{tr}\,C)^2/\mathrm{tr}(C^2)$ of covariance matrices. Because $PR$ measures the dimension of the linear subspace explored by the activity, it is coordinate-dependent and subject to linear equivalence (§7.5).
- *Diffeomorphism-invariant dynamical estimators:* the Kaplan–Yorke attractor dimension $D_{\rm KY}$ and the Kolmogorov–Sinai entropy rate $h_{\rm KS}$, derived from the Lyapunov spectrum $\lambda_1\ge\dots\ge\lambda_N$ (or its cumulative density $F'(s)$ at large $N$):

$$
D_{\rm KY}=j+\frac{\sum_{i=1}^j \lambda_i}{|\lambda_{j+1}|}\quad\Longleftrightarrow\quad \frac{D_{\rm KY}}{N}=1-F(s_{\rm KY})\ \text{ with }\ \int_{s_{\rm KY}}^{\infty}s\,F'(s)\,ds=0
$$

$$
\frac{h_{\rm KS}}{N}=\int_0^{\infty}s\,F'(s)\,ds
$$

While $PR/N$ can grow monotonically with coupling strength, $D_{\rm KY}/N$ captures the true low-dimensional saturation (and eventual contraction at strong coupling) of the nonlinear attractor relative to the ambient phase space (Clark, 2026; Engelken et al., 2023). Both $d(\varepsilon)$ (across spatial scales $r$) and the pair $(D_{\rm KY}, PR)$ (intrinsic vs linear embedding dimension) are reported on Axis A.

| Axis | What differs | How to measure |
| ---- | ------------ | -------------- |
| **A. Dimension profile $d(\varepsilon)$ and $(D_{\rm KY}, PR)$** | how many directions are used at each scale; intrinsic attractor dimension vs linear embedding dimension | correlation dimension $d(r)$, TwoNN, participation ratio $PR$, and Lyapunov spectrum $\to D_{\rm KY}, h_{\rm KS}$ via tangent-space QR or minimum-norm response $F(s)$ |
| **B. Depth $D$, contraction $F(s<0)$, and solenoidal ratio $\|Q\|/\|\Gamma\|$** | cost of leaving a region, transverse stiffness, and circulatory acceleration of return | finite perturbation of activations and time to return $\tau_{\mathrm{ret}}$; local Lyapunov spectrum in $E^s$ ($\kappa(U)=-\int_{-\infty}^0 s F'(s)ds$ via dichotomy projector $R^{vv}$); ratio of skew-symmetric to symmetric generator norms $\|Q\|/\|\Gamma\|$ (D5a); Fisher spectrum as secondary weight proxy |
| **C. Plasticity $\Pi_{\mathrm{plast}}$** | how experience rebuilds $R$ | weight or persistent-store change per unit of experience, time scales |
| **D. Autonomy and loop profile $\mathcal{A}(\tau_w)$, $\mathrm{Cl}(\tau_w)$, $U(\tau_w)$** | share of the future set by own structure, by time window; whether the system acts on its own input; whether it depends on the information it holds | standardized interventions on internal state (resolved along $E^u$ vs $E^s$), on output, and on environment input; surrogate decoupling; at several windows |

The axes are not independent. Depth depends on stake and on training history, so partly on $\Pi_{\mathrm{plast}}$. Autonomy depends on what is fixed in $R$ over the window, so on $\Pi_{\mathrm{plast}}$ and the window. For measurement they are treated separately. In conclusions the dependence is kept in mind.

Structural attributes that determine the axes: a P-layer, a self-model $M$, an other-model $O$, and stake.

The profile $d(\varepsilon)$ is where this document touches the archive's coarse-graining: directions that are invisible at a coarse scale lie, for that description, in the kernel of the map (*Algorithm*, §9). The correspondence is a homology, not an identity. The autonomy profile $\mathcal{A}(\tau_w)$ and the truncation of the generalized-motion integrator chain at order $n(\tau_w)$ (§4.4) are the analogous constructions along the time axis.

---

## 11. Comparison: LLM, World Model, Human

| Parameter | LLM (deployed) | World model (pure) | Human |
| --------- | -------------- | ------------------ | ----- |
| Composition of $Z$ | almost all S; physics only through text | almost all P; S weak or absent | P and S coupled in one subsystem |
| Integration of P and S | none (no P) | none (no S) | expected high (to be measured, P2) |
| Profile $d(\varepsilon)$ and $(D_{\rm KY}, PR)$ | measurable; high $PR$ in S; transient $\lambda_1>0$ in looped reasoning | measurable | not measurable directly; expected richer because of P (hypothesis) |
| Depth $D$ and solenoidal return | small; training loss has pits, but no stake | small (no stake); solenoidal flow reflects modelled physical dynamics | large in P (stake), rapid oscillatory homeostatic recovery ($Q\neq 0$), moderate in S |
| Plasticity $\Pi_{\mathrm{plast}}$ | present in training; about zero in deployment | offline: about zero; online agents: above zero | above zero on several time scales |
| Autonomy $\mathcal{A}(\tau_w)$ | moderate in a single call, window-dependent | depends on the agent loop | high on most windows |
| Closed informed loop (Inf, Cl, $U$) | Inf high in S; Cl about 0 in one call, above 0 on longer windows through an interlocutor or tools; $U$ relative to an external task | Inf high in P; Cl depends on the agent loop; $U$ relative to an external task | all high; $U$ relative to its own viability |
| Reasoning budget $\rho$ | spread inside S | almost all spent on P | hard competition between P and S |
| Self-model $M$ (C1) | limited, functional, reliability disputed | usually none (agents may model their own body) | rich |
| Other-model $O$ | present functionally, depth disputed | usually none | rich |
| Write-back (C2, D14a) | none for the boundary "weights"; for a scaffold boundary see below | usually none | yes |
| Stake (C3) | none | none | yes (ontological) |
| Q-structures in S | yes (structural sense, D6) | none or weak | yes |
| Q-structures in P | none | yes, shallow | yes, deep |
| Measurability | high (access to activations and Jacobians) | high | low, indirect |

Entries about structure are descriptive. Entries about geometry and autonomy in the human column, and about profiles, are predictions (UNDECIDED).

### Intermediate cases

- **Multimodal models and embodied agents** have both layers but no stake. They are the main test of integration across layers (P2).
- **An LLM agent with external memory or continual fine-tuning** has C2 or not according to D14a, evaluated for the declared boundary. For the boundary "weights only", C2 is absent unless fine-tuning is driven by the system's own operation inside the boundary. For the boundary "model plus scaffold plus persistent memory", C2 is present when the write is made by the system's own operation, survives a window boundary, and conditions the later trajectory. The same system is C2-absent for one boundary and C2-present for the other. This is intended (A1, A2, §15.15). On long windows the loop quantities also rise ($\mathrm{Cl}>0$ through tools and interlocutors).
- **The verifier-centered agent of the archive (Unified Implementable Model v2.0)** has an object-centric latent world model (P-like) and an optional semantic proposer (S-like). The two are coupled through explicit grounding maps and an authority hierarchy, by design, not through one continuous manifold. Unlike a purely continuous variational-free-energy agent (Da Costa et al., 2021) where prediction errors only drive smooth gradient flows, UIM v2.0 separates proposition from external four-valued certification (`FOLLOW`, `OMIT`, `UNDECIDED`, `NULL`) so that a certified contradiction (`NULL`) immediately halts state commitment rather than being absorbed as a continuous shift. There is no ontological stake. Memory is event-sourced and lives in an event store, not in weights. Under D14a it has write-back (C2) only if the event store lies inside the declared boundary and its entries are produced by the system's own operation and condition later trajectories. For the weights-only boundary it has none. *Status:* UNDECIDED.

---

## 12. Relation to the Archive

This is a homology of forms, not an identity. This document is not a part of the other documents, and they do not depend on it.

| Archive concept | Where | Counterpart here | Relation |
| --------------- | ----- | ---------------- | -------- |
| Consciousness as recursive semantic self-correction under external verification | *Algorithm* §10; *Framework* §4.2 | C1 (self-model) and C2 (write-back of corrections) on top of agency | The first parts are restated at the latent level. External verification prevents variational free-energy minimization from degenerating into self-confirmation. P-layer plus stake is one concrete channel through which the world penalizes errors. |
| The hard problem is bracketed | *Algorithm* §10.3 | The boundary in §14 | Same stance. |
| Substrate as constraint envelope; substrate-parameterization | *Algorithm* §11; *Framework* §4.4 | A1; §3.4; the P-layer; stake | The body enters as envelope parameters. The archive's UNDECIDED on necessary envelope thresholds applies equally to C3. |
| Irrelevance as the kernel of coarse-graining | *Algorithm* §9; *Framework* §4.3; *Spectral Realization of V4* §1–2 | Profile $d(\varepsilon)$; dichotomy projector $P_s$ onto decaying tangent directions $E^s$; truncation of high-order motion $s^{(k)}$ for $k>n(\tau_w)$ (§4.4); boundary kernel inclusion $\ker\Pi_{\mu b}\subset\ker\Pi_{\eta b}$ (§8.3a) | Homology through scale-indexing, decay of uninformative directions, and kernel inclusion across interfaces. |
| Compression is thermodynamically mandatory | *Algorithm* §9.4; *CPP v3.9* §4.2 | Bounded reasoning budget (T3); finite channel capacity (§8); transverse contraction $\kappa(U)$ | T3 and §8 inherit the bound; maintaining transverse contraction $\kappa(U)$ across $E^s$ against noise requires continuous entropy export across the boundary. |
| Grounding is a history of certified transitions; a prediction is not a fact | *Algorithm* §10.2; *UIM* §2.3, §17 | Write-back (C2); stored models of others (D16) | This document does not say what may be written back. The archive supplies a candidate rule: only externally certified corrections, otherwise recursion degenerates into self-confirmation. Not adopted. The same issue applies to a model of another agent: a stored model that is never checked against the other drifts. *Status:* UNDECIDED. |
| Geometric theory of latent representations; experimental track E1–E5 | *Framework* §5.6, §8.2; *VIM v1.0* | Effective-dimension, Lyapunov-spectrum ($D_{\rm KY}, h_{\rm KS}$), Helmholtz decomposition, and autonomy measurements (§13) | May share models and tooling. Compatibility of the two geometric descriptions is not examined. *Status:* UNDECIDED. |
| Ternary standard FOLLOW / OMIT / NULL / UNDECIDED | *Algorithm* §15; *Framework* §5.4, §7; canonical: *Modified Brusentsov Entailment Logic* §4 (`Reasoning/Modified_Brusentsov_Entailment_Logic.md`) | Statuses in §16 | Used as is. |

---

## 13. Experimental Program

### 13.1 Statement

The program measures geometry, tangent-space Lyapunov spectra, Helmholtz dissipative/solenoidal ratios, autonomy, recoverability, and directed coupling. It does not measure experience. All predictions below are untested at the date of this document.

### 13.2 Method for the geometry, tangent-space, and Helmholtz predictions

1. Take an open trained model (including recurrent, state-space, or looped-transformer architectures) and a set of inputs. Record activations of chosen layers and state-transition Jacobians $M(n)=\partial z(n+1)/\partial z(n)$.
2. Compute the spatial profile $d(\varepsilon)$ with independent estimators (correlation dimension, TwoNN, participation ratio $PR$) and the dynamical spectrum $F(s)$ (via QR reorthonormalization or the regularized minimum-norm response $\mathrm{tr}\,R^{vv}_\eta(k+1,k)/N$), extracting $D_{\rm KY}$, $h_{\rm KS}$, and the contraction rate $\kappa(U)$ in $E^s$.
3. Decompose the local drift or linearized transition generator into symmetric (dissipative, $\Gamma$) and skew-symmetric (solenoidal, $Q$) components (D5a); measure the solenoidal-to-dissipative ratio $\|Q\|_F/\|\Gamma\|_F$, the return time $\tau_{\mathrm{ret}}(U)$, and the oscillation amplitude of the loss/energy along perturbed relaxation trajectories.
4. Compare $PR$ against $D_{\rm KY}$ to separate linear embedding dimension from diffeomorphism-invariant attractor dimension, and look for plateaus and steps in $d(\varepsilon)$.

**Controls** (without them a result cannot be read):
- an untrained model of the same architecture, including random recurrent networks across the chaos transition ($g<1$ vs $g>1$, calibrated against exact single-site cavity solutions for $F(s)$, $D_{\rm KY}/N$, and $PR/N$);
- a linear network with matched covariance spectrum (linear-equivalence control: matches $PR$, but has $\lambda_1<0$ and no chaotic attractor);
- a purely symmetric gradient-flow control ($Q = 0$ with matched stationary covariance $\Sigma = \Pi^{-1}$);
- shuffled data or noise input;
- several sample sizes and estimators. If estimators of the same class disagree, no conclusion yet.

### 13.3 Method for autonomy and the loop

1. Choose systems with known internal structure: simulated physical systems (a gas cloud analogue, a thermostat), RL agents, a frozen LLM, an LLM with an agent loop. Add the three negative controls the loop is meant to exclude: (i) closed autonomous oscillators (a limit cycle, a chaotic oscillator), (ii) an untrained chaotic rate network ($g>1$ in the Sompolinsky model, where $D_{\rm KY}/N>0$ and $h_{\rm KS}/N>0$ are known analytically), and (iii) a passive stationary linear Ornstein–Uhlenbeck system with a Markov blanket ($\Pi_{\eta\mu}=0$, $\ker\Pi_{\mu b}\subset\ker\Pi_{\eta b}$) and a trained passive classifier.
2. For each, perform standardized interventions on the internal state (both isotropic and projected onto the active subspace $E^u$ vs the contracting subspace $E^s$) and on the environment input at time $t$, and measure the change in the internal state at $t+\tau$. Compute $\mathcal{A}^{\rm do}$ at several windows.
3. Perform standardized interventions on the system's output and on environment sources not mediated by it, and measure the change of the input at $t+\tau$. Compute $\mathrm{Cl}$.
4. Compute $\mathrm{Inf}$: error of a held-out probe or forward model on $Z_A$, against the same estimator with randomized $R$.
5. Compute $U$: choose $Q$ ($v$ where a viability variable exists, an external score otherwise), decouple by a surrogate (time-shuffled relevant input, or $R$ from an independent instance of the environment), and measure the drop.
6. Compare with $\mathcal{A}^{\rm pred}$ where interventions are not available.
7. Controls: a system with randomized relief (should give near-zero $\mathrm{Inf}$ and $U$ even when $h_{\rm KS}>0$ and $\mathcal{A}^{\rm do}\approx 1$), a passive sensory-coupled OU blanket (gives $\mathrm{Inf}>0$ via $\sigma(\boldsymbol{\mu}(b))=\boldsymbol{\eta}(b)$, but $\mathrm{Cl}=0$ and no stake-grounded $U$), a system with the environment input shuffled in time, several estimators of $\mathrm{Dep}$, several $\varphi_A$, several surrogate choices for $U$.

**Write-back check (D14a).** For a system with a persistent store inside the declared boundary: (i) intervene on the system's processing in window $k$ (for example replace the output of the self-model step) and test whether $R_{k+1}$ changes; (ii) check that the difference survives a window boundary; (iii) restore $R_k$ in the changed region and test whether the trajectory in window $k+1$ changes. All three must hold. Otherwise C2 is absent for that boundary.

### 13.4 Method for recoverability and coupling

1. Take pairs of models $(A,B)$ connected by an explicit bottleneck channel of controllable capacity and noise.
2. Vary: capacity $nC$, shared prior (same data and architecture vs different), boundary projection rank (satisfying vs violating $\ker\Pi_{\mu b}\subset\ker\Pi_{\eta b}$, §8.3a), capacity of $B$, attractor dimension $D_{\rm KY}$, entropy rate $h_{\rm KS}$, and integrator-chain order $n$ of $A$ (§4.4), passive vs interactive access, stationarity of $A$.
3. Measure $\mathrm{Rec}(A\!\to\!B)$ on held-out interventions and the CKA/RSA and dynamical similarity of $\hat{Z}_A$ to $Z_A$.
4. Test $\mathrm{Coup}(A\!\to\!B)$ by checking whether recovered structure beyond the prior changes $B$'s subsequent trajectory or its persistent store.
5. Controls: $B$ with no access to the channel (baseline), $B$ receiving shuffled channel output, $B$ with a rank-deficient sensory projection where $\ker\Pi_{\mu b}\not\subset\ker\Pi_{\eta b}$, and $A$ replaced by a behaviorally equivalent but internally reparameterized system (tests diffeomorphism invariance and identifiability).

### 13.5 Predictions

| ID | Prediction | Refuted if |
| -- | ---------- | ---------- |
| P1 | Similarity between LLM representations and human brain responses (RSA on neural data) is higher for abstract concepts and lower for bodily and interoceptive ones. | No difference, or the reverse, after controlling for word frequency and concreteness. |
| P2 | Integration across layers: in multimodal and embodied models the P and S subspaces are more strongly linked (CKA, linear predictability, $I(A)$) than in separately trained models, and integration crosses a measurable threshold for the whole-system case. | The link is the same. Note: convergence of representations across models and modalities would also give this result. The distinguishing version is P3. |
| P3 | An RL agent in simulation with a viability variable (simulated stake) has deeper pits in the linked regions than the same agent without it: larger escape threshold $D(U)$, longer persistence, and stronger transverse contraction $\kappa(U)$ in the negative Lyapunov spectrum $F(s<0)$. | No difference in $D(U)$ or $F(s<0)$ compared with a standard dense-reward baseline of matched episode length. |
| P4 | The spatial profile $d(\varepsilon)$ and the invariant pair $(D_{\rm KY}/N, PR/N)$ differ between an LLM, a world model, and an embodied model, and $D_{\rm KY}$ separates nonlinear attractors from covariance-matched linear controls where $PR$ does not. | The profiles and $(D_{\rm KY}, PR)$ ratios cannot be told apart. |
| P5 | Across training checkpoints of one model (for example, a public checkpoint family) coarse-scale structure forms before fine-scale structure, and random chaotic directions ($\lambda_i>0$ with $\mathrm{Inf}\approx 0$) are suppressed or aligned into lower-dimensional task attractors ($D_{\rm KY}$ compresses relative to initialization). | The order is reversed or random. The link to this framework is indirect (axis C). |
| P6 | Agency separates systems that degrees of freedom, attractor dimension $D_{\rm KY}$, entropy rate $h_{\rm KS}$, description length, and passive stationary Markov-blanket synchronization ($\sigma(\boldsymbol{\mu}(b))=\boldsymbol{\eta}(b)$) do not. With $\mathrm{Inf}$, $\mathrm{Cl}$, $U$, and $\mathcal{A}^{\rm do}$ measured on the systems of §13.3: a gas-cloud analogue is near zero on the loop quantities (no $R$); closed oscillators and untrained chaotic RNNs ($g>1$) have high $\mathcal{A}^{\rm do}$ (and high $D_{\rm KY}, h_{\rm KS}$) but near-zero $\mathrm{Inf}$ and $\mathrm{Cl}$; a passive sensory-coupled OU blanket and a trained passive classifier have high $\mathrm{Inf}$ (accurate $\sigma$) but near-zero $\mathrm{Cl}$ (and no intrinsic stake); RL agents and agentic LLM systems on long windows are above the others on all of $\mathcal{A}^{\rm do}$, $\mathrm{Inf}$, $\mathrm{Cl}$, $U$. | The classification by D12 does not differ from the ordering by $N$, $D_{\rm KY}$, $h_{\rm KS}$, description length, or stationary free-energy minimization; or a closed oscillator, chaotic random RNN, passive OU blanket, or passive classifier passes D12 at thresholds that also admit the RL agents; or the classification is not stable across estimators, $\varphi_A$, and surrogate choices. |
| P7 | Recoverability grows with channel capacity and with shared prior, saturates below the bound of §8.3, collapses on the directions where $\ker\Pi_{\mu b}\not\subset\ker\Pi_{\eta b}$ (§8.3a), and is higher for interactive than for passive access at equal capacity. | Recoverability does not respond to these factors, fails to drop when $\ker\Pi_{\mu b}\not\subset\ker\Pi_{\eta b}$, or exceeds the bound in a setup where its assumptions hold. |
| P8 | A threshold in the capacity of $B$ exists: below $C_{\rm eff}$ (tracked by $D_{\rm KY}$, $h_{\rm KS}$, and the active integrator-chain order $n(\tau_w)$ of the task-relevant subspace of $A$), recoverability saturates at a low level whatever the channel capacity. | Recoverability continues to grow past the capacity of $B$ with no threshold. |
| P9 | Adding a viability variable (stake) to an RL agent raises its autonomy $\mathcal{A}^{\rm do}$ along active manifold directions ($E^u$) at long windows compared with the same agent without it, because relevance of information becomes defined by $v$. $\mathrm{Inf}$ and $\mathrm{Cl}$ are matched between the two designs. | No change in autonomy, or a change explained by the training procedure alone. |
| P10 | In recurrent or continuous-time latent models with a fixed attractor relief $R$, increasing the solenoidal-to-dissipative flow ratio $\|Q\|_F/\|\Gamma\|_F$ (at fixed stationary covariance $\Sigma = \Pi^{-1}$ and fixed transverse Lyapunov sum $\kappa(U)$) decreases the return time $\tau_{\mathrm{ret}}(U)$ after a boundary perturbation while inducing non-monotonic damped oscillations in the instantaneous prediction error / free energy along the recovery trajectory (D5a). | Return time $\tau_{\mathrm{ret}}(U)$ is minimized at $Q=0$, or no oscillatory transient appears when $\|Q\|_F \gg \|\Gamma\|_F$. |

### 13.6 Priority

P4, P5, and P10 are the cheapest: open models, public checkpoints, and exact analytical baselines from random network theory and Ornstein–Uhlenbeck diffusions. P6 needs small simulated systems (including the Sompolinsky RNN control and the linear OU Markov-blanket control) and an intervention harness, so it is also cheap and the most direct test of the agency criterion. P7 and P8 need pairs of trained models with a controlled channel. P1 needs existing neuroimaging data. P2, P3, and P9 need training runs or simulation and cost more.

### 13.7 What is not tested

Experience. All measurements show differences in geometry, tangent-space spectra, Helmholtz flow ratios, autonomy, recoverability, and coupling. They do not show where something is "experienced from inside".

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

Every trained system has Q-structures. D6 gives a structural vocabulary, not a criterion for experience. The criterion is pushed onto agency, C1–C3, and the hard problem. A critic may fairly say D6 does little work, and that "learned attractor" would avoid philosophical friction. The term is kept here only to mark the structural slot where phenomenal content would attach if the hard problem were bridged.

### 15.2 The measure of integration is not chosen

$\mathrm{Dep}$ in D9 is a placeholder. Candidate measures (mutual information, transfer entropy, causal influence, measures from integrated-information approaches) may give different orderings, and some are not computable for large systems. Until a measure is chosen and its behavior on known cases is checked, A3 is only a replacement of a postulate by a parameter.

### 15.3 The choice of boundary and coarse-graining

A subsystem and its coarse-graining $\varphi_A$ are chosen by the observer. Different choices may give different integration, autonomy, and truncation order $n(\tau_w)$ of the generalized-motion chain (§4.4) for the same physical system. Without a canonical rule for the choice (for example, choosing $\varphi_A$ to maximize causal emergence or $I(A)\cdot\mathcal{A}(A)$), the results are conditional on the declared scale.

### 15.4 Autonomy depends on the time window

The line between internal and external is the time scale on which $R$ is treated as fixed. A system can be autonomous on one window and driven on another. This is reported as a profile and not resolved into a single value. It also means that "is a deployed LLM an agent" has no window-free answer.

### 15.5 What counts as internal

Every internal regularity entered the system from outside through learning. The framework fixes the boundary by time scale (what is already in $R$ is internal). It does not say whether that is the right boundary in every case, for example for fast adaptation inside a context window.

### 15.6 The reference for relevance and use, stationary free energy, and simulated vs ontological stake

Use (D11c) is defined relative to a reference quantity $Q$. Stake offers an intrinsic one (§5.3). Systems without stake have no such reference, and their use $U$, and with it their agency, is then defined only relative to a task or a loss function chosen from outside (including the quadratic precision cost $\frac{1}{2}[s,a,\mu]K[s,a,\mu]^\top$ of a stationary Gaussian Markov blanket). Furthermore, in simulation experiments (P3, P9), a programmed viability variable $v$ that terminates an episode is still a formal cousin of an external sparse terminal reward: it does not physically dissolve the hardware carrying $R$. Whether simulated stake reproduces the geometric effects of ontological stake is an empirical question tested by P3, not an equivalence guaranteed by A1.

### 15.7 Infinitesimal contraction versus finite basin depth

In D7 and A6, local stiffness is measured via the negative Lyapunov spectrum $F(s<0)$ of the state-space Jacobian $M(n)$, avoiding the mismatch between activation space $Z$ and weight space $\theta$ (Fisher spectrum). However, Lyapunov exponents are infinitesimal quantities. In systems exhibiting "stable chaos" (e.g., spiking networks or piecewise-nonlinear maps), trajectories can be stable to infinitesimal perturbations ($\lambda_1<0$) yet unstable to finite perturbations $D(U)$ above a small threshold. Thus both finite-perturbation escape $D(U)$ and tangent-space contraction $F(s<0)$ must be checked together.

### 15.8 Comparing a human and a model

Coordinates differ and human data are indirect. RSA and CKA compare relational geometry, but they see only what recordings allow. Full Lyapunov spectra and interventional autonomy for a human brain are largely unavailable at the required resolution. Axis A and Axis D for humans stay indirect predictions.

### 15.9 Competing explanations

Two rivals for the integration claims. First, biological naturalism: the claims about stake and body would then say something stronger than A1 allows. Second, convergence of representations across models and modalities: it predicts the P2 result without any stake. Only P3 and P9, where stake is manipulated, separate this framework from it. For recoverability, the same convergence also predicts a higher shared prior, so P7 must vary prior and capacity separately.

### 15.10 The bounds are only as good as their assumptions

The inequality in §8.3 needs a memoryless channel, noise independent of both latents, and the stated Markov structure. The kernel-inclusion equivalence in §8.3a holds exactly for joint Gaussian distributions (and locally under a Laplace approximation at a mode), whereas real agent latents are highly non-Gaussian and multimodal. Real exchanges between agents are not memoryless and the channel is shaped by the agents themselves. The bounds are ceilings and local conditions for idealized regimes, not exact estimates for real ones.

### 15.11 Requisite capacity is assumed

A9 is imported from regulation theory. Its conditions (a regulator facing a disturbance, a defined set of outcomes) may not hold for modeling an agent in general.

### 15.12 Falsifiability

Results that would damage the framework: (i) P3 and P9 show no effect of stake on depth $D(U)$, transverse contraction $F(s<0)$, or autonomy; (ii) P1 comes out reversed; (iii) P4 finds profiles $d(\varepsilon)$ and $(D_{\rm KY}, PR)$ that cannot be told apart; (iv) P6 shows that the classification by D12 tracks $N$, $D_{\rm KY}$, $h_{\rm KS}$, description length, or passive stationary free-energy minimization, or that a closed oscillator, an untrained chaotic RNN, a passive OU blanket, or a passive classifier passes it together with the RL agents; (v) P7 shows no response to prior, capacity, or boundary kernel inclusion; (vi) P10 shows that solenoidal flow $Q\neq 0$ fails to accelerate return or induce oscillatory transients in stationary diffusion settings. None of them would answer the hard problem. They would remove geometric, autonomy, or recoverability claims.

### 15.13 Engineering vocabulary

"Relief", "budget", and "traversal" come from machine learning and dynamical systems. Projecting engineering terms onto minds is a known failure mode, as the archive says (*Algorithm*, §14.4). The defense is the same: the claims that survive translation back into coordinate-invariant measurable quantities are the ones that count.

### 15.14 The loop conditions

The thresholds $\theta_{\rm Inf}$, $\theta_{\rm Cl}$, $\theta_U$ are not set, so the classification is conditional on them, like the other thresholds. $U$ depends on the choice of $Q$ and on the surrogate used for decoupling: a surrogate that leaves a dependence in place or destroys unrelated structure gives a wrong $U$. $\mathrm{Cl}$ depends on what is declared as environment: the same chat model has $\mathrm{Cl}\approx 0$ on the window of one call and $\mathrm{Cl}>0$ on the window of a conversation, because the interlocutor reacts to its output. The criterion admits a thermostat as a minimal task-relative agent. This is accepted: agency is graded, and capacity (§7) sets how far such a system can go.

### 15.15 Write-back depends on the declared boundary

C2 is a predicate of a subsystem and a window (D14a). The same physical system can be C2-absent for the boundary "the weights" and C2-present for the boundary "weights plus a scaffold with persistent memory". This follows from A1 and A2 (organization and the declared subsystem matter, not material) and is the intended behavior, not an ambiguity. The cost is the same as in §15.3: the boundary is chosen by the observer, and a result is conditional on it. C2 is not reported in this document without its boundary and window.

---

## 16. Self-Assessment Under the Ternary Standard

The archive's standard applies: FOLLOW (certified), OMIT (admissible but inessential), NULL (inadmissible), UNDECIDED (not enough certification). The standard is canonically fixed by *Modified Brusentsov Entailment Logic* (`Reasoning/Modified_Brusentsov_Entailment_Logic.md`, §4): verdict space V4, dominance chain NULL $\succ$ UNDECIDED $\succ$ OMIT $\succ$ FOLLOW, and the separation of the ontological triad from the epistemic signal UNDECIDED. Applied to the theses of this document, the standard is used at the thesis level (per *Framework* §7).

Rule used for derived claims. A claim gets FOLLOW only if it follows from the definitions alone, from a stated mathematical result under its assumptions, or describes an existing architecture. If it depends on an assumption, it gets UNDECIDED, with the dependency named. NULL marks claims rejected here. OMIT marks material kept for orientation.

| Claim of this document | Verdict | Basis |
| ---------------------- | ------- | ----- |
| Definitions D1–D19, D2a, D5a, D11a–D11c, D14a, and D15a are consistent, and D6 does not contain the felt aspect | FOLLOW (formal structure) | Stipulations; consistency checked in §3–§10 |
| Relief and reasoning budget are distinct quantities | FOLLOW | D5 versus D8; independent combinations (§4) |
| The reasoning budget is bounded for any physical system | FOLLOW | Constraint triad (*Algorithm* §3.2, §9.4) |
| In a Gaussian steady state $p=\mathcal{N}(0,\Pi^{-1})$, a Markov blanket $\eta\perp\mu\mid b$ is equivalent to $\Pi_{\eta\mu}=0$ while generally $\Sigma_{\eta\mu}\neq 0$ | FOLLOW (mathematical result) | Block matrix inversion of precision vs covariance (D2a; Da Costa et al., 2021) |
| A linear synchronization map $\sigma(\boldsymbol{\mu}(b))=\boldsymbol{\eta}(b)$ exists at a Gaussian steady state iff $\ker\Sigma_{\mu b}\subset\ker\Sigma_{\eta b} \iff \ker\Pi_{\mu b}\subset\ker\Pi_{\eta b}$ | FOLLOW (mathematical result) | Linear preimage inclusion (Lemma 2.3 in Da Costa et al., 2021; §8.3a) |
| Any smooth diffusion at steady state $p>0$ decomposes into a time-reversible dissipative drift $f_{\mathrm{rev}}=\Gamma\nabla\log p+\nabla\cdot\Gamma$ and a divergence-free solenoidal drift $f_{\mathrm{irrev}}=Q\nabla\log p+\nabla\cdot Q$ ($Q=-Q^\top$) | FOLLOW (mathematical result) | Helmholtz decomposition for stationary Fokker–Planck equations (Graham, 1977; Pavliotis, 2014; D5a) |
| Non-zero solenoidal flow $Q\neq 0$ accelerates convergence to the stationary density compared with pure gradient flow ($Q=0$) at fixed $\Gamma$, and can induce non-monotonic oscillations of the free energy | FOLLOW (mathematical result) | Spectral gap inequalities for non-reversible Langevin diffusions (Lelièvre et al., 2013; Rey-Bellet and Spiliopoulos, 2015; D5a) |
| A mean-zero stationary Gaussian boundary process with multi-exponential autocovariance can be realized as a Markovian integrator chain of generalized coordinates of motion $\tilde{s}_t=(s_t^{(0)},\dots,s_t^{(n)})$ | FOLLOW (mathematical result) | Doob's theorem and linear stochastic realization theory (Lindquist and Picci, 1985; §4.4) |
| A deployed LLM does not change weights in operation; context changes activations only | FOLLOW | Description of current deployment |
| A deployed LLM has no P-layer or stake in the direct sense | FOLLOW | Architecture; physics enters through text only |
| C2 is a predicate of a declared subsystem and window; there is no partial C2 | FOLLOW (definition) | D14a |
| The weights of a deployed LLM have no C2 | FOLLOW | Description of current deployment; D14a |
| A deployed LLM with a scaffold that has persistent memory has C2 | UNDECIDED | Depends on whether D14a (own operation, persistence, conditioning) holds in the particular scaffold |
| Channels are classified by write target, mediation by the receiver's models, and medium, and can be separated by shielding | UNDECIDED | §8.4a |
| Coupling needs recovery of structure beyond the shared prior and its use, and is directed | FOLLOW (definition) | D15a |
| The idealized measures and the Lyapunov-derived quantities ($\{\lambda_i\}$, $F(s)$, $D_{\rm KY}$, $h_{\rm KS}$) are invariant under smooth coordinate transformations | FOLLOW (mathematical result) | Diffeomorphism invariance of the derivative cocycle (§7.5) |
| Participation-ratio dimension $PR$ is coordinate-dependent and can be matched by a stable linear network (linear equivalence) | FOLLOW (mathematical result) | Clark (2026); Shen and Hu (2025) (§7.5, §10) |
| The cumulative Lyapunov distribution $F(s)$ equals the normalized trace of the one-step response of the minimum-norm shifted tangent dynamics | FOLLOW (mathematical result) | Exact finite-$N$ identity for $s\notin\{\lambda_i\}$ (Clark, 2026) (D7) |
| Integration is informational, not physical | FOLLOW (definition) | D9 |
| Scale indexing of agency quantities (via $\varphi_A$ and $\tau_w$, including truncation order $n(\tau_w)$ of generalized motion) | FOLLOW (follows from A2 and §4.4) | §4.4 |
| Shared causal order is a precondition for any channel; it does not unify internal latents | FOLLOW (definitional) | §3.1 |
| The role of the self-model is to separate the system's own contribution to its input from the environment's | UNDECIDED | C1 / D14; no test run |
| Qualia split into S and P classes | FOLLOW (formal structure) | D4, D6 |
| $I(Z_A;\hat{Z}_A)\le I(Z_A;Z_B)+nC$ under the stated assumptions | FOLLOW (mathematical result) | Data processing and channel capacity; assumptions in §8.3 |
| Interaction does not raise the capacity bound of a memoryless channel | FOLLOW (mathematical result) | Feedback does not increase the capacity of a memoryless channel |
| Recoverable content is the equivalence class of the latent, not its coordinates | FOLLOW (formal structure) | Behavioral equivalence; D18 |
| A gas cloud is not an agent by the criterion D12 | FOLLOW (given D5, D11a–D12) | No fixed structure $R$, so $\mathrm{Inf}\approx 0$; holds at the stated macro-level description |
| An untrained random chaotic RNN ($g>1$) has extensive $D_{\rm KY}\propto N$, $h_{\rm KS}>0$, and high $\mathcal{A}^{\rm do}$, and is not an agent by D12 | FOLLOW (given D11a–D12 and random couplings) | Random i.i.d. couplings carry no information about $E$ ($\mathrm{Inf}=0$) and do not close an action loop ($\mathrm{Cl}=0$) |
| A passive sensory-coupled Ornstein–Uhlenbeck process with $\Pi_{\eta\mu}=0$ and $\ker\Pi_{\mu b}\subset\ker\Pi_{\eta b}$ satisfies stationary variational free-energy minimization but is not an intrinsic agent by D12 | FOLLOW (given D11b–D12 and D17) | Has $\mathrm{Inf}>0$ via $\sigma$, but $\mathrm{Cl}=0$ (if sensory-only) and lacks viability stake $v$ and write-back (§5.1, §5.3) |
| Unity of a latent is a threshold property of a subsystem | UNDECIDED | A3; tested by P2 |
| The criterion D12 (integration, persistence, autonomy, closed informed loop) separates agents from passive and closed chaotic structures | UNDECIDED | Choice of measures and thresholds open; P6 with negative controls |
| Autonomy depends on the time window | FOLLOW (follows from D11, §4.4) | Internal means fixed in $R$ over the window |
| Stake supplies the reference for what is relevant | UNDECIDED | §5.3; P9 |
| Relevance of information is the drop of a reference quantity under surrogate decoupling | UNDECIDED | A11; P9 |
| Degrees of freedom, attractor dimension $D_{\rm KY}$, entropy rate $h_{\rm KS}$, and complexity decide agency | NULL | Gas cloud; noise; untrained chaotic RNN (§7.2) |
| Autonomy alone decides agency | NULL | A closed oscillator or chaotic RNN has maximal autonomy and is not an agent (§5.1) |
| Existence of a stationary Markov blanket with a synchronization map $\sigma(\boldsymbol{\mu}(b))=\boldsymbol{\eta}(b)$ suffices for agency | NULL | Satisfied by passive linear filters and coupled springs in a heat bath without loop closure or stake (§5.1, §5.3) |
| Capacity of the modeler must match the effective complexity of the relevant part of the modeled | UNDECIDED | A9; P8 |
| Memory and modeling of others are one mechanism | UNDECIDED | Depends on C2 being the mechanism |
| Memory does not exist, only copying of others' structure | NULL | A persistent correlated copy is memory by D16 |
| Humans have one stitched latent | UNDECIDED | Replaced by graded integration, A3; tested by P2 |
| Physical attractors are deep because of stake | UNDECIDED | A5; tested by P3 |
| Maintaining P costs more than S; deep abstraction usually reduces the P share | UNDECIDED | Plausible, unmeasured |
| Abstract thought always requires suppressing P | NULL | Counterexamples: spatial and bodily mathematical thinking |
| Human and LLM S-Q-structures overlap in relational geometry | UNDECIDED | P1 |
| Overlap of geometry implies identity of experience | NULL | Does not follow (§14) |
| Profiles $d(\varepsilon)$ and $(D_{\rm KY}, PR)$ differ between LLM, world model, and embodied model | UNDECIDED | P4 |
| Adding artificial stake deepens attractors ($\kappa(U), D(U)$) and raises autonomy | UNDECIDED | P3, P9 |
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
2. **It does not say that LLMs are or are not conscious or agents.** It lists which conditions are present or absent, and for autonomy, loop closure, and C2 it says the answer depends on the time window and on the declared subsystem boundary.
3. **It does not claim that a biological body is required.** Stake can in principle be implemented in an artificial system, though §15.6 notes the gap between simulated episode termination and physical dissolution of the carrier. P3 and P9 test the simulated version.
4. **It does not claim that a single manifold exists.** Unity is a graded, measurable property (A3).
5. **It does not claim that the measurements separate conscious from non-conscious systems.** They show geometry, tangent-space stability, Helmholtz flow ratios, autonomy, recoverability, and coupling.
6. **It does not claim measured values.** The entries in the comparison tables are structural statements, expectations from definitions, or predictions.
7. **It does not claim a physical origin of latents** in any quantum, electromagnetic, or gravitational structure, and does not depend on one.
8. **It does not claim that a good model of an agent reproduces the agent's experience.** §8 is about information about structure.
9. **It does not claim novelty.** A partial comparison was done in October 2026 (abstracts, targeted papers, not an exhaustive review). Close precedents exist. D11c uses the scrambling test of semantic information (Kolchinsky and Wolpert). D12 corresponds to the three conditions of agency of Barandiaran, Di Paolo, and Rohde (individuality, interactional asymmetry, normativity). $\mathcal{A}^{\rm pred}$ corresponds to the predictive information conditioned on the environment of Krakauer and collaborators. $\mathrm{Cl}$ corresponds to empowerment. The Q-structure corresponds to learned state-space structure (Churchland), trajectory geometry (Fekete and Edelman), and relational qualia structure (Tsuchiya and collaborators). The tangent-space response identity for $F(s)$, the single-site cavity solution for $D_{\rm KY}$ and $h_{\rm KS}$, and the contrast with $PR$ under linear equivalence follow Clark (2026) and Engelken et al. (2023). The precision-matrix Markov blanket ($\Pi_{\eta\mu}=0$), the kernel-inclusion condition for the synchronization map ($\ker\Pi_{\mu b}\subset\ker\Pi_{\eta b}$), the Helmholtz decomposition into dissipative and solenoidal drifts, and the stochastic-realization expansion into generalized coordinates of motion follow Da Costa, Friston, Heins, and Pavliotis (2021), Pavliotis (2014), and Lindquist and Picci (1985, 2015). What may be specific here is the synthesis: the window-indexed definition of internal structure and integrator-chain truncation (§4.4), tangent-space decomposition of interventional autonomy along $E^u$ vs $E^s$ (D11), the separation of true agency from passive stationary Markov blankets via stake and interventional loop closure (§5.1, §5.3), C2 as a predicate of a declared boundary (D14a), recoverability as a property of a pair with a protocol (§8), and directed coupling (D15a).
10. **It does not claim completeness.** The statuses in §16 can move in both directions after the experiments in §13.

---

## 18. Conclusion

Learning fixes a relief in the latent space of a subsystem, whose flow combines dissipative contraction with solenoidal circulation. Thinking spends a limited budget to move through it. Whether the subsystem is an agent is decided by integration, persistence, informational autonomy (the share of the system's future set by its own fixed structure), and a closed informed loop: the fixed structure carries information about the environment, the system acts on the environment, and the information it uses is information whose loss would cost it something. Autonomy, internal dynamical richness ($D_{\rm KY}, h_{\rm KS}$), and stationary Markov-blanket synchronization ($\sigma(\boldsymbol{\mu}(b))=\boldsymbol{\eta}(b)$) alone do not decide this. Degrees of freedom and complexity do not decide it either. They set capacity, which limits how much the system can hold and how much of another system it can model.

Between two agents the structure that can pass is bounded by the shared prior plus the channel's capacity, gated at the boundary by the kernel-inclusion condition $\ker\Pi_{\mu b}\subset\ker\Pi_{\eta b}$, and what is recovered is an equivalence class of the other's latent, not its coordinates. Memory and models of others are the same mechanism, write-back at limited resolution, applied to different targets. Coupling is directed and requires recovery beyond the prior plus use.

$$
\text{Subsystem}\rightarrow\text{Latent}\rightarrow\text{Learned relief }(f_{\mathrm{rev}}+f_{\mathrm{irrev}})\rightarrow\text{Informedness }(\ker\Pi_{\mu b}\subset\ker\Pi_{\eta b})\rightarrow\text{Action loop}\rightarrow\text{Use}\rightarrow\text{Autonomy}\rightarrow\text{Self-model}\rightarrow\text{Write-back}\rightarrow\text{Other-model}\rightarrow\text{Directed coupling}
$$

Stake modifies the depth of the relief and supplies the reference for what is relevant along this chain. The step from the chain to experience is not made here. What can be done is to measure geometry, Lyapunov spectra, Helmholtz ratios, autonomy, recoverability, and coupling and see whether the predictions hold.

---

## Appendix A: Core Formulae as Schemata

Most expressions are schemata: compressed relations that make the argument easier to follow. Some are formal definitions. Some are measurement proxies. Several are mathematical results under stated assumptions.

| Expression | Status | Reading |
| ---------- | ------ | ------- |
| $Z_A=\varphi_A(x_A)$ | Schema | Latent as a coarse-grained description of a subsystem |
| $\Pi_{\eta\mu}=0,\ \Sigma_{\eta\mu}=-\Pi_\eta^{-1}\Pi_{\eta b}\Sigma_{b\mu}\neq 0$ | Mathematical result (Gaussian / local Laplace) | Markov blanket as precision sparsity coexisting with long-range covariance (D2a; Da Costa et al., 2021) |
| $\ker\Pi_{\mu b}\subset\ker\Pi_{\eta b} \iff \exists\,\sigma:\ \sigma(\boldsymbol{\mu}(b))=\boldsymbol{\eta}(b)$ | Mathematical result (Gaussian steady state) | Kernel-inclusion condition for lossless synchronization across the boundary (§8.3a; Da Costa et al., 2021) |
| $f_R = (-\Gamma\nabla\mathcal{U}_R+\nabla\cdot\Gamma) + (-Q\nabla\mathcal{U}_R+\nabla\cdot Q),\ Q=-Q^\top$ | Mathematical result (stationary smooth diffusions) | Helmholtz decomposition of relief flow into dissipative and solenoidal parts (D5a) |
| $ds_t^{(k)} = f_k(s_t^{(k)},s_t^{(k+1)})\,dt + \varsigma_k\,dW_t^{(k)}$ ($k\le n(\tau_w)$) | Mathematical result (multi-exponential Gaussian processes) | Stochastic realization as an integrator chain of generalized coordinates of motion, truncated at scale $\tau_w$ (§4.4) |
| $Z\supseteq P\cup S$, coupled | Schema | Layers of one subsystem's latent |
| $R=R(\theta)$ | Schema | Relief determined by weights / persistent structure |
| $D(U)=\inf\{\lVert\delta\rVert: z+\delta\text{ does not return to }U\}$ | Formal structure | Finite-perturbation depth of a region |
| $F(s)=\lim_{\eta\to 0^+}\frac{1}{N}\mathrm{tr}\,R^{vv}_\eta(k+1,k)$ | Mathematical result (exact at finite $N$ for $s\notin\{\lambda_i\}$) | Cumulative Lyapunov distribution as trace of the minimum-norm tangent response / dichotomy projector onto $E^s_s$ (Clark, 2026) |
| $\kappa(U)=-\int_{-\infty}^0 s\,F'(s)\,ds$ | Measurement proxy | Local transverse contraction rate in $U$ (primary stiffness measure under A6) |
| $F(\theta)=\mathbb{E}[\nabla\log p\,\nabla\log p^{\top}]$, spectrum of $F$ | Measurement proxy | Weight-space stiffness as a secondary proxy for depth |
| $d(r)=d\log C(r)/d\log r$ | Measurement proxy | Effective spatial dimension at scale $r$ |
| $D_{\rm KY}=j+\frac{\sum_{i=1}^j \lambda_i}{\vert{}\lambda_{j+1}\vert{}}$ and $h_{\rm KS}=\sum_{\lambda_i>0}\lambda_i$ | Formal structure (diffeomorphism-invariant) | Kaplan–Yorke attractor dimension and Kolmogorov–Sinai entropy rate (Pesin's formula) |
| $PR=(\mathrm{tr}\,C)^2/\mathrm{tr}(C^2)$ | Measurement proxy (coordinate-dependent) | Linear subspace participation ratio |
| $c_P+c_S\le\rho_{\max}$ | Schema | The cost of traversal per unit time is bounded by the envelope |
| $\Pi_{\mathrm{plast}}=\lVert\Delta R\rVert/\text{unit of experience}$ | Schema | Plasticity |
| $M(z)\subset Z$, with $M\subset z$ | Schema | Self-model inside the space it models |
| $I(A)=\min_{\text{cuts}}\mathrm{Dep}(A_1\leftrightarrow A_2)/\mathrm{Dep}(A\leftrightarrow E)$ | Schema, measure open | Integration |
| $\mathcal{A}^{\rm pred}_\tau=I(Z_{t+\tau};Z_t\mid E_t)$ | Measurement proxy | Predictive autonomy |
| $\mathcal{A}^{\rm do}_\tau=\mathbb{E}\lVert\Delta_{\rm int}\rVert/(\mathbb{E}\lVert\Delta_{\rm int}\rVert+\mathbb{E}\lVert\Delta_{\rm env}\rVert)$ | Measurement proxy | Interventional autonomy (resolved along $E^u$ vs $E^s$) |
| $\mathrm{Inf}=1-\varepsilon_A/\varepsilon_0$ | Measurement proxy | Informedness: gain over randomized relief |
| $\mathrm{Cl}=\mathbb{E}\lVert\Delta^{\rm act}_{\rm in}\rVert/(\mathbb{E}\lVert\Delta^{\rm act}_{\rm in}\rVert+\mathbb{E}\lVert\Delta^{\rm ext}_{\rm in}\rVert)$ | Measurement proxy | Loop closure |
| $U=(Q_{\rm int}-Q_{\rm dec})/(Q_{\rm int}-Q_{\rm floor})$ | Measurement proxy | Use of relevant information |
| $C(A)\ge C_{\rm eff}(B\mid\text{task})$ | Schema (A9) | Requisite capacity |
| $I(Z_A;\hat{Z}_A)\le I(Z_A;Z_B)+nC$ | Mathematical result under stated assumptions | Recoverability bound |
| $\nu$ | Schema | Resolution of a stored model, bits per structure |
| $W(A,\tau_w)$ | Predicate (D14a) | Write-back: own operation, persistence, conditioning |
| $\mathrm{Coup}(A\!\to\!B)$ | Predicate (D15a) | Directed coupling: channel, recovery beyond the prior, use |

---

## Appendix B: Related Concepts (partly checked at the level of abstracts or primary preprints, otherwise from memory, not for publication)

Names only, so that later checking is easier. Entries marked [checked] were confirmed at the level of primary texts, abstracts, or secondary sources in October 2026. The others are from memory and unverified. Each needs to be verified before use. Nothing in the framework depends on the correctness of an attribution.

- **Bayesian mechanics for stationary processes, Markov blankets, Helmholtz decomposition, and stochastic realization of integrator chains** (Da Costa, Friston, Heins, and Pavliotis, 2021, *Proc. R. Soc. A* 477: 20210518; Pavliotis, 2014; Graham, 1977; Lelièvre, Nier, and Pavliotis, 2013; Rey-Bellet and Spiliopoulos, 2015; Lindquist and Picci, 1985, 2015; Aguilera, Millidge, Tschantz, and Buckley, 2021; Biehl, Pollock, and Kanai, 2021) [checked]: Markov blanket as precision sparsity $\Pi_{\eta\mu}=0$; Lemma 2.3 establishing $\ker\Sigma_{\mu b}\subset\ker\Sigma_{\eta b} \iff \ker\Pi_{\mu b}\subset\ker\Pi_{\eta b}$ as necessary and sufficient for the synchronization map $\sigma(\boldsymbol{\mu}(b))=\boldsymbol{\eta}(b)$; Helmholtz decomposition of stationary diffusion drift into reversible dissipative ($\Gamma$) and irreversible solenoidal ($Q=-Q^\top$) flows with accelerated convergence; stochastic realization of non-Markovian Gaussian boundary processes via nested Ornstein–Uhlenbeck integrator chains $\tilde{s}_t=(s_t^{(0)},\dots,s_t^{(n)})$ and PID-like control; technical critiques of when drift coupling vs precision sparsity implies a Markov blanket. Used in D2a, D5a, §4.4, §5.1, §5.3, §8.3a, P6, P7, and P10.
- **Lyapunov spectrum of random neural networks, minimum-norm tangent response, and linear equivalence** (Clark, 2026, `arXiv:2610.12426`; Engelken, Wolf, and Abbott, 2023; Sompolinsky, Crisanti, and Sommers, 1988; Clark, Abbott, and Litwin-Kumar, 2023; Shen and Hu, 2025) [checked]: exact finite-$N$ identity $F(s)=N^{-1}\mathrm{tr}\,\partial v(k+1)/\partial I^v(k)$ via the dichotomy projector onto stable tangent subspaces; single-site cavity solution for $F(s)$, Kaplan–Yorke attractor dimension $D_{\rm KY}$, and Kolmogorov–Sinai entropy rate $h_{\rm KS}$; contrast between diffeomorphism-invariant $D_{\rm KY}$ and coordinate-dependent participation ratio $PR$ under linear equivalence. Used in A6, D7, D11, §7.5, §10, and P4–P6.
- **Multiplicative ergodic theorem, attractor dimension, entropy rate, and dichotomy projectors** (Oseledets, 1968; Kaplan and Yorke, 1979; Pesin, 1977; Ruelle, 1978, 1982; Sacker and Sell, 1978; Hüls, 2009; Deninger, 2011) [checked via Clark, 2026]: tangent-space splitting $\mathbb{R}^N=E^s(n)\oplus E^u(n)$, $D_{\rm KY}$, $h_{\rm KS}$, and dichotomy spectrum.
- **Transient chaos and fractal basins in latent reasoning; dynamical similarity** (Lai, Bao, Quinn, and Gilpin, 2026, `arXiv:2609.04963`; Ostrow, Eisen, Kozachkov, and Fiete, 2023; Poole et al., 2016; Engelken, 2023) [checked via secondary citations]: looped latent reasoning lingering near unstable chaotic states ($\lambda_1>0$) on hard tasks (D8), and Dynamical Similarity Analysis (D18).
- **Law of requisite variety; good-regulator theorem** (Ashby; Conant and Ashby): the source of A9.
- **Information closure and autonomy as an information-theoretic quantity** (Bertschinger, Olbrich, Ay, Jost and related work): close to D11.
- **Informational theory of individuality** (Krakauer and collaborators) [checked: autonomy as predictive information conditioned on the environment]: close to D9–D12 and to $\mathcal{A}^{\rm pred}$.
- **Causal emergence** (Hoel and collaborators): relevant to the choice of coarse-graining in A2 and §15.3.
- **Statistical complexity and the epsilon-machine** (Crutchfield and collaborators): the predictive complexity in §7.2.
- **Semantic information as viability-relevant information** (Kolchinsky and Wolpert) [checked]: D11c uses their scrambling test, and viability that is intrinsic to the system as the reference (§5.3) is also their point.
- **Defining agency: individuality, normativity, asymmetry** (Barandiaran, Di Paolo, and Rohde, 2009) [checked]: three conditions that correspond to D9–D11 (individuality), D11b (the system as an active source of change in its coupling with the environment), and D11c with stake (normativity). D12 is close to a restatement of these in information-theoretic form.
- **Empowerment** (capacity of the channel from actions to later inputs; Klyubin, Polani, and Nehaniv, from memory) [checked: the notion, and a 2025 preprint estimating it for language-model agents]: close to D11b.
- **State-space semantics** (P. Churchland; Laakso and Cottrell on distances between activations in trained networks) [checked through secondary sources]: regions and points of the learned activation space of a trained network as carriers of qualitative content. Close to the Q-structure of D6.
- **Experience as the structure of state-space trajectories** (Fekete and Edelman; dynamical emergence theory) [checked]: the structure of phenomenal experience defined by the geometry and topology of the system's own dynamics. Close to the traversal side of §4.
- **Relational structure of qualia** (Tsuchiya, Saigo, and collaborators) [checked]: relations among qualia mirrored by relations among neural or model representations. Close to A7.
- **Attention schema theory** (Graziano) and **forward models and comparator accounts of the sense of agency** (Wolpert and collaborators; from memory): a self-model whose function is control, and the separation of self-caused from externally caused input. Background for C1 and the candidate role of $M$ in D14.
- **Integrated information** (Tononi and collaborators): a competing family of integration measures; criticized for assigning high values to simple structures.
- **Homeostatic accounts of feeling** (Damasio; Seth), **self-model theory** (Metzinger), **embodied cognition** (Varela, Thompson, Rosch): background for C1–C3.
- **Representational similarity analysis; centered kernel alignment** (Kriegeskorte et al.; Kornblith et al.): instruments for A7 and D18.
- **Platonic representation hypothesis** (Huh et al.): the competing explanation for P2 and P7.
- **Information geometry and natural gradient** (Amari): related to the Fisher metric retained as a secondary weight-level proxy in D7.
- **Reconstructive memory** (Bartlett and later work on reconsolidation): background for D16 and §8.7.