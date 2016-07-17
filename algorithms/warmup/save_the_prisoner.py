#!/bin/python3

import sys

t = int(input().strip())

for i in range(t):
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

    n = arr[0]
    m = arr[1]
    s = arr[2]
    
    m -= 1
    
    posOfLast = m + s
    
    # Circular positioning, loop back if necessary
    if posOfLast > n:
        moduloPos = posOfLast % n
        posOfLast = moduloPos
        
        # Correct for the case where subtracting 1 early on
        # misleads and finds no remainder
        if posOfLast == 0:
            posOfLast = n
    
    print(posOfLast)
