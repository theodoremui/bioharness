# Review record for proposals 5 to 8

This record explains how the four newer proposals were chosen, checked and revised, and what remains open. It covers [proposal 5](05-what-makes-a-harness-improvable.md), [proposal 6](06-who-self-improvement-leaves-behind.md), [proposal 7](07-learning-how-to-look-at-tool-outputs.md) and [proposal 8](08-blind-analysis-for-agents.md). All reviews described here were carried out by AI reviewers (Claude agents and OpenAI Codex), not by external human referees, and the novelty and significance scores are their estimates. The underlying reports are kept in [output/idea-summaries-build/](../../output/idea-summaries-build/): literature and theory notes in `research/`, simulation scripts in `sim/`, and every review and resolution table in `reviews/`.

## How the four directions were chosen

The aim was four directions in recursive self-improvement and agent tool use that would be useful for measuring movement from video, general enough to matter for other agents, and not already crowded. Six candidates were checked against the 2025 and 2026 literature by separate agents, each scoring novelty and significance from 1 to 5 as a demanding area chair would. A red-team reviewer then attacked the set.

| Candidate | First estimate (novelty, significance) | Closest work found | Decision |
|---|---|---|---|
| Harness structure and improvability | 4.0, 3.5 | Code for Machines (observational), Agentic Harness Engineering, Huxley-Gödel Machine | Kept, with a single-edit profile, a length-matched placebo and a proposer-capability crossover (proposal 5) |
| Overfitting from reading execution traces | 2.5 to 3.5, 3.5 to 4.0 | The winner's curse in LLM self-improvement loops (arXiv 2610.09239), RRSI, TextReg, compression bounds of Bertran, Roth and Wu | Dropped: at least five 2026 papers study the same problem |
| Self-designed observations for VLM agents | 3.5, 3.5 | Plots Unlock Time-Series Understanding, graphical-perception studies of multimodal models, Toward a Machine Bertin | Kept, with transfer predicted from perception profiles as the primary outcome (proposal 7) |
| Certified self-compilation of agent trajectories | 2.5 to 3.0, 3.0 to 3.5 | SGM (statistical Gödel machine), Auto (compiled programs behind conformal guards) | Dropped: both the framing and the mechanism exist |
| Subgroup drift under accept-if-better loops | 3.5, 3.5 | SAGE, item-level transitions in prompt optimization, CVaR-RMD, classical correlated-response theory | Kept after reframing as a forecastable correlated-response law with a dose-response test (proposal 6); reviewer estimate about 4.5 if reframed |
| Context steering an agent's measurement | 3.0, 3.5 | Agentic forking paths and the m-value, Epistemic Blinding, stage-resolved bias in search agents | Kept after reframing as "calibration bug or information bug" with path splicing (proposal 8); reviewer estimate about 4.3 and 4.4 if reframed |

The red-team reviewer also proposed a replacement in which label-free agreement rewards teach an agent to pick instruments that fail together. It was not adopted because it reuses the shared-error mechanism of [proposal 1](01-learning-with-biased-references.md).

## What the theory checks established

Before drafting, a separate agent derived the formal claims and checked them by Monte Carlo simulation (`output/idea-summaries-build/sim/` and `research/theory-checks.md`).

- **Proposal 6.** The closed form for a subgroup's expected change under mean-based acceptance was exact across 1,344 parameter settings (largest error 0.023 of the majority effect's spread). The sign condition is sufficient, not necessary, and best-of-$K$ selection scales the selection term without changing its sign. A cumulative tail-harm guarantee holds when gate data are fresh or sealed. It fails when the same tail people are reused every round (realized error 0.11 to 0.29 at a nominal 0.05), which is why the proposal moves certification to a domain with fresh tail data.
- **Proposal 8.** The double-counting result was proved in the stated Gaussian setting. When the clinician already uses the referral as a prior, any shrinkage of the measurement toward the referral raises expected log loss, even over a range where it lowers mean squared error; the simulation checks found no violations in 360 settings. Path splicing identifies the four cells of a two-by-two factorial by intervention, provided a self-splice placebo passes.
- **Proposal 5.** Detecting a change in single-edit success from 0.10 to 0.15 needs about 1,000 edits per arm when edits are clustered by seed. Claims about harnesses in general need ten or more independently written base harnesses, and showing that the one-step profile beats descendant counts needs about 100 configurations.
- **Proposal 7.** A reader's error was written as the tool floor plus an information term plus a perceptual term, using Bayes risks. The note also states the conditions under which the split is meaningful, including an oracle that reads the same input as the model.

