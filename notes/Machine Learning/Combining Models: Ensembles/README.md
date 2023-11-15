# Combining Models: Ensembles
**Bayesian Model Averaging (BMA):**

- Model selection does not always pick out one model, h, as a clear winner.

- We may be uncertain about which model is correct

- We can express uncertainty by assigning a weight to each model. We can take an expectation.

- Our predictions now come from a wieghted sum over the models

$$ p(z|X)=\sum_{h=1}^Hp(z|X,h)p(h|X) $$

- This sum is marginalising over h, since h is an unkown variable we consider all the possible h and calcuated the weighted sum given h

- We can apply bayes rule to estimate the weights

$$ p(h|X)=\frac{p(X|h)p(h)}{\sum_{h'=1}^Hp(X|h')p(h')} $$

We have to assign a prior first for each H.

- As we increase the amount of data in X, this will converge onto one model. BMA then becomes a soft model selection, it doesn’t combine the models to make a more powerful model.

**Ensemble Bagging:**

- Ensembles combine different models, outperforming the average individual. It is different to BMA as BMA attempts to identify a single correct model. The wieghts do not provide the optimal combination

- Given a set of models, 1,…,M, y_m(x) is the prediction from model m. A simple ensemble is the mean of the indivual predictions

$$ \text{Mean: }y_{com}=\frac{1}{M}\sum_{m=1}^My_m(x) \\ \text{Error of combination: }(y(x)-y_{com}(x))^2 =\frac{1}{M}\sum_{m=1}^M((y(x)-y_m(x))^2)\\ \text{Expected Error: }E_x[(y(x)-y_{com}(x))^2]=E_{com} \\ \text{Expected Average Error: } \frac{1}{M}\sum_{m=1}^ME[((y(x)-y_m(x))^2)]=E_{AV} \\ E_{com}=\frac{1}{M}E_{AV} $$

- This relies on the two asusmptions that each model has zero mean, and that the errors of different models are not correlated

- This assumptions are generally not true. In practice they are usually highly correlated and biased. We can never really achieve the E_com = 1/m X E_AV

- However the combined error can never be wrose that the average error E_com ≤ E_AV

- The result tells us that models should be diverse to avoid repeating the same errors

**Boostrap Aggregation (Bagging):**

- Create diversity by training models on different samples of the training set.

- For each model m randomly sample N data points with replacement from a training set with N data points and train m on the subsample

- In each sample, some data points will repeated and others will be emitted

- We can then combine predications by taking the mean (regression) or majority vote (classification)

**Boosting:**

- We can modify the training data to overcome errors in other classifies.

- Train base models sequentally, ensuring that each base model addresses the weaknesses of the ensemble.

- Instead of random sampling, weight the data points in the training set according to the performance of the previous base models. So it will make fewer errors on the data points that the previous models made errors on.

- AdaBoost is a popular boosting method.

**AdaBoost:**

Train a new classifier on wieghted data that outputs class labels +1 or -1. At the start the weights are all equal for each data point. Then we can compute the weights from the performance of the previous classifier. We train M different classifiers. We then take all their predictions and combine them using: 

$$ Y_M(x)=\text{sign}\left(\sum_m^M\alpha_my_m(x)\right) $$

Data Weights:

1. Initialise weights:

$$ w^1_n=\frac{1}{N} $$

1. Compute the weighted error rate of model m:

$$ \epsilon_m\frac{\sum_{n=1}^Nw^m_n[y_m(x_n\ne y(x_n)]}{\sum_{n=1}^Nw^m_n} $$

1. Update the wieght for each data point n

$$ w_n^{m+1}=\begin{cases}w_n^m(\frac{1-\epsilon_m}{\epsilon_m}) & \text{if } y_m(x_n)\ne y(x_n) \\ w^m_n & \text{if } y_m(x_n)= y(x_n)\end{cases} $$

Then we choose our weight alpha for m that minimises the exponential loss of m:

$$ \alpha_m=\ln\left\{ \frac{1-\epsilon_m}{\epsilon_m}\right\} $$

- Weights are highter for classifiers with a lower error rate.

- Not that alpha is a log odds function AdaBoost optimises the log odds ratio

**Stacking:**

- Given a trained set of base classifiers, we learn the combination function

- Bagging: The combination function was majority vote - unweighted

- AdaBoost: A weighted sum of classifier ouputs determined by a model of error rates

- Stacking: Use another classifier or regresssor to learn a combination function that minimises the error rate of the entire ensemble. 

**Decision Trees:**

- Attempts to classify data based on a series of conditionals at each node in a tree.

- In order to learn a decision tree we need to know which variable to use at each node, what threshold to set for the split at each node.

- A common method used is a classification and regression tree (CART).

- It will greedily minise the errors:

	- Regression: Sum of squares errors

	- Classification: Cross entropy

- It will choose the best split greedily at each point. 

	- Start from the root node

	- Run an exhaustive serach over each possible variable and threshold for a new node

		- Compute the average of the target variable for each leaf node of the proposed node.

		- Compute the error if we stopped added nodes here. 

	- Choose the variable and threshold that minise this error

	- Add a new node for the chosen variable and threshold

	- Repeat until there are only n data points associated with each leaf node.

	- Prune back the tree to remove branches that do not reduce error by more than a small tolerance value. This will reduce overfitting.

**Pruning:**

- Balance residual training-set error against model-complexity

- Start with a tree T_0

- Consider pruning each node in T_0 by combining the branches to obtain tree T. 

- Compute the following criterion

$$ C(T)=\sum_{\tau=1}^{|\Tau|}e_\tau(T)+\lambda|T| \\ \text{if }C(T) \le C(T_0) \text{ Keep the pruned tree} $$

**Interpretability:**

- The sequence of decisions is often easier to interpret in decision trees than in neural networks. However, sometimes small changes to the dataset cause big changes to the tree.

- If the non-optimal decision boundary is not aligned with the axes of an input variable we may need lots of splits.hyfyhfyxdfykhdfxfdyhk

