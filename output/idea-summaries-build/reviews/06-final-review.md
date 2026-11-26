# Proposal 06: final independent review

Doc: `docs/idea-summaries/06-who-self-improvement-leaves-behind.md` (audit: 6,187 prose words, 8 figures, 34 references; no dashes or banned words). Figures rendered to `output/idea-summaries-build/png/06/` and inspected. The resolutions table was read first; points it settled are not re-raised unless noted.

**Verdict for this pass.** The science is careful and the earlier high-severity findings are fixed. What still stands between a reader and the four things they should take away (question, why open, decisive experiment, falsifier) is presentation: the question is split across a dense box and the middle of a long paragraph, the one quantity everything rests on (the covariance $C$) is never stated in words before the equations, the "selection term" that H2 tests is never defined, five symbols are overloaded, and no passage maps hypotheses to experiments. Two scientific gaps need attention as well: H1's power at about five fall-risk people per block, and circularity in E4's rescoring arm.

---

## 1. The five changes that would most improve readability and clarity

### 1.1 Give the question, why it is open, the decisive test and the falsifier one plain sentence each

The box uses three terms the reader has not met ("correlated-response law", "sealed guard set", "rejected candidates"). "Sealed guard set" also clashes with the document's own vocabulary, where "sealed" means test people and guard people are only "hidden". "Rejected candidates" suggests the estimator uses only rejected edits, when it uses every candidate. The body's statement of the question sits mid-paragraph in the Problem section, followed by an unrelated pilot sentence. The decisive experiment is never named.

Proposed box (about 160 words, under the 170 limit):

> **Research question.** When a self-improving agent keeps only edits that lower its average error, how does a small group fixed in advance (people at risk of falling) fare, and can that be forecast early from every candidate the loop scores?
>
> **Why it matters.** Balance tools exist to find people who balance poorly, yet such people are about one in seven in StaBLE, and GEPA, Meta-Harness and the Darwin Gödel Machine select edits on scores the majority dominates; no published study tracks a subgroup's held-out error across generations of such a loop.
>
> **ML contribution.** A guard-set estimate of the quantity that sets the group's fate (the covariance between an edit's effect on the group and the score that selects it), a forecast and a dose-response test built on it, and a sample-size rule for protective gates.
>
> **What would prove it wrong.** A generation-10 forecast that predicts the generation-50 change no better than extrapolating the group's own curve, or Global-MMLU tail drift that does not change sign at the tail weight where that covariance crosses zero.

In the Problem section, end with a short paragraph of its own after the Global-MMLU example:

> "The question is whether a loop can predict how a group fixed in advance will fare on sealed test people, using candidates it already generates scored on a held-out guard set, and which acceptance rule protects that group at the lowest cost in average improvement. It is open because published work tracks items or averages, never a human subgroup's held-out error across generations (next section)."

At the top of Hypotheses, add one sentence naming the decisive tests:

> "Two tests carry the proposal: H2 in E4's rescoring arm, where the same frozen edits are re-selected at four tail weights so that only selection changes, and H1 in E3, where a forecast frozen at generation 10 must beat extrapolation at generation 50."

### 1.2 Say what the law says in words, and define the "selection term", before any equation

The proposal rests on one number, $C=\mathrm{Cov}(b,S)$, but no sentence says in plain words what it does before the reader reaches three display equations. H2, E4, Figure 3, Figure 8, the ablations and the Baselines prediction all talk about "the selection term", which is never defined. It is the second term of $D$, $(C/\sigma_S)\phi(z)$. It also equals $\mathrm{Cov}(b,\mathbf{1}\{S>0\})$, which is Price's $\mathrm{Cov}(\omega,b)$ and what the guard log estimates. So one definition links the Gaussian law, the Price form, the estimator and H2.

Add to Key ideas, at the end of "Correlated response":

> "In a self-improvement loop the selected trait is the gate's score $S$ and the correlated trait is an edit's tail effect $b$. The tail's expected change per accepted edit is then its average edit effect plus a term proportional to $C$, the covariance of $b$ with $S$. When $C$ is negative, the harder the gate selects, the more the tail loses."

Add right after the $D$ display:

> "In words, $D$ is the tail's average edit effect times the acceptance rate, plus a selection term $(C/\sigma_S)\phi(z)$. The selection term equals the covariance between an edit's tail effect and whether the gate accepts it, $\mathrm{Cov}(b,\mathbf{1}\{S>0\})$, which the guard log estimates directly and which Price's equation generalizes beyond the Gaussian case."

Then state "noise rescales the selection term but cannot flip its sign" **once**, here. It currently appears in H2, the paragraph after $D$, the Figure 3 caption and alt text, the Figure 8 caption, E4 and the selection-strength ablation.

### 1.3 Add a map from hypotheses to experiments, and signposts at the top of Method and Experiments

A reader has to piece together that E3 tests H1, E4 tests H2, E5 tests H3, E6 tests H5 and E7 tests H4, while E1 supplies moments and E2 supplies loops. H1 names two comparators and E3 lists four. Add a two-sentence roadmap at the top of Method:

> "Method has four parts. The law says when selection on the mean harms the tail and the timing model says when that sign turns; the guard log and forecast measure the law's inputs from a running loop; the protective gate, its sample-size rule and its validity conditions answer which rule protects the tail most cheaply."

Then put a small table at the top of Experiments, replacing prose that currently has to be inferred (about 90 words):

| Hypothesis | Tested in | Domain | Fails if |
|---|---|---|---|
| H1 forecast | E3 (E1 panels, E2 loops) | Global-MMLU, StaBLE | frozen forecast's paired error is not below extrapolation's or accepted-only's, or coverage under 80% |
| H2 dose-response | E4 rescoring arm, then loop arm | Global-MMLU | sign of the selection term disagrees with the sign of $C(\pi)$ from held-out edits |
| H3 timing | E5 | StaBLE parameterized harness; open-ended lineages | predicted regime mismatches later-panel drift sign |
| H4 mechanism | E7 | StaBLE | tail harm vanishes after affine recalibration |
| H5 price and validity | E6 | Global-MMLU | violation rate above 5%, or gain kept departs from the design rule |

### 1.4 Remove overloaded and undefined notation, and fix terminology drift

