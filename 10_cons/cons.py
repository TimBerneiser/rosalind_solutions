#!/usr/bin/env python3
"""
Author : tim <tim@localhost>
Date   : 2024-05-27
Purpose: Find consensus sequence
"""

import argparse
from typing import NamedTuple, TextIO, List, Dict
import pandas as pd
from Bio import SeqIO


class Args(NamedTuple):
    """ Command-line arguments """
    files: List[TextIO]


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Find consensus sequence',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILES',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Input FASTA file(s)')

    args = parser.parse_args()

    return Args(args.files)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    seqs_list = []

    for fh in args.files:
        if seqs := SeqIO.parse(fh, 'fasta'):
            for seq in seqs:
                bases = [base for index, base in enumerate(str(seq.seq).upper())]
                seqs_list.append(bases)

    seqs_df = pd.DataFrame(seqs_list)

    profile_matrix = seqs_df.apply(lambda x: x.value_counts()).fillna(0).astype(int)

    consensus = profile_matrix.apply(lambda x: x.idxmax()).to_string(header=False, index=False).split('\n')

    profile_matrix = profile_matrix.to_string(header=False)

    print(''.join(consensus))
    print(''.join(profile_matrix))


# --------------------------------------------------
if __name__ == '__main__':
    main()
