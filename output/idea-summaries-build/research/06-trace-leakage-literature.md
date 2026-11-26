# P06 Trace Leakage: literature and novelty check

Checked on 2026-11-24. Every link in this report was fetched once (arXiv abstract page, proceedings page or journal page) unless it is marked UNVERIFIED or "listing only". Numbers quoted from papers come from the abstract page or from a targeted read of the HTML version; where a number came from a search-engine summary and was not seen on the paper page, the text says so.

## 1. The idea under review

P06 asks what happens when a reflective optimizer (GEPA, Meta-Harness, TextGrad, ACE, or a Darwin Goedel Machine style archive search) reads per-example execution traces from the same examples it then uses to decide which candidate harness is best. Two terms carry the argument.

- **Selection set.** The labeled examples whose scores decide which candidate is kept. In GEPA this is D_pareto; in Meta-Harness it is the "search set".
- **Optimism.** The measured gain on the selection set minus the gain on people the optimizer never touched. A gain of 0.05 MAE on the selection set that becomes 0.02 on fresh people has optimism 0.03 and a transfer ratio of 0.4.

The proposal claims that trace access opens a second route for optimism on top of the ordinary winner's curse of picking the best of many noisy candidates. A proposer that sees "participant 112, tandem stance, predicted 2.1, label 3.0, CoM sway trace attached" can write a rule that fixes that one example, and if participant 112 is also in the selection set, the rule is rewarded. P06 wants to measure how much of the reported improvement is of this kind, how it scales with selection-set size n, number of iterations T and feedback richness, and which protocol (separate diagnose, select and test pools; reusable holdout or Ladder; traces aggregated over k examples; added noise) recovers honest improvement. The planned design has a feedback-channel ladder at matched budget, a null-label test in which labels are permuted (in the spirit of Zhang et al. 2017), and a sweep over n.

## 2. Search log

Twenty-six searches were run; the ones that changed the picture are listed with what they returned.

| # | Query (abridged) | What it surfaced |
|---|---|---|
| 1 | GEPA reflective prompt evolution | GEPA, arXiv 2507.19457, ICLR 2026 oral |
| 2 | prompt optimization overfitting validation set generalization gap | TextReg 2605.21318; Bertran, Roth, Wu 2606.11045; Madras et al. 2510.08413; OPRO |
| 3 | Meta-Harness held-out | Meta-Harness 2603.28052 and its feedback-interface ablation |
| 4 | overtuning hyperparameter optimization | Schneider, Bischl, Feurer 2506.19540 |
| 5 | benchmark overfitting self-improving agents, DGM | DGM 2505.22954 |
| 6 | prompt optimizers overfit small validation set, GEPA MIPROv2, 2026 | practitioner blogs only (not cited as evidence) |
| 7 | LLM optimizer memorizes training examples in prompt | practitioner reports (orq.ai, Evidently); no primary study |
| 8 | adaptive overfitting leaderboard, reusable holdout, Ladder, LLM | Blum and Hardt 2015; Bertran et al. 2026 |
| 9 | Akinwande prompt engineering rethinking generalization | ICLR 2024 PAC-Bayes paper |
| 10 | Agentic Context Engineering | ACE 2510.04618 |
| 11 | system prompt optimization error analysis overfitting | ETGPO 2602.00997; state-space search 2511.18619; ReASearch 2608.06714 |
| 12 | prompt optimization random or shuffled labels memorization | nothing applying a null-label test to an LLM optimizer |
| 13 | self-improving agent overfits validation tasks, ADAS, AFlow | Harnesses That Improve Themselves 2611.22299; pointer to RRSI |
| 14 | Huxley-Goedel Machine | HGM 2510.21614 |
| 15 | Google regularized recursive self-improvement harness overfitting | RRSI 2609.24972 |
| 16 | Feldman Frostig Hardt multiple classes test set reuse | ICML 2019 paper |
| 17 | benchmarking prompt optimizers, held-out, validation reuse, systematic | Lumer et al. 2610.12601; Chen 2611.22605; Mitra and Mahmud 2610.19084 |
| 18 | reflective optimizer feedback with ground-truth labels, leakage, richness ablation | Lumer et al. verifier ablation; CMVF 2607.24354 |
| 19 | reusable holdout or Thresholdout in prompt optimization or agent self-improvement | CRISP 2611.20156 |
| 20 | separate reflection examples from selection examples, disjoint ablation | Zhou and Cheng 2609.32452; Zhou and Cheng 2610.27367; NPO 2608.27266 |
| 21 | Rademacher complexity, LLM optimizer, random labels | nothing for LLM optimizers |
| 22 | Guess and Check, Rogers et al. | AISTATS 2020 paper |
| 23 | Saeb subject-wise vs record-wise cross-validation | GigaScience 2017 |
| 24 | Leaderboard Illusion | arXiv 2504.20879 |
| 25 | IFBench; AppWorld; Qwen3-VL | candidate second-domain benchmarks and model report |
| 26 | Mania model similarity test set overuse | NeurIPS 2019 paper |

The main lesson of the search is that the period from June to November 2026 produced at least six papers that measure validation-to-test gaps in reflective prompt or harness optimization. The phenomenon P06 starts from is therefore documented. What none of them does is separate the two routes to optimism, test an optimizer against labels that carry no signal, or sweep n and feedback bandwidth in a controlled way.

## 3. Closest prior work

### 3.1 Lumer et al. 2026: a topic-disjoint protocol for GEPA on a deep-research agent

