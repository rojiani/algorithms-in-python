"""
Graph Algorithms for the single-source shortest paths problem
Based on CLRS Ch. 23
"""

from sample_graphs import *

# s = start node
def init_single_source(G, s):
    for v in G.getVertices():
        v.setPathCost(float('inf'))
        v.setPredecessor(None)
    s.setPathCost(0)

# Relax an edge cost (distance)
# return: True if the edge was relaxed
def relax(edge):
    u,v = edge.getEndpoints()
    if v.getPathCost() > u.getPathCost() + edge.getWeight():
        v.setPathCost(u.getPathCost() + edge.getWeight())
        v.setPredecessor(u)
        return True

#-----------------------------------------------------------------------------#
#   Bellman-Ford                                                              #
#-----------------------------------------------------------------------------#

# returns False if a negative-weight cycle exists
# negative-weight edges are ok though
def bellman_ford(G, s):
    init_single_source(G, s)

    # relax the edge set |V|-1 times
    for i in range(G.getVertexCount() - 1):
        for edge in G.getEdges():
            relax(edge)
    
    # check for negative-weight cycles
    for edge in G.getEdges():
        u,v = edge.getEndpoints()
        if v.getPathCost() > u.getPathCost() + edge.getWeight():
            return False
    return True

# Assumes Bellman-Ford has been called on G
def print_shortest_path(G, s, t):
    dist = t.getPathCost()
    path = []    # shortest-path tree vertices
    v = t
    while v != None:
        path.insert(0, v)
        v = v.getPredecessor()
    print("Shortest path from %s to %s [Distance (Cost) = %s: " % (str(s), str(t), dist))
    for v in path: print(v)

def demo_bellman_ford():
    g = setup_bellman_ford_graph()
    s = g.getVertex(0)
    bellman_ford(g, s)
    for v in g.getVertices():
        print_shortest_path(g, s, v)

demo_bellman_ford()

#-----------------------------------------------------------------------------#
#   Dijkstra                                                                  #
#-----------------------------------------------------------------------------#

# Edge weights must be nonnegative.

# TODO