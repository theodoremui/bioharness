# Codex adversarial review of v5 (verbatim)

Target: `docs/ideas-claude/v5_world-model-transfer-and-known-answer-verification.md`. Progress lines removed; findings verbatim.

```text
# Codex Adversarial Review

Target: working tree diff
Verdict: needs-attention

Do not launch confirmatory runs unchanged. The verifier can certify fabricated timings, held-out-task evaluation lacks required inputs, and unresolved scoring and uncertainty rules threaten the central claims.

Findings:
- [high] Expert probe annotations conceal fabricated annotations on the current video (docs/ideas-claude/v5_world-model-transfer-and-known-answer-verification.md:71-77)
  The probes replace the agent's annotations with expert annotations. Consequently, a function returning task_end − task_start can ignore the video, reproduce an invented current-video duration, and pass every probe using correct expert timings. The teacher filter makes the same substitution. Training-time annotation penalties do not establish annotation correctness at inference, so passing these checks cannot support the claim that reference numbers cannot be copied or that the submitted measurement is verified.
  Recommendation: Test the complete annotation-producing policy on probes, add annotation-encoding shortcuts to verifier validation, and independently evaluate current-video timing accuracy. Until then, describe verification as a check of computation conditional on annotations.
- [high] Held-out tasks lack the calibration data required to execute evaluation (docs/ideas-claude/v5_world-model-transfer-and-known-answer-verification.md:125-131)
  The eligibility table prohibits endpoint fitting for held-out tasks, while scoring requires task-feature endpoints, fallback means, and training ranges. Verification additionally requires four labelled development videos of the same task. Section 6.2 withholds those tasks through development, leaving these inputs undefined. Introducing task-specific labelled probes at confirmation would instead make the deployed system use labelled examples of the supposedly unseen tasks.
  Recommendation: Specify a complete transfer protocol: either use independently fixed scales and checks requiring no held-out-task labels, or reserve an explicit task-calibration set shared across methods and describe the experiment as transfer with labelled calibration.
- [high] Arm-dependent scoring can confound the reward comparison (docs/ideas-claude/v5_world-model-transfer-and-known-answer-verification.md:83-87)
  The verified arm substitutes training means for rejected features, whereas both controls score submitted values. Section 8 never establishes whether this difference persists during evaluation or defines common handling of missing features, malformed submissions, and timeouts. If the training scoring rules carry over, identical raw predictions can receive different test scores solely because one arm gets verifier-based replacement. The result would mix learning effects with postprocessing effects.
  Recommendation: Freeze one primary evaluation policy across arms, including identical failure handling. Evaluate submitted features through the same scoring formula, and separately report verifier-gated deployment scores, replacement rates, and measurement coverage.
- [high] Three-seed bootstrapping does not establish nominal confidence (docs/ideas-claude/v5_world-model-transfer-and-known-answer-verification.md:164-168)
  The confirmatory arms have only three seeds, yet superiority relies on a 95% crossed-bootstrap interval without specifying or validating its construction. A standard independent-seed percentile implementation produced positive intervals in 9.1% of 5,000 seed-dominated null simulations, versus a nominal positive tail of 2.5%. This is a counterexample, not an estimate of this study's actual error rate. Participant resampling cannot repair insufficient information about training variability, and SFT seed variation does not establish GRPO variability.
  Recommendation: Specify seed pairing and interval construction, validate false-positive rates and power under plausible GRPO variability, and budget enough independent runs to support method-level inference. Otherwise restrict conclusions to the fitted agents.
- [medium] The intervention contrast compares feature accuracy with score accuracy (docs/ideas-claude/v5_world-model-transfer-and-known-answer-verification.md:154)
  S7 measures the agent's response as the fraction of individual features satisfying a ratio tolerance, but evaluates the direct predictor through an aggregate score change. These are different outcomes: incorrect feature changes can cancel in the score while failing both feature-level checks. Moreover, correct time-scaling behavior alone does not establish measurement; duration-based guesses and constant angle predictions can obey the specified transformations.
  Recommendation: Use the same score-change statistic and tolerance for the confirmatory comparison. Report feature responses separately, include timestamp-only shortcut controls, and require absolute feature accuracy alongside transformation consistency before claiming movement measurement.
- [medium] The conformal calibration fold is reused in final fitting (docs/ideas-claude/v5_world-model-transfer-and-known-answer-verification.md:103)
  Split conformal calibration uses one development fold, but Section 6.3 subsequently fits final models on all 111 development participants. That includes the calibration participants and invalidates the separation needed for the advertised 90% intervals. Repeated development-based selection creates another exposure unless the calibration fold is explicitly excluded from it.
  Recommendation: Reserve participant-level calibration data from fitting and selection, calibrate the frozen deployed agent's actual score residuals, and do not refit afterward. Alternatively specify a cross-fitting method with an applicable coverage guarantee.

Next steps:
- Resolve verification, transfer calibration, and common evaluation rules before generating training trajectories.
- Validate the inference procedure and revise the independent-run budget.
- Prespecify comparable intervention outcomes and an untouched uncertainty-calibration partition.
exit=0
```
