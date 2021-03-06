def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def check(b):
	#print("Checking :",b)
	ans=[]
	ans.append(int(b))
	b=str(b)
	boolean=True	
	for i in range(2,11):
		#print(i)
		l=int(b,i)
		#print(l)
		m=multiple(l)
		if(m!=0):
			ans.append(m)
		else:
			boolean=False
			break		
	if(boolean):
		return ans
	else:
		return 0

def multiple(a):
	#print("finding multiple")
	if(isprime(a)):
		return 0
	elif(a>1):
		for i in range(2,a):
	#		print(i)
			if(a%i==0):
				return i
		return 0
	else:
		return 0

def gen(n):
	for i in range(1, 2**n):
		yield '{:0{n}b}'.format(i, n=n)

t=int(input())
n,j=input().split(' ')
n=int(n)
n=n-2
j=int(j)

count=0
answer=[]
for i in gen(n):
	#print(count, end=" ")
	k=[]
	k.append('1')
	k.append(str(i))
	k.append('1')
	k=''.join(k)
	#print(k,end=" ")
	p=check(k)
#	print(p)
	if(p!=0):
		count+=1
		answer.append(p)
	if(count==j):
		break
print("Case #1:")
for i in range(len(answer)):
	for j in range(len(answer[i])):
		print(answer[i][j], end=" ")
	print()	

