"""
RSA starter code

Uses the Cryptography module in Python to encrypt and decrypt data using RSA

Generates private and public keys and saves them in separate PEM files
"""

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# Generate private RSA key
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Generate public RSA key
public_key = private_key.public_key()

# Save private RSA key in file
with open("rsa_private_key.pem", "wb") as rsa_file:
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption())
    rsa_file.write(pem)

# Save public RSA key in file
with open("rsa_public_key.pem", "wb") as rsa_file:
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo)
    rsa_file.write(pem)

# Encryption
plaintext = b'Hello world'

ciphertext = public_key.encrypt(
    plaintext=plaintext,
    padding=padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

decrypted_ciphertext = private_key.decrypt(
    ciphertext=ciphertext,
    padding=padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)