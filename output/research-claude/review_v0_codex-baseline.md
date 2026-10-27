# Review of v0: "Learning What to Preserve in Biomechanical Agents" (Codex draft)

Reviewed file: `output/research-codex/biomechanical_agent_proposal.md`
Reviewer stance: ICML 2027 area chair, Application-Driven ML track, with the lab's own documents in hand (see `00_source_notes.md`).

## Rubric used for every version

Each dimension is scored from 1 to 10. The overall score is the weighted mean. The weights reflect what decides an ICML outcome for an application-driven paper: the machine-learning contribution and its evidence count most, while presentation still matters because reviewers outside biomechanics must follow the argument.

| # | Dimension | Weight | What a 10 looks like |
|---|---|---|---|
| D1 | ICML significance and relevance | 15% | The paper teaches the ML community something general about training or evaluating agents, with biomechanics as a demanding test bed |
| D2 | Methodological novelty | 15% | A clearly stated new idea that prior work does not already contain, with a precise mechanism |
| D3 | Research question (SMART) | 10% | One primary question that is specific, measurable, achievable, relevant and time-bound, plus a small number of secondary ones |
| D4 | Technical soundness | 10% | Every component is defined well enough to implement, and the parts fit together without hidden contradictions |
| D5 | Experimental design and baselines | 10% | Strong, budget-matched baselines, ablations that isolate each claim, and controls for the obvious alternative explanations |
| D6 | Statistical rigor and leakage control | 10% | Correct unit of analysis, participant-level splits, a sealed test set, pre-registered contrasts, power analysis, and honest handling of failures |
| D7 | Feasibility and fit to data and lab assets | 10% | Uses data and tools that exist, with compute and calendar time that add up |
| D8 | Clarity and first-principles accessibility | 10% | A newcomer can follow every concept from scratch without a glossary hunt |
| D9 | Story arc and hypothesis-driven iteration | 5% | A visible chain of hypothesis, test, result and next decision, repeated across the project |
| D10 | Writing naturalness | 5% | Reads like a careful human researcher; free of the stylistic tics listed in the brief |

Score bands used for the ICML readiness call: below 5 is a likely reject, 5 to 6 a weak reject, 6 to 7 borderline, 7 to 8 a weak accept, above 8 an accept.

## Scores for v0

| Dimension | Score | Rationale |
|---|---|---|
| D1 Significance | 4 | The contribution (learning reusable "evidence contracts") is framed around a single narrow gait statistic. The ML lesson, that a harness should keep the information a later step needs, is closer to software engineering than to learning. |
| D2 Novelty | 4 | The contracts resemble typed interfaces and specification checking from program synthesis, which the draft itself cites. The "learning" part (estimating which requirements help) is a bandit-style ranking that is never specified. |
| D3 Research question | 6 | Specific and time-bound (12 weeks), with a named outcome. Measurability depends on a tolerance that is never fixed, and relevance to the lab's aims is weak. |
| D4 Soundness | 4 | The optimizer, the operation library and the "learned ranking" are described at the level of intentions. No loss, reward or search procedure is defined. |
| D5 Experimental design | 6 | Good instincts: matched budgets against Meta-Harness, ablations of each component, an expert-workflow control, and withheld combinations of operations as a transfer test. |
| D6 Statistics and leakage | 7 | Participant-level grouping, a cluster bootstrap over people, five search runs reported separately, and a cap on validation reuse. Power is acknowledged but not computed. |
| D7 Feasibility and fit | 3 | Depends on walking videos synchronized with an instrumented walkway, which the lab documents do not mention. It ignores the StaBLE dataset, the existing baselines (SFT Qwen, OpenCap Monocular) and the tool inventory the lab already has. |
| D8 Clarity | 5 | Terms are defined, but the central idea is abstract and hard to picture. The two borrowed figures show other people's systems rather than this project's pipeline. |
| D9 Story arc | 3 | No sequence of hypotheses. There is no fine-tuning, no reinforcement learning, no model of the world, and no visible path from one result to the next decision. |
| D10 Writing | 6 | Mostly plain and careful, but compressed to the point of being cryptic in places ("A repair must use evidence available under the original recording conditions"). |

**Weighted overall: 4.75 / 10.** ICML readiness: likely reject in its current form.

## What v0 gets right and should be kept

