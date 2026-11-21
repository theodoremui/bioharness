Line numbers refer to the [proposal](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v6_simplified-reward-what-can-be-checked.md). No files were edited.

1. **High — research-question. The primary comparison changes an additional source of supervision.**  
   **Quote:** “the primary comparison tests per-feature rewards, the check and timing supervision together” (line 78).  
   **Problem:** The highlighted question names feature rewards and checking, but timing supervision could independently explain an improvement. Matching starting models and training trajectories does not resolve this confound.  
   **Fix:** Hold timing supervision fixed across the primary arms. Shorten the question to: “With the starting model, tools, training data and timing supervision fixed, do checked per-feature rewards improve within-task rank agreement with three-camera scores on new participants compared with final-score rewards?”

2. **High — research-question. Training effects may be mixed with evaluation-time replacement effects.**  
   **Quote:** “Not checked” versus “Replaced by the training average and penalized” (reward-arm table, lines 74–76).  
   **Problem:** The document does not establish whether this difference persists during evaluation. If only the checked arm replaces failed features, improved scores could come from that replacement rule rather than anything learned during training.  
   **Fix:** Specify identical evaluation-time checking and fallback rules across reward arms, and report scores from the original submissions separately.

3. **High — inconsistency. “Unseen people” is not established by the proposed retrospective split.**  
   **Quotes:** “order unseen people” (line 9); “Because the pilot trained models on some of them, this is a retrospective re-split” (line 82).  
   **Problem:** The caveat is candid, but the proposal never says whether the common fine-tuned starting model retains that exposure. Sealing participants now cannot remove information already incorporated into a checkpoint.  
   **Fix:** Explicitly require every study-specific starting checkpoint, demonstration set and fitted component to exclude evaluation participants. Retain the retrospective-data-reuse limitation without calling this an untouched confirmatory sample.

4. **Medium — research-question. The mechanism does not yet motivate the chosen primary outcome.**  
   **Quote:** “its error can never exceed the average feature error, so a high reward implies an accurate score” (line 55).  
   **Problem:** This argument concerns absolute score error, whereas the primary outcome is rank agreement. Smaller feature errors need not improve ordering, and appearance-based predictions can rank people well. Figure 1 itself gives the final-score method the more accurate score.  
   **Fix:** Add the actual prediction: “We hypothesize that checking individual features reduces person-dependent shortcut errors on new videos, improving rank agreement.” Describe ranking success as improved reference agreement; reserve claims about measuring movement for the diagnostic evidence.

5. **Medium — research-question. The movement diagnostic permits the cancellation the proposal criticizes.**  
   **Quote:** “how often each method's change in task score falls within a preset tolerance of the change implied by the reference features” (line 84).  
   **Problem:** Incorrect changes in speed and hold time can cancel in the aggregate score. Comparing the final agent with a direct predictor also does not isolate whether the reward intervention caused improved movement sensitivity.  
   **Fix:** Test the expected changes in individual features for the same reward arms used in the primary comparison. Keep the direct predictor’s score response as a supporting comparison.

6. **Medium — overclaim. Passing probes does not remove measurement-free shortcuts.**  
   **Quote:** “Crediting a feature only when its code recovers known answers on other videos removes the first” (line 13).  
   **Problem:** The argument rules out an input-independent constant, not every shortcut. Code can exploit correlated cues or overfit the probe cases. This categorical claim conflicts with the later, appropriate statement that passing is “not a proof of measurement.”  
   **Replacement:** “Known-answer checks reject constant guesses and some other shortcuts, although passing them does not establish correct measurement on new videos.”

7. **Medium — clarity. The reward’s units and penalty sign are ambiguous.**  
   **Quotes:** “The reward adds up the error” (line 55); “Minus the average feature error, with 0.5 added for each feature that fails” (line 76).  
   **Problem:** Submissions contain seconds, angles and speeds; averaging their raw errors would give arbitrary weights. The error bound requires errors on the same normalized scale as the task score. “0.5 added” can also be read as increasing the reward for failure.  
   **Replacement:** “The reward is minus the mean absolute error of the features after training-set rescaling, minus 0.5 for each failed check.” State whether that error uses submitted or replacement values.

8. **Medium — clarity. Held-out-task transfer still uses task-specific labeled support.**  
   **Quote:** “their rescaling endpoints, fallback values and probe videos come from development participants' reference values for those tasks” (line 82).  
   **Problem:** These tasks are excluded from model training, but their labeled examples still configure the scoring and checking system. “Tasks never trained on” can therefore suggest a stronger form of transfer than is tested. It is also unclear whether these tasks enter the primary task average.  
   **Fix:** Describe this as “transfer to tasks excluded from model training, with labeled support for normalization and checking.” Give both comparison agents identical support and report these tasks separately under S5.

