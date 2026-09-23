# The Law of Useful Information Structuring in Model Latent Spaces

**Theory of Informational Minimal Surfaces**

**Status:** variational principle + upper surrogates (VIM) + mean curvature equation + NTK-filtered dynamics + operational protocol + explicit non-claims

**Language:** English (standard mathematical notation)

---

## 0. Objective and Conceptual Shift

We formulate the law of structuring useful information in latent spaces.

The correct geometric framework is minimal surface theory, not an analogy with general relativity.

The latent space metric is externally determined by the probabilistic structure of the task and system constraints. The trainable model (encoder) does not bend space itself; rather, it selects an optimal embedding of the data manifold into this environment.

The latent representation behaves like a multidimensional "soap film": the drive to compress information acts as surface tension, while the requirement to preserve predictive power acts as external directed pressure.

---

## 1. Spaces and Dynamical Variables

Let:

- $\mathcal{X}$ be the input space (tokens, images, context).
- $Z$ be the ambient latent space (layer activations of dimension $d$).
- $E: \mathcal{X} \to Z$ be the encoder (a model parameterized by weights $\theta$).
- $\Sigma = E(\mathcal{X}) \subset Z$ be the encoder image, a submanifold (possibly stratified) in $Z$.

The dynamical variable is the image $\Sigma$ (the embedding governed by the encoder weights), not the metric of the latent space.

---

### 1.1. Latent Space Metric: True Metric and Operational Approximations

#### 1.1.1. Status of the Metric

One must distinguish between:

1. The **true effective metric** of the model's latent space, which is determined by the entire stack of constraints—physical, architectural, algorithmic, and informational.
2. An **operational metric approximation**, which can be computed or estimated experimentally.

Below, the true metric is denoted as $g_{\mathrm{true}}$, and the approximation used in computations as $g_{\mathrm{approx}}$.

#### 1.1.2. True Effective Metric $g_{\mathrm{true}}$

By $g_{\mathrm{true}}$ we mean the effective geometry induced by the combination of constraints:

- **Physical:** finite precision (fp32, fp16), hardware noise, setting the lower scale of geometric resolution.
- **Architectural:** dimension $d$, non-linearities (ReLU, GELU), normalization, defining the admissible class of images $\Sigma$.
- **Algorithmic:** optimizer, learning rate schedule, dropout, affecting reachable regions and preferred directions.
- **Informational:** requirements for predictive power, noise structure, and redundancy in the data.

The metric $g_{\mathrm{true}}$ is not given in closed form. The existence of $g_{\mathrm{true}}$ does not imply that it is known or unique; it serves as a conceptual object motivating the choice of experimental approximations.

Within a single experiment or the analysis of a fixed checkpoint, $g_{\mathrm{true}}$ is treated as a fixed background. When the architecture, training phase, decoder, or hardware conditions change, the effective metric may change.

The dynamical variable of the theory remains the image $\Sigma$.

#### 1.1.3. Operational Metric $g_{\mathrm{approx}}$

Because $g_{\mathrm{true}}$ is inaccessible for direct computation, experiments employ an operational approximation $g_{\mathrm{approx}}$. All geometric objects in the law are evaluated with respect to the chosen approximation:

$$
\mathrm{Vol}_{g_{\mathrm{approx}}}(\Sigma), \quad \mathbf{H}_{g_{\mathrm{approx}}}, \quad \nabla_{g_{\mathrm{approx}}} i.
$$

Possible operational approximations:

1. **Fisher metric via an external decoder:** $P(Y|z) := D(z)$, where $D: Z \to \Delta(Y)$.

$$
g^{(D)}_{ij}(z) = \mathbb{E}_{y \sim D(z)} \left[ \partial_i \log D(y|z) \cdot \partial_j \log D(y|z) \right].
$$

2. **Metric via the Hessian of the training loss:**

$$
g^{(\mathcal{L})}_{ij}(z) = \mathbb{E} \left[ \partial_i \partial_j \mathcal{L}_{\mathrm{task}}(z, y) \right].
$$

