# Transferring Measurement Knowledge from a Privileged Teacher

## Research question {-}

> **Can a teacher's access to multi-camera motion measurements improve a student's single-camera estimates of balance-related features when those measurements are unavailable at evaluation?**

A richer measurement can reveal errors that are ambiguous in one camera view. The scientific question is whether this information helps a teacher produce demonstrations from which a student learns useful measurement strategies, or encourages decisions the student cannot infer from its own observations.

## Scientific rationale {-}

Privileged-information distillation studies learning from a teacher that receives information unavailable to the student. Transferring successful actions is difficult when those actions depend on hidden information. [Penaloza et al. (2026)](https://arxiv.org/abs/2602.04942).

Here the extra information is a three-camera motion estimate from StaBLE. [Heigold et al. (2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13621976/). The hypothesis is that it helps the teacher identify event boundaries and diagnose faulty single-camera estimates, producing more informative demonstrations. Restricting the teacher to the student's tools makes its actions executable by the student, but does not ensure those actions are learnable from single-camera evidence.

## Study {-}

Generate demonstrations with the same teacher under two conditions: access to single-camera observations alone, or access to those observations plus the corresponding three-camera curves. Both teachers use the same measurement tools and undergo the same reference-based quality filtering. Use the same participant–task examples accepted in both conditions for the primary comparison, matching demonstration counts. Report acceptance rates separately to expose differences in coverage.

Train identical students on the two demonstration sets. The students receive only single-camera observations, task definitions and the metadata required by the shared tools. Remove the reference panel and explicit reference-derived answers from demonstrations. Retain computations that can be replayed on student-accessible inputs and tested on other development recordings. These restrictions reduce direct copying; they cannot remove every decision influenced by privileged information.

The primary comparison is feature error immediately after demonstration training, before any reinforcement learning can obscure the teacher's contribution. A secondary comparison asks whether the difference persists after both students receive the same per-feature reward and computation checks. Hold subsequent training exposure and timing supervision constant.

Evaluate feature errors in physical units and summarize them with training-derived scales, weighting tasks equally. Report event-boundary errors, task-score error and within-task rank correlation to locate any benefit. Compare teacher and student performance on the same development examples: a strong privileged teacher with no student gain would suggest that its advantage did not transfer.

Keep every participant's recordings on one side of the training–evaluation split. Demonstrations, acceptance thresholds, probe examples and normalization come only from training participants. Use measured, unflagged references for primary evaluation, apply identical fallbacks to failed predictions, and report failures. Repeat error comparisons on cases completed by both students. Rebuild all fitted components without evaluation participants and describe dataset reuse as retrospective. Uncertainty reflects both participant differences and variation in demonstration generation and student training.

## Interpretation {-}

Lower student feature error would support transfer through privileged demonstrations on the matched examples. This restriction may favor easier recordings and excludes any benefit from increased demonstration coverage. It would not show that the student acquired every strategy used by the teacher, or that all of the benefit came from better event localization.

No improvement, despite stronger teacher demonstrations, would count against this transfer mechanism. Because the reference is reconstructed motion, any gain establishes closer agreement with that reference; it does not independently validate the inferred biomechanics.
