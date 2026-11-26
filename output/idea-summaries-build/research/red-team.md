# Red-team review of directions P05 to P08

Status: COMPLETE (2026-11-24).

Role taken: a demanding senior area chair at ICML, NeurIPS or ICLR who has read the 2025 to 2026 self-improvement literature and is looking for a reason to reject. Scores use a 1 to 5 scale, where 5 means "a reviewer cannot name a paper that already answers this question, and the answer would change how people build agents." Every paper cited below was checked by fetching its arXiv abstract page (or the HTML full text where a specific number mattered) in this session, unless it is marked UNVERIFIED. Numbers quoted from a paper come from its abstract unless the text says otherwise.

## Summary table

| Idea | Novelty | Significance | Verdict |
|---|---|---|---|
| P05 Evolvability | 4.0 | 3.5 | Keep, but rebuild around one measurable quantity and matched-length controls |
| P06 Trace leakage | 3.5 | 4.0 | Keep; becomes the strongest of the four if the trace channel is separated from the winner's curse and tied to an information bound |
| P07 Self-designed observations | 3.5 | 3.5 | Keep, but make cross-reader transfer the primary outcome and predict it from a perceptual profile |
| P08 Certified self-compilation | 2.5 | 3.0 | Replace. The framing and the mechanism both exist in 2025 to 2026 work, and the guarantee is close to vacuous at this sample size |

Overall: keep P05, P06 and P07 with the upgrades below, and replace P08 with a direction on how label-free agreement rewards push an agent toward instruments whose errors are correlated (section "Replacement for P08").

---

## P05 Evolvability

Question as posed: if a harness's input-output behavior is held fixed, do structural properties of its code (modularity, logged intermediate values, exposed parameters, executable checks, identifier naming) causally change how far an LLM-driven self-improvement loop can take it under a fixed evaluation budget? The second half uses structure to predict metaproductivity for parent selection and tests a "refactor first, then optimize" split of the budget.

### Searches aimed at disproving novelty

1. "code structure modularity affects LLM self-improvement agent evolvability refactoring" and a follow-up on seed-agent sensitivity in DGM-style loops.
2. "semantics-preserving refactoring identifier naming effect on LLM code repair success rate controlled experiment", plus a search on "metaproductivity" prediction.

### Closest work found

- Darwin Goedel Machine (Zhang, Hu, Lu, Lange, Clune; arXiv 2505.22954). Keeps an archive of self-modified coding agents and validates each change on benchmarks; reports SWE-bench 20.0% to 50.0% and Polyglot 14.2% to 30.7%. Treats the agent's code as the thing being edited and never varies its structure while holding behavior fixed.
- Huxley-Goedel Machine (Wang, Piekos, Nanbo, Laakom, Chen, Ostaszewski, Zhuge, Schmidhuber; arXiv 2510.21614, ICLR 2026). Defines clade metaproductivity (CMP), the aggregate success of an agent's descendants, and the metaproductivity-performance mismatch. CMP is estimated from descendant outcomes; the abstract says nothing about predicting it from code features. This is the baseline P05 must beat on parent selection.
- Code for Machines, Not Just Humans (Borg, Hagatulah, Tornhill, Soderberg; arXiv 2601.02200, FORGE 2026). LLMs refactored 5,000 Python files; human-oriented CodeHealth was associated with semantic preservation after AI refactoring. The design is observational, the task is a single refactoring rather than a multi-step improvement loop, and the code is small competitive-programming files. A secondary summary of the full text says one frontier agent's success barely varied with CodeHealth; I did not confirm that on the abstract page.
- When Names Disappear (Le et al.; arXiv 2510.03178). Removing identifier names with behavior-preserving obfuscation degrades summarization strongly and execution-prediction tasks measurably. Shows that naming is a real causal channel for LLMs reading code, though not for improvement loops.
- Mutation Without Variation (Gurkan, Stonedahl, Wilensky; arXiv 2606.05408). Without selection, LLM mutation converges to a small set of program structures: in 87% of mutation chains, over 93% of mutations revisit a structure already seen. Relevant because it suggests the starting structure may set the attractor the loop falls into.
- A Self-Improving Coding Agent (Robeyns, Szummer, Aitchison; arXiv 2504.15228), Mendel Goedel Machine (Liu, Liu, Yan, Tresp, Ma; arXiv 2608.07645) and the survey Self-Evolving Coding Agents (Zhou et al.; arXiv 2608.03392). None varies harness structure at fixed behavior. The survey lists the agent's framework and topology as things that can be evolved, which is different from asking whether they make evolution easier.
- "Do Self-Improving Coding Agents Beat Textbook Baselines?" (Tomar; Zenodo DOI 10.5281/zenodo.23720889, repository github.com/tejasvi/self-improving-agents-textbook-baselines). The repository page was fetched; it describes an engineered-seed comparison against a DGM port but does not state the result. Unreviewed. Relevant as evidence that people are starting to ask how much the seed matters.

