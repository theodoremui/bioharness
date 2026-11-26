**Verdicts in file order** 1 fix · 2 fix · 3 redraw · 4 fix · 5 ship · 6 fix

I reviewed the supplied PNGs visually at the intended scale of about 850 px wide. Coordinates below are approximate and refer to the supplied 2× PNGs, measured from the top-left corner. Most secondary text will land around 10–11 px. The biggest problems are the ambiguous arrowhead in Figure 3, the missing information about when the sealed test is opened in Figure 4, and the differing definitions of a breach in Figure 6.

## 1. `edit-effect-scatter` · **Fix**

- **(a) Text collisions.** None visible. The lower-right “accepted, tail harmed” annotation fits, but repeats the legend and pulls attention away from the points.
- **(b) Crossings.** The blue decision line and both dashed zero guides meet at `(870, 710)`. The intersection is meaningful, but the nearly vertical dashed guide competes with the decision line near zero.
- **(c) Arrow clarity.** No arrows. “Rejected” and “accepted” identify the correct sides, though those labels sit far from the region where the lines converge.
- **(d) Display size.** The title and colored points survive. The parameter sentence, legend text, and two zero labels are around 10–11 px.
- **(e) Caption candidates.** Move the draw correlation and the illustrative-sample note to the caption. Keep the tail weight near the decision line because it explains the geometry.
- **(f) Five-second read.** **Yes on the outcome, partial on the mechanism.** The headline and orange points convey that the rule accepts tail-harming edits. Seeing how a positive majority gain offsets a tail loss takes longer.
- **(g) Fixes.** Lighten the vertical zero guide at `x≈870`, keep the horizontal zero guide visible, and rename the legend’s line “Mean gain = 0.” Use “Tail-harming edits that pass” inside the shaded wedge near `(1049, 1126)`. If the text interprets the line’s visual steepness quantitatively, make the axis scales explicit.

## 2. `drift-sign-map` · **Fix**

- **(a) Text collisions.** None visible. The `ρ* = −0.143` callout near `(649, 688)` has clearance, but singles out the solid curve even though the table already gives all three thresholds.
- **(b) Crossings.** The curves and the horizontal zero guide converge at `(300, 640)`. At `x≈605`, the dashed reference line crosses all three curves. The open circles help, but the two dashed lines briefly compete for attention.
- **(c) Arrow clarity.** No arrows. The main ambiguity is the space *between* curves, where the answer changes with the spread ratio. The large “helps” and “harms” labels can initially read as a single map.
- **(d) Display size.** The side explanation, line-style labels, and ticks are around 10–11 px. The difference between dashes and dots is easiest to see in the legend and harder near the shared origin.
- **(e) Caption candidates.** Move “computed from the formula” and the “one tail person in eight” gloss to the caption. Keep `π = 0.125` and the three threshold values in the figure.
- **(f) Five-second read.** **Partial.** A reader sees three falling curves. They may miss that each curve is a zero-drift boundary and that the same `(π, ρ)` can imply harm for one spread ratio and help for another.
- **(g) Fixes.** Replace the paragraph around `(1620, 608)` with “Each curve marks zero tail drift. Below that curve, selection harms the tail.” Rename the side heading “Tail-to-majority spread ratio” and use `1×`, `2×`, and `4×`. Remove the duplicate single-value callout near `(649, 688)` and keep the three values in the table.

## 3. `timing-regimes-geometry` · **Redraw**