3. **Local activation covariance metric:**

$$
g^{(\mathrm{cov})}(z) = \left( C(z) + \epsilon I \right)^{-1}.
$$

4. **NTK-induced metric:** based on the tangent kernel $\Theta_E$.

5. **Graph reconstruction:** via local patches and holonomies.

None of these approximations is considered canonical by default. The choice is specified in the experimental protocol.

#### 1.1.4. Local Information Density and Distribution Consistency

To compute the local information density, an operational decoder or probe $D: Z \to \Delta(Y)$ is fixed. Then:

$$
P(Y|z) := D(z).
$$

As $P(Y)$, one uses either the empirical label distribution or the induced marginal distribution $\bar{P}_D(Y) = \mathbb{E}_{z \sim \mu_\Sigma} D(Y|z)$. The choice is fixed in the protocol.

If $P(Y)$ is specified externally, the equality $\mathbb{E}[i(z)] = I(E(X);Y)$ requires consistency of the marginals.

#### 1.1.5. Robustness Requirement to Metric Selection

Substantive claims must be robust to the choice of operational metric. The experimental protocol requires evaluating diagnostic quantities (projection coefficient, normalized curvature) for at least two independent metrics.

If an effect persists under a change of $g_{\mathrm{approx}}$, it is treated as reflecting properties of $g_{\mathrm{true}}$. If it disappears, it is treated as an artifact of the approximation.

---

### 1.2. Distribution on $\Sigma$

Mutual information is defined between random variables:

$$
I(\Sigma; Y) := I(E(X); Y), \quad X \sim P_X.
$$

The distribution on $\Sigma$ is the pushforward $\mu_\Sigma = E_* P_X$. It constitutes part of the dynamical variable alongside the image itself.

---

## 2. Global Variational Principle

### 2.1. Formulation

$$
\min_{\Sigma \subset Z} \; \mathrm{Vol}_{g_I}(\Sigma) \quad \text{subject to} \quad I(E(X); Y) \ge R_{\mathrm{task}}
$$

The minimum is taken over embeddings $E: \mathcal{X} \to Z$ with respect to the metric $g_I \equiv g_{\mathrm{approx}}$.

### 2.2. Connection to $\varepsilon$-Capacity (Weyl's Formula)

According to Weyl's asymptotic expansion for the intrinsic metric on $\Sigma$ with intrinsic dimension $m$:

$$
H_\varepsilon(\Sigma, g_I|_\Sigma) \approx \frac{\mathrm{Vol}_{g_I}(\Sigma)}{c_m \, \varepsilon^m} + O(\varepsilon^{2-m}).
$$

Here $m$ is the effective intrinsic dimension of the image, which does not necessarily coincide with the dimension $d$ of the ambient space.

The leading term is volume. Minimizing volume is equivalent to minimizing predictive complexity in the first approximation.

---

## 3. Local Source and the Stationary State Equation

### 3.1. Lagrangian and Information Density

$$
\mathcal{L}[\Sigma] = \mathrm{Vol}_{g_I}(\Sigma) + \lambda \bigl( R_{\mathrm{task}} - I(E(X); Y) \bigr).
$$

Local information density:

$$
i(z) = D_{\mathrm{KL}}\bigl( P(Y|z) \;\|\; P(Y) \bigr).
$$

### 3.2. Stationary State

Under the fixed density approximation ($\delta(d\mu_\Sigma) = 0$), the stationarity condition $\delta\mathcal{L}/\delta\Sigma = 0$ yields:

$$
\boxed{ \mathbf{H}(z) = \lambda \, \bigl( \nabla_Z \, i(z) \bigr)^{\perp} }
$$

where:

- $\mathbf{H}(z)$ is the mean curvature vector of the image $\Sigma$ in the ambient space $Z$;
- $\bigl( \nabla_Z i(z) \bigr)^{\perp}$ is the normal component of the information density gradient;
- $\lambda$ is the Lagrange multiplier.

