import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Створюємо графи
G1 = nx.Graph()
G1.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)])
layout = nx.spring_layout(G1)
nx.draw(G1, layout)
nx.draw_networkx_edge_labels(G1, pos=layout)
plt.show()

G2 = nx.Graph()
G2.add_edges_from([(10, 20), (10, 30), (20, 30), (30, 40), (40, 50)])
layout = nx.spring_layout(G2)
nx.draw(G2, layout)
nx.draw_networkx_edge_labels(G2, pos=layout)
plt.show()
# Перевірка на ізоморфізм
isomorphic = nx.is_isomorphic(G1, G2)
print("Isomorphic: ", isomorphic)

# Якщо графи ізоморфні, модифікуємо один з графів
if isomorphic:
    # Додаємо вершину, якої немає в іншому графі
    G1.add_node(6)
    G1.add_edge(6, 1)
    G1.add_edge(6, 3)
    G1.add_edge(6, 4)
    G1.add_edge(6, 5)
    # Перевірка на ізоморфізм після модифікації
    isomorphic = nx.is_isomorphic(G1, G2)
    print("Isomorphic after modification: ", isomorphic)

layout = nx.spring_layout(G1)
nx.draw(G1, layout)
nx.draw_networkx_edge_labels(G1, pos=layout)
plt.show()
