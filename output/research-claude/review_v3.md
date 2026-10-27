# Review of v3: "Rewarding the Measurement"

Reviewed file: `docs/ideas-claude/v3_measurement-grounded-rewards.md`
Rubric: see `review_v0_codex-baseline.md`.

## Scores

| Dimension | v0 | v1 | v2 | v3 | Rationale for v3 |
|---|---|---|---|---|---|
| D1 Significance (15%) | 4 | 6 | 6.5 | 7.5 | A general lesson is now visible: when an answer is a known function of measurable intermediate quantities and a better sensor exists at training time, reward the intermediate quantities and verify them. |
| D2 Novelty (15%) | 4 | 5 | 5 | 7 | Verified, per-feature rewards from a privileged sensor are a concrete mechanism that differs from outcome rewards (DeepEyes, LongVT), argument-level rewards (ToolRL) and learned process rewards. |
| D3 Research question (10%) | 6 | 7 | 8 | 8 | A clean primary contrast (measurement reward against score-only reward, same start, same rollouts) with a well-chosen secondary family. |
| D4 Soundness (10%) | 4 | 5 | 6 | 7 | The bound argument and masking of imputed targets are right. The dependence check can be passed by code that reads its input trivially (a constant plus a negligible term). |
| D5 Experimental design (10%) | 6 | 5 | 7 | 8 | The tool-feature regressor, the fixed-call ablation and best-of-8 close the obvious alternative explanations. Budget matching across levers is still loose. |
| D6 Statistics and leakage (10%) | 7 | 5 | 7.5 | 8.5 | Sealed confirmatory set, per-fold endpoints, exact estimators, crossed bootstrap, statuses in the ledger. |
| D7 Feasibility (10%) | 3 | 7 | 7 | 6.5 | The compute assumption (13,000 H100-hours) is stated but may exceed what the lab has, and warm-start yield from a frozen 235B model is unknown. |
| D8 Clarity (10%) | 5 | 7 | 8 | 8 | The concepts section is a real improvement. The method section is dense for a newcomer. |
| D9 Story arc (5%) | 3 | 5 | 7 | 6 | The staged journey from v2 (re-baseline, frozen agent, harness, SFT, RL) was compressed into a hypothesis table, so the "hypothesis, test, next step" rhythm is weaker. |
| D10 Writing (5%) | 6 | 7 | 7 | 7 | Clear. A few antithesis-style constructions crept in (the title's "instead of"). |

**Weighted overall: 7.43 / 10** (v2: 6.78). ICML readiness: weak accept if executed well. The proposal now has a mechanism and a fair test of it. Its weakest points are the warm start and how much of the three-camera data it puts to use.

## Main critiques

1. **The privileged data does only half its job.** The three-camera reconstruction is used to score trajectories but not to produce good ones. The warm start relies on a larger frozen model that sees the same single video, and the lab's pilot suggests frozen VLMs are weak at this task. A teacher that can *see* the three-camera reference while choosing only actions the student can also take would produce better demonstrations. Recent work on privileged-information distillation ([Penaloza et al., 2026](https://arxiv.org/abs/2602.04942)) gives a template, and also warns that a teacher whose actions depend on information the student lacks produces demonstrations the student cannot follow.
2. **The dependence check is too weak.** "The value must change" is satisfied by `c + 1e-9 * mean(x)`. The check should require a *material* change of a size fixed in advance, measured on probe videos whose reference values are far apart.
3. **Budget matching is still informal.** GEPA and harness search spend proposer-model tokens; RL spends GPU hours on gradients and rollouts. The proposal should compare methods at a few prespecified budgets, charging every cost (failed candidates, warm-start data generation, cache misses), and report the accuracy-versus-cost curve.
4. **The journey is less visible than in v2.** v2's stage table made the logic of each next step explicit. v3 should bring it back with decision gates that say what happens if a stage fails.
5. **Cost is a reported number, not part of the agent's job.** OpenCap Monocular takes minutes per clip. An agent that calls it on every video when 2D pose would do is wasteful, and nothing in v3 teaches the agent otherwise.
6. **Feasibility needs a smaller default.** The plan should name a minimum version that fits a smaller budget (for instance, fewer tasks in RL or a 4B model) and say what claims survive in that version.
7. **The title uses an "X instead of Y" construction**, which the style brief asks to avoid.

## Suggestions for v4

1. Add a **privileged teacher**: the same harness, given the three-camera joint angles and center of mass as extra context, writes monocular analyses whose actions are restricted to the student's tools; distill these into the student before RL, and compare with the non-privileged warm start.
2. Strengthen verification with a **materiality threshold** on probe videos.
3. Define **budget tiers** and plot accuracy against total cost for every lever.
4. Restore the **staged story arc** with explicit decision gates.
5. Add a small **cost term** to the reward and report the accuracy–cost trade-off.
6. Add a **minimum viable scope** and the claims it supports.

## Codex adversarial review of v3 and its disposition

Verbatim output: `codex_adversarial_review_v3.md`. Verdict: needs-attention.

| Codex finding | Severity | Response |
|---|---|---|
| The verifier certifies almost-constant guesses (`0.5 + 1e-8·mean(x)`) | high | v4's materiality threshold narrows the hole but a tuned linear trick could still pass. v5 replaces it with **known-answer probes**: the feature code must reproduce the three-camera reference on development probe videos within a tolerance and in the right order, and a pre-registered suite of shortcut programs must fail the verifier before RL starts. |
| Rank agreement undefined for constant predictions | high | Addressed in v4 (operational zero, fixed task set); v5 adds a rule for a zero skill denominator. |
| Power not targeted at the primary statistic | high | Addressed in v4 (simulation with the joint decision rule and seed variability); v5 states 80% target power and an exploratory-only fallback. |
| Enlarging the sealed set would move evaluated participants into it | high | Adopted in v5: 60 participants are reserved before any development analysis and all 60 are evaluated; development uses the other 111. |
| Ledger does not link trials and references | high | Addressed in v4 (trial-level manifest, StaBLE aggregation rule). |
| Sampler includes non-attempts | high | Adopted in v5: status-specific eligibility table for sampling, normalization, rewards and evaluation; non-attempts enter only the composite StaBLE score, as the protocol requires. |
| Person swap confounds appearance and motion | high | v4 added demographic and single-frame baselines. v5 adds feature-specific **time-scaling interventions** with predicted responses (durations scale up, speeds scale down, angles stay fixed), which preserve appearance exactly. |
| Clipping invalidates the score-error bound | medium | Adopted in v5: errors are uncapped, unverified features fall back to the training mean and carry an extra fixed penalty, and the bound is restated and holds exactly. |
| Original training pool is not provably untouched | medium | Adopted in v5: the design is described as a retrospective re-split with an audit of prior use; prospective confirmation on newly recorded participants is proposed as follow-up. |
| Verification contribution only tested in an exploratory arm | medium | Adopted in v5: the no-verification arm gets three seeds at matched budget and its contrast with the full method is a confirmatory secondary test. |
