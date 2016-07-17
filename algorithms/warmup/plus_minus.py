#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

pos = 0
neg = 0
zer = 0
total = 0

for i in arr:
    if i==0:
        zer += 1
    elif i<0:
        neg += 1
    elif i>0:
        pos += 1
    total += 1
    
pt = pos/total
nt = neg/total
zt = zer/total
print("%.6f" % pt)
print("%.6f" % nt)
print("%.6f" % zt)
