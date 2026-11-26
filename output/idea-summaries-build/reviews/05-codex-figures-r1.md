Figures 6 and 8 need redraws. Figure 6 compares a current score with two predictions without making the difference clear. Figure 8 leaves the experimental units and the matched-cost comparison ambiguous. Figures 1–5 and 7 need targeted fixes.

Coordinates below are approximate PNG pixels measured from the top left. Text sizes are visual estimates at 850 px display width.

## 1. `same-outputs-different-futures.png`

- **(a) Text.** The boxes and plot labels have clear separation.
- **(b) Lines.** The input arrows converge cleanly. The gap bracket at approximately x=2255, y=359–627 stops short of both curves, so it looks detached from the comparison it measures.
- **(c) Direction and endpoints.** The arrow leaving “Same outputs” points toward the middle of the chart’s left edge, well above the common origin. It reads as entering the plot at an unexplained improvement level.
- **(d) Readability.** The title and curve labels survive reduction. The axis labels and two-line gap annotation land around 10–11 px.
- **(e) Caption.** Move the 400-line detail and the inventory of structural changes to the caption. Explain there that the curves are hypothetical and what a point at a given budget represents. A continuous held-out curve otherwise invites the inference that the sealed set is scored throughout a loop.
- **(f) Five-second read.** Yes. Two harnesses start with identical scores and could improve at different rates. “Gap from structure alone” reads as an established causal result even though the curves illustrate the hypothesis.
- **(g) Fix.** Remove the arrow from the center box into the plot and label the origin “Same starting scores.” At the right edge, mark one shared budget and align the bracket ends to the two curve values at that x-coordinate. Label it “Hypothesized gap.”

**Verdict — fix.**

## 2. `pipeline-two-forms.png`

- **(a) Text.** Text clears the box edges. The two “Task score” boxes carry different subtitles, which weakens the intended output match.
- **(b) Lines.** Horizontal arrows stay in the gaps. Dashed trace arrows clear all text and have distinct entry points into the trace strip.
- **(c) Direction and endpoints.** The floating green checks are positioned over stages, but readers have to infer where they run and whether a failure blocks scoring. The upper path starts with `kp` already in hand, while the lower path starts by loading keypoints. The comparison boundary is unclear.
- **(d) Readability.** The green badges, config identifiers, and trace inventory are around 9–11 px. The threshold loop is legible when inspected closely and too dense for a quick scan.
- **(e) Caption.** Move the threshold values, pose model and frame rate, and full trace inventory to the caption. Keep the configured cutoff and threshold, warning-only checks, and optimizer access visible.
- **(f) Five-second read.** Partly. The monolith versus staged pipeline is immediate. Identical StaBLE Y-Balance scores and the fact that the optimizer reads the trace take more work.
- **(g) Fix.** Name StaBLE Y-Balance in the title. Give both paths the same input label and either mark their right-hand outputs “Identical task scores” or join them to a common score endpoint. Anchor each check to its stage and label it “Warning only.” Rename the strip at y≈912 “Per-stage trace the optimizer reads.”

**Verdict — fix.**

## 3. `bpt-equivalence-gate.png`

- **(a) Text.** The labels fit. The gate’s four-line body makes the two acceptance criteria hard to scan separately.
- **(b) Lines.** The branches to Pass and Fail are clean. The arrows at x≈516 and x≈1256 stop just outside the dashed outline, making that group look loosely connected to the flow.
- **(c) Direction and endpoints.** Pass and Fail are unambiguous. The five stacked cards could represent five sequential rewrites or five factors used to generate variants.
- **(d) Readability.** The M/O/P/T/N initials survive reduction. Their descriptions and the gate details land near 10 px.
- **(e) Caption.** Move the naming levels and padding implementation to the caption. Keep matched token counts and the two differential-test criteria in the figure.
- **(f) Five-second read.** Yes for the admission rule. The title’s “prove” promises more than differential tests on cached and fuzzed inputs can establish.
- **(g) Fix.** Use “Check each rewrite against the seed before admission.” Label the dashed block “Generate variants across five factors” and connect its boundary to the incoming and outgoing arrows. Rename “Pad length” to “Match token counts.” Give the gate two short lines for matching outputs and matching task-facing tool calls. Specify in the caption how the comparison treats the traces and warnings introduced by the rewrite.

**Verdict — fix.**

## 4. `single-edit-profile.png`

