PK     D0�D��C#F  F     codejam_io.pyfrom __future__ import print_function
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
PK     � �Ha�~�\  \  	   babble.py#! /usr/bin/env python
from __future__ import print_function, division
try:
    range = xrange
except NameError:
    pass

import collections
# import functools
import itertools as it
# import numpy as np # See http://www.numpy.org
# import sympy as sp # See http://sympy.org/en/index.html
# import gmpy2 # See https://code.google.com/p/gmpy/
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
    N = int(f_in.readline())
    topics = []
    for i in range(N):
        topics.append(f_in.readline().strip().split())
    ans = solve(topics)
    print("Case #{}: {}".format(case_no, ans), file=f_out)

def solve(topics):
    N = len(topics)
    
    max_fakes = 0

    fsts = set()
    secs = set()
    for i, topic in enumerate(topics):
        fw, sw = topic
        fsts.add(fw)
        secs.add(sw)
    for is_real in it.product([True, False], repeat=N):
        # print(is_real)
        fsts2 = set(fsts)
        secs2 = set(secs)
        n_fakes = 0
        for i, topic in enumerate(topics):
            if is_real[i]:
                fw, sw = topic
                fsts2.discard(fw)
                secs2.discard(sw)
            else:
                n_fakes += 1
        if not fsts2 and not secs2:
            if n_fakes > max_fakes:
                max_fakes = n_fakes
    return max_fakes

def solve2(topics):
    N = len(topics)
    fsts = collections.defaultdict(set)
    secs = collections.defaultdict(set)
    fakes = set(range(N))
    for i, topic in enumerate(topics):
        fw, sw = topic
        fsts[fw].add(i)
        secs[sw].add(i)
    # print(fsts)
    # print(secs)
    # print()
    inf = float('inf')
    while True:
        best = (inf, inf)
        to_remove = None
        for fake in fakes:
            fw, sw = topics[fake]
            if fw not in fsts:
                count0 = inf
            else:
                count0 = len(fsts[fw])
            if sw not in secs:
                count1 = inf
            else:
                count1 = len(secs[sw])
            c0 = min(count0, count1)
            c1 = max(count0, count1)
            counts = (c0, c1)
            # print(fw, sw, counts)
            if counts < best:
                best = counts
                to_remove = fake
        if to_remove is None:
            break
        fw, sw = topics[to_remove]
        # print(fw, sw)
        if fw in fsts:
            del fsts[fw]
        if sw in secs:
            del secs[sw]
        fakes.remove(to_remove)
    return len(fakes)

if __name__ == '__main__':
    codejam_io.process_input(process_case, process_first, __file__)

PK      D0�D��C#F  F             ��    codejam_io.pyPK      � �Ha�~�\  \  	           ��q  babble.pyPK      r   �    