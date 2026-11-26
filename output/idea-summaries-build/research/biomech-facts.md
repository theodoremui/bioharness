# Biomechanics, dataset, model and statistics facts for P05 to P08

Status: complete (2026-11-24). All five sections filled; items not confirmed by a fetched page are listed in Section 5.

Verification date: 2026-11-24. Each external entry records title, authors, year, venue and URL as read from the fetched landing page. Entries that could not be fetched are marked UNVERIFIED.

## 1. StaBLE and the lab pilot (from local notes)

Sources read: `output/research-claude/00_source_notes.md` (summary of the StaBLE preprint, the NMBL planning note and the 20 Oct 2026 lab slides), `notes/claude-brainstorm/ideas-claude/v2_measure-or-guess-evaluation.md`, and `docs/idea-summaries/related-work.md` (section "What the movement studies actually measured"). Public-release facts in 1.2 were checked on Zenodo and GitHub on 2026-11-24.

### 1.1 What StaBLE contains (published protocol)

- Preprint: Heigold H, Ruth PS, Muccini J, Lee D, Barta S, Rodrigues A, Hastie T, Steenerson KK, Delp SL. "StaBLE: digital metrics capture balance performance across a wide spectrum of balance tasks and abilities." bioRxiv, posted 23 Sep 2026. https://doi.org/10.64898/2026.09.16.750744 (VERIFIED: landing page at https://www.biorxiv.org/content/10.64898/2026.09.16.750744v1).
- Participants: 180 (117 F, 63 M), ages 18 to 87, 71 with self-reported diagnoses, 30 sports represented including elite balancers, six collection sites (from local notes of the full text; the abstract confirms 180 and 18 tasks).
- Tasks: 18 balance tasks (standing, reaching, sit-to-stand, single-leg tasks, jump, gait), five performed with eyes closed.
- Cameras: recorded with OpenCap using three smartphones at 60 fps with HRNet keypoints. The three-camera OpenCap reconstruction is the reference against which single-camera methods are judged; it is itself a video-derived estimate, with no markers or force plates.
- Trials: 3,322 motion trials. 98 trials across 24 participants were not performed for safety and were assigned score 0. 30 trials (0.9%) had significant reconstruction error but were kept. 3 failed trials had features imputed by linear regression on age.
- Labels: 76 engineered features (for example, for "rise to toes": peak upward center-of-mass speed, peak ankle angle, time the center of mass stays high).
- Score computation: each feature value v is min-max normalized, S = (v - L) / (U - L), with direction flipped where lower is better; a task score is the mean of its normalized features (range 0 to 1); the StaBLE score is the mean of the 18 task scores.
- Leakage issue: L and U are the minimum and maximum of each feature over all 180 participants (Eq. 1 to 2 in the preprint). Any train/test analysis that uses the published task scores therefore carries information from test participants into the label scale. The v2 proposal's remedy is to recompute L and U on development participants only, accept test scores slightly outside 0 to 1, and report the published scale as a secondary analysis.
- Score distribution: StaBLE score min 0.08, max 0.84, mean 0.64, SD 0.12, left-tailed, with task scores clustered at zero for tasks some people could not attempt.
- Validity (cross-sectional): Spearman rho = -0.76 with age; rho = 0.60 with the Activities-specific Balance Confidence (ABC) Scale; Kendall tau about 0.55 to 0.57 with a Mini-BESTest item, the 4-Stage Balance Test and the SPPB; KS = 0.67 between fall-risk groups.
- Task redundancy: forward subset selection shows Y-Balance alone explains 63% of StaBLE-score variance and five tasks explain 88%.
- Single time point: each person was assessed once; the paper discusses ceiling effects and single-time-point limitations (related-work.md). There is no test-retest session and no between-visit change.
- Public exemplar video: seven participants appear in a public exemplar video (Fig. 3); results should be reported with and without any of them who fall in a test set.

### 1.2 What is publicly released versus held by the lab

- Zenodo record "Stanford Balance Level Evaluation (StaBLE) digital metrics of balance performance across a wide spectrum of balance tasks and abilities", v1, 10 Sep 2026, CC BY-NC 4.0, open access: https://doi.org/10.5281/zenodo.22286165 (VERIFIED). Files: `stable_features.csv`, `stable_scores.csv`, `stable_demographics.csv`, `feature_info.csv`, `incomplete_trials.csv`, README, and `opencap_data.zip` (189.6 MB) holding a scaled OpenSim model, virtual markers and kinematics for 7 exemplar participants only. No videos and no raw keypoints are listed.
- Code: https://github.com/stanfordnmbl/stable-analysis (VERIFIED, MIT license). `compute_scores.ipynb` computes normalized features, task scores and the StaBLE score for all 180 participants; `get_features` segments tasks and extracts features from OpenCap data.
- Consequence: the single-camera videos used in the pilot are lab-internal. A proposal that needs videos, per-frame kinematics for all 180 people, or re-running feature extraction must rely on lab access, not the public release.

