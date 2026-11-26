# Proposal 05: resolutions of the final review and the last Codex rounds

Sources: `05-final-review.md` (independent final review), `05-codex-figures-r4.md` (visual review of all eight figures) and `05-codex-adversarial-r2.md` (second adversarial pass). This run resumed an interrupted one. The interrupted run had applied most of the review and produced earlier versions of r4 and r2, but it then changed the figures and the text again, so both reviews were stale. Their findings are recorded below as "r4 (stale)" and "r2 (stale)", and both reviews were then rerun on the final files.

Final audit (`audit_doc.py`): 5,896 prose words, 8 figures, 26 references, no dashes, no banned words, no missing images, no unanchored or uncited references. The box is 169 words. Every caption starts with *Figure k.* in order, and the text cites Figures 1 to 8.

## 1. Final review: the five main changes

| # | Item | Decision | What changed |
|---|---|---|---|
| 1.1 | Define the design vocabulary before the Hypotheses; add **Trace** | Applied | Key ideas has a **Trace** entry and ends with **The design in brief**, which defines base, variant, the five factors, cell 1 and 8, the three splits, tier 1, tier 2 and configuration. The Hypotheses preamble is gone. |
| 1.2a | Box carries the question, the decisive experiment and the falsifier | Applied | ML contribution opens with "The decisive experiment ...". The falsifier is one sentence naming H1, H1b and H3. This run changed it so that H1b is described as observability's effect, since H1b tests only O. |
| 1.2b | Add H1b (tier-2 O main effect on sealed-test gain) | Applied | H1b is in the list and the table: 480 against 480 loops, falsified if the 95% interval's upper end is below $0.25\sigma_{loop}$. |
| 1.2c | "Why it matters" states the consequence | Applied | Now ends "loops should restructure before searching and rank newborn candidates by code" (completed in this run). |
| 1.2d | Drop the bold research-question paragraph | Applied | Its two follow-up questions close the second problem paragraph. |
| 1.3a | Rename overloaded symbols (S for harness B, $\theta$, $\sigma_{loop}$, $u$ intercepts, $c_{fe}$, $C_R$, $n_{loop}$, one definition of $J$) | Applied | All renamed in the text and in Figures 1 and 2. |
| 1.3b | Drop $f_h$ and $\pi$; expand CMP | Applied | |
| 1.3c | One word for the property (improvability), with evolvability and metaproductivity tied to it | Applied | Key ideas entry is **Improvability**; biology's evolvability and HGM's metaproductivity are named as the same idea. H3's outcome is "an estimate of $E_{100}$". |
| 1.4a | One claim per hypothesis plus a mapping to experiment, measurement and falsifier | Applied | Each hypothesis is one or two short sentences; a table gives experiment, primary test and falsifier for H1 to H7. |
| 1.4b | "One pre-registered primary test" contradicts multi-leg H2 to H5 | Applied (this run) | The sentence now reads "The table gives each hypothesis's primary test, which for H2 and H4 has more than one leg; every other test is secondary". H4's cell names its three tests with Holm correction. |
| 1.5a | Define the success event once, with selection and development variants | Applied | Defined once in Key ideas. This run added that the development variant computes both gain and the shrinkage guard on development people, so loops never read selection people during search. |
| 1.5b | Profile paragraph as a definition list | Applied | Valid, Scoring rule (with the 0.8 example), Shrinkage guard, Profile. This run split the 45-word guard sentence and removed a three-clause run in the scoring rule. |
| 1.5c | Move the six controls to Ablations and controls as "control: what it rules out"; name the placebo | Applied | Five controls are listed, and "Padded cell 1 is the length-matched placebo for cell 8". |
| 1.5d | Split the gate sentence and the refactor experiment | Applied | The gate is a three-item list. Experiment 5 is split into Arms, Prediction and Crossover. |

## 2. Final review: paragraph-level edits

