myinput = """
100
132
1000
7
204
343
129
818
827
845
149
254
839
87
1
810
933
136
291
705
778
445
840
748
494
762
418
135
814
79
626
996
442
644
634
123
938
444
738
208
414
891
480
513
999
766
780
584
432
176
358
730
478
815
595
532
724
60
836
822
590
317
54
536
977
974
238
945
352
106
119
529
570
168
210
713
372
561
809
998
339
230
315
318
853
120
2
267
959
689
613
374
694
338
834
866
21
397
262
726
994
"""

ns = [l for l in myinput.split('\n') if l][1:]

def is_happy(n):
  for i, c in enumerate(n):
    if i > 0 and n[i-1] > c:
      return False
  return True

for n in ns:
  if is_happy(n):
    print(n)
  else:
    candidates = [
      str(int(str(int(n[:i-1])-1) + '9' * (len(n)-i+1)))
      for i in range(len(n), 1, -1)
    ]
    for candidate in candidates:
      if is_happy(candidate):
        print(candidate)
        break