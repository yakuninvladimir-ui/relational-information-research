# Technical Specification v0.1.1 (FINAL)

## Minimal Software Complex for Stochastic Verification of the Appearance of \(\Gamma_{\rm corr}\) in the Causal-Phase Model \(H_P\)

**Version:** 0.1.1-FINAL (pilot)  
**Date:** 24 August 2026  
**Status:** executable technical specification of the first stage  
**Goal of the stage:** answer the question *“Does informational truncation of the \(U(1)\) measure produce a measurable, stable, non-local residual of the effective action?”*  
**Outside the scope of the stage:** derivation of the Einstein equation, SPARC/DESI fitting, full modular / Araki–Uhlmann relative entropy, 5D/radion, Brusentsov logic.

---

## 0. Scope and Boundaries of v0.1

| Included in v0.1 | Excluded from v0.1 |
| :--- | :--- |
| Lattice \(U(1)\) (Wilson) | Dynamical metric / gravity on the lattice |
| Classical \(D_{\rm KL}\) on gauge-invariant descriptors | Full modular / Araki–Uhlmann calculation |
| Simple cut / penalty by threshold | Ternary logic, nullity selection |
| Comparison of full and truncated measures | Export of \(K(r,r')\) for SPARC |
| Diagnostics of presence/absence of residual | Cosmology, magnetars, \(\Gamma_{\rm corr}\) “on all scales” |

**Success criterion of v0.1:** a reproducible numerical answer (yes/no + magnitude) for the existence of a stable residual under a prescribed constraint; complete log of parameters, seeds and null tests.

---

## 1. Lattice \(U(1)\) (Wilson) + Configuration Updates

### 1.1. Requirements
- Three-dimensional Euclidean lattice \(L_x\times L_y\times L_\tau\) with periodic boundary conditions.
- On every oriented edge a variable \(U_e\in U(1)\), \(U_e=e^{i\theta_e}\), \(\theta_e\in[0,2\pi)\).
- Microscopic Wilson action:
  \[
  S[U]=\beta\sum_p\bigl(1-\operatorname{Re}U_p\bigr),\qquad
  U_p=U_\mu(x)\,U_\nu(x+\hat\mu)\,U_\mu^\dagger(x+\hat\nu)\,U_\nu^\dagger(x),
  \]
  where \(p\) runs over plaquettes and \(\beta=1/g_*^2\).
- Update algorithm: **Heat-Bath** for \(U(1)\) plus **over-relaxation** cycles (to reduce autocorrelation).
- Measurements: mean \(\langle\operatorname{Re}U_p\rangle\), Polyakov lines (optional), integrated autocorrelation time \(\tau_{\rm int}\).

### 1.2. Code
- Language: **Python 3.10+** (NumPy / Numba) for the prototype. GPU acceleration is **not required** in v0.1.
- Modules:
  - `lattice.py` — geometry, edge/plaquette indexing, PBC;
  - `wilson_action.py` — evaluation of \(S\), local heat-bath update of a single edge;
  - `overrelax.py` — over-relaxation sweep;
  - `measure.py` — observables and estimation of \(\tau_{\rm int}\) (binning / autocorrelation).
- Input: \(L\), \(\beta\), number of thermalisation sweeps, number of measurement sweeps, seed.
- Output: array of configurations (or online accumulation of observables), log of \(\langle S\rangle\), \(\tau_{\rm int}\).

### 1.3. Data
- Synthetic: generated inside the Monte Carlo.
- Checkpoints: save 10–50 configurations in HDF5/NPZ for reproducibility and subsequent diamond analyses (not thousands of full volumes — RAM/disk economy).
- Default parameters (pilot): \(L\in\{12,16,20\}\); \(L=24\) optional if time permits; \(\beta\in\{0.5,1.0,1.5,2.0\}\).

### 1.4. Computational resources
- **Target machine:** Ryzen 5 5500 (6c/12t), 16 GB RAM, RX 6650 XT (GPU unused in v0.1).
- CPU + Numba + `joblib`/`multiprocessing` over seeds and \(\kappa\).
- RAM: do not store mass full-configs; write boundary descriptors, weights and flags.

### 1.5. Estimated implementation time
- 3–7 working days (pure Python + Numba).

### 1.6. Acceptance criteria for item 1
- [ ] Reproduction of the known \(U(1)\) order/disorder behaviour versus \(\beta\).
- [ ] \(\tau_{\rm int}\) measured and \(\lt 50\) sweeps at working \(\beta\).
- [ ] Configurations saved and loaded without loss of precision (FP64).

---

## 2. Definition of the Diamond / Boundary and \(N_\partial\)

### 2.1. Requirements
- Operational definition of a **diamond-like subregion** \(D\) on the Euclidean lattice (no claim of true Lorentzian causality at this stage).
- Recommended pilot variant:
  - “Spatial” slice: fixed interval in \(\tau\), rectangular (or diamond-shaped in the 2-d section) region in \((x,y)\);
  - Boundary \(\partial D\) = set of edges that have exactly one endpoint inside \(D\);
  - \(N_\partial\) = number of such boundary edges (discrete geometric scale, analogue of “area”). Used in the threshold \(B=c\cdot N_\partial\).
- **Boundary collar:** all plaquettes that possess **at least one** edge on \(\partial D\). Gauge-invariant descriptors are built from these plaquettes. Their number is logged separately from \(N_\partial\).
- Alternative (to be coded as an option): cube / ball in the Manhattan metric; comparison of \(N_\partial\) between definitions.
- For every configuration one must be able to extract the vector \(\{\operatorname{Re}U_p\}\) of the collar plaquettes.

### 2.2. Code
- `diamond.py`:
  - `define_region(L, center, size, shape="rect"|"manhattan")`;
  - `boundary_edges(region) \to list[edge_id]`;
  - `N_boundary(region) \to int`;
  - `collar_plaquettes(region) \to list[plaquette_id]`;
  - `extract_boundary_plaquettes(config, region) \to ndarray`  # \(\operatorname{Re}U_p\) of the collar.
- Unit tests: on \(L=4,6,8\) verify \(N_\partial\) and the composition of the collar by hand counting.

### 2.3. Data
- Table: \((L,\text{size},\text{shape})\to N_\partial\), number of collar plaquettes.
- Set of gauge-invariant boundary descriptors in JSON/HDF5 next to the run metadata.

### 2.4. Computational resources
- Negligible (\(O(\text{volume})\) once).

### 2.5. Estimated implementation time
- 1–2 working days.

### 2.6. Acceptance criteria for item 2
- [ ] \(N_\partial\) is deterministic and documented for every `shape`.
- [ ] Collar is defined unambiguously: plaquettes with \(\ge 1\) edge on \(\partial D\).
- [ ] Extraction of \(\operatorname{Re}U_p\) of the collar coincides with direct indexing.
- [ ] At least two distinct boundary definitions exist for null comparison.

---

## 3. Two Ensembles: “Vacuum” and “Perturbation”

### 3.1. Requirements
- **Ensemble \(\rho\) (dynamical / “vacuum”):** ordinary thermal Wilson ensemble at given \(\beta\), no external source.
- **Ensemble \(\sigma\) (perturbation):** same \(\beta\), but with a **gauge-invariant** source. Fixing individual \(\theta_e\) or introducing a link-linear bias of the form \(\sum J_e\theta_e\), \(\cos(\theta_e-\theta_{\rm cl})\) is forbidden.

  Admissible source variants (choose one as default, the second as option):

  - **A (recommended):** plaquette bias  
    \[
    S_\sigma=S[U]-\kappa\sum_{p\in P_*}\operatorname{Re}U_p,
    \]
    where \(P_*\) is a fixed set of plaquettes inside the diamond and/or on the boundary collar.

  - **B:** bias by a small / medium Wilson loop  
    \[
    S_\sigma=S[U]-\kappa\operatorname{Re}W_\gamma,
    \]
    \(\gamma\) defines a non-trivial flux compatible with the diamond boundary.

- Strength parameter \(\kappa\) is scanned; as \(\kappa\to 0\) the ensemble \(\sigma\) must coincide with \(\rho\).
- Both ensembles are generated by the same update code (the only difference is the gauge-invariant term in the action).

### 3.2. Code
- `ensemble.py`:
  - `run_vacuum(L, beta, n_therm, n_meas, seed)`;
  - `run_perturbed(L, beta, source_spec, kappa, n_therm, n_meas, seed)`;
  - `source_spec` — JSON with type (`plaquette_bias` | `wilson_loop_bias`), list of plaquettes/loops, no link-level fixings.
- Storage: directories `vacuum/` and `perturbed_k{kappa}/` with metadata.

### 3.3. Data
- For each \((L,\beta,\kappa)\): \(\ge 200\)–\(1000\) approximately independent configurations (accounting for \(\tau_{\rm int}\)).
- Metadata: seed, \(\beta\), \(\kappa\), `source_spec`, \(N_\partial\), number of collar plaquettes.

### 3.4. Computational resources
- Main load of the stage.
- \(L=16\): Ryzen 5 5500, hours–days for a grid of \(\beta,\kappa\).
- \(L=20\): admissible; \(L=24\) only if time reserve exists, with reduced statistics.

### 3.5. Estimated implementation time
- 2–4 working days (on top of item 1).

### 3.6. Acceptance criteria for item 3
- [ ] Vacuum and perturbation differ only by an explicitly given **gauge-invariant** source.
- [ ] The source does not fix individual \(\theta_e\) and does not introduce a link-linear bias.
- [ ] As \(\kappa\to 0\) the observables of \(\sigma\) converge to those of \(\rho\).
- [ ] Logs are fully reproducible from the seed.

---

## 4. Classical \(D_{\rm KL}\) and Simple Cut / Penalty

### 4.1. Requirements
- **Classical** estimate of the distinguishability of distributions of **only gauge-invariant** observables associated with the boundary:
  \[
  D_{\rm KL}(\hat p_\sigma\|\hat p_\rho)
  =\sum_i\hat p_\sigma(i)\log\frac{\hat p_\sigma(i)}{\hat p_\rho(i)}.
  \]
- Descriptors (choose default + option):
  1. Vector \(\operatorname{Re}U_p\) of the plaquettes of the **collar** \(\partial D\) (all plaquettes with \(\ge 1\) edge on the boundary).
  2. Small Wilson loops supported on / piercing the boundary.
  3. After dimensional reduction — kNN / KDE estimate of \(D_{\rm KL}\) in the space of these invariants.
- **Raw phases of boundary links \(\theta_e\) are never used.**
- **Threshold:** \(B=c\cdot N_\partial\) with \(c\) a scanned parameter (e.g. \(c\in\{0.1,0.5,1.0,2.0\}\)).  
  *Important:* this is a **working hypothesis of truncation** (constraint threshold), not a claim that it realises the Casini bound. In the report write “constraint threshold”, not “Bekenstein”.
- **Cut:** configurations of \(\sigma\) for which \(D_{\rm KL}>B\) receive weight 0 (hard cut) **or** a soft penalty \(w=\exp\bigl(-\lambda(D_{\rm KL}-B)_+\bigr)\).
- No Brusentsov logic, no ternary DNF.

### 4.2. Code
- `kl_estimate.py`:
  - construction of empirical distributions strictly from gauge-invariant descriptors;
  - `kl_div(p_sigma, p_rho)`;
  - `apply_threshold(configs, kl_values, B, mode="hard"|"soft")`;
  - smoke test: a random local gauge transformation of a configuration must leave \(D_{\rm KL}\) unchanged (within numerical noise).
- Unit tests on synthetic distributions (known KL).

### 4.3. Data
- Tables: for every configuration of \(\sigma\) — \(D_{\rm KL}\), accept/reject flag, weight.
- Summary: fraction rejected versus \((L,\beta,\kappa,c)\).

### 4.4. Computational resources
- Post-processing after generation (minutes–hours on CPU).

### 4.5. Estimated implementation time
- 2–5 working days.

### 4.6. Acceptance criteria for item 4
- [ ] Estimate of \(D_{\rm KL}\) is **strictly independent** of local gauge transformations.
- [ ] Descriptors contain no raw \(\theta_e\).
- [ ] At \(\kappa=0\) the mean \(D_{\rm KL}\approx 0\) (within noise).
- [ ] Fraction rejected grows monotonically with \(\kappa\) and falls with increasing \(c\).
- [ ] Both hard and soft modes are implemented.

---

## 5. Comparison of Full and Truncated Measures → Residual Effective Action

### 5.1. Requirements
- Full measure: ensemble \(\sigma\) without cut (or with \(c\to\infty\)).
- Truncated measure: the same ensemble after hard/soft cut on \(D_{\rm KL}\).
- Estimate of the **difference of free energies** / effective action caused by the truncation.
  - Simplest proxy for v0.1:
    \[
    \Delta F\approx-\log\frac{Z_{\rm trunc}}{Z_{\rm full}}
    \approx-\log\bigl(\langle w\rangle_{\rm full}\bigr)
    \]
    (soft) or \(-\log(N_{\rm accept}/N_{\rm total})\) (hard, with caution).
  - More carefully (optional): thermodynamic integration / reweighting with respect to the penalty parameter \(\lambda\).
- Dependence of \(\Delta F\) on the background strength \(\kappa\) and on \(N_\partial\) (different diamond sizes).
- Goal: to understand whether a **systematic** residual appears that depends non-trivially on the background (not merely a local renormalisation).

### 5.2. Code
- `residual.py`:
  - `delta_F_hard(accept_fraction)`;
  - `delta_F_soft(weights)`;
  - (optional) `thermodynamic_integration_lambda(...)`;
  - recording of \(\Delta F(\kappa,L,c,\beta)\).
- Visualisation: curves \(\Delta F\) versus \(\kappa\) for different \(c\), \(L\).

### 5.3. Data
- Table/CSV + plots in `results/residual/`.
- Raw weights and accept flags — in HDF5.

### 5.4. Computational resources
- Post-processing; under reweighting — additional generation at intermediate \(\lambda\).

### 5.5. Estimated implementation time
- 2–4 working days.

### 5.6. Acceptance criteria for item 5
- [ ] As \(c\to\infty\) (no cut) \(\Delta F\to 0\).
- [ ] As \(\kappa\to 0\) \(\Delta F\to 0\).
- [ ] Quantitative dependence \(\Delta F(\kappa)\) with error estimate exists.
- [ ] Result is reproduced under a change of seed.

---

## 6. Diagnostics: Is There a Non-Zero, Stable, Non-Local Residual?

### 6.1. Requirements
Mandatory set of null and stability tests:

1. **Null source:** \(\kappa=0\) → \(\Delta F\) compatible with zero.
2. **Null threshold:** very large \(c\) → \(\Delta F\to 0\).
3. **Shuffle boundary:** random permutation / mixing of the **gauge-invariant** collar descriptors (\(\operatorname{Re}U_p\)) at the same \(N_\partial\); \(\Delta F\) must disappear or drop strongly. (Do not shuffle raw link phases.)
4. **Volume scan:** \(L=12,16,20\) (and \(24\) if possible) — scaling of \(\Delta F\) with \(N_\partial\) or with volume.
5. **Shape scan:** two boundary definitions (rect vs Manhattan) — qualitatively the same conclusion.
6. **Seed scan:** \(\ge 3\) independent seeds; confidence intervals.
7. **Locality (crude):** compare the residual when the support of the source \(P_*/\gamma\) lies deep inside the diamond versus on the boundary collar; if there is no difference at the same \(\kappa\) — suspicion of a purely local / normalisation effect.

**Interpretation (for the report, not for the code):**
- If after all tests \(\Delta F\) is stably non-zero and depends non-trivially on the background / boundary geometry → “pilot signal in favour of the possibility of \(\Gamma_{\rm corr}\)”; proceed to v0.2.
- If \(\Delta F\) vanishes in the null tests or is unstable → “in the present formulation informational truncation does not produce a measurable residual”; a negative result is recorded (and is valuable).

### 6.2. Code
- `diagnostics.py` — run of all tests, summary table pass/fail + numerical values.
- `report.md` / Jupyter notebook — automatic generation of a short report.

### 6.3. Data
- Summary JSON/CSV: all points \((L,\beta,\kappa,c,\mathrm{seed})\), \(\Delta F\), errors, test flags.
- Plots in `results/diagnostics/`.

### 6.4. Computational resources
- Repeated runs of items 3–5 on CPU (main consumer of wall-clock time).

### 6.5. Estimated implementation time
- 2–3 working days for automation + machine time for the runs.

### 6.6. Acceptance criteria for item 6
- [ ] All seven diagnostics executed and documented.
- [ ] An unambiguous conclusion: “signal present / signal absent / data insufficient” with indication of which test was lacking.

---

## 7. Stack, Precision, Repository

| Component | Requirement v0.1 |
| :--- | :--- |
| Language | Python 3.10+, NumPy, SciPy, h5py, matplotlib; **Numba mandatory** |
| Precision | FP64 for angles, action, KL, \(\Delta F\) |
| Parallelism | `multiprocessing` / `joblib` over seeds and over \(\kappa\) (`n_workers \approx 10` on Ryzen 5 5500) |
| GPU | **not used** in v0.1 |
| Version control | git; every run — commit hash + config YAML in the metadata |
| Reproducibility | a single `config.yaml` + seed completely determines the result |
| Tests | pytest: geometry, collar, synthetic KL, gauge invariance of KL, limits \(\kappa\to 0\), \(c\to\infty\) |

**Target hardware:** Ryzen 5 5500, 16 GB RAM, ≥50 GB disk.  
`store_full_configs: false` by default.

---

## 8. Execution Plan (Checklist)

| Stage | Content | Estimated effort | Dependencies |
| :--- | :--- | :--- | :--- |
| E0 | Repository, config YAML, logging, FP64 policy | 0.5–1 day | — |
| E1 | Item 1: Wilson + heat-bath + overrelax + measure | 3–7 days | E0 |
| E2 | Item 2: diamond, \(N_\partial\), collar, boundary plaquettes | 1–2 days | E1 |
| E3 | Item 3: vacuum / **invariant** perturbation, grid \(\beta,\kappa\) | 2–4 days | E1, E2 |
| E4 | Item 4: KL on plaquettes, hard/soft cut, gauge-invariance test | 2–5 days | E3 |
| E5 | Item 5: \(\Delta F\), curves vs \(\kappa\) | 2–4 days | E4 |
| E6 | Item 6: full set of diagnostics + report | 2–3 days + machine time | E5 |
| E7 | Writing of `REPORT_v0.1.md` with conclusion | 1–2 days | E6 |

**Total (person):** orientative **2.5–5 weeks** of development + **several days – 1–2 weeks** of machine time for the grid \((L,\beta,\kappa,c,\mathrm{seed})\).

**Critical path:** E1 → E3 → E4 → E5 → E6.

---

## 9. Deliverables of v0.1

1. Repository with code and `README` (build, one pilot run).
2. `config.yaml` + set of used configs.
3. Raw results in HDF5/NPZ (descriptors, weights, KL, flags, \(\Delta F\); full-config optional and sparse).
4. `REPORT_v0.1.md`:
   - statement of the problem;
   - definition of the diamond, \(N_\partial\), collar;
   - KL method (only invariants) and threshold;
   - tables/plots of \(\Delta F(\kappa)\);
   - results of all diagnostics;
   - **unambiguous conclusion** (signal / no signal / insufficient data);
   - limitations of v0.1 and what is carried to v0.2.
5. Reproducible script `run_pilot.sh` / `make pilot`.

---

## 10. Explicit Prohibitions of v0.1 (to prevent scope creep)

- Do not declare \(D_{\rm KL}\le c\cdot N_\partial\) “the Bekenstein bound according to Casini”.
- Do not introduce Brusentsov logic / ternary implication.
- Do not tune the threshold \(c\) to obtain a desired non-zero \(\Delta F\).
- Do not export \(K(r,r')\) and do not compare with SPARC.
- Do not claim that the quantum relative entropy of Araki–Uhlmann has been computed.
- Do not change the definition of the boundary *after* inspecting \(\Delta F\).
- Do not use raw \(\theta_e\) as KL descriptors and do not set the source by fixing individual links.

---

## 11. Criterion for Transition to v0.2

v0.2 is opened **only** if `REPORT_v0.1.md` records one of the two outcomes:

- **A.** Stable non-zero residual that passed the null tests → then: improved KL estimators / reweighting, first probes of non-local descriptors, cautious link to an effective operator.
- **B.** Stable zero residual → then: either a change of the constraint definition (modular proxy, different descriptor), or a documented negative result for the present realisation of \(H_P\)-truncation.

Without a closed report of v0.1, work on SPARC, magnetars, replicas and \(\Gamma_{\rm corr}\) “on all scales” does not begin.

---

*End of Technical Specification v0.1.1-FINAL*
