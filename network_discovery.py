"""
Network Discovery using UDP
Aggregates discovered IoT devices
"""

import socket
import networkx as nx
import time

UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", UDP_PORT))
sock.setblocking(False)

G = nx.Graph()
active_devices = {}

print("[INFO] Network discovery started")

while True:
    try:
        data, addr = sock.recvfrom(1024)
        msg = data.decode()

        if msg.startswith("DISCOVER"):
            device_id = msg.split(":")[1]
            active_devices[device_id] = time.time()
            G.add_node(device_id)

            # Random adjacency simulation
            for other in G.nodes:
                if other != device_id:
                    G.add_edge(device_id, other)

            print(f"[DISCOVERED] {device_id}")

    except BlockingIOError:
        pass

    # Remove inactive nodes
    current_time = time.time()
    for dev in list(active_devices):
        if current_time - active_devices[dev] > 10:
            G.remove_node(dev)
            del active_devices[dev]
            print(f"[REMOVED] {dev}")

    time.sleep(1)
