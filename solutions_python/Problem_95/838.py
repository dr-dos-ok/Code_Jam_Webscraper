cases = raw_input()
for case in xrange(int(cases)):
    mapping = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o',
               'd': 's', 'g': 'v', 'f': 'c', 'i': 'd',
               'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l',
               'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z',
               'p': 'r', 's': 'n', 'r': 't', 'u': 'j',
               't': 'w', 'w': 'f', 'v': 'p', 'y': 'a',
               'x': 'm', 'z': 'q', ' ': ' '}

    c = raw_input()
    p = ''.join([mapping[i] for i in c])
    
    print 'Case #%d: %s' % (case + 1, p)
