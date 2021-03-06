#!/usr/local/bin/python

# GOOGLE CODE JAM 2013
# This is a submission to the Google Code Jam 2013

#IMPORTS
import sys
import os
import re


#bool - Defines wether test mode should be used regardless of arguments
FORCE_TEST_MODE = False

#str - Test Input
TEST_INPUT = open("test.txt").read()
#list - Outputs for each test case
TEST_OUTPUT=["X won","Draw", "Game has not completed", "O won", "O won", "O won", "O won"]

#bool - Defines wether the number of lines per test case is constant or notb
NR_OF_LINES_PER_CASE_ISCONSTANT = True

#int - Number of lines per case, if NR_OF_LINES_PER_CASE_ISCONSTANT = True
NR_OF_LINES_PER_CASE = 5




#parseInput(input)
#Parses the input file 
#ONLY EXECUTED:
#if not NR_OF_LINES_PER_CASE_ISCONSTANT
#input = list of string with lines in the input file
#problemCount = Ammount of problems in input
#Returns list of list of strings
def parseInput(input, problemCount):
  #Example Implementation:
  #   one line at the beginning of every
  #   problem with an int that represents
  #   the number of lines per problem

  cases = []
  for x in xrange(0,problemCount):
    count = input.pop(0)
    curCase = []
    for line in xrange(0,int(count)):
      curCase.append(input.pop(0))
    cases.append(curCase)
  return cases


def checkWon(four):
  if four.count("X")==4 or (four.count("X")==3 and "T" in four):
    return "X won"
  elif four.count("O")==4 or (four.count("O")==3 and "T" in four):
    return "O won"
  return None

#solveCase(case) 
#Solves a testcase

#Main problem solving

#case = list of string with lines in input file
#       that belong to one Test case
#Returns output for the case as string; Unformatted (no Case: #X)
#   and without \n
def solveCase(case):
  
  # First do lines

  for line in case:
    won = checkWon(line)
    if won:
      return won

  cols = [[],[],[],[]]

  for line in case:
    i=0
    for char in line:
      cols[i].append(char)
      i+=1

  for col in cols:
    won = checkWon(col)
    if won:
      return won

  tlbr = [case[0][0],case[1][1],case[2][2],case[3][3]]
  won = checkWon(tlbr)
  if won:
    return won

  trbl = [case[0][3],case[1][2],case[2][1],case[3][0]]
  won = checkWon(trbl)
  if won:
    return won

  #Aperrantly there's no winner till here so check if draw or not complete
  
  for line in case:
    for char in line:
      if char==".":
        return "Game has not completed"

  return "Draw"





##### ONLY BOILERPLATE CODE BELOW - SHOULD NOT NEED TO BE ALTERED


def getCases(lines):
  # Parse file
  cases = []
  try:
    m = int(lines.pop(0)) #Number of problems always in line 
  except Exception, e:
    errorOut("Invalid Input")


  if NR_OF_LINES_PER_CASE_ISCONSTANT:
    n = NR_OF_LINES_PER_CASE
    i = 0

    for x in xrange(0,m):
      case = []
      for x in xrange(0,n):
          case.append(lines.pop(0))
      cases.append(case)

  else:
    cases = parseInput(lines,m)

  print "Found "+str(len(cases))+" test cases\n"
  return cases



## Work with unit tests - define TEST_INPUT : see above
def test():
  
  if not TEST_INPUT and not TEST_OUTPUT:
    errorOut("Please make sure you define TEST_INPUT and TEST_OUTPUT")
  testcount = len(TEST_OUTPUT)
  rightcount = 0
  

  cases = getCases(TEST_INPUT.split("\n"))
  solutions = TEST_OUTPUT

  if not len(cases) == testcount:
    errorOut("Invalid test cases")

  i=0
  for testcase in cases:
    toprint = "Evaluating: "
    solve = solveCase(testcase)
    if solve==solutions[i]:
      toprint += "Correct!"
      rightcount+=1
    else:
      toprint+="Uh oh!"
    
    toprint += "   Given: "+solve
    toprint += " Expected: "+solutions[i]
    toprint += " Input: "+ "".join(testcase)
    print toprint 

    i+=1

  print
  print "Solved "+str(rightcount)+" out of "+ str(testcount) + " test cases correctly"



def production():
  # Get filename
  #Default filename = SCRIPT.in (Without .py)  
  filename = sys.argv[0][:-3]+".in"
  if "--in" in sys.argv:
    try:
      filename=sys.argv[sys.argv.index("--in")+1]
    except Exception, e:
      errorOut("Please specify an input file")
    

  if not os.path.isfile(filename):
    errorOut("Specified input file does not exist\nStandard input: "+sys.argv[0][:-3]+'.in\n')

  # Get output file
  out=sys.argv[0][:-3]+".out"
  if "--out" in sys.argv:
    try:
      out=sys.argv[sys.argv.index("--out")+1]
    except Exception, e:
      errorOut("Please specify an output file")
    
  
  # Get input by line
  f=None
  try:
    f=open(filename,"rU")
  except Exception, e:
    errorOut("Could not open input file!")

  cases = getCases(f.read().split("\n"))


  
  # Let's play

  output = ""
  curCase = 1
  for case in cases:
    print "Solving " + str(curCase) + " out of "+str(len(cases))
    output+="Case #"+str(curCase)+": "
    output+=solveCase(case)
    output+="\n"
    curCase+=1
 

  # Store output
  try:
    outf = open(out,"w")
    outf.write(output)
    outf.close()

    print "\n\n"

    print "Done! Output stored in: "+out
  except Exception, e:
    print "Error writing output! Here it is in stdout \n"+output

def main():
  if "--test" in sys.argv or FORCE_TEST_MODE:
    print "Test mode"
    test()
  else:
    print "Production mode"
    production()
    


#Exit with error
def errorOut(msg):
  sys.stderr.write(msg+"\n")
  sys.exit(1)

if __name__ == '__main__':
  main()
