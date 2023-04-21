# Імпортуємо необхідні бібліотеки
import sys
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
# Граф на основі матриці суміжності

path1 = "l1_1.txt"
path2 = "l1_2.txt"
path3 = "l1_3.txt"

with open(path1) as f:
    lines = (line for line in f if not line.startswith('#'))
    graph = np.loadtxt(lines, skiprows=1)

G = nx.from_numpy_matrix(np.matrix(graph), create_using=nx.DiGraph)
layout = nx.spring_layout(G)
nx.draw(G, layout)
nx.draw_networkx_edge_labels(G, pos=layout)
plt.show()


print(graph)
# Визначаємо кількість вершин у графі
V = len(graph)

class Graph:

    def __init__(self, graph, vertices):
        self.V = vertices
        self.graph = graph

    # Функція для знаходження вершини з мінімальною вагою ребра
    def minKey(self, key, mstSet):

        # Ініціалізуємо мінімальне значення
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    # Функція для знаходження вершини з максимального вагою ребра
    def maxKey(self, key, mstSet):

        # Ініціалізуємо мінімальне значення
        max = -sys.maxsize

        for v in range(self.V):
            if key[v] > max and not mstSet[v]:
                max = key[v]
                max_index = v
        return max_index

    # Функція для виведення мінімального кісткового дерева
    def primMST(self, phonk=0):

        # Зберігаємо ключі та батьківські вершини
        if not phonk:
            key = [sys.maxsize] * self.V
        else:
            key = [-sys.maxsize] * self.V
        parent = [None] * self.V  # Зберігаємо конструкцію MST
        key[0] = 0  # Забезпечуємо першій вершині ключ зі значенням 0
        mstSet = [False] * self.V

        parent[0] = -1  # Перший вузол є кореневим в MST

        for cout in range(self.V):

            # Вибираємо вершину з мінімальним або максимальним ключем
            if phonk:
                u = self.maxKey(key, mstSet)
            else:
                u = self.minKey(key, mstSet)

            # Додаємо вершину до MST Set
            mstSet[u] = True
            if not phonk:
                # Оновлюємо значення ключів та батьківських вершин сусідніх вершин
                for v in range(self.V):

                    # graph[u][v] непорожнє, mstSet[v] дорівнює False та ключ v більший за вагу ребра (u,v)
                    if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u
            else:
                # Оновлюємо значення ключів та батьківських вершин сусідніх вершин
                for v in range(self.V):

                    # graph[u][v] непорожнє, mstSet[v] дорівнює False та ключ v більший за вагу ребра (u,v)
                    if self.graph[u][v] > 0 and not mstSet[v] and key[v] < self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u
        # Виводимо збудоване MST
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

graph = Graph(graph, V)
print("Мінімальне:")
graph.primMST()
print("Максимальне:")
graph.primMST(phonk=1)