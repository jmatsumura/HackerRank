#!/bin/python3

import sys

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

still_jumping = True
i=0
j=0

while(still_jumping):
    
    if(i == (len(c)-1)):
        still_jumping = False
    elif((i+2 <= (len(c)-1))) and (c[i+2] == 0):
        i += 2
        j += 1
    elif((i+1 <= (len(c) -1)) and (c[i+1] == 0)):
        i += 1
        j += 1
             
print(j)
