I reviewed the attached PNGs in file order at their intended scale of about 850 px wide. Most labels shrink to roughly 10–12 px. The biggest issues are structural in Figures 4 and 5. Figure 4 blurs the boundary between search and evaluation. Figure 5 makes the primary reader assignments compete with the holdout notation.

### 1. `one-output-four-encodings` — fix

- **(a) Text collisions.** The `time →` label sits against the bottom of the line-plot inset. The `x` and `y` labels crowd the right ends of their traces.
- **(b) Line crossings.** The four connector arrows are clean. Inside the line plot, the traces come close enough that following them by color alone takes effort at 850 px.
- **(c) Arrow direction and endpoints.** The four branches clearly run from one tool output to four encodings. `Time →` is readable as an axis direction once the label is moved away from the inset border.
- **(d) Small text.** The sample rows, subscript-sized frame details, and inset axis labels are the first things to go at display size. The two pill labels in each row carry more information and should remain larger than the samples.
- **(e) Caption text.** Move the 30-second trial, phone frame rate, and token-count assumptions to the caption. Keep a short visible cue that the examples are illustrative.
- **(f) Five-second read.** **Yes.** One CoM path becomes four representations with different costs and tradeoffs. The weak point is the claim about physical scale. The pictured line plot omits units and ticks, but autoscaling by itself preserves physical scale when the axis is labeled.
- **(g) Fix.** In the third inset, reserve a bottom gutter for `Time`, distinguish the traces by stroke style, and change the red pill to `physical scale omitted`. In the first row, use `keeps all samples` if the text representation rounds values as shown. Keep the approximate token counts and document their basis in the caption.

### 2. `risk-decomposition` — fix

- **(a) Text collisions.** No literal overlap. The composition subscript in `Rₕ ∘ ₓ(r)` is dense enough to look like several separate symbols at display size.
- **(b) Line crossings.** None. The blue bracket starts a few pixels inside `R(r)` and ends a few pixels inside `Rₓ(r)`, weakening its alignment with the boundaries it describes.
- **(c) Arrow direction and endpoints.** `risk →` clearly shows increasing risk. The bracket has no directional role, but its endpoints should land exactly on the decoder boundaries.
- **(d) Small text.** The four decoder descriptions are legible individually. Linking each description to its risk symbol takes longer, especially at the right end where the notation is densest.
- **(e) Caption text.** Move the decoder explanation to the caption. Keep `Schematic widths` visible because the unequal widths invite a quantitative reading.
- **(f) Five-second read.** **Partial.** The three-part structure is quick to see. A reader needs longer to understand that “resolution” and “calibration” are *risk increments* between three decoder boundaries.
- **(g) Fix.** Snap the perceptual bracket to the `R(r)` and `Rₓ(r)` dividers. Give the last two ticks short prominent labels, `Recalibrated reader` and `Original reader`, with the precise risk notation below. Use `Resolution gap` and `Calibration gap` inside the blue blocks.

### 3. `oracle-learning-curve` — fix

- **(a) Text collisions.** None. Both annotations clear the curves and markers.
- **(b) Line crossings.** The orange curve crossing the blue reader line is meaningful. The dashed gap at 5,000 renders has a different color from the early gap, which makes two instances of the same comparison look like different measurements.
- **(c) Arrow direction and endpoints.** There are no arrows. The estimated-gap guides visibly connect reader and oracle risk. The true gap is written beside the later guide without its own endpoints, so it can be read as a second value for the same span.
- **(d) Small text.** The ticks are workable at 850 px. The later two-line annotation is dense, and the long title spends space that could go to the two comparisons.
- **(e) Caption text.** Move the full gap definition and the choice of training sizes to the caption. Keep `Preliminary simulation` on the figure.
- **(f) Five-second read.** **Partial.** The oracle improves with more renders. The negative-to-positive reversal and the distinction between the estimated and true gaps take longer to decode.
- **(g) Fix.** Use the title `An undertrained oracle makes the estimated gap negative`. Mark `−0.049 cm²` at 200 renders and `+0.0079 cm²` at 5,000 with the same bracket treatment. Add a separate reader-to-floor bracket beyond the last orange point for `True gap +0.0087 cm²`. Label the y-axis `Mean squared error` if the plotted risks are averages.

### 4. `renderer-evolution-loop` — redraw

