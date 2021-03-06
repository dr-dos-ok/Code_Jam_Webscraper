#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Dmytro Molkov on 2012-04-13.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os

inputs="""1093511 1940159
1023198 1917935
1091602 1911396
15 90
1063789 1917758
1099875 1995724
127123 897627
1065722 1941466
1041702 1948957
1000 9999
29 91
1 2
1062320 1225196
208202 469003
1339192 1646742
3 7
60419 94960
1056573 1991476
1082509 1942986
2032 7318
1453688 1479157
287761 501777
602573 753886
1063264 1924579
1042807 1968910
3146 8603
1093872 1998310
3545 9581
910132 910132
20153 23619
709 973
1042751 1996838
1000000 1000000
1062906 1978968
1652526 1652526
1366914 1456113
2131 9640
1018848 1922589
1081954 1911414
111 455
23859 70077
1359459 1410140
100000 999999
892665 968131
17639 36672
1017504 1933836
1532091 1661634
676 700
520575 845623
44522 55605"""

def main():
    inlines = inputs.split("\n")
    case = 0
    total = 0
    for line in inlines:
        case += 1
        input_pair =line.strip().split(" ")
        A = int(input_pair[0])
        B = int(input_pair[1])
        
        ans = 0
        for i in range(A, B+1):
            inext = str(i)
            inext = inext[-1] + inext[:-1]
            while int(inext) != i:
                inext_n = int(inext)
                if inext_n <= B and inext_n >= A and inext_n > i:
                    ans += 1
                inext = inext[-1] + inext[:-1]
        print "Case #" + str(case) + ": " + str(ans)

if __name__ == '__main__':
    main()

