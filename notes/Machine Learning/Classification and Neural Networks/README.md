# Classification and Neural Networks
**Classification:**

Model - A discriminant function is a function that takes an input vector x and assigns it to a class Ck.

Linear Discriminant Function:

$$ y(x)=w_0+w^Tx \qquad w_0=\text{bias} \qquad x=\text{input vector}\qquad w=\text{weights} $$

For K = 2 if y(x) ≥ 0 add to class C1 else add to class C2

We can minimise the least squares (error function) to compute the optimal parameters.

This model only works for data that is linearly separable

<br/>

**Logistic Functions:**

A logistic function can be used to obtain a probability of being in class Ck. For example:

	 

	$$ y(x)=\sigma(w^Tx)\qquad p(C_1|x)=y(x) \qquad p(C_2|x)=1-p(C_1|x) $$

When y→0 choose class 2 and when y→1 choose class 1.

**Logistic Regression - Maximum Likelihood Estimation:**

$$ p(t|x,w)=\prod_{n=1}^Ny_n^{t_n}(1-y_n)^{1-t_n}\qquad y_n=p(C_1|x_n)\qquad t_n \in\{0,1 \} \qquad \text{dataset} = \{n_n, t_n \} $$

In order to find the derivative of the negative log of this model we have to use an iterative technique to find a local minimum. We start with random weights and perform gradient descent.

$$ \frac{\delta \ln p(t|x,w)}{\delta w}\sum_{n=1}^N(y_n-t_n)x_n =\text{slope} $$

<br/>

