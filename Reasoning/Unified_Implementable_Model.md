# Unified Implementable Model, Version 2.0: Verifier-Centered Latent World Models with Evidence-Grounded Three-Way Semantics

Unified Implementable Model, Version 2.0:
                Verifier-Centered Latent World Models with
                 Evidence-Grounded Three-Way Semantics
                                           Vladimir Yakunin

                                               July 8, 2026

                                                 Abstract
          We present a revised unified architecture for embodied agents operating in partially ob-
      served, safety-relevant environments such as mobile robotics and autonomous aerial systems.
      The architecture combines an object-centric latent world model, a geometric predicate layer,
      bounded semantic hypothesis generation, measurable verification contracts, exact post-action
      verification, event-sourced memory, and recursive recovery across failed attempts. Its central
      design principle is an explicit authority boundary: imagined trajectories may rank actions and
      suppress bad routes, but only an accepted action followed by a trusted observation may create
      factual transition evidence. A semantic proposer, including an optional language model, is
      therefore not an action authority, a metric authority, or a factual memory writer.
          The mathematical treatment corrects two common errors in box-based semantics. First,
      the differentiable containment penalty is oriented so that it vanishes exactly when the an-
      tecedent box is contained in the consequent box. Second, box incompatibility is represented
      by separation in at least one coordinate, rather than by the substantially stronger and generally
      incorrect requirement of zero overlap in every coordinate. We further distinguish structural
      ontology constraints from grounded state evaluation: predicate boxes are persistent semantic
      regions, while a predicted or observed entity embedding is tested for membership in those
      regions.
          The resulting model uses three specification relations—required entailment, required in-
      compatibility, and irrelevance—together with a separate epistemic outcome, unresolved. Plan-
      ning is performed by surface-conditioned, risk-sensitive model predictive control over mixed
      discrete and continuous actions. Candidate rollouts remain predictive-only; before execution,
      a deterministic binder constructs a measurable contract and a verifier checks legality, surface
      compatibility, semantic constraints, and uncertainty. After execution, the official before–
      action–after tuple is ingested exactly once, producing a four-way verdict: required, forbidden,
      irrelevant, or unresolved. Canonical claims, assumption lineage, and memory events prevent
      speculative explanations from being promoted into confirmed mechanics. The same core ar-
      chitecture supports different domains by replacing the perception adapter, action surface,
      constraint modules, research modules, and recovery policy while preserving the authority,
      verification, and memory invariants.

Contents
1 Scope and Architectural Position                                                                        3
  1.1 Non-claims . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          4

2 Formal Environment and Evidence Model                                                                   4
  2.1 Partially observed controlled process . . . . . . . . . . . . . . . . . . . . . . . . . .           4
  2.2 Trusted observation is not metaphysical truth . . . . . . . . . . . . . . . . . . . . .             4
  2.3 Authority hierarchy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         5

3 Three-Way Semantic Specification and Four-Way Judgment                                                  5

                                                     1

4 Corrected Predicate-Box Semantics                                                                     5
  4.1 Entity and relation grounding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         5
  4.2 Signed membership and epistemic band . . . . . . . . . . . . . . . . . . . . . . . .              6
  4.3 Exact entailment and corrected containment loss . . . . . . . . . . . . . . . . . . .             6
  4.4 Exact incompatibility and corrected separation loss . . . . . . . . . . . . . . . . . .           7
  4.5 Structural relations versus state constraints . . . . . . . . . . . . . . . . . . . . . .         7
  4.6 Ontology loss . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       7
  4.7 Expressivity boundary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         8

5 Object-Centric Latent World Model                                                                     8
  5.1 Belief state . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      8
  5.2 Probabilistic dynamics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        8
  5.3 Predictive objective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      8
  5.4 Anti-collapse regularization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        9
  5.5 Grounding and calibration losses . . . . . . . . . . . . . . . . . . . . . . . . . . . .          9

6 Canonical Evidence Ledger                                                                             9

7 Proposer, Binder, Planner, and Verifier                                                         9
  7.1 Semantic proposer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
  7.2 Deterministic binder . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
  7.3 Planner and compiler . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
  7.4 Pre-action and post-action verifier . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

8 Measurable Verification Contracts                                                                    10

9 Surface-Conditioned Action Realization                                                               11

10 Risk-Sensitive Predictive Planning                                                                  11
   10.1 Predictive rollouts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    11
   10.2 Chance and hard constraints . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      12
   10.3 Mixed discrete–continuous CEM . . . . . . . . . . . . . . . . . . . . . . . . . . . .          12

11 Two-Phase Execution and the Factual Commit Boundary                                                 13
   11.1 Pre-action phase . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     13
   11.2 Pending transition invariant . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     13
   11.3 Post-action phase . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    13

12 Recursive Hypothesis Revision                                                                       13

13 Canonical Event-Sourced Memory                                                                 14
   13.1 Deterministic consolidation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14

14 Attempts, Recovery, and Termination                                                                 14

15 Learning Objective                                                                          15
   15.1 Observed versus imagined training data . . . . . . . . . . . . . . . . . . . . . . . . 15

16 Knowledge Distillation with Alignment and Authority Control                                         16
   16.1 Representation alignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       16
   16.2 Dynamic distribution distillation . . . . . . . . . . . . . . . . . . . . . . . . . . . .      16
   16.3 Semantic distillation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    16
   16.4 Logit distillation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   16
   16.5 Teacher authority boundary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       16

                                                   2

17 Correctness Results and Precise Guarantees                                                          17

18 Worked Drone Example                                                                                18
   18.1 Predicates and relations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     18
   18.2 Current action surface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     18
   18.3 Bound contract . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     18
   18.4 Recovery . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   19

19 Implementation Invariants and Test Obligations                                                      19

20 Research Modules and Domain Substitution                                                            20

21 Development Roadmap                                                                                 20
   21.1 Stage 1: Static verified baseline . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    20
   21.2 Stage 2: Calibrated uncertainty and active research . . . . . . . . . . . . . . . . . .        20
   21.3 Stage 3: Canonical evidence and recursive revision . . . . . . . . . . . . . . . . . .         20
   21.4 Stage 4: Event-sourced memory and attempt recursion . . . . . . . . . . . . . . . .            20
   21.5 Stage 5: Controlled predicate and relation induction . . . . . . . . . . . . . . . . .         21
   21.6 Stage 6: Richer semantic geometries . . . . . . . . . . . . . . . . . . . . . . . . . .        21
   21.7 Stage 7: Hierarchical skills and long-horizon planning . . . . . . . . . . . . . . . . .       21

