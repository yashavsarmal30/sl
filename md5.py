
import hashlib

# Take input from user
text = input("Enter text to hash: ")

# Encode the text and generate MD5 hash
hash_object = hashlib.md5(text.encode())

# Get the hexadecimal representation
md5_hash = hash_object.hexdigest()

print(f"MD5 Hash: {md5_hash}")
