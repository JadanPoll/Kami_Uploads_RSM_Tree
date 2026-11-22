# Neuromorphic engineering — durable two-book reference and mechanism map

**Read this before reopening or reindexing either book.** It is the persistent human-readable entry to the two PDFs: all 33 book chapters (plus Mead's four appendices), 52 selected subsection starts, source-inspected mechanism notes and cross-book functional routes. The canonical [investigation JSON](investigation.json) holds the structured chapter catalog and technical records. The adjacent [glossary JSON](glossary.json) is an independently growable landscape of terminology; vocabulary does **not** need a question, link, or completed experiment to exist.

**Source shelf:** [Neuromorphic engineering (Google Drive)](https://drive.google.com/drive/folders/1dF3VIEePbbg3LdDMDs3WTO2QEjaF-S0a) · **Source IDs:** `MEAD-1989` and `LIU-2015`. Printed page numbers below come from the books' contents, **not certified PDF viewer offsets**. This guide distinguishes examined mechanisms from content-table retrieval leads; neither is a reproduction of the full original experiment.

## What these books factor into

| Layer of capability | Mead, 1989 | Liu et al., 2015 | What can be composed |
| --- | --- | --- | --- |
| Device physics | Weak-inversion MOS, current mirrors, differential pairs, continuous-time filters | Silicon neurons, synapses, bias circuits and floating-gate programming | Physical nonlinearities, time constants, low-power constraints and noisy device parameters |
| Local neural computation | Resistive grids, aggregation, axon-hillock, retina and cochlea | Biophysical circuits, attractors, on-chip learning and configurable synapses | Spatial aggregation, spike generation, memory and sensor responses |
| Transport and integration | One-chip analog network and sensory examples | Address-event representation, arbitration, queue/drop, chip-to-chip AER and FPGA/software bridges | Spike identities/timestamps over shared hardware with explicit traffic contracts |
| Applications and evidence | SeeHear, optical motion, silicon retina and electronic cochlea | DVS, cochlea, robotics, event trackers, Neurogrid and large systems | Bounded physical workflows, end-to-end latency and measured task outcomes |

**A consequential contrast:** the first book develops *continuous-time analog physical computation*; the second extensively develops *discrete asynchronous event communication between such computing elements*. A sparse event stream can still saturate a shared bus, and a low-power neuron circuit does not by itself establish an energy-efficient system.

## What to open for a real curiosity

| Starting question or surprise | Crucial distinction | Direct book retrieval | Evidence status |
| --- | --- | --- | --- |
| Why can a transistor calculate? | Current as a nonlinear physical function versus logic instructions | Mead Ch. 3 pp. 33–39; Ch. 6 p. 83 | Subthreshold and current mirrors inspected; arithmetic is TOC lead |
| Why does an analog signal carry history? | Capacitance/time constant versus discrete memory register | Mead Chs. 8–11 pp. 127–179 | TOC lead |
| Why can local neighbors solve a global visual problem? | Coupled resistive equilibrium versus centralized aggregation | Mead Ch. 7 pp. 101, 116 | HRes passage inspected |
| How does a physical neuron fire? | Integrating leaked current, thresholding and reset | Mead Ch. 12 p. 194; Liu Ch. 7 p. 161 | Both mechanisms inspected |
| How does a shared neuron/event wire work? | Addressed event identity versus analog waveform | Liu Ch. 2 p. 12; Ch. 12 p. 285 | AER conceptual pathway inspected; hardware circuits TOC lead |
| Why do spikes arrive late or disappear? | Queueing preserves events but delays them; dropping preserves recent timing but loses information | Liu Ch. 2 §2.3.3 p. 24, §2.3.4 p. 25 | Queue-versus-drop discussion inspected |
| Why is a DVS quiet in an unchanged scene? | Temporal contrast versus synchronous frame intensity | Liu Ch. 3 p. 40 and DVS p. 41 | Selected comparison inspected |
| Why does a stationary sensor still fire? | Electrical leakage/background events versus physical scene changes | Liu Ch. 3 §3.7.2 p. 62 | Background-event circuit discussion inspected |
| How does silicon imitate hearing? | Frequency filtering/delay line versus auditory event encoding | Mead Ch. 16 pp. 279, 289; Liu Ch. 4 p. 71, Ch. 9 p. 219 | TOC lead |
| How can a chip learn without forgetting? | Finite synaptic state versus durable memory retention and attractor recall | Liu Ch. 6 pp. 122, 143–145; Ch. 8 pp. 201–203 | Memory tradeoff and on-chip learning section inspected |
| How does a computer actually receive sensor events? | Capture time stamps versus software processing delay and closed-loop latency | Liu Ch. 13 p. 305; Ch. 14 §14.4.3 p. 353, jAER p. 359 | Timestamp/latency discussion inspected |
| Could a neural circuit coordinate a walking robot? | Rhythmic central pattern versus stabilized feedback under physical load | Liu Ch. 5 pp. 100, 108–112 | TOC lead |
| Why do large neuron arrays not automatically scale? | Transport saturation, bias distribution and workload utility versus raw neuron count | Liu Chs. 2, 11–14, 16 (p. 381+) | Mixed inspected transport passages and TOC leads |

## Book 1 — Carver Mead, *Analog VLSI and Neural Systems* (1989)

[Open in Drive/Kami](https://drive.google.com/file/d/1EoxZXhmCF_aiJCdQBhu8E2VUiw6xvY_Q/view?usp=drivesdk). The scanned contents give **16 chapters across four parts and four appendices**. Some OCR labels are garbled; printed page values are the contents' page labels, not PDF offsets. This book is a 1989 hardware research source—do not copy its old transistor/process assumptions into contemporary silicon without a target PDK and measurements.

| Part | Ch. | Book section | Printed start | Retrieve for |
| --- | ---: | --- | ---: | --- |
| I · Basics | 1 | Introduction | 3 | I · Basics · Introduction |
| I · Basics | 2 | Eclectronics | 11 | I · Basics · Eclectronics |
| I · Basics | 3 | Transistor Physics | 27 | I · Basics · Transistor Physics |
| I · Basics | 4 | Neurons | 43 | I · Basics · Neurons |
| II · Static functions | 5 | Transconductance Amplifier | 67 | II · Static functions · Transconductance Amplifier |
| II · Static functions | 6 | Elementary Arithmetic Functions | 83 | II · Static functions · Elementary Arithmetic Functions |
| II · Static functions | 7 | Aggregating Signals | 101 | II · Static functions · Aggregating Signals |
| III · Dynamic functions | 8 | Time-Varying Signals | 127 | III · Dynamic functions · Time-Varying Signals |
| III · Dynamic functions | 9 | Follower-Integrator Circuit | 147 | III · Dynamic functions · Follower-Integrator Circuit |
| III · Dynamic functions | 10 | Differentiators | 163 | III · Dynamic functions · Differentiators |
| III · Dynamic functions | 11 | Second-Order Section | 179 | III · Dynamic functions · Second-Order Section |
| III · Dynamic functions | 12 | Axons | 193 | III · Dynamic functions · Axons |
| IV · System examples | 13 | SeeHear | 207 | IV · System examples · SeeHear |
| IV · System examples | 14 | Optical Motion Sensor | 229 | IV · System examples · Optical Motion Sensor |
| IV · System examples | 15 | Silicon Retina | 257 | IV · System examples · Silicon Retina |
| IV · System examples | 16 | Electronic Cochlea | 279 | IV · System examples · Electronic Cochlea |
| Appendix | A | CMOS Fabrication | 305 | Silicon-gate CMOS, yield and geometric constraints |
| Appendix | B | Fine Points of Transistor Physics | 319 | Electrostatics, subthreshold operation and generalized MOS model |
| Appendix | C | Resistive Networks | 339 | Continuous/discrete resistor networks, shunting inhibition and branches |
| Appendix | D | Complexity in Neural Systems | 353 | Analog and entropy factors as historical complexity arguments |

### Mead — selected subsection locator shelf

| Ch. | Subsection | Printed start | Canonical mechanism |
| ---: | --- | ---: | --- |
| 3 | MOS Transistors | 33 | `NMR-PHYS` |
| 3 | Circuit Properties of Transistors | 36 | `NMR-PHYS` |
| 3 | Current Mirrors | 39 | `NMR-MIRROR` |
| 5 | Transistor Mismatch | 72 | `NMR-MIRROR` |
| 6 | Exponentials and Logarithms | 97 | `NMR-ANALOG` |
| 7 | The Horizontal Resistor (HRes) Circuit | 116 | `NMR-AGGREGATE` |
| 8 | The Resistor-Capacitor (RC) Circuit | 129 | `NMR-DYNAMICS` |
| 9 | Follower-Integrator Delay Line | 152 | `NMR-DYNAMICS` |
| 10 | Hysteretic Differentiator | 173 | `NMR-DYNAMICS` |
| 11 | Stability Limit | 187 | `NMR-DYNAMICS` |
| 12 | The Axon-Hillock Circuit | 194 | `NMR-SPIKE` |
| 12 | Self-Resetting Neuron | 198 | `NMR-SPIKE` |
| 14 | Solution of Simultaneous Constraints | 233 | `NMR-MOTION` |
| 15 | Photoreceptor Circuit | 260 | `NMR-RETINA` |
| 16 | Silicon Cochlea | 289 | `NMR-COCHLEA` |
| 16 | Transistor Parameter Variation | 294 | `NMR-COCHLEA` |

### Mead — what was actually inspected

**Weak inversion (Ch. 3):** The text explicitly derives useful behavior from extremely low, exponentially voltage-dependent transistor currents. It identifies low power, current-source behavior and exponential nonlinearity as advantages; matching, temperature and circuit constraints remain relevant. The transferable idea is *function as semiconductor physics* rather than repeating instruction sequences.

**Current mirrors (Ch. 3):** Mead uses diode-connected MOS transistors to establish reusable current sources and sinks. This supplies a primitive for distributing analog operating points, but the symbolic mirror does not establish exact copy accuracy under device mismatch.

**Horizontal resistor networks (Ch. 7):** Mead describes an electronic, bias-controlled resistive connection and its use as a retinal horizontal-cell model. Spatial computations emerge from a network of coupled local elements instead of a serial global loop.

**Axon-hillock (Ch. 12, p. 194 onward):** The proposed silicon neuron integrates injected current until an electrical event fires; input leak determines whether weak input is insufficient to trigger repeated spikes. The physical capacitor/positive-feedback/reset path matters to spike timing.

## Book 2 — Liu, Delbruck, Indiveri, Whatley & Douglas (eds.), *Event-Based Neuromorphic Systems* (2015)

[Open in Drive/Kami](https://drive.google.com/file/d/1chsw9TCVW_qVTCvunYcIMSHWOdy99V43/view?usp=drivesdk). The book has **17 chapters**, divided into understanding and building sections with hardware, software, event algorithms and system scaling. All listed starts are **printed** page numbers from the accessible contents.

| Ch. | Section | Printed start | Retrieve for |
| ---: | --- | ---: | --- |
| 1 | Introduction | 1 | Origins and scope of event-based systems |
| 2 | Communication | 9 | AER encoding, arbitration, routing and transport tradeoffs |
| 3 | Silicon Retinas | 37 | DVS/ATIS, analog front-end, event image sensing and sensor specifications |
| 4 | Silicon Cochleas | 71 | Cascaded filters, active cochlea and spike-based auditory models |
| 5 | Locomotion Motor Control | 91 | Central pattern generators, neuroprostheses and walking robots |
| 6 | Learning in Neuromorphic Systems | 119 | Memory maintenance, synapse models and attractor circuits |
| 7 | Silicon Neurons | 155 | Conductance dynamics, threshold, refractory and integrate-and-fire circuits |
| 8 | Silicon Synapses | 185 | Conductance and plasticity implementations |
| 9 | Silicon Cochlea Building Blocks | 219 | Transconductors, tau cells, filters and hair-cell models |
| 10 | Programmable and Configurable Analog Neuromorphic ICs | 237 | Floating-gate programming, computing in memory and analog arrays |
| 11 | Bias Generator Circuits | 261 | Current reference, splitters, startup, bias tuning and power control |
| 12 | On-Chip AER Communication Circuits | 285 | Transmit arbiters, receivers, handshake and decoders |
| 13 | Hardware Infrastructure | 305 | Event monitoring, mapping, interfaces, FPGA and multichip systems |
| 14 | Software Infrastructure | 349 | NeuroML, event streams, jAER and Python/PyNN |
| 15 | Algorithmic Processing of Event Streams | 365 | Noise filters, feature/event tracking and auditory event processing |
| 16 | Towards Large-Scale Neuromorphic Systems | 381 | Hierarchical event routing, Neurogrid and larger systems |
| 17 | The Brain as Potential Technology | 393 | Biological principles and neuromorphic cognition |

### Liu et al. — subsection locator shelf

| Ch. | Subsection | Printed start | Canonical mechanism |
| ---: | --- | ---: | --- |
| 2 | Address-Event Representation | 12 | `NMR-AER` |
| 2 | Arbitration Mechanisms | 13 | `NMR-QUEUES` |
| 2 | Routing | 19 | `NMR-AER` |
| 2 | Queueing versus Dropping Spikes | 24 | `NMR-QUEUES` |
| 2 | Predicting Throughput Requirements | 25 | `NMR-QUEUES` |
| 3 | Asynchronous Event-Based Pixel Output Versus Synchronous Frames | 40 | `NMR-RETINA` |
| 3 | Dynamic Vision Sensor | 41 | `NMR-RETINA` |
| 3 | DVS Background Activity | 62 | `NMR-RETINA` |
| 3 | DVS Latency and Jitter | 63 | `NMR-RETINA` |
| 4 | Spike-Based Cochleas | 83 | `NMR-COCHLEA` |
| 5 | Basic CPG Construction | 100 | `NMR-LOCOMOTION` |
| 5 | Walking Robots | 111 | `NMR-LOCOMOTION` |
| 6 | Problem of Memory Maintenance: Quantitative Analysis | 122 | `NMR-LEARNING` |
| 6 | Attractor States in a Neuromorphic Chip | 143 | `NMR-LEARNING` |
| 6 | Learning Visual Stimuli in Real Time | 145 | `NMR-LEARNING` |
| 7 | Spiking Thresholds and Refractory Periods | 161 | `NMR-SPIKE` |
| 7 | Compact I&F Circuits for Event-Based Systems | 169 | `NMR-SPIKE` |
| 8 | Short-Term Plasticity | 201 | `NMR-LEARNING` |
| 8 | Long-Term Plasticity | 203 | `NMR-LEARNING` |
| 9 | Translinear Loop | 227 | `NMR-COCHLEA` |
| 10 | Modifying Floating-Gate Charge | 242 | `NMR-CONFIG` |
| 10 | Analog Computing in Memory | 249 | `NMR-CONFIG` |
| 11 | Master Bias Startup and Power Control | 266 | `NMR-BIAS` |
| 11 | Current Splitters | 267 | `NMR-BIAS` |
| 12 | Arbiter | 290 | `NMR-AER` |
| 12 | Decoder | 299 | `NMR-AER` |
| 13 | Monitoring AER Events | 307 | `NMR-INTEGRATION` |
| 13 | Mapping AER Events | 313 | `NMR-INTEGRATION` |
| 13 | FPGAs | 340 | `NMR-INTEGRATION` |
| 14 | Bandwidth and Latency | 353 | `NMR-INTEGRATION` |
| 14 | jAER | 359 | `NMR-INTEGRATION` |
| 14 | Python and PyNN | 360 | `NMR-INTEGRATION` |
| 15 | Noise Reduction Filters | 370 | `NMR-ALGORITHMS` |
| 15 | Visual Trackers | 374 | `NMR-ALGORITHMS` |
| 16 | Hierarchical AER | 384 | `NMR-SCALE` |
| 16 | Neurogrid | 386 | `NMR-SCALE` |

### Liu et al. — inspected nuggets that change investigations

**Queue versus drop (Ch. 2 §2.3.3):** With an overloaded event channel, retaining spikes in a queue adds latency and temporal dispersion; dropping earlier spikes loses data while preserving new response timing. This is a task-conditioned systems decision, not a universal preference for lossless transport.

**DVS background events (Ch. 3 §3.7.2):** The book describes junction leakage producing events unrelated to the scene; event-based sensors are *not* literally silent or noise-free at zero scene activity. Distinguish scene-driven contrast events from sensor background activity and software filtering.

**Memory retention (Ch. 6 §6.2.2):** A bounded synaptic state that saturates or is overwritten cannot preserve arbitrary earlier learning. The book distinguishes synaptic modifications, sustained attractor activity and actual retrievable memory. A demo that recalls one pattern does not establish long-term independent retention.

**Firing and refractory dynamics (Ch. 7 §7.2.3):** Implemented silicon neuron circuits expose threshold and refractory controls through physical device elements. Their parameters are chip- and bias-dependent, not merely arbitrary software constants.

**Software latency (Ch. 14 §14.4.3):** Hardware time stamps preserve source inter-event timing for delayed offline analysis, but online closed-loop control still depends on sensor-to-output latency. Capture fidelity and real-time actuation must be verified separately.

## Cross-book mechanism chains

**Convert an analog physical signal into sparse events.** Mead Ch. 3 subthreshold MOS / Ch. 12 axon hillock → Liu Ch. 7 threshold/refractory → Liu Ch. 2 AER.

*Critical contract:* Input dynamic range and leak; spike timing and identity; output bandwidth and latency. *Discriminating experiment:* Current sweep to spike timings and event transport under load.

**Turn changes in light into usable motion events.** Mead Chs. 7, 14–15 analog spatial computation → Liu Ch. 3 DVS/ATIS → Liu Ch. 15 event filtering/tracking.

*Critical contract:* Scene statistics, background activity, timestamps, downstream motion error. *Discriminating experiment:* Stationary versus moving scene and false-event rate at equal task latency.

**Build networks with configurable and learned responses.** Mead Ch. 5 amplifier/mismatch and Ch. 7 network → Liu Ch. 6 memory retention → Ch. 8 plastic synapses → Ch. 10 floating-gate tuning.

*Critical contract:* Stable state versus transient attractor activity, bounded weights, drift and learning interference. *Discriminating experiment:* Recall before/after additional learning, voltage/bias drift and calibration.

**Connect analog continuous-time sensing to an embodied event-based actuator.** Mead Chs. 9, 11, 16 filters → Liu Ch. 4 spike cochlea → Liu Ch. 5 central pattern generator → Ch. 14 software.

*Critical contract:* Bandwidth, sensor response, delays, actuator safety and closed-loop stability. *Discriminating experiment:* Compare real controlled device response to simpler digital filtered control.

**Compose neuromorphic arrays into systems.** Liu Ch. 2 arbiters and queueing → Ch. 12 AER circuits → Chs. 13–14 hardware/software infrastructure → Ch. 16 hierarchical routing.

*Critical contract:* AER saturation, event loss, timestamp fidelity, host and I/O energy. *Discriminating experiment:* Measure latency, drop rate, energy and task quality while increasing simultaneous activity.

## Glossary-first exploration is independent of question coverage

The domain-local [glossary](glossary.json) currently contains **401 unique concept identities** in 10 groups, plus redirects for true synonyms. Terms are divided between vocabulary seeded by these book landscapes and explicitly marked **adjacent candidates** (e.g. memristors, photonic neuromorphics and current hardware ecosystems). Adjacent candidates are possible future directions, **not** passages already verified from these two books.

No term needs a question, bridge, evidence node or user preference to be worth keeping. This is a discoverable landscape, not an empty slot that must be filled with artificial investigation questions. Use the viewer's **Vocabulary** tab to scan terms; click through to a question only when a real relationship exists. The current 28 curated ordinary questions and 20 canonical technical records intentionally cover only a minority of those terms.

## Next investigations without reindexing

1. **Start at the glossary or a real frustration.** Scan unfamiliar terms freely; selecting a term without linked research is legitimate. Choose a question only when it is helpful.
2. **Retrieve a known source location.** Search this guide by concept, inspect the corresponding chapter/subsection, and follow `book_landscaplets` in [investigation.json](investigation.json) for stable source IDs and printed-page scheme.
3. **Promote a lead into actual knowledge.** Read a discriminating derivation, circuit, diagram or experiment, record what it concretely establishes and what remains uncertain. The index entry's prior TOC status should not be silently upgraded.
4. **Preserve independent vocabulary.** New technical words may be appended to [glossary.json](glossary.json) with permanent IDs even if no current question maps to them. Never renumber existing term IDs.
5. **Compare whole-system outcomes.** A strong competence probe is a working event sensor/pipeline with measured event loss, false activity, timestamp preservation, latency, energy and task quality against a simpler baseline. Do not claim hardware success from a synthetic schema check.
6. **Avoid historical traps.** These volumes are 1989/2015 artifacts. The mechanism landscape remains valuable, but current process design rules, device models, software APIs and performance benchmarks require independent contemporary evidence.
