#!/bin/python3

import sys

x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

# First account for the case where kangaroo 1 starts ahead and is faster
if (x1 > x2 and v1 > v2):
    print("NO")
    
# Now if kangaroo 2 starts ahead and is faster
elif (x2 > x1 and v2 > v1):
    print("NO")

# Account for the case where they start at same pos and aren't equal in speed
elif (x1 == x2 and (v1 > v2 or v2 > v1)):
    print("NO")
    
# Case of same velocity but one starts ahead of the other
elif (v1 == v2 and (x1 > x2 or x2 > x1)):
    print("NO")
    
# Account for most obvious equivalent case
elif (x1 == x2 and v1 == v2):
    print("YES")
    
# Now the more complicated case, not a clear "NO" so calculate positions over time
# Remember that they need to accomplish this in the same number of jumps
else:
    
    notOverlapped = True
    jumps = 1

    while(notOverlapped):
        
        kang1 = (x1 + jumps * v1)
        kang2 = (x2 + jumps * v2)
            
        if (kang1 == kang2):
            print("YES")
            notOverlapped = False
    
        # Need to stop if the faster one passes the slower one    
        elif ((kang1 > kang2 and v1 > v2) or (kang2 > kang1 and v2 > v1)):
            print("NO")
            notOverlapped = False
            
        else:
            # increment counter each time they are not yet at or passed one another
            jumps += 1
