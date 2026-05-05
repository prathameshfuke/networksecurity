"""
Experiment 2
Title: Write a program to perform encryption and decryption using the following algorithms: Ceaser Cipher, Substitution Cipher.

Theory:
1. Caesar Cipher (Encryption & Decryption)
   - Logic: Each letter is shifted by a fixed number (key)
   - Works only on alphabetic characters
   - Preserves case (uppercase/lowercase)

2. Substitution Cipher (Encryption & Decryption)
   - Logic: Each letter is replaced by another letter based on a substitution key
   - Key must be a permutation of the alphabet (26 unique letters)
   - Example Key:
     Plain Alphabet : abcdefghijklmnopqrstuvwxyz
     Cipher Alphabet: qwertyuiopasdfghjklzxcvbnm
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
