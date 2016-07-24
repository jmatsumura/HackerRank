#!/bin/python3

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

# Print out initial amount
print(n)

while(sum(i for i in arr if i > 0) > 0):
    
    curr_count = 0
    curr_min = max(arr) # start high and work way down
    
    # Since I can't use numpy, have to go about finding min old fashioned way.
    for i in arr:
        if(i > 0 and i < curr_min):
            curr_min = i
                
    # Now cut the sticks
    arr[:] = [x - curr_min for x in arr]    
    
    # Performing this count before doesn't accommodate last stick
    for i in arr:
        if(i > 0):
            curr_count += 1
    
    if(curr_count != 0):
        print(curr_count)
