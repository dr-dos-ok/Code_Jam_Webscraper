PK     (�I��C#F  F     codejam_io.pyfrom __future__ import print_function
""" Some basic tools for command-line processing of Google Code Jam. """
import os
import sys
import inspect
import subprocess
import zipfile

class MultiOutput(object):
    """ A simple class to duplicate output into multiple output files.

    Makes an object that allows you to write to multiple files as though
    they were a single file (via the write() method, which is sufficient
    to also work for the print() function).

    You can also provide sys.stdout among those files, but it
    it will not be closed when the MultiOutput is closed.
    """
    def __init__(self, files):
        """ Creates the wrapper. """
        self._files = list(files)

    def close(self):
        """ Closes all wrapped files, except sys.stdout. """
        for f in self._files:
            if f != sys.stdout:
                f.close()

    def write(self, data):
        """ Writes the given data to all wrapped files. """
        for f in self._files:
            f.write(data)
            # Automatically flush stdout
            if f == sys.stdout:
                f.flush()

def process_input(pfun, p0=lambda f:(int(f.readline()), None),
        module_path=None, argv=None):
    """ Processes a single Code Jam input file with some command-line tools.

    The arguments are two functions; - the first (pfun) takes
    four arguments - the input file, the output file, the current case
    number, and any other case data (this is often None).

    The second only requires the input file, and should parse the file for
    the number of cases and any additional data that is needed; this
    data is passed onto pfun via its fourth argument.

    The command-line options are simple - a single input file is expected,
    defaulting to test.in if no file is given. By default, the output
    simply goes to stdout, but this is modified by two options:
        -d    Outputs to a file, which is named by replacing ".in" with ".out"
                on the end of the input filename, or by simply appending
                ".out" afterwards.
        -c    If -d was selected, the output will be copied to stdout as well
                as to the file.
        -n    Don't update the source code archive.
    """
    if not argv:
        argv = sys.argv[1:]

    options = set()
    for arg in argv:
        if arg.startswith("-"):
            argv.remove(arg)
            options.update(arg[1:])
    filename = argv[0] if argv else 'test.in'

    targets = []
    if "d" in options:
        root, ext = os.path.splitext(filename)
        if ext == '.out':
            root += '.out'
        targets.append(open(root + '.out', 'w'))
    if not targets or "c" in options:
        targets.append(sys.stdout)
    if "n" in options:
        module_path = None
    f_out = MultiOutput(targets)

    with open(filename) as f_in:
        num_cases, other_data = p0(f_in)
        for case_no in range(1, num_cases+1):
            pfun(f_in, f_out, case_no, other_data)
    f_out.close()

    if module_path is not None:
        make_archive(module_path)

def make_archive(module_path):
    paths = set()
    target = os.path.join(os.path.split(module_path)[0], "src.zip")
    paths.add(os.path.realpath(module_path))
    for module_name in sys.modules:
        try:
            path = inspect.getsourcefile(sys.modules[module_name])
            if path.startswith(os.environ['GOOGLE_DRIVE']):
                paths.add(path)
        except (TypeError, AttributeError):
            pass
    print(file=sys.stderr)
    try:
        os.remove(target)
        print("Deleted {} - remaking".format(target), file=sys.stderr)
    except OSError:
        pass

    archive = zipfile.ZipFile(target, 'w')
    for path in paths:
        filename = os.path.basename(path)
        archive.write(path, filename)
        print("Added {}".format(filename), file=sys.stderr)
    archive.close()
PK     ��J+*֋�  �     pony.py#! /usr/bin/env python
from __future__ import print_function, division
try:
    range = xrange
except NameError:
    pass

# import collections
# import functools
# import itertools as it
import numpy as np # See http://www.numpy.org
# import sympy as sp # See http://sympy.org/en/index.html
import gmpy2 # See https://code.google.com/p/gmpy/
# import networkx as nx # See http://networkx.github.io/

import os
import sys
# MY MODULES - available at https://github.com/lackofcheese/CodeJamLib/
sys.path.append(os.path.join(
    os.environ['GOOGLE_DRIVE'], 'Coding', 'GCJ', 'CodeJamLib'))
import codejam_io

def toks_line(f_in, fun=int):
    return [fun(k) for k in f_in.readline().split()]

def process_first(f_in):
    num_cases = int(f_in.readline())
    other_data = None
    return num_cases, other_data

def process_case(f_in, f_out, case_no, other_data=None):
    N, Q = toks_line(f_in)

    horses = []
    for i in range(N):
        E, S = toks_line(f_in)
        horses.append((E, S))

    dists = []
    for i in range(N):
        Ds = toks_line(f_in)
        dists.append(Ds)

    pairs = []
    for i in range(Q):
        U, V = toks_line(f_in)
        pairs.append((U-1, V-1))

    times = solve(N, Q, horses, dists, pairs)
    print("Case #{}: ".format(case_no), file=f_out, end='')
    for t in times:
        print("{:.10f} ".format(t), file=f_out, end='')
    print("", file=f_out)

def solve(N, Q, horses, dists, pairs):
    dists = np.array(dists, dtype=object)
    for i in range(N):
        dists[i, i] = gmpy2.mpz(0)
    for i in range(N):
        for j in range(N):
            d = dists[i, j]
            if d == -1:
                dists[i,j] = np.inf
            else:
                dists[i,j] = gmpy2.mpz(d)
    # print(dists.astype('float'))
    for k in range(N):
        for i in range(N):
            for j in range(N):
                other = dists[i,k] + dists[k,j]
                if dists[i,j] > other:
                    dists[i,j] = other
    # print(dists.astype('float'))


    times = np.ones((N, N)) * np.inf
    for i in range(N):
        times[i, i] = 0
    for start in range(N):
        E, S = horses[start]
        for end in range(N):
            d = dists[start, end]
            if d <= E:
                times[start, end] = d / S
    for k in range(N):
        for i in range(N):
            for j in range(N):
                other = times[i,k] + times[k,j]
                if times[i,j] > other:
                    times[i,j] = other
    # print(times)

    pair_times = []
    for U, V in pairs:
        pair_times.append(times[U, V])
    return pair_times

def solve_small(N, Q, horses, dists, pairs):
    # print(N, Q, horses, dists, pairs)
    dists2 = []
    for i in range(N-1):
        dists2.append(gmpy2.mpz(dists[i][i+1]))

    pair_dists = np.zeros((N, N), dtype=object)
    for i in range(N):
        pair_dists[i, i] = gmpy2.mpz(0)
        for j in range(i+1, N):
            pair_dists[i, j] = pair_dists[i, j-1] + dists2[j-1]
    # print(pair_dists)

    fastest_times = np.ones(N) * np.inf
    fastest_times[N-1] = 0
    for start in range(N-2, -1, -1):
        best_time = np.inf
        E, S = horses[start]
        for end in range(start+1, N):
            dist = pair_dists[start, end]
            # print(start, end, dist)
            if dist > E:
                continue
            time = (dist / S) + fastest_times[end]
            if time < best_time:
                best_time = time
        fastest_times[start] = best_time
    # print(fastest_times)
    return [fastest_times[0]]

if __name__ == '__main__':
    codejam_io.process_input(process_case, process_first, __file__)
PK      (�I��C#F  F             ��    codejam_io.pyPK      ��J+*֋�  �             ��q  pony.pyPK      p   e    