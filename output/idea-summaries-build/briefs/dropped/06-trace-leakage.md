# Brief for proposal 06: does reading its own failures make a self-improving agent overfit?

Output file: `docs/idea-summaries/06-overfitting-from-reading-traces.md`. Figures: `docs/idea-summaries/images/06/`. Figure code: `output/idea-summaries-build/figs_06.py`.

## Core question

When an LLM optimizer improves an agent by reading per-example execution traces from the same examples it uses to accept or reject candidates, how much of the measured improvement fails to transfer to new people? How does the gap scale with the number of examples, the number of iterations and the richness of the feedback channel, and which protocol recovers honest improvement at the smallest cost in real gains?

One-line thesis: reflective optimizers have turned the validation set into a training set with a very wide channel, and classical evidence that adaptive overfitting is mild (scalar leaderboards) does not transfer to optimizers that read every failure.

## Why it is open

GEPA, TextGrad, DSPy/MIPRO, ACE, Meta-Harness and DGM-style loops feed traces or per-example feedback back to a proposer. Adaptive data analysis (Dwork et al. 2015 reusable holdout; Blum and Hardt 2015 Ladder; Russo and Zou; Xu and Raginsky mutual-information bounds) shows that reuse of a holdout causes bias proportional to information leaked. Empirical studies (Recht et al. 2019 ImageNet; Roelofs et al. 2019 Kaggle) found modest adaptive overfitting, but their feedback was a scalar score. Trace feedback contains the inputs, intermediate outputs and errors of identifiable examples. Meta-Harness ablations show trace access helps; whether part of that help is memorization of the dev examples has not been measured with null controls. Check the literature report for any direct study and state the exact residual gap.

## Running biomechanics example

StaBLE dev sets have tens of people (the lab pilot evaluated on 43 test people; BioCV has 15). A trace reads: "participant 112, tandem stance, right foot occluded after frame 410, estimated sway 2.1 times the label". The optimizer writes a rule that fixes this clip (for example, "if ankle confidence drops below 0.31 after frame 400, clamp sway"). The rule can be a general fix for occlusion or a memorized patch. People contribute 18 tasks each, so per-trial splits leak identity; clinical extremes are rare, so rules about extremes are the most likely to be memorized. Generalize: a coding agent's harness tuned on 50 SWE-bench issues; a customer-service agent tuned on 30 dialogues.

## Definitions to include

Execution trace; reflective optimizer; feedback channel; adaptive data analysis; optimism gap (dev minus fresh-test score); reusable holdout and Thresholdout; Ladder mechanism; mutual-information generalization bound; canary (from privacy auditing).

Formal core: dev set $D$ of $n$ people, final artifact $h_T$ produced after $T$ rounds of feedback through channel $C$. Optimism gap $G=S_D(h_T)-S_{\text{pop}}(h_T)$. For a $\sigma$-sub-Gaussian loss, $|\mathbb{E}[G]|\le\sqrt{2\sigma^2 I(h_T;D)/n}$. Selecting one of $K$ candidates per round from scalar scores leaks at most $T\log_2 K$ bits; a trace channel can leak far more, so the bound becomes vacuous and the size of the gap is an empirical question.

## Method and experiments

1. Feedback-channel ladder at matched proposer, rounds and candidates: F0 aggregate score; F1 per-example scores; F2 per-example scores plus inputs and metadata; F3 full traces (tool calls, intermediate outputs, errors), the default in GEPA and Meta-Harness; F4 full traces plus labels shown.
2. Null-label memorization test in the spirit of Zhang et al. 2017: permute labels across people within each task, breaking the video-label link. Any dev gain is pure fitting capacity of the loop. Report dev gain under true and permuted labels by channel.
3. Canary audit borrowed from privacy (Carlini et al. 2019): insert a few dev examples with a distinctive, task-irrelevant marker (a metadata tag or a small watermark) and a deliberately shifted label. Rules keyed on the canary are direct evidence of memorization.
4. Scaling: $n\in\{10,20,40,80,160\}$ people and $T$ up to 200 rounds; fit the gap as a function of channel, $n$ and $T$; identify the stopping point where honest gain peaks.
5. Artifact forensics: rule specificity (share of conditions in the evolved code or prompt that fire on two or fewer dev people), leave-one-person-out influence on test error.
6. Protocols that bound leakage (method contribution): (a) diagnose/select/test split, traces visible only on the diagnosis split; (b) Ladder or Thresholdout for selection scores; (c) k-aggregated traces that report only failure patterns shared by at least k people, with identifiers stripped; (d) rotating diagnosis subsets; (e) early stopping from the selection split. Compare at matched labeled data on honest gain and on calibration of the reported gain.
7. Second domain with large test sets where published optimizer numbers exist (for example the GEPA tasks HotpotQA, IFBench, HoVer, PUPA, or an agentic benchmark such as AppWorld or tau-bench) so dev size can be varied while the test set stays large.

Analysis: primary outcome is fresh-test improvement and the optimism gap per channel; paired by seed; participant-level bootstrap; pre-register the channel contrasts.

## Figures (suggested)

1. Concept: dev curve rising, fresh-test curve flat after a point (illustrative).
2. Mechanism: one trace -> one patch rule -> fixes that clip only.
3. Feedback-channel ladder with leaked information increasing.
4. Null-label and canary tests side by side.
5. Three-way split protocol with what each split reveals.
6. k-aggregated trace summary vs raw traces.
7. Hypothetical scaling map of the gap over $n$ and channel.

## Falsifiers

Under permuted labels the dev gain of F3 is no larger than F0's; or fresh-test improvement tracks dev improvement within noise at $n=20$; or the protective protocols cost more honest gain than they remove in optimism.