22 Conclusion                                                                                          21

1     Scope and Architectural Position
The Unified Implementable Model (UIM) is intended for agents that must jointly:

    (i) infer a compact state from high-dimensional and noisy observations;

 (ii) predict the consequences of candidate actions;

(iii) reason over semantic objects, relations, and constraints;

 (iv) select actions under uncertainty and changing control modes;

 (v) distinguish predicted consequences from observed consequences;

 (vi) revise hypotheses without erasing still-valid assumptions;

(vii) retain only evidence-grounded knowledge across levels, attempts, or mission phases.

    The architecture is domain-general, but not domain-free. A robotics deployment and an ab-
stract reasoning deployment use different perception front ends, action spaces, verification metrics,
and research probes. They nevertheless share one control architecture:

           observe → canonicalize evidence → propose → bind → plan
                                                                                                       (1)
                  → verify before action → act → verify after observation → consolidate

    The model is verifier-centered. A neural world model predicts; a semantic proposer generates
testable explanations; a binder makes them measurable; a planner realizes them as routes; and an
exact verifier determines what the trusted transition actually supports.

                                                   3

1.1     Non-claims
The following claims are explicitly excluded.
    1) Exact satisfaction of a learned latent constraint is not, by itself, a proof of physical-world
       safety.
    2) A language model explanation is not factual evidence.
    3) An imagined rollout is not an observed transition.
    4) A failed route does not imply that every assumption of its parent hypothesis is false.
    5) A successful route does not automatically confirm the proposer’s explanation of why it
       succeeded.
    6) A geometric box ontology is not universally expressive; disjunctions, rotated regions, multi-
       modal concepts, and temporal properties may require richer representations.

2     Formal Environment and Evidence Model
2.1     Partially observed controlled process
Let the physical environment be a controlled stochastic process
                                       M = (X , O, A, T , Z, C),                                     (2)
where xt ∈ X is the inaccessible physical state, ot ∈ O is an observation, at ∈ A is an action,
T (xt+1 | xt , at ) is the transition law, Z(ot | xt ) is the observation law, and C is the collection of
task and safety constraints.
    At time t, not every action in A is necessarily available. The current action surface is
                                      Σt = (At , κt ),       At ⊆ A,                                 (3)
where κt contains mode, capability, payload, actuator, communication, and authorization meta-
data. For a drone, Σt may distinguish manual-rate control, position hold, landing, return-to-home,
degraded navigation, or payload operation. For a symbolic environment, it may distinguish dif-
ferent interaction modes or newly available action symbols.

2.2     Trusted observation is not metaphysical truth
The agent cannot directly record xt . It records a trusted, timestamped observation packet
                                            ōt = (ot , Σt , mt ),                                   (4)
where mt contains source, timestamp, calibration, synchronization, and estimator metadata. The
pair
                                       ϵt = (ōt , at , ōt+1 )                             (5)
is the highest-authority transition evidence available to the agent, provided that the environment
or control stack accepted at and the returned observation passed ingestion checks. It is called an
authoritative observed transition; it is not claimed to be the hidden physical state itself.
Definition 2.1 (Evidence scope). Each result has one of the scopes
             NOT_AVAILABLE,        PREDICTIVE_ONLY,                  OBSERVED_TRANSITION,
                                                                                                     (6)
                                         REPLAY_VERIFIED.
A predictive result may affect ranking and risk estimation, but it may not create a factual transition,
a confirmed mechanic, or positive success memory.

                                                      4

2.3     Authority hierarchy
A generic authority order is

                accepted action and trusted post-action observation
                   > current action-surface legality and capability
                   > post-action verifier result and bound metric result
                   > canonical observed memory and deterministic consolidation
                                                                                                   (7)
                   > committed causal models and current deterministic scene facts
                   > bound semantic hypothesis and route realization
                   > predictive rollout
                   > unbound semantic proposal or explanation.

No lower layer may promote its output into a higher evidentiary class without the corresponding
higher-authority observation or verification event.

3      Three-Way Semantic Specification and Four-Way Judgment
The UIM uses a three-way relation vocabulary inspired by the distinction between consequence,
incompatibility, and omission of a relation. Let P be a predicate vocabulary. For a pair (p, q) ∈ P 2 ,
the structural specification label is

                                    R(p, q) ∈ {REQ, FORB, IRR}.                                    (8)

The labels mean:

    (1) R(p, q) = REQ: the ontology requires p ⇒ q;

    (2) R(p, q) = FORB: the ontology requires p ∧ q to be impossible for the same grounded argu-
        ment;

    (3) R(p, q) = IRR: no entailment or incompatibility constraint is asserted between p and q.

   Irrelevance is not falsehood. It means that the theory intentionally imposes no relation of the
specified kind. Data may still reveal correlation, partial overlap, causal dependence, or a future
need to refine the ontology.
   At runtime, the verifier emits a separate epistemic-semantic judgment

                   J ∈ {REQUIRED, FORBIDDEN, IRRELEVANT, UNRESOLVED}.                              (9)

Here UNRESOLVED is not a fourth structural relation. It records insufficient, predictive-only,
stale, unstable, or contradictory evidence. This separation prevents unknown from being treated
as false and prevents a legal no-progress action from being treated as a contradiction.

4      Corrected Predicate-Box Semantics
4.1     Entity and relation grounding
A predicate box is a region in a semantic feature space, not a state-dependent box generated anew
for every rollout. Let et,i be an object or entity representation extracted from the current scene
graph Gt . A grounding map produces

                                      ξt,i = ψη (et,i , Gt ) ∈ Rm .                               (10)

                                                   5

For a binary relation r(i, j), a relation grounding map may use
                                     (2)
                                    ξt,ij = ψη(2) (et,i , et,j , Gt ) ∈ Rm2 .               (11)

Unary and relational predicates may use separate semantic spaces.
   Each unary predicate p ∈ P is represented by a closed axis-aligned box

                              Bp = [ℓp , up ] = {ξ ∈ Rm : ℓp ≤ ξ ≤ up },                    (12)

