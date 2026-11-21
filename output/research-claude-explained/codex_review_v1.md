I reviewed the [proposal](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v1_stable-tool-agent-reframe.md) and all 20 referenced figures. No files were edited.

1. **High — error.** §5.3: “a better score can only come from better features.”

   **Why:** Feature errors can cancel during averaging. Reference features of 0.2 and 0.8 and incorrect predictions of 0.5 and 0.5 produce the same task score. The score-only reinforcement-learning reward therefore cannot establish accurate measurements.

   **Fix:** Replace with: “The fixed formula makes score calculation reproducible. Individual feature errors must be evaluated separately because errors can cancel in the average.” Add this limitation to Risks without changing the proposed reward.

2. **High — figure-text-mismatch.** §5.3 requires “a pointer to the tool output and the time window”; [fig_agent_loop.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_agent_loop.svg) instead requires “features in physical units, plus the code that computed each one.”

   **Why:** These are different submission requirements. A source pointer alone cannot establish how a feature was calculated, and neither requirement specifies verification of the claimed calculation.

   **Fix:** Require the feature value, executable calculation, tool-output identifier, tool settings and time window. State that the harness reruns the calculation and checks agreement before accepting the submission.

3. **High — logical-gap.** §5.1: “The agent receives only the video from the left-side phone (Cam0).”

   **Why:** The named reconstruction tool assumes known participant height, camera calibration information and a stationary camera. These inputs matter because image distances alone do not determine meters or meters per second. The proposal omits how they reach the tool. [OpenCap Monocular methods](https://arxiv.org/html/2603.24733v1)

   **Fix:** Enumerate all permitted inputs, including information supplied directly to tools. Explain where height and camera calibration come from; if they are estimated instead, describe that estimation and its consequences for physical measurements.

4. **High — logical-gap.** §6.3: “the primary question requires zero failures”; §5.4: “The reward for a run is minus the absolute difference between its task score and the reference task score.”

   **Why:** “Valid” is undefined, failed runs have no score from which to calculate this reward, and there is no stopping budget. Unlimited retries and accepting arbitrary finite numbers could radically change the apparent failure rate.

   **Fix:** Define required features, units, calculation checks, maximum calls or runtime, and treatment of missing or malformed outputs. Specify a fixed reward for failed training attempts and state that failed test cases prevent reporting an all-case MAE.

5. **High — inconsistency.** §4 asks which method “gives the largest gain per unit of compute,” but §5.4 applies them “in turn, each starting from the best agent so far.”

   **Why:** Later stages inherit earlier improvements and encounter different starting conditions. This design measures contributions within one sequence; it cannot isolate which method is generally most effective.

   **Fix:** Preserve the sequence and narrow the question: “How much additional accuracy does each stage provide, at what additional cost, in this fixed order?” Report both additional and cumulative compute.

6. **Medium — overclaim.** §2.7 describes “a test set, used once at the end,” while §6.1 retains “the same as in the pilot.”

   **Why:** The pilot’s test results already inform the proposal’s motivation and design. One additional evaluation does not make this an untouched test set, although it can remain a useful benchmark.

   **Fix:** State: “We reuse the pilot’s benchmark cohort. No further test results will guide development; the final evaluation measures performance on this previously studied benchmark.” Avoid presenting it as fully independent confirmation.

7. **Medium — error.** §2.1: “each feature is rescaled to the range 0 to 1.”

   **Why:** The displayed formula guarantees that range only when the input lies between \(L\) and \(U\). With the stated speed limits, a prediction of 0.60 m/s becomes approximately 1.16. Predictions can exceed the reference dataset’s extrema.

   **Fix:** Explain the formula’s domain and explicitly specify the scorer’s out-of-range policy—clipping, rejection or allowing extrapolation—consistently with the baseline. Also specify handling of \(U=L\).

8. **Medium — logical-gap.** §2.1 defines \(L\) and \(U\) as “the lowest and highest values of that feature in the dataset.”

   **Why:** “The dataset” could mean all 180 participants, the development set or each training fold. These choices produce different scores and affect both baseline comparability and the blanket prohibition on test information in §2.7.

   **Fix:** Identify the exact calibration population and constants. Distinguish published constants that define the benchmark from quantities estimated during model development, and confirm that every compared method uses the same scoring scale.

9. **Medium — figure-text-mismatch.** §6.1: “The other 128 participants form the development set”; [fig_split_v1.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_split_v1.svg): “171 participants with usable single-camera video.”

   **Why:** The prose introduces 180 participants, but \(128+43=171\). Only the figure introduces the reduced population, and neither explains the nine exclusions. Similarly, 729 examples leave 45 missing participant–task combinations relative to \(43\times18\).

   **Fix:** Add a short inclusion statement accounting for the nine excluded participants and the missing task examples, with explicit eligibility criteria. Change the figure’s “18 task videos of one person” to “up to 18.”

10. **Medium — inconsistency.** §8: “every tool output is computed once per video and stored.”

    **Why:** Point tracking depends on selected points; cropping depends on the requested region; harness search can change tool settings. One stored output per video cannot cover these changing requests.

    **Fix:** State: “We reuse outputs for identical video, tool-version and argument combinations. Requests with new points, crops or settings require computation.” Include those computations in the cost estimate.

11. **Medium — figure-text-mismatch.** [fig_levers.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_levers.svg) labels prompt optimization and harness search “Cost: agent runs only”; §2.6 says, “No weights change, so the method is cheap.”

    **Why:** Both methods also run a proposer language model. Frozen weights do not imply low total computation, and equal agent-run counts do not account for proposal generation, varying run lengths or training updates.

    **Fix:** Change both labels to “Agent evaluations + proposer-model calls.” Report these costs alongside training and tool computation, and replace the categorical cheapness claim with “It avoids weight updates, but total cost depends on the search budget.”

12. **Medium — logical-gap.** §5.1: “The 76 features computed from the three-camera reconstruction serve as reference values.”

    **Why:** The released StaBLE scoring code includes age-based replacement of some missing features and special zero-score rules for inability to complete tasks. The proposal does not establish whether its targets are independently recomputed measurements or released values containing these exceptions. [StaBLE scoring code](https://raw.githubusercontent.com/stanfordnmbl/stable-analysis/main/compute_scores.ipynb)

    **Fix:** Identify the exact target files or computation procedure. Flag any substituted reference values and explain incomplete-task scoring; distinguish these from directly measured features in the feature-agreement analysis.

13. **Medium — logical-gap.** §8 proposes “2D pose and point tracking, for timing features such as hold time, which do not need a full 3D skeleton.”

    **Why:** The defined hold time depends on the center of mass remaining above half its rise. Timing a heel or another image landmark measures a different event unless equivalence is established. Having seconds as the output unit does not remove the geometric requirement.

    **Fix:** Name the observable used by each fallback and explain how it estimates the defined feature. Describe it as an approximation and evaluate its agreement with the reference.

14. **Medium — logical-gap.** §5.4 selects runs “whose features land close to the reference values”; §4 asks “how often” features agree.

    **Why:** Neither “close” nor “agree” has a numerical definition. This leaves both the supervised-training dataset and a secondary research outcome unspecified. Errors in degrees, seconds and meters per second cannot share an unexplained threshold.

    **Fix:** Define feature-specific acceptance tolerances and the rule for accepting an entire trajectory. Report feature MAE in physical units and, if reporting agreement frequency, the fraction within each declared tolerance.

15. **Medium — error.** §3: “In all three, the tasks are question answering and the reward is whether the final answer is right.”

    **Why:** This contradicts Figure 19’s caption, which lists accuracy, format and tool-use rewards. ToolRL also explicitly rewards tool names, parameter names and parameter values, rather than only final-answer correctness. [ToolRL reward design](https://arxiv.org/html/2504.13958v1), [DeepEyes reward design](https://arxiv.org/html/2505.14362v3)

    **Fix:** Replace with: “These studies train tool use with different rewards: DeepEyes combines answer accuracy, formatting and conditional tool-use rewards, while ToolRL evaluates the correctness and formatting of tool calls.”

16. **Medium — overclaim.** §2.6: “SFT imitates; it cannot find a better strategy than the one in its examples.”

    **Why:** Matching training examples is the optimization objective, not a mathematical ceiling on resulting behavior. Supervised fine-tuning can generalize beyond its examples; the categorical contrast with reinforcement learning teaches a false distinction. [Research on SFT generalization](https://arxiv.org/abs/2604.06628)

    **Fix:** Replace with: “SFT trains the model to reproduce example outputs. RL instead evaluates newly generated attempts using a reward; neither method guarantees discovery of a better strategy.”

17. **Medium — overclaim.** Abstract: “they fail on unusual movements”; “always return an answer, but they explain nothing.”

    **Why:** These turn observations about particular pilot implementations into universal properties of entire method families. The document also calls tools “validated” without distinguishing validation on selected movements from validation on all 18 balance tasks.

    **Fix:** Limit the claims to the reported implementations: “In the lab’s pilot, reconstruction-based scoring failed on some tasks, while direct predictors returned scores without accompanying feature measurements.” Specify the movement range covered by tool validation.

18. **Medium — logical-gap.** §4 requires error “lower than that of the fine-tuned Qwen baseline (0.100)”; §2.7 says an interval “entirely above zero” indicates an advantage.

    **Why:** The subtraction order is never defined, and the proposal does not distinguish a lower observed error from evidence of improvement beyond this sample. The rounded value 0.100 is also insufficient for a close comparison.

    **Fix:** Define the difference as baseline MAE minus agent MAE, using unrounded paired predictions. Report observed improvement separately from whether its confidence interval excludes zero, while retaining zero failures as the stated success requirement.

19. **Medium — undefined-term.** Abstract: “prompt optimization, harness search, fine-tuning and reinforcement learning”; Introduction: “a neural network” and “a harness.”

    **Why:** The reader encounters the main technical claims before receiving the definitions several sections later. The abstract cannot stand alone for the specified audience.

    **Fix:** Use plain descriptions on first appearance: “rewriting instructions, changing the software that runs tools, learning from successful examples, and learning from scored attempts.” Introduce the technical names alongside those descriptions.

20. **Medium — undefined-term.** Figures 2, 4, 9, 15 and 17, especially:
    [qwen3vl_fig1_architecture.png](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/papers/qwen3vl_fig1_architecture.png),
    [lora_fig1.png](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/papers/lora_fig1.png), and
    [deepseekmath_fig4_grpo.png](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/papers/deepseekmath_fig4_grpo.png).

    **Why:** The originals introduce unexplained histograms, summation symbols, probability distributions, matrix notation, “Dense/MoE Decoder,” “DeepStack” and “GAE.” The short captions do not make these figures readable from first principles.

    **Fix:** Replace expert architecture figures in the main text with simplified diagrams of the needed concepts. Put originals and symbol explanations in an appendix, and explain a histogram as bars counting observations within value ranges.

21. **Medium — undefined-term.** §2.5: “writing the few lines of code that turn a center-of-mass curve into a peak speed.”

    **Why:** This skips the central measurement operation. A novice has not been told what the curve represents or how changing position becomes speed.

    **Fix:** Add a worked sentence: “The curve records estimated height at each time. A rise of 0.01 meters over 0.05 seconds gives an average upward speed of 0.20 meters per second; comparing such intervals identifies the fastest rise.” Put the precise smoothing and calculation procedure in an appendix.

22. **Medium — error.** Figure 16’s caption: “reward minus the group average, divided by the spread of rewards within the group”; §2.6: “the others are made less likely.”

    **Why:** “Spread” is undefined, identical rewards produce division by zero, and an attempt exactly at the mean has zero advantage rather than a negative one. These cases are plausible when all attempts fail.

    **Fix:** Define the spread as standard deviation, explain its calculation briefly, and specify the equal-reward convention. Say that above-mean attempts receive positive advantages, below-mean attempts negative advantages, and ties no reward-based preference.

23. **Low — concision.** §2.6: “GEPA … asks it to rewrite the instructions”; §3: “GEPA … rewrites prompts using feedback from runs”; §5.4: “GEPA rewrites the system prompt and the tool descriptions.”

    **Why:** The four improvement methods are introduced three times. Tool descriptions and the three-route motivation are also substantially repeated.

    **Fix:** Keep first-principles explanations in Background, make Related Work explain differences from previous studies, and reserve Method for this experiment’s settings, selection rules and budgets. Replace repeated tool prose with a reference to the existing table.

24. **Low — structure.** §4: “By the ICML 2027 submission deadline…” and “Each part of the question has a purpose. One model family, one dataset, one group of held-out people and one outcome make the answer unambiguous.”

    **Why:** The scientific question is interrupted by scheduling and commentary about how the question was constructed. The claim of being “unambiguous” substitutes reassurance for the missing operational definitions.

    **Fix:** Move the deadline and feasibility discussion to Timeline. Delete the commentary about question construction and state the comparison, outcome and failure criterion directly.

25. **Low — style.** §1: “Geometry stays with validated tools, judgment and bookkeeping go to the model.”

    **Why:** The slogan-like parallelism and attribution of “judgment” obscure the concrete division of work. It also reinforces the unsupported impression that tool-produced geometry is assuredly correct.

    **Fix:** Replace with: “Existing programs estimate body position; the language model selects tools and generates code to calculate the required features.”

The proposal has a workable research question, but its current wording promises measurement validity that its score-based training cannot establish. Several experimental rules need specification before the comparisons are interpretable, and the opening and reproduced figures still assume substantial technical knowledge. These issues can be corrected while preserving this version’s scientific design and shortening the document.