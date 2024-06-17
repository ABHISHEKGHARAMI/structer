# setting up the logger
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()

# class for the Queue
class Queue:
    def __init__(self):
        self.queue = []
        
    def push(self,data):
        logging.info(f"{data} added in to queue.")
        self.queue.append(data)
        
        
    def pop(self):
        if self.isEmpty() != 1:
            pos = self.queue.index(self.queue[-1])
            return self.queue.pop(self.queue[pos])
    
    def isEmpty(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0
        
# class for the stack
class Stack:
    def __init__(self):
        self.stack = []
        
    # push for data
    def push(self,data):
        logging.info(f"{data} inserted for the stack.")
        self.stack.append(data)
        
    def isEmpty(self):
        if len(self.stack) == 0:
            return 1
        else:
            return 0
        
    def pop(self):
        if self.isEmpty() != 1:
            return self.stack.pop(-1)
# class for the graph
class Graph:
    def __init__(self):
        self.graph = {}
        
    # adding edge
    def addEdge(self,u,v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        
        # reverse the connection
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)
        
    # printing the  graph
    def printGraph(self):
        try:
            if not self.graph:
                print("Graph is empty.")
                logging.info("Graph is empty.")
            else:
                for vertex in self.graph:
                    print(vertex, "->", " -> ".join(map(str, self.graph[vertex])))
                    logging.info(f"{vertex}  ---> {self.graph[vertex]}")
        except Exception as e:
            print(e)
            logging.info(e)
            
            
    # get the graph vertex
    def getVertex(self):
        try:
            a = self.graph.keys()
            return list(a)
        except Exception as e:
            print(e)
            logging.info(e)
            
            
    # bfs for the graph
    def bfs(self,start):
        try:
            q1 = Queue()
            q1.push(start)
            visited = set()
            while q1.isEmpty() != 1:
                vertex = q1.pop()
                print(f"->{vertex}",end=" ")
                logging.info(f"->{vertex}")
                visited.add(vertex)
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        q1.push(neighbor)
        except Exception as e:
            print(e)
            logging.info(e)