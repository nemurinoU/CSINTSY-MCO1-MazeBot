import math
from graph import *

def heuristicFunction(node, end):
    h_value = math.abs(node.position.x - end.position.x) + math.abs(node.position.y - end.position.y)
    
    if len(node.connections) == 1:
        correctionFactor = node.connections[0].cost

    return h_value + correctionFactor

def determineHeuristicValues(graph):
    for vertex in graph.vertices.keys():
        graph.vertices[vertex] = heuristicFunction(vertex, graph.val)