| Section | Item | Decision | Note |
|---|---|---|---|
| Problem | Define and cite OpenCap; split the pilot sentence; add the constant-guess baseline; define RTMPose | Applied | OpenCap is [2] (Uhlrich et al. 2023). |
| Problem | Split the Version S sentence; "may determine"; vary the "how the code is written" refrain | Applied | |
| Problem | Coding-agent paragraph signposts H7 | Applied | |
| Problem | Figure 1 caption avoids "budget $B$"; y-axis says "sealed-test" | Applied | |
| Problem | Figure 2 caption tied to the running example | Declined (optional) | The paragraph just above says that only S's trace shows the empty windows. The caption sentence was cut in this run for length. |
| Problem | Every figure is referred to in the text | Applied (this run) | Only Figure 7 was cited before; Figures 1 to 6 and 8 now have in-text references. |
| Key ideas | Expand SICA; BPT example; split the improvability sentence | Applied | The BPT example is the renaming `v` to `toe_speed_mps`, which is shorter than the review's example. |
| Key ideas | Metaproductivity: 3 and 1 give 0.75; define Thompson sampling | Applied | |
| Key ideas | "its success rate $s$ is the primary outcome" | Applied | |
| Key ideas | Fold sealed people into the design paragraph | Applied | |
| Key ideas | Numeric equivalence example | Applied | |
| Known and missing | Cite AHE at first mention; define pass@1; correct "never ablated" | Applied | |
| Known and missing | Code for Machines numbers; Predict Before You Modify comparator; Meta-Harness summary-versus-raw numbers | Applied | |
| Known and missing | Rewrite the gap paragraph; remove "new only in a narrow sense" | Applied | |
| Hypotheses | H2 must not overstate Code for Machines | Applied (reworded again this run) | "consistent with" became "a sharper test of", because Sonnet 4.5's 2.8-point gap exceeds the 0.025 margin. |
| Hypotheses | Drop "(pre-registered)" from H2; align H6 with Experiment 5; H7 exploratory; define the fifth Holm contrast | Applied | |
| Method | Map sentence; "both levels of each factor"; who annotates; active-voice renaming | Applied | |
| Method | Gate as a list; "no labels are read"; define tool calls; merge the gate audit | Applied | This run also corrected "Sealed inputs are never run during the study", which contradicted scoring each final candidate on sealed people. It now reads "The gate never runs on sealed inputs". |
| Method | Remove the antithesis about the trace channel; fix the permuted-label logic | Applied | |
| Method | "in sessions of ten"; remove the "This is what lets" pivot; report starting $J_{sel}$ | Applied | |
| Method | Say why H3 and $B^{\star}$ use different events | Applied | Both now use the development event, the event the loop accepts on. |
| Method | Figure 5 matches the 0.010 to 0.015 example | Applied | The crossing falls at about 3 times the refactor cost. |
| Method | Prior: expand CMP, explain beta-binomial fitting, numeric example, keep $\tau$ | Applied | This run corrected "HGM's rule is the case $\kappa=2$" to "HGM's Thompson draw is the case": the point estimate HGM reports is $n_s/(n_s+n_f)$, while the Beta(1+$n_s$, 1+$n_f$) draw matches $\kappa=2$, $p_a=0.5$. |
| Method | Refactor-first: remove the pivot; clarify the unverified arm | Applied | |
| Method | Define the island archive and evolve markers; say which trace Meta-Harness reads | Applied | It reads the incumbent's aggregated trace plus a 5,000-token table of earlier candidates. |
| Method | Label the pseudocode "Tier 1" | Applied | This run also made the pseudocode record both the selection and the development events. |
| Experiments | Shorten the splits paragraph; split the bases sentence | Applied | |
| Experiments | Expand IDM; define localization | Applied | |
| Experiments | Gloss "alias"; give an example cell; edit totals as a sum | Applied | This run also added the missing verb in "two-way interactions are confounded in pairs". |
| Experiments | "Each proposer output must begin with a stated cause" | Applied | |
| Experiments | Compress the structural-drift experiment | Applied as a cut | It was not tied to a hypothesis, so it was removed for length along with its reference. |
| Experiments | Contamination wording | Applied | |
| Experiments | Define average marginal effects and the design effect; remove the "which is why" pivots | Applied | |
| Experiments | Define Williams' test | Superseded | The primary H3 comparison is now a single bootstrap statistic, and Williams' test is no longer used. |
| How to read | Remove references to proposals 06 and 07; remove the antithesis; fix the permuted-label row | Applied | |
| Compute | "about 44,100" CPU-hours | Applied and updated | Every row was recomputed in this run. After the extra edits and the r2 fixes: 710 H100-hours, 10.3 billion open-model tokens, 50,900 CPU-hours (including a new 4,900 for the second domain) and USD 410 to 1,230 for the API. |
| Risks | Remove three bullets that repeat Method; add a shrinkage risk | Applied | |
| Learn more | Define GEPA and MIPRO; remove "which is why" | Applied | |
| References | [4] exact title; OpenEvolve authors and year; Ye et al. initials; add OpenCap | Applied and verified | This run checked the OpenEvolve entry against the repository's BibTeX (A. Sharma, 2025, same title) and the Ye et al. initials against arXiv 2608.18066 (Ye Q, Li Y, Pruksachatkun Y, Zhang J, Wu C-S). |
| Tics table | Eleven tics listed | Applied | Reread in this run: no "rather than", "instead of", "which is why", antithesis or intensifier remains. |

