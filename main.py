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
    """
    This function returns the manhattan distance between
    two nodes.

    :param  state:      Coordinates of the current state
    :param  end:        Coordinates of the goal state
    
    :type   state:      tuple (int, int)
    :type   end:        tuple (int, int)
    
    :return:            Manhattan distance
    :rtype:             int
    """
    x1, y1 = state
    x2, y2 = end
    
    # calculate manhattan distance from the state to the goal
    return abs (x1 - x2) + abs (y1 - y2)
    

def heuristic_two (state, end):
    """
    This function returns the euclidean distance between
    two nodes.

    :param  state:      Coordinates of the current state
    :param  end:        Coordinates of the goal state
    
    :type   state:      tuple (int, int)
    :type   end:        tuple (int, int)
    
    :return:            Euclidean distance
    :rtype:             int
    """
    x1, y1 = state
    x2, y2 = end
    
    # euclidean distance
    return int(math.sqrt (pow (x2-x1, 2) + pow (y2-y1, 2)) // 1) 

def astar (grid, n):
    """
    A-star algorithm, this is where the magic happens.
    
    Using a priority queue, the bot traverses through a maze
    based on the actual cost to get there and two heuristics:
        > Euclidean distance
        > Manhattan distance
        
    The bot then makes a move based on the total cost f(n):
        
        f(n) = g(n) + h_1(n) + h_2(n)
        
        where   g(n)    -->     actual cost
                h_1(n)  -->     manhattan distance
                h_2(n)  -->     euclidean distance

    :param  grid:       Matrix containing the grid
    :param  n:          Describes the dimension of a grid
    
    :type   grid:       int[][]
    :type   n:          int
    
    :return:            tuple of visited nodes, optimal path, start node, end node, value to check if path was found, total cost
    :rtype:             tuple
    """
    
    # initialize the queue that will store
    # the total cost, heuristic cost, and node
    # f(n) = actual cost + heuristic = g(n) + h(n)
    pq = PriorityQueue ()
    
    # define the start, goal node
    # calling euclid_map generates all the coordinates for every non-wall tile in the grid
    #
    #   coords = [[0, 0], [0, 1], ..., [n, n]]
    #
    # calling direction_map generates the availability of the adjacent nodes in the cardinal directions
    #
    #   direction_map = { (0, 0) : {    'North':    0
    #                                   'South':    1
    #                                   'East':     1
    #                                   'West':     0}
    #                                   ..., (n, n)}
    
    start, goal, coords = mapper.euclid_map (grid, n)
    directions = mapper.direction_map (grid, n)
    
    # create a dictionary of the all the visited nodes
    visited = dict ()
    
    # g(n) is the actual cost, we set them all to inf at first
    # except for the starting cell where it is 0
    g_cost = {cell : float ('inf') for cell in coords}
    g_cost [start] = 0
    
    # f(n) is the total cost
    # total cost at the start has the sum of the two heuristic already
    f_cost = {cell : float ('inf') for cell in coords}
    f_cost [start] = heuristic (start, goal) + heuristic_two (start, goal)
    
    # enqueue the starting node to the queue
    # we use prio queue because we want to get the smallest total cost first
    pq.enqueue ((f_cost[start], heuristic (start, goal) + heuristic_two (start, goal), start))
    
    
    while not pq.isEmpty():
        # while the queue still has nodes, traverse through the maze
        # current cell refers to the node not yet visited with the smallest total cost
        current_cell = pq.pop ()[2]
        
        # if the current cell we're visiting is already the goal, stop the travese
        if current_cell == goal:
            break
        
        # for the cell being visited, check its cardinal directions
        # 'NSEW' is the order of directions being checked North -> South ... so on
        for dir in 'NSEW':
            
            # if the direction being checked is free
            if directions[current_cell][dir] == 1:
                
                # copy the node (child) in question
                if dir == 'E':
                    child = (current_cell[0], current_cell[1] + 1)
                if dir == 'W':
                    child = (current_cell[0], current_cell[1] - 1)
                if dir == 'N':
                    child = (current_cell[0] - 1, current_cell[1])
                if dir == 'S':
                    child = (current_cell[0] + 1, current_cell[1])
                
                # get the total cost of the node being checked
                temp_g_cost = g_cost[current_cell] + 1
                temp_f_cost = temp_g_cost + heuristic (child, goal) + heuristic_two (child, goal)
                
                # compare it with the current node
                # if the one being checked (child) is less than the current node, enqueue the child
                # and save its total cost, then add to the visited list
                if temp_f_cost < f_cost[child]:
                    g_cost[child] = temp_g_cost
                    f_cost[child] = temp_f_cost
                    pq.enqueue ((temp_f_cost, heuristic (child, goal) + heuristic_two (child, goal), child))
                    visited[child] = current_cell
    
    # declare the optimal path (aPath)
    #
    # head acts like a pointer in the visited list 
    # success tells us if we reached the goal
    aPath = dict()
    head, success = goal, True
    
    # add the goal to the optimal path
    aPath[goal] = goal
    
    
    # find the path from S to G, then store it in aPath
    while head != start:
        """
        NOTES:  How does this work?
        
        It lies in understanding the structure of aPath and visited.
        The pointer HEAD starts at the goal.
        
        
        FOR VISITED:
            visited =   { '(2, 4)' : '(3, 4)' 
                        ...                 }
                        
            For each key, its value will be the node that you are supposed to be going to.
            
            We are putting the node we are going into as the key for aPath.
            The effect of this is that aPath is in reverse, but no worries we can just
            reverse () in the GFX process.
            
            Example:
            Visited :   {   (1, 2): (2, 2), 
                            (3, 2): (2, 2), 
                            (2, 3): (2, 2), 
                            (2, 1): (2, 2), 
                            (0, 2): (1, 2), 
                            (0, 3): (0, 2), 
                            (0, 1): (0, 2), 
                            (0, 4): (0, 3)} <--- HEAD started here
                            
            Actual  :   {   (0, 4): (0, 4), 
                            (0, 3): (0, 4), 
                            (0, 2): (0, 3), 
                            (1, 2): (0, 2), 
                            (2, 2): (1, 2)}
            
        It is a bit hard to explain... but good luck trying to trace!
        """
        try:
            aPath[visited[head]] = head
            head = visited[head]
            
        except KeyError:
            success = False
            del aPath[goal]
            break
        
    
    return visited, aPath, start, goal, success, f_cost
    
if __name__ == '__main__':
    # Storing the GRID and the dimensions
    # @ grid is for representation of the maze
    # @ n is the dimension of one side of mat
    grid, n = fileHandler.load_file("Test Cases/anime.txt")

    # @ tileSize    -> the size of each tile
    # @ dims        -> the length of a window side (1:1 aspect ratio)
    tileSize = 900 // n
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
        """
        When called, this function begins the A-star algorithm
        and calls the Graphics class to draw the path calculated
        
        :return:            None
        :rtype:             void
        """
        visited, aPath = dict (), dict ()
        
        print ("Do A* w/ Manhattan and Euclidean Distance Heuristic")
        
        # @visited, aPath are the path node tables
        # @start, goal is just the beginning nodes and end nodes
        # @succ tells us if it has found a path or not
        # @totalC is the list of total costs for each node in the graph
        # 
        # all obtained from the astar() function
        visited, aPath, start, goal, succ, totalC = astar (grid, n)
        

        # Declare speed based on the size of the grid and the number of digits
        speed = n / (n * 20 * len(str(n)))
        
        # this paints the visited nodes onto the canvas
        for node in visited:
            if node != start and node != goal:
                time.sleep (speed)
                gfx.drawTile (node[0], node[1], "red")
                gfx.canvas.create_text (node[1] * tileSize + tileSize // 2, node[0] * tileSize + tileSize // 2, text=f"{totalC[node]}", font=('Impact', -tileSize + 5), fill="white")

        # likewise for the optimal path
        for node in reversed (aPath):
            if node != start and node != goal:
                time.sleep (speed)
                gfx.drawTile (node[0], node[1], "green")
                gfx.canvas.create_text (node[1] * tileSize + tileSize // 2, node[0] * tileSize + tileSize // 2, text=f"{totalC[node]}", font=('Impact', -tileSize + 5), fill="white")
        
        # show feedback: path found? visited nodes? optimal path count?
        succ = "Path found!" if succ else "Cannot reach goal!"
        message = f"Nodes Visited: {len (visited) + 1}\nOptimal Path: {len (aPath)}"
        tkinter.messagebox.showinfo (succ, message)
        
        myLabel = Label(root, text = message, font=('Impact', -13))
        myLabel.pack()
        
        print (message)

    # Threading
    # Start a new threat that calls the start () which is responsible for everything A* and drawing
    main_thread = threading.Thread (target=start)
    main_thread.daemon = True
    main_thread.start ()
    
    root.mainloop ()