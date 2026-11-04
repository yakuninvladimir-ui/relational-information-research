# **The Law of Useful Information Structuring in Model Latent Spaces: Theory of Informational Minimal Surfaces**

**Author:** Vladimir Yakunin  
**Version:** 1.0 (ML Engineering Edition — full structural and mathematical fidelity)  
Date: 2026-09  
Document Status: Working theoretical specification (Reasoning layer): variational principle \+ upper surrogates (VIM) \+ mean curvature equation \+ NTK-filtered dynamics \+ operational protocol \+ explicit non-claims.  
Role in Repository: Variational theory of informational minimal surfaces in model latent spaces; continuous-space counterpart of the informational minimal-surface construction used in the Causal Phase Program (Physics/Causal\_Phase\_Program\_v4.md, §3.1; marked OMIT-context there). Defines the experimental verification program E1–E5.  
**Domain:** Information geometry, variational principles, neural tangent kernel (NTK) theory, latent representation learning.

# **Abstract & ML Engineering Intuition**

Why this document exists (for ML Engineers):  
How does a neural network organize its hidden-layer activations (latent space Z) during training? A common trap in theoretical ML is to borrow metaphors from general relativity—claiming that the network "bends the metric of latent space." That picture is backwards. The effective metric of the latent space is fixed externally by the task's probabilistic structure, the decoder/head, and hardware/architectural constraints. What the trainable encoder E\_θ actually controls is **how the data manifold Σ \= E\_θ(X) is embedded inside Z**.

Think of the embedded data manifold Σ as a **multidimensional soap film**:

