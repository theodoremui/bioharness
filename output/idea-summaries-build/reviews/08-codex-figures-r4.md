**Release verdict at 850 px:** Ship 1 and 4. Fix 2, 3, 5, 6, 7, and 8. All eight pass the basic text-overlap check. The remaining issues are mostly about what readers infer from arrows, labels, and plot symbols. Figure 3 has the highest risk of a scientific misread.

Coordinates are approximate and refer to the original 2600 px-wide PNGs, measured from the upper-left corner. At 850 px, 30–36 px source text renders at roughly 10–12 px.

### 1. `one-video-two-referrals` — Ship

- **(a–c) Collisions, crossings, arrows.** No text collisions or crossings. Both diagonal arrows clearly leave the same video card and point to different referral cards. Each colored arrow points to a single outcome.
- **(d) Readability.** “Single-leg stance” and “illustrative example” are the smallest labels and remain readable. The headings and outcomes carry the first glance.
- **(e) Caption.** Keep “illustrative example” visible. The caption can explain why both timing rules are defensible and clarify the role of the two filter settings. The figure changes the stopping rule and cutoff together, so it cannot show which change accounts for the hold-time difference.
- **(f) Five-second read.** **Yes.** One clip goes through two analyses and yields two hold times. Why both analyses are defensible takes a caption sentence.
- **(g) Concrete fix.** No layout change needed. In the caption, describe the timing and filter choices as paired analysis settings. The two filter bullets at approximately `(785, 390)` and `(785, 870)` are the details most likely to be mistaken for an explanation of the outcome.

### 2. `referral-counted-twice` — Fix

- **(a–c) Collisions, crossings, arrows.** No text collisions or arrow crossings. The two orange arrows have clear destinations. “Referral-shaped M” sits below and to the right of the rising measurement-to-combiner arrow, so its attachment is weaker than the two “count” labels.
- **(d) Readability.** The box text is readable, though the combiner’s two-line qualification is easy to skim past at this size.
- **(e) Caption.** “Clinician’s starting odds” can move to the caption. Keep the blind-report calibration condition in the combiner because it explains why the second route creates a problem.
- **(f) Five-second read.** **Mostly.** The two orange branches show that the referral enters twice. A reader has to follow the lower gray arrow to see that the second entry reaches the decision *through the measurement*.
- **(g) Concrete fix.** Recolor the measurement-to-combiner arrow from approximately `(1380, 700)` to `(1540, 527)` in orange, and give “Referral-shaped M” the same orange treatment. Keep the video-to-measurement arrow blue. Break the combiner copy into “Prior odds × likelihood ratio” and “Likelihood ratio fitted on blind reports” so the calibration mismatch survives a quick read.

### 3. `better-measurer-worse-decision` — Fix

- **(a–c) Collisions, crossings, arrows.** No text collisions and no arrows. The dashed guides clear the labels. The hazard is visual association. The diamonds near `(457, 636)` and `(1777, 768)` sit close enough to the shrinkage curves to look like additional samples, especially in the right panel.
- **(d) Readability.** Axis ticks are around 10 px at display size. They remain usable, but the numeric annotations and the simulation note are small for information the reader needs to interpret the result correctly.
- **(e) Caption.** Keep the simulation status and the two results at γ* in the figure. Put the definition of *effective shrinkage* and how it was assigned to the Bayes report in the caption.
- **(f) Five-second read.** **Yes for the trade-off, no for the Bayes comparison.** The left curve falls below the blind baseline while the right curve rises from zero. The diamonds’ shared x-coordinate and separate provenance are easy to miss.
- **(g) Concrete fix.** Use a shared key above the panels with a filled circle for “Shrinkage report” and an open diamond for “Bayes report at effective γ.” Mark the Bayes report’s x-coordinate on both axes, near `x=457` and `x=1777`, with a short colored tick or subtle guide. Use a light outline or distinctive color to keep the right diamond visibly separate from the red curve. Label the right baseline point “Blind report” if it can fit without crowding the first two markers.

