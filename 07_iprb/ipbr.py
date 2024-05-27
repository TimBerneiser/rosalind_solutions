#!/usr/bin/env python3
"""
Author : tim <tim@localhost>
Date   : 2024-05-25
Purpose: Compute simple Mendelian probability
"""

import argparse
from typing import NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    k: int
    m: int
    n: int


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Compute simple Mendelian probability',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('k',
                        metavar='dominant',
                        type=int,
                        help='Homozygous dominant individuals')

    parser.add_argument('m',
                        metavar='hetero',
                        type=int,
                        help='Heterozygous individuals')

    parser.add_argument('n',
                        metavar='recessive',
                        type=int,
                        help='Homozygous recessive individuals')

    args = parser.parse_args()

    return Args(args.k, args.m, args.n)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    k = args.k
    m = args.m
    n = args.n
    summed = k + m + n
    prob = 1/summed * (k 
                      + m/2 + (m*k)/(2*(summed-1)) + ((m-1)*m)/(4*(summed-1)) 
                      + (n*k)/(summed-1) + (n*m)/(2*(summed-1)))

    print(f'{prob:.6f}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
