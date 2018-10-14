import copy
fin= open("B-large (2).in",'r')
fout=open("round1C_B2.out",'w')
bases =range(2,11)
T = int(fin.readline())
for t in range(T):
    [B,M]= [int(i) for i in fin.readline().split()]
    slides = [[0]*B for i in range(B)]
    solved=False
    print B,M
    for i in range(B-1):
      for j in range(i+1,B-1):
        slides[i][j]=1
    m=M
    if M>2**(B-2):
        print 'IMPOSSIBLE'
        fout.write("Case #"+str(t+1)+': IMPOSSIBLE'+ '\n')
        
    elif M==2**(B-2):
        for i in range(B-1):
            slides[i][B-1]=1;
        print 'POSSIBLE'
        print '\n'.join([str(i) for i in slides])
        fout.write("Case #"+str(t+1)+': POSSIBLE'+ '\n')
        fout.write('\n'.join([''.join([str(j)for j in i]) for i in slides]))
        fout.write('\n')
    else:
        for i in range(B-1):
            if (M/(2**i))%2:
                slides[i+1][B-1]=1;
        print 'POSSIBLE'
        print '\n'.join([str(i) for i in slides])
        fout.write("Case #"+str(t+1)+': POSSIBLE'+ '\n')
        fout.write('\n'.join([''.join([str(j)for j in i]) for i in slides]))
        fout.write('\n')



        
    
fout.close()
fin.close()




positionVals =[ [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648L],
[1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467, 3486784401L, 10460353203L, 31381059609L, 94143178827L, 282429536481L, 847288609443L, 2541865828329L, 7625597484987L, 22876792454961L, 68630377364883L, 205891132094649L, 617673396283947L],
[1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824, 4294967296L, 17179869184L, 68719476736L, 274877906944L, 1099511627776L, 4398046511104L, 17592186044416L, 70368744177664L, 281474976710656L, 1125899906842624L, 4503599627370496L, 18014398509481984L, 72057594037927936L, 288230376151711744L, 1152921504606846976L, 4611686018427387904L],
[1, 5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625, 48828125, 244140625, 1220703125, 6103515625L, 30517578125L, 152587890625L, 762939453125L, 3814697265625L, 19073486328125L, 95367431640625L, 476837158203125L, 2384185791015625L, 11920928955078125L, 59604644775390625L, 298023223876953125L, 1490116119384765625L, 7450580596923828125L, 37252902984619140625L, 186264514923095703125L, 931322574615478515625L, 4656612873077392578125L],
[1, 6, 36, 216, 1296, 7776, 46656, 279936, 1679616, 10077696, 60466176, 362797056, 2176782336L, 13060694016L, 78364164096L, 470184984576L, 2821109907456L, 16926659444736L, 101559956668416L, 609359740010496L, 3656158440062976L, 21936950640377856L, 131621703842267136L, 789730223053602816L, 4738381338321616896L, 28430288029929701376L, 170581728179578208256L, 1023490369077469249536L, 6140942214464815497216L, 36845653286788892983296L, 221073919720733357899776L, 1326443518324400147398656L],
[1, 7, 49, 343, 2401, 16807, 117649, 823543, 5764801, 40353607, 282475249, 1977326743, 13841287201L, 96889010407L, 678223072849L, 4747561509943L, 33232930569601L, 232630513987207L, 1628413597910449L, 11398895185373143L, 79792266297612001L, 558545864083284007L, 3909821048582988049L, 27368747340080916343L, 191581231380566414401L, 1341068619663964900807L, 9387480337647754305649L, 65712362363534280139543L, 459986536544739960976801L, 3219905755813179726837607L, 22539340290692258087863249L, 157775382034845806615042743L],
[1, 8, 64, 512, 4096, 32768, 262144, 2097152, 16777216, 134217728, 1073741824, 8589934592L, 68719476736L, 549755813888L, 4398046511104L, 35184372088832L, 281474976710656L, 2251799813685248L, 18014398509481984L, 144115188075855872L, 1152921504606846976L, 9223372036854775808L, 73786976294838206464L, 590295810358705651712L, 4722366482869645213696L, 37778931862957161709568L, 302231454903657293676544L, 2417851639229258349412352L, 19342813113834066795298816L, 154742504910672534362390528L, 1237940039285380274899124224L, 9903520314283042199192993792L],
[1, 9, 81, 729, 6561, 59049, 531441, 4782969, 43046721, 387420489, 3486784401L, 31381059609L, 282429536481L, 2541865828329L, 22876792454961L, 205891132094649L, 1853020188851841L, 16677181699666569L, 150094635296999121L, 1350851717672992089L, 12157665459056928801L, 109418989131512359209L, 984770902183611232881L, 8862938119652501095929L, 79766443076872509863361L, 717897987691852588770249L, 6461081889226673298932241L, 58149737003040059690390169L, 523347633027360537213511521L, 4710128697246244834921603689L, 42391158275216203514294433201L, 381520424476945831628649898809L],
[1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000L, 100000000000L, 1000000000000L, 10000000000000L, 100000000000000L, 1000000000000000L, 10000000000000000L, 100000000000000000L, 1000000000000000000L, 10000000000000000000L, 100000000000000000000L, 1000000000000000000000L, 10000000000000000000000L, 100000000000000000000000L, 1000000000000000000000000L, 10000000000000000000000000L, 100000000000000000000000000L, 1000000000000000000000000000L, 10000000000000000000000000000L, 100000000000000000000000000000L, 1000000000000000000000000000000L, 10000000000000000000000000000000L] ]
primes =  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
           67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
           139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
           223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
           293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379,
           383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461,
           463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563,
           569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643,
           647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
           743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829,
           839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937,
           941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021,
           1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093,
           1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181,
           1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259,
           1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321,
           1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433,
           1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493,
           1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579,
           1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657,
           1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741,
           1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831,
           1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913,
           1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999,1];