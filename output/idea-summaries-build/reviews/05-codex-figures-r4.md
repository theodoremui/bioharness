**1 ships, 5 need fixes, and 2 need redraws.** I reviewed the figures in file order at an intended width of 850 px. Coordinates below refer to the supplied PNGs, measured approximately from the top left. Text sizes are estimates at display width.

### 1. `same-outputs-different-futures` — **Fix**

- **(a–c) Collisions and connectors.** No text overlaps or crossings. Both arrows clearly enter “Same outputs,” but the diagram then stops. The chart starts from a separate black dot, so the reader has to infer that the dot represents the shared baseline. The endpoint labels “S” and “A” also require a lookup across the figure.
- **(d–e) Readability and copy.** The plot annotations and box descriptions are about 10–11 px. The 400-line count and implementation details belong in the caption. “Identical scores on every input” also reads as a universal claim. If equivalence was established using the gate in Figure 3, name the tested inputs.
- **(f) Five-second read.** Yes, the two curves show different improvement from a common start. The mapping from the curves to the two harnesses takes longer.
- **(g) Fix.** Rename the center box “Same starting score” and use “Shared baseline” at the origin near `(1540, 840)`. Replace the endpoint letters near `(2325, 340)` and `(2325, 640)` with “Typed stages” and “One function.” Shorten the plot heading to free room for the direct labels, and keep “Hypothesized gap” next to the bracket.

### 2. `pipeline-two-forms` — **Fix**

- **(a–c) Collisions and connectors.** No overlaps or line crossings. The solid arrows clearly show the scoring pipeline, and the dashed arrows clearly enter the trace bar. The upper score box combines output and feedback, while the lower feedback is drawn as a separate destination. That asymmetry makes the comparison harder to see. The green stems read as annotations, though their color gives the warnings more prominence than the feedback difference.
- **(d–e) Readability and copy.** The code, config names, and trace examples shrink to roughly 10–11 px. Move the threshold loop, pose-model names, variable names, normalization detail, and full trace inventory to the caption. Keep the stage names.
- **(f) Five-second read.** Partial. One function versus a pipeline is immediate. Score error alone versus score error plus a trace requires reading two different parts of the figure.
- **(g) Fix.** Replace the code block inside the upper box near `(80, 164)` with “Cached pose → one scoring function.” Give both lanes an output box labeled “Same Y-Balance score” and a visibly distinct feedback destination with parallel wording. Use “Optimizer receives score error” in the upper lane and “Optimizer receives score error + stage trace” in the lower lane. Move the green callouts near `(796, 567)` and `(1804, 567)` to the caption.

### 3. `bpt-equivalence-gate` — **Fix**

- **(a–c) Collisions and connectors.** No overlaps or crossings. The left-to-right sequence and pass/fail branches are clear. The incoming and outgoing arrows align with the middle factor card, however, which can momentarily make “Parameters” look like the sole route through the rewrite block.
- **(d–e) Readability and copy.** Factor levels and gate copy land near 10 px. Keep the five factor names, the equal-token step, and both matching criteria. Move the list of levels, cached and fuzzed input details, and “As written” to the caption.
- **(f) Five-second read.** Mostly. Rewrite → pad → gate → admit is legible at a glance. The actual admission rule takes longer because it is set as four lines of body text.
- **(g) Fix.** Compress the rewrite group at `x≈524–1248` into a single step headed “Rewrite with one level per factor,” with the factor names underneath. Connect the arrows to that outer step. In the gate at `x≈1804–2232`, elevate “Scores and tool calls match the base” to the primary label and set it over two lines.

### 4. `single-edit-profile` — **Fix**

- **(a–c) Collisions and connectors.** No collisions or crossings. The brackets group the three sessions clearly, and the arrows show the sequence. The one-parent box feeding the proposer does leave a brief sequential reading open. A reader could interpret later edits as edits of earlier candidates.
- **(d–e) Readability and copy.** The session labels, profile details, and legend are around 10 px. “Base b, cell c” and “g, r: from per-edit errors” belong in the caption. Move the 1% threshold and guard condition there as well, so the legend can use three short category names.
- **(f) Five-second read.** Partial. The grid immediately shows three outcomes, but the reader has to drop to the legend and then return to the profile. The numbers check out. The grid shows six invalid edits and four successes among 30 proposals.
- **(g) Fix.** Relabel the grid above `(1220, 216)` as “30 edits, each from the same parent.” Move the legend from `y≈627–810` to directly below the grid and shorten it to “Invalid,” “Valid, no success,” and “Success.” In the profile box at `x≈2084–2640`, enlarge “24/30 valid (v)” and “4/30 successful (s).”

