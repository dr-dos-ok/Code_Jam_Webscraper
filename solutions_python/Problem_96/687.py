from sys import stdin


num_cases = int(stdin.readline())
for case_index in xrange(1, num_cases+1):
    line = stdin.readline().strip().split(' ')
    n,s,p = int(line[0]),int(line[1]),int(line[2])
    ss=s
    nlimit = 3*p - 2 if p > 0 else p
    slimit = 3*p - 4 if p > 2 else p
    maxg = 0
    
    t=[]
    for i in range(n):
        totscore = int(line[i+3])
        t.append(totscore)
        if totscore >= nlimit:
            maxg += 1
        elif totscore >= slimit and s > 0:            
            s -= 1
            maxg += 1
##    print '***[%s,%s] N:%d S:%d P:%d T:%s'%(nlimit,slimit,n,ss,p,t)
    print "Case #" + str(case_index) + ": " + str(maxg)