Overloaded symbols:
- **$K$** is candidates per generation ($K=4$), the best-of-$K$ index in $m_K(c)$, and the panel size in $\hat D=\frac1K\sum_{e=1}^K$ (the panel has 200 edits). Use $m$ (or $N_{\text{panel}}$) for the panel.
- **$D$** is per-proposal drift and also the dev set in the pseudocode (`dev people D`, `score(e, D, ...)`).
- **$G$** is the guard set (pseudocode), $G_t$ the cumulative majority gain, and G1/G2 the validity conditions. Rename the gain $\Gamma_t$ and the conditions (V1)/(V2).
- **$T$** is the number of tests in the design rule and the sealed test set in the pseudocode, next to generation $t$ and "the $t$ test". Use $L$ for the number of tests.
- **$H$** is cumulative harm and also the hypothesis labels H1 to H5. Consider $R$ ("regression") for harm.
- **$z$** is $\mu_S/\sigma_S$ and also normal quantiles $z_{1-\alpha_t}$. Define the quantile notation in one clause.

Symbols and terms never defined:
- **$\tau$**: first used in $\mathbf{1}\{S_{\text{dev},e}>\tau\}$ and in Figure 6. Add: "$\tau$ is the gate's threshold on $S$ ($\tau=0$ for the plain mean gate)."
- **$\bar b$, $\bar\omega$, "transmission term"** in the Price paragraph.
- **"$c=0$"** in "the per-round tail change at $c=0$". Say "when the average candidate neither raises nor lowers the score ($z=0$)".
- **$\bar H$, "the loop's operating harm"**: define as "the typical cumulative harm of candidates the loop proposes".

Sign convention. $a$ and $b$ are gains (positive means lower error), Figure 1 plots error (positive means worse), and $H$ is harm. Add one sentence in Notation: "Effects are gains, positive when error falls; $H$ is a harm, positive when tail error rises."

Terminology to unify:
- The same group is called minority, tail, subpopulation, subgroup, fall-risk group, tail people and tail languages. Introduce "tail" in the Problem section ("we call this group the tail") and keep "minority" for the box only.
- One log has three names: "guard log" (H1, forecast), "drift log" (pseudocode, Figure 6) and "rejection log" (heading). Pick "guard log".
- Drift appears as "per-proposal drift", "per-round tail change", "per-edit drift" and "per-generation drift". Keep "drift $D$ per proposal" and "incumbent change $\hat\Delta_t$ per generation".
- "Drift", "panel", "guard log" and "child" are used before they are defined (box, H1 to H3, Key ideas). Add them to Key ideas, one sentence each.

### 1.5 Break up the four densest paragraphs, and put the simulation evidence in one labelled place

Several paragraphs each carry four to six ideas:
- **Statistical analysis** (304 words in one paragraph) mixes the primary outcome, effect size, the H1 model, the trajectory model, multiplicity, panel power, guarantee power, StaBLE certification and Global-MMLU power.
- **Estimating drift** (179 words) mixes the incumbent estimator, telescoping, the DGM lineage, unbiasedness, disattenuation and power.
- **Valid protective designs** (165 words of simulation results).
- **The forecast**: one 75-word sentence.
- **E6**: a 106-word bullet.

Split Statistical analysis into three paragraphs: (i) outcomes and models; (ii) power; (iii) testing the guarantee. Split the forecast sentence into a "what it computes" sentence and a "what it is fitted on" sentence.

Define the simulation labels once, where they first appear. The labels A1 to A4 are used eleven times and never explained:

> "Four preliminary simulations support the method (scripts in `output/idea-summaries-build/sim/`): A1 checks the closed form against Monte Carlo, A2 checks best-of-$K$, A3 runs the Fisher model, the guard estimator and the forecast over many generations, and A4 tests the guarantee."

---

## 2. Paragraph-by-paragraph edits

Numbering continues across sections. Sentence lengths are word counts.

### Title and box
1. Box: replace as in 1.1. "pre-defined minority" becomes "a group fixed in advance".
2. Box, ML contribution: "estimated online on a sealed guard set" contradicts "sealed test" usage. Use "estimated on a held-out guard set".

### The problem, in one concrete case
3. Para 1: "the task score averages normalized features" should say "features each rescaled to 0 to 1 between cohort bounds".
4. Para 1: "Qwen3-VL-8B [3]" should read "Qwen3-VL-8B, an 8-billion-parameter vision-language model [3]".
5. Para 1: "on development people" should add "(the people the loop scores while it edits)".
6. Para 2, 49-word sentence "A stronger low-pass filter ... protective step": split into three sentences, one per mechanism, and define "protective step (a step taken to stop a fall)".
7. Para 2: "passes the gate" uses "gate" before Key ideas defines it. Write "passes the acceptance test (the gate)".
8. Para 2, 48-word sentence "When the minority is a small share ... climbed": replace the vague "costs it a little and gains the majority slightly more" with numbers:
   > "With the tail at one person in eight, the mean gate accepts an edit that raises each tail person's error by 0.07 task-score units as long as it lowers each majority person's error by just over 0.01. After 50 generations (rounds of propose, score and keep) the mean can have fallen at every step while the tail's error climbed."
9. Para 2: move "The research question is whether ..." to its own closing paragraph (see 1.1). Move the lab-pilot sentence (43 words) before the Global-MMLU example or into H4. It currently ends the paragraph that should end on the question. "is not cited as selection drift" reads as an antithesis; write "so it motivates the mechanism split in H4".
10. Para 2: "These are hypotheses: the closest published evidence, a five-person pilot ..." should read "a five-person study of older adults" (that is what [7] is; "pilot" suggests the lab pilot).
11. Para 3, 52-word sentence: split after "poorly". Define "high-resource languages (languages with abundant web text)". Delete "which the mean gate accepts for the same reason it accepts the StaBLE clamp".
12. Para 3, last sentence (14,000 rows): delete. It is repeated in Data and splits and Second domain.
13. Figure 1: move it directly after para 2, which it illustrates. Caption: "stops gaining" applied to error is ambiguous (error "gaining" reads as rising). Write "fall-risk-group error (orange) reaches its lowest point at the first marker and passes its starting value at the second".

