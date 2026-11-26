# P08 Certified Self-Compilation: literature and novelty check

Status: complete (searches run 2026-11-24). Every URL marked "verified" was fetched in this session (arXiv abstract page, proceedings page or PDF header, PMC page, or a DOI redirect that resolved to the same publisher record). Items that could not be fetched are marked UNVERIFIED.

## 0. The idea under review

A tool-using agent (pilot: Qwen3-VL-8B calling RTMPose, OpenCap Monocular, SAM 2, CoTracker3 and similar tools on StaBLE balance videos) repeatedly solves the same kinds of task. P08 proposes that the agent mine its own recurring tool-call trajectories, turn them into ordinary programs, and pair each program with a learned validity gate. When the gate accepts an input, the program runs in place of deliberation; when it rejects, the agent deliberates as before. The claim to be certified is that on new people the compiled path is cheaper, more repeatable (higher test-retest ICC, smaller minimal detectable change) and, with a finite-sample guarantee from Learn-then-Test (LTT) or conformal risk control (CRC), no less accurate than deliberation on the inputs it accepts. Each such replacement is framed as a statistically certified self-modification, placed between the proof-based Goedel machine and the empirical Darwin Goedel Machine.

Terms used below:

- Compilation: replacing a model-driven loop (deliberation) with a fixed program that makes the same tool calls without per-step model reasoning.
- Validity gate: a function of the input, and of signals computed while the program runs, that decides whether the program's output is trusted or the input is sent back to deliberation.
- Selective risk: the error rate among accepted inputs only. Joint risk: the probability that an input is both accepted and wrong. Joint risk is monotone in the gate threshold; selective risk usually is not, which matters for which calibration method applies.
- LTT: calibrates a threshold by testing, for each candidate threshold, the null hypothesis "risk exceeds alpha", and keeping thresholds whose null is rejected; the result holds with probability at least 1 minus epsilon over the calibration draw and does not need monotone risk.
- CRC: picks a threshold so that the expected value of a monotone loss is at most alpha; the guarantee is in expectation over the calibration draw.

## 1. Search log

| # | Query (WebSearch unless noted) | Main hits used |
|---|---|---|
| 1 | Agent Workflow Memory | arXiv 2409.07429, ICML 2025 (PMLR v267) |
| 2 | Agent Skill Induction ASI web agents programs | arXiv 2504.06821 (COLM 2025) |
| 3 | Agentic Plan Caching | arXiv 2506.14852 (NeurIPS 2025) |
| 4 | AgentRR record and replay agents | arXiv 2505.17716 |
| 5 | learn then test risk control | arXiv 2110.01052; Ann. Appl. Stat. 19(2), 2025 |
| 6 | conformal prediction LLM agents tool use abstain | 2405.01563, 2502.06884 (single-output abstention only) |
| 7 | compile LLM agent trajectories into code (extended) | TraceCompiler 2608.02680; Compiled AI 2604.05150 |
| 8 | KnowNo robots ask for help conformal | arXiv 2307.01928, PMLR v229 |
| 9 | conformal risk control agent skill cache fallback (extended) | Auto 2607.04542; ToolChain-CRC 2606.18467; role-stratified CRC 2607.24343; Conformal Policy Control 2603.02196 |
| 10 | Distilling System 2 into System 1 | arXiv 2407.06023 |
| 11 | Darwin Godel Machine | arXiv 2505.22954 |
| 12 | tau-bench pass^k | arXiv 2406.12045; tau2-bench 2506.07982 |
| 13 | weighted conformal prediction covariate shift | arXiv 1904.06019 (NeurIPS 2019) |
| 14 | test-retest markerless motion capture ICC MDC | Horsak et al. J Biomech 2024; OpenCap PLOS Comp Biol 2023 |
| 15 | LLM nondeterminism reproducibility | arXiv 2408.04667 |
| 16 | "Learn then Test" LLM agent workflow skill (extended) | no direct hit |
| 17 | Trust or Escalate provable guarantees | arXiv 2407.18370 (ICLR 2025) |
| 18 | statistical guarantee self-modification e-values (extended) | SGM 2510.10232; SEA 2607.00871; statistical limits 2510.04399 (TMLR); Conformal Selective Acting 2605.20270 |
| 19 | Huxley-Goedel Machine | arXiv 2510.21614 (ICLR 2026 per conference site) |
| 20 | SkillWeaver | arXiv 2504.07079 |
| 21 | LLM agent repeated runs ICC | arXiv 2512.06710 |
| 22 | risk-controlled LLM cascade deferral conformal | Conformal Cascade 2607.25018; CompCRC 2611.11114; Conformal Arbitrage 2506.00911 (NeurIPS 2025) |
| 23 | agent skill reuse statistical guarantee (extended) | Skill-V 2610.11781 (no guarantee) |
| 24 | agent JIT compilation guards deoptimization (extended) | ReaComp 2605.05485; Agent JIT 2605.21470 (ICML 2026); AgentPRO 2611.00628 |
| 25 | vCache verified semantic prompt caching | arXiv 2502.03771 (ICLR 2026 per arXiv comments) |

The decisive finding of the search is that the 2026 literature already contains (a) several trace-to-program compilers, (b) one system, Auto, that runs compiled agent behavior behind split-conformal guards with fallback and recompilation, (c) a statistical Goedel machine that gates self-modifications with e-values under a global error budget, and (d) a crowded line of risk-controlled LLM cascades. P08's novelty therefore has to be argued at the level of what these works certify and how, not at the level of "compile plus gate plus guarantee".

## 2. Closest prior work

Ordered from closest to more distant. "Overlap" is with P08; "open" is what the work leaves for P08.

