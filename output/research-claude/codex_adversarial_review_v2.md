# Codex adversarial review of v2 (verbatim)

Target: `docs/ideas-claude/v2_measure-or-guess-evaluation.md`. Progress lines removed; findings verbatim.

```text
# Codex Adversarial Review

Target: working tree diff
Verdict: needs-attention

Do not proceed unchanged. The protocol cannot establish measurement rather than guessing, and its primary statistic, power calculation, and cross-validation safeguards remain incomplete.

Findings:
- [high] Correct scores can conceal fabricated or incorrect measurements (docs/ideas-claude/v2_measure-or-guess-evaluation.md:104-106)
  The reward observes an average of normalized features, so opposing feature errors can cancel exactly: reference features (0.2, 0.8) and predictions (0.5, 0.5) produce the same score. Every proposed score-level metric inherits this blind spot. Naming a tool output and time window does not specify or verify the computation that produced a feature.
  Recommendation: Require executable feature provenance checked by an independent evaluator, train against feature-level reference errors with prespecified tolerances, and report verified feature accuracy and coverage separately from score accuracy.
- [high] The failure policy leaves rank agreement undefined (docs/ideas-claude/v2_measure-or-guess-evaluation.md:112)
  An entirely failed task receives the same training mean for every participant, making Spearman correlation undefined. This is a concrete case: the source notes report no valid OpenCap Y-Balance scores. Consequently, the task average or bootstrap can become undefined; silently dropping these tasks would reward failure and give methods different evaluation sets.
  Recommendation: Prespecify handling of constant predictions, constant references, ties, and degenerate bootstrap samples. Retain a common task set and explicitly assign an operational zero-association value to all-fallback predictions, or choose a ranking loss defined for constant predictions.
- [high] The power calculation does not estimate power for the primary outcome (docs/ideas-claude/v2_measure-or-guess-evaluation.md:118)
  The formula assumes an average of independent participant-level differences, but the primary outcome is a difference of correlations computed across participants. No participant-level contribution or influence estimator is defined. Switching only cheaper methods to cross-validation over 171 people also fails to increase power for the stated paired agent-versus-predictor comparison.
  Recommendation: Estimate power by simulating or resampling complete participant task vectors and applying the actual joint rank/skill decision rule, including seed variability. If switching designs, evaluate all primary comparators on identical outer folds with development repeated inside each training partition.
- [high] Development-wide normalization still leaks across validation folds (docs/ideas-claude/v2_measure-or-guess-evaluation.md:91-92)
  Recomputing extrema from all development participants protects the fixed test set but includes each validation fold in the training-target definition. Those contaminated fold results drive stage selection and the power decision. Likewise, allowing examples from any development fold does not exclude the fold currently being evaluated.
  Recommendation: Fit endpoints, fallback means, prompt examples, and training trajectories using only each split's training participants. Use all 128 development participants only for final fitting. Specify nested selection if cross-validation replaces the final test.
- [high] The evaluation does not distinguish motion measurement from appearance shortcuts (docs/ideas-claude/v2_measure-or-guess-evaluation.md:40)
  Rank agreement, skill, and slope describe predictions, not which evidence produced them. The source notes report an overall StaBLE–age correlation of −0.76, making an appearance-based shortcut plausible without establishing that it occurs. A model could improve these metrics using apparent age or physique while ignoring task motion; low slope also does not itself demonstrate video neglect.
  Recommendation: Add demographic-only and static-frame baselines, plus prespecified motion/evidence perturbations appropriate to each feature. Perturb cached tool evidence consistently with video inputs. Require movement-sensitive feature accuracy before describing the result as measurement.
- [high] The expert pipeline does not isolate the value of learned tool use (docs/ideas-claude/v2_measure-or-guess-evaluation.md:50-52)
  The agent receives specialist tool outputs and feature-based trajectory selection, whereas the direct predictor learns scores from video. A deterministic expert pipeline controls for hand-written engineering but not for a learned predictor receiving the same information. An agent win could therefore reflect better inputs or supervision without any benefit from adaptive analysis, leaving the application-driven ML contribution unidentified.
  Recommendation: Add a non-agent predictor using the same cached outputs and feature supervision, and ablate adaptive calls against a fixed-call learned system. State the general learning hypothesis these matched comparisons would establish.
- [medium] The sequential ladder cannot identify which improvement method contributes most (docs/ideas-claude/v2_measure-or-guess-evaluation.md:62-64)
  Later stages inherit earlier optimization and consume additional computation, while no common budget or continuation control is specified. Their marginal gains depend on stage order and starting checkpoint. Three seeds and corrected significance tests cannot separate an algorithmic benefit from simply spending more search or training compute.
  Recommendation: For each added stage, compare against spending the same additional budget on the preceding method. Charge proposer calls, failed searches, prerequisite training, tool execution, and inference; report accuracy–cost frontiers or narrow claims to this particular sequence.
- [medium] The ledger still does not identify which trial and reference are being evaluated (docs/ideas-claude/v2_measure-or-guess-evaluation.md:80)
  The source notes distinguish 3,322 trials, safety nonattempts assigned zero, age-imputed features, and retained reconstruction errors. A participant–task row with a generic reference field does not specify trial selection or aggregation, nor distinguish observed from synthetic targets. Videos could consequently be paired with another attempt's features or evaluated against demographic imputations as though they were measurements.
  Recommendation: Add linked trial/video/reference identifiers, a fixed repeated-trial aggregation rule, and explicit nonattempt, imputation, and reconstruction-quality flags. Define primary measurement eligibility and sensitivity analyses before training.
- [medium] One final evaluation does not undo prior test-set exposure (docs/ideas-claude/v2_measure-or-guess-evaluation.md:94)
  The same 43 participants already supplied six benchmark results and the Y-Balance failure that motivates the proposed fallback. They remain held out of fitting, but their outcomes have informed research design. Logging one additional evaluation does not close adaptive test reuse or make the resulting evidence untouched confirmation.
  Recommendation: Disclose the split as a reused benchmark and frame results accordingly. Reserve genuinely untouched participants or an external cohort for confirmation if available; otherwise explicitly limit confirmatory claims.
- [medium] The cache assumption conflicts with adaptive tool settings (docs/ideas-claude/v2_measure-or-guess-evaluation.md:102)
  The agent is supposed to choose tools and settings, and point tracking depends on selected points. One cached output per video cannot represent every such request. Either the action space is narrower than advertised or additional executions invalidate the claim that repeated runs cost only model time, leaving the thirteen-week compute plan unsupported.
  Recommendation: Define fixed versus adaptive tool arguments, cache by video/version/complete arguments, and budget cache misses. Provide measured rollout and training throughput on available hardware, with a dated scope-reduction decision.

Next steps:
- Freeze a trial-linked dataset manifest, fold-local preprocessing, and a statistical protocol that handles failures and estimates power for the actual outcome.
- Add verified feature evaluation, motion-dependence controls, and matched-information and matched-budget baselines before launching optimization.
exit=0
```
