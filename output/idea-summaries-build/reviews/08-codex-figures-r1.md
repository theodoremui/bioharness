I’d **fix figures 1–4, 6, and 7, and redraw figures 5 and 8**. The biggest issues are scientific rather than cosmetic. Figure 5 describes the interaction ambiguously, Figure 7 visibly routes only one experimental cell into the audit, and Figure 8 plots a path share where its denominator is zero.

Coordinates below are approximate, measured from the upper-left corner of the supplied PNGs. At 850 px wide, the images display at about one-third of their supplied size. Many body labels and ticks land around 10–11 px, which is readable with effort and weak for a five-second scan.

### 1. one-video-two-referrals.png — Fix

- **(a) Text collisions** Clear. **(b) Line crossings** Clear. **(c) Arrow clarity** The split from the video card and the two arrows to the outcomes are easy to follow.
- **(d) Readability** The stance label and analysis bullets are small but legible. The gray *illustrative* tag at the lower right is easy to miss. **(e) Caption** Put the rationale for each analysis choice in the caption. Keep the trim/keep distinction and both filter cutoffs in the graphic.
- **(f) Five-second read** Yes. One clip produces two hold times under two referrals. The static pose leaves the reader to infer that both paths react to the same sway and recovery.
- **(g) Fix** At the two analysis cards around `(740,120)` and `(740,600)`, remove the repeated “Agent’s analysis path” heading and use the space to enlarge parallel action labels such as “End trial at first large sway” and “Keep trial after recovery.” The video card around `(80,280)` could show two small poses for sway and recovery. Move “Illustrative” next to “Same video,” where readers will see it before reading the two paths as protocols.

### 2. referral-counted-twice.png — Fix

- **(a) Text collisions** Clear. **(b) Line crossings** Clear. “Count 2” sits far enough left of the diagonal that its attachment takes a moment. **(c) Arrow clarity** The two referral arrows have clear destinations. The arrow leaving the measurement agent lacks a label identifying what enters the combiner.
- **(d) Readability** The combiner’s crucial “fitted on blind M” is small and easily skipped. **(e) Caption** Define \(H\) and \(M\) in the caption if they connect to the proposal equations. Keep the calibration mismatch in the graphic.
- **(f) Five-second read** Partly. The two orange routes communicate reuse of the referral. The reason this can inflate confidence takes longer to decode because the same \(M\) refers to the agent’s current output and the blind calibration data.
- **(g) Fix** Label the lower arrow into the combiner near `(1450,635)` “Referral-aware hold time.” In the combiner at `(1580,360)`, use “Prior odds × blind-calibrated likelihood ratio.” In the posterior box at `(2200,360)`, use “Can overstate support for a wrong referral.” This makes the failure conditional and pins it to the mismatch.

### 3. better-measurer-worse-decision.png — Fix

- **(a) Text collisions** Clear. **(b) Line crossings** The vertical dashed guides at `x≈588` and `x≈1908` bisect the two highlighted data markers. **(c) Arrow clarity** No arrows. The guides align the same \(\gamma^*\) across panels.
- **(d) Readability** The tick labels and gray simulation note are small. The penalty annotation is legible, but it sits near the top of the plot, far from the point it describes. **(e) Caption** Move \(\Delta\), \(\tau\), \(s\), \(q\), and `sim/b1` to the caption. Keep a short “Simulation” label above the plots.
- **(f) Five-second read** Mostly. The falling blue curve and rising red curve communicate a tradeoff. The reader still has to locate the two values at the shared optimum and infer which combiner incurs the penalty.
- **(g) Fix** Add a horizontal blind baseline at MSE \(=1\), `y≈490`. Shade the gap between that baseline and the blue curve only where the curve is below it. The current shading extends to MSE \(=2\) while carrying the label “MSE below blind.” Draw the dashed guides behind the markers and place “MSE ≈ 0.64” and “+0.026 nats” close to the respective points at `(588,601)` and `(1908,726)`. Name the blind-calibrated combiner in the right panel title or subtitle.

