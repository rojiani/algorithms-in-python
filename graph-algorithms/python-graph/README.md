Python Graph Data Structures & Algorithms  
=========================================  


# TODO

VERTEX:


    def setPredecessor(self, predecessor):
        self.predecessor = predecessor
    def getPredecessor(self):
        return self.predecessor
    def hasPredecessor(self):
        return self.predecessor != None

    Path Cost or Distance to this vertex
    def setPathCost(self, cost):
        self.pathCost = cost
    def getPathCost(self):
        return self.pathCost

GRAPH:
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

