#!/usr/bin/python
#coding: utf-8

t = int(raw_input())

formesOk = [ [],
        [[['c']]], #1
        [], #2
        [], #3
        [[['c','.'],['.','.']]], #4
        [], #5
        [[['c','.','.'],['.','.','.']],[['c','.'],['.','.'],['.','.']]], #6
        [], #7
        [[['c','.','.','.'],['.','.','.','.']],[['c','.','.'],['.','.','.'],['.','.','*']],[['c','.'],['.','.'],['.','.'],['.','.']]], #8
        [[['c','.','.'],['.','.','.'],['.','.','.']]], #9
        [[['c','.','.','.','.'],['.','.','.','.','.']],[['c','.','.','.'],['.','.','.','.'],['.','.','*','*']],[['c','.','.'],['.','.','.'],['.','.','*'],['.','.','*']],[['c','.'],['.','.'],['.','.'],['.','.'],['.','.']]], #10
        [[['c','.','.','.'],['.','.','.','.'],['.','.','.','*']],[['c','.','.'],['.','.','.'],['.','.','.'],['.','.','*']]], #11
        [[['c','.','.','.'],['.','.','.','.'],['.','.','.','.']],[['c','.','.'],['.','.','.'],['.','.','.'],['.','.','.']]], #12
        [[['c','.','.','.','.'],['.','.','.','.','.'],['.','.','.','*','*']],[['c','.','.','.'],['.','.','.','.'],['.','.','.','*'],['.','.','*','*']],[['c','.','.'],['.','.','.'],['.','.','.'],['.','.','*'],['.','.','*']]], #13
        [[['c','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','*']],[['c','.','.','.'],['.','.','.','.'],['.','.','.','.'],['.','.','*','*']],[['c','.','.'],['.','.','.'],['.','.','.'],['.','.','.'],['.','.','*']]], #14
        [[['c','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.']],[['c','.','.','.'],['.','.','.','.'],['.','.','.','.'],['.','.','.','*']],[['c','.','.'],['.','.','.'],['.','.','.'],['.','.','.'],['.','.','.']]], #15
        [[['c','.','.','.'],['.','.','.','.'],['.','.','.','.'],['.','.','.','.']]], #16
        [[['c','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','*','*','*']],[['c','.','.','.'],['.','.','.','.'],['.','.','.','*'],['.','.','.','*'],['.','.','.','*']]], #17
        [[['c','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','*','*']],[['c','.','.','.'],['.','.','.','.'],['.','.','.','.'],['.','.','.','*'],['.','.','.','*']]], #18
        [[['c','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','*']],[['c','.','.','.'],['.','.','.','.'],['.','.','.','.'],['.','.','.','.'],['.','.','.','*']]], #19
        [[['c','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.']],[['c','.','.','.'],['.','.','.','.'],['.','.','.','.'],['.','.','.','.'],['.','.','.','.']]], #20
        [[['c','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','*'],['.','.','*','*','*']]], #21
        [[['c','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','*','*','*']]], #22
        [[['c','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','*','*']]], #23
        [[['c','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','*']]], #24
        [[['c','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.']]]] #25

def printtab(t):
    for l in t:
        print ''.join(l)

'''
i = 0
for formes in formesOk:
    print "== %d ==" % i
    for forme in formes:
        print
        printtab(forme)
    print
    i += 1
'''

def tournerTab(t):
    tt = []
    for i in xrange(t[0]):
        l = []
        for j in xrange(t):
            l.append('')
        tt.append(l)
    for i in xrange(t):
        for j in xrange(t[0]):
            tt[j][i] = t[i][j]


for case in xrange(1,t+1):
    i = [eval (n) for n in raw_input().strip().split(" ")]
    r,c,m = int(i[0]),int(i[1]),int(i[2])
    print "Case #%d:" % case
    if (c == 1):
        print "c"
        for i in xrange(0,r-m-1):
            print "."
        for i in xrange(0,m):
            print "*"
    elif (r == 1):
        s = "c"
        for i in xrange(0,c-m-1):
            s += "."
        for i in xrange(0,m):
            s += "*"
        print s
    else:
        formes = formesOk[r*c-m]
        possible = False
        t = []
        for i in xrange(0,r):
            l = []
            for j in xrange(0,c):
                l.append('*')
            t.append(l)
        for forme in formes:
            rr = len(forme)
            cc = len(forme[0])
            if (rr <= r and cc <= c and not possible):
                possible = True
                for i in xrange(0,rr):
                    for j in xrange(0,cc):
                        t[i][j] = forme[i][j]
        if not possible:
            #print "Impossible %d %d %d %d" % (r,c,m,r*c-m)
            print "Impossible"
        else:
            total = 0
            for l in t:
                for i in l:
                    if (i == '*'):
                        total += 1
            if (total != m):
                print "BUGBUGBUGBUGBUGBUGBUG"
            printtab(t)