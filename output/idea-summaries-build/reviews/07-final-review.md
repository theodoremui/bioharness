# Proposal 07: final independent review

Target: `docs/idea-summaries/07-learning-how-to-look-at-tool-outputs.md` (audit count 6,297 prose words, 8 figures, 35 references) and the eight SVGs in `docs/idea-summaries/images/07/`, rendered to `output/idea-summaries-build/png/07/` and inspected one by one. Line numbers refer to the current file. I read `07-resolutions.md` first and do not re-raise settled points unless the resolution leaves a problem; where I do, I say so.

The short verdict is that the science is careful and the leakage controls are strong. The document is hard to read on a first pass, for three reasons. The central idea (where a renderer's gain comes from, and which part transfers) is spread over six places and is stated inconsistently in two of them. Terms and participant groups are used several sections before they are defined. And the notation reuses the same letters for different objects. The fixes below can be made without adding net length.

---

## 1. The five changes that would most improve readability and conceptual clarity

### Change 1. State the central idea once, as a four-way split of a gain with one example per part

**Problem.** A reader has to assemble the core concept from L23, L35, L37, L113 to L117, L119 and E5. Two of those statements disagree. L23 says a rendering's gain may "compute a useful feature, show sway in a form any competent reader decodes better, or exploit a quirk of that model". L119 says, correctly, that drawing a derived feature "cannot push $I$ below that of a lossless encoding; it lowers $P$". So computation sits inside the perceptual term, not the information term. Yet the box (L7) describes the split as "information, shared perception and reader-specific exploitation", which reads as if computation were counted as information. The three-term form of the gain is also never written down as one equation, and $S_A$ is never tied to it.

**Fix.** Put this table in Key ideas in place of most of the "Information and perceptual terms" paragraph (L35). Then add the equation and the identity in Splitting a gain (after L117).

| Where a gain can come from | Tandem-stance example (reader Qwen3-VL-8B) | Term | What separates it |
|---|---|---|---|
| Information the default plot discarded | fixing the axis at a physical scale, so 1 cm and 3 cm of sway no longer look the same | $\Delta I$ | oracle floors |
| Computation done for the reader | drawing the fitted 95% ellipse | part of the shared perceptual gain $\overline{\Delta P}$ | E5, derived quantities on or off |
| A display most readers decode well | showing sway as position on a common axis, not as area | the rest of $\overline{\Delta P}$ | E5, marks against text |
| A quirk of the scoring model | a line width or hue that only Qwen's vision encoder resolves | $\Delta P_A-\overline{\Delta P}$ | transfer to held-out readers |

Equation to add:

$$G_A=\underbrace{\Delta I}_{\text{information}}+\underbrace{\overline{\Delta P}}_{\text{shared perception}}+\underbrace{\Delta P_A-\overline{\Delta P}}_{\text{specific to }A},$$

followed by: "When every held-out reader's floor matches $A$'s, the mean held-out gain is $\Delta I+\overline{\Delta P}$, so $S_A=(\Delta P_A-\overline{\Delta P})/G_A$: the reader-specific share is the fraction of $A$'s gain that only $A$ receives." This one line is what makes $S_A$ meaningful, and it is missing now.

Then correct L23 to match (see Change 2), and change the ML-contribution line in the box to "a split of each gain into information, perception shared across readers (which includes computation the renderer does for the reader) and a part specific to the scoring model".

### Change 2. End the problem section with the question, why it is open, the decisive experiment and the falsifier, in plain words

**Problem.** The research question appears in the box and again at L23 as a 41-word sentence that uses "graphical-perception battery", "self-designed rendering" and "co-adaptation" before any of them is defined. The document never says in the problem section why the answer is unknown, and it never names E3 plus E4 as the decisive experiment. The title asks a different question ("Can a vision-language agent learn how to look at its own data?") from the research question, which is about predicting transfer.

**Fix.** Retitle the document "Can a perception test predict who else can read an agent's plots?" (11 words). Replace L23 with this paragraph (about 175 words against about 100 now; Section 3 pays for it):

> Once the agent writes its own rendering code and keeps whatever lowers one reader's error, the gain can come from four places. A renderer can restore information the autoscaled default plot threw away, for example a fixed physical scale. It can compute a feature for the reader, such as the 95% ellipse. It can use a display most readers decode well, such as position on a common axis. Or it can rely on a line width or hue that only Qwen3-VL-8B's vision encoder resolves. The first three should also help other models and the clinician. The last should not. We ask whether a short perception test of each reader, run before any search, predicts how much of an evolved renderer's gain carries over to other readers. The answer is unknown because perception tests of VLMs have so far only described readers, and no study has evolved a renderer for one model and measured who else can read it. The decisive experiment evolves renderers against one model, forecasts each held-out reader's gain before scoring it, and checks the forecasts on sealed participants (E3 and E4). The idea fails if the forecasts rank readers no better than model family and size.

### Change 3. Define participant groups, "normalized error" and the reader sets before Method uses them

**Problem.** Method uses "calibration people" (L99), "development and calibration people" (L129), "dev-train" and "dev-select" (L135, L157, L161) and "sealed people" (L129, L161). H4 (L71) uses "dev-select" too. All of these are defined only at L169, in a 212-word paragraph. "Normalized error" is the fitness (L135), defines accuracy and $D_t$ (L161), and sets the scale of Figures 6, 7 and 8, but the text never defines it. D1 to D4 are in cm, cm² and ms, and D5 includes an AUC, so the average is undefined as written. The text also uses five names for overlapping sets of readers: held-out $\mathcal H$, fresh $\mathcal F$, "readers outside every fitness condition" (H3), "unseen family" (Figure 5) and "VLMs outside both fitness sets" (Figure 6).

**Fix.** Add a "Participants and readers" paragraph to Key ideas with this table. It replaces the middle of L169, so the net cost is about 20 words.

| Group | People | Used for | Never used for |
|---|---|---|---|
| dev-train | 52 | mutator feedback, oracle training, reader fine-tuning | fitness, choosing a best renderer |
| dev-select | 52 | fitness, every choice of a best renderer, the frozen-reader term | mutator feedback, training |
| calibration | 24 | calibration maps $h$, battery stimuli, oracle validation | search |
| sealed test | 43 | one scoring of each checkpoint after its run ends | everything else |

Also add one sentence defining normalized error. One option: "For each decision, normalized error is the mean absolute error divided by that of predicting the dev-train mean, so 1 means no better than the mean and 0 means perfect; fitness averages it over the two fitted decisions." Then name those two decisions; L266 says "two decisions" without saying which. Finally, give the reader sets one name each. Use $\mathcal H$ for readers held out from a given run, and call the readers that set fitness in no condition "never-fitness readers". Use the same set in H3 and Figure 6 (see W7).

### Change 4. Remove notation clashes and give each object one symbol and one name

**Problem.** These clashes each cost a careful reader a re-read:

- Renderers are written $e$ (L79, $e_0$ and $e_1$ at L111), $r$ (L125 to L129) and $r_t$ (L157). Worse, $e_0$ is the default line plot while $r_0$ is the clinical stabilogram (L157).
- $D_t$, the drift gap (L159), collides with decisions D1 to D5 (L175 to L179). "$D_4$" can mean either the timing decision or the gap at round 4.
- $e_1$, the evolved renderer, sits next to experiment E1.
- Readers are $\pi$ (L79 to L99), $X$, $A$ and $B$ (L101 onward) and $A_t$ (L157). In E7, "policy" also means an RL policy.
- "Legibility term" names two different objects: the frozen-reader term in co-adaptation (L161, weight $\mu$) and the crowd-profile term in the last fitness row of Figure 5 (L183). The second one is never given a formula or a weight.
- The same idea is called "private dialect" (L39, L73, L259), "private visual code" (L7), "pair-specific code" (L163, L260) and "reader-specific code" (L255).
- "Saved renderers" means every survivor in the pseudocode (L147) but eight checkpoints per run in Compute (L269, L271).

**Fix.** Use $r$ for every renderer, with $r_{\text{def}}$ for the default plot and $r_{\text{stab}}$ for the stabilogram. Rename the decisions Q1 to Q5, or rename the gap $\Delta_t$. Use $X$ for a generic reader, $A$ for the source and $B$ for a held-out reader, and drop $\pi$ outside the Objective, or keep $\pi$ only there. Name the two terms "frozen-reader term" ($\mu$) and "predicted-human term" (give its formula, for example $\nu\,\hat P_{\text{crowd}}(r)$, and its weight). Use "private dialect" everywhere. Use "checkpoint" for the eight renderers per run that are scored on sealed people.

### Change 5. Give each hypothesis a one-line plain claim and a decision rule, and add a roadmap at the top of Method

**Problem.** H1 to H5 are single sentences of 50 to 68 words that mix the claim, the estimand and the threshold. H1's rule is ambiguous: L65 says the correlation "is at least 0.5", but L237 tests it "with a smallest effect of interest of 0.5" by permutation, and the power calculation targets 0.6 against 0. A reader cannot tell whether H1 passes on a point estimate of 0.5 or above, on a lower bound above 0.5, or on significance against 0. H2's test is "the slope of observed on predicted shortfall" with no value that would count. Method has six subsections and no sentence saying how they connect.

**Fix.** Proposed wording:

- **H1 (primary). Profiles predict who else gains.** Before any held-out score is seen, the registered rule forecasts each held-out reader's gain from each evolved renderer. Within each renderer (gains centered on the renderer's mean), the leave-one-reader-out Spearman correlation between forecast and observed gain is at least 0.5 as a point estimate, has a permutation $p<0.05$, and exceeds the family-and-size predictor's correlation with a paired-bootstrap lower bound above 0.
- **H2. Single-reader search drifts toward the source reader's strong channels.** Under single-reader fitness, renderers shift weight toward channels where reader $A$ resolves differences better than the crowd panel does, and people's shortfall relative to $A$ grows as the two profiles predict (the slope of observed on predicted shortfall has a 95% interval that excludes 0 and includes 1).
- **H3. Two-family fitness keeps gains readable.** At equal reader calls, averaging fitness over two readers from different families keeps the transfer ratio to never-fitness readers at 0.8 or above after 40 generations, costs at most 20% of $A$'s gain, and transfers better than a same-family pair.
- **H4. Gains survive a ban on printed text.** With in-image text limited to axis ticks, the best evolved renderer (chosen on dev-select) beats the clinical stabilogram for reader $A$ on sealed participants, and its marks beat the same computed values shown as text at equal tokens.
- **H5. Co-adaptation creates a private dialect.** Alternating renderer search with reader fine-tuning raises the pair's accuracy while fresh readers lose accuracy on the same renders. The decisive part is that the fine-tuned reader reads its own renderer better than renderers co-adapted with independent copies (the matched-pair test). A frozen-reader term closes at least half of the gap by raising fresh readers' accuracy.

