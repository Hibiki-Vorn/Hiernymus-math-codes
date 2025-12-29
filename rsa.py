from sage.all import * # type: ignore
import random
from lib import EuclideanAlgorithm

def generate_keys(p=None, q=None):
    if p is None:
        p = random_prime(2^1024, lbound=2^1023) # pyright: ignore[reportUndefinedVariable]
    if q is None:
        q = random_prime(2^1024, lbound=2^1023) # pyright: ignore[reportUndefinedVariable]
    
    def phi(p,q):
        return (p - 1)*(q - 1)

    n = p*q
    phi_n = phi(p,q)
    e=65537
    while gcd(e, phi_n) != 1: # pyright: ignore[reportUndefinedVariable]
        e = random.randrange(1,phi_n)
    d = EuclideanAlgorithm.extended_gcd(e, phi_n)[1]
    if d < 0:
        d = d + phi_n

    print("Public Key: (", n, ",", e, ")")
    print("Private Key: (", n, ",", d, ")")
    return ((n, e), (n, d))

def encrypt(message, public_key):
    n, e = public_key
    encrypted_message = mod(pow(message, e),n) # pyright: ignore[reportUndefinedVariable]
    print("Encrypted message:", encrypted_message)
    return encrypted_message

def decrypt(encrypted_message, private_key):
    n, d = private_key
    message = mod(pow(encrypted_message, d), n) # pyright: ignore[reportUndefinedVariable]
    print("Decrypted message:", message)
    return message

while True:
    print("1. Generate Keys")
    print("2. Encrypt")
    print("3. Decrypt")
    method = input("Select a method [0]")
    if method == "1":
        generate_keys(int(input("Enter a prime p (or leave blank for random): ") or 0), int(input("Enter a prime q (or leave blank for random): ") or 0))
    if method == "2":
        message = int(input("Enter a message to encrypt: "))
        key = (int(input("Enter the public key n: ")),int(input("Enter the public key e: ")))
        encrypt(message, key)
    if method == "3":
        encrypted_message = int(input("Enter an encrypted message to decrypt: "))
        key = (int(input("Enter the private key n: ")),int(input("Enter the private key d: ")))
        decrypt(encrypted_message, key)
    