#!/usr/bin/env python3
"""
Author : tim <tim@localhost>
Date   : 2024-11-22
Purpose: Return lexographically ordered strings of length n formed from alphabet
"""

import argparse
from typing import NamedTuple
import sys


class Args(NamedTuple):
    """ Command-line arguments """
    alphabet: str
    length: int


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Return lexographically ordered strings of length n formed from alphabet',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('alphabet',
                        help='alphabet (max 10 symbols)',
                        metavar='alph',
                        type=str
                        )

    parser.add_argument('length',
                        help='Length of the output strings (max 10)',
                        metavar='length',
                        type=int
                        )

    args = parser.parse_args()

    if len("".join(args.alphabet).split()) > 10:
        sys.exit(
            'Alphabet has to contain less than 10 symbols, has '
            f'{len("".join(args.alphabet).split())}')

    if args.length > 10:
        sys.exit(f'Length of string has to be less than 10, is {args.length}')

    return Args(args.alphabet, args.length)

# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    #Order Alphabet
    alphabet = "".join(args.alphabet.split())
    alphabet = "".join(sorted(alphabet))

    #Create substrings
    substrings = list(alphabet)
    length = args.length
    while length > 1:
        new_subs = []
        for char in alphabet:
            for element in substrings:
                new_subs.append(f'{char}{element}')
        length += -1
        substrings = new_subs
    print(substrings)

# --------------------------------------------------
if __name__ == '__main__':
    main()
