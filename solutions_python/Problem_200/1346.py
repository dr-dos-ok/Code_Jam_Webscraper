import numpy
lines = open('file.in', 'r').read().splitlines()
numberOfCases = int(lines[0])
for number in range(numberOfCases):
findTidy = lines[number+1]
while True:
	tidyList = numpy.array(list(findTidy))
	lenth = len(tidyList)
	allNotSet = False
	for i in range(1, lenth):
		if not tidyList[i-1] <= tidyList[i]:
			tidyList[i-1] = int(tidyList[i-1]) - 1
			tidyList[i:] = 9
			allNotSet = True
			findTidy = list(tidyList)
			break
	if not allNotSet:
		break
print('Case #{}: {}'.format(number+1, int(''.join(tidyList))))