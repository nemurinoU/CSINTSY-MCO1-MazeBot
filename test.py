from textToGraph import *

grid = [[".", ".", ".", ".", "G"],
        ["#", ".", "#", "#", "#"],
        [".", ".", ".", "#", "S"],
        [".", "#", ".", "#", "."],
        [".", "#", ".", ".", "."],]

g = gridToGraph(5, grid)

for e in g.edges:
    print(f"({e.nodes[0].position.x}, {e.nodes[0].position.y}) to ({e.nodes[1].position.x}, {e.nodes[1].position.y})")
    print(e.cost)

for k,v in g.vertices.items():
    print(f"Key: ({k.position.x}, {k.position.y})")
    print(f"Value: {v}")