# Preserving Individual Differences in Video-Based Balance Assessment

## Research question {-}

> **Do tool-derived biomechanical features preserve differences in balance performance between people better than direct video-to-score prediction?**

A predictor can achieve a small average error by staying close to typical performance. The scientific problem is whether it captures who performs better and how much participants differ, rather than merely approximating the population's score distribution.

## Scientific rationale {-}

Three properties distinguish an informative prediction from a plausible population estimate. Absolute error measures numerical agreement, rank correlation measures ordering, and the spread of predictions indicates whether differences are compressed. A predictor can preserve ordering while shrinking every difference.

The hypothesis is that features computed from each participant's movement preserve more individual information than direct score prediction. Appearance is an alternative source of such information: StaBLE scores are associated with age, so better ordering alone cannot establish sensitivity to movement. [Heigold et al. (2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13621976/).

## Study {-}

Compare a tool-using feature estimator with a direct predictor built from the same vision-language model, using the same single-camera videos, participant split, task descriptions and available metadata. A fixed pipeline and a predictor trained on fixed tool outputs and feature labels test whether any advantage requires adaptive analysis. A training-median predictor, a demographic model and a single-frame model establish how much can be predicted without observing movement over time.

The primary outcome is Spearman rank correlation between predicted and reference task scores, computed within each task and averaged across tasks. Report absolute score error and the slope of predicted against reference scores alongside it. A slope below one indicates compressed differences, but does not by itself imply poor ordering. Constant predictions receive zero ordering credit; tasks with constant references are excluded from rank comparisons for every method alike.

To examine input dependence, replace each video with another person's recording of the same task, carrying over the camera parameters and body dimensions needed for valid reconstruction. Predictions should track the replacement recording's reference. Appearance and metadata also change, so this diagnostic complements the appearance controls without isolating the contribution of movement.

Evaluate every method on the same recorded trials with usable video and measured, unflagged references. Failed predictions receive the same training-derived baseline, and their frequency is reported separately. Repeat the comparison on cases completed by both methods. Keep participants separate across training and evaluation, derive normalization from training participants, and apply it equally to predictions and references without clipping. Refit every component without evaluation participants; reuse of the pilot dataset remains retrospective. Estimate uncertainty across participants and repeated training runs.

## Interpretation {-}

Better ordering with preserved numerical accuracy would support improved discrimination between participants. Improved ordering accompanied by compressed predictions would support a narrower conclusion: the method identifies relative performance but understates its magnitude. Numerical tradeoffs must remain visible rather than being hidden inside a single success threshold.

If appearance controls perform similarly, the contribution of movement remains uncertain. These experiments assess agreement with reconstructed balance-task performance, not an independent clinical measure of balance or the ability to detect change within one person.
