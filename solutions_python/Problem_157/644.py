minus = {}
minus['1'] = 'm'
minus['i'] = 'n'
minus['j'] = 'o'
minus['k'] = 'p'
minus['m'] = '1'
minus['n'] = 'i'
minus['o'] = 'j'
minus['p'] = 'k'

def computeProd(a, b):
	if a == '1':
		return b
	elif a == 'i':
		if b =='1':
			return 'i'
		elif b == 'i':
			return minus['1']
		elif b == 'j':
			return 'k'
		elif b == 'k':
			return minus['j']
		else:
			return minus[computeProd(a, minus[b])]
	elif a == 'j':
		if b =='1':
			return 'j'
		elif b == 'i':
			return minus['k']
		elif b == 'j':
			return minus['1']
		elif b == 'k':
			return 'i'
		else:
			return minus[computeProd(a, minus[b])]
	elif a == 'k':
		if b =='1':
			return 'k'
		elif b == 'i':
			return 'j'
		elif b == 'j':
			return minus['i']
		elif b == 'k':
			return minus['1']
		else:
			return minus[computeProd(a, minus[b])]
	else:
		return minus[computeProd(minus[a], b)]
	
for t in range(input()):
	L, X = map(int, raw_input().split())
	chars = raw_input()
	if L*X < 3:
		print "Case #"+str(t+1)+": NO"
	else:
		chars = chars*X
		c = chars[0]
		i_found = False
		j_found = False
		i_pos = 0
		j_pos = 0
		for i in range(1, L*X):
			if c == 'i':
				i_pos = i-1
				i_found = True
				break
			c = computeProd(c, chars[i])
		if i_found == False:
			print "Case #"+str(t+1)+": NO"
			continue
		c = chars[i_pos+1]
		
		for i in range(i_pos+2, L*X):
			if c == 'j':
				j_pos = i-1
				j_found = True
				break
			c = computeProd(c, chars[i])
		if j_found == False:
			print "Case #"+str(t+1)+": NO"
			continue
		c = chars[j_pos+1]
		for i in range(j_pos+2, L*X):
			c = computeProd(c, chars[i])
		if c != 'k':
			print "Case #"+str(t+1)+": NO"
			continue
		print "Case #"+str(t+1)+": YES"