# Codex adversarial review of v1 (verbatim)

Target: `docs/ideas-claude/v1_stable-tool-agent-reframe.md`. Progress lines removed; findings verbatim.

```text
# Codex Adversarial Review

Target: working tree diff
Verdict: needs-attention

Not ready for confirmatory experiments. Test-derived normalization, inconsistent scoring, and a reward that permits incorrect measurements undermine the central claim. The comparisons also cannot isolate the value of learned tool use.

Findings:
- [high] Published normalization leaks test outcomes into training (docs/ideas-claude/v1_stable-tool-agent-reframe.md:78)
  The source notes explicitly state that StaBLE normalization uses feature extrema from all 180 participants. Applying that normalization unchanged makes training targets and rewards depend on test participants. Keeping the formula outside the VLM does not remove this leakage.
  Recommendation: Fit normalization endpoints on each training fold only, then on all development participants for final training. Freeze out-of-range handling and recompute every baseline under this protocol; retain published-scale results only as a secondary comparison.
- [high] Score-only reinforcement learning does not identify correct measurements (docs/ideas-claude/v1_stable-tool-agent-reframe.md:84-85)
  The reward observes an average of normalized features, so equal-and-opposite feature errors can cancel perfectly. A run can therefore receive optimal reward while reporting incorrect biomechanics. The output pointers in Section 4.3 have no specified verification procedure and do not prevent invented values from being attached to genuine tool outputs.
  Recommendation: Require executable, independently recomputed feature provenance and use a feature-level objective with predefined units and tolerances. Evaluate provenance validity separately from reference agreement, and include evidence-removal or shuffled-evidence controls to detect guessing.
- [high] Invalid outputs have no defined contribution to the primary loss (docs/ideas-claude/v1_stable-tool-agent-reframe.md:99)
  An MAE over all 729 examples cannot be computed when some predictions are missing unless their treatment is specified. Reporting failures separately leaves selective omission possible. This already affects the comparison: OpenCap's 0.146 covers only 567 cases and excludes an entire task, unlike the full-coverage predictors.
  Recommendation: Prespecify one failure rule for every method, such as a development-only task fallback or an explicit failure penalty, and recompute all baselines on the same examples. Report verified measurement coverage separately; fallback predictions must not count as valid measurements.
- [high] The statistical estimator changes the advertised outcome (docs/ideas-claude/v1_stable-tool-agent-reframe.md:99)
  Averaging errors within participants and then comparing participants estimates participant-weighted MAE, not the advertised task-averaged MAE. With 729 observations instead of 43 × 18, task availability is unequal, so these estimands need not agree. The resulting estimate and interval cannot be compared directly with the task-averaged 0.100 baseline.
  Recommendation: Define the primary estimator explicitly: average error within each task, then average equally across tasks. Resample whole participants and recompute that same estimator and paired baseline difference in every bootstrap replicate.
- [high] The controls cannot establish a contribution from learned analysis (docs/ideas-claude/v1_stable-tool-agent-reframe.md:95)
  The proposed agent receives multiple tools and feature-level supervision, whereas the strongest listed predictor learns scores from video. An improvement could come from those extra inputs, supervision, or repaired extraction heuristics without benefiting from adaptive tool use. Comparing four existing optimization techniques under these conditions leaves the application-driven ML contribution unestablished.
  Recommendation: Add a tuned deterministic workflow with the same tools and a non-agent predictor trained with the same tool outputs and feature labels. Ablate adaptive tool selection against fixed calls, and state the specific learning hypothesis those comparisons will test.
- [high] The cohort and reference measurements are not reconciled with the sources (docs/ideas-claude/v1_stable-tool-agent-reframe.md:62)
  The proposal describes reconstructed features for every participant, but the source notes identify safety-related nonattempts assigned zero, age-imputed features and retained reconstruction errors. They also distinguish 180 enrolled participants from 171 usable participants, explaining the otherwise missing nine in the 128/43 split. Without row-level accounting, exclusions can remove the least able participants or treat synthetic targets as observed measurements.
  Recommendation: Freeze a participant/task/trial manifest identifying usable videos, nonattempts, repeated trials, imputed labels and reconstruction-quality flags. Define eligibility and aggregation identically across methods, distinguish measured from assigned targets, and limit claims to the resulting population.
- [medium] Equal rollout counts do not support the compute-efficiency comparison (docs/ideas-claude/v1_stable-tool-agent-reframe.md:95)
  Agent runs differ in tool calls, retries and generated tokens. Prompt and harness search also incur proposer costs, while reinforcement learning inherits supervised training and adds backward passes. Equal run counts plus aggregate GPU-hour reporting do not establish which method performs best at a common resource budget.
  Recommendation: Compare accuracy at prespecified compute budgets, charging proposer calls, failed candidates, prerequisite training and tool execution. Separate development cost from deployment cost and include a frozen-agent repeated-sampling baseline with a label-free selection rule.
- [medium] The reused test set is not untouched confirmatory evidence (docs/ideas-claude/v1_stable-tool-agent-reframe.md:91)
  Section 1.2 already exposes six methods' results and a task-specific failure on these participants; that failure motivates the proposed mitigation. These participants remain held out of fitting, but their results have informed study design. Evaluating the new pipeline once does not undo that adaptive reuse.
  Recommendation: Label the existing split as a reused benchmark and confirm the frozen method on genuinely untouched participants if available. Otherwise frame the evidence as exploratory, disclose prior test access, and avoid claiming an untouched confirmatory evaluation.
- [medium] One cached output per video cannot support the proposed adaptive actions (docs/ideas-claude/v1_stable-tool-agent-reframe.md:114)
  Harness search changes tool settings, and CoTracker accepts chosen image points. Those actions can require different outputs for the same video. A single cached result either removes the advertised adaptation or leaves additional tool computation outside the feasibility estimate; caching also does not eliminate VLM rollout and training costs.
  Recommendation: Specify which tool configurations are fixed and which remain adaptive. Cache by video, tool version and complete arguments, budget cache misses, and provide a hardware-backed rollout/training estimate with an explicit scope-reduction rule for the thirteen-week schedule.

Next steps:
- Freeze the eligible-data manifest and training-only normalization before generating trajectories.
- Prespecify verified feature outputs, failure handling, the primary estimator, a meaningful effect size and participant-level power analysis.
- Add matched-information controls and compute budgets, then distinguish reused-benchmark results from confirmatory evidence.
exit=0
```
