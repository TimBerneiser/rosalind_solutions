#!/usr/bin/env python3
"""
Author : tim <tim@localhost>
Date   : 2024-05-27
Purpose: Find occurences of substring
"""

import argparse
from typing import NamedTuple, List
import os


class Args(NamedTuple):
    """ Command-line arguments """
    sequence: str
    motif: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Find occurences of substring',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        metavar='sequence',
                        type=str,
                        help='Enter DNA sequence')

    parser.add_argument('motif',
                        metavar='motif',
                        type=str,
                        help='Enter motif')

    args = parser.parse_args()

    if os.path.isfile(args.seq):
        args.seq = open(args.seq).read().rstrip()

    if os.path.isfile(args.motif):
        args.motif = open(args.motif).read().rstrip()

    return Args(args.seq, args.motif)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    print([index+1 for index, kmer in enumerate(get_kmers(args.sequence, len(args.motif))) if kmer==args.motif])


# --------------------------------------------------
def get_kmers(sequence: str, k: int) -> List[str]:
    """ Get all k-mers in sequence """

    return [sequence[i:i+k] for i in range(len(sequence)-k+1)]


# --------------------------------------------------
def test_get_kmers() -> None:
    """ Test get_kmers """

    assert get_kmers('ABCDEFG', 3) == ['ABC', 'BCD', 'CDE', 'DEF', 'EFG']
    assert get_kmers('ABCDEFG', 2) == ['AB', 'BC', 'CD', 'DE', 'EF', 'FG']
    assert get_kmers('', 3) == []


# --------------------------------------------------
if __name__ == '__main__':
    main()
