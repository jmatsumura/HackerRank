t = int(input().strip()) # trips

for t in range(0,t):
    
    prices = {} # new batch of variables for each iteration
    p1 = 0
    p2 = 0

    m = int(input().strip()) # $
    n = int(input().strip()) # num of flavors
    ar = [int(i) for i in input().strip().split()]
    
    # Build a hash table with costs as keys and values as indices.
    # Note that values can be an array to account for dupes. 
    for i in range(0, n):
        prices.setdefault(ar[i], []).append(i)
        
    for k in prices:
        
        diff = m - k
        
        if diff in prices:
      
            if diff == k: # dupes
                indices = prices[k]
                p1 = indices[0]
                p2 = indices[1]
                break
                
            else:
                p1 = prices[k][0]
                p2 = prices[diff][0]
                break
           
    p1 += 1
    p2 += 1 
    
    if p1 > p2: # print in ascending order
        print('{} {}'.format(p2, p1))
    else:
        print('{} {}'.format(p1, p2))
