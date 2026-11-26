The biggest ship blockers are in Figures **4, 5, and 7**. Figure 4 leaves the feedback path ambiguous, Figure 5 makes a second layer of meaning depend on faint column shading, and Figure 7 lets group separation look like evidence of ranking within groups.

Coordinates below are approximate `(x, y)` positions in the original PNGs, measured from the upper left. At 850 px wide, most secondary labels render at about 10–11 px.

## 1. `one-output-four-encodings.png` — **Fix**

- **(a) Text collisions.** None visible. The four rows have enough room for their labels.
- **(b) Crossings.** The four arrows run cleanly between the left panel and the encoding cards.
- **(c) Arrow ambiguity.** Direction and destinations are clear. The two line traces are unlabeled, so a reader has to infer that they are the two coordinates of the same path.
- **(d) Readability.** The sample rows, summary values, and token badges are about 10–11 px at display size. The badge text carries the main comparison and should be larger. The `1 cm` label survives, but its bar is only about 23 px wide.
- **(e) Caption material.** Move the recording setup and the frame-count arithmetic to the caption. Keep “illustrative” visible by the examples.
- **(f) Five-second read.** One path can be shown four ways. **Yes** for that structure, **partial** for the token and information trade-off. The equally prominent badges make the reader work through eight separate claims.
- **(g) Fix.** Enlarge and align the token counts at `x≈2012` as a single comparison column. Below each count, use one parallel retention statement. In the line-plot thumbnail at `(872, 828)`, identify the two traces and label the horizontal axis “time.” In the summary thumbnail at `(872, 538)`, change “ellipse” to “95% ellipse area” if that is the statistic intended.

## 2. `risk-decomposition.png` — **Fix**

- **(a) Text collisions.** None visible. The recalibrated-reader subscript at `(1820, 575)` is dense enough to look like a separate row of notation.
- **(b) Crossings.** No lines cross text. The blue bracket correctly spans resolution and calibration.
- **(c) Arrow ambiguity.** There are no arrows. The left-to-right risk direction depends on the subtitle, while the nearly equal segment widths can be read as relative magnitudes.
- **(d) Readability.** The block labels survive. The subscripts and two-line “best possible render decoder” label slow down the boundary-to-decoder mapping at 850 px.
- **(e) Caption material.** Move the explanation of how each decoder is constructed to the caption. Keep “schematic widths” and short decoder names in the figure.
- **(f) Five-second read.** Reader risk accumulates from the tool floor through information loss and perception. **Yes** for the split. Identifying which decoder defines each boundary takes longer.
- **(g) Fix.** Put a small “increasing risk →” cue near the bar. At the five ticks (`x≈180, 680, 1200, 1820, 2300`), use consistent stacks with a short name on one line and notation on the next. Rename the orange block “information loss” and keep \(I(r)\) alongside it.

## 3. `oracle-learning-curve.png` — **Fix**

- **(a) Text collisions.** None visible.
- **(b) Crossings.** The orange curve crosses the blue reader line once, which is the meaningful sign change. The vertical gap markers are close enough in style to the dashed floor that they compete with the plot lines.
- **(c) Arrow ambiguity.** There are no arrows. Both vertical markers show distance, so the signs depend on reading the equation in the subtitle and the numbers beside the markers.
- **(d) Readability.** Axis labels and legend are readable. The distinction between `0.0079` and `0.0087 cm²` requires a close read, especially because the numbers sit in different parts of the figure.
- **(e) Caption material.** Move the 20 px bar height, k-nearest-neighbour detail, and exact gap values to the caption. Keep “preliminary simulation” and the subtraction order visible.
- **(f) Five-second read.** A weak oracle can put the estimated gap on the wrong side of zero, and more training brings it near the true gap. **Partial.** The title gives away the first half. The second requires matching the dashed floor, orange markers, and sidebar number.
- **(g) Fix.** At `x≈428` and `x≈1233`, use capped vertical brackets and the labels “negative estimate” and “near true gap.” Direct-label the blue reader line and dashed floor near their right ends. Make the title conditional and include the recovery, for example “More oracle training brings the gap estimate near its true value.”

## 4. `renderer-evolution-loop.png` — **Redraw**

