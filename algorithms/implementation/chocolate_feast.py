#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n,c,m = input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    
    chocos = 0
    wrappers = (n/c)
    
    chocos += wrappers

    # Neatest case with no excess currency
    if(wrappers%m == 0):
        print(int(chocos+wrappers/m))
        
    # Case where, even with bonus wrappers, not enough to use promo
    elif(wrappers/m < 1):
        print(int(chocos+wrappers//m))
        
    # Final case where promo feeds into more promo
    else:

        # Handle a promo trade-in chain
        while(wrappers >= m):  
            new_wrappers = wrappers//m # round down
            chocos += new_wrappers
            wrappers -= (m*(new_wrappers))
            wrappers += new_wrappers
        
        print(int(chocos))
