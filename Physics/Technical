# Technical Specification v0.2 (CONSOLIDATED)

## Software Complex for Stochastic Verification of Local Condensation and Global Decompression on a Budget-Constrained Causal-Phase Graph

**Version:** 0.2.0 (consolidates v0.1 static baseline and v0.2 dynamic-topology test)  
**Date:** 17 October 2026  
**Author:** Vladimir Yakunin  
**Status:** Executable technical specification (single-track priority)  
**Target Hardware:** AMD Ryzen 5 5500 (6c/12t), 16 GB RAM, RX 6650 XT (CPU + Numba FP64 pipeline; GPU optional/not required)  

**Primary Scientific Question:**  
*When a causal-phase graph with a strictly conserved total vertex/link budget is subjected to a localized gauge-invariant $U(1)$ flux excitation ($\kappa > 0$) under an informational capacity bound $D_{\rm KL} \le c \cdot N_\partial$, does the graph spontaneously condense links around the source to satisfy the bound while depleting link/vertex density (expanding effective metric distances) in the surrounding void?*

---

## 0. Architectural Consolidation: Why v0.1 and v0.2 Are Merged

Because Stage v0.1 was not executed prior to the theoretical synthesis of October 2026, running a standalone static-lattice pipeline followed by a separate graph rewrite would waste engineering time under strict resource constraints. 

In v0.2, **the static lattice of v0.1 is preserved as the exact $\mathrm{Mobility} = 0$ control branch** within the same codebase:
- **Mode A (`topology_mode = "frozen"` — v0.1 Baseline):** The graph adjacency matrix $R_{xy}$ is initialized as a regular 3D layered causal lattice (or cubic grid) and held strictly fixed. Only the $U(1)$ phases $\theta_e \in [0, 2\pi)$ update via Heat-Bath / over-relaxation. This answers the original v0.1 question (*Does informational truncation produce a non-zero residual $\Delta F$ on a fixed background?*).
- **Mode B (`topology_mode = "dynamic_budget"` — v0.2 Core Test):** Both the $U(1)$ phases $\theta_e$ and the causal links $R_{xy} \in \{0,1\}$ evolve via Metropolis–Hastings rewiring moves that **strictly conserve the total number of vertices $N_V$ and total number of links $N_E$** (and preserve causal acyclicity / layered order). This directly tests whether local $D_{\rm KL}$ saturation forces topological condensation in the core ($D_{\rm core}$) and topological rarefaction (metric expansion) in the void ($D_{\rm void}$).

---

## 1. Scope and Explicit Boundaries of v0.2

| Included in v0.2 | Explicitly Excluded from v0.2 |
| :--- | :--- |
| Layered causal graph (DAG) with conserved $N_V, N_E$ and matrix representation $W_{xy} = r_{xy}e^{i\theta_{xy}}$ | Full continuum 4D Lorentzian manifold reconstruction or Regge calculus |
| Gauge-invariant minimal 4-cycle (causal diamond / plaquette) Wilson action | 5D Kaluza–Klein geometry or free radion field ($H_R$ is permanently `NULL`) |
| Mode A (`frozen` topology = v0.1) and Mode B (`dynamic_budget` rewiring = v0.2) | Direct fitting of SPARC rotation curves or DESI $H(z)$ data |
| Classical $D_{\rm KL}$ on gauge-invariant collar descriptors + $\mathrm{sLSE}_T$ non-diluting aggregation | Full quantum Araki–Uhlmann modular operator calculation |
| Direct measurement of core condensation ($\Delta N_{\partial, {\rm core}}$) vs. void decompression ($\Delta \rho_{\rm void}$, $\Delta d_{\rm eff}^{\rm void}$) | Phenomenological fluid equations of state ($w = -1, -1/3$, etc.) |

---

## 2. Mathematical Model of the Discrete System

### 2.1. Layered Causal Graph (DAG) with Conserved Budget