with componentwise inequalities. A stable parameterization is

                  ℓp = cp − rp ,         up = cp + rp ,        rp = rmin + softplus(ρp ),   (13)

where rmin > 0 prevents numerical collapse and up is the upper endpoint of Bp .

4.2   Signed membership and epistemic band
For a grounded feature ξ, define the signed box margin

                              µp (ξ) = min min{ξj − ℓp,j , up,j − ξj }.                     (14)
                                           1≤j≤m

Then µp (ξ) > 0 means that ξ lies in the interior of Bp , µp (ξ) = 0 means that it lies on the
boundary, and µp (ξ) < 0 means that it lies outside.
   Given an epistemic tolerance γp > 0, the grounded truth status is
                                     
                                     TRUE,
                                                       µp (ξ) ≥ γp ,
                         truthp (ξ) = FALSE,            µp (ξ) ≤ −γp ,                    (15)
                                     
                                        UNRESOLVED, |µp (ξ)| < γp .
                                     

The unresolved band absorbs representation error, sensor uncertainty, and small numerical per-
turbations. A differentiable membership score may be defined by
                                                         
                                                   µp (ξ)
                                     m
                                     e p (ξ) = σ            ,                             (16)
                                                    τp
where σ is the logistic sigmoid and τp > 0 is a temperature.

4.3   Exact entailment and corrected containment loss
The intended structural semantics is

                                         p⇒q       ⇐⇒       Bp ⊆ Bq .                       (17)

For closed axis-aligned boxes,

                              Bp ⊆ Bq         ⇐⇒       ℓq ≤ ℓp and up ≤ uq                  (18)

componentwise. Using up for the upper endpoint of Bp , the exact condition is

                                   ℓq,j ≤ ℓp,j ,      up,j ≤ uq,j         ∀j.               (19)

   For a desired clearance ε⇒ ≥ 0, the corrected hinge loss is
                                   m
                                   X
                    Lε⊆ (p, q) =
                                                                                    
                                         [ℓq,j + ε⇒ − ℓp,j ]+ + [up,j − uq,j + ε⇒ ]+ .      (20)
                                   j=1

For ε⇒ = 0, the loss vanishes exactly when Bp ⊆ Bq . A positive margin requires Bp to lie inside
Bq with coordinatewise clearance.

                                                       6

4.4    Exact incompatibility and corrected separation loss
For closed boxes,
                                                                                        
                      Bp ∩ Bq = ∅       ⇐⇒       ∃j : up,j < ℓq,j        ∨    uq,j < ℓp,j .         (21)

Define the signed overlap depth in coordinate j by

                              δj (p, q) = min(up,j , uq,j ) − max(ℓp,j , ℓq,j ).                    (22)

The boxes intersect if and only if δj (p, q) ≥ 0 for every coordinate. They are separated by at least
ε⊥ > 0 in some coordinate if and only if

                                            min δj (p, q) ≤ −ε⊥ .                                   (23)
                                             j

Therefore a correct margin loss is
                                                                         
                                 Lε⊥ (p, q) =        ε⊥ + min δj (p, q)          .                  (24)
                                                          1≤j≤m              +

This loss is non-smooth but subdifferentiable almost everywhere. A smooth approximation may
replace min by the normalized soft minimum
                                                                
                                                      m
                                                   1 X
                             sminτ (δ) = −τ log         e−δj /τ  ,                    (25)
                                                  m
                                                               j=1

with the understanding that the exact deployment check remains equation (21).
                                                                         P
Remark 4.1 (Why a sum of coordinate overlaps is wrong). The quantity j [δj ]+ vanishes only
when every coordinate has non-positive overlap. Empty intersection, however, requires separation
in at least one coordinate. The summed-overlap objective therefore enforces a much stronger
geometry and can incorrectly push boxes apart along dimensions that need not separate them.

4.5    Structural relations versus state constraints
The relations Bp ⊆ Bq and Bp ∩ Bq = ∅ are properties of the ontology. They do not need
to be re-evaluated as if the boxes themselves changed at every predicted step. Runtime state
checking instead evaluates whether grounded entities or relations satisfy atomic predicates and
task formulas.
     For example, if Bsquare ⊆ Brectangle and an entity embedding ξt,i is robustly inside Bsquare , then
it is also inside Brectangle . A planner checks ξt,i ∈ Bp for the predicted state and separately verifies
that the ontology remains structurally valid.

4.6    Ontology loss
Let Θ⇒ be the required entailments and Θ⊥ the required incompatibilities. The structural ontol-
ogy loss is
                                                           λpq
                               X                     X
                      Lont =         λpq ε
                                      ⇒ L⊆ (p, q) +
                                                               ε
                                                            ⊥ L⊥ (p, q).                  (26)
                                 (p,q)∈Θ⇒                     (p,q)∈Θ⊥

Relations marked irrelevant contribute no structural penalty. This does not prevent a separate
statistical model from learning correlations between them.

                                                         7

4.7     Expressivity boundary
Axis-aligned boxes represent conjunction-like, convex, coordinate-factorized concepts. The follow-
ing extensions are permitted when needed:
    (i) a finite union of boxes for multimodal predicates;
 (ii) oriented boxes or ellipsoids for rotated geometry;
(iii) neural energy regions for highly non-convex concepts;
 (iv) temporal automata for predicates over trajectories;
 (v) relation-specific spaces for pairwise or higher-arity predicates.
The authority and verification architecture does not depend on the box family; only the grounding
and exact-check modules change.

5     Object-Centric Latent World Model
5.1     Belief state
The agent maintains a recurrent belief state
                                                             
                           ht = Fθ ht−1 , Eθ (ot ), at−1 , Σt ,            qθ (st | ht ),       (27)
where st is a stochastic latent state. An object-centric decoder or slot extractor yields
                               Gt = (Vt , Et ),         Vt = {et,1 , . . . , et,nt },           (28)
with object attributes, identities or descriptors, and typed relations. Object identifiers are state-
local unless a re-identification module supplies evidence for persistence.

5.2     Probabilistic dynamics
The world model predicts
                                 pϕ (st+1 , Gt+1 , Σt+1 | st , Gt , Σt , at ).                  (29)
Predicting Σt+1 is important because an action may change the available action set, control mode,
payload state, or authorization surface.
    A practical ensemble {pϕr }M
                               r=1 provides epistemic disagreement. For a scalar predicted quantity
