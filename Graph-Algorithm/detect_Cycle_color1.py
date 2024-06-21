# setting up the cycle for the graph using the color
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()


# Graph class
class Graph:
    def __init(self,V):
        self.V = V
        self.graph = {}
        
    # adding edge for the graph
    def addEdge(self,u,v):
        try:
            if u not in self.graph:
                self.graph[u] = []
            self.graph[u].append(v)
        except Exception as e:
            print(e)
            logging.info(e)
            raise e