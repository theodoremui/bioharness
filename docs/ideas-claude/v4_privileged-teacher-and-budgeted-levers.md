# Seeing More While Learning, Seeing Less When Tested: Privileged Training of Tool-Calling Video Agents for Balance Assessment

*Version 4. Changes from v3: the three-camera reconstruction now also drives a privileged teacher that writes demonstrations the single-camera student can follow; verification requires a material response on probe videos; every improvement method is compared at fixed compute budgets with continuation controls; demographic, single-frame and motion-perturbation controls test whether the agent measures movement or reads appearance; and the project is laid out as a sequence of stages with decision gates.*

## Abstract

Smartphone video could make balance testing routine, but a score computed from one camera is only trustworthy if it measures the person's movement. On the StaBLE balance dataset, a constant guess comes close to the best learned model, and the score correlates strongly with age, so a model can look accurate while measuring little. We study a vision-language agent that calls pose, segmentation and reconstruction tools, writes code that computes each task's defined features, and passes them to a fixed scoring formula. Our approach uses a three-camera reconstruction that exists only during training in two ways: as a per-feature reward, credited only when the harness can re-run the agent's code on the cited evidence, and as extra context for a teacher whose demonstrations use only the tools the single-camera student has. We will compare this approach with outcome-only reinforcement learning, prompt and harness optimization, and learned predictors that see the same tool outputs, at matched compute and on participants sealed until the end. The study asks whether privileged, verified supervision produces agents that rank unseen people more accurately than outcome-only training, and whether that advantage reflects measured movement rather than appearance.

## 1. Motivation

