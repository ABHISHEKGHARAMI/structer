# setting up the logger file
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()


# stack for the dfs iterative
class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self,data):
        self.stack.append(data)
        
    def isEmpty(self):
        if len(self.stack) == 0:
            return 1
        else:
            return 0
        
    def pop(self):
        if self.isEmpty() != 1:
            a = self.stack.index(self.stack[-1])
            return self.stack.po(a)

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
            
    
    # using the iterative approach for the Graph
    def dfs_iterative(self,start):
        try:
            s1 = Stack()
            s1.push(start)
            visited = set()
            while s1.isEmpty() != 1:
                vertex = s1.pop()
                print(f"--->{vertex}",end=" ")
                logging.info(f"---->{vertex}")
                if vertex not in visited:
                    visited.add(vertex)
                    
                    
                    # go for all the edges for the vertex
                    for neighbor in reversed(self.graph[vertex]):
                        if neighbor not in visited:
                            s1.push(neighbor)
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


g.printGraph()


# checking for the dfs iterative
g.dfs_iterative('a')