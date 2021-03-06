#!/usr/bin/python2
### Google Code Jam template
# Futures
from __future__ import division
from __future__ import with_statement
from __future__ import print_function
## Library
# @memoized
def memoized(func):
    mem = {}
    def wrapped(*args):
        if args not in mem:
            mem[args] = func(*args)
        return mem[args]
    return wrapped

## Input templates
# Line as int
readint = lambda infile: int(infile.readline())
# Line as many ints
readints = lambda infile: [int(s) for s in infile.readline().split()]

# Base class
class ProblemSolver(object):
    def __init__(self):
        self.precalculate()

    def precalculate(self):
        raise NotImplementedError

    def process(self, infile, ncase):
        raise NotImplementedError

    def run(self, infile, outfile):
        cases = int(infile.readline())
        for ncase in range(cases):
            print("Case #{nc}".format(nc=ncase + 1))
            # Perform all nessesary calculation
            data = self.process(infile, ncase=ncase)
            outfile.write("Case #{nc}: {data}\n".format(
                    nc=ncase + 1,data=data))

# Working class
class Solver(ProblemSolver):
    def precalculate(self):
        ## User code here
        pass

    def process(self, infile, ncase):
        ## User code here
        N = readint(infile)
        vines = [readints(infile) for i in range(N)]
        self.distance = readint(infile)
        self.position, self.length = zip(*vines)
        self.lowest = [0] * N
        return "YES" if self.swing(0, self.position[0]) else "NO"

    def swing(self, start, length):
        if start + length >= self.distance:
            return True
        for num, pos in enumerate(self.position):
            if not pos > start:
                continue
            if pos > start + length:
                break
            if self.lowest[num] < min(self.length[num], pos - start):
                self.lowest[num] = min(self.length[num], pos - start)
                if self.swing(pos, self.lowest[num]):
                    return True
        return False

# Script code
if __name__ == '__main__':
    ## Setup
    # Task letter
    from os.path import basename, splitext
    TASK = splitext(basename(__file__))[0]
    print("Task {}".format(TASK))
    from sys import argv
    if len(argv) > 1:
        print("Filename given: {}".format(argv[1]))
        FILE = splitext(argv[1])[0]
    else:
        FILE = TASK
    ## Precalculation
    print("Initialization...")
    solver = Solver()
    print("Initialization done.")
    ## Calculation
    print("Calculation...")
    with open(FILE + ".in") as infile:
        with open(FILE + ".out",mode="wt") as outfile:
            solver.run(infile, outfile)
    print("Calculation done.")
