from sys import *
from heapq import *
from time import time
from multiprocessing import Pool
from collections import *
import itertools
from copy import deepcopy
from bisect import *
setrecursionlimit(10000)
from math import *
from time import sleep
import os
import sys
import re
import numpy as np
import heapq

# dp = np.zeros((A, B)), np.int32)

def readint():
    return int(fi.readline())

def readints():
    return [int(X) for X in fi.readline().split()]

def readfloats():
    return [float(X) for X in fi.readline().split()]

def readstr():
    return fi.readline().rstrip()

def read_case():
    N = readint()
    S = readints()
    return (N, S)

def cd(lst):
    rv = merge_count_inversion(lst)[1]
    return rv

def merge_count_inversion(lst):
    if len(lst) <= 1:
        return lst, 0
    middle = int( len(lst) / 2 )
    left, a = merge_count_inversion(lst[:middle])
    right, b = merge_count_inversion(lst[middle:])
    result, c = merge_count_split_inversion(left, right)
    return result, (a + b + c)

def merge_count_split_inversion(left, right):
    result = []
    count = 0
    i, j = 0, 0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += left_len - i
            j += 1
    result += left[i:]
    result += right[j:]
    return result, count        

def solve_case(N, S):
    swaps = 0
    SS = sorted(S)
    for X in SS:
        idx = S.index(X)
        S.remove(X)
        swaps += min(idx, len(S)-idx)
    return swaps
    
def print_solution(case):
    val = solve_case(*case[1])
    msg = "Case #{}: {}".format(case[0], val)
    print msg
    return msg

t0 = time()
# Initialisation here
t1 = time()
print "Intialisation took %f seconds" % (t1 - t0)

if __name__ == '__main__':
    fni = "%s-%s-%s.in" % (argv[1], argv[2], argv[3])
    fno = "%s-%s-%s.out" % (argv[1], argv[2], argv[3])

    if not os.path.isfile(fni):
        sys.stdout.write('Waiting for input file {}...'.format(fni))
        while not os.path.isfile(fni):
            sys.stdout.flush()
            sleep(1)
            sys.stdout.write(".")
        sleep(1)
        print ''
    fi = open(fni, 'r')

    numcases = readint()
    cases = [(I, read_case()) for I in range(1,1+numcases)]

    mt = False
    if mt:
        print "Running multi-threaded"
        p = Pool(8)
        output = p.map(print_solution, cases)
    else:
        print "Running single-threaded"
        output = map(print_solution, cases)
    print "Elapsed time %f seconds " % (time() - t1)

    if os.path.isfile(fno):
        print 'Verifying against existing results'
        fo = open(fno, 'r')
        oc = re.split('(Case #[0-9]+:\s*)', fo.read())[1:]
        refout = [(A+B).rstrip() for (A,B) in zip(oc[::2], oc[1::2])]
        diffs = 0
        for C in range(numcases):
           if refout[C] != output[C]:
               print '-'*20
               print 'Input {}\nReference Output {}\nGenerated Output {}'.format(cases[C][1], refout[C], output[C])
               print '-'*20
               diffs += 1
        print '{} diffs found'.format(diffs)
    else:
        fo = open(fno, 'w')
        fo.write('\n'.join(output))
        print '{} cases written'.format(len(output))

