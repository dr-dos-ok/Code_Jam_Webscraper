
key = {
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
    'z': 'q'
}

count = raw_input()

for i in range(int(count)):
    s = raw_input()
    newstr = ''
    for j in range(len(s)):
        if s[j] in key:
            newstr += key[s[j]]
        else:
            newstr += s[j]

    print 'Case #' + str(i+1) + ': ' + newstr
    