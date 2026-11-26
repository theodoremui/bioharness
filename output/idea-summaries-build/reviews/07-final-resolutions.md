# Proposal 07: resolutions of the final review and the round-2 and round-4 Codex reviews

Sources: `07-final-review.md` (independent final review: 5 main changes, 64 numbered edits, weaknesses W1 to W10, notes on eight figures), `07-codex-adversarial-r2.md` (second adversarial pass on the text and SVGs, verdict "needs-attention", 4 high and 3 medium findings) and `07-codex-figures-r4.md` (visual review of all eight PNGs after this pass's figure changes).

An interrupted run had applied most of the final review's edits to `docs/idea-summaries/07-learning-how-to-look-at-tool-outputs.md` and `figs_07.py` without recording them. This run checked every item against the current text, applied what was missing, fixed the round-2 adversarial findings, redrew Figure 5 and Figure 1, reran the visual review on all eight figures, and trimmed the prose back to 5,898 audit words (it rose to 6,187 after the round-2 fixes). Line numbers refer to the final proposal.

Reuse decisions. `07-codex-adversarial-r2.md` (9 KB) was newer than the proposal and the SVGs it reviewed, so it was reused and not rerun. The earlier `07-codex-figures-r4.md` (15:14) was older than the PNGs re-rendered at 15:31, so it no longer described the shipped figures; it is preserved as `07-codex-figures-r4-prefix.md` and the round-4 visual review was rerun on the current PNGs, overwriting `07-codex-figures-r4.md`.

Totals: final review 82 entries (64 numbered edits, 10 weaknesses, 8 figure notes), 81 applied and 1 declined in part; Codex adversarial round 2: 7 findings (4 high), all fixed, with one sub-recommendation of a high finding declined for compute; Codex figures round 4: 23 findings over eight figures, 15 fixed and 8 declined with reasons.

## 1. Final review: five main changes

| Change | Status | Where |
|---|---|---|
| 1. Four-part split of a gain, equation $G_A=\Delta I+\overline{\Delta P}+(\Delta P_A-\overline{\Delta P})$ and identity $S_A=(\Delta P_A-\overline{\Delta P})/G_A$ | Applied (earlier run), verified | L23 four sources; Key ideas table L37 to L42; equations L136 to L140; box ML contribution names computation inside shared perception |
| 2. Retitle; research question, why open, decisive experiment and falsifier in plain words | Applied, verified; this run added the profile-free comparator to the falsifier | Title L1; box L3; L23 |
| 3. Participant groups, normalized error and reader-set names before Method | Applied, verified | Key ideas L50 to L61 (table of dev-train, dev-select, calibration, sealed test; normalized error and skill; held-out, never-fitness and fresh readers) |
| 4. One symbol per object | Applied, verified by grep (no $e$, $\pi$, D1 to D5, "legibility term", "pair-specific", "private visual code", "saved renderer" remain); this run renamed "legibility variant" to "frozen-reader variant" | $r$, $r_{\text{def}}$, $r_{\text{stab}}$; Q1 to Q5; $X$, $A$, $B$; "frozen-reader term" ($\mu$) and "predicted-human term" ($\nu\hat P_{\text{crowd}}$, L212); "checkpoint" |
| 5. One-line hypotheses with explicit decision rules; Method roadmap | Applied, verified; this run named the decisive conjunct of H5 and added the profile-free conjunct to H1 | Hypothesis table L94 to L100; roadmap L104 |

## 2. Final review: numbered edits 1 to 64

| Items | Status | Note |
|---|---|---|
| 1 to 4 (title, box) | Applied | Box is 167 words; falsifier now also names the profile-free forecast |
| 5, 6 (OpenCap, monocular agent, keypoints, CoM printed row, 95% ellipse, Qwen3-VL token cost) | Applied | L13, L15, Figure 1 caption |
| 7 (split pilot sentence, normalization caveat) | Applied; the split itself was finished in this run | L21 |
| 8 (problem paragraph) | Applied | L23 |
| 9 (split the coding-agent sentence) | Applied in this run | L25 |
| 10 to 17 (Key ideas definitions, channel, Bayes risk, gain table, transfer example, participants, fitness, mutator, archive) | Applied | "Information-matched" dropped; the Gemma and InternVL token-count claim was removed with the visual-token paragraph, and the Figure 1 caption states the Qwen3-VL assumption; archive is defined where first used in Method |
| 18 to 22 (related work) | Applied | By My Eyes "picks the best of its renders"; "average chart accuracy" for Dubey et al.; gap sentence without the triad. This run merged the By My Eyes and AutoV/MatPlotAgent rows to save length |
| 23 to 27 (H1 to H5) | Applied | Decision rules in the table; H1 rule is point estimate at least 0.5, permutation $p<0.05$, paired-bootstrap lower bounds above 0 |
| 28 to 43 (Method) | Applied | Roadmap; identity wording; split paragraphs; k-nearest-neighbour oracle and quadratic recalibration stated; $m_{rk}$, $c_d$ and the resolution curve $\sigma^2=a+b\,m^{-2}$ defined; percent scale for the proportional score (this run later cut that sentence for length, so the mis-scaling cannot recur); declared-channel MAP-Elites descriptor; checkpoints every fifth generation; GRPO sentence split in this run; fresh readers reported by family; E7 deleted |
| 44 to 57 (Experiments) | Applied | Participant table; held-out tasks drawn at random and registered; BioCV only after search; Q4 and the lowest-10% flag defined; verl defined; predicted-human term given a formula and weight; LLMTime serialization defined; Pareto front in E1; E5 as a 2 by 3 table; winner's-curse rationale corrected; long sentences split |
| 58 (outcome table) | Applied | H2 and H3 falsified rows; Schaeffer et al. in the H3 row; negative-gap diagnostic moved to Method; this run also added an H4 row conditioned on the computation contrast and a "no E5 contrast positive" row (Codex r2 medium) |
| 59 (compute) | Applied | Fitness decisions Q1 and Q5; OpenCap 7 min per 30-second trial from the 3.8 min per 17-second pilot; FP8 for the 480B mutator; E7 hours removed |
| 60 (risks) | Applied | Merged bullets |
| 61 (Where to learn more) | Applied | Time-series item dropped; one clause per item. This run also dropped the UvA adversarial-attacks item for length |
| 62, 63 (references [9], [34]) | Applied | Ma D, Chen S, Yang Y, et al.; full Hu and Tang title |
| 64 (global notation pass) | Applied | See Change 4 |

## 3. Final review: weaknesses W1 to W10

| W | Decision | What changed |
|---|---|---|
| W1 few readers, ambiguous rule | Applied, with one part declined | Rule stated (table L96); power computed with readers as the unit (L273 to L277); the reader set is 13 VLMs in six families, 12 held out for a Qwen3-VL-8B run. **Declined in part:** raising the count to 15 to 20 readers up front. Each added family needs its own battery run and per-processor oracle floors, so readers are added only if the registered power simulation gives under 80% power at 0.6 (L277) |
| W2 weak comparators | Applied | Comparators specified (L156); comparator (1) fitted in leave-one-reader-out folds on raw gains; the reference comparator keeps variance within a checkpoint; the profile-free forecast now varies within a checkpoint because floors are never pooled (Codex r2) |
| W3 computation mislabelled | Applied | Change 1 |
| W4 predictor underspecified | Applied | Curve form, $m_{rk}$, $c_d$, declared-channel descriptor; this run made the knockout weights defined for redundant and uninformative marks (Codex r2) |
| W5 battery error mis-scaled | Applied, then sentence cut | Percent scale was applied; the sentence was later removed for length because no result depends on it |
| W6 normalized error undefined | Applied | L50; AUC kept out of fitness |
| W7 H3 target set and baseline | Applied | Never-fitness readers named in Figure 5 and used in H3 and Figure 6; H3 measured against the stabilogram; Schaeffer et al. in the outcome table |
| W8 fresh set mixes families; predicted-human term undefined | Applied | $D_t$ by family (L190); term formula and weight (L212) |
| W9 BioCV role | Applied | BioCV enters only after the search (L198); Figure 4's held-out tasks card is consistent with that |
| W10 scope | Applied | E7 dropped; E6 marked secondary in the box, hypotheses and experiments |

## 4. Final review: figure notes

| Figure | Decision | What changed |
|---|---|---|
| 1 one-output-four-encodings | Applied | Printed row shows the CoM path (1,800 frames by 2); cm² fixed; caption states Qwen3-VL token assumption; this run labelled the two traces x and y |
| 2 risk-decomposition | Applied | Canvas cropped to 372 units tall; prose orders resolution before calibration |
| 3 oracle-learning-curve | Applied | Caption names the toy 20-pixel bar plot and the k-nearest-neighbour oracle |
| 4 renderer-evolution-loop | Applied | Probe named in the reader A box and error tables; "child code" label; BioCV consistent with text; two-reader clause moved to the Selection text |
| 5 reader-design-matrix | Applied | "clinicians"; never-fitness columns shaded. This run changed the same-family partner from Qwen3-VL-2B to Qwen3-VL-4B (Codex r2 high 4), which moves 2B into the never-fitness set |
| 6 transfer-decomposition-curve | Applied | Title starts "Hypothesized"; right panel names Gemma 3 12B; never-fitness VLMs plotted; axis is gain over the stabilogram in normalized error, 0 to 0.5 |
| 7 profile-predicts-transfer | Applied | Checkpoint-centered gains on both axes, Spearman about 0.6 pooled with within-family values, family-and-size panel jittered |
| 8 co-adaptation-drift | Applied | Skill defined as 1 minus normalized error with a predict-the-mean zero line |

## 5. Codex adversarial round 2 (07-codex-adversarial-r2.md)

| Finding | Decision | What changed |
|---|---|---|
| [high] H1 can pass on processor differences alone: the forecast adds reader-specific $\Delta I_B$, which centering does not remove | Fixed | H1 now also requires the full forecast to beat the profile-free forecast $\Delta I_B(r)$ on the same signed cells, with a paired-bootstrap lower bound above 0 (box falsifier, L23, H1 line, table L96, comparator (2) at L156). A forecast constant within every checkpoint scores 0 (L271) |
| [high] Knockout weights undefined for redundant marks (zero denominator, negative differences) | Fixed | Importance is the clipped knockout rise plus the clipped keep-only-this-mark fall from a blank render, so duplicated marks still count; if all importances are zero the decision-field marks share the weight equally, so every checkpoint has a forecast; the rule is tested on synthetic single-mark, redundant and uninformative renders before evolution (L150) |
| [high] Oracle agreement cannot establish information equivalence or bound the gain | Fixed | Floors are always per processor family and never pooled (L122); the convolutional-probe agreement check was removed; a difference of two oracle risks is reported as an empirical contrast, not a bound; H1 is rerun with each $\Delta I_B$ shifted by the oracle error measured on synthetic encodings (L130) |
| [high] H3 confounds partner capacity with family (Qwen 2B against InternVL ≈8B and Gemma 12B) | Fixed, one sub-recommendation declined | The same-family partner is whichever of Qwen3-VL-4B and 30B-A3B has dev-select error on the default plot and stabilogram closer to the cross-family partners' mean, fixed before search; H3 is claimed only for the named pairs, with partner skill as a covariate and absolute held-out gains beside the ratios (L212; H3 line L88 and table; Figure 5 redrawn). **Declined:** crossing several source readers with matched same- and cross-family partners. Each condition costs about 135 H100-hours (5 seeds of 27 hours), so a 3-source grid adds at least 540 hours; Codex's own fallback (named pairs, absolute gains) is adopted |
| [medium] Leave-one-reader-out comparator can see the excluded reader through centering; reader-history comparator needs its own split | Fixed | Comparator (1) is fitted on raw gains in leave-one-reader-out folds and centered only after prediction; centering of gains and forecasts happens after any fitting (L156, L271); the reference comparator uses the reader's gains on checkpoints of other runs that hold it out |
| [medium] E5's H4 contrast changes modality along with encoding; any H4 failure read as computation | Fixed | H4 is M1 against M2 (marks against the same values printed in one image); M3 (native text) is reported apart (L255, H4 line and table L99); the outcome table attributes a gain to computation only when M cells beat N cells, and a separate row covers no positive E5 contrast (L295, L296) |
| [medium] Oracle budget does not cover the fit grid | Fixed | Recounted: 504 checkpoints by 5 processor families by 2 decisions (5,040), about 20 knockout and keep-one fits for each of 320 E3 checkpoints (6,400), and Q2 to Q4 for 63 final checkpoints (945), about 12,400 fits at 0.05 h, 620 H100-hours (L311); total 5,430 (L316). Knockout weights are per renderer, so they are fit once at native resolution and only for the E3 checkpoints that H1 uses; L277 now says each reader contributes cells from up to 320 E3 checkpoints |

Round-1 high findings, rechecked by round 2: Codex confirmed the signed-gain endpoint, forecast timing, separate crowd panel, task exclusions across development use, co-adaptation controls and cohort disclosure as fixed. Its remaining round-1 concerns (oracle equivalence and computation controls) are the round-2 findings fixed above.

## 6. Codex figures round 4 (07-codex-figures-r4.md)

Run on all eight PNGs after this pass's figure changes (Figure 1 trace labels, Figure 5 partner change), which also covers the four figures whose round-3 fixes had not been re-reviewed (1, 2, 4, 6). Verdicts: Figure 1 fix, 2 fix, 3 fix, 4 redraw, 5 redraw, 6 fix, 7 fix, 8 ship. After the fixes below, every SVG was regenerated with `figs_07.py`, rendered, linted (no overlap, off-canvas or line-through-text warnings; two coverage notes only) and each PNG was reopened and inspected. Two defects found on inspection were also fixed: the Figure 4 tool-output card text overflowed its narrowed box (box widened), and Figure 7's "within-family" had its hyphen converted to a minus sign (fixed in code).

| Figure | Finding | Decision | What changed |
|---|---|---|---|
| 1 | `time` label against the inset border; x and y labels crowd the trace ends | Fixed | Bottom gutter reserved; traces stop short of the axis end; labels sit at each trace's midline |
| 1 | Traces distinguished by color only | Fixed | y trace dashed |
| 1 | "loses physical scale" overstated, since ticks keep scale | Fixed | Pill reads "hides physical scale" (drawn size no longer encodes centimetres, as the text at L15 says); first pill reads "keeps all samples" |
| 1 | Move trial setup and token basis to the caption | Declined in part | The subtitle keeps "traces are illustrative", which the style guide requires in the figure; the token basis is already in the caption |
| 2 | Perceptual bracket ends inside the boundaries | Fixed | Bracket snapped to $R(r)$ and $R_X(r)$ |
| 2 | Rename blocks "resolution gap"/"calibration gap"; simplify $R_{h\circ X}$ | Declined | Block names and notation match the equation labels and the terms used throughout the text |
| 3 | The two estimated-gap guides use different colors; true gap has no endpoints | Fixed | Both guides are the same dashed slate; a separate capped reader-to-floor bracket past the last point is labelled "true gap 0.0087 cm²"; second estimate reads "+0.0079 cm²" |
| 3 | y-axis label | Fixed | "mean squared error, cm² (log scale)" |
| 3 | Retitle to the failure only | Declined | The title states the failure and the recovery, as the earlier round-4 review asked |
| 4 | Boundary between search and evaluation blurred; checkpoint arrow can suggest scoring during search | Fixed (redraw) | Dashed "Development search" region encloses renderer, renders, reader A, error tables, fitness, archive and mutator; the checkpoint arrow exits it into a frame titled "After the search ends: score checkpoints" |
| 4 | Cached tool outputs read as a shared header | Fixed | Narrowed card feeding only the renderer program |
| 4 | Pair the dev-train and dev-select labels; move tool and model names to the caption | Declined | Each split label sits on its own branch; the remaining box text is short and names objects the text defines |
| 5 | Full-height gray strips compete with the fitness marks | Fixed (redraw) | Strips replaced by header chips over never-fitness columns; legend "never sets fitness (H3 target)"; caption updated to "Shaded headers mark readers that never set fitness" |
| 5 | Other-family rings too heavy | Fixed | Smaller, thinner rings |
| 5 | Crowd exception in the last row ambiguous | Fixed | Diamond labelled directly "via predictor" |
| 5 | No row grouping | Fixed | "single reader" and "two readers" group labels |
| 5 | Labels small at 850 px | Declined | Labels are 13 to 14.5 px in SVG units, at or above the guide's minimum; 15 columns must fit the width |
| 6 | People series differs from never-fitness VLMs only by dash | Fixed | People drawn in dashed slate |
| 6 | Shorten title and panel labels; move the bracket definition to the caption | Declined | The title must say "Hypothesized" for an illustrative curve; the subtitle keeps the bracket's denominator, which the earlier round asked for; the caption already defines gain |
| 7 | Within-family correlation should be the primary callout | Fixed | "within-family Spearman 0.51" and "−0.07" in bold; pooled values secondary |
| 7 | Jitter note easy to miss | Fixed | "x jittered for visibility" inside the right panel by its axis |
| 7 | Distinguish the pooled other families by marker shape | Declined | Five more shapes in 36 points would crowd the plot; the within-family statistic carries the claim |
| 8 | Optional: one shared skill label | Declined | Verdict was ship; the per-panel label keeps each panel self-contained |

## 7. Final checks

`audit_doc.py`: 5,899 prose words, 8 figures, 35 references; no em-dashes or en-dashes, banned words, missing images, unanchored citations or uncited references. No dashes in the SVGs. Every figure is referred to in the text (Figures 1 to 8 at L15, L35, L124, L104, L212, L236, L242, L257) and every caption starts with *Figure k.* in order. A full reread fixed an ambiguous "It" in the Mutator paragraph, a dangling "StaBLE's", "Figures are H100-hours" (now "GPU costs"), and split three sentences of 50 to 61 words.
