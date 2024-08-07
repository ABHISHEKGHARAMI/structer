# logger file for the bi connected graph
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()

class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = { vertex : [] for vertex in self.vertices }
        self.time = 0
        
    # add edge for the graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    # building the util function for bi connected graph
    def isBiConnectedUtil(self,u,visited,parent,low,disc,ap):
        children = 0
        visited[u] = True
        disc[u] = self.time 
        low[u] = self.time
        self.time += 1
        
        
        for v in self.graph[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                
                if self.isBiConnectedUtil(v,visited,parent,low,disc,ap):
                    return True
                low[u] = min(low[u],low[v])
                
                if parent[u] is None and children > 1:
                    ap[u] = True
                if parent[u] is not None and low[v] >= disc[u]:
                    ap[u] = True
            elif v!=parent[u]:
                low[u] = min(low[u],disc[v])
        return ap[u]
    

    # main function for checking the bi connected graph
    def isBiConnected(self):
        visited = { vertex : False for vertex in self.vertices }
        disc = { vertex : float('Inf') for vertex in self.vertices }
        low = { vertex : float('Inf') for vertex in self.vertices }
        parent = { vertex : None for vertex in self.vertices }
        ap = { vertex : False for vertex in self.vertices }
        
        if self.isBiConnectedUtil(self.vertices[0],visited,parent,low,disc,ap):
            return False
        if any(not visited[vertex] for vertex in self.vertices):
            return False
        
        return True
    
    
    # print the graph
    def printGraph(self):
        for vertex in self.graph:
            print(f"{vertex} : {'->'.join(self.graph[vertex])}")
            logging.info(f"{vertex} : {'->'.join(self.graph[vertex])}")
                
    
    
# vertices for graph
vertices = ['a','b','c','d','e','f']

g = Graph(vertices)

g.addEdge('a', 'b')
g.addEdge('a', 'c')
g.addEdge('b', 'c')
g.addEdge('b', 'd')
g.addEdge('d', 'e')
g.addEdge('e', 'f')
g.addEdge('f', 'd')

print("Printing the graph :")
logging.info("Printing the graph :")
g.printGraph()

if g.isBiConnected():
    print("the graph is bi connected .")
    logging.info("the graph is bi connected .")
else:
    print("the graph is not bi connected .")
    logging.info("the graph is not bi connected .")
          
        