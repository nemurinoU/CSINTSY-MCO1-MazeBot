from graph import *

def heuristicFunction(node, end):
    h_value = abs(node.position.x - end.position.x) + abs(node.position.y - end.position.y)
    correctionFactor = 0
    
    if len(node.connections) == 1 and node.type == NodeType.JUNCTION:
        correctionFactor = node.connections[0].cost

    return h_value + correctionFactor

def determineHeuristicValues(graph):
    for vertex in graph.vertexSet:
        graph.vertices[vertex] = heuristicFunction(vertex, graph.end)