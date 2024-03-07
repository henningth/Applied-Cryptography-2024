"""
Live coding MD5 and SHA1
"""

from cryptography.hazmat.primitives import hashes

text = b'Yellow submarine'

# MD5
md5hash = hashes.Hash(hashes.MD5())
md5hash.update(text)
md5digest = md5hash.finalize()
print(md5digest.hex())

# SHA1
sha1hash = hashes.Hash(hashes.SHA1())
sha1hash.update(text)
sha1digest = sha1hash.finalize()
print(sha1digest.hex())