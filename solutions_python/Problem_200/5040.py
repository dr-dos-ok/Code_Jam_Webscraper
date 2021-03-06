#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:09:08 2017

@author: psalm
"""

def is_sorted(n: int) -> int:
    digits = [int(d) for d in str(n)]
    if len(digits) == 1:
        return True
    else:
        k = 1
        while k < len(digits):
            if digits[k-1] > digits[k]:
                return False
            else:
                k += 1
        return True
    
    
def find_last_tidy(n: int) -> int:
    num = n
    while not is_sorted(num):
        num -= 1
    return(num)
    

#t = int(input())
t = 100
inputs = [132,
1000,
7,
879,
110,
257,
585,
550,
449,
887,
376,
176,
953,
441,
769,
821,
886,
999,
950,
519,
21,
795,
902,
213,
586,
684,
43,
900,
485,
100,
656,
693,
818,
530,
814,
428,
130,
451,
766,
913,
874,
747,
823,
194,
632,
128,
306,
654,
409,
819,
525,
205,
574,
788,
203,
215,
476,
263,
277,
87,
702,
411,
3,
440,
472,
32,
225,
541,
513,
518,
563,
52,
599,
507,
778,
534,
317,
841,
794,
326,
363,
265,
593,
231,
391,
882,
711,
242,
597,
714,
801,
688,
1,
196,
402,
351,
294,
344,
835,
740]
for i in range(1,t+1):
#    N = int(input())
    N = inputs[i-1]
    last_tidy = find_last_tidy(N)
    print("Case #{}: {}".format(i, last_tidy))