#!/usr/bin/env python

T = int(raw_input())
for X in range(1, T + 1):
    n = int(raw_input())
    if n == 2:
        Y = '027'
    else:
        Y = ['751', '255', '527', '143', '751', '935', '607', '903', '991', '335', '047', '943', '471', '055', '447', '463', '991', '095', '607', '263', '151', '855', '527', '743', '351', '135', '407', '903', '791', '135', '647', '343', '471', '455', '847', '263', '191', '095', '807', '463', '551', '455', '527', '343', '951', '335', '207', '903', '591', '935', '247', '743', '471', '855', '247', '063', '391', '095', '007', '663', '951', '055', '527', '943', '551', '535', '007', '903', '391', '735', '847', '143', '471', '255', '647', '863', '591', '095', '207', '863', '351', '655', '527', '543', '151', '735', '807', '903', '191', '535', '447', '543', '471', '655', '047', '663', '791', '095', '407', '063'][n % 100]
    print 'Case #%d:' % X, Y