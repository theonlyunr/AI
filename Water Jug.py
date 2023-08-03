from collections import deque
def water_jug_bfs(capacity_a, capacity_b, target):
    queue = deque()
    visited = set()
    # Initialize the starting state with both jugs empty (0 liters each)
    queue.append((0, 0))
    visited.add((0, 0))
    while queue:
        current_state = queue.popleft()
        jug_a, jug_b = current_state
        if jug_a == target or jug_b == target:
            return current_state  # Solution found
        # Generate all possible next states by filling, pouring, or emptying the jugs
        next_states = [
            (capacity_a, jug_b),  # Fill Jug A
            (jug_a, capacity_b),  # Fill Jug B
            (0, jug_b),           # Empty Jug A
            (jug_a, 0),           # Empty Jug B
            (jug_a - min(jug_a, capacity_b - jug_b), jug_b + min(jug_a, capacity_b - jug_b)),  # Pour from A to B
            (jug_a + min(jug_b, capacity_a - jug_a), jug_b - min(jug_b, capacity_a - jug_a))   # Pour from B to A
        ]
        for state in next_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)
    return None  # No solution found
def main():
    print("Water-Jug Problem Solver using BFS")
    capacity_a = int(input("Enter the capacity of Jug A: "))
    capacity_b = int(input("Enter the capacity of Jug B: "))
    target_amount = int(input("Enter the target amount: "))
    result = water_jug_bfs(capacity_a, capacity_b, target_amount)
    if result:
        print(f"Solution Found: Jug A: {result[0]} liters, Jug B: {result[1]} liters.")
    else:
        print("No solution found for the given capacities and target amount.")
if __name__ == "__main__":
    main()

