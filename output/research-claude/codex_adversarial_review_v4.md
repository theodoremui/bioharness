# Codex adversarial review of v4 (verbatim)

Target: `docs/ideas-claude/v4_privileged-teacher-and-budgeted-levers.md`. Progress lines removed; findings verbatim.

```text
# Codex Adversarial Review

Target: working tree diff
Verdict: needs-attention

Not ready for confirmatory experiments. The verifier can certify fabricated measurements, holdout enlargement introduces leakage, and the comparisons cannot isolate the claimed learning mechanism.

Findings:
- [high] Unchecked annotations bypass measurement verification (docs/ideas-claude/v4_privileged-teacher-and-budgeted-levers.md:77-80)
  A function returning task_end − task_start can ignore every tool output and reproduce an invented duration. On probes, the harness replaces the agent's annotations with expert annotations, so the same function can pass the material-response check. The teacher's cross-video filter also substitutes expert annotations. Neither check establishes that the submitted annotations came from the current video, contradicting the claim that verification prevents copying reference values.
  Recommendation: Evaluate the complete annotation-producing policy on probes, audit annotation accuracy against blinded timing labels, and test explicit annotation-encoding shortcuts. Describe passing replay checks as reproducibility rather than verified measurement unless feature accuracy is independently established.
- [high] Holdout enlargement moves evaluated participants into confirmation (docs/ideas-claude/v4_privileged-teacher-and-budgeted-levers.md:131)
  Section 6 allocates 43 participants to confirmation and all remaining 128 to development. Section 9 then uses cross-validated development predictions to decide whether confirmation should grow to 60. The additional 17 participants would already have contributed to the power analysis and study decisions. Saying enlargement occurs before training does not resolve this: the specified power procedure itself requires repeated training.
  Recommendation: Reserve all 60 potential confirmatory participants before any development analysis and use only the remaining 111 for planning and tuning. Prespecify an exploratory-only or stop decision if 60 participants remain insufficient.
- [high] Sampling and reward eligibility remain contradictory (docs/ideas-claude/v4_privileged-teacher-and-budgeted-levers.md:113-117)
  The sampler draws all training ledger rows, but the ledger includes safety non-attempts and excluded cases. Non-attempts supply neither performed movement nor measured feature targets. The reward explicitly masks imputed and flagged references only. Saying assigned values never count as measurements does not define how these rows are removed from sampling, normalization, rewards, or evaluation; silently excluding them also changes the represented ability distribution.
  Recommendation: Add a status-by-operation eligibility table covering sampling, endpoint fitting, teacher filtering, rewards and evaluation. Separate safety-assigned scores from measured-feature outcomes and report participant/task counts after each exclusion.
- [high] Failed and partially verified submissions have no common scoring rule (docs/ideas-claude/v4_privileged-teacher-and-budgeted-levers.md:143-147)
  The proposal mentions fallback means and all-fallback predictions but never specifies when fallbacks apply, whether individual rejected features or entire task scores are replaced, or whether score-only and verified arms share the same evaluation rule. This affects an observed failure mode: the source notes report no valid OpenCap Y-Balance scores. Consequently, the primary error, skill and ranking comparisons are not fully defined.
  Recommendation: Prespecify one evaluation policy for timeouts, malformed outputs, missing features and verification failures across all methods. Retain every eligible task example, identify all fallback values explicitly, and exclude fallbacks from measurement coverage.
- [high] The primary comparison cannot identify the proposed mechanism (docs/ideas-claude/v4_privileged-teacher-and-budgeted-levers.md:33-35)
  The primary contrast changes teacher privilege, reward granularity and verification simultaneously. A positive result therefore supports the package only; it cannot establish H2/H3 or explain which component contributes as promised by S2. No explicit arm-by-seed design supplies the required matched-start contrasts. The hard-subset analysis also lacks a same-VLM fixed-call control, so gains cannot be attributed to adaptive analysis.
  Recommendation: Specify teacher-by-reward factorial arms, a matched-start verification-off contrast, and a fixed-call version of the same VLM. Allocate replicated seeds and explicit budgets to the mechanism claims, or narrow the contribution to the combined package.
- [medium] Clipped feature errors invalidate the stated guarantee (docs/ideas-claude/v4_privileged-teacher-and-budgeted-levers.md:94)
  The triangle inequality bounds score error by uncapped feature errors, not the implemented capped penalty. With normalized references [0, 0.5, 0.5, 0.5] and verified predictions [1.4, 0.5, 0.5, 0.5], predictions satisfy the permitted range, but score error is 0.35 while the measurement penalty is 0.25. Masked features introduce a further gap if they remain in the task score.
  Recommendation: Use uncapped errors if the reward must upper-bound score error, or remove the guarantee for the implemented reward. State separately which score and feature set the inequality covers after masking.
- [medium] The sources do not establish an untouched confirmatory cohort (docs/ideas-claude/v4_privileged-teacher-and-budgeted-levers.md:119)
  From the supplied counts, the new 43 participants must come from the pilot's original 128 training participants. The source notes do not establish that these people or their derived artifacts escaped inspection, preprocessing decisions and model selection. Retraining on a new split prevents direct parameter reuse but cannot establish the stronger claim that nobody previously evaluated this cohort.
  Recommendation: Audit prior participant and artifact use. Unless independence is established, describe this as a retrospective resplit with disclosed exposure, and reserve prospective confirmation for genuinely new participants.
- [medium] Frame shuffling cannot establish movement measurement (docs/ideas-claude/v4_privileged-teacher-and-budgeted-levers.md:154)
  A correctly measured peak angle is invariant to frame permutation, so unchanged output can incorrectly refute H5. Conversely, shuffled frames can disrupt temporal reconstruction and change an incorrect predictor's output without demonstrating meaningful measurement. Merely observing changed or unverifiable features is therefore neither necessary nor sufficient evidence for the central movement claim.
  Recommendation: Define feature-specific interventions and expected responses. For example, controlled time scaling should scale durations and inversely scale speeds while preserving angles. Test quantitative agreement with these expectations and retain invariant features as negative controls.

Next steps:
- Freeze the maximum holdout, audit prior exposure, and specify eligibility and failure handling before development analysis.
- Repair the verifier and reward mathematics using explicit shortcut counterexamples.
- Prespecify replicated mechanism controls and feature-specific movement tests before committing the training budget.
exit=0
```
