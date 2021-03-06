PK     �i�Dm�ǀ,  ,     Code.py#!C:\Python33\python
from decimal import *
import sys
import fileinput

sys.path.append(r'D:\Data\Programming\Python\Libraries')
from PeterJam import *
from PeterData import *
from PeterMath import *

def main ():
	lines = fileinput.input()
	cases = int(lines.readline())
	for case in range(1, cases + 1):
		prec = 5
		getcontext().prec = 10
		cost, increase, victory = readType(lines.readline(), Decimal)
		seconds = 0
		cps = Decimal(2)
		while True:
			#calculate time to win
			timeToWin = victory / cps
			
			#calculate time to win after buying another farm
			timeToGetFarm = cost / cps
			timeToWinFarm =  timeToGetFarm + victory / (cps + increase)
			
			#if another farm is better add time to farm to seconds and increase to cps
			if timeToWin > timeToWinFarm:
				seconds += timeToGetFarm
				cps += increase
				
			#if win is better answer is seconds + time to win and break
			elif timeToWin <= timeToWinFarm:
				seconds += timeToWin
				break
			
			
		print ("Case #{0}: {1}".format(case, seconds))
		
main()
PK     kf�D���  �     PeterData.py#!C:\Python33\python
import numpy
import collections
import functools
import itertools

