#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

validPairs = 0

# remember for range the stop is exclusive
for i in range(0,n):
    
    for j in range(i+1, n):

        if (((a[i]+a[j]) % k) == 0):
            validPairs += 1
            
print(validPairs)