### Scores

Novelty 4.0. I found no paper that applies behavior-preserving transformations to a harness and then measures the downstream self-improvement trajectory. The causal design with differential testing is the novel part. It loses a point because "clean code helps LLMs" is folk wisdom that Borg et al. already support observationally, and because HGM already owns the idea that score is a poor guide to metaproductivity.

Significance 3.5. If structure matters, everyone running DGM, HGM, AlphaEvolve-style or Meta-Harness loops would want to refactor their seed and to select parents on structure. If it does not matter at frontier-optimizer strength, the result is a useful negative but a weak paper.

### Strongest objection

The effect will be confounded with context length and swamped by run-to-run variance. Behavior-preserving transformations change how many tokens the harness occupies and how much of it fits in the optimizer's context, so a "modularity" effect may be a "shorter files" effect. Separately, self-improvement runs are noisy: Ye et al. (arXiv 2608.18066) show that single-run results in self-improving agents mislead and that task order alone moves outcomes by large margins. A five-factor factorial with a stochastic optimizer, run under a fixed budget, will need many seeds per cell to detect anything, and each seed costs a full improvement run with expensive tools inside.

### Change that would most raise the score

Replace the five-factor sweep with one mechanistic quantity, and test whether it mediates the structure effect and predicts long-run outcomes.

Define the single-edit success profile of a (harness, optimizer) pair: over a fixed suite of a few hundred one-step improvement requests, the probability that a single proposed edit is behavior-correct and improves held-out error, and the size of the improvement when it does. This costs a small fraction of a full loop. Then make three claims that can each fail. First, randomized behavior-preserving transformations shift this profile, with token count matched across arms (pad or compress so every variant has the same length). Second, the profile measured early predicts the outcome of a full 50-iteration loop across structures and across two optimizers of different strength, better than the parent's score (DGM) and better than CMP estimated from the same number of evaluations (HGM). Third, a simple model of the loop as accept-if-better search with acceptance probability given by the profile predicts the budget at which refactoring first pays off, which gives the refactor-first split a derived value instead of a tuned one.

The surprising prediction worth registering in advance: structure matters most for weaker optimizers and small budgets, so the curves for weak and strong optimizers cross. A crossover is far more convincing than a main effect, and it is what practitioners need to know.

### Is the biomechanics test bed load-bearing?

Partly. A measurement harness has a natural modular decomposition (pose, filtering, center-of-mass estimate, feature, score), exposed parameters with physical meaning (filter cutoffs, event thresholds), and intermediate values in physical units, so the structural factors are realistic rather than contrived. Expensive tools (OpenCap Monocular, OpenSim) make the evaluation budget bind, which is where the question matters. But the causal question does not need biomechanics. To make the domain load-bearing, add one factor that only a scientific harness has: names and logs that carry physical units and meaning (for example a variable named for anterior-posterior sway in millimetres versus an opaque name). To show generality, replicate the core contrast on one public non-biomechanics harness, such as a Meta-Harness classification task.

---

## P06 Trace leakage

Question as posed: when a reflective optimizer reads per-example execution traces from the same examples it uses to select candidates, how much of the measured improvement fails to transfer to new people, how does the gap scale with dev-set size, iterations and feedback richness, and which protocol recovers honest improvement?

### Searches aimed at disproving novelty

1. "overfitting validation set prompt optimization GEPA reflective traces generalization gap holdout".
2. "adaptive data analysis LLM agent optimization benchmark overfitting reusable holdout prompt search", plus follow-ups on RRSI, on permuted-label tests for prompt optimizers, and on the winner's curse in self-improvement loops.

### Closest work found

