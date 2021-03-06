#!/usr/bin/python
#@Author: Bilal Ahamad (bilal.ahamad@gmail.com)

import sys

try:
    f = open(sys.argv[1], 'r')
    totalTC = int(f.readline())
    inputs = f.readlines()
    f.close()
    result = []
    for i in range(0, totalTC):
        tcsmall = inputs[i*5:i*5+5]
        inpt = ''.join((''.join(tcsmall)).split('\n'))
        if 'T' in inpt:
            k = inpt.index('T')
            li = list(inpt)
            li[k] = 'X'
            inpt_x = ''.join(li)
            li[k] = 'O'
            inpt_o = ''.join(li)
        else:
            inpt_x = inpt_o = inpt

        posSet = [[0,1,2,3], [4,5,6,7], [8,9,10,11], [12,13,14,15],
                  [0,4,8,12], [1,5,9,13], [2,6,10,14], [3,7,11,15],
                  [0,5,10,15], [3,6,9,12]]
        flag = 0
        for l in range(0, len(posSet)):
            if (inpt_x[posSet[l][0]] == inpt_x[posSet[l][1]] == inpt_x[posSet[l][2]] == inpt_x[posSet[l][3]] == 'X') and flag == 0:
                result.append('X won')
                flag = 1
                break
            if (inpt_o[posSet[l][0]] == inpt_o[posSet[l][1]] == inpt_o[posSet[l][2]] == inpt_o[posSet[l][3]] == 'O') and flag == 0:
                result.append('O won')
                flag = 1
                break

        if not '.' in inpt_x or not '.' in inpt_o:
            if flag == 0:
                result.append('Draw')
                flag = 1
        else:
            if flag == 0:
                result.append('Game has not completed')
                flag = 1
    result_list = []
    if flag == 1:
        for _ in range(1, totalTC+1):
            #print 'Case #'+str(_)+': '+result[_-1]
            result_list.append('Case #'+str(_)+': '+result[_-1]+'\n')
        fo = open('output.txt', 'w')
        fo.writelines(result_list)
        fo.close()
        

except Exception, e:
    print str(e)
