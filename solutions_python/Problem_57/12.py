PK     �&�<b`�DH
  H
  *   Work/MyProjects/GCJ/2010/QR2.A/B/solver.pyimport os,sys,glob,zipfile,heapq
try:
    import unittest2 as unittest
except:
    import unittest


def debug(locals,where=''):
    print '%s locals:%s ' % (where,locals)


def solve(row,D,I,M):
    MAX = 100*100*100
    minc = [0 for i in range(256)]
    for r in row:
        actc = [minc[i]+D for i in range(256)] 
        #best = actc[r]
        for mr in range(256):
            if M == 0:
                actc[mr] = min(actc[mr],minc[mr]+abs(mr-r))
            else:
                for pr in range(256):
                    mpr = minc[pr]
                    inum = (abs(abs(pr-mr)-1))/M
                    mnum = abs(mr-r)
                    #best = min(best,mpr+inum*I)
                    #best = min(best,mpr+abs(r-pr)) # edit
                    #if mr == 3 and r == 7 and pr == 1:
                    #    print 'mnum:%d inum:%d M:%d' % (mnum,inum,M)
                    actc[mr] = min(actc[mr],mpr+inum*I+mnum)
        #print 'actc:%d = %s' % (r,actc)
        minc = actc
    return min(minc)

def solve_cases(inf,outf):
    T = int(inf.readline())
    for casei in range(T):
        D,I,M,N = map(int,inf.readline().split())
        row = map(int,inf.readline().split())
        y = solve(row,D,I,M)
        ret = 'Case #%d: %s\n' % (casei+1,y)
        outf.write(ret)

def solve_all(input_file,output_file):
    print "solving:%s" % input_file
    with open(output_file,'w') as outf:
        with open(input_file,'r') as inf:
            solve_cases(inf,outf)


class SolverTest(unittest.TestCase):
    def _testDataDir(self):
        return os.path.join(os.path.dirname(__file__),'test_data')
    def _testOne(self):
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
    PK     �&�<b`�DH
  H
  *           ��    Work/MyProjects/GCJ/2010/QR2.A/B/solver.pyPK      X   �
    