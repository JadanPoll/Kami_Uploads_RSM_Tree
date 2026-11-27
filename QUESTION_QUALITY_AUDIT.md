# Cross-domain question quality audit — 2026-11-24

This is an **evidence-sensitive sample**, not a global quality score. Run `python3 scripts/question_audit.py --strict` for the complete **structural** question-type census. The original 281-entry census excluded the 43 OS and 56 human–AI question-index nodes and technical study questions; never merge those populations without a separate denominator.

## Representative traversals

| Entry | What the current route actually offers | Remaining test / obstruction |
| --- | --- | --- |
| `ROB-CURI-kidnapped` — relocated robot | Its `ESTIMATION` bridge distinguishes observation ambiguity from lost localization and explicitly cites *Probabilistic Robotics* §8.3.5, “Random Particle MCL: Recovery from Failures.” | Strong **source-location candidate**; test unfamiliar-user recognition, actual opening of the edition's page, and usefulness of its procedure. |
| `MFG-CURI-printed-clip` — broken 3D-printed clip | `SNAP` separates layer failure, excessive flexure strain, and fatigue, pointing to different technical nodes and books. | Test whether a real failure scenario selects the right alternative and reaches a source passage, not just a book label. |
| `OS-CAP-page-translation` — page-table walk | The `OS-BRG-memory` bridge includes both “Addresses appear identical across processes” and “Memory is exhausted or slow”; both touch `OS-03`, so target filtering can surface the latter for a page-translation exercise. | **Semantic route mismatch risk.** Add a dedicated page-walk route or more specific bridge-choice filtering; verify against an actual Sv39 translation example rather than accepting shared node IDs. |
| `MATH-CAP-row-reduction` — Gaussian elimination | The `LINEAR` bridge routes through broad coordinate-change/vector-space material, with references to Halmos and Artin, but does not itself identify a worked echelon-form exercise. | **Source specificity unresolved.** Find the exact worked passage/problem and demonstrate from question to result. |
| `HAI-CURI-verify` — spectacular AI claim | `HAI-BRG-trust` and `HAI-BRG-demystify` reference substantive technical investigations; their bridge choices do not carry specific `section_targets`. | Test the complete route from claim to original result, reproduction and limits; a success criterion is not a verification already performed. |
| `NMR-CURI-better` — neuromorphic hardware advantage | `VALIDATE` points toward system validation and historical Mead (1989) / Liu (2015) source regions. | **Comparative evidence gap.** A contemporary benchmark with workload, accuracy, energy, latency and system-level overhead is required to establish present-day superiority. |

## Interpretation

- A resolved `bridge_id` means a reference is structurally valid, **not** that the bridge is a relevant explanation, sufficiently narrow retrieval route, or test of competence.
- An `execution`, `verification` or `empirical_investigation` label describes **what the question requests**, not what the reader or connected sources can demonstrably do.
- Domain distributions are affected by **sampling frames**. Mathematics has a deliberately expanded collection of canonical operational capability families; the other fields have far fewer. Equalizing shares without authentic tasks would make the atlas worse.
- Test quality by a representative independent goal/problem **and** reverse-sampled important passages (FKEN-16A). Record false positives, missed alternatives, source-opening failures, and actual task outcomes. Prefer the smallest correction to an already canonical route.

## Next useful discrimination

Choose a small number of authentic **non-mathematics execution tasks**—for example one UART receiver, a page-table walk, a tolerance stack, and a state-estimation update. For each: supply one representative real input, reach the source or implementation from ordinary question wording, perform the operation, compare with an independent oracle or working artifact, and record the first navigation or competence failure. This tests whether the current apparent mathematical capability imbalance is merely a difference in entry-question wording or a real omission in the practical skill landscape.

## Operational revision — 2026-11-27

