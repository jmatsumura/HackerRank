#!/bin/python3

import sys

a_ar = input().strip().split(' ')
b_ar = input().strip().split(' ')

a=0
b=0

for i in range(0,len(a_ar)):
    av,bv = [int(a_ar[i]),int(b_ar[i])]
    if av > bv:
        a+=1
    elif av < bv:
        b+=1
        
print("%d %d" % (a,b))
