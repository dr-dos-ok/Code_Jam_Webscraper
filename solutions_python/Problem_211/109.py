#!/usr/local/bin/pypy3

import sys, io, types, os, time, concurrent.futures, multiprocessing
import math, decimal as dec, collections as coll, itertools as itt, fractions as fr, pickle, functools as fts

#SMALL


def code_here(_cc, _DEBUG, _data):
    global DEBUG
    DEBUG = _DEBUG
    dd = Data(_data)

    res = 0

    p = sorted(dd.P)

    p.append(10000)

    cur = 0
    sp = dd.U
    level = p[cur]
    while sp > 0 and cur < dd.N:
        new_cur = cur + 1
        while p[new_cur] == p[new_cur-1] and new_cur < dd.N:
            new_cur += 1

        new_level = p[new_cur]
        cur = new_cur

        if sp >= (new_level-level) * (cur):
            sp -= (new_level - level) * (cur)
            level = new_level
        else:
            level += sp / (cur)
            break



    res = level ** cur

    if cur < dd.N:
        res *= fts.reduce(lambda x, y: x*y, p[cur:dd.N] )


    return "{0:.8f}".format(res / 10000**(dd.N))


def read_data(_T):
    for _cc in range(_T):
        N, K = map(int, input().split())
        U = int(input().replace(".",""))
        P = list(map(lambda x: int(x.replace(".","")), input().split()))

        yield {k: v for k, v in locals().items() if k not in ["sys", "__builtins__", "_cc", "_T", "_i"]}


#<editor-fold defaultstate="collapsed" desc="GCJ init">

class Data(object):
    def __init__(self, dd):
        self.__dict__ = dd
        
_MAX_WORKERS = multiprocessing.cpu_count() - 1

def iterations(_outfile=None):
    _T = int(input())
    _tt = max(_T // 20, 1)

    _start_time = time.time()

    with concurrent.futures.ProcessPoolExecutor(max_workers=_MAX_WORKERS) as executor:
        map_func = map if DEBUG else executor.map

        _iterator = map_func(code_here, range(_T), itt.repeat(DEBUG, _T), read_data(_T))

        for _cc, res in zip(range(_T), _iterator):
            if _cc % _tt == 0:
                _time_diff = int((time.time() - _start_time) / (_cc + 1) * _T)
                print('Solving: ', (_cc + 1) * 100 // _T, '%',
                      'Estimated running:', '{}m {}s'.format(*divmod(_time_diff, 60)),
                      file=sys.stderr)

            if isinstance(res, list): 
                if DEBUG: print('Case #{}:'.format(_cc + 1))
                print('Case #{}:'.format(_cc + 1), file=_outfile)

                for _r in res:
                    if DEBUG: print(_r)
                    print(_r, file=_outfile)
            else:
                if DEBUG: print('Case #{}:'.format(_cc + 1), res)
                print('Case #{}:'.format(_cc + 1), res, file=_outfile)


def main():
    global DEBUG

    # Read input and prepare output
    _in = get_input_file()
    with open(_in, 'r') as _infile:
        sys.stdin.close()
        sys.stdin = _infile

        i = 0  # Do not overwrite existing files
        while os.path.isfile(_in + '.{}.out'.format(i)):
            i += 1

        print('', file=sys.stderr)
        if DEBUG: print('*** Running in DEBUG mode ***', file=sys.stderr)
        print('<<<', _in, '<<<', file=sys.stderr)
        print('>>>', _in + '.{}.out'.format(i), '>>>', file=sys.stderr)
        print('', file=sys.stderr)

        with open(_in + '.{}.out'.format(i), 'w') as _outfile:
            iterations(_outfile)

def get_input_file():
    global DEBUG
    
    # If file name is supplied via arguments – take it
    if len(sys.argv) > 1:
        _tmp = os.path.dirname(os.path.realpath(__file__)) + '/' + sys.argv[1]
        if os.path.isfile(_tmp):
            DEBUG, _in = len(sys.argv) > 2, _tmp
        else:
            DEBUG, _in = True, find_last_modified_file()
    else:
        DEBUG, _in = False, find_last_modified_file()
        # Debugging in PyCharm detection
        if "PYCHARM_HOSTED" in os.environ:
            try:
                import pydevd
                pycharm_debugging = True
            except ImportError:
                pycharm_debugging = False

            DEBUG = pycharm_debugging

    return _in

def find_last_modified_file(suffix='.in', subfolder=''):
    """
    Find the most recently modified *.in file (aka freshly downloaded input)
    in the *SAME* folder as the script
    :return: file path
    """
    _in = (0, None)
    _folder_path = os.path.dirname(os.path.realpath(__file__)) + subfolder  + '/'
    for _file in os.listdir(_folder_path):
        if _file.endswith(suffix):
            last_modified = os.path.getmtime(_folder_path + _file)
            if _in[0] < last_modified:
                _in = (last_modified, _folder_path + _file)
    if _in[1] == None:
        raise Exception('No input file is found :/')
    return _in[1]
    
#</editor-fold>

if __name__ == "__main__":
    main()