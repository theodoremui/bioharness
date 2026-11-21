For the 15 findings in the previous review, assessed against the [current proposal](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v2_measure-or-guess-evaluation.md):

1. **Partly resolved — mechanism:** Ordering is now linked to person-specific information, but hypothesis A still claims the error advantage “comes mostly from compression (calibration slope below 0.5),” which that slope cannot establish.
2. **Resolved — changing primary measure:** Rank agreement remains primary regardless of the observed slope.
3. **Resolved — mean baseline:** The proposed skill measure uses the training median; the historical pilot retains its mean baseline.
4. **Partly resolved — information held fixed:** The deliberate comparison of “two complete systems built on one model” is acceptable, but metadata access remains incompletely specified and “Tools alone raise rank agreement” still implies an isolated effect.
5. **Partly resolved — accuracy tolerance:** The highlighted question now permits 0.02 skill loss, but the abstract still promises “without losing accuracy.”
6. **Partly resolved — normalization and comparability:** Rerunning methods and treating Figure 3 as historical context address comparability, but the out-of-range policy is missing and Figure 5 still says “so results stay comparable.”
7. **Resolved — expert-pipeline superiority:** Superiority now requires a positive difference interval and is explicitly limited to this particular pipeline.
8. **Resolved — subordinate hypotheses:** C–E are exploratory, and D–E now specify rank-agreement comparisons.
9. **Resolved — untested benefits:** The motivation now describes a test and acknowledges that score agreement cannot establish correct feature measurement.
10. **Resolved — cost as another research question:** The economic criteria have been removed from the question and interpretation.
11. **Partly resolved — concision:** The sections are shorter, but “Stages C to E use prompt optimization…” still repeats the table as an implementation catalogue, and 18 references remain.
12. **Partly resolved — terminology:** Most tool descriptions now have useful glosses, but Figure 3 still says “no training,” and its SVG description calls the pretrained model “untrained.”
13. **Resolved — ankle direction:** The running example now specifies plantar flexion and explains its direction.
14. **Resolved — participant accounting:** The text explicitly distinguishes 180 recorded participants from 171 with usable video.
15. **Resolved — checklist style and personification:** The flagged passages have been replaced with connected prose and descriptions of inspectable outputs.

The new or still-serious problems, in severity order, are:

1. **High — The protocol appears to expose reference answers to prediction methods.**  
   **Quote:** “Every method reads one ledger … recording … the reference values.”  
   **Why:** As written, methods receive the answers for evaluation cases. Training-only normalization does not prevent this separate source of leakage; the intended reader may instead be the evaluator, but that distinction is essential.  
   **Fix:** Write: “The evaluator maintains a shared ledger containing reference values and exclusions; prediction methods receive only the permitted inputs, without held-out reference values.” ([§3.2](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v2_measure-or-guess-evaluation.md:61))

2. **High — A constant predictor can satisfy the success rule.**  
   **Quote:** “the difference in rank agreement … lies above zero” and “the skill difference is above −0.02”; elsewhere, “measures that a guess cannot satisfy.”  
   **Why:** A constant agent receives rank agreement 0 under the stated convention. If the direct predictor has negative rank agreement and worse error, that constant agent can satisfy both conditions while distinguishing nobody. The decision rule therefore does not establish the proposal’s central measuring-versus-guessing claim.  
   **Fix:** Also require the agent’s own rank agreement to be demonstrably above zero, and describe the safeguard as excluding a **constant** predictor rather than every possible guess. ([Decision](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v2_measure-or-guess-evaluation.md:21))

3. **High — Compression remains a causal explanation without supporting evidence.**  
   **Quote:** “its small departures from the average are dominated by noise” and “advantage … comes mostly from compression.”  
   **Why:** The pilot measured neither ranking nor compression, as the document itself acknowledges. Moreover, the defined slope combines association with prediction spread: unrelated predictions can have slope zero without being compressed. Figure 1 correctly shows that compression alone preserves ordering, but the surrounding prose still assumes the missing mechanism.  
   **Fix:** Present compression and noisy ordering as separate possibilities to investigate; remove the causal claim in A. Describe slope as a descriptive diagnostic, and, if compression remains an explicit hypothesis, assess prediction spread directly. ([Rationale and hypotheses](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v2_measure-or-guess-evaluation.md:13))

4. **Medium — The interpretation exceeds the deliberately chosen whole-system comparison.**  
   **Quote:** “The agent also receives the task’s feature definitions”; “Tools alone raise rank agreement”; “computing features with tools carries person-specific information that direct prediction misses.”  
   **Why:** Comparing complete systems is a valid design choice, but an advantage cannot then be attributed specifically to tool measurement. Task knowledge, metadata, and training changes also differ; height and camera parameters are substantive reconstruction inputs, as the [OpenCap Monocular methods](https://arxiv.org/html/2603.24733v1#S2.SS2.SSS2) explain.  
   **Fix:** Explicitly list each system’s permitted inputs and narrow the conclusion to better performance by the complete agent system. Replace “Tools alone” with “The agent without task-specific training”; no redesign is necessary. ([Setting](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v2_measure-or-guess-evaluation.md:11))

5. **Medium — The revised normalization remains incomplete, and Figure 5 retains the superseded claim.**  
   **Quote:** “rescaling endpoints … come from training participants only, which changes the scale slightly”; Figure 5: “The same 43 people … so results stay comparable.”  
   **Why:** Training extrema do not necessarily bound held-out values, and the change need not be slight. Clipping versus retaining out-of-range values can affect errors and rankings. Identical participants alone also do not establish comparability under changed normalization.  
   **Fix:** State that predictions and references use identical training-derived endpoints, specify whether out-of-range values are retained or clipped, and remove “slightly.” Update the [Figure 5 sentence](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_split_v2.svg:187) to distinguish historical pilot results from uniformly rescored comparisons.

6. **Medium — Three formulations describe different accuracy guarantees.**  
   **Quote:** “without losing accuracy”; “within 0.02 of that model’s”; “the lower end … is above −0.02.”  
   **Why:** These respectively imply no loss, potentially a symmetric distance, and a one-sided tolerance for loss. Also, the decision concerns task-averaged skill, so the single-task error example is an illustration of scale, not a bound on deterioration in each task.  
   **Fix:** Use “with task-averaged skill no more than 0.02 lower” consistently. Label the numerical example illustrative and briefly explain why that trade-off is acceptable. ([Abstract and question](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v2_measure-or-guess-evaluation.md:5))

7. **Medium — Run-allocation and replication planning remain, alongside repeated implementation detail.**  
   **Quote:** “Claims about a training method also resample training runs”; “every stage here is compared at a matched number of agent runs”; “Stages C to E use prompt optimization … harness search … LoRA … GRPO.”  
   **Why:** The first two passages retain replication and allocation planning explicitly excluded by the brief. The optimizer catalogue repeats the exploratory stages and adds terminology and citations without sharpening the highlighted question.  
   **Fix:** Retain the participant-level uncertainty principle, remove run-allocation and replication instructions, and summarize the exploratory stages once in plain language. Prune references used only by the removed implementation catalogue. ([Approach](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v2_measure-or-guess-evaluation.md:53), [analysis and related work](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v2_measure-or-guess-evaluation.md:73))

The document is not ready: the revision improves focus, but the answer-access wording, constant-predictor loophole, and unsupported compression explanation still undermine its central claim. These can be corrected within this version’s existing evaluation-centered design, followed by a short consistency and concision pass.