# **Technical Specification v0.3 — Computational Verification of Protocols V1–V7**

**STATUS: ACTIVE — supersedes Technical_Specification_v0.2 (FROZEN).**  
**Implements:** Protocols V1–V7 of `Causal Phase Program v3.9` (`Physics/Causal_Phase_Program_v3.md`).  
**Reference implementation baseline:** §9 of CPP v3.9 (corrected Python/NumPy/SciPy).  
**Author:** Vladimir Yakunin  
**Version:** 0.3.0  
**Date:** 2026-10-22  
**Predecessor outcome:** Technical Specification v0.2 was executed and returned `UNDECIDED`
(autocorrelation divergence in Mode B link-rewiring; finite-size ambiguity between
$`L=12,16,20`$ preventing clean core/void separation). This outcome triggered the
theoretical rework into v3.9. The present specification does NOT re-run v0.2;
it implements the v3.9 protocol suite.

**Target Hardware:** AMD Ryzen 5 5500 (6c/12t), 16 GB RAM, RX 6650 XT
(CPU + Numba FP64 pipeline; GPU optional).

---

## **0. Relationship to Predecessor Documents**

| Document | Status | Role in v0.3 |
|---|---|---|
| `Technical_Specification_v0.2.md` | FROZEN | Historical. Mode B tested the same local-condensation / void-rarefaction mechanism now covered by Protocol V3, but under the v2.0 $`D_{\mathrm{KL}} \le c \cdot N_\partial`$ mechanics. v0.2 returned UNDECIDED due to glassy freezing and finite-size ambiguity. |
| `Causal_Phase_Program_v3.md` §7 | ACTIVE | Defines the seven protocols V1–V7 with confirmation/refutation criteria. This document specifies HOW to execute them. |
| `Causal_Phase_Program_v3.md` §9 | ACTIVE | Reference implementation. v0.3 extends it with graph generators, annealing schedules, control ensembles, and automated reporting. |
| `Modified_Brusentsov_Entailment_Logic.md` | CANON | All final verdicts are classified in $`V_4`$. Protocol outcomes map to FOLLOW / NULL / UNDECIDED per §7 of CPP v3.9. |

---

## **1. Scope**

### **1.1 Included**

| Protocol | What is computed | §9 functions used | New code required |
|---|---|---|---|
| V1 | $`K_{xy}^{\mathrm{eff}}`$ distribution, twin reduction rate, spectral dimensions $`(d_s, d_H, d_\tau)`$ | `interval_local_path_quotient`, `collapse_structural_twins`, `is_hasse_transitive_free` | Graph generator with penalty exponent $`p`$; annealing schedule; Myrheim–Meyer dimension estimator |
| V2 | $`\kappa(A)`$, $`h_{\mathrm{KS}}(A)`$, $`\varepsilon`$-box entropy $`H_\varepsilon`$, $`H_{\mathrm{in}}`$, $`H_{\mathrm{out}}`$, $`\sigma_{\mathrm{bath}}`$ | `compute_oseledets_landauer_profile` | $`\varepsilon`$-partition entropy estimator; noise injection harness; linear-network control |
| V3 | $`f_{\mathrm{null}}(\mathcal{E})`$, $`\Delta\rho_D^{\mathrm{far}}`$, $`\ell_{\mathrm{null}}`$, diamond residual profile | `compute_edge_diamond_participation`, `evaluate_synchronization_and_balance`, `partition_triad` | Core condensation driver; degree-preserving swap control; phase-scrambling control |
| V4 | $`\delta\omega(r)/\omega_\infty`$, $`V_{\mathrm{int}}(r)`$, shell extent | `evaluate_synchronization_and_balance` | Radial frequency profiler; interaction free-energy estimator; $`\omega_A = \omega_{\mathrm{ext}}`$ control |
| V5 | Network topology transition $`N_{\mathrm{crit}}`$, $`\lambda_2`$ under degree bound | `evaluate_synchronization_and_balance` | Volume/frustration minimizer with $`\lambda_2`$ constraint; degree-matched configuration-model control |
| V6 | $`\eta_{\mathrm{sat}}`$, mutual information across $`\partial^+ A`$, interior $`K^{\mathrm{eff}}`$ at $`\eta_{\mathrm{sat}} \ge 1`$ | `compute_oseledets_landauer_profile`, `interval_local_path_quotient`, `partition_triad` | Bulk-contraction driver; trans-boundary MI estimator |
| V7 | Synchronization error, $`\gamma(Q)`$ vs $`\gamma(0)`$, integrator truncation residual | `verify_precision_helmholtz_and_integrator_chain` | (Minimal new code; §9 function is near-complete) |

