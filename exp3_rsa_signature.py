"""
Experiment 3
Title: Write a program to implement digital Signature.

Theory: Working flow using RSA algorithm
- Message is converted into a numeric value
- Private key signs the message
- Public key verifies the signature
- RSA works under modulo n
- Decrypted value equals message mod n
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
