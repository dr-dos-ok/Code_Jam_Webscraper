#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==============================================================================
from __future__ import unicode_literals


# ==============================================================================
def find_fault(n):
    """Find and return the index of the faulty one."""
    for i in xrange(1, len(n)):
        if n[i] < n[i - 1]:
            return i
    return None


def solve():
    """Problem solution implementation."""
    n = list(str(int(raw_input().strip())))  # str(int()) to remove any leading zeros
    n = [int(d) for d in n]
    f = find_fault(n)
    while f is not None:
        n[f - 1] -= 1
        for i in xrange(f, len(n)):
            n[i] = 9
        f = find_fault(n)
    return str(int(''.join(str(d) for d in n)))


# ==============================================================================
if __name__ == '__main__':
    test_cases = int(raw_input())
    for t in xrange(1, test_cases + 1):
        print('Case #{}: {}'.format(t, solve()))
