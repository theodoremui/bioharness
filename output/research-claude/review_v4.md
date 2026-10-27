# Review of v4: "Seeing More While Learning, Seeing Less When Tested"

Reviewed file: `docs/ideas-claude/v4_privileged-teacher-and-budgeted-levers.md`
Rubric: see `review_v0_codex-baseline.md`.

## Scores

| Dimension | v1 | v2 | v3 | v4 | Rationale for v4 |
|---|---|---|---|---|---|
| D1 Significance (15%) | 6 | 6.5 | 7.5 | 8 | Privileged supervision used twice (reward and teacher), with appearance controls, is a clear, general recipe for any setting where a better sensor exists only at training time. |
| D2 Novelty (15%) | 5 | 5 | 7 | 7.5 | The action-restricted privileged teacher with a cross-video validity filter is a concrete answer to the "privilege illusion" problem in agent distillation. |
| D3 Research question (10%) | 7 | 8 | 8 | 7.5 | The primary contrast now changes two things at once (warm start and reward), so a win cannot be attributed to either without the secondary analysis. |
| D4 Soundness (10%) | 5 | 6 | 7 | 7.5 | Material-response verification closes the trivial-dependence loophole. The frame-shuffle test is invalid for features that do not depend on frame order (a peak angle is the same in any order). |
| D5 Experimental design (10%) | 5 | 7 | 8 | 8 | Continuation controls and budget tiers are the right idea, but the arm-by-tier matrix is large and not prioritized. |
| D6 Statistics and leakage (10%) | 5 | 7.5 | 8.5 | 8.5 | Degenerate cases are defined, power is simulated with the real decision rule, everything is fitted per fold. |
| D7 Feasibility (10%) | 7 | 7 | 6.5 | 6.5 | The minimum viable scope helps; total arm count still threatens the calendar. |
| D8 Clarity (10%) | 7 | 8 | 8 | 7 | The document has become long and technical; verification and the teacher take effort to follow without a picture. |
| D9 Story arc (5%) | 5 | 7 | 6 | 8 | The stage table with gates reads as a real research journey. |
| D10 Writing (5%) | 7 | 7 | 7 | 7 | Clear; the title is long and slightly cute. |

**Weighted overall: 7.58 / 10** (v3: 7.43). ICML readiness: weak accept. The science is sound, but the proposal is getting heavier faster than it is getting clearer.

## Main critiques

1. **The primary contrast is a package.** Comparing (privileged teacher + verified feature reward) with (plain teacher + score reward) cannot say which change mattered. A 2 × 2 factorial design (teacher type × reward type) answers both questions with the same four arms, and the package contrast becomes one cell comparison within it.
2. **The motion perturbation is wrong for some features.** Shuffling frame order leaves maxima, minima and ranges unchanged, so a correctly measuring agent would legitimately return the same peak ankle angle. The test should be limited to features that depend on order (speeds, durations, sway paths) or use a perturbation that changes the movement while keeping appearance, such as time-reversal for asymmetric movements or swapping in the same person's video of a different task.
3. **Cost is still passive.** OpenCap Monocular costs minutes per clip, and nothing helps the agent decide when a cheap tool is enough. A model that predicts each tool's likely outcome and error before it is called would let the agent plan, and it doubles as an uncertainty estimate.
4. **No test of generalization to new tasks.** If the agent has learned how to measure, it should handle a task whose feature definitions it has never trained on. A leave-task-out split, fixed in the ledger before development, is the natural ICML-style generalization test.
5. **Annotations are an unverified channel.** The agent may set `task_start` and `task_end` by looking at frames. The probe check verifies the code but not these choices. Annotation accuracy against the three-camera segmentation should be reported, and the reward should include it during training.
6. **Too many arms.** Prompt search, harness search, two warm starts, three RL rewards, a cost arm, three budget tiers and three seeds produce more runs than ten weeks can hold. The proposal should name the confirmatory arms (four or five) and mark the rest exploratory, with one seed.
7. **Readability.** A newcomer needs one figure that shows what is used during training only, what the agent sees, and where the sealed set sits.

## Suggestions for v5

1. Recast the primary analysis as a 2 × 2 factorial (teacher × reward) at matched compute, with the full-versus-control cell contrast as primary.
2. Fix the motion test: order-dependent features only, plus a same-person different-task swap.
3. Add a **tool-outcome world model** trained on cached development outputs, used for cost-aware tool choice and as an uncertainty signal.
4. Add a **leave-task-out** transfer test with three held-out tasks fixed before development.
5. Reward and report annotation accuracy.
6. Trim the arm list to a confirmatory core and an exploratory periphery.
7. Plan the pipeline figure.

## Codex adversarial review of v4 and its disposition

Verbatim output: `codex_adversarial_review_v4.md`. Verdict: needs-attention.

| Codex finding | Severity | Response |
|---|---|---|
| Annotations bypass verification (a function returning `task_end − task_start` passes probes that use expert annotations) | high | Partly addressed in v5–v6 (annotation error rewarded and reported). Fully addressed in v7: a **required-signal sensitivity test** (perturbing the signal a feature must depend on has to change the output), annotation-only shortcuts in the shortcut suite, and annotation probes on development videos at evaluation. v7 also states that the check certifies computation, and that the agent's choice of time window is measured separately. |
| Holdout enlargement leaks | high | Addressed in v5: 60 reserved before any analysis. |
| Sampling and reward eligibility contradictory | high | Addressed in v5: status-by-operation eligibility table. |
| No common scoring rule for failures and partially verified submissions | high | Addressed in v7: one scoring policy for every method. The primary evaluation uses features **as submitted** (no checking gate), so the checked arm is not favoured by construction; checked scores and coverage are reported separately. |
| Primary comparison is a package | high | Addressed in v5: primary contrast changes only the reward; teacher effect measured at the SFT stage; replicated no-check arm. v7 restores a fixed-call ablation of the same VLM at inference (no extra training). |
| Clipping breaks the bound | medium | Addressed in v5 (uncapped errors, fallback plus penalty; Appendix B in v6). |
| Confirmatory cohort not provably untouched | medium | Addressed in v5 (retrospective re-split, audit, prospective follow-up). |
| Frame shuffling is not a valid movement test | medium | Addressed in v5 (time-scaling interventions with feature-specific predicted responses; invariant features serve as negative controls in v7). |
