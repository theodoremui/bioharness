# Proposal 05: final independent review

Reviewer scope: `docs/idea-summaries/05-what-makes-a-harness-improvable.md` read in full; all eight SVGs rendered with `render.py` into `output/idea-summaries-build/png/05/` and inspected; `lint_svg.py` run (one real warning: `two-tier-design.svg` heavy text, 128 words); `audit_doc.py` run (6,299 prose words, 8 figures, 33 references, no dashes, no banned words). The resolutions table was read first; settled points (missing-score rule, sealed cohort kept out of the gate, scalar H3 forecast with base means removed, HGM pooling of own evaluations, H2 moved to main effects, development-event $B^{\star}$, external-trace control, compute rows) are not re-raised except where the fix itself has a problem.

**One-read test.** After one read, a reader can state the research question (it is in the box and repeated in bold). They will struggle with the other three items. Why the answer is open is spread across a 150-word gap paragraph. No sentence names the decisive experiment; the reader has to assemble it from Hypotheses, Method and Core experiments. The box gives three falsifiers of different parts with no order of priority. And the Hypotheses section uses about fifteen terms that are defined only later.

---

## 1. The five changes that would most improve readability and conceptual clarity

### 1.1 Define the design vocabulary before the Hypotheses, not after

**Problem.** The Hypotheses section (lines 74 to 82) uses these before they are defined: *cell 1* and *cell 8*, *factor*, *degraded* and *structured level*, *O*, *P*, *tier 1*, *tier 2*, *selection-split error*, *the 30B proposer*, *base*, *configuration*, *300-edit profile*, *clade estimate*, *development-event profile*, *evaluation-equivalent*, *accept-if-better loop*, *seeded defects*, *physical naming*, *archive nodes*, *static code features*. Factors appear only in Method (line 88), splits only in Experiments (line 179), bases only at line 189. Key ideas defines *sealed test people* but not the development and selection splits, and it never defines **trace**, which STYLE lists by name as a term to define.

**Fix.** End Key ideas with two short paragraphs, and keep only the level details in Method's "Structural factors".

