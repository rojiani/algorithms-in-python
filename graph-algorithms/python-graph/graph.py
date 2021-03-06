"""
Graph ADT
@author Navid Rojiani
"""


from enum import Enum

#-----------------------------------------------------------------------------#
#   Graph                                                                     #
#-----------------------------------------------------------------------------#
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
    def addVertex(self, v_id):
        # id = vertex.getId()
        if v_id in self.vertices:
            raise ValueError('Vertex %d already in Graph' % (v_id))
        else:
            self.vertices[v_id] = Vertex(v_id)
    def addVertices(self, v_id_list):
        """Add vertices from a list of ids"""
        for v_id in v_id_list:
            self.addVertex(v_id)
    def addEdge(self, u_id, v_id, weight=1.0):
        """ Make an edge connecting u and v """

        # check that u and v are in Graph        
        if u_id not in self.vertices:
            raise ValueError('Vertex %d not in Graph' % u_id)
        elif v_id not in self.vertices:
            raise ValueError('Vertex %d not in Graph' % v_id)
        u,v = self.vertices[u_id],self.vertices[v_id]

        # check that there isn't already an edge from (u, v)
        if self.directed and self.getEdge(u_id,v_id) != None: 
            raise ValueError("Directed Edge (%d,%d) already exists" % (u_id,v_id))
        if not self.directed and (self.getEdge(u_id,v_id) != None or \
                                  self.getEdge(v_id,u_id) != None):
            raise ValueError("Undirected Edge (%d,%d) or (%d,%d) already exists" % \
                (u_id,v_id,v_id,u_id))

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
    def addEdges(self, edge_list):
        """Add edges from list of tuples containing the edges"""
        for e_tup in edge_list:
            n_args = len(e_tup)
            if n_args == 2:
                self.addEdge(e_tup[0], e_tup[1])
            elif n_args == 3:
                self.addEdge(e_tup[0], e_tup[1], e_tup[2])
            elif n_args == 4:
                self.addEdge(e_tup[0], e_tup[1], e_tup[2], e_tup[3])
            else:
                self.addEdge(e_tup[0], e_tup[1], e_tup[2], e_tup[3], e_tup[4])
    def getVertex(self, v_id):
        if v_id in self.vertices:
            return self.vertices[v_id]
        else:
            return None
    def getEdge(self, src_id, dest_id):
        edge = None
        if self.isDirected():
            for e in self.edges:
                if e.getSource().getId() == src_id and \
                        e.getDest().getId() == dest_id:
                    edge = e
        else:
            for e in self.edges:
                if (e.getSource().getId() == src_id and \
                    e.getDest().getId() == dest_id) or \
                   (e.getSource().getId() == dest_id and \
                       e.getDest().getId() == src_id):
                    edge = e
        return edge
    def getVertices(self):
        """ Returns vertices as a list """
        vertex_list = []
        indices = list(self.vertices.keys())
        for i in indices:
            vertex_list.append(self.getVertex(i))
        return sorted(vertex_list, key=id)
    def getAdjacentVertices(self, u):
        """ 
        Returns list of vertices adjacent to u.
        Undirected & directed graphs: returns list of all adjacent (whether u is src or dest)
        """
        adjV = []
        for e in self.getEdges():
            if u.getId() == e.getSource().getId():
                adjV.append(e.getDest())
            elif u.getId() == e.getDest().getId():
                adjV.append(e.getSource())
        return adjV

    def getChildVertices(self, u):
        """ 
        Returns list of vertices adjacent to u that are connected by an edge (u,v)
        Undirected graphs: returns list of all adjacent vertices
        Directed graphs: returns list of all adjacent vertices with u as the source
        """
        if self.directed:
            dests = []
            for e in self.getEdges():
                if u.getId() == e.getSource().getId():
                    dests.append(e.getDest())
            return dests
        else:
            return self.getAdjacentVertices(u)

    def getAdjacentEdges(self, u):
        """ 
        Returns list of edges adjacent to v. 
        Undirected & directed graphs: returns list of all adjacent (whether u is src or dest)
        """
        adjE = []
        for e in self.getEdges():
            if u.getId() == e.getSource().getId():
                adjE.append(e)
            elif u.getId() == e.getDest().getId():
                adjE.append(e)
        return adjE
    def getOutgoingEdges(self, u):
        if self.directed:
            outE = []
            for e in self.getEdges():
                if u.getId() == e.getSource().getId():
                    outE.append(e)
            return outE
        else:
            return self.getAdjacentEdges(u)


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
        s += '================ Vertices (%d) ================\n' % self.getVertexCount()
        for v in self.vertices:
            s += '\t' + str(v) + '\n'
        s += '================= Edges (%d) ==================\n' % self.getEdgeCount()
        for e in self.edges:
            s += '\t' + str(e) + '\n'
        return s


