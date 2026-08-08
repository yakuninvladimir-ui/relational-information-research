# KK–Jacobson Commutativity Note

KK–Jacobson Commutativity Note
       Discrete Causal Structure, U (1) Holonomies, and the
      Thermodynamic Origin of the Einstein–Maxwell System

                                    V. Yakunin

                                  July 15, 2026

                                      Abstract

        A minimal working hypothesis is proposed that combines three math-
     ematically established constructions: discrete causal order, a U (1) gauge
     connection, and the thermodynamic derivation of the Einstein equations.
        At the fundamental level, the gravitational sector is associated with the
     structure of a causal network, whereas the electromagnetic sector is de-
     scribed by U (1) phase variables assigned to its links. In the continuum
     limit, this system is interpreted as a four-dimensional Lorentzian geometry
     equipped with a principal U (1) bundle. Its geometric lift to five dimensions
     has Kaluza–Klein form.
        The central hypothesis is that Jacobson’s local thermodynamic princi-
     ple should be applied to the complete five-dimensional geometry. After
     reduction, the five-dimensional equation of state should generate the four-
     dimensional Einstein equations, Maxwell equations, and the radion equa-
     tion.
        The construction contains no derivation of dark energy, dark matter, or
     the four conjectured equation-of-state regimes. These interpretations must
     be obtained from the dynamics rather than introduced as initial postulates.

1 Status of the Hypothesis

Three levels of claims are distinguished in this work.
Established mathematical elements:

  1. causal partial order and locally finite causal sets;

  2. discrete U (1) connections and holonomies;

  3. geometry of principal bundles;

  4. Kaluza–Klein reduction;

  5. the Raychaudhuri equation;

                                          1

  6. Unruh temperature and horizon entropy;

  7. the thermodynamic derivation of the Einstein equation in Jacobson’s con-
     struction.

Central hypothesis:

             causal network with a U (1) connection
               −→ four-dimensional geometry with a U (1) bundle
               −→ five-dimensional Kaluza–Klein geometry                  (1)
               −→ local horizon thermodynamics
               −→ Einstein–Maxwell–radion system.

Not yet derived:

  • the origin of the compactness of the fifth dimension;

  • stabilization of its radius;

  • cosmological relaxation;

  • effective dark energy;

  • galactic dynamics without dark matter;

  • the phase sequence 1, 1/3, −1/3, −1.

2 Discrete Kinematics

2.1 Causal structure

The fundamental structure is a locally finite partially ordered set,

                                     C = (X, ≺),                          (2)

where x ≺ y means that event x causally precedes event y.
No external global time is assumed. Proper time between causally related
events may be related approximately to the length of a maximal chain:

                                τC (x, y) = τ∗ max |γ|.                   (3)
                                              γ:x⇝y

The number of elements in the causal interval

                            I(x, y) = {z ∈ X | x ≺ z ≺ y}                 (4)

plays the role of a discrete volume measure:

                                          2

                                 V (x, y) ∼ v∗ |I(x, y)|.                   (5)

In the continuum limit, causal order should reproduce light cones, while ele-
ment counting should reproduce Lorentzian volume.

2.2 U (1) connection on the causal network

Associate to each oriented causal link x ≺ y a group element

                            Uxy ∈ U (1),          Uxy = eiqaxy .            (6)

It describes parallel transport of the phase of a charged state between two
events.
If the field at a vertex transforms as

                             ψx −→ gx ψx ,          gx ∈ U (1),             (7)

then the discrete connection transforms according to

                                   Uxy −→ gx Uxy gy−1 .                     (8)

Parallel transport along a causal chain

                            γ : x = x0 ≺ x1 ≺ · · · ≺ xn = y                (9)

is defined by the product

                                            Y
                                            n−1
                                  U (γ) =         Uxj xj+1 .              (10)
                                            j=0