To guarantee strict causal acyclicity ($W^N = 0$) without expensive global cycle-detection searches at every Monte Carlo step, the vertex set $X$ of size $N_V = L_\tau \times L_x \times L_y$ is organized into $L_\tau$ discrete causal time slices $\mathcal{S}_0, \mathcal{S}_1, \dots, \mathcal{S}_{L_\tau - 1}$, each containing $L_x \times L_y$ vertices.

1. **Admissible Causal Links:** A directed link $e = (x \to y)$ with $r_{xy} = 1$ is admissible if and only if $x \in \mathcal{S}_t$ and $y \in \mathcal{S}_{(t+1) \bmod L_\tau}$ (or within a bounded causal horizon $\Vert{} \mathbf{x}_\perp - \mathbf{y}_\perp \Vert{} \le R_{\max}$ between adjacent slices), plus spatial links within the same slice for the Mode A 3D Euclidean comparison.
2. **Minimal Causal Diamonds (Plaquettes) $D$:** A minimal diamond $D(x, y; z_1, z_2)$ consists of a past apex $x \in \mathcal{S}_{t-1}$, a future apex $y \in \mathcal{S}_{t+1}$, and two distinct intermediate vertices $z_1, z_2 \in \mathcal{S}_t$ such that $r_{x z_1} = r_{z_1 y} = r_{x z_2} = r_{z_2 y} = 1$.
3. **Gauge-Invariant Diamond Holonomy:**
   $$W_D = U_{x z_1} U_{z_1 y} U_{z_2 y}^* U_{x z_2}^* = \exp\bigl(i (\theta_{x z_1} + \theta_{z_1 y} - \theta_{x z_2} - \theta_{z_2 y})\bigr).$$
   Under any local gauge transformation $\psi_v \to e^{i\chi_v}\psi_v$, $\theta_{uv} \to \theta_{uv} + \chi_u - \chi_v$, the holonomy $W_D$ is strictly invariant.
4. **Conserved Global Budget:** The total number of vertices $N_V$ and the total number of active links $N_E = \sum_{x,y} r_{xy}$ are **strictly constant** throughout the simulation:
   $$N_V = \mathrm{const}, \qquad N_E = \sum_{e} r_e = \mathrm{const}.$$

### 2.2. Microscopic Action and Gauge-Invariant Flux Source

Let $\mathcal{D}(R)$ be the set of all active minimal diamonds in the current graph configuration $R = \{r_{xy}\}$.

- **Vacuum Action ($\rho$ ensemble):**
  $$S_0[\theta, R] = \beta \sum_{D \in \mathcal{D}(R)} \bigl(1 - \mathrm{Re}\, W_D\bigr) + \mu_{\rm deg} \sum_{v \in X} \bigl(\mathrm{deg}(v) - \bar{k}\bigr)^2,$$
  where $\beta = 1/g_*^2$ is the gauge coupling and $\mu_{\rm deg} \ge 0$ is a weak baseline combinatorial elasticity that prevents degenerate star-graph collapse when $\kappa = 0$.
- **Perturbed Action ($\sigma$ ensemble with localized source in $D_{\rm core}$):**
  Let $D_{\rm core} \subset X$ be a fixed central region (the "baryonic/field condensation zone") and $D_{\rm void} = X \setminus D_{\rm core}^{\rm buffer}$ be the complementary exterior ("cosmic void"). For diamonds $D \subset D_{\rm core}$, a gauge-invariant flux bias $\kappa \ge 0$ (or target phase twist $\Phi_0 \in (0, \pi]$) is applied:
  $$S_\sigma[\theta, R] = S_0[\theta, R] - \kappa \sum_{D \subset D_{\rm core}} \mathrm{Re}\bigl(e^{-i\Phi_0} W_D\bigr).$$
  *Prohibition:* Fixing raw link angles $\theta_e$ is strictly forbidden. At $\kappa = 0$, $S_\sigma \equiv S_0$.

### 2.3. Boundary Cut $N_\partial$, Relative Entropy $D_{\rm KL}$, and the Capacity Penalty

