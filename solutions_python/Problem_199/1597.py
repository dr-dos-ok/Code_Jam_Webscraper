def a (fname):
    fin = open(fname + ".in")
    lines = fin.readlines()
    T = int(lines[0])
    fout = open(fname + ".out", "w")
    for t in range(1, T+1):
        line = lines[t].split(" ")
        stack = [(c == "+") for c in line[0]]
        size = int(line[1])
        fout.write("Case #" + str(t) + ": " + str(flips(stack, size)) + "\n")
        print(t)

def flips(stack, size):
    print(stack)
    if False not in stack:
        return 0
    for i in range(len(stack)):
        if len(stack)-i < size:
            return "IMPOSSIBLE"
        if not stack[i]:
            next = flips(list([not b for b in stack[i+1:i+size]]) + list(stack[i+size:]), size)
            if next == "IMPOSSIBLE":
                return "IMPOSSIBLE"
            return next + 1
def sheep(N):
    print (N)
    if N == 0:
        return "INSOMNIA"
    digits = [0,0,0,0,0,0,0,0,0,0]
    i = 1
    while 0 in digits:
        s = str(i*N)
        for c in s:
            j = int(c)
            if digits[j] == 0:
                digits[j] = int(s)
                print(digits)
        i = i + 1
        # input()
    return s


def b (fname):
    fin = open(fname + ".in")
    lines = fin.readlines()
    T = int(lines[0])
    fout = open(fname + ".out", "w")
    for t in range(1, T+1):
        line = lines[t]
        stack = [(c == "+") for c in line[:-1]]
        fout.write("Case #" + str(t) + ": " + str(flips(stack)) + "\n")
        print(t)



def c (fname):
    fin = open(fname + ".in")
    lines = fin.readlines()
    T = int(lines[0])
    fout = open(fname + ".out", "w")
    for t in range(1, T+1):
        l1 = lines[t].split()
        print(l1)
        n = int(l1[0])
        j = int(l1[1])
        fout.write("Case #" + str(t) + ":\n")
        print("Case #" + str(t) + ":")
        j0 = 0
        for i in range(j):
            j1, s = jamcoin(j0, n)
            print(str(i)+": " + s)
            fout.write(s)
            j0 = j1 + 1

def jamcoin(j, n):
    b = bin(j)[2:]
    s = "1" + ("0"*(n-2-len(b))) + b + "1"
    fs = []
    for base in range(2, 11):
        prime, f = isprime(int(s, base))
        if prime:
            return jamcoin(j+1,n)
        fs.append(f)
    sfs = s + " " + " ".join([str(f) for f in fs])+ "\n"
    return j, sfs

primes_db = {}

def isprime(n):
    if n <= 1:
        return False
    if n in primes_db:
        return primes_db[n]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            primes_db[n] = False, i
            return False, i
    primes_db[n] = True, ""
    return True, ""

def d (fname):
    fin = open(fname + ".in")
    lines = fin.readlines()
    T = int(lines[0])
    fout = open(fname + ".out", "w")
    for t in range(1, T+1):
        l1 = lines[t].split()
        k = int(l1[0])
        c = int(l1[1])
        s = int(l1[2])
        fout.write("Case #" + str(t) + ": ")
        print ("Case #" + str(t) + ":")
        fout.write(fractile(k,c,s))
        fout.write("\n")

def fractile(k,c,s):
    if s >= k:
        ts = [str(n*(k**(c-1)) + 1) for n in range(k)]
        print(ts)
        return " ".join(ts)
    return "IMPOSSIBLE"
