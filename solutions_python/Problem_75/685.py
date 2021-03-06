'''
Problem
@YEAR Google Code Jam 2011: Qualification Round
@ID B
@NAME Magicka
@URL http://code.google.com/

Solution
@AUTHOR Wonjohn Choi (http://capcs.wordpress.com/)
@LANG Python 3
@RESULT accepted (small inputs)
'''

def convert(inputs, combines, opposes):
    output = []
    
    #for every command
    for c in inputs:
        output.append(c)
        if len(output)>=2:
            
            #check if end is combinable
            done = False
            while not done:
                done = True
                for combine in combines:
                    if output[-1]==combine[0] and output[-2]==combine[1]:
                        output = output[:-2]+[combine[2]]
                        done = False
                        break
            
            #check if containing opposable
            for oppose in opposes:
                if oppose[0] in output and oppose[1] in output:
                    output = [] #clear
                    break
                    
    return output
                        

def solve():
    t = int(input())
    for i in range(t):
        line = map(str, str(input()).split(' '))
        #print(line)
        
        c = int(next(line))
        combines = []
        for j in range(c):
            e = str(next(line))
            combines.append(e)              #QRI
            combines.append(e[1]+e[0]+e[2]) #RQI
        
        d = int(next(line))
        opposes = []
        for j in range(d):
            e = str(next(line))
            opposes.append(e) #QF
        
        n = int(next(line))
        inputs = str(next(line)) #ini
        
        print('Case #'+str(i+1)+': ['+', '.join(convert(inputs, combines, opposes))+']')
        
        
solve()