- **Reference.** Elias Lumer, Sahil Sen, Vamse Kumar Subbiah, Kevin Paul. "Reflective Prompt Optimization of a Deep-Research Agent: A Topic-Disjoint, Multi-Seed Protocol for Measuring Transferable Gains and Prompt-Level Overfitting." arXiv 2610.12601, October 2026. https://arxiv.org/abs/2610.12601
- **What they did.** They ran GEPA (240 metric calls, reflection minibatch of 3, Pareto selection) on the two system prompts of a multi-agent research agent, with train, validation and test split by topic (24, 24 and 500 tasks). Held-out citation reward rose by 0.079 (0.702 to 0.781, bootstrap CI 0.051 to 0.107) while the validation gain was 0.202. A verifier ablation found that decomposed per-dimension feedback gave held-out transfer of +0.075, whereas collapsing feedback to one scalar gave -0.021. About half of the winning prompt was a memorized answer key, yet an ablation showed the key earned no reward, even on the training questions it encoded. The authors attribute the validation minus held-out gap to small-sample selection under a noisy judge.
- **Overlap with P06.** High. It measures optimism for a reflective optimizer, varies feedback richness, and asks whether memorized content explains the gap.
- **What remains open.** One system, one optimizer, two seeds per ablation cell. Validation size and iteration count are never varied (the authors list a larger validation set and a selection penalty as untested remedies). There is no null-label test and no reusable-holdout or Ladder arm. Its finding that richer feedback helps transfer runs against the naive form of P06's hypothesis, and P06 has to engage with it.

### 3.2 Chen 2026: generate-and-select as an audit control for prompt optimizers

- **Reference.** Bohe Chen. "Simplicity Goes Far: Auditing Prompt Optimizers with Demonstration-Conditioned Prompt Search." arXiv 2611.22605, November 2026. https://arxiv.org/abs/2611.22605
- **What they did.** They proposed DCPS, a control that samples candidate prompts from a frozen generator conditioned on random demonstrations and keeps the one with the best validation score, with no reflection or evolution. On DSPy programs with GPT-4.1-mini it matches GEPA's macro accuracy with 55% fewer rollouts. Their Table 4 reports large validation-to-test drops after selection: IFBench 96.7 to 51.5 (GPT-4.1-mini) and 88.3 to 43.9 (Qwen3-8B); AIME-2025 80.0 to 48.0 (GPT-4.1-mini). On LiveBench-Math, more rollouts raised validation accuracy and lowered held-out accuracy in single-seed runs. They call this "a winner's-curse effect shared by any validation-selection method, including GEPA" and note the gap is largest when the validation subset is small.
- **Overlap with P06.** High on the scaling-with-n and scaling-with-budget questions, and DCPS is the natural zero-trace control P06 needs.
- **What remains open.** The gap versus subset size is read off across tasks, not from a controlled sweep. Because DCPS and GEPA are compared on accuracy, the paper does not ask whether GEPA's optimism exceeds DCPS's at matched candidate count, which is the comparison that isolates trace content from selection.

### 3.3 Bertran, Roth, Wu 2026: compression, Ladder feedback and validation overfitting in research agents

- **Reference.** Martin Andres Bertran, Aaron Roth, Zhiwei Steven Wu. "What Fits (Into Few Tokens) Doesn't Overfit: Compression and Generalization in ML Research Agents." arXiv 2606.11045, June 2026. https://arxiv.org/abs/2606.11045
- **What they did.** Claude Opus agents driven by Claude Code searched for strong models on 8 datasets (Folktables, gene expression, SST-2, CIFAR-10, CIFAR-100 diffusion, ImageNet-1K, an HH-RLHF reward model, WikiText-103). Two bottlenecks were imposed: a reproducer agent had to recover the explorer's result from a 32 or 64 token prompt, and in a separate arm the explorer saw only one-bit Ladder feedback. Neither bottleneck hurt much, and observed validation-holdout gaps (0.0 to 1.9 points) stayed inside their description-length and Ladder bounds. They then induced overfitting with an aggressive prompt, full sample-level validation access, smaller validation sets or injected label noise; 38 of 102 checkpoints then showed more than 10% relative gap, and failure to reproduce from a 128-token prompt flagged all 38 (6 false alarms among 64 others).
- **Overlap with P06.** High on theory and protocol: one-bit Ladder feedback, label noise that rewards memorization, and a bound linking description length of the solution to the gap, |R_hat - R| <= sqrt(((B+1) ln|V| + ln(2/delta)) / 2n) with B the token budget.
- **What remains open.** The agents train models; they are not reflective optimizers rewriting a harness from per-example traces. Sample-level access appears only inside the stress test, where it is one of several levers pulled at once, so its separate effect is not identified. Label noise is used to induce overfitting, not as a calibrated null to measure an optimizer's capacity. No reflective optimizer (GEPA, TextGrad, ACE, Meta-Harness) is studied.

### 3.4 Zhou and Cheng 2026: what the reflector should see

- **Reference.** Xiaofan Zhou, Lu Cheng. "What Should the Reflector See? An Empirical Study of Evidence in Reflective Prompt Optimization." arXiv 2609.32452, September 2026. https://arxiv.org/abs/2609.32452
- **What they did.** With Qwen3.5-9B as both task model and reflector, they compared nine reflection strategies on five datasets, varying evidence composition (failures only, balanced mix, no examples), example visibility, candidate selection and domain-knowledge policy. Failures-only gave the largest mean test gain (+8.0 points). The no-examples strategy was best at improving sampled parents but gained only 1.4 points on test. Calibration-to-test gaps were larger on GPQA and IFBench, and the authors describe the gap as descriptive rather than a direct overfitting measure.
- **Overlap with P06.** Medium to high: this is a feedback-content ablation with a calibration-versus-test gap.
- **What remains open.** One model, one search scheme. The axis is which examples are shown, not whether they overlap with the selection set. There is no matched-budget channel ladder, no null labels and no sweep over n.

