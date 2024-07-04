# setting up the logger file
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()

# setting up the graph class
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.v = len(self.vertices)
        self.index_map = {vertex : idx for idx,vertex in enumerate(self.vertices)}
        self.graph = {vertex : [] for vertex in self.vertices}
        
        
    # adding the edges of the graph
    def addEdge(self,u,v,w):
        if u and v in self.vertices:
            self.graph[u].append((v,w))
        else:
            print(f"{u} or {v} or both does not belong to the vertices")
            logging.info(f"{u} or {v} or both does not belong to the vertices")
            
            
    # print the graph 
    def printGraph(self):
        try:
            if not self.graph:
                print("Graph is empty.")
                logging.info("Graph is empty.")
            else:
                print("printing the graph.")
                logging.info("printing the graph .")
                for vertex in self.graph:
                    print(f"{vertex}: ", end="")
                    for neighbor in self.graph[vertex]:
                        print(f"{neighbor} ", end="")
                    print()
                logging.info("Graph printed successfully.")
        except Exception as e:
            print(e)
            logging.info(e)
    
    
    # printing the solution for the graph
    def printArr(self,dist):
        print("Vertex Distance from Source")
        for vertex in dist:
            print("{0}\t\t{1}".format(vertex, dist[vertex]))
            
            
    # main function for the bellman ford shortest path algorithm
    def bellman_fordSP(self,start):
        dist = { vertex : float('inf') for vertex in self.vertices }
        dist[start] = 0
        
        # first we need to relax every edge of the graph
        for _ in range(self.v - 1):
            for u in self.graph:
                for v,w in self.graph[u]:
                    if dist[u] != float('inf') and dist[u] + w  < dist[v]:
                        dist[v] = dist[u] + w
                        
        # after relaxation we  need to check again if any relaxation is possible then go for 
        # declare that negative cycle exist and there for print the graph
        for u in self.graph:
            for v,w in self.graph[u]:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    print("negative cycle exist.")
                    logging.info("negative cycle exist.")
                    return True
                
        self.printArr(dist)
        print("Negative cycle does not exist.")
        logging.info("Negative cycle does not exist.")
        return False
    
    
#main execution of the program
vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


g1 = Graph(vertices)

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

g1.printGraph()


g1.bellman_fordSP('a')

