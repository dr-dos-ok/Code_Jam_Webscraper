import sys

def process(s,count):
	c = s.split()[1:]
	totalTime = 0
	current = {'O':1,'B':1}
	ct = 0
	prevc = ''
	for i in range(0,len(c),2):
		time_needed = abs(int(c[i+1]) - current[c[i]])
		if prevc == c[i]:
			td = time_needed + 1
			totalTime += td
			ct += td
		else:
			if time_needed <= ct:
				ct = 1
				totalTime += 1
			else:
				ct = time_needed - ct  + 1
				totalTime += ct
		current[c[i]] = int(c[i+1])
		prevc = c[i]
	
	return 'Case #' + str(case) + ': ' + str(totalTime)


filename = sys.argv[1]
f = open(filename, 'r')
inputs = f.readlines()
case = 1
outputs = []
for i in inputs[1:]:
	outputs.append(process(i,case)+'\n')
	case += 1


fo = open('a_out.txt','w+')
fo.writelines(outputs)
fo.close()
f.close()	