1. **Dynamic Boundary Cut $N_\partial(R)$:**  
   Define the boundary of the core region $\partial D_{\rm core}$ as the set of active links $e = (u, v)$ with $r_{uv} = 1$ having exactly one endpoint in $D_{\rm core}$ and one endpoint outside $D_{\rm core}$. The boundary capacity is:
   $$N_\partial(R) = \sum_{u \in D_{\rm core},\, v \notin D_{\rm core}} r_{uv} + \sum_{u \notin D_{\rm core},\, v \in D_{\rm core}} r_{uv}.$$
   Crucially, in Mode B (`dynamic_budget`), **$N_\partial(R)$ is a dynamical variable**: the graph can increase $N_\partial(R)$ by migrating links from $D_{\rm void}$ to the boundary/collar of $D_{\rm core}$!

2. **Collar Gauge-Invariant Descriptors and $D_{\rm KL}$:**  
   Let $\mathcal{C}_{\rm collar}(R)$ be the set of active diamonds $D$ that share at least one link with $\partial D_{\rm core}$. From the set of invariants $\{\mathrm{Re}\, W_D\}_{D \in \mathcal{C}_{\rm collar}}$, compute the empirical distribution $\hat{p}_\sigma$ (binned histogram or 1D/2D KDE over $[-1, 1]$ of the collar holonomy values and local diamond energy density) and evaluate the classical Kullback–Leibler divergence against the calibrated vacuum reference distribution $\hat{p}_\rho(\beta)$:
   $$D_{\rm KL}^{\rm collar}(\theta, R) = N_{\rm collar}(R) \sum_{b=1}^{N_{\rm bins}} \hat{p}_\sigma(b) \log \frac{\hat{p}_\sigma(b)}{\hat{p}_\rho(b)}.$$

3. **Informational Truncation / Capacity Penalty (with $\mathrm{sLSE}_T$ option):**  
   The constraint threshold is $B(R) = c \cdot N_\partial(R)$. Define the excess information load:
   $$\mathcal{E}_{\rm info}(\theta, R) = \bigl[ D_{\rm KL}^{\rm collar}(\theta, R) - c \cdot N_\partial(R) \bigr]_+.$$
   When subdividing $\partial D_{\rm core}$ into $M$ local boundary patches $\{P_m\}_{m=1}^M$, aggregate the patch excesses $q_m = \tanh(\mathcal{E}_m / B_0)$ using the padding-invariant shifted LogSumExp (`Spectral_V4` §5.4):
   $$\mathcal{Q}_T(\theta, R) = \min\left\{ 1, \; T \log\left( 1 + \sum_{m=1}^{M} \bigl(e^{q_m / T} - 1\bigr) \right) \right\}.$$
   The total effective action governing the truncated/constrained ensemble is:
   $$S_{\rm total}[\theta, R] = S_\sigma[\theta, R] + \lambda_{\rm pen} \, \mathcal{E}_{\rm info}(\theta, R).$$

---

## 3. Monte Carlo Update Pipeline (Mode A and Mode B)

Each Monte Carlo sweep consists of two stages:

### Stage 1: Phase Sweep (Executed in both Mode A and Mode B)
- Iterate over all active links $e$ ($r_e = 1$).
- Update $\theta_e \in [0, 2\pi)$ using a **Heat-Bath** step for the local staple sum $\Sigma_e = \sum_{D \ni e} U_{\text{staple}(D)}$, followed by **1–2 over-relaxation reflection steps** $\theta_e \to (2\theta_{\Sigma_e} - \theta_e) \bmod 2\pi$ (which exactly conserve $S_0$ and rapidly decorrelate phases).
- If $\lambda_{\rm pen} > 0$ and $e$ belongs to a collar diamond, apply a Metropolis accept/reject filter for the change $\Delta \mathcal{E}_{\rm info}$.

