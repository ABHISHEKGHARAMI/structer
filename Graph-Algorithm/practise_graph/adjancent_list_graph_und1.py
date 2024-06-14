# setting up the logger file
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging


setup_logging()


class Graph:
    def __init__(self):
        self.graph = {}
        
        
    # add Edge
    def addEdge(self,src,dest):
        if src not in self.graph:
            self.graph[src] = []
        
        self.graph[src].append(dest)
        
        
        # adding the reverse edge for the undirected graph
        if dest not in self.graph:
            self.graph[dest] = []
      
        self.graph[dest].append(src)
            
    # print the graph
    def printEdges(self):
        if not self.graph:
            print("graph is empty.")
            logging.info(f"the graph is empty.")
        else:
            for vertex in self.graph:
                print(vertex, "->", " -> ".join(map(str, self.graph[vertex])))
                logging.info(f"{vertex}  ---> {self.graph[vertex]}")
                
                
# for testing
G = Graph()

'''while True:
    print("1:for add vertex 2: print vertex." )
    choice = int(input("enter choice"))
    if choice == 1:
        src,dest = map(str,input("enter two string with comma").split(","))
        G.addEdge(src,dest)
    elif choice == 2:
        print("printing the graph.")
        logging.info("printing the graph.")
        G.printEdges()
    elif choice == 0:
        exit(0)
    else:
        print("wrong choice.")'''
        
G.addEdge('a','b')
G.addEdge('b','c')
G.printEdges()
print(f"the vertex of the graph is : {G.graph.keys()}")