- **(a) Text.** The cards, grid, legend, and profile have clear separation.
- **(b) Lines.** The arrows clear the squares and text. Their alignment with the middle row visually singles out that session.
- **(c) Direction and endpoints.** The left-to-right flow is clear. The diagram leaves room to infer that edits accumulate within a session or that the profile summarizes only the middle row.
- **(d) Readability.** The three square styles remain distinguishable at about 19 px. The legend and metric descriptions are around 10–11 px.
- **(e) Caption.** Move “Base b, cell c” and the metric definitions to the caption. Define the success-rate denominator, what qualifies as a regression, and how an edit counts as accepted.
- **(f) Five-second read.** Yes for “edits become a profile.” The important design detail that every edit starts from the same parent is easy to miss.
- **(g) Fix.** Put “All 30 edits start from the same parent” in the proposer card or above the grid. Label the three rows as sessions and add a bracket spanning them before the arrow to Profile at x≈1890. Use “Valid, no reduction in selection error” for the outlined squares so ties and worsening edits fit the same label.

**Verdict — fix.**

## 5. `refactor-first-break-even.png`

- **(a) Text.** The labels fit. At display size, `b_R` and `B*` are close and readers have to decode both while following the front of the curves.
- **(b) Lines.** The blue curve overlays the horizontal axis from x≈260 to 503, so the upfront cost can look like axis highlighting. The crossing at x≈623 and its dashed guide are easy to locate.
- **(c) Direction and endpoints.** The plain axes give a clear left-to-right budget progression. The marker identifies break-even, while the end of the initial blue segment lacks a plain-language label.
- **(d) Readability.** The curves and dot hold up. The axis descriptors are around 10–11 px, and the literal underscore in `b_R` looks like raw notation.
- **(e) Caption.** Put the accept-if-better rule and the denominator for “fraction of error gap closed” in the caption. Identify the assumptions that produce the illustrated crossover.
- **(f) Five-second read.** Yes. Refactoring starts behind and eventually overtakes search in this sketch. The headline makes that outcome sound guaranteed.
- **(g) Fix.** Use “Refactoring can pay off after a break-even budget.” Mark the interval from x≈260 to 503 below the axis as “Upfront refactor cost.” Mark the dot “Break-even \(B^*\)” and label the curves at their right ends to free up the legend area.

**Verdict — fix.**

## 6. `parent-selection-at-birth.png`

- **(a) Text.** Labels clear the tree and plots. “No descendants evaluated yet” sits beneath the tree as a whole, so its scope is unclear.
- **(b) Lines.** Tree edges and the blue arrow clear the text. The link from the newborn to the structural-prior card gives that rule an exclusive visual connection to the node.
- **(c) Direction and endpoints.** The blue arrow has a clear destination. The ambiguity is whether DGM and HGM also evaluate the newborn. The three right-hand graphics share a column heading even though the first shows current dev score and the other two show distributions over clade success.
- **(d) Readability.** The main labels survive. The scale endpoints and axis descriptions are around 10 px, which makes the change in quantity easy to miss.
- **(e) Caption.** Move the extra branch labels and rule acronyms to the caption unless they are needed elsewhere. Explain what “clade success” measures and the basis for the illustrative prior’s location and spread.
- **(f) Five-second read.** Partly. The blue styling signals the favored rule. The reader has to work out that DGM supplies current performance, HGM supplies a flat prior at birth in this setup, and code features supply a more specific prediction of future success. The title overstates the information gap.
- **(g) Fix.** Put “New archive node with no evaluated descendants” above all three rules. Label the DGM row “Current dev score.” Place HGM and the structural prior side by side on a common 0–1 clade-success scale with density identified. Use a title such as “Code features give a newborn harness a prior on future edit success.”

**Verdict — redraw.**

## 7. `participant-splits.png`

- **(a) Text.** The labels fit, including the lock icon and both right-hand callouts.
- **(b) Lines.** The three-way split is clean. The right-hand arrows point inward and resemble inputs to the split cards.
- **(c) Direction and endpoints.** The normalization arrow around x≈1748–1832, y≈314 reverses the natural reading of provenance. The dev group supplies the bounds. The sealed-test arrow likewise makes an access restriction look like a data flow.
- **(d) Readability.** All four participant counts are prominent. The callout pills and card descriptions are smaller but readable at 850 px.
- **(e) Caption.** Move “2,968 single-camera task examples” and the pilot provenance to the caption. Keep the split counts, dev-only normalization, and end-of-loop test timing visible.
- **(f) Five-second read.** Yes for the 85/43/43 person split. The reader has to reconcile the direction of the bounds arrow and look to the headline for the once-per-loop rule.
- **(g) Fix.** Put “Fit normalization bounds on these participants only” inside the dev card around y≈224–404. Put “Score the final candidate once per loop” and “Hidden from proposer and search” inside the sealed card around y≈704–884. Remove both incoming annotation arrows.

