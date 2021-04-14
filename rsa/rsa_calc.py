"""
Put all rsa calculations here, create public/private key, p and q primes,
ascii dictionary
public key is n with e as exponent

caveat: primes are configurable, make sure you use the same values for decryption
that you used for encryption
"""

import string
import pprint


class RSACalc:
    i = 2
    # up and low case letters, numbers, punctuation and whitespace - no line feeds
    ENCRYPT_DICTIONARY = {char: ord(char) for char in string.printable}
    DECRYPT_DICTIONARY = {v: k for k, v in ENCRYPT_DICTIONARY.items()}

    def __init__(self, p_prime=0, q_prime=0):
        if not bool(p_prime):  # make automated testing easier
            self.p_prime = 13
        if not bool(q_prime):
            self.q_prime = 17

        self.phi_n = (self.p_prime - 1) * (self.q_prime - 1)
        self.exponent = self.create_exponent()  # this is e: 1 < e < ϕ(𝑛)  ϕ(𝑛) cannot be divisible by e
        self.private_key = self.create_private_key()

        # this is n:  ϕ(𝑛) = (𝑝 − 1)(𝑞 − 1) and e as exponent
        self.public_key = self.p_prime * self.q_prime

        # this is d: (𝑖 × ϕ(𝑛) + 1) / 𝑒   i can be any integer
        private_key = self.create_exponent()
        self.print_values()

    # pick a (preferably low) number for e, can't be a factor of ϕ(𝑛)
    # this should always get the lowest number
    def create_exponent(self):
        exp = 1
        # print(f"phi_n = {self.phi_n}")
        while exp < self.phi_n and self.phi_n % exp == 0:
            exp += 1
        # print(f"exponent = {exp}")
        return exp

    # create private key - gotta be an int tho
    def create_private_key(self):
        self.private_key = int((self.i * self.phi_n + 1) / self.exponent)
        # print(f"private key = {self.private_key}")
        return self.private_key

    def print_values(self):
        print(
            f'phi_n: {self.phi_n}, exponent: {self.exponent}, private key: {self.private_key}, public key: {self.public_key}')

    @staticmethod
    def print_dictionary(self, rsa_dict):
        print(rsa_dict)
