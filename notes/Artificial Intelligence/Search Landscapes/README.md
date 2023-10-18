# Search Landscapes
The set of possible genotypes is the GA’s search space, S

Given geneotypes of length L from alphabet of size A:

- The space has L dimensions which each have A possible values

- Therefore there are A^L possible genotypes in S

- Each genotype is a point in the search space

- Genotypes are neighbours if they differ by one mutation

The structure of a search space determines how hard it will be to search

The search space can be visualised a fitness landscape where the fitness of each genotype is the height at that point.

<br/>

**Landscape Structures:**

Needle-in-a-haystack:

All genotypes except for one have the same low fitness value, this is a very hard landscape to search. The fitness function is unhelpful as it has no gradient to exploit.

<br/>

Random Landscape:

Hard to search since its full of suboptimal genotypes that give us no information about the optimal solution.

<br/>

A Nice Landscape:

- Local smoothness, nearby points have similar fitness = Correlation Structure

- High peaks are broad = Non-deceptive

- Can be divided into parts = Decomposable

We can define the distance between points a and b in terms of how easy it is for the algorithm to move between them

- a and b are neighbours if a can reach b in one genetic operation (a single mutation)

**Modality:**

- A landscape with one global optimum is **unimodal**

- A landscape with two optima is **bimodal**

- A landscape with many optima is **multimodal**

- A set of points that lie of hill-climbing routes that terminate at one local optimum are said to lie within the **basin of attraction **of that local optima.

- 

