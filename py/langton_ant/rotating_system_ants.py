"""
Now, the main goal is to write a program that allows us to simulate the
behaviour of multiple agents interacting with the same rules. The last 
step is to identify, if there exist what we can call class of behaviours 
where different behaviours can lead to specific patterns.

Conjecture:
In a configuration with two ants acting with the same rules going in
directions such as the direction's vectors can form a rotation
matrix, regardless of the configuration, there will be an infinite
loop of reiteration of a specific pattern where a chaotic (or emergent) 
mode of one will interact with the other one and destroy the
apparent stabilization.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Creating the universe
dim = 400
a = np.matrix(np.zeros((dim, dim)))

pos_1 = np.matrix([[dim//2], [dim//2]])
direction_1 = np.matrix([[0], [-1]])

pos_2 = np.matrix([[dim//2], [2*dim//5]])
direction_2 = np.matrix([[1], [0]])

# Defining the matrices for rotation
clockwise_rotation = np.matrix([[0, 1], [-1, 0]])
counter_rotation = np.matrix([[0, -1], [1, 0]])


def take_step(board, pos1, pos2, direction1, direction2):
    """To make it work for more than two agents, we can just
    use python list to provide the arguments of the same types."""

    pos1[:] = pos1 + direction1
    pos2[:] = pos2 + direction2
    if board[pos1[0, 0], pos1[1, 0]] == 0:
        board[pos1[0, 0], pos1[1, 0]] = 1
        direction1[:] = clockwise_rotation * direction1
    else:
        board[pos1[0, 0], pos1[1, 0]] = 0
        direction1[:] = counter_rotation * direction1

    if board[pos2[0, 0], pos2[1, 0]] == 0:
        board[pos2[0, 0], pos2[1, 0]] = 2
        direction2[:] = clockwise_rotation * direction2
    else:
        board[pos2[0, 0], pos2[1, 0]] = 0
        direction2[:] = counter_rotation * direction2


fig = plt.figure()
im = plt.imshow(a, interpolation='none', vmin=0, vmax=2)


def animate(i):
    take_step(a, pos_1, pos_2, direction_1, direction_2)
    im.set_data(a)
    print(i)
    return [im]


anim = FuncAnimation(fig, animate, frames=100000,
                     interval=0, blit=True, repeat=False)
plt.show()
