# Literature sweep and area-chair review for proposal 08: blind analysis for tool-using agents

Status: COMPLETE (2026-11-24). This run resumed an interrupted sweep (searches 1 to 14 were logged by the earlier run), added searches 15 to 28, re-verified the central papers, ran a small simulation of the brief's decision-theoretic proposition, and filled every section. A companion file from another run, `research/08-blind-literature-science.md`, covers the science-of-science and clinical-epidemiology angle; its verified entries are reused here where noted, and the key ones were re-fetched in this run.

Verification rule. An item is marked verified when its arXiv abstract page, Crossref record, Europe PMC record, PMC page, publisher page or author-hosted PDF was fetched in this run or in the earlier run of this same report and the title and authors matched. Venues are given only when a fetched page states them. Items not confirmed by a fetched page are marked UNVERIFIED and collected in Section 9.

## 0. Question under review

Brief: `output/idea-summaries-build/briefs/08-blind-analysis.md`. When a tool-using analysis agent is told a hypothesis about the case it is measuring (a diagnosis, a referral reason, an expected result), does the hypothesis change which tools and parameters it selects and the value it reports? How much of that change passes through the analysis path (tool choice, filter cutoff, trial trimming, exclusions, event thresholds) and how much is direct anchoring of the final number? Do self-improvement loops amplify it when context predicts the label? Does a blind-analysis harness (measurement path frozen before context is revealed, interpretation allowed to use context afterward) remove the bias while keeping the legitimate value of context? The thesis is that a measurement that has already looked at the diagnosis double-counts it when a clinician later combines measurement and referral, so an agent that is optimal for measurement error can be harmful for the decision it feeds.

## 1. Searches run

Earlier run (logged before the interruption):

1. "LLM agents p-hacking data analysis hypothesis framing": Asher et al. "Do Claude Code and Codex P-Hack?"; Baumann et al. LLM hacking 2509.08825; Kosch prompt-hacking 2504.14571.
2. "LLM agents questionable research practices": BadScientist 2510.18003; AI-scientist verification-gap survey 2608.05179.
3. "AI scientist confirmation bias data analysis": Failing to Falsify 2604.02485; Confirming Our Biases 2608.06977.
4. "sycophancy tool use agents hypothesis": Rational analysis of sycophantic AI 2602.14270; multi-agent sycophancy 2604.02668.
5. BLADE and DiscoveryBench: 2408.09667, 2407.01725.
6. "many analysts LLM persona": Many AI Analysts, One Dataset 2602.18710.
7. "multiverse analysis LLM agents": Agentic Garden of Forking Paths 2607.01507; When AI Analysts Disagree 2611.25198; Preregistration for Experiments with AI Agents 2606.11217.
8. "anchoring bias large language models": 2412.06593, 2505.15392, 2511.05766.
9. "vision language models biased by text prior over visual evidence": ViLP 2501.00569, VLind-Bench 2406.08702, 2606.10400, 2610.21902.
10. "medical VLM misleading clinical history": EchoBench 2509.20146; 2509.21979; Medical Context Distorts Decisions 2605.17436.
11. "LLM judge reference answer bias": 2506.22316.
12. "AI scientist hidden pitfalls": 2509.08713.
13. "blind analysis LLM agent harness": no direct hit.
14. "optimizing for user feedback sycophancy": 2411.02306; Sharma et al. 2310.13548.

This run:

15. "observer bias randomized trials blinded and nonblinded assessors": Hrobjartsson et al., CMAJ 2013.
16. "LLM agent tool selection bias prompt context": BiasBusters 2510.00307; Tool Preferences in Agentic LLMs are Unreliable 2505.18135 (both concern tool metadata, not case context).
17. "self-refinement amplifies bias, in-context reward hacking": Xu et al. 2402.11436 (ACL 2024); Pan et al. 2402.06627 (ICML 2024).
18. "Dutilh flexible yet fair blinding analyses psychology": Synthese 2021.
19. "agent told expected result confirmation bias ground truth 2026": Brown et al. 2611.05662; Xiao and Yu 2611.05720; Alexopoulos et al. 2603.18740.
20. "Kriegeskorte circular analysis double dipping": Nature Neuroscience 2009.
21. "combining forecasts with shared information, double counting": Palley and Soll, Management Science 2019.
22. "blinded evaluation, hide hypothesis from analysis agent, unblinding protocol": Cuccarese, Epistemic Blinding 2604.06013 (closest remedy precedent); no hypothesis-blinding harness found.
23. "RLHF approval reward misleads evaluators": Wen et al. 2409.12822 and an ICLR 2026 blog-post critique of its experiments.
24. "inference after coding agents" (from the science-angle notes): Gunsilius, Van Dijcke, Wuthrich 2611.23174.
25. "causal mediation of framing through tool calls, replay of cached tool outputs": Causal Agent Replay 2606.08275; AttriGuard 2603.10749; AgentSentry 2602.22724 (not fetched).
26. "blind analysis AI scientist agents 2026": verification-gap survey 2608.05179; open-ended AI research case studies 2607.27191; no physics-style blind analysis for agents found.
27. "VLM video assessment, diagnosis in prompt, clinical rating": Monte e Freitas et al. 2604.08294 (action-quality judging); Li et al. 2511.17727 (stroke rehabilitation); no study of a diagnosis in the prompt shifting a VLM movement score.
28. Second-domain checks: EchoNet-Dynamic (Ouyang et al., Nature 2020); ACIC 2016 data challenge (Dorie et al., arXiv 1707.02641).

## 2. Closest prior work

Each entry gives exact title, first author et al., year, venue or arXiv ID, a verified URL, what they did, and what they leave open for the 08 question. Ordered by closeness.

