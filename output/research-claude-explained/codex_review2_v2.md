1. **High · research-question — The mechanism does not predict the primary outcome.**  
   **Text:** “Features computed from measured movement should preserve the differences between people—visible as better ordering and a calibration slope closer to 1.”  
   **Problem:** Shrinking predictions toward a constant preserves their ordering unless ties arise. [fig_guess.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_guess.svg) demonstrates this: the shrunk predictor has rank agreement 1.0, versus 0.8 for the “measuring” predictor. A low slope also cannot establish that shrinkage caused an error advantage.  
   **Fix:** Replace with: “Tools may improve ordering by reducing errors in identifying movement phases and extracting task features. Prediction slope separately describes compression of differences between people.”

2. **High · research-question — The primary measure changes in response to results.**  
   **Text:** “A slope above 0.8, in which case error replaces rank agreement as the primary measure.”  
   **Problem:** This changes the scientific question after inspecting development results. The abstract, highlighted question and decision rule nevertheless continue to promise a ranking comparison. It also leaves the interpretation of slopes between 0.5 and 0.8 unspecified.  
   **Fix:** Keep rank agreement primary throughout. Replace the cell with: “A slope near 1 weakens the compression hypothesis; rank agreement remains the primary outcome.”

3. **High · error — Beating the mean does not establish useful video information.**  
   **Text:** “predicting each task's average score for everyone”; “so 0 means no better than ignoring the video.”  
   **Problem:** The median minimizes absolute error among constant predictions; the mean need not. A video-independent median predictor can therefore earn positive skill against the mean baseline. For example, on scores 0, 0, 1, it earns skill 0.25 without distinguishing anyone. [Scikit-learn’s scoring guidance](https://scikit-learn.org/stable/modules/model_evaluation.html#which-scoring-function-should-i-use) explains the median–absolute-error correspondence.  
   **Fix:** Retain the mean for the historical pilot comparison, add a training-task-median baseline, and use that baseline for the proposed absolute-error skill measure.

4. **Medium · research-question — The information held fixed is incomplete.**  
   **Text:** “Each method receives one smartphone video per task.” Figure 4 additionally supplies “Height and lens parameters (passed to the tools).”  
   **Problem:** The proposal does not establish whether the direct predictor receives the same side information and task definitions. Height and camera parameters materially constrain reconstruction, as the [OpenCap Monocular methods](https://arxiv.org/html/2603.24733v1) explain. An advantage could therefore reflect additional information as well as tool use.  
   **Fix:** State explicitly that both primary arms use the same Qwen3-VL-8B starting checkpoint, Cam0 videos, permitted metadata, training participants and score targets.

5. **Medium · inconsistency — The decision rule permits the accuracy loss that the question excludes.**  
   **Text:** “without becoming less accurate relative to a constant guess”; “the lower end of the interval for the skill difference is above −0.02.”  
   **Problem:** The rule allows a loss approaching two percentage points of task-averaged skill. The question promises no loss, and no rationale establishes why this tolerance is acceptable.  
   **Fix:** Change the question to “while retaining error-based skill within a prespecified tolerance,” and briefly justify the chosen tolerance in those units.

6. **Medium · inconsistency — Changing normalization undermines the claimed pilot comparability.**  
   **Text:** “The pilot's 43 test participants remain the test set, so results can be compared with Figure 3”; “rescaling endpoints…are recomputed from training people.”  
   **Problem:** Changing feature ranges changes their relative weights in the averaged task score, potentially changing reference rankings as well as errors. Identical participants do not ensure an identical evaluation. Training-only extrema also need not bound held-out values within 0–1.  
   **Fix:** Specify that predictions and reference features use the same training-only endpoints and one stated out-of-range policy. Recompute comparison results under that rule, or label Figure 3 a historical illustration rather than a directly comparable benchmark.

7. **Medium · overclaim — The expert-pipeline interpretation exceeds the comparison.**  
   **Text:** “If the agent orders people better and the expert pipeline does not match it, learning to conduct the analysis adds something that careful manual engineering does not.”  
   **Problem:** Failure to establish a match can reflect uncertainty; a claim of superiority needs a direct superiority result. One hand-written pipeline also cannot establish the limits of careful manual engineering generally.  
   **Fix:** Replace with: “If the interval for agent-minus-expert rank agreement lies above zero, the agent outperforms this particular fixed pipeline.”

8. **Medium · research-question — Several subordinate hypotheses lack their claimed outcome measures.**  
   **Text:** “Fine-tuning on successful agent runs improves tool choice”; “Reinforcement learning toward the reference score improves further.”  
   **Problem:** The proposed measures assess scores, not tool-choice quality. “Improves further” leaves the outcome unspecified, while the table starts to resemble a second research agenda about optimization methods.  
   **Fix:** Label C–E exploratory training stages. Replace D with “Fine-tuning raises within-task rank agreement over C,” and E with the corresponding comparison against D; retain the shared accuracy constraint.

9. **Medium · overclaim — The motivation announces benefits that remain untested.**  
   **Text:** “An agent that measures with tools, evaluated by measures that a guess cannot satisfy, addresses both problems at once.”  
   **Problem:** Tool use does not establish correct feature measurement or successful recovery from reconstruction failures. The later limitations correctly acknowledge that score agreement cannot verify features, making this earlier assurance inconsistent in strength.  
   **Fix:** Replace with: “We test whether tool use improves within-task ordering and reduces failed analyses. Agreement with reference scores alone does not establish correct feature measurement.”

10. **Medium · structure — Cost considerations introduce an unwanted additional question.**  
    **Text:** “at low cost”; “If the expert pipeline is as good and cheaper”; “If the expert pipeline matches it at lower cost.”  
    **Problem:** These clauses introduce economic or feasibility criteria into the research question and interpretation, contrary to the requested scope. Cost is also undefined and absent from the measures.  
    **Fix:** Delete these cost clauses. Keep the expert pipeline as a scientific control for whether adaptive tool use adds predictive value.

11. **Medium · concision — The snapshot carries a methods inventory and repeated motivation.**  
    **Text:** “The improvement steps behind hypotheses C to E…”; “## 6. Related work”; “If hypothesis A holds, the pilot's ranking of methods partly reflects shrinkage…”  
    **Problem:** The optimization catalogue repeats the hypothesis table, related work surveys several research families, and the opening of expected outcomes repeats the rationale. The 23-entry bibliography and implementation details make the document read like a compressed full proposal.  
    **Fix:** Reduce the optimization paragraph to one sentence describing the stages, related work to two sentences establishing the nearest comparisons, and remove references used only by the deleted catalogue. Cut the repeated shrinkage conclusion and the exact bootstrap-resample and seed counts; retain the participant-level uncertainty principle.

12. **Medium · undefined-term — Essential tool and training terminology lacks short glosses.**  
    **Text:** “RTMPose 2D pose”; “SAM 2 segmentation”; “Python sandbox”; “LoRA adapters”; “GRPO”; “the untrained agent.”  
    **Problem:** These require background beyond an advanced high-school reader. “Untrained” also misleadingly suggests that Qwen has never been trained.  
    **Fix:** Use “joint locations in each frame,” “outlining the person,” and “an isolated Python code runner.” Either remove LoRA and GRPO or gloss them as training small additional weight matrices and learning from comparisons among rewarded runs. Replace “untrained” with “without task-specific training.”

13. **Medium · figure-text-mismatch — The running example loses the direction of the ankle measurement.**  
    **Text:** “the peak ankle angle.”  
    **Figure:** [stable_fig2a_features.png](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/papers/stable_fig2a_features.png) specifies “peak plantar flexion.”  
    **Problem:** “Ankle angle” does not identify the movement direction; depending on the coordinate convention, its maximum could represent the opposite motion.  
    **Fix:** Replace with “peak plantar-flexion angle—how far the foot points downward at the ankle.”

14. **Low · inconsistency — The prose skips the reduction from 180 to 171 participants.**  
    **Text:** “recorded 180 adults”; “The other 128 participants form five development folds.”  
    **Problem:** After reserving 43 of 180 people, “the other” would mean 137. [fig_split_v2.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_split_v2.svg) supplies the missing explanation: only 171 have usable single-camera video.  
    **Fix:** Write: “Of the 180 recorded participants, 171 have usable single-camera video; 43 form the test set and 128 the development set.”

15. **Low · style — Checklist fragments and personification weaken the scientific voice.**  
    **Text:** “Five routes are closed. People never appear on both sides of a split”; “the methods that could explain their numbers.”  
    **Problem:** The leakage paragraph becomes a staccato checklist, and methods are attributed an explanatory ability that actually belongs to their inspectable outputs. “Closed” also sounds stronger than the acknowledged reused-benchmark setting warrants.  
    **Fix:** Combine the leakage statements: “Participant splits separate training from evaluation, and fitted quantities and prompt examples use training participants only.” Replace the personification with “pipelines with inspectable intermediate outputs.”

The evaluation-centered idea is clear, but its shrinkage argument and changing decision rules do not yet support a clean answer to the main question. Preserve this design while fixing the baseline and controls, keeping one primary measure, and cutting the cost discussion and implementation inventory.