- **(a) Text collisions.** None visible.
- **(b) Crossings.** No literal crossings. The two left-going return paths at `y≈834` and `y≈1104` make readers trace the loop twice to learn that error tables and parent code both go to the mutator.
- **(c) Arrow ambiguity.** The “Error tables” box names probe errors, but its only drawn source is Reader A. The dashed archive arrow at `x≈1200` stops at the scoring enclosure, leaving the relationship between checkpoints and the three evaluation boxes implicit.
- **(d) Readability.** “dev-train,” “dev-select,” and the two return-path labels are about 11 px. They are as visually prominent as node descriptions, although they define different data paths.
- **(e) Caption material.** Move model and tool versions, the MAP-Elites descriptor, the checkpoint count, and held-out task examples to the caption. Keep the split names, what the mutator receives, and when held-out scoring occurs.
- **(f) Five-second read.** Search uses development data and the fitness reader; held-out evaluation happens afterward. **Partial.** The red enclosure signals separation. The mutator’s inputs and the distinction between feedback and selection take much longer.
- **(g) Fix.** Put `Renderer → Images → Fitness reader` on one row. Below it, draw two clearly labeled branches from the reader: `dev-train → error tables → mutator` and `dev-select → fitness → archive → mutator`. Put “error tables” and “parent code” on the mutator’s incoming edges and “child code” on its outgoing edge. Draw a source for probe errors or move that detail to the caption. Route `archive → saved checkpoints → post-search evaluation` to an explicit node that branches to participants, readers, and tasks.

## 5. `reader-design-matrix.png` — **Redraw**

- **(a) Text collisions.** None visible. The final row label at `(149, 1070)` is long and forces readers to scan across a wide, dense row.
- **(b) Crossings.** The dashed row divider at `y≈750` crosses the gray column bands without touching any symbols. Adjacent shaded bands visually merge around `x≈1232–1456` and `x≈2076–2300`, weakening the column boundaries.
- **(c) Arrow ambiguity.** There are no arrows. The diamond in the crowd column at `(2508, 1072)` sits on a “never sets fitness” band even though the crowd profile feeds a predictor used by that condition. Direct scoring versus indirect contribution takes careful legend reading.
- **(d) Readability.** The model headers and five legend entries render at roughly 9–10 px. The two adjacent `≈8B` headers under “Other open” are indistinguishable even at full size.
- **(e) Caption material.** Put the full model inventory and the crowd-predictor explanation in the caption or an accompanying table. The figure needs short, unique reader labels.
- **(f) Five-second read.** Each fitness condition leaves other families available for evaluation. **Partial.** The blue dots reveal who sets fitness. Same-family holdouts and columns that never set fitness take a legend lookup and a second pass.
- **(g) Fix.** Group columns by family and put a labeled header marker above each permanently held-out reader. Keep blue dots and squares for fitness and same-family holdouts, with a lighter mark for cross-family or human evaluation. Give the two “Other open” readers distinct names. Put the crowd-profile diamond beside the final condition label with a short note about its indirect role.

## 6. `transfer-decomposition-curve.png` — **Fix**

- **(a) Text collisions.** None visible. The long title and subtitle demand more reading than the two-panel comparison.
- **(b) Crossings.** No confusing crossings. The three curves converge near generation zero, where the solid and dashed green traces are briefly hard to distinguish.
- **(c) Arrow ambiguity.** There are no arrows. The end brackets identify the absolute vertical differences. The reader must infer that `55%` and `11%` divide those differences by Reader A’s gain in each panel.
- **(d) Readability.** The percentages survive at 850 px. The metric at `(244, 339)` looks like an annotation on the left panel, and readers may miss that it applies to both.
- **(e) Caption material.** Move the normalization formula and the definition of the unshared percentage to the caption. Use the panel titles to name the two fitness conditions and retain a prominent “Illustrative hypothesis” label.
- **(f) Five-second read.** Held-out VLMs share more of Reader A’s gain under cross-family fitness. **Yes.** The narrowing pink area is immediate. The exact percentages look like results despite the illustrative label.
- **(g) Fix.** Use one shared y-axis title. End-label the blue and solid green series where space permits. Replace the brackets beside `x≈1104` and `x≈2284` with “larger unshared gain” and “smaller unshared gain,” or keep the numbers and label them “example percentages” beside the brackets.

## 7. `profile-predicts-transfer.png` — **Redraw**

