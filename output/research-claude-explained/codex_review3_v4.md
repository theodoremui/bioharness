I checked the [revised proposal](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v4_privileged-teacher-and-budgeted-levers.md) and all five linked figures. No files were edited.

Against the prior review’s numbered findings:

1. **Partly resolved — Verification overclaim:** §3.1 is appropriately qualified, but §5 still claims “response to movement in selected videos.”
2. **Resolved — Dropping the teacher:** The additional arm remains omitted, acceptably; §5 explicitly acknowledges that the teacher’s contribution under verified rewards remains untested.
3. **Resolved — Mechanism versus ranking:** The rationale now connects participant-specific errors on unseen people to the predicted improvement in ordering.
4. **Partly resolved — Logistics:** The budget ladder is gone, but “A and B are run with several training seeds; C and D with one” remains, alongside Figure 4’s “at most 40 per task.”
5. **Partly resolved — Reference supervision in the control:** A’s reference-derived reward is acknowledged, but “and the score alone” overlooks the reference-based feature filters also applied to A’s teacher.
6. **Resolved — Equal compute:** The unsupported compute claim is replaced with the narrower, defensible control of equal numbers of attempts.
7. **Resolved — Changing primary endpoint:** Rank agreement stays primary; age-adjusted agreement is consistently secondary.
8. **Partly resolved — Undefined correlation:** “Constant predictions count as rank agreement 0” handles prediction collapse, but constant reference scores remain unaddressed.
9. **Resolved — Participant counts:** Conflicting prospective allocations are removed; the remaining counts describe the dataset and historical pilot.
10. **Partly resolved — Shuffle figure:** Its description is improved, but the appearance-model box still asserts “Its output barely moves.”
11. **Resolved — ToolRL characterization:** The revised description correctly recognizes detailed tool-call rewards, consistent with [ToolRL §3.3](https://arxiv.org/html/2504.13958v1#S3.SS3).
12. **Partly resolved — Undefined vocabulary:** Most terms are explained or removed, but Figure 4 still introduces unexplained “LoRA.”
13. **Partly resolved — Repetition:** The optics and literature digressions are cut, but “Two traps make accuracy figures misleading here” still repeats both motivations from the abstract.
14. **Resolved — Teacher threshold:** Both prose and figure use “at least as accurate”; accepting ties is an internally consistent alternative to the suggested stricter rule.
15. **Partly resolved — Aphoristic writing:** The closing antithesis is gone, but “the training signal decides much of what the agent learns” remains a broad, repetitive maxim.

The following are new problems or serious residuals, ordered by severity:

1. **High · research-question — H2’s comparison cannot identify shortcut reduction.**  
   **Quote:** “Verification reduces shortcut use”; assessed through B against D, with “No change in rank agreement” counting against it.  
   **Why:** Better ranking could result from improved numerical accuracy without reduced shortcut use; reduced shortcuts could also leave rankings unchanged. The outcome measures predictive performance, not the claimed mechanism.  
   **Fix:** Rename H2 to “Verification improves held-out rank agreement.” Treat shortcut reduction as a possible explanation, assessed separately through the existing diagnostics. Make the null-result wording consistent with the stated rule that an interval containing zero is inconclusive.

2. **High · overclaim — The conclusion reinstates the verification claim corrected in the methods.**  
   **Quote (§5):** “The checks establish reproducibility and response to movement in selected videos, not correctness.”  
   **Why:** Even a response in the correct direction across two people could depend on body proportions or another correlated characteristic. This contradicts §3.1’s appropriate statement that movement dependence remains an experimental question.  
   **Fix:** Replace “response to movement” with “variation across selected videos,” retaining the distinction between passing checks and measuring the intended movement.

3. **Medium · research-question / figure mismatch — H4 still conflates movement dependence with predictive advantage.**  
   **Quotes:** H4 counts “no gain over an age-and-sex model” against movement dependence; [Figure 5](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_shuffle.svg:191) says an appearance-based method’s output “barely moves.”  
   **Why:** A noisy movement measurement can perform worse than demographics while still measuring movement. Conversely, an appearance-based model can change after shuffling because frame selection or processing changes. Neither result establishes the claimed distinction.  
   **Fix:** Describe demographic comparisons as tests of added predictive value and shuffling as a test of temporal sensitivity. Qualify the figure’s invariance claim as applying only to an appearance baseline whose processing ignores frame order.

4. **Medium · error — The decision metrics still have undefined cases.**  
   **Quotes:** “Constant predictions count as rank agreement 0”; skill divides error by “that of the training-median guess.”  
   **Why:** Spearman correlation remains undefined when reference scores are constant. Skill is undefined when the baseline’s error is zero, including a possible zero-over-zero result. These cases can also arise in resamples.  
   **Fix:** State a shared, method-independent rule for constant-reference tasks and degenerate resamples. When baseline error is zero, report absolute error instead of the skill ratio.

5. **Medium · inconsistency — The control receives feature-level information through demonstration selection.**  
   **Quotes (§1):** “the contrast is between richer use of it … and the score alone”; **§3.3:** “The teacher without reference curves is the same model without the panel, with identical filters.”  
   **Why:** Those filters assess individual feature functions against reference-based criteria and the expert pipeline. Consequently, the control’s demonstrations are also selected using information beyond final scores, even though its teacher never sees the panel. The intended comparison remains valid, but its description is inaccurate.  
   **Fix:** Say that both teachers share reference-based demonstration filtering; the experimental differences are panel access during demonstration generation and the reinforcement-learning reward.

6. **Medium · ambiguity — The historical and experimental scoring scales need an explicit distinction.**  
   **Quotes (§2):** “using the lowest and highest values among all 180 participants”; **§4:** “Rescaling endpoints … come from training participants only.”  
   **Why:** These can describe different stages consistently, but the transition is unstated. Changing feature-specific endpoints changes their relative contributions to task scores and can change participant ordering; training-based endpoints also do not automatically keep unseen values within 0–1.  
   **Fix:** Explicitly label the first rule as the published StaBLE normalization. State that experimental predictions and reference features use the same training-derived endpoints, and specify whether values beyond those endpoints are clipped.

7. **Medium · figure-text mismatch — Figure 3 omits the revised direction requirement.**  
   **Quote ([Figure 3](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_check_v4.svg:37)):** “The two results must differ by at least a quarter of the feature’s typical spread.”  
   **Why:** §3.1 now additionally requires the difference to follow the reference direction. The figure’s written rule permits a sufficiently large reversed response, which the prose rejects.  
   **Fix:** Add “in the same direction as the reference values” to the figure’s acceptance rule.

8. **Medium · scope / readability — Prohibited planning details survive in both prose and artwork.**  
   **Quotes:** “A and B are run with several training seeds; C and D with one”; [Figure 4](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_teacher.svg:45): “fine-tuned with LoRA” and “demonstrations (at most 40 per task).”  
   **Why:** These retain replication allocation, a demonstration quota, and unexplained implementation terminology despite the requested proposal-snapshot scope. Removing them only from the Markdown leaves them in the document readers actually see.  
   **Fix:** Remove seed allocations and demonstration quotas, replace the figure’s LoRA wording with “trained on the kept demonstrations,” and retain participant separation and the scientific arm definitions.

The document is not yet ready as the requested concise proposal snapshot. Its central comparison is now coherent, but readiness requires narrower interpretations of the diagnostics, complete scoring conventions, synchronized figures, and removal of the remaining logistics.