#!/usr/bin/python
def displayPathtoPrincess(n,grid):
    i = n-1 # correct for 0-index
    m = ((n+1)/2)-1 # find the position of mario. e.g. (m,m)
    # know exactly how far peach can possibly be
    distance = int(i-m) # remember it's a square, only need one dimension to know both
    if grid[i][0] == "p": # bottom-left
        for j in range(0,distance):
            print("DOWN")
            print("LEFT")
    elif grid[i][i] == "p": # bottom-right
        for j in range(0,distance):
            print("DOWN")
            print("RIGHT")    
    elif grid[0][0] == "p": # top-left
        for j in range(0,distance):
            print("UP")
            print("LEFT")      
    elif grid[0][i] == "p": # top-right
        for j in range(0,distance):
            print("UP")
            print("RIGHT") 

#print all the moves here
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