- **(a) Text collisions.** None visible. **Mark-on-mark collisions are substantial.** In the right panel, open green markers overlap along `x≈1905`, hiding how many observations are present. The left panel also has close pairs around `(745, 755)` and `(850, 705)`.
- **(b) Crossings.** The dashed equality line passes through dense points near the center of both panels. It invites a calibration reading even though the stated outcome is rank.
- **(c) Arrow ambiguity.** There are no arrows. The ambiguity is what a point represents. The subtitle describes checkpoint centering without saying whether each point is one reader at one checkpoint or an aggregate.
- **(d) Readability.** The correlation callouts are clear. The repeated x-axis labels and in-plot y-axis labels are about 10 px, and the stacked markers remain hard to count at any reasonable text size.
- **(e) Caption material.** Move the centering procedure and the definition of a point to the caption. Keep “within checkpoint,” “illustrative,” and the metric used to compare rank visible.
- **(f) Five-second read.** The profile rule shows a stronger overall association with observed gains. **Yes.** Whether it ranks readers *within* family groups is **unclear**. A pooled Spearman can reward group separation, and the gray baseline points show some horizontal variation.
- **(g) Fix.** For a ranking claim, plot forecast rank against observed rank with tied ranks shown explicitly, or show within-family rank associations beside the pooled values. In the current layout, replace the overlapping baseline stack at `x≈1905` with a strip display using small horizontal offsets identified as jitter. Drop the `y=x` line unless calibration is part of the claim. Qualify “only separates groups” if the gray group’s horizontal variation encodes genuine within-group predictions.

## 8. `co-adaptation-drift.png` — **Fix**

- **(a) Text collisions.** None visible.
- **(b) Crossings.** No confusing crossings. The green point at round 1 in the left panel sits on zero, where it is still distinguishable by its square marker.
- **(c) Arrow ambiguity.** There are no arrows. Both brackets clearly connect the two round-4 endpoints. “Fresh readers” leaves open whether the frozen reader used in fitness also contributes to the green evaluation series.
- **(d) Readability.** The gap labels and markers are readable at 850 px. The in-panel y-axis description is small and duplicated by neither a shared axis label nor a definition.
- **(e) Caption material.** Move “H5” and the exact illustrative gap values to the caption. Keep the definition of zero next to the axis because it changes how readers interpret the negative values.
- **(f) Five-second read.** Standard co-adaptation opens a gap, and adding a frozen-reader term keeps it smaller. **Yes.** A reader cannot recover from the figure that negative skill means worse than predicting the mean. The right panel also shows lower co-adapted-pair skill, which the gap label alone obscures.
- **(g) Fix.** Replace “skill on sealed test participants” at `(264, 365)` with a shared label, “Skill = 1 − normalized error.” Add “predict-the-mean baseline” at the zero line (`y≈753`). Identify which fresh readers contribute to the green series and whether they are held out from fitness. Keep the same axes across panels so both the narrower gap and the lower blue endpoint remain visible.
tokens used
57,732
The biggest ship blockers are in Figures **4, 5, and 7**. Figure 4 leaves the feedback path ambiguous, Figure 5 makes a second layer of meaning depend on faint column shading, and Figure 7 lets group separation look like evidence of ranking within groups.

Coordinates below are approximate `(x, y)` positions in the original PNGs, measured from the upper left. At 850 px wide, most secondary labels render at about 10–11 px.

## 1. `one-output-four-encodings.png` — **Fix**

- **(a) Text collisions.** None visible. The four rows have enough room for their labels.
- **(b) Crossings.** The four arrows run cleanly between the left panel and the encoding cards.
- **(c) Arrow ambiguity.** Direction and destinations are clear. The two line traces are unlabeled, so a reader has to infer that they are the two coordinates of the same path.
- **(d) Readability.** The sample rows, summary values, and token badges are about 10–11 px at display size. The badge text carries the main comparison and should be larger. The `1 cm` label survives, but its bar is only about 23 px wide.
- **(e) Caption material.** Move the recording setup and the frame-count arithmetic to the caption. Keep “illustrative” visible by the examples.
- **(f) Five-second read.** One path can be shown four ways. **Yes** for that structure, **partial** for the token and information trade-off. The equally prominent badges make the reader work through eight separate claims.
- **(g) Fix.** Enlarge and align the token counts at `x≈2012` as a single comparison column. Below each count, use one parallel retention statement. In the line-plot thumbnail at `(872, 828)`, identify the two traces and label the horizontal axis “time.” In the summary thumbnail at `(872, 538)`, change “ellipse” to “95% ellipse area” if that is the statistic intended.

## 2. `risk-decomposition.png` — **Fix**

- **(a) Text collisions.** None visible. The recalibrated-reader subscript at `(1820, 575)` is dense enough to look like a separate row of notation.
- **(b) Crossings.** No lines cross text. The blue bracket correctly spans resolution and calibration.
- **(c) Arrow ambiguity.** There are no arrows. The left-to-right risk direction depends on the subtitle, while the nearly equal segment widths can be read as relative magnitudes.
- **(d) Readability.** The block labels survive. The subscripts and two-line “best possible render decoder” label slow down the boundary-to-decoder mapping at 850 px.
- **(e) Caption material.** Move the explanation of how each decoder is constructed to the caption. Keep “schematic widths” and short decoder names in the figure.
- **(f) Five-second read.** Reader risk accumulates from the tool floor through information loss and perception. **Yes** for the split. Identifying which decoder defines each boundary takes longer.
- **(g) Fix.** Put a small “increasing risk →” cue near the bar. At the five ticks (`x≈180, 680, 1200, 1820, 2300`), use consistent stacks with a short name on one line and notation on the next. Rename the orange block “information loss” and keep \(I(r)\) alongside it.

