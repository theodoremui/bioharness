**Role**: You are an expert AI/ML researcher specializing in vision-language models (VLMs) and agents.

**Task**: You are to carefully read and analyze the attached presentation. Then, deeply and systematically brainstorm and generate novel methods for utilizing the tools below for the development of a general biomechanical agent:

- OpenCap, OpenSim, DynamicsNet, GaitDynamics, RTMPose, SAM2.1, CoTracker3, Video Depth Anything, NumPy, matplotlib, video + overlays

Feel free to suggest any better replacements for the proposed tools, as well as other biomechanical tools for different use cases, if it would provide a distinct, significant advantage to the agent. 

Ultrathink on exploring promising exciting new research directions in the areas of: harness and tools, biomechanics specific VLMs, co-scientists and agents.

You should use the following related works to inform your brainstorming and inspire your idea generation process:

## AGENT HARNESS LITERATURE REVIEW

We want to find an optimal way to shape model behavior and tool selection for biomechanical tasks. Fine-tuning changes the model weights, either fully or partially through low-rank adapters (LoRA). BiomechGPT shows that fine-tuning can teach clinical motion tasks. Our pilot study shows that fine-tuning can improve average error while lowering performance on clinical extremes.

Prompt optimization changes the instructions given to the model, which govern tool choice, and leaves the weights fixed. APE selects instructions by task score, OPRO iteratively generates solutions based on past candidates and scores, DSPy and MIPRO jointly optimize instructions and demonstrations across the modules of a multi-step program, and TextGrad propagates natural-language critiques backward through a computation graph. GEPA, a genetic-Pareto optimizer, reflects on execution traces to propose prompt mutations and keeps every candidate that is best on at least one evaluated example. With Qwen3-8B, GEPA beats the RL method GRPO on aggregate across six tasks, but loses on AIME-2025.

Harness evolution edits the surrounding program around an agent rather than the model or its prompts. ADAS enables the automatic design and generation of more capable agents, while AFlow searches over agent workflows using Monte Carlo tree search (MCTS). Meta-Harness gives the optimizer filesystem access to previous code, scores, and traces, and its ablations support the value of trace access within that protocol. For linking harness failures to repair, Agentic Harness Engineering attaches a testable predicted effect to each edit, and HarnessFix diagnoses recurring failures through data and control dependencies. CHILL-Harness instead attributes effects, isolating one workflow change by replaying paired executions from a shared checkpoint, given that enough agent and environment state is restored.

Reinforcement learning trains the policy that selects actions in an environment. Toolformer fine-tunes on self-inserted API calls that improve language modeling, and ToolRL shows that reward granularity (format, tool identity, arguments) shapes what is learned. Search-R1 rewards only the final answer and masks retrieved text from the policy loss, while ReTool first trains on verified code-assisted examples, then applies outcome-based RL. Agent Lightning, extended in Agent Lightning v1.0, separates the trainer from the harness, so a policy can be trained inside existing tool infrastructure.

## BIOMECHANICS & VLM LITERATURE

Literature
- Enhancing Gait Video Analysis in Neurodegenerative Diseases by Knowledge
Augmentation in Vision Language Model
- BioGait-VLM: A Tri-Modal Vision-Language-Biomechanics Framework for Interpretable
Clinical Gait Assessment
- Fine-Tuning Large Multimodal Models for Fitness Action Quality Assessment
- CoachVLM: Vision-Language Model Driven Automatic Sports Technique Assessment
and Intelligent Teaching Feedback
- Decoding Children’s Gait Behavior
- https://pediamedai.com/ChildrenGait/
- A dual-branch vision framework for interpretable balance assessment via pose dynamics
and Vision-LLM semantics
- MyoMechanix: Biomechanically-Grounded Compositional Skilled Activity Understanding
and Coaching

Use adversarial review to check and verify your brainstorming, writing, and analysis. Address and improve on all issues carefully and systematically.
