# Conducting the Analysis or Predicting the Score? Tool-Calling Vision-Language Agents for Single-Camera Balance Assessment

## Abstract

Smartphone video could make balance testing routine, but the two established ways of turning one video into a balance score each fall short. Rebuilding a 3D skeleton and applying a task's scoring rules can be inspected step by step, yet it is slow and returns nothing when a step fails. Training a model to map video straight to a score always gives an answer, but the answer cannot be traced to anything a clinician can check, and on a recent balance dataset it improves only modestly on a constant guess. This proposal tests a third option: a vision-language model that conducts the analysis, calling pose, segmentation and reconstruction tools, computing each task's defined features in code, and passing those features to the task's fixed scoring formula. The study asks whether such an agent predicts the balance of unseen people more accurately, and for more of them, than the same model trained to output the score directly. It also measures how much of any advantage remains when simpler methods receive the same tools and the same feature labels, and which of three ways of improving the agent without reinforcement learning pays off per unit of compute.

## 1. Motivation

### 1.1 From video to a balance score

Biomechanics describes how the body moves. A video-based measurement of a balance task usually passes through four stages. A pose model locates body landmarks such as ankles, knees and hips in each frame. A reconstruction step turns those landmarks into a 3D skeleton whose joint angles and **center of mass** (the average position of the body's mass) change over time. A feature step reduces those curves to a few numbers that capture what the task asked of the person. In the StaBLE "rise to toes" task, a person rises onto their toes as quickly and as high as possible and holds for five seconds, and the three **features** are the peak upward speed of the center of mass, the peak ankle angle, and the time the center of mass stays high. A scoring step rescales each feature to a 0-to-1 range and averages the rescaled values into a **task score**. The StaBLE protocol ([Heigold et al., 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13621976/)) defines 76 features across 18 tasks and averages the task scores into one balance score.

### 1.2 Two routes, two kinds of failure

A pilot study in the lab compared both routes on single-camera StaBLE videos of 43 held-out participants (729 task scores).

| Route | Method | Task-averaged absolute error |
|---|---|---|
| Reconstruct, then apply the rules | OpenCap Monocular followed by StaBLE's scoring code | 0.146, with a valid score for only 567 of 729 cases |
| Ignore the video | Each task's mean training score | 0.120 |
| Predict directly | 2D pose with a learned temporal network | 0.119 |
| Predict directly | Qwen3-VL-8B prompted for a score | 0.238 |
| Predict directly | Qwen3-VL-8B fine-tuned on scores | 0.100 |
| Predict features | Qwen3-VL-8B prompted for features, score computed in code | 0.179 |

The reconstruction route can be checked at every stage, but one failed step leaves no score. In the Y-Balance task, for instance, the scoring code looks for the moment the toe reverses direction during each reach and often finds none in a monocular reconstruction, and each 17-second clip costs about four GPU-minutes. The direct route always answers, but its best version improves on the constant guess by only about a sixth, and nothing in its output shows where the number came from.

### 1.3 Why an agent, and why its value is uncertain

A **vision-language model (VLM)** is a neural network that takes images or video frames together with text and produces text. In **tool calling**, part of that output is a structured request, such as `pose2d(video, model="rtmpose")`, which surrounding software executes before returning the result to the model as new input. That software is the **harness**: the tool descriptions, the loop that runs calls, the record of earlier steps and the stopping rule. The model and its harness acting over several steps form an **agent**, and one complete run from video to answer is a **trajectory**.

An agent can divide the work by what each component handles well. Specialist tools — several of them validated against laboratory motion capture — compute the geometry. The VLM reads the task description, chooses tools and settings, requests frames or plots to judge whether a tool output is plausible, and writes the short program that turns a center-of-mass curve into a peak speed. A fixed formula then turns the features into a score, so every score can be traced to measurements. [BiomechAgent](https://arxiv.org/abs/2602.06975) found that adding a validated gait-event tool improved a code-writing agent's answers, and systems that compose vision tools through generated programs ([VisProg](https://arxiv.org/abs/2211.11559), [ViperGPT](https://arxiv.org/abs/2303.08128)) have done well on visual question answering.

Whether this pays off for physical measurement is not obvious. The agent inherits the tools' failures. Its score accumulates the errors of every feature, while a direct predictor trained end to end can learn to absorb systematic biases. And an apparent advantage may come from the feature labels or from the tools themselves, which simpler methods could also use. The study is designed to tell these explanations apart.

## 2. Research question and hypotheses

> **Research question.** Does a vision-language agent that measures a balance task's defined features with tools, and scores them with the task's fixed formula, predict the three-camera balance scores of unseen people more accurately, and for more of them, than the same model trained to output scores directly? How much of any advantage remains once a fixed pipeline and a learned regressor receive the same tools and the same feature labels?

**Secondary question.** Of three ways to improve the agent without reinforcement learning (optimizing its prompts, searching over its harness code, and fine-tuning it on verified demonstrations), which gives the largest gain per GPU-hour, and do those gains survive a control that spends the same compute on repeated sampling?

| ID | Hypothesis | Refuted if |
|---|---|---|
| H1 (primary) | The fine-tuned agent has lower task-averaged error than the direct score predictor | The 95% interval for the difference includes zero or favors the direct predictor |
| H2 | The agent returns a usable score for more cases than reconstruction followed by the rules | Its fallback rate is not lower |
| H3 | Tools add value beyond feature supervision | The agent does not beat the same model fine-tuned to output features from video without tools |
| H4 | The agent's own choices add value beyond the tools | The agent does not beat both the expert pipeline and the tool-feature regressor |
| H5 (exploratory) | Prompt and harness search add value beyond repeated sampling | Neither beats best-of-n sampling at the same budget |

**What the study would establish.** Results on visual question answering show that composing tools through generated programs can help a model answer questions about images. This study asks the corresponding question for measurement against a physical reference, where the answer has a known correct value, and the comparisons behind H3 and H4 locate which part of the agent's design carries any benefit. A negative result on H4 would also be informative: it would mean that, for measurement tasks whose analysis is already defined, a carefully written pipeline captures what the agent adds.

## 3. Related work

**VLMs for movement assessment.** Knowledge-augmented prompt tuning for gait ([Wang et al., 2024](https://arxiv.org/abs/2403.13756)), [BioGait-VLM](https://arxiv.org/abs/2603.08564), [MyoMechanix](https://arxiv.org/abs/2608.26094) and [BiomechGPT](https://arxiv.org/abs/2505.18465) map video, skeletons or motion tokens to labels, scores or coaching feedback. None of them calls measurement tools at inference.

**Agents for biomedical analysis.** [Biomni](https://doi.org/10.1101/2025.05.30.656746) gives a language-model agent a large set of biomedical tools, and BiomechAgent writes analysis code over processed motion-capture data. Both start from processed data, and neither trains the model.

**Visual programming.** VisProg and ViperGPT generate programs that call vision modules and report gains over end-to-end models on visual reasoning benchmarks. Their targets are answers to questions. Here the target is a physical quantity with a reference value, which turns the comparison with end-to-end prediction into a quantitative one.

**Monocular reconstruction.** [OpenCap Monocular](https://arxiv.org/abs/2603.24733) refines WHAM and ViTPose estimates and fits a full-body OpenSim musculoskeletal model, and it has been validated against marker-based motion capture for walking, squatting and sit-to-stand. It is both one of the agent's tools and the core of the reconstruction baseline.

**Improving harnesses without training.** [GEPA](https://arxiv.org/abs/2507.19457) rewrites prompts using feedback from runs, [Meta-Harness](https://arxiv.org/abs/2603.28052) searches over harness code with access to earlier candidates and their traces, and [VidHarness](https://arxiv.org/abs/2609.38413) applies harness search to long video. A re-evaluation of harness evolution ([Wang et al., 2026](https://arxiv.org/abs/2607.12227)) found that such gains often disappear against budget-matched repeated sampling and on held-out tasks, which is why H5 includes that control.

## 4. Approach

### 4.1 The agent and its tools

The agent receives the Cam0 video, the task description and the task's feature definitions with units. Large arrays stay inside a Python sandbox and the model receives short summaries or plots, so its context stays small and no data are truncated. Every signal is indexed by time in seconds from the original video, because hold times and speeds depend on true time.

| Tool | Returns | Arguments the agent may choose |
|---|---|---|
| `frames` | Timestamped frames or crops | Window, rate, crop |
| `pose2d` | 2D landmarks per frame (RTMPose or a second pose model) | Model |
| `segment_person` | The person's outline per frame (SAM 2.1) | None |
| `track_points` | Point tracks (CoTracker3) | One of 16 body regions |
| `reconstruct3d` | Joint angles and center of mass (OpenCap Monocular) | One of two settings |
| `plot`, `python` | An image of a signal; code execution | Free |
| `submit` | Features with provenance | Ends the trajectory |

Every reachable call to an expensive tool is computed once and stored under the video, tool version and full argument list, and a request outside the menu returns an error message. Repeated runs therefore cost only model inference and sandbox time, and every trajectory can be replayed step for step.

### 4.2 What the agent returns

For each feature the agent submits a value in physical units together with the sandbox cell that computed it, the tool outputs that cell read, and the time window it used. The harness re-runs the cell on the cited outputs and requires the same value, so every reported number is reproducible from its evidence. Code then applies the task's rescaling and averaging; the model never writes the score.

### 4.3 Methods compared

| Group | Method | What it isolates |
|---|---|---|
| Reference points | Constant task mean; reconstruction followed by StaBLE's released scoring code | Ignoring the video; the classical pipeline |
| Direct prediction | Qwen3-VL-8B fine-tuned with low-rank adapters to output task scores from frames | The end-to-end alternative (primary comparator) |
| Feature supervision without tools | The same model fine-tuned to output features from frames, scored by the formula | Feature labels without tools (H3) |
| Same tools, no agent | Expert pipeline: fixed calls, hand-tuned fallbacks (for example, 2D pose for timing features when 3D reconstruction fails) and released feature code. Tool-feature regressor: gradient-boosted trees on summaries of fixed tool outputs, trained on feature labels | Tools and labels without adaptive choices (H4) |
| Agent | Frozen; prompts optimized with GEPA; harness search; fine-tuned on verified demonstrations (primary) | The agent route and three ways of improving it |

**Demonstrations for fine-tuning.** A larger frozen model (Qwen3-VL-235B-A22B) runs the same harness eight times on each training video. A trajectory is kept if every feature replays and its mean feature error against the reference, in score units (Section 6), is below a threshold fixed before generation. At most 40 trajectories are kept per task, and the counts per task and per ability quintile are reported, because easy tasks yield more accepted trajectories. The 8B agent is then fine-tuned on the kept trajectories with low-rank adapters.

**Budget-matched improvement (secondary).** Prompt optimization, harness search and fine-tuning are each run at three development budgets (50, 200 and 800 H100-hours), counting proposer models, demonstration generation, training and inference. Each search run may evaluate on the validation fold at most 20 times, and those evaluations are charged to its budget. The control for H5 is best-of-n sampling of the frozen agent at the same budget, selecting the median of the n submitted feature sets, a rule that uses no labels.

## 5. Data, splits and leakage

**Dataset.** StaBLE contains 180 adults aged 18 to 87, from people with vestibular disorders to competitive athletes and dancers, each recorded performing up to 18 balance tasks with three smartphones. A three-camera OpenCap reconstruction of every trial provides the reference: 76 features, 18 task scores and an overall StaBLE score. The study uses one camera (Cam0) as input. Of the 180 participants, 171 have usable single-camera video.

**Ledger.** Before any experiment, a ledger lists every recorded trial (3,322), linking its Cam0 video to its reference features, participant and task; StaBLE's released code defines how repeated or two-sided trials combine. Each row carries a status. Measured trials are used everywhere. Thirty trials flagged for reconstruction error and three whose features were imputed are kept as inputs but excluded from training targets and from the primary evaluation. Ninety-eight tasks not attempted for safety have no video and enter only the overall StaBLE score, as zeros, as StaBLE defines it. Every reported number states how many ledger rows it covers.

**Splits.** Sixty participants are set aside before any analysis, stratified by StaBLE score quintile, age group and athlete status, and drawn from people who were never in the lab pilot's test set. The pilot trained models on some of them, so this is a retrospective re-split: prior use is documented, every baseline is retrained without them, and confirmation on newly recorded participants is the natural follow-up. The other 111 participants form five development folds, stratified the same way and checked against the whole (Kolmogorov–Smirnov tests and standardized mean differences below 0.1). All of a person's trials stay in one fold, and the sealed set is evaluated once, after every method is frozen.

**Leakage.** StaBLE rescales each feature to 0–1 using its minimum and maximum over all 180 participants, which would let test participants shape the scale. Endpoints are therefore refitted on the training folds of each split, and on all 111 development participants for final models, and sealed values outside 0–1 are kept unclipped. Fallback means, demonstrations, prompt examples and search feedback also come only from training folds. Seven participants appear in StaBLE's public exemplar video, and results are reported with and without any of them in the sealed set. StaBLE's feature definitions were designed on all 180 people and are treated as part of the measuring instrument.

**Keeping the data's shape.** Fine-tuning data are drawn from ledger rows with equal probability per row, and the demonstration filter's tilt toward easy tasks is corrected by reweighting any task whose share of kept examples differs from its ledger share by more than a quarter. Evaluation always covers every eligible sealed trial.

## 6. Evaluation and statistics

**Outcomes.** Task-averaged absolute error is primary: the mean absolute score error within each task, averaged over tasks with equal weight. Each method's fallback rate is reported beside it. For methods that produce features, feature error is reported in physical units and in **score units**, the absolute difference between the submitted and reference values after both are rescaled with training endpoints, because a correct score can hide two wrong features. Per-task error and compute per video, split into first-use and cached costs, are secondary.

**Failure rule.** When a method gives no usable output for a trial (a failed tool, a malformed answer, a time limit), that task score is the training-fold mean and is counted as a fallback. Every method is therefore scored on every eligible sealed trial. A sensitivity analysis repeats each comparison on the trials both methods completed, as a diagnostic.

**Unit of analysis.** Participants, because one person's tasks are correlated. Every interval comes from resampling participants with all their trials and recomputing the estimator from scratch.

**Training runs.** A lucky training run shifts every participant at once, and resampling participants cannot average that away. Claims about a training method therefore target the expected improvement over retraining, estimated from five paired seeds for each fine-tuned method (the agent, the direct score predictor and the direct feature predictor). The interval combines the spread between paired seed differences with the participant-bootstrap spread of the seed-averaged difference, using a t-distribution with Satterthwaite degrees of freedom. Its coverage is checked by simulation before training, under symmetric, skewed and failed-run seed distributions.

**Decision rules.** H1 succeeds if the upper 95% bound for the agent-minus-direct error difference is below zero. H2–H4 form one family under Holm's correction. H5 is exploratory and is reported as accuracy-versus-cost curves. Before training, power for a 0.01 difference in task-averaged error is estimated by resampling cross-validated development predictions of existing methods; if it falls below 60%, results are reported as estimates without confirmatory claims.

## 7. Scope and cost

| Item | H100-hours (estimate) |
|---|---|
| Tool cache, computed once | 400 |
| Baselines and regressors across five folds | 150 |
| Frozen agent, prompt optimization and harness search at three budgets | 450 |
| Demonstration generation | 250 |
| Fine-tuning: agent and two direct predictors, five seeds each | 200 |
| Sealed evaluation | 50 |
| **Total** | **about 1,500** |

The estimates are replaced by throughput measured on 50 videos before any other work begins. The study involves no reinforcement learning, which keeps it within a single lab's resources.

## 8. Risks and what each outcome would mean

If the agent relies on monocular reconstruction for every task, it inherits that tool's failures; the 2D pose and point-tracking routes give it cheaper alternatives for timing features, and the fallback rate shows whether it uses them. If the direct feature predictor matches the agent, tools add nothing beyond feature supervision in this setting. If the expert pipeline or the regressor matches the agent, the value lies in the tools and the feature definitions, and an agent is not needed for tasks whose analysis is already known. A win on H1, H3 and H4 together would support learned, tool-based analysis as a route to inspectable single-camera measurement.

The three-camera reconstruction is itself an estimate, and it shares its body model and inverse-kinematics step with the monocular tool. Agreement with it therefore supports the reproduction of StaBLE's measurements; agreement with laboratory motion capture or with clinical outcomes is a separate question.
