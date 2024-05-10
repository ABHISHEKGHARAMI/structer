import networkx as nx
import os
import matplotlib.pyplot as plt
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging

setup_logging()

class UGraph:
    def __init__(self):
        self.graph = {}
        
        
    # here goes the adding the edge
    def addEdge(self,u,v):
        try:
            # for directed graph have to add two edges for the connection
            if u not in self.graph:
                self.graph[u] = []
            else:
                self.graph[u].append(v)
                
            if v not in self.graph:
                self.graph[v] = []
            else:
                self.graph[v].append(u)
                
            
        except Exception:
            print(e)
            logging.info(e)
            raise Exception
        
        
    # printing the graph
    def printGraph(self):
        if not self.graph:
            print("Graph is empty.")
            logging.info("Graph is empty.")
        else:
            for vertex in self.graph:
                print(vertex, "->", " -> ".join(map(str, self.graph[vertex])))
                logging.info(f"{vertex}  ---> {self.graph[vertex]}")
                
                
if __name__=="__main__":
    g1 = UGraph()
    g1.addEdge('a','b')
    g1.addEdge('a','c')
    g1.addEdge('b','f')
    g1.addEdge('c','d')
    
    g1.printGraph()
