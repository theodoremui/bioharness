I reviewed the proposal and all its referenced figures without editing files.

1. **High · inconsistency — The held-out tasks lack the examples needed by the checker.**  
   **Text:** “Their videos are excluded from every training stage” (§6), but the checker requires “other development videos of the same task” (§3.2), and its probes, endpoints and fallback averages come from training folds.
   
   **Why:** The proposal does not explain where these task-specific resources come from for the three withheld tasks. Without them, the final agent cannot use the stated checking and scoring procedure.
   
   **Fix:** Specify the source and permitted use of held-task probes, endpoints and fallback averages. Distinguish tasks excluded from policy training from tasks unavailable to the checker; make the transfer claim match that distinction.

2. **High · error — The probe rule can reject a perfectly correct function.**  
   **Text:** “two near the 25th and two near the 75th percentile” and “both low probes below both high probes” (Appendix A).
   
   **Why:** Capped features can have identical lower- and upper-quartile values. Figure 2 shows substantial saturation at the five-second hold limit. If all four reference values are five seconds, correct code returns four equal answers and fails the strict-order rule.
   
   **Fix:** Require ordering only between meaningfully different reference values, allow reference-consistent ties, and state what happens when a feature lacks enough variation to test input dependence.

3. **High · overclaim — Passing other videos does not certify the current measurement or prevent reference copying.**  
   **Text:** “so it cannot copy the reference into its answer” and “which removes solutions tuned with hindsight to one video” (§3.3).
   
   **Why:** A function can recognize the current input, return a reference-derived constant there, and perform an ordinary calculation elsewhere. More generally, success on four or five other videos does not establish correctness on this video, whose reconstruction or selected time window may be wrong.
   
   **Fix:** Replace both guarantees with “reduces the risk.” Define permitted function inputs, restrict access to identifiers and reference-derived constants, test input-specific branching, and describe passing results as evidence of generality rather than certification.

