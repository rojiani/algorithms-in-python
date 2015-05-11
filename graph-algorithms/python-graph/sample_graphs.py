"""
Generate graphs
"""

from graph import *

# CLRS Fig. 22.3 Graph p. 596
# Undirected, unweighted
def setup_fig_22_3_graph():
    g = Graph()
    # vertices = []
    # for i in range(1,9): # r-y
    #     vertices.append(Vertex(i))
    g.addVerticesFromList(list(range(1,8+1)))
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
    return g

def setup_fig_22_4_graph():
    dg = Graph(True, False)
    # vertices = []
    # for i in range(1, 7):
        # vertices.append(Vertex(i))
    dg.addVerticesFromList(list(range(1,6+1)))
    dg.addEdge(1,2)
    dg.addEdge(1,4)
    dg.addEdge(2,5)
    dg.addEdge(3,5)
    dg.addEdge(3,6)
    dg.addEdge(4,2)
    dg.addEdge(5,4)
    dg.addEdge(6,6)
    return dg

def setup_directed_graph():
    g = Graph(True,False)
    # vertices = []
    # for i in range(8):
    #     vertices.append(Vertex(i))
    g.addVerticesFromList(list(range(7+1)))
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
    # print(g)
    return g

def setup_graph_2():
    dg = Graph(True, False)
    # vertices = []
    # for i in range(1, 9):
    #     vertices.append(Vertex(i))
    dg.addVerticesFromList(list(range(1,9)))    
    dg.addEdge(1,2)
    dg.addEdge(1,4)    
    dg.addEdge(1,5)
    dg.addEdge(2,3)
    dg.addEdge(2,4)
    dg.addEdge(3,1)
    dg.addEdge(4,3)
    dg.addEdge(5,4)
    dg.addEdge(5,6)
    dg.addEdge(6,4)
    dg.addEdge(7,5)
    dg.addEdge(7,6)
    dg.addEdge(7,8)
    dg.addEdge(8,4)
    return dg

def setup_graph_2UD():
    udg = Graph(False, False)
    # vertices = []
    # for i in range(1, 9):
    #     vertices.append(Vertex(i))
    udg.addVerticesFromList(list(range(1,9)))    
    udg.addEdge(1,2)
    udg.addEdge(1,4)    
    udg.addEdge(1,5)
    udg.addEdge(2,3)
    udg.addEdge(2,4)
    udg.addEdge(3,1)
    udg.addEdge(4,3)
    udg.addEdge(5,4)
    udg.addEdge(5,6)
    udg.addEdge(6,4)
    udg.addEdge(7,5)
    udg.addEdge(7,6)
    udg.addEdge(7,8)
    udg.addEdge(8,4)
    return udg

def setup_simple_DAG():
    dag = Graph(True, False)
    # vertices = []
    # for i in range(1, 4+1):
    #     vertices.append(Vertex(i))
    dag.addVerticesFromList(list(range(1,4+1)))
    dag.addEdge(1,2)
    dag.addEdge(1,4)
    dag.addEdge(2,3)
    return dag

def setup_DAG_2():
    dag = Graph(True, False)
    # vertices = []
    # for i in range(1, 9+1):
    #     vertices.append(Vertex(i))
    dag.addVerticesFromList(list(range(1,9+1)))
    dag.addEdge(1,2)
    dag.addEdge(1,5)
    dag.addEdge(2,3)
    dag.addEdge(2,5)
    dag.addEdge(4,5)    
    dag.addEdge(6,3)    
    dag.addEdge(6,7)
    dag.addEdge(7,8)
    return dag