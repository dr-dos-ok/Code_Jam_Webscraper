import bisect

def is_sorted(l):
	return all(l[i] <= l[i+1] for i in xrange(len(l)-1))

def to_bin(n):
	return "{0:b}".format(n)

def to_int(s):
	return int(s, 2)

def gen_tidy(c=1000):
	# m = []
	for i in xrange(c + 1):
		I = map(int, str(i))
		if is_sorted(I):
			# m.append(i)
			print i
	# return m


# M = gen_tidy(10**18)
# print M
M = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29, 33, 34, 35, 36, 37, 38, 39, 44, 45, 46, 47, 48, 49, 55, 56, 57, 58, 59, 66, 67, 68, 69, 77, 78, 79, 88, 89, 99, 111, 112, 113, 114, 115, 116, 117, 118, 119, 122, 123, 124, 125, 126, 127, 128, 129, 133, 134, 135, 136, 137, 138, 139, 144, 145, 146, 147, 148, 149, 155, 156, 157, 158, 159, 166, 167, 168, 169, 177, 178, 179, 188, 189, 199, 222, 223, 224, 225, 226, 227, 228, 229, 233, 234, 235, 236, 237, 238, 239, 244, 245, 246, 247, 248, 249, 255, 256, 257, 258, 259, 266, 267, 268, 269, 277, 278, 279, 288, 289, 299, 333, 334, 335, 336, 337, 338, 339, 344, 345, 346, 347, 348, 349, 355, 356, 357, 358, 359, 366, 367, 368, 369, 377, 378, 379, 388, 389, 399, 444, 445, 446, 447, 448, 449, 455, 456, 457, 458, 459, 466, 467, 468, 469, 477, 478, 479, 488, 489, 499, 555, 556, 557, 558, 559, 566, 567, 568, 569, 577, 578, 579, 588, 589, 599, 666, 667, 668, 669, 677, 678, 679, 688, 689, 699, 777, 778, 779, 788, 789, 799, 888, 889, 899, 999]

T = int(raw_input())

for t in xrange(T):
	N = raw_input()
	n = int(N)

	i = bisect.bisect(M, n)

	a = M[i - 1] if i > 0 else 0

	print "Case #%d: %d" % (t+1, a)