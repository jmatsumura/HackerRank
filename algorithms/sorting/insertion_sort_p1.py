def insertionSort(l):
    
    x = len(l) # requirement said fxn can only take 1 parameter
    e = l[x-1]
    
    if(e < l[x-2]):
        l[x-1] = l[x-2]
        
    for i in range(1, x):
              
        j = x-i-1 # account for python idx
        
        if(j > 0):
            print(' '.join([str(x) for x in l]) )
           
            if(l[j-1] < e):
                l[j] = e
                print(' '.join([str(x) for x in l]) )
                break
            else:
                l[j] = l[j-1]
                
        else: # hit the end, final check
            if(l[0] < e):
                l[1] = e
            else:
                print(' '.join([str(x) for x in l]) )
                l[1] = l[0]
                l[0] = e
                
            print(' '.join([str(x) for x in l]) )
            
m = int(input().strip())
ar = [int(i) for i in input().strip().split()]

insertionSort(ar)
