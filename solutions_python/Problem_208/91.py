#!/usr/bin/env python3

import sys,time, math
cin=sys.stdin
cerr=sys.stderr
cout=sys.stdout

def rl(cin):
	"""readline and remove \n"""
	return cin.readline()[:-1]
cin.rl=lambda:rl(cin)
def rs(cin):
	return cin.rl().split()
cin.rs=lambda:rs(cin)
def ri(cin):
	return int(cin.rl())
cin.ri=lambda:ri(cin)
def riv(cin):
	return [int(x) for x in rs(cin)]
cin.riv=lambda:riv(cin)
def rf(cin):
	return float(cin.rl())
cin.rf=lambda:rf(cin)
def rfv(cin):
	return [float(x) for x in rs(cin)]
cin.rfv=lambda:rfv(cin)
def rev(i):
	o=[]	
	for x in range(1,1+len(i)): o+=[i[-x]]
	return o
def revs(s):
	return ''.join(rev(s))	
def isPrime(n):
	for i in range(2, int(math.sqrt(n))):
		if not i%n:
			return true
		
def printr(*args):
	cerr.write(', '.join([repr(x) for x in args])+'\n')
		
class bin_base:
	def __init__(self):
		pass
	def up(self):
		pass
	def lo(self):
		pass
	def cont(self):
		pass
class bin_int:
	def __init__(self, m=0, M=10):
		self.m=m-1
		self.M=M+1
		self.c=int((self.M+self.m)/2)
	def up(self):
		self.m=self.c+1
		self.c=int((self.M+self.m)/2)
		return self.c
	def lo(self):
		self.M=self.c
		self.c=int((self.m+self.M)/2)
		return self.c
	def cont(self):
		return self.m < self.M

def search(r, k, pred):
	while r.cont():
		pre=pred(r.c)
		if pre < k:
			r.up()
		else:
			r.lo()
	return r.m

def step(n, t, i, ce, cs, e, s, d, mc = 0):
	printr(t, i, ce, cs)
	if i == n-1: return t
	t1 = -1
	t2 = -1
	if ce < d[i][i+1] and e[i] < d[i][i+1]: return -1
	if not (e[i] >= ce and s[i] >= cs) and ce >= d[i][i+1]:
			t1 = step(n,t+d[i][i+1]/cs, i+1,ce - d[i][i+1],cs, e,s,d )
	if not (e[i] < ce and s[i] < cs) and e[i] >= d[i][i+1]:
		t2 = step(n,t+d[i][i+1]/s[i], i+1, e[i] - d[i][i+1],s[i], e,s,d )
	if t1 == -1 and t2 == -1: return -1
	if t1 == -1: return t2
	if t2 == -1: return t1
	return min(t1,t2)

def do(l):
	n, q = l.riv()
	e = []
	s = []
	d = []
	uv = []
	for i in range(n):
		ei, si = l.riv()
		e += [float(ei)]
		s += [float(si)]
	for i in range(n):
		d += [[float(x) for x in l.riv()]] 
	for i in range(q):
		ui,vi = l.riv()
		uv += [(ui,vi)]
	printr(n,q,e,s,d,uv)

	# small
	r = step(n, float(0), 0, e[0],s[0],e,s,d,0)
	printr(r)
	return r

def main():
	start = time.time()
	T=cin.ri()
	cerr.write("Going to process {} cases\n".format(T))
	k=0
	for Ti in range(1,T+1):
		if math.log(100*Ti/T) > k:
			cerr.write("case {}...".format(Ti))
		print("case #{0}: {1:0.8f}".format(Ti, do(sys.stdin)))
		if math.log(100*Ti/T) > k:
			k+=1
			cerr.write("duration {}\n".format(time.time()-start))
	cerr.write("duration {0}\n".format(time.time()-start))

if __name__=="__main__":
	main()