9. **Medium — figure-text-mismatch. The overview introduces an undeclared reward arm.**  
   **Figure:** [pipeline_v5_v6.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/pipeline_v5_v6.svg), containing “− λ · tool cost (cost-aware arm)”.  
   **Problem:** The prose specifies three reward arms, none with a tool-cost penalty. The figure therefore describes an additional intervention and makes the actual comparison uncertain.  
   **Fix:** Remove the cost-aware reward term from this figure. Tool-outcome prediction can remain a shared component without becoming another reward experiment.

10. **Medium — structure. Explicitly prohibited logistics remain.**  
    **Quotes:** “60 are sealed”; “The other 111 form five development folds” (line 82); “100 sealed videos” (line 84); “each reinforcement-learning arm uses three seeds” (line 90); “spending the same compute on more harness search” (line 98).  
    **Problem:** These are sample-allocation and compute-planning details, contrary to the requested snapshot format. Figure 4 additionally includes “8 rollouts per video” and “~4 GPU-min.”  
    **Fix:** Delete the planned counts, compute comparison and runtime estimates. Retain the scientific controls: participant separation, task separation, matched training conditions and treatment of invalid references.

11. **Medium — concision. Repeated explanation and supporting components obscure the central idea.**  
    **Quotes:** “The question tests one principle: reward the measurements, and only those that can be checked” (line 13); “four design choices that follow from the principle” (line 49); “A worked trajectory” (line 64).  
    **Problem:** The slogan repeats, while the abstract, numbered approach, walkthrough and Figures 4–6 repeatedly explain the same tool/check sequence. Teacher training and tool-outcome prediction receive nearly equal billing with the reward question. Related work then introduces another harness-search comparison.  
    **Fix:** Cut the worked-trajectory paragraph and Figure 6, retain the verification example, and compress the teacher and tool-outcome model into shared supporting infrastructure. Reduce related work to the specific gap addressed by checked feature rewards, and remove the repeated principle framing.

12. **Medium — undefined-term. Several central terms exceed the stated reader background.**  
    **Quotes:** “training trajectories” (line 9), “tool-feature regressor” (line 27), “pose confidence” (line 58), “calibration slope” (line 90); “SFT” and “GRPO” in Figure 4.  
    **Problem:** These are introduced without short explanations, including in the highlighted question and overview.  
    **Fix:** Gloss “training trajectory” as “a sequence of tool calls and results,” “pose” as “estimated body-joint positions,” and “tool-feature regressor” as “a model predicting scores from tool-produced features.” Define reinforcement learning as training through rewards. Remove nonessential algorithm acronyms and calibration slope from the snapshot.

13. **Medium — error. A cited observational result is presented as a learning mechanism.**  
    **Quote:** “tool agents trained on outcomes learn to skip verification” (line 98).  
    **Problem:** Thaman compares existing models and explicitly identifies its training comparison as observational; it does not isolate outcome rewards as the cause of verification-skipping. [The paper’s limitations](https://arxiv.org/html/2605.02964v1#S8) acknowledge this attribution limit.  
    **Replacement:** “A benchmark observed verification-skipping and other exploits in some tool-using models.”

14. **Medium — overclaim. The expected positive result is generalized far beyond the study.**  
    **Quote:** “rewarding checked measurements is a practical recipe wherever a better instrument exists only during training” (line 94).  
    **Problem:** One balance dataset cannot establish effectiveness across instruments, tasks or reference-error patterns. Having a better reference also does not ensure that useful known-answer checks can be constructed elsewhere.  
    **Replacement:** “A positive result would support checked per-feature supervision for this single-camera balance setting and motivate tests with other reference instruments.”

15. **Low — figure-text-mismatch. The cancellation example names the wrong features.**  
    **Quote:** “overestimating the ankle angle while underestimating hold time” (line 13).  
    **Figure:** [fig_cancel.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_cancel.svg).  
    **Problem:** Attempt A overestimates upward speed, underestimates ankle angle, and gets hold time right.  
    **Replacement:** “overestimating peak upward speed while underestimating peak ankle angle.”

The proposal presents a concrete reward-design hypothesis, but the current controls and diagnostics do not cleanly establish that checked rewards teach better measurement. Resolve those ambiguities, narrow the claims, and remove procedural and repeated explanatory material so the research question leads the snapshot.