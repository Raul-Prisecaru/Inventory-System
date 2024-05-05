import secrets
import pysqlcipher3.dbapi2 as sqlite

# Generate a random encryption key
encryptionKey = secrets.token_hex(32)

print(encryptionKey)
