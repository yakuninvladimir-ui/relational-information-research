# Propose, Judge, Commit: Ternary Verdicts with External State Authority for LLM Agents

**Vladimir Yakunin**  
Independent researcher  
August 2026

---

## Abstract

LLM agents do not distinguish generated text from accepted state: a plausible but ungrounded utterance enters the transcript and thereafter influences tool calls, memory writes and final answers. We propose an architecture of strict authority separation: a language model proposes candidate moves, an adapter normalises them into typed semantic objects, an external judge classifies each move under an explicit verification contract, and a state manager commits only certified transitions. State is a versioned reasoning graph with status labels on nodes, grounded in the global invariants of the task; the transcript is not state. The judge issues one of four verdicts — FOLLOW, OMIT, NULL, UNDECIDED — in bijection with controller actions (commit / silence / block / seek or defer). Verdict semantics follow Brusentsov's ternary logic of consequence, in which inessentiality of a relation member is a first-class logical status distinct from both truth and exclusion — unlike the third truth values of Łukasiewicz and Kleene. NULL corresponds to exclusion (incompatibility) and severs a branch; OMIT to inessentiality: the node is silenced from the active projection but retained in the graph as a possible growth point for new branches; UNDECIDED is epistemic abstention and a trigger for evidence seeking. We formalise certified transitions, establish constructive properties of the architecture under the explicit assumption of adapter and certificate correctness (state groundedness, judge totality, auditability), introduce a re-verification protocol with rollback in an isolated context, a metric suite with primary metric FalseFollowRate, and an evaluation protocol on a controlled retrieval corpus. A preliminary live MVP run (150 questions, 212 atomic claims; industrial LLMs as generator and judge) shows that the ternary loop reduces FalseFollowRate by an order of magnitude (0.36 → 0.035 at Coverage 0.81), whereas a binary judge from the same family as the generator is indistinguishable from direct generation — consistent with LLM-judge self-preference. Ablating the judge to a model of a different family decomposes the effect: the primary factor is judge competence (a competent binary judge reduces FalseFollowRate threefold); the certificate contract with a fixed rule is its multiplier and an insurance against self-judging.

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

**Definition 5** (Certified transition). A transition $G_t \to G_{t+1}$ is certified if and only if there exists a verdict $v \in \{\text{FOLLOW}, \text{OMIT}, \text{NULL}, \text{UNDECIDED}\}$ issued under an explicit contract, with an associated certificate (or an explicit absence of certificate mapped by the fixed rule), and the state manager applies only the action prescribed by the bijection verdict $\mapsto$ action.

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
- no certificate / ungrounded certificate $\mapsto$ UNDECIDED (or forced NULL under closed-world assumption).

The rule is not trained; any future learned component may only propose certificates, not override the mapping.

---

## 5 Architecture

### 5.1 Authority separation

Four roles with non-overlapping powers:

1. **Generator** — proposes candidate text / moves; has no write access to state.
2. **Adapter** — extracts and normalises typed semantic moves from generator output; validates schema.
3. **Judge** — under the active contract, produces certificates and reason codes; does not mutate state.
4. **State manager** — applies only certified transitions; maintains versioning, audit log and active projection.

### 5.2 Judgment without a world model

In the absence of a world model the only external anchors are the global invariants $I$ and the connectivity of $G$. A move that would introduce a cycle contradicting $I$, or that cannot be grounded in available evidence under the contract, cannot receive FOLLOW. Coherence is necessary, not sufficient: a graph consistent with $I$ may still be coherently false. Sufficiency appears only with external evidence (retrieval, tools) or a world model — an open boundary of the architecture.

### 5.3 Re-verification with rollback

At configurable checkpoints the state manager may re-judge a subset of committed nodes in an isolated context (without mutating the live graph). If a previously FOLLOW node fails re-verification, the protocol rolls back to the last consistent checkpoint and marks the affected subgraph for re-growth. This protects against silent accumulation of errors that only become visible after later evidence arrives.

---

## 6 Constructive Properties

Under the explicit assumption that the adapter correctly extracts moves and that certificates are faithful to the evidence they cite, the following hold as constructive invariants of the architecture (not as empirical claims about any particular model):

**Property 1** (Groundedness). Every node with status FOLLOW is reachable from evidence or invariants by a finite chain of certified transitions.

**Property 2** (Totality of the judge). No move can be committed without a verdict. Uncertified moves are mapped by the fixed rule to UNDECIDED or NULL; silent acceptance is excluded by construction.