### 4. `calibration-bug-or-information-bug` — Ship

- **(a–c) Collisions, crossings, arrows.** No text collisions, confusing line crossings, or arrows. The two right-panel curves intentionally share the rising segment. The open circles and dashed drops clearly locate two distinct blind values at the same report.
- **(d) Readability.** The axis labels and annotations are readable. The small italic “schematic” label is secondary, and the absence of numeric ticks reinforces it.
- **(e) Caption.** The left panel says twice that recalibration can undo the shift. The caption can carry the qualification that recalibration is done within each referral.
- **(f) Five-second read.** **Yes.** The parallel lines retain distinctions within each referral. The cap visibly merges two blind values into one report.
- **(g) Concrete fix.** Optional polish. Remove the redundant footer centered around `(710, 990)` or shorten it to “Recalibrate within each referral.” Keep both open circles and their vertical guides.

### 5. `path-splicing-factorial` — Fix

- **(a–c) Collisions, crossings, arrows.** No text overlaps or arrow crossings. The four arrowheads point clearly right or down and stop just short of the destination cells. The ambiguity is in the headers. “Report under a” can sound like a finished report produced under referral *a*, obscuring that the second factor is the referral supplied at reporting time.
- **(d) Readability.** The cell symbols and direction labels are readable. The small subscripts are the weakest detail, especially in the interaction equation.
- **(e) Caption.** Move the interaction equation to the caption unless readers are expected to evaluate it from the diagram. The instruction to check self-splices against natural runs can also be stated once in the caption.
- **(f) Five-second read.** **Yes for rightward/direct and downward/indirect.** The factorial intervention takes longer because readers must infer exactly what the row and column headings hold fixed.
- **(g) Concrete fix.** Relabel the column headers above `x≈830` and `x≈1530` as “Referral shown at reporting: a” and “Referral shown at reporting: b.” Relabel the row headers as “Path generated under a” and “Path generated under b.” Retain the full words “direct” and “indirect” on the arrows. They are doing more work than the symbolic subscripts at this size.

### 6. `blind-analysis-harness` — Fix

- **(a–c) Collisions, crossings, arrows.** No collisions or crossings. Arrowheads and box endpoints are clear. The referral’s only drawn destination is Interpretation, so the gray Interpretation → Decision arrow can look like it carries referral-shaped evidence into the decision. The Decision box then says the referral is used once as prior, but the route that ensures this is left implicit.
- **(d) Readability.** All essential labels are readable. The lock icon remains recognizable at 850 px.
- **(e) Caption.** Move “skeleton render” and the examples of masked cues to the caption if space is needed. Keep both the absence of referral during measurement and its release after the commit visible.
- **(f) Five-second read.** **Yes for masking, blinding, and commit before reveal.** The one-use-as-prior claim is readable in the box but harder to verify by following the arrows.
- **(g) Concrete fix.** At the Interpretation → Decision handoff near `(2110, 520)`, explicitly distinguish the committed measurement evidence from the referral prior. One option is a labeled evidence line from Commit to Decision and a separate orange referral-to-prior branch that starts at the post-commit referral box. If Interpretation produces something the Decision consumes, label that handoff with what it actually carries. The diagram should make clear which input supplies the likelihood evidence and which supplies the prior.

### 7. `self-improvement-design` — Fix

