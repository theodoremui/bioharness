# Brief for proposal 07: can a vision-language agent learn how to look at its own data?

Output file: `docs/idea-summaries/07-learning-how-to-look-at-tool-outputs.md`. Figures: `docs/idea-summaries/images/07/`. Figure code: `output/idea-summaries-build/figs_07.py`.

## Core question

When a VLM agent receives numeric tool outputs (keypoint time series, center-of-mass sway, joint angles), which encodings let it make accurate decisions per token spent? Can the agent improve its own rendering code so the gains transfer to new tasks, to other VLMs and to human readers, instead of exploiting quirks of one model?

One-line thesis: how a tool's output is shown to a multimodal agent is itself a learnable action, and the best encoding for a VLM need not be the best for a person.

## Why it is open

Tool-using VLM agents (VisProg, ViperGPT, Visual Sketchpad, DeepEyes and "thinking with images") call perception tools and then read their outputs, usually serialized as text or JSON. Numbers are expensive and poorly read as tokens; "Plots unlock time-series understanding in multimodal models" (Daswani et al. 2024) found plots beat text for time-series reasoning; "Vision language models are blind" shows failures on simple geometric perception. Human graphical perception has a well-established ranking (Cleveland and McGill 1984; Heer and Bostock 2010 replication): position on a common scale beats length, angle, area and color. Missing: (1) information-matched tests that separate what an encoding discards from what the model fails to perceive, on agent-relevant data; (2) a closed loop in which the agent optimizes its own observation interface; (3) tests of whether the optimized encodings are general or model-specific. Check the literature report and state the residual gap precisely.

## Running biomechanics example

A 30-second StaBLE tandem-stance trial at 30 fps gives 900 frames x 17 keypoints x 2 coordinates, about 30,000 numbers. Serialized as text this is on the order of 100k tokens; summary statistics discard timing; a default matplotlib line plot costs a few hundred visual tokens and may hide a 2 cm sway difference. Clinicians already use stabilograms (center-of-pressure or center-of-mass path in the anterior-posterior by medio-lateral plane), sway time series with normative bands and skeleton overlays. Generalize: a data-analysis agent reading a 10,000-row table; a DevOps agent reading latency logs; a lab agent reading spectra.

## Definitions to include

Encoding (a function from a tool output to text or an image); information-matched encodings; graphical perception; perceptual gap; visual tokens; Pareto front; co-adaptation; private dialect (from emergent communication).

Formal core: tool output $o$, task statistic $s(o)$, label $y$, encoding $e\in\mathcal{E}$, VLM policy $\pi$. Objective $\min_e \mathbb{E}[\ell(\pi(e(o)),y)]+\lambda\,\text{tokens}(e(o))$. Decompose the error of an encoding into an information term, measured by an oracle decoder that reads the rendered pixels or text and recovers $s(o)$ (for example a small CNN trained on renders or an exact parser), and a perceptual term, the VLM's excess error over that oracle.

## Method and experiments

1. A graphical-perception battery for VLMs built from real sway and keypoint signals and matched synthetic ones: compare magnitudes, estimate ratios (Cleveland-McGill percent judgments), locate an event time (a step or loss of balance), judge left-right asymmetry, read a value at a time, count oscillations. Encodings: position on a common aligned scale, non-aligned position, length, angle, area, color, a text table, text summary statistics. Metric: Cleveland-McGill log error $\log_2(|\hat{p}-p|+1/8)$ and signed bias. Models: Qwen3-VL-8B and 32B, InternVL3.5, Gemma 3, one API model. Compare the resulting ranking with the human ranking.
2. Information-matched downstream tasks: StaBLE balance score regression, a clinical-extreme classification (bottom decile of the score), and BioCV contact timing from keypoint trajectories scored against force-plate events. Verify information content with the oracle decoder before attributing differences to perception.
3. Encoding search as self-improvement: the render tool is a program space (matplotlib functions under constraints: no access to labels; a separate "annotated" arm may print computed statistics and is reported separately because its gain is computation, not perception). Search with a GEPA-style reflective mutator that sees failure cases, and with an OpenEvolve-style loop; objective is downstream accuracy minus a token penalty; keep a Pareto archive over tasks and tokens.
4. Encoding as an action: train the agent with GRPO to choose a render specification per query (zoom window, overlay vs plot, which channels) and compare with the single best fixed encoding.
5. Transfer tests: held-out StaBLE tasks; cross-model (an encoding evolved for Qwen3-VL-8B tested on InternVL3.5 and an API model; define a model-specificity index as source gain minus target gain); human readers (a small timed study with biomechanics students or clinicians under IRB); fragility (small perturbations of line width, color, jitter).
6. Co-adaptation drift: alternate LoRA fine-tuning of the VLM on its current encoding with re-evolving the encoding for the current VLM. Measure accuracy, cross-model transfer and human readability each round. Prediction: accuracy rises while readability for other models and people falls, unless a readability regularizer is added (for example requiring a frozen reference VLM to stay accurate). This links observation design to emergent communication.
7. Second domain: time-series reasoning benchmarks (for example TimeSeriesExam) or table-heavy data-analysis agents, to test whether the perceptual profile and the evolved encodings carry over.

