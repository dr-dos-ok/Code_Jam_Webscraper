import math

def usqrt(x):
  s = int(math.sqrt(x))
  if s*s < x:
    s += 1
  return s

def lsqrt(x):
  s = int(math.sqrt(x))
  if s*s > x:
    s -= 1
  return s

cache = [0, 1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002]

t = int(raw_input())
for ti in xrange(1, t+1):
  ra,rb = [int(i) for i in raw_input().split(" ")[:2]]
  a,b = usqrt(ra),lsqrt(rb)
  cnt = 0
  for i in cache:
    if a <= i <= b:
      cnt += 1
  print "Case #%d: %d" % (ti, cnt)

