Nine prior findings are resolved and six are partly resolved. I checked the [revised proposal](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/v5_world-model-transfer-and-known-answer-verification.md) and all six referenced figures; no files were changed.

Statuses below follow the earlier review’s numbering.

1. **Resolved — timing confound:** Both primary arms now share initialization, tools, timing penalties and evaluation rules.
2. **Partly resolved — verification overclaim:** The rationale acknowledges shortcuts and constant-valued probes, but §5 still says the check “certifies the computation.”
3. **Resolved — primary outcome versus mechanism:** The primary question now concerns ordering accuracy; movement and appearance tests separately assess measurement behavior.
4. **Partly resolved — decision specification:** Task scope, MAE and aggregation are specified; the training-median baseline and taskwise skill averaging are acceptable alternatives, but “above −0.02” remains unexplained.
5. **Resolved — time-scaling target:** Both methods are compared on complete task-score changes, with duration caps explicitly applied.
6. **Partly resolved — evaluation references:** The caption explains continuing probe access, but Figure 3 still labels the reference “TRAINING ONLY · 3-CAMERA REFERENCE” and lacks a separate evaluation-time probe input.
7. **Resolved — feature direction:** The scoring explanation explicitly reverses features for which lower values indicate better performance.
8. **Resolved — acceptance ranges:** Prose and Figure 4 both use the training range widened by half its width at each end, subject to physical limits.
9. **Partly resolved — probe boundaries:** Using “the expert pipeline’s start and end times” is an acceptable design choice, but §5 still describes verification “given the agent’s own marks.”
10. **Resolved — literature overclaims:** The narrowed temporal-shortcut claim matches [Xu’s study](https://arxiv.org/html/2606.22043v1), and the unsupported Thaman training claim is removed.
11. **Resolved — competing components:** Demonstrations are explicitly shared initialization, verification and rewards are the intervention, and the tool-outcome model is exploratory.
12. **Partly resolved — logistics:** Several counts disappeared, but Figure 3 retains “Sealed · 60 people” and “Development · 111 people in 5 folds”; prose also retains the five-fold allocation.
13. **Resolved — repetition and literature breadth:** Procedural exposition is substantially shorter, and related work is reduced to two sentences while retaining this version’s components.
14. **Partly resolved — vocabulary:** Reinforcement learning, trajectories and warm start receive explanations, and SFT/GRPO disappear; “tool-feature regressor” remains undefined.
15. **Resolved — editorial residue:** The flagged inconclusiveness wording, repeated re-split caveat and unexplained “Earlier checks” wording are removed.

The new or still-serious problems are:

1. **High — the reward can favor malformed answers.**  
   **Quote:** “a feature that fails the check … costs an extra 0.5”; both arms “give −2 to an unparseable answer” (§3.2). Figure 3 confirms a “penalty per unverified feature.”  
   **Why:** For a task with five failed features, a well-formed submission receives at most −2.5 before feature-error and timing penalties. An unparseable answer therefore earns a better reward. This creates an avoidable shortcut in a proposal designed to prevent shortcuts.  
   **Fix:** Bound the reward components and set the unparseable-answer reward strictly below the lowest valid-submission reward. Consider averaging failure penalties across features so their weight does not depend on the task’s feature count.

2. **High — the limitations still claim more verification than the procedure provides.**  
   **Quote:** “the check certifies the computation given the agent’s own marks” (§5), versus probes using “the expert pipeline’s start and end times” (§3.1).  
   **Why:** Replay establishes consistency with submitted evidence; finite probe agreement does not certify correctness on the current participant. Furthermore, the known-answer tests use pipeline boundaries, so they do not test feature computation under the agent’s predicted boundaries. This preserves the substance of prior findings 2 and 9.  
   **Fix:** Replace the sentence with: “Replay checks consistency on the current video; known-answer probes test agreement on development videos using pipeline boundaries. Timing accuracy is assessed separately.” Assess checker generalization on probes unused for reward feedback.

3. **Medium — the constant-valued exception conflicts with the universal shortcut-rejection requirement.**  
   **Quote:** “for such features the check rests on replay and range,” followed by “a fixed suite of deliberate shortcut programs must fail the check” (§3.1); Figure 4 explicitly includes “typical values.”  
   **Why:** A program returning five seconds can pass replay and range for the capped hold-time example. The blanket requirement needs to distinguish informative probe sets from the acknowledged exception.  
   **Fix:** Restrict the constant-rejection requirement to probes with meaningfully different reference values. Describe all-equal cases consistently as receiving replay-and-range checks only, including in Figure 4.

4. **Medium — Figure 3 still obscures reference support during evaluation.**  
   **Quote:** “TRAINING ONLY · 3-CAMERA REFERENCE” in [Figure 3](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/pipeline_v5_v6.svg:160), versus “Development probe answers … remain available to the check at evaluation” in its caption.  
   **Why:** The caption fixes the explanation, but the diagram still omits a substantive input to the deployed verifier, including support for transfer tasks. A reader following the figure alone gets an incomplete account of the method.  
   **Fix:** Add a separate frozen development-reference input to the verifier, available during training and evaluation. Reserve the training-only label for the current training participant’s reference.

5. **Medium — prospective allocation details still violate the requested snapshot format.**  
   **Quote:** “Sealed · 60 people,” “Development · 111 people in 5 folds” and “60 people, all eligible tasks” in Figure 3; “Development participants form five folds” in §4.  
   **Why:** These are study-allocation plans, not historical evidence or essential scientific distinctions. Removing them from some locations has left the proposal inconsistently simplified.  
   **Fix:** Remove the prospective counts and enumerated fold boxes throughout. Retain participant-disjoint development/evaluation, training-only calibration, task exclusions and uncertainty across participants and training runs; retain historical dataset and pilot counts.

6. **Medium — the rationale states an untested mechanism as fact.**  
   **Quote:** “Offsetting errors are tuned to the training videos and become person-specific errors on new people, which scramble the ordering” (§1).  
   **Why:** Cancellation need not fail on new participants: equal-and-opposite errors could persist and preserve task scores. The proposed benefit is a plausible hypothesis, not a necessary consequence of final-score rewards.  
   **Fix:** Write: “We hypothesize that feature-error cancellations learned on training participants will often fail on unseen participants, reducing rank agreement.”

7. **Medium — the central acceptance criterion remains undefined.**  
   **Quote:** Probe outputs “must come close to the known values and order them correctly” (§3.1); Figure 4 likewise says “land close.”  
   **Why:** “Close” determines rewards, feature replacement and final scores. Without even a rule for choosing the tolerance, readers cannot distinguish a meaningful check from one that rejects ordinary tool noise or accepts substantial errors.  
   **Fix:** Briefly specify a fixed, feature-specific absolute-error tolerance, calibrated on development data and frozen before evaluation. Require ordering only where reference differences exceed the relevant tolerance; detailed numerical settings need not occupy this snapshot.

8. **Medium — central comparisons and figure outcomes still exceed the stated audience’s vocabulary.**  
   **Quote:** “tool-feature regressor” in S3–S5; “Calibration slope” and “Verified coverage” in Figure 3; “Holm’s procedure” and “bootstrap resample” in the analysis.  
   **Why:** These terms identify comparators, outcomes and evidence standards, yet an advanced high-school reader cannot infer their meaning from the document. The new introductory glosses do not reach these remaining terms.  
   **Fix:** Add short explanations where needed: a model predicting scores from tool measurements; whether predicted differences are too compressed or exaggerated; the share of features passing checks; correction for multiple comparisons; and resampling participants to estimate uncertainty. Remove incidental labels that do not help explain the question.

The revision substantially improves the research question, but the document is not ready yet. The reward loophole, verification contradictions, incomplete figure updates and remaining logistics need correction before it serves as a reliable, concise proposal snapshot.