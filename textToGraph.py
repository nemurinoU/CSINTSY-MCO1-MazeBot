from graph import *

def hasTurn(line, next):
    if line.start.x - next.x != 0 and line.start.y - next.y != 0:
        return True
    else:
        return False

def defineEdges(junctionList, nodeGrid):
    edges = []
    currentLine = None

    for j in junctionList:
        for coord in j.adjacents:
            currentEdge = Edge()
            currentEdge.nodes[0] = nodeGrid[coord.x][coord.y]
            currentLine = Line(coord, coord)
            previous = coord
            
            end = False
            while not end:
                if nodeGrid[previous.x][previous.y].adjacents[0] == previous:
                    next = nodeGrid[previous.x][previous.y].adjacents[0]
                else:
                    next = nodeGrid[previous.x][previous.y].adjacents[1]

                if nodeGrid[next.x][next.y].type == NodeType.JUNCTION:
                    currentEdge.nodes[1] = nodeGrid[next.x][next.y]
                    end = True
                else:
                    if hasTurn(currentLine, next):
                        currentEdge.addLines(currentLine)
                        currentLine = Line(next, next)
                    else:
                        currentLine.end = next

                    previous = next

            edges.append(currentEdge)
    
    return edges

#The grid to graph parser transforms the grid to a graph representation 
def gridToGraph(n, grid):
    currId = 1
    junctionList = []
    nodeGrid = []

    for x in range(n):
        nodeGrid.append([])
        for y in range(n):
            if grid[y][x] == "S":
                nodeGrid[x].append(Node(0, Coordinate(x, y), NodeType.START))
            elif grid[y][x] == "E":
                nodeGrid[x].append(Node(-1, Coordinate(x, y), NodeType.TERMINAL))
            elif grid[y][x] == " ":
                nodeGrid[x].append(Node(-10, Coordinate(x, y), NodeType.EDGE_NODE))

            #Process node
            if nodeGrid[x][y].type == NodeType.EDGE_NODE:
                #Check up
                if y - 1 > 0:
                    if grid[y - 1][x] == " ":
                        nodeGrid[x][y].adjacents.append(Coordinate(x, y - 1))
                
                #Check down
                if y + 1 < n:
                    if grid[y + 1][x] == " ":
                        nodeGrid[x][y].adjacents.append(Coordinate(x, y + 1))

                #Check left
                if x - 1 > 0:
                    if grid[y][x - 1] == " ":
                        nodeGrid[x][y].adjacents.append(Coordinate(x - 1, y))
                
                #Check down
                if x + 1 < n:
                    if grid[y][x + 1] == " ":
                        nodeGrid[x][y].adjacents.append(Coordinate(x + 1, y))
                
                if nodeGrid[x][y].adjacents.count == 1 or nodeGrid[x][y].adjacents.count > 2:
                    nodeGrid[x][y].id = currId
                    nodeGrid[x][y].type = NodeType.JUNCTION
                    junctionList.append(nodeGrid[x][y])
                    currId += 1
    
    edges = defineEdges(junctionList, nodeGrid)
            
