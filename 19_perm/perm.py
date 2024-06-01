#!/usr/bin/env python3
"""
Author : tim <tim@localhost>
Date   : 2024-05-31
Purpose: Find permutations
"""

import argparse
from typing import NamedTuple


class Args(NamedTuple):
    """ Command-line arguments """
    integer: int


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Find permutations',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('integer',
                        metavar='int',
                        type=int,
                        help='Length of permutation')


    args = parser.parse_args()

    return Args(args.integer)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    first_perm = ''.join(str(x+1) for x in list(range(args.integer)))

    permutations = list(generate_perms(first_perm))

    print(f'{len(permutations)}\n' + '\n'.join(permutations))


# --------------------------------------------------
def generate_perms(permutable):
    """ Generator for all permutations """

    if len(permutable) <= 1:
        yield permutable 
        return

    for i in range(len(permutable)):
        for perm in generate_perms(''.join([permutable[i+1:], permutable[:i]])):
            yield permutable[i] + perm


# --------------------------------------------------
if __name__ == '__main__':
    main()
