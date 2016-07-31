#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    
    n = int(input().strip())
    
    counts = 0
    
    for x in str(n):
        if(x == '0'):
            pass
        elif(n % int(x) == 0):
            counts += 1
            
    print(counts)
