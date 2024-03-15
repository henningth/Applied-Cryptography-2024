"""
Python chat program: Server
"""

import socket

HOST = '127.0.0.1' # Localhost
PORT = 9999 # Choose port above 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    conn, addr = sock.accept()
    with conn:
        print("Connection received from:", addr)
        while True:
            # Receives data from server
            r_data = conn.recv(1024)
            print("Received data:", r_data)

            # Enters data and sends it to client
            s_data = input("Enter data to send: ").encode('UTF-8')
            conn.sendall(s_data)