y, one may use
                                             M              M
                                                                 !2
                                          1 X            1 X
                               Uepi (y) =         ŷr −       ŷk .                            (30)
                                          M             M
                                                  r=1                k=1
Aleatoric uncertainty is represented by each member’s conditional distribution.

5.3     Predictive objective
With a target encoder E
                      e , a stable one-step latent objective is
                       θ̄
                                                                  
                                                                2
                             Lpred = E ẑt+1 − sg E  e (ot+1 )
                                                      θ̄             ,                          (31)
                                                                               2

where ẑt+1 = Pϕ (ht , at , Σt ). The target encoder may be an exponential moving average of the
online encoder or another stable target construction. A probabilistic alternative is the negative
log-likelihood
                                   Ldyn = −E log pϕ (st+1 | st , at , Σt ).                  (32)
For long-horizon consistency, one may add multi-step losses with scheduled sampling while retain-
ing explicit uncertainty growth.

                                                        8

5.4   Anti-collapse regularization
A concrete variance–covariance regularizer for a batch Z ∈ RB×d is
                                        d                    
                                     1X
                                                 q
                             Lvar =         γ − Var(Z:,j ) + ϵ ,                                  (33)
                                     d                         +
                                       j=1
                                         1    X
                             Lcov =               Cov(Z)2ij .                                     (34)
                                     d(d − 1)
                                                   i̸=j

A constant representation incurs a strictly positive variance penalty when γ > 0. This fact
alone does not prove that every collapsed parameterization is absent as a local stationary point
under every optimizer and weighting; such a global anti-collapse theorem would require stronger
assumptions than are generally available.
    A projection-based Gaussian discrepancy such as SIGReg may replace equation (34), provided
its finite-sample statistic, normalization, and gradients are specified explicitly and tested rather
than invoked as an informal guarantee.

5.5   Grounding and calibration losses
When predicate labels or weak supervision are available, the grounding loss may be
                                                                            
                  Lground = −E(ξ,p,y) y log m
                                            e p (ξ) + (1 − y) log 1 − m
                                                                      e p (ξ) .                   (35)
Calibration of transition and predicate uncertainty is enforced by a proper scoring rule, for example
negative log-likelihood or the Brier score. The calibration set must be disjoint from the training
set used to fit the same confidence thresholds.

6     Canonical Evidence Ledger
The semantic proposer receives one canonical evidence interface rather than several independently
summarized truth copies. A claim is a tuple
                                  C = (id, k, τ, s, r, v, α, c, σ, E, S),                         (36)
where k is a semantic key, τ is claim type, s is subject scope, r is predicate or relation, v is value,
α is authority rank, c is confidence, σ is status, E is the set of evidence references, and S is the
set of superseded claims.
    Claims are deduplicated by semantic key. If two claims conflict, the higher-authority claim
supersedes the lower-authority representation while preserving lineage. Derived summaries may
exist for efficiency, but they are marked non-authoritative and refer back to canonical claim
identifiers.
    The ledger includes a canonical belief delta
                                                                                           !
              changed components, confirmed assumptions, contradicted assumptions,
    ∆Bt =                                                                                    .     (37)
              unresolved assumptions, new high-authority claims
This delta lets a revision module respond to genuinely new evidence instead of regenerating
unrelated hypotheses from scratch.

7     Proposer, Binder, Planner, and Verifier
7.1   Semantic proposer
A semantic proposer may be a language model, a program synthesizer, a graph search module, or
a hybrid. It may propose:

                                                    9

    (i) a semantic hypothesis;

 (ii) target object or relation descriptors;

(iii) a metric family and improvement direction;

 (iv) required action surfaces;

 (v) explicit assumptions and registered questions;

 (vi) parent–child revision lineage.

It may not authorize a primitive action, certify a metric baseline, write factual memory, or promote
its explanation to confirmed knowledge.

7.2     Deterministic binder
The binder resolves proposal references against the current trusted scene and constructs a mea-
surable verification contract. It owns:

    (i) target bindings and stable descriptors;

 (ii) metric selection from an allowed registry;

(iii) baseline recomputation;

 (iv) direction, tolerances, progress threshold, success threshold, and failure margin;

 (v) contract identity and hash.

Numeric values suggested by the proposer are treated as intent, not authority.

7.3     Planner and compiler
The planner converts a bound hypothesis into one or more surface-conditioned routes. The com-
piler maps each route step to executable actions, preserving the contract, required surface, target
bindings, and predicted next surface. A planner may use continuous optimization, graph search,
sampling, trajectory optimization, or a hybrid.

7.4     Pre-action and post-action verifier
The pre-action verifier checks current legality, capability, surface compatibility, contract validity,
uncertainty, and hard safety constraints. The post-action verifier evaluates the trusted transition
using the same bound metric and target semantics. The post-action result has higher authority
than predictive evaluation.

8     Measurable Verification Contracts
A contract is
                              K = (id, D, µ, b, d, auprog , τsucc , τfail , ε, h),               (38)
where D contains target descriptors and bindings, µ is a registered metric, b is the baseline,
d ∈ {−1, +1} is the favorable direction, the τ values are progress, success, and failure thresholds,
ε is tolerance, and h is a contract hash.
    The binder computes
                                           b = µ(Gt ; Dt )                                     (39)

                                                      10

from the current trusted scene. After action execution, the targets are rebound using stable
descriptors rather than transient indices, and the verifier computes
                                b− = µ(Gt ; D
                                            bt ),            b+ = µ(Gt+1 ; D
                                                                           bt+1 ).                    (40)
If |b− − b| > ε, the contract is stale and the outcome is unresolved.
     Define observed improvement
                                          ∆K = d (b+ − b− ).                                          (41)
A generic classification is
              
              
                REQUIRED,              terminal success or contract success,
              
              REQUIRED,                ∆K ≥ τprog ,
              
              
              
   J(ϵt , K) = FORBIDDEN,               ∆K ≤ −τfail or a hard constraint is violated,                 (42)
              
                 IRRELEVANT,            legal, resolved, and |∆K | < τprog ,
              
              
              
              
              
                 UNRESOLVED,            predictive-only, stale, unstable, or insufficient evidence.
              

Domain-specific contracts may replace scalar µ by a vector metric with a declared partial order,
but the order must be fixed before observing the post-action result.

