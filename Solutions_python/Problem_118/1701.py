#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Problem

Little John likes palindromes, and thinks them to be fair (which is a fancy word for nice). A palindrome is just a number that reads the same backwards and forwards - so 6, 11 and 121 are all palindromes, while 12, 223 and 2244 are not.

He recently became interested in squares as well, and formed the definition of a fair and square number - it is a number that is a palindrome and a square of a palindrome at the same time. For instance, 1, 9 and 121 are fair and square (being palindromes and squares, respectively, of 1, 3 and 11), while 16, 22 and 676 are not fair and square - the first is not a palindrome, the second is not a square, and the third is a square, but not a square of a palindrome.

Now he wants to search for bigger fair and square numbers. Your task is, given an interval Little John is searching through, to tell him how many fair and square numbers are there in the interval, so he knows when he has found them all.

Solving this problem

Usually, Google Code Jam problems have 1 Small input and 1 Large input. This problem has 1 Small input and 2 Large inputs. Once you have solved the Small input, you will be able to download any of the two Large inputs. As usual, you will be able to retry the Small input (with a time penalty), while you will get only one chance at each of the Large inputs.

Input

The first line of the input gives the number of test cases, T. T lines follow. Each lines contains two numbers, A and B - the endpoints of the interval Little John is looking at.

Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the number of fair and square numbers greater or equal to A and smaller or equal than B.

Limits

Small dataset

1 ≤ T ≤ 100.
1 ≤ A ≤ B ≤ 1000.

First large dataset

1 ≤ T ≤ 10000.
1 ≤ A ≤ B ≤ 1014.

Second large dataset

1 ≤ T ≤ 1000.
1 ≤ A ≤ B ≤ 10100.

Sample


Input 
3
1 4
10 120
100 1000

Output 
Case #1: 2
Case #2: 0
Case #3: 2
"""
import sys
import math

def is_palindromes(tt):
    for i in range(len(tt)/2):
        if tt[i] != tt[-(i+1)]:
            return False
    return True

pp = []
i = 1
MAX = math.pow(10, 14)
while i <= math.trunc(math.sqrt(MAX)):
    if is_palindromes(str(i)):
        pp.append(i*i)
    i+=1

def ans(a, b):
    c = 0
    for p in pp:
        if a <= p <= b and is_palindromes(str(p)):
            c += 1
    return c


with open(sys.argv[1]) as fr, open('c.out', 'w') as fw:
    T = int(fr.readline())
    for i in range(T):
        no = i+1
        (a, b) = map(int, fr.readline().split(' '))
        fw.write("Case #{no}: {ans}\n".format(no=no,ans=ans(a, b)))


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4