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
        
        
    # get the all vertex of the graph
    def getVertex(self):
        if self.graph:
            a = list(self.graph.keys())
            return a
        
        
    def printGraph(self):
        try:
            print("Printing the graph :")
            logging.info("Printing the graph :")
            for key,value in self.graph.items():
                print(f"Vertex is : {key} and its neighbors are : {value}")
                logging.info(f"Vertex is : {key} and its neighbors are : {value}")
        except Exception as e:
            print(e)
            logging.info(e)
            raise e
        
    # here goes the recursive approach of the dfs for graph
    def dfs_recursive(self,start,visited=None):
        try:
            if visited:
                visited = set()
            visited.add(start)
            print(f"--->{start}",end=" ")
            logging.info(f"--->{start}")
            for neighbor in self.graph[start]:
                if neighbor not in visited:
                    self.dfs_recursive(neighbor,visited)
        except Exception as e:
            print(e)
            logging.info(e)
            raise e