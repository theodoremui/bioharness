# Proposal 08: final independent review

Target: `docs/idea-summaries/08-blind-analysis-for-agents.md` (5,739 prose words by `audit_doc.py`; 8 figures; 35 references; audit reports no dashes, banned words or staccato runs). Figures rendered to `output/idea-summaries-build/png/08/` and inspected. Line numbers refer to the current file. Points already settled in `08-resolutions.md` are not re-raised unless noted.

Overall judgement: the science is careful and most of the earlier high-severity problems are fixed. The main barrier now is reading load. One pass leaves a reader able to state H1, but not the decisive experiment or the falsifier, because (a) route and recoverability are run together in the framing and pulled apart only in Proposition 2's last sentence, (b) the hypotheses have no map to experiments and primary outcomes, and (c) about a dozen terms and symbols are used before they are defined, with seven symbol clashes. Two new soundness problems also need attention. The decision primary outcome (P4) has no power calculation and looks badly underpowered on 43 sealed people. The power arithmetic for P1 and P2 depends on a variance-component convention that the E1 model contradicts.

---

## 1. The five changes that would most improve readability and conceptual clarity

### 1.1 Rewrite the box (and optionally the title) around one question, with every term defined

At 44 words, the current research question (line 3) asks three things in one sentence. The box uses "gated agent" and "0.2 SD" (line 9) before either is defined. The ML contribution (line 7) is a 54-word list that describes splicing inaccurately: splicing replays the recorded transcript (calls and outputs) into a report step told another referral, so "replays cached tool outputs across framings" misdescribes it. Proposed box (about 160 words):

> **Research question.** When a tool-using measurement agent is told the referral, how far does its number move, and does the referral act on the final report, which a clinician can undo by recalibrating, or on the analysis path, which can discard information? Does self-improvement shift it between these routes?
>
> **Why it matters.** The clinician already holds the referral, so a number pulled toward it counts the referral twice: an agent can lower its measurement error and still worsen the decision.
>
> **ML contribution.** Path splicing, which replays an agent's recorded tool calls into a report step told a different referral, to split the effect by route; a test of which route a downstream combiner can repair; a pre-registered prediction of where each optimizer puts learned context; and a blind-then-interpret harness scored on decision loss.
>
> **What would prove it wrong.** Framing effects within 0.2 between-person standard deviations (SD) for every agent whose blind reports track the reference; no effect carried by the tool calls; or a blind harness with worse decision loss than per-referral recalibration.

The falsifiers now map one-to-one onto P1, P2 and P4. The current title asks only H1. An optional alternative that names the contribution (12 words): "Can a clinician undo what the referral did to an agent's measurement?"

### 1.2 Separate *route* from *recoverability* everywhere, and define the direct route by intervention

The document has two orthogonal axes. Route is where the referral enters (path or report), and splicing measures it. Recoverability is whether the map from the blind report to the context-aware report is one-to-one or many-to-one, and recalibration measures it. The scripted controls (line 195) and Proposition 2's last sentence (line 120) treat these as crossed. Four places equate them, though:

- Box line 7: "repairable context use (a one-to-one shift of the number) from irreparable use (a many-to-one analysis path)".
- Line 23: "The organizing distinction is calibration bug or information bug: a shift ... can be undone ..., while a path change such as trimming can send different trials to one number".
- Key ideas line 37: "The first is usually one-to-one within a referral and the second can be many-to-one."
- H3 line 74: "the routes differ in repairability", tested by "direct-route agents" against "path-route agents", a classification that is never defined.

Line 37 also defines the direct route as acting "when the final number shifts". The final number shifts under both routes. The direct route is the effect with the transcript held fixed. Replace the "Routes and recalibration" paragraph with two paragraphs:

> **Route.** The referral can change the number in two places. Through the path route it changes which tool calls the agent makes (a trim, a filter cutoff, an exclusion), and so the outputs the report step reads. Through the direct route it changes what the report step outputs while the transcript is held fixed. Path splicing separates the two by experiment.
>
> **Recoverability.** Separately, the context-aware report can be a one-to-one function of the blind report within each referral (a shift or a shrinkage), in which case a combiner refitted per referral undoes it. It can also be many-to-one (a cap, or a trim that gives a 5 s hold and a 25 s hold the same reported value), in which case information about the person is lost. Either route can produce either map. Our hypothesis is that in real agents the path route is more often many-to-one, because trimming and exclusion discard data.

Then recast H3 as that association, with the route class pre-specified:

> **H3 (path effects are harder to repair).** Among gated agents, the decision penalty left after within-referral recalibration grows with the tool-calls-only indirect effect and is near zero for agents whose effect is direct. Test: residual penalty (recalibrated minus blind log loss on sealed people) against path share, with the four scripted controls as calibration points; an agent is "path-route" if its indirect effect excludes zero and its path share exceeds 0.5.

Line 23 can then shrink to one sentence that points to these definitions. The Proposition 2 sentence "Splicing measures how much ... by clipping" (line 120) becomes redundant and can go (see cut list).

### 1.3 Add a hypothesis-to-test map and name the decisive experiment

A reader meets six hypotheses, five experiments, four primary outcomes (P1 to P4, defined only at line 231), two propositions, three rewards and two extra domains, and nothing says which result decides the idea. Add a compact table at the end of Hypotheses, followed by a two-sentence decisive-test paragraph:

| Hypothesis | Experiment | Outcome | Falsified if |
|---|---|---|---|
| H1 framing moves the number | E1 | P1, TE | TE within the 0.2 SD margin for every gated agent |
| H2 part passes through the path | E2 | P2, indirect effect (tool calls only) | indirect effect within 0.1 SD |
| H3 path effects resist recalibration | E2 then E5 | secondary | no residual penalty for path-route agents while the lossy scripted controls show one |
| H4 accuracy reward learns shrinkage | E4 | secondary, $\hat\gamma$ against $\gamma_B$ | $\hat\gamma$ near 0 under reward (a) |
| H5 the optimizer sets the route | E4 | P3, indirect-effect gap | gap within the detectable 0.23 SD |
| H6 measure blind, then interpret | E5 | P4, log-loss difference | blind harness worse than within-referral recalibration |

