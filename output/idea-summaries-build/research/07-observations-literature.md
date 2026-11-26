# P07 Self-Designed Observations: literature and novelty check

Date of check: 2026-11-24. Every link in Sections 3 and 8 was opened during this check (arXiv abstract page, proceedings page, ACL Anthology page, or Crossref record). Items I could not open are marked UNVERIFIED in Section 9.

## 1. The idea under review

P07 asks how a vision-language model (VLM) agent should look at the numbers its own tools produce. In BioHarness the agent calls RTMPose, OpenCap Monocular and similar tools and gets back keypoint time series, center-of-mass (CoM) sway traces and joint angles. It can read those as printed numbers, as summary statistics, as plots, or as overlays drawn on video frames. P07 has two halves:

1. Measurement: which encoding gives the most accurate downstream decision per input token, tested with a Cleveland-McGill style graphical-perception battery for VLMs and with information-matched controls (a "pixel oracle" that bounds what the image contains).
2. Self-improvement: let the agent evolve its own rendering code (the program that turns tool output into an image), then ask whether the gains transfer to new tasks, other VLMs and human readers, or whether the search has found quirks of one model. A co-adaptation arm jointly fine-tunes the reader and evolves the renderer and asks whether the pair drifts into a private visual dialect.

For the novelty check I split P07 into six claims:

- C1. Plots beat printed numbers for VLM reasoning over time series, and they cost fewer tokens.
- C2. A Cleveland-McGill battery reveals how VLMs decode elementary visual encodings (position, length, angle, area, color).
- C3. Information-matched controls separate "the image lacks the information" from "the model fails to read it."
- C4. An agent can search over executable rendering code, with downstream decision accuracy as the fitness signal.
- C5. Evolved renderings can be tested for transfer to unseen tasks, other VLM families and human readers, which separates general perceptual gains from exploitation of one reader.
- C6. Jointly training the reader and evolving the renderer produces a reader-specific visual code that fresh models and humans cannot read (emergent-communication drift in the observation channel).

## 2. Search log

Twenty-six web searches were run, followed by targeted fetches of abstract pages. The main phrasings and what they returned:

| Query (paraphrased) | What came back |
|---|---|
| Plots unlock time-series understanding in multimodal models | Daswani et al. 2024 (arXiv 2410.02637), Google blog |
| graphical perception VLMs, Cleveland McGill | Nguyen et al. 2025 (PacificVis), Zhang et al. 2025 (arXiv 2503.10857), Cleveland and McGill 1984 |
| Vision language models are blind | Rahmanzadehgervi et al. (arXiv 2407.06581, ACCV 2024) |
| Visual Sketchpad; DeepEyes; PyVision; CodePlot-CoT | Hu et al. NeurIPS 2024; Zheng et al. 2025; Zhao et al. 2025; Duan et al. 2025 |
| time series as images, VLM time-series reasoning | VL-Time (NAACL 2025), Zhou and Yu (ICLR 2025), Xu et al. (WWW 2026), MLLM4TS, IJCAI 2025 survey, TimeMaster |
| visualization design choices and MLLM chart accuracy | EncQA (TVCG 2026), VLAT variants, Chartographer (EMNLP 2026), misleading-chart work |
| LLM evolves visualization code for a multimodal reader | Dubey et al. 2026 (arXiv 2610.35077, evolves the inference program, not the renderer), MatPlotAgent; no direct hit |
| visualization for machine readers | Keith-Norambuena 2026 "Toward a Machine Bertin" (position paper, no experiments) |
| automatic search over chart rendering parameters for VLMs | no direct hit; EncQA, Visual Self-Refine, Beyond Pixels (iPlotBench) |
| LLM table serialization format | Sui et al. WSDM 2024; Deng et al. Findings ACL 2024 (tables as text vs images) |
| tool output formatting for agents | Kutschka and Geiger 2026 "Notation Matters" (TOON/TRON in agent loops); SWE-agent ACI |
| visual prompting optimization, Set-of-Mark | SoM (arXiv 2310.11441), PIVOT, AutoV (ECCV 2026) |
| emergent communication drift, co-adaptation | Lazaridou et al. ACL 2020; Lee, Cho, Kiela EMNLP 2019; Rita et al. NeurIPS 2022; Mihai and Hare NeurIPS 2021 |
| Heer Bostock crowdsourcing graphical perception | Heer and Bostock CHI 2010 |
| VLM skeleton overlay pose reading, gait | BioGait-VLM (arXiv 2603.08564, skeleton as tokens), stroke-rehab VLM study (PLOS Digit Health 2026); no overlay study |
| VLMs as proxies for human chart readers | Verma et al. 2025/2026 (Sci. Rep.), several HCI preprints |
| sensor data visual prompting | By My Eyes (EMNLP 2024), eye-tracking HAR preprint |
| transfer of optimized images across VLMs | Schaeffer et al. ICLR 2025 |
| render text as image for token efficiency | DeepSeek-OCR (arXiv 2510.18234), critique arXiv 2512.03643 |
| two extended searches for "agent evolves its own plotting code for VLM accuracy, transfer to other models and humans" | no paper found that does this |

## 3. Closest prior work

### 3.1 Daswani et al. 2024, Plots Unlock Time-Series Understanding in Multimodal Models

