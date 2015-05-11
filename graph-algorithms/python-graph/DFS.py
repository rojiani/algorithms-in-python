"""
Depth-First Search
Graph Algorithm
"""

from graph import *
from stack import ArrayStack


time = 0

def init_DFS(G):
    """Initialize values prior to performing DFS.
    Note: All vertices in graph have these values when created."""
    for v in G.getVertices():
        v.setVisitStatus(VisitStatus.UNDISCOVERED)
        v.setPredecessor(None)
        v.setTimeDiscovered(None)
        v.setTimeFinished(None)

def DFS(G):
    global time 
    time = 0
    init_DFS(G)
    for u in G.getVertices():
        if u.isUndiscovered():
            DFS_visit(G, u)

def DFS_visit(G, u):
    global time 
    time += 1
    u.setTimeDiscovered(time)
    u.markDiscovered()
    for v in G.getChildVertices(u):  # explore edge (u,v)
        if v.isUndiscovered():
            v.setPredecessor(u)
            DFS_visit(G, v)
    u.markExplored()
    time += 1
    u.setTimeFinished(time)

# def iterative_DFS(G):
#     #global time
#     t = 0
#     stack = ArrayStack()
#     init_DFS(G)
#     s = G.getVertices()[0]
#     stack.push(s)
#     while not stack.is_empty():
#         v = stack.pop()
#         if v.isUndiscovered():
#             v.markDiscovered()
#             adj_edges = G.adj


def fig_22_4_graph():
    dg = Graph(True, False)
    vertices = []
    for i in range(1, 7):
        vertices.append(Vertex(i))
    dg.addVerticesFromList(vertices)    
    dg.addEdge(1,2)
    dg.addEdge(1,4)
    dg.addEdge(2,5)
    dg.addEdge(3,5)
    dg.addEdge(3,6)
    dg.addEdge(4,2)
    dg.addEdge(5,4)
    dg.addEdge(6,6)
    return dg

def setup_graph_2():
    dg = Graph(True, False)
    vertices = []
    for i in range(1, 9):
        vertices.append(Vertex(i))
    dg.addVerticesFromList(vertices)    
    dg.addEdge(1,2)
    dg.addEdge(1,4)    
    dg.addEdge(1,5)
    dg.addEdge(2,3)
    dg.addEdge(2,4)
    dg.addEdge(3,1)
    dg.addEdge(4,3)
    dg.addEdge(5,4)
    dg.addEdge(5,6)
    dg.addEdge(7,5)
    dg.addEdge(7,6)
    dg.addEdge(7,8)
    dg.addEdge(8,5)
    return dg

def DFS_timestamps():
    dg = fig_22_4_graph()
    DFS(dg)
    for v in dg.getVertices():
        print("%s: v.d = %d, v.f = %d" % (str(v), v.getTimeDiscovered(), v.getTimeFinished()))

def DFS_timestamps_2():
    dg = setup_graph_2()
    DFS(dg)
    for v in dg.getVertices():
        print("%s: v.d = %d, v.f = %d" % (str(v), v.getTimeDiscovered(), v.getTimeFinished()))

def DFS_iterative_timestamps_2():
    dg = setup_graph_2()
    iterative_DFS(dg)
    #for v in dg.getVertices():
    #    print("%s: v.d = %d, v.f = %d" % (str(v), v.getTimeDiscovered(), v.getTimeFinished()))

# DFS_timestamps()
DFS_timestamps_2()
# DFS_iterative_timestamps_2()