Roadmap sentence for the top of Method: "The method has four parts. We split each reader's error into what the image omits and what the reader misreads, and apply the split to the gain from a new renderer. A perception battery turns each reader's misreadings into a profile that forecasts gains. The renderer search (Figure 4) and the co-adaptation arm produce the renderers whose gains are forecast."

---

## 2. Paragraph-by-paragraph edits

Numbered so they can be checked off. LLM tics are collected at the end of this section.

**Title and box**

1. L1, title. It does not name transfer, which is the actual question. Use "Can a perception test predict who else can read an agent's plots?"
2. L3, research question (42 words). Replace with: "When an agent evolves the code that plots its tool outputs for one vision-language model, can a short perception test of each reader, run before the search, predict which other models and people also benefit?" (36 words).
3. L7, ML contribution (52 words). "Self-designed observation", "Bayes-risk split" and "private visual code" are undefined at this point. Replace with: "A rule, registered before the search, that forecasts from perception profiles which readers gain from an evolved plot; a split of each gain into information, perception shared across readers and a part specific to the scoring model; and a test for a private visual code under co-adaptation." (45 words).
4. L9, falsifier. "Sealed test people" and "clinical stabilogram" are undefined in the box. Use "held-out participants" and "a standard clinical sway plot", and put "(primary)" after the first clause.

