import sys

test = int(input().strip())
for i in range(test):
    x,y = input().strip().split(' ')
    d=int(x)
    n=int(y)
    k=[]
    s=[]
    t=[]
    for j in range(n):
        x,y = input().strip().split(' ')
        t.append((d-int(x))/int(y))
    j=t.index(max(t))
    z=round((d/t[j]),6)
    print("Case #"+str(i+1)+": %.6f" %z)
