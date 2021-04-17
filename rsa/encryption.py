"""
simple encryption script
input: string from user, limited to upper/lower case letters, numbers, punctuation and whitespace
output: encrypted text as cipher

"""
import sys
from arguments import Arguments
from rsa_calc import RSACalc


def main():
    args = Arguments.get_arguments()
    rsa = RSACalc(args.pprime, args.qprime)
    user_text = get_input_from_user()
    text_to_list = list(user_text)
    print(f'List of Characters ={text_to_list}')
    cipher = encrypt_input(text_to_list, rsa)
    separator = " "
    print(f'your cipher is: {separator.join(map(str, cipher))}')


def get_input_from_user():
    user_text = input("give me some text: ")
    if not user_text or not user_text.isprintable():
        sys.exit("you have to input numbers, letters or punctuation")
    return user_text


def encrypt_input(converted_text, rsa):
    exp = rsa.exponent
    public_key = rsa.public_key
    ciph = []

    for char in converted_text:
        ascii_value = rsa.ENCRYPT_DICTIONARY[char]
        # print(f'ascii:  {ascii_value}')
        encrypted_char = (ascii_value ** exp) % public_key
        ciph.append(encrypted_char)
    return ciph


if __name__ == "__main__":
    main()
