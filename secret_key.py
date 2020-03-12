import binascii
import os
import secrets

print(len(binascii.hexlify(os.urandom(32))))
print(os.urandom(32))
print(len(secrets.token_bytes(31)))