### 3.5 Xia et al. 2026: RRSI, regularized recursive self-improvement of harnesses

- **Reference.** Peng Xia, Rujun Han, Zifeng Wang, Yanfei Chen, Yufan Zhuang, Yoonho Lee, et al. (14 authors, Google). "RRSI: Regularized Recursive Self-Improvement of Agent Harnesses." arXiv 2609.24972, September 2026 (v3 October 2026). https://arxiv.org/abs/2609.24972
- **What they did.** They argue that harness evolution can overfit by "memorizing the training tasks", giving large in-distribution gains that shrink or vanish out of distribution. RRSI adds an annealed edit budget to the proposer and a critic plus pruner to the selector. Across eight benchmarks the abstract reports up to 6.0 points on the evolution split and up to 4.3 points on five out-of-distribution benchmarks, with about 30% fewer policy tokens.
- **Overlap with P06.** Medium: same failure mode at harness level, with a regularization remedy.
- **What remains open.** The overfitting is attributed to recursive evolution in general; the paper does not test whether reading traces from the selection split is the cause, and does not compare statistical protocols (disjoint pools, Ladder, reusable holdout) against its regularizers. RRSI is a strong baseline for P06's protocol arm.

### 3.6 Lee et al. 2026: Meta-Harness

- **Reference.** Yoonho Lee, Roshen Nair, Qizheng Zhang, Kangwook Lee, Omar Khattab, Chelsea Finn. "Meta-Harness: End-to-End Optimization of Model Harnesses." arXiv 2603.28052, March 2026. https://arxiv.org/abs/2603.28052
- **What they did.** A Claude Code proposer reads the source, scores and raw execution traces of every earlier candidate from a filesystem and writes new harness code. Their Table 3 (online text classification) compares proposer interfaces: scores only (median 34.6, best 41.3), scores plus summary (34.9, 38.7), full traces (50.0, 56.7). The table is not labeled by split; since the proposer sees only search-set feedback, these look like search-set numbers. Test sets for classification and math were held out until the end ("The proposer never sees test-set results"), but on TerminalBench-2 search and final evaluation used the same 89 tasks.
- **Overlap with P06.** High on the channel ladder. Meta-Harness is the clearest case of an optimizer that reads traces from the very examples it selects on.
- **What remains open.** The interface ablation is reported where it is most exposed to optimism. Nobody has rerun it with the selection-minus-fresh gap as the outcome, with matched candidate counts, or with null labels.

### 3.7 Agrawal et al. 2025: GEPA

- **Reference.** Lakshya A Agrawal, Shangyin Tan, Dilara Soylu, Noah Ziems, Rishi Khare, Krista Opsahl-Ong, et al. (17 authors). "GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning." arXiv 2507.19457, ICLR 2026 (oral). https://arxiv.org/abs/2507.19457
- **What they did.** GEPA samples trajectories, reflects on them in natural language and keeps a Pareto frontier of candidates. It splits D_train into D_feedback (minibatches for reflection) and D_pareto (selection). The frontier is per instance: "For each training instance, GEPA records the highest score across all candidates", and candidates that are best on at least one instance survive. It reports beating GRPO by 6% on average with up to 35 times fewer rollouts, and beating MIPROv2 by more than 10%. The paper states that reflectively evolved instructions show a lower generalization gap (validation minus test) than few-shot demonstration optimization (its Figure 16).
- **Overlap with P06.** GEPA already implements a diagnose/select split by default, so that arm of P06 is the status quo and cannot count as a proposed remedy. Its per-instance Pareto selection is itself a per-example channel into selection, even when reflection never reads D_pareto traces.
- **What remains open.** The "lower generalization gap" claim compares GEPA with demonstration optimizers, not with a scalar-only control at matched candidate count; it does not separate selection from trace content.

### 3.8 Mitra and Mahmud 2026: item-level transitions

- **Reference.** Chinmoy Mitra, Tarek Mahmud. "Beyond Aggregate Accuracy: Item-Level Transitions in Prompt Optimization." arXiv 2610.19084, October 2026. https://arxiv.org/abs/2610.19084
- **What they did.** They tracked recoveries, regressions and churn per item across five benchmarks with a GPT-5 optimizer and GPT-4o-mini or GPT-4.1 Mini solvers. In five of nine configurations churn was at least five times the net change. Average validation gains were 7.9 points against 5.2 on held-out tests.
- **Overlap with P06.** Medium: one more measured gap, plus churn as a metric P06 should adopt.
- **What remains open.** No causal attribution of the gap.

### 3.9 Jawad et al. 2026: risk-certified prompt optimization with a reusable holdout

- **Reference.** Hussein Jawad, Alexandre Landeau, Guy Fleury Iradukunda, Paul Beaumont, Theodore Rezel, Sofiane Schaack, Nicolas J-B. Brunel. "Risk-certified prompt optimization for LLM-as-a-judge guardrails." arXiv 2611.20156, November 2026. https://arxiv.org/abs/2611.20156
- **What they did.** CPS certifies a fixed pool of prompts on held-out data with simultaneous upper confidence bounds; CRISP runs an adaptive search that uses a reusable-holdout interface so that risk feedback can steer generation without voiding the guarantee.
- **Overlap with P06.** Medium: the first use I found of reusable-holdout machinery inside an LLM prompt search.
- **What remains open.** The goal is a risk constraint for guardrail judges, not measuring or reducing optimism in general harness search.

### 3.10 Fu et al. 2026: TextReg