4. **High · logical-gap — The source of physical scale is missing.**  
   **Text:** “The practical goal is to get the same measurements from a single phone that anyone could prop up in a clinic or at home” (§2.2). Figure 12 lists video, task description and feature definitions as inputs.
   
   **Why:** Producing meters per second requires a physical scale. The cited OpenCap Monocular method assumes known participant height, camera calibration information and a stationary camera; those inputs and assumptions are absent here. [OpenCap Monocular, §2.2.2](https://arxiv.org/html/2603.24733v1)
   
   **Fix:** Add measured height, camera information and recording requirements to the input specification and figures. Explain how they convert image distances into physical distances and what happens when they are unavailable.

5. **High · logical-gap — The experimental reward arms are not fully defined.**  
   **Text:** “GRPO with a final-score reward” (§4); “the same reward without the check” (S1); Appendix A supplies only the checked reward formula.
   
   **Why:** It is unclear whether the score-only arm receives scores calculated from raw or fallback-replaced features, whether it also pays verification and timing penalties, and whether checking remains active during evaluation. These choices change what the central comparison isolates.
   
   **Fix:** Add a compact table defining all three arms: reward formula, fallback handling, verification penalty, timing penalty, invalid-submission handling, and evaluation procedure.

6. **High · logical-gap — S4 compares methods with different outputs without defining a shared outcome.**  
   **Text:** “Final agent against the direct predictor on time-scaling interventions” (§4), followed by expected changes in durations, speeds and angles (§8).
   
   **Why:** The direct predictor returns a task score, not those individual features. The proposed feature-response test therefore cannot be applied to both methods as written.
   
   **Fix:** Define a shared score-response measure by transforming the reference features and recomputing the expected task score. Report feature-response errors separately for methods that produce features.

7. **High · logical-gap — The confirmatory decision rules remain incomplete.**  
   **Text:** “the skill difference is not worse than −0.02” (§8); “age-adjusted rank agreement becomes co-primary” (§7); “Holm-corrected as one family of five” (§4).
   
   **Why:** The skill condition does not say whether it applies to a point estimate or an interval bound. “Ranks people as well” has no threshold, age adjustment has no specified calculation, and the secondary comparisons lack explicit test statistics and p-value procedures.
   
   **Fix:** Predefine each comparison’s outcome, direction, uncertainty rule and success threshold. Specify the age-adjustment calculation and how introducing a second primary outcome changes the overall success rule.

8. **Medium · figure-text-mismatch — The slowdown prediction mishandles capped durations.**  
   **Text:** “durations should grow by a quarter” (§8). [fig_timescale.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_timescale.svg) adds an exception only for holds already at five seconds.
   
   **Why:** Holds that cross the cap also fail the stated ×1.25 rule: a 4.5-second hold becomes five scored seconds, not 5.625. The prose omits even the figure’s partial exception.
   
   **Fix:** State and illustrate: “The scored hold becomes `min(5 seconds, original hold / 0.8)`.” List the transformation rules for every feature included in this test.

9. **Medium · inconsistency — The training budget does not reconcile with five-fold cross-validation.**  
   **Text:** “each candidate is trained on four folds and checked on the fifth, and the roles rotate” (§2.11), versus “nine RL runs (three rewards, three seeds each)” (§9).
   
   **Why:** Applying the stated rotation to those three rewards and three seeds requires 45 RL fits before any final refitting. Nine runs cover only one split.
   
   **Fix:** State which candidates undergo all five rotations, how the final models are fitted, and how many fits the compute estimate includes. Recalculate the budget accordingly.

10. **Medium · logical-gap — Training-only rescaling no longer guarantees scores between zero and one.**  
    **Text:** “a task score between 0 and 1” (§2.1); “Within the training range widened by half its width on each side” (Appendix A).
    
    **Why:** With training-only endpoints, an accepted value can rescale to −0.5 or 1.5; new reference values can also exceed the training range. No clipping or extrapolation policy is specified. An empirical range also does not establish physical possibility.
    
    **Fix:** Specify whether scoring clips values or permits scores outside the original range, and distinguish score calculations from uncapped feature-error calculations. Rename the range check a plausibility screen.

11. **Medium · error — The shrinkage example confuses ordering with the size of differences.**  
    **Text:** The shrunk predictor tells us “almost nothing about who balances better” (§2.7); Figure 18 says “only the noisy predictor keeps the differences between people.”
    
    **Why:** The shrunk predictor orders every person correctly: its rank agreement is 1, as [fig_guess.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_guess.svg) explicitly shows. The noisy predictor misorders two pairs and has rank agreement 0.8.
    
    **Fix:** Replace with: “The shrunk predictor preserves the ordering perfectly but understates every score difference by a factor of five; the noisy predictor better preserves the scale of differences.”

12. **Medium · logical-gap — Predicted tool error does not automatically provide score uncertainty.**  
    **Text:** “its predicted errors, once calibrated, give an uncertainty range for each score” (§3.4). [fig_worldmodel.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_worldmodel.svg) trains on errors from the expert pipeline’s feature code.
    
    **Why:** Those labels describe the expert’s computations, whereas the agent can write different code and choose different windows. A predicted average error also does not specify interval width or the proportion of true values an interval should contain.
    
    **Fix:** Limit the initial claim to predicting expert-route performance. Define and separately validate any interval procedure on the complete agent’s outputs, stating its intended coverage.

13. **Medium · logical-gap — The power calculation does not describe how the proposed effect and seed variation are generated.**  
    **Text:** “Power is estimated before training by resampling development predictions of existing methods and applying this rule” (§8).
    
    **Why:** Resampling existing predictions estimates behavior under their observed differences; it does not by itself simulate the proposed 0.05 rank-agreement gain or variability across future training runs. Repeatedly resampling three seeds also supplies little information about rare training outcomes.
    
    **Fix:** Specify how simulated method differences and seed variation enter the power calculation. Report sensitivity to those assumptions and describe intervals based on three seeds as approximate.

14. **Medium · inconsistency — “Before any analysis” contradicts the acknowledged prior use.**  
    **Text:** “60 are set aside before any analysis,” followed by “the pilot trained models on some of the sealed participants” (§6). [fig_split_v5.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_split_v5.svg) repeats the stronger wording.
    
    **Why:** The later caveat is valuable, but the earlier sentence and figures present the sample as previously untouched. Retraining excludes those people from new fits; it does not erase their role in earlier development.
    
    **Fix:** Use “reserved before this study’s further model development” consistently. Retain the disclosure of prior use and the distinction between retrospective evaluation and future independent confirmation.

15. **Medium · undefined-term — The worked calculation skips the essential arithmetic.**  
    **Text:** “takes the rate of change of the vertical center-of-mass position over time and returns its maximum between `ann.start` and `ann.end`” (§3.5).
    
    **Why:** “Rate of change,” the function arguments and the relationship between annotations and code are not explained. This is the central measurement step, yet a reader without programming or calculus knowledge cannot reproduce it.
    
    **Fix:** Add: “If height increases by 0.01 meters over 0.1 seconds, upward speed is 0.01 ÷ 0.1 = 0.1 meters per second. The function repeats this calculation within the marked interval and returns the largest speed.” Define `out` and `ann` in ordinary language.

16. **Medium · overclaim — A negative comparison would not establish continued measurement.**  
    **Text:** If checked rewards do no better, “it would suggest that for this kind of task outcome rewards did not lead the agent to stop measuring” (§10).
    
    **Why:** Both methods could exploit shortcuts, both could fail to learn, or the experiment could miss a real difference. Similar performance does not identify either method’s mechanism.
    
    **Fix:** Replace with: “A null result would show no detected benefit of checked rewards at the study’s precision; the behavioral tests would separately assess evidence of movement dependence.”

17. **Medium · overclaim — Frame-order insensitivity is presented as absence of video use.**  
    **Text:** “a sign that the models had stopped using the video” (§2.8); “A video-language model stops watching” (Figure 19).
    
    **Why:** A model can use individual frames while ignoring their order. The cited diagnostic specifically uses questions about temporal order or progression; that qualification is missing. [Xu, Appendix A.3](https://arxiv.org/html/2606.22043v1)
    
    **Fix:** Write: “On questions requiring temporal order, answers became less sensitive to frame shuffling, suggesting reduced use of temporal information.” Replace the anthropomorphic figure title accordingly.

18. **Medium · error — SFT is given an unjustified performance ceiling.**  
    **Text:** “SFT imitates; it cannot find a better strategy than the one in its examples” (§2.6).
    
    **Why:** An imitation objective does not impose that absolute limit: learned models can generalize beyond individual demonstrations. Teacher–student learning can even produce students that outperform their teachers. [Furlanello et al., 2018](https://proceedings.mlr.press/v80/furlanello18a.html)
    
    **Fix:** Replace with: “SFT trains the model to reproduce demonstrations; unlike RL, its training objective does not directly reward improvements found through new attempts.”

19. **Medium · inconsistency — Repeated sampling is promised but never specified.**  
    **Text:** “equally budgeted repeated sampling … so both appear here as budget-matched baselines” (§5).
    
    **Why:** The research plan and comparison table do not define a repeated-sampling baseline: its attempt count, answer-selection rule and cost accounting are missing. Selection is especially important because choosing the best attempt using test reference values would be unfair.
    
    **Fix:** Add an explicit baseline with a fixed sampling budget and a selection rule that uses only information available at deployment.

20. **Medium · undefined-term — The abstract and opening require concepts defined much later.**  
    **Text:** “a vision-language model,” “pose, segmentation and 3D reconstruction tools,” and “a teacher” (Abstract).
    
    **Why:** The reader encounters an entire technical architecture before learning what a model, pose tool or teacher demonstration is. The introductory summary repeats the same burden.
    
    **Fix:** Begin with plain descriptions: “We train a program that reads video and writes instructions for tools that locate body joints and estimate movement.” Introduce technical names alongside those descriptions rather than relying on later sections.

21. **Medium · undefined-term — Several operational terms remain unexplained.**  
    **Text:** “the regressor applies gradient-boosted trees” (§4), “features were imputed from age” (§6), “H100-hours” (§9), and “25th … percentile” (Appendix A).
    
    **Why:** These terms determine the comparison method, excluded data, feasibility and checker behavior. None can be assumed for the intended reader.
    
    **Fix:** Explain a regressor as a number-predicting model; describe boosted trees as successive rule-based predictors correcting earlier errors; replace “imputed” with “filled in using predictions from age”; define an H100-hour as one H100 graphics processor running for one hour; explain percentile cutoffs.

22. **Medium · undefined-term — Several reproduced figures require specialist knowledge their captions do not supply.**  
    **Figures:** `figures/papers/qwen3vl_fig1_architecture.png`, `figures/papers/deepseekmath_fig4_grpo.png`, and `figures/papers/pi_distill_fig1.png`.
    
    **Why:** These contain unexplained “Dense/MoE Decoder,” “DeepStack,” “GAE,” and expressions such as `πθ(o | s, I)`. Figure 17 also depicts a reward model, whereas this proposal uses a fixed reward calculation, inviting confusion.
    
    **Fix:** Move specialist architecture diagrams to an appendix or replace them with simpler attributed schematics. Keep only the components needed for this study, explain every retained label, and distinguish borrowed architectures from the proposed implementation.

23. **Low · concision — The central pitch is repeated while supporting machinery receives disproportionate space.**  
    **Text:** “Four design choices follow from it” (§1), followed by “Four design choices respond to these weaknesses” (§3), after the abstract has already listed them.
    
    **Why:** The abstract, introduction, approach opening, pipeline figure and worked trajectory repeatedly summarize the same mechanism. Meanwhile, the LoRA matrix-size calculation and PPO comparison delay the experiment without being necessary to understand its question.
    
    **Fix:** Keep one short introduction overview and let §3 provide the operational details. Move matrix arithmetic and the PPO comparison to an appendix; retain the concrete measurement example and essential statistical explanations.

24. **Low · structure — The SMART self-assessment is proposal meta-commentary.**  
    **Text:** “The question is specific … measurable … achievable … relevant … and time-bound” (§4).
    
    **Why:** This evaluates the document against a planning rubric rather than stating scientific content. The conference deadline inside the primary question similarly mixes publication logistics with the hypothesis.
    
    **Fix:** Delete the SMART paragraph. State the scientific question directly and keep timing information in the feasibility schedule.

25. **Low · style — The opening turns the hypothesis into a slogan.**  
    **Text:** “To train it, we follow one rule.” / “**Thesis: reward the measurements, and only those that can be checked.**” (§1).
    
    **Why:** The short setup and bold maxim add rhetorical emphasis while obscuring that checking is itself an imperfect method under investigation. They also repeat the title and surrounding summary.
    
    **Fix:** Replace both with: “We test whether rewarding individual feature estimates after checking their submitted calculations improves movement measurement.”

The proposal has a testable central idea, but unresolved checker behavior, transfer requirements and comparison rules currently weaken its conclusions. Its explanations often help beginners, yet specialist figures and repeated summaries make it longer and harder to follow than necessary. These problems can be repaired while preserving this version’s scientific design.