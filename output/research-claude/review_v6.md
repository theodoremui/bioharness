# Review of v6: "Rewarding Only What Can Be Checked"

Reviewed file: `docs/ideas-claude/v6_simplified-reward-what-can-be-checked.md`
Rubric: see `review_v0_codex-baseline.md`.

## Scores

| Dimension | v2 | v3 | v4 | v5 | v6 | Rationale for v6 |
|---|---|---|---|---|---|---|
| D1 Significance (15%) | 6.5 | 7.5 | 8 | 8.5 | 8.5 | Unchanged science; the one-line thesis makes the general lesson easy to carry away. |
| D2 Novelty (15%) | 5 | 7 | 7.5 | 8 | 8 | Same mechanisms, now stated so a reviewer can see what is new in one paragraph. |
| D3 Research question (10%) | 8 | 8 | 7.5 | 8 | 8.5 | Five confirmatory comparisons, each with a one-line purpose. The SMART paragraph is explicit. |
| D4 Soundness (10%) | 6 | 7 | 7.5 | 8 | 8 | Two gaps remain: an annotation-only function can still pass the probes, and the document does not say whether the check is applied when scoring the final-score arm. |
| D5 Experimental design (10%) | 7 | 8 | 8 | 8.5 | 8.5 | The fixed-call ablation of the same VLM was dropped between v3 and v6; without it, "adaptive tool use" is not separately tested. |
| D6 Statistics and leakage (10%) | 7.5 | 8.5 | 8.5 | 9 | 9 | Per-stage table makes data shape and leakage visible at each step. The harness-search cap ("a fixed number of queries") needs a number. |
| D7 Feasibility (10%) | 7 | 6.5 | 6.5 | 6.5 | 7 | Clearer budget and minimum scope. |
| D8 Clarity (10%) | 8 | 8 | 7 | 6.5 | 8.5 | The rise-to-toes example and the worked trajectory make every concept concrete. |
| D9 Story arc (5%) | 7 | 6 | 8 | 8 | 8 | The stage table is complete; one short paragraph on how results route between stages would make the loop explicit. |
| D10 Writing (5%) | 7 | 7 | 7 | 7 | 8 | Much more natural. A few contrastive constructions remain ("as opposed to predicting a plausible score"; "rather than outcomes"), and "checked" and "verified" are used interchangeably. |

**Weighted overall: 8.23 / 10** (v5: 7.88). ICML readiness: accept-leaning. What remains is a small number of precise fixes rather than structural change.

## Main critiques

1. **Evaluation could favour the checked arm by construction.** If unchecked features are replaced by averages at test time for every agent, the final-score arm, which was never trained to pass the check, is penalized by the evaluation rule itself. The primary comparison should use features as submitted, with checked scores and checked coverage reported separately.
2. **Annotation-only functions.** A duration feature can be faked by returning `task_end − task_start`; on probes the expert annotations make it look right. The check needs a required-signal test: perturbing the signal that a feature must depend on (for example, the center-of-mass curve) must change the output.
3. **Adaptive tool use is no longer tested.** Restore the fixed-call ablation: the final agent's weights with a harness that hands it a fixed set of default tool outputs and allows no further calls. It needs no extra training.
4. **Terminology.** Use "checked" throughout and define it once.
5. **Harness-search cap.** State the number of validation evaluations harness and prompt search may use (for example 20) and charge them to the budget.
6. **World-model evaluation.** Say how the tool-outcome model itself is judged (rank correlation between predicted and realized errors on sealed data; coverage of calibrated intervals).
7. **Remaining stylistic contrasts.** Reword the two "X rather than Y" constructions.

## Suggestions for v7

1. Fix the evaluation policy (features as submitted for the primary analysis; one policy for every method).
2. Add the required-signal sensitivity test and annotation shortcuts to the check and its validation suite; add annotation probes at evaluation.
3. Restore the fixed-call ablation.
4. Add the final title options, tighten the abstract, unify terminology, and run a style audit for the patterns listed in the brief.
5. Fold in Codex's v5 and v6 findings.

## Codex adversarial review of v6 and its disposition

Verbatim output: `codex_adversarial_review_v6.md`. Verdict: needs-attention.

| Codex finding | Severity | Response in v7 |
|---|---|---|
| A function can recognize the current video and return the privileged reference while computing honestly elsewhere | high | Adopted: replay on a noisy copy of the cited outputs (a memorizing branch takes a different path and fails), program restrictions (fixed array library, no branching on identity, limited literals), and an identity-branch program in the shortcut suite. Passing the check is described as tested behaviour, not proof of measurement. |
| Held-out tasks lack a verification and calibration protocol | high | Adopted: a task-calibration set of development participants' references for the three tasks supplies endpoints, fallback averages and probes for every method; sealed participants are the query set; the test is described as transfer with labelled calibration and no training on the task. |
| Evaluation-time replacement can confound the reward comparison | high | Adopted: arm-by-arm table of training reward and evaluation policy; primary evaluation uses submitted features for every arm. |
| Three seeds do not give calibrated method-level inference | high | Adopted: five paired seeds, a two-part rule (participant-bootstrap interval for the seed-averaged agents and a sign test across paired seeds), and a Stage 0 simulation of false-positive rate and power. |
| Malformed submissions can outrank valid ones | medium | Adopted: training reward is `−min(P, 3)` and malformed output gets −4, so it always ranks last; the bound is stated for the uncapped penalty. |
| Comparisons do not isolate adaptive tool selection | medium | Adopted by narrowing the claim: S3 is stated not to show adaptive tool choice; the fixed-call ablation is exploratory and no confirmatory claim about adaptive routing is made. |
| Compute omits fold-level workload | medium | Adopted: a run matrix. Expensive stages use one development split with one seed; only final models are replicated. Total about 5,300 H100-hours, with a reduced scope below 3,000. |
| A null result cannot show that outcome rewards preserved measurement | medium | Adopted: a null is reported as "no demonstrated advantage", with behavioural measures used to interpret it. |