- **Reference.** Lucheng Fu, Ye Yu, Yiyang Wang, Yiqiao Jin, Haibo Jin, B. Aditya Prakash, Haohan Wang. "TextReg: Mitigating Prompt Distributional Overfitting via Regularized Text-Space Optimization." arXiv 2605.21318, May 2026. https://arxiv.org/abs/2605.21318
- **What they did.** They name "prompt distributional overfitting" (prompts grow and pick up sample-specific rules) and regularize text-space updates, reporting up to +11.8% out-of-distribution accuracy over TextGrad and +16.5% over REVOLVE.
- **Overlap with P06.** Medium: the mechanism (sample-specific rules) is the content route P06 cares about.
- **What remains open.** The target is distribution shift, not in-distribution selection optimism; no protocol comparison.

### 3.11 Schneider, Bischl, Feurer 2025: overtuning in hyperparameter optimization

- **Reference.** Lennart Schneider, Bernd Bischl, Matthias Feurer. "Overtuning in Hyperparameter Optimization." AutoML 2025, arXiv 2506.19540. https://arxiv.org/abs/2506.19540
- **What they did.** Reanalyzing HPO benchmark data, they found that in about 10% of cases the configuration selected on validation generalizes worse than the default or first configuration.
- **Overlap with P06.** The scalar-feedback ancestor of P06; it supplies the definition and the recommendation of resampling.
- **What remains open.** HPO proposers do not read per-example traces.

### 3.12 Akinwande et al. 2024 and Madras et al. 2025: PAC-Bayes bounds for prompts

- **References.** Victor Akinwande, Yiding Jiang, Dylan Sam, J. Zico Kolter. "Understanding prompt engineering may not require rethinking generalization." ICLR 2024, arXiv 2310.03957. https://arxiv.org/abs/2310.03957. David Madras, Joshua Safyan, Qiuyi Zhang. "Prompts Generalize with Low Data: Non-vacuous Generalization Bounds for Optimizing Prompts with More Informative Priors." arXiv 2510.08413 (ICML 2025 workshop). https://arxiv.org/abs/2510.08413
- **What they did.** Discrete prompts with a language-model prior give PAC-Bayes bounds within a few points of test error on ImageNet; perplexity priors keep bounds non-vacuous with little data.
- **Overlap with P06.** These explain why prompts often do not overfit. The Akinwande title already plays on Zhang et al. 2017, so P06's null-label test should cite it as the reason a positive result would be surprising.
- **What remains open.** Bounds are for prompt search with scalar scores; they do not model a proposer that reads traces from the selection set.

### 3.13 Classical adaptive data analysis that P06 builds on

| Work | Main point for P06 |
|---|---|
| Dwork et al. 2015, Science 349:636 (reusable holdout, Thresholdout) and NeurIPS 2015 (arXiv 1506.02629) | Holdout reuse with guarantees via differential privacy and description length |
| Blum and Hardt 2015, ICML (Ladder) | Release only "beats running best" to keep a leaderboard honest |
| Russo and Zou 2016, AISTATS | Bias of adaptively selected estimates is bounded by mutual information between the selection and the data |
| Rogers et al. 2020, AISTATS (Guess and Check) | Instance-specific valid confidence intervals for heuristic adaptive analysis, tighter than worst-case bounds |
| Feldman, Frostig, Hardt 2019, ICML | Bias from test reuse shrinks with the number of classes |
| Mania et al. 2019, NeurIPS | Similar candidate models reduce effective overfitting |
| Recht et al. 2019, ICML | New test sets show 3 to 15% (CIFAR-10) and 11 to 14% (ImageNet) drops, mostly not from adaptivity |
| Roelofs et al. 2019, NeurIPS | Across about 120 Kaggle competitions, little evidence of substantial adaptive overfitting |
| Cawley and Talbot 2010, JMLR | Variance of the selection criterion causes selection overfitting, comparable to differences between algorithms |
| Saeb et al. 2017, GigaScience | Record-wise splits inflate accuracy relative to subject-wise splits in smartphone and wearable studies |

The tension between Roelofs et al. (little adaptive overfitting in practice) and the recent LLM-optimizer gaps (up to 45 points on IFBench in Chen 2026) is the most interesting fact in this literature. The classical explanation for benign reuse is that analysts submit few, similar, low-information models. A reflective optimizer breaks all three assumptions at once: it proposes many candidates, reads high-bandwidth per-example evidence, and can write example-specific code. P06 is best framed as testing which of these broken assumptions matters.

## 4. Is the core idea already done?

**Partially.** The existence of selection-set optimism in reflective optimizers is established by Lumer et al. 2026, Chen 2026, Mitra and Mahmud 2026, Zhou and Cheng 2026 and RRSI. A coarse version of the channel ladder exists (Meta-Harness Table 3 on the search set; Lumer et al. scalar versus decomposed feedback on held-out topics; Zhou and Cheng on evidence composition; Bertran et al. one-bit versus scalar for research agents). GEPA already separates the reflection pool from the selection pool by default, and Ladder and reusable-holdout interfaces have each been tried once in an LLM search (Bertran et al.; Jawad et al.).

Two findings cut against the naive form of P06. Meta-Harness and Lumer et al. both find that richer per-example feedback improves results, and Lumer et al. find that memorized answer content earns no reward and that the gap comes from selection noise. A paper that only shows "rich traces cause leakage" would be contradicted by the closest prior work unless it explains why.

**Residual gap.** No paper does the following, and together these define a publishable contribution.

