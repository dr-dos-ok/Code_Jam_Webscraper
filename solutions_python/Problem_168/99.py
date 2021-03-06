PK     ���F��l#  l#  	   cj_lib.py'''
CodeJam Python Lib for Festony, By Festony

Created on 2012-12-12

@author: festony
'''

import time
import inspect
import os.path
import shutil
import math
import fractions


import properties
import zipfile

from properties import *

__all__ = [ \
           'run_proc', \
           'accumulate', \
           'get_full', \
           'get_perm', \
           'get_comb', \
           'gen_prime', \
           'get_prime_list', \
           'int2bin', \
           'bin2int', \
           'gcd', \
           'nCk', \
           'nCkMod', \
           'testOnLine', \
           'get_yh_triangle', \
           ]

print_details = True

def print_detailed_info(info):
    if print_details:
        print info

def check_input(working_folder, file_name, func):
    in_path = working_folder + file_name + '.in'
    out_path = working_folder + file_name + '.out'
    
    r = [in_path, out_path, working_folder]
    
    if file_name.find('test') >= 0:
        return r
    
    full_source_path = inspect.getsourcefile(func)
    source_file_name = full_source_path.split('\\')[-1][:-3]
    first_separator_index = source_file_name.find('_')
    if first_separator_index < 0:
        return r
    in_year_str = source_file_name[:first_separator_index]
    in_year = -1
    try:
        in_year = int(in_year_str)
    except ValueError:
        return r
    if in_year < 2007 or in_year > 2020:
        return r
    source_file_name = source_file_name[first_separator_index+1:]
    first_separator_index = source_file_name.find('_')
    if first_separator_index < 0:
        return r
    in_round = source_file_name[:first_separator_index]
    source_file_name = source_file_name[first_separator_index+1:]
    question = source_file_name[0]
    if len(source_file_name) > 1 and source_file_name[1] != '_':
        return r
    if not question.isalpha() or question != question.upper():
        return r
    moved_in_folder = working_folder + in_year_str + "\\" + in_round + "\\"
    if not os.path.isdir(moved_in_folder):
        os.makedirs(moved_in_folder)
    new_in_path = moved_in_folder + file_name + '.in'
    new_out_path = moved_in_folder + file_name + '.out'
    new_r = [new_in_path, new_out_path, moved_in_folder]
    if os.path.isfile(new_in_path):
        return new_r
    if os.path.isfile(in_path):
        shutil.move(in_path, new_in_path)
        return new_r
    return r

def run_proc(func, input_dividing_func, working_folder=default_working_folder, file_name=default_file_name):
    '''Run the function multiple times for cases.
    
    Process time for each run / all runs are tracked.
    1) need to provide the function to process each case, the function
    should take a list as raw func_input;
    2) an input_dividing_func should be provided to break func_input lines into func_input lists
    for each case.
    '''
    in_path = working_folder + file_name + '.in'
    out_path = working_folder + file_name + '.out'
    in_path, out_path, working_folder = check_input(working_folder, file_name, func)
    inputfile = open(in_path, 'r')
    raw_input_str = inputfile.read()
    inputfile.close()
    input_lines = map(lambda x:x.rstrip('\r\n'), raw_input_str.split('\n'))
    inputs = input_dividing_func(input_lines)
    r = ''
    case_total_num = len(inputs)
    print_detailed_info('{0} cases in total.'.format(case_total_num))
    start_time_overall = time.clock()
    
    for i, func_input in enumerate(inputs):
        case_num = i + 1
        print_detailed_info('Case {0}:'.format(case_num))
        start_time_single_case = time.clock()
        r += 'Case #%d: %s\n' % (case_num, str(func(func_input)))
        print_detailed_info("Process time: %g sec(s)" % \
        (time.clock() - start_time_single_case,))
        print_detailed_info("Overall process time till now: %g sec(s)" % \
        (time.clock() - start_time_overall,))
    
    end_time_overall = time.clock()
    print(r)
    print("Overall process time: %g sec(s)" % \
    (end_time_overall - start_time_overall,))
    inputfile = open(out_path, 'w')
    inputfile.write(r)
    inputfile.close()
    
    if not ('practice' in file_name or 'test' in file_name):
        cjlibfile = inspect.getsourcefile(run_proc)
        propfile = inspect.getsourcefile(properties)
        funcfile = inspect.getsourcefile(func)
        codezip = zipfile.ZipFile(working_folder + file_name + '-code.zip', 'w')
        codezip.write(cjlibfile, os.path.split(cjlibfile)[1])
        codezip.write(propfile, os.path.split(propfile)[1])
        codezip.write(funcfile, os.path.split(funcfile)[1])
        codezip.close()
    
    return r

# commonly used functions

def accumulate(l):
    r = l[:]
    for i in range(1, len(r)):
        r[i] += r[i-1]
    return r

def get_full(k):
    r = []
    k1 = 0
    for i in range(k):
        if r == []:
            for j in range(k):
                r.append([j])
        else:
            l = len(r)
            for j in range(l):
                temp = r.pop(0)
                for j1 in range(k):
                    temp2 = temp + [j1]
                    r.append(temp2)
    return r

def get_perm(k, n):
    if k == 0:
        return []
    r = []
    if k == 1:
        for i in range(n):
            r.append([i])
        return r
    r1 = get_perm(k-1, n)
    r = []
    for p in r1:
        for j in range(max(p)+1, n):
            for i in range(k):
                temp = p[:]
                temp.insert(i, j)
                r.append(temp)
    return r
    
def get_comb(k, n):
    '''
    get k items out of total n
    '''
    if k == 0:
        return []
    r = []
    if k == 1:
        for i in range(n):
            r.append([i])
        return r
    r1 = get_comb(k-1, n)
    for sr in r1:
        for i in range(sr[-1] + 1, n):
            if i not in sr:
                temp = sr[:]
                temp.append(i)
                r.append(temp)
    return r

def is_dividable(n, prime_list):
    for p in prime_list:
        if n % p == 0:
            return True
    return False

def gen_prime(n):
    r = [2]
    i = 3
    while i <= n:
        if not is_dividable(i, r):
            r.append(i)
        i += 2
    return r

def get_prime_list():
    f = open('prime_list.txt', 'r')
    prime_list = eval(f.read())
    f.close()
    return prime_list

def int2bin(n, N = None):
    bn = bin(n)[2:]
    if N == None or N <= len(bn):
        return map(int, list(bn))
    else:
        return map(int, list(bn.zfill(N)))

def bin2int(bn):
    return int(''.join(map(str, list(bn))), 2)

def gcd(N):
    if N == []:
        return 0
    n = N[:]
    while len(n) > 1:
        p = n[-2:]
        n = n[:-2]
        n.append(fractions.gcd(p[0], p[1]))
    return n[0]

def nCk(n, k):
    return int( reduce(lambda x,y:x*y, (fractions.Fraction(n-i, i+1) for i in range(k)), 1) )

def nCkMod(n, k, m):
    return (int( reduce(lambda x,y:(x*y)%m, (fractions.Fraction(n-i, i+1) for i in range(k)), 1) )) % m

def testOnLine(A, B, P, threshold = None):
    r = ((B[0]-A[0])*(P[1]-A[1])-(B[1]-A[1])*(P[0]-A[0]))
    if threshold == None:
        threshold = 0
    if r > threshold:
        return 1
    elif r < threshold * -1:
        return -1
    return 0

def get_yh_triangle(maxn):
    fname = 'yanghui_triangle_{}.txt'.format(maxn)
    f = open(fname, 'r')
    yh_tri = eval(f.read())
    f.close()
    return yh_tri


# Test
if __name__ == '__main__':
    def test_process_func(func_input):
        print 'func_input:', func_input
        return 0
    
    # Set test case input file
    f = open(default_working_folder + default_file_name + '.in', 'r')
    old_content = f.read()
    f.close()
    f = open(default_working_folder + default_file_name + '.in', 'w')
    f.write('''4