**Property 3** (Auditability). For every version $G_t$ the audit log contains the full sequence of moves, verdicts, certificates and rule applications sufficient to reconstruct $G_t$ from $G_0$.

These properties are conditional on adapter and certificate correctness; adapter hallucinations remain a residual risk (§8).

---

## 7 Evaluation Protocol and Live MVP

### 7.1 Primary metric

**FalseFollowRate (FFR)** — the share of moves certified as FOLLOW that are not a valid refinement of state under independent gold check. **Coverage** is the share of questions that receive at least one committed answer. Secondary metrics: FalseNullRate, FalseUndecidedRate, UnsupportedClaimRate, cost per correct answer (tokens).

### 7.2 Corpus and configurations

Controlled synthetic corpus: 40 documents, 150 questions (60 supported / 30 contradiction / 30 unanswerable / 30 redundancy), automatic gold labels. Three configurations: direct (generator only), binary (generator + binary confirm/reject judge), ternary (generator + ternary judge + fixed rule). Certificates are symbolic (exact substring of a document). Independent FOLLOW check uses exact span of the gold value after normalisation.

### 7.3 Live results

Live run (2026-08-09): generator and main judge qwen3.6-plus (DashScope, T=0), 212 atomic claims. Offline rescore after tightened gold check.

| Metric | direct | binary | ternary |
|:---|:---|:---|:---|
| FalseFollowRate (primary) | 0.362 (68/188) | 0.364 (68/187) | 0.035 (4/116) |
| Coverage | 1.00 | 1.00 | 0.81 |
| UnsupportedClaimRate | 0.362 | 0.364 | 0.035 |
| FalseNullRate (supported) | 0 (0/60) | 0.017 (1/60) | 0 (0/60) |
| FalseUndecidedRate (supported) | 0 | 0 | 0.133 (8/60) |

Wilson intervals for ternary FFR and the baselines do not overlap; the order-of-magnitude claim is stable at this sample size.

**Absence-claims sensitivity.** On unanswerable questions the live generator produces meta-statements of absence rather than fabricated values (24/24). These are excluded from the primary denominator. All three treatments:

| Absence treatment | direct | binary | ternary | direct/ternary |
|:---|:---|:---|:---|:---|
| excluded (primary) | 0.362 | 0.364 | 0.035 | 10.5× |
| valid FOLLOW | 0.321 | 0.322 | 0.029 | 10.9× |
| invalid FOLLOW (conservative) | 0.434 | 0.436 | 0.179 | 2.4× |

Even under the conservative treatment the ternary loop halves FFR.

**OMIT probe.** Under a neutral prompt the live generator produces no redundancy. A separate slice with a provocative prompt ("include relevant background") on 30 redundancy questions yielded 6 background facts: all 6 received OMIT and did not enter the answer (ternary FFR 0 on the slice vs. 0.091 for direct and binary).

**Judge ablation.** Replacing the judge with deepseek-v4-flash (different family) on cached generator claims:

| FFR (absence excluded) | direct | binary | ternary |
|:---|:---|:---|:---|
| judge deepseek-v4-flash | 0.362 | 0.134 | 0.145 |
| judge qwen3.6-plus (main) | 0.362 | 0.364 | 0.035 |

The ablation decomposes the effect. First, the leniency of a binary judge from the generator's family (0.364 ≈ direct) is consistent with LLM-judge self-preference [14, 15, 16]: a judge that "recognises" its own generations accepts them almost always, whereas a judge of another family is nearly threefold stricter on the same claims — without any certificate contract. Second, under a less competent judge the advantage of the contract over a binary verdict disappears (0.145 vs. 0.134, within noise), while under a competent judge it is an order of magnitude (0.035 vs. 0.364). Conclusion: the primary factor is judge competence; the certificate contract with a fixed rule is its multiplier and insurance against self-judging (the ternary loop reaches 0.035 even under a same-family judge). Two judges are two observation points: dependence of effect magnitude on competence is reported as an observation, not as a scaling law.

**Summary of §7.3.** On the controlled corpus the ternary loop reduces FalseFollowRate by an order of magnitude (0.36 → 0.035) at Coverage 0.81 and false-abstention rate 13%. A binary verdict alone has no effect under a same-family judge; a competent binary judge reduces FFR threefold. The durable architectural difference is not the verdict label but the bundle "grounded certificate + fixed rule": it multiplies judge competence and remains effective under self-judging. Transfer to open domains is not claimed (§8).