- **(a) Text collisions.** None visible. Around the mean optimum at `(1220, 680)`, the three rays, two optimum labels, and dashed boundary create a crowded junction even though the lettering clears.
- **(b) Crossings.** Path 2 crosses the ball boundary at the diamond near `(525, 550)`, which is intentional. All three dashed paths converge at `(1220, 680)`, where their common destination is visually mixed with the horizontal line joining the optima.
- **(c) Arrow clarity.** Path 1 is the worst offender. Its oblique arrowhead near `(1375, 765)` is hard to parse at a glance, so the reader can read the dashed ray as traveling out from the mean optimum toward seed 1. All three directions should read immediately as seed → mean optimum.
- **(d) Display size.** The labels are mostly legible at about 11 px. The more consequential losses are the small oblique arrowheads and the unlabeled dashed baselines in the three trajectory panels.
- **(e) Caption candidates.** Put the full leading-order explanation in the caption and keep “Negative expected gain per step, leading order” on the ball. The “schematic” badge can also move to the caption.
- **(f) Five-second read.** **No.** The three outcomes read quickly on the right. Connecting each outcome to its seed, tracing motion toward the mean optimum, and distinguishing cumulative gain from gain per step take a second pass.
- **(g) Fixes.** Redraw as a geometry panel and three aligned mini-plots, using the same numbered markers on both sides. Add a clear, large arrowhead on each ray aimed toward the mean optimum. Keep the paired diamonds at the entry and the peak. Label the mini-plots’ shared baseline “0 change from seed.” In panel 2, either keep the declining segment above zero or say in the caption that the final sign varies. The current dip below zero can read as a necessary feature of the inverted-U regime.

## 4. `instrumented-loop` · **Fix**

- **(a) Text collisions.** The revised layout has no visible overlaps. The bottom line of the Forecast box, “frozen at generation 10,” sits only about 20 source pixels above the border, roughly 7 px at display size.
- **(b) Crossings.** The long feedback, gate-decision, and checkpoint routes clear the text and one another. The two arrows into “compare” have distinct endpoints and do not cross.
- **(c) Arrow clarity.** Arrowheads point cleanly into their boxes. The ambiguity is what gets logged and when. “Keep or reject” can read as one generation-level decision, and the route labeled “checkpoints, generations 0 to 50” can suggest repeated access to sealed scores. The return path also leaves the no-edit case implicit.
- **(d) Display size.** Box titles hold up. The Forecast body, connector labels, and lock icons are small. The lock icons carry too much of the burden of communicating who sees which scores and when.
- **(e) Caption candidates.** Move “prompts, tools, code” and the full `S > τ` rule to the caption if those mechanics are already explained there. Keep “all K,” the guard’s hidden status, and the forecast freeze in the figure.
- **(f) Five-second read.** **Partial.** The top row reads as an edit loop. It takes longer to see that *every* candidate gets a hidden guard score and that a forecast frozen at generation 10 is checked against a sealed generation 0–50 change.
- **(g) Fixes.** Label the gate-to-log route near `(2075, 565)` “Decision for each candidate.” Label the upper return path “Next parent: kept edit or current parent.” At `(354, 812)`, clarify when the sealed scores are opened and which checkpoints feed the endpoint comparison. If only generations 0 and 50 are evaluated, write “Gen 0 and 50 checkpoints.” If intermediate checkpoints are also evaluated under seal, label the route “Save checkpoints” and put the unsealing time on the sealed-test box. Set the Forecast box to two prominent lines, “Predict tail change, gen 0–50” and “Freeze at gen 10.”

## 5. `stable-person-splits` · **Ship**

- **(a) Text collisions.** None. The long “sealed test” labels fit comfortably, and the row labels clear the grid.
- **(b) Crossings.** None.
- **(c) Arrow clarity.** No arrows are needed. The diagonal sealed-test cells and the guard cell wrapping to block 1 in fold 5 make the rotation legible.
- **(d) Display size.** Cell labels remain readable at around 12 px. The legend body is closer to 10–11 px, with the guard description wrapping onto a third line.
- **(e) Caption candidates.** The legend’s approximate counts repeat information implied by the subtitle and grid. They can move to the caption if space is needed. Keep the short descriptions of what each role does.
- **(f) Five-second read.** **Yes.** The diagonal shows that each person block serves as sealed test once. The repeated cell labels make the design readable without relying on color.
- **(g) Fixes.** No blocking fix. If the figure is revised, add “Each block is sealed test once” to the subtitle near `(120, 145)` and shorten the guard legend near `(1930, 550)` to “Scores every candidate. Scores stay hidden from the loop.”