> **The decisive test.** If only one experiment ran, it would be E2 followed by E5 on the same gated agents: splice each agent to measure how much of its framing effect passes through the tool calls, then ask whether per-referral recalibration removes its decision penalty. The idea survives if agents with path-mediated effects keep a penalty that recalibration cannot remove while the scripted controls behave as built. It fails if recalibration repairs every agent.

Add one signpost sentence at the top of Method ("Proposition 1 shows why a referral-shaped number harms the decision; Proposition 2 says which harm a combiner can repair; path splicing measures which route an agent uses; the remaining subsections define the secondary metrics, the harness and the loops") and one at the top of Experiments ("E1 tests H1, E2 and E3 locate the route, E4 tests self-improvement, E5 scores the remedies"). Together these cost about 150 words and supply the logical thread the document currently lacks.

### 1.4 Remove symbol clashes, state the sign convention, and define terms before use

Symbol clashes, each with a proposed fix:

| Symbol | Meaning 1 | Meaning 2 | Fix |
|---|---|---|---|
| $\pi$ | prior $\pi_H$ (line 86) | path policy $\pi(dz\mid v,f)$ (line 130) | call the policy $\kappa$ |
| $\mu$ | class mean $\mu_C$ (line 92) | splice cell $\mu_v(f_{\mathrm{path}},f_{\mathrm{rep}})$ (line 130) | call the cells $c(a,b)$ or the class means $\nu_C$ |
| $\beta_f$ | evidence slope (line 165) | framing fixed effect in the E1 model (line 233) | call the fixed effect $\theta_f$ |
| $V$ | variance $\tau^2+s^2$ (line 94) | set of clips (line 161) | write $\mathcal V$ for clips |
| $R$ | report $R_0,R_H$ (line 116) | runs per clip in the pseudocode | reuse $M_0$, $M_H$ in Proposition 2 |
| $X$ / $v$ | clip in Proposition 2 | clip everywhere else | use $v$ |
| $F$ / $H$ / $f$ / $h$ | framing $F$ (line 33) | referral $H$ (line 86) | one symbol $H$ with values $a$ (frail) and $b$ (athlete); drop $F$ |
| "pilot" | the lab pilot (earlier study) | the 20 "pilot people" of this study (line 189) | rename the 20 as "calibration people" |

Missing conventions:

- **Sign.** H2 says the indirect effect is "positive", but no direction is ever defined. Add to the path-splicing definition: "Effects are signed so that positive means toward the typical value of the referral named second ($b$, athlete, longer hold)."
- **Subscripts.** $\mathrm{DE}_a$ holds the path at $a$, while $\mathrm{IE}_b$ holds the report at $b$, so the subscripts index different stages. Say so in one clause in the text and in the Figure 5 caption.
- **Prior notation.** $\mathrm{logit}$, $\mathrm{LLR}$ ($\log f(m\mid 1)/f(m\mid 0)$), $(2H-1)$ (which needs $H=1$ to mean the high-risk referral) and "nats" (log loss in natural-log units) are all used without definition.

Terms used before definition. Box/H1 "gated agent" is defined only at line 165. "Sealed people" appears in H3 and H4 but is defined at line 187. "Bridge tasks" appears at line 86 and is defined at line 191. "Reward (a)" appears at line 169 and is defined at line 181. "E2 to E5" appears at line 165. "Orderings" and the "tool-calls-only splice" appear in H2 and are defined at lines 132 and 136. "Scripted controls" appear in H3 and are defined at line 195. "The API agent" appears in H1 and is named at line 195. Fix: add three one-sentence entries to Key ideas (**Development and sealed people**, **Measurement gate**, **Scripted controls**), and in each hypothesis point to the Method subsection that defines its test. Pull the gate out of the evidence-sensitivity paragraph into its own sentence.

### 1.5 Make the opening concrete with numbers, and start with the referral, not the dataset census

Problem paragraph 1 (line 13) opens with cohort statistics (180 people, 18 tasks, 71 diagnoses, fall-risk groups and elite balancers) before the reader knows why they matter. The 71 diagnoses matter only for the "true group" sentence at line 33. Start with the case: "A clinician refers a patient with the note 'suspected Parkinson's disease, recent falls'. A measurement agent receives that note, one smartphone clip of a single-leg stance trial and a set of tools ..." Then put StaBLE in one sentence as the source of such clips.

The double-counting paragraph (line 21) is abstract. Add the worked number from Proposition 1, which I recomputed: with $\Delta=2\tau$, $s=\tau$, $q=0.2$ and $\gamma^*=0.357$, a person whose blind hold time is typical of the low-risk class but who arrives with a frail referral gets a 60% posterior of high fall risk from the blind number and 75% from a number shrunk toward the referral at the error-minimizing amount. One sentence: "In the Gaussian model of Proposition 1, a person whose blind hold time is typical of low-risk people but who arrives with a frail referral is given a 60% chance of high fall risk from the blind number and 75% from the error-minimizing referral-shaped number." For the calibration-or-information paragraph (line 23), the "5 s and 25 s hold both reported as 5 s" example from 1.2 does the same job.

---

## 2. Paragraph-by-paragraph edits

**Title (line 1).** Fine as written; see 1.1 for an option that names the contribution.

**Box (lines 3 to 9).** See 1.1. RQ 44 words, ML contribution 54 words: split or replace. "routes context where" is awkward. "gated" and "SD" are undefined.

**Problem ¶1 (line 13, 47-word second sentence).** Reorder as in 1.5. Split the tool list into its own sentence. Say what RTMPose and OpenCap Monocular are in a clause ("2D keypoint detector", "single-video 3D kinematics"), and define OpenCap once ("smartphone markerless motion capture").

**Problem ¶2 (line 15, 48 words).** Split at the semicolon. "another treats the sway as a recovered wobble" gives agency to a transcript. Write "another keeps timing because balance recovers after the sway". The text says "collegiate gymnast, routine screening" but Figure 1 says "screening"; align them.

**Figure 1 caption (line 19).** "Every step on both paths is defensible, yet the hold times differ" is a "yet" pivot and does not say what to look at. Replace: "*Figure 1.* Illustrative, not a measured result. The clip and tools are the same; only the referral line differs. Compare the stopping rule in the two cards: stopping at the first sway shortens the hold."

