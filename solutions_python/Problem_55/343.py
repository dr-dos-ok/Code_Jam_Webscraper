PK     {s�<d�J�         solution.pyfrom collections import deque
from util import * #@UnusedWildImport

def solution(filename):
    runTestCases(filename, resolveTestCase);

def resolveTestCase():
    # runs,space for k people,n people,
    r,k,n = readInts()
    g = readInts()
    #trace(r,k,n,g)
    return testCaseResultFast(r,k,n,g)

def testCaseResultSlow(r,k,n,gList):
    g = deque(gList)
    result = 0
    for ri in xrange(r):
        p = k
        #trace(g)
        for i in xrange(n):
            gi = g[0]
            if gi<=p:
                p -= gi
                g.rotate(-1)
            else:                
                break
        result += k-p
    return result
    
def testCaseResultFast(r,k,n,gList):
    g = deque(gList)
    result = 0
    pos = 0
    ri = 0
    sumUntil = [None for i in range(n)]
    posModPos = [None for i in range(n)]
    foundLoop = False
    while ri<r:
        p = k        
        #trace(g)
        for i in xrange(n):
            gi = g[0]
            if gi<=p:
                p -= gi
                g.rotate(-1)
                pos += 1
            else:                
                break        
        ri += 1
        result += k-p
        if not foundLoop:
            posMod = pos%n
            if sumUntil[posMod]!=None:
                #trace("FoundLoop")
                foundLoop = True
                loopLength = ri-posModPos[posMod]
                remainingLoops = (r-ri)/loopLength
                loopSum = result-sumUntil[posMod]
                result += loopSum * remainingLoops
                ri += remainingLoops*loopLength
            else:
                sumUntil[posMod] = result
                posModPos[posMod] = ri
                
    return result            

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
    PK     {s�<d�J�                 ��    solution.pyPK     �S�<�C               ��)  util.pyPK      n   h    