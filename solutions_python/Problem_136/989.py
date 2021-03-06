#!/usr/bin/python


def cookie(fw, i, C, F, X):
    rate = 2.0
    total_time = 0.0
    if (X <= C):
        total_time = X/rate;
    else:
        while(1):
            if((X/rate) < ((C/rate) + (X/(rate+F)))):
                total_time += X/rate
                break
            else:
                total_time += C/rate
                rate += F
    fw.write("Case #"+str(i)+": "+"%.7f"%total_time+"\n")


def inputData():
    fr = open('B-large.in','r')
    fw = open('resultat_cookie.txt','w')
    lines = fr.readlines()
    num_cases = int(lines[0])
    j = 1
    for i in range (1, num_cases + 1):
        line = lines[j].split()
        cookie(fw, i, float(line[0]), float(line[1]), float(line[2]))
        j += 1

if __name__ == "__main__":
    inputData()