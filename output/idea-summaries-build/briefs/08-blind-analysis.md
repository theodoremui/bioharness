# Brief for proposal 08: does telling an agent the diagnosis change what it measures?

Output file: `docs/idea-summaries/08-blind-analysis-for-agents.md`. Figures: `docs/idea-summaries/images/08/`. Figure code: `output/idea-summaries-build/figs_08.py`.

## Core question

When a tool-using analysis agent is told a hypothesis about the case it is measuring (a diagnosis, a referral reason, an expected result), does the hypothesis change which tools and parameters it selects and the value it reports? How much of that change passes through analysis choices rather than direct anchoring of the final number? Do self-improvement loops amplify it, even when rewarded only for accuracy, because context predicts the label? Does a blind-analysis harness (measurement path frozen before context is revealed, interpretation allowed to use context afterward) remove the bias while keeping the legitimate value of context?

One-line thesis: a measurement that has already looked at the diagnosis double-counts it when a clinician later combines the two, so an agent that is optimal for measurement error can be harmful for the decision it feeds, and physics' blind-analysis practice gives a harness-level remedy.

## Why it is open (to be confirmed by the literature report)

Agents now run end-to-end analyses (AI Scientist, Agent Laboratory, Biomni, data-science agents evaluated by BLADE and DiscoveryBench). Analyses have many defensible paths (the garden of forking paths, researcher degrees of freedom, multiverse analysis). Sycophancy and anchoring in LLMs are documented, and VLMs follow textual priors over visual evidence. What is missing is (1) a causal measurement, with physical ground truth, of how a stated hypothesis steers an agent's analysis path, separated from anchoring of the final answer; (2) evidence on whether self-improvement amplifies it; (3) a decision-theoretic account of why context-aware measurement harms downstream decisions; (4) a tested harness remedy adapted from blind analysis in particle physics (Klein and Roodman 2005; MacCoun and Perlmutter 2015).

## Running biomechanics example

The same single-leg-stance video is analyzed twice. Prompt A: "Referral: suspected Parkinson's disease, recent falls." Prompt B: "Referral: collegiate gymnast, routine screening." Under A the agent trims the trial at the first large excursion, uses a lower filter cutoff and reports a worse score; under B it treats the same excursion as a recoverable wobble. Each choice is defensible on its own. StaBLE supplies the setting (71 self-reported diagnoses, fall-risk groups, elite balancers) and labels; BioCV and OpenCap LabValidation supply independent marker and force-plate references for the measured quantity. Generalize: a data-analysis agent told "we expect the new onboarding flow raised retention" chooses covariates and outlier rules that produce a positive effect; a code-review agent told "this PR fixes the bug" runs fewer tests.

## Formal core

Decision-theoretic proposition (verify against `research/theory-checks.md`): a clinician holds prior $\pi=\Pr(C=1\mid H)$ from the referral $H$ and combines it with a measurement $M$ using a likelihood $f(M\mid C)$ calibrated on blind measurements. If the agent instead reports $M_\gamma=(1-\gamma)M_0+\gamma\,m_H$, shrinking the blind measurement $M_0$ toward the value $m_H$ the hypothesis suggests, then $M_\gamma$ can have lower mean squared error than $M_0$ for some $\gamma>0$, yet the clinician's posterior is misspecified and its expected log loss is strictly larger than with $M_0$ for every $\gamma\ne0$. The agent's training objective and the system's objective disagree.

Mediation through the analysis path: with framing $F$, path $P$ (tool choices, parameters, trims) and report $M$, the total framing effect splits into an effect through the path and a direct effect at reporting time. The harness can set the path directly: cache tool outputs for the path chosen under $F=a$ and replay them into the reporting step under $F=b$ ("path splicing"), which identifies controlled direct and indirect effects by intervention instead of by modeling assumptions.

Steering index: enumerate a multiverse of defensible paths (for example 200 combinations of pose model, filter, trim rule, event threshold); locate each chosen path's result as a quantile within the multiverse distribution for that video; the steering index is the framing-induced shift in that quantile. It needs no ground truth.

