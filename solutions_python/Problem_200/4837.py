# Google CodeJam - Qualifiers B

def check(a):
    # returns boolean of whether A is tidy or not
    b = str(a)
    last = b[0]
    for digit in b[1:]:
        if last <= digit:
            last = digit
        else:
            return False
    return True

inp = """100
132
1000
7
943
803
86
701
286
218
568
778
676
177
383
712
388
259
587
598
986
655
333
149
309
761
650
498
160
688
243
437
783
403
600
726
283
483
381
108
293
192
677
75
767
304
115
6
891
350
1
344
174
920
319
732
999
470
821
993
282
913
147
21
899
531
280
122
345
204
808
958
876
242
818
110
576
773
391
559
982
102
945
887
858
311
678
281
973
560
52
689
782
414
807
738
48
846
477
187
455
""".split()
cases = int(inp[0])
for c in xrange(1,cases+1):
    n = int(inp[c])
    loo = 0
    while loo < n:
        if check(n-loo):
            print "Case #{}:".format(c), n-loo
            break
        loo += 1
