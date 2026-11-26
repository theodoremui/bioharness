# Proposal 06: resolutions of the final review and the closing Codex rounds

Doc: `docs/idea-summaries/06-who-self-improvement-leaves-behind.md`. Figures: `docs/idea-summaries/images/06/`, drawn by `output/idea-summaries-build/figs_06.py`.

Sources: `06-final-review.md` (independent review: five priority changes, 92 numbered edits, cut list C1 to C36, weaknesses W1 to W9, questions, citation spot-check, figure review), `06-codex-figures-r4.md` (visual review of the six figures changed in this pass, which include the two round-3 fixes Codex had not seen), `06-codex-adversarial-r2.md` (second adversarial pass).

An earlier run of this revision was interrupted after applying most of the text edits. This pass checked every review item against the text as found, applied what was still missing, made the figure changes, ran both Codex rounds and recorded the decisions below.

## 1. Five priority changes (review section 1)

| item | decision | where it stands |
|---|---|---|
| 1.1 One plain sentence each for question, why open, decisive test, falsifier | applied | Box rewritten (about 163 words, no "correlated-response law", "sealed guard set" or "rejected candidates"); closing question paragraph ends the Problem section; Hypotheses opens with the two decisive tests (H2 in E4's rescoring arm, H1 in E3) and points to the table opening Experiments |
| 1.2 Law in words; define the selection term; state noise invariance once | applied | Key ideas "Correlated-response law" states the law in words; after the $D$ display the selection term is defined as $(C/\sigma_S)\phi(z)=\mathrm{Cov}(b,\mathbf{1}\{S>0\})$, estimated by $\hat D_{\text{sel}}=\hat D-\hat\mu_b\hat P$; "rescales but cannot flip" appears once in the text (H2 and the ablation state predictions, not the property) |
| 1.3 Method roadmap and hypothesis-to-experiment table | applied | Method opens with a two-sentence roadmap plus the A1 to A4 definitions; Experiments opens with the H-to-E table (hypothesis, experiment, domain, failure condition); H1 now names its two primary comparators and E3 marks the other two as secondary |
| 1.4 Overloaded and undefined notation, terminology drift | applied | $m$ for panel size, `dev`/`guard`/`test` in pseudocode, $\Gamma_t$ for cumulative gain, V1/V2 for validity conditions, $L$ for number of tests, $R$ for harm, $\Phi^{-1}$ for quantiles; $\tau$ defined in Notation; Price bars and "transmission term" removed; "$c=0$" replaced; $\bar R$ defined; sign convention stated; one name each for tail, guard log (also in Figure 6, which said "Drift log") and drift per proposal |
| 1.5 Break up dense paragraphs; define A1 to A4 once | applied | Statistical analysis is four paragraphs (sequence and effect size; models; power; guarantee); Estimating drift two; forecast split; E6 split; A1 to A4 defined at the top of Method |

## 2. Numbered edits 1 to 92

All 92 were applied, most by the interrupted run and the rest in this pass. Items applied in a different form than proposed:

| item | form used | reason |
|---|---|---|
| 9 | Lab-pilot sentence kept at the end of the StaBLE paragraph, compressed, before the Global-MMLU example | The review allowed either place; here it introduces shrinkage just before H4 needs it |
| 15, 21 | GEPA weighting clause added to Baselines item 2; CVaR expanded in the table and GroupDRO in Baselines | The Key-ideas entries were merged away in the cut list, so each acronym is expanded at its first use |
| 17 | Edit effects defined in Method's Notation paragraph | Key ideas no longer has an "Edit effect" entry; Notation is where $a$ and $b$ first appear |
| 23 | Tail drift, panel and guard log added to Key ideas; Price's equation in the correlated-response entry; Fisher's geometric model glossed in a clause at its first use in H3 | Length budget; the full model is two paragraphs into Method |
| 35, 59 (W5) | H5(b) now predicts gain kept as the interval from rerunning A4 with E1's moments; the design-rule paragraph says why the closed form only sets the scale of $n_B$ | The first-order mapping (gain kept about the pass probability at $R=0$) ignores how $\sigma_R$ grows along the lineage, which A4 shows matters |
| 43 (W7) | "Transmission term" removed from the Price form and from How to read | For the stated quantity the identity is exact without it |
| 70 (W8) | Tail is "the 13 languages the Global-MMLU paper classes as low-resource [8]" | Verified this pass against the arXiv HTML of 2412.03304, Section 4.1: 13 low-resource languages (Amharic, Hausa, Igbo, Kyrgyz, Malagasy, Nepali, Nyanja, Shona, Sinhala, Somali, Swahili, Telugu, Yoruba), following Joshi et al.; the paper also gives 14K samples per language, so [8] supports the 14,000 figure |
| 85 | Second domain kept as its own short subsection (required by STYLE); the duplicate Risks bullet "Small StaBLE tails" was deleted | The small-tail limit is stated in Data and splits, E3 and Statistical analysis |
| 86 | "Forecast works in Global-MMLU but fails in StaBLE" folded into the forecast row ("if only StaBLE fails, report the tail size needed") | Saves a row with the same action |

Additional text fixes made in this pass, prompted by rereading:
- Hu and Tang: "estimate each generation's winner's inflation" became "model", matching their abstract (a model, calibrated with a pilot prior, gives the winner's-curse size per generation).
- CS329Z Lecture 9 clause said "GEPA and MIPRO, the optimizers instrumented here"; MIPRO is not instrumented, so it now reads "GEPA, the optimizer the L1 loops follow". "Mon Oct 13" dropped from the CS329A entry (STYLE excludes calendars).
- Global-MMLU had no stated margin or smallest effect of interest (0.03 was in StaBLE task-score units). The smallest effect of interest is now three points of error rate, and the margin $M$ five points of tail error rate, sized to the gate pool (see Codex r2, finding 3).
- E6 could not test validity if candidates never approach the margin; the forced-translation edit is now offered to the proposer every generation.
- Compute omitted sealed-test scoring of checkpoints. Added: 0.2 billion tokens in StaBLE and 2.5 billion in Global-MMLU (generation-25 and 50 checkpoints of 210 loops on 4,000 sealed items). With the Codex r2 changes (2.1 billion for breach calls, 0.4 billion for certification) the totals are about 2,030 H100-hours (2,540 with margin) and 121 billion tokens.
- E3's power check rewritten so the direction of the condition is unambiguous.
- "realized error 0.11 to 0.29" became "breach rates of 0.11 to 0.29"; "disattenuated" is defined in a clause.

## 3. Cut list C1 to C36

Applied, with these exceptions: C19 and edits 18 and 65 (StaBLE guard people also certify checkpoints) became moot when Codex r2 finding 4 removed StaBLE certification, so those sentences were deleted; C26 handled as in item 85; C28 dropped the UvA bullet and, in this pass, the "Two Scans per Patient" bullet. The audit count went from 6,187 (review) to 5,937 (interrupted run) to the final figure in section 7.

## 4. Weaknesses W1 to W9 and questions

| item | decision | what changed |
|---|---|---|
| W1 H1 underpowered in StaBLE | applied | Global-MMLU is H1's primary venue and StaBLE a registered secondary (H1, table, Statistical analysis); E3 makes StaBLE's H1 confirmatory only if the generation-0 panel predicts a standard error below the smallest effect of interest, then tries the age-70-and-above tail, otherwise descriptive; moments are fitted hierarchically across seeds with the generation-0 panel as prior |
| W2 primary outcome not the box's claim | applied | Registered fixed sequence: H2 rescoring arm, H1 Global-MMLU, H1 StaBLE, StaBLE drift |
| W3 E4 rescoring arm circular | applied | Moments from a random half of the frozen edits, selection term measured on the other half; agreement metric registered (at least 10 of 12 signs) and, in this pass, the slope of observed on predicted selection terms is reported |
| W4 H2's measured quantity undefined | applied | Selection term defined after the $D$ display and estimated by $\hat D_{\text{sel}}$ |
| W5 H5(b) | applied | See items 35 and 59 |
| W6 timing geometry leading-order | applied | "to leading order in step size" in text, Figure 4 caption and (this pass) the ball label; E5 predicts the sign of $D$; E5 says random steps stand in for LLM proposals |
| W7 transmission term | applied | Removed |
| W8 Global-MMLU tail and conflict premise | applied | Taxonomy named and verified; E4 go/no-go: if the fitting half of the generation-0 panel gives $\hat\rho\ge0$, the tail is narrowed to the languages where forced translation does worst |
| W9 smaller issues | applied | Effect size re-expressed in development people's per-person error spread; fresh-people claim qualified by noise law; rule 9 no longer runs as separate StaBLE loops (the earlier run reused the mean-gate lineages, and Codex r2 then removed StaBLE certification altogether); in this pass the trajectory model is stated to cover the StaBLE primary change with family as a fixed effect, and each family is reported alone |
| Questions 1 to 8 | answered in text where they change the design | Q1 and Q5 by the E3 power check and hierarchical fit; Q2 by E4's split; Q3 by the named 13-language tail; Q4 by reporting loops with fewer than five accepted edits separately; Q6 by the table's "more than 2 of 10 lineages"; Q7 is moot (StaBLE runs no protective arm); Q8 by confirming breaches only when a simultaneous interval on 2,000 sealed tail items clears $M$, with indeterminate cases reported as bounds (Codex r2, finding 2) |

## 5. Review figure section (6) and Codex visual review round 4

Figures changed in this pass: edit-effect-scatter, drift-sign-map, timing-regimes-geometry, instrumented-loop, stable-person-splits, guarantee-validity-and-price. All six (including the two round-3 fixes not seen before) went to `06-codex-figures-r4.md`; after its fixes each was re-rendered, linted (0 warnings apart from the library's arc-approximation note on the loop figure) and inspected as a PNG.

| source | finding | decision | what changed |
|---|---|---|---|
| review, Fig 1 | caption wording; move after the StaBLE paragraph | applied (earlier run) | caption says the orange curve "bottoms out" and "passes its starting value" |
| review, Fig 2 | caption uses $\rho$ early; optional takeaway title | applied | caption says "a correlation of $-0.4$"; title now "The mean rule accepts many edits that harm the tail", parameters moved to a muted line above the legend |
| review, Fig 3 | "20 tail people in 160" invents a cohort; "lowers" ambiguous | applied | guide label "π = 0.125"; caption uses "harms" and "once ρ < −0.143" |
| review, Fig 4 | leading order | applied | ball label ends "(leading order)"; caption says the exact turn comes slightly earlier |
| review, Fig 5 | "ending" left in caption; right axis title | applied | caption names the event per design; axis title "tail people per test"; the accessible description no longer says "ending" |
| review, Fig 6 | $\tau$ undefined; optional "Gate on dev people"; certification role | applied | $\tau$ defined in Notation; box retitled "Gate on dev people"; "Drift log" renamed "Guard log"; caption notes certification in StaBLE; accessible title no longer says "sealed guard people" |
| review, Fig 7 | subtitle said "fall-risk status" | applied | "stratified by fall-risk group and age" |
| review, Fig 8 | optional noise gloss; held-out moments | applied (earlier run) | caption gives the noise in squared majority-spread units and says registered predictions use held-out E1 moments |
| r4, scatter (fix) | vertical zero guide competes with the acceptance line | fix | guide drawn in the lighter rule colour |
| r4, scatter | legend line name | fix | "acceptance line (score S = 0)" |
| r4, scatter | rename wedge label; move ρ to caption | decline | the wedge label is the figure's point and matches the legend; ρ is one short muted line and the caption also gives it |
| r4, sign map (fix) | side note does not say what a curve is | fix | "Each curve is where the selection term is zero. Below a curve, selection harms the tail for that spread ratio." |
| r4, sign map | single ρ* callout duplicates the table; move the "one in eight" gloss to the caption | fix | callout removed; guide reads "π = 0.125"; the caption keeps "one tail person in eight" |
| r4, sign map | rename legend heading and rows | partly | rows read "1 × majority", "2 × majority", "4 × majority"; the heading stays "Tail effect spread" because the longer heading collides with the right-hand column title |
| r4, timing (redraw) | small oblique arrowheads, path 1 reads as leaving the optimum | fix, redraw declined | arrowheads are now large filled triangles at 62% of each path, all pointing to the mean optimum; the layout already pairs numbered seeds with numbered insets and paired diamonds, so a full redraw was not needed |
| r4, timing | unlabelled inset baselines; inverted U dipping below zero may read as necessary | fix | each inset baseline carries "0"; caption says seed 2's gain "peaks before falling, possibly below zero" |
| r4, timing | move "schematic" badge to caption | decline | STYLE asks for the label in the figure as well as the caption |
| r4, loop (fix) | forecast box text close to its border | fix | bottom-row boxes 124 px tall and the compare node re-centred |
| r4, loop | "keep or reject" reads as one decision per generation; no-edit case implicit | fix | "decision for each candidate"; top label "the kept edit, if any, becomes the next parent" |
| r4, loop | when are sealed scores opened | fix | arrow label "saved checkpoints"; sealed-test box "opened after the run: tail change from generation 0 to 50"; caption says the sealed set scores checkpoints only after the run |
| r4, loop | move "prompts, tools, code" and the $S>\tau$ rule to the caption | decline | both are four-word labels that make the boxes self-explanatory, and the text defines $\tau$ |
| r4, splits (ship) | optional "each block is sealed test once" | fix | added to the subtitle |
| r4, guarantee (fix) | log scale unstated; the dot at 1 is unexplained | fix | axis title ends "(log scale)"; the per-step dot carries "1.0 at every size" |
| r4, guarantee | dodged green series look measured at different sizes | fix | dodge removed; both series sit on the true sample sizes, with a large open square around a small filled dot so both stay visible where they meet at n = 10 |
| r4, guarantee | group the three any-parent rows under one event label | decline | round 3 asked for an event line on every row and that is what the figure has; the certification row's "deployed checkpoint only" already stands apart, and the caption states both events |

## 6. Codex adversarial review round 2

`06-codex-adversarial-r2.md` (the working-tree diff exceeded the plugin's limit, so the helper ran the plugin's prompt through `codex exec`, scoped to the proposal and its figures). Verdict: needs-attention. It confirmed that the round-1 findings on drift units, the noise-sign claim, test people certifying checkpoints and the frozen-candidate arm are resolved, and reported six new high-severity findings. All six were fixed.

| finding | decision | what changed |
|---|---|---|
| 1. H2's 0.02 null probability assumes 12 independent sign matches, but cells share edits and items | fix | H2's sign agreement is tested against a permutation null that applies one shuffle of guard tail effects among the held-out edits to all 12 cells, which keeps their dependence; tail and grid choices use only the fitting half; the slope of observed on predicted selection terms is reported; the table's failure condition now reads "sign agreement not above its permutation null, or $n_B$ flips the sign" |
| 2. E6's breach labels are noisy and pooled across gate sizes | fix | A breach is confirmed only when a tested harness's interval against the seed on 2,000 sealed tail items, simultaneous over the run, lies above $M$, and is indeterminate when it contains $M$; breach rates are reported per size as lower and upper bounds; validity is judged against A4 rerun on E1's per-item harms, where true harms are known. The pooled test is kept for rejecting H5(a), and the text says why it is valid: H5(a) must hold at every size, so pooled counts are dominated by a binomial at 5% |
| 3. The Global-MMLU gate has no specified valid test, and binary items make a level-0.001 test unable to pass small batches | fix | Method now specifies an exact one-sided test on paired item outcomes (newly wrong, unchanged, newly right) of distinct questions, one tail language each, at the worst-case share of changed answers. It states the floor (no test at level 0.05/50 passes fewer than about 135 items at a five-point margin) and that 50 such tests would exhaust the 6,000-question pool, so the gate tests the harness ending each five-generation block ($L=10$, level 0.005) and reverts the block on failure, with the guarantee covering block-end harnesses. E6's sizes became $n_B\in\{150,300,600\}$ (600 times 10 tests uses the whole pool), with pass probabilities 0.26, 0.56 and 0.90 for a tail-neutral harness when 10% of answers change (normal approximation, per-item variance 0.1). $M$ is five points of tail error rate. Rule 9 in E2 uses the middle size |
| 4. StaBLE certification can never certify a non-seed checkpoint with five fall-risk people | fix | StaBLE runs no protective arm: Statistical analysis says why (a bounded Hoeffding test at five people cannot certify below about 1.1 task-score units); certification moved to Global-MMLU, where it certifies the mean-gate lineages of E2 on 1,000 fresh tail items in generation order (Baselines item 9, E2, pseudocode, compute 0.4 billion tokens); the StaBLE certification sentences in Key ideas, Data and splits and the Figure 6 caption were removed |
| 5. H1's recursion has no transition for an archive's parent sampling | fix | Confirmatory H1 uses single-incumbent loops (L1 and L2); L3 forecasts are descriptive. Global-MMLU, H1's primary venue, runs only L1 and L2, so its test is unchanged |
| 6. Prompt scanning misses state written while candidates run on guard or test people | fix | Risks: each candidate runs on guard and test people in a fresh sandbox from an immutable snapshot that sees only that split's cached tool outputs, so nothing written there reaches later candidates or folds; the prompt scan stays as a second check |

## 7. Final state

- Audit (`audit_doc.py`): no em-dashes, en-dashes, banned words, `\operatorname`, missing images, unanchored citations or uncited references; 5,897 prose words (limit about 5,900); 8 figures, 35 references; no staccato or antithesis flags. A manual reread found no "rather than", "instead of" or anthropomorphic phrasing.
- Figures: eight embedded, each referred to in the text, captions *Figure 1.* to *Figure 8.* in order. All eight SVGs lint clean (the loop figure's only note is the library's arc approximation).
- Figure verdicts from `06-codex-figures-r4.md`: edit-effect-scatter fix, drift-sign-map fix, timing-regimes-geometry redraw, instrumented-loop fix, stable-person-splits ship, guarantee-validity-and-price fix. All the fixes in section 5 were applied, re-rendered and inspected; the timing redraw was declined in favour of the targeted arrow and baseline fixes. Codex has not re-reviewed these final renders. concept-mean-vs-tail and dose-response-design were not changed in this pass (both rated ship earlier).
- Counts: 92 review edits applied (none declined; nine in a different form, listed in section 2); W1 to W9 applied; Codex r4: 13 items fixed or partly fixed, 4 declined, and the timing redraw replaced by targeted fixes; Codex r2: 6 high-severity findings, 6 fixed.
