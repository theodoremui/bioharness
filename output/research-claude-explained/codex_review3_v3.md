I checked the revised [proposal](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v3_measurement-grounded-rewards.md) and all five embedded figures. No files were changed.

Statuses follow the original review’s numbering:

1. **Resolved — Ranking mechanism.** The rationale now predicts person-specific errors that change ordering and treats compression separately.
2. **Resolved — Feature direction.** §3.3 defines both normalization directions and explicitly averages those values into task scores.
3. **Resolved — Verification overclaim.** Both prose and Figure 5 limit the guarantee to reproducibility and input variation; the audit includes nearly constant and unrelated-input programs.
4. **Resolved — Malformed submissions.** Both valid rewards lie between −1 and 0, making the −2 parsing penalty strictly worse.
5. **Partly resolved — Logistics.** Most counts and allocations disappeared, but “Development participants form five folds, split by person and balanced by score, age and elite-athlete status” still specifies prohibited allocation planning.
6. **Resolved — Error bound.** The mathematical bound now applies explicitly to uncapped errors; the capped reward is identified as a surrogate.
7. **Resolved — Reference exclusions.** Whole trials with imputed or flagged references are consistently excluded from both rewards and primary evaluation.
8. **Resolved — Failure handling.** §4 states the shared fallback and retains numerical predictions regardless of verification status.
9. **Resolved — Main-question prominence.** The abstract now ends with one primary question; the search/optimization menu is gone, and retaining explicitly subordinate questions is acceptable.
10. **Resolved — Thaman attribution.** The benchmark is now described observationally, consistent with [its stated attribution limits](https://arxiv.org/html/2605.02964v1).
11. **Partly resolved — Frame-order overclaim.** The figure disappeared, but §2 still says “answers stop depending on the order of events”; [Xu reports increased shuffle invariance and calls it a proxy](https://arxiv.org/html/2606.22043v1).
12. **Resolved — Excessive conclusions.** §5 limits support to the tested tasks and correctly leaves the necessity of adaptive tool use unestablished.
13. **Resolved — Excessive inventories.** Related work and tool descriptions are substantially shorter and now serve the proposal’s explanation.
14. **Resolved — Previously identified vocabulary.** Trajectory, pose, segmentation and sandbox receive explanations; training seeds are no longer mentioned.
15. **Resolved, with acceptable retention — Framing.** The aphoristic pivot is gone; the retained “Measure Balance Instead of Guessing It” can reasonably express the proposed aim, so a title change is unnecessary.

Four additional problems warrant correction:

1. **High · Overclaim — The abstract assumes the causal effect being investigated.**  
   **Quote:** “reinforcement learning that rewards only the final number makes such shortcuts more likely.”  
   **Why:** This asserts an established effect for balance prediction, while §2 says whether final-score training causes such behavior here remains a research question. Figure 1 establishes that erroneous features can receive a good final-score reward; it does not establish that training increases shortcut use.  
   **Fix:** Replace with: “A reward on the final score can be high even when individual feature estimates are wrong.”

2. **Medium · Research-question weakness — H2’s measurements do not establish shortcut reduction.**  
   **Quote:** “Verification reduces shortcut use”; “Counts against it if removing the check changes neither rank agreement nor slope.”  
   **Why:** As Figure 1 demonstrates, different feature errors can produce identical scores. Shortcut use could therefore change without changing either statistic. Similarly, evaluating “the hard subset of cases the expert pipeline flags as failures” does not itself test dependence on video.  
   **Fix:** Rephrase H2 as whether verification improves score prediction, describe the hard subset as a robustness check, and reserve shortcut conclusions for direct program audits.

3. **Medium · Contradiction and repetition — Reference availability is described inconsistently.**  
   **Quote:** §§2 and 6 both say the instrument “exists only for the training data,” whereas §1 says the reference “enters rewards and evaluation.”  
   **Why:** Held-out reference scores are essential to the primary outcome; the repeated training-only claim contradicts that requirement.  
   **Fix:** State once: “Three-camera references supply training rewards and held-out evaluation targets, but are never inputs to the agent.”

4. **Medium · Accessibility — Statistical terminology remains unexplained where it determines conclusions.**  
   **Quote:** “95% interval,” “Holm’s procedure,” and “bootstrap resample.”  
   **Why:** Advanced high-school readers cannot reliably interpret the decision rules from these names alone, despite the improved explanations of agent terminology.  
   **Fix:** Briefly explain an uncertainty interval, repeated sampling with replacement, and correction for multiple comparisons; omit procedural names where they add little to the snapshot.

The revision is substantially stronger, but it is not yet ready as the requested concise research-proposal snapshot. Correct the remaining overclaims and reference-use contradiction, align the secondary tests with their claims, and remove allocation planning while preserving the central reward-comparison design.