# setting up the logger file
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()

class Graph:
    
    def __init__(self):
        self.graph = {}
        
        
    # adding the edge for the undirected graph
    def addEdge(self,u,v):
        
        try:
            if u not in self.graph:
                self.graph[u] = []
            self.graph[u].append(v)
            
            
            # connecting the ede for the undirected graph
            if v not in self.graph:
                self.graph[v] = []
            self.graph[v].append(u)
        except Exception as e:
            print(e)
            logging.info(e)
            raise e