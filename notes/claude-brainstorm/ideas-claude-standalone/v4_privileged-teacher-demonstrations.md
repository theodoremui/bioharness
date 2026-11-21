# Learning from a Better-Informed Teacher: Privileged Multi-Camera Demonstrations for Single-Camera Measurement Agents

## Abstract

When a more accurate instrument is available during training but not in deployment, one way to use it is to give it to a teacher. In balance assessment from one smartphone video, a three-camera reconstruction can show where the single-camera tools went wrong, such as a missed start of a movement or a reach that monocular reconstruction failed to detect. A teacher model given that reconstruction, but allowed to act only through the student's tools, could write better demonstrations of how to conduct the analysis. Whether a student that never receives the reconstruction can learn from them is uncertain, because decisions that depend on information the student lacks cannot be imitated reliably. This proposal compares students trained on demonstrations from the same teacher with and without a privileged view of the three-camera reconstruction, using matched examples and identical filters, and it measures both the teacher's advantage and how much of it reaches the student. It also tests whether the teacher decisions that transfer are the ones predictable from what the student observes, which is the condition under which privileged imitation should work.

## 1. Motivation

### 1.1 The measurement task and the agent

In the StaBLE "rise to toes" task ([Heigold et al., 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13621976/)), a person rises onto their toes as quickly and as high as they can and holds for five seconds. Three **features** describe the performance: the peak upward speed of the **center of mass** (the average position of the body's mass), the peak ankle angle, and the time the center of mass stays high. Each is rescaled to 0–1 and the rescaled values are averaged into a **task score**. StaBLE has 18 tasks and 76 features, recorded from 180 adults with three smartphones, and the three-camera reconstruction is accurate enough to serve as the reference.

The student is a tool-calling **vision-language model** (VLM): given one camera's video, it requests frames, runs pose, segmentation and 3D-reconstruction tools, writes short functions that turn their outputs into features, and submits the features, which the task's fixed formula turns into a score. A strong way to start training such an agent is **supervised fine-tuning (SFT)** on demonstrations: complete example runs, or **trajectories**, from a more capable model, which the student learns to reproduce.

### 1.2 Where single-camera analysis goes wrong

Monocular reconstruction estimates depth from modeling assumptions, so it can misplace the center of mass, miss the start of a rise, or fail to register the moment the toe reverses during a Y-Balance reach. A teacher working from the same single-camera tools makes the same mistakes unless something tells it otherwise. A read-only panel of the three-camera curves for the training video would reveal, for instance, that the rise begins at 3.9 s although the monocular center of mass stays flat until 4.6 s — and the teacher could then choose a window or a tool route that the student could also have chosen.

### 1.3 The imitation gap

A teacher's decision is useful to a student only if the student can tell, from its own observations, when to make it. Suppose the teacher picks the window 3.9–10.6 s because the panel shows the rise. If the 2D heel-height signal available to the student also shows the rise at 3.9 s, the student can learn the decision. If only the panel shows it, the student learns to choose windows it cannot justify and may apply them where they are wrong. This gap between what a privileged expert does and what an observer can infer is a known hazard in imitation learning ([Weihs et al., 2021](https://arxiv.org/abs/2007.12173)) and in distilling privileged language-model teachers ([Penaloza et al., 2026](https://arxiv.org/abs/2602.04942)). Restricting the teacher to the student's actions removes one source of the gap (the student can execute everything the teacher does) and leaves the other (the student may not know when to).

## 2. Research question and hypotheses

> **Research question.** Can a teacher given a privileged three-camera reconstruction, but allowed to act only through the student's single-camera tools, write demonstrations that make the student a more accurate measurer than demonstrations from the same teacher without that view? How much of the teacher's own advantage reaches the student, and which kinds of decisions carry it?

| ID | Hypothesis | Refuted if |
|---|---|---|
| H1 (prerequisite) | The privileged teacher's own feature error is lower than the plain teacher's on the same training videos | No difference on development folds |
| H2 (primary) | Students fine-tuned on privileged demonstrations have lower feature error on sealed participants | The 95% interval for the expected difference over retraining includes zero |
| H3 | The student gap persists after both students receive identical reinforcement learning | The gap closes |
| H4 | Teacher decisions that are predictable from student observations transfer more than those that are not | The share of the teacher's advantage that transfers does not depend on decision predictability |

The **transfer ratio**, the student gap divided by the teacher gap on the same development examples, summarizes how much of the privileged advantage survives distillation.

**What the study would establish.** In most privileged-teacher settings the teacher differs from the student both in what it observes and in what it may do. Here teacher and student share one action space, so the remaining gap is one of observation alone, and a physical reference measures the result. The predictability analysis behind H4 offers a practical test that could be run before any student is trained: if the teacher's key decisions cannot be predicted from student-visible signals, privileged demonstrations should not be expected to help.

## 3. Related work

**Learning with privileged information.** Vapnik and Vashist (2009) introduced training with information that is unavailable at test time. [Learning by Cheating](https://arxiv.org/abs/1912.12294) trained a driving agent with privileged access to the world's state, then distilled it into a vision-only student with on-policy supervision. Asymmetric actor–critic methods ([Pinto et al., 2017](https://arxiv.org/abs/1710.06542)) give the critic, but not the policy, privileged state.

**The imitation gap.** Weihs et al. (2021) showed that imitating a privileged expert fails when its actions depend on unobserved information and proposed mixing imitation with reward learning. π-Distill and on-policy self-distillation (Penaloza et al., 2026) study the same problem for language-model agents.

**Demonstrations before reinforcement learning.** Tool-use agents are commonly fine-tuned on verified demonstrations and then trained with outcome rewards ([ReTool](https://arxiv.org/abs/2504.11536)). This study asks whether privileged information makes the demonstration stage more valuable, and whether any advantage survives the later RL stage.

**Biomechanics agents.** [BiomechAgent](https://arxiv.org/abs/2602.06975) writes analysis code over processed motion-capture data without training the model; [OpenCap Monocular](https://arxiv.org/abs/2603.24733) supplies the single-camera reconstruction tool.

## 4. Method

### 4.1 Tools and harness

Both teachers and students use one harness. Its tools are timestamped frames and crops, 2D landmarks (RTMPose or a second pose model), person segmentation (SAM 2.1), point tracks (CoTracker3) for 16 body regions, 3D joint angles and center of mass (OpenCap Monocular, two settings), plotting and a Python sandbox. Expensive outputs are computed once and cached, requests outside the menu return an error, and every signal is indexed by time in seconds. For each feature, a submission contains the value, the function that computed it from cited tool outputs and marked start and end times, the cited outputs and the marks.

### 4.2 Two teachers

The teacher is a larger frozen model (Qwen3-VL-235B-A22B). The **privileged teacher** additionally receives a read-only reference panel showing the three-camera joint-angle and center-of-mass curves and the reference feature values for the training video. The **plain teacher** is the same model with the same prompt minus the panel. Each makes eight attempts per training video.

### 4.3 Keeping demonstrations executable and honest

The panel must improve decisions without leaking answers. Four safeguards apply identically to both teachers:

- **Executable actions.** Teachers act only through the student's tools, and every submitted feature must replay from the cited single-camera outputs.
- **No copied numbers.** Each feature function is also run on a copy of its inputs with noise far below measurement precision; a function that returns a memorized value takes a different path on the noisy copy and fails. Feature functions may use only array operations from a fixed library, with no branching on array identity and no numeric literals beyond physical constants and small integers.
- **Cross-video validity.** The teacher's final feature functions are run on five other training videos of the same task, with the expert pipeline's start and end marks, and must be no less accurate there than the expert pipeline. A function tuned with hindsight to one video fails.
- **Panel stripping.** The panel and any text quoting it are removed before a trajectory is used, and trajectories whose remaining text mentions panel values (string matching) or panel-specific terms are discarded.

Demonstrations must also meet the same accuracy threshold against the reference, fixed before generation.

### 4.4 Matched demonstration sets

The two teachers will succeed on different videos, and a student trained on more or different examples could improve for that reason alone. The primary comparison therefore uses only the participant–task examples accepted in both conditions, with equal counts per task and at most 40 per task. Acceptance rates are reported for each teacher, and a secondary comparison uses all accepted demonstrations from each, which includes any coverage benefit.

### 4.5 Students

Qwen3-VL-8B is fine-tuned with low-rank adapters on each demonstration set, with five paired seeds per condition and identical hyperparameters, data order and training length. The students receive only the Cam0 video, the task description and the feature definitions. For H3, both students then receive the same reinforcement learning, group relative policy optimization ([GRPO](https://arxiv.org/abs/2402.03300)) with a per-feature reward against the reference, for the same number of rollouts and with three seeds each.

### 4.6 Which decisions can be inferred

From every kept privileged demonstration, the analysis extracts the teacher's decisions: the tool route used for each feature (3D reconstruction or 2D signals), the start and end marks, and any retry after a failed tool. For each decision type, a gradient-boosted model is trained on training folds to predict the decision from **student-observable** signals: 2D pose confidence, the fraction of frames with both feet visible, clip length, overall motion energy and summaries of cached tool outputs. Its cross-validated accuracy, against a baseline that always predicts the most common choice, is that decision type's **predictability**. Features are then grouped by the predictability of the decisions that most affect them, and the transfer ratio is compared across groups (H4).

## 5. Data, splits and leakage

**Dataset and ledger.** StaBLE contains 180 adults aged 18 to 87, from people with vestibular disorders to competitive athletes and dancers; 171 have usable single-camera video. A ledger lists every recorded trial (3,322) with its Cam0 video, reference features, participant, task and status. Thirty trials flagged for reconstruction error and three with imputed features are kept as inputs but never shown on a panel, used as targets or used in the primary evaluation. Ninety-eight tasks not attempted for safety have no video.

**Splits.** Sixty participants are set aside before any analysis, stratified by StaBLE score quintile, age group and athlete status, and drawn from people who were never in the lab pilot's test set. This is a retrospective re-split, documented as such, with every baseline retrained without them. The other 111 participants form five stratified development folds, checked against the whole (Kolmogorov–Smirnov tests and standardized mean differences below 0.1). Teachers generate demonstrations only for development participants, and only from training folds when a development decision is being made.

**Leakage.** The panel shows references of training videos only, and no sealed participant's reference is ever displayed, used to filter a demonstration or used to fit any component. Rescaling endpoints, accuracy thresholds, cross-video check recordings and the predictability models come from training folds. Seven participants appear in StaBLE's public exemplar video; results are reported with and without them.

**Keeping the data's shape.** Teachers attempt every eligible training row, so generation covers the dataset's mix of tasks, ages and ability levels. Matching and filtering can tilt that mix toward easy recordings, so per-task and per-ability-quintile counts are reported for each demonstration set, and fine-tuning reweights any task whose share drifts by more than a quarter from its ledger share.

## 6. Evaluation

**Primary outcome.** Feature error in score units (the absolute difference between submitted and reference values after rescaling with training endpoints) on sealed participants, immediately after fine-tuning, averaged over features within a task and then over tasks with equal weight. Errors in physical units are reported per feature.

**Secondary outcomes.** Error in the start and end marks against the three-camera segmentation, which locates any benefit in event finding; task-score error and within-task rank agreement; the same outcomes after RL (H3); the transfer ratio overall and by predictability group (H4); and teacher-versus-student error on identical development examples, since a strong privileged teacher with no student gain points to a failure of transfer.

**Failure rule.** A trial without usable output receives the training-fold task mean and is counted as a fallback; fallback rates are reported, and comparisons are repeated on trials both students completed.

## 7. Statistics

Participants are the unit of analysis, and every interval resamples participants with all their trials. Claims about the two demonstration sets are claims about a training method, so they target the expected improvement over retraining: five paired fine-tuning seeds per condition (three for the RL stage), with an interval that combines the spread between paired seed differences and the participant-bootstrap spread of the seed-averaged difference (t-distribution, Satterthwaite degrees of freedom), and whose coverage is checked by simulation before training. H2 succeeds if the upper 95% bound for the privileged-minus-plain error difference is below zero. H3 and H4 form one Holm-corrected family; H1 is a prerequisite reported with its interval. Power for a 0.01 difference in feature error is estimated before training from repeated fine-tuning runs.

## 8. Scope and cost

| Item | H100-hours (estimate) |
|---|---|
| Tool cache, computed once | 400 |
| Teacher generation, both teachers, eight attempts per development video | 500 |
| Student fine-tuning, two conditions × five seeds | 150 |
| Predictability models | 10 |
| RL stage, two students × three seeds (about 150 each) | 900 |
| Evaluation | 50 |
| **Total** | **about 2,000** |

The primary comparison needs no reinforcement learning and costs about 1,100 H100-hours; the RL stage can be run on six tasks spanning the main task families for about 360 H100-hours, against 900 for all tasks.

## 9. What each outcome would mean

A lower student error after fine-tuning (H2) would show that privileged demonstrations transfer on the matched examples; the matching may favor easier recordings, so the secondary comparison shows whether coverage adds to the benefit. A privileged teacher that is much better than the plain one (H1) with no student gain would show that its advantage lives in decisions the student cannot make on its own evidence, and the predictability analysis would say which. If the gap closes after RL (H3 refuted), privileged demonstrations speed up the start of training without changing where it ends.

The safeguards reduce direct copying but cannot remove every decision influenced by the panel, which is why the comparison measures outcomes instead of assuming that the restrictions work. Because the reference is a reconstruction that shares its body model with the monocular tool, any gain establishes closer agreement with that reference, not independent validation of the inferred biomechanics.