**The problem, in one concrete case**

5. L13. Define OpenCap ("which reconstructs 3D motion from several synchronized smartphone videos"), "monocular agent" ("an agent that sees one phone's video") and "keypoints" ("image positions of 17 body landmarks such as nose, knees and ankles").
6. L15. "Printed numbers keep everything" refers to the keypoints, while the other three forms use the CoM path. Write "Printing the keypoints keeps every value but costs ...". Define "95% prediction ellipse" as the ellipse expected to contain 95% of the CoM positions. Write "about 600 visual tokens for Qwen3-VL", because Gemma 3 resizes every image to 896 by 896 and spends a fixed 256 tokens, and InternVL3.5 tiles at 448 pixels (see item 14).
7. L21 (48-word sentence). Split after "(0.120)". Add the caveat from `biomech-facts.md` that these pilot scores use StaBLE's published normalization over all 180 people, which the proposal itself treats as leakage at L169.
8. L23. Replace with the paragraph in Change 2. This also fixes the conflation of computation with information.
9. L25 (51 words). Split at the semicolon: "... while vision-only views hurt [9]. An agent that evolved such views against one model would need to know whether they also help another model and the engineer who reviews its trace."

**Key ideas in plain terms**

10. L29 (52 words). Split into three sentences: "A reader is any system that maps an input to a decision: a VLM, a trained network, a crowd worker or a clinician. An encoding $e$ turns the tool output into reader input, as text or an image. A renderer is an encoding written as plotting code that an agent can edit." Add that a "decision" is one of the quantities Q1 to Q5 the reader must report.
11. L31. Define "channel" before it is used: "a channel is the visual property that carries a value (position, length, angle, area, color)". Replace "how large the judged difference appears" with "the size of the judged difference as a fraction of the panel", which matches $m$ at L123.
12. L33. "Near Bayes" is undefined; write "close to the Bayes risk, the lowest error any decoder can reach from that input". "Information-matched" is defined here but used only in Where to learn more, item 1. Either drop it, or use it at L101 where floors are pooled.
13. L35 (62 words). Replace it with the table in Change 1. Whatever stays, fix "the reader's excess over the oracle" to "the reader's excess over the best possible decoder of the same image, which the oracle estimates". Mention resolution before calibration, to match Figure 2's left-to-right order.
14. L37 (79 words) joins two unrelated ideas; split it into "Visual tokens" and "Transfer". "A VLM turns each block of image patches into a fixed number of tokens, so image size sets token cost" is false for Gemma 3. Write: "Qwen3-VL spends one token per 32 by 32 pixel block, InternVL3.5 256 tokens per 448-pixel tile, and Gemma 3 a fixed 256 tokens per image." Move "Pareto front" to E1, the only place that uses it. Add a numeric example: "If a renderer cuts Qwen3-VL-8B's error by 0.04 and Gemma 3 12B's by 0.01, then $T(\text{Gemma}\mid\text{Qwen})=0.25$."
15. L39. The last sentence ("The renderer search is itself a self-improvement loop over the agent's own code") dangles; move it to the opening of Method or into the Change 2 paragraph. Use "private dialect" as the only name.
16. Add the participant-group table and the reader-set names from Change 3 here.
17. Add one-line definitions of fitness (the score the search minimizes), mutator (the code LLM that edits renderer code) and archive (the store of renderers kept for breeding). All three are used in H2, H3 and L135 before Method defines them.

**What is known and what is missing**

18. L47 (52 words) repeats the first four table rows. Compress it to: "Plots are known to beat printed numbers for time-series reasoning in multimodal models [5]-[8], and VLM graphical-perception profiles are known to differ from human ones [12]-[16]." (Write the ranges as "[5] to [8]" to keep en-dashes out.)
19. L53. For By My Eyes, "by rating its own plots" is inaccurate. The paper's MLLM filters 16 functions and then chooses the single best of its own renders. Write "picks the best of its own renders from 16 plotting functions".
20. L54. "Profiles are descriptive and predict nothing" reads as a slogan. Write "Profiles describe readers; none is used to forecast a downstream gain."
21. L57. For Dubey et al., the abstract reports "average accuracy" from 16.6% to 41.3% across three VLMs and four benchmarks. Write "average accuracy" unless the body says exact match.
22. L61 (49-word sentence plus a triad of negations). Split it, and replace the triad with: "This proposal does not claim that plots beat numbers or that its battery is the first for VLMs; a position paper already poses the machine-reader question without experiments [17]." Cut the "Missing are ..." sentence, which repeats the box.

**Hypotheses**

23 to 27. L65 to L73: rewrite H1 to H5 as in Change 5. The H3 target set must match the one Figure 6 shows (see W7), and the decisive conjunct of H5 should be named.

**Method**

