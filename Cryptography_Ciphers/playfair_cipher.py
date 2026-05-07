"""
Name: Prathamesh Fuke
Roll Number: TE258
Cipher: Playfair Cipher
"""

def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for char in key:
        if char not in used and char.isalpha():
            used.add(char)
            matrix.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used:
            used.add(char)
            matrix.append(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]


def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j


def prepare_text(text):
    text = text.upper().replace("J", "I")
    prepared = ""

    i = 0
    while i < len(text):
        a = text[i]

        if not a.isalpha():
            i += 1
            continue

        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                prepared += a + "X"
                i += 1
            else:
                prepared += a + b
                i += 2
        else:
            prepared += a + "X"
            i += 1

    return prepared


def encrypt(text, matrix):
    text = prepare_text(text)
    cipher = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]

        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            cipher += matrix[row1][(col1 + 1) % 5]
            cipher += matrix[row2][(col2 + 1) % 5]

        elif col1 == col2:
            cipher += matrix[(row1 + 1) % 5][col1]
            cipher += matrix[(row2 + 1) % 5][col2]

        else:
            cipher += matrix[row1][col2]
            cipher += matrix[row2][col1]

    return cipher


if __name__ == "__main__":
    key = input("Enter Key: ")
    plaintext = input("Enter Plaintext: ")

    matrix = generate_key_matrix(key)

    print("Key Matrix:")
    for row in matrix:
        print(row)

    ciphertext = encrypt(plaintext, matrix)

    print("Encrypted Text:", ciphertext)
