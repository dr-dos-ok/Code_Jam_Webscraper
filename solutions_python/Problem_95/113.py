#!/usr/bin/python2

from sys import stdin

kv = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', 'q':'z'}

n = int(stdin.readline())
for i in xrange(1, n+1):
  inp = stdin.readline().strip()
  res = ''.join(kv[c] for c in inp)

  print 'Case #%d: %s' % (i, res)
