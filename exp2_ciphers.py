"""
Experiment 2
Title: Write a program to perform encryption and decryption using the following algorithms: Ceaser Cipher, Substitution Cipher.

Theory:
1. Caesar Cipher (Shift Cipher)
   - **Logic**: A monoalphabetic substitution cipher where each letter in the plaintext is shifted by a fixed number of positions (the key) down the alphabet.
   - **Mathematical Formula**:
     - Encryption: `C = E(P, K) = (P + K) mod 26`
     - Decryption: `P = D(C, K) = (C - K) mod 26`
     - where `P` is the plaintext character, `C` is the ciphertext character, and `K` is the key.
   - **Security**: Highly vulnerable to brute-force attacks (only 25 possible keys) and frequency analysis.

2. Substitution Cipher (Monoalphabetic Cipher)
   - **Logic**: Each letter of the plaintext is replaced by another letter based on a fixed, secret mapping (the key).
   - **Key Requirement**: The key must be a permutation of all 26 letters of the alphabet, ensuring a one-to-one mapping.
   - **Complexity**: Provides `26!` (approx. 4 x 10^26) possible keys, making brute-force impractical.
   - **Security**: Still vulnerable to frequency analysis, as the relative frequency of letters in the ciphertext remains the same as in the plaintext.
"""

# 1. Caesar Cipher
def caesar_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char
    return result


def caesar_decrypt(cipher_text, key):
    return caesar_encrypt(cipher_text, -key)


# 2. Substitution Cipher
alphabet = "abcdefghijklmnopqrstuvwxyz"
sub_key = "qwertyuiopasdfghjklzxcvbnm"

def substitution_encrypt(text, key):
    key = key.lower()
    result = ""

    for char in text:
        if char.isalpha():
            index = alphabet.index(char.lower())
            encrypted_char = key[index]
            result += encrypted_char.upper() if char.isupper() else encrypted_char
        else:
            result += char
    return result


def substitution_decrypt(cipher_text, key):
    key = key.lower()
    result = ""

    for char in cipher_text:
        if char.isalpha():
            index = key.index(char.lower())
            decrypted_char = alphabet[index]
            result += decrypted_char.upper() if char.isupper() else decrypted_char
        else:
            result += char
    return result


# Example usage
if __name__ == "__main__":
    print("--- Caesar Cipher ---")
    message = "Hello World"
    key = 3

    encrypted = caesar_encrypt(message, key)
    decrypted = caesar_decrypt(encrypted, key)

    print("Original Message :", message)
    print("Encrypted Message:", encrypted)
    print("Decrypted Message:", decrypted)

    print("\n--- Substitution Cipher ---")
    sub_encrypted = substitution_encrypt(message, sub_key)
    sub_decrypted = substitution_decrypt(sub_encrypted, sub_key)

    print("Original Message :", message)
    print("Encrypted Message:", sub_encrypted)
    print("Decrypted Message:", sub_decrypted)
