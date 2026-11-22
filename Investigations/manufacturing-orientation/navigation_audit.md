# Manufacturing navigation acceptance audit — FKEN-16A

The objective is not to make a tree look complete. It is to let someone start with a real frustration or purpose, recognize consequential intermediate distinctions, and reach a recoverable source passage without knowing the book's terminology. Read [FKEN-16A in AGENTS.md](../../AGENTS.md) before interpreting these results.

## Confirmed defect and repair (2026-11-21)

Before the repair, five major views and 65 TOC-level entries existed but most source sections appeared only in a root-level book catalog. Existing questions such as external fabrication ended without actionable alternatives; users needed source vocabulary such as *fatigue*, *intermittent motion* or *geometric tolerancing* to discover the right study.

The repair keeps **one canonical investigation JSON**, adds ten ordinary-language problem entries, 27 discriminating choice paths, and connects all 65 existing book-section locators to intermediate question nodes via `entry_node_ids` and `use_when`. It exposes the paths in the viewer's **Problems** entry, each case inspector, and contextual chapter routes. Studies still retain their canonical IDs across all views.

These fixes improve navigational *structure*. They do not demonstrate that a reader can use it successfully.

## Audit states

| Measure | Outcome | What it establishes |
| --- | --- | --- |
| Canonical source-book records | 5 | Source identity is preserved |
| Source-inspected technical studies | 10 | Some destinations contain actual mechanism evidence |
| Everyday problem entries | 10 | There are recognizable initial situations |
| Conditional alternatives | 27 | A user can distinguish hypotheses rather than view a flat source list |
| Section locators with an intermediate-question route | 65 / 65 | Structural chapter-level reverse coverage |
| Orphaned cases, broken section IDs, or view-parent cycles | 0 found in static checks | Graph metadata is internally consistent |
| Real novice blind-navigation sessions | **Not performed** | No claim of human discovery effectiveness |
| Full subchapter/passage coverage | **Not established** | A TOC locator is not a fully factored book |

**Do not reinterpret the 65/65 result as success on FKEN-16A.** It tests *potential graph routes* at chapter granularity, not whether those routes are recognizable, relevant, accessible, or efficient to a human. Some chapters are still only candidates for future close reading.

## Blind navigation: question → passage

Present only the left column to someone who has not seen the source mapping, and do not hint at the expected mechanism. Begin from the manufacturing atlas's initial screen, rather than entering at a convenient technical node.

| Ordinary question or frustration | Audit key, hidden from participant |
| --- | --- |
| My printed clip cracks after several openings. | Investigate layer direction, stress at the flexure, and repeated-load fatigue; Smyth pp. 18–21, 94–95, 141; Howell pp. 8–11, 111–120; Shigley Ch. 6 p. 297 (TOC-only) |
| The gear wheel needs to advance one notch and then wait. | Indexing/dwell and motion profile; Sclater Geneva variants pp. 192–197; optionally Howell FACT pp. 82–89 |
| Both components match my CAD model but they stick when assembled. | Calibration, mating clearance, geometric variation; Smyth Ch. V p. 116 and Shigley Ch. 20 p. 995 |
| I might make ten of these enclosures now and thousands later. | Revision cost, tooling reuse, mold economics and quantitative break-even; manufacturing processes injection section PDF pp. 57–59, compare a digitally controlled route |
| I want a unique part but I have no workshop. | Outsourced flat cutting or printing with toleranced specification; manufacturing processes waterjet PDF pp. 279–281, additive PDF pp. 239–241, Shigley Ch. 20 |
| A hinge bends in unintended directions. | Degrees-of-freedom constraints versus flexure geometry; Howell FACT Ch. 6 pp. 82–89; tolerance and structural stiffness |
| I need to cut this material without melting the edge. | Thermal versus nonthermal material removal; manufacturing processes waterjet PDF pp. 279–281 |
| I need a hollow internal passage that an ordinary tool cannot reach. | Support/removal, expendable molds, layered construction or splitting/assembly; process handbook sand casting PDF pp. 127–129, SLA/SLS PDF pp. 239–241; Smyth Ch. II |
| I need more force without changing the motor. | Input/output force-distance tradeoff, friction and efficiency; Sclater Ch. 1 pp. 2–8, with limits on available travel |
| A mechanism returns to a different position each cycle. | Unwanted DOFs, loose joints, friction/hysteresis and toleranced geometry; Howell FACT pp. 82–89, Shigley Ch. 20, Sclater mechanisms basics |

For each route record: which view the person chose, whether they noticed **Problems**, the branch labels chosen, number of decisions and wrong turns, whether the linked source was opened at the correct printed or PDF page, the explanation they can give for why the passage is relevant, and whether it offers an actionable next step. Compare to a naive search or TOC browsing baseline. A click is not proof of understanding.

## Reverse navigation: passage → plausible question

Sample useful passages *independently* of existing navigation tags. Hide their book titles and special vocabulary while generating plausible human problems. Then trace from those problems to the source location.

Suggested starting passages include:
- Smyth, printed p. 141, snap latches and required flexure orientation;
- Shigley, Ch. 6, repeated loading/fatigue;
- Howell, Ch. 6, desired freedom and complementary constraints;
- Sclater, Ch. 7, mechanical indexing and dwell;
- manufacturing process handbook, PDF pp. 279–281, waterjet cutting and its edge-quality tradeoffs.

A source route counts as *observably useful* only when the actual destination is relevant and sufficiently specific to help decide or act. If the relevant material is deep inside a chapter, improve the subchapter/passage anchor rather than declaring the whole chapter covered.

## Failure taxonomy and correction rule

| What the user experiences | Likely deficiency | First intervention |
| --- | --- | --- |
| Cannot find a recognizable initial branch | Missing everyday-language question entry | Rename or add the smallest functional entry |
| Chooses a plausible branch that leads nowhere | Broken parent/child or missing actionable cross-link | Connect the existing canonical records |
| Gets unrelated books or generic chapters | Weak relevance discrimination | Add conditions, failure signatures or specific source sections |
| Can find a title but not the passage | Insufficient provenance/granularity | Record actual printed/PDF page or a verified deep link |
| Source is relevant but not enough to solve the problem | Confusing relevance with operational evidence | Improve real examples, experiments, implementation references |
| Navigator is slower than a TOC or search | Unnecessary steps or wrong hierarchy | Shorten route, change grouping or use search as entry fallback |

When evaluating a correction, repeat the same task with the same source corpus, including counterexamples where another explanation should win. Prefer observed failure reduction to growing the number of nodes or views.

## Boundaries

- Five user-selected goal trees are projections of **one canonical research corpus**, not copies of the books.
- Indexed chapters that were not closely read remain **TOC-level candidates**.
- No actual human usability timing or unfamiliar-user trials have been performed.
- Current source links open the relevant Drive/Kami book, but a printed page label is not guaranteed to create a direct page-positioned browser link.
- Future work should prioritize real failure examples from readers and passage-level coverage, not automatically enumerate every subheading.
