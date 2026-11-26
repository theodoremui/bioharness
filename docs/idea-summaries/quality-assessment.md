**Research-idea quality assessment**

Assessment date: **26 November 2026**. Scope: the eight numbered proposals in this directory, evaluated as research plans in their current form.

**Recommendation:** prioritize proposal **8** for scientific impact, proposal **3** for a tractable first project, and proposal **1** as the shared measurement-validity foundation. Proposal **6** is a strong alternative if subgroup monitoring is the central research interest. Proposal **7** has substantial novelty potential but needs a much smaller validation study before its full program. Proposal **5** remains worthwhile, but additional prior work narrows its novelty. Proposal **4** needs better paired data; proposal **2** needs a clearer advantage over existing active calibration methods.

These judgments concern what the projects could establish, conditional on successful experiments. None currently demonstrates its central empirical claim. Detailed protocols, illustrative figures and simulations under assumed models do not constitute evidence that the proposed mechanism occurs in real agents.

**Rubric and interpretation**

All four criteria use a **1 to 5 scale**, in half-point increments. A 3 is a credible, worthwhile research direction; a 4 is strong; a 5 requires an exceptional case. Scores are comparative judgments, not probabilities of publication. Differences of half a point should not be treated as precise measurements.

| Criterion | 1: weak | 3: credible | 5: exceptional |
|---|---|---|---|
| Novelty | Substantially repeats established work | Distinct question, mechanism or empirical test using established ingredients | Opens a substantially new research direction or delivers a major conceptual advance |
| Significance | Limited consequence even if successful | Useful advance for an identifiable community | Changes how a broad community builds, evaluates or understands systems |
| Technical soundness | Central inference is invalid or underspecified | Coherent core with material assumptions or design gaps | Exceptionally strong identification, controls and inferential justification |
| Feasibility | Critical resources or evidence are unavailable | Executable with substantial engineering, data or statistical risk | A decisive study is readily executable with available resources and adequate independent evidence |

Novelty is assessed against the strongest relevant precedent, rather than the novelty of using a method in biomechanics. Significance reflects the knowledge a successful study would add. Soundness assesses the present argument and experiment, not hypothetical future repairs. Feasibility covers the central claims at the proposed scope, including data access, independent sample size, engineering and compute. Access to H100s is assumed as stated in the proposals; actual allocations and throughput have not been verified.

The four-dimensional ratings are more useful than a single average: an ambitious idea with high potential and weak feasibility serves a different purpose from a reliable infrastructure project. Confidence is moderate overall, with greater uncertainty in novelty and practical execution than in the elementary algebra. The previous AI reviews were treated as context, not independent empirical corroboration or scoring anchors.

| # | Idea | Novelty | Significance | Soundness | Feasibility | Assessment |
|---|---|---:|---:|---:|---:|---|
| 1 | Learning with biased references | 3.0 | 4.0 | 4.5 | 3.5 | Strong measurement-validity study; narrower algorithmic novelty |
| 2 | Learning numerical tool behavior | 2.5 | 3.5 | 4.0 | 3.0 | Useful active calibration; incremental until compositional transfer wins |
| 3 | Learning what to reexecute | 3.0 | 4.0 | 4.5 | 4.0 | Best practical starting point; value depends on residual savings after caching |
| 4 | Learning to measure change | 3.5 | 4.0 | 4.0 | 3.0 | Distinct acquisition question; independent paired data are the bottleneck |
| 5 | What makes a harness improvable | 3.5 | 4.0 | 3.5 | 3.0 | Useful controlled study; update novelty claims and simplify the program |
| 6 | Who self-improvement leaves behind | 3.5 | 4.5 | 3.5 | 3.0 | Important problem; prospective forecasting is the decisive contribution |
| 7 | Learning how to display tool outputs | 4.0 | 4.0 | 3.0 | 2.5 | Distinctive transfer hypothesis; fragile forecast and demanding execution |
| 8 | Blind analysis for agents | 4.0 | 4.5 | 4.0 | 3.0 | Strongest scientific opportunity; separate recoverability from calibration limits |