> **Trace.** A text record that a harness writes while it runs, beyond its outputs: here, per-stage summaries such as keypoint-confidence quantiles, the center-of-mass range and whether a reach window was found. The optimizer passes the trace to the proposer together with the score errors.
>
> **The design in brief.** A *base* is one independently written harness for one StaBLE task family; there are 20. A *variant* is a base rewritten, without changing any output, along five factors, each at a degraded or a structured level: modularity (M), observability (O), named parameters (P), warning-only checks (T) and naming (N). A *cell* is one combination of M, O, P and T levels in an eight-cell half fraction: cell 1 has all four degraded, cell 8 all four structured. People are split into *development* people (the proposer sees their errors and traces), *selection* people (they define edit success and pick each loop's final candidate) and *sealed* people (scored once per loop, after search ends). *Tier 1* measures one-step edit profiles for every cell, base and proposer (a 30B and a 480B open model and one frontier API model). *Tier 2* runs full loops with the 30B proposer on 96 *configurations*: three bases times all 32 settings of the five factors.

Net words: about +170, offset by deleting the Hypotheses preamble (line 74, 25 words) and the "Length-matched placebo and sealed test people" paragraph's sealed half (25 words).

### 1.2 State the question, the decisive experiment and the falsifier once, and make the box carry all three

**Problem.** The question appears three times (box line 3, bold paragraph line 17, Figure 1 caption). The box's ML contribution line (53 words) lists four products in undefined terms ("single-edit success profile", "clade estimate", "structural prior", "parent selection before a candidate has descendants"). No sentence anywhere says "the decisive experiment is ...". The falsifier gives three disjoint conditions. Its first clause ("every structural effect falls inside a pre-registered equivalence margin for every proposer") cannot be reached at the planned sample size (see Weakness 1 in section 4). A conceptual gap sits underneath: the headline question is about how far a *loop* improves a harness. Tier 2's 32-setting full factorial (480 against 480 loops per main effect, detectable effect about $0.18\sigma$ by line 227) answers that question directly. Yet it has no numbered hypothesis and is used only to validate H3's forecast.

**Fix.** Replace the box's last two lines with:

> **ML contribution.** The decisive experiment rewrites 20 balance-scoring harnesses without changing any output, crosses five code properties with three LLM proposers in 28,800 one-step edits, and checks the result against 960 full loops. It yields a causal estimate of each property's effect on improvability at fixed behavior and length, a one-step forecast of long-run gain, a code-based prior for choosing parents, and a break-even budget for refactoring first.
>
> **What would prove it wrong.** At matched length, no factor changes the one-step success rate (H1) or the loops' sealed-test gain (H1b) for any proposer, or the one-step forecast predicts loop gains no better than HGM's descendant-count estimate at equal cost (H3).

Add **H1b** after H1: "*In tier-2 loops, the O main effect on the final candidate's sealed-test MAE reduction is positive.* Test: paired mixed model over 480 against 480 loops, minimum detectable effect about $0.18\sigma$." Rewrite "Why it matters" so that it states the consequence: "...rest on the untested premise that modular, logged code is easier to improve. If it is, a loop should restructure before it searches and rank newborn candidates by their code." Delete the bold "The research question." paragraph's first sentence (it repeats the box) and keep its two follow-up questions as the signpost into the coding-agent paragraph.

### 1.3 Remove overloaded symbols and pick one word for the property being measured

**Problem.** Eight symbols carry two meanings, and the property itself has three names: *improvability* (title, box, line 17), *evolvability* (Key ideas, with $E_B$) and *metaproductivity* (HGM's term). $E_B(h)$ is defined at line 39 and never used again. Its estimate is the H3 outcome, but the text does not say so.

| Symbol | First meaning | Second meaning | Proposed change |
|---|---|---|---|
| $B$ | harness "Version B" (lines 15, 23, figs 1 and 2) | budget $B$ (lines 23, 37, 124 onward) | Call the staged version **S** in text and figs 1 and 2 ("Harness S: typed stages") |
| $\delta$ | success threshold 0.01 (lines 43, 114) | interaction coefficients $\delta_{f,q}$ (line 221) | Rename coefficients $\theta_{f,q}$ |
| $\sigma$ | logistic function (line 144) | seed-to-seed spread (line 227) | Write the spread as $\sigma_{\text{loop}}$ |
| $w$ | prior weights $w$ (line 142) | session intercept $w_{k(e)}$ (line 221) | Intercepts $u^{\text{base}}_b$, $u^{\text{cell}}_{bc}$, $u^{\text{sess}}_k$ |
| $v$ | valid rate (line 114) | base-by-cell intercept $v_{b(e),c(e)}$ | as above |
| $x$ | static code features $x_a$ (line 140) | factor codes $x_{fe}$ (line 221) | Factor codes $c_{fe}$ |
| $b$ | base index $b$, $b(e)$, $L_b$ | refactor cost $b_R$ | Refactor cost $C_R$ |
| $n$ | edits per profile (line 114) | loops per arm (line 227) | $n_{\text{loop}}$ for loops |
| $J$ | sealed-test MAE (line 37) | $J_{sel}$ (line 114) | Define once: "$J_{dev}$, $J_{sel}$ and $J_{test}$ are the task-averaged MAE on each split; $J$ alone means $J_{test}$" |
| $f_h$, $\omega$, $\pi(h,q)$ | each used once | | Drop $f_h$ ("if $h$ and $h'$ compute the same function"); keep $\omega$; drop $\pi$ |
| CMP | in $\widehat{\mathrm{CMP}}(a)$ (line 142) | never expanded | "estimated clade metaproductivity" |

In Key ideas, retitle **Evolvability** as **Improvability** and add one clause: "biologists call the analogous property evolvability; HGM's metaproductivity is an estimate of the same idea from a node's descendants". After H3's outcome, add "(an estimate of $E_{100}(h)$)" so the definition gets used.

### 1.4 Shorten each hypothesis to one plain sentence and map it to its experiment

**Problem.** Six of the seven hypotheses are single sentences of 42 to 55 words. Each packs the claim, the threshold, the conditions and the test into one sentence. H4 holds three claims in a triad with broken parallelism ("successful edits touch fewer lines, break fewer previously correct examples, and fewer candidates are invalid"). The reader cannot see which Core experiment tests which hypothesis until line 202. Line 223 says "H2 to H7 each have one pre-registered primary test", but H2, H3 and H5 each state two tests and H4 three.

**Fix.** One claim per hypothesis, then a *Test* line that names the experiment number and the falsifying result. Examples:

> 1. **H1, structure raises the one-step success rate.** With the 30B proposer and at matched length, cell 8's success rate exceeds cell 1's, and the O or P main effect is positive. *Test (Experiment 2):* logistic mixed model, Holm across the five main effects. *Falsified if* both intervals include zero.
> 3. **H3, one-step profiles forecast loops.** Within each base, the forecast $\hat F=1-(1-sg)^{100}$ from a 300-edit profile correlates at least 0.6 with the mean sealed-test gain of ten loops, and more strongly than HGM's estimate from the same 300 evaluations. *Test (Experiment 4):* within-base Pearson correlation; Williams' test for two correlations that share one variable. *Falsified if* the correlation is below 0.6 or does not exceed the clade estimate's.
> 4. **H4, the mechanism is smaller and better-aimed edits.** In structured cells, successful edits touch fewer lines and break fewer correct examples, and fewer edits are invalid. Under O, edits that cite a logged quantity succeed more often, and seeded defects are repaired in fewer evaluations. *Test (Experiments 2 and 3).*

Then name the single primary test for each hypothesis, or change line 223 to "each hypothesis names its primary test first".

### 1.5 Break the four densest Method paragraphs into definition lists, and define the success event once

**Problem.** "The single-edit success profile" (line 114) is 416 words in seven sentences of up to 58 words, and it introduces about ten objects: $V_i$, validity, $\Delta_i$, the zero-error exclusion, the eligible-example list, the missing-score charge, coverage, $Z_i$, $\pi$, the regression share, $s_{dev}$ and $g_{dev}$. "Holding length and feedback fixed" (line 110) carries six separate controls in one paragraph. "Equivalence gate" opens with a 62-word sentence. Experiment 6 (line 206) is a 94-word sentence. The success event ("lowers error by at least 1%") is defined five times, in lines 43, 74 and 114 and in the Figure 4 and 6 captions. Two versions exist (development event and selection event), and the reader has to track which one each estimator uses.

**Fix.**
- Define the two success events once, in Key ideas, with names: "A *selection success* is a valid edit that lowers $J_{sel}$ by at least 1% of the parent's value; a *development success* is the same on $J_{dev}$. The profile uses selection successes; the loop model, the clade counts and the prior use development successes, the event a loop's acceptance rule sees." Every later mention then uses the name.
- Rewrite the profile paragraph as a list: **Valid**, **Gain** $\Delta_i$, **Scoring rule** (with an example: "a missing score for a person whose reference is 0.8 is charged 0.8, the worst error any in-range score could have"), **Success** $Z_i$, **Profile** $(v,s,g,r)$, **Development variant** $(s_{dev},g_{dev})$. Move the session-length power sentence (line 116) to Statistical analysis, which already discusses power.
- Move the six controls from line 110 to the near-empty "Ablations and controls" subsection (line 215) and lay them out as **Control: what it rules out**. Say which arm is the placebo: "padded cell 1 is the length-matched placebo; unpadded cells 1 and 8 measure what padding itself does". As written, Key ideas defines a "length-matched placebo", but Method never says which arm it is.
- Split Experiment 6 into arms, budget, prediction and crossover rule.

---

## 2. Paragraph-by-paragraph edits

Line numbers refer to the current file.

### Box (lines 3 to 9)
- L3, Research question (45 words): acceptable. Optional tighter version: "If two versions of a harness return identical outputs on every input, does the way their code is written change how much an LLM self-improvement loop improves them at a fixed budget, and can a cheap one-step measurement predict the difference?"
- L5, Why it matters: states the premise but not the payoff; see 1.2.
- L7, ML contribution: 53 words of undefined terms; see 1.2.
- L9, falsifier: see 1.2. "a length-matched placebo reproduces the effects" is ambiguous until the placebo arm is named (1.5).

### The problem, in one concrete case
- L13 (paragraph 1): "OpenCap" is used without definition or citation. Add "(a markerless motion-capture system that reconstructs movement from two or more phones [new ref])" and cite Uhlrich et al. 2023, PLOS Comput Biol, https://doi.org/10.1371/journal.pcbi.1011462 (already verified in `biomech-facts.md`). Split the 45-word sentence: "On 43 held-out people it reached a task-averaged mean absolute error (MAE) of 0.146, worse than the 0.120 of a constant guess at each task's training mean. Only 567 of 729 task scores were valid, and the Y-Balance test received no score at all, although it alone explains 63% of the variance of the overall StaBLE score [1]." The constant-guess figure (now buried in Metrics, line 197) makes the case sharper and sets up the shrinkage caveat. Define RTMPose at first use (line 15): "a 2D keypoint detector [4]".
- L15 (paragraph 2): split the 51-word sentence at the colon: "Version S computes the same function in typed stages: pose input (RTMPose keypoints or OpenCap Monocular kinematics), filtering, center of mass, reach window and score. It logs a summary of each stage to a trace file, keeps ...". Change "may decide how much evidence" to "may determine how much evidence". "how the code is written" occurs here, at L23 and at L41; reword two of the three to avoid a refrain.
- L17: see 1.2.
- L19 (coding agent): good generalization. End it with a signpost: "H7 tests this prediction."
- Figure 1 caption (L23): "A point at budget $B$" collides with harness B; write "A point at a given number of labelled evaluations is the expected sealed-test improvement ...". The figure's y-axis says "held-out improvement", the caption says "sealed-test improvement"; use "sealed-test" in both.
- Figure 2 caption (L27): fine. Optionally tie it to the running example: "...so only B's trace can show that every Y-Balance reach window was empty."

### Key ideas
- L31 Harness: fine.
- L33 Loop and proposer: expand SICA ("the Self-Improving Coding Agent (SICA) [7]"). The mutation-operator sentence carries the mechanism; keep it.
- L35 BPT: add a one-line example: "for example, replacing `if v > 0.5:` with `if toe_speed_mps > cfg.threshold_mps:`, where the configuration holds 0.5".
- L37 to L41 Evolvability: see 1.3. Split the 43-word sentence after the definition of the optimizer. Note that $J$ here is on sealed people while the profile uses $J_{sel}$.
- L43 Metaproductivity: the 49-word sentence carries two ideas (HGM counts versus this proposal's event). Split it, and add an example: "a node whose clade holds 3 successes and 1 failure has estimate 0.75". Replace "one event shared by every estimator" with "every estimator in this proposal counts this same event". Define Thompson sampling here, since H5 and the prior use it: "HGM then draws one value per node from a Beta distribution with these counts and expands the node with the largest draw (Thompson sampling)".
- L45 Single-edit profile: "it is the primary outcome" contradicts Metrics (L197), where the success rate $s$ is primary. Write "its success rate $s$ is the primary outcome". Say that the four quantities are defined in Method.
- L47 Placebo and sealed people: two unrelated terms in one paragraph; fold sealed people into "The design in brief" (1.1).
- L49 Equivalence test: add a numeric example: "with $m=0.025$, a success rate of 0.10 is declared equivalent to the comparison arm only if the 90% interval of the difference lies within $\pm 0.025$".

### What is known and what is missing
- L53: cite AHE [12] at its first mention here, not only in the table.
- Table, AHE row: "pass@1" is undefined; write "first-attempt pass rate on Terminal-Bench 2, a benchmark of terminal tasks". Change "never ablated" to "its ablations add single evolved components; none removes the decomposition or an observability pillar" (this matches the paper's Table 3).
- Table, Code for Machines row: replace "no significant effect for Sonnet 4.5" with "13.2% against 16.0% for Sonnet 4.5, not significant". See citation finding 4.
- Table, Predict Before You Modify row: add the comparator, "up to 46% higher average performance than HyperAgents".
- Table, Meta-Harness row: add "scores-only and summarized feedback both trail raw traces (median 34.6 and 34.9 against 50.0)". This bears directly on the O design (Weakness 4).
- L70 gap paragraph (two sentences of 66 and 53 words): rewrite; see the cut list. Remove "the O factor is new only in a narrow sense:" (hedging pivot).

### Hypotheses
- L74: delete once 1.1 is in place (it defines cells and success, which will already be defined).
- L76 to L82: see 1.4. In H2, "as Code for Machines found for refactoring" overstates the source; write "consistent with the non-significant difference Code for Machines found for Sonnet 4.5". H2's "(pre-registered)" label implies the others are not; drop it or apply it to all. H6 says "From the degraded form", but Experiment 6 also starts from the as-written form; align them. H7: add "(exploratory)" (Weakness 8).
- "Holm correction across five main effects" (L76, L223): M, O, P and T are four factorial main effects, and N has three levels and appears only on cells 1 and 8. Define the fifth contrast ("physical against generic naming, pooled over cells 1 and 8").

### Method
- L86 intro: add a map sentence. "Four instruments follow: the equivalence gate makes variants; the single-edit profile measures them (H1, H2, H4); a loop model turns profiles into forecasts and a break-even budget (H3, H6); and a code-feature prior adapts parent selection (H5)."
- L90: "Each factor has a degraded and a structured level, so a base that is already well written does not sit at a ceiling." The "so" does not follow: having two levels does not by itself prevent a ceiling. Write "Every base is rewritten to both levels of each factor, so even a well-written base gets a degraded copy to compare against."
- L98: "from a short annotation of each base". Say who writes it: "a person marks stage boundaries and constants once per base". "Renaming is done by an LLM that receives only code" is passive; write "An LLM that sees only the code performs the renaming".
- Figure 3 caption (L102): fine.
- L106 gate (62-word first sentence): make it a three-item list (scores on cached inputs; scores on 10,000 fuzzed inputs per stage; tool-call sequence). "outputs are compared, never labels" is an antithesis; write "the gate compares outputs and reads no labels". Say what a "tool call" is in a harness that reads cached tool outputs (Question 4). Merge Experiment 1 ("Gate audit") into this paragraph.
- L110 controls: see 1.5. "O and T change what the trace contains, never what the loop may read" is an antithesis; write "O and T change the trace's content; the channel's format and length stay fixed". "would indicate memorization rather than diagnosis" has the logic reversed (Weakness 7).
- L114: see 1.5. "draw $n$ independent one-step edits" conflicts with L116, where edits within a session see summaries of earlier edits; write "draw $n$ one-step edits in sessions of ten". "This is what lets a repair of the unscored Y-Balance task register as a gain" is a pivot phrase; write "Under this rule, repairing the unscored Y-Balance task registers as a gain." State $J_{sel}$ of each base under this rule, so readers can see how much of the starting error is the missing-score penalty.
- L124 to L132 loop model: clear. Add one sentence saying why H3's forecast uses selection-event $(s,g)$ while $B^{\star}$ uses $(s_{dev},g_{dev})$ (Question 1).
- Figure 5 caption (L136): fine; see figure review for the mismatch with the L132 example.
- L140 to L144 prior: expand CMP. Explain "beta-binomial maximum likelihood" in a clause: "chosen to maximize the probability of the observed success counts when each node's rate is drawn from a Beta distribution centered on $\sigma(w^\top x_a)$". Add a numeric example: "with $\kappa=10$ and $\sigma(w^\top x_a)=0.2$, a node with one success has estimate $(1+2)/(1+10)=0.27$". Say whether HGM's temperature schedule $\tau$ is kept.
- Figure 6 caption (L148): 64 words; see figure review.
- L152 refactor-first: "This is the recursive step:" is a pivot phrase; write "The phase makes the loop recursive, because it restructures the code it will later optimize." "an 'always refactor' baseline skips the gate" is unclear; write "an unverified-refactor arm applies the same restructuring edits without the gate".
- L156 optimizers: define "island archive" ("several sub-populations that evolve separately and exchange candidates") and "evolve markers" ("comments that mark the region the LLM may edit"). The Meta-Harness-style proposer "reads and writes a directory of all earlier candidates' code, scores and traces". Say whether these are the fixed-length aggregated traces of L110 (Question 2).
- Pseudocode: label it "Tier 1".

### Experiments
- L179 (73-word sentence): Figure 7 already shows the three splits. Shorten to the numbers plus the leakage rule, and move the sealed cohort's history (parenthesis) to Risks, where it is already stated.
- L181: fine.
- L189 (53 words): split after "four independent implementations each".
- L193 Baselines: "IDM-style" is an undefined acronym; write "a forecaster in the style of the Improvement Dynamics Model (IDM) of Predict Before You Modify [13]".
- L197 Metrics: define "localization" for the defect probe ("whether the edit touches the stage that holds the defect").
- L202 Experiment 2: "alias" needs a gloss ("cannot be separated from"). Add an example cell: "cell 2 sets M and T structured and O and P degraded". The second sentence (50 words) lists three edit totals; it is clearer as "14,400 factorial edits + 7,200 naming + 7,200 control = 28,800".
- L203 Experiment 3: "The proposer states a cause before each edit" reads as agency; write "Each proposer output must begin with a stated cause".
- L206 Experiment 6: split the 94-word sentence (1.5).
- L207 Experiment 7: compress (cut list).
- L215 Ablations and controls: "private StaBLE bases and newly transformed coding variants limit contamination" does not say contamination of what; write "the proposer models cannot have seen the unpublished StaBLE bases or the newly transformed coding variants in pretraining". Move the controls here (1.5).
- L221 to L223 model: rename symbols (1.3). Define "average marginal effects" ("the average change in predicted success probability when a factor moves from degraded to structured").
- L225: define "design effect" ("the variance inflation from correlated edits within a session, $1+(m-1)\rho$ for session size $m$ and intraclass correlation $\rho$"). "which is why H2's equivalence test uses main effects" is a pivot phrase; write "so H2's equivalence test uses main effects".
- L227 (69-word H3 sentence): split into two. "which is why the primary test of H5 uses archive nodes": write "so H5's primary test uses archive nodes". Define Williams' test at first use (H3) rather than here.
- L231 second domain: fine.

### How to read the results
- L238 "Structure substitutes for proposer capability": acceptable as a reading.
- L239 and L242 point to "proposals 06 and 07" and "the leakage protocol of proposal 06". The proposal must stand alone; replace these with plain descriptions ("shift effort to how loops read tool outputs and trace leakage"; "audit for development-set leakage").
- L241 "and not as code form" is an antithesis; write "Logging helps as delivered information, as Meta-Harness found; the code that emits it adds nothing".
- L242: fix the permuted-label logic (Weakness 7).

### Compute, data and scope
- L250 (45-word sentence): compress (cut list). The arithmetic checks out. I recomputed 219,700 loop steps, 87,900 accepted candidates, 700 H100-hours (888 with the cache), 10.21 billion open-model tokens and USD 216 to 648 for the API. Total CPU is 44,110 hours, so "at most 44,000" should read "about 44,100".

### Risks and limitations
- Bullets 1 (equivalence), 6 (noise) and 7 (mediation) repeat Method or Statistical analysis; see the cut list.
- Add a risk for Weakness 3 (shrinkage edits counted as successes).

### Where to learn more
- L287: "GEPA and MIPRO" are undefined; write "two prompt optimizers, GEPA and MIPRO". "which is why logging changes" is the third "which is why"; write "so logging changes an optimizer's input".

### References
- [3]: use the exact title (citation finding 2).
- [22]: no year or authors; add the year of the release used and the maintainers as the repository names them (or "OpenEvolve contributors").
- [29] "Ye et al." lacks initials; use the same format as the other entries.
- Add OpenCap (Uhlrich et al. 2023), which is used at L13 but not cited.

### LLM tics found (STYLE.md)
| Line | Text | Type | Replacement |
|---|---|---|---|
| 70 | "the O factor is new only in a narrow sense:" | hedging pivot | "For O the question is narrower:" |
| 106 | "outputs are compared, never labels" | antithesis | "the gate compares outputs and reads no labels" |
| 110 | "change what the trace contains, never what the loop may read" | antithesis | see above |
| 110 | "memorization rather than diagnosis" | "rather than" | rewrite per Weakness 7 |
| 114 | "This is what lets a repair ..." | pivot phrase | "Under this rule, a repair ... registers as a gain." |
| 152 | "This is the recursive step:" | pivot phrase | see above |
| 225, 227, 287 | "which is why" (three times) | recycled pivot | "so" |
| 241 | "..., and not as code form" | antithesis | see above |
| 15, 23, 41 (and box) | "how the code is written" | refrain | vary: "code form", "the way it is coded" |
| 79 | "touch fewer lines, break fewer ..., and fewer candidates are invalid" | triad with broken parallelism | split per 1.4 |
| 203 | "The proposer states a cause" | mild agency | "Each proposer output must begin with a stated cause" |

No em-dashes, en-dashes, `\operatorname` or banned words were found (audit clean).

---

## 3. Cut list (target at or below about 5,900 words by `audit_doc.py`)

Current count: 6,299. Planned clarity additions (1.1 design-in-brief and trace, about +170; H1b and the decisive-experiment sentence, +60; examples in BPT, metaproductivity, scoring rule, equivalence and prior, +90; Meta-Harness numbers, constant-guess clause and placebo naming, +40) total about +360. Cuts must therefore remove at least about 760 words.

| # | Passage | Action | Words saved |
|---|---|---|---|
| 1 | Gap paragraph, L70 (about 150 words) | Replace with: "No study we found randomizes behavior-preserving rewrites of a harness and then measures how far an LLM optimizer improves it at a fixed budget; budget-allocation work does not consider restructuring [25]. Four things are missing: a causal estimate of each structural property's effect with behavior and length fixed; its dependence on proposer capability; a cheap measurement that predicts it; and a test of whether structure can rank newborn parents, where HGM has almost no data, or justify a refactoring phase that gains nothing at first, which Predict Before You Modify leaves open [13]. Meta-Harness shows that what the proposer reads matters [14], so for O the question is whether it matters which code fills a fixed trace channel." | about 45 |
| 2 | Hypotheses L74 to L82 (437 words) | Delete the preamble; rewrite per 1.4 (one claim plus a short Test and Falsified-if line each) | about 110 net of H1b |
| 3 | Literature table | Delete the FunSearch/OpenEvolve row (the convention it raises is never tested); shorten the "When Names Disappear; AGENTS.md" and "Gurkan; van Stein; Pelleriti" cells to one clause each | about 40 |
| 4 | Key ideas L47 | Delete the sealed-people half (moved into the design paragraph) | about 25 |
| 5 | Profile L116 | Move the session-length power claim into Statistical analysis and merge it with the design-effect sentence there | about 40 |
| 6 | Controls L110 | Restructure as a list (1.5); delete the external-trace rationale, which is repeated from L70 and the outcome table | about 45 |
| 7 | Equivalence gate L106 and Experiment 1 | Delete "Tool outputs are cached once, so ..." (said again in Compute); merge Experiment 1 into the gate paragraph | about 30 |
| 8 | Data and splits L179 | Drop the parenthesis about the sealed cohort's history (Risks covers it) and the restated split roles that Figure 7 shows | about 40 |
| 9 | Statistical analysis L225 to L227 | Compress the power material into: "Simulation (`sim/c_power.py`): 20 bases give power 0.99, 0.95 and 0.72 for base-by-arm heterogeneity of 0, 0.2 and 0.4 (three bases give at most 0.38), so tier 1 uses 20 bases." Shorten the H3 power sentence to its two power figures and the independence caveat | about 80 |
| 10 | Compute L250 and L269 | Keep the assumptions (throughput, tokens per edit, CPU per example) and one worked example (tier-2 loops); move the second-domain arithmetic into the table row | about 70 |
| 11 | Risks | Delete "Equivalence rests on testing", "Loops are noisy" and "Mediation needs assumptions" (each repeats Method or Statistics); add one line for shrinkage | about 60 net |
| 12 | Outcome table | Shorten "What we would do next" cells to five words or fewer; merge "Placebo matches" with "External trace matches" into one length-and-delivery row | about 40 |
| 13 | Figure captions | Fig 4 (72 words) to about 40: "Thirty one-step edits from one parent in three sessions of ten, each invalid, valid with selection gain under 1%, or a success (illustrative). Squares give $v$ and $s$; $g$ and $r$ need per-edit gains the squares do not show." Fig 6 (64) to about 40; Fig 8 (about 55) to about 35; Fig 3 (47) to about 35 | about 90 |
| 14 | Where to learn more | Cut each "what it teaches" clause to at most 10 words | about 40 |
| 15 | Experiment 7 L207 | "The features $x_a$ of every accepted tier-2 candidate are logged, with and without a lint gate that rejects edits lowering a structured factor, since LLM editing tends to add complexity [18]." | about 15 |
| 16 | Box ML contribution | Replace per 1.2 (adds the experiment, removes the term list) | about 0 |
| 17 | Problem L17 | Drop the first sentence of the bold paragraph (it repeats the box) | about 30 |
| | **Total cuts** | | **about 800** |

Expected result: 6,299 + 360 - 800 ≈ 5,860 words.

---

## 4. Scientific review (ICML format)

### Summary
The proposal asks whether the way a harness's code is written changes how much an LLM-driven self-improvement loop can improve it, while input-output behavior and file length are held fixed. The running case is a StaBLE balance-scoring harness that cannot find a Y-Balance reach window in single-phone reconstructions. Variants are produced by scripted, behavior-preserving transformations along five factors (modularity, observability, named parameters, warning-only checks, naming). Each variant must pass a differential-testing gate and is padded to a common token length. Tier 1 measures one-step edit profiles (valid rate, success rate, gain, regression share) for 20 bases, an eight-cell half fraction and three proposers (28,800 edits). Tier 2 runs 960 loops on 96 configurations of three bases to test whether a profile-based forecast predicts sealed-test gain better than HGM's clade estimate. The proposal also derives a break-even budget for refactoring before search, fits a code-feature prior for HGM-style parent selection, probes repair of seeded defects, and replicates the main contrasts on a self-improving coding agent (Aider Polyglot). Cost: about 700 H100-hours and 10.2 billion open-model tokens.

### Strengths
1. **A clean causal handle.** The equivalence gate makes $J$ identical across variants, so any difference in improvability is attributable to code form. Padding, synonym renaming and the external-trace control separate length, vocabulary and delivered information from structure. The observational evidence the proposal builds on (Code for Machines) has none of this control.
2. **Nulls are informative by design.** Equivalence margins, a placebo arm and pre-stated falsifying outcomes let a negative result carry weight, which matters because the nearest prior work found nulls for strong models.
3. **Leakage discipline.** Splits are made by person before anything is built. Normalization bounds are refit on development people only. The gate never runs on sealed inputs, and sealed people meet each final candidate once.
4. **A testable quantitative model.** The accept-if-better model gives a closed-form break-even budget $B^{\star}$ (checked: $F(B)=1-(1-sg)^B$ follows from $K\sim\mathrm{Binomial}(B,s)$, and the 0.010 to 0.015 example gives $B^{\star}=2.98\,C_R$). The crossover rule, including the no-crossing outcome, is pre-specified.
5. **Complete, correct arithmetic.** Every compute row recomputes to within rounding.
6. **A second domain** whose error signal differs (tests print failures; balance scores fail silently) gives H7 a principled direction.

### Weaknesses (each with a fix)

1. **H2's equivalence leg cannot pass at the planned sample size, even if every true effect is zero.** At the stated rate of 0.10 and design effect of 1.45, 2,400 edits per factor level give a standard error of 0.0104. Two one-sided tests at margin $\pm 0.025$ succeed only if the estimate falls within $0.025-1.645\times0.0104=\pm0.0078$. With a true effect of exactly zero, that happens with probability 0.55 per main effect. Requiring all four main effects to pass gives about 0.09. Line 225 treats "a 90% half-width near 0.017, inside the equivalence margin" as adequate, which conflates interval width with the power of the equivalence test. The box's first falsifier depends on the same test. **Fix:** give the frontier proposer about 5,400 edits per factor level (10,800 factorial edits instead of 4,800; about 99 million more API tokens, roughly USD 140 to 400, and 1,100 CPU-hours). That yields joint power of 0.81. Alternatively, pre-register a margin of $\pm 0.035$ (joint power 0.70) with a stated justification, or claim equivalence factor by factor.

2. **H1's composite contrast is underpowered for its own effect size.** Cells 1 and 8 have 600 edits each per proposer. For 0.10 against 0.15, power is 0.70 one-sided and 0.59 two-sided, and it is lower still if "exceeds by at least 0.05" is tested as a minimum effect. **Fix:** state H1 as superiority (effect above zero) with the O and P main effects (2,400 per level) as its primary test, or add 600 edits each to cells 1 and 8 for the 30B proposer (1,200 edits, about 1 H100-hour), which raises two-sided power to 0.87.

3. **The success event rewards shrinkage and constant imputation.** The pilot harness (0.146) is worse than a constant guess at each task's mean (0.120). A missing score is charged $\max(y,1-y)\ge 0.5$. The cheapest "success" for the reaching-family base is therefore an edit that outputs the task mean whenever no window is found. That needs no diagnosis, and its ease may depend on P (a named threshold is easy to clamp) more than on O. This dilutes or misattributes the mechanism claims (H4), and it means the profile can rise without the harness measuring anyone better. Loops report Spearman correlation as a secondary metric, but single-edit success has no such guard. **Fix:** pre-register success as "$\Delta_i\ge\delta$ and no fall in within-task Spearman correlation on selection people". Flag and report separately any edits that cut within-task output variance by more than half. Report each base's $J_{sel}$ under the charging rule.

4. **The O arm is delivered through the channel that Meta-Harness found ineffective.** Every arm gets a fixed-length, aggregated trace ("per-task summaries plus at most five per-trial excerpts"). Meta-Harness's own ablation (Table 3) found that summaries do not beat scores alone (median 34.9 against 34.6), while raw traces do (50.0), and the authors write that "summaries do not recover the missing signal". A null on O would then say more about aggregation than about observability. In addition, the Meta-Harness-style optimizer is described as reading "a directory of all earlier candidates' code, scores and traces", which may break the one-channel rule in tier 2. **Fix:** cite this result. Specify which trace the Meta-Harness-style loop reads. Add one tier-1 arm in which cell 8's trace is available as raw per-trial files under the same total token budget, so the design can tell "O does not help" apart from "aggregated O does not help".

5. **The H5 comparison in biomechanics is tilted toward the prior.** On cached inputs a harness evaluation is deterministic, so a node's own evaluation contributes one count and can never contribute more. HGM's task-level counts, by contrast, accumulate per task. This makes the clade estimate weaker at 0 and 5 descendants than it is in HGM. The prior also has a training and test mismatch. It is fit on children of scripted, length-padded, behavior-equivalent variants (token length varies only between bases, which cross-fitting holds out) and tested on LLM-evolved archive nodes. **Fix:** count successes per task within a family, so that one evaluation gives several counts, as in HGM. Include archive nodes from held-out bases in the prior's cross-fitting folds. Report the shift in each feature's distribution between training and test nodes.

6. **The H3 forecast and the $B^{\star}$ forecast use different success events without a stated reason.** $\hat F$ uses selection-event $(s,g)$; $B^{\star}$ uses $(s_{dev},g_{dev})$ "because a loop accepts on development error". By the proposal's own argument, the loop model behind $\hat F$ should use the development event too. The decision rule for "correlation of at least 0.6" (point estimate or lower bound) is unstated, and attenuation correction is unstable at reliabilities of 0.75 and 0.83. The beat-the-clade comparison has power 0.38 when the true correlations are 0.6 and 0.4. **Fix:** pre-register one event for both forecasts, or report both. Make the raw within-base correlation primary and the attenuation-corrected one secondary. State that 0.6 is a point-estimate criterion. In H3, say that the comparison with the clade estimate is powered only for gaps of about 0.4.

7. **The permuted-label control is interpreted backwards.** L110 says that "a logging gain that survives permutation would indicate memorization rather than diagnosis". Suppose the O gain is measured on sealed people. If it survives permuted development labels, the trace supports label-free diagnosis (fixing an empty window needs no labels), which is the opposite of memorization. Memorization shows up as an O advantage on development error under permuted labels. **Fix:** "If O lowers development error more than cell 1 does when development labels are permuted, the trace is helping the loop fit noise." Update the matching outcome-table row (L242).

8. **H7 compares effects measured on different scales.** The success events differ by domain (a 1% relative MAE drop against a pass-count rise beyond rerun noise), base rates differ, and the minimum detectable difference (0.054) exceeds the effect of interest (0.05). **Fix:** label H7 exploratory, or pre-register the comparison on the log-odds-ratio scale with a power statement.

9. **The headline question has no numbered hypothesis.** See 1.2. **Fix:** add H1b (tier-2 O main effect on sealed-test gain).

10. *Settled but limiting contribution (not re-raised as defects):* tier-2 and refactor claims rest on three bases; the sealed people were scored once in the pilot; the 480B and frontier proposers do not run loops. These are stated in Risks. They bound the headline claim to "harnesses like these three, with a 30B proposer".

### Questions for the authors
1. Why does H3's forecast use selection-event $(s,g)$ while $B^{\star}$ uses $(s_{dev},g_{dev})$?
2. In the Meta-Harness-style loop, does the proposer read the fixed-length aggregated traces or the raw trace files of earlier candidates?
3. What is the fifth main effect in "Holm correction across five main effects", given that N has three levels and appears only on cells 1 and 8?
4. Harnesses read cached tool outputs. Which tool calls does the gate compare, and may loop edits change them?
5. In the balance-domain clade estimate, is one evaluation of a node one count, or one count per task?
6. What is each base's starting $J_{sel}$ under the $\max(y,1-y)$ rule, and what share of it comes from unscored trials?
7. Is HGM's Thompson-sampling temperature schedule kept when the structural prior replaces the flat prior?
8. For the strongest proposer, what is the equivalence test's power under your own simulation once base heterogeneity is included?

### Scores
- Soundness: **3 / 4.** The design is careful and the arithmetic is right. The H2 equivalence power, the shrinkage-prone success event and the aggregated O channel need fixing before the headline nulls or positives can be trusted.
- Presentation: **2 / 4.** The content is rigorous, but it is dense: terms are used before they are defined, symbols are overloaded, several sentences run past 50 words, and the success event is defined five times.
- Contribution: **3 / 4.** This is the first randomized, behavior-controlled test of a premise that current harness-evolution systems rely on. It also offers a usable one-step predictor and a closed-form refactoring rule. The scope is limited to three tier-2 bases and one loop proposer.
- Overall: **6 / 10.**
- Confidence: **4 / 5.**

---

## 5. Citation spot-check (8 most load-bearing; each link fetched once)

| # | Ref | Link fetched | Entry matches link? | Claim in text | Finding |
|---|---|---|---|---|---|
| 1 | [1] StaBLE | doi.org/10.64898/... redirects to the bioRxiv lookup | Yes: title, first authors (Heigold, Ruth, Muccini), bioRxiv | 180 people, 18 tasks, three phones, OpenCap, Y-Balance explains 63% | The abstract confirms 180 participants and 18 tasks. The three phones, OpenCap and the 63% figure are not on the landing page; they come from the local full-text notes (`biomech-facts.md`). No mismatch. Because the 63% figure carries the motivation, recheck it against the full text. Separately, OpenCap itself has no citation; add Uhlrich et al. 2023. |
| 2 | [3] OpenCap Monocular | arxiv.org/abs/2603.24733 | **No.** The entry gives a bracketed description in place of the title | Single-phone 3D kinematics | The exact title is "OpenCap Monocular: 3D Human Kinematics and Musculoskeletal Dynamics from a Single Smartphone Video" (Gilon S, Miller EY, Uhlrich SD, arXiv:2603.24733, 2026). Replace the bracketed description. |
| 3 | [5] DGM | arxiv.org/abs/2505.22954 | Yes | Polyglot 14.2% to 30.7%; lineages pass through lower-scoring nodes | Numbers match (SWE-bench 20.0% to 50.0%, Polyglot 14.2% to 30.7%). The lower-scoring-ancestor claim is in the body, not the abstract ("stepping stones"); the local notes record it as verified in HTML v3. |
| 4 | [10] Code for Machines | arxiv.org/html/2601.02200 | Yes (FORGE 2026 noted on the page) | Qwen 19.3% against 27.8%; no significant effect for Sonnet 4.5 or agentic Claude; H2 "as Code for Machines found" | The numbers match (Table 2; p = 0.439 for both Claude setups). **Overstated in H2:** the paper reports non-significance, not equivalence, and Sonnet 4.5's gap (13.2% against 16.0%, 2.8 points) lies *outside* the proposal's $\pm 0.025$ margin. Reword to "consistent with the non-significant difference Code for Machines found for Sonnet 4.5 (13.2% against 16.0%)". |
| 5 | [6] HGM | arxiv.org/html/2510.21614 | Yes. The arXiv page lists no venue; the ICLR 2026 poster is recorded in the local notes | CMP pooled over the clade including the node; $n_s/(n_s+n_f)$; Thompson sampling; 800-evaluation protocol | All confirmed (Sec. 3.3; Sec. 4.2 uses at most 800 evaluations). HGM samples Beta$(\tau(1+n_s),\tau(1+n_f))$ with a growing temperature $\tau$, so the prior section should say whether $\tau$ is kept. |
| 6 | [12] AHE | arxiv.org/html/2604.25850 | Yes | Terminal-Bench 2 pass@1 69.7% to 77.0%; decomposition and observability never ablated | The numbers match. The "never ablated" claim holds for the decomposition and the three observability pillars, but the paper does run component-layer ablations (Table 3: memory only 75.3%, tool only 73.0%, middleware only 71.9%). Write "its ablations add single components; none removes the decomposition or an observability pillar". |
| 7 | [13] Predict Before You Modify | arxiv.org/abs/2610.13991 and the HTML | Yes | Forecasting before evaluation improves self-evolution by up to 46%; leaves zero-immediate-gain steps open | Confirmed. The 46% is "higher average performance over generations" relative to HyperAgents, so name that comparator. The conclusion lists "modification sequences whose early steps offer little immediate gain but enable greater improvements" as future work, which matches the gap claim. |
| 8 | [14] Meta-Harness | arxiv.org/abs/2603.28052 and the HTML | Yes | Proposer reads code, scores and traces and beats hand-built harnesses; what it reads changes outcomes | Confirmed, but **the row omits the finding most relevant to O**. In Table 3, summaries do not beat scores alone (median 34.9 against 34.6), while raw traces reach 50.0, and the authors write that "summaries do not recover the missing signal". Add this to the row and address it in the design (Weakness 4). |

Additional checks, all matching: [15] Component-Aware Feedback (one third of the budget, as a median, to reach the strongest baseline's final quality; presupposes components), [26] Qwen3-Coder-30B-A3B (30.5B total, 3.3B active), [33] Aider Polyglot (225 Exercism problems in 6 languages). Format issues: [22] has no year or authors, and [29] "Ye et al." lacks initials.

---

## 6. Figure review

All eight PNGs were rendered and inspected at full size. None has collisions, off-canvas text or arrows crossing text.

**Figure 1, `same-outputs-different-futures`.** *One point:* yes, same outputs and different improvement curves. *Caption:* says what a point means and that the curves are illustrative. *Matches text:* yes. *Changes:* (a) The y-axis reads "held-out improvement" while the caption and text say "sealed-test"; use "sealed-test improvement". (b) Harness B's card says "invariant checks", a term the text never uses; write "warning-only checks". (c) If the text renames harness B to S (1.3), relabel the card and the curve end "S". Verdict: ship after the label edits.

**Figure 2, `pipeline-two-forms`** (round-3 fix not re-reviewed by Codex). *One point:* yes; the feedback band now says "score error plus a per-stage trace" and A's box says "Only its error is fed back", which resolves the round-3 recipient issue. *Caption:* adequate. *Matches text:* mostly. *Changes:* (a) "COM range" in the band is an unexpanded acronym; write "center-of-mass range". (b) The input card says "kp, RTMPose 2D", but the next stage produces metric 3D quantities (`com_ap_m`), and the text says the input is "RTMPose keypoints or OpenCap Monocular kinematics". Write "RTMPose 2D or OpenCap Monocular 3D". (c) Optional: tie the band to the running example with "window found or empty (empty for every Y-Balance trial in the lab pilot)", which is a pilot fact and not an invented result. Verdict: ship after (a) and (b).

**Figure 3, `bpt-equivalence-gate`** (round-3 fix not re-reviewed). *One point:* yes; the gate now reads "On cached and fuzzed inputs: scores and tool calls match the seed", which fixes the round-3 qualifier problem. *Caption:* adequate (47 words; trim to about 35). *Matches text:* yes. *Change:* "Seed harness" and "match the seed" use a third word for what the text calls the *base*, and "seed" already means a random seed and DGM's or SICA's "seed agents". Rename the card "Base harness" and the gate line "match the base". Verdict: ship after the rename.

**Figure 4, `single-edit-profile`** (round-3 fix not re-reviewed). *One point:* yes. The arrowhead at the session bracket and the two legend entries now naming the same quantity resolve round 3. *Caption:* 72 words; trim per the cut list. *Matches text:* yes. *Suggested change:* let the illustration compute what it can. The grid shows 6 invalid edits and 4 successes, so the profile card could read "valid rate v = 24/30" and "success rate s = 4/30", with "g, r: from per-edit gains" on the last line. That makes the denominators concrete (Codex asked for them in round 3) and removes the impression that the colors determine $g$ and $r$. Verdict: ship; the numeric change is optional but cheap.

**Figure 5, `refactor-first-break-even`.** *One point:* yes. *Caption:* good. *Matches text:* **no, quantitatively.** `figs_05.py` uses r0 = 0.01 and r1 = 0.03 (the refactor triples $sg$), which puts the crossing at $B^{\star}\approx1.5\,C_R$. The text's worked example (L132: $sg$ from 0.010 to 0.015) gives $B^{\star}\approx3\,C_R$. *Change:* set r1 = 0.015 in `refactor_first()`, so the crossing falls at 60 on the 120-wide axis, still well inside the plot. Label the bracket "refactor cost $C_R$" and the crossing "B* ≈ 3 C_R", so that figure and example agree. Verdict: fix.

**Figure 6, `parent-selection-at-birth`** (last Codex verdict: redraw; round-3 fixes not re-reviewed). *Rendering:* the round-3 layout fixes worked. DGM is a dot on its own axis, both densities share the 0 to 1 "clade success rate" axis, and the blue curve is labelled "hypothesized prior". *One point:* only partly, and for a conceptual reason that layout cannot fix. The figure shows the prior as *concentrated*, but H5 is about *ranking* newborn nodes (Spearman correlation and regret). A concentrated prior can be confidently wrong, and with one node the figure cannot show ranking at all. *Redraw:* show two newborn nodes, one from degraded code and one from structured code, with the same development score and the same single outcome. DGM's two dots coincide; HGM's two Beta(2,1) ramps coincide (say "one success" on the ramp, since its shape depends on the outcome); the structural prior places the two nodes at different clade success rates. Title: "Hypothesis: code features separate newborn nodes that score and count alike." Caption (about 40 words): "Two new nodes with one evaluation each and the same outcome. DGM and HGM cannot tell them apart; the structural prior separates them using code features alone. H5 tests whether that separation ranks nodes by their later metaproductivity. Densities are illustrative." Verdict: redraw.

**Figure 7, `participant-splits`.** *One point:* yes. *Caption:* good. *Matches text:* yes (85 + 43 + 43 = 171; normalization fitted on development people only). The lint's arc warning concerns the padlock icon and is harmless. Verdict: ship.

**Figure 8, `two-tier-design`** (lint: 128 words, too much text). *One point:* yes, cheap profiles checked against loops. *Correctness:* I checked that the matrix is a valid $I=MOPT$ half fraction (every column has an even number of degraded levels). *Caption:* adequate. *Matches text:* yes. *Changes to reach 90 words or fewer:* (a) delete the key line "M modularity, O observability, P parameters, T checks" and instead label the matrix rows with the full factor names, which Codex also asked for (net about -2 words, and it removes the decode step); (b) shorten the subtitle to "8 cells x 20 bases x 3 proposers x 30 edits = 14,400 edits" and move "Resolution IV half fraction, I = MOPT" to the caption (-6); (c) shorten the lower box to "10 loops per configuration (2 optimizers x 5 seeds, B = 100); 960 in all" (-8); (d) delete "Within-base correlation" from the comparison box and say it in the caption (-2); (e) "3 bases x all 32 factor settings" leaves 32 unexplained; add "(N opaque or physical)" to the caption, not the figure. With the row labels counted, the result is still about 105 words. The remaining overage is cell numbers and factor letters, which Codex accepted. Removing the cell-number row (keeping only the "1" and "8" labels on the dashed outlines) brings it to about 95. Verdict: fix (text only).