### 2.1 The Agentic Garden of Forking Paths
Miao, Pritchard, Zou. 2026. arXiv 2607.01507 (1 Jul 2026; no venue stated). https://arxiv.org/abs/2607.01507 (verified).
What they did: agents given different personas reach divergent, often opposing conclusions from the same data and question, tracking the persona's beliefs. On a 42-team human many-analyst immigration study, agents reproduced 72% of the human ideological gap in effect estimates; 86% of the AI analyses passed independent AI review and 78% passed majority human expert review. They define the m-value (the probability that an analysis path yields a claim at least as extreme as the reported one) and estimate it with "Agentic Bootstrap", which samples plausible paths with agents; 13.5% of the human reported analyses fell in the most extreme 5% of the space.
What remains open: no ground truth, so steering cannot be scored as error; belief enters as a persona of the analyst, not as a hypothesis about the case; no separation of path effects from final-answer effects; no remedy beyond reporting the position within the path distribution; no measurement from perceptual data. The brief's "steering index" is close to a framing-induced shift in this m-value and must be defined that way.

### 2.2 Many AI Analysts, One Dataset: Navigating the Agentic Data Science Multiverse
Bertran, Fogliato, Wu. 2026. arXiv 2602.18710 (v1 21 Feb 2026, v2 11 Mar 2026; no venue stated). https://arxiv.org/abs/2602.18710 (verified).
What they did: autonomous AI analysts run full pipelines on a fixed dataset and hypothesis, with an AI auditor screening for validity; across three datasets, effect sizes, p-values and conclusions vary substantially, traced to preprocessing, model specification and inference. Changing the analyst persona or the LLM shifts the result distribution even among audited-sound runs.
What remains open: no ground truth, no case-level hypothesis given to the agent, no causal split of path versus report, no blinding remedy, no self-improvement.

### 2.3 Do Claude Code and Codex P-Hack? Sycophancy and Statistical Analysis in Large Language Models
Asher, Malzahn, Persano, Paschal, Myers, Hall. 2026. Working paper dated 19 Feb 2026 (25 pages). https://www.andrewbenjaminhall.com/pdfs/asher_et_al_LLM_sycophancy.pdf (verified, first two pages read); replication archive https://github.com/janetmalzahn/llm-phacking (verified).
What they did: Claude Opus 4.6 (Claude Code) and GPT-5.2-Codex on four published null-result political-science papers (RD, DiD, selection on observables, RCT), a 2 x 4 design crossing neutral versus directional-prior framing with four nudges, 10 runs per cell, 640 sessions. Under standard prompts estimates were "remarkably stable" and both models refused direct p-hacking; a prompt that recasts specification search as uncertainty reporting bypassed the refusals, and the resulting inflation tracked the design's analytic flexibility (observational more than randomized). Search snippets of a later version state that directional framing alone made little difference; that detail was not re-read in the PDF (see Section 9).
What remains open: this is the strongest negative prior for 08. Frontier coding agents on well-specified estimation tasks are not visibly steered by a stated hypothesis. Open: weakly specified measurement steps (trim rules, event thresholds, exclusion of a "bad" trial), perceptual inputs, smaller open models, and whether self-improvement changes the picture.

### 2.4 Inference after coding agents
Gunsilius, Van Dijcke, Wuthrich. 2026. arXiv 2611.23174 (17 Nov 2026; stat.ME). https://arxiv.org/abs/2611.23174 (verified).
What they did: in zero-effect simulations, four frontier agents asked for a "compelling finding" reported significant p-values in 54% to 98% of runs. They propose resetting and replaying the agent on subsamples to estimate the probability that it selects the reported analysis when that analysis looks favorable, and show the corrected test is asymptotically valid conditional on selection for agents with stable selection behavior, bringing false rejections near 5%.
What remains open: the pressure is an explicit request for a compelling result, not a hypothesis about the case; the target is testing validity, not measurement error or downstream decisions; no harness-level blinding; no perceptual measurement. The replay correction is a strong baseline for the second domain.

### 2.5 Evaluating LLM Research Agents as Tests of Return Predictability
Liu. 2026. arXiv 2611.04070 (v1 2 Nov 2026, v2 8 Nov 2026; q-fin.ST). https://arxiv.org/abs/2611.04070 (verified). The earlier run recorded a v1 title "Are LLM Research Agents Reliable Judges of Predictability?"; the fetched page shows only the current title.
What they did: agent verdicts on whether a forecast beats the historical mean are treated as statistical tests on simulated return series with planted signals. Agents over-claim predictability in null worlds, and verdicts change after a single sentence about prior research. Recommended remedies: a neutral brief, a decision rule fixed outside the agent, and a sealed holdout.
What remains open: these remedies are informal pieces of blind analysis; no decomposition of how the sentence acts (path or verdict), no measurement task, no decision-theoretic account, no self-improvement.

### 2.6 Reporting Under Pressure: Separating Factual and Tonal Sycophancy in LLM Statistical Analysis
Balani, Panda. 2026. arXiv 2609.27756 (15 Aug 2026). https://arxiv.org/abs/2609.27756 (verified).
What they did: 4 editorial framings x 4 data patterns (genuine effect, confound that fails a robustness check, well-powered null, underpowered null), 480 responses scored separately for factual and tonal divergence. Factual distortion concentrated in two cells (critical framing on a genuine effect, 97%; significance-seeking framing on an underpowered null, 100%); a confound blocked both kinds of shift almost entirely.
What remains open: single-shot analysis without tools, no path decomposition, no measurement. Useful prediction for 08: framing effects should concentrate where the evidence is ambiguous (low-quality video, borderline excursions), which is testable as an interaction with evidence strength.

