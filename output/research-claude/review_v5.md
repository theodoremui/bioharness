# Review of v5: "Privileged, Verified Supervision for Tool-Calling Video Agents"

Reviewed file: `docs/ideas-claude/v5_world-model-transfer-and-known-answer-verification.md`
Rubric: see `review_v0_codex-baseline.md`.

## Scores

| Dimension | v1 | v2 | v3 | v4 | v5 | Rationale for v5 |
|---|---|---|---|---|---|---|
| D1 Significance (15%) | 6 | 6.5 | 7.5 | 8 | 8.5 | Transfer to held-out tasks and intervention tests turn "the agent is accurate" into "the agent has learned to measure", which is the claim ICML would care about. |
| D2 Novelty (15%) | 5 | 5 | 7 | 7.5 | 8 | Known-answer verification is a clean, general mechanism: credit a reported number only if the code that produced it reproduces known answers elsewhere. |
| D3 Research question (10%) | 7 | 8 | 8 | 7.5 | 8 | Back to a single-factor primary contrast. Seven secondary contrasts are too many for 60 participants after Holm correction. |
| D4 Soundness (10%) | 5 | 6 | 7 | 7.5 | 8 | The bound now holds exactly; the verifier is validated against named shortcuts. The agent's own time annotations are still unverified at test time. |
| D5 Experimental design (10%) | 5 | 7 | 8 | 8 | 8.5 | Replicated mechanism arm, a warm-start comparison at the SFT stage, and a continuation control. |
| D6 Statistics and leakage (10%) | 5 | 7.5 | 8.5 | 8.5 | 9 | Sealed set reserved first, status-specific eligibility, honest retrospective framing, power gate with an estimation-only fallback. |
| D7 Feasibility (10%) | 7 | 7 | 6.5 | 6.5 | 6.5 | About 4,000 H100-hours plus a 235B teacher. The minimum scope is sensible but the default plan is heavy. |
| D8 Clarity (10%) | 7 | 8 | 8 | 7 | 6.5 | The document is now a protocol. A newcomer meets tolerances, percentiles and reward constants before seeing one concrete trajectory. |
| D9 Story arc (5%) | 5 | 7 | 6 | 8 | 8 | The stage table carries the journey; the prose between stages is thin. |
| D10 Writing (5%) | 7 | 7 | 7 | 7 | 7 | Accurate but dense; some sentences stack three or four clauses. |

**Weighted overall: 7.88 / 10** (v4: 7.58). ICML readiness: accept-leaning on substance. Presentation is now the main obstacle: the ideas are strong and the reader has to work too hard to see them.

## Main critiques

1. **The proposal is hard to read.** Numbers that matter for implementation (probe percentiles, tolerances, penalty constants) appear in the main text and hide the four ideas that matter for understanding. A single worked example of one trajectory, from video to verified feature to reward, would explain more than any paragraph of definitions.
2. **Too many confirmatory contrasts.** Seven Holm-corrected contrasts on 60 participants will leave most of them underpowered. Comparing the final agent with three separate baselines (S3–S5) could be one contrast against the strongest non-agent method, chosen on development folds before unsealing.
3. **The agent's time annotations remain an unchecked choice.** Verification certifies the code, not the window the agent chose for this video. Annotation error against the three-camera segmentation should be a reported outcome on the sealed set, and the proposal should say plainly that verification covers computation, not perception.
4. **The world model predicts the expert pipeline's error, not the agent's.** That is fine for routing and for a first uncertainty estimate, but the text should say so, and the conformal calibration should use the agent's own development errors once the agent is frozen.
5. **The time-scaling intervention may break the tools.** Slowing a video to 0.8× could change how the reconstruction model behaves. The expected responses should be checked first on development videos with the expert pipeline, whose response accuracy then serves as the ceiling.
6. **The central idea is not stated in one line.** A reader should leave knowing the paper's thesis: reward the measurements, and only those that can be checked.
7. **The per-stage account of data shape and leakage is split across sections.** The brief asks that each methodological step say how the dataset's shape is preserved, how the split works and how leakage is prevented. A single table per stage would do this.

## Suggestions for v6

1. Rewrite for a newcomer: open with the thesis, explain each concept once with the rise-to-toes example, and include a short worked trajectory.
2. Move fixed settings (tolerances, constants, percentiles) into a compact table near the end.
3. Collapse S3–S5 into one contrast against the strongest non-agent method; keep five confirmatory secondaries.
4. Report annotation error and state the scope of verification.
5. Calibrate interventions on development videos first.
6. Give every stage one row stating what is trained, on which data, how the data's shape is preserved, what blocks leakage, and which statistic decides the gate.
7. Shorten the abstract and keep it free of protocol numbers.

## Codex adversarial review of v5 and its disposition

Verbatim output: `codex_adversarial_review_v5.md`. Verdict: needs-attention.

| Codex finding | Severity | Response in v7 |
|---|---|---|
| Expert probe annotations conceal fabricated current-video timings | high | Required-signal test added (a function of the time marks alone fails); time-mark-only shortcuts added to the validation suite; the frozen agent also marks start and end on probe videos, and its timing error there and on sealed videos is reported. The text now says the check certifies computation given the time marks, and time marks are judged separately. |
| Held-out tasks lack endpoints, fallback means and probes | high | Adopted: a **task-calibration set** (development participants' reference features for the held-out tasks, never used for training or shown to any model) fixes endpoints, fallback means and probes, identically for all methods. The experiment is described as transfer with labelled calibration and no training on the task. |
| Arm-dependent scoring confounds the reward comparison | high | Adopted (also raised in review_v6): one policy for all methods, primary scores from features as submitted, checked scores reported separately. |
| Three seeds do not support nominal crossed-bootstrap confidence | high | Adopted: five paired seeds for the primary arms and for S1. Method-level claims require both the participant-bootstrap interval for the seed-averaged agents and a pre-registered sign test across the five paired seed differences (all five favouring the checked reward, one-sided p ≈ 0.03). The false-positive rate of the full rule is checked by simulation in Stage 0. |
| Intervention contrast compares different statistics | medium | Adopted: S4 uses one score-change statistic for both methods; feature-level responses are reported separately; a timestamp-only shortcut is a control; the test is stated as necessary, not sufficient, for a measurement claim. |
| Conformal calibration fold reused in final fitting | medium | Adopted by narrowing the claim: the tool-outcome model's uncertainty is evaluated as a ranking signal (predicted versus realized error, selective-prediction curve), with no coverage guarantee claimed. |