### **1.2 Explicitly excluded**

- Continuum 4D Lorentzian manifold reconstruction.
- Fitting SPARC / DESI / DES-SN5YR data (deferred to post-v0.3 continuum-contact stage per CPP v3.9 §7).
- Full quantum Araki–Uhlmann modular operator calculation.
- Phenomenological fluid equations of state.
- 5D Kaluza–Klein geometry or free radion field (permanently NULL).

---

## **2. Software Architecture**

### **2.1 Repository structure**

```
Physics/v0.3_protocols/
├── config.yaml                    # Single source of truth for all run parameters
├── run_protocol.py                # CLI: python run_protocol.py --protocol V1 --seed 42
├── src/
│   ├── graph_gen.py               # Causal graph generators (Erdős–Rényi DAG, layered lattice, KR random)
│   ├── annealing.py               # Simulated annealing with branching penalty exponent p
│   ├── epsilon_entropy.py         # ε-box partition entropy estimator (V2)
│   ├── dynamics.py                # Discrete map G_R with noise injection (V2)
│   ├── condensation.py            # Core condensation / void rarefaction driver (V3, V6)
│   ├── radial_profile.py          # Frequency shift, interaction potential (V4)
│   ├── network_minimizer.py       # Volume/frustration minimization with λ₂ constraint (V5)
│   ├── mutual_information.py      # Trans-boundary MI estimator (V6)
│   ├── dimension_estimators.py    # Myrheim–Meyer, Hausdorff, spectral dimension (V1)
│   ├── controls.py                # Degree-preserving swaps, phase scrambling, linear-network control
│   ├── reporting.py               # Auto-generated REPORT_v0.3.md with V4 verdicts
│   └── v4_verdicts.py             # V4 classification of protocol outcomes per MBEL
├── tests/
│   ├── test_graph_gen.py          # Hasse validity, transitive irreducibility
│   ├── test_annealing.py          # Budget conservation, penalty monotonicity
│   ├── test_epsilon_entropy.py    # Known analytic cases
│   ├── test_dimension_estimators.py # Known graphs (path, grid, random DAG)
│   ├── test_controls.py           # Degree distribution preservation, gauge invariance
│   └── test_v4_verdicts.py        # Cascade conformance to MBEL §4.3
├── results/
│   ├── raw_metrics.h5             # FP64 time-series
│   └── REPORT_v0.3.md             # Auto-generated report
└── README.md
```

### **2.2 Dependency on §9**

All functions from CPP v3.9 §9 are imported as a **frozen baseline**:

```python
from cpp_v39_reference import (
    is_hasse_transitive_free,
    compute_causal_phase_invariants,
    compute_edge_diamond_participation,
    verify_wilson_identity,
    partition_triad,
    interval_local_path_quotient,
    collapse_structural_twins,
    compute_oseledets_landauer_profile,
    evaluate_synchronization_and_balance,
    verify_precision_helmholtz_and_integrator_chain,
)
```

**Fixes to §9 required before v0.3 execution** (from prior audit):

