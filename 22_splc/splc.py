#!/usr/bin/env python3
"""
Author : tim <tim@localhost>
Date   : 2024-06-01
Purpose: Splice out introns
"""

import argparse
from typing import NamedTuple, TextIO
import re


class Args(NamedTuple):
    """ Command-line arguments """
    fasta: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Splice out introns',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('fasta',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Fasta file containing sequence and introns')

    args = parser.parse_args()

    return Args(args.fasta)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    get_spliced(sequence, introns)


# --------------------------------------------------
def get_spliced(sequence: str, introns: list) -> str:
    """ Get spliced sequence """

    spliced = sequence

    for _, intron in enumerate(introns):
        spliced = re.sub(intron, '', spliced, re.IGNORECASE)

    return spliced


# --------------------------------------------------
def test_get_spliced() -> None:
    """ Test get_spliced """

    assert get_spliced('ABCDEFGAAAHIJKLMBBBBBBNOP', ['AAA', 'BBBBBB']) == 'ABCDEFGHIJKLMNOP'
    assert get_spliced('ABC', []) == 'ABC'
    assert get_spliced('', ['ABC', 'BCD']) == ''


# --------------------------------------------------
if __name__ == '__main__':
    main()
