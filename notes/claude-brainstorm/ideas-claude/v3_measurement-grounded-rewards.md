# Rewarding the Measurement: Training Tool-Calling Video Agents to Measure Balance Instead of Guessing It

*Version 3. Changes from v2: the reinforcement-learning reward now scores each intermediate feature against a three-camera reference, and a feature earns credit only if the harness can recompute it from the evidence the agent cites. This version also adds a sealed confirmatory test set that nobody has looked at, a learned non-agent baseline that sees the same tool outputs and feature labels, a fully specified cache of tool outputs, and exact definitions of every estimator.*

## Abstract

A model that predicts a balance score from video can reach a respectable average error by staying close to typical values, and reinforcement learning that rewards only the final number makes this drift more likely. We study a tool-calling vision-language agent that measures each balance task the way a biomechanist would: it runs pose, segmentation and reconstruction tools, writes code that computes the task's defined features, and passes them to a fixed scoring formula. Our main idea is to reward the measurement itself. During training, a three-camera motion-capture reconstruction supplies a reference value for every feature, so the agent is rewarded feature by feature. A feature earns credit only if the harness can re-run the agent's own code on the evidence the agent cited and obtain the same number. We test on the StaBLE dataset of eighteen balance tasks whether this reward, compared with rewarding the final score alone, yields agents that rank unseen people more accurately and report numbers that can be verified, and whether the gain comes from adaptive tool use or simply from access to tool outputs and feature labels.

## 1. Motivation

### 1.1 From video to a balance score