The mean curvature vector of the activation submanifold is balanced by the normal component of the useful information gradient. The model curves the data manifold just enough so that the gradient of predictive power counterbalances further entropic compression.

### 3.3. Limitations of the Stationary Equation

The equation $\mathbf{H} = \lambda(\nabla i)^\perp$ is the stationary condition of the **original** variational functional. Minimizing the upper surrogate $\widehat{\mathcal{F}}$ does not guarantee exact satisfaction of this equation; it guarantees control over the original functional only under the condition of sufficient tightness of the surrogate bounds. Conformance to the stationary equation under VIM training remains an empirical hypothesis.

---

## 4. Dynamics and Surrogates: NTK-Filtered Flow

### 4.1. Upper Surrogates of the Variational Functional (VIM)

Instead of incorrectly postulating the equivalence between the standard loss function and the geometric variational functional, rigorous upper bounds are introduced.

Let $Z = E_\theta(X)$, $D: Z \to \Delta(Y)$ be a decoder, and

$$
\mathrm{CE}_D(\theta) = \mathbb{E}_{(X,Y) \sim P} \left[ -\log D(Y|Z) \right].
$$

#### 4.1.1. Information Deficit

The information deficit is upper-bounded:

$$
\bigl[ R_{\mathrm{task}} - I(Z;Y) \bigr]_+ \le \bigl[ R_{\mathrm{task}} - H(Y) + \mathrm{CE}_D(\theta) \bigr]_+.
$$

This follows from $\mathrm{CE}_D(\theta) \ge H(Y|Z)$ and $I(Z;Y) = H(Y) - H(Y|Z)$.

#### 4.1.2. Volume

For volume, an upper surrogate is introduced, structurally analogous to the transition from surface area to Dirichlet energy. Strictly, it is derived from the AM–GM inequality for the eigenvalues of the induced metric $A_\theta$.

If the input space is locally an $m$-dimensional manifold $M$, and the induced metric is

$$
A_\theta(u) = J_E(u)^\top \, g_I(E_\theta(u)) \, J_E(u),
$$

then by the AM–GM inequality:

$$
\mathrm{Vol}_{g_I}(\Sigma_\theta) \le \widehat{\mathrm{Vol}}_\theta = \int_M \left( \frac{\operatorname{tr} A_\theta(u)}{m} \right)^{m/2} du.
$$

**Assumptions:** The bound assumes a continuous $m$-dimensional parameterization of the input and smoothness of the encoder. For discrete inputs, continuous relaxation, local smoothing, or discrete graph reconstruction is applied. If integration is performed with respect to $P_X$ rather than a uniform measure on $M$, the surrogate should be interpreted as a $P_X$-weighted geometric complexity rather than pure Riemannian volume.

For $m = 2$, the surrogate coincides in form with Dirichlet energy; for arbitrary $m$, the power $(\operatorname{tr} A_\theta / m)^{m/2}$ is used.

#### 4.1.3. Final Surrogate and Loss

Let $\widehat{I}_\theta \le I(E_\theta(X); Y)$ be a lower bound on mutual information. Then the variational functional is strictly upper-bounded by the surrogate:

$$
\mathcal{F}(\theta) \le \widehat{\mathcal{F}}(\theta) = \widehat{\mathrm{Vol}}_\theta + \lambda \bigl[ R_{\mathrm{task}} - \widehat{I}_\theta \bigr]_+.
$$

The corresponding regularized loss (Variational Information Metric, VIM):

$$
\mathcal{L}_{\mathrm{VIM}}(\theta) = \mathrm{CE}_D(\theta) + \alpha \, \widehat{\mathrm{Vol}}_\theta + \beta \, \bigl[ R_{\mathrm{task}} - \widehat{I}_\theta \bigr]_+.
$$

The coefficient $\beta$ serves as the practical analogue of the Lagrange multiplier $\lambda$ for the information constraint. The coefficient $\alpha$ controls the strength of the geometric regularizer and depends on the chosen upper surrogate for volume.