* **Compression (Surface Tension):** Minimizing geometric volume pulls the representation tight, collapsing redundant and noisy directions.  
* **Predictive Power (External Pressure):** Preserving mutual information with the target I(E\_θ(X); Y) ≥ R\_task pushes outward, preventing the manifold from collapsing into a point.  
* **Equilibrium (Mean Curvature Balance):** Where the film settles, its mean curvature vector H(z) is balanced by the normal component of the predictive information gradient: H(z) \= λ (∇\_Z i(z))⊥.  
* **Practical Training (VIM Regularizer):** Standard Cross-Entropy (CE) loss only controls the information deficit; it does not directly penalize geometric volume. We derive a computable upper bound on Riemannian volume using the trace of the pullback metric (estimable in PyTorch via Jacobian-vector products and Hutchinson's trace estimator), yielding the Variational Information Metric (VIM) loss L\_VIM(θ).

# **0\. Objective and Conceptual Shift**

We formulate the law of structuring useful information in model latent spaces:

* **Minimal surfaces, not general relativity:** The geometric framework is minimal surface theory.  
* **External metric vs. trainable embedding:** The latent space metric is externally determined by the probabilistic structure of the task and system constraints. The trainable model (encoder E\_θ) does not bend space itself; rather, it selects an optimal embedding Σ \= E\_θ(X) of the data manifold into this environment.  
* **The soap-film balance:** The latent representation behaves like a multidimensional "soap film": the drive to compress information acts as surface tension (minimizing embedded volume), while the requirement to preserve predictive power acts as external directed pressure.

# **1\. Spaces and Dynamical Variables**

Let the core spaces and mappings be defined as follows:

* X: Input space (tokens, images, multimodal context).  
* Z: Ambient latent space (layer activations of dimension d, i.e., Z ⊆ ℝ^d).  
* E: X → Z: The encoder (a neural network parameterized by weights θ; also written E\_θ).  
* Σ \= E(X) ⊂ Z: The encoder image, an m-dimensional submanifold (possibly stratified) embedded in Z.

**Key architectural rule:** The dynamical variable of the theory is the image Σ (the embedding governed by the encoder weights θ), **not** the metric of the latent space Z.

## **1.1. Latent Space Metric: True Metric and Operational Approximations**

### **1.1.1. Status of the Metric**

In any practical ML experiment, we must strictly distinguish between two objects:

1. **The true effective metric (g\_true)** of the model's latent space, which is induced by the entire stack of physical, architectural, algorithmic, and informational constraints.  
2. **An operational metric approximation (g\_approx)**, which can be explicitly computed or estimated in code from activations, gradients, or a probe head.

### **1.1.2. True Effective Metric (g\_true)**

By g\_true we mean the effective geometry induced by four layers of constraints:

* **Physical:** Finite floating-point precision (fp32, fp16, bf16, fp8/fp4) and hardware noise, which set the lower cutoff of geometric resolution.  
* **Architectural:** Ambient dimension d, activation non-linearities (ReLU, GELU, SwiGLU), and normalization layers (LayerNorm, RMSNorm), which define the admissible class of embedded manifolds Σ.  
* **Algorithmic:** Optimizer dynamics (AdamW, SGD), learning rate schedules, and regularization/dropout, which govern reachable parameter regions and preferred trajectory directions.  
* **Informational:** Task requirements for predictive power, noise structure, and input redundancy.

The metric g\_true is not given in closed analytical form. Its existence does not imply that it is known or unique; it serves as the conceptual target motivating experimental approximations. Within a single experiment or the analysis of a fixed checkpoint, g\_true is treated as a fixed background. When the architecture, training phase, decoder, or hardware conditions change, g\_true may shift, while the dynamical variable under study remains the image Σ.

### **1.1.3. Operational Metric (g\_approx)**

Because g\_true cannot be evaluated in closed form, experiments compute all geometric quantities—volume, mean curvature, and information gradients—with respect to an operational approximation g\_approx:

Vol\_{g\_approx}(Σ),   H\_{g\_approx},   ∇\_{g\_approx} i.

Five concrete operational approximations are available for ML practitioners:

**Fisher Information Metric via an external decoder/probe:** Let P(Y \| z) := D(z), where D: Z → Δ(Y) is a task decoder or linear/MLP probe mapping latent states to target probability distributions (Amari, 2016):  
g^(D)\_{ij}(z) \= E\_{y \~ D(z)} \[ ∂\_i log D(y \| z) · ∂\_j log D(y \| z) \].

1. **Loss Hessian Metric:** Using the positive-definite (or Gauss-Newton) part of the task loss Hessian with respect to latent activations z:  
   g^(L)\_{ij}(z) \= E \[ ∂\_i ∂\_j L\_task(z, y) \].  
2. **Local Activation Covariance (Mahalanobis) Metric:** Using the regularized inverse local covariance C(z) of activations:  
   g^(cov)(z) \= ( C(z) \+ ε I )^(-1).  
3. **NTK-Induced Metric:** Built from the empirical neural tangent kernel Θ\_E of the encoder.  
4. **Graph Reconstruction Metric:** Built non-parametrically from k-NN local patches and local parallel transport / holonomies.

None of these approximations is declared canonical by default; the specific choice must be fixed in the experimental protocol.

### **1.1.4. Local Information Density and Distribution Consistency**

To evaluate local predictive information at a point z ∈ Z, we fix an operational decoder or probe D: Z → Δ(Y) so that P(Y \| z) := D(z). For the marginal target prior P(Y), one uses either the empirical dataset label distribution or the induced marginal distribution:

P\_bar\_D(Y) \= E\_{z \~ μ\_Σ} \[ D(Y \| z) \].

The choice is fixed in the protocol. If P(Y) is specified externally, the identity E\[i(z)\] \= I(E(X); Y) requires marginal consistency between P(Y) and P\_bar\_D(Y).

### **1.1.5. Robustness Requirement to Metric Selection**

Substantive geometric claims must not be artifacts of a single proxy metric. The experimental protocol requires evaluating diagnostic quantities (such as the curvature-gradient alignment coefficient r and normalized curvature \|H\|) across **at least two independent choices of g\_approx** (e.g., Fisher metric g^(D) and Mahalanobis covariance metric g^(cov)). If an effect persists across metrics, it is attributed to the underlying geometry; if it vanishes, it is treated as an approximation artifact.

## **1.2. Pushforward Distribution on Σ**

Mutual information is defined over the input distribution X \~ P\_X:

I(Σ; Y) := I(E(X); Y),   X \~ P\_X.

The probability measure on the embedded manifold Σ is the pushforward measure μ\_Σ \= E\_\* P\_X. Alongside the geometric support Σ, the measure μ\_Σ is part of the dynamical state of the representation.

# **2\. Global Variational Principle**

## **2.1. Constrained Optimization Formulation**

**Engineering Intuition:** An ideal encoder compresses the latent manifold Σ to occupy the smallest possible Riemannian volume in the task metric g\_I ≡ g\_approx while preserving at least R\_task bits of mutual information with the target Y (an Information Bottleneck constraint in geometric form; Tishby et al., 1999):

min\_{Σ ⊂ Z} Vol\_{g\_I}(Σ)   subject to   I(E(X); Y) ≥ R\_task.

## **2.2. Connection to ε-Capacity and Coding Complexity (Weyl's Formula)**

Why minimize Riemannian volume? By Weyl's asymptotic expansion (Weyl, 1911\) for the metric restricted to an m-dimensional manifold Σ (where the intrinsic dimension m \= dim(Σ) is typically much smaller than the ambient layer width d \= dim(Z)), the metric ε-entropy (packing capacity H\_ε) scales as:

H\_ε(Σ, g\_I\|Σ) ≈ Vol{g\_I}(Σ) / (c\_m · ε^m) \+ O(ε^(2 \- m)),

where c\_m is the volume of the m-dimensional unit ball. The leading term at fine resolution ε is proportional to Vol\_{g\_I}(Σ). Therefore, **minimizing the Riemannian volume of Σ is equivalent to minimizing the coding/predictive complexity of the representation at leading order**.

# **3\. Local Source and the Stationary State Equation**

## **3.1. Lagrangian and Local Information Density**

Introducing a Lagrange multiplier λ ≥ 0 for the information constraint gives the variational functional:

L\[Σ\] \= Vol\_{g\_I}(Σ) \+ λ ( R\_task − I(E(X); Y) ).

The local predictive information density at point z ∈ Z is the Kullback–Leibler divergence between the posterior and prior target distributions (Cover & Thomas, 2006):

i(z) \= D\_KL( P(Y \| z) \|\| P(Y) ),   where   E\_{z \~ μ\_Σ}\[ i(z) \] \= I(E(X); Y).

## **3.2. Stationary Euler–Lagrange Equation (Mean Curvature Balance)**

Under the fixed-density approximation (δ(dμ\_Σ) \= 0), taking the first variation δL / δΣ \= 0 with respect to normal deformations of the submanifold Σ ⊂ Z yields the fundamental stationary state equation:

H(z) \= λ ( ∇\_Z i(z) )⊥

where:

* H(z) ∈ N\_z Σ is the **mean curvature vector** (do Carmo, 1976\) of the embedded manifold Σ in the ambient latent space Z (the first variation of volume, pointing in the direction that shrinks surface area fastest);  
* (∇\_Z i(z))⊥ ∈ N\_z Σ is the **normal component** of the ambient gradient of local information density i(z) (orthogonal to the tangent space T\_z Σ);  
* λ is the Lagrange multiplier trading off compression against predictive accuracy.

**Geometric Reading for ML Engineers:**  
A flat submanifold has H(z) \= 0\. Why does a trained neural representation curve inside Z? Because shrinking volume pulls Σ flat (via H), except where bending into the normal bundle N\_z Σ increases predictive power i(z). At equilibrium, the inward "surface tension" H(z) is exactly counterbalanced by the outward "information pressure" λ(∇\_Z i(z))⊥.

## **3.3. Limitations of the Stationary Equation**

The balance H \= λ(∇ i)⊥ is the exact Euler–Lagrange condition of the **original** variational functional L\[Σ\]. In practical deep learning, we minimize differentiable upper surrogates rather than the exact Riemannian volume. Minimizing an upper surrogate controls the original functional only to the extent that the surrogate bound is tight; whether standard or VIM-regularized networks satisfy H \= λ(∇ i)⊥ is an empirical hypothesis tested in Experiments E1 and E5.

# **4\. Training Dynamics and Computable Surrogates: VIM and NTK Flow**

## **4.1. Upper Surrogates of the Variational Functional (VIM Loss)**

Standard Cross-Entropy (CE) loss is **not** equivalent to the geometric variational functional: CE penalizes only the predictive information deficit and leaves geometric volume unconstrained. To control both terms rigorously in PyTorch/JAX, we construct tractable upper bounds.

Let Z \= E\_θ(X), let D: Z → Δ(Y) be a decoder/probe, and let the cross-entropy loss be:

CE\_D(θ) \= E\_{(X, Y) \~ P} \[ −log D(Y \| Z) \].

### **4.1.1. Upper Bound on the Information Deficit**

Because CE\_D(θ) ≥ H(Y \| Z) (by non-negativity of KL divergence) and I(Z; Y) \= H(Y) − H(Y \| Z), the information deficit is strictly upper-bounded by:

\[ R\_task − I(Z; Y) \]*\+ ≤ \[ R\_task − H(Y) \+ CE\_D(θ) \]*\+,

where \[x\]\_+ \= max(0, x).

### **4.1.2. Upper Bound on Riemannian Volume (Generalized Dirichlet Energy)**

Suppose the input space is locally parameterized by an m-dimensional chart u ∈ M, and let J\_E(u) \= ∂E\_θ(u)/∂u ∈ ℝ^(d × m) be the encoder Jacobian. The pullback (induced) metric on M is the m × m matrix:

A\_θ(u) \= J\_E(u)ᵀ g\_I(E\_θ(u)) J\_E(u).

The exact Riemannian volume element is √(det A\_θ(u)) du. Computing determinants of Jacobians is expensive and numerically unstable when A\_θ is near-singular. However, by the **Arithmetic Mean–Geometric Mean (AM–GM) inequality** applied to the eigenvalues λ\_1, ..., λ\_m ≥ 0 of A\_θ(u), we have det(A\_θ)^(1/m) ≤ (1/m) tr(A\_θ), which yields a rigorous, smooth upper bound on the volume:

Vol\_{g\_I}(Σ\_θ) \= ∫\_M √(det A\_θ(u)) du ≤ Vol\_hat\_θ := ∫\_M ( tr A\_θ(u) / m )^(m/2) du.

* For m \= 2, Vol\_hat\_θ reduces to the classical **Dirichlet energy** (1/2) ∫ tr(A\_θ) du used in minimal surface theory.  
* For general intrinsic dimension m, the power (tr A\_θ / m)^(m/2) preserves scale homogeneity.  
* **Regularity assumptions:** This bound assumes a local continuous m-dimensional input parameterization and a smooth encoder E\_θ. For discrete inputs (such as tokens), one applies continuous embedding relaxation, local neighborhood smoothing, or k-NN graph differences. When expectation is taken over the empirical data distribution P\_X rather than a uniform chart measure du, Vol\_hat\_θ acts as a P\_X-weighted geometric complexity regularizer.

### **4.1.3. The VIM Loss Function and PyTorch Implementation**

Combining the cross-entropy bound, a lower-bound mutual information estimator I\_hat\_θ ≤ I(E\_θ(X); Y), and the volume surrogate Vol\_hat\_θ bounds the variational functional:

F(θ) ≤ F\_hat(θ) \= Vol\_hat\_θ \+ λ \[ R\_task − I\_hat\_θ \]\_+.

This gives the practical **Variational Information Metric (VIM) training objective**:

L\_VIM(θ) \= CE\_D(θ) \+ α · Vol\_hat\_θ \+ β · \[ R\_task − I\_hat\_θ \]\_+,

where α \> 0 controls geometric volume compression and β ≥ 0 enforces the information floor.

**PyTorch Implementation Sketch (Hutchinson Trace Estimator for Vol\_hat\_θ):**

```py
import torch
from torch.func import jvp

def compute_vim_volume_surrogate(encoder, x, metric_fn, m_dim: int, n_probes: int = 4):
    """
    Estimates Vol_hat_θ = E_x [ (tr(J_E^T g_I J_E) / m)^(m/2) ]
    using Rademacher random probes and forward-mode AD (jvp).
    """
    z = encoder(x)  # [B, d]
    g_mat = metric_fn(z).detach()  # [B, d, d] operational metric g_approx (stop-grad on background metric)
    
    trace_est = torch.zeros(x.shape[0], device=x.device)
    for _ in range(n_probes):
        v = torch.randint(0, 2, x.shape, device=x.device, dtype=x.dtype) * 2.0 - 1.0
        _, jv = jvp(encoder, (x,), (v,))  # jv = J_E @ v, shape [B, d]
        # Quadratic form v^T J_E^T g_I J_E v
        quad = torch.einsum("bi,bij,bj->b", jv, g_mat, jv)
        trace_est = trace_est + quad / n_probes

    return torch.mean(torch.clamp(trace_est / max(1, m_dim), min=1e-8) ** (0.5 * m_dim))
```

### **4.1.4. Limitations of Surrogate Bounds**

Because AM–GM holds with equality only when all eigenvalues of A\_θ(u) are equal (conformal/isometric embedding), Vol\_hat\_θ can be loose when singular values of J\_E are highly anisotropic. Minimizing L\_VIM(θ) guarantees approximate minimization of the true variational functional only when the surrogate gap F\_hat(θ) − F(θ) remains controlled.

## **4.2. Training Dynamics Filtered by the Neural Tangent Kernel (NTK)**

During gradient descent in weight space θ, the embedded manifold Σ\_t \= E(X; t) does not deform freely in Z; every point displacement must be realizable by a weight update Δθ. Consequently, the geometric variational force

F\_var(x) \= H(x) − λ ( ∇\_Z i(x) )⊥

is filtered through the encoder's empirical **Neural Tangent Kernel (NTK)** (Jacot et al., 2018):

∂E(x; t) / ∂t \= −η ∫\_Σ Θ\_E(x, x'; t) · ( H(x') − λ (∇\_Z i(x'))⊥ ) dμ\_Σ(x'),

where:

* Θ\_E(x, x'; t) \= ⟨ ∇\_θ E(x; t), ∇\_θ E(x'; t) ⟩\_Θ \= J\_θ E(x) · J\_θ E(x')ᵀ is the d × d matrix-valued empirical tangent kernel of the encoder;  
* η \> 0 is the learning rate;  
* integration is performed over the pushforward data measure dμ\_Σ(x').

**Equilibrium condition:** Training stops deforming the manifold either when the variational force vanishes (H(x) \= λ(∇\_Z i(x))⊥, true geometric optimum) or when the residual force F\_var lies entirely in the **null space of the integral operator Θ\_E** (architectural bottleneck: the network weights lack the expressivity to bend Σ further).

# **5\. Experimental Verification Program (E1–E5)**

To test this theory on real checkpoints (LLMs, vision encoders, world models), we define five falsifiable protocols:

## **E1. Curvature Projection onto the Information Gradient (Stationarity Check)**

* **Method:** At sampled latent points z ∈ Σ, estimate the mean curvature vector H(z) (via local quadratic surface fitting on k-NN tangent/normal patches) and the normal information gradient (∇\_Z i(z))⊥. Compute their cosine alignment in the operational metric g\_approx:  
  r \= ⟨ H, (∇ i)⊥ ⟩*{g\_approx} / ( \|H\|*{g\_approx} · \|(∇ i)⊥\|\_{g\_approx} ).  
* **Null baselines:** (1) Random normal vectors in N\_z Σ; (2) model trained on shuffled labels; (3) untrained random-weight initialization; (4) autoencoder trained without the target task; (5) Euclidean metric I\_d vs. at least two choices of g\_approx.  
* **Success criterion:** r is statistically significantly above all null models and persists across at least two distinct operational metrics g\_approx.

## **E2. Curvature Flattening Profile Across Training Epochs**

* **Method:** Track the mean normalized curvature norm \|H\|(t) across training checkpoints t.  
* **Prediction:** Early in training, \|H\|(t) may rise as the encoder rapidly folds Σ to separate task classes; once mutual information I(Z; Y) saturates near R\_task, \|H\|(t) decreases monotonically as redundant curvature is ironed out.

## **E3. Stratification at Decision Boundaries**

* **Method:** Compare the local eigenvalue spectrum of the Fisher metric g^(D)(z) with the local intrinsic dimension d\_eff(z) across Σ.  
* **Prediction:** Zones where g^(D)(z) becomes rank-deficient (zero-eigenvalue radical) align with the interior of constant-prediction cells, whereas cell boundaries exhibit sharp local curvature and rank transitions.

## **E4. Empirical NTK-Filtered Flow Verification (Hypothesis H1)**

* **Method:** Across consecutive training steps t → t \+ Δt, record the actual activation shift ΔE(x) \= E(x; t \+ Δt) − E(x; t) and compare its normal component against the NTK-filtered variational force F\_tilde(x) \= ∫ Θ\_E(x, x') F\_var(x') dμ\_Σ(x').  
* **Success criterion:** Significantly positive cosine correlation between ΔE⊥ and −F\_tilde⊥, confirming that representation geometry evolves along the NTK-filtered variational flow.

## **E5. Direct Evaluation of VIM Regularization**

* **Method:** Train identical architectures under (a) standard CE, (b) CE \+ weight decay, (c) CE \+ intrinsic dimension penalty, and (d) the explicit VIM objective L\_VIM(θ).  
* **Six success criteria:**  
  1. Validation task accuracy does not degrade relative to standard CE.  
  2. Curvature-gradient alignment r (from E1) is significantly higher under L\_VIM.  
  3. Mean normalized curvature \|H\| is lower and more concentrated at task boundaries.  
  4. Information deficit \[R\_task − I(Z; Y)\]\_+ is maintained or reduced.  
  5. Geometric improvements hold across multiple operational metrics g\_approx.  
  6. L\_VIM outperforms simple weight decay and unstructured dimension penalties.

# **6\. Summary Table: Mathematical Facts vs. Empirical Hypotheses**

## **Established Mathematical Facts (Follow from Definitions & Calculus)**

| Component | Status | Mathematical Basis |
| :---- | :---- | :---- |
| First variation of volume yields the mean curvature vector H | **Theorem** | Classical differential geometry / calculus of variations (do Carmo, 1976\) |
| Upper bound on volume Vol\_hat\_θ via trace tr(A\_θ) | **Theorem** | AM–GM inequality on eigenvalues of A\_θ \= J\_Eᵀ g\_I J\_E (under C¹ smoothness) |
| Cross-entropy CE\_D(θ) upper-bounds the mutual information deficit | **Theorem** | Non-negativity of KL divergence D\_KL(P(Y\|Z) \|\| D(Y\|Z)) ≥ 0 |
| Stationary balance equation H(z) \= λ(∇\_Z i(z))⊥ | **Corollary** | Euler–Lagrange equation δL/δΣ \= 0 under fixed pushforward density |
| Encoder tangent kernel Θ\_E \= J\_θ E · J\_θ Eᵀ filters parameter-space gradients | **Definition / Identity** | Chain rule in parameter space (standard NTK theory; Jacot et al., 2018\) |

## **Empirical Hypotheses (Require Testing via E1–E5)**

| Hypothesis | Status | Verification Protocol |
| :---- | :---- | :---- |
| Networks trained with standard CE implicitly approximate H \= λ(∇ i)⊥ | **Hypothesis** | Experiments E1, E2 |
| Observed alignment and curvature effects are invariant across operational metrics g\_approx | **Hypothesis** | Metric robustness check (§1.1.5, E1, E5) |
| Actual checkpoint trajectory correlates with the NTK-filtered geometric force (H1) | **Hypothesis H1** | Experiment E4 |
| Explicit minimization of L\_VIM(θ) improves geometric regularity and out-of-distribution robustness over CE | **Hypothesis** | Experiment E5 |

# **7\. Explicit Non-Claims**

To prevent misinterpretation when integrating this document with the rest of the repository (MBEL, Spectral Realization of V\_4, and LAF), the following boundaries are strictly enforced:

1. **No spacetime / General Relativity analogy:** Latent spaces are not spacetimes. The metric is fixed externally by task and system constraints; the encoder embeds a surface into Z rather than curving Z via Einstein-like field equations.  
2. **No closed-form canonical g\_true:** It is not claimed that g\_true is analytically known, unique, or identical to the Fisher metric of a single probe.  
3. **Standard CE ≠ Variational Functional:** Standard cross-entropy controls only the information deficit; controlling geometric volume requires an explicit regularizer (such as Vol\_hat\_θ) or architectural inductive bias.  
4. **Surrogate minimization ≠ exact Euler–Lagrange satisfaction:** Minimizing the upper bound F\_hat(θ) does not guarantee exact point-wise fulfillment of H \= λ(∇ i)⊥ unless the AM–GM and variational bounds are tight.  
5. **No smoothness guarantee everywhere:** The embedded image Σ \= E(X) may be stratified (e.g., piecewise-linear or kinked under ReLU activations); differential statements apply stratumwise.  
6. **Normal curvature ≠ tangential task progress (crucial for Spectral V\_4):** In H(z) \= λ(∇\_Z i(z))⊥, both vectors lie in the **normal bundle N\_z Σ \= (T\_z Σ)⊥**, governing how training bends the manifold Σ inside Z. Active state transitions of an agent on a fixed checkpoint move along the **tangent bundle T\_z Σ** and are governed by the tangential gradient ∇\_Σ i(z) and external verification contracts (see Spectral Realization of V\_4, §3.2 and §8.1).

# **8\. Executive Summary for Practitioners**

Useful information structures a model's latent space by embedding the data manifold Σ \= E\_θ(X) as an **informational minimal surface**: minimizing embedded volume in the task's effective metric subject to preserving predictive mutual information I(E(X); Y) ≥ R\_task.

* **At stationarity:** Inward surface-tension curvature H(z) balances outward normal information pressure λ(∇\_Z i(z))⊥.  
* **During training:** Manifold deformation is filtered through the encoder's Neural Tangent Kernel Θ\_E.  
* **In code:** Standard cross-entropy bounds only the information deficit; adding the trace-based volume surrogate Vol\_hat\_θ yields the computable **VIM loss L\_VIM(θ)**, turning minimal-surface geometry into a practical PyTorch regularizer.

# **References**

1. Weyl, H. (1911). Über die asymptotische Verteilung der Eigenwerte. *Mathematische Annalen*, 71, 441–479.  
2. Jacot, A., Gabriel, F., & Hongler, C. (2018). Neural Tangent Kernel: Convergence and Generalization in Neural Networks. *Advances in Neural Information Processing Systems (NeurIPS)*.  
3. Amari, S.-I. (2016). *Information Geometry and Its Applications*. Springer.  
4. Cover, T. M., & Thomas, J. A. (2006). *Elements of Information Theory* (2nd ed.). Wiley.  
5. Tishby, N., Pereira, F. C., & Bialek, W. (1999). The Information Bottleneck Method. *Proceedings of the 37th Annual Allerton Conference on Communication, Control and Computing*, 368–377.  
6. do Carmo, M. P. (1976). *Differential Geometry of Curves and Surfaces*. Prentice-Hall.