| Issue | Fix |
|---|---|
| `R @ R` on boolean arrays may produce unexpected results in some NumPy versions | Explicit `R = R.astype(np.int64)` at entry of every function |
| `np.linalg.inv(np.eye(N) - R)` in `is_hasse_transitive_free` is $`O(N^3)`$ and numerically fragile for $`N \ge 128`$ | Replace with iterative path count: `reach = R.copy(); for k in range(2, N): reach += np.linalg.matrix_power(R, k)` (nilpotency guarantees termination) |
| `svdvals(M_jac)` computes singular values, not eigenvalues | Document explicitly; add `eigvals(M_jac)` as alternative; report both |
| `shortest_path(A_sym, directed=False)` uses undirected graph for causal diameter | Add `directed=True` option; report both and flag discrepancy |
| Isolated vertices produce `1/sqrt(eps)` blowup in normalized Laplacian | Filter isolated vertices before $`\lambda_2`$ computation |

These fixes are **mandatory** before any protocol run. They are versioned as `cpp_v39_reference_patched.py`.

---

## **3. Protocol V1 — Binary Diamond Selection and Dimension Convergence**

### **3.1 Graph generation**

Generate random DAGs via the following procedure:

1. **Layered causal lattice (control):** $`L_\tau`$ time slices × $`L_x \times L_y`$ spatial vertices. Admissible links: $`x \in \mathcal{S}_t \to y \in \mathcal{S}_{t+1}`$ with $`\vert{}\mathbf{x}_\perp - \mathbf{y}_\perp\vert{} \le R_{\max}`$. Apply Hasse transitive reduction.

2. **Erdős–Rényi DAG:** $`N`$ vertices, each pair $`(i,j)`$ with $`i < j`$ linked with probability $`p_{\mathrm{edge}}`$. Apply transitive reduction.

3. **Kleitman–Rothschild random partial order:** Three-layer random poset (KR model). This is the **stress test**: without penalty, KR orders have $`\Theta(N^2/4)`$ relations.

Sizes: $`N \in \{64, 128, 256, 512\}`$ (V1 criterion says $`N \in \{128, 256\}`$; we extend to check scaling).

### **3.2 Annealing with branching penalty**

For each graph, run simulated annealing on the phase configuration $`\{\theta_{xy}\}`$ with cost functional:

```math
\mathcal{F}^{(p)}_{\mathrm{loc}} = a \sum_{(x,y): K_{xy} \ge 2} (K^{\mathrm{eff}}_{xy})^p + b \sum_{(x,y): K_{xy} \ge 2} J^{\mathrm{eff}}_{xy}
```

Penalty exponents: $`p \in \{2, 1, 0.5\}`$ (convex, linear, concave).
Parameters: $`a = 1.0`$, $`b \in \{0.0, 0.1, 1.0\}`$, $`T_{\mathrm{init}} = 5.0`$, $`T_{\mathrm{final}} = 0.01`$, geometric cooling rate $`0.995`$, $`10^4`$ sweeps per temperature.

**Key constraint:** vertex valency bounded by $`k_{\max} \in \{4, 6, 8\}`$. Proposals violating $`k_{\max}`$ are rejected.

### **3.3 Observables**

| Observable | Computation | Confirmation criterion (FOLLOW) |
|---|---|---|
| $`f_{K^{\mathrm{eff}}=2}`$ | Fraction of active intervals ($`K_{xy} \ge 2`$) with $`K^{\mathrm{eff}}_{xy} = 2`$ after annealing | $`\ge 0.80`$ under $`p=2`$, $`k_{\max} \le 8`$ |
| Twin reduction rate | Fraction of vertices merged by `collapse_structural_twins` vs total | Report only; no threshold |
| $`d_s`$ (spectral dimension) | From return probability of random walk on the Hasse graph | $`\vert{}d_s - d_H\vert{} \le 0.3`$, $`\vert{}d_s - d_\tau\vert{} \le 0.3`$ |
| $`d_H`$ (Hausdorff dimension) | From scaling of ball volume $`\sim r^{d_H}`$ | Same |
| $`d_\tau`$ (Myrheim–Meyer) | From causal interval counting: $`\vert{}I(x,y)\vert{} \sim \tau^{d_\tau}`$ | Same |

