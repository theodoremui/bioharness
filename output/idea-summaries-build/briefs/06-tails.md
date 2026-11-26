# Brief for proposal 06: who does self-improvement leave behind?

Output file: `docs/idea-summaries/06-who-self-improvement-leaves-behind.md`. Figures: `docs/idea-summaries/images/06/`. Figure code: `output/idea-summaries-build/figs_06.py`.

## Core question

In loops that accept an edit when it raises the average score, how does performance on rare, high-stakes subpopulations evolve across generations? Can that trajectory be predicted from the joint distribution of single-edit effects measured early in the loop? Which acceptance rule protects those subpopulations at the smallest cost in average improvement?

One-line thesis: accept-if-the-average-improves is a selection rule, and selection on a noisy average that is dominated by the majority can steadily degrade a minority whenever late-stage edits trade one group against the other, even when every accepted edit raises the mean.

## Why it matters here

Clinical balance tools exist to find people with poor balance. In StaBLE (180 people, ages 18 to 87, 71 with self-reported diagnoses, elite balancers at the other extreme, fall-risk groups, and 24 participants with trials skipped for safety) those people are a minority of every dev set. The lab pilot found that supervised fine-tuning lowered average error while hurting clinical extremes (internal account). Every recursive self-improvement loop in current use (GEPA, Meta-Harness, DGM, HGM, AlphaEvolve-style evolution, ACE) accepts or ranks candidates by average dev score, sometimes with per-instance Pareto bookkeeping (GEPA). Tool behavior is also tail-specific: pose estimators trained mostly on healthy adults lose track during large sway or stepping, walkers and canes occlude feet, and smoothing filters tuned to quiet standing flatten the large excursions that define poor balance. So many candidate edits (switch to a faster pose model, raise a filter cutoff, clamp outliers) help the majority and hurt the tail.

Generalize: coding agents tuned on popular repositories and languages; multilingual assistants tuned on high-resource languages; medical QA agents tuned on common conditions.

## Theory to present (verify against `research/theory-checks.md` once the math agent has written it)

Each candidate edit has true mean loss reductions $a$ (majority) and $b$ (tail), jointly Gaussian with means $\mu_a,\mu_b$, standard deviations $\sigma_a,\sigma_b$ and correlation $\rho$. Estimates from $n_A$ and $n_B$ people add independent noise with variances $s_a^2=v/n_A$ and $s_b^2=v/n_B$. The mean rule accepts if $S=w\hat a+(1-w)\hat b>0$ with $w=n_A/(n_A+n_B)$. Then

$$\mathbb{E}[b\mid S>0]=\mu_b+\frac{\mathrm{Cov}(b,S)}{\sigma_S}\,\lambda\!\left(\frac{\mu_S}{\sigma_S}\right),\qquad \lambda(z)=\frac{\phi(z)}{\Phi(z)},$$

