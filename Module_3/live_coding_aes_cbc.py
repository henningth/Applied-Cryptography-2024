"""
Live Coding AES-CBC
Write a Python program which can encrypt and decrypt using AES in CBC mode
Plaintext length: Multiple of 16 bytes
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from os import urandom

def encrypt(plaintext, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return ciphertext

def decrypt(ciphertext, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    decryptedplaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return decryptedplaintext

key = urandom(16) # 16 bytes for key
iv = urandom(16) # 16 bytes for iv
plaintext = b'Hello World.....' # 16 characters

ciphertext = encrypt(plaintext, key, iv)
decryptedplaintext = decrypt(ciphertext, key, iv)

if plaintext == decryptedplaintext:
    print("SUCCESS")
else:
    print("FAILURE")