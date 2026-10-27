# Codex adversarial review of v0 (verbatim)

Command: `/codex:adversarial-review` via codex-companion.mjs, focus text targeting `output/research-codex/biomechanical_agent_proposal.md`. Progress lines removed; findings verbatim.

```text
# Codex Adversarial Review

Target: working tree diff
Verdict: needs-attention

Do not proceed unchanged. The reference dataset is unsecured, the statistical decision rule omits search uncertainty, and the experiments could declare success without establishing useful learned transfer.

Findings:
- [high] The confidence interval does not support a method-level superiority claim (output/research-codex/biomechanical_agent_proposal.md:90-92)
  Averaging five searches before resampling participants conditions on those particular searches. A lucky search affects every participant, so additional participants cannot resolve that uncertainty. For illustration, run-level improvements of +20, 0, 0, 0, and −15 percentage points shared across participants produce a participant-only interval of [+1, +1], while resampling runs gives approximately [−9, +12]. Reporting run variation separately does not fix the positive-interval decision rule.
  Recommendation: Define whether inference concerns fixed fitted programs or the stochastic search method. For the latter, incorporate independent searches and participants as crossed sources of uncertainty; include workflow-family uncertainty if claiming generalization beyond the tested families. Base power calculations and the success decision on that estimand.
- [high] The essential reference dataset is not established by the sources (output/research-codex/biomechanical_agent_proposal.md:86)
  The supplied source notes establish StaBLE smartphone recordings and derived features, but do not establish this project's access to synchronized independent foot-contact recordings. This paragraph names an instrument type rather than a dataset and supplies no eligible participant or stride counts. Consequently, neither the primary experiment nor its power is currently demonstrably feasible. Starting the twelve-week clock only after access, as line 17 does, leaves the largest dependency outside the schedule.
  Recommendation: Name the dataset, access status, reference sensor, synchronization procedure, and eligible participant/stride counts by split. Add a dated access milestone and a power-based minimum sample requirement, with a concrete fallback or stop decision if either fails.
- [high] The success rule permits a positive result despite domination by ordinary engineering (output/research-codex/biomechanical_agent_proposal.md:92-94)
  The primary comparison is against code search, while expert and full-retention workflows are only listed as additional comparisons. Thus the declared support criterion can pass even when a fixed program answers all three questions more accurately and cheaply. These questions require only simple calculations over timestamps; mean and variance can even be preserved with a constant-size statistical summary. A win over another search procedure would then establish neither an application benefit nor a need to learn preservation requirements.
  Recommendation: Make the expert and full-retention baselines part of the decision criterion. Require a prespecified useful accuracy or total-cost advantage, including amortized search cost. If learning is dominated, stop the proposed contribution or explicitly reframe the work as a negative result.
- [high] The workflow holdout lacks an enforceable definition (output/research-codex/biomechanical_agent_proposal.md:82)
  The test split is defined by operation combinations, but the optimizer constructs complete programs and can retrieve original contacts. The proposal does not define fixed test interfaces or evidence-access constraints, nor exclude held-out compositions from development search. A nominally unfamiliar workflow could therefore have been synthesized during training or bypassed by the same contact-to-standard-deviation routine. This is a protocol vulnerability, not evidence that leakage has already occurred; participant separation alone does not address it.
  Recommendation: Define immutable cases with inputs, available records, interface constraints, and expected outputs. Partition composition families before development, specify how overlap is detected, and log all training evaluations. Explicitly distinguish legitimate retrieval-based recovery from cases that actually exercise unseen composition.
- [medium] The learned component is insufficiently specified to reproduce or assess novelty (output/research-codex/biomechanical_agent_proposal.md:57-62)
  The method supplies human-written templates and prioritizes observed improvements, but never defines the representation of a 'condition,' the score estimator, how an unseen condition receives a ranking, or when a previous check remains valid. These choices determine both the algorithm and its apparent transfer. Since the cited [Meta-Harness](https://arxiv.org/abs/2603.28052v1) already searches code using execution history, naming requirements and caching checks does not by itself establish the additional learning contribution.
  Recommendation: Add executable pseudocode defining inputs, learned state, score updates, unseen-condition behavior, and check-reuse validity. Specify the replacement policy in the ranking ablation, including a fixed human-authored contract policy, and narrow the novelty claim to the mechanism these comparisons can isolate.

Next steps:
- Resolve reference-data access and sample adequacy before committing to the twelve-week execution plan.
- Freeze the algorithm, workflow split, baseline decision criteria, and uncertainty analysis before comparative searches.
exit=0
```
