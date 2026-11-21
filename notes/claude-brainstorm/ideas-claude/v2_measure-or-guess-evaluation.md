# Measuring or Guessing? Tool-Calling Vision-Language Agents for Balance Assessment from One Camera

*Version 2. Changes from v1: the evaluation now asks whether a method measures the person in the video or falls back on typical values; a data ledger, training-only normalization and a single failure rule make every method see the same data on the same terms; and the four improvement methods become a sequence of hypotheses with decision rules.*

## Abstract

A balance score computed from one smartphone video is only useful if it reflects the person in that video. On the StaBLE balance dataset, simply predicting each task's average score is already close to the best learned model, which means a method can look accurate while saying little about the individual. We propose to train a vision-language model to conduct the analysis with tools: it calls pose, segmentation and reconstruction software, computes each task's defined features in code, and passes them to a fixed scoring formula. We judge every method, including this agent, by whether it orders people correctly within each task, how much it improves on the average-score guess, and whether its predictions shrink toward typical values, with all methods trained and tuned on one group of participants and tested once on another. The study asks whether the inspectable agent can match or exceed a fine-tuned direct predictor on these measures, and which way of improving the agent (better prompts, better harness code, fine-tuning or reinforcement learning) contributes most.

## 1. Motivation

### 1.1 From video to a balance score

