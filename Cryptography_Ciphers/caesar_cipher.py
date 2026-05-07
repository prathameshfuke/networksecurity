"""
Name: Prathamesh Fuke
Roll Number: TE258
Cipher: Caesar Cipher
"""

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += encrypted_char
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


if __name__ == "__main__":
    plaintext = input("Enter Plaintext: ")
    shift = int(input("Enter Shift Value: "))

    ciphertext = encrypt(plaintext, shift)
    print("Encrypted Text:", ciphertext)

    decrypted = decrypt(ciphertext, shift)
    print("Decrypted Text:", decrypted)
