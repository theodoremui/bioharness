Figures 4 and 6 need redraws because their connectors obscure the mechanisms they’re meant to explain. The other six need targeted fixes. The clearest visible collision is in figure 1, where the turning-point marker touches the blue curve and makes the turn look like a crossover event.

Coordinates below are approximate native PNG pixels measured from the upper-left corner. At 850 px wide, a 30 px source label displays at roughly 10–11 px.

## 1. `concept-mean-vs-tail.png` · **Fix**

- **(a) Collisions.** The orange ring at `(600, 646)` touches the blue curve. It also sits just to the right of the orange minimum, around `(570, 648)`. The marker, the minimum, and the crossing of the two curves read as one event.
- **(b–c) Lines and arrows.** Both crossings of the dashed start line are meaningful and clear. The orange ring obscures the blue–orange crossing. There are no directional arrows.
- **(d–e) Size and caption.** “Worse,” “start,” and “better” are around 11 px at display size. The long title takes the most prominent position but describes the rule more clearly than the result. Put the full rule in the caption and use that space for the takeaway.
- **(f) Five-second read.** **Yes.** Mean error keeps falling while fall-risk-group error turns and eventually exceeds its starting level. The end labels and dashed baseline carry that point.
- **(g) Fix.** Remove the ring at `(600, 646)`. Use a small orange point at the true minimum with a lower-left callout, or drop the turning-point marker and label the orange crossing of the starting level near `(1230, 436)` as “Back to starting error.” Direct-label the orange series “StaBLE fall-risk group.”

## 2. `edit-effect-scatter.png` · **Fix**

- **(a) Collisions.** Several marks overlap, especially the two open circles near `(555, 310)`, the cluster around `(710–785, 695–745)`, and the orange pair near `(910, 870)`.
- **(b–c) Lines and arrows.** Around `(880–925, 740–990)`, several markers straddle the blue acceptance boundary. Their colors give the gate decision, but their edges make the geometry look inconsistent. The line has no arrows, and the accepted side has to be inferred from the points and shading.
- **(d–e) Size and caption.** The zero labels and axis titles are around 10–11 px. The three-line paragraph in the legend repeats the visual argument. Its last phrase, “the majority decides,” also overstates a rule that still gives the tail some weight.
- **(f) Five-second read.** **Partial.** The orange points make accepted tail harm visible. A reader has to inspect the legend to connect it to the 12.5% weight, and the negative-correlation premise is easy to miss.
- **(g) Fix.** Shrink the near-boundary marks and draw the boundary behind them. Label its right side “Accepted” and label the region below zero “Tail loses.” Move the 12.5% weight into the headline or directly beside the boundary. Identify the negative-correlation scenario in a short subtitle and move the explanatory paragraph to the caption.

## 3. `drift-sign-map.png` · **Fix**

- **(a) Collisions.** No text collisions observed. The three rings at `π = 0.125` are distinct.
- **(b–c) Lines and arrows.** The vertical guide at `x = 605` crosses all three curves intentionally. The confusion is the orange fill: it extends to the solid equal-spread curve, so parts of the shaded region lie above the dashed or dotted threshold and represent gain for those spreads. There are no arrows.
- **(d–e) Size and caption.** Tick labels, subscripts, and the equal-spread shading note are small. That note is essential to interpreting the fill and deserves a direct label. The “20 tail people in 160” example is worth keeping if the figure specifies that this corresponds to `π = 0.125` under equal per-person weighting.
- **(f) Five-second read.** **Partial.** The three curves communicate that weight and relative spread change the threshold. The equal-spread result `ρ* = −0.143` takes a legend lookup, and the figure gives no visible cue that evaluation noise leaves the threshold unchanged under the model.
- **(g) Fix.** Direct-label the solid-line ring at `(605, 706)` with `ρ* = −0.143`. Lighten the fill and label it inside the plot “Harm for equal spreads.” Use “Expected tail gain above each curve” to explain how to read the other two boundaries. Add a short model note about evaluation noise.

## 4. `timing-regimes-geometry.png` · **Redraw**

