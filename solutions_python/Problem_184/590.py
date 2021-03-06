# encoding: UTF-8

from __future__ import absolute_import, division

import collections
import itertools
import sys

class gcj:
    IN = open('D:\code jam\input.in', 'r')
    OUT = open('D:\code jam\output.txt', 'w')
    buf = None

    identity = lambda x: x

    @classmethod
    def _read_line(cls):
        if cls.buf:
            res = cls.buf
            cls.buf = None
        else:
            res = cls.IN.readline()
        if not res:
            raise EOFError()
        return res

    @classmethod
    def line(cls, conv=identity):
        line = cls._read_line()
        return conv(line.rstrip(b'\r\n'))

    @classmethod
    def splitline(cls, conv=identity):
        line = cls._read_line()
        return [conv(x) for x in line.split()]

    @classmethod
    def whitespace(cls):
        line = None
        while not line:
            line = cls._read_line()
            i = 0
            l = len(line)
            while i < l and line[i].isspace():
                i += 1
            line = line[i:]
        cls.buf = line

    @classmethod
    def token(cls, conv=identity):
        cls.whitespace()
        line = cls._read_line()
        i = 0
        l = len(line)
        while i < l and not line[i].isspace():
            i += 1
        cls.buf = line[i:] if i < l else None
        return conv(line[:i])

    @classmethod
    def tokens(cls, cnt, conv=identity):
        #tokens=[]
        #for _ in range(cnt):
        #    tokens.append(cls.token(conv))
        #return tokens   
        return [cls.token(conv) for _ in range(cnt)]

    current_case = 0

    @classmethod
    def case(cls):
        cls.current_case += 1
        return 'Case #{}:'.format(cls.current_case)
    
    @classmethod
    def writefile(cls, case, solve):
        cls.OUT.write( case + " " + str(solve) + '\n')
        return
    

def solve():
    #Get Variables
    S = gcj.token(str) #can be token(int) or tokens(N, int) # can be int or str

    #SOLVE
    numbers = [0]*10
    
    numbers[0]=S.count('Z')
    numbers[2]=S.count('W')
    numbers[4]=S.count('U')
    numbers[3]= S.count('R') - numbers[4] - numbers[0]

    numbers[5]= S.count('F') - numbers[4]
    
    numbers[6]= S.count('X')
    numbers[7]= S.count('V') - numbers[5]
    numbers[8]= S.count('G')

    numbers[9]= S.count('I') - numbers[5] - numbers[6] -numbers[8]
    numbers[1]= S.count('N') - numbers[7] - numbers[9] -numbers[9]

    
    #print('S:', S)
    #print('numbers:', numbers)    
    
    result='0'*numbers[0]+'1'*numbers[1]+'2'*numbers[2]+'3'*numbers[3]+'4'*numbers[4]
    result+='5'*numbers[5]+'6'*numbers[6]+'7'*numbers[7]+'8'*numbers[8]+'9'*numbers[9]
    #print('B:', B)    
    #print('K:', K)    

        
    return result


def main():
    t = gcj.token(int)
    for _ in range(t):
        case = gcj.case()
        if case == "Case #34:":
            j=1
        result = solve()
        
        gcj.writefile(case, result)
        print(case, result)

main()
