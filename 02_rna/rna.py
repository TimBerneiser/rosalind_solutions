#!/usr/bin/env python3
"""
Author : tim <tim@localhost>
Date   : 2024-05-25
Purpose: Transcribe DNA to RNA
"""

import argparse
from typing import NamedTuple
import os
import re


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

    print(transcribe(args.sequence))


# --------------------------------------------------
def transcribe(seq: str) -> str:
    """ Transcribe DNA to RNA """

    return re.sub('t', 'u', re.sub('T', 'U', seq))


# --------------------------------------------------
def test_transcribe() -> None:
    """ Test transcribe """

    assert transcribe('') == ''
    assert transcribe('12hd!§483') == '12hd!§483'
    assert transcribe('ABCDEFG') == 'ABCDEFG'
    assert transcribe('ATTCATA') == 'AUUCAUA'
    assert transcribe('AaTtCcTtU') == 'AaUuCcUuU'
    assert transcribe('TTTtTT') == 'UUUuUU'
    assert transcribe('UT') == 'UU'


# --------------------------------------------------
if __name__ == '__main__':
    main()
