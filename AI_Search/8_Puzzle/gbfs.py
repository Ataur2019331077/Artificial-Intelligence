import heapq

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)


def isEqual(state1, state2):
    return state1 == state2

'''
1 2 3   1 2 3   
4 5 6   4 5 6
7 8 0   0 7 8
'''

def heuristic(state):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_i, goal_j = divmod(state[i][j]-1, 3)
                h += abs(i - goal_i) + abs(j - goal_j)
    return h

def generate_next_state(current_state):
    blank_i, blank_j = find_blank(current_state)
    next_states = []

    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for move in moves:
        new_i, new_j = blank_i+move[0], blank_j+move[1]
        if 0<=new_i<3 and 0<=new_j<3:
            new_state = [row[:] for row in current_state]
            new_state[new_i][new_j], new_state[blank_i][blank_j] = new_state[blank_i][blank_j], new_state[new_i][new_j]
            next_states.append(new_state)

    return next_states


def solve_8_puzzle_gbfs(initial_state):
    visited = set()
    priority_queue = [(heuristic(initial_state), initial_state)]

    solution_path = []

    while priority_queue:
        _, current_state = heapq.heappop(priority_queue)

        if isEqual(current_state, goal_state):
            solution_path.append(current_state)
            return solution_path
        
        visited.add(tuple(map(tuple, current_state)))
        solution_path.append(current_state)

        next_states = generate_next_state(current_state)

        for next_state in next_states:
            if tuple(map(tuple, next_state)) not in visited:
                heapq.heappush(priority_queue, (heuristic(next_state), next_state))
    
    return None


initial_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
solution_path = solve_8_puzzle_gbfs(initial_state)

if solution_path:
    print("Solution found!")
    for step, state in enumerate(solution_path):
        print(f"Step {step + 1}:")
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")

