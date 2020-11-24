from math import gcd
from helpers import inverse_mod

def rsa_encrypt(m, e, n):
    return (m**e) % n

def rsa_decrypt(c, d, n):
    return (c**d) % n

if __name__ == "__main__":

    # RSA (exponentiation cipher)
    print("===RSA===")
    p = 181     # Prime
    q = 1451    # Prime
    n = p * q
    e = 154993                      # Encryption Key (public)
    tot_n = (p-1) * (q-1)           # Totient
    d = inverse_mod(e, tot_n)       # Decryption Key (private)
    print("Private key check: " + str(gcd(e, tot_n) == 1 and e < n))
    m = 152015                      # Message: PUP
    c = rsa_encrypt(m, e, n)        # Prepare Cipher
    print("Cipher is " + str(c))
    m = rsa_decrypt(c, d, n)
    print("Decipher is " + str(m))