### 5. `refactor-first-break-even` — **Fix**

- **(a–c) Collisions and connectors.** No text overlaps or ambiguous arrows. The two curves cross intentionally at the marked point. The blue zero-gain segment lies directly on the horizontal axis, making it easy to miss that the refactor-first strategy is already spending budget. The bracket below the axis helps, but it requires a second look.
- **(d–e) Readability and copy.** The direct curve labels are readable. The two stacked labels below the axis are smaller, and “B*” adds a label for a point that already has one. Keep the approximate 3× relationship on the plot and put the evaluation-equivalent conversion in the caption.
- **(f) Five-second read.** Yes for the crossover. The 3× relationship is slower to retrieve. The geometry is consistent with the stated example. The refactor interval spans about 290 PNG px and the break-even point is about 865 px from the origin.
- **(g) Fix.** Lightly shade the refactor interval between `x≈260` and `550` so the blue segment remains visible against the axis. Replace “B*” near `(1150, 650)` with “Break-even ≈ 3× refactor cost in this example.” Use “Total budget” below the axis and retain the illustrative label.

### 6. `parent-selection-at-birth` — **Redraw**

- **(a–c) Collisions and connectors.** No collisions or confusing crossings. The two lines from the parent to the newborn nodes lack arrowheads. Their direction is inferable from the labels, but one arrow per method row points vaguely toward a plot and fails to identify what each newborn receives.
- **(d–e) Readability and copy.** The axes, “both nodes” labels, and supporting text are around 10 px. The two density panels and their endpoints give an illustrative prior more visual weight and apparent precision than the tie-breaking hypothesis needs. Move distribution details to the caption.
- **(f) Five-second read.** No. The reader must map the newborn pair onto a score axis, then a shared density, then two separate densities. The first two rows tie the nodes in visually different ways, which obscures the common result.
- **(g) Fix.** Keep the newborn pair at the top and add arrowheads at their boxes near `x≈440`. Replace the three method-to-plot rows below `y≈420` with three aligned rows and two labeled columns, “Degraded code” and “Structured code.” Show a shared score for DGM, a shared clade estimate for HGM, and visibly separated markers on one common scale for HGM with a code-feature prior. Label that final row “Hypothesized separation.”

### 7. `participant-splits` — **Ship**

- **(a–c) Collisions and connectors.** No overlaps or crossings. The shared trunk and three right-facing arrowheads clearly represent a split. Each arrow terminates at one cohort.
- **(d–e) Readability and copy.** The cohort headings and counts are clear at 850 px, and the body copy is about 12–13 px. The cohort roles earn their space. The 2,968-example count and lab-pilot detail could move to the caption if space is needed.
- **(f) Five-second read.** Yes. The title and branching layout establish that the person-level split comes first, and the lock distinguishes the sealed group. The counts sum to 171.
- **(g) Fix.** No shipping blocker. If revising the title near `(80, 70)`, use “Split participants before building the harnesses.” The sealed-test box already states that the final candidate is scored once per loop.

### 8. `two-tier-design` — **Redraw**

- **(a–c) Collisions and connectors.** No overlaps or arrow crossings. The dashed outlines correctly isolate cells 1 and 8. The two arrows labeled “correlate” near `x≈1700–1850` point into “Sealed-test gain,” which makes the predictors look like inputs to the gain calculation. The validation loops are described inside the outcome box, so the diagram gives the observed outcome no explicit path of its own.
- **(d–e) Readability and copy.** The dots survive at 850 px, but cell numbers, legend notes, and Tier 2 details are around 10 px. Keep the eight-cell matrix, four factor names, 96 configurations, both predictors, and observed gain. Move the cell 1 and 8 naming and control details, seed counts, and exact evaluation budgets to the caption.
- **(f) Five-second read.** Tier 1 mostly works. The matrix matches the stated \(I=MOPT\) half fraction, but “structured” and “degraded” are less precise than the two levels of each factor. Tier 2 fails the glance test because its arrows suggest a procedure different from the planned comparison.
- **(g) Fix.** Preserve the matrix at `x≈486–1518, y≈300–708` and use a compact two-level legend. Redraw everything below `y≈756` so “96 configurations” fans out to three parallel boxes: “Profile forecast,” “HGM clade estimate,” and “Observed sealed-test gain from validation loops.” Bring those three outputs into a distinct comparison box labeled “Correlate each predictor with observed gain.”
tokens used
53,524
**1 ships, 5 need fixes, and 2 need redraws.** I reviewed the figures in file order at an intended width of 850 px. Coordinates below refer to the supplied PNGs, measured approximately from the top left. Text sizes are estimates at display width.

