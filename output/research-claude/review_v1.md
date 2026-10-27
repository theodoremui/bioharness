# Review of v1: "Learning to Conduct Balance Assessments from One Camera with Tool-Calling Vision-Language Models"

Reviewed file: `docs/ideas-claude/v1_stable-tool-agent-reframe.md`
Rubric: see `review_v0_codex-baseline.md`.

## Scores

| Dimension | v0 | v1 | Rationale for v1 |
|---|---|---|---|
| D1 Significance (15%) | 4 | 6 | Now squarely about training tool-calling VLMs, which ICML cares about, with a dataset that has a reference for every intermediate quantity. The ML lesson is still unstated. |
| D2 Novelty (15%) | 4 | 5 | A sensible combination of known levers (GEPA, Meta-Harness, SFT, GRPO). Nothing in the method is new. |
| D3 Research question (10%) | 6 | 7 | SMART and tied to an existing baseline. Beating 0.100 on MAE alone is a weak target, because MAE barely separates a constant guess (0.120) from the best model. |
| D4 Soundness (10%) | 4 | 5 | The reinforcement-learning reward uses only the final score error, which invites the model to output typical values. The "pointer to the tool output" is not defined. |
| D5 Experimental design (10%) | 6 | 5 | Baselines are good, but "the same number of agent runs" is not a fair budget across methods with very different costs, there are no ablations, and simple test-time scaling (best-of-N, majority vote) is missing. |
| D6 Statistics and leakage (10%) | 7 | 5 | The participant split and bootstrap are right. Three leaks or gaps remain: StaBLE's normalization endpoints come from all 180 people, including the test set; there is no power analysis for 43 people; and several methods are compared without correcting for multiple comparisons. |
| D7 Feasibility (10%) | 3 | 7 | Uses data, tools and baselines the lab already has. Reinforcement learning with video inputs in 13 weeks is tight, and the compute estimate is missing. |
| D8 Clarity (10%) | 5 | 7 | The first-principles walk through pose, reconstruction, features and score works well. The four improvement methods are named rather than explained. |
| D9 Story arc (5%) | 3 | 5 | The four levers appear as a list, without a hypothesis for each or a rule for what result leads to which next step. |
| D10 Writing (5%) | 6 | 7 | Natural and readable. The triad-like SMART bullet list is mechanical. |

**Weighted overall: 5.85 / 10** (v0: 4.75). ICML readiness: weak reject. The framing is now right, but the evaluation cannot yet tell measuring from guessing, and the method has no new idea.

## Main critiques

1. **The metric cannot separate measuring from guessing.** Predicting each task's training mean already scores 0.120, and the best model scores 0.100. A model that reverts toward typical values can look competitive on mean absolute error while ignoring the video. The question needs metrics that reward ordering people correctly (within-task rank correlation), that compare against the constant guess (a skill score), and that detect shrinkage toward the mean (the slope of predicted on reference scores).
2. **Normalization leaks the test set.** StaBLE rescales each feature using the minimum and maximum across all 180 participants (StaBLE Methods, Eq. 1–2). Using those endpoints means test participants helped define the scale on which training targets live. The fix is to recompute endpoints on development participants only for the primary analysis, and to report the published scale as a secondary analysis for comparability.
3. **The data accounting is implicit.** The dataset has 180 × 18 = 3,240 possible task slots, 3,322 recorded trials, 98 trials not performed for safety, 3 failed reconstructions, and 2,968 usable single-camera examples in the lab's pilot. v1 never says which of these rows enter training, which enter evaluation, and what happens to the rest. Without a fixed ledger, a reader cannot verify that each method sees the same data.
4. **Failures are not handled on equal terms.** OpenCap Monocular's 0.146 is computed on 567 valid cases, while the other methods are scored on all 729. A fair comparison needs one rule for all methods. For example, every failed case receives the training-task mean and the failure is reported, in the manner of an intention-to-treat analysis in clinical trials.
5. **The fine-tuning data will be skewed.** Keeping only "successful" frozen-agent runs means keeping mostly easy tasks and typical participants. The fine-tuned model then sees a distorted version of the dataset. The proposal should record how many examples survive per task and per ability level, and correct for it (quotas or reweighting).
6. **Reinforcement learning on the final score alone invites shortcuts.** Recent work shows that outcome-only rewards can make video models stop using the video ([Xu, 2026](https://arxiv.org/abs/2606.22043)). Score-only rewards also allow feature errors to cancel. The three-camera reference features, the dataset's most valuable asset, are not used as a training signal.
7. **Temporal information can be lost.** If frames are subsampled for the VLM without timestamps, hold times and speeds become meaningless. The proposal should state that every frame passed to the model carries its original time.
8. **No hypotheses.** Each improvement method should have a stated expected effect and a decision rule.

## Suggestions for v2

1. Reframe the primary question as "does the agent measure or guess?", and use a skill score against the constant baseline plus within-task rank correlation as co-primary outcomes, with mean absolute error kept for comparability.
2. Add a data ledger and a stratified participant split that preserves the distribution of age, ability and task-score shape in every fold; recompute normalization endpoints on development folds only.
3. Adopt one failure rule for all methods and report coverage.
4. Add a power calculation, a pre-registered list of primary contrasts with Holm correction, and seed-to-seed variability.
5. Turn the four levers into a sequence of hypotheses, each tested on development folds with a decision rule.
6. Keep timestamps attached to every frame and tool output.
7. Flag, for v3, the need to use the three-camera features as training signal.

## Codex adversarial review of v1 and its disposition

Verbatim output: `codex_adversarial_review_v1.md`. Verdict: needs-attention.

| Codex finding | Severity | Response |
|---|---|---|
| Published normalization leaks test outcomes | high | Addressed in v2 (development-only endpoints); v3 refits endpoints inside every cross-validation fold. |
| Score-only RL does not identify correct measurements; pointers are unverified | high | Addressed in v3: per-feature reward, replay/dependence/range verification, evidence-swap control. |
| Invalid outputs have no defined contribution | high | Addressed in v2 (single fallback rule); v3 adds verified coverage and states that fallbacks never count as measurements. |
| Participant-averaged error is a different estimator from task-averaged error | high | Addressed in v3: every estimator is defined within task first, then averaged over tasks, and recomputed inside each bootstrap replicate. |
| Controls cannot isolate learned tool use | high | Addressed in v3: expert pipeline, tool-feature regressor trained on the same labels, and a fixed-call ablation of the agent. |
| Cohort and reference measurements not reconciled | high | Addressed in v3: ledger statuses (measured, assigned zero, imputed, flagged, excluded); assigned and imputed targets masked from rewards. |
| Equal rollout counts do not support compute claims | medium | Partly addressed in v3 (best-of-8 baseline, cost reported). Accuracy at prespecified compute budgets is added in v4. |
| The reused test set is not untouched | medium | Addressed in v3: the lab's 43 test participants move into development and a new sealed confirmatory set of 43 is drawn. |
| One cached output per video cannot support adaptive actions | medium | Addressed in v3: cache keyed by video, tool version and full arguments, with a fixed argument menu and a cost estimate. |
