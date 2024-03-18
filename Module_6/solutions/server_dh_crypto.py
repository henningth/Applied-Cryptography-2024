"""
Python chat program: Server

Uses Diffie-Hellman key exchange (rudimentary)
"""

import socket
from random import randint
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes

HOST = '127.0.0.1' # Localhost
PORT = 9999 # Choose port above 1024

key = b'This is a secret' # The key is secret
nonce = b'This is a nonce.' # The nonce can be public

g = 5 # Generator
p = 23 # Group order
server_secret = randint(1,p-1)

key_exchange_done = False

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
            if not key_exchange_done:
                # Receive public value from client
                client_public_bytes = conn.recv(1024)
                client_public = int.from_bytes(client_public_bytes, 'little')
                print("Received public value from client:", client_public)

                # Send public value to client
                server_public = (g**server_secret) % p
                conn.send(server_public.to_bytes(32, 'little'))
                print("Sent server public to client:", server_public)

                # Compute common secret
                common_secret = (client_public**server_secret) % p
                print("Computed common secret:", common_secret)
                common_secret_bytes = common_secret.to_bytes(32, 'little')

                # Create key and nonce out of common_secret
                hkey = hashes.Hash(hashes.SHA256())
                hkey.update(common_secret_bytes)
                key_material = hkey.finalize() # Should use HKDF instead
                key = key_material[:16]
                nonce = key_material[16:32]

                print("Diffie-Hellman key exchange done.")
                print("Key:", key.hex())
                print("Nonce:", nonce.hex())
                key_exchange_done = True

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