1. **Separate the two routes at matched candidate count.** Optimism from picking the best of K candidates exists with zero trace access (DCPS in Chen 2026 is that arm). Optimism from trace content is whatever is left after subtracting the matched-K selection term. No study crosses trace source (selection set versus a disjoint diagnose pool) with feedback channel while holding K and rollouts fixed.
2. **A null-label capacity test for LLM optimizers.** Fix a random permutation of labels once (so that labels are memorizable but carry no signal), run each optimizer, and measure the selection-set gain. Under null labels the true gain is zero by construction, so the selection gain is pure optimism. This gives an empirical capacity for each optimizer and channel, analogous to Zhang et al. 2017 for networks. Search 12 and 21 found no such test for any LLM optimizer; Bertran et al.'s label-noise lever is the closest relative and is used to induce overfitting in research agents, not to calibrate it.
3. **Controlled scaling in n, T and feedback bandwidth** across optimizer families, with a fitted law. Chen's subset-size observation is cross-task and single-seed.
4. **Clustered units.** All prior LLM-optimizer studies treat examples as independent. In StaBLE, 18 tasks and 3 phones share one person, so the effective sample size is people, and a trace about one trial of a person informs the other 53 recordings of that person. The record-wise versus person-wise inflation documented by Saeb et al. 2017 has not been measured for optimizers.
5. **Protocol comparison at matched label budget.** For a fixed number of labeled people, is it better to enlarge the selection pool, carve out a disjoint diagnose pool, route selection through a Ladder or Guess and Check, aggregate traces over k examples, or add noise? Nobody reports "honest improvement per labeled person" across these.
6. **Continuous clinical targets and multimodal tool-using agents.** Every prior study uses text tasks with accuracy or judge scores.

The nearest high-value open question is therefore: *how much of a reflective optimizer's measured gain is optimism, can it be estimated without a fresh test set by a null-label audit, and does it scale with the description length of the edits the optimizer makes, as Bertran et al.'s bound predicts, rather than with the bandwidth of the feedback it reads?*

## 5. Scores (demanding ICML area chair)

- **Novelty: 2.5 out of 5 as currently stated.** The gap, its dependence on validation size, the effect of feedback richness and two of the protocols have all appeared in 2026 papers. A reviewer who knows Lumer et al., Chen and Bertran et al. will read the stated version as a larger replication. With the sharpenings below (matched-K decomposition, null-label audit as an estimator, description-length scaling law, clustered units), novelty rises to about 3.5. It is hard to see this direction reaching 4.5 unless the description-length law holds across optimizer families and the null-label audit predicts fresh-person optimism well enough to replace a test set.
- **Significance: 3.5 out of 5.** GEPA, DSPy, ACE and Meta-Harness style search are in wide use, and the field is reporting gains on small selection sets (24 validation tasks in Lumer et al.). An audit that tells practitioners how much of a gain to discount, and which protocol to run, would be used. The ceiling is set by the fact that evaluation-methodology papers are valued for surprising laws; Recht et al. 2019 and Roelofs et al. 2019 are the bar, and both owe their impact to a clear, general empirical regularity.

## 6. Sharpenings

### 6.1 One-line thesis

Reflective optimizers overfit their selection set through two separable channels, selection among many candidates and example-specific content read from traces, and a null-label audit run alongside the search estimates the total optimism to within a stated error without touching fresh people.

### 6.2 The decisive experiment: matched-K null-label factorial

Hold the proposer model, temperature, number of candidates K and total rollouts fixed. Vary three factors and measure optimism on fresh people.

- **Channel (what the proposer reads).** C0: nothing (DCPS-style generate-and-select, zero bits from data to proposer). C1: one bit per candidate (Ladder). C2: aggregate score. C3: per-example scores. C4: per-example scores plus outputs. C5: C4 plus reference labels. C6: full execution traces (tool calls, intermediate arrays, plots) plus labels.
- **Trace source.** S: traces drawn from the selection people. D: traces drawn from a disjoint diagnose pool of people. R: traces from other recordings (other tasks or phones) of the selection people, which is the record-wise arm.
- **Labels.** True labels versus a fixed within-task permutation of balance scores across people, drawn once and frozen for the whole run.

Estimands, with person-level bootstrap intervals:
- O_total = (gain on selection people) minus (gain on fresh people).
- O_select = O_total in C0 at the same K. This is the winner's-curse term.
- O_content = O_total(Ck, S) minus O_total(C0). This is the trace-content term.
- O_null(Ck, source) = selection-set gain under permuted labels. The fresh-person gain under null labels must be zero, which serves as a sanity check.

