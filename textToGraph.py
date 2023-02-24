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
            if currNode != None:
                #Check up
                if y - 1 > 0:
                    if grid[y - 1][x] == " ":
                        currNode.adjacents.append(Coordinate(x, y - 1))
                
                #Check down
                if y + 1 < n:
                    if grid[y + 1][x] == " ":
                        currNode.adjacents.append(Coordinate(x, y + 1))

                #Check left
                if x - 1 > 0:
                    if grid[y][x - 1] == " ":
                        currNode.adjacents.append(Coordinate(x - 1, y))
                
                #Check down
                if x + 1 < n:
                    if grid[y][x + 1] == " ":
                        currNode.adjacents.append(Coordinate(x + 1, y))
                
                if currNode.adjacents.count == 1 or currNode.adjacents.count > 2:
                    currNode.id = currId
                    currNode.type = NodeType.JUNCTION

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
                        currNode.adjacents.append(Coordinate(y, x - 1))
                
                #Check down
                if x + 1 < n:
                    if grid[x + 1][y] == " ":
                        currNode.adjacents.append(Coordinate(y, x + 1))

                #Check left
                if y - 1 > 0:
                    if grid[x][y - 1] == " ":
                        currNode.adjacents.append(Coordinate(y - 1, x))
                
                #Check down
                if y + 1 < n:
                    if grid[x][y + 1] == " ":
                        currNode.adjacents.append(Coordinate(y + 1, x))
                
                if currNode.adjacents.count == 1 or currNode.adjacents.count > 2:
                    currNode.id = currId
                    currNode.type = NodeType.JUNCTION

                currNode = None
                 
