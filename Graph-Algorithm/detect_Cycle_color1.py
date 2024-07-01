# setting up the cycle for the graph using the color
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()


# class for the graph 
class Graph:
    def __init__(self,V):
        self.V = V
        self.graph = {i : [] for i in range(V)}
        
    # adding edge for the graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    # print the graph
    def printGraph(self):
        try:
            if not self.graph:
                print("Graph is empty.")
                logging.info("Graph is empty.")
            else:
                for vertex in self.graph:
                    print(vertex, "->", " -> ".join(map(str, self.graph[vertex])))
                    logging.info(f"{vertex}  ---> {self.graph[vertex]}")
        except Exception as e:
            print(e)
            logging.info(e)
            
    # module for the helper function for the graph
    def isDfsUtil(self,u,color):
        color[u] = "grey"
        
        for v in self.graph[u]:
            
            if color[v] == "grey":
                return True
            
            if color[v] == "white" and self.isDfsUtil(v,color) == True:
                return True
            
        color[u] = "black"
        return False
    
    # module for the detect function for the graph
    def cycleGraph(self):
        color = ['white'] * self.V
        
        for i in range(self.V):
            if color[i] == 'white':
                if self.isDfsUtil(i,color) == True:
                    return True
        return False
    
    
    
g1 = Graph(4)

g1.addEdge(0,1)
g1.addEdge(1,2)
g1.addEdge(2,3)

if g1.cycleGraph() == 1:
    print("the graph contains cycle.")
    logging.info("the graph contains cycle.")
else:
    print("the graph does not contain cycle.")
    logging.info("the graph does not contain cycle.")
