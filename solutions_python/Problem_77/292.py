#c:/cygwin/home/python
#python 2.6.5
#input from stdin.in, output to stdout.out 

import sys
import math

trial=list()
setting=list()
candy=list()
bicandy=list()

def fair (a):
    if divmod(a,10)[1]%2==1:
        return 0
    if divmod(a,10)[0]==0:
        return 1
    else:
        a=divmod(a,10)[0]
        return fair(a)

def main():
    f= open(sys.argv[1],'r')
    numcases=int(f.readline().strip())
    for x in range(numcases):
        count1=0.0000001
        index=int(f.readline().strip())
        trial.append([int(y) for y in f.readline().strip().split()])
        for y in range(index):
            if y+1!=trial[x][y]:
                count1=1.0+count1
        print  'Case #%g: %.6f \n'%(x+1, count1)
    return


if __name__=="__main__": 
    main() 
