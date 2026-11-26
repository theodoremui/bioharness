I’d fix figures **1, 2, 4, and 6** and ship **3, 5, and 7**. The four fixes address what readers may infer about the data, the oracle, the scoring loop, or the reported percentages. All four can keep their current layouts.

Type sizes are approximate at 850 px wide. Coordinates refer to the supplied PNGs, measured from the upper-left corner.

### 1. `one-output-four-encodings.png` — Fix

- **(a) Text collisions.** None. **(b) Line crossings.** None. **(c) Arrow endpoints.** All four arrows clearly point right, but they leave the same panel edge at x≈680. The diagram makes the formats look like four encodings of the same payload, even though printed numbers use keypoints and the other three use the CoM path.
- **(d) Readability.** The sample rows and `1 cm` label are roughly 10 px at display size. The scale label matters because it demonstrates what the stabilogram preserves. **(e) Caption material.** The three sample rows and the remainder count spend four lines demonstrating a point already made by “61,200 numbers.”
- **(f) Five-second read.** Yes for “one trial, four ways to show it.” The source of each encoding and its trade-off take longer.
- **(g) Fix.** Label the connector at y≈345 **“Keypoints”** and give the three lower connectors a shared **“CoM path”** branch. Change the stabilogram badge from “sway area visible” to **“Spatial scale kept, timing lost”** so it states a trade-off alongside the other rows. Keep two example rows and enlarge the `1 cm` label.

### 2. `risk-decomposition.png` — Fix

- **(a) Text collisions.** None. **(b) Line crossings.** The perceptual bracket clears the labels and spans both intended segments. **(c) Endpoints.** The ticks align cleanly. The ambiguity is at x≈1200, where “(oracle estimate)” makes \(R(e)\) look like the fitted oracle’s measured risk. Figure 3 depends on the fitted oracle and the true floor being distinct.
- **(d) Readability.** The subscripts in the perceptual term and the two right-hand risk labels shrink to roughly 7–8 px. The composition \(h\circ\pi\) is the hardest to parse. **(e) Caption material.** Move the oracle-estimation detail to the caption. Keep “widths are schematic” on the figure.
- **(f) Five-second read.** Yes for four components and the bracket grouping resolution with calibration. The decoder sequence requires a closer read.
- **(g) Fix.** Label \(R(e)\) **“best possible render decoder”** and explain in the caption that the trained oracle estimates its risk. Enlarge the subscripts at x≈1820 and x≈2300 and in the bracket heading. Shorten the subtitle to **“Risk increases from left to right. Widths are schematic.”** This also avoids implying that the zero tick represents a decoder.

### 3. `oracle-learning-curve.png` — Ship

- **(a) Text collisions.** None. **(b) Line crossings.** The orange curve crosses the blue reader baseline once, making the sign change visible. The vertical guides stop at their intended series and clear the text. **(c) Endpoints.** Both guides are clear. The subtraction rule in the subtitle establishes the sign.
- **(d) Readability.** The ticks and annotations are roughly 11 px and remain readable. **(e) Caption material.** The sidebar parenthetical “reader minus true floor” could move to the caption if space is needed. Keep the subtraction rule and the true-gap value on the figure.
- **(f) Five-second read.** Yes. The red −0.049 at 200 renders stands out, and 0.0079 at 5,000 is easy to compare with the true gap of 0.0087.
- **(g) Optional polish.** In the sidebar at x≈1800, use **“True gap 0.0087 cm²”** as a single line if trimming. Keep the true-floor legend immediately above it.

### 4. `renderer-evolution-loop.png` — Fix

