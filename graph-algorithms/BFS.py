"""
Breadth-First Search
Graph Algorithm
"""

from graph import *
from queue import LinkedQueue

def init_BFS(G):
    """Initialize values prior to performing BST.
    Note: All vertices in graph have these values when created."""
    for v in G.getVertices():
        print(str(v))
        v.setVisitStatus(VisitStatus.UNDISCOVERED)
        v.setPredecessor(None)
        v.setDistance(float('inf'))


# s = start node
def BFS(G, s):
    init_BFS(G)

    s.setVisitStatus(VisitStatus.DISCOVERED)
    s.setDistance(0)
    s.setPredecessor(None)

    Q = LinkedQueue()
    Q.enqueue(s)
    edge_strings = []
    while not Q.is_empty():
        u = Q.dequeue()
        neighbors = G.getNeighbors(u)
        for n in neighbors: print(n)
        for v in neighbors:
            if v.isUndiscovered():
                uv_edge = G.getEdge(u.getId(), v.getId())
                edge_strings.append(str(uv_edge))
                v.markDiscovered()
                v.setPredecessor(u)
                v.setDistance(u.getDistance() + 1)
                # print("Distance to %d: %d" % (v.getId(), v.getDistance()))
                Q.enqueue(v)
        u.setVisitStatus(VisitStatus.EXPLORED)
    print_BFS_edges(edge_strings)

#def print_path_from_source()

def print_BFS_edges(edge_strings):
    print("Edges:")
    for s in edge_strings:
        print(s)    

# CLRS Fig. 22.3 Graph p. 596
# Undirected, unweighted
def fig_22_3():
    g = Graph()
    vertices = []
    for i in range(1,9): # r-y
        vertices.append(Vertex(i))
    g.addVerticesFromList(vertices)
    g.addEdge(1,2)
    g.addEdge(1,5)
    g.addEdge(2,6)
    g.addEdge(3,4)
    g.addEdge(3,6)
    g.addEdge(3,7)
    g.addEdge(4,7)
    g.addEdge(4,8)
    g.addEdge(6,7)
    g.addEdge(7,8)
    print(g)
    return g

def directed_g1():
    g = Graph(True,False)
    vertices = []
    for i in range(8):
        vertices.append(Vertex(i))
    g.addVerticesFromList(vertices)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,0)
    g.addEdge(1,2)
    g.addEdge(1,5)
    g.addEdge(1,6)
    g.addEdge(3,7)
    g.addEdge(4,7)
    g.addEdge(5,3)
    g.addEdge(6,2)
    g.addEdge(6,5)
    g.addEdge(6,7)
    g.addEdge(7,6)
    print(g)
    return g

g = fig_22_3()
BFS(g, g.getVertex(2))

g1 = directed_g1()
BFS(g1, g1.getVertex(0))