#c:/cygwin/home/python
#python 2.6.5
#input from stdin.in, output to stdout.out 

import sys
import math

candy=list()
bicandy=list()
lenbi=list()

def main():
    f= open(sys.argv[1],'r')
    numcases=int(f.readline().strip())
    for x in range(numcases):
        pile=0
        final=0
        index=int(f.readline().strip())
        candy.append([int(y) for y in f.readline().strip().split()])
        candy[x].sort()
        candy[x].reverse()
        bicandy.append([str(bin(z)[2:]) for z in candy[x]])
        lenbi.append([int(len(z)) for z in bicandy[x]])
        for y in range(lenbi[x][0]):
            count1=0
            for z in range(len(lenbi[x])):
                if lenbi[x][z]>y:
                    count1+=int(bicandy[x][z][lenbi[x][z]-1-y])
            if (count1%2)!=0:
                pile=1
        j=0
        safe=0
        final=sum(candy[x][:-1])
        if pile==1:
            print  'Case #{0}: NO \n'.format(x+1)
        if pile==0:
           print   'Case #{0}: {1} \n'.format(x+1, final)
           #print bicandy[x]
    return


if __name__=="__main__": 
    main() 