### **3.4 Null tests**

| ID | Test | Pass criterion |
|---|---|---|
| V1-N1 | $`p = 0`$ (no penalty): $`K^{\mathrm{eff}}`$ should NOT concentrate at 2 | $`f_{K^{\mathrm{eff}}=2} < 0.50`$ |
| V1-N2 | Gauge invariance: random $`\chi_v`$ shifts leave all observables invariant | $`\Delta < 10^{-13}`$ |
| V1-N3 | $`k_{\max} = 2`$ (path graph): no diamonds exist, $`f_{K^{\mathrm{eff}}=2} = 0`$ | Exact |
| V1-N4 | Budget conservation: $`N_V`$, $`N_E`$ constant across annealing | $`\Delta N_E = 0`$ |

### **3.5 Refutation criterion (NULL)**

$`K^{\mathrm{eff}} = 2`$ fails to emerge without manual hard-coding, OR spectral dimensions diverge ($`\vert{}d_s - d_H\vert{} > 0.5`$) across a decade of scale.

---

## **4. Protocol V2 — Oseledets Contraction and `ε`-Cell Merging**

### **4.1 Setup**

Select a connected subgraph $`A \subset X`$ (output of V1 annealing or a synthetic attractor). Define the discrete map:

```math
z(n+1) = G_R(z(n)) = M_{\mathrm{jac}} \cdot z(n) + \xi(n)
```

where $`M_{\mathrm{jac}}`$ is constructed as in §9 (`compute_oseledets_landauer_profile`) and $`\xi(n)`$ is stationary Gaussian noise with variance calibrated to maintain $`H_\varepsilon(Z_{n+1}) = H_\varepsilon(Z_n)`$.

### **4.2 ε-box entropy estimator**

Partition the state space into $`\varepsilon`$-cells aligned with the estimated $`E^u \oplus E^s`$ splitting:

```python
def epsilon_box_entropy(trajectory, lyapunov_basis, epsilon):
    """
    Compute H_epsilon(Z_n) = Shannon entropy of the occupation
    distribution over epsilon-boxes in the Lyapunov basis.
    """
    coords = trajectory @ lyapunov_basis.T
    cell_indices = np.floor(coords / epsilon).astype(int)
    unique_cells, counts = np.unique(cell_indices, axis=0, return_counts=True)
    probs = counts / counts.sum()
    return -np.sum(probs * np.log(probs))
```

### **4.3 Observables**

| Observable | Formula | Confirmation criterion |
|---|---|---|
| $`\kappa(A) - h_{\mathrm{KS}}(A)`$ | From Lyapunov spectrum | Positive (dissipative confinement) |
| $`H_{\mathrm{in}}^{(\varepsilon)} - H_{\mathrm{out}}^{(\varepsilon)}`$ | From entropy balance | Pearson $`r \ge 0.90`$ with $`\kappa - h_{\mathrm{KS}}`$ across stiffness sweep |
| Transverse merging rate | $`\exp(\kappa(A))`$ | $`\varepsilon`$-box count ratio scales as $`e^{\kappa}`$ |
| $`\sigma_{\mathrm{bath}}`$ | $`H_{\mathrm{in}} - H_{\mathrm{out}}`$ | $`> 0`$ and equals $`\kappa - h_{\mathrm{KS}}`$ within 5% |

### **4.4 Control**

**Covariance-matched linear network:** Construct a linear map $`M_{\mathrm{lin}}`$ with the same stationary covariance $`\Sigma`$ as the nonlinear system but $`\lambda_1 < 0`$ everywhere (stable). This tests whether the entropy balance is an artifact of covariance shape rather than nonlinear contraction.

### **4.5 Null tests**

