"""
Experiment 6
Title: Implementation of DES.

Theory:
- Data Encryption Standard (DES): The most popular symmetric key algorithm.
- DES is a symmetric key encryption algorithm.
- Key size: 8 bytes (64 bits).
- Same key is used for encryption and decryption.
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