### 1.3 Lab pilot results (LAB PILOT, unpublished, NMBL lab meeting 20 Oct 2026)

Setup: Cam0 only; 180 x 18 = 3,240 possible participant-task slots; 171 participants with 2,968 usable single-camera task examples; split by participant; test set of 43 held-out participants with 729 task scores. Metric: task-averaged mean absolute error on task scores in [0, 1] (lower is better). These scores use the published all-180 normalization, so they carry the leakage noted above.

| Method (lab pilot) | Task-averaged MAE | Notes |
|---|---|---|
| OpenCap Monocular + StaBLE rules | 0.146 | only 567 of 729 valid scores; 17 tasks (no Y-Balance score) |
| Training-task mean (no video) | 0.120 | predicts each task's training mean |
| RTMPose + temporal CNN (TCN) | 0.119 | frozen 2D pose, learned temporal model |
| Frozen Qwen3-VL-8B, score prompt | 0.238 | worse than the constant baseline |
| Qwen3-VL-8B, supervised LoRA fine-tuning (SFT) | 0.100 | best result |
| Frozen Qwen3-VL-8B prompted for StaBLE features, score computed in code | 0.179 | no tools |

Further pilot facts:
- Y-Balance failure: the reference script finds reach windows from a toe-velocity reversal, sweeping thresholds from 0.7 to 0.3 m/s; on monocular reconstructions no reach window was detected.
- OpenCap Monocular cost: about 3.8 minutes for a 17 s clip (1,020 frames) on one NVIDIA H100 (WHAM 156 s; refinement + OpenSim + diagnostics 44.6 s; feature extraction 1.5 s).
- The best learned model (0.100) improves on the constant guess (0.120) by about one sixth (skill score about 0.17), so MAE alone cannot separate a method that measures the person from one that shrinks toward the mean (v2 proposal, Section 1.3).
- Tools named in the lab slides: OpenCap Monocular, OpenSim (kinematics and whole-body center of mass), DynamicsNet, GaitDynamics, RTMPose, SAM 2.1, CoTracker3, Video Depth Anything, plotting, and frame revisit/crop.

## 2. Verified external works: datasets, tools, models, training stack

"Verified" means the landing page (arXiv abstract page, publisher page, Crossref record or Europe PMC record) was fetched on 2026-11-24 and the title and authors matched. A venue is given only when the fetched page states it; otherwise the entry says "venue not confirmed".

### 2.1 Datasets and biomechanics software

