
# coding: utf-8

# In[95]:

import numpy
import math


# In[96]:

inputs = """100
2 1
100 20
200 10
2 2
100 20
200 10
3 2
100 10
100 10
100 10
4 2
9 3
7 1
10 1
8 4
6 3
25922 2488
28570 2654
21003 2612
292753 81
226214 82
22252 2561
9 2
3025 317257
10592 8
14744 52
3195 307004
3657 390720
3069 388980
3468 326967
3568 398744
3173 318922
9 4
451904 550023
556264 701676
681702 343614
340775 346521
371619 592931
457735 275255
825040 494551
484029 278623
559184 145166
5 3
17574 58
3987 331685
3917 397483
13522 64
3400 334289
2 1
373410 874962
91809 729080
10 5
22230 2386
25119 2596
27244 2095
28314 2447
29640 2738
297601 3
257316 42
26568 2828
273321 53
21851 2048
9 5
87172 471366
44892 915306
133644 307458
308826 133052
411768 99789
663404 61938
50616 811797
261516 157122
55944 734483
9 5
717742 168920
694717 594640
659800 394062
850028 280964
331595 673057
159286 574587
720766 801699
841160 434943
764642 353096
10 3
3269 303149
3834 343044
3577 356616
3488 365069
13552 83
3287 317879
3596 332209
3163 387218
19820 10
12195 69
5 3
133644 133722
27972 638894
135864 131537
860472 20769
35224 507357
6 4
25101 2300
228411 88
25925 2437
242839 7
25605 2390
22596 2766
10 2
24479 2290
274027 87
27978 2231
22606 2857
255980 88
24367 2404
200512 96
25107 2246
21294 2986
29518 2611
8 5
36018 216524
38628 201894
185592 42021
94392 82621
126063 61864
73416 106227
14168 550449
81548 95634
2 1
256879 73
26867 2304
7 3
555909 81551
337708 134243
377530 120083
881591 51424
76291 594237
89799 504849
511427 88644
4 2
86130 396263
133144 256340
409298 83387
810384 42116
6 3
28714 2543
206437 79
22185 2557
24780 2928
25908 2505
244589 5
10 6
3232 387716
18142 6
3446 376118
3814 350746
18671 66
3948 318923
3676 385624
3772 364996
19587 55
3803 370115
7 2
3023 391172
3421 336135
3845 331603
17650 79
18303 83
3477 371137
3251 320779
9 6
27593 2441
28561 2515
21249 2048
25391 2416
250664 13
221474 63
28679 2682
20994 2904
23195 2536
8 5
223949 28707
334022 182301
490957 983195
96805 311206
676970 931583
564201 808242
682097 114615
519382 639414
7 4
3363 315338
10689 59
3758 344903
12117 16
3229 371862
3410 395432
3016 321354
5 1
3999 327366
3183 307478
17034 96
16174 10
3684 319003
7 3
28483 332926
730171 672526
621102 70091
233652 967515
583686 258338
454961 836446
975859 634564
6 1
79878 958592
111476 686878
86918 880950
980026 78131
540347 141706
231253 331111
3 1
607508 599282
422683 263945
964664 163628
8 6
94462 535035
84275 599709
86053 587318
323428 156265
146917 344007
66831 756243
170307 296761
177472 284780
8 3
149016 163218
76307 318740
149016 163218
174247 139584
927970 26210
350518 69389
420863 57791
131586 184838
5 1
82695 950655
570158 344907
697603 574642
961917 399728
877207 555813
9 3
125367 134335
27740 607108
37217 452513
431471 39032
383111 43959
32810 513294
181443 92818
165040 102043
224561 74996
2 1
12039 62
3613 343901
5 2
3281 361680
19342 21
3881 360375
17711 92
3403 312015
9 2
790820 73082
336450 171778
218747 264208
132393 436539
112644 513074
160429 360251
237271 243581
578161 99963
450083 128409
9 2
547904 129198
213957 330852
130191 543725
384173 184261
89459 791291
390245 181394
145215 487471
361267 195944
245509 288332
10 2
225301 57
28633 2436
26749 2512
258855 92
26607 2784
227385 20
25949 2043
25179 2590
20277 2776
23170 2215
8 3
23388 2565
24307 2237
279561 88
20865 2949
27018 2123
22012 2201
24144 2898
270144 5
5 3
3525 324579
3678 351575
13784 90
3889 389548
19743 71
1 1
1 1
2 2
573426 10868
588924 10582
3 1
61518 174921
87447 123055
24174 445139
9 5
333959 462285
474513 287259
937858 313309
418685 70605
475008 909298
776482 553271
247546 235421
700807 146291
124686 390337
4 2
22723 2480
236286 57
28914 2110
26930 2816
9 5
946160 70941
156582 428667
965458 69523
254441 263800
158655 423066
317325 211523
386311 173750
81586 822709
179725 373468
7 4
27993 849816
495726 47988
660968 35991
134676 176638
70004 339822
202797 117304
194184 122507
10 3
3370 333659
14474 4
3714 372832
3387 373274
3140 304512
3892 342633
3254 329567
10314 72
3823 302451
17323 100
3 1
3053 355489
3297 397229
10370 77
7 2
3161 356351
3608 345446
3049 327991
19333 42
3519 302157
12748 48
3902 346063
9 5
180523 127224
42066 545972
658378 34884
213528 107559
131733 174344
43911 523032
91512 250971
676172 33966
82584 278103
4 3
69426 350796
39928 609957
194184 125419
58466 416556
7 4
839188 18414
40579 380808
36828 419594
85239 181288
821128 18819
698148 22134
61404 251658
4 2
49758 244352
89649 135623
16484 737592
59296 205047
5 3
92092 37962
11362 307692
15873 220248
309764 11286
129352 27027
9 2
28148 2602
29086 2856
26461 2009
22136 2729
26810 2883
202835 1
20673 2038
283040 90
22401 2907
8 6
13930 23
19195 61
3818 327289
3937 355706
3457 336172
3605 331888
3127 321166
3313 397809
7 4
642255 417602
396934 55346
150855 664902
104051 317447
508656 650066
235077 633465
336475 852966
3 2
3586 366743
18612 4
3199 335983
5 1
606066 35255
90859 235165
52310 408466
105200 203107
47773 447258
3 2
210200 20062
607578 295240
64667 155619
9 5
28694 2546
23208 2858
214632 31
23579 2988
25120 2943
258834 93
26589 2767
28441 2520
24815 2778
4 3
334500 449212
828558 79200
348203 79692
785813 349213
7 3
28854 2155
20199 2828
206389 39
220239 30
20487 2049
22004 2689
21396 2303
10 10
1000000 1000000
1000000 1000000
1000000 1000000
1000000 1000000
1000000 1000000
1000000 1000000
1000000 1000000
1000000 1000000
1000000 1000000
1000000 1000000
6 2
24532 436229
422487 143202
453418 451832
690736 157805
847606 438112
29167 880806
10 6
552636 43586
98642 244188
120916 199206
560728 42957
430236 55986
54094 445284
122094 197284
144522 166668
200466 120156
132867 181288
3 1
3337 333228
3573 320814
13362 14
8 5
90261 948633
160797 532501
148539 576445
463650 184675
268281 319160
166496 514274
865988 98875
327026 261828
2 2
11284 865674
865674 11284
4 2
27524 908946
38032 657810
709464 35263
58530 427436
4 2
510653 106687
441309 123451
172355 316092
649136 83927
7 3
714427 110167
698612 833032
464023 948997
160546 115191
247316 632695
375790 871910
321805 482147
2 1
519069 146904
611921 124613
8 2
160944 628879
953003 68700
26072 638716
378921 408684
267709 553049
12419 515282
409968 42944
561655 273887
4 3
28423 2171
23948 2465
239029 3
27252 2700
6 4
25652 2961
23450 2838
255843 25
26643 2042
252830 7
21940 2537
4 1
3439 350412
3018 360697
14616 92
3783 349999
3 2
18354 326196
10166 588924
7956 752514
2 1
3103 391196
16808 77
10 5
264089 397241
649241 17172
70266 663064
417420 126820
679832 583848
448271 422661
683693 188066
901801 483030
509558 826575
637394 872377
8 3
869681 106787
936704 633636
320506 403745
210753 608721
684644 414749
909411 228808
157072 47925
341344 309826
6 4
40052 120582
580754 8316
208278 23188
70686 68324
15283 316008
34713 139128
9 5
24539 2219
24483 2122
20339 2663
291936 54
23516 2621
25203 2325
222731 38
24786 2102
29228 2621
10 6
157509 119784
106812 176638
152306 123876
529914 35604
153846 122636
59598 316572
205128 91977
210012 89838
23994 786324
53406 353276
3 2
289281 276444
194843 410433
260319 307200
6 4
615846 28044
42408 407253
23994 719796
232716 74214
340956 50654
904419 19096
10 6
69003 93912
258258 25092
262548 24682
89913 72072
18018 359652
552024 11739
489294 13244
15912 407253
23562 275028
26488 244647
4 3
370566 183131
154377 439587
109264 621084
214438 316465
8 5
22034 2794
29793 2007
22657 2344
22183 2167
23840 2027
210129 69
240981 91
23935 2189
3 2
81432 84847
15624 442221
71253 96968
3 1
27794 2843
283008 29
24406 2824
7 2
922425 489638
209356 707031
55601 262713
139073 633057
714708 21612
543344 267274
90811 60808
10 6
7866 444444
10101 346104
4788 730158
9828 355718
552552 6327
6916 505494
131054 26676
228228 15318
226044 15466
11063 316008
3 1
520109 861640
372094 50141
247096 451433
4 2
698458 845831
806027 485728
409997 24122
409623 976124
5 3
727818 28044
251937 81016
214396 95202
126936 160797
66092 308826
6 1
10224 50
3308 361480
3151 368736
3886 397529
3433 348503
12280 48
2 1
349220 200005
325518 214568""".split('\n')


