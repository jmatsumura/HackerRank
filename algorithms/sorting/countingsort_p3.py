m = int(input().strip())

counts = {}

for i in range(0, m):
    ar = input().strip().split(' ')
    num = int(ar[0])
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
        
     
for i in range(0, 100):

    tot = 0 
    for x in range(0, i+1):
        if x in counts:
            tot += counts[x]
        
    print(tot, end=" ")
