# Estimating Balance Through Biomechanical Features

## Research question

> **Does estimating defined biomechanical features from single-camera video improve agreement with three-camera balance scores, compared with predicting those scores directly?**

A balance score summarizes several aspects of movement. Predicting the summary accurately does not establish that its underlying quantities have been recovered. This proposal tests whether explicitly estimating those quantities provides a better basis for predicting balance performance in new participants.

## Scientific rationale

StaBLE defines balance tasks through physical features and combines them into task scores. Its multi-camera recordings provide a reference for comparing alternative single-camera estimates. [Heigold et al. (2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13621976/).

The hypothesis is that a feature-based representation constrains predictions to information about the observed movement and reduces errors on new participants. A competing explanation is that errors in single-camera reconstruction overwhelm any benefit from this structure. Monocular reconstruction estimates depth through modeling assumptions, so recovering the task's features cannot be taken for granted. [Gilon et al. (2026)](https://arxiv.org/abs/2603.24733).

## Study

Compare a vision-language model trained to predict task scores directly with an agent that uses pose and reconstruction tools to estimate the defined features, then applies the same fixed scoring rule. Both receive the same video, task information and available camera and body metadata. Match the starting model and training participants. The comparison concerns the complete feature-based approach, including its additional feature supervision.

Two controls distinguish possible sources of improvement: a fixed analysis pipeline using the same tools, and a predictor trained on the same tool outputs and feature labels without adaptive tool selection. These controls matter because useful measurement tools alone could account for an apparent agent advantage. BiomechAgent provides precedent for code-generating biomechanical analysis, but does not establish the benefit of this single-camera comparison. [Cotton and Leonard (2026)](https://arxiv.org/abs/2602.06975).

The primary outcome is mean absolute task-score error, averaged equally across tasks. For methods that produce features, compare errors in physical units against the fixed pipeline and feature predictor to reveal incorrect estimates concealed by a correct score. Report prediction coverage alongside accuracy; failed predictions receive a common training-derived baseline in the main score comparison and remain identifiable as failures. Also compare errors on cases completed by both methods.

Keep all recordings of each participant together across training and evaluation. Use only recorded trials with usable video and measured, unflagged references for the primary analysis. Fit score normalization on training participants and apply it identically to predictions and references, retaining values outside the training range. All fitted components must exclude evaluation participants. Reusing this previously studied dataset is a retrospective evaluation, and uncertainty must reflect both participant differences and variation across training runs.

## Interpretation

Lower score error would support feature-based estimation as a useful approach in this setting. Lower feature error would provide stronger evidence that the benefit reflects improved measurement. Matching the fixed pipeline or feature predictor would leave the contribution of adaptive tool use unresolved.

The three-camera reference is itself an estimate and shares some modeling assumptions with the single-camera tools. Agreement therefore supports reproduction of reference measurements; clinical validity and accuracy against an independent physical instrument remain separate questions.
