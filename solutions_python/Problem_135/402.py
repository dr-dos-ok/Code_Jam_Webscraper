PK     ���Dj�r
(  (     launcher.py#!/usr/bin/env python3

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
    first_answer = int(inf.readline())
    first_cards = [0] * 4
    for i in range(4): first_cards[i] = inf.readline().split()
    second_answer = int(inf.readline())
    second_cards = [0] * 4
    for i in range(4): second_cards[i] = inf.readline().split()
    with open(filename + ".lp", 'w+t') as f:
        f.write('answer(first, {0}).\nanswer(second, {1}).\n'.format(first_answer, second_answer))
        for i, row in enumerate(first_cards):
            f.write('row(first, {0}, ({1})).\n'.format(i + 1, ", ".join(row)))
        for i, row in enumerate(second_cards):
            f.write('row(second, {0}, ({1})).\n'.format(i + 1, ", ".join(row)))


def dump_result(outf, test, result, filename):
    with open(filename, 'w+t') as f:
        f.write(result)
    outf.write("Case #{0}: {1}\n".format(test, result))
    

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
PK     ׎�D=6\��  �     MagicTrick.lp#include "../common.py.lp".

#script (python)
from gringo import Model

def terms(model, name):
    return [t for t in model.atoms(Model.ATOMS) if t.name() == name]

def on_model(model):
    cands = terms(model, 'candidate')
    if len(cands) == 1:
        print cands[0].args()[0]
    elif len(cands) == 0:
        print 'Volunteer cheated!'
    else:
        print 'Bad magician!'

def main(prg):
    prg.ground('base', [])
    prg.solve(on_model)

#end.

in_row(Case, Row, @nth(Data, K)) :- row(Case, Row, Data), K = 1..@arity(Data).
candidate(N) :- in_row(first, Row1, N), answer(first, Row1), in_row(second, Row2, N), answer(second, Row2).

#show candidate/1.
PK      ��D����m  m     ../common.py.lp#script (python)

from gringo import Fun

NULL = Fun('__null', [])

def arity(term):
    if isinstance(term, tuple): return len(term)
    if isinstance(term, Fun): return len(term.args())
    return 0

def nth(term, n):
    if isinstance(term, tuple): return term[n-1]
    if isinstance(term, Fun): return term.args()[n - 1]
    return NULL

#end.
PK     ���Dj�r
(  (             �    launcher.pyPK     ׎�D=6\��  �             �Q  MagicTrick.lpPK      ��D����m  m             �0  ../common.py.lpPK      �   �    