| Work | Authors, year, venue | Link | What it provides (one sentence) |
|---|---|---|---|
| StaBLE preprint | Heigold, Ruth, Muccini, Lee, Barta, Rodrigues, Hastie, Steenerson, Delp; bioRxiv, posted 23 Sep 2026 | https://doi.org/10.64898/2026.09.16.750744 | Protocol and validity study of 18 balance tasks in 180 people recorded with three-phone OpenCap, with 76 features min-max normalized over all participants into task scores and a StaBLE score. |
| StaBLE data release | Same creators; Zenodo v1, 10 Sep 2026, CC BY-NC 4.0 | https://doi.org/10.5281/zenodo.22286165 | Features, scores, demographics and fall/ABC covariates for 180 people, plus OpenSim model, virtual markers and kinematics for 7 exemplar participants; no videos. |
| StaBLE code | stanfordnmbl, MIT license | https://github.com/stanfordnmbl/stable-analysis | Notebooks that extract task features from OpenCap data and compute normalized features, task scores and StaBLE scores. |
| OpenCap | Uhlrich SD, Falisse A, Kidzinski L, Muccini J, Ko M, Chaudhari AS, Hicks JL, Delp SL; 2023; PLOS Computational Biology 19(10): e1011462 | https://doi.org/10.1371/journal.pcbi.1011462 | Smartphone motion capture (two or more phones, 720x1280 at 60 Hz) estimating kinematics and dynamics; validation in ten healthy adults recorded by five iPhone 12 Pro phones (results mostly from the two +/-45 degree phones) against 100 Hz marker capture and force plates, with joint-angle MAE 4.5 degrees and translational MAE 12.3 mm reported in the main text. |
| OpenCap Monocular | Gilon S, Miller EY, Uhlrich SD; arXiv 2603.24733, v1 25 Mar 2026; venue not confirmed | https://arxiv.org/abs/2603.24733 | Single-smartphone-video 3D kinematics and kinetics by refining WHAM pose with a biomechanically constrained OpenSim model and physics/ML force estimation, validated on walking, squat and sit-to-stand against markers and force plates (rotational MAE 4.8 degrees, pelvis translation 3.4 cm). |
| OpenCap LabValidation data | OpenCap project, SimTK; Apache 2.0 use agreement | https://simtk.org/projects/opencap | 10 participants performing squats, sit-to-stand, drop vertical jump and walking, with RGB video from 5 cameras, marker motion capture, ground reaction forces, EMG from 10 muscles, and processed OpenSim IK/ID and muscle-driven simulations. |
| BioCV | Evans M, Needham L, Wade L, Parsons M, Colyer S, McGuigan P, Bilzon J, Cosker D; 2024; Scientific Data 11: 1300 | https://doi.org/10.1038/s41597-024-04077-3 ; data https://doi.org/10.15125/BATH-01258 | Synchronized 9-camera 200 fps video, 200 Hz marker motion capture (15-camera Qualisys, 42 markers), 1000 Hz in-floor force plates (4 Kistler) and photogrammetry body scans for 15 healthy adults (8 F, 7 M) doing repeated walking, running, jumping and hopping; access on request after agreeing to terms. |
| AddBiomechanics Dataset | Werling K, Kaneda J, Tan T, Agarwal R, Skov S, Van Wouwe T, Uhlrich S, Bianco N, Ong C, Falisse A, Sapkota S, Chandra A, Carter J, Preatoni E, Fregly B, Hicks J, Delp S, Liu CK; Computer Vision, ECCV 2024, LNCS, pp. 490 to 508 (Crossref) | https://arxiv.org/abs/2406.18537 ; https://doi.org/10.1007/978-3-031-73223-2_27 | 273 subjects and over 70 hours of motion with force-plate data (over 24 million frames) processed into physically consistent OpenSim kinematics and dynamics, with a benchmark for estimating torques and ground reaction forces from motion. |
| OpenSim (2007) | Delp SL, Anderson FC, Arnold AS, Loan P, Habib A, John CT, Guendelman E, Thelen DG; 2007; IEEE Trans Biomed Eng 54(11): 1940 to 1950 | https://doi.org/10.1109/TBME.2007.901024 | Original open-source software for building musculoskeletal models and dynamic simulations of movement. |
| OpenSim (2018) | Seth A, Hicks JL, Uchida TK, Habib A, Dembia CL, Dunne JJ, Ong CF, DeMers MS, Rajagopal A, Millard M, Hamner SR, Arnold EM, Yong JR, Lakshmikanth SK, Sherman MA, Ku JP, Delp SL (and others); 2018; PLOS Computational Biology 14(7): e1006223 | https://doi.org/10.1371/journal.pcbi.1006223 | OpenSim 4.0-era description of the extensible platform for simulating musculoskeletal dynamics and neuromuscular control (inverse kinematics, inverse dynamics, muscle forces, predictive simulation). |
| GaitDynamics | Tan T, Van Wouwe T, Werling KF, Liu CK, Delp SL, Hicks JL, Chaudhari AS; 2026; Nature Biomedical Engineering 10(8): 1659 to 1671 (online 5 Jan 2026) | https://doi.org/10.1038/s41551-025-01565-8 ; code https://github.com/stanfordnmbl/GaitDynamics | Diffusion-based generative model of walking and running trained on AddBiomechanics data that estimates ground reaction forces from kinematics, fills missing kinematics, and predicts effects of gait modifications. |

### 2.2 Vision tools the agent can call