- Citation: Mayank Daswani, Mathias M.J. Bellaiche, Marc Wilson, et al. (14 authors). arXiv:2410.02637, 2024.
- URL: https://arxiv.org/abs/2410.02637
- What they did: fed time series to GPT-4o, GPT-4o-mini, Gemini 1.5 Pro and Flash either as text or as plots. Plots improved zero-shot synthetic tasks by up to 120% and real consumer-health tasks (fall detection, activity recognition from IMU, readiness) by up to 150%, with up to 90% lower API cost.
- Overlap with P07: this is C1 on wearable data, which is close to BioHarness tool output.
- What remains open: the paper states "we do not rigorously study what the optimal plotted form of a certain time-series might be for visual understanding," reports that its plot ablations had no strong positive effect, and says choosing how and when to plot "could in theory be automated and forms the basis for future work." That is P07's C4, named as open by the authors.

### 3.2 Yoon et al. 2024, By My Eyes

- Citation: Hyungjun Yoon, Biniyam Aschalew Tolera, Taesik Gong, Kimin Lee, Sung-Ju Lee. "By My Eyes: Grounding Multimodal Large Language Models with Sensor Data via Visual Prompting." EMNLP 2024, pp. 2219-2241.
- URL: https://aclanthology.org/2024.emnlp-main.133/ (arXiv https://arxiv.org/abs/2407.10385)
- What they did: visual prompts for nine sensing tasks across four modalities, about 10% higher accuracy than text prompts and 15.8 times fewer tokens. They add a "visualization generator": the MLLM first filters a fixed menu of 16 plotting functions (Matplotlib, SciPy, NeuroKit2), every surviving function draws a plot, and the MLLM picks the plot it judges most useful. Main model GPT-4o; LLaVA-7B was near chance.
- Overlap with P07: the closest method to C4. It is an agent choosing its own visualization.
- What remains open: the choice is made by the model's self-judgment, with no labeled downstream fitness, and the search is a selection over 16 fixed functions instead of edits to rendering code. They report no cross-model transfer of the chosen plots, no human study, no information-matched control, and no co-adaptation. Their stated limitations include weak performance on exact numeric retrieval and an unresolved split of information between image and text.

### 3.3 Liu, Liu and Prakash 2025, VL-Time and TimerBed

- Citation: Haoxin Liu, Chenghao Liu, B. Aditya Prakash. "A Picture is Worth A Thousand Numbers: Enabling LLMs Reason about Time Series via Visualization." NAACL 2025, pp. 7486-7518.
- URL: https://aclanthology.org/2025.naacl-long.383/ (arXiv https://arxiv.org/abs/2411.06018)
- What they did: built TimerBed (real-world time-series classification tasks with zero-shot and in-context settings) and VL-Time, a prompt method that plots the series for a multimodal LLM. About 140% average improvement and 99% average token reduction versus numeric prompts. They locate the failure of text prompts in numeric encoding.
- Overlap: C1, and TimerBed is a usable second domain.
- Open: plot design is hand-chosen; no search, transfer or human evaluation.

### 3.4 Zhou and Yu 2025, Can LLMs Understand Time Series Anomalies?

- Citation: Zihao Zhou, Rose Yu. ICLR 2025.
- URL: https://proceedings.iclr.cc/paper_files/paper/2025/hash/05774fb74e863308c4b460c9f49f6918-Abstract-Conference.html
- What they did: controlled synthetic anomaly benchmark. LLMs "understand time series better as images rather than as text," do better with fewer tokens even at some information loss, and vary strongly across models.
- Overlap: C1, and the across-model variation is direct motivation for C5.
- Open: no search over encodings; the model-to-model variation is reported but not explained or exploited.

### 3.5 Nguyen et al. 2025, Evaluating Graphical Perception with Multimodal LLMs (and Haehn et al. 2019 for CNNs)

