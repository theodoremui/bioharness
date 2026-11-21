# Adversarial review and revision record

Three AI reviewers evaluated first revisions written by someone else. The calibration reviewer read proposals 1 and 4, the paired-measurement reviewer read 2, and the biased-reference reviewer read 3. They examined the strongest precedents, challenged the experimental inference and inspected rendered figures. The authors revised all four proposals. This record describes design changes and outstanding empirical questions.

## How the reviews judged a proposal

ICLR asks what knowledge a paper would add, whether it is well motivated in the literature and what evidence supports its claims. ICML's main review form evaluates soundness, presentation, significance and originality, including new understanding gained from existing methods. NeurIPS' main-track guidance asks application-driven work to explain why methodological choices succeed or fail. Its concept-and-feasibility guidance also expects rigorous support for claims made now. We applied these criteria to research plans. [ICLR 2026 Reviewer Guide](https://iclr.cc/Conferences/2026/ReviewerGuide) · [ICML 2026 Reviewer Instructions](https://icml.cc/Conferences/2026/ReviewerInstructions) · [NeurIPS 2026 Reviewer Guidelines](https://neurips.cc/Conferences/2026/ReviewerGuidelines)

Two award-winning studies supplied tests of scientific clarity. Schaeffer, Miranda and Koyejo compared metrics on fixed model outputs, derived predictions and tested them on language and vision tasks. Their NeurIPS Outstanding Paper motivates holding route outputs fixed while changing a reference in 1, and holding full executions fixed while changing the replay sampling design in 3. Locatello et al. constructed observationally equivalent latent explanations before benchmarking disentanglement methods across seven datasets. Their ICML Best Paper motivates the indistinguishable-update control in 2 and the two-world contrast control in 4. Both controls state what even a perfect learner could infer from the allowed observations. [Schaeffer et al., NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/adc98a266f45005c403b8311ca7e8bd7-Abstract-Conference.html) · [NeurIPS award record](https://media.neurips.cc/Conferences/NeurIPS2023/NeurIPS2023-Fact_Sheet.pdf) · [Locatello et al., ICML 2019](https://proceedings.mlr.press/v97/locatello19a.html) · [ETH award record](https://bmi.inf.ethz.ch/people/person/francesco-locatello/)

## 1. A biased reference can reverse a preference

**Strongest idea.** Fix both routes' marginal errors and alter only their dependence on the scorer. A ranking reversal then has a known cause. The correction's sign follows from expansion of squared loss. [Proposal 1](01-learning-with-biased-references.md)

| Challenge to the first revision | Change in the second revision |
|---|---|
| A reference denoiser with the same data can express the optimal expected loss comparison. Active model selection already targets differences between candidates. | Derive the squared-disagreement weighting that makes a denoiser a stronger control. Compare against it and a loss-difference audit rule at matched cost. |
| An audited contact on a source clip also labels any held-out pipeline already run on that clip. Fresh target labels could make ordinary rectification look like transfer. | Mask held-composition outputs during fitting. Separate the zero-target-audit test from the curve after randomized target audits. |
| A best-in-hindsight winner on a small test set looks artificially strong. Missed events might disappear from a squared-time calculation. | Make paired differences between locked feasible selectors primary. Freeze event matching and failure penalties. Apply the identity only to matched timestamps and score all eligible recordings. |
| Grid axes and references could obscure what was withheld. | Label pose and event-rule axes, distinguish held cells and separate fitting from confirmation participants. Specify force-derived events and perturb clock alignment. |

**Open limitation.** A physical instrument changes the error source and still has its own uncertainty. Fifteen healthy participants could expose a failure mode. Establishing useful transport to a new population or coupling to an unrecorded component requires additional evidence.

## 2. A calibration trial has value when it can change a choice

**Strongest idea.** Two updates can agree on every allowed slow trial yet favor opposite routes on fast trials. This gives a calculable cost to an uninformative probe. Oboe and task-oriented exploration already address much of the general problem of spending a few observations to make a later choice. [Proposal 2](02-learning-numerical-tool-behavior.md)

| Challenge to the first revision | Change in the second revision |
|---|---|
| A sophisticated router could win by buying the informative trial while conventional regression is given fixed trials. | Cross three response models with the same three probe-selection schemes. Include a cost-aware matrix-completion baseline. |
| Repeated recordings or synthetic faults cannot substitute for independent software replacements. Wrapper aliases and version names could disclose which update is installed. | Restrict the four-cell pilot to its named implementations, rotate held cells, and distinguish an implementation-family claim. Use opaque replacement IDs and matched canonicalization. |
| Counting every query as a new reference conceals the value of reusing one label. Treating a curated bank as free conceals its construction cost. | Price each distinct reference, each execution and the initial bank separately. Repeat deployment-library draws and compare paired participant losses at a prespecified joint budget. |
| The flowchart skipped from choosing a route to scoring it. | Show the selected route running on the held-out person and restrict the force measurement to the scorer. Add explicit arrowheads for renderer compatibility. |

**Open limitation.** A family of tools can share code without sharing residual behavior under new geometry. Failure on a real substitution after success on implanted faults would confine the mechanism to those faults. The pilot cannot establish a distribution of future software updates.

## 3. Cheap audits must resolve which edit to choose

**Strongest idea.** A replay is valuable when it resolves uncertainty in a decision. A large predictable timing shift may need fewer audits than a small unpredictable one. Historical benchmark matrices, predictive regression testing and checkpoint-based effect learning all supply strong competitors. [Proposal 3](03-learning-what-to-reexecute.md)

| Challenge to the first revision | Change in the second revision |
|---|---|
| Minimizing the variance of one candidate's mean need not reduce regret among close candidates. Shared runs can change the cost of a comparison. | Compare independent candidate audits with matched audits of the residual difference between contenders. Charge shared pose work once and score the final decision against full replay. |
| A dependency heuristic is too weak. One cheap edited function can prove that the rest of the state is unchanged. Historical-factor prediction also needs a fair cold start. | Perform exact partial recomputation for every selector. Include change-aware test prioritization and an equally informed flat regressor. Distinguish familiar recordings from new participants and edits with matched initialization costs. |
| A rare failure can go completely unobserved. An estimated standard error of zero would give false reassurance. A fixed mean-cost rule can overrun its budget. | Bound the loss, floor audit probabilities and use simultaneous design-based bounds for aggregate and subgroup decisions. Report indecision, actual cost and coverage over audit randomizations. |
| A diagram of residuals can imply that their true values are known before buying a run. Color alone can hide an exact-reuse decision. | Label the forecast scale and the constructed example explicitly. Mark reusable outputs in text and add directed connections to the edit diagram. |

**Open limitation.** A bound can be valid and too wide to support adoption. Exact caching or a score-only predictor could settle most decisions. Population claims require unused participants beyond repeated random audits on the same finite table.

## 4. Dependence matters before the next observation is bought

**Strongest idea.** Which error source is preferable depends on the physical contrast. A noisier endpoint can give a cleaner estimate of change when its errors recur across both trials. This motivates a predictive test for the next observation. [Proposal 4](04-learning-to-measure-change.md)

| Challenge to the first revision | Change in the second revision |
|---|---|
| An algebraic check by the author after independent review identified a further issue. Once the route outputs are observed, each proposed contrast is a known number. A covariance advantage attributed to terminal ranking could simply be a better change predictor. | Put cross-recording dependence in the forecast of an **unbought** observation. Freeze the terminal predictor shared by every acquisition policy in the primary comparison. Model detection failures separately when sampling possible measurements. |
| If another view is free, a policy can always observe it and ignore it. A timestamp offset common to heel strike and toe-off cancels within a stance duration. | Price processing a stored view. Compare with fixed acquisition at matched mean workloads and report full-budget acquisition as a cost ceiling. Use a contact-boundary error that can actually shift duration. |
| A correlation estimate from imperfect endpoint labels can include correlated reference noise. Distinct repeats cannot be labeled zero-change simply because they come from the same person. | Vary plausible reference correlation and timing thresholds. Use force-defined eligible strikes, report failure costs, and use different views of the same performance for verified nulls. |
| A privileged oracle can outperform any policy without demonstrating leakage. A loop diagram can hide which evidence has been purchased. | Add indistinguishable observations with target contrasts separated by a known amount and a separate history-matched oracle. Label the history update and hidden evaluator, and define endpoint scale in the crossover graphic. |

**Open limitation.** Near-zero changes inside reference uncertainty have ambiguous sign. Same-session BioCV trials can test whether purchasing an extra view helps. They cannot establish responsiveness across visits, clinical importance or a causal treatment effect.

## What compute and verification establish

H100 access makes batched pose inference and repeated replay experiments plausible. Each proposal has a smaller test that precedes expensive policy training. A compute estimate requires measured throughput for the chosen backbone, views and CPU tools. Statistical feasibility additionally depends on distinct participants, independent references, real software variants and the uncertainty target chosen before confirmation.

The overview figure compares the same offset under two decisions. The eight proposal figures depict analytic examples, study designs or allowed data flows. The examples in 1, 2 and 4 follow from their stated models. The audit variances in 3 use four hypothetical residual magnitudes. All nine SVGs were rendered and inspected at their display sizes. The Markdown image references resolve and all 47 math expressions passed rendering checks. The [literature synthesis](related-work.md) identifies the withdrawn manuscript and the assumptions retained from the primary sources.
