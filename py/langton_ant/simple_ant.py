"""
The Langton's Ant is a cellular automata that works on the following rules :
Squares on a plane are colored variously either black or white. We arbitrarily
identify one square as the 'ant'. The ant can travel in any of the four cardinal
directions at each step it takes. It moves according to the rules below:
  - At a white square, turn 90 degree clockwise, flip the color of the square,
  move forward one  unit.
  - At a black square, turn 90 degree counter-clockwise, flip the color of the 
  square, move forward one unit.
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

dim = 200
a = np.matrix(np.zeros((dim, dim)))
pos = np.matrix([[dim // 2], [dim // 2]])
direction = np.matrix([[1], [0]])

# Defining the matrices for rotation
clockwise_rotation = np.matrix([[0, 1], [-1, 0]])
counter_rotation = np.matrix([[0, -1], [1, 0]])


def take_step(a, ant_direction, position):
    position[:] = position + ant_direction
    if a[position[0, 0], position[1, 0]] == 0:
        a[position[0, 0], position[1, 0]] = 1
        ant_direction[:] = clockwise_rotation * ant_direction
    else:
        a[position[0, 0], position[1, 0]] = 0
        ant_direction[:] = counter_rotation * ant_direction


fig = plt.figure()
im = plt.imshow(a, interpolation='none', vmin=0, vmax=1)


def animate(i):
    take_step(a, direction, pos)
    im.set_data(a)
    print(i)
    return [im]

anim = FuncAnimation(fig, animate, frames=15000,
                     interval=0, blit=True, repeat=False)
plt.show()
