#c:/cygwin/home/python
#python 2.6.5
#input from stdin.in, output to stdout.txt 

import sys
import math

value=list()
setting=list()
obutton=list()
bbutton=list()
btime=list()
otime=list()

def step(time,opos,otarget,bpos,btarget,turn):
    if turn=='O':
        if (bpos-btarget)!=0:
            if bpos>btarget: bpos+=-1
            if bpos<btarget: bpos+=1
        if opos==otarget:
            pushed=1
            time+=1
        else:
            pushed=0
            time+=1
        if opos>otarget: opos+=-1
        if opos<otarget: opos+=1
    if turn=='B':
        if (opos-otarget)!=0:
            if opos>otarget: opos+=-1
            if opos<otarget: opos+=1
        if bpos==btarget:
            pushed=1
            time+=1
        else:
            pushed=0
            time+=1
        if bpos>btarget: bpos+=-1
        if bpos<btarget: bpos+=1
    return (time,opos,otarget,bpos,btarget,turn,pushed)

    
def main():
    f= open(sys.argv[1],'r')
    numcases=int(f.readline().strip())
    for x in range(numcases):
        setting.append(f.readline().strip().split())
        #print int(setting[x][2])
        obutton.append([])
        bbutton.append([])
        for y in range(int(setting[x][0])):
            if setting[x][2*y+1]=='O':
                obutton[x].append(int(setting[x][2*y+2]))
                bbutton[x].append(-1)
            if setting[x][2*y+1]=='B':
                bbutton[x].append(int(setting[x][2*y+2]))
                obutton[x].append(-1)
        time=0
        opos=1
        otarget=obutton[x][0]
        btarget=bbutton[x][0]
        turn=setting[x][1]
        bpos=1
        count=0
        indexo=0
        indexb=0
        while count<(len(obutton[x])+1):
           while otarget<0 and indexo<len(obutton[x]):
                otarget=obutton[x][indexo]
                indexo+=1
           while btarget<0 and indexb<len(bbutton[x]):
                btarget=bbutton[x][indexb]
                indexb+=1
           if btarget==-1:
               bpos=-1
           if otarget==-1:
               opos=-1
           (time,opos,otarget,bpos,btarget,turn,pushed)=step(time,opos,otarget,bpos,btarget,turn)
           if pushed==1:
               count+=1
               if count<len(obutton[x]):
                   indexo=count
                   indexb=count
                   otarget=obutton[x][indexo]
                   btarget=bbutton[x][indexb]
                   turn=setting[x][2*count+1]
        print  'Case #{0}: {1} \n'.format(x+1, time-1)
    return


if __name__=="__main__": 
    main() 