### 2.1 Auto: The AGI Compiler (closest system)

- Citation: Jaber, J. and Jaber, O. "Auto: The AGI Compiler." arXiv 2607.04542, July 2026. https://arxiv.org/abs/2607.04542 (verified; HTML version also read).
- What they did: Auto records live agent behavior, measures which spans are "witnessed-deterministic" (seen at least twice with identical output), and extracts them into verified programs or distilled specialist models, packaged as WebAssembly artifacts with manifests. A tiered runtime runs compiled behavior behind guards; a guard trip falls back ("deoptimizes") to the reference agent (gpt-5.4-mini in their runs), and the new trace is recompiled. Guards use lexical trigram similarity to witnessed inputs, with an abstention threshold set by split-conformal calibration over leave-one-out scores at a declared miscoverage alpha (0.1 or 0.4). On their pre-registered AUTO-BENCH, 87.1 percent of 560 spans are witnessed-deterministic; on a 300-item stream with three scheduled shifts, marginal cost falls from 59 to 2 micro-dollars per item, with 96.9 percent parity with the reference on witnessed inputs. They also report that a loose guard silently mislabels 48.9 percent of compiled answers against design labels, and they state that parity is not ground truth.
- Overlap: nearly the whole P08 pipeline (mine traces, compile, guard, fall back, recompile in a loop), including a conformal calibration step and a cost objective.
- Open: the guard certifies input familiarity (coverage of a similarity score), not the error of compiled outputs; there is no LTT or CRC guarantee on accuracy relative to the reference or to ground truth; no comparison with AWM, ASI, plan caching or distillation; no repeatability or measurement-reliability analysis; text-only tasks with small calibration sets (20 to 40 inputs per family); no treatment of grouped data, covariate shift (weighted conformal) or the validity of repeated recompilation. Their 48.9 percent silent-error figure is direct evidence that an uncertified or familiarity-only guard is not enough, which strengthens P08's motivation.

### 2.2 SGM: A Statistical Goedel Machine (owns the framing)

- Citation: Wu, X. et al. "SGM: A Statistical Godel Machine for Risk-Controlled Recursive Self-Modification." arXiv 2510.10232, October 2025 (v2 September 2026). https://arxiv.org/abs/2510.10232 (verified).
- What they did: replace the Goedel machine's proof obligation with statistical tests (e-values, Hoeffding bounds). A self-modification is admitted only when its superiority is certified at a chosen confidence, and a global error budget bounds the chance of ever accepting a non-improving edit; Confirm-Triggered Harmonic Spending spends the budget only on edits that reach a confirmation stage. Experiments in supervised learning (certified gain on CIFAR-100, rejection of a spurious gain on ImageNet-100), RL and black-box optimization.
- Overlap: P08's proposed framing ("statistically certified self-modification, between the Goedel machine and the DGM") is this paper's thesis.
- Open: SGM makes one global accept or reject decision per edit and certifies average improvement; it does not certify a self-replacement on a learned subset of inputs, does not target cost, and assumes i.i.d. evaluation with a stable harness. P08 can cite SGM for the framing and must claim something narrower and different: input-conditional (selective) certification of a self-replacement.

### 2.3 Trust or Escalate (statistical template for a certified cheap path)

- Citation: Jung, J., Brahman, F. and Choi, Y. "Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement." ICLR 2025; arXiv 2407.18370. https://arxiv.org/abs/2407.18370 (verified; ICLR 2025 header confirmed from the proceedings PDF https://proceedings.iclr.cc/paper_files/paper/2025/file/08dabd5345b37fffcbe335bd578b15a0-Paper-Conference.pdf).
- What they did: a judge estimates its confidence (Simulated Annotators); a threshold chosen by fixed-sequence testing on a small calibration set guarantees, with high probability, that accepted judgments agree with humans at a user-set level; cascades from a cheap model (Mistral-7B) to stronger ones. On a Chatbot Arena subset they guarantee over 80 percent human agreement at nearly 80 percent coverage and report large cost reductions relative to GPT-4.
- Overlap: this is the LTT-style certificate P08 needs (selective risk on accepted items, high-probability guarantee, cascade to an expensive path).
- Open: the cheap path is a fixed pretrained model, not a program the agent synthesized from its own traces; outputs are discrete preferences; no repeated self-modification, no regression outputs with clinical tolerances, no reliability metrics.

### 2.4 Risk-controlled cascades and routing

- Conformal Arbitrage: Overman, W. and Bayati, M. "Conformal Arbitrage: Risk-Controlled Balancing of Competing Objectives in Language Models." NeurIPS 2025; arXiv 2506.00911. https://arxiv.org/abs/2506.00911 (verified; NeurIPS 2025 proceedings PDF first page read: https://proceedings.neurips.cc/paper_files/paper/2025/file/65a655c5a267f678fd3e897e4137ef53-Paper-Conference.pdf). A CRC-calibrated threshold routes between a primary model and a conservative guardian so that the long-run rate of undesirable events stays under a quota.
- Conformal Cascade: Dou, Y., Lian, S. and Li, S. "Conformal Cascade: Distribution-Free Accuracy Guarantees for Multi-Tier LLM Inference." arXiv 2607.25018, July 2026. https://arxiv.org/abs/2607.25018 (verified). Accept when the conformal set at a tier is a singleton; coverage at least 1 minus K alpha over K tiers; 18 multiple-choice benchmarks.
- CompCRC: Sun, Y. et al. "Compositional Conformal Risk Control for Multi-Stage LLM Cascades." arXiv 2611.11114, November 2026. https://arxiv.org/abs/2611.11114 (verified). Splits accepted-error risk into additive stage-wise budgets with a finite-sample bound under conditional exchangeability; MMLU, GSM8K, HellaSwag.
- Overlap: the statistics of "accept cheap output, else escalate, with a guarantee" are established, including multi-stage composition.
- Open: all tiers are fixed pretrained models on classification-style tasks; none has tiers that are created, revised and re-certified by the system itself, and none studies regression outputs, repeatability or grouped (person-clustered) data.

