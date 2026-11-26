# Theory checks for proposals 05, 06, 07 and 08

Status: COMPLETE (2026-11-24). All checks A1 to D done; corrections for the briefs are collected at the end.

Scripts live in `output/idea-summaries-build/sim/`. Every number below comes from those scripts with fixed seeds. Run any script with `uv run --no-project --with scipy==1.13.1 --with numpy==1.26.4 python <script>.py` from that directory; each writes a `<script>_results.json` next to itself.

## A. Proposal 06 (tail drift)

### A1. Closed form for $\mathbb{E}[b \mid S>0]$ under the mean rule

**Setting.** A candidate edit has true mean loss reductions $a$ (majority) and $b$ (tail), jointly Gaussian with means $\mu_a,\mu_b$, standard deviations $\sigma_a,\sigma_b$ and correlation $\rho$. The loop sees $\hat a=a+e_a$ and $\hat b=b+e_b$ with $e_a\sim N(0,s_a^2)$, $e_b\sim N(0,s_b^2)$, independent of each other and of $(a,b)$. With per-person variance $v$ of the loss difference, $s_a^2=v/n_A$ and $s_b^2=v/n_B$. The mean rule accepts if $S=w\hat a+(1-w)\hat b>0$ with $w=n_A/(n_A+n_B)$.

**Derivation.** $(b,S)$ is bivariate Gaussian, so $\mathbb{E}[b\mid S]=\mu_b+\beta(S-\mu_S)$ with $\beta=\mathrm{Cov}(b,S)/\sigma_S^2$. Taking the expectation over $S>0$ and using $\mathbb{E}[Z\mid Z>c]=\phi(c)/(1-\Phi(c))$ for standard normal $Z$ with $c=-\mu_S/\sigma_S$:

$$\mathbb{E}[b\mid S>0]=\mu_b+\frac{\mathrm{Cov}(b,S)}{\sigma_S}\,\lambda\!\left(\frac{\mu_S}{\sigma_S}\right),\qquad \lambda(z)=\frac{\phi(z)}{\Phi(z)},$$

$$\mathrm{Cov}(b,S)=w\rho\sigma_a\sigma_b+(1-w)\sigma_b^2,\quad \mu_S=w\mu_a+(1-w)\mu_b,\quad \sigma_S^2=w^2(\sigma_a^2+s_a^2)+(1-w)^2(\sigma_b^2+s_b^2)+2w(1-w)\rho\sigma_a\sigma_b .$$

The noise terms enter only $\sigma_S$, because $e_a,e_b$ are independent of $b$. The expected tail change per proposed edit (the drift per generation for a one-candidate loop) is

$$\mathbb{E}[b\,\mathbf 1\{S>0\}]=\mu_b\,\Phi(\mu_S/\sigma_S)+\frac{\mathrm{Cov}(b,S)}{\sigma_S}\,\phi(\mu_S/\sigma_S).$$

**Sign condition.** The selection term has the sign of $\mathrm{Cov}(b,S)$, which is negative exactly when $\rho<\rho^*:=-(1-w)\sigma_b/(w\sigma_a)$. So: if $\mu_b\le 0$ and $\rho<\rho^*$, then $\mathbb{E}[b\mid S>0]<0$. Two remarks the brief should carry. (i) The condition is sufficient, not necessary. When $\mu_b<0$ (most random edits slightly hurt the tail, which is the usual case near a good harness) the tail can degrade per accepted edit even with $\rho>\rho^*$, because weak selection does not overcome the negative mean. (ii) The threshold $\rho^*$ does not depend on the estimation noise; noise only shrinks the size of the selection term through $\sigma_S$. If $(1-w)\sigma_b\ge w\sigma_a$, no correlation in $[-1,1]$ satisfies the sufficient condition. StaBLE-like numbers: $n_A=140$, $n_B=20$ gives $w=0.875$ and $\rho^*=-0.143$ when $\sigma_b=\sigma_a$, $-0.286$ when $\sigma_b=2\sigma_a$, $-0.571$ when $\sigma_b=4\sigma_a$. A mild negative correlation is enough when the tail is one eighth of the dev set.

**Numerical check** (`sim/a1_drift_formula.py`, seed 20261124). Grid: $\rho\in\{-0.9,-0.6,-0.3,0,0.3,0.6,0.9\}$, $w\in\{0.5,0.8,0.9,0.95\}$, $\sigma_b/\sigma_a\in\{0.5,1,2,4\}$, three noise levels (per-person noise sd $0$, $0.5\sigma_a$, $2\sigma_a$ at a 20-person scale, so $s_a,s_b$ range from 0 to well above $\sigma_a$), and four mean pairs $(\mu_a,\mu_b)\in\{(0,0),(-0.5,-0.5),(0.3,-0.3),(-1,0.2)\}$; 1344 cells, 400,000 draws per cell.

| Quantity | Value |
|---|---|
| max $\lvert$closed form $-$ MC$\rvert$ | 0.023 $\sigma_a$ (cell with $\sigma_b=4\sigma_a$, so 0.6% of $\sigma_b$) |
| max $\lvert$error$\rvert$ / MC standard error | 3.46 (expected maximum over 1344 cells for a correct formula is about 3.3 to 3.8) |
| mean $\lvert$error$\rvert$ / MC standard error | 0.78 (0.80 expected) |
| cells meeting the sufficient condition | 297, with 0 violations |
| cells with negative tail drift outside the sufficient condition | 255: 183 with $\mu_b<0$ and $\mathrm{Cov}(b,S)>0$ (weak selection, mostly the high-noise level), 72 with $\mu_b>0$ and $\mathrm{Cov}(b,S)<0$ |

Verdict: the formula is exact under the stated model, and the brief's sign condition is correct as a sufficient condition.

### A2. Best-of-$K$ selection (winner's curse)

**Setting.** Each round draws $K$ independent candidates $(a_k,b_k,S_k)$ as in A1, picks $k^*=\arg\max_k S_k$ and accepts if $S_{k^*}>0$.

**Exact result.** Because candidates are independent, $\mathbb{E}[b_k\mid S_1,\dots,S_K]=\mu_b+\beta(S_k-\mu_S)$, so $\mathbb{E}[b_{k^*}\mid S_1,\dots,S_K]=\mu_b+\beta(S_{(K)}-\mu_S)$ where $S_{(K)}$ is the maximum. Hence

$$\mathbb{E}[b_{k^*}\mid S_{(K)}>0]=\mu_b+\frac{\mathrm{Cov}(b,S)}{\sigma_S}\,m_K(c),\qquad c=-\frac{\mu_S}{\sigma_S},\qquad m_K(c)=\mathbb{E}[Z_{(K)}\mid Z_{(K)}>c]=\frac{\int_c^\infty zK\phi(z)\Phi(z)^{K-1}dz}{1-\Phi(c)^K},$$

with $Z_{(K)}$ the maximum of $K$ standard normals. $K=1$ recovers A1. The sign of the selection term is still the sign of $\mathrm{Cov}(b,S)$, and $m_K(c)$ increases in $K$. So best-of-$K$ amplifies whichever direction the selection term points: it makes tail harm worse when $\mathrm{Cov}(b,S)<0$ and makes tail gains larger when $\mathrm{Cov}(b,S)>0$. Per round, the acceptance probability also rises to $1-\Phi(c)^K$.

**Approximations.** (a) Treat $Z_{(K)}$ as $N(e_K,v_K)$ with Blom's $e_K=\Phi^{-1}((K-0.375)/(K+0.25))$; then $m_K(c)\approx e_K+\sqrt{v_K}\,\lambda((e_K-c)/\sqrt{v_K})$. Quadrature values of $v_K$: 0.682 ($K=2$), 0.448 (5), 0.344 (10), 0.276 (20), 0.216 (50); the Gumbel limit $\pi^2/(12\ln K)$ is within 15% for $K\ge5$. (b) A two-regime rule needs no $v_K$: $m_K(c)\approx\max\{e_K,\ \phi(c)/(1-\Phi(c))\}$. A lenient threshold ($c\ll e_K$) gives the mean of the maximum, about $\sqrt{2\ln K}$ for large $K$ (Blom is far more accurate at small $K$); a strict threshold ($c\gg e_K$) gives a single exceedance, the same as $K=1$.

