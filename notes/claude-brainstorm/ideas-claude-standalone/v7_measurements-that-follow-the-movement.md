# Do Measurements Follow the Movement? Physical-Response Checks as Training Signals for Measurement Agents

## Abstract

A measurement is more than a number on one recording, because it implies how that number should change when the movement changes. Slowing a movement should lower its peak speed and lengthen its durations, while leaving joint angles unchanged. A model can reproduce reference values on familiar recordings while depending on cues that break these rules, such as clip length or apparent age. This proposal turns such rules into a training signal for a tool-calling vision-language agent that measures balance from one smartphone video. During training, each feature function the agent writes must respond to prescribed perturbations of the body signal in the way the feature's definition dictates. The expected responses are computed by running the task's released feature code on equally perturbed reference trajectories, so thresholds and caps are respected. Evaluation uses whole-video transformations held out from training, including speed changes within clips of unchanged length. The study asks whether these response checks make single-camera measurements follow changes in movement more faithfully than accuracy-based training alone, and at what cost to ordinary accuracy.

## 1. Motivation

### 1.1 The measurement task and the agent

In the StaBLE "rise to toes" task ([Heigold et al., 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13621976/)), a person rises onto their toes as quickly and as high as they can and holds for five seconds. Three **features** describe the performance: the peak upward speed of the **center of mass** (the average position of the body's mass), the peak ankle angle, and the time the center of mass stays high. Each is rescaled to 0–1 and averaged into a **task score**. StaBLE has 18 tasks and 76 features, recorded from 180 adults with three smartphones; the three-camera reconstruction serves as the reference.

The agent is a tool-calling **vision-language model** (VLM). Given one camera's video, it requests frames, runs pose, segmentation and 3D-reconstruction tools, and writes a short function per feature that computes it from tool outputs and from start and end times it marks on the video. It is trained with reinforcement learning against the three-camera reference, which exists only during training.

### 1.2 Why accuracy on recordings is not enough

Agreement with reference values on a set of recordings constrains what a measurement function returns on those recordings, but not why. A hold-time function that partly reads the clip's length can match references on typical recordings, because longer clips tend to contain longer holds. A peak-speed function can rank people correctly through features correlated with age. Both would fail on a recording where the movement changes and the correlated cue does not. Checking agreement on more recordings helps only to the extent that the recordings happen to break the correlation.

### 1.3 Metamorphic relations

Software testing faces the same problem when correct outputs are unknown, and **metamorphic testing** addresses it by checking relations between outputs under known transformations of the input: if an input is transformed in a known way, the output must change in a known way ([Chen et al., 1998](https://arxiv.org/abs/2002.12543); [Segura et al., 2016](https://doi.org/10.1109/TSE.2016.2532875)). The idea has been used to test machine-learning classifiers ([Xie et al., 2011](https://doi.org/10.1016/j.jss.2010.11.920)) and reinforcement-learning policies ([LEGIBLE, 2025](https://ijcai.org/proceedings/2025/696)). For biomechanical features the relations follow from the definitions. Steepening the center-of-mass rise must raise the peak speed. Shifting the moment the center of mass drops must change the hold time. Rescaling the height of the center-of-mass curve leaves threshold crossings in place, so it must leave the hold time unchanged.

### 1.4 From tests to training signals

This proposal uses such relations during training, as a condition for a feature to earn credit, and then tests whether the resulting agent follows held-out transformations of whole videos. Two details make this workable. First, expected responses are never derived by hand. They come from applying the same perturbation to the three-camera reference curves and rerunning StaBLE's released feature code, which handles definitions with thresholds and caps (hold time, for instance, is capped at five seconds). Second, the training perturbations act on body signals while the evaluation transformations act on whole videos — and are never used in training — so a gain cannot come from learning the test.

### 1.5 A design tension

A response check requires a feature to respond to the signal its definition names. A hold time computed from the agent's own start and end marks would fail it, even though the marks come from inspecting plots and may be accurate. The check therefore enforces fidelity to the definition, which may cost accuracy when the monocular signal itself is unreliable. The study measures this trade-off through ordinary feature error.

## 2. Research question and hypotheses

> **Research question.** Does requiring an agent's measurement code to respond to controlled changes in the measured body signal, as each feature's definition prescribes, make single-camera measurements follow held-out changes in movement more faithfully than training on per-feature accuracy and known answers alone, without lowering accuracy on unmodified videos?

| ID | Hypothesis | Refuted if |
|---|---|---|
| H1 (primary) | Response-checked training lowers the error of predicted feature changes under held-out video transformations | The 95% interval for the expected difference over retraining includes zero |
| H2 | Accuracy on unmodified videos is not lowered | The upper bound for the feature-error difference exceeds +0.01 score units |
| H3 | The gain extends to transformations unlike any training perturbation | The gain on within-clip speed changes at fixed total duration has an interval including zero |
| H4 | Response checks reduce shortcut use | The share of duration-only and mark-only functions on audit recordings does not differ |

**What the study would establish.** Rewards for agents that write code usually check outputs on examples. Relations that follow from a quantity's definition are a different kind of signal: they constrain how the output must change, which no finite set of examples pins down. The approach applies wherever a measured quantity has known responses to time, scale or unit changes, which covers much of scientific measurement. The held-out video transformations also give a reusable evaluation of whether any measurement method, agent or not, responds to movement as physics predicts.

## 3. Related work

**Metamorphic testing.** Chen et al. (1998) introduced checking relations among outputs when exact outputs are unknown; Segura et al. (2016) survey its development. Xie et al. (2011) applied it to machine-learning classifiers, and LEGIBLE (IJCAI 2025) uses metamorphic relations to test and improve RL policies. A single literature search found no prior use of metamorphic relations as a training reward for program-writing agents, which is weak evidence that the combination is new.

**Consistency and equivariance.** Consistency regularization trains models to give stable outputs under perturbations ([Sajjadi et al., 2016](https://arxiv.org/abs/1606.04586)), and equivariant architectures build known transformation behavior into a network. Here the transformation behavior is feature-specific, includes required changes as well as invariances, and is imposed on generated programs instead of network weights.

**Physics-informed training.** Physics-informed neural networks add known equations to the loss ([Raissi et al., 2019](https://doi.org/10.1016/j.jcp.2018.10.045)). Response checks use known relations from measurement definitions in a similar role, without requiring the governing equations of the movement.

**Code generation with execution rewards.** [CodeRL](https://arxiv.org/abs/2207.01780) and related work reward programs that pass unit tests. Response checks are tests on relations between runs instead of on individual outputs.

**Video models and temporal information.** Many video-language tasks can be solved from a single frame ([Buch et al., 2022](https://arxiv.org/abs/2206.01720)), so tests that hold appearance fixed while changing timing are a direct way to show that a method uses motion.

## 4. Method

### 4.1 Tools and harness

Tools: timestamped frames and crops, 2D landmarks (RTMPose or a second pose model), person segmentation (SAM 2.1), point tracks (CoTracker3) for 16 body regions, 3D joint angles and center of mass ([OpenCap Monocular](https://arxiv.org/abs/2603.24733), two settings), plotting and a Python sandbox. Expensive outputs are computed once and cached, requests outside the menu return an error, and every signal is indexed by time in seconds.

### 4.2 Training shared by both arms

Both arms start from Qwen3-VL-8B fine-tuned with low-rank adapters on verified demonstrations from a larger frozen model (Qwen3-VL-235B-A22B), at most 40 per task. Both are trained with group relative policy optimization ([GRPO](https://arxiv.org/abs/2402.03300)), with eight trajectories per video, advantages normalized within groups and groups with identical rewards skipped ([DAPO](https://arxiv.org/abs/2503.14476)). Rollouts, data order and sampler are identical. Both receive a per-feature reward against the reference and apply the same checks:

- *replay*: the function reproduces its value on the cited outputs, and nearly the same value on a copy with negligible noise;
- *known answers*: run on four development recordings with known values (two near the feature's 25th percentile, two near its 75th) using the expert pipeline's marks, the function lands within tolerance and orders them correctly;
- *range*: the value is physically plausible;
- *program form*: array operations from a fixed library only, with no branching on array identity and no numeric literals beyond physical constants and small integers.

With `e_f` the error of the submitted value against the reference in score units, the penalty is `P = (1/k) Σ_f [e_f + 0.5 · 1(f fails a check)]` and the reward is `−min(P, 3)`. Unparseable submissions receive −4.

### 4.3 Response checks (treatment arm only)

Before training, two to four perturbations are written for each feature from its definition, for example steepening the center-of-mass rise, shifting the moment the center of mass drops, or rescaling its height. For each perturbation, the expected effect (an increase, a decrease, or no change within tolerance) comes from applying it to the three-camera reference curves of development recordings and rerunning StaBLE's released feature code. The agent's function is run on the same perturbation of its cited single-camera signals with its marks held fixed, and it passes if the direction of change, or the invariance, matches. A feature that fails any response check counts as failing a check in the penalty above.

Holding the marks fixed means a function that reads a duration from the marks fails a perturbation that moves the event within the signal. Features whose definition depends only on task-level event times, with no body-signal threshold, are exempt and are evaluated through timing error. Every perturbation is validated on development recordings before training: the expert pipeline's functions must pass at least 90% of the time, and a suite of shortcut programs (a function of the marks only, of clip duration, of pixel height, a constant) must fail at least 95% of the time.

### 4.4 Held-out video transformations (evaluation only)

For 200 sealed trials stratified by task, three transformations of the whole video are made by resampling frames with corrected timestamps, so that appearance is unchanged:

- **uniform slowing** to 0.8× speed;
- **within-clip time warp**, slowing the movement phase while speeding the quiet phases so that the clip's total duration is unchanged, which defeats a function that reads clip length;
- **uniform speeding** to 1.25×.

All tools are rerun on the transformed videos. Expected changes come from applying the identical time transformation to the reference trajectories and rerunning StaBLE's released feature code. The expert pipeline is run on the same transformed videos of development participants first, to confirm that the tools still work after resampling and to set the response accuracy that is achievable with these tools.

### 4.5 The primary measure

For each feature expected to respond, and each transformed trial, the **change error** is the absolute difference between the method's predicted change (output on the transformed video minus output on the original) and the expected change, in score units. It is averaged over features within a task and then over tasks with equal weight. A **no-change predictor**, which always predicts zero change, gives the baseline. Features expected to stay constant are reported separately as negative controls, so that a method cannot score well by not responding at all.

## 5. Data, splits and leakage

**Dataset and ledger.** StaBLE contains 180 adults aged 18 to 87, from people with vestibular disorders to competitive athletes and dancers; 171 have usable single-camera video. A ledger lists every recorded trial (3,322) with its Cam0 video, reference features, participant, task and status. Thirty trials flagged for reconstruction error and three with imputed features are excluded from rewards, perturbation validation and the primary evaluation. Ninety-eight tasks not attempted for safety have no video.

**Splits.** Sixty participants are set aside before any analysis, stratified by StaBLE score quintile, age group and athlete status, and drawn from people who were never in the lab pilot's test set. This is a retrospective re-split, documented as such, with every baseline retrained without them. The other 111 participants form five stratified development folds, checked against the whole (Kolmogorov–Smirnov tests and standardized mean differences below 0.1).

**Leakage.** Perturbations, their expected responses, probes and tolerances come from development recordings only. The video transformations are fixed in advance, never applied during training, and evaluated once on sealed participants. Rescaling endpoints are refitted on training folds. Seven participants appear in StaBLE's public exemplar video; results are reported with and without them.

**Keeping the data's shape.** The RL sampler draws ledger rows with equal probability; the share of updates per task and per ability quintile is logged, and any task drifting by more than a quarter from its ledger share is reweighted. The 200 transformed sealed trials are stratified by task so that every task contributes.

## 6. Evaluation

**Primary outcome.** Change error on responsive features under the three held-out transformations, pooled, for the two trained arms.

**Controls.** The no-change predictor; a duration-only shortcut that computes each feature from the clip's length; a single-frame predictor; and a direct score predictor (Qwen3-VL-8B fine-tuned on scores), compared on change in task score, the only change it can express.

**Secondary outcomes.** Feature error on unmodified sealed videos (H2), change error by transformation (H3), invariance violations on features expected to stay constant, shortcut rate on audit recordings (H4), the agent's timing error under each transformation, and task-score error and within-task rank agreement.

**Failure rule.** A trial without usable output on either version of a video receives the training-fold mean on both and is counted as a fallback; comparisons are repeated on trials both arms completed.

## 7. Statistics

Participants are the unit of analysis, and every interval resamples participants with all their trials and transformations. Each arm is trained with seven paired seeds. Method claims target the expected improvement over retraining, with an interval that combines the spread between paired seed differences and the participant-bootstrap spread of the seed-averaged difference (t-distribution, Satterthwaite degrees of freedom), and whose coverage is checked by simulation before training. H1 succeeds if the upper 95% bound for the treatment-minus-control change-error difference is below zero. H2 is a non-inferiority test at a margin of 0.01 score units. H3 and H4 form one Holm-corrected family.

## 8. Scope and cost

| Item | H100-hours (estimate) |
|---|---|
| Tool cache, computed once | 400 |
| Tool outputs for 600 transformed sealed videos and the development validation | 80 |
| Demonstrations and warm-start fine-tuning | 300 |
| Perturbation validation and RL development runs | 300 |
| RL, two arms × seven seeds (about 150 each) | 2,100 |
| Evaluation | 50 |
| **Total** | **about 3,250** |

A reduced version runs RL on six tasks spanning the main task families (standing, sit-to-stand, single-leg, Y-Balance, jump, gait) for about 1,950 H100-hours.

## 9. What each outcome would mean

Smaller change errors with preserved accuracy (H1 and H2) would show that relations derived from a quantity's definition are a useful training signal beyond agreement with examples, at least for the transformations tested. A gain only on uniform slowing (H3 refuted) would suggest the agent learned something closer to the training perturbations than to the physical relation. Higher check-pass rates without lower change error would indicate adaptation to the checks. A loss of ordinary accuracy would quantify the cost of enforcing the definition over the agent's own visual timing.

Frame resampling can create artifacts that affect tools, but it does so identically for every method, and the expert pipeline's response sets the achievable ceiling. Synthetic changes of speed are a controlled probe and do not establish that a method detects naturally occurring differences between people or within one person over time. The expected changes come from a reconstructed reference, so errors that the reference shares with the monocular tool remain outside the test.
