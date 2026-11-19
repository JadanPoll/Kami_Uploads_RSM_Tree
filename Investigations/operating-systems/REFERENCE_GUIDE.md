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

Structured source of truth: [`reference_guide.json`](reference_guide.json); question tree: [`question_tree.json`](question_tree.json).


## Hardware and bare-metal cross-references

These are **additional ways into the existing OS question tree**. Keep OSTEP for OS concepts; use the architecture texts to see what the processor actually provides, and *Making Embedded Systems* to compare software running without an OS. References are prospective reading leads, not established certificates.

| When I ask… | Book and chapter/section | Printed pages |
|---|---|---|
| What do I actually need an OS for? | MES: Ch. 1 — Introduction; MES: Ch. 6 — Managing the Flow of Activity; COD-RV: §1.3–1.4 — Below Your Program; Under the Covers; COD-ARM: §1.3–1.4 — Below Your Program; Under the Covers | MES chapter (range unverified); MES chapter (range unverified); COD-RV 13–24; COD-ARM 13–23 |
| How do I bring up hardware and get my program working? | MES: Ch. 3 — Getting Your Hands on the Hardware; COD-RV: §2.12 — Translating and Starting a Program; COD-ARM: §2.12 — Translating and Starting a Program | MES chapter (range unverified); COD-RV 131–139; COD-ARM 128–136 |
| How does a processor hand control to my OS when something happens? | COD-RV: §4.10 — Exceptions; COD-ARM: §4.9 — Exceptions; MES: Ch. 5 — Interrupts; MES: Ch. 6 — Managing the Flow of Activity | COD-RV 333–339; COD-ARM 336–341; MES chapter (range unverified); MES chapter (range unverified) |
| How do I talk to a device and know when it needs attention? | MES: Ch. 4 — Inputs, Outputs, and Timers; MES: Ch. 5 — Interrupts; MES: Ch. 7 — Communicating with Peripherals; MES: Ch. 8 — Putting Together a System | MES chapter (range unverified); MES chapter (range unverified); MES chapter (range unverified); MES chapter (range unverified) |
| What does the processor do when my OS gives a program virtual memory? | COD-RV: §5.7 — Virtual Memory; COD-ARM: §5.7 — Virtual Memory | COD-RV 440–463; COD-ARM 441–464 |
| If two cores have caches, how do they see each other's changes? | COD-RV: §5.10 — Cache Coherence; COD-ARM: §5.10 — Cache Coherence | COD-RV 475–478; COD-ARM 477–480 |
| What if my processor doesn't have enough memory, time, or power? | MES: Ch. 11 — Doing More with Less; MES: Ch. 13 — Reducing Power Consumption | MES chapter (range unverified); MES chapter (range unverified) |
| Why does my system hang, and how do I find out where? | MES: Ch. 9 — Getting into Trouble; MES: Ch. 3 — Getting Your Hands on the Hardware | MES chapter (range unverified); MES chapter (range unverified) |

[Making Embedded Systems](https://drive.google.com/file/d/1hU4l-fAivhO7f3b8ZZK58JOPTKysXzhl/view?usp=drivesdk) · [RISC-V architecture book](https://drive.google.com/file/d/1oLtJEtoD_edhxRXXp9NqBg0eqwdHDpjP/view?usp=drivesdk) · [ARM architecture book](https://drive.google.com/file/d/11keBAs8ZzIym0p4V_QEUfNtgjGH_91EA/view?usp=drivesdk)

**Boundary:** The processor books' program-start sections are not a replacement for a firmware/bootloader manual. The embedded book deliberately focuses on bare-metal software, not OS kernel implementation.

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