- What Fits (Into Few Tokens) Doesn't Overfit (Bertran, Roth, Wu; arXiv 2606.11045). LLM research agents search for models using a validation set under two bottlenecks: a reproducer must match the explorer from a very short prompt, and the explorer receives one bit per submission (does it beat the running best). Across 8 datasets the bottlenecks barely hurt, which the authors explain by description length: good strategies are compressible, so benchmark reuse rarely overfits. When overfitting was induced on purpose, it did not survive compression. This is the paper P06 must engage directly, and it uses a Ladder-style channel.
- The Winner's Curse in LLM Self-Improvement Loops (Hu, Tang; arXiv 2610.09239). Treats keep-if-better as selection under noise. In a pre-registered study, selection-set scores overstated held-out accuracy by 13 to 20 points with 16 selection items and by 1 to 5 points with 256. Scoring the start and end prompts on 64 unused items removes the average bias. The abstract does not separate trace feedback from score noise.
- RRSI (Xia et al., Google; arXiv 2609.24972). Shows harness evolution memorizes training tasks and adds regularizers to the proposer (annealed edit budget, exploration bonus) and selector (critic, pruner). Reports gains on the evolve split and on five out-of-distribution benchmarks. A regularization method, with no channel-by-channel accounting.
- TextReg (Fu et al.; arXiv 2605.21318). Names "prompt distributional overfitting": optimized prompts grow and accumulate sample-specific rules. Proposes regularized textual gradients and reports out-of-distribution gains over TextGrad and REVOLVE.
- Meta-Harness (Lee, Nair, Zhang, Lee, Khattab, Finn; arXiv 2603.28052). The proposer reads source code, scores and raw execution traces of all prior candidates through a filesystem. Its interface ablation (Table 3 in the HTML full text) reports median accuracy 34.6 with scores only, 34.9 with scores plus summaries and 50.0 with full traces. The table does not label the split; it reads as search-set accuracy. The paper holds out a test set and checks out-of-distribution datasets, and for TerminalBench-2 it uses the same 89 tasks for search and evaluation with manual and regex audits for leakage.
- GEPA (Agrawal et al.; arXiv 2507.19457, ICLR 2026). Reflects in natural language on sampled trajectories and selects from a Pareto frontier of its own attempts; search results indicate the returned candidate is the best on the validation set used for selection.
- Statistical foundations: the reusable holdout and its information-theoretic basis (Dwork, Feldman, Hardt, Pitassi, Reingold, Roth; arXiv 1506.02629), the Ladder (Blum, Hardt; arXiv 1502.04585), mutual-information bounds on exploration bias (Russo, Zou; arXiv 1511.05219) and on generalization (Xu, Raginsky; arXiv 1705.07809), and the random-label memorization test (Zhang, Bengio, Hardt, Recht, Vinyals; arXiv 1611.03530).

### Scores

Novelty 3.5. That reflective and evolutionary optimizers overfit their selection set is now documented from three angles (Hu and Tang on score noise, RRSI and TextReg on regularization, Bertran, Roth and Wu on why it is usually small). What nobody has done is isolate the trace channel: how much extra information about the selection labels flows through per-example traces, beyond what the winner's curse already explains, and whether that extra flow creates gains that do not transfer. Meta-Harness shows traces are where the search-set gain comes from; nobody has checked whether that gain survives on new people at small n.

Significance 4.0. Every trace-reading optimizer (GEPA, Meta-Harness, ACE, DGM-style loops) reports improvements that a practitioner then deploys. A result saying "with fewer than N examples and per-example traces, a measured share of your improvement is memorization, and here is the protocol that removes it" would be cited and adopted. It is a measurement-science contribution, which some reviewers rate lower than a method, so it needs a theoretical anchor.

### Strongest objection

This is ordinary adaptive overfitting, already characterized. Hu and Tang measured the overstatement and its dependence on selection-set size; Bertran, Roth and Wu argue it is small in practice; RRSI and TextReg already regularize it; and the major papers already report held-out test numbers. Without a clean separation of what traces add beyond score noise, the paper reduces to "use a held-out set," which a reviewer will call a hygiene note.

### Change that would most raise the score

Turn P06 into a direct, falsifiable test of the compression explanation, with a decomposition that only P06 can produce.

Run the same optimizer at matched evaluation budget under a ladder of feedback channels: scores only, one-bit Ladder feedback, traces aggregated over k examples, and per-example traces. Run every channel twice, once on true labels and once on permuted labels. On permuted labels any dev-set improvement is memorization by construction, so the permuted run measures each channel's capacity to leak, separately from the winner's curse (which the scores-only permuted run measures). The held-out gap on true labels then splits into a selection-noise part and a trace part.

Pair this with a bound that can be proved: following Russo and Zou and Xu and Raginsky, the expected gap between dev and held-out error is controlled by the mutual information between the selected harness and the dev labels, and that information is at most the number of bits the feedback channel carries per iteration times the number of iterations. A scalar score carries a few bits per iteration, a ladder signal one bit, and a per-example trace carries information about every example's label, so the bound predicts that the trace part of the gap grows with iterations and shrinks roughly with n.

The prediction that sets P06 against Bertran, Roth and Wu: compression keeps score-fed loops honest because the optimizer can only learn compressible strategies, but per-example traces let it write example-specific rules, so the description length of the accepted harness diffs should grow with iterations under trace feedback and stay flat under score or ladder feedback, and that description length should predict the held-out gap. If this holds, P06 explains when the compression argument breaks. If it fails, P06 extends their result to trace-reading optimizers, which is still publishable.

### Is the biomechanics test bed load-bearing?

Yes, more than for any other idea here. The dev sets are small in people (171 people in the pilot, 43 test people), and each person contributes up to 18 tasks times 3 phones, so splitting by recording instead of by person leaks identity through traces. Traces are long numeric time series that can carry person-specific signatures. Expensive tools cap how many examples the optimizer can afford to evaluate, which keeps n small in the regime the bound cares about. Labels are continuous clinical scores, and the project already knows of one leakage source (StaBLE normalizes features with the minimum and maximum over all 180 people). To make the domain load-bearing in the paper: report the gap as a function of distinct people rather than recordings; use the three phones of the same trial to estimate the noise floor; and express the overfit gain relative to the clinical minimal detectable change, so the reader learns whether the leaked improvement is clinically meaningful.

