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


class Node:
    def __init__ (self, val):
        self.data = val
        self.connections = []
        
    def add_connection (self, v):
        if v not in self.connections:
            self.connections.append (v)
            self.neighbours.sort ()