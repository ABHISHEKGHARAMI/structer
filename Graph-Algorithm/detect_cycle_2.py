# setting up the cycle for the graph using the color
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()


# graph class
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.v = len(self.vertices)
        self.graph = { vertex: [] for vertex in self.vertices}
        
        
    # add edge for the graph
    def addEdge(self,u,v):
        if u in self.graph and v in self.graph:
            self.graph[u].append(v)
            
    # print the graph
    def printGraph(self):
        try:
            if not self.graph:
                print("Graph is empty.")
                logging.info("Graph is empty.")
            else:
                for vertex in self.graph:
                    print(vertex, "->",
                          " -> ".join(map(str, self.graph[vertex])))
                    logging.info(f"{vertex}  ---> {self.graph[vertex]}")
        except Exception as e:
            print(e)
            logging.info(e)
            
    # detect cycle for util function
    def isDfsUtil(self,u,color):
        color[u] = "grey"
        
        for v in self.graph[u]:
            if color[v] == "grey":
                return True
            if color[v] == "white" and self.isDfsUtil(v,color) == True:
                return True
            
        color[u] = "black"
        return False
    
    
    
    # detect cycle using color for main function
    def detectCycle(self):
        color = {vertex : "white" for vertex in self.vertices}
        
        for vertex in self.vertices:
            if color[vertex] == "white":
                if self.isDfsUtil(vertex,color):
                    return True
            
        return False



# checking the execution of the function
vertices = ['a','b','c','d']

g1 = Graph(vertices)

g1.addEdge('a','b')
g1.addEdge('b','c')
g1.addEdge('c','d')
g1.addEdge('d','a')

if g1.detectCycle() == 1:
    print("This graph contains the cycle")
    logging.info("this graph contains the cycle.")
else:
    print("this graph does not contain cycle.")
    logging.info("this graph does not contain cycle.")