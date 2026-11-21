I reviewed the [proposal](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v2_measure-or-guess-evaluation.md) and all 22 referenced figures. No files were edited.

1. **High · error — The shrinkage example contradicts its interpretation (§2.7, Figure 18).**  
   **Text:** “while telling us almost nothing about who balances better” and “only the noisy predictor keeps the differences between people.”  
   **Why:** The shrunk predictions preserve everyone’s order perfectly: Spearman correlation is 1.0, as `figures/fig_guess.svg` correctly reports. The noisy predictor reverses two pairs and scores 0.8. Shrinkage compresses the size of differences; it does not necessarily destroy information about ordering.  
   **Fix:** Replace with: “The shrunk predictor orders everyone correctly but reduces score differences to one fifth of their reference size. The noisy predictor preserves their scale more closely but misorders two pairs.” Correct the caption and SVG description accordingly.

2. **High · error — The power calculation does not apply to the primary statistic (§7).**  
   **Text:** “the spread $\sigma$ (standard deviation) of per-participant differences between two methods” and “the smallest detectable difference is roughly $2.8\,\sigma/\sqrt{43}$.”  
   **Why:** This approximation concerns an average of participant-level differences. The primary outcome is a difference between averages of within-task correlations; no participant-level quantity whose average equals that outcome is defined. It also omits the joint requirement to pass the skill test.  
   **Fix:** Estimate power by repeatedly simulating studies with specified improvements and applying the actual rank-plus-skill decision rule. Explain this as “counting how often simulated studies detect a known improvement.”

3. **High · overclaim — Agreement and traceability do not establish measurement (§§1, 2.5).**  
   **Text:** “an evaluation protocol that separates measuring from guessing” and “Because the score comes from features through a fixed formula, every score traces back to measurements a clinician can inspect.”  
   **Why:** Ranking, error and slope describe agreement with the reference, not which information produced the predictions. A fixed formula can also turn incorrect features into a correct score: equal positive and negative feature errors can cancel when averaged.  
   **Fix:** Say: “The protocol assesses agreement with the three-camera reference and detects compressed predictions; it does not by itself establish accurate feature measurement.” For the traceability claim, explicitly require saved executable feature code and replayable tool outputs.

