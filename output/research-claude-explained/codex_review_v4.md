I reviewed the Markdown and all 30 referenced figures. No files were edited.

1. **High · overclaim — Verification does not establish measurement (§§2.5, 5.3).**  
   **Quote:** “every score traces back to measurements a clinician can inspect.”  
   **Why:** Replay establishes reproducibility; variation on two probes establishes input dependence. Neither establishes that the function computes the specified movement feature. Code could respond to body size, clip length, or agent-supplied annotations and pass all three checks.  
   **Fix:** Replace with: “Each score includes inspectable code and tool outputs. Separate accuracy tests assess whether these computations recover the defined movement features.” Add adversarial tests using irrelevant input statistics and annotation-encoded answers.

2. **High · error — A constant can pass the material-response test (§5.3).**  
   **Quote:** “The two results must differ by at least a quarter of the feature’s interquartile range … A constant, or a constant plus a negligible term, fails.”  
   **Why:** When the interquartile range is zero, the required difference is zero, so a constant passes. This is particularly relevant to capped hold times; Figure 2 shows a large concentration at five seconds. [fig_check_v4.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_check_v4.svg) repeats the unconditional claim.  
   **Fix:** Define a positive, feature-specific minimum response threshold and a separate rule for features with no meaningful training variation.

3. **High · overclaim — Teacher filtering does not guarantee learnable demonstrations (§§1, 5.5).**  
   **Quote:** “it may act only through the student’s tools, so its demonstrations remain ones the student can follow.”  
   **Why:** A permitted action can still depend on unavailable information—for example, choosing a start time from the reference curve. Removing explicit references to the panel does not remove that dependence. Testing final functions with expert annotations also does not test whether the student could select the teacher’s annotations or actions.  
   **Fix:** Say the filters reduce obvious dependence on privileged information, rather than guarantee learnability. Audit action and annotation choices using only student-visible evidence, and evaluate transfer empirically.

