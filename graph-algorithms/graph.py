#
# Graph ADT
# @author Navid Rojiani
#


from enum import Enum

class Graph(object):
    def __init__(self, directed=False, weighted=False):
        """
        Vertices dictionary (each vertex stores its connections)
        Key: Vertex id number (n)
        Value: Vertex
            {
                0: <V_0>
                2: <V_2>
                3: <V_3>
            }
        """
        self.vertices = {}
        """ Simple List containing Edges """
        self.edges = []

        self.directed = directed
        self.weighted = weighted
    def addVertex(self, vertex):
        id = vertex.getId()
        if id in self.vertices:
            raise ValueError('Vertex %d already in Graph' % (id))
        else:
            self.vertices[id] = vertex
    def addVerticesFromList(self, vertices):
        for v in vertices:
            self.addVertex(v)
    def addEdge(self, u_id, v_id, weight=1.0):
        """ Make an edge connecting u and v """
        if u_id not in self.vertices:
            raise ValueError('Vertex %d not in Graph' % u)
        elif v_id not in self.vertices:
            raise ValueError('Vertex %d not in Graph' % v)
        u,v = self.vertices[u_id],self.vertices[v_id]

        if self.weighted and self.directed:
            edge = Edge(u, v, weight, True, True)
        elif self.weighted and not self.directed:
            edge = Edge(u, v, weight, True, False)
        elif not self.weighted and self.directed:
            edge = Edge(u, v, 1.0, False, True)
        else:
            edge = Edge(u, v)
        self.edges.append(edge)             # Add to Graph's edges list
        if self.directed:                   # Add to u.connections
            u.addConnection(edge)
        else:                               # Add to u.connections & v.connections
            u.addConnection(edge)
            v.addConnection(edge)
    def getVertex(self, v_id):
        if v_id in self.vertices:
            return self.vertices[v_id]
        else:
            return None
    def getEdge(self, src_id, dest_id):
        edge = None
        for e in self.edges:
            if e.getSource().getId() == src_id and \
               e.getDest().getId() == dest_id:
                edge = e
        return edge
    def getVertices(self):
        return self.vertices
    def getEdges(self):
        return self.edges
    def getVertexCount(self):
        return len(self.vertices)
    def getEdgeCount(self):
        return len(self.edges)
    def isDirected(self):
        return self.directed
    def isWeighted(self):
        return self.weighted
    def getDegree(self, v):
        """ Get the number of edges incident to v """
        degree = 0
        for e in self.edges:
            if v == e.getSource() or v == e.getDest(): degree += 1
        return degree
    def isIsolated(self, v):
        return self.getDegree(v) == 0
    def __str__(self):
        s = 'GRAPH:\n'
        s += '%s\n' % 'Weighted' if self.weighted else 'Unweighted\n'
        s += '%s\n' % 'Directed' if self.directed else 'Undirected\n'
        s += '===== Vertices (%d) =====\n' % self.getVertexCount()
        for v in self.vertices:
            s += '\t' + str(v) + '\n'
        s += '===== Edges (%d) =====\n' % self.getEdgeCount()
        for e in self.edges:
            s += '\t' + str(e) + '\n'
        return s



#----------------------------------------------------------------------------#

class Vertex(object):
    def __init__(self, id):
        self.id = int(id)          # positive integer ID
        """ Dictionary storing details of all edges incident to this vertex.
        Key: id # of opposite vertex
        Value: weight of edge
        {
            3: 5.0,
            7: 2.0
        }
        - In unweighted graphs, all edges represented as having a weight of 1.0
        - In undirected graphs, only 1 edge is stored in the Graph class for an
            undirected edge (u,v), but both u and v will have the opposite
            vertex as an entry in their connections dictionary:
                u.connections => { ... v: 1.0, ... } and
                v.connections => { ... u: 1.0, ... }.
            For a directed graph, the edge will only be included in the source
            vertex's connections dictionary.
        """
        self.connections = {}
        self.visitStatus = VisitStatus.UNDISCOVERED
    def getId(self):
        """ Identifying number - must be positive integer """
        return self.id
    def addConnection(self, edge):
        self.connections[edge.getOppositeVertex(self).getId()] = edge.getWeight()
    # Visitation
    def getVisitStatus(self):
        return self.visitStatus
    def setVisitStatus(self, status):
        self.visitStatus = status
    def isUnvisited(self):
        return self.visitStatus == VisitStatus.UNDISCOVERED
    def connectionsString(self):
        s = 'V<' + str(self.id) + '> Connections: [ '
        for adj in self.connections:
            s += str(adj) + ' '
        s += ']'
        return s
    def outgoingEdgesString(self):
        """ Return a string representation of all outgoing edges """
        s = 'V<' + self.id + '> Connections: [ '
        for i in range(list(self.connections.keys())):
            s += str(self.connections.keys()[i])
            s += ' <W = %.2f>,' % self.connections[i]
        s = s[:-1] + ' ]'
        return s
    def __str__(self):
        return 'V<%d>' % self.id

class VisitStatus(Enum):
    # As defined in CLRS
    UNDISCOVERED  = 'White'
    DISCOVERED    = 'Gray'          # Frontier, not all neighbors discovered
    EXPLORED      = 'Black'         # All neighbors discovered


#----------------------------------------------------------------------------#
class Edge(object):
    def __init__(self, src, dest, weight= 1.0, weighted=False, directed=False):
        """Assumes src and dest are vertices"""
        self.src = src
        self.dest = dest
        self.directed = True if directed else False
        self.weighted = True if weighted else False
        if not weight:
            self.weight = 1.0
        else:
            self.weight = weight        # 1.0 if unweighted
    def getSource(self):
        return self.src
    def getDest(self):
        return self.dest
    def getWeight(self):
        return self.weight
    def isDirected(self):
        return self.directed
    def isWeighted(self):
        return self.weighted
    def getEndpoints(self):
        """Return (u,v) tuple for vertices u and v."""
        return (self.src, self.dest)
    def getOppositeVertex(self, v):
        """Return the vertex that is opposite v on this edge."""
        if not isinstance(v, Vertex):
            raise TypeError('v must be an instance of class Vertex')
        return self.dest if v is self.src else self.src
    def __str__(self):
        if self.isDirected() and self.isWeighted():
            return '( %d ==[%.2f]==> %d )' % (self.src.getId(),self.getWeight(), self.dest.getId())
        elif self.isDirected() and not self.isWeighted():
            return '( %d ====> %d )' % (self.src.getId(), self.dest.getId())
        elif not self.isDirected() and self.isWeighted():
            return '( %d <==[%.2f]==> %d )' % (self.src.getId(),self.getWeight(), self.dest.getId())
        else:
            return '( %d <====> %d )' % (self.src.getId(), self.dest.getId())
