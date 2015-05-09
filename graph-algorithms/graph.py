class Vertex(object):
    def __init__(self, n):
        self.n = n
        self.connections = {}
        """ if connected to 3 with weight 5, and 7 with weight 2:
        {
            3: 5,
            7: 2
        }
        """
        self.visited = False
        self.predecessor = None
        self.pathCost = 0.0
    def n(self):
        return self.n
    def addNeighbor(self, edge):
        if dest in self.adj:
            raise ValueError('Duplicate Vertex')
        else:
            self.connections[edge.getDest()] = edge.getWeight()

    def getAdjacent(self):
        return sorted(list(self.connections.keys()))
    def hasAdjacent(self):
        return len(self.connections) > 0

    """ Marking Visitation """
    def visit(self):
        self.visited = True
    def unvisit(self):
        self.visited = False
    def isVisited(self):
        return self.visited

    """ Marking Predecessors """
    # def setPredecessor(self, predecessor):
    #     self.predecessor = predecessor
    # def getPredecessor(self):
    #     return self.predecessor
    # def hasPredecessor(self):
    #     return self.predecessor != None

    """ Marking Path Cost """
    def setPathCost(self, cost):
        self.pathCost = cost
    def getPathCost(self):
        return self.pathCost

    def neighborsString(self):
        s = 'V<' + self.n + '> Neighbors: [ '
        for adj in connections:
            s += str(adj) + ' '
        s += ']'
        return s
    def connectionsString(self):
        s = 'V<' + self.n + '> Connections: [ '
        for adj in list(connections.keys()):
            s += str(adj) + ' '
        s += ']'
        return s
    def __str__(self):
        return 'V<%d>' % self.n



class Edge(object):
    def __init__(self, src, dest, weight = 1.0, directed = False):
        """Assumes src and dest are vertices"""
        self.src = src
        self.dest = dest
        self.weight = weight
        self.directed = directed
    def getSource(self):
        return self.src
    def getDest(self):
        return self.dest
    def getWeight(self):
        return self.weight
    def isDirected(self):
        return self.directed
    def __str__(self):
        return '(%d, %d, [%.2f])' % (self.src.n(), self.dest.n(), self.weight)


class Graph(object):
    def __init__(self):
        self.adjLists = {} # key:V<num>, value: V<num>.adjList
        """ 
        Adjacency List of an undirected Graph:
            { 
                0: [1, 2],
                1: [0],
                2: [0, 3],
                3: [2]
            }
        """
    def addVertex(self, number):
        if number in adjLists:
            raise ValueError('Vertex %d already in Graph' % (number))
        else:
            adjLists[number] = []
    def addEdge(self, edge):
        u = edge.getSource()
        v = edge.getDest()
        if vertices[u] == None:
            raise ValueError('Vertex %d not in Graph' % u)
        elif vertices[v] == None:
            raise ValueError('Vertex %d not in Graph' % v)
        else:
            if directed:
                self.adjLists[u].append(v)
            else:
                self.adjLists[u].append(v)
                self.adjLists[v].append(u)
    def numVertices(self):
        return len(adjLists)
    