4. **High · logical-gap — The source of physical scale is missing (§5.1).**  
   **Quote:** “The agent receives the Cam0 video, the task description and the feature definitions with units.”  
   **Why:** Naming meters per second does not supply a conversion from pixels to meters. OpenCap Monocular assumes known participant height and camera parameters, which this input specification omits. [OpenCap Monocular methods](https://arxiv.org/html/2603.24733v1).  
   **Fix:** Specify the height and camera information supplied to reconstruction, how it is obtained at deployment, and which baselines receive it. Explain that height supplies a physical size reference.

5. **High · logical-gap — Evaluation has no complete failure policy (§§5.7, 8).**  
   **Quote:** “Evaluation always covers every eligible sealed row”; later, “because every case fell back to the mean.”  
   **Why:** The proposal never defines when fallback happens: failed tools, exhausted attempts, malformed submissions, missing features, or failed verification. Different choices can substantially change both accuracy and coverage.  
   **Fix:** Add one shared rule specifying failure triggers, whether one rejected feature invalidates the whole task, the training-derived fallback value, and how failed cases enter every reported metric.

6. **High · logical-gap — Component claims lack specified comparisons (§3).**  
   **Quote:** “Which component carries the gain: the teacher, the per-feature reward or verification?”  
   **Why:** The primary comparison changes teacher privilege and reward design together. It tests the complete recipe, but cannot identify which component caused an improvement. The proposal mentions removing verification without specifying the corresponding training arms.  
   **Fix:** Add an experiment table listing teacher access, reward, verification, compute, and seeds for every arm. Link each component claim to a comparison that holds the other components fixed.

7. **High · overclaim — Frame shuffling is not a decisive measurement test (§8.3).**  
   **Quote:** “A measuring agent’s features should change or become unverifiable, while an appearance reader’s would not.”  
   **Why:** A correctly measured maximum ankle angle can remain unchanged when the same frames are reordered. Conversely, changed outputs can result from tracking failures or sensitivity to artificial discontinuities. [fig_shuffle.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_shuffle.svg) makes the stronger claim that a measuring method “must change its answer.”  
   **Fix:** Restrict expected changes to features that depend on temporal order, specify expectations feature by feature, and describe the result as evidence of temporal sensitivity rather than proof of correct measurement.

8. **Medium · error — The shrinkage example contradicts its own ranking result (§2.7).**  
   **Quote:** “while telling us almost nothing about who balances better.”  
   **Why:** The shrunk predictions identify everyone’s order perfectly: their rank agreement is 1.0, as [fig_guess.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_guess.svg) correctly reports. They rank people better than the noisy predictor, whose agreement is 0.8. What they lose is the magnitude of differences.  
   **Fix:** Replace with: “The shrunk predictor orders everyone correctly but understates every score difference by a factor of five.” Update the caption to distinguish ordering from calibration.

9. **Medium · inconsistency — The ledger mixes recorded trials with nonexistent recordings (§6).**  
   **Quote:** “One row per recorded trial (3,322)” and “assigned zero for 98 tasks not attempted for safety.”  
   **Why:** An unattempted task has no recorded trial or Cam0 video. The split also totals 171 participants while retaining the exclusions of nine participants as an unresolved investigation; the figure already labels all 171 as having usable video.  
   **Fix:** Separate participant–task slots from recorded trials, with explicit links between them. Provide an eligibility accounting from 180 participants to the final split and define which statuses enter training and evaluation.

10. **Medium · inconsistency — Training-only rescaling does not guarantee scores between zero and one (§§2.1, 5.3–5.4).**  
    **Quote:** “rescaled to the range 0 to 1”; “the training range widened by half its width on each side.”  
    **Why:** A permitted value at the widened upper endpoint rescales to 1.5. Held-out reference values can also exceed training extrema. The proposal therefore cannot retain its unconditional descriptions of a zero-to-one scale.  
    **Fix:** Explicitly allow values outside that interval and explain their interpretation, or specify clipping consistently for predictions and references. Also define handling when the training minimum equals the maximum.

11. **Medium · overclaim — Demographic controls cannot identify what another model uses (§8.3).**  
    **Quote:** “appearance alone explains much of their success”; “A method that only reads age drops to near zero.”  
    **Why:** Similar performance by an age-and-sex baseline does not establish that another method uses appearance. Removing a straight-line association between ranks also does not remove every demographic relationship. A perfect age-rank predictor leaves constant residuals, making the remaining correlation undefined.  
    **Fix:** Say these controls assess predictive information beyond the specified demographic relationship. Avoid attributing a mechanism from matched performance, and define the zero-residual-variation case.

12. **Medium · error — Failure to demonstrate improvement is called refutation (§3).**  
    **Quote:** H2 is “Refuted if” its interval “includes zero.”  
    **Why:** An interval spanning zero can reflect insufficient precision. Conversely, an interval entirely below zero would contradict H2 but does not satisfy the written condition.  
    **Fix:** Use three outcomes: “supported if the entire interval is positive; contradicted if the entire interval is negative; otherwise inconclusive.” Apply similarly precise criteria to “no difference” claims elsewhere in the table.

13. **Medium · logical-gap — The conditional primary endpoint lacks a decision rule (§§7, 9).**  
    **Quote:** “If the demographic model matches the fine-tuned predictor’s rank agreement, age-adjusted rank agreement becomes co-primary.”  
    **Why:** “Matches” has no numerical definition. The later success rule mentions only ordinary rank agreement and skill, leaving unclear whether both ranking endpoints must succeed or how multiple testing is handled.  
    **Fix:** Define the development-stage trigger numerically and state the complete success rule for either branch before confirmation. Use that same rule in the power simulation.

14. **Medium · logical-gap — The power simulation does not specify the proposed effect (§§7, 9).**  
    **Quote:** “power for a 0.05 gain in rank agreement”; “resample … predictions of two existing methods.”  
    **Why:** Resampling their observed predictions does not automatically simulate a true gain of 0.05. The procedure also requires variability from repeated training, while the sample-size gate is described as occurring “before any training.”  
    **Fix:** Specify how simulated data represent the target ranking gain, skill constraint, and seed variability. Identify pilot training as part of Stage 0, using permanently designated development participants.

15. **Medium · inconsistency — Equal trajectory counts do not establish equal compute (§§3, 7, 10).**  
    **Quote:** “under the same compute budget”; “GRPO arms at equal numbers of trajectories.”  
    **Why:** Trajectories can differ in generated length, tool calls, and verification work. Teacher generation also has different input lengths with and without the panel. Equal counts therefore need not satisfy the central budget-matching promise.  
    **Fix:** Make measured H100-hours the primary stopping rule and report trajectory counts separately. State whether each budget includes all folds, seeds, teacher generation, and preceding optimization stages.

16. **Medium · figure-text-mismatch — The lever diagram omits proposer costs.**  
    **Figure:** [fig_levers.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_levers.svg), Figure 13.  
    **Quote:** Prompt optimization and harness search both say “Cost: agent runs only.”  
    **Why:** Both methods also run a proposer model; §10 explicitly includes that cost. The prose’s “No weights change, so the method is cheap” likewise treats a possible outcome as guaranteed.  
    **Fix:** Use “Cost: proposer calls and agent evaluations; no weight training.” Replace the absolute cost ranking with a statement that actual costs will be measured.

17. **Medium · logical-gap — Best-of-eight selection is unspecified (§7).**  
    **Quote:** “best-of-8 with label-free selection.”  
    **Why:** Without reference answers, “best” needs an observable selection rule. Selection can materially affect results, yet neither its criterion nor its relationship to the other agent arms is specified.  
    **Fix:** Define a deterministic rule—for example, most verified features, then lowest recorded cost, with a fixed tie-break—and the fallback when none qualifies. State which methods receive the same inference allowance.

18. **Medium · error — SFT is given an unjustified performance ceiling (§2.6).**  
    **Quote:** “SFT imitates; it cannot find a better strategy than the one in its examples.”  
    **Why:** The training objective encourages imitation, but does not mathematically prevent generalization or better performance. Supervised distillation has produced students outperforming their teachers. [Born Again Neural Networks](https://proceedings.mlr.press/v80/furlanello18a.html).  
    **Fix:** Replace with: “SFT trains on demonstrated outputs rather than directly rewarding newly generated attempts; its generalization depends on the examples and the starting model.”

19. **Medium · inconsistency — Task reweighting cannot preserve the promised ability mix (§5.7).**  
    **Quote:** “we log each task’s and each ability quintile’s share of updates and reweight any task whose share drifts.”  
    **Why:** Reweighting tasks does not correct a shift toward easier participants within each task. Teacher filtering and skipped groups can produce precisely that shift. Equal sampling of trial rows also gives more weight to people with more recorded trials.  
    **Fix:** State the intended sampling population explicitly. If preserving ability proportions is required, adjust sampling within task-and-ability groups and report groups with no usable demonstrations or updates.

20. **Medium · error — The definition of balance excludes ordinary dynamic balance (§2.1).**  
    **Quote:** “Balance is the ability to keep the body’s weight over the feet, whether standing still or moving.”  
    **Why:** During walking, the center of mass can move beyond the supporting foot without a fall; velocity and subsequent foot placement matter. [Experimental study of walking stability](https://pmc.ncbi.nlm.nih.gov/articles/PMC6715793/).  
    **Fix:** Replace with: “Balance is the ability to control body position and movement without falling. Standing still usually requires keeping the center of mass over the support area; walking also requires controlling momentum and foot placement.”

21. **Medium · undefined-term — The opening requires knowledge introduced much later (Abstract, §1).**  
    **Quote:** “a vision-language agent that calls pose, segmentation and reconstruction tools”; “per-feature reward”; “outcome-only reinforcement learning.”  
    **Why:** The intended reader encounters the proposed solution before understanding its components. “Spearman correlation −0.76” similarly appears before any explanation of correlation.  
    **Fix:** Introduce the system as “a computer model that chooses analysis programs and writes measurement code.” Briefly identify pose as joint locations, segmentation as outlining the person, and reward as a number guiding training; introduce technical names afterward.

22. **Medium · undefined-term — Later statistical and mathematical terms remain unexplained (§§5–10).**  
    **Quote:** “ability quintile,” “Kolmogorov–Smirnov tests and standardized differences below 0.1,” and “a crossed bootstrap over seeds and participants.”  
    **Why:** The earlier tutorial does not explain these terms or the combined resampling procedure. The reward equations also introduce symbols such as \(\hat S\), \(S^*\), and \(\lambda\) without a complete plain-language key.  
    **Fix:** Define quintiles as five equally sized score groups; explain what each distribution check detects; describe exactly how seeds and participants are resampled. Add a symbol key and one worked reward calculation, moving unnecessary test mechanics to an appendix.

23. **Medium · undefined-term — Several reproduced figures are inaccessible at the stated level.**  
    **Figures:** [qwen3vl_fig1_architecture.png](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/papers/qwen3vl_fig1_architecture.png), [lora_fig1.png](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/papers/lora_fig1.png), and [deepseekmath_fig4_grpo.png](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/papers/deepseekmath_fig4_grpo.png).  
    **Why:** Labels including “MoE Decoder,” “DeepStack,” “GAE,” and \(\mathcal N(0,\sigma^2)\) are unexplained. Figure 17 additionally depicts a reward model, although this proposal uses a computed reward rule, without explaining that distinction.  
    **Fix:** Replace these with minimal diagrams containing only necessary, defined components, or move the originals to an appendix. Explicitly distinguish the borrowed GRPO illustration from this study’s implementation.

24. **Low · concision — Background and figures repeat material needed only once.**  
    **Locations:** “### 2.6 Four ways to improve an agent,” “## 4. Related work,” and the stage table plus Figure 28.  
    **Why:** The background occupies roughly 4,900 words, and the document contains 30 figures. GEPA, harness search, teacher distillation, and several evaluation concepts receive repeated introductions; the stage figure largely duplicates its table.  
    **Fix:** Retain first-principles definitions and the rise-to-toes example, shorten related work to relevant differences, remove duplicate stage presentation, and move LoRA matrix arithmetic and the PPO comparison to an appendix.

25. **Low · style — Announcements and anthropomorphic wording interrupt the explanation.**  
    **Quotes:** “Two results stand out”; “This has been observed”; “Three more ideas from statistics appear below”; “helps it see where the one-camera tools went wrong.”  
    **Why:** Repeated announcements add little information, while “see where … went wrong” blurs the distinction between comparing outputs and establishing their correctness.  
    **Fix:** State the result directly: “The fine-tuned model achieved…,” “Xu reports…,” and “The teacher compares one-camera outputs with the reference curves.” Integrate necessary definitions where they first matter.

The proposal has a coherent research question and a useful running example, but its verifier and movement controls do not establish its strongest claims. Its scoring, comparison, and decision rules need clarification before the experiment is reproducible. It also needs a shorter background, first-use definitions, and simpler figures to serve the intended high-school reader.