"""
Major Course Output 1: MazeBot

This program will take a text file input
of an n x n grid to simulate a maze.
Output is a visualization of a search
algorithm from a START state to an
END goal.

Author(s):  Martinez, Francis Benedict V.
            Jawali, Armina
            Encinas, Robert
            Rejano, Martin
            
Version:    TK-0.0.1 CONTROL TEST
Date:       2023-02-10
"""
from tkinter import *
from graphics import Graphics
from customq import PriorityQueue

import time
import threading
import tkinter.messagebox
import fileHandler
import mapper
import math


"""
===== TO DO !!!!
In the future, I think it would be ideal if
graphics were done in another .py file.

!!!! NOTE: Install tkinter library with this command w/o quotes

FOR LINUX DISTROS/UBUNTU:
`pip install tk`
`sudo apt-get install python3-tk

FOR WINDOWS:
Just do the pip stuff above,
but if it doesn't work, try this.

https://tkdocs.com/tutorial/install.html#installwin
"""

def heuristic (state, end):
    x1, y1 = state
    x2, y2 = end
    
    # calculate manhattan distance from the state to the goal
    return abs (x1 - x2) + abs (y1 - y2)
    #return math.sqrt (pow (x2-x1, 2) + pow (y2-y1, 2))

def astar (grid, n):
    # initialize the queue that will store
    # the total cost, heuristic cost, and node(?)
    # f(n) = actual cost + heuristic = g(n) + h(n)
    pq = PriorityQueue ()
    
    # define the start, goal, and all other coordinates
    start, goal, coords = mapper.euclid_map (grid, n)
    directions = mapper.direction_map (grid, n)
    
    visited = dict ()
    
    # g(n) is the actual cost
    g_cost = {cell : float ('inf') for cell in coords}
    g_cost [start] = 0
    
    # f(n) is the total cost
    f_cost = {cell : float ('inf') for cell in coords}
    f_cost [start] = heuristic (start, goal)
    
    pq.enqueue ((f_cost[start], heuristic (start, goal), start))
    
    while not pq.isEmpty():
        current_cell = pq.pop ()[2]
        
        if current_cell == goal:
            break
        
        for dir in 'NSEW':
            if directions[current_cell][dir] == 1:
                if dir == 'E':
                    child = (current_cell[0], current_cell[1] + 1)
                if dir == 'W':
                    child = (current_cell[0], current_cell[1] - 1)
                if dir == 'N':
                    child = (current_cell[0] - 1, current_cell[1])
                if dir == 'S':
                    child = (current_cell[0] + 1, current_cell[1])
                
                temp_g_cost = g_cost[current_cell] + 1
                temp_f_cost = temp_g_cost + heuristic (child, goal)
                
                if temp_f_cost < f_cost[child]:
                    g_cost[child] = temp_g_cost
                    f_cost[child] = temp_f_cost
                    pq.enqueue ((temp_f_cost, heuristic (child, goal), child))
                    visited[child] = current_cell
    
    print (f_cost)
    aPath = dict()
    head = goal
    success = True
    
    #print ("visited", visited)
    aPath[goal] = goal
    
    while head != start:
        try:
            aPath[visited[head]] = head
            head = visited[head]
        except KeyError:
            success = False
            del aPath[goal]
            break
    
    #print ("aPath", aPath)
    
    return visited, aPath, start, goal, success
    
if __name__ == '__main__':
    # Storing the GRID and the dimensions
    # @ grid is for representation of the maze
    # @ n is the dimension of one side of mat
    grid, n = fileHandler.load_file("Test Cases/20x20.txt")

    # @ tileSize    -> the size of each tile
    # @ dims        -> the length of a window side (1:1 aspect ratio)
    tileSize = 600 / n
    dims = n * tileSize

    # Initializing GUI using TKinter
    # I'm not qualified enough to explain what it does under the hood, just know we call the window using this
    root = Tk ()
    
    # Set the window title
    root.title ("A*-Maze-ing Bot")

    # Initialize a drawable canvas
    myCanvas = tkinter.Canvas (root, bg="grey", height = dims, width = dims)
    myCanvas.pack ()
    
    # initalize Graphics class
    # and begin drawing the grid
    gfx = Graphics (tileSize, myCanvas)
    gfx.makeTiles (n, grid)

    def start ():
        visited, aPath = dict (), dict ()
        
        print ("Do A* w/ Manhattan Distance Heuristic")
        visited, aPath, s, g, succ = astar (grid, n)
        
        speed = n / (n * 10 * len(str(n)))
        
        for i in visited:
            if i != s and i != g:
                time.sleep (speed)
                gfx.drawTile (i[0], i[1], "red")

        for i in reversed (aPath):
            if i != s and i != g:
                time.sleep (speed)
                gfx.drawTile (i[0], i[1], "green")
        
        succ = "Path found!" if succ else "Cannot reach goal!"
        message = f"Nodes Visited: {len (visited) + 1}\nShortest Path: {len (aPath)}"
        tkinter.messagebox.showinfo (succ, message)
        
        print (message)
            
    # Threading
    main_thread = threading.Thread (target=start)
    main_thread.daemon = True
    main_thread.start ()
    
    root.mainloop ()