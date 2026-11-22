# Robotics — persistent three-book factorization and research navigator

**Source shelf:** [three exact Drive PDFs](https://drive.google.com/drive/folders/19cCUGF1zFASTTVcYnyMTK8mrEV6F7MEp) · **Canonical evidence and questions:** [`investigation.json`](investigation.json) · **Independently browsable vocabulary:** [`glossary.json`](glossary.json) · **Atlas:** view `robotics-curiosities` in the shared Knowledge Atlas.

**Before reindexing:** this catalog already stores **43 numbered chapters**, **458 numbered subsection starts**, **12 appendix locations**, selected examined passages, and source-to-question routes. Extend the specific uncertain location rather than repeating an entire TOC scan. Numbers are retrieval coverage, not established learning or validated robot performance.

## The factorization: a robot is a composition, not a book outline

| Independent decision | Questions that distinguish real alternatives | Why it matters |
| --- | --- | --- |
| Embodiment and constraints | Articulated arm, differential rover, omniwheel base, fixed-wing aircraft, multirotor, legged system? Can it move sideways, hover, make contact? | Changes admissible controls and paths; general software APIs cannot erase physics |
| State and geometry | Configuration vs task space; SE(3) frames; joint angles, pose, velocity, map; what is observable? | Prevents 'valid numbers, wrong frame' and singular/reachability errors |
| Physical transition | Rigid-body/actuator dynamics, friction, contact, aerodynamic lift, wind and saturation? | Turns ideal commands into actual acceleration and possible failure |
| Measurement and inference | Which observables, models, noise processes and ambiguous hypotheses? Gaussian, particles, graph constraints? | Separates sensor facts from inferred world-state beliefs |
| Decisions and planning | Is the objective a trajectory, collision-free path, information gain, or manipulation? Is state known? | Changes whether a geometric planner, MDP, belief policy or active sensing is appropriate |
| Action and feedback | Does a loop regulate pose, joint torque, force, flight attitude, course or airspeed? What bandwidth/saturation contract? | Prevents incompatible controller composition and contact damage |
| Evidence and integration | Which simulator, ground truth, hardware disturbances, latency, recovery and task outcomes matter? | Passing equations and nominal sims do not establish operational capability |

**Higher-order pattern:** the three books show different sorts of factorization: (1) **kinematic composition**: a chain of screw motions maps joints to end-effector pose (Modern Robotics §4.1); (2) **probabilistic conditional independence**: conditioned on a robot path, FastSLAM separates landmark estimators (Probabilistic Robotics §13.2); (3) **control hierarchy**: fast inner aircraft loops support slower outer loops, subject to actuator limits (Small Unmanned Aircraft §§6.1–6.2). These are analogous as compositional designs, **not equivalent mathematical factorizations**. If their prerequisites fail—rigid chain assumptions, correct path/correspondence hypotheses, or bandwidth/saturation separation—the decomposition's practical usefulness changes.

## Three exact books and what they contribute

| Book (open original) | Distinctive capability | Known boundary | Catalog |
| --- | --- | --- | ---: |
| [Probabilistic Robotics](https://drive.google.com/file/d/1NqxGKSV7M4pMbBN_BdcKSYKbGzGHkuxm/view) | Recursive probabilistic state estimation, localization, mapping, SLAM and decision-making under uncertainty | Algorithms and examples reflect publication period; model assumptions, real-time compute and sensor limitations must be checked for a target system. | 17 chapters, 243 subsection starts |
| [Modern Robotics: Mechanics, Planning, and Control](https://drive.google.com/file/d/1wKeNmtPvxRGkb_MabBjqb4-Iq-s2eBIf/view) | Rigid motion and mechanism geometry, kinematics, dynamics, manipulation, planning and feedback control | Preprint pagination used; it is not necessarily identical to printed editions. Mechanical feasibility, calibration and model validity are task-dependent. | 13 chapters, 161 subsection starts |
| [Small Unmanned Aircraft: Theory and Practice](https://drive.google.com/file/d/10hEU6VDGJLBcdHa6kqrgkgwhkZkdJpyv/view) | Fixed-wing aircraft modeling, trim, successive-loop autopilots, state estimation, waypoint guidance, vision and end-to-end simulation | Specifically fixed-wing small/miniature aircraft, not a generic multicopter controller; design examples do not certify real-aircraft safety. | 13 chapters, 54 subsection starts |

**Page scheme:** all following numeric starts are the books' **printed pages as seen in their connected PDF contents**, **not verified PDF viewer offsets**. The Modern Robotics file is the May 2017 preprint. Open the precise PDF and navigate by chapter/printed page; a tested Kami page-level deep-link has not yet been established.

## Complete numbered-chapter shelf

Book source IDs are stable. Each chapter maps to sections/subsections in `investigation.json`; all chapter-level titles below are TOC evidence, not claims that every chapter was read.

### Probabilistic Robotics
[Open exact PDF](https://drive.google.com/file/d/1NqxGKSV7M4pMbBN_BdcKSYKbGzGHkuxm/view)

| Chapter | Printed start | Mechanism / use |
| ---: | ---: | --- |
| 1 · Introduction | 3 | Why robot uncertainty matters |
| 2 · Recursive State Estimation | 13 | Recursive belief updates and probabilistic state |
| 3 · Gaussian Filters | 39 | Kalman, EKF, UKF and information filters |
| 4 · Nonparametric Filters | 85 | Grid, histogram, particle and nonparametric inference |
| 5 · Robot Motion | 117 | Probabilistic velocity and odometry motion models |
| 6 · Robot Perception | 149 | Range sensor likelihood and landmark measurements |
| 7 · Mobile Robot Localization: Markov and Gaussian | 191 | Markov/EKF localization and correspondence |
| 8 · Mobile Robot Localization: Grid And Monte Carlo | 237 | Grid and Monte Carlo localization |
| 9 · Occupancy Grid Mapping | 281 | Occupancy mapping and inverse sensor models |
| 10 · Simultaneous Localization and Mapping | 309 | EKF SLAM with known/unknown association |
| 11 · The GraphSLAM Algorithm | 337 | Graph constraints and inference for SLAM |
| 12 · The Sparse Extended Information Filter | 385 | Sparse information representation and map merging |
| 13 · The FastSLAM Algorithm | 437 | Factored trajectory/landmark inference with FastSLAM |
| 14 · Markov Decision Processes | 487 | Decision-making with observable state |
| 15 · Partially Observable Markov Decision Processes | 513 | Belief-space POMDPs and information-seeking actions |
| 16 · Approximate POMDP Techniques | 547 | Approximate partially observable planning |
| 17 · Exploration | 569 | Exploration and entropy/information-gain choices |

### Modern Robotics: Mechanics, Planning, and Control
[Open exact PDF](https://drive.google.com/file/d/1wKeNmtPvxRGkb_MabBjqb4-Iq-s2eBIf/view)

| Chapter | Printed start | Mechanism / use |
| ---: | ---: | --- |
| 1 · Preview | 1 | Whole-robot architecture and motion vocabulary |
| 2 · Configuration Space | 11 | Configuration manifolds and constraints |
| 3 · Rigid-Body Motions | 59 | SE(3), rigid transforms, twists and wrenches |
| 4 · Forward Kinematics | 137 | Forward kinematics and product of exponentials |
| 5 · Velocity Kinematics and Statics | 171 | Velocity Jacobians, singularities and manipulability |
| 6 · Inverse Kinematics | 219 | Analytic/numerical inverse kinematics |
| 7 · Kinematics of Closed Chains | 245 | Closed-chain and parallel mechanisms |
| 8 · Dynamics of Open Chains | 271 | Actuator/link dynamics, inverse and forward dynamics |
| 9 · Trajectory Generation | 325 | Trajectory timing and dynamic feasibility |
| 10 · Motion Planning | 353 | Geometric collision-free planning, grids and sampling |
| 11 · Robot Control | 403 | Feedback, force, hybrid and impedance control |
| 12 · Grasping and Manipulation | 461 | Contact, friction, form/force closure and manipulation |
| 13 · Wheeled Mobile Robots | 513 | Wheeled mobile models, rolling constraints and odometry |

**Appendices:** A Summary of Useful Formulas (p. 565) · B Other Representations of Rotations (p. 575) · C Denavit–Hartenberg Parameters (p. 585) · D Optimization and Lagrange Multipliers (p. 597)

### Small Unmanned Aircraft: Theory and Practice
[Open exact PDF](https://drive.google.com/file/d/10hEU6VDGJLBcdHa6kqrgkgwhkZkdJpyv/view)

| Chapter | Printed start | Mechanism / use |
| ---: | ---: | --- |
| 1 · Introduction | 1 | Aircraft system architecture and end-to-end simulator |
| 2 · Coordinate Frames | 8 | Frames, rotations and air/ground/wind velocities |
| 3 · Kinematics and Dynamics | 28 | Six-DOF kinematics and aircraft rigid-body dynamics |
| 4 · Forces and Moments | 39 | Aerodynamic, propulsion and disturbance forces/moments |
| 5 · Linear Design Models | 60 | Trim, linearization, mode structure and design models |
| 6 · Autopilot Design Using Successive Loop Closure | 95 | Cascaded autopilot loops, saturation and PID |
| 7 · Sensors for MAVs | 120 | IMU, pressure, compass and GPS sensor models |
| 8 · State Estimation | 143 | Continuous-discrete observers, attitude and GPS estimation |
| 9 · Design Models for Guidance | 164 | Closed-loop guidance models |
| 10 · Straight-line and Orbit Following | 174 | Straight-line and orbit path following |
| 11 · Path Manager | 187 | Waypoint transitions and fixed-radius Dubins paths |
| 12 · Path Planning | 206 | Point-to-point and coverage planning |
| 13 · Vision-guided Navigation | 226 | Camera/gimbal projection, geolocation and precision landing |

**Appendices:** A Nomenclature and Notation (p. 247) · B Quaternions (p. 254) · C Animations in Simulink (p. 260) · D Modeling in Simulink Using S-Functions (p. 270) · E Airframe Parameters (p. 275) · F Trim and Linearization in Simulink (p. 277) · G Essentials from Probability Theory (p. 286) · H Sensor Parameters (p. 288)

## High-value subsection retrieval shelf

This table samples discriminating material rather than restating every subsection. **Examined** means a relevant passage was inspected in the PDF text; **TOC** means a navigation lead only.

### Probabilistic Robotics

| Section | Printed page | Why retrieve it | Evidence |
| --- | ---: | --- | --- |
| §2.4.1 · The Bayes Filter Algorithm | 26 | The Bayes Filter Algorithm | **Examined passage** |
| §2.4.4 · The Markov Assumption | 33 | The Markov Assumption | TOC lead |
| §3.2 · The Kalman Filter | 40 | The Kalman Filter | TOC lead |
| §3.3 · The Extended Kalman Filter | 54 | The Extended Kalman Filter | TOC lead |
| §3.4 · The Unscented Kalman Filter | 65 | The Unscented Kalman Filter | TOC lead |
| §4.3 · The Particle Filter | 96 | The Particle Filter | **Examined passage** |
| §4.3.4 · Practical Considerations and Properties of Particle Filters | 104 | Practical Considerations and Properties of Particle Filters | TOC lead |
| §5.3 · Velocity Motion Model | 121 | Velocity Motion Model | TOC lead |
| §5.4 · Odometry Motion Model | 132 | Odometry Motion Model | TOC lead |
| §6.3 · Beam Models of Range Finders | 153 | Beam Models of Range Finders | TOC lead |
| §6.4 · Likelihood Fields for Range Finders | 169 | Likelihood Fields for Range Finders | **Examined passage** |
| §6.6 · Feature-Based Measurement Models | 176 | Feature-Based Measurement Models | TOC lead |
| §7.5 · Estimating Correspondences | 215 | Estimating Correspondences | TOC lead |
| §8.3 · Monte Carlo Localization | 250 | Monte Carlo Localization | TOC lead |
| §8.3.5 · Random Particle MCL: Recovery from Failures | 256 | Random Particle MCL: Recovery from Failures | TOC lead |
| §9.2 · The Occupancy Grid Mapping Algorithm | 284 | The Occupancy Grid Mapping Algorithm | TOC lead |
| §10.3 · EKF SLAM with Unknown Correspondences | 323 | EKF SLAM with Unknown Correspondences | TOC lead |
| §11.2 · Intuitive Description | 340 | Intuitive Description | **Examined passage** |
| §11.5 · Data Association in GraphSLAM | 362 | Data Association in GraphSLAM | TOC lead |
| §12.5 · Sparsification | 398 | Sparsification | TOC lead |
| §13.2 · Factoring the SLAM Posterior | 439 | Factoring the SLAM Posterior | **Examined passage** |
| §13.2.1 · Mathematical Derivation of the Factored SLAM Posterior | 442 | Mathematical Derivation of the Factored SLAM Posterior | TOC lead |
| §13.9 · FastSLAM for Feature-Based Maps | 468 | FastSLAM for Feature-Based Maps | TOC lead |
| §14.3 · Value Iteration | 495 | Value Iteration | TOC lead |
| §15.4 · Mathematical Derivation of POMDPs | 531 | Mathematical Derivation of POMDPs | TOC lead |
| §16.4 · Monte Carlo POMDPs | 559 | Monte Carlo POMDPs | TOC lead |
| §17.2.1 · Information Gain | 571 | Information Gain | **Examined passage** |
| §17.4 · Exploration for Learning Occupancy Grid Maps | 580 | Exploration for Learning Occupancy Grid Maps | TOC lead |
| §17.5 · Exploration for SLAM | 593 | Exploration for SLAM | TOC lead |

### Modern Robotics: Mechanics, Planning, and Control

| Section | Printed page | Why retrieve it | Evidence |
| --- | ---: | --- | --- |
| §2.3 · Configuration Space: Topology and Representation | 23 | Configuration Space: Topology and Representation | TOC lead |
| §2.4 · Configuration and Velocity Constraints | 29 | Configuration and Velocity Constraints | TOC lead |
| §3.1 · Rigid-Body Motions in the Plane | 62 | Rigid-Body Motions in the Plane | TOC lead |
| §3.2 · Rotations and Angular Velocities | 68 | Rotations and Angular Velocities | TOC lead |
| §3.3 · Rigid-Body Motions and Twists | 89 | Rigid-Body Motions and Twists | TOC lead |
| §4.1 · Product of Exponentials Formula | 140 | Product of Exponentials Formula | **Examined passage** |
| §4.2 · The Universal Robot Description Format | 152 | The Universal Robot Description Format | TOC lead |
| §5.1 · Manipulator Jacobian | 178 | Manipulator Jacobian | **Examined passage** |
| §5.3 · Singularity Analysis | 191 | Singularity Analysis | TOC lead |
| §6.2 · Numerical Inverse Kinematics | 226 | Numerical Inverse Kinematics | TOC lead |
| §7.3 · Singularities | 256 | Singularities | TOC lead |
| §8.3.2 · Newton-Euler Inverse Dynamics Algorithm | 294 | Newton-Euler Inverse Dynamics Algorithm | **Examined passage** |
| §8.9 · Actuation, Gearing, and Friction | 303 | Actuation, Gearing, and Friction | TOC lead |
| §9.2 · Point-to-Point Trajectories | 326 | Point-to-Point Trajectories | TOC lead |
| §9.4 · Time-Optimal Time Scaling | 336 | Time-Optimal Time Scaling | TOC lead |
| §10.2 · Foundations | 358 | Foundations | **Examined passage** |
| §10.4 · Grid Methods | 369 | Grid Methods | TOC lead |
| §10.5 · Sampling Methods | 378 | Sampling Methods | **Examined passage** |
| §11.4 · Motion Control with Torque or Force Inputs | 420 | Motion Control with Torque or Force Inputs | TOC lead |
| §11.6 · Hybrid Motion–Force Control | 437 | Hybrid Motion–Force Control | TOC lead |
| §11.7 · Impedance Control | 441 | Impedance Control | **Examined passage** |
| §12.1 · Contact Kinematics | 463 | Contact Kinematics | TOC lead |
| §12.2 · Contact Forces and Friction | 484 | Contact Forces and Friction | TOC lead |
| §12.2.1 · Friction | 484 | Friction | **Examined passage** |
| §13.2 · Omnidirectional Wheeled Mobile Robots | 515 | Omnidirectional Wheeled Mobile Robots | TOC lead |
| §13.3 · Nonholonomic Wheeled Mobile Robots | 520 | Nonholonomic Wheeled Mobile Robots | TOC lead |
| §13.4 · Odometry | 546 | Odometry | TOC lead |

### Small Unmanned Aircraft: Theory and Practice

| Section | Printed page | Why retrieve it | Evidence |
| --- | ---: | --- | --- |
| §1.1 · System Architecture | 1 | System Architecture | TOC lead |
| §1.3 · Design Project | 6 | Design Project | TOC lead |
| §2.3 · Airspeed, Wind Speed, and Ground Speed | 18 | Airspeed, Wind Speed, and Ground Speed | TOC lead |
| §2.4 · The Wind Triangle | 20 | The Wind Triangle | TOC lead |
| §3.3 · Rigid-body Dynamics | 31 | Rigid-body Dynamics | TOC lead |
| §4.2 · Aerodynamic Forces and Moments | 40 | Aerodynamic Forces and Moments | **Examined passage** |
| §4.4 · Atmospheric Disturbances | 54 | Atmospheric Disturbances | TOC lead |
| §5.3 · Trim Conditions | 65 | Trim Conditions | **Examined passage** |
| §5.4 · Transfer Function Models | 68 | Transfer Function Models | TOC lead |
| §5.5 · Linear State-space Models | 77 | Linear State-space Models | TOC lead |
| §6.1 · Successive Loop Closure | 95 | Successive Loop Closure | TOC lead |
| §6.2 · Saturation Constraints and Performance | 97 | Saturation Constraints and Performance | **Examined passage** |
| §6.3 · Lateral-directional Autopilot | 99 | Lateral-directional Autopilot | TOC lead |
| §6.4 · Longitudinal Autopilot | 105 | Longitudinal Autopilot | TOC lead |
| §7.1 · Accelerometers | 120 | Accelerometers | TOC lead |
| §7.5 · Global Positioning System | 134 | Global Positioning System | TOC lead |
| §8.5 · Derivation of the Continuous-discrete Kalman Filter | 151 | Derivation of the Continuous-discrete Kalman Filter | **Examined passage** |
| §8.6 · Attitude Estimation | 156 | Attitude Estimation | TOC lead |
| §9.2 · Kinematic Model of Controlled Flight | 165 | Kinematic Model of Controlled Flight | TOC lead |
| §10.1 · Straight-line Path Following | 175 | Straight-line Path Following | TOC lead |
| §10.2 · Orbit Following | 181 | Orbit Following | TOC lead |
| §11.1 · Transitions Between Waypoints | 187 | Transitions Between Waypoints | TOC lead |
| §11.2 · Dubins Paths | 194 | Dubins Paths | **Examined passage** |
| §12.1 · Point-to-Point Algorithms | 207 | Point-to-Point Algorithms | TOC lead |
| §12.2 · Coverage Algorithms | 220 | Coverage Algorithms | TOC lead |
| §13.1 · Gimbal and Camera Frames and Projective Geometry | 226 | Gimbal and Camera Frames and Projective Geometry | TOC lead |
| §13.3 · Geolocation | 231 | Geolocation | TOC lead |
| §13.5 · Time to Collision | 238 | Time to Collision | **Examined passage** |
| §13.6 · Precision Landing | 240 | Precision Landing | TOC lead |

## Inspected mechanisms worth remembering

| Mechanism and source | Consequential insight | Failure of the naive model |
| --- | --- | --- |
| [Recursive belief prediction and correction — Probabilistic Robotics §2.4.1, p. 26](https://drive.google.com/file/d/1NqxGKSV7M4pMbBN_BdcKSYKbGzGHkuxm/view) | Estimate is a distribution updated by transitions and measurement likelihoods, not a sensor reading with a smoothing knob. | Unmodeled environment dynamics and incorrect likelihoods violate assumed conditional independence. |
| [Particles and resampling — Probabilistic Robotics §4.3, p. 96](https://drive.google.com/file/d/1NqxGKSV7M4pMbBN_BdcKSYKbGzGHkuxm/view) | Samples can represent multiple hypotheses and nonlinear transformations; weighted resampling changes the represented posterior. | Insufficient proposals and particle depletion collapse real alternatives. |
| [Likelihood fields — Probabilistic Robotics §6.4, p. 169](https://drive.google.com/file/d/1NqxGKSV7M4pMbBN_BdcKSYKbGzGHkuxm/view) | A smooth endpoint-distance likelihood offers computationally convenient range matching; the text explicitly notes its less physically grounded, ad-hoc nature. | A high matching score is not automatically a calibrated probability of a sensor's real generative process. |
| [Graph constraints — Probabilistic Robotics §11.2, p. 340](https://drive.google.com/file/d/1NqxGKSV7M4pMbBN_BdcKSYKbGzGHkuxm/view) | Control and observations create local information contributions/edges between states and map features. | False correspondences can introduce misleading global constraints. |
| [Conditional independence in FastSLAM — Probabilistic Robotics §13.2, p. 439](https://drive.google.com/file/d/1NqxGKSV7M4pMbBN_BdcKSYKbGzGHkuxm/view) | Robot path variables separate individual landmark posteriors in the graphical model; particles over paths and conditional estimators over landmarks factor the problem. | Incorrect paths, correspondences, or poor particle diversity invalidate useful approximations. |
| [Expected information gain — Probabilistic Robotics §17.2.1, p. 571](https://drive.google.com/file/d/1NqxGKSV7M4pMbBN_BdcKSYKbGzGHkuxm/view) | The next action can be chosen for its expected effect on belief entropy, not only distance to the goal. | Entropy-only navigation ignores travel cost and danger. |
| [Product of exponentials — Modern Robotics §4.1](https://drive.google.com/file/d/1wKeNmtPvxRGkb_MabBjqb4-Iq-s2eBIf/view) | A base frame, end-effector home pose and joint screw axes can express chain kinematics without requiring a frame on every individual link. | Its clean formula does not itself address motor torque, calibration, collisions or flexibility. |
| [Jacobian velocity relation — Modern Robotics §5.1](https://drive.google.com/file/d/1wKeNmtPvxRGkb_MabBjqb4-Iq-s2eBIf/view) | Joint velocities map into spatial tip velocities; Jacobian rank exposes missing instantaneous motion directions. | Solving endpoint pose alone can hide near-singular, impractically large joint rates. |
| [Recursive inverse dynamics — Modern Robotics §8.3.2, p. 294](https://drive.google.com/file/d/1wKeNmtPvxRGkb_MabBjqb4-Iq-s2eBIf/view) | Spatial motion and wrench propagation compute joint forces from desired accelerations. | Kinematically legal commands may exceed motor torque/gearing limits. |
| [Sampling planners — Modern Robotics §10.5, p. 378](https://drive.google.com/file/d/1wKeNmtPvxRGkb_MabBjqb4-Iq-s2eBIf/view) | Random/deterministic samples in state or C-space plus collision checks and local steering make high-dimensional path search practical. | Geometric feasibility is not a guarantee of differential or dynamic feasibility. |
| [Impedance and compliance — Modern Robotics §11.7, p. 441](https://drive.google.com/file/d/1wKeNmtPvxRGkb_MabBjqb4-Iq-s2eBIf/view) | A mass–spring–damper-like endpoint response is a control objective; high impedance approximates stiff motion, low impedance yields under force. | Position and force cannot both be independently imposed in one constrained direction. |
| [Frictional contact — Modern Robotics §12.2.1, p. 484](https://drive.google.com/file/d/1wKeNmtPvxRGkb_MabBjqb4-Iq-s2eBIf/view) | Available tangential contact force is limited by normal load and friction model; grasp force claims require contact geometry. | Mere geometric reach is not stable manipulation. |
| [Aerodynamic dynamic pressure — Small Unmanned Aircraft §4.2, p. 40](https://drive.google.com/file/d/10hEU6VDGJLBcdHa6kqrgkgwhkZkdJpyv/view) | Fixed-wing lift/drag/moment models depend on air relative velocity, density and shape; dynamic pressure scales with squared airspeed. | GPS ground speed is not lift-producing airspeed, especially in wind. |
| [Flight trim — Small Unmanned Aircraft §5.3, p. 65](https://drive.google.com/file/d/10hEU6VDGJLBcdHa6kqrgkgwhkZkdJpyv/view) | Steady flight, climbing and turning may be relative equilibria; linear models are conditioned on operating point. | One nominal linear model is not a full-flight-envelope certificate. |
| [Actuator saturation and cascaded loops — Small Unmanned Aircraft §6.2, p. 97](https://drive.google.com/file/d/10hEU6VDGJLBcdHa6kqrgkgwhkZkdJpyv/view) | Inner-loop bandwidth and finite control-surface travel bound what slower outer loops can command. | Tuning the outer loop cannot overcome an inner plant that is saturated or slow. |
| [Dubins transition — Small Unmanned Aircraft §11.2, p. 194](https://drive.google.com/file/d/10hEU6VDGJLBcdHa6kqrgkgwhkZkdJpyv/view) | Heading-constrained paths with bounded turning can be synthesized from curves and straight segments; the presentation assumes constant-altitude/groundspeed planning. | A waypoint polyline alone can demand impossible instantaneous changes of direction. |
| [Time-to-collision scale ambiguity — Small Unmanned Aircraft §13.5, p. 238](https://drive.google.com/file/d/10hEU6VDGJLBcdHa6kqrgkgwhkZkdJpyv/view) | The text explicitly notes that monocular imagery alone cannot generally supply metric TTC without additional information/assumptions. | Visual expansion does not magically reveal absolute distance or speed. |

## Ambition → operator composition → physical discriminator

| Ambition / composable capability | Source-grounded operator chain | Critical distinction to test |
| --- | --- | --- |
| **Turn raw observations into a position estimate resilient to ambiguous environments** | MR Ch 3 frame semantics → PR Ch 5 motion model / Ch 6 sensor likelihood → PR Ch 2 Bayes recursion → PR Ch 3 EKF or Ch 4 particle representation → PR Chs 7–8 localization/recovery | Teleport in a symmetric environment and measure recovery, false confidence and compute |
| **Navigate an unknown building without accumulating a hopeless map** | PR Ch 9 inverse range mapping → PR Chs 10–13 SLAM and loop closure → MR Ch 10 geometry/collision paths → MR Ch 11 controller → PR Ch 17 exploration | Inject one false loop closure, one dynamic obstacle and one unknown corridor |
| **Reach, grasp and move an object without destroying the part or saturating joints** | MR Chs 2–5 configuration/twists/Jacobian → Ch 6 inverse kinematics → Ch 8 dynamics → Ch 9 timing → Ch 11 force/impedance → Ch 12 grasp | Compare free-space versus wall-contact manipulation under one trajectory/controller |
| **Build a model-based fixed-wing autonomous mission from physics to navigation** | UAV Chs 2–5 frame/airspeed/forces/trim → Ch 6 cascaded autopilot → Chs 7–8 sensors/estimator → Chs 9–11 guidance/path manager → Chs 12–13 planning/vision | Fly a simulated route with crosswind, sensor dropout, actuator saturation and the same logged mission contract |
| **Decide whether to act or gather information** | PR Ch 2 belief update → Ch 14 MDP contrast → Ch 15 POMDP → Ch 16 approximation → Ch 17 information gain | Two indistinguishable corridors: compare rush-to-goal policy with one sensing detour |
| **Separate 'where is it' from 'how may it move' from 'what changes motion'** | MR Chs 2–3 configuration and transforms → MR Chs 4–8 kinematics/dynamics → UAV Chs 3–5 aircraft physical constraints → PR Ch 5 stochastic motion models | Pass the same waypoint plan to a differential rover and fixed-wing aircraft; document incompatible contracts |
| **Turn a camera detection into world-referenced action** | MR Ch 3 frame composition → UAV Ch 13 camera/gimbal model / geometric projection → PR Ch 6 observation modeling → UAV Chs 9–10 path following | Move camera and target separately, compare geolocation and time-to-collision inferred from projection |
| **Turn a perfect-model success into a meaningful systems demonstration** | UAV Ch 1 end-to-end design project → MR Ch 8 motor/friction and Ch 11 control → PR Ch 6 sensor errors / Ch 8 recovery → UAV Ch 6 actuator limits | Run the same mission under ideal, noisy and failing components; compare outcome and traces |
| **Understand why FastSLAM and multilevel autopilots are both forms of useful decomposition** | PR Ch 13 conditional independence over features given path → MR Ch 4 products of screw motions for joint chain → UAV Ch 6 fast-inner/slow-outer control hierarchy | Remove one factor's assumption (known path, rigid link, or inner-loop bandwidth) and compare collapse behavior |

## Scope and transfer boundaries

These three sources collectively cover **much** classical robotics, but they do not constitute all of robotics. The following comparisons prevent accidental inheritance of fixed-wing or planar-robot assumptions:

| Embodiment | Distinctive physics | Source/transfer boundary |
| --- | --- | --- |
| Planar differential-drive rover | Nonholonomic planar rolling; no lateral velocity | Probabilistic localization and map-based navigation transfer; aircraft aerodynamics does not |
| Holonomic/omniwheel rover | Planar motion approximates direct sideways translation | Same state/estimation family; reachability and drive constraints differ |
| Serial robot arm | Jointed articulated body with contacts and workspace | POE/Jacobians, torques and contact mechanics core; wheel odometry/aircraft trim irrelevant |
| Fixed-wing small aircraft | Airspeed-dependent lift, wind, minimum turn radius and no in-place hover | Frame, belief and planning abstractions transfer; hover-capable controller assumptions do not |
| Multirotor aircraft | Rotor thrust allocation and hover dynamics | Frames/estimation generalize; fixed-wing trim, coordinated turns and control surface loops do not transfer literally |
| Legged humanoid/quadruped | Contact schedule, balance, impacts and many-DOF dynamics | Contact/inverse dynamics useful; centroidal balance/gait/contact switching need additional sources |
| Underwater or space robotics | Fluid or orbital/environment-specific dynamics, sparse sensing and constraints | Do not assume aircraft aerodynamic or terrestrial range models apply |

## Three integrated competence probes (not arbitrary exercises)

**A. Navigation with uncertainty:** build one differential rover simulation with measured odometry, a range sensor likelihood, a configurable EKF/particle estimator, a small occupancy map, collision checking and feedback. Run ambiguous corridors, kidnapped relocalization, bad correspondence and delayed measurements. Observe actual recovery and false-map rate against a simpler deterministic baseline. This connects Modern Robotics Chs. 2, 10, 13 and Probabilistic Robotics Chs. 2, 4, 8, 9, 11.

**B. Manipulation with contact:** for a 2–3-link arm, implement frame-correct forward/IK and Jacobian, forward/inverse dynamics, one collision-aware trajectory and an impedance/contact mode. Compare unloaded, payload, near-singular and wall-contact cases. The useful evidence is achievable end-effector motion, measured (simulated) joint torque and contact forces, and failure boundaries, not a single successful reach. This connects Modern Robotics Chs. 3–6, 8–12.

**C. Fixed-wing closed-loop mission:** implement a six-DOF aircraft physics model, aerodynamic/propulsion disturbance models, trim/local controller, inner/outer autopilot, sensor simulation, state estimator and line/orbit/Dubins guidance. Compare perfect-state, noisy-sensor, crosswind and actuator-saturated mission runs. Record stall/airspeed margin and cross-track error; do not treat simulation as permission to fly. This closely follows Small Unmanned Aircraft's cumulative chapter design project.

## Navigation audit: frustration → useful passage

FKEN-16A requires a **two-sided** test: begin with authentic unfamiliar-user frustrations and separately sample important sections, invent plausible everyday tasks without disclosing their terminology, then inspect whether the Atlas provides meaningful intermediate choices and a recoverable relevant passage. A syntactically linked node is *not* evidence that a human could discover or use it.

| Starting frustration | Expected decisive bridge | Passage to retrieve |
| --- | --- | --- |
| A depth-sensing rover confuses two lookalike rooms | Multimodality versus Gaussian approximation | [Probabilistic Robotics, §4.3, printed p. 96](https://drive.google.com/file/d/1NqxGKSV7M4pMbBN_BdcKSYKbGzGHkuxm/view) |
| A rover recognizes its start but its map jumps elsewhere | Whether a false correspondence created an erroneous graph constraint | [Probabilistic Robotics, §11.5, printed p. 362](https://drive.google.com/file/d/1NqxGKSV7M4pMbBN_BdcKSYKbGzGHkuxm/view) |
| A 6-axis arm unexpectedly speeds up near a target | Jacobian rank and required joint rates | [Modern Robotics: Mechanics, Planning, and Control, §5.1, printed p. 178](https://drive.google.com/file/d/1wKeNmtPvxRGkb_MabBjqb4-Iq-s2eBIf/view) |
| A fixed-wing aircraft stalls despite substantial GPS speed | Ground speed and airspeed under wind | [Small Unmanned Aircraft: Theory and Practice, §4.2, printed p. 40](https://drive.google.com/file/d/10hEU6VDGJLBcdHa6kqrgkgwhkZkdJpyv/view) |
| A waypoint path contains an impossible sharp turn | Minimum-turn-radius heading-constrained transition | [Small Unmanned Aircraft: Theory and Practice, §11.2, printed p. 194](https://drive.google.com/file/d/10hEU6VDGJLBcdHa6kqrgkgwhkZkdJpyv/view) |
| An arm pushes too hard against a rigid surface | Impedance versus stiff position control | [Modern Robotics: Mechanics, Planning, and Control, §11.7, printed p. 441](https://drive.google.com/file/d/1wKeNmtPvxRGkb_MabBjqb4-Iq-s2eBIf/view) |
| A monocular camera sees an object but cannot provide metric range | Scale observability and assumed extra geometry | [Small Unmanned Aircraft: Theory and Practice, §13.5, printed p. 238](https://drive.google.com/file/d/10hEU6VDGJLBcdHa6kqrgkgwhkZkdJpyv/view) |
| Simulation-perfect autopilot fails with finite aileron travel | Saturation and inner-loop bandwidth | [Small Unmanned Aircraft: Theory and Practice, §6.2, printed p. 97](https://drive.google.com/file/d/10hEU6VDGJLBcdHa6kqrgkgwhkZkdJpyv/view) |

**Current certification:** source identity, chapter mapping, question/bridge references and source-text excerpts have been checked; actual Kami direct-page navigation, unfamiliar-user task success, time-to-relevant-passage and physical robotics performance are **not** yet certified. Compare Atlas vs PDF TOC vs ordinary full-text retrieval rather than rewarding node count.

## Continuation rule

1. Retrieve `investigation.json` and `glossary.json` before editing. Preserve permanent node and term IDs; use aliases and redirects for true synonyms, and explicit conceptual links for different mechanisms.
2. A question, broader set, technical node and book passage can all share one canonical mechanism; **do not** create duplicate trees or duplicate explanations for every view.
3. Advance an uncertain claim by reading a consequential actual passage or constructing a discriminating systems test; mark TOC-only leads, inspected passages, and reproduced demonstrations separately.
4. The glossary can grow without any mapped question or source. Mark adjacent-ecosystem terms honestly and connect them only when a real retrieval or diagnostic reason exists.
5. Rerun two-sided navigation tests when a change alters a meaningful route, and subtract dead-end or misleading paths rather than manufacturing more boilerplate.