**Problem ¶3 (line 21, 48 words).** Split after "evidence". Add the worked number (1.5). "Epidemiology names related problems review bias and incorporation bias" uses two undefined terms. Either define them in a clause ("an index test read with knowledge of the outcome it is meant to predict") or move the sentence to Known (see cut list). "yet clinical information generally improves the accuracy" is a pivot. Write "Clinical information also tends to make test reading more accurate [5], so our subject is the combination step: ...". QUADAS-2 needs a gloss ("a checklist for rating diagnostic-accuracy studies").

**Problem ¶4 (line 23, 48 words).** "The organizing distinction is calibration bug or information bug:" is slogan-like. Replace with one sentence that points to Key ideas and uses the seconds example from 1.2.

**Problem ¶5 (line 25).** Keep the retention example. Its first sentence (45 words) should split after "outlier rules". The literature sentence (46 words, "Frontier coding agents ... [8]") repeats the table and contains a "yet" pivot; cut it (see cut list). End with: "What remains open is which route a hypothesis takes through an analysis and what that route costs the decision."

**Harness (line 29).** Fine.

**Path, transcript and report (line 31, 43 words).** Split after the transcript definition. Add "the report step is the final model call that reads the transcript and outputs $M$", because "report step" is used everywhere and never defined.

**Framing and true group (line 33).** "A person's true group ... decides whether a framing is consistent, because the 71 diagnoses are self-reported" is hard to parse, and the consistency notion is not used again. Either cut it (see cut list) or say what it is for: "Because diagnoses are self-reported, we call a framing consistent when it matches the person's recorded age band, fall-risk group or elite status, and report effects separately for consistent and inconsistent framings."

**Combiner and log loss (line 35).** Define $p$ as "the combiner's probability of high fall risk" and give log loss its unit (nats). Good otherwise.

**Routes and recalibration (line 37).** Replace as in 1.2.

**Path splicing (line 39).** This is a fragment ("Replaying the cached transcript ..."); make it a sentence. Gloss "interventional direct and indirect effects" in a clause: "averages over the paths an agent produces under each referral, not claims about a single run".

**Steering index and evidence sensitivity (line 41).** Four terms in four sentences. Compress (see cut list). Also see Method, line 161: the quantity defined is a percentile shift, not an m-value shift.

**Self-improvement and shrinkage (line 43).** Two concepts in one paragraph; split. Expand GEPA, ACE and GRPO once, or say "a prompt optimizer", "a playbook optimizer" and "an RL method". "GRPO updates weights from a group-normalized reward" needs "rewards normalized within a group of samples for the same input".

**Blinding (line 45).** "Appearance-blind input shows the agent only a rendered skeleton", but Figure 6 says "skeleton or silhouette". Align the two.

**Known ¶1 (line 49).** Loy and Irwig appear here and in Problem ¶3; keep one. The Batista and Griffiths sentence is good.

**Table (lines 51 to 64).** The Brown et al. row is accurate. The Xiao and Yu row says "no remedy"; the abstract mentions "exploratory interventions", so write "exploratory interventions only". See the cut list for rows to drop or merge.

**Gap ¶ (line 66, 46-word second sentence).** Split into two: what no study does by intervention, and what no study does on decisions. "Prior work thus shows" uses a "thus" pivot. The last sentence ("In video, the input itself also shows age, build and walking aids") dangles; write "Video adds a problem that text-only studies do not face: the frames themselves show age, build and walking aids, so deleting the referral line does not remove all context."

**H1 (line 70).** Is the 0.2 SD threshold for the clip average or for ambiguous clips? H1 also predicts small effects on clear clips, so the average may sit below 0.2 even when H1's mechanism holds. State which estimand P1 tests and what the ambiguity interaction must show. Name the API agent here or say "the frontier API model in E1".

**H2 (line 72).** Define "positive" (sign convention, 1.4) and "both orderings" (point to Path splicing).

**H3 (line 74, 45-word test sentence).** Replace as in 1.2. The current final clause "a residual counts as unrecovered by those combiners, not as proof of lost information" is an "X, not Y" antithesis. Write "a residual means the pre-specified combiners did not recover the information; it does not prove the information is gone."

**H4 (line 76).** $\gamma_B$ is used before it is defined (line 169). Add "(the effective shrinkage of the squared-error-optimal report, defined in Method)". See weakness W3 on the moving target.

**H5 (line 78, 45 words).** Split after the GEPA/ACE clause. The claim is narrowed correctly (settled).

**H6 (line 80).** Is "accuracy cost below 0.2 SD" MAE or MSE, and in which units? Say "an MAE increase below 0.2 between-person SD".

**Setting and notation (line 86, 45-word sentence).** Split into: (i) the symbols; (ii) "$q$ is the probability that the referral is wrong"; (iii) the assignment-matrix construction. "Markers on bridge tasks" needs a forward pointer to Data and splits. State that $H\in\{0,1\}$ with $H=1$ the high-risk referral. Also state what referral text the decision task shows the agent (see W8).

**Proposition 1 (line 90).** Replace "A preliminary simulation in this project (`output/idea-summaries-build/sim/b1_double_counting.py`) checked a Gaussian case in which" with "In a Gaussian model in which". Put the simulation in one closing clause: "a simulation over 36 settings and ten values of $\gamma$ found no case where the penalty was zero or negative". The internal build path means nothing to an outside reader and is the kind of drafting artefact STYLE.md excludes. Define $\mathrm{LLR}$ in symbols (line 94). Line 102's "The simulation found no violation in 360 checks" does not say what was checked.

**Figures 2 and 3 captions (lines 106, 110).** Good. See section 6.

**Three boundaries (line 112, 42-word final sentence).** Set as three short sentences, each starting with its boundary ("Who pays: ...", "Which combiner: ...", "When recalibration works: ..."). The last clause, "which a self-improvement loop changes", is the motivation for H4; say so.

