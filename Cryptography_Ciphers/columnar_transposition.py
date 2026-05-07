"""
Name: Prathamesh Fuke
Roll Number: TE258
Cipher: Columnar Transposition Cipher
"""

import math

def encrypt(message, key):
    cipher = [""] * key

    for col in range(key):
        pointer = col

        while pointer < len(message):
            cipher[col] += message[pointer]
            pointer += key

    return "".join(cipher)


if __name__ == "__main__":
    message = input("Enter Message: ")
    key = int(input("Enter Key: "))

    ciphertext = encrypt(message, key)

    print("Encrypted Text:", ciphertext)
