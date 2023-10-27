# Independent Component Analysis
$$ x_n\in\R^D \text{ = Vector of signals recieved at time n} \\ z_n\in\R^D \text{ = Vector of source signals at time n} \\ \text{We assume there is an unkown DxD mixing matrix A} \\ x_n=Az_n $$

Therefore the signal recieved is a linear mixture of signals, we ignore temporal dependence between signals at different time points and treat the data as i.i.d (independent and identically distributed)

This is essentially probabilistic PCA but where the sources are required to be non-gaussian 

$$ p(z_t)=\prod_{j=1}^Lp_j(z_{tj}) \qquad z_{tj}=\text{ sources}\\x_t=Wz_t $$

Given observed values for x_t and a particular choice for p_j we can use MLE to get a value for W so we invent a non-gaussian distribution to use for p_j. 