### 4. calibration-bug-or-information-bug.png — Fix

- **(a) Text collisions** Clear. **(b) Line crossings** Clear. **(c) Arrow clarity** No arrows. The plateau reads as a cap, but “merged after the cut” leaves the reader to work out what merged.
- **(d) Readability** Curve labels and bottom takeaways are legible with effort. The gray *schematic* tag is easy to miss. **(e) Caption** Move the two-sentence explanation of recalibration into the caption and retain a short conclusion under each panel.
- **(f) Five-second read** Partly. Parallel lines versus a plateau is a clear visual difference. Recoverability is the harder point. Readers have to infer that two different blind measurements become the same report **within the same referral**.
- **(g) Fix** On the red plateau near `(2012,565)`, mark two distinct \(M_0\) values, for example at `x≈2150` and `x≈2350`, with faint guides from the x-axis to the same reported height. Label the pair “Different blind hold times, same report.” Use “The offset can be reversed within each referral” under the left panel. In the caption, specify that the plateau shows a shared cutoff and that recovering the original hold time requires information beyond the report and referral.

### 5. path-splicing-factorial.png — Redraw

- **(a) Text collisions** Clear. **(b) Line crossings** Clear. **(c) Arrow clarity** The visible arrows show report framing changing first, then path framing. The lower-left splice is visually disconnected even though it supplies the second ordering.
- **(d) Readability** The four \(\mu\) labels read well. The row and column labels, the top transcript details, and the three right-hand cards are small at display size. **(e) Caption** Move the transcript contents and placebo acceptance criterion to the caption. Keep a short self-splice check visible.
- **(f) Five-second read** The top strip communicates replaying one path under a different referral. The factorial contrasts and interaction take longer, and “their gap is the interaction” can be read as a difference between the two route totals. Both route totals equal \(\mu(b,b)-\mu(a,a)\). The interaction is the difference between the two report-stage effects, or equivalently between the two path-stage effects.
- **(g) Fix** Make the grid around `(600,600)` the main figure. Draw arrows along all four sides. Label horizontal moves “Change report framing” and vertical moves “Change path framing.” Use one compact interaction note, \([\mu(b,b)-\mu(b,a)]-[\mu(a,b)-\mu(a,a)]\). Put “Self-splice \(a\to a\) checks replay against the natural run” beside the diagonal cell or directly below the grid. Reduce the top strip to a small inset if the replay mechanism still needs a visual.

### 6. blind-analysis-harness.png — Fix

- **(a) Text collisions** Clear. **(b) Line crossings** Clear. **(c) Arrow clarity** The vertical referral arrow has an unambiguous endpoint at Interpretation. The left-to-right sequence and the lock indicate when the referral enters.
- **(d) Readability** The pipeline titles hold up. The five variant chips and their gray outlines compete with the smaller pipeline text. **(e) Caption** Move the variants, masking examples, and hashing detail to the caption. Keep “Freeze analysis path and result” in the pipeline.
- **(f) Five-second read** Yes. The agent measures blind, commits, and then sees the referral for interpretation. “Pre-declared changes only” introduces a consequential ambiguity about whether interpretation can revise the committed measurement.
- **(g) Fix** In Interpretation at `(1560,380)`, use “Apply the predeclared interpretation menu to the committed result.” In Commit at `(1120,380)`, use “Freeze analysis path and result.” Keep “Referral revealed after commit” above the vertical arrow. If the variants are planned, label them “Variants to test” in the caption.

### 7. self-improvement-design.png — Fix

