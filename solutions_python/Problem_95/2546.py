#!/bin/python

answers = []
d = {
'e':'o',
'j':'u',
'p':'r',
'm':'l',
'y':'a',
's':'n',
'l':'g',
'j':'u',
'y':'a',
'l':'g',
'c':'e',
'k':'i',
'd':'s',
'k':'i',
'x':'m',
'v':'p',
'e':'o',
'd':'s',
'd':'s',
'k':'i',
'n':'b',
'm':'l',
'c':'e',
'r':'t',
'e':'o',
'j':'u',
's':'n',
'i':'d',
'c':'e',
'p':'r',
'd':'s',
'r':'t',
'y':'a',
's':'n',
'i':'d',
'r':'t',
'b':'h',
'c':'e',
'p':'r',
'c':'e',
'y':'a',
'p':'r',
'c':'e',
'r':'t',
't':'w',
'c':'e',
's':'n',
'r':'t',
'a':'y',
'd':'s',
'k':'i',
'h':'x',
'w':'f',
'y':'a',
'f':'c',
'r':'t',
'e':'o',
'p':'r',
'k':'i',
'y':'a',
'm':'l',
'v':'p',
'e':'o',
'd':'s',
'd':'s',
'k':'i',
'n':'b',
'k':'i',
'm':'l',
'k':'i',
'r':'t',
'k':'i',
'c':'e',
'd':'s',
'd':'s',
'e':'o',
'k':'i',
'r':'t',
'k':'i',
'd':'s',
'e':'o',
'o':'k',
'y':'a',
'a':'y',
'k':'i',
'w':'f',
'a':'y',
'e':'o',
'j':'u',
't':'w',
'y':'a',
's':'n',
'r':'t',
'r':'t',
'e':'o',
'u':'j',
'j':'u',
'd':'s',
'r':'t',
'l':'g',
'k':'i',
'g':'v',
'c':'e',
'j':'u',
'v':'p',
'z':'q',
'q':'z',
' ': ' '
}


def do():
	inp = raw_input()
	out = ''.join([d[i] for i in inp])
	answers.append(out)

def print_answers():
	i = 1
	for j in answers:
		print "Case #%d: %s" %(i, j)
		i += 1

x = int(raw_input())
while x:
	do()
	x -= 1

print_answers()
