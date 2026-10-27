# Rewarding Only What Can Be Checked: Training Tool-Calling Video Agents to Measure Balance from One Camera

*Version 6. This is a simplification pass. The science of v5 is kept, but the document is reorganized around one thesis and one running example (the "rise to toes" task), with a worked trajectory, a single table that says for every stage how the data keep their shape and how leakage is blocked, five confirmatory comparisons instead of seven, and every fixed number moved to an appendix.*

![Training pipeline](figures/training_pipeline.svg)

*Figure 1. Data are frozen before training (top). In training (middle), the agent works from one camera and cached tool outputs; the three-camera reference (amber) reaches it only through rewards, teacher demonstrations and the tool-outcome model's labels. Sealed participants and held-out tasks are opened once, at the end (bottom).*

## Abstract

Smartphone video could make balance assessment routine, but a score computed from one camera is worth trusting only if it reflects how the person moved. On a large balance dataset, simply predicting the average score is nearly as accurate as the best learned model, and age alone explains much of the score, so accuracy figures can hide models that measure little. We propose to train a vision-language model to carry out the measurement itself, calling pose, segmentation and 3D reconstruction tools and writing the code that turns their outputs into each task's defined features, and to reward it only for what can be checked. During training, a three-camera reconstruction gives a reference for every feature; a feature earns credit only when the agent's code also reproduces known answers on other videos; a teacher that can see the reference produces demonstrations restricted to the tools the student has; and a learned model of the tools predicts what each call will cost and how accurate it will be. Evaluated on people and tasks held back until the end, the study asks whether this kind of supervision teaches an agent to measure movement, as opposed to predicting a plausible score, and what that costs.

## 1. The problem, through one example

