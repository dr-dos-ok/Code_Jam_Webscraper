#!/usr/bin/env python3

import itertools
from pprint import pprint

from scipy.stats import bernoulli
from sympy.ntheory import divisors


def solve_for_base(x, base):
    n = int(x, base)
    return next(itertools.dropwhile(lambda x: x in [1, n], divisors(n, generator=True)), None)


def solve(x):
    answer = [solve_for_base(x, base) for base in range(2, 11)]
    return None if any(x is None for x in answer) else answer


def generate_test(p, n):
    return '1' + ''.join(bernoulli.rvs(p, size=n - 2).astype('str')) + '1'


def brute_small():
    answers = {}
    while len(answers) < 50:
        t = generate_test(0.3, 16)
        while t in answers:
            t = generate_test(0.3, 16)
        ans = solve(t)
        if ans is not None:
            answers[t] = ans
    print('Case #1:')
    for k, v in answers.items():
        print(k, ' '.join(map(str, v)))


def solve_naive(z):
    answer = [y if x % y == 0 else None for x, y in zip([int(z, base) for base in range(2, 11)],
                                                        [3, 2, 5, 2, 5, 2, 3, 2, 11])]
    return None if any(x is None for x in answer) else answer

def brute_large():
    # answers = {'10000100000010000001000000101011': [199, 2, 13, 2, 40093, 2, 17592067551073, 2, 125639],
    #            '10000000000101100001000000000001': [23, 2, 3, 2, 13, 2, 21651838067, 2, 3],
    #            '10001001000001010001100000010011': [5, 2, 13, 2, 5, 2, 103, 2, 12497],
    #            '10010110011000000000000010000001': [3, 2, 5, 2, 7, 2, 3, 2, 11],
    #            '11010011000001000000001000010001': [3, 5, 3, 3, 271, 3, 3, 11, 3],
    #            '10000000111100000000000000000001': [3, 2, 3, 2, 7, 2, 3, 2, 3],
    #            '10010010000010000010110000000001': [11, 2, 43, 2, 29, 2, 283, 2, 1303],
    #            '10000000100000000011100000000001': [7, 2, 3, 2, 19, 2, 73, 2, 3],
    #            '10001101000100010001010000001001': [17, 2, 7, 2, 5, 2, 67, 2, 17],
    #            '11100001000010000000100000000001': [71, 5, 41, 41, 41, 13, 5, 23, 31],
    #            '11000000000001000000100100000001': [13, 2, 3, 2, 11, 2, 12421, 2, 3],
    #            '10000011000000001010100000010001': [47, 2, 7, 2, 23, 2, 5, 2, 47],
    #            '10010000000000000010000010000001': [5, 7, 29, 57427, 5, 5, 11, 338556070837, 7],
    #            '10110000101000000000001010001011': [3, 2, 13, 2, 5, 2, 3, 2, 7],
    #            '10000000010000000001000000000011': [71, 53, 7, 7, 5, 8209, 677, 29, 199],
    #            '10011110000101000000000000001001': [11, 5, 3, 101, 39922271, 3, 5, 1021, 3],
    #            '10100000010010000000010010010101': [5, 11, 3, 23, 97, 3, 71, 7, 3],
    #            '10000001000000001000101000000011': [3, 71, 7, 3, 13, 5, 3, 3301, 29],
    #            '10001011000001000001010000001011': [3, 2, 5, 2, 5, 2, 3, 2, 11],
    #            '10000100101100100000001000000011': [3, 461, 3, 3, 113, 3, 3, 11047273, 3],
    #            '10000000001001000011000011010001': [337, 4547, 3, 61, 613, 3, 19, 883, 3],
    #            '11000100000000010000010000010001': [7, 127, 5, 636953, 13, 347, 7, 5, 19],
    #            '11010000001000000000010000100001': [41, 8803177, 384819881, 509, 101, 17, 7, 29, 181],
    #            '10011000110001100101110100100001': [17, 2, 257, 2, 113, 2, 7, 2, 73],
    #            '10000001110100000000010101001001': [5, 2, 761, 2, 5, 2, 11, 2, 449201],
    #            '10000000100100000000111000000101': [3, 2, 5, 2, 7, 2, 3, 2, 7],
    #            '10101000000000001100000000000001': [97, 2, 3, 2, 67, 2, 23, 2, 3],
    #            '10000100000010000011000100010001': [1063, 2, 47, 2, 29, 2, 5, 2, 31],
    #            '10100010000100101100001000000011': [109, 2, 4937, 2, 5, 2, 5, 2, 173],
    #            '10010100000000001100000000100011': [3, 2, 5, 2, 7, 2, 3, 2, 11],
    #            '10100000001000010000000100000001': [3, 2, 3, 2, 7, 2, 3, 2, 3],
    #            '10110000011010000000100000000101': [47, 19, 3, 11, 11, 3, 569, 305671663993, 3],
    #            '11000000010000110000000100000001': [3, 89, 107, 3, 19, 11, 3, 47, 68667103],
    #            '11000000000101000011010000000011': [3, 716033, 3, 3, 13, 3, 3, 127, 3],
    #            '10000000000000100101010000000001': [5, 2, 3, 2, 37, 2, 5, 2, 3],
    #            '10001000000100000000010000000001': [13, 5, 218783, 11, 5, 144961, 5, 1309141373, 5578847],
    #            '10100001001000001000000100100001': [5, 2, 7, 2, 827, 2, 107, 2, 5168021],
    #            '10111000000000000010101000000001': [373, 2, 19, 2, 1854843889, 2, 11, 2, 203475101707321],
    #            '11100000000000010100000000100001': [1013, 7, 89153, 42557, 97, 26627, 7, 1931, 7],
    #            '10100010010000001000000011000001': [31, 2, 7, 2, 209821, 2, 11459533, 2, 1571668243657],
    #            '11100000001001100000000110010001': [3, 2, 5, 2, 5, 2, 3, 2, 11],
    #            '10101100000110001001100010000011': [7, 2, 3, 2, 43, 2, 5, 2, 3],
    #            '10100000000110000010000010010101': [5, 271, 3, 11, 13, 3, 193803851, 11243, 3],
    #            '10010000010000010010001000010001': [5, 2, 1933, 2, 17, 2, 23, 2, 31],
    #            '10000010011000000000000001001111': [5, 19, 3, 7, 47, 3, 79, 643, 3],
    #            '10100110101100010100000011000011': [37, 17, 1831, 17, 5623, 127, 457, 10993, 47],
    #            '10000010000000010001100100000101': [139, 2, 11, 2, 77293297, 2, 5, 2, 7],
    #            '10000000000010000010010000000001': [29, 7, 5717, 29, 5, 17, 2917, 23, 7],
    #            '10100000000000100000010000100001': [43, 2, 3, 2, 4021, 2, 3739, 2, 3],
    #            '10000000000100000001100100000001': [5, 2, 3, 2, 13, 2, 17, 2, 3],
    #            '10000000000010101000100100000001': [3, 1114381, 41, 3, 13, 17, 3, 79, 17],
    #            '10100001001100000000000100000011': [3, 2, 5, 2, 7, 2, 3, 2, 11],
    #            '10000011000101001000001100010001': [59, 2, 7, 2, 5, 2, 11, 2, 19],
    #            '11100010000001001100010001000001': [13, 2, 7, 2, 5, 2, 373, 2, 13],
    #            '10000000000100110011100000000001': [3, 2, 5, 2, 7, 2, 3, 2, 11],
    #            '10000000000000000000000000010001': [5, 67, 3, 43, 4423, 3, 6197, 127, 3],
    #            '10010000001000110010000000001101': [11, 5, 3, 383, 510007303583, 3, 5, 7487, 3],
    #            '10111000001000001000001100000001': [3, 457, 3, 3, 1453, 3, 3, 4999, 3],
    #            '10000010010010000000111110000001': [491, 2, 73, 2, 5, 2, 29, 2, 607],
    #            '11000000110001000000010100000001': [257, 2, 41, 2, 17, 2, 37, 2, 7],
    #            '10101000000001110000010000000001': [3, 2, 5, 2, 7, 2, 3, 2, 11],
    #            '10101110000000000001000000000111': [7, 13, 3, 31, 11, 3, 17, 7, 3],
    #            '11000000000000000000000001101001': [3, 2, 3, 2, 7, 2, 3, 2, 3],
    #            '10101010010001001000000010000001': [3, 109, 3, 3, 19, 3, 3, 23, 3],
    #            '10010100000001000000000101100001': [5, 2, 17, 2, 37, 2, 5, 2, 101],
    #            '10010100101010000001011001010001': [5167, 2, 3, 2, 97, 2, 55542437, 2, 3],
    #            '10000001000000000010001000010001': [3, 2, 3, 2, 7, 2, 3, 2, 3],
    #            '10000100000000000000000110000001': [11, 5, 643, 291474397, 5, 13, 5, 31, 13],
    #            '10000100100000000000000011010001': [103, 587, 7724447, 7, 107, 71, 7, 5233, 26473043],
    #            '10100100000000110000010101010001': [13, 2, 97, 2, 5, 2, 43, 2, 17],
    #            '10100000000000000000000010101001': [7, 2, 3, 2, 43, 2, 17, 2, 3],
    #            '11000100000000100010100000000001': [47, 2129, 2305777, 17, 23, 21487, 7, 94427, 13],
    #            '10001001000100010000100110000101': [61, 2, 5462917, 2, 5, 2, 79, 2, 761],
    #            '10000000011000001000100000000001': [47, 2, 3, 2, 73, 2, 11, 2, 3],
    #            '10000001101010001000000100000101': [67, 541, 3, 7, 103566332843, 3, 37, 1093327, 3],
    #            '10100000000000000000000100110001': [3, 2, 3, 2, 7, 2, 3, 2, 3],
    #            '10000000100000101000100000000001': [5, 2, 3, 2, 4383923, 2, 311, 2, 3],
    #            '10010000000000100100000000110101': [431, 2, 7, 2, 3001, 2, 79, 2, 2153986507],
    #            '10011000000110000001000100011001': [281, 2, 653, 2, 5, 2, 13, 2, 105509],
    #            '10011100000000100000000010000101': [3, 2, 5, 2, 7, 2, 3, 2, 11],
    #            '11100000100000000101000100010001': [3, 139, 3, 3, 103, 3, 3, 37, 3],
    #            '10000010011000001000001100100001': [3, 67, 3, 3, 191, 3, 3, 43, 3],
    #            '11000010010000000101100000010011': [5, 2, 17, 2, 5, 2, 5, 2, 13],
    #            '10000100010000001000000000000011': [3, 2, 3, 2, 7, 2, 3, 2, 3],
    #            '10000000110010010000001001001101': [3, 2, 5, 2, 5, 2, 3, 2, 7],
    #            '11000100000000000011100001010011': [5, 2, 17, 2, 5, 2, 5, 2, 31],
    #            '10000011010000001010001000100001': [3, 139, 3, 3, 1249, 3, 3, 181, 3],
    #            '10000110001100000000000000011001': [3, 2, 5, 2, 7, 2, 3, 2, 11],
    #            '10000001010001110010110000101001': [3, 2, 3, 2, 7, 2, 3, 2, 3],
    #            '10000110000000010001011000100101': [19, 2, 30869, 2, 5, 2, 593, 2, 167],
    #            '10001000000000000000000100000001': [3, 2, 5, 2, 7, 2, 3, 2, 11],
    #            '10000010000010000100000000100001': [5, 2, 3, 2, 37, 2, 5, 2, 3],
    #            '10000100001000000010001000000001': [31, 2, 3, 2, 127, 2, 11, 2, 3],
    #            '10001001100001000001000000001001': [3, 2, 5, 2, 7, 2, 3, 2, 11],
    #            '10001100000101010000101001000001': [7, 2, 5987, 2, 5, 2, 97, 2, 41],
    #            '10000011000001110000000000010011': [11, 11, 3, 13, 107383947173, 3, 101, 160580512991, 3],
    #            '10001000000001011000000100100001': [3, 2, 5, 2, 7, 2, 3, 2, 7],
    #            '10100000100000000000010010010001': [29, 5, 7, 7, 9109, 13, 5, 3499, 47],
    #            '10000000000000000100100000000001': [3, 2, 5, 2, 7, 2, 3, 2, 11],
    #            '10000010000100000100000110110101': [79, 2, 11, 2, 5, 2, 19, 2, 439694447117],
    #            '10000001000000000000000001000101': [3, 19, 809, 3, 5, 4547, 3, 14057, 13397],
    #            '10010000100101100000000101000001': [3, 43, 3, 3, 22168121, 3, 3, 7879, 3],
    #            '10000000000000000100000101000101': [9811, 2, 3, 2, 23, 2, 29, 2, 3],
    #            '11000000000000110100011000101111': [3, 2, 3, 2, 7, 2, 3, 2, 3],
    #            '10110001000011000000000000001101': [53, 5, 3, 7, 44641, 3, 5, 1097, 3],
    #            '11000001100101001000000100000001': [3, 19, 3, 3, 17, 3, 3, 367, 3],
    #            '11010100001000100101001000000001': [7, 2, 107, 2, 5, 2, 128055598871, 2, 47],
    #            '10000000001000110000100001100011': [3, 13, 3, 3, 19, 3, 3, 7, 3],
    #            '10100000101011000000011100100001': [3, 10639, 37, 3, 775309, 313, 3, 23, 89],
    #            '10010001100101111101010011101011': [461, 2, 3, 2, 4073, 2, 11, 2, 3],
    #            '11010100001001100000000011111101': [727, 2, 109, 2, 11, 2, 7, 2, 19],
    #            '10010100100000100101111000000001': [541, 17, 5839, 2347, 47, 2582208671111, 2243, 1439663, 127],
    #            '11100010100000000011000000000101': [7, 13, 3, 7, 43, 3, 73, 7, 3],
    #            '11100110110000010000000100000001': [5, 2, 17, 2, 5, 2, 5, 2, 101],
    #            '10010000100100010000000010000001': [19, 5, 7, 47, 7549, 23, 5, 53, 127],
    #            '11100000001111000001100100101101': [3, 2, 5, 2, 7, 2, 3, 2, 11],
    #            '11100000100000000101100000001001': [353, 4139, 3, 11113, 23, 3, 17, 548707, 3],
    #            '10110100011100010010100000000001': [7, 5, 109, 17, 53, 11, 5, 7, 181],
    #            '10000101110011111010110000001001': [863, 23, 3, 7, 5, 3, 149, 6473, 3],
    #            '11000001000010000000011100000001': [7, 2, 29, 2, 71699, 2, 109, 2, 7],
    #            '10010000000000010000100010010011': [3, 2, 5, 2, 7, 2, 3, 2, 11],
    #            '11001010100000000100010011010011': [3, 2, 3, 2, 7, 2, 3, 2, 3],
    #            '11010000001001000000001101010101': [19, 31, 5, 811, 71, 103, 280597, 5, 79],
    #            '10011000010000000000000101010101': [523, 5, 3, 97, 73, 3, 5, 5, 3],
    #            '10101000010010110001010111000011': [3, 2, 5, 2, 7, 2, 3, 2, 11],
    #            '11101010000000000000000100000011': [17, 2, 13, 2, 902413, 2, 5701, 2, 17],
    #            '10000000000000000100100001010011': [37, 37, 1783, 7, 109, 31, 7, 17, 16649],
    #            '10000100000001000011100000000011': [3, 2, 5, 2, 7, 2, 3, 2, 11],
    #            '11001010110001011011110100100001': [3, 2, 5, 2, 7, 2, 3, 2, 11],
    #            '10100100100001100110000000001001': [227, 2, 7, 2, 5, 2, 463, 2, 293],
    #            '11010000110000010011100010100101': [13, 5, 7, 266980697, 19, 53, 5, 11, 17],
    #            '10000000000100100100000010000001': [3, 2, 3, 2, 7, 2, 3, 2, 3],
    #            '10101000001000111010000100000001': [5, 2, 233, 2, 5, 2, 3181268604863, 2, 1987],
    #            '11010000011010000010000000101101': [23, 139, 7, 1980551191, 1070244193273, 17, 137, 38949569, 1187],
    #            '10000001000001001100000101001011': [41, 2, 23, 2, 5, 2, 16922112876871, 2, 97],
    #            '11001010100110010000100010100011': [11, 11, 5, 11, 378538893589, 17, 19, 5, 1861],
    #            '10000000011000110000100000000011': [17, 2, 19, 2, 241, 2, 4817, 2, 607],
    #            '10101000000110110001100100011101': [3, 2, 5, 2, 7, 2, 3, 2, 7],
    #            '10000010000100001000010000000001': [3, 2, 3, 2, 7, 2, 3, 2, 3],
    #            '10001010000011000110000001100101': [41, 53, 83, 53, 31, 281, 59, 19, 83737],
    #            '10000001000000101000001001111101': [13, 11, 72617, 3671, 13, 257, 71039, 27618763, 241],
    #            '10010100000001001000010101000001': [5, 31, 3, 3199521341, 41, 3, 999331, 5, 3],
    #            '10010010001010010011001010001111': [5, 2, 11, 2, 521, 2, 7, 2, 23],
    #            '10000100000010100000010010000001': [5, 7, 7, 37, 97, 5, 7, 11, 7],
    #            '10100110101011000001010110100011': [3, 61, 3, 3, 5, 3, 3, 43, 3],
    #            '11010100000000100000110010100001': [3, 2, 5, 2, 5, 2, 3, 2, 11],
    #            '10001001000001001010000000001101': [7, 499, 3, 7, 11, 3, 7023857, 7, 3],
    #            '10100000011011100000010010000001': [7, 2, 67, 2, 5, 2, 532372370051, 2, 7],
    #            '10001100100100111000011001011001': [3, 2, 5, 2, 7, 2, 3, 2, 11],
    #            '11000000010000001100000000100011': [3, 2, 5, 2, 7, 2, 3, 2, 11],
    #            '11001000001001001001010101000011': [13, 2, 3, 2, 11, 2, 1621, 2, 3],
    #            '11100000000001010010000001001011': [3, 2, 5, 2, 5, 2, 3, 2, 7],
    #            '10010011000000010010100000000111': [3, 2, 5, 2, 5, 2, 3, 2, 11],
    #            '10001110010100100100000010010011': [3, 2, 3, 2, 7, 2, 3, 2, 3],
    #            '10010011010000101000111000000001': [41, 7, 7, 149, 79, 733, 89, 3559, 7],
    #            '10000000010000110000101001110101': [109, 19, 13, 197, 73, 29, 37, 227, 103],
    #            '11001000000110010011010101111001': [3, 11, 3, 3, 5, 3, 3, 104107, 3],
    #            '10000000110000000001010000000001': [1361, 2, 3, 2, 79098425801, 2, 523, 2, 3],
    #            '11110000001011001000000001000101': [12073, 5, 11, 7, 11, 29, 5, 13, 63857],
    #            '10100011111100111001101110000001': [3, 5, 43, 3, 79, 5, 3, 11, 7109],
    #            '10001010110011000001010010000011': [11, 2, 3, 2, 130841, 2, 5, 2, 3],
    #            '10001101100001011000000000100111': [3, 2, 3, 2, 7, 2, 3, 2, 3],
    #            '11111011100100011010000001000111': [3, 2, 5, 2, 7, 2, 3, 2, 11],
    #            '10000000001000101000110100010101': [3, 2, 5, 2, 5, 2, 3, 2, 11]}

    answers = {}
    while len(answers) < 500:
        t = generate_test(0.3, 32)
        while t in answers:
            t = generate_test(0.3, 32)
        # ans = solve(t)
        ans = solve_naive(t)
        if ans is not None:
            answers[t] = ans

    print('Case #1:')
    for k, v in answers.items():
        print(k, ' '.join(map(str, v)))


def main():
    brute_large()


if __name__ == "__main__":
    main()