Source standard: [OPERATIONAL.md](https://github.com/JadanPoll/FKEN_REA_CaseStudies/blob/main/OPERATIONAL.md). The eight canonical entry atlases were reviewed as prospective books. All original 281 entry questions were considered; 243 formulations were revised, 47 chapter-level families now expose the major territories, two duplicate mathematical capability entries were consolidated, and four independent missing dimensions were added. There are now **283 canonical entries** and 60 capability-family contracts. The initial pass incorrectly moved original concrete formulations to aliases. The calibration correction below restores those formulations as visible questions. Existing source-backed studies, larger investigation sets, stable glossary identities and question types were retained; the 99 separate question-index nodes and underlying technical questions were not comprehensively rewritten.

| Domain | Distinct territory made more visible | Remaining inverse/forward coverage concern |
| --- | --- | --- |
| Manufacturing | Material behavior, accuracy, mechanical transformations, process feasibility, production; added reliable joining | Broader process selection and surface/quality inspection deserve reverse sampling from the five book catalogs. |
| Operating systems | Split runtime, virtual memory/protection, devices, bootstrapping, persistence and distributed systems; added concurrent-state correctness | Compare IPC, synchronization, file-system implementation and architecture-specific translation against independently selected chapters. |
| Human–AI | Separated claim reliability, learning, continuity, agency, coordination and exceptional work; added population measurement | Usage distributions are not capability distributions; independent comparative outcome data remains necessary. |
| Digital hardware | Distinguish implementation interfaces, RTL/state, timing, physical silicon and architecture selection | Reverse-sample arithmetic/datapath design, memory interfaces and physical design; the existing technical coverage does not establish practical operator coverage. |
| Neuromorphic engineering | Analog operations, perception, spikes, learning and system integration; linked optical-motion computation directly | The optical-motion chapter is a TOC lead; circuit reconstruction and contemporary benchmark evidence remain open. |
| Electronics | Separate analog design, failure mechanisms, instrumentation, interconnect, power and realization | Reverse-sample component selection, stability and power magnetics for checkable task coverage, without duplicating diagnosis entries. |
| Robotics | Separate embodiment, geometric reachability, belief, planning, dynamics, flight, decisions and validation; added inverse dynamics | Existing books do not establish coverage of modern soft, legged or learning-based robotics; verify representative real-world navigation and actuation tasks. |
| Mathematics | Preserve actual mathematical operator families; consolidate inclusion–exclusion and Möbius inversion duplicates; move residue calculation to complex analysis | Remaining conceptual/execution pairs must be judged by their independent demand, and reverse sampling must test the fourteen-book coverage. |

### Forward-route repairs

- Page-table translation now uses `OS-BRG-page-walk`, directly linking OSTEP chapters 18 and 20 rather than the memory-exhaustion branch. Round-robin scheduling has its own queue-tracing bridge to chapter 7. Chapter anchors are existing TOC-level evidence, not completed exercises.
- Gaussian elimination and solving linear systems use `LINEAR-SYSTEMS`, with the previously indexed Artin §1.2 **Row Reduction** and Halmos §50 rank/nullity. The exact Artin page and a worked problem remain unverified.
- Neuromorphic visual motion now directly reaches `NMR-MOTION` and Mead chapter 14 (printed p. 229; TOC-level lead).
- Mechanical joining reaches `MFG-JOINING`, the FFM joinery chapter and Shigley's joint chapters; robot inverse dynamics reaches the previously inspected Modern Robotics §8.3.2. The new human–AI measurement question retains the population fieldwork routes and candidate primary sources.

This is a semantic review and structural repair pass, not an independent inspection of every book passage. Do not interpret the revised number of questions or chapter labels as proof of authoritative coverage. The unresolved work is two-sided sampling of actual source regions and representative real goals, with observed navigation and task outcomes.

### Negative calibration correction — question wording

The user updated [OPERATIONAL.md](https://github.com/JadanPoll/FKEN_REA_CaseStudies/blob/main/OPERATIONAL.md#negative-calibration-case--generalizing-away-the-curiosity-and-natural-application) specifically in response to the above rewrite. The previous pass confused abstraction of the intellectual territory with abstraction of its entry language. It reduced curiosity, mentally manipulable situations, and recognition of problems in practice. The 243 rewritten titles have been rolled back across the eight domains, with the two consolidated mathematical entries using the original natural-language curiosity as their visible title and retaining the exact capability contract and redirects. Original family headings and descriptions have been restored except for OS, where the six genuinely distinct territories remain organized under readable question headings. The four new entries, source-route fixes, IDs, glossary links, classifications, and removal of repetitive context boilerplate remain. This is a targeted rollback, not a repository-wide revert. No claim is made that the four new entries or all remaining questions pass the inverse criterion; do not rewrite them wholesale to satisfy a taxonomy.

Future audits must distinguish the marginal intellectual contribution of a sibling from the natural recognition value of its phrasing. The relevant regression test is a human browsing without the technical vocabulary, and a human later recognizing an opportunity in the real world, not merely a successful LLM classification or a valid reference graph.
