#!/usr/bin/env python3
"""
Author : tim <tim@localhost>
Date   : 2024-05-25
Purpose: Calculate Hamming distance
"""

import argparse
from typing import NamedTuple
import os
from itertools import zip_longest
from Bio import Align


class Args(NamedTuple):
    """ Command-line arguments """
    seq1: str
    seq2: str
    align: bool


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Calculate Hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq1',
                        metavar='sequence',
                        type=str,
                        help='Sequence 1')

    parser.add_argument('seq2',
                        type=str,
                        metavar='sequence',
                        help='Sequence 2')

    parser.add_argument('-a',
                        '--align',
                        metavar='align',
                        type=bool,
                        default=False,
                        help='Align sequences?')

    args = parser.parse_args()

    if os.path.isfile(args.seq1):
        args.seq1 = open(args.seq1).read().rstrip()

    if os.path.isfile(args.seq2):
        args.seq2 = open(args.seq2).read().rstrip()

    return Args(args.seq1, args.seq2, args.align)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    seq1 = args.seq1
    seq2 = args.seq2

    if args.align:
        aligner = Align.PairwiseAligner()
        aligned = aligner.align(seq1, seq2)
        seq1 = aligned[0][0]
        seq2 = aligned[0][1]

    print(get_hamming(seq1, seq2))


# --------------------------------------------------
def get_hamming(seq1: str, seq2: str) -> int:
    """ Compute Hamming distance """

    return sum((1 for c1, c2 in zip_longest(seq1, seq2) if c1 != c2))


# --------------------------------------------------
def test_get_hamm() -> None:
    """ Test get_hamm """

    assert get_hamming('', '') == 0
    assert get_hamming('A-A', 'ATA') == 1
    assert get_hamming('AACC', 'AA') == 2
    assert get_hamming('ACGCAACG', 'CGAGCCGA') == 8
    assert get_hamming('AACCGGCCAA', 'ACCGGCCAAT') == 5


# --------------------------------------------------
if __name__ == '__main__':
    main()
