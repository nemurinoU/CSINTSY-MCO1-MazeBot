from enum import Enum
import math

class Graph:
    vertices = {}
    
    def add_vertex (self, v):
        if isinstance(v, Node) and v.data not in self.vertices:
            self.vertices[v.data] = v
            return True
        else:
            return False
            
    def add_edge (self, u, v):
        if u in self.vertices and v in self.vertices:
            for k, v in self.vertices.items():
                if k == u:
                    v.add_connection (v)
                if k == v:
                    v.add_connection (u)
            return True
        else:
            return False
            
    def print_graph (self):
        for k in sorted(list(self.vertices.keys())):
            print (k + str(self.vertices[k].connections))

class NodeType (Enum):
    START = 0
    TERMINAL = 1
    REGULAR = 2

class Coordinate:
    def __init__ (self, val, x, y):
        self.data = val
        self.x = x
        self.y = y

class Node:
    def __init__ (self, val, id, position, nodeType):
        self.data = val
        #self.id refers to the numerical code (index) of the node in the adjacency matrix
        self.id = id
        #self.position is the Coordinate of the Node
        self.position = position
        #self.connections would be an array of Edges
        self.connections = [] 
        #self.type identifies if the node is the starting node, ending node, or just a regular node
        self.type = nodeType
        
    def add_connection (self, edge):
        if edge not in self.connections:
            self.connections.append (edge)

class Line:
    def __init__ (self, val, start, end):
        self.data = val
        #self.start is the Coordinate of the starting point of the line
        self.start = start
        #self.end is the Coordinate of the ending point of the line
        self.end = end

class Edge:
    def __init__ (self, val, nodes):
        self.data = val
        #self.nodes is a 2 element array of the 2 Nodes that the edge joins together
        self.nodes = nodes
        #self.lines is the array of lines that makes up the edge (Note: Lines must be in correct traversal order)
        self.lines = []
        #self.cost is the cost to traverse this Edge
        self.cost = 0

    def addLines (self, line):
        self.lines.append(line)

    def getCost (self):
        for line in self.lines:
            self.cost += math.abs(line.start[0] - line.end[0]) + math.abs(line.start[1] - line.end[1]) 

#The dot that traverses the graph
class Pointer:
    def __init__ (self, val, position):
        self.data = val
        #self.position is the Coordinate of where the Pointer is currently at
        self.position = position

    def traverse (self, edge):
        if self.position == edge.nodes[0]:
            self.position = edge.nodes[1]
        else:
            self.position = edge.nodes[0]

        