Because causal order contains no directed closed cycles, discrete curvature is
defined by comparing two distinct chains with the same endpoints:

                              γ1 : x ⇝ y,         γ2 : x ⇝ y.             (11)

The corresponding relative holonomy is

                              W (γ1 , γ2 ) = U (γ1 )U (γ2 )−1 .           (12)

If

                                     W (γ1 , γ2 ) ̸= 1,                   (13)

then the result of phase transport depends on the selected causal path. This is
the discrete analogue of nonzero curvature,

                                             3

                                   Fµν = ∂µ Aν − ∂ν Aµ .                   (14)

Thus, in the initial picture,

       gravitational sector = structure and dynamics of causal order,
                                                                           (15)
    electromagnetic sector = U (1) connection on causal links.

The photon should therefore be interpreted not as the phase of an individual
particle, but as a propagating excitation of the connection Uxy itself.

3 Continuum Limit

Assume the existence of a coarse-graining regime in which

                                (C, Uxy ) −→ (M4 , gµν , Aµ ).             (16)

Causal order and the discrete volume measure generate a four-dimensional
Lorentzian geometry gµν , while discrete holonomies become a U (1) connection
Aµ :
                                          Z y        
                                Uxy ≃ exp iq        µ
                                               Aµ dx .                     (17)
                                                  x

At this level, gravitation and electromagnetism are geometric objects of differ-
ent types:

                                gµν = metric of the base,                  (18)

                Aµ = connection on the U (1) layer over the base.          (19)

They can be unified through a five-dimensional geometric lift, but need not be
identified.

4 Kaluza–Klein Geometric Lift

Consider the principal bundle

                                           c5 −→ M4 .
                                  U (1) ,→ M                               (20)

The five-dimensional metric is written as

                                              4

                s 2 = e−2αϕ(x) gµν (x)dxµ dxν + e4αϕ(x) [dy + κAµ (x)dxµ ]2 .
               db                                                               (21)

Here:

  • gµν is the four-dimensional metric;

  • Aµ is the electromagnetic connection;

  • y is the coordinate of the compact layer;

  • φ is the radion determining the physical size of the layer;

  • α and κ depend on normalization.

The combination

                                   Θ5 = dy + κAµ dxµ                            (22)

is invariant under

                        y −→ y − κλ(x),          Aµ −→ Aµ + ∂µ λ.               (23)

Thus, four-dimensional gauge symmetry is interpreted as the freedom to choose
a coordinate on the compact layer.
The fifth dimension need not be understood as a fundamental additional space;
it may instead be viewed as a geometric representation of the internal U (1)
phase.

5 Five-Dimensional Horizon Thermodynamics

5.1 Local five-dimensional horizon

At each point of the five-dimensional geometry, consider a local Rindler horizon
with null tangent vector

                                        b
                                        kAb
                                          kA = 0.                               (24)

The area of its spatial cross-section in five dimensions is a three-dimensional
quantity A3 .
Take the horizon entropy to be

                                           kB c 3
                                      S5 =        A3 .                          (25)
                                           4h̄G5

The temperature of the locally accelerated observer is

                                             5

                                           h̄b
                                             κ
                                   TU =         .                          (26)
                                          2πckB

Postulate the local equilibrium Clausius relation

                                   δQ5 = TU δS5                            (27)

for all local five-dimensional Rindler horizons.
Thermodynamics is not treated here as an independent microscopic substance.
It is a macroscopic law of coarse-grained causal geometry.

5.2 Five-dimensional Raychaudhuri equation

For a hypersurface-orthogonal five-dimensional null congruence,

                         dθb    1
                             = − θb2 − σ
                                       bAB σ     bAB b
                                           bAB − R   kAb
                                                       kB .                (28)
                         dλ     3
The coefficient 1/3 appears because the transverse cross-section of a five-
dimensional null congruence has dimension three.
It is not an equation of state

                                        1
                                     w=− ,                                 (29)
                                        3
