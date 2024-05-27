#!/usr/bin/env python3
"""
Author : tim <tim@localhost>
Date   : 2024-05-25
Purpose: Translate into protein
"""

import argparse
from typing import NamedTuple
import os
import re
import sys


class Args(NamedTuple):
    """ Command-line arguments """
    sequence: str
    stop: bool
    fshift: int


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Translate into protein',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='RNA/DNA sequence (or txt file)')

    parser.add_argument('-s',
                        '--stop',
                        metavar='stop',
                        type=bool,
                        default=False,
                        help='Stop translating at stop codon')

    parser.add_argument('-f',
                        '--fshift',
                        metavar='frame_shift',
                        type=int,
                        default=0,
                        help='Shift reading frame')

    args = parser.parse_args()

    if os.path.isfile(args.sequence):
        args.sequence = open(args.sequence).read().rstrip()

    if not 0 <= args.fshift <=2:
        sys.exit(f'Frame shift has to be between 0 and 2, is "{args.fshift}"')

    return Args(args.sequence, args.stop, args.fshift)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    print(translate(args.sequence, args.stop, args.fshift))


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
def test_translate() -> None:
    """ Tests translate """

    assert(translate('AAC')) == 'N'
    assert(translate('ACCUGACGG')) == 'T*R'
    assert(translate('ACCUGACGG', stop=True)) == 'T'
    assert(translate('ACCUGACGGGC')) == 'T*R'
    assert(translate('AACCUGACGGGC', shift=1)) == 'T*R'


# --------------------------------------------------
if __name__ == '__main__':
    main()