- **(a) Text collisions.** No literal collisions. `parent code` is squeezed into the narrow bridge between Archive and Text-only mutator. `dev-train` and `dev-select` sit on different parts of their paths, so they are harder to read as a matched pair.
- **(b) Line crossings.** The arrows avoid literal intersections. The two long return paths and the feedback path from Error tables create competing reading routes. The checkpoint arrow stops at the border of the evaluation panel, with no visible path from the scoring step to its three evaluation inputs.
- **(c) Arrow direction and endpoints.** Individual arrowheads are clear. The *timing* is ambiguous. `Eight checkpoints per run` on a downward arrow out of Archive can suggest scoring during search. The broad Cached tool outputs bar also looks like a shared header even though its only arrow feeds Renderer program.
- **(d) Small text.** The box interiors carry several lines of roughly 10–11 px text. A reader must hunt for the two data splits and follow their arrows to reconstruct what each split controls.
- **(e) Caption text.** Move the tool names, exact model name and probe details, MAP-Elites grid description, checkpoint count, and held-out task names to the caption. Keep the roles of the two development splits and the evaluation timing on the figure.
- **(f) Five-second read.** **No.** The page reads as a workflow with a separate test panel. It takes longer to recover the two feedback routes and understand that checkpoint scoring starts after search finishes.
- **(g) Fix.** Draw a bounded `Development search` region around the renderer, reader, mutator, and archive. Put `Dev-train errors → Mutator` and `Dev-select fitness → Archive` on two short, parallel branches from the reader. Route unlabeled cached outputs directly into Renderer. Use one exit labeled `After search ends` from saved checkpoints to `Score checkpoints`, with sealed participants, held-out readers, and held-out tasks visibly attached to that scoring step.

### 5. `reader-design-matrix` — redraw

- **(a) Text collisions.** No literal overlap. `30B-A3B` nearly fills its column, and the three adjacent headers `Open 4`, `Open 5`, and `Closed` feel crowded at display size.
- **(b) Line crossings.** The dashed horizontal divider runs through the gray column strips. This causes little physical interference, but the gray strips and green rings create a dense field that competes with the blue fitness marks.
- **(c) Arrow direction and endpoints.** No arrows. The ambiguity is in the encodings. Gray means `never sets fitness`, yet the crowd strip stops at the diamond. The reader has to infer whether the crowd counts as a fitness source in that row or whether only its profile informs a predictor.
- **(d) Small text.** This is the weakest figure at 850 px. The model-size labels and row names require deliberate reading. The last row carries a protocol distinction that is easy to miss at that scale.
- **(e) Caption text.** Move the predictor mechanics and the expansion of placeholder model names to the caption. Keep the crowd exception and H3 target designation visible because they affect how the cells are read.
- **(f) Five-second read.** **No.** It is clear that blue marks some special assignments. Identifying a row’s fitness readers, distinguishing the two kinds of holdout, and finding the H3 target columns requires repeated trips to the legend.
- **(g) Fix.** Keep a single compact matrix with filled blue dots for fitness and small gray squares for same-family holdout. Use a light, sparse mark for other-family or human readers. Replace the full-height gray strips with header-level marks for the H3 target VLMs. Keep the diamond in the final crowd cell and label it directly `Profile via predictor`. Add short row-group labels for single-reader and combined fitness conditions.

### 6. `transfer-decomposition-curve` — fix

- **(a) Text collisions.** None. The left `55% unshared` callout takes up much of the gutter between panels, reducing the separation between the two conditions.
- **(b) Line crossings.** No confusing crossings. The two green series are close together early in each panel and are distinguished only by dash style, which becomes less obvious after reduction.
- **(c) Arrow direction and endpoints.** No arrows. The red brackets clearly connect the blue and solid green endpoints. Their geometry represents an absolute gap, while the label is a fraction of reader A’s gain. The denominator is available in the subtitle but easy to miss.
- **(d) Small text.** The long title and subtitle run wide, and the four-part legend takes time to scan. The percentages are readable.
- **(e) Caption text.** Move the full bracket calculation and normalized-error definition to the caption. Keep `Illustrative hypothesis` visible and name whose gain is being measured beside the percentages.
- **(f) Five-second read.** **Yes.** The smaller right-hand wedge conveys more transfer with cross-family fitness. The exact interpretation of 55% versus 11% takes longer.
- **(g) Fix.** Shorten the title to `Cross-family fitness may improve transfer`. Shorten the panel labels to `Reader A only` and `Reader A + Gemma`. Put both endpoint annotations in the same position relative to their plots and label them `55% unshared` and `11% unshared` under a shared cue, `Share of reader A’s gain`. Give the people series a distinct color or marker as well as a dash pattern.

### 7. `profile-predicts-transfer` — fix