## 3. Final review: the cut list

All 17 cuts were applied. Rows 3 and 15 were cut further than asked: the FunSearch/OpenEvolve row and the name-and-context rows were merged, and the drift experiment was removed. The review predicted 5,860 words; the final count is 5,899 because this run added figure references, the guard on development people and the multi-leg sentence, then offset them with smaller cuts (a repeated caption sentence, a repeated model-scope sentence, a file path, the parent-score baseline and several clauses).

The parent-score baseline was removed because the score is constant across a base's variants by construction, so it cannot be tested as a predictor within a base, which is where H3 is evaluated.

## 4. Final review: scientific weaknesses and questions

| # | Weakness | Decision | What changed |
|---|---|---|---|
| W1 | H2's TOST cannot pass at 2,400 edits per level | Applied (more edits) | The interrupted run gave the frontier proposer 70 edits per cell. This run changed that to the full 16-cell factorial at 40 edits per variant (see r2 finding 2): 6,400 edits per level, SE 0.0064, per-factor power 0.98 (0.96 with heterogeneity 0.2) and joint power 0.91 (0.86). Equivalence is claimed factor by factor. The numbers come from the closed form, which reproduces the earlier stated values (0.55, 0.09, 0.96, 0.84, 0.92, 0.71). |
| W2 | H1's composite is underpowered | Applied | The 30B proposer gets 60 edits on cells 1 and 8 (1,200 per cell), giving two-sided power 0.87. |
| W3 | Success rewards shrinkage | Applied | Shrinkage guard (Spearman fall, constant outputs, more than half the spread lost); guard failures reported; starting $J_{sel}$ and the unscored share reported; new risk bullet. |
| W4 | O is delivered through an aggregated channel | Applied | The Meta-Harness numbers are cited, a raw-trace cell 8 control was added, and the Meta-Harness-style loop's input is specified. |
| W5 | H5 is tilted toward the prior | Applied | Per-task counts; archive nodes from the other tier-2 bases in the training folds; feature shift reported. |
| W6 | H3 and $B^{\star}$ use different events; the 0.6 rule is unclear | Applied | One event (development) for both; the raw correlation is primary; 0.6 is a point-estimate criterion; the comparison is "powered only for gaps above 0.4". |
| W7 | Permuted-label control interpreted backwards | Applied | Fixed in Ablations and in the outcome table. |
| W8 | H7 compares different scales | Applied | Exploratory, on the log-odds scale. |
| W9 | Headline question has no hypothesis | Applied | H1b. |
| Q1 to Q8 | Author questions | Answered in the text | Q1 by the single development event; Q2 by the Optimizers paragraph; Q3 by the five Holm contrasts; Q4 by gate item 3; Q5 by per-task counts; Q6 by the pre-outcome audit (the values cannot be known before the gate runs); Q7 by "$\tau$ ... kept unchanged"; Q8 by the heterogeneity powers in brackets. |

