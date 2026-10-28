# **Technical Specification v0.4 — Computational Verification of Protocols V1–V7 of Causal Phase Program v4.0**

**STATUS: ACTIVE — supersedes Technical Specification v0.3 (superseded before execution by the v4.0 revision; removed from the repository).**  
**Implements:** Protocols V1–V7 of *Causal Phase Program v4.0* (`Physics/Causal_Phase_Program_v4.md`).  
**Reference implementation baseline:** §9 of CPP v4.0 (`cpp_v40_reference.py`, including the `run_self_test()` driver that reproduces the §10 verification table).  
**Author:** Vladimir Yakunin  
**Version:** 0.4.0  
**Date:** 2026-10-22  
**Predecessor outcomes:** Technical Specification v0.2 was executed and returned `UNDECIDED` (autocorrelation divergence in Mode B link-rewiring; finite-size ambiguity at $`L=12,16,20`$). Technical Specification v0.3 was written for CPP v3.9 and superseded before execution; its specification-gap fixes (penalty families, schedule/budget consistency, topology classifier, rank-deficiency lessons) are absorbed here in the form required by v4.0.

**Target Hardware:** AMD Ryzen 5 5500 (6c/12t), 16 GB RAM, RX 6650 XT (CPU + Numba FP64 pipeline; GPU optional).

---

## **0. Relationship to the Corpus**

| Document | Status | Role in v0.4 |
|---|---|---|
| `Causal_Phase_Program_v4.md` §7 | ACTIVE | Defines protocols V1–V7 with confirmation/refutation criteria. This document specifies HOW to execute them. |
| `Causal_Phase_Program_v4.md` §9 | ACTIVE | Frozen reference baseline (`cpp_v40_reference.py`). v0.4 extends it with ensemble movers, estimators, controls, and reporting. |
| `Causal_Phase_Program_v4.md` §10 | ACTIVE | Executed identity-level checks; the self-test driver passing is a hard gate (Phase 0) before any protocol run. |
| `Modified_Brusentsov_Entailment_Logic.md` | CANON | All final verdicts are classified in $`V_4`$ per CPP v4.0 §7–§8 and MBEL §§4–5 (including the non-promotion rule for `UNDECIDED`). |
| Technical Specifications v0.2 / v0.3 | REMOVED | Historical predecessors; outcomes and lessons recorded above and in §14. |

---

## **1. Scope**

### **1.1 Included**

| Protocol | What is computed | §9 baseline functions | New code required |
|---|---|---|---|
| V1 | Admissible-ensemble sampling; $`K`$/$`K^{\mathrm{eff}}`$ structure; $`N_D/N`$ vs $`\nu`$; dimensions $`(d_s, d_H, d_\tau)`$ | `admissible`, `directed_hypercube`, `diamond_density_interior`, `causal_phase_invariants`, `interval_local_path_quotient`, `structural_twins` | M1/M2/M3 ensemble movers with Hastings correction; Metropolis annealer over $`F_{\mathrm{struct}}`$ (Numba); dimension estimators $`d_s`$ (return probability), $`d_H`$ (ball growth), $`d_\tau`$ (Myrheim–Meyer, **with validity guards**); linear-extension weighting diagnostics |
| V2 | Benettin spectrum; KL entropies; three-channel balance of Theorem 4.3 | `transport_hermitian`, `G_map`, `real_jacobian`, `benettin_spectrum`, `knn_entropy`, `entropy_balance_check` | Stiffness sweep harness; Lemma 4.2 precondition gate; exact Gaussian control solver (discrete Lyapunov); non-injective-$`G`$ control |
| V3 | Equilibrium co-evolution of $`(R,\Theta)`$ under $`\mathscr{F}_{\mathrm{joint}}`$; $`\Delta f_{\mathrm{null}}(\mathcal{E}_A)`$, $`\Delta\ell_{\mathrm{null}}`$ | `magnetic_precision`, `woodbury_edge_swap_ratio`, `structural_and_joint_cost`, `diamond_participation`, `partition_triad` | Metropolis–Hastings sampler with **exact** Woodbury determinant ratios (no refactorization per move); frustrated-core initializer ($`\Phi_D=\Phi_0`$ in $`\mathcal{I}_A`$); null-path length measurement; $`\eta_{\mathrm{field}}=0`$ twin-budget control |
| V4 | Defect interaction $`V_{\mathrm{int}}(r_{AB})`$; interface functional $`\mathscr{S}_{\mathrm{interface}}`$ | `triadic_schur_decomposition`, `magnetic_precision`, `loop_expansion_diagnostics` | Two-defect placement at graph distance $`r_{AB}`$; exact $`\ln\det`$ difference evaluation; radial profile builder; flat-phase control |
| V5 | Constrained minimization (edges + frustration) at $`\lambda_2 \ge \lambda_{\mathrm{sync}}`$, $`\deg \le k_{\max}`$; topology class | `sync_time`, `admissible` | Constrained minimizer; **pre-registered topology classifier** (§7.2); random regular expander control; degree-matched configuration control; coarse-graining $`\mathcal{R}_{\ell\to\ell+1}`$ stability check |
| V6 | Inclusion residual $`V_{\mathrm{inc}}(A)`$; matchings $`\partial A \to \mathcal{I}_A`$; $`\Sigma_{\mathcal{I}\mathcal{E}}`$ | `kernel_inclusion_violation`, `screening_and_mediated_covariance`, `partition_triad` | Hopcroft–Karp maximum matching; region constructors for the three required classes (§8) |
| V7 | Mediated covariance, Woodbury, Schur identities; $`\gamma(0)`$ vs $`\gamma(Q_W)`$ over a $`\beta`$-grid; integrator truncation in the window $`(\gamma_3^{-1}, \gamma_2^{-1})`$ | `screening_and_mediated_covariance`, `woodbury_edge_swap_ratio`, `triadic_schur_decomposition`, `solenoidal_from_transport`, `relaxation_gap` | $`\beta`$-grid sweep; OU-chain truncation residual measurement |

