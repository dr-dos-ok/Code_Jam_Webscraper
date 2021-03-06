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
PK     K��F�UA�  �     dijkstra.py#! /usr/bin/env python
from __future__ import print_function, division
try:
    range = xrange
except NameError:
    pass

# import collections
# import functools
# import itertools as it
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

PRODUCTS = {
    "1":{"1":"1", "i":"i",  "j":"j",  "k":"k" },
    "i":{"1":"i", "i":"-1", "j":"k",  "k":"-j"},
    "j":{"1":"j", "i":"-k", "j":"-1", "k":"i" },
    "k":{"1":"k", "i":"j",  "j":"-i", "k":"-1"}
}

def neg(q):
    if "-" in q:
        return q[1]
    else:
        return "-" + q

for t1 in ["1", "i", "j", "k"]:
    PRODUCTS[neg(t1)] = {}
    for t2 in ["1", "i", "j", "k"]:
        prod = PRODUCTS[t1][t2]
        nprod = neg(prod)
        PRODUCTS[t1][neg(t2)] = nprod
        PRODUCTS[neg(t1)][t2] = nprod
        PRODUCTS[neg(t1)][neg(t2)] = prod

def multiply(q1, q2):
    return PRODUCTS[q1][q2]

def inv(q):
    if q == "1":
        return "1"
    elif q == "-1":
        return "-1"
    else:
        return neg(q)

def toks_line(f_in, fun=int):
    return [fun(k) for k in f_in.readline().split()]

def process_first(f_in):
    num_cases = int(f_in.readline())
    other_data = None
    return num_cases, other_data

def process_case(f_in, f_out, case_no, other_data=None):
    L, X = toks_line(f_in)
    string = f_in.readline().strip()
    ans = solve(string, X)
    print("Case #{}: {}".format(case_no, ans), file=f_out)

def solve(string, X):
    if X % 4 == 0:
        return "NO"
    L = len(string)
    if L == 1:
        return "NO"
    if L * X < 3:
        return "NO"

    string_product = "1"
    for c in string:
        string_product = multiply(string_product, c)

    # Check that the overall product is -1
    if string_product == "1":
        return "NO"
    elif string_product == "-1":
        if X % 2 == 0:
            return "NO"
        cycle = {"1":0, "-1":1}
    else:
        if X % 2 != 0:
            return "NO"
        cycle = {"1":0, "-1": 2, string_product:1, neg(string_product):3}

    earliest = {"1":0}
    latest =   {string_product:L}

    product = "1"
    for i, c in enumerate(string):
        product = multiply(product, c)
        r_product = multiply(inv(product), string_product)
        if product not in earliest:
            earliest[product] = i + 1
        latest[r_product] = L - i - 1

    earliest_i = float("inf")
    for q, idx in earliest.items():
        rem = multiply("i", inv(q))
        if rem not in cycle:
            continue
        idx2 = L * cycle[rem] + idx
        if idx2 < earliest_i:
            earliest_i = idx2

    latest_k = float("inf")
    for q, idx in latest.items():
        rem = multiply(inv(q), "k")
        if rem not in cycle:
            continue
        idx2 = L * cycle[rem] + idx
        if idx2 < latest_k:
            latest_k = idx2

    if earliest_i + latest_k <= L * X:
        return "YES"
    return "NO"

if __name__ == '__main__':
    codejam_io.process_input(process_case, process_first, __file__)
PK      D0�D��C#F  F             ��    codejam_io.pyPK      K��F�UA�  �             ��q  dijkstra.pyPK      t   "    