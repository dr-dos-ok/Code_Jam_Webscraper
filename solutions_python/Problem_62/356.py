#!/usr/bin/env python

'''

Rope Intranet

A company is located in two very tall buildings. The company intranet connecting the buildings consists of many wires, each connecting a window on the first building to a window on the second building.

You are looking at those buildings from the side, so that one of the buildings is to the left and one is to the right. The windows on the left building are seen as points on its right wall, and the windows on the right building are seen as points on its left wall. Wires are straight segments connecting a window on the left building to a window on the right building.

You've noticed that no two wires share an endpoint (in other words, there's at most one wire going out of each window). However, from your viewpoint, some of the wires intersect midway. You've also noticed that exactly two wires meet at each intersection point.

How many intersection points do you see?

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each case begins with a line containing an integer N, denoting the number of wires you see.

The next N lines each describe one wire with two integers Ai and Bi. These describe the windows that this wire connects: Ai is the height of the window on the left building, and Bi is the height of the window on the right building.

Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the number of intersection points you see.

Limits

1 <= T <= 15.
1 <= Ai <= 104.
1 <= Bi <= 104.
Within each test case, all Ai are different.
Within each test case, all Bi are different.
No three wires intersect at the same point.

Small dataset

1 <= N <= 2.

Large dataset

1 <= N <= 1000.

Sample


Input 
 	
Output 
 
2
3
1 10
5 5
7 7
2
1 1
2 2
Case #1: 2
Case #2: 0

author: cpm80
'''

from optparse import OptionParser

def main(filename):
    '''
    Main function

    Inputs
      filename - input filename 

    Outputs
      None   
    '''

    results = list()

    try:
        fd = open(filename, "r")
        numCases = int(fd.readline().strip())

        for i in xrange(numCases):
	    numWires = int(fd.readline().strip())
            buildingA = list()
            buildingB = list()

	    for j in xrange(numWires):
                pair = fd.readline().strip().split()
                buildingA.append(int(pair[0]))
                buildingB.append(int(pair[1]))
        
            points = 0
            for each in buildingA:
                a = buildingA.pop(0)
                b = buildingB.pop(0)
                if a == b:
                    pass                
                aboveA, belowA = partition(a, buildingA)
                aboveB, belowB = partition(b, buildingB)
                points += len(aboveA.intersection(belowB)) + \
                    len(belowA.intersection(aboveB))

            print "Case #%d: %d" % (i+1, points) 

        fd.close()

    except (IOError, ValueError, EOFError), e:
        print e.__str__()
        return None

    return None
      
def partition(pivot, array):
    '''
    '''
    above = list()
    below = list()

    for i in xrange(len(array)):
        if array[i] < pivot:
            below.append(i)
        else:
            above.append(i)

    return (set(above), set(below))

if __name__ == "__main__":

    usage = "usage: %prog [options] arg"

    parser = OptionParser(usage)

    (options, args) = parser.parse_args()

    if len(args) != 1:
        print "Invalid argument"
        parser.print_help()
    else:
        main(args[0])
