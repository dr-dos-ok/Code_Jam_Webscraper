def pal(k):
    r, kp = 0, k
    while kp > 0:
        r *= 10
        r += kp % 10
        kp //= 10
    return k == r

#squares = [k*k  for k in range(0, 10000000) if pal(k) and pal(k*k)]
squares = [0, 1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004]

f = open('C-large-1.in', 'r')
w = open('out.txt', 'w')

case = 1
for line in f.readlines()[1:]:
    line = [int(k) for k in line.split()]
    size = len([1 for k in squares if k >= line[0] and k <= line[1]])
    w.write('Case #' + str(case) + ": " + str(size) + '\n')
    case += 1

f.close()
w.close()