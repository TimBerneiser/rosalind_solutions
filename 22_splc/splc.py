#!/usr/bin/env python3
"""
Author : tim <tim@localhost>
Date   : 2024-06-01
Purpose: Splice out introns
"""

import argparse
from typing import NamedTuple, TextIO
import re
from Bio import SeqIO


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

    sequences = []

    for rec in SeqIO.parse(args.fasta, 'fasta'):
        if rec:
            sequences.append(str(rec.seq))

    print(translate(get_spliced(sequences[0], sequences[1:]))[:-1])


# --------------------------------------------------
def get_spliced(sequence: str, introns: list) -> str:
    """ Get spliced sequence """

    spliced = sequence

    for _, intron in enumerate(introns):
        spliced = re.sub(intron, '', spliced, re.IGNORECASE)

    return spliced


# --------------------------------------------------
def translate(sequence: str, stop=False, shift=0) -> str:
    """ Translates an RNA or DNA sequence """

    sequence = sequence.upper()

    if sequence.find('T'):
        sequence = re.sub('t', 'u', re.sub('T', 'U', sequence))

    codon_table = {
        "UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V",
        "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V",
        "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V",
        "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V",
        "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A",
        "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
        "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
        "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
        "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D",
        "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
        "UAA" : "*", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
        "UAG" : "*", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
        "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G",
        "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
        "UGA" : "*", "CGA" : "R", "AGA" : "R", "GGA" : "G",
        "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G"
    }

    codons = [sequence[i:i+3] for i in range(shift, len(sequence), 3) if len(sequence[i:i+3])==3]

    aas = [codon_table.get(codon) for codon in codons]

    if '*' in aas and stop:
        return ''.join(aas[:aas.index('*')])

    return ''.join(aas)


# --------------------------------------------------
def test_get_spliced() -> None:
    """ Test get_spliced """

    assert get_spliced('ABCDEFGAAAHIJKLMBBBBBBNOP', ['AAA', 'BBBBBB']) == 'ABCDEFGHIJKLMNOP'
    assert get_spliced('ABC', []) == 'ABC'
    assert get_spliced('', ['ABC', 'BCD']) == ''


# --------------------------------------------------
if __name__ == '__main__':
    main()
