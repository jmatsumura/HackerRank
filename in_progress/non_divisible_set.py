#!/bin/python3

import sys
from itertools import combinations

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
nums = [int(nums_temp) for nums_temp in input().strip().split(' ')]

x = {}

for var in combinations(nums, 2):
    n1 = var[0]
    n2 = var[1]
    if ((n1 + n2)%k) == 0:
        
        if n1 in x:
            val = (x[n1] + 1)
            x.update({n1:val})
        else:
            x.update({n1:1})
        if n2 in x:
            val = (x[n2] + 1)
            x.update({n2:val})
        else:
            x.update({n2:1})
            
for k in x:
    if x[k] > 1:
        n -= 1
        
print(n)
