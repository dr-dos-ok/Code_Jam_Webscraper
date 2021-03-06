PK     }Y�D���eQ
  Q
     launcher.py#!/usr/bin/env python3

### README:
# This is the wrapper around the solution. The actual solution is in "*.lp" file.
# The solution is written in AnsProlog, the language for answer set programming technique.
# The wrapper splits the input file into T independent testcases, launches T independent ASP solvers, and collects the results.
# 
# To launch the solution, you need to have Potassco ASP toolkit in your PATH.
# Link: http://potassco.sourceforge.net/
# You need the 'clingo' tool, version 4.3.0+. It should be built with Python scripting support (Linux version is built with it by
# default, Windows and OSX versions aren't). This tool should be available in your PATH by the name 'clingo4'.
#
# Launch this launcher as:
# launcher.py PROBLEMNAME TESTCATEGORY < INPUTFILE
# For example: launcher.py MagicTrick small < A-small.in

import sys
import os
import shutil
import subprocess
from zipfile import ZipFile

# Reads the test input from the input stream, and dumps it into filename.lp.
# The only part of the launcher that has to be modified per problem.
def dump_test(inf, filename):
    R, C, M = inf.readline().split()
    with open(filename + ".lp", 'w+t') as f:
        f.write('#const row_count = {0}.\n#const col_count = {1}.\n#const mine_count = {2}.\n'.format(R, C, M))

def dump_result(outf, test, result, filename):
    with open(filename, 'w+t') as f:
        f.write(result)
    outf.write("Case #{0}:\n{1}\n".format(test, result))
    

problem_name = sys.argv[1]
size = sys.argv[2]
problem = "{0}-{1}".format(problem_name, size)
path = os.path.join(os.getcwd(), problem + "-data")
shutil.rmtree(path, ignore_errors = True)
os.mkdir(path)

with sys.stdin as inf:
    test_count = int(inf.readline())
    for test in range(1, test_count + 1):
        dump_test(inf, os.path.join(path, "{0}.{1}".format(problem, test)))

with open("{0}.out.txt".format(problem), 'w+t') as outf:
    for test in range(1, test_count + 1):
        instance_file = os.path.join(path, "{0}.{1}.lp".format(problem, test))
        encoding_file = problem_name + ".lp"
        try:
            result = subprocess.check_output('clingo4 --outf=3 {0} "{1}"'.format(encoding_file, instance_file), shell=True)
        except subprocess.CalledProcessError as e:
            result = e.output
        result = result.decode('utf-8').strip()
        dump_result(outf, test, result, os.path.join(path, "{0}.{1}.out".format(problem, test)))

with ZipFile("{0}.zip".format(problem), 'w') as zipf:
    zipf.write("launcher.py")
    zipf.write(encoding_file)
    zipf.write("../common.py.lp")
PK     |
�D�[k��  �     MinesweeperMaster.lp#include "../common.py.lp".

#script(python)
import sys
from gringo import SolveResult

def on_model(model, row_count, col_count):
    mines = { t.args()[0] for t in terms(model, 'mine') }
    click = terms(model, 'click')[0].args()[0]
    for row in xrange(1, row_count + 1):
        print ''.join('*' if (row, col) in mines else ('c' if (row, col) == click else '.') for col in xrange(1, col_count + 1))

def main(prg):
    row_count = prg.getConst('row_count')
    col_count = prg.getConst('col_count')
    prg.ground('base', [])
    result = prg.solve(lambda m: on_model(m, row_count, col_count))
    if result == SolveResult.UNSAT:
        print 'Impossible'

#end.

cell((Row, Col)) :- Row = 1..row_count, Col = 1..col_count.
mine_count { mine(Cell): cell(Cell) } mine_count.
hint((Row, Col), S) :- cell((Row, Col)), not mine(cell), S = #count { AR,AC: AR = Row + (-1..1), AC = Col + (-1..1), mine((AR,AC)) }.

1 { click(Cell): cell(Cell), not mine(Cell) } 1.
open(Cell) :- click(Cell).
open((AR, AC)) :- open(Cell), hint(Cell, 0), Cell = (R, C), AR = R + (-1..1), AC = C + (-1..1).

bad :- cell(Cell), not mine(Cell), not open(Cell).
:- bad.
PK     ��D#4{*�  �     ../common.py.lp#script (python)

from gringo import Fun, Model

NULL = Fun('__null', [])

def terms(model, name):
    return [t for t in model.atoms(Model.ATOMS) if t.name() == name]

def arity(term):
    if isinstance(term, tuple): return len(term)
    if isinstance(term, Fun): return len(term.args())
    return 0

def nth(term, n):
    if isinstance(term, tuple): return term[n-1]
    if isinstance(term, Fun): return term.args()[n - 1]
    return NULL

#end.
PK     }Y�D���eQ
  Q
             �    launcher.pyPK     |
�D�[k��  �             �z
  MinesweeperMaster.lpPK     ��D#4{*�  �             �I  ../common.py.lpPK      �   K    