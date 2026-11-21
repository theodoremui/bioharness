1. **High — research-question. The comparison does not specify what is held fixed.**  
   **Text:** “more accurately than the same model fine-tuned to output scores directly”; “All pilot methods in Figure 2, and the agent after each improvement step.”  
   **Problem:** “Same model” establishes architecture, but not equivalent inputs, development data or supervision. The agent receives height, camera parameters and feature-level supervision; the comparator’s access is unspecified. Which agent stage supplies the primary result is also unclear.  
   **Fix:** Identify the primary agent checkpoint and explicitly hold the starting model, participant splits, video inputs and available metadata fixed. State any supervision differences and describe the result as a comparison of complete systems if those differences remain.

2. **High — error. The primary error measure is undefined when a case fails.**  
   **Text:** “the task-averaged mean absolute error over all 729 cases, with the number of failures reported beside it; if any case fails, the error over the valid cases is also reported”.  
   **Problem:** A missing prediction has no absolute error. Reporting a failure count does not make an all-case MAE computable, and “also” incorrectly implies that both errors exist.  
   **Fix:** Replace with: “Success requires a complete score for every eligible case and lower task-averaged MAE. If any case fails, the success criterion is unmet; report coverage and valid-case MAE descriptively.”

3. **High — research-question. The recovery mechanism does not support the full prediction.**  
   **Text:** “Handing the geometry to established tools should remove the first failure”; “a failed 3D reconstruction can be replaced by 2D pose or point tracking for timing features.”  
   **Problem:** Tools can still produce inaccurate geometry. More importantly, recovering timing does not recover every required physical feature, and the reported Y-Balance failure concerns event detection on an existing reconstruction—not necessarily reconstruction failure. The rationale therefore overextends a plausible timing repair into complete scoring and superiority over the trained comparator.  
   **Fix:** Write: “We predict that 2D tracking can recover missed task windows when usable 3D trajectories exist, reducing segmentation-related errors and failures. Recovering geometry-dependent features when reconstruction fails remains uncertain.”

