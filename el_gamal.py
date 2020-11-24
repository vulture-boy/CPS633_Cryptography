from helpers import co_prime2

# region El Gamal
# p - prime number, with p-1 having at least one large factor
#           Note: p - 1 is always even; 2 * (p-1)/2
# g - generator, 1 < g < p
# k_private - private key, 1 < k_private < p-1

def el_gamal_create_public_key(p, g, k_private):
    y = (g**k_private) % p
    return [p, g, y]


def el_gamal_encipher(msg, k, k_pub):
    p = k_pub[0]
    g = k_pub[1]
    y = k_pub[2]

    c1 = g**k % p           # Component 1
    c2 = msg*(y**k) % p       # Component 2
    return [c1, c2]         # Ciphertext


def el_gamal_decipher(ciphertext, p, k_priv):
    c1 = ciphertext[0]
    c2 = ciphertext[1]

    return c2 * (c1 ** ((p-1) - k_priv)) % p

def plaintext_numbers(string):
    text = ""
    for i in range(0, len(string), 2):
        num = int(string[i] + string[i+1])
        text += chr(65 + num)

    return text

# endregion

if __name__ == "__main__":
        # El Gamal
    print("===El Gamal===")
    p = 262643
    g = 9563  # 1 < g < p
    private_key = 3632  # 1 < k < p-1
    print("Private Key (key, p, g): " + str([private_key, p, g]))
    public_key = el_gamal_create_public_key(p, g, private_key)
    print("Public Key (p, g, y): " + str(public_key))
    msg = 152015  # PUP
    k = 5  # "Random" co-prime
    print("Co-prime Valid?: " + str(co_prime2(k, p-1)))

    print("Message: " + str(msg))
    ciphertext = el_gamal_encipher(msg, k, public_key)
    print("Enciphered: " + str(ciphertext))
    ciphertext = el_gamal_decipher(ciphertext, p, private_key)
    print("Deciphered: " + str(ciphertext))
    print("Text: " + plaintext_numbers(str(ciphertext)))
