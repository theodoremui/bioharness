# Codex adversarial review of v7 (verbatim)

Target: `docs/ideas-claude/v7_final_rewarding-what-can-be-checked.md` (state before the final fixes). Progress lines removed; findings verbatim.

```text
# Codex Adversarial Review

Target: working tree diff
Verdict: needs-attention

Do not launch confirmatory experiments unchanged. The checker rejects legitimate measurements, the reward can prefer inaccurate submissions, and the statistical design cannot reliably establish the claimed learning contribution.

Findings:
- [high] The required-signal test rejects correct StaBLE computations (docs/ideas-claude/v7_final_rewarding-what-can-be-checked.md:184)
  Signal dependence does not imply sensitivity to scaling or translation. StaBLE's rise-to-toes hold time uses crossings of relative center-of-mass height thresholds; positive scaling or translation preserves those crossing times. A correct implementation therefore fails this mandatory check, loses training credit, and reduces checked coverage. This follows from the [released feature code](https://raw.githubusercontent.com/stanfordnmbl/stable-analysis/main/get_features/get_features_rtt.py).
  Recommendation: Specify feature-specific transformations and expected responses, including legitimate invariances. For hold time, move the relevant crossing times while preserving amplitude. Validate acceptance separately for every feature before training.
- [high] The reward hides errors that primary evaluation exposes (docs/ideas-claude/v7_final_rewarding-what-can-be-checked.md:200)
  Appendix B computes error after replacing unchecked submissions with training means, whereas primary evaluation uses raw submissions. For one normalized feature with reference and training mean both 0.5, an unchecked submission of 1.4 receives penalty 0.5; a checked submission of 1.1 receives penalty 0.6. Training therefore prefers the less accurate answer. Arbitrarily wrong unchecked values receive the same replacement-based penalty, and the stated bound does not cover primary scores.
  Recommendation: Compute training feature error from submitted values in every arm, then add the check penalty. Reserve substitution for the separately reported deployment policy, and state the bound for the same values used by the primary evaluation.
- [high] The sign-test gate does not establish mean improvement across training runs (docs/ideas-claude/v7_final_rewarding-what-can-be-checked.md:146)
  The participant interval conditions on the fitted runs; the sign test concerns the probability of a positive difference, not its expected magnitude. If method superiority means expected improvement over retraining, consider seed effects of +0.02 with probability 0.95 and −0.38 otherwise: expected improvement is zero, yet all five effects are positive with probability 77.4%. In the seed-dominated limit, the proposed rule can declare success on those draws. Simulating only symmetric seed variation would miss this failure.
  Recommendation: Define whether the estimand is expected improvement, median improvement, or probability of improvement. Match inference to that estimand; for expected improvement, budget sufficient independent runs and validate coverage under skewed and failed-run distributions. Explicitly require a confidence bound for skill noninferiority.
- [high] Five seeds cannot resolve the key mechanism contrast under the planned Holm family (docs/ideas-claude/v7_final_rewarding-what-can-be-checked.md:77-85)
  S1 is the comparison needed to distinguish the checker from ordinary feature supervision. Applying the stated method-level sign-test safeguard gives a minimum one-sided p-value of 1/32 = 0.03125. Holm's first threshold for five comparisons is 0.01. If S1 is the only real improvement and the other comparisons are nonsignificant, S1 cannot be confirmed regardless of effect size. Omitting the seed safeguard instead leaves its method claim unsupported by the specified participant-only intervals.
  Recommendation: Prespecify a valid p-value for each secondary contrast. Either prioritize S1 through a justified hierarchical testing procedure or increase independent seeds; seven permits a sign-test p-value below 0.01, but power still requires calculation. Update the compute budget accordingly.
- [medium] The time-scaling benchmark assigns incorrect expected answers to capped features (docs/ideas-claude/v7_final_rewarding-what-can-be-checked.md:144)
  Multiplying every duration feature by 1.25 does not preserve StaBLE's feature definitions. The [released rise-to-toes implementation](https://raw.githubusercontent.com/stanfordnmbl/stable-analysis/main/get_features/get_features_rtt.py) caps hold time at five seconds. A five-second scored hold remains five after slowing, while this benchmark expects 6.25. S4 can consequently penalize correct measurement and reward violation of the scoring definition. Calling the expert pipeline an achievable ceiling does not repair incorrect targets.
  Recommendation: Generate intervention targets by transforming reference trajectories and rerunning the complete feature definitions, including caps, thresholds, and segmentation. Prespecify which features support analytic scaling and which remain invariant.

Next steps:
- Validate feature-specific checker and intervention rules against the released StaBLE computations.
- Align training errors, primary scoring, and the mathematical guarantee.
- Freeze the inferential estimands, multiplicity procedure, and adequately powered run budget before training.
exit=0
```
