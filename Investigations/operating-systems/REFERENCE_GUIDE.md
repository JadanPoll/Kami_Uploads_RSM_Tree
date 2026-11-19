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
| 51 | Summary Dialogue on Distribution | 653–652 |
| 51 | Summary Dialogue on Distribution | 653–654 |

## How this relates to the question tree

The question tree starts from **“I want to build an OS!”** and keeps the childlike questions about running programs, using memory, talking to devices, and making files survive. Each question links to one or more routes in this reference. It does **not** need a separate copy of every chapter. The routes and chapter catalog are reusable across different investigations.

**Candidate C references vs established certificates:** A chapter range says where we expect to find clarity. It is not an established conclusion or a certificate that the claim is true. Once we investigate a question, specific passages, findings, limitations and observed behavior can form a certificate.

Structured source of truth: [`reference_guide.json`](reference_guide.json); question tree: [`question_tree.json`](question_tree.json).
