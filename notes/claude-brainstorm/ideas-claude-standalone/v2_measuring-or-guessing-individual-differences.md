# Measuring or Guessing? Testing Whether Video-Based Balance Scores Preserve the Differences Between People

## Abstract

A balance score computed from one smartphone video is useful only if it reflects the person in that video. A model can reach a respectable average error by predicting values close to the population's typical score, and on a recent balance dataset a constant guess comes within a sixth of the best learned model. Average error cannot tell a model that measures from one that pulls its answers toward the mean, and age, which can be read from appearance, already predicts much of the score. This proposal defines an evaluation that separates these cases, using within-task rank agreement, skill against the constant guess, the calibration slope, accuracy at the clinical extremes, appearance-only controls, video swaps and independent clinical scales. It applies the evaluation to one central comparison: do balance scores built from tool-derived biomechanical features preserve differences between people better than direct video-to-score prediction? It also tests a specific explanation for a pilot observation, that fine-tuning lowered average error while worsening performance at the extremes: the fine-tuned model may simply shrink its predictions toward the average.

## 1. Motivation

### 1.1 From video to a balance score

In the StaBLE "rise to toes" task ([Heigold et al., 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13621976/)), a person rises onto their toes as quickly and as high as they can and holds for five seconds. Three numbers describe the performance: the peak upward speed of the **center of mass** (the average position of the body's mass), the peak ankle angle, and the time the center of mass stays high. Each such number, a **feature**, is rescaled to a 0-to-1 range using the lowest and highest values in the data, and the rescaled values are averaged into a **task score**. StaBLE defines 76 features over 18 tasks, recorded from 180 adults with three smartphones, and averages the task scores into one balance score. The practical aim is to obtain these scores from a single phone.

### 1.2 Why a small error can hide a method that ignores the video

Consider five people whose true task scores are 0.4, 0.5, 0.6, 0.7 and 0.8.

| Predictor | Predictions | Mean absolute error | Rank agreement | Slope |
|---|---|---|---|---|
| Constant guess | 0.6 for everyone | 0.120 | none | 0 |
| Shrunk but ordered | 0.56, 0.58, 0.60, 0.62, 0.64 | 0.096 | perfect | 0.2 |
| Noisy but measuring | 0.50, 0.45, 0.70, 0.60, 0.85 | 0.080 | 0.8 | 0.85 |

The second predictor beats the constant on error while compressing every difference between people to a fifth of its true size; the third has a similar error but keeps most of the spread. Three measures separate these cases. **Rank agreement** is the Spearman correlation between predicted and reference scores within a task: it asks whether the method puts people in the right order, which is also how StaBLE validates its score against clinical scales. The **skill score** is one minus the ratio of a method's error to the constant guess's error, so zero means no better than ignoring the video. The **calibration slope** is the slope of a straight-line fit of predicted scores on reference scores. Fitting in this direction has a useful property: independent noise in the predictions leaves the slope near one, while shrinkage toward the mean pulls it toward zero.

### 1.3 Three ways to look accurate without measuring

The first is **regression toward the mean**. A model that is uncertain about a person can lower its expected error by moving its answer toward the population's center, and average error rewards this. In clinical prediction the calibration slope is the standard diagnostic for it ([Van Calster et al., 2019](https://doi.org/10.1186/s12916-019-1466-7)).

The second is **appearance**. The StaBLE score correlates −0.76 with age, so a model can order people well by how old they look. Models that solve a task through such correlated cues instead of the intended signal are a familiar problem in machine learning ([Geirhos et al., 2020](https://arxiv.org/abs/2004.07780)), and many video benchmarks can be solved from a single frame ([Buch et al., 2022](https://arxiv.org/abs/2206.01720)).

The third is **insensitivity to the recording**. A model may return a score that suits the typical person of a given appearance — a plausible score for someone who looks like this — without responding to how this particular person moved. Swapping in another person's video exposes this.

### 1.4 The pilot observation this study can explain

A pilot in the lab, on single-camera StaBLE videos of 43 held-out participants, found task-averaged errors of 0.120 for the constant guess and 0.100 for a fine-tuned Qwen3-VL-8B, and noted that fine-tuning improved average error while lowering performance on clinical extremes. Shrinkage predicts this pattern. If a model's predictions follow `a + s·y` for a reference score `y` with slope `s < 1`, its error for a person whose score lies a distance `d` from the mean is about `(1 − s)·d`, which grows toward both extremes. If shrinkage explains the pilot result, the remedy lies in what a model measures; if it does not, something else, such as failures specific to unusual movement, is at work.

## 2. Research question and hypotheses

> **Research question.** Do balance scores computed from tool-derived biomechanical features preserve the differences between people (their ordering, the size of their differences, and accuracy at the extremes) better than direct video-to-score prediction, beyond what age, sex and a single frame already predict?

**Second question.** Is the direct predictor's loss of accuracy at the extremes explained by uniform shrinkage toward the average?

| ID | Hypothesis | Refuted if |
|---|---|---|
| H1 | Most of the direct predictor's improvement over the constant guess comes from shrinkage | Its median calibration slope is above 0.8 |
| H2 (primary) | The feature-based agent has higher mean within-task rank agreement than the direct predictor, without lower skill | The interval for the rank-agreement difference includes zero, or the lower bound of the skill difference is below −0.02 |
| H3 | The direct predictor's excess error at the extremes is what its calibration predicts | The error left unexplained by its fitted slope and intercept has an interval above zero |
| H4 | The agent's ordering of people is not explained by appearance | Its age-adjusted rank agreement falls to the demographic model's, or the single-frame model matches it |
| H5 | The agent responds to the recording | Its predictions track the reference of a swapped-in video no better than the direct predictor's |
| H6 | The agent's overall score relates to independent clinical measures about as strongly as the three-camera score does | Its correlation with the balance-confidence scale is significantly lower than the reference score's |

**What the study would establish.** The evaluation applies wherever a model is meant to replace a measuring instrument: clinical scores from video, laboratory assays from images, physical quantities from cheaper sensors. In each case average error can reward a model for regressing toward the population, and a protocol that diagnoses this, controls for appearance and anchors results to independent measures is useful beyond balance. The comparison itself tests whether forcing a model to compute defined physical features is one way to avoid the problem.

## 3. Related work

**Calibration of clinical prediction models.** The calibration slope and intercept are standard checks of whether predicted risks or scores spread as widely as outcomes do ([Van Calster et al., 2019](https://doi.org/10.1186/s12916-019-1466-7)). Machine-learning work on video-based assessment usually reports error and correlation without them.

**Shortcuts and single-frame solutions.** Shortcut learning ([Geirhos et al., 2020](https://arxiv.org/abs/2004.07780)) describes models that succeed on benchmarks through unintended cues. An atemporal probe showed that many video-language tasks can be solved from one frame ([Buch et al., 2022](https://arxiv.org/abs/2206.01720)), which motivates the single-frame control.

**VLMs for movement assessment.** Knowledge-augmented gait VLMs ([Wang et al., 2024](https://arxiv.org/abs/2403.13756)), [BioGait-VLM](https://arxiv.org/abs/2603.08564) and [MyoMechanix](https://arxiv.org/abs/2608.26094) report accuracy or agreement on labels, but not whether predictions preserve individual differences or exceed demographic baselines.

**Tool-based analysis.** [BiomechAgent](https://arxiv.org/abs/2602.06975) shows that a code-writing agent benefits from validated biomechanics tools, and [OpenCap Monocular](https://arxiv.org/abs/2603.24733) reconstructs musculoskeletal kinematics from a single smartphone video. Neither addresses whether feature-based estimates preserve differences between people better than direct prediction.

## 4. Methods compared

**The feature-based agent.** A tool-calling vision-language model (Qwen3-VL-8B) receives the Cam0 video, the task description and the feature definitions with units. Its tools are timestamped frames and crops, 2D landmarks (RTMPose or a second pose model), person segmentation (SAM 2.1), point tracks (CoTracker3) for 16 body regions, 3D joint angles and center of mass (OpenCap Monocular), plotting and a Python sandbox, with expensive outputs computed once and cached. For each feature it submits a value in physical units and the code that computed it, which the harness re-runs to confirm the value; the task's fixed formula then gives the score. The agent is fine-tuned with low-rank adapters on demonstrations from a larger frozen model (Qwen3-VL-235B-A22B), kept only when every feature replays and the mean feature error is below a preset threshold, with at most 40 per task.

| Group | Method | Role |
|---|---|---|
| No movement information | Constant task mean; demographic model (ridge regression from age and sex to each task score) | What can be predicted without observing movement |
| Appearance only | The direct predictor given one middle frame | What a single image reveals |
| Direct prediction | Qwen3-VL-8B fine-tuned on task scores (primary comparator); 2D pose with a temporal network | The end-to-end route |
| Feature-based | Expert pipeline with fixed tool calls and StaBLE's released feature code; regressor trained on fixed tool outputs and feature labels; the fine-tuned agent (primary) | Whether features computed from movement preserve differences, with and without adaptive tool use |

## 5. Data, splits and leakage

**Dataset.** StaBLE contains 180 adults aged 18 to 87, from people with vestibular disorders to competitive athletes and dancers, each recorded performing up to 18 balance tasks with three smartphones. A three-camera OpenCap reconstruction of every trial provides the reference features, task scores and overall score. The study uses one camera (Cam0) as input. Of the 180 participants, 171 have usable single-camera video. The release also includes self-reported balance confidence and fall history, and the StaBLE score correlates with the Activities-Specific Balance Confidence scale (ρ = 0.60) and the 4-Stage Balance Test (τ = 0.55); these measures do not depend on OpenCap and serve as independent anchors.

**Ledger.** One row per recorded trial (3,322) links its Cam0 video to its reference features, participant and task, with StaBLE's released code deciding how repeated or two-sided trials combine. Measured trials are used everywhere. Thirty trials flagged for reconstruction error and three with imputed features are excluded from training targets and the primary evaluation. Ninety-eight tasks not attempted for safety have no video and enter only the overall score, as zeros, as StaBLE defines it.

**Splits.** Sixty participants are set aside before any analysis, stratified by StaBLE score quintile, age group and athlete status, and drawn from people who were never in the lab pilot's test set. The pilot trained models on some of them, so this is a retrospective re-split: prior use is documented, every baseline is retrained without them, and confirmation on newly recorded participants is the natural follow-up. The other 111 participants form five stratified development folds, checked against the whole (Kolmogorov–Smirnov tests and standardized mean differences below 0.1). All of a person's trials stay in one fold, and the sealed set is opened once.

**Leakage.** Rescaling endpoints, which StaBLE computes over all 180 participants, are refitted on training folds, and sealed values outside 0–1 are kept unclipped. The thresholds that define the extremes (Section 6) come from development participants. Fallback means, demonstrations and the demographic model are fitted on training folds only. Seven participants appear in StaBLE's public exemplar video; results are reported with and without them.

**Keeping the data's shape.** Fine-tuning examples are drawn with equal probability per ledger row, and any task whose share of kept demonstrations differs from its ledger share by more than a quarter is reweighted. Every eligible sealed trial is evaluated for every method.

## 6. Evaluation

**Core measures**, each computed within a task and then averaged over tasks with equal weight:

- *Rank agreement*: Spearman correlation between predicted and reference scores. Ties use average ranks, constant predictions receive zero, and a task whose references are constant in a bootstrap replicate is excluded for every method alike.
- *Skill*: `1 − MAE_t / MAE_t(constant)`; a task with zero constant-guess error is excluded for every method.
- *Calibration slope and intercept*: from a least-squares fit of predictions on references; the median slope across tasks is reported.
- *Absolute error*, for completeness.

**The extremes.** For each task, sealed trials whose reference score lies below the development 10th percentile or above the 90th are the extremes. For each method, the shrinkage-predicted error of a trial is `|a + s·y − y|`, using the method's slope `s` and intercept `a` fitted on the middle 80% of trials. The unexplained extreme error is the observed mean absolute error at the extremes minus the mean shrinkage-predicted error there; H3 holds if its interval includes zero.

**Appearance.** The demographic and single-frame models set the level reachable without movement. Age-adjusted rank agreement removes the rank-linear effect of age from both predictions and references before correlating them.

**Video swap.** Each sealed video is replaced by another sealed participant's video of the same task, together with the camera parameters and body dimensions that reconstruction needs, so the tools run validly. Input dependence is the Spearman correlation, across swaps, between the change in a method's prediction and the change in reference score. Appearance changes with the video as well, so this diagnostic complements the appearance controls without isolating movement.

**Independent anchors.** Each method's overall score (the average of its predicted task scores, with not-attempted tasks as zero) is correlated with balance confidence and the 4-Stage Balance Test where these are available, and the difference from the reference score's correlation is bootstrapped over participants.

**Failure rule.** A trial without a usable output receives the training-fold task mean and is counted as a fallback. Fallback rates are reported beside each result, and comparisons are repeated on trials completed by both methods as a diagnostic.

## 7. Statistics

**Unit.** Participants. Every interval resamples participants with all their trials and recomputes the measure from scratch.

**Training runs.** The agent and the direct predictor are each fine-tuned with five paired seeds. Method-level claims target the expected improvement over retraining, with an interval that combines the spread between paired seed differences and the participant-bootstrap spread of the seed-averaged difference (t-distribution, Satterthwaite degrees of freedom), and with its coverage checked by simulation before training.

**Decision rules.** H2 is primary and uses the rule stated in its row. H3 to H6 form one family under Holm's correction. H1 is reported as an estimate with its interval. Before training, power for a 0.05 gain in rank agreement with 60 participants is estimated by resampling development predictions of existing methods; if it falls below 60%, results are reported as estimates without confirmatory claims.

## 8. Scope and cost

Most of the work is evaluation. The tool cache (about 400 H100-hours, dominated by monocular reconstruction at about four GPU-minutes per 17-second clip) is computed once and also covers the video swaps, since every sealed video is already cached. Demonstration generation (about 250 H100-hours), fine-tuning of the agent and the direct predictor with five seeds each (about 150), baselines across folds (about 100) and evaluation (about 50) bring the total to roughly 950 H100-hours.

## 9. What each outcome would mean

If the direct predictor's slope is high (H1 refuted), its gain over the constant reflects real measurement, and rank agreement becomes a secondary outcome. If the agent orders people better but its predictions are compressed, the conclusion is narrower: it identifies relative performance but understates its magnitude, which matters for any use that compares a person with a clinical threshold. If the appearance controls perform about as well as the agent, the contribution of movement remains uncertain, however good the ranking looks. If shrinkage explains the extreme-decile errors, the pilot's observation needs no special explanation beyond regression toward the mean, and methods should be judged by their slope as well as their error.

All of these results concern agreement with a reconstructed reference across people at one visit. The clinical anchors give a partial independent check, but detecting change within one person over time needs repeated recordings that this dataset does not contain.
