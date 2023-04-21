# Імпортуємо необхідні бібліотеки
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import itertools
from prettytable import PrettyTable


path1 = "l2_1.txt"
path2 = "l2_2.txt"
path3 = "l2_3.txt"


def tsp(weights_matrix):
    # ініціалізуємо змінні
    n = len(weights_matrix)
    nodes = range(n)
    best_path = None
    best_distance = float('inf')

    # перебираємо всі можливі перестановки вузлів
    for path in itertools.permutations(nodes):
        distance = 0

        # розраховуємо загальну відстань по маршруту
        for i in range(n - 1):
            distance += weights_matrix[path[i]][path[i + 1]]
        distance += weights_matrix[path[-1]][path[0]]  # додаємо відстань від останнього вузла до першого

        # перевіряємо, чи є даний маршрут найкращим
        if distance < best_distance:
            best_distance = distance
            best_path = path

    # повертаємо найдешевший маршрут та його відстань
    return best_path, best_distance
# Граф на основі матриці суміжності


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

# викликаємо функцію tsp()
best_path, best_distance = tsp(graph)
result = [i for i in best_path]
table = PrettyTable(result)
print(table)