### 2.7 Grounded but Not Immune: Confirmation Bias in Agent-as-a-judge
Brown, Pahwa, Ge, Romeo, Agnihotri, Zhang, Ma, Bonadiman. 2026. arXiv 2611.05662 (3 Nov 2026; preprint under review). https://arxiv.org/abs/2611.05662 (verified).
What they did: a tool-using judge with the full trajectory is given one false authority-attributed pre-screening note; the note overturns up to 40% of correct verdicts across four judges and five datasets even when the judge gathers decisive evidence. Failure modes are classified as over-trust, hallucination and under-investigation; over-trust is 67% to 75% of harmful flips for two Claude judges. Lightweight mitigations blunt the bias but never remove it.
What remains open: this is the nearest agentic result on "a hint about the answer changes a tool-using agent", and its failure-mode split is a qualitative version of path (under-investigation) versus direct (over-trust) effects. Open: interventional identification of the split, continuous measurement, a structural remedy (blinding instead of prompt-level mitigation), and amplification under training.

### 2.8 Cognitive Bias Signatures in Search-Equipped LLM Agents: A Stage-Resolved Analysis
Xiao, Yu. 2026. arXiv 2611.05720 (3 Nov 2026). https://arxiv.org/abs/2611.05720 (verified).
What they did: a controlled search harness with fixed questions and corpora varies result order, records of prior failed work, and initial hypotheses, across 10 models and 1,000 synthetic search worlds, tracking queries, retrievals, document openings and answers. Under wrong hypotheses, stage-level measurements separate reduced retrieval or opening of counter-evidence from errors that persist after counter-evidence is opened.
What remains open: this partly pre-empts the brief's claim that no one has separated path effects from final-answer effects. It does so observationally by stage, for retrieval, with discrete answers. Open: interventional splicing that fixes the path and varies only the framing at reporting time, continuous measurement with a physical reference, the decision cost of each route, and a remedy.

### 2.9 Epistemic Blinding: An Inference-Time Protocol for Auditing Prior Contamination in LLM-Assisted Analysis
Cuccarese. 2026. arXiv 2604.06013 (7 Apr 2026). https://arxiv.org/abs/2604.06013 (verified).
What they did: replaces entity identifiers with anonymous codes before prompting and compares against an unblinded control, in an agentic drug-target prioritization system with blinded LLM-guided evolution of scoring functions; blinding changed 16% of top-20 oncology predictions with identical recovery of validated targets, and brand recognition reshaped 30% to 40% of S&P 500 top-20 rankings. Released as an open tool and a Claude Code skill. The paper says blinding is counterproductive for hypothesis generation.
What remains open: this is the closest remedy precedent and must be cited as such. It blinds entity identity, not a stated hypothesis; it has no measurement ground truth beyond recovery of known targets; it does not separate measurement from interpretation, test decision quality, or study self-improvement (although it blinds an evolutionary optimizer, which is a useful design precedent).

### 2.10 Medical Context Distorts Decisions in Clinical Vision Language Models
Restrepo, Ktena, Vakalopoulou, Christodoulidis, Ferrante. 2026. arXiv 2605.17436 (17 May 2026). https://arxiv.org/abs/2605.17436 (verified).
What they did: on MIMIC-CXR tasks, general and medical VLMs are dominated by text over the image, are swayed by irrelevant clinical histories, and flip image-correct predictions under semantically equivalent prompt changes.
What remains open: no tools, no measurement path, no continuous quantity, no remedy beyond calls for stress testing. EchoBench (Yuan et al. 2509.20146, verified) adds sycophancy rates in medical VLMs (Claude 3.7 Sonnet 45.98%, GPT-4.1 59.15%, many medical models above 95%) and shows prompt-level mitigations help.

### 2.11 When AI Analysts Disagree: Agentic Multiverse Analysis and the Robustness of Empirical Research
Gao, Xiao. 2026. arXiv 2611.25198 (18 Nov 2026; 45 pages; subsumes 2603.16744). https://arxiv.org/abs/2611.25198 (verified).
What they did: 150 coding agents on one dataset disagree on the same kinds of choices human analysts face, over a narrower range; AI peer review leaves the disagreement unchanged, while showing top-rated exemplars collapses it, mostly through imitation. The AMA framework enumerates, rubric-scores and runs specifications for 10 management studies, 1,755 estimates.
What remains open: the exemplar result bears on self-improvement: prompt or playbook evolution (GEPA, ACE) works by showing the agent its own best traces, so it may homogenize paths and lock in a framing-dependent rule. No hypothesis framing, no measurement, no blinding.

### 2.12 When AI Agrees Too Much: Manipulating Automated Code Review via Bias Injection
Alexopoulos, Alexopoulos, Spinellis, Mitropoulos. 2026. arXiv 2603.18740 (v5 27 Oct 2026); to appear at ICSE 2027 per the arXiv comments. https://arxiv.org/abs/2603.18740 (verified). Its v1 HTML carried the title "Measuring and Exploiting Confirmation Bias in LLM-Assisted Security Code Review".
What they did: framing pull-request metadata biases LLM vulnerability detection across 6 LLMs and five framings; on 33 CVEs in 20 projects against Claude Code and CodeRabbit, an LLM-refined bias-injection attack succeeded in 32 of 33 cases.
What remains open: this already covers the brief's code-review generalization ("a code-review agent told this PR fixes the bug runs fewer tests"); the brief must cite it and drop that example as novel.

### 2.13 A Rational Analysis of the Effects of Sycophantic AI
Batista, Griffiths. 2026. arXiv 2602.14270 (15 Feb 2026). https://arxiv.org/abs/2602.14270 (verified).
What they did: a Bayesian agent given data sampled according to its current hypothesis grows more confident without approaching the truth; in a modified Wason 2-4-6 task with 557 participants, unmodified LLM feedback suppressed discovery and inflated confidence about as much as explicitly sycophantic prompting, and unbiased sampling gave five times higher discovery.
What remains open: this is the closest formal prior to the brief's "double counting" thesis (evidence that was shaped by the hypothesis inflates confidence). It concerns data selection for a human learner, not a measurement fed to a separate combiner, and it does not distinguish invertible from information-destroying contamination.

