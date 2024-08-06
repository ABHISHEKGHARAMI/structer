# setting up the logger file
import sys
sys.path.append("/home/abhishek/Documents/DataStructure&Algorithm/structer")
from settings import setup_logging

import logging
setup_logging()

# setting up the graph class
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = { vertex : {} for vertex in self.vertices }
        self.flow  = { vertex : {} for vertex in self.vertices }
        self.ROW = len(self.vertices)
        
    # adding edge for the graph
    def addEdge(self,u,v,capacity):
        if u in self.graph and v in self.graph:
            self.graph[u][v] = capacity
        
            if v not in self.graph[u]:
                self.graph[u][v] = 0
            
            if u not in self.graph[v]:
                self.graph[v][u] = 0
                
            if u not in self.flow[v]:
                self.flow[v][u] = 0
            
            if u not in self.flow:
                self.flow[u] = {}
            
            if v not in self.flow[u]:
                self.flow[u][v] = 0
            
        else:
            print(f"either {u} or {v} or both not in the graph.")
            logging.info(f"either {u} or {v} or both not in the graph.")
            
    def BFS(self,source,sink,parent):
        visited = { vertex : False for vertex in self.vertices }
        queue = []
        
        queue.append(source)
        visited[source] = True
        
        
        while queue:
            u = queue.pop(0)
            
            for v , capacity in self.graph[u].items():
                if visited[v] != True and capacity>0:
                    queue.append(v)
                    parent[v] = u
                    
        
        return True if visited[sink] else False
    
    
    # adding the ford fulkerson method for the max flow
    
        
        
        