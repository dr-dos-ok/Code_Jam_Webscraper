t=int(input())
i=1
while(t>0):
	s=int(input())
	x=set()
	m=1
	if(s!=0):
		while(len(x)<10):
			a=s*m
			n=a
			while(n!=0):
				x.add(n%10)
				n//=10
			m+=1
	else:
		a="INSOMNIA"
	print("Case #{}: {}".format(i,a))
	i+=1
	t-=1