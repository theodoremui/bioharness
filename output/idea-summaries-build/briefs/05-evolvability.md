# Brief for proposal 05: what makes a harness improvable?

Output file: `docs/idea-summaries/05-what-makes-a-harness-improvable.md`. Figures: `docs/idea-summaries/images/05/`. Figure code: `output/idea-summaries-build/figs_05.py`.

## Core question

Holding an agent harness's input-output behavior fixed, do structural properties of its code causally change how far an LLM-driven self-improvement loop can improve it under a fixed evaluation budget? If they do, can a self-improving system raise its own improvability before it optimizes for score?

One-line thesis to build around: two harnesses that produce identical outputs on every input can have very different futures under self-improvement, and that difference can be measured, predicted and engineered.

## Why it is open

Recursive self-improvement loops (STOP, ADAS, AFlow, Goedel Agent, Darwin Goedel Machine, Huxley-Goedel Machine, Meta-Harness, AlphaEvolve and its open versions) pick which candidate to extend mainly by its current score, sometimes with novelty or descendant statistics. The Huxley-Goedel Machine paper names a "metaproductivity-performance mismatch": a candidate's own score predicts its descendants' gains poorly, and it estimates clade metaproductivity from descendants. Nobody has asked which properties of the artifact cause high metaproductivity, and no study holds function fixed while manipulating structure. Evolutionary biology has a theory for this (evolvability; modularity and the genotype-phenotype map; neutral networks), and genetic programming has studied representation effects, but LLM mutation operators read code, names and logs, so the relevant properties may be different (for example, identifier names matter to an LLM and not to a tree-crossover operator).

## Running biomechanics example

A StaBLE balance-scoring harness: phone video -> RTMPose 2D keypoints (optionally OpenCap Monocular 3D) -> gap filling and a low-pass filter -> a center-of-mass proxy -> sway features (path length, RMS, 95% confidence-ellipse area, time to stabilization) -> task-specific score mapping. Version A is one 400-line function with inlined constants. Version B is the same computation split into typed stages that log intermediate arrays (keypoint confidence, filtered trajectory summaries), with named configuration values and invariant checks. Both produce bit-identical scores. Errors in this pipeline are silent numbers, not crashes, which makes observability load-bearing. Contrast with a coding agent where failing tests announce failures loudly. Prediction: the observability effect is larger in the numeric pipeline than in the coding domain (a domain-by-factor interaction that is a sharp, testable prediction).

## Definitions to include

Harness; recursive self-improvement loop; mutation operator (an LLM proposing an edit); behavioral equivalence; behavior-preserving transformation (BPT); evolvability $E_B(h)$; metaproductivity and clade metaproductivity (HGM); differential testing.

