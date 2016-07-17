#!/bin/python3

import sys


t = int(input().strip())
for a in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    
    numOfEarly = 0
    for i in a:
        if i < 1:
            numOfEarly += 1
            
    if (numOfEarly >= k):
        print("NO")
    else:
        print("YES")