### **1.2 Explicitly excluded**

- Continuum extrapolations: Einstein equations with $`\Lambda_{\mathrm{eff}}`$, post-horizon phase, mean-curvature balance (CPP v4.0 Registry row 17, `OMIT`).
- Fitting SPARC / DESI / DES-SN5YR data — outside the current program scope.
- Poisson sprinklings of causal sets — excluded from the ensemble class by the bounded-valency constraint (L3) (CPP v4.0 §3.2, “price of the choice”).
- Full quantum Araki–Uhlmann modular computations; 5D Kaluza–Klein geometry (permanently `NULL`).

---

## **2. Software Architecture**

### **2.1 Repository structure**

```
Physics/v0.4_protocols/
├── config.yaml                    # Single source of truth for all run parameters and thresholds
├── run_protocol.py                # CLI: python run_protocol.py --protocol V1 --seed 42
├── src/
│   ├── cpp_v40_reference.py       # Frozen §9 baseline (copied verbatim from CPP v4.0 §9)
│   ├── ensemble.py                # M1/M2/M3 moves, admissibility gates, Hastings corrections
│   ├── annealing.py               # Metropolis over F_struct / F_joint with exact Woodbury ratios
│   ├── dimensions.py              # d_s, d_H, d_tau estimators with validity guards
│   ├── dynamics.py                # V2 harness: stiffness sweep, precondition gate, controls
│   ├── defects.py                 # V4: frustrated-defect placement, V_int profiles
│   ├── minimizer.py               # V5: constrained edge/frustration minimization
│   ├── matching.py                # V6: Hopcroft–Karp matching vs injectivity
│   ├── topology.py                # V5: pre-registered topology classifier
│   ├── controls.py                # Hasse-gated degree-preserving swaps, phase scrambling, expander/control generators
│   ├── reporting.py               # Auto-generated REPORT_v0.4.md with V4 verdicts
│   └── v4_verdicts.py             # V4 classification per MBEL (incl. non-promotion rule)
├── tests/
│   ├── test_selftest_gate.py      # run_self_test() of the baseline must pass (Phase 0 gate)
│   ├── test_ensemble.py           # Moves preserve (L0)–(L4); Hastings symmetry
│   ├── test_woodbury_sampler.py   # Detailed balance with exact ratios
│   ├── test_dimensions.py         # Estimators on known graphs (hypercube: d via C(d,2) density)
│   ├── test_controls.py           # Degree/Hasse preservation of swap controls
│   └── test_v4_verdicts.py        # Cascade conformance to MBEL §4.3
├── results/
│   ├── raw_metrics.h5             # FP64 time-series
│   └── REPORT_v0.4.md             # Auto-generated report
└── README.md
```

### **2.2 Baseline discipline and mandatory additions**

All functions of `cpp_v40_reference.py` are imported as a **frozen baseline**; the Phase 0 gate requires `run_self_test()` to pass (all 15 checks, reproducing CPP v4.0 §10) before any protocol run. Mandatory additions on top of the baseline (lessons of the v3.9-era code audit):

