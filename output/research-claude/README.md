# BioHarness proposal series: scores, critiques and reviews

This folder records how the proposal in `output/research-codex/biomechanical_agent_proposal.md` (v0) was graded, critiqued and revised through seven versions, saved in `docs/ideas-claude/`. Each version was reviewed twice: once against the rubric below, and once by Codex through `/codex:adversarial-review`, whose verbatim output is kept alongside a table showing how every finding was handled.

## Files

| File | Contents |
|---|---|
| `00_source_notes.md` | Facts drawn from the three source documents, plus the verified literature list |
| `review_v0_codex-baseline.md` | Rubric definition and the review of the original Codex proposal |
| `review_v1.md` … `review_v7.md` | Scores, critiques and suggestions for each Claude version, with Codex dispositions |
| `codex_adversarial_review_v0.md` … `_v7.md` | Verbatim Codex adversarial reviews |

## Proposal versions

| Version | File | What changed |
|---|---|---|
| v0 | `output/research-codex/biomechanical_agent_proposal.md` | Original: learned "evidence contracts" for gait stride variability |
| v1 | `docs/ideas-claude/v1_stable-tool-agent-reframe.md` | Re-anchored on StaBLE, monocular video and a tool-calling VLM; lab baselines as the ladder |
| v2 | `docs/ideas-claude/v2_measure-or-guess-evaluation.md` | Measure-or-guess evaluation (rank agreement, skill, calibration slope), data ledger, training-only normalization, expert pipeline, crossed bootstrap |
| v3 | `docs/ideas-claude/v3_measurement-grounded-rewards.md` | Per-feature rewards from the three-camera reference, executable provenance checks, sealed confirmatory set, tool-feature regressor, cached tool environment |
| v4 | `docs/ideas-claude/v4_privileged-teacher-and-budgeted-levers.md` | Privileged teacher restricted to student actions, budget tiers with continuation controls, appearance controls, staged journey with gates |
| v5 | `docs/ideas-claude/v5_world-model-transfer-and-known-answer-verification.md` | Known-answer probes and a shortcut suite, exact reward bound, tool-outcome world model, held-out tasks, time-scaling interventions, 60 sealed participants reserved first, pipeline figure |
| v6 | `docs/ideas-claude/v6_simplified-reward-what-can-be-checked.md` | Simplification: one thesis, one running example, a worked trajectory, five confirmatory comparisons, per-stage data-shape and leakage table |
| v7 | `docs/ideas-claude/v7_final_rewarding-what-can-be-checked.md` | Final: unbiased evaluation policy, required-signal check tied to StaBLE's released code, noisy-copy replay, seven paired seeds with a fixed testing order, Codex v5–v7 fixes, title options, style audit |

Figures: `docs/ideas-claude/figures/training_pipeline.svg` (used by v5 and v6) and `training_pipeline_v7.svg` (final, used by v7). Earlier versions keep their own figure so that no version is overwritten.

## Score trajectory

Weighted overall score out of 10 (rubric in `review_v0_codex-baseline.md`).

| Dimension (weight) | v0 | v1 | v2 | v3 | v4 | v5 | v6 | v7 |
|---|---|---|---|---|---|---|---|---|
| D1 Significance (15%) | 4 | 6 | 6.5 | 7.5 | 8 | 8.5 | 8.5 | 8.5 |
| D2 Novelty (15%) | 4 | 5 | 5 | 7 | 7.5 | 8 | 8 | 8.5 |
| D3 Research question (10%) | 6 | 7 | 8 | 8 | 7.5 | 8 | 8.5 | 8.5 |
| D4 Soundness (10%) | 4 | 5 | 6 | 7 | 7.5 | 8 | 8 | 8.5 |
| D5 Experimental design (10%) | 6 | 5 | 7 | 8 | 8 | 8.5 | 8.5 | 8.5 |
| D6 Statistics and leakage (10%) | 7 | 5 | 7.5 | 8.5 | 8.5 | 9 | 9 | 9.5 |
| D7 Feasibility (10%) | 3 | 7 | 7 | 6.5 | 6.5 | 6.5 | 7 | 7 |
| D8 Clarity (10%) | 5 | 7 | 8 | 8 | 7 | 6.5 | 8.5 | 8.5 |
| D9 Story arc (5%) | 3 | 5 | 7 | 6 | 8 | 8 | 8 | 8.5 |
| D10 Writing (5%) | 6 | 7 | 7 | 7 | 7 | 7 | 8 | 8.5 |
| **Weighted overall** | **4.75** | **5.85** | **6.78** | **7.43** | **7.58** | **7.88** | **8.23** | **8.45** |

## Title options (from v7)

1. Rewarding Only What Can Be Checked: Training Tool-Calling Video Agents to Measure Balance from One Camera *(recommended)*
2. Learning to Conduct Biomechanical Analysis: Privileged, Checked Supervision for Vision-Language Agents
3. Known Answers as Rewards: Reinforcement Learning for Tool-Using Video Agents in Movement Assessment
4. From Three Cameras to One: Distilling Biomechanical Measurement into a Tool-Calling Vision-Language Model
5. Privileged Sensors, Checked Measurements: Training Agents to Measure Human Movement from Smartphone Video
6. Do Video Agents Measure? Robust Training of Tool-Calling Vision-Language Models for Balance Assessment
7. When a Better Instrument Exists Only in Training: Checked Rewards for Tool-Calling Agents in Clinical Movement Analysis

## How the story evolved

The original draft (v0) tried to learn which information a gait workflow must keep, on data the lab does not have. v1 moved the project onto the StaBLE dataset and the lab's own question: can a vision-language model learn to conduct the analysis with tools? v2 noticed that a constant guess almost matches the best model and rebuilt the evaluation around whether a method measures or guesses. v3 turned that diagnosis into a training signal by rewarding each feature against the three-camera reference and checking that each number came from executed code. v4 used the same privileged data a second time, through a teacher restricted to the student's tools, and laid the work out as stages with decision gates. v5 hardened the check with known-answer probes and a shortcut suite, added a tool-outcome world model, held-out tasks and movement interventions, and reserved a larger sealed set before any analysis. v6 rewrote everything around one thesis and one example so a newcomer can follow it. v7 closed the last loopholes that Codex found (memorizing functions, arm-dependent evaluation, a reward that scored different values from the evaluation, too few seeds for the mechanism test, transfer calibration, capped features) and fixed the compute plan.
