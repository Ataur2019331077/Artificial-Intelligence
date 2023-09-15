# 8-Puzzle Solver using BFS and GBFS
This repository contains Python implementations of two popular search algorithms, **Breadth-First Search (BFS)** and **Greedy Best-First Search (GBFS)**, applied to solve the 8-Puzzle problem. The 8-Puzzle is a classic sliding puzzle game where you must rearrange the tiles to get them in the correct order, typically from 1 to 8 in a 3x3 grid.

## Problem Description
The 8-Puzzle problem is a well-known problem in the field of artificial intelligence and computer science. It involves a 3x3 grid with eight numbered tiles and an empty space. The goal is to reach a target configuration from an initial configuration by moving the tiles into the empty space.

## Algorithms
## Breadth-First Search (BFS)
Breadth-First Search is an uninformed search algorithm that explores all possible states in a systematic manner, starting from the initial state. It guarantees the shortest solution if one exists but can be memory-intensive for larger problems.

### Greedy Best-First Search (GBFS)
Greedy Best-First Search is an informed search algorithm that uses a heuristic function to estimate the cost of reaching the goal from each state. It always expands the node that appears to be closest to the goal according to the heuristic. GBFS may not always find the optimal solution but can be more memory-efficient than BFS.