| Work | Authors, year, venue | Link | What it provides |
|---|---|---|---|
| RTMPose | Jiang T, Lu P, Zhang L, Ma N, Han R, Lyu C, Li Y, Chen K; arXiv 2303.07399, 2023; venue not confirmed | https://arxiv.org/abs/2303.07399 | Real-time 2D multi-person pose estimation in MMPose (RTMPose-m 75.8% COCO AP at over 90 FPS on CPU; RTMPose-l 67.0% COCO-WholeBody AP). |
| RTMW | Jiang T, Xie X, Li Y; arXiv 2407.08634, 2024; venue not confirmed | https://arxiv.org/abs/2407.08634 | Real-time 2D and 3D whole-body pose models extending RTMPose (largest variant 70.2 mAP on COCO-WholeBody). |
| ViTPose | Xu Y, Zhang J, Zhang Q, Tao D; NeurIPS 2022 (arXiv comments) | https://arxiv.org/abs/2204.12484 | Plain vision-transformer backbone with a light decoder for 2D human pose estimation, scaling to state-of-the-art COCO results. |
| SAM 2 | Ravi N, Gabeur V, Hu Y-T, and 15 others; arXiv 2408.00714, 2024 | https://arxiv.org/abs/2408.00714 | Promptable transformer model for segmenting and tracking objects in images and videos with streaming memory. |
| CoTracker3 | Karaev N, Makarov I, Wang J, Neverova N, Vedaldi A, Rupprecht C; arXiv 2410.11831, 2024 | https://arxiv.org/abs/2410.11831 | Point tracker trained by pseudo-labelling real videos with existing trackers, giving dense long-range 2D point tracks. |
| Video Depth Anything | Chen S, Guo H, Zhu S, Zhang F, Huang Z, Feng J, Kang B; arXiv 2501.12375; CVPR 2025 (DOI 10.1109/CVPR52734.2025.02126 per Semantic Scholar) | https://arxiv.org/abs/2501.12375 | Temporally consistent relative depth for long videos, extending Depth Anything V2 with a spatial-temporal head (the abstract does not claim metric depth). |
| WHAM | Shin S, Kim J, Halilaj E, Black MJ; CVPR 2024 (Crossref DOI 10.1109/CVPR52733.2024.00202); arXiv 2312.07531 | https://arxiv.org/abs/2312.07531 | World-grounded 3D human mesh motion from video using lifted 2D keypoints, image features, SLAM camera rotation and contact-aware foot refinement; the first stage of OpenCap Monocular. |
| GVHMR | Shen Z, Pi H, Xia Y, Cen Z, Peng S, Hu Z, Bao H, Hu R, Zhou X; SIGGRAPH Asia 2024 (arXiv comments) | https://arxiv.org/abs/2409.06662 | World-grounded human motion recovery in gravity-view coordinates, avoiding drift of autoregressive world-frame methods. |

### 2.3 Base models

| Work | Authors, year | Link | What it provides |
|---|---|---|---|
| Qwen3-VL Technical Report | Bai S, Cai Y, Chen R, et al. (64 authors); arXiv 2511.21631, Nov 2025 | https://arxiv.org/abs/2511.21631 | Open VLM family for text, images and video: dense 2B, 4B, 8B, 32B and MoE 30B-A3B and 235B-A22B, native 256K context; the 8B dense model is the pilot base. |
| InternVL3.5 | Wang W, Gao Z, Gu L, and 72 others; arXiv 2508.18265, Aug 2025 | https://arxiv.org/abs/2508.18265 | Open multimodal family with two-stage RL for reasoning, a visual-resolution router and decoupled vision-language deployment; a second open VLM for cross-model transfer. |
| Gemma 3 Technical Report | Gemma Team (Kamath A, Ferret J, Pathak S, and 213 others); arXiv 2503.19786, Mar 2025 | https://arxiv.org/abs/2503.19786 | Open 1B to 27B models with image input and at least 128K context; a third model family for transfer tests. |
| Qwen3-Coder | Qwen team blog "Qwen3-Coder: Agentic Coding in the World", 22 Jul 2025 | https://qwenlm.github.io/blog/qwen3-coder/ | Agentic coding model (first release Qwen3-Coder-480B-A35B-Instruct, 256K native context) trained with long-horizon multi-turn RL; no arXiv technical report is linked, so cite the blog. |

### 2.4 Training and serving stack

