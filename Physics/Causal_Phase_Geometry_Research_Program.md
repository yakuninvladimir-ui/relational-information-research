# Causal-Phase Geometry Research Program

**4D Continuum Limit, Relative Entropy, and the Correlation Functional**

**V. Yakunin**  
Updated draft — August 2026  
Status: active research program under hypothesis \(H_P\) only

---

## Abstract

A working hypothesis is proposed that unifies discrete causal microstructure, local proper time, discrete \(U(1)\) holonomies, and an information-theoretic derivation of the gravitational equations. The fundamental kinematics is a locally finite causal structure equipped with phase transport on oriented links. In the corresponding continuum limit, causal order together with volume information determine a Lorentzian metric, while the phase transport determines a \(U(1)\) gauge connection.

In the present revision the literal five-dimensional Kaluza–Klein interpretation and any free radion field are abandoned. The phase layer is treated strictly as an internal fibre bundle over the four-dimensional base (hypothesis \(H_P\)). Macroscopic gravity (the Einstein–Maxwell system) is obtained not from Jacobson’s phenomenological thermodynamics, but from rigorous quantum-information principles in the spirit of the Dorau–Mukha approach, in which the role of heat flux is played by the quantum relative entropy evaluated on a horizon.

Any “new physics” (dark-matter and dark-energy effects) is regarded not as independent fields, but as a correlation functional \(\Gamma_{\rm corr}\) that inevitably arises under large-scale coarse-graining because of hard informational constraints (a discrete analogue of the Bekenstein bound) on the underlying graph.

---

## 1. Status of the Construction and Mathematical Foundations

The program rests on the following established mathematical structures:

1. Locally finite partially ordered sets (causal sets).
2. Discrete \(U(1)\) connections and holonomies.
3. Geometry of principal bundles and the continuum Einstein–Maxwell system.
4. Derivation of semi-classical Einstein equations from quantum relative entropy (Araki–Uhlmann relative entropy) and modular theory (Dorau–Mukha approach).
5. The rigorous link between the Bekenstein bound and the non-negativity of relative entropy (Casini).

In contrast to earlier iterations, the following are **not** assumed:

- existence of a physical fifth dimension or a free radion field;
- introduction of ad-hoc equations of state (cosmological phases \(1\), \(1/3\), \(-1/3\), \(-1\)) prior to a strict computation of the effective dynamics.

---

## 2. Discrete Kinematics and the \(U(1)\) Sector

The fundamental structure is a locally finite partially ordered set \(C = (X,\prec)\), where \(x\prec y\) means that event \(x\) causally precedes event \(y\).

To every causal link an element \(U_{xy}\in U(1)\) is assigned that describes parallel transport of phase.

The baseline microscopic dynamics of the gauge sector is a Wilson-type functional evaluated on causal diamonds (or lattice plaquettes in the pilot lattice realisation):

\[
S_{U(1)}[U;C] = \sum_D\frac{1}{g_*^2}\,w_D\bigl(1-\operatorname{Re}W_D\bigr),
\]

where \(W_D\) is the holonomy around the boundary of the diamond (plaquette). In the continuum limit of small phases this action becomes the standard Maxwell term

\[
-\frac{1}{4e^2}\int d^4x\sqrt{-g}\,F_{\mu\nu}F^{\mu\nu}.
\]

---

## 3. Rejection of 5D (Radion) and Fixation of Hypothesis \(H_P\)

Instead of a five-dimensional Kaluza–Klein geometry with a dynamical radion \(\phi(x)\), the phase layer is fixed as an internal space:

\[
U(1)\hookrightarrow P\xrightarrow{\pi}M_4.
\]

The internal normalisation of the fibre is held strictly fixed (\(\delta\ell_*=0\)); free scalar modes are absent.

