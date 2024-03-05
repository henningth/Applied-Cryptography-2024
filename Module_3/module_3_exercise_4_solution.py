"""
Module 3.
Exercise 4: In this exercise, we are working with the stream cipher ChaCha20 in Python. 
See https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/#cryptography.hazmat.primitives.ciphers.algorithms.ChaCha20 for usage and an example.
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from os import urandom

"""
(a): Encrypt the plaintext “Hello world” (without quotes) using the stream cipher ChaCha20. Be sure to generate a key and nonce properly. Print the ciphertext in the console, what do you see?
"""

nonce = urandom(8) # Note: 8 bytes for the nonce, since it's concatenated with a counter
counter = bytearray(8)
nonceandcounter = counter + nonce
key = urandom(32)

plaintext = b'Hello world'

cipher = Cipher(algorithm=algorithms.ChaCha20(key, nonceandcounter), mode=None)
encryptor = cipher.encryptor()
ciphertext = encryptor.update(plaintext)

"""
(b): Decrypt the ciphertext obtained in part (a), and check that the original plaintext and 
decrypted ciphertext are equal (why do we want to check this?)
"""

decryptor = cipher.decryptor()
decryptedciphertext = decryptor.update(ciphertext)

print("Test with unchanged ciphertext")
if plaintext == decryptedciphertext:
    print("SUCCESS")
else:
    print("FAILURE")

"""
(c): Change one byte of the ciphertext and decrypt it using the same key and nonce as in part (a). 
What do you observe?
"""

changedciphertext = ciphertext[:-2] + b'\x4f'
decryptor = cipher.decryptor()
decryptedchangedciphertext = decryptor.update(changedciphertext)

print("Test with changed ciphertext")
if plaintext == decryptedchangedciphertext:
    print("SUCCESS")
else:
    print("FAILURE")

"""
(d): Change one byte of the key and decrypt the ciphertext obtained in part (b). What do you see?
"""

changedkey = key[:-1] + b'\x43'
cipher2 = Cipher(algorithm=algorithms.ChaCha20(changedkey, nonceandcounter), mode=None)
decryptor2 = cipher2.decryptor()

decryptedciphertext2 = decryptor2.update(ciphertext)

print("Test with unchanged ciphertext and changed key")
if plaintext == decryptedciphertext2:
    print("SUCCESS")
else:
    print("FAILURE")