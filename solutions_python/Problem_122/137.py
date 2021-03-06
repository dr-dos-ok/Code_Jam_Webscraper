from functools import *
import math

def end(t):
  print('Case #' + str(t) + ':')

#3 numbers
#[2,5] inclusive
#50% correct needed
#k=7 products given
#products generated by filter 50% and product()
perms = []
for a in range(2,6):
  for b in range(a,6):
    for c in range(b,6):
      perms.append([a,b,c])

perm_prods = []
for p in perms:
  [a,b,c] = p
  prods = []
  for x in range(2):
    for y in range(2):
      for z in range(2):
        prod = 1
        if x:
          prod *= a
        if y:
          prod *= b
        if z:
          prod *= c
        if prod > 0:
          prods.append(prod)
  perm_prods.append(prods)

cand_master = []
for i in range(20):
  cand_master.append(i)

testcases = int(input())
end(1)
for tc in range(1, testcases + 1):
  R,N,M,K = [int(x) for x in input().split()]
  for i in range(R):
    r = [int(x) for x in input().split()]
    cands = cand_master.copy()
    for prod in r:
      removal = []
      for cand in cands:
        if not prod in perm_prods[cand]:
          removal.append(cand)
      for cand in removal:
        cands.remove(cand)
    
    guess = cands[0]

    for x in perms[guess]:
      print(str(x), end='')
    print('')
