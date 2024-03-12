"""
Exercise 6: Implementing Encrypt-then-MAC
Exercise 7: Implementing Decrypt-then-MAC
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, hmac
from os import urandom

# Testing with plaintext
plaintext = b'Hello world'
enc_key = urandom(16)
mac_key = urandom(16)
nonce = urandom(16)

def encrypt_then_mac(enc_key, mac_key, nonce, plaintext):
    # Encrypt the plaintext
    cipher = Cipher(algorithms.AES(enc_key), modes.CTR(nonce))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext)
    ciphertext += encryptor.finalize()
    # Create tag
    mac = hmac.HMAC(mac_key, hashes.SHA256())
    mac.update(ciphertext)
    tag = mac.finalize()
    return ciphertext, tag

def decrypt_then_mac(ciphertext, enc_key, mac_key, nonce, tag):
    # Compute tag and compare
    mac = hmac.HMAC(mac_key, hashes.SHA256())
    mac.update(ciphertext)
    computed_tag = mac.finalize()
    if computed_tag == tag:
        # Decrypt ciphertext
        cipher = Cipher(algorithms.AES(enc_key), modes.CTR(nonce))
        decryptor = cipher.decryptor()
        decrypted_plaintext = decryptor.update(ciphertext)
        decrypted_plaintext += decryptor.finalize()
        return decrypted_plaintext
    else:
        # Return false
        return False

ciphertext, tag = encrypt_then_mac(enc_key, mac_key, nonce, plaintext)

print("Ciphertext:", ciphertext)
print("Tag:", tag)

plaintext = decrypt_then_mac(ciphertext, enc_key, mac_key, nonce, tag)

print("Plaintext:", plaintext)


