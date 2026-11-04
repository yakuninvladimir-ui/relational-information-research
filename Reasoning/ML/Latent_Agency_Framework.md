# **Latent Agency Framework (LAF) — Integration, Autonomy, Learned Relief, and the Recoverability of Structure Between Agents**

**Author:** Vladimir Yakunin  
**Version:** 2.1 (ML Engineering Edition — full structural and mathematical fidelity)  
Date: 2026-10-21  
Successor to: Latent Agency Framework v2.0; Unified Latent Space of Consciousness v1.0 (superseded; archived on Zenodo)  
Status: Working concept specification (Reasoning layer). Framework only; not a finished theory. Thesis statuses under V\_4 are listed in §16.

# **Abstract & ML Engineering Overview**

Why this document exists (for ML Engineers):  
When we inspect modern AI systems—frozen LLMs, recurrent/state-space world models, RL agents, and tool-using agentic scaffolds—four fundamental questions are routinely conflated:

1. **What does training fix?** Training shapes a **learned relief R** (attractor basins, vector fields, invariant manifolds) inside the subsystem's latent space Z. Its flow splits via **Helmholtz decomposition** into a dissipative gradient pull (Γ) and a rotational solenoidal circulation (Q \= −Qᵀ) that accelerates convergence back to attractors.  
2. **What does inference spend?** Moving a state trajectory z(t) through the relief spends a **bounded reasoning budget ρ** (compute/activations per step).  
3. **What makes a subsystem an agent at all?** Neither parameter count N, nor chaotic attractor dimension (D\_KY, h\_KS), nor the mere existence of a stationary Markov blanket (Bayesian mechanics) makes a system an agent. Agency is a graded 6-tuple property measured at a declared spatial coarse-graining φ\_A and time window τ\_w: **Integration I(A)**, **Persistence T\_pers(A)**, **Informational Autonomy A(A; τ\_w)**, and a **Closed Informed Loop** consisting of **Informedness Inf**, **Interventional Loop Closure Cl**, and **Viability/Task-Grounded Use U**.  
4. **How much of Agent A's internal latent structure can Agent B recover across a low-dimensional communication channel?** Recovery is upper-bounded by `I(Z_A; Z_B) + nC` (shared prior plus channel capacity), gated at the boundary by the **kernel-inclusion condition** `ker(Π_{μb}) ⊂ ker(Π_{ηb})`, and unified with long-term memory as a single mechanism: **finite-resolution write-back W(A, τ\_w)** into the persistent relief.

This document keeps these four questions strictly separated, provides coordinate-invariant dynamical estimators (Lyapunov spectrum F(s), Kaplan–Yorke dimension D\_KY, minimum-norm tangent response R^{vv}), contrasts genuine agency against three negative controls (a gas cloud, a Sompolinsky chaotic random RNN at g \> 1, and a passive stationary Ornstein–Uhlenbeck Markov blanket), and formulates **ten falsifiable experimental predictions (P1–P10)**. The philosophical "hard problem" of subjective experience is explicitly bracketed outside the framework (§14).

# **1\. Introduction: The Problem**

## **1.1. Statement: Separating Four Tangled Questions**

We can now open artificial systems and inspect their hidden activations and Jacobians directly. A physics world model has a latent space Z shaped by sensorimotor dynamics (P-layer). A deployed LLM has a latent space shaped almost entirely by text semantics (S-layer). A biological agent couples both layers tightly. To compare them without philosophical hand-waving, we separate four questions:

1. **What does learning fix?** (The relief R and its dissipative \+ solenoidal vector field G\_R.)  
2. **What does thinking spend?** (The bounded reasoning budget ρ.)  
3. **What distinguishes an agent from a passive filter or an isolated chaotic generator?** (The 6 agency criteria on window τ\_w.)  
4. **How much of one agent's latent structure can another agent reconstruct across a channel?** (The recoverability bound and kernel-inclusion gate.)

## **1.2. What Changed in Version 2.1**

* **Unity as a measurable threshold, not a human postulate:** Earlier versions assumed humans possess a single unified manifold while models do not. Here, unity of a latent space is a graded informational integration score I(A) measured on a subsystem at a declared scale.  
* **Relation to Stationary Markov Blankets ("Bayesian Mechanics"):** A Markov blanket (block sparsity Π\_{ημ} \= 0 in the inverse covariance / precision matrix between environment η and internal states μ given boundary b \= (s, a)) provides a clean mathematical boundary description, a synchronization map σ(μ\_bar(b)) \= η\_bar(b) when `ker(Π_{μb}) ⊂ ker(Π_{ηb})`, a Helmholtz decomposition of drift, and a stochastic-realization chain of generalized coordinates s\_t^(0..n). However, we prove by counterexample that **stationary Markov-blanket mechanics is a necessary boundary kinematics, not a sufficient criterion of agency**: without interventional loop closure (Cl \> θ\_Cl), viability-grounded stake (v), write-back (W), and external verification, a stationary Markov blanket cannot distinguish an adaptive agent from a passive RC circuit or coupled springs in a heat bath.

## **1.3. Place in the Repository Architecture**

*The Algorithm of Being* defines consciousness-like architecture at the macro-level as recursive self-modeling under external verification (`Propose — Judge — Commit`). This document (*LAF v2.1*) works one layer deeper—at the tangent-space dynamics, Lyapunov spectra, and boundary projections of the latent carrier Z—and establishes the formal prerequisites for being an agent in the first place.

## **1.4. Scope**

* **In scope:** Formal definitions (D1–D19), system taxonomy, information-theoretic and linear-Gaussian recoverability theorems, and ten runnable empirical predictions (P1–P10).  
* **Out of scope:** The hard problem of phenomenal consciousness (§14), quantum/gravitational theories of mind, and any "universal latent space of the universe."

# **2\. Explicit Foundational Assumptions (A1–A11)**

Every derived statement in this framework rests on the eleven explicit assumptions below. None is treated as dogma; all carry status `UNDECIDED` under the repository's ternary standard.