- **(a) Collisions.** No literal text overlap. The mean- and majority-optimum labels compete for two blue dots only 105 source px apart, about 35 px at display size.
- **(b–c) Lines and arrows.** The arrowheads at roughly `(1198, 674)`, `(1207, 655)`, and `(1262, 705)` point toward the same mean optimum but stop in three different places. Their direction is readable. Their shared destination is less clear. The path from seed 2 crosses into the shaded ball near `(510, 583)` with no marker, even though that transition explains the inverted U.
- **(d–e) Size and caption.** Seed labels and inset axis labels are around 10–11 px. Give the trajectories and their matching regime names priority. Move the explanation of the inverted U’s final height relative to baseline to the caption if that endpoint is specific to the example.
- **(f) Five-second read.** **No.** A reader can name the three regimes but has to match numbers across the figure and infer how the paths produce them. Two seeds start outside the ball and have different outcomes. Whether the path enters the ball is the distinction the graphic needs to show.
- **(g) Fix.** Make all three trajectories visibly converge on the mean optimum at `(1235, 680)`. Mark seed 2’s entry into the ball and use the same mark at the peak of its inset. Label the outside routes “Stays outside” and “Enters the ball,” and the third “Starts inside.” Use the same identifiers on the paths and insets. Change the shaded-region label to “Expected tail gain is negative inside the ball.”

## 5. `guarantee-validity-and-price.png` · **Fix**

- **(a) Collisions.** The two green markers at `n = 10`, around `(1813, 654)` and `(1813, 665)`, are only 11 source px apart and overlap. At display size they largely read as one mark.
- **(b–c) Lines and arrows.** The green series genuinely cross near `n = 9`, but their matching color and marker shape make them hard to follow through the crossing. There are no arrows. On the left, the colored horizontal marks have ambiguous endpoints because the figure gives no definition of what their span represents.
- **(d–e) Size and caption.** The left panel’s log ticks, probability label, and method labels are small. Keep “Preliminary simulation” visible. Move the bottom scenario note into the caption and define `M`, the comparison baseline and horizon, what the horizontal spans represent, and the denominator for majority gain kept.
- **(f) Five-second read.** **Partial.** The 5% line makes the split between methods legible. It takes longer to tell that the orange cumulative method reuses people, that certification is at checkpoints, and that both estimated gain curves rise with sample size.
- **(g) Fix.** Use “Cumulative, reused people” and “Checkpoint certification” as method labels. Give fresh people and certification distinct marker shapes as well as line styles. Label the oracle at its displayed value or align it with 100% if the normalization defines it as 100%. The current line at `y ≈ 258` sits visibly below the 100% tick at `y ≈ 240`.

## 6. `instrumented-loop.png` · **Redraw**

- **(a) Collisions.** No text overlaps. The isolated “50” in the sealed test box looks like a detached label.
- **(b–c) Lines and arrows.** The two inputs to the drift log are visible, but “tail effect on guard × gate decision” reads like multiplication. The arrow from Forecast to Sealed test people, around `(2030, 1108) → (1710, 1108)`, makes the forecast look like an input to test scoring. The reader needs to see the frozen prediction and the independently measured outcome meeting at a comparison.
- **(d–e) Size and caption.** Connector labels and body copy display around 10–11 px. The examples of editable harness components and the prose around `S > τ` can move into the caption. “All candidates,” “keep/reject,” “frozen at generation 10,” and “measured at generation 50” need the space.
- **(f) Five-second read.** **No.** The feedback loop is immediate. Scoring every candidate, joining each score to its gate decision, and checking a forecast with a sealed test set take a full trace of the diagram.
- **(g) Fix.** Preserve the proposer fan-out to development and guard, and put “All K candidates” on the guard branch. Label the two arrows entering the log “Keep/reject by candidate” and “Guard tail effect by candidate.” Replace the bottom arrow with two inputs to a comparison node: “Forecast frozen at gen 10” and “Tail change measured at gen 50 on sealed test.” Use gray for guard to match figure 7.

## 7. `stable-person-splits.png` · **Fix**

