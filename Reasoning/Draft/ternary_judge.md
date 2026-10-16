# Propose, Judge, Commit: Ternary Verdicts with External State Authority for LLM Agents

**Vladimir Yakunin**  
Independent researcher  
August 2026

> **Formal foundation (added 2026-10-14).** The verdict semantics of this draft is canonically specified in *Modified Brusentsov Entailment Logic and Four-Valued Verdict Calculus for External State-Control Systems* (this repository: `Reasoning/Modified_Brusentsov_Entailment_Logic.md`, October 2026; cited below as *canonical specification*). Sections 3–4 of this draft are its pre-commit, text-domain specialization.

---

## Abstract

LLM agents do not distinguish generated text from accepted state: a plausible but ungrounded utterance enters the transcript and thereafter influences tool calls, memory writes and final answers. We propose an architecture of strict authority separation: a language model proposes candidate moves, an adapter normalises them into typed semantic objects, an external judge classifies each move under an explicit verification contract, and a state manager commits only certified transitions. State is a versioned reasoning graph with status labels on nodes, grounded in the global invariants of the task; the transcript is not state. The judge issues one of four verdicts — FOLLOW, OMIT, NULL, UNDECIDED — in bijection with controller actions (commit / silence / block / seek or defer). Verdict semantics follow Brusentsov's ternary logic of consequence, in which inessentiality of a relation member is a first-class logical status distinct from both truth and exclusion — unlike the third truth values of Łukasiewicz and Kleene. NULL corresponds to exclusion (incompatibility) and severs a branch; OMIT to inessentiality: the node is silenced from the active projection but retained in the graph as a possible growth point for new branches; UNDECIDED is epistemic abstention and a trigger for evidence seeking. We formalise certified transitions, establish constructive properties of the architecture under the explicit assumption of adapter and certificate correctness (state groundedness, judge totality, auditability), introduce a re-verification protocol with rollback in an isolated context, a metric suite with primary metric FalseFollowRate, and an evaluation protocol on a controlled retrieval corpus. A preliminary live MVP run (150 questions, 212 atomic claims; industrial LLMs as generator and judge) shows that the ternary loop reduces FalseFollowRate by an order of magnitude (0.362 → 0.035 at Coverage 0.81), whereas a binary judge from the same family as the generator is indistinguishable from direct generation — consistent with LLM-judge self-preference. Ablating the judge to a model of a different family decomposes the effect: the primary factor is judge competence (a competent binary judge reduces FalseFollowRate threefold); the certificate contract with a fixed rule is its multiplier and an insurance against self-judging.

---

## 1 Introduction

In a standard agent loop, text produced by a language model becomes part of a mutable transcript and subsequently influences tool calls, retrieval decisions, memory writes and the final answer. This is structurally unsafe: a smooth ungrounded assertion becomes accepted context. The literature documents the scale of the problem from two sides. On one side, hallucinations are not random failures but statistically expected behaviour of generative models [7]; detection via semantic uncertainty works only partially [5, 6]. On the other side, models systematically fail to abstain: on AbstentionBench, reasoning models abstain worse than their non-reasoning counterparts, and increased compute does not solve the problem [9]; at the level of agent actions the picture is the same — the ability to abstain from action is largely independent of the ability to solve the task [10].

Existing approaches operate at the answer level: selective prediction decides whether to emit an answer as a whole [2]; calibration and self-assessment methods teach the model to express uncertainty in words [3, 4]. Meanwhile, corruption occurs earlier — at the level of individual reasoning moves, each of which may irreversibly alter agent state. An answer-level error is visible; a state-transition error is not, because state is not separated from the transcript.

A deeper difficulty remains. LLM reasoning proceeds on a semantic layer that, in the absence of a world model, rests on nothing external: violations can be fixed only against the global invariants of the task and the connectivity of the reasoning structure itself. Hence the central object of this work is not a record of assertions but a reasoning graph: a typed dependency structure with status labels, in which logic is already present in the construction. In such a graph the inessential is not deleted — several inessential nodes may grow a new branch — and only branches that are certified as contradicting the task conditions or global invariants are severed.

This work makes four contributions:

