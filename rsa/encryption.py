"""
simple encryption script
input: string from user, limited to upper/lower case letters, numbers, punctuation and whitespace
output: encrypted text as cipher

"""
import sys
import argparse
from rsa_calc import RSACalc

parser = argparse.ArgumentParser()
parser.add_argument("pprime", type=int, nargs="?", default=0)
parser.add_argument("qprime", type=int, nargs="?", default=0)
args = parser.parse_args()

raw_text = input("give me some text: ")
if not raw_text.isprintable() or not raw_text:
    sys.exit("you have to input numbers, letters or punctuation")

# we're encrypting, so get the private key
rsa = RSACalc(args.pprime, args.qprime)
text_to_list = list(raw_text)
print(f'List of Characters ={text_to_list}')

# encrypted text array of 𝑡𝑟𝑎𝑛𝑠𝑙𝑎𝑡𝑖𝑜𝑛 𝑒 𝑚𝑜𝑑 n

public_key = rsa.public_key


def encrypt_input(converted_text):
    exp = rsa.exponent
    ciph = []
    for char in converted_text:
        ascii_value = rsa.ENCRYPT_DICTIONARY[char]
        # print(f'ascii:  {ascii_value}')
        encrypted_char = (ascii_value ** exp) % public_key
        ciph.append(encrypted_char)
    return ciph


cipher = encrypt_input(text_to_list)
separator = " "
print(f'your cipher is: {separator.join(map(str, cipher))}')
