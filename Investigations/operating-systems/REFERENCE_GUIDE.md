# I want to build an OS! — quick book reference

**Book:** [Operating Systems: Three Easy Pieces (OSTEP)](https://drive.google.com/file/d/1jyZtuBGG6C9WdbX6gT7ACTp5OQcICsDt/view?usp=drivesdk) — version 1.00 (2018).

Use this when you know what you want to inspect and need the chapter. **Page numbers are printed book pages, not PDF viewer positions.** All ranges below are inclusive.

## Find a chapter by the question you're asking

| I want to figure out… | OSTEP chapters | Printed pages |
|---|---|---|
| What is the OS supposed to do? | Ch. 2 | 3–22 |
| How does my code first take control of the machine? | Ch. 4, Ch. 6 | 25–64 |
| How does a program start, run and stop? | Ch. 4, Ch. 5, Ch. 6 | 25–64 |
| How do I decide what runs next? | Ch. 7, Ch. 8, Ch. 9, Ch. 10 | 65–116 |
| How does an address in a program reach memory? | Ch. 13, Ch. 14, Ch. 15, Ch. 16 | 121–166 |
| How do pages, page tables and free space work? | Ch. 17, Ch. 18, Ch. 19, Ch. 20 | 167–230 |
| What happens when RAM isn't enough? | Ch. 21, Ch. 22, Ch. 23 | 231–278 |
| Why do threads interfere with each other? | Ch. 26, Ch. 27, Ch. 28, Ch. 29 | 287–350 |
| How should threads wait, wake and cooperate? | Ch. 30, Ch. 31, Ch. 32 | 351–400 |
| Could I do this without a thread for every task? | Ch. 33 | 401–412 |
| How does my OS talk to a device? | Ch. 36, Ch. 37, Ch. 38 | 419–466 |
| How are files and directories represented? | Ch. 39, Ch. 40, Ch. 41 | 467–524 |
| What happens if the machine crashes while writing? | Ch. 42, Ch. 43, Ch. 44, Ch. 45 | 525–600 |
| Could my OS use a different machine? | Ch. 48, Ch. 49, Ch. 50 | 605–652 |

**Note on booting:** OSTEP's early chapters explain processes, direct execution and privilege, not a complete firmware/bootloader implementation guide. Boot-specific sources will need a separate reference route.

## Full chapter index

| Chapter | Title | Printed pages |
|---:|---|---:|
| 1 | A Dialogue on the Book | 1–2 |
| 2 | Introduction to Operating Systems | 3–22 |
| 3 | A Dialogue on Virtualization | 23–24 |
| 4 | The Abstraction: The Process | 25–36 |
| 5 | Interlude: Process API | 37–48 |
| 6 | Mechanism: Limited Direct Execution | 49–64 |
| 7 | Scheduling: Introduction | 65–76 |
| 8 | Scheduling: The Multi-Level Feedback Queue | 77–88 |
| 9 | Scheduling: Proportional Share | 89–102 |
| 10 | Multiprocessor Scheduling (Advanced) | 103–116 |
| 11 | Summary Dialogue on CPU Virtualization | 117–118 |
| 12 | A Dialogue on Memory Virtualization | 119–120 |
| 13 | The Abstraction: Address Spaces | 121–130 |
| 14 | Interlude: Memory API | 131–140 |
| 15 | Mechanism: Address Translation | 141–154 |
| 16 | Segmentation | 155–166 |
| 17 | Free-Space Management | 167–184 |
| 18 | Paging: Introduction | 185–198 |
| 19 | Paging: Faster Translations (TLBs) | 199–214 |
| 20 | Paging: Smaller Tables | 215–230 |
| 21 | Beyond Physical Memory: Mechanisms | 231–242 |
| 22 | Beyond Physical Memory: Policies | 243–260 |
| 23 | Complete Virtual Memory Systems | 261–278 |
| 24 | Summary Dialogue on Memory Virtualization | 279–284 |
| 25 | A Dialogue on Concurrency | 285–286 |
| 26 | Concurrency: An Introduction | 287–302 |
| 27 | Interlude: Thread API | 303–314 |
| 28 | Locks | 315–336 |
| 29 | Lock-based Concurrent Data Structures | 337–350 |
| 30 | Condition Variables | 351–366 |
| 31 | Semaphores | 367–384 |
| 32 | Common Concurrency Problems | 385–400 |
| 33 | Event-based Concurrency (Advanced) | 401–412 |
| 34 | Summary Dialogue on Concurrency | 413–416 |
| 35 | A Dialogue on Persistence | 417–418 |
| 36 | I/O Devices | 419–432 |
| 37 | Hard Disk Drives | 433–448 |
| 38 | Redundant Arrays of Inexpensive Disks (RAIDs) | 449–466 |
| 39 | Interlude: Files and Directories | 467–492 |
| 40 | File System Implementation | 493–510 |
| 41 | Locality and The Fast File System | 511–524 |
| 42 | Crash Consistency: FSCK and Journaling | 525–546 |
| 43 | Log-structured File Systems | 547–562 |
| 44 | Flash-based SSDs | 563–586 |
| 45 | Data Integrity and Protection | 587–600 |
| 46 | Summary Dialogue on Persistence | 601–602 |
| 47 | A Dialogue on Distribution | 603–604 |
| 48 | Distributed Systems | 605–620 |
| 49 | Sun’s Network File System (NFS) | 621–638 |
| 50 | The Andrew File System (AFS) | 639–652 |
| 51 | Summary Dialogue on Distribution | 653–654 |

## How this relates to the question tree

The question tree starts from **“I want to build an OS!”** and keeps the childlike questions about running programs, using memory, talking to devices, and making files survive. Each question links to one or more routes in this reference. It does **not** need a separate copy of every chapter. The routes and chapter catalog are reusable across different investigations.

**Candidate C references vs established certificates:** A chapter range says where we expect to find clarity. It is not an established conclusion or a certificate that the claim is true. Once we investigate a question, specific passages, findings, limitations and observed behavior can form a certificate.

Structured source of truth: [`investigation.json`](investigation.json), with `chapter_catalog`, `routes`, `cross_source_routes`, `source_catalogs`, `question_nodes`, and `curiosity_atlas` in one file.


## Embedded-systems and architecture shelf — indexed once

**Source folder:** [Embedded systems and computer architecture](https://drive.google.com/drive/folders/1Yfk9GlplruQzpIsPq7ks3fmMYNz7lFvS). This folder contains three **existing** OS investigation sources: [Making Embedded Systems](https://drive.google.com/file/d/1hU4l-fAivhO7f3b8ZZK58JOPTKysXzhl/view?usp=drivesdk) (MES), [Computer Organization and Design — RISC-V](https://drive.google.com/file/d/1oLtJEtoD_edhxRXXp9NqBg0eqwdHDpjP/view?usp=drivesdk) (COD-RV), and [Computer Organization and Design — ARM](https://drive.google.com/file/d/11keBAs8ZzIym0p4V_QEUfNtgjGH_91EA/view?usp=drivesdk) (COD-ARM). The book identities were already in the canonical JSON; the addition here is the deeper reusable map.

**Navigation convention:** Source catalogs are canonical in [`investigation.json`](investigation.json) under `source_catalogs.MES`, `source_catalogs.COD-RV`, and `source_catalogs.COD-ARM`. The architecture entries below report **printed page starts** transcribed from these exact PDFs' tables of contents; MES chapter starting pages are **not yet established**. They are not PDF-position offsets or verified Kami jumps. Book contents identify *candidate reading locations*; only the selected observations under `source_inspected_observations` were read more closely.

### What each book contributes to the OS question

| Book | Where it sits in the stack | Why it matters | Do not confuse it with… |
| --- | --- | --- | --- |
| **MES** — Elecia White, 2nd ed. (2024) | Firmware, board integration and resource-constrained software **without** an OS | Architecture, bare-metal main loops, state machines, IRQ timing, device buses, debugging, updates, power and physical behavior | A kernel implementation reference or a complete device-specific hardware manual |
| **COD-RV** — Patterson & Hennessy, RISC-V edition | Instructions, datapath, memory hierarchy, exceptions and multicore hardware | The machine-level mechanisms that OS schedulers, traps, memory translation and synchronization rely on | The complete RISC-V privileged architecture specification (needed for concrete supervisor configuration) |
| **COD-ARM** — Patterson & Hennessy, ARM edition | Comparable machine-level mechanisms with an ARM-centered teaching ISA | Architectural contrasts and the Cortex-A53 examples; useful alongside RISC-V | Real ARMv8-A instruction semantics: **LEGv8 is a deliberately simplified teaching subset**, not the complete architecture |

### Factorization: six capability boundaries

**Which OS functions genuinely need a privileged kernel?** A superloop, finite-state machine, IRQ handlers and peripheral drivers can run directly on hardware; adding multiple independently untrusted programs changes isolation, resource arbitration and recovery requirements.

*Retrieve:* MES Ch. 2, Ch. 5, Ch. 6, Ch. 8 · OSTEP Ch. 2, Ch. 4, Ch. 6 · LKD Ch. 3, Ch. 5. *Discriminate:* Try satisfying the actual device requirement bare-metal; identify the first unmet contract that justifies a scheduler, protection domain, or service boundary.

**How does a physical event become safe software action?** Hardware raises an event, the processor takes an exception/interrupt path, low-level code saves state and acknowledges it, and deferred work or a main loop completes the operation under timing and concurrency constraints.

*Retrieve:* MES Ch. 4, Ch. 5, Ch. 6 · COD-RV §4.10 · COD-ARM §4.9 · OSTEP Ch. 36 · LKD Ch. 7, Ch. 8. *Discriminate:* Measure worst-case IRQ-to-useful-response latency, including masking, handler time and deferred work; compare polling and interrupts.

**What lies beneath a process address and a memory fault?** The instruction set produces virtual addresses; translations and permissions affect access; caches and coherence determine performance/visibility, while the OS supplies mappings, allocation, page-fault and reclaim policies.

*Retrieve:* COD-RV §5.3, §5.7, §5.10 · COD-ARM §5.3, §5.7, §5.10 · OSTEP Chs. 13–23 · LKD Ch. 12, Ch. 15, Ch. 16. *Discriminate:* Differentiate translation/permission faults, physical memory pressure, cache misses and shared-memory ordering with their own measurements.

**What turns source code into control of a real device?** Compiler, assembler and linker produce an executable image; the processor executes instructions through an implementation, but firmware reset/boot handoff and board-specific peripheral setup remain platform contracts.

*Retrieve:* COD-RV §2.12, §4.3–4.10 · COD-ARM §2.12, §4.3–4.9 · MES Ch. 3, Ch. 9. *Discriminate:* Separate a hosted program startup example from reset vector, linker mapping, initialization, trap vector and actual bootloader responsibility.

**How do multiple cores share memory without silently corrupting progress?** ISA synchronization primitives, memory hierarchy/cache coherence and OS thread synchronization solve different pieces of the shared-memory problem. Coherence does not automatically provide atomicity for an application invariant.

*Retrieve:* COD-RV §2.11, §5.10 · COD-ARM §2.11, §5.10 · OSTEP Chs. 26–33 · TLPI Chs. 29–31. *Discriminate:* Construct a concurrent operation with well-defined ownership and measure whether the invariant survives interleavings and stalls.

**What makes a useful physical computer persist beyond a successful demo?** The device must bound memory, power, response times, peripheral errors, firmware update and recovery procedures; the OS may simplify services but does not by itself prove a safe physical session.

*Retrieve:* MES Ch. 8, Ch. 9, Ch. 10, Ch. 11, Ch. 13, Ch. 14 · OSTEP Ch. 42, Ch. 48. *Discriminate:* Exercise representative faults, resets, power limits and updates; check that controlled hardware reaches safe states and correctly recovers.

### MES — complete chapter map (2nd edition, 2024)

The source preface confirms that the examples operate bare-metal and describes each of these fourteen chapters. **Chapter titles and purposes are verified; printed starting pages remain unverified.** Use chapter names in Kami/Drive search rather than inventing offsets.

| Chapter | What it covers | Use it when… |
| ---: | --- | --- |
| 1 | Introduction | Bound the resource, timing and hardware interaction requirements before deciding whether an OS is necessary |
| 2 | Creating a System Architecture | Decompose requirements, data flows, module responsibilities and state before implementing drivers |
| 3 | Getting Your Hands on the Hardware | Bring up boards, inspect schematics and debug physical/software integration |
| 4 | Inputs, Outputs, and Timers | Implement concrete I/O, timers, observable hardware events and small diagnostics |
| 5 | Interrupts | Trace IRQ-to-ISR path, context, latency, nested priorities and short interrupt work |
| 6 | Managing the Flow of Activity | Compare cooperative main loop, event processing, finite-state machines and interrupt-driven execution |
| 7 | Communicating with Peripherals | Select UART/SPI/I2C/USB interfaces and understand framing, communication ownership and timing |
| 8 | Putting Together a System | Integrate LCD/ADC/flash/sensors with buffers, bandwidth and pipelines |
| 9 | Getting into Trouble | Trace hard faults, linker maps, stack corruption, reset and hardware-versus-code failure |
| 10 | Building Connected Devices | Handle connected-device lifecycle, updates, remote visibility, monitoring and security |
| 11 | Doing More with Less | Inspect RAM/flash/CPU budget, memory layout and measurement-driven optimization |
| 12 | Math | Reason about arithmetic representation, fixed point, floating point and numeric limitations |
| 13 | Reducing Power Consumption | Trade sleep/wakeup, latency, energy and always-on requirements |
| 14 | Motors and Movement | Connect firmware timing and control loops to motors, sensing and physical movement |

**Inspected technical nugget — interrupt latency (MES Ch. 5):** the processor's interrupt entry latency and the system's worst-case latency are different. The latter includes time spent with interrupts disabled; long handlers and context management increase response time. An ISR's existence is not itself evidence of meeting a physical deadline. This was read from the book text, though its printed page number is not established.

### RISC-V and ARM — complete six-chapter top-level maps

Both editions use a parallel progression but differ in concrete instruction-set examples and section numbering. **Do not assume the same numbered section covers an identical topic:** for example, exceptions are **RISC-V §4.10 (p. 333)** versus **ARM §4.9 (p. 336)**.

| Ch. | RISC-V edition (printed start) | ARM edition (printed start) | Why this level matters |
| ---: | --- | --- | --- |
| 1 | Computer Abstractions and Technology — **p. 2** | Computer Abstractions and Technology — **p. 2** | Hardware/software abstraction, measured performance, power and the OS's placement |
| 2 | Instructions: Language of the Computer — **p. 66** | Instructions: Language of the Computer — **p. 60** | ISA instruction and call conventions, atomic operations, translation/linking/starting a program |
| 3 | Arithmetic for Computers — **p. 188** | Arithmetic for Computers — **p. 186** | Representations and arithmetic behavior affecting correctness and numerical limits |
| 4 | The Processor — **p. 252** | The Processor — **p. 254** | Datapath/pipeline, hazards, exceptions and machine-level control transfer |
| 5 | Large and Fast: Exploiting Memory Hierarchy — **p. 386** | Large and Fast: Exploiting Memory Hierarchy — **p. 386** | Caches, virtual machines/memory, translation and coherence |
| 6 | Parallel Processors from Client to Cloud — **p. 518** | Parallel Processors from Client to Cloud — **p. 514** | Multicore execution, synchronization context, parallel hardware and cluster boundaries |

### Targeted hardware lookup: OS question → exact printed section

| Problem | RISC-V | ARM | What this helps establish |
| --- | --- | --- | --- |
| How does source code become executable work? | §2.12 Translating and Starting a Program — **p. 131** | §2.12 Translating and Starting a Program — **p. 128** | Compiler/linker/startup concepts, **not** the firmware-to-kernel boot process |
| Why do two threads need atomic operations? | §2.11 Parallelism and Instructions: Synchronization — **p. 128** | §2.11 Parallelism and Instructions: Synchronization — **p. 125** | ISA synchronization primitives, distinct from the correct application-level invariant |
| What is the processor executing and how? | §4.3 Building a Datapath — **p. 261** | §4.3 Building a Datapath — **p. 263** | Datapath construction and implementation constraints |
| What makes a pipeline stall or forward data? | §4.8 Data Hazards: Forwarding versus Stalling — **p. 313** | §4.7 Data Hazards: Forwarding versus Stalling — **p. 316** | Dependencies, stalls and forwarding mechanisms |
| How does the processor transfer control on an exception? | §4.10 Exceptions — **p. 333** | §4.9 Exceptions — **p. 336** | Hardware exception concepts; platform trap details need the relevant privileged specification |
| What is virtual memory below an OS page table? | §5.7 Virtual Memory — **p. 440** | §5.7 Virtual Memory — **p. 441** | Virtual address translation, mappings and hardware-facing concepts |
| How do caches accelerate, but also complicate, memory? | §5.3 The Basics of Caches — **p. 398** | §5.3 The Basics of Caches — **p. 397** | Locality and the cache hierarchy |
| How do multiple cores keep their cache contents coherent? | §5.10 Parallelism and Memory Hierarchy: Cache Coherence — **p. 475** | §5.10 Parallelism and Memory Hierarchy: Cache Coherence — **p. 477** | Cache coherence, **not** guaranteed application atomicity |
| Why is multicore parallelism difficult? | §6.2 The Difficulty of Creating Parallel Processing Programs — **p. 522** | §6.2 The Difficulty of Creating Parallel Processing Programs — **p. 518** | Parallel programming difficulty and cross-core design tradeoffs |
| What is the cost of hardware multithreading? | §6.4 Hardware Multithreading — **p. 534** | §6.4 Hardware Multithreading — **p. 530** | Latency hiding versus resource contention |
| Where do dedicated accelerators and clusters fit? | §6.7 Domain-Specific Architectures — **p. 549** | §6.6 Introduction to Graphics Processing Units — **p. 538** | Parallel hardware landscape; different topics at the same section number |

**Important practical distinctions:** `COD-RV` and `COD-ARM` have complete chapter and subsection-start catalogs in the canonical JSON (115 and 105 entries). This Markdown section surfaces the highest-value OS intersections rather than repeating every textbook section. In the ARM PDF, the authors explicitly distinguish LEGv8 from the full ARMv8 instruction set. In the RISC-V edition's further reading, the authors refer readers to the privileged architecture manual for detailed privilege and address-protection mechanisms.

### High-information paths that combine the shelf with the OS books

| Starting failure or ambition | First sources | What to differentiate |
| --- | --- | --- |
| A board never reaches my program | MES Chs. 3, 9; COD-RV/ARM §2.12; target board startup spec | Wrong image/reset vector/linker placement vs driver initialization vs actual bootloader handoff |
| Interrupt fires but hardware misses a deadline | MES Chs. 4–6; COD-RV §4.10 or ARM §4.9; LKD Chs. 7–8 | CPU entry latency, interrupt-masked time, ISR cost and deferred-work delay |
| Busy main loop versus small OS scheduler | MES Chs. 2, 6; OSTEP Chs. 4–10 | What tasks are independently schedulable, who owns timing, and whether isolation is needed |
| Virtual addresses or cache effects make memory behavior surprising | COD-RV/ARM §§5.3, 5.7, 5.10; OSTEP Chs. 13–23; LKD Chs. 12, 15–16 | Page translation, resident-memory pressure, cache/locality and ordering are distinct mechanisms |
| I need multiple cooperative peripherals without data loss | MES Chs. 7–8; LKD Chs. 7–8; TLPI Ch. 63 | Device protocol and buffers vs driver work queues and nonblocking program interfaces |
| An embedded device hangs after hours or after an update | MES Chs. 9–11, 13; OSTEP persistence; TLPI process lifecycle | Reproducible fault trace, reset/supervision path, persistent state and power-dependent failure |
| A robot controller must not harm its hardware on stalls | MES Chs. 5–6, 13–14; OSTEP Ch. 7; platform timing documentation | Deadline guarantees and safe state, not merely benchmark throughput |

### Long-term retrieval rule

On a future OS question, **search this guide or the canonical `source_catalogs` first**. Reuse the existing `MES`, `COD-RV`, and `COD-ARM` source IDs. Open only the relevant section, record newly inspected mechanism/evidence with its actual page scheme, and update an existing technical node or source route instead of cloning a question tree or reindexing the books. The embedded folder is a *shelf*, not a new independent research database.


## Linux programming and kernel references

OSTEP is not the whole OS library. For each question below, use [The Linux Programming Interface](https://drive.google.com/file/d/1fT4Nqq2d5-UnQxZpnDioEar0C5N0Sd8l/view?usp=drivesdk) (TLPI) to examine **what applications can ask the OS to do**, and [Linux Kernel Development](https://drive.google.com/file/d/11yI22zgg2Rka_Nj2Kbv2UW7bMqe5sua0/view?usp=drivesdk) (LKD) to examine **how a 2010-era Linux kernel implemented related mechanisms**.

**All ranges use printed book page numbers, inclusive.** These are lookup references, not established RSM certificates.

| What do I want to look up? | TLPI chapters and pages | LKD chapters and pages |
|---|---|---|
| What is the OS supposed to do? | Ch. 2 (21–42), Ch. 3 (43–68) | Ch. 1 (1–10), Ch. 2 (11–22) |
| How does my code first take control of the machine? | Ch. 27 (563–590), Ch. 28 (591–616) | Ch. 2 (11–22), Ch. 5 (69–84) |
| How does a program start, run and stop? | Ch. 6 (113–138), Ch. 24 (513–530), Ch. 25 (531–540), Ch. 26 (541–562), Ch. 27 (563–590), Ch. 28 (591–616) | Ch. 3 (23–40), Ch. 5 (69–84) |
| How do I decide what runs next? | Ch. 23 (479–512), Ch. 35 (733–752) | Ch. 4 (41–68), Ch. 11 (207–230) |
| How does an address in a program reach memory? | Ch. 7 (139–152), Ch. 49 (1017–1044), Ch. 50 (1045–1056) | Ch. 15 (305–322) |
| How do pages, page tables and free space work? | Ch. 49 (1017–1044), Ch. 50 (1045–1056) | Ch. 12 (231–260), Ch. 15 (305–322) |
| What happens when RAM isn't enough? | Ch. 7 (139–152), Ch. 49 (1017–1044), Ch. 50 (1045–1056) | Ch. 12 (231–260), Ch. 16 (323–336) |
| Why do threads interfere with each other? | Ch. 29 (617–630), Ch. 30 (631–654), Ch. 31 (655–670) | Ch. 9 (161–174), Ch. 10 (175–206) |
| How should threads wait, wake and cooperate? | Ch. 30 (631–654), Ch. 31 (655–670), Ch. 43 (877–888), Ch. 47 (965–996), Ch. 53 (1089–1106), Ch. 55 (1117–1148) | Ch. 9 (161–174), Ch. 10 (175–206) |
| Could I do this without a thread for every task? | Ch. 20 (387–420), Ch. 21 (421–446), Ch. 22 (447–478), Ch. 63 (1325–1374) | Ch. 7 (113–132), Ch. 8 (133–160) |
| How does my OS talk to a device? | Ch. 3 (43–68), Ch. 4 (69–88), Ch. 23 (479–512), Ch. 63 (1325–1374) | Ch. 7 (113–132), Ch. 8 (133–160), Ch. 14 (289–304), Ch. 17 (337–362) |
| How are files and directories represented? | Ch. 4 (69–88), Ch. 5 (89–112), Ch. 14 (251–278), Ch. 18 (339–374) | Ch. 13 (261–288), Ch. 14 (289–304) |
| What happens if the machine crashes while writing? | Ch. 4 (69–88), Ch. 5 (89–112), Ch. 13 (233–250), Ch. 14 (251–278) | Ch. 14 (289–304), Ch. 16 (323–336) |
| Could my OS use a different machine? | Ch. 43 (877–888), Ch. 44 (889–920), Ch. 56 (1149–1164), Ch. 57 (1165–1178), Ch. 58 (1179–1196), Ch. 59 (1197–1238), Ch. 60 (1239–1252) | — |

### Complete chapter catalogs

**TLPI — all 64 chapters**

| Ch. | Chapter title | Printed pages |
|---:|---|---:|
| 1 | History and Standards | 1–20 |
| 2 | Fundamental Concepts | 21–42 |
| 3 | System Programming Concepts | 43–68 |
| 4 | File I/O: The Universal I/O Model | 69–88 |
| 5 | File I/O: Further Details | 89–112 |
| 6 | Processes | 113–138 |
| 7 | Memory Allocation | 139–152 |
| 8 | Users and Groups | 153–166 |
| 9 | Process Credentials | 167–184 |
| 10 | Time | 185–210 |
| 11 | System Limits and Options | 211–222 |
| 12 | System and Process Information | 223–232 |
| 13 | File I/O Buffering | 233–250 |
| 14 | File Systems | 251–278 |
| 15 | File Attributes | 279–310 |
| 16 | Extended Attributes | 311–318 |
| 17 | Access Control Lists | 319–338 |
| 18 | Directories and Links | 339–374 |
| 19 | Monitoring File Events | 375–386 |
| 20 | Signals: Fundamental Concepts | 387–420 |
| 21 | Signals: Signal Handlers | 421–446 |
| 22 | Signals: Advanced Features | 447–478 |
| 23 | Timers and Sleeping | 479–512 |
| 24 | Process Creation | 513–530 |
| 25 | Process Termination | 531–540 |
| 26 | Monitoring Child Processes | 541–562 |
| 27 | Program Execution | 563–590 |
| 28 | Process Creation and Program Execution in More Detail | 591–616 |
| 29 | Threads: Introduction | 617–630 |
| 30 | Threads: Thread Synchronization | 631–654 |
| 31 | Threads: Thread Safety and Per-Thread Storage | 655–670 |
| 32 | Threads: Thread Cancellation | 671–680 |
| 33 | Threads: Further Details | 681–698 |
| 34 | Process Groups, Sessions, and Job Control | 699–732 |
| 35 | Process Priorities and Scheduling | 733–752 |
| 36 | Process Resources | 753–766 |
| 37 | Daemons | 767–782 |
| 38 | Writing Secure Privileged Programs | 783–796 |
| 39 | Capabilities | 797–816 |
| 40 | Login Accounting | 817–832 |
| 41 | Fundamentals of Shared Libraries | 833–858 |
| 42 | Advanced Features of Shared Libraries | 859–876 |
| 43 | Interprocess Communication Overview | 877–888 |
| 44 | Pipes and FIFOs | 889–920 |
| 45 | Introduction to System V IPC | 921–936 |
| 46 | System V Message Queues | 937–964 |
| 47 | System V Semaphores | 965–996 |
| 48 | System V Shared Memory | 997–1016 |
| 49 | Memory Mappings | 1017–1044 |
| 50 | Virtual Memory Operations | 1045–1056 |
| 51 | Introduction to POSIX IPC | 1057–1062 |
| 52 | POSIX Message Queues | 1063–1088 |
| 53 | POSIX Semaphores | 1089–1106 |
| 54 | POSIX Shared Memory | 1107–1116 |
| 55 | File Locking | 1117–1148 |
| 56 | Sockets: Introduction | 1149–1164 |
| 57 | Sockets: UNIX Domain | 1165–1178 |
| 58 | Sockets: Fundamentals of TCP/IP Networks | 1179–1196 |
| 59 | Sockets: Internet Domains | 1197–1238 |
| 60 | Sockets: Server Design | 1239–1252 |
| 61 | Sockets: Advanced Topics | 1253–1288 |
| 62 | Terminals | 1289–1324 |
| 63 | Alternative I/O Models | 1325–1374 |
| 64 | Pseudoterminals | 1375–1400 |

**Linux Kernel Development — all 20 chapters**

| Ch. | Chapter title | Printed pages |
|---:|---|---:|
| 1 | Introduction to the Linux Kernel | 1–10 |
| 2 | Getting Started with the Kernel | 11–22 |
| 3 | Process Management | 23–40 |
| 4 | Process Scheduling | 41–68 |
| 5 | System Calls | 69–84 |
| 6 | Kernel Data Structures | 85–112 |
| 7 | Interrupts and Interrupt Handlers | 113–132 |
| 8 | Bottom Halves and Deferring Work | 133–160 |
| 9 | An Introduction to Kernel Synchronization | 161–174 |
| 10 | Kernel Synchronization Methods | 175–206 |
| 11 | Timers and Time Management | 207–230 |
| 12 | Memory Management | 231–260 |
| 13 | The Virtual Filesystem | 261–288 |
| 14 | The Block I/O Layer | 289–304 |
| 15 | The Process Address Space | 305–322 |
| 16 | The Page Cache and Page Writeback | 323–336 |
| 17 | Devices and Modules | 337–362 |
| 18 | Debugging | 363–378 |
| 19 | Portability | 379–394 |
| 20 | Patches, Hacking, and the Community | 395–406 |

**Important:** LKD's 2010 implementation details are historical; use current Linux source/documentation for exact present-day interfaces. TLPI's system-call descriptions and OSTEP's design concepts have different roles. *Making Embedded Systems* chapters currently have verified titles but unverified printed page boundaries.