---

## P07 Self-designed observations

Question as posed: when a VLM agent receives numeric tool outputs (keypoint series, center-of-mass sway, joint angles), which encodings give accurate decisions per token, and can the agent evolve its own rendering code so the gains transfer to new tasks, other VLMs and human readers rather than exploiting one model's quirks? Includes a Cleveland-McGill battery, a pixel-oracle control, evolutionary search over plotting code, cross-model and human transfer, and a co-adaptation drift test.

### Searches aimed at disproving novelty

1. "vision language models graphical perception Cleveland McGill elementary perceptual tasks benchmark".
2. "time series as plots versus text numbers multimodal LLM reasoning token efficiency visualization", plus searches on LLMs evolving rendering code for VLM agents and on chart designs that help VLMs.

### Closest work found

- Plots Unlock Time-Series Understanding in Multimodal Models (Daswani et al.; arXiv 2410.02637). Plots instead of numeric text give up to 120% better zero-shot synthetic performance, up to 150% on consumer-health tasks including fall detection and activity recognition, and up to 90% lower API cost, across GPT and Gemini.
- A Picture is Worth A Thousand Numbers (Liu, Liu, Prakash; arXiv 2411.06018, NAACL 2025). TimerBed plus VL-Time, a prompt-based method using visualized data; about 140% average improvement and about 99% token reduction. Search summaries describe an LLM planning the visualization method; the abstract does not confirm whether the model designs the plot.
- Evaluating Graphical Perception with Multimodal LLMs (Nguyen, Maeda, Geshvadi, Haehn; arXiv 2504.04221) and Understanding Graphical Perception in Data Visualization through Zero-shot Prompting of VLMs (Guo, Kang, Shah, Pfister, Varma; arXiv 2411.00257). Both reproduce Cleveland-McGill tasks with VLMs. Models beat humans on some tasks and not others; accuracy shifts with style changes (fill color, bar contiguity) at fixed data. So the "battery" exists in two forms.
- LLM Agents Can See Code Repositories (Ma et al.; arXiv 2606.14061, ASE 2026). For coding agents, vision-only repository views hurt, while adding rendered graphs to text cut input tokens by up to 26% at equal or better accuracy. Closest agentic analog: rendered observations as a supplementary channel.
- SWE-agent (Yang et al.; arXiv 2405.15793). Agent-computer interface design changes agent performance; the interface was hand-designed.
- Visual Sketchpad (Hu et al.; arXiv 2406.09403, NeurIPS 2024). Multimodal models draw on a canvas as intermediate reasoning; the drawing tools are fixed.
- Countering Language Drift via Visual Grounding (Lee, Cho, Kiela; arXiv 1909.04499, EMNLP 2019). Agents trained on task reward drift away from human-readable language; this is the precedent for the co-adaptation test, transposed from text to a visual channel.

### Scores

Novelty 3.5. Text versus plot is settled at a coarse level (Daswani; Liu), and VLM graphical perception has two studies. The new parts are evolutionary search over the renderer judged on downstream decisions, the information-matched pixel oracle, and the drift test when reader and renderer co-adapt. A reviewer will see the first part as harness optimization applied to one function unless transfer is the headline.

Significance 3.5. Every agent that turns numbers into something a model reads (dashboards, logs, sensor data, code graphs) faces this design choice, so a general answer about whether machine-optimized encodings are universal or private would matter. The per-token accuracy framing is useful but incremental on its own.

### Strongest objection

Plots beat numbers is already known, and evolution will find the OCR shortcut. A renderer optimized for a VLM will learn to print the relevant numbers into the image as large text, which makes the plot-versus-text contrast meaningless and turns "self-designed observations" into "self-designed number formatting." The comparison is also confounded by resolution and visual-token budget, since a plot can discard precision that text keeps.

### Change that would most raise the score

Make cross-reader transfer the primary outcome and predict it before running evolution.

Run the Cleveland-McGill battery on each VLM reader and on a panel of human readers. This gives each reader a perceptual profile: how accurately it decodes position on a common scale, length, slope, angle, area and color intensity. Then pre-register two predictions. First, a renderer evolved against reader A transfers to reader B in proportion to the similarity of their profiles, so the battery predicts transfer a priori. Second, evolution against a VLM drifts toward encodings where that VLM's profile beats the human one and away from encodings where humans read better, so human readability falls by an amount the profiles predict. Ban in-image text in one arm so the OCR shortcut is measured rather than assumed, and keep the pixel oracle to cap the information available. If the predictions hold, P07 gives a theory of machine graphical perception that explains when optimized interfaces stay human-legible; the co-adaptation drift test then becomes the extreme case of the second prediction.

### Is the biomechanics test bed load-bearing?

