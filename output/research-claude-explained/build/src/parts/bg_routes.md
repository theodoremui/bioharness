### Three ways to turn one video into a score {#bg-routes}

The lab that collected StaBLE has already compared several ways of predicting task scores from a single video, the one taken by the phone on the participant's left (called Cam0). Their pilot study kept 43 participants (729 task scores) aside for testing and trained on the others. The methods fall into three families ({fig:routes}).

@fig routes | figures/fig_routes.svg | Three families of methods for getting a balance score from one video. This proposal develops the third.

**Reconstruct and measure.** Rebuild the 3D body with OpenCap Monocular, then run StaBLE's own feature code on it. Every intermediate result can be plotted and checked, but when one step fails there is no score. In the Y-Balance task, for example, StaBLE's code finds each reach by looking for the moment the toe reverses direction, and on one-camera reconstructions it often found no reach at all. The reconstruction also takes about four minutes of GPU time for a 17-second clip. (A GPU, or graphics processor, is the hardware that runs neural networks; compute in this proposal is counted in **H100-hours**, hours of work on one NVIDIA H100, a data-center GPU.)

**Learn to predict.** Train a neural network ({sec:bg-vlm}) to map the video, or the 2D body landmarks extracted from it, straight to the task score. This always returns a number, but the number comes with no explanation a clinician could check.

**Learn to conduct the analysis.** Give a vision-language model the analysis tools a biomechanist would use and let it choose the tools, inspect their outputs and write the code that computes each feature. The fixed StaBLE formula then turns the features into the score. This is the route this proposal develops.

{fig:pilot} shows the pilot results. The error measure is the **mean absolute error**. For every test case, take the absolute difference between the predicted task score and the reference task score; average these within each task; then average the 18 task values so that each task counts equally. An error of 0.10 means that predictions miss by a tenth of the 0-to-1 scale on average.

@fig pilot | figures/fig_pilot.svg | Pilot results on 43 held-out participants (lower is better). The dashed line marks the constant guess, which ignores the video entirely. OpenCap Monocular's error is computed only on the 567 cases where it produced a score, so it is not directly comparable with the other bars, which cover all 729.

The best method, the Qwen3-VL-8B model fine-tuned to output scores (fine-tuning is explained in {sec:bg-levers}), reached an error of 0.100, while predicting each task's average training score for everyone, without looking at the video, reached 0.120. The best learned model thus beats a constant guess by only about a sixth. The same model without fine-tuning did worse than the constant guess (0.238), and it was still worse when asked to report features and let a formula compute the score (0.179). Reading a speed in meters per second off raw pixels is a poor fit for these models.
