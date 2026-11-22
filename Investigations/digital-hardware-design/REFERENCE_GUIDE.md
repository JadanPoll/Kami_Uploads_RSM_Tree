# Digital hardware — FPGA, Verilog, and VLSI reference guide

**Persistent book map, not another independent research database.** Begin here when you have an FPGA/VLSI idea or hardware failure. The canonical [`investigation.json`](investigation.json) stores the 24 ordinary entry questions, 15 conditional mechanism bridges, 15 technical nodes, five larger investigation sets, 27 chapter anchors, and source distinctions. This guide makes them quickly retrievable without reconstructing either PDF's table of contents.

**Drive shelf:** [FPGA and VLSI collection](https://drive.google.com/drive/folders/1veFqc1U0plkG-mpiXaqRW-QLEPY5pvYS). The two books are [Pong P. Chu — FPGA Prototyping by Verilog Examples](https://drive.google.com/file/d/1N_LEBervU1AF7B3deioFkq-h83zAdDbA/view?usp=drivesdk) (2008, Spartan-3) and [Carver Mead & Lynn Conway — Introduction to VLSI Systems](https://drive.google.com/file/d/1FX7k8OxgEFrcgIr6sIn_gCd3mpE9STsh/view?usp=drivesdk) (1980, nMOS-era integrated systems). The shelf also contains two empty organizational folders. **These books are historical sources of transferable mechanisms, not current tool/PDK manuals.**

## Choose the layer where the uncertainty lives

| Layer | Ask | Most relevant source | Distinction that changes the next action |
| --- | --- | --- | --- |
| Behavioral contract | What input/state/output relationship should be true? | Chu Chs. 1, 3–7 | Combinational logic, clocked state and multicycle FSMD are different specifications |
| FPGA mapping | Which LUTs, FFs, memories, pins and timing routes realize it? | Chu Chs. 2, 4, 11–12 | Successful simulation is not mapped timing closure or a board-level observation |
| Device interface | How does a physical signal become a valid transaction? | Chu Chs. 8–14 | Signal timing, framing, buffering and semantic events are independent requirements |
| Integrated computation | Could this be a programmed processor or a dedicated controller/datapath? | Chu Chs. 6, 15–18; Mead–Conway Chs. 3, 5–6 | Changeability and programmability versus predictable direct hardware execution |
| Electrical circuit | How does a transistor-level gate switch under real load? | Mead–Conway Ch. 1 | Boolean equality ignores capacitance, charge, delay and power |
| Layout/fabrication | Can the geometry be realized reliably by the process? | Mead–Conway Chs. 2, 4 | A logic-correct circuit is not necessarily design-rule-legal, routable or high-yield |
| Timing/concurrency | What must be ordered, acknowledged and sampled? | Chu Ch. 4; Mead–Conway Chs. 7–8 | Global clock, clock-domain crossing and self-timed communication have different contracts |

## From a natural question to the right source

| Question or failure | First meaningful split | Book locator | Evidence state |
| --- | --- | --- | --- |
| The HDL simulates correctly but the board does nothing | RTL/model vs mapping, physical pins, clock/reset or timing | Chu Ch. 2; Ch. 4 | Chapter 2 flow and selected timing discussion inspected; actual board not verified |
| An `always` block mysteriously remembers a value | Incomplete combinational assignment vs deliberate state | Chu Ch. 3, combinational `always` guidance | Inspected passage |
| One press registers twice | Mechanical bounce vs control transition vs synchronizer | Chu Ch. 5, debouncing; Mead–Conway Ch. 7 | Candidate reading; synchronization section inspected, design untested |
| A calculation needs multiple clock cycles | Fixed datapath iteration vs hardwired combinational logic | Chu Ch. 6 FSMD; Mead–Conway Chs. 3, 5–6 | TOC/preface-level lead |
| UART data becomes garbage or framing drifts | Bit-center/baud-rate mismatch vs clocking domain | Chu Ch. 8 §8.2.1–8.2.2 | Inspected passage: 16× oversampling and enable ticks |
| The design meets behavior but not target frequency | Combinational path + clock-to-Q + setup versus real path/skew | Chu Ch. 4; Mead–Conway Ch. 7 | Selected passage inspected |
| Two working clocked subsystems fail when connected | Synchronous timing closure vs asynchronous sampling/metastability | Mead–Conway Ch. 7 §§7.3–7.8; Chu Ch. 4 | Selected timing/synchronization passage inspected |
| A large FIFO won't fit in logic registers | FF array vs internal block RAM vs external controller | Chu Chs. 4, 11–12 | TOC and book preface leads |
| Need keyboard, mouse, graphics or text display | Transport/protocol/scan timing vs application data | Chu Chs. 9–10, 13–14 | TOC and preface leads; current-board interface not guaranteed |
| Want to run software inside an FPGA | Dedicated RTL/FSMD vs soft-core stored-program execution | Chu Chs. 15–18; Mead–Conway Chs. 5–6 | Chapter/preface leads |
| A Boolean gate is slow when connected to many others | Input-output truth table vs transistor load capacitance | Mead–Conway Ch. 1 §§1.1–1.5 | Selected passage inspected |
| The chip schematic is correct but layout fails | Connectivity vs geometric design rules, contact and wires | Mead–Conway Ch. 2 §2.6; Ch. 4 | Source sections identified; no modern PDK applied |
| Fabricated chips differ in quality | Electrical intent vs process variability and defect/yield statistics | Mead–Conway Ch. 2 §2.4 | Selected text inspected; no current process data |
| Should I use FPGA or build a chip? | Configurable existing silicon vs fixed manufactured patterns and economic volume | Chu Ch. 2; Mead–Conway Chs. 2, 4 | Conceptual comparison; no fabrication quotation |

## Book 1 — Pong P. Chu, FPGA Prototyping by Verilog Examples (2008)

[Open in Drive/Kami](https://drive.google.com/file/d/1N_LEBervU1AF7B3deioFkq-h83zAdDbA/view?usp=drivesdk) · **18 chapters / 3 parts.** Chapter names and purpose were inspected in the PDF preface; individual chapter **printed starts could not be reliably recovered from the extracted table's separated columns**, so the robust locators are chapter/section identifiers, not invented PDF page offsets.

| Ch. | Book's chapter title | Part | What it enables | Linked canonical nodes |
| ---: | --- | --- | --- | --- |
| 1 | Gate-level combinational circuit | I | Verilog structure, primitive gates and testbench; mapping a Boolean function to explicit logic | `DHW-COMB` |
| 2 | Overview of FPGA and EDA software | I | FPGA configuration and tool flow; synthesize, place, constrain and load the circuit | `DHW-FLOW` |
| 3 | RT-level combinational circuit | I | Operators, mux/priority structure, incomplete assignment and unintended latches | `DHW-COMB` |
| 4 | Regular Sequential Circuit | I | Flip-flop, register, counter, FIFO and clock timing; clock-to-Q, setup and hold | `DHW-TIMING`, `DHW-STATE` |
| 5 | FSM | I | Control state and transitions; switch debounce and edge detection | `DHW-STATE` |
| 6 | FSMD | I | FSM plus datapath and register-transfer operations; divider and BCD conversion | `DHW-DATAPATH` |
| 7 | Selected Topics of Verilog | I | Blocking versus nonblocking, signed arithmetic, functions and richer testbenches | `DHW-COMB`, `DHW-TIMING` |
| 8 | UART | II | Receiver oversampling, baud-enable tick generation, framing and serial verification | `DHW-UART` |
| 9 | PS2 Keyboard | II | Scan-code receiving, sampling/decoding and protocol boundary | `DHW-PERIPHERALS` |
| 10 | PS2 Mouse | II | Bidirectional PS/2 host control, mouse events and initialization | `DHW-PERIPHERALS` |
| 11 | External SRAM | II | Memory-controller timing, safe versus aggressive access and verification | `DHW-MEMORY` |
| 12 | Xilinx Spartan-3 Specific Memory | II | FPGA memory primitives, inference and board-dependent resources | `DHW-MEMORY` |
| 13 | VGA controller I: graphic | II | Synchronization timing and bit-/object-mapped graphics controllers | `DHW-VIDEO` |
| 14 | VGA controller II: text | II | Character tiles, fonts and display memory addressing | `DHW-VIDEO` |
| 15 | PicoBlaze Overview | III | Microcontroller datapath/ISA hosted inside FPGA programmable resources | `DHW-SOFTCORE` |
| 16 | PicoBlaze Assembly Code Development | III | Assembly behavior and firmware development for a soft-core processor | `DHW-SOFTCORE` |
| 17 | PicoBlaze I/O Interface | III | Custom soft-core ports and hardware/firmware interfaces | `DHW-SOFTCORE`, `DHW-PERIPHERALS` |
| 18 | PicoBlaze Interrupt Interface | III | Soft-core interrupt handling and its custom external logic | `DHW-SOFTCORE`, `DHW-TIMING` |

### Source-inspected mechanisms worth remembering

**Unexpected latch (Ch. 3):** A combinational `always` block that does not assign an output on every branch can infer memory. The discriminating check is whether the output remains a function only of present inputs, and whether the synthesized device contains inferred storage. This is materially different from a logic bug with no state.

**Timing is physical (Ch. 4):** Flip-flops have clock-to-Q, setup and hold behavior; combinational delay between registering stages limits maximum safe clock. RTL simulation without back-annotated physical timing does not establish the circuit meets clock requirements.

**UART without a serial clock (Ch. 8 §§8.2.1–8.2.2):** The text reconstructs bit centers from start-bit timing with a 16× baud sampler. The baud-rate generator should emit synchronous enable ticks rather than inventing another derived FPGA clock domain. That architectural choice is more reusable than the book's fixed board clock and baud examples.

**RTL versus hardware implementation (Ch. 2):** The book's sequence of description → simulation → synthesis → implementation → programming still illustrates distinct contracts. Its ISE user interface, Spartan-3 primitives, timing reports and pin constraints are tool/target-specific. For a newer device, use the current vendor board manuals, pin/clock constraints and modern toolchain.

## Book 2 — Mead & Conway, Introduction to VLSI Systems (1980)

[Open in Drive/Kami](https://drive.google.com/file/d/1FX7k8OxgEFrcgIr6sIn_gCd3mpE9STsh/view?usp=drivesdk) · **9 chapters.** This OCR copy is noisy, so the printed page starts below are **indicative values read from the scanned contents, not certified direct-jump positions**. Chapter numbers and distinctive subtopic names remain the preferred retrieval key.

| Ch. | Book chapter | Approx. printed start | Mechanism landscape | Technical links |
| ---: | --- | ---: | --- | --- |
| 1 | MOS Devices and Circuits | 1 | Transistor gating, pullups, capacitance, switching delay and logic fan-out | `DHW-MOS`, `DHW-PHYSICAL-TIMING` |
| 2 | Integrated System Fabrication | 38 | Photolithographic patterning, nMOS process, design rules, yield and scaling | `DHW-FABRICATION`, `DHW-LAYOUT` |
| 3 | Data and Control Flow in Systematic Structures | 60 | Two-phase clocking, registers, register transfer, logic arrays and FSMs | `DHW-DATAPATH`, `DHW-STATE` |
| 4 | Implementing Integrated System Designs: From Circuit Topology to Patterning Geometry to Wafer Fabrication | 91 | Symbolic layout, design-rule adaptation, chip production and multiproject chips | `DHW-LAYOUT`, `DHW-FABRICATION` |
| 5 | Overview of an LSI Computer System and the Design of the OM2 Datapath Chip | 145 | Functional partitioning into ALU, registers, buses, barrel shifter and register array | `DHW-DATAPATH`, `DHW-SOFTCORE` |
| 6 | Architecture and Design of System Controllers, and the Design of the OM2 Controller Chip | 189 | Stored-program control, microprogramming and integrated controller architecture | `DHW-SOFTCORE`, `DHW-STATE` |
| 7 | System Timing | 218 | Synchronous clocks, distribution and skew, synchronization failure and self-timed systems | `DHW-PHYSICAL-TIMING`, `DHW-TIMING` |
| 8 | Highly Concurrent Systems | 263 | Global communication, hierarchically structured concurrent computation and processor arrays | `DHW-PHYSICAL-TIMING`, `DHW-DATAPATH` |
| 9 | Physics of Computational Systems | 333 | Voltage, charge discreteness, thermodynamic/quantum/physical limits and computational complexity | `DHW-MOS`, `DHW-PHYSICAL-TIMING` |

### Why these chapters are a different kind of hardware book

**Ch. 1 — MOS devices and delay:** A 'gate' is a physical switching network. Transistor sizing, charging and discharging a capacitive load, and interconnect alter actual transition times. Logical equivalence does not imply equal timing, area, or electrical robustness.

**Ch. 2 — processes and yield:** Mask/pattern geometry must obey material-layer and spacing constraints. The book discusses yield statistics for manufactured chips; passing a logical test never proves manufacturing yield. Its nMOS design rules are **historical examples**, not substitutes for the current foundry's process design kit.

**Chs. 3, 5–6 — structure and architecture:** Registers, data movement, ALUs, control and microprogramming provide a link between the Boolean abstraction and physical computer architecture. This complements Chu's FSM-with-datapath work without duplicating a separate technical tree.

**Ch. 7 — timing is architecture:** Clock distribution and skew, synchronization failure and self-timed handshakes change the execution contract. A processor can compute a logically right result yet sample an indeterminate transition at the wrong time. CDC design requires a real target-specific strategy; book concepts are not evidence of safe handoff on a particular FPGA.

## Composable paths spanning both books

**A physical UART-controlled device.** Chu Ch. 8 bit sampling → Chu Ch. 5 controller → Chu Ch. 4 timing → Mead–Conway Ch. 7 synchronization. *Why:* UART port needs framing/timing correctness before integrating with a larger state machine.
**A soft-core with custom peripheral.** Chu Chs. 15–18 soft CPU and I/O → Chu Ch. 6 FSMD datapath → Mead–Conway Chs. 5–6 controller/data organization. *Why:* Separate firmware programmability from the fixed peripheral protocol and bus contract.
**A working video design.** Chu Chs. 13–14 pixel/tiles → Chu Chs. 11–12 memory/storage → Chu Ch. 4 timing. *Why:* The display interface consumes pixel data at a fixed schedule whether the producer is ready or not.
**A reconfigurable logic module.** Chu Chs. 1–4 HDL and synthesis → Mead–Conway Ch. 1 electrical gate constraints → Ch. 4 layout. *Why:* Physical details matter even if FPGA vendor tools hide most transistor placement.
**A reliable timed system.** Chu Ch. 4 setup/hold → Mead–Conway Ch. 7 clock distribution/metastability → real board constraints and observations. *Why:* A timing report is a necessary but not sufficient explanation of an intermittent interface failure.
**A route to actual custom silicon.** Mead–Conway Ch. 2 process rules → Chs. 3–4 layout structures → Chs. 5–6 datapath/control → contemporary PDK and foundry signoff. *Why:* Historical nMOS examples expose the design-to-fabrication contract, not the instructions for fabricating a modern ASIC.

## Source coverage and boundaries

- **Inspected text**, not just contents: Chu's combinational latch inference, clock-to-Q/setup/hold timing, UART oversampling/baud enables, and tool-flow explanation; Mead–Conway's MOS switching/load behavior, fabrication/yield, and clock/synchronization discussion.
- **Mapped but not independently executed:** Verilog example implementations, SRAM controllers, PS/2, VGA, PicoBlaze, physical chip layout and wafer fabrication. The chapter routes enable later study, not a claim that the books' examples passed a modern test.
- **Technology-generation caveat:** Spartan-3/ISE (2008) differs from modern FPGA architecture/constraints; nMOS VLSI geometry and tool flows (1980) differ strongly from current CMOS and foundry signoff. Transfer principles, not undocumented pinouts, syntax dialects or mask dimensions.
- **User folder substructure:** [Binding_And_Logical_Gases](https://drive.google.com/drive/folders/12WX4O3pf0U2iAy3JMHKzUreVLuB0UWN9) and [Tacit](https://drive.google.com/drive/folders/1dNsN1Hff4Pe6n9P50WB2hEE3CnYZmsWx) were empty when inspected; no exercise or source is claimed to exist within them.

## Next research pass — no unnecessary re-indexing

1. Search this guide by natural problem or open the matching `curiosity_atlas.entries` question; choose its `navigation_bridges` branch based on observable constraints.
2. Retrieve existing source ID plus `book_landscaplets` chapter from the **single** [`investigation.json`](investigation.json); use an inspected node's `source_sections` when available.
3. Inspect **only the subsection relevant to unresolved uncertainty**; extract the actual explanation, worked example or waveform, and record its printed page or PDF offset correctly.
4. Connect it to an existing technical node or add one new mechanism when the existing abstraction cannot represent it. A new question phrasing usually needs only an entry alias or bridge.
5. Evaluate a working hardware target through representative clocks, interfaces and actual synthesis/constraint reports; distinguish the book's proof-of-concept from observed current-board behavior.
6. When adding a new hardware book, index its meaningful contents **once**; do not reprocess these 27 already mapped chapters.
