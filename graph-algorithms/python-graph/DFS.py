"""
Depth-First Search
Graph Algorithm
"""

from graph import *
from datastructures.stack import ArrayStack
from sample_graphs import *

time = 0
tree = []
back = []
# fwd = []
# cross = []
fwd_or_cross = []

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


""" a directed graph G is acylic <===> DFS(G) yields no back edges """
def is_acyclic(G):
    if not G.isDirected():
        raise Exception("must be a directed graph")
    global time 
    global tree
    global back
    global fwd_or_cross
    time = 0
    tree = []
    back = []
    fwd_or_cross = []
    init_DFS(G)
    for u in G.getVertices():
        if u.isUndiscovered():
            DFS_edges_visit(G, u)
    return len(back) == 0

def is_DAG(G):
    return is_acyclic(G)

""" Topological Sort """
def topo_sort(G):
    if not is_DAG(G):
        print('x')
        raise Exception("G must be a directed acyclic graph")
    DFS(G)
    vertices = G.getVertices()
    return sorted(vertices, key=lambda x: x.getTimeFinished(), reverse=True)


# Categorize the edges
def DFS_edges(G):
    global time 
    global tree
    global back
    global fwd_or_cross
    time = 0
    tree = []
    back = []
    fwd_or_cross = []
    init_DFS(G)
    for u in G.getVertices():
        if u.isUndiscovered():
            DFS_edges_visit(G, u)
    print("Tree Edges:")
    for e in tree:
        print(e)
    print("Back Edges:")
    for e in back:
        print(e)
    print("Other Edges:")
    for e in fwd_or_cross:
        print(e)
    print()

def DFS_edges_visit(G, u):
    global time 
    global tree 
    global back 
    global fwd_or_cross
    # global fwd 
    # global cross 
    time += 1
    u.setTimeDiscovered(time)
    u.markDiscovered()
    for v in G.getChildVertices(u):  # explore edge (u,v)
        edge_uv = G.getEdge(u.getId(), v.getId())
        if v.isDiscovered() and not edge_categorized(G,u,v):
            back.append(edge_uv)
        elif v.isExplored() and not edge_categorized(G,u,v):
            fwd_or_cross.append(edge_uv)
        else: # v.isUndiscovered():
            if not edge_categorized(G,u,v):
                tree.append(edge_uv)
                v.setPredecessor(u)
                DFS_edges_visit(G, v)
    u.markExplored()
    time += 1
    u.setTimeFinished(time)

def edge_categorized(G, u, v):
    # check if reverse edge categorized for undirected
    if G.isDirected():
        return False
    else:
        edge_vu = G.getEdge(v.getId(), u.getId())
        categorized = False
        if edge_vu in tree: categorized = True
        if edge_vu in back: categorized = True
        if edge_vu in fwd_or_cross: categorized = True
        return categorized


def DFS_timestamps():
    dg = setup_fig_22_4_graph()
    DFS(dg)
    for v in dg.getVertices():
        print("%s: v.d = %d, v.f = %d" % (str(v), v.getTimeDiscovered(), v.getTimeFinished()))

def DFS_timestamps_2():
    dg = setup_graph_2()
    DFS(dg)
    for v in dg.getVertices():
        print("%s: v.d = %d, v.f = %d" % (str(v), v.getTimeDiscovered(), v.getTimeFinished()))

def DFS_timestamps_edges():
    dg = setup_fig_22_4_graph()
    DFS_edges(dg)
    for v in dg.getVertices():
        print("%s: v.d = %d, v.f = %d" % (str(v), v.getTimeDiscovered(), v.getTimeFinished()))

def DFS_timestamps_edges_2():
    dg = setup_graph_2()
    DFS_edges(dg)
    for v in dg.getVertices():
        print("%s: v.d = %d, v.f = %d" % (str(v), v.getTimeDiscovered(), v.getTimeFinished()))

def DFS_timestamps_edges_2UD():
    dg = setup_graph_2UD()
    DFS_edges(dg)
    for v in dg.getVertices():
        print("%s: v.d = %d, v.f = %d" % (str(v), v.getTimeDiscovered(), v.getTimeFinished()))



# def e_in_x(G,u,v, x):
#     if G.isDirected():
#         return False
#     else:
#         edge_vu = G.getEdge(v.getId(), u.getId())
#         categorized = False
#         if edge_vu in x: categorized = True
#         return categorized

# def DFS_iterative_timestamps_2():
#     dg = setup_graph_2()
#     iterative_DFS(dg)
#     for v in dg.getVertices():
#        print("%s: v.d = %d, v.f = %d" % (str(v), v.getTimeDiscovered(), v.getTimeFinished()))

# DFS_timestamps()
# DFS_timestamps_2()
# print()
# DFS_timestamps_edges()
DFS_timestamps_edges_2()
# DFS_iterative_timestamps_2()
# g = setup_graph_2UD()
# # for e in g.getEdges():
# #     print(e)
# v1 = g.getVertex(1)
# for v in g.getChildVertices(v1):
#     print(v)
# print()
# v2 = g.getVertex(2)
# for v in g.getChildVertices(v2):
#     print(v)

# edge_uv12 = g.getEdge(1,2)
# edge_vu21 = g.getEdge(2,1)
# v3 = g.getVertex(3)

# x = []
# x.append(edge_uv12)
# print(e_in_x(g, v1, v3, x))

# DFS_timestamps_edges_2UD()

# TEST is_acyclic
# g1 = setup_fig_22_4_graph()
# g2 = setup_directed_graph()
# g3 = setup_graph_2()
# g4 = setup_simple_DAG()
# # print(is_acyclic(g2))
# # print(is_acyclic(g3))
# print(is_acyclic(g4))

# TOPO SORT
print("Topological Sort")
# tsorted = topo_sort(g4)
# for v in tsorted:
#     print(v)
g5 = setup_DAG_2()
print(is_acyclic(g5))
tsorted = topo_sort(g5)
for v in tsorted:
    print(v, end=',')    