| ID | Test | Pass criterion |
|---|---|---|
| V2-N1 | $`\varepsilon \to 0`$: entropy diverges (consistency) | $`H_\varepsilon \sim -d \log \varepsilon`$ |
| V2-N2 | $`\varepsilon \to \infty`$: entropy $`\to 0`$ | Exact |
| V2-N3 | No noise ($`H_{\mathrm{in}} = 0`$): system contracts to a point | $`H_\varepsilon \to 0`$ monotonically |
| V2-N4 | Linear control: $`\kappa - h_{\mathrm{KS}}`$ should NOT track entropy balance | $`r < 0.5`$ |

### **4.6 Refutation criterion (NULL)**

Coarse-grained entropy drop does not track $`\kappa(A) - h_{\mathrm{KS}}(A)`$ across stiffness parameters.

---

## **5. Protocol V3 — Phase-Mediated Void Rarefaction**

### **5.1 Setup**

Start from a V1-annealed graph at $`N = 256`$. Define:
- Core region $`\mathcal{I}_A`$: central 20% of vertices (by topological depth).
- Void region $`\mathcal{E}_{\mathrm{void}}`$: outer 40% of vertices.
- Buffer shell: 20% on each side.

### **5.2 Condensation driver**

Increase internal contraction $`\kappa(\mathcal{I}_A)`$ by:
1. Adding links within $`\mathcal{I}_A`$ (subject to $`k_{\max}`$).
2. Increasing phase coherence within $`\mathcal{I}_A`$ (lowering $`J_{xy}`$).
3. Removing links from $`\mathcal{E}_{\mathrm{void}}`$ (budget-conserving: removed void links are added to $`\partial A`$).

**Budget conservation:** $`N_V = \text{const}`$, $`N_E = \text{const}`$ throughout.

### **5.3 Observables**

| Observable | Formula | Confirmation criterion |
|---|---|---|
| $`\Delta\rho_D^{\mathrm{far}}(r)`$ | Radial diamond density profile, far region | $`> 3\sigma`$ drop: $`\Delta\rho_D^{\mathrm{far}} < 0`$ |
| $`f_{\mathrm{null}}(\mathcal{E}_{\mathrm{void}})`$ | Fraction of Hasse links with $`d_\diamond = 0`$ in void | Rise $`> 0`$ |
| $`\ell_{\mathrm{null}}(\mathcal{E}_{\mathrm{void}})`$ | Mean shortest-path distance in void | Expansion $`\Delta\ell_{\mathrm{null}} > 0`$ |

### **5.4 Controls**

| Control | Purpose |
|---|---|
| Degree-preserving swaps | Random rewiring preserving degree sequence. If $`f_{\mathrm{null}}`$ and $`\Delta\rho_D^{\mathrm{far}}`$ are fully explained by degree swaps → NULL |
| Boundary phase scrambling | Randomize phases on $`\partial A`$ links. If void effects persist → phase mediation is not causal → NULL |
| $`\kappa = 0`$ baseline | No condensation. All observables should be flat |

### **5.5 Null tests**

| ID | Test | Pass criterion |
|---|---|---|
| V3-N1 | Budget conservation: $`N_E(t) = N_E(0)`$ at every step | Exact |
| V3-N2 | Gauge invariance under random $`\chi_v`$ | $`\Delta < 10^{-13}`$ |
| V3-N3 | Hasse validity after every rewiring step | `is_hasse_transitive_free = True` |
| V3-N4 | Symmetric core (no condensation): all void observables flat | Within $`2\sigma`$ |

### **5.6 Refutation criterion (NULL)**

$`f_{\mathrm{null}}`$ and $`\Delta\rho_D^{\mathrm{far}}`$ are fully explained by degree-preserving edge swaps, OR insensitive to phase scrambling.

---

## **6. Protocol V4 — Interfacial Synchronization Shell**

### **6.1 Setup**