---

## 8 Limitations

1. **Cost.** The architecture is multiplicative in calls: $C_{\text{turn}} = C_G + k \cdot C_A + k \cdot C_J + m \cdot C_R + r \cdot C_{\text{rejudge}} + C_F$ (Appendix B). FFR reduction is paid for in calls; economic gain is possible only via cascaded configurations (cheap models on extraction, strong models on disputed moves and checkpoints).
2. **Connectivity is not truth.** Judgment without a world model is limited to internal coherence: a graph consistent with $I$ and connected may be coherently false. Invariant and graph checks are necessary conditions; sufficiency appears only with external evidence or a world model. This is a principled boundary of the MVP, not an implementation defect.
3. **Adapter hallucinations.** Invented moves corrupt the pipeline before the judge. Mitigation — grounding on spans and schema validation; the risk is not fully eliminated, and Property 6.1 is conditional on adapter correctness. In the §7.3 run the adapter is trivial and the risk was not stressed.
4. **Contract ambiguity.** Verdicts are inconsistent across domains under vague contracts; the MVP uses one contract per domain, without a universal fallback.
5. **Over-nullification.** Mapping open unknown to NULL is a named risk: severing is irreversible, and a false NULL is costlier than a false UNDECIDED; the rule of §4.4 directs uncertifiable moves to UNDECIDED, but the quality of the distinction depends on certificates.
6. **No learned judge.** The current version is a rule over certificates; a discriminative learned certificate scorer is future work (risk: drift toward a preference model, §2).
7. **Evaluation scale.** The MVP is limited to a controlled corpus; transfer to open domains is not claimed. Retrieval is token overlap with stop words: sufficient for 40 documents, on live collections it will be a source of noise and false UNDECIDEDs. One run per configuration at zero temperature; self-check and "platform without middleware" baselines were not run.
8. **Certificate-scheme defects shown by the live run.** (a) Absence-claims: a positive quote-substring cannot in principle certify absence of evidence, yet the judge issued CERTIFIED on such moves — a scheme defect, not an implementation error; a separate verdict/rule or a semantic adequacy check of the quote is required. (b) NULL-by-conflict: contradiction is a relation between two documents, while the certificate is unary; 30/60 contradictions ended in UNDECIDED precisely because a single-quote certificate could not be assembled. The scheme needs a binary variant (quote-pair).
9. **Dependence of effect on judge competence.** The ablation shows that effect direction is robust to judge family, but magnitude depends on competence; under a weak judge the advantage of the contract over a binary verdict may vanish. The observation is based on two judges and is not a scaling law.
10. **Graph persistence was not tested in the MVP.** The §7.3 run quantifies verdict quality in the loop "verdict → fixed rule → commit/block"; writing of OMIT nodes, invariants, re-verification with rollback and branch re-growth (§5.2–§5.3) are future work; RegrowthYield is not defined in the MVP.

---

## 9 Conclusion

The architecture transfers the question of trust from the level of text to the level of state transitions. Authority separation (generator proposes — judge reasons — state commits), four verdicts in bijection with controller actions, a graph form of state and a fixed rule interpreter provide a constructive boundary between the plausible and the accepted, and the metric FalseFollowRate makes that boundary measurable. A preliminary live MVP run confirms that the boundary is measurable in practice: the ternary loop reduces FalseFollowRate by an order of magnitude (0.36 → 0.035 at Coverage 0.81). The experiment also yields two negative results that clarify the mechanism. First: a binary judge from the generator's family is nearly useless — on FalseFollowRate it is indistinguishable from direct generation, consistent with LLM-judge self-preference [14, 15, 16]. Second: under a judge of another family a binary verdict alone reduces FalseFollowRate threefold, and the advantage of the contract over it disappears — effect magnitude depends on judge competence. What disciplines is therefore not the fact of judging and not the verdict label, but the bundle of a grounded certificate with a fixed interpretation rule: it multiplies judge competence and remains effective even under self-judging. The logical foundation is Brusentsov's ternarity: inessentiality as a first-class status without which consequence degenerates — to our knowledge first applied to control of LLM-agent state; its graph reading (silence with retention, severing only under certified contradiction) turns out to be a working mechanism for restructuring reasoning branches. A graph with global invariants is a surrogate anchor layer for judgment in the absence of a world model; a world model as the first layer against which the judge would compare the semantic layer remains an open direction, together with learnable certificate scorers without preference drift, binary certificates for contradictions, cascaded economical configurations and transfer of the protocol to open domains.

