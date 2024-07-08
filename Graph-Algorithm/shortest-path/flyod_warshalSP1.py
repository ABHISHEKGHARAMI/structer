# setting up the logger
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()


# class for graph for the shortest path
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.v = len(self.vertices)
        self.index_map = { vertex : idx for idx,vertex in enumerate(self.vertices)}
        self.graph = [[float('inf')]*self.v for _ in range(self.v)]
        
        
        # making the weight zero for self loop
        
        for i in range(self.v):
            self.graph[i][i] = 0
            
            
    # adding the edges for the graph
    def addEdge(self,u,v,w):
        if u in self.vertices and v in self.vertices:
            u_idx = self.index_map[u]
            v_idx = self.index_map[v]
            self.graph[u_idx][v_idx] = w
            
        else:
            print(f"{u} and {v} no longer in the vertex.")
            logging.info(f"{u} and {v} no longer in the vertex.")
            
    
    # print the graph

    def printSolution(self, dist):
        print(
            "Following matrix shows the shortest distances between every pair of vertices")
        for i in range(self.v):
            for j in range(self.v):
                if dist[i][j] == float('inf'):
                    print("INF", end=" ")
                else:
                    print(f"{dist[i][j]:7}", end=" ")
            print()
            
            
    #  floyd warshall algorithm
    def floyd_warshallSP(self):
        dist = [row[:] for row in self.graph]
        
        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
                    
        self.printSolution(dist)
        
        
# execution of the floyd warshall algorithm
vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

g1 = Graph(vertices)

# Adding 12 edges
g1.addEdge('a', 'b', 4)
g1.addEdge('a', 'c', 2)
g1.addEdge('b', 'c', 5)
g1.addEdge('b', 'd', 10)
g1.addEdge('c', 'e', 3)
g1.addEdge('d', 'f', 11)
g1.addEdge('e', 'd', 4)
g1.addEdge('e', 'f', 8)
g1.addEdge('e', 'g', 7)
g1.addEdge('f', 'h', 1)
g1.addEdge('g', 'h', 2)
g1.addEdge('h', 'i', 6)
g1.addEdge('i', 'j', 4)
g1.addEdge('j', 'a', 5)

g1.floyd_warshallSP()
