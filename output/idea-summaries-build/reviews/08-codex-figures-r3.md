**Round 3 verdict for Proposal 08:** Ship figures 1–3. Fix figures 4–6. The main issues are small effect subscripts in figure 4, misleading reuse of blue in figure 5, and a prediction in figure 6 that takes too much cross-panel decoding.

Coordinates are approximate `(x, y)` positions in the supplied 2,600 px-wide PNGs, measured from the upper left. Text sizes are estimates at 850 px display width.

### 1. `one-video-two-referrals.png` — Ship

- **(a) Text collisions.** None. Both referral headers fit, and the two choices in each card have room.
- **(b) Line crossings.** None. The two diagonal arrows clear the video label and the referral text.
- **(c) Arrow direction and endpoints.** Clear. The gray arrows branch from the same clip, and each colored arrow leads to its own hold time.
- **(d) Small text.** The stance label and illustrative tag are roughly 11 px. Both remain readable, although the italic tag is the easiest text to miss.
- **(e) Caption material.** Keep the stopping rules and filter cutoffs in the figure. The caption can explain why each choice might be defensible.
- **(f) Five-second read.** Yes. One clip goes through two analyses and yields two hold times. The example’s illustrative status takes a closer look.
- **(g) Concrete fix.** Optional. At `(160, 220)`, shorten the tag to **Illustrative** and use upright type so it reads more readily at display size.

### 2. `referral-counted-twice.png` — Ship

- **(a) Text collisions.** None. The narrow posterior card wraps its text, but all lines fit.
- **(b) Line crossings.** None. “Count 2” and “referral-shaped M” both clear their diagonals. The two inputs to the combiner land at distinct heights.
- **(c) Arrow direction and endpoints.** Clear. The orange branches show the referral going into both the prior and the measurement. The measurement then enters the combiner through its own arrow.
- **(d) Small text.** Body text is roughly 11 px. “Fitted on blind reports” is legible, though easy to skip because it sits below the equation.
- **(e) Caption material.** Keep the blind fit in the figure. It explains why the second route matters. The caption can carry the definitions of `H` and `M`.
- **(f) Five-second read.** Yes for the double count and the risk of overconfidence. Connecting the blind-fitted ratio to the referral-shaped measurement takes a second pass.
- **(g) Concrete fix.** Optional. In the combiner at `(1572, 440)`, change “fitted on blind reports” to **Ratio fitted on blind reports** so the qualifier has an explicit subject.

### 3. `calibration-bug-or-information-bug.png` — Ship

- **(a) Text collisions.** None. The red annotation fits between the dashed guides without touching either.
- **(b) Line crossings.** The two guides intentionally meet the circled points on the plateau. Data lines clear their labels.
- **(c) Arrow direction and endpoints.** No arrows. The main ambiguity is the orange-to-red transition at `(2012, 565)`. A quick scan can briefly register the red plateau as a separate series.
- **(d) Small text.** Main labels are roughly 11 px. The `₀` in `M₀` is smaller, but the axis wording carries the meaning.
- **(e) Caption material.** The right footer repeats the marked example. The circled points and “different M₀, same report” already show the many-to-one mapping.
- **(f) Five-second read.** Yes. The left panel preserves differences through a shift. The right panel collapses them at the plateau.
- **(g) Concrete fix.** Optional. Continue the orange curve through the plateau from `(2012, 565)` to `(2430, 565)` and use red for the circles, guides and annotation. Set the left footer at `(468, 975)` in neutral text so blue keeps its meaning elsewhere.

### 4. `path-splicing-factorial.png` — Fix

- **(a) Text collisions.** None. Row labels clear the matrix, and both cards have padding.
- **(b) Line crossings.** None. The dotted leader to the example card stays horizontal and is visually distinct from the effect arrows.
- **(c) Arrow direction and endpoints.** Clear. Rightward arrows change the report referral with the path held fixed. Downward arrows change the path referral with the report referral held fixed.
- **(d) Small text.** The `a` and `b` subscripts are roughly 7–8 px at display size. They carry the distinction between the effects, so this is a legibility problem.
- **(e) Caption material.** Keep the worked `μ(a,b)` example and the diagonal checks. The example can lose “transcript Z frozen” while still explaining what gets replayed.
- **(f) Five-second read.** Yes for the two factors and the direction of the effects. The example and interaction take longer, and the small subscripts slow the comparison.
- **(g) Concrete fix.** Enlarge the subscripts beside all four arrows and in the interaction card. At `(1912, 783)`, use the space saved by minus signs to set **DEᵦ − DEₐ = IEᵦ − IEₐ** on one line with full legibility. Shorten the example at `(1912, 288)` to **Replay the path from referral a. Give the reporting step referral b.**

### 5. `self-improvement-design.png` — Fix