1. **Matched-budget comparison with harness code search.** The idea that any new method must beat Meta-Harness-style search given the same models, information and compute is the right standard, and the recent evidence that evolved harnesses often fail to beat simple test-time scaling ([Wang et al., 2026](https://arxiv.org/abs/2607.12227)) makes it essential.
2. **Participant-level grouping and a participant bootstrap.** These carry over unchanged.
3. **Separating preservation from physical accuracy.** The distinction between "the pipeline kept the detector's output intact" and "the detector's output matches an independent reference" is useful. In later versions it becomes the distinction between *faithfulness* (the reported feature can be recomputed from the evidence the agent cites) and *accuracy* (the feature matches the three-camera reference).
4. **Charging construction cost to the search budget.** Later versions keep this accounting.

## Critiques

1. **The proposal answers a question the lab is not asking.** The lab's own framing (lab meeting, slides 15 and 50) is whether a VLM can learn to choose and use analysis tools to conduct the StaBLE assessment from one camera. The planning note asks for a hierarchy: reproduce features, then task scores, then the ranking that the StaBLE paper derives. v0 instead studies stride-duration variability in gait, a single derived statistic, with a fixed language model and no VLM at all.
2. **The central problem may not exist at a scale that matters.** v0 concedes that "full retention may prove sufficient and inexpensive." If keeping all detector outputs solves the problem, the paper's contribution disappears. An ICML reviewer will ask why storage is not simply cheap.
3. **No learning in the learning method.** Evidence contracts are written from researcher-supplied templates; the only adaptive piece is ranking which requirements help. There is no gradient-based training, no policy, and no reward, which leaves the paper outside the ML methods that the brief asks about (fine-tuning, prompt optimization, reinforcement learning, harness evolution, world models).
4. **The data assumption is unverified.** Independent foot-contact measurements on a common clock are needed for the primary outcome. None of the three source documents mention such data. The StaBLE dataset, by contrast, already provides a three-camera reference for every one of its 76 features.
5. **The existing results are ignored.** The lab has already shown that a frozen Qwen3-VL-8B scores worse than predicting each task's training mean (MAE 0.238 versus 0.120), that supervised fine-tuning helps (0.100), and that the reconstruct-and-measure route returns valid scores for only 567 of 729 test cases. These results are the strongest motivation for an agent and they appear nowhere.
6. **The tolerance that defines success is left open.** "Within a tolerance fixed before comparing methods" is good practice, but without even a provisional value the reader cannot judge whether the question is answerable with the available participants.
7. **Figures do not show the proposal.** Both figures are adapted from other papers. A reader finishes without a picture of this project's training pipeline.

## Concrete suggestions for v1

1. Re-anchor the proposal on the StaBLE dataset and the monocular setting that the lab is already working on, and adopt the planning note's hierarchy (features, then task scores, then the overall score) as the evaluation structure.
2. Make the agent a tool-calling VLM and keep the existing pilot results as the baseline ladder.
3. Keep the matched-budget comparison with harness search, and add the other levers the brief names: prompt optimization, supervised fine-tuning and reinforcement learning.
4. Replace the stride-variability outcome with the StaBLE task score so the comparison with the lab's baselines is direct.
5. Keep the participant-level split and bootstrap, and keep the evidence idea in a smaller form: the agent reports each feature together with the tool output it came from.
6. Explain from first principles what a VLM, a tool call and a harness are, and why the agent route might beat both existing routes.

## Codex adversarial review of v0

See `codex_adversarial_review_v0.md` for the verbatim output and the disposition table at the end of this file.

### Disposition of Codex findings on v0

| Codex finding | Severity | How the Claude series responds |
|---|---|---|
| Averaging five searches before resampling participants ignores search-to-search uncertainty | high | Adopted. From v2 onward, claims about a *training method* resample both seeds and participants (a crossed bootstrap); claims about a single frozen agent resample participants only, and each result states which estimand it uses. |
| The foot-contact reference dataset is not established | high | Adopted by changing datasets. From v1 onward the reference is the three-camera StaBLE reconstruction, which exists for every participant and task. |
| The success rule can pass while an expert-written program dominates | high | Adopted. From v2 onward the decision rule requires the agent to match or beat a fixed expert pipeline that uses the same tools, with total cost reported. |
| The workflow holdout is not enforceable | high | Carried into the task-transfer design (v5 onward): held-out tasks are fixed in the ledger before development, and their definitions are never shown during training. |
| The learned component is under-specified | medium | Adopted. v3 onward defines rewards and training loops in pseudocode-level detail. |