### Key ideas in plain terms
14. Harness: add "each edited copy is a child", since "child" is used next.
15. Acceptance rule (74 words): compress the GEPA and DGM mechanics to one sentence each; Baselines and Models repeat them. Add "weighted by how many instances each leads" to the GEPA clause (as in [6]).
16. Tail (43 words): explain "regression to the mean" in a clause: "(people chosen for an extreme score move back toward the average when remeasured, so any edit appears to help or hurt them)". "Tail" also means extreme values in statistics; add "here a group of people, not a range of values".
17. Edit effect: "These are an edit's true reductions ..." has no subject noun. Replace with "An edit's effect is its true reduction in mean loss relative to its parent: $a$ on the majority and $b$ on the tail. The loop sees only noisy estimates $\hat a$ and $\hat b$." Add the sign convention from 1.4.
18. Development, guard and sealed test people: add "In StaBLE the guard people also certify frozen checkpoints."
19. Correlated response: add the plain statement of the law (1.2).
20. Winner's curse and shrinkage: fine. Optionally merge the two halves into one sentence to save words.
21. Worst-group loss and CVaR: expand "CVaR (conditional value at risk)", and name "GroupDRO (group distributionally robust optimization), which minimizes worst-group loss [15]". Both acronyms appear later undefined.
22. Non-inferiority and bio-creep: "known as bio-creep in medical-device approval [16]" does not match the source, which calls it "biocreep in the drug development literature" and studies it for medical-device software. Write "a drift called bio-creep in drug development, which Feng and colleagues studied for approving medical-device software [16]".
23. Missing entries, each used before Method defines it: **tail drift** ("the expected change in tail error that one round of selection causes"), **panel** (H3: "a batch of single-step edits of one parent, all scored"), **guard log** (H1), **Fisher's geometric model** (H3) and **Price's equation** (Method). One sentence each.
24. Figure 2 caption: "drawn with $\rho=-0.4$" uses $\rho$ before Method defines it. Write "drawn with a correlation of $-0.4$ between majority and tail effects".

### What is known and what is missing
25. Narrative paragraph, 53-word first sentence: split after "the data". The paragraph restates the table; compress to two sentences (see cut list).
26. Table, the "X, not Y" antithesis in five rows (an LLM tic per STYLE). Rephrase:
    - "Items, not human subgroups; no rule or forecast" becomes "Measures items; no human subgroups, rule or forecast".
    - "Forgetting across distributions, not minority drift within one" becomes "Forgetting across task distributions; no subgroup within one".
    - "Tails over conditions, not people; ..." becomes "Tails over test conditions; no groups of people, mechanism or guarantee".
    - "One selection, not a chain of edits" becomes "A single selection; no chain of edits".
    - "Through retention or pseudo-labels, not edit selection" becomes "Mechanism is retention or pseudo-labelling; no edit selection".
27. Table, Hu and Tang row: the source title has a subtitle (see citations). The row is fine.
28. Gap paragraph, 80-word second sentence: it ends in a rhythmic triad ("the law converts it ..., a guard set estimates it ..., and it predicts ..."). Replace with:
    > "Hu and Tang already score every candidate on held-out items and estimate the winner's inflation [14], so the contribution here rests on one quantity, the covariance $C$ between an edit's tail effect and the score that selects it. A guard set estimates $C$ from candidates the loop already produces, and the law turns it into a forecast of drift and a prediction of which rules fail."
29. Gap paragraph, first sentence (45 words): "No work found in the literature sweep" becomes "No study we found".

### Hypotheses
30. Add the decisive-test sentence (1.1) and a pointer to the H-to-E table.
31. H1 (61 words): split. E3 lists four comparators and H1 names two. State that linear extrapolation and accepted-only are primary and the other two are secondary. Proposed:
    > "**H1, forecast.** A forecast of the sealed-test change in fall-risk error from generation 0 to 50, fitted to the guard log of generations 0 to 10 and frozen there, has lower paired absolute error across loops than linear extrapolation of the tail's guard-measured curve and than the same forecast fitted on accepted candidates alone. Its 90% interval covers the realized change in at least 80% of loops."
32. H2 (54 words): the first clause tests "the sign of tail drift" and the second "the selection term". Since $\mu_b\ne0$ lets total drift flip with noise, H2 must be about the selection term. Proposed:
    > "**H2, dose-response.** In Global-MMLU, raising the tail weight $\pi$ moves the selection term from negative to positive within one grid step of the $\pi$ at which $C$, estimated on held-out E1 edits, crosses zero, and changing the tail sample $n_B$ rescales it without changing its sign. The test runs first on frozen candidates, then in full loops."
33. H3 (88 words): delete "and either result is publishable" (salesy, and it refers to venues, which STYLE excludes). "Two rivals are registered" is enough. Split the test sentence.
34. H4: make it conditional: "If the mean gate harms the StaBLE tail, part of that harm survives ...".
35. H5 (42 words, three claims in one): split it as below. "keeps the share of majority gain that the design rule predicts" promises a prediction the design rule does not yet make (it gives $n_B$ for a pass probability, and "the exact version ... will be derived"). Either state the mapping (under tail-neutral edits, gain kept is about the pass probability at $H=0$) or drop the clause.
    > "**H5, price and validity.** (a) The cumulative per-group gate with fresh gate items breaches the margin $M$ in at most 5% of loops. (b) The share of majority gain it keeps matches the pass probability the design rule gives at each $n_B$. (c) When $C<0$, the rules order by tail drift as Baselines predicts."

### Method: notation and the law
36. Add the Method roadmap (1.3).
37. Notation para (125 words, about 15 symbols): split into two paragraphs (effects and their distribution; scores and noise).
38. Notation para: "The tail's weight in the objective, $\pi$, is its population share" contradicts E4, where $\pi$ is set by design. Write "$\pi$ is the tail's weight in the objective; by default it equals the tail's population share (about 0.14 for StaBLE's fall-risk group), and in Global-MMLU it is varied by design."
39. After the $D$ display: add the "In words" and selection-term sentences (1.2).
40. Para after the display, 41-word sentence "Noise enters the selection term only through $\sigma_S$ ...": split at the semicolon. Keep this as the single statement of noise invariance.
41. Same paragraph: "The condition is sufficient but not necessary, since ..." merges into the next paragraph's "found 255 cells with negative drift outside the sufficient condition"; one mention is enough.
42. A1/A2 paragraph (62-word sentence): define the A labels (1.5); replace "at $c=0$" with "when the average candidate neither raises nor lowers the score ($z=0$)".
43. Price paragraph (47 words): define $\bar b$ and $\bar\omega$ (means over candidates). "Plus a transmission term" is undefined, and for the quantity stated (the selection-weighted mean of $b$) the identity is exact without it. Either drop it or define it concretely, for example "a transmission term, the change in an edit's tail effect once later edits are stacked on it, which E8's reverts measure". The "How to read" row "inspect transmission" depends on this.
44. Figure 3 caption: "Below a curve, the selection term lowers the tail" is ambiguous ("lowers" could mean lowers error). The figure now says "harms", so write "harms the tail". "-0.143 suffices for equal spreads" should read "the selection term turns negative once $\rho<-0.143$ for equal spreads". "20 tail people in 160" is an invented cohort; see figure review.