| Issue | Requirement |
|---|---|
| Control rewiring can silently break degree conservation | Degree-preserving swap control rebuilds its edge list after every accepted mutation and gates every proposal by `is_hasse_irreducible` |
| Random-DAG controls can violate the Hasse property | Any ER-DAG-style control generator applies **closure-based** transitive reduction against the original reachability (sequential deletion is prohibited) |
| Myrheim–Meyer estimator is undefined off-domain | $`d_\tau`$ returns an explicit validity flag; negative or non-finite values are recorded as `estimator-invalid`, never as dimensions |
| ε-box entropy bias | Not used: V2 employs the Kozachenko–Leonenko $`k`$-NN estimator of the baseline (bias documented in §10 of CPP v4.0) |
| Numba porting | M1/M2/M3 inner loops and the annealer are ported to `@njit` FP64 with results cross-checked against the NumPy baseline to $`<10^{-12}`$ on $`N=64`$ |

---

## **3. Protocol V1 — Admissible Ensemble: Diamond Structure and Dimension**

### **3.1 Ensemble and moves**

States are $`(R,\Theta) \in \mathcal{A}(\nu, k_{\max})`$ (Definition 3.1 of CPP v4.0): (L0) Hasse, (L1) diamond covering, (L2) connectivity, (L3) $`\deg \le k_{\max}`$, (L4) $`N_D \ge \nu N`$. Moves: **M1** single edge replacement (accepted only if the result is admissible; field coupling uses the exact Woodbury ratio, §5), **M2** diamond corner flip with the Hastings correction $`|\mathcal{C}(R)|/|\mathcal{C}(R')|`$ and a direct recount of $`N_D`$, **M3** transposition of adjacent incomparable indices. Phases: uniform redraw on the circle per move. Sizes $`N \in \{64,128,256\}`$, $`\nu \in \{0.5,1,2,3\}`$, $`k_{\max} \in \{6,8\}`$.

### **3.2 Annealing**

Cost functional $`F_{\mathrm{struct}} = a\sum K^p + b\sum J + g\Vert C\Vert_F^2`$ with the three penalty families prescribed by CPP v4.0: convex $`p=2`$, linear $`p=1`$, concave $`\ln(1+K)`$. Parameters: $`a=1.0`$, $`b \in \{0.0, 0.1, 1.0\}`$, $`g \in \{0, 0.1, 0.3\}`$ (a 3-fold variation of $`a:b:g`$); geometric schedule $`T: 5.0 \to 0.01`$, rate $`0.995`$ (≈1240 levels), **total budget $`10^4`$ sweeps per run** distributed geometrically across levels. Because zero-temperature minimizers at free phases are gauge-flat (Proposition 1.2), $`T=0`$ minimizers and $`T>0`$ equilibrium samples are recorded **separately**; the $`K=2`$ fraction criterion is evaluated on $`T>0`$ samples (or at $`T=0`$ with frustrated boundary conditions).

### **3.3 Observables and criteria**

| Observable | Confirmation criterion (`FOLLOW`) |
|---|---|
| Fraction of active pairs ($`K\ge2`$) with $`K=2`$, $`K_{\max}`$ | $`\ge 80\%`$ at $`p=2`$, $`K_{\max}\le3`$, exceeding the concave control by $`\ge 0.2`$ |
| Manifold-like phase | $`\vert d_s - d_H\vert \le 0.3`$ and $`\vert d_s - d_\tau\vert \le 0.3`$ across a decade of scales |
| Diamond density | $`N_D/N`$ monotone in $`\nu`$; $`d_s`$ step-wise in $`\nu`$ |
| Twin reduction rate | Reported (no threshold) |

**Negative control A:** the same functional **without** (L1), (L4) must collapse to two-layer/tree states (Proposition 3.2). **Hypercube control:** on $`H_d`$ the estimators must reproduce $`d`$ via the density $`\binom{d}{2}`$ (Proposition 3.5, baseline check [5]).

### **3.4 Null tests**

| ID | Test | Pass criterion |
|---|---|---|
| V1-N1 | Gauge invariance: random $`\chi_v`$ shifts leave all observables invariant | $`\Delta < 10^{-12}`$ |
| V1-N2 | Admissibility: `admissible(R, nu, kmax)` after every accepted move | Exact `True` |
| V1-N3 | Hasse validity after every move | `is_hasse_irreducible = True` |
| V1-N4 | Hastings symmetry of M2 (forward/reverse proposal recounts) | Ratio identity to $`10^{-12}`$ |

### **3.5 Refutation criterion (`NULL`)**

No manifold-like phase anywhere on the grid; or equal $`K=2`$ fractions under convex and concave penalties; or the dimension depends on $`a:b:g`$ more strongly than on $`\nu`$.

---

## **4. Protocol V2 — Exact Entropy Balance (Theorem 4.3)**

### **4.1 Setup**