- **(a) Text collisions** Clear. **(b) Line crossings** Clear. **(c) Arrow clarity** The horizontal arrow starting at `(1872,820)` visibly comes from **ACE × accuracy with randomized referral**. Its placement implies that only that cell feeds the checkpoint audit. The vertical arrow from the sealed test cohort is clear.
- **(d) Readability** The nine repeated “5 seeds” labels dominate the smaller reward descriptions and audit measures. **(e) Caption** Move the optimizer implementation descriptions and detailed audit metrics to the caption. Keep the cohort split, reward conditions, seed count, and checkpoint cadence in the figure.
- **(f) Five-second read** The 3×3 design is apparent. The requirement to audit every checkpoint across all nine cells is easy to misread. Red on the approval-judge arm also makes the positive control look like an observed harm result.
- **(g) Fix** Replace the nine seed labels with one “5 seeds per cell · 45 runs” line. Connect an enclosing matrix bracket to a box titled “Audit every checkpoint from all 45 runs.” Keep the sealed cohort arrow entering that box separately. Use orange for the referral-aware judge, or gray for the reward condition, to preserve red for harm and information loss.

### 8. predicted-routes-by-optimizer.png — Redraw

- **(a) Text collisions** Clear. **(b) Line crossings** The blue randomized-referral line crosses both orange curves near the left origin because it is drawn slightly above zero. The crossing reads as a predicted early reversal. **(c) Arrow clarity** No arrows. The shared line-style legend is ambiguous because the blue control is solid and solid also identifies prompt or playbook evolution.
- **(d) Readability** The left reference label and bottom legend are small. The pre-registered prediction status deserves more prominence than the lower-right *hypothetical* tag. **(e) Caption** Put the definition of path share, the handling of the interaction, and the checkpoint convention in the caption. Keep the accuracy-reward condition in the figure.
- **(f) Five-second read** Partly. The right panel shows the prompt and playbook curve taking a larger path share. The left panel leaves the accuracy-reward condition implicit and puts \(\gamma^*\) on an unlabeled vertical scale. More seriously, the left panel starts both total effects at zero while the right panel shows both path shares at about 0.10. A share of a zero total is undefined.
- **(g) Fix** Omit the right-panel share at generation 0 and begin it where the total effect is estimable. Label the 0.5 line “Half the total effect.” Give the left y-axis the units of the pre-registered framing-effect measure, and map \(\gamma^*\) into those units if the proposal defines that mapping. Direct-label the two optimizer curves and give the randomized control its own zero reference style. Use orange for referral framing in both panels, and put “Pre-registered predictions under accuracy reward” above them.
tokens used
55,278
I’d **fix figures 1–4, 6, and 7, and redraw figures 5 and 8**. The biggest issues are scientific rather than cosmetic. Figure 5 describes the interaction ambiguously, Figure 7 visibly routes only one experimental cell into the audit, and Figure 8 plots a path share where its denominator is zero.

Coordinates below are approximate, measured from the upper-left corner of the supplied PNGs. At 850 px wide, the images display at about one-third of their supplied size. Many body labels and ticks land around 10–11 px, which is readable with effort and weak for a five-second scan.

### 1. one-video-two-referrals.png — Fix

- **(a) Text collisions** Clear. **(b) Line crossings** Clear. **(c) Arrow clarity** The split from the video card and the two arrows to the outcomes are easy to follow.
- **(d) Readability** The stance label and analysis bullets are small but legible. The gray *illustrative* tag at the lower right is easy to miss. **(e) Caption** Put the rationale for each analysis choice in the caption. Keep the trim/keep distinction and both filter cutoffs in the graphic.
- **(f) Five-second read** Yes. One clip produces two hold times under two referrals. The static pose leaves the reader to infer that both paths react to the same sway and recovery.
- **(g) Fix** At the two analysis cards around `(740,120)` and `(740,600)`, remove the repeated “Agent’s analysis path” heading and use the space to enlarge parallel action labels such as “End trial at first large sway” and “Keep trial after recovery.” The video card around `(80,280)` could show two small poses for sway and recovery. Move “Illustrative” next to “Same video,” where readers will see it before reading the two paths as protocols.

### 2. referral-counted-twice.png — Fix

