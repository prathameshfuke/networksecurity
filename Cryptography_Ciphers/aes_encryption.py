"""
Name: Prathamesh Fuke
Roll Number: TE258
Cipher: AES (Advanced Encryption Standard)
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def aes_demo():
    key = b'1234567890123456' # 16-byte key for AES-128

    cipher = AES.new(key, AES.MODE_ECB)

    plaintext = input("Enter Plaintext: ").encode()

    # Padding to 16-byte block size
    encrypted = cipher.encrypt(pad(plaintext, 16))

    print("Encrypted:", encrypted)

    decrypted = unpad(cipher.decrypt(encrypted), 16)

    print("Decrypted:", decrypted.decode())

if __name__ == "__main__":
    aes_demo()
