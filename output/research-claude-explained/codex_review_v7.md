I reviewed the [proposal](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v7_final_rewarding-what-can-be-checked.md), all 17 referenced SVGs, and all 13 reproduced paper figures. No files were edited.

1. **High · logical-gap — The inputs needed to recover physical scale are missing.**  
   **Quote:** “Validated tools handle geometry, so the model never has to estimate a speed from pixels” (§2.5).  
   **Problem:** Moving the calculation into a tool does not resolve the scale ambiguity explained in §2.2. OpenCap Monocular requires participant height, known camera parameters, and a stationary camera; the proposal’s input diagrams list only video, task text, and feature definitions. These requirements are explicit in the [OpenCap Monocular paper](https://arxiv.org/html/2603.24733v1).  
   **Fix:** Specify how height and camera parameters are supplied or obtained, include them in the input diagrams, and explain which measurements remain possible without them.

2. **High · error — The checker can reject correct capped features.**  
   **Quotes:** “both low probes below both high probes” (Appendix A); “shifting the moment the center of mass drops must change the output” (§3.2).  
   **Problem:** Hold time is capped at five seconds. Shifting a crossing need not change a capped answer, and the selected lower and upper percentile probes can have identical reference values. Figure 2 visibly shows a large concentration at the cap. Strict ordering would then reject even the reference computation.  
   **Fix:** Define cap-aware perturbation expectations and tie-aware probe rules. Require strict ordering only where reference values differ by a specified minimum amount.

3. **High · inconsistency — “Credit only checked features” is not the proposed reward.**  
   **Quote:** “A feature earns credit only when its code passes a check” (§1).  
   **Problem:** Appendix A includes every feature’s error and adds a finite penalty for failing the check. Reducing an unchecked feature’s error still improves its reward; GRPO can reinforce an unchecked attempt that outperforms its group. This is a soft penalty, not conditional eligibility for credit.  
   **Fix:** Preserve the design but describe it accurately throughout: “Reward feature accuracy and apply an additional penalty to features that fail verification.” Revise the title and thesis accordingly.

4. **High · error — The shrinkage example teaches the wrong lesson.**  
   **Quote:** “while telling us almost nothing about who balances better” (§2.7).  
   **Problem:** The shrunk predictions preserve everyone’s ordering perfectly. They also preserve all score information through an invertible linear transformation. [fig_guess.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_guess.svg) correctly reports rank agreement 1.0, exceeding the noisy predictor’s 0.8. The problem is understated differences, not missing information about who performs better.  
   **Fix:** “The shrunk predictor ranks everyone correctly but understates the differences between them. The noisy predictor estimates their magnitudes more closely but makes two ordering errors.” Correct the caption too.

5. **High · logical-gap — The reward comparisons are not fully specified.**  
   **Quotes:** “Error of the final score” (§8.1); “plus a fixed penalty for each unchecked feature” (§8.1); “+ 0.1 × timing error” (Appendix A).  
   **Problem:** Only the checked arm receives a complete reward formula. It is unclear whether timing penalties, reward caps, and malformed-output penalties also apply to the controls. If timing supervision differs, the primary comparison changes more than feature scoring and verification.  
   **Fix:** Give all three reward equations together, explicitly identifying shared terms and differing terms. Describe any deliberately different timing supervision as part of the tested treatment.

6. **High · logical-gap — The uncertainty calculation is not reproducible.**  
   **Quote:** “combines two sources of uncertainty: the spread between the seven paired differences, and the participant-bootstrap spread of the seed-averaged difference” (§8.4).  
   **Problem:** “Combines” does not define an estimator. Run-to-run spread differs from uncertainty in the mean, and both calculations reuse the same participants. The treatment of their interaction is unspecified. The paragraph also describes seven differences although S2 uses five seeds.  
   **Fix:** Put the exact variance calculation, degrees-of-freedom calculation, seed counts, and simulation scenarios in an appendix. State whether the target averages over RL retraining alone or also over warm-start retraining.

7. **Medium · inconsistency — Training-only endpoints no longer guarantee scores between zero and one.**  
   **Quote:** “a task score between 0 and 1” (§2.1).  
   **Problem:** After endpoints are fitted on training participants, a new participant can exceed them. Using the example endpoints, 0.60 m/s becomes approximately 1.16. Neither clipping nor another out-of-range policy is specified. A constant training feature also makes the denominator zero.  
   **Fix:** Specify out-of-range and zero-width-range rules for predictions and references. Either define consistent clipping or acknowledge that these rescaled values can fall outside 0–1.

8. **Medium · error — The range test does not establish physical plausibility.**  
   **Quote:** “The value is physically plausible” (§3.2).  
   **Problem:** The actual rule merely widens the observed training range. For the illustrated hold-time range of 0.2–5 seconds, it permits −2.2–7.4 seconds, including negative durations and values above the feature’s explicit cap.  
   **Fix:** Enforce feature-specific physical and definitional bounds separately from the empirical training-range check. For capped hold time, require 0–5 seconds.

9. **Medium · figure-text-mismatch — The slowdown figure handles the cap incorrectly.**  
   **Figure:** [fig_timescale.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_timescale.svg): “longer, ×1.25” and “except a hold already at the 5-second cap.”  
   **Problem:** A hold can reach the cap after slowing without having been capped originally. A 4.5-second hold becomes 5 seconds, not 5.625 seconds. The prose correctly delegates this calculation to StaBLE’s code.  
   **Fix:** Replace the figure’s rule with “Increases until it reaches the five-second cap; expected values are recomputed with StaBLE’s code.”

10. **Medium · overclaim — Tiny noise does not reliably defeat memorization.**  
    **Quote:** “A function that recognizes this particular video and returns a memorized number takes a different path on the noisy copy and fails” (§3.2).  
    **Problem:** Recognition can tolerate small noise. A function based on rounded summaries or smoothly varying identifying features can return the same memorized answer after perturbation. The later qualification that checking is weaker than proof does not repair this specific guarantee.  
    **Fix:** “Noisy replay can expose brittle, exact-match lookups.” Include noise-tolerant recognition programs in the shortcut suite and report their observed rejection rates.

11. **Medium · overclaim — Transferable feature code does not establish transferable teacher decisions.**  
    **Quote:** “which removes solutions tuned with hindsight to one video” (§3.3).  
    **Problem:** A general feature function can work on five other videos while the teacher’s current tool choice or time marks still depend on the privileged reference. Testing the function does not test whether those decisions are recoverable from the student’s input.  
    **Fix:** “This filter rejects some video-specific computations, but does not establish that the student can reproduce the teacher’s tool choices or annotations.”

12. **Medium · logical-gap — The tool-outcome model predicts a different quantity from the one claimed.**  
    **Figure:** [fig_worldmodel.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_worldmodel.svg): labels come from “the expert pipeline’s feature code,” but “predicted errors of the final features” flag unreliable scores.  
    **Problem:** Error from fixed expert code is not automatically the error of arbitrary agent-written code using agent-selected time marks. The prediction target changes between training and use.  
    **Fix:** Call this an estimate of the fixed expert route’s error. Treat its ability to flag errors in agent submissions as a separate empirical question.

13. **Medium · inconsistency — “Before any analysis” overstates the test set’s isolation.**  
    **Quotes:** “60 are set aside before any analysis”; “the pilot trained models on some of the sealed participants” (§6).  
    **Problem:** The retrospective limitation is acknowledged, but the stronger wording persists in the prose and split diagrams. Readers can mistake this for a historically untouched test cohort.  
    **Fix:** Use “reserved before development of the present experiment” consistently, and state beside the split diagram that some participants previously contributed to pilot training.

14. **Medium · logical-gap — The pilot plot does not define the failed-case denominator.**  
    **Figure:** [fig_pilot.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_pilot.svg): “on 729 task scores,” alongside “valid score in only 567 of 729 cases.”  
    **Problem:** It is unclear whether OpenCap’s 0.146 error uses only successful cases or includes assigned outputs for failures. Those are different comparisons, especially when difficult cases cause failures.  
    **Fix:** Label the denominator and failure treatment for every bar. If 0.146 is conditional on success, say so explicitly and avoid presenting it as directly comparable to all-case errors.

15. **Medium · error — SFT has no hard ceiling at demonstration quality.**  
    **Quote:** “SFT imitates; it cannot find a better strategy than the one in its examples” (§2.6).  
    **Problem:** The imitation objective does not mathematically restrict the trained model to reproducing demonstrated strategies. Generalization, prior capabilities, and combining patterns can produce better behavior.  
    **Fix:** “SFT trains the model to imitate demonstrations; it does not explicitly search for strategies with higher reward.”

16. **Medium · inconsistency — The related-work summary omits DeepEyes’ tool reward.**  
    **Quote:** “train VLMs to crop, zoom or resample video from rewards on final answers” (§5).  
    **Problem:** This framing obscures an important distinction already present in Figure 27’s caption: DeepEyes includes format rewards and a conditional tool-use bonus. Its [reward specification](https://arxiv.org/html/2505.14362v3) confirms this.  
    **Fix:** Describe those additional rewards, then locate this proposal’s contribution specifically in physical-feature errors and verification tests.

17. **Medium · overclaim — Frame-shuffle invariance does not establish complete visual neglect.**  
    **Quote:** “a sign that the models had stopped using the video” (§2.8).  
    **Problem:** A model can use visual appearance while ignoring frame order. The cited experiment concerns questions dependent on temporal structure, and its diagnostic specifically tests sensitivity to that structure. [Xu, Appendix A.3](https://arxiv.org/html/2606.22043v1).  
    **Fix:** “The answers became less sensitive to frame order on questions requiring temporal information.” Replace Figure 19’s anthropomorphic “stops watching” title with “Reduced sensitivity to temporal order.”

18. **Medium · logical-gap — Several supposedly fixed decision rules remain undefined.**  
    **Quotes:** “within a fixed tolerance” (§8.3); “ranks people as well as the direct predictor” (§7).  
    **Problem:** Neither the intervention tolerance nor the rule triggering an age-adjusted co-primary outcome is specified. “Removing the effect of age” also lacks a defined procedure. These choices can materially change the conclusions.  
    **Fix:** State the tolerance or its development-only selection rule, the comparison criterion for activating the co-primary outcome, the age-adjustment procedure, and the resulting success rule.

19. **Medium · undefined-term — The opening assumes concepts explained much later.**  
    **Quotes:** “vision-language model,” “pose, segmentation and 3D reconstruction tools” (Abstract); “GPU-minutes” (§1).  
    **Problem:** These are central to understanding the proposal, but their plain definitions arrive several sections later. The introduction also uses “center of mass” before explaining it.  
    **Fix:** Introduce short glosses at first use: a model processing pictures and text; tools locating joints, outlining the person, and estimating three-dimensional movement; graphics-processor time. Move the center-of-mass definition to its first occurrence.

20. **Medium · undefined-term — Advanced terminology remains unexplained after the tutorial.**  
    **Quotes:** “gradient-boosted trees” (§4); “25th … percentile” and “standard deviation” (Appendix A); “H100-hours” (§9).  
    **Problem:** These labels require background the intended reader explicitly lacks. Naming a method or giving a citation is not a definition.  
    **Fix:** Explain boosted trees as successive sets of branching prediction rules that correct earlier errors; percentiles as positions in sorted data; standard deviation as a numerical measure of spread; and an H100-hour as one hour on one specified graphics processor.

21. **Medium · undefined-term — The reproduced diagrams introduce unexplained technical machinery.**  
    **Figures:** [qwen3vl_fig1_architecture.png](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/papers/qwen3vl_fig1_architecture.png), [deepseekmath_fig4_grpo.png](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/papers/deepseekmath_fig4_grpo.png), and [pi_distill_fig1.png](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/papers/pi_distill_fig1.png).  
    **Problem:** Labels such as “Dense/MoE Decoder,” “DeepStack,” “GAE,” and the teacher–student objective equations are not explained by the captions. Readers cannot tell which components matter.  
    **Fix:** Use simplified main-text diagrams containing only explained concepts, or explicitly guide readers through the relevant portion. Put full technical reproductions in an appendix.

22. **Medium · concision — Repeated explanations and diagrams delay the experiment.**  
    **Quote:** “A lucky training run shifts every participant at once, and resampling participants cannot average that away” (§8.4).  
    **Problem:** This repeats §2.12 and Figure 22. The background occupies roughly 4,900 words and 22 figures; §7 then presents the same eight stages in both a detailed table and Figure 29.  
    **Fix:** Keep the first explanation of training randomness and use a short cross-reference later. Retain the detailed stage table and remove its duplicate diagram. Move optional architecture and algorithm-history material to an appendix while preserving essential first-principles explanations.

23. **Medium · figure-text-mismatch — Search costs omit the proposer model.**  
    **Figure:** [fig_levers.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_levers.svg): “Cost: agent runs only.”  
    **Problem:** Both prompt optimization and harness search also invoke a proposer model. Those calls can be expensive, particularly when comparing methods under matched budgets. “No weights change, so the method is cheap” likewise does not follow automatically.  
    **Fix:** “Cost: proposer-model calls, agent runs, and tool execution; no weight training.” State that all three costs enter budget comparisons.

24. **Low · structure — The SMART checklist is proposal-writing meta-commentary.**  
    **Quote:** “The question is specific … measurable … achievable … relevant … and time-bound” (§4).  
    **Problem:** This evaluates the document against a writing rubric rather than advancing its scientific argument. The surrounding sections already supply the scope, measurements, feasibility, and schedule.  
    **Fix:** Delete the paragraph.

25. **Low · style — The introduction uses a staccato buildup and slogan.**  
    **Quote:** “We propose a vision-language agent that measures. It calls validated tools … To train it we follow one rule.” Followed by “**Thesis: reward the measurements, and only those that can be checked.**”  
    **Problem:** The short declarations and slogan repeat the proposal’s premise while making an unresolved research question sound settled.  
    **Fix:** “We will train a vision-language agent to call measurement tools and calculate StaBLE features, rewarding accuracy and penalizing computations that fail predefined checks.”

The proposal is not ready for its intended reader: several central explanations are incorrect, and key protocol details remain undefined. The most urgent repairs concern capped-feature verification, the reward claim, and the measurement and inference specifications. A shorter background with simpler figures could preserve this version’s scientific design while making the proposal substantially clearer.