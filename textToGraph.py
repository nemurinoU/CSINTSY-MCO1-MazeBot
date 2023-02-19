from graph import *

#The grid to graph parser transforms the grid to a graph representation 
def gridToGraph(n, grid, graph):
    verticalLines = []
    horizontalLines = []
    currentVerticalLine = None
    currentHorizontalLine = None
    currNode = None
    currId = 1

    for x in range(n):
        for y in range(n):
            #Vertical axis check
            #Check if starting node
            if grid[y][x] == "S":
                start = Node(0, Coordinate(x, y), NodeType.START)
            elif grid[y][x] == "E":
                end = Node(-1, Coordinate(x, y), NodeType.TERMINAL)
            elif grid[y][x] == " ":
                currNode = Node(-1, Coordinate(x, y), NodeType.EDGE_NODE)
            else:
                verticalLines.append(currentVerticalLine)
                currentVerticalLine = None

            #Process node
            counter = 0
            if currNode != None:
                #Check up
                if y - 1 > 0:
                    if grid[y - 1][x] == " ":
                        counter += 1
                
                #Check down
                if y + 1 < n:
                    if grid[y + 1][x] == " ":
                        counter += 1

                #Check left
                if x - 1 > 0:
                    if grid[y][x - 1] == " ":
                        counter += 1
                
                #Check down
                if x + 1 < n:
                    if grid[y][x + 1] == " ":
                        counter += 1
                
                if counter == 1 or counter > 2:
                    currNode.id = currId
                    currNode.type = NodeType.JUNCTION

                    if currentVerticalLine != None:
                        verticalLines.append(currentVerticalLine)
                        currentVerticalLine = None
                else:
                    if currentVerticalLine == None:
                        currentVerticalLine = Line(Coordinate(x, y), Coordinate(x, y))
                    else:
                        currentVerticalLine.end = Coordinate(x, y)

                currNode = None

            #Horizontal axis check
            #Check if starting node
            if grid[x][y] == "S":
                start = Node(0, Coordinate(y, x), NodeType.START)
            elif grid[x][y] == "E":
                end = Node(-1, Coordinate(y, x), NodeType.TERMINAL)
            elif grid[x][y] == " ":
                currNode = Node(-1, Coordinate(y, x), NodeType.EDGE_NODE)
            else:
                horizontalLines.append(currentHorizontalLine)
                currentHorizontalLine = None

            #Process node
            counter = 0
            if currNode != None:
                #Check up
                if x - 1 > 0:
                    if grid[x - 1][y] == " ":
                        counter += 1
                
                #Check down
                if x + 1 < n:
                    if grid[x + 1][y] == " ":
                        counter += 1

                #Check left
                if y - 1 > 0:
                    if grid[x][y - 1] == " ":
                        counter += 1
                
                #Check down
                if y + 1 < n:
                    if grid[x][y + 1] == " ":
                        counter += 1
                
                if counter == 1 or counter > 2:
                    currNode.id = currId
                    currNode.type = NodeType.JUNCTION

                    if currentHorizontalLine != None:
                        horizontalLines.append(currentHorizontalLine)
                        currentHorizontalLine = None
                else:
                    if currentHorizontalLine == None:
                        currentHorizontalLine = Line(Coordinate(y, x), Coordinate(y, x))
                    else:
                        currentHorizontalLine.end = Coordinate(y, x)

                currNode = None
                 