A video-based balance measurement passes through four stages. A pose model locates body landmarks such as ankles, knees and hips in each frame. A reconstruction step turns those landmarks into a 3D skeleton whose joint angles and **center of mass** (the average position of the body's mass) change over time. A feature step reduces these curves to a few numbers that capture what the task asked of the participant. In the "rise to toes" task, for instance, the features are the peak upward speed of the center of mass, the peak ankle angle, and how long the center of mass stays high. A scoring step finally rescales each feature to the 0-to-1 range and averages the rescaled features into a task score. The StaBLE protocol ([Heigold et al., 2026](https://doi.org/10.64898/2026.09.16.750744)) defines 76 such features across 18 tasks and averages the 18 task scores into a single balance score.

### 1.2 What the lab has learned so far

On single-camera videos from 43 held-out participants (729 task scores), the lab compared six approaches.

| Approach | Task-averaged absolute error |
|---|---|
| Rebuild a 3D skeleton with OpenCap Monocular, then apply StaBLE rules | 0.146 (valid for 567 of 729 cases) |
| Predict each task's mean training score, ignoring the video | 0.120 |
| 2D pose plus a learned temporal network | 0.119 |
| Qwen3-VL-8B prompted for a score, no training | 0.238 |
| Qwen3-VL-8B fine-tuned to output scores | 0.100 |
| Qwen3-VL-8B prompted to output features, score computed in code | 0.179 |

Two observations motivate this proposal. The reconstruction route is inspectable but brittle: when a step fails, as when the Y-Balance script cannot find the moment the toe reverses direction, there is no score at all. The learned predictors always answer, yet the best of them improves on a constant guess by only about a sixth, and none of them can show where its number came from.

### 1.3 Why a small error can hide a method that ignores the video

Consider five people whose true task scores are 0.4, 0.5, 0.6, 0.7 and 0.8.

| Predictor | Predictions | Mean absolute error | Rank agreement | Slope |
|---|---|---|---|---|
| Constant guess | 0.6 for everyone | 0.120 | none | 0 |
| Shrunk but ordered | 0.56, 0.58, 0.60, 0.62, 0.64 | 0.096 | perfect | 0.2 |
| Noisy but measuring | 0.50, 0.45, 0.70, 0.60, 0.85 | 0.080 | 0.8 | 0.85 |

The second predictor beats the constant on error while compressing all differences between people to a fifth of their true size; the third has a similar error but keeps those differences. Mean absolute error alone cannot tell these apart, so we add three measures. **Rank agreement** is the Spearman correlation between predicted and reference scores within a task: it asks whether the method puts people in the right order, which is how the StaBLE paper itself validates its score against clinical scales. The **skill score** is one minus the ratio of a method's error to the constant guess's error, so zero means "no better than ignoring the video." The **calibration slope** is the slope of a straight-line fit of predicted scores on reference scores; a value near one means differences between people are preserved, and a value near zero means predictions collapse toward the average.

### 1.4 Why an agent

A **vision-language model (VLM)** is a neural network that takes images or video frames together with text and produces text. In **tool calling**, part of the model's output is a structured request, such as `pose2d(video, model="rtmpose")`, which the surrounding software executes before returning the result to the model as new input. That surrounding software is the **harness**: the tool descriptions, the loop that runs calls, the record of earlier steps, and the stopping rule. The model plus its harness, acting over several steps, is an **agent**.

The agent route gives geometry to specialist tools that are already validated, so the VLM never has to estimate a speed in meters per second from pixels. The VLM keeps the jobs it handles well: reading the task description, choosing tools and settings, looking at frames or plots to notice a failed step, and writing the short program that turns tool outputs into features. Because a fixed formula turns features into the score, every score can be traced back to measurements. [BiomechAgent](https://arxiv.org/abs/2602.06975) found that a validated gait-event tool improved a code-writing agent's timing answers, and [DeepEyes](https://arxiv.org/abs/2505.14362) showed that reinforcement learning can teach a VLM when to use a visual tool.

## 2. Research question and hypotheses

**Primary question.** By the ICML 2027 submission deadline (expected late January 2027), does a Qwen3-VL-8B agent that calls existing analysis tools and reports StaBLE features achieve higher mean within-task rank agreement with three-camera reference scores than the fine-tuned direct predictor, on the 43 held-out participants, without a lower skill score?

A win over the fine-tuned predictor is not enough on its own. The agent must also match or beat an **expert pipeline**: a fixed program, written by a lab member in the first two weeks, that calls the same tools in a hand-chosen order with hand-tuned fallbacks (for example, 2D pose for timing features when the 3D reconstruction fails). If the expert pipeline is as accurate and cheaper, the case for learning disappears, and we will report that as the finding.

The outcome is measurable (rank agreement and skill score, both defined above), the comparison is with an existing result, the tools and data already exist, the question decides whether an inspectable analysis can compete with an opaque one, and the work fits in about thirteen weeks.

**Hypotheses, tested in order on development data only.**

| Stage | Hypothesis | Test on development folds | Decision |
|---|---|---|---|
| A. Re-baseline | The fine-tuned predictor's advantage over the constant guess comes mostly from shrinkage: calibration slope below 0.5 | Re-run all baselines under the new protocol | If the slope is above 0.8, rank agreement becomes a secondary outcome and the primary question reverts to error |
| B. Frozen agent | Tools raise rank agreement above both prompting baselines | Frozen Qwen with the fixed harness | If not, inspect failure logs before any optimization |
| C. Prompts and harness | Optimizing prompts and harness code improves the frozen agent at low cost | GEPA, then harness search | Carry the better of the two forward |
| D. Fine-tuning | Training on successful agent runs improves tool choice | Low-rank adapters on Qwen3-VL-8B | Carry forward if it beats stage C |
| E. Reinforcement learning | Rewarding closeness to the reference improves further | GRPO from the stage D model | Final candidate |

## 3. Related work

**VLMs for movement assessment.** Knowledge-augmented prompt tuning ([Wang et al., 2024](https://arxiv.org/abs/2403.13756)), [BioGait-VLM](https://arxiv.org/abs/2603.08564) and [MyoMechanix](https://arxiv.org/abs/2608.26094) feed gait parameters, skeleton tokens or phase structure into VLMs that classify or coach. They learn direct mappings and do not call measurement tools.

**Agents for biomedical analysis.** [Biomni](https://doi.org/10.1101/2025.05.30.656746) and [BiomechAgent](https://arxiv.org/abs/2602.06975) give language-model agents domain tools but start from processed data and do not train the model.

**Learning to use tools.** [DeepEyes](https://arxiv.org/abs/2505.14362), [LongVT](https://arxiv.org/abs/2511.20785) and [ToolRL](https://arxiv.org/abs/2504.13958) train tool use with reinforcement learning, mostly on question answering.

**Improving harnesses without training.** [GEPA](https://arxiv.org/abs/2507.19457), [Meta-Harness](https://arxiv.org/abs/2603.28052) and [VidHarness](https://arxiv.org/abs/2609.38413) optimize prompts or harness code from run feedback. [Wang et al. (2026)](https://arxiv.org/abs/2607.12227) report that such gains often vanish against budget-matched test-time scaling and on held-out tasks.

## 4. Data, splits and leakage control

### 4.1 A fixed ledger that every method shares

The StaBLE recordings form a nested structure: participant, task, trial, camera, frame. Before any experiment we write a ledger with one row per participant–task slot (180 × 18 = 3,240 rows). Each row records whether the task was performed, whether a single-camera video exists, the reference features and task score, and the reason for any exclusion. The lab's pilot used 2,968 usable examples from 171 participants; the ledger will document why 9 participants and the remaining slots were excluded, and we will check that the excluded participants do not differ in age or ability from those kept, since a systematic exclusion would change the population the results describe. Every method, baseline and ablation reads the same ledger, and every reported number states how many ledger rows it covers.

Videos keep their native timing. When the VLM receives subsampled frames, each frame carries its original timestamp, and every tool output is indexed by time in seconds, because hold times and speeds depend on true time.

### 4.2 Splits

The 43 test participants from the lab's pilot remain the test set, so results stay comparable with Section 1.2. The other 128 participants form the development set, divided into five folds by participant, so all of a person's videos fall in one fold. Folds are stratified by StaBLE score quintile, age group (under 40, 40 to 64, 65 and over) and elite-athlete status, and we check after splitting that each fold's distribution of every task score matches the whole development set (two-sample Kolmogorov–Smirnov test and standardized mean differences below 0.1). We also report how the fixed test set compares with the development set on the same variables.

### 4.3 Leaks we close

1. **Same person on both sides.** Prevented by participant-level splits.
2. **Normalization endpoints.** StaBLE rescales each feature using its minimum and maximum over all 180 participants. For the primary analysis we recompute these endpoints from development participants only, which allows test scores slightly outside 0–1; the published scale is reported as a secondary analysis.
3. **Prompt examples.** Few-shot examples and any text shown to the model come only from development folds.
4. **Public videos.** Seven participants appear in a public exemplar video in the StaBLE paper. Results are reported with and without any of them who fall in the test set.
5. **Repeated test use.** The test set is evaluated once, after every model, prompt and harness is frozen; the evaluation script and its outputs are logged.

### 4.4 One failure rule for every method

When a method returns no valid score (a tool fails, the output is malformed, or a time limit is reached), that case receives the training-task mean, the score the constant guess would give. All 729 test cases are therefore scored for every method, and the fraction of cases that fell back is reported next to each result. Results restricted to valid cases are shown as a secondary analysis, as for OpenCap Monocular in the lab's pilot.

## 5. The agent

The agent receives the Cam0 video, the task description and the StaBLE feature definitions with units. Its tools are a frame viewer that returns timestamped frames or crops, RTMPose for 2D landmarks, SAM 2.1 for the person's outline, CoTracker3 for point tracks, OpenCap Monocular for 3D joint angles and center of mass, a plotter that returns an image of any signal, and a Python sandbox. All tool outputs are computed once per video and cached, so repeated runs cost only model time.

The agent returns the task's features in physical units. For each feature it also returns the name of the tool output and the time window it used, so a reader can recompute the value. Code applies the StaBLE normalization; the model never writes the score.

The four improvement methods are defined as in v1: GEPA prompt optimization, Meta-Harness-style search over harness code, low-rank fine-tuning on successful runs, and group relative policy optimization ([GRPO](https://arxiv.org/abs/2402.03300)) rewarding closeness of the computed score to the reference. To keep the fine-tuning data from over-representing easy tasks, we cap the number of examples per task and report how many successful runs each task and ability quintile contributed.

## 6. Statistics

**Unit of analysis.** Each participant contributes up to 18 task scores, and those scores are correlated because they come from one body. All confidence intervals therefore resample participants, never individual videos.

**Primary contrast.** For the agent and the fine-tuned predictor, compute the Spearman correlation between predicted and reference scores within each task, average across tasks, and take the difference. A 95% interval comes from 10,000 bootstrap resamples of test participants, recomputing every task correlation in each resample. The agent is judged better if the interval lies above zero and the skill-score difference has an interval whose lower end is above −0.02.

**Secondary contrasts.** Pre-registered before any test evaluation: each stage's best agent against the previous stage, and the final agent against OpenCap Monocular. Holm's correction controls the family-wise error across these.

**Seeds and the two kinds of claim.** Stochastic methods (prompt search, harness search, fine-tuning, reinforcement learning) are run with three seeds. Two different claims are possible and we keep them apart. A claim about *one frozen agent* ("this delivered program orders test participants better") resamples participants only. A claim about *a training method* ("reinforcement learning improves this agent") must also account for the luck of a particular run, because a fortunate seed shifts every participant at once and more participants cannot average that away. For method claims we therefore use a crossed bootstrap that resamples seeds and participants together, and the decision rule above applies to that interval.

**Power.** In weeks 1 and 2 we estimate, from cross-validated baselines on the development set, the spread of per-participant differences between two methods. With 43 participants, 80% power and a two-sided 5% test, the smallest detectable difference is roughly 2.8 times that spread divided by the square root of 43. If this exceeds the smallest effect we consider meaningful (0.05 in mean rank agreement), we switch, before any test results are seen, to five-fold cross-validation over all 171 participants for the cheaper methods.

## 7. Timeline (from 26 October 2026)

| Weeks | Work |
|---|---|
| 1–2 | Ledger, splits, endpoint recomputation, power estimate; cache tool outputs |
| 3 | Stage A re-baselining |
| 4–5 | Stages B and C |
| 6–9 | Stages D and E |
| 10 | Freeze; single test evaluation |
| 11–13 | Analysis and writing |

## 8. Risks

If the agent depends on OpenCap Monocular for every task, it inherits its failures; cheaper timing tools (2D pose, point tracking) give an alternative path. Reinforcement learning with video inputs is the most expensive stage; caching tool outputs keeps each rollout to model inference plus a sandbox call.
