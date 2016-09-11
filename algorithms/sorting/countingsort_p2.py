def countingSort(a, n):

    counts = {}
    f_array = []
    
    for i in range(0, n):
        if a[i] in counts:
            counts[a[i]] += 1    
        else: 
            counts[a[i]] = 1
            
    for i in range(0, 100):
        if i in counts:
            for x in range(0, counts[i]):
                f_array.append(str(i))
                
    print(' '.join(f_array))

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]

countingSort(ar, m)
