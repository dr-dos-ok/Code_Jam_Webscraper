from __future__ import division, print_function

import itertools
import sys


def solve():
    """Solve."""
    629
    599
    def check(num):
        for i in xrange(1, len(num)):
            if num[i - 1] < num[i]:
                return False
        return True

    def decrease(num, i, l, m):
        while i < l and num[i] in (0, 1):
            num[i] = m
            i += 1
        if i == l:
            l -= 1
        else:
            num[i] -= 1
        return l

    number = read_int_array(sep='')[::-1]
    if check(number):
        return ''.join(str(n) for n in number)[::-1]
    i = 0
    l = len(number)
    while i < l:
        j = i
        while j + 1 < l:
            if number[j] >= number[j + 1]:
                j += 1
            else:
                break
        if j + 1 == l:
            break
        number[i:j + 1] = [9 if i == 0 else number[i - 1]] * (j + 1 - i)
        l = decrease(number, j + 1, l, number[i])
        i = j + 1
    return ''.join(str(n) for n in number[:l])[::-1]


def main():
    for i in range(1, read_int() + 1):
        write('Case #{}: {}'.format(i, solve()))
        # write('Case #{}: '.format(i), end='')
        # solve()


def bye(message=None):
    if message is not None:
        write(message)
    sys.exit()


def times(n):
    return itertools.repeat(None, n)


def read(func=None):
    a = sys.stdin.readline().rstrip('\n')
    return a if func is None else func(a)


def read_array(func=None, sep=None, max_split=-1):
    array = read().split(sep, max_split) if sep != '' else list(read())
    return array if func is None else [func(a) for a in array]


def read_2d_array(n, func=None, sep=None, max_split=-1):
    return [read_array(func, sep, max_split) for _ in times(n)]


def read_int():
    """:rtype: int"""
    return read(int)


def read_int_array(sep=None, max_split=-1):
    """:rtype: list[int]"""
    return read_array(int, sep, max_split)


def read_int_2d_array(n, sep=None, max_split=-1):
    """:rtype: list[list[int]]"""
    return read_2d_array(n, int, sep, max_split)


def write(*args, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    sys.stdout.write(sep.join(str(a) for a in args) + end)


def write_array(array, **kwargs):
    write(*array, **kwargs)


def write_2d_array(array, **kwargs):
    [write_array(a, **kwargs) for a in array]


def _main_():
    name = ''  # fill with a name of a problem
    names = False  # fill with True
    if name or names:
        in_name = (name + '.in') if name else 'input.txt'
        out_name = (name + '.out') if name else 'output.txt'
        stdin = sys.stdin
        stdout = sys.stdout
        sys.stdin = open(in_name)
        sys.stdout = open(out_name, 'w')
        try:
            main()
        finally:
            sys.stdin.close()
            sys.stdout.close()
            sys.stdin = stdin
            sys.stdout = stdout
    else:
        main()


_main_()