and is not by itself related to coasting cosmology.
Equation (28) converts five-dimensional curvature into a change of local horizon
area.

5.3 Five-dimensional equation of state

Applying Jacobson’s logic to (27) and (28) should lead to the five-dimensional
Einstein equation:

                             G     b gAB = 8πG5 TbAB .
                             bAB + Λb                                      (30)
                                            c4

The cosmological constant arises as an integration constant. The thermody-
namic derivation alone does not determine its magnitude.

6 Reduction of the Thermodynamic Equation

Equation (30) separates into the components

                                          6

                        (A, B) = (µ, ν),              (µ, 5),    (5, 5).   (31)

After reduction, these components should yield, respectively,

                                     8πG4 matter    EM    (ϕ)
                                                              
                    Gµν + Λ4 gµν =      4
                                          Tµν    + Tµν + Tµν    ,          (32)
                                      c

                                            
                                ∇µ e−aϕ F µν = J ν ,                       (33)

and

                                     ∂Veff
                            □φ =           + C e−aϕ Fµν F µν .             (34)
                                      ∂φ

The coefficients a and C depend on the normalization chosen for the five-
dimensional metric and the field Aµ .
The electromagnetic stress-energy tensor has the standard structure
                                                                    
                                                       1
                        EM
                       Tµν = e−aϕ        Fµα Fν   α
                                                      − gµν Fαβ F αβ
                                                                       .   (35)
                                                       4

Consequently, the central intersection of Kaluza–Klein and Jacobson is

           5D local thermodynamics −→ 5D Einstein equation
                                      
                                      
                                      4D Einstein equation,               (36)
                                   −→ Maxwell equation,
                                      
                                      
                                        radion equation.

Thus, the Einstein equation is not derived from Maxwell’s equations. Both
equations arise as different projections of one five-dimensional thermodynamic
equation of state.

7 Entropy and the Size of the Compact Layer

Let the physical length of the compact layer be

                                         L5 = 2πb.                         (37)

In a locally factorized regime, the five-dimensional horizon area is

                                       A3 = L5 A2 ,                        (38)

where A2 is the area of the four-dimensional horizon cross-section.

                                             7

Then

                                              kB c3
                                       S5 =         L5 A2 .                (39)
                                              4h̄G5

If L5 is constant, define

                                                    G5
                                           G4 =        ,                   (40)
                                                    L5

and obtain the ordinary four-dimensional entropy:

                                               kB c 3
                                        S5 =          A2 .                 (41)
                                               4h̄G4

For a variable layer size,

                                       kB c3
                             δS5 =           (L5 δA2 + A2 δL5 ) .          (42)
                                       4h̄G5

The first term describes the change in four-dimensional horizon area.
The second term describes the change in the geometry of the compact layer. It
is not a newly introduced arbitrary entropy component; it is the variation of an
existing Kaluza–Klein degree of freedom.

8 Equilibrium Einstein–Maxwell Regime

The working equilibrium regime is defined by

                            φ ≃ φ0 ,       ∇µ φ ≃ 0,          δi S ≃ 0.    (43)

With consistent radion stabilization, the system approaches

                                            8πG4 matter     EM
                                                               
                        Gµν + Λ4 gµν =           T µν   + T µν   ,         (44)
                                             c4

                                         ∇µ F µν = J ν .                   (45)

This regime is the candidate for the ordinary observed coupling of general rel-
ativity and electromagnetism.
However, the simple condition

                                          φ = const                        (46)

is not always a consistent solution of the full KK system. Equation (34) imposes
the additional constraint

                                                8

                               ∂Veff
                          0=          + C e−aϕ0 Fµν F µν .                 (47)
                                ∂φ ϕ0

For an arbitrary varying electromagnetic field, this condition normally requires
a stabilization mechanism or a special sector of solutions.
The radion cannot be removed merely by declaration.

