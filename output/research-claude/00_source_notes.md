# Source notes for the BioHarness proposal series

This file collects the facts that the proposal versions in `docs/ideas-claude/` rely on, so that every claim can be checked against a source. It summarizes three internal documents and the external literature that was verified on 2026-10-22.

## 1. Internal documents

### 1.1 "Biomechanical Agent" planning note (`~/Downloads/nmbl/Biomechanical Agent.pdf`, 2 pages)

- Two candidate directions: (a) monocular video to good kinematics; (b) what an agent can do once good kinematics exist.
- Start with the StaBLE dataset and expand afterwards.
- Two kinds of validation are wanted: a technical validation of the tool (for example, in-painting missing data and computing features correctly) and a balance validation that a clinician would care about.
- Hierarchical breakdown of the work:
  1. Can the agent reproduce specific StaBLE features, and which tools does it use for feature extraction (easy to validate)?
  2. Can it reproduce StaBLE task scores (either given feature definitions, or given only task objectives)?
  3. Can it reproduce the paper: propose a balance score and compare the resulting ranking of participants?
- Progressive abstraction: start with three cameras and progressively reduce information, while asking the agent to extract the same results.
- Planned experiment ladder: zero-shot prompting (Astra, Gemini, Qwen), few-shot prompting, SFT, SFT + GRPO, frozen model with tools, model trained with tools.
- Related work named: Biomni, AI co-scientist, knowledge-augmented gait VLMs, BioGait-VLM, fitness action-quality VLMs, CoachVLM, children's gait, a dual-branch balance framework, MyoMechanix.
- Open logistics: IRB, model access (GPT, Gemini), GitHub.

### 1.2 NMBL lab meeting, 20 Oct 2026, "Learning to Conduct Biomechanical Analyses from Monocular Video" (53 slides)

- Framing: three ways to estimate a task score from video: **reconstruct and measure** (OpenCap Monocular, then StaBLE features and rules), **learn to predict** (video or pose to score), and **learn to conduct the analysis** (a VLM that calls analysis tools).
- Data: 180 participants × 18 tasks × 1 camera (Cam0) = 3,240 possible task samples; split by participant; 171 participants with 2,968 usable task examples; test set = 43 held-out participants with 729 task scores.
- Results (task-averaged mean absolute error on task scores in [0, 1], 43 test participants; lower is better):

| Method | Task-averaged MAE | Notes |
|---|---|---|
| OpenCap Monocular + StaBLE rules | 0.146 | only 567/729 valid scores, 17 tasks (no Y-Balance score) |
| Training-task mean (no video) | 0.120 | predicts each task's training mean |
| RTMPose + temporal CNN | 0.119 | frozen 2D pose, learned temporal model |
| Frozen Qwen3-VL-8B, score prompt | 0.238 | worse than the constant baseline |
| Qwen3-VL-8B, supervised LoRA fine-tuning | 0.100 | best result |
| Frozen Qwen, prompted to output StaBLE features (score computed in code) | 0.179 | no tools |

- Y-Balance failure: the reference script finds reach windows from a toe-velocity reversal, sweeping thresholds from 0.7 to 0.3 m/s; on monocular reconstructions no reach window was detected.
- OpenCap Monocular inference: ~3.8 minutes for a 17 s clip (1,020 frames) on an NVIDIA H100 (WHAM 156 s; refinement + OpenSim + diagnostics 44.6 s; feature extraction 1.5 s).
- Feature-prompt design: the VLM returns raw features with units; the fixed StaBLE normalization `S = (v − L) / (U − L)` is applied in code, so reference endpoints stay outside the model.
- Available tools named: OpenCap Monocular, OpenSim (kinematics and whole-body COM), DynamicsNet, GaitDynamics, RTMPose, SAM 2.1, CoTracker3, Video Depth Anything, plotting, and revisit/crop of frames.
- Closing question: "Can we train a VLM to choose which tools to use, and use their outputs to conduct the assessment?" Candidate levers: prompt optimization and RL optimization, judged on accuracy and cost.
- Reflection slide: reproducing a measurement pipeline is inspectable but needs better reconstruction and segmentation; learning the video-to-score map needs labels and gives little visibility into what drives a prediction.

### 1.3 StaBLE paper (Heigold et al., bioRxiv, posted 23 Sep 2026, doi 10.64898/2026.09.16.750744)