Standard cross-entropy controls only the information deficit. Geometric complexity is controlled by a separate, computable regularizer $\widehat{\mathrm{Vol}}_\theta$.

#### 4.1.4. Limitations of Surrogate Bounds

Upper surrogates are rigorous bounds under the stated regularity assumptions, but they may be loose. Guaranteeing approximate minimization of the original functional requires controlling the gap $\widehat{\mathcal{F}}(\theta) - \mathcal{F}(\theta)$.

---

### 4.2. Dynamical Equation with the Tangent Kernel

Training proceeds in parameter space $\theta$. The gradient flow for the geometric part is filtered by the encoder Jacobian:

$$
\frac{\partial E(x; t)}{\partial t} = -\eta \int_\Sigma \Theta_E(x, x'; t) \, \Bigl( \mathbf{H}(x') - \lambda \, (\nabla_Z i(x'))^\perp \Bigr) \, d\mu_\Sigma(x')
$$

where:

- $\Theta_E(x, x'; t) = \bigl\langle \nabla_\theta E(x; t), \, \nabla_\theta E(x'; t) \bigr\rangle_\Theta$ is the encoder tangent kernel (empirical NTK);
- integration is taken over the image $\Sigma$ with measure $\mu_\Sigma = E_* P_X$;
- $\mathbf{H}$ and $(\nabla i)^\perp$ are normal vector fields on $\Sigma$;
- $\eta$ is the learning rate;
- the minus sign corresponds to gradient descent along the functional.

At equilibrium, the variational force $F_{\mathrm{var}}(x) = \mathbf{H}(x) - \lambda (\nabla_Z i(x))^\perp$ either vanishes or lies in the null space of the kernel.

**Scope of applicability:** The equation is formulated for the gradient flow of the original variational functional. When using a standard training loss, correspondence to this flow is a hypothesis. When explicitly minimizing the surrogate $\mathcal{L}_{\mathrm{VIM}}$, the variational force must be replaced by the gradient of the corresponding surrogate; the exact form $\mathbf{H} - \lambda(\nabla i)^\perp$ is recovered only in the limit of tight surrogate bounds.

---

## 5. Verification Program (E1–E5)

### E1. Curvature Projection onto the Information Gradient

**Method:** Compute the projection

$$
r = \frac{\langle \mathbf{H}, (\nabla i)^\perp \rangle_{g_{\mathrm{approx}}}}{|\mathbf{H}|_{g_{\mathrm{approx}}} \cdot |(\nabla i)^\perp|_{g_{\mathrm{approx}}}}
$$

for various choices of $g_{\mathrm{approx}}$. Test $r > r_0$ (collinearity condition in high codimension).

**Null models for comparison:**

- random normal vectors in place of $(\nabla i)^\perp$;
- shuffled labels;
- untrained model;
- model trained without a task;
- Euclidean metric as a baseline;
- alternative $g_{\mathrm{approx}}$.

**Success criterion:** $r$ is significantly higher than in null models and robust to changes in the metric.

### E2. Flattening at Convergence

**Method:** Track $|\mathbf{H}|$ across training epochs.

**Verification:** As training converges, curvature should decrease. Nuance: early in training, curvature may increase (structure learning) and subsequently decline. Track the full profile $|\mathbf{H}|(t)$.

### E3. Stratification

**Method:** Verify that degeneracy zones of the Fisher metric correspond to boundaries of behavioral cells (drop in $d_{\mathrm{eff}}$).

### E4. NTK Flow Verification

**Method:** Compute the correlation between the empirical representation update $\partial_t E$ and the predicted filtered force $\tilde{F} = \mathcal{K} \, F_{\mathrm{var}}$.

**Verification:** Correlation coefficient between $\partial_t E$ and $\tilde{F}$ in the normal bundle. Significantly positive indicates support for hypothesis H1. Non-significant indicates dynamics do not follow the NTK-filtered flow.

### E5. Analysis of Surrogate Dynamics (VIM)

**Method:** Compare the geometry of models trained with standard CE against models explicitly optimizing the surrogate $\mathcal{L}_{\mathrm{VIM}}(\theta)$.

**Success criteria:**

1. Task performance must not degrade noticeably.
2. The coefficient $r$ must be higher for VIM.
3. Normalized curvature must be lower or more structured.
4. Information deficit must decrease.
5. The effect must persist across different choices of $g_{\mathrm{approx}}$.
6. VIM must outperform CE + weight decay or CE + intrinsic dimension penalty.

---

## 6. Status: Established Results and Hypotheses

### Established (Mathematical Facts)

| Component | Status | Justification |
|---|---|---|
| Volume variation yields the mean curvature vector | Theorem | Calculus of variations |
| Upper bound on volume $\widehat{\mathrm{Vol}}_\theta$ via $\operatorname{tr} A_\theta$ | Theorem | AM–GM inequality (under smoothness and continuous parameterization conditions) |
| $\mathrm{CE}_D(\theta)$ upper-bounds the deficit in $I(Z;Y)$ | Theorem | Properties of $D_{\mathrm{KL}}$; assuming a well-defined decoder $D$ and consistent $H(Y)$ |
| Equation $\mathbf{H} = \lambda(\nabla i)^\perp$ | Corollary | $\delta\mathcal{L}/\delta\Sigma = 0$ under fixed density |
| Tangent kernel $\Theta_E = J_E J_E^\dagger$ | Definition | Standard NTK theory |

### Hypotheses (Requiring Empirical Verification)

| Component | Status | Experiment |
|---|---|---|
| Models trained with standard CE approximate $\mathbf{H} = \lambda(\nabla i)^\perp$ | Hypothesis | E1, E2 |
| Geometric effects are robust to choice of $g_{\mathrm{approx}}$ | Hypothesis | Protocol 1.1.5 |
| Empirical dynamics correlate with NTK-filtered flow | Hypothesis H1 | E4 |
| Explicit minimization of $\mathcal{L}_{\mathrm{VIM}}$ yields superior geometric properties compared to standard CE | Hypothesis | E5 |

---

## 7. Explicit Non-Claims

- It is not claimed that latent spaces are spacetimes (general relativity analogies are excluded; geometry is external).
- It is not claimed that $g_{\mathrm{true}}$ is known, unique, or canonical.
- It is not claimed that the Fisher metric via a decoder is always the appropriate operational approximation $g_{\mathrm{approx}}$.
- It is not claimed that standard training loss is equivalent to the variational functional. A rigorous relationship is established via upper surrogates, but standard loss controls only the information deficit; geometric control requires a separate regularizer.
- It is not claimed that minimizing the upper surrogate $\widehat{\mathcal{F}}$ guarantees exact fulfillment of the stationary equation $\mathbf{H} = \lambda(\nabla i)^\perp$. This holds only in the limit of tight bounds.
- It is not claimed that $\Sigma$ is necessarily smooth. The image may be stratified.
- It is not claimed that upper surrogates are tight. They may be loose, and minimizing an upper bound is not equivalent to minimizing the original functional without controlling the gap.
- It is not claimed that commercial product success validates the hypothesis.

---

## 8. Framework Summary

Useful information structures the latent space so as to minimize the volume of the embedded image in the task's effective metric, subject to a prescribed level of mutual information.

**Stationarity condition:** The mean curvature vector of the image is balanced by the normal component of the gradient of local predictive power.

**Dynamics:** The deformation of the image is filtered by the encoder tangent kernel (NTK), projecting variational forces onto the reachable parameter space.

**Practical implementation:** Explicit minimization of the surrogate $\mathcal{L}_{\mathrm{VIM}}$ controls the variational functional via rigorous upper bounds. Standard training predominantly controls the information deficit; controlling geometric complexity requires a dedicated regularizer and remains an empirical question.