"""
Live coding AES-CTR
Write a Python program which can encrypt and decrypt 
using AES in counter (CTR) mode
Need key and nonce
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from os import urandom

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

key = urandom(16)
nonce = urandom(16)

plaintext = 'Hello world'.encode() # Correct format, important
ciphertext = encrypt(plaintext, key, nonce)
print(ciphertext)
decryptedplaintext = decrypt(ciphertext, key, nonce)

if plaintext == decryptedplaintext:
    print("SUCCESS")
else:
    print("FAILURE")