Model of Definition 4.1 on subsystems with $`2N_A \le 8`$ real dimensions: $`G(\psi) = (1-\delta)\psi + g H_A f(\psi)`$, $`\psi_{n+1} = G(\psi_n) + \xi_n`$, $`\xi_n \sim \mathcal{CN}(0, s^2 I)`$. **Precondition gate (Lemma 4.2):** runs with $`g\Vert H_A\Vert_2 \ge 1-\delta`$ are rejected before measurement and logged. Stiffness sweep: $`\delta \in \{0.15, 0.30, 0.45\}`$, $`g \in \{0.10, 0.25, 0.40\}`$, $`s \in \{0.15, 0.30, 0.45\}`$ (≥ 6 valid points), ≥ 4 seeds each.

### **4.2 Measurement channels (non-circular)**

1. **Spectrum:** Benettin QR along the noisy trajectory ($`\ge 2\cdot10^4`$ steps, burn-in $`\ge 500`$) — baseline `benettin_spectrum`.
2. **Jacobian channel:** $`-\mathbb{E}\ln\vert\det DG(Z)\vert`$ on $`\ge 10^5`$ stationary samples.
3. **Entropy channel:** $`\hat\Delta_{\mathrm{noise}} = \hat h(G(Z)+\xi) - \hat h(G(Z))`$ by Kozachenko–Leonenko $`k`$-NN ($`k=5`$) on the same samples.
4. **Stationarity:** window-averaged drift of $`\hat h(Z_n)`$ (first vs second half).

No channel may be computed from another: the balance identity is the *tested statement*, never an input (this was the v3.9 defect, CPP v4.0 Registry row 18).

### **4.3 Criteria**

| Observable | Confirmation criterion (`FOLLOW`) |
|---|---|
| $`\vert\hat\Delta_{\mathrm{noise}} - (-\sum_i\lambda_i)\vert`$ | $`\le 0.05`$ nats |
| $`\vert -\mathbb{E}\ln\vert\det DG\vert - (-\sum_i\lambda_i)\vert`$ | $`\le 0.02`$ nats |
| Stationarity residual | $`\le 0.05`$ nats/step |
| Exact Gaussian control (closed form $`-\ln\vert\det A\vert`$ via the discrete Lyapunov solution) | reproduced to $`0.02`$ by the same estimators |

**Controls:** exact Gaussian linear system; **non-injective $`G`$** (rank-deficient $`H_A`$ projection) where the theorem’s premises fail — divergence is expected and documents the injectivity boundary.

### **4.4 Null tests**

| ID | Test | Pass criterion |
|---|---|---|
| V2-N1 | Precondition gate rejects $`g\Vert H_A\Vert_2 \ge 1-\delta`$ | Rejection logged, no measurement emitted |
| V2-N2 | Seed stability | Spread across ≥4 seeds within tolerance |
| V2-N3 | KL estimator sanity on a known Gaussian | Bias $`\le 0.03`$ nats at $`n=10^5`$, $`k=5`$ |

### **4.5 Refutation criterion (`NULL`)**

Violation of the identity on injective systems with converged estimators, or failure of the estimators on the Gaussian control.

---

## **5. Protocol V3 — Equilibrium Graph Restructuring Under Field Back-Reaction (Proposition 6.2)**

### **5.1 Setup**

Equilibrium Metropolis–Hastings sampling of $`(R,\Theta) \in \mathcal{A}(\nu,k_{\max})`$ under the joint functional

```math
\mathscr{F}_{\mathrm{joint}} = F_{\mathrm{struct}}(R,\Theta; a,b,g,p) + \eta_{\mathrm{field}} \ln\det\Pi(R,\Theta), \qquad \eta_{\mathrm{field}} \in \{0.5, 1.0, 2.0\},
```

with a frustrated core $`A`$: diamond holonomies in $`\mathcal{I}_A`$ initialized at $`\Phi_D = \Phi_0 \in (0, \pi]`$ (fixed boundary-condition flux, per Proposition 1.2 corollary — free phases would relax to flatness). M1 edge moves use the **exact** Woodbury determinant ratio (Proposition 6.2, baseline `woodbury_edge_swap_ratio`) — no matrix refactorization per proposal; incremental $`\ln\det`$ bookkeeping is audited against a full `slogdet` recomputation every $`10^3`$ moves (drift tolerance $`10^{-10}`$).

### **5.2 Observables**