Code, corpus, run results and rescoring scripts are open: https://github.com/yakuninvladimir-ui/mvp-ternary-judge

---

## References

[1] N.P. Brusentsov. Improvement of the Logic of Inference. Moscow: New Millennium Foundation, 2012.

[2] Y. Geifman and R. El-Yaniv. Selective Classification for Deep Neural Networks. NeurIPS, 2017. arXiv:1705.08500.

[3] S. Kadavath et al. Language Models (Mostly) Know What They Know. 2022. arXiv:2207.05221.

[4] S. Lin, J. Hilton and O. Evans. Teaching Models to Express Their Uncertainty in Words. TMLR, 2022. arXiv:2205.14334.

[5] L. Kuhn, Y. Gal and S. Farquhar. Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation. ICLR, 2023. arXiv:2302.09664.

[6] S. Farquhar et al. Detecting Hallucinations Using Semantic Entropy. Nature, 2024.

[7] A. Kalai et al. Why Language Models Hallucinate. 2025. arXiv:2509.04664.

[8] P. Manakul, A. Liusie and M. Gales. SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models. EMNLP, 2023. arXiv:2303.08896.

[9] P. Kirichenko, M. Ibrahim, K. Chaudhuri and S.J. Bell. AbstentionBench: Reasoning LLMs Fail on Unanswerable Questions. NeurIPS, 2025. arXiv:2506.09038.

[10] X. Liu et al. AgentAbstain: Do LLM Agents Know When Not to Act? 2026. arXiv:2607.10059.

[11] Y. Sun et al. Why and How LLMs Hallucinate: Connecting the Dots with Subsequence Associations. 2025. arXiv:2504.12691.

[12] O. Evans et al. Truthful AI: Developing and Governing AI That Does Not Lie. 2021. arXiv:2112.06674.

[13] L. Zheng et al. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. NeurIPS D&B, 2023. arXiv:2306.05685.

[14] A. Liusie, P. Manakul and M. Gales. LLM Evaluators Recognize and Favor Their Own Generations. NeurIPS, 2024. arXiv:2404.13076.

[15] K. Wataoka, T. Takahashi and R. Ri. Self-Preference Bias in LLM-as-a-Judge. 2024. arXiv:2410.21819.

[16] W.-L. Chen et al. Do LLM Evaluators Prefer Themselves for a Reason? 2025. arXiv:2504.03846.

[17] E. Spiliopoulou et al. Play Favorites: A Statistical Method to Measure Self-Bias in LLM-as-a-Judge. 2025. arXiv:2508.06709.

[18] J. Gu et al. A Survey on LLM-as-a-Judge. 2024. arXiv:2411.15594.

[19] J. Łukasiewicz. O logice trójwartościowej. Ruch Filozoficzny, 1920.

[20] S.C. Kleene. Introduction to Metamathematics. 1952.

[21] N.P. Brusentsov. Foundations of Informatics. Moscow: New Millennium Foundation, 1994.

[22] N.P. Brusentsov. Ordering of Mathematical Logic. Moscow: New Millennium Foundation, 2011.

[23] H. Lightman et al. Let's Verify Step by Step. ICLR, 2024.

[24] Z. Wang et al. Multi-step Problem Solving Through a Verifier: An Empirical Analysis on Model-induced Process Supervision. Findings of EMNLP, 2024. arXiv:2402.02658.

[25] A. Setlur et al. Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning. ICLR, 2025. arXiv:2410.08146.

[26] H.-Y. Chen et al. Process Supervision via Verbal Critique Improves Reasoning in Large Language Models. 2026. arXiv:2604.21611.

[27] Z. Jia et al. Do We Need to Verify Step by Step? Rethinking Process Supervision from a Theoretical Perspective. 2025. arXiv:2502.10581.

[28] Y. Mou et al. ToolSafe: Enhancing Tool Invocation Safety of LLM-based Agents via Proactive Step-level Guardrail and Feedback. 2026. arXiv:2601.10156.

[29] H. Xia et al. SafeToolBench: Pioneering a Prospective Benchmark to Evaluating Tool Utilization Safety in LLMs. 2025. arXiv:2509.07315.

[30] Y. Ke et al. A Few Neurons Reveal When LLMs Misuse Tools: Sparse Detection and Selective Steering for Reliable Tool Use (PRISMS). 2026. arXiv:2608.00218.

