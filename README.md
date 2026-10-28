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
├── Unified Informational-Constructive Framework.md   # synthesis & archive map (v2.0)
├── Philosophy/
│   └── The Algorithm of Being.md
├── Physics/
│   ├── Causal_Phase_Program_v4.md                    # active program (v4.0, Oct 2026)
│   ├── Technical_Specification_v0.4.md               # active executable specification (protocols V1–V7)
│   ├── KK_Jacobson_Commutativity_Note.md             # historical: 5D route frozen (Aug 2026)
│   └── old_test/                                     # historical working data (see below)
├── Reasoning/
│   ├── Modified_Brusentsov_Entailment_Logic.md       # canonical formal-logical foundation (verdict semantics)
│   ├── Spectral_and_Matrix_Realization_of_V4.md      # geometric/matrix realization of V4 in latent spaces
│   ├── Unified_Implementable_Model.md
│   ├── External_Ternary_Judge_Adapter.md
│   ├── Self_Developing_Runtime_Research_Program.md
│   ├── Latent_Information_Structuring.md             # geometry of latent representations (EN)
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
| **Synthesis** | [Unified Informational-Constructive Framework](Unified%20Informational-Constructive%20Framework.md) | Archive map, cross-level synthesis, thesis statuses (v2.0) |
| Philosophy | [The Algorithm of Being](Philosophy/The%20Algorithm%20of%20Being.md) | Philosophical framework |
| Physics | [Causal Phase Program v4.0](Physics/Causal_Phase_Program_v4.md) | **Active** formal specification and research program: unified Gaussian model $\Pi = m^2 I + L_\Theta$ on the Hasse graph, hard locality constraints (L0)–(L4) with the Kleitman–Rothschild impossibility theorem, diamond-participation multiplicity $d_\diamond$, exact entropy balance (Theorem 4.3, Landauer reading separated as Hypothesis H-L), exact field back-reaction (Woodbury edge-swap law, loop expansion, triadic Schur decomposition), hypercube counterexample (the “3+1” derivation is retracted, NULL); protocols V1–V7 with $V_4$ registry and reference implementation; §10 records the executed identity-level checks; supersedes v3.9 (removed) |
| Physics | [Technical Specification v0.4](Physics/Technical_Specification_v0.4.md) | **Active** executable specification of protocols V1–V7: Phase 0 self-test gate, ensemble movers M1/M2/M3, exact-Woodbury equilibrium sampler, pre-registered topology classifier (V5), three inclusion region classes (V6), execution plan ≈20–32 h, $V_4$ decision rules per MBEL, automated `REPORT_v0.4.md`; predecessors v0.2 (executed → UNDECIDED) and v0.3 (superseded before execution) are removed |
| Physics | [KK–Jacobson Commutativity Note](Physics/KK_Jacobson_Commutativity_Note.md) | Technical note on the 5D→4D thermodynamic bridge (5D route frozen; historical) |
| Reasoning | [Modified Brusentsov Entailment Logic](Reasoning/Modified_Brusentsov_Entailment_Logic.md) | **Canonical formal-logical foundation**: modified Brusentsov DNF, four-valued verdict calculus (FOLLOW / OMIT / NULL / UNDECIDED), typed certificates, ensemble law quantifiers, metric/box/graph semantics; normative reference for verdict semantics across the corpus |
| Reasoning | [Spectral and Matrix Realization of V₄](Reasoning/Spectral_and_Matrix_Realization_of_V4.md) | Mathematical realization of V₄ in latent spaces: kernel-path quotients, tangent-space diagnostics, four-channel semilattice aggregation and smooth surrogates; normative parent = MBEL §§3–6; related foundations = latent information structuring + Latent Agency Framework |
| Reasoning | [Unified Implementable Model](Reasoning/Unified_Implementable_Model.md) | Theoretical architecture (verifier-centered latent world models) |
| Reasoning | [External Ternary Judge Adapter](Reasoning/External_Ternary_Judge_Adapter.md) | Technology assessment / protocol for external verification |
| Reasoning | [Self-Developing Runtime Research Program](Reasoning/Self_Developing_Runtime_Research_Program.md) | Pre-implementation research program (v0.2): controlled self-development of an LLM under an external verifier |
| Reasoning | [Latent Information Structuring](Reasoning/Latent_Information_Structuring.md) | Geometric theory of latent representations (EN); active experimental program E1–E5 |
| Reasoning | [Latent Agency Framework](Reasoning/Latent_Agency_Framework.md) | Working hypothesis (v2.1): graded agency via integration, persistence, informational autonomy; relief vs budget; recoverability bound and kernel-inclusion synchronization; Helmholtz decomposition and integrator-chain truncation of boundary dynamics; ten measurable predictions; hard problem bracketed |
| Reasoning (drafts) | [Propose, Judge, Commit](Reasoning/Draft/ternary_judge.md) | Draft paper; includes preliminary live MVP results on a controlled corpus (FalseFollowRate 0.362 → 0.035) |
| Reasoning (drafts) | [Hierarchical Ternary KG as RAG Alternative](Reasoning/Draft/Hierarchical_Ternary_KG_as_RAG_Alternative.md) | Draft: ternary hierarchical knowledge graph as an alternative to RAG |
| Engineering | [ARCHITECTURAL\_SPECIFICATION](Engineering/architectural_specification_v10_9.md) | ARC-AGI-3 LCLD Agent (Version 10.9): architectural specification; verdict semantics aligned to the canonical logic specification
| Engineering | [ENGINEERING\_SPECIFICATION](Engineering/engineering_specification_v10_9.md) | ARC-AGI-3 LCLD Agent (Version 10.9): engineering specification |

