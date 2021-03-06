PK     ���<7e��  �     solution.pyfrom collections import defaultdict
from util import * #@UnusedWildImport
from itertools import combinations
import psyco

psyco.full() 

def solution(filename):
    runTestCases(filename, resolveTestCase);

def resolveTestCase():
    n = readInt()
    return solve(n)

def isPure(x,s):
    lastI = x
    i = s.index(x)+1    
    while i!=1 and lastI!=i:
        lastI = i
        if i not in s:
            return False
        i = s.index(i)+1
    return i==1

         
cache = {}            

def solve(x):
    global cache
    if x in cache:
        return cache[x]
    c = 0
    s = range(2,x)
    #trace(s)
    for k in range(1,len(s)+1):
        #trace(k)
        for ss in combinations(s,k):
            if isPure(x, ss+(x,)):
                c += 1 
                #trace(ss)
    c += 1
    c = c%100003
    cache[x]=c
    return c 

if __name__ == "__main__":            
    solution("example.txt")
    #print solve(25)
    #print isPure(2,[2,4])            
    

PK     ��<	Y       util.pyimport sys
from collections import defaultdict

global enableTrace,inFile
enableTrace = True

def inFile():
    return inFile

def openFile(filename):
    global inFile
    inFile = open(filename)

def rangeFrom1(n):
    return xrange(1,n+1)

def readInt():
    global inFile
    return int(inFile.readline().strip())

def readInts():
    global inFile
    return map(int, inFile.readline().split())

def readFloats():
    global inFile
    return map(float, inFile.readline().split())

def readString():
    global inFile
    return inFile.readline().translate(None, '\n')

def readStrings():
    global inFile
    return inFile.readline().split()

def readLines(lines):
    global inFile
    s = ""
    for i in xrange(lines):
        s += inFile.readline()
    return s

def readTrimmedLines(lines):
    global inFile
    list = []
    for i in xrange(lines):
        list.append(readString())
    return list

def readStringsLines(lines):
    global inFile
    list = []
    for i in xrange(lines):
        list.append(readStrings())
    return list


    
def trace(*s):
    global enableTrace
    if enableTrace:
        sys.stderr.write(" ".join(map(str,s))+"\n");
        sys.stderr.flush()

def write(s):
    sys.stdout.write(s)
    
def flushOut():
    sys.stdout.flush()
    
def positionMap(l):
    positions = defaultdict(list)
    for i,p in enumerate(l):
        positions[p].append(i)   
    return positions 
    
def runTestCases(filename,algorithm):
    openFile(filename);
    n = readInt()
    for case in rangeFrom1(n):
        caseResult = algorithm()
        write("Case #%d: " % (case))
        if type(caseResult).__name__=='list' or type(caseResult).__name__=='tuple':
            caseResult = " ".join(map(str,caseResult))
        print caseResult
    inFile.close()
    PK     ���<7e��  �             ��    solution.pyPK     ��<	Y               ���  util.pyPK      n   '    