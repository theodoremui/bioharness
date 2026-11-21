No files were edited. Line numbers refer to the [current proposal](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v6_simplified-reward-what-can-be-checked.md); Figure 4 is the [pipeline SVG](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/pipeline_v5_v6.svg).

The prior findings, in their original order:

1. **Resolved — timing supervision:** The question explicitly holds it fixed, and every reward arm receives the same timing penalty.
2. **Resolved — evaluation-time replacement:** Every arm now uses identical checking and fallback rules; scores from original submissions are reported separately.
3. **Resolved — prior participant exposure:** Starting models and demonstration sets explicitly use development participants only; the retrospective-reuse limitation remains disclosed.
4. **Resolved — motivation for ranking:** The rationale now predicts fewer person-specific errors and higher rank agreement, although its new causal wording overstates that hypothesis; see below.
5. **Resolved — cancellation in the movement diagnostic:** Feature responses are now reported for every reward arm; retaining score-level S4 as a supporting comparison is internally consistent.
6. **Resolved — checks presented as proof:** The text explicitly says passing checks does not establish correct measurement on new videos; a narrower contradiction concerning constant probes remains below.
7. **Partly resolved — reward definition:** Units and penalty sign are fixed, but “Minus the average feature error” still leaves submitted versus replacement values unspecified (line 67).
8. **Resolved — task-transfer support:** S5 explicitly uses labeled support shared across methods, and the primary average excludes tasks withheld from training.
9. **Resolved — undeclared cost-aware reward arm:** The cost penalty has been removed from Figure 4.
10. **Partly resolved — logistics:** Most planning details are gone, but “Development participants form five folds” remains (line 81), alongside Figure 4’s “Sealed · 60 people” and “Development · 111 people in 5 folds.”
11. **Partly resolved — repetition:** Supporting infrastructure and related work are shorter, but “A worked trajectory” (line 73) repeats Figure 6B; retaining that illustration is acceptable, though the duplication remains.
12. **Partly resolved — undefined terms:** Trajectories and reinforcement learning are explained, but “pose confidence” (line 71) and Figure 4’s “Calibration slope” remain unexplained.
13. **Resolved — observational result described causally:** The revised sentence reports observed verification-skipping without attributing it to outcome training, consistent with [Thaman’s benchmark](https://arxiv.org/html/2605.02964v1#S8).
14. **Resolved — excessive generalization:** The expected positive conclusion is limited to single-camera balance assessment and motivates further tests.
15. **Resolved — cancellation example:** The prose now correctly identifies overestimated upward speed and underestimated plantar flexion.

New or still-serious problems, most severe first:

1. **High — the normalization used by the proposed experiment is ambiguous.**  
   **Quote:** “using the lowest and highest values among all 180 participants” (line 33), versus Figure 4’s “Endpoints … come only from each fold’s training part.”  
   **Why:** The first statement accurately describes published StaBLE, but the proposal never clearly distinguishes that historical scale from its experimental scale. Feature-specific rescaling changes their relative contribution to the averaged task score, potentially changing the reference ordering itself. Using all-participant endpoints would also contradict the figure’s separation rule.  
   **Fix:** Explicitly distinguish the two: “Published StaBLE uses all participants; this study fits rescaling endpoints on training participants only and applies those same endpoints to predictions and references.” State whether values beyond those endpoints remain outside 0–1 or are clipped.

2. **High — malformed answers can earn a better reward than valid submissions.**  
   **Quote:** “minus 0.5 for each failed check” and “gives −2 to an unparseable answer” (lines 67–69).  
   **Why:** Five failed checks yield at most −2.5 before measurement or timing error. An agent can therefore improve its reward by deliberately producing an unparseable answer. Even fewer failures can cross −2 once the other penalties are included.  
   **Fix:** Bound the combined valid-submission loss and make the malformed-answer penalty strictly worse than that bound. Apply a consistent failure convention across arms.

3. **High — the checked arm’s central reward remains incompletely defined.**  
   **Quote:** “Minus the average feature error, minus 0.5 for each failed check,” paired with “Replaced by the training average” (line 67).  
   **Why:** Unlike the other rows, this does not say which values enter the error. Penalizing the original wrong value and penalizing its fallback produce different learning incentives; replacement in the final score does not settle this question.  
   **Fix:** Specify “mean absolute error after failed features are replaced by their training averages,” if intended, or explicitly say “mean absolute error of the submitted values.” Keep that definition consistent with Figure 4.

4. **Medium — the shortcut-test requirement contradicts the equal-answer exception.**  
   **Quote:** “When the probe answers are all equal … only closeness counts” and “a suite of deliberate shortcut programs must fail the check” (line 55); Figure 5 includes “typical values” among those programs.  
   **Why:** If every reference hold is five seconds, `return 5` passes closeness, replay and range. The stated tests cannot reject that constant program. Selecting “two slow risers and two fast risers” also guarantees no variation in other features or applicability to other tasks.  
   **Fix:** Describe probes as spanning the reference values of the particular feature, with slow/fast risers as the speed example. Explicitly exempt constant-reference cases from the constant-rejection guarantee and acknowledge their weaker check.

5. **Medium — the new ranking rationale states an untested mechanism as fact.**  
   **Quote:** “Offsetting errors like these are tuned to the training videos and become person-specific errors on new people, which scramble the ordering” (line 13).  
   **Why:** Cancellation does not establish either training-specific tuning or poorer ordering on new participants. Errors could continue to cancel, or remain too small to change ranks; this is precisely the hypothesis the experiment should test.  
   **Fix:** Replace with: “We hypothesize that final-score rewards encourage cancelling errors that generalize poorly to new people, and that checked per-feature rewards reduce the resulting ranking errors.”

6. **Medium — Figure 4 retains an unexplained optimization step.**  
   **Quote:** “Prompt and harness / search, no weights” and “updates harness or weights,” versus “Reward and check are the intervention” (line 49).  
   **Why:** The figure does not establish whether this search is shared preparation, an additional comparison, or something performed separately for each reward arm. Separately optimized prompts or harnesses could introduce another difference into the primary comparison.  
   **Fix:** Label it as shared preparation producing the same fixed prompt and harness for all reward arms, if intended; otherwise remove the unexplained search box.

7. **Medium — prohibited allocation planning remains, especially in the figure.**  
   **Quote:** “Development participants form five folds” (line 81); Figure 4: “Sealed · 60 people,” “Development · 111 people in 5 folds,” and “60 people, all eligible tasks.”  
   **Why:** These are planned allocations, which the requested snapshot explicitly excludes. Removing them from one paragraph while retaining them in the overview does not resolve the requirement.  
   **Fix:** Use “development participants” and “held-out evaluation participants,” retaining participant separation and training-only fitting without allocation counts or fold diagrams.

8. **Medium — important passages still exceed the stated reader background.**  
   **Quote:** “one family corrected with Holm’s procedure” (line 21), “pose confidence” (line 71), “bootstrap resample” (line 89), and Figure 4’s “Calibration slope.”  
   **Why:** These terms carry methodological meaning but receive no plain-language explanation. The long success-rule sentence also combines uncertainty, two metrics and a mathematical threshold before explaining their practical meaning.  
   **Fix:** Briefly explain pose confidence as confidence in estimated body-joint positions, bootstrap as repeated resampling to estimate uncertainty, and Holm correction as controlling false positives across several comparisons. Remove the unused calibration-slope label and introduce the decision rule as “better ordering without a meaningful loss of numerical accuracy” before giving its threshold.

The document is not yet ready as a finished proposal snapshot. Its central question is now coherent, but the reward definition and incentives, normalization ambiguity, figure inconsistencies and remaining logistics need correction.