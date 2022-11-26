import numpy.random as random
import matplotlib.pyplot as plt
import numpy as np

from copy import copy
from operator import itemgetter

# Parameters
M = 100
p = 0.3
v0 = 0
n_cars = 70
t_max = 1000
v_max = 5

random.seed(1)
roads = np.array( [ [[0,M+0.5], [0.5,0.5]], [[0,M+0.5], [1.5,1.5]] ] )
cars = np.array([[random.randint(1,M), random.randint(1,2)] for _ in range(1,n_cars+1)])
cars = np.array(sorted(cars, key=itemgetter(0)))

total = []
rev = 0
a = 0
v = v0
count = 0
movement = []
queue_cars = [i for i in range(n_cars)]

# Main Program
for t in range(t_max):
    x_row = []
    for i in queue_cars:
        car = cars[i]
        next_car = cars[i + 1 if i + 1 < n_cars else 0]        

        v = np.min([v+1, v_max])        

        if (next_car[0] < car[0]):
            d = M - car[0] + next_car[0]
        else: 
            d = (next_car[0]-car[0])
        v = np.min([v, d-1])

        pr = random.rand()
        if (pr < p):
            v = np.max([0, v-1])

        x = copy(car[0])
        x = x + v
        if (x >= M):
            x = x - M
        x_row.append(copy([x,car[1]]))

    cars = copy(x_row)
    movement.append(cars)

    # density
    if 80 <= t <= 90:
        for j in (movement[t]):
            if j[0] >= 80 and j[0] <= 90:
                count += 1

        print(f'x{t}: {count / len(movement[t]) * 100:.2f}%')
        count = 0

# Average
for i in range(len(movement) - 1):
    if a >= len(movement) - 1:
        break

    a = i + 1
    nextemp = movement[a][2]
    temp = movement[i][2]

    if nextemp[0]<temp[0]:
        if nextemp[0] == movement[a][2][0] or nextemp[0] >= movement[a][2][0]:  
            total.append(a)
            rev += 1

average = total[-1] / rev
print('Time average:', average)

# Plotting
a = np.zeros(shape = (t_max, M)) 
for t in range(t_max):
    for car in movement[t]:
        a[t, car[0]] = 1 if car[1] == 2 else 2

plt.imshow(a, cmap='Greys', interpolation='nearest')
plt.show()
