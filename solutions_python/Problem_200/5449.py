import numpy as np

pos= (132,1000,7,791,676,741,892,291,174,56,834,512,184,307,8,540,415,388,127,825,225,767,345,884,445,795,706,769,838,581,690,380,495,800,421,427,712,673,486,850,166,245,76,351,325,91,383,675,428,613,559,891,621,267,520,65,771,235,567,624,238,968,403,725,822,564,134,154,296,426,1,446,999,527,340,925,983,770,745,45,640,922,526,318,369,461,738,848,872,953,555,129,762,890,206,241,674,710,856,147)
cpt = 1
for cpt in range(1,101):
    n=pos[cpt-1]
    tidy=0
    while (tidy == 0):
        s=str(n)
        tidy=1
        previous =0
        for  ch in s:
            if (ch<previous):
                tidy=0
                break
            previous=ch
        n=n-1
    n=n+1
    print ('case #'+str(cpt)+': '+ str(n))
