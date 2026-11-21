1. **High · error — The reward signs reverse the intended incentives (§3.2).**  
   **Quote:** “plus 0.5 for each feature that fails the check, plus 0.1 times the timing error”  
   **Problem:** Maximizing this reward encourages failed checks and inaccurate timing. “Capped at 3” also leaves unclear whether the cap applies to timing error, total error, or reward.  
   **Fix:** Write the expression explicitly: `R = −min(3, E + 0.5F + 0.1T)`, where `E` is mean absolute rescaled feature error, `F` counts failed features, and `T` is timing error in seconds; malformed submissions receive −4.

2. **High · research-question — The headline question omits a treatment difference (§§1, 3.2).**  
   **Quote:** “the primary comparison tests per-feature rewards, the check and timing supervision together”  
   **Problem:** The headline names feature rewards and checks, but timing supervision also changes. A positive result could therefore come from better boundary annotations rather than the proposed measurement incentives. Acknowledging the bundle later does not make the headline accurate.  
   **Fix:** Hold timing supervision constant between the primary arms. Shorten the question to: “With initialization, training data, tools and timing supervision fixed, does rewarding feature accuracy and penalizing failed checks improve within-task rank agreement with three-camera scores on unseen people, compared with rewarding final-score accuracy?”

3. **High · research-question — The cancellation mechanism does not yet predict the primary outcome (§1; Figure 1).**  
   **Quote:** “Scoring every feature against the reference removes cancellation.”  
   **Problem:** This explains why feature errors cannot cancel *inside the reward*, but not why participant rankings should improve. Figure 1 actually prefers a submission with a worse final score; it contains no comparison of rankings across people.  
   **Fix:** Add the missing generalization hypothesis: “We hypothesize that feature errors that cancel during training will fail to cancel on unseen participants. Penalizing those errors and rejecting shortcut computations should therefore reduce participant-specific score errors and improve held-out rankings.” Present this as the prediction being tested.

4. **High · figure-text-mismatch — The pipeline depicts a different evaluation and an unexplained training arm.**  
   **Figure:** [pipeline_v7.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/pipeline_v7.svg), labels “failures → task mean” and “− λ · tool cost (cost-aware arm)”.  
   **Problem:** The check flows into a scoring box that substitutes means, whereas §3.2 says primary evaluation uses submitted features and substitution occurs only in a secondary score. The cost-aware arm appears nowhere in the reward specification or comparison table.  
   **Fix:** Show submitted-feature scoring as the primary path and label replacement scoring explicitly as secondary. Distinguish malformed submissions from failed checks, and remove the unintroduced cost-aware arm.

5. **Medium · research-question — The outcome definition leaves consequential choices unresolved (§1).**  
   **Quotes:** “averaged over tasks”; “one minus a method's error divided by the error of predicting the task average”  
   **Problem:** The primary average could cover trained task types, held-out task types, or both. “Skill” does not specify whether it averages task-level error ratios or divides task-averaged errors; these differ. Constant predictions—the motivating failure mode—also make Spearman correlation undefined.  
   **Fix:** Identify the primary task set, reserve transfer tasks for the subordinate comparison, and define the skill calculation explicitly using MAE and training-derived task averages. State a common treatment of constant or invalid predictions rather than silently excluding them.

6. **Medium · structure — Substantial logistics remain throughout the snapshot.**  
   **Quotes:** “seven pairs of runs”; “60 are sealed”; “111 form five development folds”; “100 sealed videos”; “seven paired seeds for reinforcement learning and five for fine-tuning”; “compared at matched compute”.  
   **Problem:** These are sample allocation, repetition planning and compute-matching details explicitly excluded by the requested format. The inference paragraph and pipeline’s “8 rollouts per video” reinforce the protocol-document character.  
   **Fix:** Remove these allocations and the interval-calibration simulation. Retain the scientific controls, participant-level separation and a sentence such as: “Uncertainty will account for both retraining variability and differences among participants.”

7. **Medium · research-question — The abstract and secondary program compete with the primary question.**  
   **Quote:** “the study asks whether this supervision teaches an agent to measure movement and whether that skill carries over to unfamiliar tasks”  
   **Problem:** This replaces the specified ranking comparison with two broader questions. Teacher quality, tool-route prediction, agent superiority and task transfer then receive their own objectives, making the snapshot resemble a research program.  
   **Fix:** End the abstract with the primary reward comparison and its rank-agreement outcome. Describe check removal and movement interventions as tests of the proposed mechanism; compress teacher and transfer comparisons into clearly subordinate diagnostics, with shared infrastructure described once.