## 6. `guarantee-validity-and-price` · **Fix**

- **(a) Text collisions.** No visible overlaps after the revisions. The series labels on the right are clear of the markers. The four repeated breach sublabels make the left panel dense.
- **(b) Crossings.** The two green series cross between 5 and 10. Solid circles and dashed squares distinguish them, but their horizontal offsets make the markers look as if they were measured at different sample sizes. The dashed 0.05 line on the left clears the displayed marks.
- **(c) Arrow clarity.** No arrows. The endpoint ambiguity is in the marks. The left panel describes every mark as a bar even though the per-step method appears as a dot at `1`. The chart also gives little visual weight to the distinction between a breach at *any* accepted parent and a breach at the *deployed* checkpoint.
- **(d) Display size.** Titles and series labels survive. The event definitions and left-panel ticks are around 10–11 px, yet the event definitions carry the most important qualification.
- **(e) Caption candidates.** Move the full simulation setup and the sample-size sweep details to the caption. Keep a short “Preliminary simulation” label and leave the breach-event distinction on the figure itself.
- **(f) Five-second read.** **Partial.** The reader sees two methods on either side of 0.05 and more gain retained with larger tests. They can easily take all four breach rates as measuring the same event or read the simulated rates as a guarantee.
- **(g) Fixes.** In the left panel near `(615, 400–865)`, group the three “any accepted parent” methods under one event label and separate certification under “Deployed checkpoint only.” Label the reference “Nominal 5%” and the x-axis as logarithmic. Explain what the dot at `(1280, 392)` represents, and label it `100%` if the rate is exactly 1. On the right, center both green series on the actual ticks at `x≈1636, 1837, 2240`. Keep the circle/square distinction. The line styles already separate the series.
tokens used
48,251
**Verdicts in file order** 1 fix · 2 fix · 3 redraw · 4 fix · 5 ship · 6 fix

I reviewed the supplied PNGs visually at the intended scale of about 850 px wide. Coordinates below are approximate and refer to the supplied 2× PNGs, measured from the top-left corner. Most secondary text will land around 10–11 px. The biggest problems are the ambiguous arrowhead in Figure 3, the missing information about when the sealed test is opened in Figure 4, and the differing definitions of a breach in Figure 6.

## 1. `edit-effect-scatter` · **Fix**

- **(a) Text collisions.** None visible. The lower-right “accepted, tail harmed” annotation fits, but repeats the legend and pulls attention away from the points.
- **(b) Crossings.** The blue decision line and both dashed zero guides meet at `(870, 710)`. The intersection is meaningful, but the nearly vertical dashed guide competes with the decision line near zero.
- **(c) Arrow clarity.** No arrows. “Rejected” and “accepted” identify the correct sides, though those labels sit far from the region where the lines converge.
- **(d) Display size.** The title and colored points survive. The parameter sentence, legend text, and two zero labels are around 10–11 px.
- **(e) Caption candidates.** Move the draw correlation and the illustrative-sample note to the caption. Keep the tail weight near the decision line because it explains the geometry.
- **(f) Five-second read.** **Yes on the outcome, partial on the mechanism.** The headline and orange points convey that the rule accepts tail-harming edits. Seeing how a positive majority gain offsets a tail loss takes longer.
- **(g) Fixes.** Lighten the vertical zero guide at `x≈870`, keep the horizontal zero guide visible, and rename the legend’s line “Mean gain = 0.” Use “Tail-harming edits that pass” inside the shaded wedge near `(1049, 1126)`. If the text interprets the line’s visual steepness quantitatively, make the axis scales explicit.

## 2. `drift-sign-map` · **Fix**

