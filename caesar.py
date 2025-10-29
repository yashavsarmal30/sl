
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Shift uppercase and lowercase letters separately
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            # Non-alphabetic characters remain the same
            result += char
    return result

def decrypt(cipher, shift):
    return encrypt(cipher, -shift)  # Reverse the shift


text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))

cipher_text = encrypt(text, shift)
print(f"Encrypted Text: {cipher_text}")

plain_text = decrypt(cipher_text, shift)
print(f"Decrypted Text: {plain_text}")

# Example Usage:
# Input:
# Enter the text: Hello World
# Enter the shift value: 3
#
# Expected Output:
# Encrypted Text: Khoor Zruog
# Decrypted Text: Hello World