- **(a) Text collisions.** The return connector separates “parent” from “code” at x≈800, y≈1104. The line runs between the words, so the label reads as two fragments. **(b) Line crossings.** The other connectors clear the text and one another. **(c) Endpoints.** The arrows from Reader A go straight to “Error tables” and “Fitness,” which makes it look as if Reader A computes its own errors. The saved-renderers arrow stops at the group border directly above the center card, so a quick scan can associate it with held-out readers alone.
- **(d) Readability.** Box copy is roughly 11–12 px. The difficulty is tracing the feedback paths while reading the split labels. **(e) Caption material.** “No labels” appears in both the cache and renderer boxes. Keep the renderer restriction and use the recovered space to clarify scoring.
- **(f) Five-second read.** The render-to-reader path lands. The distinction between dev-train feedback and dev-select fitness, which matters for interpreting the search, takes longer.
- **(g) Fix.** Label the outgoing branches **“dev-train predictions”** and **“dev-select predictions.”** State in each destination box that scoring uses the corresponding split’s labels. Put **“parent code”** on one line above the archive-to-mutator arrow. End the saved-renderers arrow at a shared **“Post-search scoring”** header spanning all three cards.

### 5. `reader-design-matrix.png` — Ship

- **(a) Text collisions.** None, including the longest condition name. **(b) Line crossings.** The family rules and dashed row divider clear the labels and markers. **(c) Endpoints.** No arrows. The diamond is visually distinct, though its meaning requires the legend.
- **(d) Readability.** Headers and legend text are about 10–11 px. The symbols are larger and distinguishable by shape as well as color. **(e) Caption material.** Nothing needs to move. The diamond explanation earns its place because it describes a unique cell.
- **(f) Five-second read.** Yes for which models drive fitness and which columns are broadly held out. The same-family distinction and the prior crowd profile take a legend lookup.
- **(g) Optional polish.** At the last legend item, x≈1760, use **“Prior crowd profile enters fitness via predictor.”** This makes the indirect role explicit in one read.

### 6. `transfer-decomposition-curve.png` — Fix

- **(a) Text collisions.** None. The left callout fits between panels. **(b) Line crossings.** The shared origin is intentional. The red brackets clear the curves. **(c) Endpoints.** Both brackets attach to the blue and solid green endpoints. They show the absolute gap on the plotted scale, while “55% unshared” and “11% unshared” report a fraction of Reader A’s gain. The denominator is missing from the figure.
- **(d) Readability.** The percentages are readable. The smaller “gain over default plot” label appears inside the left panel and can look specific to that panel. **(e) Caption material.** Move the H2/H3 identifiers to the caption. Keep the illustrative status prominent.
- **(f) Five-second read.** Yes for a visibly smaller gap under ensemble fitness. A reader cannot tell from the percentages alone what is being divided by what or that the callouts refer specifically to held-out VLMs.
- **(g) Fix.** Keep the large percentages and add a shared line above the panels reading **“Share of Reader A’s gain unshared by held-out VLMs.”** Move “gain over default plot” to a shared axis label. Use **“Predicted transfer to held-out VLMs improves with ensemble fitness”** as the headline so it reads as a hypothesis at a glance.

### 7. `co-adaptation-drift.png` — Ship

- **(a) Text collisions.** None. **(b) Line crossings.** The round-zero markers sit on the y-axis as expected and clear the tick labels. The brackets clear the endpoints. **(c) Endpoints.** Both brackets clearly measure the round-four accuracy gap.
- **(d) Readability.** The axis labels and legend remain readable at roughly 11 px. Marker shape reinforces the color distinction. **(e) Caption material.** “At round 4” is redundant in both callouts because each bracket sits at the last tick. Keep the illustrative status on the figure.
- **(f) Five-second read.** Yes. Fresh readers decline under standard fitness and improve with the frozen-reader term, with the gap shrinking from 0.42 to 0.12. The lower blue endpoint in the right panel also makes the trade-off visible.
- **(g) Optional polish.** At the brackets near x≈1104 and x≈2344, use **“42 pp gap”** and **“12 pp gap.”** Give “accuracy on sealed test participants” shared placement if there’s room so it clearly applies to both panels.
tokens used
56,428
I’d fix figures **1, 2, 4, and 6** and ship **3, 5, and 7**. The four fixes address what readers may infer about the data, the oracle, the scoring loop, or the reported percentages. All four can keep their current layouts.

