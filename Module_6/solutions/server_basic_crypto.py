"""
Python chat program: Server

Assumes secret key was already exchanged
"""

import socket
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

HOST = '127.0.0.1' # Localhost
PORT = 9999 # Choose port above 1024

key = b'This is a secret' # The key is secret
nonce = b'This is a nonce.' # The nonce can be public

def encrypt(plaintext, key, nonce):
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return ciphertext

def decrypt(plaintext, key, nonce):
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
    decryptor = cipher.decryptor()
    decryptedplaintext = decryptor.update(plaintext) + decryptor.finalize()
    return decryptedplaintext

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    conn, addr = sock.accept()
    with conn:
        print("Connection received from:", addr)
        while True:
            # Receive encrypted data from client
            re_data = conn.recv(1024)
            print("Received encrypted data:", re_data)

            # Decrypt the received data and print it
            r_data = decrypt(re_data, key, nonce)
            print("Received data:", r_data.decode())

            # User enters data, and the data is converted to binary format
            s_data = input("Enter data to send: ").encode('UTF-8')

            # Encrypt data using AES-CTR
            e_data = encrypt(s_data, key, nonce)
            print("Encrypted data to send:", e_data)
            conn.sendall(e_data)