A video-based balance measurement has four stages. A pose model finds body landmarks in each frame; a reconstruction step turns them into a 3D skeleton whose joint angles and **center of mass** (the average position of the body's mass) change over time; a feature step reduces those curves to the few numbers a task cares about; and a scoring step rescales each feature to a 0-to-1 range and averages the rescaled features into a task score. In the StaBLE "rise to toes" task, the features are the peak upward speed of the center of mass, the peak ankle angle, and the time the center of mass stays high. StaBLE ([Heigold et al., 2026](https://doi.org/10.64898/2026.09.16.750744)) defines 76 features over 18 tasks, recorded from 180 adults ranging from people with vestibular disorders to professional dancers.

### 1.2 Two routes that each fail differently

On single-camera videos of 43 held-out participants, the lab's pilot found that rebuilding a 3D skeleton with OpenCap Monocular and applying StaBLE's rules gave valid scores for only 567 of 729 cases (task-averaged error 0.146). Predicting each task's average training score, without looking at the video, gave 0.120. A fine-tuned Qwen3-VL-8B gave 0.100, a 2D-pose temporal network 0.119, and the same VLM prompted without training 0.238, worse than the constant. The reconstruction route can be inspected but breaks when a step fails; the predictive route always answers but improves on the constant by only about a sixth and cannot show where its number came from.

### 1.3 Why error alone can hide a method that ignores the video

Take five people with true task scores 0.4, 0.5, 0.6, 0.7 and 0.8. A constant guess of 0.6 has mean absolute error 0.120. A predictor that keeps the right order but compresses every difference to a fifth of its size (0.56, 0.58, 0.60, 0.62, 0.64) has a lower error, 0.096, while almost erasing the differences between people. A predictor that measures with noise (0.50, 0.45, 0.70, 0.60, 0.85) has error 0.080 and keeps most of the spread. Three additional measures separate these cases: **rank agreement** (Spearman correlation between predicted and reference scores within a task), the **skill score** (one minus the ratio of a method's error to the constant's error, so zero means no better than ignoring the video), and the **calibration slope** (the slope of predicted on reference scores, near one when differences between people are kept and near zero when predictions collapse toward the average).

## 2. Concepts from first principles

**Vision-language model (VLM).** A neural network that takes images or video frames together with text and produces text. Here it is Qwen3-VL-8B ([technical report](https://arxiv.org/abs/2511.21631)).

**Tool call, harness, agent.** In a tool call, the model's output is a structured request, such as `pose2d(video_id, model="rtmpose")`, that software executes before returning the result as new input. The **harness** is that software: the tool descriptions, the loop that runs calls, the record of earlier steps, and the stopping rule. The model and harness acting over several steps form an **agent**, and one complete run from video to final answer is a **trajectory**.

**Supervised fine-tuning (SFT).** The model is shown example trajectories and its weights are adjusted so those trajectories become more probable. It copies good behaviour but cannot discover anything better than its examples.

**Reinforcement learning (RL) and rewards.** The model produces its own trajectories, a **reward** function scores each one, and the weights are adjusted to make high-reward trajectories more probable. **Group relative policy optimization** (GRPO, [Shao et al., 2024](https://arxiv.org/abs/2402.03300)) samples several trajectories for the same input and scores each relative to the group's average, so the model learns which of its own attempts were better than its typical attempt on that input.

**Why outcome-only rewards invite shortcuts.** If the reward depends only on the final score, any trajectory that lands near the right number is equally good, including one that never looks at the video and outputs a typical value. Outcome-only RL has been shown to make video-language models stop using the video ([Xu, 2026](https://arxiv.org/abs/2606.22043)), and RL-trained tool agents skip verification steps more often than their untrained counterparts ([Thaman, 2026](https://arxiv.org/abs/2605.02964)). A second problem is specific to averaged scores: if one feature is overestimated and another underestimated by the same amount, the score is right while both measurements are wrong.

**Privileged reference.** StaBLE was recorded with three cameras, and the three-camera reconstruction gives a reference value for every feature of every trial. The agent sees one camera. The reference is used to compute rewards during training and to evaluate at test time, and never enters the agent's input.

## 3. Research question and hypotheses

**Primary question.** By the ICML 2027 submission deadline (expected late January 2027), does training a Qwen3-VL-8B tool-calling agent with *measurement-grounded rewards* (per-feature error against the three-camera reference, credited only for verified features) yield higher mean within-task rank agreement on a sealed set of held-out participants than training the same agent, from the same starting point and for the same number of rollouts, with a reward on the final score alone?

**Secondary questions** (pre-registered, Holm-corrected as one family):

1. Does the measurement-grounded agent match or exceed the strongest non-agent methods: the fine-tuned direct predictor, an expert-written pipeline using the same tools, and a learned regressor that sees the same tool outputs and is trained on the same feature labels?
2. Does adaptive tool use matter? We compare the full agent with the same agent forced to make a fixed sequence of tool calls.
3. What fraction of the agent's reported features pass verification on held-out participants, where no reference is available to the agent or to the harness?

**Hypotheses.**

| ID | Hypothesis | Prediction that would refute it |
|---|---|---|
| H1 | Score-only RL drifts toward typical values | Its calibration slope on development folds stays within 0.1 of the starting model's |
| H2 | Measurement-grounded rewards raise rank agreement over score-only rewards | The crossed-bootstrap interval for the difference includes zero |
| H3 | The verification check is what blocks the shortcut | Removing the check leaves rank agreement and slope unchanged |
| H4 | Adaptive tool use beats fixed calls on cases where default tool settings fail | No difference on the pre-defined hard subset (Section 7.3) |

## 4. Related work

**VLMs and agents for movement analysis.** Knowledge-augmented gait VLMs ([Wang et al., 2024](https://arxiv.org/abs/2403.13756)), [BioGait-VLM](https://arxiv.org/abs/2603.08564) and [MyoMechanix](https://arxiv.org/abs/2608.26094) learn direct mappings from video, skeletons or phases to labels or feedback. [BiomechAgent](https://arxiv.org/abs/2602.06975) writes analysis code over processed motion-capture data and benefits from validated event-detection tools, without training the model. None of these trains a model to use measurement tools.

**Reinforcement learning for tool use.** [DeepEyes](https://arxiv.org/abs/2505.14362), [LongVT](https://arxiv.org/abs/2511.20785) and [VITAL](https://arxiv.org/abs/2508.04416) teach VLMs to crop, zoom or resample video with outcome rewards on question-answering tasks. [ToolRL](https://arxiv.org/abs/2504.13958) shows that finer-grained rewards on tool names and arguments help. Our rewards are fine-grained in a different sense: they score the physical quantities the tools are used to measure.

**Intermediate supervision.** Process reward models score reasoning steps with learned or human-labelled judgments. Our intermediate signal comes from an independent and more accurate measurement system that exists only at training time, and the task's own scoring rule supplies the decomposition of the score into features, so no step labels have to be collected or learned.

**Harness and prompt optimization.** [GEPA](https://arxiv.org/abs/2507.19457), [Meta-Harness](https://arxiv.org/abs/2603.28052) and [VidHarness](https://arxiv.org/abs/2609.38413) improve prompts or harness code without changing weights. [Wang et al. (2026)](https://arxiv.org/abs/2607.12227) find that their gains often disappear against budget-matched test-time scaling and on held-out tasks; we include both as baselines.

## 5. Method

### 5.1 Agent and harness

The agent receives the Cam0 video, the task description and the StaBLE feature definitions with units. Its tools are listed below. Large outputs (landmark arrays, joint-angle curves) stay inside a Python sandbox, and the model receives a short text summary or a plot, so the context stays small and the full-resolution data are never truncated. Every array is indexed by time in seconds taken from the original video.

| Tool | Returns | Cached or live |
|---|---|---|
| `frames(t0, t1, fps, crop)` | Timestamped frames | Live (cheap) |
| `pose2d(model)` | 2D landmarks per frame (RTMPose) | Cached |
| `segment_person()` | Person outline per frame (SAM 2.1) | Cached |
| `track_points(region)` | Point tracks (CoTracker3) on a fixed grid of 16 body regions | Cached |
| `reconstruct3d(setting)` | Joint angles and center of mass (OpenCap Monocular), two settings | Cached |
| `plot(signal, t0, t1)` | An image of a signal | Live |
| `python(code)` | Runs code on sandbox variables | Live |
| `submit(features)` | Ends the trajectory | Live |

### 5.2 The cached tool environment

Tool outputs are computed once and stored under a key made of the video identifier, the tool version and the complete argument list. Agent-chosen arguments are restricted to a menu so that every reachable call is in the cache: two OpenCap Monocular settings, two pose models, and 16 predefined body regions for point tracking. A call outside the menu returns an error message rather than triggering new computation. This makes every RL rollout cost only model inference and sandbox time, and makes runs exactly reproducible. We estimate the one-time cache cost at roughly 300 to 400 H100-hours, dominated by OpenCap Monocular (about four minutes per 17-second clip), and will measure it precisely on 50 videos in week 1.

### 5.3 What the agent submits, and how it is verified

For each feature `f` the agent submits a value `x̂_f` in physical units and a pointer `(cell_id, inputs, t0, t1)`: the sandbox cell that computed the value, the tool outputs it read, and the time window. The harness then runs three checks.

1. **Replay.** Re-execute the cell in a clean sandbox with the cited inputs. The result must equal `x̂_f` to within a relative tolerance of 10⁻⁶.
2. **Dependence.** Run the same cell on the cited tool outputs of two other development videos of the same task. The value must change. A cell that returns a constant fails, which closes the route of typing a typical value and attaching an unrelated pointer.
3. **Range.** The value must lie within the training-fold range of that feature, widened by half its width on each side.

A feature that passes all three is **verified**. Code then applies StaBLE's normalization and averaging to the submitted values; the model never writes the score.

### 5.4 Rewards

Let task `t` have `k` features. With endpoints `L_f` and `U_f` fitted on the training folds, each feature is mapped to the score scale by `n_f(x) = (x − L_f)/(U_f − L_f)` (or `(U_f − x)/(U_f − L_f)` when lower is better), and the task score is the average of the `n_f`. Define the feature error in score units as `e_f = |n_f(x̂_f) − n_f(x*_f)|`, where `x*_f` is the three-camera reference, and set `ẽ_f = min(e_f, 1)` if the feature is verified and `ẽ_f = 1` otherwise.

- **Measurement reward:** `R_meas = −(1/k) Σ_f ẽ_f`.
- **Score-only reward (ablation):** `R_score = −|Ŝ − S*|`, with no verification.
- **Format penalty:** −1 for a submission that cannot be parsed.

Because the score is an average of the `n_f`, the triangle inequality gives `|Ŝ − S*| ≤ (1/k) Σ_f e_f`. For verified features, the score error can never exceed the measurement penalty, so a trajectory with a small penalty also has a small score error. The converse fails, because opposite feature errors cancel in the score, and that gap is what the score-only reward leaves open. Features whose reference was imputed in the StaBLE release (3 trials) or flagged for reconstruction error (30 trials) are masked from the reward.

### 5.5 Training loop

1. **Warm start.** A larger frozen model (Qwen3-VL-235B-A22B, or a frontier API model if access is granted) runs the same harness on development training folds with eight attempts per video. We keep trajectories whose features are all verified and whose measurement reward exceeds a threshold fixed in advance, cap the kept trajectories at 40 per task, and fine-tune Qwen3-VL-8B on them with low-rank adapters. Week 2 measures the yield per task; tasks with fewer than 10 kept trajectories are flagged as RL-only.
2. **GRPO.** For each video in a batch, sample eight trajectories, compute rewards, and normalize advantages within the group. Groups in which every trajectory receives the same reward carry no learning signal and are skipped, following the dynamic sampling of [DAPO](https://arxiv.org/abs/2503.14476). Training uses the same number of rollouts for every reward variant.

### 5.6 Keeping the training data in the same shape as the dataset

Every sampler draws participant–task rows from the ledger (Section 6.1) with equal probability, so the mix of tasks, ages and ability levels seen in training matches the training folds. Two steps can tilt this mix: the warm-start filter keeps more trajectories from easy tasks, and skipping zero-variance groups removes examples that are too easy or too hard. We log the share of updates per task and per ability quintile, and if any task's share drifts more than 25% (relative) from its ledger share, its examples are reweighted. Evaluation always uses every ledger row in the test set.

## 6. Data, splits and leakage control

### 6.1 Ledger

One row per participant–task slot (180 × 18). Each row records whether the task was performed, whether a usable Cam0 video exists, the reference features and task score, and a status: *measured*, *assigned zero* (task not attempted for safety, 98 trials), *imputed* (3 trials, features regressed on age), *flagged* (30 trials with reconstruction error) or *excluded* with a reason. Assigned and imputed targets are never treated as measurements. The lab's pilot used 171 participants; the ledger records why 9 were dropped, and we check that they do not differ in age or ability from those kept.

### 6.2 A sealed confirmatory set

The lab's 43 test participants have already been used to compare six methods, and what was learned from them (for instance the Y-Balance failure) shaped this design. They therefore move into the development set. A new confirmatory set of 43 participants is drawn, stratified by StaBLE score quintile, age group and elite-athlete status, from the 128 participants that no one has evaluated on. Its videos and references are stored separately and are not opened until every method is frozen. The remaining 128 participants (85 original training participants plus the former test participants) form five development folds, stratified in the same way, with each fold's task-score distributions checked against the full development set. All baselines, including the lab's fine-tuned predictor, are retrained under this split, so the slide numbers serve only as motivation.

### 6.3 Leaks we close

1. **Same person on both sides:** participant-level splits.
2. **Normalization:** StaBLE's published endpoints use all 180 participants. We refit `L_f, U_f` on the training folds of each cross-validation split, and on all 128 development participants for the final models. Test values may fall slightly outside 0–1 and are not clipped.
3. **Text shown to the model:** examples and prompt text come only from training folds.
4. **Public videos:** seven participants appear in StaBLE's public exemplar video; we report results with and without any of them who land in the confirmatory set.
5. **Feature design:** StaBLE's features were designed on all 180 participants. We treat the feature definitions as part of the measurement instrument and say so, since this cannot be undone.

### 6.4 Failure rule

Any case without a valid score receives the training-fold task mean, the constant guess. Every method is scored on every confirmatory row, and **verified coverage**, the share of rows whose features all pass verification, is reported separately. A fallback score is never counted as a measurement.

## 7. Experiments

### 7.1 Methods compared

| Group | Method | What it isolates |
|---|---|---|
| Reference points | Constant task mean; RTMPose + temporal network; fine-tuned direct predictor; feature-prompted VLM | Lab baselines, retrained |
| Same tools, no agent | Expert pipeline (fixed calls, hand-tuned fallbacks); tool-feature regressor (fixed calls, gradient-boosted trees trained on feature labels) | Whether tools and feature labels alone explain any gain |
| Frozen agent | Fixed harness; GEPA-optimized prompts; Meta-Harness-style harness search; best-of-8 with median features (no labels used for selection) | Gains without changing weights, and plain test-time scaling |
| Trained agent | Warm start only; score-only GRPO; measurement GRPO without verification; measurement GRPO with verification (full) | The reward design |
| Ablation | Full agent forced into a fixed call sequence | Adaptive tool use |

### 7.2 Outcomes and estimators

All estimators are computed on the confirmatory set. **Task-averaged error**: average the absolute score error within each task, then average the 18 task values equally. **Skill**: `1 − MAE_t / MAE_t(constant)` per task, averaged over tasks. **Rank agreement**: Spearman correlation within each task, averaged over tasks. **Calibration slope**: per task, median across tasks. **Verified coverage**: as defined above. **Feature error**: per feature, in score units.

### 7.3 Diagnostics

- **Video swap.** Each confirmatory video is replaced by another participant's video of the same task. A method whose output barely changes is not using the video; we report the correlation between the change in output and the change in reference.
- **Hard subset.** Defined without reference values, from the expert pipeline's own quality flags (reconstruction failure, no event detected, low pose confidence). H4 is tested on this subset.

### 7.4 Statistics

**Unit of analysis.** Participants. Every bootstrap replicate resamples participants with all their rows and recomputes the estimator from scratch.

**Two kinds of claim.** A claim about a frozen agent resamples participants. A claim about a training method resamples seeds and participants together (a crossed bootstrap), because a lucky run shifts every participant at once. Primary arms (score-only and full measurement GRPO) use three seeds; other trained arms use one seed and are labelled exploratory.

**Decision rule for the primary question.** The 95% crossed-bootstrap interval for the difference in mean rank agreement lies above zero, and the interval for the skill difference has a lower end above −0.02.

**Power.** In week 2, the spread of per-participant differences is estimated from cross-validated baselines. If the minimum detectable difference in rank agreement with 43 participants exceeds 0.05, the confirmatory set is enlarged to 60 participants before any training begins.

## 8. Compute, timeline and scope

**Compute assumption.** Eight H100 GPUs for ten weeks (about 13,000 GPU-hours). The cache needs roughly 400; each GRPO run of about 30,000 rollouts is estimated at 150 to 250, to be measured in week 3. If the measured cost exceeds the budget, the scope shrinks in this order: one seed for non-primary arms, then fewer rollouts for ablations, then dropping harness search.

| Weeks from 26 Oct 2026 | Work |
|---|---|
| 1–2 | Ledger, sealed split, refitted endpoints, power estimate; tool cache; expert pipeline |
| 3–4 | Frozen-agent arms, GEPA, harness search; warm-start trajectories |
| 5–8 | SFT and GRPO arms |
| 9 | Freeze all methods; open the confirmatory set once |
| 10–13 | Analysis and writing |

## 9. Risks

If the verification check is too strict, few trajectories earn any credit and learning stalls; the check's tolerances are set on development folds before RL starts. If OpenCap Monocular fails on the same cases for every method, no method can measure them; 2D pose and point tracks give the agent an alternative for timing features. If the expert pipeline matches the trained agent at lower cost, that is the result we report.
