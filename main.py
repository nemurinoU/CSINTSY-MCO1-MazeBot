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

import time
import threading
import tkinter.messagebox
import fileHandler


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

def start():
    print ("Do A*")

if __name__ == '__main__':
    # Storing the GRID and the dimensions
    # @ grid is for representation of the maze
    # @ n is the dimension of one side of mat
    grid, n = fileHandler.load_file("Test Cases/tc1.txt")

    # @ tileSize    -> the size of each tile
    # @ dims        -> the length of a window side (1:1 aspect ratio)
    tileSize = 300 / n
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

    # Threading
    main_thread = threading.Thread (target=start)
    main_thread.daemon = True
    main_thread.start ()
    
    root.mainloop ()

    