## 3. `oracle-learning-curve.png` — **Fix**

- **(a) Text collisions.** None visible.
- **(b) Crossings.** The orange curve crosses the blue reader line once, which is the meaningful sign change. The vertical gap markers are close enough in style to the dashed floor that they compete with the plot lines.
- **(c) Arrow ambiguity.** There are no arrows. Both vertical markers show distance, so the signs depend on reading the equation in the subtitle and the numbers beside the markers.
- **(d) Readability.** Axis labels and legend are readable. The distinction between `0.0079` and `0.0087 cm²` requires a close read, especially because the numbers sit in different parts of the figure.
- **(e) Caption material.** Move the 20 px bar height, k-nearest-neighbour detail, and exact gap values to the caption. Keep “preliminary simulation” and the subtraction order visible.
- **(f) Five-second read.** A weak oracle can put the estimated gap on the wrong side of zero, and more training brings it near the true gap. **Partial.** The title gives away the first half. The second requires matching the dashed floor, orange markers, and sidebar number.
- **(g) Fix.** At `x≈428` and `x≈1233`, use capped vertical brackets and the labels “negative estimate” and “near true gap.” Direct-label the blue reader line and dashed floor near their right ends. Make the title conditional and include the recovery, for example “More oracle training brings the gap estimate near its true value.”

## 4. `renderer-evolution-loop.png` — **Redraw**

- **(a) Text collisions.** None visible.
- **(b) Crossings.** No literal crossings. The two left-going return paths at `y≈834` and `y≈1104` make readers trace the loop twice to learn that error tables and parent code both go to the mutator.
- **(c) Arrow ambiguity.** The “Error tables” box names probe errors, but its only drawn source is Reader A. The dashed archive arrow at `x≈1200` stops at the scoring enclosure, leaving the relationship between checkpoints and the three evaluation boxes implicit.
- **(d) Readability.** “dev-train,” “dev-select,” and the two return-path labels are about 11 px. They are as visually prominent as node descriptions, although they define different data paths.
- **(e) Caption material.** Move model and tool versions, the MAP-Elites descriptor, the checkpoint count, and held-out task examples to the caption. Keep the split names, what the mutator receives, and when held-out scoring occurs.
- **(f) Five-second read.** Search uses development data and the fitness reader; held-out evaluation happens afterward. **Partial.** The red enclosure signals separation. The mutator’s inputs and the distinction between feedback and selection take much longer.
- **(g) Fix.** Put `Renderer → Images → Fitness reader` on one row. Below it, draw two clearly labeled branches from the reader: `dev-train → error tables → mutator` and `dev-select → fitness → archive → mutator`. Put “error tables” and “parent code” on the mutator’s incoming edges and “child code” on its outgoing edge. Draw a source for probe errors or move that detail to the caption. Route `archive → saved checkpoints → post-search evaluation` to an explicit node that branches to participants, readers, and tasks.

## 5. `reader-design-matrix.png` — **Redraw**

- **(a) Text collisions.** None visible. The final row label at `(149, 1070)` is long and forces readers to scan across a wide, dense row.
- **(b) Crossings.** The dashed row divider at `y≈750` crosses the gray column bands without touching any symbols. Adjacent shaded bands visually merge around `x≈1232–1456` and `x≈2076–2300`, weakening the column boundaries.
- **(c) Arrow ambiguity.** There are no arrows. The diamond in the crowd column at `(2508, 1072)` sits on a “never sets fitness” band even though the crowd profile feeds a predictor used by that condition. Direct scoring versus indirect contribution takes careful legend reading.
- **(d) Readability.** The model headers and five legend entries render at roughly 9–10 px. The two adjacent `≈8B` headers under “Other open” are indistinguishable even at full size.
- **(e) Caption material.** Put the full model inventory and the crowd-predictor explanation in the caption or an accompanying table. The figure needs short, unique reader labels.
- **(f) Five-second read.** Each fitness condition leaves other families available for evaluation. **Partial.** The blue dots reveal who sets fitness. Same-family holdouts and columns that never set fitness take a legend lookup and a second pass.
- **(g) Fix.** Group columns by family and put a labeled header marker above each permanently held-out reader. Keep blue dots and squares for fitness and same-family holdouts, with a lighter mark for cross-family or human evaluation. Give the two “Other open” readers distinct names. Put the crowd-profile diamond beside the final condition label with a short note about its indirect role.

