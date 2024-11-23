#!/usr/bin/env python3
"""
Author : tim <tim@localhost>
Date   : 2024-11-22
Purpose: Longest increasing and decreasing subsequence
"""

import argparse
from typing import NamedTuple, TextIO
import sys


class Args(NamedTuple):
    """ Command-line arguments """
    length: int
    permutation: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Longest increasing and decreasing subsequence',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('length',
                        metavar='length',
                        type=int,
                        help='Length of permutation')

    parser.add_argument('permutation',
                        metavar='perm',
                        type=str,
                        help='Permutation of numbers, string separated by whitespace')

    args = parser.parse_args()

    if args.length > 10000:
        sys.exit(f'Length of permutation has to be less than 10000, is {args.length}.')

    if args.length != len(args.permutation.split()):
        sys.exit(f'Permutation is not of length {args.length}')

    return Args(args.length, args.permutation)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    permutation = [int(x) for x in args.permutation.split()]

    inc_perms = list()
    dec_perms = list()

    for index in range(len(permutation)-1):
        inc_perms.append(incr_perm(permutation[index], permutation[index+1:]))

    for index in range(len(permutation)-1):
        dec_perms.append(decr_perm(permutation[index], permutation[index+1:]))

    print([x for x in inc_perms if len(x)==max([len(x) for x in inc_perms])][0])
    print([x for x in dec_perms if len(x)==max([len(x) for x in dec_perms])][0])


# --------------------------------------------------
def incr_perm(high, permutation):
    """ Give the longest increasing permutation """

    if permutation == []:
        return([high])

    if high > max(permutation):
        return([high])

    inc_perms = [high]
    inc = []
    for index in range(len(permutation)):
        if high < permutation[index]:
            inc = [high] + incr_perm(permutation[index], permutation[index+1:])
        if len(inc) >= len(inc_perms):
            inc_perms = inc

    return(inc_perms)


# --------------------------------------------------
def decr_perm(low, permutation):
    """ Give the longest decreasing permutation """

    if permutation == []:
        return([low])

    if low < min(permutation):
        return([low])

    dec_perms = [low]
    dec = []
    for index in range(len(permutation)):
        if low > permutation[index]:
            dec = [low] + decr_perm(permutation[index], permutation[index+1:])
        if len(dec) >= len(dec_perms):
            dec_perms = dec

    return(dec_perms)


# --------------------------------------------------
if __name__ == '__main__':
    main()
