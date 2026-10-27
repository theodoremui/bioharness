# Codex adversarial review of v3 (verbatim)

Target: `docs/ideas-claude/v3_measurement-grounded-rewards.md`. Progress lines removed; findings verbatim.

```text
# Codex Adversarial Review

Target: working tree diff
Verdict: needs-attention

Not ready for confirmatory experiments. The verifier can certify guesses, the reward guarantee is false, and unresolved holdout, target-definition and statistical problems could invalidate the central result.

Findings:
- [high] The verifier certifies almost-constant guesses (docs/ideas-claude/v3_measurement-grounded-rewards.md:91-95)
  For a feature with training range [0,1], code returning `0.5 + 1e-8 * mean(input)` reproduces exactly, changes on both probe videos and passes the range check. It therefore earns verified status while effectively guessing a typical value. Replayability and nonzero dependence do not establish that the defined biomechanical feature was measured.
  Recommendation: Test the verifier against explicit shortcut programs. Require feature-specific, materially correct responses to controlled interventions and validated feature computations; otherwise rename the property replayability and remove claims that it blocks guessing.
- [high] The primary ranking estimator is undefined for planned comparisons (docs/ideas-claude/v3_measurement-grounded-rewards.md:152)
  The constant baseline necessarily has undefined Spearman correlation. The same occurs when an entire task falls back to its training mean; the source notes document precisely this failure for OpenCap Y-Balance. Neither the task average nor bootstrap specifies how to handle these cases. Dropping undefined tasks would give methods different evaluation sets and conceal failure.
  Recommendation: Freeze a common task set and explicit rules for ties, constant predictions, constant references, degenerate bootstrap samples and zero skill-score denominators. Assign a declared operational zero-association value to constant predictions or use a ranking loss defined for them.
- [high] The power calculation does not target the primary statistic (docs/ideas-claude/v3_measurement-grounded-rewards.md:167)
  Mean within-task rank agreement is calculated across participants, so there is no defined per-participant correlation difference whose spread supplies the proposed power estimate. The calculation also omits seed variability and the joint rank-superiority/skill-noninferiority decision. Consequently, it cannot establish that either 43 or 60 participants can detect the intended effect.
  Recommendation: Estimate power using complete participant task vectors and seed variation, applying the actual joint decision rule under prespecified effects. State the target power and an exploratory-only or stop decision if the maximum sample remains inadequate.
- [high] The enlargement rule can move evaluated participants into the sealed set (docs/ideas-claude/v3_measurement-grounded-rewards.md:167)
  Section 6.2 allocates all remaining 128 participants to development. After their cross-validated predictions inform the week-2 power decision, enlarging the test set from 43 to 60 necessarily transfers 17 development participants into it. Those participants have already influenced study decisions, contradicting the promised sealed confirmatory evaluation.
  Recommendation: Reserve all 60 potential confirmatory participants before any development analysis. Use only the remaining 111 for power estimation and tuning, and prespecify whether 43 or all 60 reserved participants will be evaluated.
- [high] Participant–task rows do not identify the matching trial and reference (docs/ideas-claude/v3_measurement-grounded-rewards.md:120)
  The source notes report 3,322 motion trials, exceeding the 3,240 participant–task slots. This ledger supplies neither trial/video/reference identifiers nor a repeated-trial aggregation rule. A video could therefore be scored against another attempt's features or an aggregate target, making the feature reward and reported measurement error invalid.
  Recommendation: Add a trial-level manifest linking each Cam0 video to its exact reference reconstruction and feature vector. Specify trial selection and participant–task aggregation before splitting, and reconcile the resulting counts with the pilot.
- [high] The sampler includes rows that cannot support measurement rewards (docs/ideas-claude/v3_measurement-grounded-rewards.md:114)
  Every ledger row is sampled, but the ledger includes 98 safety nonattempts with assigned-zero scores and no performed movement. These rows have neither a task video nor measured feature targets. Section 5.4 masks imputed and flagged references only. The resulting training objective is undefined for nonattempts, while silently removing them would alter the claimed ability distribution.
  Recommendation: Define status-specific eligibility for sampling, normalization, rewards and evaluation. Exclude nonattempts from feature-measurement objectives, report the eligible cohort explicitly, and evaluate safety-assigned scores separately from measured movement.
- [high] Swapping people cannot distinguish motion measurement from appearance prediction (docs/ideas-claude/v3_measurement-grounded-rewards.md:156)
  A video swap changes age, physique and identity alongside movement. An appearance-based predictor could consequently change in the expected direction and pass this diagnostic without measuring motion. This is a plausible confound given the source notes' overall StaBLE–age correlation of −0.76, not evidence that the proposed model already exploits it.
  Recommendation: Add demographic-only and single-frame baselines plus feature-specific motion interventions that preserve appearance. Apply each intervention consistently to the video and all cached evidence, and prespecify the expected feature response.
- [medium] Clipping invalidates the claimed score-error bound (docs/ideas-claude/v3_measurement-grounded-rewards.md:99-105)
  The triangle inequality bounds score error by uncapped feature errors, whereas the reward caps each error at 1. For normalized references [0,0.5,0.5,0.5] and predictions [1.4,0.5,0.5,0.5], every prediction is within the permitted range, but score error is 0.35 and measurement penalty is 0.25. Verification does not restore the asserted guarantee.
  Recommendation: Use uncapped errors if the reward must upper-bound score error, or explicitly restrict the theorem to uncapped error and remove the guarantee about the implemented penalty. State how masking changes the bound.
- [medium] The original training pool is not established as untouched confirmation (docs/ideas-claude/v3_measurement-grounded-rewards.md:124)
  The supposedly unseen pool consists of the pilot's 128 original training participants. Retraining baselines prevents direct reuse of fitted parameters, but does not establish that these participants were absent from prior inspection, preprocessing decisions or model selection. The supplied sources do not support the stronger claim that nobody has looked at this confirmatory cohort.
  Recommendation: Audit and document prior use of candidate participants and derived artifacts. Describe the experiment as a retrospective resplit unless independence from prior development can be established; reserve genuinely new participants for prospective confirmation.
- [medium] The verification contribution receives only an exploratory test (docs/ideas-claude/v3_measurement-grounded-rewards.md:163-165)
  The primary comparison changes both feature supervision and verification. The arm that removes verification—the comparison needed for H3—gets only one seed and is explicitly exploratory. A significant primary result could therefore reflect ordinary feature supervision without establishing the proposed verifier's contribution, leaving the central ML mechanism unidentified.
  Recommendation: Give the measurement-without-verification arm replicated, matched-budget training and prespecify its contrast with the full method. Require that contrast for claims about verification, or narrow the contribution to the combined training objective.

Next steps:
- Repair and adversarially test the verifier and reward mathematics before generating training trajectories.
- Freeze trial-linked eligibility rules and the maximum holdout before development analysis.
- Specify executable estimators, realistic power analysis and replicated mechanism controls before claiming confirmatory evidence.
exit=0
```
