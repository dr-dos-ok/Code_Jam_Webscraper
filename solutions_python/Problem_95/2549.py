#!/usr/bin/python3

table = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o',
         'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x',
         'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k',
         'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't',
         'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a',
         'x': 'm', 'z': 'q'}
table = str.maketrans(table)

for i in range(1, int(input()) + 1):
    print('Case #{}: {}'.format(i, input().translate(table)))
