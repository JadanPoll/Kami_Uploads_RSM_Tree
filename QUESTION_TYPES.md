# Question types — inquiry, execution, and evidence

This is a **classification of what a question asks the person to do**, not a taxonomy of subject matter or a demand for identical wording. A rich investigation needs both exploratory questions and already well-defined capabilities. Start by identifying the requested cognitive or practical operation; do not manufacture questions to satisfy proportions.

## Primary question types

| ID (`question_type`) | Functional contract | Representative questions or capability prompts |
| --- | --- | --- |
| `explanation` | Understand a mechanism, concept, relationship or distinction | Why can pointwise and uniform limits differ? · What does a quotient preserve? · Why do some switching converters oscillate? |
| `execution` | **Perform** a defined operation on suitable inputs and produce a checkable result; a particular worksheet instance is optional | Can you perform Gaussian elimination? · Can you calculate a Bode plot from a transfer function? · Can you implement a UART receiver from a timing specification? |
| `verification` | Prove, refute, check, bound or certify a stated property/obligation | Can you prove a function is injective? · Can you verify timing constraints for a design? · Can you construct a counterexample to a claimed theorem? |
| `diagnosis` | Explain an observed failure/discrepancy and discriminate competing causes | Why does this RC car veer under acceleration? · Which hypothesis explains an intermittent I²C bus failure? · Why does the series approximation diverge? |
| `decomposition` | Turn an open-ended goal into requirements, independent subproblems, mechanisms and dependencies | How would I build an RC car? · What needs solving to build a low-cost scanning electron microscope? · What subtasks make a robot autonomous? |
| `design` | Synthesize an artifact, procedure or model to meet requirements and constraints | Can you design RC-car steering geometry under specified dimensions? · Can you design a stable compensator for this plant? · Can you design a bijection for a counting proof? |
| `empirical_investigation` | Plan, conduct or interpret observations that discriminate models or estimate quantities | Which experiment distinguishes thermal drift from measurement noise? · How would you measure a MEMS resonator's Q? · Does a controller remain stable on hardware? |
| `transfer` | Adapt, generalize, compose or establish the limits of a method across settings | Can you adapt Gaussian elimination to sparse systems? · When can a finite-dimensional spectral argument extend to operators? · Which control-law assumptions survive changing vehicle models? |

**Primary classification:** label the dominant obligation. Use `secondary_question_types` only when a genuinely independent second operation matters, not to hedge. For example, an experiment that diagnoses a failure is primarily `empirical_investigation` when the critical action is collecting discriminating measurements; it is primarily `diagnosis` when the measurements already exist and the task is fault localization.

## Independent task specificity

`task_scope` describes how fully the work has been instantiated; it is **not** difficulty or question type.

| ID | Meaning | Example |
| --- | --- | --- |
| `conceptual` | Understand a phenomenon or distinction, without a specific deliverable | Why does Gaussian elimination preserve solutions? |
| `open_goal` | Intended outcome known; mechanism/requirements/subtasks must be established | Build a reliable RC car |
| `capability_family` | A reusable operation or proof/construction contract is known; specific inputs can be supplied later | Perform Gaussian elimination and identify free variables |
| `specified_instance` | Inputs, assumptions and expected outputs are provided sufficiently to attempt this exact task | Row-reduce the supplied 4×4 matrix and parameterize its nullspace |

In particular, `capability_family` **does not need** arbitrary numbers, a theorem picked at random or a fabricated project scenario. It is a mathematical/engineering *operator class* that can later generate many bona fide homework or lab problems. A `specified_instance` adds an actual instance when useful, not by default.

## Minimal persistent fields

A question entry can use:

```json
{
  "id": "MATH-CAP-gaussian-elimination",
  "question": "Can you perform Gaussian elimination and identify pivot and free variables?",
  "question_type": "execution",
  "task_scope": "capability_family",
  "target_ids": ["MATH-VECTOR"],
  "success_criterion": "For an assigned matrix, produce a valid echelon form, identify pivot and free columns, and check the resulting solution parameterization."
}
```

- `question_type` and `task_scope` are orthogonal labels, not synonyms for `kind`, `status`, or evidence quality.
- `target_ids` is optional, linking a capability prompt to the canonical technical studies that support it; do not invent an unrelated technical node just to attach a label. Its IDs must exist, and a navigation bridge should reach them.
- `success_criterion` is a **checkable outcome contract**. It is not a claim that the learner can already do it, that a book teaches it in an inspected passage, or that any test was performed.
- Preserve original entries/IDs and source anchors. Review and tag an existing question rather than duplicating it under several phrasings.
- For technical study nodes, tags are optional: a study about eigenvalues is not *itself* an executable question merely because someone could use it in an exercise.

## Practical question-quality checks

Ask whether the prompt has a distinct demand rather than merely naming a topic; whether a learner could recognize what successful action looks like; whether a known method can be applied without re-deriving an entire discipline; and whether ambiguity is **intentional** (decomposition) or **accidental** (under-specified execution).

An entry like “Can you analyze linear algebra?” does not count as execution. Neither does “How does Gaussian elimination work?” unless the requested outcome is explanation. “Can you perform Gaussian elimination?” does: it names an operation whose input and output contracts are well established.

Some broad open-ended problems are legitimate exactly because they **test decomposition**. Do not ‘repair’ “How would I build an RC car?” by pretending it is a row-reduction-style task. Conversely, do not replace an actionable operator with a vague design-thinking question.

## Coverage as a diagnostic, not a quota

For a given domain, count questions by `question_type` and `task_scope`, and optionally cross-tabulate by family and source. An overwhelming `explanation` share can reveal missing actionable skills; an overwhelming `execution` share can hide design, diagnosis, proof and experimentation. These counts signal **where to investigate omissions**, not target percentages to optimize. A domain can legitimately have a skewed distribution.

Audit concrete coverage separately: map a representative task to a capability, its supporting source passage, a possible instance, and a plausible wrong answer or failure mode. Count **capability families**, not arbitrary parameter variations. A handful of generators is more useful than dozens of synthetic drill questions.

## Adoption across this repository

Tag existing questions incrementally when they are reviewed. For mathematics, the canonical question entries live in `Investigations/mathematics/investigation.json`, while five family files retain only stable `question_ids`. Technical nodes and sources remain family-owned. Do not duplicate source notes, broad curiosities or instantiated homework into the family files.

The root `AGENTS.md` is the authoring contract; future domains use this classification without importing the mathematics-specific operators. The viewer should display the tags and success criteria without conflating them with evidence or task completion.
