"""
Experiment 1
Name: Prathamesh Fuke
Roll Number: TE258
Title: Write a program to perform encryption and decryption 

Theory:
- This experiment implements a **Numeric Substitution Cipher** where each letter is mapped to its numerical position in the English alphabet (A=1, B=2, ..., Z=26).
- **Mapping Logic**:
    - **Uppercase letters**: Represented by positive integers from 1 to 26.
    - **Lowercase letters**: Represented by negative integers from -1 to -26 to maintain case information in a numeric format.
    - **Spaces**: Preserved as double spaces to clearly demarcate word boundaries.
- **Mathematical Basis**: 
    - For a character 'C', its position 'P' is calculated using ASCII values: `P = ord(C) - ord('A') + 1`.
- **Security**: This is a simple encoding scheme rather than a cryptographic cipher, as it lacks a secret key and follows a predictable 1:1 mapping.
"""

def encrypt(text):
    result = ""
    for char in text:
        if char.isupper():
            result += str(ord(char) - ord('A') + 1) + " "
        elif char.islower():
            result += str(-(ord(char) - ord('a') + 1)) + " "
        elif char == " ":
            result += "  "   # double space for word gap
    return result.strip()

def decrypt(cipher_text):
    result = ""
    words = cipher_text.split("  ")  # split words

    for word in words:
        tokens = word.split()
        for token in tokens:
            num = int(token)
            if num > 0:
                result += chr(num + ord('A') - 1)
            else:
                result += chr(-num + ord('a') - 1)
        result += " "
    return result.strip()


# Main Program
if __name__ == "__main__":
    message = input("Enter message: ")

    encrypted = encrypt(message)
    decrypted = decrypt(encrypted)

    print("\nEncrypted Message:", encrypted)
    print("Decrypted Message:", decrypted)