## Drafting and Codex review

Four agents drafted the proposals in parallel, each owning one document, one figure script and one image folder, with eight vector figures per proposal drawn from a shared style library. Every figure was rendered, linted for overlapping labels and lines crossing text, and inspected as an image. Two Codex passes then reviewed each proposal: a visual review of the rendered figures, and the codex adversarial-review prompt applied to the document and its figures.

| Proposal | Codex findings, first stage | Fixed | Declined with a reason |
|---|---|---|---|
| 5 | 30 | 27 | 2 |
| 6 | 39 | 36 | 3 |
| 7 | 36 | 29 | 7 |
| 8 | 38 | 30 | 8 |

The adversarial findings changed the designs, not only the wording. Examples include charging missing scores in proposal 5's primary endpoint, separating the tail's objective weight from its evaluation size in proposal 6, splitting each plot gain into computation, shared perception and reader-specific parts in proposal 7, and routing all four splice cells in proposal 8 through one report interface so replay artifacts cannot pose as path effects.

## Independent review and final revision

A fresh reviewer for each proposal, who had not seen the drafts, wrote a review that put readability and conceptual clarity first. It followed with an ICML-style assessment, a spot-check of the eight most load-bearing citations against their links, and a figure-by-figure critique. All four drafts received soundness 3 of 4, presentation 2 of 4, contribution 3 of 4 and overall 6 of 10, with confidence 4 of 5. Presentation was the weakest score, so the final revision concentrated on it. A reviser then applied the suggestions, closed the figure issues left open by the first stage with another Codex visual round, and ran a second Codex adversarial pass on the revised text.

| Proposal | Review items applied | Declined | High-severity Codex findings in the second pass | Resolved |
|---|---|---|---|---|
| 5 | 95 | 3 | 5 | 5 |
| 6 | 92 | 0 | 6 | 6 |
| 7 | 81 | 1 | 4 | 4 |
| 8 | 76 | 2 | 4 | 4 |

The revisions defined each proposal's design vocabulary before its hypotheses, renamed overloaded symbols and added a table linking each hypothesis to its test and falsifier. They split long sentences and kept each document near 5,900 words. Several scientific fixes also came from this pass. Proposal 5 now runs the full factorial for the frontier proposer and guards against edits that win by shrinking toward the mean. Proposal 6 moved certification off StaBLE, where about five fall-risk people per fold cannot support it. Proposal 7's primary test must beat a forecast that ignores the profiles. Proposal 8's power was recomputed by Monte Carlo and its decision-quality claim is confirmed on EchoNet-Dynamic.

## Verification of the final documents

- A script checked every document for em-dashes and en-dashes, banned words, unresolved image links, citations without a matching reference, references never cited, staccato runs and a LaTeX operator macro that GitHub does not render. All four pass.
- The 130 references carry 112 unique links. 101 return HTTP 200. The other 11 are publisher DOIs (IEEE, JAMA, Taylor and Francis, Oxford, ACM, Annual Reviews, SAGE, INFORMS, CMAJ, ACP) that refuse automated clients, and each resolves through doi.org to the right article page.
- Every figure is embedded and cited, captions run in order, and no SVG contains a dash character. The README overview figure went through two Codex visual rounds and three redraws.

## What remains open

- **Figures.** The last round of figure fixes in each proposal was checked by eye and by the lint script but not sent to Codex again. Some Codex suggestions were declined because they conflicted with earlier rounds or with the running example; the reasons are in each `reviews/NN-final-resolutions.md`.
- **Proposal 5.** The sealed participants were scored once in the lab pilot, so a confirmatory claim needs a fresh cohort. Tier-2 claims rest on three base harnesses and one proposer, and the frontier proposer is to be named and pinned at registration.
- **Proposal 6.** StaBLE carries the forecast and tool attribution but not the protective gate, which is tested on Global-MMLU. The block-level gate protects harnesses at the end of each block, a weaker guarantee than the per-generation design simulated.
- **Proposal 7.** The primary test rests on 12 held-out VLMs, and the sealed participants are the pilot's test set. The second adversarial pass predates the last text changes made in response to it.
- **Proposal 8.** The gate on measurement quality may fail, since the pilot's tool pipeline scored worse than a constant guess, so later experiments depend on stated fallbacks. The optimizer comparison is limited to the configurations tested and cannot isolate a mechanism.
- **All four.** Compute totals rest on throughput assumptions that each proposal measures on a small pilot first, and none of the proposals contains empirical results yet.
