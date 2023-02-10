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
from random import randint
import time
import threading

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

root = Tk ()

root.title ("A-Maze-ing Bot")
root.geometry ("1366x768")

def five_secs ():
    time.sleep (5)
    my_label.config (text = "5 seconds have passed. WRYYY")

def rando ():
    random_label.config (text = f'Random Number: {randint(1, 100)}')

my_label = Label (root, text = "Hello there!")
my_label.pack (pady = 20)

my_button1 = Button (root, text = "5 seconds", command=threading.Thread(target=five_secs).start())
my_button1.pack (pady = 20)

my_button2 = Button (root, text="Pick Random Number", command=rando)
my_button2.pack (pady = 20)

random_label = Label (root, text = '')
random_label.pack (pady = 20)

root.mainloop ()

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
print (f"n = {n}")
for i in mat:
    print (i)
"""
################################
!!! END OF FILE INPUT CODE
################################
"""


