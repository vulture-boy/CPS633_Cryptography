from helpers import co_prime2

if __name__ == "__main__":
    # Diffie Hellman
    print("===Diffie Hellman===")
    p = 53      # Prime number
    g = 17      # g != 0, 1, p-1; g is primitive to p (co-prime)
    print("Valid p, g?: " + str(co_prime2(p, g)))
    k_a = 5     # Alice private key
    k_b = 7     # Bob private key
    k_a_public = g**k_a % p     # Alice public key
    k_b_public = g**k_b % p     # Bob public key
    symmetric_key = k_b_public**k_a % p     # Alice's computation of symmetric key
    print("Valid symmetric key?: " + str(symmetric_key == k_a_public**k_b % p))     # Check vs Bob's sym.
    # endregion