from graph import *
from heuristic import *

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
            currentLine = Line(coord, coord)
            previous = j.position
            next = coord
            currentEdge.nodes[0] = nodeGrid[previous.x][previous.y]
            
            end = False
            while not end:
                if nodeGrid[next.x][next.y].type != NodeType.EDGE_NODE:
                    currentEdge.nodes[1] = nodeGrid[next.x][next.y]
                    currentEdge.addLines(currentLine)
                    end = True
                else:
                    if hasTurn(currentLine, next):
                        currentEdge.addLines(currentLine)
                        currentLine = Line(next, next)
                    else:
                        currentLine.end = next

                if not end:
                    if len(nodeGrid[next.x][next.y].adjacents) == 1:
                        previous = next
                        next = nodeGrid[next.x][next.y].adjacents[0]
                    elif nodeGrid[next.x][next.y].adjacents[0].x == previous.x and nodeGrid[next.x][next.y].adjacents[0].y == previous.y:
                        previous = next
                        next = nodeGrid[next.x][next.y].adjacents[1]
                    else:
                        previous = next
                        next = nodeGrid[next.x][next.y].adjacents[0]
            
            currentEdge.getCost()
            j.connections.append(currentEdge)
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
            if grid[x][y] == "S":
                nodeGrid[x].append(Node(0, Coordinate(x, y), NodeType.START))
                start = nodeGrid[x][y]
            elif grid[x][y] == "G":
                nodeGrid[x].append(Node(-1, Coordinate(x, y), NodeType.TERMINAL))
                end = nodeGrid[x][y]
            elif grid[x][y] == ".":
                nodeGrid[x].append(Node(-10, Coordinate(x, y), NodeType.EDGE_NODE))
            else:
                nodeGrid[x].append(Node(-10, Coordinate(x, y), NodeType.WALL))

            #Process node
            if nodeGrid[x][y].type != NodeType.WALL:
                #Check up
                if y - 1 >= 0:
                    if grid[x][y - 1] != "#":
                        nodeGrid[x][y].adjacents.append(Coordinate(x, y - 1))
                
                #Check down
                if y + 1 < n:
                    if grid[x][y + 1] != "#":
                        nodeGrid[x][y].adjacents.append(Coordinate(x, y + 1))

                #Check left
                if x - 1 >= 0:
                    if grid[x - 1][y] != "#":
                        nodeGrid[x][y].adjacents.append(Coordinate(x - 1, y))
                
                #Check down
                if x + 1 < n:
                    if grid[x + 1][y] != "#":
                        nodeGrid[x][y].adjacents.append(Coordinate(x + 1, y))
                
                if len(nodeGrid[x][y].adjacents) == 1 or len(nodeGrid[x][y].adjacents) > 2 or nodeGrid[x][y].type == NodeType.START or nodeGrid[x][y].type == NodeType.TERMINAL:
                    nodeGrid[x][y].id = currId

                    if nodeGrid[x][y].type == NodeType.EDGE_NODE:
                        nodeGrid[x][y].type = NodeType.JUNCTION

                    junctionList.append(nodeGrid[x][y])
                    currId += 1

    edges = defineEdges(junctionList, nodeGrid)

    g = Graph(edges, junctionList, start, end)
    determineHeuristicValues(g)

    return g