#-----------------------------------------------------------------------------#
#   Vertex                                                                    #
#-----------------------------------------------------------------------------#
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
        self.path_length = float('inf')
        self.path_cost = float('inf')
        self.predecessor = None
        self.timeDiscovered = None
        self.timeFinished = None
    def getId(self):
        """ Identifying number - must be positive integer """
        return self.id
    def addConnection(self, edge):
        self.connections[edge.getOppositeVertex(self).getId()] = edge.getWeight()
    def getConnectedIds(self):
        """ 
        Returns list of the IDs of vertices adjacent to v. 
        Undirected graphs: returns list of all adjacent (whether v is src or dest)
        Directed graphs: returns list of all nodes with v as the source
        """
        return list(self.connections.keys())

    # Visitation
    def getVisitStatus(self):
        return self.visitStatus
    def setVisitStatus(self, status):
        self.visitStatus = status
    def isUndiscovered(self):
        return self.visitStatus == VisitStatus.UNDISCOVERED
    def isDiscovered(self):
        return self.visitStatus == VisitStatus.DISCOVERED
    def isExplored(self):
        return self.visitStatus == VisitStatus.EXPLORED
    def markDiscovered(self):
        self.visitStatus = VisitStatus.DISCOVERED
    def markExplored(self):
        self.visitStatus = VisitStatus.EXPLORED

    """ Path length used to refer to number of edges, used in BFS """
    def getPathLength(self):
        return self.path_length
    def setPathLength(self, path_len):
        self.path_length = path_len
    
    """Path cost = sum of weights of edges on path, aka path distance """
    def setPathCost(self, path_cost):
        self.path_cost = path_cost
    def getPathCost(self):
        return self.path_cost

    """Predecessor - used for BFS and other algorithms"""
    def setPredecessor(self, predecessor):
        self.predecessor = predecessor
    def getPredecessor(self):
        return self.predecessor
    def hasPredecessor(self):
        return self.predecessor != None

    """Time Discovered & Time Finished - used for DFS"""
    def getTimeDiscovered(self):
        return self.timeDiscovered
    def setTimeDiscovered(self, time):
        self.timeDiscovered = time
    def getTimeFinished(self):
        return self.timeFinished
    def setTimeFinished(self, time):
        self.timeFinished = time

    def hasLoop(self):
        return self.getId() in self.connections

    def connectionsString(self):
        """Return a string representation of all connections"""
        s = 'V<' + str(self.id) + '> Connections: {\n'
        for i in list(self.connections.keys()):
            s += '\t' + str(i) + ': ' + str(self.connections[i]) + '\n'
        s += '}'
        return s

    def __str__(self):
        return 'V<%d>' % self.id

class VisitStatus(Enum):
    # As defined in CLRS
    UNDISCOVERED  = 'White'
    DISCOVERED    = 'Gray'          # Frontier, not all neighbors discovered
    EXPLORED      = 'Black'         # All neighbors discovered


#-----------------------------------------------------------------------------#
#   Edge                                                                      #
#-----------------------------------------------------------------------------#
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