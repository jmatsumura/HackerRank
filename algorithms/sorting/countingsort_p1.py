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
            f_array.append(str(counts[i]))
        else:
            f_array.append('0')
            
    print(' '.join(f_array))

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]

countingSort(ar, m)
