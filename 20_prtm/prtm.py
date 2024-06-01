#!/usr/bin/env python3
"""
Author : tim <tim@localhost>
Date   : 2024-06-01
Purpose: Calculate protein mass
"""

import argparse
from typing import NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    protein: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Calculate protein mass',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('protein',
                        metavar='prot',
                        type=str,
                        help='Input amino acid sequence')

    args = parser.parse_args()

    return Args(args.protein)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    print(f'{get_protein_mass(args.protein):.3f}')

# --------------------------------------------------
def get_protein_mass(sequence: str) -> float:
    """ Get protein mass """

    aa_masses = {'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259,
                 'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I': 113.08406,
                 'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293,
                 'P': 97.05276, 'Q': 128.05858, 'R': 156.10111, 'S': 87.03203,
                 'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333}

    weight = 0

    for aa in sequence.upper():
        weight += aa_masses[aa]

    return weight


# --------------------------------------------------
if __name__ == '__main__':
    main()
