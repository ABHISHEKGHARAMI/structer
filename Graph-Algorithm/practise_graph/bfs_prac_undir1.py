# setting up the logger file
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging


setup_logging()

class Queue:
    def __init__(self):
        self.queue = []
        
    #push
    def push(self,data):
        self.queue.append(data)
        
    # check is empty or not
    def isEmpty(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0
        
    def pop(self):
        if self.isEmpty() != 1:
            return self.queue.pop(0)


class Graph:
    def __init__(self):
        self.graph = {}
        
        
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
            
            
    # bfs for the undirected graph
    def bfs(self,start):
        try:
            q1 = Queue()
            q1.push(start)
            visited = set()
            while q1.isEmpty() != 1:
                vertex = q1.pop()
                print(f"vertex is : {vertex}")
                logging.info(f"vertex is : {vertex}")
                visited.add(vertex)
                for _ in self.graph[vertex]:
                    if _ not in visited:
                        q1.push(_)
                        
        except Exception as e:
            print(e)
            logging.info(e)
            
            
            
G = Graph()
G.addEdge('a','b')
G.addEdge('b','c')
G.addEdge('c','d')
G.addEdge('d','e')

G.bfs('a')

