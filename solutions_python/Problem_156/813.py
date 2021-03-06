from multiprocessing import Pool, Manager
from copy import deepcopy
from itertools import *
import math

def minsToGetToN(p, n):
    if p <= n:
        return 0

    half_pile = n
    other_half = p - half_pile

    return 1 + minsToGetToN(half_pile, n) + minsToGetToN(other_half, n)

def solve(solve_input):
    D, P = solve_input

    min_minutes = max(P)

    for i in xrange(2, 10):
        total_minutes = sum(map(lambda p: minsToGetToN(p, i), P)) + i
        if total_minutes < min_minutes:
            min_minutes = total_minutes

    return min_minutes


def solve_file(filename, use_threadpool):
    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')
    #data read
    inputs = []
    T = int(fin.readline())
    for case in xrange(T):
        D = int(fin.readline().strip())
        P = map(int, fin.readline().strip().split(' '))
        inputs.append((D, P))
    #solve
    answers = []
    if use_threadpool:
        thread_pool = Pool(10)
        answers = thread_pool.map(solve, inputs)
    else:
        answers = map(solve, inputs)
    #output
    for i in xrange(1, len(answers) + 1):
        fout.write(("Case #%d: " % i) + str(answers[i-1]) + "\n")

    fin.close()
    fout.close()

if __name__ == "__main__":
    solve_file("B-small-attempt2", False)
