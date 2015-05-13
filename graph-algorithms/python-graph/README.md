Python Graph Data Structures & Algorithms  
=========================================  


# TODO


VERTEX:
instead of having Vertex have edgeLength, pathCost, predecessor, etc. methods,
might be cleaner to track those using lists in the actual algorithms.


GRAPH:
    graph contain element, not just an id
    remove edge, remove V
    connectedComponent(self, v) [aka connectedSubgraph, use BFS/DFS]
    refactor Graph, Digraph subclass
    addVerticesFromList
    hasCycle
    hamiltonian
    connected
    complete
    hasEulerianPath
    def getNumberOutgoingEdges(self, v):

