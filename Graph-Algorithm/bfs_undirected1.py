# setting up the logger
import networkx as nx
import os
import matplotlib.pyplot as plt
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()


class Queue:
    def __init__(self):
        self.queue = []
        
    def push(self,data):
        if data:
            print(f"{data} inserting in the queue.")
            logging.info(f"{data} inserting in the queue.")
            self.queue.append(data)
            
    # pop operation
    def pop(self):
        if self.isEmpty() != 1:
            return self.queue.pop(0)
    
    def isEmpty(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0
        
        
# Graph class for the Undirected graph
class UGraph:
    def __init__(self):
        self.graph = {}
        
    # add edge for the graph
    def addEdge(self,u,v):
        try:
            if u not in self.graph:
                self.graph[u] = []
            self.graph[u].append(v)
            
            
            if v not in self.graph:
                self.graph[v] = []
            self.graph[v].append(u)
        except Exception as e:
            print(e)
            logging.info(e)
            raise e