5
Yeehaw
NSM
Dont Ask
B9
Googol
10
Yeehaw
Yeehaw
Googol
B9
Googol
NSM
B9
NSM
Dont Ask
Googol
5
Yeehaw
NSM
Dont Ask
B9
Googol
7
Googol
Dont Ask
NSM
NSM
Yeehaw
Yeehaw
Googol
4
Zol
Zolz
Zollz
Zolzz
0
0
3
'AZ'
'BZ'
'CZ'
''')
    f.close()

    def test_input_dividing_func(input_lines):
        total_case = int(input_lines.pop(0))
        case_inputs = []
        for i in range(total_case):
            engine_num = int(input_lines.pop(0))
            engines = input_lines[:engine_num]
            del input_lines[:engine_num]
            query_num = int(input_lines.pop(0))
            queries = input_lines[:query_num]
            del input_lines[:query_num]
            case_inputs.append([engines, queries])
        return case_inputs
    
    run_proc(test_process_func, test_input_dividing_func)
    
    # restore file used in test case back to its original content.
    f = open(default_working_folder + default_file_name + '.in', 'w')
    f.write(old_content)
    f.close()
PK     SK�F`)��  �     properties.py'''
Created on Dec 12, 2012

@author: dingliangl
'''

# store some common properties that might be relative to local environment, so
# leave svn peace.

default_file_name = 'test'

default_input_file_path = r'D:\CodeJam\inout\test.in'
default_output_file_path = r'D:\CodeJam\inout\test.out'
default_working_folder = 'D:\\CodeJam\\inout\\'

curr_working_folder = 'D:\\CodeJam\\inout\\'


#default_input_file_path = r'G:\Project\Codejam_inout\test.in'
#default_output_file_path = r'G:\Project\Codejam_inout\test.out'
#default_working_folder = 'G:\\Project\\Codejam_inout\\'
#
#curr_working_folder = 'G:\\Project\\Codejam_inout\\2008\\q\\'
#
#curr_working_folder = 'G:\\Project\\Codejam_inout\\'

PK     ��Fَ3��  �     2015_r2_A_small.py'''
CodeJam Practice 
Created on 2012-12-20

