# Set-level review of proposals 05 to 08

Written by the orchestrating agent after the first literature round and red-team review (`red-team.md`), and before drafting. Drafting agents should follow the boundary rules and the shared protocol below.

## What unites the collection

A tool-using agent that improves itself has four places where the improvement can go right or wrong, and each proposal studies one of them with an intervention that only an instrumented harness makes possible.

| Proposal | Where in the loop | Intervention that makes the question causal |
|---|---|---|
| 05 What makes a harness improvable? | The code the improver edits | Behavior-preserving transformations: identical outputs, different structure |
| 06 Who does self-improvement leave behind? | The rule that decides which edits survive | Edit-effect panels that measure each candidate edit on every subgroup |
| 07 Can a VLM agent learn how to look at its own data? | What the agent sees of its tool outputs | Information-matched encodings and cross-reader transfer |
| 08 Does telling an agent the diagnosis change what it measures? | What context the measurement may condition on | Randomized framing and path splicing (replaying cached tool outputs across framings) |

In one sentence for the README: the four proposals ask what a self-improving agent edits, what it keeps, what it sees and what it is allowed to know, and each answers with an experiment in which the harness holds everything else fixed.

## Distinct contribution of each

- **05.** A causal, budgeted estimate of how code structure changes improvability, a cheap predictor (the single-edit success profile) that beats score-based and descendant-based parent selection, and a pre-registered crossover with proposer strength.
- **06.** A selection-dynamics account of when accept-if-the-average-improves degrades a minority, an early-warning quantity (edit-effect correlation between groups) that predicts it, a pre-registered inverted-U prediction, and an acceptance rule with a cumulative guarantee.
- **07.** Perceptual profiles of VLM readers that predict, before any search, how far a self-designed observation transfers to other models and to people, with gains decomposed into computation, general perception and reader-specific exploitation.
- **08.** A causal decomposition of how a stated hypothesis steers an agent's analysis path versus its final number, a decision-theoretic result that context-aware measurement harms the downstream decision even when it lowers measurement error, evidence on amplification by self-improvement, and a blind-analysis harness adapted from physics.

## Boundary rules

- **05 and 06** both use panels of one-step edits. 05 varies the harness's structure and measures average improvability; 06 holds structure fixed and measures how edit effects covary between groups and what the acceptance rule does with that covariance. 05 reports averages with subgroup results as a secondary check; 06 is about subgroups.
- **05 and trace leakage (dropped).** 05 holds the feedback channel fixed across arms. Its logging factor changes what the optimizer reads, so 05 reports every result on sealed held-out people and runs a permuted-label check on the logging arm. 05 does not study leakage.
- **07 and the earlier feature-versus-direct-prediction study.** 07 holds the information in the observation fixed (pixel oracle, information-matched text) and varies only its encoding. Whether the agent should compute features at all is out of scope.
- **07 and 08** both concern what a VLM reads. 07 is about how numeric tool outputs are encoded; 08 is about task context (a referral, a hypothesis) steering tool choices. 07 uses neutral prompts throughout; 08 uses fixed default encodings.
- **08 and earlier proposal 01 (biased references).** 01 concerns how an evaluation reference that shares processing steps misranks tools. 08 concerns how context given to the agent steers its own analysis path. 08 never uses a software reference as ground truth; it uses marker and force-plate references or StaBLE labels.
- **06 and the lab pilot.** The pilot observation that SFT hurt clinical extremes is motivation only, quoted as an internal account.

## Shared evaluation protocol (state it in each proposal, briefly, in the experiments section)

1. Split by participant before building any panel, cache or library. All recordings, tasks and phones of one person stay in one split.
2. Keep a sealed test set of people that no optimizer, search or training run ever touches. For small subgroups use five-fold cross-fitting with sealed folds.
3. Recompute StaBLE's feature normalization bounds (the per-feature minimum and maximum) on development people only; the published scores use all 180 people and leak the test scale. Report the published-scale analysis as secondary.
4. Run at least five seeds for any stochastic loop; self-improvement runs are noisy and selected candidates inherit a winner's curse (cite the noise and winner's-curse papers in the literature reports, for example arXiv 2610.09239 and 2608.18066).
5. Report effective sample size in people, person-clustered bootstrap intervals, and pre-registered primary outcomes and smallest effects of interest; use equivalence tests when a null would be informative.
6. Replicate the central result in one public domain outside biomechanics.
7. Report compute as H100-hours, LLM tokens and tool CPU time, with the arithmetic.

## Titles (questions, at most 12 words)

- 05: "What makes an agent harness easier to improve?"
- 06: "Who does self-improvement leave behind?"
- 07: "Can a vision-language agent learn how to look at its own data?"
- 08: "Does telling an agent the diagnosis change what it measures?"

## Expected ranking before drafting (to revisit after the literature sweeps for 06 and 08)

08 first if the sweep confirms no direct prior study: it pairs a clean causal design with a decision-theoretic result and has broad reach to AI-scientist agents. 06 second: a provable prediction and a safety-relevant failure that current loops do not track. 07 third: a quantitative transfer prediction in a field where qualitative findings exist. 05 fourth: a strong question that is the hardest to power, rescued by the single-edit profile.
