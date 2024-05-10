import networkx as nx
import os
import matplotlib.pyplot as plt
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging


class Graph:
    def __init__(self):
        self.graph = {}
        
    
    #adding edge
    def addEdge(self,u,v):
        try:
            if u not in self.graph:
                self.graph[u] = []
            self.graph[u].append(v)
            
        except Exception as e:
            print(e)
            logging.info(e)
            raise e
        
    # print edges of the graph
    def printEdges(self):
        if not self.graph:
            print("graph is empty.")
            logging.info("graph is empty.")
        else:
            for vertex in self.graph:
                print(f"{vertex}  ---> {self.graph[vertex]}")
                logging.info(f"{vertex}  ---> {self.graph[vertex]}")
                
                
                
                
g2 = Graph()
g2.addEdge('a','b')
g2.addEdge('a','c')
g2.addEdge('b','e')
g2.addEdge('c','f')
g2.printEdges()