from helpers import co_prime2, inverse_mod, totient


# region Knapsack Public Key
# m must be > than sum of all numbers in private key.
#       m = p * q, p*q are prime
# n must not have common factors with m. (use co_prime2(m, n) to test)

# Determines a public key from a private key
#       given the stated modulus and n values
def knapsack_public_key(private_list, m, n):
    # Multiply all values by n mod m
    public_list = []
    for p in private_list:
        public_list.append((p * n) % m)
    return public_list


# Determines a private key from a public key
#       given the original modulus and n values
def knapsack_private_key(public_list, m, n):
    tot_m = totient(m)
    private_list = []
    for p in public_list:
        p_value = (p * (inverse_mod(n, m))) % m
        private_list.append(p_value)
    return private_list


# Enciphers a binary message with a public knapsack key
def knapsack_encipher(public_list, binary_str):
    p_index = 0
    sum_cipher = 0
    cipher = []
    for c in binary_str:
        if c == " ":    # Skip blanks
            continue
        sum_cipher += int(c) * public_list[p_index]  # Add to current sum
        p_index += 1

        if p_index == len(public_list):  # Repeat for another message
            p_index = 0
            cipher.append(sum_cipher)
            sum_cipher = 0
    return cipher


# Decipher a ciphered message with a private key
# Note: Only works for easy knapsacks
def knapsack_easy_decipher(private_list, m, n, cipher):
    binary_str = ""
    inv_mod = inverse_mod(n, m)
    for c in cipher:
        # Determine decryption value
        decrypt = (c * inv_mod) % m     # Decryption value for item
        msg = ""                        # Bin. word from decrypted item
        for i in range(len(private_list)-1, -1, -1):
            if decrypt - private_list[i] >= 0:
                msg += "1"              # Match
                decrypt -= private_list[i]
            else:
                msg += "0"              # No match
        binary_str += msg[::-1] + " "  # Reverse; word created in reverse order
    return binary_str
# endregion


if __name__ == '__main__':

    # Knapsack
    print("===Knapsack===")
    private_key = [2, 3, 6, 13, 27, 52]
    m = 21 * 5
    n = 31
    print("Are m & n a valid combo?: " +
          str(m > sum(private_key) and co_prime2(m, n)))
    public_key = knapsack_public_key(private_key, m, n)
    print(public_key)
    print(inverse_mod(n, m))
    private_key = knapsack_private_key(public_key, m, n)
    print(private_key)

    message = "011000 110101 101110"
    cipher = knapsack_encipher(public_key, message)
    print(cipher)
    message = knapsack_easy_decipher(private_key, m, n, cipher)
    print(message)


