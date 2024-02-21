"""
Module 2, ex. 43
"""

from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers import algorithms
from cryptography.hazmat.primitives.ciphers import modes
from cryptography.hazmat.primitives import padding

import os

choice = input("Generate key (G) or enter key (any other key)")

if choice == "G":
    key = os.urandom(16) # Generate 16 bytes for the key
else:
    key = input("Enter key:")
    key = key.encode("UTF-8")
    padder = padding.PKCS7(128).padder()
    padded_key = padder.update(key)
    padded_key += padder.finalize()
    key = padded_key 
        
print("key", key)
message = b'Hello World, heyHello World, hey' # Message is 16 bytes
cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.ECB())

def encrypt(message):
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message)
    ciphertext += encryptor.finalize()
    return ciphertext

ciphertext = encrypt(message)
print(ciphertext)

def decrypt(ciphertext):
    decryptor = cipher.decryptor()
    decryptedmessage = decryptor.update(ciphertext)
    decryptedmessage += decryptor.finalize()
    return decryptedmessage

decryptedtext = decrypt(ciphertext)
print(decryptedtext)