| ID | Assumption | Status | Main Risk / Competing View |
| :---- | :---- | :---- | :---- |
| **A1** | **Computational functionalism with the body as a functional constraint envelope.** Organization and causal/informational structure matter, not biological wetware. The body enters via the P-layer and viability stake v. | UNDECIDED | Rival: biological naturalism (mind requires living metabolism). |
| **A2** | **A latent space is a scale-indexed description of a subsystem.** For subsystem A ⊂ C, a coarse-graining map φ\_A yields Z\_A \= φ\_A(x\_A) at the chosen spatial/temporal scale. | UNDECIDED | Results depend on the choice of φ\_A unless a canonical scale selector is fixed (§15.3). |
| **A3** | **Unity is graded.** Integration I(A) varies continuously; "one unified latent" means I(A) \> θ\_I. | UNDECIDED | Candidate dependence measures (MI, transfer entropy, causal emergence) may rank edge cases differently. |
| **A4** | **Learning fixes the relief R; inference traverses it.** Over operational window τ\_w, R changes only via plasticity Π\_plast. | UNDECIDED | In biological brains and in-context learning, fast activation shifts and slow plasticity blur. |
| **A5** | **Attractor depth in the P-layer scales monotonically with stake v.** | UNDECIDED | Tested directly in Prediction P3. |
| **A6** | **Dynamic depth via tangent-space contraction and solenoidal acceleration.** Local stiffness of an attractor U ⊂ Z is tracked by the negative Lyapunov spectrum of the state Jacobian M(n) \= ∂z(n+1)/∂z(n) (via the dichotomy projector onto stable directions E^s), while return speed τ\_ret(U) is accelerated by the ratio of solenoidal (skew-symmetric Q) to dissipative (symmetric Γ) flow. Weight-space Fisher stiffness F(θ) is only a secondary proxy. | UNDECIDED | Infinitesimal contraction (λ\_i \< 0\) and finite basin width D(U) can diverge under "stable chaos" (§15.7). |
| **A7** | **Relational and diffeomorphism-invariant comparison.** Systems with different coordinates are compared via relational geometry (RSA, CKA) and coordinate-invariant dynamical quantities (Lyapunov spectrum {λ\_i}, Kaplan–Yorke dimension D\_KY, KS entropy rate h\_KS). | UNDECIDED | Human neural recordings are too coarse for full Lyapunov spectra. |
| **A8** | **Internal sub-models.** A subspace M ⊂ Z can represent a self-model of Z, and O\_B ⊂ Z can represent an other-model of agent B. | UNDECIDED | Reliability of self-models in current LLMs is contested. |
| **A9** | **Requisite capacity (Ashby's Good Regulator principle).** Regulating or predicting agent B requires model capacity C(A) ≥ C\_eff(B \| task). | UNDECIDED | Imported from classical control theory; tested in P8. |
| **A10** | **Interventional measurability.** Autonomy A^do, loop closure Cl, and use U are measurable via standardized interventions (1 SD of natural variation), resolved along the tangent splitting E^s ⊕ E^u. | UNDECIDED | Exact in open-weights models/sims; indirect in biology. |
| **A11** | **Operational relevance via surrogate decoupling.** Information in R about environment E is relevant to A to the extent that time-shuffling or decoupling that channel lowers a maintained reference quantity Q (where Q \= v under stake). | UNDECIDED | Without intrinsic stake v, Q is externally assigned (§15.6). |

# **3\. Substrate, Subsystems, Markov Blankets, and Latent Layers**

## **3.1. Engineering Intuition: Causal Substrate and Interfaces**

To talk about agents interacting in a physical or simulated world, we require only four minimal properties from the underlying substrate C: (1) a causal order, (2) finite signal speed, (3) finite channel capacity, and (4) finite information and thermodynamic cost per bounded region. Sharing a causal order allows two subsystems A and B to exchange signals through a channel, but it does **not** merge their internal latent spaces Z\_A and Z\_B into a single manifold.

## **3.2. Formal Definitions (D1–D4)**

* **D1. Substrate C:** A causal structure with finite signal propagation speed, finite channel capacity, finite information per bounded region, and non-zero thermodynamic cost for irreversible operations (Landauer bound).  
* **D2. Subsystem A, Environment E, and Interface B\_A:** A subsystem A ⊂ C with an identifiable boundary B\_A \= (S\_A, Act\_A) partitioned into **sensory states S\_A** (receiving inputs from outside) and **active states Act\_A** (emitting actions to the outside). E \= C \\ (A ∪ B\_A) is the external environment coupled to A through B\_A.  
* **D2a. Statistical Boundary (Markov Blanket) vs. Dynamical Coupling:** In a stationary regime where joint states x \= (η, b, μ) ∈ E × B\_A × I\_A admit a smooth density p(x) with inverse covariance (precision matrix) Π \= Σ⁻¹, a **Markov blanket** is the conditional independence relation η ⊥ μ \| b. In the Gaussian (or local Laplace) regime, this is equivalent to block zeroes in the precision matrix while long-range correlations remain non-zero (Da Costa et al., 2021):  
  Π\_{ημ} \= Π\_{μη}ᵀ \= 0,   whereas in general   Σ\_{ημ} \= −Π\_η⁻¹ Π\_{ηb} Σ\_{bμ} ≠ 0\.  
  *Crucial Dynamical Caveat:* In a continuous-time SDE, stationary precision sparsity (Π\_{ημ} \= 0\) does not by itself forbid direct skew-symmetric (solenoidal) drift coupling across the boundary unless causal locality is enforced by the substrate (Biehl et al., 2021). Here, interaction locality through B\_A is enforced structurally by D1–D2.  
* **D3. Latent Space Z\_A:** A compressed representation Z\_A \= φ\_A(x\_A) of the subsystem's microstate at scale φ\_A, governed by the discrete-step map z(n+1) \= G\_R(z(n), s(n)) or continuous-time SDE.  
* **D4. P-Layer, S-Layer, and Cross-Layer Stitching:**  
  * **P-Layer (Physical / Embodied / Sensorimotor):** Encodes spatial physics, sensorimotor kinematics, interoception, and homeostatic variables.  
  * **S-Layer (Semantic / Symbolic / Abstract):** Encodes language, logic, mathematics, and discrete conceptual abstractions.  
  * **Stitching:** Coupling between P and S within Z\_A, measured empirically by cross-layer integration I(A) and CKA/predictability (Prediction P2).

| System Type | Latent Space Z Composition |
| :---- | :---- |
| **Deployed LLM (text-only)** | Almost entirely S-layer; physical world represented indirectly via text tokens. |
| **Pure Visual/Physics World Model** | Almost entirely P-layer; weak or absent symbolic S-layer. |
| **Human / Embodied Multimodal Agent** | Both P and S present; tightly coupled in humans (why bodily pain disrupts abstract math, and abstract fear triggers autonomic response). |

# **4\. Learned Relief, Helmholtz Decomposition, and Generalized Coordinates**

## **4.1. Engineering Intuition: Why Solenoidal Flows Speed Up Convergence**

When a neural network or dynamical system relaxes toward a learned attractor (a basin U in the relief R), its trajectory is rarely a straight gradient descent. By the **Helmholtz decomposition** for stationary diffusions, any smooth drift vector field f\_R(z) splits into a **dissipative gradient component** (pulling straight down the potential U\_R(z) \= −log p\_R(z)) and a **divergence-free solenoidal (rotational/vortical) component** Q(z) \= −Q(z)ᵀ circulating along level sets. Far from being a nuisance, a non-zero solenoidal matrix Q ≠ 0 breaks detailed balance, suppresses diffusive backtracking, and **strictly accelerates convergence to the attractor**, at the cost of damped oscillatory spirals in the loss/energy during recovery (Prediction P10).

## **4.2. Formal Definitions (D5–D8)**

* **D5. Learned Relief R:** The persistent structure fixed by learning (network weights θ, synaptic conductances, persistent memory stores inside the declared boundary) that defines the transition operator G\_R or drift field f\_R on Z.  
* **D5a. Helmholtz Decomposition of the Relief Flow:** For a continuous-time latent SDE `dz_t = f_R(z_t) dt + ς(z_t) dW_t` with local stationary density `p_R(z) ∝ exp(−U_R(z))`, the drift decomposes uniquely into time-reversible dissipative and time-irreversible solenoidal parts (Graham, 1977; Pavliotis, 2014; Da Costa et al., 2021):  
  f\_R(z) \= f\_rev(z) \+ f\_irrev(z),  
  f\_rev(z) \= −Γ(z) ∇U\_R(z) \+ ∇·Γ(z)   (Dissipative gradient flow, where Γ(z) \= (1/2) ς(z) ς(z)ᵀ ⪰ 0),  
  f\_irrev(z) \= −Q(z) ∇U\_R(z) \+ ∇·Q(z)   (Solenoidal circulatory flow, where Q(z) \= −Q(z)ᵀ and ∇·(p\_R f\_irrev) \= 0).  
  In discrete-step linearized dynamics `v(n+1) = M(n) v(n)`, this corresponds to splitting the generator into its symmetric and skew-symmetric parts.  
  * *Property 1 (Accelerated relaxation):* At fixed diffusion Γ, any non-zero solenoidal flow Q ≠ 0 strictly increases the spectral gap and accelerates convergence to p\_R compared to pure gradient descent Q \= 0 (Lelièvre et al., 2013; Rey-Bellet & Spiliopoulos, 2015).  
  * *Property 2 (Damped oscillatory transients):* When ‖Q‖\_F ≫ ‖Γ‖\_F, trajectories spiral into the attractor, producing damped oscillations in instantaneous prediction error / free energy (tested in P10).  
* **D6. Structural Quale (Q-Structure and Q-Event):**  
  * *Q-structure:* A learned attractor basin or invariant submanifold fixed in R.  
  * *Q-event:* A runtime trajectory pass z(t) through a Q-structure. *(Used strictly in a deflated structural sense; whether it feels like anything is bracketed in §14.)*  
* **D7. Attractor Depth D(U), Tangent-Space Contraction κ(U), and Minimum-Norm Response F(s):**  
  * *Finite-perturbation basin depth:* `D(U) = inf { ‖δ‖ : trajectory from z + δ does not return to U }`, paired with return time `τ_ret(U)`.  
  * *Infinitesimal tangent-space stability (Clark, 2026):* Along trajectory z(n) ∈ U with state Jacobian `M(n) = ∂G_R(z)/∂z|_{z(n)}` and Lyapunov exponents `λ_1 ≥ ... ≥ λ_N`, shifting the Jacobian via `M_s(n) = e^(−δs) M(n)` and selecting the minimum-norm tangent trajectory driven by source `I^v(k)` yields a one-step response matrix `R^{vv}(k+1, k) = ∂v(k+1)/∂I^v(k)` that equals the oblique **dichotomy projector P\_s(k+1)** onto the stable subspace E^s\_s of directions with λ\_i \< s. The exact cumulative Lyapunov distribution at finite N is the normalized trace:  
    F(s) \= (1 / N) \|{ i : λ\_i \< s }\| \= lim\_{η → 0⁺} (1 / N) tr R^{vv}\_η(k+1, k).  
    Local transverse stiffness of basin U is measured directly in activation space Z by the fraction of contracting directions F(0) and the **mean transverse contraction rate**:  
    κ(U) \= −∫\_{−∞}^0 s F'(s) ds \= (1 / N) ∑\_{λ\_i \< 0} \|λ\_i\|.  
* **D8. Reasoning Budget ρ:** The bounded computational resource spent per unit time to update activations along the relief. On hard reasoning inputs, looped latent models can exhibit **transient chaos** (λ\_1 \> 0 over finite horizons; Lai et al., 2026), lingering near saddle structures and consuming more of ρ before settling.

## **4.4. Temporal Scale τ\_w and Truncation of Generalized Coordinates of Motion**

When sensory inputs s\_t arriving at boundary S\_A have smooth multi-exponential temporal autocorrelation C(τ) \= E\[s\_{t+τ} ⊗ s\_t\], Doob's theorem and linear stochastic realization theory (Lindquist & Picci, 1985, 2015; Da Costa et al., 2021\) show that the non-Markovian boundary stream can be embedded as a Markovian **integrator chain of generalized coordinates of motion** `s_tilde_t = (s_t^(0), s_t^(1), ..., s_t^(n))` (representing position, velocity, acceleration, jerk, up to order n):

ds\_t^(k) \= f\_k(s\_t^(k), s\_t^(k+1)) dt \+ ς\_k dW\_t^(k)   (k \= 0, ..., n − 1),   ds\_t^(n) \= f\_n(s\_t^(n)) dt \+ ς\_n dW\_t^(n).

**Engineering Meaning of Choosing Scale (φ\_A, τ\_w):**  
Fixing a spatial coarse-graining φ\_A and temporal evaluation window τ\_w is dynamically equivalent to **truncating this integrator chain at finite order n(τ\_w)**:

* Fast higher-order derivatives k \> n(τ\_w) whose relaxation times are much shorter than τ\_w fall into the coarse-graining kernel `ker(dφ_A)` (`OMIT`) and are integrated out as effective white noise.  
* Active orders k ≤ n(τ\_w) must be tracked and controlled by the internal relief R (yielding proportional/integral control for n \= 0, 1, PID-like control for n \= 2, and higher-order trajectory prediction for n ≥ 3).

# **5\. What Makes a Subsystem an Agent: The Six Measurable Criteria**

## **5.1. Three Negative Controls That Break Naive Agency Definitions**

Why do we need six criteria (D9–D12)? Because simpler definitions fail on three classic physical and neural systems:

1. **Cloud of Gas:** Enormous number of degrees of freedom N, identifiable boundary, high entropy—yet zero fixed internal relief R (Inf ≈ 0, A ≈ 0). Driven entirely from outside.  
2. **Untrained Chaotic Random RNN (Sompolinsky model at coupling g \> 1):** Has high integration, long persistence, maximal internal autonomy (A^do ≈ 1), extensive attractor dimension (D\_KY ∝ N), and positive Kolmogorov–Sinai entropy production (h\_KS \> 0). Yet its random weights J\_{ij} \~ N(0, g²/N) carry **zero information about an environment (Inf \= 0\)** and **zero action loop closure (Cl \= 0\)**. It is an isolated chaotic generator, not an agent.  
3. **Passive Stationary Markov Blanket (Linear Ornstein–Uhlenbeck filter in a heat bath):** Satisfies Π\_{ημ} \= 0 and `ker(Π_{μb}) ⊂ ker(Π_{ηb})`, so its conditional internal mean linearly tracks external states `σ(μ_bar(b_t)) = η_bar(b_t)` (Inf \> 0\) and algebraically minimizes quadratic variational free energy at steady state (Da Costa et al., 2021). Yet a passive RC filter or damped spring network satisfies these exact equations\! Because its precision matrix Π is fixed externally by the bath, it has **zero interventional loop closure (Cl \= 0 if sensory-only)**, **no viability stake v** (scrambling the bath merely shifts the Gaussian steady state without destroying the circuit), and **no self-initiated write-back W**.

## **5.2. Formal Definitions of the Six Agency Quantities (D9–D12)**

All quantities are evaluated at a declared spatial coarse-graining φ\_A and temporal window τ\_w:

* **D9. Integration I(A):** Interdependence of internal parts relative to environmental coupling across all bipartitions (A\_1, A\_2) of Z\_A:  
  I(A) \= min\_{cuts (A\_1, A\_2)} \[ Dep(A\_1 ↔ A\_2) / Dep(A ↔ E) \].  
  *(Integration is informational, not physical: a model sharded across 8 GPUs has the exact same I(A) as on 1 GPU.)*  
* **D10. Persistence T\_pers(A):** Duration over which the boundary B\_A remains identifiable and I(A) \> θ\_I.  
* **D11. Informational Autonomy A(A; τ\_w):** Share of the future internal state Z\_{t+τ} determined by A's own state at t versus environment inputs:  
  * *Predictive proxy:* `A^pred_τ = I( Z_{t+τ} ; Z_t | E_t )`.  
  * *Interventional measure (preferred):* Under 1-SD standardized interventions on internal state (`Δ_int`, projected onto active attractor directions `E^u` via `Id − P_{s_KY}` where Jacobians are available) vs. environment input (`Δ_env`):  
    A^do\_τ \= E‖Δ\_int‖ / ( E‖Δ\_int‖ \+ E‖Δ\_env‖ ) ∈ \[0, 1\].  
* **D11a. Informedness Inf(A; τ\_w):** How much predictive information the fixed relief R carries about environmental regularities E (including active generalized motion orders s\_tilde\_t^(k)), compared to a randomized relief baseline (e.g., i.i.d. Gaussian weights of matched variance):  
  Inf \= 1 − (ε\_A / ε\_0) ∈ \[0, 1\].  
* **D11b. Interventional Loop Closure Cl(A; τ\_w):** Share of the system's future sensory input at t \+ τ caused by its own active outputs at t (`Δ^{act}_{in}`) versus independent external environment sources (`Δ^{ext}_{in}`):  
  Cl \= E‖Δ^{act}*{in}‖ / ( E‖Δ^{act}*{in}‖ \+ E‖Δ^{ext}\_{in}‖ ) ∈ \[0, 1\].  
* **D11c. Viability/Task Relevance and Use U(A; τ\_w):** Relative drop in a maintained reference quantity Q when the dependence of A on E is broken by a marginal-preserving surrogate (e.g., time-shuffled sensory input):  
  U \= (Q\_int − Q\_dec) / (Q\_int − Q\_floor).  
  When A has an intrinsic viability variable v (D17), setting **Q \= v** defines *intrinsic relevance*. Otherwise Q is an external task score (*task-relative relevance*).  
* **D12. Agent (6-Tuple Criterion):** Subsystem A is an **agent on window τ\_w** iff all six conditions exceed their thresholds:  
  I(A) \> θ\_I,   T\_pers(A) \> θ\_T,   A(A; τ\_w) \> θ\_A,   Inf \> θ\_Inf,   Cl \> θ\_Cl,   U \> θ\_U.  
  * **Intrinsic Agent:** Passes D12 with Q \= v (intrinsic viability stake).  
  * **Task-Relative Agent:** Passes D12 with an externally supplied task objective Q.

```py
# Reference Python / PyTorch Evaluation of the 6-Tuple Agency Criterion (D9-D12)
def evaluate_agency_d12(
    I_integration: float, T_pers: float,
    delta_int_norm: float, delta_env_norm: float,
    err_model: float, err_random_relief: float,
    delta_in_from_act: float, delta_in_from_ext: float,
    Q_intact: float, Q_decoupled: float, Q_floor: float,
    thresholds: dict
) -> dict:
    A_do = delta_int_norm / (delta_int_norm + delta_env_norm + 1e-12)
    Inf  = max(0.0, 1.0 - err_model / (err_random_relief + 1e-12))
    Cl   = delta_in_from_act / (delta_in_from_act + delta_in_from_ext + 1e-12)
    U    = (Q_intact - Q_decoupled) / (Q_intact - Q_floor + 1e-12)

    is_agent = (
        I_integration > thresholds["I"]
        and T_pers > thresholds["T_pers"]
        and A_do > thresholds["A_do"]
        and Inf > thresholds["Inf"]
        and Cl > thresholds["Cl"]
        and U > thresholds["U"]
    )
    return {"I": I_integration, "T_pers": T_pers, "A_do": A_do, "Inf": Inf, "Cl": Cl, "U": U, "is_agent": is_agent}
```

## **5.3. Taxonomic Comparison Across Systems**

| System | Integration I | Persistence T\_pers | Autonomy A(τ\_w) | Loop (Inf / Cl / U) | Classification under D12 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **Cloud of gas** | Low | Short | \~0 (macro) | 0 / 0 / 0 (no relief R) | **Not an agent** (driven externally) |
| **Chaotic Random RNN (g \> 1\)** | High | Long | \~1 (h\_KS \> 0\) | Inf ≈ 0, Cl \= 0, U \= 0 | **Not an agent** (Negative Control 1: isolated chaos) |
| **Passive OU Markov Blanket** | High | Long | Low–Mod | Inf \> 0 (via σ), Cl \= 0, no stake v | **Not an agent** (Negative Control 2: passive physical filter) |
| **Trained Passive Classifier** | High | Long | Low | Inf high, Cl \= 0, U high (task) | **Not an agent** (open-loop feed-forward evaluator) |
| **Thermostat** | High (1D) | Long | Low | Inf low (n=0 rule), Cl high, U high (ext) | **Minimal task-relative agent** (near-zero capacity) |
| **Deployed LLM (single API call)** | High in S | Call window | Moderate | Inf high in S, Cl ≈ 0 in 1 call, U ext | **Open-loop proposer** on a single-call window |
| **LLM in Agentic Loop \+ Tools/Memory** | High in S | Multi-turn | Higher | Inf high, Cl \> 0 via tools/user, U ext | **Task-relative agent** on conversation/episode windows |
| **Biological Animal / Human** | High (P+S) | Lifetime | High | All high; U grounded in viability v | **Intrinsic agent** (human adds rich self/other-models M, O) |

# **6\. Plasticity, Self-Model, Write-Back, Other-Model, and Stake**

## **6.1. Formal Definitions (D13–D17)**

* **D13. Operational Plasticity Π\_plast:** Rate `‖ΔR‖ / unit of experience` at which the relief R updates during operation across three time scales: *fast* (activations/context only, ΔR \= 0), *medium* (online weight/memory updates), and *slow* (sleep consolidation / continual fine-tuning).  
* **D14. Self-Model M and Recursion:** A subspace M ⊂ Z holding an approximate model of the current state of Z (including M itself), fed back into the transition loop. Candidate functional role: separating self-caused sensory changes (`Act_A → S_A`) from external changes (`E → S_A`).  
* **D14a. Write-Back Predicate W(A, τ\_w) (Condition C2):** Fix subsystem boundary B\_A and window τ\_w, and let R\_k be the persistent structure inside B\_A at the start of window k. Write-back holds iff all three conditions are satisfied:  
  1. *Own operation:* `R_{k+1} ≠ R_k`, and the change is caused by A's own internal processing during window k (intervening on A's processing alters `R_{k+1}`);  
  2. *Cross-window persistence:* The modification survives across the window boundary into window k \+ 1;  
  3. *Causal conditioning:* Reverting `R_{k+1} → R_k` alters A's state trajectory in window k \+ 1\.  
     *(Engineering consequence: For the boundary "frozen LLM weights only", W \= False. For the boundary "LLM \+ agentic scaffold \+ persistent episodic/invariant store" such as CPSA's `GameInvariantStore`, W \= True whenever the agent writes verified laws that condition subsequent levels\!)*  
* **D15. Other-Model O\_B and Modeling Hierarchy (E / M / O):** A subspace O\_B ⊂ Z\_A modeling another agent B. Defines three distinct modeling targets: **E-level** (environment physics & generalized motion orders), **M-level** (self-model), and **O-level** (other agents' internal relief).  
* **D15a. Directed Coupling Coup(A → B):** Holds on window τ\_w iff (i) a finite-capacity channel exists between A and B, (ii) B recovers structure of A *strictly beyond* their shared prior I(Z\_A; Z\_B), and (iii) the recovered structure causally alters B's trajectory or persistent relief R\_B. Coupling is asymmetric: `Coup(A → B)` does not imply `Coup(B → A)`.  
* **D16. Memory as Finite-Resolution Stored Model:** Any persistent structure written back into R at resolution ν (bits per structure) that remains correlated with a past state of A or another agent B. Remembering is lossy reconstruction from R, unifying personal episodic memory and models of other agents into one mechanism (§8.7).  
* **D17. Viability Stake v (Ontological vs. Simulated):** A carrier viability variable v whose irreversible degradation penalizes or dissolves the system. We distinguish **ontological stake** (where losing v physically destroys the carrier hardware/organism) from **simulated stake** (where v is a programmed survival meter whose depletion terminates an RL episode, as tested in P3 and P9).

## **6.2. Candidate Conditions for Consciousness-Like Organization (C1–C3)**

Built on top of the 6 agency criteria (D12):

* **C1 (Self-Model M):** Active recursive self-representation.  
* **C2 (Write-Back W(A, τ\_w) from M):** Self-model outputs are written back into persistent relief R across windows (required for a *continuous self over time*, though not for momentary experience, as shown by anterograde amnesia; Thesis T7).  
* **C3 (Viability Stake v):** Grounds intrinsic normativity and deepens P-layer attractors.

# **7\. Capacity, Attractor Dimension, and Diffeomorphism Invariance**

## **7.1. Why Linear Covariance Dimension (PR) Can Be Fooled ("Linear Equivalence")**

In ML, practitioners often estimate representation dimensionality using the **Participation Ratio** of the activation covariance matrix C:

PR \= (tr C)² / tr(C²).

However, PR measures only the linear subspace spanned by the point cloud and is **not invariant under nonlinear coordinate transformations**. Worse, by the **linear equivalence theorem** (Clark, 2026; Shen & Hu, 2025), a strongly chaotic nonlinear network (λ\_1 \> 0\) and a globally stable noise-driven linear network (λ\_1 \< 0\) can have the **exact same stationary covariance spectrum and identical PR**\!

To measure intrinsic dynamical richness on the relief R, we must pair PR with **diffeomorphism-invariant tangent-space quantities** derived from the Lyapunov spectrum λ\_1 ≥ ... ≥ λ\_N (with cumulative density F'(s)):

1. **Kaplan–Yorke Attractor Dimension (D\_KY):**  
   D\_KY \= j \+ (∑\_{i=1}^j λ\_i) / \|λ\_{j+1}\|   ⟺   D\_KY / N \= 1 − F(s\_KY)   with   ∫\_{s\_KY}^∞ s F'(s) ds \= 0\.  
2. **Kolmogorov–Sinai Entropy Rate (Pesin's Formula):**  
   h\_KS / N \= ∫\_0^∞ s F'(s) ds \= (1 / N) ∑\_{λ\_i \> 0} λ\_i.

Comparing `PR / N` (linear embedding dimension) against `D_KY / N` (intrinsic attractor dimension) reveals how nonlinearly the attractor manifold is folded inside the ambient layer space Z.

# **8\. Inter-Agent Channel, Kernel-Inclusion Gate, and Recoverability**

## **8.1. The Information-Theoretic Recoverability Bound**

Suppose Agent A (latent Z\_A) transmits signals X^n across n uses of a memoryless channel of capacity C bits/use to Agent B (latent Z\_B), which forms a structural estimate Z\_hat\_A \= f(Y^n, Z\_B). By the data-processing inequality and chain rule of mutual information:

I(Z\_A; Z\_hat\_A) ≤ I(Z\_A; Z\_B) \+ n C.

* **First term `I(Z_A; Z_B)` (Shared Prior):** Alignment that B already shares with A before a single token is sent—due to shared training corpora, shared physical laws, or shared architecture.  
* **Second term `n C` (Channel Throughput):** New structural information transmitted during interaction. *(Note: Interactive querying by B does not increase the memoryless capacity bound nC, but allows B to allocate those nC bits to maximally informative subspaces of Z\_A\!)*

## **8.2. Linear-Gaussian Boundary Limit: The Synchronization Map and Kernel Inclusion (§8.3a)**

Consider the local Gaussian steady state (or Laplace approximation around an attractor mode) where external state η (e.g., the task-relevant subspace of Z\_A), interface state b ∈ B, and internal state μ (of Z\_B) have joint covariance Σ \= Π⁻¹ with Markov blanket Π\_{ημ} \= 0\. The conditional expectations given boundary observation b are:

η\_bar(b) \= E\[η \| b\] \= Σ\_{ηb} Σ\_b⁻¹ b,   μ\_bar(b) \= E\[μ \| b\] \= Σ\_{μb} Σ\_b⁻¹ b.

**Lemma 8.1 (Kernel-Inclusion Condition for Lossless Boundary Synchronization; Da Costa et al., 2021, Lemma 2.3).** A linear synchronization map `σ: Im(μ_bar) → Im(η_bar)` satisfying `σ(μ_bar(b)) = η_bar(b)` for all b ∈ B exists if and only if every boundary variation collapsed into the receiver's internal projection kernel also lies in the external projection kernel:

∃ σ : σ(μ\_bar(b)) \= η\_bar(b)   ⟺   ker(Σ\_{μb}) ⊂ ker(Σ\_{ηb})   ⟺   ker(Π\_{μb}) ⊂ ker(Π\_{ηb}).

When this inclusion holds, `σ(μ) = Σ_{ηb} Σ_{μb}^− μ = Π_η⁻¹ Π_{ηb} Π_{μb}^− Π_μ μ` (via the Moore–Penrose pseudoinverse), and the expected internal state minimizes precision-weighted prediction error:

μ\_bar(b\_t) \= argmin\_μ (1/2) (σ(μ) − η\_bar(b\_t))ᵀ Π\_η (σ(μ) − η\_bar(b\_t)).

**Connection to MBEL and the Boundary Projection Theorem:**  
This is the exact Gaussian boundary realization of the repository's universal **kernel-inclusion law** `ker(π_int) ⊆ ker(π_ext)` (*Boundary Projection Theorem*, §3.2; *Spectral Realization of V\_4*, Prop 2.1). If `ker(Π_{μb}) ⊄ ker(Π_{ηb})`, Agent B's sensory encoder projects external distinctions into `OMIT`, causing permanent representational blindness even as channel time `nC → ∞`\!

# **9\. Core Theses of the Framework (T1–T13)**

* **T1 (Two classes of Q-structures):** S-qualia are abstract/semantic; P-qualia are bodily/homeostatic and more individual-specific (`FOLLOW` by definition; coupling is `UNDECIDED`, P1–P2).  
* **T2 (Depth from stake \+ solenoidal acceleration):** Stake deepens P-attractors (`D(U), κ(U)`), while solenoidal flow `Q ≠ 0` accelerates return at the cost of damped oscillations (`FOLLOW` for math of Q ≠ 0; `UNDECIDED` for stake depth, P3 & P10).  
* **T3 (Bounded reasoning budget ρ):** P-maintenance and S-reasoning compete for finite ρ (`FOLLOW` for bound; `UNDECIDED` that deep S usually suppresses P; `NULL` that it *always* must).  
* **T4 (Shared abstract geometry between humans and LLMs):** LLM and human S-spaces overlap in relational geometry (RSA/CKA), without implying identical subjective experience (`UNDECIDED`, P1).  
* **T5 (What a deployed LLM lacks):** Frozen text LLMs lack a direct P-layer and viability stake v; adding simulated stake to embodied/RL agents is predicted to deepen P-basins (`FOLLOW` for architecture; `UNDECIDED` for deepening, P3).  
* **T6 (Truncated recursion vs. scaffold write-back):** In-context CoT provides C1 without weight write-back (`W = False` for weights boundary), whereas a verified external memory store inside a declared agent boundary can satisfy C2 (`FOLLOW` by D14a).  
* **T7 (Candidate sufficiency for continuous self):** Agency \+ C1 \+ C2 suffices for continuous-self organization, and C3 adds bodily depth (`UNDECIDED`). Three naive claims are refuted (`NULL`): C2 alone suffices; C2 is necessary for momentary experience (refuted by anterograde amnesia); Q-structures alone suffice.  
* **T8 (Agency is the 6-tuple D12, not N, chaos, or a passive Markov blanket):** Excludes gas clouds, Sompolinsky chaotic RNNs (`g > 1`), and passive OU Markov blankets (`FOLLOW` by D12; empirical separation tested in P6).  
* **T9 (Unity is graded integration I(A) \> θ\_I):** Tested in P2 (`UNDECIDED`).  
* **T10 (Recoverability bound \+ kernel-inclusion gate):** `I(Z_A; Z_hat_A) ≤ I(Z_A; Z_B) + nC` gated by `ker(Π_{μb}) ⊂ ker(Π_{ηb})` (`FOLLOW` mathematically; empirical factors tested in P7).  
* **T11 (Requisite capacity across active motion orders):** `C(B) ≥ C_eff(A | task)` across untruncated generalized motion orders `k ≤ n(τ_w)` (`UNDECIDED`, P8).  
* **T12 (Unified mechanism of memory and other-modeling):** Both are finite-resolution write-back into R (`UNDECIDED`).  
* **T13 (Directed coupling):** `Coup(A → B)` requires recovery beyond shared prior plus causal use (`FOLLOW` by D15a).

# **10\. Four Axes of Empirical Comparison Across AI & Biological Systems**

| Axis | What It Measures | Concrete Estimators for ML Engineers |
| :---- | :---- | :---- |
| **Axis A: Dimension Profile d(ε) & (D\_KY, PR)** | Active directions across spatial scales ε; intrinsic nonlinear attractor dimension vs. linear PCA embedding dimension. | Correlation integral slope d(r), TwoNN, linear Participation Ratio `PR`, and invariant Kaplan–Yorke dimension `D_KY` \+ entropy rate `h_KS` via tangent QR or `F(s) = tr R^{vv} / N`. |
| **Axis B: Attractor Depth D(U), Contraction κ(U), & Solenoidal Ratio ‖Q‖/‖Γ‖** | Basin escape threshold, local transverse stiffness in E^s, and circulatory acceleration of return. | Activation perturbation threshold `D(U)` and return time `τ_ret(U)`; negative Lyapunov integral `κ(U) = −∫_{−∞}^0 s F'(s) ds`; skew-to-symmetric drift ratio `‖Q‖_F / ‖Γ‖_F`. |
| **Axis C: Plasticity Π\_plast & Write-Back W** | Rate at which experience modifies persistent relief R across time scales. | `‖ΔR‖` per step across fast/medium/slow scales; three-step causal write-back verification test (D14a). |
| **Axis D: Autonomy & Closed Loop Profile (A, Inf, Cl, U)** | Internal vs. external trajectory control and closed viability/task loop across windows τ\_w. | Standardized 1-SD interventions on internal state (along E^u vs. E^s), actions, and environment inputs; time-shuffled surrogate decoupling for Use U. |

# **11\. System Comparison Matrix & Intermediate Architectures**

*(See §5.3 for the 8-system agency table.)*  
**Three Crucial Intermediate Cases in Modern AI:**

1. **Multimodal & Embodied Foundation Models:** Possess both P and S representations without ontological stake; serve as the primary testbed for cross-layer integration I(A) (Prediction P2).  
2. **Agentic LLM Scaffolds with Persistent Memory:** Evaluated strictly relative to the declared subsystem boundary (D14a). For the boundary `weights θ only`, `W = False`. For the boundary `LLM + tool harness + persistent memory store`, `W = True` if and only if writes are generated by the agent's own loop, persist across episodes/levels, and causally steer future trajectories.  
3. **Verifier-Centered Architecture (UIM v2.0 / CPSA 2.2):** Couples a programmatic/latent P-world-model with an S-proposer through an explicit **four-valued MBEL Judge (`FOLLOW`, `OMIT`, `UNDECIDED`, `NULL`)**. Unlike continuous free-energy agents (Da Costa et al., 2021\) that absorb arbitrary contradictions as smooth gradient shifts, a certified `NULL` immediately halts commitment and triggers hypothesis repair.

# **12\. Structural Homology with the Repository Corpus**

| Repository Concept | Canonical Document | Counterpart in LAF v2.1 | Mathematical / Architectural Link |
| :---- | :---- | :---- | :---- |
| Recursive self-correction under external verification | *Algorithm* §10; *MBEL* §§1–5 | Agency (D12) \+ Self-model (C1) \+ Verified Write-back (C2) | External `V_4` certification prevents self-model write-back from drifting into wireheading/hallucination. |
| Irrelevance as the kernel of coarse-graining (`OMIT`) | *Boundary Projection Theorem* §1; *Spectral V\_4* §§1–2 | Dichotomy projector `P_s` onto decaying subspace `E^s`; truncation of motion orders `k > n(τ_w)`; boundary inclusion `ker(Π_{μb}) ⊂ ker(Π_{ηb})` | Fast-decaying transverse modes and truncated motion derivatives fall into the coarse-graining kernel. |
| Thermodynamic cost of compression & control | *Algorithm* §9.4; *VIM* §2 | Bounded reasoning budget `ρ` (D8); transverse contraction `κ(U)` | Maintaining `κ(U) > 0` against diffusion noise `Γ` requires continuous entropy export across `B_A`. |
| Four-valued verdict standard `V_4` | *MBEL* §4; *Boundary Projection Theorem* §2 | Thesis evaluation table in §16 | Used verbatim (`FOLLOW`, `OMIT`, `UNDECIDED`, `NULL`). |

# **13\. Experimental Program: Ten Falsifiable Predictions (P1–P10)**

All ten predictions below can be executed on open-weights neural networks, simulated RL agents, and public neural datasets:

| ID | Testable Prediction | Explicit Refutation Criterion (When is it NULL?) |
| :---- | :---- | :---- |
| **P1** | **Human–LLM S vs. P Alignment:** RSA/CKA similarity between LLM embeddings and human neuroimaging data is significantly higher for abstract S-concepts than for bodily/interoceptive P-concepts. | No difference (or reverse ordering) after controlling for word frequency and concreteness. |
| **P2** | **Cross-Layer Integration in Multimodal/Embodied Models:** Jointly trained multimodal/embodied models exhibit significantly higher P–S mutual predictability and integration I(A) than separately trained unimodal encoders. | Cross-layer integration is indistinguishable from stitchings of frozen unimodal models. |
| **P3** | **Simulated Stake Deepens Attractors:** Adding an irreversible viability variable v (simulated stake) to an RL agent increases basin escape threshold D(U) and transverse Lyapunov contraction κ(U) compared to a dense-reward baseline of matched episode length. | No significant increase in D(U) or negative Lyapunov integral κ(U) \= −∫\_{−∞}^0 s F'(s) ds. |
| **P4** | **Invariant (D\_KY, PR) Separation:** The scale profile d(ε) and ratio `(D_KY / N, PR / N)` separate LLMs, physics world models, and embodied agents; crucially, `D_KY` separates nonlinear chaotic attractors from covariance-matched stable linear controls where `PR` is blind. | `(D_KY / N, PR / N)` profiles fail to separate model classes or linear-equivalence controls. |
| **P5** | **Coarse-to-Fine Training Consolidation:** Across training checkpoints, coarse-scale geometric structure forms before fine-scale structure, while initial random chaotic directions (λ\_i \> 0 with Inf ≈ 0\) are compressed into lower-dimensional task attractors (D\_KY decreases). | Fine-scale structure forms first, or D\_KY expands randomly without suppressing uninformative chaos. |
| **P6** | **The 6-Tuple Agency Criterion Separates Negative Controls:** On the test suite of §13.3, D12 cleanly separates adaptive RL/agentic systems from (i) gas clouds (Inf \= 0), (ii) Sompolinsky chaotic RNNs at g \> 1 (A^do ≈ 1, D\_KY \> 0, but Inf \= Cl \= 0), and (iii) passive stationary OU Markov blankets (Inf \> 0 via σ, but Cl \= 0 and no stake v). | D12 ordering reduces to N, D\_KY, h\_KS, or stationary free-energy minimization, or admits any of the three negative controls alongside genuine agents. |
| **P7** | **Recoverability Bound & Kernel-Inclusion Gate:** Inter-model recoverability Rec(A → B) grows with shared prior I(Z\_A; Z\_B) and channel throughput nC, stays below `I(Z_A; Z_B) + nC`, is higher for interactive querying than passive listening, and **collapses on subspaces where `ker(Π_{μb}) ⊄ ker(Π_{ηb})`**. | Rec(A → B) fails to drop when `ker(Π_{μb}) ⊄ ker(Π_{ηb})` or shows no gain from interactive querying at fixed nC. |
| **P8** | **Requisite Capacity Threshold Across Motion Orders:** When receiver capacity C(B) drops below sender complexity C\_eff(A) (tracked by D\_KY, h\_KS, and active generalized motion order n(τ\_w)), Rec(A → B) saturates at a low ceiling even as nC → ∞. | Recoverability continues to scale to 1.0 regardless of receiver bottleneck C(B) \< C\_eff(A). |
| **P9** | **Stake Elevates Long-Horizon On-Manifold Autonomy:** Adding viability stake v to an RL agent increases interventional autonomy `A^do(τ_w)` along active manifold directions (`E^u`) at long windows τ\_w (at matched Inf and Cl). | No increase in long-window on-manifold autonomy `A^do(τ_w)`. |
| **P10** | **Solenoidal Acceleration & Damped Oscillations:** In continuous-time or recurrent latent models at fixed stationary covariance Σ \= Π⁻¹ and fixed transverse contraction κ(U), increasing the solenoidal-to-dissipative ratio `‖Q‖_F / ‖Γ‖_F` **decreases return time τ\_ret(U)** after perturbation while **inducing damped oscillations** in instantaneous prediction error / free energy (D5a). | Return time τ\_ret(U) is minimized at pure gradient flow Q \= 0, or strong solenoidal flow ‖Q‖\_F ≫ ‖Γ‖\_F produces monotonic non-oscillatory decay. |

**Execution Priority for Engineers:**  
Start with **P4, P5, P6, and P10**—they require zero large-scale training and run directly on existing checkpoints, Sompolinsky random RNNs, and exact linear Ornstein–Uhlenbeck Markov-blanket baselines.

# **14\. The Explicit Boundary: Bracketing the Hard Problem**

This framework translates structural questions about agency and self-modeling into measurable dynamical and information-theoretic quantities, and stops deliberately before the hard problem of subjective experience. Knowing that an agent satisfies D12 \+ C1–C3, or that Agent B recovers 95% of Agent A's relational geometry, says nothing about why passing through a Q-structure feels like anything from the inside. Similarly, while self-model write-back (reading R and modifying R) shares a formal self-referential loop structure with the observer problem in physics, it is ordinary classical self-modification of weights/memory—no quantum-measurement isomorphism is claimed.

# **15\. Technical Objections, Edge Cases, and Limitations (15.1–15.15)**

1. **D6 ("Quale") is broad by design (§15.1):** Every trained network has attractor basins (Q-structures); D6 marks the structural slot in Z without claiming phenomenal experience.  
2. **Choice of Dependence Measure `Dep` in D9 (§15.2):** Mutual information, transfer entropy, and causal emergence can rank borderline architectures differently; candidate measures must be benchmarked against the negative controls of P6.  
3. **Observer-Relative Choice of Scale `(φ_A, τ_w)` (§15.3–15.5):** Integration I(A), autonomy A(τ\_w), and generalized-motion truncation order n(τ\_w) depend on the declared coarse-graining and time window. Reporting values without stating `(φ_A, τ_w)` is meaningless.  
4. **Borrowed vs. Intrinsic Normativity and Simulated vs. Ontological Stake (§15.6):** Without stake v, Use U is defined only relative to an external task loss (or an externally fixed precision matrix Π in a stationary Gaussian blanket). In RL simulations (P3, P9), a programmed survival variable v is a sparse terminal constraint that does not physically melt the GPU; P3 tests whether simulated stake suffices to reproduce deep basin geometry.  
5. **Infinitesimal Lyapunov Contraction vs. Finite Basin Width under "Stable Chaos" (§15.7):** Because λ\_1 \< 0 measures infinitesimal perturbations while spiking or piecewise-linear networks can exhibit "stable chaos" (sensitive to finite kicks δ), Axis B always pairs tangent contraction κ(U) with finite-perturbation escape threshold D(U).  
6. **Indirect Human Observability (§15.8) & Convergent Representations (§15.9):** Full Jacobians M(n) are accessible in artificial models but not in human fMRI/EEG; furthermore, Platonic representation convergence (Huh et al., 2024\) can mimic P2/P7 unless stake (P3, P9) and capacity/kernel rank (P7, P8) are manipulated independently.  
7. **Idealized Channel & Gaussian Blanket Assumptions (§15.10–15.11):** The bound `I(Z_A; Z_B) + nC` assumes a memoryless channel, and `ker(Π_{μb}) ⊂ ker(Π_{ηb})` is exact in the linear-Gaussian / local Laplace limit, serving as local ceiling conditions for multimodal nonlinear agents.  
8. **Boundary-Dependence of Write-Back C2 (§15.14–15.15):** By D14a, the exact same physical LLM is `C2 = False` for the boundary "frozen weights θ" and `C2 = True` for the boundary "weights \+ agentic scaffold \+ persistent verified store." This is a direct, intended consequence of functionalism (A1–A2).

# **16\. Self-Assessment Table Under the Canonical V\_4 Standard**

Evaluated under the normative calculus (*Modified Brusentsov Entailment Logic*, §4): `FOLLOW` (proven mathematically from definitions/assumptions or describes existing engineering), OMIT (orientation only), UNDECIDED (empirical hypothesis awaiting P1–P10), `NULL` (refuted/rejected).

| Claim of This Document | V\_4 Verdict | Basis / Reference |
| :---- | :---- | :---- |
| Consistency of definitions D1–D19, D2a, D5a, D11a–c, D14a, D15a; separation of relief R and budget ρ | **FOLLOW** | Formal definitions (§§3–10); bounded compute envelope |
| In a Gaussian steady state p \= N(0, Π⁻¹), Markov blanket η ⊥ μ \| b is equivalent to Π\_{ημ} \= 0 while generally Σ\_{ημ} ≠ 0 | **FOLLOW** | Block matrix inversion (D2a; Da Costa et al., 2021\) |
| Linear synchronization map σ(μ\_bar(b)) \= η\_bar(b) exists at Gaussian steady state iff `ker(Σ_{μb}) ⊂ ker(Σ_{ηb}) ⟺ ker(Π_{μb}) ⊂ ker(Π_{ηb})` | **FOLLOW** | Linear preimage inclusion (Lemma 8.1; Da Costa et al., 2021, Lemma 2.3) |
| Smooth stationary diffusion drift splits uniquely into dissipative f\_rev (Γ ⪰ 0\) and divergence-free solenoidal f\_irrev (Q \= −Qᵀ) | **FOLLOW** | Helmholtz decomposition for stationary Fokker–Planck equations (D5a; Pavliotis, 2014\) |
| Non-zero solenoidal flow Q ≠ 0 accelerates convergence to stationary density relative to pure gradient flow Q \= 0 at fixed Γ, and induces damped oscillations when ‖Q‖ ≫ ‖Γ‖ | **FOLLOW** | Spectral gap inequalities for non-reversible Langevin diffusions (Lelièvre et al., 2013; Rey-Bellet & Spiliopoulos, 2015\) |
| Multi-exponential stationary Gaussian boundary processes admit a Markovian integrator chain of generalized coordinates `s_tilde_t = (s_t^(0), ..., s_t^(n))` | **FOLLOW** | Doob's theorem & stochastic realization theory (§4.4; Lindquist & Picci, 1985, 2015\) |
| Deployed text LLMs do not update weights θ at inference, lack a direct P-layer and stake v, and have C2 \= False for the weights-only boundary | **FOLLOW** | Architectural fact of standard deployment; D14a |
| Lyapunov spectrum `{λ_i}`, `F(s)`, `D_KY`, `h_KS` are diffeomorphism-invariant, whereas Participation Ratio `PR` is coordinate-dependent and blind to linear equivalence | **FOLLOW** | Smooth coordinate invariance of derivative cocycle; Clark (2026); Shen & Hu (2025) |
| Exact finite-N identity `F(s) = (1/N) tr R^{vv}_η(k+1, k)` via the minimum-norm tangent dichotomy projector | **FOLLOW** | Exact identity for s ∉ {λ\_i} (D7; Clark, 2026\) |
| Information-theoretic recoverability bound `I(Z_A; Z_hat_A) ≤ I(Z_A; Z_B) + nC` on memoryless channels | **FOLLOW** | Data processing inequality & chain rule (§8.1) |
| Gas cloud, Sompolinsky chaotic random RNN (`g > 1`), and passive sensory-only OU Markov blanket are excluded from agency by D12 | **FOLLOW** | Gas has no R (`Inf = 0`); random RNN has `Inf = Cl = 0`; passive OU blanket has `Cl = 0` and no stake `v` (§5.1) |
| Degrees of freedom N, chaotic dimension D\_KY, entropy rate h\_KS, autonomy alone, or a passive stationary Markov blanket suffice for agency | **NULL** | Refuted by the three negative controls of §5.1 and §7.2 |
| C2 (write-back) is necessary for momentary experience, or C2 alone suffices, or Q-structures alone suffice | **NULL** | Refuted by anterograde amnesia, simple online filters, and universal presence of basins (T7) |
| Abstract S-thought *always* requires suppressing the P-layer | **NULL** | Counterexamples: spatial/kinesthetic mathematical reasoning (T3) |
| Empirical predictions P1–P10 (stake deepening, cross-layer integration, D12 separation stability, solenoidal return curves) | **UNDECIDED** | Require empirical execution of protocols in §13 |
| Parallel with the observer problem in physics | **OMIT** | Retained for conceptual orientation only (§14.2) |

# **17\. Summary of Explicit Non-Claims**

1. **No solution to the hard problem of consciousness (§14).**  
2. **No blanket label ("agent" or "not an agent") for LLMs without a stated time window τ\_w and subsystem boundary B\_A.**  
3. **No requirement for biological wetware (A1), while honestly noting the gap between simulated RL survival variables and physical hardware dissolution (§15.6).**  
4. **No claim that latent spaces come from quantum, electromagnetic, or gravitational fields.**  
5. **No claim that recovering an agent's latent structure reproduces its subjective experience (§8.8).**

# **18\. Synthesis: The End-to-End Agency and Coupling Chain**

```
Subsystem (A ⊂ C)
  ──► Coarse-Grained Latent Space Z_A (at spatial scale φ_A, truncating motion orders k > n(τ_w))
  ──► Learned Relief R (Helmholtz flow: dissipative pull Γ + solenoidal acceleration Q)
  ──► Informedness Inf > θ_Inf (gated at boundary by kernel inclusion: ker Π_{μb} ⊂ ker Π_{ηb})
  ──► Active Interventional Loop Closure Cl > θ_Cl & Viability/Task Use U > θ_U (grounded by stake v)
  ──► Informational Autonomy A^do(τ_w) > θ_A  ══►  [AGENT ON WINDOW τ_w (D12)]
  ──► Self-Model M (C1) + Cross-Window Verified Write-Back W(A, τ_w) (C2)
  ──► Other-Model O_B (bounded by I(Z_A; Z_B) + nC and requisite capacity C(A) ≥ C_eff(B))
  ──► Directed Inter-Agent Coupling Coup(A → B)
```

# **Appendix A: Quick Formula Reference Table for Engineers**

| Formula / Expression | Role in Framework | Engineering Meaning |
| :---- | :---- | :---- |
| `Z_A = φ_A(x_A)` | Definition (D3) | Coarse-grained latent state at spatial scale φ\_A |
| `Π_{ημ} = 0`, `Σ_{ημ} = −Π_η⁻¹ Π_{ηb} Σ_{bμ} ≠ 0` | Math Result (D2a) | Markov blanket: conditional independence coexists with long-range covariance |
| `ker(Π_{μb}) ⊂ ker(Π_{ηb}) ⟺ ∃ σ: σ(μ_bar(b)) = η_bar(b)` | Math Result (Lemma 8.1) | Boundary kernel inclusion prevents `OMIT` blindness across an interface |
| `f_R = (−Γ ∇U_R + ∇·Γ) + (−Q ∇U_R + ∇·Q)`, `Q = −Qᵀ` | Math Result (D5a) | Helmholtz decomposition into dissipative pull (Γ) and solenoidal circulation (Q) |
| `ds_t^(k) = f_k(s_t^(k), s_t^(k+1)) dt + ς_k dW_t^(k)` (`k ≤ n(τ_w)`) | Math Result (§4.4) | Generalized coordinates of motion truncated at temporal window τ\_w |
| `D(U) = inf { ‖δ‖ : z + δ does not return to U }` | Definition (D7) | Finite-perturbation basin escape threshold |
| `F(s) = lim_{η→0⁺} (1/N) tr R^{vv}_η(k+1, k)` | Math Result (D7) | Exact cumulative Lyapunov distribution from minimum-norm tangent response |
| `κ(U) = −∫_{−∞}^0 s F'(s) ds` | Metric (D7) | Mean transverse contraction rate in stable Oseledets subspace E^s |
| `D_KY = j + (∑_{i=1}^j λ_i) / |λ_{j+1}|`, `h_KS = ∑_{λ_i > 0} λ_i` | Invariants (D19) | Coordinate-invariant Kaplan–Yorke attractor dimension and KS entropy rate |
| `PR = (tr C)² / tr(C²)` | Proxy (D19) | Linear PCA participation ratio (coordinate-dependent; subject to linear equivalence) |
| `I(A) = min_{cuts} Dep(A_1 ↔ A_2) / Dep(A ↔ E)` | Criterion 1 (D9) | Informational integration of latent space Z\_A |
| `A^do_τ = E‖Δ_int‖ / (E‖Δ_int‖ + E‖Δ_env‖)` | Criterion 3 (D11) | Interventional informational autonomy on window τ\_w |
| `Inf = 1 − ε_A / ε_0` | Criterion 4 (D11a) | Informedness of relief R over randomized-weight baseline |
| `Cl = E‖Δ^{act}_{in}‖ / (E‖Δ^{act}_{in}‖ + E‖Δ^{ext}_{in}‖)` | Criterion 5 (D11b) | Interventional action-to-input loop closure |
| `U = (Q_int − Q_dec) / (Q_int − Q_floor)` | Criterion 6 (D11c) | Viability/task relevance via time-shuffled surrogate decoupling |
| `I(Z_A; Z_hat_A) ≤ I(Z_A; Z_B) + nC` | Bound (§8.1) | Inter-agent structural recoverability ceiling |
| `W(A, τ_w)` | Predicate (D14a) | Cross-window causal write-back into persistent relief R |

# **Appendix B: Primary Mathematical & Theoretical References**

1. **Bayesian Mechanics, Markov Blankets, Helmholtz Decomposition, and Generalized Coordinates:** Da Costa, L., Friston, K., Heins, C., & Pavliotis, G. A. (2021). Bayesian mechanics for stationary processes. *Proceedings of the Royal Society A*, 477(2256), 20210518; Pavliotis, G. A. (2014). *Stochastic Processes and Applications*. Springer; Graham, R. (1977). Covariant formulation of non-equilibrium statistical thermodynamics. *Zeitschrift für Physik B*, 26, 397–405; Lelièvre, T., Nier, F., & Pavliotis, G. A. (2013). Optimal non-reversible linear drift for the convergence to equilibrium of a diffusion. *Journal of Statistical Physics*, 152, 237–274; Rey-Bellet, L., & Spiliopoulos, K. (2015). Irreversible Langevin samplers and variance reduction. *Nonlinearity*, 28(7), 2081; Lindquist, A., & Picci, G. (1985, 2015). *Linear Stochastic Systems: A Geometric Approach to Modeling, Estimation and Identification*. Springer; Biehl, M., Pollock, F. A., & Kanai, R. (2021). A technical critique of some parts of the Free Energy Principle. *Entropy*, 23(3), 293\.  
2. **Lyapunov Spectrum of Neural Networks, Minimum-Norm Tangent Response, and Linear Equivalence:** Clark, D. G. (2026). Lyapunov spectrum of random neural networks. *arXiv:2610.12426*; Engelken, R., Wolf, F., & Abbott, L. F. (2023). Lyapunov spectra of chaotic recurrent neural networks. *Physical Review Research*, 5(4), 043044; Sompolinsky, H., Crisanti, A., & Sommers, H. J. (1988). Chaos in random neural networks. *Physical Review Letters*, 61(3), 259; Shen, J., & Hu, Y. (2025). Linear equivalence of covariance spectra in nonlinear recurrent networks.  
3. **Ergodic Theory, Attractor Dimension, and Dichotomy Projectors:** Oseledets, V. I. (1968). A multiplicative ergodic theorem. *Transactions of the Moscow Mathematical Society*, 19, 197–231; Kaplan, J. L., & Yorke, J. A. (1979). Chaotic behavior of multidimensional difference equations. *Lecture Notes in Mathematics*, 730, 204–227; Pesin, Y. B. (1977). Characteristic Lyapunov exponents and smooth ergodic theory. *Russian Mathematical Surveys*, 32(4), 55; Sacker, R. J., & Sell, G. R. (1978). A spectral theory for linear differential systems. *Journal of Differential Equations*, 27(3), 320–358.  
4. **Transient Chaos in Looped Latent Reasoning & Dynamical Similarity:** Lai, Z., Bao, Y., Quinn, C., & Gilpin, W. (2026). Transient chaos and fractal basins in latent reasoning. *arXiv:2609.04963*; Ostrow, M., Eisen, A., Kozachkov, L., & Fiete, I. (2023). Beyond geometry: Comparing the temporal structure of computation in neural circuits with Dynamical Similarity Analysis (DSA). *NeurIPS*.  
5. **Agency, Semantic Information, Empowerment, and Requisite Variety:** Ashby, W. R. (1956). *An Introduction to Cybernetics*; Conant, R. C., & Ashby, W. R. (1970). Every good regulator of a system must be a model of that system. *International Journal of Systems Science*, 1(2), 89–97; Kolchinsky, A., & Wolpert, D. H. (2018). Semantic information, autonomous agency and non-equilibrium statistical physics. *Interface Focus*, 8(6), 20180041; Barandiaran, X. E., Di Paolo, E., & Rohde, M. (2009). Defining agency: Individuality, normativity, asymmetry, and spatio-temporality in action. *Adaptive Behavior*, 17(5), 367–386; Krakauer, D., Bertschinger, N., Olbrich, E., Flack, J. C., & Ay, N. (2020). The information theory of individuality. *Theory in Biosciences*, 139, 209–223; Klyubin, A. S., Polani, D., & Nehaniv, C. L. (2005). Empowerment: A universal agent-centric measure of control. *IEEE Congress on Evolutionary Computation*.  
6. **Representational Geometry & Convergence:** Kriegeskorte, N., Mur, M., & Bandettini, P. (2008). Representational similarity analysis. *Frontiers in Systems Neuroscience*, 2, 4; Kornblith, S., Norouzi, M., Lee, H., & Hinton, G. (2019). Similarity of neural network representations revisited (CKA). *ICML*; Huh, M., Cheung, B., Wang, T., & Isola, P. (2024). The Platonic Representation Hypothesis. *ICML*.

