import sys
def flip (arr, i, k):
	for j in range (0, k):
		arr[i] = 1 if arr[i] == 0 else 0;
		i=i+1
	return arr

def abc (arr, k):
	i,c=0,0
	while i <= len(arr) - k:
		if arr[i]==0:
			arr = flip (arr, i, k)
			c=c+1
		i=i+1
	while i <=len (arr)-1:
		if 	arr[i] == 0:  
			return "IMPOSSIBLE"
			break
		i=i+1	
	if i == len(arr):
		return c

with open(sys.argv[1],'r') as files :
    t = int (files.readline())
    for i in xrange(1, t + 1):
        str, K = files.readline().split (' ')
        j, arr =0, []
       	while j < len(str):
        	arr.append(0) if str[j] == '-' else arr.append(1)
        	j=j+1
        print "Case #{}: {}".format(i, abc(arr, int(K)))
