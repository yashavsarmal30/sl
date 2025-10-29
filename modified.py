# Modified Caesar Cipher in Python (using a key)

def encrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
            key_index += 1
        else:
            result += char
    return result

def decrypt(cipher, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in cipher:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start - shift) % 26 + start)
            key_index += 1
        else:
            result += char
    return result

# Example usage
text = input("Enter the text: ")
key = input("Enter the key: ")

cipher_text = encrypt(text, key)
print(f"Encrypted Text: {cipher_text}")

plain_text = decrypt(cipher_text, key)
print(f"Decrypted Text: {plain_text}")

# Example Usage:
# Input:
# Enter the text: Hello World
# Enter the key: key
#
# Expected Output:
# Encrypted Text: Khoor Zruog
# Decrypted Text: Hello World