### Method: when the sign changes
45. "conflict in the metric of the proposal distribution" should read "conflict once weighted by the covariance of proposed steps".
46. Add "to leading order in step size" to "For isotropic edits this happens inside the ball". A3 found the turn while $\rho$ (0.10) was still above $\rho^*$ ($-0.12$), because random steps cost the tail on average ($\mu_b<0$). The text already says "the turn comes where $D$ changes sign"; say explicitly that this is slightly before the seed enters the ball.
47. A3 paragraph: "a falling correlation alone predicts nothing" is aphoristic; write "the fall in $\rho$ did not by itself predict the turn". "in all but one small-range case" and "in a phenomenological variant, harm began while $\rho$ was still $+0.128$" use undefined terms; cut both or define "phenomenological variant" in a clause.
48. Figure 4 caption, 53-word sentence: split after "throughout". Add the leading-order caveat.

### Method: estimating drift
49. Heading "Estimating drift from the rejection log" should read "Estimating drift from the guard log" (one name, 1.4).
50. Define $\tau$ at its first use here.
51. Replace $K$ in $\hat D$ with $m$ (panel size, 200 in E1).
52. "they telescope to the guard-measured change since $h_0$" should read "they sum to the guard-measured change since $h_0$".
53. "reported raw and disattenuated with bootstrap noise variances" should read "reported raw and corrected for measurement noise (disattenuated) using bootstrap noise variances".
54. Last sentence (48 words): keep the attenuation example; move the power clause ("with 200 edits ... 0.13 to 0.29 $\sigma_a$") to Statistical analysis and delete the duplicate there.

### Method: the forecast
55. The 75-word sentence: split. Define "mean-field recursion" ("a recursion that replaces each generation's random outcome by its expected value"). Say how many candidates feed the fit: in a loop without a panel, generations 0 to 10 at $K=4$ give 44 candidates for six moment coefficients. Say whether E1 panels or pooling across seeds in a fold are used.
56. "With moments following a known function of $G_t$ (check A3) ... 20 of 20 simulated cells" (53 words): split after "cells".

### Method: design rule
57. Define $z_{1-\alpha_t}$ and $z_{p^\star}$ as standard normal quantiles. Define $\bar H$.
58. "in the units of check A4" is opaque; write "in the per-person harm units of simulation A4, where per-edit harm has spread 0.25".
59. Add one sentence tying the rule to H5(b): "Under tail-neutral edits the share of majority gain kept is close to this pass probability, which H5 tests."

### Method: valid protective designs
60. 58-word sentence "If each test is valid ... (check A4)": split after "(V2)". Rename G1/G2 as in 1.4.
61. "which needs a large tail and shows the proposer only accept or reject bits" is unclear. Write "which needs a large tail and leaks to the proposer only whether each candidate passed".
62. "Two designs stayed valid: fresh tail people for every test (realized error at most 0.0013)": add "under normal and heavy-tailed symmetric noise". In A4, fresh gating with harm confined to 10% of tail people breached at 0.58 with 5 people and 0.08 with 10. The next sentence's $0.9^{n_B}$ point implies this, but the "stayed valid" sentence overstates it.
63. Figure 5 caption: see figure review (an "ending" wording is left over from an earlier round).

### Method: instrumented loop
64. Pseudocode: rename `D`, `G`, `T` to `dev`, `guard`, `test` (they collide with $D$, $G_t$, $T$). Comment the certification line: `# guard people never fed the loop, so certification is valid`.
65. Figure 6 caption: define $\tau$, or say "the gate keeps the best candidate if its score clears the threshold". Mention that the guard set also certifies checkpoints in StaBLE.

### Experiments
66. Add the H-to-E table (1.3) at the top.
67. Shared evaluation protocol: "The collection's shared protocol applies" points outside the document (each proposal must stand alone). Write "Protocol:". Define "cross-fitting" in a clause ("rotating which block plays each role, so every person is tested once"). Delete "StaBLE normalization bounds are recomputed on development people", which Data and splits repeats.
68. Data and splits, StaBLE: "whose reference reach-window detector failed on monocular reconstructions" should read "whose reference method for finding the reach window failed on single-camera reconstructions".
69. Same paragraph, 53-word sentence "The primary tail is ...": split after "secondary tails". Define the questionnaire: "the CDC Stay Independent questionnaire (12 items; a score of 4 or more indicates fall risk)". Passive "the count among usable participants is confirmed before registration" should read "we confirm the count among usable participants before registration". State the resulting StaBLE $\pi$ (about 0.14).
70. Data and splits, Global-MMLU: "a published resource taxonomy" is unnamed and uncited. Name it and cite it after verification (the Global-MMLU paper itself may group languages by resource level; check before citing).
71. Figure 7 caption: fine. The figure's subtitle says "stratified by fall-risk status" while the text says "stratified by fall-risk group and age" (see figure review).
72. Models and tools: "OpenSim center-of-mass computation" is used without definition or citation. Add "OpenSim, musculoskeletal modelling software [Delp et al. 2007]" (verified in `biomech-facts.md`). Gloss "Qwen3-Coder-480B-A35B-Instruct" as "(a mixture-of-experts coding model with 480 billion parameters, 35 billion active)". Split the 46-word sentence after "per generation".
73. Baselines, item 7: "the aACP-BAC policy" should read "the automatic algorithmic change protocol of Feng and colleagues, which combines alpha-investing with group-sequential and gatekeeping tests to bound bad approvals (aACP-BAC), applied to tail loss". Say which population it is applied to.
74. Baselines, item 9 in StaBLE is "the mean gate plus post-hoc certification": certification does not change which edits are accepted (A4: 46.8 accepted edits, the same as no gate). E2 nevertheless runs rule 9 as 10 separate StaBLE loops. Reuse the mean-gate L1 loops, or say what differs. This saves about 4.5 billion tokens.
75. Baselines prediction paragraph, 66-word sentence: split after "covariance". "rescoring corrects the mean's optimism but not the covariance" is an antithesis; write "rescoring removes the mean's optimism and leaves $C$ unchanged".
76. Metrics: "calibration slope" should read "calibration slope (the slope of reference on predicted score)".
77. E1: the parenthetical "(in Global-MMLU on 512 majority and 512 tail development items, so that E4 can resample them)" goes to Data and splits.
78. E3: mark which comparators are primary (see 31).
79. E4: add held-out estimation of the moments (see W3 below): "moments are fitted on half the E1 edits and predictions tested on the other half".
80. E5: "tool-route weight" is undefined; write "tool-route weight (the share of clips routed to RTMPose)".
81. E6 (106 words): split into a design sentence, a reference sentence and a comparison sentence.
82. Figure 8 caption: optionally gloss "per-item noise variance 64" as "so the majority score's noise SD is half the spread of true majority effects".
83. Ablations, trace composition: "Proposer traces" should read "Proposer traces (the logged inputs, tool calls and outputs shown to the proposer)".
84. Statistical analysis: restructure into three paragraphs (1.5).
    - Define "Clopper-Pearson intervals (exact binomial confidence intervals)" and "a one-sided Hoeffding bound (a finite-sample bound for bounded variables)".
    - "cannot certify a margin below about 1.1 task-score units" should add "even when every observed difference is zero".
    - "the StaBLE score's standard deviation of 0.12" is the composite score's SD across people, while the outcome is a task-score error. State the per-person task-error SD computed on development people, or say why the composite SD is the right scale.
