# P05 Evolvability: literature and novelty check

Status: complete. 28 web searches run; about 45 abstract or landing pages fetched (arXiv abs pages, four arXiv HTML full texts for targeted claims, proceedings and author pages). Verification date: 2026-11-24. Every entry in Sections 3 and 7 was read from a fetched page unless it is marked UNVERIFIED.

## 1. The idea under review

P05 asks whether the structure of a harness's code changes how far an LLM-driven self-improvement loop can take it, when the harness's input-output behavior is held fixed. Structure here means five properties: modularity, logged intermediate values, exposed parameters, executable checks and identifier naming. The method applies behavior-preserving transformations to a seed harness (verified by differential testing), assigns them in a randomized factorial design, and runs a fixed optimizer under a fixed evaluation budget. A second stage uses structure to predict metaproductivity for parent selection, compared with the Darwin Goedel Machine (DGM) score-based rule and the Huxley-Goedel Machine (HGM) clade-metaproductivity estimate. It also tests a refactor-first split of the budget.

The formal object is simple to state. Let $h$ be a harness, $O$ an optimizer (proposer LLM plus search loop), $B$ an evaluation budget and $J$ a held-out score. Define the evolvability of $h$ as $E(h; O, B) = \mathbb{E}_O[\max_{t \le B} J(h_t)] - J(h_0)$. A behavior-preserving transformation $T$ satisfies $f_{T(h)}(x) = f_h(x)$ for every input $x$, so $J(T(h)) = J(h)$. P05 asks whether $E(T(h); O, B) \neq E(h; O, B)$, which factors of $T$ drive the difference, and whether the difference shrinks as $O$ becomes more capable. This is the software analogue of the distinction in evolutionary biology between a phenotype and its variational properties, where two genotypes with the same phenotype can differ in how readily selection improves them (Wagner and Altenberg 1996, citation 26).

## 2. Search log

Queries run (WebSearch, standard mode):

1. Huxley-Godel Machine clade metaproductivity self-improving coding agent
2. Darwin Godel Machine open-ended evolution of self-improving agents arXiv
3. Meta-Harness end-to-end optimization of model harnesses
4. Agentic Harness Engineering arXiv 2026 harness evolution coding agent
5. evolvability of programs under LLM mutation code structure modularity evolutionary search
6. code readability identifier names affect LLM code generation program repair empirical study
7. code health metrics AI-friendliness LLM refactoring success "code for machines"
8. codebase quality technical debt effect on LLM coding agent task success controlled experiment
9. Mutation Without Variation convergence dynamics LLM-driven program evolution
10. initial seed program sensitivity LLM evolutionary search AlphaEvolve OpenEvolve ShinkaEvolve ablation
11. predicting which agent will self-improve metaproductivity estimation parent selection 2026
12. HarnessFix agent harness repair
13. identifier renaming obfuscation LLM code understanding robustness
14. does refactoring code make LLM agents more effective at modifying it
15. Wagner Altenberg 1996 complex adaptations and the evolution of evolvability
16. evaluating AGENTS.md repository context files effect on coding agent success
17. "evolvability" LLM-guided program search representation design harness self-improvement
18. Hyperagents recursive metacognitive self-improvement DGM-H
19. semantics-preserving code transformations change LLM evolutionary optimization outcome
20. self-improving coding agent SICA
21. refactoring step before optimization LLM agent budget allocation
22. Kashtan Alon 2005 spontaneous evolution of modularity
23. what makes a program easier for LLM to improve, seed structure, documentation ablation
24. Schulte Forrest software mutational robustness
25. evolvability-based parent selection offspring potential LLM program evolution
26. code bloat complexity growth self-improving agent lineage DGM
27. randomized controlled experiment refactoring agent scaffold modular vs monolithic LLM optimizer
28. follow-ups on benchmark and model pages (Aider polyglot, SWE-bench, tau2-bench, Qwen model cards)

Nine searches phrased around the P05 design (queries 5, 6, 8, 10, 14, 19, 23, 25, 27) returned an explicit "no study found" for the exact question. That pattern is evidence, not proof, that the core causal experiment is unpublished. Full texts were read for four claims where the abstract was silent: AHE (whether it ablates observability or compares modular and monolithic harnesses), Code for Machines (study design and effect sizes), HGM (how CMP is estimated, and whether code features are used) and Predict Before You Modify (its inputs and prediction horizon). The DGM HTML was read for its parent-selection description and stepping-stone evidence.

## 3. Closest prior work

Ordered from closest to the P05 core question to more distant.

### 3.1 Code for Machines, Not Just Humans (Borg et al., 2026)

- Citation: Markus Borg, Nadim Hagatulah, Adam Tornhill, Emma Soederberg. "Code for Machines, Not Just Humans: Quantifying AI-Friendliness with Code Health Metrics." FORGE 2026 (3rd ACM International Conference on AI Foundation Models and Software Engineering). arXiv:2601.02200.
- URL: https://arxiv.org/abs/2601.02200 (verified; HTML v1 read for numbers)
- What they did: they stratified 5,000 Python CodeContests solutions by CodeHealth (a maintainability metric calibrated on human comprehension) and asked LLMs to refactor them, with passing unit tests as the correctness check. Five medium open-weight models (Gemma, GLM, Granite, GPT, Qwen) all broke healthy code significantly less often (for example Qwen 19.3% versus 27.8% break rate). Sonnet 4.5 (13.2% versus 16.0%) and an agentic Claude setup (3.8% versus 5.2%) showed no significant difference. A one standard deviation increase in CodeHealth raised the odds of a non-breaking refactoring by about 20% to 40%, but decision-tree AUCs were only 0.54 to 0.57.
- Overlap with P05: it is the only paper found that links human-oriented code structure to LLM editing success with numbers, and it frames structure as a property that changes what an AI can safely do to code.
- What it leaves open: the design is observational (different programs with different behaviors, no behavior-preserving manipulation), the outcome is one refactoring step rather than an improvement trajectory, and there is no optimizer, budget or fitness signal. Its most important finding for P05 is a warning: the effect was not significant for the two strongest models. P05 must treat "structure stops mattering for strong proposers" as a live hypothesis and design for it.