- **(a) Text collisions** Clear. **(b) Line crossings** Clear. “Count 2” sits far enough left of the diagonal that its attachment takes a moment. **(c) Arrow clarity** The two referral arrows have clear destinations. The arrow leaving the measurement agent lacks a label identifying what enters the combiner.
- **(d) Readability** The combiner’s crucial “fitted on blind M” is small and easily skipped. **(e) Caption** Define \(H\) and \(M\) in the caption if they connect to the proposal equations. Keep the calibration mismatch in the graphic.
- **(f) Five-second read** Partly. The two orange routes communicate reuse of the referral. The reason this can inflate confidence takes longer to decode because the same \(M\) refers to the agent’s current output and the blind calibration data.
- **(g) Fix** Label the lower arrow into the combiner near `(1450,635)` “Referral-aware hold time.” In the combiner at `(1580,360)`, use “Prior odds × blind-calibrated likelihood ratio.” In the posterior box at `(2200,360)`, use “Can overstate support for a wrong referral.” This makes the failure conditional and pins it to the mismatch.

### 3. better-measurer-worse-decision.png — Fix

- **(a) Text collisions** Clear. **(b) Line crossings** The vertical dashed guides at `x≈588` and `x≈1908` bisect the two highlighted data markers. **(c) Arrow clarity** No arrows. The guides align the same \(\gamma^*\) across panels.
- **(d) Readability** The tick labels and gray simulation note are small. The penalty annotation is legible, but it sits near the top of the plot, far from the point it describes. **(e) Caption** Move \(\Delta\), \(\tau\), \(s\), \(q\), and `sim/b1` to the caption. Keep a short “Simulation” label above the plots.
- **(f) Five-second read** Mostly. The falling blue curve and rising red curve communicate a tradeoff. The reader still has to locate the two values at the shared optimum and infer which combiner incurs the penalty.
- **(g) Fix** Add a horizontal blind baseline at MSE \(=1\), `y≈490`. Shade the gap between that baseline and the blue curve only where the curve is below it. The current shading extends to MSE \(=2\) while carrying the label “MSE below blind.” Draw the dashed guides behind the markers and place “MSE ≈ 0.64” and “+0.026 nats” close to the respective points at `(588,601)` and `(1908,726)`. Name the blind-calibrated combiner in the right panel title or subtitle.

### 4. calibration-bug-or-information-bug.png — Fix

- **(a) Text collisions** Clear. **(b) Line crossings** Clear. **(c) Arrow clarity** No arrows. The plateau reads as a cap, but “merged after the cut” leaves the reader to work out what merged.
- **(d) Readability** Curve labels and bottom takeaways are legible with effort. The gray *schematic* tag is easy to miss. **(e) Caption** Move the two-sentence explanation of recalibration into the caption and retain a short conclusion under each panel.
- **(f) Five-second read** Partly. Parallel lines versus a plateau is a clear visual difference. Recoverability is the harder point. Readers have to infer that two different blind measurements become the same report **within the same referral**.
- **(g) Fix** On the red plateau near `(2012,565)`, mark two distinct \(M_0\) values, for example at `x≈2150` and `x≈2350`, with faint guides from the x-axis to the same reported height. Label the pair “Different blind hold times, same report.” Use “The offset can be reversed within each referral” under the left panel. In the caption, specify that the plateau shows a shared cutoff and that recovering the original hold time requires information beyond the report and referral.

### 5. path-splicing-factorial.png — Redraw

- **(a) Text collisions** Clear. **(b) Line crossings** Clear. **(c) Arrow clarity** The visible arrows show report framing changing first, then path framing. The lower-left splice is visually disconnected even though it supplies the second ordering.
- **(d) Readability** The four \(\mu\) labels read well. The row and column labels, the top transcript details, and the three right-hand cards are small at display size. **(e) Caption** Move the transcript contents and placebo acceptance criterion to the caption. Keep a short self-splice check visible.
- **(f) Five-second read** The top strip communicates replaying one path under a different referral. The factorial contrasts and interaction take longer, and “their gap is the interaction” can be read as a difference between the two route totals. Both route totals equal \(\mu(b,b)-\mu(a,a)\). The interaction is the difference between the two report-stage effects, or equivalently between the two path-stage effects.
- **(g) Fix** Make the grid around `(600,600)` the main figure. Draw arrows along all four sides. Label horizontal moves “Change report framing” and vertical moves “Change path framing.” Use one compact interaction note, \([\mu(b,b)-\mu(b,a)]-[\mu(a,b)-\mu(a,a)]\). Put “Self-splice \(a\to a\) checks replay against the natural run” beside the diagonal cell or directly below the grid. Reduce the top strip to a small inset if the replay mechanism still needs a visual.

