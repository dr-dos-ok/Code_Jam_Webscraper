arr=[1, 4, 9, 121, 484, 676, 10201, 12321, 14641, 40804, 44944, 69696, 94249, 698896, 1002001, 1234321, 4008004, 5221225, 6948496, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 522808225, 617323716, 942060249, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 637832238736, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1086078706801, 1210024200121, 1212225222121, 1214428244121, 1230127210321, 1232346432321, 1234567654321, 1615108015161, 4000008000004, 4004009004004, 4051154511504, 5265533355625, 9420645460249, 100000020000001, 100220141022001, 102012040210201, 102234363432201, 121000242000121, 121242363242121, 123212464212321, 123456787654321, 123862676268321, 144678292876441, 165551171155561, 400000080000004, 900075181570009, 4099923883299904, 10000000200000001, 10002000300020001, 10004000600040001, 10020210401202001, 10022212521222001, 10024214841242001, 10201020402010201, 10203040504030201, 10205060806050201, 10221432623412201]

sq = [str(int(x**0.5)) for x in arr]

def is_palindrome(w):
    return w == w[::-1]

pals = [ 1 if is_palindrome(x) else 0 for x in sq]

fairsq = [arr[x] for x in xrange(len(pals)) if pals[x]==1]

t = input()

for x in xrange(t):
	a,b=map(int,raw_input().split())
	count = 0
	for y in fairsq:
		if (a <=y <= b):
			count+=1
	print "Case #%d: %d" %(x+1,count)
