**Role**: You are an expert AI/ML research scientist specializing in agent behavior, tool selection, and the evolution and optimization of agent harnesses.

**Task**: You are to deeply and thoughtfully synthesize the ideas and methods in `docs/idea-summaries`. Ultrathink on how to creatively extend the proposals toward insightful new research directions. You must be grounded in hard evidence, logical reasoning, and compelling inferences.

You should carefully and systematically review each document in detail, and pay attention to the related works as well as the proposed novel and significant idea in each proposal.

After thoughtfully reviewing the documents, ultrathink on how to rewrite each document to be much more detailed, clear, and polished using concrete and compelling ideas as a framing for structuring the documents. Edit the same files in `docs/idea-summaries`. Explain all ideas, topics, and concepts using maximum clarity and natural language, as well as with fluent tone and style.

To evaluate the quality of each proposal, use codex:adversarial-review subagents as well as the official ICLR/ICML/NeurIPS reviewer guide and examples of past outstanding papers from tier 1 AI/ML conferences, arxiv, and other authoritative sources.

Your description & writeup for each proposed idea should be succinct, well-structured, compelling, and specific. It must describe in well-supported detail what the research question is, related works, and potential methods and experiments.

Illustrate frequently and abudantly with vector graphics and flowcharts to illuminate ideas and concepts, saving the images in the "images" subfolders. Use adversarial review of your generated vector graphics and workflow to ensure that they are not cluttered, and that no excessive text or line overlaps. Each generated image should be easy to understand and with minimal clutter.

After your careful revision, thoughtfully consider how you could make the revision even better and clearer with concrete and specific suggestions. Based on these suggestions, thoroughly and systematically revise the draft to a final version that greatly improves the readability and conceptual clarity of the different proposals. Provide clear and referenceable citations to key papers from arxiv and other authoritative sources. Do not use em-dashes in your writing.

Fan out subagents. Use dynamic workflow orchestration.

---

**Role**: You are an expert AI/ML research scientist specializing in agent behavior, tool selection, and the evolution and optimization of agent harnesses.

**Task**: Deeply synthesize the ideas and methods in `docs/idea-summaries`. Identify meaningful connections from the papers in `docs/idea-summaries/related-work.md` to the proposal ideas and creatively extend the proposals to strengthen the idea quality. You should exhaustively read the relevant papers and gain a deep understanding of what the authors tried and what can be improved or borrowed for the proposals. Ground your analysis in verifiable evidence, explicit reasoning, and well-supported inferences. Clearly distinguish established findings, reasoned hypotheses, and the primary research question of each proposal. Make sure that the central research question is scientific in nature and not merely a combination of technical jargon or engineering-esque keywords. They should concisely and precisely identify the machine learning problem and offer a deep insightful question that will be addressed in detail later in the proposal.

When you read the documents in the related works file, systematically examine its research question, motivation, related work, proposed contribution, assumptions, methods, and experimental approach. Consult the key cited sources to verify relevant claims. Identify both the strongest ideas and the gaps that limit each proposal's clarity, novelty, significance, or feasibility.

After reviewing the full collection, rewrite each document in place in `docs/idea-summaries`. Preserve its core research intent while substantially improving its depth, critical insights, organization, precision, and polish. Structure the narrative around concrete research questions and compelling ideas. Explain technical concepts in clear, natural language, define unfamiliar terms when introduced, and use specific examples where they improve understanding.

Evaluate each proposal using adversarial-review subagents, official ICLR, ICML, and NeurIPS reviewer guidance, and relevant examples of outstanding research from leading AI/ML conferences, arXiv, and other authoritative sources. Verify the guidance and sources you use. Have reviewers challenge novelty, significance, technical soundness, feasibility (we are given access to the Stanford HAIC compute cluster with NVIDIA H100 GPUs),and clarity, identifying specific weaknesses and actionable improvements. 

Each proposal should be concise in expression and substantive in detail. Clearly explain the research question, why it matters, related works, the specific gap, and the proposed contribution. Describe plausible methods and experiments with enough specificity to assess feasibility: include relevant baselines, datasets or environments, evaluation metrics, ablations, and success or failure criteria. Explain what the experiments would establish and what findings would challenge the central hypothesis. Avoid repetition, unsupported novelty claims, and detail that does not advance the argument.

Illustrate the proposals generously with vector graphics and flowcharts that clarify mechanisms, architectures, experimental designs, and relationships between ideas. Save the graphics as SVG files in the appropriate images subfolders and reference them from the documents. Give each graphic a clear explanatory purpose. Render and visually inspect every graphic, and use adversarial review to identify clutter, excessive text, overlapping labels or lines, ambiguous arrows, and unreadable typography. Revise until the graphics are easy to understand at their intended display size.

After the first revision, conduct a separate critical review of each document and develop concrete, specific suggestions for improving it further. Use those findings to complete a second substantive revision. Resolve the review findings or explicitly explain any remaining limitations. Verify that citations support the associated claims and include clear bibliographic references with stable links to the relevant papers or authoritative sources. Check that all referenced images exist and render correctly. Do not fabricate citations, evidence, or experimental results. Do not use em dashes in the writing. Make sure all included LaTeX expressions display properly without using the \operatorname{...} macro.

Fan out subagents and use dynamic workflow orchestration. Parallelize independent document analysis, literature verification, and adversarial review; assign explicit file ownership to prevent conflicting edits. Sequence dependent work so that synthesis informs drafting and independent review informs final revision. Adjust assignments as new gaps emerge, and integrate the results into a coherent collection.
