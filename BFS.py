graph = {
  1: [3, 7],
  3: [8, 4],
  7: [10],
  8: [],
  4: [10],
  10: []
}

visited = []  # List for visited nodes.
queue = []    # Initialize a queue

def bfs(visited, graph, node):  # Function for BFS
    visited.append(node)
    queue.append(node)

    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Driver Code
print("Enter the start node:")
start_node = int(input())
print("Following is the Breadth-First Search")
bfs(visited, graph, start_node)  # Function calling
