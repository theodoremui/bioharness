1. **High · research-question — The mechanism does not predict the primary outcome.**  
   **Text:** “Final-score RL drifts toward typical values, lowering the calibration slope”; “The primary measure is **rank agreement**.”  
   **Problem:** Compressing predictions toward typical values can preserve every person’s rank. Spearman correlation is unchanged by any strictly increasing transformation, so preventing compression does not itself predict better ranking.  
   **Fix:** Add the missing hypothesis: “We predict that feature-level rewards reduce participant-specific measurement errors that reverse people’s task-score ordering.” Keep calibration slope as a secondary diagnostic, and distinguish this prediction from the mathematical argument about average error.

2. **High · error — The task-scoring specification omits feature direction.**  
   **Text:** “rescaled with training-fold endpoints by \(n_f(x)=(x-L_f)/(U_f-L_f)\).”  
   **Problem:** The only explicit normalization increases with the feature value. StaBLE reverses this direction for features where lower values mean better performance, such as deviation. Absolute feature errors are unaffected by reversing both values, but averaging the stated normalization into task scores can change the target and its rankings. [StaBLE’s scoring methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC13621976/) specify both directions.  
   **Fix:** Define score normalization as \((x-L)/(U-L)\) for higher-is-better features and \((U-x)/(U-L)\) for lower-is-better features; explicitly use these values in task-score averages.

3. **High · research-question — The verification check does not block the proposed shortcut.**  
   **Text:** “Verification is what blocks the shortcut.” [fig_check_v3.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_check_v3.svg) says the dependence check “blocks typing a guess and attaching an unrelated pointer.”  
   **Problem:** A typical value plus a small, detectable input-dependent perturbation can pass replay, dependence and range checks while remaining essentially a guess. An unrelated statistic can also vary across videos. The caveat in §3.2 acknowledges semantic uncertainty but does not repair these stronger claims.  
   **Fix:** Say “The check rejects constant-return programs; whether it suppresses more general shortcuts is an empirical question.” Include nearly constant and unrelated-input programs in the already proposed adversarial audit.

4. **High · error — The control reward can favor malformed submissions.**  
   **Text:** “An unparseable submission receives −2 in both arms, below any valid reward.”  
   **Problem:** The final-score control has neither an explicit score bound nor a capped loss. A parseable score more than two units from its reference receives less than −2, making a malformed submission preferable. Training-fold normalization does not itself bound predictions.  
   **Fix:** Define a bounded control reward, for example \(r_{\mathrm{final}}=-\min(|\hat{s}-s^*|,1)\), so the −2 parsing penalty is genuinely below every valid reward.

5. **High · structure — Prohibited logistics occupy substantial space.**  
   **Text:** “a training run costs only model computation”; “at most 40 per task”; “a new **confirmatory set** of 43 participants”; “the two primary arms use three seeds each.”  
   **Problem:** These are compute, sampling and run-allocation details expressly excluded by the brief. The fold diagram and sampler-reweighting rules further turn the snapshot into an execution protocol.  
   **Fix:** Cut the cost rationale, demonstration and trajectory counts, planned split counts, fold diagram, seed allocation and sampler thresholds. Retain the scientific controls: both arms share the starting model, tools, training data and learning procedure; evaluation holds out entire participants.

6. **Medium · error — The stated error bound does not apply to the capped reward.**  
   **Text:** “because the error of an average never exceeds the average of the errors, rewarding accurate features also rewards an accurate score”; feature error “is capped at 1.”  
   **Problem:** The inequality concerns uncapped errors. For normalized references \((0,0)\) and predictions \((1.5,0)\), score error is 0.75 while average capped feature error is 0.5. Even without clipping, reducing an upper bound need not improve the actual score error—as Figure 1 itself illustrates.  
   **Fix:** State: “Uncapped average feature error bounds task-score error. The capped reward is a surrogate whose effect on score accuracy and ranking must be tested.”

7. **Medium · inconsistency — Reference exclusions change from features to whole trials.**  
   **Text:** “Features whose reference was filled in from age or flagged for reconstruction error are left out of the reward”; “trials with imputed or flagged references … [are] kept out of rewards and the primary evaluation.”  
   **Problem:** These specify different inclusion rules. A partially flagged trial could contribute under the first rule and disappear under the second, leaving the reward comparison and evaluation population ambiguous.  
   **Fix:** Choose one rule and apply it consistently. A concise option is: “Both reward arms and the primary evaluation use trials with complete, unflagged reference features.”

8. **Medium · clarity — Failure handling is hidden in a figure and remains incomplete.**  
   **Figure:** [fig_split_v3.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_split_v3.svg) mentions “the average used when a method fails.”  
   **Problem:** The Measures paragraph never states that fallback or explains whether failed verification counts as failure. Different handling of missing and rejected predictions can change rank agreement and skill.  
   **Fix:** Put the policy beside the primary measure. For example: “All methods are evaluated on the same eligible trials; missing task scores receive the training-task mean. Numerical predictions remain in the ranking regardless of verification status, which is reported separately.”