## 6. `transfer-decomposition-curve.png` — **Fix**

- **(a) Text collisions.** None visible. The long title and subtitle demand more reading than the two-panel comparison.
- **(b) Crossings.** No confusing crossings. The three curves converge near generation zero, where the solid and dashed green traces are briefly hard to distinguish.
- **(c) Arrow ambiguity.** There are no arrows. The end brackets identify the absolute vertical differences. The reader must infer that `55%` and `11%` divide those differences by Reader A’s gain in each panel.
- **(d) Readability.** The percentages survive at 850 px. The metric at `(244, 339)` looks like an annotation on the left panel, and readers may miss that it applies to both.
- **(e) Caption material.** Move the normalization formula and the definition of the unshared percentage to the caption. Use the panel titles to name the two fitness conditions and retain a prominent “Illustrative hypothesis” label.
- **(f) Five-second read.** Held-out VLMs share more of Reader A’s gain under cross-family fitness. **Yes.** The narrowing pink area is immediate. The exact percentages look like results despite the illustrative label.
- **(g) Fix.** Use one shared y-axis title. End-label the blue and solid green series where space permits. Replace the brackets beside `x≈1104` and `x≈2284` with “larger unshared gain” and “smaller unshared gain,” or keep the numbers and label them “example percentages” beside the brackets.

## 7. `profile-predicts-transfer.png` — **Redraw**

- **(a) Text collisions.** None visible. **Mark-on-mark collisions are substantial.** In the right panel, open green markers overlap along `x≈1905`, hiding how many observations are present. The left panel also has close pairs around `(745, 755)` and `(850, 705)`.
- **(b) Crossings.** The dashed equality line passes through dense points near the center of both panels. It invites a calibration reading even though the stated outcome is rank.
- **(c) Arrow ambiguity.** There are no arrows. The ambiguity is what a point represents. The subtitle describes checkpoint centering without saying whether each point is one reader at one checkpoint or an aggregate.
- **(d) Readability.** The correlation callouts are clear. The repeated x-axis labels and in-plot y-axis labels are about 10 px, and the stacked markers remain hard to count at any reasonable text size.
- **(e) Caption material.** Move the centering procedure and the definition of a point to the caption. Keep “within checkpoint,” “illustrative,” and the metric used to compare rank visible.
- **(f) Five-second read.** The profile rule shows a stronger overall association with observed gains. **Yes.** Whether it ranks readers *within* family groups is **unclear**. A pooled Spearman can reward group separation, and the gray baseline points show some horizontal variation.
- **(g) Fix.** For a ranking claim, plot forecast rank against observed rank with tied ranks shown explicitly, or show within-family rank associations beside the pooled values. In the current layout, replace the overlapping baseline stack at `x≈1905` with a strip display using small horizontal offsets identified as jitter. Drop the `y=x` line unless calibration is part of the claim. Qualify “only separates groups” if the gray group’s horizontal variation encodes genuine within-group predictions.

## 8. `co-adaptation-drift.png` — **Fix**

- **(a) Text collisions.** None visible.
- **(b) Crossings.** No confusing crossings. The green point at round 1 in the left panel sits on zero, where it is still distinguishable by its square marker.
- **(c) Arrow ambiguity.** There are no arrows. Both brackets clearly connect the two round-4 endpoints. “Fresh readers” leaves open whether the frozen reader used in fitness also contributes to the green evaluation series.
- **(d) Readability.** The gap labels and markers are readable at 850 px. The in-panel y-axis description is small and duplicated by neither a shared axis label nor a definition.
- **(e) Caption material.** Move “H5” and the exact illustrative gap values to the caption. Keep the definition of zero next to the axis because it changes how readers interpret the negative values.
- **(f) Five-second read.** Standard co-adaptation opens a gap, and adding a frozen-reader term keeps it smaller. **Yes.** A reader cannot recover from the figure that negative skill means worse than predicting the mean. The right panel also shows lower co-adapted-pair skill, which the gap label alone obscures.
- **(g) Fix.** Replace “skill on sealed test participants” at `(264, 365)` with a shared label, “Skill = 1 − normalized error.” Add “predict-the-mean baseline” at the zero line (`y≈753`). Identify which fresh readers contribute to the green series and whether they are held out from fitness. Keep the same axes across panels so both the narrower gap and the lower blue endpoint remain visible.