9    Surface-Conditioned Action Realization
Every route step carries
                                        Rh = (ah , Σreq b exp
                                                    h , Σh+1 , Kh , χh ),                             (43)
where χh contains target bindings and semantic hypothesis lineage. The action may be emitted
only if
                                  ah ∈ At and Σt |= Σreqh .                             (44)
A mode-changing action is a first-class surface transition. The next route step is not emitted until
the next trusted observation confirms the new surface.
    If the observed surface differs from the expected surface, the route realization becomes un-
resolved or failed. This does not by itself falsify the semantic hypothesis. The architecture
distinguishes
                      mechanic error, target-binding error, metric error,
                                                                                               (45)
                                 surface-plan error, route error.
This distinction is essential in robotics, where a correct mission objective may be paired with an
invalid control mode or temporarily unavailable actuator.

10     Risk-Sensitive Predictive Planning
10.1    Predictive rollouts
For a candidate action sequence
                                                   a = at:t+H−1 ,                                     (46)
the world model generates M stochastic rollouts
                                       (r)         (r)      (r)
                       τb(r) = (st , sbt+1 , . . . , sbt+H , Σ
                                                             b
                                                               t+1:t+H ),   r = 1, . . . , M.         (47)
Every such rollout has evidence scope PREDICTIVE_ONLY.
   A risk-sensitive cost is
                     M
         b = 1
                     X                                             
         J(a)                   τ (r) ) + λcvar CVaRα Jrisk (b
                         Jtask (b                            τ (r) ) + λepi Uepi (a) − λinfo I(a),    (48)
                 M
                      r=1

where I(a) is expected information gain for a registered question. Information gain may justify a
probe, but it does not convert the probe into positive task success.

                                                           11

Algorithm 1 Verifier-centered receding-horizon control
Require: Trusted observation ōt , canonical ledger Lt , world model W , budgets B
Ensure: One emitted action or a controlled stop/recovery decision
 1: Ingest ōt and synchronize the current action surface Σt
 2: Build the current scene graph Gt and canonical belief delta
 3: Obtain bounded semantic hypotheses grounded in known claim identifiers
 4: for all eligible hypotheses Hi do
 5:     Bind targets and construct a measurable contract Ki
 6:     if Ki is invalid or vacuous then
 7:         reject Hi for the current cycle
 8:         continue
 9:     end if
10:     Compile surface-conditioned candidate routes
11:     Evaluate routes predictively under equations (48) and (49)
12:     Mark all rollout results as PREDICTIVE_ONLY
13: end for
14: Select the best route passing legality, surface, uncertainty, and hard pre-action checks
15: if no goal-directed route is authorized then
16:     Select a registered epistemic probe, if one is verifier-authorized
17: end if
18: if no authorized action exists then
19:     return controlled stop or domain recovery action
20: end if
21: Register a pending transition token for the selected action at
22: Emit at and receive ōt+1
23: Ingest (ōt , at , ōt+1 ) exactly once
24: Rebind K, recompute the metric, and emit a four-way verdict
25: Append canonical transition and verifier events; update assumptions and memory
26: Execute only the first action of the route; replan from ōt+1

10.2    Chance and hard constraints
For each safety constraint gk (s) ≤ 0, the planner may require

                                   st+h ) ≤ 0) ≥ 1 − αk ,
                            P (gk (b                               h = 1, . . . , H.           (49)

Constraints with certified runtime monitors remain hard and are checked again immediately before
action emission. A learned chance constraint is not a substitute for an independent low-level safety
controller where one is available.

10.3    Mixed discrete–continuous CEM
For hybrid actions ah = (adh , ach ), use a factorized proposal
                                         H−1
                                         Y
                              qω (a) =         Cat(adh ; πh ) N (ach ; µh , Σh ),              (50)
                                         h=0

followed by projection of continuous controls onto actuator limits. This avoids the invalid assump-
tion that all action sequences are Gaussian vectors.
    If no feasible elites exist during CEM, the planner must not insert arbitrary random actions
merely to keep the loop running. It either changes the search distribution, chooses a registered
information-gathering probe, invokes an explicitly authorized recovery policy, or stops in a con-
trolled manner.

                                                      12

11     Two-Phase Execution and the Factual Commit Boundary
11.1    Pre-action phase
Before action emission the agent may parse observations, update beliefs, invoke bounded semantic
proposal, construct contracts, perform predictive rollouts, estimate uncertainty, reject routes, and
select a candidate action. None of these operations creates an observed causal fact.

11.2    Pending transition invariant
Immediately before emitting an action, the agent registers a token

                              πt = (sequence, hash(ōt ), at , hash(Kt )).                     (51)

A second action may not be emitted while πt remains pending.

11.3    Post-action phase
After the control stack accepts at and returns ōt+1 , the system must immediately ingest equa-
tion (5). The commit operation is idempotent with respect to πt . It:

  (i) compares trusted before and after observations and action surfaces;

 (ii) rebuilds grounded scene representations;

 (iii) rebinds contract targets;

 (iv) recomputes the official before and after metric;

 (v) produces the post-action verdict;

 (vi) writes exactly one committed transition edge;

(vii) updates observed action-effect and movement models;

(viii) appends canonical memory events;

 (ix) clears the pending token.

The control loop may not terminate normally with a pending accepted transition.

12     Recursive Hypothesis Revision
A hypothesis is
                              H = (id, PH , g, ρ, C + , C − , AH , TH , SH ),                  (52)
where PH is the parent set, g is lineage generation, ρ is revision type, C + and C − are supporting
and challenged claim identifiers, AH is an assumption graph, TH is target and metric intent, and
SH is the surface and route intent.
   Assumptions have statuses

               PROPOSED,       CONFIRMED,         CONTRADICTED,             UNRESOLVED.        (53)

A route failure updates only assumptions actually contradicted by observed evidence or explicitly
rejected by a grounded child revision. Other assumptions remain confirmed or unresolved.
    Permitted revision operators include:

  (i) preserve the mechanic and change the route;

                                                    13

 (ii) replace the target binding;

(iii) replace the metric;

 (iv) change the surface plan;

 (v) refine assumptions;

 (vi) split a hypothesis into alternatives;

(vii) abandon the hypothesis family.

A child must cite an eligible parent, use a new identifier, preserve or reject known parent assump-
tions explicitly, and make the change declared by its revision type. Parents remain in memory as
superseded rather than being deleted.

13     Canonical Event-Sourced Memory
The memory system is a bounded append-only stream of canonical events. A generic event is

                            Me = (id, h, τ, scope, authority, J, Pe , Re , χ),                 (54)

where h is a deterministic hash, τ is event type, J is semantic judgment, Pe contains parent
events, Re contains source records, and χ is typed payload.
   Useful event types include:

OBSERVED_TRANSITION,             VERIFIER_OUTCOME,               BELIEF_UPDATE,    BACKREACTION,
       SEGMENT_COMPLETION,                ATTEMPT_RESET,              ATTEMPT_TERMINATED.
                                                                                         (55)
Memory layers are separated into raw evidence, belief state, transferable mechanics, proposed
explanations, and summaries. A proposed explanation remains proposed even when its associated
route succeeds, unless independent observed evidence establishes the claimed mechanism.

13.1    Deterministic consolidation
At a confirmed mission-segment or level boundary, consolidation produces

                              Mcons = (F + , F − , U, T , Esrc , σdet , σprop ),               (56)

where F + are confirmed facts, F − contradicted facts, U unresolved proposals, T transferable
mechanics, Esrc source event identifiers, σdet a deterministic summary, and σprop an optional
proposer-authored explanation. Only the first six fields may contribute confirmed transfer without
further evidence.
    Negative transfer is scope-sensitive. A failure tied to a transient object identifier, local map
patch, battery state, or route binding must not become a universal mission rule.

14     Attempts, Recovery, and Termination
An attempt begins from an initial or recovered state and ends at one of:

  (i) confirmed task or segment success;

 (ii) environment-originated failure followed by an accepted recovery transition;

(iii) wall-clock, energy, action-count, or communication budget exhaustion;

                                                     14

 (iv) non-recoverable orchestration or hardware failure.

    Environment failure and orchestration termination are different causal classes. A timeout must
not be converted into an environment reset. For a drone, recovery may mean hover, re-localize,
return-to-home, divert, or land. It is allowed only if the recovery action is currently available,
authorized, and consistent with remaining hard budgets.
    Across an accepted recovery boundary, preserve game- or mission-scoped observed knowledge:

  (i) canonical evidence and consolidations;

 (ii) observed transition and action-effect models;

(iii) failed and irrelevant route signatures;

 (iv) verifier backreaction and hypothesis lineage;

 (v) cumulative proposal and action budgets.

Clear or renew state-local execution state:

  (i) active route and transient bindings;

 (ii) pending verification and pending transition token;

(iii) local candidate blacklist and oscillation counters;

 (iv) state-specific research queues;

 (v) per-attempt proposal slots.

A recovery does not restart a higher-level mission deadline unless the mission specification explic-
itly defines a new segment.

15     Learning Objective
A mature training objective separates representation, dynamics, grounding, ontology, calibration,
and distillation:
                    Ltotal = λpred Lpred + λdyn Ldyn + λvar Lvar + λcov Lcov
                             + λobj Lobj + λground Lground + λont Lont + λcal Lcal             (57)
                             + λdist Ldist .

The weights are not assumed to be commensurate. They must be chosen by dimension-aware nor-
malization, gradient diagnostics, and held-out performance rather than by treating equation (57)
as a scale-free sum.

15.1    Observed versus imagined training data
Training batches should retain provenance. Let Dobs contain trusted observed transitions and
Dimag contain model-generated trajectories. Dynamics fitting and factual causal updates use
Dobs . Imagined data may regularize planning or representation learning only under an explicit
synthetic-data weight and may not be labeled as observed evidence.

                                                 15

16     Knowledge Distillation with Alignment and Authority Control
16.1    Representation alignment
Teacher and student latent coordinates need not be directly comparable. Let A map student
latents into the teacher space. The representation loss is
                                                                    2
                                        Ldist       S
                                         repr = E Az − z
                                                         T
                                                                    2
                                                                      ,                        (58)

with an orthogonality or condition-number regularizer when appropriate. Matching raw coordi-
nates without alignment is unjustified when dimensions, permutations, rotations, or scales differ.

16.2    Dynamic distribution distillation
For probabilistic dynamics,

                        Ldist
                         dyn = E KL (pT (st+1 | st , at ) ∥ pS (st+1 | st , at )) ,            (59)

possibly after mapping student states through A. For ensembles, mean, covariance, and tail-risk
predictions should be matched separately.

16.3    Semantic distillation
Directly matching raw box centers and raw width parameters is coordinate-dependent. A more
invariant semantic objective matches grounded membership margins and relation violations:
                                                          2
                              Ldist        S        T
                               sem = Eξ,p µp (ξ) − µp (ξ)
                                          X                             2
                                     +           LS⊆ (p, q) − LT⊆ (p, q)
                                            (p,q)∈Θ⇒                                           (60)
                                              X                                  2
                                        +              LS⊥ (p, q) − LT⊥ (p, q)        .
                                            (p,q)∈Θ⊥

If teacher and student semantic spaces differ, the grounded samples must be aligned or evaluated
through a shared semantic probe.

16.4    Logit distillation
For K classes and temperature τ ,

                                       eti /τ                        esi /τ
                              pT,τ
                               i   = PK            ,        pS,τ
                                                             i   = PK            ,             (61)
                                             tj /τ                         sj /τ
                                      j=1 e                         j=1 e

with
                                       Ldist     2
                                        logit = τ KL(p
                                                       T,τ
                                                           ∥pS,τ ).                            (62)
The exact high-temperature coefficient is stated in theorem 17.3; it is not generally 1/2 unless the
class-count normalization is absorbed elsewhere.

16.5    Teacher authority boundary
A teacher may be more accurate than a student but remains a predictive model. Distilled outputs
do not become authoritative transition evidence. Factual memory still requires trusted observed
transitions and verifier lineage.

                                                       16

17     Correctness Results and Precise Guarantees
Proposition 17.1 (Containment-loss correctness). For ε⇒ ≥ 0, the loss in equation (20) satisfies

                                                Lε⊆ (p, q) = 0                               (63)

if and only if
                                 ℓp ≥ ℓq + ε⇒ 1,          up ≤ uq − ε⇒ 1.                    (64)
In particular, for zero margin it vanishes if and only if Bp ⊆ Bq .

Proof. Every summand in equation (20) is nonnegative. The sum is zero if and only if each
positive-part argument is nonpositive. These inequalities are exactly the stated lower- and upper-
endpoint conditions.

Proposition 17.2 (Separation-loss correctness). For ε⊥ > 0, the loss in equation (24) satisfies

                              Lε⊥ (p, q) = 0    ⇐⇒        min δj (p, q) ≤ −ε⊥ .              (65)
                                                           j

Hence zero loss certifies separation by at least ε⊥ in at least one coordinate.

Proof. By definition, [x]+ = 0 if and only if x ≤ 0. Substituting x = ε⊥ + minj δj yields the
result.

Theorem 17.1 (Grounded entailment soundness). If Bp ⊆ Bq and ξ ∈ Bp , then ξ ∈ Bq .

Proof. Because ξ ∈ Bp , ℓp ≤ ξ ≤ up . Because Bp ⊆ Bq , ℓq ≤ ℓp and up ≤ uq . Therefore
ℓq ≤ ξ ≤ uq , so ξ ∈ Bq .

Theorem 17.2 (Robust entailment under bounded grounding error). Assume

                                    ℓp ≥ ℓq + ε1,         up ≤ uq − ε1                       (66)

for some ε > 0. If ξ ∈ Bp and ∥η∥∞ ≤ ε, then ξ + η ∈ Bq .

Proof. For every coordinate,
                                        ξj + ηj ≥ ℓp,j − ε ≥ ℓq,j ,                          (67)
and
                                       ξj + ηj ≤ up,j + ε ≤ uq,j .                           (68)
Thus ξ + η ∈ Bq .

Theorem 17.3 (High-temperature distillation limit). Let t, s ∈ RK satisfy i ti = i si = 0.
                                                                           P    P
Then
                                                        1
              τ 2 KL (softmax(t/τ ) ∥ softmax(s/τ )) =    ∥t − s∥22 + O(τ −1 )        (69)
                                                       2K
as τ → ∞.

Proof. For centered logits,
                                                     1   ti
                                softmax(t/τ )i =       +    + O(τ −2 ),                      (70)
                                                     K   Kτ
and similarly for s. Expanding the KL divergence to second order around the uniform distribution
gives
                                         K
                                      1 X (pi − qi )2
                           KL(p∥q) =                   + O(∥p − q∥33 ).                     (71)
                                      2       1/K
                                               i=1

Substitution yields (2Kτ 2 )−1 ∥t − s∥22 + O(τ −3 ) before multiplication by τ 2 .

                                                     17

Proposition 17.3 (Non-promotion invariant). Suppose every factual write API requires evidence
scope OBSERVED_TRANSITION or REPLAY_VERIFIED, and predictive evaluators can emit only
PREDICTIVE_ONLY. Then no purely predictive computation can create a factual transition or
confirmed positive mechanic.

Proof. The conclusion follows from the type and authority guard on every factual write path.
A predictive result does not satisfy the precondition of any factual write API. The invariant is
architectural and must be regression-tested; it is not guaranteed by model accuracy.

Corollary 17.1 (Scope of exact verification). Exact box and contract checks guarantee only that
the encoded state, bound metric, and declared constraints satisfy their formal conditions. Physical
safety additionally requires valid sensing, calibration, model coverage, uncertainty control, actuator
compliance, and any independent runtime safety mechanisms mandated by the domain.

18     Worked Drone Example
Consider a multirotor operating in a mapped but partially changing environment. The observation
packet contains synchronized camera, inertial, altitude, localization, battery, and flight-mode data.
The scene graph contains the vehicle, obstacles, candidate landing zones, corridor segments, and
geofence regions.

18.1    Predicates and relations
Possible predicates include

                   inside_authorized_corridor,    obstacle_clear,    battery_safe,
                                                                                                  (72)
               landing_zone_stable,     localization_reliable,   emergency_reachable.

A structural entailment may be

                          certified_landing_zone ⇒ landing_zone_stable,                           (73)

and an incompatibility may be

                     inside_authorized_corridor ⊥ inside_hard_no_fly_region                       (74)

for the same spatial point. Other predicate pairs are irrelevant unless explicitly constrained.

18.2    Current action surface
Suppose the current surface is

                         Σt = {velocity_control, hover, land, return_home}                        (75)

with payload actuation unavailable. A semantic hypothesis that requires payload release may
remain plausible as a mission explanation but is not currently realizable. The route is therefore
surface-unresolved rather than semantically false.

18.3    Bound contract
Assume the proposer suggests “move toward the nearest certified emergency landing zone.” The
binder identifies a landing-zone descriptor dL and registers

                          µ(Gt ; dL ) = risk-weighted path distance to dL .                       (76)

                                                 18

The favorable direction is d = −1, because smaller is better. The binder computes the baseline
from the trusted current scene, not from the proposer’s numeric estimate. A candidate action
is predictively ranked by expected distance reduction, collision risk, localization uncertainty, and
surface stability.
    After the accepted action, the verifier recomputes the before and after metric from the trusted
transition. A decrease exceeding τprog is REQUIRED progress. A legal action with negligible change
is IRRELEVANT. An increase beyond the failure margin or a geofence violation is FORBIDDEN.
A localization discontinuity, stale target binding, or predictive-only evaluation is UNRESOLVED.

18.4    Recovery
If localization becomes unreliable, a recovery policy may authorize hover and re-localization. This
is an environment- and capability-conditioned recovery action. If the mission deadline or energy
reserve is already exhausted, the system must not pretend that the same recovery constitutes a
fresh mission attempt; it must execute the appropriate terminal safety action under the higher-
priority budget policy.

19     Implementation Invariants and Test Obligations
A conforming implementation should regression-test at least the following invariants:

  1) predictive rollouts cannot call factual transition writers;

  2) there is exactly one factual commit point for accepted transitions;

  3) no second action is emitted while a prior transition token is pending;

  4) containment and incompatibility losses satisfy the equivalences in section 17;

  5) structural box checks are not confused with grounded state membership;

  6) the binder recomputes baselines and rejects stale contracts;

  7) every route step retains its action-surface contract;

  8) a surface mismatch invalidates route realization, not automatically the parent mechanic;

  9) semantic proposals cite known canonical claims;

 10) a revision cites eligible parents and performs its declared change;

 11) route failure does not blanket-contradict all assumptions;

 12) positive memory requires observed or independently verified source lineage;

 13) proposer-authored explanations remain proposed without independent evidence;

 14) recovery preserves mission-scoped observed knowledge and clears state-local execution state;

 15) external timeout, energy exhaustion, or action-limit termination cannot emit a reset-like
     transition;

 16) the loop cannot exit normally with an un-ingested accepted action.

    Trace artifacts should include the canonical evidence ledger, belief delta, proposer input and
