"""
seems like overkill now, but put all commandline args here
any static methods shared between scripts so I don't have to write them more than once
"""

import argparse


class Arguments:

    @staticmethod
    def get_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("pprime", type=int, nargs="?", default=0, help="custom p (co prime), has to be a prime int")
        parser.add_argument("qprime", type=int, nargs="?", default=0, help="custom q (co prime), has to be a prime int")
        args = parser.parse_args()
        return args
