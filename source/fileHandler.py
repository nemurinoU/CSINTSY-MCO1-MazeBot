"""
fileHandler.py

This module is used to load maze files.

Author(s):  Martinez, Francis Benedict V.
            Jawali, Armina
            Encinas, Robert
            Rejano, Martin
            
Version:    0.0.1
Date:       2023-02-22
"""
def print_text_grid (grid, n):
    """
    When called, prints the inputted grid file in text through CLI.

    :param  n:          Describes the dimension of a grid
    :param  grid:       Matrix containing the grid
    
    :type   n:          int
    :type   grid:       int[][]
    
    :return:            None
    :rtype:             void
    """
    print (f"n = {n}")
    for i in grid:
        print (i)

def load_file (FILE_PATH):
    """
    Loads the input file into a matrix.

    :param  FILE_PATH:          Path of the file
    
    :type   FILE_PATH:  String
    
    :return:            None
    :rtype:             void
    """
    
    # grid is for representation of the maze
    # n is the dimension of one side of mat
    grid, n = list(), -1

    with open (FILE_PATH, "r+") as file:
        for line in file:
            if n == -1:
                n = int (line.strip())
            else:      
                grid.append ([i for i in line.strip()])

    return grid, n