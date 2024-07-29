# set up the logger 
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()


# class for Graph
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = { vertex : [] for vertex in self.vertices }
        self.time = 0
        
    # add edge for the Graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    # util for the Graph for the bridge
    def isBridgeUtil(self,u,visited,parent,low,disc):
        visited[u] = True
        disc[u] = self.time
        low[u] = self.time
        self.time += 1
        
        
        # transverse the graph
        for v in self.graph[u]:
            if visited[v] == False:
                parent[v] = u
                self.isBridgeUtil(v,visited,parent,low,disc)
                
                low[u] = min(low[u],low[v])
                
                if low[v] > disc[u]:
                    print(f"{u} -> {v}")
                    logging.info(f"{u} ->{v}")
                    
            elif v != parent[u]:
                low[u] = min(low[u],disc[v])
                
    # bridge of the graph
    def bridgeComp(self):
        visited = { vertex : False for vertex in self.vertices }
        disc = { vertex : float('Inf') for vertex in self.vertices }
        low = { vertex : float('Inf') for vertex in self.vertices }
        parent = { vertex : None for vertex in self.vertices }
        
        for vertex in self.vertices:
            if visited[vertex] == False:
                self.isBridgeUtil(vertex,visited,parent,low,disc)
                
    
    # print the graph
    def printGraph(self):
        print("Printing of the Graph :")
        logging.info("Printing of the Graph :")
        for vertex in self.graph:
            print(f"{vertex} : {'->'.join(self.graph[vertex])}")
            logging.info(f"{vertex} : {'->'.join(self.graph[vertex])}")
                
                

# main function
vertices = ['a','b','c','d']

g = Graph(vertices)

g.addEdge('a','b')
g.addEdge('b','c')
g.addEdge('c','d')

g.printGraph()

# print the graph
print("printing the bridge :")
logging.info("printing the bridge :")

g.bridgeComp()


                