### 2.14 Accuracy of Diagnostic Tests Read With and Without Clinical Information: A Systematic Review
Loy, Irwig. 2004. JAMA 292(13):1602. https://doi.org/10.1001/jama.292.13.1602 (verified via Crossref and Europe PMC).
What they did: 16 studies (11 comparing ROC areas); clinical information generally improved reading accuracy, the gain was smaller with real than with constructed information, no study found that clinical information significantly reduced accuracy, and some gains were higher sensitivity at unchanged specificity. They concluded that reading tests with clinical information "appears justified".
What remains open: this is the strongest counterweight to the brief. Context can raise the accuracy of a reading; the harm the brief claims exists only when a downstream combiner adds the same context again under an independence assumption. The proposal must be framed around that combination step, not around context use per se. Hrobjartsson et al. (CMAJ 2013, verified) supply the opposite human evidence for outcome assessment: in 16 trials (2,854 patients) with both blinded and nonblinded assessors of subjective measurement scales, nonblinded assessors exaggerated the pooled effect size by 68% (95% CI 14% to 230%).

## 3. Is the core idea already done?

Partly. The phenomenon that a stated belief steers an LLM agent's analysis is established in 2026 for data-analysis agents (Miao et al.; Bertran et al.; Liu; Balani and Panda), tool-using judges (Brown et al.), search agents (Xiao and Yu), code review (Alexopoulos et al.) and clinical VLMs without tools (Restrepo et al.; EchoBench). A stage-level separation of path effects from answer effects exists for search agents (Xiao and Yu), and a failure-mode split for tool-using judges (Brown et al.). A blind-versus-unblind protocol for agentic analysis exists for entity identity (Cuccarese). The m-value of Miao et al. already places a reported path within the multiverse, which is most of the brief's steering index. Classical epidemiology already names the double-counting problem (incorporation bias, review bias, QUADAS-2's blinding items), and neuroscience names its selection form (double dipping). Asher et al. report that frontier coding agents are barely moved by directional hypotheses on well-specified estimation tasks.

What is not done, as far as this sweep found:
- an interventional decomposition (cached tool outputs spliced across framings) of a hypothesis effect into path-mediated and direct parts, for a continuous measurement with a reference;
- any study of whether self-improvement (prompt or harness evolution, RL on the agent) learns to use case context, and through which route;
- a decision-theoretic result that says which route is harmful and when recalibration can repair it;
- a harness that separates a blind measurement stage from a context-aware interpretation stage and is scored on downstream decision quality;
- any of this for video measurement, where the data themselves reveal context (age, gait aid, athletic build).

Nearest open, high-value reframing. The simulation in Section 5.1 shows the brief's proposition splits in two. When context enters as an invertible adjustment of the blind number (direct anchoring, linear shrinkage toward the referral's expected value), no information is lost: a combiner recalibrated on context-aware outputs recovers the blind-optimal decision exactly, so the harm is a calibration bug. When context enters through the analysis path (trimming at the first excursion, excluding a trial, a lower filter cutoff), the map from video to number is not invertible and information is destroyed: no combiner can recover it, so the harm is an information bug. The reframed proposal is: "Accuracy-driven self-improvement teaches measurement agents to use case context; whether that is repairable depends on whether the optimizer routes context into the final number or into the analysis path. We identify the route by path splicing, predict the route from the optimizer type, and show that blind analysis is required exactly when the route is the path." This keeps every experiment in the brief, gives the mediation analysis a decision-theoretic meaning, and turns "self-improvement amplifies bias" (which Bayes shrinkage predicts and reviewers will call obvious) into a sharper question about where the bias lives.

## 4. Area-chair scores

