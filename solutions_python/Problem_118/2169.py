'''
import itertools
def add2(n):
    s = str(n)
    if s[0]=='1':
        return [int('{}0{}0{}'.format(s[0],s[1:-1],s[-1])),
                int('{}1{}1{}'.format(s[0],s[1:-1],s[-1]))]
    elif s[0]=='2':
        return [int('{}0{}0{}'.format(s[0],s[1:-1],s[-1]))]
ns = [[1,2,3,11,22], [101, 111, 121, 202, 212, 1001, 1111, 2002]]
while len(str(ns[-1][-1]))<8:
    ns.append(list(itertools.chain(*map(add2,ns[-1]))))

nss = list(map((2).__rpow__, itertools.chain(*ns)))
'''

nss = [
 1,
 4,
 9,
 121,
 484,
 10201,
 12321,
 14641,
 40804,
 44944,
 1002001,
 1234321,
 4008004,
 100020001,
 102030201,
 104060401,
 121242121,
 123454321,
 125686521,
 400080004,
 404090404,
 10000200001,
 10221412201,
 12102420121,
 12345654321,
 40000800004,
 1000002000001,
 1002003002001,
 1004006004001,
 1020304030201,
 1022325232201,
 1024348434201,
 1210024200121,
 1212225222121,
 1214428244121,
 1232346432321,
 1234567654321,
 1236790876321,
 4000008000004,
 4004009004004,
]

def count(a,b):
    return sum(map(range(a,b+1).__contains__, nss))

fin=open('C-small-attempt1.in')
T=next(fin)
for i, line in enumerate(fin, 1):
    a,b = map(int, line.split())
    print("Case #{}:".format(i), count(a,b))
    