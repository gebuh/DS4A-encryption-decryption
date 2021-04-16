"""
input: cipher - space separated list of numbers - no commas or quotes
output: original text (we hope)
"""
import sys
from rsa_calc import RSACalc
from arguments import Arguments


def main():
    args = Arguments.get_arguments()
    rsa = RSACalc(args.pprime, args.qprime)
    private_key = rsa.private_key
    public_key = rsa.public_key

    cipher_string = get_input_from_user()
    raw_cipher_list = cipher_string.split()  # get rid of commas
    clean_cipher_list = convert_str_list_to_int_list(raw_cipher_list)
    decrypted_str = decrpyt_cipher(clean_cipher_list, private_key, public_key, rsa)
    print(f'is this your string?: {decrypted_str}')


# get input from the user

def get_input_from_user():
    cipher_string = input("give me your cipher: ")
    if not cipher_string:
        sys.exit("you have to give me something to work with son, enter a space separated string of integers")
    return cipher_string


# take user input converted from string to list of ints or die trying
# return a list of ints
def convert_str_list_to_int_list(raw_list):
    cipher_list = []
    for each in raw_list:
        try:
            cipher_list.append(int(each))
        except ValueError:
            sys.exit("THIS ISN'T A CIPHER - SHOULD ONLY CONSIST OF SPACE SEPARATED INTEGERS")
    return cipher_list


# return a decrypted string from a list of ints, decrypts each char then
# gets string value from ascii
# returns the final string
def decrpyt_cipher(clean_ciph_list, private_key, public_key, rsa):
    decrypted_list = []
    try:
        for each in clean_ciph_list:
            decrypted_ascii = (each ** private_key) % public_key
            decrypted_char = rsa.DECRYPT_DICTIONARY[decrypted_ascii]
            decrypted_list.append(decrypted_char)
            # print(f'encryt char: {each}, decrypted ascii number: {decrypted_ascii}, original char: {decrypted_char}')
    except KeyError:
        sys.exit("decryption failed, i'm outta here, are you using the correct primes?")
    decrypted_string = ''.join(decrypted_list)
    return decrypted_string


if __name__ == "__main__":
    main()