- **(a) Text collisions.** None. Several points partly obscure one another, notably near the left panel’s origin and in the right panel’s green cluster.
- **(b) Line crossings.** The zero lines pass behind some markers and read as guides. The more consequential issue is that horizontal jitter in the right panel can look like genuine within-group variation in forecast gain.
- **(c) Arrow direction and endpoints.** No arrows or directional connectors. The small jitter note is the only signal that some displayed x-positions were deliberately shifted.
- **(d) Small text.** The within-family Spearman values are the decisive evidence for the illustrated claim, yet they share a dense line with pooled values. The footer’s jitter note competes with the legend and is easy to skip.
- **(e) Caption text.** Move the point definition and exact jitter procedure to the caption. Keep the plotted unit, `checkpoint-centered gain`, on the axes and identify the numbers as illustrative in the figure.
- **(f) Five-second read.** **Partial.** The left plot shows a clearer overall association. The intended claim is stronger: the profile rule also ranks gains within families, while family and size mostly separate groups. That distinction requires reading the small statistics, and the two marker categories do not show which families are pooled into “other.”
- **(g) Fix.** Make `Within-family ρ = 0.51` and `Within-family ρ = −0.07` the primary panel callouts and move the pooled values to the caption or secondary text. Label the right panel’s jitter beside its x-axis. If the green points represent multiple families, distinguish those families with marker shapes or add a small within-family view.

### 8. `co-adaptation-drift` — ship

- **(a) Text collisions.** None. The gap labels and the zero-baseline note clear the plot marks.
- **(b) Line crossings.** None that confuse the reading. The fresh-reader series meets and crosses zero in the left panel, which is meaningful.
- **(c) Arrow direction and endpoints.** No arrows. Both red brackets clearly connect the round-four values.
- **(d) Small text.** The condition names, endpoint gaps, and series labels hold up at 850 px. The repeated skill definition is the smallest consequential text.
- **(e) Caption text.** The skill formula and sealed-participant detail can move to the caption. Keep the meaning of zero visible because the left panel shows negative skill.
- **(f) Five-second read.** **Yes.** Fresh-reader skill falls under standard fitness and rises with a frozen-reader term. The endpoint gap shrinks from 0.44 to 0.12 in the illustration.
- **(g) Fix.** If a revision is already planned, place `Skill on sealed participants` once above the shared scale and `0 = predicting the dev-train mean` once below both panels. The current placement inside only the right panel makes a shared reference look panel-specific.
tokens used
57,627
I reviewed the attached PNGs in file order at their intended scale of about 850 px wide. Most labels shrink to roughly 10–12 px. The biggest issues are structural in Figures 4 and 5. Figure 4 blurs the boundary between search and evaluation. Figure 5 makes the primary reader assignments compete with the holdout notation.

### 1. `one-output-four-encodings` — fix

- **(a) Text collisions.** The `time →` label sits against the bottom of the line-plot inset. The `x` and `y` labels crowd the right ends of their traces.
- **(b) Line crossings.** The four connector arrows are clean. Inside the line plot, the traces come close enough that following them by color alone takes effort at 850 px.
- **(c) Arrow direction and endpoints.** The four branches clearly run from one tool output to four encodings. `Time →` is readable as an axis direction once the label is moved away from the inset border.
- **(d) Small text.** The sample rows, subscript-sized frame details, and inset axis labels are the first things to go at display size. The two pill labels in each row carry more information and should remain larger than the samples.
- **(e) Caption text.** Move the 30-second trial, phone frame rate, and token-count assumptions to the caption. Keep a short visible cue that the examples are illustrative.
- **(f) Five-second read.** **Yes.** One CoM path becomes four representations with different costs and tradeoffs. The weak point is the claim about physical scale. The pictured line plot omits units and ticks, but autoscaling by itself preserves physical scale when the axis is labeled.
- **(g) Fix.** In the third inset, reserve a bottom gutter for `Time`, distinguish the traces by stroke style, and change the red pill to `physical scale omitted`. In the first row, use `keeps all samples` if the text representation rounds values as shown. Keep the approximate token counts and document their basis in the caption.

### 2. `risk-decomposition` — fix