- **(a) Text collisions.** None visible. The `ρ* = −0.143` callout near `(649, 688)` has clearance, but singles out the solid curve even though the table already gives all three thresholds.
- **(b) Crossings.** The curves and the horizontal zero guide converge at `(300, 640)`. At `x≈605`, the dashed reference line crosses all three curves. The open circles help, but the two dashed lines briefly compete for attention.
- **(c) Arrow clarity.** No arrows. The main ambiguity is the space *between* curves, where the answer changes with the spread ratio. The large “helps” and “harms” labels can initially read as a single map.
- **(d) Display size.** The side explanation, line-style labels, and ticks are around 10–11 px. The difference between dashes and dots is easiest to see in the legend and harder near the shared origin.
- **(e) Caption candidates.** Move “computed from the formula” and the “one tail person in eight” gloss to the caption. Keep `π = 0.125` and the three threshold values in the figure.
- **(f) Five-second read.** **Partial.** A reader sees three falling curves. They may miss that each curve is a zero-drift boundary and that the same `(π, ρ)` can imply harm for one spread ratio and help for another.
- **(g) Fixes.** Replace the paragraph around `(1620, 608)` with “Each curve marks zero tail drift. Below that curve, selection harms the tail.” Rename the side heading “Tail-to-majority spread ratio” and use `1×`, `2×`, and `4×`. Remove the duplicate single-value callout near `(649, 688)` and keep the three values in the table.

## 3. `timing-regimes-geometry` · **Redraw**

- **(a) Text collisions.** None visible. Around the mean optimum at `(1220, 680)`, the three rays, two optimum labels, and dashed boundary create a crowded junction even though the lettering clears.
- **(b) Crossings.** Path 2 crosses the ball boundary at the diamond near `(525, 550)`, which is intentional. All three dashed paths converge at `(1220, 680)`, where their common destination is visually mixed with the horizontal line joining the optima.
- **(c) Arrow clarity.** Path 1 is the worst offender. Its oblique arrowhead near `(1375, 765)` is hard to parse at a glance, so the reader can read the dashed ray as traveling out from the mean optimum toward seed 1. All three directions should read immediately as seed → mean optimum.
- **(d) Display size.** The labels are mostly legible at about 11 px. The more consequential losses are the small oblique arrowheads and the unlabeled dashed baselines in the three trajectory panels.
- **(e) Caption candidates.** Put the full leading-order explanation in the caption and keep “Negative expected gain per step, leading order” on the ball. The “schematic” badge can also move to the caption.
- **(f) Five-second read.** **No.** The three outcomes read quickly on the right. Connecting each outcome to its seed, tracing motion toward the mean optimum, and distinguishing cumulative gain from gain per step take a second pass.
- **(g) Fixes.** Redraw as a geometry panel and three aligned mini-plots, using the same numbered markers on both sides. Add a clear, large arrowhead on each ray aimed toward the mean optimum. Keep the paired diamonds at the entry and the peak. Label the mini-plots’ shared baseline “0 change from seed.” In panel 2, either keep the declining segment above zero or say in the caption that the final sign varies. The current dip below zero can read as a necessary feature of the inverted-U regime.

## 4. `instrumented-loop` · **Fix**

