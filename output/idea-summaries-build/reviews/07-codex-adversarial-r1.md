[codex] Starting Codex task thread.
[codex] Thread ready (01a213c9-83dd-73a0-b070-2d828b051f55).
[codex] Turn started (01a213c9-8564-79d3-876d-05040689e861).
[codex] Assistant message captured: I’ll review Proposal 07 and its eight figures, focusing on whether the experiments can suppor...
[codex] Running command: /bin/zsh -lc "nl -ba docs/idea-summaries/07-learning-how-to-look-at-tool-outputs.md | sed -n ...
[codex] Running command: /bin/zsh -lc "nl -ba docs/idea-summaries/07-learning-how-to-look-at-tool-outputs.md | sed -n ...
[codex] Command completed: /bin/zsh -lc "nl -ba docs/idea-summaries/07-learning-how-to-look-at-tool-outputs.md | sed -n ... (exit 0)
[codex] Command completed: /bin/zsh -lc "nl -ba docs/idea-summaries/07-learning-how-to-look-at-tool-outputs.md | sed -n ... (exit 0)
[codex] Running command: /bin/zsh -lc 'git diff --stat HEAD -- docs/idea-summaries/07-learning-how-to-look-at-tool-out...
[codex] Running command: /bin/zsh -lc 'git status --short -- docs/idea-summaries/07-learning-how-to-look-at-tool-outpu...
[codex] Command completed: /bin/zsh -lc 'git diff --stat HEAD -- docs/idea-summaries/07-learning-how-to-look-at-tool-out... (exit 0)
[codex] Command completed: /bin/zsh -lc 'git status --short -- docs/idea-summaries/07-learning-how-to-look-at-tool-outpu... (exit 0)
[codex] Running command: /bin/zsh -lc "nl -ba docs/idea-summaries/07-learning-how-to-look-at-tool-outputs.md | sed -n ...
[codex] Running command: /bin/zsh -lc "nl -ba docs/idea-summaries/07-learning-how-to-look-at-tool-outputs.md | sed -n ...
[codex] Command completed: /bin/zsh -lc "nl -ba docs/idea-summaries/07-learning-how-to-look-at-tool-outputs.md | sed -n ... (exit 0)
[codex] Command completed: /bin/zsh -lc "nl -ba docs/idea-summaries/07-learning-how-to-look-at-tool-outputs.md | sed -n ... (exit 0)
[codex] Searching:
[codex] Searching:
[codex] Searching:
[codex] Searching:
[codex] Searching:
[codex] Running command: /bin/zsh -lc "for f in docs/idea-summaries/images/07/*.svg; do rg -n '<title|<desc|calibratio...
[codex] Command completed: /bin/zsh -lc "for f in docs/idea-summaries/images/07/*.svg; do rg -n '<title|<desc|calibratio... (exit 0)
[codex] Assistant message captured: The main issues are in the study design. I’m checking the transfer formula against the propos...
[codex] Searching:
[codex] Running command: /bin/zsh -lc "git --no-pager diff --no-index -- /dev/null docs/idea-summaries/07-learning-how...
[codex] Command completed: /bin/zsh -lc "git --no-pager diff --no-index -- /dev/null docs/idea-summaries/07-learning-how... (exit 0)
[codex] Running command: /bin/zsh -lc 'for f in docs/idea-summaries/images/07/*.svg; do git --no-pager diff --no-index...
[codex] Command completed: /bin/zsh -lc 'for f in docs/idea-summaries/images/07/*.svg; do git --no-pager diff --no-index... (exit 0)
[codex] Searching:
[codex] Running command: /bin/zsh -lc "nl -ba docs/idea-summaries/images/07/risk-decomposition.svg | sed -n '9,35p'"
[codex] Command completed: /bin/zsh -lc "nl -ba docs/idea-summaries/images/07/risk-decomposition.svg | sed -n '9,35p'" (exit 0)
[codex] Running command: /bin/zsh -lc "nl -ba docs/idea-summaries/images/07/transfer-decomposition-curve.svg | awk 'le...
[codex] Command completed: /bin/zsh -lc "nl -ba docs/idea-summaries/images/07/transfer-decomposition-curve.svg | awk 'le... (exit 0)
[codex] Searching:
[codex] Assistant message captured: { "verdict": "needs-attention", "summary": "Do not ship this as an executable research propos...
[codex] Turn completed.
# Codex Adversarial Review

Target: working tree diff
Verdict: needs-attention

Do not ship this as an executable research proposal. The primary transfer test can drop the regressions it is meant to detect, and the experiments cannot attribute gains to presentation, reader-family diversity, or co-adaptation.

Findings:
- [high] The primary transfer analysis is undefined for key outcomes (docs/idea-summaries/07-learning-how-to-look-at-tool-outputs.md:221-227)
  E4 includes every held-out renderer–reader cell, while H1 models log transfer. The ratio is undefined at the default checkpoint, unstable when the source gain is near zero, and has no real logarithm when the source improves but the target regresses. Dropping those cells would bias the result toward successful transfer. The power calculation also counts search seeds, even though the test of transfer to new readers depends on the much smaller set of reader families and panels.
  Recommendation: Use signed target gains as the primary endpoint, model source gains jointly, and reserve ratios for a preregistered minimum source gain. Simulate the full reader, family, run, and checkpoint design before fixing sample sizes.
- [high] H1 does not specify how to produce independent forecasts (docs/idea-summaries/07-learning-how-to-look-at-tool-outputs.md:111-119)
  Equation 117 needs the evolved renderer, labeled oracle-risk changes after mark removal, and an oracle-risk difference from the default. Those inputs are unavailable before search, although E2 says the predictions themselves will be registered then. The proposal also leaves the scoring split for those renderer-specific inputs unspecified. Using sealed labels would put outcome-side information into the predictor, and reusing the crowd profile that shaped the legibility arm makes that panel a dependent evaluation target for that arm.
  Recommendation: Preregister the rule before search, then timestamp renderer-specific forecasts using only development or calibration labels before opening sealed outcomes. Compare against an oracle-only predictor and use a separate crowd panel to evaluate the crowd-regularized arm.
- [high] The no-glyph experiment cannot isolate perception from computation (docs/idea-summaries/07-learning-how-to-look-at-tool-outputs.md:105-109)
  The no-glyph grammar still lets the renderer filter, window, and compute derived statistics. For example, an enlarged mark can encode an amplitude the renderer has already calculated. A win over a clinical plot or a separately evolved text summarizer could therefore come from feature computation, feature selection, or presentation. Equal token counts do not hold those factors fixed, and the proposed computation share has no causal interpretation.
  Recommendation: Cross a fixed upstream transform with multiple encodings. Render the exact same computed values as marks and text at matched budgets, and toggle derived features while keeping the display fixed.
- [high] The oracle checks cannot establish the shared information term (docs/idea-summaries/07-learning-how-to-look-at-tool-outputs.md:87-99)
  A CNN and a frozen-feature probe can plateau above Bayes risk and agree while both miss the same signal. Their agreement does not establish information equivalence. The derivation also omits the task named in every reader prompt, and the cross-reader equation assumes a shared information term despite using each model's post-resize input. Different preprocessing can erase different cues. The toy simulation illustrates oracle error, but it contains no transfer experiment that supports the claim that mixed profiles would mispredict transfer. [Xu et al. on usable information](https://arxiv.org/html/2002.10689#S3.SS2)
  Recommendation: Condition every decoder on the same task information and use reader-specific floors unless effective inputs are matched. Establish information equivalence on controlled encodings with known decoders, report empirical oracle risks as decoder-dependent bounds, and narrow the simulation claim to what it measures.
- [high] The task holdout excludes fitness alone (docs/idea-summaries/07-learning-how-to-look-at-tool-outputs.md:155-157)
  The three StaBLE tasks are barred from fitness, but dev-train supplies labeled reader and oracle errors to the mutator and also supplies fine-tuning data. As written, those tasks can shape proposed edits or reader weights through other people before they are scored as held-out tasks. Separately, the 43 test people already supplied the reported pilot results. Their reuse does not establish participant leakage, but the proposal does not document which design decisions preceded access to those results.
  Recommendation: Enforce task exclusions across feedback, oracle fitting, calibration, and reader training. Record prior access to the pilot cohort and use a fresh participant cohort for the confirmatory result, or label the reused cohort as replication on previously measured people.
- [high] The co-adaptation gap cannot identify a private visual code (docs/idea-summaries/07-learning-how-to-look-at-tool-outputs.md:145-151)
  The matched pair can improve through ordinary reader fine-tuning while fresh readers lose a cue because the renderer drops it. That produces the predicted gap without a pair-specific code. The fitted reader can also get worse and close the gap without improving outside readability. Frozen A0 is included in both the legibility objective and the fresh-reader average, so that average can improve through direct optimization. The round definition also leaves it unclear whether the pair is scored before or after its reader update.
  Recommendation: Cross checkpoint readers and renderers within and across seeds, add a renderer-only control, and test the matched-pair interaction. Use readers excluded from the legibility objective to test absolute readability recovery and define the checkpoint timing explicitly.
- [medium] The ensemble comparison confounds diversity with more scoring (docs/idea-summaries/07-learning-how-to-look-at-tool-outputs.md:169-175)
  The matrix crosses single readers with cross-family pairs but has no same-family pair. The budget then gives the two-reader runs twice the scoring cost. Improved transfer could come from averaging two noisy objectives or spending twice as much on feedback. Figure 6 adds a misleading cue by shading an absolute source-to-VLM gap and calling it the reader-specific share, which the text defines as normalized and averaged over held-out readers.
  Recommendation: Add a same-family pair with a common source and match total reader calls or GPU time. Evaluate the same unseen targets across arms and plot the registered normalized share with the stated reader weights.
- [medium] Prior work narrows the novelty to the cross-reader forecast (docs/idea-summaries/07-learning-how-to-look-at-tool-outputs.md:54-61)
  The gap statement underplays Mihai and Hare, who optimized a learned drawing channel on downstream identification and tested it with human receivers and a perceptual constraint. Long et al. also composed elementary error profiles to predict human performance on a new chart and task without refitting. These results leave room for a prospective forecast across readers of evolved tool-output renderers, but the proposal has no compositional predictor baseline to show what its method adds. [Mihai and Hare](https://arxiv.org/html/2106.02067) · [Long et al.](https://arxiv.org/html/2604.02220v2)
  Recommendation: Narrow the novelty claim to the prospective cross-reader forecast and compare the proposed channel-weighted formula with a task-operator baseline on the same renderer–reader pairs.
- [medium] The compute budget omits work required by the protocol (docs/idea-summaries/07-learning-how-to-look-at-tool-outputs.md:248-256)
  The search estimate prices dev-select reader calls, but mutations also require dev-train reader and oracle feedback. The budget assigns 100 H100-hours to oracles without specifying how training or scoring scales across candidate renderers and mark-removal variants. It also assigns 300 hours to two replication suites that are described as rerunning E2–E5, while the main search alone is budgeted at 1,400 hours. The resulting total cannot establish that the confirmatory design is feasible.
  Recommendation: Benchmark a complete generation with both participant pools and oracle feedback. Specify what is cached, how many renderer-specific oracles are fit, and the candidate, checkpoint, and trial counts for each replication suite.
- [medium] Figure 2 reverses calibration and resolution (docs/idea-summaries/images/07/risk-decomposition.svg:12-15)
  The figure labels the interval from the encoding floor to the recalibrated reader as calibration, and the interval from the recalibrated reader to the original reader as resolution. Equation 93 defines them the other way around. The distinction matters because the proposed transfer profiles use resolution after recalibration.
  Recommendation: Swap the segment labels so resolution is the residual above the encoding floor and calibration is the reduction achieved by the fitted map.

Next steps:
- Freeze a signed transfer endpoint and a forecast protocol before any search or sealed scoring.
- Run a small factorial pilot to check the oracle, computation, and co-adaptation controls and measure the cost of a complete generation.
