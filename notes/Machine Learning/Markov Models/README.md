# Markov Models
## Sequential Data:

- The i.i.d. assumption ignores any ordering of the data points

- Data points often occur in a sequence such as a sequence of words in sentence, frames in a video or sensor observations over time

- This can be generalised to more than one dimension.

- Treating the timestamp is not generally an informative feature but the neighbouring data can be useful

We can model these neighbourhood dependencies:

![Untitled](ef477325_Untitled.png)

<br/>

- Stationary Distribution: Probability distribution remains the same over time ⇒ Homogeneous Markov chain

- The number of parameters increases exponentially with the order of the Markov Chain. Meaning higher-order models are often impractical.

For each state we have:

- Transition Distribution - Modelling dependencies betweeen states $ p(z_n|z_{n-1}) $

- Emission Distribution - Models observations given a latent state $ p(x_n|z_n) $

![Untitled](377ad577_Untitled.png)

 

Emission Distributions:

Real valued observations may use gaussian emissions, discrete observations may use a categorical distribution.

For each observation there are K values of $ p(x_n|z_n,\phi_n) $ one fore each possible value of unobserved z_n

<br/>

The complete HMM can be defined by the joint distribution over observations and latent states:

$$ p(X,Z|A,\pi,\phi)=p(z_1,\pi)\prod_{n=2}^Np(z_n|z_{n-1},A)\prod_{n=1}^Np(x_n|z_n,\phi) \\ {} \\ A, \pi, \phi \text{ are parameters that must be learned}  $$

<br/>