Abandonment of the physical-radion hypothesis (\(H_R\)) removes conflicts with stringent local constraints on weak-equivalence-principle violation (MICROSCOPE), variations of fundamental constants, and torsion-balance tests. All observed anomalies must be explained solely by the non-local collective response of the underlying causal-phase structure.

---

## 4. Relative Entropy and the Generation of Gravity

In place of the classical macroscopic relation \(\delta Q=T\,\delta S_H\), the macroscopic geometry is derived from the informational capacity of the graph.

### 4.1. Dynamical vacuum and perturbations

On a finite causal diamond one defines:

- **Dynamical vacuum \(\rho_{\rm dyn}\)** — the state localised near flat connections (\(W_D\approx 1\)) that minimises the average action \(\langle S_{U(1)}\rangle\).
- **Perturbed state \(\sigma\)** — a phase distribution whose average action is bounded by an energy-like quantity \(E\) (analogue of energy-constrained states).

### 4.2. Bekenstein-type bound on the graph

In place of a continuous area one uses a discrete analogue — an antichain (transverse section of the diamond) consisting of \(N_\partial\) links. The distinguishability of \(\sigma\) from the vacuum is measured by the Kullback–Leibler divergence \(D_{\rm KL}(\sigma\|\rho_{\rm dyn})\).

In accordance with an informational Bekenstein bound, the maximum amount of information that can cross the boundary of the diamond at given energy is strictly limited by the geometry of the graph:

\[
D_{\rm KL}(\sigma\|\rho_{\rm dyn})\le c\cdot N_\partial.
\]

In the continuum limit, following the logic of Dorau and Mukha, the relative entropy of a field perturbation (expressed through gradients of \(\operatorname{Re}W_D\), i.e., through the tensor \(F_{\mu\nu}F^{\mu\nu}\)) is proportional to the variation of horizon area. From this proportionality the semi-classical Einstein equations follow automatically.

---

## 5. Origin of the Correlation Functional \(\Gamma_{\rm corr}\)

The global effective dynamics under hypothesis \(H_P\) takes the form

\[
\Gamma_P=\Gamma_0[g,A,\Psi]+\Gamma_{\rm corr}[g,A,\Psi],
\]

where \(\Gamma_0\) is the standard Einstein–Maxwell action.

The term \(\Gamma_{\rm corr}\) is not postulated phenomenologically; it arises as the mathematical remainder of the large-scale coarse-graining operation. At low energy \(E\) the phase distribution optimises into weak coherent gradients (free electrodynamics). When one attempts to localise large field-strength fluxes, the system encounters a localisation penalty dictated by the Bekenstein-type bound (\(N_\partial\)).

Because the discrete Gauss theorem holds only up to combinatorial corrections, the exact balance between the internal phase action and the boundary throughput capacity is imperfect. This statistical remainder generates an effective non-local geometric response:

\[
H_{\mu\nu}^{\rm corr}=-\frac{2}{\sqrt{-g}}\frac{\delta\Gamma_{\rm corr}}{\delta g^{\mu\nu}}.
\]

This macroscopic response is intended to replace the need for independent dark-matter and dark-energy fields.

---

## 6. Pilot Numerical Programme (v0.1)

The first concrete computational step is a minimal stochastic check of the appearance of a measurable residual under informational truncation of the \(U(1)\) measure. Full technical specification is given in the companion document

**[Technical Specification v0.1.1 — \(\Gamma_{\rm corr}\) Extraction](./Technical_Specification_v0.1.1_Gamma_corr_Extraction.md)**

### Goal of stage v0.1

Answer the question:  
*Does informational truncation of the \(U(1)\) measure produce a measurable, stable, non-local residual of the effective action?*

### Explicitly outside the scope of v0.1

- derivation of the Einstein equation;
- fitting of SPARC / DESI data;
- full modular / Araki–Uhlmann relative-entropy calculation;
- five-dimensional geometry or radion;
- Brusentsov ternary logic.

### Success criterion of v0.1

