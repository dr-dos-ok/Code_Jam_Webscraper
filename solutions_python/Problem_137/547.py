from itertools import combinations
N = 5

def neighbours(R, C, r, c):
    ret = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if (dx, dy) == (0, 0):
                continue
            x = r + dx
            y = c + dy
            if x in range(R) and y in range(C):
                ret.append((x, y))
    return ret

def win(R, C, mines, start):
    if start in mines:
        return False
    done = []
    q = [start]
    while q:
        node = q.pop()
        done.append(node)
        naybs = neighbours(R, C, *node)
        if all(n not in mines for n in naybs):
            for n in naybs:
                if n not in done and n not in q:
                    q.append(n)
    return len(done) + len(mines) == R * C



def cell(r, c, mines, start):
    if (r, c) == start:
        return 'c'
    if (r, c) in mines:
        return '*'
    return '.'

def format(R, C, mines, start):
    return '\n' + '\n'.join(''.join(cell(r, c, mines, start) for c in range(C)) for r in range(R))


def solve(R, C, M):
    positions = [(r, c) for r in range(R) for c in range(C)]
    for mines in combinations(positions, M):
        for start in positions:
            if win(R, C, set(mines), start):
                return format(R, C, mines, start)
    return "\nImpossible"
d = {}

for R in range(1, N+1):
    for C in range(1, N+1):
        for M in range(R*C):
            pass
            # d[(R, C, M)] = solve(R, C, M)

