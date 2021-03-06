
import sys


def run(filename):
    f = open(filename, "r")
    case_count = int(f.readline())
    mapping = getMapping()
    for i in xrange(case_count):
        line = f.readline()[:-1]
        result = process_case(mapping, line)
        print('Case #%d: %s' % (i+1, result))
        
        
def process_case(mapping, line):
    result = ''
    for c in line:
        result += c if c not in mapping else mapping[c]
        
    return result
        
def getMapping():
    googlese = ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
        'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
        'de kr kd eoya kw aej tysr re ujdr lkgc jv']
    english = ['our language is impossible to understand', 
        'there are twenty six factorial possibilities',
        'so it is okay if you want to just give up']
    
    givenMapping = {'y':'a', 'e':'o', 'q':'z', 'z': 'q'}
    for i in xrange(len(googlese)):
        for j in xrange(len(googlese[i])):
            givenMapping[googlese[i][j]] = english[i][j]
            
    return givenMapping


#MAIN
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "Sample.in"

run(filename)