Select a cluster $`A`$ with internal phase rate $`\omega_A \neq \omega_{\mathrm{ext}}`$. Measure:

1. Radial frequency shift $`\delta\omega(r)/\omega_\infty`$ as a function of distance $`r`$ from cluster boundary.
2. Interaction free energy $`V_{\mathrm{int}}(r) = -\log \langle e^{-\Delta S(r)} \rangle`$ where $`\Delta S(r)`$ is the action cost of placing a test diamond at distance $`r`$.

### **6.2 Observables**

| Observable | Confirmation criterion |
|---|---|
| Shell extent $`[r_{\mathrm{bulk}}, r_{\mathrm{halo}}]`$ where $`\partial_r V_{\mathrm{int}}(r) > 0`$ | Scales with $`\vert{}\omega_A - \omega_{\mathrm{ext}}\vert{}`$ and $`\mathscr{S}_{\mathrm{interface}}(\partial A)`$ |
| $`V_{\mathrm{int}}(r)`$ at $`r > r_{\mathrm{halo}}`$ | Decays to 0 |

### **6.3 Control**

$`\omega_A = \omega_{\mathrm{ext}}`$: shell should vanish. $`V_{\mathrm{int}}(r) \approx 0`$ for all $`r`$.

### **6.4 Refutation criterion (NULL)**

Potential truncates sharply at core boundary with no extended shell.

---

## **7. Protocol V5 — Network Architecture Transition**

### **7.1 Setup**

Minimize volume + frustration subject to:
- $`\lambda_2(A) \ge \lambda_{\mathrm{sync}}`$ (synchronization connectivity)
- $`\deg(x) \le k_{\max}`$ (bounded degree)

Across $`N = 64, 128, 256, 512, 1024`$.

### **7.2 Observables**

| Observable | Confirmation criterion |
|---|---|
| Topology class: compact ball vs node-filament-void | Transition at $`N_{\mathrm{crit}}`$ |
| $`\lambda_2(N)`$ scaling | Violates $`\tau_{\mathrm{sync}} \le 2\pi/\sigma_\omega`$ above $`N_{\mathrm{crit}}`$ |
| Stability under $`\mathcal{R}_{\ell \to \ell+1}`$ | Coarse-graining preserves topology class |

### **7.3 Control**

Degree-matched configuration model (random graph with same degree sequence). If topology is indistinguishable from random → NULL.

### **7.4 Refutation criterion (NULL)**

Graphs disconnect, collapse to trees, or depend on manual clustering thresholds.

---

## **8. Protocol V6 — Interface Saturation**

### **8.1 Setup**

Increase bulk contraction $`\kappa(\mathcal{I}_A)`$ at fixed $`\vert{}\partial^+ A\vert{}_E`$. Track:

1. $`\eta_{\mathrm{sat}}(A) = \dot{I}_{\mathrm{erase}}^{\mathrm{net}} / (c_0 \ln 2 \cdot \vert{}\partial^+ A\vert{}_E)`$
2. Trans-boundary mutual information $`I(\mathcal{I}_A; \mathcal{E}_A)`$
3. Interior $`K^{\mathrm{eff}}_{xy}`$ distribution

### **8.2 Observables**

| Observable | Confirmation criterion |
|---|---|
| $`I(\mathcal{I}_A; \mathcal{E}_A)`$ vs $`\eta_{\mathrm{sat}}`$ | Saturates at $`\vert{}\partial^+ A\vert{}_E`$ when $`\eta_{\mathrm{sat}} \ge 1`$ |
| $`\sigma`$ degeneracy | Synchronization map $`\sigma`$ breaks on deep interior modes |
| Interior $`K^{\mathrm{eff}}`$ at $`\eta_{\mathrm{sat}} \ge 1`$ | Stabilizes at $`K^{\mathrm{eff}} \ge 3`$ |

### **8.3 Refutation criterion (NULL)**

