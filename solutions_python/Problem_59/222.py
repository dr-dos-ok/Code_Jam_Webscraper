PK     擶<dSiȸ  �     solution.pyfrom collections import defaultdict
from util import * #@UnusedWildImport
import shutil
import os

def solution(filename):
    runTestCases(filename, resolveTestCase);

def resolveTestCase():
    n,m = readInts()
    existing = readTrimmedLines(n)
    todo = readTrimmedLines(m)
    return solve(existing,todo)

def createDir(list):
    c = 0
    fname = 'td'
    for f in list:
        fname += '/'+f
        if not os.path.exists(fname):
            os.mkdir(fname)
            c += 1
    return c
            
def solve(existing,todo):
    existing = [l[1:].split('/') for l in existing]
    todo = [l[1:].split('/') for l in todo]
    trace(existing,todo)
    os.mkdir('td')
    c = 0
    for p in existing:
        createDir(p)
    for p in todo:
        c += createDir(p)        
    shutil.rmtree('td')
    return c

if __name__ == "__main__":            
    #solution("example.txt")            
    print solve(['/a'],['/a/b','/a/c','/b/b'])

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
    PK     擶<dSiȸ  �             ��    solution.pyPK     ��<	Y               ���  util.pyPK      n       