**Verdict — fix.**

## 8. `two-tier-design.png`

- **(a) Text.** Both panels have clear spacing. The isolated “+ naming, placebo arms” pill has no clear attachment to a design unit.
- **(b) Lines.** The arrows clear the text. The divider also breaks the visual link between Tier 1’s measured profile and Tier 2’s use of that profile as a predictor.
- **(c) Direction and endpoints.** The right-hand chain makes the two predictors look like treatments that each launch ten loops. The intended reading is ten loops per configuration, with both predictors judged at matched cost against the resulting test gain. “30 edits each” also leaves the denominator unclear.
- **(d) Readability.** The filled and hollow markers work at 850 px. The cell labels, legend, and loop-budget line sit around 10 px. The M/O/P/T initials are legible but depend on another figure for their meaning.
- **(e) Caption.** Keep the resolution IV half fraction and \(I=MOPT\) in the figure. Put the factor definitions, aliasing details, naming and placebo allocations, and the unit used to match predictor cost in the caption. Define what is sampled in the 32 combinations per base. Four binary factors alone give 16 distinct settings.
- **(f) Five-second read.** Partly. The two tiers are obvious. The reader has to reconstruct the fractional factorial, the edit allocation, and how the predictors are compared.
- **(g) Fix.** Label the left grid “Eight-cell resolution IV half fraction” with \(I=MOPT\) beneath it. Attach “30 one-step edits” to its explicit unit, spelling out the base × cell × proposer crossing if each combination receives 30. On the right, show **96 configurations × 10 loops per configuration = 960 loops**, with “2 optimizers × 5 seeds” beside the loop count. Route the matched-cost profile and clade predictions into a comparison with the gain measured on sealed participants.

**Verdict — redraw.**
tokens used
55,460
Figures 6 and 8 need redraws. Figure 6 compares a current score with two predictions without making the difference clear. Figure 8 leaves the experimental units and the matched-cost comparison ambiguous. Figures 1–5 and 7 need targeted fixes.

Coordinates below are approximate PNG pixels measured from the top left. Text sizes are visual estimates at 850 px display width.

## 1. `same-outputs-different-futures.png`

- **(a) Text.** The boxes and plot labels have clear separation.
- **(b) Lines.** The input arrows converge cleanly. The gap bracket at approximately x=2255, y=359–627 stops short of both curves, so it looks detached from the comparison it measures.
- **(c) Direction and endpoints.** The arrow leaving “Same outputs” points toward the middle of the chart’s left edge, well above the common origin. It reads as entering the plot at an unexplained improvement level.
- **(d) Readability.** The title and curve labels survive reduction. The axis labels and two-line gap annotation land around 10–11 px.
- **(e) Caption.** Move the 400-line detail and the inventory of structural changes to the caption. Explain there that the curves are hypothetical and what a point at a given budget represents. A continuous held-out curve otherwise invites the inference that the sealed set is scored throughout a loop.
- **(f) Five-second read.** Yes. Two harnesses start with identical scores and could improve at different rates. “Gap from structure alone” reads as an established causal result even though the curves illustrate the hypothesis.
- **(g) Fix.** Remove the arrow from the center box into the plot and label the origin “Same starting scores.” At the right edge, mark one shared budget and align the bracket ends to the two curve values at that x-coordinate. Label it “Hypothesized gap.”

**Verdict — fix.**

## 2. `pipeline-two-forms.png`