| Work | Authors, year, venue | Link | What it provides |
|---|---|---|---|
| DeepSeekMath (GRPO) | Shao Z, Wang P, Zhu Q, and 8 others; arXiv 2402.03300, Feb 2024 | https://arxiv.org/abs/2402.03300 | Introduces Group Relative Policy Optimization, a PPO variant that replaces the value network with group-normalized rewards. |
| DAPO | Yu Q, Zhang Z, Zhu R, and 32 others; arXiv 2503.14476, Mar 2025 | https://arxiv.org/abs/2503.14476 | Open-source large-scale RL algorithm and system (decoupled clipping, dynamic sampling) reaching 50 points on AIME 2024 with Qwen2.5-32B base. |
| verl / HybridFlow | Sheng G, Zhang C, Ye Z, Wu X, Zhang W, Zhang R, Peng Y, Lin H, Wu C; EuroSys 2025, pp. 1279 to 1297 (Crossref, DOI 10.1145/3689031.3696075); arXiv 2409.19256 | https://arxiv.org/abs/2409.19256 ; code https://github.com/volcengine/verl | Hybrid single/multi-controller RLHF framework with a 3D-HybridEngine for actor resharding; open-sourced as verl. |
| vLLM (PagedAttention) | Kwon W, Li Z, Zhuang S, Sheng Y, Zheng L, Yu CH, Gonzalez JE, Zhang H, Stoica I; SOSP 2023 (arXiv comments) | https://arxiv.org/abs/2309.06180 | LLM serving system with paged key-value cache memory, 2 to 4x throughput over prior systems. |
| LoRA | Hu EJ, Shen Y, Wallis P, Allen-Zhu Z, Li Y, Wang S, Wang L, Chen W; arXiv 2106.09685, 2021; venue not confirmed on arXiv page | https://arxiv.org/abs/2106.09685 | Freezes pretrained weights and trains low-rank update matrices per layer, cutting trainable parameters while matching full fine-tuning. |
| Agent Lightning | Luo X, Zhang Y, He Z, Wang Z, Zhao S, Li D, Qiu LK, Yang Y; arXiv 2508.03680, Aug 2025 | https://arxiv.org/abs/2508.03680 | Decouples agent execution from RL training and splits recorded agent trajectories into per-step transitions with assigned rewards, so existing agents can be trained without rewriting. |

### 2.5 Closest biomechanics-agent work

| Work | Authors, year | Link | What it provides |
|---|---|---|---|
| BiomechGPT | Yang R, Kennedy A, Cotton RJ; arXiv 2505.18465 (v1 May 2025, v2 Jul 2026) | https://arxiv.org/abs/2505.18465 | Motion-language model that tokenizes clinical motion and answers clinical movement questions, trained on 71 hours from 750 participants; treats agentic tool use as future work. |
| BiomechAgent | Cotton RJ, Leonard T; arXiv 2602.06975 (abs page lists v1 as submitted 16 Jan 2026); venue not stated | https://arxiv.org/abs/2602.06975 | Code-generating agent for natural-language biomechanical analysis, with a benchmark (retrieval, visualization, classification, temporal segmentation, clinical reasoning) showing that domain prompts and a validated gait-event tool improve accuracy; per related-work.md, temporal answers rose from 0/12 to 10/12 against a concealed instrumented walkway when GaitTransformer was added. |

## 3. Measurement reliability and graphical perception statistics

### 3.1 Sources