- **(a) Text collisions.** The revised layout has no visible overlaps. The bottom line of the Forecast box, “frozen at generation 10,” sits only about 20 source pixels above the border, roughly 7 px at display size.
- **(b) Crossings.** The long feedback, gate-decision, and checkpoint routes clear the text and one another. The two arrows into “compare” have distinct endpoints and do not cross.
- **(c) Arrow clarity.** Arrowheads point cleanly into their boxes. The ambiguity is what gets logged and when. “Keep or reject” can read as one generation-level decision, and the route labeled “checkpoints, generations 0 to 50” can suggest repeated access to sealed scores. The return path also leaves the no-edit case implicit.
- **(d) Display size.** Box titles hold up. The Forecast body, connector labels, and lock icons are small. The lock icons carry too much of the burden of communicating who sees which scores and when.
- **(e) Caption candidates.** Move “prompts, tools, code” and the full `S > τ` rule to the caption if those mechanics are already explained there. Keep “all K,” the guard’s hidden status, and the forecast freeze in the figure.
- **(f) Five-second read.** **Partial.** The top row reads as an edit loop. It takes longer to see that *every* candidate gets a hidden guard score and that a forecast frozen at generation 10 is checked against a sealed generation 0–50 change.
- **(g) Fixes.** Label the gate-to-log route near `(2075, 565)` “Decision for each candidate.” Label the upper return path “Next parent: kept edit or current parent.” At `(354, 812)`, clarify when the sealed scores are opened and which checkpoints feed the endpoint comparison. If only generations 0 and 50 are evaluated, write “Gen 0 and 50 checkpoints.” If intermediate checkpoints are also evaluated under seal, label the route “Save checkpoints” and put the unsealing time on the sealed-test box. Set the Forecast box to two prominent lines, “Predict tail change, gen 0–50” and “Freeze at gen 10.”

## 5. `stable-person-splits` · **Ship**

- **(a) Text collisions.** None. The long “sealed test” labels fit comfortably, and the row labels clear the grid.
- **(b) Crossings.** None.
- **(c) Arrow clarity.** No arrows are needed. The diagonal sealed-test cells and the guard cell wrapping to block 1 in fold 5 make the rotation legible.
- **(d) Display size.** Cell labels remain readable at around 12 px. The legend body is closer to 10–11 px, with the guard description wrapping onto a third line.
- **(e) Caption candidates.** The legend’s approximate counts repeat information implied by the subtitle and grid. They can move to the caption if space is needed. Keep the short descriptions of what each role does.
- **(f) Five-second read.** **Yes.** The diagonal shows that each person block serves as sealed test once. The repeated cell labels make the design readable without relying on color.
- **(g) Fixes.** No blocking fix. If the figure is revised, add “Each block is sealed test once” to the subtitle near `(120, 145)` and shorten the guard legend near `(1930, 550)` to “Scores every candidate. Scores stay hidden from the loop.”

## 6. `guarantee-validity-and-price` · **Fix**

- **(a) Text collisions.** No visible overlaps after the revisions. The series labels on the right are clear of the markers. The four repeated breach sublabels make the left panel dense.
- **(b) Crossings.** The two green series cross between 5 and 10. Solid circles and dashed squares distinguish them, but their horizontal offsets make the markers look as if they were measured at different sample sizes. The dashed 0.05 line on the left clears the displayed marks.
- **(c) Arrow clarity.** No arrows. The endpoint ambiguity is in the marks. The left panel describes every mark as a bar even though the per-step method appears as a dot at `1`. The chart also gives little visual weight to the distinction between a breach at *any* accepted parent and a breach at the *deployed* checkpoint.
- **(d) Display size.** Titles and series labels survive. The event definitions and left-panel ticks are around 10–11 px, yet the event definitions carry the most important qualification.
- **(e) Caption candidates.** Move the full simulation setup and the sample-size sweep details to the caption. Keep a short “Preliminary simulation” label and leave the breach-event distinction on the figure itself.
- **(f) Five-second read.** **Partial.** The reader sees two methods on either side of 0.05 and more gain retained with larger tests. They can easily take all four breach rates as measuring the same event or read the simulated rates as a guarantee.
- **(g) Fixes.** In the left panel near `(615, 400–865)`, group the three “any accepted parent” methods under one event label and separate certification under “Deployed checkpoint only.” Label the reference “Nominal 5%” and the x-axis as logarithmic. Explain what the dot at `(1280, 392)` represents, and label it `100%` if the rate is exactly 1. On the right, center both green series on the actual ticks at `x≈1636, 1837, 2240`. Keep the circle/square distinction. The line styles already separate the series.
