import numpy as np
import matplotlib.pyplot as plt

# Parameters
M = 100
v0 = 0
d = 2
p = 0.3
v_max = 5
t_max = 1000
density = 0.7

# Initial state
cars_num = int(density * M)
initial = [0] * cars_num + [-1] * (M - cars_num)
np.random.shuffle(initial)

# Evolution
iterations = [initial]

# Iteration
for i in range(t_max):
    prev,curr = iterations[-1],[-1] * M

    for x in range(M):
        if prev[x] > -1:
            vi = prev[x]
            d = 1
            while prev[(x + d) % M] < 0:
                d += 1

            vtemp = min(vi+1, d - 1, v_max)
            v = max(vtemp - 1, 0) if np.random.uniform(0,1) < p else vtemp
            curr[(x + v) % M] = v
            
    iterations.append(curr)

# Plotting
a = np.zeros(shape=(t_max,M))
for i in range(M):
    for j in range(t_max):
        a[j,i] = 1 if iterations[j][i] > -1 else 0

plt.imshow(a, cmap="Greys", interpolation="nearest")
plt.show()