| Work | Bibliographic record (verified) | Link | What it provides |
|---|---|---|---|
| Shrout and Fleiss 1979 | Shrout PE, Fleiss JL. "Intraclass correlations: uses in assessing rater reliability." Psychological Bulletin 86(2): 420 to 428. PMID 18839484 | https://doi.org/10.1037/0033-2909.86.2.420 | Guidelines for choosing among six forms of the ICC for n targets rated by k judges, with confidence intervals for each (abstract verified). |
| McGraw and Wong 1996 | McGraw KO, Wong SP. "Forming inferences about some intraclass correlation coefficients." Psychological Methods 1(1): 30 to 46 | https://doi.org/10.1037/1082-989X.1.1.30 | The ten-form ICC taxonomy (model, type, definition) that Koo and Li summarize (bibliography verified via Crossref; content not re-read). |
| Koo and Li 2016 | Koo TK, Li MY. "A Guideline of Selecting and Reporting Intraclass Correlation Coefficients for Reliability Research." Journal of Chiropractic Medicine 15(2): 155 to 163. PMID 27330520, PMCID PMC4913118 | https://doi.org/10.1016/j.jcm.2016.02.012 | Reporting guideline: state software and the model, type and definition; interpret using the 95% CI of the ICC with poor < 0.5, moderate 0.5 to 0.75, good 0.75 to 0.9, excellent > 0.90 (abstract verified). |
| Weir 2005 | Weir JP. "Quantifying test-retest reliability using the intraclass correlation coefficient and the SEM." Journal of Strength and Conditioning Research 19(1): 231 to 240. PMID 15705040 | https://doi.org/10.1519/15184.1 | Test-retest ICC and SEM, and the "minimal difference" needed to call an individual change real (abstract verified; the explicit formula is in the subscription full text, not re-read here). |
| Furlan and Sterr 2018 | Furlan L, Sterr A. "The Applicability of Standard Error of Measurement and Minimal Detectable Change to Motor Learning Research: A Behavioral Study." Frontiers in Human Neuroscience 12: 95. PMCID PMC5875129 | https://doi.org/10.3389/fnhum.2018.00095 | Open-access source that states SEM = s_baseline x sqrt(1 - ICC) and MDC95 = SEM x 1.96 x sqrt(2) in its Methods (full text verified via Europe PMC). |
| Bland and Altman 1986 | Bland JM, Altman DG. "Statistical methods for assessing agreement between two methods of clinical measurement." Lancet 1(8476): 307 to 310. PMID 2868172 | https://doi.org/10.1016/S0140-6736(86)90837-8 | Plot the difference between methods against their mean; report bias (mean difference d) and limits of agreement d +/- 2s (more precisely d +/- 1.96s), with standard error of the limits about sqrt(3 s^2 / n); correlation is not agreement (verified from the author-hosted copy at https://www-users.york.ac.uk/~mb55/meas/ba.pdf). |
| Prieto et al. 1996 | Prieto TE, Myklebust JB, Hoffmann RG, Lovett EG, Myklebust BM. "Measures of postural steadiness: differences between healthy young and elderly adults." IEEE Trans Biomed Eng 43(9): 956 to 966. PMID 9214811 | https://doi.org/10.1109/10.532130 | Time- and frequency-domain center-of-pressure (COP) measures in 20 young (21 to 35) and 20 elderly (66 to 70) adults, eyes open and closed; mean COP velocity was the only measure that detected age differences in both visual conditions (abstract verified). |
| Quijoux et al. 2021 | Quijoux F, Nicolai A, Chairi I, Bargiotas I, Ricard D, Yelnik A, Oudre L, Bertin-Hugault F, Vidal P-P, Vayatis N, Buffat S, Audiffren J. "A review of center of pressure (COP) variables to quantify standing balance in elderly people: Algorithms and open-access code." Physiological Reports 9(22): e15067. PMCID PMC8623280 | https://doi.org/10.14814/phy2.15067 | Open-access definitions and code for COP variables: sway length (sum of distances between consecutive COP points), mean velocity (sway length / duration), RMS radius (citing Prieto 1996) and 95% ellipse area (citing Schubert and Kirchner 2014). |
| Schubert and Kirchner 2014 | Schubert P, Kirchner M. "Ellipse area calculations and their applicability in posturography." Gait and Posture 39(1): 518 to 522. PMID 24091249 | https://doi.org/10.1016/j.gaitpost.2013.09.001 | Shows that "confidence ellipses" are widely misused for COP scatter and recommends the prediction ellipse (abstract verified). |
| Cleveland and McGill 1984 | Cleveland WS, McGill R. "Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods." Journal of the American Statistical Association 79(387): 531 to 554 | https://doi.org/10.1080/01621459.1984.10478080 | Defines elementary perceptual tasks for reading graphs and ranks them by accuracy from proportional-judgment experiments (bibliography verified via Crossref; the publisher abstract could not be fetched). |
| Heer and Bostock 2010 | Heer J, Bostock M. "Crowdsourcing graphical perception: using Mechanical Turk to assess visualization design." Proc. CHI 2010, pp. 203 to 212 | https://doi.org/10.1145/1753326.1753357 | Replicated Cleveland and McGill's proportional-judgment study on Mechanical Turk (seven judgment types: position on a common scale, length, angle, circular area), preserved the accuracy ranking, and added rectangular-area, chart-height and gridline experiments (verified from the paper PDF at http://vis.stanford.edu/files/2010-MTurk-CHI.pdf). |

### 3.2 Definitions the proposals can use

