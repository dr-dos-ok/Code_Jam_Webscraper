PK     q�<�=�d@  @  *   Work/MyProjects/GCJ/2010/QR2.A/A/solver.pyimport os,sys,glob,zipfile,heapq
try:
    import unittest2 as unittest
except:
    import unittest


def debug(locals,where=''):
    print '%s locals:%s ' % (where,locals)


def solve(rows,K):
    max = [[],[],[],[]]
    for row in rows:
        act = [[],[],[],[]]
        dirs = [[act[0],-1],[max[1],-1],[max[2],0],[max[3],1]]
        for i,c in enumerate(row):
            for diri,dir in enumerate(dirs):
                #print 'i:%s Diri:%s, dir:%s' % (i,diri,dir)
                actdir = act[diri]
                if c == '.':
                    actdir.append(0)
                else:
                    pmax = dir[0]
                    pi = i+dir[1]
                    if len(pmax) > pi and pi >= 0: 
                        maxval = pmax[pi]+1
                        actdir.append(maxval)
                        if maxval >= K:
                            return True
                    else: 
                        actdir.append(1)
        #print 'Act:%s' % act
        max = act
    return False

def solve_cases(inf,outf):
    T = int(inf.readline())
    for casei in range(T):
        N,K = map(int,inf.readline().split())
        redrows,bluerows = [],[]
        for i in range(N):
            redrow,bluerow = [],[]
            for ch in inf.readline():
                if ch == 'R':
                    redrow.append(ch)
                    bluerow.append('.')
                elif ch == 'B':
                    bluerow.append(ch)
                    redrow.append('.')
            redrows.append(list(reversed(redrow)))
            bluerows.append(list(reversed(bluerow)))
        #print "starting case:%d N:%d" % (casei+1,N)
        #print "redrows,bluerows:%s" % ((redrows,bluerows),) 
        reda,bluea = solve(redrows,K),solve(bluerows,K)
        ans = 'Neither'
        if reda and bluea:
            ans = 'Both'
        elif reda:
            ans = 'Red'
        elif bluea:
            ans = 'Blue'
        else:
            ans = 'Neither'
        ret = 'Case #%d: %s\n' % (casei+1,ans)
        outf.write(ret)

def solve_all(input_file,output_file):
    print "solving:%s" % input_file
    with open(output_file,'w') as outf:
        with open(input_file,'r') as inf:
            solve_cases(inf,outf)


class SolverTest(unittest.TestCase):
    def _testDataDir(self):
        return os.path.join(os.path.dirname(__file__),'test_data')
    def testOne(self):
        self.assertEqual(True,solve([['R'], ['R', '.'], ['R', '.'], ['R', '.']],4))   
    def testAll(self):
        items = list(glob.glob(os.path.join(self._testDataDir(),'*.in.txt')))
        items.sort()
        for input_file in items:
            print 'Solving:%s' % input_file
            output_file = '.'.join(input_file.split('.')[:-2]+['out','gen','txt'])
            reference_file = '.'.join(input_file.split('.')[:-2]+['out','ref','txt'])
            solve_all(input_file,output_file)
            if os.path.exists(reference_file):
                output = file(output_file).readlines()
                reference = file(reference_file).readlines()
                self.assertEqual(output,reference)
            

def package(file):
    zf = zipfile.ZipFile(os.path.join(os.path.dirname(__file__),'code.zip'),'w')
    zf.write(file)
    zf.close()  

if __name__=="__main__":
    package(__file__)
    #import cProfile
    #cProfile.run('unittest.main()')
    unittest.main()
    PK     q�<�=�d@  @  *           ��    Work/MyProjects/GCJ/2010/QR2.A/A/solver.pyPK      X   �    