output, binder result, route and surface contract, predictive score, pre-action verifier result, pend-
ing transition token, post-action observation, contract result, exact verdict, memory event identi-
fiers, and nondeterminism classification.

                                                 19

20     Research Modules and Domain Substitution
The architecture remains fixed while domain modules vary.

   Core interface          Robotics or drone realization      Abstract reasoning realization
   Perception adapter      Sensor fusion, detection,          Grid parsing, object extraction,
                           tracking, mapping                  relation graph
   Action surface          Flight modes, actuator limits,     Available action symbols,
                           payload and safety                 interaction modes, coordinate
                           authorization                      actions
   World model             Stochastic physical and sensor     State-transition and
                           dynamics                           action-effect model
   Semantic grounding      Objects, regions, trajectories,    Objects, colors, shapes,
                           hazards                            topology, transformations
   Binder metrics          Distance, clearance, energy,       Graph distance, overlap
                           stability, tracking error          mismatch, alignment,
                                                              containment, endpoint error
   Research modules        Active perception, calibration     Action-semantics probe,
                           maneuver, system identification    coordinate probe, ambiguity
                                                              resolution
   Recovery policy         Hover, re-localize,                Level reset or controlled
                           return-to-home, divert, land       termination when explicitly
                                                              available
   Hard verifier           Geofence, collision shield,        Action legality, exact state and
                           actuator and energy limits         contract checks

    A research module is allowed to choose an information-gathering action only when it is tied to
