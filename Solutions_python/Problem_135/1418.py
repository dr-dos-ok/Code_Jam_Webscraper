print('\n'.join('Case #{}: {}'.format(case+1, (lambda a: a.pop() if len(a) == 1 else 'Volunteer cheated!' if not a else 'Bad magician!')(set((lambda a, m: m[a-1])(int(input()), [[int(n) for n in input().split()] for _ in range(4)])) & set((lambda a, m: m[a-1])(int(input()), [[int(n) for n in input().split()] for _ in range(4)])))) for case in range(int(input()))))