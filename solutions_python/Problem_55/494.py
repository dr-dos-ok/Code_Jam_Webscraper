#c:/ p y t h o n 
#python 2.6.2
#input from *practice.in, output to *outputsmall.txt 
 
import sys
import math

info=list()
people=list()
money=list()

def main():
    f = open('c:/python26/C-small-attempt0.in', 'r')
    ou = open('c:/python26/outputsmall.txt', 'w')
    numcases=int(f.readline().strip())
    for x in range(numcases):
        info.append([int(y) for y in f.readline().strip().split()])
        people.append([int(y) for y in f.readline().strip().split()])
        count=0
        money.append(0)
        for rides in range(info[x][0]):
            pasangers=0
            for group in range (info[x][2]):
                if (int(info[x][1]-pasangers) >= people[x][count]):
                    pasangers=pasangers+people[x][count]
                    count=count+1
                    if count >= info[x][2]:
                        count=0
            money[x]=pasangers+money[x]
        #print money[x]
        #print  'Case #{0}: {1} \n'.format(x+1, money[x])
        ou.write('Case #{0}: {1} \n'.format(x+1, money[x]))
    return
