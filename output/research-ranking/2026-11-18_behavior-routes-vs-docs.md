# Ranking the research ideas: the Codex behavior routes (13 Nov) against the docs proposals

Prepared 18 November 2026.

## What was compared

- **Attached set (R1–R4).** The four one-page routes and README in `~/Documents/Codex/2026-11-07/role-you-are-an-expert-ai/outputs/behavior-research-2026-11-13/`, read together with that folder's `adversarial-review.md` and `related-work.md`.
- **Docs set.** `docs/ideas-claude/` v1–v7 is one program refined seven times, ending in v7, "Rewarding Only What Can Be Checked". `docs/ideas-claude-simplified/` splits that program into seven single-hypothesis studies, labelled S1–S7 here: S1 feature-based estimation against direct prediction, S2 preserving differences between people, S3 per-feature rewards, S4 privileged teacher, S5 transfer to held-out tasks, S6 known-answer checks, S7 physical-response checks. The reviews in `output/research-claude/` and `output/research-claude-explained/` were read as well.
- **Not included.** `extended-proposals-2026-11-14/` and `paper-edition-2026-11-14/`, which sit in the same Codex folder.

Four targeted literature searches were run to test the claims that decide the ranking. They are cited where used, and a single search finding nothing is treated as weak evidence of novelty, not proof of it.

## 1. The two sets ask different questions

The docs program asks how to train a tool-calling vision-language model (VLM) so that it measures the person in the video instead of reproducing typical values. Every docs study shares one setup: Qwen3-VL-8B, single-camera StaBLE video, cached tool outputs, the three-camera OpenCap reconstruction as the reference, and an evaluation built to separate measuring from guessing (within-task rank agreement, skill against the constant guess, calibration slope, and appearance controls).

The attached routes ask whether the signals around an optimizer can be trusted, and whether they can be afforded. R1 asks whether the reference shares the tools' errors, R2 how a tool behaves numerically after a software change, R3 which old evaluations stay valid after a harness edit, and R4 how to coordinate analyses when the quantity of interest is the difference between two recordings. Only R1 and R4 depend on biomechanics in an essential way. R2 and R3 would work the same on any scientific toolchain or agent benchmark.

The two sets therefore sit at different layers of one system and are better combined than chosen between:

| Attached route | Closest element in docs | Relationship |
|---|---|---|
| R1 shared-error reference | The three-camera reference, which docs use as the reward, the probe answers, the teacher's panel, the tool-outcome model's labels and the evaluation target | R1 tests the assumption the whole docs program rests on. Docs mention it only in closing "Interpretation" paragraphs |
| R2 tool-response learning | The tool-outcome world model in v5–v7, dropped from the simplified set | R2 is the version of that model that transfers across software changes |
| R3 evidence regeneration | Stage 3 prompt and harness search, capped at 20 validation evaluations per run | R3 would replace the cap with audited reuse of earlier evaluations |
| R4 paired change | Time-scaling interventions (S7, and S4 in v7) | Docs test the response to a synthetic change; R4 makes the paired contrast the quantity being estimated and the unit of decision |

## 2. The docs set: strengths and weaknesses

**Strengths.** The designs can be run on data the lab already has. Leakage control is careful: a sealed set reserved first, endpoints refitted inside folds, one scoring policy for every method, and seeds treated as a source of uncertainty. The evaluation lens (does a method order people correctly, or does it shrink toward the average?) is the most useful shared asset in either set, and every attached route would need something like it. The program answers the lab's own question.

**Weaknesses, most consequential first.**

