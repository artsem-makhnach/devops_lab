#!/bin/python

import sys


n = int(raw_input().strip())
a = []
temp1 = 0
temp2 = 0
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
    temp1 += a_temp[a_i]
    temp2 += a_temp[n-1-a_i]
print (abs(temp1-temp2))