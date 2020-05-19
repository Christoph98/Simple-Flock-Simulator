# Simple Flock Simulator
Skeleton code was given by my professor Orit Peleg, the equations and repulsive bodies I implemented.

As the name of the project suggests, this is a very simple flock simulator. It shows the emergent behavior of a flock where the 
movement of each body in the flock is determined by 4 factors:
- **Attraction force**, a body of the flock is attracted to other bodies around it. Given by summing over the distance vectors beween one body to all other bodies.

<img src="https://render.githubusercontent.com/render/math?math=\displaystyle v1_n = v1_n %2B \sum_{m=0, m\neq n}^N  c1\times(p_m - p_n)">

- **Repulsion force**, a body of the flock is repulsed by other bodies around it. Given by summing over all bodies and calculating the ratio
of the distance vector between the body at hand and the current iteration body over the euclidean distance of that squared.

<img src="https://render.githubusercontent.com/render/math?math=\displaystyle v2_n = v2_n - \sum_{m=0, m\neq n}^N  \frac{c2\times(p_m - p_n)}{(p_{mx} - p_{nx})^2 %2B (p_{my} - p_{ny})^2}">

- **Flock Alignment**, a body of the flock tends to follow the direction of the flock. Given by summing over all bodies's velocities.

<img src="https://render.githubusercontent.com/render/math?math=\displaystyle v3 = c3 \times \sum_{m=0}^N v_m">

- **Random Movement**, a body of the flock tends to have some random motion. Given by a random x and y number given by a gaussian distribution.

<img src="https://render.githubusercontent.com/render/math?math=\displaystyle v3 = c4 \times randn(2,1)">

The code also allows for creation of a barrier to see how the flock avoids the barrier simply given by the emergent behavior of it.