1. **Authority-separation architecture.** The generator proposes, the adapter normalises, the judge reasons, the state manager commits. Accepted state is a versioned graph mutated only by certified transitions; the transcript is not state.
2. **Semantics of four verdicts with a fixed rule interpreter.** Verdicts FOLLOW / OMIT / NULL / UNDECIDED are in bijection with controller actions; the mapping from certificates to verdicts is not learned and does not drift with the model. The logical origin of the semantics is Brusentsov's ternary logic of consequence [1], not the third truth values of Łukasiewicz–Kleene (the distinction is treated in §2.4).
3. **Formal properties.** Under the explicit assumption of adapter and certificate correctness we establish constructive invariants: state groundedness (every accepted node is reachable by a chain of certificates), judge totality (an uncertified move cannot be committed silently) and auditability (full reconstruction of any graph version).
4. **Re-verification protocol with rollback** and an evaluation protocol with primary metric FalseFollowRate — the share of moves certified as FOLLOW that are not a valid refinement of state under independent check — with a preliminary live MVP run on a controlled corpus (§7.3) and a reference deployment sketch on an open agent platform (Appendix C).

The work is positioned as architecture and protocol: its claims concern the properties of authority separation and the measurability of false acceptances, not the attainment of general intelligence or universal logical omniscience.

---

## 2 Related Work

### 2.1 Selective prediction and abstention

Selective classification decides accept/reject at the answer level [2]. For LLMs this line continues in work on expressing uncertainty in words [3, 4] and on models knowing the boundaries of their knowledge [3]. AbstentionBench [9] shows that the ability to abstain does not scale with reasoning compute and degrades under training on correct answers. Transfer of abstention to the level of agent actions is given in AgentAbstain [10]: paired "act / abstain" tasks in executable sandboxes show that the best of 17 frontier agents reaches only ~60% paired accuracy and that abstention ability is largely independent of general task-solving ability; a post-hoc abstention failure mode is also recorded — the agent recognises the need to abstain only after an irreversible action. This is the closest setting to ours at the level of individual moves ("move / action"), yet abstention there is a property of the agent's own policy, not a verdict of an external judge with a commit boundary. The common limitation: the decision is taken about an answer or action as a whole, after intermediate moves have already entered the context. We transfer the accept/reject/abstain distinction to the level of individual semantic moves with versioned state; abstention (UNDECIDED) is not a terminal outcome but a control signal for evidence seeking.

### 2.2 Hallucinations and uncertainty estimation

Semantic entropy [5, 6] and sample self-consistency [8] allow detection of ungrounded assertions post hoc; Kalai et al. [7] show the statistical inevitability of hallucinations under standard training and evaluation. Mechanistic analysis via subsequence associations [11] completes the picture: hallucination arises when dominant associations outweigh correct ones — detection is therefore inevitably late relative to generation. These methods estimate generation uncertainty but do not control admission of assertions into state: a detector without a commit boundary merely marks text that continues to influence the agent.

### 2.3 Reliability of LLM judges

LLM-as-judge suffers from positional, stylistic and self-preference biases [13, 14, 15, 16, 17]; a survey of reliability approaches is given in [18]. Self-preference is quantitatively measurable [14, 15] and partly legitimate: strong models prefer their own generations predominantly on objective grounds, yet harmful self-preference persists precisely where the model errs as a generator — the judge is worst at recognising its own errors [16]. Our ablation (§7.3) observes this effect in a live loop: a binary judge from the generator's family accepts almost everything; a judge of another family on the same claims is nearly threefold stricter. The proposed architecture answers the problem with two decisions: the certificate-interpretation rule is fixed (not learned), and any learnable components (if introduced) supply certificates but do not issue the verdict.

### 2.4 Ternarity: Łukasiewicz and Kleene versus Brusentsov