**Proposition 2 (line 116).** Reuse $M_0$, $M_H$ and $v$ (see 1.4). Introduce "Ent" with "we write Ent for entropy because $H$ is the referral". Define the features $Y$ or drop them ("the best combiner given its inputs attains their conditional entropy"). Line 120: the censoring identity should condition on the referral, $\sum_h \Pr(H=h)\Pr(M_0>c_h\mid H=h)\,I(C;M_0\mid H=h,M_0>c_h)$; $\Pr(R_0>c_H)$ is ambiguous because $c_H$ is random.

**Path splicing (lines 128 to 136).** Line 128: add the sign convention and the subscript meaning. Line 134 (41 words): split after "replay harness". Line 136: the 59-word simulation sentence should become three sentences: what was recovered; what happens when reasoning is stripped; what happens when it is carried. The final 41-word sentence lists four devices; set it as a short list or split it in two. Define "common support" ("paths that occur under both referrals") and "prefix splice" ("replaying only the first $k$ steps").

**Pseudocode (lines 138 to 151).** Correct. `fresh()` and `transcript(..., arm)` are clear. No change.

**Steering index (lines 159 to 163).** Line 161 defines $\mathbb{E}[G_v(M)]$, where $G_v$ is the distribution function of path values. That is the report's percentile in the multiverse, and the one-sided upper m-value is $1-G_v(M)$. Call it "the framing-induced shift in the report's percentile among the clip's 200 paths (equivalently, minus the shift in the one-sided m-value [12])". Use $\mathcal V$ for the clip set.

**Evidence sensitivity (line 165, 46-word final sentence).** Rename the slope symbol only if $\beta_f$ stays in the E1 model (1.4). The gate is a key concept buried here; give it its own sentence and put it in Key ideas. "In the lab pilot (an unpublished internal account) ..." is quoted here and again in Risks; keep one. Also report the pilot number that bears on the gate: the deterministic OpenCap Monocular plus StaBLE-rules pipeline (see W6).

**Effective shrinkage (line 169, 45-word second sentence).** Split after "target". Note that $\gamma^*$ here equals Proposition 1's because $\mathbb{E}[(m_H-T)^2]=\tau^2+q\Delta^2$ there. "Reward (a)" needs a forward pointer. See W3.

**Blind harness (line 173).** "Masked input places raw frames or skeleton renders in context" contradicts itself, since raw frames are not masked. Write "The input stage places either raw frames (text-blind variant) or skeleton renders (appearance-blind variant) in context." The 42-word interpretation sentence should split after "alternative feature)". The 48-word variants sentence should become a short list. "blind then unblind" is never defined; define it or drop it.

**Self-improvement loops (line 181).** "Per-instance Pareto pool" is jargon; write "keeps every candidate prompt that is best on at least one training clip". Define "positive control" ("a condition built to produce the effect, so the audit can be shown to detect it"). Expand LoRA once.

**Data and splits (lines 187 to 189).** The split arithmetic (171, 43, 128, 20, 108, 151) is hard to follow in prose, and "pilot" is overloaded (1.4). Replace most of line 189 with a four-row table:

