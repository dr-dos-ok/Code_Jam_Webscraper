# -*- coding: utf-8 -*-

def iswon(board, s):
    s3t = sorted(s * 3 + 'T')
    for i in xrange(0, 4):
        if sorted(board[i]) == s3t or board[i] == [s] * 4:
            return True
        h = sorted([board[e][i] for e in xrange(0, 4)])
        if h == s3t or h == [s] * 4:
            return True
    h = sorted([board[i][i] for i in xrange(0, 4)])
    if h == s3t or h == [s] * 4:
        return True
    h = sorted([board[i][3-i] for i in xrange(0, 4)])
    if h == s3t or h == [s] * 4:
        return True
    return False
    
def solve(board):
    if iswon(board, 'X'):
        return 'X won'
    if iswon(board, 'O'):
        return 'O won'
    for e in board:
        if '.' in e:
            return 'Game has not completed'
    return 'Draw'

if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t+1):
        board = []
        for j in xrange(0, 4):
            board.append(list(raw_input()))
        print 'Case #%d:' % i, solve(board)
        raw_input()
