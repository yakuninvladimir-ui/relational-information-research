# Hierarchical Knowledge Graph with Ternary Filtering as an Alternative to RAG

**Vladimir Yakunin**  

## Abstract

Modern Retrieval-Augmented Generation (RAG) systems rely on vector proximity and statistical relevance thresholds. This leads to systematic errors of two types: false acceptance of the inessential (false follow) and loss of information that could become essential upon a change in the scale of consideration. This paper proposes an alternative architecture — a hierarchical knowledge graph whose nodes and edges are equipped with ternary statuses in the sense of Brusentsov's logic (necessarily given / necessarily excluded / incidental). Operations of transitioning between hierarchy levels are formalized as coarse-graining and fine-graining, borrowed from statistical physics. The resulting construction allows one to explicitly distinguish between incompatibility and inessentiality, preserves the possibility of subsequent refinement, and provides a natural semantics for an external judge in Propose–Judge–Commit architectures. It is shown that this approach structurally reduces the risk of hallucinations and provides more contentful retrieval than classical RAG.

**Keywords:** hierarchical knowledge graph, ternary logic, Brusentsov, coarse-graining, RAG alternative, contentful consequence, Propose-Judge-Commit.

## 1. Introduction

The dominant paradigm of retrieval for large language models is RAG: documents or their fragments are embedded into a vector space, and relevance is determined by proximity of embeddings and a threshold. This approach systematically confuses two fundamentally different situations: (1) a fragment is incompatible with the query (contradiction), and (2) a fragment is inessential for the current scale of consideration. As a result, systems either accept noise as signal (false follow) or irreversibly lose information that would become essential upon a change of resolution.

Meanwhile, it is precisely this distinction that underlies the contentful logic developed by N.P. Brusentsov and Yu.S. Vladimirova at the Faculty of Computational Mathematics and Cybernetics (VMK) of Moscow State University. In their ternary generalization of Boolean algebra, a member of a disjunctive normal form (or a component of a scale) can be:

- necessarily given (asserted),
- necessarily excluded (nullity),
- incidental (inessential) — and the last status is first-class, not the absence of a value.

The architecture proposed here transfers this distinction into a hierarchical knowledge graph:

1. each node and edge carries a ternary status tied to the level of resolution;
2. transitions between levels are formalized as coarse-graining (projection that may render some members incidental) and fine-graining (re-introduction of previously incidental members);
3. the graph remains the external state of a Propose–Judge–Commit loop, so that statuses are assigned only by an external judge under an explicit verification contract.

The architecture is compatible with the previously proposed Propose–Judge–Commit loop and strengthens it, giving the judge an explicit language for the verdicts OMIT (incidental) and NULL (exclusion).

## 2. Formal Framework

### 2.1. Brusentsov's Ternary Logic of Consequence

Classical material implication $x \to y$ is paradoxical because in two-valued algebra it is impossible to express that the member $x'y$ is *incidental*. Brusentsov showed that necessary contentful consequence has the form

$$
x \Rightarrow y \;\equiv\; Vx \land V'xy' \land Vy'
$$

where the middle zero precisely means the incidental status of $x'y$. Similar scales are constructed for relations of arbitrary arity. Operations on scales (conjunction, disjunction, inversion, change of arity) allow one to fully computerize Aristotelian syllogistics without paradoxes and with preservation of the subordination of the particular to the general.