Predictions that would make the paper: O_content is positive for C5 and C6 with source S and near zero with source D; source R sits between them (identity leakage); O_null(Ck, S) tracks O_total(Ck, S) under true labels closely enough that it can be used as a plug-in correction; both scale as roughly sqrt(L / n_people), where L is the token length of the shortest reproducer of the final harness diff (Bertran et al.'s reproducer test), and not with the raw size of the traces the proposer read.

A reduced design that keeps the decisive contrasts: channels {C0, C2, C4, C6}, sources {S, D}, labels {true, null}, n_select in {16, 64} people, 3 seeds, which is 96 runs per optimizer. Add R and the full channel ladder only for GEPA.

### 6.3 Essential controls

- Matched K and matched rollouts across channels; C0 is non-negotiable, since without it any gap can be blamed on selection.
- Null labels must be fixed for the run, not resampled per iteration, or they cannot be memorized and the test loses power.
- Identity scrubbing: strip participant IDs, filenames and timestamps from traces in one arm, so a person-specific rule has to be learned from signal content rather than an identifier.
- A verbatim-leak detector: n-gram and numeric-constant overlap between the final harness and the traces the proposer saw (for example, a threshold equal to one participant's sway value).
- Fresh people are never evaluated during search; the 43 StaBLE test people stay sealed, and a second sealed set (BioCV) checks cross-site transfer.
- All three phones and all tasks of one person stay in one pool.
- At least 5 seeds for the headline cells; the two-seed cells in Lumer et al. are the weakness to avoid.

### 6.4 Strongest baselines (named, with links)

- Optimizers under test: GEPA (https://arxiv.org/abs/2507.19457), TextGrad (https://arxiv.org/abs/2406.07496), ACE (https://arxiv.org/abs/2510.04618), Meta-Harness-style filesystem proposer (https://arxiv.org/abs/2603.28052), and a DGM-style archive search (https://arxiv.org/abs/2505.22954). MIPROv2 (https://arxiv.org/abs/2406.11695) as the non-reflective Bayesian optimizer.
- Zero-trace control: DCPS generate-and-select (https://arxiv.org/abs/2611.22605).
- Remedies to beat: RRSI regularized proposer and selector (https://arxiv.org/abs/2609.24972); TextReg (https://arxiv.org/abs/2605.21318); error aggregation into a taxonomy as a k-aggregation baseline, ETGPO (https://arxiv.org/abs/2602.00997) and CMVF (https://arxiv.org/abs/2607.24354).
- Statistical protocols: Ladder (https://proceedings.mlr.press/v37/blum15.html), Thresholdout and reusable holdout (https://arxiv.org/abs/1506.02629), Guess and Check (https://proceedings.mlr.press/v108/rogers20a.html), the CRISP reusable-holdout interface (https://arxiv.org/abs/2611.20156), and repeated k-fold selection as recommended against overtuning (https://arxiv.org/abs/2506.19540).

### 6.5 Models

- Biomechanics task agent: Qwen3-VL-8B (pilot model; report at https://arxiv.org/abs/2511.21631), with Qwen3-VL-32B as a scale check.
- Second-domain task models: Qwen3-8B and GPT-4.1-mini, which match the GEPA and Chen 2026 IFBench settings and let P06 reproduce a known large-gap cell before extending it.
- Proposer or reflector: one open-weight model fixed across all arms (for example Qwen3-235B-A22B) and one frontier model of the kind Meta-Harness uses (a Claude Opus model via Claude Code). Optimism should be reported per proposer, since a stronger proposer may write more example-specific code.

### 6.6 Datasets and environments

- **Biomechanics.** StaBLE (180 participants by 18 balance tasks by 3 phones; code and dataset pointers at https://github.com/stanfordnmbl/stable-analysis). Use the pilot split: 128 training people divided into diagnose and selection pools by person, the 43 test people sealed. Sweep n_select over {8, 16, 32, 64} people. Cache tool outputs (RTMPose keypoints, OpenCap Monocular kinematics, SAM 2 masks) per recording so that a candidate evaluation costs only the agent's language-model calls. BioCV (15 participants with markers and force plates) serves as a sealed cross-site check.
- **Second domain.** IFBench (https://arxiv.org/abs/2507.02833): 58 out-of-distribution verifiable constraints, a GEPA benchmark, and the setting where Chen 2026 saw a 45-point validation-to-test drop. Constraint type plays the role of "person" for grouped splits.
- **Optional agentic third domain.** AppWorld (https://arxiv.org/abs/2407.18901): 750 tool-use tasks over 457 APIs, the ACE setting, with normal and challenge test splits.

### 6.7 Metrics

- Optimism O_total, its decomposition into O_select and O_content, and the transfer ratio (fresh gain over selection gain), each with person-level bootstrap intervals.
- Null-label optimism O_null and its calibration as a predictor of O_total (slope, R squared and coverage of a corrected interval).
- Honest improvement per labeled person for each protocol at a fixed label budget.
- Biomechanics outcome metrics: task-averaged MAE against the clinical score (pilot reference points: frozen Qwen3-VL-8B 0.238, training-task mean 0.120, SFT 0.100), plus Spearman correlation.
- Item churn (Mitra and Mahmud), final harness length, reproducer length L, and verbatim-leak rate.

### 6.8 Falsifier

If, at matched K and rollouts, full traces drawn from the selection people (C6, source S) show no more optimism than the same traces drawn from disjoint people (C6, source D) and no more than the zero-trace control (C0), across both n values and both domains, then trace leakage is not a separate phenomenon: the gap is the classical winner's curse and the only remedy needed is a larger or resampled selection set. A second falsifier targets the audit: if O_null fails to predict O_total (for example R squared below 0.5 across cells), the null-label audit is not a usable estimator and the contribution reduces to a measurement study.

### 6.9 Compute and scope

With tool outputs cached, one StaBLE candidate evaluation on 64 people using 6 of the 18 tasks and one phone is 384 agent calls. At K = 60 candidates this is about 23,000 calls per run; at roughly 2 seconds per batched call on one H100 that is about 13 GPU-hours, so the 96-run reduced design is on the order of 1,000 to 1,500 GPU-hours for the task model, plus proposer API cost. IFBench runs are cheaper per candidate. These are planning estimates, not measurements.

## 7. Key citations

| # | Reference | URL | Claim it supports | Verified |
|---|---|---|---|---|
| 1 | Lumer, E., Sen, S., Subbiah, V. K., Paul, K. (2026). Reflective Prompt Optimization of a Deep-Research Agent: A Topic-Disjoint, Multi-Seed Protocol for Measuring Transferable Gains and Prompt-Level Overfitting. arXiv 2610.12601. | https://arxiv.org/abs/2610.12601 | GEPA validation gain 0.202 vs held-out 0.079; scalar feedback gives negative transfer; memorized answer key earns no reward; gap attributed to selection under noisy judge | yes |
| 2 | Chen, B. (2026). Simplicity Goes Far: Auditing Prompt Optimizers with Demonstration-Conditioned Prompt Search. arXiv 2611.22605. | https://arxiv.org/abs/2611.22605 | Generate-and-select matches GEPA; IFBench 96.7 to 51.5 after selection; winner's curse grows with small validation subsets and more rollouts | yes |
| 3 | Bertran, M. A., Roth, A., Wu, Z. S. (2026). What Fits (Into Few Tokens) Doesn't Overfit: Compression and Generalization in ML Research Agents. arXiv 2606.11045. | https://arxiv.org/abs/2606.11045 | One-bit Ladder feedback suffices; description-length bound on the gap; induced overfitting via sample-level access and label noise; reproducer failure detects overfitting | yes |
| 4 | Zhou, X., Cheng, L. (2026). What Should the Reflector See? An Empirical Study of Evidence in Reflective Prompt Optimization. arXiv 2609.32452. | https://arxiv.org/abs/2609.32452 | Evidence composition changes test gain and calibration-to-test gap; local reflection success does not predict final quality | yes |
| 5 | Xia, P., Han, R., Wang, Z., et al. (2026). RRSI: Regularized Recursive Self-Improvement of Agent Harnesses. arXiv 2609.24972. | https://arxiv.org/abs/2609.24972 | Harness evolution memorizes training tasks; regularized proposer and selector improve out-of-distribution gains | yes |
| 6 | Lee, Y., Nair, R., Zhang, Q., Lee, K., Khattab, O., Finn, C. (2026). Meta-Harness: End-to-End Optimization of Model Harnesses. arXiv 2603.28052. | https://arxiv.org/abs/2603.28052 | Raw traces beat scores-only and summaries (Table 3); proposer reads traces of all prior candidates from the search set; TerminalBench-2 had no held-out split | yes |
| 7 | Agrawal, L. A., Tan, S., Soylu, D., et al. (2025). GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning. ICLR 2026 (oral). arXiv 2507.19457. | https://arxiv.org/abs/2507.19457 | D_feedback/D_pareto split; per-instance Pareto selection; claim of lower generalization gap | yes |
| 8 | Mitra, C., Mahmud, T. (2026). Beyond Aggregate Accuracy: Item-Level Transitions in Prompt Optimization. arXiv 2610.19084. | https://arxiv.org/abs/2610.19084 | Validation gain 7.9 vs held-out 5.2 points; churn often five times the net change | yes |
| 9 | Jawad, H., Landeau, A., Iradukunda, G. F., et al. (2026). Risk-certified prompt optimization for LLM-as-a-judge guardrails. arXiv 2611.20156. | https://arxiv.org/abs/2611.20156 | Reusable-holdout interface used inside an adaptive prompt search | yes |
| 10 | Fu, L., Yu, Y., Wang, Y., et al. (2026). TextReg: Mitigating Prompt Distributional Overfitting via Regularized Text-Space Optimization. arXiv 2605.21318. | https://arxiv.org/abs/2605.21318 | Iterative rewriting accumulates sample-specific rules; regularization improves OOD by up to 11.8 points over TextGrad | yes |
| 11 | Schneider, L., Bischl, B., Feurer, M. (2025). Overtuning in Hyperparameter Optimization. AutoML 2025. arXiv 2506.19540. | https://arxiv.org/abs/2506.19540 | About 10% of HPO runs select a configuration worse than the default; scalar-feedback analogue of P06 | yes |
| 12 | Akinwande, V., Jiang, Y., Sam, D., Kolter, J. Z. (2024). Understanding prompt engineering may not require rethinking generalization. ICLR 2024. | https://arxiv.org/abs/2310.03957 | PAC-Bayes bounds for discrete prompts are tight; prompt search with scalar scores rarely overfits | yes |
| 13 | Madras, D., Safyan, J., Zhang, Q. (2025). Prompts Generalize with Low Data: Non-vacuous Generalization Bounds for Optimizing Prompts with More Informative Priors. arXiv 2510.08413. | https://arxiv.org/abs/2510.08413 | Perplexity priors give non-vacuous bounds in the low-data regime | yes |
| 14 | Zhang, C., Bengio, S., Hardt, M., Recht, B., Vinyals, O. (2017). Understanding deep learning requires rethinking generalization. ICLR 2017. | https://arxiv.org/abs/1611.03530 | Random-label fitting as an empirical capacity test; template for the null-label audit | yes |
| 15 | Dwork, C., Feldman, V., Hardt, M., Pitassi, T., Reingold, O., Roth, A. (2015). The reusable holdout: Preserving validity in adaptive data analysis. Science 349(6248):636-638. doi:10.1126/science.aaa9375 | https://www.science.org/doi/10.1126/science.aaa9375 | Reusable holdout and Thresholdout | listing only (DOI resolves to science.org; page returned 403; citation confirmed on author page https://www.cis.upenn.edu/~aaroth/reusable.html) |
| 16 | Dwork, C., Feldman, V., Hardt, M., Pitassi, T., Reingold, O., Roth, A. (2015). Generalization in Adaptive Data Analysis and Holdout Reuse. NeurIPS 2015. arXiv 1506.02629. | https://arxiv.org/abs/1506.02629 | Description-length and max-information routes to valid holdout reuse | yes |
| 17 | Blum, A., Hardt, M. (2015). The Ladder: A Reliable Leaderboard for Machine Learning Competitions. ICML 2015, PMLR 37:1006-1014. | https://proceedings.mlr.press/v37/blum15.html | One-bit "beats the best" feedback with adaptive guarantees | yes |
| 18 | Russo, D., Zou, J. (2016). Controlling Bias in Adaptive Data Analysis Using Information Theory. AISTATS 2016, PMLR 51:1232-1240. | https://proceedings.mlr.press/v51/russo16.html | Bias bounded by mutual information between selection and data; motivates bits-per-iteration analysis | yes |
| 19 | Rogers, R., Roth, A., Smith, A., Srebro, N., Thakkar, O., Woodworth, B. (2020). Guaranteed Validity for Empirical Approaches to Adaptive Data Analysis. AISTATS 2020, PMLR 108:2830-2840. | https://proceedings.mlr.press/v108/rogers20a.html | Guess and Check gives tight instance-specific intervals for heuristic adaptive analysis | yes |
| 20 | Feldman, V., Frostig, R., Hardt, M. (2019). The advantages of multiple classes for reducing overfitting from test set reuse. ICML 2019, PMLR 97:1892-1900. | https://proceedings.mlr.press/v97/feldman19a.html | Reuse bias depends on output space; relevant to continuous scores vs pass/fail | yes |
| 21 | Mania, H., Miller, J., Schmidt, L., Hardt, M., Recht, B. (2019). Model Similarity Mitigates Test Set Overuse. NeurIPS 2019. arXiv 1905.12580. | https://arxiv.org/abs/1905.12580 | Similar candidates reduce effective overfitting; reflective edits are highly similar, which may explain small gaps | yes |
| 22 | Recht, B., Roelofs, R., Schmidt, L., Shankar, V. (2019). Do ImageNet Classifiers Generalize to ImageNet? ICML 2019, PMLR 97:5389-5400. | https://proceedings.mlr.press/v97/recht19a.html | Fresh-test-set methodology; drops mostly not explained by adaptivity | yes |
| 23 | Roelofs, R., Shankar, V., Recht, B., Fridovich-Keil, S., Hardt, M., Miller, J., Schmidt, L. (2019). A Meta-Analysis of Overfitting in Machine Learning. NeurIPS 2019. | https://papers.nips.cc/paper_files/paper/2019/hash/ee39e503b6bedf0c98c388b7e8589aca-Abstract.html | Public vs private leaderboard comparison shows little adaptive overfitting among human analysts | yes |
| 24 | Cawley, G. C., Talbot, N. L. C. (2010). On Over-fitting in Model Selection and Subsequent Selection Bias in Performance Evaluation. JMLR 11:2079-2107. | https://www.jmlr.org/papers/v11/cawley10a.html | Selection-criterion variance causes overfitting comparable to differences between algorithms | yes |
| 25 | Saeb, S., Lonini, L., Jayaraman, A., Mohr, D. C., Kording, K. P. (2017). The need to approximate the use-case in clinical machine learning. GigaScience 6(5):gix019. | https://academic.oup.com/gigascience/article/6/5/gix019/3071704 | Record-wise splits inflate accuracy; 28 of 62 smartphone and wearable studies used them; motivates person-level leakage arm | yes |
| 26 | Yuksekgonul, M., Bianchi, F., Boen, J., Liu, S., Huang, Z., Guestrin, C., Zou, J. (2024). TextGrad: Automatic "Differentiation" via Text. arXiv 2406.07496 (published in Nature 639:609-616, 2025). | https://arxiv.org/abs/2406.07496 | Textual-gradient optimizer under test | arXiv yes; Nature page redirected to login (listing only) |
| 27 | Zhang, Q., Hu, C., Upasani, S., et al. (2025). Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models. ICLR 2026. arXiv 2510.04618. | https://arxiv.org/abs/2510.04618 | Generator, Reflector, Curator playbook optimizer under test; AppWorld setting | yes |
| 28 | Opsahl-Ong, K., Ryan, M. J., Purtell, J., Broman, D., Potts, C., Zaharia, M., Khattab, O. (2024). Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs. EMNLP 2024. | https://arxiv.org/abs/2406.11695 | MIPROv2 as the non-reflective comparison optimizer | yes |
| 29 | Zhang, J., Hu, S., Lu, C., Lange, R., Clune, J. (2025). Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents. arXiv 2505.22954. | https://arxiv.org/abs/2505.22954 | Archive-based self-modification with empirical selection on benchmark subsets | yes |
| 30 | Wang, W., Piekos, P., Nanbo, L., et al. (2025). Huxley-Godel Machine. arXiv 2510.21614. | https://arxiv.org/abs/2510.21614 | Selection by descendants' scores (CMP) is another adaptive reuse of the same evaluation set | yes |
| 31 | Singh, S., et al. (2025). The Leaderboard Illusion. arXiv 2504.20879 (NeurIPS 2025 Datasets and Benchmarks per proceedings listing). | https://arxiv.org/abs/2504.20879 | Best-of-many private variants inflates public scores; same selection mechanism at leaderboard scale | yes (arXiv); venue from listing only |
| 32 | Pyatkin, V., et al. (2025). Generalizing Verifiable Instruction Following. NeurIPS 2025 Datasets and Benchmarks. arXiv 2507.02833. | https://arxiv.org/abs/2507.02833 | IFBench, 58 OOD constraints; second domain | yes |
| 33 | Trivedi, H., Khot, T., Hartmann, M., et al. (2024). AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents. ACL 2024. | https://arxiv.org/abs/2407.18901 | Agentic third domain | yes |
| 34 | Bai, S., et al. (2025). Qwen3-VL Technical Report. arXiv 2511.21631. | https://arxiv.org/abs/2511.21631 | Task-agent model family | yes |
| 35 | Heigold et al. (2026). StaBLE: digital metrics capture balance performance across a wide spectrum of balance tasks and abilities. bioRxiv, doi:10.64898/2026.09.16.750744 (as cited by the repository README). | https://github.com/stanfordnmbl/stable-analysis | Biomechanics test bed | repository yes; bioRxiv DOI UNVERIFIED |

Note on two items found but not used as evidence: practitioner reports (orq.ai, Decagon, Effloow) describe GEPA writing topic-specific rules into prompts and an inverted-U in training-set size; they are anecdotal and are not cited. A search summary claimed Meta-Harness gains only 0.9 points out of distribution in RRSI's comparison; that number was not checked on the RRSI paper page and is not relied on.
