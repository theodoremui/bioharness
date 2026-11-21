1. **High · overclaim — Verification does not establish movement dependence.**  
   **Quoted text (§3.1):** “Passing shows that the number is reproducible and responds to the movement in other videos”; **§1:** “removes shortcuts”.  
   A function of static body proportions could differ between the two probe participants, reproduce reliably, and remain within range without measuring the intended movement. The response check does not even require the difference to have the correct direction.  
   **Fix:** Replace with: “Passing establishes reproducibility and variation across selected videos. Whether that variation reflects the intended movement remains an experimental question.” Change “removes shortcuts” to “is intended to reduce shortcuts”.

2. **High · research-question — The comparisons cannot establish that the teacher can be dropped.**  
   **Quoted text (§5):** “If only H2 holds, the reward carries the gain and the teacher can be dropped.”  
   H2 compares B with C, both using the privileged teacher. H4’s post-training comparison, C against A, measures the teacher’s contribution under final-score rewards. Neither tests its contribution under B’s verified feature rewards; the two components could interact.  
   **Fix:** Replace with: “If H2 holds, verified feature rewards help when combined with privileged teaching; the teacher’s contribution under those rewards remains unresolved.” Retaining the stronger conclusion requires a plain-teacher arm with verified feature rewards.

3. **High · research-question — The proposed mechanism does not directly predict the primary outcome.**  
   **Quoted text (H1):** “Final-score RL shrinks predictions toward the average”; **§1:** “The primary measure is **rank agreement**”.  
   Compression toward the average can preserve every participant’s ordering: multiplying score deviations by a positive constant leaves Spearman correlation unchanged. Reducing feature-error cancellation likewise need not improve task-score ordering.  
   **Fix:** State the missing prediction explicitly: “Feature-level feedback may reduce participant-specific errors that reverse score ordering.” Keep calibration slope as a subordinate test of compression, distinct from the explanation for improved ranking.

4. **High · structure — Substantial prohibited logistics remain.**  
   **Quoted text:** “at most 40 kept demonstrations per task”; “at three budget levels, each four times the last”; “100 sealed videos”. Also [fig_budget.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_budget.svg).  
   Demonstration quotas, seed counts, sample allocation, sampling schedules, GPU penalties and a budget-ladder figure make this an execution protocol rather than the requested snapshot.  
   **Fix:** Remove the Seeds column, numerical training schedule in §3.4, planned participant/video counts, cost-penalty arm and Figure 5. Preserve the arm definitions, participant separation and a brief qualitative statement of the continuation control.

5. **Medium · inconsistency — The control also receives supervision from the reference.**  
   **Quoted text (§2):** “this proposal tests whether using it in both the reward and the teacher's demonstrations is better than using neither.”  
   A’s final-score reward already depends on scores derived from the three-camera reconstruction. The contrast concerns access to richer reference information, rather than reference supervision versus its absence. “Exists only during training” also obscures its necessary use as the evaluation reference.  
   **Fix:** Use a shorter primary question: “With the base model, tools and training participants fixed, does reference-informed teaching plus verified feature rewards improve mean within-task Spearman agreement with three-camera scores on unseen participants, compared with teaching without reference access plus final-score rewards?” Specify that reference inputs are withheld from the evaluated agent.

6. **Medium · inconsistency — Equal trajectory counts do not establish equal compute.**  
   **Quoted text (§1):** “holding the base model, harness and compute fixed”; **§4:** “Arms are matched on the number of training trajectories, and their measured GPU time is reported.”  
   Trajectories can differ in length and tool use; verification and teacher generation add differing costs. Reporting GPU time does not make those costs equal. This undermines a condition stated in the primary comparison.  
   **Fix:** Remove the equal-compute claim from this snapshot and describe the training exposure that is actually controlled. Any retained equal-compute claim needs a consistent accounting rule covering teacher generation, training and verification.

7. **Medium · research-question — The primary success criterion changes conditionally.**  
   **Quoted text (§4):** “age-adjusted rank agreement becomes a second primary measure, and both must succeed.”  
   Even if this development-data rule is specified in advance, the proposal switches between two definitions of success. Agreement with reference scores and agreement after age adjustment answer different questions, weakening the requested single-primary-question structure.  
   **Fix:** Keep one primary endpoint throughout. Report age-adjusted agreement as a prespecified secondary diagnostic regardless of the demographic baseline’s performance.