### 2.5 vCache: verified semantic caching

- Citation: Schroeder, L. G. et al. "vCache: Verified Semantic Prompt Caching." arXiv 2502.03771 (ICLR 2026 accepted, per arXiv comments). https://arxiv.org/abs/2502.03771 (verified).
- What they did: per-entry similarity thresholds learned online, with an exploration probability that calls the LLM anyway to check whether the cached answer would have been right, giving user-defined error-rate guarantees on cache hits; up to 12.5x higher hit rates and up to 26x lower error rates than static thresholds.
- Overlap: a reuse mechanism with a learned gate and an error-rate guarantee, verified by occasionally running the expensive path. This is the closest analogue of P08's "label-free" certification against the expensive path.
- Open: reuses stored answers rather than executing a program on a new input, so the reused output does not depend on the new input; no tool calls, no trajectories, no repeatability.

### 2.6 Programmatic skills from trajectories: ASI, AWM, SkillWeaver, Voyager

- ASI: Wang, Z. Z., Gandhi, A., Neubig, G. and Fried, D. "Inducing Programmatic Skills for Agentic Tasks." COLM 2025 (per arXiv PDF header); arXiv 2504.06821. https://arxiv.org/abs/2504.06821 (verified). Induces Python skills from trajectories and admits them only if a rewritten trajectory using the skill passes verification; on WebArena, 23.5 percent higher success than a static agent and 11.3 percent over AWM, with 10.7 to 15.3 percent fewer steps.
- AWM: Wang, Z. Z., Mao, J., Fried, D. and Neubig, G. "Agent Workflow Memory." ICML 2025, PMLR 267; arXiv 2409.07429. https://arxiv.org/abs/2409.07429 and https://proceedings.mlr.press/v267/wang25bx.html (verified). Induces text workflows from successful trajectories (online mode uses an LM evaluator to judge success).
- SkillWeaver: Zheng, B. et al. "SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills." arXiv 2504.07079. https://arxiv.org/abs/2504.07079 (verified). Explores websites, synthesizes Python APIs, tests them on generated cases; 31.8 and 39.8 percent relative gains on WebArena and real sites.
- Voyager: Wang, G. et al. "Voyager: An Open-Ended Embodied Agent with Large Language Models." arXiv 2305.16291. https://arxiv.org/abs/2305.16291 (verified). Executable-code skill library with self-verification in Minecraft.
- Overlap: the "trajectory to program" step and the idea of admitting a skill only after a check.
- Open: verification is a pass or fail check on a few trajectories, with no statement about the error rate on new inputs; skills are callable by the agent (the agent still deliberates about when to call them) rather than replacing deliberation under a certified gate; no cost-accuracy-reliability accounting on held-out people.

### 2.7 Trace compilers without certification: TraceCompiler, Compiled AI, ReaComp, Agent JIT, AgentPRO

- TraceCompiler: El Yadouni, S. and Li, G. arXiv 2608.02680, August 2026. https://arxiv.org/abs/2608.02680 (verified). Mines noisy traces into mostly deterministic workflows with residual LLM decisions; refuses to compile an intent with an underdetermined irreversible side effect; AppWorld and T1; explicitly makes no net efficiency claim.
- Compiled AI: Trooskens, G. et al. "Compiled AI: Deterministic Code Generation for LLM-Based Workflow Automation." arXiv 2604.05150, 2026. https://arxiv.org/abs/2604.05150 (verified). LLM writes code once; workflow then runs without model calls; 96 percent task completion on BFCL (n = 400) with zero execution tokens; four-stage validation; no fallback and no statistical guarantee.
- ReaComp: Naik, A. et al. arXiv 2605.05485, May 2026. https://arxiv.org/abs/2605.05485 (verified). Compiles LLM reasoning traces into symbolic solvers over DSLs; zero test-time LLM calls, hybrid mode with LLM search.
- Agent JIT Compilation: Winston, C. et al. ICML 2026; arXiv 2605.21470. https://arxiv.org/abs/2605.21470 (verified). Compiles task descriptions into code plans with pre and postconditions; 10.4x speedup over Browser-Use.
- AgentPRO: Ren, J. and Wang, Z. arXiv 2611.00628. https://arxiv.org/abs/2611.00628 (verified). Guarded compiler rewrites with runtime fallback on AppWorld; 41.85 percent fewer tokens; no accuracy guarantee.
- Open for all five: no finite-sample statement about the accuracy of the compiled path relative to deliberation on new inputs.

### 2.8 Agentic Plan Caching and AgentRR

- Agentic Plan Caching: Zhang, Q., Wornow, M., Wan, G. and Olukotun, K. NeurIPS 2025; arXiv 2506.14852. https://arxiv.org/abs/2506.14852 (verified). Extracts plan templates from completed runs, matches new requests by keyword extraction, adapts templates with a small model; 50.31 percent lower cost and 27.28 percent lower latency on average. The abstract describes no reuse gate with a guarantee.
- AgentRR: Feng, E. et al. "Get Experience from Practice: LLM Agents with Record & Replay." arXiv 2505.17716. https://arxiv.org/abs/2505.17716 (verified). Records traces, summarizes them into multi-level experiences, replays them with "check functions" as a trust anchor; the abstract reports no quantitative evaluation.
- Open: both give cost reduction from reuse with heuristic matching or hand-written checks; neither quantifies or bounds the error introduced by reuse.

