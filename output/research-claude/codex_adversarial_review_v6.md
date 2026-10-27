# Codex adversarial review of v6 (verbatim)

Target: `docs/ideas-claude/v6_simplified-reward-what-can-be-checked.md`. Progress lines removed; findings verbatim.

```text
# Codex Adversarial Review

Target: working tree diff
Verdict: needs-attention

Do not launch confirmatory experiments unchanged. The verifier permits reference copying, task-transfer evaluation is incomplete, and the scoring and statistical protocols cannot yet support the claimed learning effect.

Findings:
- [high] The teacher can copy reference answers while passing every probe (docs/ideas-claude/v6_simplified-reward-what-can-be-checked.md:37)
  A permitted function can recognize the current video's tool-array fingerprint, return its privileged reference value, and execute a correct feature computation on every other input. This passes replay, range, known-answer probes and cross-video filtering while copying the current answer. Thus neither 'cannot copy' nor 'removes solutions tuned with hindsight' follows from the proposed checks.
  Recommendation: Restrict feature programs against participant-specific branches and label literals; audit annotation inputs; add identity-branch and annotation-encoding attacks. Evaluate complete policies on hidden participants and describe probe passing as tested behavior, not proof of measurement.
- [high] Held-out tasks lack a defined verification and calibration protocol (docs/ideas-claude/v6_simplified-reward-what-can-be-checked.md:88-90)
  These tasks exclude their videos from every training stage, but verification requires four labeled videos of the same task, and scoring requires task-specific endpoints and fallback means. No evaluation-time support phase supplies these artifacts. Either the checker cannot operate as specified, or labeled task adaptation is introduced without being accounted for in S5's transfer interpretation.
  Recommendation: Specify disjoint support and query participants for held-out tasks, exactly which support labels the harness may use, and when calibration occurs. Report this as supervised task adaptation, or use label-free checks and raw-unit feature errors for zero-shot transfer.
- [high] Evaluation-time replacement can confound the reward comparison (docs/ideas-claude/v6_simplified-reward-what-can-be-checked.md:109)
  The proposal replaces rejected features with training means, but never specifies whether score-only and no-check arms receive the same transformation during evaluation. Different policies would mix learning gains with reference-calibrated rejection and shrinkage. Common handling of partial submissions, malformed outputs and timeouts is also absent from the final evaluation definition.
  Recommendation: Define an arm-by-arm training-loss and evaluation-policy table. Use identical primary scoring and failure handling across arms; report checked deployment scores, raw feature accuracy and checked coverage separately.
- [high] Three-seed resampling does not establish calibrated method-level inference (docs/ideas-claude/v6_simplified-reward-what-can-be-checked.md:113)
  Only three seeds per reward are budgeted, without specifying interval construction or checking coverage. In the seed-dominated limit, a paired percentile bootstrap of three independent symmetric seed effects yields the observed minimum and maximum; its null coverage is 75%, not 95%. Additional participants cannot fix this. Resampling existing methods' predictions also does not establish power for the proposed RL seed variability.
  Recommendation: Specify the interval algorithm, increase independent training runs, and simulate null coverage and power with participant and seed variability. Require the skill-difference confidence bound to exceed −0.02; otherwise restrict inference to the fitted agents.
- [medium] Malformed submissions can earn more reward than valid attempts (docs/ideas-claude/v6_simplified-reward-what-can-be-checked.md:140-141)
  Valid rewards are unbounded below, while malformed submissions receive −2. For example, average feature error 0.9 and annotation error 12 seconds produce −2.1 even without verification penalties. GRPO therefore prefers malformed output to that attempt, creating an avoidable escape route on difficult examples.
  Recommendation: Define explicit abstention separately from malformed output and ensure malformed responses cannot outrank valid submissions, using a bounded training reward or validity-first ordering. Retain uncapped errors for the mathematical bound and evaluation.
- [medium] The comparisons do not isolate adaptive tool selection (docs/ideas-claude/v6_simplified-reward-what-can-be-checked.md:66)
  Beating an expert pipeline or a tool-feature regressor can reflect the VLM's capacity, feature computation or training procedure rather than adaptive tool selection. No comparison holds the VLM, supervision and available evidence fixed while removing adaptive calls. S3 therefore cannot establish the specific agent contribution attributed to it.
  Recommendation: Add a fixed-call version of the same VLM with matched training and inference budgets. Attribute gains to adaptive routing only if that contrast supports them; otherwise narrow the ML contribution to the reward or feature-computation procedure.
- [medium] The compute estimate omits the stated fold-level training workload (docs/ideas-claude/v6_simplified-reward-what-can-be-checked.md:117)
  The budget enumerates nine RL runs, while Sections 7–8 describe fold-local development across five folds. If all three rewards and three seeds follow that design, development requires 45 RL fits before nine final fits, excluding continuation searches and teacher generation. A cheaper development design is possible, but none is specified, so the claimed budget and timeline are not substantiated.
  Recommendation: Provide a run matrix covering folds, seeds, budgets, teacher generation, continuation controls and final fitting. Either budget the full workload or explicitly restrict exploratory development to fewer fits before the final replicated comparison.
- [medium] Failure to outperform cannot establish absence of shortcut learning (docs/ideas-claude/v6_simplified-reward-what-can-be-checked.md:130)
  The proposed negative-result conclusion is invalid: equal performance could mean both arms stopped measuring, the verifier failed, or the experiment lacked power. This is especially consequential because the stage gate permits proceeding below the stated 80% power target. A nonsignificant superiority comparison cannot show that outcome rewards preserved measurement behavior.
  Recommendation: Interpret a null comparison as no demonstrated advantage. Claim preserved measurement only with prespecified behavioral accuracy criteria and an adequately powered equivalence or noninferiority analysis.

Next steps:
- Freeze the verifier threat model, held-out-task support protocol and common evaluation policy before generating demonstrations.
- Reconcile the run budget with a calibrated statistical design, then preregister mechanism claims and permissible negative-result conclusions.
exit=0
```
