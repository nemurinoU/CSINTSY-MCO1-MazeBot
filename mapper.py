"""
mapper.py

This module is used to bridge the maze representation
to graph representation or rather priority queue.

Grid -> Euclidean Space Hashmap
    i.e., gives cells coordinates
Grid -> Direction Hashmap
    i.e., @ (1, 5), South: FREE, North, INACCESSIBLE... etc

Author(s):  Martinez, Francis Benedict V.
            Jawali, Armina
            Encinas, Robert
            Rejano, Martin
            
Version:    0.0.1
Date:       2023-02-22
"""

def isEdge (coord, n):
    x, y = coord
    res = False
    
    if x == 0 or x == n:
        res = True
    
    if y == 0 or y == n:
        res = True
        
    return res

def direction_map (grid, n):
    temp = dict ()
    curr = ()
    
    for i in range (n):
        for j in range (n):
            curr = grid[i][j]
            coord = (i, j)
            if curr != '#':
                temp[coord] = {k : 0 for k in 'NSEW'}
                
                if isEdge (coord, n - 1):
                    if j != n - 1: # if left edge, check east
                        if grid[i][j + 1] != '#': # East
                            temp[coord]['E'] = 1
                    if j > 0 and j <= n - 1: # if right edge, check west
                        if grid[i][j - 1] != '#': # West
                            temp[coord]['W'] = 1
                            
                    if i != n - 1: # if top edge, check south
                        if grid[i + 1][j] != '#':
                            temp[coord]['S'] = 1
                    if i > 0 and i <= n - 1: # if bottom edge, check north
                        if grid[i - 1][j] !='#':
                            temp[coord]['N'] = 1
                else:
                    if grid[i - 1][j] != '#': # North
                        temp[coord]['N'] = 1
                    if grid[i + 1][j] != '#': # South
                        temp[coord]['S'] = 1
                    if grid[i][j + 1] != '#': # East
                        temp[coord]['E'] = 1
                    if grid[i][j - 1] != '#': # West
                        temp[coord]['W'] = 1
    
    return temp

def euclid_map (grid, n):
    temp = []
    s, g = (), ()
    
    for i in range (n):
        for j in range (n):
            if grid[i][j] == 'S':
                s = (i, j)
            elif grid[i][j] == 'G':
                g = (i, j)
            
            if grid[i][j] != '#':
                temp.append ((i, j))
                
    return s, g, temp