- **(a) Text.** Text clears the box edges. The two “Task score” boxes carry different subtitles, which weakens the intended output match.
- **(b) Lines.** Horizontal arrows stay in the gaps. Dashed trace arrows clear all text and have distinct entry points into the trace strip.
- **(c) Direction and endpoints.** The floating green checks are positioned over stages, but readers have to infer where they run and whether a failure blocks scoring. The upper path starts with `kp` already in hand, while the lower path starts by loading keypoints. The comparison boundary is unclear.
- **(d) Readability.** The green badges, config identifiers, and trace inventory are around 9–11 px. The threshold loop is legible when inspected closely and too dense for a quick scan.
- **(e) Caption.** Move the threshold values, pose model and frame rate, and full trace inventory to the caption. Keep the configured cutoff and threshold, warning-only checks, and optimizer access visible.
- **(f) Five-second read.** Partly. The monolith versus staged pipeline is immediate. Identical StaBLE Y-Balance scores and the fact that the optimizer reads the trace take more work.
- **(g) Fix.** Name StaBLE Y-Balance in the title. Give both paths the same input label and either mark their right-hand outputs “Identical task scores” or join them to a common score endpoint. Anchor each check to its stage and label it “Warning only.” Rename the strip at y≈912 “Per-stage trace the optimizer reads.”

**Verdict — fix.**

## 3. `bpt-equivalence-gate.png`

- **(a) Text.** The labels fit. The gate’s four-line body makes the two acceptance criteria hard to scan separately.
- **(b) Lines.** The branches to Pass and Fail are clean. The arrows at x≈516 and x≈1256 stop just outside the dashed outline, making that group look loosely connected to the flow.
- **(c) Direction and endpoints.** Pass and Fail are unambiguous. The five stacked cards could represent five sequential rewrites or five factors used to generate variants.
- **(d) Readability.** The M/O/P/T/N initials survive reduction. Their descriptions and the gate details land near 10 px.
- **(e) Caption.** Move the naming levels and padding implementation to the caption. Keep matched token counts and the two differential-test criteria in the figure.
- **(f) Five-second read.** Yes for the admission rule. The title’s “prove” promises more than differential tests on cached and fuzzed inputs can establish.
- **(g) Fix.** Use “Check each rewrite against the seed before admission.” Label the dashed block “Generate variants across five factors” and connect its boundary to the incoming and outgoing arrows. Rename “Pad length” to “Match token counts.” Give the gate two short lines for matching outputs and matching task-facing tool calls. Specify in the caption how the comparison treats the traces and warnings introduced by the rewrite.

**Verdict — fix.**

## 4. `single-edit-profile.png`

- **(a) Text.** The cards, grid, legend, and profile have clear separation.
- **(b) Lines.** The arrows clear the squares and text. Their alignment with the middle row visually singles out that session.
- **(c) Direction and endpoints.** The left-to-right flow is clear. The diagram leaves room to infer that edits accumulate within a session or that the profile summarizes only the middle row.
- **(d) Readability.** The three square styles remain distinguishable at about 19 px. The legend and metric descriptions are around 10–11 px.
- **(e) Caption.** Move “Base b, cell c” and the metric definitions to the caption. Define the success-rate denominator, what qualifies as a regression, and how an edit counts as accepted.
- **(f) Five-second read.** Yes for “edits become a profile.” The important design detail that every edit starts from the same parent is easy to miss.
- **(g) Fix.** Put “All 30 edits start from the same parent” in the proposer card or above the grid. Label the three rows as sessions and add a bracket spanning them before the arrow to Profile at x≈1890. Use “Valid, no reduction in selection error” for the outlined squares so ties and worsening edits fit the same label.

**Verdict — fix.**

## 5. `refactor-first-break-even.png`

- **(a) Text.** The labels fit. At display size, `b_R` and `B*` are close and readers have to decode both while following the front of the curves.
- **(b) Lines.** The blue curve overlays the horizontal axis from x≈260 to 503, so the upfront cost can look like axis highlighting. The crossing at x≈623 and its dashed guide are easy to locate.
- **(c) Direction and endpoints.** The plain axes give a clear left-to-right budget progression. The marker identifies break-even, while the end of the initial blue segment lacks a plain-language label.
- **(d) Readability.** The curves and dot hold up. The axis descriptors are around 10–11 px, and the literal underscore in `b_R` looks like raw notation.
- **(e) Caption.** Put the accept-if-better rule and the denominator for “fraction of error gap closed” in the caption. Identify the assumptions that produce the illustrated crossover.
- **(f) Five-second read.** Yes. Refactoring starts behind and eventually overtakes search in this sketch. The headline makes that outcome sound guaranteed.
- **(g) Fix.** Use “Refactoring can pay off after a break-even budget.” Mark the interval from x≈260 to 503 below the axis as “Upfront refactor cost.” Mark the dot “Break-even \(B^*\)” and label the curves at their right ends to free up the legend area.

