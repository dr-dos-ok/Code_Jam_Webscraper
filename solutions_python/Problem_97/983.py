import math
def intLen(n):
    if n > 0:
        digits = int(math.log10(n))
    elif n == 0:
        digits = 0
    else:
        digits = int(math.log10(-n))+1
    return digits

def rotate(no,times):
    length = intLen(no)
    mod = 0
    while not mod:
        mod = no%10
        no/=10
        #print no,mod
        if mod:
            no+=mod*(10**length)
            #print no
    return no


if __name__ == '__main__':
    fin = open("C-small-0.in","r")
    fout = open("C.out","w")
    N = int(fin.readline())

    for i in range(0,N):
        A,B = fin.readline().split()
        A,B = int(A),int(B)
        print A,B
        result = 0
        for j in range(A,B+1):
            times = 1
            rot = rotate(j,times)
            while rot != j:
                if rot > j and rot<=B:
                    result +=1
                rot = rotate(rot,times)
        fout.write("Case #"+str(i+1)+": "+str(result)+"\n")
