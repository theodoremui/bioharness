**Role**: You are a legendary AI/ML researcher and master at producing breakthrough research papers and contributing significant discoveries to the scientific community.

**Task**: Update the proposal writeups in `docs/idea-summaries`.

Ultrathink on 4 new research directions to have top-tier novelty and significance scores (roughly 4.5 to 5 out of 5). They should be highly promising and different from the previously generated ideas or what you have seen before that has not worked.

Deeply brainstorm from current research and related work from authoritative sources like arxiv and top conference papers (ICLR, ICML, NeurIPS, CVPR, ACL, etc.) on recursive self improvement and agent behavior / tool selection. This should be helpful for optimizing tool calls for biomechanical tasks, but you should generalize to broader agentic use cases.

You must leverage your rich background knowledge and reasoning capabilities to choose ideas and research directions that have great potential to contribute a new and useful piece of machine learning or AI knowledge.

Your goal is to select research routes that propose unique and interesting ideas related to agents and VLMs for biomechanics. You must not simply reuse the same methodology patterns or experiments as prior related work. You must also clearly identify the ML contribution, and it should be in an area niche enough that a significant chunk of people are not already working on the problem, and broad enough that it could generate meaningful scientific impact.

You should output your writeups as proposal documents in `docs-idea-summaries`. Your proposals should be as well-documented and clear as possible. Make sure to focus on making the motivation and introduction super specific and highlighting the main problem and research question. You should also put extra effort into making your methods and experiments section detailed and thorough. Reference specific models, techniques, and technical concepts. Each proposal should be easy to read and understand, as well as guide the reader to feel comfortable and confident with the idea. Describe specific modules in https://usaaio.guide/, https://uvadlc-notebooks.readthedocs.io/en/latest/, Stanford CS329Z (https://cs329z.stanford.edu/), or Stanford CS329A (https://cs329a.stanford.edu/) where the reader can learn more about topics in the proposed research direction.

Illustrate frequently and abundantly with vector graphics and flowcharts to illuminate ideas and concepts -- saving the images in the "images" subfolders. Use codex:adversarial-review of your generated vector graphics and workflow to ensure that they are not cluttered, and that no excessive text or line overlaps. Each generated image should be easy to understand and with minimal clutter.

After your careful revision, thoughtfully consider how you could make the revision even better and clearer with concrete and specific suggestions. Based on these suggestions, thoroughly and systematically revise the draft to a final version that greatly improves the readability and conceptual clarity of the different proposals. Provide clear and referenceable citations to key papers from arxiv and other authoritative sources. Do not use em-dashes in your writing.

Fan out subagents. Use dynamic workflow orchestration.

---

Carefully and systematically move proposals 05 through 08 in `docs/idea-summaries` into a new folder, `docs/research-plans`. The file `docs/idea-summaries/README.md` should be renamed to `research-overview.md`, and act as an index linking across all eight proposals.