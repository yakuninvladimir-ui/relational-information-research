# Relational Information Research

Independent research program spanning:

1. **Relational and informational philosophy**
2. **Causal-phase approaches to effective geometry**
3. **Verifier-centered reasoning, agent architectures, and a latent-space hypothesis of consciousness**

This repository holds the current working documents only.
Earlier and superseded materials remain archived on Zenodo.

**Start here:** [Unified Informational-Constructive Framework](Unified%20Informational-Constructive%20Framework.md)
→ cross-level map of theses, verification statuses (FOLLOW / OMIT / NULL / UNDECIDED), isomorphism of levels, and the experimental program.

**Canonical logic:** [Modified Brusentsov Entailment Logic](Reasoning/Modified_Brusentsov_Entailment_Logic.md)
→ the single formal foundation of ternary / four-valued verdict semantics for the whole corpus: modified Brusentsov DNF, verdict calculus V4 (FOLLOW / OMIT / NULL / UNDECIDED) with dominance semilattice, certificates, ensemble law quantifiers, metric / box / graph realizations. Documents that define verdict semantics cite it as normative.

---

## Repository layout

```
├── Unified Informational-Constructive Framework.md   # synthesis & archive map (v1.7)
├── Philosophy/
│   └── The Algorithm of Being.md
├── Physics/
│   ├── Causal_Phase_Geometry_Research_Program_v2.md  # active program (v2.0, Oct 2026)
│   ├── Causal_Phase_Geometry_Research_Program.md     # historical predecessor (Aug 2026)
│   ├── Technical_Specification_v0.2.md               # consolidated pilot (Mode A + Mode B)
│   ├── Technical_Specification_v0.1.1_Gamma_corr_Extraction.md  # historical static pilot
│   ├── KK_Jacobson_Commutativity_Note.md             # historical: 5D route frozen (Aug 2026)
│   └── old_test/                                     # internal working data (see below)
├── Reasoning/
│   ├── Modified_Brusentsov_Entailment_Logic.md       # canonical formal-logical foundation (verdict semantics)
│   ├── Spectral_and_Matrix_Realization_of_V4.md      # geometric/matrix realization of V4 in latent spaces
│   ├── Unified_Implementable_Model.md
│   ├── External_Ternary_Judge_Adapter.md
│   ├── Self_Developing_Runtime_Research_Program.md
│   ├── latent_information_structuring.md             # geometry of latent representations (EN)
│   ├── Latent_Agency_Framework.md
│   └── Draft/                                        # working drafts, not formal deliverables
│       ├── ternary_judge.md
│       └── Hierarchical_Ternary_KG_as_RAG_Alternative.md
├── Engineering/
│   ├── architectural_specification_v10_9.md                # Version 10.9
│   └── engineering_specification_v10_9.md                  # Version 10.9
├── LICENSE                                           # CC BY 4.0
└── README.md
```

---

## Documents

