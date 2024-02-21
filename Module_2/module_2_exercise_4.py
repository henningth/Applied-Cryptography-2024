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

def add_padding(message):
    padder = padding.PKCS7(128).padder()
    padded_message = padder.update(message)
    padded_message += padder.finalize()
    return padded_message

def remove_padding(padded_message):
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_message = unpadder.update(padded_message)
    return unpadded_message

def encrypt(message):
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message)
    ciphertext += encryptor.finalize()
    return ciphertext

def decrypt(ciphertext):
    decryptor = cipher.decryptor()
    decryptedmessage = decryptor.update(ciphertext)
    decryptedmessage += decryptor.finalize()
    return decryptedmessage
        
print("key", key)
message = b'Hello World, hey' # Message is 16 bytes
cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.ECB())

padded_message = add_padding(message) # Add padding to message

padded_ciphertext = encrypt(padded_message)

padded_decrypted_ciphertext = decrypt(padded_ciphertext)

decrypted_ciphertext = remove_padding(padded_decrypted_ciphertext)

ciphertext = encrypt(message)
print(ciphertext)



decryptedtext = decrypt(ciphertext)
print(decryptedtext)