a registered question with an explicit prior, expected evidence, disconfirming evidence, required
surface, and resolution rule. Unregistered random exploration is not a valid degraded fallback.

21     Development Roadmap
21.1   Stage 1: Static verified baseline
Implement the observation adapter, action-surface synchronization, object-centric world model,
fixed ontology, corrected box losses, deterministic binder, receding-horizon planner, pre-action
verifier, and single post-action commit point.

21.2   Stage 2: Calibrated uncertainty and active research
Add ensemble or Bayesian uncertainty, held-out calibration, registered questions, and information-
gain probes. Require explicit separation between task progress and epistemic progress.

21.3   Stage 3: Canonical evidence and recursive revision
Introduce canonical claims, belief deltas, parent–child hypothesis lineage, assumption statuses,
and typed revision operators. Preserve superseded hypotheses for audit and learning.

21.4   Stage 4: Event-sourced memory and attempt recursion
Add canonical memory events, deterministic consolidation, mission-scoped transfer, recovery bound-
aries, and external termination causes. Validate preserved and cleared state explicitly.

                                               20

21.5    Stage 5: Controlled predicate and relation induction
Propose new predicates from persistent residual structure, but require utility, identifiability, held-
out stability, and compatibility checks. New predicates remain proposed until observed evidence
supports their grounding. Relation induction must distinguish absence of counterexamples from
evidence of incompatibility.