### Physics/old_test

Unstructured working data from successive stages of the cosmological and astrophysical testing pipeline (scripts, plots, Cobaya reports, RAR analyses, attractor studies, etc.).
Historical; kept for internal continuity; not catalogued as formal deliverables.

---

## Author's Note

This archive was created with the assistance of Large Language Models (LLMs). However, the models were strictly controlled, the outputs were filtered, and cross-verification was performed, culminating in my final review and approval. I fully understand that modern AI with frozen weights can hardly transcend the boundaries of existing human knowledge. Therefore, this repository captures specific points at the frontiers of the research directions that interest me, focusing on hypotheses I consider promising. While the depth of exploration varies across these different directions, I consider it sufficient to convey the overall structure of the ideas.

---

## Status disclaimer

- The physics documents **do not** claim an experimentally established replacement for general relativity or ΛCDM. They formulate a research program with explicit falsification criteria. Causal Phase Program v4.0 supplies the structural hypothesis, the $V_4$-classified mathematical core, and the computational protocols V1–V7; its identity-level checks are executed and recorded in §10, but no physical hypothesis has been tested: protocols V1–V7 have not been run under Technical Specification v0.4 yet. The continuum layer — Einstein-type equations, dark-sector decompositions, horizon phases — is explicitly OMIT from the program (Registry row 17); observational contact (SPARC, DESI/DES-SN5YR) is outside its current scope. The historical predecessor v0.2 was executed and returned UNDECIDED (glassy freezing; finite-size ambiguity).
- The reasoning-system and engineering documents specify research architectures and prototype evaluation plans. They **do not** establish general intelligence or universal logical correctness.
- The consciousness document is a working hypothesis. It does **not** explain why any state is experienced (the hard problem is bracketed), and its predictions are untested.
- Thesis-level statuses (FOLLOW / OMIT / NULL / UNDECIDED) are maintained in the Framework document and are attached to claims, not merely to files. Their formal semantics is fixed by [Modified Brusentsov Entailment Logic](Reasoning/Modified_Brusentsov_Entailment_Logic.md), the canonical reference for verdict semantics corpus-wide.

---

## License

All content in this repository is released under the **Creative Commons Attribution 4.0 International License** (CC BY 4.0). See [LICENSE](LICENSE).
