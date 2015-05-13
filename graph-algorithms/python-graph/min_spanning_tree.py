"""
Kruskal and Prim's Minimum Spanning Tree Algorithms
Graph Algorithms

Based on the algorithms in CLRS Ch. 23 and 
Data Structures and Algorithms in Python - Goodrich, Tamassia, Goldwasser
"""

from graph import *
from sample_graphs import *
from datastructures.disjoint_set import Partition
from datastructures.priority_queue import *


#-----------------------------------------------------------------------------#
#   Kruskal's Algorithm                                                       #
#-----------------------------------------------------------------------------#

def MST_Kruskal(G):  
    verify_graph(G)             # Verify graph is weighted and undirected

    tree = []                   # list of edges in spanning tree

    forest = Partition()            # Union/Find data structure
    forest_posn = {}            # Maps each vertex to its Partition entry

    for v in G.getVertices():   # make each vertex a set in the partition
        forest_posn[v] = forest.make_set(v) 

    # Sort edges by weight, lowest to greatest
    edges = sorted(G.getEdges(), key=lambda e: e.getWeight())

    # num_V = G.getVertexCount()
    for e in edges:
        # if len(tree) == (num_V - 1):
        #    break
        # Above shouldn't be necessary since find comparison fails once
        # spanning tree is formed
        u,v = e.getEndpoints()
        a = forest.find_set(forest_posn[u])
        b = forest.find_set(forest_posn[v])
        if a != b:
            tree.append(e)
            forest.union(a, b)

    return tree

def demo_Kruskal():
    G = setup_MST_1()
    mst = MST_Kruskal(G)
    print("MST:")
    for edge in mst:    
        print(edge)
    print("|V|: %d" % G.getVertexCount())
    print("|E|: %d" % G.getEdgeCount())
    print("Number of Edges in MST: %d" % len(mst))
    print("Number of Edges should be %d" % (G.getVertexCount() - 1))
    weight = sum_weights(mst)
    print("Weight of MST: %d" % weight)
    print("Weight should be %d" % 43)

    G = setup_MST_2()
    mst = MST_Kruskal(G)
    print("MST:")
    for edge in mst:    
        print(edge)
    print("|V|: %d" % G.getVertexCount())
    print("|E|: %d" % G.getEdgeCount())
    print("Number of Edges in MST: %d" % len(mst))
    print("Number of Edges should be %d" % (G.getVertexCount() - 1))
    weight = sum_weights(mst)
    print("Weight of MST: %d" % weight)
    print("Weight should be %d" % 37)


def sum_weights(edge_list):
    w = 0
    for e in edge_list: w += e.getWeight()
    return w

# Graph must be undirected and weighted
def verify_graph(G):
    if G.isDirected() or not G.isWeighted():
        raise Exception("MST Algorithms require an undirected, weighted graph")

demo_Kruskal()

#-----------------------------------------------------------------------------#
#   Prim's Algorithm                                                          #
#-----------------------------------------------------------------------------#
""" Incomplete """
# root - an arbitrary vertex in G
# def MST_Prim(G, root=None):
#     verify_graph(G)             # Verify graph is weighted and undirected
#     V = G.getVertices()
#     if root == None:
#         root = V[0]             # Choose arbitrary vertex as root
    
#     # Add all V to Priority Queue, and set predecessors to None
#     Q = HeapPriorityQueue()
#     for u in V:
#         u.setPredecessor(None)
#         if u == root: 
#             Q.add(0, root)
#         else:
#             Q.add(float('inf', u))

#     V_a = []    # set of vertices not in Q (Priority Queue not searchable?)

#     while not Q.is_empty():
#         u_min, u = Q.remove_min()
#         V_a.append(u)
#         for v in G.getAdjacentVertices(u):
#             if v not in V_a and G.getEdge(u.getId(), v.getId()).getWeight() < 