- **(a) Collisions.** No collisions. The cells and headers have adequate separation.
- **(b–c) Lines and arrows.** No competing lines or arrows. The test diagonal and the guard wrap from block 5 to block 1 are legible in the matrix.
- **(d–e) Size and caption.** The stratification statement is around 10 px in the footer, even though it is a key design choice. The guard and test legend descriptions can be shorter. The usable-video eligibility detail can move to the caption.
- **(f) Five-second read.** **Yes for the rotation.** A reader sees one test block, one guard block, and three development blocks per fold. The same reader can easily miss that these are person-level StaBLE blocks stratified by fall-risk status.
- **(g) Fix.** Add “StaBLE person-level folds” in the empty band above the column headers. Elevate “171 people in five blocks, stratified by fall-risk status” to a readable subtitle. In the legend, label the test count “about 34 per fold” and name the role “Sealed test.”

## 8. `dose-response-design.png` · **Fix**

- **(a) Collisions.** No text overlaps. The dashed rule at `x = 1450` fits in the 20 px gutter but has only about 3 px of clearance from each cell at display size.
- **(b–c) Lines and arrows.** The rule looks like a quantitatively positioned threshold, yet it is halfway between the equally spaced `0.20` and `0.40` column centers. On a numeric scale that midpoint would read as `0.30`. There are no arrows.
- **(d–e) Size and caption.** Signs and values are readable. The units and assumed `ρ = −0.3` are relegated to roughly 10 px. Keep the outcome unit with the grid and move the model assumptions to the caption. The figure currently gives no visible indication that this is the Global-MMLU design.
- **(f) Five-second read.** **Partial.** The orange and blue columns make the sign change obvious. The size effect is easy to miss. At `π = 0.40`, predicted gain rises from `+0.083` to `+0.123` as the evaluation grows. The negative columns change very little at the displayed precision.
- **(g) Fix.** Replace the full-height rule with a bracket spanning `0.20` to `0.40` and label it “Predicted flip near π = 0.23.” If a marker needs to show the exact location, give it a separate proportional axis. Add “Global-MMLU predicted tail drift” above the grid and a short callout beside the gain column showing `+0.083 → +0.123` as evaluation size rises.
tokens used
57,123
Figures 4 and 6 need redraws because their connectors obscure the mechanisms they’re meant to explain. The other six need targeted fixes. The clearest visible collision is in figure 1, where the turning-point marker touches the blue curve and makes the turn look like a crossover event.

Coordinates below are approximate native PNG pixels measured from the upper-left corner. At 850 px wide, a 30 px source label displays at roughly 10–11 px.

## 1. `concept-mean-vs-tail.png` · **Fix**

- **(a) Collisions.** The orange ring at `(600, 646)` touches the blue curve. It also sits just to the right of the orange minimum, around `(570, 648)`. The marker, the minimum, and the crossing of the two curves read as one event.
- **(b–c) Lines and arrows.** Both crossings of the dashed start line are meaningful and clear. The orange ring obscures the blue–orange crossing. There are no directional arrows.
- **(d–e) Size and caption.** “Worse,” “start,” and “better” are around 11 px at display size. The long title takes the most prominent position but describes the rule more clearly than the result. Put the full rule in the caption and use that space for the takeaway.
- **(f) Five-second read.** **Yes.** Mean error keeps falling while fall-risk-group error turns and eventually exceeds its starting level. The end labels and dashed baseline carry that point.
- **(g) Fix.** Remove the ring at `(600, 646)`. Use a small orange point at the true minimum with a lower-left callout, or drop the turning-point marker and label the orange crossing of the starting level near `(1230, 436)` as “Back to starting error.” Direct-label the orange series “StaBLE fall-risk group.”

## 2. `edit-effect-scatter.png` · **Fix**