In the StaBLE "rise to toes" task ([Heigold et al., 2026](https://doi.org/10.64898/2026.09.16.750744)), a person rises onto their toes as quickly and as high as they can and holds for five seconds. Three numbers capture how well they did: the peak upward speed of their **center of mass** (the average position of the body's mass), the peak ankle angle, and how long the center of mass stays high. Each number, called a **feature**, is rescaled to a 0-to-1 range using the lowest and highest values seen in the data, and the three rescaled values are averaged into a **task score**. StaBLE has 18 such tasks with 76 features in total, recorded from 180 adults ranging from people with vestibular disorders to professional dancers, and averages the 18 task scores into one balance score.

The dataset was recorded with three smartphones, whose combined views give an accurate 3D reconstruction. The practical goal is to get the same numbers from one phone. The lab's pilot tried two routes. Rebuilding the skeleton from one camera with OpenCap Monocular and then applying StaBLE's rules produced a valid score for only about three quarters of test cases and took around four GPU-minutes per clip. Learned models that map video straight to a score always answered, but the best of them, a fine-tuned Qwen3-VL-8B, beat a constant guess (each task's average) by only about a sixth, and the same model without fine-tuning did worse than the constant.

A low error can hide a model that ignores the video. Suppose five people have true scores 0.4, 0.5, 0.6, 0.7 and 0.8. Guessing 0.6 for everyone gives a mean absolute error of 0.12. A model that keeps the right order but shrinks every difference to a fifth of its size does slightly better, 0.096, while telling us almost nothing about who balances better. We therefore judge methods mainly by **rank agreement**, the correlation between predicted and true orderings of people within a task, and also report **skill** (how much a method beats the constant guess) and the **calibration slope** (whether differences between people survive or collapse toward the average). A second trap is appearance: the balance score falls steeply with age, so a model can rank people well by how old they look.

## 2. Why an agent

A **vision-language model (VLM)** takes images or video frames together with text and produces text. In **tool calling**, part of that text is a structured request, such as "run the pose detector on this video", which surrounding software carries out before returning the result to the model. That surrounding software is the **harness**: the list of tools and their descriptions, the loop that executes calls, the record of what has happened, and the rule for stopping. The model plus its harness, acting over several steps, is an **agent**, and one complete run from video to answer is a **trajectory**.

The agent route splits the work along the lines of what each component does well. Specialist tools, already validated, handle geometry: finding ankles in each frame, reconstructing a skeleton, tracking a point. The VLM handles the parts that need judgement and language: reading the task description, choosing which tools fit, looking at a plot to see when the person actually started rising, noticing that a tool returned nonsense, and writing the few lines of code that turn a center-of-mass curve into a peak speed. A fixed formula then turns features into a score, so every score can be traced back to measurements that a clinician could inspect. Prior work supports both halves of this division: a code-writing biomechanics agent improved when given a validated gait-event tool ([BiomechAgent](https://arxiv.org/abs/2602.06975)), and reinforcement learning taught a VLM when to use a visual tool ([DeepEyes](https://arxiv.org/abs/2505.14362)).

## 3. The thesis and its four parts

**Thesis: reward the measurements, and only those that can be checked.**

A standard way to improve an agent is **reinforcement learning (RL)**: the model produces its own trajectories, a **reward** scores each one, and the model is nudged toward the higher-scoring ones. We use group relative policy optimization ([GRPO](https://arxiv.org/abs/2402.03300)), which samples several trajectories for the same video and compares each with the group's average. The obvious reward, closeness of the final score to the true score, has two weaknesses. A trajectory can land near the right score without measuring anything, and it is known that rewarding only final answers can lead video models to stop using the video ([Xu, 2026](https://arxiv.org/abs/2606.22043)). And because the score is an average, overestimating the ankle angle while underestimating hold time can produce the right score from two wrong measurements. Four design choices address these weaknesses.

**1. Reward each feature, not just the score.** During training, the three-camera reconstruction gives a reference value for each of the three rise-to-toes features. The reward adds up the error of each feature separately. Because the score is an average of features, its error can never be larger than this sum, so a high reward implies an accurate score, while errors no longer cancel.

**2. Give credit only for features that pass a known-answer check.** The agent must submit, with each number, the short function that computed it from tool outputs. The harness re-runs that function on a few other development videos of the same task whose correct values are known, two from people who rose slowly and two from people who rose quickly. A function that measures peak speed gives roughly the right answers on those videos and puts them in the right order; a function that returns a typical speed whatever the input does not. A feature that fails the check is replaced by the average value and penalized. The check needs no reference for the video being analysed, so it works identically when the agent is tested on new people.

**3. Start from a privileged teacher.** RL learns slowly from a weak starting point, so the agent is first fine-tuned on demonstrations (**supervised fine-tuning**, SFT). The demonstrations come from a larger model given a **reference panel** showing the three-camera curves for the training video, which helps it see, for example, that the one-camera reconstruction missed the start of the rise. The teacher acts only through the tools the student has, and its own numbers must pass the same known-answer check, so it cannot copy the reference into its answer. Demonstrations are kept only if the teacher's functions also work on five other videos of the task, which removes solutions tuned with hindsight to one video. Information that the teacher can use and the student cannot is a known hazard when distilling privileged teachers ([Penaloza et al., 2026](https://arxiv.org/abs/2602.04942)), and these restrictions are designed to keep the teacher's choices learnable.

**4. Learn what the tools will do before calling them.** The one-camera 3D reconstruction takes minutes per clip, while 2D pose takes seconds. A small **tool-outcome model**, a world model of the tool environment, predicts from cheap signals (pose confidence, whether the feet are visible, clip length) how accurate each tool route is likely to be for each feature and what it will cost. The agent can query it before an expensive call, and its predicted errors, once calibrated, give an uncertainty range for each score. This is a narrow, checkable version of the broader idea of letting agents predict the outcome of an action before committing to it ([survey](https://arxiv.org/abs/2604.22748)).

## 4. A worked trajectory

The example below shows the shape of one training trajectory for rise to toes. The numbers are illustrative.

1. The agent reads the task and the three feature definitions.
2. It calls the 2D pose tool. The harness replies with a summary: 26 landmarks per frame at 60 frames per second, ankles visible in 98% of frames.
3. It asks for a plot of heel height over time, sees the rise beginning near 4.1 s and the return near 10.3 s, and records `task_start = 3.9` and `task_end = 10.6`.
4. It asks the tool-outcome model whether the 3D reconstruction is worth four minutes for this clip. The predicted error for peak center-of-mass speed is much lower with 3D than with 2D, so it calls the reconstruction.
5. It writes three functions, for instance `peak_speed(out, ann)`, which differentiates the vertical center-of-mass position with respect to time and takes the maximum between `ann.start` and `ann.end`.
6. It submits the three values with their functions and annotations.

The harness then re-runs each function on the cited outputs (the values match), runs it on four probe videos with known answers (errors are small and the slow risers come out below the fast risers), and checks that each value is in a plausible range. All three features are verified, the formula computes the task score, and the reward is minus the average feature error against the three-camera reference, minus a small penalty for timing error in the annotations. Had the agent written `return 0.18` for peak speed, the probe check would have returned 0.18 for slow and fast risers alike, the feature would have failed, and the reward would have dropped.

## 5. Research question and hypotheses

**Primary question.** By the ICML 2027 submission deadline (expected late January 2027), does GRPO with the verified per-feature reward produce a Qwen3-VL-8B tool-calling agent with higher mean within-task rank agreement, on 60 participants sealed until the end, than GRPO with a final-score reward, when both start from the same fine-tuned model and use the same number of trajectories?

This is specific (one model, one change, one dataset), measurable (rank agreement with a stated decision rule, Section 9), achievable (data, tools and baselines exist; Section 10 gives a reduced scope if compute falls short), relevant (it tests whether rewarding checked measurements, rather than outcomes, teaches an agent to measure), and time-bound (thirteen weeks).

**Confirmatory secondary comparisons** (Holm-corrected as one family of five):

| | Comparison | What it tells us |
|---|---|---|
| S1 | Verified per-feature reward against the same reward without the check | Whether the known-answer check is needed |
| S2 | Privileged teacher against a plain teacher, after fine-tuning | Whether the reference panel improves the starting point |
| S3 | Final agent against the strongest non-agent method, chosen on development data from three candidates: the fine-tuned direct predictor, an expert-written pipeline using the same tools, and a regressor trained on the same tool outputs and feature labels | Whether learned tool use adds anything beyond the tools and labels themselves |
| S4 | Final agent against the direct predictor on time-scaling interventions (Section 9) | Whether outputs respond to movement as physics predicts |
| S5 | Trained against untrained agent on three held-out tasks | Whether the learned skill transfers to tasks never trained on |

Cost-aware training with the tool-outcome model, prompt and harness search across budgets, and calibrated uncertainty are exploratory.

## 6. Related work

**Movement-analysis VLMs.** Knowledge-augmented gait VLMs ([Wang et al., 2024](https://arxiv.org/abs/2403.13756)), [BioGait-VLM](https://arxiv.org/abs/2603.08564) and [MyoMechanix](https://arxiv.org/abs/2608.26094) map video, skeletons or movement phases to labels or coaching feedback without calling measurement tools.

**Biomedical agents.** [Biomni](https://doi.org/10.1101/2025.05.30.656746) and [BiomechAgent](https://arxiv.org/abs/2602.06975) show that domain tools help agents but do not train the model to use them.

**RL for tool use.** [DeepEyes](https://arxiv.org/abs/2505.14362), [LongVT](https://arxiv.org/abs/2511.20785) and [VITAL](https://arxiv.org/abs/2508.04416) train VLMs to crop, zoom or resample video from rewards on final answers; [ToolRL](https://arxiv.org/abs/2504.13958) adds finer rewards on tool names and arguments. Our rewards score the physical quantities the tools are used to measure, and credit only checked ones. Concerns about agents gaming their rewards ([Thaman, 2026](https://arxiv.org/abs/2605.02964)) motivate the check.

**Prompt and harness optimization.** [GEPA](https://arxiv.org/abs/2507.19457), [Meta-Harness](https://arxiv.org/abs/2603.28052) and [VidHarness](https://arxiv.org/abs/2609.38413) improve an agent without changing its weights. A recent re-evaluation found that such gains often vanish against equally budgeted repeated sampling and on new tasks ([Wang et al., 2026](https://arxiv.org/abs/2607.12227)), so both appear here as budget-matched baselines.

## 7. Data, splits and leakage

**The ledger.** One row per recorded trial (3,322 in StaBLE), linking the single-camera video to its three-camera reference features and to its participant and task, with StaBLE's released code deciding how repeated or two-sided trials combine. Each row has a status. *Measured* rows are used everywhere. Thirty trials flagged for reconstruction error and three whose features were imputed from age are kept as inputs but excluded from rewards and from the primary evaluation. Ninety-eight tasks not attempted for safety have no video and enter only the overall balance score, as zeros, exactly as StaBLE defines it.

**Sealed participants.** Of the 171 participants with usable video, 60 are set aside before any analysis, chosen from people who were never in the pilot's test set and stratified by balance score, age group and elite-athlete status. The remaining 111 form five development folds, stratified the same way. Because the pilot trained models on some of the sealed participants, this is a retrospective re-split: we document all prior use of their data, retrain every baseline without them, and propose confirmation on newly recorded participants as follow-up.

**Held-out tasks.** Semi-Tandem, Gait-Backwards and Functional Reach are fixed now. Their videos are excluded from every training stage, and their feature definitions are first shown to the agent at the final evaluation.

**Everything fitted inside folds.** The rescaling endpoints (StaBLE's published ones use all 180 people, including future test participants), the fallback averages, probe videos, teacher demonstrations, prompt examples and harness-search feedback all come only from the training folds of each split.

## 8. The research journey

Each stage asks one question, is answered on development folds only, and ends with a decision. The sealed set is opened once, at the end. The table states, for every stage, how the training data keep the dataset's shape and what prevents leakage.

| Stage | Question and change | Data used | How the data keep their shape | What blocks leakage | Decision |
|---|---|---|---|---|---|
| 0. Groundwork | Is the protocol sound and powered? Build ledger, cache tool outputs, write expert pipeline, validate the checker | All 171 people, sealed set untouched | One row per trial with explicit status; no row dropped silently | Sealed set reserved first; checker tuned on development folds | Power below 60%: report estimates only; 60–80%: proceed and report power |
| 1. Re-baseline | What do existing methods achieve, and through what? | Development folds | Each fold stratified by balance score, age and athlete status, checked statistically | All baselines retrained inside folds, endpoints refitted per fold | If an age-and-sex model ranks people as well as the direct predictor, age-adjusted rank agreement becomes co-primary |
| 2. Frozen agent | Do tools alone help? | Development folds | Every eligible trial evaluated, failures scored as the training average | No training; prompt examples from training folds | Low checked coverage sends us back to the harness |
| 3. Prompt and harness search | How much do text-level changes add per GPU-hour? | Training folds for feedback, validation fold for selection | Feedback sampled evenly over tasks | Search never sees validation results beyond a fixed number of queries | The best harness becomes the training harness |
| 4. Warm start | Does the privileged teacher help? | Training folds | At most 40 demonstrations per task; per-task counts reported | Teacher sees references of training videos only | The better warm start feeds every RL arm |
| 5. RL | Do checked per-feature rewards beat final-score rewards, and is the check needed? | Training folds | Trials sampled with equal probability; any task whose share of updates drifts by more than a quarter is reweighted | References used only inside rewards | Freeze all components |
| 6. Tool-outcome model | Can the agent spend less? | Training folds | All tool configurations of every training video | Labels from training folds only | Exploratory |
| 7. Confirmation | Do findings hold for new people and new tasks? | Sealed set and held-out tasks | Every eligible sealed trial scored | Opened once, after freezing | Report all pre-registered comparisons |

## 9. Evaluation and statistics

**What is measured.** All measures are computed within each task and then averaged over tasks with equal weight: rank agreement (primary), skill, calibration slope, absolute error, the share of trials whose features all pass the check (**checked coverage**), and per-feature error. The agent's time annotations are compared with the three-camera segmentation and reported separately, because the check certifies the agent's code but not the window it chose by looking at the video. Ties, constant predictions and other degenerate cases have fixed rules (Appendix A).

**Is it measuring movement?** Three controls. An age-and-sex model and a model given a single frame show how far appearance alone goes. Rank agreement is also reported after removing the effect of age. In **time-scaling interventions**, 100 sealed videos are slowed to 0.8× speed with corrected timestamps, so appearance is identical but movement is slower; durations should grow by a quarter, speeds should drop by a fifth, and angles should not change. The expected responses are first checked on development videos with the expert pipeline, which also sets the achievable ceiling. A method that measures movement should respond as predicted, while a method that reads appearance should not.

**Inference.** The unit of analysis is the participant, because one person's 18 tasks are correlated. Every confidence interval comes from resampling participants with all their trials and recomputing each measure. Claims about a training method (for example "the checked reward helps") also resample the training seeds, because a lucky run shifts every participant at once; claims about one frozen agent do not. The primary comparison succeeds if the 95% interval for the rank-agreement difference lies above zero and the skill difference is not worse than −0.02. Power is estimated before training by resampling development predictions of existing methods and applying this exact rule.

## 10. Feasibility

The tool cache costs about 400 H100-hours, dominated by the one-camera reconstruction. The default plan adds about 3,600 H100-hours: teacher generation, fine-tuning with three seeds per teacher, and nine RL runs (three rewards, three seeds each) plus one cost-aware run, with the throughput measured on 50 videos in the first week. Each RL arm is compared with spending the same budget on more harness search. If less than 2,000 H100-hours is available, RL is limited to six tasks spanning the main task families, the primary comparison is made on those, and claims about the overall balance score are dropped.

| Weeks from 26 Oct 2026 | Work |
|---|---|
| 1–2 | Stage 0; scope decision by 6 November |
| 3 | Stage 1 |
| 4–5 | Stages 2 and 3; teacher generation |
| 6–9 | Stages 4 to 6 |
| 10 | Stage 7 |
| 11–13 | Analysis and writing |

## 11. Risks, and what a negative result would teach

If the checker is too strict, few trajectories earn credit and learning stalls; its tolerances are fixed in Stage 0 against a suite of deliberate shortcut programs that must fail and expert functions that must pass. If some tasks defeat every tool, they produce fallbacks for every method and are reported separately. If an expert pipeline or a regressor on the same tool outputs matches the trained agent at lower cost, that is a useful finding about when learning is worth it. And if checked per-feature rewards do no better than final-score rewards, the result still tells the field something specific: that for this kind of task, outcome rewards did not lead the agent to stop measuring.

## Appendix A. Settings fixed before training

| Setting | Value |
|---|---|
| Probe videos per feature | Four from training folds: two near the 25th and two near the 75th percentile of the reference, among videos where the expert pipeline's start and end agree with the three-camera segmentation within 0.2 s |
| Probe pass rule | Mean probe error at most max(0.15, 1.5 × expert pipeline's probe error) in score units, and both low probes below both high probes |
| Range rule | Within the training range widened by half its width on each side |
| Shortcut suite | Training mean; mean plus a tiny multiple of the input; mean plus noise; right computation on the wrong body part; wrong units; hard-coded window; function of clip duration; function of pixel height. Each must fail at least 95% of the time; expert functions must pass at least 90% |
| Reward | `−(1/k) Σ_f [e_f + 0.5 · unverified_f] − 0.1 × annotation error (s)`; unparseable submission −2 |
| GRPO | Eight trajectories per video; groups with identical rewards skipped ([DAPO](https://arxiv.org/abs/2503.14476)) |
| Degenerate cases | Ties use average ranks; constant predictions get rank agreement 0; a bootstrap replicate with constant references gives 0 to every method; a task with zero constant-guess error is dropped from skill for all methods |
| Power target | 80% for a 0.05 gain in rank agreement with 60 participants |

## Appendix B. Why the per-feature reward bounds the score error

Let a task have `k` checked-or-replaced features with rescaled values `n_f`, so the task score is their average. For predicted values `x̃_f` (the agent's value if checked, the training mean otherwise) and reference values `x*_f`, define `e_f = |n_f(x̃_f) − n_f(x*_f)|`. Then `|Ŝ − S*| = |(1/k) Σ_f (n_f(x̃_f) − n_f(x*_f))| ≤ (1/k) Σ_f e_f`, which is at most the reward's penalty term. The inequality covers features with a usable reference; masked features are left out of both sides.