### 6. blind-analysis-harness.png — Fix

- **(a) Text collisions** Clear. **(b) Line crossings** Clear. **(c) Arrow clarity** The vertical referral arrow has an unambiguous endpoint at Interpretation. The left-to-right sequence and the lock indicate when the referral enters.
- **(d) Readability** The pipeline titles hold up. The five variant chips and their gray outlines compete with the smaller pipeline text. **(e) Caption** Move the variants, masking examples, and hashing detail to the caption. Keep “Freeze analysis path and result” in the pipeline.
- **(f) Five-second read** Yes. The agent measures blind, commits, and then sees the referral for interpretation. “Pre-declared changes only” introduces a consequential ambiguity about whether interpretation can revise the committed measurement.
- **(g) Fix** In Interpretation at `(1560,380)`, use “Apply the predeclared interpretation menu to the committed result.” In Commit at `(1120,380)`, use “Freeze analysis path and result.” Keep “Referral revealed after commit” above the vertical arrow. If the variants are planned, label them “Variants to test” in the caption.

### 7. self-improvement-design.png — Fix

- **(a) Text collisions** Clear. **(b) Line crossings** Clear. **(c) Arrow clarity** The horizontal arrow starting at `(1872,820)` visibly comes from **ACE × accuracy with randomized referral**. Its placement implies that only that cell feeds the checkpoint audit. The vertical arrow from the sealed test cohort is clear.
- **(d) Readability** The nine repeated “5 seeds” labels dominate the smaller reward descriptions and audit measures. **(e) Caption** Move the optimizer implementation descriptions and detailed audit metrics to the caption. Keep the cohort split, reward conditions, seed count, and checkpoint cadence in the figure.
- **(f) Five-second read** The 3×3 design is apparent. The requirement to audit every checkpoint across all nine cells is easy to misread. Red on the approval-judge arm also makes the positive control look like an observed harm result.
- **(g) Fix** Replace the nine seed labels with one “5 seeds per cell · 45 runs” line. Connect an enclosing matrix bracket to a box titled “Audit every checkpoint from all 45 runs.” Keep the sealed cohort arrow entering that box separately. Use orange for the referral-aware judge, or gray for the reward condition, to preserve red for harm and information loss.

### 8. predicted-routes-by-optimizer.png — Redraw

- **(a) Text collisions** Clear. **(b) Line crossings** The blue randomized-referral line crosses both orange curves near the left origin because it is drawn slightly above zero. The crossing reads as a predicted early reversal. **(c) Arrow clarity** No arrows. The shared line-style legend is ambiguous because the blue control is solid and solid also identifies prompt or playbook evolution.
- **(d) Readability** The left reference label and bottom legend are small. The pre-registered prediction status deserves more prominence than the lower-right *hypothetical* tag. **(e) Caption** Put the definition of path share, the handling of the interaction, and the checkpoint convention in the caption. Keep the accuracy-reward condition in the figure.
- **(f) Five-second read** Partly. The right panel shows the prompt and playbook curve taking a larger path share. The left panel leaves the accuracy-reward condition implicit and puts \(\gamma^*\) on an unlabeled vertical scale. More seriously, the left panel starts both total effects at zero while the right panel shows both path shares at about 0.10. A share of a zero total is undefined.
- **(g) Fix** Omit the right-panel share at generation 0 and begin it where the total effect is estimable. Label the 0.5 line “Half the total effect.” Give the left y-axis the units of the pre-registered framing-effect measure, and map \(\gamma^*\) into those units if the proposal defines that mapping. Direct-label the two optimizer curves and give the randomized control its own zero reference style. Use orange for referral framing in both panels, and put “Pre-registered predictions under accuracy reward” above them.
