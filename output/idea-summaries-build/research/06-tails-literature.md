# Literature sweep and area-chair review for proposal 06: who does self-improvement leave behind?

Status: COMPLETE (2026-11-24). This run resumed an interrupted sweep and merges its machine-learning log with the statistics, evolutionary-biology and clinical-measurement leads recorded in the sibling interim file `06-tails-literature-stats.md` (which was read, not edited).

Verification rule: every link below was fetched once (arXiv abstract page, publisher landing page, PubMed or Europe PMC record, or Semantic Scholar record for paywalled classics). Items that were not fetched are marked UNVERIFIED and are listed in Section 8. DGM and Meta-Harness were verified in the P05 sweep (`05-evolvability-literature.md`) and are reused from there.

## 0. Bottom line

The brief asks how rare, high-stakes subpopulations fare when a self-improvement loop accepts edits that raise the average, whether their trajectory can be forecast from the joint distribution of single-edit effects, and which acceptance rule protects them most cheaply.

- The phenomenon is partly documented. Aggregate gains in prompt optimization hide large item-level churn and regressions (Mitra and Mahmud, Oct 2026), an aggregate-score gate admits edits that break items the agent already solved (SAGE, Sep 2026), and self-evolving agents erode earlier capabilities (Yu et al., May 2026). Outside agents, mean-driven repeated training is known to amplify disparity (Hashimoto et al. 2018; Zhu et al. 2022) and to thin out tails (Ding et al. 2025; Shumailov et al. 2024).
- Tail-protective selection already exists in neighboring settings: CVaR selection in LLM-driven program evolution (CVaR-RMD, Oct 2026), GroupDRO weighting of a prompt pool (Xu et al., Aug 2026), high-probability tail-risk bounds for prompt choice (Prompt Risk Control, ICLR 2024), and error-controlled sequential approval of model modifications to fight bio-creep (Feng, Emerson and Simon 2019).
- The drift formula is textbook selection theory: the correlated response to truncation selection, with the inverse Mills ratio of Heckman (1979) and the covariance logic of Lande and Arnold (1983) and Price (1970). It cannot be sold as a theoretical contribution on its own.
- No paper found measures subgroup trajectories across generations of an accept-if-better agent loop, forecasts them from early edit-effect moments, tests whether trade-off edits arrive early or late, or prices a cumulative per-group guarantee against mean improvement. That combination is open.
- As written: novelty 3.5, significance 3.5. With the reframing in Section 3 (a correlated-response law for self-improving agents, estimated from the loop's own rejection log, plus a design theorem that says how many tail examples a dev set needs) and a large-n second domain where the tail fraction is set by the experimenter, both scores can plausibly reach 4.5.

## 1. Searches run

Across the interrupted runs and this one, 41 distinct queries were run (21 in the machine-learning log, 18 in the statistics log, and the new phrasings below). All 14 seed phrasings from the assignment are covered.

| # | Query (abridged) | Main result |
|---|---|---|
| 1 | prompt optimization subgroup performance disparity / GEPA | GEPA 2507.19457; no subgroup trajectory study |
| 2 | self-improving agents fairness subgroups | none direct; surveys 2607.13104, 2607.07663 (UNVERIFIED) |
| 3 | Beyond Aggregate Accuracy item-level transitions | Mitra and Mahmud 2610.19084 |
| 4 | do self-evolving agents forget | Yu et al. 2605.09315 |
| 5 | winner's curse self-improvement loop | Hu and Tang 2610.09239 |
| 6 | model collapse tails disappear Shumailov | Nature 631:755 |
| 7 | fairness feedback loops synthetic data | Wyllie et al. 2403.07857; Taori and Hashimoto 2209.03942 |
| 8 | accuracy on the line subgroup | Miller et al.; OODSelect (both UNVERIFIED, not used) |
| 9 | RLHF hurts minority preferences | MaxMin-RLHF 2402.08925 |
| 10 | distributionally robust / worst-group prompt optimization | DRO-InstructZero 2510.15260; GroupDRO prompt selection 2608.04339 |
| 11 | multilingual low-resource prompt optimization | 2512.02841, 2510.19806 (no per-language regression analysis in abstracts) |
| 12 | Darwin Godel Machine rare tasks | DGM 2505.22954, aggregate only |
| 13 | fine-tuning improves average hurts tail clinical | Oakden-Rayner et al. 1909.12475 |
| 14 | regression-free model update negative flips | Yan et al. 2011.09161 |
| 15 | disparity amplification repeated loss minimization Hashimoto | 1806.08010 |
| 16 | group DRO worst-group | Sagawa et al. 1911.08731 |
| 17 | Seldonian / high-confidence policy improvement | Thomas et al. Science 2019; ICML 2015 |
| 18 | lexicase selection fairness | La Cava and Moore 2004.13282 |
| 19 | approval policies bio-creep | Feng, Emerson, Simon 1912.12413 |
| 20 | self-improvement tail narrowing | Ding et al. 2411.00750 |
| 21 | harness optimization per-subgroup acceptance | HarnessEvo 2609.02889 (slot-level only) |
| 22 | selection on noisy estimates truncated bivariate normal | Heckman 1979; Smith and Winkler 2006 |
| 23 | correlated response to selection breeder's equation | Lande and Arnold 1983; Price 1970 |
| 24 | non-inferiority alpha spending e-values anytime-valid | Lan and DeMets 1983; Ramdas et al. 2210.01948 |
| 25 | Fisher geometric model trade-offs across environments | Martin and Lenormand 2015; Blanquart et al. 1405.3504; Connallon et al. 2025 |
| 26 | Cooper Lenski specialization | Nature 407:736 |
| 27 | adaptive data analysis holdout reuse / Ladder | Dwork et al. 1506.02629; Blum and Hardt 1502.04585 |
| 28 | spectrum bias diagnostic tests | Ransohoff and Feinstein 1978 |
| 29 | SWE-bench Multilingual | swebench.com: 300 tasks, about 43 per language |
| 30 | Global-MMLU low-resource languages | 2412.03304; HF card: 42 languages, about 14k test rows each |
| 31 | (new) self-improving LLM agent loop subgroup degradation accept-if-better 2026 | no subgroup study; SAGE, Hu and Tang, Yu et al. resurface |
| 32 | (new) prompt optimization per-language regression | no direct per-language regression report |
| 33 | (new) model updates subgroup regression clinical AI non-inferiority | Bilionis et al. 2604.23954 (EMBC 2026 best paper) |
| 34 | (new) self-evolving agents worst-group performance | SAGE only; Falsification-gated evolution 2611.14326 (UNVERIFIED) |
| 35 | (new) AlphaEvolve / DGM per-language or per-repo regression | none |
| 36 | (new) anytime-valid sequential non-inferiority e-values model monitoring | components only; no group-wise loop guarantee |
| 37 | (new) CVaR tail-risk prompt optimization | Prompt Risk Control 2311.13628; CVaR-RMD 2610.25697 |
| 38 | (new) FDA predetermined change control plan subgroups | FDA PCCP final guidance (Aug 2025 page) |
| 39 | (new) gradient conflict over training | PCGrad context only; no general late-conflict result |
| 40 | (new) markerless pose older adults walking aids occlusion | Graf et al. 2026 (five-person pilot); no walking-aid validation found |
| 41 | (new) distribution of fitness effects of LLM edits across tasks | none for LLM edits; biology DFE literature only |

The repeated "no direct study" answers in queries 2, 31, 32, 34, 35 and 41 are evidence, not proof, that the subgroup-trajectory question is unpublished.

## 2. Closest prior works

### 2.1 Beyond Aggregate Accuracy: Item-Level Transitions in Prompt Optimization
- Mitra C, Mahmud T. arXiv:2610.19084, 13 Oct 2026. https://arxiv.org/abs/2610.19084 (verified)
- What they did: tracked recoveries, regressions and churn at the item level across prompt-optimization runs on five benchmarks. In five of nine configurations churn was at least five times the absolute net change. Item-level feedback (RFDPO) cut churn by 40% on LegalBench-Hearsay at similar net gain; validation gains (7.9 points) exceeded held-out gains (5.2).
- What remains open: items, not subpopulations; no acceptance rule; no theory for when churn concentrates on a group; no forecast across generations.

### 2.2 SAGE: A Statistical Acceptance Gate for Self-Evolving Agents
- Wang Y, Xia L, Liu R, et al. arXiv:2609.36043, 28 Sep 2026. https://arxiv.org/abs/2609.36043 (verified)
- What they did: argue that an aggregate gate accepts edits that break items already solved, and that the best observed score on a small validation set is biased upward. SAGE compares parent and child item by item, penalizes regressions, and commits only when a one-sided paired test says wins reliably outnumber losses. Regression rate fell in 19 of 20 settings (LiveMath with DeepSeek-V4: 36.5% to 0%).
- What remains open: per-item rather than per-group protection; the abstract states no guarantee across a sequence of accepted edits. A per-item gate can still let a small group lose a little on every edit as long as wins elsewhere dominate the sign test. SAGE is the strongest baseline the proposal must beat or explain.

### 2.3 The Winner's Curse in LLM Self-Improvement Loops
- Hu L, Tang Y. arXiv:2610.09239, 7 Oct 2026. https://arxiv.org/abs/2610.09239 (verified)
- What they did: treat keep-if-better as selection under measurement noise. Most proposals after the first are harmful; loops overstate gains by 13 to 20 points with 16 selection items and by 1 to 5 with 256; alternative acceptance rules did not beat greedy over whole runs; rescoring on 64 never-selected items removes the average bias. Pre-registered.
- What remains open: everything is on the mean. The joint distribution of gains across groups, and the correlated response of a minority to selection on the majority-weighted mean, are not studied. P06 is the two-group generalization, and this paper sets the bar for pre-registration and held-out rescoring.

### 2.4 Do Self-Evolving Agents Forget? Capability Degradation and Preservation
- Yu Y, Yuan X, Jin H, Liu H, Yu Y, Wang H. arXiv:2605.09315, 10 May 2026. https://arxiv.org/abs/2605.09315 (verified)
- What they did: show capability erosion when agents adapt their workflows, skills, weights or memory to new task distributions; propose Capability-Preserving Evolution (CPE). Under GPT-5.1 workflow evolution, retained simple-task performance rose from 41.8% to 52.8% with CPE.
- What remains open: erosion across sequential task distributions (forgetting), not within one stationary dev distribution under mean selection; no causal theory of why erosion happens; no subgroup analysis.

### 2.5 Self-Evolving Agent Harness
- Wei C, Guan H, Zhu M, et al. arXiv:2610.18813, 13 Oct 2026. https://arxiv.org/abs/2610.18813 (verified)
- What they did: frame harness self-evolution as evolutionary optimization analyzed with continual PAC learning; give an expected generalization bound, a retention bound conditional on historical regression budgets, and a high-probability admission rule using fresh validation data.
- What remains open: the bounds are on average performance; the abstract mentions no subgroup or tail guarantee and no empirical forecast of who loses. The proposed cumulative tail rule is the group-wise version of this retention bound, so the proposal must cite it and show what the group version adds.

### 2.6 CVaR-RMD: CVaR Selection Pressure for Robust Metaheuristic Discovery
- Cui R, Niu L. arXiv:2610.25697, 19 Oct 2026. https://arxiv.org/abs/2610.25697 (verified)
- What they did: in LLM-driven evolution of heuristic programs, rank candidates by empirical CVaR across instance families, seeds and scales instead of the mean. Tail performance improves, failures drop, mean stays competitive, and the gains persist on larger unseen instances.
- What remains open: CVaR over evaluation conditions, not over pre-defined human subpopulations; no account of why the mean rule harms the tail or how fast; no guarantee. It removes "CVaR acceptance" as a novelty claim.

### 2.7 Equitable System-Prompt Selection via Constrained Mixed-Strategy GroupDRO
- Xu M, Yang Q, Liu Z, et al. arXiv:2608.04339, 5 Aug 2026. https://arxiv.org/abs/2608.04339 (verified)
- What they did: weight prompts from a fixed pool to minimize worst metric-group loss subject to mean loss near average-based selection; 13.1% to 13.7% reductions in mean, worst-25% and worst loss across five LLMs on two bilingual (medical, consumer-finance) benchmarks.
- What remains open: one-shot selection from a pool, not an iterative loop; no dynamics; groups are phrasing variants, not people.

### 2.8 Prompt Risk Control
- Zollo TP, Morrill T, Deng Z, Snell JC, Pitassi T, Zemel R. "Prompt Risk Control: A Rigorous Framework for Responsible Deployment of Large Language Models." ICLR 2024; arXiv:2311.13628. https://arxiv.org/abs/2311.13628 (verified)
- What they did: choose prompts by high-probability upper bounds on families of risk measures, including worst-case response quality and disparities across users, with extensions to distribution shift.
- What remains open: a single selection, not a sequence of accepted edits whose errors compound; the cumulative-harm version over generations is not addressed in the abstract.

### 2.9 GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning
- Agrawal LA, Tan S, Soylu D, et al. arXiv:2507.19457; ICLR 2026 (oral). https://arxiv.org/abs/2507.19457 (verified; HTML v2 read for Algorithms 1 and 2)
- What they did: reflective prompt evolution. A child is added to the pool only if its average minibatch score beats the parent's; parents are then sampled in proportion to how many instances of a Pareto set they lead, with strictly dominated candidates pruned.
- What remains open: the per-instance front protects instance specialists as parents, but acceptance is a minibatch mean gate, and the paper reports no per-group held-out regression analysis. Whether the Pareto bookkeeping protects a minority group in the final deployed prompt is untested, and this is a clean question for P06.

### 2.10 Approval policies for modifications to ML-based software as a medical device: a study of bio-creep
- Feng J, Emerson S, Simon N. arXiv:1912.12413, Dec 2019 (journal version in Biometrics 2021 per the earlier log; not confirmed on the fetched page). https://arxiv.org/abs/1912.12413 (verified)
- What they did: repeated adoption of modifications under weak approval rules lets accuracy decay (bio-creep). They cast approval as online hypothesis testing and build aACP-BAC and aACP-BABR from alpha-investing, group-sequential and gate-keeping tools; error control is proven for a constant population and data source.
- What remains open: one population; no subgroup-wise creep; no LLM proposer. This is the closest statistical prior for the brief's cumulative non-inferiority rule, which must be presented as a group-wise extension of it.

### 2.11 Fairness Without Demographics in Repeated Loss Minimization
- Hashimoto TB, Srivastava M, Namkoong H, Liang P. ICML 2018; arXiv:1806.08010. https://arxiv.org/abs/1806.08010 (verified)
- What they did: ERM gives minority groups higher loss; when accuracy drives retention, the minority shrinks and ERM amplifies disparity over time. A DRO objective controls minority risk at each step without group labels.
- What remains open: the amplification runs through population dynamics (who stays), not through selection of discrete edits on a fixed population. P06's mechanism is different and should be stated as such.

### 2.12 The Rich Get Richer: Disparate Impact of Semi-Supervised Learning
- Zhu Z, Luo T, Liu Y. ICLR 2022; arXiv:2110.06282. https://arxiv.org/abs/2110.06282 (verified)
- What they did: pseudo-label SSL helps the group with higher baseline accuracy more, and the poor group may decline; theory, experiments and a Benefit Ratio metric.
- What remains open: self-training on unlabeled data, not edit selection; but its "rich get richer" result is the nearest ML statement of the thesis and gives a metric P06 can reuse.

### 2.13 Mitigating Tail Narrowing in LLM Self-Improvement via Socratic-Guided Sampling
- Ding Y, Xi Z, He W, et al. NAACL 2025; arXiv:2411.00750. https://arxiv.org/abs/2411.00750 (verified)
- What they did: in iterative self-training, sampling skews toward easy queries and solutions to hard queries nearly vanish over iterations; guided hints restore them.
- What remains open: tails defined by difficulty within self-generated training data, not by subpopulation under edit acceptance.

### 2.14 The population genetics of ecological specialization in evolving E. coli populations
- Cooper VS, Lenski RE. Nature 407:736 to 739, 2000. https://doi.org/10.1038/35037572 (verified via Europe PMC record)
- What they did: in 12 lines evolved on glucose for 20,000 generations, unused catabolic functions were lost mostly early, while beneficial mutations were sweeping fastest; high-mutation-rate lines did not lose them faster, which favors antagonistic pleiotropy over mutation accumulation.
- What remains open for P06: this is direct counter-evidence to the brief's "late specialization" story. In the best-studied evolution experiment, trade-offs arrived early, during rapid adaptation. P06 should pre-register both timing hypotheses (Section 4.3).

Other near neighbors (verified, used in the text): RSEA held-out keep-better gate (Nguyen et al. arXiv:2606.28374, https://arxiv.org/abs/2606.28374); High Confidence Policy Improvement (Thomas, Theocharous, Ghavamzadeh, ICML 2015, https://proceedings.mlr.press/v37/thomas15.html); Seldonian framework (Thomas et al., Science 366:999, 2019, https://doi.org/10.1126/science.aag3311, PubMed 31754000); positive-congruent training and negative flips (Yan et al., CVPR 2021, https://arxiv.org/abs/2011.09161); bias bounties with no tension between overall and subgroup accuracy (Globus-Harris, Kearns, Roth, https://arxiv.org/abs/2201.10408); lexicase selection over protected-group intersections (La Cava and Moore, GECCO 2020, https://arxiv.org/abs/2004.13282); clinical model-update fairness (Bilionis et al., https://arxiv.org/abs/2604.23954); HarnessEvo slot attribution (https://arxiv.org/abs/2609.02889); rise-and-collapse in RL self-training (Lin, https://arxiv.org/abs/2606.21090); self-consuming performative loop bias (Wang et al., https://arxiv.org/abs/2601.05184).

## 3. Is the core idea already done?

Partly. Four pieces exist and one central piece does not.

Already done:
1. The observation that mean improvement hides losses on part of the data during prompt or skill optimization (Mitra and Mahmud 2026 at the item level; SAGE 2026 at the item level; Yu et al. 2026 across task distributions).
2. Tail-protective selection rules for LLM-driven search (CVaR-RMD 2026; GroupDRO prompt selection 2026; Prompt Risk Control 2024; GEPA's per-instance Pareto parent selection; lexicase over groups in GP, La Cava and Moore 2020).
3. Error-controlled sequential approval of model modifications (Feng, Emerson, Simon 2019; Thomas et al. 2015 and 2019; Wei et al. 2026's retention bound with regression budgets; RSEA's held-out gate).
4. The mathematics of the drift formula: the correlated response of a second trait to truncation selection on a noisy index (Heckman 1979; Lande and Arnold 1983; Price 1970), and the optimizer's curse (Smith and Winkler 2006).

Not done: no paper measures how a pre-defined human subpopulation's sealed-test performance evolves across generations of an accept-if-better agent loop, forecasts that trajectory from the joint distribution of edit effects, tests when trade-off edits appear, or derives how large a tail sample must be for a cumulative per-group guarantee to cost little mean improvement.

Nearest open, high-value reframing:

> **A correlated-response law for self-improving agents.** For any acceptance or parent-selection rule that acts on a scalar score S, the expected change in a subgroup per generation equals the regression slope of the subgroup's true edit effect on S times the selection differential the rule applies to S, plus a transmission term. Both quantities can be estimated from the loop's own logs, including rejected candidates, so a loop can report, while running, whom it is about to leave behind. The paper then proves how many tail examples (and what split of the evaluation budget) a dev set needs for a cumulative per-group non-inferiority guarantee to cost at most a given fraction of mean improvement, and tests both claims in a domain where the tail fraction is set by design.

This keeps the brief's question and its StaBLE motivation, but moves the contribution from "the tail can drift" (expected) and "here is a protective rule" (partly done) to a predictive law with a forecast interval, an online diagnostic and a design formula, which are new.

## 4. Area-chair review

### 4.1 Scores

- Novelty: 3.5 out of 5 as written. The question is fresh for agent loops, and no paper tracks subgroup trajectories under accept-if-better selection. The score is held down because the formula is classical selection theory, the protective rules (CVaR, GroupDRO, per-item paired gate, alpha-investing approval) each have a close 2024 to 2026 precedent, and a reader can summarize the paper as "Hu and Tang (2026) with two groups" or "SAGE with groups". It reaches 4.5 if the paper delivers an out-of-sample forecast of tail trajectories that beats naive extrapolation, a design theorem for tail sample size, and a decisive test between early and late trade-offs.
- Significance: 3.5 out of 5 as written. Every deployed loop selects on an average and every clinical, multilingual and coding application has a minority that matters, so the stakes are clear, and regulators already ask for modification plans (FDA PCCP final guidance, 2025 page). It is limited because the StaBLE tails are a few dozen people, the guarantee will have little power there, and the lab pilot's tail harm (after SFT) is more likely shrinkage toward the mean than selection drift. It reaches 4.5 if the law holds across two optimizer families and two domains, and the design formula changes how practitioners build dev sets.

### 4.2 Strongest reviewer objection

"The drift result is the breeder's equation: when selection acts on a score, a correlated trait moves by its regression on the score times the selection differential. That is true by construction for jointly Gaussian effects, so the theory adds nothing. The empirical claim that mean selection can hurt minorities is already shown for self-training (Zhu et al. 2022), repeated ERM (Hashimoto et al. 2018) and prompt optimization at the item level (Mitra and Mahmud 2026; SAGE 2026), and tail-protective rules already exist (SAGE, CVaR-RMD, GroupDRO prompt selection, Prompt Risk Control, aACP approval policies). On StaBLE the tail is a few dozen people, so neither the edit-effect correlation nor the guarantee can be estimated with useful precision; and the tail harm that motivated the study came from fine-tuning under MAE, where shrinkage toward the mean lowers average error and raises error at the extremes with no selection involved."

A strong rebuttal needs three things: (a) a forecast that is non-trivial because it is made out of sample, from early-generation data or from rejected candidates, and beats simple baselines; (b) a mechanism split that separates selection drift from shrinkage; and (c) a domain where tail n is large enough for the guarantee to be tested at real power.

### 4.3 Upgrades that would push the scores toward 4.5 to 5

1. **State the law for any selection on S, and estimate it from the loop's own logs.** For jointly Gaussian (b, S), E[b | selected] = mu_b + (Cov(b,S)/Var(S)) (E[S | selected] - mu_S) holds for any selection event that depends on S alone: threshold acceptance, best-of-K (argmax of S), or score-proportional parent sampling (DGM-style). The sign of the response is set by Cov(b,S) and the rule only scales its size through the selection differential. Best-of-K therefore amplifies drift (the expected maximum of K draws grows roughly like sigma_S times sqrt(2 log K)) but cannot change its sign. The Price equation gives the distribution-free version (change = selection covariance + transmission). Because loops evaluate many candidates they then reject, Cov(b,S) can be estimated from the rejection log on a guard set without separate panels. Pre-register a forecast interval for the sealed-test tail change at generation 50 from generations 0 to 10, and compare against linear extrapolation and against the mean trajectory.
2. **A design theorem: the price of protection and the minimum tail sample.** Separate the objective weight pi (population share of the tail) from the evaluation allocation n_B (how many tail people are scored). Under the Gaussian edit model, derive the expected mean gain per generation of the cumulative non-inferiority rule as a function of (rho, sigma_a, sigma_b, pi, n_A, n_B, horizon T, alpha, M), and the allocation of a fixed evaluation budget that maximizes mean gain subject to the guarantee. The output is a formula practitioners can use: "with rho = -0.3 and 40 generations you need at least N tail examples for protection to cost under 10% of mean gain." No prior work in Section 2 gives this.
3. **A decisive dose-response experiment.** In the second domain, set the tail fraction pi and the tail evaluation n_B factorially (for example pi in {0.05, 0.1, 0.2, 0.4} and n_B in {16, 64, 256}). The law predicts a specific sign flip and slope in tail drift as functions of pi and n_B given the measured rho. A theory that predicts a crossing point on a grid the authors chose in advance is far harder to dismiss than a single loop that happened to hurt a group.
4. **Pre-register two competing timing hypotheses.** Early trade-offs: Cooper and Lenski (2000) found that unused functions were lost mostly early, during rapid adaptation, through antagonistic pleiotropy, and Connallon et al. (2025) find that trade-off alleles are under-represented among established mutations because they are more easily lost to drift (the analog of evaluation noise). Late specialization: in Fisher's geometric model, landscapes are close to additive far from the optimum and rugged with sign epistasis near it (Blanquart et al. 2014; Martin and Lenormand 2015). The two predict opposite signs for the trend of rho_t. Pre-register the slope test on rho_t and the inverted-U test with both outcomes treated as publishable.
5. **Split the mechanisms: selection drift versus shrinkage.** Report per-group calibration slope (prediction regressed on reference) and per-group bias alongside MAE, classify accepted edits as shrinking or not (for example, clamp outliers, raise a filter cutoff, regress toward a prior), and rerun the primary contrast under a shrinkage-neutral criterion (error after a per-fold affine recalibration fitted on dev, or within-group rank correlation). Drift that survives this is selection drift; drift that vanishes is shrinkage, which is still worth reporting but is a different paper.
6. **Stronger baselines, chosen so the theory predicts their ranking.** Mean gate; GEPA per-instance Pareto; SAGE's per-item paired one-sided test; CVaR selection over people (CVaR-RMD style); GroupDRO-weighted mean; Prompt Risk Control style upper-bound selection; Feng et al.'s aACP-BAC alpha-investing approval; Hu and Tang's fresh-holdout rescoring; and the cumulative per-group rule. State in advance which rule the law predicts will fail at negative rho and small n_B (for example, a per-item sign test passes edits that cost a small group a little each time).
7. **Generality across loop families.** Run the law on a GEPA-style prompt optimizer and on a Meta-Harness or DGM-style code optimizer, and if budget allows on a weight-update loop such as rejection-sampling self-training. If the same Cov(b,S) estimate forecasts drift in all three, the result is a property of selection, not of one optimizer.
8. **Tool-level counterfactuals.** For each accepted edit attributed to a tool switch or parameter change, re-run the tail people with that single change reverted (a counterfactual swap) and report the recovered tail error. This turns "where tools fail in the tail" from a hypothesis into a measured attribution and connects directly to tool selection in agentic use.

### 4.4 Must-fix items in the brief

1. **Overstated claim about current loops.** "Every recursive self-improvement loop in current use accepts or ranks candidates by average dev score" is imprecise. GEPA gates children on minibatch mean but samples parents from a per-instance Pareto front (Algorithms 1 and 2 of the GEPA paper). DGM keeps an archive and samples parents roughly in proportion to score and inversely to child count (P05 sweep), with no accept-if-better step. HGM ranks by clade success rates. State the theory for selection on any scalar S, and treat GEPA's Pareto rule as selection on a vector, where the scalar law does not apply directly.
2. **Credit the theory.** The formula E[b | S > 0] = mu_b + Cov(b,S)/sigma_S times lambda(mu_S/sigma_S) is the standard truncated-normal and inverse-Mills-ratio result (Heckman 1979) and the correlated response to selection (Lande and Arnold 1983; Price 1970). The winner's-curse term is Smith and Winkler (2006) and, for loops, Hu and Tang (2026). Present the forecast test and the design theorem as the contributions.
3. **"Best-of-K sharpens the effect" needs care.** Best-of-K scales the selection differential and therefore the size of the drift, but it cannot change the sign, which is fixed by Cov(b,S) under joint Gaussianity. Say so, and note the per-generation drift is P(accept) E[b | accept] = mu_b Phi(z) + (Cov(b,S)/sigma_S) phi(z), which differs from the per-accepted-edit quantity the brief writes down.
4. **w plays two roles.** The brief sets w = n_A/(n_A + n_B), which ties the objective weight to the evaluation sample. Tail-oversampled evaluation changes n_B but should not change the population-weighted objective. Use pi for the objective weight and n_A, n_B for the noise; otherwise the "tail-oversampled" arm is misanalyzed.
5. **Noise attenuates the measured correlation.** rho estimated from noisy panel estimates a-hat, b-hat is biased toward zero, badly so with few tail people. Estimate the noise covariance by person-level bootstrap or split-half across people and correct (method-of-moments disattenuation), and report both raw and corrected rho with intervals. Without this, "measured rho near zero" (a stated falsifier) can be produced by noise alone.
6. **The motivating pilot result is probably shrinkage.** The SFT model's MAE (0.100) beats the constant baseline (0.120) by about one sixth, so part of its gain is plausibly shrinkage toward the mean, which raises error at the extremes with no selection. Do not cite the pilot as evidence of selection drift; use it as motivation for the mechanism split in upgrade 5.
7. **Tail labels that are not measurements.** In StaBLE, 98 trials across 24 participants were not performed for safety and were assigned score 0, and 3 failed trials had features imputed by regression on age. These people are disproportionately in the tail. A loop can lower tail error by learning the assignment rule (for example, visible impairment implies zero) rather than measuring. Exclude these trials from tail loss or analyze them as a separate stratum, and say which.
8. **Normalization endpoints are set by the tail.** StaBLE's min-max scaling uses the minimum and maximum over all 180 people, and those endpoints are by definition set by the most extreme people. Recompute L and U on dev people per fold; expect test tail scores outside 0 to 1, and do not clip them silently, since clipping changes tail error the most. Report errors on the raw feature scale as well.
9. **Outcome-defined tails need an independent reference.** Groups defined by the bottom or top decile of the same reference score used in the loss carry regression-to-the-mean artifacts: any shrinking edit looks tail-harmful. Make the primary tail covariate-defined (fall-risk group, age 70 and above, or self-reported diagnosis), and if an outcome-defined tail is kept, define it with an external measure (ABC Scale or fall history) rather than the scored reference.
10. **Multiplicity and overlap of tail definitions.** Age, diagnosis, fall risk and device use are correlated, and the brief lists six definitions. Pre-register one primary tail and one primary contrast; treat the others as secondary with a stated correction. Check which covariates exist: the public Zenodo release lists demographics, fall history, fall risk and balance confidence, while "assistive device" and "unusual camera placement" were not confirmed in any source read for this sweep (CHECK with the lab files).
11. **Adaptivity breaks the guarantee unless the guard data are fresh.** If the tail data used for the non-inferiority test also feed S or the proposer's traces, each test is run on data the loop has already adapted to, and the nominal level fails. Specify a tail guard set that neither S nor the proposer sees, or use a reusable-holdout mechanism (Dwork et al. 2015). State that alpha-spending (Lan and DeMets 1983) gives validity under arbitrary dependence between tests through a union bound, and that an e-process (Ramdas et al.) allows optional stopping. With K tail groups, the guarantee needs alpha/K or closed testing.
12. **Power of the guarantee on StaBLE.** With roughly 7 to 15 tail people in a guard fold and alpha spent over 50 generations, per-generation levels near 0.001 will reject almost every edit, so the falsifier "the protective rule costs most of the average improvement" can trigger from low power alone. Run a power calculation before the loop, pick the margin M from a defensible clinical difference (StaBLE has no test-retest session, so a minimal detectable change is not available; use the three-camera reconstruction disagreement or a pre-specified fraction of the score SD of 0.12), and run the main guarantee test in the large-n second domain.
13. **The panel must share the loop's lineage.** For the drift forecast, edits at generation t must be proposed on the parent the loop actually holds at t, per seed. With five folds and five seeds this multiplies panels; state whether one lineage's rho_t is used to forecast other lineages (a harder and more useful test) or only its own.
14. **Tool-failure claims are hypotheses.** The brief asserts that pose estimators lose track during large sway or stepping, that walkers and canes occlude feet, and that smoothing flattens large excursions. The evidence found is thin: a five-person perturbed-walking pilot reported lower gait-event detection under perturbation, mainly through lower recall, with differences not statistically significant (Graf et al., Frontiers in Sports and Active Living 2026), and no markerless validation with walking aids was found. Phrase these as hypotheses that experiment 5 tests.
15. **Cost.** Experiment 1 alone is about 4 generations x 200 edits x 5 folds of full-panel evaluation, and OpenCap Monocular takes about 3.8 minutes per 17 s clip on an H100. Cache tool outputs per video, restrict panels to edits whose tool calls can reuse cached outputs where possible, and give the total in GPU-hours and API tokens.
16. **Keep distinct from earlier project ideas.** The protective rule should not become "calibration after tool updates" or "paired change measurement", and the tool-route attribution should not become "re-execution after harness edits". The contribution is about the selection rule and the tail, so keep the tool analysis as attribution only.

### 4.5 Verdict

Revise before submission; promising. As written, the paper reads as an expected phenomenon plus a protective rule with close precedents, demonstrated on a dataset whose tails are too small for its own guarantee. Reframed as a correlated-response law for self-improving agents (estimated online from rejected candidates, with a pre-registered out-of-sample forecast), a design theorem for tail sample size and evaluation allocation, a dose-response experiment in a large-n domain, and a pre-registered contest between early and late trade-offs, it is a credible 4.5 on both axes for a top ML venue. StaBLE should remain the motivating high-stakes case and the site of the tool-route attribution, with the guarantee tested where n allows.

## 5. Second domain recommendation

**Primary: Global-MMLU, run as a tool-using QA agent with low-resource languages as the tail.**

- What it is: Singh et al., "Global MMLU: Understanding and Addressing Cultural and Linguistic Biases in Multilingual Evaluation" (arXiv:2412.03304), 42 languages with translation quality checked by compensated professional and community annotators, plus culturally sensitive and culturally agnostic subsets; 28% of MMLU questions were judged to need culturally sensitive knowledge. The Hugging Face card lists about 14k test rows and 285 dev rows per language subset.
- Why it fits: (1) the tail is defined before the loop starts (low-resource languages, or the culturally sensitive subset), avoiding outcome-defined artifacts; (2) per-group sealed-test n is in the thousands, so the cumulative guarantee can be tested at real power; (3) the experimenter can compose the dev set to set pi and n_B, which enables the dose-response test of upgrade 3; (4) evaluation is cheap, so 200-edit panels and many seeds are affordable; (5) natural tool-route edits carry language-dependent trade-offs (translate the question to English with a tool before answering, call retrieval in English, force the reasoning language), which links the study to tool selection in general agentic use; (6) GEPA-style optimizers run on it unchanged.
- Caveats: multiple-choice format; possible pretraining contamination; the dataset does not ship a resource-tier label, so the tiering must be fixed in advance from a published language-resource taxonomy (cite one and verify it before use).

**Agentic alternative for code: Multi-SWE-bench.** Zan et al. (arXiv:2504.02605): 1,632 issue-resolution instances across Java, TypeScript, JavaScript, Go, Rust, C and C++, curated by 68 annotators. Languages or repositories can serve as groups for a Meta-Harness or DGM-style code optimizer. It is costlier per evaluation, and per-language counts were not confirmed in this sweep. SWE-bench Multilingual is not suitable as the tail test: it is balanced by design at about 43 tasks per language (300 tasks total, swebench.com), so there is no minority and the per-group n is as small as StaBLE's. MGSM (Shi et al., arXiv:2210.03057; 250 problems in 10 languages including Bengali and Swahili) is a cheap sanity domain but too small per language for the guarantee.

## 6. Theory notes for the math agent

These follow from the brief's model and should be checked in `theory-checks.md` (A2 to A4 are still pending there).

- General selection on S: if (b, S) is jointly Gaussian and selection depends only on S, then b - beta S is independent of S, with beta = Cov(b,S)/Var(S), so E[b | selected] = mu_b + beta (E[S | selected] - mu_S). Threshold (S > 0): E[S | S > 0] - mu_S = sigma_S lambda(mu_S/sigma_S), which reproduces the brief. Best-of-K among independent candidates: E[b of winner] = mu_b + beta (E[max_k S_k] - mu_S). Sign set by Cov(b,S) in both cases.
- Per-generation expected tail change with a threshold rule: mu_b Phi(z) + (Cov(b,S)/sigma_S) phi(z), with z = mu_S/sigma_S.
- Noise: with a-hat = a + e_a and b-hat = b + e_b, independent noise across disjoint groups, Cov(b,S) = w rho sigma_a sigma_b + (1 - w) sigma_b^2 as the brief says, with w replaced by the objective weight pi once evaluation allocation is separated (must-fix 4). Noise enters only through sigma_S, so more tail evaluation shrinks sigma_S and increases both the acceptance rate and the selection differential per unit of S.
- The A1 check already found 255 cells with negative tail drift that the brief's sufficient condition misses (mu_b < 0 with Cov(b,S) > 0). The brief should state the condition as sufficient, not necessary, and give the exact sign condition above.

## 7. Key citations

| # | Reference | URL | Supports | Verified |
|---|---|---|---|---|
| 1 | Agrawal LA et al. GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning. ICLR 2026; arXiv:2507.19457 | https://arxiv.org/abs/2507.19457 | Minibatch-mean acceptance plus per-instance Pareto parent selection; the per-instance rule P06 must test | yes |
| 2 | Mitra C, Mahmud T. Beyond Aggregate Accuracy: Item-Level Transitions in Prompt Optimization. arXiv:2610.19084, 2026 | https://arxiv.org/abs/2610.19084 | Aggregate gains hide churn at least five times the net change in 5 of 9 configurations | yes |
| 3 | Wang Y et al. SAGE: A Statistical Acceptance Gate for Self-Evolving Agents. arXiv:2609.36043, 2026 | https://arxiv.org/abs/2609.36043 | Aggregate gates admit edits that break solved items; per-item paired test as baseline | yes |
| 4 | Hu L, Tang Y. The Winner's Curse in LLM Self-Improvement Loops. arXiv:2610.09239, 2026 | https://arxiv.org/abs/2610.09239 | Keep-if-better as selection under noise; mean-only; pre-registration and held-out rescoring standard | yes |
| 5 | Yu Y et al. Do Self-Evolving Agents Forget? arXiv:2605.09315, 2026 | https://arxiv.org/abs/2605.09315 | Capability erosion in self-evolving agents; CPE | yes |
| 6 | Wei C et al. Self-Evolving Agent Harness. arXiv:2610.18813, 2026 | https://arxiv.org/abs/2610.18813 | Continual-PAC retention bound with regression budgets; average-only guarantee to extend group-wise | yes |
| 7 | Cui R, Niu L. CVaR-RMD: CVaR Selection Pressure for Robust Metaheuristic Discovery. arXiv:2610.25697, 2026 | https://arxiv.org/abs/2610.25697 | CVaR selection in LLM program evolution improves tails with competitive mean | yes |
| 8 | Xu M et al. Equitable System-Prompt Selection via Constrained Mixed-Strategy GroupDRO. arXiv:2608.04339, 2026 | https://arxiv.org/abs/2608.04339 | Worst-group prompt selection with a mean constraint (one-shot, pool-based) | yes |
| 9 | Zollo TP et al. Prompt Risk Control. ICLR 2024; arXiv:2311.13628 | https://arxiv.org/abs/2311.13628 | Selecting by mean validation score can yield poor responses for disadvantaged users; tail-risk bounds | yes |
| 10 | Hashimoto TB et al. Fairness Without Demographics in Repeated Loss Minimization. ICML 2018; arXiv:1806.08010 | https://arxiv.org/abs/1806.08010 | Repeated ERM amplifies disparity; DRO remedy | yes |
| 11 | Sagawa S et al. Distributionally Robust Neural Networks for Group Shifts. arXiv:1911.08731 (ICLR 2020; venue not on fetched page) | https://arxiv.org/abs/1911.08731 | Group DRO and worst-group objectives | yes |
| 12 | Zhu Z, Luo T, Liu Y. The Rich Get Richer: Disparate Impact of Semi-Supervised Learning. ICLR 2022; arXiv:2110.06282 | https://arxiv.org/abs/2110.06282 | Self-training helps the better-off group and can hurt the worse-off group | yes |
| 13 | Ding Y et al. Mitigating Tail Narrowing in LLM Self-Improvement via Socratic-Guided Sampling. NAACL 2025; arXiv:2411.00750 | https://arxiv.org/abs/2411.00750 | Hard-query solutions nearly vanish over self-improvement iterations | yes |
| 14 | Shumailov I et al. AI models collapse when trained on recursively generated data. Nature 631:755 to 759, 2024 | https://doi.org/10.1038/s41586-024-07566-y | Recursive training degrades models (model collapse); tails of the original distribution are lost (abstract wording not retrieved; PubMed 39048682 record confirmed) | yes (record) |
| 15 | Feng J, Emerson S, Simon N. Approval policies for modifications to ML-based SaMD: a study of bio-creep. arXiv:1912.12413 | https://arxiv.org/abs/1912.12413 | Sequential approvals cause bio-creep; alpha-investing approval policies; closest prior for the cumulative rule | yes |
| 16 | Thomas P, Theocharous G, Ghavamzadeh M. High Confidence Policy Improvement. ICML 2015, PMLR 37:2380 to 2388 | https://proceedings.mlr.press/v37/thomas15.html | Accept a new policy only with a high-confidence lower bound; incremental version | yes |
| 17 | Lan KKG, DeMets DL. Discrete sequential boundaries for clinical trials. Biometrika 70(3):659 to 663, 1983 | https://doi.org/10.1093/biomet/70.3.659 | Alpha-spending functions that do not require the number of looks in advance | yes |
| 18 | Ramdas A, Grunwald P, Vovk V, Shafer G. Game-theoretic statistics and safe anytime-valid inference. arXiv:2210.01948 | https://arxiv.org/abs/2210.01948 | E-processes and confidence sequences valid under continuous monitoring and optional stopping | yes |
| 19 | Smith JE, Winkler RL. The Optimizer's Curse: Skepticism and Postdecision Surprise in Decision Analysis. Management Science, 2006 | https://doi.org/10.1287/mnsc.1050.0451 | Selecting the best of noisy estimates overstates its value | yes (record) |
| 20 | Heckman JJ. Sample selection bias as a specification error. Econometrica, 1979 | https://doi.org/10.2307/1912352 | Inverse Mills ratio correction for selection on a Gaussian index | yes (record) |
| 21 | Lande R, Arnold SJ. The measurement of selection on correlated characters. Evolution, 1983 | https://doi.org/10.1111/j.1558-5646.1983.tb00236.x | Selection on one trait moves correlated traits; regression framework for correlated response | yes (record) |
| 22 | Price GR. Selection and covariance. Nature, 1970 | https://doi.org/10.1038/227520a0 | Distribution-free decomposition of change into a selection covariance and transmission | yes (record) |
| 23 | Cooper VS, Lenski RE. The population genetics of ecological specialization in evolving E. coli populations. Nature 407:736 to 739, 2000 | https://doi.org/10.1038/35037572 | Trade-offs appeared early, during rapid adaptation, via antagonistic pleiotropy (counter-evidence to late specialization) | yes |
| 24 | Blanquart F, Achaz G, Bataillon T, Tenaillon O. Properties of selected mutations and genotypic landscapes under Fisher's Geometric Model. arXiv:1405.3504 | https://arxiv.org/abs/1405.3504 | Landscapes near-additive far from the optimum, rugged with sign epistasis near it (basis for late specialization) | yes |
| 25 | Oakden-Rayner L, Dunnmon J, Carneiro G, Re C. Hidden stratification causes clinically meaningful failures in ML for medical imaging. arXiv:1909.12475 (ML4H 2019) | https://arxiv.org/abs/1909.12475 | Good average performance with over 20% relative gaps on clinically important low-prevalence subsets | yes |
| 26 | Dwork C, Feldman V, Hardt M, Pitassi T, Reingold O, Roth A. Generalization in Adaptive Data Analysis and Holdout Reuse. arXiv:1506.02629 | https://arxiv.org/abs/1506.02629 | Reusing a holdout adaptively invalidates naive tests; reusable-holdout remedy for the guard set | yes |
| 27 | Singh S et al. Global MMLU. arXiv:2412.03304; dataset card | https://arxiv.org/abs/2412.03304 | 42 languages, culturally sensitive and agnostic subsets; about 14k test rows per language (HF card) | yes |
| 28 | Zan D et al. Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving. arXiv:2504.02605 | https://arxiv.org/abs/2504.02605 | 1,632 instances in 7 languages for a code-agent tail study | yes |

Further verified sources used in the text: Connallon T et al., Evolution 79(7):1243 to 1255, 2025, https://doi.org/10.1093/evolut/qpaf061 (trade-off alleles under-represented among established mutations); Martin G, Lenormand T, Evolution 69(6):1433 to 1447, 2015, https://doi.org/10.1111/evo.12671; Thomas PS et al., Science 366:999 to 1004, 2019, https://doi.org/10.1126/science.aag3311; Nguyen M et al. RSEA, https://arxiv.org/abs/2606.28374; Yan S et al. CVPR 2021, https://arxiv.org/abs/2011.09161; Globus-Harris I, Kearns M, Roth A, https://arxiv.org/abs/2201.10408; La Cava W, Moore JH, https://arxiv.org/abs/2004.13282; Wyllie S, Shumailov I, Papernot N, https://arxiv.org/abs/2403.07857; Taori R, Hashimoto TB, https://arxiv.org/abs/2209.03942; Chakraborty S et al. MaxMin-RLHF, https://arxiv.org/abs/2402.08925; Li Y. DRO-InstructZero, https://arxiv.org/abs/2510.15260; Bilionis I et al., https://arxiv.org/abs/2604.23954; Blum A, Hardt M. The Ladder, https://arxiv.org/abs/1502.04585; Manheim D, Garrabrant S. Categorizing Variants of Goodhart's Law, https://arxiv.org/abs/1803.04585; Ransohoff DF, Feinstein AR. Problems of spectrum and bias in evaluating the efficacy of diagnostic tests, NEJM 1978, https://doi.org/10.1056/NEJM197810262991705 (record); Shi F et al. MGSM, https://arxiv.org/abs/2210.03057; SWE-bench Multilingual, https://www.swebench.com/multilingual.html; Graf V et al., Frontiers in Sports and Active Living 8, 2026, https://doi.org/10.3389/fspor.2026.1902010; FDA PCCP final guidance, https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence; Zhang L et al. Cross-Lingual Prompt Steerability, https://arxiv.org/abs/2512.02841; Lin J. rise-and-collapse, https://arxiv.org/abs/2606.21090; Wang Y et al. SCPL, https://arxiv.org/abs/2601.05184; Nguyen M et al. HarnessEvo, https://arxiv.org/abs/2609.02889. DGM (https://arxiv.org/abs/2505.22954) and Meta-Harness (https://arxiv.org/abs/2603.28052) were verified in the P05 sweep.

## 8. Unverified or corrected items

- UNVERIFIED leads from the interrupted run, not fetched and not used: MAS-PromptBench 2606.23664; Prompt Fairness 2511.19956; Fairness-Aware Test-Time Prompt Tuning 2608.25707; GDRO-RL 2601.19280; RPO 2305.13954; PolyPrompt 2502.19756; surveys 2607.13104 and 2607.07663; Harmony Harness 2610.15150; "Harnesses that improve themselves" (logged as 2611.22299; search results show Self-Harness as 2606.09498, so the ID is uncertain); Falsification-gated self-evolution 2611.14326; Miller et al. "Accuracy on the line"; OODSelect; BCWI 2301.10546; Xie et al. 2105.03048; Helmuth et al. 1905.09372; the npj Digital Medicine 2026 intersectional VLM fairness paper.
- Venues not shown on the fetched page: Sagawa et al. (ICLR 2020), Wyllie et al. (FAccT 2024 per the earlier log), Feng et al. (Biometrics 2021 per the earlier log), Globus-Harris et al. (FAccT 2022 per an ACM search hit in the earlier log). The arXiv IDs are verified.
- Shumailov et al.: the PubMed record confirms title, authors, volume and pages; the abstract sentence about tails disappearing was not retrieved, so quote it only after reading the article.
- Zhang et al. 2512.02841: a secondary summary claimed that "translate the question into multiple languages" directives are harmful; the abstract does not say this. Treat as UNVERIFIED.
- FDA PCCP: the final guidance page was fetched, but it contains no statement about subgroup evaluation; the claim that PCCPs may target "performance for a defined subpopulation" comes from a law-firm summary and is UNVERIFIED against the guidance text.
- Global-MMLU: no resource-tier label per language was found on the dataset card; the tiering must come from a separately verified taxonomy.
- Correction to the brief: the sign condition rho < -(1 - w) sigma_b/(w sigma_a) is sufficient (with mu_b <= 0), not necessary; theory check A1 found 255 cells with negative drift it does not flag.
- Correction to the brief: Cooper and Lenski (2000) report early, not late, loss of unused functions, so the late-specialization prediction is contested by the best-known evolution experiment.