**Numerical check** (`sim/a2_best_of_k.py`, seed 7). 720 cells: $K\in\{1,2,5,10,20,50\}$, $\rho\in\{-0.8,-0.4,0,0.4,0.8\}$, $w\in\{0.8,0.9\}$, $\sigma_b/\sigma_a\in\{1,2\}$, two noise levels, three mean pairs; at least 400,000 candidate draws per cell.

| Quantity | Value |
|---|---|
| exact formula vs MC: max $\lvert$error$\rvert$ | 0.038 $\sigma_a$; max $\lvert z\rvert$ = 2.85, mean $\lvert z\rvert$ = 0.85 |
| approximation (a) vs exact | max 0.056 $\sigma_a$, median 0.003 $\sigma_a$ |
| approximation (b) vs exact, error in $m_K$ | max 0.165 (at $K=5$, $c=0.5$, the crossover between regimes) |

Selection factor $m_K(c)$ (exact):

| $c=-\mu_S/\sigma_S$ | $K=1$ | 2 | 5 | 10 | 20 | 50 |
|---|---|---|---|---|---|---|
| $-1$ (lenient) | 0.29 | 0.61 | 1.16 | 1.54 | 1.87 | 2.25 |
| $0$ | 0.80 | 0.91 | 1.21 | 1.54 | 1.87 | 2.25 |
| $+1$ (strict) | 1.53 | 1.55 | 1.61 | 1.71 | 1.90 | 2.25 |

At $c=0$, $\mu_b=0$ and $\mathrm{Cov}(b,S)/\sigma_S=-0.1$, the expected tail change per round is $-0.040$ for $K=1$, $-0.117$ for $K=5$ and $-0.225$ for $K=50$: the per-round harm grows about 5.6-fold from $K=1$ to $K=50$, through both a larger selection factor and near-certain acceptance. Conversely, with $\mu_b=-0.2$, $\rho=0.3$, $w=0.9$ (so $\mathrm{Cov}(b,S)>0$), the accepted edit's tail effect rises from $+0.40$ at $K=1$ to $+0.69$ at $K=50$.

Verdict: the brief's phrase "best-of-$K$ sharpens the effect" is right only in magnitude. Replace it with: best-of-$K$ multiplies the selection term by $m_K(c)/\lambda(\mu_S/\sigma_S)$, which grows like $\sqrt{2\ln K}$ under lenient thresholds; it worsens the tail only when $\mathrm{Cov}(b,S)<0$.

### A3. Multi-generation loop with falling $\rho$ (inverted U)

Script `sim/a3_multigen.py` (seed 31), four parts.

**Part 1, phenomenological loop.** One candidate per generation, Gaussian $(a,b)$ as in A1, with the correlation tied to the cumulative true majority gain $G_t$: $\rho(G)=\rho_\infty+(\rho_0-\rho_\infty)e^{-G/G_0}$, so shared improvements are used up as the majority improves. Settings: $\rho_0=0.8$, $G_0=20$, $\mu_a=\mu_b=-0.25$ (most random edits hurt a little), $\sigma_a=\sigma_b=1$, A1-style noise at 160 people ($s_a=0.24$, $s_b=0.63$ at $w=0.875$), 400 generations, 4000 replicate loops. The prediction is a mean-field recursion that adds $\mathbb{E}[a\mathbf 1\{S>0\}]$ and $\mathbb{E}[b\mathbf 1\{S>0\}]$ (A1 formulas at $\rho(G_t)$) each generation.

Define $\rho_{\text{crit}}$ as the root of the per-edit tail drift $\mu_b\Phi(z)+\frac{\mathrm{Cov}(b,S)}{\sigma_S}\phi(z)=0$. It was $-0.872$, $-0.066$, $+0.128$ and $+0.217$ for $w=0.5$, $0.75$, $0.875$, $0.95$.

| Result | Value |
|---|---|
| cells with an inverted U in the MC mean tail trajectory | 11 of 20, exactly the cells with $\rho_\infty<\rho_{\text{crit}}<\rho_0$ |
| agreement of the inverted-U call, MC vs mean-field | 20 of 20 |
| peak generation, MC vs mean-field | within 0 to 8 generations (MC slightly later) |
| max trajectory error, MC vs mean-field | 1.21 on trajectories of size up to 110 (about 1%) |

Two lessons. When $\mu_b<0$ the critical correlation lies above the A1 sufficient threshold (at $w=0.875$: $\rho_{\text{crit}}=+0.128$ against $\rho^*=-0.143$), so tail harm can begin while edit effects are still positively correlated. And an inverted U does not imply the loop ends below its start: at $w=0.875$, $\rho_\infty=0$ the tail peaked at generation 138 and ended at $+2.6$, still above generation 0.

**Part 2, mechanistic loop (Fisher geometric model).** Harness state $x\in\mathbb{R}^{10}$, group losses $L_A=\lVert x-x_A\rVert^2$ and $L_B=\lVert x-x_B\rVert^2$ with $\lVert x_A-x_B\rVert=1$, $w=0.875$, mean-loss optimum $x_w=wx_A+(1-w)x_B$, edits $\delta\sim N(0,\tau^2I)$ with total size 0.1, start 3 units from $x_w$ at angle $\theta$ to the axis that runs from $x_B$ toward $x_A$, noise sd 0 or 0.05 ($s_b=0.14$), 1500 generations, 400 replicates.

Derivation. With $g_A=x-x_A$ and $g_B=x-x_B$, $a=-2g_A\cdot\delta-\lVert\delta\rVert^2$, so $\mu_a=\mu_b=-d\tau^2$, $\mathrm{Var}(a)=4\tau^2\lVert g_A\rVert^2+2d\tau^4$ and $\mathrm{Cov}(a,b)=4\tau^2g_A\cdot g_B+2d\tau^4$. Hence $\rho\approx\cos\angle(g_A,g_B)$, which falls from about $+1$ far from both optima toward $-1$ near $x_w$ (where the two gradients are antiparallel). The selection term is

$$\mathrm{Cov}(b,S)=4\tau^2\,(x-x_B)\cdot(x-x_w)+2d\tau^4 ,$$

whose leading term is negative exactly when $x$ lies inside the ball whose diameter joins the tail optimum $x_B$ and the mean optimum $x_w$. More generally, for edit covariance $\Sigma_\delta$ the leading term is $\nabla L_B^\top\Sigma_\delta\nabla L_w$: the tail is harmed by selection when the tail gradient and the mean-objective gradient conflict in the metric of the proposal distribution. This gives three regimes, set by where the seed harness sits relative to the tail optimum:

| Start (noise 0) | Tail trajectory | Tail loss start / min / end | Peak gen (observed) | First gen with predicted harm |
|---|---|---|---|---|
| majority side, $\theta=0$ | monotone gain | 15.02 / 0.77 / 0.77 | none | none |
| perpendicular, $\theta=90°$ | monotone gain | 9.77 / 0.77 / 0.77 | none | none |
| tail side, $\theta=150°$ | inverted U | 5.22 / 0.43 / 0.77 | 199 | 197 |
| tail side, $\theta=180°$ | inverted U | 4.52 / 0.25 / 0.77 | 183 | 183 |
| inside the ball | decline from generation 0 | 0.19 / 0.19 / 0.77 | 0 | 0 |

The mean loss fell monotonically in every run (9.11 to 0.11), and $\rho$ fell from about $+1$ to $-0.78$ in every regime, including the two with no tail harm. A falling $\rho$ is therefore not sufficient for an inverted U: the threshold $\rho^*_t=-(1-w)\sigma_{b,t}/(w\sigma_{a,t})$ also falls as the majority's remaining gains shrink. With noise 0.05 the same three regimes appear (peaks at 232 and 203, predicted first harm at 221 and 205), plus a small mutation-load decline in all regimes: tail loss rose 0.016 to 0.027 after its minimum for the majority-side and perpendicular starts, against 0.44 to 0.61 for the tail-side starts.

