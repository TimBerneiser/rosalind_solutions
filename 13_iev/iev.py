#!/usr/bin/env python3
"""
Author : tim <tim@localhost>
Date   : 2024-05-29
Purpose: Calculating Expected Offspring
"""

import argparse
from typing import NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    a: int
    b: int
    c: int
    d: int
    e: int
    f: int


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Calculating Expected Offspring',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('a',
                        metavar='int',
                        type=int,
                        help='Number of AA-AA couples')

    parser.add_argument('b',
                        metavar='int',
                        type=int,
                        help='Number of AA-Aa couples')

    parser.add_argument('c',
                        metavar='int',
                        type=int,
                        help='Number of AA-a couples')

    parser.add_argument('d',
                        metavar='int',
                        type=int,
                        help='Number of Aa-Aa couples')

    parser.add_argument('e',
                        metavar='int',
                        type=int,
                        help='Number of Aa-aa couples')

    parser.add_argument('f',
                        metavar='int',
                        type=int,
                        help='Number of aa-aa couples')


    args = parser.parse_args()

    return Args(args.a, args.b, args.c, args.d, args.e, args.f)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    print(args.a*2+args.b*2+args.c*2+args.d*0.75*2+args.e*0.5*2)

# --------------------------------------------------
if __name__ == '__main__':
    main()