- **(a–c) Collisions, crossings, arrows.** No collisions or crossings. The matrix bracket and sealed-cohort arrow both terminate at the audit box. The bracket gathers the runs, but the diagram leaves the transfer from runs to saved checkpoints implicit.
- **(d) Readability.** Optimizer and reward headings remain readable. “Prompt evolution,” “playbook,” “weights,” and the longer arm descriptions are small for secondary detail.
- **(e) Caption.** Move optimizer descriptions and detailed control rationales to the caption. Keep the optimizer names, reward conditions, seed counts, and sealed-cohort restriction on the figure.
- **(f) Five-second read.** **Mostly.** The matrix gives 45 runs and the audit box gives six checkpoints per run. The figure makes readers infer that the development cohort covers all nine cells and that the bracket provides checkpoints while the other arrow provides the audit cohort.
- **(g) Concrete fix.** Keep the dots and the 8/3/4 labels. Tie the matrix explicitly to the development cohort, for example by changing the banner near `(128, 157)` to “All runs use the development cohort.” Label the bracket’s output near `(1915, 900)` “Saved checkpoints,” moving the audit box down or shortening its text if needed to give the label room.

### 8. `predicted-routes-by-optimizer` — Fix

- **(a–c) Collisions, crossings, arrows.** No text-on-text collisions and no arrows. The right edge of the gray H4 band, near `x=2170`, cuts through the background of both “mostly…” annotations. The dashed zero line also remains visible inside the open control marker, making it look like a different symbol from a simple point at zero.
- **(d) Readability.** Row labels and the legend are readable. The H4 label’s subscript and the long normalization label take longer to parse at 850 px.
- **(e) Caption.** Move the long takeaway sentence to the caption. Keep “Hypothetical final-checkpoint predictions” prominent because the exact bar lengths can otherwise read as results. Put the definition of γ_B and how the illustrative segment lengths were chosen in the caption.
- **(f) Five-second read.** **Mostly.** The two totals end in the shaded band, and the dark versus light segments show the opposite route mixes. The zero row is clear once found. The long headline currently gives away the answer before the reader has decoded the chart.
- **(g) Concrete fix.** Move both route annotations entirely beyond the band edge, with enough right margin, or remove them and let the legend and stack proportions carry that comparison. Give the zero marker at `(867, 740)` an opaque white fill so the dashed line stops behind it. Keep a short, visible label over the shaded region, such as “H4 target band,” with `γ_B ± 0.1` underneath if space permits.
tokens used
51,143
**Release verdict at 850 px:** Ship 1 and 4. Fix 2, 3, 5, 6, 7, and 8. All eight pass the basic text-overlap check. The remaining issues are mostly about what readers infer from arrows, labels, and plot symbols. Figure 3 has the highest risk of a scientific misread.

Coordinates are approximate and refer to the original 2600 px-wide PNGs, measured from the upper-left corner. At 850 px, 30–36 px source text renders at roughly 10–12 px.

### 1. `one-video-two-referrals` — Ship

- **(a–c) Collisions, crossings, arrows.** No text collisions or crossings. Both diagonal arrows clearly leave the same video card and point to different referral cards. Each colored arrow points to a single outcome.
- **(d) Readability.** “Single-leg stance” and “illustrative example” are the smallest labels and remain readable. The headings and outcomes carry the first glance.
- **(e) Caption.** Keep “illustrative example” visible. The caption can explain why both timing rules are defensible and clarify the role of the two filter settings. The figure changes the stopping rule and cutoff together, so it cannot show which change accounts for the hold-time difference.
- **(f) Five-second read.** **Yes.** One clip goes through two analyses and yields two hold times. Why both analyses are defensible takes a caption sentence.
- **(g) Concrete fix.** No layout change needed. In the caption, describe the timing and filter choices as paired analysis settings. The two filter bullets at approximately `(785, 390)` and `(785, 870)` are the details most likely to be mistaken for an explanation of the outcome.

### 2. `referral-counted-twice` — Fix