@author: festony
'''

from cj_lib import *
from properties import *

import math
import fractions


curr_file_name = 'large'
#curr_file_name = 'small-attempt0'

#curr_file_name = 'large-practice'
#curr_file_name = 'small-practice'
#curr_file_name = 'test'

# map(int, input_lines.pop(0).split(' '))

def input_dividing_func(input_lines):
    total_case = int(input_lines.pop(0))
    case_inputs = []
    for i in range(total_case):
        R, C = map(int, input_lines.pop(0).split(' '))
        M = []
        for j in range(R):
            M.append(list(input_lines.pop(0)))
        case_inputs.append([R, C, M])
    return case_inputs

# pos:[x, y]

def turn_left(d):
    if d == 'v':
        return '>'
    if d == '>':
        return '^'
    if d == '^':
        return '<'
    return 'v'

def find_next_pos(R, C, M, pos, d):
    X, Y = pos
    if d == 'v' and Y < R-1:
        for y in range(Y+1, R):
            if M[y][X] != '.':
                return [X, y]
        return []
    if d == '^' and Y > 0:
        for y in range(Y-1, -1, -1):
            if M[y][X] != '.':
                return [X, y]
        return []
    if d == '>' and X < C-1:
        for x in range(X+1, C):
            if M[Y][x] != '.':
                return [x, Y]
        return []
    if d == '<' and X > 0:
        for x in range(X-1, -1, -1):
            if M[Y][x] != '.':
                return [x, Y]
        return []
    return []

def verify(R, C, M, pos, verified, temp_v):
    d = M[pos[1]][pos[0]]
    if d == '.':
        return 0
    if pos in verified or pos in temp_v:
        return 0
    # remain unchanged
    t0 = temp_v[:]
    t0.append(pos)
    next_pos = find_next_pos(R, C, M, pos, d)
    r0 = -1
    if next_pos != []:
        r0 = verify(R, C, M, pos, verified, t0)
        for p in t0:
            temp_v.append(p)
        return r0
    
    # left turn
    t1 = temp_v[:]
    t1.append(pos)
    d = turn_left(d)
    next_pos = find_next_pos(R, C, M, pos, d)
    r1 = -1
    if next_pos != []:
        r1 = verify(R, C, M, pos, verified, t1) + 1
    
    # left turn
    t2 = temp_v[:]
    t2.append(pos)
    d = turn_left(d)
    next_pos = find_next_pos(R, C, M, pos, d)
    r2 = -1
    if next_pos != []:
        r2 = verify(R, C, M, pos, verified, t2) + 1
    
    
    # left turn
    t3 = temp_v[:]
    t3.append(pos)
    d = turn_left(d)
    next_pos = find_next_pos(R, C, M, pos, d)
    r3 = -1
    if next_pos != []:
        r3 = verify(R, C, M, pos, verified, t3) + 1
    
    t = []
    min_r = -1
    if r0 > -1 and r0 < min_r:
        min_r = r0
        t = t0
    if r1 > -1 and r1 < min_r:
        min_r = r1
        t = t1
    if r2 > -1 and r2 < min_r:
        min_r = r2
        t = t2
    if r3 > -1 and r3 < min_r:
        min_r = r3
        t = t3
    
    if min_r > -1:
        for p in t:
            temp_v.append(p)
    
    return min_r

def simplified_v(R, C, M, pos):
    #print M, pos
    d = M[pos[1]][pos[0]]
    if d == '.':
        return 0
    next_pos = find_next_pos(R, C, M, pos, d)
    if next_pos != []:
        return 0
    while next_pos == []:
        d = turn_left(d)
        if d == M[pos[1]][pos[0]]:
            return -1
        next_pos = find_next_pos(R, C, M, pos, d)
        if next_pos != []:
            return 1
    
def process_func(func_input):
    R, C, M = func_input
    #print R, C, M
    r = 0
    for y in range(R):
        for x in range(C):
            pos = [x, y]
            #print pos
            tr = simplified_v(R, C, M, pos)
            if tr < 0:
                return 'IMPOSSIBLE'
            r += tr
    
    return r

if curr_file_name != 'test':
    filenamesec = __file__.split('_');
    q = filenamesec[2][0]
    curr_file_name = q + '-' + curr_file_name

run_proc(process_func, input_dividing_func, curr_working_folder, curr_file_name)


PK      ���F��l#  l#  	           ��    cj_lib.pyPK      SK�F`)��  �             ���#  properties.pyPK      ��Fَ3��  �             ���&  2015_r2_A_small.pyPK      �   �6    