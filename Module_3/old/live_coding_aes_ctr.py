"""
Live coding AES-CTR
Write a Python program which can encrypt and decrypt using AES in counter (CTR) mode
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from os import urandom

def encrypt(plaintext, key, nonce):
    cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.CTR(nonce))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return ciphertext

def decrypt(ciphertext, key, nonce):
    cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.CTR(nonce))
    decryptor = cipher.decryptor()
    decryptedciphertext = decryptor.update(ciphertext) + decryptor.finalize()
    return decryptedciphertext

key = urandom(16)
nonce = urandom(16)

plaintext = b'Hello world.....'
ciphertext = encrypt(plaintext, key, nonce)
ciphertextchanged = ciphertext[:len(ciphertext)-1] + b'A'
#noncechanged = nonce[:len(nonce)-1] + chr(nonce[-1]).encode()
noncechanged = nonce[:len(nonce)-1] + nonce[-1].to_bytes(1, 'little')
decryptedplaintext = decrypt(ciphertext, key, noncechanged)

if plaintext == decryptedplaintext:
    print("SUCCESS")
else:
    print("FAILURE")
