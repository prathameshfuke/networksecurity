"""
Name: Prathamesh Fuke
Roll Number: TE258
Cipher: Rail Fence Cipher
"""

def encrypt(text, key):
    rail = [['\n' for i in range(len(text))]
            for j in range(key)]

    direction_down = False
    row, col = 0, 0

    for char in text:
        if row == 0 or row == key - 1:
            direction_down = not direction_down

        rail[row][col] = char
        col += 1

        row += 1 if direction_down else -1

    result = ""
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result += rail[i][j]

    return result


if __name__ == "__main__":
    plaintext = input("Enter Plaintext: ")
    key = int(input("Enter Key: "))

    ciphertext = encrypt(plaintext, key)

    print("Encrypted Text:", ciphertext)
