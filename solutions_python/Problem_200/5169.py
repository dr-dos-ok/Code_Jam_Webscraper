def tidy(num):
	numList = list(str(num))
	a = []
	for i in range(len(numList)-1):
		if numList[i] > numList[i+1]:
			return 'null'
		else:
			a.append(numList[i])
	a.append(numList[-1])
	b = ''.join(a)
	return b

def tidyNumber(num):
	b = 'null'
	for i in xrange(num):
		if b == 'null':
			b = tidy(num-i)
	return b	

def main(a):
	for i in range(len(a)):
		print 'Case #%d: %s' % (i+1,tidyNumber(a[i]))

if __name__ == "__main__":
  main([132,
1000,
7,
943,
803,
86,
701,
286,
218,
568,
778,
676,
177,
383,
712,
388,
259,
587,
598,
986,
655,
333,
149,
309,
761,
650,
498,
160,
688,
243,
437,
783,
403,
600,
726,
283,
483,
381,
108,
293,
192,
677,
75,
767,
304,
115,
6,
891,
350,
1,
344,
174,
920,
319,
732,
999,
470,
821,
993,
282,
913,
147,
21,
899,
531,
280,
122,
345,
204,
808,
958,
876,
242,
818,
110,
576,
773,
391,
559,
982,
102,
945,
887,
858,
311,
678,
281,
973,
560,
52,
689,
782,
414,
807,
738,
48,
846,
477,
187,
455])