# In[97]:

NumP = int(inputs[0]);
inputs = inputs[1:];


# In[98]:

problem_index = 0;
while NumP > 0:
    # number of lines to parse for each instance of problem
    N, K= [int(z) for z in inputs.pop(0).split()];
    # for each instance of problem, parse each line
    cakes = [];
    while N > 0:
        radius, height = [int(z) for z in inputs.pop(0).split()];
        whole_surface = 2*radius*height + radius**2 ;
        side_surface = 2*radius*height;
        cakes.append((radius, height, whole_surface, side_surface));
        N = N-1;
        
    # choose a bottom and do the rest
    best_so_far = 0;
    best_bottom_cake = 0;
    best_top_cakes = [];
    for cake_i, bottom_cake in enumerate(cakes):
        top_pancake_contribution = 0;
        total_area = 0;
        sorted_cakes_by_side_area = sorted([z for cake_j, z in enumerate(cakes) if cake_j != cake_i and z[0] <= bottom_cake[0]], key=lambda x: -1*x[3]);
        if len(sorted_cakes_by_side_area) < K-1:
            pass;
        else:
            if len(sorted_cakes_by_side_area) > 0:
                top_cakes = sorted(sorted_cakes_by_side_area[0:K-1], key=lambda x: -1*x[3]);
                top_pancake_contribution  = sum([z[3] for z in top_cakes]);
                
            bottom_pancake_contribution = bottom_cake[2]
            total_area = math.pi*(bottom_pancake_contribution + top_pancake_contribution);
        if total_area >= best_so_far:
            best_so_far = max(best_so_far, total_area)
            best_bottom_cake = bottom_cake;
            best_top_cakes = top_cakes
        
    print("Case #"+str(problem_index+1)+":", '{0:.9f}'.format(best_so_far));
    
    
    NumP=NumP-1;
    problem_index+=1;
    
        
        


# In[93]:

best_bottom_cake


# In[94]:

best_top_cakes


# In[89]:

best_so_far


# In[ ]:


