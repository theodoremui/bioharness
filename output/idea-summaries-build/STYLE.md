# Drafting guide for proposals 05 to 08

This guide is shared by every agent that drafts, reviews or revises proposals 05 to 08 in `docs/idea-summaries/`. Read it in full before writing.

## Audience and purpose

Readers are ML researchers and strong graduate students. Some know agents and RL well but not biomechanics; others know biomechanics but not recursive self-improvement. Each proposal must stand alone as a complete research idea that a reader can judge on its merits and start executing. A reader should finish it able to say, in one sentence, what question is being asked, why the answer is not already known, what experiment would answer it, and what result would prove the idea wrong.

Do not mention venues, deadlines, calendars, week-by-week schedules, version numbers, earlier drafts or reviews. Feasibility is expressed as compute cost, data access and scope.

## Required structure

Use these sections in this order. Headings may be phrased as questions where that reads better, but keep the content.

1. `# Title` phrased as the research question or a crisp claim (at most about 12 words).
2. A boxed summary using a blockquote with four bold-labelled lines: **Research question**, **Why it matters**, **ML contribution**, **What would prove it wrong**. Keep the whole box under 170 words.
3. `## The problem, in one concrete case` A running biomechanics example (a real StaBLE or BioCV task, a real tool such as RTMPose or OpenCap Monocular) that makes the failure or opportunity tangible in the first 300 words. Then generalize: show the same problem in a non-biomechanics agent (a coding agent, a data-analysis agent, a web agent).
4. `## Key ideas in plain terms` Define every term the rest of the document uses (for example harness, trace, recursive self-improvement, metaproductivity, reusable holdout, conformal risk control, graphical perception). One short paragraph per term, first-principles, no jargon left undefined.
5. `## What is known and what is missing` A short narrative plus a table with columns: Work | What it showed | What it leaves open for this question. Cite each row with a link. End with a one-paragraph statement of the gap.
6. `## Hypotheses` Numbered, falsifiable, each with the measurement that tests it.
7. `## Method` Detailed and specific: components, algorithms, equations (LaTeX, `$...$` inline and `$$...$$` display, never `\operatorname`), pseudocode where it helps (fenced code block), model names and sizes, tools, optimizers, hyperparameters that matter.
8. `## Experiments` Subsections for: data and splits (split by participant before anything else; state how leakage is prevented), models and tools, baselines (named methods with links), metrics, the core experiments (numbered), ablations and controls, statistical analysis (pre-registered primary outcome, effect size of interest, mixed-effects or paired designs, multiplicity), and a second domain outside biomechanics that tests generality.
9. `## How to read the results` A table: Outcome | What it would mean | What we would do next. Include the null and the falsifying outcomes.
10. `## Compute, data and scope` GPU-hours on H100s (Stanford HAIC), token counts for LLM calls, CPU time for tools, data access steps. Give the arithmetic.
11. `## Risks and limitations` Honest, specific, with mitigations.
12. `## Where to learn more` Specific modules (exact titles and deep links) from usaaio.guide, the UvA DL notebooks, Stanford CS329Z and Stanford CS329A, taken from `output/idea-summaries-build/research/course-modules.md`. Say in one clause what each module teaches that the reader needs here. Only list modules that the mapping verified.
13. `## References` Numbered list. Each entry: authors (first author et al. when more than three), title, venue or arXiv ID, year, stable link. Inline citations in the text use bracketed numbers that link to the reference list, for example `[3](#ref-3)`, and each reference line starts with `<a id="ref-3"></a>`. Only cite works whose links were verified in `output/idea-summaries-build/research/`. Never invent a citation.

Target length: 3,800 to 5,500 words of prose excluding references. Detail belongs in Method and Experiments. Motivation must be specific and short.

## Writing rules

- No em-dashes anywhere (no "—" and no " -- "). Use commas, colons, parentheses or separate sentences. Hyphens in compound words are fine. Avoid en-dashes too; write "5 to 10".
- Write natural, fluent, medium-length sentences. Avoid staccato runs of short sentences, aphorisms and slogans.
- Avoid the "it is not X, it is Y" antithesis and its variants; keep "rather than", "instead of" and "as opposed to" rare.
- Avoid recycled pivot phrases, intensifiers ("actually", "exactly", "truly", "crucially"), and groomed triads (lists of three parallel adjectives or clauses used for rhythm).
- Do not anthropomorphize models ("the model wants", "the agent believes"). Describe what a system computes or outputs.
- Avoid the stock LLM lexicon (delve, landscape, tapestry, underscore, pivotal, seamless). Using "robust" once is fine.
- Define each symbol when it first appears. Use one running example consistently.
- Distinguish established findings (cite), reasoned hypotheses (say so) and the proposal's own question.
- Do not report results that do not exist. Illustrative curves must be labelled "illustrative" or "hypothetical" in the figure and caption.
- Lab pilot numbers may be quoted only as "lab pilot" figures, with the caveat that they come from an internal account.

## Figures

- Draw every figure with `output/idea-summaries-build/svglib.py` (import it; do not edit it). Put your figure code in `output/idea-summaries-build/figs_0N.py` and write SVGs to `docs/idea-summaries/images/0N/` with descriptive kebab-case names.
- Aim for 6 to 8 figures per proposal: a concept figure near the top, a mechanism figure, a method or pipeline flowchart, an experiment-design figure, and others where they help (a split diagram, an outcome map, a schematic plot).
- Each figure makes one point. Keep text to short labels (aim for at most about 60 to 90 words per figure). Put explanation in the caption, not the figure. Use at most four colors with consistent meaning across your figures. Leave generous whitespace. Arrows must start and end at box edges, never cross text, and point unambiguously. No overlapping labels.
- Width 1100 to 1400 px in SVG units; the figure is displayed at roughly 850 px wide, so body labels must be at least 13 px before the library's 1.18 scale.
- Render each SVG with `python3 -B output/idea-summaries-build/render.py output/idea-summaries-build/png/0N <files>` and open every PNG with the Read tool to inspect it. Run `python3 -B output/idea-summaries-build/lint_svg.py <files>` and fix every overlap, off-canvas and line-through-text warning that is real.
- Embed with `![Alt text that states the point](images/0N/name.svg)` followed by an italic caption paragraph starting with `*Figure k.*` that explains what to look at.

## Shared facts

Dataset facts, model names and verified links are in `output/idea-summaries-build/research/biomech-facts.md`. Literature for each proposal is in `output/idea-summaries-build/research/0N-*-literature.md`, with a red-team review in `red-team.md`. Use them; do not contradict them.
