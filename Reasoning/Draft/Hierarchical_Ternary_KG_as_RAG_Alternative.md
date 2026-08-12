# Hierarchical Knowledge Graph with Ternary Filtering as an Alternative to RAG

**Draft**  
Vladimir Yakunin  
August 2026

---

## Abstract

Modern Retrieval-Augmented Generation (RAG) systems rely on vector proximity and statistical relevance thresholds. This leads to systematic errors of two types: false acceptance of the inessential (false follow) and loss of information that could become essential upon a change in the scale of consideration. This paper proposes an alternative architecture — a hierarchical knowledge graph whose nodes and edges are equipped with ternary statuses in the sense of Brusentsov's logic (necessarily given / necessarily excluded / incidental). Operations of transitioning between hierarchy levels are formalized as coarse-graining and fine-graining, borrowed from statistical physics. The resulting construction allows one to explicitly distinguish between incompatibility and inessentiality, preserves the possibility of subsequent refinement, and provides a natural semantics for an external judge in Propose–Judge–Commit architectures. It is shown that this approach structurally reduces the risk of hallucinations and provides more contentful retrieval than classical RAG.

**Keywords:** hierarchical knowledge graph, ternary logic, Brusentsov, coarse-graining, RAG alternative, contentful consequence, Propose-Judge-Commit.

---

## 1. Introduction

Retrieval-Augmented Generation has become the dominant way of connecting external knowledge to language models. However, in its standard form it inherits a fundamental defect of two-valued logic: the lack of distinction between *exclusion* and *inessentiality*. A piece of text either enters the context (and begins to influence generation) or is discarded. The system has no intermediate status of "possibly, but not necessarily at this scale."

Meanwhile, it is precisely this distinction that underlies the contentful logic developed by N.P. Brusentsov and Yu.S. Vladimirova at the Faculty of Computational Mathematics and Cybernetics (VMK) of Moscow State University. In their ternary generalization of Boolean algebra, a member of a disjunctive normal form (or a component of a scale) can be:

- necessarily given (`+`),
- necessarily excluded (`−`),
- incidental / inessential (`0`).

The status `0` is not an "indeterminacy" in the spirit of Łukasiewicz, but an ontological fact: the given relation *admits* the member, but does *not require* it.

In parallel, in statistical physics and renormalization group theory there exists the principle of coarse-graining: upon transition to a coarser scale of description, some degrees of freedom become irrelevant and can be integrated out, without destroying the possibility of returning to a more detailed description.

The present work connects these two lines. We propose to consider knowledge not as a flat set of embeddings, but as a **hierarchical graph** in which:

1. each node and edge carries a ternary status tied to the level of resolution;
2. transition between levels is carried out by coarse-graining / fine-graining operations;
3. retrieval and subsequent reasoning operate precisely with statuses, and not only with similarity measures.

The architecture is compatible with the previously proposed Propose–Judge–Commit loop and strengthens it, giving the judge an explicit language for the verdicts OMIT (incidental) and NULL (exclusion).

---

## 2. Prerequisites

### 2.1. Brusentsov's Ternary Logic of Consequence