with $\mathrm{Cov}(b,S)=w\rho\sigma_a\sigma_b+(1-w)\sigma_b^2$, $\mu_S=w\mu_a+(1-w)\mu_b$ and $\sigma_S^2=w^2(\sigma_a^2+s_a^2)+(1-w)^2(\sigma_b^2+s_b^2)+2w(1-w)\rho\sigma_a\sigma_b$. The tail degrades in expectation per accepted edit when this is negative; with $\mu_b\le0$ this happens whenever $\rho<-(1-w)\sigma_b/(w\sigma_a)$. Best-of-$K$ selection sharpens the effect (a winner's-curse term). Two predictions follow and are the core empirical tests:

1. **Drift prediction.** The tail trajectory of a full loop is predicted by the edit-effect moments $(\mu,\sigma,\rho)$ measured from one-step edit panels.
2. **Late specialization (inverted U).** Shared improvements (positive $\rho$) are found and exhausted early, so $\rho_t$ falls with generation $t$ and tail performance first improves, then degrades, while the mean keeps improving.

A protective rule with a guarantee: accept only if the estimated majority gain is positive and a one-sided test rejects "cumulative tail harm since generation 0 exceeds $M$" at level $\alpha_t$, with $\sum_t\alpha_t\le\alpha$ (alpha-spending or an e-process). Then the probability that the loop ever ends more than $M$ worse on the tail than where it started is at most $\alpha$ under the stated sampling assumptions. Compare its price in average improvement against other rules.

## Definitions to include

Recursive self-improvement loop; acceptance rule; subgroup and tail (covariate-defined: age 70 and above, self-reported diagnosis, fall-risk group, assistive device, unusual camera placement; outcome-defined: bottom and top decile of a task score); edit-effect panel; selection on noisy estimates; inverse Mills ratio (in plain words); per-instance Pareto (GEPA); worst-group and CVaR objectives; non-inferiority testing; alpha-spending.

## Experiments

0. Monte Carlo validation of the formula and of the guarantee (cheap).
1. Edit-effect panels: at generations $t\in\{0,10,25,50\}$ sample about 200 single-step edits from the proposer on the current parent and evaluate each on a panel pool of people disjoint from the loop's dev set, using cross-fitting over five participant folds so every person is used. Estimate $(\mu,\sigma,\rho)$ per generation with person-clustered bootstrap intervals.
2. Full loops: acceptance rules (mean; GEPA per-instance Pareto; worst-group; CVaR over people; tail-oversampled evaluation that reallocates evaluation budget to tail people; the cumulative non-inferiority rule) crossed with two optimizer families (a GEPA-style prompt and harness optimizer, a Meta-Harness or DGM-style code optimizer) and at least five seeds, per domain. Report per-group sealed-test trajectories.
3. Prediction test: compare observed tail trajectories with the drift predicted from step 1; pre-register the inverted-U test.
4. Price of protection: frontier of average improvement against tail change for each rule.
5. Tool-route attribution: classify accepted edits (tool switch, parameter change, prompt rule, new check) and attribute tail harm to edit types and to specific tools.
6. Second domain with large tail $n$: for example a multilingual math or QA agent with low-resource languages as the tail, or a coding agent on a multilingual SWE-bench split. Let the literature report choose.

Statistics: StaBLE tails are small, so use five-fold cross-fitting with sealed test folds, person-clustered bootstrap, pooled tasks per person, and pre-registered primary contrasts. Report effective $n$ in people.

## Figures (suggested)

1. Concept: mean improves while the tail curve rises then falls (illustrative).
2. Edit-effect scatter: majority gain vs tail gain, acceptance line of the mean rule, shaded region of accepted-but-tail-harmful edits.
3. The drift formula as a picture: how $\rho$ and $w$ set the sign.
4. Late specialization: $\rho_t$ falling with generation (illustrative).
5. Experimental flow: panels, loops, sealed folds.
6. Acceptance rules compared on a price-of-protection frontier (illustrative).
7. Where tools fail in the tail (large sway, occlusion by walking aids, smoothing).

## Falsifiers

Tail performance tracks the mean under the mean rule; measured $\rho$ is near zero or positive at all generations; the drift prediction fails out of sample; or the protective rule costs most of the average improvement.

## Reframing after the literature sweep, area-chair review and theory checks (overrides the design above where they conflict)

Read `research/06-tails-literature.md` and section A of `research/theory-checks.md` first. Novelty as first briefed was 3.5: the phenomenon (item-level churn, capability erosion) and several protective rules already exist in 2026 work (Mitra and Mahmud arXiv 2610.19084; SAGE 2609.36043; Yu et al. 2605.09315; Wei et al. 2610.18813; CVaR-RMD 2610.25697; GroupDRO prompt selection 2608.04339; Prompt Risk Control 2311.13628; Hu and Tang 2610.09239), and the drift formula is classical selection theory (Heckman 1979; Price 1970; Lande and Arnold 1983; Smith and Winkler 2006). Credit all of these plainly.

**New framing: a correlated-response law for self-improving agents, tested by forecasting.** For any selection that depends only on the scalar score $S$, $\mathbb{E}[b\mid\text{selected}]=\mu_b+\frac{\mathrm{Cov}(b,S)}{\mathrm{Var}(S)}\left(\mathbb{E}[S\mid\text{selected}]-\mu_S\right)$, which covers threshold acceptance, best-of-$K$ and score-proportional parent sampling (the Price equation is the distribution-free version). The contribution is not the formula but (1) estimating $\mathrm{Cov}(b,S)$ online from the loop's own rejected candidates on a sealed guard set and issuing a pre-registered out-of-sample forecast of the sealed-test tail change at generation 50 from generations 0 to 10; (2) a design theorem for tail sample size and evaluation allocation under the protective rule; (3) a factorial dose-response in a large-$n$ domain; (4) a pre-registered test between two timing hypotheses.

Must-fix items:
- Separate the objective weight $\pi$ (share of the tail in the objective) from the evaluation allocation $n_B$.
- Give per-proposal drift $\mu_b\Phi(z)+\frac{\mathrm{Cov}(b,S)}{\sigma_S}\phi(z)$ and per-accepted-edit drift; say the sign condition is sufficient, not necessary, and that the threshold does not depend on noise; best-of-$K$ multiplies the selection term (exact factor $m_K(c)$) and cannot flip its sign.
- Timing: replace "inverted U" with three regimes predicted by a Fisher geometric model (monotone tail gain, inverted U, early decline), set by whether the tail and mean gradients conflict; early trade-offs (Cooper and Lenski 2000) and late specialization are competing pre-registered hypotheses, both publishable.
- Panels: naive $\rho$ is attenuated by noise; estimate drift directly as the mean of $b_{\text{panel}}\cdot\mathbf{1}\{S_{\text{dev}}>0\}$ with each panel edit scored on dev people and on disjoint panel people.
- Guarantee: valid only with fresh or sealed gate data, alpha spent per test, every candidate compared with $h_0$ (bio-creep, arXiv 1912.12413). Reusing the same tail people breaks it (realized 0.11 to 0.29 at nominal 0.05); at StaBLE sizes the practical valid option is sealed checkpoint certification by fixed-sequence testing. Skewed harms make t tests anti-conservative; say so. Use the simulated price numbers (valid rules keep 9 to 57 percent of majority gain, an oracle 97 percent, the unconstrained loop crosses the harm margin in 41 percent of runs) only as simulation results.
- Separate selection drift from shrinkage toward the mean (per-group calibration slope and bias; a shrinkage-neutral criterion). The lab pilot SFT tail harm is plausibly shrinkage; do not cite it as selection drift.
- StaBLE specifics: 98 skipped-for-safety trials (24 people) were assigned 0 and 3 trials were imputed; exclude them from tail loss or treat as a separate stratum. Recompute min-max normalization per fold on dev people. Make the primary tail covariate-defined (fall-risk group, age 70 and above) and pre-register one primary tail; outcome-defined deciles carry regression to the mean. Check which covariates are recorded before naming assistive devices or camera placement.
- Second domain for the dose-response and the guarantee: Global-MMLU (arXiv 2412.03304) run as a tool-using QA agent, with low-resource languages or the culturally sensitive subset as the tail, so tail fraction $\pi\in\{0.05,0.1,0.2,0.4\}$ and tail evaluation size $n_B\in\{16,64,256\}$ are set by design.
- Baselines with predicted ranking: mean gate, GEPA Pareto, SAGE per-item paired test, CVaR over people, GroupDRO-weighted mean, a Prompt Risk Control-style bound, aACP-style approval, Hu and Tang fresh-holdout rescoring, the cumulative per-group rule.
- Generality across loop families: a GEPA-style prompt optimizer, a Meta-Harness or DGM-style code optimizer, optionally a rejection-sampling self-training loop; describe DGM and HGM selection accurately (archive, score and child-count parent sampling; clade success rates) and treat Pareto as vector selection.
- Tool-route attribution by counterfactual swaps: revert single accepted tool or parameter edits on tail people only and measure recovered tail error. Phrase tail-specific tool failures as hypotheses.
- Compute: about 4 generations x 200 edits x 5 folds of panel evaluation with cached tool outputs (OpenCap Monocular about 3.8 minutes per clip on an H100 if not cached).
