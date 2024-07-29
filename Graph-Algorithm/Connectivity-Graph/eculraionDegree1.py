# setting up the logger file
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()


# setting up the graph structure for the euclerion path and cycle
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = { vertex : [] for vertex in self.vertices }
        
        
    # adding the edge for the graph for undirected graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
        
    # util helper function for the dfs 
    def dfsUtil(self,v,visited):
        visited[v] = True
        
        # transverse the graph
        for u in self.graph[v]:
            if visited[u] == False:
                self.dfsUtil(u,visited)
                
                
    # check  for the graph is connected or not
    def isConnected(self):
        visited = { vertex : False for vertex in self.vertices }
        
        for i in self.vertices :
            if visited[i] == False and len(self.graph[i]) > 0:
                return False
        return True
    
    
    # the euclerain path 
    def isEuclerain(self):
        if self.isConnected() == False:
            return 0
        else:
            odd = 0
            for i in self.vertices:
                if len(self.graph[i]) % 2 != 0:
                    odd += 1
                    
            if odd == 0:
                return 2
            elif odd == 2:
                return 1
            elif odd > 2:
                return 0
            
            
    # test for the path or cycle
    def eTest(self):
        res = self.isEuclerain()
        if res == 0:
            print(f"The graph is not euclerian path.")
            logging.info(f"the graph is not euclerian path.")
        elif res == 1:
            print(f"The graph has a euclerian path.")
            logging.info(f"The graph has a euclerian path.")
        else:
            print(f"The graph has a euclerian cycle.")
            logging.info(f"The graph  has a euclerian cycle.")
            
            
vertices = ['a','b','c','d','e']

g1 = Graph(vertices)

g1.addEdge('a', 'b')
g1.addEdge('a', 'c')
g1.addEdge('b', 'c')
g1.addEdge('c', 'd')


g1.eTest()

