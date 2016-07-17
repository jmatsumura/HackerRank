#!/bin/python3

import sys

total = 0

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

if n == len(arr):
    # everything is fine
    for i in arr:
        total += int(i)
else:
    print ("please enter the correct array length")
    sys.exit(0)
    
print (total)
