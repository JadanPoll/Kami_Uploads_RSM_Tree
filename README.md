# Kami Uploads — Research Navigator

Explore what you are curious about, follow the underlying mechanisms, and recover the relevant parts of real books. This repository preserves **questions, evidence, technical investigations, source locations, and links** across conversations; original books stay in Drive/Kami.

[**Open the manufacturing questions and investigations**](https://raw.githack.com/JadanPoll/Learning_Visualizations_Taxonomy/main/RSM_Tree_Viewer.html?repo=https%3A%2F%2Fgithub.com%2FJadanPoll%2FKami_Uploads_RSM_Tree&view=manufacturing-curiosities)

[**Explore neuromorphic engineering**](https://raw.githack.com/JadanPoll/Learning_Visualizations_Taxonomy/main/RSM_Tree_Viewer.html?repo=https%3A%2F%2Fgithub.com%2FJadanPoll%2FKami_Uploads_RSM_Tree&view=neuromorphic-curiosities)

[**Explore FPGA and VLSI questions**](https://raw.githack.com/JadanPoll/Learning_Visualizations_Taxonomy/main/RSM_Tree_Viewer.html?repo=https%3A%2F%2Fgithub.com%2FJadanPoll%2FKami_Uploads_RSM_Tree&view=digital-hardware-curiosities)

[**Explore electronics engineering**](https://raw.githack.com/JadanPoll/Learning_Visualizations_Taxonomy/main/RSM_Tree_Viewer.html?repo=https%3A%2F%2Fgithub.com%2FJadanPoll%2FKami_Uploads_RSM_Tree&view=electronics-curiosities)

[**Explore robotics — from a curious question to physical mechanisms and source passages**](https://raw.githack.com/JadanPoll/Learning_Visualizations_Taxonomy/main/RSM_Tree_Viewer.html?repo=https%3A%2F%2Fgithub.com%2FJadanPoll%2FKami_Uploads_RSM_Tree&view=robotics-curiosities)

[**Explore mathematics — operational capabilities, proofs and fourteen connected textbooks**](https://raw.githack.com/JadanPoll/Learning_Visualizations_Taxonomy/main/RSM_Tree_Viewer.html?repo=https%3A%2F%2Fgithub.com%2FJadanPoll%2FKami_Uploads_RSM_Tree&view=mathematics-curiosities)

## Two complementary question layers

[**Question types and task specificity**](QUESTION_TYPES.md) distinguish explanatory inquiry, task decomposition and genuine operational execution. A broad "How would I build an RC car?" legitimately asks for problem decomposition; "Can I perform Gaussian elimination?" asks whether a known mathematical operation can be carried out on suitable inputs, without inventing a matrix for every entry. Each type supports different learning and navigation goals. The canonical entry atlas now tags **all 281 curiosity questions across eight domains** (85 Mathematics; 196 across seven other fields). This census is limited to `curiosity_atlas.entries`: the 43 OS and 56 human–AI `question_nodes`, as well as technical studies and their subquestions, are distinct navigation layers and must not be silently mixed into the entry-question distribution. Run [`scripts/question_audit.py`](scripts/question_audit.py) to recalculate the cross-domain counts and check structural references. Type totals diagnose omissions, but do not certify navigability or practical competence. The viewer exposes question-type filters and success criteria for operational questions. Reviewed entries carry `question_type` and `task_scope`; defined capabilities may include checkable `success_criterion` and links to canonical technical studies. Counts are diagnostics for underrepresented abilities, not a reason to generate filler.

## One entrance, variable investigation scope

The manufacturing browser supports two entry sizes in one place:

- **One ordinary question**, such as “Why does my metal paper clip snap?” Its technical projection distinguishes cyclic plastic deformation, static fracture, and alternatives for designing flexible parts.
- **A larger question set**, such as “How can I make an unfamiliar functional thing?” Its technical projection spans manufacturing possibilities, functional requirements, mechanisms, assembly, tolerances, and practical verification.

An *investigation* is the purposeful exploration of one question **or a set of questions**, with evolving evidence and unresolved alternatives—not a separate file type or an independently copied tree. Both entry sizes traverse the **same technical records**. Change the question or scope; do not clone the books.

The technical explanations remain detailed and source-specific even when the entry question is childlike. The five larger sets—**Possibilities**, **Make it**, **Mechanisms**, **Production**, and **Bootstrap**—remain available through the same entry browser, not a separate manufacturing menu.

## Search by curiosity or technical vocabulary

Each investigation also has a [**separate, lightweight concept glossary**](GLOSSARY_SCHEMA.md): stable term IDs, synonyms and explicit relationships without copied technical explanations. A curiosity, technical study, question set, bridge or fieldwork case can reference the same concept by `term_ids`, so searching for **metastability** can find “Why can two individually working circuits fail when connected?” without forcing the word into the beginner-friendly question.

The Knowledge Atlas viewer loads only the selected domain's glossary. In the question browser, choose **Questions** for ranked concept-aware search or **Vocabulary** to browse unfamiliar terms, aliases, related concepts, and linked research. Selected technical records also expose concept chips. The viewer still works with ordinary text when a glossary is absent.

| Domain | Vocabulary index |
| --- | --- |
| Manufacturing | [glossary.json](Investigations/manufacturing-orientation/glossary.json) |
| Operating systems | [glossary.json](Investigations/operating-systems/glossary.json) |
| Human–AI collaboration | [glossary.json](Investigations/human-ai-symbiosis/glossary.json) |
| FPGA and VLSI | [glossary.json](Investigations/digital-hardware-design/glossary.json) |
| Neuromorphic engineering | [glossary.json](Investigations/neuromorphic-engineering/glossary.json) |
| Electronics engineering | [glossary.json](Investigations/electronics-engineering/glossary.json) |
| Robotics | [glossary.json](Investigations/robotics/glossary.json) |
| Mathematics | [glossary.json](Investigations/mathematics/glossary.json) |

**Research remains canonical in `investigation.json`.** Vocabulary changes need not duplicate its mechanisms or books. IDs are permanent: change a label or add aliases without changing identity, and keep redirects when combining true synonyms. A related concept does not mean the same mechanism.

## Canonical domain data, without redundant JSONs

Most domains have **one canonical research JSON** (and multiple possible scoped views); mathematics composes five family-owned files into a unified atlas:

| Domain | Canonical research file | Contains |
| --- | --- | --- |
| Manufacturing | [`investigation.json`](Investigations/manufacturing-orientation/investigation.json) | Questions, technical nodes, source sections, and manufacturing operators |
| Operating systems | [`investigation.json`](Investigations/operating-systems/investigation.json) | 15 curiosity entries, 43 question-index nodes, 9 technical nodes, 51 OSTEP chapter anchors, and cross-book routes |
| Human–AI collaboration | [`investigation.json`](Investigations/human-ai-symbiosis/investigation.json) | 18 curiosities, 56 question-index nodes, 13 technical nodes, 19 fieldwork nodes, supporting sources, projects, and communities |
| Digital hardware (FPGA/VLSI) | [`investigation.json`](Investigations/digital-hardware-design/investigation.json) | 24 curiosities, five larger sets, 15 technical nodes, 18 FPGA + 9 VLSI chapter locations, and conditional source routes |
| Neuromorphic engineering | [`investigation.json`](Investigations/neuromorphic-engineering/investigation.json) | 28 curiosity entries, 20 technical records, 12 conditional bridges, five investigation sets, two books, and their reusable source maps |
| Robotics | [`investigation.json`](Investigations/robotics/investigation.json) | Three books, 43 chapters, 458 indexed subsection starts, 41 curiosities, 30 technical nodes, eight larger landscapes, nine cross-book compositions and an embodiment matrix |
| Electronics engineering | [`investigation.json`](Investigations/electronics-engineering/investigation.json) | 34 curiosity entries, 31 technical nodes, 12 conditional bridges, 50 chapter maps and 1,133 subsection locators across three electronics books |

The manufacturing corpus's principal sections are:

| Section | Responsibility |
| --- | --- |
| `curiosity_atlas` | Searchable, ordinary-language entry questions and aliases |
| `landscape_views` | Larger question sets and purpose-conditioned parent relationships |
| `navigation_bridges` | Conditional technical explanations and which passages support investigating them |
| `nodes`, `connections` | Canonical technical questions, observations, mechanisms, experiments and relationships |
| `sources`, `book_landscaplets` | Book identities and bounded chapter/section retrieval locations |
| `book_factorization` | Reusable manufacturing operators and cross-book synthesis |

[`rsm-view.json`](rsm-view.json) is a small **viewer mapping manifest**, not another knowledge database. OS chapter guidance is inside the OS investigation file; human–AI fieldwork is inside the human–AI investigation file. The different question, technical, and fieldwork presentations reference sections within the same domain corpus.

The current manufacturing collection contains **5 connected books**, **65 chapter/part retrieval locations**, **24 ordinary-language question entries**, **5 larger investigation scopes**, and **10 source-inspected technical studies**. These numbers describe the present index, **not** full passage coverage or proven practical navigation.

## Acceptance test: frustration → useful source

Follow [FKEN-16A — Frustration-to-resource traversability](AGENTS.md#fken-16a--frustration-to-resource-traversability). Start from an unfamiliar real frustration without giving away book vocabulary. The user should be able to recognize the next relevant distinction, reach an actual page or worked example, and explain why it helps.

Run the **reverse test** from independently chosen important passages: can plausible everyday questions lead to them? Compare with a book's table of contents and ordinary full-text search. Counts of nodes, branches, or chapter links do not establish discoverability.

[Robotics book reference guide — three books, reusable capabilities, exact printed-page locators, working-case routes](Investigations/robotics/REFERENCE_GUIDE.md)

[Manufacturing book reference guide — all five books, 65 indexed chapters/parts, inspected passages, and quick retrieval routes](Investigations/manufacturing-orientation/REFERENCE_GUIDE.md)

[Operating systems reference guide — OS, Linux, bare-metal and architecture book maps](Investigations/operating-systems/REFERENCE_GUIDE.md)

[FPGA and VLSI reference guide — 2 books, 27 reusable chapter anchors and practical mechanism routes](Investigations/digital-hardware-design/REFERENCE_GUIDE.md)

[Neuromorphic reference guide — 33 book chapters, four Mead appendices, 52 selected subsection starts and inspected mechanisms](Investigations/neuromorphic-engineering/REFERENCE_GUIDE.md)
[Electronics reference guide — three books, 50 chapters, 1,133 section locators and failure-to-passage routes](Investigations/electronics-engineering/REFERENCE_GUIDE.md)

[Manufacturing navigation audit and test prompts](Investigations/manufacturing-orientation/navigation_audit.md)

## Continuing and contributing

1. Start with a genuine curiosity or purpose. Choose one question or the broader set it belongs to.
2. Examine the technical alternatives; follow source citations. Clearly distinguish inspected technical evidence from suggested reading.
3. Record what an experiment, worked example, or source really established and what remains uncertain.
4. Preserve stable question, study, and source IDs across views so notes, links, and earlier research remain useful.
5. When navigation fails, correct the smallest consequential entry, mechanism distinction, source anchor, or relation. Don't create a new JSON or menu just because the existing one is awkward.

A [cross-domain question quality audit](QUESTION_QUALITY_AUDIT.md) compares representative navigation routes, including promising source-specific cases and semantic misroutes that classification counts cannot reveal.\n\nThe [Richer Scientific Method](https://github.com/JadanPoll/Learning_Visualizations_Taxonomy/blob/main/Navigationals/The_Richer_Scientific_Method.md) guides investigation, and the [Richer Engineering Method](https://github.com/JadanPoll/Learning_Visualizations_Taxonomy/blob/main/Navigationals/The_Richer_Engineering_Method.md) guides practical functionality, testing, and subtraction. [`AGENTS.md`](AGENTS.md) carries persistent continuation instructions.

The objective is a navigator worth returning to after a month: **ask what you actually care about, encounter the relevant depth, and recover the evidence without rediscovering the organization**.


**Mathematics collection:** [unified investigation](Investigations/mathematics/investigation.json), [five canonical research families](Investigations/mathematics/REFERENCE_GUIDE.md#research-families--canonical-ownership), [139 active vocabulary concepts](Investigations/mathematics/glossary.json), [693 optional unlinked vocabulary candidates](Investigations/mathematics/vocabulary_candidates.json), and [fourteen-book navigator](Investigations/mathematics/REFERENCE_GUIDE.md). The five families own 14 book catalogs and 37 studies; the atlas owns two shared studies, 46 curiosities, nine question landscapes and twelve cross-book compositions. The viewer assembles the actual files, without duplicate root records.