| Group | People | Used by |
|---|---|---|
| Sealed test | 43 (the lab pilot's held-out set) | all confirmatory audits; the only people for the pilot LoRA agent, E4 and E5 |
| Calibration | 20 | prompts and variance components, then set aside |
| Development | 108 | optimizers, combiners, $\gamma^*$, $\gamma_B$ |
| Fixed-agent audit | 151 = 108 + 43 | E1 to E3 for agents with no StaBLE training |

The 48-word sentence about fixed agents and the LoRA agent can then shrink to one clause. Define "Cam0" ("the fixed front phone").

**Bridge sets (line 191).** Good. Name what "physical-accuracy claims" means ("agreement with marker-based kinematics").

**Models and tools (line 195).** "an InternVL3.5 model near 8B" is vague; name the checkpoint (InternVL3.5-8B). Is the pilot LoRA agent (trained to output scores) a tool-using agent with a separate report step? Say how it is wrapped. The scripted-controls sentence (45 words) reads well as a 2×2 (route × map); consider four labelled items.

**Baselines (line 199).** Item (5) misattributes counterexample prompting to Brown et al. (see section 5). Replace with "(5) a guard instruction telling the agent the referral may be wrong, which Brown et al. found reduces but does not remove confirmation bias in tool-using judges [23]".

**Metrics (line 203).** "tokens and time per clip" belongs in Compute. Otherwise fine.

**E1 to E4 (lines 207 to 213).** E3 has no hypothesis; label it "(exploratory)". E4: say "six audited checkpoints per run" here, because Figure 8's x-axis depends on it.

**Figures 7 and 8 captions (lines 217, 221).** See section 6.

**E5 (line 223).** State whether each sealed clip runs under both referrals (see W1). "the gated fixed agents" assumes a count (17 = 15 + 2 in the compute table); say "the (expected two) gated fixed agents".

**Ablations (line 227).** Fine.

**Statistical analysis (lines 231 to 237).** Rename $\beta_f$ (1.4). How is P1 aggregated across agents: one test per agent with Bonferroni inside the Holm family, or a pooled effect? The power paragraph uses Bonferroni over five agents while the primary family is Holm over four; state the full family. Line 237: state the variance-component convention (W4) and add P4's power (W1). "No power check exists yet for this proposal, so this is planning arithmetic" is accurate, but "for this proposal" adds nothing; write "This is planning arithmetic with assumed variance components ...".

**Second domain (line 241).** Split the 58-word sentence at the semicolon. Name the agent model. Say whether EchoNet referrals are generated with an assignment matrix as in StaBLE.

**Synthetic check (line 243, 58 words).** Compress (see cut list).

**How to read the results (lines 247 to 258).** "Better measurer, worse decision, at a predicted size" is a slogan; write "MSE falls while log loss rises, by the predicted amount". "Agents infer context from appearance" anthropomorphizes; write "Agent outputs depend on appearance cues". Add a row for "gate passed by no agent" (W6).

**Compute (lines 262 to 278).** Arithmetic checks out (I recomputed every row and the 2,526 total). The 47-word assumption sentence should split after "per report call".

**Risks ¶1 (line 282).** Remove the pilot repetition. Add the gate-failure fallback (W6).

**Risks ¶2 (line 284).** Fine.

**Risks ¶3 (line 286).** The first sentence repeats the path-splicing paragraph; cut it. "Loops are noisy and selected candidates inherit a winner's curse" uses an undefined term; add "(the best of many noisy candidates looks better on the data that selected it than it is)".

**Where to learn more (lines 290 to 295).** All six modules appear in `research/course-modules.md`. Fine.

**Long sentences (over 40 words) not already mentioned:** lines 25 (both sentences), 31, 66, 112, 134, 136 (two), 165, 169, 173 (two), 187 (43 words), 189, 195 (two), 241, 243, 262, 278. Split each at its semicolon or main conjunction.

**LLM-tic instances (STYLE.md):**
- "yet" pivots: line 19 ("yet the hold times differ"), line 21 ("yet clinical information generally improves"), line 25 ("yet Claude Code and Codex stayed stable").
- "thus" pivot: line 66 ("Prior work thus shows").
- "X, not Y" antithesis: line 74 ("not as proof of lost information").
- Slogans: line 23 ("The organizing distinction is calibration bug or information bug"); line 253 ("Better measurer, worse decision").
- Anthropomorphism: line 15 ("treats the sway as a recovered wobble"); line 258 ("Agents infer context from appearance").
- No banned words, intensifiers, em-dashes or en-dashes found.

---

## 3. Cut list (target: at most about 5,900 words after the clarity additions)

The clarity additions above come to about 330 words: box changes +5, decisive-test table and paragraph +150, route and recoverability paragraphs +60 net, three Key-ideas entries +45, worked number +35, sign convention and subscripts +25, split table +10 net. The cuts below remove about 430 words, which would leave roughly 5,640.

| # | Location | Cut | Words saved |
|---|---|---|---|
| C1 | Problem ¶5, line 25 | Delete "Frontier coding agents asked for a compelling finding ... on well-specified tasks [8](#ref-8)." The table and Known section carry all three works; refs 6, 7 and 8 stay cited there | 46 |
| C2 | Problem ¶3, line 21 | Move "Epidemiology names related problems ... QUADAS-2 ... [4]" to Known ¶1 as one clause ("diagnostic-accuracy research calls this review or incorporation bias and rates it with QUADAS-2 [4]"); drop the Loy and Irwig duplicate in Known | 25 |
| C3 | Key ideas line 33 | Delete the "true group" sentence unless consistency is analysed (then use the rewrite in section 2) | 30 |
| C4 | Table lines 59, 63 | Delete the Alexopoulos row (a detection task, tangential; ref 27 is cited nowhere else, so drop it from References) and merge Bertran into the Miao row ("Miao et al.; Bertran et al. [12] [21] ... persona steers results, m-value") | 30 |
| C5 | Gap ¶ line 66 | Compress the first sentence to "Prior work shows that hypotheses steer LLM analysts in some settings and barely in others." | 15 |
| C6 | Key ideas line 41 | Compress to two sentences: multiverse and steering index as a percentile shift [11] [12]; evidence sensitivity as the slope of $M$ on $T$. Detail stays in Method | 25 |
| C7 | Line 23 | Replace with one pointer sentence once 1.2's Key-ideas paragraphs exist | 25 |
| C8 | Proposition 2, line 120 | Delete the last sentence ("Splicing measures how much ... by clipping"); 1.2's Recoverability paragraph now carries it | 38 |
| C9 | Proposition 1, line 90 | Drop the build path and "preliminary simulation in this project" wording (see section 2) | 12 |
| C10 | Line 165 or 282 | Keep the lab-pilot MAE in one place only | 25 |
| C11 | Risks ¶3, line 286 | Delete "Splices are off-policy contexts; the placebo, the inconsistency-remark rate and scripted conflict transcripts expose reactions to them." (repeats line 136) | 18 |
| C12 | Line 243 | Compress the synthetic check to "A cheap third check runs Qwen3-VL-32B (text mode) and the API model on 200 generated retention datasets (half null, half with a 0.2 SD effect) under neutral, positive and negative expectations, comparing the splice decomposition with reset-and-replay [6] and data blinding [18]; the setting is crowded [8] [7] [22], so it tests only generality." | 30 |
| C13 | Line 173 | Drop the undefined "blind then unblind" variant and compress the variants list | 12 |
| C14 | Line 189 | Prose replaced by the split table (net, after the table) | 30 |
| C15 | Risks ¶1, line 282 | Compress to "H1 may fail, as Asher et al. found for frontier coding agents; an equivalence result with a validated audit is still useful." | 20 |
| C16 | Box | Shorter ML contribution and falsifier (1.1) | 15 |
| C17 | Line 136 | Rewrite the simulation sentence (59 words) and the four-device sentence (41 words) in about 70 words | 30 |
| C18 | Metrics, line 203 | Drop "tokens and time per clip" (already in Compute) | 5 |

---

## 4. Scientific review (ICML format)

### Summary

The proposal asks whether telling a tool-using measurement agent the referral (a suspected diagnosis) changes the number it reports, and whether that change harms the downstream decision. The testbed is StaBLE single-leg stance and sit-to-stand clips analysed with RTMPose, OpenCap Monocular and the StaBLE feature code. Proposition 1 shows in a Gaussian model that shrinking the blind report toward the referral lowers MSE over $0<\gamma<2\gamma^*$ while strictly raising the log loss of a combiner whose likelihood was fitted on blind reports. In other words, the referral is counted twice. Proposition 2 writes the excess entropy as information discarded minus information added, and separates one-to-one maps (repairable by per-referral recalibration) from many-to-one maps (not repairable). Path splicing is a two-by-two replay factorial that crosses the referral seen during tool use with the referral seen at the report step. Under explicit assumptions S1 to S4 it identifies interventional direct and indirect effects, with self-splice placebos and three reasoning arms validated in simulation. The experiments audit five agents (E1), splice them (E2, E3) and run 45 self-improvement loops (GEPA, ACE and GRPO under three rewards). The loops test whether accuracy reward drives effective shrinkage toward a pre-computed Bayes endpoint $\gamma_B$, and whether prompt evolution puts more of it in the path (E4). E5 compares a measure-blind, commit, then interpret harness with recalibration, masking, prompting and neutral-brief baselines on decision log loss. EchoNet-Dynamic and a synthetic data-analysis task test generality.

### Strengths

1. **The framing reconciles conflicting evidence.** Clinical information improves reading accuracy [5], while unblinded assessors exaggerate effects [19]. The proposal places the harm in the combination step and models two combiners (Bayes and flat prior), so the claim is precise and falsifiable instead of a general warning about context.
2. **Path splicing is a real methodological contribution.** It identifies interventional mediation effects by construction rather than by sequential ignorability. It states its assumptions, reports both orderings and the interaction, uses the same report call in all four cells, and includes a placebo whose failure modes were shown in simulation (the stripped-reasoning and carried-reasoning cases). It transfers directly to any agent harness.
3. **The theory is checked.** Both propositions are correct as stated. I re-derived the logit identity, the MSE formula, the $2\gamma^*$ range and the entropy identity. The nonlinear Bayes endpoint $\gamma_B$ fixes the earlier mis-specified band.
4. **The leakage hygiene is unusually careful.** Splits are by participant before caching, StaBLE's normalization is recomputed on development people, the reused LoRA's provenance is restricted, and EchoNet's sealed set is the original test split.
5. **The design is honest.** Equivalence testing, scripted controls that cross route with map, every-clip scoring with exclusions counted, an outcome table that includes null and falsifying results, and transparent compute arithmetic (all rows recompute).

### Weaknesses (each with a fix)

**W1. The decision primary outcome (P4) has no power analysis and looks badly underpowered.** P4 (blind harness minus within-referral recalibration, log loss) is the endpoint the whole argument leads to, yet line 237 powers only P1, P2 and P3. Use Proposition 1's own setting as a stand-in. The penalty at $\gamma^*$ is 0.026 nats, concentrated on the 20% of people with wrong referrals (+0.353 against −0.056), so the per-person difference has SD of at least about 0.16 and $d_z\approx0.16$. 80% power at a Holm-level $\alpha=0.0125$ then needs about 440 people. With 43 sealed people, power is about 0.18 even at $\alpha=0.05$. Fix: (i) run every sealed clip under both referrals and compute each person's expected log loss by weighting the two with the assignment matrix $\Pr(H\mid C)$, which removes the referral-draw variance that dominates this SD; (ii) state the smallest log-loss difference of interest and its power; (iii) make EchoNet's 1,000 sealed videos the confirmatory decision test and StaBLE the secondary one, or say plainly that StaBLE's P4 is a descriptive estimate.

**W2. Route and recoverability are conflated in the framing, and H3's route classes are undefined.** See 1.2. Fix: two axes, a pre-specified route class (indirect effect excluding zero and path share above 0.5), and H3 restated as an association validated on the four scripted controls.

**W3. $\gamma_B$ is a moving target.** $\gamma_B$ depends on the agent's blind noise $s^2$. It is "computed before any loop runs" (line 169), but accuracy-rewarded loops are expected to reduce $s^2$ as well as learn shrinkage, and a smaller $s^2$ lowers $\gamma_B$. A loop that both measures better and shrinks optimally could therefore leave the pre-computed band, and the cause would be correct optimization, not failure. Fix: pre-register the formula. At each checkpoint, estimate $s^2$ from that checkpoint's blind runs (referral removed) on development people, recompute $\gamma_B$, and test $\hat\gamma$ against the checkpoint's own $\gamma_B$. Report the fixed pre-loop value as secondary.

**W4. The power arithmetic depends on an unstated variance-component convention that the E1 model contradicts.** The model at line 233 has per-framing random effects $u^F_{if}$ and $w^F_{ijf}$. If the assumed SDs (0.2 and 0.3) are per framing, the frail-minus-athlete contrast doubles them. The person-level contrast variance becomes $2(0.2^2)+(2(0.3^2)+2(0.5^2)/8)/3\approx0.161$ rather than 0.091. Then $n$ for P1 rises from 34 to about 60 (more than the 43 sealed people), P2's power on 151 people falls from 0.93 to about 0.69, and TOST on 43 people falls from above 0.99 to about 0.90. Fix: state that the SDs refer to the person-level and clip-level contrast, or recompute with per-framing components and adjust the samples (for example, more clips per person).

**W5. P3 is powered at the edge of the predicted effect.** The detectable gap is 0.23 SD (10 against 5 seeds). Figure 8 predicts an indirect-effect gap of about 0.17 in shrinkage units. With a between-referral gap of about 1.4 between-person SD, as in Proposition 1's setting with balanced classes, that is about 0.24 SD, so P3 sits at about 80% power only if every assumption holds. Fix: reallocate the fixed 45 runs toward the main arm: reward (a) 8 seeds per optimizer, reward (b) 3, reward (c) 4 (24 + 9 + 12 = 45). That gives 16 against 8 seeds and a detectable gap of about $2.8\times0.15\times\sqrt{1/16+1/8}\approx0.18$ SD, with no change in compute. Update Figure 7's dots if adopted.

**W6. Gate feasibility is unaddressed, and the loops depend on it.** The lab pilot (`research/biomech-facts.md` §1.3) found the frozen Qwen3-VL-8B worse than a constant guess (0.238 against 0.120). It also found the deterministic OpenCap Monocular plus StaBLE-rules pipeline worse than a constant guess on task scores (0.146 against 0.120, with Y-Balance failing outright). All loops optimize Qwen3-VL-8B. If no agent's blind slope clears 0.3, E2 to E5 collapse, and the document has no fallback. Fix: report the pilot pipeline's slope against the reference on the single-leg stance feature (the gate's actual quantity), name which agents are expected to pass, and pre-specify a fallback. Options are to start the loops from the pilot LoRA agent wrapped with tools, or to restrict to the tasks where the tool pipeline passes. Add a "no agent passes the gate" row to the results table.

**W7. The 0.2 SD margin is justified on the measurement scale only.** In Proposition 1's setting (between-person SD about $1.41\tau$, $\Delta=2\tau$), a 0.2 SD framing effect is $\gamma\approx0.14$ and costs about 0.004 nats, roughly 1% of the blind log loss of 0.365. So an effect at the margin is nearly harmless to the decision under the direct route, which undercuts using it as the falsifier in the box. Fix: justify the margin by its decision cost, for example "the smallest framing effect whose decision penalty exceeds X nats in the development-fitted model", or add a decision-scale margin for P4.

**W8. The decision task's referral content is underspecified.** $H$ is binary with error rate $q$, but E1's framings are frail and athlete. "Athlete" is not the low-risk class; elite balancers sit beyond it. Meanwhile $m_h$, the denominator of $\hat\gamma$, is "the mean reference value of development people in the class that referral $h$ points to". If E4 and E5 show "collegiate gymnast" for $H=0$, the agent's natural target is the elite mean, not the low-risk class mean, and $\hat\gamma$ is mis-scaled. Fix: give the exact referral texts for the decision task (for example "suspected high fall risk" and "routine screening, no concerns"), use them in E4 and E5, and keep frail and athlete for E1.

**W9. The placebo tolerance equals the smallest indirect effect of interest.** Self-splices must match natural runs "within 0.1 SD" (line 134), and P2's power is computed for an indirect effect of 0.1 SD. A placebo gap at the tolerance could account for the whole effect when the result is transported to the intact agent. Fix: tighten the placebo margin to 0.05 SD, or power P2 for an indirect effect above the margin. Say how the placebo is tested (TOST per agent and referral).

**W10. Scope dilutes the core result.** Six hypotheses, five experiments, a steering index, evidence-sensitivity ratios, two extra domains and eight harness variants compete for attention. Fix: mark E1, E2, E4 and E5 as core and the steering index, E3 and the synthetic check as secondary (see 1.3). This also justifies the cut list.

(The optimizer-configuration confound was settled in the resolutions and is correctly acknowledged; not re-raised.)

### Questions for the authors

1. What is the blind slope of the deterministic tool pipeline on single-leg stance hold time in the lab pilot, and which of the five agents do you expect to pass the gate?
2. How is the pilot LoRA agent, trained to output scores, wrapped as a tool-using agent with a separate stateless report step?
3. Is P1 one test per agent (Bonferroni inside Holm) or a pooled estimate, and what is the full multiplicity family?
4. In E5, does each sealed clip run under both referrals? If so, will the decision loss be averaged over the assignment matrix (W1)?
5. What referral texts does the decision task use, and how does $m_b-m_a$ map onto them (W8)?
6. For GRPO, what is a "checkpoint", and how do the 6,000 rollouts divide between path-phase and report-step tokens?
7. Does stripping segment dimensions from OpenCap outputs in the appearance-blind arm also degrade blind accuracy, and is that cost charged to H6?
8. Are EchoNet referrals generated from an assignment matrix as in StaBLE, and which VLM runs the EchoNet agent?

### Scores

- Soundness: 3 / 4. The theory and identification are correct. The decision endpoint's power, the $\gamma_B$ target and the variance convention need fixing.
- Presentation: 2 / 4. The prose is rigorous but dense, with symbol clashes, forward references and no hypothesis-to-test map.
- Contribution: 3 / 4. Path splicing and the route-recoverability question are new and general. The phenomenon itself is partly established.
- Overall: 6 / 10.
- Confidence: 4 / 5.

---

## 5. Citation spot-check (8 load-bearing citations, plus two extras)

| Ref | Link fetched | Result | Mismatch and fix |
|---|---|---|---|
| [12] Miao, Pritchard, Zou, arXiv 2607.01507 | arxiv.org/abs/2607.01507 | Title and authors match. The m-value is defined as "the probability that an analysis path would produce a claim at least as extreme as the reported one". Personas steer conclusions; no ground truth | None. The table row is accurate. Note the steering index is a percentile shift (section 2, line 161) |
| [6] Gunsilius, Van Dijcke, Wuthrich, arXiv 2611.23174 | arxiv.org/abs/2611.23174 | "four frontier agents report significant p-values between 54% and 98% of the time when asked to produce a compelling finding" on zero-effect data; reset-and-replay on subsamples, asymptotically valid for agents with stable selection | None. The text says "Frontier coding agents"; the abstract does not name them, so "four frontier agents" would be exact |
| [8] Asher et al., working paper (PDF) | andrewbenjaminhall.com PDF, pages 1 to 3 read | Claude Opus 4.6 and GPT-5.2-Codex; four political-science papers with null or near-null results; 640 runs; "under standard prompting, including an ex-ante hypotheses and even explicit pressure for significance, both models produce stable estimates" | No mismatch, but the proposal undersells the finding. Stability held even with a directional hypothesis, which is the strongest prior against H1. Write "stayed stable even when the prompt stated a directional hypothesis" (line 25 if kept, table row, Risks) |
| [23] Brown et al., arXiv 2611.05662 | arxiv.org/abs/2611.05662 and the HTML full text | "overturns up to 40% of a tool-using judge's correct verdicts"; three failure modes; "Lightweight mitigations blunt but never remove the bias". The mitigations tested are a guard instruction, a cite-evidence checklist, a learned skill and a sufficiency gate. Counterexample prompting is not tested | **Mismatch at Baselines item (5), line 199**: "prompts to ignore the referral and counterexample prompting, which Brown et al. found blunt confirmation bias without removing it". Fix: "a guard instruction saying the referral may be wrong, which Brown et al. found reduced harmful flips (18% to 5%) without removing them and also removed helpful corrections [23]". If counterexample prompting stays as a baseline, cite a source that tested it (the literature notes point to EchoBench) or drop it. The lost helpful corrections are relevant to H6's trade-off and worth one clause |
| [25] Cuccarese, arXiv 2604.06013 | arxiv.org/abs/2604.06013 | Blinding "changes 16% of top-20 predictions while preserving identical recovery of validated targets"; the evolutionary optimizer of scoring functions runs without entity identity; identifiers replaced with anonymous codes | None. The row and Baselines item (4) are accurate |
| [1] Heigold et al., StaBLE, bioRxiv | doi.org/10.64898/2026.09.16.750744 redirected to bioRxiv, which returned HTTP 429; data release doi.org/10.5281/zenodo.22286165 fetched | Zenodo: 180 participants aged 18 to 87, 18 tasks, 71 self-reported diagnoses, 30 in competitive sports; features and scores only, no videos; OpenCap kinematics for 7 exemplar participants | Consistent with lines 13 and 189 and the "seven people in the public exemplar" clause. The phone count and three-camera reference come from the local preprint notes, not from the page I could fetch |
| [19] Hróbjartsson et al., CMAJ 2013 | doi redirected to cmaj.ca (403); Europe PMC record fetched | 16 trials, 2,854 patients; nonblinded assessors "exaggerated the pooled effect size by 68%" (95% CI 14% to 230%); CMAJ 185(4):E201 to E211 | None. Optionally restore the diacritic (Hróbjartsson) |
| [5] Loy and Irwig, JAMA 2004 | doi redirected to jamanetwork (403); Europe PMC record fetched | Clinical information generally improved accuracy, with a smaller gain for real than for constructed information; no study found it significantly reduced accuracy | Claims match. The reference gives only the start page; write "JAMA 292(13):1602 to 1609" |
| [24] Xiao and Yu, arXiv 2611.05720 (extra) | arxiv.org/abs/2611.05720 | Stage-level measurements separate reduced retrieval from persisting errors; the abstract also mentions "exploratory interventions" | Minor: the row's "no remedy" is slightly strong. Write "exploratory interventions only" |
| [10] VanderWeele, Vansteelandt, Robins, Epidemiology 2014 (extra) | Europe PMC record | Three decompositions identifiable with an exposure-induced mediator-outcome confounder, pages 300 to 306 | The abstract does not name interventional effects, but the paper is the standard source for randomized interventional analogues; the citation is appropriate |

---

## 6. Figure review

All eight PNGs were rendered and inspected. Lint reports no overlaps (only arc-approximation notes). Word counts are 43 to 85 per figure, within the guide.

**Figure 1, one-video-two-referrals.** One clear point (same clip, two defensible paths, two hold times). The caption does not say what to look at and uses a "yet" pivot; use the replacement in section 2. The text says "routine screening" but the figure says "screening"; align them. Otherwise ship.

**Figure 2, referral-counted-twice.** One clear point. The caption defines $H$ and $M$ and says what the orange arrows mean, and the figure matches the text. Ship.

**Figure 3, better-measurer-worse-decision.** One clear point. All plotted values match the text (0.357, 0.64, +0.026, shading ending at $2\gamma^*\approx0.71$). Optional change to tie the figure to H4: add $\gamma_B$ as a separate marker off the curve at $(0.214, 0.614)$ in the left panel and at $(0.214, 0.019)$ in the right, labelled "Bayes rule ($\gamma_B$)". This shows that the unrestricted optimum shrinks less and beats every linear blend. The blue MSE curve reuses the colour that means "blind" in Figures 2 and 6; neutral ink would keep colour meanings consistent. The caption is fine.

**Figure 4, calibration-bug-or-information-bug.** One point, but the titles ("Direct route: a shift recalibration can undo", "Path route: trimming erases differences") reinforce the route-equals-recoverability conflation (W2). The left title is also missing "that". Retitle by map ("One-to-one: a shift that recalibration can undo"; "Many-to-one: a cap that erases differences"), and add to the caption: "Either route can produce either map; the scripted controls cross them." In the right panel the athlete line and the frail line below the cut are offset by about 12 px and differ slightly in slope. That suggests a referral shift on the path route, which the schematic does not intend. Either overlay them below the cut (athlete dashed on top) or add "drawn apart for visibility" to the caption.

**Figure 5, path-splicing-factorial (round-3 fixes, not re-reviewed by Codex).** Verified: the effect labels and subscripts are now legible; the interaction sits on one line ("DE_b − DE_a = IE_b − IE_a", which I checked algebraically equals the text's interaction); the example card is short and attached to $\mu(a,b)$; all four arrows point the right way for the definitions at line 132; and every cell is dashed, matching "every cell replays". The figure makes one clear point and matches the text. The one change is in the caption: add "Subscripts name the referral held fixed: $\mathrm{DE}_a$ holds the path at $a$, $\mathrm{IE}_b$ holds the report at $b$." Ship with that caption edit.

**Figure 6, blind-analysis-harness.** One clear point. Three mismatches:
- The caption says "Blue stages never see ... the person's appearance", but that holds only in the appearance-blind variant; the text-blind variant shows raw frames. Write "In the appearance-blind variant shown, blue stages never see the referral or the person's appearance."
- The input card says "skeleton or silhouette", but the text mentions only skeleton renders. Drop "or silhouette" or add it to the text.
- The Decision card uses the referral (as the prior) but is neutral, while the caption says orange marks the stages that see the referral. Outline Decision in orange, or add "the decision uses the referral once, as the prior" to the caption.

**Figure 7, self-improvement-design (round-3 fixes, not re-reviewed by Codex).** Verified: the development banner and arm (c) are neutral, the dot key is gone, the audit title reads "Audit every checkpoint / from all 45 runs", the sealed-cohort arrow enters the audit card separately, and the bracket clears the third column. One clear point; matches the text. Optional: add "6 checkpoints per run" under the audit title or in the caption, because Figure 8's x-axis depends on it. If W5's seed reallocation is adopted, the dots change to 8, 3 and 4 per row and the headline formula changes. Otherwise ship.

**Figure 8, predicted-routes-by-optimizer (round-3 fixes, not re-reviewed by Codex).** Verified: the status line and claim headline are present, the neutral dotted reward (c) traces are labelled "all optimizers" in both panels, all four orange endpoints are marked, and the band label has a legible subscript. Three remaining issues:
1. The x-axis reads "generation" from 0 to 10, but each run has six audited checkpoints (line 181), and GRPO has no generations. Relabel it "audited checkpoint" with ticks 0 to 6, or "rollouts (thousands)" from 0 to 6.
2. "band: γ_B (dashed)" collides with GRPO's dashed curve in the same panel. Draw the $\gamma_B$ reference as a thin grey dotted line labelled directly "γ_B = 0.214".
3. The left panel shows GRPO's total effect well below GEPA/ACE (about 0.17 against 0.24). That is a prediction H4 and H5 do not register. Either draw both totals ending near the same value inside the band, or add to the caption "the total-effect gap is not part of the prediction".

The caption is otherwise accurate.

**Missing figure (optional).** STYLE.md suggests a split diagram. The split table proposed in section 2 does the job at lower cost; a figure is not needed.
