1. **High — research-question. The main comparison changes timing supervision as well as feature credit.**  
   **Quote:** “minus 0.1 times the timing error of the agent's start and end marks in seconds”; the comparator is “minus the absolute error of the task score.”  
   **Problem:** Better temporal boundaries could improve rankings independently of feature-level rewards or verification. S1 isolates the check, but the primary comparison still measures a broader intervention than the question names.  
   **Fix:** Give both primary arms the same timing term and identical initialization, tools and evaluation rules. Alternatively, explicitly describe the primary intervention as the combined feature, verification and timing reward.

2. **High — overclaim. Passing known-answer probes does not identify measurement code.**  
   **Quote:** “code that measures the defined feature recovers those values and their order, while code that returns typical values, reads the wrong body part or uses appearance cues such as the person's height in pixels does not.”  
   **Problem:** An appearance-based function could match four probes when appearance correlates with their answers. Conversely, correct feature code can disagree because its tool outputs are noisy. When all probe holds equal five seconds, a constant also passes the stated exception. The later limitation does not repair this categorical rationale.  
   **Fix:** Replace with: “Agreement on reference probes can reject some shortcuts; we test whether this improves performance on unseen participants.” Treat constant-valued probe sets as uninformative about constant guessing, and evaluate checker generalization on separate probes.

3. **High — research-question. The primary outcome cannot establish the advertised measurement mechanism.**  
   **Quotes:** “The primary measure is **rank agreement**”; “known answers are a practical way to reward measuring.”  
   **Problem:** Shrinking predictions toward their mean preserves Spearman correlation whenever their order stays unchanged. Age-based predictions can also rank participants successfully. The skill safeguard permits these behaviors if their absolute error remains acceptable. Thus, primary success need not resolve either motivating shortcut.  
   **Fix:** Keep ranking as the primary question, but describe success as improved ordering against the reference. Reserve claims about measurement for supporting results from the existing appearance controls, movement interventions and calibration assessment.

4. **Medium — research-question. The primary decision is incompletely specified.**  
   **Quotes:** “averaged over tasks”; “one minus a method's error divided by the error of predicting the task average.”  
   **Problem:** It is unclear whether the primary average includes the three transfer tasks. “Error” also leaves open the loss, aggregation order and source of the task average; averaging task-specific skill ratios differs from taking a ratio of task-averaged errors.  
   **Fix:** State, for example: “The primary outcome averages within-task Spearman correlations over tasks used in training; transfer tasks are assessed separately. Skill is one minus task-averaged MAE divided by the corresponding MAE of each task’s training-mean predictor.” Explain what deterioration the −0.02 margin permits.

5. **Medium — research-question. The time-scaling comparison excludes features but evaluates whole scores.**  
   **Quotes:** “features that are or would become capped … are excluded”; “each method's change in task score.”  
   **Problem:** A direct score predictor does not expose feature contributions that can be removed. Excluding a capped feature from the reference calculation therefore creates a different target from the predictor’s full task score.  
   **Fix:** Compute the expected change in the complete task score, retaining all features and applying the cap explicitly—for example, transformed hold time is `min(1.25 × original hold time, 5 seconds)`. Apply identical scoring and eligibility rules to both methods.

6. **Medium — figure-text-mismatch. The overview omits reference information used by the verifier at evaluation.**  
   **Figure:** [pipeline_v5_v6.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/pipeline_v5_v6.svg).  
   **Quotes:** “TRAINING ONLY · 3-CAMERA REFERENCE”; “Sealed participants and held-out tasks are opened once, at the end.”  
   **Problem:** The verifier continues to use development-video reference answers at evaluation, including task-specific probes for held-out tasks. This is permissible support information, but the diagram obscures it and can suggest transfer without task-specific reference support.  
   **Fix:** Draw a separate frozen development-probe input to the verifier. State: “The current participant’s reference is unavailable during inference; fixed development references remain available to the verifier, including for transfer tasks.”