| Observable | Definition | Confirmation criterion (`FOLLOW`) |
|---|---|---|
| $`\Delta f_{\mathrm{null}}(\mathcal{E}_A)`$ | $`f_{\mathrm{null}}(\eta_{\mathrm{field}}) - f_{\mathrm{null}}(0)`$ via $`d_\diamond`$ (Definition 2.1) on the external zone | $`> 0`$ at $`>3\sigma`$ (bootstrap over blocks of the chain) |
| $`\Delta\ell_{\mathrm{null}}(\mathcal{E}_A)`$ | Mean length of unbranched null chains / null shortest paths in $`\mathcal{E}_A`$ | $`> 0`$ at $`>3\sigma`$ |
| Frustration sensitivity | Both effects vs $`\Phi_0 \to 0`$ | Vanish continuously as $`\Phi_0 \to 0`$ |

**Null control:** identical budgets at $`\eta_{\mathrm{field}} = 0`$ (pure $`F_{\mathrm{struct}}`$ ensemble), same seeds, same move counts.

### **5.3 Null tests**

| ID | Test | Pass criterion |
|---|---|---|
| V3-N1 | Detailed-balance sanity: acceptance ratios symmetric under move reversal | $`\Delta < 10^{-12}`$ on $`10^3`$ pairs |
| V3-N2 | Admissibility (L0)–(L4) after every accepted move | Exact |
| V3-N3 | Gauge invariance of $`\mathscr{F}_{\mathrm{joint}}`$ under random $`\chi`$ | $`\Delta < 10^{-12}`$ |
| V3-N4 | Hasse-gated degree-preserving swap control (§2.2): explains at most the combinatorial part of $`\Delta f_{\mathrm{null}}`$ | Excess remains at $`>3\sigma`$ beyond the swap control |
| V3-N5 | Incremental $`\ln\det`$ audit vs full recomputation | Drift $`< 10^{-10}`$ |

### **5.4 Refutation criterion (`NULL`)

External statistics at $`\eta_{\mathrm{field}} > 0`$ indistinguishable from the uncoupled control $`\eta_{\mathrm{field}} = 0`$, or insensitive to the core frustration $`\Phi_0`$ — closure of the field-driven background rarefaction hypothesis (Registry row 16).

---

## **6. Protocol V4 — Interface Schur Functional and Defect Interaction (Proposition 6.4)**

### **6.1 Setup**

Two frustrated phase defects $`\mathcal{D}_A, \mathcal{D}_B`$ (cores with $`\Phi_D = \Phi_0`$) are placed on admissible lattices/graphs at graph distance $`r_{AB} \in \{1, \dots, r_{\max}\}`$. The interaction energy is evaluated **exactly** (no sampling required at fixed $`R`$):

```math
V_{\mathrm{int}}(r_{AB}) := \ln\det\Pi(R,\Theta_{r_{AB}}) - \ln\det\Pi(R,\Theta_\infty),
```

where $`\Theta_\infty`$ places the second defect at maximal distance; ensemble averaging uses the equilibrium V3 chains at the same $`\eta_{\mathrm{field}}`$. The interface functional $`\mathscr{S}_{\mathrm{interface}}(A)`$, $`\mathscr{S}_{\mathrm{interface}}(A\cup B)`$ is computed via `triadic_schur_decomposition`.

### **6.2 Observables and criteria**

| Observable | Confirmation criterion (`FOLLOW`) |
|---|---|
| Profile $`V_{\mathrm{int}}(r_{AB})`$ | Monotone decreasing in $`r_{AB}`$, resolved above noise for $`r_{AB} \le r_{\max}`$ |
| Interface excess $`\mathscr{S}_{\mathrm{interface}}(A) - \mathscr{S}_{\mathrm{interface}}(A)\vert_{\Phi_0=0}`$ | $`> 0`$ and growing with $`1-\cos\Phi_0`$ |
| Pair excess $`\mathscr{S}_{\mathrm{interface}}(A\cup B) - \mathscr{S}_{\mathrm{interface}}(A) - \mathscr{S}_{\mathrm{interface}}(B)`$ | Sign and magnitude consistent with $`V_{\mathrm{int}}`$ (cross-channel coherence) |

**Control:** flat phases $`\Phi_0 = 0`$ (all profiles must vanish identically, Proposition 1.2).

### **6.3 Null tests**

| ID | Test | Pass criterion |
|---|---|---|
| V4-N1 | Large-distance decay | $`V_{\mathrm{int}}`$ indistinguishable from 0 at $`r_{AB} = r_{\max}`$ within bootstrap CI |
| V4-N2 | Symmetry under defect exchange $`A \leftrightarrow B`$ | $`\Delta < 10^{-12}`$ |
| V4-N3 | Gauge invariance of $`V_{\mathrm{int}}`$ and $`\mathscr{S}_{\mathrm{interface}}`$ | $`\Delta < 10^{-12}`$ |
| V4-N4 | Schur identity audit on every configuration | decomposition error $`< 10^{-12}`$ |