Yes. The agent's evidence is numeric time series, and the clinical decisions map onto elementary perceptual judgments: sway amplitude is position on a common scale, drift is slope, a sway ellipse is area, and event timing is position along time. BioCV's force plates and markers give ground-truth center of pressure and joint kinematics, which is what makes an information-matched pixel oracle possible. Clinicians and trained raters are a natural human-reader panel with real stakes in legibility. To make the domain carry the paper, choose the downstream decisions so that each one depends mainly on one perceptual type, which lets the battery profile predict task-level transfer.

---

## P08 Certified self-compilation

Question as posed: can a tool-using agent turn recurring tool-call trajectories into programs plus learned validity gates, so that on new people it is cheaper, more repeatable (ICC, minimal detectable change) and, with a Learn-then-Test or conformal risk control guarantee, no less accurate than deliberation on the inputs it compiles? Framed as statistically certified self-modification between the proof-based Goedel machine and the empirical Darwin Goedel Machine.

### Searches aimed at disproving novelty

1. "compile LLM agent trajectories into executable programs replace LLM calls record and replay agent verification fallback", plus "agentic plan caching".
2. "statistically certified self-modification agent hypothesis test accept self-improvement guarantee Darwin Godel Machine", plus "conformal risk control certify LLM agent cascade defer".

### Closest work found

- SGM: A Statistical Goedel Machine for Risk-Controlled Recursive Self-Modification (Wu et al.; arXiv 2510.10232). Replaces formal proofs with statistical confidence tests (e-values, Hoeffding bounds); admits a modification only when superiority is certified, with a global error budget across edits and a budget-spending rule. This is P08's framing, already published.
- On the Statistical Limits of Self-Improving Agents (Wang, Dorchen, Jin; arXiv 2510.04399, TMLR 2026). PAC learnability survives self-modification only if the reachable policy family stays capacity-bounded; proposes a two-gate guardrail (validation improvement plus a capacity cap).
- Auto: The AGI Compiler (Jaber, Jaber; arXiv 2607.04542). Records live agent behavior, extracts spans that behave deterministically into verified programs or distilled models behind guards described as conformally calibrated, and falls back to the reference agent when a guard trips. On its own benchmark, 87.1% of 560 spans were deterministic in this sense, marginal cost fell from 59 to 2 micro-dollars per item at 96.9% parity, and a loose guard mislabeled 48.9% of compiled answers. This is P08's mechanism, already published.
- SkillCache, "How Much Skill Orchestration Can LLM Agents Compile Away?" (Ni et al.; arXiv 2611.10022). Compiles one invocation into a parameterized capsule, replays it before reuse, and returns control to the model when needed; 81% and 74% token cuts at comparable reward, with cross-model transfer.
- TraceCompiler (El Yadouni, Li; arXiv 2608.02680). Compiles noisy agent traces into mostly deterministic workflows with procedural gates and refuses to compile underdetermined irreversible steps; no statistical guarantee.
- Agentic Plan Caching (Zhang, Wornow, Wan, Olukotun; arXiv 2506.14852, NeurIPS 2025), Agent Workflow Memory (Wang, Mao, Fried, Neubig; arXiv 2409.07429) and Agent Skill Induction (Wang, Gandhi, Neubig, Fried; arXiv 2504.06821), the last with programmatic verification of induced skills.
- Certified deferral: Learn then Test (Angelopoulos, Bates, Candes, Jordan, Lei; arXiv 2110.01052), Conformal Risk Control (Angelopoulos, Bates, Fisch, Lei, Schuster; arXiv 2208.02814), CompCRC for multi-stage cascades (Sun et al.; arXiv 2611.11114) and Conformal Cascade (Dou, Lian, Li; arXiv 2607.25018), whose guarantee weakens as 1 minus K alpha across K tiers.

### Scores

Novelty 2.5. The framing is SGM's. Compiling agent behavior into programs with gates and fallback is Auto's, and SkillCache, TraceCompiler and APC cover the cost side. Certified deferral between a cheap and an expensive path is CompCRC and Conformal Cascade. What remains is the reliability objective (ICC, minimal detectable change) and a non-inferiority guarantee against a stochastic deliberating agent on continuous outputs, which is a narrow increment.

Significance 3.0. Cost and repeatability matter in clinical deployment, but the general agent community already has these tools, so the paper would read as an application.

### Strongest objection

Already done, and the guarantee is vacuous here. SGM and Auto together cover certified self-modification and certified compilation. In this setting the calibration pool is a few dozen people, and Learn-then-Test with roughly 40 to 80 exchangeable units gives a risk bound too loose to admit most compiled programs at a clinically useful tolerance. Exchangeability also fails along the axes that matter (phone placement, task, site), and the 18 tasks times 3 phones per person are not independent units, so the honest effective n is the number of people.

### Change that would most raise the score

If the team keeps P08, pivot it to reliability: certify, with person-clustered calibration, that the compiled path has a minimal detectable change no larger than deliberation's, and compare head-to-head against Auto's guards and SGM's acceptance test. That is the one claim neither paper makes. Even so, I expect a ceiling near 3.5, and I recommend replacing it.