8. **Medium · error — The primary metric lacks a rule for the collapse it is meant to detect.**  
   **Quoted text (§4):** “that case receives the training-fold task average and counts as a fallback in every metric.”  
   If all predictions for a task become the same fallback—or collapse to another constant—Spearman correlation is undefined. Silently dropping such tasks from the average would conceal an important failure. Constant reference scores create a separate undefined case.  
   **Fix:** State an explicit aggregation convention: for example, assign constant predictions zero rank information by evaluation convention, and handle tasks with constant reference scores using a method-independent rule.

9. **Medium · inconsistency — The participant counts do not reconcile.**  
   **Quoted text (§2):** “recorded 180 adults”; **§4:** “43 participants … are sealed” and “The other 128 form five development folds”.  
   The apparent development/test allocation totals 171, leaving nine participants unexplained. It is also unclear whether the previous 43 test participants are included in the 128.  
   **Fix:** For this snapshot, remove the allocation counts and retain: “Previously examined participants enter development; evaluation uses participants untouched during method development.” If counts remain, explain eligibility and exclusions.

10. **Medium · figure-text-mismatch — The shuffle figure claims a stronger diagnostic than the prose supports.**  
    **Figure:** [fig_shuffle.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_shuffle.svg), whose description says: “A method that measures movement must change its answer; one that reads appearance will not.”  
    The prose correctly allows angles to remain unchanged and acknowledges that sensitivity does not establish correctness. Shuffling also introduces discontinuities, and an appearance-based model may change because its frame selection or processing changes.  
    **Fix:** Replace the figure description and “only the motion is destroyed” caption with: “Shuffling changes temporal order while preserving the frames. Changes in timing-dependent features provide a diagnostic of temporal sensitivity.”

11. **Medium · error — The related-work contrast mischaracterizes a cited precedent.**  
    **Quoted text (§6):** “relies mainly on final-answer rewards”, with ToolRL included among the supporting citations.  
    ToolRL explicitly uses detailed rewards for tool names, parameter names and parameter values. Presenting it as support for the final-answer contrast hides a directly relevant precedent. See [ToolRL, §3.3](https://arxiv.org/html/2504.13958v1).  
    **Fix:** Replace the broad contrast with: “ToolRL studies detailed rewards for tool calls; this proposal tests rewards tied to reconstructed physical features and execution checks.”

12. **Medium · undefined-term — Essential vocabulary arrives before its explanation.**  
    **Quoted terms:** “warm start”, “harness”, “reinforcement-learning trajectories”, “Calibration slope”, “ledger rows”, “LoRA”, “GRPO”.  
    These terms carry substantive meaning that an advanced high-school reader cannot reliably infer from citations. “Ledger rows” has no defined referent even for an ML reader.  
    **Fix:** Briefly gloss the essentials: warm start = initial training on teacher demonstrations; harness = software that supplies tools and runs code; trajectory = one sequence of agent actions; calibration slope = slope of predicted scores against reference scores. Replace “ledger rows” with the actual sampling unit and cut optional algorithm names with the training logistics.

13. **Medium · concision — Repeated motivation crowds out the proposal.**  
    **Quoted text (§2):** “Two traps make accuracy figures misleading here.” The paragraph ends by restating that the proposal uses the reference in both rewards and demonstrations.  
    Both traps and both reference roles have already appeared in the abstract and research-question rationale. The depth-reconstruction aside and broad prompt/harness literature survey add further material without sharpening this comparison.  
    **Fix:** Cut that final motivation paragraph, the height/lens-parameter explanation in §2, and the prompt/harness survey in §6. Retain the concrete rise-to-toes example and a short statement connecting the closest prior work to the proposed contribution.

14. **Low · figure-text-mismatch — Teacher acceptance uses conflicting thresholds.**  
    **Quoted text (§3.3):** “stay more accurate than the expert pipeline”; **figure:** [fig_teacher.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_teacher.svg) says “at least as accurate as the expert pipeline”.  
    The figure accepts ties; the prose rejects them. These define different demonstration sets.  
    **Fix:** Choose one rule and use it consistently—for example, change the figure to “more accurate than the expert pipeline”.

15. **Low · style — Aphoristic pivots replace precise claims.**  
    **Quoted text:** “An agent that computes features with tools is designed to measure, but how it is trained decides whether it does”; “both limits are measured, not assumed away.”  
    The first sounds like a maxim and overassigns responsibility to training; the second uses a polished antithesis while leaving “measured” unspecified. Both repeat claims already expressed more concretely elsewhere.  
    **Fix:** Delete the first sentence and replace the closing clause with: “The experiments test whether these checks and teacher filters improve agreement on unseen participants.”

The combined teacher-and-reward idea is identifiable, but its mechanism claims and component conclusions exceed what the proposed checks and comparisons establish. A fixed primary endpoint, narrower interpretations and substantial cuts to logistics and repetition would make it a stronger research-proposal snapshot.