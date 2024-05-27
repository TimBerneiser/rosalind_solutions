#!/usr/bin/env python3
"""
Author : tim <tim@localhost>
Date   : 2024-05-25
Purpose: Count nucleotides
"""

import argparse
from typing import NamedTuple, Dict
import os


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

    counter = count_bases(args.sequence)

    print(counter)


# --------------------------------------------------
def count_bases(sequence: str) -> Dict[str, int]:
    """ Count bases in string """

    counter = {}

    for base in sequence:
        if base.upper() in counter.keys():
            counter[base.upper()]+=1
        else:
            counter[base.upper()]=1

    return counter


# --------------------------------------------------
def test_count_bases() -> None:
    """ Test count_bases """

    assert count_bases('') == {}
    assert count_bases('AAA') == {'A': 3}
    assert count_bases('BbB') == {'B': 3}
    assert count_bases('ABC') == {'A': 1, 'B': 1, 'C': 1}
    assert count_bases('ABCaBC') == {'A': 2, 'B': 2, 'C': 2}
    assert count_bases('ABCDEFG') == {'A':1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1}
    assert count_bases('AABbbCAA') == {'A': 4, 'B': 3, 'C': 1}


# --------------------------------------------------
if __name__ == '__main__':
    main()
