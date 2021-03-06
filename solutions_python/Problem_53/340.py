PK     t�<��Z�  �     solution.pyfrom util import * #@UnusedWildImport

def solution(filename):
    runTestCases(filename, resolveTestCase);

def resolveTestCase():
    #n snapper, k times
    n,k = readInts()
    return resolveTestCaseFast(n, k)

def resolveTestCaseSlow(n,k):
    #n snapper, k times
    snappers = [False for i in range(n)]
    for t in xrange(k):
        for i,ss in enumerate(snappers):
            if ss:
                snappers[i] = not ss
            else:
                snappers[i] = True
                break
        #trace([1 if x else 0 for x in snappers])
    return "ON" if all(snappers) else "OFF"  

def resolveTestCaseFast(n,k):
    return "ON" if (k+1)%(2**n)==0 else "OFF"
            
if __name__ == "__main__":
    solution("example.txt")            
    

PK     �S�<�C       util.pyimport sys
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

def readString():
    global inFile
    return inFile.readline().translate(None, '\n')

def readStrings():
    global inFile
    return inFile.readline().split()
    
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
    PK     t�<��Z�  �             ��    solution.pyPK     �S�<�C               ��&  util.pyPK      n   e    