85. Second domain: merge with Risks "Small StaBLE tails" (cut list).

### How to read the results, compute, risks, learning
86. How to read: merge the rows "Drift changes sign at the predicted $\pi$" and "far from the predicted $\pi$". Add two rows:
    - "$\hat C\ge0$ in the generation-0 panel": nothing to protect against in this domain; move effort to a tail with conflicting edits.
    - "Forecast works in Global-MMLU but fails in StaBLE": the guard sample is too small; report the minimum tail size.
87. Compute, Global-MMLU bullet: "200 candidates on 630 items" does not say what 630 is made of (dev majority, dev tail, guard). Derive it in a clause.
88. Compute, tool-cache bullet: "872,000 frames" implies 60 fps; say so.
89. Risks, "Leakage from gate to proposer": passive "Logs are audited" should read "an automated check scans every proposer prompt for guard and test identifiers".
90. Risks, "Scope": delete the comparison with proposal 05. The document should stand alone.
91. Risks, "Moments may not extrapolate": duplicates the How-to-read row; delete.
92. Where to learn more: the UvA "Guide 2" bullet is only loosely tied to this proposal (seeds); drop it or shorten every clause to about 10 words.

**Total edits listed: 92.**

---

## 3. Cut list (target: at most 5,900 words by `audit_doc.py` after the clarity additions)

The current count is 6,187. The additions in sections 1 and 2 come to about 440 words: box rewrite about 0, closing question paragraph +20, concrete example +25, plain law +45, Key-ideas entries +45, selection term +40, roadmap +35, H-to-E table +90, symbol and acronym definitions +80, StaBLE $\pi$ +12, H5 +15, outcome ordering +30. The cuts below remove about 770, which gives an estimated **5,850**.

| # | Passage | Action | Words saved |
|---|---|---|---|
| C1 | Problem para 3, "With about 14,000 test rows per language, Global-MMLU lets ... be set by design." | delete (in Data and splits and Second domain) | 24 |
| C2 | Problem para 3, "which the mean gate accepts for the same reason it accepts the StaBLE clamp" | delete | 14 |
| C3 | Problem para 2, lab-pilot sentence | compress to "A lab pilot (internal account), in which fine-tuning cut average task error from 0.120 to 0.100 while raising error at the extremes, points to shrinkage, which H4 separates from selection." | 12 |
| C4 | Key ideas, Acceptance rule: DGM and GEPA mechanics | one clause each (Baselines and Models repeat them) | 20 |
| C5 | Key ideas, Winner's curse and shrinkage | merge into two sentences | 10 |
| C6 | What is known, narrative paragraph (106 words) | replace with "Agent and prompt-optimization studies show aggregate gains hiding losses on items [18], [19] and earlier capabilities [20], and keep-if-better acting as selection under noise [14]; outside agents, mean-driven training widens disparities [21], [22], [23] and clinical models fail on rare subsets [24]. Tail-protective selection [25], [26], [27], [16] and the correlated response [12], [10], [11] are established, so no new formula is claimed." | 50 |
| C7 | Table rows Hashimoto/Zhu, Heckman/Lande/Price and Yu | delete (all are covered in the narrative, and the first and third carry antitheses) | 55 |
| C8 | Gap paragraph (125 words) | replace as in edit 28 | 45 |
| C9 | H3, "and either result is publishable" plus a shorter test sentence | delete and compress | 15 |
| C10 | Para after $D$, "The condition is sufficient but not necessary, since ..." | merge with the 255-cells clause | 20 |
| C11 | A1/A2 paragraph, inline path and repeated "preliminary simulation in this project" | replace with the label definition at first use (1.5) | 10 |
| C12 | Price paragraph | compress to about 30 words | 25 |
| C13 | Figure 3 caption, "and evaluation noise does not move the curves" | delete (stated once in text) | 8 |
| C14 | A3 Fisher paragraph, "in all but one small-range case" and the phenomenological-variant clause | delete | 20 |
| C15 | Figure 4 caption (73 words) | to about 45 | 28 |
| C16 | Estimating drift, power clause | keep only in Statistical analysis | 25 |
| C17 | The forecast | compress while splitting | 25 |
| C18 | Design rule, "The exact version ... will be derived and tested in Global-MMLU." | shorten | 8 |
| C19 | Valid designs, "In StaBLE it uses the guard block ... measures a harness." | keep once in Data and splits (Figure 7 caption already says it) | 15 |
| C20 | Figure 5 caption (93 words) | to about 60 | 33 |
| C21 | Figure 6 caption (64 words) | to about 45 | 19 |
| C22 | Shared evaluation protocol (82 words) | to about 50 | 32 |
| C23 | Data and splits StaBLE, Y-Balance aside and the skipped-trials sentence | compress | 25 |
| C24 | Core experiments, E1 parenthetical and E6 | move and compress | 20 |
| C25 | Statistical analysis, duplicated panel-power clause and "Global-MMLU's large test pool gives the better-powered replication" | delete (the H-to-E table carries the domain) | 30 |
| C26 | Second domain plus Risks "Small StaBLE tails" | merge into one 25-word bullet | 30 |
| C27 | Risks, Scope, proposal-05 comparison | delete | 18 |
| C28 | Where to learn more | drop the UvA bullet or shorten every clause | 30 |
| C29 | How to read, rows 3 and 4 | merge | 15 |
| C30 | Baselines list items | trim each to name, one clause and citation | 20 |
| C31 | Key ideas, Alpha-spending | compress | 15 |
| C32 | Models, "all cached per video and configuration" | delete (Compute says it) | 6 |
| C33 | Figure 2 caption | compress | 10 |
| C34 | Figure 7 caption | compress (the legend carries the roles) | 12 |
| C35 | Global-MMLU split, "verified before use because the dataset card gives no tier" | replace with the named, cited taxonomy | 10 |
| C36 | Risks, "Moments may not extrapolate" | delete (duplicates How-to-read) | 20 |
| | **Total** | | **about 770** |