Evidence sensitivity: the slope of reported $M$ on the reference value within a framing group; context reliance lowers it below 1.

## Experiments

1. Framing audit: randomize framing independently of truth (neutral, consistent with the true group, inconsistent, and dose: "suspected" vs "confirmed"), many runs per video, several agents (Qwen3-VL-8B frozen and SFT, Qwen3-VL-32B, InternVL3.5, one API model). Outcomes: framing effect on $M$, error against reference, steering index, evidence sensitivity.
2. Path splicing mediation.
3. Which choices move: per-decision shifts (pose model, cutoff, trim, exclusion, threshold).
4. Self-improvement amplification: prompt or harness evolution (GEPA or ACE) and GRPO on the agent, under (a) accuracy reward with realistic informative referrals, (b) an approval reward from an LLM judge that sees the hypothesis, (c) accuracy reward with framing randomized. Track framing sensitivity and evidence sensitivity across generations.
5. Blind-analysis harness variants: full blinding of the measurement agent; blind then unblind with logged justification for any change; context visible but analysis path pre-registered before tool outputs are seen; data blinding for analysis agents (develop the analysis on data whose key variable is permuted or offset, then run frozen code once on the real data, as in MacCoun and Perlmutter). Outcomes: measurement accuracy, framing effect, downstream decision quality (posterior log loss and fall-risk AUC when a clinician model combines prior and measurement), cost.
6. Second domain: data-analysis agents on synthetic datasets with known null and non-null effects, told a hypothesis; outcomes are false-positive rate, effect-size inflation and the same blinding remedies. Also apply to a public benchmark such as BLADE or DiscoveryBench where alternative analyses are annotated.

## Figures (suggested)

1. One video, two referrals, two paths, two scores.
2. Path splicing diagram (direct vs indirect effect).
3. Multiverse and the steering index.
4. Double counting: prior plus context-aware measurement makes an overconfident posterior.
5. Amplification across generations under three rewards (illustrative).
6. Blind-analysis harness flow (measure blind, commit, unblind, interpret).
7. Data blinding for analysis agents.

## Falsifiers

Framing effects on $M$ are within run-to-run noise for all agents; the effect is entirely direct (paths do not move); self-improvement does not increase framing sensitivity under informative referrals; or blinding costs more decision quality than it removes.

## Reframing after the literature sweep, area-chair review and theory checks (overrides the design above where they conflict)

Read `research/08-blind-literature.md` and section B of `research/theory-checks.md` first. As first briefed, novelty was 3.0: 2026 work already shows that a stated belief steers analysis agents (Miao, Pritchard and Zou arXiv 2607.01507 with the m-value; Bertran et al. 2602.18710; Liu 2611.04070; Balani and Panda 2609.27756; Brown et al. 2611.05662; Xiao and Yu 2611.05720 with stage-resolved effects for search agents; Alexopoulos et al. 2603.18740 for code review; Restrepo et al. 2605.17436 and EchoBench 2509.20146 for clinical VLMs), Epistemic Blinding (Cuccarese 2604.06013) compares blinded and unblinded agentic analysis by masking entity identity, Asher et al. 2026 found directional hypotheses barely move frontier coding agents on well-specified tasks, and clinical epidemiology names the problem (review bias, incorporation bias, QUADAS-2; the JAMA 2004 systematic review of tests read with and without clinical information). Credit all of these plainly.

**New framing: calibration bug or information bug?** Context can enter an agent's measurement by two routes. Through the reported number (anchoring, shrinkage): if the transform of the blind measurement is invertible given the context, a combiner recalibrated within each context value recovers the full decision value. Through the analysis path (trimming, exclusions, filter or window choices conditional on the referral): the transform is generally not invertible and destroys information no combiner can recover. Contributions: (1) a proposition separating the two routes, with Gaussian and censored closed forms; (2) path splicing as the interventional way to measure the irrecoverable (path-mediated) part; (3) a pre-registered prediction of which self-improvement optimizer routes context where (prompt or playbook evolution such as GEPA or ACE tends to write path rules; scalar-reward GRPO tends to learn direct shrinkage), with the effective shrinkage moving toward $\gamma^*=s^2/(s^2+\tau^2+q\Delta^2)$ under accuracy reward and informative referrals, and a predicted "better measurer, worse decision" crossover; (4) a blind-measure-then-interpret harness scored on downstream decision log loss, which should beat every baseline except within-context recalibration when the route is direct, and beat that too when the route is the path.

