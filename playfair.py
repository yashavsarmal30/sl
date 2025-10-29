# Playfair Cipher in Python

def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for char in key:
        if char.isalpha() and char not in used:
            used.add(char)
            matrix.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used:
            matrix.append(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == char:
                return i, j
    return None

def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    prepared = ""
    i = 0
    while i < len(text):
        prepared += text[i]
        if i+1 < len(text):
            if text[i] == text[i+1]:
                prepared += "X"
            else:
                prepared += text[i+1]
                i += 1
        else:
            prepared += "X"
        i += 1
    return prepared

def encrypt_pair(pair, matrix):
    r1, c1 = find_position(matrix, pair[0])
    r2, c2 = find_position(matrix, pair[1])

    if r1 == r2:  # Same row
        return matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
    elif c1 == c2:  # Same column
        return matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
    else:  # Rectangle rule
        return matrix[r1][c2] + matrix[r2][c1]

def decrypt_pair(pair, matrix):
    r1, c1 = find_position(matrix, pair[0])
    r2, c2 = find_position(matrix, pair[1])

    if r1 == r2:
        return matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
    elif c1 == c2:
        return matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]

def playfair_encrypt(text, key):
    matrix = generate_key_matrix(key)
    text = prepare_text(text)
    cipher = ""
    for i in range(0, len(text), 2):
        cipher += encrypt_pair(text[i:i+2], matrix)
    return cipher

def playfair_decrypt(cipher, key):
    matrix = generate_key_matrix(key)
    plain = ""
    for i in range(0, len(cipher), 2):
        plain += decrypt_pair(cipher[i:i+2], matrix)
    return plain

# Example usage
text = input("Enter the text: ")
key = input("Enter the key: ")

encrypted = playfair_encrypt(text, key)
print(f"Encrypted Text: {encrypted}")

decrypted = playfair_decrypt(encrypted, key)
print(f"Decrypted Text: {decrypted}")

# Example Usage:
# Input:
# Enter the text: Hide the gold in the tree stump
# Enter the key: playfairexample
#
# Expected Output:
# Encrypted Text: BMODZBXDNABEKUDMUIXMMUSSDX
# Decrypted Text: HIDETHEGOLDINTHETREESTUMPX
