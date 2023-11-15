# Motion Estimation
The relationship between varaition in pixels - known as apparent motion or optical flow - and the true motion is not trivial.

- Apparent motion/Optical Flow - Perceived mtoion in the video sequence caused by changes in pixel values.

- Sometimes its not possible to determine 2-D motion field without additional constraints or assumptions

**Optical Flow:**

- Assume optical flow results from a **brightness constancy contraint **- A moving pixel retains its value between frames

- For continuous video I(x, y, t):

$$ I(x+\Delta x,y+\Delta y,t +\Delta t)=I(x,y,t) \\ \text{Using Taylor Series (Higher Order Terms}\rightarrow \text{0 for small delta)}\\ I(x+\Delta x,y+\Delta y,t +\Delta t)=I(x,y,t) +\frac{\delta I}{\delta x}\Delta x+\frac{\delta I}{\delta y}\Delta y+\frac{\delta I}{\delta t}\Delta t \\ {} \\ \frac{\delta I}{\delta x}\Delta x+\frac{\delta I}{\delta y}\Delta y+\frac{\delta I}{\delta t}\Delta t=0 \\ \text{Divide by }\Delta t \\\frac{\delta I}{\delta x}\frac{\Delta x}{\Delta t}+\frac{\delta I}{\delta y}\frac{\Delta y}{\Delta t}+\frac{\delta I}{\delta t}\frac{\Delta t}{\Delta t}=0 $$

The rate of change of x and y with time:

$$ \text{Optical flow field u}=(u_x,u_y) \\ \text{Spatial and temperal gradients = }(I_x,I_y,I_t) $$

**Normal Flow:**

$$ \text{OFE for u}=(u_x,u_y) \text{ and }\nabla I=(I_x,I_y) \\ I_xu_x+I_yu_y+I_t=0\rightarrow\nabla I.u+I_t=0 $$

Therefore the OFE alone is not sufficient to estime motion. We can only estimate normal flow, i.e the flow in the direction of the spatial graident normal, u_n is the motion field in the direction of the normal.

$$ \nabla I.u+I_t=\nabla I.u_n+I_t=0 \qquad ||U_n||=\frac{-I_t}{||\nabla I||} \\ \angle u_n=\angle \nabla I $$

This means that good motion estimations depend on having sufficient varitation in spatial gradients.

**Constraining the OFE:**

OFE is under-constrained, can only estimate normal flow. We must add extra constraints. For example we can assume parametric form of motion field in regions.

For example linear (Affine):

$$ u_x=ax+by+c\\u_y=dx+ey+f $$

**Constant Velocity Model:**

For a region, find the velocity u which minimises:

$$ \epsilon(u_x,u_y)=\sum_{\text{region}}(I_xu_x+I_yu_y+I_t)^2 \\ \frac{\delta\epsilon}{\delta x}=2\sum_{\text{region}}(I_xu_x+I_yu_y+I_t)I_x=0 \\ \frac{\delta\epsilon}{\delta y}=2\sum_{\text{region}}(I_xu_x+I_yu_y+I_t)I_y=0 \\ \text{We can write these equations in matrix form: }Au=b \\ A=\sum_{\text{region}}\begin{bmatrix}I^2_x & I_xIy \\ I_xIy & I^2_y\end{bmatrix} \qquad b=-\sum_{\text{region}} \begin{bmatrix}-I_tIx \\ -I_tIy\end{bmatrix} \qquad u=A^{-1}b $$

**Spatial and Temporal Gradients:**

$$ I_x=\frac{\delta I}{\delta x}\approx I(x+1,y,t)-I(x,y,t)\\ \text{i.e. assume }\delta x=\text{1} $$

**Luckas and Kanade Algorithm:**

- For a pair of frames at time t and time t+1

- For each pixel x and y in the first frame

- For each pixel the region about x and y

- Compute the spatial gradients, compute A and B sum for each pixel x and y.

- Use A and B to get the motion field.

<br/>

