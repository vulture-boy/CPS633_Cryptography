from math import gcd

# region Modular Arithmetic
def ab_mod_n(a, b, n, op):
    if op == '+':  # Addition
        # [(a mod n) + (b mod n)] mod n == (a+b) mod n
        return (a + b) % n

    elif op == '-':  # Subtraction
        # [(a mod n) - (b mod n)] mod n == (a-b) mod n
        return (a - b) % n

    elif op == '*':  # Multiplication
        # [(a mod n) * (b mod n)] mod n == (a*b) mod n
        return (a * b) % n

    elif op == '^':  # Power
        # (a mod n)**b mod n == a**b mod n
        return (a ** b) % n
# endregion

# region Discrete Logarithm Problem
# Relatively Prime
def co_prime2(a, b):
    # Greatest common denominator is 1
    return gcd(a, b) == 1


# Naive solution for Inverse Modulo
def inverse_mod(a, n):
    a = a % n
    for x in range(1, n):
        if (a * x) % n == 1:
            return x
    return 1


# Totient function
def totient(n):
    # Number of positive integers less than n
    #   and relatively prime to n
    return sum(1 for k in range(1, n + 1) if co_prime2(n, k))


# Quick Totient solution (Prime N)
def totient_prime_n(n):
    # If n is prime,  totient(n) = n-1
    return n - 1


# Quick Totient solution (Prime P & Q, PQ = N)
def totient_prime_pq(p, q):
    # If n = p*q, then totient(n) = (p-1)(q-1)
    return (p-1) * (q-1)
# endregion

if __name__ == "__main__":
    # region Driver Tests

    # Modular Arithmetic
    print("===Modular Arithmetic===")
    print(ab_mod_n(9563, 3230, 262643, "^"))

    # Discrete Log Problem
    print("===Totient===")
    print(totient(123))

    # endregion