- ICC forms. Shrout and Fleiss name forms ICC(1,1), ICC(2,1), ICC(3,1) and their k-average versions ICC(1,k), ICC(2,k), ICC(3,k), set by whether raters (here: runs, sessions or devices) are a random sample, fixed, or nested, and whether one rating or a mean of k is used. McGraw and Wong add the consistency versus absolute-agreement distinction, giving ten forms. For repeated agent runs on the same video, where any run could be the deployed run, the natural choice is two-way random effects, absolute agreement, single measurement (ICC(2,1) in Shrout-Fleiss notation, "ICC(A,1)" in McGraw-Wong). This mapping follows from the definitions; it is our reading, not a sentence quoted from either paper.
- SEM. SEM = SD x sqrt(1 - ICC), or SEM = sqrt(within-subject mean square error) from the ANOVA (Weir 2005 discusses both; the second does not depend on between-subject spread).
- MDC95. MDC95 = 1.96 x sqrt(2) x SEM (stated in Furlan and Sterr 2018; Weir 2005 calls the same quantity the minimal difference). The sqrt(2) arises because a change score is the difference of two noisy measurements.
- Bland-Altman. Bias = mean of paired differences; 95% limits of agreement = bias +/- 1.96 SD of the differences; check whether the spread grows with the mean and log-transform if it does.
- Posturography. COP sway path length (also called total excursion or sway length) = sum of distances between consecutive COP samples; mean velocity = path length / duration; RMS distance (RMS radius) = sqrt(mean squared distance from the mean COP); sway area as the area of an ellipse covering about 95% of COP samples, which Schubert and Kirchner argue should be a prediction ellipse, not a confidence ellipse. Prieto et al. 1996 is the standard source for these measures; the abstract confirms "time and frequency domain measures", and the detailed list above is taken from Quijoux et al. 2021, which cites Prieto for RMS radius.
- StaBLE relevance. StaBLE features are computed from video-reconstructed whole-body center of mass, not from force-plate COP, so COP sway measures apply to StaBLE only by analogy (center-of-mass sway from kinematics) and directly only to datasets with force plates.
- Graphical perception. In the Cleveland-McGill proportional-judgment task, a viewer sees two marked elements and estimates what percentage the smaller is of the larger; Heer and Bostock score accuracy as log2(|judged percent - true percent| + 1/8) and summarize with midmeans and bootstrapped 95% intervals. They report position encoding significantly more accurate than length encoding. The widely cited Cleveland-McGill accuracy ordering (position on a common scale, then position on non-aligned scales, then length, direction and angle, then area, then volume and curvature, then shading and color saturation) is from the 1984 paper but was not re-read in this session; cite the paper, and treat the exact ordering as needing a check against its text before quoting.

## 4. What each dataset can and cannot support

Key: YES = supported by the documented data; NO = not available; PARTIAL = available with a stated limit; CHECK = plausible but not documented on the pages fetched.

| Capability | StaBLE (lab videos) | StaBLE (public Zenodo only) | BioCV | OpenCap LabValidation | AddBiomechanics |
|---|---|---|---|---|---|
| Participants | 180 (171 usable in pilot) | 180 features; 7 with kinematics | 15 healthy adults | 10 healthy adults | 273 |
| Single-camera video to run a VLM agent on | YES (3 phones, 60 fps; lab-internal) | NO (no videos released) | YES (9 synchronized cameras, 200 fps; access on request) | YES (5 phones, 60 Hz; public "withVideos" zip) | NO (motion and force data only) |
| Repeated runs of an agent on the same video | YES, given lab access | NO for video; YES for code-only agents on the 7 exemplar kinematics | YES | YES | NO for video; YES for agents that take kinematics as input |
| Same movement seen by several cameras (inter-device agreement) | YES (Cam0, Cam1, Cam2 of one trial) | NO | YES (9 views) | YES (5 views) | NO |
| Repeated trials of the same person, same session | PARTIAL: one session, mostly one trial per task; the exact repeat structure must be read from the trial ledger (`incomplete_trials.csv` lists missing trials) | PARTIAL (features per task only) | YES (each movement repeated "numerous times"; exact count not on the archive page) | YES (five squats and five sit-to-stands per condition, three drop jumps per condition, three walking trials per condition) | YES (multiple trials per subject; counts vary by source study, CHECK) |
| Test-retest across days (between-visit change) | NO (single time point) | NO | NO (single session described) | NO | CHECK (depends on source study) |
| Independent ground-truth kinematics from markers | NO (reference is three-camera OpenCap, itself video-derived with HRNet keypoints) | NO | YES (42 markers, 200 Hz, 15-camera Qualisys, synchronized to video) | YES (marker capture at 100 Hz, OpenSim IK provided) | YES (marker-derived OpenSim kinematics, but no video to compare against) |
| Force-plate events (contact, toe-off, GRF) | NO | NO | YES (4 Kistler in-floor plates, 1000 Hz; related-work.md notes that force-derived stance events and marker heel strikes differ and that synchronization problems are documented) | YES (ground reaction forces; also EMG of 10 muscles) | YES (force plates; ID and GRF processed) |
| COP sway measures (Prieto-style) | NO (only video-derived center-of-mass sway) | NO | PARTIAL (force plates exist, but the listed movements are dynamic, not quiet standing) | PARTIAL (same caveat) | PARTIAL (depends on source study) |
| Clinical balance scales | YES per preprint (ABC Scale, a Mini-BESTest item, 4-Stage Balance Test, SPPB, fall history and fall risk); CHECK which are in the lab files | PARTIAL (Zenodo lists demographics, self-reported fall history, fall risk and balance confidence) | NO | NO | NO (not documented) |
| Task overlap with StaBLE | full | full | gait, jump, hop only | sit-to-stand, squat, gait, drop jump | gait, running, varied by study |

