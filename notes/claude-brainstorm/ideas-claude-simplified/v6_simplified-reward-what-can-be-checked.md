# The Added Value of Known-Answer Checks for Balance Measurements

## Research question

> **Do known-answer checks improve the accuracy of individual balance measurements beyond per-feature supervision alone?**

Giving a reward for every feature removes one ambiguity in an aggregate score: errors can no longer cancel unnoticed. It leaves another ambiguity unresolved, because a plausible feature value may come from a computation unrelated to the intended movement. This proposal isolates the additional value of checking that computation.

## Scientific rationale

Three-camera estimates in StaBLE provide reference quantities for training and evaluation. [Heigold et al. (2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13621976/). We hypothesize that requiring a feature function to reproduce known values on other recordings discourages recording-specific shortcuts and improves its accuracy on new participants.

ToolRL shows that reward design can influence tool use, while process-supervision research distinguishes intermediate feedback from final-answer feedback. The open question here is whether checking executable measurement functions adds value once intermediate quantities already receive direct supervision. [Qian et al. (2025)](https://arxiv.org/abs/2504.13958); [Lightman et al. (2023)](https://arxiv.org/abs/2305.20050).

## Study

Compare three reward conditions for the same single-camera agent:

| Condition | What training rewards |
|---|---|
| Final score | Accuracy of the aggregate task score |
| Per-feature | Accuracy of every submitted feature |
| Checked per-feature | The same feature accuracy, plus penalties for failing known-answer checks |

The primary contrast adds known-answer checks to per-feature training while holding basic checks fixed. The final-score condition establishes whether intermediate supervision helps at all. All conditions share the starting model, demonstrations, tools, training examples, training exposure and any event-timing supervision, with rewards on a common range. Teacher access to reference data is identical across conditions.

All conditions share replay checks on cited tool outputs and checks for physical validity. The added known-answer check applies each function to training probe recordings, using fixed event annotations to isolate the computation from event detection. Tolerances are fixed from development data. Probe values must differ enough to distinguish correct behavior from a constant; saturated features are identified separately. Physical constraints reject impossible values, while values outside the observed training range are flagged rather than automatically rejected.

The primary outcome is feature error on new participants, reported in physical units and summarized with training-derived scales and equal task weights. Task-score error, within-task rank correlation and event-boundary error are secondary. Independent audit examples test whether higher check-pass rates reflect broader correctness. Deliberately incorrect functions measure the check's susceptibility to shortcuts.

All evaluation scores use submitted features, regardless of whether they pass the check. A common training-derived fallback handles missing predictions; report their frequency and repeat error comparisons on cases completed by both methods. Keep participants separate across training and evaluation, exclude missing or flagged reference measurements from the primary analysis, and derive normalization and all checks without evaluation data. Refit every component on the permitted participants; reuse of this dataset remains retrospective. Uncertainty includes participant differences and variation across training runs.

## Interpretation

Lower error than per-feature training with basic checks would demonstrate an incremental benefit from known-answer checking. Beating final-score training alone would leave that benefit unresolved. Improved check-pass rates without lower independent feature error would suggest adaptation to the validator.

The check can establish reproducibility and accuracy on sampled examples, not correctness on every recording. Its use of fixed probe annotations also leaves the agent's own event detection to be evaluated separately. Conclusions concern agreement with reconstructed reference quantities, without establishing independent clinical validity.