Type sizes are approximate at 850 px wide. Coordinates refer to the supplied PNGs, measured from the upper-left corner.

### 1. `one-output-four-encodings.png` — Fix

- **(a) Text collisions.** None. **(b) Line crossings.** None. **(c) Arrow endpoints.** All four arrows clearly point right, but they leave the same panel edge at x≈680. The diagram makes the formats look like four encodings of the same payload, even though printed numbers use keypoints and the other three use the CoM path.
- **(d) Readability.** The sample rows and `1 cm` label are roughly 10 px at display size. The scale label matters because it demonstrates what the stabilogram preserves. **(e) Caption material.** The three sample rows and the remainder count spend four lines demonstrating a point already made by “61,200 numbers.”
- **(f) Five-second read.** Yes for “one trial, four ways to show it.” The source of each encoding and its trade-off take longer.
- **(g) Fix.** Label the connector at y≈345 **“Keypoints”** and give the three lower connectors a shared **“CoM path”** branch. Change the stabilogram badge from “sway area visible” to **“Spatial scale kept, timing lost”** so it states a trade-off alongside the other rows. Keep two example rows and enlarge the `1 cm` label.

### 2. `risk-decomposition.png` — Fix

- **(a) Text collisions.** None. **(b) Line crossings.** The perceptual bracket clears the labels and spans both intended segments. **(c) Endpoints.** The ticks align cleanly. The ambiguity is at x≈1200, where “(oracle estimate)” makes \(R(e)\) look like the fitted oracle’s measured risk. Figure 3 depends on the fitted oracle and the true floor being distinct.
- **(d) Readability.** The subscripts in the perceptual term and the two right-hand risk labels shrink to roughly 7–8 px. The composition \(h\circ\pi\) is the hardest to parse. **(e) Caption material.** Move the oracle-estimation detail to the caption. Keep “widths are schematic” on the figure.
- **(f) Five-second read.** Yes for four components and the bracket grouping resolution with calibration. The decoder sequence requires a closer read.
- **(g) Fix.** Label \(R(e)\) **“best possible render decoder”** and explain in the caption that the trained oracle estimates its risk. Enlarge the subscripts at x≈1820 and x≈2300 and in the bracket heading. Shorten the subtitle to **“Risk increases from left to right. Widths are schematic.”** This also avoids implying that the zero tick represents a decoder.

### 3. `oracle-learning-curve.png` — Ship

- **(a) Text collisions.** None. **(b) Line crossings.** The orange curve crosses the blue reader baseline once, making the sign change visible. The vertical guides stop at their intended series and clear the text. **(c) Endpoints.** Both guides are clear. The subtraction rule in the subtitle establishes the sign.
- **(d) Readability.** The ticks and annotations are roughly 11 px and remain readable. **(e) Caption material.** The sidebar parenthetical “reader minus true floor” could move to the caption if space is needed. Keep the subtraction rule and the true-gap value on the figure.
- **(f) Five-second read.** Yes. The red −0.049 at 200 renders stands out, and 0.0079 at 5,000 is easy to compare with the true gap of 0.0087.
- **(g) Optional polish.** In the sidebar at x≈1800, use **“True gap 0.0087 cm²”** as a single line if trimming. Keep the true-floor legend immediately above it.

### 4. `renderer-evolution-loop.png` — Fix