### **6.4 Refutation criterion (`NULL`)

The profile $`V_{\mathrm{int}}(r_{AB})`$ is indistinguishable from noise at $`r_{AB} \ge 2`$ — closure of the long-range defect-interaction-through-the-field hypothesis.

---

## **7. Protocol V5 — Architecture of Synchronizable Bounded-Degree Graphs**

### **7.1 Setup**

Minimize the edge number and frustration subject to $`\lambda_2(A) \ge \lambda_{\mathrm{sync}}`$, $`\deg(x) \le k_{\max}`$, and connectivity, across $`N = 64, 128, 256, 512, 1024`$ (the §3.2 annealer with a constraint-rejection rule; $`\lambda_2`$ of the normalized skeleton Laplacian with isolated-vertex filtering).

### **7.2 Pre-registered topology classifier**

Computed on the symmetric skeleton; all thresholds live in `config.yaml`:

1. **Chain fraction** $`f_{\mathrm{chain}} := \vert{}\{v : \deg(v) \le 2\}\vert{} / N`$.
2. **Core clustering ratio** $`C_{\mathrm{ratio}}`$ := mean local clustering coefficient of the top-decile-degree vertices ÷ the same statistic on degree-matched configuration models (10 realizations).
3. **Distance bimodality** $`b`$ := Sarle coefficient of the pairwise BFS-distance histogram ($`b = (\gamma^2 + 1)/\kappa`$, where $`\gamma`$ and $`\kappa`$ are the skewness and kurtosis of the histogram — not to be confused with the contraction rate $`\kappa(A)`$; $`b > 0.555`$ indicates bimodality).

**Class assignment:** `compact` if $`f_{\mathrm{chain}} < 0.25`$ and $`C_{\mathrm{ratio}} < 2`$; `filamentary-void` if $`f_{\mathrm{chain}} \ge 0.5`$ and $`C_{\mathrm{ratio}} \ge 3`$ and $`b > 0.555`$; otherwise class-`UNDECIDED` (excluded from $`N_{\mathrm{crit}}`$ estimation and logged). $`N_{\mathrm{crit}}`$ := the smallest $`N`$ for which the class is `filamentary-void` at every $`N' \ge N`$, confirmed in ascending and descending $`N`$ order (hysteresis check). **Spectral scale-invariance:** fit $`\rho(\lambda) \propto \lambda^{\alpha}`$ on $`\lambda \in (0, \lambda_{\mathrm{sync}}]`$; criterion: $`\alpha`$ varies by $`\le 0.15`$ across $`N \in \{256, 512, 1024\}`$.

### **7.3 Controls and criteria**

**Baseline controls:** $`d`$-dimensional balls (`directed_hypercube`); **random $`k_{\max}`$-regular expanders** (the competing shallow architecture of Corollary 5.3); degree-matched configuration models. **Confirmation (`FOLLOW`):** minimizers are `filamentary-void`, have lower cost than balls and expanders at the same $`\lambda_{\mathrm{sync}}`$, and the class is stable under $`\mathcal{R}_{\ell\to\ell+1}`$ (Definition 5.2). **Refutation (`NULL`):** minimizers turn out to be expanders, lose connectivity, or the classification depends on manual thresholds.

---

## **8. Protocol V6 — Kernel Inclusion Through Interfaces (Proposition 2.2, Corollary 2.3)**

### **8.1 Setup and required region classes**

For subsystems $`A`$ on lattices and admissible graphs, compute the inclusion residual $`V_{\mathrm{inc}}(A) = \Vert\Pi_{\mathcal{E}b}P_{\ker\Pi_{\mathcal{I}b}}\Vert_2`$ (baseline `kernel_inclusion_violation`), the mediated covariance $`\Sigma_{\mathcal{I}\mathcal{E}}`$, and the maximum matching $`\partial A \to \mathcal{I}_A`$ (Hopcroft–Karp on the Hasse bipartite support). Three region classes are **required** (lesson of the v0.3 audit — with injective $`\Pi_{\mathcal{I}b}`$ the inclusion is vacuous and violations are undetectable):

| Class | Construction | Expected $`V_{\mathrm{inc}}`$ |
|---|---|---|
| (a) Matching-saturated | Slab-like regions ($`\vert{}\partial A\vert{} \le \vert{}\mathcal{I}_A\vert{}`$, every boundary vertex matched to a distinct interior neighbor) | $`< 10^{-10}`$ |
| (b) Isolated boundary vertex | Regions with a boundary vertex lacking interior neighbors (e.g., rectangular blocks: corners) | Exactly the unit-modulus prediction of Corollary 2.3(1) (for a single defect: $`\sqrt2`$ — verified in the baseline self-test [7]) |
| (c) Rank-deficient | $`\vert{}\partial A\vert{} > \vert{}\mathcal{I}_A\vert{}`$ or structurally degenerate couplings | Generic violation; magnitude correlates with $`\dim\ker\Pi_{\mathcal{I}b}`$ |

