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

## Multiple manufacturing landscapes

- Keep `Investigations/manufacturing-orientation/investigation.json` as the canonical identity of sources, findings, questions and mechanism studies. Its `landscape_views` are goal-conditioned projections: member IDs plus alternate parents, **not duplicate copies** of evidence. Preserve stable IDs across every view.
- Differentiate actual source inspection from table-of-contents navigation. `book_landscaplets` is a retrieval map, not a collection of established results. Record exact edition and printed/PDF page scheme where known.
- Prefer substantive functional operators—force/travel transformation, motion and constraint, material transformation, support/release, geometry, joining, tolerancing and scale—over taxonomies of book titles or manufacturing brands.
- A cross-view link should answer a useful new question. Do not automatically assign every source or case to all views. Add a new view only when a distinct navigation purpose is demonstrated.
- The existing canonical IDs (for example `MFG-FUNC-COMPLIANT`) can appear in several manufacturing perspectives; user annotations and source lineage must remain attached to the one record. Inspect the actual source section and contrasting mechanism before upgrading candidate navigation to an observed claim.

## Keep it lean

- Begin with a question and a few useful nodes. Grow only when new distinctions affect research or decisions.
- Create one canonical JSON record per investigation. Optional Markdown notes should serve actual reading or explanatory needs, not duplicate the JSON.
- Use stable IDs. Prefer editing/relinking existing branches to copying them.
- Avoid rote RSM checklists, fabricated question trees, universal ontologies, auto-generated source dumps, and model-facing prose in reader-facing records.
- Link FKEN resource/domain records rather than duplicating them. Link original PDFs, Kami documents, or Drive files rather than copying binary books into Git.
- Do not conflate an open branch with an outstanding task; the goal is understanding, not maximizing node count.
- Respect GitHub version history. Never erase competing explanations or source lineage without recording why the interpretation changed.

## Minimal record convention

`investigations.json` lists `id`, `title`, `path`, `status`, and `updated` for each investigation.

A substantive investigation record should have `id`, `title`, `question`, and `nodes`. Add `sources`, `relations`, `certificates`, and `notes` as the investigation needs them. Every node uses a stable `id`; when hierarchical, a `parent_id` points to another node, or is `null` for the root.

Avoid schema churn. A useful source record has a URL or stable locator, the book/paper identity, verified chapter/page details when available, and a short statement of relevance. A useful certificate allows a reader to check what we established without trusting an ungrounded summary.
