The revision fixes the reward signs and the timing-control problem, but several scientific and scope issues remain.

Against the earlier review, using its original numbering:

1. **Resolved — Reward signs:** §3.2 now explicitly subtracts the capped error-and-penalty sum and assigns malformed answers −4.
2. **Resolved — Treatment comparison:** The headline and all three reward formulas now hold timing supervision constant.
3. **Partly resolved — Cancellation mechanism:** The ranking prediction is added, but “Offsetting errors are tuned to the training videos and become person-specific errors on new people” states the proposed mechanism as fact rather than hypothesis.
4. **Resolved — Pipeline scoring:** Figure 4 now uses submitted features, distinguishes malformed-answer fallback, and removes the cost-aware reward arm.
5. **Resolved — Outcome definition:** Training tasks define the primary average; skill uses task-level MAE ratios against training medians; constant predictions receive rank agreement 0 and unparseable answers receive a fallback.
6. **Partly resolved — Logistics:** Several counts disappeared from the prose, but Figure 4 still specifies “Sealed · 60 people” and “Development · 111 people in 5 folds”; paired-run planning also remains.
7. **Partly resolved — Competing objectives:** The abstract now ends with the primary comparison, but “Secondary questions, tested in a fixed order” still introduces five formal comparisons, including teacher quality, agent superiority and transfer.
8. **Partly resolved — Score direction:** Reversal is explained, but “using the lowest and highest values among all 180 participants” is not explicitly distinguished in prose from Figure 4’s training-only endpoints.
9. **Resolved — Feature definitions:** Peak plantar flexion and the half-peak-rise threshold for hold time are now explained.
10. **Resolved — Range rule:** The author retained widened-range rejection rather than adopting warning-only treatment; prose and Figure 5 now agree, so this is an acceptable retained design choice.
11. **Resolved — S2 interpretation:** S2 now measures starting-performance benefit, and §3.3 explicitly says it does not resolve individual teacher decisions’ dependence on the reference panel.
12. **Resolved — Generalization claim:** §5 limits support to single-camera balance assessment and frames other domains as future tests requiring suitable references and checks.
13. **Partly resolved — Concision:** The peripheral surveys are gone, but “retrospective re-split of existing data” appears in both §§4 and 5, alongside repeated explanations of the training-only reference.
14. **Partly resolved — Vocabulary:** The original training/tool terms are glossed and SFT/GRPO removed, but “Satterthwaite’s degrees of freedom” and Figure 4’s “Calibration slope” remain unexplained.
15. **Resolved — Aphoristic contrast:** The “built to measure” sentence has been removed.

Additional problems and serious residuals, most severe first:

1. **High — The experiment’s normalization rule remains ambiguous.**  
   **Quotes:** “using the lowest and highest values among all 180 participants” ([§2](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v7_final_rewarding-what-can-be-checked.md:33)); “Endpoints … come only from each fold’s training part” ([Figure 4](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/pipeline_v7.svg:60)).  
   **Why:** The all-participant rule correctly describes the [published StaBLE method](https://pmc.ncbi.nlm.nih.gov/articles/PMC13621976/), but §3.2 never identifies which endpoints define this experiment’s rewards and reference scores. Different feature ranges change their relative weights in the task average and can change participant rankings; this affects the primary outcome.  
   **Fix:** Add one explicit distinction: published StaBLE uses all-participant endpoints, whereas this study fixes endpoints from training participants—or the designated calibration data for transfer tasks—and applies them identically to predictions and references.

2. **Medium — Figure 4 introduces an unspecified optimization stage.**  
   **Quote:** “Prompt and harness / search, no weights,” connected to “updates harness or weights” ([Figure 4](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/pipeline_v7.svg:209)).  
   **Why:** The prose describes demonstration training followed by reward training; it never explains this additional search. If prompts or the harness are optimized separately between arms, the comparison changes more than reward design.  
   **Fix:** Remove this box if obsolete, or label the search as shared preparation whose resulting prompts and harness remain fixed across reward arms.

3. **Medium — The “reference-free” check leaves its reference dependency unclear.**  
   **Quotes:** “responds to the same edit of the reference curves” and “None of them needs the reference value of the video being analyzed” ([§3.1](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v7_final_rewarding-what-can-be-checked.md:57)).  
   **Why:** The required-signal test does not identify whose reference curves supply the expected response. If they belong to the current video, the check requires the privileged instrument; if they are development curves used to establish general rules, that crucial distinction is missing.  
   **Fix:** State that expected responses are established from development references, while checks on a new video operate only on its single-camera tool outputs and those fixed rules.

4. **Medium — The general checking procedure accidentally becomes rise-to-toes-specific.**  
   **Quote:** “Each submitted feature faces four tests,” followed by “four development videos of the task, two slow and two fast risers” ([§3.1](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v7_final_rewarding-what-can-be-checked.md:57)).  
   **Why:** Walking, reaching and standing tasks do not necessarily contain a rise. Even within rise-to-toes, speed differences do not ensure informative differences in ankle angle or capped hold time.  
   **Fix:** Say that known-answer examples span the relevant feature’s values, then identify slow and fast risers explicitly as the peak-speed example.

5. **Medium — The cancellation rationale assumes the result it should test.**  
   **Quote:** “Offsetting errors are tuned to the training videos and become person-specific errors on new people, which scramble the ordering” ([§1](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v7_final_rewarding-what-can-be-checked.md:13)).  
   **Why:** Cancellation can persist on new participants; penalizing individual feature errors does not mathematically guarantee better task-score rankings. Figure 1 establishes different reward preferences, not the claimed generalization behavior.  
   **Fix:** Write: “We hypothesize that feature errors that cancel during training will cancel less reliably on unseen people, reducing rank agreement.” Keep the following prediction explicitly conditional on that hypothesis.

6. **Medium — S1 can demonstrate added benefit, not necessity.**  
   **Quotes:** “Whether the check is needed” and “with S1 confirming that the check is needed” ([comparison table](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v7_final_rewarding-what-can-be-checked.md:25); [§5](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v7_final_rewarding-what-can-be-checked.md:85)).  
   **Why:** Checked rewards could outperform unchecked per-feature rewards while both outperform final-score rewards. That establishes an incremental benefit, not that checking is necessary for improvement.  
   **Fix:** Replace both formulations with “whether the check adds benefit beyond per-feature rewards.”

7. **Medium — Protocol detail still prevents this from being the requested snapshot.**  
   **Quotes:** “estimated from paired training runs,” “Development participants form five folds,” “Satterthwaite’s degrees of freedom,” and Figure 4’s “Development · 111 people in 5 folds” ([§1](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v7_final_rewarding-what-can-be-checked.md:19); [§4](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v7_final_rewarding-what-can-be-checked.md:73); [Figure 4](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/pipeline_v7.svg:57)).  
   **Why:** Allocation and retraining plans remain despite the explicit exclusion of logistics. The detailed testing hierarchy and interval machinery also compete with the research question and exceed the intended reader’s assumed vocabulary.  
   **Fix:** Remove allocation counts and replication procedures from prose and figures; retain participant separation, matched scientific controls, the primary outcome, and one sentence that uncertainty accounts for participant differences and retraining variability. Compress the secondary comparisons into subordinate diagnostics and explain or remove figure-only statistical terms.

The document is not yet ready as the requested concise research-proposal snapshot, although its central reward comparison is substantially clearer and now has correct incentives. Clarifying normalization and check inputs, qualifying the causal claims, aligning Figure 4, and removing the remaining protocol detail would address the main obstacles without changing v7’s distinctive design.