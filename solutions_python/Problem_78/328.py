#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import sys

max = 100000

def solve(f):
   res = "" 
   lst = []
   lst.append([int(x) for x in f.readline().split()])
   N = 0
   Pd = 0
   Pg = 0 
   for i in lst:
      N  = i[0]
      Pd = i[1]/100.
      Pg = i[2]/100.
   
   if Pg == 0. and Pd != 0.:
      res = "Broken"
   elif Pg == 0. and Pd == 0.:
      res = "Possible" 
   elif (Pd * N)
   else:
      y1 = ((N*Pd) + 1)/Pg - N
      y2 = ((N*Pd) + N)/Pg - N
      y3 = ((N*Pd) + max)/Pg - N
      #print y1, y2, y3
      #print "...."
      #print 1, N, max
      if ((y1 >= 1) or (y2 >= N) or (y3 >= max)):
      #if (y1 >= 1):
         res = "Possible"
      else:
         res = "Broken" 
   #print N, Pd, Pg
   return  res



f = sys.stdin
n = int(f.readline())

for i in xrange(n):
   res = solve(f)
   print "Case #%d: %s" % (i+1, res)
