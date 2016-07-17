#!/bin/python3

import sys


n = int(input().strip())

numOfSpaces = 0
numOfHashes = 0

for i in range (1, n+1):
    string=''
    numOfSpaces = (n-i)
    numOfHashes = i
    string += " " * numOfSpaces
    string += "#" * numOfHashes
    print(string)
