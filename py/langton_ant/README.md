# Langton's Ant

The Langton's ant is a two-dimensional universal Turing machine, which like other cellular automata works under a very simple set of rules but can conduct to complex emergent behavior. It was invented by Chris Langton in 1986 and runs on a square lattice of black and white cells. 
The Langton's ant is Turing complete and his universality was proven in 2000. However, the idea has been generalized in several different ways, such as turmites which add more colors and more states.
This Turing machine works with 2 symbols and 4 states. It consists of a grid of cells along with an ant that is located on one of the cells and faces one of the four cardinal direction. Squares on the grid can be colored variously either black or white. One of these cells is arbitrarily chosen  as the ant and this one can travel in any of the four cardinal directions at each step if takes, according to the following rules.

- At a blank cell, turn 90 degree right, toggle the cell and move forward.
- At a marked cell, turn 90 degree left, toggle the cell and move forward.

*It's important to notice that the Langton's Ant can also be described as a cellular automata, where the grid is colored back or white and the ant is a square that has one of eight different colors assigned to encode the combination of black-white state and the current direction of motion of the ant.*

**Implementation at simple_ant.py**

# My Exploration 

In the original version, we observe different modes of behavior. These simple rules lead to complex structures from which we can distinguish three distinct modes that appears, when starting on a completely white grid (as in our simulation, where the grid is set to be completely blank at start time). These modes are:

- Simplicity, which is observed during the first few hundred moves it creates a very simple patterns which are often symmetric.
- Chaos, which appears after the simplistic mode. A large, irregular pattern of black and white squares appears. The ant traces a pseudo-random path until around 10 thousands steps.
- Emergent order, which after the chaotic mode, appears and the ant describes what we call a recurrent "highway" pattern of 104 steps that indefinitely repeats.

Curiosity can lead one to think about what would appear if the where multiple agents interacting in the same board? What if they are operating with completely different rules? symmetric rules? Does this emergent mode always happen regardless of the configuration, number of ants and rules?  And trying to answer the last question, one experiment has proven the contrary and it could be the departure point of a bigger research. The idea leads to the following conjecture:

>If two ants are interacting in the grid, in a configuration such that they are governed by the same rules but having directions such as the direction's vectors can form a rotation matrix, regardless of the configuration, there will be an infinite
>loop of reiteration of a specific pattern where the emergent mode never happen and the ants keep permutating there positions at each iteration and this is regardless of their distance (apparently). 

**Implementation in rotating_system.py**