4. **Medium — inconsistency. The reference is presented as measured movement, but apparently includes substituted values.**  
   **Text:** “task scores computed from a three-camera reconstruction of the same movement”; later, “excluding reference values that StaBLE filled in from age, set to zero or flagged for reconstruction error”.  
   **Problem:** The exclusion applies only to secondary feature error. Readers cannot tell whether the primary score comparison includes imputed or unreliable targets, or how many test cases are affected. StaBLE’s published code explicitly includes age-based substitutions. [StaBLE scoring code](https://github.com/stanfordnmbl/stable-analysis/blob/main/compute_scores.ipynb)  
   **Fix:** Define the primary target as the published StaBLE benchmark score, disclose which substitutions enter the evaluation, and report a subordinate comparison restricted to scores with usable measured references.

5. **Medium — clarity. The normalization constants are not specified for the proposed comparison.**  
   **Text:** “using the lowest and highest values in the data”.  
   **Problem:** “The data” could mean the original cohort, development participants or each evaluation group. These choices change the outcome scale and whether Figure 2 remains directly comparable. The published implementation computes extrema across the loaded cohort. [StaBLE scoring code](https://github.com/stanfordnmbl/stable-analysis/blob/main/compute_scores.ipynb)  
   **Fix:** For the stated benchmark comparison, specify: “All methods and reference scores use the same frozen, published StaBLE normalization constants, originally estimated from the full cohort.”

6. **Medium — overclaim. Formatting requirements do not establish measurement provenance.**  
   **Text:** “valid score, meaning that all of the task's features are submitted in the expected units”; [fig_routes.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_routes.svg): “every number traces to a measurement”.  
   **Problem:** Correct units and accompanying code do not establish that executing that code on the recorded tool outputs reproduces the submitted values. The figure asserts a stronger guarantee than the validity definition provides.  
   **Fix:** Require finite feature values reproducible by executing the submitted code on logged tool outputs. Describe this as computational traceability; retain feature error as the separate assessment of measurement accuracy.

7. **Medium — error. The failure penalty is not guaranteed to be worse than a completed prediction.**  
   **Text:** “The reward is minus the absolute score error, and −1 for a run without a valid score.”  
   **Problem:** Min–max scaling does not automatically constrain predictions outside the reference feature range. Without an explicit rule, a completed prediction can receive reward below −1, making failure preferable; even bounded error can tie the failure penalty.  
   **Fix:** Specify out-of-range handling. For example, constrain evaluated scores to [0,1] and assign −2 to invalid runs, while retaining unclipped feature errors for diagnosis.

8. **Medium — structure. Compute logistics remain throughout the snapshot.**  
   **Text:** “at what extra compute?”; “within a fixed limit on tool calls and running time”; “Each step receives the same number of agent runs”; “compute per video”. [fig_levers.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_levers.svg) also contains four “Cost:” callouts.  
   **Problem:** These introduce a resource-allocation and efficiency study despite the requested exclusion of compute budgets and logistics.  
   **Fix:** Remove these clauses and callouts from the snapshot, along with “minutes of GPU time per clip” in Figure 3. Keep execution-budget details in a separate experimental protocol, without adding an appendix here.

9. **Medium — concision. The improvement sequence receives duplicate tutorial treatment.**  
   **Text:** “The agent is improved in four steps, each starting from the best agent so far”; Figure 5’s repeated explanations of those same four steps; “## 6. Related work”.  
   **Problem:** Section 3.2 and Figure 5 teach the same optimization mechanisms twice, while related work revisits several of them again. This gives the training machinery disproportionate prominence relative to the research question.  
   **Fix:** Preserve the four-step design, but explain it once: retain either the substantive figure descriptions or the numbered explanations. Reduce related work to the closest movement-assessment comparison and the evidence motivating tool-assisted measurement; remove the repeated optimization survey.

10. **Medium — overclaim. The proposed interpretation does not follow from the stated result.**  
    **Text:** “If it wins only on tasks where OpenCap Monocular works, its accuracy is bounded by the reconstruction it calls”.  
    **Problem:** That pattern would establish an association, not an accuracy bound. Task difficulty, training coverage or tool-selection errors could produce the same pattern.  
    **Fix:** Replace with: “If gains occur only where OpenCap Monocular succeeds, they may depend on reconstruction quality; compare reconstruction and feature errors within those tasks.”

11. **Medium — figure-text-mismatch. The running example leaves the ankle feature ambiguous.**  
    **Text:** “the peak ankle angle”; [stable_fig2a_features.png](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/papers/stable_fig2a_features.png) specifies “peak plantar flexion (deg)”.  
    **Problem:** “Ankle angle” does not identify the movement direction or sign convention. Taking a maximum under a different convention could select the opposite motion.  
    **Fix:** Use “peak ankle plantar-flexion angle—the angle associated with pointing the foot downward—in degrees, using StaBLE’s sign convention.”

12. **Medium — undefined-term. Several central operations need short glosses.**  
    **Text:** “2D pose estimation”, “person segmentation”, “phone's lens parameters”, “Python sandbox”.  
    **Problem:** These are functional parts of the proposal, but an advanced high-school reader may not know what information they provide. Naming implementations does not explain their functions.  
    **Fix:** Add compact glosses: “locating body joints in each image”; “marking the pixels belonging to the person”; “camera calibration values describing how the lens projects the scene”; and “an isolated environment for running Python code.”

13. **Low — figure-text-mismatch. The example submission contains two unexplained features.**  
    **Figure:** [fig_agent_loop.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_agent_loop.svg), panel B: “0.31 m/s” followed by “submit(three features + their code)”.  
    **Problem:** The illustrated run computes only center-of-mass speed before submitting three features. This omission is conspicuous in a figure intended to demonstrate traceability.  
    **Fix:** Add an explicit omitted-steps marker for the ankle-angle and hold-time calculations, or show those two calculations.

14. **Low — style. A slogan replaces a precise description of the figure.**  
    **Figure:** [fig_levers.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_levers.svg): “An agent is three things”.  
    **Problem:** This is an aphoristic, artificially exhaustive triad; it describes three components being optimized, not everything constituting the agent.  
    **Fix:** Replace with “Components changed by the four improvement steps.”

The proposal has a recognizable central comparison, but its controls, failure handling and reference-score definition are not yet precise enough to interpret a win. Cutting the duplicated optimization explanations and compute logistics would make the research question substantially more prominent without changing this version’s design.