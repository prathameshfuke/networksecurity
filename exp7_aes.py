"""
Experiment 7
Name: Prathamesh Fuke
Roll Number: TE258
Title: Implementation of AES (Advanced Encryption Standard).

Theory:
- **Introduction**: AES was established by NIST in 2001 to replace DES. It is the global standard for symmetric-key encryption.
- **Architecture**: Unlike DES's Feistel structure, AES uses a **Substitution-Permutation Network (SPN)**, where the entire data block is processed in each round.
- **Block and Key Sizes**:
    - **Block Size**: Fixed at 128 bits (16 bytes).
    - **Key Sizes**: 128, 192, or 256 bits.
- **Round Operations**: Each round (except the final one) consists of four layers:
    1. **SubBytes**: Non-linear byte substitution using an S-box.
    2. **ShiftRows**: Cyclic shifting of rows in the state matrix.
    3. **MixColumns**: Mathematical mixing of column data (skipped in the last round).
    4. **AddRoundKey**: XORing the state with a round key.
- **Rounds**: The number of rounds depends on key size: 10 rounds (128-bit), 12 rounds (192-bit), or 14 rounds (256-bit).
- **Efficiency**: AES is highly efficient in both hardware and software, making it suitable for everything from smart cards to high-speed network traffic.
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
