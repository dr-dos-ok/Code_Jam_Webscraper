#!/bin/env python

input_file = None

import glob
import os
import sys

def main():
    cases = readone(int)
    output = []
    for case_num in range(1, cases + 1):
        result = None
        ### Begin solution code
        cakes = readone(str)
        while '++' in cakes:
            cakes = cakes.replace('++', '+')
        while '--' in cakes:
            cakes = cakes.replace('--', '-')
        if cakes[-1] == '+':
            cakes = cakes[:-1]
        result = len(cakes)
        ### End solution code
        output.append('Case #%d: ' % (case_num,) + str(result))
    output_file = open(output_filename, 'w')
    output_file.write('\n'.join(output))
    output_file.close()
    print '\n'.join(output)

def readone(t):
    line = input_file.readline()
    assert(len(line.split()) == 1)
    return t(line.strip())

def readmany(t):
    return map(t, input_file.readline().split())

if __name__ == '__main__':
    input_file = sys.stdin
    problem = os.path.split(__file__)[1][0].upper()
    output_filename = 'test.out'
    inputs = glob.glob(os.path.expanduser('~') + '/Downloads/' + problem + '-*.in')
    newest = max(inputs, key=os.path.getctime)
    input_filename = os.path.split(newest)[1]
    output_filename = problem + '-' + input_filename.split('-')[1][:-3] + '.out'
    input_file = open(newest)
    
    main()
    input_file.close()