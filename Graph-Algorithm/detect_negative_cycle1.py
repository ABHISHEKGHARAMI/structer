# setting up the logger file
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
        self.graph = {vertex : [] for vertex in self.vertices}
        
        
    # adding the edge
    def addEdge(self,u,v,w):
        if u in self.graph:
            self.graph[u].append((v,w))
        else:
            print(f"{v} is not a  vertex of the graph.")
            logging.info(f"{v} is not a vertex of the graph.")
            
            
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
            
            
    # bellman ford negative cycle for checking the graph
    def detectNegativeCycle(self,src):
        dist = { vertex : float('inf') for vertex in self.graph}
        dist[src] = 0
        
        # first relaxation for the graph and going for the shortest path for the graph
        for _ in range(self.v - 1):
            for u in self.graph:
                for v,w in self.graph[u]:
                    if dist[v] != float('inf') and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
        
        # after that go for declaration for the negative cycle for the graph
        for u in self.graph:
            for v,w in self.graph[u]:
                if dist[v] != float('inf') and dist[u] + w < dist[v]:
                    print("the graph contains the negative cycle.")
                    logging.info("the graph contains the negative cycle")
                    return True
        
        # final declaration for the garph
        print("the graph does not contains cycle.")
        logging.info("the graph does not contains cycle.")
        return False
        
        
# main execution for the program
vertices = ['a','b','c','d']

g1 = Graph(vertices)

g1.addEdge('a', 'b', 1)
g1.addEdge('b', 'c', 3)
g1.addEdge('c', 'd', -2)
g1.addEdge('d', 'b', -1)

g1.printGraph()


g1.detectNegativeCycle('a')
        
        
            
            
            