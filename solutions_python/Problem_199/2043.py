import sys

t=int(input().strip())
for i in range(t):
    s,f=input().strip().split(' ')
    flip=int(f)
    l=[]
    l=str(s)
    c=[]
    for j in l:
        if j=='+':
            c.append(1)
        elif j=='-':
            c.append(0)
    m=len(c)
    count=0
    k=0
    flag = 1 
    while k<m:
        if c[k]==0:
            p=0
            if k+flip<=m:
                count=count+1
                while p<flip:
                    if c[p+k]==0:
                        c[p+k]=1
                    else:
                        c[p+k]=0
                    p=p+1    
            else:
                flag=0
                break
        k=k+1
    if flag==1:
         print("Case #"+str(i+1)+": "+str(count))
    else:
        print("Case #"+str(i+1)+": IMPOSSIBLE")
       