Drift prediction. Applying the A1 formula to the local moments at each replicate's current state predicted the cumulative tail change to within 0.05 to 0.25 (at most 4% of the trajectory range, except 26% for the small-range inside-ball case without noise), with per-generation correlation 0.98 to 1.00 between predicted and realized drift (0.61 in the noisy inside-ball case, where the drift is tiny), and placed the peak within 0 to 11 generations. At the observed peaks $\rho_t$ was still $+0.10$ to $+0.34$ while $\rho^*_t\approx-0.1$; with finite edit size $\mu_b<0$, so harm starts before $\rho_t$ reaches $\rho^*_t$, as in Part 1.

This also reconciles the Cooper and Lenski observation (unused functions lost mostly early; Nature 2000, verified in `research/06-tails-literature-stats.md`) with the late-specialization prediction: early loss is regime 3 (the seed already sits near the tail optimum), late loss is regime 2.

**Part 3, measuring $\rho$ from an edit panel.** With estimation noise the naive panel correlation is attenuated, $\rho_{\text{obs}}=\rho\sigma_a\sigma_b/\sqrt{(\sigma_a^2+s_a^2)(\sigma_b^2+s_b^2)}$. Simulation with 200 edits confirmed the formula: true $\rho=0.6$ gives naive 0.53, 0.40, 0.21 for $s_b/\sigma_b=0.5,1,2$. Subtracting the known noise variances removes the bias (0.60, 0.60, 0.63) but leaves sd 0.06, 0.09, 0.22.

**Part 4, estimating the drift directly.** The prediction needs $\mathbb{E}[b\mathbf 1\{S>0\}]$, not $\rho$. Evaluate each panel edit on the loop's own dev people (to get the decision the loop would make, $\mathbf 1\{S_{\text{dev}}>0\}$) and on disjoint panel people (to get its tail effect $\hat b_{\text{panel}}$). The average of $\hat b_{\text{panel}}\mathbf 1\{S_{\text{dev}}>0\}$ is unbiased without any Gaussian assumption, because panel noise has mean zero and is independent of dev-set noise. In simulation (200 edits, $\mu=-0.25$, $w=0.875$) the direct estimator was within 0.004 of the truth in all nine cells (inside Monte Carlo error), and the Gaussian plug-in with noise-corrected moments was within 0.008 (a small bias at $s_b=2\sigma_b$ from clipping the corrected variances); the direct estimator's sd was 10% to 15% larger (for example 0.049 against 0.043 at $\rho=0$, $s_b=0.5\sigma_b$). With 200 edits the sd is 0.05 to 0.10 $\sigma_a$, so the smallest per-edit drift detectable at 80% power is about 0.13 to 0.29 $\sigma_a$. Panels near the drift's sign change will need more edits or pooled generations.

### A4. Cumulative tail-harm guarantee

**Statement.** Let $H(h)$ be the population mean tail loss of harness $h$ minus that of the seed $h_0$ (positive means harm). At round $t$ the loop forms a candidate $h'_t$ and accepts it only if the estimated majority gain is positive and a one-sided test $\varphi_t$ rejects $H_{0,t}:H(h'_t)\ge M$. Let $\mathcal F_{t-1}$ hold everything that determined $h'_t$ (seed, proposer randomness, majority data, all earlier gate data). Assume

