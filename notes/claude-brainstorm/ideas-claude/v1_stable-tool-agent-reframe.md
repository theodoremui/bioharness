# Learning to Conduct Balance Assessments from One Camera with Tool-Calling Vision-Language Models

*Version 1. This version moves the project away from gait stride variability and onto the StaBLE balance dataset, which is the setting the lab is already working in, and replaces the fixed language model with a tool-calling vision-language model.*

## Abstract

Smartphone video could make balance testing routine, but turning a single video into a trustworthy balance score is still hard. Pipelines that rebuild a 3D skeleton and then apply hand-written scoring rules can be inspected step by step, yet they fail on unusual movements and take minutes per clip. Models trained to map video straight to a score always return an answer, but they explain nothing, and on a recent balance dataset they improve only modestly on a constant guess. We propose a third route, in which a vision-language model conducts the analysis: it calls pose, segmentation and reconstruction tools, writes code that computes each task's defined features, and passes those features to a fixed formula that produces the score. Using the StaBLE dataset of eighteen balance tasks, we will test whether such an agent, improved through prompt optimization, harness search, fine-tuning and reinforcement learning, can match learned predictors on people it has never seen while keeping every number traceable to a measurement.

## 1. Motivation

### 1.1 What a biomechanical measurement is

Biomechanics describes how the body moves and what forces produce that motion. A video-based measurement usually passes through four stages. A pose model first finds body landmarks (ankles, knees, hips, shoulders) in each frame. A reconstruction step turns those landmarks into a 3D skeleton whose joint angles and **center of mass**, the average position of the body's mass, change over time. A feature step then reduces those curves to a few numbers that capture what the task asked for. In the StaBLE "rise to toes" task, for example, a participant rises onto their toes as quickly and as high as possible and holds for five seconds, so the features are the peak upward speed of the center of mass, the peak ankle angle, and the time the center of mass stays high. Finally, a scoring step rescales each feature to a 0-to-1 range and averages them into a task score.

### 1.2 Two existing routes, and why neither is enough

The lab has already compared two families of methods on single-camera StaBLE videos from 43 held-out participants (729 task scores).

| Route | Example | Task-averaged error (lower is better) | Problem |
|---|---|---|---|
| Reconstruct and measure | OpenCap Monocular, then StaBLE rules | 0.146 | Valid score for only 567 of 729 cases; about four minutes of GPU time per clip |
| Constant guess | Each task's mean training score | 0.120 | Uses no video |
| Learn to predict | 2D pose with a temporal network | 0.119 | Barely better than the constant |
| Learn to predict | Qwen3-VL-8B, prompted without training | 0.238 | Worse than the constant |
| Learn to predict | Qwen3-VL-8B, fine-tuned on scores | 0.100 | Best so far, but opaque |
| Learn to predict | Qwen3-VL-8B, prompted to output features | 0.179 | Features are guessed from pixels |

The reconstruction route is interpretable because each intermediate quantity can be plotted and checked, but it breaks when a step fails. In the Y-Balance task, the scoring script looks for the moment the toe reverses direction during each reach, and on monocular reconstructions it often finds no reach at all. The predictive route always produces a number, but the number cannot be checked against anything a clinician can see, and the fine-tuned model's advantage over the constant guess is modest.

### 1.3 Why an agent

A **vision-language model (VLM)** is a neural network that takes images or video frames together with text and produces text. **Tool calling** means that some of the model's output is a structured request, such as `pose2d(video, model="rtmpose")`, that the surrounding software executes and returns as new input. The **harness** is that surrounding software: the list of tools and their descriptions, the loop that runs calls and returns results, the record of what has happened so far, and the rule for when to stop. An **agent** is the model and its harness working together over several steps.

