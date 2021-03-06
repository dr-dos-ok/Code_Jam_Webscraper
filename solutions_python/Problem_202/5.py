PK     n�Jy����  �  
   fashion.py#! /usr/bin/env python
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
# import gmpy2 # See https://code.google.com/p/gmpy/
# import networkx as nx # See http://networkx.github.io/
import collections

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
    N, M = toks_line(f_in)
    models = []
    for i in range(M):
        model, row, col = f_in.readline().split()
        models.append((model, int(row), int(col)))
    grid = np.zeros((N, N), dtype='|S1')
    grid.fill('.')
    for m, r, c in models:
        grid[r-1,c-1] = m

    orig_grid = grid.copy()
    solve(N, grid)
    value = get_value(grid)
    diff = grid_diff(N, orig_grid, grid)
    # print("-------")
    # print_grid(orig_grid)
    # print("-------")
    # print_grid(grid)
    # print("-------")
    if not is_legal(N, grid):
        print("ILLEGAL", file=sys.stderr)
        print_grid(grid)
        sys.exit(100)
    print("Case #{}: {} {}".format(case_no, value, len(diff)), file=f_out)
    for m, r, c in diff:
        print("{} {} {}".format(m, r, c), file=f_out)

def is_legal(N, grid):
    for row in range(N):
        if np.count_nonzero((grid[row, :] != b'+') & (grid[row, :] != b'.')) > 1:
            return False
    for col in range(N):
        if np.count_nonzero((grid[:, col] != b'+') & (grid[:, col] != b'.')) > 1:
            return False
    for offset in range(-(N-1), N):
        d = np.diagonal(grid, offset)
        if np.count_nonzero((d != b'x') & (d != b'.')) > 1:
            return False
    for offset in range(-(N-1), N):
        d = np.diagonal(np.fliplr(grid), offset)
        if np.count_nonzero((d != b'x') & (d != b'.')) > 1:
            return False
    return True

def get_value(grid):
    value = 0
    for row in grid:
        for cell in row:
            if cell == b'+' or cell == b'x':
                value += 1
            elif cell == b'o':
                value += 2
    return value

def grid_diff(N, orig_grid, grid):
    diff = []
    for i in range(N):
        for j in range(N):
            if grid[i, j] != orig_grid[i, j]:
                diff.append((grid[i, j].decode('UTF-8'), i+1, j+1))
    return diff

def print_grid(grid):
    for row in grid:
        print(row.tostring().decode('UTF-8'))
        # print(''.join(str(c) for c in row))

def solve(N, grid):
    # Find the horizontal/vertical slack
    slack_rows = []
    slack_cols = []
    for row in range(N):
        if not np.any((grid[row, :] != b'+') & (grid[row, :] != b'.')):
            slack_rows.append(row)
    for col in range(N):
        if not np.any((grid[:, col] != b'+') & (grid[:, col] != b'.')):
            slack_cols.append(col)
    # Allocate the slack (it doesn't matter how!)
    for index in range(min(len(slack_rows), len(slack_cols))):
        row = slack_rows[index]
        col = slack_cols[index]
        v = grid[row, col]
        if v == b'+':
            grid[row, col] = b'o'
        else:
            grid[row, col] = b'x'

    # Find the diagonal / antidiagonal slack
    is_slack_diag = np.zeros(2*N-1, dtype=bool)
    is_slack_adiag = np.zeros(2*N-1, dtype=bool)
    for offset in range(-(N-1), N):
        d = np.diagonal(grid, offset)
        is_slack_diag[offset+N-1] = not np.any((d != b'x') & (d != b'.'))
    for offset in range(-(N-1), N):
        d = np.diagonal(np.flipud(grid), offset)
        is_slack_adiag[offset+N-1] = not np.any((d != b'x') & (d != b'.'))

    # Represent the slack via a bipartite graph.
    diagonals = set()
    anti_diagonals = set()
    slack_ad_per_diagonal = collections.defaultdict(list)
    for i in range(N):
        for j in range(N):
            d_ind = j - i + N - 1
            ad_ind = i + j
            if is_slack_diag[d_ind] and is_slack_adiag[ad_ind]:
                diagonals.add(d_ind)
                anti_diagonals.add(ad_ind)
                slack_ad_per_diagonal[d_ind].append(ad_ind)
    match = HopcroftKarp(diagonals, anti_diagonals, slack_ad_per_diagonal)
    # Allocate the slack according to the matching we found.
    for d_ind, ad_ind in match.items():
        if ad_ind is not None:
            row = ((N-1) - (d_ind - ad_ind)) // 2
            col = ((d_ind + ad_ind) - (N-1)) // 2
            v = grid[row, col]
            if v == b'x':
                grid[row, col] = b'o'
            else:
                grid[row, col] = b'+'

# Hopcroft-Karp algorithm based on pseudocode from Wikipedia.
def BFS(U, V, Adj, Pair_U, Pair_V, Dist):
    queue = collections.deque()
    for u in U:
        if Pair_U[u] is None:
            Dist[u] = 0
            queue.append(u)
        else:
            Dist[u] = np.inf
    Dist[None] = np.inf
    while queue:
        u = queue.popleft()
        if Dist[u] < Dist[None]:
            for v in Adj[u]:
                u2 = Pair_V[v]
                if Dist[u2] == np.inf:
                    Dist[u2] = Dist[u] + 1
                    queue.append(u2)
    return Dist[None] != np.inf

def DFS(u, U, V, Adj, Pair_U, Pair_V, Dist):
    if u is None:
        return True
    for v in Adj[u]:
        u2 = Pair_V[v]
        if Dist[u2] == Dist[u] + 1:
            if DFS(u2, U, V, Adj, Pair_U, Pair_V, Dist):
                Pair_V[v] = u
                Pair_U[u] = v
                return True
    Dist[u] = np.inf
    return False

def HopcroftKarp(U, V, Adj):
    Pair_U = dict()
    Pair_V = dict()
    Dist = dict()
    for u in U:
        Pair_U[u] = None
    for v in V:
        Pair_V[v] = None
    matching = 0
    distances = dict()
    while BFS(U, V, Adj, Pair_U, Pair_V, Dist):
        for u in U:
            if Pair_U[u] is None:
                if DFS(u, U, V, Adj, Pair_U, Pair_V, Dist):
                    matching += 1
    return Pair_U 

if __name__ == '__main__':
    codejam_io.process_input(process_case, process_first, __file__)
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
PK      n�Jy����  �  
           ��    fashion.pyPK      (�I��C#F  F             ��  codejam_io.pyPK      s   y)    