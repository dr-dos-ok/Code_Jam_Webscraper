import sys

if __name__ == "__main__":
	letter_mapping = {'\n': '\n', ' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', 'q': "z"}
	infile = open(sys.argv[1], 'r')
	outfile = open(sys.argv[2], 'w')
	lines = int(infile.readline())

	for i in xrange(1, lines+1):
		inline = infile.readline()
		outfile.write("Case #" + str(i) + ": ")
		for j in inline:
			outfile.write(letter_mapping.get(j, "_"))