### Is the biomechanics test bed load-bearing?

Moderately. ICC and minimal detectable change are clinical standards, the 18 tasks produce recurring trajectories, three phones per trial give natural repeated measurements, and OpenCap and OpenSim are slow enough that compilation saves real money. The same domain also exposes the weakness: n is too small for a tight finite-sample guarantee.

### Overlap with earlier project ideas

P08 overlaps more with the explored list than any other idea. Compiled programs are measurement programs (held-out-task transfer, library-constrained measurement code), and deciding which inputs need the expensive deliberating path resembles selecting which recordings to re-execute after a harness edit and running calibration trials when a tool is updated. This is a second reason to replace it.

---

## Overlap among P05 to P08 and with earlier ideas

### Among the four

- P05 and P06 collide on logging. P05 treats logged intermediate values as a structural factor; P06 treats trace richness as a feedback channel. Logging more intermediates is a richer trace, so a P05 "logging helps evolvability" result measured on the dev set could be P06 leakage. Keep them distinct by assigning the variable once: P06 varies the feedback channel with harness structure fixed, and P05 varies structure with the feedback channel fixed (aggregated traces) and always reports held-out-person results under P06's protocol. The P06 permuted-label test should be run on P05's logging arm as a check.
- P07 is itself a self-improvement loop (it evolves rendering code), so its gains on 43 test people are exposed to the same leakage P06 measures. Use P06's grouped splits and reusable-holdout protocol in P07, and state that P07 inherits P06's evaluation rules rather than studying them.
- P07's co-adaptation drift and P06's memorization are both forms of a loop fitting something it should not (the reader versus the dev labels). Keep P07 on the reader axis: the dev labels are fixed, and the question is legibility to other readers.
- P08 and P06 share statistical machinery (held-out certification), which is fine; the replacement below removes this overlap anyway.

### With previously explored ideas

- P05's "executable checks" factor overlaps with known-answer checks and physical-response checks. Define P05's checks as generic assertions (array shapes, units, value ranges, monotonic time stamps), and if the domain checks are included, cite them as one level of the factor rather than as a contribution.
- P05's differential testing for behavior preservation reuses the re-execution machinery from the harness-edit idea; reuse the code and say so, since the question differs.
- P06 against held-out-task transfer: P06 must stay on the person axis (new people, same tasks), so the two never measure the same gap.
- P06 against measurement-grounded per-feature rewards and privileged teacher demonstrations: no overlap, since P06 studies the optimizer's feedback channel, not the training signal.
- P07 against the feature-versus-direct-prediction study and the pilot's feature-prompted Qwen (MAE 0.179): those vary which information the model gets; P07 must hold the information fixed (the pixel oracle and information-matched text) and vary only its encoding.
- P07 against tool world models: none.

---

## Replacement for P08

### Instrument collusion: do label-free agreement rewards teach agents to pick instruments that fail together?

Research question. When a tool-using agent improves itself without labels by rewarding agreement among its own measurements of the same event (three phones filming one trial, two pose estimators, repeated runs), does it learn to route those measurements through shared processing so their errors become correlated, raising agreement while accuracy stays flat or worsens? And can a small labeled anchor set that bounds the residual correlation between instruments turn agreement into a reward whose optimum is the true value?

Why it matters. Labels are the bottleneck for self-improvement, and agreement is the most common substitute: majority voting in TTRL, paraphrase consistency in Self-Harmony, peer rewards in Co-RL, panels of LLM judges, multi-retriever RAG and multi-sensor robots all reward views for agreeing. All of these assume the views' errors are independent enough. In an agent, the views are not fixed: the agent chooses which tools to call and how to process their outputs, so it can buy agreement by making its instruments share a failure mode (the same pose model for every phone, heavy smoothing, ignoring view-specific information). That is a Goodhart effect on tool selection itself, and nobody has measured it.

Why it is novel. The consensus-trap literature treats the views as given. CoVerRL (Pan et al.; arXiv 2603.17775) shows majority-vote pseudo-labels collapse diversity and lock in confident errors, and adds a co-evolving verifier. Co-RL (Yang et al.; arXiv 2608.17253) reduces correlated errors by training models from different families, but the abstract describes peer diversity as a design choice, not something the agents select. Self-Harmony (Wang et al.; arXiv 2511.01191, ICLR 2026) uses agreement across paraphrases, and TTRL (Zuo et al.; arXiv 2504.16084) uses majority vote. EpipolarPose (Kocabas, Karagoz, Akbas; arXiv 1903.02330, CVPR 2019) self-supervises 3D pose from multi-view geometry with a fixed pipeline. Co-training theory (Blum and Mitchell, COLT 1998, DOI 10.1145/279943.279962; UNVERIFIED, the ACM page returned 403) requires conditionally independent views. None of these studies the case where the learner controls the correlation between its views, and reasoning benchmarks cannot measure that correlation directly because they lack a physical ground truth for each view's error.

