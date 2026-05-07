"""
Name: Prathamesh Fuke
Roll Number: TE258
Cipher: Monoalphabetic Cipher
"""

import string

alphabet = string.ascii_uppercase
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

encrypt_dict = dict(zip(alphabet, key))
decrypt_dict = dict(zip(key, alphabet))


def encrypt(text):
    result = ""

    for char in text.upper():
        if char in encrypt_dict:
            result += encrypt_dict[char]
        else:
            result += char

    return result


def decrypt(text):
    result = ""

    for char in text.upper():
        if char in decrypt_dict:
            result += decrypt_dict[char]
        else:
            result += char

    return result


if __name__ == "__main__":
    plaintext = input("Enter Plaintext: ")

    ciphertext = encrypt(plaintext)
    print("Encrypted Text:", ciphertext)

    decrypted = decrypt(ciphertext)
    print("Decrypted Text:", decrypted)
