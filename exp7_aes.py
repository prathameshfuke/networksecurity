"""
Experiment 7
Title: Implementation of AES.

Theory:
- Advanced Encryption Standard (AES) is a Symmetric key cryptography.
- Block size: 128 bits.
- Key sizes: 128 / 192 / 256 bits.
- Same key is used for encryption and decryption.
- More secure than DES.
"""

# pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# AES key (16 bytes = 128-bit key)
key = b'ThisIsA16ByteKey'

def run_aes():
    # Create AES cipher object (ECB mode)
    cipher = AES.new(key, AES.MODE_ECB)

    # Input message
    message = input("Enter message: ").encode()

    # Encryption
    encrypted_message = cipher.encrypt(pad(message, 16))

    # Decryption
    decrypted_message = unpad(cipher.decrypt(encrypted_message), 16)

    print("\nOriginal Message:", message.decode())
    print("Encrypted Message:", encrypted_message)
    print("Decrypted Message:", decrypted_message.decode())

if __name__ == "__main__":
    try:
        run_aes()
    except ImportError:
        print("Error: pycryptodome not installed. Run 'pip install pycryptodome'")
