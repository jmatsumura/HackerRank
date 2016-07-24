#!/bin/python3

import sys

n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]
    
# Need to calc an initial sum for first check
sh1 = sum(h1)
sh2 = sum(h2)
sh3 = sum(h3)

if(sh1 != sh2 and sh2 != sh3):
    not_equal = False
else:
    print(sh3)
    sys.exit()

# When altering these lists, use pop instead of delete since this
# will remove the need to do a full sum each time (can just do simple -)
while(not_equal == False):
    
    if(sh1 > sh2 and sh1 > sh3):
        sh1 = sh1 - h1.pop(0)
        
    elif(sh2 > sh1 and sh2 > sh3):
        sh2 = sh2 - h2.pop(0)
        
    elif(sh3 > sh1 and sh3 > sh2):
        sh3 = sh3 - h3.pop(0)
        
    elif(sh1 == sh2 and sh2 > sh3):
        sh1 = sh1 - h1.pop(0)
        sh2 = sh2 - h2.pop(0)
        
    elif(sh2 == sh3 and sh3 > sh1):
        sh2 = sh2 - h2.pop(0)
        sh3 = sh3 - h3.pop(0)

    elif(sh1 == sh3 and sh1 > sh2):
        sh1 = sh1 - h1.pop(0)
        sh3 = sh3 - h3.pop(0)
               
    if(sh1 == sh2 and sh2 == sh3):
        print(sh3)
        not_equal = True
