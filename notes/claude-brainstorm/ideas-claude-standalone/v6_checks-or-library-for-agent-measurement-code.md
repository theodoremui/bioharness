# Checks or a Library? Keeping Agent-Written Measurement Code Honest Under Per-Feature Rewards

## Abstract

Agents that write their own analysis code can compute quantities no fixed pipeline anticipated, but the same freedom lets them write code that returns plausible values without measuring anything. Two remedies are available. One is to check the code: re-run it, and require it to reproduce known values on other recordings. The other is to remove the freedom: let the agent call only a validated library of feature code and choose its inputs. This proposal compares the two for a tool-calling vision-language agent that measures balance from one smartphone video and is trained with rewards on each feature against a three-camera reference. It asks whether known-answer checks make measurements of unseen people more accurate than training without them, whether a library-constrained agent reaches the same accuracy without checks, and how often each approach accepts deliberately wrong programs or rejects correct ones. The answer says where verification is worth its cost: everywhere, or only where no validated code exists.

## 1. Motivation

### 1.1 The measurement task and the agent

In the StaBLE "rise to toes" task ([Heigold et al., 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13621976/)), a person rises onto their toes as quickly and as high as they can and holds for five seconds. Three **features** describe the performance: the peak upward speed of the **center of mass** (the average position of the body's mass), the peak ankle angle, and the time the center of mass stays high. Each is rescaled to 0–1 and the rescaled values are averaged into a **task score**. StaBLE has 18 tasks and 76 features, recorded from 180 adults with three smartphones; the three-camera reconstruction serves as the reference.

The agent is a tool-calling **vision-language model** (VLM). Given one camera's video, it requests frames, runs pose, segmentation and 3D-reconstruction tools, and writes a short function per feature that computes it from tool outputs and from start and end times it marks on the video. It is trained with **reinforcement learning (RL)**, which samples its own attempts, scores each with a reward, and shifts the model toward higher-scoring ones. The reward here is the error of each submitted feature against the three-camera reference, which exists only during training.

### 1.2 How free-form code can satisfy a per-feature reward without measuring

A per-feature reward penalizes wrong numbers, but RL searches for any program that produces right-looking numbers on training videos, and several such programs do not measure the intended quantity:

- returning a typical value, or a typical value plus a tiny multiple of some input;
- computing a hold time from the agent's own start and end marks instead of from the center-of-mass signal the definition names;
- recognizing a training video and returning a remembered answer;
- computing the right quantity on the wrong body part, or in the wrong units, in a way that happens to correlate with the answer;
- relying on cues such as clip length or the person's height in pixels.

RL-trained tool agents have been observed to skip verification steps ([Thaman, 2026](https://arxiv.org/abs/2605.02964)), and optimizing a proxy reward can move a policy away from the intended behavior ([Gao et al., 2023](https://arxiv.org/abs/2210.10760)). On new participants these programs fail in ways a single training video does not reveal.

### 1.3 Two remedies with different costs

**Checking** keeps the agent's freedom and tests its output. Its costs are recordings with known answers for every feature, tolerances that must be tuned, and the risk of rejecting correct code that disagrees with the probes for legitimate reasons. **Constraining** removes the freedom: the agent calls validated feature code and chooses only the tool route, the time window and any filtering. This is possible only where someone has already written and validated the code — as StaBLE's released analysis code does for its own tasks. For a new task, no library exists.

### 1.4 A worked example

For peak center-of-mass speed, a free-form agent might submit `peak_speed(out, ann)`, which differentiates the vertical center-of-mass position over time and takes the maximum between the marked start and end. The check re-runs it, then runs it on four development recordings with known answers: two slow risers and two fast risers. A correct function lands near their values and ranks them correctly. A function that returns 0.18 gives 0.18 for all four and fails. A library-constrained agent instead submits `feature("peak_com_speed", source="reconstruct3d:A", window=(3.9, 10.6))`, which cannot return a constant, though it can still choose a poor route or window.

## 2. Research question and hypotheses

> **Research question.** When a tool-calling agent writes its own measurement code under per-feature rewards, does checking that code against known answers on other recordings make its measurements of unseen people more accurate? Does restricting the agent to a validated library of feature code achieve the same accuracy without checks?

| ID | Hypothesis | Refuted if |
|---|---|---|
| H0 (gate, before RL) | The check rejects deliberate shortcut programs and accepts expert code | Any shortcut passes more than 5% of the time, or expert functions fail more than 10% |
| H1 (primary) | Checked training gives lower feature error on sealed participants than unchecked training | The 95% interval for the expected difference over retraining includes zero |
| H2 | Checked training lowers the shortcut rate on independent audit recordings | No difference |
| H3 (equivalence) | A library-constrained agent matches the checked agent | Its feature error differs from the checked agent's by more than 0.01 score units in either direction |
| H4 | Passing the check reflects broader correctness | Higher pass rates come without lower error on audit recordings, which would indicate adaptation to the validator |

**What the study would establish.** RL with verifiable rewards is spreading to agents that write scientific code, and execution-based checks are the usual safeguard. This study measures what such checks buy compared with the simpler alternative of constraining the action space, and it estimates their false acceptance and false rejection directly. If H3 holds, the practical rule is to constrain wherever validated code exists and to reserve checking for new analyses. If the checked agent beats the library, the freedom to write code is worth having even when a library exists, for instance because it lets the agent adapt computations to the failures of single-camera tools.

## 3. Related work

**Code generation with execution rewards.** [CodeRL](https://arxiv.org/abs/2207.01780) and later work reward generated programs by running them against unit tests. Reinforcement learning with verifiable rewards ([Lambert et al., 2024](https://arxiv.org/abs/2411.15124)) generalizes this to any automatically checkable outcome. The known-answer check is a test suite whose cases are recordings with reference values, close in spirit to programming by example ([Gulwani, 2011](https://doi.org/10.1145/1926385.1926423)).

**Constrained action spaces.** Visual-programming systems ([VisProg](https://arxiv.org/abs/2211.11559), [ViperGPT](https://arxiv.org/abs/2303.08128)) restrict generated programs to a fixed library of vision modules, trading flexibility for reliability. A domain-specific library of validated feature code is the analogous choice here.

**Reward granularity and process supervision.** [ToolRL](https://arxiv.org/abs/2504.13958) studies rewards on tool names and arguments, and process supervision rewards intermediate reasoning steps ([Lightman et al., 2023](https://arxiv.org/abs/2305.20050)). Both arms here already receive per-feature rewards; the question is what keeps the code behind each feature honest.

**Biomechanics agents.** [BiomechAgent](https://arxiv.org/abs/2602.06975) found that a validated gait-event tool improved a code-writing agent, which is evidence for the value of validated components.

## 4. Method

### 4.1 Tools and harness

Tools: timestamped frames and crops, 2D landmarks (RTMPose or a second pose model), person segmentation (SAM 2.1), point tracks (CoTracker3) for 16 body regions, 3D joint angles and center of mass ([OpenCap Monocular](https://arxiv.org/abs/2603.24733), two settings), plotting and a Python sandbox. Expensive outputs are computed once and cached, requests outside the menu return an error, and every signal is indexed by time in seconds.

### 4.2 Three arms

All arms share the per-feature reward, the warm start and the training budget. With features rescaled by training endpoints, `e_f` is the error of the submitted value against the reference in score units, computed from the submitted value in every arm.

| Arm | Feature code | Checks | Penalty `P` (reward `−min(P, 3)`) |
|---|---|---|---|
| A. Unchecked | Free-form, restricted program form | Replay (including the noisy copy) and range | `(1/k) Σ_f [e_f + 0.5 · 1(f fails a basic check)]` |
| B. Checked | Free-form, restricted program form | A's checks plus known answers | `(1/k) Σ_f [e_f + 0.5 · 1(f fails any check)]` |
| C. Library | Calls to validated feature code only | Replay is automatic | `(1/k) Σ_f e_f` |

The **restricted program form**, shared by arms A and B, allows array operations from a fixed library, with no branching on array identity, hashes or shapes, and no numeric literals beyond physical constants and small integers. Holding it fixed means the A-versus-B contrast changes only the known-answer check.

The **validated library** for arm C is the expert pipeline's feature code: StaBLE's released feature functions for 3D signals, and expert-written equivalents for 2D signals, which are themselves validated against the reference on development folds. The agent chooses the feature function's input source, time window and filter settings from menus.

Unparseable submissions receive −4 in every arm, below every valid attempt.

### 4.3 The known-answer check

For each feature, four development recordings of the same task serve as probes: two with reference values near the feature's 25th percentile and two near its 75th, chosen among recordings where the expert pipeline's start and end marks agree with the three-camera segmentation within 0.2 s. The submitted function is run on each probe's cached outputs with the expert marks, which isolates the computation from event finding. It passes if its mean probe error is at most the larger of 0.15 score units and 1.5 times the expert pipeline's error on the same probes, and if both low probes fall below both high probes. Probes whose values are too close to distinguish a correct function from a constant are replaced, and features for which no such pair exists are reported as unverifiable.

### 4.4 Validating the check before training

On development folds, a suite of deliberately wrong programs is run through the full check: the training mean; the mean plus a tiny multiple of an input; the mean plus noise; a function of the agent's marks only; a function that recognizes the current video and returns a remembered value; the right computation on the wrong body part; the wrong units; a hard-coded window; a function of clip duration; and a function of the person's pixel height. Each must fail at least 95% of the time, and the expert pipeline's functions must pass at least 90% of the time (H0). If either threshold is missed, tolerances are revised on development folds and the suite is rerun before any RL begins.

### 4.5 Training

Each arm starts from Qwen3-VL-8B fine-tuned with low-rank adapters on demonstrations from a larger frozen model (Qwen3-VL-235B-A22B) running that arm's harness, kept when features replay and the mean feature error is below a preset threshold, with equal counts per task (at most 40). RL uses group relative policy optimization ([GRPO](https://arxiv.org/abs/2402.03300)): eight trajectories per video, advantages normalized within groups, and groups with identical rewards skipped ([DAPO](https://arxiv.org/abs/2503.14476)). Rollouts, data order and sampler are identical across arms.

### 4.6 Audit recordings

A separate set of development recordings, never used as probes, serves as the audit. Each submitted function from the sealed evaluation is also run on audit recordings of its task with expert marks. The **shortcut rate** is the share of functions that are constant-like there (their outputs barely change across recordings with widely different references) or whose audit error exceeds the expert pipeline's by more than the check's tolerance. Audit results never enter training or selection.

## 5. Data, splits and leakage

**Dataset and ledger.** StaBLE contains 180 adults aged 18 to 87, from people with vestibular disorders to competitive athletes and dancers; 171 have usable single-camera video. A ledger lists every recorded trial (3,322) with its Cam0 video, reference features, participant, task and status. Thirty trials flagged for reconstruction error and three with imputed features are excluded from rewards, probes, audits and the primary evaluation. Ninety-eight tasks not attempted for safety have no video.

**Splits.** Sixty participants are set aside before any analysis, stratified by StaBLE score quintile, age group and athlete status, and drawn from people who were never in the lab pilot's test set. This is a retrospective re-split, documented as such, with every baseline retrained without them. The other 111 participants form five stratified development folds, checked against the whole (Kolmogorov–Smirnov tests and standardized mean differences below 0.1). Probes and audit recordings are drawn from disjoint development participants.

**Leakage.** Rescaling endpoints, which StaBLE computes over all 180 participants, are refitted on training folds. Probes, tolerances, the shortcut suite's thresholds and the library's validation use development data only. No sealed participant's reference enters a check, so the check runs identically on sealed videos. Seven participants appear in StaBLE's public exemplar video; results are reported with and without them.

**Keeping the data's shape.** The RL sampler draws ledger rows with equal probability; the share of updates per task and per ability quintile is logged, and any task drifting by more than a quarter from its ledger share is reweighted.

## 6. Evaluation

**Primary outcome.** Feature error in score units on sealed participants, computed from features as submitted in every arm (no substitution for features that fail a check), averaged over features within a task and then over tasks with equal weight.

**Secondary outcomes.** Shortcut rate on audit recordings; checked coverage (the share of trials whose features all pass), reported for every arm; false acceptance and false rejection of the check, from the shortcut suite and expert code; the relation between pass rate and audit error (H4); error in the agent's marks against the three-camera segmentation; task-score error and within-task rank agreement.

**Failure rule.** A trial without usable output receives the training-fold task mean and is counted as a fallback; comparisons are repeated on trials completed by both arms.

## 7. Statistics

Participants are the unit of analysis, and every interval resamples participants with all their trials. Each arm is trained with seven paired seeds. Method claims target the expected improvement over retraining, with an interval that combines the spread between paired seed differences and the participant-bootstrap spread of the seed-averaged difference (t-distribution, Satterthwaite degrees of freedom), and whose coverage is checked by simulation before training. H1 succeeds if the upper 95% bound for the checked-minus-unchecked difference is below zero. H3 is tested as equivalence with two one-sided tests at a margin of 0.01 score units. H2 to H4 form one Holm-corrected family.

## 8. Scope and cost

| Item | H100-hours (estimate) |
|---|---|
| Tool cache, computed once | 400 |
| Demonstrations for three harnesses and warm-start fine-tuning | 450 |
| Check validation and RL development runs | 300 |
| RL, three arms × seven seeds (about 150 each) | 3,150 |
| Audit and evaluation | 50 |
| **Total** | **about 4,350** |

A reduced version runs all RL on six tasks spanning the main task families (standing, sit-to-stand, single-leg, Y-Balance, jump, gait) for about 2,450 H100-hours.

## 9. What each outcome would mean

If checked training beats unchecked training (H1) and the library matches it (H3), checks are needed only where no validated code exists, which points them toward new tasks and new analyses. If the checked agent beats the library, free-form code adds accuracy even when validated code exists, which suggests that the agent adapts computations to tool failures in useful ways; the per-feature errors show where. If checks raise pass rates without lowering audit error (H4), training adapted to the validator, and the check's coverage should not be read as evidence of measurement. If the check stalls learning by rejecting too much, its tolerances or its probes are at fault, and the gate in H0 is designed to catch this before RL starts.

Passing the check is tested behavior on known recordings, which is weaker than a proof of correctness. It certifies the computation given the agent's marks, so the timing of those marks is evaluated separately. As in any study anchored to the three-camera reconstruction, errors shared between the reference and the monocular tool remain invisible.
