"""
Simulated IoT Device
Sends UDP broadcast messages for discovery
"""

import socket
import time
import random

UDP_PORT = 5005
BROADCAST_IP = "255.255.255.255"

device_id = f"device_{random.randint(100,999)}"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

print(f"[INFO] {device_id} started broadcasting")

while True:
    message = f"DISCOVER:{device_id}"
    sock.sendto(message.encode(), (BROADCAST_IP, UDP_PORT))
    time.sleep(random.randint(2, 5))
