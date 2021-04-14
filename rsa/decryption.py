"""
input: cipher - space separated list of numbers - no commas or quoted
output: original text (we hope)
"""

import sys
from rsa_calc import RSACalc

rsa = RSACalc()
private_key = rsa.private_key
public_key = rsa.public_key

# rsa.print_dictionary(rsa.DECRYPT_DICTIONARY)


# take user input converted from string to list of ints
# or die trying
def convert_raw_cipher(raw_list):
    cipher_list = []
    for each in raw_list:
        try:
            cipher_list.append(int(each))
        except ValueError:
            sys.exit("this isn't a cipher - should only consist of space separated integers")
    return cipher_list


# return a decrypted string from a list of ints, decrypts each char then
# gets string value from ascii
def decrpyt_cipher(clean_ciph_list):
    decrypted_string = ""
    decrypted_list = []
    exp = rsa.exponent
    for each in clean_ciph_list:
        decrypted_ascii = (each ** private_key) % public_key
        decrypted_char = rsa.DECRYPT_DICTIONARY[decrypted_ascii]
        decrypted_list.append(decrypted_char)
        print(f'encryt char: {each}, decrypted ascii number: {decrypted_ascii}, original char: {decrypted_char}')
    decrypted_string = ''.join(decrypted_list)
    return decrypted_string


cipher_string = input("give me your cipher: ")
if not cipher_string:
    sys.exit("you have to give me something to work with son")

raw_cipher_list = cipher_string.split()
clean_cipher_list = convert_raw_cipher(raw_cipher_list)
decrypted_str = decrpyt_cipher(clean_cipher_list)

print(f'is this your string?: {decrypted_str}')
