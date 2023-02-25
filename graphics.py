"""
graphics.py

This module is used to bridge the maze representation
to a GUI representation.

Author(s):  Martinez, Francis Benedict V.
            Jawali, Armina
            Encinas, Robert
            Rejano, Martin
            
Version:    0.0.1
Date:       2023-02-22
"""
class Graphics:
    def __init__ (self, tileSize, canvas):
        self.tileSize = tileSize
        self.canvas = canvas
        
    def makeTiles (self, n, grid):
        """
        When called, it draws all the tiles for a grid.

        :param  n:          Describes the dimension of a grid
        :param  grid:       Matrix containing the grid
        
        :type   n:          int
        :type   grid:       int[][]
        
        :return:            None
        :rtype:             void
        """
        colors = {'.':'Grey','G':'Magenta','S':'Orange','#':'Black'}
        
        for row in range (n):
            for col in range (n):
                self.drawTile (row, col, colors[grid[row][col]])

    def drawTile (self, row, col, color):
        """
        Subroutine for makeTiles()
        
        Creates a rectangle object in the canvas.
        
        :param  row:        Index of the i-th row
        :param  col:        Index of the j-th column
        :param  color:      Color of a tile
        
        :type   row:        int
        :type   col:        int
        :type   color:      String
        
        :return:            None
        :rtype:             void
        """
        x1 = col * self.tileSize
        y1 = row * self.tileSize
        
        x2 = x1 + self.tileSize
        y2 = y1 + self.tileSize
        
        self.canvas.create_rectangle (x1, y1, x2, y2, fill=color)
        