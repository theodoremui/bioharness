### Balance and the StaBLE dataset {#bg-stable}

Balance is the ability to control the body's position and movement without falling. Standing still mostly means keeping the body's weight over the feet; walking or jumping also means controlling momentum and where the feet land. It declines with age and with conditions such as inner-ear disorders, nerve damage in the feet and Parkinson's disease, and poor balance is a common cause of falls. In a clinic, balance is usually tested with simple tasks that are timed with a stopwatch or judged by eye, such as standing on one leg for ten seconds. These tests are coarse. Everyone who lasts the full ten seconds receives the same top mark, whether they stood perfectly still or wobbled the whole time.

StaBLE [@heigold2026] is a dataset built to measure balance more finely. It contains 180 adults aged 18 to 87, from people with balance disorders to professional ballet dancers, acrobats and gymnasts. Each person performed up to 18 tasks, among them standing with eyes closed, standing heel to toe, rising onto the toes, reaching, standing up from a chair five times, standing on one leg, jumping and several kinds of walking. Three smartphones on tripods filmed every task at the same time ({fig:stable-setup}).

@fig stable-setup | figures/papers/stable_fig1_setup.png | The StaBLE recording setup. Three smartphones on tripods film the participant from different angles, and tape on the floor marks where to stand. Reproduced from @{heigold2026}, Fig. 1 (CC BY 4.0).

Each task has goals, and StaBLE turns each goal into a number called a **feature**. This proposal uses the "rise to toes" task as its running example. The person rises onto their toes as quickly and as high as they can and holds the position for five seconds. Three features describe the attempt ({fig:stable-features}):

- **Peak upward speed of the center of mass**, in meters per second. The center of mass is the single point where the body's weight can be treated as concentrated; in a standing person it sits a little below the navel. Rising quickly makes it move upward fast.
- **Peak ankle angle**, in degrees: how far the foot points downward at the highest moment. Rising high requires a large angle.
- **Hold time**, in seconds: how long the center of mass stays above the halfway point of its rise, counted up to the five seconds the task asks for. The count stops at five, so many people share the top value; such a limit is called a **cap**.

@fig stable-features | figures/papers/stable_fig2a_features.png | How StaBLE scores rise to toes. Each goal becomes a feature measured from the 3D reconstruction (gray histograms, bars that count how many participants fall in each range of values, show how the feature varies across the 180 participants), and each feature is rescaled to the range 0 to 1 using the lowest and highest values in the dataset (blue). Reproduced from @{heigold2026}, Fig. 2a (CC BY 4.0).

Numbers in different units cannot be averaged directly, so each feature is **rescaled** to the range 0 to 1:

$$\text{rescaled value} = \frac{\text{value} - L}{U - L},$$

where $L$ and $U$ are the lowest and highest values of that feature in the dataset; StaBLE took them from all 180 participants. (For a feature where smaller is better, such as how much the body sways, the formula is flipped so that 1 is still the best.) If peak upward speeds in the data range from $L = 0.03$ to $U = 0.52$ m/s, a person who reaches 0.30 m/s gets $(0.30 - 0.03)/(0.52 - 0.03) = 0.55$. If $L$ and $U$ are computed from one group of people, a new person can fall slightly outside the range and get a value a little below 0 or above 1. The rescaled features of a task are averaged into a **task score**, normally between 0 and 1, and the 18 task scores are averaged into the overall **StaBLE score** ({fig:chain}). Across the 18 tasks there are 76 features, and higher is better everywhere.

@fig chain | figures/fig_chain.svg | From one video to a task score for rise to toes, with illustrative values. The rescaled features 0.55, 0.75 and 1.00 average to a task score of 0.77.

@fig stable-scores | figures/papers/stable_fig2bc_scores.png | The 18 StaBLE tasks, how each task score is spread across the 180 participants, and the overall StaBLE score, which averages the task scores. Reproduced from @{heigold2026}, Fig. 2b–c (CC BY 4.0).

The StaBLE score behaves as a measure of balance should. It drops steadily with age, it agrees with established clinical balance tests, and it separates people who report a high risk of falling from those who do not [@heigold2026].
