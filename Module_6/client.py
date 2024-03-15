"""
Python chat program: Client
"""

import socket

HOST = '127.0.0.1' # Localhost
PORT = 9999 # Choose port above 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    while True:
        # Enters data and sends it to server
        s_data = input("Enter data to send:").encode('UTF-8')
        sock.sendall(s_data)

        # Receives data from server
        r_data = sock.recv(1024)
        print("Received data:", r_data)