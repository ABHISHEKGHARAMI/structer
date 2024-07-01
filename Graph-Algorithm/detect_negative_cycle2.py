# setting up the logger file
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()

# class for the graph
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.v = len(self.vertices)
        self.index_map = { vertex : idx for idx,vertex in enumerate(self.vertices)}
        self.graph = [[float('inf')] for _ in range(self.v)]
        
        # create for the diagonal for the zero
        for i in range(self.v):
            self.graph[i][i] = 0
        
    # adding the edge  for the graph
    def addEdge(self,u,v,w):
        if u in self.vertices and v in self.vertices:
            u_idx = self.index_map[u]
            v_idx = self.index_map[v]
            self.graph[u_idx][v_idx] = w
        else:
            print(f"{u} or {v} not present in the vertices")
            logging.info(f"{u} or {v} not present in the vertex .")
            
    # print the graph 
    def printGraph(self):
        try:
            if not self.graph:
                print("Graph is empty.")
                logging.info("Graph is empty.")
            else:
                for i in range(self.v):
                    for j in range(self.v):
                        if self.graph[i][j] == float('inf'):
                            print("INF", end="\t")
                        else:
                            print(self.graph[i][j], end="\t")
                    print()
                logging.info("Graph printed successfully.")
        except Exception as e:
            print(e)
            logging.info(e)
    
    
    # floyd warshall for the graph
    def floydWarshall(self):
        dist = self.graph
        
        # count the shortest path for the negative cycle
        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    if dist[i][k] != float('inf') and dist[k][j] != float('inf') and dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        
        # check for the negative cycle
        for i in range(self.v):
            if dist[i][i]<0:
                print("graph contains the negative cycle.")
                logging.info("graph contains the negative cycle.")
        print("the graph does not contain the negative cycle.")
        logging.info("the graph does not contain the negative cycle.")
        
        
# main execution for the cycle

vertices = ['a','b','c','d']

g1 = Graph(vertices)

g1.addEdge('a', 'b', 1)
g1.addEdge('b', 'c', 3)
g1.addEdge('c', 'd', -2)
g1.addEdge('d', 'b', -3)
g1.printGraph()

g1.floydWarshall()
                        
                        
            