7. **Medium — error. The scoring explanation omits reversal of features where smaller values are better.**  
   **Quote:** “Each feature is rescaled to the range 0 to 1 using the lowest and highest values in the data, the rescaled features are averaged into a **task score**.”  
   **Problem:** The rise-to-toes illustration covers features where larger values are better. StaBLE also reverses features such as sway, where smaller values indicate better performance; its scoring code explicitly implements both directions. [StaBLE scoring code](https://raw.githubusercontent.com/stanfordnmbl/stable-analysis/main/compute_scores.ipynb)  
   **Fix:** Add: “Features are oriented so that higher normalized values always indicate better performance; quantities such as sway are reverse-scaled before averaging.”

8. **Medium — figure-text-mismatch. The prose and Figure 4 define different acceptance ranges.**  
   **Quote:** “the value lies within the training range and physical limits.”  
   **Figure:** [fig_check_v5.svg](/Users/theodoremui/dev/bioharness/docs/ideas-claude-explained/figures/fig_check_v5.svg) instead says “training range widened by half its width on each side.”  
   **Problem:** These rules accept different predictions, particularly unusually strong or weak performances. That changes verification, fallback scores and rewards.  
   **Fix:** Choose one rule and use it throughout. If the figure is authoritative, replace the prose with “within physical limits and the training range expanded by half its width at each end.”

9. **Medium — clarity. Probe-specific start and end marks are unspecified.**  
   **Quotes:** “a function of tool outputs and the agent's own start and end marks”; “run on four development videos.”  
   **Problem:** Different videos require different temporal boundaries. Reusing the current video’s marks can reject correct code; supplying reference marks tests computation under privileged segmentation; generating new marks tests an additional agent behavior. These interpretations give the check different meanings.  
   **Fix:** Specify whose marks are supplied for each probe. For example: “Each probe uses its own boundaries predicted from single-camera input; boundary accuracy is assessed separately from feature computation.”

10. **Medium — overclaim. Two literature claims exceed their supporting evidence.**  
    **Quotes:** “Outcome-only reinforcement learning makes the first trap worse”; “tool-using agents trained this way learn to skip verification.”  
    **Problem:** Xu studies reduced dependence on temporal video content, which does not establish increased compression toward average numerical predictions. Thaman evaluates existing models and explicitly describes its post-training comparison as observational. [Xu](https://arxiv.org/html/2606.22043v1), [Thaman, limitations](https://arxiv.org/html/2605.02964v1#S8)  
    **Fix:** Use: “Outcome-only training has produced temporal shortcuts in video question answering.” Separately: “A tool-agent benchmark observed verification-skipping and other exploits, with rates associated with post-training differences.”

11. **Medium — structure. Secondary components compete with the primary question.**  
    **Quotes:** “Whether the teacher's access to the reference helps the student”; “Whether the learned skill transfers to new tasks”; “A model of what each tool will deliver.”  
    **Problem:** The abstract, seven secondary comparisons and dedicated tool-outcome section give several contributions similar prominence. Readers must infer which components define the primary intervention and which are shared infrastructure or follow-up tests.  
    **Fix:** Preserve this version’s components while stating their roles explicitly: teacher demonstrations initialize the matched agents; S1 isolates verification; transfer and movement tests examine generalization; tool-cost prediction is exploratory. Shorten §3.3 to one paragraph subordinate to that hierarchy.

12. **Medium — concision. Sample-allocation and training logistics remain throughout.**  
    **Quotes:** “60 are sealed”; “The other 111 form five development folds”; “100 sealed videos”; “the three reinforcement-learning arms use three seeds each.”  
    **Problem:** These are prospective allocation and replication details, which the requested snapshot explicitly excludes. Figures 3 and 6 repeat them; Figure 3 additionally specifies “8 rollouts per video.”  
    **Fix:** Remove these planned counts from prose and figures. Retain participant-disjoint evaluation, training-only calibration, held-out task identities and uncertainty across participants and training runs. Historical dataset and pilot counts can remain as evidence.

13. **Medium — concision. Repeated explanations and the broad literature survey dilute the idea.**  
    **Quotes:** “A **known-answer check** tests the computation itself”; “The harness checks it three ways”; “World models for agents predict the outcome of an action before it is taken.”  
    **Problem:** The check is explained in the rationale, §3.1, Figure 4 and the limitations. The related-work paragraph then surveys several neighboring topics already introduced elsewhere. This spends snapshot space repeatedly establishing background.  
    **Fix:** Keep the rationale’s prediction, let Figure 4 carry the procedural example, and restrict §3.1 to details the figure cannot convey. Replace the broad related-work survey with two sentences identifying the closest reward-learning work and this proposal’s specific difference.

14. **Medium — undefined-term. Essential ML vocabulary lacks first-use glosses.**  
    **Quotes:** “reinforcement learning,” “training trajectories,” “warm start,” “tool-feature regressor”; Figure 3 adds “SFT” and “GRPO.”  
    **Problem:** These terms appear in the central question, comparisons or overview before an advanced high-school reader receives an explanation.  
    **Fix:** Briefly gloss essential terms: reinforcement learning—training through rewards; trajectory—one sequence of tool calls and a submission; warm start—initial training on demonstrations; tool-feature regressor—a model predicting scores from tool-derived measurements. Remove incidental algorithm acronyms from the overview.

15. **Low — style. Contrastive phrasing and unexplained chronology add editorial residue.**  
    **Quotes:** “An interval that includes zero is inconclusive, not a refutation”; “The sealed participants are a retrospective re-split, not newly recorded people”; “Earlier checks.”  
    **Problem:** The first two use the flagged antithesis pattern; the second repeats an existing caveat. “Earlier” implies a development history that the snapshot has not introduced.  
    **Fix:** Write “An interval containing zero leaves the comparison inconclusive,” delete the repeated re-split sentence from §5, and replace “Earlier checks” with “Replay and input-dependence checks.”

The proposal has a testable primary comparison, but its reward contrast and verification claims currently support a narrower conclusion than “learning to measure.” Matching timing supervision, aligning the figures and scoring definitions, and cutting logistical and repeated exposition would make it a stronger research snapshot.