8. **Medium · error — The score description omits feature direction (§2).**  
   **Quote:** “Each feature is rescaled to the range 0 to 1 using the lowest and highest values in the data”  
   **Problem:** Some features improve when they decrease, such as sway. StaBLE’s implementation reverses those features before averaging; the current explanation can imply that larger values always improve the score. [Released scoring code](https://github.com/stanfordnmbl/stable-analysis/blob/main/compute_scores.ipynb)  
   **Fix:** “Features are rescaled so that 1 always represents better performance, reversing quantities where lower values are better.” Then distinguish the published dataset-wide normalization from this study’s training-derived endpoints and designated task-calibration values.

9. **Medium · clarity — The running example loses the feature definitions that the check is supposed to enforce (§2).**  
   **Quote:** “the peak ankle angle, and the hold time, which stops counting at five seconds”  
   **Problem:** “Ankle angle” does not identify the direction of rotation, and “hold time” does not explain what counts as holding. StaBLE specifies peak plantar flexion and a center-of-mass height threshold. These distinctions matter when checking code and predicting intervention responses. [StaBLE paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC13621976/)  
   **Fix:** Use “the greatest downward pointing of the foot (peak plantar flexion), and time above half the peak center-of-mass rise, capped at five seconds.”

10. **Medium · figure-text-mismatch — The range check has two different acceptance rules (§3.1; Figure 5).**  
    **Quote:** “the value lies within the training range and physical limits”  
    **Figure:** [fig_check_v7.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_check_v7.svg) says “the training range widened by half its width on each side”.  
    **Problem:** These rules penalize different submissions. A strict training-range rule also rejects physically valid measurements from unseen people who exceed the observed extremes.  
    **Fix:** Specify one rule consistently. Prefer physical impossibility as a hard failure and an empirical-range excursion as a warning; if the widened range remains a rejection rule, state that choice and its limitation in both places.

11. **Medium · inconsistency — S2 is credited with measuring something it does not isolate (§3.3).**  
    **Quote:** “choices that quietly depend on the panel can remain, which is what S2 measures”  
    **Problem:** S2 compares student performance after privileged versus plain demonstrations. That measures the net effect of teacher access, not whether particular teacher choices depended on information unavailable to the student.  
    **Fix:** “S2 tests whether privileged demonstrations improve the student's starting performance; dependence of individual teacher decisions on hidden information remains unresolved.”

12. **Medium · overclaim — A positive result is generalized to an unrestricted class of domains (§5).**  
    **Quote:** “rewarding checked measurements is a practical recipe wherever a better instrument exists only during training”  
    **Problem:** One retrospective balance dataset cannot establish effectiveness wherever privileged instruments exist. The proposal also requires meaningful intermediate quantities, executable computations and useful checks—conditions beyond having a better instrument.  
    **Fix:** “A positive result would support checked feature rewards for single-camera balance estimation and motivate tests in other domains with reliable intermediate references and meaningful computation checks.” Narrow the corresponding abstract claim too.

13. **Medium · concision — Peripheral surveys and repeated explanations dilute the reward idea (§§1–6).**  
    **Quotes:** “Privileged-information distillation”; “language world models”; “Prompt and harness optimization”; “Passing the check is evidence, not proof”  
    **Problem:** The related-work paragraph surveys three additional research directions after establishing the relevant reward distinction. The limitations of checking and the training-only reference setup are also explained repeatedly.  
    **Fix:** Cut the teacher/world-model and prompt/harness surveys from §6, retaining the cited contrast with existing reward designs. Keep the check’s limitation once, and remove repeated explanations of the privileged instrument from the motivation and conclusion.

14. **Medium · undefined-term — Essential vocabulary arrives without short glosses.**  
    **Quotes:** “reinforcement learning”, “fine-tuned”, “trajectories”, “harness”, “segmentation”; Figure 4’s “SFT” and “GRPO”.  
    **Problem:** These terms appear in the question or central explanation before an advanced high-school reader has enough context to interpret them. Defining the vision-language model does not resolve the training and tool vocabulary.  
    **Fix:** Briefly gloss reinforcement learning as “training through rewards,” fine-tuning as “further training a pretrained model,” trajectories as “sequences of tool calls and outputs,” harness as “software that exposes and runs the tools,” and segmentation as “identifying the person's pixels.” Replace the figure’s algorithm acronyms with “demonstration training” and “reward-based training.”

15. **Low · style — An aphoristic contrast substitutes for a precise claim (§2).**  
    **Quote:** “An agent that computes features with tools is built to measure, but its training decides whether it does.”  
    **Problem:** “Built to measure” assigns purpose without establishing behavior, while the polished contrast repeats the surrounding argument.  
    **Fix:** “Tool access alone does not ensure that predictions depend on measured movement.”

The proposal identifies a testable reward-design question, but its current specification contains a reversed incentive, an incompletely stated treatment comparison and contradictory scoring paths. Correcting those points and removing the protocol logistics and peripheral objectives would make the central scientific prediction much easier to assess.