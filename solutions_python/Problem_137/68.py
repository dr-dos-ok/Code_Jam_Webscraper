PK     笌D�k��  �     codejam_io.pyfrom __future__ import print_function
""" Some basic tools for command-line processing of Google Code Jam. """
import os
import sys
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
            path = sys.modules[module_name].__file__
            if path.startswith(os.environ['GOOGLE_DRIVE']):
                paths.add(path)
        except AttributeError:
            pass
    try:
        os.remove(target)
        print("Deleted {} - remaking".format(target))
    except OSError:
        pass

    archive = zipfile.ZipFile(target, 'w')
    for path in paths:
        filename = os.path.basename(path)
        archive.write(path, filename)
        print("Added {}".format(filename))
    archive.close()
PK     묌D�e��  �     minesweeper_master.py#! /usr/bin/env python
from __future__ import print_function, division
try:
    range = xrange
except NameError:
    pass
import collections
import functools
import itertools as it
import numpy as np # See http://www.numpy.org/
import gmpy2 # See https://code.google.com/p/gmpy/
#import networkx as nx # See http://networkx.github.io/

import os
import sys
# MY MODULES - available at https://github.com/lackofcheese/CodeJamLib/
sys.path.append(os.path.join(
    os.environ['GOOGLE_DRIVE'], 'Coding', 'GCJ', 'CodeJamLib'))
import codejam_io

def toks_line(f_in, fun=lambda x: x):
    return [fun(k) for k in f_in.readline().strip().split()]

def process_first(f_in):
    num_cases = int(f_in.readline())
    other_data = None
    return num_cases, other_data

def process_case(f_in, f_out, case_no, other_data=None):
    R, C, num_mines = (int(v) for v in f_in.readline().split())
    solution = solve(R, C, num_mines)
    print("Case #{}:".format(case_no), file=f_out)
    if solution is None:
        print("Impossible".format(case_no), file=f_out)
    else:
        for row in solution:
            print("".join(list(row)), file=f_out)

def solve(R, C, num_mines):
    if R < C:
        solution = solve(C, R, num_mines)
        if solution is None:
            return None
        else:
            return np.transpose(solution)

    numbers = solve_numbers(R, C, num_mines)
    if numbers is None:
        return None
    grid = np.tile('*', (R, C))
    #print(numbers)
    #print(grid)
    for i in range(len(numbers)):
        num_empty = numbers[i]
        grid[:num_empty,i] = '.'
    grid[0,0] = 'c'
    return grid

def solve_numbers(R, C, num_mines):
    if num_mines == 0:
        return [R] * C
    num_cells = R * C
    num_empty = num_cells - num_mines
    if num_empty == 1:
        return [1]
    if C == 1:
        return [num_empty]

    if num_empty < 4:
        return None
    if C == 2:
        if num_empty % 2 != 0:
            return None
        else:
            return [num_empty / 2] * 2

    max_height = num_empty // 2
    if max_height <= 1:
        return None
    if max_height > R:
        max_height = R

    num_max_cols = num_empty // max_height
    num_left = num_empty - num_max_cols * max_height

    if num_left == 0:
        return [max_height] * num_max_cols

    if num_max_cols >= C:
        print("WTF ERROR!?")
        return None

    if num_left > 1:
        return [max_height] * num_max_cols + [num_left]


    # There was only one unit left, so we reorganize.
    if max_height == 2:
        return None
    if max_height == 3:
        if num_max_cols == 2:
            return None
    if num_max_cols > 2:
        return [max_height] * (num_max_cols - 1) + [max_height - 1, 2]
    else:
        return [max_height-1, max_height-1, 3]

if __name__ == '__main__':
    codejam_io.process_input(process_case, process_first, __file__)
PK      笌D�k��  �             ��    codejam_io.pyPK      묌D�e��  �             ���  minesweeper_master.pyPK      ~   �    