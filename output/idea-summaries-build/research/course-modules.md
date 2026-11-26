# Course module map for P05 to P08 (learning resources)

Status: COMPLETE (2026-11-24). Section 1 site status, Section 2 full module inventories, Section 3 topic mapping (18 topics), Section 4 reading paths for P05 to P08.

Rules used here. Every module title and URL below was read from the live site on 2026-11-24 (WebFetch on the index pages, plus direct download of the site's own catalog and ordering data files for usaaio.guide). Nothing was invented. Where a source title contains an em-dash, it is rewritten with a colon to follow the project style rule; this is noted in place.

## 1. Site status

| Site | Reachable | What it is |
|---|---|---|
| https://usaaio.guide/ | Yes | "USAAIO Guide, USA AI Olympiad Prep" (AIO Initiative). Lessons, worked derivations and auto-graded practice for the USA AI Olympiad, from Round 1 through Camp. 82 modules in 4 sections (Round 1, Round 2, Camp, Advanced), plus several hundred worked "theory" problems. The index pages are rendered by JavaScript; module titles were read from the site's own `content/catalog.js` and `content/ordering.js`. The sitemap lists the mirror domain https://www.aioinitiative.com/ as canonical; the same paths work on both domains. |
| https://uvadlc-notebooks.readthedocs.io/en/latest/ | Yes | "UvA Deep Learning Tutorials" (University of Amsterdam). Guides, a JAX scaling series, Deep Learning 1 (PyTorch and JAX+Flax versions), Deep Learning 2. |
| https://cs329z.stanford.edu/ | Yes | CS 329Z: Engineering AI Agents, Stanford, Fall 2026. Instructors Diyi Yang, Michael Ryan, John Yang. Each lecture has a slides PDF (web.stanford.edu/class/cs329z/slides/lectureNN.pdf, all returned HTTP 200) and most have a YouTube video. |
| https://cs329a.stanford.edu/ | Yes | CS329A: Self-Improving AI Agents, Stanford, Autumn 2025. Instructors Aakanksha Chowdhery and Azalia Mirhoseini. The schedule is a reading list per session; the page links no slides or recordings. |

Deep-link conventions.
- usaaio.guide modules: `https://usaaio.guide/module/?id=<module-id>`; worked problems: `https://usaaio.guide/theory/?id=<problem-id>`. Both returned HTTP 200 on 2026-11-24. The pages render client-side, so a text-only fetch shows only the shell; the module text itself is served at `https://usaaio.guide/content/<section folder>/<file>.md` (also HTTP 200).
- UvA: one HTML page per tutorial (URLs below).
- CS329Z: the schedule anchor is https://cs329z.stanford.edu/#schedule; the deepest per-lecture links are the slide PDFs and videos.
- CS329A: the schedule anchor is https://cs329a.stanford.edu/#schedule; the deepest per-session links are the assigned readings.

## 2. Module inventories

### 2.1 usaaio.guide (82 modules)

Format: number, code, title (exact), module URL, one-line summary (the site's own summary). Chapter names are the site's own.

**Round 1** (https://usaaio.guide/round1/): "Python, mathematics, probability, machine learning, and computer vision."

| # | Code | Title | Deep link | Covers (site summary, lightly shortened) |
|---|---|---|---|---|
| 1.23 | PY7 | Python Basics | https://usaaio.guide/module/?id=python-basics | Enough Python for every later module. |
| 1.1 | PY1 | NumPy Programming | https://usaaio.guide/module/?id=programming-essentials | Arrays, vectorized code, broadcasting and indexing. |
| 1.2 | PY2 | Pandas Data Cleaning | https://usaaio.guide/module/?id=pandas-data-cleaning-storing | Loading, cleaning and reshaping a table. |
| 1.3 | PY3 | Data Visualization | https://usaaio.guide/module/?id=plotting-matplotlib-seaborn | Clear plots with Matplotlib (sections include "Choosing the plot", "Showing uncertainty", "Checking a plot without looking at it", "Choosing a colormap"). |
| 1.4 | PY4 | Colab Notebooks | https://usaaio.guide/module/?id=colab-markdown-notebooks | Running a notebook and writing answers a grader can read. |
| 1.5 | PY5 | Scikit-Learn Pipelines | https://usaaio.guide/module/?id=scikit-learn-api-ml-pipelines | Fit, tune and score models without leaking test data (sections "Transformers and the leak", "Cross-validation", "Tuning with GridSearchCV"). |
| 1.24 | PY8 | Why PyTorch, not TensorFlow | https://usaaio.guide/module/?id=why-pytorch-not-tensorflow | The framework rule, define-by-run, and how autograd computes a gradient. |
| 1.25 | PY9 | PyTorch Tensors & Autograd | https://usaaio.guide/module/?id=pytorch-tensors-autograd | Tensor shapes, views, broadcasting, reductions, and autograd in code. |
| 1.26 | PY10 | Writing a Training Loop in PyTorch | https://usaaio.guide/module/?id=training-loop-in-pytorch | DataLoader batches, the training step, evaluation, the loop, on MNIST. |
| 1.7 | MA1 | Vectors and Matrices | https://usaaio.guide/module/?id=linear-algebra-i-vectors-matrices-systems-transformations | Dot products, matrices, rank and least squares. |
| 1.8 | MA2 | Eigenvalues and Spectral Theory | https://usaaio.guide/module/?id=linear-algebra-ii-eigenvalues-eigenvectors-spectral-theory | Eigenvalues, symmetric matrices and the SVD. |
| 1.9 | MA3 | Calculus and Gradients | https://usaaio.guide/module/?id=calculus-gradients | Derivatives, the chain rule, gradients and Hessians. |
| 1.10 | PS1 | Probability and Bayes | https://usaaio.guide/module/?id=probability-foundations | Counting, conditional probability and Bayes' theorem. |
| 1.11 | PS2 | Expectation and Joint Distributions | https://usaaio.guide/module/?id=expectations-multivariate-distributions | Expectation, variance, covariance and joint distributions. |
| 1.12 | PS3 | Statistical Inference | https://usaaio.guide/module/?id=statistics-hypothesis-testing | Estimating a parameter and saying how sure you are (MLE, MAP, confidence intervals, hypothesis tests, the bootstrap). |
| 1.13 | ML1 | Feature Engineering & Data Preparation | https://usaaio.guide/module/?id=data-processing-features | Scaling, encoding, missing values and leakage. |
| 1.27 | ML8 | Linear & Logistic Regression | https://usaaio.guide/module/?id=linear-logistic-regression | Least squares and logistic regression, by hand and in NumPy. |
| 1.28 | ML9 | Loss Functions | https://usaaio.guide/module/?id=loss-functions | Squared error, cross-entropy and hinge, and where each comes from. |
| 1.15 | ML3 | Support Vector Machines | https://usaaio.guide/module/?id=kernel-methods-svms | The maximum-margin classifier, the hinge loss and kernels. |
| 1.29 | ML10 | Decision Trees & k-Nearest Neighbors | https://usaaio.guide/module/?id=decision-trees-knn | Nearest neighbors and decision trees, by hand and in scikit-learn. |
| 1.16 | ML4 | Ensemble Learning | https://usaaio.guide/module/?id=tree-based-models-ensembles | Bagging, random forests and boosting. |
| 1.17 | ML5 | k-Means Clustering | https://usaaio.guide/module/?id=clustering | Lloyd's algorithm, k-means++ and choosing k. |
| 1.31 | ML5 | Clustering Methods | https://usaaio.guide/module/?id=clustering-methods | Centroid, single-linkage and density views of clustering. |
| 1.18 | DL1 | The Multilayer Perceptron | https://usaaio.guide/module/?id=neural-networks-perceptrons-mlps-activations | Neurons, layers, activation functions, a digit reader. |
| 1.19 | DL2 | Core Layers (Affine, Normalization, Dropout) | https://usaaio.guide/module/?id=neural-network-regularization-dropout-batchnorm | Batch norm, layer norm and dropout, by hand and as nn.Module layers. |
| 1.21 | DL4 | Optimizers & Training Tricks | https://usaaio.guide/module/?id=optimization-adam-sgd | Momentum, Adam, weight decay, schedules, early stopping, initialization. |
| 1.30 | CV7 | Convolutional Neural Networks | https://usaaio.guide/module/?id=convolutional-neural-networks | Convolution, receptive field, a small CNN, residual blocks, frozen backbones. |

**Round 2** (https://usaaio.guide/round2/): "Backpropagation, model evaluation, computer vision, and transformers."

| # | Code | Title | Deep link | Covers |
|---|---|---|---|---|
| 2.15 | MA6 | Forward Propagation | https://usaaio.guide/module/?id=forward-propagation | The forward pass by hand and as a NumPy loop, with the cache backprop needs. |
| 2.1 | MA4 | Backpropagation by Hand | https://usaaio.guide/module/?id=backpropagation-mechanics | The chain rule as one backward sweep, worked on a small network. |
| 2.3 | ML6 | Classification Metrics | https://usaaio.guide/module/?id=model-evaluation | Confusion matrix, precision, recall, F1, AUC; "Are the probabilities trustworthy?" (calibration). |
| 2.16 | ML11 | Bias-Variance Tradeoff & Cross-Validation | https://usaaio.guide/module/?id=bias-variance-cross-validation | Where test error comes from and how to estimate it (the split, k-fold CV, more data). |
| 2.17 | ML12 | Principal Component Analysis | https://usaaio.guide/module/?id=principal-component-analysis | PCA from the covariance matrix and the SVD. |
| 2.18 | ML13 | Nonlinear Dimensionality Reduction: t-SNE and UMAP | https://usaaio.guide/module/?id=nonlinear-dimensionality-reduction | t-SNE and UMAP, and how to read their plots. |
| 2.19 | ML14 | Semi-Supervised Learning | https://usaaio.guide/module/?id=semi-supervised-learning | Pseudo-labeling and label propagation with few labels. |
| 2.20 | ML15 | Time Series | https://usaaio.guide/module/?id=time-series | Windows, time-ordered evaluation and forecasting; leakage from shuffled folds; classifying whole series. |
| 2.5 | DL5 | Convex Optimization | https://usaaio.guide/module/?id=advanced-optimization | Gradient descent, convexity and Lagrangian duality. |
| 2.6 | DL5 | Advanced Optimization | https://usaaio.guide/module/?id=advanced-optimization-methods | Why an optimizer makes progress or stalls, on simple objectives. |
| 2.21 | CV8 | 1. Setup and pixels | https://usaaio.guide/module/?id=vision-setup | The image classification task; an image as numbers. |
| 2.23 | CV10 | 2. Convolution and pooling | https://usaaio.guide/module/?id=vision-convolution | Convolution filters, ReLU and pooling. |
| 2.25 | CV12 | 3. Classifying, going deeper and transfer learning | https://usaaio.guide/module/?id=vision-classify | Classifier head, residual depth, reusing a trained network. |
| 2.28 | CV15 | Hierarchical vision models: Swin, ConvNeXt and compound scaling | https://usaaio.guide/module/?id=hierarchical-vision-models | Backbones that move information across space affordably. |
| 2.7 | CV3 | 4. Segmentation and adversarial attacks | https://usaaio.guide/module/?id=semantic-segmentation-unet-masks | U-Net segmentation; gradient-based adversarial attacks. |
| 2.8 | CV4 | ResNets and Transfer Learning | https://usaaio.guide/module/?id=modern-vision-architectures-resnet-efficientnet-transfer | What to freeze, what to train, and when to doubt the transfer. |
| 2.30 | TF10 | 1. Setup and input | https://usaaio.guide/module/?id=transformer-setup | Next-token task; text to token IDs, vectors and positions. |
| 2.34 | TF14 | 2. Attention scores | https://usaaio.guide/module/?id=transformer-qkv | Queries, keys, values, the causal mask and softmax. |
| 2.37 | TF17 | 3. Attention output | https://usaaio.guide/module/?id=transformer-weighted-sum | Weighted sum of values; multiple heads. |
| 2.39 | TF19 | 4. The Transformer block | https://usaaio.guide/module/?id=transformer-residual-and-layernorm | Residuals, LayerNorm, feed-forward network, stacking. |
| 2.42 | TF22 | 5. Predicting and generating | https://usaaio.guide/module/?id=transformer-predict | Next-token probabilities, the loss, generating text. |
| 2.9 | TF1 | Self-Attention Fundamentals | https://usaaio.guide/module/?id=transformer-fundamentals | Attention and a full block from scratch in NumPy, with FLOP and memory cost. |
| 2.10 | TF2 | BERT and Masked Language Modeling | https://usaaio.guide/module/?id=transformer-architectures-bert-mlm | How BERT learns by filling in blanks. |
| 2.44 | TF24 | GPT and Causal Language Modeling | https://usaaio.guide/module/?id=gpt-causal-lm | Next-token prediction, the causal mask and generation. |
| 2.12 | TF4 | T5 and Sequence-to-Sequence Models | https://usaaio.guide/module/?id=transformer-architectures-t5-encoder-decoder | Encoder-decoder Transformers and text-in, text-out. |
| 2.14 | RP2 | Contrastive Learning and CLIP | https://usaaio.guide/module/?id=contrastive-learning | InfoNCE, temperature, and CLIP's joint image-text space. |

**Camp** (https://usaaio.guide/camp/): "Information theory, vision, NLP, generative models, and representation learning."

| # | Code | Title | Deep link | Covers |
|---|---|---|---|---|
| 3.1 | PS4 | Information Theory for AI | https://usaaio.guide/module/?id=information-theory-core | Entropy, cross-entropy, KL divergence, mutual information. |
| 3.3 | CV6 | 5. Vision Transformer and object detection | https://usaaio.guide/module/?id=vision-transformers-vit-attention | Attention over image patches; detection with boxes. |
| 3.4 | NL1 | Tokenization & Word Embeddings | https://usaaio.guide/module/?id=natural-language-processing-tokenization-embeddings | WordPiece, Unigram, byte-level BPE, word2vec, GloVe. |
| 3.14 | NL3 | Pre-training & Fine-tuning | https://usaaio.guide/module/?id=pre-training-fine-tuning | Pretraining objectives, fine-tuning, transfer. |
| 3.5 | NL2 | Recurrent Networks: RNN, LSTM, GRU | https://usaaio.guide/module/?id=sequence-models-transfer-learning | Recurrence, BPTT, vanishing gradients, gates, "From recurrence to attention". |
| 3.6 | TF5 | Retrieval-Augmented Generation | https://usaaio.guide/module/?id=rag-retrieval-embeddings | Letting a language model look things up. |
| 3.7 | TF6 | Positional Encoding and RoPE | https://usaaio.guide/module/?id=relative-position-rope-positional-methods | Relative encodings, RoPE, context stretching. |
| 3.8 | TF7 | Vision-Language Models | https://usaaio.guide/module/?id=cross-attention-multimodal-attention | How models like LLaVA feed images to a language model (patches, projector, two-stage training, cross-attention design). |
| 2.13 | RP1 | 2. Autoencoders and VAEs | https://usaaio.guide/module/?id=representation-learning-autoencoders-vaes-latent-spaces | Bottleneck compression and the VAE. |
| 3.9 | RP4 | Autoregressive Generation | https://usaaio.guide/module/?id=autoregressive-generative-models | Factoring distributions into conditionals and sampling. |
| 3.15 | GM3 | 1. Setup | https://usaaio.guide/module/?id=generative-setup | The data distribution, three approaches, roadmap. |
| 3.11 | GM1 | 3. GAN | https://usaaio.guide/module/?id=generative-adversarial-networks | Generator and discriminator, mode collapse. |
| 3.16 | GM4 | 4. Diffusion and guidance | https://usaaio.guide/module/?id=generative-adding-noise | Adding and removing noise; guidance. |
| 3.26 | GM7 | Evaluating Generative Models | https://usaaio.guide/module/?id=evaluating-generative-models | "Use several measurements tied to the intended use" (BLEU, FID, precision/recall, failure modes). |
| 3.19 | XT3 | 1. The equation and the network | https://usaaio.guide/module/?id=sciml-setup | The heat equation and a network whose output solves it. |
| 3.22 | XT6 | 2. Derivatives and the physics loss | https://usaaio.guide/module/?id=sciml-derivatives | Autograd derivatives and an equation-based loss. |
| 3.24 | XT8 | 3. Training and checking | https://usaaio.guide/module/?id=sciml-training-and-checking | L-BFGS, checking against a trusted solution, inverse problems. |
| 3.25 | XT9 | Neural operators: DeepONet and FNO | https://usaaio.guide/module/?id=neural-operators | Learning a solution operator. |

**Advanced** (https://usaaio.guide/advanced/): "Long-context attention, multimodal models, reinforcement learning, and graph networks."

| # | Code | Title | Deep link | Covers |
|---|---|---|---|---|
| 4.3 | TF9 | Efficient Attention | https://usaaio.guide/module/?id=efficient-attention-long-context | FlashAttention, linear, low-rank and hashing attention, and their costs. |
| 4.7 | TF25 | 1. Setup, prefill and decode | https://usaaio.guide/module/?id=efficient-setup | Where long-context inference spends time. |
| 4.9 | TF27 | 2. The KV cache and sharing it | https://usaaio.guide/module/?id=efficient-kv-cache | Keeping and sharing keys and values. |
| 4.11 | TF29 | 3. FlashAttention and linear attention | https://usaaio.guide/module/?id=efficient-flashattention | Blocked exact attention; running-state attention. |
| 4.13 | TF31 | 4. Sparse attention, sinks and eviction | https://usaaio.guide/module/?id=sparse-attention-sinks-and-eviction | Which cache entries to drop. |
| 4.14 | TF32 | 5. State-space models | https://usaaio.guide/module/?id=state-space-models | Linear recurrences trained as convolutions. |
| 4.15 | TF33 | Mixture of Experts | https://usaaio.guide/module/?id=mixture-of-experts | Sparse routing. |
| 4.16 | RF2 | Reinforcement Learning: MDPs and Q-Learning | https://usaaio.guide/module/?id=reinforcement-learning | MDPs, Bellman equations, learning a policy from experience. |
| 4.17 | RF3 | Policy Gradients and Actor-Critic | https://usaaio.guide/module/?id=policy-gradients | REINFORCE, baselines, advantage, and PPO. |
| 4.18 | RF4 | RLHF and Preference Optimization | https://usaaio.guide/module/?id=preference-optimization-rlhf-and-dpo | Reward modeling from comparisons, PPO with a KL penalty, DPO; mentions IPO, KTO and GRPO's group-relative baseline. |
| 4.6 | XT2 | Graph Neural Networks | https://usaaio.guide/module/?id=graph-neural-networks | Message passing, the GCN layer, its symmetry. |

**Selected worked problems** (usaaio.guide "theory" pages; title exact, parent module in brackets). These are the most useful deep links for evaluation methodology.

| Problem | Deep link | What it teaches |
|---|---|---|
| The Best of Five Noisy Scores [Scikit-Learn Pipelines] | https://usaaio.guide/theory/?id=skl-best-of-five-noisy-scores | Five settings with equal true accuracy; the max of noisy CV scores is biased upward (winner's curse in model selection). |
| Hoeffding's Inequality and Generalization [Statistical Inference] | https://usaaio.guide/theory/?id=theory-hoeffding-generalization | Bound test vs true error, size a test set, then union-bound over many candidate models. |
| Margins on a Competition Leaderboard [Statistical Inference] | https://usaaio.guide/theory/?id=si-leaderboard-margins | Simultaneous guarantees for every score on a hidden-test leaderboard. |
| The Gap Between Two Models on One Test Set [Statistical Inference] | https://usaaio.guide/theory/?id=si-gap-on-a-shared-test-set | Paired comparison on a shared test set using per-example differences. |
| Two Intervals That Overlap [Statistical Inference] | https://usaaio.guide/theory/?id=si-two-overlapping-intervals | Why overlapping intervals do not imply no difference. |
| The Bootstrap Spread of a Mean [Statistical Inference] | https://usaaio.guide/theory/?id=si-bootstrap-spread-of-a-mean | Bootstrap variance of a mean. |
| How Often a 95% Interval Covers a Rare Failure Rate [Statistical Inference] | https://usaaio.guide/theory/?id=si-wald-coverage-for-rare-failures | Wald interval undercoverage at small n and rare failures. |
| A Test Set for a Strong Model [Statistical Inference] | https://usaaio.guide/theory/?id=si-test-size-for-a-strong-model | Sizing a test set for a target interval half-width. |
| Two Scans per Patient [Scikit-Learn Pipelines] | https://usaaio.guide/theory/?id=skl-scans-of-the-same-patient | Subject-level leakage when one patient has several samples. |
| A Test Set with Five Scans per Patient [Expectation and Joint Distributions] | https://usaaio.guide/theory/?id=ej-grouped-test-set | Effective sample size of a clustered test set. |
| Copies on Both Sides of the Split [Bias-Variance Tradeoff & Cross-Validation] | https://usaaio.guide/theory/?id=bv-copies-across-the-split | How duplicated rows across the split inflate a metric (memorization). |
| How Much a Better Model Can Gain [Bias-Variance Tradeoff & Cross-Validation] | https://usaaio.guide/theory/?id=bv-noise-floor-from-repeats | Noise floor from repeated measurements, bounding achievable MSE. |
| The Bias-Variance Decomposition and Cross-Validation [Bias-Variance Tradeoff & Cross-Validation] | https://usaaio.guide/theory/?id=theory-bias-variance-cv | Derivation, sound CV design, finding the leak in a flawed scheme. |
| Two Models Whose Bands Overlap [Data Visualization] | https://usaaio.guide/theory/?id=viz-overlapping-bands-paired-seeds | Paired seeds vs overlapping error bands. |
| The Max of Noisy Estimates [Reinforcement Learning: MDPs and Q-Learning] | https://usaaio.guide/theory/?id=rl-the-max-of-noisy-estimates | Maximization bias of noisy value estimates. |
| Training Windows for a Store Chain [Time Series] | https://usaaio.guide/theory/?id=ts-windows-for-a-store-chain | Window construction that keeps scored days out of training. |
| Question First, Photo Second [Vision-Language Models] | https://usaaio.guide/theory/?id=vlm-question-before-the-photo | Token layout and KV reuse for image tokens under a causal mask. |
| Attention with Smaller Patches [5. Vision Transformer and object detection] | https://usaaio.guide/theory/?id=cv-attention-with-smaller-patches | Patch size and ViT attention by hand. |

Gaps in usaaio.guide (searched all 82 module texts): no module on agents, tool use, prompt optimization, program search, self-improvement, verifiers, test-time compute or self-consistency, conformal prediction, meta-learning, pose estimation or video. The words "conformal", "verifier", "self-consistency", "keypoint", "meta-learn" and "program synthesis" do not occur in any module text.

### 2.2 UvA Deep Learning Tutorials

Index: https://uvadlc-notebooks.readthedocs.io/en/latest/ . Titles exact.

**Guides**
| Title | URL |
|---|---|
| Guide 1: Working with the Snellius cluster | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial1/Lisa_Cluster.html |
| Guide 2: Research projects with PyTorch | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/guide2/Research_Projects.html |
| Guide 3: Debugging in PyTorch | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/guide3/Debugging_PyTorch.html |
| Guide 4: Research Projects with JAX | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/guide4/Research_Projects_with_JAX.html |

**Training Models at Scale (JAX)**: Overview; Part 1.1 Training Larger Models on a Single GPU; Part 1.2 Profiling and Scaling Single-GPU Transformer Models; Part 2.1 Introduction to Distributed Computing in JAX; Part 2.2 (Fully-Sharded) Data Parallelism; Part 3.1 Pipeline Parallelism; Part 3.2 Looping Pipelines; Part 4.1 Tensor Parallelism; Part 4.2 Asynchronous Linear Layers with Tensor Parallelism; Part 4.3 Transformers with Tensor Parallelism; Part 5 Language Modeling with 3D Parallelism. Base: https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/scaling/JAX/overview.html (not mapped below; infrastructure only).

**Deep Learning 1 (PyTorch)**
| Title | URL |
|---|---|
| Tutorial 2: Introduction to PyTorch | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial2/Introduction_to_PyTorch.html |
| Tutorial 3: Activation Functions | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial3/Activation_Functions.html |
| Tutorial 4: Optimization and Initialization | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial4/Optimization_and_Initialization.html |
| Tutorial 5: Inception, ResNet and DenseNet | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial5/Inception_ResNet_DenseNet.html |
| Tutorial 6: Transformers and Multi-Head Attention | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial6/Transformers_and_MHAttention.html |
| Tutorial 7: Graph Neural Networks | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial7/GNN_overview.html |
| Tutorial 8: Deep Energy-Based Generative Models | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial8/Deep_Energy_Models.html |
| Tutorial 9: Deep Autoencoders | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial9/AE_CIFAR10.html |
| Tutorial 10: Adversarial attacks | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial10/Adversarial_Attacks.html |
| Tutorial 11: Normalizing Flows for image modeling | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial11/NF_image_modeling.html |
| Tutorial 12: Autoregressive Image Modeling | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial12/Autoregressive_Image_Modeling.html |
| Tutorial 15: Vision Transformers | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial15/Vision_Transformer.html |
| Tutorial 16: Meta-Learning - Learning to Learn | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial16/Meta_Learning.html |
| Tutorial 17: Self-Supervised Contrastive Learning with SimCLR | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial17/SimCLR.html |

**Deep Learning 1 (JAX+Flax)**: JAX versions of Tutorials 2, 3, 4, 5, 6, 7, 9, 11, 12, 15 and 17, under https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/JAX/ (for example "Tutorial 6 (JAX): Transformers and Multi-Head Attention" at https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/JAX/tutorial6/Transformers_and_MHAttention.html and "Tutorial 15 (JAX): Vision Transformers" at https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/JAX/tutorial15/Vision_Transformer.html).

**Deep Learning 2**
| Title | URL |
|---|---|
| GDL - Regular Group Convolutions | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/Geometric_deep_learning/tutorial1_regular_group_convolutions.html |
| GDL - Steerable CNNs | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/Geometric_deep_learning/tutorial2_steerable_cnns.html |
| DPM1 - Deep Probabilistic Models I | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/deep_probabilistic_models_I/tutorial_1.html |
| DPM2 - Variational inference for deep discrete latent variable models | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/deep_probabilistic_models_II/tutorial_2a.html |
| DPM 2 - Variational Inference for Deep Continuous LVMs | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/deep_probabilistic_models_II/tutorial_2b.html |
| AGM - Advanced Topics in Normalizing Flows - 1x1 convolution | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/Advanced_Generative_Models/Normalizing_flows/advancednormflow.html |
| HDL - Introduction to HyperParameter Tuning | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/High-performant_DL/hyperparameter_search/hpdlhyperparam.html |
| HDL - Introduction to Multi GPU Programming | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/High-performant_DL/Multi_GPU/hpdlmultigpu.html |
| Tutorial 1: Bayesian Neural Networks with Pyro | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/Bayesian_Neural_Networks/dl2_bnn_tut1_students_with_answers.html |
| Tutorial 2: Comparison to other methods of uncertainty quantification | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/Bayesian_Neural_Networks/dl2_bnn_tut2_student_with_answers.html |
| DNN - Tutorial 2 Part I: Physics inspired Machine Learning | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/Dynamical_Neural_Networks/Complete_DNN_2_1.html |
| DNN - Tutorial 2 Part II: Physics inspired Machine Learning | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/Dynamical_Neural_Networks/Complete_DNN_2_2.html |
| DS - Dynamical Systems & Neural ODEs | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/Dynamical_systems/dynamical_systems_neural_odes.html |
| SGA - Sampling Discrete Structures | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/sampling/introduction.html |
| SGA - Sampling Subsets with Gumbel-Top (k) Relaxations | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/sampling/subsets.html |
| SGA: Learning Latent Permutations with Gumbel-Sinkhorn Networks | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/sampling/permutations.html |
| SGA - Graph Sampling for Neural Relational Inference | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/sampling/graphs.html |
| CRL - Causal Identifiability from Temporal Intervened Sequences | https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/Causality_and_CRL/citris-tutorial.html |

Per-tutorial descriptions for the tutorials used in the mapping are given in Section 3.

### 2.3 Stanford CS329Z: Engineering AI Agents (Fall 2026)

Schedule: https://cs329z.stanford.edu/#schedule . Lecture titles are exact (section label, then lecture title). One source title contains an em-dash, rewritten here as a colon. Slides follow https://web.stanford.edu/class/cs329z/slides/lectureNN.pdf (HTTP 200 for lectures 01 to 13, 15, 17).

| # | Date | Section label / lecture title | Slides | Video | Assigned readings (from the page) |
|---|---|---|---|---|---|
| 1 | Wed Sep 23 | Foundations & Landscape / Introduction: What Are Agentic Systems? | https://web.stanford.edu/class/cs329z/slides/lecture01.pdf | https://youtu.be/DGI4vucR71w | BAIR compound AI systems post; Weng "LLM Powered Autonomous Agents"; arXiv 2407.01502 |
| 2 | Mon Sep 28 | LLMs for Builders | https://web.stanford.edu/class/cs329z/slides/lecture02.pdf | https://youtu.be/Vr1NzH8bT44 | arXiv 1706.03762; arXiv 2006.16236; Anthropic "Effective context engineering for AI agents" |
| 3 | Wed Sep 30 | Building Blocks / Retrieval-Augmented Generation (RAG) | https://web.stanford.edu/class/cs329z/slides/lecture03.pdf | https://youtu.be/psLc-46GqY0 | arXiv 2005.11401; 2004.04906; 2004.12832 |
| 4 | Mon Oct 5 | Tool Use & Function Calling | https://web.stanford.edu/class/cs329z/slides/lecture04.pdf | https://youtu.be/s0S38lz6O7M | Toolformer (2302.04761); Gorilla (2305.15334); MCP specification 2025-06-18 |
| 5 | Wed Oct 7 | Frameworks & Agent Design / Frameworks & Orchestration | https://web.stanford.edu/class/cs329z/slides/lecture05.pdf | https://youtu.be/q0Q-Hy8TTps | DSPy (2310.03714); LangGraph Overview; Arena.ai "HarnessTax: How Much Does the Harness Matter for Coding Agents?" Code: https://github.com/cs329z/lecture5-frameworks |
| 6 | Mon Oct 12 | Agent Design Patterns & Scaffolds | https://web.stanford.edu/class/cs329z/slides/lecture06.pdf | https://youtu.be/JC_pLC5EX_w | ReAct (2210.03629); Anthropic "Building Effective AI Agents"; LangChain "Context Engineering"; additional: Reflexion (2303.11366), Executable Code Actions / CodeAct (2402.01030) |
| 7 | Wed Oct 14 | Memory & Multi-Agent Systems / Agent Memory Architectures | https://web.stanford.edu/class/cs329z/slides/lecture07.pdf | https://youtu.be/qh5tP6PBZ6U | CoALA (2309.02427); MemGPT (2310.08560); Generative Agents (2304.03442) |
| 8 | Mon Oct 19 | Multi-Agent Systems | https://web.stanford.edu/class/cs329z/slides/lecture08.pdf | https://youtu.be/TlX_ft_PQIM | arXiv 2308.08155; 2503.13657; 2512.08296 |
| 9 | Wed Oct 21 | Optimization / Optimization | https://web.stanford.edu/class/cs329z/slides/lecture09.pdf | https://youtu.be/e_m99aR7_3Q | GEPA (2507.19457); MIPRO, "Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs" (2406.11695); DeepSeekMath (2402.03300) |
| 10 | Mon Oct 26 | Guest Lecture: Terminal-Bench (Ryan Marten, Alex Shaw) | https://web.stanford.edu/class/cs329z/slides/lecture10.pdf | https://youtu.be/7GW-9ug2nvw | tbench.ai; arXiv 2601.11868 |
| 11 | Wed Oct 28 | Data for Agentic Systems / What Data Do Agents Need? | https://web.stanford.edu/class/cs329z/slides/lecture11.pdf | none listed | Shankar "AI engineering flywheel" blog; EMNLP 2024 main.54 |
| 12 | Mon Nov 2 | Data Selection & Quality | https://web.stanford.edu/class/cs329z/slides/lecture12.pdf | none listed | arXiv 2504.21798; 2404.12272; additional 2305.11206 |
| 13 | Wed Nov 4 | Evaluation for Agentic Systems / Evaluation Fundamentals & Benchmark Design | https://web.stanford.edu/class/cs329z/slides/lecture13.pdf | none listed | "Establishing Best Practices for Building Rigorous Agentic Benchmarks" (2507.02825); additional: Press, "How to Build Good Language Modeling Benchmarks"; tinyBenchmarks (2402.14992) |
| 14 | Mon Nov 9 | Fireside Chat with Andrew Ng | none | none listed | none |
| 15 | Wed Nov 11 | LLM-as-Judge & Evaluation Infrastructure | https://web.stanford.edu/class/cs329z/slides/lecture15.pdf | none listed | Anthropic "Demystifying Evals for AI Agents"; MT-Bench/Chatbot Arena (2306.05685); AutoMetrics (2512.17267); additional: AutoLibra (OpenReview 4BjGVZ7Bxn) |
| 16 | Mon Nov 16 | Guest Lecture: SWE-bench (Carlos Jimenez, Alexander Wettig) | none listed | none listed | SWE-bench (2310.06770) |
| 17 | Wed Nov 18 | Safety / Agent Safety & Guardrails | https://web.stanford.edu/class/cs329z/slides/lecture17.pdf | none listed | arXiv 2409.00138; 2508.10880; 2601.05918; additional 2603.02983, OpenAI prompt injections, Anthropic RSP |
| 18 | Mon Nov 30 | Coding Agents & Personal Agents / Coding & Software Agents | not yet posted | not yet posted | SWE-agent (2405.15793); OpenHands (2407.16741); additional: Anthropic "Claude Code: Best Practices for Agentic Coding", "Effective Harnesses for Long-Running Agents" |
| 19 | Wed Dec 2 | Personal Agents | not yet posted | not yet posted | arXiv 2505.10831; additional 2603.05923 |
| 20 | Wed Dec 9 | Open Problems & Final Demos / Final Project Demo Day | n/a | n/a | n/a |

Assignments: HW1 "CS 329Z Assignment 1: Building an Agent Harness (starter)", https://github.com/cs329z/assignment1-harness (model-call wrapper with caching, spending tracking and a budget limit; data pipelines; an agent loop with tools including a sandboxed terminal; deterministic, model-graded and simulated-user tests). HW2 https://github.com/cs329z/assignment2-harness (redirects to the repository titled "CS 329Z Assignment 2: Building an Evaluation Task (starter)": build a Harbor-format evaluation task, with mini-SWE-agent and a SWE-bench task).

### 2.4 Stanford CS329A: Self-Improving AI Agents (Autumn 2025)

Schedule: https://cs329a.stanford.edu/#schedule . Session titles and reading titles exact (link text as shown on the page).

| # | Date | Session | Readings (link text, URL as linked) |
|---|---|---|---|
| 1 | Mon Sep 22 | Course Overview | none |
| 2 | Fri Sep 26 | Test-time Compute Scaling | Large Language Monkeys: Scaling Inference Compute with Repeated Sampling (https://arxiv.org/abs/2407.21787); Archon: An Architecture Search Framework for Inference-Time Techniques (https://www.arxiv.org/abs/2409.15254); Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters (https://arxiv.org/abs/2408.03314); How Do Large Language Monkeys Get Their Power (Laws)? (https://arxiv.org/abs/2502.17578) |
| 3 | Mon Sep 29 | Robust Verification | Shrinking the Generation-Verification Gap with Weak Verifiers (https://arxiv.org/abs/2506.18203); Training Verifiers to Solve Math Word Problems (https://arxiv.org/abs/2110.14168); Let's Verify step by step (https://arxiv.org/abs/2305.20050); Math-Shepherd (https://arxiv.org/abs/2312.08935) |
| 4 | Fri Oct 3 | Learning from feedback with tools/code | ReAct (https://arxiv.org/abs/2210.03629); RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning (https://arxiv.org/abs/2410.02089); Constitutional AI: Harmlessness from AI Feedback (https://arxiv.org/abs/2212.08073) |
| 5 | Mon Oct 6 | Multi-step Reasoning/Planning | SWiRL (https://arxiv.org/abs/2504.04736); Language Agent Tree Search (https://arxiv.org/abs/2310.04406); SPRINT (https://arxiv.org/abs/2506.05745); ADaPT (https://arxiv.org/abs/2311.05772); Wider or Deeper? Scaling LLM Inference-Time Compute with Adaptive Branching Tree Search (https://arxiv.org/abs/2503.04412) |
| 6 | Fri Oct 10 | Train Time Scaling/Scaling RL | STaR: Bootstrapping Reasoning With Reasoning (https://arxiv.org/pdf/2203.14465); DeepSeekMath (https://arxiv.org/abs/2402.03300); DAPO: An Open-Source LLM Reinforcement Learning System at Scale (https://arxiv.org/abs/2503.14476) |
| 7 | Mon Oct 13 | Open-Ended Evolution of Self-Improving Agents | link text "Automated design of agentic systems" but href https://arxiv.org/pdf/2505.22954, which is "Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents" (Zhang, Hu, Lu, Lange, Clune; verified on arXiv); The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery (https://arxiv.org/abs/2408.06292); AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms (DeepMind PDF, https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/AlphaEvolve.pdf) |
| 8 | Fri Oct 17 | Self improvement with Search & Deep Research Agents | Competition-Level Code Generation with AlphaCode (https://arxiv.org/pdf/2203.07814); AlphaCode 2 Technical Report (DeepMind PDF); Search-o1 (https://arxiv.org/pdf/2501.05366) |
| 9 | Mon Oct 20 | Guest Lecture: Melvin Johnson (Google DeepMind) | "Evolution of Post-training from Chatbots to Agents" (no link) |
| 10 to 12 | Oct 24, 27, 31 | Mid term presentations | none |
| 13 | Mon Nov 3 | Agentic Frameworks for Software Engineering | CodeMonkeys (https://arxiv.org/abs/2501.14723); KernelBench (https://arxiv.org/pdf/2502.10517); Improving Parallel Program Performance with LLM Optimizers via Agent-System Interfaces (https://arxiv.org/abs/2410.15625) |
| 14 | Fri Nov 7 | Augmenting Agents with Memory (guest: Junchen Jiang) | Cartridges (https://arxiv.org/abs/2506.06266); MemGPT (https://arxiv.org/abs/2310.08560); CacheBlend (http://arxiv.org/abs/2405.16444) |
| 15 | Mon Nov 10 | Guest Lecture: Denny Zhou, LLM Reasoning | none |
| 16 | Fri Nov 14 | Guest Lecture: Thang Luong, Towards AI Superhuman Reasoning: AlphaProof, AlphaGeometry & Gemini IMO Gold Medal | none |
| 17 | Mon Nov 17 | Agentic Evaluations & Long-Horizon Tasks | Measuring AI Ability to Complete Long Tasks (https://arxiv.org/abs/2503.14499; the current arXiv title is "Measuring AI Ability to Complete Long Software Tasks"); GDPVal (https://arxiv.org/abs/2510.04374); DeepScholar-Bench (https://arxiv.org/abs/2508.20033) |
| 18 | Fri Nov 21 | Guest Lecture: Misha Laskin, Building Agentic Systems for Autonomy: Lessons & Open questions | none |
| 19 | Mon Dec 1 | Guest Lecture: Danny Driess, Multimodal AI Agents in Robotics | none |
| 20 | Fri Dec 5 | Future Research Areas | none |

Homework (page text, verbatim): "The homeworks will help develop intuition for the basics of self-improvement, multi-step reasoning, and tool use techniques." No per-homework descriptions are posted.

## 3. Topic to module mapping

For each topic: the best 1 to 4 modules, with the deepest stable link and what the module covers for our purpose. Course readings named here were checked against arXiv metadata (one arXiv API query for all 67 IDs, 2026-11-24; every ID resolved to the title shown). Non-arXiv links (DeepMind PDFs, Anthropic posts, MCP spec, Arena blog, OpenReview, YouTube, GitHub) returned HTTP 200 the same day. "Gap" lines state what none of the four resources teaches.

### 3.1 Evolutionary and LLM-guided program search
1. CS329A, Mon Oct 13, "Open-Ended Evolution of Self-Improving Agents" (https://cs329a.stanford.edu/#schedule). Readings: Darwin Godel Machine (https://arxiv.org/abs/2505.22954; the page's link text says "Automated design of agentic systems" but the href is the DGM paper), The AI Scientist (https://arxiv.org/abs/2408.06292), AlphaEvolve (DeepMind PDF linked from the page). Covers archive-based open-ended evolution of agent code and LLM-guided evolutionary search over programs.
2. CS329Z Lecture 9, "Optimization" (slides https://web.stanford.edu/class/cs329z/slides/lecture09.pdf, video https://youtu.be/e_m99aR7_3Q). Readings GEPA, "Reflective Prompt Evolution Can Outperform Reinforcement Learning" (https://arxiv.org/abs/2507.19457) and MIPRO (https://arxiv.org/abs/2406.11695). Covers reflective, trace-reading evolution of text programs.
3. CS329A, Fri Sep 26, "Test-time Compute Scaling", reading Archon (https://arxiv.org/abs/2409.15254). Covers automated search over combinations of inference-time techniques and LLMs under a compute budget.
4. CS329A, Mon Nov 3, "Agentic Frameworks for Software Engineering", reading "Improving Parallel Program Performance with LLM Optimizers via Agent-System Interfaces" (https://arxiv.org/abs/2410.15625). Covers generative optimization of system code where a DSL defines the search space and "AutoGuide" turns raw execution output into actionable feedback.
- Gap: neither usaaio.guide nor UvA has an evolutionary-algorithms or program-search module. The nearest UvA material is "HDL - Introduction to HyperParameter Tuning" (grid search and Bayesian optimization with Ax), https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/High-performant_DL/hyperparameter_search/hpdlhyperparam.html .

### 3.2 Recursive self-improvement and self-improving agents
1. CS329A, Mon Oct 13, "Open-Ended Evolution of Self-Improving Agents" (as 3.1). The DGM reading is the direct reference for empirical self-modification of an agent's own code.
2. CS329A, Fri Oct 10, "Train Time Scaling/Scaling RL" (https://cs329a.stanford.edu/#schedule). Reading STaR, "Bootstrapping Reasoning With Reasoning" (https://arxiv.org/abs/2203.14465): a model improving by training on its own filtered rationales.
3. CS329A, Fri Oct 3, "Learning from feedback with tools/code". Readings ReAct (https://arxiv.org/abs/2210.03629), RLEF (https://arxiv.org/abs/2410.02089), Constitutional AI (https://arxiv.org/abs/2212.08073). Covers improvement from execution feedback and AI feedback.
4. CS329Z Lecture 6, "Agent Design Patterns & Scaffolds" (slides https://web.stanford.edu/class/cs329z/slides/lecture06.pdf, video https://youtu.be/JC_pLC5EX_w). Additional reading Reflexion (https://arxiv.org/abs/2303.11366): agents that reflect verbally on feedback and keep the reflections in an episodic memory buffer, without weight updates.
- Gap: no resource covers Godel-machine theory, Huxley-Godel Machine style clade metaproductivity, or formal guarantees for self-modification.

### 3.3 Agent harnesses, tool use and tool selection
1. CS329Z Lecture 4, "Tool Use & Function Calling" (slides https://web.stanford.edu/class/cs329z/slides/lecture04.pdf, video https://youtu.be/s0S38lz6O7M). Readings Toolformer (https://arxiv.org/abs/2302.04761), Gorilla (https://arxiv.org/abs/2305.15334), Model Context Protocol specification 2025-06-18 (https://modelcontextprotocol.io/specification/2025-06-18).
2. CS329Z Lecture 5, "Frameworks & Orchestration" (slides https://web.stanford.edu/class/cs329z/slides/lecture05.pdf, video https://youtu.be/q0Q-Hy8TTps, code https://github.com/cs329z/lecture5-frameworks). Readings DSPy (https://arxiv.org/abs/2310.03714) and Arena.ai, "HarnessTax: How Much Does the Harness Matter for Coding Agents?" (https://arena.ai/blog/coding-agents-harness-tax).
3. CS329Z Assignment 1, "Building an Agent Harness" (https://github.com/cs329z/assignment1-harness). Students build a model-call wrapper with caching, spend tracking and a budget limit, an agent loop with tools including a sandboxed terminal, and deterministic, model-graded and simulated-user tests.
4. CS329Z Lecture 18, "Coding & Software Agents" (no slides posted yet as of 2026-11-24; schedule https://cs329z.stanford.edu/#schedule). Readings SWE-agent, "Agent-Computer Interfaces Enable Automated Software Engineering" (https://arxiv.org/abs/2405.15793), OpenHands (https://arxiv.org/abs/2407.16741), and Anthropic, "Effective Harnesses for Long-Running Agents" (https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).
- Also relevant: CS329Z Lecture 6 (ReAct, CodeAct "Executable Code Actions Elicit Better LLM Agents", https://arxiv.org/abs/2402.01030) and CS329A Mon Nov 3 (Agent-System Interfaces).
- Gap: no resource treats tool selection as a learned decision under a cost budget; CS329Z Lecture 1's reading "AI Agents That Matter" (https://arxiv.org/abs/2407.01502) argues for jointly optimizing cost and accuracy, the closest framing.

### 3.4 Prompt optimization (DSPy, GEPA)
1. CS329Z Lecture 9, "Optimization" (slides https://web.stanford.edu/class/cs329z/slides/lecture09.pdf, video https://youtu.be/e_m99aR7_3Q). Readings GEPA (https://arxiv.org/abs/2507.19457), "Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs" (MIPRO, https://arxiv.org/abs/2406.11695), and DeepSeekMath (https://arxiv.org/abs/2402.03300) as the RL comparison point.
2. CS329Z Lecture 5, "Frameworks & Orchestration" (as 3.3). Reading "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines" (https://arxiv.org/abs/2310.03714).
3. CS329A, Fri Sep 26, "Test-time Compute Scaling", reading Archon (https://arxiv.org/abs/2409.15254): configuration search over inference-time techniques, tuned to target benchmarks.
- Gap: usaaio.guide and UvA have nothing on prompt or program optimization.

### 3.5 Reinforcement learning for LLMs (policy gradient, PPO, GRPO)
1. usaaio.guide 4.17 RF3, "Policy Gradients and Actor-Critic" (https://usaaio.guide/module/?id=policy-gradients). REINFORCE, why the dynamics drop out, baselines, advantage and actor-critic, why PPO exists, and a from-scratch implementation.
2. usaaio.guide 4.18 RF4, "RLHF and Preference Optimization" (https://usaaio.guide/module/?id=preference-optimization-rlhf-and-dpo). Bradley-Terry reward modeling from comparison pairs, PPO with a KL penalty to the reference, DPO, and a note on IPO, KTO and GRPO ("replaces the value network with a group-relative baseline computed from several sampled responses").
3. CS329A, Fri Oct 10, "Train Time Scaling/Scaling RL" (https://cs329a.stanford.edu/#schedule). Readings STaR, DeepSeekMath (https://arxiv.org/abs/2402.03300, which introduced GRPO) and DAPO (https://arxiv.org/abs/2503.14476).
4. CS329A, Mon Oct 6, "Multi-step Reasoning/Planning", reading "Synthetic Data Generation & Multi-Step RL for Reasoning & Tool Use" (SWiRL, https://arxiv.org/abs/2504.04736). RL over multi-step tool-use trajectories.
- Prerequisite: usaaio.guide 4.16 RF2, "Reinforcement Learning: MDPs and Q-Learning" (https://usaaio.guide/module/?id=reinforcement-learning). UvA has no RL tutorial.

### 3.6 Verifiers and reward models
1. CS329A, Mon Sep 29, "Robust Verification" (https://cs329a.stanford.edu/#schedule). Readings "Shrinking the Generation-Verification Gap with Weak Verifiers" (Weaver, https://arxiv.org/abs/2506.18203; combines many weak verifiers with weak supervision to estimate each one's accuracy), "Training Verifiers to Solve Math Word Problems" (https://arxiv.org/abs/2110.14168), "Let's Verify Step by Step" (https://arxiv.org/abs/2305.20050), Math-Shepherd (https://arxiv.org/abs/2312.08935).
2. CS329Z Lecture 15, "LLM-as-Judge & Evaluation Infrastructure" (slides https://web.stanford.edu/class/cs329z/slides/lecture15.pdf). Readings "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (https://arxiv.org/abs/2306.05685), AutoMetrics (https://arxiv.org/abs/2512.17267), Anthropic "Demystifying Evals for AI Agents" (https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents); additional AutoLibra (https://openreview.net/forum?id=4BjGVZ7Bxn).
3. usaaio.guide 4.18 RF4, "RLHF and Preference Optimization" (https://usaaio.guide/module/?id=preference-optimization-rlhf-and-dpo). Reward model as an SFT model with a scalar head trained on preference pairs.
4. CS329Z Lecture 12, "Data Selection & Quality" (slides https://web.stanford.edu/class/cs329z/slides/lecture12.pdf). Reading "Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences" (https://arxiv.org/abs/2404.12272).

### 3.7 Test-time compute and self-consistency
1. CS329A, Fri Sep 26, "Test-time Compute Scaling" (https://cs329a.stanford.edu/#schedule). Readings "Large Language Monkeys" (https://arxiv.org/abs/2407.21787; coverage scales log-linearly with samples, and majority voting and reward models plateau beyond several hundred samples when no automatic verifier exists), Snell et al. on compute-optimal test-time scaling (https://arxiv.org/abs/2408.03314), "How Do Large Language Monkeys Get Their Power (Laws)?" (https://arxiv.org/abs/2502.17578), Archon.
2. CS329A, Mon Oct 6, "Multi-step Reasoning/Planning". Readings Language Agent Tree Search (https://arxiv.org/abs/2310.04406), "Wider or Deeper? ... Adaptive Branching Tree Search" (https://arxiv.org/abs/2503.04412), ADaPT (https://arxiv.org/abs/2311.05772), SPRINT (https://arxiv.org/abs/2506.05745).
3. CS329A, Mon Nov 3, "Agentic Frameworks for Software Engineering", reading CodeMonkeys (https://arxiv.org/abs/2501.14723): test-time compute for software engineering.
4. CS329A, Fri Oct 17, "Self improvement with Search & Deep Research Agents". Readings AlphaCode (https://arxiv.org/abs/2203.07814), AlphaCode 2 report, Search-o1 (https://arxiv.org/abs/2501.05366).
- Gap: no session is devoted to self-consistency (majority vote over sampled reasoning paths) as such; the Large Language Monkeys reading is the closest treatment of voting.

### 3.8 Generalization, overfitting and validation methodology
1. usaaio.guide 2.16 ML11, "Bias-Variance Tradeoff & Cross-Validation" (https://usaaio.guide/module/?id=bias-variance-cross-validation), with worked problems "The Bias-Variance Decomposition and Cross-Validation" (https://usaaio.guide/theory/?id=theory-bias-variance-cv) and "Copies on Both Sides of the Split" (https://usaaio.guide/theory/?id=bv-copies-across-the-split).
2. usaaio.guide 1.5 PY5, "Scikit-Learn Pipelines" (https://usaaio.guide/module/?id=scikit-learn-api-ml-pipelines), with worked problems "The Best of Five Noisy Scores" (https://usaaio.guide/theory/?id=skl-best-of-five-noisy-scores; the winning configuration's CV score is biased upward even when all candidates are equal) and "Two Scans per Patient" (https://usaaio.guide/theory/?id=skl-scans-of-the-same-patient; split by subject, not by sample).
3. CS329Z Lecture 1, "Introduction: What Are Agentic Systems?" (source title uses an em-dash; slides https://web.stanford.edu/class/cs329z/slides/lecture01.pdf, video https://youtu.be/DGI4vucR71w). Reading "AI Agents That Matter" (https://arxiv.org/abs/2407.01502): many agent benchmarks have inadequate or no holdout sets, agents overfit to benchmarks, and the paper prescribes a framework for avoiding this.
4. CS329Z Lecture 13, "Evaluation Fundamentals & Benchmark Design" (slides https://web.stanford.edu/class/cs329z/slides/lecture13.pdf). Reading "Establishing Best Practices for Building Rigorous Agentic Benchmarks" (https://arxiv.org/abs/2507.02825; task-setup and reward-design flaws can misestimate agent performance by up to 100% in relative terms).
- Also: UvA "Guide 2: Research projects with PyTorch" (https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/guide2/Research_Projects.html) on seeds, reproducibility and hyperparameter search; it does not discuss overfitting to the validation set.

### 3.9 Adaptive data analysis and statistics of evaluation
1. usaaio.guide 1.12 PS3, "Statistical Inference" (https://usaaio.guide/module/?id=statistics-hypothesis-testing). Confidence intervals, hypothesis tests ("could this be luck?"), the bootstrap.
2. usaaio.guide worked problem "Hoeffding's Inequality and Generalization" (https://usaaio.guide/theory/?id=theory-hoeffding-generalization; bound the test-vs-true gap, size a test set, then union-bound over many candidate models) and "Margins on a Competition Leaderboard" (https://usaaio.guide/theory/?id=si-leaderboard-margins; a simultaneous guarantee for every leaderboard score on a hidden test set).
3. usaaio.guide worked problems on paired and clustered evaluation: "The Gap Between Two Models on One Test Set" (https://usaaio.guide/theory/?id=si-gap-on-a-shared-test-set), "A Test Set with Five Scans per Patient" (https://usaaio.guide/theory/?id=ej-grouped-test-set), "Two Models Whose Bands Overlap" (https://usaaio.guide/theory/?id=viz-overlapping-bands-paired-seeds).
4. CS329Z Lecture 13, "Evaluation Fundamentals & Benchmark Design" (as 3.8); additional reading tinyBenchmarks (https://arxiv.org/abs/2402.14992; estimating benchmark performance from about 100 curated examples).
- Gap: none of the four resources teaches adaptive data analysis proper (reusable holdout, Thresholdout, the Ladder mechanism, or differential-privacy arguments for holdout reuse). Proposals must cite primary papers for these.

### 3.10 Uncertainty quantification and conformal prediction
1. UvA DL2, "Tutorial 2: Comparison to other methods of uncertainty quantification" (https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/Bayesian_Neural_Networks/dl2_bnn_tut2_student_with_answers.html). Deterministic MLP, deep ensembles, MC dropout, a Bayesian last layer in Pyro, and conformal prediction with naive softmax, APS and RAPS scores, on toy regression and on MNIST under rotation shift.
2. UvA DL2, "Tutorial 1: Bayesian Neural Networks with Pyro" (https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/Bayesian_Neural_Networks/dl2_bnn_tut1_students_with_answers.html).
3. usaaio.guide 2.3 ML6, "Classification Metrics" (https://usaaio.guide/module/?id=model-evaluation), section "Are the probabilities trustworthy?" (calibration), plus threshold tuning.
4. usaaio.guide worked problem "How Often a 95% Interval Covers a Rare Failure Rate" (https://usaaio.guide/theory/?id=si-wald-coverage-for-rare-failures): finite-sample undercoverage of the Wald interval, the reason exact or distribution-free bounds are needed.
- Gap: no resource covers Learn-then-Test, conformal risk control, or selective prediction with guarantees.

### 3.11 Vision transformers and vision-language models
1. usaaio.guide 3.8 TF7, "Vision-Language Models" (https://usaaio.guide/module/?id=cross-attention-multimodal-attention). LLaVA-style models: image as a sequence of patches, bridging vision and text spaces, two-stage training, and the cross-attention alternative. Worked problem "Question First, Photo Second" (https://usaaio.guide/theory/?id=vlm-question-before-the-photo).
2. usaaio.guide 3.3 CV6, "5. Vision Transformer and object detection" (https://usaaio.guide/module/?id=vision-transformers-vit-attention), with "Attention with Smaller Patches" (https://usaaio.guide/theory/?id=cv-attention-with-smaller-patches).
3. UvA DL1, "Tutorial 15: Vision Transformers" (https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial15/Vision_Transformer.html). ViT from scratch on CIFAR10, compared with the Tutorial 5 CNNs (about 75% vs about 90% accuracy).
4. usaaio.guide 2.14 RP2, "Contrastive Learning and CLIP" (https://usaaio.guide/module/?id=contrastive-learning).

### 3.12 Transformers and attention
1. UvA DL1, "Tutorial 6: Transformers and Multi-Head Attention" (https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial6/Transformers_and_MHAttention.html). Scaled dot-product and multi-head attention, encoder, positional encoding, warm-up; experiments on sequence reversal and set anomaly detection.
2. usaaio.guide 2.9 TF1, "Self-Attention Fundamentals" (https://usaaio.guide/module/?id=transformer-fundamentals), with the five-part build that starts at "1. Setup and input" (https://usaaio.guide/module/?id=transformer-setup).
3. CS329Z Lecture 2, "LLMs for Builders" (slides https://web.stanford.edu/class/cs329z/slides/lecture02.pdf, video https://youtu.be/Vr1NzH8bT44). Readings "Attention Is All You Need" (https://arxiv.org/abs/1706.03762), "Transformers are RNNs" (https://arxiv.org/abs/2006.16236), Anthropic on context engineering.
4. usaaio.guide 4.3 TF9, "Efficient Attention" (https://usaaio.guide/module/?id=efficient-attention-long-context).

### 3.13 Adversarial examples
1. UvA DL1, "Tutorial 10: Adversarial attacks" (https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial10/Adversarial_Attacks.html). FGSM and adversarial patches on a pretrained ResNet34, transferability of a patch to DenseNet121, and defenses (adversarial training, defensive distillation).
2. usaaio.guide 2.7 CV3, "4. Segmentation and adversarial attacks" (https://usaaio.guide/module/?id=semantic-segmentation-unet-masks). Gradient attacks after a U-Net segmentation section.
3. CS329Z Lecture 17, "Agent Safety & Guardrails" (slides https://web.stanford.edu/class/cs329z/slides/lecture17.pdf). Agent-level attacks and defenses, including prompt injection (additional reading from OpenAI) and privacy risks of agents.

### 3.14 Meta-learning
1. UvA DL1, "Tutorial 16: Meta-Learning - Learning to Learn" (https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial16/Meta_Learning.html). Prototypical Networks, MAML and first-order ProtoMAML on CIFAR100 split by class (80 train, 10 validation, 10 test classes), with SVHN for out-of-domain adaptation.
2. CS329A, Mon Oct 13 (as 3.1), as the agent-level analog: the DGM improves the code that does the improving.
- Gap: usaaio.guide and CS329Z have no meta-learning module.

### 3.15 Time-series and sequence modeling
1. usaaio.guide 2.20 ML15, "Time Series" (https://usaaio.guide/module/?id=time-series). Windows, time-ordered evaluation, baselines, features from the past only, leakage from a rolling mean and from shuffled folds, classifying whole series, and a phase-vs-spectrum example in which logistic regression scores 0.533 on raw samples and 1.000 on FFT magnitudes of the same series. Worked problem "Training Windows for a Store Chain" (https://usaaio.guide/theory/?id=ts-windows-for-a-store-chain).
2. usaaio.guide 3.5 NL2, "Recurrent Networks: RNN, LSTM, GRU" (https://usaaio.guide/module/?id=sequence-models-transfer-learning).
3. usaaio.guide 4.14 TF32, "5. State-space models" (https://usaaio.guide/module/?id=state-space-models).
4. UvA DL2, "DNN - Tutorial 2 Part I: Physics inspired Machine Learning" (https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/Dynamical_Neural_Networks/Complete_DNN_2_1.html). SINDy sparse equation discovery from sampled trajectories and reservoir computing for next-state prediction on the Lorenz attractor. Companion: "DS - Dynamical Systems & Neural ODEs" (https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/Dynamical_systems/dynamical_systems_neural_odes.html).

### 3.16 Human pose estimation or video understanding
- Gap: none of the four resources has a module on human pose estimation, keypoint tracking, or video understanding. The nearest material:
1. usaaio.guide 3.3 CV6, "5. Vision Transformer and object detection" (https://usaaio.guide/module/?id=vision-transformers-vit-attention): localization with boxes, the step before keypoints.
2. usaaio.guide 2.7 CV3, "4. Segmentation and adversarial attacks" (https://usaaio.guide/module/?id=semantic-segmentation-unet-masks): per-pixel masks, the output type SAM 2 produces.
3. UvA DL2, "CRL - Causal Identifiability from Temporal Intervened Sequences" (https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/DL2/Causality_and_CRL/citris-tutorial.html): learning latent causal variables (position, rotation, lighting) from temporal image sequences.
4. CS329A, Mon Dec 1, Guest Lecture: Danny Driess (Physical Intelligence), "Multimodal AI Agents in Robotics" (https://cs329a.stanford.edu/#schedule; no reading or recording posted).

### 3.17 Memory and skill libraries for agents
1. CS329Z Lecture 7, "Agent Memory Architectures" (slides https://web.stanford.edu/class/cs329z/slides/lecture07.pdf, video https://youtu.be/qh5tP6PBZ6U). Readings "Cognitive Architectures for Language Agents" (CoALA, https://arxiv.org/abs/2309.02427; modular memory components and a structured action space), MemGPT (https://arxiv.org/abs/2310.08560), Generative Agents (https://arxiv.org/abs/2304.03442).
2. CS329A, Fri Nov 7, "Augmenting Agents with Memory" (guest Junchen Jiang). Readings Cartridges (https://arxiv.org/abs/2506.06266; train a small KV cache offline per corpus and amortize its cost across queries), MemGPT, CacheBlend (https://arxiv.org/abs/2405.16444).
3. CS329Z Lecture 6, "Agent Design Patterns & Scaffolds" (as 3.2): Reflexion's episodic memory of reflections, and CodeAct's executable code actions (https://arxiv.org/abs/2402.01030), a basis for stored programs as skills.
4. usaaio.guide 3.6 TF5, "Retrieval-Augmented Generation" (https://usaaio.guide/module/?id=rag-retrieval-embeddings), or CS329Z Lecture 3, "Retrieval-Augmented Generation (RAG)" (slides https://web.stanford.edu/class/cs329z/slides/lecture03.pdf).
- Gap: no session on skill libraries or workflow memory as such (Voyager, Agent Workflow Memory, agent skill induction) or on plan caching.

### 3.18 Program synthesis and code generation
1. CS329A, Fri Oct 17, "Self improvement with Search & Deep Research Agents". Readings "Competition-Level Code Generation with AlphaCode" (https://arxiv.org/abs/2203.07814) and AlphaCode 2 Technical Report (https://storage.googleapis.com/deepmind-media/AlphaCode2/AlphaCode2_Tech_Report.pdf).
2. CS329A, Mon Nov 3, "Agentic Frameworks for Software Engineering". Readings CodeMonkeys, KernelBench (https://arxiv.org/abs/2502.10517), Agent-System Interfaces (https://arxiv.org/abs/2410.15625).
3. CS329Z Lecture 18, "Coding & Software Agents" (as 3.3), plus Lecture 16, "Guest Lecture: SWE-bench" (reading https://arxiv.org/abs/2310.06770).
4. CS329A, Fri Oct 3, "Learning from feedback with tools/code", reading RLEF (https://arxiv.org/abs/2410.02089): RL from code execution feedback.

## 4. Suggested reading paths per proposal (P05 to P08)

Each path lists modules from Section 3 in reading order, with the reason each one matters for that proposal.

**P05 Evolvability (structure of harness code vs. how far self-improvement gets).**
1. CS329Z Assignment 1, "Building an Agent Harness" and Lecture 5, "Frameworks & Orchestration" (HarnessTax reading): what a harness is and evidence that the harness changes results.
2. CS329A Mon Oct 13 (Darwin Godel Machine): the score-based parent selection and archive that P05 compares against.
3. CS329A Mon Nov 3, Agent-System Interfaces reading: a DSL that structures the search space and a feedback layer that interprets execution output, close to P05's "exposed parameters" and "logged intermediate values".
4. CS329Z Lecture 9, "Optimization" (GEPA): the fixed optimizer reads traces, so logged intermediates are its input.
5. usaaio.guide "Two Models Whose Bands Overlap" and "The Gap Between Two Models on One Test Set": paired analysis across seeds and examples for the factorial design.

**P06 Trace leakage (reflective optimizers that read traces from their own selection set).**
1. usaaio.guide "The Best of Five Noisy Scores" and "Hoeffding's Inequality and Generalization": selection bias and the union bound, the two quantities the leakage gap grows with.
2. usaaio.guide "Margins on a Competition Leaderboard": the simultaneous-guarantee view behind reusable-holdout protocols.
3. usaaio.guide "Copies on Both Sides of the Split" and "Two Scans per Patient": memorization and subject-level leakage, the clinical analog of transfer to new people.
4. CS329Z Lecture 1 ("AI Agents That Matter") and Lecture 13 (Agentic Benchmark Checklist): the agent-evaluation literature that already flags missing holdouts.
5. CS329Z Lecture 9 (GEPA, MIPRO) and CS329A Fri Sep 26 (Archon): the optimizers whose protocols P06 audits.

**P07 Self-designed observations (how a VLM should see numeric tool outputs).**
1. usaaio.guide 1.3 PY3, "Data Visualization": choosing the plot, showing uncertainty, colormaps, and "Checking a plot without looking at it" (read back the data behind a figure in code, the basis of an information-matched control).
2. usaaio.guide 2.20 ML15, "Time Series": the phase-vs-spectrum example shows that the encoding of the same series decides whether a linear reader can use it.
3. usaaio.guide 3.8 TF7, "Vision-Language Models" and UvA Tutorial 15, "Vision Transformers": how patches become tokens, which bounds what fine detail a VLM can read from a plot.
4. UvA Tutorial 10, "Adversarial attacks", section on transferability: a renderer tuned to one reader may exploit that reader, as a patch tuned on ResNet34 partly transfers to DenseNet121.
5. usaaio.guide 3.1 PS4, "Information Theory for AI" (https://usaaio.guide/module/?id=information-theory-core): mutual information, for defining information-matched encodings.
6. CS329A Mon Oct 13 (AlphaEvolve): evolutionary search over code, applied here to plotting code.

**P08 Certified self-compilation (replace deliberation with programs plus validity gates, with guarantees).**
1. CS329Z Lecture 6 (CodeAct) and Lecture 7 (CoALA, MemGPT): code as actions and stored procedures as memory, the substrate of compiled programs.
2. CS329A Fri Sep 26 ("Large Language Monkeys", Snell et al.): the cost of deliberation that compilation saves.
3. UvA DL2 Tutorial 2, uncertainty quantification with conformal prediction: split-conformal mechanics before Learn-then-Test.
4. usaaio.guide "How Often a 95% Interval Covers a Rare Failure Rate" and "Hoeffding's Inequality and Generalization": why finite-sample, multiplicity-corrected bounds are needed for a gate that certifies "no less accurate".
5. usaaio.guide "How Much a Better Model Can Gain" (https://usaaio.guide/theory/?id=bv-noise-floor-from-repeats): the noise floor from repeated measurements, the statistic behind test-retest and minimal detectable change.
6. CS329A Mon Oct 13 (Darwin Godel Machine) and CS329Z Lecture 1 ("AI Agents That Matter", cost and accuracy optimized together): the empirical self-modification and cost-accuracy framing P08 sits between.