A reproducible numerical answer (yes/no + magnitude) for the existence of a stable residual under a prescribed constraint, together with a complete log of parameters, seeds and null tests.

### Outline of the pilot pipeline

1. **Lattice \(U(1)\) (Wilson)** on a 3-d Euclidean lattice with periodic boundaries; Heat-Bath + over-relaxation updates; measurement of plaquette observables and integrated autocorrelation time.
2. **Operational diamond / boundary** — rectangular or Manhattan region; boundary edges \(N_\partial\); collar of plaquettes that touch the boundary; extraction of gauge-invariant descriptors \(\{\operatorname{Re}U_p\}\).
3. **Two ensembles** — vacuum \(\rho\) (pure Wilson) and perturbed \(\sigma\) (Wilson + gauge-invariant plaquette or Wilson-loop bias of strength \(\kappa\)).
4. **Classical \(D_{\rm KL}\)** evaluated exclusively on gauge-invariant boundary descriptors; hard or soft threshold \(B=c\cdot N_\partial\); configurations exceeding the threshold receive weight zero or an exponential penalty.
5. **Residual effective action** — comparison of the full and truncated measures; proxy \(\Delta F\approx-\log\langle w\rangle\) (soft) or \(-\log(N_{\rm accept}/N_{\rm total})\) (hard).
6. **Diagnostics** — null source (\(\kappa=0\)), null threshold (\(c\to\infty\)), shuffle of boundary descriptors, volume and shape scans, seed scan, locality test (source deep inside versus on the collar).

Only after a closed report of stage v0.1 may work proceed to improved KL estimators, non-local descriptors, or any contact with SPARC / cosmology.

---

## 7. Experimental Verification Programme (post-v0.1)

Because the radion hypothesis \(H_R\) is frozen, the test programme concentrates on the search for a single coherent structure of the kernel of \(\Gamma_{\rm corr}\).

1. **Variational problem on the graph** — compute analytically and numerically the dependence of \(D_{\rm KL}\) on \(N_\partial\) and \(E\); extract the continuum form of \(\Gamma_{\rm corr}\).
2. **Galactic tests (SPARC)** — verify whether the computed \(\Gamma_{\rm corr}\) reproduces the observed mass-discrepancy versus baryonic-acceleration relation without free parameters; independent check of the radial response kernel \(K(r,r')\).
3. **Cosmological tests** — the same functional must reproduce the full set of data: \(H(z)\), DES-SN5YR luminosity distances (including the time-dilation profile \(\Delta t_{\rm obs}=(1+z)\Delta t_{\rm em}\)), DESI BAO, and lensing.
4. **Falsifiability criterion** — if the \(\Gamma_{\rm corr}\) obtained from the informational bound requires mutually irreducible coefficients for galactic rotation curves and cosmological expansion, the hypothesis is rejected.

---

## 8. Relation to Earlier Documents

- The previous competing-branch document (July 2026) that kept both \(H_R\) and \(H_P\) is superseded by the present single-hypothesis formulation.
- The technical note on KK–Jacobson commutativity remains on record as an exploration of the abandoned 5-d route; its mathematical condition is no longer part of the active programme.
- Working data under `Physics/old_test/` are retained for continuity but are not part of the formal deliverables of the current programme.

---

## 9. What This Document Does Not Claim

- It does not claim that \(\Gamma_{\rm corr}\) has already been computed or that it fits SPARC or cosmological data.
- It does not identify the discrete threshold \(c\cdot N_\partial\) with the continuum Bekenstein–Casini bound; the threshold is a working constraint used in the pilot numerics.
- It does not claim a derivation of the Einstein equation from the classical KL divergence used in stage v0.1; that divergence is a classical proxy.
- It does not re-introduce a free radion or a physical fifth dimension.

---

*End of document. Companion technical specification: Technical_Specification_v0.1.1_Gamma_corr_Extraction.md*
