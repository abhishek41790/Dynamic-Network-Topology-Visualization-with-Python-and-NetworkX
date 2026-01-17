"""
Real-Time Network Topology Visualization
"""

import networkx as nx
import matplotlib.pyplot as plt
import random
import time

G = nx.Graph()
plt.ion()

nodes = []

for i in range(15):
    plt.clf()

    # Simulate node join
    if random.random() > 0.4:
        node = f"device_{random.randint(100,999)}"
        G.add_node(node)
        nodes.append(node)

    # Simulate edges
    if len(nodes) > 1:
        n1, n2 = random.sample(nodes, 2)
        G.add_edge(n1, n2)

    # Simulate node leave
    if random.random() > 0.7 and nodes:
        remove_node = random.choice(nodes)
        G.remove_node(remove_node)
        nodes.remove(remove_node)

    pos = nx.spring_layout(G)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2000,
        node_color="lightgreen",
        edge_color="gray",
        font_size=10
    )

    plt.title("Dynamic IoT Network Topology")
    plt.pause(1)

plt.ioff()
plt.show()
