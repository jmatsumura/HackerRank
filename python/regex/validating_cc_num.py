#!/bin/python3

import sys,re

# Function to guarantee none of the same number occurs 4 times in a row
def noRepeats(num):
    for x in range(0,11):
        
        # iterate through, and make sure no repeats of 4-in-a-row
        if num[x] == num[x+1]:
            if num[x+1] == num[x+2]:
                if num[x+2] == num[x+3]:
                    print('Invalid')
                    return

    print('Valid')
    return

cases = int(input())

# Go over the input and validate all CCs
for test in range(0,cases):
    card_num = input()
  
    # First meet the criteria that it must start with a 4, 5, or 6
    if not re.search(r'^[456]+',card_num):
        print('Invalid')
        continue
    
    # First handle cases with dashes embedded.
    if '-' in card_num:
        
        # If there are dashes, make sure each separates 4 digits
        if not re.search(r'^\d{4}-{1}\d{4}-{1}\d{4}-{1}\d{4}$',card_num):
            print('Invalid')
            
        # Have a valid hyphen area, now make sure no repeats
        else:
            card_num = card_num.replace('-','')
            noRepeats(card_num)
                
        continue
            
    # No hyphens, the length of the string must be 16 then. If it indeed is,
    # make sure there are no repeats. 
    if re.search(r'^\d{16}$',card_num):
        noRepeats(card_num)
    else:
        print('Invalid')
    