Formal core: let $f_h$ be the input-output map of harness $h$, $\mathcal{O}$ a self-improvement operator with evaluation budget $B$ and random seed $\omega$. Define $E_B(h)=\mathbb{E}_\omega[S_{\text{test}}(\text{best}_B(h,\omega))]-S_{\text{test}}(h)$. If $f_h=f_{h'}$ on the input domain then $S(h)=S(h')$, yet $E_B(h)$ and $E_B(h')$ can differ. That difference is purely structural (same phenotype, different genotype).

## Method

1. A catalogue of BPTs, each a factor with two levels: M modularity (monolith vs typed stages), O observability (intermediate values written to the trace the optimizer reads; outputs unchanged), P parameter exposure (inlined constants vs a named config with ranges and units), T executable checks (invariant assertions and unit tests that never fire on valid inputs), N naming (descriptive identifiers and docstrings vs alpha-renamed identifiers). N isolates an LLM-specific prior.
2. Equivalence gate: every variant must give bit-identical outputs on all cached dev and test inputs plus property-based fuzzing on synthetic inputs (Hypothesis library). Tool outputs (pose, tracks, depth) are cached once so harness evaluation is CPU-cheap.
3. Fixed optimizer: an OpenEvolve or ShinkaEvolve style loop and, separately, a Meta-Harness style proposer with file access to code, scores and traces; one fixed proposer LLM (for example Qwen3-Coder-30B-A3B served with vLLM on H100s), replicated on a subset with a frontier API model.
4. Seeded-defect probe (cheap, decisive): plant known defects (wrong filter cutoff, swapped axis, frame-rate off by a factor, a units error) in every structural variant and measure evaluations-to-repair. This isolates diagnosability.
5. Open-ended optimization: fractional factorial $2^{4-1}$ over M, O, P, T (resolution IV) plus an N contrast, three independently written base harnesses per domain, five optimizer seeds each, budget $B=100$ to $150$ candidate evaluations.
6. Structure persistence: track modularity, coupling and function-length metrics across generations. Does the optimizer erode or build structure?
7. Metaproductivity prediction and parent selection inside a DGM-like archive: compare score-proportional selection (DGM), HGM's clade-metaproductivity Thompson sampling, a structure-informed prior plus score, and uniform, at equal total evaluations.
8. Refactor-first: give the optimizer a fraction $\rho\in\{0,0.1,0.25\}$ of its budget for self-proposed BPTs (accepted only if the equivalence gate passes) before score optimization. This is the recursive step: the system improves its own improvability.

## Experiments to specify

Data: StaBLE split by participant into optimizer-dev, selection and untouched test; BioCV for a force-plate event task. Second domain: a cheap harness benchmark (for example the ADAS or Meta-Harness task suites, or a small coding-agent harness such as mini-SWE-agent on a SWE-bench Verified subset). Primary outcome: held-out improvement at budget $B$. Secondary: area under the best-so-far curve, edit validity rate, fraction of improving edits, evaluations-to-repair for seeded defects, diagnosis accuracy (does the proposer's stated cause match the planted defect). Analysis: mixed-effects model with base harness and seed as random effects; pre-registered smallest effect of interest; equivalence tests (TOST) so a null is informative. Mediation: does O act through better diagnoses (proposals that cite logged quantities)?

## Figures (suggested)

1. Concept: two harnesses with identical outputs, diverging illustrative improvement curves.
2. The biomechanics pipeline in monolithic vs modular-observable form.
3. BPT catalogue with the equivalence gate (differential testing) as a checkpoint.
4. Factorial design flow: base harnesses x variants x seeds -> fixed optimizer -> held-out test.
5. Seeded-defect probe timeline.
6. Parent-selection rules compared inside an archive tree.
7. Refactor-first budget split.

## Falsifiers

Main effects and interactions all inside the equivalence margin; or effects that vanish after the optimizer's first few refactors; or structure-informed parent selection no better than HGM at equal budget.

## Upgrades after the literature check and red-team review (these override the design above where they conflict)

Read `output/idea-summaries-build/research/05-evolvability-literature.md` and the P05 section of `research/red-team.md` first.

- **Closest work to position against.** Code for Machines (Borg et al., arXiv 2601.02200: observational CodeHealth vs single-step LLM refactoring breakage; effect present for medium open models, absent for Sonnet 4.5 and agentic Claude); Agentic Harness Engineering (arXiv 2604.25850: builds on modularity and observability but never ablates them); Huxley-Goedel Machine (arXiv 2510.21614: clade metaproductivity from descendants only, so it is uninformative at birth); Darwin Goedel Machine (arXiv 2505.22954); Predict Before You Modify (arXiv 2610.13991: predicts one-step diff effects, leaves long-horizon zero-immediate-gain steps such as refactoring to future work); Meta-Harness (arXiv 2603.28052); When Names Disappear (arXiv 2510.03178); Mutation Without Variation (arXiv 2606.05408); Evaluating AGENTS.md. Say plainly that "clean code helps LLMs" is folk wisdom with mixed observational evidence, and that the contribution is the causal, behavior-controlled, budgeted test plus a usable predictor.
- **Primary measurable quantity: the single-edit success profile.** For each structural variant, sample a few hundred one-step edits and record, per edit, whether it is valid, whether it improves held-out error, and by how much. This is cheap and well powered. Claim and test three things: (1) randomized behavior-preserving transformations shift the profile, with token length matched across arms; (2) the early profile predicts the outcome of 50-iteration loops better than parent score (DGM) or clade metaproductivity (HGM) computed from the same number of evaluations, across two optimizers; (3) a simple accept-if-better model built on the profile predicts the budget at which a refactor-first phase starts to pay off.
- **Length-matched placebo.** Every structural arm gets a control with the same token count but no structural content (neutral comments or verbose but uninformative code), so a "modularity effect" cannot be a "shorter files effect".
- **Proposer-capability crossover (pre-registered surprising prediction).** Use at least three proposers (Qwen3-Coder-30B-A3B-Instruct, a larger open coder, one frontier API model). Predict that structure helps weak proposers and small budgets and fades for strong proposers, consistent with the Code for Machines null for strong models.
- **A factor only scientific harnesses have.** Physically meaningful names and units in code and logs (for example `com_ap_m`, `cutoff_hz`) against opaque names. This is where the biomechanics test bed is load-bearing.
- **Mediators.** Edit localization (lines and modules touched), regression rate per accepted edit as a pleiotropy proxy, and invalid-candidate rate.
- **Interface with proposal 06 and trace leakage.** Hold the feedback channel fixed across arms (aggregated traces), report every result on sealed held-out people with participant-level splits, and run a permuted-label check on the logging arm so a logging effect on dev cannot be memorization.
- **Practical win.** A structural metaproductivity prior that fixes HGM's cold start, and the refactor-first phase, compared with DGM, HGM and IDM-style prediction at matched evaluation budget, in the biomechanics harness and in one public non-biomechanics harness (for example the DGM seed agent on Aider Polyglot, or the Meta-Harness task suite).
- **Executable checks.** Define them as generic assertions (shapes, units, ranges, timestamps). Domain physics checks from earlier project ideas are out of scope here.
- **Power.** Self-improvement runs are noisy (cite the noise and winner's-curse papers found in the literature reports). Give a power calculation for the single-edit profile and for the loop-level validation.

## Power and estimand (from `research/theory-checks.md`, section C)

Detecting single-edit success 0.10 versus 0.15 needs about 686 edits per arm unclustered and about 1,000 per arm when edits are clustered in sessions of about 10 per seed (design effect at ICC 0.05). Three base harnesses cannot support claims about harnesses in general: either state the estimand as conditional on the chosen bases or use 10 or more independently written base harnesses (with 10 bases power for the population effect is roughly 0.4 to 0.8 depending on base-by-arm heterogeneity; 20 bases reach about 0.7 to 0.99). The loop-level minimum detectable effect is about 1.0 seed-to-seed standard deviation with 15 loops per arm and 0.51 for a factorial main effect over 120 loops. Showing that the early profile beats parent score or HGM as a predictor needs about 100 configurations. Design the study to these numbers and say so.