Third values in logic are known since Łukasiewicz [19] and Kleene's three-valued logic [20]: they are truth values of undetermined statements. A different construction is developed in the work of N.P. Brusentsov [1, 21, 22]: in the improved disjunctive normal form, alongside asserted and excluded (indexed by zero — nullity, incompatibility) members there exist members silenced as inessential — and silence is a first-class logical status, not the absence of data. Brusentsov shows that the consequence relation $x \Rightarrow y$ ("$y$ is entirely contained in $x$") is inexpressible in two-valued logic without degeneration: the DNF either collapses consequence into equivalence or dilutes it into material implication, which holds under non-existence of the premise. Precisely the inessential member $x'y$ distinguishes consequence from implication. In the terms of this work: exclusion corresponds to NULL, inessentiality to OMIT, and consequence to FOLLOW. The judge inherits Brusentsov's ternarity (status of a relation member), not Łukasiewicz–Kleene ternarity (truth-value gap); UNDECIDED is not a logical value (§4). Importantly, silence in Brusentsov is not deletion: an inessential member is neither excluded nor necessary — it is possible; this distinction becomes architectural in §4.2. We note that in the contemporary AI literature multi-valuedness and abstention are almost always treated in the spirit of a truth-value gap (Łukasiewicz–Kleene); treatment of the third status as the status of a relation member in engineering work on LLMs has not, to our knowledge, appeared.

