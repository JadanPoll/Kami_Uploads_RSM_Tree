# Kami Uploads — RSM Investigation Tree

A persistent home for investigations across ChatGPT conversations. Start with a question, discover its larger purpose and neighboring possibilities, find the relevant books and chapters, and preserve what reading, experiments, and discussion actually establish.

The repository follows the [Richer Scientific Method (RSM)](https://github.com/JadanPoll/Learning_Visualizations_Taxonomy/blob/main/Navigationals/The_Richer_Scientific_Method.md). It is an **investigation navigator**, not a second PDF library or a collection of AI-generated summaries.

## Open the visual navigator

[**Explore these investigations visually**](https://raw.githack.com/JadanPoll/Learning_Visualizations_Taxonomy/main/RSM_Tree_Viewer.html) — choose a question, follow related branches, and open book references. The viewer uses this repository's [`rsm-view.json`](rsm-view.json) mapping without changing the source records. It can also load other public GitHub repositories with their own maps.

## Where things belong

- **Here:** Questions, branches, alternative explanations, sources mapped to those branches, findings, unresolved questions, and reasons to revisit earlier conclusions.
- **[FKEN Ecosystem](https://github.com/JadanPoll/FKEN_Ecosystem):** Broad domain and resource landscapes, reusable knowledge, projects, and skills. Link relevant records instead of copying them.
- **Google Drive / Kami:** Original books and annotated PDFs. Link to actual files; do not commit copyrighted books or duplicate uploads solely to populate this repository.

## Using the tree

1. Start with an actual curiosity or goal. Recover the parent purpose without silently replacing the question.
2. Sketch **only consequential branches**. The tree is provisional; cross-branch dependencies and competing models matter as much as hierarchy.
3. Search existing books and external literature. Recommend **specific verified books, editions, chapters/sections, and page ranges** when available. Distinguish a recommendation from a chapter actually inspected.
4. Attach evidence, observations, hypotheses, interpretations, and annotations to the branches they inform. Preserve competing explanations.
5. Revise the tree as understanding changes. Summarize a sufficiently investigated branch with its evidence, assumptions, limitations, and reopening conditions.
6. At the start of a later conversation, read the investigation record before continuing. Commit meaningful updates so the repository—not one chat—is the durable state.

## Layout

- `investigations.json` — Small directory of active and archived investigations.
- `Investigations/<slug>/investigation.json` — One canonical, structured record per substantive investigation, created only when needed.
- `Investigations/<slug>/notes.md` — Optional readable working notes or longer narratives when they add value.
- `AGENTS.md` — Conventions for continuing and editing investigations.

Each investigation can contain a root question, parent purpose, branch nodes, relationships, book/chapter references, evidence, and compact certificates. Stable node IDs allow links and references to survive renaming. Avoid mandatory empty fields and universal templates: add detail when it earns its cost.

## Returning to an investigation

In a new ChatGPT conversation, link this repository and name the investigation, e.g.:

> Continue the investigation on [topic] from Kami_Uploads_RSM_Tree. Read its current tree and evidence, then help me decide which question and book chapters are most consequential next.

An investigation is useful if someone returning after a month can see **why a question was asked, what was learned, where to verify it, and what could change the answer**.