**Relation to other notations.** The conjunctive $V$-form states Carroll's truth-conditions of consequence ($`x_1y'_0`$: $x$ is non-empty, $xy'$ is empty) conjoined with the non-empty-universe axioms of the Aristotelian discourse ($Vx$, $Vy'$). Its classical DNF expansion is $`x \Rightarrow y \equiv xy \lor (xy')_0 \lor x'y'`$, in which the silenced incidental member is exactly $x'y$. The two forms are equivalent characterizations of one relation: truth-conditions versus expansion members. In the canonical Carroll–Brusentsov indices of the reference specification (`Reasoning/Modified_Brusentsov_Entailment_Logic.md` §1.2) the same relation reads $`(x\Rightarrow y)\equiv x_1\land(xy')_0\land y'_1`$; the reference specification further generalizes it to the normative modified DNF of conditional entailment $(ac\Rightarrow y)$ with a strictly disjoint three-way consequent partition $y^{+}/y^{\sim}/y^{\bot}$ (its §3). Classical two-term notation remains useful for exposition and is a special case of the MDNF (setting $a=x$, $c\equiv 1$); all normative verdict semantics, dominance order and OMIT subtypes are fixed by the canonical specification §§4–5.

The key principle is the **coexistence of opposites**: a primary term can be considered only if both things to which it is inherent and things to which it is anti-inherent are present in the universe. This guarantees the variability of terms and the contentfulness of relations.

### 2.2. Coarse-graining

In physics, when transitioning from a microscopic to a macroscopic description, some variables become irrelevant. It is important that:

- irrelevant variables are not destroyed forever — upon increasing resolution they may again become essential;
- essential connections (symmetries, conservation laws, necessary consequences) must be preserved under projection.

We adopt the same discipline for the knowledge graph. Coarse-graining is a projection $\pi_{\ell\to\ell+1}$ that may change statuses of nodes and edges according to the compositional law of the reference specification (§6.3). Fine-graining is the inverse operation that re-introduces previously incidental members when the scale of consideration requires them.

### 2.3. Hierarchical Knowledge Graph

A hierarchical knowledge graph $G = (N, E, \sigma, \ell)$ consists of nodes $N$, edges $E$, a status labelling $\sigma: N \cup E \to \{+, -, 0\}$ and a level assignment $\ell$. Statuses are ternary in Brusentsov's sense:

- $+$ — necessarily given at the current level;
- $-$ — necessarily excluded;
- $0$ — incidental (inessential at the current level, retained for possible fine-graining).

The exact status-transformation law is fixed in the reference specification (§6.3, Definition 6.1): a macro-element receives status $-$ if **any** of its essential micro-elements is $-$; otherwise $+$ if **any** essential micro-element is $+$; otherwise $0$. The coarse-graining status order is $-\succ_{\mathrm{cg}}+\succ_{\mathrm{cg}}0$, violated safety invariants propagate to all coarser scales, and status assignment is compositional under an explicit compatibility condition on essential subsets (Proposition 6.1). Note the polarity difference with step aggregation: in the verdict calculus the dominance chain is NULL ≻ UNDECIDED ≻ OMIT ≻ FOLLOW (reference §4.2), where OMIT outranks FOLLOW because a single unfulfilled active expectation blocks step certification; in spatial coarse-graining, a single certified ($+$) essential micro-element certifies the macro-element.

### 2.4. Retrieval as Ternary Compatibility

A query $q$ is encoded as a set of statuses (or as a ternary scale) at a chosen level $\ell$. Retrieval consists in finding the maximal subgraph $G'\subseteq G$ compatible with $q$ in the sense of ternary algebra:

- nodes/edges marked $-$ under the query are excluded;
- nodes/edges marked $0$ are admissible but not required;
- nodes/edges marked $+$ are required.

This is strictly stronger than vector proximity: incompatibility is hard exclusion, inessentiality is soft silence with retention.

### 2.5. Integration with Propose–Judge–Commit

- **Propose** — a language model (or any generator) proposes candidate moves: new nodes, edges, status changes, or level transitions.
- **Judge** — an external judge classifies the proposal using a verification contract, which can now rely on ternary algebra and current graph statuses. Verdicts:
  - FOLLOW ↔ transition to `+` and commit;
  - OMIT ↔ transition/preservation in `0`;
  - NULL ↔ transition to `-` and branch cutoff;
  - UNDECIDED ↔ request for additional evidence (an epistemic control signal, not a fourth truth value).

  The canonical verdict space, the aggregation dominance order (NULL ≻ UNDECIDED ≻ OMIT ≻ FOLLOW), and the OMIT subtype taxonomy (BLOCKED / REDUNDANT / INCIDENTAL) are fixed in the reference specification (`Reasoning/Modified_Brusentsov_Entailment_Logic.md` §§4–5).
- **Commit** — only FOLLOW transitions update the versioned graph; OMIT retains the element for possible later fine-graining; NULL severs the branch.

## 3. Comparison with Classical RAG

| Aspect | Classical RAG | Hierarchical Ternary KG |
|--------|---------------|-------------------------|
| Relevance | vector proximity + threshold | ternary compatibility |
| Incompatibility vs inessentiality | conflated | distinguished |
| Information loss | irreversible (summarization) | reversible (fine-graining) |
| External control | weak (post-hoc) | native (verdicts on state) |
| Hallucination risk | high (false follow of inessential) | reduced (OMIT is first-class) |

## 4. Conclusion

A hierarchical knowledge graph equipped with ternary statuses in the spirit of Brusentsov and coarse-/fine-graining operations offers a fundamentally different way of organizing retrieval and reasoning. It eliminates the main semantic defect of two-valued RAG — the failure to distinguish between exclusion and inessentiality — and provides a natural language for external control of state in agent architectures.

The construction is compatible with the Propose–Judge–Commit loop and with the canonical Modified Brusentsov Entailment Logic that now governs the whole corpus.

## References

1. Brusentsov N.P., Vladimirova Yu.S. Ternary Computerization of Logic // Mathematical Methods of Pattern Recognition. MMRO-12. — Moscow: MAX Press, 2005.
2. Brusentsov N.P. Improvement of the Logic of Inference. Moscow: New Millennium Foundation, 2012.
3. Canonical specification: Reasoning/Modified_Brusentsov_Entailment_Logic.md (this repository).