### 1. `same-outputs-different-futures` — **Fix**

- **(a–c) Collisions and connectors.** No text overlaps or crossings. Both arrows clearly enter “Same outputs,” but the diagram then stops. The chart starts from a separate black dot, so the reader has to infer that the dot represents the shared baseline. The endpoint labels “S” and “A” also require a lookup across the figure.
- **(d–e) Readability and copy.** The plot annotations and box descriptions are about 10–11 px. The 400-line count and implementation details belong in the caption. “Identical scores on every input” also reads as a universal claim. If equivalence was established using the gate in Figure 3, name the tested inputs.
- **(f) Five-second read.** Yes, the two curves show different improvement from a common start. The mapping from the curves to the two harnesses takes longer.
- **(g) Fix.** Rename the center box “Same starting score” and use “Shared baseline” at the origin near `(1540, 840)`. Replace the endpoint letters near `(2325, 340)` and `(2325, 640)` with “Typed stages” and “One function.” Shorten the plot heading to free room for the direct labels, and keep “Hypothesized gap” next to the bracket.

### 2. `pipeline-two-forms` — **Fix**

- **(a–c) Collisions and connectors.** No overlaps or line crossings. The solid arrows clearly show the scoring pipeline, and the dashed arrows clearly enter the trace bar. The upper score box combines output and feedback, while the lower feedback is drawn as a separate destination. That asymmetry makes the comparison harder to see. The green stems read as annotations, though their color gives the warnings more prominence than the feedback difference.
- **(d–e) Readability and copy.** The code, config names, and trace examples shrink to roughly 10–11 px. Move the threshold loop, pose-model names, variable names, normalization detail, and full trace inventory to the caption. Keep the stage names.
- **(f) Five-second read.** Partial. One function versus a pipeline is immediate. Score error alone versus score error plus a trace requires reading two different parts of the figure.
- **(g) Fix.** Replace the code block inside the upper box near `(80, 164)` with “Cached pose → one scoring function.” Give both lanes an output box labeled “Same Y-Balance score” and a visibly distinct feedback destination with parallel wording. Use “Optimizer receives score error” in the upper lane and “Optimizer receives score error + stage trace” in the lower lane. Move the green callouts near `(796, 567)` and `(1804, 567)` to the caption.

### 3. `bpt-equivalence-gate` — **Fix**

- **(a–c) Collisions and connectors.** No overlaps or crossings. The left-to-right sequence and pass/fail branches are clear. The incoming and outgoing arrows align with the middle factor card, however, which can momentarily make “Parameters” look like the sole route through the rewrite block.
- **(d–e) Readability and copy.** Factor levels and gate copy land near 10 px. Keep the five factor names, the equal-token step, and both matching criteria. Move the list of levels, cached and fuzzed input details, and “As written” to the caption.
- **(f) Five-second read.** Mostly. Rewrite → pad → gate → admit is legible at a glance. The actual admission rule takes longer because it is set as four lines of body text.
- **(g) Fix.** Compress the rewrite group at `x≈524–1248` into a single step headed “Rewrite with one level per factor,” with the factor names underneath. Connect the arrows to that outer step. In the gate at `x≈1804–2232`, elevate “Scores and tool calls match the base” to the primary label and set it over two lines.

### 4. `single-edit-profile` — **Fix**

- **(a–c) Collisions and connectors.** No collisions or crossings. The brackets group the three sessions clearly, and the arrows show the sequence. The one-parent box feeding the proposer does leave a brief sequential reading open. A reader could interpret later edits as edits of earlier candidates.
- **(d–e) Readability and copy.** The session labels, profile details, and legend are around 10 px. “Base b, cell c” and “g, r: from per-edit errors” belong in the caption. Move the 1% threshold and guard condition there as well, so the legend can use three short category names.
- **(f) Five-second read.** Partial. The grid immediately shows three outcomes, but the reader has to drop to the legend and then return to the profile. The numbers check out. The grid shows six invalid edits and four successes among 30 proposals.
- **(g) Fix.** Relabel the grid above `(1220, 216)` as “30 edits, each from the same parent.” Move the legend from `y≈627–810` to directly below the grid and shorten it to “Invalid,” “Valid, no success,” and “Success.” In the profile box at `x≈2084–2640`, enlarge “24/30 valid (v)” and “4/30 successful (s).”

