# Segmentation Basics
**Image Segmentation:**

The process of spatial subsectioning of a digital image into multiple portions of pixels according to a given criteria.

- Image simplification

- Higher-level object description

	- Regions belonging to the same object

	- Regions provide properties such as shape and colour.

- Input for content classifiers

**Top-Down:**

Pixels belong together because they are from the same object.

**Bottom-Up:**

Pixels belong together because they look similar.

<br/>

The effects of noise, non-uniform illumination, and occlusions give rise to the problem of over-segmentation and under-segmentation.

**Over-segmentation:**

Pixels belonging to the same region are classified as belonging to different regions.

**Under-segmentation:**

Pixels belonging to different regions are classified as belonging to the same region.

**Methods:**

- Thresholding based on intensity

- Edge-based - regions are constructed from edge maps

- Region-based - Region growing from seed pixels.

- K-Means clustering

**Threshold Selection Algorithm:**

1. Select an initial estimate for the threshold T

2. Segment the image using T, producing two groups of pixels greater than T and less than T

3. Compute the average grey level value for both groups, m1 and m2 

4. Compute a new threshold value T = (m1 + m2) / 2

5. Repeat until convergence.

**Split and Merge Segmentation:**

Homogeneity function H - defines whether a region contains enough variance to be segmented

H(Region A) = 1 ⇒ Homogeneous

H(Region B) = 0 ⇒ Non homogeneous

1. Start with R0 which represents the entire image

2. If H(Ri) = 0 then split the area into 4 blocks (quadtree splitting)

3. Merage all subregions that pairwise satisfy H(Ri U Rj) = 1

**Conceptual Summary:**

Iteratively split image into regions of a maximally sized selected shape that does not satisfy the homogeneity function. Merge regions together that together satisfy homogeneity.

 Using quadtrees can result in blocky images, we can fix that by using an adaptive homogeneity condition that could change depending on the region size.

**Clustering:**

The aim of clustering is the minimise the distance between each cluster point and its centre.

$$ \Theta(\text{clusters},\text{data})=\sum_{j\in\text{Clusters}}[\sum_{i\in\text{jth cluster}}||x_i-\mu_j||^2] $$

$$ \text{K-Means Clustering: }\\\text{1. Randomly initialise K vectors }\mu_1,...,\mu_k \\ \text{2. Assign each }x\in\text{ Features to the nearest }\mu \\ \text{3. Recompute }\mu_j\text{ as the mean of the points assigned to it}\\ \text{4. Repeat until there is not change in }\mu_1,...,\mu_k $$

This will attempt to minimise the sum squared difference between the data points and their cluster centres. This algorithm will always find a local optimum but not necessarily a global optimal value for each cluster centre.

**Pros:**

- Fast to compute

- Always converges to a local minimum

**Cons:**

- We have to choose the number of clusters

- It is sensitive to the initial centres chosen randomly

- Sensitive to outliers

- Detects spherical outliers 

