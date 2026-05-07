"""
Name: Prathamesh Fuke
Roll Number: TE258
Cipher: Vigenère Cipher
"""

def generate_key(text, key):
    key = list(key)

    if len(text) == len(key):
        return "".join(key)

    for i in range(len(text) - len(key)):
        key.append(key[i % len(key)])

    return "".join(key)


def encrypt(text, key):
    cipher = ""

    for i in range(len(text)):
        if text[i].isalpha():
            x = (ord(text[i].upper()) + ord(key[i].upper()) - 2 * 65) % 26
            cipher += chr(x + 65)
        else:
            cipher += text[i]

    return cipher


def decrypt(cipher, key):
    plain = ""

    for i in range(len(cipher)):
        if cipher[i].isalpha():
            x = (ord(cipher[i].upper()) - ord(key[i].upper()) + 26) % 26
            plain += chr(x + 65)
        else:
            plain += cipher[i]

    return plain


if __name__ == "__main__":
    plaintext = input("Enter Plaintext: ")
    key = input("Enter Key: ")

    generated_key = generate_key(plaintext, key)

    ciphertext = encrypt(plaintext, generated_key)
    print("Encrypted Text:", ciphertext)

    decrypted = decrypt(ciphertext, generated_key)
    print("Decrypted Text:", decrypted)
