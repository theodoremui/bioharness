# Review of v7 (final): "Rewarding Only What Can Be Checked"

Reviewed file: `docs/ideas-claude/v7_final_rewarding-what-can-be-checked.md`
Figure: `docs/ideas-claude/figures/training_pipeline_v7.svg`
Rubric: see `review_v0_codex-baseline.md`.

## Scores

| Dimension | v0 | v1 | v2 | v3 | v4 | v5 | v6 | v7 | Rationale for v7 |
|---|---|---|---|---|---|---|---|---|---|
| D1 Significance (15%) | 4 | 6 | 6.5 | 7.5 | 8 | 8.5 | 8.5 | 8.5 | The general recipe is stated in the abstract: reward checked measurements whenever a better instrument exists only during training. |
| D2 Novelty (15%) | 4 | 5 | 5 | 7 | 7.5 | 8 | 8 | 8.5 | The check is now a coherent mechanism (replay including a noisy copy, required-signal test, known-answer probes, restricted programs) validated against a named shortcut suite. |
| D3 Research question (10%) | 6 | 7 | 8 | 8 | 7.5 | 8 | 8.5 | 8.5 | One primary contrast and five confirmatory comparisons, each with a stated purpose and an honest limit. |
| D4 Soundness (10%) | 4 | 5 | 6 | 7 | 7.5 | 8 | 8 | 8.5 | The evaluation no longer favours the checked arm; the reward ranks malformed answers last; the bound is stated for the uncapped penalty. |
| D5 Experimental design (10%) | 6 | 5 | 7 | 8 | 8 | 8.5 | 8.5 | 8.5 | Strong controls; adaptive routing is explicitly left unisolated, which is honest but leaves one interesting question exploratory. |
| D6 Statistics and leakage (10%) | 7 | 5 | 7.5 | 8.5 | 8.5 | 9 | 9 | 9.5 | Seven paired seeds, an interval for the expected gain over retraining whose coverage is checked by simulation, and a fixed testing order; a defined task-calibration set for transfer; one scoring policy for all methods. |
| D7 Feasibility (10%) | 3 | 7 | 7 | 6.5 | 6.5 | 6.5 | 7 | 7 | A run matrix makes the cost visible (about 5,600 H100-hours); the reduced scope is defined, but the default remains ambitious for thirteen weeks. |
| D8 Clarity (10%) | 5 | 7 | 8 | 8 | 7 | 6.5 | 8.5 | 8.5 | Keeps v6's running example and worked trajectory; the added safeguards are explained in plain words before the appendix gives numbers. |
| D9 Story arc (5%) | 3 | 5 | 7 | 6 | 8 | 8 | 8 | 8.5 | The stage table plus a paragraph on how each outcome routes to the next stage. |
| D10 Writing (5%) | 6 | 7 | 7 | 7 | 7 | 7 | 8 | 8.5 | Contrastive constructions removed, terminology unified ("checked"), American spelling throughout, a few natural dashes. |

**Weighted overall: 8.45 / 10** (v6: 8.23; v0: 4.75). ICML readiness: accept-leaning for the Application-Driven ML track, conditional on executing Stage 0 as written.

## What makes v7 compelling for ICML

1. **A clear, general thesis.** Reward the measurements, and only those that can be checked. It applies wherever a better instrument exists at training time (multi-camera capture, laboratory assays, high-resolution imaging) and a deployable instrument is cheaper and noisier.
2. **A test bed where intermediate steps can be verified.** Few agent benchmarks have a reference for every intermediate quantity. StaBLE does, which lets the paper study process-level supervision for tool-using agents with ground truth instead of learned judges.
3. **An evaluation that cannot be passed by guessing or by reading appearance.** Rank agreement, skill against the constant guess, calibration slope, demographic and single-frame controls, and time-scaling interventions together separate measuring from guessing.
4. **Honest scope.** Retrospective re-split disclosed, transfer described as transfer with labelled calibration, adaptive routing claims withheld, and a null result interpreted carefully.

## Remaining weaknesses (accepted, with reasons)

1. **Compute.** About 5,600 H100-hours is a lot for a thirteen-week project. The reduced scope (six tasks) keeps the primary contrast alive, which is the claim that matters.
2. **Adaptive tool choice is not isolated.** Isolating it would need a separately trained fixed-call agent with seven seeds, roughly doubling RL cost. The paper's thesis concerns rewards rather than routing, so this stays exploratory.
3. **The confirmatory cohort is retrospective.** Prospective confirmation on newly recorded participants is the right follow-up and is named as such.
4. **Time marks remain a perception step.** The check certifies computation given the marks; timing error is measured and rewarded, but a wrong mark on a new video still yields a wrong feature. That is the honest boundary of what the check can promise.

## Codex adversarial review of v7 and its disposition

Verbatim output: `codex_adversarial_review_v7.md`. Verdict: needs-attention. Because v7 is the last version in the series, its findings were fixed in v7 itself (v1–v6 are untouched); the scores above refer to the fixed v7.

| Codex finding | Severity | Response (applied to v7) |
|---|---|---|
| The required-signal test rejects correct StaBLE computations (threshold-crossing features are invariant to scaling and shifting) | high | Adopted: two to four perturbations per feature, with the expected change or invariance taken from running StaBLE's released feature code on the same perturbation of the reference curves; validated per feature on development videos before RL. |
| The reward scored substituted values while the primary evaluation scores submitted values, so a worse unchecked answer could earn more | high | Adopted: training error is computed from submitted values in every arm, the check adds a penalty on top, and Appendix B states the bound for the submitted values used in the primary evaluation. |
| The sign test does not establish mean improvement across runs | high | Adopted: the estimand is now the expected improvement over retraining; the interval combines seed-to-seed and participant uncertainty (t-distribution, Satterthwaite degrees of freedom); its coverage is simulated under symmetric, skewed and failed-run seed distributions and widened if needed; the sign test is dropped as a decision criterion. |
| Five seeds cannot pass Holm's first threshold for S1 | high | Adopted: a fixed testing order (primary, then S1 at 5%, then Holm over S2–S5) and seven paired RL seeds; S3–S5 are stated as claims about the delivered agent with participant-bootstrap p-values. Compute updated to about 5,600 H100-hours. |
| Time-scaling targets ignore caps (hold time is capped at five seconds) | medium | Adopted: expected responses come from slowing the reference trajectories and rerunning StaBLE's released feature code, never from hand-computed ratios. |
