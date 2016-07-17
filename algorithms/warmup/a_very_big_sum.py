#!/bin/python3

import sys

total = 0

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
if n == len(arr):
    for i in arr:
        total += i
    print (total)
else:
    "Error please enter the correct length of array specified by first input"