### 2.9 Distillation into weights

- Kang, M. et al. "Distilling LLM Agent into Small Models with Retrieval and Code Tools." NeurIPS 2025 Spotlight (arXiv comments); arXiv 2505.17612. https://arxiv.org/abs/2505.17612 (verified). Transfers full agent trajectories into 0.5B to 7B students that match or beat larger CoT-distilled models.
- Yu, P., Xu, J., Weston, J. and Kulikov, I. "Distilling System 2 into System 1." arXiv 2407.06023. https://arxiv.org/abs/2407.06023 (verified). Self-supervised distillation of System 2 prompting outputs into direct answers at lower inference cost.
- Overlap: the alternative way to amortize deliberation, and the main competitor P08 must beat or match.
- Open: distilled weights remain stochastic and opaque; no gate, no guarantee, no reliability analysis.

### 2.10 Reliability of agent outputs

- Mustahsan, Z. et al. "Stochasticity in Agentic Evaluations: Quantifying Inconsistency with Intraclass Correlation." arXiv 2512.06710, December 2025. https://arxiv.org/abs/2512.06710 (verified). Uses ICC to split variance into task and agent-inconsistency parts on GAIA and FRAMES; recommends trusting sub-agent replacement only when ICC also improves.
- Yao, S. et al. "tau-bench." arXiv 2406.12045. https://arxiv.org/abs/2406.12045 (verified). Introduces pass^k; gpt-4o pass^8 below 25 percent in retail.
- Atil, B. et al. "Non-Determinism of 'Deterministic' LLM Settings." arXiv 2408.04667. https://arxiv.org/abs/2408.04667 (verified). Accuracy varies up to 15 percent across 10 runs in configurations meant to be deterministic.
- Open: these measure inconsistency; none uses compilation as a way to remove it, and none certifies a reliability gain.

### 2.11 Other certified self-improvement and agent risk control (context)

- SEA: Sengupta, B. "Self-Evolving Agents with Anytime-Valid Certificates." arXiv 2607.00871. https://arxiv.org/abs/2607.00871 (verified). Anytime-valid gates on self-edits of a steering adapter and harness; 52-instance SWE-bench Verified subset; single runs.
- Wang, C. L., Dorchen, K. and Jin, P. "On the Statistical Limits of Self-Improving Agents." TMLR 2026 (arXiv comments); arXiv 2510.04399. https://arxiv.org/abs/2510.04399 (verified). Two-Gate guardrail (validation margin plus capacity cap) preserves PAC learnability under self-modification.
- Opoku, J. and Banahene, D. "ToolChain-CRC." arXiv 2606.18467. https://arxiv.org/abs/2606.18467 (verified). Trajectory-level CRC with an anytime alarm for tool-using agents under drift.
- Ren, A. Z. et al. "Robots That Ask For Help (KnowNo)." CoRL 2023, PMLR 229:661-682. https://proceedings.mlr.press/v229/ren23a.html (verified). Conformal prediction sets over LLM plan options; ask for help when the set is not a singleton.
- Prinster, D. et al. "Conformal Policy Control." ICML 2026; arXiv 2603.02196. https://arxiv.org/abs/2603.02196 (verified). A safe reference policy regulates how far a new policy may deviate, with finite-sample risk guarantees.
- These show that "risk control around agent actions" and "certified self-edits" are both active; none certifies the replacement of deliberation by a self-written program.

## 3. Is the core idea already done?

Verdict: partially.

Each ingredient of P08 exists. Trajectory-to-program compilation is established (ASI, SkillWeaver, Voyager, TraceCompiler, Compiled AI, ReaComp). Gated execution with fallback and a recompile loop exists in Auto, which even uses split-conformal calibration. Finite-sample guarantees for "accept the cheap output, else escalate" exist for fixed models (Trust or Escalate, Conformal Arbitrage, Conformal Cascade, CompCRC) and for answer caches (vCache). The framing of statistically certified self-modification as a middle ground between the Goedel machine and the DGM is the stated thesis of SGM. ICC as an agent-consistency metric is in 2512.06710. A reviewer who knows these papers would say the combination is natural and that Auto is a working version of it.

What none of these papers does, and what P08 can own, is the following, stated as one residual gap:

> A finite-sample, input-conditional certificate that a program the agent wrote from its own trajectories is non-inferior to the agent's own stochastic deliberation on the inputs its gate accepts, valid under person-clustered data and device shift, maintained across repeated rounds of self-compilation, and accompanied by a measured gain in test-retest reliability (ICC, MDC) on continuous measurement outputs.

Four parts of that sentence are new relative to the closest work:

1. Certified quantity. Auto certifies how familiar an input is; SGM certifies that an edit improves an average; cascades certify agreement of a fixed model with a label. P08 would certify the paired, per-input discrepancy between compiled output and the deliberation distribution, which needs no ground-truth labels (only extra deliberation runs on a calibration sample) and implies a ground-truth bound by the triangle inequality (Section 5.2).
2. Self-generated, revisable cheap tier. In every certified cascade the cheap tier is fixed in advance. In P08 the cheap tier is produced by the system, from data that overlaps the deployment distribution, and is revised over generations. This creates two statistical issues that no cited paper handles together: the compile, certify and test data must be disjoint at the person level, and later generations are compiled from, and certified on, the residual inputs that earlier gates rejected.
3. Reliability as a certified outcome. No compilation paper measures test-retest ICC or MDC, and no reliability paper uses compilation to remove the agent's own sampling variance.
4. Continuous outputs with clinical tolerances, person clusters and device shift (three phones in StaBLE), where exchangeability is the assumption most likely to fail.

