"""
Live coding AES ECB.
"""

from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers import algorithms
from cryptography.hazmat.primitives.ciphers import modes

import os

key = os.urandom(16) # Generate 16 bytes for the key
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