Interior collapses into unstructured Kleitman–Rothschild 3-layer graph.

---

## **9. Protocol V7 — Precision Kernel Inclusion, Solenoidal Gap, Integrator Truncation**

### **9.1 Setup**

This protocol is the most directly executable: §9 function `verify_precision_helmholtz_and_integrator_chain` implements the core measurements.

Additional requirements:
- Generate random positive-definite $`\Pi_{\mathcal{E}}, \Pi_{\mathcal{I}}, \Pi_b`$ of dimensions $`(d_E, d_b, d_I) \in \{(10,5,10), (20,10,20), (50,20,50)\}`$.
- Generate $`\Pi_{\mathcal{E},b}, \Pi_{\mathcal{I},b}`$ satisfying (and separately violating) kernel inclusion.
- Generate $`\Gamma \succ 0`$ and $`Q = -Q^\top`$.

### **9.2 Observables**

| Observable | Confirmation criterion |
|---|---|
| Synchronization error under kernel inclusion | $`< 10^{-10}`$ |
| $`\gamma(Q) - \gamma(0)`$ | $`> 0`$ (strict acceleration) |
| Integrator fast-mode residual | $`O((\gamma_3 \tau_w)^{-1})`$ decay |

### **9.3 Null tests**

| ID | Test | Pass criterion |
|---|---|---|
| V7-N1 | Violate kernel inclusion: synchronization error should diverge | Error $`> 10^{-3}`$ |
| V7-N2 | $`Q = 0`$: $`\gamma(Q) = \gamma(0)`$ | Exact |
| V7-N3 | $`\tau_w \to \infty`$: all modes retained, residual $`\to 0`$ | Exact |

### **9.4 Refutation criterion (NULL)**

Synchronization fails under inclusion, $`\gamma(Q) < \gamma(0)`$, or high orders fail to decouple.

---

## **10. Execution Plan and Resource Budget**

### **10.1 Compute estimates (Ryzen 5 5500, Numba @njit)**

| Protocol | Estimated wall-clock | Dominant cost |
|---|---|---|
| V1 | 2–4 hours | Annealing at $`N = 256`$, $`10^4`$ sweeps × 5 temperatures × 3 penalties × 4 seeds |
| V2 | 1–2 hours | Trajectory integration $`10^5`$ steps × 6 stiffness values × 4 seeds |
| V3 | 2–3 hours | Rewiring $`10^5`$ steps × 4 condensation levels × 4 seeds |
| V4 | 1–2 hours | Radial profiling at 20 distance bins × 4 seeds |
| V5 | 3–5 hours | Minimization at 5 graph sizes × 3 constraints × 4 seeds |
| V6 | 2–3 hours | Contraction sweep × 4 seeds |
| V7 | < 30 minutes | Linear algebra at 3 dimensions × 10 random instances |
| **Total** | **~12–20 hours** | |

### **10.2 Memory**

Peak: $`N = 512`$ graph with $`N_E \approx 4096`$ edges. Adjacency + phases: $`< 1`$ MB. Lyapunov integration with QR: $`< 100`$ MB. Total $`< 500`$ MB per worker. 10 parallel workers: $`< 5`$ GB.

### **10.3 Execution order**

**Phase 1 (foundation):** V7 → V1.
V7 is the cheapest and validates the Gaussian machinery. V1 establishes the graph ensemble.

**Phase 2 (dynamics):** V2 → V3.
V2 validates the entropy balance on synthetic dynamics. V3 tests the physical mechanism on V1 graphs.

**Phase 3 (emergence):** V4 → V5 → V6.
These test higher-order emergent phenomena and depend on V1/V3 infrastructure.

---

## **11. Decision Criteria and V4 Classification**

Upon completion of `REPORT_v0.3.md`, each protocol receives a $`V_4`$ verdict:

### **FOLLOW (Confirmed)**
All null tests pass. Confirmation criterion met with $`> 3\sigma`$ statistical significance. Result robust across $`\ge 4`$ independent seeds and $`\ge 2`$ parameter choices.