4. **High · logical-gap — Required reconstruction inputs are missing (§6, Figure 12).**  
   **Text:** “The agent receives the Cam0 video, the task description and StaBLE’s feature definitions with their units.”  
   **Why:** The proposed reconstruction tool assumes a stationary camera, known participant height and camera intrinsics—lens parameters that relate image positions to viewing directions. These inputs matter particularly for speeds in meters per second, yet neither the input specification nor Figure 12 includes them. [OpenCap Monocular methods](https://arxiv.org/html/2603.24733v1#S2.SS2.SSS2)  
   **Fix:** Specify how height and camera parameters are obtained, which methods receive them, and what happens when they are unavailable. Describe the input as one camera’s video plus the required measurements and recording information.

5. **High · inconsistency — The power contingency abandons the stated evaluation design (§7).**  
   **Text:** “we switch, before any test results are seen, to five-fold cross-validation over all 171 participants for the cheaper methods.”  
   **Why:** This puts the 43 reserved participants into development and gives different methods different evaluation populations. It conflicts with the primary question, shared-split promise, timeline and Figures 20 and 22. “Cheaper methods” is also unspecified.  
   **Fix:** Preserve the stated 43-person primary evaluation and report limited power if necessary. If retaining the contingency, fully specify its methods, tuning boundaries, comparisons and corresponding changes throughout the document.

6. **High · logical-gap — Constant predictions leave the primary metric undefined (§§2.7, 7).**  
   **Text:** “A constant guess gives every person the same rank, so it has no rank agreement at all.”  
   **Why:** Spearman correlation is mathematically undefined for constant predictions, rather than automatically zero. This affects the constant baseline, methods that fall back on every case of a task, and potentially bootstrap samples. The proposed averaging procedure supplies no handling rule. [SciPy’s Spearman documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html)  
   **Fix:** Report the constant baseline’s correlation as undefined, explain average ranks for partial ties, and preregister handling of constant predictions, constant references and degenerate bootstrap samples. Do not silently omit different tasks for different methods.

7. **High · inconsistency — Stage A can change the primary outcome, but the analysis never changes (§§3, 7).**  
   **Text:** “If the slope is above 0.8, rank agreement becomes a secondary outcome and the primary question reverts to error.”  
   **Why:** Section 7 defines only the rank-based primary test. Moreover, a slope above 0.8 does not establish good ordering or accuracy; substantial noise or excessive slopes can satisfy that condition.  
   **Fix:** Retain rank agreement as the stated primary outcome and treat slope as a diagnostic, or specify a complete alternative error-based question and decision rule before development begins. Explain why the switching threshold warrants that alternative.

8. **High · logical-gap — A required success criterion has no statistical definition (§3).**  
   **Text:** “The agent must also match or beat the expert pipeline.”  
   **Why:** Section 7 includes neither this comparison nor a definition of “match.” Failure to detect a difference would not establish equivalent performance, and the cost condition has no measurement rule.  
   **Fix:** Add the expert comparison to the formal success criteria, specifying the metric, acceptable performance margin, uncertainty rule and cost accounting. Explain how it joins the direct-predictor comparison in deciding whether the study succeeds.

9. **Medium · overclaim — The reused test set is described like an unopened holdout (§§2.9, 5.2–5.3).**  
   **Text:** “before the held-back data are opened” and “The 43 test participants from the lab’s pilot remain the test set.”  
   **Why:** Results on these participants already motivate the proposal. One additional evaluation after freezing new methods does not erase that prior exposure. Reuse can support benchmark comparisons, but its evidential status differs from a completely untouched test.  
   **Fix:** State: “We reuse the pilot benchmark, whose aggregate results are already known, and permit one additional evaluation after freezing this study’s methods.” Disclose what earlier test information was available and qualify claims of independent confirmation.

10. **Medium · logical-gap — Fold-specific leakage prevention is not operationalized (§5.3, Figure 22).**  
    **Text:** “recompute these endpoints from development participants only” and “any other text shown to the model come only from development folds.”  
    **Why:** During cross-validation, “development participants” includes the validation fold. Figure 22 instead promises “Learned from training people only.” The text does not explicitly distinguish those two boundaries for endpoints, prompt examples or fallback means.  
    **Fix:** Specify that each rotation derives all three from its four training folds; the fifth fold supplies evaluation only. After selection, recompute them using all 128 development participants for the final test.

11. **Medium · logical-gap — Multiple trials are never mapped to one ledger row (§5.1).**  
    **Text:** “each task has one or more trials” and “one row per participant–task slot.”  
    **Why:** The reader cannot determine which video supplies a row, whether repeated attempts are averaged, or whether the reference and prediction refer to the same attempt. Different choices can change scores and the stated case counts.  
    **Fix:** Define a trial-selection or aggregation rule before examining method errors, and record the contributing video and reference IDs in each row.

12. **Medium · logical-gap — The skill gate lacks an across-task definition (§§2.7, 7).**  
    **Text:** “Skill compares a method’s error with the constant guess’s error on the same task” and “the interval for the skill difference has a lower end above −0.02.”  
    **Why:** The first sentence defines task-specific skill; the second requires one study-wide value. Averaging task-specific ratios differs from taking the ratio of task-averaged errors. The practical meaning of the margin is unexplained.  
    **Fix:** State the aggregation formula and justify the margin. For orientation, a 0.02 skill loss on a task whose baseline error is 0.120 permits an error increase of only 0.0024.

13. **Medium · overclaim — Sequential stages cannot identify which improvement method contributes most in general (Abstract).**  
    **Text:** “which way of improving the agent (better prompts, better harness code, fine-tuning or reinforcement learning) contributes most.”  
    **Why:** Later stages inherit earlier improvements and selected training examples. Their gains depend on starting point and order, so the proposed comparisons do not isolate each method’s independent contribution.  
    **Fix:** Narrow the aim to “the additional improvement obtained at each stage of the specified development sequence.” Describe conclusions about individual methods as conditional on that sequence.

14. **Medium · inconsistency — The stage-selection branches do not connect (§3, Figure 20).**  
    **Text:** Stage D: “Carry forward if it beats stage C”; Stage E: “GRPO from the stage D model” and “Final candidate.”  
    **Why:** If D fails, its model is rejected but remains E’s required starting point. E becomes the final candidate even if it performs worse. “Beats” is also undefined for development selection.  
    **Fix:** Define the selection metric and both branches: what starts E when D fails, and which candidate is retained when E fails. Make the table and `figures/fig_stages_v2.svg` agree.

15. **Medium · error — The proposed distribution test compares overlapping samples (§5.2).**  
    **Text:** “each fold’s distribution of every task score matches the whole development set, using … the two-sample Kolmogorov–Smirnov test.”  
    **Why:** Each fold is part of the whole development set, whereas the ordinary two-sample test assumes independent samples. A nonsignificant result would also not establish matching distributions. [SciPy’s KS-test documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ks_2samp.html)  
    **Fix:** Compare each fold with its complementary training folds using descriptive plots and standardized differences. Explain how imperfect balance or sparse demographic groups will be handled instead of promising that every distribution matches.

16. **Medium · overclaim — Agent-run counts do not establish equal computational cost (§§2.6, 4, Figure 13).**  
    **Text:** “No weights change, so the method is cheap”; “matched numbers of agent runs”; `figures/fig_levers.svg`: “Cost: agent runs only.”  
    **Why:** Prompt and harness searches also invoke proposer models. Runs can have different lengths, and fine-tuning and reinforcement learning add weight-update costs. Equal run counts therefore do not establish equal budgets or low cost.  
    **Fix:** Treat cheapness as a hypothesis. Report proposer usage, agent usage, tool computation and training time separately; describe matched run counts as one controlled quantity, not total cost.

17. **Medium · inconsistency — Universal precaching conflicts with adaptive tools (§6).**  
    **Text:** “All tool outputs are computed once per video and stored, so repeated runs cost only model time.”  
    **Why:** Chosen crops, chosen tracking points, modified tool settings, plots and generated Python programs depend on the run. A single cached output per video cannot cover all those calls. Section 9 itself acknowledges sandbox computation.  
    **Fix:** Say: “We cache fixed pose, segmentation and reconstruction outputs. Parameter-dependent calls are cached by their inputs; new calls, plots and generated code incur additional computation.”

18. **Medium · error — The explanation gives supervised fine-tuning an unjustified performance ceiling (§2.6).**  
    **Text:** “SFT imitates; it cannot find a better strategy than the one in its examples.”  
    **Why:** Learning from examples does not imply an absolute ceiling on generalization or performance. The sentence turns a difference in training objectives into an impossibility claim. Research directly demonstrates substantial SFT generalization beyond training conditions. [Lin et al., 2025](https://arxiv.org/abs/2510.00237)  
    **Fix:** Replace with: “SFT trains the model to reproduce example outputs. RL instead uses rewards to favor successful generated attempts; either method’s improvement must be tested.”

19. **Medium · error — The opening definition describes static balance as if it covered movement (§2.1).**  
    **Text:** “Balance is the ability to keep the body’s weight over the feet, whether standing still or moving.”  
    **Why:** During movement, balance depends on velocity and changing support as well as position. Keeping the center of mass over the current support area is not a general requirement for dynamic balance. [Hof et al., *The condition for dynamic stability*](https://braceworks.ca/wp-content/uploads/2016/05/hof-condition-for-dynamic-stability.pdf)  
    **Fix:** Replace with: “Balance is the ability to control body position and movement without falling. Standing balance and balance during movement place different demands on that control.”

20. **Medium · figure-text-mismatch — The pilot plot announces a common denominator it does not use (Figure 8).**  
    **Figure:** `figures/fig_pilot.svg`, heading: “Task-averaged mean absolute error on 729 task scores.”  
    **Why:** The OpenCap bar reports error on 567 valid cases, according to §5.4 and the figure’s annotation. The common heading makes that selected-case error appear directly comparable with errors covering all 729 cases.  
    **Fix:** Change the heading to describe 729 eligible cases and explicitly state in the caption that OpenCap’s 0.146 uses only 567 successful cases. Label the historical bars as using different failure handling.

21. **Medium · undefined-term — Essential terminology arrives before its explanation (Abstract, §§1–2.3).**  
    **Text:** “pose, segmentation and reconstruction software,” “better harness code,” and “fine-tuned direct predictor.”  
    **Why:** These terms carry much of the opening argument but are not explained until §§2.4–2.6. A novice must interpret the research question before receiving its vocabulary.  
    **Fix:** Introduce short plain descriptions at first use: “software that locates joints, outlines the person and estimates a three-dimensional body”; “the software coordinating those tools”; “a model given additional training to output scores directly.”

22. **Medium · undefined-term — Several reproduced diagrams require substantial unexplained knowledge.**  
    **Figures:** `figures/papers/qwen3vl_fig1_architecture.png`, `lora_fig1.png`, and `deepseekmath_fig4_grpo.png`.  
    **Why:** Labels such as “Dense/MoE Decoder,” “DeepStack,” $\mathcal N(0,\sigma^2)$ and “GAE” are unexplained. The GRPO diagram also contains a learned “Reward Model,” whereas this proposal uses a fixed score-error calculation; the caption never explains that substitution.  
    **Fix:** Use simplified diagrams containing only the components needed here, or move the technical originals to an appendix. Explicitly state that this study replaces the reward-model box with its fixed error formula.

23. **Low · concision — Background and methods repeatedly explain the same machinery (§§2.5–2.9, 3, 6–7).**  
    **Text:** “Its tools are a frame viewer that returns timestamped frames or crops” begins another seven-tool inventory in §6; “Seeds and the two kinds of claim” repeats the distinction already developed in §2.9.  
    **Why:** These repetitions, plus the nearly identical stage table and Figure 20, lengthen the proposal without adding corresponding decisions.  
    **Fix:** Keep the full tool inventory in §6 and one illustrative call in the background. Keep the conceptual uncertainty explanation in §2.9 and only the actual procedure in §7. Retain either the stage table or Figure 20.

24. **Low · style — Anthropomorphic descriptions obscure the actual leakage mechanisms (§2.8).**  
    **Text:** “people it has never seen,” “recognize the person and recall their typical score,” and “has already been told something about the extremes.”  
    **Why:** These phrases describe perception and memory rather than identifying which data enter training or evaluation. The endpoint example especially benefits from a literal explanation.  
    **Fix:** Use “participants excluded from training and tuning,” “predict from person-specific appearance,” and “the rescaling endpoints contain information calculated from test participants.”

25. **Low · structure — Self-assessment does not belong in the proposal (§3).**  
    **Text:** “The question names one outcome with a definition, compares with an existing result, uses tools and data the lab already has, decides whether an inspectable analysis can compete with an opaque one, and fits in about thirteen weeks.”  
    **Why:** This evaluates the quality of the research question instead of presenting research content. It reads like commentary from a proposal-writing checklist.  
    **Fix:** Delete it; the research question, methods and timeline already supply the relevant information.

The proposal’s central shrinkage example and power calculation currently undermine its scientific argument. Its input specification, evaluation boundaries and success criteria also need to become consistent before the study can be executed as written. These repairs, together with earlier definitions and less repetition, would preserve this version’s design while making it substantially more accessible to the intended reader.