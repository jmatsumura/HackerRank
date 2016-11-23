#!/usr/bin/python

# Can take advantage of how relative position to mario
# is revealing for left/right (-/+) and up/down (+/-).
def nextMove(n,r,c,grid):
    
    # first goal is to find peach
    ppos = (0,0)
    for x in range(0,n):
        for j in range(0,n):
            if grid[x][j] == "p":
                ppos = (x,j)
                break # can leave once found
    # find the difference in rows and columns, relative to peach
    ver = ppos[0]-r
    hor = ppos[1]-c

    # Note return statements will limit to just the next move
    if ver != 0: # need to move rows?
        if ver < 0:
            print("UP")
            return
        else:
            print("DOWN")
            return
                
    if hor != 0: # need to move columns?
        if hor < 0:
            print("LEFT")
            return
        else:
            print("RIGHT")
            return

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []

for i in range(0, n):
    grid.append(input())

nextMove(n,r,c,grid)