**1. Learning with biased references**

[Proposal](01-learning-with-biased-references.md)

**What deserves credit.** The proposal identifies a concrete way that a benchmark can reward a physically worse measurement route. Its strongest contribution would be demonstrating that recorded component sharing predicts these ranking errors on unseen pipeline combinations, under a fixed budget of independent audits.

- **Novelty, 3.0/5.** Correlated reference errors, noisy labels and prediction-assisted correction are established topics. [Prediction-Powered Inference](https://arxiv.org/abs/2301.09633) already uses paired measurements to correct inference based on predictions. The new part is the test of composition-level transfer and the decision-relevant relationship between reference error and route disagreement. The squared-loss identity is explanatory algebra, rather than a new inference principle. The proposal correctly acknowledges that an equally informed denoiser can express the optimal expected comparison.
- **Significance, 4.0/5.** A reproducible ranking reversal would directly challenge how measurement agents are selected and how shared software is used as ground truth. This could matter beyond biomechanics wherever tools and evaluators inherit components. The contribution remains useful even if ordinary denoising wins, provided the real failure mode and the audit requirements are established.
- **Technical soundness, 4.5/5.** The identity, constant-marginal-error intervention, disagreement-weighted denoiser, masking of held-out compositions and participant-level confirmation form a strong design. The distinction between zero-target-audit transfer and correction with new audits is especially valuable. The remaining leap is transport: component overlap need not imply stable residual dependence under new geometry, interactions or populations. Unbiased risk estimates also do not make the selected minimum unbiased; the separate confirmation set is essential.
- **Feasibility, 3.5/5.** A compact panel can be cached, and one independent event label can assess several routes. However, BioCV has only 15 participants and requires access approval. A three-way fit, selection and confirmation split will be small, and held-out route combinations are not independent new implementations. A pilot can establish a reversal; broad transport claims need more people and more genuinely distinct component combinations. [BioCV archive](https://researchdata.bath.ac.uk/1258/)

**Principal unresolved issue:** can ancestry improve selection beyond an equally informed weighted denoiser, or does it merely provide useful features to a standard model?

**Best first experiment:** fix two candidate routes, change one software-reference component, and test whether the proxy ranking reverses while the force-based ranking stays stable. Then run a small held-composition comparison against the weighted denoiser. Proceed to a new algorithm only if a reproducible advantage remains.

**Judgment:** a strong first paper on measurement validity is plausible; a major new learning method is less clearly justified.

**2. Learning numerical tool behavior**

[Proposal](02-learning-numerical-tool-behavior.md)

**What deserves credit.** Calibration is tied to the later routing decision, rather than to reducing average tool error. The slow-step/fast-step example clearly distinguishes informative from uninformative probes.

- **Novelty, 2.5/5.** Budgeted probing followed by algorithm selection is close to [Oboe](https://web.stanford.edu/~udell/doc/yang2019_oboe.pdf), which learns from a performance matrix and executes informative configurations under a time budget. Meta-learning and experimental design cover much of the remaining machinery. The specific contribution must be transfer of conditional error distributions across tool compositions. A set encoder, shared component coefficients and decision-aware acquisition do not establish that contribution by themselves.
- **Significance, 3.5/5.** Calibrating after software updates is an important operational problem, and task-conditioned calibration could avoid unnecessary full revalidation. The impact depends on how often updates actually change the best route and whether calibration cost is repaid over later cases. With only a few known substitutions, the result would principally benefit a specialist workflow.
- **Technical soundness, 4.0/5.** The indistinguishability example is correct. Crossing response models with the same probe-selection strategies is a strong control, as are opaque tool IDs, matched metadata and separate calibration people. Remaining weaknesses concern model complexity relative to the number of independent updates, and whether the inferred error distribution is calibrated enough for expected-value-of-information decisions.
- **Feasibility, 3.0/5.** Offline replay makes the mechanics manageable. The scarce resource is a library of independent, realistic replacements with conditional failure differences. A two-by-two crossed panel can test named substitutions, but it cannot support a general distribution of future updates or reliably train a rich meta-learner. Synthetic faults help test implementation and identification, but do not supply that evidence.

**Principal unresolved issue:** is component structure buying generalization that a conventional mixed-effects model or a low-rank response matrix cannot provide?

**Best first experiment:** give conventional regression, Oboe-style completion and the structured model the same diagnostic probes on a small set of real replacements. Measure routing gain after charging bank construction and calibration. If simpler methods tie, retain the calibration protocol and defer the neural response model.

**Judgment:** useful applied research, but the weakest current claim to a distinctive general ML contribution.

**3. Learning what to reexecute**

[Proposal](03-learning-what-to-reexecute.md)

**What deserves credit.** The proposal targets uncertainty in the decision between updates. It distinguishes an edit's large predictable effect from an effect that is difficult to predict, and explicitly gives every method exact caching before testing learned replay allocation.

- **Novelty, 3.0/5.** [Active Testing](https://proceedings.mlr.press/v139/kossen21a.html), [Active Statistical Inference](https://proceedings.mlr.press/v235/zrnic24a.html) and [Factorized Active Querying](https://arxiv.org/abs/2601.20251) already cover selective evaluation, prediction-assisted estimation and historical performance information. [CHILL-Harness](https://arxiv.org/abs/2607.25825) also learns effects of workflow interventions. The distinct question is whether edit location in an old trace predicts residual uncertainty on unseen edits after these advantages have been accounted for. The correction estimator and square-root allocation are established statistical ingredients.
- **Significance, 4.0/5.** Repeated evaluation can dominate harness optimization costs. Lower candidate-selection regret at a fixed replay budget would have direct practical value. Charging shared computation once and testing harmful adoption make the outcome relevant to real update decisions, rather than merely producing a smaller standard error.
- **Technical soundness, 4.5/5.** Conditional finite-table unbiasedness is valid when predictions are frozen and audit probabilities are positive and logged. The stated variance and expected-cost allocation are correct. Matching audits across contenders addresses the difference between estimating one score and selecting an update. Simultaneous bounded-loss intervals, failure penalties and unused participants for population claims are strong choices. The main concern is usefulness: conservative bounds can be too wide for adoption, and a fixed finite-table guarantee does not certify an indefinitely adaptive sequence of new edits.
- **Feasibility, 4.0/5.** This is the most contained experimental design: a small edit menu and exhaustive replay table can support repeated, objectively scored audit experiments without training a large agent. The main uncertainty is whether costly unresolved executions remain after exact partial recomputation. Full-table construction and predictor training must be charged when judging amortized value. The small human dataset limits population conclusions, but not the conditional replay-allocation experiment.

**Principal unresolved issue:** is there enough expensive, unpredictable continuation left after exact reuse to make a learned selector worthwhile?

**Best first experiment:** implement exact reuse, then measure residual replay cost and update-selection regret on a fixed menu containing real substitutions and branching edits. Compare uniform matched audits, a historical predictor and the equally informed flat regressor. Expand only if trace structure improves the decision at overlapping achieved costs.

**Judgment:** the strongest near-term project on execution and evaluation efficiency. Its expected contribution is a carefully isolated empirical and systems result, rather than a new general estimator.

**4. Learning to measure change**

[Proposal](04-learning-to-measure-change.md)

**What deserves credit.** The target is an individual's change, and the intervention is buying another view before its output is visible. Freezing the terminal estimator prevents a better change regressor from masquerading as a better acquisition policy.

- **Novelty, 3.5/5.** Error cancellation in differences is classical, and [EDDI](https://proceedings.mlr.press/v97/ma19c.html) and [generative active feature acquisition](https://proceedings.mlr.press/v139/li21p.html) already select unobserved information. The distinctive combination is learning cross-recording tool-error dependence to decide which member of a pair needs further processing, then testing compositional transfer against unrestricted acquisition. This is a meaningful question, although the covariance identity itself contributes no novelty.
- **Significance, 4.0/5.** A method optimized for endpoint accuracy can be poorly suited to detecting change. Establishing when that changes acquisition decisions could inform longitudinal measurement and other paired numerical workflows. The proposed same-session experiment would establish a measurement result; clinical responsiveness and between-visit monitoring remain additional claims requiring additional data.
- **Technical soundness, 4.0/5.** The risk expression and crossover are correct. The design appropriately holds endpoint marginals fixed, varies dependence, models failures, freezes the terminal predictor and tests static paired selection. Reference error can still mimic correlated route error. A factor covariance model fitted on a small panel also risks imposing the cancellation pattern it is intended to discover, so reference-noise sensitivity and unrestricted baselines are central.
- **Feasibility, 3.0/5.** Cached views and a two-step action space make a pilot feasible. The difficulty is estimating conditional cross-trial covariance with enough independent people and settings. Many pairs constructed from one person's trials are highly dependent. BioCV's repeated recordings from 15 people do not establish across-visit stability, and a larger instrumented cohort would be needed for that extension. [BioCV archive](https://researchdata.bath.ac.uk/1258/)

**Principal unresolved issue:** does conditional covariance change the best next observation often enough to beat a single fixed route or static paired acquisition?

**Best first experiment:** estimate the covariance structure on a small, clean force-referenced panel, propagate plausible reference correlation, and compare static paired selection with the best affordable next-view decision. Defer learned sequential control until this reveals a material opportunity.

**Judgment:** a coherent, potentially important direction whose progress will be determined more by paired-data quality than by policy complexity.

**5. What makes a harness improvable**

[Proposal](05-what-makes-a-harness-improvable.md)

**What deserves credit.** Equal starting task behavior makes this a much cleaner experiment than comparing unrelated harnesses. The strongest result would connect a verified change in code representation to later improvement, then predict that gain for new parents at a budget that includes obtaining the prediction.

- **Novelty, 3.5/5.** [HGM](https://arxiv.org/abs/2510.21614) already distinguishes current performance from improvement potential. Additional close work absent from the proposal includes [Harness Handbook](https://arxiv.org/abs/2607.13285), on behavior localization and edit planning, and [ModularRSI, section 6.3](https://arxiv.org/html/2609.14857v2), which compares modular, joint-module and non-modular evolution under matched aggregate evolution budgets. A November study also compares gated modular updates with full rewrites. The defensible novelty is the behavior-preserving, factor-separated intervention plus prospective prediction; broad claims that modularity's role in improvement is untested are too strong. [Harnesses That Improve Themselves](https://arxiv.org/html/2611.22299v1)
- **Significance, 4.0/5.** If a cheap representation-level intervention reliably improves future search, agent developers gain a new design objective beyond immediate accuracy. A generalizable predictor or demonstrated refactoring break-even point would be useful. Merely showing that meaningful variable names or helpful traces improve weak-model edits would be less consequential.
- **Technical soundness, 3.5/5.** Equivalence checks, length controls, an external tracer and multiple authors are substantial strengths. However, the observability treatment changes the information delivered to the proposer as well as the code; equality of task outputs does not imply equality of the optimizer's observation. The proposal recognizes the joint treatment, but the headline needs the same precision. Differential testing gives tested equivalence, not proof on every possible input. The stationary one-step model is mathematically correct under its assumptions but ignores exhaustion of easy fixes, changing mutation distributions and generalization gaps.
- **Feasibility, 3.0/5.** Twenty bases, many transformed versions, roughly 41,000 initial profile edits and extensive loops make this a large engineering study. The budget lists about 50,900 CPU-hours: approximately 33 days on 64 continuously occupied cores before overhead. The 300-evaluation profile is also more expensive than the 100-step search it forecasts, unless its cost is reused or amortized. Three tier-2 bases and one proposer constrain generality even with hundreds of runs.

**Specific repairs needed before execution:**

1. Cross code structure with externally supplied feedback on the main contrasts if the intended claim separates representation from observability. Treat physical names, units, ranges and annotations as information-bearing interventions.
2. Reconcile development-only normalization with the scoring assumption that every reference lies in `[0,1]`. Held-out normalized values can lie outside this range. Declare clipping or a valid extended scoring rule and missing-output penalty explicitly.
3. Include profile, prior-training and equivalence-gate costs in deployment comparisons. Separate amortized parent-selection utility from the cost of the research study.
4. Match power and generalization claims to bases and task families. More seeds estimate uncertainty conditional on the same few bases; they do not create additional independent harness families.

**Best first experiment:** use a modest set of independently authored bases, verified modular and inlined versions, and the same external trace. Test one-step gains and a small number of subsequent loops. Add the structural prior and refactoring budget prediction only after a stable effect survives these controls.

**Judgment:** worthwhile, but its clean causal question should replace the current collection of many partially independent claims.

**6. Who self-improvement leaves behind**

[Proposal](06-who-self-improvement-leaves-behind.md)

**What deserves credit.** The project asks about a predefined group's fate over time and proposes to predict it before observing the future. Logging rejected candidates is particularly valuable: an accepted-only record cannot reveal the distribution selection acts on.

- **Novelty, 3.5/5.** Aggregate improvement hiding regressions is already demonstrated by [item-level prompt-transition analysis](https://arxiv.org/abs/2610.19084) and addressed by [SAGE](https://arxiv.org/abs/2609.36043). Held-out scoring of every candidate also appears in [The Winner's Curse in LLM Self-Improvement Loops](https://arxiv.org/abs/2610.09239), while cumulative approval deterioration predates agent research. The proposal correctly credits classical selection theory. Its new contribution would be an independently validated subgroup forecast and a controlled change in selection weight, rather than rediscovering a covariance identity or introducing another protective gate. [Bio-creep approval policies](https://arxiv.org/abs/1912.12413)
- **Significance, 4.5/5.** Average-based optimization can undermine the users or conditions for which a system is most needed. A reliable early warning and a measured cost of protection would affect evaluation practice across agent applications. This is one of the two most consequential questions in the set.
- **Technical soundness, 3.5/5.** The Gaussian one-step law is correct under the stated model. Independent guard evaluation, separation of group weight from group sample size, frozen-candidate rescoring and fresh gate data are good decisions. The difficult leap is from an exact one-step expectation to a generation-50 forecast fitted at generation 10. Six moment coefficients, a small early log and nonstationary proposer behavior make that a substantive hypothesis. Independent guard data do not establish independent additive development noise for candidates adaptively written from development feedback; correlated candidates also complicate the independent best-of-K calculation.
- **Feasibility, 3.0/5.** About five fall-risk people per StaBLE guard or test block cannot support precise subgroup monitoring or certification. The proposal appropriately moves the primary forecast and protective gate to Global-MMLU, but that makes the strongest confirmatory evidence multilingual QA evidence. The full program has hundreds of loops and roughly 121 billion small-model tokens under assumed throughput. The gate can be studied, but its practical value at the chosen margin remains uncertain.

**Specific inferential boundaries:** the zero crossing of the selection term is not generally the zero crossing of total tail drift; the document's equations recognize this, and abstracts and conclusions must preserve it. A guarantee for a pooled low-resource-language group does not guarantee protection for each language. Block-end certification does not protect every intermediate candidate. If the tail is narrowed after a fitting panel reveals no conflict, the finding applies to that development-selected tail rather than automatically to all low-resource languages.

**Principal unresolved issue:** does the early covariance log forecast later outcomes better than a simpler tail trajectory, under real nonstationary search?

**Best first experiment:** use one loop family, a fixed predefined language group and independent candidate halves to test the weight-dependent response. Then freeze the generation-10 forecast and compare it with extrapolation on held-out runs. If only local prediction works, publish a monitoring result and defer the long-horizon claim.

**Judgment:** high priority for significance, with most of its scientific value concentrated in the prospective forecast rather than the protective-rule catalog.

**7. Learning how to display tool outputs**

[Proposal](07-learning-how-to-look-at-tool-outputs.md)

**What deserves credit.** Predicting which readers benefit from a newly optimized display is more distinctive than improving one VLM's accuracy. Separating numerical computation from presentation, and testing transfer to readers that never supplied fitness, are strong design choices.

- **Novelty, 4.0/5.** [Plots Unlock Time-Series Understanding](https://arxiv.org/abs/2410.02637) already establishes advantages of plotted inputs; [graphical-perception experiments](https://arxiv.org/abs/2504.04221) already compare models with people; and [Toward a Machine Bertin](https://arxiv.org/abs/2602.01527) explicitly motivates machine-oriented visual design. The prospective mapping from a reader's perception profile to its gains on evolved renderers is the distinctive contribution. The Bayes-risk identity and private-dialect hypothesis draw on established principles and should not carry the novelty claim alone.
- **Significance, 4.0/5.** A transferable display-design rule could reduce repeated model-specific optimization and help make agent evidence readable by people. Its impact would extend beyond biomechanics if it predicts performance on genuinely different tasks and reader families. If it only ranks a fixed set of models on one plot grammar, its impact is narrower.
- **Technical soundness, 3.0/5.** The risk decomposition is valid under its information assumptions, and the document acknowledges oracle undertraining. However, differences between approximate oracle risks do not identify information loss. The forecast also combines channel errors using heuristic knockout weights and equal division across channels. More concretely, it maps squared relative battery error into downstream MAE with a single scale factor. Even for centered Gaussian errors, MAE scales with standard deviation, not variance; the stated linear conversion therefore needs empirical justification. The predictor is a testable heuristic, not a consequence of the risk identity.
- **Feasibility, 2.5/5.** This is the broadest program: multiple model families, evolutionary code search, approximately 12,400 oracle fits, human studies, co-adaptation and two replication suites. Its estimated 5,430 H100-hours depend on throughput and short oracle-fit assumptions that have not been established. Twelve held-out readers in a handful of families provide limited evidence for reader-level transfer; hundreds of checkpoints do not create hundreds of independent readers.

**Specific repairs needed before execution:**

1. Validate the variance-to-MAE mapping and channel-combination rule on held-out synthetic compositions with known information content. Compare with simple profile similarity and calibrated error models.
2. Test generalization by holding out an entire model family and task, as well as individual readers. Use family-aware uncertainty and permutation schemes for claims beyond the tested roster.
3. Establish the value of profiles using a fixed renderer library before starting expensive evolution. Evolution should create a harder out-of-distribution test, rather than being required to learn whether the battery predicts anything.
4. Defer co-adaptation and the private-dialect study. They introduce a second learning problem and are unnecessary for the primary transfer claim.

The permutation-label control also needs cautious interpretation: an improvement on untouched true labels after permuted-label search is a warning to investigate, not proof of leakage. Label-independent rendering repairs and pretrained priors can occasionally improve a baseline.

**Best first experiment:** apply a small perception battery and a fixed, information-controlled renderer library to a diverse set of readers. Pre-register forecasts for new renderers and held-out families. Proceed to evolutionary search only if profiles predict gains beyond general reader skill and model-family effects.

**Judgment:** an attractive higher-risk direction with a distinctive question, but the present program is too large relative to the evidence supporting its central forecasting model.

**8. Blind analysis for agents**

[Proposal](08-blind-analysis-for-agents.md)

**What deserves credit.** The strongest insight is the distinction between a reversible context-dependent transformation and lost decision-relevant information. Coupling that distinction to a randomized path/report factorial is more informative than showing that referrals change answers.

- **Novelty, 4.0/5.** Context-steered analysis, blinding and stage-resolved agent bias already have close precedents: [The Agentic Garden of Forking Paths](https://arxiv.org/abs/2607.01507), [Epistemic Blinding](https://arxiv.org/abs/2604.06013) and [Cognitive Bias Signatures](https://arxiv.org/abs/2611.05720). Replay-based correction also exists in [Inference after coding agents](https://arxiv.org/abs/2611.23174). The distinctive combination is interventional localization of continuous-measurement effects, recoverability controls and downstream decision scoring. Generic mediation and the information-loss identity are established foundations.
- **Significance, 4.5/5.** The proposal addresses a practically important failure: a measurement can become more accurate against its target while becoming misleading evidence for a downstream user who already knows the context. Establishing when recalibration suffices and when measurement-stage blinding helps would change agent interface design. Evidence would initially concern the specified simulated combiner, rather than actual clinician behavior.
- **Technical soundness, 4.0/5.** The Gaussian calculation is sound for the specified blind-trained combiner and conditional-independence assumptions. The entropy identity correctly permits context to add information as well as destroy it. The four-cell design, both decomposition orderings, stateless report stage, self-splice controls and scripted reversible/lossy agents are strong. The largest unresolved issue is empirical recoverability: failure of a kernel-density combiner on limited development data cannot establish irreversible information loss. The proposal appropriately qualifies this claim, but its strongest interpretation still needs stronger comparator evidence.
- **Feasibility, 3.0/5.** A fixed-agent framing and splice pilot is manageable with cached tools. The complete study adds three optimizer families, training, multiple audit arms and an echocardiography replication. The document correctly recognizes that 43 StaBLE test people cannot support its small decision-loss contrast. EchoNet offers a much larger annotated video dataset, but creates a separate tool-validation and domain-engineering task; its existence alone does not establish a comparable effect size. [EchoNet-Dynamic](https://echonet.github.io/dynamic/)

**Specific repairs needed before execution:**

1. Compare several well-tuned context-aware combiners, including a joint discriminative model using the report and referral, with matched training budgets and learning curves. Compare the value of access to the full transcript as well. State residual penalties as failures of the tested recovery methods unless stronger identification is available.
2. Strengthen the measurement gate. A slope above 0.3 does not by itself imply useful precision or performance above a simple baseline: a highly noisy unbiased measurement can have slope near one. Add a preregistered accuracy or skill requirement suitable for the target.
3. Fix route classifications using development data. Preserve all-agent results because excluding failed placebos or low-support cross-splices can preferentially remove the most context-sensitive paths. EchoNet's proposed separate classification pool is a good model for this separation.
4. Keep the optimizer comparison secondary. Prompt evolution versus GRPO differs in update surface and feedback, so observed differences identify the tested configurations rather than a general optimizer mechanism.

**Principal unresolved issue:** do real path changes lose useful information after strong, adequately trained context-aware recalibration, or is the apparent advantage of blinding mostly a combiner estimation problem?

**Best first experiment:** gate one fixed agent, randomize two referrals, recover all four splice cells and validate the scripted reversible and lossy controls. Test flexible recalibration on untouched cases. Only after a residual decision penalty appears should the project fund self-improvement loops and a large EchoNet confirmation.

**Judgment:** the strongest overall scientific opportunity, provided the paper centers on recoverability and controlled path effects rather than a broad claim that context or nonblinded analysis is inherently harmful.

**Issues that affect the whole portfolio**

**Independent evidence is the limiting resource.** BioCV's 15 people, StaBLE's small fall-risk subgroup, three long-loop base harnesses and twelve held-out VLMs are different statistical bottlenecks. More clips, edit attempts, seeds or checkpoints can improve conditional precision but cannot substitute for new people, harness families, model families or software implementations.

**Reference agreement must remain distinct from physical accuracy.** Proposals 1 and 4 make this issue explicit. The newer proposals also rely heavily on multi-camera OpenCap or derived StaBLE scores. Those are useful operational targets, but agreement with them does not establish independent physical validity. Different proposals using the same reference do not provide independent confirmation of the reference.

**Prior exposure to test results limits confirmation.** The newer proposals disclose reuse of the pilot's 43-person test cohort. That is preferable to concealing the history, but aggregate pilot results can still influence research design. These experiments should be described as new tests on a previously examined cohort; fresh participants or an independently untouched domain are stronger confirmation. Across proposals, incompatible development/guard/test rotations also require a shared data-use ledger if findings from one project will guide another.

**Small effects, nulls and failures need different language.** Failure to reject zero does not establish equivalence, and a forecast missing a point-estimate threshold does not necessarily refute the underlying mechanism. Several hypothesis tables currently use “falsified” for underpowered or inconclusive outcomes. Register separate criteria for positive support, practically meaningful equivalence and unresolved uncertainty.

**Budgets are planning assumptions.** Report prefill, decoding, vision encoding, batching, CPU work and API calls separately. Token totals divided by an aggregate throughput do not establish wall-clock feasibility for dependent agent loops. Benchmark a complete representative evaluation unit before committing to the full factorial. Proposal 5 illustrates why GPU-hours alone can hide a large CPU burden.

**Do not run every extension before resolving the central question.** Proposals 5 to 8 each contain material for multiple papers. A smaller decisive experiment is more valuable than a large collection of secondary results that leaves the primary mechanism uncertain. Human studies, multiple optimizers, private-dialect learning and additional protective gates should follow evidence that their core premise holds.

**Suggested first-investment order**

| Purpose | First choice | Evidence required before expansion |
|---|---|---|
| Most consequential scientific result | 8 | Valid splicing and a residual penalty after strong recalibration |
| Most tractable evaluation project | 3 | Substantial replay cost remains after exact reuse; trace features improve selection |
| Shared measurement foundation | 1 | A real instrument-backed ranking reversal robust to timing uncertainty |
| Subgroup monitoring and protection | 6 | Prospective forecasts beat trajectory extrapolation on independent runs |
| Higher-risk conceptual exploration | 7 | Profiles predict transfer on fixed renderers and held-out model families |
| Harness-design study | 5 | Behavior-matched representation effects survive matched feedback and updated baselines |
| Paired-measurement extension | 4 | Stable covariance changes acquisition choices beyond static paired selection |
| Calibration extension | 2 | Structured transfer beats conventional active calibration on real replacements |

This is an investment sequence, not a ranking by a hidden aggregate score. For a short project, 3 can reasonably precede 8. For a biomechanics-first program, the reference-validity panel in 1 should precede claims of physical improvement from the newer proposals.

**Assessment checks and limits**

The review read all eight proposals, the overview, the local literature synthesis and review records, and relevant pilot/theory notes. It spot-checked primary literature through arXiv, proceedings pages, author manuscripts and official dataset pages, including additional close work for proposal 5. This was targeted novelty checking, not an exhaustive systematic review; absence of a matching paper in this search does not prove priority. Several recent sources are preprints.

Independent arithmetic checks confirmed proposal 1's squared-loss identity and 0.75 crossing, proposal 2's 7.5 ms uninformative-probe regret, proposal 3's unbiased mean and variance by exhaustive enumeration of a small audit design, proposal 4's 5/9 crossover, and proposal 5's binomial loop formula. The checks also reproduced the 135-item lower-count calculation for proposal 6's stated simple gate boundary and approximately 38% Fisher-approximation power for proposal 7's correlation of 0.5 with twelve independent readers. These checks validate the stated simplified calculations, not the empirical assumptions needed to apply them.

The earlier simulation outputs are model checks, not observations of real agent behavior; the entire existing simulation suite was not rerun. No raw clinical-data experiment, model training, benchmark run or throughput measurement was performed for this assessment. The StaBLE manuscript DOI could not be retrieved through the browsing tool in this pass, so its participant and pilot claims were treated as proposal-reported rather than independently revalidated. BioCV's participant count and access conditions, and EchoNet's dataset description, were checked against their official pages.