**Note (verified during baseline construction):** convex balls and rectangular blocks on grid Hasse diagrams systematically fail the Hall condition near corners — this is itself a Corollary 2.3 prediction, not an estimator artifact; class (a) must use slab-like or matching-verified regions.

### **8.2 Criteria and null tests**

**Confirmation (`FOLLOW`):** every class-(b) region gives $`V_{\mathrm{inc}} > 0`$; every matching-saturated class-(a) region gives $`V_{\mathrm{inc}} < 10^{-10}`$; the matching rank equals the generic-phase matrix rank of $`\Pi_{\mathcal{I}b}`$ (Edmonds). **Refutation (`NULL`):** any discrepancy with Corollary 2.3 (indicating an implementation or algebra error). Null tests: gauge invariance of $`V_{\mathrm{inc}}`$ ($`\Delta<10^{-12}`$); consistency of $`\Sigma_{\mathcal{I}\mathcal{E}}`$ with the mediated-covariance formula ($`<10^{-12}`$); empty-zone guard raises a controlled error (no silent crashes).

---

## **9. Protocol V7 — Mediated Covariance, Solenoidal Gap, Integrator Truncation**

### **9.1 Setup**

Pure linear-algebra protocol on the model objects: (i) the mediated-covariance identity, the Woodbury law, and the Schur decomposition on random admissible graphs and lattices (baseline functions); (ii) $`\gamma(0)`$ vs $`\gamma(Q_W)`$ over a grid $`\beta \in \{0, 0.25, 0.5, 1, 2, 4\}`$ on anisotropic graphs; (iii) integrator-chain truncation: OU chains with modes $`\{\gamma_k\}`$ satisfying $`\gamma_2 \ll \gamma_3`$, window $`\tau_w^{(\ell)} \in (\gamma_3^{-1}, \gamma_2^{-1})`$ (the corrected non-empty window), residual measured for orders $`k \ge 3`$.

### **9.2 Criteria and null tests**

**Confirmation (`FOLLOW`):** algebraic identities to $`< 10^{-12}`$; $`\gamma(Q_W) \ge \gamma(0)`$ everywhere and strictly greater at $`\beta \ne 0`$ on anisotropic graphs; fast-mode residual decays as $`O((\gamma_3\tau_w)^{-1})`$ (least-squares slope $`-1 \pm 0.15`$ in log-log). **Null tests:** $`\beta = 0`$ gives exact equality $`\gamma(Q_W)=\gamma(0)`$; $`\tau_w \to \gamma_3^{-1}`$ (window collapse) must **fail** the truncation criterion — a documented negative control. **Refutation (`NULL`):** identity error above tolerance, $`\gamma(Q_W) < \gamma(0)`$, or absence of fast-mode cutoff.

---

## **10. Execution Plan and Resource Budget**

### **10.1 Order and estimates (Ryzen 5 5500, Numba @njit)**

| Phase | Protocols | Estimated wall-clock | Gate role |
|---|---|---|---|
| 0 | Baseline `run_self_test()` | < 5 min | **Hard gate:** failure blocks everything |
| 1 | V6 → V7 | < 1 h total | Cheap algebra; validates Gaussian/Woodbury machinery |
| 2 | V2 | 1–2 h | Validates the dynamical channel (Theorem 4.3) |
| 3 | V3 → V4 | 4–7 h | Equilibrium co-evolution; exact ratios keep M1 moves O(N²) |
| 4 | V1 | 6–10 h | Large ensembles: ≈1240 temperature levels, $`10^4`$ total sweeps per run × 3 penalty families × 4 seeds × grid ($`N, \nu, k_{\max}`$) |
| 5 | V5 | 8–12 h | Constrained minimization at $`N \le 1024`$ |
| — | **Total** | **≈20–32 h** | |

### **10.2 Memory**

Peak: $`N=1024`$ graph, $`\Pi \in \mathbb{C}^{1024\times1024}`$ (16 MB), full inverse for audits (16 MB), Lyapunov QR on $`\le 8`$ real dimensions (negligible), k-NN trees on $`10^5 \times 8`$ (< 100 MB). Total < 1 GB per worker; 6 parallel workers < 6 GB.

---

## **11. Decision Criteria and V4 Classification**