---

## 4. Scientific review (ICML format)

### Summary
The proposal asks whether accept-if-better self-improvement loops for LLM agent harnesses (GEPA-style prompt and route optimization, Meta-Harness-style code optimization, DGM-style archives) predictably harm a small group fixed in advance. The groups are StaBLE participants at risk of falling for a monocular-video balance-scoring agent, and low-resource languages for a Global-MMLU question-answering agent with a translation tool.

It models candidate edits' true effects on majority and tail as bivariate Gaussian with independent evaluation noise. It then derives, from classical selection theory (Heckman, Lande and Arnold, Price), the expected tail change per proposal under threshold and best-of-$K$ selection. The sign of the selection term depends only on $C=\mathrm{Cov}(b,S)$, which noise cannot flip. Every candidate is scored on a guard set hidden from the loop, which gives unbiased estimates of $C$ and of drift. These feed a forecast frozen at generation 10 and checked at generation 50 on sealed test people. A Fisher geometric model predicts when the sign turns.

Protection is studied through a cumulative per-group non-inferiority gate against the seed, with alpha spending and fresh gate items, and through post-hoc checkpoint certification, with a sample-size rule. Simulations show that reuse of tail people and per-step comparison break the guarantee. Experiments cover panels, 135 StaBLE and 210 Global-MMLU loops, a dose-response grid over tail weight and tail sample size with a frozen-candidate arm, a timing test, a shrinkage-versus-selection split and tool attribution, at about 2,500 H100-hours.

### Strengths
1. **An important, concrete question that is open.** Subgroup trajectories under accept-if-better agent loops are unstudied, the clinical stakes are real, and the second domain is chosen so that the tail's share and sample size can be set by design.
2. **Honest scoping of novelty.** The formula is credited to classical theory, Hu and Tang's instrumentation is acknowledged, and the claim is narrowed to measuring and using $C$.
3. **Clean separation of objective weight $\pi$ from evaluation size $n_B$.** This makes the dose-response design possible and exposes the "noise rescales, never flips, the selection term" prediction.
4. **Sound estimator design.** Guard noise is independent of the gate's noise, so $\mathrm{Cov}(\hat b_{\text{guard}},S_{\text{dev}})$ is unbiased for $C$ without Gaussianity. Increments telescope along the lineage as a log check. The accepted-only ablation isolates what rejected edits add.
5. **Careful validity analysis of protective rules.** It covers holdout reuse, bio-creep under per-step comparison, skewed harms and the gap between certifying only the deployed checkpoint and controlling any-parent breaches. StaBLE certification is honestly labelled exploratory, with a stated detectable margin.
6. **Registered rival timing hypotheses, a frozen-candidate arm that isolates selection, a shrinkage-neutral mechanism test, and a results table that includes the null.** Compute arithmetic is traceable. I re-derived the token totals, the 2,009 H100-hours, Figure 8's cells, $\rho^*$, the design-rule example (97), the Hoeffding margin (1.1) and the binomial powers (0.97 and 0.62), and all match.

### Weaknesses, each with a fix

**W1. H1, the headline hypothesis, is underpowered in StaBLE, and no power analysis covers it.**
- Each guard block and each test block holds about five fall-risk people.
- Each $\hat b_{\text{guard}}$ is therefore a mean over about five people, and each fold's realized target change is a mean over about five people shared by all 15 loops in that fold. The effective sample for the target is about 25 people.
- In a loop without a panel, the forecast fits six moment coefficients from 44 candidates.
- The only power statement concerns 200-edit panels at $s_b\le2\sigma_b$, and with five tail people $s_b/\sigma_b$ may be far larger.

*Fix:*
- Make Global-MMLU the primary venue for H1 and StaBLE a registered secondary.
- Measure $v$ and $\sigma_b$ on the generation-0 StaBLE panel and register a go/no-go power threshold before the loops run.
- Fit moments hierarchically across seeds within a fold, using the E1 panels.
- Report how many usable participants are aged 70 and above; if that tail is larger, consider it for the StaBLE forecast.

**W2. The registered primary outcome is not the claim in the box.**
- The StaBLE primary outcome is the size of the mean-gate drift.
- The box's falsifiers are forecast skill (H1) and the sign flip (H2).
- A reader cannot tell which result decides the proposal.

*Fix:* Register the outcomes in a fixed sequence at $\alpha=0.05$:
1. H2 sign agreement in the Global-MMLU rescoring arm;
2. H1 forecast skill, Global-MMLU then StaBLE;
3. StaBLE drift.

The proposal already uses fixed-sequence testing elsewhere.

**W3. E4's rescoring arm risks circularity.**
- The moments that predict each cell come from the same 200 frozen E1 edits, and from overlapping development items, whose re-selection produces the observed drift.
- Linear covariance and covariance with an acceptance indicator share sign under almost any monotone relation, so agreement is close to guaranteed.

*Fix:*
- Fit $C(\pi)$ on a random half of the edits, or on other lineages, and test the selection term's sign on the held-out half.
- Register the agreement metric: the number of the 12 cells with the correct sign, plus the slope of observed against predicted.

**W4. H2's measured quantity is not defined.**
- "The selection term" is not directly observed, and the text never says how it is computed from data.

*Fix:* Define it as $\widehat{\mathrm{Cov}}(\hat b_{\text{guard}},\mathbf{1}\{S>\tau\})=\hat D-\hat\mu_b\cdot\widehat{P}(\text{accept})$. This is the Gaussian law's $(C/\sigma_S)\phi(z)$ and Price's $\mathrm{Cov}(\omega,b)$. Restate H2 in those terms (edit 32).

**W5. H5(b) promises a prediction the method does not yet make.**
- The design rule gives $n_B$ for a pass probability, not a share of majority gain, and the exact version is deferred.

