'''

@author: Dan Bjorge
'''

#fileprefix = 'A-small-ex'
#fileprefix = 'A-small-attempt0'
fileprefix = 'A-large'

filepath = ''
filepathname = filepath + fileprefix
infilename = filepathname + '.in'
outfilename = filepathname + '.out'
lines = open(infilename, 'rU').read().split("\n")
outfile = open(outfilename, 'w+')

#This will sometimes, but not often, change
linenum = 1
cases = int(lines[0])

for casenum in range(1, cases+1):
    #Begin parsing for one problem starting at line linenum
    L = int(lines[linenum])
    
    #End parsing - start outputting
    casestr = 'Case #'+str(casenum)+': '+ out
    print (casestr)
    outfile.write(casestr+"\n")