- **(a–c) Collisions, crossings, arrows.** No text collisions or arrow crossings. The two orange arrows have clear destinations. “Referral-shaped M” sits below and to the right of the rising measurement-to-combiner arrow, so its attachment is weaker than the two “count” labels.
- **(d) Readability.** The box text is readable, though the combiner’s two-line qualification is easy to skim past at this size.
- **(e) Caption.** “Clinician’s starting odds” can move to the caption. Keep the blind-report calibration condition in the combiner because it explains why the second route creates a problem.
- **(f) Five-second read.** **Mostly.** The two orange branches show that the referral enters twice. A reader has to follow the lower gray arrow to see that the second entry reaches the decision *through the measurement*.
- **(g) Concrete fix.** Recolor the measurement-to-combiner arrow from approximately `(1380, 700)` to `(1540, 527)` in orange, and give “Referral-shaped M” the same orange treatment. Keep the video-to-measurement arrow blue. Break the combiner copy into “Prior odds × likelihood ratio” and “Likelihood ratio fitted on blind reports” so the calibration mismatch survives a quick read.

### 3. `better-measurer-worse-decision` — Fix

- **(a–c) Collisions, crossings, arrows.** No text collisions and no arrows. The dashed guides clear the labels. The hazard is visual association. The diamonds near `(457, 636)` and `(1777, 768)` sit close enough to the shrinkage curves to look like additional samples, especially in the right panel.
- **(d) Readability.** Axis ticks are around 10 px at display size. They remain usable, but the numeric annotations and the simulation note are small for information the reader needs to interpret the result correctly.
- **(e) Caption.** Keep the simulation status and the two results at γ* in the figure. Put the definition of *effective shrinkage* and how it was assigned to the Bayes report in the caption.
- **(f) Five-second read.** **Yes for the trade-off, no for the Bayes comparison.** The left curve falls below the blind baseline while the right curve rises from zero. The diamonds’ shared x-coordinate and separate provenance are easy to miss.
- **(g) Concrete fix.** Use a shared key above the panels with a filled circle for “Shrinkage report” and an open diamond for “Bayes report at effective γ.” Mark the Bayes report’s x-coordinate on both axes, near `x=457` and `x=1777`, with a short colored tick or subtle guide. Use a light outline or distinctive color to keep the right diamond visibly separate from the red curve. Label the right baseline point “Blind report” if it can fit without crowding the first two markers.

### 4. `calibration-bug-or-information-bug` — Ship

- **(a–c) Collisions, crossings, arrows.** No text collisions, confusing line crossings, or arrows. The two right-panel curves intentionally share the rising segment. The open circles and dashed drops clearly locate two distinct blind values at the same report.
- **(d) Readability.** The axis labels and annotations are readable. The small italic “schematic” label is secondary, and the absence of numeric ticks reinforces it.
- **(e) Caption.** The left panel says twice that recalibration can undo the shift. The caption can carry the qualification that recalibration is done within each referral.
- **(f) Five-second read.** **Yes.** The parallel lines retain distinctions within each referral. The cap visibly merges two blind values into one report.
- **(g) Concrete fix.** Optional polish. Remove the redundant footer centered around `(710, 990)` or shorten it to “Recalibrate within each referral.” Keep both open circles and their vertical guides.

### 5. `path-splicing-factorial` — Fix

- **(a–c) Collisions, crossings, arrows.** No text overlaps or arrow crossings. The four arrowheads point clearly right or down and stop just short of the destination cells. The ambiguity is in the headers. “Report under a” can sound like a finished report produced under referral *a*, obscuring that the second factor is the referral supplied at reporting time.
- **(d) Readability.** The cell symbols and direction labels are readable. The small subscripts are the weakest detail, especially in the interaction equation.
- **(e) Caption.** Move the interaction equation to the caption unless readers are expected to evaluate it from the diagram. The instruction to check self-splices against natural runs can also be stated once in the caption.
- **(f) Five-second read.** **Yes for rightward/direct and downward/indirect.** The factorial intervention takes longer because readers must infer exactly what the row and column headings hold fixed.
- **(g) Concrete fix.** Relabel the column headers above `x≈830` and `x≈1530` as “Referral shown at reporting: a” and “Referral shown at reporting: b.” Relabel the row headers as “Path generated under a” and “Path generated under b.” Retain the full words “direct” and “indirect” on the arrows. They are doing more work than the symbolic subscripts at this size.

