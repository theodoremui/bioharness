# What Outcome Rewards Teach a Tool-Using Agent When Its Instruments Are Noisy: Feature-Level Rewards from a Privileged Reference

## Abstract

Reinforcement learning on the final answer is the standard way to improve tool-using agents, and it works well when the tools are reliable. In measurement tasks the tools are often noisier than the differences between the people being measured. A policy rewarded only for its final score can then gain by moving its answers toward typical values, or by letting errors in different intermediate quantities cancel. This proposal studies that regime with a tool-calling vision-language agent that measures balance from one smartphone video. During training, a three-camera reconstruction supplies a reference value for every intermediate feature, so the reward can be placed on each feature instead of on the final score. The study compares the two rewards on unseen people and, by injecting calibrated noise into cached tool outputs, maps how each behaves as the tools become less reliable than a guess. It tests two competing predictions: that per-feature rewards prevent the drift toward typical values, or that they remove cancellation while inheriting the drift, because each feature's own error is also reduced by shrinking toward that feature's average.

## 1. Motivation

### 1.1 The measurement task

In the StaBLE "rise to toes" task ([Heigold et al., 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13621976/)), a person rises onto their toes as quickly and as high as they can and holds for five seconds. Three **features** describe the performance: the peak upward speed of the **center of mass** (the average position of the body's mass), the peak ankle angle, and the time the center of mass stays high. Each is rescaled to a 0-to-1 range and the rescaled values are averaged into a **task score**. StaBLE has 18 tasks and 76 features, recorded from 180 adults with three smartphones.

The agent studied here is a **vision-language model** (a network that takes video frames and text and produces text) that works through **tool calls**: structured requests, such as running a pose detector, that surrounding software (the **harness**) executes and answers. Given one camera's video, it calls pose, segmentation and 3D-reconstruction tools, writes short functions that turn their outputs into the task's features, and submits the features; the task's fixed formula computes the score. **Reinforcement learning (RL)** then samples the agent's own attempts (**trajectories**), scores each with a **reward**, and shifts the model toward the higher-scoring ones.

### 1.2 The regime: tools noisier than the population

A pilot in the lab found that a constant guess of each task's average score had a task-averaged error of 0.120 on held-out participants, while reconstructing the skeleton from one camera and applying StaBLE's rules had 0.146 and produced a valid score for only 567 of 729 cases. The single-camera instruments are, on average, less informative than the population average.

Statistics says what an estimator should do in that situation. If a tool reading is `t = y + ε`, where `y` is the person's true value with spread `σ_y` across people and `ε` is tool error with spread `σ_ε`, the best linear estimate under squared error is `m + w·(t − m)`, with population mean `m` and weight `w = σ_y² / (σ_y² + σ_ε²)`. Under absolute error the optimum is a posterior median with a similar pull toward the center. As `σ_ε` grows past `σ_y`, `w` falls below one half and the best estimate approaches the constant. An agent that writes its own feature code can implement this pull — smoothly (`0.5 · reading + 0.5 · typical`) or abruptly (returning a typical value whenever a tool output looks unreliable) — and RL will favor whichever raises the reward.

### 1.3 What rewarding only the final score allows

Rewarding the final score, `−|Ŝ − S*|`, leaves three openings. The first is the pull toward typical values described above, which preserves ranks when it is uniform but destroys them when the policy switches to constant answers on hard cases. The second is **cancellation**: because the score is an average, an overestimated ankle angle and an underestimated hold time can produce the right score from two wrong measurements. The third is weak **credit assignment**: one number summarizes several features, so the reward cannot say which feature was wrong. Outcome-only RL has been reported to make video models stop using the video ([Xu, 2026](https://arxiv.org/abs/2606.22043)), and RL-trained tool agents to skip verification steps ([Thaman, 2026](https://arxiv.org/abs/2605.02964)).

### 1.4 What a privileged reference makes possible, and what it may not fix

The three-camera reconstruction gives a reference for every feature of every training trial, and it is unavailable when the agent is deployed. That **privileged** reference allows a per-feature reward, `−(1/k) Σ_f e_f`, where `e_f` is the error of feature `f` after rescaling. Because the score is the average of the rescaled features, the triangle inequality gives `|Ŝ − S*| ≤ (1/k) Σ_f e_f`: a small per-feature penalty guarantees a small score error, and cancelling errors are penalized. Per-feature rewards therefore close the second opening and should help with the third. Whether they close the first is unclear, because each feature's own error is also lowered by pulling it toward that feature's average. The study is designed around that uncertainty.

## 2. Research question and hypotheses

> **Research question.** When a tool-calling agent's instruments are noisy relative to the differences between people, does rewarding each intermediate feature against a privileged three-camera reference, instead of rewarding the final score, make the agent's measurements of unseen people more accurate? And does it prevent the drift toward typical values that outcome rewards produce as the tools become less reliable?

| ID | Hypothesis | Refuted if |
|---|---|---|
| H1 (primary) | Per-feature rewards give lower feature error on sealed participants at the tools' natural noise level | The 95% interval for the expected difference over retraining includes zero |
| H2 | Outcome rewards leave more cancellation | The cancellation gap (Section 6) does not differ between arms |
| H3 | Under outcome rewards, the calibration slope falls as tool noise grows | The slope does not decline across noise levels |
| H4a or H4b (competing) | (a) Under per-feature rewards the slope stays near its natural-level value; (b) it falls as under outcome rewards | The reward-by-noise interaction on slope decides between them (Section 7) |
| H5 | Per-feature rewards learn faster | They do not reach the outcome arm's final development feature error in fewer rollouts |

**What the study would establish.** Work on RL for tool use has studied reward granularity in terms of formats, tool names and arguments ([ToolRL](https://arxiv.org/abs/2504.13958)), and process supervision has studied rewards on reasoning steps ([Lightman et al., 2023](https://arxiv.org/abs/2305.20050)). Neither has a setting where the intermediate quantities are physical measurements with known reference values and where instrument noise can be dialed up and down. This study provides one. Its central product is a measured map of when outcome rewards suffice for a tool-using agent and which of their failures a better training-time instrument repairs. If H4b holds, the result is general and somewhat sobering: denser intermediate rewards fix cancellation and credit assignment, but they do not stop a policy from regressing toward the population when its tools are poor. Something else, such as constraints on the agent's code, would then be needed.

## 3. Related work

**RL for tool use.** [DeepEyes](https://arxiv.org/abs/2505.14362), [LongVT](https://arxiv.org/abs/2511.20785) and [VITAL](https://arxiv.org/abs/2508.04416) train vision-language models to crop, zoom or resample video from rewards on final answers. ToolRL shows that rewards on tool names and arguments shape what is learned, and [Search-R1](https://arxiv.org/abs/2503.09516) trains search policies from outcome rewards alone. Here the reward granularity concerns the physical quantities the tools are used to measure.

**Process supervision.** Rewarding intermediate steps improved mathematical reasoning (Lightman et al., 2023), with step labels collected from people or learned. In this setting the intermediate signal comes from a more accurate instrument, and the task's scoring rule supplies the decomposition of the score into features, so no step labels need to be collected.

**Reward misspecification.** Optimizing a proxy reward can move a policy away from the intended objective ([Gao et al., 2023](https://arxiv.org/abs/2210.10760)), and outcome rewards can teach agents to drop inputs or checks (Xu, 2026; Thaman, 2026). The pull toward typical values studied here is a case where the proxy (average error) and the intended objective (measuring the individual) diverge for a known statistical reason.

**Shrinkage.** That a noisy measurement should be combined with a population prior is classical Bayesian and empirical-Bayes estimation. The open questions are whether RL policies discover such behavior, in which form, and whether reward design controls it.

**Learning with privileged information.** Training-time information unavailable at test time has long been used to guide learning (Vapnik and Vashist, 2009). Here it enters only through the reward.

## 4. Method

### 4.1 Agent and harness

The agent (Qwen3-VL-8B) receives the Cam0 video, the task description and the feature definitions with units. Its tools are timestamped frames and crops, 2D landmarks (RTMPose or a second pose model), person segmentation (SAM 2.1), point tracks (CoTracker3) for 16 body regions, 3D joint angles and center of mass ([OpenCap Monocular](https://arxiv.org/abs/2603.24733), two settings), plotting and a Python sandbox. Expensive outputs are computed once and cached under the video, tool version and full arguments; requests outside the menu return an error. Large arrays stay in the sandbox, the model receives summaries or plots, and every signal is indexed by time in seconds.

### 4.2 Submissions

For each feature the agent submits a value, the function that computed it from cited tool outputs and from the start and end times it marked, the cited outputs, and the marks. The harness re-runs the function and requires the same value. This replay requirement applies to both arms, so the arms differ only in the reward, and neither receives a separate reward for its time marks (timing error is reported).

### 4.3 Rewards

With endpoints `L_f, U_f` fitted on training folds, each feature is rescaled by `n_f(x) = (x − L_f)/(U_f − L_f)` (reversed when lower is better), and `e_f = |n_f(x̂_f) − n_f(x*_f)|` is the error of the submitted value against the reference.

- **Outcome reward:** `−|Ŝ − S*|`, with `Ŝ = (1/k) Σ_f n_f(x̂_f)`.
- **Per-feature reward:** `−(1/k) Σ_f e_f`.
- **Both:** a submission that cannot be parsed or fails replay receives −4, below every valid attempt, and rewards are capped at −3 otherwise. GRPO normalizes advantages within each group of attempts, so the arms' different reward scales do not change step sizes.

Features whose reference was imputed or flagged for reconstruction error are left out of both rewards.

### 4.4 Training

Both arms start from the same model: Qwen3-VL-8B fine-tuned with low-rank adapters on demonstrations from a larger frozen model (Qwen3-VL-235B-A22B), kept when every feature replays and the mean feature error is below a preset threshold, at most 40 per task. RL uses group relative policy optimization ([GRPO](https://arxiv.org/abs/2402.03300)): eight trajectories per video, advantages normalized within each group, and groups whose trajectories all receive the same reward skipped, following [DAPO](https://arxiv.org/abs/2503.14476). Both arms receive the same number of rollouts, the same data order for each paired seed, and the same sampler.

### 4.5 The noise sweep

Noise is added to the cached tool outputs (landmarks, point tracks, joint angles and center-of-mass curves) as smooth, low-pass-filtered Gaussian perturbations, so that it resembles tool error more than frame-to-frame jitter. Its level is defined by a **tool-skill ratio** `ρ`: the expert pipeline's feature error divided by the constant guess's feature error, measured on development folds. Three levels are used: the natural tools (no added noise), `ρ ≈ 1` (tools as informative as guessing) and `ρ ≈ 1.5` (tools worse than guessing). For each video the noise realization is fixed across arms and seeds, so both arms see identical inputs, and sealed evaluation at each level uses fresh realizations of the same process. The video frames themselves are left clean, as they would be when a tool fails on a clear recording, and the agent is not told the noise level.

### 4.6 Agreement beyond the reference

The three-camera reconstruction shares its body model and inverse-kinematics step with the monocular tool, so a reward based on it could favor routes that share its errors. As a secondary check, annotators mark event times (start and end of the rise, the moment the heels return) on 300 sealed trials directly from video, independently of any pose model. Timing features computed by each arm are compared with these marks as well as with the reference.

## 5. Data, splits and leakage

**Dataset and ledger.** StaBLE contains 180 adults aged 18 to 87, from people with vestibular disorders to competitive athletes and dancers; 171 have usable single-camera video. A ledger lists every recorded trial (3,322) with its Cam0 video, reference features, participant, task and status. Measured trials are used everywhere. Thirty trials flagged for reconstruction error and three with imputed features are kept as inputs but excluded from rewards and the primary evaluation. Ninety-eight tasks not attempted for safety have no video and enter only the overall score, as zeros.

**Splits.** Sixty participants are set aside before any analysis, stratified by StaBLE score quintile, age group and athlete status, and drawn from people who were never in the lab pilot's test set. Because the pilot trained models on some of them, this is a retrospective re-split, documented as such, with every baseline retrained without them. The other 111 participants form five stratified development folds, checked against the whole (Kolmogorov–Smirnov tests and standardized mean differences below 0.1). Development decisions (thresholds, noise calibration, learning rates) use folds 1–4 for training and fold 5 for validation; final models train on all 111.

**Leakage.** Rescaling endpoints, which StaBLE computes over all 180 participants, are refitted on training folds, and sealed values outside 0–1 are kept unclipped. The noise calibration, fallback means and demonstrations come only from training folds. The three-camera reference is used only inside rewards and evaluation and never enters the agent's input. Seven participants appear in StaBLE's public exemplar video; results are reported with and without them.

**Keeping the data's shape.** The RL sampler draws ledger rows with equal probability. Skipped groups and the demonstration filter can tilt training toward easy or hard tasks, so the share of updates per task and per ability quintile is logged, and any task whose share drifts by more than a quarter from its ledger share is reweighted.

## 6. Evaluation

**Primary outcome.** Feature error in score units on sealed participants at the natural noise level, averaged over features within a task and then over tasks with equal weight. Errors in physical units are reported per feature. Every method is scored from its features as submitted.

**Cancellation gap.** With direction-aligned signed errors `d_f = n_f(x̂_f) − n_f(x*_f)`, the gap for a trial is `(1/k) Σ_f |d_f| − |(1/k) Σ_f d_f|`. It is zero when all errors share a sign and grows as they cancel. It is averaged over trials and tasks.

**Drift toward typical values.** Calibration slope (least-squares fit of predictions on references) at the feature level and the score level, per noise level, with the median over tasks reported. The **constant-output rate** is the share of submitted feature functions whose outputs barely change across four development recordings with widely different reference values, a direct count of the abrupt form of the drift.

**Secondary.** Task-score error, within-task rank agreement, skill against the constant guess, fallback rate, timing error against the three-camera segmentation and against the human marks, and learning curves of development feature error against rollouts.

**Failure rule.** A trial without usable output receives the training-fold task mean and is counted as a fallback; comparisons are repeated on trials both arms completed.

## 7. Statistics

**Unit.** Participants. Every interval resamples participants with all their trials and recomputes the estimator.

**Primary comparison.** Each arm is trained with seven paired seeds at the natural noise level (each pair shares its starting checkpoint and data order). The estimand is the expected improvement over retraining. Its interval combines the spread between paired seed differences with the participant-bootstrap spread of the seed-averaged difference, using a t-distribution with Satterthwaite degrees of freedom, and its coverage is checked by simulation before training under symmetric, skewed and failed-run seed distributions. H1 succeeds if the upper 95% bound for the per-feature-minus-outcome error difference is below zero.

**The sweep.** Each arm is trained with three seeds at each added noise level. Slopes are modeled with reward, noise level and their interaction as fixed effects and seed as a random effect, with participant-bootstrap intervals. H3 holds if the outcome arm's slope declines across levels. H4a is supported if the interaction shows a smaller decline under per-feature rewards, with an interval excluding zero, and the per-feature slope at `ρ ≈ 1.5` stays within 0.1 of its natural-level value. H4b is supported if the interaction interval includes zero while both arms decline.

**Multiplicity and power.** H2 and H5 form one Holm-corrected family. The sweep analysis is pre-specified and reported separately. Before training, power for a 0.01 difference in feature error is estimated from repeated fine-tuning runs and development predictions; if it falls below 60%, H1 is reported as an estimate.

## 8. Scope and cost

| Item | H100-hours (estimate) |
|---|---|
| Tool cache, computed once | 400 |
| Demonstrations and warm-start fine-tuning | 300 |
| RL development runs (one seed, fold 5 validation) | 300 |
| RL at natural noise, two arms × seven seeds (about 150 each) | 2,100 |
| RL noise sweep, two arms × two levels × three seeds, on six tasks (about 60 each) | 720 |
| Human event marks and evaluation | 50 |
| **Total** | **about 3,900** |

A reduced version runs all RL on six tasks spanning the main task families (standing, sit-to-stand, single-leg, Y-Balance, jump, gait) for about 2,600 H100-hours, with claims limited to those tasks.

## 9. What each outcome would mean

If per-feature rewards lower feature error (H1) and keep the slope as noise grows (H4a), a better training-time instrument repairs the main failures of outcome rewards in this regime. If they lower cancellation but the slope falls in both arms (H4b), the lesson is that intermediate rewards fix how errors combine without changing the incentive to regress toward the population, and preventing that needs constraints on what the agent may compute. If outcome rewards do not drift even at `ρ ≈ 1.5`, RL from this starting point keeps measuring under heavy noise, which would also be worth knowing. If H2 holds without H1, cancellation existed but did not matter for accuracy.

Injected noise differs from real tool failure, which is structured (missed events, depth errors, lost tracking), so the natural level carries the primary claim and the sweep is a controlled probe of mechanism. Agreement with the three-camera reference is the scope of the main result; the human event marks give a partial independent check for timing features only.
