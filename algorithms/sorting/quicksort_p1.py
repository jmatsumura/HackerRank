def partitionSort(a, n):

    left = []
    middle = a[0]
    right = []
    
    for i in range(1, n):
        
        if a[i] > middle:
            
            right.append(a[i])
            
        else:
            
            left.append(a[i])
            
    print(' '.join([str(z) for z in left]) + ' ' + str(middle) + ' ' + ' '.join([str(z) for z in right]))

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]

partitionSort(ar, m)
