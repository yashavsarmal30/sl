# RSA Encryption and Decryption for Text in Python

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None

# === Key Generation ===
print("=== RSA Key Generation ===")
p = int(input("Enter first prime number (p): "))
q = int(input("Enter second prime number (q): "))

n = p * q
phi = (p - 1) * (q - 1)

# Choose e
e = 2
while e < phi:
    if gcd(e, phi) == 1:
        break
    e += 1

# Find d
d = mod_inverse(e, phi)

print(f"\nPublic Key: (e={e}, n={n})")
print(f"Private Key: (d={d}, n={n})")

# === Encryption ===
text = input("\nEnter text to encrypt: ")
cipher = []

for char in text:
    encrypted_char = pow(ord(char), e, n)  # Encrypt ASCII value
    cipher.append(encrypted_char)

print(f"Encrypted Message: {cipher}")

# === Decryption ===
decrypted = ''
for c in cipher:
    decrypted_char = chr(pow(c, d, n))  # Decrypt to ASCII, then to char
    decrypted += decrypted_char

print(f"Decrypted Message: {decrypted}")

# Example Usage:
# Input:
# Enter first prime number (p): 61
# Enter second prime number (q): 53
# Enter text to encrypt: HELLO
#
# Expected Output (values for e, d, n will be calculated):
# Public Key: (e=17, n=3233)
# Private Key: (d=2753, n=3233)
# Encrypted Message: [2094, 1018, 1018, 1821, 1521] (These values may vary based on e and d calculation)
# Decrypted Message: HELLO
