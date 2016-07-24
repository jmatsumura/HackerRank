#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]

still_jumping = True
i=0
t=0
j=0
e=100

while(still_jumping):

    if((len(c) == (i+k))):
        still_jumping = False
    else:

        if((c[i+k]) == 0):
            i += k
        else:
            i += k
            t += 1
            
    j += 1
    
# Account for last spot landing on thundercloud
if(c[0] == 1):
    t += 1
    
print(e-(1*j)-(2*t))
