#c:/ p y t h o n 
#python 2.6.2
#input from *practice.in, output to *outputsmall.txt 
 
import sys
import math

snap=list()
setting=list()

def main():
    f = open('c:/python26/A-large.in', 'r')
    ou = open('c:/python26/outputlarge.txt', 'w')
    numcases=int(f.readline().strip())
    for x in range(numcases):
        snap.append([int(y) for y in f.readline().strip().split()])
        value=(snap[x][1]+1)/math.pow(2,snap[x][0])
        #print value
        if int(value) > 0:
            if value % int(value)> 0:
                setting.append('OFF')
                #print 'OFF'
            else:
                setting.append('ON')
                #print 'ON'
        else:
            setting.append('OFF')
            #print 'OFF'
        #print  'Case #{0}: {1} \n'.format(x+1, setting[x])
        ou.write('Case #{0}: {1} \n'.format(x+1, setting[x]))
    return
