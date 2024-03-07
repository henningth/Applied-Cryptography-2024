"""
Live coding MAC
"""

from cryptography.hazmat.primitives import hashes, hmac
from os import urandom

def computeTag(message, key):
    mac = hmac.HMAC(key, hashes.SHA256())
    mac.update(message)
    tag = mac.finalize()
    return tag

def verifyTag(message, key, tag):
    # Compute MAC tag of message
    computedTag = computeTag(message, key)
    # Compare computed tag to the tag in the argument
    if computedTag == tag:
        return True
    else:
        return False

key = urandom(16)
message = b'This is a test.'
tag = computeTag(message, key)
print(tag.hex())

result = verifyTag(message, key, tag)
print(result)