- **(a) Text collisions.** No literal overlap. The composition subscript in `Rₕ ∘ ₓ(r)` is dense enough to look like several separate symbols at display size.
- **(b) Line crossings.** None. The blue bracket starts a few pixels inside `R(r)` and ends a few pixels inside `Rₓ(r)`, weakening its alignment with the boundaries it describes.
- **(c) Arrow direction and endpoints.** `risk →` clearly shows increasing risk. The bracket has no directional role, but its endpoints should land exactly on the decoder boundaries.
- **(d) Small text.** The four decoder descriptions are legible individually. Linking each description to its risk symbol takes longer, especially at the right end where the notation is densest.
- **(e) Caption text.** Move the decoder explanation to the caption. Keep `Schematic widths` visible because the unequal widths invite a quantitative reading.
- **(f) Five-second read.** **Partial.** The three-part structure is quick to see. A reader needs longer to understand that “resolution” and “calibration” are *risk increments* between three decoder boundaries.
- **(g) Fix.** Snap the perceptual bracket to the `R(r)` and `Rₓ(r)` dividers. Give the last two ticks short prominent labels, `Recalibrated reader` and `Original reader`, with the precise risk notation below. Use `Resolution gap` and `Calibration gap` inside the blue blocks.

### 3. `oracle-learning-curve` — fix

- **(a) Text collisions.** None. Both annotations clear the curves and markers.
- **(b) Line crossings.** The orange curve crossing the blue reader line is meaningful. The dashed gap at 5,000 renders has a different color from the early gap, which makes two instances of the same comparison look like different measurements.
- **(c) Arrow direction and endpoints.** There are no arrows. The estimated-gap guides visibly connect reader and oracle risk. The true gap is written beside the later guide without its own endpoints, so it can be read as a second value for the same span.
- **(d) Small text.** The ticks are workable at 850 px. The later two-line annotation is dense, and the long title spends space that could go to the two comparisons.
- **(e) Caption text.** Move the full gap definition and the choice of training sizes to the caption. Keep `Preliminary simulation` on the figure.
- **(f) Five-second read.** **Partial.** The oracle improves with more renders. The negative-to-positive reversal and the distinction between the estimated and true gaps take longer to decode.
- **(g) Fix.** Use the title `An undertrained oracle makes the estimated gap negative`. Mark `−0.049 cm²` at 200 renders and `+0.0079 cm²` at 5,000 with the same bracket treatment. Add a separate reader-to-floor bracket beyond the last orange point for `True gap +0.0087 cm²`. Label the y-axis `Mean squared error` if the plotted risks are averages.

### 4. `renderer-evolution-loop` — redraw

- **(a) Text collisions.** No literal collisions. `parent code` is squeezed into the narrow bridge between Archive and Text-only mutator. `dev-train` and `dev-select` sit on different parts of their paths, so they are harder to read as a matched pair.
- **(b) Line crossings.** The arrows avoid literal intersections. The two long return paths and the feedback path from Error tables create competing reading routes. The checkpoint arrow stops at the border of the evaluation panel, with no visible path from the scoring step to its three evaluation inputs.
- **(c) Arrow direction and endpoints.** Individual arrowheads are clear. The *timing* is ambiguous. `Eight checkpoints per run` on a downward arrow out of Archive can suggest scoring during search. The broad Cached tool outputs bar also looks like a shared header even though its only arrow feeds Renderer program.
- **(d) Small text.** The box interiors carry several lines of roughly 10–11 px text. A reader must hunt for the two data splits and follow their arrows to reconstruct what each split controls.
- **(e) Caption text.** Move the tool names, exact model name and probe details, MAP-Elites grid description, checkpoint count, and held-out task names to the caption. Keep the roles of the two development splits and the evaluation timing on the figure.
- **(f) Five-second read.** **No.** The page reads as a workflow with a separate test panel. It takes longer to recover the two feedback routes and understand that checkpoint scoring starts after search finishes.
- **(g) Fix.** Draw a bounded `Development search` region around the renderer, reader, mutator, and archive. Put `Dev-train errors → Mutator` and `Dev-select fitness → Archive` on two short, parallel branches from the reader. Route unlabeled cached outputs directly into Renderer. Use one exit labeled `After search ends` from saved checkpoints to `Score checkpoints`, with sealed participants, held-out readers, and held-out tasks visibly attached to that scoring step.

### 5. `reader-design-matrix` — redraw

- **(a) Text collisions.** No literal overlap. `30B-A3B` nearly fills its column, and the three adjacent headers `Open 4`, `Open 5`, and `Closed` feel crowded at display size.
- **(b) Line crossings.** The dashed horizontal divider runs through the gray column strips. This causes little physical interference, but the gray strips and green rings create a dense field that competes with the blue fitness marks.
- **(c) Arrow direction and endpoints.** No arrows. The ambiguity is in the encodings. Gray means `never sets fitness`, yet the crowd strip stops at the diamond. The reader has to infer whether the crowd counts as a fitness source in that row or whether only its profile informs a predictor.
- **(d) Small text.** This is the weakest figure at 850 px. The model-size labels and row names require deliberate reading. The last row carries a protocol distinction that is easy to miss at that scale.
- **(e) Caption text.** Move the predictor mechanics and the expansion of placeholder model names to the caption. Keep the crowd exception and H3 target designation visible because they affect how the cells are read.
- **(f) Five-second read.** **No.** It is clear that blue marks some special assignments. Identifying a row’s fitness readers, distinguishing the two kinds of holdout, and finding the H3 target columns requires repeated trips to the legend.
- **(g) Fix.** Keep a single compact matrix with filled blue dots for fitness and small gray squares for same-family holdout. Use a light, sparse mark for other-family or human readers. Replace the full-height gray strips with header-level marks for the H3 target VLMs. Keep the diamond in the final crowd cell and label it directly `Profile via predictor`. Add short row-group labels for single-reader and combined fitness conditions.

