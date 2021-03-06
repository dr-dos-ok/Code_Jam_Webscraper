r = open('B-small-attempt6.in','r')
w = open('B-Output.out','w')

#r = ['3 1 5 15 13 11','3 0 8 23 22 21','2 1 1 8 0','6 2 8 29 20 8 18 18 21']

a0 = '''100
3 1 5 15 13 11
3 0 8 23 22 21
2 0 3 9 6
3 1 5 3 12 11
2 2 4 3 26
3 3 4 11 7 3
3 0 1 27 10 29
3 3 0 22 20 11
2 0 3 27 24
3 0 10 26 18 25
3 0 0 20 21 22
2 0 7 19 18
2 0 5 27 12
1 0 8 17
3 3 10 4 23 2
1 0 5 12
3 0 9 19 21 5
2 0 7 1 0
2 1 4 9 9
1 0 8 15
3 0 0 0 0 0
1 0 8 19
3 3 2 25 11 27
3 0 10 27 26 14
1 0 9 2
3 2 10 10 16 13
1 0 8 25
2 0 6 26 23
1 0 1 13
3 1 9 18 8 11
2 2 6 17 9
1 1 8 12
2 2 10 6 18
2 2 10 7 12
1 1 3 9
2 0 7 19 3
2 0 8 27 4
1 1 3 8
1 0 0 30
2 0 10 30 30
3 3 7 3 25 16
3 0 4 26 8 18
3 1 8 21 20 21
1 0 4 9
3 3 7 14 16 25
2 1 4 9 8
1 1 0 12
1 1 4 25
3 3 10 19 7 18
1 0 6 15
1 0 8 4
1 0 2 3
2 2 7 17 6
1 0 5 0
2 0 5 11 3
3 1 8 6 19 15
1 0 5 12
3 0 3 18 7 18
2 1 7 1 11
3 2 5 22 17 19
1 0 7 4
1 0 2 2
2 0 8 24 29
2 0 9 23 15
1 0 7 30
1 0 6 14
3 1 2 22 2 2
3 0 8 23 20 21
1 1 7 23
3 2 6 7 18 21
1 0 1 9
3 0 1 14 20 15
1 0 2 2
2 1 3 3 4
3 0 0 13 16 7
2 0 5 14 12
2 0 4 9 8
2 1 3 29 18
1 0 2 3
3 0 6 4 30 4
3 3 0 28 20 6
1 0 3 16
2 2 9 8 12
3 0 0 20 18 0
3 2 5 21 23 15
3 0 1 11 23 21
1 1 7 10
3 2 1 27 0 18
1 1 6 21
3 1 5 11 12 11
1 1 4 12
1 0 10 28
3 3 1 7 11 27
2 2 5 18 17
2 0 5 21 10
3 0 3 6 5 6
3 0 1 0 0 0
1 0 9 22
1 1 9 11
2 0 4 16 29

'''

numLines = int(r.readline())

def getMinScore(n):
    n = int(n)
    r = [n/3]*3
    if n%3 == 2:
        r[0] += 1
        r[1] += 1
    if n%3 == 1:
        r[0] += 1
    
    return r

def countBest(l,best,surprises):
    count = 0
    for i in l:
        if i[0] >= best:
            count+=1
        elif i[0] == i[1] and i[1] == i[2] and i[0] + 1 >= best and surprises > 0 and i[2] + i[1] + i[0] >= 1:
            count += 1
            surprises -= 1
        elif i[2] + 2 >= best and surprises > 0 and i[2] + i[1] + i[0] >= 2 and i[1] != i[2]:
            count += 1
            surprises -= 1
    return count

c = 1
for i in r:
    i = i.split(' ')
    numDancers = int(i[0])
    surprises = int(i[1])
    best = int(i[2])
    i = i[3:]
    #print i
    for n in range(len(i)):
        i[n] = getMinScore(i[n])
    w.write('Case #' + str(c) + ': ' + str(countBest(i,best,surprises)) + '\n')
    c += 1
    #print i,best,surprises,countBest(i,best,surprises)
                        
w.close()