### Stage 2: Budget-Conserving Link Rewiring Sweep (Executed in Mode B only)
Perform $K_{\rm rewire} \approx 0.1 N_E$ elementary **Link-Swap Moves** per sweep:
1. Randomly select an active link $e_{\rm old} = (u_1 \to v_1)$ with $r_{u_1 v_1} = 1$ ( Ensuring $\mathrm{deg}(u_1) > k_{\min}$ and $\mathrm{deg}(v_1) > k_{\min}$ so the graph remains connected).
2. Randomly select an inactive admissible causal pair $e_{\rm new} = (u_2 \to v_2)$ with $r_{u_2 v_2} = 0$ (50% global proposals between $D_{\rm void}$ and $D_{\rm core}$ collar; 50% local shift proposals).
3. Propose the swap: $r_{u_1 v_1} : 1 \to 0$ and $r_{u_2 v_2} : 0 \to 1$, drawing the initial phase $\theta_{u_2 v_2}$ from the local heat-bath distribution.
4. **Exact Budget Conservation:** By construction, $\Delta N_V = 0$ and $\Delta N_E = -1 + 1 = 0$.
5. Compute the total action change:
   $$\Delta S_{\rm total} = \Delta S_\sigma[\theta, R] + \lambda_{\rm pen} \Bigl( \mathcal{E}_{\rm info}(\theta', R') - \mathcal{E}_{\rm info}(\theta, R) \Bigr).$$
   *Key physical mechanism:* When $\kappa$ is large inside $D_{\rm core}$, $D_{\rm KL}^{\rm collar}$ exceeds $c \cdot N_\partial(R)$, creating a large positive penalty $\lambda_{\rm pen} \mathcal{E}_{\rm info}$. Moving a link from $D_{\rm void}$ onto $\partial D_{\rm core}$ increases $N_\partial(R) \to N_\partial(R) + 1$, which **lowers the penalty by $-\lambda_{\rm pen} c$**!
6. Accept the swap with Metropolis probability $P_{\rm acc} = \min\bigl(1, \exp(-\Delta S_{\rm total})\bigr)$.

---

## 4. Primary Observables: Testing the Condensation–Decompression Hypothesis

For every parameter point $(L, \beta, \kappa, c, \lambda_{\rm pen}, \text{mode})$, record five primary observables:

1. **Residual Free Energy $\Delta F$ (v0.1 deliverable):**
   $$\Delta F(\kappa, c) = -\log \bigl\langle \exp(-\lambda_{\rm pen} \mathcal{E}_{\rm info}) \bigr\rangle_{\sigma, \lambda_{\rm pen}=0}$$
   plus the non-diluting aggregate score $\langle \mathcal{Q}_T \rangle$.
2. **Core Boundary Condensation $\Delta N_\partial$:**
   $$\Delta N_\partial(\kappa, c) = \langle N_\partial(R) \rangle_{\kappa, c} - \langle N_\partial(R) \rangle_{\kappa=0, c\to\infty}.$$
   *Prediction:* In Mode B, for $\kappa > \kappa_{\rm crit}$ where $D_{\rm KL}$ hits the threshold $c N_\partial$, $\Delta N_\partial > 0$ (links migrate from the void to the core boundary).
3. **Void Link Density Depletion $\delta \rho_{\rm void}$ (The Dark Energy Proxy):**
   Let $\rho_{\rm void}(R) = N_E(D_{\rm void}) / \vert{}D_{\rm void}\vert{}$ be the spatial density of active links in the exterior void region (separated from $D_{\rm core}$ by a buffer shell of thickness $\ge 2$ lattice spacings). Define the relative depletion:
   $$\delta \rho_{\rm void}(\kappa, c) = \frac{\langle \rho_{\rm void} \rangle_{\kappa, c} - \langle \rho_{\rm void} \rangle_{\kappa=0}}{\langle \rho_{\rm void} \rangle_{\kappa=0}}.$$
   *Prediction:* $\delta \rho_{\rm void} < 0$, and $\vert{}\delta \rho_{\rm void}\vert{}$ scales linearly with $\Delta N_{\rm core} / \vert{}D_{\rm void}\vert{}$.