The agent route combines the strengths of the other two. Geometry is delegated to specialist tools that are already validated, so the VLM does not need to estimate a speed in meters per second from pixels, which is where the frozen and feature-prompted models fail. The VLM is still useful for what it does well: reading a task description, choosing which tools and settings fit the task, looking at frames or plots to notice when a tool has failed, and writing the short program that turns tool outputs into features. Because the score is computed from features by a fixed formula, every score can be traced to the measurements behind it. Recent work points in this direction: [BiomechAgent](https://arxiv.org/abs/2602.06975) found that adding a validated gait-event tool improved a code-writing agent's spatiotemporal answers, and [DeepEyes](https://arxiv.org/abs/2505.14362) showed that reinforcement learning can teach a VLM when and where to use a visual tool.

## 2. Research question

**Primary question.** By the ICML 2027 submission deadline (expected late January 2027), can a Qwen3-VL-8B agent that calls existing analysis tools and reports StaBLE features, with the score computed by the fixed StaBLE formula, achieve a task-averaged mean absolute error on the 43 held-out participants that is lower than the fine-tuned Qwen baseline (0.100), while returning a valid score for all 729 task examples?

- *Specific*: one model family, one dataset, one held-out set, one outcome.
- *Measurable*: task-averaged mean absolute error and the fraction of valid scores.
- *Achievable*: the tools, the data and the baselines already exist in the lab.
- *Relevant*: it tests whether an inspectable analysis can be as accurate as an opaque predictor.
- *Time-bound*: about thirteen weeks, from late October 2026 to late January 2027.

**Secondary questions.** (a) Which of four improvement methods (prompt optimization, harness code search, supervised fine-tuning, reinforcement learning) gives the largest gain per unit of compute? (b) How often does the agent's reported feature agree with the three-camera reference feature, task by task?

## 3. Related work

**VLMs for movement assessment.** Knowledge-augmented prompt tuning ([Wang et al., 2024](https://arxiv.org/abs/2403.13756)) and [BioGait-VLM](https://arxiv.org/abs/2603.08564) feed gait parameters or skeleton tokens into a VLM to classify gait disorders, and [MyoMechanix](https://arxiv.org/abs/2608.26094) decomposes exercises into phases for coaching. These systems learn a direct mapping from inputs to labels and do not call measurement tools.

**Agents for biomedical analysis.** [Biomni](https://doi.org/10.1101/2025.05.30.656746) gives a language-model agent a large set of biomedical tools, and [BiomechAgent](https://arxiv.org/abs/2602.06975) writes analysis code over processed motion-capture databases. Both start from processed data rather than raw video, and neither trains the model.

**Learning to use tools.** [DeepEyes](https://arxiv.org/abs/2505.14362), [LongVT](https://arxiv.org/abs/2511.20785) and [ToolRL](https://arxiv.org/abs/2504.13958) train models with reinforcement learning to call tools, mostly for question answering where the reward is whether the final answer is right.

**Improving the harness without training the model.** [GEPA](https://arxiv.org/abs/2507.19457) rewrites prompts using feedback from runs, [Meta-Harness](https://arxiv.org/abs/2603.28052) searches over the harness code itself, and [VidHarness](https://arxiv.org/abs/2609.38413) applies harness search to long-video question answering. [Wang et al. (2026)](https://arxiv.org/abs/2607.12227) caution that these gains often shrink when the search budget is matched by simpler methods and when the harness is tested on new tasks.

## 4. Approach

### 4.1 Data

StaBLE contains 180 adults aged 18 to 87, from people with balance disorders to elite gymnasts and dancers, each recorded performing up to 18 tasks with three smartphones. A three-camera OpenCap reconstruction produced 76 features, 18 task scores and an overall StaBLE score for every participant. We use only the left-side camera (Cam0) as the agent's input. The three-camera features serve as reference values.

### 4.2 Tools

| Tool | What it returns | Typical cost |
|---|---|---|
| Frame viewer | Selected frames with timestamps, optionally cropped | Seconds |
| RTMPose | 2D landmarks for every frame | Seconds |
| SAM 2.1 | The participant's outline in every frame | Tens of seconds |
| CoTracker3 | Tracks of chosen image points | Tens of seconds |
| OpenCap Monocular | 3D joint angles and center of mass | About four minutes per 17-second clip |
| Plotter | An image of any signal, returned to the VLM | Seconds |
| Python sandbox | Runs agent-written code on tool outputs | Seconds |

### 4.3 What the agent returns

For each video the agent returns the task's features in physical units, each paired with a pointer to the tool output and time window it came from. Code then applies the StaBLE normalization and averaging. The agent never writes the score itself, which keeps the scoring rule out of the model and makes every score reproducible from the reported features.

### 4.4 Four ways to improve the agent

1. **Prompt optimization.** GEPA rewrites the system prompt and the tool descriptions, using feedback from runs on training participants.
2. **Harness search.** A Meta-Harness-style proposer edits the harness code (retry rules, default tool settings, checks on tool outputs), keeping a record of every earlier candidate and its results.
3. **Supervised fine-tuning.** Successful agent runs on training participants, those whose features land close to the reference, become training examples for low-rank adapters on Qwen3-VL-8B.
4. **Reinforcement learning.** Starting from the fine-tuned model, group relative policy optimization ([GRPO](https://arxiv.org/abs/2402.03300)) samples several runs per video and increases the probability of runs whose final score is closer to the reference.

## 5. Experiments

### 5.1 Splits

We keep the lab's existing split, so the 43 test participants stay the same and results remain comparable with the slide baselines. The remaining 128 participants form the development set, divided into five folds by participant, so that all of a person's videos fall in one fold. Prompt optimization, harness search, fine-tuning and reinforcement learning use only development folds. The test set is evaluated once, after all choices are fixed.

### 5.2 Comparisons

The agent variants are compared with every baseline in Section 1.2. The four improvement methods are given the same number of agent runs on training videos, and their compute in GPU hours is reported.

### 5.3 Outcomes and statistics

The primary outcome is task-averaged mean absolute error over all 729 test examples; a case without a valid score counts as a failure and is reported separately. Because each participant contributes up to 18 tasks, errors are first averaged within each participant. Differences between methods are computed per participant and summarized with a 95% confidence interval from 10,000 bootstrap resamples of participants. Secondary outcomes are per-task error, agreement between reported and reference features, and compute per video.

## 6. Timeline

| Weeks (from 26 Oct 2026) | Work |
|---|---|
| 1–2 | Freeze splits; cache tool outputs for all videos; implement the harness |
| 3–4 | Frozen-agent baseline; prompt optimization |
| 5–6 | Harness search |
| 7–9 | Supervised fine-tuning and reinforcement learning |
| 10–11 | Single test-set evaluation; analysis |
| 12–13 | Writing |

## 7. Risks

The agent may fail on the same tasks that defeat OpenCap Monocular, because it relies on the same reconstructions. The planned mitigation is to give the agent cheaper alternatives (2D pose and point tracking) for timing features, which do not need a full 3D skeleton. Reinforcement learning on 8-billion-parameter models with video inputs is expensive, so tool outputs are computed once per video and cached.