## 5. Final review: citations

| Ref | Finding | Decision |
|---|---|---|
| StaBLE [1] | Recheck the 63% figure against the full text | Kept as given in `biomech-facts.md`, which records it from the full text |
| OpenCap Monocular [4] | Bracketed description in place of the title | Fixed |
| DGM [6] | Matches | No change |
| Code for Machines [12] | H2 overstated the source | Fixed (see Hypotheses row) |
| HGM [7] | State whether $\tau$ is kept | Fixed |
| AHE [11] | "never ablated" too strong | Fixed |
| Predict Before You Modify [13] | Name the comparator | Fixed |
| Meta-Harness [14] | Add summaries-versus-raw finding | Fixed |
| OpenEvolve, Ye et al., OpenCap | Format issues; OpenCap uncited | Fixed and verified (see section 2) |

## 6. Final review: figures

| Figure | Review request | Decision |
|---|---|---|
| 1 same-outputs-different-futures | "sealed-test" axis, "warning-only checks", rename B to S | Applied |
| 2 pipeline-two-forms | Expand COM; "RTMPose 2D or OpenCap Monocular 3D"; optional running-example band | Applied; the optional band text was declined because the figure is already at 109 words |
| 3 bpt-equivalence-gate | "Base harness", "match the base" | Applied |
| 4 single-edit-profile | Profile card computes v = 24/30 and s = 4/30 | Applied. This run also changed the legend to "valid, not a success" and "success: gain 1% or more, guard passed", because the success event now includes the shrinkage guard. |
| 5 refactor-first-break-even | r1 = 0.015 so the crossing is at about 3 $C_R$ | Applied |
| 6 parent-selection-at-birth | Redraw with two newborn nodes that DGM and HGM rank alike | Applied |
| 7 participant-splits | Ship | No change |
| 8 two-tier-design | Factor names as row labels; shorter subtitle and lower box; under about 100 words | Applied (101 words, no lint warning) |

## 7. Codex figure review r4 (stale version, written before the last figure changes)

The stale r4 asked for fixes to Figures 1 to 5 and redraws of 6 and 8. The interrupted run applied them before it stopped. Checked here against the current renders:

| Figure | r4 (stale) request | Status |
|---|---|---|
| 1 | "Hypothesized gap"; caps aligned with curves; "identical starting scores"; longer curve-end labels | Applied, except the curve-end labels stay "S" and "A". There is about 60 px between the curve ends and the canvas edge, and the cards on the left name each harness in the same colors. |
| 2 | Replace the code excerpt; give A the same "Feedback to optimizer" end; one collector for S | Applied, except the code excerpt is kept: the 0.7 to 0.3 threshold sweep is the failure the running example turns on (a decision carried over from rounds 1 to 3). |
| 3 | "Rewrite using one level per factor"; "Pad to length / Same token count"; gate lists scores and tool calls first | Applied |
| 4 | "30 one-step edits of one parent"; one arrow into a bracket; v and s prominent | Applied |
| 5 | Zero marked on the y-axis; ratio marked | Applied ("0" on the axis; "break-even ≈ 3× refactor cost") |
| 6 | Three aligned rows with a shared input statement, DGM with the coincident marker, HGM with the shared density, the prior with two labelled densities | Applied |
| 8 | Label the half fraction; number the columns; note on cells 1 and 8; explain 32 settings; two labelled comparisons into one outcome; relate the tiers | Applied ("3 of the 20 bases", "(naming opaque or physical)", two "correlate" arrows into "Sealed-test gain") |

## 8. Codex adversarial review r2 (stale version, written before the last text changes)