A video-based balance measurement runs through four stages: a pose model finds body landmarks; a reconstruction step builds a 3D skeleton whose joint angles and **center of mass** (the average position of the body's mass) change over time; a feature step reduces those curves to the quantities the task asks for, such as the peak upward speed of the center of mass when rising onto the toes; and a scoring step rescales and averages the features. StaBLE ([Heigold et al., 2026](https://doi.org/10.64898/2026.09.16.750744)) defines 76 such features over 18 tasks recorded from 180 adults.

The lab's pilot on single-camera videos showed two failure modes. Rebuilding the skeleton with OpenCap Monocular and applying StaBLE's rules gave valid scores for only 567 of 729 test cases, and took about four GPU-minutes per 17-second clip. Learned predictors always answered, but the best (a fine-tuned Qwen3-VL-8B, error 0.100) improved on predicting each task's average (0.120) by about a sixth, and the same model without fine-tuning (0.238) did worse than the average.

Error alone can hide a method that ignores the video. For five people with true scores 0.4 to 0.8, a constant guess of 0.6 has error 0.120; a predictor that keeps the order but shrinks every difference to a fifth has error 0.096; a noisy predictor that measures has error 0.080. We therefore also report **rank agreement** (within-task Spearman correlation), **skill** (one minus the ratio of a method's error to the constant's), and the **calibration slope** (near one when differences between people survive, near zero when predictions collapse to the average). A second trap is appearance: the StaBLE score correlates −0.76 with age, so a model can rank people by how old they look. Section 8.3 adds controls for this.

## 2. Concepts from first principles

**Vision-language model (VLM).** A neural network that takes images or video frames with text and produces text; here Qwen3-VL-8B ([report](https://arxiv.org/abs/2511.21631)).

**Tool call, harness, agent, trajectory.** A tool call is a structured request in the model's output that software executes and answers. The harness is that software: tool descriptions, the loop that runs calls, the record of earlier steps, and a stopping rule. The model and harness acting over several steps are an agent; one run from video to final answer is a trajectory.

**Supervised fine-tuning (SFT).** Adjust the model's weights so that example trajectories become more probable. It imitates its examples and cannot improve on them.

**Reinforcement learning (RL) and GRPO.** The model generates its own trajectories, a reward function scores them, and the weights move toward higher-reward trajectories. Group relative policy optimization ([Shao et al., 2024](https://arxiv.org/abs/2402.03300)) samples several trajectories for the same video and compares each with the group average.

**Outcome-only rewards and shortcuts.** If only the final score is rewarded, a trajectory that outputs a typical value without measuring anything can score well. Outcome-only RL can make video models stop using the video ([Xu, 2026](https://arxiv.org/abs/2606.22043)), and RL-trained tool agents skip verification more often ([Thaman, 2026](https://arxiv.org/abs/2605.02964)). Averaging also lets opposite feature errors cancel.

**Privileged information.** Information available during training but not at test time. Here, the three-camera reconstruction. A model trained to imitate a teacher that sees privileged information can fail if the teacher's choices depend on what the student cannot see, a gap described in recent distillation work ([Penaloza et al., 2026](https://arxiv.org/abs/2602.04942)).

## 3. Research question and hypotheses

**Primary question.** By the ICML 2027 submission deadline (expected late January 2027), does a Qwen3-VL-8B tool-calling agent trained with privileged, verified supervision (a privileged-teacher warm start followed by GRPO with per-feature verified rewards) achieve higher mean within-task rank agreement on a sealed set of 43 held-out participants than the same agent trained from the same base model, under the same compute budget, with a non-privileged warm start and a final-score reward?

**Secondary questions** (one Holm-corrected family): (S1) Does the privileged agent match or exceed the fine-tuned direct predictor, the expert pipeline, and a tool-feature regressor trained on the same cached outputs and labels? (S2) Which component carries the gain: the teacher, the per-feature reward, or verification? (S3) Does rank agreement survive adjustment for age? (S4) What share of the agent's features are verified on sealed participants?

| ID | Hypothesis | Refuted if |
|---|---|---|
| H1 | Score-only RL shrinks predictions toward the average | Its development calibration slope stays within 0.1 of the warm-start model's |
| H2 | Per-feature verified rewards beat score-only rewards | Crossed-bootstrap interval for the rank-agreement difference includes zero |
| H3 | Verification is what blocks the shortcut | Removing verification changes neither rank agreement nor slope |
| H4 | The privileged teacher gives a better warm start than a non-privileged one | No development difference after warm start, or the gap closes after RL |
| H5 | The agent measures movement | Age-adjusted rank agreement falls to the demographic baseline's, or motion perturbation leaves outputs unchanged |

## 4. Related work

**Movement-analysis VLMs and agents.** Gait VLMs with knowledge augmentation ([Wang et al., 2024](https://arxiv.org/abs/2403.13756)), [BioGait-VLM](https://arxiv.org/abs/2603.08564) and [MyoMechanix](https://arxiv.org/abs/2608.26094) learn direct mappings; [BiomechAgent](https://arxiv.org/abs/2602.06975) writes analysis code over processed data without training the model.

**RL for tool use.** [DeepEyes](https://arxiv.org/abs/2505.14362), [LongVT](https://arxiv.org/abs/2511.20785) and [VITAL](https://arxiv.org/abs/2508.04416) learn visual tool use from outcome rewards on question answering; [ToolRL](https://arxiv.org/abs/2504.13958) refines rewards on tool names and arguments.

**Privileged supervision.** π-Distill and on-policy self-distillation ([Penaloza et al., 2026](https://arxiv.org/abs/2602.04942)) train a student from a teacher conditioned on privileged information. Our teacher's privilege is a physical measurement, and its action space is restricted to the student's, so the remaining gap is in what each can observe.

**Prompt and harness optimization.** [GEPA](https://arxiv.org/abs/2507.19457), [Meta-Harness](https://arxiv.org/abs/2603.28052) and [VidHarness](https://arxiv.org/abs/2609.38413) change prompts or harness code without changing weights; [Wang et al. (2026)](https://arxiv.org/abs/2607.12227) show that these gains often vanish against matched test-time scaling and on held-out tasks.

## 5. Method

### 5.1 Agent and harness

The agent receives the Cam0 video, the task description and the feature definitions with units. Large arrays stay in a Python sandbox; the model sees short summaries or plots. All signals carry timestamps in seconds from the original video.

| Tool | Returns | Arguments the agent may choose |
|---|---|---|
| `frames` | Timestamped frames or crops | Window, rate, crop (live) |
| `pose2d` | 2D landmarks (RTMPose, or a second pose model) | Model (cached) |
| `segment_person` | Person outline (SAM 2.1) | None (cached) |
| `track_points` | Point tracks (CoTracker3) | One of 16 body regions (cached) |
| `reconstruct3d` | Joint angles and center of mass (OpenCap Monocular) | One of two settings (cached) |
| `plot`, `python` | An image of a signal; code execution | Live |
| `submit` | Features with provenance | Ends the trajectory |

### 5.2 Cached environment

Every reachable cached call is computed once and stored under (video, tool version, full arguments). A request outside the menu returns an error message. Rollouts therefore cost model inference and sandbox time only, and every trajectory can be replayed exactly.

### 5.3 Submissions and verification

Feature code must be written as a function of tool outputs and a small set of named **annotations** (for example `task_start`, `task_end`), which the agent may set by inspecting frames. For each feature the agent submits the value, the function, the cited tool outputs and its annotations. The harness checks:

1. **Replay.** Re-running the function on the cited outputs and annotations reproduces the value (relative tolerance 10⁻⁶).
2. **Material response.** Two probe videos of the same task are chosen from the training folds, with reference values near the 10th and 90th percentiles of that feature. The function is run on their cached outputs, with annotations taken from the expert pipeline's segmentation of those probes. The two results must differ by at least a quarter of the feature's training interquartile range. A constant, or a constant plus a negligible term, fails.
3. **Range.** The value lies within the training range widened by half its width on each side.

Verification needs no reference value for the video being analysed, so it runs identically on sealed participants.

### 5.4 Rewards

Let task `t` have `k` features with training-fold endpoints `L_f`, `U_f`, and define the rescaled feature `n_f(x) = (x − L_f)/(U_f − L_f)` (reversed when lower is better). With reference `x*_f` and submitted `x̂_f`, the feature error in score units is `e_f = |n_f(x̂_f) − n_f(x*_f)|`; set `ẽ_f = min(e_f, 1)` if verified and `ẽ_f = 1` otherwise.

- **Measurement reward:** `R_meas = −(1/k) Σ_f ẽ_f`.
- **Score-only reward (control):** `R_score = −|Ŝ − S*|`.
- **Format penalty:** −1 for an unparseable submission.
- **Cost term (secondary arm only):** `−λ` times tool GPU-seconds divided by the clip's duration.

For verified features the score error never exceeds the measurement penalty (triangle inequality), so a small penalty guarantees a small score error, while a small score error can hide cancelling feature errors. Imputed (3 trials) and reconstruction-flagged (30 trials) references are masked from rewards.

### 5.5 Privileged teacher

The teacher is a larger frozen model (Qwen3-VL-235B-A22B) running the same harness with the same tools, plus a read-only **reference panel** that shows the three-camera joint-angle and center-of-mass curves and the reference feature values for the training video. It may use the panel to diagnose where the monocular tools went wrong (a missed reach, a mistimed start) but it can act only through the student's tools, and its submission is verified like the student's, so it cannot copy reference numbers into its answer. Two filters keep demonstrations that the student can follow:

- **Cross-video validity.** The teacher's final feature functions are run on five other training videos of the same task (with expert-pipeline annotations) and must keep their error below the expert pipeline's on those videos. A function tuned to one video using privileged hindsight fails this test.
- **Observation stripping.** The panel and any text that quotes it are removed before the trajectory is used for SFT. Trajectories whose remaining reasoning refers to panel content are discarded.

The **non-privileged warm start** uses the same teacher model without the panel, with the same filters and the same number of attempts. Comparing the two isolates the value of the panel (H4).

### 5.6 Training loop

1. Generate eight teacher attempts per training video; keep filtered trajectories, at most 40 per task.
2. Fine-tune Qwen3-VL-8B with low-rank adapters on the kept trajectories.
3. Run GRPO: eight trajectories per video, advantages normalized within each group, groups with identical rewards skipped as in [DAPO](https://arxiv.org/abs/2503.14476).

### 5.7 Keeping the data in its original shape

Samplers draw ledger rows from the training folds with equal probability, so task, age and ability mixtures match the data. Teacher filtering and skipped GRPO groups can tilt this mix; we log update shares per task and per ability quintile and reweight any task whose share drifts by more than 25% (relative) from the ledger. Evaluation always covers every eligible sealed row.

## 6. Data, splits and leakage control

**Ledger.** One row per recorded trial (3,322), linked to its Cam0 video, its reference features and its participant–task slot, with StaBLE's released code defining how repeated or bilateral trials aggregate into a task example. Each row carries a status (*measured*, *assigned zero* for 98 safety non-attempts, *imputed* for 3 failed trials, *flagged* for 30 trials with reconstruction error, *excluded* with a reason). Assigned and imputed values never count as measurements. We document why 9 of 180 participants were excluded from the lab's pilot and check that they do not differ in age or ability.

**Sealed confirmatory set.** The lab's 43 previous test participants have already informed this design, so they join development. Forty-three participants who have never been evaluated by anyone are drawn, stratified by StaBLE quintile, age group and elite-athlete status, and stored separately until every method is frozen. The remaining 128 form five stratified development folds, with each fold's task-score distributions checked against the whole (Kolmogorov–Smirnov tests and standardized differences below 0.1).

**Everything fitted per fold.** Normalization endpoints, fallback means, probe videos, teacher demonstrations, prompt examples and harness-search feedback come only from the training folds of each split; final models use all 128 development participants.

**Other leaks.** Seven participants appear in StaBLE's public exemplar video; we report results with and without any in the sealed set. StaBLE's features were designed on all 180 participants; we treat the definitions as part of the instrument and say so.

## 7. The research journey: stages and gates

Each stage is tested on development folds only, and each has a gate that decides the next step. The sealed set is opened once, after Stage 6.

| Stage | Question | Data and leakage guard | Gate |
|---|---|---|---|
| 0. Groundwork | Is the protocol sound and powered? | Ledger, sealed split, per-fold fitting, cache, expert pipeline | If simulated power for a 0.05 rank-agreement gain is below 80%, enlarge the sealed set to 60 before any training |
| 1. Re-baseline | How far do existing methods get, and through what? | All baselines retrained per fold, plus demographic-only and single-frame models | If the demographic baseline matches the fine-tuned predictor's rank agreement, age-adjusted rank agreement becomes co-primary |
| 2. Frozen agent | Do tools alone help? | Frozen Qwen with the fixed harness; best-of-8 with label-free selection | If verified coverage is below 30%, fix harness bugs before optimization |
| 3. Text-level levers | How much do prompt and harness search add per unit of compute? | GEPA and harness search, feedback from training folds only | The best harness becomes the training harness for Stages 4–5 |
| 4. Warm start | Does the privileged teacher help? | Privileged and non-privileged teachers, same filters and attempts | Keep both arms for Stage 5; flag tasks with fewer than 10 kept demonstrations |
| 5. RL | Do verified per-feature rewards beat score-only rewards? | GRPO arms at equal rollouts, three seeds for primary arms | Freeze all methods |
| 6. Confirmation | Do the development findings hold? | Sealed set, opened once | Report all pre-registered contrasts |

## 8. Evaluation

### 8.1 Estimators

All computed on the sealed set. **Task-averaged error**: mean absolute score error within each task, averaged equally over tasks. **Skill**: `1 − MAE_t / MAE_t(constant)` per task, averaged. **Rank agreement**: Spearman correlation within each task, averaged. **Calibration slope**: per task, median across tasks. **Verified coverage**: share of rows whose features all pass verification. **Feature error**: per feature, in score units.

### 8.2 Degenerate cases

Ties use average ranks. A task where a method's predictions are constant (for example, every case fell back) receives rank agreement 0 for that method. The task set is fixed in advance and no task is dropped for any method. A bootstrap replicate in which a task's references are constant assigns 0 to every method for that task.

### 8.3 Is it measuring movement?

- **Demographic-only baseline:** ridge regression from age and sex to each task score.
- **Single-frame baseline:** the fine-tuned predictor given one middle frame.
- **Age-adjusted rank agreement:** Spearman correlation between predictions and references after removing the rank-linear effect of age from both.
- **Motion perturbation:** for 100 sealed videos, shuffle frame order (keeping appearance, destroying motion) and recompute the affected tool outputs; a measuring agent's features should become unverifiable or change, while an appearance reader's would not.
- **Hard subset:** cases the expert pipeline flags (reconstruction failure, no event found, low pose confidence), defined without reference values; adaptive tool use should matter most here.

## 9. Statistics

**Unit.** Participants; every bootstrap replicate resamples participants with all their rows and recomputes estimators from scratch.

**Method claims and artifact claims.** Claims about a training method use a crossed bootstrap over seeds and participants; claims about one frozen agent resample participants only.

**Decision rule.** For the primary contrast, the 95% crossed-bootstrap interval for the rank-agreement difference lies above zero and the skill difference's interval has a lower end above −0.02.

**Power.** In Stage 0, power is simulated by resampling complete participant task vectors from cross-validated development predictions of two existing methods (the fine-tuned predictor and the tool-feature regressor), adding seed variability measured from repeated training, and applying the decision rule above.

**Multiplicity.** The secondary family is Holm-corrected; everything else is labelled exploratory.

## 10. Compute, budgets and timeline

**Currency.** All development compute is measured in H100-hours, including proposer models for prompt and harness search (run locally on open models), teacher generation, training, cache misses and inference. The shared tool cache (about 400 H100-hours) is counted once and reported separately.

**Budget tiers.** Each improvement method is evaluated at 50, 200 and 800 H100-hours of development compute where it can use them. Each added stage is compared with a **continuation control** that spends the same extra budget on the preceding method (for instance, more harness search instead of RL), and results are reported as accuracy-versus-cost curves.

**Minimum viable scope.** If the measured budget is below about 2,000 H100-hours, RL is restricted to six tasks covering the main families (standing, sit-to-stand, single-leg, Y-Balance, jump, gait), the primary contrast is evaluated on those tasks, and claims about the overall StaBLE score are dropped.

| Weeks from 26 Oct 2026 | Stage |
|---|---|
| 1–2 | Stage 0, with throughput measured on 50 videos and the scope decision dated 6 Nov |
| 3 | Stage 1 |
| 4–5 | Stages 2–3; teacher generation begins |
| 6–9 | Stages 4–5 |
| 10 | Stage 6 |
| 11–13 | Analysis and writing |

## 11. Risks

A strict verifier may starve learning; its thresholds are set on development folds before RL begins. The teacher may rarely succeed on tasks where every tool fails; those tasks fall back to RL-only training and are reported separately. If the expert pipeline or the tool-feature regressor matches the trained agent at lower cost, that is the finding.
