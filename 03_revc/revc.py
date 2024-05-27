#!/usr/bin/env python3
"""
Author : tim <tim@localhost>
Date   : 2024-05-25
Purpose: Reverse complement of a sequence
"""

import argparse
from typing import NamedTuple
import os
import sys


class Args(NamedTuple):
    """ Command-line arguments """
    sequence: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Count nucleotides',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='Sequence (txt file)')

    args = parser.parse_args()

    if os.path.isfile(args.sequence):
        args.sequence = open(args.sequence).read().rstrip()

    return Args(args.sequence)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    reverse_seq(args.sequence)


# --------------------------------------------------
def reverse_seq(seq: str) -> str:
    """ Reverse complement to a sequence """

    revc = ''
    trans = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G',
             'a': 't', 't': 'a', 'g': 'c', 'c': 'g'}

    for base in seq[::-1]:
        if base not in trans.keys():
            sys.exit(f'Found "{base}" in sequence. Please enter a valid DNA sequence.')
        else:
            revc+=trans[base]

    return revc


# --------------------------------------------------
def test_reverse_seq() -> None:
    """ Test reverse_seq """

    assert reverse_seq('') == ''
    assert reverse_seq('ACTG') == 'CAGT'
    assert reverse_seq('AAAA') == 'TTTT'
    assert reverse_seq('atTgC') == 'GcAat'
    assert reverse_seq('AttA') == 'TaaT'
    assert reverse_seq('aTTa') == 'tAAt'


# --------------------------------------------------
if __name__ == '__main__':
    main()