### 3.2 Agentic Harness Engineering (Lin et al., 2026)

- Citation: Jiahang Lin, Shichun Liu, Chengjun Pan, Lizhi Lin, Shihan Dou, Zhiheng Xi, Xuanjing Huang, Hang Yan, Zhenhua Han, Tao Gui, Yu-Gang Jiang. "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses." arXiv:2604.25850 (v1 28 Apr 2026, v5 22 Nov 2026).
- URL: https://arxiv.org/abs/2604.25850 (verified; HTML v4 read)
- What they did: AHE evolves a coding-agent harness in the NexAU framework, which exposes seven component types (system prompt, tool description, tool implementation, middleware, skill, sub-agent configuration, long-term memory) as explicit files, and adds three "observability" pillars (component, experience, decision). Ten iterations raise Terminal-Bench 2 pass@1 from 69.7% to 77.0%, above the Codex-CLI harness (71.9%). The only ablation swaps single evolved components into the seed (memory only 75.3%, tool only 73.0%, middleware only 71.9%, system prompt only 67.4%). Fix-prediction precision was 33.7% and recall 51.4%.
- Overlap with P05: AHE is built on the premise that P05 wants to test. Its introduction states that tightly coupled harness frameworks make edits beyond the prompt error-prone, and it argues that file-level decoupling localizes every pass-rate change to one file.
- What it leaves open: the full text contains no ablation of the observability pillars and no comparison between a monolithic and a modular harness. Modularity and observability are asserted design choices, never manipulated. P05 can be framed as the causal test of AHE's premise.

### 3.3 Huxley-Goedel Machine (Wang et al., 2025; ICLR 2026)

