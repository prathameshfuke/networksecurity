"""
Name: Prathamesh Fuke
Roll Number: TE258
Cipher: RSA Algorithm
"""

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    return None


if __name__ == "__main__":
    p = 3
    q = 11

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 7

    d = mod_inverse(e, phi)

    print("Public Key:", (e, n))
    print("Private Key:", (d, n))

    message = int(input("Enter Message (number): "))

    cipher = (message ** e) % n
    print("Encrypted Message:", cipher)

    plain = (cipher ** d) % n
    print("Decrypted Message:", plain)
