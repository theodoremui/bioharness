# Writing Measurement Programs for Tasks Never Trained On: Transfer of Checked Biomechanical Measurement Across Balance Tasks

## Abstract

A useful measurement agent should handle a new assessment from its written definition. A clinic may add a balance task whose features are described in a protocol but for which no analysis code or training data exist. This proposal asks whether a tool-calling vision-language agent, trained with reinforcement learning to measure the features of some balance tasks from one smartphone video, writes accurate measurement programs for held-out tasks given only their feature definitions. It also asks whether training with a known-answer check, which credits a feature only if the agent's code reproduces reference values on other recordings, produces more reusable programs than the same training without the check. Three tasks from different families are excluded from all training. The study separates transfer of learned skill from competence the model already had, tests whether a handful of labeled examples of the new task help at test time, and distinguishes held-out features that reuse familiar physical quantities from those that introduce new ones.

## 1. Motivation

### 1.1 The measurement task and the agent

In the StaBLE "rise to toes" task ([Heigold et al., 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13621976/)), a person rises onto their toes as quickly and as high as they can and holds for five seconds. Three **features** describe the performance: the peak upward speed of the **center of mass** (the average position of the body's mass), the peak ankle angle, and the time the center of mass stays high. StaBLE defines 76 such features across 18 tasks, from quiet standing and tandem stance to reaching, jumping and walking, recorded from 180 adults with three smartphones; the three-camera reconstruction serves as the reference.

The agent is a tool-calling **vision-language model** (VLM). Given one camera's video and a task's feature definitions, it requests frames, runs pose, segmentation and 3D-reconstruction tools, writes a short function for each feature that computes it from tool outputs and from start and end times it marks on the video, and submits the values. The task's fixed formula turns them into a score.

### 1.2 Why transfer is where agent-written code matters

For tasks the lab already analyzes, StaBLE's released analysis code computes every feature from reconstructed kinematics, and an agent could simply call it. For a new task no such code exists. Measuring it means translating a written definition ("the forward displacement of the most distal finger point during the reach, relative to its starting position") into a program over noisy single-camera tool outputs, together with finding the right moments in the video. This is program synthesis from a specification combined with perception — the capability a general measurement agent most needs.

### 1.3 Why a known-answer check might help

During training, the agent's feature functions are rewarded against reference values. A function rewarded only on the video at hand can fit that video, for example through a hard-coded window or a quantity that happens to correlate with the answer. A function that must also reproduce known values on other recordings of the same task is pushed toward the general computation. The hypothesis is that this pressure produces measurement habits (differentiate the right signal, threshold relative to baseline, respect units) that carry over to tasks never seen. The alternative is that the agent adapts to the specific probe recordings, improving its check performance without learning anything that transfers.

## 2. Research question and hypotheses

> **Research question.** Given only the written feature definitions of a balance task it has never been trained on, can a tool-calling agent produce accurate measurement programs for that task? Does reinforcement learning with known-answer checks on other tasks improve this ability more than the same training without checks?

| ID | Hypothesis | Refuted if |
|---|---|---|
| H1 | Checked training lowers feature error on held-out tasks relative to the starting model | The interval for the difference includes zero |
| H2 (primary) | Checked training lowers held-out feature error relative to unchecked training | The 95% interval for the expected difference over retraining includes zero |
| H3 | The benefit is larger for held-out features whose physical quantity type occurs in training | The difference between feature groups has an interval including zero |
| H4 (secondary) | Selecting among sampled programs with five labeled recordings of the new task lowers error further | No gain over the unselected checked agent |
| H5 (secondary) | The measurement agent transfers better than a direct score predictor prompted with the new task | Held-out task-score error does not differ |

**What the study would establish.** Reinforcement learning with verifiable rewards is usually evaluated on the distribution it was trained on. This study asks whether verification during training produces programs that generalize to new specifications, in a domain where every intermediate quantity has a physical reference. A positive H2 would support training-time verification as a source of reusable skill; a positive H1 with a null H2 would mean that RL on measurement transfers but checks add nothing to it.

## 3. Related work

**Program synthesis and reuse.** Programming by example infers programs from input–output pairs ([Gulwani, 2011](https://doi.org/10.1145/1926385.1926423)), and [DreamCoder](https://arxiv.org/abs/2006.08381) learns libraries of reusable abstractions that speed up synthesis on new tasks. The known-answer check resembles learning from examples, applied to physical measurement from noisy perception.

**Code generation with test rewards.** [CodeRL](https://arxiv.org/abs/2207.01780) and later work reward generated programs by running them against unit tests and report gains on unseen problems from the same benchmarks. Here the "tests" are recordings with reference values, and generalization is measured across task definitions.

**Generalization of tool-use RL.** [ToolRL](https://arxiv.org/abs/2504.13958) and [DeepEyes](https://arxiv.org/abs/2505.14362) train tool use with RL on question answering. A re-evaluation of harness evolution found that gains often fail to transfer to held-out tasks ([Wang et al., 2026](https://arxiv.org/abs/2607.12227)), which makes held-out-task evaluation a necessary test for any claim of learned skill.

**Biomechanics agents.** [BiomechAgent](https://arxiv.org/abs/2602.06975) writes analysis code from natural-language requests over processed motion-capture data, without training the model or evaluating on raw video.

## 4. Method

### 4.1 Tools and harness

Tools: timestamped frames and crops, 2D landmarks (RTMPose or a second pose model), person segmentation (SAM 2.1), point tracks (CoTracker3) for 16 body regions, 3D joint angles and center of mass ([OpenCap Monocular](https://arxiv.org/abs/2603.24733), two settings), plotting and a Python sandbox. Expensive outputs are computed once and cached, requests outside the menu return an error, and every signal is indexed by time in seconds.

### 4.2 Held-out tasks

Semi-Tandem (standing), Gait-Backwards (gait) and Functional Reach (reaching) are fixed before any analysis, one from each of three task families. Their videos are excluded from every training stage, including demonstration generation, prompts and any learned component, and their feature definitions are shown to the agent for the first time at evaluation. Before any development work, each held-out feature is classified from its definition alone by physical quantity type (duration, peak speed, displacement, angle, sway or path length) and by whether a training-task feature of the same type exists. This classification defines the groups for H3.

### 4.3 The known-answer check

A submitted feature is **checked** when it passes four tests, none of which uses the reference of the video being analyzed:

- **Replay.** Re-running the function on the cited tool outputs gives the submitted value, and re-running it on a copy of those outputs with noise far below measurement precision gives nearly the same value. A function that recognizes the video and returns a memorized number fails the second part.
- **Known answers.** The function is run on four development recordings of the same task whose reference values are known (two near the feature's 25th percentile and two near its 75th), using the expert pipeline's start and end marks so that the check isolates the computation from event finding. It passes if its mean error on these probes is at most the larger of 0.15 score units and 1.5 times the expert pipeline's error on the same probes, and if both low probes fall below both high probes.
- **Range.** The value lies within the training range widened by half its width on each side.
- **Program form.** The function uses only array operations from a fixed library, with no branching on array identity, hashes or shapes, and no numeric literals beyond physical constants and small integers.

Before any RL, the check is validated on development folds against a suite of deliberately wrong programs (the training mean, the mean plus a tiny multiple of the input, a function of clip duration only, a function of the person's pixel height, the right computation on the wrong body part or in the wrong units, a hard-coded window, a memorized value), each of which must fail at least 95% of the time. The expert pipeline's own functions must pass at least 90% of the time.

### 4.4 Arms and rewards

All arms start from the same model: Qwen3-VL-8B fine-tuned with low-rank adapters on verified demonstrations of the 15 training tasks from a larger frozen model (Qwen3-VL-235B-A22B), at most 40 per task. With features rescaled by training endpoints and `e_f` the error of the submitted value against the reference in score units:

- **Starting model:** no RL (for H1).
- **Unchecked RL:** reward `−(1/k) Σ_f e_f`, with replay and range required (a failure counts as a format error).
- **Checked RL:** penalty `P = (1/k) Σ_f [e_f + 0.5 · 1(f not checked)]` and reward `−min(P, 3)`. Training error is always computed from the submitted value, so an unchecked answer can never earn more than the same answer checked.
- **Both RL arms:** unparseable submissions receive −4. Group relative policy optimization ([GRPO](https://arxiv.org/abs/2402.03300)) samples eight trajectories per video, normalizes advantages within each group, and skips groups with identical rewards ([DAPO](https://arxiv.org/abs/2503.14476)). Rollouts, data order and sampler are identical between arms.
- **Direct score predictor (H5):** Qwen3-VL-8B fine-tuned on task scores of the 15 training tasks, then given the held-out task description, its feature definitions and its rescaling endpoints.

### 4.5 Calibration and test-time selection on the new task

Scoring a held-out task still needs rescaling endpoints, fallback means and recordings for the audit, so the development participants' reference features for the three held-out tasks form a **task-calibration set**. It is used only for those purposes, identically for every method, and never for training or prompting. The transfer claim is therefore transfer with labeled calibration but without any training on the task. For H4 only, a secondary arm also uses five labeled calibration recordings per held-out task at test time: the checked agent samples eight trajectories per sealed video, and the one whose feature functions have the lowest error on those five recordings is submitted.

### 4.6 Auditing what the check accepts on new tasks

Audit recordings for each held-out task are drawn from the task-calibration set, separate from the probes. They measure two error rates of the check on the new task: false acceptance (deliberately wrong programs that pass) and false rejection (expert-written correct implementations that fail). Features whose probe values are too close to separate a correct function from a constant are flagged, because the check cannot provide evidence for them.

## 5. Data, splits and leakage

**Dataset and ledger.** StaBLE contains 180 adults aged 18 to 87, from people with vestibular disorders to competitive athletes and dancers; 171 have usable single-camera video. A ledger lists every recorded trial (3,322) with its Cam0 video, reference features, participant, task and status. Thirty trials flagged for reconstruction error and three with imputed features are excluded from rewards, probes and the primary evaluation. Ninety-eight tasks not attempted for safety have no video.

**Splits.** Sixty participants are set aside before any analysis, stratified by StaBLE score quintile, age group and athlete status, and drawn from people who were never in the lab pilot's test set. This is a retrospective re-split, documented as such, with every baseline retrained without them. The other 111 participants form five stratified development folds, checked against the whole (Kolmogorov–Smirnov tests and standardized mean differences below 0.1). The evaluation crosses the two kinds of novelty: sealed participants on training tasks, and sealed participants on held-out tasks.

**Leakage.** Held-out task videos never enter training. Rescaling endpoints, fallback means, probes and audit recordings come from development participants only, and from training folds for development decisions. Seven participants appear in StaBLE's public exemplar video; results are reported with and without them. StaBLE's feature definitions, including those of the held-out tasks, were designed on all 180 people and are treated as part of the measuring instrument.

**Keeping the data's shape.** The RL sampler draws training-task rows with equal probability; the share of updates per task and per ability quintile is logged, and any task drifting by more than a quarter from its ledger share is reweighted.

## 6. Evaluation

**Primary outcome.** Feature error in score units on the held-out tasks for sealed participants, computed from features as submitted, reported per task and pooled with equal task weights. Physical-unit errors are reported per feature.

**Secondary outcomes.** Feature error on training tasks for sealed participants, which separates participant generalization from task transfer; held-out task-score error and within-task rank agreement; timing error of the agent's marks; checked coverage on held-out tasks; the audit's false-acceptance and false-rejection rates; and the H3 and H4 contrasts.

**Failure rule.** A trial without usable output receives the task-calibration mean (for held-out tasks) or the training-fold mean (for training tasks) and is counted as a fallback. Comparisons are repeated on trials completed by both arms.

## 7. Statistics

Participants are the unit of analysis, and every interval resamples participants with all their trials. Each RL arm is trained with seven paired seeds. Method claims target the expected improvement over retraining, with an interval that combines the spread between paired seed differences and the participant-bootstrap spread of the seed-averaged difference (t-distribution, Satterthwaite degrees of freedom), and whose coverage is checked by simulation before training. H2 succeeds if the upper 95% bound for the checked-minus-unchecked held-out error difference is below zero. H1 and H3 to H5 form one Holm-corrected family.

With three held-out tasks, the pooled estimate describes these tasks and is not a sample from a population of possible tasks. Each task's result is therefore reported separately, and a claim of transfer requires the pooled effect together with no task showing a significant effect in the opposite direction. If the budget allows, a second rotation that holds out three other tasks, one per family, serves as a replication.

## 8. Scope and cost

| Item | H100-hours (estimate) |
|---|---|
| Tool cache, computed once | 400 |
| Demonstrations and warm-start fine-tuning | 300 |
| Check validation and RL development runs | 300 |
| RL, two arms × seven seeds (about 150 each) | 2,100 |
| Direct predictor, test-time selection and evaluation | 100 |
| **Total** | **about 3,200** |

A reduced version trains on six tasks spanning the main families and evaluates on the same three held-out tasks, for about 1,900 H100-hours; transfer distance is then larger, and the result should be read with that in mind.

## 9. What each outcome would mean

Lower held-out error for the checked agent (H2) would support known-answer checks as a source of reusable measurement skill. Better probe performance without better transfer would suggest adaptation to the check. A gain confined to training tasks would limit the conclusion to new participants. If the benefit appears only for familiar quantity types (H3), the agent transfers procedures it has practiced, not the ability to implement new definitions. If test-time selection helps (H4), a few labeled recordings are a cheap way to deploy the agent on a new task.

Each held-out task belongs to a family that remains in training, so this is near transfer, and the definitions and calibration labels supply domain knowledge that a fully unspecified task would lack. Agreement with the three-camera reference is the scope of the claim, and errors that the reference shares with the monocular tool would not be detected.