- 180 participants (117 F, 63 M), ages 18–87, 71 with self-reported diagnoses, 30 sports represented, including elite balancers; six collection sites.
- 18 tasks (standing, reaching, sit-to-stand, single-leg tasks, jump, gait), five with eyes closed; recorded with OpenCap using three smartphones (60 fps, HRNet).
- 3,322 motion trials; 98 trials across 24 participants were not performed for safety (assigned score 0); 30 trials (0.9%) had significant reconstruction error but were kept; 3 failed trials had features imputed by linear regression on age.
- 76 engineered features → 18 task scores (mean of normalized features) → StaBLE score (mean of task scores).
- **Normalization uses the minimum and maximum of each feature across all 180 participants** (Eq. 1–2). Any train/test analysis inherits information from test participants unless the endpoints are recomputed on training participants.
- StaBLE score distribution: min 0.08, max 0.84, mean 0.64, SD 0.12; left-tailed; clusters at zero for tasks some people could not attempt.
- Validity: Spearman ρ = −0.76 with age; ρ = 0.60 with ABC Scale; Kendall τ ≈ 0.55–0.57 with Mini-BESTest item, 4-Stage Balance Test, SPPB; KS = 0.67 between fall-risk groups.
- Forward subset selection: Y-Balance alone explains 63% of StaBLE variance; five tasks explain 88%.
- Seven participants appear in a public exemplar video (Fig. 3).
- Data: engineered features and covariates on Zenodo (10.5281/zenodo.22286165); code at github.com/stanfordnmbl/stable-analysis.

## 2. External literature (verified 2026-10-22)

| Work | Link | Why it matters here |
|---|---|---|
| OpenCap (Uhlrich et al., PLoS Comp Bio 2023) | https://doi.org/10.1371/journal.pcbi.1011462 | Multi-camera smartphone motion capture that produced the StaBLE reference |
| OpenCap Monocular (Gilon, Miller, Uhlrich, 2026) | https://arxiv.org/abs/2603.24733 | Single-video reconstruction tool; validated on walking, squat, sit-to-stand |
| BiomechAgent (Cotton & Leonard, 2026) | https://arxiv.org/abs/2602.06975 | Code-generating biomechanics agent; validated tools help spatiotemporal tasks |
| DeepEyes (Zheng et al., ICLR 2026) | https://arxiv.org/abs/2505.14362 | RL teaches a VLM when and where to call a crop tool |
| LongVT (2025) | https://arxiv.org/abs/2511.20785 | RL for native tool calling over long videos |
| VITAL / Thinking with Videos (CVPR 2026) | https://arxiv.org/abs/2508.04416 | Tool-augmented RL for video reasoning |
| ToolRL (Qian et al., NeurIPS 2025) | https://arxiv.org/abs/2504.13958 | Fine-grained reward design for tool use with GRPO |
| DeepSeekMath / GRPO (Shao et al., 2024) | https://arxiv.org/abs/2402.03300 | Group-relative policy optimization |
| Visual shortcuts in multimodal RLVR (Xu, 2026) | https://arxiv.org/abs/2606.22043 | Outcome-only rewards make video models stop using the video |
| Reward Hacking Benchmark (Thaman, 2026) | https://arxiv.org/abs/2605.02964 | Tool agents skip verification steps; RL post-training raises exploit rates |
| Privileged Information Distillation (Penaloza et al., 2026) | https://arxiv.org/abs/2602.04942 | π-Distill and on-policy self-distillation from a privileged teacher |
| GEPA (Agrawal et al., 2025) | https://arxiv.org/abs/2507.19457 | Reflective prompt evolution; competitive with GRPO at far fewer rollouts |
| Meta-Harness (Lee et al., 2026) | https://arxiv.org/abs/2603.28052 | Agentic search over harness code using a filesystem of past runs |
| VidHarness (Liang et al., 2026) | https://arxiv.org/abs/2609.38413 | Harness evolution for cost-efficient long-video understanding |
| Rethinking the Evaluation of Harness Evolution (Wang et al., 2026) | https://arxiv.org/abs/2607.12227 | Evolved harnesses often fail to beat matched test-time scaling and transfer poorly |
| Qwen-AgentWorld (Zuo et al., 2026) | https://arxiv.org/abs/2606.24597 | Language world models as simulators for agentic RL |
| Agentic World Modeling survey (2026) | https://arxiv.org/abs/2604.22748 | Tool-calling world models that predict a call's outcome before committing |
| Qwen3-VL Technical Report (2025) | https://arxiv.org/abs/2511.21631 | Base VLM used in the lab's pilot |
| Prediction-Powered Inference (Angelopoulos et al., 2023) | https://arxiv.org/abs/2301.09633 | Valid inference when model predictions supplement scarce labels |
| SWE-agent (Yang et al., 2024) | https://arxiv.org/abs/2405.15793 | Agent–computer interface design changes agent performance |
| Biomni (Huang et al., 2025) | https://doi.org/10.1101/2025.05.30.656746 | General biomedical agent with a large tool environment |
| AI co-scientist (Gottweis et al., 2025) | https://arxiv.org/abs/2502.18864 | Multi-agent generate–debate–evolve scientific workflow |
| Knowledge-augmented gait VLM (Wang et al., MICCAI 2024) | https://arxiv.org/abs/2403.13756 | VLM prompt tuning with gait parameters as numeric text |
| BioGait-VLM (2026) | https://arxiv.org/abs/2603.08564 | Skeleton tokens aligned with language for clinical gait assessment |
| MyoMechanix (2026) | https://arxiv.org/abs/2608.26094 | Compositional, biomechanics-grounded action-quality assessment |

The original Codex proposal also cited WiCER and DeMem (information preservation under compression). They are not used in the Claude versions because the information-loss framing was dropped after the v0 review.
