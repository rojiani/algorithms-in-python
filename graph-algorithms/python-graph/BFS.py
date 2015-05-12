"""
Breadth-First Search
Graph Algorithm
"""

from graph import *
from datastructures.queue import LinkedQueue
from sample_graphs import *


def init_BFS(G):
    """Initialize values prior to performing BFS.
    Note: All vertices in graph have these values when created."""
    for v in G.getVertices():
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
    while not Q.is_empty():
        u = Q.dequeue()
        for v in G.getChildVertices(u):
            if v.isUndiscovered():
                v.markDiscovered()
                v.setPredecessor(u)
                v.setDistance(u.getDistance() + 1)
                Q.enqueue(v)
        u.markExplored()

def BFS_print_edges_and_distance(G, s):
    init_BFS(G)

    s.setVisitStatus(VisitStatus.DISCOVERED)
    s.setDistance(0)
    s.setPredecessor(None)

    Q = LinkedQueue()
    Q.enqueue(s)
    edge_strings = []
    while not Q.is_empty():
        u = Q.dequeue()
        neighbors = G.getChildVertices(u)
        for v in neighbors:
            if v.isUndiscovered():
                uv_edge = G.getEdge(u.getId(), v.getId())
                edge_strings.append(str(uv_edge))
                v.markDiscovered()
                v.setPredecessor(u)
                v.setDistance(u.getDistance() + 1)
                print("Distance to %s: %d" % (str(v), v.getDistance()))
                Q.enqueue(v)
        u.setVisitStatus(VisitStatus.EXPLORED)
    print_BFS_edges(edge_strings)

# Prints a breadth-first tree from s to v. 
# Assumes that BFS already run on G, with s as the source.
# See CLRS p. 601
def print_path(G,s,v):
    print("Path from %s to %s:" % (str(s), str(v)))
    print_path_rec(G,s,v)

def print_path_rec(G,s,v):
    if v == s:
        print(s)
    elif v.getPredecessor() == None:
        print("No path from %s to %s exists" % (str(s), str(v)))
    else:
        print_path_rec(G, s, v.getPredecessor())
        print(v)

def print_BFS_edges(edge_strings):
    print("Edges traversed during BFS:")
    for s in edge_strings:
        print(s)    

# Demo
def bfs_undirected():
    ug = setup_fig_22_3_graph()
    print("Undirected graph g:")
    print(ug)
    print("Running BFS(ug,2):")
    # BFS(ug, ug.getVertex(2))
    BFS_print_edges_and_distance(ug, ug.getVertex(2))

def bfs_undirected_path():
    ug = setup_fig_22_3_graph()
    print("Undirected graph g:")
    print(ug)
    s = ug.getVertex(2)
    BFS(ug, s)
    for v_id in range(1,9):
        v = ug.getVertex(v_id)
        print_path(ug, s, v)
        print("")
    s,v = ug.getVertex(1), ug.getVertex(2)
    BFS(ug, s)
    print_path(ug, s, v)

    s,v = ug.getVertex(5), ug.getVertex(4)
    BFS(ug, s)    
    print_path(ug, s, v)


def bfs_directed():
    dg = setup_directed_graph()
    print("Directed graph dg:")
    print(dg)
    print("Running BFS(dg, 0):")
    #BFS(dg, dg.getVertex(0))
    BFS_print_edges_and_distance(dg, dg.getVertex(0))

def bfs_directed_path():
    dg = setup_directed_graph()
    print("Directed graph dg:")
    # print(dg)
    s = dg.getVertex(0)
    BFS(dg, s)
    for v_id in range(1,8):
        v = dg.getVertex(v_id)
        print_path(dg, s, v)
        print("")
    s,v = dg.getVertex(1), dg.getVertex(2)
    BFS(dg, s)
    print_path(dg, s, v)

    s,v = dg.getVertex(5), dg.getVertex(4)
    BFS(dg, s)    
    print_path(dg, s, v)

# bfs_undirected()
# bfs_undirected_path()
# bfs_directed()
bfs_directed_path()