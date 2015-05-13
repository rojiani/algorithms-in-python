"""
Generate graphs
"""

from graph import *

# CLRS Fig. 22.3 Graph p. 596
# Undirected, unweighted
def setup_fig_22_3_graph():
    g = Graph()
    g.addVertices(list(range(1,8+1)))
    g.addEdges([(1,2), (1,5), (2,6), (3,4), (3,6), (3,7), (4,7), (4,8), \
                (6,7), (7,8)])
    return g

def setup_fig_22_4_graph():
    dg = Graph(True, False)
    dg.addVertices(list(range(1,6+1)))
    dg.addEdges([(1,2), (1,4), (2,5), (3,5), (3,6), (4,2), (5,4), (6,6)])
    return dg

def setup_directed_graph():
    g = Graph(True,False)
    g.addVertices(list(range(7+1)))
    g.addEdges([(0,1), (0,2), (1,0), (1,2), (1,5), (1,6), (3,7), (4,7), \
                (5,3), (6,2), (6,5), (6,7), (7,6)])
    return g

def setup_graph_2():
    dg = Graph(True, False)
    dg.addVertices(list(range(1,9)))   
    dg.addEdges([(1,2), (1,4), (1,5), (2,3), (2,4), (3,1), (4,3), (5,4), (5,6), \
                 (6,4), (7,5), (7,6), (7,8), (8,4)])
    return dg

def setup_graph_2UD():
    udg = Graph(False, False)
    udg.addVertices(list(range(1,9)))   
    udg.addEdges([(1,2), (1,4), (1,5), (2,3), (2,4), (3,1), (4,3), (5,4), \
                  (5,6), (6,4), (7,5), (7,6), (7,8), (8,4)])
    return udg

def setup_simple_DAG():
    dag = Graph(True, False)
    dag.addVertices(list(range(1,4+1)))
    dag.addEdges([(1,2), (1,4), (2,3)])
    return dag

def setup_DAG_2():
    dag = Graph(True, False)
    # for i in range(1, 9+1):
    dag.addVertices(list(range(1,9+1)))
    dag.addEdges([(1,2), (1,5), (2,3), (2,5), (4,5), (6,3), (6,7), (7,8)])
    return dag

# Figure CLRS Instructor's Manual 2/E
def setup_MST_1():
    ud_w_g = Graph(False, True)
    ud_w_g.addVertices(list(range(1,9+1)))
    ud_w_g.addEdges([(1,2,10), (1,3,12), (2,3,9), (2,4,8), (3,5,3), (3,6,1), \
                     (4,7,8), (4,5,7), (4,8,5), (5,6,3), (6,8,6), (7,8,9), \
                     (7,9,2), (8,9,11)])
    return ud_w_g

# Figure 23.4, p. 631
def setup_MST_2():
    ud_w_g = Graph(False, True)
    ud_w_g.addVertices(list(range(1,9+1)))
    ud_w_g.addEdges([(1,2,4),(1,8,8),(2,3,8),(2,8,11),(3,4,7),(3,6,4),(3,9,2), \
                    (4,5,9),(4,6,14),(5,6,10),(6,7,2),(7,8,1),(7,9,6),(8,9,7)])                
    return ud_w_g

# Figure 24.4, p. 652
# Directed graph with some negative-weight edges (no neg.-wt cycles)
def setup_bellman_ford_graph():
    g = Graph(True, True)
    g.addVertices(list(range(5)))
    g.addEdges([(0,1,6), (0,3,7), (1,2,5), (1,3,8), (1,4,-4), (2,1,-2), \
                   (3,2,-3), (3,4,9), (4,0,2), (4,2,7)])
    return g

# print("Fig. 22.3 Graph:")
# print(setup_fig_22_3_graph())
# print("---------------------------------------------")
# print("Fig. 22.4 Graph:")
# print(setup_fig_22_4_graph())
# print("---------------------------------------------")
# print("Directed Graph:")
# print(setup_directed_graph())
# print("---------------------------------------------")

