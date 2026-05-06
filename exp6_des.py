"""
Experiment 6
Name: Prathamesh Fuke
Roll Number: TE258
Title: Implementation of DES (Data Encryption Standard).

Theory:
- **Introduction**: Developed in the 1970s by IBM and adopted as a federal standard. It is a symmetric-key block cipher.
- **Architecture**: DES is based on the **Feistel Network** structure, which divides the data block into two halves and applies a series of substitutions and permutations.
- **Key and Block Size**:
    - **Block Size**: 64 bits (8 bytes).
    - **Key Size**: 64 bits total, but 8 bits are used for parity, resulting in an **effective key length of 56 bits**.
- **Processing**: 
    - The algorithm involves **16 rounds** of identical operations.
    - Each round uses a unique 48-bit subkey derived from the main 56-bit key.
- **Security Status**: Due to its small key size, DES is considered insecure against modern brute-force attacks and has been replaced by more robust standards like AES.
"""

# pip install pycryptodome
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# DES key must be exactly 8 bytes
key = b'abcdefgh'

def run_des():
    # Create DES object
    des = DES.new(key, DES.MODE_ECB)

    # Input message
    message = input("Enter message: ").encode()

    # Encryption
    encrypted_message = des.encrypt(pad(message, 8))

    # Decryption
    decrypted_message = unpad(des.decrypt(encrypted_message), 8)

    print("\nOriginal Message:", message.decode())
    print("Encrypted Message:", encrypted_message)
    print("Decrypted Message:", decrypted_message.decode())

if __name__ == "__main__":
    try:
        run_des()
    except ImportError:
        print("Error: pycryptodome not installed. Run 'pip install pycryptodome'")