4. **Effective Metric Expansion in the Void $\Delta \ell_{\rm eff}^{\rm void}$ (Geodesic / Resistance Distance):**
   Measure the average shortest-path combinatorial distance $d_{\rm graph}(x, y)$ (and effective graph resistance distance $R_{\rm eff}(x,y)$ via the graph Laplacian $L = D - A$) between antipodal reference pairs $(x, y) \in D_{\rm void}$ whose connecting paths do not pass through $D_{\rm core}$:
   $$1 + z_{\rm void}^{\rm eff} := \frac{\langle d_{\rm graph}(x, y) \rangle_{\kappa, c}}{\langle d_{\rm graph}(x, y) \rangle_{\kappa=0}}.$$
   *Prediction:* As links are drawn into $D_{\rm core}$ to satisfy the Bekenstein bound, paths across the void become sparser and more tortuous, yielding $z_{\rm void}^{\rm eff} > 0$ (**effective metric expansion of the void driven by local condensation**).
5. **Radial Profile $K(r)$ of Link Density:**
   Compute the shell-averaged link density $\rho(r)$ as a function of Manhattan/Euclidean distance $r$ from the center of $D_{\rm core}$ to verify the transition from the condensed halo ($\Delta \rho(r) > 0$, Regime I) to the depleted void ($\Delta \rho(r) < 0$, Regime II).

---

## 5. Mandatory Diagnostics and Null Tests

To prevent false positives or confirmation bias, the automated report `REPORT_v0.2.md` must execute and log eight strict tests:

| Test ID | Diagnostic Name | Configuration | Pass Criterion |
| :--- | :--- | :--- | :--- |
| **D1** | Gauge Invariance Smoke Test | Apply random local gauge shifts $\chi_v \in [0, 2\pi)$ to saved configs | $\Delta D_{\rm KL} < 10^{-13}$ (FP64 machine precision) |
| **D2** | Null Source ($\kappa = 0$) | $\kappa = 0$, finite $c$ and $\lambda_{\rm pen} > 0$ | $\Delta N_\partial = 0$ and $\delta \rho_{\rm void} = 0$ within $2\sigma$ statistical noise |
| **D3** | Null Capacity Bound ($c \to \infty$ or $\lambda_{\rm pen} = 0$) | $\kappa > 0$, but capacity penalty turned off ($\lambda_{\rm pen} = 0$) | Tests whether phase action $S_\sigma$ alone causes rewiring vs. the informational bound $\mathcal{E}_{\rm info}$; isolates the pure Bekenstein-bound contribution $\Delta(\delta \rho_{\rm void}) = \delta \rho_{\rm void}(\lambda_{\rm pen}>0) - \delta \rho_{\rm void}(\lambda_{\rm pen}=0)$ |
| **D4** | Mode A (`frozen`) vs. Mode B (`dynamic_budget`) | Identical $(\beta, \kappa, c, \lambda_{\rm pen})$ | Mode A yields $\Delta N_\partial \equiv 0$, $\delta \rho_{\rm void} \equiv 0$, $\Delta F > 0$; Mode B lowers $\mathcal{E}_{\rm info}$ by increasing $N_\partial$ at the cost of $\delta \rho_{\rm void} < 0$ |
| **D5** | Shuffled Collar Null | Randomly permute collar plaquette invariants across the graph before computing $D_{\rm KL}$ | Directional migration of links to $\partial D_{\rm core}$ disappears ($\Delta N_\partial \to 0$) |
| **D6** | Budget Conservation Audit | Check $\sum_{x,y} r_{xy}$ at every measurement step | $N_E(t) - N_E(0) \equiv 0$ (zero drift across $10^5$ sweeps) |
| **D7** | Volume Scaling Scan | $L \in \{12, 16, 20\}$ at fixed $D_{\rm core}$ size | Total condensed links $\Delta N_{\rm core}$ remains $O(1)$ while $\delta \rho_{\rm void} \propto -L^{-3}$ and $\mathrm{sLSE}_T$ remains un-diluted |
| **D8** | Multi-Seed Reproducibility | $\ge 4$ independent PRNG seeds per grid point | Sign and confidence interval of $\Delta N_\partial$, $\delta \rho_{\rm void}$, and $z_{\rm void}^{\rm eff}$ are consistent across all seeds |

---

## 6. Software Architecture and Implementation Plan

