PK     ���<q ��
  �
  '   Work/MyProjects/GCJ/2010/R1/B/solver.pyimport os,sys,glob,zipfile,heapq
try:
    import unittest2 as unittest
except:
    import unittest

def debug(locals,where=''):
    print '%s locals:%s ' % (where,locals)

def do_solve(inf,outf):
    T, = map(int,inf.readline().split())
    for casei in range(T):
        P, = map(int,inf.readline().split())
        m = map(int,inf.readline().split())
        #print "M:%s" % m
        price = [[] for ii in range(P)]
        for pi in range(P):
            price[pi] = map(int,inf.readline().split())
        MAX = 100*100000
        sol = [None for i in range(P+1)]
        sol[0] = [None for ii in range(2**P)]
        for i in range(2**P):
            sol[0][i] = [None for li in range(P+1)]
            for l in range(P+1):
                if l >= P-m[i]:
                    sol[0][i][l] = 0
                else:
                    sol[0][i][l] = MAX
        #print 'Sol0:%s' % sol[0]
        for k in range(1,P+1):
            sol[k] = [None for ii in range(2**(P-k))]
            for i in range(2**(P-k)):
                sol[k][i] = [None for li in range(P-k+1)]
                for l in range(P-k+1):
                    sol[k][i][l] = min(price[k-1][i]+sol[k-1][2*i][l+1]+sol[k-1][2*i+1][l+1],
                                       sol[k-1][2*i][l]+sol[k-1][2*i+1][l])
        #print 'Sol P:%s' % (sol[P]) 
        #print 'Sol P-1:%s' % (sol[P-1]) 
        res = sol[P][0][0]
        ret = 'Case #%d: %d\n' % (casei+1,res)
        outf.write(ret)
        #raise Exception(ret)

def solve(input_file,output_file):
    with open(output_file,'w') as outf:
        with open(input_file,'r') as inf:
            do_solve(inf,outf)
            


class SolverTest(unittest.TestCase):
    def _testDataDir(self):
        return os.path.join(os.path.dirname(__file__),'test_data')
    def testAll(self):
        items = list(glob.glob(os.path.join(self._testDataDir(),'*.in.txt')))
        items.sort()
        for input_file in items:
            output_file = '.'.join(input_file.split('.')[:-2]+['out','gen','txt'])
            reference_file = '.'.join(input_file.split('.')[:-2]+['out','ref','txt'])
            print 'Solving:%s' % (os.path.basename(input_file))
            solve(input_file,output_file)
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
    PK     ���<q ��
  �
  '           ��    Work/MyProjects/GCJ/2010/R1/B/solver.pyPK      U   �
    