def alternateChain(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # Recipe credited to George Sakkis
    pending = len(iterables)
    nexts = itertools.cycle(iter(it).__next__ for it in iterables)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = itertools.cycle(itertools.islice(nexts, pending))
			
def getInRange(iterable, start, end):
	return itertools.dropwhile(lambda x: x < start, itertools.takewhile(lambda x: x <= end, iterable))
	
def grouper(n, iterable, padvalue=None):
    "grouper(3, 'abcdefg', 'x') --> ('a','b','c'), ('d','e','f'), ('g','x','x')"
    return zip(*[itertools.chain(iterable, itertools.repeat(padvalue, n-1))]*n)
	
def getFirstChange (gen1, gen2):
	for a, b in zip(gen1, gen2):
		if a != b:
			return (a, b)
	
def getIndices (gen, indices):
	largest = max(indices)
	for i, result in enumerate(gen):
		if i > largest:
			break
			
		if i in indices:
			yield result
	
class Cached:
   def __init__(self, func):
      self.func = func
      self.cache = {}
	  
   def __call__(self, *args):
      if not isinstance(args, collections.Hashable):
         return self.func(*args)
		 
      if args in self.cache:
         return self.cache[args]
		 
      else:
         value = self.func(*args)
         self.cache[args] = value
         return value
		 
   def __repr__(self):
      return self.func.__doc__
	  
   def __get__(self, obj, objtype):
      return functools.partial(self.__call__, obj)
	  
def getLength (gen):
	result = 0
	for _ in gen:
		result += 1
	
	return result
	
def getDiagonals (array):
	diags = [array[::-1,:].diagonal(i) for i in range(-array.shape[0]+1, array.shape[1])]
	diags.extend(array.diagonal(i) for i in range(array.shape[1]-1,-array.shape[0],-1))
	
	return diags
	
def getDiagonalIndices (array):
	diags = [array[::-1,:].diag_indices(i) for i in range(-array.shape[0]+1, array.shape[1])]
	diags.extend(array.diag_indices(i) for i in range(array.shape[1]-1,-array.shape[0],-1))
	
	return diags
	
def convertWord (n, useHyphen = True):
	single = {
		"0": "zero",
		"1": "one",
		"2": "two",
		"3": "three",
		"4": "four",
		"5": "five",
		"6": "six",
		"7": "seven",
		"8": "eight",
		"9": "nine",
	}
	
	double = {
		"2": "twenty",
		"3": "thirty",
		"4": "forty",
		"5": "fifty",
		"6": "sixty",
		"7": "seventy",
		"8": "eighty",
		"9": "ninety",
	}
	
	teens = {
		"0": "ten",
		"1": "eleven",
		"2": "twelve",
		"3": "thirteen",
		"4": "fourteen",
		"5": "fifteen",
		"6": "sixteen",
		"7": "seventeen",
		"8": "eighteen",
		"9": "nineteen",
	}
	
	rest = ["thousand", "million", "billion", "trillion"]
	hyphen = "-" if useHyphen else " "
	number = str(n).lstrip("0")
	
	if number == "":
		return "zero"
	
	if len(number) == 1:
		return single[number[0]]
		
	if len(number) == 2:
		if number[0] == "1":	
			return teens[number[1]]
		
		else:
			last = single[number[1]]
			if last == "zero":
				return double[number[0]]
				
			else:
				return double[number[0]] + hyphen + last
			
	if len(number) == 3:
		sub = convertWord(number[1:], useHyphen)

		if sub == "zero":
			return single[number[0]] + " hundred"
		
		else:
			return single[number[0]] + " hundred and " + sub
				
	
	word = ""
	if number[-3:] == "0" * 3:
		hundred = ""
		
	else:
		hundred = convertWord(number[-3:], useHyphen)
		if number[-3] == "0":
			hundred = "and " + hundred
		
	number = number[:-3]
	current = 0
	parts = []
	for i in range(iDivUp(len(number), 3)):
		parts.append(convertWord(number[-3:], useHyphen) + " " + rest[current] + " ")
		number = number[:-3]
		current += 1
	
	return ("".join(reversed(parts)) + hundred).strip()		
			PK     jh�D��1�  �     PeterJam.py#!C:\Python33\python
	
debug = True
def setDebug (value):
	global debug
	debug = value
	
def printDebug (string):
	global debug
	if debug:
		print (string)
	
def splitPath (path):
	if path[-1] == "/":
		path = path[0:-1]
	
	folders = []
	while True:
		path,folder = os.path.split(path)
			
		if folder != "":
			folders.append(folder)
			
		else:
			if path != "":
				folders.append(path)
				
			break

	folders.reverse()
	return folders[1:]
	
def readInts (line):
	return tuple(int(x) for x in line.strip().split())
	
def readTypes (line, *args):
	return tuple(args[i](x) for x, i in enumerate(line.strip().split(" ")))
	
def readType (line, arg):
	return tuple(arg(x) for x in line.strip().split(" "))
	
	
PK     frnCn-0       PeterMath.py#!C:\Python33\python
import numpy
import PeterData
import math
import gmpy2
import string
import random
import itertools
from functools import reduce
romanNumeralMap = {
	"I": 1, 
	"IV": 4, 
	"V": 5, 
	"IX": 9, 
	"X": 10, 
	"XL": 40, 
	"L": 50, 
	"XC":90, 
	"C": 100,
	"CD": 400,
	"D": 500, 
	"CM": 900,
	"M": 1000
}
romanNumerals = [item[0] for item in sorted(romanNumeralMap.items(), key=lambda item: item[1])]

def fromRoman (s):
	n = 0
	previous = None
	for i in range(len(s) - 1, -1, -1):
		if previous == None or previous <= romanNumeralMap[s[i]]:
			n += romanNumeralMap[s[i]]
		
		else:
			n -= romanNumeralMap[s[i]]
			
		previous = romanNumeralMap[s[i]]
		
	return n
	
def toRoman (n):
	s = ""
	while n > 0:
		for i in range(len(romanNumerals) - 1, -1, -1):
			if n >= romanNumeralMap[romanNumerals[i]]:
				s += romanNumerals[i]
				n -= romanNumeralMap[romanNumerals[i]]
				break
				
	return s
			
	
def generateEulerCF ():
	x = 2
	while True:
		yield 1
		yield x
		yield 1
		x += 2
		
def getConvergents(start, seq):
	seq = list(seq)
	for i in range(1, len(seq)):
		yield getConvergent(start, seq[:i])
	
def getConvergent(start, seq):
	seq = list(seq)
	frac = None
	for n in reversed(seq):
		if frac:
			frac = 1 / (n + frac)
			
		else:
			frac = gmpy2.mpq(1, n)
	
	return start + frac
	
def getPeriod (s):
	if not gmpy2.is_square (s):
		m = 0
		d = 1
		a = gmpy2.isqrt(s)
		start = a
		done = set(((m, d, a),))
		while True:
			yield a
			m = d * a - m
			d = (s - m ** 2) // d
			a = (start + m) // d
			triplet = (m, d, a)
			if triplet in done:
				break
			
			done.add(triplet)
			
def generatePolygons (s):
	for n in itertools.count(1):
		yield getPolygon(s, n)

def getPolygon (s, n):
	return (n ** 2 * (s - 2) - n * (s - 4)) // 2
	
def generatePrimes():
    D = { 9: 3, 25: 5 }
    yield 2
    yield 3
    yield 5
    MASK= 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
    MODULOS = frozenset( (1, 7, 11, 13, 17, 19, 23, 29) )

    for q in itertools.compress(
            itertools.islice(itertools.count(7), 0, None, 2),
            itertools.cycle(MASK)):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
			
        else:
            x = q + 2*p
            while x in D or (x%30) not in MODULOS:
                x += 2*p
            D[x] = p

def getBrent(N):
		if N%2==0:
				return 2
		y,c,m = random.randint(1, N-1),random.randint(1, N-1),random.randint(1, N-1)
		g,r,q = 1,1,1
		while g==1:             
				x = y
				for i in range(r):
						y = ((y*y)%N+c)%N
				k = 0
				while (k<r and g==1):
						ys = y
						for i in range(min(m,r-k)):
								y = ((y*y)%N+c)%N
								q = q*(abs(x-y))%N
						g = gcd(q,N)
						k = k + m
				r = r*2
		if g==N:
				while True:
						ys = ((ys*ys)%N+c)%N
						g = gcd(abs(x-ys),N)
						if g>1:
								break
		 
		return g    

def getPrimeFactors(n, sort = False):
	factors = []
	limit = int(n ** .5) + 1
	for checker in primeSet:
		if checker > limit: break
		while n % checker == 0:
			factors.append(checker)
			n //= checker


	if n < 2:
		return factors
		
	else : 
		factors.extend(getBigFactors(n, sort))
		return factors

def getBigFactors(n, sort = False):
	factors = []
	while n > 1:
		if gmpy2.is_prime(n):
			factors.append(n)
			break
			
		factor = getBrent(n) 
		factors.extend(getBigFactors(factor, sort)) # recurse to factor the not necessarily prime factor returned by pollard-brent
		n //= factor

	if sort: 
		factors.sort()  
		
	return factors
	
def isPentagonal (number):
	number = 24 * number + 1
	if isSquare(number):
		return gmpy2.isqrt(number) % 6 == 5
	
def isTriangular (number):
	return gmpy2.is_square(8 * number + 1)

def isHexagonal (number):
	return ((math.sqrt(8 * number + 1) + 1) // 4).is_integer()
		
def getTriangle (n):
	return n * (n + 1) // 2

def getHexagon(n):
	return 2 * n * (2 * n - 1) // 2
	
def generatePandigitals (begin = 1, start=1, end=9, ascending = True):
	digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	for i in range(start, end + 1) if ascending else range(end, start + 1, -1):
		for permutation in itertools.permutations(reversed(digits[begin: i + 1]), i + 1 - begin):
			if permutation [0] == '0':
				continue
				
			yield int("".join(permutation))

def isPandigital (n, begin = 1, end = 9):
	digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	return sorted(str(n)) == digits[begin:end + 2]
	
def isPalindromic (n):
	n = str(n)
	return n[::-1] == n
	
def generateFibonacci(start, next):
	yield start
	yield next
	
	while True:
		after = start + next
		yield after
		
		start = next
		next = after
		
def iDivUp (n, d):
	return (d + n - 1) // d
	
def iDivRound (n, d):
	return (n + d // 2) // d
	
def generateDigits (n, base = 10):
	n = abs(n)
	while n:
		n, mod = divmod(n, 10)
		yield mod
	
def countDigits(n, base = 10):
	n = abs(n)
	if n == 0:
		return 1
		
	test = 1
	digits = 0
	while n >= test:
		digits += 1
		test *= base
		
	return digits
	
def gcd(*args):
	return reduce(gmpy2.gcd, args)
	
def lcm(*args): 
	return reduce(gmpy2.lcm, args)	
								
def choose(n, r):
	if n < r:
		return 0
		
	return math.factorial(n) // math.factorial(r) // math.factorial(n - r)
	
def choose2(n, m = 2):
	total = 0
	for i in range(m, n + 1):
		total += choose(n, i)
		
	return total

def generateFactors(n):
	for i in range(2, gmpy2.isqrt(n) + 1):
		div, mod = divmod(n, i)
		if mod == 0:
			yield div
			if i != div:
				yield i
				
def generateFactorPairs(n):
	for i in range(2, gmpy2.isqrt(n) + 1):
		div, mod = divmod(n, i)
		if mod == 0:
			yield (div, i)
			
def generateDivisors(n):
	for i in range(1, gmpy2.isqrt(n) + 1):
		div, mod = divmod(n, i)
		if mod == 0:
			yield div
			if i != div:
				yield i
				
def generateDivisorPairs(n):
	for i in range(1, gmpy2.isqrt(n) + 1):
		div, mod = divmod(n, i)
		if mod == 0:
			yield (div, i)PK      �i�Dm�ǀ,  ,             ��    Code.pyPK      kf�D���  �             ��Q  PeterData.pyPK      jh�D��1�  �             ��  PeterJam.pyPK      frnCn-0               ��  PeterMath.pyPK      �   H/    