'''

@author: Dan Bjorge
'''

#fileprefix = 'A-small-ex'
fileprefix = 'A-small-attempt0'
#fileprefix = 'A-large'

filepath = ''
filepathname = filepath + fileprefix
infilename = filepathname + '.in'
outfilename = filepathname + '.out'
lines = open(infilename, 'rU').read().split("\n")
outfile = open(outfilename, 'w+')

#This will sometimes, but not often, change
linenum = 1
cases = int(lines[0])

    
    #Begin parsing for one problem starting at line linenum
    bases = [int(x) for x in lines[linenum].split(" ")]
    out = solve(bases) #Assign solved value
    linenum+=1
    
    #End parsing - start outputting
    casestr = 'Case #'+str(casenum)+': '+str(out)
    print (casestr)
    outfile.write(casestr+"\n")