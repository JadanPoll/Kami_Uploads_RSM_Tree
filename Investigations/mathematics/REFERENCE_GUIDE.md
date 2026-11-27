# Mathematics — fourteen-book research navigator and generative factorization

**Read this before reindexing the shelf.** The root [`investigation.json`](investigation.json) composes five family-owned research files at read time. Its [`glossary.json`](glossary.json) indexes the independent vocabulary landscape, including terms without mapped questions. The investigation currently contains 14 books, 185 main chapter/part/section units, 836 finer subsection candidates, 39 canonical technical studies, 85 question entrances (46 conceptual/research prompts and 39 reusable capability prompts), 9 large investigation sets, 12 cross-book operator chains, and 14 source-passage inspections. Counts are **navigation coverage**, not comprehension or proof reproduction.

**Original [Drive shelf](https://drive.google.com/drive/folders/1Qx_V7FAz2EhbmCAijHMr18swPu5GLyZr)**. Read and highlight original PDFs in Kami/Drive; GitHub holds only research state, stable pointers and interpretation.

## Capability-first mathematical practice (November 2026 revision)

The shared mathematics atlas now separates its **46 original orientation questions** from **39 additional operational capability prompts**: Gaussian elimination, linear-system solving, rank/nullity, eigenstructure, modular arithmetic, inclusion–exclusion, Möbius inversion, limit and compactness proofs, contour integration, curvature, Bayesian conditioning, estimation, and other representative mathematical operators. Unlike an arbitrary homework worksheet, a capability prompt names a *reusable family* of input/output tasks. Each new prompt specifies an observable `success_criterion` and a `target_ids` link to an existing canonical study; it does **not** claim the student has performed the exercise or that a textbook exercise number was verified. Specific practice instances can be generated later.

Question-type labels are governed by [../../QUESTION_TYPES.md](../../QUESTION_TYPES.md). The current 85 question entries are **36 explanation, 31 execution, 13 verification and 5 transfer**. These are the current *mathematics question-panel* counts, not technical-node counts or goals for future percentages. Diagnosis, design, experimental investigation and decomposition are important in other disciplines and may be pertinent to mathematical practice, but we should not force every mathematical field to have matching numbers. Existing conceptual questions remain available for why/when/transfer exploration; practicing an operation should not require first reconstructing its entire research context.

**Research-node scope is unchanged.** The 39 canonical technical studies, 14 books, source passage inspections, all source IDs, and glossary identities remain family-owned; the root owns shared entry texts and bridge routes. The new narrowly targeted capability prompts constrain the viewer's broad navigation branches to the relevant study rather than importing a whole unrelated family into the practice card.

## Research-family question panels

Each family records `question_ids` in its own `investigation.json`: stable references to ordinary-language questions owned by the mathematics root `curiosity_atlas.entries`. A question can appear in several families **without copying its text, bridge definitions or evidence**. The [viewer](https://github.com/JadanPoll/Learning_Visualizations_Taxonomy/blob/main/RSM_Tree_Viewer.html) loads the family research and the shared question atlas explicitly, not GitHub's recursive directory API. Within the family panel, shared bridge choices are limited to technical records actually owned there; **Explore all mathematics** exposes their other branches on demand. The family glossary panel similarly indexes only concepts connected to its research.

To extend a family: add or improve authentic questions in the root entry registry, reference those IDs in the relevant family's `question_ids`, and add source-backed mechanisms to the family research file. Do not manufacture filler questions or add a question merely to achieve symmetry between families. Check that each selected question has at least one technical route into that family, and that the viewer can actually traverse it. The full atlas remains the cross-family entry point.

## Research families — canonical ownership

- [Foundations and algebra](foundations-and-algebra/) — Definitions, mappings, linear structure, symmetry and algebraic obstructions.
- [Analysis and dynamics](analysis-and-dynamics/) — Limits, integration, function spaces and operators; future home for differential equations and dynamical systems.
- [Geometry and topology](geometry-and-topology/) — Continuity, global shape, topology and intrinsic/extrinsic curvature.
- [Probability and statistics](probability-and-statistics/) — Uncertainty models, stochastic processes, observations and inference.
- [Discrete mathematics](discrete-mathematics/) — Arithmetic, posets, counting, graphs and finite certificates.

Each source catalog, technical node and inspected passage has one canonical owner. The unified atlas preserves cross-family questions, operator compositions and stable source identities without duplicating the content of family files. Original Drive PDF links remain unchanged.

## The underlying generative model

Mathematics becomes navigable when a question exposes: **objects → added structure → admissible transformations → invariants and obstructions → construction/inference/approximation → proof obligations**. Different branches reuse these operators, but the hypotheses and invariants are not interchangeable.

| Added structure | New objects/transformations | What can now be asked? |
| --- | --- | --- |
| Set | membership, relations, functions · functions and bijections | Which constructions are admissible? |
| Vector space | addition and scalar multiplication · linear transformations | Which basis-free invariants survive? |
| Group | reversible composition · homomorphisms and equivariant actions | What symmetries and quotients exist? |
| Ring or field | addition, multiplication and ideals · ring or field homomorphisms | What factoring and extension properties hold? |
| Topological/metric space | open sets or distances · continuous maps, homeomorphisms, isometries | Which neighborhoods, limits and holes survive? |
| Measurable/probability space | sigma-algebra, countably additive measure · measurable or distribution-preserving maps | What is measurable or uncertain? |
| Graph or poset | adjacency or order relation · graph isomorphisms or order-preserving maps | Which global constraints follow from local relations? |

**Consequential comparison:** a *bijection* preserves set cardinality, a *group isomorphism* preserves operations, a *homeomorphism* preserves topology, an *isometry* preserves distances, and a *measure-preserving map* preserves a specified measure. They may share an underlying bijection but are different contracts. Similarly, 'normal' is unrelated across a normal subgroup, normal operator and normal probability distribution unless a substantive theorem connects them.

## Books, coverage and boundaries

| Source | Intellectual contribution | Indexed units | Precision / caveat |
| --- | --- | ---: | --- |
| [Algebra](https://drive.google.com/file/d/1r6Y76kY6T36HiBRPEV4IzFj8u24VQqtQ/view) | Linear algebra, symmetry groups, representation theory, rings, arithmetic and Galois theory | 16 + 135 | Edition in connected PDF; exact imprint/year to confirm from title pages |
| [Finite-Dimensional Vector Spaces](https://drive.google.com/file/d/1eFyex_8kmj5ZYSSQlpfQN8i-KGjPoxry/view) | Basis-free linear maps, duality, tensors, spectra, orthogonality and finite-dimensional analysis | 4 + 85 | Springer reprint, PDF OCR degraded; original work in sections not modern chapters |
| [Topology](https://drive.google.com/file/d/1_a8QHxSed_yHkSJ7Rru01WhMak7-kf11/view) | Open-set topology, compactness/connectedness, separation, metrization, homotopy and covering spaces | 13 + 0 | Second Edition text in 2014 Pearson Custom Library assembly |
| [Statistical Inference](https://drive.google.com/file/d/16l7HK50HTLSDxGNZt31yLu__JsMLOqkm/view) | Sampling distributions, sufficiency, estimation, tests, confidence intervals and large-sample theory | 12 + 152 | Second Edition, 2002 |
| [An Introduction to Probability Theory and Its Applications, Volume I](https://drive.google.com/file/d/1qY0vrM1KHzLD5x1cMjdio6LFIP_ge4Pb/view) | Classical and discrete probability, random walks, limit laws, generating functions, renewal, branching and Markov processes | 17 + 0 | Third Edition, revised printing |
| [Complex Analysis: An Introduction to the Theory of Analytic Functions of One Complex Variable](https://drive.google.com/file/d/1WNsPRVM8YucXXZCYWLjtLx891LHIqoCg/view) | Holomorphic maps, contour integration, residues, conformal maps, elliptic functions and analytic continuation | 8 + 0 | Third Edition |
| [Real Analysis](https://drive.google.com/file/d/13FxsPLoAJIm3LY5hNlfGP6rfdqwNsZ4W/view) | Lebesgue measure/integration, Lp, abstract measure, Banach spaces, general topology and invariant measures | 22 + 91 | Fifth Edition |
| [Naive Set Theory](https://drive.google.com/file/d/1Rai3_jSkyOeFnqDncR2f62Bs2va0a5ZM/view) | Axiomatic set operations, relations/functions, choice, ordinals, cardinals and recursion | 25 + 0 | Van Nostrand Reinhold edition as connected PDF |
| [An Introduction to the Theory of Numbers](https://drive.google.com/file/d/1-IfqhSU9Ro7oppMhY4ta0dBWpd7gU509/view) | Prime distribution, congruences, Diophantine equations, multiplicative functions, partitions and elliptic curves | 25 + 156 | Sixth Edition, revised by D. R. Heath-Brown and J. H. Silverman |
| [Differential Geometry of Curves and Surfaces](https://drive.google.com/file/d/1Hjfdm25uPxJ_A8k7SGl9TIDkxlEdnuGX/view) | Curvature, tangent geometry, intrinsic/extrinsic surfaces, geodesics, Gauss–Bonnet and global geometry | 5 + 37 | Revised & Updated Second Edition, Dover |
| [Introductory Functional Analysis with Applications](https://drive.google.com/file/d/1ArZFwHZVVMRxn64aPispU6hE21jL1Mu3/view) | Metric, Banach and Hilbert spaces, operator theory, approximation, fixed-point arguments and spectral methods | 11 + 65 | John Wiley & Sons, 1978 |
| [Principles of Mathematical Analysis](https://drive.google.com/file/d/1al-Lk0C8wHshwF3JTd4iB-glNI1hp-ny/view) | Limits, metric topology, continuity, differentiation, integration, series, uniform convergence and several variables | 11 + 0 | Rudin text retypeset by a third party; PDF foreword explicitly notes changed page numbering (filename '5ed' not reliable edition evidence) |
| [Graph Theory](https://drive.google.com/file/d/1OaIGUFGzOcHMyUGanaP1G98izbHWYETC/view) | Connectivity, matching, flow, planar graphs, coloring, extremal and random graphs, minors and treewidth | 12 + 71 | Sixth Edition as stated on title page; check source edition when citing theorem labels |
| [Enumerative Combinatorics, Volume 1](https://drive.google.com/file/d/1-Virg2U0k4ZDVtbYH7PlRAkLvHhC9yR3/view) | Counting operators, inclusion-exclusion, posets and Möbius inversion, rational generating functions and transfer matrices | 4 + 44 | Second Edition |

**Pagination is not uniform.** The connected *Rudin* PDF explicitly announces changed pagination from retypesetting; despite the filename '5ed', that is not evidence of a fifth published edition. *Munkres* comes in a Pearson Custom Library assembly that lists chapters 13 and 12 out of numerical order. *Feller* and *Hardy–Wright* use Roman numerals in their contents; *Halmos, Finite-Dimensional Vector Spaces* uses numbered sections within four parts. Many *Artin* and other scan-OCR page hints are candidate anchors, **not verified PDF positions**. Only use direct Kami page links when independently verified.

## Book-by-book chapter navigator

### Algebra
<small>Source ID: `ARTIN` · [Open original PDF](https://drive.google.com/file/d/1r6Y76kY6T36HiBRPEV4IzFj8u24VQqtQ/view) · 16 principal units and 135 finer locators</small>

| Unit | Title / functional retrieval | Printed start |
| --- | --- | ---: |
| 1 | Matrices | Unverified |
| 2 | Groups | Unverified |
| 3 | Vector Spaces | Unverified |
| 4 | Linear Operators | Unverified |
| 5 | Applications of Linear Operators | Unverified |
| 6 | Symmetry | Unverified |
| 7 | More Group Theory | Unverified |
| 8 | Bilinear Forms | Unverified |
| 9 | Linear Groups | Unverified |
| 10 | Group Representations | Unverified |
| 11 | Rings | Unverified |
| 12 | Factoring | Unverified |
| 13 | Quadratic Number Fields | Unverified |
| 14 | Linear Algebra in a Ring | Unverified |
| 15 | Fields | Unverified |
| 16 | Galois Theory | Unverified |

### Finite-Dimensional Vector Spaces
<small>Source ID: `HALMOS-LIN` · [Open original PDF](https://drive.google.com/file/d/1eFyex_8kmj5ZYSSQlpfQN8i-KGjPoxry/view) · 4 principal units and 85 finer locators</small>

| Unit | Title / functional retrieval | Printed start |
| --- | --- | ---: |
| I | Spaces | 1 |
| II | Transformations | 55 |
| III | Orthogonality | 118 |
| IV | Analysis | 175 |

### Topology
<small>Source ID: `MUNKRES` · [Open original PDF](https://drive.google.com/file/d/1_a8QHxSed_yHkSJ7Rru01WhMak7-kf11/view) · 13 principal units and 0 finer locators</small>

| Unit | Title / functional retrieval | Printed start |
| --- | --- | ---: |
| 1 | Set Theory and Logic | 1 |
| 2 | Topological Spaces and Continuous Functions | 73 |
| 3 | Connectedness and Compactness | 145 |
| 4 | Countability and Separation Axioms | 187 |
| 5 | The Tychonoff Theorem | 228 |
| 6 | Metrization Theorems and Paracompactness | 241 |
| 7 | Complete Metric Spaces and Function Spaces | 261 |
| 8 | Baire Spaces and Dimension Theory | 292 |
| 9 | The Fundamental Group | 317 |
| 10 | Separation Theorems in the Plane | 372 |
| 11 | The Seifert-van Kampen Theorem | 403 |
| 12 | Classification of Surfaces | 468 |
| 13 | Classification of Covering Spaces | 443 |

### Statistical Inference
<small>Source ID: `CASELLA` · [Open original PDF](https://drive.google.com/file/d/16l7HK50HTLSDxGNZt31yLu__JsMLOqkm/view) · 12 principal units and 152 finer locators</small>

| Unit | Title / functional retrieval | Printed start |
| --- | --- | ---: |
| 1 | Probability Theory | 1 |
| 2 | Transformations and Expectations | 47 |
| 3 | Common Families of Distributions | 85 |
| 4 | Multiple Random Variables | 139 |
| 5 | Properties of a Random Sample | 207 |
| 6 | Principles of Data Reduction | 271 |
| 7 | Point Estimation | 311 |
| 8 | Hypothesis Testing | 373 |
| 9 | Interval Estimation | 417 |
| 10 | Asymptotic Evaluations | 467 |
| 11 | Analysis of Variance and Regression | 521 |
| 12 | Regression Models | 577 |

### An Introduction to Probability Theory and Its Applications, Volume I
<small>Source ID: `FELLER` · [Open original PDF](https://drive.google.com/file/d/1qY0vrM1KHzLD5x1cMjdio6LFIP_ge4Pb/view) · 17 principal units and 0 finer locators</small>

| Unit | Title / functional retrieval | Printed start |
| --- | --- | ---: |
| I | The Sample Space | Unverified |
| II | Elements of Combinatorial Analysis | Unverified |
| III | Fluctuations in Coin Tossing and Random Walks | 67 |
| IV | Combination of Events | 97 |
| V | Conditional Probability and Stochastic Independence | 114 |
| VI | The Binomial and the Poisson Distributions | 146 |
| VII | The Normal Approximation to the Binomial Distribution | 173 |
| VIII | Infinite Sequences of Bernoulli Trials | Unverified |
| IX | Random Variables; Expectation | 212 |
| X | Laws of Large Numbers | 243 |
| XI | Integral-Valued Variables; Generating Functions | 264 |
| XII | Compound Distributions; Branching Processes | 286 |
| XIII | Recurrent Events; Renewal Theory | 303 |
| XIV | Random Walk and Ruin Problems | 342 |
| XV | Markov Chains | 372 |
| XVI | Algebraic Treatment of Finite Markov Chains | Unverified |
| XVII | The Simplest Time-Dependent Stochastic Processes | Unverified |

### Complex Analysis: An Introduction to the Theory of Analytic Functions of One Complex Variable
<small>Source ID: `AHLFORS` · [Open original PDF](https://drive.google.com/file/d/1WNsPRVM8YucXXZCYWLjtLx891LHIqoCg/view) · 8 principal units and 0 finer locators</small>

| Unit | Title / functional retrieval | Printed start |
| --- | --- | ---: |
| 1 | Complex Numbers | 1 |
| 2 | Complex Functions | Unverified |
| 3 | Analytic Functions as Mappings | Unverified |
| 4 | Complex Integration | Unverified |
| 5 | Series and Product Developments | 175 |
| 6 | Conformal Mapping; Dirichlet's Problem | Unverified |
| 7 | Elliptic Functions | Unverified |
| 8 | Global Analytic Functions | Unverified |

### Real Analysis
<small>Source ID: `ROYDEN` · [Open original PDF](https://drive.google.com/file/d/13FxsPLoAJIm3LY5hNlfGP6rfdqwNsZ4W/view) · 22 principal units and 91 finer locators</small>

| Unit | Title / functional retrieval | Printed start |
| --- | --- | ---: |
| 1 | The Real Numbers: Sets, Sequences, and Functions | 7 |
| 2 | Lebesgue Measure | 29 |
| 3 | Lebesgue Measurable Functions | 51 |
| 4 | Lebesgue Integration | 62 |
| 5 | Lebesgue Integration: Further Topics | 81 |
| 6 | Differentiation and Integration | 92 |
| 7 | The Lp Spaces: Completeness and Approximation | Unverified |
| 8 | The Lp Spaces: Duality, Weak Convergence, and Minimization | Unverified |
| 9 | General Measure Spaces: Their Properties and Construction | 159 |
| 10 | Particular Measures | 174 |
| 11 | Integration over General Measure Spaces | 201 |
| 12 | General Lp Spaces: Completeness, Convolution, and Duality | Unverified |
| 13 | Metric Spaces: General Properties | 263 |
| 14 | Metric Spaces: Three Fundamental Theorems and Applications | 285 |
| 15 | Topological Spaces: General Properties | 305 |
| 16 | Topological Spaces: Three Fundamental Theorems | 323 |
| 17 | Continuous Linear Operators Between Banach Spaces | 337 |
| 18 | Duality for Normed Linear Spaces | 355 |
| 19 | Compactness Regained: The Weak Topology | 382 |
| 20 | Continuous Linear Operators on Hilbert Spaces | 392 |
| 21 | Measure and Topology | 423 |
| 22 | Invariant Measures | 452 |

### Naive Set Theory
<small>Source ID: `HALMOS-SET` · [Open original PDF](https://drive.google.com/file/d/1Rai3_jSkyOeFnqDncR2f62Bs2va0a5ZM/view) · 25 principal units and 0 finer locators</small>

| Unit | Title / functional retrieval | Printed start |
| --- | --- | ---: |
| 1 | The Axiom of Extension | 1 |
| 2 | The Axiom of Specification | 4 |
| 3 | Unordered Pairs | 7 |
| 4 | Unions and Intersections | 10 |
| 5 | Complements and Powers | 14 |
| 6 | Ordered Pairs | 18 |
| 7 | Relations | 22 |
| 8 | Functions | 25 |
| 9 | Families | 28 |
| 10 | Inverses and Composites | 31 |
| 11 | Numbers | 34 |
| 12 | The Peano Axioms | 38 |
| 13 | Arithmetic | 41 |
| 14 | Order | 45 |
| 15 | The Axiom of Choice | 49 |
| 16 | Zorn's Lemma | 52 |
| 17 | Well Ordering | 55 |
| 18 | Transfinite Recursion | 58 |
| 19 | Ordinal Numbers | 61 |
| 20 | Sets of Ordinal Numbers | 64 |
| 21 | Ordinal Arithmetic | 67 |
| 22 | The Schroeder–Bernstein Theorem | 71 |
| 23 | Countable Sets | 74 |
| 24 | Cardinal Arithmetic | 77 |
| 25 | Cardinal Numbers | 81 |

### An Introduction to the Theory of Numbers
<small>Source ID: `HARDY` · [Open original PDF](https://drive.google.com/file/d/1-IfqhSU9Ro7oppMhY4ta0dBWpd7gU509/view) · 25 principal units and 156 finer locators</small>

| Unit | Title / functional retrieval | Printed start |
| --- | --- | ---: |
| I | The Series of Primes (1) | Unverified |
| II | The Series of Primes (2) | Unverified |
| III | Farey Series and a Theorem of Minkowski | Unverified |
| IV | Irrational Numbers | 45 |
| V | Congruences and Residues | 57 |
| VI | Fermat's Theorem and Its Consequences | Unverified |
| VII | General Properties of Congruences | 103 |
| VIII | Congruences to Composite Moduli | Unverified |
| IX | The Representation of Numbers by Decimals | Unverified |
| X | Continued Fractions | Unverified |
| XI | Approximation of Irrationals by Rationals | 198 |
| XII | The Fundamental Theorem of Arithmetic in Quadratic Fields | Unverified |
| XIII | Some Diophantine Equations | 245 |
| XIV | Quadratic Fields (1) | 264 |
| XV | Quadratic Fields (2) | 283 |
| XVI | The Arithmetical Functions | 302 |
| XVII | Generating Functions of Arithmetical Functions | 318 |
| XVIII | The Order of Magnitude of Arithmetical Functions | 342 |
| XIX | Partitions | 361 |
| XX | Representation by Two or Four Squares | Unverified |
| XXI | Representation by Cubes and Higher Powers | Unverified |
| XXII | The Series of Primes (3) | Unverified |
| XXIII | The Series of Primes (4) | Unverified |
| XXIV | Geometry of Numbers | 523 |
| XXV | Elliptic Curves | 549 |

### Differential Geometry of Curves and Surfaces
<small>Source ID: `DOCARMO` · [Open original PDF](https://drive.google.com/file/d/1Hjfdm25uPxJ_A8k7SGl9TIDkxlEdnuGX/view) · 5 principal units and 37 finer locators</small>

| Unit | Title / functional retrieval | Printed start |
| --- | --- | ---: |
| 1 | Curves | 1 |
| 2 | Regular Surfaces | 53 |
| 3 | The Geometry of the Gauss Map | 136 |
| 4 | The Intrinsic Geometry of Surfaces | 220 |
| 5 | Global Differential Geometry | 321 |

### Introductory Functional Analysis with Applications
<small>Source ID: `KREYSZIG` · [Open original PDF](https://drive.google.com/file/d/1ArZFwHZVVMRxn64aPispU6hE21jL1Mu3/view) · 11 principal units and 65 finer locators</small>

| Unit | Title / functional retrieval | Printed start |
| --- | --- | ---: |
| 1 | Metric Spaces | Unverified |
| 2 | Normed Spaces; Banach Spaces | 49 |
| 3 | Inner Product Spaces; Hilbert Spaces | 127 |
| 4 | Fundamental Theorems for Normed and Banach Spaces | Unverified |
| 5 | Further Applications: Banach Fixed Point Theorem | Unverified |
| 6 | Further Applications: Approximation Theory | Unverified |
| 7 | Spectral Theory of Linear Operators | Unverified |
| 8 | Compact Linear Operators on Normed Spaces | Unverified |
| 9 | Spectral Theory of Bounded Self-Adjoint Linear Operators | Unverified |
| 10 | Unbounded Linear Operators in Hilbert Space | Unverified |
| 11 | Unbounded Linear Operators in Quantum Mechanics | Unverified |

### Principles of Mathematical Analysis
<small>Source ID: `RUDIN` · [Open original PDF](https://drive.google.com/file/d/1al-Lk0C8wHshwF3JTd4iB-glNI1hp-ny/view) · 11 principal units and 0 finer locators</small>

| Unit | Title / functional retrieval | Printed start |
| --- | --- | ---: |
| 1 | The Real and Complex Number Systems | 1 |
| 2 | Basic Topology | 22 |
| 3 | Numerical Sequences and Series | 43 |
| 4 | Continuity | 76 |
| 5 | Differentiation | 94 |
| 6 | The Riemann–Stieltjes Integral | 110 |
| 7 | Sequences and Series of Functions | 132 |
| 8 | Some Special Functions | 159 |
| 9 | Functions of Several Variables | 190 |
| 10 | Integration of Differential Forms | 230 |
| 11 | The Lebesgue Theory | 282 |

### Graph Theory
<small>Source ID: `DIESTEL` · [Open original PDF](https://drive.google.com/file/d/1OaIGUFGzOcHMyUGanaP1G98izbHWYETC/view) · 12 principal units and 71 finer locators</small>

| Unit | Title / functional retrieval | Printed start |
| --- | --- | ---: |
| 1 | The Basics | 1 |
| 2 | Matching, Covering and Packing | 37 |
| 3 | Connectivity | 63 |
| 4 | Planar Graphs | 93 |
| 5 | Colouring | 123 |
| 6 | Flows | 155 |
| 7 | Extremal Graph Theory | 179 |
| 8 | Infinite Graphs | 227 |
| 9 | Ramsey Theory for Graphs | 303 |
| 10 | Hamilton Cycles | 323 |
| 11 | Random Graphs | 339 |
| 12 | Graph Minors | 363 |

### Enumerative Combinatorics, Volume 1
<small>Source ID: `STANLEY` · [Open original PDF](https://drive.google.com/file/d/1-Virg2U0k4ZDVtbYH7PlRAkLvHhC9yR3/view) · 4 principal units and 44 finer locators</small>

| Unit | Title / functional retrieval | Printed start |
| --- | --- | ---: |
| 1 | What Is Enumerative Combinatorics? | 1 |
| 2 | Sieve Methods | 195 |
| 3 | Partially Ordered Sets | 241 |
| 4 | Rational Generating Functions | 464 |

## High-value retrieval shortcuts

These are *selected* points whose mathematical distinctions affect decisions, not a substitute for all indexed subsections. Their exact status is retained in the canonical JSON.

### Algebra

| Reference | Subject | Printed page / status |
| --- | --- | --- |
| §2.5 | Homomorphisms | start unverified · TOC heading only |
| §6.7 | Abstract Symmetry: Group Operations | start unverified · TOC heading only |
| §7.7 | The Sylow Theorems | start unverified · TOC heading only |
| §10.4 | Characters | start unverified · TOC heading only |
| §11.4 | Quotient Rings . . | start unverified · TOC heading only |
| §13.5 | Factoring Ideals | start unverified · TOC heading only |
| §16.1 | Symmetric Functions | p. 477 · OCR candidate — verify title/page |
| §16.10 | Roots of Unity | p. 497 · OCR candidate — verify title/page |

### Finite-Dimensional Vector Spaces

| Reference | Subject | Printed page / status |
| --- | --- | --- |
| §1 | Fields | p. 1 · OCR candidate — verify title/page |
| §8 | Dimension | p. 13 · OCR candidate — verify title/page |
| §50 | Rank and nullity | p. 90 · OCR candidate — verify title/page |
| §54 | Proper values | p. 102 · OCR candidate — verify title/page |
| §79 | Spectral theorem | p. 155 · OCR candidate — verify title/page |
| §83 | Polar decomposition | p. 169 · OCR candidate — verify title/page |
| §92 | Ergodic theorem | p. 184 · OCR candidate — verify title/page |

### Topology

| Reference | Subject | Printed page / status |
| --- | --- | --- |
| §2 | Topological Spaces and Continuous Functions | p. 73 · TOC inspected |
| §3 | Connectedness and Compactness | p. 145 · TOC inspected |
| §5 | The Tychonoff Theorem | p. 228 · TOC inspected |
| §9 | The Fundamental Group | p. 317 · TOC inspected |
| §11 | The Seifert-van Kampen Theorem | p. 403 · TOC inspected |
| §13 | Classification of Covering Spaces | p. 443 · TOC inspected |

### Statistical Inference

| Reference | Subject | Printed page / status |
| --- | --- | --- |
| §3.4 | Exponential Families | p. 111 · TOC inspected |
| §6.2 | The Sufficiency Principle | p. 272 · TOC inspected |
| §7.3 | Methods of Evaluating Estimators | p. 330 · TOC inspected |
| §8.3 | Methods of Evaluating Tests | p. 382 · TOC inspected |
| §9.2 | Methods of Finding Interval Estimators | p. 420 · TOC inspected |
| §10.1 | Point Estimation | p. 467 · TOC inspected |

### An Introduction to Probability Theory and Its Applications, Volume I

| Reference | Subject | Printed page / status |
| --- | --- | --- |
| §III | Fluctuations in Coin Tossing and Random Walks | p. 67 · TOC inspected |
| §V | Conditional Probability and Stochastic Independence | p. 114 · TOC inspected |
| §IX | Random Variables; Expectation | p. 212 · TOC inspected |
| §XI | Integral-Valued Variables; Generating Functions | p. 264 · TOC inspected |
| §XIII | Recurrent Events; Renewal Theory | p. 303 · TOC inspected |
| §XV | Markov Chains | p. 372 · TOC inspected |
| §XVII | The Simplest Time-Dependent Stochastic Processes | start unverified · TOC inspected |

### Complex Analysis: An Introduction to the Theory of Analytic Functions of One Complex Variable

| Reference | Subject | Printed page / status |
| --- | --- | --- |
| §2 | Complex Functions | start unverified · TOC inspected |
| §3 | Analytic Functions as Mappings | start unverified · TOC inspected |
| §4 | Complex Integration | start unverified · TOC inspected |
| §5 | Series and Product Developments | p. 175 · TOC inspected |
| §6 | Conformal Mapping; Dirichlet's Problem | start unverified · TOC inspected |
| §7 | Elliptic Functions | start unverified · TOC inspected |
| §8 | Global Analytic Functions | start unverified · TOC inspected |

### Real Analysis

| Reference | Subject | Printed page / status |
| --- | --- | --- |
| §2.6 | Vitali’s Example of a Non-measurable Set | p. 45 · TOC inspected |
| §4.3 | The Integral of a Non-Negative Measurable Function | p. 70 · TOC inspected |
| §4.5 | Countable Additivity and Continuity of Integration | p. 78 · TOC inspected |
| §7.2 | The Inequalities of Young, H¨older, and Minkowski | p. 125 · TOC inspected |
| §17.4 | The Open Mapping and Closed Graph Theorems | p. 347 · TOC inspected |
| §18.2 | The Hahn-Banach Theorem | p. 361 · TOC inspected |
| §22.4 | Measure Preserving Transformations and Ergodicity | p. 463 · TOC inspected |

### Naive Set Theory

| Reference | Subject | Printed page / status |
| --- | --- | --- |
| §7 | Relations | p. 22 · TOC inspected |
| §8 | Functions | p. 25 · TOC inspected |
| §15 | The Axiom of Choice | p. 49 · TOC inspected |
| §16 | Zorn's Lemma | p. 52 · TOC inspected |
| §18 | Transfinite Recursion | p. 58 · TOC inspected |
| §22 | The Schroeder–Bernstein Theorem | p. 71 · TOC inspected |
| §24 | Cardinal Arithmetic | p. 77 · TOC inspected |

### An Introduction to the Theory of Numbers

| Reference | Subject | Printed page / status |
| --- | --- | --- |
| §V | Congruences and Residues | p. 57 · TOC inspected |
| §X | Continued Fractions | start unverified · TOC inspected |
| §XVI | The Arithmetical Functions | p. 302 · TOC inspected |
| §XVII | Generating Functions of Arithmetical Functions | p. 318 · TOC inspected |
| §XIX | Partitions | p. 361 · TOC inspected |
| §XXIV | Geometry of Numbers | p. 523 · TOC inspected |
| §XXV | Elliptic Curves | p. 549 · TOC inspected |

### Differential Geometry of Curves and Surfaces

| Reference | Subject | Printed page / status |
| --- | --- | --- |
| §2-5 | The First Fundamental Form; Area | p. 94 · TOC inspected |
| §4-4 | Parallel Transport. Geodesics. | p. 241 · TOC inspected |
| §4-5 | The Gauss-Bonnet Theorem and Its Applications | p. 267 · TOC inspected |
| §5-3 | Complete Surfaces. Theorem of Hopf-Rinow | p. 331 · TOC inspected |

### Introductory Functional Analysis with Applications

| Reference | Subject | Printed page / status |
| --- | --- | --- |
| §4.2 | Hahn-Banach Theorem | p. 213 · TOC inspected |
| §5.1 | Banach Fixed Point Theorem | p. 299 · TOC inspected |
| §7.1 | Spectral Theory in Finite Dimensional Normed Spaces | p. 364 · TOC inspected |
| §11.1 | Basic Ideas. States, Observables, Position Operator | p. 572 · TOC inspected |

### Principles of Mathematical Analysis

| Reference | Subject | Printed page / status |
| --- | --- | --- |
| §2 | Basic Topology | p. 22 · TOC inspected |
| §3 | Numerical Sequences and Series | p. 43 · TOC inspected |
| §6 | The Riemann–Stieltjes Integral | p. 110 · TOC inspected |
| §7 | Sequences and Series of Functions | p. 132 · TOC inspected |
| §9 | Functions of Several Variables | p. 190 · TOC inspected |
| §10 | Integration of Differential Forms | p. 230 · TOC inspected |
| §11 | The Lebesgue Theory | p. 282 · TOC inspected |

### Graph Theory

| Reference | Subject | Printed page / status |
| --- | --- | --- |
| §3.3 | Menger’s theorem* | p. 71 · TOC inspected |
| §6.1 | Circulations(⇤) | p. 156 · TOC inspected |
| §8.1 | Basic notions, facts and techniques* | p. 228 · TOC inspected |
| §11.1 | The notion of a random graph* | p. 340 · TOC inspected |
| §12.6 | Tree-decompositions and forbidden minors | p. 391 · TOC inspected |
| §12.7 | The graph minor theorem(⇤) | p. 396 · TOC inspected |

### Enumerative Combinatorics, Volume 1

| Reference | Subject | Printed page / status |
| --- | --- | --- |
| §1.9 | The Twelvefold Way | p. 71 · TOC inspected |
| §2.1 | Inclusion-Exclusion | p. 195 · TOC inspected |
| §3.7 | The Möbius Inversion Formula | p. 264 · TOC inspected |
| §4.7 | The Transfer-Matrix Method | p. 500 · TOC inspected |

## Inspected source passages and what they actually establish

A phrase or mechanism below was located in the connected PDF's text and examined for scope. **Inspected** does not mean that its proof was re-derived, experimentally reproduced or formally checked.

| Book / region | Mechanism worth retaining | Original |
| --- | --- | --- |
| **Chapter 16 geometric constructibility and Galois** | Field extension degrees obstruct some ruler-and-compass constructions. | [Algebra](https://drive.google.com/file/d/1r6Y76kY6T36HiBRPEV4IzFj8u24VQqtQ/view) |
| **§50 rank and nullity; §79 spectral theorem** | Rank and nullity concern linear maps; spectral conclusions depend on operator assumptions. | [Finite-Dimensional Vector Spaces](https://drive.google.com/file/d/1eFyex_8kmj5ZYSSQlpfQN8i-KGjPoxry/view) |
| **Chapter 9 fundamental group** | The text distinguishes constructing a homeomorphism from detecting failure with invariants. | [Topology](https://drive.google.com/file/d/1_a8QHxSed_yHkSJ7Rru01WhMak7-kf11/view) |
| **Chapters 6–7 sufficiency/Rao–Blackwell** | Sufficiency and conditioning are model-relative routes to estimator improvement. | [Statistical Inference](https://drive.google.com/file/d/16l7HK50HTLSDxGNZt31yLu__JsMLOqkm/view) |
| **Markov-chain and random-walk text** | Temporal dependence demands transition and recurrence structure rather than blindly independent trials. | [An Introduction to Probability Theory and Its Applications, Volume I](https://drive.google.com/file/d/1qY0vrM1KHzLD5x1cMjdio6LFIP_ge4Pb/view) |
| **Chapter 4 Cauchy formula and residues** | Contour integration reconstructs holomorphic values; residues encode isolated singular contributions. | [Complex Analysis: An Introduction to the Theory of Analytic Functions of One Complex Variable](https://drive.google.com/file/d/1WNsPRVM8YucXXZCYWLjtLx891LHIqoCg/view) |
| **Chapter 4 convergence of Lebesgue integrals** | Monotone and dominated convergence provide conditional exchange guarantees. | [Real Analysis](https://drive.google.com/file/d/13FxsPLoAJIm3LY5hNlfGP6rfdqwNsZ4W/view) |
| **§15 choice; §18 transfinite recursion** | Choice and well-ordering support existential reasoning and generalized recursion. | [Naive Set Theory](https://drive.google.com/file/d/1Rai3_jSkyOeFnqDncR2f62Bs2va0a5ZM/view) |
| **Chapter X continued fractions** | Continued fractions encode systematic rational approximation. | [An Introduction to the Theory of Numbers](https://drive.google.com/file/d/1-IfqhSU9Ro7oppMhY4ta0dBWpd7gU509/view) |
| **Chapter 4 Gauss–Bonnet discussion** | Local curvature can constrain global surface topology. | [Differential Geometry of Curves and Surfaces](https://drive.google.com/file/d/1Hjfdm25uPxJ_A8k7SGl9TIDkxlEdnuGX/view) |
| **§4.2 Hahn–Banach and §5.1 Banach fixed point** | Extension of functionals differs from contraction-based constructive existence. | [Introductory Functional Analysis with Applications](https://drive.google.com/file/d/1ArZFwHZVVMRxn64aPispU6hE21jL1Mu3/view) |
| **Chapter 7 uniform convergence** | A pointwise-vanishing sequence can have integrals that fail to converge accordingly. | [Principles of Mathematical Analysis](https://drive.google.com/file/d/1al-Lk0C8wHshwF3JTd4iB-glNI1hp-ny/view) |
| **Chapter 12 graph minors and treewidth** | Excluded minor structures relate to graph width and decomposition. | [Graph Theory](https://drive.google.com/file/d/1OaIGUFGzOcHMyUGanaP1G98izbHWYETC/view) |
| **§4.7 transfer-matrix method** | State transitions and linear-algebra powers encode combinatorial path counts. | [Enumerative Combinatorics, Volume 1](https://drive.google.com/file/d/1-Virg2U0k4ZDVtbYH7PlRAkLvHhC9yR3/view) |

## Cross-book operator compositions

The value of this shelf is not fourteen isolated summaries. Each chain shows where a capability crosses book boundaries **and the contract that determines whether that transfer works**.

| Reusable capability | Composition of sources | Contract and falsifying probe |
| --- | --- | --- |
| **Give one carrier set different laws and see what becomes possible** | Halmos set operations → Artin/Halmos algebraic structures → Munkres topology → Royden measurable spaces | Carrier, added structure, preserving map, invariant. **Check:** Use one set with two topologies and measure how continuity changes |
| **Collapse equivalent representations while preserving laws** | Halmos equivalence classes → Artin normal quotient and ring quotient → Munkres quotient topology | Compatibility of identification with the operation or topology. **Check:** Attempt quotient group multiplication using a nonnormal subgroup |
| **Use symmetry to avoid double-counting identical configurations** | Artin group actions → Stanley labeled/unlabeled counting → Diestel graph symmetries | Allowed symmetry group, orbit, stabilizer and labeling. **Check:** Count bead necklaces under rotation and then reflection |
| **Invert aggregate counts on structured hierarchies** | Stanley posets/§3.7 Möbius inversion → Hardy divisor sums and arithmetic functions | Locally finite poset and appropriate incidence convolution. **Check:** Recover primitive periodic strings from total periodic counts |
| **Turn local rules into global sequence counts** | Diestel graph walks → Stanley §4.7 finite-state transfer matrix → Feller generating functions | States, transitions and coefficient meaning. **Check:** Count forbidden-substring words by enumeration and matrix powers |
| **Recognize where finite matrix decomposition stops working** | Halmos eigen/spectral modes → Artin Jordan form → Kreyszig/Royden operator domains and spectra | Normality, boundedness, eigenbasis, operator domain. **Check:** Compare defective Jordan matrix to differentiation in an Lp domain |
| **Know exactly when limits commute with operations** | Rudin Ch 7 → Royden Lebesgue convergence → Kreyszig completeness | Uniformity, monotonicity, domination and closed limits. **Check:** Exhibit pointwise-zero spike with nonzero integral |
| **Connect local geometric invariants with global consequences** | Munkres loops/coverings → do Carmo Gauss–Bonnet/geodesics → Ahlfors conformal maps | Topology, orientation, boundary, analyticity and smoothness. **Check:** Compare total curvature and loops on a sphere and torus |
| **Differentiate computable, nonconstructive and impossible solutions** | Halmos choice/Zorn → Kreyszig Hahn–Banach and contractions → Artin algebraic impossibility | Choice axioms, contraction constants, field degrees. **Check:** Identify which proof actually yields an algorithm |
| **Build inference from probabilistic models without confusing the two** | Royden normalized measure → Feller random processes → Casella/Berger likelihood, sufficiency and tests | Sample law, independence, risk, power and interval coverage. **Check:** Simulate dependent samples and check nominal false-positive rates |
| **Transport integer questions into algebraic and analytic settings** | Hardy congruences/arithmetical functions → Artin ideals/Galois → Ahlfors analytic techniques | Ring, prime notion, field extension and convergence domain. **Check:** Contrast modular obstruction and ideal-factorization failure |
| **Replace exhaustive path search with structural obstructions** | Diestel matching, flow, cuts and minors → Stanley enumerative alternatives | Edge/vertex capacity, disjointness and permissible minor operations. **Check:** Construct many routes through a single small cut |

## From an unfamiliar frustration to an exact book region

| Starting frustration | Decisive structural question | Source destination |
| --- | --- | --- |
| A limit and integral disagree | Check the selected mechanism's assumptions against the original section | [Principles of Mathematical Analysis, §7, printed p. 132](https://drive.google.com/file/d/1al-Lk0C8wHshwF3JTd4iB-glNI1hp-ny/view) |
| A finite-state rule generates exponentially many strings | Check the selected mechanism's assumptions against the original section | [Enumerative Combinatorics, Volume 1, §4.7, printed p. 500](https://drive.google.com/file/d/1-Virg2U0k4ZDVtbYH7PlRAkLvHhC9yR3/view) |
| A network has many routes but very low capacity | Check the selected mechanism's assumptions against the original section | [Graph Theory, §6, printed p. 155](https://drive.google.com/file/d/1OaIGUFGzOcHMyUGanaP1G98izbHWYETC/view) |
| Someone reads p=0.01 as 99 percent chance of a hypothesis | Check the selected mechanism's assumptions against the original section | [Statistical Inference, §8, printed p. 373](https://drive.google.com/file/d/16l7HK50HTLSDxGNZt31yLu__JsMLOqkm/view) |
| A surface's global topology seems linked to curvature | Check the selected mechanism's assumptions against the original section | [Differential Geometry of Curves and Surfaces, §4-5, printed p. 267](https://drive.google.com/file/d/1Hjfdm25uPxJ_A8k7SGl9TIDkxlEdnuGX/view) |
| An unfamiliar ring does not factor integers uniquely | Check the selected mechanism's assumptions against the original section | [Algebra, §13](https://drive.google.com/file/d/1r6Y76kY6T36HiBRPEV4IzFj8u24VQqtQ/view) |
| A Cauchy approximation fails to converge in the space | Check the selected mechanism's assumptions against the original section | [Introductory Functional Analysis with Applications, §1.4, printed p. 25](https://drive.google.com/file/d/1ArZFwHZVVMRxn64aPispU6hE21jL1Mu3/view) |
| A continuous bijection lacks continuous inverse | Check the selected mechanism's assumptions against the original section | [Topology, §2, printed p. 73](https://drive.google.com/file/d/1_a8QHxSed_yHkSJ7Rru01WhMak7-kf11/view) |
| Two equal-size vector representations are claimed identical | Check the selected mechanism's assumptions against the original section | [Finite-Dimensional Vector Spaces, §50, printed p. 90](https://drive.google.com/file/d/1eFyex_8kmj5ZYSSQlpfQN8i-KGjPoxry/view) |
| A small sample summary may be statistically sufficient | Check the selected mechanism's assumptions against the original section | [Statistical Inference, §6, printed p. 271](https://drive.google.com/file/d/16l7HK50HTLSDxGNZt31yLu__JsMLOqkm/view) |

## Three high-information competence demonstrations

**1. Convergence and invalid inference.** Build an explicit family of functions whose pointwise limit and integrals disagree; test a domination or uniformity hypothesis that repairs the interchange. Trace Rudin Ch 7 to Royden Ch 4. A successful result is a computed counterexample, a correct repaired theorem and a hypothesis check—not a symbolic derivation that assumes the desired conclusion.

**2. Discrete problem factorization.** Define a small finite-state constraint such as binary strings avoiding a forbidden pattern. Build a directed-state automaton and transfer matrix; derive a recurrence/generating function and compare coefficients with exhaustive counts for small n. Then relate the same count to graph walks (Diestel) and restricted counting (Stanley). A useful test is the first n for which a modeling mistake creates a wrong count.

**3. Probability versus inference.** Generate Bernoulli data, then introduce dependence or sampling bias. Compare likelihood-based estimation, a sufficient summary, confidence intervals and hypothesis-test behavior. Relate probability axioms/limit properties (Feller), measure conditions (Royden) and frequentist operating characteristics (Casella/Berger). Test empirical interval coverage and false rejection under both assumed and violated models; do not mistake a pass under perfect assumptions for a result about reality.

## Evidence, acceptance and continuation

The canonical research file distinguishes **table-of-contents leads**, **OCR candidates**, **selected actual passages**, and **unreproduced mathematical/engineering competence**. At present, the 10 forward and 12 reverse routes were checked structurally, but no unfamiliar-user benchmark, full PDF viewer offset audit, or Kami deep-link validation has been completed. Apply FKEN-16A by comparing natural user frustrations and independently sampled important sections against direct TOC and full-text search; record false positives and wrong turns rather than scoring link counts.

Before future work: open [`investigation.json`](investigation.json) and [`glossary.json`](glossary.json), preserve all stable term/node IDs, and *extend only the uncertain passage or consequential question*. The glossary's 832 terms can grow without being forced onto existing questions. A cross-domain connection should preserve sense and hypotheses; a common word is not enough.
