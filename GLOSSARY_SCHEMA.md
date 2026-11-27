# Glossary substrate for the Knowledge Atlas

Most domains have **one canonical `investigation.json` for evidence, questions and mechanisms** and **one adjacent `glossary.json` for persistent vocabulary identities**. Mathematics instead composes five family-owned files into a small root atlas; its glossary contains independent vocabulary, whether or not linked to an existing question. They are distinct data lifecycles: changing how a term is spelled or discovered should not copy or rewrite its technical explanations.

| Domain | Vocabulary | Research |
| --- | --- | --- |
| Manufacturing | [glossary](Investigations/manufacturing-orientation/glossary.json) | [investigation](Investigations/manufacturing-orientation/investigation.json) |
| Operating systems | [glossary](Investigations/operating-systems/glossary.json) | [investigation](Investigations/operating-systems/investigation.json) |
| Human–AI collaboration | [glossary](Investigations/human-ai-symbiosis/glossary.json) | [investigation](Investigations/human-ai-symbiosis/investigation.json) |
| FPGA / VLSI | [glossary](Investigations/digital-hardware-design/glossary.json) | [investigation](Investigations/digital-hardware-design/investigation.json) |
| Robotics | [glossary](Investigations/robotics/glossary.json) | [investigation](Investigations/robotics/investigation.json) |
| Mathematics | [glossary](Investigations/mathematics/glossary.json) | [investigation](Investigations/mathematics/investigation.json) |

## Contract

A `glossary.json` owns the following properties:

- `schema_version: "1.0"`, `domain_id`, `title`, `terms`, and optional `redirects`.
- A term has a **permanent** `id`, preferred `label`, `aliases: []`, a retrieval `category`, and `related_ids: []`. Optional supplementary fields may be introduced only when they materially improve search or understanding.
- Term IDs, such as `dhw-t-0082` for **metastability** and `dhw-t-0080` for **clock-domain crossing**, are **opaque identities**, not hashes of a mutable display name. Renaming, reclassifying, reordering, adding or removing an alias **must not change the ID**.
- `related_ids` means a **real, non-equivalent conceptual relation** (e.g. metastability relates to clock-domain crossing). Do not use it to merge distinct concepts into synonyms, or to imply that two phenomena share the same cause.
- A true synonym or acronym belongs in the **same term's `aliases`**. If a former term is merged, keep its old ID as a `redirects` mapping to the survivor. Never reuse retired IDs for other meanings.
- Domain IDs are namespaced. An OS **register** and an FPGA **register** need not be the same concept. Cross-domain relationships should be explicit and sense-aware rather than inferred from spelling.
- Original [FKEN glossaries](https://github.com/JadanPoll/FKEN_Ecosystem/tree/main/Glossaries) are vocabulary seed sources, not another live dependency or second owner of the domain's terminology. Some seed-list groups describe related **different** words, not equivalent spellings.

A canonical `investigation.json` references these IDs with optional `term_ids: ["dhw-t-0082", "dhw-t-0080"]` on:

- `curiosity_atlas.entries` (ordinary-language entry questions)
- `nodes` (technical mechanism and evidence records)
- `navigation_bridges` and their `choices` (conditional mechanism options)
- `landscape_views` (larger question sets)
- `question_nodes` and `fieldwork_nodes` where present (legacy question indexes and independently sourced cases)

These records do **not** embed second copies of term names or long definitions. Substantive explanations and bounded source locations belong in the technical corpus.

## Search and browsing

The [Knowledge Atlas viewer](https://github.com/JadanPoll/Learning_Visualizations_Taxonomy/blob/main/RSM_Tree_Viewer.html) loads `investigation.json` and its declared glossary from the same repository and branch, not through GitHub's rate-limited recursive tree enumeration. Missing or unreadable glossaries degrade gracefully to ordinary text search.

The questions browser searches (in descending relevance):

1. Question text, ordinary context and entry aliases.
2. **Directly referenced concept** labels and aliases (`term_ids`).
3. **One-hop related concepts**, with lower ranking because related does not mean equivalent.

A Vocabulary mode permits discovery of terms without already knowing which ordinary question to ask. Opening a term shows linked curiosity questions, technical nodes and other explicitly related concepts. The term page can be shared through the URL's `term` parameter. Concept chips in the technical inspector navigate back to these pages.

## When adding or changing knowledge

1. **Search existing labels and aliases** in that domain and check the *sense*, not merely spelling. Reuse an existing term ID if it is the same concept.
2. If the concept is new, append a new term with a fresh never-reused ID. **Do not regenerate or renumber previous IDs.** A word's hash is not a safe permanent identity.
3. Add the minimal `term_ids` on relevant questions, bridge choices or canonical nodes. Avoid blanket tagging: a loosely related term should not make an unrelated question appear to be its direct application.
4. If a user searches for a real mechanism and finds the wrong question, correct the ambiguous alias, misleading relation or target link. Do not stuff the full technical explanation into `glossary.json`.
5. Keep the FKEN glossary vocabulary useful for independent browsing and competence discovery; this domain-local index is the Atlas's **search and cross-reference substrate**, not a replacement for the original FKEN work.
6. When changing the schema, preserve previous valid IDs and links; add compatibility handling rather than silently breaking bookmarked notes or previously shared term links.

### Example

```json
{
  "id": "DHW-CURI-cdc",
  "question": "Why can two individually working circuits fail when connected?",
  "term_ids": ["dhw-t-0080", "dhw-t-0082"]
}
```

An everyday question can now be recovered by searching **metastability** even though that word need never appear in the entry question. The detailed physical explanation, clock-domain conditions, and book passages stay in the technical node instead of being copied into every entry.

**Evidence boundary:** A vocabulary link is a candidate *retrieval connection*, not a demonstration that the concept explains the user's specific failure. As with the existing investigation corpus, source-inspected sections and chapter-only leads remain different evidentiary statuses.
