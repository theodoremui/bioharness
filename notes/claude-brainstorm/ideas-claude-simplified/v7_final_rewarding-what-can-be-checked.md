# Testing Whether Balance Estimates Follow the Movement

## Research question

> **Do checks of a feature's expected response to movement changes improve the physical consistency of single-camera balance estimates beyond feature-accuracy rewards and known-answer checks?**

A function can reproduce known answers while relying on an irrelevant signal. The scientific problem is whether training against the expected behavior of a physical quantity makes the learned measurement more faithful to changes in movement, including changes absent from training.

## Scientific rationale

A measurement has implications beyond its value on one recording. Changing the temporal pattern of movement should change speed-related features in predictable ways, while some geometric features should remain invariant. StaBLE's feature definitions and released analysis code provide explicit quantities whose responses can be evaluated. [Heigold et al. (2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13621976/); [StaBLE analysis code](https://github.com/stanfordnmbl/stable-analysis).

The hypothesis is that checking these responses discourages functions that memorize probe answers or depend only on annotations. This adds a scientific constraint to reward design for tool use: agreement with reference values must be accompanied by the expected dependence on the measured signal. [Qian et al. (2025)](https://arxiv.org/abs/2504.13958). Passing a finite set of checks remains compatible with other shortcuts, so the hypothesis requires an independent test.

## Study

Compare two agents trained with identical per-feature rewards, replay checks and known-answer probes. Only one also receives penalties when its computations respond incorrectly to prescribed edits of the relevant body signal. A feature-specific rule might require estimated peak speed to increase when a center-of-mass rise becomes steeper. Establish valid responses and tolerances on development data, respecting feature definitions, saturation and physical constraints.

Match the starting model, demonstrations, tools, training exposure, reward scaling and event-timing supervision. Both students operate on single-camera observations. The checks use development reference examples and fixed response rules; they never receive the current evaluation recording's reference. Evaluate event localization separately because correct behavior given fixed annotations does not establish that the agent found the right movement interval.

The decisive test uses transformed full videos, rather than only editing intermediate tool signals. Prespecify transformations that preserve valid task executions and withhold them from training, including changes to movement speed within clips of unchanged total duration. Transform the corresponding reference trajectories in the same way and rerun the feature definitions to obtain expected changes, including any caps. A model using only clip duration should fail on changes that preserve total duration. Include that shortcut and a single-frame predictor as diagnostic controls.

The primary outcome is error in predicted feature changes relative to reference changes, restricted to features expected to respond. Summarize using development-derived scales, with tasks weighted equally, and compare with a no-change predictor. Report invariant features separately. Ordinary feature error on unmodified videos checks whether physical consistency comes at the expense of measurement accuracy. Task-score error and participant ordering are secondary. Audit constants, annotation-only functions and recording lookups on examples excluded from reward construction.

Evaluate submitted features directly, without replacing values that fail checks. Use identical training-derived fallbacks for missing predictions, report failures, and repeat comparisons on cases completed by both agents. Keep participants separate across training and evaluation; all demonstrations, probes, response rules and normalization exclude evaluation participants. Use measured, unflagged references for primary outcomes, and acknowledge retrospective dataset reuse. Uncertainty includes participant differences and repeated training runs.

## Interpretation

Smaller errors in feature changes, together with preserved accuracy on ordinary videos, would support improved physical consistency under the tested transformations. Better check-pass rates without that improvement would suggest adaptation to the training checks. A gain on synthetic transformations alone would not establish better measurement of naturally occurring movement differences.

The experiment evaluates dependence on movement and agreement with a reconstructed reference. Shared reconstruction assumptions and untested transformations limit the conclusion; broader biomechanical or clinical validity requires independent evidence.
