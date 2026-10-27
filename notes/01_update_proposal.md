**Role**: You are an expert AI/ML researcher specializing in frontier agent research and vision-language models (VLMs).

**Task**: Based on the latest proposal in `output/research-codex/biomechanical_agent_proposal.md`, fully and systematically analyze and grade it using a thoughtful and appropriate multi-dimensional score, along with specific critiques as well as concrete suggestions on how to improve. The goal is to iterate the paper and make it strongly relevant and compelling to the International Conference on Machine Learning.

Iteratively create 7 versions of the proposal without overriding by thoughtfully incorporating each of the successive versions' critique and suggestions. Each version must improve upon previous versions by carefully reviewing and selecting the most appropriate techniques, inferences, and experiments using creative and insightful analysis of novel machine learning methods to enhance the capabilities of agent harnesses and tool-calling VLMs, as well as any relevant literature from authoritative sources such as ArXiv, along with the following documents:

* `./../../Downloads/nmbl/Biomechanical Agent.pdf`
* `./../../Downloads/nmbl/NMBL Lab Meeting Oct 20 2026 - Learning to Conduct Biomechanical Analysis [FINAL].pdf`
* `../../../Downloads/nmbl/stable_paper.pdf`

 Be thoughtful and strategic in what to select and what to ignore in order to create an ever more compelling, cogent, and intellectually relevant paper.

To illustrate the data processing pipeline, thoughtfully create a modern, clean, and simple illustration using vector graphics of the training pipeline. Use best UI/UX design skills for your vector graphics.

Provide 7 suggestions of relevant titles that reflect the objective of the proposal. For the abstract, stay strategic without dwelling on and over-emphasizing numerical or other irrelevant details of different stages of the processing and experiments. Save your scores, suggestions, and critiques of each revision in the file: `output/research-claude`. Each revision of the proposals should also be saved in `docs/ideas-claude` with thoughtfully useful filename with version number.

For each proposed idea, the writeup should be succinct, well-structured, compelling, and specific. It should describe in well-supported detail what the research question is, related works, and potential methods and experiments. The research question must be specific, measurable, achievable, relevant, and time-bound. Ultrathink on how to simplify the language and explanations to make each proposal much, much easier to understand. Start from first principles and fully explain all concepts and how they inter-relate with each other.

## Writing Style
Your writing should be natural, fluent, grounded, and easy to understand and to follow. Avoid common LLM styling and characteristics in your response. Fully explain any technical jargon in clear, simple terms. The introduction should provide good motivation on why you are using agent harnesses and/or VLMs. For each step of the methodology, highlight how the training preserves the exact shape of the dataset, how you split between training and testing, to avoid leakage of the training dataset into testing and ensure rigorous statistical inference on any results.

Provide a logical story arc that maps from motivation, hypothesis, testing, evaluation, and rinse and repeat many times through this intellectual journey of trying to improve agent performance through fine-tuning, prompt optimization, reinforcement learning, harness evolution, world models, or other approaches that you come up with.

Use codex:adversarial-review to carefully and thoughtfully review your proposal writeups and propose suggested changes. Based on these suggestions, systematically revise the proposals and address all feedback.

## Avoidance
Your output must avoid common LLM output styling and characteristics:

* Staccato drumbeat sentences: short sentences
* Excessive aphorism
* The "it is not X, it is Y" correction reflex that is highly correlated with LLM outputs. This antithesis pattern appears throughout at high density.
* Recycled pivot phrases. A human author usually notices near-verbatim self-repetition ten lines apart; models reaching for a favorite transition do not.
    * "Confidence tells the same story from a different angle"
    * "The concurrency tier tells the same story from a slightly different angle"
    * "What looks like an architecture effect is noise"
* Intensifier tics: too many repeated adverbs such as: "Actually" or "exactly".
* Anthropomorphic phrasing throughout.
* Many groomed triads: examples:
    * "Real, sharply structured, and immune to the standard fixes."
    * "Never the oracle, never the operator, and never which arm of the pair."
* The suspicious absences of em-dashes "--", and zero instances of the classic AI lexicon (delve, leverage, robust, comprehensive, landscape, underscore). Most human ML writers use a dash or the word "robust" at least once.