- **(a) Collisions.** Several marks overlap, especially the two open circles near `(555, 310)`, the cluster around `(710–785, 695–745)`, and the orange pair near `(910, 870)`.
- **(b–c) Lines and arrows.** Around `(880–925, 740–990)`, several markers straddle the blue acceptance boundary. Their colors give the gate decision, but their edges make the geometry look inconsistent. The line has no arrows, and the accepted side has to be inferred from the points and shading.
- **(d–e) Size and caption.** The zero labels and axis titles are around 10–11 px. The three-line paragraph in the legend repeats the visual argument. Its last phrase, “the majority decides,” also overstates a rule that still gives the tail some weight.
- **(f) Five-second read.** **Partial.** The orange points make accepted tail harm visible. A reader has to inspect the legend to connect it to the 12.5% weight, and the negative-correlation premise is easy to miss.
- **(g) Fix.** Shrink the near-boundary marks and draw the boundary behind them. Label its right side “Accepted” and label the region below zero “Tail loses.” Move the 12.5% weight into the headline or directly beside the boundary. Identify the negative-correlation scenario in a short subtitle and move the explanatory paragraph to the caption.

## 3. `drift-sign-map.png` · **Fix**

- **(a) Collisions.** No text collisions observed. The three rings at `π = 0.125` are distinct.
- **(b–c) Lines and arrows.** The vertical guide at `x = 605` crosses all three curves intentionally. The confusion is the orange fill: it extends to the solid equal-spread curve, so parts of the shaded region lie above the dashed or dotted threshold and represent gain for those spreads. There are no arrows.
- **(d–e) Size and caption.** Tick labels, subscripts, and the equal-spread shading note are small. That note is essential to interpreting the fill and deserves a direct label. The “20 tail people in 160” example is worth keeping if the figure specifies that this corresponds to `π = 0.125` under equal per-person weighting.
- **(f) Five-second read.** **Partial.** The three curves communicate that weight and relative spread change the threshold. The equal-spread result `ρ* = −0.143` takes a legend lookup, and the figure gives no visible cue that evaluation noise leaves the threshold unchanged under the model.
- **(g) Fix.** Direct-label the solid-line ring at `(605, 706)` with `ρ* = −0.143`. Lighten the fill and label it inside the plot “Harm for equal spreads.” Use “Expected tail gain above each curve” to explain how to read the other two boundaries. Add a short model note about evaluation noise.

## 4. `timing-regimes-geometry.png` · **Redraw**

- **(a) Collisions.** No literal text overlap. The mean- and majority-optimum labels compete for two blue dots only 105 source px apart, about 35 px at display size.
- **(b–c) Lines and arrows.** The arrowheads at roughly `(1198, 674)`, `(1207, 655)`, and `(1262, 705)` point toward the same mean optimum but stop in three different places. Their direction is readable. Their shared destination is less clear. The path from seed 2 crosses into the shaded ball near `(510, 583)` with no marker, even though that transition explains the inverted U.
- **(d–e) Size and caption.** Seed labels and inset axis labels are around 10–11 px. Give the trajectories and their matching regime names priority. Move the explanation of the inverted U’s final height relative to baseline to the caption if that endpoint is specific to the example.
- **(f) Five-second read.** **No.** A reader can name the three regimes but has to match numbers across the figure and infer how the paths produce them. Two seeds start outside the ball and have different outcomes. Whether the path enters the ball is the distinction the graphic needs to show.
- **(g) Fix.** Make all three trajectories visibly converge on the mean optimum at `(1235, 680)`. Mark seed 2’s entry into the ball and use the same mark at the peak of its inset. Label the outside routes “Stays outside” and “Enters the ball,” and the third “Starts inside.” Use the same identifiers on the paths and insets. Change the shaded-region label to “Expected tail gain is negative inside the ball.”

## 5. `guarantee-validity-and-price.png` · **Fix**

- **(a) Collisions.** The two green markers at `n = 10`, around `(1813, 654)` and `(1813, 665)`, are only 11 source px apart and overlap. At display size they largely read as one mark.
- **(b–c) Lines and arrows.** The green series genuinely cross near `n = 9`, but their matching color and marker shape make them hard to follow through the crossing. There are no arrows. On the left, the colored horizontal marks have ambiguous endpoints because the figure gives no definition of what their span represents.
- **(d–e) Size and caption.** The left panel’s log ticks, probability label, and method labels are small. Keep “Preliminary simulation” visible. Move the bottom scenario note into the caption and define `M`, the comparison baseline and horizon, what the horizontal spans represent, and the denominator for majority gain kept.
- **(f) Five-second read.** **Partial.** The 5% line makes the split between methods legible. It takes longer to tell that the orange cumulative method reuses people, that certification is at checkpoints, and that both estimated gain curves rise with sample size.
- **(g) Fix.** Use “Cumulative, reused people” and “Checkpoint certification” as method labels. Give fresh people and certification distinct marker shapes as well as line styles. Label the oracle at its displayed value or align it with 100% if the normalization defines it as 100%. The current line at `y ≈ 258` sits visibly below the 100% tick at `y ≈ 240`.

