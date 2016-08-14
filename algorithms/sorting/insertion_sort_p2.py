def insertionSort(l):

    x = len(l) # requirement said fxn can only take 1 parameter

    for i in range(1, x):
        
        inserted = False

        if(i == 1):
            if(l[0] > l[1]):
                t = l[1]
                l[1] = l[0]
                l[0] = t

        else:
            j = i
            while(inserted == False):
                
                if(l[j] > l[j-1]): # already in order
                    inserted = True
                else: # move back one step at a time
                    t = l[j]
                    l[j] = l[j-1]
                    l[j-1] = t
                    
                j = j - 1
                
                if(j == 0): # if we hit the first index, then we're done checking all
                    inserted = True
                    
        print(' '.join([str(x) for x in l]) )
                
        
m = int(input().strip())
ar = [int(i) for i in input().strip().split()]

insertionSort(ar)