1. **One instrument does every job.** The three-camera reconstruction supplies the reward, the probe answers, the teacher's panel, the world model's labels and the final evaluation. OpenCap Monocular refines WHAM and ViTPose estimates and then runs OpenSim inverse kinematics on a full-body musculoskeletal model ([Gilon et al., 2026](https://arxiv.org/abs/2603.24733)), and the three-camera pipeline also ends in OpenSim inverse kinematics. Errors that come from the body model's joint definitions or segment masses can therefore appear in both. Center-of-mass features are the clearest case, because they are computed from the model's segment masses in both pipelines, while a center of mass estimated from 2D keypoints would not share that assumption. Any shared error is invisible to every component of the docs program at once. This is R1's point, and it is the strongest argument for combining the sets.

2. **The check may be solving a problem the design created.** The agent writes free-form feature code. That opens shortcuts (constants, memorized values, functions of the agent's own time marks), and the four-part check then closes them. StaBLE's released analysis code already computes the features from reconstructed kinematics, and v7 runs it to set the expected responses. An agent that calls that code as a tool, and decides only the route, the time window and any signal repair, cannot write a constant. No docs version includes this *library-constrained agent*. If it matches the checked agent, the check matters only where no library exists, which is the held-out-task setting of S5, and the headline should move to routing and timing.

3. **The required-signal check can reject legitimate perception.** A hold time computed from the agent's start and end marks is a valid measurement when the marks are right, and those marks are what the VLM produces by reading plots. The check rejects that kind of function, which pushes the agent toward threshold rules on the monocular signal, the same signal that fails in the hard cases.

4. **Scale and calendar.** v7 needs about 5,600 H100-hours and 21 final RL runs. Its schedule began on 26 October, the ICML deadline is roughly ten weeks away, and this repository contains proposals only. v7 as written cannot be executed before the deadline. Its primary contrast, at the six-task reduced scope it already defines, can.

5. **The closest prior art is not cited.** Known-answer checks are test-case rewards for generated code ([CodeRL](https://arxiv.org/abs/2207.01780) and later work) combined with programming by example. Required-signal checks are metamorphic testing (Chen et al., 1998; Xie et al., 2011): a metamorphic relation states how a program's output must change when its input is transformed in a known way. The privileged teacher restricted to the student's actions resembles [Learning by Cheating](https://arxiv.org/abs/1912.12294) and learning using privileged information (Vapnik and Vashist, 2009). The tool-outcome model is a form of learned routing ([FrugalGPT](https://arxiv.org/abs/2305.05176), [RouteLLM](https://arxiv.org/abs/2406.18665)). None of these makes the program redundant, but reviewers will raise each one.

6. **The internal scores are not independent.** The 8.45 out of 10 assigned to v7 came from the pipeline that wrote it. The Codex reviews found five serious problems in the final draft, which were patched in place.

## 3. The attached set: strengths and weaknesses

**Strengths.** Each route names the equally informed baseline that would make its method unnecessary: reference denoising for R1, unstructured meta-learning and system identification for R2, exact caching with uniform audits for R3, and an unrestricted paired policy for R4. The docs set should adopt that habit. R1's synthetic experiment, which holds each error distribution fixed while varying only the dependence between candidate and reference errors, is clean and cheap. R1 also finds the blind spot described above.

**Weaknesses.**

1. **The core estimators are already established, and the routes say so.** R1's identity, R3's residual estimator and R4's variance decomposition are textbook results. Each claim therefore rests on a learned representation beating an equally informed baseline, and the prior probability of that is low. The most likely publishable outcome for R1 and R2 is a demonstrated phenomenon or a benchmark, not a new method.

2. **R1's mathematics needs extending before it applies to the docs reward.** The identity holds: with Δ the loss of route *a* minus the loss of route *b*, Δ_ref − Δ_true = −2(r − y)(a − b) under squared loss. Because a − b is observed at deployment, predicting the correction amounts to predicting E[r − y | context, a, b], which is reference denoising conditioned on the route outputs. The README concedes this. The docs reward and the error metric are absolute errors, and under absolute loss the picture changes. Reference error then distorts a preference only when the reference or the truth lies between the two candidate outputs, and the distortion is bounded by 2|r − y|. That structure is more useful than the squared-loss case and should be the version R1 develops.

3. **Part of the "shared error" is the target.** StaBLE features are defined through OpenCap's three-camera reconstruction. For the lab's practical goal of reproducing StaBLE from one phone, agreement with the reference is the objective, shared components included. R1 matters for claims about physical movement and in the clinical extremes, where the reference itself may fail. R1 links shared error to the pilot's degradation at the extremes, but that link is speculative. Shrinkage toward the mean, which S2 already diagnoses, is the simpler explanation and should be ruled out first.

4. **Two routes need data StaBLE lacks.** R1 needs anchors that do not come from OpenCap, and R4 needs repeated recordings; StaBLE reports no repeatability data. Partial substitutes exist inside StaBLE. The StaBLE score correlates with the Activities-Specific Balance Confidence scale (ρ = 0.60) and the 4-Stage Balance Test (τ = 0.55), and the release includes fall history ([Heigold et al., 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13621976)). Those are participant-level anchors. Human-annotated event times would anchor the timing features. For R4, two kinds of contrast already in StaBLE could stand in for repeated visits. One is left against right in the bilateral tasks, where both sides have a three-camera reference. The other is a pair of phones viewing the same trial, where the true change is zero and any measured change comes from the analysis.

5. **The closest prior art is missing here too.** R3's estimator, together with model-guided sampling probabilities, is the core of [Active Testing](https://arxiv.org/abs/2103.05331) (Kossen et al., ICML 2021) and [Active Statistical Inference](https://arxiv.org/abs/2403.03208) (Zrnic and Candès, ICML 2024). Successive halving and racing ([Hyperband](https://arxiv.org/abs/1603.06560)) are the natural baselines for choosing the best candidate harness, and neither appears. A recent preprint on [self-evolving harnesses](https://arxiv.org/abs/2610.18813) raises R3's concern about reusing rollouts across search steps. For R1, the relevant literature covers correlated errors across models ([Kim et al., ICML 2025](https://arxiv.org/abs/2506.07962)), LLM evaluators favoring their own outputs ([Panickssery et al., 2024](https://arxiv.org/abs/2404.13076)) and reward-model overoptimization ([Gao et al., ICML 2023](https://arxiv.org/abs/2210.10760)). Framing R1 as the instrument version of judge self-preference would make it immediately legible to an ICML audience.

6. **R2 and R3 are far from the lab's question.** Neither needs a VLM or biomechanics. To persuade ML reviewers they would have to run on standard agent benchmarks, at which point they become different projects.

7. **The writing is hard to follow.** "Ancestry", "potentials", "rectifiers", "routes" and "audits" are used without definitions, and the sentences are compressed to the point that a reader outside the review loop cannot follow the argument.

## 4. Final ranking

The ranking orders ideas by expected payoff as the headline of an ICML 2027 submission from this lab, using StaBLE and the deadline about ten weeks away. The qualitative ratings are inputs to a judgment and are not summed; the last column, the chance of a clear result in either direction, carries real weight. S1 and S2 are left out of the ranking because they are foundations: every training study needs their baselines and evaluation, and neither is an ML contribution on its own. S3 and S6 are folded into rank 1, which is their joint contrast.

| Rank | Idea | Source | ML novelty | Feasible by late Jan | Clean decisive test | Lab value | Prior-art risk | Chance of a clear result |
|---|---|---|---|---|---|---|---|---|
| 1 | Checked per-feature reward against outcome reward | v7 core (S3 + S6) | Medium | Medium, at six tasks | High | High | Medium | Medium-high |
| 2 | Shared-error references | R1 | High | Low-medium | Synthetic high, real low | Medium-high | Medium | Medium |
| 3 | Privileged teacher, compared after fine-tuning | S4 | Medium | Medium-high | Medium | Medium-high | Medium-high | Medium |
| 4 | Physical-response (metamorphic) checks | S7 | High | Medium | Medium | Medium-high | Low | Low as training, high as evaluation |
| 5 | Evidence regeneration after harness edits | R3 | Low-medium | High | High | Low | High | High |
| 6 | Transfer to held-out tasks | S5 | Medium-high | Medium | Low | Medium-high | Medium | Low |
| 7 | Numerical tool-response learning | R2 | Medium | Low-medium | Low-medium | Medium | High | Low |
| 8 | Joint measurement of change | R4 | Medium | Low | Medium | High | Medium | Medium, once data exist |

**1. Checked per-feature reward against outcome reward (docs v7 core).** This is the lab's question, it runs on existing data, and the regime that makes it interesting is already visible in the pilot. A constant guess (task-averaged error 0.120) beats the monocular reconstruction route (0.146, valid on 567 of 729 cases), so an outcome reward pulls the policy toward abandoning its tools. Showing that collapse, then showing that a per-feature reward prevents it, is a general lesson for training scientific agents with verifiable rewards. No prior work combining a privileged instrument, verified intermediate rewards and a tool-calling VLM measurement agent turned up. To keep this first, the study needs the library-constrained agent as an added arm, a cut to the six-task scope with one primary contrast, the prior art in Section 2, item 5 positioned explicitly, and S7's held-out transformations used as evaluation.

**2. Shared-error references (R1).** This is the most important idea in the attached set, because it names the one assumption every docs study depends on. As a method it is weak: under squared loss the correction is reference denoising. As a phenomenon it is general, covering any agent trained against a model-based verifier that shares components with its tools. That includes LLM judges sharing a base model with the policy, which links it to work an ICML audience already follows. It ranks below rank 1 because its real-data test needs independent anchors and its practical bite for StaBLE reproduction is partly definitional. Its cheapest version fits inside rank 1. The study would ask whether checked RL raises agreement with the three-camera reference without raising agreement with human-annotated event times and the clinical measures, and whether it drifts toward the monocular 3D route specifically on center-of-mass features. The synthetic dependence experiment can run now — on a CPU, in a few days.

**3. Privileged teacher, compared after fine-tuning (S4).** The simplified version compares students immediately after supervised fine-tuning, so it needs teacher generation and fine-tuning but no RL. It is the cheapest training result with an open answer: whether a teacher's advantage from seeing the three-camera curves can be learned by a student that never sees them. It doubles as rank 1's warm start, so the work is not wasted if the effect is null. Novelty is moderate given Learning by Cheating and recent privileged distillation ([Penaloza et al., 2026](https://arxiv.org/abs/2602.04942)).

**4. Physical-response checks (S7).** This is the most original mechanism in the docs. One standard-mode search found no prior use of metamorphic relations as a reward for program-writing agents, and the idea applies wherever a quantity has a known response to time, scale or unit changes. As a training intervention, however, its effect is likely small. The comparison arm already has known-answer probes, which remove most of the shortcuts that response checks target, and the check can reject legitimate durations computed from visual time marks (Section 2, item 3). Held-out video transformations, with expected values computed by rerunning StaBLE's feature code on equally transformed reference trajectories, are a strong evaluation that rank 1 should adopt immediately. Training with response checks can follow once that evaluation shows a gap.

**5. Evidence regeneration after harness edits (R3).** This route is the easiest to run and to settle: full fresh re-execution is the hidden answer key, and the comparison is a cost-against-ranking-regret curve. Its novelty is thin, because the estimator belongs to Active Testing and Active Statistical Inference, and only the conditioning on the harness edit is new. Its value to the lab is mainly lower Stage 3 cost. It would make a reasonable general-agent paper on standard benchmarks with racing baselines, or a piece of infrastructure, but not this lab's headline.

**6. Transfer to held-out tasks (S5).** This is the right ML question, and it is where free-form measurement code, and therefore the check, earns its place. Three held-out tasks cannot support a transfer claim, and each comes from a family (standing, reaching, gait) that stays in training. Running it properly needs leave-one-family-out evaluation, which multiplies RL cost. A version using frozen or prompted agents could be included in rank 1 as a descriptive result.

**7. Numerical tool-response learning (R2).** The unit of generalization is a tool implementation, and only a handful of real pose estimators and 3D lifters exist. Meta-learning over that few is statistically weak, and synthetic tool variants do not establish transfer to real software. System identification and unstructured meta-learning are strong competitors, as the route itself says. The docs' tool-outcome model is the natural non-transfer baseline if this is ever pursued.

**8. Joint measurement of change (R4).** Paired change — across visits, devices or a course of rehabilitation — is what clinics most need over the longer term, and the joint-error argument is sound. StaBLE cannot validate it. A prototype using bilateral asymmetry and pairs of phones viewing the same trial is possible now, but test-retest validity needs new recordings. This is a strong candidate for a grant or a follow-up collection, not for January.

## 5. Recommended plan for the next ten weeks

- **Weeks 1–2.** Build the foundations from S1 and S2: ledger, sealed split, retrained baselines and the measure-or-guess evaluation. Build the tool cache and the library-constrained agent. Run R1's synthetic dependence experiment. Start human annotation of event times on a few hundred development and sealed videos.
- **Weeks 3–6.** Run rank 1 at the six-task scope with four arms (outcome reward, per-feature reward, checked per-feature reward, library-constrained) from S4's warm start. The S4 comparison after fine-tuning is the first reportable result.
- **Weeks 7–8.** Open the sealed set once. Evaluate with S7's held-out transformations and the R1 audit against human event times and the clinical measures.
- **Weeks 9–10.** Write.

## 6. What would change this ranking

- **The library-constrained agent matches the checked agent on development folds.** The headline of rank 1 moves to outcome against per-feature rewards for routing and timing, and S5 rises, because checks then matter only where code must be written.
- **The R1 audit shows that the checked agent's gains are mostly shared with the reference.** R1 becomes the headline, as a cautionary result about training scientific agents against model-derived references.
- **Six-task RL turns out to be unaffordable.** S4, which needs fine-tuning only, becomes the main training result, and R3 becomes a cheap second paper.
