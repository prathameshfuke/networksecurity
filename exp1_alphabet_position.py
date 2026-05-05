"""
Experiment 1
Title: Write a program to perform encryption and decryption 

Theory:
- Encrypts letters -> their alphabet position
- Uppercase letters -> positive numbers
- Lowercase letters -> negative numbers
- Space -> space (unchanged)
- Decrypts numbers -> back to letters
- Works for full words/sentences
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
