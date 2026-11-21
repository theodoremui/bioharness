# Research-proposal snapshot revision and adversarial review

Scope: the seven proposals in `docs/ideas-claude-explained/` and their corresponding build sources. Reviewed on 2026-11-05.

The proposals now begin with a highlighted scientific question, followed by the rationale, a focused study and the interpretation of possible results. They contain no abstract that repeats the question, tutorial background, implementation walkthrough, feasibility discussion, schedule or appendix. Citations remain next to the claims they support. Original filenames are preserved.

## Length and scientific focus

Counts include headings, tables and inline citations, using whitespace-separated words.

| Version | Before | After | Primary scientific focus |
|---|---:|---:|---|
| v1 | 2,430 | 514 | Feature-based estimation versus direct score prediction |
| v2 | 2,495 | 507 | Preservation of differences between participants |
| v3 | 2,753 | 549 | Feature rewards and compensating measurement errors |
| v4 | 2,636 | 563 | Transfer from privileged teacher demonstrations |
| v5 | 2,866 | 580 | Transfer of checked computations across tasks |
| v6 | 2,818 | 568 | Added value of known-answer checks |
| v7 | 2,955 | 622 | Physical consistency under movement transformations |
| Total | 18,953 | 3,903 | 79.4% reduction |

## Review method

The editing agent conducted two separate adversarial passes. The first challenged whether each experiment could answer its stated question, using alternative explanations and counterexamples. The second reread the revised documents for residual confounding, leakage, metric ambiguity, unsupported conclusions and unnecessary detail. This was an author-side review, not an independent external-model review.

Primary sources were checked for the retained factual claims: [StaBLE](https://pmc.ncbi.nlm.nih.gov/articles/PMC13621976/), [OpenCap Monocular](https://arxiv.org/abs/2603.24733), [BiomechAgent](https://arxiv.org/abs/2602.06975), [ToolRL](https://arxiv.org/abs/2504.13958), [process supervision](https://arxiv.org/abs/2305.20050), [privileged-information distillation](https://arxiv.org/abs/2602.04942), and the [StaBLE analysis repository](https://github.com/stanfordnmbl/stable-analysis). Internal pilot claims unnecessary to the shortened arguments were removed.

## Findings and resolutions

| Finding or adversarial challenge | Resolution |
|---|---|
| Research questions were dominated by model specifications, training conditions and numerical decision rules. | Questions now name a scientific relationship. Essential matching conditions appear only in the study. Arbitrary success margins, schedules and implementation stages were removed. |
| Repeated explanations and figures displaced the proposal's main idea. | Removed duplicate abstracts, tool and training tutorials, worked trajectories, pipeline diagrams and broad literature surveys. Retained brief, directly relevant source attribution. |
| A system can improve because it receives better tools or richer labels, without demonstrating a benefit from adaptive analysis. | v1–v2 match available inputs, include fixed-pipeline and feature-predictor controls, and limit conclusions about adaptive tool use. v1 evaluates intermediate errors only for methods that actually produce features. |
| Good ordering can coexist with compressed differences; low absolute error need not imply either good ordering or measurement. | v2 separates rank correlation, numerical error and calibration slope. Its interpretation distinguishes relative ordering from the magnitude of differences. |
| Swapping a video while retaining incompatible camera or body metadata can invalidate reconstruction. | v2 carries over reconstruction metadata and identifies the swap as an input-dependence diagnostic that does not isolate movement from appearance. |
| Cancelling feature errors do not imply worse rankings on unseen participants. | v3 makes this a testable hypothesis, uses feature error as the primary outcome, and defines cancellation on direction-aligned normalized features. Score error and ranking remain downstream outcomes. |
| Changing teacher access and reward design together prevents attribution to the teacher. Different accepted examples can also explain a student gain. | v4 isolates reference access, compares students before reinforcement learning, and uses matched participant–task demonstrations accepted in both conditions. It reports acceptance rates and acknowledges the restriction to this shared subset. |
| The later proposals combined reward design, teaching, tool-cost prediction and task transfer into competing research programs. | v5 centers task transfer, v6 isolates known-answer checking, and v7 isolates expected physical responses. Tool-cost modeling and optimization stages were removed; shared teaching is only a control where needed. |
| Passing known examples may reflect memorization; capped features can let constant programs pass. | v5–v6 separate reward probes from audit examples, include deliberately wrong functions, and state the limit of probes with indistinguishable values. v6 separates physical limits from merely unusual training-range values. |
| v6 initially changed replay and physical checks alongside known-answer checking. | Replay and physical-validity checks are now shared. The primary comparison changes only the addition of known-answer checks. |
| A constant predictor can appear physically consistent if invariant features dominate the metric. A duration-only shortcut can pass uniform slowing. | v7 measures changes in responsive features as the primary outcome, adds a no-change baseline, and reports invariants separately. Held-out full-video transformations include changes within fixed-duration clips, with expected changes recomputed from reference trajectories. |
| Verification-based replacement of submitted values can favor the condition trained to pass the validator. | v3 and v5–v7 evaluate submitted features directly. Check results remain diagnostics, rather than a scoring advantage. |
| A lower error can result from greater fallback use. | All proposals report failures and include both the common-fallback comparison and a sensitivity comparison restricted to cases completed by both methods. The restricted comparison is diagnostic, not a replacement for the primary population. |
| Participant leakage, substituted references and task-calibration labels can inflate generalization claims. | Retained participant separation, training-only fitted components and measured, unflagged primary references. Dataset reuse is explicitly retrospective. v5 discloses labeled calibration support and possible overlap in feature types across tasks. |
| Agreement with a reconstructed reference and passing finite checks were liable to be read as proof of measurement or clinical validity. | Every interpretation limits its claim. Finite-check behavior, reference agreement, task transfer and clinical validity are distinguished. Negative and inconclusive interpretations remain available. |
| Historical build sources could regenerate the discarded tutorials. | Replaced all seven active sources with synchronized concise versions. Unused background parts, figures and earlier review files remain historical assets and are not included by these proposals. |

All actionable findings from these passes were addressed. Remaining limitations are explicit scientific boundaries: shared reconstruction assumptions, retrospective evaluation, finite probe coverage and limited transfer claims.

## Verification

- Rebuilt all seven documents into a temporary directory and verified byte-for-byte equality with the delivered Markdown.
- Checked that every document starts with its single highlighted research question and uses the same four-section structure.
- Checked table structure, local link targets, whitespace and unresolved build directives.
- Confirmed the absence of feasibility material, appendices, deadlines, hardware budgets and obsolete figure or section references in both the delivered documents and active sources.
- No research experiment was run; this verification concerns the proposal documents and their generation.
