# Імпортуємо необхідні бібліотеки
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

path1 = "l3_1.txt"
path2 = "l3_2.txt"

def branch_and_bound(adj_matrix):
    # Initialize variables
    n = len(adj_matrix)
    best_path = []
    best_cost = float('inf')
    stack = [(0, [0], 0)]

    # Iterate over stack until empty
    while stack:
        # Pop top element from stack
        node, path, cost = stack.pop()

        # If path is complete, check if it's better than the current best
        if len(path) == n:
            if cost + adj_matrix[node][0] < best_cost:
                best_path = path + [0]
                best_cost = cost + adj_matrix[node][0]

        # Otherwise, expand the node
        else:
            # Get possible next nodes and their costs
            next_nodes = [i for i in range(n) if i not in path]
            next_costs = [adj_matrix[node][i] for i in next_nodes]

            # Sort nodes and costs by increasing cost
            sorted_indices = np.argsort(next_costs)

            # Add nodes to stack in increasing order of cost
            for i in sorted_indices:
                next_node = next_nodes[i]
                next_cost = next_costs[i]
                if cost + next_cost + adj_matrix[next_node][0] < best_cost:
                    stack.append((next_node, path + [next_node], cost + next_cost))

    return best_path, best_cost

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

best_path, best_distance = branch_and_bound(np.array(graph))
result = [str(i) for i in best_path]
print(result)
