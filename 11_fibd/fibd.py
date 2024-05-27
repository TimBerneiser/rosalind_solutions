#!/usr/bin/env python3
"""
Author : tim <tim@localhost>
Date   : 2024-05-07
Purpose: Calculate Fibonacci
"""

import argparse
from typing import NamedTuple
from functools import lru_cache


class Args(NamedTuple):
    """ Command-line arguments """
    generations: int
    survival: int


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Calculate Fibonacci',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('generation',
                        metavar='GEN',
                        type=int,
                        help='Litter generation')

    parser.add_argument("survival",
                        type=int,
                        help='Months after which rabbits die',
                        metavar='LIT')

    args = parser.parse_args()

    if not 1 <= args.generation <= 100:
        parser.error(f'generations "{args.generation}" must be between 1 and 100')

    if not 1 <= args.survival<= 20:
        parser.error(f'Months "{args.survival}" must be between 1 and 20')

    return Args(generations = args.generation, survival = args.survival)


## --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    print(fib(args.generations, args.survival)[0])


# --------------------------------------------------
@lru_cache()
def fib(gen, months):
    """ Recusively calculate Fibonacci sequence with mortal rabbits """

    litter_size = 0
    pregnancies = 0

    if gen == 1:
        return [1, 0]
    if gen == 2:
        return [1, 1]
    if gen == 0:
        return [0, 1]
    if gen <= 0:
        return [0, 0]

    for i in range(months+1)[1:]:
        litter_size += fib(gen-i, months)[1]
    for i in range(months+1)[2:]:
        pregnancies += fib(gen-i, months)[1]

    return [litter_size, pregnancies]


# --------------------------------------------------
if __name__ == '__main__':
    main()