### 6. `blind-analysis-harness` — Fix

- **(a–c) Collisions, crossings, arrows.** No collisions or crossings. Arrowheads and box endpoints are clear. The referral’s only drawn destination is Interpretation, so the gray Interpretation → Decision arrow can look like it carries referral-shaped evidence into the decision. The Decision box then says the referral is used once as prior, but the route that ensures this is left implicit.
- **(d) Readability.** All essential labels are readable. The lock icon remains recognizable at 850 px.
- **(e) Caption.** Move “skeleton render” and the examples of masked cues to the caption if space is needed. Keep both the absence of referral during measurement and its release after the commit visible.
- **(f) Five-second read.** **Yes for masking, blinding, and commit before reveal.** The one-use-as-prior claim is readable in the box but harder to verify by following the arrows.
- **(g) Concrete fix.** At the Interpretation → Decision handoff near `(2110, 520)`, explicitly distinguish the committed measurement evidence from the referral prior. One option is a labeled evidence line from Commit to Decision and a separate orange referral-to-prior branch that starts at the post-commit referral box. If Interpretation produces something the Decision consumes, label that handoff with what it actually carries. The diagram should make clear which input supplies the likelihood evidence and which supplies the prior.

### 7. `self-improvement-design` — Fix

- **(a–c) Collisions, crossings, arrows.** No collisions or crossings. The matrix bracket and sealed-cohort arrow both terminate at the audit box. The bracket gathers the runs, but the diagram leaves the transfer from runs to saved checkpoints implicit.
- **(d) Readability.** Optimizer and reward headings remain readable. “Prompt evolution,” “playbook,” “weights,” and the longer arm descriptions are small for secondary detail.
- **(e) Caption.** Move optimizer descriptions and detailed control rationales to the caption. Keep the optimizer names, reward conditions, seed counts, and sealed-cohort restriction on the figure.
- **(f) Five-second read.** **Mostly.** The matrix gives 45 runs and the audit box gives six checkpoints per run. The figure makes readers infer that the development cohort covers all nine cells and that the bracket provides checkpoints while the other arrow provides the audit cohort.
- **(g) Concrete fix.** Keep the dots and the 8/3/4 labels. Tie the matrix explicitly to the development cohort, for example by changing the banner near `(128, 157)` to “All runs use the development cohort.” Label the bracket’s output near `(1915, 900)` “Saved checkpoints,” moving the audit box down or shortening its text if needed to give the label room.

### 8. `predicted-routes-by-optimizer` — Fix

- **(a–c) Collisions, crossings, arrows.** No text-on-text collisions and no arrows. The right edge of the gray H4 band, near `x=2170`, cuts through the background of both “mostly…” annotations. The dashed zero line also remains visible inside the open control marker, making it look like a different symbol from a simple point at zero.
- **(d) Readability.** Row labels and the legend are readable. The H4 label’s subscript and the long normalization label take longer to parse at 850 px.
- **(e) Caption.** Move the long takeaway sentence to the caption. Keep “Hypothetical final-checkpoint predictions” prominent because the exact bar lengths can otherwise read as results. Put the definition of γ_B and how the illustrative segment lengths were chosen in the caption.
- **(f) Five-second read.** **Mostly.** The two totals end in the shaded band, and the dark versus light segments show the opposite route mixes. The zero row is clear once found. The long headline currently gives away the answer before the reader has decoded the chart.
- **(g) Concrete fix.** Move both route annotations entirely beyond the band edge, with enough right margin, or remove them and let the legend and stack proportions carry that comparison. Give the zero marker at `(867, 740)` an opaque white fill so the dashed line stops behind it. Keep a short, visible label over the shaded region, such as “H4 target band,” with `γ_B ± 0.1` underneath if space permits.