21.6    Stage 6: Richer semantic geometries
Introduce unions of boxes, temporal constraints, relation-specific spaces, or neural energy regions
only when the fixed box family is empirically inadequate. Preserve exact or certified checking for
hard constraints whenever possible.

21.7    Stage 7: Hierarchical skills and long-horizon planning
Learn temporally extended skills with explicit initiation surfaces, termination conditions, measur-
able contracts, and failure scopes. High-level plans must compile to lower-level verified actions
without bypassing the post-action truth boundary.

22     Conclusion
The revised UIM is not merely a latent world model with a logical regularizer. It is an authority-
structured agent architecture. Its central invariants are that predictions do not become facts,
proposals do not become actions, explanations do not become confirmed mechanics, and route
failures do not erase unrelated assumptions. Corrected box mathematics provides a coherent
geometric ontology, but runtime semantics is grounded in entity membership and measurable
state transitions rather than repeated inspection of static box relations.
    The architecture is shared across robotics, drones, and abstract reasoning systems because the
essential control problem is the same: infer under partial observability, propose testable structure,
bind it to measurable quantities, plan under changing action surfaces, verify before and after
action, and retain only evidence-grounded knowledge. Different domains supply different con-
straints and research modules; the authority hierarchy, verification contracts, recursive revision,
and event-sourced memory remain unchanged.

References
 [1] N. P. Brusentsov. Improving the Logic of Inferences. New Millennium Foundation, 2012.

 [2] J. Schmidhuber. Making the world differentiable: On using self-supervised recurrent neural
     networks for reinforcement learning and planning. Technical Report FKI-126-90, 1990.

 [3] D. Ha and J. Schmidhuber. World Models. arXiv:1803.10122, 2018.

 [4] Y. LeCun. A Path Towards Autonomous Machine Intelligence. OpenReview, 2022.

 [5] G. Hinton, O. Vinyals, and J. Dean.         Distilling the Knowledge in a Neural Network.
     arXiv:1503.02531, 2015.

 [6] C. Buciluă, R. Caruana, and A. Niculescu-Mizil. Model Compression. In Proceedings of KDD,
     2006.

 [7] R. Y. Rubinstein and D. P. Kroese. The Cross-Entropy Method: A Unified Approach to Com-
     binatorial Optimization, Monte-Carlo Simulation, and Machine Learning. Springer, 2004.

                                                 21

 [8] J. B. Rawlings, D. Q. Mayne, and M. Diehl. Model Predictive Control: Theory, Computation,
     and Design. Nob Hill Publishing, second edition, 2017.

 [9] R. T. Rockafellar and S. Uryasev. Optimization of conditional value-at-risk. Journal of Risk,
     2(3):21–41, 2000.

[10] A. Bardes, J. Ponce, and Y. LeCun. VICReg: Variance-Invariance-Covariance Regularization
     for Self-Supervised Learning. In International Conference on Learning Representations, 2022.

[11] L. P. Kaelbling, M. L. Littman, and A. R. Cassandra. Planning and acting in partially
     observable stochastic domains. Artificial Intelligence, 101(1–2):99–134, 1998.

                                               22
