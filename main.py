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
            
Version:    0.0.1
Date:       2023-02-10
"""
from tkinter import *
import turtle


"""
################################
!!! BEGINNING OF GRAPHICS CODE
################################

===== TO DO !!!!
In the future, I think it would be ideal if
graphics were done in another .py file.

!!!! NOTE: Install turtle library with this command w/o quotes

FOR LINUX DISTROS/UBUNTU:
`pip install PythonTurtle`
`pip install tk`
`sudo apt-get install python3-tk

FOR WINDOWS:
Just do the pip stuff above,
but if it doesn't work, try this.

https://tkdocs.com/tutorial/install.html#installwin

===== ADDENDUM !!!!
Our code is currently using PythonTurtle libraries to
draw graphics. I might want to change this in the future
to just using multithreaded TK.
"""
# Declare 'constant' dimensions for tiles
SIDE = 100

# Declaration of turtle drawer and screen object
t = turtle.Turtle ()
win = turtle.Screen ()

# set turtle position to home and speed to slowest
# win.tracer () actually stops the animation so that
# the animation seems instantaneous
t.home ()
t.speed (0)
win.tracer (0)

"""
tile()
This sub-routine method is responsible for 
drawing a square using the turtle.

    @param      None
    @return     void
"""
def tile ():
    for i in range (4):
        t.forward (SIDE)
        t.right (90) #hiiii martin's crush is...
    t.forward (SIDE)
# === END OF METHOD

"""
This nested loop repeatedly calls
drawer method tile() depending
on the size of the board.

Currently: 8x8, standard chessboard
"""
for i in range (8):
    t.penup ()
    t.goto (0, SIDE * i)	
    t.pendown ()
    
    # Changes the color of the tile based on its 
    for j in range (8):
        if (j + i) % 2 == 0:
            color = 'black'
        else:
            color = 'white'
       
        t.fillcolor (color)
        t.begin_fill ()   
        tile ()
        t.end_fill ()
# === END OF LOOP

# hide the cursor, update the graphics, close pointer
t.hideturtle ()
win.update ()
turtle.done ()

"""
################################
!!! END OF GRAPHICS CODE
################################
"""




"""
################################
!!! BEGINNING OF FILE INPUT CODE
################################
"""

# mat is for representation of the maze
# n is the dimension of one side of mat
mat, n = [], -1

with open ("Test Cases/tc1.txt", "r+") as file:
    for line in file:
        if n == -1:
            n = int (line.strip())
        else:
            mat.append (line.strip())

# confirm proper feeding of input
print ("n =", n)
for i in mat:
    print (i)
"""
################################
!!! END OF FILE INPUT CODE
################################
"""