### 5. `refactor-first-break-even` — **Fix**

- **(a–c) Collisions and connectors.** No text overlaps or ambiguous arrows. The two curves cross intentionally at the marked point. The blue zero-gain segment lies directly on the horizontal axis, making it easy to miss that the refactor-first strategy is already spending budget. The bracket below the axis helps, but it requires a second look.
- **(d–e) Readability and copy.** The direct curve labels are readable. The two stacked labels below the axis are smaller, and “B*” adds a label for a point that already has one. Keep the approximate 3× relationship on the plot and put the evaluation-equivalent conversion in the caption.
- **(f) Five-second read.** Yes for the crossover. The 3× relationship is slower to retrieve. The geometry is consistent with the stated example. The refactor interval spans about 290 PNG px and the break-even point is about 865 px from the origin.
- **(g) Fix.** Lightly shade the refactor interval between `x≈260` and `550` so the blue segment remains visible against the axis. Replace “B*” near `(1150, 650)` with “Break-even ≈ 3× refactor cost in this example.” Use “Total budget” below the axis and retain the illustrative label.

### 6. `parent-selection-at-birth` — **Redraw**

- **(a–c) Collisions and connectors.** No collisions or confusing crossings. The two lines from the parent to the newborn nodes lack arrowheads. Their direction is inferable from the labels, but one arrow per method row points vaguely toward a plot and fails to identify what each newborn receives.
- **(d–e) Readability and copy.** The axes, “both nodes” labels, and supporting text are around 10 px. The two density panels and their endpoints give an illustrative prior more visual weight and apparent precision than the tie-breaking hypothesis needs. Move distribution details to the caption.
- **(f) Five-second read.** No. The reader must map the newborn pair onto a score axis, then a shared density, then two separate densities. The first two rows tie the nodes in visually different ways, which obscures the common result.
- **(g) Fix.** Keep the newborn pair at the top and add arrowheads at their boxes near `x≈440`. Replace the three method-to-plot rows below `y≈420` with three aligned rows and two labeled columns, “Degraded code” and “Structured code.” Show a shared score for DGM, a shared clade estimate for HGM, and visibly separated markers on one common scale for HGM with a code-feature prior. Label that final row “Hypothesized separation.”

### 7. `participant-splits` — **Ship**

- **(a–c) Collisions and connectors.** No overlaps or crossings. The shared trunk and three right-facing arrowheads clearly represent a split. Each arrow terminates at one cohort.
- **(d–e) Readability and copy.** The cohort headings and counts are clear at 850 px, and the body copy is about 12–13 px. The cohort roles earn their space. The 2,968-example count and lab-pilot detail could move to the caption if space is needed.
- **(f) Five-second read.** Yes. The title and branching layout establish that the person-level split comes first, and the lock distinguishes the sealed group. The counts sum to 171.
- **(g) Fix.** No shipping blocker. If revising the title near `(80, 70)`, use “Split participants before building the harnesses.” The sealed-test box already states that the final candidate is scored once per loop.

### 8. `two-tier-design` — **Redraw**

- **(a–c) Collisions and connectors.** No overlaps or arrow crossings. The dashed outlines correctly isolate cells 1 and 8. The two arrows labeled “correlate” near `x≈1700–1850` point into “Sealed-test gain,” which makes the predictors look like inputs to the gain calculation. The validation loops are described inside the outcome box, so the diagram gives the observed outcome no explicit path of its own.
- **(d–e) Readability and copy.** The dots survive at 850 px, but cell numbers, legend notes, and Tier 2 details are around 10 px. Keep the eight-cell matrix, four factor names, 96 configurations, both predictors, and observed gain. Move the cell 1 and 8 naming and control details, seed counts, and exact evaluation budgets to the caption.
- **(f) Five-second read.** Tier 1 mostly works. The matrix matches the stated \(I=MOPT\) half fraction, but “structured” and “degraded” are less precise than the two levels of each factor. Tier 2 fails the glance test because its arrows suggest a procedure different from the planned comparison.
- **(g) Fix.** Preserve the matrix at `x≈486–1518, y≈300–708` and use a compact two-level legend. Redraw everything below `y≈756` so “96 configurations” fans out to three parallel boxes: “Profile forecast,” “HGM clade estimate,” and “Observed sealed-test gain from validation loops.” Bring those three outputs into a distinct comparison box labeled “Correlate each predictor with observed gain.”