(G1) conditional validity: on the event $\{H(h'_t)\ge M\}$, $\Pr(\varphi_t=1\mid\mathcal F_{t-1})\le\alpha_t$;
(G2) spending: $\sum_t\alpha_t\le\alpha$, summed over every gate test run, not over rounds (a round that gates several candidates spends once per candidate).

Then $\Pr(\text{some accepted parent has }H>M)\le\alpha$. In particular the final harness is more than $M$ worse than the seed on the tail with probability at most $\alpha$, and the same bound holds at every intermediate generation.

**Proof.** An accepted parent with $H>M$ was accepted at a round where $H_{0,t}$ held and $\varphi_t$ rejected. So the bad event lies in $\bigcup_t\{\varphi_t=1,\ H(h'_t)\ge M\}$. Since $h'_t$ is $\mathcal F_{t-1}$-measurable, $\Pr(\varphi_t=1,\,H(h'_t)\ge M)=\mathbb{E}[\mathbf 1\{H(h'_t)\ge M\}\Pr(\varphi_t=1\mid\mathcal F_{t-1})]\le\alpha_t$. A union bound finishes it.

(G1) holds when the round-$t$ gate uses tail people whose data are independent of $\mathcal F_{t-1}$ (fresh people, sealed from the proposer, which sees only accept or reject) and $\varphi_t$ is an exact or conservative level-$\alpha_t$ test for the per-person harm distribution at that sample size. Comparing every candidate with $h_0$ (not with the current parent) is what blocks creep; this is the clinical-trials fix for "bio-creep" in chains of non-inferiority trials (Feng, Emerson and Simon, arXiv 1912.12413).

**Simulation** (`sim/a4_guarantee.py`, seed 424242, 20,000 loops per cell). Model: tail person $i$'s loss change from edit $e$ is $h_e+u_{ie}$ with $u_{ie}$ independent across edits and people, sd $\sigma_u=0.25$; a harness's per-person cumulative harm sums over the edits in its lineage. Edits have majority gain $a\sim N(0.2,0.1^2)$ and tail harm $h\sim N(0.1,0.1^2)$ (a loop pushing against the margin) or $N(0,0.1^2)$ (tail-neutral on average). $M=0.5$, 50 rounds, $\alpha=0.05$, $\alpha_t=\alpha/50$, one-sided $t$ test, 140 majority people. Per-person noise laws: normal; Student $t_3$; lognormal (right-skewed); a rare-harm mixture in which 10% of tail people are hurt by $+3$ sd units and the rest gain $1/3$ (mean 0, sd 1).

1. The one-sided $t$ test itself, at the null boundary (400,000 replicates):

| Noise | $n=5$ | $n=10$ | $n=20$ |
|---|---|---|---|
| normal, nominal 0.05 / 0.001 | 0.049 / 0.0010 | 0.051 / 0.0010 | 0.050 / 0.0009 |
| $t_3$, nominal 0.05 / 0.001 | 0.041 / 0.0006 | 0.045 / 0.0005 | 0.048 / 0.0006 |
| lognormal, nominal 0.05 / 0.001 | 0.23 / 0.039 | 0.21 / 0.051 | 0.17 / 0.043 |
| rare-harm mixture, any nominal level | 0.59 | 0.35 | 0.12 |

Symmetric heavy tails make the test conservative. Right skew in harm (a few people hurt badly, which is the clinically realistic case: an occlusion-sensitive pose model fails for the walker users) makes it anti-conservative, by a factor of 40 to 50 at the small per-round levels alpha-spending requires. For the rare-harm mixture the realized level is the chance that no harmed person is in the sample, $0.9^{n}$, whatever the nominal level: no test can see a harm that touches nobody it observes. Only a bound on per-person harm restores validity; with loss range $L$, a Hoeffding test needs a margin of $2L\sqrt{\ln(1/\alpha_t)/(2n)}=0.83L$ at $n=20$, $\alpha_t=0.001$, which is useless.

2. The loop, push regime ($h\sim N(0.1,0.1^2)$), normal noise. "P(bad)" is the probability that some accepted parent (or the deployed checkpoint, for certification) has $H>M$:

| Gate | $n_B=5$: P(bad) / majority gain kept | $n_B=10$ | $n_B=20$ |
|---|---|---|---|
| none (majority only) | 1.000 / 9.84 | 1.000 / 9.84 | 1.000 / 9.84 |
| per-step non-inferiority vs current parent, margin $M$ | 1.000 / 8.36 | 1.000 / 9.61 | 1.000 / 9.79 |
| oracle (knows true $H$) | 0 / 3.87 | 0 / 3.84 | 0 / 3.86 |
| cumulative test, fresh people each round | 0.0003 / 0.45 | 0.0006 / 0.94 | 0.0013 / 1.37 |
| cumulative test, same people every round | **0.18** / 1.22 | **0.29** / 2.38 | **0.11** / 2.72 |
| fold retirement, 2 folds | 0 / 0.05 | 0.0001 / 0.33 | 0 / 0.41 |
| checkpoint certification, fixed sequence | 0.018 / 0.38 | 0.019 / 0.54 | 0.016 / 0.66 |
| checkpoint certification, Bonferroni | 0.0013 / 0.05 | 0.0009 / 0.23 | 0.0006 / 0.42 |

Reusing the same tail people breaks the guarantee: realized error 0.11 to 0.29 against a nominal 0.05. The mechanism is selection on the sample: a parent is accepted because its sample harm looked low, that downward bias is inherited by every descendant tested on the same people, and the loop keeps accepting until the sample (not the population) reaches the margin. With fresh people the bound holds with room to spare (0.0003 to 0.0013; the union bound is loose because most candidates are far from the margin). Per-step non-inferiority creeps to certain failure.

3. Under right-skewed harm the same rules fail through the test, not the design: fresh-people gating gave 0.58 ($n_B=5$), 0.084 (10), 0.031 (20) under the rare-harm mixture, and 0.027, 0.049, 0.040 under lognormal harm; fixed-sequence certification gave 0.084, 0.048, 0.032 (mixture) and 0.067, 0.055, 0.037 (lognormal). The guarantee is credible at $n_B\ge20$ only, and only if per-person harm is not dominated by rare large failures.

4. Price of protection, tail-neutral regime ($h\sim N(0,0.1^2)$, normal noise). The majority-only loop ends with mean tail change 0 yet crosses the margin at some point in 41% of loops, because the tail effects random-walk. Majority gain kept, out of 9.84 unconstrained and 9.54 for the oracle: fresh-people gating 0.89, 3.05, 5.59 for $n_B=5,10,20$; fixed-sequence certification 1.44, 2.86, 4.15. In the push regime the oracle itself keeps only 3.87, and the valid rules keep 0.4 to 1.4. The cost is driven by the per-round level $\alpha/T$ and by the per-person noise of cumulative harm growing with lineage length; it falls quickly with more tail people. The spending schedule matters: $\alpha_t=6\alpha/(\pi^2t^2)$ instead of $\alpha/T$ cut the kept gain at $n_B=20$ from 1.37 to 0.91.

**Which assumptions break, and the fixes.**

- Reuse of the same tail people across rounds violates (G1). This is the holdout-reuse problem of adaptive data analysis (Dwork et al., arXiv 1506.02629; Blum and Hardt's Ladder, arXiv 1502.04585): limiting what the gate reveals (accept or reject bits, added noise, Ladder-style thresholds) reduces the bias, but a formal bound then has to count the information released, which at 50 rounds and $n_B\le20$ leaves little power. Valid fixes: (a) fresh tail people per gated round, possible only in a large-tail second domain; (b) fold retirement: split the tail people into folds and retire a fold once it certifies an acceptance (rejections may reuse it if the proposer sees only "rejected"); valid, but it allows at most as many acceptances as folds, so it is nearly powerless at StaBLE sizes; (c) checkpoint certification: let the loop run under any internal rule, freeze its checkpoints $h_1,\dots,h_T$ (determined by dev data only), then test them on sealed tail people never shown to the loop, by fixed-sequence testing in generation order at full $\alpha$ (stop at the first failure and deploy the last checkpoint that passed). Fixed-sequence testing controls family-wise error under any dependence, and in simulation it was the most useful valid option at $n_B\le20$. This is a terminal guarantee about the deployed harness, not a trajectory guarantee about the loop.
- Cross-fitting does not restore (G1) for a single sequential loop, because every fold's data eventually influence the parent. It remains the right tool for the edit-effect panels (A3, Part 4). A cross-fitted variant that is valid: run one loop per fold, each certified on its own held-out fold; each loop's certificate is valid on its own, but choosing among the loops by their certificates needs a further Bonferroni split.
- An e-process (for example a betting e-value for bounded harm, Waudby-Smith and Ramdas, arXiv 2010.09686) makes each round's test valid under optional stopping, so tail people or extra trials can be added until the decision is clear. It does not fix reuse, and across rounds the e-value thresholds $1/\alpha_t$ still need $\sum_t\alpha_t\le\alpha$. Alpha-investing, as in the bio-creep paper, can recover some of the power the union bound wastes.
- Validity of the per-round test at small $n_B$ (see table 1). Pre-register a test that is valid for the per-person harm distribution actually expected, check skew on the pilot, pool the 18 tasks within each person (this reduces task-level noise but not person-level skew), and report the guarantee as conditional on $n_B\ge20$ and on the absence of rare large per-person failures, or switch to a bounded test and accept its margin.
- The proposer must not see gate traces or per-person gate results; otherwise the candidate depends on gate data through a channel the union bound does not count.

## B. Proposal 08 (blind analysis)

### B1. Double counting proposition

**Setting.** Class $C\in\{0,1\}$ (for example high fall risk). Referral $H\in\{0,1\}$ with $\Pr(H=1)=1/2$, wrong with probability $q$: $\Pr(C=H\mid H)=1-q$, so the decision maker's prior is $\pi_H=\Pr(C=1\mid H)$, equal to $1-q$ or $q$. Latent truth $T\mid C\sim N(\mu_C,\tau^2)$ with $\mu_1-\mu_0=\Delta$. Blind measurement $M_0=T+e$, $e\sim N(0,s^2)$ independent of $(T,H)$. The decision maker's likelihood is calibrated on blind measurements, $f(m\mid C)=N(\mu_C,V)$ with $V=\tau^2+s^2$. The agent reports $M_\gamma=(1-\gamma)M_0+\gamma m_H$ with $m_H=\mu_H$, and the decision maker computes $p_\gamma$ by Bayes' rule from $\pi_H$ and $f$ evaluated at $M_\gamma$.

**Proposition.** (i) If $0<q<1$, the decision maker's expected log loss is strictly larger with $M_\gamma$ than with $M_0$ for every $\gamma\neq0$ (negative values and $\gamma\ge1$ included). (ii) $\mathrm{MSE}(\gamma)=\mathbb{E}[(M_\gamma-T)^2]=(1-\gamma)^2s^2+\gamma^2(\tau^2+q\Delta^2)$, minimized at

$$\gamma^*=\frac{s^2}{s^2+\tau^2+q\Delta^2},\qquad \frac{\mathrm{MSE}(\gamma^*)}{\mathrm{MSE}(0)}=\frac{\tau^2+q\Delta^2}{s^2+\tau^2+q\Delta^2},$$

and $\mathrm{MSE}(\gamma)<\mathrm{MSE}(0)$ for every $0<\gamma<2\gamma^*$. So for any $s>0$ some $\gamma>0$ lowers MSE while raising decision loss.

**Proof.** (i) Because $M_0\perp H\mid C$ and $f$ is the true law of $M_0\mid C$, $p_0=\Pr(C=1\mid H,M_0)$ is the true posterior. $p_\gamma$ is some other function of $(H,M_0)$, and for log loss $\mathbb{E}[\ell(p_\gamma,C)]-\mathbb{E}[\ell(p_0,C)]=\mathbb{E}\big[\mathrm{KL}(\mathrm{Bern}(p_0)\,\Vert\,\mathrm{Bern}(p_\gamma))\big]\ge0$ (strict propriety), with equality only if $p_\gamma=p_0$ almost surely. With Gaussian equal-variance classes the log-likelihood ratio is linear, $\mathrm{LLR}(m)=\frac{\Delta}{V}(m-\frac{\mu_0+\mu_1}{2})$, so

$$\operatorname{logit}p_\gamma=\operatorname{logit}\pi_H+\gamma\,\frac{\Delta^2}{2V}\,(2H-1)+(1-\gamma)\,\mathrm{LLR}(M_0).$$

This differs from $\operatorname{logit}p_0$ unless $M_0=m_H$, a null event, so the KL term is positive with probability one. (ii) $M_\gamma-T=(1-\gamma)e+\gamma(m_H-T)$; the cross term vanishes because $e$ is independent of $(T,H)$ with mean zero, and $\mathbb{E}[(m_H-T)^2]=\tau^2+q\Delta^2$. $\square$

The displayed logit is the plain-words reading: a report shrunk toward the referral is equivalent to adding $\gamma\Delta^2/(2V)$ to the prior log-odds in the referral's direction and multiplying the evidence weight by $1-\gamma$. The referral is counted once by the clinician and again inside the number.

**Generalization.** (i) needs only: $M_0\perp H\mid C$; $f$ equal to the true class-conditional law of $M_0$; a strictly monotone likelihood ratio; $M_0$ continuous; $0<\pi_H<1$ with positive probability; and the decision maker does not know $\gamma$. (ii) needs only $e$ independent of $(T,H)$ with mean zero, with $\tau^2+q\Delta^2$ replaced by $\mathbb{E}[(m_H-T)^2]$.

**Numerical check** (`sim/b1_double_counting.py`, seed 808). Quadrature over $M_0$ on 36 cells ($\Delta/\tau\in\{1,2,3\}$, $s/\tau\in\{0.5,1,2\}$, $q\in\{0.1,0.2,0.3,0.5\}$), each at ten values of $\gamma$ from $-0.5$ to $1.5$: 0 violations of strictness in 360 checks. Quadrature agreed with 2,000,000-case Monte Carlo to within 0.001 nats, and the MSE formula to within 0.003.

Worked example, $\Delta=2\tau$, $s=\tau$, $q=0.2$: $\gamma^*=0.357$, MSE falls by 36% (ratio 0.643), expected log loss rises from 0.365 to 0.391 nats (+0.026, +7.2%), and the error rate at threshold 1/2 rises from 0.158 to 0.181. The penalty is concentrated on people whose referral is wrong: $+0.353$ nats for them against $-0.056$ for people whose referral is right. Across the grid, the penalty at $\gamma^*$ ranged from $+0.001$ to $+0.064$ nats (0.3% to 23% of the blind log loss), largest when classes are well separated, measurement noise is moderate and referrals are usually right ($\Delta=3\tau$, $s=\tau$, $q=0.1$: +23%).

| $\gamma$ (worked example) | 0 | 0.1 | 0.2 | 0.357 | 0.5 | 1.0 |
|---|---|---|---|---|---|---|
| MSE | 1.000 | 0.828 | 0.712 | 0.643 | 0.700 | 1.800 |
| log-loss penalty (nats) | 0 | 0.002 | 0.008 | 0.026 | 0.052 | 0.201 |
| error rate | 0.158 | 0.160 | 0.165 | 0.181 | 0.195 | 0.200 |

**Recalibration and the scope of the claim.** If the likelihood is refitted on context-aware measurements pooled over referrals, the penalty shrinks but stays positive in all 36 cells (it is still a function that ignores the dependence of $M_\gamma$ on $H$ given $C$). If it is refitted separately for each referral value, the penalty is zero for $\gamma<1$, because $M_\gamma$ is then an invertible function of $M_0$ within each stratum; this remedy requires $\gamma$ to stay fixed, which is exactly what a self-improvement loop does not guarantee. Finally, the harm requires a decision maker who already uses the referral. One who ignores it (flat prior) does better with context-aware measurement: in the worked example its log loss falls from 0.492 at $\gamma=0$ to 0.439 at $\gamma=0.5$, though it remains worse than the Bayes combination of prior and blind measurement (0.365). The brief should say which decision maker it models.

### B2. Path splicing identification

**Setting.** For video $v$, framing $F\in\{a,b\}$ is randomized. A run has a path phase that produces a transcript $Z=(P,O)$ (tool calls with arguments, and tool outputs) from a policy $\pi(z\mid v,f)$, and a report step that produces $M$ from a report kernel $r(m\mid v,f_{\text{rep}},z)$. A splice $(f_{\text{path}}\to f_{\text{rep}})$ draws $Z$ from a run under $f_{\text{path}}$ and calls the report step under $f_{\text{rep}}$ with that $Z$ in context and fresh report-step randomness. Define the four cells

$$\mu_v(f_{\text{path}},f_{\text{rep}})=\int \mathbb{E}[M\mid v,f_{\text{rep}},z]\;\pi(dz\mid v,f_{\text{path}}).$$

**Assumptions.** (S1) Context sufficiency: the report step depends on the path phase only through what is placed in its context (a stateless call; no memory, cache or server-side state carried across). (S2) Splice consistency: a spliced context has the same format as a natural one, so the report kernel applied to it is the kernel natural runs use. (S3) No framing leakage: the spliced transcript encodes $F$ only through the agent's own choices; free text that restates the referral is either stripped or declared part of the mediator. (S4) Tool outputs are deterministic given $(v,P)$ and cached, or are cached as part of $Z$.

**Result.** Under (S1) to (S4) all four cells are identified by running them, with no modelling assumption. The natural cells are $\mu_v(a,a)$ and $\mu_v(b,b)$, and

$$\mathrm{TE}=\mu(b,b)-\mu(a,a)=\underbrace{\mu(a,b)-\mu(a,a)}_{\mathrm{IDE}_a}+\underbrace{\mu(b,b)-\mu(a,b)}_{\mathrm{IIE}_b}=\underbrace{\mu(b,a)-\mu(a,a)}_{\mathrm{IIE}_a}+\underbrace{\mu(b,b)-\mu(b,a)}_{\mathrm{IDE}_b},$$

and the two orderings differ by the interaction $\mu(b,b)-\mu(b,a)-\mu(a,b)+\mu(a,a)$. Path splicing is a two-by-two factorial with framing at the path stage crossed with framing at the report stage, and should be analyzed and reported that way.

**What is identified when paths are random.** $\mathrm{IDE}_a=\mathbb{E}_{Z\sim\pi(\cdot\mid v,a)}[\mathrm{CDE}_v(Z)]$ with $\mathrm{CDE}_v(z)=\mathbb{E}[M\mid v,b,z]-\mathbb{E}[M\mid v,a,z]$: the controlled direct effect averaged over the path distribution under $a$. These are the mediation-formula (randomized interventional) direct and indirect effects. In observational mediation they need sequential ignorability or a cross-world assumption; here they are identified by intervention, because the harness physically draws $Z$ from one framing and the report noise independently. What is not identified is any unit-level natural effect (what this particular run would have reported under $b$ with its own path), since a stochastic generator has no defined cross-world counterfactual without a coupling of random seeds. A controlled direct effect at one specific path $z$ is identified by replaying that same $z$ many times under each framing. For a multi-step path, splicing a prefix $z_{1:k}$ from $a$ and letting the agent continue under $b$ identifies path-specific effects through the later steps.

**Numerical check** (`sim/b2_path_splicing.py`, seed 2026; 400 videos, 200 runs per video and cell). Toy agent: $P\in\{0,1\}$ (trim at first large excursion), $\Pr(P=1)=0.7$ under $a$ and $0.3$ under $b$; tool output $O=\theta_v-0.6P+\eta_{v,P}$ cached per video and path; report $M=O-0.3\cdot\mathbf 1[F_{\text{rep}}=a]+\dots+\varepsilon$. Cell Monte Carlo SE is about 0.001 to 0.003.

| Variant | Splice vs truth (max abs error over TE, IDE, IIE, both orderings, interaction) | Self-splice placebo, natural $(a,a)$ minus splice $(a\to a)$ |
|---|---|---|
| V1 ideal (TE 0.552 = IDE 0.300 + IIE 0.252) | 0.0016 | $-0.0005$ |
| V2 framing by path interaction ($\iota=-0.4$; interaction $-0.160$, orderings 0.580 + 0.227 and 0.387 + 0.420) | 0.0025 | $+0.0019$ |
| V3a reasoning text restates framing ($\kappa=-0.25$), reasoning stripped from splice | 0.0026 | $-0.250$ (flags the channel) |
| V3b same, reasoning carried into splice | IIE inflated by $+0.249$ (absorbs the reasoning channel) | $+0.0001$ (passes) |
| V4 hidden run state shared by path choice and report ($\varphi=1.5$, $\lambda=-0.5$) | 0.0055 | $-0.123$ (flags the violation) |

Reading. Under the assumptions the splice recovers every quantity to within Monte Carlo error. When the natural report also depends on something the splice does not carry (stripped reasoning, hidden state), the spliced contrasts still estimate the tool-path decomposition correctly, but they no longer add up to the natural total effect, and the self-splice placebo measures the gap ($-0.25$ is exactly the reasoning channel). When reasoning that restates the referral is carried, the placebo passes but the "indirect" effect silently includes anchoring through the reasoning text. The fix is a three-arm splice (tool calls only; tool calls plus redacted reasoning; tool calls plus full reasoning): differences between arms isolate the reasoning channel, and the self-splice placebo should be a pre-registered check. A blind-analysis harness that passes only structured tool outputs to the report step satisfies (S1) to (S3) by construction.

**Positivity.** Splicing a path that is rare under the other framing asks the report step to read an atypical context. The effect is still a defined intervention, but its relevance is clearest on paths with support under both framings; report $\mathrm{CDE}(z)$ by path type and flag spliced contexts outside common support.

**Related formalisms** for the write-up: the mediation formula and natural direct and indirect effects (Pearl, arXiv 1301.2300), interventional (randomized) analogues (VanderWeele, Vansteelandt and Robins 2014), identification under sequential ignorability (Imai, Keele and Yamamoto, arXiv 1011.1079), and the same intervention logic applied inside networks as causal mediation analysis of neurons (Vig et al., arXiv 2004.12265) and path patching (Goldowsky-Dill et al., arXiv 2304.05969). Path splicing is that idea at the level of an agent's transcript.

## C. Proposal 05 power calculations

Script `sim/c_power.py` (seed 505). All tests two-sided at 0.05 unless stated.

**C1. Single-edit success profile, unclustered.** Edits per arm for 80% (90%) power with the standard two-proportion formula:

| Contrast | 80% power | 90% power |
|---|---|---|
| 0.10 vs 0.12 | 3841 | 5142 |
| 0.10 vs 0.15 | 686 | 918 |
| 0.10 vs 0.20 | 199 | 266 |

**C2. Clustering by proposer seed.** If each seed (one proposer session on one base harness) yields $m$ edits whose success indicators share an intraclass correlation ICC, multiply by the design effect $1+(m-1)\,\mathrm{ICC}$. For 0.10 vs 0.15 at 80% power:

| ICC | $m=10$ | $m=25$ | $m=50$ |
|---|---|---|---|
| 0.01 | 748 | 851 | 1023 |
| 0.02 | 810 | 1016 | 1359 |
| 0.05 | 995 | 1510 | 2367 |
| 0.10 | 1304 | 2333 | 4048 |

Many short sessions beat a few long ones: at ICC 0.05, ten-edit sessions need 995 edits against 2367 for fifty-edit sessions.

**C3. Monte Carlo with the real design** (three base harnesses paired across arms; $\mathrm{logit}\,p=\mathrm{logit}\,p_{\text{arm}}+u_{\text{base}}+v_{\text{base}\times\text{arm}}+w_{\text{seed}}$, $u\sim N(0,0.5^2)$; 2000 replicates per cell). Two estimands need different analyses. (i) The effect in these three base harnesses: test on seed-level proportions, base as a fixed effect. (ii) The effect for new harnesses: test on the three base-level differences (2 degrees of freedom).

| Edits per arm ($m=10$) | seed sd $\sigma_w$ (latent ICC) | base-by-arm sd $\tau$ | power (i) | power (ii) |
|---|---|---|---|---|
| 690 | 0 | 0 | 0.81 | 0.28 |
| 690 | 0.3 (0.027) | 0 | 0.75 | 0.29 |
| 690 | 0.3 | 0.4 | 0.63 | 0.09 |
| 1200 | 0.3 | 0 | 0.95 | 0.38 |
| 1200 | 0.6 (0.099) | 0 | 0.87 | 0.32 |
| 2400 | 0.3 | 0.2 | 0.92 | 0.21 |
| 2400 | 0.3 | 0.4 | 0.82 | 0.10 |

With $m=50$ edits per seed the same budgets lose power (for example 0.61 instead of 0.75 at about 700 edits and $\sigma_w=0.3$). The arm effect on the logit scale is 0.46, so $\tau=0.4$ means the structural effect varies across base harnesses by almost its own size.

Number of base harnesses needed for estimand (ii) (100 edits per base and arm, $m=10$, $\sigma_w=0.3$):

| Base harnesses | $\tau=0$ | $\tau=0.2$ | $\tau=0.4$ |
|---|---|---|---|
| 3 | 0.15 | 0.13 | 0.07 |
| 6 | 0.49 | 0.35 | 0.22 |
| 10 | 0.82 | 0.66 | 0.41 |
| 20 | 0.99 | 0.95 | 0.72 |

Recommendation for the brief: about 1000 edits per arm in sessions of about ten edits gives at least 80% power for 0.10 vs 0.15 within the chosen base harnesses under realistic seed clustering. With three base harnesses, a claim about harnesses in general cannot be tested at any edit budget (power 0.07 to 0.38), so the paper should either state the estimand as conditional on its base harnesses or use ten or more base harnesses, which could be cheaper, smaller harnesses. In the $2^{4-1}$ factorial each main effect compares 12 against 12 base-by-cell combinations, so about 1000 edits per factor level means roughly 85 edits per (cell, base), a few hundred edits per structural variant in total, consistent with the brief.

**C4. Loop-level comparison of arms.** Final held-out improvement varies across optimizer seeds with sd $\sigma$. With loops paired by base harness (base effects cancel), the minimum detectable effect at 80% power is $2.80\sigma\sqrt{2/n}$: $1.02\sigma$ for 15 loops per arm (3 bases by 5 seeds), $0.72\sigma$ for 30, $0.51\sigma$ for 60. In the $2^{4-1}$ factorial with 3 bases and 5 seeds per cell (120 loops), each main effect compares 60 against 60 loops, again $0.51\sigma$. Loop-level tests detect only effects of about half the seed-to-seed spread or more; base-by-factor heterogeneity makes this worse in the same way as C3. This is why the single-edit profile should be the primary outcome.

**C5. Loop-level validation of the profile as a predictor.** Across $n$ configurations (structural variant by base harness), correlate the early profile with the mean loop outcome. Both are measured with error: reliability 0.83 for the outcome means 5 seeds when between-configuration and seed sds are equal; 0.75 for a profile from about 300 edits; 0.5/0.5 is a pessimistic case. Power (10,000 replicates, one-sided 0.05), first for detecting a positive correlation, then for showing the profile beats parent score (Williams' test for dependent correlations):

| $n$ configurations | true $r$ profile / parent score | reliabilities 0.83 / 0.75 | 0.5 / 0.5 |
|---|---|---|---|
| 24 | 0.5 / 0.0 | 0.63 ; 0.39 | 0.32 ; 0.20 |
| 24 | 0.7 / 0.3 | 0.89 ; 0.37 | 0.53 ; 0.18 |
| 48 | 0.7 / 0.3 | 0.995 ; 0.61 | 0.79 ; 0.28 |
| 96 | 0.7 / 0.3 | 1.00 ; 0.87 | 0.97 ; 0.45 |
| 96 | 0.6 / 0.4 | 1.00 ; 0.38 | 0.91 ; 0.19 |

The factorial's 24 configurations suffice to show that the profile predicts loop outcomes when the true correlation is 0.6 or more, but not that it predicts better than parent score or HGM's clade estimate. That comparison needs about 100 configurations (for example 32 random combinations of the five structural transformations on each of 3 bases) with 5 seeds each, or a pre-registered claim limited to detection. Report the attenuation-corrected correlation alongside the raw one.

## D. Proposal 07 information and perception decomposition

**Definitions.** Tool output $o$, target $y$ (a label or a statistic $s(o)$), loss $\ell$. An encoding $e$ maps $o$ to what the reader receives, $x=e(o)$: pixels or text, together with any fixed prompt. A reader $\pi$ maps $x$ to a prediction. Three risks:

- tool floor $R(o)=\inf_g\mathbb{E}\,\ell(g(o),y)$, the best any decoder can do from the raw tool output;
- encoding floor $R(e)=\inf_g\mathbb{E}\,\ell(g(e(o)),y)$, the best any decoder can do from what the reader sees;
- reader risk $R_\pi(e)=\mathbb{E}\,\ell(\pi(e(o)),y)$.

**Decomposition.**

$$R_\pi(e)=R(o)+\underbrace{[R(e)-R(o)]}_{\text{information term }I(e)}+\underbrace{[R_\pi(e)-R(e)]}_{\text{perceptual term }P_\pi(e)} .$$

The identity is a telescoping sum; its content lies in the signs. $I(e)\ge0$ because $e(o)$ is a function of $o$, so every decoder of $e(o)$ is also a decoder of $o$ (the data-processing inequality for Bayes risk; Blackwell's garbling order). $P_\pi(e)\ge0$ because the reader is one particular decoder of $x$, provided it sees nothing beyond $x$. Under log loss with a reader that outputs a predictive distribution $q(\cdot\mid x)$, the terms are exact information quantities: $I(e)=H(Y\mid e(o))-H(Y\mid o)$, the mutual information about $Y$ that the encoding discards, and $P_\pi(e)=\mathbb{E}_x\,\mathrm{KL}\big(p(\cdot\mid x)\,\Vert\,q(\cdot\mid x)\big)$. When the floor is estimated with a restricted decoder family $\mathcal V$ (a CNN of fixed size), $I$ becomes information usable by $\mathcal V$, in the sense of predictive $\mathcal V$-information (Xu et al., arXiv 2002.10689).

**Sub-decomposition of the perceptual term.** Let $h$ range over a fixed class of post-hoc maps (affine, low-order polynomial or monotone) fitted on a separate calibration set. Then $P_\pi(e)=[R_\pi(e)-R_{h\circ\pi}(e)]+[R_{h\circ\pi}(e)-R(e)]$, a calibration part (a systematic misreading such as compressed area judgments, removable by recalibration) plus a resolution part (failure to tell values apart). Perceptual profiles meant to predict transfer between readers should be stated in resolution terms, because calibration can be fixed cheaply for any one reader.

**Conditions for the decomposition to mean what it says.**

1. Same input. The oracle must read exactly what the reader reads, after the reader's own preprocessing. VLMs resize and patchify images; if the VLM downsamples a render to its input size, train the oracle on the downsampled image, or report the front-end resolution loss as its own term. Otherwise part of the "perceptual" gap is information the VLM never received.
2. No side information. The reader's prompt carries nothing about $y$ beyond $x$ (no referral text, no hints). A reader that beats the oracle by more than sampling error signals a breach of condition 1, 2 or 4.
3. Same loss and output space. Parse every reader output into the oracle's output space; give a parse failure a fixed fallback prediction (such as the training mean) and count it in $R_\pi$.
4. A near-Bayes oracle. A trained oracle's risk exceeds $R(e)$ by approximation and estimation error, so the measured gap $\hat P=R_\pi-\hat R(e)$ understates $P$, and the information term is overstated by the same amount. Checks: learning curves that flatten; agreement between two oracle architectures; closed-form floors where available (quantization variance $\Delta^2/12$ for a plot of pixel step $\Delta$; zero for a text encoding that an exact parser reads back).
5. Split hygiene. Train the oracle on renders of training people only and score oracle and reader on the same sealed test items. An oracle that has seen test people can memorize them, which understates $R(e)$ and overstates $P$.
6. Task relativity. $I(e)$ depends on the target: a plot can be lossless for amplitude and lossy for event timing. Index every profile by (encoding, task).
7. Information matching before attribution. Across encodings $R(o)$ cancels, so $R_\pi(e)-R_\pi(e')=\Delta I+\Delta P$. A difference counts as perceptual only when $R(e)\approx R(e')$ within confidence limits.
8. Where renderer computation shows up. Drawing a derived feature (a computed envelope, a fitted ellipse) cannot lower $I$ below that of a lossless encoding; it lowers $P$ by doing work the reader would otherwise have to do. An annotated arm that prints the statistic drives $R_\pi$ toward $R(o)$ through OCR, which is why it needs its own arm and a no-in-image-text control. For a gain $G_\pi=R_\pi(e_0)-R_\pi(e_1)=\Delta I+\Delta P_\pi$, the brief's three-way split is: $\Delta I$; a general perceptual part, the mean of $\Delta P$ over held-out readers; and a reader-specific part, $\Delta P_\pi$ minus that mean.

**Numerical illustration** (`sim/d_decomposition.py`, seed 707). Target: sway amplitude $A\sim U(1,5)$ cm, squared loss, tool floor 0. The plot has an autoscaled axis and pixel step $5/H$; the encoding floor is computed exactly. Readers: position on a common scale with 3% multiplicative noise; area with Stevens-type compression (exponent 0.7, 10% noise) read through a fixed linear map. The oracle is a $k$-nearest-neighbour decoder on (bar pixels, axis scale), standing in for a CNN.

| $H$ | $R(e)$ | position reader: $R$ = $I$ + $P$ (calibration + resolution) | area reader |
|---|---|---|---|
| 20 px | 0.0050 | 0.0137 = 0.0050 + 0.0087 (0.0001 + 0.0086) | 0.3505 = 0.0050 + 0.3455 (0.1924 + 0.1530) |
| 100 px | 0.0002 | 0.0096 = 0.0002 + 0.0093 (0.0002 + 0.0091) | 0.3421 = 0.0002 + 0.3418 (0.1838 + 0.1580) |

Oracle trained on 200 renders (at $H=20$): risk 0.063, about 12 times the true floor, so the position reader appears to beat the oracle ($\hat P=-0.049$) and the area reader's gap is understated by 17% (0.288 against 0.346). With 5000 renders the excess falls to 0.0008 and the measured gaps match the true ones to within 0.001. Two practical points follow. First, a negative perceptual gap is a diagnostic for an under-trained oracle (or for side information), not a finding. Second, more than half of the area reader's gap here is calibration, so a recalibrated reader closes much of it; profiles that mix the two parts will mispredict transfer.

## Corrections the briefs need

**Brief 06 (tails).**

1. The drift formula is correct (A1). The sentence "with $\mu_b\le0$ this happens whenever $\rho<-(1-w)\sigma_b/(w\sigma_a)$" should say the condition is sufficient, not necessary, and that the threshold does not depend on estimation noise. Add the per-proposal drift $\mu_b\Phi(\mu_S/\sigma_S)+\frac{\mathrm{Cov}(b,S)}{\sigma_S}\phi(\mu_S/\sigma_S)$, which is what a loop accumulates per generation. When random edits hurt the tail on average ($\mu_b<0$), harm begins above the threshold (at $w=0.875$, $\mu_b=-0.25$: $\rho_{\text{crit}}=+0.128$ against $\rho^*=-0.143$).
2. "Best-of-$K$ sharpens the effect" should become: best-of-$K$ multiplies the selection term by $m_K(c)/\lambda(\mu_S/\sigma_S)$ (exact expression in A2), which grows roughly like $\sqrt{2\ln K}$ under lenient thresholds. It worsens the tail only when $\mathrm{Cov}(b,S)<0$ and improves it when $\mathrm{Cov}(b,S)>0$.
3. Prediction 2 (inverted U) needs restating. A falling $\rho_t$ is not sufficient, because the threshold $\rho^*_t$ also falls as the majority's remaining gains shrink; in the geometric model $\rho$ fell from $+1$ to $-0.78$ in every regime, including the two with no tail harm. The testable statement: the tail trajectory turns down at the generation where the per-edit drift $\mathbb{E}[b\mathbf 1\{S>0\}]$ changes sign. In the geometric model this happens when the harness enters the ball whose diameter joins the tail optimum and the mean optimum (equivalently, when the tail gradient and the mean-objective gradient conflict in the metric of the proposal distribution). Three regimes follow: monotone gain, inverted U, and decline from generation 0. The early-loss regime is the Cooper and Lenski pattern, so their result fits the model and need not be treated as counter-evidence.
4. Edit-effect panels. (a) Naive panel correlations are attenuated by estimation noise (0.6 reads as 0.21 when $s_b=2\sigma_b$); subtract the known noise variances, or better, (b) estimate the drift directly: evaluate each panel edit on the loop's dev people to get the decision the loop would make, and on disjoint panel people to get its tail effect, then average $\hat b_{\text{panel}}\mathbf 1\{S_{\text{dev}}>0\}$. This is unbiased with no Gaussian assumption. (c) With 200 edits per generation the detectable per-edit drift is about 0.13 to 0.29 $\sigma_a$; plan more edits, or pool adjacent generations, near the sign change.
5. The guarantee holds as stated only under (G1) and (G2) of A4. Changes: say "no accepted parent, at any generation, is more than $M$ worse than the seed"; spend $\alpha$ per gate test, not per round; compare every candidate with $h_0$ (cite the bio-creep work); keep gate data sealed from the proposer. Reusing the same tail people every round breaks it (realized 0.11 to 0.29 at nominal 0.05). Cross-fitting does not repair this; fresh people, fold retirement, or checkpoint certification on sealed tail people by fixed-sequence testing do. The checkpoint route is the only practical one at StaBLE sizes. An e-process helps with optional stopping within a round, not with reuse. The one-sided $t$ test is anti-conservative under right-skewed per-person harm at $n_B\le20$ (lognormal: 0.17 to 0.23 at nominal 0.05, and 40 to 50 times nominal at 0.001), and a harm that hits 10% of tail people is missed with probability $0.9^{n_B}$ by any test. State these limits and report the guarantee as credible only from about 20 tail people.
6. Price of protection, for the frontier figure: in a tail-neutral regime the majority-only loop crosses a margin of 0.5 in 41% of runs even though the mean tail change is 0. Valid rules then keep 9% to 57% of the majority gain as $n_B$ goes from 5 to 20 (fresh people) or 15% to 42% (certification), against 97% for an oracle.

**Brief 08 (blind analysis).**

7. The proposition is true in the stated setting (B1), with 0 violations in 360 checks. Add the assumptions it uses: blind measurements are independent of the referral given the class; the decision maker already uses the referral as a prior and does not know $\gamma$; $0<q<1$. Strengthen the MSE half: for every $s>0$, every $\gamma\in(0,2\gamma^*)$ lowers MSE, with $\gamma^*=s^2/(s^2+\tau^2+q\Delta^2)$. Add the logit identity, which says in one line that the referral is counted twice. Add that the decision penalty falls on people whose referral is wrong (+0.35 nats against −0.06 nats for correct referrals in the worked example). Add the boundary of the claim: a decision maker who ignores the referral gains from context-aware measurement. Recalibrating the likelihood on pooled context-aware measurements does not remove the penalty; recalibrating within each referral value does, but only while $\gamma$ stays fixed, and a self-improvement loop does not hold it fixed.
8. Path splicing (B2) identifies the four cells of a two-by-two factorial (framing at the path stage by framing at the report stage), not a single direct and indirect pair. Report both orderings and the interaction (in V2 the indirect effect is 0.227 or 0.387 depending on ordering). With random paths, the estimands are the mediation-formula (interventional) effects averaged over the path distribution, not unit-level natural effects. Replace "identifies controlled direct and indirect effects" with that. State assumptions S1 to S4, pre-register the self-splice placebo, and use a three-arm splice (tool calls only, plus redacted reasoning, plus full reasoning), because reasoning text that restates the referral is a third channel: stripping it makes the placebo fail, and carrying it silently moves anchoring into the "indirect" effect. Cite Pearl, VanderWeele and colleagues, Imai and colleagues, and the neural-network analogues (causal mediation analysis of neurons; path patching).

**Brief 05 (evolvability).**

9. Power numbers to insert: 686 edits per arm detect 0.10 against 0.15 at 80% power without clustering, and about 1000 with realistic clustering in proposer sessions of about ten edits; avoid long sessions. With three base harnesses, a claim about harnesses in general cannot be tested at any edit budget (power 0.07 to 0.38), so either state the estimand as conditional on the base harnesses or use ten or more. Loop-level comparisons detect only about $1.0\sigma$ (15 loops per arm) or $0.51\sigma$ (factorial main effects) of seed-to-seed spread. The claim that the early profile predicts loop outcomes better than parent score or clade metaproductivity needs about 100 configurations; 24 suffice only to detect that the profile predicts at all.

**Brief 07 (observations).**

10. Write the decomposition with Bayes risks (D) and state its conditions: the oracle reads exactly what the VLM reads after the VLM's own resizing; no side information in the prompt; the same loss and output space with parse failures counted; a near-Bayes oracle checked by learning curves and closed-form floors; participant-level splits for the oracle; task-indexed profiles; information matching before any gain is called perceptual. Add the calibration and resolution split of the perceptual term, and say that a negative measured gap diagnoses an under-trained oracle (an oracle trained on 200 renders made a perfect-position reader look better than Bayes). Under log loss the two terms are a mutual-information loss and an expected KL divergence; with a restricted oracle family the information term is usable ($\mathcal V$-) information. Renderer computation appears as a drop in the perceptual term, which is why the annotated arm and the no-in-image-text control are needed.

## References verified for this report

Each fetched once on 2026-11-24 (arXiv abstract page or Crossref record).

- Feng, Emerson, Simon. Approval policies for modifications to machine learning-based software as a medical device: a study of bio-creep. arXiv 1912.12413.
- Waudby-Smith, Ramdas. Estimating means of bounded random variables by betting. arXiv 2010.09686.
- Dwork, Feldman, Hardt, Pitassi, Reingold, Roth. Generalization in adaptive data analysis and holdout reuse. arXiv 1506.02629.
- Blum, Hardt. The Ladder: a reliable leaderboard for machine learning competitions. arXiv 1502.04585.
- Pearl. Direct and indirect effects. UAI 2001; arXiv 1301.2300.
- VanderWeele, Vansteelandt, Robins. Effect decomposition in the presence of an exposure-induced mediator-outcome confounder. Epidemiology 25(2):300-306, 2014. DOI 10.1097/EDE.0000000000000034 (Crossref record; PubMed page blocked automated fetch).
- Imai, Keele, Yamamoto. Identification, inference and sensitivity analysis for causal mediation effects. Statistical Science 25(1):51-71, 2010; arXiv 1011.1079.
- Vig et al. Causal mediation analysis for interpreting neural NLP: the case of gender bias. arXiv 2004.12265.
- Goldowsky-Dill, MacLeod, Sato, Arora. Localizing model behavior with path patching. arXiv 2304.05969.
- Xu, Zhao, Song, Stewart, Ermon. A theory of usable information under computational constraints. ICLR 2020; arXiv 2002.10689.

Named standard methods used without a separate citation: inverse Mills ratio and truncated bivariate normal moments, Blom's approximation to normal order statistics, the Kish design effect, fixed-sequence testing, Williams' test for dependent correlations, Hoeffding's inequality, Blackwell's ordering of experiments.

## Scripts and outputs

| Check | Script | Output |
|---|---|---|
| A1 drift formula | `sim/a1_drift_formula.py` | `sim/a1_drift_formula_results.json` |
| A2 best-of-$K$ | `sim/a2_best_of_k.py` | `sim/a2_best_of_k_results.json` |
| A3 multi-generation loops, panels | `sim/a3_multigen.py` | `sim/a3_multigen_results.json` |
| A4 cumulative guarantee | `sim/a4_guarantee.py` | `sim/a4_guarantee_results.json` |
| B1 double counting | `sim/b1_double_counting.py` | `sim/b1_double_counting_results.json` |
| B2 path splicing | `sim/b2_path_splicing.py` | `sim/b2_path_splicing_results.json` |
| C power | `sim/c_power.py` | `sim/c_power_results.json` |
| D decomposition | `sim/d_decomposition.py` | `sim/d_decomposition_results.json` |
