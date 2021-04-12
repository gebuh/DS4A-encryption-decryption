"""
Put all rsa calculations here, create public/private key, p and q primes,
ascii dictionary
public key is n with e as exponent

"""

import string


class RSACalc:

    def __init__(self, name):
        self.name = name
        self.exponent = self.create_exponent() # this is e: 1 < e < ϕ(𝑛)  ϕ(𝑛) cannot be divisible by e

    def __repr__(self):
        return self.name

    P_PRIME = 13
    Q_PRIME = 17

    # this is n:  ϕ(𝑛) = (𝑝 − 1)(𝑞 − 1) and e as exponent
    public_key = P_PRIME * Q_PRIME

    phi_n = (P_PRIME - 1) * (Q_PRIME - 1)

    # this is d: (𝑖 × ϕ(𝑛) + 1) / 𝑒   i can be any integer
    private_key = 0

    # encrypted text array of 𝑡𝑟𝑎𝑛𝑠𝑙𝑎𝑡𝑖𝑜𝑛 𝑒 𝑚𝑜𝑑 n
    cipher = []

    # up and low case letters, numbers, punctuation and whitespace - no line feeds
    dictionary = {char: ord(char) for char in string.printable}

    # pick a (preferably low) number for e, can't be a factor of ϕ(𝑛)
    def create_exponent(self):
        while self.exponent < self.phi_n and self.phi_n % self.exponent != 0:
            self.exponent += 1
        return self.exponent

    def create_cipher(raw_text):