# print d
d = {(4, 2, 2): '\n**\n..\nc.\n..', (5, 4, 14): '\n****\n****\n****\n*...\n*.c.', (5, 2, 7): '\nImpossible', (3, 5, 11): '\n*****\n***..\n***.c', (4, 4, 0): '\nc...\n....\n....\n....', (4, 5, 13): '\nImpossible', (5, 5, 1): '\n*.c..\n.....\n.....\n.....\n.....', (5, 4, 12): '\n****\n****\n****\n....\nc...', (5, 1, 1): '\n*\n.\nc\n.\n.', (1, 4, 2): '\n**.c', (2, 5, 9): '\n*****\n****c', (3, 5, 9): '\n*****\n**...\n**.c.', (4, 5, 15): '\nImpossible', (5, 5, 3): '\n***.c\n.....\n.....\n.....\n.....', (5, 2, 3): '\nImpossible', (1, 4, 0): '\nc...', (5, 5, 5): '\n*****\n.....\nc....\n.....\n.....', (3, 2, 2): '\n**\n..\nc.', (3, 5, 13): '\nImpossible', (1, 2, 0): '\nc.', (5, 5, 7): '\n*****\n**...\n...c.\n.....\n.....', (3, 1, 2): '\n*\n*\nc', (5, 1, 0): '\nc\n.\n.\n.\n.', (3, 2, 0): '\nc.\n..\n..', (2, 5, 3): '\nImpossible', (4, 5, 16): '\n*****\n*****\n***..\n***.c', (5, 4, 19): '\n****\n****\n****\n****\n***c', (5, 5, 9): '\n*****\n***..\n*...c\n.....\n.....', (3, 1, 0): '\nc\n.\n.', (5, 2, 9): '\n**\n**\n**\n**\n*c', (2, 5, 1): '\nImpossible', (4, 5, 18): '\nImpossible', (4, 1, 1): '\n*\n.\nc\n.', (5, 4, 3): '\n**.c\n*...\n....\n....\n....', (5, 5, 11): '\n*****\n*****\n*....\n..c..\n.....', (5, 3, 2): '\n*.c\n*..\n...\n...\n...', (3, 2, 4): '\nImpossible', (2, 5, 7): '\nImpossible', (4, 1, 3): '\n*\n*\n*\nc', (5, 5, 13): '\n*****\n*****\n***..\n....c\n.....', (5, 3, 0): '\nc..\n...\n...\n...\n...', (5, 1, 3): '\n*\n*\n*\n.\nc', (5, 4, 17): '\nImpossible', (2, 5, 5): '\nImpossible', (4, 3, 6): '\n***\n***\n...\nc..', (5, 5, 15): '\n*****\n*****\n*****\n.....\nc....', (5, 3, 6): '\n***\n***\n...\nc..\n...', (1, 5, 1): '\n*.c..', (3, 4, 5): '\nImpossible', (2, 3, 4): '\nImpossible', (5, 2, 1): '\nImpossible', (4, 3, 4): '\n***\n*..\n..c\n...', (5, 3, 4): '\n***\n*..\n..c\n...\n...', (1, 5, 3): '\n***.c', (3, 4, 7): '\nImpossible', (1, 3, 1): '\n*.c', (4, 5, 10): '\n*****\n*****\n.....\nc....', (4, 3, 2): '\n*.c\n*..\n...\n...', (5, 3, 10): '\nImpossible', (3, 3, 1): '\n*.c\n...\n...', (5, 1, 2): '\n*\n*\n.\nc\n.', (3, 4, 1): '\n*.c.\n....\n....', (2, 3, 0): '\nc..\n...', (4, 3, 0): '\nc..\n...\n...\n...', (5, 3, 8): '\nImpossible', (3, 3, 3): '\n***\n...\nc..', (2, 4, 0): '\nc...\n....', (4, 4, 15): '\n****\n****\n****\n***c', (3, 4, 3): '\n*.c.\n*...\n*...', (2, 3, 2): '\n*.c\n*..', (5, 5, 16): '\n*****\n*****\n**...\n**.c.\n**...', (5, 3, 14): '\n***\n***\n***\n***\n**c', (3, 3, 5): '\n***\n*..\n*.c', (2, 4, 2): '\n*.c.\n*...', (4, 4, 13): '\nImpossible', (4, 5, 0): '\nc....\n.....\n.....\n.....', (5, 5, 18): '\nImpossible', (4, 4, 6): '\n****\n**..\n...c\n....', (5, 3, 12): '\nImpossible', (3, 3, 7): '\nImpossible', (2, 4, 4): '\n**.c\n**..', (4, 4, 11): '\nImpossible', (4, 5, 2): '\n**.c.\n.....\n.....\n.....', (5, 5, 20): '\nImpossible', (4, 3, 10): '\nImpossible', (5, 4, 1): '\n*.c.\n....\n....\n....\n....', (2, 4, 6): '\nImpossible', (4, 4, 9): '\nImpossible', (3, 4, 9): '\nImpossible', (4, 5, 4): '\n***.c\n*....\n.....\n.....', (4, 2, 5): '\nImpossible', (5, 5, 22): '\nImpossible', (4, 3, 8): '\n***\n***\n*..\n*.c', (5, 4, 7): '\n****\n**..\n*..c\n....\n....', (3, 5, 2): '\n**.c.\n.....\n.....', (2, 2, 3): '\n**\n*c', (3, 4, 11): '\n****\n****\n***c', (4, 5, 6): '\n*****\n*....\n..c..\n.....', (4, 2, 7): '\n**\n**\n**\n*c', (1, 1, 0): '\nc', (5, 4, 5): '\n****\n*...\n..c.\n....\n....', (3, 5, 0): '\nc....\n.....\n.....', (2, 2, 1): '\nImpossible', (4, 5, 8): '\n*****\n***..\n....c\n.....', (2, 1, 1): '\n*\nc', (4, 2, 1): '\nImpossible', (5, 4, 11): '\n****\n****\n*...\n*.c.\n*...', (5, 2, 4): '\n**\n**\n..\nc.\n..', (3, 5, 6): '\n**.c.\n**...\n**...', (4, 4, 3): '\n**.c\n*...\n....\n....', (4, 4, 7): '\n****\n*...\n*.c.\n*...', (4, 2, 3): '\nImpossible', (5, 4, 9): '\n****\n****\n*...\n..c.\n....', (5, 2, 6): '\n**\n**\n**\n..\nc.', (3, 5, 4): '\n**.c.\n*....\n*....', (4, 4, 1): '\n*.c.\n....\n....\n....', (4, 5, 12): '\n*****\n*****\n*....\n*.c..', (5, 4, 15): '\nImpossible', (5, 2, 0): '\nc.\n..\n..\n..\n..', (2, 5, 8): '\nImpossible', (3, 5, 10): '\nImpossible', (4, 5, 14): '\n*****\n*****\n**...\n**.c.', (5, 5, 0): '\nc....\n.....\n.....\n.....\n.....', (5, 4, 13): '\nImpossible', (5, 2, 2): '\n**\n..\nc.\n..\n..', (1, 4, 3): '\n***c', (3, 5, 8): '\nImpossible', (5, 5, 2): '\n**.c.\n.....\n.....\n.....\n.....', (1, 4, 1): '\n*.c.', (3, 5, 14): '\n*****\n*****\n****c', (5, 5, 4): '\n***.c\n*....\n.....\n.....\n.....', (3, 2, 3): '\nImpossible', (2, 5, 2): '\n*.c..\n*....', (3, 5, 12): '\nImpossible', (1, 2, 1): '\n*c', (5, 4, 18): '\nImpossible', (5, 5, 6): '\n*****\n*....\n..c..\n.....\n.....', (3, 1, 1): '\n*\n.\nc', (5, 2, 8): '\nImpossible', (3, 2, 1): '\nImpossible', (2, 5, 0): '\nc....\n.....', (4, 5, 17): '\nImpossible', (5, 5, 24): '\n*****\n*****\n*****\n*****\n****c', (4, 1, 0): '\nc\n.\n.\n.', (5, 4, 16): '\n****\n****\n****\n**..\n**.c', (5, 5, 8): '\n*****\n***..\n....c\n.....\n.....', (5, 3, 3): '\n***\n...\nc..\n...\n...', (2, 5, 6): '\n***.c\n***..', (4, 5, 19): '\n*****\n*****\n*****\n****c', (4, 1, 2): '\n*\n*\n.\nc', (5, 5, 10): '\n*****\n*****\n.....\nc....\n.....', (5, 3, 1): '\n*.c\n...\n...\n...\n...', (1, 5, 4): '\n****c', (3, 2, 5): '\n**\n**\n*c', (2, 5, 4): '\n**.c.\n**...', (5, 5, 12): '\n*****\n*****\n**...\n...c.\n.....', (5, 3, 7): '\n***\n***\n*..\n..c\n...', (4, 4, 5): '\n****\n*...\n..c.\n....', (3, 4, 4): '\n****\n....\nc...', (4, 3, 7): '\nImpossible', (5, 5, 14): '\n*****\n*****\n**...\n*..c.\n*....', (5, 3, 5): '\n***\n*..\n*.c\n...\n...', (1, 5, 0): '\nc....', (3, 4, 6): '\n****\n*...\n*.c.', (2, 3, 5): '\n***\n**c', (1, 3, 2): '\n**c', (4, 3, 5): '\nImpossible', (5, 3, 11): '\n***\n***\n***\n*..\n*.c', (1, 5, 2): '\n**.c.', (3, 4, 0): '\nc...\n....\n....', (1, 3, 0): '\nc..', (4, 3, 3): '\n***\n...\nc..\n...', (5, 1, 4): '\n*\n*\n*\n*\nc', (5, 3, 9): '\n***\n***\n***\n...\nc..', (3, 3, 0): '\nc..\n...\n...', (2, 4, 1): '\nImpossible', (4, 4, 4): '\n****\n....\nc...\n....', (3, 4, 2): '\n**.c\n....\n....', (2, 3, 1): '\nImpossible', (5, 5, 17): '\n*****\n*****\n*****\n*....\n*.c..', (4, 3, 1): '\n*.c\n...\n...\n...', (3, 3, 2): '\nImpossible', (2, 4, 3): '\nImpossible', (4, 4, 14): '\nImpossible', (2, 3, 3): '\nImpossible', (5, 5, 19): '\n*****\n*****\n*****\n**...\n**.c.', (5, 4, 2): '\n**.c\n....\n....\n....\n....', (5, 3, 13): '\nImpossible', (3, 3, 4): '\nImpossible', (2, 4, 5): '\nImpossible', (4, 4, 12): '\n****\n****\n**..\n**.c', (4, 5, 1): '\n*.c..\n.....\n.....\n.....', (5, 5, 21): '\n*****\n*****\n*****\n***..\n***.c', (5, 4, 0): '\nc...\n....\n....\n....\n....', (3, 3, 6): '\nImpossible', (2, 4, 7): '\n****\n***c', (4, 4, 10): '\n****\n****\n*...\n*.c.', (3, 4, 8): '\n****\n**..\n**.c', (4, 5, 3): '\n***.c\n.....\n.....\n.....', (5, 5, 23): '\nImpossible', (4, 3, 11): '\n***\n***\n***\n**c', (5, 4, 6): '\n****\n**..\n...c\n....\n....', (3, 3, 8): '\n***\n***\n**c', (3, 5, 3): '\n***.c\n.....\n.....', (4, 4, 8): '\n****\n****\n....\nc...', (3, 4, 10): '\nImpossible', (4, 5, 5): '\n*****\n.....\nc....\n.....', (4, 2, 4): '\n**\n**\n..\nc.', (4, 3, 9): '\nImpossible', (5, 4, 4): '\n****\n....\nc...\n....\n....', (3, 5, 1): '\n*.c..\n.....\n.....', (2, 2, 2): '\nImpossible', (4, 5, 7): '\n*****\n**...\n...c.\n.....', (2, 1, 0): '\nc\n.', (4, 2, 6): '\nImpossible', (5, 4, 10): '\n****\n****\n**..\n...c\n....', (3, 5, 7): '\n*****\n*....\n*.c..', (2, 2, 0): '\nc.\n..', (4, 5, 9): '\n*****\n**...\n*..c.\n*....', (4, 2, 0): '\nc.\n..\n..\n..', (5, 4, 8): '\n****\n****\n....\nc...\n....', (5, 2, 5): '\nImpossible', (3, 5, 5): '\n*****\n.....\nc....', (4, 4, 2): '\n**.c\n....\n....\n....', (4, 5, 11): '\n*****\n**...\n**.c.\n**...'}
T = int(raw_input())
for case_num in range(1, T+1):
    R, C, M = map(int, raw_input().split())
    print "Case #%d:%s" % (case_num, d[(R, C, M)])
