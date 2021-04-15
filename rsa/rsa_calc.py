"""
Put all rsa calculations here, create public/private key, p and q primes,
ascii dictionary
public key is n with e as exponent

caveat: primes are configurable, make sure you use the same values for decryption
that you used for encryption
"""

import string


class RSACalc:
    # completely random value used to calculate private key
    i = 2
    # up and low case letters, numbers, punctuation and whitespace - no line feeds - create 2 to go both ways
    ENCRYPT_DICTIONARY = {char: ord(char) for char in string.printable}
    DECRYPT_DICTIONARY = {v: k for k, v in ENCRYPT_DICTIONARY.items()}

    def __init__(self, pprime=0, qprime=0):
        self.p_prime = pprime
        self.q_prime = qprime
        if not bool(pprime):  # make automated testing easier
            self.p_prime = 13
        if not bool(qprime):
            self.q_prime = 17

        # this is ϕ(𝑛)
        self.phi_n = (self.p_prime - 1) * (self.q_prime - 1)
        self.exponent = self.create_exponent()  # this is e: 1 < e < ϕ(𝑛)  ϕ(𝑛) cannot be divisible by e

        # this is d: (𝑖 × ϕ(𝑛) + 1) / 𝑒   i can be any integer
        self.private_key = self.create_private_key()

        # this is n
        self.public_key = self.p_prime * self.q_prime

        self.print_values(self)

    # returns the lowest possible value for e, that isn't a factor of ϕ(𝑛)
    # this should always get the lowest number
    def create_exponent(self):
        exp = 1
        # print(f"phi_n = {self.phi_n}")
        while exp < self.phi_n and self.phi_n % exp == 0:
            exp += 1
        # print(f"exponent = {exp}")
        return exp

    # create private key - gotta be an int tho d: (𝑖 × ϕ(𝑛) + 1) / 𝑒
    def create_private_key(self):
        self.private_key = int((self.i * self.phi_n + 1) / self.exponent)
        return self.private_key

    @staticmethod
    def print_values(self):
        print(f'phi_n: {self.phi_n}, exponent: {self.exponent}, private key: {self.private_key}, public key: {self.public_key}')

    @staticmethod
    def print_dictionary(rsa_dict):
        print(rsa_dict)