### **NULL (Refuted)**
Null tests pass, but confirmation criterion fails across ALL scanned parameters. Result is recorded permanently. No post-hoc tuning.

### **UNDECIDED (Epistemic insufficiency)**
- Autocorrelation time diverges (glassy freezing).
- Finite-size effects prevent separation of signal from noise.
- Statistical significance $`< 3\sigma`$ despite promising trend.
- Control and treatment are indistinguishable.

**Critical rule (MBEL §5.4):** An UNDECIDED result is NEVER overwritten to NULL on budget exhaustion. The record retains UNDECIDED permanently.

### **OMIT (Not applicable)**
A protocol is classified OMIT if its preconditions are not met by the graph ensemble generated in an earlier protocol (e.g., V6 requires $`\eta_{\mathrm{sat}} \ge 1`$ to be reachable; if V2/V3 show no contraction mechanism, V6 is OMIT).

---

## **12. Automated Report Format**

`REPORT_v0.3.md` must contain:

1. **Header:** date, code version, §9 baseline hash, config.yaml hash.
2. **Per-protocol section:**
   - Observables table with mean ± std across seeds.
   - Null test results (pass/fail with values).
   - Control comparison.
   - $`V_4`$ verdict with justification.
   - Plots: radial profiles, dimension scaling, entropy balance, network topology.
3. **Cross-protocol consistency:**
   - Does V3 mechanism depend on V1 $`K^{\mathrm{eff}} = 2`$?
   - Does V2 entropy balance hold on V3-condensed graphs?
   - Does V6 saturation threshold agree with V2 contraction rate?
4. **Resource log:** total wall-clock, peak memory, seed list.
5. **Verdict summary table:**

| Protocol | $`V_4`$ Status | Key Observable | Value | Threshold |
|---|---|---|---|---|
| V1 | ... | $`f_{K^{\mathrm{eff}}=2}`$ | ... | $`\ge 0.80`$ |
| V2 | ... | $`r(\sigma_{\mathrm{bath}}, \kappa - h_{\mathrm{KS}})`$ | ... | $`\ge 0.90`$ |
| ... | ... | ... | ... | ... |

---

## **13. What This Specification Does Not Claim**

- It does not claim that the §9 reference implementation is bug-free. The fixes in §2.2 are mandatory.
- It does not claim that $`N = 256`$ is sufficient for continuum-limit conclusions. Finite-size scaling is an observable, not an assumption.
- It does not claim that the annealing schedule is optimal. The penalty exponent comparison (V1) is designed to test sensitivity.
- It does not claim that the ε-box entropy estimator is unique. Alternative partition schemes (adaptive, Voronoi) are future work.
- It does not claim that protocols V4–V6 will produce FOLLOW results. They may all return UNDECIDED or NULL.

---

## **14. Relation to v0.2 Outcome**

Technical Specification v0.2 returned UNDECIDED due to:
1. Glassy freezing in Mode B link-rewiring (autocorrelation $`\tau_{\mathrm{int}}`$ divergence).
2. Finite-size ambiguity: $`L = 12, 16, 20`$ insufficient to separate core collar from void buffer.

v0.3 addresses these by:
1. Replacing Metropolis link-rewiring with **annealing on phase configurations** (V1) and **explicit condensation drivers** (V3, V6). The graph topology is modified by controlled operations, not stochastic rewiring.
2. Extending graph sizes to $`N = 512`$ and $`N = 1024`$ (V5).
3. Using **explicit buffer shells** and radial profiles to separate core/interface/void.
4. Running V7 first as a cheap validation of the linear-algebra machinery before committing to expensive protocols.

---

*End of Technical Specification v0.3.*

*Normative parent: Causal Phase Program v3.9, §7–§9.*

*Canonical logic: Modified Brusentsov Entailment Logic, §§4–5.*