| Severity | Finding | Status in the final text |
|---|---|---|
| high | The break-even model uses a different acceptance rule from the loop | Resolved: the Meta-Harness-style loop accepts only development successes, so the profile measures its acceptance event. $s'g'\le sg$ predicts no crossover, and zero successes are handled by the per-edit $sg$ estimator (section 10). |
| high | The crossover is evaluated on the cohort that picks candidates | Resolved: each checkpoint's incumbent is fixed by development error alone, then scored on selection people. The prediction is rounded to the same 25-step grid. |
| high | Full-history loop exceeds the 64,000-token context | Resolved: the proposer sees the incumbent plus a 5,000-token table of recent and best candidates, and a 200-step pilot checks token counts. |
| high | H3 test assumes independent configurations | Resolved: one statistic (the mean over bases of the within-base correlation difference), with a bootstrap that resamples sealed people jointly across configurations and seeds within configuration. The power statement says shared people lower power. |
| medium | Matched-cost predictors have different budgets | Resolved by restating the comparison as equal evaluations ("descendant counts at equal evaluations", "from as many evaluations"); the cost table lists both. |
| medium | The trace control uses one cell | Resolved by scoping: O effects are reported as the joint effect of instrumented code and its trace. Crossing the tracer with all cells and with loops was declined on cost. |

## 9. Codex figure review r4 (rerun on the final figures)

One Codex visual review covered all eight figures: 1 ship (participant-splits), 5 fix, 2 redraw (parent-selection-at-birth, two-tier-design). The fixes below were rendered, linted (no warnings apart from the harmless padlock arc in Figure 7) and checked by eye. As the task allows one Codex review in this pass, they were not sent back.

| Figure | Verdict | Finding | Decision |
|---|---|---|---|
| 1 same-outputs-different-futures | fix | Curve-end letters need a lookup | Applied: the plot was narrowed and the ends now read "S, typed stages" and "A, one function". The axis labels were repositioned to clear a lint overlap. |
| 1 | fix | Rename the center box "Same starting score"; "every input" reads as universal | Declined: identical outputs on every input is the premise of the figure and of the research question. The origin is already labelled "same starting score". |
| 2 pipeline-two-forms | fix | Parallel feedback wording for both harnesses | Applied: "Optimizer receives: score error only" and "Optimizer receives: score error plus a per-stage trace". |
| 2 | fix | Replace the code block; move the warning callouts to the caption | Declined: the 0.7 to 0.3 threshold sweep is the running example's failure, and the warning-only checks are factor T, part of what S is. Both decisions date from rounds 1 to 3. |
| 3 bpt-equivalence-gate | fix | Compress the factor group to names only; arrows align with the P card | Declined: round 2 asked for each factor's levels so the group would not read as a fixed recipe. The arrows end at the dashed group boundary, about 25 px from the P card, and the gate's first line already reads "Scores and tool calls match the base". |
| 4 single-edit-profile | fix | Say every edit is from the same parent; shorten the legend | Applied: the header reads "30 edits, each of the same parent (illustrative)" and the legend reads "invalid", "valid, not a success" and "success: gain 1% or more, guard passed". The success line keeps its definition, since the guard is new. |
| 5 refactor-first-break-even | fix | Flat refactor segment hidden on the axis; duplicate B* labels | Applied: the refactor interval is shaded and labelled "refactoring, no gain yet", and one label "B* ≈ 3× refactor cost" sits at the crossing. The axis keeps "budget in evaluation-equivalents", because $C_R$ is in those units. |
| 6 parent-selection-at-birth | redraw | Three rows tie the nodes in different visual ways; densities overstate precision; no arrowheads | Applied: the parent now has arrows to both new nodes. Every row uses markers on its own scale, with an orange ring around a blue dot where the nodes coincide (DGM and HGM rows) and separated markers in the prior row, whose card reads "Hypothesized separation by code". Spread bars replace the densities. The caption now says "Positions and spreads are illustrative". |
| 7 participant-splits | ship | Optional title change | No change |
| 8 two-tier-design | redraw | Predictors point into "Sealed-test gain", so they look like its inputs | Applied: "96 configurations" now fans out to three parallel boxes ("Profile forecast", "Clade estimate (HGM)", "Observed sealed-test gain"), which all feed one "Correlate within base: each predictor with the observed gain" box. The evaluation budgets stay in the figure, since they define the equal-evaluation comparison. The caption names the frontier proposer's extra eight cells and the five single-incumbent loops H3 uses. |