## 6. `instrumented-loop.png` · **Redraw**

- **(a) Collisions.** No text overlaps. The isolated “50” in the sealed test box looks like a detached label.
- **(b–c) Lines and arrows.** The two inputs to the drift log are visible, but “tail effect on guard × gate decision” reads like multiplication. The arrow from Forecast to Sealed test people, around `(2030, 1108) → (1710, 1108)`, makes the forecast look like an input to test scoring. The reader needs to see the frozen prediction and the independently measured outcome meeting at a comparison.
- **(d–e) Size and caption.** Connector labels and body copy display around 10–11 px. The examples of editable harness components and the prose around `S > τ` can move into the caption. “All candidates,” “keep/reject,” “frozen at generation 10,” and “measured at generation 50” need the space.
- **(f) Five-second read.** **No.** The feedback loop is immediate. Scoring every candidate, joining each score to its gate decision, and checking a forecast with a sealed test set take a full trace of the diagram.
- **(g) Fix.** Preserve the proposer fan-out to development and guard, and put “All K candidates” on the guard branch. Label the two arrows entering the log “Keep/reject by candidate” and “Guard tail effect by candidate.” Replace the bottom arrow with two inputs to a comparison node: “Forecast frozen at gen 10” and “Tail change measured at gen 50 on sealed test.” Use gray for guard to match figure 7.

## 7. `stable-person-splits.png` · **Fix**

- **(a) Collisions.** No collisions. The cells and headers have adequate separation.
- **(b–c) Lines and arrows.** No competing lines or arrows. The test diagonal and the guard wrap from block 5 to block 1 are legible in the matrix.
- **(d–e) Size and caption.** The stratification statement is around 10 px in the footer, even though it is a key design choice. The guard and test legend descriptions can be shorter. The usable-video eligibility detail can move to the caption.
- **(f) Five-second read.** **Yes for the rotation.** A reader sees one test block, one guard block, and three development blocks per fold. The same reader can easily miss that these are person-level StaBLE blocks stratified by fall-risk status.
- **(g) Fix.** Add “StaBLE person-level folds” in the empty band above the column headers. Elevate “171 people in five blocks, stratified by fall-risk status” to a readable subtitle. In the legend, label the test count “about 34 per fold” and name the role “Sealed test.”

## 8. `dose-response-design.png` · **Fix**

- **(a) Collisions.** No text overlaps. The dashed rule at `x = 1450` fits in the 20 px gutter but has only about 3 px of clearance from each cell at display size.
- **(b–c) Lines and arrows.** The rule looks like a quantitatively positioned threshold, yet it is halfway between the equally spaced `0.20` and `0.40` column centers. On a numeric scale that midpoint would read as `0.30`. There are no arrows.
- **(d–e) Size and caption.** Signs and values are readable. The units and assumed `ρ = −0.3` are relegated to roughly 10 px. Keep the outcome unit with the grid and move the model assumptions to the caption. The figure currently gives no visible indication that this is the Global-MMLU design.
- **(f) Five-second read.** **Partial.** The orange and blue columns make the sign change obvious. The size effect is easy to miss. At `π = 0.40`, predicted gain rises from `+0.083` to `+0.123` as the evaluation grows. The negative columns change very little at the displayed precision.
- **(g) Fix.** Replace the full-height rule with a bracket spanning `0.20` to `0.40` and label it “Predicted flip near π = 0.23.” If a marker needs to show the exact location, give it a separate proportional axis. Add “Global-MMLU predicted tail drift” above the grid and a short callout beside the gain column showing `+0.083 → +0.123` as evaluation size rises.
