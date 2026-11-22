# Working with the RSM investigation tree

## Governing writing standard (verbatim from ChatGPT.md)

Be high density and not filler with your words. Should be in such a way that will maximally activate my neurons

Apply this to reader-facing questions, case studies, explanations, source notes, comparisons, and viewer presentation. Prefer consequential mechanisms, real observations, failure-to-intervention sequences, and transferable insight over lists of abstract labels. Do not artificially lengthen unsupported cases; record missing evidence explicitly. Keep authoring instructions outside user-visible descriptions.

This repository is persistent state for research across chats, not an instruction to turn every conversation into an elaborate report. Follow the [Richer Scientific Method](https://github.com/JadanPoll/Learning_Visualizations_Taxonomy/blob/main/Navigationals/The_Richer_Scientific_Method.md) selectively, especially RSM-01, RSM-02, RSM-04, RSM-05, and RSM-08.

## Persistent navigation acceptance criterion (verbatim FKEN-16A)

Source: [FKEN — Frustration-to-resource traversability](https://github.com/JadanPoll/Learning_Visualizations_Taxonomy/blob/main/Navigationals/Fractal_Knowledge_And_Ecosystem_Navigation.md#fken-16a--frustration-to-resource-traversability). This is the actual test of whether a question landscape helps people find and use the books, not merely a taxonomy-coverage requirement.

### FKEN-16A — Frustration-to-resource traversability

**FKEN-16A.1 — Empirical goal.** An investigator should be able to begin with an authentic frustration, naive question, or intended accomplishment—without knowing the relevant author's vocabulary, book title, or source chapter—and navigate to consequentially relevant resources. In a bounded book collection, ask whether its genuinely useful passages can be reached through the available questions, sets/supersets, domainlets, and landscaplets, instead of requiring the investigator to already know where to look.

**FKEN-16A.2 — Traversable intermediate choices.** At successive points of a question tree or activated landscape, the next branching choices should express meaningful distinctions that help orient the investigator: alternative mechanisms, functional requirements, constraints, failure modes, and broader question families. A relevant resource may appear in multiple pathways while retaining one canonical identity. A globally reachable catalog link is not evidence of useful *navigation*; the path itself should explain why the destination matters.

**FKEN-16A.3 — Reachable endpoint.** Success is not merely encountering a book or a vaguely related heading. It is discovering a relevant, recoverable passage, worked implementation, person, or experiment with sufficient source location and explanation to decide whether to study or use it. Distinguish source relevance, evidenced applicability, and actual competence acquired through use.

**FKEN-16A.4 — Two-sided coverage audit.** Sample (a) real frustrations and questions independently of the resource classifications, and (b) consequential source regions identified independently from the navigator. For each source region, construct plausible tasks that would make it useful, without supplying the source's own title or key terminology. Trace whether the interface can lead to it from plausible entry points. Audit both what questions retrieve and which valuable passages are never surfaced; a high link count alone establishes neither.

**FKEN-16A.5 — Practical measurement.** On representative unfamiliar-user tasks, record whether an actually useful resource was reached, the relevance of the first candidates, wrong turns, backtracking, time or interaction cost, dependence on exact terminology, and whether the final source anchor can be opened. Compare with simple baselines such as full-text search, the book's table of contents, or direct expert guidance. Track misses and false positives separately; the best structure may vary by question.

**FKEN-16A.6 — Limits and revision.** Do not demand that every node directly lead to every resource, or that all book passages have equal value. Scope the audit to the collection, meaningful resource regions, and intended question families. When a genuinely relevant resource is difficult to reach, investigate the obstruction: missing source coverage, missing everyday-language entry, misleading grouping, absent cross-branch relationship, or poor interface. Improve the smallest consequential bridge, landscaplet, or question family before multiplying permanent trees or generic links. Re-run representative routes after revisions.

*Manufacturing example:* A user frustrated that a printed latch keeps breaking should be able to encounter alternative material/load-direction explanations (FFM anisotropy), elastic mechanism design (compliant flexures), cyclic failure analysis (fatigue), and different fabrication or joining approaches, with appropriately qualified links to the relevant chapters—not need to know any of those names in advance.

## When an investigation resumes

1. Read `investigations.json` and the relevant `Investigations/<slug>/investigation.json` before proposing changes.
2. Recover the user's actual question, parent purpose, existing branches, prior evidence, unresolved alternatives, and why the latest stopping point mattered.
3. Continue from that state. Don't restart, duplicate branches, invent achievements, or silently rewrite the user's aims.
4. Search for actual source material and chapter-level treatments that could change the investigation. Prefer books already in the user's connected library when useful; consider outside literature as well.
5. Commit only meaningful state changes, and report which nodes and evidence changed. Read the latest version before updating so changes from another chat are not overwritten.

## What to preserve

- The user's original wording when it matters, distinct from clarified formulations.
- The question's parent purpose, live competing explanations, relevant constraints, and the reason each consequential branch exists.
- Stable node IDs and explicit links for relationships that cannot be expressed by parent-child containment (`depends_on`, `supports`, `challenges`, `shares_mechanism`, etc.).
- Source references precise enough to check: author/title/edition, chapter/section, printed or PDF page numbers when verified, direct file or publication link, and what the source contributes.
- Evidence separate from model interpretation; hypotheses remain hypotheses. For books not inspected, mark chapters/pages as unverified candidates rather than inventing exact locations.
- Compact certificates: conclusion or obstruction, first-hand evidence, assumptions, uncertainty, and what would justify reopening.

## Each domain: one research corpus, question- or set-scoped investigation

The manufacturing, operating-systems, and human–AI domains each use a single `Investigations/<slug>/investigation.json`. Do not reintroduce separate `question_tree.json`, `reference_guide.json`, or `fieldwork.json` files just because an investigation has multiple entry questions, sources, evidence types, or presentation views. The canonical domain file preserves `curiosity_atlas`, `navigation_bridges`, `landscape_views`, `nodes`, and `sources`; supplementary `question_nodes`, `fieldwork_nodes`, and `routes` remain sections of that same file when they offer distinct information. The `rsm-view.json` manifest may define multiple display projections over one source file without duplicating research.

Do not confuse `question_nodes` (historical question-index entries and candidate reading paths) with `nodes` (canonical technical investigation records), and do not treat `fieldwork_nodes` as independently validated conclusions. Old JSONs remain recoverable in Git history but are not active files. Update only the relevant section of the canonical file while preserving stable IDs and source anchors.

## Manufacturing: one research corpus, question- or set-scoped investigation

An **investigation** is a purposeful exploration of one question or a set of related questions, including relevant mechanisms, evidence, open alternatives and source locations. It is not a different kind of tree or a separate JSON by default. Questions and question sets both enter the same technical research corpus.

- **Canonical knowledge:** `Investigations/manufacturing-orientation/investigation.json` holds all manufacturing technical `nodes`, `connections`, book `sources`, and `book_landscaplets` (65 chapter/part locators). Research is written once with stable IDs, evidence status, and printed/PDF page distinctions.
- **Entry:** `curiosity_atlas.entries` has simple questions and search aliases. `navigation_bridges` defines substantive, conditional mechanism options and cited source sections. Similar wording need not mean the same explanation: repeatedly bent **metal wire** and a broken **3D-printed polymer clip** must remain distinguishable.
- **Sets:** `landscape_views` defines existing larger investigations as sets of question IDs and their purpose-dependent parent relationships. Render these alongside individual questions in the same browse interface. Neither kind of entry duplicates technical evidence or requires another investigation JSON.
- **Projection:** A selected entry activates a dense technical subgraph that can contain existing study IDs and source citations. Keep ordinary-language wording at the entrance; avoid diluting technical explanations and evidence with repeated beginner-facing prompts.
- **Provenance:** Distinguish `source_section_inspected` from chapter-only candidates. Source IDs and reader notes must remain stable across every projection. Archived `MFG-ISSUE-*` IDs are retained for historical note compatibility, not displayed as current technical nodes.
- **Subtraction rule:** Prefer fewer user-facing paths to the same purpose. Do not revive the former root-level **Problems** menu, replicate the entire book catalog at every tree root, or introduce a separate “question tree versus investigation tree” workflow. Use contextual source routes and one questions/sets browser.
- **Empirical acceptance:** Apply FKEN-16A using real unfamiliar questions and independently sampled meaningful passages. Static node/link checks are not proof of discoverability. Fix failed navigation with the smallest useful change rather than inflating taxonomies.

## Keep it lean

- Begin with a question and a few useful nodes. Grow only when new distinctions affect research or decisions.
- Keep research evidence canonical within its domain/corpus. Create a new JSON only when a distinct source, data lifecycle, or tooling boundary earns it; questions and investigation sets are projections, not automatic files.
- Use stable IDs. Prefer editing/relinking existing branches to copying them.
- Avoid rote RSM checklists, fabricated question trees, universal ontologies, auto-generated source dumps, and model-facing prose in reader-facing records.
- Link FKEN resource/domain records rather than duplicating them. Link original PDFs, Kami documents, or Drive files rather than copying binary books into Git.
- Do not conflate an open branch with an outstanding task; the goal is understanding, not maximizing node count.
- Respect GitHub version history. Never erase competing explanations or source lineage without recording why the interpretation changed.

## Minimal record convention

`investigations.json` lists `id`, `title`, `path`, `status`, and `updated` for each investigation.

A canonical research-corpus record should have an identity, substantive questions or nodes, and provenance appropriate to what has actually been investigated. Add `sources`, `relations`, `certificates`, and `notes` as the investigation needs them. Every node uses a stable `id`; when hierarchical, a `parent_id` points to another node, or is `null` for the root.

Avoid schema churn. A useful source record has a URL or stable locator, the book/paper identity, verified chapter/page details when available, and a short statement of relevance. A useful certificate allows a reader to check what we established without trusting an ungrounded summary.
