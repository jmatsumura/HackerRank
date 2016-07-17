#!/bin/python3

import sys

diag1 = 0
diag2 = 0
even = False



n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
x=n-1

for i in range(n):
    diag1 += a[i][i]
    diag2 += a[x][i]
    x -= 1
diff = diag1 - diag2
print (abs(diff))