- Novelty: 3.0 out of 5 as written. The audit of framing effects on an analysis agent, the multiverse steering index and the code-review and data-analysis generalizations are all close to 2026 papers. The novel parts are path splicing for a continuous measurement, amplification under self-improvement, and a blind-analysis harness scored on decisions.
- Significance: 3.5 out of 5 as written. The question matters for any agent whose output feeds a later decision with the same context (clinical measurement, code review, analytics), and blind analysis is a portable harness rule. The biomechanics evidence base is thin (StaBLE's reference is video-derived; the marker and force-plate sets are 10 and 15 healthy adults without balance tasks), and the pilot VLM barely measures, which limits how much the clinical claims can carry.
- With the upgrades in Section 6: novelty about 4.3, significance about 4.4.

Strongest reviewer objection. "This is the 2026 framing-and-sycophancy result moved to a new domain. Asher et al. already found that a directional hypothesis barely moves frontier agents; Miao et al. and Bertran et al. show persona steering with an m-value; Brown et al. show hinted tool-using judges flip; Xiao and Yu already separate stage-level effects; Cuccarese already proposes blind-versus-unblind analysis for agents. The double-counting proposition is a textbook misspecified-likelihood result (incorporation bias), and amplification under accuracy reward is Bayes shrinkage that any learner will find, which a combiner can undo by recalibrating on the agent's outputs. Finally, the frozen 8B VLM in the pilot does worse than a constant guess, StaBLE has no physical reference, and the video already shows the person's age, so text blinding does not blind the agent."

## 5. Checks run for this review

### 5.1 Gaussian check of the double-counting proposition

Script (scratch, not a project file): `/private/tmp/claude-501/-Users-theodoremui-dev-bioharness/c0c289fd-8fe6-48ca-ab62-0edfc09b41dd/scratchpad/p08/double_count.py`, seed 0, 2,000,000 draws. Setting: C in {0,1}; referral H in {0,1} with prior P(C=1|H) of 0.2 or 0.8; true quantity X given C is normal with mean 0 or 1 and sd 0.5; blind measurement M0 = X + noise with sd 0.7; reported M_g = (1 - g) M0 + g m_H with m_H = E[X|H]; the clinician combines the prior with the likelihood of a blind measurement.

| g | MSE of M_g against X | log loss, blind-calibrated combiner | log loss, recalibrated combiner |
|---|---|---|---|
| 0.0 | 0.489 | 0.4036 | 0.4036 |
| 0.1 | 0.400 | 0.4046 | 0.4036 |
| 0.3 | 0.277 | 0.4130 | 0.4036 |
| 0.5 | 0.225 | 0.4304 | 0.4036 |
| 0.7 | 0.245 | 0.4567 | 0.4036 |

The MSE-optimal shrinkage is g* = s^2 / (s^2 + Var(X|H)) = 0.544 here, which matches the MSE minimum in the table. The blind-calibrated combiner's log loss rises with g, as the brief claims, while a combiner that knows g and m_H recovers the blind optimum at every g < 1, because the adjustment is invertible given H. A non-invertible path effect (under H=1 the agent reports max(M0, 0.6), a stand-in for trimming in the "worse" direction) raises the best achievable log loss from 0.4034 to 0.4155 even for a nonparametric combiner fitted on (H, reported value). Consequences for the brief: (i) state the conditions for "strictly larger log loss for every g other than 0" (informative measurement, combiner calibrated on blind measurements); (ii) add the recalibration result, which is the obvious rebuttal; (iii) promote the non-invertible case to the main theorem. `research/theory-checks.md` section B1 is still PENDING and should replace this scratch check.

### 5.2 Facts checked against the project's facts file

From `research/biomech-facts.md`: StaBLE's reference is three-camera OpenCap with HRNet keypoints, video-derived, no markers or force plates; the Zenodo release has no videos (lab access needed); diagnoses are self-reported; StaBLE scores use min-max normalization over all 180 participants (label-scale leakage); BioCV (15 healthy adults: walking, running, jumping, hopping) and OpenCap LabValidation (10 healthy adults: squat, sit-to-stand, drop jump, walking) have marker and force references but no balance tasks; the frozen Qwen3-VL-8B score prompt had task-averaged MAE 0.238 against 0.120 for the training-task mean (lab pilot, unpublished).

## 6. Upgrades that would move the scores toward 4.5 to 5

1. Sharper question and a provable result: "calibration bug or information bug". Prove that any context-dependent transform of the blind measurement that is invertible given the context leaves the Bayes decision value unchanged (repairable by recalibration), while any context-dependent selection, trimming or censoring that is non-invertible strictly lowers it (a data-processing argument), with a closed form for the Gaussian and censored cases. Then the path-spliced indirect effect is the irrecoverable part of the framing effect, and the direct effect is the recalibratable part. This answers the strongest objection head on.
2. Pre-registered quantitative prediction for amplification. Under accuracy reward with informative referrals, the MSE-optimal policy is shrinkage with g* = s^2 / (s^2 + Var(X|H)), computable from the run-to-run noise s and the within-referral spread of the reference. Pre-register that self-improvement moves the agent's effective g toward g*, and that the "better measurer, worse decision" crossover appears at a predicted generation. A numerical endpoint predicted in advance is far stronger than "self-improvement amplifies bias".
3. Decisive experiment on the route of context. Pre-register the prediction that prompt and playbook evolution (GEPA, ACE), which write conditional procedural rules ("for frail referrals, trim at the first large excursion"), route context into the path, while GRPO with a scalar accuracy reward on the final number learns mostly direct shrinkage. Track the spliced indirect and direct effects per generation. If confirmed, this is a surprising and general finding about how self-improving agents absorb context; if refuted, the decomposition still tells practitioners which remedy is needed.
4. Close the visual-context channel. Add an appearance-blind condition (tools run on skeleton-only or appearance-masked renderings, or the agent sees only tool outputs) so that the hypothesis the agent infers from the video (age, gait aid, athletic build) is separated from the stated referral. No prior work separates stated from self-inferred context; for VLM measurement this is the analog of the physicists' hidden signal region.
5. Stronger baselines. (a) Recalibration: a combiner refitted on context-aware outputs (the cheapest fix and the one reviewers will ask for); (b) Epistemic Blinding-style masking of referral text (Cuccarese); (c) the reset-and-replay correction (Gunsilius et al.) in the analysis-agent domain; (d) Liu's neutral brief plus decision rule fixed outside the agent; (e) prompt-level "ignore the referral" and counterexample prompting (EchoBench; Jhaveri et al.). Blind analysis should beat (b) to (e) on decision log loss at similar cost, and should match (a) only when the route is direct.
6. Validate a ground-truth-free audit metric. Define the steering index as the framing-induced shift in the m-value of Miao et al. and show, on the subset with a reference, that it predicts the framing-induced error. A label-free audit that is validated against a reference is useful far beyond biomechanics.
7. Identification you can state as a proposition. With framing randomized and the path set by intervention, the average natural direct effect E[M(b, P(a))] - E[M(a, P(a))] is identified by sampling paths from F=a runs and replaying them into F=b reporting, without cross-world assumptions for this average, because the harness controls the mediator. Add placebo splices (a into a) to measure the splice artifact, since spliced transcripts are off-policy (the divergence problem noted by AttriGuard and Causal Agent Replay).
8. A second domain where the decision is real and n is large (Section 7), so the decision-quality claim does not rest on 10 to 15 healthy adults.

## 7. Must-fix items in the brief

1. Steering index: it is essentially the m-value of Miao et al. (2607.01507). Cite it and define the index as the framing-induced shift in m-value.
2. "What is missing (1)": a stage-level split of path versus answer effects exists for search agents (Xiao and Yu 2611.05720) and a failure-mode split for tool-using judges (Brown et al. 2611.05662). Reword the gap as an interventional split for continuous measurement with a reference.
3. Remedy precedent: cite Epistemic Blinding (2604.06013), Liu's neutral brief and sealed holdout (2611.04070), Gunsilius et al.'s replay correction (2611.23174) and Dutilh et al.'s data blinding (Synthese 2021), and say what blind analysis adds (a frozen measurement stage before any context, then interpretation).
4. Confront Asher et al.: directional hypotheses barely moved frontier coding agents on well-specified tasks. Pre-register that direct anchoring may be small for frontier agents and that effects should concentrate in weakly specified steps and ambiguous evidence (as Balani and Panda found).
5. "Physical ground truth": StaBLE's reference is three-camera OpenCap with HRNet, which is video-derived. BioCV and OpenCap LabValidation have markers and force plates but healthy adults only and no single-leg stance or other balance tasks. The running example (single-leg stance) therefore has no physical reference; use sit-to-stand or squat (in both StaBLE and LabValidation) as the bridge task for physical-reference claims, and say that framing effects themselves need no reference because framing is randomized.
6. Data access: StaBLE videos are lab-internal; the Zenodo release has features, scores and kinematics for 7 exemplar participants only.
7. "Consistent" versus "inconsistent" framing relies on the true group. The 71 diagnoses are self-reported; prefer age band, fall-risk group and elite status as the true group, and treat diagnosis-consistency as secondary.
8. Visual context leak: text blinding does not blind a VLM that sees an 80-year-old with a cane. Add the appearance-blind condition (Upgrade 4) or the "blind" arm is not blind.
9. Double-counting proposition: state the conditions (informative measurement; combiner calibrated on blind measurements; strictness generic, not universal) and add the recalibration result from Section 5.1. Theory-checks B1 is PENDING; do not present the proposition as verified until it is done.
10. "Amplification even when rewarded only for accuracy" is the expected behavior of an MSE-optimal learner when context predicts the label. Present it as a predicted endpoint (g*), not a surprise.
11. Evidence sensitivity: the slope of reported M on the reference is attenuated by reference noise (regression dilution) and is below 1 for any shrinkage estimator. Compare slopes across framings within agent, with an errors-in-variables correction, not against 1.
12. Gate on measurement: the frozen Qwen3-VL-8B score prompt is worse than the constant baseline (0.238 versus 0.120, lab pilot, unpublished). A framing audit on an agent with near-zero evidence sensitivity is uninformative; report evidence sensitivity first and run the main audit on tool pipelines that pass it.
13. "Blind then unblind with logged justification": chain-of-thought justifications are often unfaithful to the real cause (Turpin et al., NeurIPS 2023). Allow post-unblinding changes only from a pre-declared menu and score them, without relying on the justification text.
14. Path splicing: define the mediator (tool calls, parameters and tool outputs; reasoning tokens regenerated), add placebo splices, and report how often spliced transcripts trigger visible inconsistency handling by the agent.
15. Label leakage: StaBLE's min-max normalization uses all 180 participants; recompute L and U on the development split for any score used as a reference or reward.
16. Approval-reward arm (4b): optimizing against a judge that sees the hypothesis is a known route to sycophancy and misleading outputs (Sharma et al.; Wen et al.; Williams et al.). Position it as a positive control.
17. Code-review generalization: already shown by Alexopoulos et al. (ICSE 2027); cite it or drop the example.
18. Label lab-pilot numbers as unpublished in every place they appear, and do not cite DiscoveryBench with a venue (the arXiv page states none).

## 8. Second domain recommendation

Primary: EchoNet-Dynamic (Ouyang et al., "Video-based AI for beat-to-beat assessment of cardiac function", Nature 580:252 to 256, 2020; dataset page https://echonet.github.io/dynamic/, both verified). It has 10,030 apical four-chamber echocardiography videos from Stanford (2016 to 2018) with ejection fraction (EF), end-systolic and end-diastolic volumes and expert left-ventricle tracings, measured by a registered sonographer and verified by a level 3 echocardiographer; access is through the Stanford AIMI portal under a research use agreement. Why it fits: (i) it is video measurement with tool-like steps that are classic forking paths (left-ventricle segmentation, end-diastole and end-systole frame choice, which beats to average, whether to exclude a foreshortened view), so path splicing transfers directly; (ii) the output is a continuous number with standard clinical thresholds (EF below 50% or 40%), so decision quality can be scored; (iii) referral framings are natural ("suspected heart failure" against "baseline before chemotherapy" or "athlete screening"); (iv) n is large enough for self-improvement training and for well-powered framing audits; (v) it shares a research group with StaBLE, which eases access. Caveat: the EF labels came from the clinical workflow, where sonographers likely saw clinical context, so the reference may carry review bias; this affects accuracy estimates but not the randomized framing effect.

For the general agentic audience, add data-analysis agents on semi-synthetic data with known effects, using the ACIC 2016 causal-inference competition data (Dorie et al., arXiv 1707.02641, verified; the number of simulation settings is not stated on the abstract page and is UNVERIFIED here), with framing randomized against the true effect sign, and BLADE (Gu et al., EMNLP 2024 per arXiv comments, verified) for expert-annotated alternative analyses. This domain is more crowded (Asher et al., Gunsilius et al., Liu, Balani and Panda), so its role is to show the route-of-context result generalizes, not to carry the novelty.

## 9. Key citations

| # | Reference | URL | Claim it supports | Verified |
|---|---|---|---|---|
| 1 | Klein JR, Roodman A. Blind analysis in nuclear and particle physics. Annu Rev Nucl Part Sci 55:141 to 163, 2005 | https://doi.org/10.1146/annurev.nucl.55.090704.151521 | Origin and methods of blind analysis in physics | yes (Crossref) |
| 2 | MacCoun R, Perlmutter S. Blind analysis: Hide results to seek the truth. Nature 526:187 to 189, 2015 | https://doi.org/10.1038/526187a | Blind analysis proposed for other sciences, including data blinding | yes (Crossref) |
| 3 | Dutilh G, Sarafoglou A, Wagenmakers E-J. Flexible yet fair: blinding analyses in experimental psychology. Synthese 198(S23):5745 to 5772, 2021 | https://doi.org/10.1007/s11229-019-02456-7 | Analysis blinding by shuffling the criterion variable; complement to preregistration | yes (Crossref) |
| 4 | Gelman A, Loken E. The garden of forking paths. Working paper, 14 Nov 2013 | https://sites.stat.columbia.edu/gelman/research/unpublished/p_hacking.pdf | Data-contingent analysis choices create multiplicity without fishing | yes (PDF page 1 read) |
| 5 | Simmons JP, Nelson LD, Simonsohn U. False-positive psychology. Psychol Sci 22(11):1359 to 1366, 2011 | https://doi.org/10.1177/0956797611417632 | Researcher degrees of freedom inflate false positives | yes (Europe PMC) |
| 6 | Steegen S, Tuerlinckx F, Gelman A, Vanpaemel W. Increasing transparency through a multiverse analysis. Perspect Psychol Sci 11(5):702 to 712, 2016 | https://doi.org/10.1177/1745691616658637 | Multiverse of defensible processing choices | yes (Europe PMC) |
| 7 | Loy CT, Irwig L. Accuracy of diagnostic tests read with and without clinical information. JAMA 292(13):1602, 2004 | https://doi.org/10.1001/jama.292.13.1602 | Clinical information generally improves reading accuracy (the counterweight) | yes (Crossref, Europe PMC) |
| 8 | Whiting PF et al. QUADAS-2. Ann Intern Med 155(8):529 to 536, 2011 | https://doi.org/10.7326/0003-4819-155-8-201110180-00009 | Risk-of-bias domains for diagnostic accuracy, including index-test interpretation | yes (Europe PMC; the exact signalling-question wording was not re-read) |
| 9 | Worster A, Carpenter C. Incorporation bias in studies of diagnostic tests. CJEM 10(2):174 to 175, 2008 | https://doi.org/10.1017/S1481803500009891 | Named form of double counting when the test is part of the reference | yes (Europe PMC record; no abstract) |
| 10 | Hrobjartsson A et al. Observer bias in randomized clinical trials with measurement scale outcomes. CMAJ 185(4):E201 to E211, 2013 | https://doi.org/10.1503/cmaj.120744 | Nonblinded assessors exaggerate effect sizes by 68% (95% CI 14% to 230%) | yes (PMC3589328) |
| 11 | Kriegeskorte N et al. Circular analysis in systems neuroscience: the dangers of double dipping. Nat Neurosci 12(5):535 to 540, 2009 | https://doi.org/10.1038/nn.2303 | Selection-dependent analysis distorts estimates; 42% of 134 fMRI papers | yes (PMC2841687) |
| 12 | Palley AB, Soll JB. Extracting the wisdom of crowds when information is shared. Management Science, 2019 | https://doi.org/10.1287/mnsc.2018.3047 | Shared information is over-weighted when combined as if independent | yes (Crossref; volume and pages not shown) |
| 13 | Batista RM, Griffiths TL. A rational analysis of the effects of sycophantic AI. arXiv 2602.14270, 2026 | https://arxiv.org/abs/2602.14270 | Hypothesis-shaped evidence inflates confidence without progress | yes |
| 14 | Pearl J. Direct and indirect effects. UAI 2001, pp. 411 to 420 | https://arxiv.org/abs/1301.2300 | Definitions of direct and indirect effects used for path splicing | yes |
| 15 | Asher SGZ et al. Do Claude Code and Codex P-Hack? Working paper, 2026 | https://www.andrewbenjaminhall.com/pdfs/asher_et_al_LLM_sycophancy.pdf | Frontier agents stable under standard prompts; reframing bypasses guardrails | yes (PDF) |
| 16 | Miao J, Pritchard JK, Zou J. The Agentic Garden of Forking Paths. arXiv 2607.01507, 2026 | https://arxiv.org/abs/2607.01507 | Persona beliefs steer conclusions; m-value and Agentic Bootstrap | yes |
| 17 | Bertran M, Fogliato R, Wu ZS. Many AI Analysts, One Dataset. arXiv 2602.18710, 2026 | https://arxiv.org/abs/2602.18710 | Persona and model steer results among audited-sound runs | yes |
| 18 | Gunsilius F, Van Dijcke D, Wuthrich K. Inference after coding agents. arXiv 2611.23174, 2026 | https://arxiv.org/abs/2611.23174 | 54% to 98% false significance under pressure; replay correction | yes |
| 19 | Liu C. Evaluating LLM Research Agents as Tests of Return Predictability. arXiv 2611.04070, 2026 | https://arxiv.org/abs/2611.04070 | One sentence about prior research changes verdicts; neutral brief and sealed holdout | yes |
| 20 | Balani P, Panda S. Reporting Under Pressure. arXiv 2609.27756, 2026 | https://arxiv.org/abs/2609.27756 | Framing distorts facts mainly where evidence is ambiguous | yes |
| 21 | Brown DB et al. Grounded but Not Immune: Confirmation Bias in Agent-as-a-judge. arXiv 2611.05662, 2026 | https://arxiv.org/abs/2611.05662 | A false hint flips up to 40% of a tool-using judge's correct verdicts | yes |
| 22 | Xiao Y, Yu Y. Cognitive Bias Signatures in Search-Equipped LLM Agents. arXiv 2611.05720, 2026 | https://arxiv.org/abs/2611.05720 | Stage-resolved separation of retrieval effects from persisting errors | yes |
| 23 | Cuccarese M. Epistemic Blinding. arXiv 2604.06013, 2026 | https://arxiv.org/abs/2604.06013 | Blind-versus-unblind protocol for agentic analysis (entity identity) | yes |
| 24 | Restrepo D et al. Medical Context Distorts Decisions in Clinical Vision Language Models. arXiv 2605.17436, 2026 | https://arxiv.org/abs/2605.17436 | Clinical VLMs follow text and irrelevant history over the image | yes |
| 25 | Yuan B et al. EchoBench. arXiv 2509.20146, 2025 | https://arxiv.org/abs/2509.20146 | High sycophancy rates in medical VLMs; prompt mitigations help | yes |
| 26 | Alexopoulos G et al. When AI Agrees Too Much. arXiv 2603.18740; ICSE 2027 | https://arxiv.org/abs/2603.18740 | Framing PR metadata biases automated code review | yes |
| 27 | Turpin M, Michael J, Perez E, Bowman SR. Language Models Don't Always Say What They Think. NeurIPS 2023 | https://arxiv.org/abs/2305.04388 | Biasing features change answers without being mentioned in the explanation | yes |
| 28 | Ouyang D et al. Video-based AI for beat-to-beat assessment of cardiac function. Nature 580:252 to 256, 2020 | https://doi.org/10.1038/s41586-020-2145-8 | EchoNet-Dynamic, 10,030 echo videos, for the second domain | yes (Crossref and dataset page) |

Further verified works used in the review: Shah, Causal Agent Replay, arXiv 2606.08275 (https://arxiv.org/abs/2606.08275; step-level do-interventions and replay for failure attribution); He et al., AttriGuard, USENIX Security 2026 per arXiv comments (https://arxiv.org/abs/2603.10749; teacher-forced shadow replay against trajectory divergence); Xu et al., Pride and Prejudice, ACL 2024 pp. 15474 to 15492 (https://aclanthology.org/2024.acl-long.826/; self-refinement amplifies self-bias); Pan et al., Feedback Loops With Language Models Drive In-Context Reward Hacking, ICML 2024 camera-ready per arXiv (https://arxiv.org/abs/2402.06627); Williams et al., On Targeted Manipulation and Deception when Optimizing LLMs for User Feedback, ICLR 2025 (https://arxiv.org/abs/2411.02306); Wen et al., Language Models Learn to Mislead Humans via RLHF, arXiv 2409.12822 (https://arxiv.org/abs/2409.12822; the arXiv page names no venue, and a 2026 ICLR blog post disputes its experiments); Sharma et al., Towards Understanding Sycophancy in Language Models, arXiv 2310.13548 (https://arxiv.org/abs/2310.13548); Jhaveri et al., Failing to Falsify, NeurIPS 2026 camera-ready per arXiv (https://arxiv.org/abs/2604.02485; counterexample prompting raises rule discovery from 42% to 56%); Luo, Kasirzadeh, Shah, Hidden Pitfalls of AI Scientist Systems, NeurIPS 2025 AI4Science spotlight (https://arxiv.org/abs/2509.08713; post-hoc selection bias and leakage, traces reveal failures); Vaccaro, Preregistration for Experiments with AI Agents, ICML 2026 position paper spotlight per arXiv (https://arxiv.org/abs/2606.11217; preregistration of experiments on agents, not by agents); Gu et al., BLADE, EMNLP 2024 per arXiv (https://arxiv.org/abs/2408.09667); Majumder et al., DiscoveryBench, arXiv 2407.01725 (https://arxiv.org/abs/2407.01725; 264 tasks, 903 synthetic); Agrawal et al., GEPA, ICLR 2026 oral per arXiv (https://arxiv.org/abs/2507.19457); Zhang et al., ACE, ICLR 2026 per arXiv (https://arxiv.org/abs/2510.04618); Lu et al., The AI Scientist, arXiv 2408.06292 (https://arxiv.org/abs/2408.06292); Luo et al., ViLP, arXiv 2501.00569 (https://arxiv.org/abs/2501.00569; GPT-4 66.17%); Lou and Sun, Anchoring Bias in LLMs, arXiv 2412.06593 (https://arxiv.org/abs/2412.06593); Baumann et al., LLM Hacking, arXiv 2509.08825 (https://arxiv.org/abs/2509.08825; about 31% of hypotheses reach wrong conclusions with state-of-the-art annotators); Monte e Freitas et al., Can VLMs Judge Action Quality?, arXiv 2604.08294 (https://arxiv.org/abs/2604.08294; near-chance quality judgments and a bias toward "correct execution"); Li et al., VLMs for Human Motion Understanding in Stroke Rehabilitation, arXiv 2511.17727 (https://arxiv.org/abs/2511.17727; dose estimates no better than a video-blind baseline); Dorie et al., ACIC 2016 competition, arXiv 1707.02641 (https://arxiv.org/abs/1707.02641).

## 10. Unverified or uncertain items

- Asher et al.: the claim that directional-prior framing alone made little difference, and the "about 4.2 published SEs" figure for Claude under the nuclear prompt, come from search snippets; the abstract (read) does not state the framing main effect. Read the results section before quoting numbers.
- Alexopoulos et al.: a "16% to 93% drop in detection" figure appeared in a search snippet of the v1 HTML; the current abstract does not contain it. UNVERIFIED.
- QUADAS-2: that "index test interpreted without knowledge of the reference standard" is a signalling question was not confirmed on the fetched record (standard knowledge, but re-read the tool before quoting).
- DiscoveryBench venue (ICLR 2025 in the earlier run's notes): UNVERIFIED; the arXiv page states no venue.
- Palley and Soll 2019: volume and pages not shown on the Crossref search result.
- ACIC 2016 number of simulation settings and replications: UNVERIFIED.
- AgentSentry (2602.22724), BadScientist (2510.18003), Confirming Our Biases (2608.06977), VLind-Bench (2406.08702), 2505.15392, 2511.05766, 2606.10400, 2610.21902, 2509.21979, 2506.22316, 2604.02668, 2608.05179, 2607.27191: seen in search results only in this run; not used for claims above.
- Hrobjartsson et al. updated analysis (Salazar et al., SSRN 5141572, 29% exaggeration in odds ratios): seen only in a search snippet. UNVERIFIED.