*Fix:*
- State the first-order mapping: under tail-neutral edits, gain kept is about the pass probability at $H=0$.
- Check the mapping against A4, where fresh gating kept 9%, 31% and 57% of majority gain at 5, 10 and 20 people. Otherwise drop the clause.

**W6. The timing geometry is leading-order, but the text and Figure 4 present it as exact.**
- The ball is where $C<0$ to first order in step size.
- In A3 the inverted U peaked while $\rho>\rho^*$, because $\mu_b<0$ at second order, so the turn precedes entry into the ball.

*Fix:*
- Say "to leading order in step size" in the text and in the Figure 4 caption.
- Have E5 and the open-ended regime calls predict the sign of $D$, not ball membership.
- E5's three-parameter harness tests the geometry on real cached outputs, not LLM-proposed edits. Say so, so that H3's external validity is not overstated.

**W7. The Price form carries an undefined "transmission term".**
- For the stated quantity, the selection-weighted mean of $b$, the identity is exact without it, yet the How-to-read table relies on "inspect transmission".

*Fix:* Define transmission as the non-additivity of stacked edits, measured by E8's single reverts, or remove both mentions.

**W8. Global-MMLU's tail and the conflict premise are unspecified.**
- The taxonomy that defines the tail is unnamed.
- A negative $\rho$ for translation-routing edits is a hypothesis. If $\rho\ge0$, $C>0$ at every $\pi$ in the grid, H2 predicts no flip, and E4 loses most of its power to falsify.

*Fix:*
- Name and cite the taxonomy.
- Add a go/no-go on the generation-0 Global-MMLU panel: if $\hat\rho\ge0$, seed the proposer with routing edits known to conflict (forced English translation), or choose tail languages the translator handles poorly, before running E4.

**W9. Smaller issues.**
- The effect size of interest uses the composite score SD for a task-error outcome (fix in edit 84).
- The "fresh people stayed valid" claim needs its noise qualifier (edit 62).
- Rule 9 in StaBLE duplicates the mean-gate loops (edit 74).
- Pooling L1 to L3 in the StaBLE primary outcome mixes edit distributions with different moments. Add family as a fixed effect (already in the trajectory model) and report per family.

### Questions for the authors
1. What noise ratio $s_b/\sigma_b$ do you expect for five guard fall-risk people? Is any estimate available from the pilot's per-person error variance?
2. How exactly is the selection term estimated in E4, and which edits and items are held out from the moment fit?
3. Which taxonomy defines low-resource languages, and how many languages and items fall in the tail?
4. In loops where the mean gate accepts few edits ($z\ll0$), drift and the forecast are both near zero. Are such loops excluded from H1, or do they inflate its apparent skill?
5. Does the StaBLE forecast for loops without E1 panels use only 44 candidates? If panels are shared across seeds within a fold, how is the dependence handled?
6. H3's open-ended test has one panel lineage per fold (five StaBLE, five Global-MMLU). What is the minimum agreement rate that counts as support?
7. What does rule 9 change in StaBLE beyond post-hoc certification of the mean-gate lineage?
8. In E6, is the "accepted parent" breach judged on 1,000 sealed tail items per parent? How is the multiplicity across about 25 parents per loop handled in the any-parent event?

### Scores
- Soundness: **3/4** (the derivations are correct and the validity analysis is careful; H1's StaBLE power and E4's circularity are open)
- Presentation: **2/4** (complete and well sourced, but dense, with overloaded notation, an undefined central term, many 50 to 80 word sentences and no hypothesis-to-experiment map)
- Contribution: **3/4** (a new and useful question for agent loops, with a measurable lever and a design rule; the theory is classical by design)
- Overall: **6/10** (accept as a research plan once W1 to W4 are addressed)
- Confidence: **4/5**

---

## 5. Citation spot-check (8 most load-bearing, each link fetched once)

| Ref | Link fetched | Claim in the proposal | Finding |
|---|---|---|---|
| [1] StaBLE, Heigold et al. | doi.org/10.64898/2026.09.16.750744 (bioRxiv landing page), plus the full text at PMC13621976 | 180 people aged 18 to 87, 18 tasks; 25 of 180 at fall risk (CDC Stay Independent 4 or more); score SD 0.12; 98 trials across 24 participants scored 0; 3 imputed | **Matches.** The landing page confirms 180 participants and 18 tasks; the full text confirms ages 18 to 87, n = 25 at fall risk with the 12-question Stay Independent tool at 4 or more, SD 0.12, 98 unperformed trials across 24 participants assigned zero, and 3 imputed trials. Usage note: 0.12 is the composite StaBLE score SD, used here to scale a task-error outcome (edit 84). |
| [6] GEPA, Agrawal et al. | arxiv.org/abs/2507.19457 and its HTML | Gates on a minibatch mean, then samples parents among candidates that lead on at least one instance; ICLR 2026 | **Matches.** ICLR 2026 (Oral) is confirmed. The paper evaluates on a minibatch and admits only if improved; parents are sampled among non-dominated candidates "weighting probabilities by how many tasks each candidate leads". Suggest adding the weighting clause. |
| [8] Global-MMLU, Singh et al. | arxiv.org/abs/2412.03304 | 42 languages; about 14,000 test rows per language | **Partial.** 42 languages is confirmed. The per-language row count is not on the arXiv page; it comes from the Hugging Face dataset card (recorded in `06-tails-literature.md`). Cite the dataset card for the 14,000 figure. The source gives no resource tiers, as the proposal says, so the tail taxonomy needs its own verified citation. |
| [14] Hu and Tang | arxiv.org/abs/2610.09239 | Keep-if-better is selection under noise; fresh rescoring removes the mean bias; instrumented runs score every candidate on held-out items; within-generation inflation estimates | **Matches, with one title mismatch.** The full title is "The Winner's Curse in LLM Self-Improvement Loops: Selection Noise, Lock-in, and Acceptance Rules"; the reference omits the subtitle. The abstract confirms selection under noise, that rescoring on 64 unselected items removes the average bias, and that every candidate is scored on 600 held-out items in the Qwen runs. The inflation estimate is described as a model with a pilot prior matching average overstatement; confirm the exact "from within-generation logs" wording against Sections 4 and 6 before keeping it. |
| [16] Feng, Emerson and Simon | arxiv.org/abs/1912.12413 | Bio-creep "in medical-device approval"; alpha-investing control; aACP-BAC baseline | **Wording mismatch.** The source says bio-creep is the term "in the drug development literature", applied there to medical-device software; fix edit 22. The policies (aACP-BAC, aACP-BABR) "combine alpha-investing, group-sequential, and gate-keeping methods", so "alpha-investing approval" undersells them. Expand aACP (automatic algorithmic change protocol) and BAC (bad approval count) (edit 73). |
| [18] Mitra and Mahmud | arxiv.org/abs/2610.19084 | Churn exceeded net change at least fivefold in five of nine configurations | **Exact match** ("in five of nine configurations, churn was at least five times the absolute net change"). |
| [19] SAGE, Wang et al. | arxiv.org/abs/2609.36043 | A per-item paired test cut regressions in 19 of 20 settings | **Matches** (per-item paired comparison with a one-sided paired test; regression rate lower in 19 of 20 settings; no cumulative or group guarantee in the abstract). |
| [28] Wei et al., Self-Evolving Agent Harness | arxiv.org/abs/2610.18813 | Retention bounds and fresh-data admission; average performance only | **Matches** ("a retention bound conditional on historical regression budgets"; "a high-probability admission rule using fresh, independent validation data"). The abstract does not mention subgroups, so "average performance only" is an inference from the abstract; acceptable, but "no subgroup guarantee stated" is safer. |
| (extra) [7] Graf et al. | frontiersin.org, doi 10.3389/fspor.2026.1902010 | Five-person study; more missed events under perturbation, not significant | **Matches** (five older adults; recall fell, "None of the comparisons reached statistical significance"). Call it a "five-person study" rather than a "pilot" (edit 10). |

