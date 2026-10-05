# KK–Jacobson Commutativity Note

**Discrete Causal Structure, U(1) Holonomies, and the Thermodynamic Origin of the Einstein–Maxwell System**

V. Yakunin

July 15, 2026

---

## Abstract

A minimal working hypothesis is proposed that combines three mathematically established constructions: discrete causal order, a U(1) gauge connection, and the thermodynamic derivation of the Einstein equations.

At the fundamental level, the gravitational sector is associated with the structure of a causal network, whereas the electromagnetic sector is described by U(1) phase variables assigned to its links. In the continuum limit, this system is interpreted as a four-dimensional Lorentzian geometry equipped with a principal U(1) bundle. Its geometric lift to five dimensions has Kaluza–Klein form.

The central hypothesis is that Jacobson’s local thermodynamic principle should be applied to the complete five-dimensional geometry. After reduction, the five-dimensional equation of state should generate the four-dimensional Einstein equations, Maxwell equations, and the radion equation.

The construction contains no derivation of dark energy, dark matter, or the four conjectured equation-of-state regimes. These interpretations must be obtained from the dynamics rather than introduced as initial postulates.

---

## Contents

1. [Status of the Hypothesis](#1-status-of-the-hypothesis)
2. [Discrete Kinematics](#2-discrete-kinematics)
   - 2.1 [Causal structure](#21-causal-structure)
   - 2.2 [U(1) connection on the causal network](#22-u1-connection-on-the-causal-network)
3. [Continuum Limit](#3-continuum-limit)
4. [Kaluza–Klein Geometric Lift](#4-kaluzaklein-geometric-lift)
5. [Five-Dimensional Horizon Thermodynamics](#5-five-dimensional-horizon-thermodynamics)
   - 5.1 [Local five-dimensional horizon](#51-local-five-dimensional-horizon)
   - 5.2 [Five-dimensional Raychaudhuri equation](#52-five-dimensional-raychaudhuri-equation)
   - 5.3 [Five-dimensional equation of state](#53-five-dimensional-equation-of-state)
6. [Reduction of the Thermodynamic Equation](#6-reduction-of-the-thermodynamic-equation)
7. [Entropy and the Size of the Compact Layer](#7-entropy-and-the-size-of-the-compact-layer)
8. [Equilibrium Einstein–Maxwell Regime](#8-equilibrium-einsteinmaxwell-regime)
9. [Nonequilibrium Regime](#9-nonequilibrium-regime)
10. [Four Conjectured Regimes](#10-four-conjectured-regimes)
11. [Relation to Holography](#11-relation-to-holography)
12. [Central Consistency Condition](#12-central-consistency-condition)
13. [Falsification Criteria](#13-falsification-criteria)
14. [Minimal Computational Program](#14-minimal-computational-program)
15. [Final Formulation of the Hypothesis](#15-final-formulation-of-the-hypothesis)
16. [References](#references)

---

## 1 Status of the Hypothesis

Three levels of claims are distinguished in this work.

**Established mathematical elements:**

1. causal partial order and locally finite causal sets;
2. discrete U(1) connections and holonomies;
3. geometry of principal bundles;
4. Kaluza–Klein reduction;
5. the Raychaudhuri equation;
6. Unruh temperature and horizon entropy;
7. the thermodynamic derivation of the Einstein equation in Jacobson’s construction.

**Central hypothesis:**

```
causal network with a U(1) connection
  → four-dimensional geometry with a U(1) bundle
  → five-dimensional Kaluza–Klein geometry
  → local horizon thermodynamics
  → Einstein–Maxwell–radion system.
```

**Not yet derived:**

- the origin of the compactness of the fifth dimension;
- stabilization of its radius;
- cosmological relaxation;
- effective dark energy;
- galactic dynamics without dark matter;
- the phase sequence \(1,\; 1/3,\; -1/3,\; -1\).

---

## 2 Discrete Kinematics

### 2.1 Causal structure

The fundamental structure is a locally finite partially ordered set,

$$
\mathcal{C} = (X, \prec),
$$

where \(x \prec y\) means that event \(x\) causally precedes event \(y\).

No external global time is assumed. Proper time between causally related events may be related approximately to the length of a maximal chain:

$$
\tau_{\mathcal{C}}(x, y) = \tau_* \max_{\gamma:\, x \rightsquigarrow y} |\gamma|.
$$

The number of elements in the causal interval

$$
I(x, y) = \{z \in X \mid x \prec z \prec y\}
$$

plays the role of a discrete volume measure:

$$
V(x, y) \sim v_* \, |I(x, y)|.
$$

In the continuum limit, causal order should reproduce light cones, while element counting should reproduce Lorentzian volume.

### 2.2 U(1) connection on the causal network

Associate to each oriented causal link \(x \prec y\) a group element

$$
U_{xy} \in \mathrm{U}(1), \qquad U_{xy} = e^{iq a_{xy}}.
$$

It describes parallel transport of the phase of a charged state between two events.

If the field at a vertex transforms as

$$
\psi_x \longrightarrow g_x \psi_x, \qquad g_x \in \mathrm{U}(1),
$$

then the discrete connection transforms according to

$$
U_{xy} \longrightarrow g_x U_{xy} g_y^{-1}.
$$

Parallel transport along a causal chain

$$
\gamma : x = x_0 \prec x_1 \prec \cdots \prec x_n = y
$$

is defined by the product

$$
U(\gamma) = \prod_{j=0}^{n-1} U_{x_j x_{j+1}}.
$$

Because causal order contains no directed closed cycles, discrete curvature is defined by comparing two distinct chains with the same endpoints:

$$
\gamma_1 : x \rightsquigarrow y, \qquad \gamma_2 : x \rightsquigarrow y.
$$

The corresponding relative holonomy is

$$
W(\gamma_1, \gamma_2) = U(\gamma_1)\, U(\gamma_2)^{-1}.
$$

If

$$
W(\gamma_1, \gamma_2) \neq 1,
$$

then the result of phase transport depends on the selected causal path. This is the discrete analogue of nonzero curvature,

$$
F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu.
$$

Thus, in the initial picture,

$$
\begin{aligned}
\text{gravitational sector} &= \text{structure and dynamics of causal order}, \\
\text{electromagnetic sector} &= \mathrm{U}(1)\text{ connection on causal links}.
\end{aligned}
$$

The photon should therefore be interpreted not as the phase of an individual particle, but as a propagating excitation of the connection \(U_{xy}\) itself.

---

## 3 Continuum Limit

Assume the existence of a coarse-graining regime in which

$$
(\mathcal{C}, U_{xy}) \longrightarrow (M_4, g_{\mu\nu}, A_\mu).
$$

Causal order and the discrete volume measure generate a four-dimensional Lorentzian geometry \(g_{\mu\nu}\), while discrete holonomies become a U(1) connection \(A_\mu\):

$$
U_{xy} \simeq \exp\left[iq \int_x^y A_\mu\, dx^\mu\right].
$$

At this level, gravitation and electromagnetism are geometric objects of different types:

$$
g_{\mu\nu} = \text{metric of the base},
$$

$$
A_\mu = \text{connection on the U(1) layer over the base}.
$$

They can be unified through a five-dimensional geometric lift, but need not be identified.

---

## 4 Kaluza–Klein Geometric Lift

Consider the principal bundle

$$
\mathrm{U}(1) \hookrightarrow \hat{M}_5 \longrightarrow M_4.
$$

The five-dimensional metric is written as

$$
d\hat{s}^2 = e^{-2\alpha\phi(x)}\, g_{\mu\nu}(x)\, dx^\mu dx^\nu + e^{4\alpha\phi(x)}\, \bigl[dy + \kappa A_\mu(x)\, dx^\mu\bigr]^2.
$$

Here:

- \(g_{\mu\nu}\) is the four-dimensional metric;
- \(A_\mu\) is the electromagnetic connection;
- \(y\) is the coordinate of the compact layer;
- \(\phi\) is the radion determining the physical size of the layer;
- \(\alpha\) and \(\kappa\) depend on normalization.

The combination

$$
\Theta_5 = dy + \kappa A_\mu\, dx^\mu
$$

is invariant under

$$
y \longrightarrow y - \kappa\lambda(x), \qquad A_\mu \longrightarrow A_\mu + \partial_\mu \lambda.
$$

Thus, four-dimensional gauge symmetry is interpreted as the freedom to choose a coordinate on the compact layer.

The fifth dimension need not be understood as a fundamental additional space; it may instead be viewed as a geometric representation of the internal U(1) phase.

---

## 5 Five-Dimensional Horizon Thermodynamics

### 5.1 Local five-dimensional horizon

At each point of the five-dimensional geometry, consider a local Rindler horizon with null tangent vector

$$
\hat{k}^A \hat{k}_A = 0.
$$

The area of its spatial cross-section in five dimensions is a three-dimensional quantity \(A_3\).

Take the horizon entropy to be

$$
S_5 = \frac{k_B c^3}{4\hbar G_5}\, A_3.
$$

The temperature of the locally accelerated observer is

$$
T_U = \frac{\hbar \hat{\kappa}}{2\pi c k_B}.
$$

Postulate the local equilibrium Clausius relation

$$
\delta Q_5 = T_U\, \delta S_5
$$

for all local five-dimensional Rindler horizons.

Thermodynamics is not treated here as an independent microscopic substance. It is a macroscopic law of coarse-grained causal geometry.

### 5.2 Five-dimensional Raychaudhuri equation

For a hypersurface-orthogonal five-dimensional null congruence,

$$
\frac{d\hat{\theta}}{d\lambda} = -\frac{1}{3}\hat{\theta}^2 - \hat{\sigma}_{AB}\hat{\sigma}^{AB} - \hat{R}_{AB}\, \hat{k}^A \hat{k}^B.
$$

The coefficient \(1/3\) appears because the transverse cross-section of a five-dimensional null congruence has dimension three.

It is **not** an equation of state

$$
w = -\frac{1}{3},
$$

and is not by itself related to coasting cosmology.

Equation (the Raychaudhuri equation above) converts five-dimensional curvature into a change of local horizon area.

### 5.3 Five-dimensional equation of state

Applying Jacobson’s logic to the Clausius relation and the Raychaudhuri equation should lead to the five-dimensional Einstein equation:

$$
\hat{G}_{AB} + \hat{\Lambda}\, \hat{g}_{AB} = \frac{8\pi G_5}{c^4}\, \hat{T}_{AB}.
$$

The cosmological constant arises as an integration constant. The thermodynamic derivation alone does not determine its magnitude.

---

## 6 Reduction of the Thermodynamic Equation

The five-dimensional Einstein equation separates into the components

$$
(A, B) = (\mu, \nu),\qquad (\mu, 5),\qquad (5, 5).
$$

After reduction, these components should yield, respectively,

$$
G_{\mu\nu} + \Lambda_4 g_{\mu\nu} = \frac{8\pi G_4}{c^4}\Bigl(T^{\mathrm{matter}}_{\mu\nu} + T^{\mathrm{EM}}_{\mu\nu} + T^{(\phi)}_{\mu\nu}\Bigr),
$$

$$
\nabla_\mu \bigl(e^{-a\phi} F^{\mu\nu}\bigr) = J^\nu,
$$

and

$$
\square\phi = \frac{\partial V_{\mathrm{eff}}}{\partial\phi} + C\, e^{-a\phi}\, F_{\mu\nu} F^{\mu\nu}.
$$

The coefficients \(a\) and \(C\) depend on the normalization chosen for the five-dimensional metric and the field \(A_\mu\).

The electromagnetic stress-energy tensor has the standard structure

$$
T^{\mathrm{EM}}_{\mu\nu} = e^{-a\phi}\left(F_{\mu\alpha} F_\nu{}^{\alpha} - \frac{1}{4} g_{\mu\nu} F_{\alpha\beta} F^{\alpha\beta}\right).
$$

Consequently, the central intersection of Kaluza–Klein and Jacobson is

```
5D local thermodynamics → 5D Einstein equation
                       → { 4D Einstein equation,
                           Maxwell equation,
                           radion equation }.
```

Thus, the Einstein equation is not derived from Maxwell’s equations. Both equations arise as different projections of one five-dimensional thermodynamic equation of state.

---

## 7 Entropy and the Size of the Compact Layer

Let the physical length of the compact layer be

$$
L_5 = 2\pi b.
$$

In a locally factorized regime, the five-dimensional horizon area is

$$
A_3 = L_5 A_2,
$$

where \(A_2\) is the area of the four-dimensional horizon cross-section.

Then

$$
S_5 = \frac{k_B c^3}{4\hbar G_5}\, L_5 A_2.
$$

If \(L_5\) is constant, define

$$
G_4 = \frac{G_5}{L_5},
$$

and obtain the ordinary four-dimensional entropy:

$$
S_5 = \frac{k_B c^3}{4\hbar G_4}\, A_2.
$$

For a variable layer size,

$$
\delta S_5 = \frac{k_B c^3}{4\hbar G_5}\bigl(L_5\, \delta A_2 + A_2\, \delta L_5\bigr).
$$

The first term describes the change in four-dimensional horizon area. The second term describes the change in the geometry of the compact layer. It is not a newly introduced arbitrary entropy component; it is the variation of an existing Kaluza–Klein degree of freedom.

---

## 8 Equilibrium Einstein–Maxwell Regime

The working equilibrium regime is defined by

$$
\phi \simeq \phi_0, \qquad \nabla_\mu \phi \simeq 0, \qquad \delta_i S \simeq 0.
$$

With consistent radion stabilization, the system approaches

$$
G_{\mu\nu} + \Lambda_4 g_{\mu\nu} = \frac{8\pi G_4}{c^4}\Bigl(T^{\mathrm{matter}}_{\mu\nu} + T^{\mathrm{EM}}_{\mu\nu}\Bigr),
$$

$$
\nabla_\mu F^{\mu\nu} = J^\nu.
$$

This regime is the candidate for the ordinary observed coupling of general relativity and electromagnetism.

However, the simple condition

$$
\phi = \mathrm{const}
$$

is not always a consistent solution of the full KK system. The radion equation imposes the additional constraint

$$
0 = \left.\frac{\partial V_{\mathrm{eff}}}{\partial\phi}\right|_{\phi_0} + C\, e^{-a\phi_0}\, F_{\mu\nu} F^{\mu\nu}.
$$

For an arbitrary varying electromagnetic field, this condition normally requires a stabilization mechanism or a special sector of solutions.

The radion cannot be removed merely by declaration.

---

## 9 Nonequilibrium Regime

Outside local equilibrium, one must use

$$
\delta S_5 = \frac{\delta Q_5}{T_U} + \delta_i S_5, \qquad \delta_i S_5 \geq 0.
$$

Nonequilibrium behavior may be associated with

$$
\nabla_\mu \phi \neq 0,
$$

$$
\delta L_5 \neq 0,
$$

$$
\hat{\sigma}_{AB}\hat{\sigma}^{AB} \neq 0,
$$

or other nonequilibrium deformations of the horizon.

Positive entropy production does not automatically imply

$$
p < 0
$$

or

$$
w \simeq -1.
$$

For a cosmological interpretation, one must independently derive the effective four-dimensional tensor

$$
T^{\mathrm{eff}}_{\mu\nu}
$$

and verify the acceleration condition

$$
\rho_{\mathrm{eff}} + 3 p_{\mathrm{eff}} < 0.
$$

Dark energy is therefore not yet a consequence of this hypothesis.

---

## 10 Four Conjectured Regimes

The sequence

$$
w \in \left\{1,\; \tfrac{1}{3},\; -\tfrac{1}{3},\; -1\right\}
$$

was considered previously.

In standard cosmology, these values correspond to:

| \(w\) | Standard interpretation |
|:-----:|-------------------------|
| \(1\) | stiff medium |
| \(1/3\) | isotropic massless radiation |
| \(-1/3\) | coasting regime or a network of stretched strings |
| \(-1\) | vacuum energy |

In the present version of the hypothesis, these values are **not** introduced as spatial phases.

In particular:

- a black hole is defined by trapped surfaces, not by a universal value \(w = 1\);
- ordinary galactic matter has approximately \(w = 0\), not \(w = 1/3\);
- \(w = -1/3\) does not follow automatically from the Raychaudhuri equation;
- \(w = -1\) does not follow from entropy production.

The four values can appear only as fixed points of a future derived effective dynamics:

$$
w_{\mathrm{eff}} = W\bigl(\phi,\, \nabla\phi,\, F^2,\, \hat{\theta},\, \hat{\sigma}^2,\, \ldots\bigr).
$$

The function \(W\) is currently unknown.

---

## 11 Relation to Holography

Holographic results show that the entropy of a quantum subsystem may be related to the area of a geometric surface.

This supports the general idea of a transition

$$
\text{quantum correlations} \longrightarrow \text{geometry},
$$

but it is not a necessary part of the minimal core of the present model.

In particular, AdS/CFT does not prove:

- the existence of a compact fifth dimension;
- the applicability of AdS holography to the observed FLRW Universe;
- the origin of the U(1) connection in this model;
- the existence of cosmological relaxation.

Holography is therefore treated as additional motivation rather than as a foundational equation.

---

## 12 Central Consistency Condition

Define two operations:

$$
T_5 : \text{local thermodynamics} \longrightarrow \text{five-dimensional field equations},
$$

$$
R_{\mathrm{KK}} : \text{five-dimensional geometry} \longrightarrow \text{four-dimensional fields}.
$$

The key requirement of the hypothesis is **commutativity**:

$$
R_{\mathrm{KK}} \circ T_5 \;\equiv\; T^{\mathrm{red}}_4 \circ R_{\mathrm{KK}}.
$$

The meaning of this condition is:

> The thermodynamic derivation of the five-dimensional geometry followed by reduction must yield the same four-dimensional dynamics as the reduction of local thermodynamic quantities followed by the derivation of the four-dimensional equations.

If this condition fails, the combination of Kaluza–Klein and Jacobson is only a formal analogy.

---

## 13 Falsification Criteria

The hypothesis must be rejected or substantially modified if at least one of the following conditions is found to hold.

1. A causal network with local U(1) holonomies has no Lorentz-invariant continuum limit.
2. The discrete holonomy functional does not reproduce the Maxwell term \(-\frac{1}{4} F_{\mu\nu} F^{\mu\nu}\).
3. The five-dimensional thermodynamic derivation does not reproduce all components of the five-dimensional Einstein equation.
4. KK reduction of the thermodynamic equation does not yield a consistent Einstein–Maxwell–radion system.
5. The radion cannot be stabilized without contradicting laboratory and astrophysical constraints.
6. The theory predicts an observable violation of Lorentz invariance, variation of electric charge, or an unacceptable variation of the effective Newton constant.
7. The cosmological consequences are inconsistent with CMB, BAO, supernovae, lensing, and structure growth.

---

## 14 Minimal Computational Program

The first stage does not require a complete theory of quantum gravity.

1. Construct a finite causal network with variables \(U_{xy} \in \mathrm{U}(1)\).
2. Define a Wilson-like functional on causal diamonds:
   $$
   S_{\mathrm{U}(1)} = \frac{1}{g^2} \sum_D w_D \bigl[1 - \mathrm{Re}\, W_D\bigr].
   $$
3. Verify that for small phases,
   $$
   1 - \mathrm{Re}\, W_D \simeq \tfrac{1}{2} \Phi_D^2,
   $$
   and that the continuum limit reproduces \(F^2\).
4. Carry out the five-dimensional version of Jacobson’s derivation using the five-dimensional metric of Section 4.
5. Explicitly decompose the five-dimensional equation into the \((\mu, \nu)\), \((\mu, 5)\), and \((5, 5)\) components.
6. Verify the commutativity condition of Section 12.
7. Investigate solutions with constant and variable radion.
8. Only then calculate the effective cosmological equation of state \(w_{\mathrm{eff}}(z)\).

---

## 15 Final Formulation of the Hypothesis

The fundamental kinematics is specified by a locally finite causal structure without an external global time.

Proper time, volume, and Lorentzian geometry emerge in the continuum limit from causal order, chain lengths, and event counts.

The electromagnetic sector is specified by U(1) holonomies on causal links. The electromagnetic field is the curvature of this connection, and the photon is its propagating excitation.

The continuum U(1) layer may be geometrized as a compact Kaluza–Klein fifth dimension.

Jacobson’s local thermodynamic relation is applied to the complete five-dimensional geometry. It generates the five-dimensional Einstein equation, which after reduction separates into the four-dimensional Einstein, Maxwell, and radion equations.

The ordinary Einstein–Maxwell system corresponds to a local equilibrium regime with a stabilized compact layer.

A nonequilibrium change in the layer size is a possible source of additional four-dimensional dynamics, but its relation to dark energy, black holes, or galactic dynamics has not yet been established.

Thus, the current status of the construction may be written as

```
standard discrete gauge kinematics + standard KK geometry
  + the hypothesis of 5D Jacobson thermodynamics.
```

This is a mathematically defined research program, but not yet a closed physical theory.

---

## References

1. T. Kaluza, Zum Unitätsproblem der Physik, *Sitzungsberichte der Preussischen Akademie der Wissenschaften*, 966–972 (1921).
2. O. Klein, Quantentheorie und fünfdimensionale Relativitätstheorie, *Zeitschrift für Physik* **37**, 895–906 (1926).
3. A. Raychaudhuri, Relativistic Cosmology. I, *Physical Review* **98**, 1123–1126 (1955).
4. L. Bombelli, J. Lee, D. Meyer, R. D. Sorkin, Space-Time as a Causal Set, *Physical Review Letters* **59**, 521–524 (1987).
5. W. G. Unruh, Notes on Black-Hole Evaporation, *Physical Review D* **14**, 870–892 (1976).
6. T. Jacobson, Thermodynamics of Spacetime: The Einstein Equation of State, *Physical Review Letters* **75**, 1260–1263 (1995).
7. C. Eling, R. Guedens, T. Jacobson, Non-Equilibrium Thermodynamics of Spacetime, *Physical Review Letters* **96**, 121301 (2006).
8. T. Jacobson, Entanglement Equilibrium and the Einstein Equation, *Physical Review Letters* **116**, 201101 (2016).
9. K. G. Wilson, Confinement of Quarks, *Physical Review D* **10**, 2445–2459 (1974).
10. J. M. Maldacena, The Large N Limit of Superconformal Field Theories and Supergravity, *Advances in Theoretical and Mathematical Physics* **2**, 231–252 (1998).
