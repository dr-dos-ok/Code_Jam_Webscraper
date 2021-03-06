fair_squares = [
    1
    ,4
    ,9
    ,121
    ,484
    ,10201
    ,12321
    ,14641
    ,40804
    ,44944
    ,1002001
    ,1234321
    ,4008004
    ,100020001
    ,102030201
    ,104060401
    ,121242121
    ,123454321
    ,125686521
    ,400080004
    ,404090404
    ,10000200001
    ,10221412201
    ,12102420121
    ,12345654321
    ,40000800004
    ,1000002000001
    ,1002003002001
    ,1004006004001
    ,1020304030201
    ,1022325232201
    ,1024348434201
    ,1210024200121
    ,1212225222121
    ,1214428244121
    ,1232346432321
    ,1234567654321
    ,4000008000004
    ,4004009004004
    ,100000020000001
    ,100220141022001
    ,102012040210201
    ,102234363432201
    ,121000242000121
    ,121242363242121
    ,123212464212321
    ,123456787654321
    ,400000080000004
]

def between(low, high):
    return(len([num for num in fair_squares if num >= low and num <= high]))


def answer(line):
    line = line.rstrip()
    line = line.split(" ")
    return between(int(line[0]),int(line[1]))


def codejam_read(filen):
    f = open(filen,'r')
    fout = open(filen[:-2] + "out", 'w')
    case_num = 0
    test_size = f.readline()

    for line in f:
        case_num += 1
        fout.write("Case #{0}: {1}\n".format(case_num,answer(line)))

    fout.close()
    f.close()

codejam_read('C-large-1.in')
