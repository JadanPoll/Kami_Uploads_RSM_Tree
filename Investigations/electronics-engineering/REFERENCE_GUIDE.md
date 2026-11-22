# Electronics engineering — persistent book reference guide

**Read this before opening or reindexing another electronics book.** This research collection already contains **3 exact PDFs**, **50 major chapters**, **1133 numbered/curated subsection locators** and **16 Art of Electronics appendices**. Detailed locators are maintained once in [`investigation.json`](investigation.json), not repeatedly rebuilt per question. This file is a *human retrieval interface* to those locators and their technical consequences.

**Source folder:** [Electronics engineering book shelf](https://drive.google.com/drive/folders/1_6JNMHCpsh5W5qdrg2Oea-CmZ1EUvm3F) · **Vocabulary:** [`glossary.json`](glossary.json), 639 term identities across 11 families. The glossary can grow independently of questions or passage links: an unfamiliar concept is already worth discovering.

**Page accuracy:** Power and Art printed starts are parsed from their editions' TOCs; these are **not direct PDF screen offsets**. Johnson/Graham's PDF has degraded OCR; section names and printed starts marked as OCR leads should be confirmed in the actual book before relying on an exact page. A chapter locator is not evidence its worked circuit was inspected or experimentally reproduced.

## Three books, three complementary questions

| Book | Distinctive function | Why this is not redundant |
| --- | --- | --- |
| [The Art of Electronics, 3rd ed. (2015)](https://drive.google.com/file/d/1gn0Ry4DXyNha41fjSmAX17YxiMOWH-vv/view?usp=drivesdk) | How do I actually assemble, bias, measure, choose components and troubleshoot a circuit? | Practical circuit blocks, noise, measurement, mixed signal, power and embedded examples |
| [High-Speed Digital Design: A Handbook of Black Magic](https://drive.google.com/file/d/1bY6RnLH7OgcZ6LGGiv6fwNnfY-W128Az/view?usp=drivesdk) | What changes when wires, clock edges, packages, return paths and probes have real geometry? | Distributed signal behavior, measurement artefacts, terminations, coupling, PCB and clock design |
| [Fundamentals of Power Electronics, 3rd ed. (2020)](https://drive.google.com/file/d/1YH4DDlxKP4WqYoq_W6QFJ8r-DsZXk9-o/view?usp=drivesdk) | How do switching devices transfer energy, remain efficient and achieve stable regulation? | Converter analysis, nonideal losses, magnetics, feedback, sampling and higher-power conversion |

**Key factorization:** useful behavior → circuit representation/bias → physical edge/return/rail → regulator/magnetics → instrumented operational envelope. A circuit can pass nominal DC and still fail on a 1 ns edge, a load transient, a distorted oscilloscope measurement, or a magnetic saturation condition.

## Problem → mechanism → actual source

| What I observe or want | Critical distinction to investigate | Retrieve first | Evidence status |
| --- | --- | --- | --- |
| Slow clock, but PCB traces ring | Clock period versus edge rise time/flight time | HSDD Ch. 1 §1.3; Ch. 4 | §1.3 examined |
| Oscilloscope makes the waveform ugly | Probe-loop pickup versus real signal vs probe loading | HSDD Ch. 3 §§3.2–3.4, pp. 86–95 | Probe discussion examined |
| Signal bounces off end of a cable | Characteristic impedance, source/end termination | HSDD Ch. 4 §4.3.3; Ch. 6 | Source termination passage examined |
| A trace crossing split ground becomes unreliable | DC ground continuity versus high-frequency return inductance | HSDD Ch. 5 §5.1, p. 189 | Inspected |
| Another output toggling corrupts this pin | Mutual coupling versus package ground bounce | HSDD Ch. 2 §2.4, p. 66; Ch. 5 §§5.2–5.7 | Ground bounce inspected; cross-talk sections TOC |
| A fast connector or via causes new failures | Return continuity versus interconnect impedance | HSDD Ch. 7 §§7.2–7.4; Ch. 9 §9.5 | Chapter/section leads |
| Regulator runs very hot | Pass-device dissipation versus switched transfer losses | Art Ch. 9 §9.6.1, p. 636; Power Ch. 3 | Art's linear/switching analysis inspected |
| Need lower or higher DC voltage | Buck/boost topology, duty cycle, inductor ripple | Power Ch. 2 §2.2, p. 18; Ch. 6 | Small-ripple source passage inspected |
| Light-load converter behaves differently | Continuous-conduction mode versus zero-current interval | Power Ch. 5 p. 135; Ch. 15 p. 585 | TOC leads |
| Power supply oscillates after a load step | Plant poles/zeros versus loop compensation/measurement | Power Chs. 7–9 pp. 215–347 | TOC leads |
| Boost output initially moves backward | RHP zero versus normal minimum-phase response | Power Ch. 8 §8.2.3, p. 316 | TOC lead; detailed mechanism still to examine |
| Digital power controller is unstable | Sample delay, quantization and Z-domain model | Power Ch. 19 p. 805 | TOC lead |
| Inductor/transformer heats or saturates | Core flux versus skin/proximity winding losses | Power Chs. 10–12 pp. 409–485 | TOC leads |
| Isolated power supply needed | Voltage conversion versus a rated isolation boundary | Power Ch. 6 §6.3 p. 178; Art Ch. 9 | TOC leads; do not infer safety certification |
| Sensor gets noisier when connected | Input current noise × source impedance versus Johnson/voltage noise | Art Ch. 8 §8.3.1, Ch. 5 | Noise discussion inspected |
| A decoupling capacitor seems ineffective | Capacitance value versus ESR/ESL and mounting loop | Art Ch. 15 §15.2 pp. 1054–1056; HSDD Ch. 8 | Art's MCU decoupling case inspected |
| A high-bit-count ADC still gives bad data | Quantization versus noise/reference/aliasing | Art Ch. 13 p. 879 | TOC lead |
| Choosing analog op-amp vs MCU vs FPGA | Fixed physical processing versus software configurability | Art Chs. 4, 11, 14–15 | TOC leads |
| Need to debug an assembled board | Probe/reference/power safety, return and full system integration | HSDD Chs. 3, 5; Art Appendices J/O; Art Ch. 15 | Mixed inspected and TOC leads |
| Want useful lab confidence | Representative load/temperature/edge/noise/thermal outcomes | HSDD Ch. 3; Art Chs. 8–9; Power Chs. 3 and 9 | Evaluation route; no working hardware claimed |

## Indexed book 1: The Art of Electronics

[Open the exact Drive PDF](https://drive.google.com/file/d/1gn0Ry4DXyNha41fjSmAX17YxiMOWH-vv/view?usp=drivesdk) · **Third Edition (2015)**. Source catalog: `book_landscaplets[source_id=ART-3]`. The table maps all 15 principal chapters and their printed page starts; the canonical JSON holds 726 section starts.

| Chapter | Title | Printed start | Use when… |
| ---: | --- | ---: | --- |
| 1 | Foundations | 1 | Electrical quantities, passive elements, signals, basic measurement and circuit models |
| 2 | Bipolar Transistors | 71 | Current sources, amplifiers, differential pairs, feedback and switching |
| 3 | Field-Effect Transistors | 131 | JFET/MOSFET behavior, switches, power stages and FET amplifiers |
| 4 | Operational Amplifiers | 223 | Feedback, real op-amp limitations, gain and nonlinear circuitry |
| 5 | Precision Circuits | 292 | Input offsets, instrumentation amplifiers, matching and precision references |
| 6 | Filters | 391 | Passive/active filter families and amplitude/phase shaping |
| 7 | Oscillators and Timers | 425 | Relaxation/tuned oscillators, timers and pulse generators |
| 8 | Low-Noise Techniques | 473 | Source/voltage/current noise, measurement and noise-aware design |
| 9 | Voltage Regulation and Power Conversion | 594 | Linear/switching regulators, power devices, biasing, batteries |
| 10 | Digital Logic | 703 | Logic families, gates, flip-flops, counters and synchronization |
| 11 | Programmable Logic Devices | 764 | PAL/PLA/FPGA examples, HDL and programmable alternatives |
| 12 | Logic Interfacing | 790 | Driving loads and levels, comparator and cable/sensor interfaces |
| 13 | Digital meets Analog | 879 | ADC, DAC, PLL and mixed-signal signal conversion |
| 14 | Computers, Controllers, and Data Links | 989 | Computer buses, I/O, serial interfaces and interrupts |
| 15 | Microcontrollers | 1053 | Integrated firmware + circuit designs and physical constraints |

**Appendices (all 16 indexed):**

| Ref | Title | Printed page | Ref | Title | Printed page |
| --- | --- | ---: | --- | --- | ---: |
| A | Math Review | 1097 | B | How to Draw Schematic Diagrams | 1101 |
| C | Resistor Types | 1104 | D | Thevenin's Theorem | 1107 |
| E | LC Butterworth Filters | 1109 | F | Load Lines | 1112 |
| G | The Curve Tracer | 1115 | H | Transmission Lines and Impedance Matching | 1116 |
| I | Television: A Compact Tutorial | 1131 | J | SPICE Primer | 1146 |
| K | Where Do I Go to Buy Electronic Goodies? | 1150 | L | Workbench Instruments and Tools | 1152 |
| M | Catalogs, Magazines, Databooks | 1153 | N | Further Reading and References | 1154 |
| O | The Oscilloscope | 1158 | P | Acronyms and Abbreviations | 1166 |

### High-value Art subsection shortcuts

| § | Book heading | Printed page |
| --- | --- | ---: |
| 2.2.7 | Common-emitter amplifier | 87 |
| 2.3.7 | Current mirrors | 101 |
| 3.5 | Power MOSFETs | 187 |
| 4.1 | Introduction to op-amps – the “perfect component” | 223 |
| 4.2 | Basic op-amp circuits | 225 |
| 5.14 | Difference amplifier | 348 |
| 6.1 | Introduction | 391 |
| 7.2 | Timers | 457 |
| 8.3.1 | Voltage noise, en | 481 |
| 8.3.2 | Current noise in | 483 |
| 9.3 | Fully integrated linear regulators | 600 |
| 9.6.1 | Linear versus switching | 636 |
| 9.6.5 | Step-down (buck) converter | 642 |
| 9.8 | A real-world switcher example | 665 |
| 10.4.4 | Synchronizer | 737 |
| 11.2.3 | The FPGA | 768 |
| 12.9 | Digital signals and long wires | 856 |
| 12.10 | Driving Cables | 858 |
| 13.5.1 | Digitizing: aliasing, sampling rate, and sampling depth | 900 |
| 13.9 | ADCs IV: delta–sigma | 922 |
| 14.7.2 | I2C 2-wire interface (“TWI”) | 1034 |
| 14.3.7 | Interrupts | 1005 |
| 15.2 | Design example 1: suntan monitor (V) | 1054 |
| 15.9 | Development environment | 1086 |

**Examined source distinctions:** *linear versus switch* regulation (9.6.1) makes the pass-device heat proportional to current × voltage drop; the noise chapter separates source Johnson noise, amplifier voltage noise and amplifier current noise acting through source impedance; the MCU design in Ch. 15 distinguishes analog rail decoupling, parallel capacitor impedance and actual sampled precision. The source's selected parts tables are a historical snapshot, not current purchase recommendations.

## Indexed book 2: High-Speed Digital Design

[Open the exact Drive PDF](https://drive.google.com/file/d/1bY6RnLH7OgcZ6LGGiv6fwNnfY-W128Az/view?usp=drivesdk) · Howard W. Johnson and Martin Graham. **12 chapters** and **61 selected subsection locators**. The scan's OCR is degraded; entries with missing pages are deliberately left unverified, not guessed.

| Chapter | Title | Printed start | Retrieve for |
| ---: | --- | ---: | --- |
| 1 | Fundamentals | 1 | Rise-time, distance, lumped versus distributed, capacitance and inductance |
| 2 | High-Speed Properties of Logic Gates | 37 | Power, speed and package-induced noise |
| 3 | Measurement Techniques | 83 | Probes, ground leads, loading, margins and clock observations |
| 4 | Transmission Lines | 133 | Characteristic impedance, reflections, terminations and propagation delay |
| 5 | Ground Planes and Layer Stacking | 189 | Signal returns, crosstalk and PCB layer selection |
| 6 | Terminations | 223 | End/source/middle termination and resistor/crosstalk choices |
| 7 | Vias | 249 | Via capacitance, inductance, return paths and geometry |
| 8 | Power Systems | 263 | Stable supply references and decoupling/distribution |
| 9 | Connectors | 295 | Inductive/capacitive coupling, continuity of return paths and cables |
| 10 | Ribbon Cables | 323 | Propagation, crosstalk, EMI and cable interfaces |
| 11 | Clock Distribution | 341 | Timing margin, clock skew, drivers, terminations |
| 12 | Clock Oscillators | 367 | Clock source, jitter and frequency stability |

### High-speed subsection map

| Section | Topic | Recorded printed page |
| --- | --- | ---: |
| 1.1 | Frequency and Time | 1 |
| 1.2 | Time and Distance | Unverified |
| 1.3 | Lumped Versus Distributed Systems | 7 |
| 1.6 | Ordinary Capacitance | 11 |
| 1.7 | Ordinary Inductance | 17 |
| 1.9 | Mutual Capacitance | 25 |
| 1.10 | Mutual Inductance | 29 |
| 2.2 | Power | 39 |
| 2.3 | Speed | 59 |
| 2.4 | Packaging | 66 |
| 3.1 | Rise Time and Bandwidth of Oscilloscope Probes | 83 |
| 3.2 | Self-inductance of a Probe Ground Loop | 86 |
| 3.3 | Spurious Pickup from Probe Ground Loops | 92 |
| 3.4 | How Probes Load Down a Circuit | 95 |
| 3.5 | Special Probing Fixtures | 98 |
| 3.7 | Viewing a Serial Transmission System | Unverified |
| 3.9 | Observing Crosstalk | 111 |
| 3.10 | Measuring Operating Margins | 113 |
| 3.11 | Observing Metastable States | 120 |
| 4.1 | Shortcomings of Ordinary Point-to-Point Wiring | 133 |
| 4.2 | Infinite Uniform Transmission Line | 140 |
| 4.3 | Source and Load Impedance | 160 |
| 4.4 | Special Transmission Line Cases | 167 |
| 4.5 | Line Impedance and Propagation Delay | 178 |
| 5.1 | High-Speed Current Follows the Path of Least Inductance | 189 |
| 5.2 | Crosstalk in Solid Ground Planes | 191 |
| 5.3 | Crosstalk in Slotted Ground Planes | 194 |
| 5.4 | Crosstalk in Cross-Hatched Ground Planes | 197 |
| 5.6 | Guard Traces | 201 |
| 5.7 | Near-End and Far-End Crosstalk | 204 |
| 5.8 | Printed Circuit Board Layer Stacking | 212 |
| 6.1 | End Terminators | 223 |
| 6.2 | Source Terminators | 231 |
| 6.3 | Middle Terminators | 235 |
| 6.4 | AC Biasing for End Terminators | 236 |
| 6.5 | Resistor Selection | 239 |
| 6.6 | Crosstalk in Terminators | 244 |
| 7.1 | Mechanical Properties of Vias | 249 |
| 7.2 | Capacitance of Vias | 257 |
| 7.3 | Inductance of Vias | 258 |
| 7.4 | Return Current and Vias | 260 |
| 8.1 | Providing a Stable Voltage Reference | 263 |
| 8.2 | Distributing Uniform Voltage | 268 |
| 8.3 | Everyday Distribution Problems | 279 |
| 8.4 | Choosing a Bypass Capacitor | 287 |
| 9.1 | Connector Crosstalk from Mutual Inductance | 295 |
| 9.2 | Connector EMI from Series Inductance | Unverified |
| 9.4 | Measuring Coupling in a Connector | 309 |
| 9.5 | Ground Continuity Under a Connector | 312 |
| 9.8 | Differential Signaling Through a Connector | 319 |
| 10.1 | Ribbon Cable Propagation | Unverified |
| 10.2 | Ribbon Cable Crosstalk | 329 |
| 10.4 | Ribbon Cable EMI | 338 |
| 11.1 | Timing Margin | 341 |
| 11.2 | Clock Skew | 343 |
| 11.5 | Source Termination of Multiple Clock Lines | 350 |
| 11.6 | Controlling Crosstalk on Clock Lines | 352 |
| 11.7 | Delay Adjustments | 353 |
| 11.8 | Differential Distribution | 360 |
| 12.1 | Using Canned Clock Oscillators | 367 |
| 12.2 | Clock Jitter | 376 |

**Examined source distinctions:** §1.3 describes the **length of a signal edge along a PCB trace**: an electrically distributed line does not have one uniform instantaneous voltage. §4.3.3 explains source termination with reflected-wave travel, including the risk of intermediate taps. §5.1 explains why fast return currents follow a low-inductance path under the trace; a ground trace that is DC-connected but separated from the return can still give a poor high-speed path. Ch. 3 examines probe ground-loop pickup and measurement loading; Ch. 2 examines package-induced ground bounce.

## Indexed book 3: Fundamentals of Power Electronics

[Open the exact Drive PDF](https://drive.google.com/file/d/1YH4DDlxKP4WqYoq_W6QFJ8r-DsZXk9-o/view?usp=drivesdk) · Robert W. Erickson and Dragan Maksimović, **Third Edition (2020)**. **23 chapters**, **346 chapter-section starts** in the canonical JSON, including converter dynamics, control, magnetics and sampled-data topics.

| Chapter | Title | Printed start | Retrieve for |
| ---: | --- | ---: | --- |
| 1 | Introduction | 1 | Power-processing systems and architectural boundaries |
| 2 | Principles of Steady-State Converter Analysis | 15 | Derive duty-cycle relationships and ripple from energy conservation |
| 3 | Steady-State Equivalent Circuit Modeling, Losses, and Efficiency | 43 | Equivalent switching circuit, conduction losses and efficiency |
| 4 | Switch Realization | 67 | Choose switch quadrants, MOSFETs, diodes and real switching losses |
| 5 | The Discontinuous Conduction Mode | 135 | Recognize discontinuous inductor current and load dependence |
| 6 | Converter Circuits | 163 | Compose converter cells, isolated and non-isolated topologies |
| 7 | AC Equivalent Circuit Modeling | 215 | Derive converter averaged small-signal models and state-space equations |
| 8 | Converter Transfer Functions | 277 | Analyze Bode plots, poles, zeros and nonminimum-phase behavior |
| 9 | Controller Design | 347 | Design control compensation and measure loop gains |
| 10 | Basic Magnetics Theory | 409 | Core, flux, winding and skin/proximity loss mechanisms |
| 11 | Inductor Design | 459 | Select winding/core to satisfy energy, saturation and loss |
| 12 | Transformer Design | 485 | Design transformers including reset and thermal/power loss |
| 13 | Techniques of Design-Oriented Analysis: The Feedback Theorem | 509 | Feedback theorem and practical control analysis |
| 14 | Circuit Averaging, Averaged Switch Modeling, and Simulation | 547 | Averaged switch models and useful simulation approximations |
| 15 | Equivalent Circuit Modeling of the Discontinuous Conduction Mode | 585 | Dynamics of discontinuous-mode converters |
| 16 | Techniques of Design-Oriented Analysis: Extra Element Theorems | 625 | Extra element theorem for perturbations and circuit interconnections |
| 17 | Input Filter Design | 675 | Design input filters without destabilizing converter dynamics |
| 18 | Current-Programmed Control | 725 | Current-programmed control, sampling and inner loops |
| 19 | Digital Control of Switched-Mode Power Converters | 805 | Digital compensation, sampling delays and Z-transform dynamics |
| 20 | Power and Harmonics in Nonsinusoidal Systems | 849 | Power factor and harmonics in distorted current/voltage waveforms |
| 21 | Pulse-Width Modulated Rectifiers | 867 | Rectifier/PFC and grid-facing converter choices |
| 22 | Resonant Conversion | 933 | Resonant power conversion |
| 23 | Soft Switching | 995 | Soft switching and switching-loss reduction tradeoffs |

### High-value Power Electronics subsection shortcuts

| § | Book heading | Printed page |
| --- | --- | ---: |
| 2.2 | Volt-Second and Charge Balance, Small-Ripple Approximation . . . . . . . . . . . . . 18 2.3 Boost Converter Example | 24 |
| 3.3 | Construction of Equivalent Circuit Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49 3.3.1 Inductor Voltage Equation | 50 |
| 3.3.4 | Efficiency. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52 3.4 How to Obtain the Input Port of the Model | 54 |
| 4.4.2 | Wide-Bandgap FETs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103 4.4.3 MOSFET Gate Drivers | 107 |
| 4.4.3 | MOSFET Gate Drivers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107 4.5 Minority-Carrier Transistors | 111 |
| 4.6.3 | Efficiency vs. Switching Frequency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126 4.7 Summary of Key Points | 126 |
| 5.1 | Origin of the Discontinuous Conduction Mode, and Mode Boundary . . . . . . . . 135 5.2 Analysis of the Conversion Ratio M(D, K) | 140 |
| 6.3 | Transformer Isolation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178 6.3.1 Full-Bridge and Half-Bridge Isolated Buck Converters | 181 |
| 6.3.4 | Flyback Converter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194 6.3.5 Boost-Derived Isolated Converters | 198 |
| 7.2 | The Basic AC Modeling Approach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220 7.2.1 Averaging the Inductor and Capacitor Waveforms | 221 |
| 7.2.6 | Perturbation and Linearization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227 7.2.7 Construction of the Small-Signal Equivalent Circuit Model | 230 |
| 7.5 | State-Space Averaging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 251 7.5.1 The State Equations of a Network | 252 |
| 8.1.3 | Right Half-Plane Zero . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 288 8.1.4 Frequency Inversion | 289 |
| 8.2.3 | Physical Origins of the RHP Zero in Converters. . . . . . . . . . . . . . . . . . . . 316 8.3 Graphical Construction of Impedances and Transfer Functions | 317 |
| 9.5 | Regulator Design . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 376 9.5.1 Lead (PD) compensator | 377 |
| 9.6 | Measurement of Loop Gains . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 392 9.6.1 Voltage Injection | 394 |
| 10.3 | Loss Mechanisms in Magnetic Devices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 423 10.3.1 Core Loss | 423 |
| 10.4 | Eddy Currents in Winding Conductors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 426 10.4.1 Introduction to the Skin and Proximity Effects | 426 |
| 10.5 | Several Types of Magnetic Devices, Their B–H Loops, and Core vs. Copper Loss | 444 |
| 11.1 | Filter Inductor Design Constraints. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 459 11.1.1 Maximum Flux Density | 461 |
| 12.2 | A First-Pass Transformer Design Procedure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 490 12.2.1 Procedure | 490 |
| 12.3 | Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 492 12.3.1 Example 1: Single-Output Isolated Cuk Converter ´ | 492 |
| 13.1 | Introduction to Part IV . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 509 13.2 The Feedback Theorem | 510 |
| 14.2 | Additional Configurations of Switch Networks . . . . . . . . . . . . . . . . . . . . . . . . . . . 558 14.3 Simulation of Averaged Circuit Models | 566 |
| 15.2 | DCM Averaged Switch Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 589 15.3 Small-Signal AC Modeling of the DCM Switch Network | 600 |
| 16.1 | Extra Element Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 625 16.1.1 Basic Result | 626 |
| 17.1 | Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 675 17.1.1 Conducted EMI | 675 |
| 18.1 | A Simple First-Order Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 728 18.1.1 Simple Model via Algebraic Approach: Buck–Boost Example | 729 |
| 19.1 | Digital Control Loop . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 806 19.1.1 A/D and DPWM Quantization | 807 |
| 19.3 | Discrete-Time Compensator Design . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 822 19.3.1 Design Procedure | 823 |
| 20.2 | Root-Mean-Square (RMS) Value of a Waveform . . . . . . . . . . . . . . . . . . . . . . . . . 853 20.3 Power Factor | 854 |
| 21.1 | Properties of the Ideal Rectifier . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 868 21.2 Realization of a Near-Ideal Rectifier | 870 |
| 22.1 | Sinusoidal Analysis of Resonant Converters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 938 22.1.1 Controlled Switch Network Model | 938 |
| 23.2 | The Zero-Current-Switching Quasi-Resonant Switch Cell .................. 1003 23.2.1 Waveforms of the Half-Wave ZCS Quasi-Resonant Switch Cell | 1005 |

**Examined source distinction — §2.2:** output voltage is a DC component plus switching ripple. Volt-second and charge-balance approximations derive steady-state behavior, subject to small-ripple assumptions; they do not establish output noise, stability or thermal adequacy of a real circuit. The preface explicitly positions digital control, wide-bandgap semiconductors and additional modern power applications as third-edition developments.

## Cross-book working paths

**Build a trustworthy voltage rail for a digital or analog device.** Art Ch. 9 linear/switch choice → Power Chs. 2–9 conversion, loss and loop models → HSDD Ch. 8 distribution and decoupling → Art Ch. 15 MCU/application rail measurements.

*Contract:* Ripple, load-step response, power loss, thermal state and supply/return impedance. *What an actual experiment must discriminate:* Measure ripple, regulation and thermal behavior under real load steps with appropriately grounded probes.

**Carry reliable data across a physically significant interconnect.** Art Chs. 10–14 logic/thresholds/interfaces → HSDD Ch. 1 rise time, Ch. 4 transmission lines, Ch. 5 return, Ch. 6 termination, Ch. 11 clocks.

*Contract:* Edge shape, threshold/noise margin, impedance, return continuity, skew, sampling time. *What an actual experiment must discriminate:* Measure at transmitter and receiver with deliberate termination/return variations.

**Capture useful small analog signals in software without swamping them in noise.** Art Chs. 4–5 amplifiers, Ch. 8 noise, Ch. 13 ADC → HSDD Ch. 3 realistic probing and Ch. 8 quiet supplies.

*Contract:* Source impedance, gain/noise bandwidth, common-mode rejection, reference, aliasing and interference. *What an actual experiment must discriminate:* Evaluate input-referred noise and measurement dependence across source impedances and bandwidth.

**Choose switching devices and magnetics for a robust load.** Art Ch. 3 power MOSFETs and Ch. 9 heat → Power Chs. 3–4 losses, Chs. 10–12 magnetics, Chs. 22–23 soft/resonant conversion.

*Contract:* Worst-case conduction/switch loss, core flux, winding heating, thermal impedance. *What an actual experiment must discriminate:* Measure efficiency and hot spots across load/line/frequency rather than relying only on ideal ratings.

**Translate a working schematic into a manufacturable, diagnosable board.** Art Chs. 1–3 components and Ch. 15 MCU case → HSDD Chs. 3/5/7/8/9 probes/return/vias/power/connectors → Art appendices SPICE/oscilloscope.

*Contract:* Physical return paths, probe access, heat, supply decoupling, component tolerances and safe instrumentation. *What an actual experiment must discriminate:* Compare representative board behavior against bench prototype and measured physical margins.

## Independent glossary and next-step policy

The [glossary](glossary.json) includes **639 identities**, some of which are explicitly marked `adjacent_candidate`. They are legitimate vocabulary-landscape entries even before a question, mechanism or source excerpt uses them. Do not manufacture connections merely to give every term a question. The natural questions in the [canonical investigation](investigation.json) use only select `term_ids`; unmapped vocabulary remains browsable through the Atlas Vocabulary mode.

**Next use:** Search this guide's problem table or independently browse the glossary; retrieve an exact chapter/section using the preindexed catalog; inspect only a new relevant passage; record the actual circuit, condition, source location and uncertainty in the canonical JSON; link the smallest necessary term IDs. Do not duplicate explanations, reindex three TOCs, or conflate proof-of-circuit with full system operation.

**Safety boundary:** Neither the textbook examples nor the research index authorize live-mains probing. Protective-earth connections, capacitor charge, isolation ratings and instrument-ground consequences require target-specific verification before any energized high-voltage work.
