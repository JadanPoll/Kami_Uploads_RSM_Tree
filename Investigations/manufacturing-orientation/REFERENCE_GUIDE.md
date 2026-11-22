# Manufacturing — reusable book reference guide

**Open this before starting another manufacturing investigation.** It is the persistent map of the current five-book library: book purposes, all 65 indexed chapter/part locators, inspected passages, and routes from ordinary problems to the right place in a book. Use the map instead of reopening and reindexing the same tables of contents for each new question.

**Source of truth:** [`investigation.json`](investigation.json) contains `sources`, `book_landscaplets`, `nodes`, `navigation_bridges`, and `book_factorization`. This Markdown file is a readable *index of that evidence*, not another independently maintained research corpus. Changes to the index belong in the canonical JSON first; extend this guide only where a human-facing shortcut is useful.

**Coverage contract:** 65 major chapter/part retrieval locations from book contents, plus 10 technical studies based on selected inspected sections. **This does not mean the whole books were read or their internal subheadings exhaustively indexed.** A TOC lead is not a conclusion. All sources are linked to their existing Drive/Kami files; the link opens the book, not necessarily the cited page.

## Which book should I open?

| Book | Best first question | Composable capabilities | What it does not settle |
| --- | --- | --- | --- |
| [Manufacturing Processes for Design Professionals](https://drive.google.com/file/d/1rGG9kMJndaCZcaaEpNGG9OJimjLTJm-1/view?usp=drivesdk) | Which transformation, tooling, material and production route can realize the geometry? | Form/cut/join/finish; mold release, setup/tooling, geometry, throughput and postprocessing | A process catalog does not size a flexure, guarantee strength, or price a real manufacturing quote. |
| [Functional Design for 3D Printing](https://drive.google.com/file/d/1aNSU5Shxl3JlKSQXEmp5jm8Cu5-EmThV/view?usp=drivesdk) | How must the part be redesigned for FFM rather than simply exported as CAD? | Anisotropy, orientation, support, split-and-join, fit, fastening, engineered features, slicer | FFM-specific practices do not automatically generalize to casting, molding, SLA/SLS or metal fatigue. |
| [Shigley's Mechanical Engineering Design](https://drive.google.com/file/d/1hWdX7Ea0928zOmgc2jKXj0NbeOvjn8iG/view?usp=drivesdk) | Will the part survive loads and repeated cycles, and fit into an assembly? | Stress/strain, materials, stiffness, static failure, fatigue, mechanical elements, GD&T | A theoretically sound design may still be impractical to fabricate or too expensive at the required quantity. |
| [Handbook of Compliant Mechanisms](https://drive.google.com/file/d/11-NSSa3M-ogZTo-XFaHbxzKKBN_F3bNl/view) | What motions and constraints can a flexure provide without a conventional joint? | Freedom/constraint topology (FACT), stiffness versus strength, pseudo-rigid-body approximation, rigid-body replacement | An elegant flexure still requires material life and fabrication-process validation. |
| [Mechanisms and Mechanical Devices Sourcebook](https://drive.google.com/file/d/1yzoMc0ZtYfXBOV__kZQG1rIhImg9unVN/view) | What device family converts a given input into the required motion, force, or timing? | Mechanical advantage, linkages, gears, cams, Geneva indexers, clutches, drive systems | Catalog examples establish possibilities, not a final load-rated, toleranced, manufactured design. |

**Useful factoring:** intended function/motion → constraints and loads → candidate mechanism → materials/geometry → fabrication route → assembly/tolerances → inspection/life → production economics. This is a dependency map, not a mandatory linear sequence. An unexpected failed part can enter at any stage.

## Problem → relevant book passage

| Actual question or frustration | Consequential distinction | First location to retrieve | Current evidence status |
| --- | --- | --- | --- |
| Repeatedly bent metal wire breaks | Cyclic strain/fatigue vs overload | Shigley Ch. 6 p. 297; Chs. 3 and 5 pp. 91, 253 | TOC leads only; not yet examined in detail |
| 3D-printed latch/clip snaps | Across-layer adhesion vs flexure strain | Smyth pp. 18–21, 94–95; Howell pp. 8–11; Smyth Ch. VII p. 136 | Selected passages inspected; Ch. VII remains a TOC lead |
| Want a hinge without pins | Allowed motion, undesirable stiffness, peak strain | Howell pp. 8–11, 82–89, 111–120 | Inspected |
| Printed parts fit in CAD but jam | Clearance/compensation vs datum/form/position error | Smyth Ch. V p. 116; Shigley Ch. 20 p. 995 | Inspected selected sections |
| Machine wobbles or won't return | Off-axis freedoms vs joint clearance vs elastic hysteresis | Howell Ch. 6 pp. 82–89; Shigley Ch. 20 p. 995; Sclater Ch. 1 pp. 2–8 | Selected inspected sections; no diagnosis guaranteed |
| Tiny force must lift heavy object | Force multiplication necessarily trades output travel (and losses) | Sclater pp. 2–8; Shigley Ch. 18 p. 953 | Sclater inspected; Shigley TOC lead |
| Wheel moves one step, pauses, repeats | Intermittent indexing/dwell vs continuously controlled motion | Sclater pp. 192–197; Howell pp. 82–89 for guidance | Inspected |
| Hollow shape or inaccessible interior | Tool release vs expendable mold/core vs layer build | Manufacturing Processes PDF pp. 127–129 and 239–241 | Inspected |
| Cut without thermal edge damage | Waterjet erosion vs heat-based cut; kerf and support remain | Manufacturing Processes PDF pp. 279–281 | Inspected |
| Print bridge droops or tall print tips | Overhang vs bridging span vs bed contact | Smyth Ch. II p. 40; selected pp. 46–61 | Partly inspected; bridge specifics still a targeted lead |
| Ten prototypes or ten thousand units | Tooling/revision/setup vs cycle/finishing economics | Manufacturing Processes PDF pp. 57–59, 127–129, 239–241; Smyth Ch. VIII p. 154 | Process passages inspected; no break-even calculation |
| Build a device without a machine shop | Sheet cutting, printing as service, assembly, inspection contract | Manufacturing Processes PDF pp. 279–281; Smyth Chs. II/VI; Shigley Ch. 20 | Mixed inspected and TOC leads |

The canonical `curiosity_atlas.entries` and `navigation_bridges` support additional formulations and conditions. Routes above are a shortcut; they are **not** a separate encyclopedia of answers.

## Known inspected sections: reopen these first

These references were previously inspected as recorded in canonical technical nodes. They are **local evidence for the specified example**, not proof for every failure or process variant.

| Book | Source location | Technical claim/study | Canonical node |
| --- | --- | --- | --- |
| Manufacturing Processes for Design Professionals | Injection Molding; PDF pages 57–59 | How does injection molding exchange tooling investment for repeatable plastic parts? | `MFG-PROC-INJECTION` |
| Manufacturing Processes for Design Professionals | Sand Casting; PDF pages 127–129 | Why can expendable sand molds create large, internally complex metal parts? | `MFG-PROC-SAND` |
| Manufacturing Processes for Design Professionals | Rapid Prototyping (SLA/SLS); PDF pages 239–241 | What do layer-building processes gain and sacrifice by avoiding a custom mold? | `MFG-PROC-LAYERS` |
| Manufacturing Processes for Design Professionals | Water Jet Cutting and glass-disc case; PDF pages 279–281 | Why can waterjet cutting reach materials that heat-based cutting may damage? | `MFG-PROC-WATERJET` |
| Functional Design for 3D Printing | Anisotropy; print orientation/design refactoring; support; layer fusion; Printed pages 18–21, 46–49, 61, 94–95 | How can reorienting and splitting an FFM part change strength, time and reliability? | `MFG-FFM-ORIENT` |
| Functional Design for 3D Printing | Designing for Fit; Printed chapter V, beginning p. 116 | How do tolerances turn an ideal CAD shape into a manufacturable assembly? | `MFG-TOLERANCE` |
| Functional Design for 3D Printing | Ch. VI Fastening and Joinery, targeted reading pending; Printed chapter starts p. 124 | How do joint geometry, fastening, bonding and tolerances determine assembly reliability? | `MFG-JOINING` |
| Shigley's Mechanical Engineering Design | Geometric Dimensioning and Tolerancing; Printed chapter 20, beginning p. 995 | How do tolerances turn an ideal CAD shape into a manufacturable assembly? | `MFG-TOLERANCE` |
| Shigley's Mechanical Engineering Design | Ch. 6 Fatigue Failure Resulting from Variable Loading — targeted study pending; Printed chapter starts p. 297 | How do load cycles and local strain concentrations govern fatigue life? | `MFG-FAILURE-CYCLIC` |
| Shigley's Mechanical Engineering Design | Chs. 3 and 5 — load/stress analysis and static failure, targeted reading pending; Printed chapters start pp. 91 and 253 | How do load paths, stress concentration and material strength govern single-event fracture? | `MFG-FAILURE-STATIC` |
| Shigley's Mechanical Engineering Design | Chs. 8–9 removable and permanent joints, targeted reading pending; Printed chapters start pp. 433 and 497 | How do joint geometry, fastening, bonding and tolerances determine assembly reliability? | `MFG-JOINING` |
| Handbook of Compliant Mechanisms | Ch. 1: Stiffness and strength; flexible yet strong; Printed pp. 8–11 | When should elastic deformation replace pin joints or articulated rigid links? | `MFG-FUNC-COMPLIANT` |
| Handbook of Compliant Mechanisms | Ch. 8: Rigid-body replacement and bicycle derailleur case; Printed pp. 111–120 | When should elastic deformation replace pin joints or articulated rigid links? | `MFG-FUNC-COMPLIANT` |
| Handbook of Compliant Mechanisms | Ch. 6: freedom/constraint spaces and FACT synthesis; Printed pp. 82–89 | How can desired degrees of freedom generate candidate flexure architectures? | `MFG-FUNC-DOF` |
| Mechanisms and Mechanical Devices Sourcebook | Ch. 1: efficiency, mechanical advantage, velocity ratio, levers and linkages; Printed pp. 2–8 | How do mechanical advantage and motion ratios constrain a mechanism's output? | `MFG-FUNC-RIGID` |
| Mechanisms and Mechanical Devices Sourcebook | Ch. 7: Twenty Geneva Drives and modified Geneva drives; Printed pp. 192–197 | How can continuous rotation produce an intermittent output with controlled dwell? | `MFG-FUNC-INDEX` |

## Permanent chapter/part maps

**How to read the tables:** `Chapter`/`Part` identifies the source's own organization; `Start` is the recorded **printed page number** unless the book-specific heading says otherwise. `—` means a starting page was not established. The **use** column is the retrieval reason already indexed in the canonical data. For each chapter, the table records *where to look*; inspected subpassages are enumerated above.

### Manufacturing Processes for Design Professionals

**Book:** [Open in Drive/Kami](https://drive.google.com/file/d/1rGG9kMJndaCZcaaEpNGG9OJimjLTJm-1/view?usp=drivesdk) · **ID:** `BOOK-MFG-PROCESSES` · **Page scheme:** major part titles verified, start pages not established.

**What this book supplies:** Form/cut/join/finish; mold release, setup/tooling, geometry, throughput and postprocessing. **Known coverage:** selected sections inspected, broad catalog not exhaustively read.

**Index provenance:** Table-of-contents sections indexed for retrieval; only individually cited studies count as inspected technical evidence.

| Chapter / part | Section | Start | Retrieve when… | Linked studies |
| --- | --- | ---: | --- | --- |
| Part 1 | Forming technology | — | Choosing between molding, casting and additive processes; compare tooling and part geometry | `MFG-PROC-INJECTION`, `MFG-PROC-SAND` |
| Part 2 | Cutting technology | — | Cutting or shaping stock while considering kerf, heat and fixturing | `MFG-PROC-WATERJET` |
| Part 3 | Joining technology | — | Designing assemblies from separately made parts; matching joining process to materials | — |
| Part 4 | Finishing technology | — | When functional surface, edge or appearance requirements need post-processing | — |
| Part 5 | Materials | — | Choosing which material properties enable a manufacturable function | — |

**Special PDF-position anchors:** Injection Molding PDF pp. **57–59**; Sand Casting **127–129**; SLA/SLS Rapid Prototyping **239–241**; Water Jet Cutting **279–281**. These were inspected; no reliable printed-page start for the book's five top-level parts has been established.

### Functional Design for 3D Printing

**Book:** [Open in Drive/Kami](https://drive.google.com/file/d/1aNSU5Shxl3JlKSQXEmp5jm8Cu5-EmThV/view?usp=drivesdk) · **ID:** `BOOK-FFF` · **Page scheme:** printed book page.

**What this book supplies:** Anisotropy, orientation, support, split-and-join, fit, fastening, engineered features, slicer. **Known coverage:** several selected sections inspected, not the full text.

**Index provenance:** Table-of-contents sections indexed for retrieval; only individually cited studies count as inspected technical evidence.

| Chapter / part | Section | Start | Retrieve when… | Linked studies |
| --- | --- | ---: | --- | --- |
| I | The Medium | 10 | Diagnosing layer-direction strength, shell/infill or porosity | `MFG-FFM-ORIENT` |
| II | Designing for FFM | 40 | Adapting geometry, orientation and supports for a printer | `MFG-FFM-ORIENT` |
| III | Design for Strength | 76 | Preventing a printed part from breaking under realistic loads | — |
| IV | Design Paradigms | 106 | Revising shape and design strategy around FFM behavior | — |
| V | Designing for Fit | 116 | Making two printed components fit or slide | `MFG-TOLERANCE` |
| VI | Fastening and Joinery | 124 | Choosing how printed parts connect or come apart | — |
| VII | Functional Elements and Engineered Features | 136 | Designing hinges, latches and useful functional features | — |
| VIII | Understanding the Slicer | 154 | Understanding why slicer settings change the manufactured part | — |

### Shigley's Mechanical Engineering Design

**Book:** [Open in Drive/Kami](https://drive.google.com/file/d/1hWdX7Ea0928zOmgc2jKXj0NbeOvjn8iG/view?usp=drivesdk) · **ID:** `BOOK-SHIGLEY` · **Page scheme:** printed book page.

**What this book supplies:** Stress/strain, materials, stiffness, static failure, fatigue, mechanical elements, GD&T. **Known coverage:** one substantive chapter section read; further contents available.

**Index provenance:** Table-of-contents sections indexed for retrieval; only individually cited studies count as inspected technical evidence.

| Chapter / part | Section | Start | Retrieve when… | Linked studies |
| --- | --- | ---: | --- | --- |
| 1 | Introduction to Mechanical Engineering Design | 3 | Translating a practical requirement into an engineering design target | — |
| 2 | Materials | 39 | Choosing materials for required properties | — |
| 3 | Load and Stress Analysis | 91 | Understanding force paths and local stresses | — |
| 4 | Deflection and Stiffness | 179 | Distinguishing unwanted deformation from strength limits | — |
| 5 | Failures Resulting from Static Loading | 253 | Diagnosing failure under a single or static load | — |
| 6 | Fatigue Failure Resulting from Variable Loading | 297 | Diagnosing failure after many load cycles | — |
| 7 | Shafts and Shaft Components | 385 | Designing rotating shafts and their load paths | — |
| 8 | Screws, Fasteners, and the Design of Nonpermanent Joints | 433 | Selecting bolts, screws and removable joint interfaces | — |
| 9 | Welding, Bonding, and the Design of Permanent Joints | 497 | Selecting permanent joints and bonding routes | — |
| 10 | Mechanical Springs | 537 | Storing energy or producing restoring force with springs | — |
| 11 | Rolling-Contact Bearings | 589 | Reducing friction and supporting rotating components | — |
| 12 | Lubrication and Journal Bearings | 637 | Reasoning about sliding-bearing loads and lubrication | — |
| 13 | Gears—General | 697 | Using gear trains to exchange speed for torque | — |
| 14 | Spur and Helical Gears | 757 | Designing common gear geometry and load limits | — |
| 15 | Bevel and Worm Gears | 809 | Redirecting rotational axes and designing worm/bevel gearing | — |
| 16 | Clutches, Brakes, Couplings, and Flywheels | 847 | Stopping, engaging or coupling rotating machinery | — |
| 17 | Flexible Mechanical Elements | 899 | Transmitting mechanical power using flexible elements | — |
| 18 | Power Transmission Case Study | 953 | Designing and assessing a complete power transmission path | — |
| 19 | Finite-Element Analysis | 973 | Exploring stress and deformation with simulation | — |
| 20 | Geometric Dimensioning and Tolerancing | 995 | Specifying which geometric variations are functionally acceptable | `MFG-TOLERANCE` |

### Handbook of Compliant Mechanisms

**Book:** [Open in Drive/Kami](https://drive.google.com/file/d/11-NSSa3M-ogZTo-XFaHbxzKKBN_F3bNl/view) · **ID:** `BOOK-COMPLIANT` · **Page scheme:** printed book page.

**What this book supplies:** Freedom/constraint topology (FACT), stiffness versus strength, pseudo-rigid-body approximation, rigid-body replacement. **Known coverage:** several substantive sections read; illustrated library not exhaustively indexed.

**Index provenance:** Table-of-contents sections indexed for retrieval; only individually cited studies count as inspected technical evidence.

| Chapter / part | Section | Start | Retrieve when… | Linked studies |
| --- | --- | ---: | --- | --- |
| 1 | Introduction to Compliant Mechanisms | 3 | Distinguishing elastic movement, stiffness and strength | `MFG-FUNC-COMPLIANT` |
| 2 | Using the Handbook to Design Devices | 15 | Selecting a compliant mechanism architecture for a function | — |
| 3 | Analysis of Flexure Mechanisms in the Intermediate Displacement Range | 29 | Estimating deflection and unwanted parasitic motion | — |
| 4 | Modeling of Large Deflection Members | 45 | Investigating large elastic deflection beyond small-motion approximations | — |
| 5 | Using Pseudo-Rigid Body Models | 55 | Using an approximate rigid-link model for flexure behavior | — |
| 6 | Synthesis through Freedom and Constraint Topologies | 79 | Synthesizing intended motions while constraining unwanted freedoms | `MFG-FUNC-DOF` |
| 7 | Synthesis through Topology Optimization | 93 | Finding alternative compliant shapes through topology optimization | — |
| 8 | Synthesis through Rigid-Body Replacement | 109 | Replacing selected rigid joints or links with flexible members | `MFG-FUNC-COMPLIANT` |
| 9 | Synthesis through Use of Building Blocks | 123 | Combining reusable flexure building blocks | — |
| 10 | Library Organization | 149 | Looking up compliant designs by functional behavior | — |
| 11 | Elements of Mechanisms | 155 | Finding reusable compliant element patterns | — |
| 12 | Mechanisms | 193 | Finding whole compliant mechanism patterns | — |
| 13 | Example Application | 277 | Studying an application of compliant mechanism design | — |

### Mechanisms and Mechanical Devices Sourcebook

**Book:** [Open in Drive/Kami](https://drive.google.com/file/d/1yzoMc0ZtYfXBOV__kZQG1rIhImg9unVN/view) · **ID:** `BOOK-MECHANISMS` · **Page scheme:** printed book page.

**What this book supplies:** Mechanical advantage, linkages, gears, cams, Geneva indexers, clutches, drive systems. **Known coverage:** selected technical sections read; large mechanism compendium not exhaustively indexed.

**Index provenance:** Table-of-contents sections indexed for retrieval; only individually cited studies count as inspected technical evidence.

| Chapter / part | Section | Start | Retrieve when… | Linked studies |
| --- | --- | ---: | --- | --- |
| 1 | Basics of Mechanisms | 1 | Relating forces, displacements, power, linkages and gear ratios | `MFG-FUNC-RIGID` |
| 2 | Motion Control Systems | 21 | Selecting actuation and feedback mechanisms for controlled motion | — |
| 3 | Stationary and Mobile Robots | 49 | Examining physical-motion capabilities in robotics | — |
| 4 | Mechanisms for Renewable Power Generation | 73 | Using mechanical conversion for renewable power generation | — |
| 5 | Linkages: Drives and Mechanisms | 89 | Finding linkage alternatives for a particular motion path | — |
| 6 | Gears: Devices, Drives, and Mechanisms | 131 | Changing speed, direction and torque using gears | — |
| 7 | Cam, Geneva, and Ratchet Drives and Mechanisms | 179 | Producing timed movement, indexing, dwell and ratcheting | `MFG-FUNC-INDEX` |
| 8 | Clutches and Brakes | 211 | Engaging, releasing, stopping or overrunning a drive | — |
| 9 | Latching, Fastening, and Clamping Devices and Mechanisms | 237 | Implementing latch, clamp and release functions | — |
| 10 | Chain and Belt Devices and Mechanisms | 261 | Transmitting power through chains and belts | — |
| 11 | Spring and Screw Devices and Mechanisms | 279 | Generating restoring forces, clamping or movement using springs and screws | — |
| 12 | Shaft Couplings and Connections | 301 | Joining rotating shafts with alignment or compliance constraints | — |
| 13 | Motion-Specific Devices, Mechanisms, and Machines | 323 | Finding mechanisms tailored to specific movement requirements | — |
| 14 | Packaging, Conveying, Handling, and Safety Mechanisms and Machines | 381 | Moving, feeding, sorting and handling products in manufacturing | — |
| 15 | Torque, Speed, Tension, and Limit Control Systems | 419 | Controlling speed, torque, tension or travel limits | — |
| 16 | Instruments and Controls: Pneumatic, Hydraulic, Electric, and Electronic | 447 | Integrating pneumatic, hydraulic, electric and electronic control | — |
| 17 | 3D Digital Prototypes and Simulation | 477 | Simulating and checking mechanism behavior before construction | — |
| 18 | Rapid Prototyping | 487 | Making prototype functional parts without production-scale tooling | — |
| 19 | New Directions in Mechanical Engineering | 501 | Scanning emerging mechanical design alternatives | — |

## Combine books instead of multiplying topic trees

**Choose a fabrication process.** Process families — Manufacturing Processes (Form/Cut/Join/Finish) → Geometry/orientation — Smyth (if FFM) → Stress/fit/quality limits — Shigley → Real supplier quotations and trial parts: not supplied by the books.

**Make an articulated device.** Specify motion and force — Sclater → Contrast rigid pin mechanisms with flexures — Howell → Check material stresses, cycles and fits — Shigley → Choose printing, cutting or molding and measure real motion — Smyth/process catalog.

**Make a strong printable clip.** Determine breakage mechanism — Smyth or Shigley (metal versus printed polymer) → Select flexure topology and strain limits — Howell → Redesign orientation/support/joints — Smyth → Perform load and life tests: future evidence.

**Make many similar parts.** Identify tooling/consumable/digital path — Manufacturing Processes → Identify tolerance and load requirements — Shigley → Quantify setup, cycle, finishing, rejection and redesign via quotes or trials → Revisit architecture when quantity changes.

**Make assembly fit.** Define datums, allowed dimensional variation — Shigley Ch. 20 → Compare printer compensation and fitting strategies — Smyth Ch. V → Compare monolithic vs split-and-joined build → Inspect multiple manufactured samples.

## How to add knowledge next time (without another indexing pass)

1. **Lookup first:** search this guide by ordinary symptom, mechanism, chapter, or named book; consult `investigation.json` for the exact source IDs, chapter locators, case nodes, and conditional bridges. Do not reload/reconstruct a full book TOC.
2. **Reuse the source identity:** a new curiosity should ordinarily reference an existing `navigation_bridge`, `node`, and `book_landscaplets` section. Create no new chapter record when only its wording or application changed.
3. **If the relevant passage is already inspected:** reopen the bounded printed/PDF page and check whether the existing mechanism applies to the new constraints. Cite the existing study node rather than copying its explanation.
4. **If the index leads only to a chapter:** open that *one section*, inspect a useful worked example/derivation, record what it does and does not establish, the exact page scheme/range, and a stable source-linked study in canonical `investigation.json`. Update the human shortcut here if it unlocks a common question.
5. **If acquiring a new book:** index its own meaningful chapters and starting pages once into `sources` + `book_landscaplets`; record edition, file link, page scheme, missing areas and overlap with existing books. Add its summary and chapter map here. Do **not** rescan the prior books.
6. **Audit failures, not counts:** if someone cannot navigate from a natural question to the right passage, identify the smallest missing entry, conditional distinction, source anchor or cross-book relationship. Counts of links and successful JSON lookups are not evidence of human usability.

### Book gaps worth recording rather than silently filling

- **Manufacturing Processes for Design Professionals:** inspected — Injection molding; sand casting; rapid prototyping; waterjet cutting; additional candidate coverage — Other forming, joining, finishing families, material and scale distinctions.
- **Functional Design for 3D Printing:** inspected — Anisotropy; print orientation; shell/infill; support; layer fusion; fitting; additional candidate coverage — Fit, fastening, hinges, latches, structural features and slicer behavior.
- **Shigley's Mechanical Engineering Design:** inspected — GD&T contract, Ch. 20; additional candidate coverage — Material selection, stress/fatigue, joints, gearing, loads, machine elements and failures.
- **Handbook of Compliant Mechanisms:** inspected — Stiffness versus strength; FACT synthesis; rigid-body replacement; catalog classification limitation; additional candidate coverage — Topology optimization, building-block synthesis, pseudo-rigid body methods, library of flexures and examples.
- **Mechanisms and Mechanical Devices Sourcebook:** inspected — Mechanical advantage, force/travel; Geneva indexing and variants; additional candidate coverage — Kinematic linkages, cams, gear trains, clutches, robotic actuation, drives and controls.

**Do not infer:** TOC chapter location = inspected mechanism, printed page = PDF screen offset, or source relevance = proven practical applicability. A new investigation should consult this durable index and deepen it *only where evidence adds something consequential*.