Theory that can be proved. Write each instrument's reading as truth plus a common-mode error (set by the processing path the agent chose, shared across instruments that use it) plus an independent error. Expected disagreement depends only on the independent part, while accuracy of the averaged reading depends on the common-mode variance plus the independent variance divided by the number of instruments. So any change in tool selection that trades independent error for common-mode error raises the agreement reward, and it lowers accuracy whenever the common-mode variance it adds exceeds the independent variance it removes divided by the number of instruments. The result gives a closed-form condition for when agreement-trained and accuracy-trained agents diverge, and a second result bounding the excess error of an agent trained on agreement restricted to instrument pairs whose residual correlation, estimated on n anchor people, falls below a threshold.

Surprising prediction. Under agreement-only reward, the agent converges to sending all three phones through one pose model with aggressive temporal smoothing, so test-retest ICC across phones rises while MAE against force-plate and marker ground truth worsens. Reliability, the clinical property people would cite as evidence the agent improved, becomes the symptom of the failure.

Decisive experiments. On BioCV (synchronized cameras, markers, force plates), measure each tool path's common-mode and independent error directly against ground truth; train or evolve the agent's tool-selection policy under accuracy reward, agreement reward, agreement restricted to certified-independent pairs, and an anchor-calibrated ICC reward; track the error correlation of the chosen instruments over training. Then transfer the finding outside biomechanics with an LLM-judge panel and a multi-retriever question-answering agent, where the agent picks which judges or retrievers to consult.

Biomechanics as an asset. This is the most load-bearing use of the test bed in the portfolio: three phones per StaBLE trial and BioCV's synchronized cameras are physically independent instruments, the tool library offers shared versus separate processing paths (RTMPose, OpenCap Monocular, CoTracker3, Video Depth Anything), and ground truth lets the error be split into common-mode and independent parts, which no text benchmark allows. P08's best idea, reliability as an objective, survives here as one of the reward arms.

Overlap and how to keep it distinct. The nearest explored idea is learning with biased software references that share processing steps. That idea holds the references fixed and asks what a supervised learner inherits; the replacement uses no reference labels beyond the small anchor set and asks whether the agent will create the shared processing itself under a label-free reward. Its outcome is the agent's tool-selection behavior, not the bias of a learned model. It also differs from known-answer and physical-response checks, which verify single outputs, because the signal here is agreement between instruments. It does not overlap with P05 to P07.

Provisional scores. Novelty 4.0 to 4.5, significance 4.0 to 4.5, conditional on proving the divergence condition and on showing the effect outside biomechanics.

---

## Overall verdict

Keep P05, P06 and P07, each with the single upgrade named above. Replace P08 with the instrument-collusion direction.

Ranked by expected score after upgrades: P06 (the information bound and the permuted-label decomposition make it a clean test of a 2026 theory, so it can reach 4.5), the replacement (a new Goodhart effect on tool selection with a provable condition and a biomechanics test bed nobody else has), P07 (if the perceptual-profile prediction holds) and P05 (strong question, but the hardest to power).

Cross-cutting requirements a reviewer will check in all four: split by person and report effective n as the number of people; run several seeds per arm, since self-improvement runs are noisy (Ye et al., arXiv 2608.18066; Hu and Tang, arXiv 2610.09239); report held-out gains with uncertainty; and include one non-biomechanics replication so the general claim is earned.

---

## Verified references

All fetched in this session on the arXiv abstract page unless noted.

Self-improvement loops and parent selection
- Zhang, Hu, Lu, Lange, Clune. Darwin Goedel Machine. https://arxiv.org/abs/2505.22954
- Wang, Piekos, Nanbo, Laakom, Chen, Ostaszewski, Zhuge, Schmidhuber. Huxley-Goedel Machine. https://arxiv.org/abs/2510.21614
- Robeyns, Szummer, Aitchison. A Self-Improving Coding Agent. https://arxiv.org/abs/2504.15228
- Liu, Liu, Yan, Tresp, Ma. Mendel Goedel Machine. https://arxiv.org/abs/2608.07645
- Zhou et al. Self-Evolving Coding Agents (survey). https://arxiv.org/abs/2608.03392
- Gurkan, Stonedahl, Wilensky. Mutation Without Variation. https://arxiv.org/abs/2606.05408
- Ye, Li, Pruksachatkun, Zhang, Wu. On the Fragility of Self-Improving Agents. https://arxiv.org/abs/2608.18066
- Tomar. Do Self-Improving Coding Agents Beat Textbook Baselines? Repository page fetched: https://github.com/tejasvi/self-improving-agents-textbook-baselines (paper DOI 10.5281/zenodo.23720889 not fetched; results not seen)

Code structure and LLMs
- Borg, Hagatulah, Tornhill, Soderberg. Code for Machines, Not Just Humans. https://arxiv.org/abs/2601.02200
- Le et al. When Names Disappear. https://arxiv.org/abs/2510.03178

