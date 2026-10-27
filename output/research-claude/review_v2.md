# Review of v2: "Measuring or Guessing? Tool-Calling Vision-Language Agents for Balance Assessment from One Camera"

Reviewed file: `docs/ideas-claude/v2_measure-or-guess-evaluation.md`
Rubric: see `review_v0_codex-baseline.md`.

## Scores

| Dimension | v0 | v1 | v2 | Rationale for v2 |
|---|---|---|---|---|
| D1 Significance (15%) | 4 | 6 | 6.5 | The "measure or guess" framing turns a benchmark result into a question the ML community recognizes (shortcut learning under outcome rewards). |
| D2 Novelty (15%) | 4 | 5 | 5 | The evaluation is careful, but the method is unchanged: four known levers applied in sequence. |
| D3 Research question (10%) | 6 | 7 | 8 | One primary contrast with a clear outcome and a dominance check against an expert pipeline. |
| D4 Soundness (10%) | 4 | 5 | 6 | The reinforcement-learning reward still targets only the final score, which conflicts with the paper's own diagnosis that methods drift toward typical values. |
| D5 Experimental design (10%) | 6 | 5 | 7 | Expert pipeline, single failure rule, and a hypothesis per stage. Budget matching across levers is still undefined, and test-time scaling baselines are missing. |
| D6 Statistics and leakage (10%) | 7 | 5 | 7.5 | Ledger, stratified folds, training-only normalization, crossed seed-and-participant bootstrap, Holm correction, power plan. Endpoints must also be recomputed inside each cross-validation fold. |
| D7 Feasibility (10%) | 3 | 7 | 7 | Data and tools exist. The cached environment is mentioned but not specified, and compute for the RL stage is not estimated. |
| D8 Clarity (10%) | 5 | 7 | 8 | The five-person example makes the measurement problem concrete in a few lines. |
| D9 Story arc (5%) | 3 | 5 | 7 | Stages A to E read as a sequence of tests. Some decision rules are vague ("inspect failure logs"). |
| D10 Writing (5%) | 6 | 7 | 7 | Natural, with a few long paragraphs that could be split. |

**Weighted overall: 6.78 / 10** (v1: 5.85). ICML readiness: borderline. The evaluation would now catch a guessing model, but the training method has no way to stop the agent from becoming one.

## Main critiques

1. **The reward contradicts the diagnosis.** v2 argues that error-based targets reward shrinkage toward typical values, then trains with a reward that is exactly the score error. Outcome-only rewards are known to let video models stop using the video ([Xu, 2026](https://arxiv.org/abs/2606.22043)), and tool agents trained with RL skip verification steps more often ([Thaman, 2026](https://arxiv.org/abs/2605.02964)).
2. **The most valuable training signal is unused.** Every training video has three-camera reference values for each of its features, not only for its task score. Rewarding each feature separately would give the policy a denser signal, rule out cancellation between feature errors, and tie credit to measuring.
3. **Group-relative advantages make a common fix ineffective.** In GRPO, each video's rollouts are compared with each other. Subtracting the constant-guess error from the reward changes nothing, because it is the same for every rollout of that video. A different mechanism is needed to make guessing unrewarding.
4. **The evidence pointer is reported but never checked.** If the harness re-executed the cited evidence and refused credit when the recomputed value disagreed with the reported value, typing a plausible number would earn nothing. That turns faithfulness from a report into a training constraint.
5. **The cached environment needs a definition.** Some tools take agent-chosen inputs (CoTracker3 tracks chosen points; OpenCap Monocular has settings). The proposal should say what is precomputed, what runs live, and what that costs.
6. **The fine-tuning stage may starve.** A frozen 8B model that scores worse than a constant guess may rarely produce runs good enough to imitate. The number of usable runs per task should be estimated before committing.
7. **Normalization inside folds.** Endpoints recomputed on "development participants" still leak across folds during cross-validation. They must be recomputed on the training folds of each split.
8. **Budget matching remains undefined.** Prompt search spends proposer-model tokens, harness search spends both tokens and rollouts, and RL spends GPU hours on gradient updates. One common currency, or a reported frontier, is needed.

## Suggestions for v3

1. Introduce **measurement-grounded rewards**: a per-feature reward against the three-camera reference, weighted by each feature's effect on the task score, so that the feature reward bounds the score error.
2. Add a **provenance check** that re-executes the cited evidence and gives no credit to unverified features.
3. Specify the **cached tool environment** and the RL loop (rollouts per video, handling of groups with no variance).
4. Add ablations that remove each reward component (score-only, features without provenance, full).
5. Add a **video-swap test** to detect outputs that do not depend on the video.
6. Recompute normalization endpoints inside each fold.
7. State the ML lesson in one sentence that applies beyond biomechanics.

## Codex adversarial review of v2 and its disposition

Verbatim output: `codex_adversarial_review_v2.md`. Verdict: needs-attention.

| Codex finding | Severity | Response |
|---|---|---|
| Correct scores can conceal wrong measurements | high | Addressed in v3 (per-feature reward, executable verification); v4 adds a materiality threshold. |
| Failure policy leaves rank agreement undefined for all-fallback tasks | high | Addressed in v4: a constant prediction vector receives rank agreement 0 for that task; ties use average ranks; degenerate bootstrap replicates assign 0; the task set is fixed in advance. |
| Power calculation does not match the primary statistic | high | Addressed in v4: power is estimated by resampling complete participant task vectors from cross-validated development predictions and applying the actual decision rule, including seed variability. |
| Development-wide normalization leaks across validation folds | high | Addressed in v3 (endpoints refit per fold); v4 extends fold-local fitting to fallback means, prompt examples and warm-start trajectories. |
| Metrics cannot separate motion measurement from appearance shortcuts (age correlates −0.76 with StaBLE) | high | Addressed in v4: demographic-only and single-frame baselines, an age-adjusted rank agreement, and motion perturbations that keep appearance fixed (frame-order shuffling, static-frame replay). |
| Expert pipeline does not isolate learned tool use | high | Addressed in v3: tool-feature regressor on the same cached outputs and labels, plus a fixed-call ablation. |
| Sequential ladder cannot attribute gains to methods | medium | Addressed in v4: every added stage is compared with spending the same extra budget on the previous stage (continuation control), and results are shown as accuracy–cost frontiers. |
| Ledger does not identify trials and references | medium | Addressed in v4: one row per trial, linked video and reference identifiers, and StaBLE's own repeated-trial aggregation rule from its released code. |
| Reused test set | medium | Addressed in v3 with a new sealed confirmatory set. |
| Cache conflicts with adaptive settings | medium | Addressed in v3 (argument menu, cache keyed by full arguments); v4 adds a measured throughput step and a dated scope decision. |
