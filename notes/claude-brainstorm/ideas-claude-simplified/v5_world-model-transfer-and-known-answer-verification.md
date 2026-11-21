# Transfer of Checked Measurements Across Balance Tasks

## Research question

> **Does checking feature computations against known examples help a single-camera agent generalize biomechanical measurements to balance tasks excluded from model training?**

A procedure can fit familiar recordings without capturing the quantity it claims to measure. This proposal asks whether testing a computation on other examples encourages reusable measurement procedures, and whether that benefit survives a change in task.

## Scientific rationale

StaBLE defines features across standing, reaching and walking tasks, providing a setting in which participant generalization and task transfer can be studied separately. [Heigold et al. (2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13621976/).

The hypothesis is that a known-answer check discourages computations tailored to a single recording. A feature function must reproduce reference values on other examples spanning that feature's variation. This extends the question of reward granularity studied in ToolRL to the transfer of physical computations. [Qian et al. (2025)](https://arxiv.org/abs/2504.13958). An alternative is that the agent simply adapts to the probe examples, improving check performance without learning a procedure that transfers.

## Study

Train two otherwise identical agents using per-feature reference rewards, with and without a known-answer check. Both estimate features from single-camera tool outputs and submit the computations used. The checked condition penalizes functions that fail on probe recordings from training participants. Keep the initial demonstrations, tools, training exposure and timing supervision identical, with rewards on a common range.

Exclude Semi-Tandem, Gait-Backwards and Functional Reach from all model fitting, including demonstration generation and any learned tool selection. Evaluate the frozen agents on both familiar and excluded tasks in new participants. Supply the excluded tasks' feature definitions to both agents. A separate set of development participants supplies labeled calibration examples for normalization and auditing on those tasks; these examples cannot update the agent or select its predictions. The claim is therefore transfer with labeled evaluation support.

The primary comparison is feature error on excluded tasks, reported by task and summarized using fixed calibration scales with equal task weights. Compare each trained agent with its shared starting model to distinguish transferred learning from competence already present before training. Errors on familiar tasks and within-task score rankings provide context, without substituting for the transfer outcome.

Keep the probes used to reward training separate from audit examples used to assess the final computations. Include constant outputs, recording lookups and functions driven by irrelevant signals in the audit. Report false acceptance of these shortcuts and false rejection of valid reference implementations. Features whose probe values are indistinguishable cannot provide evidence against constant guessing.

At evaluation, compute scores from submitted features without replacing values because they failed a check. Use identical training-derived fallbacks for missing predictions, with separate calibration baselines for excluded tasks, and report failures. Repeat error comparisons on cases completed by both agents. Primary references must be measured and unflagged. Keep evaluation participants out of every fitted component and calibration set; acknowledge retrospective dataset reuse. Uncertainty includes participant and training-run variation.

## Interpretation

Lower error on excluded tasks would support transfer beyond the tasks used to optimize the agent. Better probe performance without better transfer would support adaptation to the check rather than reusable measurement knowledge. A gain confined to familiar tasks would limit the conclusion to participant generalization.

Task definitions and labeled calibration examples provide domain knowledge, so this study cannot establish transfer to entirely unspecified tasks. Feature types may overlap with training; the transfer claim concerns new tasks, not necessarily new physical quantities. Agreement with three-camera estimates also leaves shared reconstruction errors unresolved.