Must-fix items:
- Double-counting proposition (proved in theory-checks): state assumptions ($M_0$ independent of $H$ given $C$; the decision maker uses the referral as its prior and does not know $\gamma$; $0<q<1$); the excess log loss is $\mathbb{E}[\mathrm{KL}(p_0\,\|\,p_\gamma)]$; the logit identity shows the referral counted twice; MSE falls for every $\gamma\in(0,2\gamma^*)$; the harm falls on people whose referral is wrong; a decision maker who ignores the referral can benefit; recalibration within each referral value repairs the direct route. Quote the worked example only as a computed illustration.
- Path splicing identifies the four cells of a 2 x 2 factorial (framing at the path stage by framing at the report stage) under four stated conditions (stateless report step, splice format consistency, no framing leakage in the spliced transcript, cached or deterministic tools). Report both decomposition orderings and the interaction; the estimands are interventional (mediation-formula) effects, not unit-level natural effects. Pre-register a self-splice placebo and use a three-arm splice (tool calls only; plus redacted reasoning; plus full reasoning), because reasoning text that restates the framing moves anchoring into the indirect effect. Cite Pearl, VanderWeele et al. 2014 and Imai et al.
- Steering index: define it as the framing-induced shift in Miao et al.'s m-value and validate it against reference error on the labeled subset.
- Ground truth: StaBLE's reference is three-camera OpenCap (video-derived, HRNet keypoints), not a physical reference; BioCV and OpenCap LabValidation are healthy adults without single-leg stance. Use sit-to-stand or squat as the bridge task for physical-reference claims. StaBLE videos are lab-internal.
- True groups: the 71 diagnoses are self-reported; use age band, fall-risk group and elite status as the "true group" for consistent versus inconsistent framing.
- Appearance-blind arm: the video reveals age, build and walking aids, so text blinding does not blind a VLM. Add skeleton-only or appearance-masked inputs, or tool outputs only, to separate stated from inferred context (the analog of a hidden signal region).
- Confront Asher et al.: pre-register that effects concentrate in weakly specified steps and ambiguous evidence.
- Evidence sensitivity: compare slopes across framings with an errors-in-variables correction, not against 1. Gate on measurement: the frozen VLM barely measures (lab pilot, unpublished), so run the audit on agents and tool pipelines that pass an evidence-sensitivity check first.
- Post-unblinding changes: allow only pre-declared changes; logged justifications are unreliable (Turpin et al. 2023 on unfaithful explanations).
- The approval-reward arm is a positive control for sycophancy (Sharma et al.), not a finding.
- Stronger baselines: a combiner recalibrated on context-aware outputs; Epistemic Blinding-style referral masking; Gunsilius et al. 2611.23174 reset-and-replay correction; Liu's neutral brief with a decision rule fixed outside the agent; prompt-level "ignore the referral" and counterexample prompting; data blinding (MacCoun and Perlmutter 2015; Dutilh et al. 2021).
- Second domain: EchoNet-Dynamic (Ouyang et al., Nature 2020; 10,030 echocardiography videos with ejection fraction and expert tracings; Stanford AIMI research use agreement), a video measurement with classic forking paths (segmentation, end-diastole and end-systole frame choice, beat averaging, exclusion of foreshortened views) and standard decision thresholds on ejection fraction. Keep a data-analysis-agent domain with synthetic known-null effects as a third, cheap check.
- Recompute StaBLE normalization on development people; label lab-pilot numbers as unpublished.
