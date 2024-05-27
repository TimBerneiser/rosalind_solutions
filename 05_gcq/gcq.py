#!/usr/bin/env python3
"""
Author : tim <tim@localhost>
Date   : 2024-05-25
Purpose: Get sequence with highest GC content
"""

import argparse
from typing import NamedTuple, TextIO, List
from Bio import SeqIO


class Args(NamedTuple):
    """ Command-line arguments """
    files: List[TextIO]


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Get sequence with highest GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Enter fasta file(s)')

    args = parser.parse_args()

    return Args(args.files)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    highest = {'': 0}

    for fh in args.files:
        if seqs := [rec for rec in SeqIO.parse(fh.name, 'fasta')]:
            for seq in seqs:
                if get_gc(str(seq.seq)) > max(highest.values()):
                    highest = {seq.id: get_gc(str(seq.seq))}
                elif get_gc(str(seq.seq)) == max(highest.values()):
                    highest[seq.id] = get_gc(str(seq.seq))

    for key in highest.keys():
        print(f'{key}\n{highest[key]:.6f}')


# --------------------------------------------------
def get_gc(sequence: str) -> float:
    """ Get GC content of a sequence """

    gc_count = sequence.upper().count('G') + sequence.upper().count('C')
    
    if gc_count == 0:
        return 0
    
    return 100*gc_count/len(sequence)


# --------------------------------------------------
def test_get_gc() -> None:
    """ Test get_gc """

    assert get_gc('GGCC') == 100
    assert get_gc('GCTA') == 50
    assert get_gc('') == 0
    assert get_gc('AATT') == 0
    assert get_gc('actg') == 50
    assert get_gc('AaTtcGgTATTa') == 25


# --------------------------------------------------
if __name__ == '__main__':
    main()
