Reviewed the proposal and all 25 referenced figures. No files were changed.

1. **High · overclaim — Verification does not establish measurement (§1, §5.3).**  
   **Quote:** “confirm that the number really came from a measurement”  
   **Problem:** Code returning a typical value plus a tiny input-dependent adjustment can pass replay, dependence and range checks without computing the requested feature. The same overclaim appears in [fig_check_v3.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_check_v3.svg).  
   **Fix:** Say: “The checks establish reproducibility and limited input dependence; they do not establish that the code implements the feature definition.” Test deliberately incorrect programs, including typical-value-plus-noise shortcuts, and add feature-specific checks using inputs whose expected measurements are known.

2. **High · logical-gap — The dependence check rejects correct capped measurements (§5.3).**  
   **Quote:** “The value must change.”  
   **Problem:** Hold time is capped at five seconds. Correct measurement code can return five seconds for the original video and both replacement videos; Figure 2’s histogram shows that this outcome is common. Such code would receive the maximum feature penalty despite being correct.  
   **Fix:** Allow equal outputs when the feature legitimately saturates. Test dependence using probes selected to have different expected values, or inspect the uncapped intermediate measurement.

3. **High · error — The justification for the primary outcome contradicts the example (§3).**  
   **Quote:** “ordering people correctly, which a method that stays near typical values cannot do”  
   **Problem:** The compressed predictor in [fig_guess.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_guess.svg) stays near the average and achieves rank agreement **1.0**, exceeding the noisy predictor’s **0.8**. Any positive linear compression preserves ranks. Section 2.7’s claim that this predictor tells us “almost nothing about who balances better” is therefore also wrong.  
   **Fix:** State: “Rank agreement measures ordering but cannot detect compressed differences; calibration slope and feature error assess those failures.” Revise the Figure 18 caption accordingly.

4. **High · logical-gap — Training and evaluation are undefined for several ledger statuses (§5.4–§6.4).**  
   **Quote:** “Every method is scored on every confirmatory row”  
   **Problem:** The ledger includes unperformed tasks, missing videos, imputed references, reconstruction errors and excluded cases. A fallback prediction cannot supply a trustworthy missing reference. Section 5.4 excludes imputed and flagged features but does not explain how the 98 assigned-zero trials enter training, or how rewards are averaged when features are omitted.  
   **Fix:** Add a compact status table defining training eligibility, reward denominators, evaluation eligibility and coverage denominators. Retain every slot in availability reporting, while separating measurement accuracy from agreement with assigned or imputed scores.

5. **High · logical-gap — Enlarging the sealed set can contaminate it (§7.4).**  
   **Quote:** “the confirmatory set is enlarged to 60 participants before any training begins”  
   **Problem:** The enlargement decision uses “cross-validated baselines,” which already require training and evaluation on development participants. Moving another 17 of those people into the confirmatory set would violate the promised separation.  
   **Fix:** Reserve the maximum 60-person candidate set before development begins, calculate power using only the remaining participants, and then select the final sealed sample without examining its outcomes. Update Figure 25 and development counts for either branch.