## 4. Scores (demanding ICML area chair)

- Novelty: 3.0 out of 5 as currently written. The pipeline is close to Auto, the certification framing belongs to SGM, and the statistics are those of Trust or Escalate and CRC cascades. With the sharpenings in Section 5 (paired label-free certificate against stochastic deliberation; validity across self-compilation generations on residual streams; reliability as the primary outcome; explicit failure tests under person clustering and phone shift) the contribution would read as about 3.5 to 4.0. Reaching 4.5 would need a new result that is surprising to the ML audience, for example evidence that certification changes what the self-improvement loop compiles (coverage grows over generations while realized risk stays under alpha, whereas uncertified compilers drift into silent error), or a theorem for the residual-stream setting that existing CompCRC and SGM results do not cover.
- Significance: 3.5 out of 5. For agent deployment the question of when a self-written shortcut can be trusted is general and costly to get wrong (Auto's 48.9 percent silent-error figure is a concrete warning). For clinical measurement, repeatability and MDC decide whether an instrument can track change in a patient, so an agent whose score changes on rerun is unusable as a measurement device; a certified, deterministic path addresses that directly. Significance is held back by two practical limits: StaBLE's size makes person-level certificates loose (Section 5.6), and if GPU tool calls dominate cost, compilation saves less than it does in text-only agents.

## 5. Sharpenings

### 5.1 Recast the claim

Drop "certified self-modification" as the headline (cite SGM for it) and claim: "selective certification of agent-written self-replacements". The research question becomes: when an agent compiles its own recurring tool-call trajectories into programs, can a learned gate certify, from a small unlabeled calibration sample, that the program is within a stated tolerance of the agent's own deliberation on the inputs it accepts, and does this certified replacement improve repeatability without losing accuracy on new people and new phones?

### 5.2 The certificate, concretely

Notation: $x$ is one recording; $D(x)$ is one deliberation run (a random variable because decoding and some GPU tools are nondeterministic); $\bar D_k(x)$ is the mean of $k$ independent runs; $C(x)$ is the compiled program's output; $s(x)$ is the gate score (for example tool confidences, track continuity, program assertion results, distance to the compile set); the gate accepts when $s(x) \le \lambda$; $\delta_t$ is a task-specific tolerance, set from the task's clinical MDC or score range.

Loss: $L(x) = \mathbf{1}\{|C(x) - \bar D_k(x)| > \delta_t\}$. Selective risk: $R(\lambda) = P(L = 1 \mid s(x) \le \lambda)$.

LTT procedure: order a grid $\lambda_1 < \dots < \lambda_J$; for each $j$ test $H_j: R(\lambda_j) > \alpha$ with a binomial (Clopper-Pearson) or Waudby-Smith and Ramdas betting p-value computed on person-level units; use fixed-sequence testing from the most conservative threshold and keep the largest rejected $\lambda$. With probability at least $1 - \epsilon$ over the calibration people, $R(\hat\lambda) \le \alpha$. Selective risk is not monotone in $\lambda$, which is why LTT (or the fixed-sequence form in Trust or Escalate) fits better than CRC; CRC can be used for the monotone joint risk $P(L = 1, s(x) \le \lambda)$ as a secondary analysis.

Label-free link to ground truth (a reasoned derivation, to be stated as a proposition): for the true score $y$, $|C(x) - y| \le |C(x) - \bar D_k(x)| + |\bar D_k(x) - y|$, and by convexity $|\bar D_k(x) - y| \le \frac{1}{k}\sum_{i} |D_i(x) - y|$. So on accepted inputs, with probability at least $1 - \alpha$ per input (and $1 - \epsilon$ over calibration), the compiled error is at most the average single-run deliberation error plus $\delta_t$. Certification needs only $k$ extra deliberation runs on calibration recordings, not clinician labels; labels are needed only to check the claim on the test set. This is what makes the method useful for general agents where ground truth is scarce.

Generations: in round $g$ the agent compiles a new program from trajectories on inputs that all earlier gates rejected, and certifies it on fresh calibration people passed through earlier gates. Spend $\epsilon_g = \epsilon \cdot 6 / (\pi^2 g^2)$ (or SGM's confirm-triggered harmonic spending) so that the chance that any generation's certificate fails is at most $\epsilon$; the system-level accepted risk is bounded by the sum of stage budgets, as in CompCRC.

### 5.3 The single most decisive experiment

On StaBLE, split participants once into compile (about 64 people), certify (about 64) and test (the 43 lab-pilot test people), keeping all three phones of a person in the same split. Run the SFT Qwen3-VL-8B agent $k = 5$ times per recording on compile and certify people. Mine recurring tool-call graphs per balance task, synthesize programs, learn gate scores on the compile split, and certify with LTT at $\alpha = 0.1$, $\epsilon = 0.1$ on the certify split. On test people, report for each method at matched cost: realized selective risk against $\bar D_5$, MAE against clinical labels on accepted and on all recordings, cost per recording (VLM tokens, GPU-seconds of tools, wall-clock), coverage (fraction compiled), intra-recording repeatability (ICC across reruns) and inter-device agreement (ICC across the three phones), SEM and MDC95. Repeat the split 200 times to estimate how often realized risk exceeds $\alpha$ (it should do so in at most about $\epsilon$ of splits). The decisive contrast is certified compilation against uncertified compilation (ASI-style admission and Auto-style familiarity guard) on the silent-error rate at the same coverage, and against self-consistency at the same cost on ICC.

### 5.4 Essential controls

- Person-disjoint compile, certify and test splits; tool versions frozen; GPU tools run with fixed seeds and deterministic kernels where available, so that the program's own variance is measured rather than assumed to be zero.
- Phone shift: certify on two phones and test on the third, with and without weighted conformal reweighting (density ratio estimated from unlabeled gate features), to test the exchangeability assumption directly.
- Grouping: person-level units (or one recording sampled per person per task, following Dunn et al.) so that clustered recordings do not inflate the effective sample size.
- Placebo gate: a random gate with the same acceptance rate, to show that the learned gate selects the inputs where the program is safe.
- Reference noise: compare certificates against $\bar D_1$, $\bar D_5$ and, where available, ground truth, to show how reference noise changes coverage.
- Cost accounting split into model tokens and tool compute, measured before the main study; if tool GPU time dominates, report the saving honestly.

### 5.5 Strongest baselines

- Always deliberate, single run, and self-consistency with $k$ runs (Wang et al., https://arxiv.org/abs/2203.11171).
- ASI programmatic skills (https://arxiv.org/abs/2504.06821) and AWM workflows (https://arxiv.org/abs/2409.07429), uncertified.
- Auto-style split-conformal familiarity guard with fallback (https://arxiv.org/abs/2607.04542), reimplemented on the same programs so that only the gate differs.
- Agentic Plan Caching (https://arxiv.org/abs/2506.14852).
- Distillation of the agent's own trajectories into weights (Agent Distillation, https://arxiv.org/abs/2505.17612), optionally with the same LTT gate on the distilled model's output, which isolates "program versus weights".
- Fixed pipeline: RTMPose plus TCN (lab pilot task-averaged MAE 0.119) and OpenCap Monocular (lab pilot 0.146), and the training-task-mean predictor (lab pilot 0.120). These are lab pilot figures from an internal account.
- Certified cascade with a fixed cheap model instead of a compiled program (Trust or Escalate style, https://arxiv.org/abs/2407.18370), which isolates the value of self-generation.

### 5.6 Models, data and environments

- Deliberating agents: Qwen3-VL-8B-Instruct (pilot, frozen and SFT) and Qwen3-VL-32B-Instruct as a scale check; both sizes are listed in the Qwen3-VL Technical Report (https://arxiv.org/abs/2511.21631). Program synthesis can use the same model or a Qwen3 coding or instruct model (Qwen3 Technical Report, https://arxiv.org/abs/2505.09388); exact checkpoint names should be fixed from the model cards before running.
- Biomechanics test bed: StaBLE (180 participants by 18 balance tasks by 3 phones; lab pilot used 171 people and 2,968 usable single-camera examples); BioCV (15 participants with synchronized cameras, markers and force plates) as a ground-truth check of the label-free bound for kinematic intermediates. Sample-size arithmetic matters here: with person-level units, a one-sided 90 percent Clopper-Pearson bound on selective risk is 0.086 for 2 violations in 60 accepted people and 0.101 for 3 in 64, so $\alpha = 0.1$ is certifiable only if the true violation rate is about 3 percent or lower; Hoeffding is looser (slack 0.134 at $n = 64$, $\epsilon = 0.1$). Pooling tasks with task-normalized tolerances, or certifying at $\alpha = 0.2$, may be needed.
- Second domain: AppWorld (Trivedi et al., ACL 2024, https://arxiv.org/abs/2407.18901), with 750 tasks over 9 apps and 457 APIs, scenario-based task variants that recur, and state-based unit tests that supply ground truth; TraceCompiler and AgentPRO already use it, which makes comparison direct. tau-bench and tau2-bench (https://arxiv.org/abs/2406.12045, https://arxiv.org/abs/2506.07982) provide repeated-trial reliability (pass^k) as the analogue of ICC. Here calibration sets can be large enough (hundreds of task instances) for tight certificates, which separates "the method fails" from "StaBLE is too small".

### 5.7 Metrics

Realized selective risk and its exceedance frequency over resampled splits; certified coverage at given $(\alpha, \epsilon)$; cost per input (tokens, GPU-seconds, wall-clock) and amortized cost including compilation; MAE on accepted, rejected and all inputs, against labels; silent-error rate (accepted and wrong against labels); ICC(2,1) and ICC(3,1) for reruns and across phones, reported with 95 percent intervals and interpreted with Koo and Li's bands applied to the interval; SEM $= \mathrm{SD}\sqrt{1 - \mathrm{ICC}}$ and MDC95 $= 1.96\sqrt{2}\,\mathrm{SEM}$; coverage growth over self-compilation generations; for AppWorld, task success, pass^k and collateral-damage rate.

### 5.8 Hypotheses worth pre-registering

1. Validity: realized selective risk exceeds $\alpha$ in at most about $\epsilon$ of resampled splits on person-disjoint data, and fails under phone shift unless reweighted.
2. Reliability: on accepted inputs, intra-recording ICC of the compiled path exceeds that of single-run deliberation by an amount predicted from the measured agent-sampling variance component (a quantitative prediction, since compilation should remove that component and nothing else).
3. Price of certification: at equal coverage, uncertified compilation (ASI-style and Auto-style) has a silent-error rate above $\alpha$ on new people, while certified compilation does not.
4. Program versus weights: at matched cost, distillation into weights reaches similar MAE but lower ICC than certified programs.
5. Generations: certified coverage increases over at least three self-compilation rounds while system-level risk stays under budget.

### 5.9 What would falsify the hypothesis

- The certificate is not valid in practice: realized risk on test people exceeds $\alpha$ far more often than $\epsilon$ of splits even without phone shift, showing that person clustering or residual-stream feedback breaks the assumptions.
- The certificate is valid but useless: certified coverage at $\alpha = 0.1$ is below about 20 percent at the point where uncertified compilation's silent-error rate is already under $\alpha$, so certification costs coverage and buys nothing.
- No reliability gain: compiled-path ICC on accepted inputs is no higher than self-consistency at equal cost, or the gain is far smaller than the agent-variance component predicts.
- Weights dominate: distilled weights with the same gate match the compiled path on cost, MAE and ICC, so the program form is not needed.
- The label-free bound fails: on BioCV or AppWorld, accepted compiled outputs are worse than single-run deliberation by more than $\delta_t$ at a rate above $\alpha$, which would mean $\bar D_k$ is a biased reference.

## 6. Key citations

| # | Reference | URL | Claim it supports | Verified |
|---|---|---|---|---|
| 1 | Jaber, J. and Jaber, O. Auto: The AGI Compiler. arXiv 2607.04542, 2026. | https://arxiv.org/abs/2607.04542 | Closest system: compile, split-conformal familiarity guard, fallback, recompile; parity not ground truth; 48.9 percent silent mislabeling under a loose guard. | yes |
| 2 | Wu, X. et al. SGM: A Statistical Godel Machine for Risk-Controlled Recursive Self-Modification. arXiv 2510.10232, 2025. | https://arxiv.org/abs/2510.10232 | Statistical tests replace Goedel proofs; global error budget over self-edits; global accept or reject only. | yes |
| 3 | Schmidhuber, J. Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements. arXiv cs/0309048, 2003 (rev. 2006). | https://arxiv.org/abs/cs/0309048 | Proof-based self-modification, the formal end of the spectrum. | yes |
| 4 | Zhang, J., Hu, S., Lu, C., Lange, R. and Clune, J. Darwin Godel Machine. arXiv 2505.22954, 2025. | https://arxiv.org/abs/2505.22954 | Empirical self-modification (SWE-bench 20.0 to 50.0 percent), the empirical end of the spectrum. | yes |
| 5 | Wang, W. et al. Huxley-Goedel Machine. arXiv 2510.21614, 2025 (ICLR 2026 per conference site). | https://arxiv.org/abs/2510.21614 | Clade-metaproductivity for choosing which self-modifications to expand; assumes repeatable evaluations. | yes |
| 6 | Angelopoulos, A. N., Bates, S., Candes, E. J., Jordan, M. I. and Lei, L. Learn then Test. Ann. Appl. Stat. 19(2), 2025; arXiv 2110.01052. | https://arxiv.org/abs/2110.01052 | Risk control as multiple testing over a parameter grid, valid for non-monotone risks; the certificate P08 uses. | yes |
| 7 | Angelopoulos, A. N., Bates, S., Fisch, A., Lei, L. and Schuster, T. Conformal Risk Control. ICLR 2024; arXiv 2208.02814. | https://arxiv.org/abs/2208.02814 | Expected monotone-loss control; secondary analysis of joint risk. | yes |
| 8 | Jung, J., Brahman, F. and Choi, Y. Trust or Escalate. ICLR 2025; arXiv 2407.18370. | https://arxiv.org/abs/2407.18370 | Fixed-sequence testing gives a high-probability guarantee for accepted outputs of a cheap tier with escalation. | yes |
| 9 | Overman, W. and Bayati, M. Conformal Arbitrage. NeurIPS 2025; arXiv 2506.00911. | https://arxiv.org/abs/2506.00911 | CRC-calibrated routing between a primary model and a guardian. | yes |
| 10 | Sun, Y. et al. Compositional Conformal Risk Control for Multi-Stage LLM Cascades. arXiv 2611.11114, 2026. | https://arxiv.org/abs/2611.11114 | Additive stage-wise risk budgets with a system-level finite-sample bound; template for multi-generation composition. | yes |
| 11 | Schroeder, L. G. et al. vCache: Verified Semantic Prompt Caching. arXiv 2502.03771 (ICLR 2026 accepted per arXiv). | https://arxiv.org/abs/2502.03771 | Learned per-entry reuse thresholds with user-defined error-rate guarantees, checked by occasionally calling the expensive path. | yes |
| 12 | Wang, Z. Z., Gandhi, A., Neubig, G. and Fried, D. Inducing Programmatic Skills for Agentic Tasks. COLM 2025; arXiv 2504.06821. | https://arxiv.org/abs/2504.06821 | Programs induced from trajectories with verification; gains over AWM on WebArena. | yes |
| 13 | Wang, Z. Z., Mao, J., Fried, D. and Neubig, G. Agent Workflow Memory. ICML 2025, PMLR 267. | https://proceedings.mlr.press/v267/wang25bx.html | Workflows induced from successful trajectories improve WebArena and Mind2Web. | yes |
| 14 | Zhang, Q., Wornow, M., Wan, G. and Olukotun, K. Agentic Plan Caching. NeurIPS 2025; arXiv 2506.14852. | https://arxiv.org/abs/2506.14852 | 50.31 percent cost reduction from reused plan templates without a guarantee. | yes |
| 15 | El Yadouni, S. and Li, G. TraceCompiler. arXiv 2608.02680, 2026. | https://arxiv.org/abs/2608.02680 | Trace-to-workflow compilation on AppWorld with residual LLM decisions; no net efficiency or accuracy guarantee. | yes |
| 16 | Kang, M. et al. Distilling LLM Agent into Small Models with Retrieval and Code Tools. NeurIPS 2025; arXiv 2505.17612. | https://arxiv.org/abs/2505.17612 | Distillation into weights, the main alternative to programs. | yes |
| 17 | Yu, P., Xu, J., Weston, J. and Kulikov, I. Distilling System 2 into System 1. arXiv 2407.06023, 2024. | https://arxiv.org/abs/2407.06023 | Amortizing deliberation into direct generation at lower cost. | yes |
| 18 | Mustahsan, Z. et al. Stochasticity in Agentic Evaluations: Quantifying Inconsistency with Intraclass Correlation. arXiv 2512.06710, 2025. | https://arxiv.org/abs/2512.06710 | ICC separates agent inconsistency from task difficulty; sub-agent replacement should be judged on ICC too. | yes |
| 19 | Yao, S., Shinn, N., Razavi, P. and Narasimhan, K. tau-bench. arXiv 2406.12045, 2024. | https://arxiv.org/abs/2406.12045 | pass^k shows large run-to-run inconsistency of tool agents. | yes |
| 20 | Atil, B. et al. Non-Determinism of "Deterministic" LLM Settings. arXiv 2408.04667, 2024. | https://arxiv.org/abs/2408.04667 | Up to 15 percent accuracy variation across runs in nominally deterministic settings. | yes |
| 21 | Tibshirani, R. J., Barber, R. F., Candes, E. J. and Ramdas, A. Conformal Prediction Under Covariate Shift. NeurIPS 2019; arXiv 1904.06019. | https://arxiv.org/abs/1904.06019 | Weighted conformal for phone or site shift. | yes |
| 22 | Dunn, R., Wasserman, L. and Ramdas, A. Distribution-Free Prediction Sets for Two-Layer Hierarchical Models. JASA (accepted per arXiv); arXiv 1809.07441. | https://arxiv.org/abs/1809.07441 | Conformal methods for grouped data (recordings nested in people). | yes |
| 23 | Angelopoulos, A. N. et al. Prediction-Powered Inference. arXiv 2301.09633, 2023. | https://arxiv.org/abs/2301.09633 | Combining a few labels with many model outputs for valid inference; option for tightening ground-truth claims. | yes |
| 24 | Koo, T. K. and Li, M. Y. A Guideline of Selecting and Reporting Intraclass Correlation Coefficients for Reliability Research. J Chiropr Med 15(2):155-163, 2016. doi:10.1016/j.jcm.2016.02.012. | https://pmc.ncbi.nlm.nih.gov/articles/PMC4913118/ | ICC forms, reporting, and interpretation bands applied to the confidence interval. | yes |
| 25 | Horsak, B., Kainz, H., Dumphart, B. et al. Repeatability and minimal detectable change including clothing effects for smartphone-based 3D markerless motion capture. J Biomech 175:112281, 2024. doi:10.1016/j.jbiomech.2024.112281. | https://www.sciencedirect.com/science/article/pii/S0021929024003592 | Test-retest RMSD, SEM and MDC for OpenCap; the reliability vocabulary P08 adopts. | partly (DOI redirects to this ScienceDirect record; the page itself returned 403, so full author list is from search listings) |
| 26 | Uhlrich, S. D. et al. OpenCap: Human movement dynamics from smartphone videos. PLOS Comput Biol 19(10):e1011462, 2023. | https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1011462 | Smartphone biomechanics pipeline used as a tool and baseline. | partly (seen in search results with DOI; page not fetched) |
| 27 | Trivedi, H. et al. AppWorld. ACL 2024; arXiv 2407.18901. | https://arxiv.org/abs/2407.18901 | Second-domain benchmark with 750 tasks and state-based unit tests. | yes |
| 28 | Bai, S. et al. Qwen3-VL Technical Report. arXiv 2511.21631, 2025. | https://arxiv.org/abs/2511.21631 | Model sizes 2B, 4B, 8B, 32B dense and 30B-A3B, 235B-A22B MoE. | yes |

Additional verified context papers (not in the core list): Compiled AI (https://arxiv.org/abs/2604.05150), ReaComp (https://arxiv.org/abs/2605.05485), Agent JIT Compilation (https://arxiv.org/abs/2605.21470), AgentPRO (https://arxiv.org/abs/2611.00628), AgentRR (https://arxiv.org/abs/2505.17716), SkillWeaver (https://arxiv.org/abs/2504.07079), Voyager (https://arxiv.org/abs/2305.16291), Skill-V (https://arxiv.org/abs/2610.11781), Conformal Cascade (https://arxiv.org/abs/2607.25018), SEA (https://arxiv.org/abs/2607.00871), Statistical limits of self-improving agents (https://arxiv.org/abs/2510.04399), ToolChain-CRC (https://arxiv.org/abs/2606.18467), role-stratified CRC for tool calls (https://arxiv.org/abs/2607.24343), Conformal Selective Acting (https://arxiv.org/abs/2605.20270), Conformal Policy Control (https://arxiv.org/abs/2603.02196), KnowNo (https://proceedings.mlr.press/v229/ren23a.html), self-consistency (https://arxiv.org/abs/2203.11171), tau2-bench (https://arxiv.org/abs/2506.07982), Qwen3 Technical Report (https://arxiv.org/abs/2505.09388).

## 7. Caveats on the evidence

- Many of the closest works (Auto, TraceCompiler, Conformal Cascade, CompCRC, SEA, Skill-V) are 2026 arXiv preprints without peer review; their numbers are the authors' own.
- Auto's guard details (lexical trigram similarity, alpha values, reference model) come from its HTML full text read in this session; the abstract alone does not state them.
- The derivation in Section 5.2 linking the label-free certificate to ground-truth error is a reasoned argument written for this report, not a published result; it should be checked and stated as a proposition with its conditions (independence of the $k$ runs, and the per-input probability statement versus the selective-risk statement).
- The Clopper-Pearson and Hoeffding figures in Section 5.6 were computed in this session for illustration of sample-size limits; they assume person-level independence.
