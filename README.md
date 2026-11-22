# Kami Uploads — Research Navigator

Explore what you are curious about, follow the underlying mechanisms, and recover the relevant parts of real books. This repository preserves **questions, evidence, technical investigations, source locations, and links** across conversations; original books stay in Drive/Kami.

[**Open the manufacturing questions and investigations**](https://raw.githack.com/JadanPoll/Learning_Visualizations_Taxonomy/main/RSM_Tree_Viewer.html?repo=https%3A%2F%2Fgithub.com%2FJadanPoll%2FKami_Uploads_RSM_Tree&view=manufacturing-curiosities)

## One entrance, variable investigation scope

The manufacturing browser supports two entry sizes in one place:

- **One ordinary question**, such as “Why does my metal paper clip snap?” Its technical projection distinguishes cyclic plastic deformation, static fracture, and alternatives for designing flexible parts.
- **A larger question set**, such as “How can I make an unfamiliar functional thing?” Its technical projection spans manufacturing possibilities, functional requirements, mechanisms, assembly, tolerances, and practical verification.

An *investigation* is the purposeful exploration of one question **or a set of questions**, with evolving evidence and unresolved alternatives—not a separate file type or an independently copied tree. Both entry sizes traverse the **same technical records**. Change the question or scope; do not clone the books.

The technical explanations remain detailed and source-specific even when the entry question is childlike. The five larger sets—**Possibilities**, **Make it**, **Mechanisms**, **Production**, and **Bootstrap**—remain available through the same entry browser, not a separate manufacturing menu.

## Manufacturing data, without redundant JSONs

There is **one canonical manufacturing research JSON**:

[`Investigations/manufacturing-orientation/investigation.json`](Investigations/manufacturing-orientation/investigation.json)

Its principal sections serve different purposes without needing separate files:

| Section | Responsibility |
| --- | --- |
| `curiosity_atlas` | Searchable, ordinary-language entry questions and aliases |
| `landscape_views` | Larger question sets and purpose-conditioned parent relationships |
| `navigation_bridges` | Conditional technical explanations and which passages support investigating them |
| `nodes`, `connections` | Canonical technical questions, observations, mechanisms, experiments and relationships |
| `sources`, `book_landscaplets` | Book identities and bounded chapter/section retrieval locations |
| `book_factorization` | Reusable manufacturing operators and cross-book synthesis |

[`rsm-view.json`](rsm-view.json) is a small **viewer mapping manifest**, not another manufacturing knowledge database. Other domains (operating systems and human–AI collaboration) have independent research records because they represent distinct source corpora.

The current manufacturing collection contains **5 connected books**, **65 chapter/part retrieval locations**, **24 ordinary-language question entries**, **5 larger investigation scopes**, and **10 source-inspected technical studies**. These numbers describe the present index, **not** full passage coverage or proven practical navigation.

## Acceptance test: frustration → useful source

Follow [FKEN-16A — Frustration-to-resource traversability](AGENTS.md#fken-16a--frustration-to-resource-traversability). Start from an unfamiliar real frustration without giving away book vocabulary. The user should be able to recognize the next relevant distinction, reach an actual page or worked example, and explain why it helps.

Run the **reverse test** from independently chosen important passages: can plausible everyday questions lead to them? Compare with a book's table of contents and ordinary full-text search. Counts of nodes, branches, or chapter links do not establish discoverability.

[Manufacturing navigation audit and test prompts](Investigations/manufacturing-orientation/navigation_audit.md)

## Continuing and contributing

1. Start with a genuine curiosity or purpose. Choose one question or the broader set it belongs to.
2. Examine the technical alternatives; follow source citations. Clearly distinguish inspected technical evidence from suggested reading.
3. Record what an experiment, worked example, or source really established and what remains uncertain.
4. Preserve stable question, study, and source IDs across views so notes, links, and earlier research remain useful.
5. When navigation fails, correct the smallest consequential entry, mechanism distinction, source anchor, or relation. Don't create a new JSON or menu just because the existing one is awkward.

The [Richer Scientific Method](https://github.com/JadanPoll/Learning_Visualizations_Taxonomy/blob/main/Navigationals/The_Richer_Scientific_Method.md) guides investigation, and the [Richer Engineering Method](https://github.com/JadanPoll/Learning_Visualizations_Taxonomy/blob/main/Navigationals/The_Richer_Engineering_Method.md) guides practical functionality, testing, and subtraction. [`AGENTS.md`](AGENTS.md) carries persistent continuation instructions.

The objective is a navigator worth returning to after a month: **ask what you actually care about, encounter the relevant depth, and recover the evidence without rediscovering the organization**.
