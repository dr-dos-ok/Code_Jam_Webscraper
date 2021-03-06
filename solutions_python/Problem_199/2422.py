

def problem_a():
    nb_tests = int(input())

    for i in range(1, nb_tests+1):
        nb_flips = 0
        feasible = True
        (state, k) = input().split()
        k = int(k)
        state = list(state)
        nb_pan = len(state)
        state = [1 if c == '+' else 0 for c in state]
        for j in range(0, nb_pan-k+1):
            if not state[j]:
                nb_flips += 1
                for aux in range(j+1, j+k):
                    state[aux] = 1 - state[aux]

        for j in range(nb_pan - k + 1, nb_pan):
            if not state[j]:
                feasible = False
                break
        if feasible:
            print("Case #%d: %d" % (i, nb_flips))
        else:
            print("Case #%d: IMPOSSIBLE" % i)

problem_a()
