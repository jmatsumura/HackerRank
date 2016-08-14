n = int(input().strip())

for x in range(0, n):
    
    m = int(input().strip())
    ar = [int(i) for i in input().strip().split()]
    z = len(ar)
    
    found = "NO"
    ls = 0 # left side and right side sums
    rs = 0
    summed = False
    
    for j in range(0,z):
        
        if(j == 0): # right must equal 0
            
            if(sum(ar[1:z]) == 0):
                found = "YES"
                break
            
        elif(j == z-1): # left must equal 0
            
            if(sum(ar[0:z-1]) == 0):
                found = "YES" # at the end, no need to break
            
        else: 
            if(summed == True):
                ls += ar[j-1]
                rs -= ar[j]
                
            else: # only need to iterate over array once, then add/subtract single values
                ls = sum(ar[0:j]) # careful with inclusive/exclusive idxs
                rs = sum(ar[j+1:z])
                summed = True
            
            if(ls == rs):
                found = "YES"
                break # only need to find one instance of balance
            
    print(found)