### 6. `transfer-decomposition-curve` — fix

- **(a) Text collisions.** None. The left `55% unshared` callout takes up much of the gutter between panels, reducing the separation between the two conditions.
- **(b) Line crossings.** No confusing crossings. The two green series are close together early in each panel and are distinguished only by dash style, which becomes less obvious after reduction.
- **(c) Arrow direction and endpoints.** No arrows. The red brackets clearly connect the blue and solid green endpoints. Their geometry represents an absolute gap, while the label is a fraction of reader A’s gain. The denominator is available in the subtitle but easy to miss.
- **(d) Small text.** The long title and subtitle run wide, and the four-part legend takes time to scan. The percentages are readable.
- **(e) Caption text.** Move the full bracket calculation and normalized-error definition to the caption. Keep `Illustrative hypothesis` visible and name whose gain is being measured beside the percentages.
- **(f) Five-second read.** **Yes.** The smaller right-hand wedge conveys more transfer with cross-family fitness. The exact interpretation of 55% versus 11% takes longer.
- **(g) Fix.** Shorten the title to `Cross-family fitness may improve transfer`. Shorten the panel labels to `Reader A only` and `Reader A + Gemma`. Put both endpoint annotations in the same position relative to their plots and label them `55% unshared` and `11% unshared` under a shared cue, `Share of reader A’s gain`. Give the people series a distinct color or marker as well as a dash pattern.

### 7. `profile-predicts-transfer` — fix

- **(a) Text collisions.** None. Several points partly obscure one another, notably near the left panel’s origin and in the right panel’s green cluster.
- **(b) Line crossings.** The zero lines pass behind some markers and read as guides. The more consequential issue is that horizontal jitter in the right panel can look like genuine within-group variation in forecast gain.
- **(c) Arrow direction and endpoints.** No arrows or directional connectors. The small jitter note is the only signal that some displayed x-positions were deliberately shifted.
- **(d) Small text.** The within-family Spearman values are the decisive evidence for the illustrated claim, yet they share a dense line with pooled values. The footer’s jitter note competes with the legend and is easy to skip.
- **(e) Caption text.** Move the point definition and exact jitter procedure to the caption. Keep the plotted unit, `checkpoint-centered gain`, on the axes and identify the numbers as illustrative in the figure.
- **(f) Five-second read.** **Partial.** The left plot shows a clearer overall association. The intended claim is stronger: the profile rule also ranks gains within families, while family and size mostly separate groups. That distinction requires reading the small statistics, and the two marker categories do not show which families are pooled into “other.”
- **(g) Fix.** Make `Within-family ρ = 0.51` and `Within-family ρ = −0.07` the primary panel callouts and move the pooled values to the caption or secondary text. Label the right panel’s jitter beside its x-axis. If the green points represent multiple families, distinguish those families with marker shapes or add a small within-family view.

### 8. `co-adaptation-drift` — ship

- **(a) Text collisions.** None. The gap labels and the zero-baseline note clear the plot marks.
- **(b) Line crossings.** None that confuse the reading. The fresh-reader series meets and crosses zero in the left panel, which is meaningful.
- **(c) Arrow direction and endpoints.** No arrows. Both red brackets clearly connect the round-four values.
- **(d) Small text.** The condition names, endpoint gaps, and series labels hold up at 850 px. The repeated skill definition is the smallest consequential text.
- **(e) Caption text.** The skill formula and sealed-participant detail can move to the caption. Keep the meaning of zero visible because the left panel shows negative skill.
- **(f) Five-second read.** **Yes.** Fresh-reader skill falls under standard fitness and rises with a frozen-reader term. The endpoint gap shrinks from 0.44 to 0.12 in the illustration.
- **(g) Fix.** If a revision is already planned, place `Skill on sealed participants` once above the shared scale and `0 = predicting the dev-train mean` once below both panels. The current placement inside only the right panel makes a shared reference look panel-specific.
