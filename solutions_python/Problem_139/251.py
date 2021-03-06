PK     ��DW%	�  �     launcher.py#!/cygdrive/c/Python33_x64/python

### README:
# This is the wrapper around the solution. The actual solution is in "*.lp" file.
# The solution is written in AnsProlog, the language for answer set programming technique.
# The wrapper splits the input file into T independent testcases, launches T independent ASP solvers, and collects the results.
# 
# To launch the solution, you need the Potassco ASP toolkit.
# Link: http://potassco.sourceforge.net/
# You need the 'clingo' tool, version 4.3.0+. It should be built with Python scripting support (Linux version is built with it by
# default, Windows and OSX versions aren't). This tool should be available at the location specified by the global CLINGO variable.
#
# Launch this launcher as:
# launcher.py PROBLEMNAME TESTCATEGORY < INPUTFILE
# For example: launcher.py MagicTrick small < A-small.in

import sys
import os
import shutil
import multiprocessing
from time import sleep
from zipfile import ZipFile
from datetime import timedelta as span
from string import Template
from subprocess import PIPE, Popen, TimeoutExpired, CalledProcessError

CLINGO = r'C:\cygwin\home\Administrator\clingo-4.3.0-source\build\release\clingo.exe'
TIMEOUT = span(seconds = 20)
DEFAULT_CONF = 'auto'
TRY_CONFS = ['frumpy', 'trendy', 'crafty', 'auto']

# Reads the test input from the input stream, and dumps it into filename.lp.
# The only part of the launcher that has to be modified per problem.
def dump_test(inf, filename):
    N, L = inf.readline().split()
    with open(filename + ".lp", 'w+t') as f:
        f.write('#const device_count = {0}.\n#const bit_length = {1}.\n'.format(N, L))
        outlets = inf.readline().split()
        for i, outlet in enumerate(outlets):
            f.write('outlet({0}, ({1})).\n'.format(i + 1, ', '.join(list(outlet))))
        devices = inf.readline().split()
        for i, device in enumerate(devices):
            f.write('device({0}, ({1})).\n'.format(i + 1, ', '.join(list(device))))

def dump_result(outf, test, result, filename):
    with open(filename, 'w+t') as f:
        f.write(result)
    outf.write("Case #{0}: {1}\n".format(test, result))

problem_name = sys.argv[1]
size = sys.argv[2]
problem = "{0}-{1}".format(problem_name, size)
path = os.path.join(os.getcwd(), problem + "-data")
encoding_file = problem_name + ".lp"

def clingo_result(test):
    instance_file = os.path.join(path, "{0}.{1}.lp".format(problem, test))
    command = Template('$clingo --conf=$conf --outf=3 $encoding "$instance"').safe_substitute(encoding=encoding_file, instance=instance_file, clingo=CLINGO)
    process = Popen(Template(command).safe_substitute(conf=DEFAULT_CONF), universal_newlines=True, stdout=PIPE)
    try:
        result, _ = process.communicate(timeout=TIMEOUT.total_seconds())
    except TimeoutExpired as e:
        print('Test #{0}: TimeoutExpired'.format(test))
        process.kill()
        processes = [Popen(Template(command).safe_substitute(conf=conf), universal_newlines=True, stdout=PIPE) for conf in TRY_CONFS]
        running = True
        while running:
            for i, proc in enumerate(processes):
                return_code = proc.poll()
                if return_code is not None:
                    print('Test #{0}: process finished: {1} with conf={2}'.format(test, proc.pid, TRY_CONFS[i]))
                    result, _ = proc.communicate()
                    running = False
                    break
            else: sleep(.1)
        for proc in processes:
            if not proc.poll():
                proc.kill()
    except CalledProcessError as e:
        result = e.output
    return result.strip()


def main():
    shutil.rmtree(path, ignore_errors = True)
    os.mkdir(path)

    with sys.stdin as inf:
        test_count = int(inf.readline())
        for test in range(1, test_count + 1):
            dump_test(inf, os.path.join(path, "{0}.{1}".format(problem, test)))

    pool = multiprocessing.Pool()
    results = pool.map(clingo_result, range(1, test_count + 1))

    with open("{0}.out.txt".format(problem), 'w+t') as outf:
        for test in range(1, test_count + 1):
            dump_result(outf, test, results[test - 1], os.path.join(path, "{0}.{1}.out".format(problem, test)))

    with ZipFile("{0}.zip".format(problem), 'w') as zipf:
        zipf.write("launcher.py")
        zipf.write(encoding_file)
        zipf.write("../common.py.lp")

if __name__ == '__main__':
    main()
PK     ��DbC�  �     ChargingChaos.lp#include "../common.py.lp".

#script (python)
from gringo import SolveResult

def terms(model, name):
    return [t.args() for t in model.atoms(Model.ATOMS) if t.name() == name]

def on_model(model):
    global last_ans
    last_ans = len(terms(model, 'flip'))

def main(prg):
    prg.ground('base', [])
    result = prg.solve(on_model)
    if result == SolveResult.UNSAT:
        print 'NOT POSSIBLE'
    else:
        print last_ans

#end.

device_bit(Device, L, @nth(Bits, L)) :- device(Device, Bits), L = 1..bit_length.
outlet_bit(Outlet, L, @nth(Bits, L)) :- outlet(Outlet, Bits), L = 1..bit_length.

{ flip(L): L = 1..bit_length }.

result_bit(Outlet, L, B) :- outlet_bit(Outlet, L, B), not flip(L).
result_bit(Outlet, L, 1 - B) :- outlet_bit(Outlet, L, B), flip(L).

matches(Device, Outlet) :- matches_bit(Device, Outlet, L): L = 1..bit_length; Device = 1..device_count, Outlet = 1..device_count.
matches_bit(Device, Outlet, L) :- device_bit(Device, L, B), result_bit(Outlet, L, B).

1 { plug(Device, Outlet): matches(Device, Outlet) } 1 :- Device = 1..device_count.
:- Outlet = 1..device_count, #count { Device: plug(Device, Outlet) } != 1.

:~ flip(L). [1,L]
PK     �F�D#4{*�  �     ../common.py.lp#script (python)

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
PK      ��DW%	�  �             ��    launcher.pyPK      ��DbC�  �             ���  ChargingChaos.lpPK      �F�D#4{*�  �             ���  ../common.py.lpPK      �   �    