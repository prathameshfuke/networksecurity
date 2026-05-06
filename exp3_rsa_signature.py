"""
Experiment 3
Name: Prathamesh Fuke
Roll Number: TE258
Title: Write a program to implement digital Signature.

Theory: Digital Signature using RSA Algorithm
- **Definition**: A digital signature is a mathematical technique used to validate the authenticity and integrity of a digital document, message, or software.
- **Core Security Goals**:
    - **Authentication**: Confirms the sender's identity.
    - **Integrity**: Ensures the message hasn't been tampered with during transit.
    - **Non-repudiation**: The sender cannot deny having sent the message.
- **Working Principle**:
    - Unlike encryption (where the Public key encrypts and Private key decrypts), a **Digital Signature** uses the **Private key to sign** and the **Public key to verify**.
- **Mathematical Foundations**:
    - RSA security relies on the difficulty of factoring large prime numbers.
    - **Key Generation**: Two primes `p, q` are used to find `n = p * q` and `phi = (p-1)(q-1)`. Public key `e` and Private key `d` are chosen such that `(e * d) mod phi = 1`.
    - **Signing**: `S = M^d mod n` (using sender's private key).
    - **Verification**: `M' = S^e mod n` (using sender's public key). If `M' == M`, the signature is valid.
"""

# Convert message to number
def message_to_number(message):
    return sum(ord(char) for char in message)

# Generate RSA keys (small values – for learning)
def generate_keys():
    p = 11
    q = 13
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 7
    d = 103   # (7 × 103) mod 120 = 1

    return (e, n), (d, n)

# Signature generation
def sign_message(message, private_key):
    d, n = private_key
    m = message_to_number(message)
    signature = pow(m, d, n)
    return signature, m

# Signature verification (also returns decrypted value)
def verify_signature(signature, original_message, public_key):
    e, n = public_key
    decrypted = pow(signature, e, n)
    original_mod = message_to_number(original_message) % n
    valid = (decrypted == original_mod)
    return decrypted, valid


# Main Program
if __name__ == "__main__":
    message = input("Enter message: ")

    public_key, private_key = generate_keys()

    signature, msg_value = sign_message(message, private_key)
    decrypted_value, valid = verify_signature(signature, message, public_key)

    print("\nOriginal Message:", message)
    print("Message Value:", msg_value)
    print("Message Value (mod n):", msg_value % public_key[1])
    print("Digital Signature:", signature)
    print("Decrypted Message Value:", decrypted_value)
    print("Signature Valid:", valid)
