import secrets

# Generate a random encryption key
encryptionKey = secrets.token_hex(32)

print(encryptionKey)
