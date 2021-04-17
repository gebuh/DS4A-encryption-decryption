"""
seems like overkill now, but put all commandline args here
any static methods shared between scripts so I don't have to write them more than once
"""

import argparse


class Arguments:

    @staticmethod
    def get_arguments():
        DESC_MSG = "Simple encryption/decryption script. Use the default primes or enter your own"
        P_PRIME_MSG = "Optional prime (p), has to be a prime int"
        Q_PRIME_MSG = "Optional co-prime to p (q), has to be an int that is coprime to p"

        parser = argparse.ArgumentParser(description=DESC_MSG)
        parser.add_argument("pprime", type=int, nargs="?", default=0, help=P_PRIME_MSG)
        parser.add_argument("qprime", type=int, nargs="?", default=0, help=Q_PRIME_MSG)
        args = parser.parse_args()
        return args