### 6.1. Repository Structure (`Physics/v0.2_dynamic_graph/`)
```text
Physics/v0.2_dynamic_graph/
├── config.yaml                  # Single source of truth for run parameters
├── run_experiment.py            # CLI entrypoint (joblib parallelization over seeds/kappa)
├── src/
│   ├── graph_state.py           # CSR / adjacency arrays r_xy, theta_xy, diamond lookup tables (Numba)
│   ├── wilson_updates.py        # Numba-jitted Heat-Bath + over-relaxation on active links
│   ├── rewiring.py              # Budget-conserving Link-Swap Metropolis kernel (Mode B)
│   ├── kl_slse.py               # Gauge-invariant collar descriptors, classical D_KL, and sLSE_T
│   ├── observables.py           # Delta_F, N_boundary, rho_void, radial profile rho(r), Dijkstra d_eff
│   └── diagnostics.py           # Automated execution of Tests D1–D8
├── tests/
│   └── test_invariants.py       # pytest suite: gauge invariance, budget conservation, sLSE_T bounds
└── results/
    ├── raw_metrics.h5           # Compressed HDF5 time-series (FP64)
    └── REPORT_v0.2.md           # Auto-generated markdown report + summary plots
```

### 6.2. Resource Budget and Execution Timeline (Ryzen 5 5500, 16 GB RAM)
- **Memory footprint:** For $L=16$ ($N_V = 4096$, $N_E \approx 12288$), storing adjacency lists and FP64 angles takes $< 2$ MB per worker. Running 10 parallel workers via `joblib` consumes $< 500$ MB RAM total.
- **Compute speed with Numba `@njit`:** 1 full sweep (Heat-Bath + over-relaxation + $0.1 N_E$ link swaps + local diamond delta update) on $L=16$ takes $\sim 1.5$ ms on a single Ryzen 5 5500 thread ($\sim 15$ seconds for $10,000$ sweeps).
- **Full parameter grid:** $L \in \{12, 16, 20\}$, $\beta = 1.5$, $\kappa \in \{0.0, 1.0, 2.5, 5.0\}$, $c \in \{0.2, 0.5, 1.0, \infty\}$, `mode` $\in \{\text{frozen}, \text{dynamic}\}$, 4 seeds $\implies \sim 1.5 \text{ to } 3 \text{ hours}$ total wall-clock machine time.
- **Implementation effort:** 5–8 working days total.

---

## 7. Decision Criteria Upon Completion of `REPORT_v0.2.md`

The outcome of Stage v0.2 is classified strictly under the $V_4$ verdict standard:

1. **`FOLLOW` (Confirmed Pilot Signal):**  
   All null tests D1–D6 pass; in Mode B (`dynamic_budget`), activating the flux source ($\kappa > 0$) under the capacity penalty ($\lambda_{\rm pen} > 0$) produces a statistically significant ($> 3\sigma$) positive core boundary condensation $\Delta N_\partial > 0$, a negative void link density shift $\delta \rho_{\rm void} < 0$, and a positive effective void metric expansion $z_{\rm void}^{\rm eff} > 0$ that exceeds the $\lambda_{\rm pen}=0$ control (D3).  
   *Next step:* Extract the empirical radial profile $\Delta \rho(r)$ and proceed to analytical comparison with the VIM surface-tension kernel $\mathbf{H} = \lambda (\nabla i)^\perp$.

2. **`NULL` (Refuted in Current Realization):**  
   Null tests pass, thermalization is verified ($\tau_{\rm int} < 50$), but across all scanned $(\kappa, c, \lambda_{\rm pen})$ either $\Delta N_\partial \le 0$ or the void distance $z_{\rm void}^{\rm eff}$ shows zero response above the $\lambda_{\rm pen}=0$ baseline.  
   *Next step:* Record the negative result permanently in the repository log; do not tune boundary definitions post-hoc.

3. **`UNDECIDED` (Epistemic / Numerical Insufficiency):**  
   Autocorrelation time $\tau_{\rm int}$ diverges in Mode B (glassy freezing of link swaps), or finite-size effects between $L=12, 16, 20$ prevent separating the core collar from the void buffer.  
   *Next step:* Introduce parallel tempering (replica exchange over $\lambda_{\rm pen}$) or increase $L$ before making any physical claim.