28. Add the roadmap sentences from Change 5 under `## Method`.
29. L79 to L83, Objective. Say in one clause that $\lambda$ only matters in E1, and define the error-token Pareto front there.
30. L95. "The identity telescopes, and its content lies in the signs" is aphoristic. Write: "The identity holds by construction; it is useful because both added terms are non-negative." Replace "(Blackwell's ordering of experiments)" with "because $e(o)$ is computed from $o$". Compress the log-loss and $\mathcal V$-information sentence (46 words) to one clause, since nothing later uses it.
31. L101 (168 words, with sentences of 45 and 54 words). Split it into two paragraphs: (a) the conditions under which the split holds and the reader-indexed floors; (b) oracle validation and data. Move "Dev-train holds only about 750 trials, far below the 5,000 renders the simulation below needed ..." after the simulation paragraph, because it depends on that result.
32. L103. Delete the build path `output/idea-summaries-build/sim/d_decomposition.py`; the proposal should stand alone. Define "20-pixel plot" ("a bar at most 20 pixels tall on an autoscaled axis"), "position reader" ("reads bar height with 3% multiplicative noise") and "area reader" ("perceives the value through Stevens-type compression, a systematic misreading"). Say that the simulated oracle is a k-nearest-neighbour regressor; the Figure 3 caption says this, but Key ideas says "a small convolutional network". Also, the simulation's recalibration is quadratic while L95 says "affine or monotone"; say which one. Split the 49- and 44-word sentences.
33. L111 to L117. Add the three-term equation and the $S_A$ identity from Change 1. Use $r_{\text{def}}$ and $r$ in place of $e_0$ and $e_1$.
34. L119. Add: "So the information term never credits computation: a renderer that draws a fitted ellipse shows up as perceptual gain shared by every reader, and only E5 separates the two." "It lowers $P$ by doing the reader's work" is mild personification; "by computing what the reader would otherwise estimate" is more precise.
35. L123 (121 words; one 52-word sentence). (a) Correctness: Cleveland and McGill and Heer and Bostock score $\log_2(|\hat p-p|+1/8)$ with $\hat p$ and $p$ in percent. With proportions in [0, 1], the 1/8 term dominates every small error. Write "with $\hat p$ and $p$ in percent". (b) Give the functional form of the "two-parameter resolution curve", for example $\sigma_{Xk}(m)=a_{Xk}+b_{Xk}/m$. (c) Split the long sentence after the channel list.
36. L125. Define $m_{rk}$ concretely, for example: "the median fraction of the panel spanned by the dev-people interquartile difference in the decision variable; for the stabilogram, a 2 cm sway difference spans about 8% of panel width". Say what $c_d$ is fitted on (reader $A$ only? every reader's default-plot error on development people?). Say how a mark's knockout weight is shared among the channels the mark uses.
37. L129. Define "knockout oracle" as an oracle retrained on renders with one mark removed. Use active voice: "We register the battery, ..." in place of "are registered".
38. L133 (56-word sentence). Split after "per trial". Define "arm" as one search condition.
39. L135 (162 words). Split it into "Mutator" and "Selection" paragraphs. State what the in-loop probe is for (it tells the mutator what the image contains that the reader misses). Define tournament selection (draw 4 at random and keep the best). Say "sampling temperature of the mutator". Most important, say how the MAP-Elites descriptor (the "channel carrying most weight") is computed for every child during search. As written, it needs knockout oracles, and L271 says those are fit only for saved renderers. The descriptor could come from the grammar's declared channel of the mark that carries the decision field.
40. L146 to L147, pseudocode. "save every survivor with generation g" conflicts with "eight checkpoints per run" (L207, L269). Say how the eight are chosen (for example every fifth generation).
41. L157 (65-word sentence). Split it into renderer step, reader step and GRPO settings. Define "KL weight" as the penalty on divergence from the round-start reader.
42. L161. "Accuracy" is defined here but used in H5 and in Figure 8 before this point; move the definition into Key ideas along with normalized error. $\mathcal F$ includes Qwen3-VL-32B, the same family as $A$; report $D_t$ for same-family and other-family fresh readers separately. Call the $\mu$ term the "frozen-reader term".
43. L163. Delete the E7 sentence (see the cut list). Change "pair-specific code" to "private dialect".

**Experiments**

44. L169 (212 words; one 51-word sentence). Replace it with the Change 3 table plus three short sentences: the sealed-cohort disclosure, the normalization recomputation, and the held-out tasks with the exemplar-video sensitivity check. Name the three held-out tasks, or state how they are drawn and that the draw is registered. Resolve BioCV's role: the text says "five-fold cross-fitting by person", while Figure 4 lists BioCV under post-search "Held-out tasks".
45. L173 to L179, decision table. Rename D1 to D5 (Change 4). Define "bottom-decile flag" as "participants whose task score falls in the lowest 10% of development people". For D4, say what "time of a step" means in a stance task (the moment the participant steps out of the stance).
46. L183 (129 words; sentences of 41 and 51 words). Split it. Define verl ("an RL fine-tuning library"). Move the crowd-recruitment clause into E2. Define the predicted-human fitness term (formula and weight).
47. L191. Define "LLMTime-style serialization" (fixed precision, digits separated by spaces, values separated by commas).
48. L199 (142 words). Put the normalized-error definition here if it is not in Key ideas. Split after "input tokens".
49. L203, E1. Define the Pareto front in one clause here.
50. L207 (46 words). Split it. Say which eight checkpoints.
51. L219, E5 (100 words). A 3 by 2 table (display: marks, values printed in the image, text; derived quantities: on, off) would replace two long sentences and make the presentation and computation contrasts readable at a glance.
52. L227. Delete E7.
53. L235. The citation does not support the stated rationale. "Every loop runs at least five seeds, because ... the selected candidate inherits a winner's curse [34]": Hu and Tang's remedy for the winner's curse is rescoring on held-out items, not more seeds. Write: "The selected renderer's dev-select score is optimistic, a winner's curse [34], so every reported gain is rescored on sealed participants; five seeds estimate run-to-run variance."
54. L237. Write the H1 decision rule from Change 5. Say what is refit in each leave-one-reader-out fold, given that the rule is registered and has no reader-specific parameters apart from $c_d$.
55. L241 (53 words). Split it after "five families".
56. L243 (two 42-word sentences). Split each.
57. L247 (46 words). Split it after the parenthesis.

**How to read the results**

58. Add rows for "H2 falsified (channel weights do not move toward $A$'s strong channels)" and "H3 falsified (the same-family pair transfers as well as the cross-family pair)". Schaeffer et al. [23] found that ensembles of similar models improved transfer to similar targets, so the second outcome is plausible and worth a planned response. Move "A measured perceptual gap is negative" (L258) to Method as a diagnostic, since it is not a result about a hypothesis. At L255, change "reader-specific code" to "private dialect". At L259, "Co-adaptation yields a private dialect that a cheap constraint prevents" reads as a slogan; write "Co-adaptation produces a private dialect, and a frozen-reader term prevents it."

**Compute, data and scope**

59. L266. Say which two decisions enter fitness. L274: StaBLE trials last up to about 30 seconds, while the pilot timing is 3.8 minutes for a 17-second clip, which scales to about 6.7 minutes for a 30-second trial. State the mean clip length behind "5 minutes each". L268: Qwen3-Coder-480B-A35B on 8 H100s needs FP8 weights (480 GB at FP8, 960 GB at BF16, against 640 GB of HBM); say so. Drop the 150 hours for E7.

**Risks and limitations**

60. "Approximate signatures" (L282) repeats the Ablations sentence about two oracle architectures. "Power, a reused cohort and few readers" (L284, 47 words) repeats Data and Statistical analysis. Merge both into one line each.

**Where to learn more**

61. Item 2 (Time Series) is only loosely tied to this proposal; drop it or cut it to one clause. Trim every item to one clause.

**References**

62. [9]: "Ma et al." lacks initials. Write "Ma D, Chen S, Yang Y, et al." (verified on arXiv).
63. [34]: the title is truncated. The full title is "The Winner's Curse in LLM Self-Improvement Loops: Selection Noise, Lock-in, and Acceptance Rules".
64. Notation pass across Method and Experiments: apply Change 4 globally ($r$ for renderers, Q1 to Q5, $X$/$A$/$B$ for readers, "checkpoint", "frozen-reader term").

**LLM tics found (STYLE.md list)**

- L61: "We claim neither that plots beat numbers, nor a first VLM battery, nor the machine-reader question itself" is a groomed triad of negations. Rewrite as in item 22.
- L95: "The identity telescopes, and its content lies in the signs" is an aphorism. Rewrite as in item 30.
- L54: "Profiles are descriptive and predict nothing" is a slogan (item 20).
- L259: "Co-adaptation yields a private dialect that a cheap constraint prevents" is a slogan (item 58).
- L119: "it lowers $P$ by doing the reader's work" is mild personification and optional (item 34).
- L5: "it can neither be reused ... nor checked ..." is a balanced neither/nor. It is acceptable; recasting it is optional.
- The automated checks found no em-dashes or en-dashes in the text or the SVGs, no banned words, no intensifiers, zero uses of "rather than", "instead of" or "as opposed to", no staccato runs, and no `\operatorname`. The proposal and figures do use U+2212 minus signs in numbers, which is correct.

---

## 3. Cut list (target at or below about 5,900 by `audit_doc.py`)

Current count: 6,297. The clarity additions above cost about +250 words net: the Change 2 paragraph +75, the gain table and equation +60, the participant table +20, normalized error and reader-set names +40, the roadmap +45 and small definitions +10. To land near 5,850, cut about 700 words. Estimates come from counting the passages with the audit's tokenizer, which also counts LaTeX command names such as `mathrm` as words.

| # | Passage | Action | Saves |
|---|---|---|---|
| 1 | E7 and the encoding-as-action arm: L163 last sentence (30), L227 (22), "the encoding-as-action policy needs about 150" in L271 (8) | Delete. It serves no hypothesis, and it also saves 150 H100-hours | 60 |
| 2 | L47 narrative before the table | Compress to one sentence (item 18) | 30 |
| 3 | L61: "Missing are ..." sentence (36) and the triad (25) | Delete the first; replace the second with the shorter version (item 22) | 45 |
| 4 | L95: log-loss and $\mathcal V$-information sentence (46) | One clause | 30 |
| 5 | L101 (168) | Restructure; drop the repetition of "upper bound" and the decoder-agreement clause, which the Ablations already state | 50 |
| 6 | L103 (97) | Drop the build path and tighten | 20 |
| 7 | L33: information-matching sentence (23) | Delete or move into L101 | 20 |
| 8 | L35 paragraph | Replaced by the gain table (counted in the additions) | 40 |
| 9 | L37 (79) | Split and drop the Pareto definition (moved to E1) | 15 |
| 10 | L169 (212) | Replaced by the participant table plus three sentences | 90 |
| 11 | L183: "Figure 5 shows the fitness conditions ..." (49) | Keep the same-family clause; move recruitment to E2; drop what the caption says | 25 |
| 12 | Figure 7 caption: "Reader groups alone would also order these points ..." (23) | Delete once the figure plots centered gains (Figure review) | 20 |
| 13 | Compute (461) | Convert the per-line arithmetic to a five-column table (item, count, unit cost, hours, assumption); drop repeated "about" and "at an assumed" | 110 |
| 14 | Risks (213) | Merge "Approximate signatures" and "Power ..." (item 60); drop "Reader availability", already handled in Models | 55 |
| 15 | Where to learn more (225) | One clause per item; drop item 2 | 60 |
| 16 | How to read: "negative gap" row (17) | Move to Method as one clause (the two new rows are counted in the additions) | 10 |
| 17 | Second domain (84) | Tighten the parenthetical and the split rule | 15 |
| 18 | Box, ML contribution (52) | Shorter version (item 3) | 7 |
| | **Total** | | **about 700** |

---

## 4. Scientific review (ICML format)

### Summary

The proposal studies an agent that evolves the plotting code used to show its own tool outputs (RTMPose keypoints and OpenCap Monocular center-of-mass paths for StaBLE balance tasks) to a VLM reader. It asks whether a graphical-perception battery, run on each reader before the search, can forecast how much of the evolved renderer's gain transfers to other VLMs and to people. Each reader's risk is split into a tool floor, an information term (what the encoding discards) and a perceptual term (the reader's excess over the best decoder of the image), with the perceptual term further split into calibration and resolution. Trained oracles estimate the floors. Renderers evolve through AlphaEvolve and GEPA-style mutation in a MAP-Elites archive under single-reader, same-family and cross-family fitness. A no-glyph grammar and a factorial E5 separate computation from presentation, and a co-adaptation arm tests for a private dialect using a cross-seed matched-pair design. The primary test (H1) is a registered leave-one-reader-out rank correlation between forecast and observed renderer-centered gains, compared against family-and-size and three other predictors. A replication runs on TimerBed and a synthetic anomaly suite. The budget is about 4,800 H100-hours.

### Strengths

1. The primary claim is a forecast, registered and time-stamped before held-out scoring. It is compared against named alternatives, including the obvious family-and-size baseline. This is a better design than a post-hoc transfer table.
2. Leakage control is unusually thorough. It includes participant-level splits, normalization recomputed on development people, held-out tasks excluded from every development use, disclosure of the reused sealed cohort, sensitivity to the exemplar-video participants, and a permuted-label run that would flag a leak.
3. The risk decomposition is principled: $I\ge0$ follows from data processing, and $P\ge0$ holds whenever the reader sees only the encoding. The proposal is candid that empirical oracles are biased upward, and it shows the failure mode in a simulation whose numbers I checked against `d_decomposition_results.json`.
4. E5 crosses fixed transforms with display type, which directly answers the obvious objection that a "perceptual" gain is computation in disguise.
5. The co-adaptation arm has the controls that most drift studies lack: a renderer-only cost, reader-only fine-tuning at equal compute, and a cross-seed matrix that identifies a pair-specific effect beyond the main effects.
6. The compute arithmetic is itemized and internally consistent. I re-summed the items to about 4,825 H100-hours.

### Weaknesses, each with a fix

**W1. The H1 inference rests on few readers, and its decision rule is ambiguous.** At most ten held-out readers in five families support a leave-one-reader-out correlation. The power arithmetic counts 20 runs as units, which the text itself says is the wrong unit. "At least 0.5" could be a point estimate or a bound.
*Fix:* State the rule as in Change 5. Run the registered simulation with readers as the unit and report its power in the text. Add cheap open readers to raise the count toward 15 to 20: other Qwen3-VL sizes (4B, 30B-A3B) and other open families of 7B to 12B. Each costs a few H100-hours of scoring, and the cost is dominated by the 250 hours of held-out scoring already budgeted.

**W2. Two comparators are weak or underspecified once gains are renderer-centered.** When floors are pooled, $\Delta I_B$ is shared across readers, so the information-only predictor $\hat G_B=\Delta I_B(r)$ is nearly constant within a renderer and its centered correlation is close to zero by construction. The family-and-size predictor has no stated model or fitting procedure.
*Fix:* Specify every comparator as a model fitted inside the same leave-one-reader-out folds on the same centered cells. Replace the information-only comparator with one that keeps variance within a renderer, for example the mean transfer of each reader across all other renderers.

**W3. The three-way split mislabels computation.** Section 1, Change 1 covers this. The proposal's own L119 places computation in $\overline{\Delta P}$, but the box and L23 present the split as information, shared perception and exploitation, and $S_A$ is never tied to the terms.
*Fix:* The four-row table, the three-term equation and the identity $S_A=(\Delta P_A-\overline{\Delta P})/G_A$.

**W4. The predictor is underspecified at exactly the points that decide whether it can be registered.** Four pieces are missing: the form of the "two-parameter" resolution curve; how $m_{rk}$ is measured for a renderer; what $c_d$ is fitted on; and how the in-loop MAP-Elites descriptor (the dominant channel) is computed when knockout oracles exist only for checkpoints.
*Fix:* Items 35, 36 and 39 propose concrete definitions. Each should be written into the registration.

**W5. The battery error measure is mis-scaled.** $\log_2(|\hat p-p|+1/8)$ is defined in percentage points. With proportions it compresses all errors below about 0.1 into the floor of the 1/8 term.
*Fix:* Use percent (item 35).

**W6. "Normalized error" is undefined, and it is the fitness, the accuracy and the axis of three figures.** D1 to D4 have physical units, and D5 includes an AUC.
*Fix:* Define it as in Change 3, keep AUC out of the fitness average, and name the two fitted decisions.

**W7. The H3 target set is tiny and does not match the figure, and the baseline inflates transfer.** H3 evaluates "readers outside every fitness condition (the closed VLM and the crowd panel)", which is one VLM and one human panel. A lower 95% bound above 0.8 on that set is fragile. The crowd profile also enters the predicted-legibility condition. Figure 6's green curve averages a different, larger set. Separately, every gain is measured against the autoscaled default plot, which discards physical scale. A renderer that only restores scale earns a large shared $\Delta I$ and a transfer ratio near 1 trivially. Finally, Schaeffer et al. [23] found that ensembles of similar models, not dissimilar ones, improved transfer to similar targets, and the proposal does not engage with that opposite prediction.
*Fix:* Define never-fitness readers as Qwen3-VL-32B, Gemma 3 4B and 27B, the larger InternVL3.5, the closed VLM, the crowd and the clinicians, excluding the crowd for the predicted-human arm. Use that set in H3 and Figure 6, stratified by family. Report H3 on the perceptual transfer $\Delta P_B/\Delta P_A$ as well as on $T$, or against the stabilogram baseline. Add Schaeffer et al.'s prediction to the outcome table.

**W8. The co-adaptation fresh set mixes families, and the predicted-human fitness term is undefined.** $\mathcal F$ includes Qwen3-VL-32B, which shares $A$'s family, so a dialect specific to that family could inflate or mask $D_t$. The legibility row of Figure 5 has no formula.
*Fix:* Report $D_t$ by family, and give the predicted-human term's formula and weight (Change 4).

**W9. The roles of BioCV and the held-out tasks are inconsistent between the text and Figure 4.** The text cross-fits BioCV by person; Figure 4 lists it under post-search held-out tasks.
*Fix:* State that BioCV enters only after the search (oracle floors cross-fitted within it), or remove it from the figure.

**W10. Scope.** Five hypotheses, seven experiments and two co-adaptation conditions dilute a primary result that rests on about ten readers. E7 serves no hypothesis.
*Fix:* Drop E7, and label E6 as secondary in the box and the outcome table. Spend the saved compute on more readers (W1).

### Questions for the authors

1. How is each child's MAP-Elites descriptor computed during search if knockout oracles are fit only for checkpoints?
2. What is the functional form of $\sigma^2_{Xk}(m)$, and how is $m_{rk}$ measured on a renderer?
3. Is $c_d$ fitted on reader $A$ alone, or on every reader's default-plot error on development people? If the latter, held-out readers' development data enter the forecast; that is allowed, but it should be said.
4. What is refit in each leave-one-reader-out fold, given that the rule is registered?
5. Which two decisions enter fitness, and how is normalized error defined for D4 (ms) and the D5 flag?
6. For people, gains are computed on pairwise "which sways more" judgments. Is H1 tested on VLM cells and human cells together or separately, and does the pairwise judgment correspond to D1 only?
7. Is BioCV ever seen by the search, the oracles or the battery?
8. Which three StaBLE tasks are held out, and is the running example (tandem stance) among them?
9. Why should a dissimilar pair beat a similar pair, given Schaeffer et al.'s finding that ensembles of similar models transfer better to similar targets?

### Scores

- Soundness: **3** (good). The design is careful and its controls are well chosen. The underspecified predictor pieces (W4), the mis-scaled battery error (W5) and the small reader set (W1) are fixable before registration.
- Presentation: **2** (fair). The content is complete, but terms come before their definitions, the notation is overloaded, and the central concept is scattered (Changes 1 to 4).
- Contribution: **3** (good). A registered cross-reader forecast for agent-designed observations is new and useful well beyond biomechanics. The decomposition and the drift test are well-motivated extensions of known ideas.
- Overall: **6** (weak accept as a proposal). It would be a 7 once W1 to W4 are fixed and the presentation changes are made.
- Confidence: **4**. I checked the arithmetic, the simulation numbers and eight citations. I did not read every cited paper in full.

---

## 5. Citation spot-check (8 load-bearing citations, each link fetched once)

| Ref | Link fetched | Entry matches? | Claim in the proposal | Verdict |
|---|---|---|---|---|
| [5] Daswani et al. | arxiv.org/abs/2410.02637 (and the HTML for the conclusion) | Yes: title, first three authors, arXiv 2024 | "Plots beat text ... by up to 150% on consumer-health tasks, at up to 90% lower cost"; "best plotted form and its automation are left to future work" | Supported. The abstract gives "up to 150% ... on real-world tasks" (fall detection, activity recognition, readiness) and "up to a 90% reduction in model API costs". Section 5 says they "do not rigorously study what the optimal plotted form ... might be" and that it "could in theory be automated and forms the basis for future work". |
| [6] By My Eyes | aclanthology.org/2024.emnlp-main.133 and arXiv 2407.10385 HTML | Yes: EMNLP 2024, five authors | "A model picks among 16 plotting functions by rating its own plots, about 10% gain" | Mostly supported. The 16 functions and the roughly 10% gain (15.8 times fewer tokens) are correct. The MLLM filters the tools and then **chooses** the single plot that "provides the best visual information"; it does not rate plots. Change "rating" to "choosing among" (item 19). |
| [7] VL-Time (Liu, Liu, Prakash) | aclanthology.org/2025.naacl-long.383 | Yes: NAACL 2025 | "About 140% average gain with 99% fewer tokens"; TimerBed as the second domain | Supported. The paper reports "about 140% average performance improvement" and "99% average token costs reduction", and describes TimerBed as a time-series reasoning testbed with real-world tasks. |
| [9] Ma et al. | arxiv.org/abs/2606.14061 | Partly: the venue (ASE 2026) and the ID are right, but the entry gives no author initials | "cut input tokens by up to 26% at equal or better accuracy, while vision-only views hurt" | Claim supported. Fix the entry to "Ma D, Chen S, Yang Y, et al." (item 62). |
| [20] Dubey et al. | arxiv.org/abs/2610.35077 | Yes: five authors, October 2026 | "Evolving the program around a frozen VLM raised chart-question exact match from 16.6% to 41.3%"; "The chart is fixed input" | Supported in substance. The abstract says "average accuracy" (three VLMs, four benchmarks) and says the VLM is frozen. "Exact match" is not in the abstract, so use "average accuracy" unless the body says exact match. The abstract does not say explicitly that charts are fixed, but it describes evolving only the inference program, which is consistent. |
| [21] Mihai and Hare | NeurIPS 2021 proceedings page and arXiv 2106.02067 HTML | Yes | "Sketches trained on a partner's success were hard for people to read until an inductive bias was added"; "already tested on people" (L61) | Supported, and stronger than stated. In a pilot human study (Table 5; six participants, 150 games each), humans identified game-loss-only sketches 8.3% of the time (chance 10%), against 38.3% with the added perceptual loss. The proposal could quote these numbers in the table. |
| [23] Schaeffer et al. | arxiv.org/abs/2407.15211 | Yes. The arXiv page lists NeurIPS 2024 workshops; the ICLR 2025 venue is confirmed in the research notes through mlanthology | "Images optimized against one VLM rarely transfer beyond near-identical models" | Supported. One omission matters for H3: the paper also finds that attacking larger ensembles of **highly similar** models improves transfer to a specific target, which predicts the opposite of H3's direction for same-family targets (W7). |
| [34] Hu and Tang | arxiv.org/abs/2610.09239 | Title truncated; the full title adds ": Selection Noise, Lock-in, and Acceptance Rules" | "Every loop runs at least five seeds, because ... the selected candidate inherits a winner's curse" | The winner's curse claim is supported (selection-set gains overstate held-out gains, including for GEPA). The stated remedy is not: the paper's remedy is rescoring on held-out items, not running more seeds. Reword (item 53) and fix the title (item 63). |

No link was broken and no reference pointed to the wrong paper. The two content mismatches ([6] "rating" and [34] seeds as the remedy) and the one wording mismatch ([20] "exact match") are small, and each is fixed by one wording change.

---

## 6. Figure review

Rendered with `render.py`; `lint_svg.py` reports no overlap, off-canvas or line-through-text warnings. Word counts per figure are 48 to 119.

**Figure 1, `one-output-four-encodings` (round-3 fixes checked).** The round-3 fixes landed: the badge reads "scale kept, timing lost" and the "1 cm" label is enlarged and readable. The figure makes its point at a glance. Two problems remain. (a) The title, "One tool output, four ways to show it", is not true of the figure. The printed row shows RTMPose keypoints (61,200 numbers), while the other three show the OpenCap CoM path, so the token contrast compares different data. This differs from the declined round-3 request for connector labels: it concerns the logic of the comparison, not labelling. Fix: either print the CoM path in the text row (1,800 frames by 2 coordinates, roughly 15,000 to 20,000 tokens) and put the keypoint count in a footnote, or retitle the figure "One trial, four ways to show its tool outputs". The first option is better, because it makes the four rows comparable. (b) "ellipse 6.2 cm2" should read "cm²". The caption should say that image costs are for Qwen3-VL, since Gemma 3 and InternVL3.5 count tokens differently. The caption otherwise explains what to look at and matches the text.

**Figure 2, `risk-decomposition` (round-3 fixes checked).** The round-3 fixes landed: "best possible render decoder", larger subscripts, and the new subtitle. The figure makes one clear point and matches the equations. The segments run resolution then calibration, which is consistent with L97. Changes: crop about 25% of empty canvas below the labels (the figure is 900 units tall with nothing below y of about 540), and have the L35 text mention resolution before calibration so prose and figure read in the same order. Ship after the crop.

**Figure 3, `oracle-learning-curve`.** Clear and correct; the plotted values match `d_decomposition_results.json` (oracle risk 0.063 at 200 renders, estimated gap −0.049, 0.0079 at 5,000 renders, true gap 0.0087). One change: add "toy bar plot 20 px tall; k-nearest-neighbour oracle" to the subtitle or the caption. As it stands, a reader thinks of CoM traces and of the convolutional oracle described in Key ideas. Ship otherwise.

**Figure 4, `renderer-evolution-loop` (round-3 fixes checked).** All three round-3 fixes landed: "parent code" sits on one line, the boxes read "errors vs dev-train labels" and "error vs dev-select labels", and the rule under "Post-search scoring" spans all three cards. The loop reads clearly. Remaining issues: (a) the "Held-out tasks" card lists BioCV, which conflicts with the five-fold cross-fitting at L169 (W9); (b) the error tables also contain the in-loop probe's errors (L135), so write "reader A and probe errors vs dev-train labels"; (c) label the mutator-to-renderer arrow "child code" so it pairs with "parent code"; (d) for two-reader conditions, add one caption clause such as "in two-reader conditions, two readers each score half of dev-select". Fix (a) and (b).

**Figure 5, `reader-design-matrix`.** Clear; shape coding works in grayscale, and the rows match the text. Changes: (a) "clinic" should read "clinicians"; (b) mark the never-fitness columns (Qwen3-VL-32B, Gemma 3 4B and 27B, InternVL3.5 larger, Closed, People) with a light header band labelled "never in fitness", so the H3 target set is visible (W7). Ship after (a); (b) is strongly recommended.

**Figure 6, `transfer-decomposition-curve` (round-3 fixes checked).** The round-3 subtitle (which gives the denominator) works, and the bracket percentages match the plotted endpoints (0.90 against 0.41 gives 55%; 0.78 against 0.695 gives 11%). Three problems remain. (a) The new title, "Predicted transfer to held-out VLMs improves with ensemble fitness", uses "predicted". In this proposal that word means the profile predictor's forecast $\hat G$, so a reader may take the curves for forecasts. Write "Hypothesized: ensemble fitness keeps more of the gain for held-out VLMs", or start with "If H2 and H3 hold". (b) The green set ("VLMs outside both fitness sets") does not match H3's target set, and the right panel does not name its pair. Name the pair (for example Qwen3-VL-8B plus Gemma 3 12B) and plot the never-fitness readers defined in W7. (c) The y-axis reaches 0.9 "gain over default plot" in normalized error. The pilot errors are 0.12 to 0.24 on the task-score scale, so a gain of 0.9 is impossible under any plausible definition and will confuse a reader who remembers L21. Once normalized error is defined (Change 3), either rescale the axis to a plausible range or plot "fraction of reader A's generation-40 gain". Fix.

**Figure 7, `profile-predicts-transfer`.** It shipped in round 2, but it illustrates the wrong statistic. The registered H1 test centers gains within each renderer, and the caption admits that "reader groups alone would also order these points". So the scatter shows the very pattern the test is designed not to count, and it shows near-perfect agreement (r about 0.97), where H1 asks for a rank correlation of at least 0.5. Fix: plot renderer-centered observed against renderer-centered forecast gains (both axes around 0). Draw an illustrative cloud with Spearman correlation about 0.6, and optionally overlay the family-and-size predictor's points in gray to show what "beats" means. That also lets the second caption sentence go (cut list item 12). Rescale the axes once normalized error is defined. Fix.

**Figure 8, `co-adaptation-drift`.** Clear, and it matches H5: the gap closes from 0.42 to 0.12, which is more than half, and the fresh readers rise from 0.41 to 0.64. The caption correctly says that a gap alone does not show a private code. The only issue is the scale: an accuracy of 0.6 at round 0 means a normalized error of 0.4, which is worse than the pilot's constant baseline. Rescale once normalized error is defined. Ship.
