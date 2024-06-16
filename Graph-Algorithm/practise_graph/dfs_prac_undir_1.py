# setting up the logger file
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()

# graph for dfs
class Graph:
    def __init__(self):
        self.graph = {}
        
    #adding the edge
    def addEdge(self,u,v):
        try:
            if u not in self.graph:
                self.graph[u] = []
            self.graph[u].append(v)
            
            if v not in self.graph:
                self.graph[v] =[]
            self.graph[v].append(u)
        except Exception as e:
            print(e)
            logging.info(e)
            
    # getting the edges
    def getVertex(self):
        if not self.graph:
            return []
        else:
            a = list(self.graph.keys())
            return a
        
        
    # print the graph
    def printGraph(self):
        if not self.graph:
            print("Graph is empty.")
            logging.info("Graph is empty.")
        else:
            for vertex in self.graph:
                print(vertex, "->", " -> ".join(map(str, self.graph[vertex])))
                logging.info(f"{vertex}  ---> {self.graph[vertex]}")
                
                
    # dfs for the recursive approach
    def dfs_recursive(self,start,visited = None):
        try:
            if visited is None:
                visited = set()
            visited.add(start)
            print(f"-->{start}",end=" ")
            logging.info(f"-->{start}")
            for neighbor in self.graph[start]:
                if neighbor not in visited:
                    self.dfs_recursive(neighbor,visited)
        except Exception as e:
            print(e)
            logging.info(e)
            
            
# execution of the program
g = Graph()

g.addEdge('a','b')
g.addEdge('b','c')
g.addEdge('c','d')
g.addEdge('b','e')

print(f"the all the vertex of the graph is : {g.getVertex()}")
logging.info(f"all the vertex of the graph is : {g.getVertex()}")

g.dfs_recursive('a')