9. **Medium · structure — Secondary questions compete with the main question.**  
   **Text:** The abstract asks “whether this reward orders unseen people more accurately … and whether any gain comes from adaptive tool use or only from access to tool outputs and feature labels.” The question table then adds H1–H3 and Q4–Q5.  
   **Problem:** The abstract presents two coequal aims, followed by a broad benchmark program involving prompt optimization, harness search and multiple-run aggregation. The reward comparison loses prominence.  
   **Fix:** End the abstract with the primary reward question. Keep verification removal and fixed tool calls as subordinate mechanism checks; fold slope and coverage into diagnostics. Cut the optimized-prompt and searched-harness comparison menu from this snapshot.

10. **Medium · overclaim — The cited tool-agent study does not isolate final-answer rewards.**  
    **Text:** “tool-using agents trained this way skip verification more often.”  
    **Problem:** “This way” attributes the behavior to final-answer-only training. Thaman compares models with different post-training pipelines and explicitly describes the result as an association rather than a single-variable ablation. [Thaman, §6.2](https://arxiv.org/html/2605.02964v1)  
    **Fix:** Replace with: “Tool-use benchmarks also report verification-skipping and other exploits; whether final-score-only training causes these behaviors here remains untested.”

11. **Medium · figure-text-mismatch — Figure 4’s caption overstates the plotted result.**  
    **Text:** “the answers stop depending on the order of events.”  
    **Figure:** [visual_shortcut_fig1.png](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/papers/visual_shortcut_fig1.png).  
    **Problem:** The graph shows unchanged-answer frequency increasing from roughly 75% to 91%, not complete independence from event order. The source also identifies frame-shuffle invariance as a proxy, not proof of how answers are produced. [Xu, limitations](https://arxiv.org/html/2606.22043v1)  
    **Fix:** Use: “Answers become less sensitive to frame order: the fraction unchanged after shuffling rises from roughly 75% to 91%.” Prefer cutting this figure because §1 already supplies the motivating citation.

12. **Medium · overclaim — The proposed conclusions exceed what the comparisons establish.**  
    **Text:** “supports rewarding intermediate measurements whenever a better instrument is available”; “the gain comes from the tools and labels, and adaptive tool use adds little.”  
    **Problem:** One dataset cannot establish the “whenever” generalization. Similar performance from different systems also does not identify the cause of either system’s performance; failure to demonstrate superiority is not evidence of equivalence.  
    **Fix:** Replace with: “A gain would support this reward design on the tested StaBLE tasks. Comparable performance from fixed pipelines would leave the necessity of adaptive tool use unestablished.”

13. **Medium · concision — The literature catalogue and tool inventory exceed the snapshot’s needs.**  
    **Text:** “Reinforcement learning has taught vision-language models to crop, zoom and resample video…”; “point tracking on 16 predefined body regions, OpenCap Monocular 3D reconstruction with two settings…”  
    **Problem:** §6 surveys several research areas, while §3.1 inventories implementation choices already illustrated in Figure 5. Neither needs this much space to establish the proposed contribution.  
    **Fix:** Cut the crop/zoom catalogue and detailed tool settings. Reduce related work to one positioning sentence: “Prior work rewards final answers, tool-call correctness or labeled reasoning steps; this proposal rewards physical feature estimates against a three-camera reference.”

14. **Medium · undefined-term — Essential vocabulary arrives without accessible glosses.**  
    **Text:** “training trajectories,” “training seeds,” “2D pose,” “person segmentation,” “Python sandbox.”  
    **Problem:** These terms are not reliably familiar to advanced high-school readers, and several appear before their role becomes clear.  
    **Fix:** Add brief first-use glosses where retained: trajectory—one sequence of tool calls and a submission; seed—a random setting distinguishing training runs; 2D pose—joint positions in an image; segmentation—identifying the person’s pixels; sandbox—an isolated environment for executing code.

15. **Low · style — The framing uses antithesis and an aphoristic pivot.**  
    **Text:** “Measure Balance Instead of Guessing It”; “The reward is where the two meet.”  
    **Problem:** The title implies the desired distinction has already been established, while the pivot sounds polished without adding scientific content.  
    **Fix:** Use the title “Feature-Level Rewards for Tool-Calling Balance Assessment.” Replace the pivot with: “StaBLE’s reconstructed features let us compare rewards for intermediate estimates with rewards for final scores.”

The proposal has a testable core, but its current rationale does not yet explain why the intervention should improve ranking, and its scoring and verification claims need correction. Preserve the measurement-reward design while narrowing the conclusions, clarifying the evaluation rules and removing the operational detail.