[31] S. Yao et al. Tree of Thoughts: Deliberate Problem Solving with Large Language Models. NeurIPS, 2023. arXiv:2305.10601.

[32] M. Besta et al. Graph of Thoughts: Solving Elaborate Problems with Large Language Models. AAAI, 2024. arXiv:2308.09687.

[33] M. Besta et al. Demystifying Chains, Trees, and Graphs of Thoughts. 2024. arXiv:2408.08702.

---

## A Data Schemas

### A.1 Verification state (graph serialisation)

```json
{
  "state_id": "s_001",
  "version": 12,
  "contract_id": "rag_fact_v1",
  "goal": "Answer the user question using accepted evidence only.",
  "nodes": [],
  "edges": [],
  "invariants": [],
  "checkpoints": [],
  "open_questions": [],
  "audit_log": []
}
```

Node: id, type, text, status $\sigma$, certificate; edge: (from, to, relation). The active projection is computed by a status filter.

### A.2 Semantic move

```json
{
  "move_id": "mv_001",
  "kind": "assert_claim",
  "surface_text": "The cited passage supports claim X.",
  "claim_id": "cl_001",
  "dependencies": ["ev_001"],
  "target_variables": ["q_2"],
  "assertion_mode": "established",
  "contract_id": "rag_fact_v1"
}
```

### A.3 Verdict

```json
{
  "move_id": "mv_001",
  "verdict": "UNDECIDED",
  "reason_code": "INSUFFICIENT_EVIDENCE",
  "confidence": 0.62,
  "certificate": null,
  "transition": null,
  "required_actions": ["retrieve"]
}
```

### A.4 Minimal verification contract

```json
{
  "contract_id": "rag_fact_v1",
  "state_schema": "ReasoningGraph",
  "candidate_schema": "SemanticMove",
  "allowed_operations": [
    "assert_claim", "link_evidence", "derive",
    "retrieve", "summarize", "reject"
  ],
  "invariants": [],
  "reverification": {
    "checkpoint_every_k_commits": 10,
    "isolated_context": true
  },
  "authority_policy": {
    "min_follow_confidence": 0.90,
    "min_null_confidence": 0.92,
    "require_citation_for_assertion": true,
    "allow_open_world_undecided": true
  }
}
```

---

## B Cost Model

| Term | Meaning |
|:---|:---|
| $C_G$ | Cost of candidate generation |
| $C_A$ | Cost of extracting and normalising one move |
| $C_J$ | Cost of judging one move |
| $C_R$ | Cost of retrieval / instrumental verification |
| $C_{\text{rejudge}}$ | Cost of re-evaluation after state update |
| $C_F$ | Cost of synthesising the final answer |
| $C_{\text{rev}}$ | Cost of re-verification at a checkpoint |
| $k, m, r$ | Numbers of moves, retrieval calls, re-evaluations |

$$C_{\text{turn}} = C_G + k \cdot (C_A + C_J) + m \cdot C_R + r \cdot C_{\text{rejudge}} + C_F$$

Session cost adds $\sum C_{\text{rev}}$ over checkpoints. The architecture is deliberately more expensive than a direct call; the MVP goal is to measure FFR reduction per unit cost, not immediate price superiority.

---

## C Reference Deployment

One possible implementation sketch (not a dependency of the architecture): a hosted agent runtime with isolated sessions, typed skills, and a middleware layer that inserts the adapter–judge–state-manager loop between the generator and any tool or memory write. Role assignment of models (cheap extractor, strong judge, optional re-judge at checkpoints) is a configuration choice. Full operational details and vendor-specific notes are maintained in the companion repository rather than in the paper body.

---

## D Glossary of Ternary Consequence Logic (after Brusentsov)

| Term | Notation | Meaning |
|:---|:---|:---|
| Consequence | $x \Rightarrow y$ | "$y$ is entirely contained in $x$"; Aristotle's $A_{xy}$ |
| Opposite | $\bar{x}$ | Complement of a term in the universe of coexisting opposites |
| Exclusion (nullity) | $xy_0$ | Incompatibility of members; index "0" |
| Inessentiality | silence of a member | Member omitted as not affecting the relation; neither excluded nor necessary — possible |
| Consequence in improved DNF | $xy \lor x\bar{y} \lor \bar{x}y$ | Member $\bar{x}y$ is silenced as inessential |
| Material implication | $xy \lor x\bar{y} \lor \bar{x}y \lor \bar{x}\bar{y}$ | Consequence with unjustifiably retained inessential member |
