# Learning Balance Measurements from Feature-Level Rewards

## Research question {-}

> **Does rewarding individual biomechanical features reduce compensating measurement errors and improve generalization to new participants compared with rewarding only an aggregate balance score?**

A correct average can conceal incorrect components. When a task score combines several features, overestimating one and underestimating another can yield an accurate score without accurate measurements. The question is whether the training objective changes this behavior on new participants.

## Scientific rationale {-}

StaBLE task scores average rescaled features; its three-camera estimates make errors in those components observable. [Heigold et al. (2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13621976/). We hypothesize that rewarding each feature reduces compensating errors that an aggregate-score reward leaves unpenalized. Whether this also improves score accuracy or participant ordering is an empirical question: smaller feature errors do not guarantee better rankings.

Process supervision has improved mathematical reasoning, and ToolRL studies reward granularity for tool use. Neither result establishes that intermediate rewards improve physical measurements inferred from video. Here the supervision concerns defined biomechanical quantities, rather than written reasoning steps or tool-call correctness. [Lightman et al. (2023)](https://arxiv.org/abs/2305.20050); [Qian et al. (2025)](https://arxiv.org/abs/2504.13958).

## Study {-}

Train the same single-camera, tool-using agent under three reward conditions:

| Condition | Training signal |
|---|---|
| Aggregate score | Agreement with the reference task score |
| Individual features | Agreement with each reference feature |
| Individual features with checks | The same feature reward, with penalties for computations that fail replay or input-dependence checks |

The primary comparison is individual-feature versus aggregate-score training. The third condition tests the additional value of basic computation checks. All conditions share the initial model, demonstrations, tool access, training examples and training exposure, with rewards placed on a common range. Any supervision of event timing is also identical. Three-camera measurements supply targets, never inputs to the student.

The primary outcome is feature error on new participants: report errors in physical units and a summary using training-derived feature scales, with tasks weighted equally. On features normalized in the direction used by the task score, compare average absolute error with the absolute average signed error; the gap quantifies cancellation. Report task-score error and within-task rank correlation as downstream outcomes.

Replay checks whether submitted code reproduces its value. Input-dependence checks whether it changes across examples with different reference values. Neither establishes that the computation measures the intended feature. Audit deliberately incorrect programs, including constants and functions driven by irrelevant signals, to determine what these checks actually reject.

Score all conditions from submitted features, regardless of check status. Apply a common training-derived fallback to missing outputs, report their frequency, and repeat error comparisons on cases completed by both methods. Keep participants separate across training and evaluation; derive demonstrations, checks and normalization only from training data. Exclude estimated replacements for missing references and flagged reconstructions from primary rewards and evaluation. All fitted components exclude evaluation participants, and conclusions acknowledge retrospective dataset reuse. Uncertainty includes participant and training-run variation.

## Interpretation {-}

Lower feature error with less cancellation would support the proposed mechanism. Improved task-score accuracy alone would not. If basic checks add no benefit, feature supervision may account for the improvement; if they reject valid computations, they may impede learning.

Agreement with three-camera estimates remains the scope of the claim. Shared reconstruction errors can persist even when every feature receives its own reward.
