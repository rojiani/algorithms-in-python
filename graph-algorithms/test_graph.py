import unittest
from graph import *

class TestGraph(unittest.TestCase):
    """Tests for 'graph.py'."""

    def setUp(self):
        # Undirected, Unweighted
        self.g1 = Graph()
        self.g1.addVertex(Vertex(1))
        self.g1.addVertex(Vertex(2))
        self.g1.addVertex(Vertex(3))
        self.g1.addVertex(Vertex(4))
        self.g1.addVertex(Vertex(5))
        self.g1.addEdge(1,2)
        self.g1.addEdge(1,5)
        self.g1.addEdge(2,3)
        self.g1.addEdge(2,4)
        self.g1.addEdge(2,5)
        self.g1.addEdge(3,4)

        self.ud_uw_edge = self.g1.getEdge(1,2) 

        # Undirected, Weighted Graph
        self.g2 = Graph(False, True)
        self.g2.addVertex(Vertex(1))
        self.g2.addVertex(Vertex(2))
        self.g2.addVertex(Vertex(3))
        self.g2.addVertex(Vertex(4))
        self.g2.addVertex(Vertex(5))
        self.g2.addEdge(1,2,20)
        self.g2.addEdge(1,5,21)
        self.g2.addEdge(2,3,22)
        self.g2.addEdge(2,4,23)
        self.g2.addEdge(2,5,24)
        self.g2.addEdge(3,4,25)

        self.ud_w_edge = self.g2.getEdge(1,2) 

        # Directed, Unweighted Graph
        self.g3 = Graph(True, False)
        self.g3.addVertex(Vertex(1))
        self.g3.addVertex(Vertex(2))
        self.g3.addVertex(Vertex(3))
        self.g3.addVertex(Vertex(4))
        self.g3.addVertex(Vertex(5))
        self.g3.addEdge(1,2)
        self.g3.addEdge(2,3)
        self.g3.addEdge(2,4)
        self.g3.addEdge(2,5)
        self.g3.addEdge(3,4)        
        self.g3.addEdge(4,2)        
        self.g3.addEdge(5,1)
        self.g3.addEdge(5,2)      

        self.d_uw_edge = self.g3.getEdge(1,2)

        # Directed, Weighted Graph
        self.g4 = Graph(True, True)
        self.g4.addVertex(Vertex(1))
        self.g4.addVertex(Vertex(2))
        self.g4.addVertex(Vertex(3))
        self.g4.addVertex(Vertex(4))
        self.g4.addVertex(Vertex(5))
        self.g4.addEdge(1,2,10)
        self.g4.addEdge(2,3,11)
        self.g4.addEdge(2,4,12)
        self.g4.addEdge(2,5,13)
        self.g4.addEdge(3,4,14)        
        self.g4.addEdge(4,2,15)        
        self.g4.addEdge(5,1,16)
        self.g4.addEdge(5,2,17)        

        self.d_w_edge = self.g4.getEdge(1,2)

    def tearDown(self):
        pass
        # self.g1 = None
        # self.g2 = None
        # self.g3 = None
        # self.g4 = None

        # self.ud_uw_edge = None
        # self.ud_w_edge = None
        # self.d_uw_edge = None
        # self.d_w_edge = None

    def testIsDirected(self):
        self.assertFalse(self.g1.isDirected())
        self.assertFalse(self.g2.isDirected())
        self.assertTrue(self.g3.isDirected())
        self.assertTrue(self.g4.isDirected())
    
    def testIsWeighted(self):
        self.assertFalse(self.g1.isWeighted())
        self.assertTrue(self.g2.isWeighted())
        self.assertFalse(self.g3.isWeighted())        
        self.assertTrue(self.g4.isWeighted())        

    def testGetEdgeCount(self):
        self.assertEqual(self.g1.getEdgeCount(), 6)
        self.assertEqual(self.g2.getEdgeCount(), 6)
        self.assertEqual(self.g3.getEdgeCount(), 8)
        self.assertEqual(self.g4.getEdgeCount(), 8)

    def testGetVertexCount(self):
        self.assertEqual(self.g1.getVertexCount(), 5)
        self.assertEqual(self.g2.getVertexCount(), 5)
        self.assertEqual(self.g3.getVertexCount(), 5)
        self.assertEqual(self.g4.getVertexCount(), 5)

    def testEdge(self):
        # also tests G.addEdge(), G.getEdge()
        self.assertFalse(self.ud_uw_edge.isWeighted())
        self.assertFalse(self.ud_uw_edge.isDirected())

        self.assertTrue(self.ud_w_edge.isWeighted())
        self.assertFalse(self.ud_w_edge.isDirected())

        self.assertFalse(self.d_uw_edge.isWeighted())
        self.assertTrue(self.d_uw_edge.isDirected())

        self.assertTrue(self.d_w_edge.isWeighted())
        self.assertTrue(self.d_w_edge.isDirected())

    def testVertex(self):
        v1 = self.g1.getVertex(1)
        print(v1)
        print(v1.connectionsString())
        v2 = self.g1.getVertex(2)
        print(v2.connectionsString())

        v4 = self.g4.getVertex(2)
        print(v4.connectionsString())
        v5 = self.g4.getVertex(3)
        print(v5.connectionsString())        

        self.assertTrue(v1.isUndiscovered())
        self.assertEqual(v1.getVisitStatus(), VisitStatus.UNDISCOVERED)
        v1.setVisitStatus(VisitStatus.DISCOVERED)
        self.assertEqual(v1.getVisitStatus(), VisitStatus.DISCOVERED)
        self.assertEqual(self.g1.getDegree(v1), 2)

        self.assertEqual(self.g4.getDegree(v4), 6)

        self.g1.addVertex(Vertex(9))
        v9 = self.g1.getVertex(9)
        self.assertTrue(self.g1.isIsolated(v9))

        print(self.g1)

    # def testGraphSetup(self):
        # print(self.g1)
        # print(self.g2)
        # print(self.g3)
        # print(self.g4)

        # g5 = Graph()
        # vertices = []
        # for i in range(11):
        #     vertices.append(Vertex(i))
        # g5.addVerticesFromList(vertices)
        # print(g5)

if __name__=='__main__':
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True: # raised by sys.exit(True) when tests failed
            raise