- Citation: Wenyi Wang, Piotr Piekos, Li Nanbo, Firas Laakom, Yimeng Chen, Mateusz Ostaszewski, Mingchen Zhuge, Juergen Schmidhuber. "Huxley-Goedel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine." arXiv:2510.21614; ICLR 2026 poster.
- URLs: https://arxiv.org/abs/2510.21614 and https://iclr.cc/virtual/2026/poster/10009359 (both verified; HTML v3 read)
- What they did: they name the metaproductivity-performance mismatch (an agent's own score is a poor guide to how much its descendants will improve) and estimate clade-metaproductivity as the pooled success rate over an agent's clade, $\widehat{CMP}(a) = n^{C(a)}_{s} / (n^{C(a)}_{s} + n^{C(a)}_{f})$, selecting expansions by Thompson sampling over Beta distributions. Correlation with empirical CMP (weighted / unweighted): on SWE-Verified-60, SICA 0.444 / 0.444, DGM 0.285 / 0.406, HGM 0.778 / 0.512; on Polyglot, SICA 0.274 / 0.274, DGM 0.383 / 0.357, HGM 0.626 / 0.873. Main comparisons use 800 benchmark task evaluations; Polyglot cost about 5,000 USD across the three methods.
- Overlap with P05: P05's second stage targets the same quantity (metaproductivity) for the same decision (which parent to expand).
- What it leaves open: the HGM estimator uses only success and failure counts of descendants. The full text confirms that no feature of an agent's code is used to predict metaproductivity (Appendix F inspects diffs qualitatively only). The estimator is therefore uninformative at birth, when a node has no descendants, and becomes informative only after budget has been spent on its clade. A structural prior that is available before any evaluation is the open niche.

### 3.4 Darwin Goedel Machine (Zhang et al., 2025)

- Citation: Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, Jeff Clune. "Darwin Goedel Machine: Open-Ended Evolution of Self-Improving Agents." arXiv:2505.22954 (v3 12 Mar 2026).
- URL: https://arxiv.org/abs/2505.22954 (verified; HTML v3 read)
- What they did: an archive of coding agents that rewrite their own code, validated empirically. SWE-bench rose from 20.0% to 50.0% and Polyglot from 14.2% to 30.7%. Parent selection is roughly proportional to performance and inversely proportional to the number of children with code-editing functionality. Figure 3 reports that many paths to innovation traverse lower-performing nodes, and the final best agent's lineage includes two performance dips. One SWE-bench run takes about two weeks.
- Overlap with P05: the stepping-stone observation is direct evidence that score does not equal evolvability, which motivates P05.
- What it leaves open: why some low-scoring nodes are good stepping stones. DGM does not examine whether code properties of those nodes explain their descendants' success.

### 3.5 Predict Before You Modify (Xie et al., 2026)

- Citation: Zixuan Xie, Chang Xu, Yuhua Jiang, Li Zhao. "Predict Before You Modify: Learning Improvement Dynamics for Self-Evolving Agents." arXiv:2610.13991 (v2 15 Oct 2026).
- URL: https://arxiv.org/abs/2610.13991 (verified; HTML v2 read)
- What they did: an editable Improvement Dynamics Model (IDM), a program that calls a frozen LLM, forecasts task-level outcomes of a proposed diff before evaluation and is updated from observed outcomes. Built on HyperAgents, it improves average performance over generations by up to 46% across four domains, with gains under matched token budgets and on held-out tasks.
- Overlap with P05: it predicts the effect of modifications to guide self-evolution, which is the same family of decision as structure-based parent selection.
- What it leaves open: the IDM predicts only the immediate, one-step outcome of one diff, and uses no static code-structure features. The conclusion lists as future work a world model of agent evolution that could find modification sequences "whose early steps offer little immediate gain." A behavior-preserving refactor is the cleanest example of such an early step (zero immediate gain by construction), so P05's refactor-first arm answers a question this paper leaves open.

### 3.6 Meta-Harness (Lee et al., 2026)

- Citation: Yoonho Lee, Roshen Nair, Qizheng Zhang, Kangwook Lee, Omar Khattab, Chelsea Finn. "Meta-Harness: End-to-End Optimization of Model Harnesses." arXiv:2603.28052.
- URL: https://arxiv.org/abs/2603.28052 (verified)
- What they did: an agentic proposer reads the source code, scores and execution traces of all prior candidates through a filesystem and proposes new harness code for a frozen model. It beats a state-of-the-art context-management system by 7.7 points on online text classification with 4x fewer context tokens, adds 4.7 points on 200 IMO-level retrieval-augmented math problems across five held-out models, and surpasses hand-engineered TerminalBench-2 harnesses. The paper attributes gains to richer access to prior experience.
- Overlap with P05: it shows that the information the proposer can read changes outcomes. Logged intermediate values are one way a harness's structure changes that information.
- What it leaves open: the harness's own code structure is never varied. Meta-Harness varies what history the proposer sees, while P05 varies how the object being optimized is written.

### 3.7 HarnessFix (Chen et al., 2026)

- Citation: Mengzhuo Chen, Junjie Wang, Zhe Liu, Yawen Wang, Haiming Zheng, Qing Wang. "From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws." arXiv:2606.06324 (v2 2 Jul 2026).
- URL: https://arxiv.org/abs/2606.06324 (verified)
- What they did: converts traces and harness artifacts into a structured intermediate representation, attributes failures to steps and harness layers, consolidates them into flaw records and applies scoped repairs with regression checks; 6.3% to 18.4% gains over initial harnesses on four benchmarks (v2 abstract).
- Overlap with P05: it relies on failures being attributable to harness layers, which should be easier when the harness is modular and observable.
- What it leaves open: harness structure is an input to its pipeline, not a variable it studies.

### 3.8 Component-Aware Feedback for Self-Evolving Programs (Lin, Nian, Fang, 2026)

- Citation: Ethan Lin, Jinming Nian, Yi Fang. "Component-Aware Feedback for Self-Evolving Programs." arXiv:2609.38639.
- URL: https://arxiv.org/abs/2609.38639 (verified)
- What they did: records which components changed between a program and its parent, with metric differences in local and global frames, in an attribution memory read by later mutations. On twelve BRIGHT reranking datasets it reaches the strongest baseline's final quality with about one third of the budget and ends 7.2% higher in held-out nDCG@10.
- Overlap with P05: it shows that component-level credit assignment speeds evolution, one mechanism through which modularity could raise evolvability.
- What it leaves open: the method presupposes a decomposition into components; whether making a program more decomposable improves evolution is not tested.

### 3.9 Code Evolution Graphs (van Stein et al., 2025) and Mutation Without Variation (Gurkan et al., 2026)

- Citations: Niki van Stein, Anna V. Kononova, Lars Kotthoff, Thomas Baeck. "Code Evolution Graphs: Understanding Large Language Model Driven Design of Algorithms." GECCO 2025. arXiv:2503.16668. Can Gurkan, Forrest Stonedahl, Uri Wilensky. "Mutation Without Variation: Convergence Dynamics in LLM-Driven Program Evolution." GECCO 2026 Workshop on Large Language Models for and with Evolutionary Computation. arXiv:2606.05408.
- URLs: https://arxiv.org/abs/2503.16668 and https://arxiv.org/abs/2606.05408 (both verified)
- What they did: Code Evolution Graphs tracks code complexity across LLM-driven algorithm design runs and finds complexity grows with repeated prompting and sometimes hurts performance. Mutation Without Variation finds that LLM mutation without selection collapses to a small set of forms: in 87% of chains, more than 93% of mutations revisit a previously seen structural form, unlike classical GP subtree mutation.
- Overlap with P05: both measure structural properties of code inside LLM evolution and connect them to search dynamics.
- What they leave open: both are correlational or descriptive. Neither intervenes on the seed's structure while fixing its behavior.

### 3.10 What Do Evolutionary Coding Agents Evolve? (Pelleriti et al., 2026)

- Citation: Nico Pelleriti, Sree Harsha Nelaturu, Zhanke Zhou, Zongze Li, Max Zimmer, Bo Han, Sebastian Pokutta. "What Do Evolutionary Coding Agents Evolve?" arXiv:2605.20086.
- URL: https://arxiv.org/abs/2605.20086 (verified)
- What they did: EvoTrace (traces from four frameworks, 16 tasks) and EvoReplay (replays search states and intervenes on constants, components, models or prompts). Most gains come from a few of nine edit types, and about 30% of added lines are byte-identical re-introductions of previously deleted lines.
- Overlap with P05: separating new algorithmic structure from re-tuning constants is close to P05's exposed-parameters factor, and the replay-intervention method is a useful tool for P05's mediation analysis.
- What it leaves open: interventions are on search states and operators, not on the behavior-preserving form of the seed program.

### 3.11 Naming and readability effects on LLM code understanding

- Citations: Cuong Chi Le, Minh V.T. Pham, Cuong Duc Van, Hoang N. Phan, Huy N. Phan, Tien N. Nguyen. "When Names Disappear: Revealing What LLMs Actually Understand About Code." arXiv:2510.03178 (2025). Serge Lionel Nikiema, Jordan Samhi, Abdoul Kader Kabore, Jacques Klein, Tegawende F. Bissyande. "The Code Barrier: What LLMs Actually Understand?" arXiv:2504.10557 (2025).
- URLs: https://arxiv.org/abs/2510.03178 and https://arxiv.org/abs/2504.10557 (both verified)
- What they did: semantics-preserving obfuscation (including identifier removal) degrades LLM summarization and even execution-prediction tasks; ClassEval-Obf is released as a name-suppressed benchmark. The Code Barrier tests 13 models on 250 obfuscated Java programs and finds performance falls as obfuscation grows.
- Overlap with P05: these establish that identifier naming, a behavior-preserving property, changes what an LLM computes about code. This makes P05's naming factor plausible a priori.
- What they leave open: single-shot comprehension tasks, not multi-step improvement under a budget.

### 3.12 Evaluating AGENTS.md (Gloaguen et al., 2026)

- Citation: Thibaud Gloaguen, Niels Muendler-Sasahara, Mark Niklas Mueller, Veselin Raychev, Martin Vechev. "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?" arXiv:2602.11988 (v3 29 Sep 2026).
- URL: https://arxiv.org/abs/2602.11988 (verified)
- What they did: across LLMs and coding agents, repository context files generally do not raise task success and raise inference cost by more than 20%; repository overviews do not help, though instructions are followed.
- Overlap with P05: a controlled test of a behavior-neutral addition to a codebase (documentation) on agent success.
- What it leaves open: a negative result for one kind of added text; it does not test modularity, logging, exposed parameters or checks, and does not follow an improvement trajectory. It is a second warning, alongside 3.1, that intuitive "agent-friendly" changes can have null effects on strong agents.

### 3.13 Other relevant systems (shorter)

- Hyperagents (Zhang et al., arXiv:2603.19461, https://arxiv.org/abs/2603.19461, verified): makes the meta-level modification procedure editable (DGM-H). Leaves open which properties of the editable program make metacognitive self-modification productive.
- Mendel Goedel Machine (Liu et al., arXiv:2608.07645, https://arxiv.org/abs/2608.07645, verified): inheritance-based self-modification types (clonal, reaction-norm, cross-lineage hybridization) analyzed under an additive fitness model. Cross-lineage hybridization implicitly depends on code being decomposable into separable parts, which is not measured.
- HGM-Dual (Paul et al., arXiv:2610.30042, https://arxiv.org/abs/2610.30042, verified): lineage-aware context and error-conditioned children; matches HGM variants with 2x to 4x less evaluation budget on planning tasks. A strong recent baseline for budget efficiency.
- Where Should the Evaluation Budget Go (Luo et al., arXiv:2610.37276, https://arxiv.org/abs/2610.37276, verified): splits evaluation between search and final confirmation and uses about half the evaluation cells. It does not consider spending budget on restructuring.
- ImprovEvolve (Kravatskiy et al., arXiv:2602.10233, https://arxiv.org/abs/2602.10233, verified): replaces a monolithic evolved program with three subroutines in a basin-hopping loop; the abstract reports no controlled comparison against the monolithic representation at matched budget.
- FunSearch (Romera-Paredes et al., Nature 625:468 to 475, 2023, https://pmc.ncbi.nlm.nih.gov/articles/PMC10794145/, verified) and OpenEvolve (https://github.com/algorithmicsuperintelligence/openevolve, verified): both rely on a fixed skeleton with only a marked region evolved (FunSearch evolves "only the part governing the critical program logic"; OpenEvolve uses EVOLVE-BLOCK-START and EVOLVE-BLOCK-END markers). This is a structural convention whose effect on evolvability, as far as the searches show, has never been measured.
- SemRep (Li et al., arXiv:2603.13640, https://arxiv.org/abs/2603.13640, verified): mid-trains code LLMs on semantics-preserving transformations and pairs them with an evolutionary coding agent; it shows model sensitivity to behavior-preserving form matters for evolutionary search, but does not vary the input program's form under a fixed model.

## 4. Is the core idea already done?

Verdict: partially. The central experiment is not done.

No paper found applies behavior-preserving structural transformations to a seed program or harness, randomizes them, and measures the downstream improvement trajectory of an LLM optimizer at a fixed budget. Nine searches phrased around this design returned an explicit absence. The pieces that exist are:

1. Observational evidence that human-oriented code quality predicts single-step LLM refactoring safety, with the effect vanishing for the strongest models (Borg et al. 2026).
2. Systems that assume modularity and observability help harness evolution, without ablating them (AHE, HarnessFix, component-aware feedback).
3. Evidence that score is a weak predictor of metaproductivity, an estimator based on descendant counts (HGM), and one-step pre-evaluation forecasting (IDM). None uses code features, and IDM explicitly defers long-horizon prediction.
4. Comprehension studies showing that behavior-preserving changes such as renaming change LLM outputs (When Names Disappear, The Code Barrier, and SemRep indirectly).
5. A biological theory of evolvability and modularity (Wagner and Altenberg 1996; Kashtan and Alon 2005; Clune et al. 2013) and a genetic-programming literature on neutral variation (Schulte et al. 2014) that have not been connected to LLM-driven self-improvement.

Exact residual gap: a causal, behavior-controlled estimate of how each structural property of a harness changes LLM-driven improvement at a fixed evaluation budget; how that effect depends on proposer capability; which mechanism carries it (edit localization, regression rate per edit, credit assignment, invalid-candidate rate); and whether a structural prior can fix HGM's cold-start problem in parent selection or justify spending label-free budget on refactoring before search.

## 5. Novelty and significance scores

Scored as a demanding ICML area chair would score the proposal as currently stated.

- Novelty: 4.0 out of 5. The causal design (behavior-preserving transformations, differential testing, randomized factorial, fixed optimizer and budget) is new for LLM self-improvement, and the cold-start structural prior for metaproductivity fills a real gap left by HGM. It falls short of 4.5 because reviewers will read the hypothesis ("modular, readable code is easier to improve") as long-standing software engineering folklore, and AHE and Code for Machines already make the claim informally. Novelty rises to about 4.5 if the paper is framed around the capability interaction (does structure still matter as proposers scale, and through which mechanism) and around a label-free refactoring phase that produces measurable held-out gain, since neither appears in the literature.
- Significance: 3.5 out of 5 as stated, with a credible path to 4.5. As stated it risks being an empirical SE-for-LLMs study whose answer is "somewhat, for weak models." It becomes significant if it delivers (a) an evolvability measure that predicts held-out improvement better than score and better than HGM's CMP at cold start, (b) a practical rule (refactor first, or select parents by structure) that beats DGM, HGM and HGM-Dual at matched budget in two domains, and (c) a scaling curve of the structure effect over at least three proposer capabilities. A clean null with tight equivalence bounds across proposers would also be publishable, because it would refute the design premise of AHE and the skeleton conventions of FunSearch and OpenEvolve.

## 6. Sharpenings

### 6.1 Reframe the question around three claims

1. Structure has a causal effect on evolvability that is separable from behavior and from code length.
2. The effect is mediated by measurable search quantities (localization accuracy of edits, regression rate per accepted edit, invalid-candidate rate, edit acceptance rate). This gives the paper a mechanism and connects to the biological idea that modularity reduces pleiotropy, the tendency of one change to affect many traits.
3. The effect decreases with proposer capability, and the slope of that decrease is the main scientific quantity. Code for Machines already shows a disappearing effect for Sonnet 4.5; P05 should predict and measure the slope.

### 6.2 The single most decisive experiment

A randomized fractional-factorial experiment on one seed harness, crossed with proposer capability.

- Seed: the StaBLE feature-extraction harness adapted to monocular inputs (the public `stanfordnmbl/stable-analysis` `get_features` logic run on cached RTMPose and OpenCap Monocular outputs). The Y-Balance reach-window detector, which sweeps a toe-velocity threshold from 0.7 to 0.3 m/s and found no reach window on monocular reconstructions in the lab pilot, is the running example. Whether this threshold is a buried literal or an exposed parameter, whether the detected window is logged, and whether an executable check flags an empty window are all behavior-preserving choices.
- Factors, each at two levels ("degraded" and "improved", so both directions are covered and ceiling effects are avoided): modularity (single long function versus per-task functions with typed interfaces), logged intermediates (none versus logged windows, center-of-mass traces and feature values written to a trace directory), exposed parameters (inline literals versus a typed config), executable checks (none versus invariant assertions that warn without changing outputs), naming (machine-generated opaque names versus descriptive names produced by a renamer that sees only the code). A $2^{5-1}$ resolution V design (16 cells) estimates all main effects and two-way interactions.
- Replication: at least 5 independent optimizer runs per cell per proposer (80 runs per proposer), with optimizer seeds shared across cells so that run-level randomness is paired.
- Optimizer: one fixed loop (an OpenEvolve-style or DGM-style archive with fixed parent selection and a fixed prompt), a fixed budget of $B$ candidate evaluations on development participants (for example $B = 400$) and a fixed token cap.
- Proposers: Qwen3-Coder-30B-A3B-Instruct (30.5B total, 3.3B active parameters, verified model card), a larger open coder, and one frontier API model (HGM used GPT-5-mini; the exact frontier choice is to be fixed at registration). Three capability levels are the minimum needed for a slope.
- Primary outcome: held-out-participant improvement in task-averaged MAE at budget $B$ (final best and area under the best-so-far curve), computed on a sealed test split never shown to the optimizer.
- Decisive contrast: the structure main effects and the structure by proposer interaction in a mixed-effects model with random intercepts for optimizer seed.

### 6.3 Essential controls

1. Behavior equivalence: bitwise-identical outputs (or a declared float tolerance) on all development and test inputs, property-based fuzzing of intermediate inputs, and identical tool-call sequences. Reject any transformation that fails, and report the coverage of the differential tests.
2. Length and context placebo: a length-matched transformation (neutral comments or whitespace that add the same token count) to separate structure from context length and position.
3. Change placebo: synonym renaming to equally descriptive names, separating "names were changed" from "names became informative."
4. No smuggled knowledge: the renamer and refactorer see only code, never labels, scores or the biomechanics notes, and comments may not contain results. Audit with a held-out reviewer.
5. Frozen checks: the optimizer may not edit the executable checks or the evaluator; log any attempt.
6. Optimizer-visible information: hold the feedback channel fixed across cells (scores plus traces in a filesystem, in the style of Meta-Harness), so the logging factor changes what exists to read without changing what the loop is allowed to read. Keep P06's split discipline: development participants for search, a separate selection split, sealed test participants.
7. Structure drift: measure the five structural properties at every generation, since optimizers may erode structure (Code Evolution Graphs reports complexity growth). Report evolvability with and without a structure-preserving lint gate.
8. Contamination: the BioHarness seed is private; in the second domain, use a seed whose transformed variants cannot have been seen in pretraining.

### 6.4 Mechanism measurements (mediators)

- Edit locality: files and lines touched per accepted edit.
- Pleiotropy proxy: fraction of previously correct development examples broken by an accepted edit.
- Localization accuracy: plant known faults (for example a sign flip in one feature) in otherwise equivalent variants and score whether the proposer's first edit touches the faulty unit.
- Invalid-candidate rate: crashes, exceptions and timeouts per proposal, which consume budget without giving information.
- Acceptance rate and revisit rate (the Mutation Without Variation and EvoTrace re-introduction statistics).
- A causal mediation analysis that tests whether the structure effect on held-out gain passes through these quantities.

### 6.5 Second stage, made sharper

- Structural prior for HGM: replace the uninformative Beta prior in HGM's Thompson sampling with a prior whose parameters are a learned function of structural features $x_a$ of agent $a$: $\widehat{CMP}(a) = (n_s + \alpha(x_a)) / (n_s + n_f + \alpha(x_a) + \beta(x_a))$. Fit $\alpha$ and $\beta$ on archives from stage one and from released DGM archives, then test on new runs. Report correlation with empirical CMP as a function of how many descendant evaluations exist (0, 5, 20, 80), since the claim is about cold start.
- Refactor-first: a label-free phase in which the proposer applies behavior-preserving refactors verified by differential testing, costing proposer tokens but zero labeled evaluations, followed by the same search. Compare refactor fractions $\rho \in \{0, 0.1, 0.25\}$ of total proposer tokens at matched total tokens and matched labeled evaluations. This addresses IDM's deferred question about modifications with no immediate gain, and it matters in biomechanics because each labeled evaluation depends on scarce reference recordings.

### 6.6 Strongest baselines (named, with links)

- DGM parent selection: https://arxiv.org/abs/2505.22954
- HGM (CMP with Thompson sampling): https://arxiv.org/abs/2510.21614
- HGM-Dual: https://arxiv.org/abs/2610.30042
- IDM-guided evolution (Predict Before You Modify): https://arxiv.org/abs/2610.13991
- ShinkaEvolve adaptive parent sampling: https://arxiv.org/abs/2509.19349
- EvalAlloc-style budget split: https://arxiv.org/abs/2610.37276
- Component-aware feedback: https://arxiv.org/abs/2609.38639
- AHE observability loop, as the optimizer in one arm: https://arxiv.org/abs/2604.25850
- Meta-Harness proposer with filesystem history: https://arxiv.org/abs/2603.28052
- An "always refactor" heuristic that applies a standard refactoring pass without differential testing, to show why verification matters.

### 6.7 Domains

- Biomechanics test bed: StaBLE single-camera examples, split by participant before anything else (lab pilot: 171 participants, 2,968 usable examples, 43 test participants). Stage A uses a programmatic harness over cached tool outputs, so a candidate evaluation costs CPU seconds and many replicates are affordable. Stage B repeats the two strongest factors on the tool-calling Qwen3-VL-8B-Instruct agent harness. Recompute min-max normalization bounds on development participants only.
- Second domain (primary): the DGM seed coding agent on the Aider Polyglot benchmark (225 Exercism problems in six languages, https://aider.chat/2024/12/21/polyglot.html), using HGM's 800-evaluation protocol so results are directly comparable with published DGM and HGM numbers. Self-host the open proposer to control cost.
- Second domain (cheaper alternative, or a third domain): a tool-agent harness on tau2-bench retail (https://arxiv.org/abs/2506.07982), where PRISM (https://arxiv.org/abs/2609.05736) reports harness-search lifts and stresses repeatability.

### 6.8 Metrics and statistics

- Primary: held-out improvement at budget $B$ (final value and area under the best-so-far curve).
- Secondary: evaluations needed to reach a fixed improvement threshold, tokens per accepted improvement, the mediator quantities above, structure drift, and correlation of the structural CMP prior with empirical CMP at each descendant count.
- Analysis: a pre-registered linear mixed model, outcome ~ structure factors x proposer + (1 | optimizer seed) + (1 | cell); a smallest effect of interest fixed in advance (for example 10% of the seed-to-best gain); two one-sided equivalence tests for null claims; Holm correction across the five main effects. Estimate run-to-run variance from a small pilot (PRISM and EvalAlloc both report noisy search outcomes) and size the replicates from it.

### 6.9 What would falsify the hypothesis

- With at least 5 runs per cell, no structural factor changes held-out improvement at budget $B$ beyond the smallest effect of interest, with equivalence confirmed by TOST, for the weakest proposer as well as the strongest. That would refute the premise in both domains.
- Effects appear, but the length-matched placebo reproduces them; context size, not structure, would then drive the result.
- Effects appear only on development participants and vanish on the sealed test split; structure would then be helping the optimizer overfit faster.
- For the second stage: the structural prior does not raise correlation with empirical CMP above HGM's estimator at zero to five descendants, or HGM with the prior does not beat plain HGM at matched budget.
- For refactor-first: no fraction $\rho > 0$ beats $\rho = 0$ at matched total tokens.

### 6.10 Boundary with ideas already explored

Executable checks in P05 are invariant assertions inside the harness (for example, a detected reach window must be non-empty) treated as code structure. They must not be framed as known-answer checks or physical-response checks, which earlier proposals explored. The refactor-first arm uses differential testing only as an equivalence gate, which is different from the earlier idea of selecting which recordings to re-execute after a harness edit.

## 7. Key citations (verified)

Each line gives the reference, the verified URL and the claim it supports.

1. Zhang J, Hu S, Lu C, Lange R, Clune J. "Darwin Goedel Machine: Open-Ended Evolution of Self-Improving Agents." arXiv:2505.22954, 2025. https://arxiv.org/abs/2505.22954. Supports: empirical self-modification raises SWE-bench from 20.0% to 50.0%; paths to the best agent traverse lower-scoring nodes, so score is not evolvability. Verified.
2. Wang W, Piekos P, Nanbo L, et al. "Huxley-Goedel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine." arXiv:2510.21614, 2025; ICLR 2026. https://arxiv.org/abs/2510.21614 (poster page https://iclr.cc/virtual/2026/poster/10009359). Supports: metaproductivity-performance mismatch; CMP estimated only from descendant success counts; 800-evaluation protocol and correlations with empirical CMP. Verified.
3. Lin J, Liu S, Pan C, et al. "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses." arXiv:2604.25850, 2026. https://arxiv.org/abs/2604.25850. Supports: modular, observable harness representations are asserted to make evolution work (69.7% to 77.0% on Terminal-Bench 2) but are not ablated. Verified.
4. Borg M, Hagatulah N, Tornhill A, Soederberg E. "Code for Machines, Not Just Humans: Quantifying AI-Friendliness with Code Health Metrics." FORGE 2026; arXiv:2601.02200. https://arxiv.org/abs/2601.02200. Supports: observational link between code health and LLM refactoring break rates; no significant effect for the strongest models. Verified.
5. Xie Z, Xu C, Jiang Y, Zhao L. "Predict Before You Modify: Learning Improvement Dynamics for Self-Evolving Agents." arXiv:2610.13991, 2026. https://arxiv.org/abs/2610.13991. Supports: one-step pre-evaluation forecasting helps self-evolution; long-horizon prediction of modifications with no immediate gain is left as future work. Verified.
6. Lee Y, Nair R, Zhang Q, Lee K, Khattab O, Finn C. "Meta-Harness: End-to-End Optimization of Model Harnesses." arXiv:2603.28052, 2026. https://arxiv.org/abs/2603.28052. Supports: harness code search with a filesystem of code, scores and traces; the information available to the proposer changes outcomes. Verified.
7. Zhang J, Zhao B, Yang W, Foerster J, Clune J, Jiang M, Devlin S, Shavrina T. "Hyperagents." arXiv:2603.19461, 2026. https://arxiv.org/abs/2603.19461. Supports: editable meta-level procedures (DGM-H); base system for IDM. Verified.
8. Chen M, Wang J, Liu Z, Wang Y, Zheng H, Wang Q. "From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws." arXiv:2606.06324, 2026. https://arxiv.org/abs/2606.06324. Supports: layer-level attribution of failures enables scoped repair (6.3% to 18.4% gains). Verified.
9. Lin E, Nian J, Fang Y. "Component-Aware Feedback for Self-Evolving Programs." arXiv:2609.38639, 2026. https://arxiv.org/abs/2609.38639. Supports: component-level credit assignment reaches baseline quality with about one third of the budget; presupposes decomposability. Verified.
10. Paul S, Quan P, Kumar A, Tzou N, Kulkarni V, Chappidi S. "HGM-Dual: Lineage-Aware Guided Agent Harness Optimization for Long-Horizon Planning." arXiv:2610.30042, 2026. https://arxiv.org/abs/2610.30042. Supports: strongest recent budget-efficiency baseline (2x to 4x fewer evaluations than HGM variants). Verified.
11. Luo S, Huang Y, Li M, et al. "Where Should the Evaluation Budget Go in LLM-Driven Agent Scaffold Evolution?" arXiv:2610.37276, 2026. https://arxiv.org/abs/2610.37276. Supports: evaluation-budget allocation is an open design axis; restructuring is not among the options studied. Verified.
12. van Stein N, Kononova AV, Kotthoff L, Baeck T. "Code Evolution Graphs: Understanding Large Language Model Driven Design of Algorithms." GECCO 2025; arXiv:2503.16668. https://arxiv.org/abs/2503.16668. Supports: code complexity grows under repeated LLM prompting and can hurt performance (structure drift). Verified.
13. Gurkan C, Stonedahl F, Wilensky U. "Mutation Without Variation: Convergence Dynamics in LLM-Driven Program Evolution." GECCO 2026 workshop; arXiv:2606.05408. https://arxiv.org/abs/2606.05408. Supports: LLM mutation collapses to recurring structural forms, so structure shapes the reachable search space. Verified.
14. Pelleriti N, Nelaturu SH, Zhou Z, et al. "What Do Evolutionary Coding Agents Evolve?" arXiv:2605.20086, 2026. https://arxiv.org/abs/2605.20086. Supports: replay interventions on search states; about 30% of added lines re-introduce deleted lines; gains concentrate in few edit types. Verified.
15. Le CC, Pham MVT, Van CD, Phan HN, Phan HN, Nguyen TN. "When Names Disappear: Revealing What LLMs Actually Understand About Code." arXiv:2510.03178, 2025. https://arxiv.org/abs/2510.03178. Supports: behavior-preserving removal of names changes LLM outputs, including on execution tasks. Verified.
16. Gloaguen T, Muendler-Sasahara N, Mueller MN, Raychev V, Vechev M. "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?" arXiv:2602.11988, 2026. https://arxiv.org/abs/2602.11988. Supports: an intuitive behavior-neutral addition to a codebase gave no success gain and over 20% more cost, so nulls are plausible. Verified.
17. Romera-Paredes B, Barekatain M, Novikov A, et al. "Mathematical discoveries from program search with large language models." Nature 625:468 to 475, 2023. DOI 10.1038/s41586-023-06924-6. https://pmc.ncbi.nlm.nih.gov/articles/PMC10794145/. Supports: the skeleton-plus-evolved-function convention ("only evolve the part governing the critical program logic"). Verified via PMC.
18. Novikov A, Vu N, Eisenberger M, et al. "AlphaEvolve: A coding agent for scientific and algorithmic discovery." arXiv:2506.13131, 2025. https://arxiv.org/abs/2506.13131. Supports: LLM evolutionary code search at scale; a representative optimizer family. Verified.
19. Lange RT, Imajuku Y, Cetin E, et al. "ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution." arXiv:2509.19349, 2025. https://arxiv.org/abs/2509.19349. Supports: adaptive parent-sampling baseline; a sample-efficient open optimizer usable as the fixed loop. Verified.
20. OpenEvolve. Open-source implementation of AlphaEvolve. https://github.com/algorithmicsuperintelligence/openevolve. Supports: EVOLVE-BLOCK markers as an untested structural convention; candidate fixed optimizer. Verified.
21. Robeyns M, Szummer M, Aitchison L. "A Self-Improving Coding Agent." arXiv:2504.15228, 2025. https://arxiv.org/abs/2504.15228. Supports: self-editing agent baseline (random SWE-bench Verified subset, 17% to 53%); SICA is one of the methods in HGM's CMP-correlation comparison. Verified.
22. Zelikman E, Lorch E, Mackey L, Kalai AT. "Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation." COLM 2024; arXiv:2310.02304. https://arxiv.org/abs/2310.02304. Supports: recursive improvement of an improver program; early RSI framing. Verified.
23. Hu S, Lu C, Clune J. "Automated Design of Agentic Systems." arXiv:2408.08435, 2024. https://arxiv.org/abs/2408.08435. Supports: archive-based meta agent search over agent code. Verified.
24. Yin X, Wang X, Pan L, Lin L, Wan X, Wang WY. "Goedel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement." ACL 2025; arXiv:2410.04444. https://arxiv.org/abs/2410.04444. Supports: self-referential rewriting of agent logic. Verified.
25. Zhang J, Xiang J, Yu Z, et al. "AFlow: Automating Agentic Workflow Generation." arXiv:2410.10762, 2024. https://arxiv.org/abs/2410.10762. Supports: MCTS over code-represented workflows; workflow representation is part of the search space. Verified.
26. Wagner GP, Altenberg L. "Perspective: Complex Adaptations and the Evolution of Evolvability." Evolution 50(3):967 to 976, 1996. DOI 10.1111/j.1558-5646.1996.tb02339.x. https://dynamics.org/~altenber/PAPERS/CAEE/ (author page; the publisher page returned HTTP 403). Supports: modular genotype-phenotype maps with low pleiotropy improve evolvability; the same phenotype can have different variational properties. Verified via author page.
27. Kashtan N, Alon U. "Spontaneous evolution of modularity and network motifs." PNAS 102(39):13773 to 13778, 2005. DOI 10.1073/pnas.0503610102. http://gpbib.cs.ucl.ac.uk/gp-html/Kashtan_2005_PNAS.html (bibliographic record; the PNAS page returned HTTP 403). Supports: modularly varying goals produce modular structure. Verified via bibliographic record.
28. Clune J, Mouret J-B, Lipson H. "The evolutionary origins of modularity." Proc. R. Soc. B 280:20122863, 2013. arXiv:1207.2743. https://arxiv.org/abs/1207.2743. Supports: modular networks adapt more readily than non-modular ones. Verified.
29. Schulte E, Fry ZP, Fast E, Weimer W, Forrest S. "Software Mutational Robustness." Genetic Programming and Evolvable Machines 15:281 to 312, 2014. arXiv:1204.4224. https://arxiv.org/abs/1204.4224. Supports: over 30% of random mutations are neutral on test suites; neutral variation as a resource for search. Verified (arXiv page fetched; journal volume and pages from the search listing of the Springer and gpbib records).
30. Zhong L, Wang Z, Shang J. "Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step-by-step." arXiv:2402.16906, 2024. https://arxiv.org/abs/2402.16906. Supports: exposing intermediate variable values per basic block improves LLM debugging by up to 9.8%, a single-step analogue of the logging factor. Verified.
31. Yang J, Jimenez CE, Wettig A, et al. "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering." arXiv:2405.15793, 2024. https://arxiv.org/abs/2405.15793. Supports: interface design changes agent performance, the closest established result that the shape of what an agent operates on matters. Verified.
32. Khattab O, Singhvi A, Maheshwari P, et al. "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines." arXiv:2310.03714, 2023. https://arxiv.org/abs/2310.03714. Supports: declaring modules and parameters makes pipelines optimizable, a design-for-optimizability precedent for the exposed-parameters factor. Verified.
33. Kravatskiy A, Khrulkov V, Oseledets I. "ImprovEvolve: Basin-Hopping Meets LLM-Guided Evolutionary Search." ICML 2026 AI for Math Workshop; arXiv:2602.10233. https://arxiv.org/abs/2602.10233. Supports: a decomposed program representation claimed to reduce load on the LLM, without a matched monolithic control. Verified.
34. Zhao CM, Ruan H, Chen W, Tu P, Abbasi U, Hesch J. "Beyond Prompts: Measuring and Optimizing LLM Tool-Agent Harnesses." EMNLP 2026; arXiv:2609.05736. https://arxiv.org/abs/2609.05736. Supports: harness search can pick brittle updates and repeatability should be reported, which motivates replicates per cell. Verified.
35. Aider project. "Aider polyglot benchmark." 2024. https://aider.chat/2024/12/21/polyglot.html. Supports: the second-domain benchmark (225 Exercism problems, six languages) used by DGM and HGM. Verified.

Additional verified pages useful for the method section: the Qwen3-Coder-30B-A3B-Instruct model card (https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct; 30.5B total, 3.3B active, 256K native context), the Qwen3-VL-8B-Instruct model card (https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct), SWE-bench (Jimenez et al., ICLR 2024, https://arxiv.org/abs/2310.06770), tau2-bench (Barres et al., https://arxiv.org/abs/2506.07982), GEPA (Agrawal et al., ICLR 2026 oral, https://arxiv.org/abs/2507.19457), ELM (Lehman et al., https://arxiv.org/abs/2206.08896), Olausson et al. "Is Self-Repair a Silver Bullet for Code Generation?" (ICLR 2024, https://arxiv.org/abs/2306.09896), SemRep (Li et al., https://arxiv.org/abs/2603.13640), Mendel Goedel Machine (Liu et al., https://arxiv.org/abs/2608.07645), AIDE2 "Recursive self-improvement of AI research agents" (Srikanth et al., https://arxiv.org/abs/2609.26457), "An Empirical Study of Harness Design for Coding Agents" (Fan et al., https://arxiv.org/abs/2609.20804), "Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents" (Barbaste et al., https://arxiv.org/abs/2609.00006).

UNVERIFIED or caveated items:

- An "18.6 percentage point drop from variable renaming" attributed to The Code Barrier appeared only in a search snippet; the abstract page gives no such number. Do not quote it.
- A "6x performance gap" figure attributed to Meta-Harness appears only in secondary write-ups; do not quote it.
- DGM's exact parent-selection formula (Section C.2 of the paper) was not read; describe it only as "roughly proportional to score and inversely proportional to the number of code-editing children."
- Exact frontier proposer names and sizes beyond the Qwen models were not verified; fix them at registration.
