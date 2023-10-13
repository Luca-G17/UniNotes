# Clustering
Soft clustering by MLE of a Gaussian mixture:

- Given data x and a fixed number of component Gaussian we can use maximum likelihood estimation to get a particular Gaussian mixture distribution.

- This achieves soft clustering.

$$ \text{log likelihood = }\ln(p(X|\pi,\mu,\Sigma)=\sum_{n=1}^N\ln(\sum_{k=1}^K\pi_k\mathcal{N}(x_n|\mu_k, \Sigma_k)) $$

- This has problems as this space will have lots of local maxima.

- 

