# Proposal 08: resolutions of the final review and the last Codex passes

Sources: `08-final-review.md` (independent final review), `08-codex-figures-r4-first.md` (first round-4 visual review of all eight figures, run before the interruption), `08-codex-figures-r4.md` (round-4 verification pass on all eight figures after the fixes) and `08-codex-adversarial-r2.md` (second adversarial pass). Text fixes are in `docs/idea-summaries/08-blind-analysis-for-agents.md`; figure fixes in `output/idea-summaries-build/figs_08.py`. This run resumed an interrupted one: every item below was checked against the current text, and items the interrupted run had already applied are marked "Fixed (earlier in this pass)".

Final audit: see the last section.

Counts for the summary: the review lists 78 edits; 76 were applied and 2 were answered only in part (see "Declined review items"). Codex adversarial r2 raised 4 high and 2 medium findings; all 6 were fixed, with two specific recommendations declined with reasons. Codex figures r4 (verification pass) gave fix verdicts on 6 of 8 figures: 2, 5, 6 and 8 fixed, 3 partly fixed, 7 declined with a reason.

## 1. Top five clarity changes

| Item | Decision | What changed |
|---|---|---|
| 1.1 Rewrite the box; optional title | Fixed (earlier in this pass); completed now | Title is now "Can a clinician undo what the referral did to an agent's measurement?". Research question is two sentences (how far the number moves and whether recalibration undoes it; which route and whether self-improvement moves it). "Gated" is replaced in the box by its meaning ("every agent whose blind reports track the reference") and SD is spelled out as between-person standard deviations. Falsifiers map one-to-one onto P1, P2 and P4. ML contribution now says splicing replays the recorded tool calls and outputs into a report step told another referral; a missing comma was added in this run |
| 1.2 Separate route from recoverability | Fixed (earlier in this pass) | Key ideas has separate **Route** (direct route defined with the transcript held fixed) and **Recoverability** paragraphs with the 5 s and 25 s example; "either route can produce either map" appears there and in the Figure 4 caption. H3 is an association with pre-specified route classes. This run added that route classes are fixed from the splices before any E5 log loss is computed |
| 1.3 Hypothesis-to-test table, decisive test, signposts | Fixed (earlier in this pass) | Table (hypothesis, experiment, outcome, falsified if) after H6; "The decisive test" paragraph (E2 then E5, fails if recalibration repairs every agent); one signpost sentence at the top of Method and of Experiments |
| 1.4 Symbol clashes, sign convention, forward references | Fixed (earlier in this pass); completed now | Policy is $\kappa$; class means $m_C$; fixed effect $\theta_h$; $\sigma^2$ and $\mathcal V$; $M_0$, $M_H$ and $v$ in Proposition 2; one referral symbol $H$ with values $a$, $b$; the 20 people are "calibration people". Sign (effects signed $b$ minus $a$, positive toward the referral's typical value) and subscripts ("name the referral held fixed") are stated. logit, LLR and $2H-1$ are defined; this run added "nats (natural-log units)". Key-ideas entries exist for the measurement gate, sealed/calibration/development people and scripted controls. This run also defined "the indirect effect" when no ordering is named, as $(\mathrm{IE}_a+\mathrm{IE}_b)/2$, which P2, P3, H3 and Figure 8 rely on |
| 1.5 Concrete opening, worked number, split table | Fixed (earlier in this pass) | Problem starts with the referral and the agent; the 60% against 75% posterior from Proposition 1 is in paragraph 3 (rechecked: logit 0.386 gives 0.595, logit 1.100 gives 0.750); a four-row split table replaces the split arithmetic |

## 2. Paragraph-by-paragraph edits

| Location | Decision | Note |
|---|---|---|
| Problem ¶1 reorder; gloss RTMPose, OpenCap Monocular, OpenCap | Fixed (earlier) | |
| Problem ¶2 split; anthropomorphic "treats the sway"; align "routine screening" with Figure 1 | Fixed (earlier); "one defensible transcript stops timing" changed to "one defensible analysis" in this run | Figure 1 reads "routine screening, no balance concerns" |
| Figure 1 caption "yet" pivot | Fixed (earlier) | |
| Problem ¶3 split; worked number; review/incorporation bias and QUADAS-2 moved to Known; "yet" pivot | Fixed (earlier); tightened in this run | |
| Problem ¶4 slogan | Fixed | The one-sentence pointer paragraph was merged into ¶3 in this run |
| Problem ¶5 split; cut literature sentence; new last sentence | Fixed (earlier) | |
| Path, transcript and report: define report step | Fixed (earlier) | |
| "True group" sentence | Fixed (cut, C3) | Consistency is not analysed |
| Combiner: define $p$ and nats | Fixed | "natural-log units" added in this run |
| Routes and recalibration paragraph | Fixed (replaced, 1.2) | |
| Path splicing key idea fragment; gloss interventional effects | Fixed (earlier) | |
| Steering index and evidence sensitivity key idea | Fixed (moved to Method, C6) | |
| Self-improvement and shrinkage split; expand GEPA, ACE, GRPO | Fixed (earlier) | |
| Blinding: skeleton against "skeleton or silhouette" | Fixed | Text and Figure 6 both say skeleton render |
| Known ¶1 Loy and Irwig duplicate | Fixed | Loy and Irwig appear in Problem and Risks only |
| Table: Xiao and Yu "exploratory interventions only" | Fixed (earlier) | |
| Gap ¶ split, "thus" pivot, dangling video sentence | Fixed (earlier) | |
| H1 estimand and API agent | Fixed | H1 states TE averaged over clips; the table names P1 as TE; "the frontier API model" is named in H1 |
| H2 sign and orderings | Fixed | |
| H3 rewrite and antithesis | Fixed | |
| H4 $\gamma_B$ forward pointer | Fixed | |
| H5 split | Fixed | |
| H6 MAE units | Fixed | "its MAE stays within 0.2 SD" |
| Setting and notation split; $H=1$ high risk; bridge-task pointer; decision referral texts (W8) | Fixed | |
| Proposition 1 build path and "preliminary simulation" | Fixed (C9) | "Quadrature over 36 parameter settings and ten values ... positive in all 360 cases" |
| Three boundaries paragraph | Fixed | The signpost "Three boundaries matter" was dropped in this run for length; the three boundaries each lead their sentence |
| Proposition 2 symbols, Ent, conditioning of the cap identity | Fixed (earlier) | Identity now sums over $h$ with $\Pr(M_0>c_h\mid H=h)$ |
| Path splicing sign, subscripts, long sentences, common support, prefix splice | Fixed (earlier) | |
| Steering index is a percentile shift; $\mathcal V$ | Fixed (earlier) | |
| Evidence sensitivity; gate in its own entry; pilot quoted once | Fixed | Evidence sensitivity compressed to one clause in this run |
| Effective shrinkage split; $\gamma^*$ equivalence; reward (a) pointer | Fixed (earlier) | |
| Blind harness self-contradiction, long sentences, "blind then unblind" | Fixed (earlier; C13) | |
| Self-improvement loops: Pareto jargon, positive control, LoRA | Fixed (earlier) | |
| Data and splits table; Cam0 | Fixed (earlier) | "Cam0" no longer appears |
| Bridge sets: physical-accuracy claims | Fixed | "(agreement with markers)" |
| Models: InternVL3.5-8B; LoRA wrapping; scripted controls as a 2×2 | Fixed | Scripted controls are listed by route and map in Key ideas |
| Baselines item (5) misattribution | Fixed | Guard instruction, with Brown et al.'s finding that it reduced harmful flips without removing them and removed helpful corrections |
| Metrics "tokens and time" | Fixed (C18) | |
| E3 exploratory; E4 checkpoints | Fixed | Six checkpoints follow from "an audited checkpoint every 1,000" of 6,000 rollouts and are drawn in Figure 7 |
| E5 both referrals; count of fixed agents | Fixed | "up to four gated fixed agents"; both referrals stated once, in Data and splits |
| Statistical analysis: rename $\beta_f$; P1 family; variance convention (W4); P4 power (W1); "for this proposal" | Fixed | This run also stated the $\alpha$ behind the P3 detectable gap (0.18 SD at 0.05, 0.22 SD at Holm's strictest level) |
| Second domain split; agent model; assignment matrix | Fixed | "assigned at $q=0.2$" |
| Synthetic check compression | Fixed (C12) | |
| Results table slogans, anthropomorphism, gate row | Fixed | |
| Compute assumption sentence split | Fixed | |
| Risks ¶1 pilot repetition; gate fallback | Fixed | The fallback lives in Models and tools and in the results table; the duplicate in Risks was cut in this run |
| Risks ¶3 duplicate sentence; winner's curse | Fixed | |
| Long sentences over 40 words; LLM tics | Fixed | Reread in this run; the Figure 3 caption "yet" pivot was removed in this run |

## 3. Cut list

C1 to C18 were applied (C4 removed the Alexopoulos row and its reference; C14 replaced prose with the split table). The interrupted run left the document at 5,972 audit words. This run cut a further 70 words net while adding the indirect-effect definition, the P3 $\alpha$ and the Figure 8 caption clarifications: merged the Problem pointer paragraph, shortened the Referral and Effective-shrinkage key ideas, the Batista and Griffiths sentence, the estimand sentence in Path splicing (already in Key ideas), the H5 support clause (Gao and Xiao stays in the table), the data-blinding gloss (already in Key ideas), the duplicated $\gamma_B$ numbers (already in Figure 3's caption), a duplicated "every clip under both referrals", the Risks fallback sentence and the course-module glosses.

## 4. Scientific weaknesses

| Item | Decision | What changed |
|---|---|---|
| W1 P4 unpowered | Fixed | Every sealed clip runs under both referrals and person log loss is weighted by $\Pr(H\mid C)$; P4's power is computed for a lossy cap in Proposition 1's setting; EchoNet's 1,000 sealed videos carry the confirmatory test and StaBLE gives an estimate. This run recomputed the numbers by Monte Carlo (two million people, `scratchpad p4.py`): mean 0.0143 nats, SD 0.107, about 630 people for 80% power at 0.0125 (the text had 0.015 and 590), milder cap about 1,200 (was 1,100), EchoNet power 0.96 and 0.71 (was 0.97 and 0.74). Text corrected |
| W2 route and recoverability conflated | Fixed | See 1.2 |
| W3 $\gamma_B$ moving target | Fixed | Formula pre-registered and refit at each reward-(a) final checkpoint from that checkpoint's blind reports on development people; pre-loop value secondary; compute row added |
| W4 variance convention | Fixed | Contrast-level convention stated; the per-referral alternative is computed (variance 0.161, 75 people; power 0.71; TOST 0.90). Rechecked: 0.0908, $d_z=0.664$, $n=42.0$; 0.161, $n=74.6$ |
| W5 P3 power at the edge | Fixed | Seeds reallocated to 8, 3 and 4 per optimizer (45 runs, same compute); Figure 7 redrawn |
| W6 gate feasibility | Fixed | Pilot reports MAE only, stated; scripted pipeline gated first; fallbacks to tasks where the pipeline passes and then to the LoRA agent; results-table row |
| W7 margin on measurement scale | Fixed | The 0.2 SD margin's decision cost (about 0.004 nats at $\gamma\approx0.14$) is stated and lossy paths are left to P4 |
| W8 decision referral texts | Fixed | $a$ and $b$ are the Parkinson's and routine-screening notes in every experiment; "collegiate gymnast" is one of the extra E1 lines |
| W9 placebo tolerance equal to smallest effect | Fixed | Placebo margin 0.05 SD by two one-sided tests, per referral and arm |
| W10 scope | Fixed | Core and secondary experiments named at the top of Experiments |

## 5. Citation spot-check

| Ref | Decision | Note |
|---|---|---|
| [6] Gunsilius et al. | Fixed | "Four frontier agents" |
| [8] Asher et al. | Fixed | "even given a directional hypothesis" in the table and Risks |
| [23] Brown et al. | Fixed | Baselines item (5) |
| [5] Loy and Irwig pages | Fixed | 292(13):1602 to 1609 |
| [19] diacritic | Fixed | Hróbjartsson |
| [24] Xiao and Yu | Fixed | "exploratory interventions only" |
| [1], [10], [12], [25] | No change needed | Review found no mismatch |
| [27] Gao and Xiao | No change needed | Still cited in the table after the H5 clause was cut |

## 6. Figure review in the final review

| Figure | Decision | What changed |
|---|---|---|
| 1 one-video-two-referrals | Fixed | Caption replaced; figure says "routine screening, no balance concerns"; bullets labelled "Timing" and "Filter" |
| 2 referral-counted-twice | No change needed | Ship |
| 3 better-measurer-worse-decision | Fixed | Bayes-report diamonds at $\gamma_B=0.214$ with their own MSE (0.614) and penalty (0.019), labelled "Bayes report"; MSE curve in neutral ink; parallel callouts "36% lower MSE at γ*" and "+0.026 nats at γ*". Caption explains the diamonds |
| 4 calibration-bug-or-information-bug | Fixed | Retitled by map ("One-to-one ...", "Many-to-one ..."); one neutral segment labelled "both referrals below the cap"; orange plateau labelled "high-risk referral a"; caption says either route can produce either map |
| 5 path-splicing-factorial | Fixed | Caption adds the subscript rule; example card replaced by a key "Cells: μ(path, report)" with "→ direct: report referral changes" and "↓ indirect: path referral changes"; dotted leader removed; in this run the key card was aligned with the top row (it had empty space below) |
| 6 blind-analysis-harness | Fixed | Caption limited to the appearance-blind variant; "or silhouette" dropped; Decision outlined in orange with "uses the referral once, as prior"; Referral card "unlocked after commit" |
| 7 self-improvement-design | Fixed | "Audit 6 checkpoints per run"; seeds 8, 3 and 4 written in each reward card; design line "3 optimizers × 15 seeds = 45 runs" |
| 8 predicted-routes-by-optimizer | Fixed (redrawn) | Now aligned final-checkpoint bars per optimizer row, dark indirect and light direct on the $\hat\gamma$ scale, a thin $\gamma_B$ line inside the grey H4 band, and an open control mark for reward (c). The x-axis problem (generations against six checkpoints) is gone. GEPA/ACE and GRPO totals (0.24 and 0.205) both sit in the band; this run's caption says only the route split is predicted to differ, that the indirect effect is averaged over orderings, and that the band is drawn at Figure 3's 0.214 |

## 7. Codex figures, round 4 (first pass, `08-codex-figures-r4-first.md`, before the interruption)

All of these were applied by the interrupted run and checked against the current PNGs in this run.

| Figure | Finding | Decision | What changed |
|---|---|---|---|
| 1 | Parallel outcome-facing wording; label timing and filter roles | Fixed | Bullets read "Timing: stops at the first large sway" / "Timing: continues after balance recovers" and "Filter: low-pass at 3 Hz / 6 Hz" |
| 2 | Bayes diamonds look like extra samples | Fixed | Labelled "Bayes report"; caption says they are plotted at $\gamma_B$ with their own MSE and penalty; parallel callouts at $\gamma^*$ |
| 3 | Coincident orange and purple below the cap; plateau unlabelled | Fixed | One neutral segment "both referrals below the cap"; orange plateau labelled "high-risk referral a"; violet dashed continuation starts at the split |
| 4 | Dotted leader looks like a fifth edge; arrow meaning implicit | Fixed | Leader removed; key card "Cells: μ(path, report)" with "→ direct: report referral changes", "↓ indirect: path referral changes" |
| 5 | Release condition and single use of the referral carried by card text only | Fixed | Referral card "unlocked after commit"; Decision card states the referral is used once, as prior |
| 6 | Dots must be counted; checkpoints per run unclear | Fixed | "8 seeds", "3 seeds", "4 seeds" in the reward cards; "Audit 6 checkpoints per run" |
| 7 (predicted routes) | Redraw: trajectories with checkpoint axis 0 to 6; zero line doubles as control | Fixed (redrawn) | Aligned final-checkpoint bars per optimizer, indirect and direct segments, control as its own marked row, shared $\hat\gamma$ scale with the H4 band |

## 8. Codex figures, round 4 (verification pass, `08-codex-figures-r4.md`)

Verdicts: ship 1 and 4; fix 2, 3, 5, 6, 7, 8. All fixes re-rendered, linted (no warnings beyond arc-approximation notes) and inspected by eye.

| Figure | Finding | Decision | What changed |
|---|---|---|---|
| 1 one-video | Ship; caption could call timing and filter paired settings | No change needed | Caption already says only the referral line differs and that stopping at the first sway shortens the hold |
| 2 counted-twice | Second count reaches the combiner through a grey arrow; split combiner copy | Fixed | Measurement-to-combiner arrow and "referral-shaped M" now orange; combiner reads "prior odds × likelihood ratio / fitted on blind reports". Caption rewritten: orange arrows trace the two counts, the second passing through $M$ |
| 3 better-measurer | Diamonds read as extra samples; add a shared key and x-axis ticks at $\gamma_B$ | Partly fixed | Diamonds enlarged (radius 9) and the right label moved clear of the curve. Declined the shared key and axis ticks: a $\gamma_B$ tick label at 0.214 would collide with the 0.25 tick label 17 px away, and each diamond already carries a "Bayes report" label while the caption gives $\gamma_B$ and both values |
| 4 calibration | Ship; optional footer shortening | No change needed | |
| 5 path-splicing | Headers ambiguous about what each factor holds | Fixed | Columns "Report step told a (high risk)" / "Report step told b (routine)"; rows "Path run under a / b". Declined moving the interaction equation to the caption: the figure teaches that the two orderings differ by it, and the text uses that identity |
| 6 harness | Which input supplies evidence and which the prior is implicit | Fixed | Decision card reads "evidence: commit / prior: referral, used once" |
| 7 self-improvement | Label the bracket output "saved checkpoints"; tie the matrix to development people | Declined | The bracket-to-audit arrow is 42 px long, too short for a label without moving the matrix, and the audit card already says "Audit 6 checkpoints per run"; the banner directly above the matrix says optimizers run, select and train on development people |
| 8 predicted-routes | Route labels sit on the band edge; zero line shows through the control marker; long headline | Fixed (two of three) | Route labels start beyond the band edge (plot narrowed to 330 to 1110 px); zero line drawn before the bars so the open marker hides it. Kept the headline: it states the figure's one point and the status line above it marks the figure as hypothetical |

## 9. Codex adversarial, round 2 (`08-codex-adversarial-r2.md`)

The helper fell back to the scoped `codex exec` run (working-tree diff over the plugin limit). Codex judged the round-1 splice, signed-endpoint and holdout findings resolved and raised six new ones.

| Severity | Finding | Decision | What changed |
|---|---|---|---|
| High | A replay artifact can decide which agents enter P4; support and conflict checks have no consequence | Fixed | Path splicing now states the agent always runs in the same two-stage form, so natural runs and all four cells share one stateless report call and route labels describe the agent in this harness. An agent whose placebos fail, or whose cross-splices fall outside common support on over 20% of clips, gets no route class and is left out of H3 and of P4's path-route set. P4 is also reported for all gated agents pooled, a set no route label selects |
| High | The results table still calls a residual proof of information loss and repair proof of a one-to-one map | Fixed | Rows now read "The tested combiners cannot recover what the path removes" and "The tested combiners recover path effects". The within-referral combiner is specified (kernel-density likelihood refitted per referral on development people, with a learning curve at half and all of them). H3 already limits a residual to the pre-specified combiners, and the scripted controls are the only cases with known maps |
| High | P4 is powered against zero while H6's rule uses a 0.01-nat margin | Fixed | One pre-registered criterion: P4 supports H6 if the difference exceeds zero at its Holm level and falsifies it if it is negative or TOST places it within ±0.01 nats; 0.01 nats is an equivalence margin, not a superiority threshold. Added the equivalence power at a true zero on 1,000 videos (0.81; SE 0.107/√1000). The hypothesis table already reads this way. Not adopted: powering superiority against 0.01 nats (about 8,000 people), because H6 claims the blind harness beats recalibration, not that it beats it by a margin |
| High | $\gamma_B$ conditions on the blind scalar while the trained agent sees the clip | Fixed | H4's band now states its assumption (the context-visible run uses no evidence beyond its blind number) with a pre-registered check: where the context-visible MSE is significantly below that of $\mathbb{E}[T\mid M_0,H]$, H4 is reported but not tested; TE, MSE and log loss are always tested separately. A separate restricted-reporter arm was not added: the check identifies the runs for which the band is not a valid target at no extra compute |
| Medium | P3 can pass with identical route allocation | Fixed | H5 also needs GRPO's direct effect to exceed prompt evolution's (secondary); GEPA and ACE are reported separately |
| Medium | Failed reports have no defined contribution to P1 and P2 | Fixed | In P1 and P2 a failed, excluded or repeat-requested report takes the clip's referral-free median path value, with the paired coverage contrast beside TE and complete-case means secondary |

## Declined review items (with reasons)

| Item | Reason |
|---|---|
| Final review, Question 6: how GRPO's 6,000 rollouts divide between path-phase and report-step tokens | Not added: the compute table prices each rollout at 22k processed tokens covering both phases, and throughput is measured on one complete E4 checkpoint before the loops are sized, which settles the split empirically |
| Final review, Question 2: how the pilot LoRA agent is wrapped | Answered only in one clause ("runs in the same harness and reports the task score"); a fuller description would cost words for an agent that is audited on 43 people only |
| Codex r4 verify, Figure 3 shared key and $\gamma_B$ axis ticks; Figure 5 interaction to caption; Figure 7 bracket label; Figure 8 headline | See section 8 |
| Codex r2, P4 superiority against 0.01 nats; restricted-reporter arm for H4 | See section 9 |

## Self-checks in this run

| Check | Result |
|---|---|
| Worked posterior 60% and 75% | logit 0.386 → 0.595; logit 1.100 → 0.750 (Proposition 1 setting, $\gamma^*=0.357$) |
| P1, P2, TOST power arithmetic | 0.0908, $d_z=0.664$, $n=42$; per-referral 0.161, $n=75$; P2 power 0.94 (0.71); TOST 0.99 (0.90) |
| P3 detectable gap | 0.18 SD at $lpha=0.05$; 0.22 SD at $lpha=0.0125$ (now stated) |
| P4 power | Monte Carlo with two million people: mean 0.0143 nats, SD 0.107; $npprox630$ at 0.0125; milder cap $npprox1{,}200$; 1,000 videos give 0.96 and 0.71; corrected in the text |
| 0.2 SD margin's decision cost | $\gammapprox0.14$, penalty about 0.004 nats from the simulated curve |
| Every figure referred to in the text | Added in-text references to Figures 2, 4, 5, 6, 7 and 8; captions start with *Figure 1.* to *Figure 8.* in order |

## Final audit

`python3 -B output/idea-summaries-build/audit_doc.py docs/idea-summaries/08-blind-analysis-for-agents.md`: 5,900 prose words, 8 figures, 34 references; no em-dashes or en-dashes, no banned words, no antithesis-pattern warnings, no missing images, no unanchored or uncited references, no staccato runs. Box: 169 words. Reread for the unscripted rules (no "yet" or "thus" pivots, no anthropomorphism, symbols defined at first use, one running example).