- Citation: Rami Huu Nguyen, Kenichi Maeda, Mahsa Geshvadi, Daniel Haehn. IEEE PacificVis 2025. arXiv:2504.04221.
- URL: https://arxiv.org/abs/2504.04221
- What they did: reproduced the Cleveland and McGill 1984 experiments with GPT-4o, Gemini 1.5 Flash, Gemini 1.0 Pro Vision and Llama 3.2-Vision (pretrained and fine-tuned), and compared with the human baseline. Models beat humans on some tasks (bar and pie) and not others (angle).
- Predecessor: Daniel Haehn, James Tompkin, Hanspeter Pfister. "Evaluating 'Graphical Perception' with CNNs." IEEE TVCG 25(1):641-650, 2019 (DOI https://doi.org/10.1109/TVCG.2018.2865138), the same replication for CNNs.
- Overlap: this is C2. A Cleveland-McGill battery for VLMs exists.
- Open: these batteries are descriptive. Nobody has used a reader's elementary-perception profile to predict which rendering will work for it, or whether a rendering optimized for one reader will work for another.

### 3.6 Mukherjee et al. 2026, EncQA

- Citation: Kushin Mukherjee, Donghao Ren, Dominik Moritz, Yannick Assogba. "EncQA: Benchmarking Vision-Language Models on Visual Encodings for Charts." IEEE TVCG 32(1), 2026. arXiv:2508.04650.
- URL: https://arxiv.org/abs/2508.04650 (DOI 10.1109/TVCG.2025.3634249, confirmed through Crossref)
- What they did: 2,076 synthetic questions crossing six encodings (position, length, area, quantitative color, nominal color, shape) with eight analytic tasks; nine VLMs. Accuracy varies across encodings within a task, and "performance does not improve with model size for many task-encoding pairs."
- Overlap: C2 in a systematic, encoding-by-task design.
- Open: evaluation only. It shows that the best encoding depends on the reader and task, which is the premise of C4 and C5, but does not search or test transfer.

### 3.7 Zhang et al. 2025, Towards Understanding Graphical Perception in Large Multimodal Models

- Citation: Kai Zhang, Jianwei Yang, Jeevana Priya Inala, Chandan Singh, Jianfeng Gao, Yu Su, Chenglong Wang. arXiv:2503.10857, 2025 (work in progress).
- URL: https://arxiv.org/abs/2503.10857
- What they did: an automated graphical-perception evaluation at chart, element and pixel levels. GPT-4o and others fail to generalize across chart types, misread basic visual elements, and struggle to cross-reference values.
- Overlap: C2.
- Open: same as above, diagnosis without design.

### 3.8 Keith-Norambuena 2026, Toward a Machine Bertin

- Citation: Brian Keith-Norambuena. "Toward a Machine Bertin: Why Visualization Needs Design Principles for Machine Cognition." arXiv:2602.01527, 2026 (comments: submitted to IEEE TVCG).
- URL: https://arxiv.org/abs/2602.01527
- What they did: a position paper. It synthesizes VLM benchmark evidence that human design rules do not carry over to machine readers, notes the common workaround of converting charts to tables or text, and calls for a research agenda on machine-oriented visualization.
- Overlap: states the motivation of P07 almost word for word.
- Open: no experiments, no search procedure, no transfer test. This paper raises the novelty bar for framing (P07 cannot claim to be first to ask the question) and lowers it for execution (nobody has answered it empirically).

### 3.9 Verma et al. 2025/2026, Human-centered evaluation of data visualization understanding in VLMs

- Citation: Arnav Verma, Kushin Mukherjee, Christopher Potts, Elisa Kreiss, Judith E. Fan. arXiv:2505.17202; journal reference Scientific Reports (2026).
- URL: https://arxiv.org/abs/2505.17202
- What they did: compared eight VLMs with humans item by item on five human visualization-literacy tests plus one VLM test. Models underperform humans; item difficulty correlates somewhat between models and humans; error patterns differ reliably.
- Overlap: gives the protocol and the prior expectation for C5's human-transfer arm.
- Open: fixed human-designed charts only; it does not ask whether optimizing a chart for a model moves it toward or away from human readability.

### 3.10 Zhang et al. 2025/2026, AutoV

- Citation: Yuan Zhang et al. (9 authors). "AutoV: Loss-Oriented Ranking for Visual Prompt Retrieval in LVLMs." arXiv:2506.16112; accepted to ECCV 2026.
- URL: https://arxiv.org/abs/2506.16112
- What they did: a ranker picks the best visual prompt (for example an attention heatmap overlay) from a candidate pool for each image and query. Labels come from the prediction loss of a pretrained LVLM. Gains include 10.2% for LLaVA-OV on VizWiz and 3.8% for Qwen2.5-VL on MMMU.
- Overlap: learned, reader-loss-driven choice of what to draw on the image, which is C4 for natural images.
- Open: retrieval from a fixed pool, natural-image QA, and no measurement of whether the chosen prompts are model-specific or legible to people.

### 3.11 Dubey et al. 2026, Improving VLMs on Scientific Chart Analysis via Autonomous Evolution

- Citation: Abhinav Sudhakar Dubey, Vidushi Goel, Kiran Rana, Shikhar Mathur, Vaggos Chatziafratis. arXiv:2610.35077, October 2026.
- URL: https://arxiv.org/abs/2610.35077
- What they did: froze the VLM and ran LLM-driven evolution over the inference program around it, scored on training accuracy, for chart question answering. Exact-match accuracy on descriptive questions rose from 16.6% to 41.3% on average across three VLMs and four benchmarks.
- Overlap: the same optimizer family P07 would use (code evolution with downstream fitness, frozen reader).
- Open: the chart is fixed input. The paper evolves how the model is queried, not what the model is shown, and the abstract reports no cross-reader or human transfer.

### 3.12 MatPlotAgent (Yang et al. 2024)

- Citation: Zhiyu Yang, Zihan Zhou, Shuo Wang, et al. (13 authors). "MatPlotAgent: Method and Evaluation for LLM-Based Agentic Scientific Data Visualization." Findings of ACL 2024, pp. 11789-11804.
- URL: https://aclanthology.org/2024.findings-acl.701/
- What they did: a code agent writes plotting code and a multimodal "visual agent" inspects the rendered figure and requests fixes; MatPlotBench scores plots with GPT-4V.
- Overlap: VLM-in-the-loop refinement of plotting code.
- Open: the target is fidelity to a human's request. Nobody downstream makes a decision from the plot, so there is no task fitness and no transfer question.

### 3.13 Mihai and Hare 2021, Learning to Draw: Emergent Communication through Sketching (with the language-drift line)

- Citation: Daniela Mihai, Jonathon Hare. NeurIPS 2021.
- URL: https://proceedings.neurips.cc/paper_files/paper/2021/hash/39d0a8908fbe6c18039ea8227f827023-Abstract.html
- What they did: a sender draws strokes and a receiver picks the matching photo. Trained on game reward alone, the sketches are not human-decipherable; with suitable inductive biases (reported in summaries as a perceptual loss) humans can read them at little cost to game success.
- Companion work: Lee, Cho, Kiela, "Countering Language Drift via Visual Grounding," EMNLP 2019 (https://arxiv.org/abs/1909.04499); Lazaridou, Potapenko, Tieleman, ACL 2020 (https://arxiv.org/abs/2005.07064), with a taxonomy of drift types and detection measures; Rita et al., NeurIPS 2022 (https://proceedings.neurips.cc/paper_files/paper/2022/hash/093b08a7ad6e6dd8d34b9cc86bb5f07c-Abstract-Conference.html), which splits the Lewis-game loss into an information term and a co-adaptation term.
- Overlap: this is C6 in a toy referential game. It is strong prior evidence that co-adaptation will drift the visual channel unless constrained.
- Open: none of these use a pretrained VLM reader, executable rendering programs, measurement data with real consequences, or a self-improvement loop. Whether drift appears when the sender is code written by an LLM and the receiver starts from a broadly pretrained VLM is unknown. It is a different regime: a strong pretrained prior may resist drift, or the fine-tuned reader may lose that prior quickly.

### 3.14 Related groups that bound the claim

- Agents that draw for themselves at inference time: Visual Sketchpad (Hu et al., NeurIPS 2024), PyVision (Zhao et al., arXiv 2507.07998), CodePlot-CoT (Duan et al., arXiv 2510.11718), DeepEyes (Zheng et al., arXiv 2505.14362). They show that self-generated images help, but each image is made per instance and judged only by the final answer. None of them optimizes a reusable renderer or tests who else can read its output.
- Transfer of optimized images: Schaeffer et al., ICLR 2025 (https://arxiv.org/abs/2407.15211) found gradient-optimized image jailbreaks against 40+ VLMs show little or no transfer, except between near-identical models, and that ensembles of highly similar models helped transfer to a similar target. Pixel-level optimization is a much stronger attack surface than rendering code, but the result is the right null to test against.
- Text-side encoding: Sui et al. WSDM 2024 (table serialization), Deng et al. Findings ACL 2024 (same tables as text or images), Wang et al. NeurIPS 2024 SpatialEval (VLMs often do worse than their text-only LLM counterparts and lean on text when both are given), Kutschka and Geiger 2026 "Notation Matters" (token savings and accuracy of compact formats depend on the model and on where the format is applied), Gruver et al. NeurIPS 2023 (number tokenization).
- Biomechanics specifically: Li et al. (PLOS Digital Health 2026) found current VLMs lack the fine-grained motion understanding needed for quantification in stroke rehabilitation video; BioGait-VLM (arXiv 2603.08564) feeds skeletons as tokens. I found no study of skeleton or sway overlays as VLM observations.

## 4. Is it already done?

Partially. The measurement half of P07 (C1 to C3) is largely done; the self-improvement half (C4 to C6) is open.

- C1 (plots beat numbers, fewer tokens) is established for wearable and generic time series by Daswani et al., By My Eyes, VL-Time and Zhou and Yu, with counter-evidence in spatial reasoning (SpatialEval) and fine-grained numeric retrieval (By My Eyes limitations). Repeating it on keypoints and CoM sway would be an application result.
- C2 (Cleveland-McGill battery for VLMs) is done by Nguyen et al. 2025, with EncQA and Zhang et al. covering the encoding-by-task grid and Haehn et al. 2019 covering CNNs.
- C3 (information-matched controls) is partly done. SpatialEval and Deng et al. give the same content as text or image; the probes in "VLMs are blind" indicate that information present in the vision encoder is not read out; Beyond Pixels (arXiv 2604.21134) compares pixel reading against querying the chart specification. A pixel-oracle bound for plots of tool output has not been reported, but the idea is familiar.
- C4 (search over rendering code with downstream fitness) is open in the strict sense. By My Eyes selects from a fixed menu by self-judgment, AutoV retrieves from a pool for natural images, MatPlotAgent refines for human intent, and Dubey et al. evolve the inference program around a fixed chart. Daswani et al. name the automation of plot choice as future work.
- C5 (transfer of evolved renderings to other readers, tasks and humans) is open. I found no paper that optimizes a visualization for one VLM and measures how much of the gain survives on other VLM families or on people. The Machine Bertin position paper asks for this agenda and runs no experiment.
- C6 (co-adaptation drift of a visual code between an LLM-written renderer and a fine-tuned VLM reader) is open for pretrained VLMs. The toy-game literature predicts drift and offers fixes (perceptual loss, grounding).

## 5. Residual gap

The open question, stated so a reviewer cannot collapse it into prior work: when an agent optimizes the program that renders its own tool outputs, how is the resulting gain divided among (a) computation the renderer does on the numbers (deriving a feature and drawing it), (b) perceptual improvements that any competent reader, model or human, can use, and (c) exploitation of the specific reader the search was scored against; and does jointly adapting the reader move gain from (b) into (c) while the pair's own accuracy keeps rising?

No paper measures this decomposition or the trajectory of the reader-specific share during optimization. The closest pieces (By My Eyes for agent-chosen plots, Schaeffer et al. for non-transfer of optimized images, Mihai and Hare for drift under co-adaptation, Verma et al. for human-model comparison) each cover one corner.

## 6. Scores

Scored as a demanding ICML area chair.

- Novelty as currently written: 3.5 out of 5. Two of the three headline components (the encoding comparison and the Cleveland-McGill battery) are published, and the motivation has a 2026 position paper. A reviewer who reads the abstract will see "plots versus text for time series, again" unless the self-improvement and transfer parts lead. The renderer-evolution, transfer-decomposition and co-adaptation pieces are new as far as this search could find.
- Novelty if sharpened as in Section 7 (decomposition plus drift as the thesis, measurement as calibration): about 4 to 4.5. The question "who else can read the observations a self-improving agent designs for itself" has no empirical answer in the literature and ties to recursive self-improvement and oversight.
- Significance: 3.5 out of 5 as written, 4 if sharpened. Agents that write their own tools and views (PyVision, Sketchpad, CodePlot-CoT, code-evolution systems) are spreading, so whether their self-made observation channels stay legible to people and to other models matters for monitoring and for reuse across models. The biomechanics test bed adds a setting where a clinician must be able to read the same plot. The main risk to significance is a null result that looks like ordinary prompt overfitting, or a positive result that reduces to "the renderer printed the answer-relevant statistic in large type." Both are addressed by controls in Section 7.

## 7. Sharpenings

### 7.1 Reframed thesis

One sentence: when an agent evolves the code that renders its own tool outputs, the gain splits into computation, shared perception and reader-specific exploitation, and the reader-specific share grows with optimization pressure and with co-adaptation of the reader; scoring against several dissimilar readers keeps the gain legible to new models and to people.

The Cleveland-McGill battery moves from contribution to instrument: each reader's elementary-perception profile is measured once and used to predict which evolved renderings will transfer to it. That use is new; the battery itself is not.

### 7.2 The single most decisive experiment

A transfer-decomposition curve along the evolution trajectory, with equal-budget arms.

1. Fix the tool outputs: for each StaBLE recording, RTMPose 2D keypoints, OpenCap Monocular joint angles and a CoM sway trace. Fix the decision: the clinical balance score, scored by MAE on held-out people (the pilot's 43 test people).
2. Run LLM-driven code evolution (AlphaEvolve-style, with GEPA-style reflection on failures) over a matplotlib renderer. Fitness is downstream MAE of a frozen reader A (Qwen3-VL-8B-Instruct) on a development split of training people. Save every surviving renderer with its generation index.
3. Run three fitness conditions with equal evaluation budgets: single reader A; an ensemble of readers from different families (A plus InternVL3.5 and Gemma 3 at similar size); and the ensemble plus a human-proxy legibility term (accuracy of a reader that never takes part in the search, or a small crowd panel at a few checkpoints).
4. Run an equal-budget evolved text summarizer: the same optimizer writes code that turns tool output into text (statistics, short tables), read by the same reader A. This arm isolates computation.
5. For each saved renderer, evaluate on held-out people with: reader A; held-out readers B and C from families not used in any fitness; one closed frontier VLM; and human readers on a perceptual readout version of the task (for example, "which of these two trials shows more sway?" and a 0 to 4 rating), following the crowdsourcing protocol of Heer and Bostock 2010.
6. Plot, against generation index, the gain on A, the gain on each held-out reader, and the human gain. The quantity of interest is the transfer ratio, gain on B divided by gain on A, and how it changes as search continues.

The hypothesis predicts that the ratio starts near 1 (early edits are shared perceptual fixes such as aligned scales, less clutter, a drawn sway envelope) and falls with generations under single-reader fitness, while ensemble fitness keeps it near 1 at a small cost in A's gain.

Co-adaptation arm: alternate renderer evolution with LoRA fine-tuning (SFT, then GRPO) of reader A on the current renderings for k rounds. Measure the pair's accuracy, fresh-reader accuracy on the same renderings, and human accuracy. Drift is the gap between the co-adapted pair and fresh readers or humans while the pair's accuracy holds or rises. Add the fix suggested by the drift literature (a frozen-reader or human-proxy legibility term, in the spirit of the inductive bias in Mihai and Hare and the grounding in Lee et al.) and test whether it closes the gap.

### 7.3 Essential controls

- Computation versus perception. The evolved renderer can compute a feature and write it as text inside the image, which turns the task into OCR. Three checks: the equal-budget evolved text summarizer (Section 7.2 step 4); a "no glyphs" variant where the renderer may not draw text beyond axis ticks; and a measured OCR fraction (how much of each rendering a separate OCR model can read out as numbers). Report gains with and without glyphs.
- Pixel oracle. Train a small supervised decoder (a CNN, or a linear probe on reader A's frozen vision features, following the probing in Rahmanzadehgervi et al.) on each rendering to predict the label. Its accuracy bounds what the image contains. The gap between oracle and reader is the reading failure. An evolved renderer can raise reader accuracy by closing that gap or by adding information, and the two must be reported separately.
- Token matching. Equalize visual tokens (resolution and image count) against text tokens across arms and report accuracy per thousand input tokens.
- Rendered text. Render the printed numbers as an image (the DeepSeek-OCR style of compression) to separate the modality change from graphical encoding.
- Search controls. Random search over the same rendering parameter space; hand-designed expert plots (standard stabilogram and sway-path plots); several independent evolution seeds.
- Leakage. Fitness and reflection see only development people; held-out people, held-out StaBLE tasks and held-out readers are never scored during search. This also keeps P07 separate from P06's trace-leakage question.
- Reader ablation. Fine-tune the reader on fixed hand-designed plots at equal compute (TimeMaster-style RL) to compare changing the observation with changing the reader.

### 7.4 Strongest baselines

- Printed numbers with LLMTime-style serialization: Gruver et al., NeurIPS 2023, https://arxiv.org/abs/2310.07820
- Fixed plots, zero-shot and few-shot: Daswani et al., https://arxiv.org/abs/2410.02637 ; VL-Time, https://aclanthology.org/2025.naacl-long.383/
- Agent-selected visualization from a fixed menu by self-judgment: By My Eyes, https://aclanthology.org/2024.emnlp-main.133/
- Visual-feedback refinement of plotting code: MatPlotAgent, https://aclanthology.org/2024.findings-acl.701/
- Reader-loss-ranked visual prompt retrieval: AutoV, https://arxiv.org/abs/2506.16112
- Overlays on frames: Set-of-Mark prompting, https://arxiv.org/abs/2310.11441 (adapted to keypoints and joint labels)
- Per-instance self-drawing at inference: Visual Sketchpad, https://proceedings.neurips.cc/paper_files/paper/2024/hash/fb82011040977c7712409fbdb5456647-Abstract-Conference.html ; PyVision, https://arxiv.org/abs/2507.07998
- Evolving the inference program instead of the renderer: Dubey et al., https://arxiv.org/abs/2610.35077
- Text-prompt optimization at equal budget: GEPA, https://arxiv.org/abs/2507.19457
- Reader-side RL on plots: TimeMaster, https://arxiv.org/abs/2506.13705
- Optimizer: AlphaEvolve-style code evolution, https://arxiv.org/abs/2506.13131

### 7.5 Models

- Primary reader A: Qwen3-VL-8B-Instruct (the pilot model). Qwen3-VL family sizes confirmed in the technical report: dense 2B, 4B, 8B, 32B; MoE 30B-A3B and 235B-A22B (https://arxiv.org/abs/2511.21631). Use 2B, 8B and 32B to test whether reader-specific exploitation shrinks with scale within a family.
- Held-out open readers from other families: InternVL3.5 (technical report https://arxiv.org/abs/2508.18265; flagship 241B-A28B confirmed, smaller sizes UNVERIFIED in this check) and Gemma 3 at a size near 12B (UNVERIFIED in this check). Keep at least one family out of every fitness ensemble.
- One closed frontier VLM as a held-out reader (whichever current GPT, Gemini or Claude release the lab can call; exact model IDs to be fixed at run time).
- Rewriting LLM for evolution: a strong code model, held fixed across arms.

### 7.6 Environments

- Biomechanics: StaBLE (180 people, 18 balance tasks, 3 phones; pilot split 171 people, 2,968 usable single-camera examples, 43 test people). Use held-out StaBLE tasks to test task transfer of renderers. BioCV (15 participants with synchronized cameras, markers and force plates) gives force-plate CoM as ground truth, which supports the pixel oracle and lets the human study use physically correct reference traces.
- Second, non-biomechanics domain: TimerBed from VL-Time (real-world time-series classification with public code and existing Qwen2.5-VL results through TimeMaster) for the main replication, and the synthetic anomaly suite of Zhou and Yu (ICLR 2025) for controlled tests where the generating process is known. The By My Eyes sensing tasks are a third option. For a domain further from time series, EncQA's synthetic charts give a setting where the underlying data are fully known.

### 7.7 Metrics

- Decision quality: task-averaged MAE on StaBLE (pilot references: training-task mean 0.120, RTMPose+TCN 0.119, frozen Qwen3-VL-8B 0.238, SFT Qwen 0.100, OpenCap Monocular 0.146); accuracy or macro-F1 on TimerBed.
- Efficiency: accuracy per thousand input tokens; wall-clock and API cost.
- Transfer ratio T(B given A) = gain on B divided by gain on A, per generation, with bootstrap intervals over people. Reader-specific share = 1 minus the mean T over held-out readers.
- Computation share = gain of the evolved text summarizer divided by gain of the evolved renderer, at equal budget.
- Pixel-oracle gap = oracle accuracy minus reader accuracy.
- OCR fraction of each rendering.
- Human: accuracy and response time on the perceptual readout, and clinician agreement on a small panel.
- Drift (co-adaptation arm): co-adapted pair accuracy minus fresh-reader accuracy, and minus human accuracy, on the same renderings.
- Predictive use of the battery: rank correlation between a reader's Cleveland-McGill error profile (on the encodings a renderer uses) and that renderer's transfer ratio to the reader.

### 7.8 What would falsify the hypothesis

- If the equal-budget evolved text summarizer matches the evolved renderer, and the no-glyph renderer gains nothing over the best hand-designed plot, then the gain is computation and the "self-designed observation" claim reduces to feature engineering.
- If the transfer ratio stays near 1 across all generations under single-reader fitness, and co-adaptation leaves fresh-reader and human accuracy unchanged, then optimization pressure does not create reader-specific codes in this regime. That would be a publishable negative that contradicts the extrapolation from emergent-communication games and from Schaeffer et al., but it removes the drift claim.
- If even early-generation gains fail to transfer to any held-out reader or to humans, the search is fitting one reader from the start, and ensemble fitness has to be shown to fix it before the method can be recommended.

## 8. Key citations

All links below were opened during this check.

1. Daswani M., Bellaiche M.M.J., Wilson M., et al. "Plots Unlock Time-Series Understanding in Multimodal Models." arXiv:2410.02637, 2024. https://arxiv.org/abs/2410.02637. Supports: plots beat text on time series with up to 90% lower cost; the authors leave plot design and its automation open.
2. Yoon H., Tolera B.A., Gong T., Lee K., Lee S.-J. "By My Eyes: Grounding Multimodal Large Language Models with Sensor Data via Visual Prompting." EMNLP 2024, pp. 2219-2241. https://aclanthology.org/2024.emnlp-main.133/. Supports: about 10% accuracy gain and 15.8 times fewer tokens with visual prompts; closest prior agent-chosen visualization (fixed menu, self-judgment, no transfer test).
3. Liu H., Liu C., Prakash B.A. "A Picture is Worth A Thousand Numbers: Enabling LLMs Reason about Time Series via Visualization." NAACL 2025, pp. 7486-7518. https://aclanthology.org/2025.naacl-long.383/. Supports: about 140% average improvement and 99% token reduction; TimerBed as second domain.
4. Zhou Z., Yu R. "Can LLMs Understand Time Series Anomalies?" ICLR 2025. https://proceedings.iclr.cc/paper_files/paper/2025/hash/05774fb74e863308c4b460c9f49f6918-Abstract-Conference.html. Supports: images beat text for anomaly detection; strong model-to-model variation.
5. Cleveland W.S., McGill R. "Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods." Journal of the American Statistical Association 79(387):531-554, 1984. https://doi.org/10.1080/01621459.1984.10478080 (metadata confirmed through Crossref). Supports: the elementary perceptual task ranking used for the battery.
6. Heer J., Bostock M. "Crowdsourcing Graphical Perception: Using Mechanical Turk to Assess Visualization Design." CHI 2010, pp. 203-212. https://doi.org/10.1145/1753326.1753357 (also https://idl.uw.edu/papers/crowdsourcing-graphical-perception). Supports: the human-reader protocol.
7. Haehn D., Tompkin J., Pfister H. "Evaluating 'Graphical Perception' with CNNs." IEEE TVCG 25(1):641-650, 2019. https://doi.org/10.1109/TVCG.2018.2865138 (metadata confirmed through Crossref). Supports: Cleveland-McGill replication for neural readers predates VLMs.
8. Nguyen R.H., Maeda K., Geshvadi M., Haehn D. "Evaluating Graphical Perception with Multimodal LLMs." IEEE PacificVis 2025. https://arxiv.org/abs/2504.04221. Supports: a Cleveland-McGill battery for MLLMs already exists.
9. Mukherjee K., Ren D., Moritz D., Assogba Y. "EncQA: Benchmarking Vision-Language Models on Visual Encodings for Charts." IEEE TVCG 32(1), 2026. https://arxiv.org/abs/2508.04650. Supports: the best encoding depends on reader and task; model size does not fix many encoding-task pairs.
10. Zhang K., Yang J., Inala J.P., Singh C., Gao J., Su Y., Wang C. "Towards Understanding Graphical Perception in Large Multimodal Models." arXiv:2503.10857, 2025. https://arxiv.org/abs/2503.10857. Supports: LMMs fail on perception-only chart tasks.
11. Keith-Norambuena B. "Toward a Machine Bertin: Why Visualization Needs Design Principles for Machine Cognition." arXiv:2602.01527, 2026. https://arxiv.org/abs/2602.01527. Supports: the machine-oriented visualization question is posed but untested.
12. Verma A., Mukherjee K., Potts C., Kreiss E., Fan J.E. "Human-centered evaluation of data visualization understanding in vision-language models." arXiv:2505.17202; Scientific Reports 2026. https://arxiv.org/abs/2505.17202. Supports: VLM and human error patterns differ; protocol for item-level human comparison.
13. Rahmanzadehgervi P., Bolton L., Taesiri M.R., Nguyen A.T. "Vision language models are blind: Failing to translate detailed visual features into words." arXiv:2407.06581. https://arxiv.org/abs/2407.06581. Supports: 58.07% average on trivial visual tasks; probes indicate information present in the encoder is not read out (motivates the pixel oracle).
14. Wang J., Ming Y., Shi Z., Vineet V., Wang X., Li Y., Joshi N. "Is A Picture Worth A Thousand Words? Delving Into Spatial Reasoning for Vision Language Models." NeurIPS 2024. https://proceedings.neurips.cc/paper_files/paper/2024/hash/89cc5e613d34f90de90c21e996e60b30-Abstract-Conference.html. Supports: information-matched text versus image comparison; VLMs often trail text-only LLMs.
15. Deng N., Sun Z., He R., Sikka A., Chen Y., Ma L., Zhang Y., Mihalcea R. "Tables as Texts or Images: Evaluating the Table Reasoning Ability of LLMs and MLLMs." Findings of ACL 2024, pp. 407-426. https://aclanthology.org/2024.findings-acl.23/. Supports: same content as text or image; representation and prompting both matter.
16. Kutschka L., Geiger B. "Notation Matters: A Benchmark Study of Token-Optimized Formats in Agentic AI Systems." arXiv:2605.29676, 2026. https://arxiv.org/abs/2605.29676. Supports: in agent loops, the savings and accuracy cost of compact formats depend on the model and where the format is applied, so encoding gains are reader-dependent even in text.
17. Zhang Y., et al. "AutoV: Loss-Oriented Ranking for Visual Prompt Retrieval in LVLMs." ECCV 2026. https://arxiv.org/abs/2506.16112. Supports: reader-loss-driven choice of visual prompts improves LVLMs.
18. Dubey A.S., Goel V., Rana K., Mathur S., Chatziafratis V. "Improving VLMs on Scientific Chart Analysis via Autonomous Evolution." arXiv:2610.35077, 2026. https://arxiv.org/abs/2610.35077. Supports: LLM-driven evolution around a frozen VLM gives large chart-QA gains; the renderer itself was not evolved.
19. Yang Z., Zhou Z., Wang S., et al. "MatPlotAgent: Method and Evaluation for LLM-Based Agentic Scientific Data Visualization." Findings of ACL 2024, pp. 11789-11804. https://aclanthology.org/2024.findings-acl.701/. Supports: VLM visual feedback improves plotting code for human intent.
20. Hu Y., Shi W., Fu X., Roth D., Ostendorf M., Zettlemoyer L., Smith N.A., Krishna R. "Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models." NeurIPS 2024. https://proceedings.neurips.cc/paper_files/paper/2024/hash/fb82011040977c7712409fbdb5456647-Abstract-Conference.html. Supports: self-drawn intermediate images help multimodal reasoning.
21. Zhao S., et al. "PyVision: Agentic Vision with Dynamic Tooling." arXiv:2507.07998, 2025. https://arxiv.org/abs/2507.07998. Supports: MLLMs writing their own visual tools at inference (GPT-4.1, Claude-4.0-Sonnet).
22. Schaeffer R., et al. "Failures to Find Transferable Image Jailbreaks Between Vision-Language Models." ICLR 2025. https://arxiv.org/abs/2407.15211 (venue confirmed at https://mlanthology.org/iclr/2025/schaeffer2025iclr-failures/). Supports: images optimized against one VLM rarely transfer, except between near-identical models; ensembles help only for similar targets.
23. Mihai D., Hare J. "Learning to Draw: Emergent Communication through Sketching." NeurIPS 2021. https://proceedings.neurips.cc/paper_files/paper/2021/hash/39d0a8908fbe6c18039ea8227f827023-Abstract.html. Supports: drawings optimized only for a partner's success are not human-readable without an added inductive bias.
24. Lee J., Cho K., Kiela D. "Countering Language Drift via Visual Grounding." EMNLP 2019. https://arxiv.org/abs/1909.04499. Supports: reward-only fine-tuning drifts away from natural language; grounding plus a language-model constraint counters it.
25. Rita M., Tallec C., Michel P., Grill J.-B., Pietquin O., Dupoux E., Strub F. "Emergent Communication: Generalization and Overfitting in Lewis Games." NeurIPS 2022. https://proceedings.neurips.cc/paper_files/paper/2022/hash/093b08a7ad6e6dd8d34b9cc86bb5f07c-Abstract-Conference.html. Supports: co-adaptation overfitting is a distinct loss term that can be controlled.

Additional verified references used in the text: Lazaridou A., Potapenko A., Tieleman O., ACL 2020, https://arxiv.org/abs/2005.07064 (drift taxonomy and detection); Yang J. et al., SWE-agent, NeurIPS 2024, https://proceedings.neurips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html (interface design changes agent performance); Gruver N. et al., NeurIPS 2023, https://arxiv.org/abs/2310.07820 (number tokenization); Agrawal L.A. et al., GEPA, ICLR 2026, https://arxiv.org/abs/2507.19457; Novikov A. et al., AlphaEvolve, https://arxiv.org/abs/2506.13131; Zhang J. et al., TimeMaster, https://arxiv.org/abs/2506.13705; Xu X. et al., VisualTimeAnomaly, WWW 2026, https://arxiv.org/abs/2502.17812; Ni J. et al., IJCAI 2025 survey, https://www.ijcai.org/proceedings/2025/1178; Wang Z. et al., CharXiv, NeurIPS 2024 D&B, https://proceedings.neurips.cc/paper_files/paper/2024/hash/cdf6f8e9fd9aeaf79b6024caec24f15b-Abstract-Datasets_and_Benchmarks_Track.html; Yang J. et al., Set-of-Mark, https://arxiv.org/abs/2310.11441; Zheng Z. et al., DeepEyes, https://arxiv.org/abs/2505.14362; Duan C. et al., CodePlot-CoT, https://arxiv.org/abs/2510.11718; Liu Q. et al., MLLM4TS, https://arxiv.org/abs/2510.07513; Lu Y. et al., Beyond Pixels / iPlotBench, https://arxiv.org/abs/2604.21134; Jiang Y. et al., Chartographer, EMNLP 2026, https://arxiv.org/abs/2605.27311; Wei H. et al., DeepSeek-OCR, https://arxiv.org/abs/2510.18234; Lee I.Y., Yang C., Berg-Kirkpatrick T., https://arxiv.org/abs/2512.03643 (critique of optical compression); Li V. et al., VLMs for stroke rehabilitation, PLOS Digital Health 5(7):e0001506, 2026, https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0001506 (also arXiv 2511.17727); Chen E. et al., BioGait-VLM, https://arxiv.org/abs/2603.08564 (skeletons as tokens, not overlays); Sui Y. et al., Table Meets LLM, WSDM 2024, https://arxiv.org/abs/2305.13062; Qwen Team, Qwen3-VL Technical Report, https://arxiv.org/abs/2511.21631; InternVL3.5, https://arxiv.org/abs/2508.18265.

## 9. Unverified items

- Venue of Daswani et al. 2410.02637: an OpenReview forum exists (https://openreview.net/forum?id=HkB4bW5eJj) but the page was blocked by a browser check, so the decision is UNVERIFIED. Treat it as an arXiv preprint.
- The claim that Set-of-Mark prompting lowers accuracy for LLaVA-style models comes from search snippets about Wan et al. (Contrastive Region Guidance, arXiv 2403.02325); it is not in that paper's abstract. UNVERIFIED, not used as evidence above.
- The perceptual-loss mechanism in Mihai and Hare 2021 comes from search summaries; the abstract says only "with appropriate inductive biases." Treat the specific loss as UNVERIFIED until the paper body is checked.
- Smaller InternVL3.5 sizes and Gemma 3 sizes were not confirmed in this check. UNVERIFIED.
- The CVF page for "VLMs are blind" (ACCV 2024) returned HTTP 403; the arXiv page was verified, and the ACCV venue comes from search results. UNVERIFIED venue.
- Glyph (Z.ai, visual-text compression) appeared only in secondary sources and is not cited.