Notes that matter for P05 to P08:
- Repeated agent runs on one video measure the agent's own variability (sampling temperature, tool-choice branching, GPU nondeterminism). If tool outputs are cached per video, as in the v2 design, they do not measure tool variability; re-executing tools must be a separate condition.
- For P08 (test-retest ICC and MDC), StaBLE can support run-to-run reliability on a fixed video and camera-to-camera agreement on one trial, but not person-level test-retest across sessions. Within-session trial repeats in BioCV and OpenCap LabValidation are the closest available substitute; they mix true trial-to-trial movement variation with measurement error, so an MDC computed from them is an upper bound on measurement-only MDC.
- For P07 (encodings of numeric tool outputs), StaBLE center-of-mass traces from OpenCap give realistic sway and timing signals with a reference feature value for every trial; BioCV and OpenCap LabValidation add force-plate and marker channels, which allow an "information-matched" check that a rendered plot carries the same quantity as the instrument.
- For P06 (trace leakage), the StaBLE all-180 min-max normalization is an existing example of label-scale leakage, and any reported pilot number inherits it; recomputing L and U on the development split is a prerequisite for an honest held-out estimate.
- For P05 and P08 generalization claims, BioCV and OpenCap LabValidation are the only sets here with both video and an independent physical reference, and both are small (15 and 10 people), so they suit validity checks and calibration of certification thresholds, not large-sample training.

## 5. Unverified or corrected items

- StaBLE details beyond the abstract (sex split, ages, 71 diagnoses, 30 sports, six sites, 3,322 trials, 98 unperformed, 30 kept with reconstruction error, 3 imputed, 76 features, normalization equations, score distribution, validity statistics, 63% and 88% subset results, 7 exemplar participants) come from the local summary of the full text in `00_source_notes.md`; the preprint landing page confirms title, authors, posting date, 180 participants, 18 tasks, validity against age and the ABC Scale, and the Zenodo and GitHub links. The full text was not re-read here.
- Lab pilot numbers are unpublished lab-meeting results and must be labeled as such in every proposal.
- Weir 2005: bibliography and abstract verified; the explicit MDC formula was not re-read (full text is subscription). Cite Furlan and Sterr 2018 alongside Weir for the formula.
- Prieto et al. 1996: bibliography and abstract verified; the named list of COP measures is taken from the open-access Quijoux et al. 2021 review, not from the Prieto full text.
- Cleveland and McGill 1984: bibliography verified; the exact ten-task accuracy ordering was not re-read and should be checked before quoting.
- McGraw and Wong 1996: bibliography verified via Crossref only.
- Venues NOT confirmed by any fetched page (cite as arXiv preprints unless checked): RTMPose, RTMW, SAM 2, CoTracker3, LoRA, DAPO, Agent Lightning, OpenCap Monocular, BiomechGPT, BiomechAgent, DeepSeekMath, Qwen3-VL, InternVL3.5, Gemma 3. (SAM 2 at ICLR 2025 and LoRA at ICLR 2022 are widely reported, but OpenReview blocked automated fetching, so both are UNVERIFIED as venues.)
- Venues confirmed: ViTPose NeurIPS 2022 (arXiv comments), GVHMR SIGGRAPH Asia 2024 (arXiv comments), vLLM SOSP 2023 (arXiv comments), WHAM CVPR 2024 (Crossref), Video Depth Anything CVPR 2025 (Semantic Scholar DOI), HybridFlow EuroSys 2025 (Crossref), AddBiomechanics Dataset ECCV 2024 (Crossref).
- Qwen3-Coder has no arXiv technical report linked from its release blog; cite the blog post.
- BiomechAgent: the arXiv abs page dates v1 to 16 Jan 2026 although the identifier begins 2602; cite as arXiv:2602.06975 (2026).
- Correction: the AddBiomechanics third author is Tian Tan (Crossref), not "Alan Tan".
- BioCV camera count: 9 machine-vision video cameras; the separate 15-camera Qualisys system is the marker system and the 64-camera rig is for photogrammetry scans.