9 Nonequilibrium Regime

Outside local equilibrium, one must use

                                  δQ5
                          δS5 =       + δ i S5 ,     δi S5 ≥ 0.            (48)
                                   TU

Nonequilibrium behavior may be associated with

                                       ∇µ φ ̸= 0,                          (49)

                                        δL5 ̸= 0,                          (50)

                                     bAB σ
                                     σ   bAB ̸= 0,                         (51)

or other nonequilibrium deformations of the horizon.
Positive entropy production does not automatically imply

                                          p<0                              (52)

or

                                        w ≃ −1.                            (53)

For a cosmological interpretation, one must independently derive the effective
four-dimensional tensor

                                            eff
                                           Tµν                             (54)

and verify the acceleration condition

                                   ρeff + 3peff < 0.                       (55)

Dark energy is therefore not yet a consequence of this hypothesis.

                                            9

10 Four Conjectured Regimes

The sequence
                                                       
                                            1 1
                                w∈        1, , − , −1                      (56)
                                            3 3

was considered previously.
In standard cosmology, these values correspond to:

             w    Standard interpretation
             1    stiff medium
            1/3   isotropic massless radiation
           −1/3   coasting regime or a network of stretched strings
            −1    vacuum energy

In the present version of the hypothesis, these values are not introduced as
spatial phases.
In particular:

  • a black hole is defined by trapped surfaces, not by a universal value w = 1;
  • ordinary galactic matter has approximately w = 0, not w = 1/3;
  • w = −1/3 does not follow automatically from the Raychaudhuri equation;
  • w = −1 does not follow from entropy production.

The four values can appear only as fixed points of a future derived effective
dynamics:

                                                 bσ
                          weff = W (φ, ∇φ, F 2 , θ, b 2 , . . .).          (57)

The function W is currently unknown.

11 Relation to Holography

Holographic results show that the entropy of a quantum subsystem may be
related to the area of a geometric surface.
This supports the general idea of a transition

                     quantum correlations −→ geometry,                     (58)

but it is not a necessary part of the minimal core of the present model.
In particular, AdS/CFT does not prove:

                                            10

  • the existence of a compact fifth dimension;

  • the applicability of AdS holography to the observed FLRW Universe;

  • the origin of the U (1) connection in this model;

  • the existence of cosmological relaxation.

Holography is therefore treated as additional motivation rather than as a foun-
dational equation.

12 Central Consistency Condition

Define two operations:

        T5 : local thermodynamics −→ five-dimensional field equations,     (59)

         RKK : five-dimensional geometry −→ four-dimensional fields.       (60)

The key requirement of the hypothesis is commutativity:

                             RKK ◦ T5 ≡ Tred
                                         4   ◦ RKK .                       (61)

The meaning of (61) is:

     The thermodynamic derivation of the five-dimensional geometry fol-
     lowed by reduction must yield the same four-dimensional dynamics
     as the reduction of local thermodynamic quantities followed by the
     derivation of the four-dimensional equations.

If this condition fails, the combination of Kaluza–Klein and Jacobson is only a
formal analogy.

13 Falsification Criteria

The hypothesis must be rejected or substantially modified if at least one of the
following conditions is found to hold.

  1. A causal network with local U (1) holonomies has no Lorentz-invariant con-
     tinuum limit.

  2. The discrete holonomy functional does not reproduce the Maxwell term
                                      1
                                     − Fµν F µν .
                                      4

                                       11

  3. The five-dimensional thermodynamic derivation does not reproduce all
     components of the five-dimensional Einstein equation.

  4. KK reduction of the thermodynamic equation does not yield a consistent
     Einstein–Maxwell–radion system.

  5. The radion cannot be stabilized without contradicting laboratory and as-
     trophysical constraints.

  6. The theory predicts an observable violation of Lorentz invariance, varia-
     tion of electric charge, or an unacceptable variation of the effective New-
     ton constant.

  7. The cosmological consequences are inconsistent with CMB, BAO, super-
     novae, lensing, and structure growth.

