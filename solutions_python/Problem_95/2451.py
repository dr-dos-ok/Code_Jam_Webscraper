count = input( )

translation = {
	'a': 'y',
	'b': 'h',
	'c': 'e', 
	'd': 's', 
	'e': 'o', 
	'f': 'c', 
	'g': 'v', 
	'h': 'x', 
	'i': 'd', 
	'j': 'u', 
	'k': 'i', 
	'l': 'g', 
	'm': 'l', 
	'n': 'b', 
	'o': 'k', 
	'p': 'r', 
	'q': 'z',
	'r': 't', 
	's': 'n', 
	't': 'w', 
	'u': 'j', 
	'v': 'p', 
	'w': 'f', 
	'x': 'm',
	'y': 'a',
	'z': 'q',
}

for i in range(count):
	line = raw_input( ).strip()
	
	print 'Case #%d:' % (i+1), ''.join( [ translation.get(c, c) for c in line ] )