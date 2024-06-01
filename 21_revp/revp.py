#!/usr/bin/env python3
"""
Author : tim <tim@localhost>
Date   : 2024-06-01
Purpose: Locate restriction sites
"""

import argparse
from typing import NamedTuple, TextIO, List, Tuple
from Bio import SeqIO, Seq


class Args(NamedTuple):
    """ Command-line arguments """
    file: TextIO


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Locate restriction sites',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input FASTA file',
                        type=argparse.FileType('rt'))

    args = parser.parse_args()

    return Args(args.file)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    seq = ''
    seqs = SeqIO.parse(args.file, 'fasta')
    for fasta in seqs:
        seq = str(fasta.seq)

    for i, j in locate_palis(seq):
        print(i+1, j)


# --------------------------------------------------
def find_kmers(seq: str, k: int) -> List[int]:
    """ Create a list of all k-mers in a sequence """

    return [seq[i:i+k] for i in range(len(seq)-k+1)]


# --------------------------------------------------
def test_find_kmers() -> None:
    """ Test find_kmers """

    assert find_kmers('', 4) == []
    assert find_kmers('AACC', 3) == ['AAC', 'ACC']
    assert find_kmers('ACTG', 1) == ['A', 'C', 'T', 'G']
    assert find_kmers('ACTGCGTCA', 10) == []
    assert find_kmers('ACTGCGTCA', 4) == ['ACTG', 'CTGC', 'TGCG', 'GCGT', 'CGTC', 'GTCA']


# --------------------------------------------------
def locate_palis(seq: str, low=4, high=12) -> List[Tuple[int, int]]:
    """ Takes a sequence and returns length and INDEX of all palindromes """

    pali_positions = []

    for k in range(low, high+1):
        position = 0
        for i in find_kmers(seq, k):
            if Seq.reverse_complement(i) == i:
                pali_positions.append((position, k))
            position += 1

    return sorted(pali_positions, key=lambda x: x[0])


# --------------------------------------------------
def test_locate_palis() -> None:
    """ Test locate_palis """

    assert locate_palis('') == []
    assert locate_palis('ATATCAATATGACAGT') == [(1, 4), (7, 4)]


# --------------------------------------------------
if __name__ == '__main__':
    main()