| Area          | Document                                                                                                   | Role / status                                                                                                         |
| ------------- | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Synthesis** | [Unified Informational-Constructive Framework](Unified%20Informational-Constructive%20Framework.md) | Archive map, cross-level synthesis, thesis statuses (v1.7) |
| Philosophy | [The Algorithm of Being](Philosophy/The%20Algorithm%20of%20Being.md) | Philosophical framework |
| Physics | [Causal-Phase Geometry Research Program v2.0](Physics/Causal_Phase_Geometry_Research_Program_v2.md) | **Active** research program under $H_P$: matrix kinematics $W_{xy}$, budget-constrained dual origin of dark-sector effects (local condensation / global decompression), explicit $\Gamma_{\rm corr}$; supersedes Aug 2026 draft |
| Physics | [Causal Phase Geometry Research Program](Physics/Causal_Phase_Geometry_Research_Program.md) | Historical predecessor of v2.0 (kept for continuity) |
| Physics | [Technical Specification v0.2](Physics/Technical_Specification_v0.2.md) | **Executable pilot** (consolidated): Mode A (frozen topology = former v0.1) + Mode B (dynamic budget-conserving rewiring); observables $\Delta F$, $\Delta N_\partial$, $\delta\rho_{\rm void}$, $z_{\rm void}^{\rm eff}$; null tests D1–D8 |
| Physics | [Technical Specification v0.1.1 — Γ_corr Extraction](Physics/Technical_Specification_v0.1.1_Gamma_corr_Extraction.md) | Historical static-lattice pilot (now the Mode A control branch of v0.2) |
| Physics | [KK–Jacobson Commutativity Note](Physics/KK_Jacobson_Commutativity_Note.md) | Technical note on the 5D→4D thermodynamic bridge (5D route frozen; historical) |
| Reasoning | [Modified Brusentsov Entailment Logic](Reasoning/Modified_Brusentsov_Entailment_Logic.md) | **Canonical formal-logical foundation**: modified Brusentsov DNF, four-valued verdict calculus (FOLLOW / OMIT / NULL / UNDECIDED), typed certificates, ensemble law quantifiers, metric/box/graph semantics; normative reference for verdict semantics across the corpus |
| Reasoning | [Spectral and Matrix Realization of V₄](Reasoning/Spectral_and_Matrix_Realization_of_V4.md) | Mathematical realization of V₄ in latent spaces: kernel-path quotients, tangent-space diagnostics, four-channel semilattice aggregation and smooth surrogates; normative parent = MBEL §§3–6; related foundations = latent information structuring + Latent Agency Framework |
| Reasoning | [Unified Implementable Model](Reasoning/Unified_Implementable_Model.md) | Theoretical architecture (verifier-centered latent world models) |
| Reasoning | [External Ternary Judge Adapter](Reasoning/External_Ternary_Judge_Adapter.md) | Technology assessment / protocol for external verification |
| Reasoning | [Self-Developing Runtime Research Program](Reasoning/Self_Developing_Runtime_Research_Program.md) | Pre-implementation research program (v0.2): controlled self-development of an LLM under an external verifier |
| Reasoning | [Latent Information Structuring](Reasoning/latent_information_structuring.md) | Geometric theory of latent representations (EN); active experimental program E1–E5 |
| Reasoning | [Latent Agency Framework](Reasoning/Latent_Agency_Framework.md) | Working hypothesis (v2.0): graded agency via integration, persistence, informational autonomy; relief vs budget; recoverability bound; nine measurable predictions; hard problem bracketed |
| Reasoning (drafts) | [Propose, Judge, Commit](Reasoning/Draft/ternary_judge.md) | Draft paper; includes preliminary live MVP results on a controlled corpus (FalseFollowRate 0.362 → 0.035) |
| Reasoning (drafts) | [Hierarchical Ternary KG as RAG Alternative](Reasoning/Draft/Hierarchical_Ternary_KG_as_RAG_Alternative.md) | Draft: ternary hierarchical knowledge graph as an alternative to RAG |
| Engineering | [ARCHITECTURAL\_SPECIFICATION](Engineering/architectural_specification_v10_9.md) | ARC-AGI-3 LCLD Agent (Version 10.9): architectural specification; verdict semantics aligned to the canonical logic specification
| Engineering | [ENGINEERING\_SPECIFICATION](Engineering/engineering_specification_v10_9.md) | ARC-AGI-3 LCLD Agent (Version 10.9): engineering specification |

### Physics/old_test

Unstructured working data from successive stages of the cosmological and astrophysical testing pipeline (scripts, plots, Cobaya reports, RAR analyses, attractor studies, etc.).
Kept for internal continuity; not catalogued as formal deliverables.

---

## Author's Note

This archive was created with the assistance of Large Language Models (LLMs). However, the models were strictly controlled, the outputs were filtered, and cross-verification was performed, culminating in my final review and approval. I fully understand that modern AI with frozen weights can hardly transcend the boundaries of existing human knowledge. Therefore, this repository captures specific points at the frontiers of the research directions that interest me, focusing on hypotheses I consider promising. While the depth of exploration varies across these different directions, I consider it sufficient to convey the overall structure of the ideas.

---

## Status disclaimer

- The physics documents **do not** claim an experimentally established replacement for general relativity or ΛCDM. They formulate a research program with explicit falsification criteria. Causal-Phase Geometry v2.0 supplies the structural hypothesis and the dual-regime identification of $\Gamma_{\rm corr}$; Technical Specification v0.2 is the first quantitative pilot of the condensation–decompression signals on a budget-conserving causal-phase graph.
- The reasoning-system and engineering documents specify research architectures and prototype evaluation plans. They **do not** establish general intelligence or universal logical correctness.
- The consciousness document is a working hypothesis. It does **not** explain why any state is experienced (the hard problem is bracketed), and its predictions are untested.
- Thesis-level statuses (FOLLOW / OMIT / NULL / UNDECIDED) are maintained in the Framework document and are attached to claims, not merely to files. Their formal semantics is fixed by [Modified Brusentsov Entailment Logic](Reasoning/Modified_Brusentsov_Entailment_Logic.md), the canonical reference for verdict semantics corpus-wide.

---

## License

All content in this repository is released under the **Creative Commons Attribution 4.0 International License** (CC BY 4.0). See [LICENSE](LICENSE).