## 10. Codex adversarial review r2 (rerun on the final text)

Verdict: needs-attention, with five high-severity findings and one medium. All five high findings are resolved; one part of finding 1 is declined with a reason.

| Severity | Finding | Decision | What changed |
|---|---|---|---|
| high | H6: the gate reads selection inputs inside the refactor phase, and the prediction profiles only the first seed's refactor | Applied in part | The refactor phase now runs once per base, starting form and arm, and every loop of that arm continues from its frozen output, so the twelve profiled refactors are the ones whose crossover is measured. This also cuts gated refactors from 2,100 to 210 (CPU 1,380 to 1,030). The gate keeps reading selection inputs. It reads no labels, and a refactor it admits reproduces the base's selection-person outputs exactly, so every admitted refactor has the base's selection error and the gate cannot favor an arm on selection people. Checkpoint incumbents were already fixed by development error alone. |
| high | H2: in $I=MOPT$ each main effect is aliased with a three-way interaction, so cancelling effects could pass TOST | Applied | The frontier proposer runs all 16 M, O, P and T combinations at 40 edits each, so its main effects are not confounded with three-way interactions. The cost is 1,600 more edits than the 70-per-cell plan (frontier 18,200 edits, 300M tokens, 3,340 CPU-hours, USD 410 to 1,230), and power rises to 0.98 per factor and 0.91 jointly. The figure caption and pseudocode are updated. |
| high | H3: the forecast is undefined with zero successes and is tested against a different search policy | Applied | The forecasts use only $sg$, estimated as the mean development gain per edit with non-successes counted as zero, which is finite for zero successes. The $(k+0.5)/(n+1)$ smoothing is removed. H3 now correlates with the five single-incumbent (Meta-Harness-style) loops per configuration, which the loop model describes. The rerun simulation (outcome reliability 0.71 for five loops, by Spearman-Brown from 0.83 for ten) gives beat-the-clade power 0.80 at true correlations 0.7 and 0.3, and 0.35 at 0.6 and 0.4. |
| high | Gate failures can unbalance paired contrasts; no consequence for a sealed-audit mismatch | Applied | "A base enters a contrast only if every cell the contrast needs passes", and "a mismatch voids every contrast that uses the variant". The pseudocode calls `drop_from_contrasts`. |
| high | H5: per-task clade counts undefined (reference, guard, root) | Applied | "Each evaluated node except the root adds one count per task: a success if it is valid, passes the guard and lowers that task's development MAE by 1% relative to its own parent, else a failure. HGM's estimates in H3 and H5 use the same counts." |
| medium | Second-domain CPU listed as "small" | Applied | 148,000 Polyglot attempts at an assumed 2 CPU-minutes each give 4,900 CPU-hours, and the 200-step pilot checks "token and CPU figures". The total rises to 50,900 CPU-hours. The per-attempt rate is an assumption, not a measured figure, because the HGM paper's allocation numbers were not verified here. |

## Cuts made in this run to stay at about 5,900 words

The cuts were: a repeated Figure 2 caption sentence, a repeated loop-model sentence and a file path; the parent-score baseline (constant within a base by construction); the H2 clause on Code for Machines (the literature table carries it); the outcome row for permuted labels (the Label noise control states its reading); the video-derived-reference risk (the text already judged it minor for this question); the hint-audit risk, merged into Method; and several shorter clauses.

## Left open

- The sealed participants were scored once in the lab pilot, so a confirmatory claim needs a fresh cohort (stated in Risks).
- Tier-2, H5-secondary and H6 claims rest on three bases and the 30B proposer (stated in Risks).
- The frontier API proposer is named and pinned only at registration.
- The Polyglot CPU rate (2 CPU-minutes per attempt) is an assumption that the pilot must measure.
- The figure fixes in section 9 were checked by eye and by lint but not by a second Codex round.
