
def foo(n):
    m=foo_one(n)
    if m==n:
        return m
    else:
        return foo(m)

def foo_one(n):
    d=[int(x) for x in str(n)]
    for i in range(len(d)-1):
        if d[i]>d[i+1]:
            d[i]=d[i]-1
            for j in range(i+1,len(d)):
                d[j]=9
    return int(''.join([str(x) for x in d]))


def ok(m):
    d=[int(x) for x in str(m)]
    for i in range(len(d)-1):
        if d[i+1]<d[i]:
            return False
    return True

def bar(n):
    for m in range(n,0,-1):
        if ok(m):
            return m

    

raw="""
100
132
1000
7
111111111111111110
1000000000000000000
959798857587567
43477899
71123566779
400514348429604398
666603345995689864
533
60322605208664241
11111111102244778
12246788999668899
12001123579
999999999999999999
22057370054667840
637
934010629695734211
11122003
111111122222222207
832354831424371238
111113455566666776
737351771047945138
418997373735364302
87
22234456890
43999999
211222334444567789
11222333445566623
1
835
68
322223445578889000
61344578
63
447894926990349645
516764369855276840
329999999999999
65999999999
712336778899999
11111111000
13557848
111111111109077
11122333331
80
551827015686761912
616108304267359558
533761910124648418
640644838994347044
693679388759159895
511133455666780
122346778877888999
634786521656636590
513947463518994342
439
219
61133778888
22203456889
11222335566777775
61
708173776881532728
563705935632477692
111111111111110863
52274789357
259364073089726476
11111111109
12234773968
61223344466689998
354992304834257322
122345788897778
81345569
429874446374190392
11111222334555690
152679758475359765
663847161101103282
57894566
123897977999778
622223444466688
111111111111108
43999999999999999
41122456
511123444555566678
220
5
805164181836956955
11111222344666117
48557779
110476676308197
973507579171348913
81111246677888999
488655711035942417
916217325839103001
135526289467942878
12511579
892417814763979377
111222223334442
859761602938240917
219999999999999999
11222221

"""



lines=[x for x in raw.split('\n') if x]
n=int(lines[0])
for i in range(n):
    a=foo(int(lines[i+1]))
    #b=bar(int(lines[i+1]))
    print('Case #'+str(i+1)+': '+str(a))
    #if(a!=b):
    #    print (a==b,a,b)
    
