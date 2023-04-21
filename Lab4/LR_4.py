# Імпортуємо необхідні бібліотеки
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


path1 = "l4_1.txt"
path2 = "l4_2.txt"


def ford_fulkerson(adj_matrix):
    n = len(adj_matrix)
    flow_matrix = np.zeros((n, n))

    # Create residual graph
    residual_graph = np.copy(adj_matrix)

    # Initialize variables
    max_flow = 0
    path = find_augmenting_path(residual_graph, 0, n-1)

    # Iterate until no augmenting path can be found
    while path:
        # Compute bottleneck capacity
        bottleneck_capacity = min(residual_graph[u][v] for u, v in path)

        # Update flow matrix and residual graph
        for u, v in path:
            flow_matrix[u][v] += bottleneck_capacity
            residual_graph[u][v] -= bottleneck_capacity
            residual_graph[v][u] += bottleneck_capacity

        # Update max flow and find next augmenting path
        max_flow += bottleneck_capacity
        path = find_augmenting_path(residual_graph, 0, n-1)

    return max_flow, flow_matrix

def find_augmenting_path(residual_graph, source, sink):
    n = len(residual_graph)

    # Initialize variables
    visited = [False] * n
    queue = [(source, [])]

    # BFS search
    while queue:
        current, path = queue.pop(0)
        visited[current] = True

        # Check if sink node is reached
        if current == sink:
            return path

        # Add unvisited neighbors to queue
        for neighbor in range(n):
            if residual_graph[current][neighbor] > 0 and not visited[neighbor]:
                queue.append((neighbor, path + [(current, neighbor)]))

    # No augmenting path found
    return None


with open(path1) as f:
    lines = (line for line in f if not line.startswith('#'))
    graph = np.loadtxt(lines, skiprows=1)

G = nx.from_numpy_matrix(np.matrix(graph), create_using=nx.DiGraph)
layout = nx.spring_layout(G)
nx.draw(G, layout)
nx.draw_networkx_edge_labels(G, pos=layout)
plt.show()

print(graph, end="\n\n")
# Визначаємо кількість вершин у графі
V = len(graph)

max_flow, flow_matrix = ford_fulkerson(graph)
# викликаємо функцію tsp()
print("Найбільший потік:" + str(max_flow))
print(flow_matrix)