- **(a) Text collisions.** The return connector separates “parent” from “code” at x≈800, y≈1104. The line runs between the words, so the label reads as two fragments. **(b) Line crossings.** The other connectors clear the text and one another. **(c) Endpoints.** The arrows from Reader A go straight to “Error tables” and “Fitness,” which makes it look as if Reader A computes its own errors. The saved-renderers arrow stops at the group border directly above the center card, so a quick scan can associate it with held-out readers alone.
- **(d) Readability.** Box copy is roughly 11–12 px. The difficulty is tracing the feedback paths while reading the split labels. **(e) Caption material.** “No labels” appears in both the cache and renderer boxes. Keep the renderer restriction and use the recovered space to clarify scoring.
- **(f) Five-second read.** The render-to-reader path lands. The distinction between dev-train feedback and dev-select fitness, which matters for interpreting the search, takes longer.
- **(g) Fix.** Label the outgoing branches **“dev-train predictions”** and **“dev-select predictions.”** State in each destination box that scoring uses the corresponding split’s labels. Put **“parent code”** on one line above the archive-to-mutator arrow. End the saved-renderers arrow at a shared **“Post-search scoring”** header spanning all three cards.

### 5. `reader-design-matrix.png` — Ship

- **(a) Text collisions.** None, including the longest condition name. **(b) Line crossings.** The family rules and dashed row divider clear the labels and markers. **(c) Endpoints.** No arrows. The diamond is visually distinct, though its meaning requires the legend.
- **(d) Readability.** Headers and legend text are about 10–11 px. The symbols are larger and distinguishable by shape as well as color. **(e) Caption material.** Nothing needs to move. The diamond explanation earns its place because it describes a unique cell.
- **(f) Five-second read.** Yes for which models drive fitness and which columns are broadly held out. The same-family distinction and the prior crowd profile take a legend lookup.
- **(g) Optional polish.** At the last legend item, x≈1760, use **“Prior crowd profile enters fitness via predictor.”** This makes the indirect role explicit in one read.

### 6. `transfer-decomposition-curve.png` — Fix

- **(a) Text collisions.** None. The left callout fits between panels. **(b) Line crossings.** The shared origin is intentional. The red brackets clear the curves. **(c) Endpoints.** Both brackets attach to the blue and solid green endpoints. They show the absolute gap on the plotted scale, while “55% unshared” and “11% unshared” report a fraction of Reader A’s gain. The denominator is missing from the figure.
- **(d) Readability.** The percentages are readable. The smaller “gain over default plot” label appears inside the left panel and can look specific to that panel. **(e) Caption material.** Move the H2/H3 identifiers to the caption. Keep the illustrative status prominent.
- **(f) Five-second read.** Yes for a visibly smaller gap under ensemble fitness. A reader cannot tell from the percentages alone what is being divided by what or that the callouts refer specifically to held-out VLMs.
- **(g) Fix.** Keep the large percentages and add a shared line above the panels reading **“Share of Reader A’s gain unshared by held-out VLMs.”** Move “gain over default plot” to a shared axis label. Use **“Predicted transfer to held-out VLMs improves with ensemble fitness”** as the headline so it reads as a hypothesis at a glance.

### 7. `co-adaptation-drift.png` — Ship

- **(a) Text collisions.** None. **(b) Line crossings.** The round-zero markers sit on the y-axis as expected and clear the tick labels. The brackets clear the endpoints. **(c) Endpoints.** Both brackets clearly measure the round-four accuracy gap.
- **(d) Readability.** The axis labels and legend remain readable at roughly 11 px. Marker shape reinforces the color distinction. **(e) Caption material.** “At round 4” is redundant in both callouts because each bracket sits at the last tick. Keep the illustrative status on the figure.
- **(f) Five-second read.** Yes. Fresh readers decline under standard fitness and improve with the frozen-reader term, with the gap shrinking from 0.42 to 0.12. The lower blue endpoint in the right panel also makes the trade-off visible.
- **(g) Optional polish.** At the brackets near x≈1104 and x≈2344, use **“42 pp gap”** and **“12 pp gap.”** Give “accuracy on sealed test participants” shared placement if there’s room so it clearly applies to both panels.