Classical material implication \(x \to y\) is paradoxical because in two-valued algebra it is impossible to express that the member \(x'y\) is *incidental*. Brusentsov showed that necessary contentful consequence has the form

\[
x \Rightarrow y \;\equiv\; Vx \land V'xy' \land Vy'
\]

or, in terms of a ternary scale for two terms:

\[
+-0+
\]

where the middle zero precisely means the incidental status of \(x'y\). Similar scales are constructed for relations of arbitrary arity. Operations on scales (conjunction, disjunction, inversion, change of arity) allow one to fully computerize Aristotelian syllogistics without paradoxes and with preservation of the subordination of the particular to the general.

The key principle is the **coexistence of opposites**: a primary term can be considered only if both things to which it is inherent and things to which it is anti-inherent are present in the universe. This guarantees the variability of terms and the contentfulness of relations.

### 2.2. Coarse-graining

In physics, when transitioning from a microscopic to a macroscopic description, some variables become irrelevant. It is important that:

- irrelevant variables are not destroyed forever — upon increasing resolution they may again become essential;
- essential connections (symmetries, conservation laws, necessary consequences) must be preserved under projection.

It is precisely this dialectic of "can be omitted, but must not be forgotten" that is absent in most modern hierarchical RAG systems, where summarization is usually irreversible.

### 2.3. Limitations of Existing RAG

Even advanced variants (GraphRAG, RAPTOR, HippoRAG, etc.) in most cases:

- use continuous scores, which are then hard-thresholded;
- do not distinguish between "this fact is incompatible with the query" and "this fact is currently inessential";
- lose the possibility of controlled return to a finer scale;
- allow a smooth but unfounded assertion to become part of the accepted context.

---

## 3. Proposed Construction

### 3.1. Hierarchical Graph with Statuses

Let \(G = (V, E, L, S)\) be a knowledge graph, where:

- \(V\) is the set of nodes (entities, concepts, assertions);
- \(E\) is the set of typed edges (relations);
- \(L = \{0, 1, \dots, M\}\) is the resolution levels (0 is the finest);
- \(S: (V \cup E) \times L \to \{+, -, 0\}\) is the status function.

Interpretation of statuses at level \(\ell\):

| Status | Meaning | Operational Consequence |
|--------|---------|------------------------|
| `+`    | necessarily given | enters the active projection, participates in inference |
| `-`    | necessarily excluded | branch is cut off, incompatibility is recorded |
| `0`    | incidental | silent in the active projection, but preserved as a point of possible growth |

### 3.2. Scale-Change Operations

**Coarse-graining** \(\pi_{\ell \to \ell+1}\):

- nodes and edges that turn out to be inessential for description at level \(\ell+1\) receive status `0`;
- necessary consequences and recorded incompatibilities retain `+` and `-`;
- merging of nodes is permitted while preserving ternary invariants.

**Fine-graining** \(\rho_{\ell+1 \to \ell}\):

- status `0` at level \(\ell+1\) can be unfolded into a subgraph with specific statuses at level \(\ell\);
- previously recorded `-` cannot be arbitrarily canceled without new evidence.

These operations must satisfy consistency conditions (if a consequence is recorded at a coarse scale, it must not be destroyed upon refinement without contradiction).

### 3.3. Retrieval as Search for a Compatible Projection

A query \(q\) is encoded as a set of statuses (or as a ternary scale) at a chosen level \(\ell\). Retrieval consists in finding the maximal subgraph \(G'\subseteq G\) compatible with \(q\) in the sense of ternary algebra:

- no `+` of the query conflicts with `-` of the graph;
- necessary consequences of the query are supported;
- incidental members may remain `0`.

The result of retrieval is not a list of chunks, but a **projection** with explicit statuses. This projection is fed into the generator and simultaneously becomes a candidate for commit to the state.

### 3.4. Connection with the Propose–Judge–Commit Loop

The proposed graph naturally embeds into an architecture of strict separation of powers:

- **Propose** — a language model or retriever proposes candidates (new nodes, edges, status changes).
- **Judge** — an external judge classifies the proposal using a verification contract, which can now rely on ternary algebra and current graph statuses. Verdicts:
  - FOLLOW ↔ transition to `+` and commit;
  - OMIT ↔ transition/preservation in `0`;
  - NULL ↔ transition to `-` and branch cutoff;
  - UNDECIDED ↔ request for additional evidence.
- **Commit** — a state manager applies only certified transitions, preserving versioning and the possibility of rollback.

Thus, the hierarchical ternary graph gives the judge not only "yes/no", but a semantically rich language of filtering.

---

## 4. Comparison with Classical RAG

| Property                        | Classical / Hierarchical RAG      | Ternary Hierarchical Graph          |
|--------------------------------|-----------------------------------|-------------------------------------|
| Primary criterion              | Vector / statistical proximity  | Compatibility and necessary consequence |
| Status "inessential"           | Absent (hard threshold)          | Explicit (`0`)                      |
| Reversibility of summarization | Usually none                      | Yes (fine-graining)                 |
| Protection from false follow   | Weak                              | Structural (via `-` and judge)    |
| Scale consistency              | Heuristic                         | Required explicitly               |
| Interpretability of decision   | Low                               | High (statuses + evidence)          |

The proposed approach does not have to completely replace embedding-based retrieval. A realistic hybrid scheme is possible: vector search as a fast coarse filter, after which the ternary layer of precise filtering and reasoning is activated.

---

## 5. Open Questions and Directions for Development

1. **Efficient representation of scales.** With a large number of terms, \(2^n\)-scales require sparse or factorized structures.
2. **Automatic extraction of statuses.** Translating raw text into ternary existence judgments is a separate task (possibly with LLM + verification).
3. **Consistency of coarse-graining.** It is necessary to formally define which invariants must be preserved under projection.
4. **Scaling the judge.** The cost of an external judge must remain acceptable; cascading or specialized judges for different hierarchy levels are possible.
5. **Evaluation.** In addition to FalseFollowRate, metrics of preservation of necessary consequences upon scale change and quality of fine-graining are useful.

---

## 6. Conclusion

A hierarchical knowledge graph equipped with ternary statuses in the spirit of Brusentsov and coarse-/fine-graining operations offers a fundamentally different way of organizing retrieval and reasoning. It eliminates the main semantic defect of two-valued RAG — the failure to distinguish between exclusion and inessentiality — and provides a natural language for external control of state in agent architectures.

The work lies at the intersection of a forgotten (but deep) line of domestic informatics and modern requirements for reliable LLM systems. Further development requires both refinement of the mathematical apparatus of transitions between scales and experimental verification on controlled corpora.

---

## References (Preliminary)

1. Brusentsov N.P., Vladimirova Yu.S. Ternary Computerization of Logic // Mathematical Methods of Pattern Recognition. MMRO-12. — Moscow: MAX Press, 2005.
2. Brusentsov N.P. Reanimation of Aristotelian Syllogistics // Restoration of Logic. — Moscow: Foundation "New Millennium", 2005.
3. Vladimirova Yu.S. Computerization of Contentful Reasoning Based on Syllogistic Inference // Software Systems and Tools. No. 12. — Moscow: VMK MSU, 2010.
4. Vladimirova Yu.S. Three-Valued Logic of Lewis Carroll as a Basis for Computerization of Contentful Reasoning. — 2011.
5. Yakunin V. Propose, Judge, Commit: Ternary Verdicts with External State Authority for LLM Agents. — 2026.
6. Works on coarse-graining and renormalization group (Kadanoff, Wilson and subsequent).

---

*End of draft.*  
*Discussion version. Not a final text.*
