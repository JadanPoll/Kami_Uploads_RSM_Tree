# Working with the RSM investigation tree

This repository is persistent state for research across chats, not an instruction to turn every conversation into an elaborate report. Follow the [Richer Scientific Method](https://github.com/JadanPoll/Learning_Visualizations_Taxonomy/blob/main/Navigationals/The_Richer_Scientific_Method.md) selectively, especially RSM-01, RSM-02, RSM-04, RSM-05, and RSM-08.

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