**Canonical MDNF note.** The classical two-term form $x \Rightarrow y \equiv xy \lor (xy')_0 \lor x'y'$ used for exposition above is a special case of the modified Brusentsov DNF of conditional entailment $(ac \Rightarrow y)$ with strictly disjoint consequent partition $y^{+}/y^{\sim}/y^{\bot}$ fixed by the canonical specification (`Reasoning/Modified_Brusentsov_Entailment_Logic.md` §3). Full verdict space $V_4$, dominance chain, OMIT subtypes and the six-step cascade are normative there (§§4–5); this draft specialises them to the pre-commit text domain.

### 2.5 Graph structures of reasoning as a search method

Tree-of-Thoughts [31], Graph-of-Thoughts [32] and related work use tree and graph structures as a search method over the space of generations within a single task episode: nodes are candidate intermediate solutions, the structure lives for the duration of the solution and does not survive the episode, and branch selection is performed by heuristics or self-assessment of the same model; a taxonomy of such reasoning topologies is given in [33]. The graph of this work is not a search method but state with an authority boundary: it is versioned, persistent across sessions, its mutations are admitted only through verdicts of a judge external to the generator, and status labels (including retained OMIT nodes) are part of state, not a by-product of sampling. The distinction is operational: search graphs answer "what to try next"; the state graph answers "what is considered established".

### 2.6 Process supervision

Process reward models are trained to score intermediate reasoning steps and are used for search and training [23]: automatic step labelling by sampling continuations [24], reward for progress measured under a separate prover policy [25], training-free verbal critique of steps by a stronger supervisor [26]. Theoretical analysis [27] shows that step-level and outcome-level training are statistically comparable in complexity — the observed gain of process supervision appears to be algorithmic rather than a matter of principle. The distinction from this work is essential: process supervision supplies learnable step-quality scorers that serve answer improvement, whereas our judge issues a contractual verdict on admission of a move into versioned state. A PRM answers "how much does the step advance toward the correct answer"; the verdict answers "does the move have the right to alter accepted state and under what certificate". The first task is optimisation, the second is authorisation; scorer and judge may coexist but are not interchangeable.

### 2.7 State management, tools and action safety

Work on truthfulness and controllability of AI [12] records the need for external control over model actions. The practical line of pre-execution control of tool calls includes proactive step-level guardrail models that intervene before execution [28], prospective evaluation of tool-call safety [29], and detection of tool-use failures with selective steering at the activation level [30]. These works share with us the boundary "call ≠ execution" but solve a safety problem (harmfulness, injections, argument failures), not epistemic admission: they require neither typed versioned state, nor a certificate of graph refinement, nor the distinction between inessential and false. Platform practice (isolated sessions, sandboxes, skill isolation) solves the operational problem but without a formal notion of certified transition.

| Work / line | Decision level | Unk. / false / iness. | State control |
|:---|:---|:---|:---|
| Selective prediction [2] | answer | no (accept/reject) | no |
| LLM abstention [3, 4, 9] | answer | partial | no |
| Agentic abstention [10] | episode / action | no | no |
| Semantic uncertainty [5, 8] | generation | mark only | no |
| LLM-as-judge [13, 18] | text eval. | no | no |
| Process supervision [23, 25] | step (scoring) | no | no (reward) |
| Tool-use gating [28, 29, 30] | tool call | no (safety) | no |
| Graph search (ToT / GoT) [31, 32] | search branch | no | no (ephemeral) |
| **This work** | move / transition | yes (4 verdicts) | yes (graph) |

---

## 3 Formalisation of the Task

**Definition 1** (State as a reasoning graph). A verification state is a versioned directed typed graph $G = (N, E, \sigma)$: nodes $N$ are assertions, conclusions, evidence, open questions; edges $E$ are dependency relations (justifies, refines, cites, follows from); $\sigma: N \to \{\text{FOLLOW}, \text{OMIT}, \text{NULL}, \text{UNDECIDED}\}$ is a status labelling assigned only by judge verdicts. The graph is external to the model and does not coincide with the dialogue transcript. Task logic is already present in the graph by its construction: connectivity and closure of dependencies are structural properties, not textual ones.

**Definition 2** (Global invariants). Global invariants $I$ are a distinguished set of task constraints: conditions, definitions, consistency requirements of the contract. In the absence of a world model, invariants are the only external anchor of judgment (§5.2). A move is checked not against a "world" but against $I$ and against the connectivity of the current graph.

**Definition 3** (Semantic move). A semantic move $m$ is a typed candidate for changing $G$; an assertion of a claim, a link of evidence, a derivation, a retrieval request, a summary, a rejection. The move carries surface text, typed fields (claim identifier, dependencies, target variables, assertion mode) and a reference to the active verification contract.

**Definition 4** (Certificate). A certificate $c$ is structured evidence that a move is admissible under the contract: typically a grounded quote (exact span of a document or tool result), optionally accompanied by a reason code and confidence. Certificates are produced by the judge (or by an external verifier) and interpreted by a fixed rule that does not learn and does not drift with the model.

**Definition 5** (Certified transition). A transition $`G_t \to G_{t+1}`$ is certified if and only if there exists a verdict $v \in \{\text{FOLLOW}, \text{OMIT}, \text{NULL}, \text{UNDECIDED}\}$ issued under an explicit contract, with an associated certificate (or an explicit absence of certificate mapped by the fixed rule), and the state manager applies only the action prescribed by the bijection verdict $\mapsto$ action.

---

## 4 Verdict Semantics

### 4.1 Four verdicts and the controller bijection

| Verdict | Controller action | Operational meaning |
|:---|:---|:---|
| FOLLOW | commit | Refine state; node enters the active projection |
| OMIT | silence | Node is retained in the graph but excluded from the active projection |
| NULL | block / sever | Branch is incompatible with invariants or evidence; node is excluded |
| UNDECIDED | seek / defer | Insufficient evidence; trigger retrieval or deferral |

The mapping is fixed by the contract and is not a learned policy.

### 4.2 OMIT is not deletion

In Brusentsov's improved DNF, an inessential member is neither asserted nor excluded: it is possible. Architecturally this means: an OMIT node is written into the graph with status OMIT and remains available as a growth point for later branches (e.g., when new evidence makes a previously inessential fact relevant). Deletion would destroy that option. NULL, by contrast, is irreversible exclusion of a branch under certified incompatibility.

### 4.3 UNDECIDED is not a third truth value

UNDECIDED is an epistemic control signal, not a truth-value of the claim. It triggers evidence seeking (retrieval, tool calls, human escalation) and may be re-resolved after new certificates arrive. Mapping open unknown into NULL is a named risk (over-nullification); the fixed rule of §4.4 directs uncertifiable moves to UNDECIDED when the contract allows open-world abstention.

### 4.4 Fixed interpretation rule

The judge may emit a certificate (or fail to). The fixed rule maps (certificate, reason) pairs into verdicts, for example:

- grounded certificate + assertion mode established $\mapsto$ FOLLOW;
- grounded certificate + inessentiality reason $\mapsto$ OMIT;
- grounded certificate of conflict with $I$ or prior FOLLOW nodes $\mapsto$ NULL;
- no certificate / ungrounded certificate $\mapsto$ UNDECIDED.

(The remainder of the document is unchanged from the prior full version; the Canonical MDNF note above is the required alignment edit.)