**Verdict — fix.**

## 6. `parent-selection-at-birth.png`

- **(a) Text.** Labels clear the tree and plots. “No descendants evaluated yet” sits beneath the tree as a whole, so its scope is unclear.
- **(b) Lines.** Tree edges and the blue arrow clear the text. The link from the newborn to the structural-prior card gives that rule an exclusive visual connection to the node.
- **(c) Direction and endpoints.** The blue arrow has a clear destination. The ambiguity is whether DGM and HGM also evaluate the newborn. The three right-hand graphics share a column heading even though the first shows current dev score and the other two show distributions over clade success.
- **(d) Readability.** The main labels survive. The scale endpoints and axis descriptions are around 10 px, which makes the change in quantity easy to miss.
- **(e) Caption.** Move the extra branch labels and rule acronyms to the caption unless they are needed elsewhere. Explain what “clade success” measures and the basis for the illustrative prior’s location and spread.
- **(f) Five-second read.** Partly. The blue styling signals the favored rule. The reader has to work out that DGM supplies current performance, HGM supplies a flat prior at birth in this setup, and code features supply a more specific prediction of future success. The title overstates the information gap.
- **(g) Fix.** Put “New archive node with no evaluated descendants” above all three rules. Label the DGM row “Current dev score.” Place HGM and the structural prior side by side on a common 0–1 clade-success scale with density identified. Use a title such as “Code features give a newborn harness a prior on future edit success.”

**Verdict — redraw.**

## 7. `participant-splits.png`

- **(a) Text.** The labels fit, including the lock icon and both right-hand callouts.
- **(b) Lines.** The three-way split is clean. The right-hand arrows point inward and resemble inputs to the split cards.
- **(c) Direction and endpoints.** The normalization arrow around x≈1748–1832, y≈314 reverses the natural reading of provenance. The dev group supplies the bounds. The sealed-test arrow likewise makes an access restriction look like a data flow.
- **(d) Readability.** All four participant counts are prominent. The callout pills and card descriptions are smaller but readable at 850 px.
- **(e) Caption.** Move “2,968 single-camera task examples” and the pilot provenance to the caption. Keep the split counts, dev-only normalization, and end-of-loop test timing visible.
- **(f) Five-second read.** Yes for the 85/43/43 person split. The reader has to reconcile the direction of the bounds arrow and look to the headline for the once-per-loop rule.
- **(g) Fix.** Put “Fit normalization bounds on these participants only” inside the dev card around y≈224–404. Put “Score the final candidate once per loop” and “Hidden from proposer and search” inside the sealed card around y≈704–884. Remove both incoming annotation arrows.

**Verdict — fix.**

## 8. `two-tier-design.png`

- **(a) Text.** Both panels have clear spacing. The isolated “+ naming, placebo arms” pill has no clear attachment to a design unit.
- **(b) Lines.** The arrows clear the text. The divider also breaks the visual link between Tier 1’s measured profile and Tier 2’s use of that profile as a predictor.
- **(c) Direction and endpoints.** The right-hand chain makes the two predictors look like treatments that each launch ten loops. The intended reading is ten loops per configuration, with both predictors judged at matched cost against the resulting test gain. “30 edits each” also leaves the denominator unclear.
- **(d) Readability.** The filled and hollow markers work at 850 px. The cell labels, legend, and loop-budget line sit around 10 px. The M/O/P/T initials are legible but depend on another figure for their meaning.
- **(e) Caption.** Keep the resolution IV half fraction and \(I=MOPT\) in the figure. Put the factor definitions, aliasing details, naming and placebo allocations, and the unit used to match predictor cost in the caption. Define what is sampled in the 32 combinations per base. Four binary factors alone give 16 distinct settings.
- **(f) Five-second read.** Partly. The two tiers are obvious. The reader has to reconstruct the fractional factorial, the edit allocation, and how the predictors are compared.
- **(g) Fix.** Label the left grid “Eight-cell resolution IV half fraction” with \(I=MOPT\) beneath it. Attach “30 one-step edits” to its explicit unit, spelling out the base × cell × proposer crossing if each combination receives 30. On the right, show **96 configurations × 10 loops per configuration = 960 loops**, with “2 optimizers × 5 seeds” beside the loop count. Route the matched-cost profile and clade predictions into a comparison with the gain measured on sealed participants.

**Verdict — redraw.**