Analysis: per-model mixed-effects on log error with encoding and task as fixed effects; paired comparisons on the same items; pre-registered primary contrast (best evolved pure-rendering encoding vs best human-designed clinical plot on held-out tasks).

## Figures (suggested)

1. One tool output, four encodings, token costs, decisions.
2. Graphical-perception battery tiles (elementary tasks by encoding).
3. Information vs perception decomposition with the oracle decoder.
4. Encoding evolution loop.
5. Transfer matrix (tasks, models, humans).
6. Co-adaptation drift (illustrative): model accuracy up, readability down.
7. Encoding-as-action rollout.

## Falsifiers

Text serialization matches plots at matched information; or evolved encodings give no held-out gain over clinical plots; or all gains vanish across models (pure model-specific exploitation, which is itself a reportable result about VLM perception).

## Upgrades after the literature check and red-team review (these override the design above where they conflict)

Read `output/idea-summaries-build/research/07-observations-literature.md` and the P07 section of `research/red-team.md` first.

- **Closest work to position against.** Plots Unlock Time-Series Understanding (Daswani et al., arXiv 2410.02637); A Picture is Worth A Thousand Numbers / VL-Time (arXiv 2411.06018); By My Eyes (agent-chosen visualizations of sensor data); Evaluating Graphical Perception with Multimodal LLMs (arXiv 2504.04221) and the zero-shot VLM graphical perception study (arXiv 2411.00257); EncQA; Toward a Machine Bertin (a call for design principles for machine readers); Schaeffer et al. ICLR 2025 (optimized images transfer poorly between VLMs); learning-to-draw and language-drift work (Mihai and Hare; Lee et al. arXiv 1909.04499); human-centered VLM chart evaluation (Verma et al.). Be explicit that "plots beat numbers" and "VLMs have a graphical-perception profile" are known; the contribution is the predictive link from perceptual profiles to transfer and drift of self-designed observations.
- **Primary outcome: cross-reader transfer, predicted before any evolution.** Measure a perceptual profile per reader (each VLM, crowd humans, clinicians) with the Cleveland-McGill style battery. Pre-register two predictions: (1) a renderer evolved for reader A transfers to reader B in proportion to the similarity of their profiles; (2) evolution against one VLM drifts toward encodings on which that VLM beats humans and away from those where humans read better, so human legibility falls by an amount the profiles predict. The co-adaptation experiment is the extreme case of prediction 2.
- **Decompose every gain into three parts.** (a) Computation inside the renderer (deriving a feature and drawing it), isolated by an evolved text summarizer at equal budget and by a "no in-image text" arm that removes the OCR shortcut; (b) general perceptual improvement usable by any competent reader; (c) reader-specific exploitation, measured by transfer to held-out readers. The pixel oracle caps the information each encoding carries.
- **Fitness conditions at equal budget.** Single reader; an ensemble of readers from different families (Qwen3-VL-8B, InternVL3.5, Gemma 3 at similar size); ensemble plus a legibility term from a human proxy.
- **Transfer-decomposition curve.** Save every surviving renderer with its generation index and plot gain against generation for the source reader, held-out VLMs, a closed frontier VLM and human readers.
- **Load-bearing biomechanics.** Choose downstream decisions that each depend mainly on one perceptual type: sway amplitude (position on a common scale), drift (slope), sway ellipse (area), event timing (position in time). BioCV force plates and markers provide the reference that makes the pixel oracle possible; clinicians are a natural reader panel.
- **Split hygiene.** Participant-level splits, sealed test people, several seeds per arm; the renderer search is itself a self-improvement loop and inherits those rules.

## Decomposition stated with Bayes risks (from `research/theory-checks.md`, section D)

Write $R(o)$ for the Bayes risk with the raw tool output (the tool floor), $R(e)=\inf_g\mathbb{E}\,\ell(g(e(o)),y)$ for the encoding floor, and $R_\pi(e)$ for the reader's risk. Then $R_\pi(e)=R(o)+I(e)+P_\pi(e)$ with information term $I(e)=R(e)-R(o)\ge0$ and perceptual term $P_\pi(e)=R_\pi(e)-R(e)\ge0$. Under log loss $I$ is the mutual information lost and $P$ an expected KL divergence; with a restricted oracle family $I$ becomes usable V-information (Xu et al., arXiv 2002.10689). Split $P$ into a calibration part (removable by a post-hoc map) and a resolution part; build transfer profiles on resolution. Renderer computation shows up as a drop in $P$, not in $I$, so the gain split is $\Delta I$ plus general $\Delta P$ (mean over held-out readers) plus the reader-specific remainder. Conditions: the oracle reads exactly the VLM's post-resize input; no side information in the prompt; same loss and output space with parse failures counted; a near-Bayes oracle checked by learning curves, cross-architecture agreement and closed-form floors; participant-level splits for the oracle; task-indexed profiles; information matching before calling a difference perceptual. A negative measured gap diagnoses an under-trained oracle.