Upon completion of `REPORT_v0.4.md`, each protocol receives a $`V_4`$ verdict per MBEL:

- **`FOLLOW` (confirmed):** all null tests pass; the confirmation criterion is met at $`>3\sigma`$ (statistical criteria) or at the stated algebraic tolerance (identity criteria); robust across ≥ 4 seeds and ≥ 2 parameter choices.
- **`NULL` (refuted):** null tests pass but the confirmation criterion fails across ALL scanned parameters; recorded permanently; no post-hoc tuning.
- **`UNDECIDED` (epistemic insufficiency):** autocorrelation divergence; finite-size ambiguity; significance < 3σ despite a trend; control and treatment indistinguishable. **Critical rule (MBEL §5.4):** an `UNDECIDED` is NEVER overwritten to `NULL` on budget exhaustion.
- **`OMIT` (not applicable):** preconditions unmet (e.g., V4 requires V3 to establish a coupled ensemble; if V3 returns `NULL` on the coupling itself, V4 pair-interaction is `OMIT`-ted with the reason logged).

Registry updates: protocol outcomes map to CPP v4.0 Registry rows 6 (V1), 10-item-3 (V7), 11 (V2), 13b (V5), 16 (V3, V4); identity-level rows (1–5, 7, 8, 13, 15) are re-certified by the Phase 0–1 gates.

---

## **12. Automated Report Format**

`REPORT_v0.4.md` must contain:

1. **Header:** date, code version, baseline hash (of `cpp_v40_reference.py`), `config.yaml` hash, self-test transcript.
2. **Per-protocol section:** observables (mean ± std across seeds), null-test results with values, control comparisons, $`V_4`$ verdict with justification, plots (dimension scaling, entropy-balance scatter, $`\Delta f_{\mathrm{null}}`$ vs $`\eta_{\mathrm{field}}`$, $`V_{\mathrm{int}}(r)`$ profiles, topology-class maps).
3. **Cross-protocol consistency:** do V3 restructuring statistics agree with the V1 ensemble structure? Do V6/V7 algebra gates hold on the V3 equilibrium samples? Does the V2 balance hold on subsystems extracted from V1 minimizers?
4. **Resource log:** wall-clock, peak memory, seed list, rejected-move statistics.
5. **Verdict summary table** (Protocol | $`V_4`$ | key observable | value | threshold).

---

## **13. What This Specification Does Not Claim**

- It does not claim the §9 baseline is bug-free beyond the 15 self-test checks; the Phase 0 gate is the operational bound.
- It does not claim $`N \le 1024`$ suffices for continuum-limit conclusions; finite-size scaling is an observable, not an assumption (and the continuum layer is `OMIT` in CPP v4.0 anyway).
- It does not claim the annealing schedule or the V5 classifier thresholds are optimal; both are pre-registered to prevent post-hoc tuning, and sensitivity is itself measured (V1 penalty families, V5 hysteresis check).
- It does not claim the Landauer reading (Hypothesis H-L) is tested: V2 tests the exact entropy balance (Theorem 4.3) only; the thermodynamic interpretation remains `UNDECIDED` (Registry row 12) and requires external physical calibration.
- It does not claim protocols will return `FOLLOW`; any of V1, V3, V4, V5 may return `NULL` or `UNDECIDED`.

---

## **14. Relation to Predecessor Outcomes**

**v0.2 (`UNDECIDED`, executed):** glassy freezing of stochastic Mode B rewiring and finite-size ambiguity. v0.4 removes the mechanism of freezing: graph updates are equilibrium Metropolis moves with **exact** Woodbury determinant ratios (no stochastic-gradient rewiring, no autocorrelation blow-up by construction), and sizes extend to $`N = 1024`$ with explicit radial/zone diagnostics instead of a single core/void split.

**v0.3 (superseded before execution):** written for CPP v3.9; its protocol set targeted $`\varepsilon`$-box balances and penalty-exponent scans on soft ensembles. v4.0 replaced the tautological balance with Theorem 4.3 (independent channels), replaced soft ensembles with hard admissibility (L0)–(L4) + Proposition 3.2, and replaced the phenomenological H-LG narrative with the exact field closure. The v0.3 specification-gap fixes that remain relevant are absorbed here: schedule/budget consistency (§3.2, §10.1), concave control $`\ln(1+K)`$ (§3.2), pre-registered topology classifier (§7.2), rank-deficiency lesson for inclusion tests (§8.1).

---

*End of Technical Specification v0.4.*

*Normative parent: Causal Phase Program v4.0, §7–§10.*

*Canonical logic: Modified Brusentsov Entailment Logic, §§4–5.*
