# Standalone research ideas: tool-calling agents for single-camera balance measurement

Seven self-contained proposals. Each poses its own research question and can be read, run and judged without the others. They share a testbed (StaBLE single-camera video, the three-camera OpenCap reconstruction as reference, a tool-calling Qwen3-VL-8B agent, and 60 participants sealed before any analysis) and the same protocol choices (participant-level splits, rescaling endpoints refitted inside folds, training runs treated as a source of uncertainty), so their results are comparable. None depends on another's results.

| File | Research question, in short | How the agent is improved | H100-hours (estimate) |
|---|---|---|---|
| [v1](v1_conducting-the-analysis-vs-predicting-the-score.md) | Does conducting the analysis with tools beat predicting the score directly, and what carries any advantage? | Fine-tuning; prompt and harness search | about 1,500 |
| [v2](v2_measuring-or-guessing-individual-differences.md) | Do tool-derived features preserve differences between people better than direct prediction, and does shrinkage explain errors at the extremes? | Fine-tuning; the contribution is the evaluation | about 950 |
| [v3](v3_feature-rewards-and-tool-noise.md) | When tools are noisier than the population, what do outcome rewards teach, and what do per-feature rewards repair? | RL with a tool-noise sweep | about 3,900 (2,600 reduced) |
| [v4](v4_privileged-teacher-demonstrations.md) | Can a teacher with a privileged multi-camera view write demonstrations that make a single-camera student more accurate? | Privileged demonstrations, then fine-tuning | about 2,000 (1,100 for the primary comparison) |
| [v5](v5_measurement-programs-for-unseen-tasks.md) | Can an agent write accurate measurement programs for tasks it never trained on, and do known-answer checks help? | RL with checks; held-out tasks | about 3,200 (1,900 reduced) |
| [v6](v6_checks-or-library-for-agent-measurement-code.md) | Do known-answer checks keep agent-written code honest, and does a validated feature library do as well? | RL, three arms | about 4,350 (2,450 reduced) |
| [v7](v7_measurements-that-follow-the-movement.md) | Does training code to respond to signal changes as definitions prescribe make measurements follow held-out changes in movement? | RL with metamorphic checks | about 3,250 (1,950 reduced) |

Each estimate includes the one-time tool cache (about 400 H100-hours), which is shared if more than one study runs. "Reduced" versions run reinforcement learning on six tasks spanning the main task families.

**Provenance.** Each file reframes the same-numbered version in `notes/claude-brainstorm/ideas-claude/` around that version's distinctive question; those originals are revisions of one research program and are left unchanged. The questions follow the split used in `notes/claude-brainstorm/ideas-claude-simplified/`, which holds one-page versions of the same seven ideas.
