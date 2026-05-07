"""
Name: Prathamesh Fuke
Roll Number: TE258
Cipher: DES (Data Encryption Standard)
"""

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_demo():
    key = b'12345678' # 8-byte key for DES

    cipher = DES.new(key, DES.MODE_ECB)

    plaintext = input("Enter Plaintext: ").encode()

    # Padding to 8-byte block size
    encrypted = cipher.encrypt(pad(plaintext, 8))

    print("Encrypted:", encrypted)

    decrypted = unpad(cipher.decrypt(encrypted), 8)

    print("Decrypted:", decrypted.decode())

if __name__ == "__main__":
    des_demo()
