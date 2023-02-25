from graph import *

def heuristicFunction(node, end):
    h_value = abs(node.position.x - end.position.x) + abs(node.position.y - end.position.y)
    return h_value

def determineHeuristicValues(graph):
    for vertex in graph.vertexSet:
        graph.vertices[vertex] = heuristicFunction(vertex, graph.end)