"""
Experiment 5
Name: Prathamesh Fuke
Roll Number: TE258
Title: Implementation of Symmetric and Asymmetric cryptography.

Theory:
1. Symmetric Cryptography (Secret Key Cryptography)
   - **Logic**: Uses a single shared secret key for both encryption and decryption.
   - **Characteristics**: Fast, efficient for large amounts of data, and uses fewer computational resources.
   - **Key Distribution Problem**: Securely sharing the secret key between sender and receiver is the primary challenge. If the key is compromised, all communication is exposed.
   - **Algorithms**: Caesar Cipher, DES, AES, Blowfish.

2. Asymmetric Cryptography (Public Key Cryptography)
   - **Logic**: Uses a pair of mathematically related keys: a **Public Key** (shared with everyone) and a **Private Key** (kept secret by the owner).
   - **Working**: 
     - **Encryption**: Public key encrypts, Private key decrypts.
     - **Digital Signatures**: Private key signs, Public key verifies.
   - **Characteristics**: Solves the key distribution problem but is significantly slower than symmetric cryptography due to complex mathematical operations.
   - **Algorithms**: RSA, ECC, Diffie-Hellman.
   - **Hybrid Approach**: In practice (like HTTPS/TLS), asymmetric crypto is used to securely exchange a symmetric key, which is then used for the actual data transfer.
"""

# Symmetric Encryption (Caesar Cipher)
def symmetric_encrypt(message, key):
    result = ""
    for ch in message:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + key) % 26 + base)
        else:
            result += ch
    return result

def symmetric_decrypt(cipher, key):
    result = ""
    for ch in cipher:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base - key) % 26 + base)
        else:
            result += ch
    return result


# Asymmetric Encryption (Simple RSA)
def generate_keys():
    p = 11
    q = 13
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 7
    d = 103   # (7 × 103) mod 120 = 1

    return (e, n), (d, n)

def asymmetric_encrypt(message, public_key):
    e, n = public_key
    return [pow(ord(ch), e, n) for ch in message]

def asymmetric_decrypt(cipher, private_key):
    d, n = private_key
    return "".join(chr(pow(c, d, n)) for c in cipher)


# Main Program
if __name__ == "__main__":
    message = input("Enter message: ")

    # Symmetric
    key = 3
    sym_encrypted = symmetric_encrypt(message, key)
    sym_decrypted = symmetric_decrypt(sym_encrypted, key)

    # Asymmetric
    public_key, private_key = generate_keys()
    asym_encrypted = asymmetric_encrypt(message, public_key)
    asym_decrypted = asymmetric_decrypt(asym_encrypted, private_key)

    print("\n--- Symmetric Cryptography ---")
    print("Encrypted:", sym_encrypted)
    print("Decrypted:", sym_decrypted)

    print("\n--- Asymmetric Cryptography ---")
    print("Encrypted:", asym_encrypted)
    print("Decrypted:", asym_decrypted)