- **(a) Text collisions.** None. The audit headline does leave “runs” alone on a third line, breaking up the central claim.
- **(b) Line crossings.** None. The matrix bracket and the arrow from the sealed test group enter different sides of the audit card.
- **(c) Arrow direction and endpoints.** Clear. The bracket covers all nine matrix cells, and both arrows terminate at the audit card.
- **(d) Small text.** Secondary labels are roughly 10–11 px. “One dot per seed” is readable but sits closer to the reward headers than the dots it explains.
- **(e) Caption material.** “One dot per seed” duplicates the five-seed headline and the visible groups of five. “Six checkpoints per run” can move to the caption. Keep “positive control” in the approval-judge card.
- **(f) Five-second read.** Yes for 45 runs and a sealed audit. The matching blue fills visually pair the development group with arm (c), even though development covers all three arms and arm (c) still receives a referral.
- **(g) Concrete fix.** Set the development banner at `(80, 100)` and the randomized-referral card at `(1400, 392)` in neutral tones. Remove the dot key at `(80, 476)` and set the audit headline at `(2032, 738)` as **Audit every checkpoint / from all 45 runs**.

### 6. `predicted-routes-by-optimizer.png` — Fix

- **(a) Text collisions.** None. The band label clears the curves, and the endpoint labels fit outside the plots.
- **(b) Line crossings.** The traces share the origin in each panel as intended. On the right, GRPO’s dashed curve stays close enough to the dotted zero line that the two are hard to distinguish early on. Neither crosses a label.
- **(c) Arrow direction and endpoints.** No arrows. The orange endpoints have clear labels. Each blue trace says “reward (c)” without saying it represents all optimizers.
- **(d) Small text.** Ticks and the normalization note are roughly 10–11 px. The `B` in `γ_B` is roughly 7 px. The dashed centerline also has no direct label.
- **(e) Caption material.** Move the full normalization sentence to the caption and use **Normalized effect** as a shared axis label. Keep the hypothetical, preregistered status in the figure.
- **(f) Five-second read.** Partial. The right panel immediately shows a much larger indirect effect for GEPA/ACE. Seeing that both optimizer groups reach the band and that only GEPA/ACE put most of their total effect through the path requires comparing endpoints across panels. The headline currently spends that reading time on the color key.
- **(g) Concrete fix.** Use the headline area at `(80, 60)` for **Under reward (a), both groups reach the target band. Only GEPA/ACE are predicted to put most of the effect through the path.** Keep **Hypothetical preregistered predictions** as a short status line. Mark the two total-effect endpoints at `x ≈ 1020`, and label both zero traces **Reward (c), all optimizers**. Use a neutral dotted line because reward (c) randomizes the referral.
tokens used
48,692
**Round 3 verdict for Proposal 08:** Ship figures 1–3. Fix figures 4–6. The main issues are small effect subscripts in figure 4, misleading reuse of blue in figure 5, and a prediction in figure 6 that takes too much cross-panel decoding.

Coordinates are approximate `(x, y)` positions in the supplied 2,600 px-wide PNGs, measured from the upper left. Text sizes are estimates at 850 px display width.

### 1. `one-video-two-referrals.png` — Ship

- **(a) Text collisions.** None. Both referral headers fit, and the two choices in each card have room.
- **(b) Line crossings.** None. The two diagonal arrows clear the video label and the referral text.
- **(c) Arrow direction and endpoints.** Clear. The gray arrows branch from the same clip, and each colored arrow leads to its own hold time.
- **(d) Small text.** The stance label and illustrative tag are roughly 11 px. Both remain readable, although the italic tag is the easiest text to miss.
- **(e) Caption material.** Keep the stopping rules and filter cutoffs in the figure. The caption can explain why each choice might be defensible.
- **(f) Five-second read.** Yes. One clip goes through two analyses and yields two hold times. The example’s illustrative status takes a closer look.
- **(g) Concrete fix.** Optional. At `(160, 220)`, shorten the tag to **Illustrative** and use upright type so it reads more readily at display size.

### 2. `referral-counted-twice.png` — Ship

- **(a) Text collisions.** None. The narrow posterior card wraps its text, but all lines fit.
- **(b) Line crossings.** None. “Count 2” and “referral-shaped M” both clear their diagonals. The two inputs to the combiner land at distinct heights.
- **(c) Arrow direction and endpoints.** Clear. The orange branches show the referral going into both the prior and the measurement. The measurement then enters the combiner through its own arrow.
- **(d) Small text.** Body text is roughly 11 px. “Fitted on blind reports” is legible, though easy to skip because it sits below the equation.
- **(e) Caption material.** Keep the blind fit in the figure. It explains why the second route matters. The caption can carry the definitions of `H` and `M`.
- **(f) Five-second read.** Yes for the double count and the risk of overconfidence. Connecting the blind-fitted ratio to the referral-shaped measurement takes a second pass.
- **(g) Concrete fix.** Optional. In the combiner at `(1572, 440)`, change “fitted on blind reports” to **Ratio fitted on blind reports** so the qualifier has an explicit subject.

### 3. `calibration-bug-or-information-bug.png` — Ship

