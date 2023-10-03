# Filtering Images
**Median Filter:**

Returns the median value of the pixels in a neighbourhood. 

**Sharpening Filter:**

	$$ \begin{bmatrix} -1 & -1 & -1\\-1 & 4& -1 \\ -1 & -1 & -1\end{bmatrix}=\text{basic sharpening filter} $$

Highlights edges and removes blurred parts of images. This is based on spatial differentiation, suppressing neighbouring pixels and increasing the weight of the current pixel.

Original Image - Smoothed Image = Detail

Original Image + Weight * Detail = Sharpened Image

<br/>

The 2nd derivative is more useful for image sharpening or enhancement than the first derivative as it has a stronger response to fine detail.

**Laplacian Filter:**

$$ \begin{bmatrix} 0 & 1 & 0\\1 & -4& 1 \\ 0 & 1 & 0\end{bmatrix}=\text{Laplacian sharpening filter} $$

$$ \nabla^2f=[f(x+1,y)+f(x-1,y)+f(x, y+1)+f(x,y-1)]-4f(x,y) $$

**Filtering is used to achieve:**

- Enhancement

- Smoothing

- Template mathcing

- Feature Extraction

- Analysiszx