14 Minimal Computational Program

The first stage does not require a complete theory of quantum gravity.

  1. Construct a finite causal network with variables Uxy ∈ U (1).

  2. Define a Wilson-like functional on causal diamonds:
                                      1 X
                             SU (1) = 2   wD [1 − Re WD ] .                   (62)
                                     g D

  3. Verify that for small phases,
                                                1
                                     1 − Re WD ≃ Φ2D ,                        (63)
                                                2
     and that the continuum limit reproduces F 2 .

  4. Carry out the five-dimensional version of Jacobson’s derivation using the
     metric (21).

  5. Explicitly decompose the five-dimensional equation into the (µ, ν), (µ, 5),
     and (5, 5) components.

  6. Verify the commutativity condition (61).

  7. Investigate solutions with constant and variable radion.

  8. Only then calculate the effective cosmological equation of state weff (z).

                                         12

15 Final Formulation of the Hypothesis

   The fundamental kinematics is specified by a locally finite causal struc-
   ture without an external global time.
   Proper time, volume, and Lorentzian geometry emerge in the continuum
   limit from causal order, chain lengths, and event counts.
   The electromagnetic sector is specified by U (1) holonomies on causal
   links. The electromagnetic field is the curvature of this connection, and
   the photon is its propagating excitation.
   The continuum U (1) layer may be geometrized as a compact Kaluza–Klein
   fifth dimension.
   Jacobson’s local thermodynamic relation is applied to the complete five-
   dimensional geometry. It generates the five-dimensional Einstein equa-
   tion, which after reduction separates into the four-dimensional Einstein,
   Maxwell, and radion equations.
   The ordinary Einstein–Maxwell system corresponds to a local equilib-
   rium regime with a stabilized compact layer.
   A nonequilibrium change in the layer size is a possible source of addi-
   tional four-dimensional dynamics, but its relation to dark energy, black
   holes, or galactic dynamics has not yet been established.
                                                                            (64)
Thus, the current status of the construction may be written as

      standard discrete gauge kinematics + standard KK geometry
                                                                           (65)
          + the hypothesis of 5D Jacobson thermodynamics.

This is a mathematically defined research program, but not yet a closed physical
theory.

References
 [1] T. Kaluza, Zum Unitätsproblem der Physik, Sitzungsberichte der Preussis-
     chen Akademie der Wissenschaften, 966–972 (1921).

 [2] O. Klein, Quantentheorie und fünfdimensionale Relativitätstheorie,
     Zeitschrift für Physik 37, 895–906 (1926).

 [3] A. Raychaudhuri, Relativistic Cosmology. I, Physical Review 98, 1123–
     1126 (1955).

 [4] L. Bombelli, J. Lee, D. Meyer, R. D. Sorkin, Space-Time as a Causal Set,
     Physical Review Letters 59, 521–524 (1987).

 [5] W. G. Unruh, Notes on Black-Hole Evaporation, Physical Review D 14,
     870–892 (1976).

 [6] T. Jacobson, Thermodynamics of Spacetime: The Einstein Equation of
     State, Physical Review Letters 75, 1260–1263 (1995).

                                      13

 [7] C. Eling, R. Guedens, T. Jacobson, Non-Equilibrium Thermodynamics of
     Spacetime, Physical Review Letters 96, 121301 (2006).

 [8] T. Jacobson, Entanglement Equilibrium and the Einstein Equation, Physi-
     cal Review Letters 116, 201101 (2016).

 [9] K. G. Wilson, Confinement of Quarks, Physical Review D 10, 2445–2459
     (1974).

[10] J. M. Maldacena, The Large N Limit of Superconformal Field Theories and
     Supergravity, Advances in Theoretical and Mathematical Physics 2, 231–
     252 (1998).

                                    14