- **(a) Text collisions.** None. The red annotation fits between the dashed guides without touching either.
- **(b) Line crossings.** The two guides intentionally meet the circled points on the plateau. Data lines clear their labels.
- **(c) Arrow direction and endpoints.** No arrows. The main ambiguity is the orange-to-red transition at `(2012, 565)`. A quick scan can briefly register the red plateau as a separate series.
- **(d) Small text.** Main labels are roughly 11 px. The `₀` in `M₀` is smaller, but the axis wording carries the meaning.
- **(e) Caption material.** The right footer repeats the marked example. The circled points and “different M₀, same report” already show the many-to-one mapping.
- **(f) Five-second read.** Yes. The left panel preserves differences through a shift. The right panel collapses them at the plateau.
- **(g) Concrete fix.** Optional. Continue the orange curve through the plateau from `(2012, 565)` to `(2430, 565)` and use red for the circles, guides and annotation. Set the left footer at `(468, 975)` in neutral text so blue keeps its meaning elsewhere.

### 4. `path-splicing-factorial.png` — Fix

- **(a) Text collisions.** None. Row labels clear the matrix, and both cards have padding.
- **(b) Line crossings.** None. The dotted leader to the example card stays horizontal and is visually distinct from the effect arrows.
- **(c) Arrow direction and endpoints.** Clear. Rightward arrows change the report referral with the path held fixed. Downward arrows change the path referral with the report referral held fixed.
- **(d) Small text.** The `a` and `b` subscripts are roughly 7–8 px at display size. They carry the distinction between the effects, so this is a legibility problem.
- **(e) Caption material.** Keep the worked `μ(a,b)` example and the diagonal checks. The example can lose “transcript Z frozen” while still explaining what gets replayed.
- **(f) Five-second read.** Yes for the two factors and the direction of the effects. The example and interaction take longer, and the small subscripts slow the comparison.
- **(g) Concrete fix.** Enlarge the subscripts beside all four arrows and in the interaction card. At `(1912, 783)`, use the space saved by minus signs to set **DEᵦ − DEₐ = IEᵦ − IEₐ** on one line with full legibility. Shorten the example at `(1912, 288)` to **Replay the path from referral a. Give the reporting step referral b.**

### 5. `self-improvement-design.png` — Fix

- **(a) Text collisions.** None. The audit headline does leave “runs” alone on a third line, breaking up the central claim.
- **(b) Line crossings.** None. The matrix bracket and the arrow from the sealed test group enter different sides of the audit card.
- **(c) Arrow direction and endpoints.** Clear. The bracket covers all nine matrix cells, and both arrows terminate at the audit card.
- **(d) Small text.** Secondary labels are roughly 10–11 px. “One dot per seed” is readable but sits closer to the reward headers than the dots it explains.
- **(e) Caption material.** “One dot per seed” duplicates the five-seed headline and the visible groups of five. “Six checkpoints per run” can move to the caption. Keep “positive control” in the approval-judge card.
- **(f) Five-second read.** Yes for 45 runs and a sealed audit. The matching blue fills visually pair the development group with arm (c), even though development covers all three arms and arm (c) still receives a referral.
- **(g) Concrete fix.** Set the development banner at `(80, 100)` and the randomized-referral card at `(1400, 392)` in neutral tones. Remove the dot key at `(80, 476)` and set the audit headline at `(2032, 738)` as **Audit every checkpoint / from all 45 runs**.

### 6. `predicted-routes-by-optimizer.png` — Fix

- **(a) Text collisions.** None. The band label clears the curves, and the endpoint labels fit outside the plots.
- **(b) Line crossings.** The traces share the origin in each panel as intended. On the right, GRPO’s dashed curve stays close enough to the dotted zero line that the two are hard to distinguish early on. Neither crosses a label.
- **(c) Arrow direction and endpoints.** No arrows. The orange endpoints have clear labels. Each blue trace says “reward (c)” without saying it represents all optimizers.
- **(d) Small text.** Ticks and the normalization note are roughly 10–11 px. The `B` in `γ_B` is roughly 7 px. The dashed centerline also has no direct label.
- **(e) Caption material.** Move the full normalization sentence to the caption and use **Normalized effect** as a shared axis label. Keep the hypothetical, preregistered status in the figure.
- **(f) Five-second read.** Partial. The right panel immediately shows a much larger indirect effect for GEPA/ACE. Seeing that both optimizer groups reach the band and that only GEPA/ACE put most of their total effect through the path requires comparing endpoints across panels. The headline currently spends that reading time on the color key.
- **(g) Concrete fix.** Use the headline area at `(80, 60)` for **Under reward (a), both groups reach the target band. Only GEPA/ACE are predicted to put most of the effect through the path.** Keep **Hypothetical preregistered predictions** as a short status line. Mark the two total-effect endpoints at `x ≈ 1020`, and label both zero traces **Reward (c), all optimizers**. Use a neutral dotted line because reward (c) randomizes the referral.