6. **High · logical-gap — Required information for physical scale is missing (§5.1).**  
   **Quote:** “The agent receives the Cam0 video, the task description and the StaBLE feature definitions with units.”  
   **Problem:** The cited OpenCap Monocular method assumes known participant height and camera intrinsics—the camera parameters connecting image coordinates to viewing directions. These inputs matter when converting pixels into meters and meters per second, yet their source is unspecified. [OpenCap Monocular, §2.2.2](https://arxiv.org/html/2603.24733v1)  
   **Fix:** Explicitly list the metadata supplied to the reconstruction tool, how it is obtained at deployment, and which comparison methods receive it. If scale is estimated instead, describe and evaluate that estimation.

7. **High · error — The hypothesis table confuses inconclusive evidence with refutation (§3).**  
   **Quote:** “Refuted if … The crossed-bootstrap interval for the difference includes zero”  
   **Problem:** An interval spanning zero can contain substantial benefits and harms; it does not refute improvement. “Unchanged” and “No difference” have the same problem. H1’s rule also misses a large slope increase, which would contradict the proposed drift toward typical values.  
   **Fix:** Distinguish support, evidence against and inconclusive results. Define directional changes and meaningful equivalence margins in advance; require an interval sufficiently narrow to establish equivalence before describing two methods as unchanged.

8. **Medium · logical-gap — The power calculation does not specify the planned statistic (§7.4).**  
   **Quote:** “the spread of per-participant differences is estimated from cross-validated baselines”  
   **Problem:** Mean within-task Spearman correlation is calculated jointly across participants; it is not an average of ordinary per-participant differences. The proposal supplies neither a construction for those differences nor a target power, and the calculation omits the seed variation included in the final decision rule.  
   **Fix:** Simulate the complete planned comparison using participant-level prediction records, recomputing ranks on each sample and including plausible training-run variation. Specify the target power and evaluate both parts of the primary decision rule.

9. **Medium · logical-gap — A single sandbox cell may not be replayable (§5.3).**  
   **Quote:** “Re-execute the cell in a clean sandbox with the cited inputs.”  
   **Problem:** The cell may depend on earlier helper functions, filtered signals or manually selected event boundaries. Figure 12 explicitly selects start and end times before computing speed. Transferring those times to another video can miss its movement entirely, even when the original computation was valid.  
   **Fix:** Require a self-contained computation or its complete chain of dependencies. Specify how time windows are handled on replacement videos and how an unusable replacement window affects the check.

10. **Medium · error — The range check accepts impossible hold times (§5.3).**  
    **Quote:** “the training-fold range of that feature, widened by half its width on each side”  
    **Problem:** With the illustrated hold-time range of 0.2–5.0 seconds, this permits **−2.2 to 7.4 seconds**. Negative duration and values above the defined five-second cap can therefore pass the range check.  
    **Fix:** Apply the widened empirical range together with the feature’s physical and definitional limits. For capped hold time, the accepted interval must remain within 0–5 seconds.

11. **Medium · logical-gap — Constant predictions can make the primary estimator undefined (§7.2).**  
    **Quote:** “Spearman correlation within each task, averaged over tasks.”  
    **Problem:** Spearman correlation is undefined for a constant prediction vector, a central failure mode of this proposal. Ties also arise from caps, assigned zeros and fallback predictions. No rule explains their handling, including in bootstrap samples. [SciPy’s Spearman documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html)  
    **Fix:** Specify average ranks for ties and a prespecified reporting or failure convention for constant predictions. Apply it consistently across methods and bootstrap samples; do not silently drop collapsed tasks.

12. **Medium · logical-gap — The multiple-testing family is not operationally defined (§3, §7.4).**  
    **Quote:** “Secondary questions (pre-registered and Holm-corrected as one family)”  
    **Problem:** One question contains three comparator methods, another concerns adaptive tool use, and the coverage question is descriptive unless a threshold is specified. Consequently, neither the number of tests nor their null hypotheses is clear. Several relevant trained arms also have only one seed and are designated exploratory.  
    **Fix:** Provide a short table listing each confirmatory contrast, outcome, null hypothesis or margin, and p-value procedure. Keep descriptive coverage estimates and exploratory comparisons separate from that testing family.

13. **Medium · logical-gap — Malformed output can outperform a valid control-arm submission (§5.4).**  
    **Quote:** “−1 for a submission that cannot be parsed.”  
    **Problem:** The score-only reward is uncapped and has no verification. A parseable submission with score error 1.7 receives −1.7, whereas malformed output receives −1. This creates an avoidable reward loophole.  
    **Fix:** Bound valid score penalties consistently and assign malformed submissions a reward below the worst permitted valid reward. State whether the format penalty replaces or supplements other penalties.

14. **Medium · overclaim — The reference is described as independent without qualification (§4).**  
    **Quote:** “an independent and more accurate measurement system”  
    **Problem:** The three-camera reconstruction includes Cam0, which also supplies the agent’s input, and the pipelines can share modeling assumptions. Their errors need not be independent, and agreement with this reference does not establish physical accuracy for every feature.  
    **Fix:** Use “a separately computed three-camera reference” and explicitly limit conclusions to agreement with that reference. Add shared measurement error to the limitations.

15. **Medium · overclaim — Frame-shuffle invariance does not establish that a model ignores video (§2.8).**  
    **Quote:** “a sign that the models had stopped using the video”  
    **Problem:** Shuffling preserves individual frames. A model can use appearance, posture or unordered frame content while remaining insensitive to temporal order. The cited paper itself describes this diagnostic as a proxy with limitations. [Xu, §8](https://arxiv.org/html/2606.22043v1)  
    **Fix:** Say: “The answers became less sensitive to frame order, consistent with reduced use of temporal information.” Replace the anthropomorphic Figure 19 title, “A video-language model stops watching,” with “Answers become less sensitive to frame order.”

16. **Medium · figure-text-mismatch — The pilot comparison has an unclear denominator (Figure 8).**  
    **Figure:** [fig_pilot.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_pilot.svg)  
    **Quoted labels:** “on 729 task scores” and “valid score in only 567 of 729 cases”  
    **Problem:** It is unclear whether OpenCap’s reported 0.146 error uses its 567 successful cases or all 729 cases with fallback predictions. Those calculations support different comparisons. The later confirmatory failure rule does not establish what the pilot did.  
    **Fix:** State the pilot’s denominator and failure treatment beside the result. If it used successful cases only, label that explicitly and supply a comparison using common cases or consistent fallbacks.

17. **Medium · inconsistency — Coverage changes from a feature-level question to a row-level metric (§3, §6.4).**  
    **Quotes:** “What fraction of the agent’s reported features pass verification” and “the share of rows whose features all pass verification”  
    **Problem:** These are different quantities. If one of three features fails in every trial, feature coverage is two-thirds while complete-trial coverage is zero.  
    **Fix:** Define and report both **feature verification rate** and **complete-trial verification rate**, with explicit denominators, or consistently choose one.

18. **Medium · inconsistency — The caching contribution contradicts the tool table (§1, §5.1).**  
    **Quote:** “every reachable tool call is computed in advance”  
    **Problem:** The tool table explicitly marks frame extraction, plotting and arbitrary Python execution as live. These calls cannot all be precomputed.  
    **Fix:** Replace this with: “All permitted calls to expensive vision tools are precomputed; frame extraction, plotting and Python execution run live.” Limit replay claims to computations whose inputs, dependencies and execution settings are recorded.

19. **Medium · error — SFT is given an unsupported performance ceiling (§2.6).**  
    **Quote:** “SFT imitates; it cannot find a better strategy than the one in its examples.”  
    **Problem:** An imitation objective does not impose that ceiling. A trained model can generalize across demonstrations, and supervised distillation can outperform its teacher on downstream tasks. [Hsieh et al., 2023](https://aclanthology.org/2023.findings-acl.507/)  
    **Fix:** Replace the aphorism with: “SFT trains the model to reproduce demonstrations. RL instead scores newly generated attempts, providing a direct way to favor alternatives to the demonstrated behavior.”

20. **Medium · error — The opening definition of balance incorrectly generalizes static balance (§2.1).**  
    **Quote:** “Balance is the ability to keep the body's weight over the feet, whether standing still or moving.”  
    **Problem:** During movement, balance depends on velocity and foot placement as well as position; the center of mass can lie outside the supporting area without a fall. [Hof et al., 2005](https://pubmed.ncbi.nlm.nih.gov/15519333/)  
    **Fix:** “Balance is the ability to control body position and movement without falling. During quiet standing, this usually requires keeping the center of mass above the area supported by the feet; during walking, momentum and foot placement also matter.”

21. **Medium · undefined-term — The abstract and introduction require knowledge introduced much later.**  
    **Quotes:** “tool-calling vision-language agent”; “pose, segmentation and reconstruction tools”; “harness”; “trajectory”  
    **Problem:** The reader must understand the proposed contribution before receiving the definitions in Sections 2.4–2.6. The abstract is particularly dense with unfamiliar machinery.  
    **Fix:** Introduce the idea in ordinary language first: “We train a model that accepts video and text to choose analysis programs and write code that calculates balance measurements.” Define the surrounding controller and a complete analysis attempt when first needed; reserve tool taxonomy for the method section.

22. **Medium · undefined-term — Several statistical and methodological terms remain unexplained.**  
    **Quotes:** “ability quintile”; “regressor”; “Ablation”; “estimators”; “relative tolerance”; “spread of rewards”  
    **Problem:** These terms are needed to follow sampling, comparisons, verification and GRPO, yet the document does not provide usable first-principles definitions. “Spread,” in particular, is insufficient to reproduce Figure 16’s advantages.  
    **Fix:** Define them inline: a quintile is one of five equally sized ordered groups; a regressor predicts a number; an ablation removes a component to test its contribution; an estimator is a calculation summarizing a quantity. Identify reward spread as standard deviation and explain its calculation with a small example.

23. **Medium · undefined-term — Reproduced figures introduce substantial unexplained notation.**  
    **Figures:** [qwen3vl_fig1_architecture.png](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/papers/qwen3vl_fig1_architecture.png), [lora_fig1.png](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/papers/lora_fig1.png), and [deepseekmath_fig4_grpo.png](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/papers/deepseekmath_fig4_grpo.png)  
    **Problem:** Labels such as “Dense/MoE Decoder,” “DeepStack,” \(A=\mathcal N(0,\sigma^2)\), and “GAE” remain unexplained. The GRPO diagram also includes a reward model although this proposal calculates rewards directly, creating a misleading architectural implication.  
    **Fix:** Use simplified, attributed adaptations containing only relevant components, or move the originals to an appendix. Explicitly identify which components this proposal replaces.

24. **Medium · concision — The tutorial delays the proposal and repeats later sections.**  
    **Quoted sections:** “2.6 Four ways to improve an agent,” “2.10 Testing fairly,” and “2.11 Measuring uncertainty”  
    **Problem:** Eleven background subsections and 21 figures precede the research question. Splitting, leakage and uncertainty are then explained again in Sections 6–7; detailed LoRA arithmetic and the PPO comparison contribute little to understanding the central reward experiment.  
    **Fix:** Keep the essential definitions and rise-to-toes example in the main narrative. Move architecture details and peripheral paper figures to an appendix, explain each statistical concept beside its actual use, and remove standalone transitions such as “This has been observed.”

The proposal presents a plausible reward comparison, but its verification checks and primary-outcome rationale do not support its strongest measurement claims. Missing-data handling, test-set enlargement and statistical decision rules need resolution before the experiment can yield interpretable conclusions. The worked arithmetic largely checks out, while the intended reader needs earlier definitions, simpler figures and a shorter main narrative.