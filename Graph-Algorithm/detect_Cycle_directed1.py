# setting up the logger
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()


# stack class
class Stack:
    def __init__(self):
        self.stack = []
        
    # push in the stack
    def push(self,data):
        self.stack.append(data)
        
        
    # is empty
    def isEmpty(self):
        if len(self.stack) == 0:
            return 1
        else:
            return 0
        
    def pop(self):
        if self.isEmpty() != 1:
            data = self.stack.pop(-1)
            return data

# graph class for detect cycle
class Graph:
    def __init__(self):
        self.graph = {}
        
        
    # adding the edges of the graph
    def addEdges(self,u,v):
        if u not in self.graph:
            self.graph[u] = []
        else:
            self.graph[u] = v
            
            
    # idea is that using modified dfs or bfs we can check cycle is present or not
    def dfs_iterative(self,start):
        try:
            visited = set()
            s1 = Stack()
            s1.push(start)
            while s1.isEmpty() != 1:
                vertex = s1.pop()
                if vertex not in visited:
                    visited.add(vertex)
                    
                    for neighbor in reversed(self.graph[vertex]):
                        if neighbor not in visited:
                            s1.push(neighbor)
                            
                        else:
                            print("The graph contains cycle.")
                            logging.info("The graph contains cycle.")
                            break
                else:
                    print("The graph contains cycle.")
                    logging.info("The graph contains cycle.")
                    break
        except Exception as e:
            print(e)
            logging.info(e)
            raise e
        
        
# checking for the main execution of the program
g1 = Graph()

g1.addEdges('a','b');
g1.addEdges('b','c');
g1.addEdges('c','a');

g1.dfs_iterative('a')


        
    