No fabricated or broken links were found among the checked references.

---

## 6. Figure review

**Figure 1, concept-mean-vs-tail.** Ship, with a caption fix.
- **One point:** yes; the mean falls while the tail turns back.
- **Caption:** explains what to look at, but "fall-risk-group error (orange) stops gaining at the first marked point" is ambiguous when applied to error.
- **Matches the text:** yes.
- **Change:** use the caption wording in edit 13, and move the figure directly after the StaBLE paragraph it illustrates (it now follows the Global-MMLU example).

**Figure 2, edit-effect-scatter.** Ship, with a caption fix.
- **One point:** yes; many accepted edits harm the tail. The acceptance line (slope $-(1-\pi)/\pi=-7$) is drawn correctly.
- **Caption and text:** the caption uses $\rho$ before Method defines it.
- **Change:** write "a correlation of $-0.4$ between majority and tail effects" in the caption. Optionally retitle to the takeaway, "The mean rule accepts many edits that harm the tail", to match Figure 1's takeaway-style title.

**Figure 3, drift-sign-map.** Ship, with a label and caption fix.
- **One point:** yes; the threshold correlation depends on tail share and spread ratio. The values match the formula.
- **Mismatches:** the guide-line label "π = 0.125 (20 tail people in 160)" invents a cohort unrelated to StaBLE (171 people, about 25 at fall risk, about 15 in a development set of 103, so $\pi\approx0.14$). The caption's "the selection term lowers the tail" is ambiguous where the figure says "harms".
- **Change:** relabel the guide "π = 0.125 (one in eight)", or draw StaBLE's $\pi\approx0.14$. Use "harms the tail" and "the selection term turns negative once ρ < −0.143" in the caption.

**Figure 4, timing-regimes-geometry.** Ship, with a caption fix.
- **One point:** yes; the three regimes are set by the seed's position relative to the ball, and the diamond pairing works.
- **Overstatement:** the ball label and caption state "inside the ball, expected tail gain per generation is negative" as exact. It holds to leading order in step size, and A3 found the turn before ball entry because $\mu_b<0$.
- **Change:** add "to leading order in step size" to the caption, with one clause that the exact turn comes slightly earlier. Split the 53-word caption sentence.

**Figure 5, guarantee-validity-and-price (round-3 fix, not re-reviewed by Codex).** Ship, with caption fixes.
- **Round-3 changes:** they work. Per-row event lines make the different breach events visible. "per-step gate vs parent" no longer reads as a per-step rate. The right axis now extends past 20, so the dodged square no longer suggests $n>20$. No overlaps, text crossings or off-canvas marks appear in the PNG.
- **Remaining mismatch:** the caption still says "of a harness ending more than M worse than the seed on the tail", which contradicts the figure's "breach: any accepted parent". Write "of an accepted harness being more than M worse than the seed on the tail (any accepted parent for the gates, the deployed checkpoint for certification)".
- **Minor:**
  - The per-step row is a dot while the subtitle says "each bar: range over 5 to 20"; add "(dot: 1.0 at every size)" to the caption.
  - The right axis title "tail people per gate test" does not fit certification, which tests checkpoints; "tail people per test" covers both.
  - The fresh-people bar is valid only under normal noise (the caption says so); the text needs the matching qualifier (edit 62).

**Figure 6, instrumented-loop (round-3 fix, not re-reviewed by Codex).** Ship, with text fixes.
- **Round-3 changes:** they work. The forecast box reads "tail change from generation 0 to 50, frozen at generation 10", matching the test box, and the checkpoint arrow is labelled "checkpoints, generations 0 to 50". The arrows start and end on box edges, none cross text, and the compare node makes clear the forecast is not a test input.
- **Remaining:**
  - "keep the best candidate if S > τ" shows $\tau$, which the text never defines (edit 50).
  - The "Dev people" box is really the gate; "Gate on dev people" would make the keep-or-reject arrow self-explanatory (optional).
  - The guard set's second role in StaBLE (certifying frozen checkpoints) is absent from the figure and its caption, though the pseudocode and Figure 7 caption mention it. Add a clause to the Figure 6 caption.

**Figure 7, stable-person-splits.** Ship, with a one-word fix.
- **One point:** yes; the rotation is obvious. The counts (34, 34, 103) match the text.
- **Change:** the subtitle says "stratified by fall-risk status" while the text says "stratified by fall-risk group and age"; make them agree.

**Figure 8, dose-response-design.** Ship.
- **One point:** yes; tail share sets the sign and the number of tail items changes only the size. I recomputed the cells from the stated assumptions ($\rho=-0.3$, equal spreads, zero means, $v=64$, $n_A=256$): for example $-0.089$ at $\pi=0.05$, $+0.083$ and $+0.123$ at $\pi=0.4$ for $n_B$ of 16 and 256, and a crossing at $0.3/1.3=0.23$. All match.
- **Optional:** gloss the noise variance in the caption (edit 82). Once W3 is adopted, the caption should say the real E4 predictions use held-out moments.