Optimizer overfitting and adaptive data analysis
- Bertran, Roth, Wu. What Fits (Into Few Tokens) Doesn't Overfit. https://arxiv.org/abs/2606.11045
- Hu, Tang. The Winner's Curse in LLM Self-Improvement Loops. https://arxiv.org/abs/2610.09239
- Xia et al. RRSI: Regularized Recursive Self-Improvement of Agent Harnesses. https://arxiv.org/abs/2609.24972
- Fu et al. TextReg. https://arxiv.org/abs/2605.21318
- Lee, Nair, Zhang, Lee, Khattab, Finn. Meta-Harness. https://arxiv.org/abs/2603.28052 (Table 3 numbers read from https://arxiv.org/html/2603.28052v1)
- Agrawal et al. GEPA. https://arxiv.org/abs/2507.19457
- Dwork, Feldman, Hardt, Pitassi, Reingold, Roth. Generalization in Adaptive Data Analysis and Holdout Reuse. https://arxiv.org/abs/1506.02629
- Blum, Hardt. The Ladder. https://arxiv.org/abs/1502.04585
- Russo, Zou. How much does your data exploration overfit? https://arxiv.org/abs/1511.05219
- Xu, Raginsky. Information-theoretic analysis of generalization capability of learning algorithms. https://arxiv.org/abs/1705.07809
- Zhang, Bengio, Hardt, Recht, Vinyals. Understanding deep learning requires rethinking generalization. https://arxiv.org/abs/1611.03530

Observations, plots and graphical perception
- Daswani et al. Plots Unlock Time-Series Understanding in Multimodal Models. https://arxiv.org/abs/2410.02637
- Liu, Liu, Prakash. A Picture is Worth A Thousand Numbers. https://arxiv.org/abs/2411.06018
- Nguyen, Maeda, Geshvadi, Haehn. Evaluating Graphical Perception with Multimodal LLMs. https://arxiv.org/abs/2504.04221
- Guo, Kang, Shah, Pfister, Varma. Understanding Graphical Perception in Data Visualization through Zero-shot Prompting of VLMs. https://arxiv.org/abs/2411.00257
- Ma et al. LLM Agents Can See Code Repositories. https://arxiv.org/abs/2606.14061
- Yang et al. SWE-agent. https://arxiv.org/abs/2405.15793
- Hu et al. Visual Sketchpad. https://arxiv.org/abs/2406.09403
- Lee, Cho, Kiela. Countering Language Drift via Visual Grounding. https://arxiv.org/abs/1909.04499

Compilation, caching and certification
- Wu et al. SGM: A Statistical Goedel Machine. https://arxiv.org/abs/2510.10232
- Wang, Dorchen, Jin. On the Statistical Limits of Self-Improving Agents. https://arxiv.org/abs/2510.04399
- Jaber, Jaber. Auto: The AGI Compiler. https://arxiv.org/abs/2607.04542
- Ni et al. How Much Skill Orchestration Can LLM Agents Compile Away? (SkillCache). https://arxiv.org/abs/2611.10022
- El Yadouni, Li. TraceCompiler. https://arxiv.org/abs/2608.02680
- Zhang, Wornow, Wan, Olukotun. Agentic Plan Caching. https://arxiv.org/abs/2506.14852
- Wang, Mao, Fried, Neubig. Agent Workflow Memory. https://arxiv.org/abs/2409.07429
- Wang, Gandhi, Neubig, Fried. Inducing Programmatic Skills for Agentic Tasks. https://arxiv.org/abs/2504.06821
- Angelopoulos, Bates, Candes, Jordan, Lei. Learn then Test. https://arxiv.org/abs/2110.01052
- Angelopoulos, Bates, Fisch, Lei, Schuster. Conformal Risk Control. https://arxiv.org/abs/2208.02814
- Sun et al. Compositional Conformal Risk Control for Multi-Stage LLM Cascades. https://arxiv.org/abs/2611.11114
- Dou, Lian, Li. Conformal Cascade. https://arxiv.org/abs/2607.25018
- Yao, Shinn, Razavi, Narasimhan. tau-bench (pass^k). https://arxiv.org/abs/2406.12045

Label-free agreement rewards (replacement)
- Zuo et al. TTRL: Test-Time Reinforcement Learning. https://arxiv.org/abs/2504.16084
- Wang et al. Self-Harmony. https://arxiv.org/abs/2511.01191
- Pan et al. CoVerRL: Breaking the Consensus Trap. https://arxiv.org/abs/2603.17775
- Yang et al. Co-RL. https://arxiv.org/abs/2608.17253
- Kocabas, Karagoz, Akbas. Self-Supervised Learning of 3D Human Pose using Multi-view Geometry (EpipolarPose). https://arxiv.org/abs/1903.02330
- Blum, Mitchell. Combining labeled and unlabeled data with co-training. COLT 1998. DOI 10.1145/279943.279962. UNVERIFIED: the DOI resolved to the ACM Digital Library, which returned HTTP 403.
