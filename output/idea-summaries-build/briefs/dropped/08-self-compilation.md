# Brief for proposal 08: when can an agent replace its own deliberation with code it wrote?

Output file: `docs/idea-summaries/08-certified-self-compilation.md`. Figures: `docs/idea-summaries/images/08/`. Figure code: `output/idea-summaries-build/figs_08.py`.

## Core question

Can a tool-using agent turn its recurring tool-call trajectories into programs, each with a learned condition for when it applies, so that on new people the compiled agent is cheaper, more repeatable and, with a finite-sample guarantee, no less accurate than deliberation on the inputs it chooses to compile? How does that guarantee degrade when tasks or cameras shift?

One-line thesis: a self-improving agent can safely replace parts of itself only where it can certify the replacement, and replacing a sampled deliberation by its compiled form can lower error by removing run-to-run variance.

## Why it is open

Agents as measurement instruments need test-retest reliability, yet a sampled agent can return different tool paths and different numbers on the same video. Skill and workflow induction (Voyager, Agent Workflow Memory, Agent Skill Induction, SkillWeaver, agentic plan caching, record-and-replay agents) reuse past trajectories to cut cost, but either reuse without a statistical certificate of where reuse is safe or check only that execution succeeds. Conformal and risk-control methods (conformal risk control, Learn-then-Test, KnowNo for robot planners) give finite-sample guarantees for predictions and for asking for help, but they have not been used to certify self-replacement of agent components. The Goedel machine rewrites itself only with a proof; the Darwin Goedel Machine replaces proof with benchmark evidence. A statistical certificate per replacement sits between them. Check the literature report and state the residual gap precisely.

## Running biomechanics example

Run the same StaBLE single-leg-stance video through a Qwen3-VL-8B agent eight times at its deployed temperature. Some runs call RTMPose then a Butterworth filter; others call OpenCap Monocular; filter cutoffs and window choices vary; scores spread. Clinicians judge a measurement by its intraclass correlation (ICC) and minimal detectable change (MDC95 = 1.96 x sqrt(2) x SEM). Run-to-run agent variance inflates SEM and hence MDC, so a real change in a patient's balance can hide inside the agent's own noise. Meanwhile most quiet-standing videos follow the same five tool calls. Generalize: a data-analysis agent that rewrites the same groupby-and-plot code for every weekly report; a web agent repeating the same checkout flow.

## Definitions to include

Deliberation; trajectory and tool-call skeleton; compilation; validity gate; exchangeability; conformal risk control; Learn-then-Test; ICC, SEM, MDC; covariate shift and weighted conformal prediction.

Formal core. Let $Y_\pi(x)$ be the random output of deliberation on input $x$ with label $y$. For squared loss, $\mathbb{E}[(Y_\pi(x)-y)^2]=(\mathbb{E}[Y_\pi(x)]-y)^2+\text{Var}(Y_\pi(x))$. A deterministic program $c(x)\approx\mathbb{E}[Y_\pi(x)]$ removes the variance term, so compilation can be amortized self-consistency. A gate $g(x)\in[0,1]$ routes inputs with $g(x)\ge\lambda$ to $c$. Define excess loss $\Delta(x)=\ell(c(x),y)-\mathbb{E}\,\ell(Y_\pi(x),y)$ and risk $R(\lambda)=\Pr(\Delta>\delta\mid g\ge\lambda)$ or an expected-excess version. Learn-then-Test tests $H_\lambda:R(\lambda)>\epsilon$ over a grid with fixed-sequence testing and Hoeffding-Bentkus p-values, giving $\Pr(R(\hat\lambda)\le\epsilon)\ge1-\alpha$ when calibration and deployment people are exchangeable. A label-free variant certifies fidelity to deliberation, $|c(x)-\text{median}\,Y_\pi(x)|\le\delta$, and needs no labels.

## Method

1. Reliability audit: $k=8$ runs per video for several agents; random-effects decomposition into person, task, run (agent) and residual variance; ICC(2,1), SEM, MDC95; compare with deterministic pipelines (RTMPose plus a temporal model).
2. Compilation: canonicalize trajectories into skeletons (tool names and argument slots), cluster by edit distance, and for each frequent cluster have the agent write a program that reproduces it, with explicit argument-setting rules inferred from the trajectories. Accept a program after differential testing against deliberation medians on the cluster's dev inputs.
3. Gates: predict $\Delta\le\delta$ from features available before running the program (video metadata, a cheap pose pass's confidence, motion energy, task identity, VLM embedding of preview frames).
4. Certification: Learn-then-Test on calibration people, also per task (Mondrian) for group-conditional control; weighted conformal under estimated covariate shift for new camera angles.
5. Self-improvement loop: new data, new clusters, programs revised when their gate rejects often; track coverage, cost, error and ICC across rounds; rollback when certification fails.

## Experiments to specify

Data: StaBLE split by participant into compile-dev, calibration and test; the three phones give a camera-shift test; held-out tasks give a task-shift test; BioCV for event timing against force plates. Baselines: always deliberate; self-consistency with $k$ samples (median); agentic plan caching; AWM or ASI style skills used whenever matched (no certificate); distillation into weights by SFT on the agent's own trajectories or direct prediction (the lab pilot found SFT lowered average error but hurt clinical extremes); a fixed hand-built pipeline. Metrics: MAE and error at clinical extremes, ICC and MDC95, tool calls and GPU-seconds per video, coverage, and the empirical violation rate of the certificate over 100 random calibration-test splits. Second domain: a data-analysis agent with recurring analyses (for example DABStep) or a web-agent benchmark used by AWM or ASI.

## Figures (suggested)

1. Eight runs on one video: different tool paths, spread of scores (illustrative).
2. Variance decomposition bar and the bias-variance identity.
3. Compilation pipeline: trajectories -> skeletons -> program -> differential test -> gate.
4. Learn-then-Test threshold selection along a coverage-risk curve.
5. Deployment router: gate -> program or deliberation.
6. Self-improvement rounds: coverage grows, certificate checked each round.
7. Shift map: where the guarantee holds and where it does not.

## Falsifiers

Run-to-run variance is a negligible share of error; compiled coverage stays tiny at useful $\epsilon$; empirical violation exceeds $\alpha$ even without shift; or uncertified skill reuse matches certified reuse in accuracy at clinical extremes.
