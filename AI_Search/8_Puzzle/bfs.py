from collections import deque

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)


def generate_next_state(current_state):
    blank_i, blank_j = find_blank(current_state)
    next_state = []

    for move in moves:
        new_i, new_j = move[0]+blank_i, move[1]+blank_j

        if 0<=new_i<3 and 0<=new_j<3:
            new_state = [row[:] for row in current_state]
            new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
            next_state.append(new_state)

    return next_state

def isEqual(state1, state2):
    return state1 == state2


def solve_8_puzzle_bfs(initial_state):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if isEqual(current_state, goal_state):
            return path
        
        if tuple(map(tuple, current_state)) not in visited:
            visited.add(tuple(map(tuple, current_state)))
        
        next_states = generate_next_state(current_state)

        for next_state in next_states:
            queue.append((next_state, path+[next_state]))
    
    return None

initial_state = [[1, 2, 3], [4, 5, 7], [8, 6, 0]]
solution_path = solve_8_puzzle_bfs(initial_state)

if solution_path:
    print("Solution found!")
    for step, state in enumerate(solution_path):
        print(f"Step {step + 1}:")
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
