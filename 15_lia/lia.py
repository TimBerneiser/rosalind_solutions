#!/usr/bin/env python3
"""
Author : tim <tim@localhost>
Date   : 2024-05-29
Purpose: Independent Alleles
"""

import argparse
from typing import NamedTuple
from functools import lru_cache
from math import comb
import re


class Args(NamedTuple):
    """ Command-line arguments """
    gen: int
    n: int
    genotype: str
    offspring: str

# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Independent Alleles',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('gen',
                        metavar='generation',
                        type=int,
                        help='Number of generations')

    parser.add_argument('n',
                        metavar='offspring',
                        type=int,
                        help='Number of offspring with AaBb phenotype')

    parser.add_argument('-g',
                        '--genotype',
                        metavar='genotype',
                        type=str,
                        choices=['AaBb', 'Aa Bb', 'AaBB', 'Aa BB', 'Aabb', 'Aa bb'
                                 'AABb', 'AA Bb', 'AABB', 'AA BB', 'AAbb', 'AA bb'
                                 'aaBb', 'aa Bb', 'aaBB', 'aa BB', 'aabb', 'aa bb'],
                        default='AaBb',
                        help='Genotype of the first individual in gen 0')

    parser.add_argument('-o',
                        '--offspring',
                        metavar='genotype',
                        type=str,
                        choices=['AaBb', 'Aa Bb', 'AaBB', 'Aa BB', 'Aabb', 'Aa bb'
                                 'AABb', 'AA Bb', 'AABB', 'AA BB', 'AAbb', 'AA bb'
                                 'aaBb', 'aa Bb', 'aaBB', 'aa BB', 'aabb', 'aa bb'],
                        default='AaBb',
                        help='Genotype of the wanted offspring')

    args = parser.parse_args()

    return Args(args.gen, args.n, args.genotype, args.offspring)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    prob_a = 0
    prob_b = 0


    if args.offspring.find('AA') != -1:
        k = 0
    elif args.offspring.find('Aa') != -1:
        k = 1
    else:
        k = 2

    if args.offspring.find('BB') != -1:
        m = 0
    elif args.offspring.find('Bb') != -1:
        m = 1
    else:
        m = 2


    if args.genotype.find('AA') != -1:
        prob_a = rec_lia(args.gen, 1, 0, 0)[k]
    elif args.genotype.find('Aa') != -1:
        prob_a = rec_lia(args.gen, 0, 1, 0)[k]
    else:
        prob_a = rec_lia(args.gen, 0, 0, 1)[k]

    if args.genotype.find('BB') != -1:
        prob_b = rec_lia(args.gen, 1, 0, 0)[m]
    elif args.genotype.find('Bb') != -1:
        prob_b = rec_lia(args.gen, 0, 1, 0)[m]
    else:
        prob_b = rec_lia(args.gen, 0, 0, 1)[m]

    print(get_all_trial_prob(args.gen*2, args.n, prob_a*prob_b))


# --------------------------------------------------
def get_one_trial_prob(n, k, k_prob):
    """ Probability that exactly k trials of n will be successful """

    return comb(n, k)* k_prob**k * (1-k_prob)**(n-k)


# --------------------------------------------------
def get_all_trial_prob(n, k, k_prob):
    """ Probability that at least k trials of n will be successful """

    prob = 0

    for i in range(n+1)[k:]:
        prob += get_one_trial_prob(n, i, k_prob)

    return prob


# --------------------------------------------------
@lru_cache
def rec_lia(gen, AA=0, Aa=1, aa=0):
    """ Recursively calculate offspring allele probability in gen
        Number of starting alleles
        Subsequent mating only with Aa partner
    """

    if gen == 0:
        sum_all = AA+Aa+aa
        return [AA/sum_all, Aa/sum_all, aa/sum_all]

    prob_AA = rec_lia(gen-1, AA, Aa, aa)[0]*0.5 + rec_lia(gen-1, AA, Aa, aa)[1]*0.25

    prob_Aa = rec_lia(gen-1, AA, Aa, aa)[0]*0.5 + rec_lia(gen-1, AA, Aa, aa)[1]*0.5 + rec_lia(gen-1, AA, Aa, aa)[2]*0.5

    prob_aa = rec_lia(gen-1, AA, Aa, aa)[1]*0.25 + rec_lia(gen-1, AA, Aa, aa)[2]*0.5

    return [prob_AA, prob_Aa, prob_aa]


# --------------------------------------------------
if __name__ == '__main__':
    main()
